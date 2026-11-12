# Bab 11: Pustaka Skrip Ekstraksi Bukti Teknis (Live Audit Queries) — SAP ERP/S4HANA, Active Directory, Cloud (AWS/Azure/GCP), dan Kubernetes/CI-CD

> **Cakupan Materi:** Bab ini memperluas panduan teknis *walkthrough* di Bab 10 ke platform enterprise modern yang paling sering diaudit oleh praktisi CISA/Big-4:
> 1. **SAP ERP (ECC 6.0 & S/4HANA):** *Transaction Codes (T-Codes)*, Tabel Sistem, Objek Otorisasi Kritis, dan Parameter Profil Keamanan.
> 2. **Windows Server & Active Directory (AD / Entra ID):** Perintah PowerShell *read-only* untuk mengekstrak bukti *Domain Admins*, akun *dormant*, dan kebijakan *Group Policy*.
> 3. **Cloud Security Audit (AWS, Microsoft Azure, Google Cloud Platform):** Pemeriksaan IAM, *Storage Bucket*, enkripsi KMS, dan *CloudTrail/Activity Logs*.
> 4. **Container, Kubernetes, & CI/CD Pipeline Audit:** Pemeriksaan *Docker*, *Kubernetes RBAC*, dan kontrol pemisahan tugas pada *GitHub Actions / GitLab CI*.

---

## 11.1 Panduan Audit Teknis SAP ERP (ECC 6.0 & S/4HANA)

Dalam audit ITGC maupun ITAC pada lingkungan **SAP**, auditor SI tidak boleh hanya meminta tangkapan layar sepotong-sepotong, melainkan harus memahami **T-Code (Transaction Code)**, **Tabel Database SAP**, dan **Parameter Konfigurasi** yang menjadi sumber bukti populasi (*system-generated report*).

### A. Matriks T-Codes & Tabel SAP Wajib bagi IS Auditor

| Area Kontrol ITGC / ITAC | SAP T-Code (Transaction Code) | Tabel Database SAP (`SE16` / `SE16N`) | Apa yang Harus Diperiksa oleh IS Auditor? |
| :--- | :--- | :--- | :--- |
| **1. Administrasi Pengguna & Akun Aktif (`SOXIT.03`)** | • **`SU01`** *(User Maintenance — Display)*<br>• **`SUIM`** *(User Information System)* | • **`USR02`** *(Logon Data, User Type, Lock Status, Validity Date)*<br>• **`USER_ADDR`** *(Nama Lengkap & Departemen)* | • Tarik populasi `USR02` untuk memeriksa kolom `UFLAG` (Status kunci: `0`=Tidak terkunci, `64`=Dikunci Admin, `128`=Dikunci karena salah password), `GLTGV`/`GLTGB` (Tanggal berlaku), `USTYP` (`A`=Dialog, `B`=System, `C`=Communication), dan `TRDAT` (*Last Logon Date* untuk mendeteksi akun *dormant* $> 90$ hari & akun karyawan yang telah *resign*). |
| **2. Profil Superuser (`SAP_ALL` & `SAP_NEW`)** | • **`SUIM`** $\rightarrow$ *Users by Complex Selection Criteria* $\rightarrow$ *By Profiles* | • **`UST04`** *(User Masters — Profiles)*<br>• **`AGR_USERS`** *(Assignment of Roles to Users)* | • Identifikasi seluruh pengguna yang memegang profil **`SAP_ALL`**, **`SAP_NEW`**, **`S_A.SYSTEM`**, atau peran *Basis Admin*.<br>• Pastikan tidak ada pengguna bisnis atau ABAP Developer yang memegang `SAP_ALL` di klien Produksi! |
| **3. Pemeliharaan Role & Objek Otorisasi Kritis** | • **`PFCG`** *(Role Maintenance)*<br>• **`SU24`** *(Authorization Object Check Indicators)* | • **`AGR_1251`** *(Authorization Data for Activity Group)*<br>• **`AGR_DEFINE`** | • Periksa siapa saja yang memiliki objek otorisasi berbahaya:<br>  - **`S_TABU_DIS` / `S_TABU_NAM`** dengan `ACTVT = 02` (Mengubah isi tabel database secara langsung!)<br>  - **`S_DEVELOP`** dengan `ACTVT = 01/02` di Produksi (Mengubah program ABAP atau melakukan *Debugging with Replace* di Produksi!)<br>  - **`S_USER_GRP` / `S_USER_PRO` / `S_USER_AGR`** (Memberikan akses/role kepada pengguna). |
| **4. Pengaturan Keamanan Klien Produksi (*Client Opening*)** | • **`SCC4`** *(Client Administration)*<br>• **`SE06`** *(System Change Option)* | • **`T000`** *(Clients Table)*<br>• **`TADIR`** | • Pada klien Produksi di tabel `T000` (`SCC4`), pastikan pengaturan *Changes and Transports for Client-Specific Objects* disetel ke **"No changes allowed" (`CCCORACTIV = 2`)** dan *Cross-Client Object Changes* disetel ke **"No changes to repository and cross-client customizing objs"**. Jika *client* dibuka di produksi, periksa siapa yang membukanya dan tiket perubahan daruratnya! |
| **5. Parameter Password & Keamanan Instance (`SOXIT.03.C4`)** | • **`RZ10`** *(Maintain Profile Parameters)*<br>• **`RZ11`** *(Display Profile Parameter Attributes)*<br>• **`RSPARAM`** *(Program)* | — *(Diekstrak langsung dari laporan `RSPARAM`)* | • Verifikasi nilai parameter keamanan berikut:<br>  - `login/min_password_lng` ($\ge 8$ atau $\ge 12$)<br>  - `login/password_expiration_time` ($\le 90$ hari)<br>  - `login/fails_to_user_lock` ($3 - 5$ kali)<br>  - `login/password_history_size` ($\ge 5$)<br>  - `login/disable_multi_gui_login` (`1` = melarang login ganda)<br>  - `rdisp/gui_auto_logout` ($\le 900 - 1800$ detik *session timeout*)<br>  - `login/no_automatic_user_sapstar` (`1` = menonaktifkan akun bawaan `SAP*` dengan password `PASS`). |
| **6. Manajemen Perubahan & Transport (`SOXIT.02`)** | • **`STMS`** *(Transport Management System)*<br>• **`SE01` / `SE09` / `SE10`** *(Transport Organizer)* | • **`E070`** *(Change & Transport System: Header of Requests/Tasks)*<br>• **`E071`** *(Object Entries of Requests)* | • Tarik populasi 100% perubahan yang masuk ke Produksi dari `STMS` (*Import History*) dan tabel `E070` (`TRSTATUS = 'R'` Released).<br>• Pastikan pengguna yang mengeksekusi *Import Transport* ke Produksi (objek `S_CTS_ADMI`) adalah **SAP Basis**, bukan ABAP Developer yang membuat kode (`AS4USER` di `E070` $\ne$ *Importer* di `STMS`)! |
| **7. Jejak Audit Keamanan & Emergency / Firefighter (`SOXIT.03.C5`)** | • **`SM19` / `RSAU_CONFIG`** *(Security Audit Log Configuration)*<br>• **`SM20` / `RSAU_READ_LOG`** *(Read Security Audit Log)*<br>• **`GRAC_SPM`** *(SAP GRC Firefighter)* | — | • Pastikan *Security Audit Log* (`SM19`) aktif (`rsau/enable = 1`) dan mencatat *critical events* (login gagal, transaksi dimulai, perubahan user).<br>• Untuk setiap penggunaan akun darurat (*Firefighter / FireCall ID*), periksa log `SM20` dan bukti *sign-off review* oleh pemilik kontrol. |
| **8. Penjadwalan Batch Job Produksi (`SOXIT.04`)** | • **`SM36`** *(Define Background Job)*<br>• **`SM37`** *(Overview of Job Selection)* | • **`TBTCO`** *(Job Status Overview Table)* | • Periksa hak akses pembuatan/pengubahan *batch job* (`S_BTCH_ADM` / `S_BTCH_JOB`) dan periksa daftar *job* berstatus `Canceled/Aborted` di `SM37` / tabel `TBTCO` beserta tiket penyelesaiannya. |
| **9. Kontrol Aplikasi Keuangan & Pengadaan (ITAC — Modul FI & MM)** | • **`OB52`** *(Open and Close Posting Periods)*<br>• **`OMWB` / `OBYC`** *(Automatic Account Determination)*<br>• **`FK08`** *(Confirm Vendor Master Changes)* | • **`T001B`** *(Permitted Posting Periods)*<br>• **`CDHDR` & `CDPOS`** *(Change Document Header & Items)* | • Pastikan periode pembukuan akuntansi bulan lalu telah ditutup di `OB52` (`T001B`), perubahan *Master Data Rekening Bank Vendor* memerlukan konfirmasi pihak kedua (`FK08`), dan *Three-Way Matching* (PO = GR = Invoice) ditegakkan dengan batas toleransi di modul MM. |

---

## 11.2 Skrip Ekstraksi Bukti Active Directory (AD) & Windows Server (PowerShell Read-Only)

Saat mengaudit infrastruktur Windows Server / Active Directory Domain Services (AD DS), mintalah administrator menjalankan perintah PowerShell *read-only* berikut di hadapan auditor (atau melalui sesi *screen-sharing* dengan mencantumkan `Get-Date` dan `hostname`):

```powershell
# 1. Bukti Konteks Waktu, Nama Server, & Kebijakan Password Domain (SOXIT.03.C4)
hostname; Get-Date; Get-ADDefaultDomainPasswordPolicy | Select-Object ComplexityEnabled, MinPasswordLength, MaxPasswordAge, MinPasswordAge, PasswordHistoryCount, LockoutThreshold, LockoutDuration

# 2. Daftar Seluruh Anggota Grup Berhak Istimewa (Domain Admins, Enterprise Admins, Schema Admins) (SOXIT.03.C5)
"Domain Admins","Enterprise Admins","Schema Admins","Administrators" | ForEach-Object {
    Get-ADGroupMember -Identity $_ -Recursive | Select-Object @{N="Group";E={$_}}, Name, SamAccountName, objectClass
} | Export-Csv -Path .\AD_Privileged_Accounts.csv -NoTypeInformation

# 3. Deteksi Akun Aktif yang Password-nya Tidak Pernah Kedaluwarsa (PasswordNeverExpires = True)
Get-ADUser -Filter 'Enabled -eq $true -and PasswordNeverExpires -eq $true' -Properties PasswordNeverExpires, LastLogonDate, WhenCreated, Department |
    Select-Object Name, SamAccountName, Department, WhenCreated, LastLogonDate, PasswordNeverExpires |
    Export-Csv -Path .\AD_PasswordNeverExpires.csv -NoTypeInformation

# 4. Deteksi Akun Dormant / Tidak Aktif Login > 90 Hari namun Masih Enabled (SOXIT.03.C3 & C6)
$cutoff = (Get-Date).AddDays(-90)
Get-ADUser -Filter 'Enabled -eq $true' -Properties LastLogonDate, WhenCreated, Department, Title |
    Where-Object { ($_.LastLogonDate -lt $cutoff -or $null -eq $_.LastLogonDate) -and $_.WhenCreated -lt $cutoff } |
    Select-Object Name, SamAccountName, Department, Title, WhenCreated, LastLogonDate |
    Export-Csv -Path .\AD_Dormant_Active_Users.csv -NoTypeInformation
```

---

## 11.3 Panduan Audit Keamanan Cloud (AWS, Microsoft Azure, Google Cloud Platform)

Ketika aplikasi dan database di-*hosting* di *Cloud* publik, fokus pemeriksaan teknis ITGC bergeser ke **Control Plane IAM, Network Security Groups, Storage Encryption, dan Cloud Audit Logging**:

| Kontrol Kunci Cloud | AWS (Amazon Web Services) | Microsoft Azure | Google Cloud Platform (GCP) | Kriteria Lulus Audit CISA |
| :--- | :--- | :--- | :--- | :--- |
| **1. Perlindungan Akun Root / Global Admin & MFA** | `aws iam get-account-summary` & `aws iam generate-credential-report` | *Entra ID Global Administrators* & *Conditional Access Policies* | *Organization Admins* & *Super Admin MFA Enforcement* | • Akun *Root* tidak memiliki *Access Keys* aktif, wajib dilindungi **Hardware/FIDO2 MFA**, dan tidak digunakan untuk operasional harian.<br>• $100\%$ pengguna konsol wajib menggunakan MFA. |
| **2. Pembatasan Hak Istimewa (`*:*` / Owner)** | Kebijakan IAM dengan `"Action": "*", "Resource": "*"` (`AdministratorAccess`) | Peran `Owner` atau `Contributor` pada level *Subscription* | Peran primitif `roles/owner` dan `roles/editor` | • Dilarang memberikan izin *wildcard* `*:*` pada akun servis aplikasi (*Service Accounts*).<br>• Kunci akses (*IAM Access Keys*) wajib dirotasi minimal setiap **90 hari**. |
| **3. Keamanan Penyimpanan Objek & Enkripsi (Data at Rest)** | **S3 Block Public Access**, enkripsi **AWS KMS** pada S3, EBS, dan RDS | *Storage Account AllowBlobPublicAccess = False*, *Azure Key Vault* | *Cloud Storage Public Access Prevention = Enforced*, *Cloud KMS* | • Seluruh *bucket* penyimpanan diblokir dari akses publik (*Block Public Access*) dan dienkripsi menggunakan AES-256 (KMS). |
| **4. Firewall Jaringan Virtual (Security Groups / NSG)** | `aws ec2 describe-security-groups` | *Network Security Groups (NSG)* & *Azure Firewall* | *VPC Firewall Rules* & *Cloud Armor* | • **Dilarang keras** membuka *port* manajemen (`SSH 22`, `RDP 3389`, atau *Database Port* `1433/1521/3306/5432`) ke seluruh internet (`0.0.0.0/0`)! |
| **5. Jejak Audit Cloud (Immutable Logging)** | **AWS CloudTrail** (*Multi-Region* + *Log File Validation* aktif) | *Azure Monitor Activity Log* & *Microsoft Sentinel* | *Cloud Audit Logs (Admin Activity & Data Access)* | • Log aktivitas *Control Plane* wajib diaktifkan di seluruh *region*, dilindungi validitas *hash*-nya, dan dikirim ke akun penyimpanan keamanan terpisah (*Log Archive Account*). |

---

## 11.4 Audit Container (Docker/Kubernetes) & Pipeline CI/CD (DevSecOps)

1. **Kontrol Keamanan Container & Kubernetes (K8s):**
   - **Larangan Menjalankan Container sebagai `root`:** Di dalam `Dockerfile` dan *Kubernetes Pod Security Standards*, pastikan `runAsNonRoot: true` dan `privileged: false` (mencegah *Container Escape* ke *Host OS*).
   - **Image Scanning & Trusted Registry:** Seluruh *container image* harus dipindai kerentanannya (misal menggunakan Trivy/Snyk) dan ditandatangani secara kriptografis (*Cosign*) sebelum diizinkan masuk ke klaster Kubernetes produksi.
   - **Secrets Management:** Kredensial database dan *API Key* **dilarang keras ditulis secara *hardcoded* di dalam *source code*, `Dockerfile`, atau variabel lingkungan teks terbuka** — wajib ditarik secara dinamis dari *Vault / Cloud Secrets Manager*.
2. **Kontrol Segregation of Duties (SoD) pada Pipeline CI/CD (GitHub / GitLab):**
   - Periksa pengaturan **Branch Protection Rules** pada cabang `main` / `production`:
     - `Require a pull request before merging` = **Enabled**
     - `Require approvals` = **Minimal 1 atau 2 orang (Author tidak boleh menyetujui PR miliknya sendiri!)**
     - `Dismiss stale pull request approvals when new commits are pushed` = **Enabled** (agar developer tidak bisa menyisipkan kode baru setelah PR disetujui!)
     - `Require status checks to pass before merging` (Unit Test, SAST, SCA lulus) = **Enabled**
     - `Do not allow bypassing the above settings` (Termasuk untuk Administrator repositori) = **Enabled**.
