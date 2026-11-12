# Bab 12: Panduan Fokus Area COBIT 2019 (Focus Area Guides) — Keamanan Informasi, Risiko TI (CRISC), DevOps, Cloud, dan UMKM (SME)

> **Cakupan Materi:** Bab ini mengkodifikasi suplemen resmi **ISACA COBIT® 2019 Focus Area Guides** yang memperluas kerangka kerja inti COBIT 2019 (`Design Factor 5–11`) ke dalam 5 domain spesifik:
> 1. **COBIT Focus Area: Information Security** (Integrasi ISMS, CISO, dan *Cyber Defense*)
> 2. **COBIT Focus Area: IT Risk** (Integrasi metodologi **ISACA CRISC™** dan *Risk Scenarios*)
> 3. **COBIT Focus Area: DevOps** (Tata kelola CI/CD, *Automated Gatekeepers*, dan SoD Modern)
> 4. **COBIT Focus Area: Cloud Computing** (*Shared Responsibility Matrix* IaaS/PaaS/SaaS & FinOps)
> 5. **COBIT Focus Area: Small and Medium Enterprises (SME)** (Penyederhanaan tata kelola untuk organisasi ramping).

---

## 12.1 COBIT 2019 Focus Area: Information Security (Keamanan Informasi)

Panduan *COBIT Focus Area: Information Security* menjembatani tata kelola eksekutif dengan operasional keamanan siber teknis (selaras dengan **ISO/IEC 27001:2022** dan **NIST CSF 2.0**).

### A. Objektif Inti & Target Kapabilitas Keamanan Informasi
Ketika organisasi memiliki profil risiko keamanan tinggi (*Design Factor 3 — Cyberattack, Data Breach, Insider Threat*), 6 objektif berikut menjadi tulang punggung sistem tata kelola keamanan informasi:

| Kode Objektif | Peran Spesifik dalam Fokus Area Information Security | Target Kapabilitas (Baseline vs. High-Risk) |
| :---: | :--- | :---: |
| **`EDM03`** *(Ensured Risk Optimization)* | Dewan menetapkan *Information Security Risk Appetite*, menyetujui piagam keamanan siber, dan memantau eksposur risiko kebocoran data korporat. | Level 3 $\rightarrow$ **Level 4** |
| **`APO12`** *(Managed Risk)* | Memelihara *Cyber Risk Register*, melakukan penilaian risiko aset informasi secara kuantitatif/kualitatif, dan menyusun skenario ancaman siber. | Level 3 $\rightarrow$ **Level 4** |
| **`APO13`** *(Managed Security)* | Menetapkan dan memelihara **Information Security Management System (ISMS)**, kebijakan klasifikasi informasi, rencana perlakuan risiko (*Risk Treatment Plan* / SoA), serta program kesadaran keamanan (*Security Awareness*). | Level 3 $\rightarrow$ **Level 4/5** |
| **`DSS05`** *(Managed Security Services)* | Mengoperasikan kontrol keamanan teknis harian: perlindungan *endpoint/antimalware* (`DSS05.01`), keamanan jaringan/firewall/IDS/IPS (`DSS05.02`), manajemen identitas & akses/IAM (`DSS05.04`), keamanan fisik (`DSS05.05`), dan pemantauan SIEM/SOC (`DSS05.07`). | Level 3 $\rightarrow$ **Level 4/5** |
| **`DSS02` & `DSS04`** *(Incidents & Continuity)* | Mengelola respons insiden keamanan siber (*CSIRT Playbooks*, *Containment*, *Forensics*) dan pemulihan bencana (*Ransomware Immutable Backup Recovery*). | Level 3 $\rightarrow$ **Level 4** |
| **`MEA02` & `MEA04`** *(Internal Control & Assurance)* | Melaksanakan *Vulnerability Assessment*, *Penetration Testing*, *Red Teaming* independen, dan audit kepatuhan keamanan informasi. | Level 3 $\rightarrow$ **Level 4** |

### B. Artefak Informasi Wajib (Component C — Information Flows)
1. **Information Security Charter & Policy Architecture** (`APO01` / `APO13`)
2. **Statement of Applicability (SoA) & Risk Treatment Plan** (`APO12` / `APO13`)
3. **Privileged Access & SoD Matrix** (`DSS05.04`)
4. **Key Risk Indicators (KRIs) & Security Operations Dashboard** (`EDM03` / `MEA01`)

---

## 12.2 COBIT 2019 Focus Area: IT Risk (Integrasi ISACA CRISC™)

Fokus area **IT Risk** memperdalam objektif **`EDM03`** dan **`APO12`** menggunakan metodologi **ISACA Certified in Risk and Information Systems Control (CRISC)**:

```
[1. Risk Identification] ──► [2. Risk Assessment] ──► [3. Risk Response & Mitigation] ──► [4. Risk & Control Monitoring]
 (Skenario Risiko Top-Down   (Frekuensi/Likelihood x   (Avoid, Mitigate, Share/Transfer,   (Key Risk Indicators [KRI],
  & Bottom-Up, Risk Owner)    Besaran Dampak/SLE/ALE)   Accept sesuai Risk Appetite)        Key Control Indicators [KCI])
```

### A. Metodologi Penyusunan Skenario Risiko TI (IT Risk Scenarios)
Setiap risiko dalam **IT Risk Register (`APO12.03`)** wajib dirumuskan menggunakan struktur **5 Elemen Skenario Risiko COBIT**:
1. **Actor (Aktor Ancaman):** Internal (*malicious insider, staf lalai*) vs. Eksternal (*APT group, ransomware syndicate, vendor gagal*).
2. **Threat Type (Jenis Ancaman):** *Malicious* (berniat jahat), *Accidental* (tidak sengaja/human error), *Failure* (kegagalan perangkat/sistem), atau *Natural* (bencana alam).
3. **Event (Kejadian Risiko):** Pengungkapan data rahasia (*Disclosure*), penghentian layanan (*Interruption*), modifikasi tidak sah (*Modification*), pencurian/kerusakan (*Theft/Destruction*), atau kegagalan proyek/desain.
4. **Asset / Resource (Aset Terdampak):** Aplikasi inti, database pelanggan, infrastruktur jaringan, SDM kunci, atau proses SDLC.
5. **Timing & Duration (Dimensi Waktu):** Apakah terjadi pada periode kritis (misal tutup buku akhir tahun/jam bursa) dan berapa lama durasi pemulihannya (*melampaui RTO/MTD*).

### B. Perbedaan Metrik KGI, KPI, KRI, dan KCI dalam Audit Risiko COBIT

| Jenis Indikator | Pertanyaan Utama yang Dijawab | Contoh Metrik Spesifik |
| :--- | :--- | :--- |
| **KGI** *(Key Goal Indicator — Lagging)* | *"Apakah tujuan proses/bisnis telah tercapai di akhir periode?"* | Persentase ketersediaan sistem *Core Banking* mencapai $99,98\%$ sepanjang tahun. |
| **KPI** *(Key Performance Indicator — Leading)* | *"Seberapa baik proses sedang berjalan untuk mencapai KGI?"* | Waktu rata-rata pemasangan *security patch* kritis (*Mean Time to Patch* $\le 48$ jam). |
| **KRI** *(Key Risk Indicator — Early Warning)* | *"Apakah profil eksposur risiko sedang meningkat mendekati batas bahaya?"* | Persentase server produksi yang menjalankan OS *End-of-Life (EOL)* naik di atas $10\%$; lonjakan upaya *login* gagal pada akun admin. |
| **KCI** *(Key Control Indicator)* | *"Apakah kontrol internal yang dipasang masih berfungsi efektif?"* | Persentase karyawan yang lulus simulasi *phishing* ($> 92\%$); persentase perubahan produksi yang melewati persetujuan CAB ($100\%$). |

---

## 12.3 COBIT 2019 Focus Area: DevOps & Agile Delivery (`DF9` & `DF10`)

Ketika organisasi mengadopsi **Agile & DevOps (`Design Factor 9`)**, kontrol tradisional yang mengandalkan rapat CAB manual mingguan dan dokumen kertas berurutan (*Waterfall*) sering menjadi penghambat (*bottleneck*) atau justru dilewati oleh tim developer. COBIT 2019 Focus Area DevOps menetapkan transformasi kontrol berikut:

| Objektif COBIT | Kontrol Tradisional (Waterfall) | Transformasi Kontrol pada Lingkungan DevOps / CI-CD |
| :--- | :--- | :--- |
| **`BAI02` & `BAI03`** *(Requirements & Build)* | Spesifikasi desain fungsional ratusan halaman; *code review* manual di akhir fase. | • Kebutuhan ditulis sebagai *User Stories* dengan **Security Acceptance Criteria** di dalam *Backlog*.<br>• **Shift-Left Security:** Pengujian otomatis **SAST** (*Static Application Security Testing*), **SCA** (*Software Composition Analysis* untuk pustaka *open-source*), dan **Secret Scanning** langsung di setiap *Git Commit / Pull Request*. |
| **`BAI06`** *(Managed IT Changes)* | Persetujuan manual *Change Advisory Board (CAB)* untuk setiap tiket perubahan. | • **Automated Pipeline Gatekeepers (Policy-as-Code):** Perubahan standar (*Standard/Pre-Authorized Changes*) yang lulus 100% uji otomatis, *peer review*, dan pemindaian keamanan dapat langsung di-*deploy*, sedangkan perubahan arsitektur berisiko tinggi tetap memerlukan persetujuan manusia. |
| **`BAI07`** *(Change Acceptance & Transition)* | Pemisahan fisik di mana Librarian memindahkan kode secara manual ke produksi. | • **Penegakan Segregation of Duties (SoD) di DevOps:** Developer **TIDAK BOLEH** memiliki akses *login* langsung ke server produksi atau mengubah skrip *pipeline* CI/CD sendiri! Kode hanya boleh masuk ke produksi melalui **Automated Deployment Pipeline** dengan syarat: (1) *Branch protection rule* mewajibkan minimal **1–2 Peer Code Review Approvals** dari orang berbeda (*Four-Eyes Principle*), dan (2) Seluruh log *pipeline* bersifat *immutable*. |
| **`BAI10` & `DSS01`** *(Config & Operations)* | Konfigurasi server manual; pencatatan CMDB manual. | • **Infrastructure as Code (IaC — Terraform/Ansible)** dan **Immutable Containers (Docker/Kubernetes)** di mana perubahan konfigurasi server dilakukan melalui *version control* Git (*GitOps*). |

---

## 12.4 COBIT 2019 Focus Area: Cloud Computing (`DF8` & `DF10`)

Dalam adopsi *Cloud* (**IaaS, PaaS, SaaS**), fokus tata kelola COBIT bergeser dari pengelolaan perangkat keras fisik (`BAI09` / `DSS01.05`) ke arah **Manajemen Vendor (`APO10`), Perjanjian Layanan (`APO09`), Arsitektur (`APO03`), Pengendalian Biaya FinOps (`APO06`), dan Keamanan Cloud (`APO13`/`DSS05`)**.

### Matriks Tanggung Jawab Bersama (Cloud Shared Responsibility Matrix) & Fokus Audit COBIT

| Lapisan Kontrol | On-Premises | IaaS *(Infrastructure)* | PaaS *(Platform)* | SaaS *(Software)* | Objektif COBIT yang Tetap Menjadi Akuntabilitas Klien! |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Tata Kelola, Klasifikasi Data, & Kepatuhan Regulasi** | **Klien** | **Klien** | **Klien** | **Klien** | **`EDM01`, `EDM03`, `APO14` (Data), `MEA03` (Compliance)** — *Akuntabilitas tidak pernah bisa dialihkan ke Cloud Provider!* |
| **Manajemen Identitas, Hak Akses Pengguna (IAM/MFA), & Perangkat Endpoint** | **Klien** | **Klien** | **Klien** | **Klien** | **`DSS05.04` (Identity & Logical Access)** & **`DSS05.03` (Endpoint Security)** |
| **Konfigurasi Aplikasi & Logika Bisnis** | **Klien** | **Klien** | **Klien** | Vendor *(Klien atur parameter)* | **`BAI03`, `BAI06`, `DSS06` (Business Process Controls)** |
| **Sistem Operasi (OS), Database, & Jaringan Virtual (VPC/Security Groups)** | **Klien** | **Klien** | Vendor | Vendor | **`DSS01`, `DSS05.02`, `BAI10`** (Pada PaaS/SaaS, klien wajib mengaudit melalui **`APO10` Vendor Management & Laporan SOC 2 Type 2**). |
| **Hypervisor, Server Fisik, Storage, & Keamanan Fisik Data Center** | **Klien** | Vendor | Vendor | Vendor | **`APO09` (SLA)** & **`APO10` (Right to Audit, SOC 2 Type 2, ISO 27017/27018, Exit Strategy)**. |

---

## 12.5 COBIT 2019 Focus Area: Small and Medium Enterprises (SME / UMKM)

Untuk organisasi berskala kecil-menengah (atau anak perusahaan dengan tim TI $< 20$ orang), menerapkan seluruh 40 objektif COBIT 2019 secara penuh akan terlalu birokratis. Panduan *COBIT Focus Area: SME* menyederhanakan implementasi menjadi **14 Objektif Esensial (Core SME Set)**:

1. **Governance (`EDM`):** Fokus pada **`EDM01`** (kejelasan wewenang keputusan TI) dan **`EDM03`** (perlindungan terhadap risiko fatal seperti *ransomware* dan kehilangan data).
2. **Planning & Risk (`APO`):** Fokus pada **`APO02`** (rencana TI sederhana selaras bisnis), **`APO06`** (anggaran TI), **`APO09`/`APO10`** (pengelolaan vendor SaaS/ISP), **`APO12`** (manajemen risiko praktis), dan **`APO13`** (kebijakan keamanan dasar).
3. **Build & Change (`BAI`):** Fokus pada **`BAI02`/`BAI03`** (pemilihan solusi tepat guna), **`BAI06`** (kontrol perubahan agar tidak merusak produksi), dan **`BAI11`** (manajemen proyek).
4. **Operations & Continuity (`DSS`):** Fokus pada **`DSS01`** (operasional harian), **`DSS02`** (penanganan insiden), **`DSS04`** (*backup offsite/cloud* teruji & pemulihan bencana), dan **`DSS05`** (MFA, *patching*, antivirus, kontrol akses).
5. **Kontrol Kompensasi SoD pada SME:** Karena staf TI sedikit dan sering merangkap peran, SME wajib menerapkan **kompensasi berupa pencatatan log otomatis (*immutable cloud logging*) dan peninjauan berkala oleh pemilik bisnis/direktur operasional (`MEA02`)**.
