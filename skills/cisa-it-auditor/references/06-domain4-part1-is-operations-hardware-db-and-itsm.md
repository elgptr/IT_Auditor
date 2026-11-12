# Bab 6: Domain 4 (Bagian 1) — Operasional Sistem Informasi, Perangkat Keras, Database, dan ITSM (Bobot 23%)

> **Cakupan Materi:** Bab ini membahas separuh pertama **Domain 4 CISA (Information Systems Operations and Business Resilience — 23% / ~35 soal)** yang mencakup operasional pusat data (*Job Scheduling*, *System Interfaces*), kontrol perangkat keras & media portabel (USB/RFID), *IT Asset Management* (ITAM) & kepatuhan lisensi, risiko **End-User Computing (EUC / Spreadsheet)**, arsitektur & kontrol **DBMS** (*Normalization*, ACID, *Concurrency Locking*), serta proses **IT Service Management (ITSM / ITIL)**: *Incident*, *Problem*, *Change*, *Emergency Change*, *Configuration (CMDB)*, *Release*, *Patch Management*, dan **SLA / OLA / UC**.

---

## 6.1 Kontrol Operasional TI, Job Scheduling, dan Hardware Monitoring

Operasional TI bertugas memastikan pemrosesan informasi harian berjalan secara akurat, aman, dan tepat waktu sesuai jadwal yang disepakati dengan bisnis.

### A. Job Scheduling & Batch Operations Controls
1. **Otorisasi Jadwal Kerja (*Job Schedule Authorization*):** Jadwal pemrosesan *batch* harian/bulanan harus disetujui secara formal oleh manajemen TI dan pemilik bisnis. Perubahan jadwal atau penambahan *ad-hoc job* wajib melalui tiket yang terotorisasi.
2. **Automated Job Scheduling Software (misal Control-M / Cron / Autosys):**
   - Mengurangi kesalahan intervensi manual operator dan memastikan urutan ketergantungan antar *job* (*job dependencies*) terpenuhi.
   - **Kontrol Kunci yang Diaudit (SOXIT.04.C3 & C4):** Akses *write/modify* ke parameter *Job Scheduler* harus dibatasi ketat hanya untuk personel yang berwenang, dan setiap kegagalan *batch job* (*abend / abnormal end*) harus menghasilkan peringatan otomatis (*alert*), dicatat sebagai tiket insiden, dan diselesaikan secara tepat waktu tanpa operator mengubah data produksi secara langsung.
3. **Console Logs / Operator Logs:**
   - Seluruh aktivitas konsol operator sistem harus dicatat secara otomatis, dilindungi dari modifikasi/penghapusan oleh operator sendiri, dan **ditinjau secara berkala oleh supervisor operasional yang independen**.

### B. Laporan Pemantauan Perangkat Keras (Hardware Monitoring Reports)
Auditor SI harus memahami kegunaan laporan pemantauan infrastruktur berikut:
- **Availability Reports:** Mengukur persentase waktu sistem aktif (*uptime*) vs. waktu mati (*downtime*) untuk memverifikasi kepatuhan SLA.
- **Hardware Error Reports:** Mendeteksi kegagalan komponen perangkat keras (sektor *hard disk* rusak, kesalahan memori ECC, kegagalan paket antarmuka jaringan) agar komponen dapat diganti secara preventif sebelum menyebabkan *crash* sistem.
- **Utilization / Capacity Management Reports:** Memantau penggunaan CPU, RAM, *disk space*, dan *bandwidth* jaringan untuk merencanakan peningkatan kapasitas (*capacity planning*) dan mendeteksi anomali pemrosesan (*runaway processes*).

### C. Kontrol Perangkat Portabel: USB Flash Drives & RFID
- **USB / Removable Media:** Membawa dua risiko utama: (1) Pencurian data rahasia (*Data Exfiltration*) dalam jumlah besar dengan cepat, dan (2) Masuknya *malware/ransomware* ke jaringan internal. Kontrol terbaik adalah **menonaktifkan port USB secara terpusat melalui Group Policy / Endpoint Protection**, atau mewajibkan hanya USB perusahaan yang terdaftar dan **terenkripsi secara perangkat keras (*hardware-encrypted USB*)** disertai pemantauan **DLP (Data Loss Prevention)**.
- **RFID (Radio Frequency Identification):** Rentan terhadap penyadapan gelombang radio (*eavesdropping*), kloning tag, dan pelacakan lokasi tanpa izin. Kontrol meliputi autentikasi tag-pembaca, enkripsi sinyal, dan pelindung frekuensi radio (*Faraday cage/shielding*).

---

## 6.2 IT Asset Management (ITAM), Software Licensing, dan End-User Computing (EUC)

1. **IT Asset Management (ITAM) & Kepatuhan Lisensi Perangkat Lunak:**
   - Organisasi wajib memelihara inventaris perangkat keras dan perangkat lunak yang akurat (terintegrasi dengan CMDB) serta melakukan pemindaian jaringan berkala untuk mendeteksi instalasi perangkat lunak tanpa izin (**Unauthorized / Pirated Software**).
   - Risiko instalasi perangkat lunak tidak berlisensi: Tuntutan hukum/denda hak cipta dari vendor serta masuknya *trojan/malware* dari instalasi ilegal.
2. **End-User Computing (EUC) / User-Developed Applications (UDA):**
   - EUC mengacu pada aplikasi yang dibangun dan dikelola sendiri oleh pengguna bisnis di luar departemen TI, seperti **Spreadsheet Excel kompleks dengan rumus/Macro VBA**, database Microsoft Access lokal, atau aplikasi *low-code* departemen.
   - **Risiko Utama EUC (Sangat Sering Keluar di Ujian CISA!):**
     - Ketiadaan pengujian formal (rumus salah hitung tanpa terdeteksi), ketiadaan kontrol perubahan (*version control*), ketiadaan *backup* terpusat, ketiadaan *access control* tingkat sel, dan kurangnya dokumentasi.
   - **Kontrol Audit atas EUC Kritikal (yang berdampak pada Laporan Keuangan):**
     - Menginventarisasi dan mengklasifikasikan risiko seluruh EUC/Spreadsheet kritis; mengunci sel rumus (*cell protection*), menerapkan *access control* pada folder penyimpanan, memelihara log perubahan versi, melakukan *backup* otomatis ke server pusat, dan melakukan **review logika rumus secara independen (*independent formula review*)**.

---

## 6.3 Arsitektur Database Management System (DBMS) & Kontrol Integritas Data

### A. Tiga Tingkat Abstraksi Skema Database (ANSI/SPARC Architecture)
1. **External Schema (View Level):** Cara pandang pengguna akhir atau program aplikasi tertentu terhadap sebagian data (membatasi pengguna hanya melihat kolom/baris yang diizinkan melalui `CREATE VIEW`).
2. **Conceptual / Logical Schema:** Struktur logis keseluruhan database (tabel, atribut, relasi, dan batasan integritas) yang dilihat oleh perancang database/DBA.
3. **Internal / Physical Schema:** Cara data benar-benar disimpan secara fisik di dalam blok penyimpanan *disk*, indeks (*B-Tree*), dan partisi.

### B. Normalisasi Database & Integritas Referensial
- **Database Normalization (1NF, 2NF, 3NF):** Proses mengorganisasikan tabel dan kolom dalam database relasional untuk **meminimalkan redundansi data (duplikasi)** dan mencegah anomali saat *Insert, Update,* atau *Delete*.
- *(Catatan Kinerja)*: Terkadang database sengaja **di-denormalisasi (*Denormalization*)** pada *Data Warehouse / OLAP* untuk **mempercepat kinerja pembacaan (*query performance*)**, namun konsekuensinya adalah meningkatnya redundansi data yang harus dijaga dengan kontrol sinkronisasi.
- **Entity Integrity:** Setiap baris dalam tabel harus memiliki **Primary Key** yang unik dan tidak boleh bernilai *NULL*.
- **Referential Integrity:** Setiap nilai **Foreign Key** pada tabel anak harus cocok dengan nilai *Primary Key* yang ada pada tabel induk (mencegah munculnya *orphan records* — misal: transaksi pesanan dengan kode pelanggan yang sudah dihapus).

### C. Properti Transaksi ACID & Concurrency Control
Untuk menjaga integritas database saat diakses oleh ribuan pengguna secara bersamaan (*concurrent access*), DBMS wajib menegakkan **4 properti ACID**:
1. **Atomicity (Atomisitas — "All or Nothing"):** Seluruh rangkaian operasi dalam satu transaksi harus berhasil 100% (**COMMIT**); jika salah satu langkah gagal (misal listrik mati setelah saldo didebit tetapi sebelum rekening tujuan dikredit), seluruh transaksi harus dibatalkan dan dikembalikan ke keadaan semula (**ROLLBACK**).
2. **Consistency (Konsistensi):** Transaksi hanya boleh membawa database dari satu status valid ke status valid lainnya sesuai aturan integritas.
3. **Isolation (Isolasi / Concurrency Control):** Eksekusi transaksi secara bersamaan tidak boleh saling mengintervensi (menggunakan mekanisme **Record Locking — Shared Lock vs. Exclusive Lock** untuk mencegah masalah *Lost Update* atau *Dirty Read*, serta penanganan *Deadlock*).
4. **Durability (Daya Tahan):** Setelah transaksi berhasil di-*COMMIT*, perubahannya bersifat permanen meskipun terjadi kegagalan sistem sesaat kemudian (dijamin melalui **Write-Ahead Logging / Redo Log & Before/After Image Checkpoints**).

---

## 6.4 Proses IT Service Management (ITSM / ITIL) yang Diaudit CISA

```
[INSIDEN MUNCUL] ──► [Incident Management: Pulihkan Layanan Cepat (Workaround)]
                             │
                             ▼ (Insiden Berulang / Kritikal)
                     [Problem Management: Cari Root Cause (RCA) & Known Error DB]
                             │
                             ▼ (Butuh Perbaikan Permanen)
                     [Change Management: RFC -> Impact Analysis -> CAB Approval -> UAT]
                             │
                             ▼
                     [Release & Deployment Management + Update CMDB (Configuration Mgmt)]
```

### A. Perbandingan Incident Management vs. Problem Management (Topik Favorit Ujian CISA!)

| Dimensi | Incident Management (Manajemen Insiden) | Problem Management (Manajemen Masalah) |
| :--- | :--- | :--- |
| **Definisi** | Menangani gangguan tidak terencana (*unplanned interruption*) atau penurunan kualitas layanan TI. | Mengidentifikasi dan menghilangkan **penyebab dasar (*Root Cause*)** dari satu atau lebih insiden yang berulang atau berisiko besar. |
| **Tujuan Utama** | **Memulihkan operasional layanan normal secepat mungkin (*restore normal service as quickly as possible*)** dengan meminimalkan dampak bisnis (misal melalui *reboot*, *failover*, atau *workaround* sementara). | **Mencegah terulangnya insiden di masa depan (*prevent recurrence*)** melalui **Root Cause Analysis (RCA)**, dokumentasi *Known Error Database (KEDB)*, dan pengajuan *Request for Change (RFC)* permanen. |
| **Fokus Waktu** | Kecepatan respons dan pemulihan jangka pendek (**MTTR — Mean Time to Resolve/Restore**). | Kedalaman investigasi dan perbaikan struktural jangka panjang. |

### B. Change Management, Emergency Changes, dan Configuration Management (CMDB)

1. **Alur Baku Change Management (SOXIT.02):**
   - Setiap perubahan pada aplikasi, database, atau infrastruktur produksi wajib melewati: **Pengajuan RFC (Request for Change)** $\rightarrow$ **Analisis Dampak & Risiko (*Impact & Risk Assessment*)** $\rightarrow$ **Pengembangan & Pengujian di Lingkungan Non-Produksi (termasuk UAT & Regression Test)** $\rightarrow$ **Persetujuan Rencana Rollback/Backout** $\rightarrow$ **Persetujuan Formal Change Advisory Board (CAB) & Pemilik Bisnis** $\rightarrow$ **Migrasi ke Produksi oleh Fungsi Independen (bukan Developer!)**.
2. **Prosedur Emergency Change (Perubahan Darurat — Sangat Penting!):**
   - Ketika terjadi insiden kritis di produksi pada malam hari/akhir pekan yang menuntut perbaikan segera (*emergency patch/fix*) dan tidak memungkinkan menunggu jadwal rapat CAB reguler:
     - Penggunaan akses darurat (*Emergency / FireCall ID*) tetap memerlukan persetujuan darurat (*expedited approval* misal via telepon/pesan dari *Emergency CAB*).
     - Seluruh aktivitas selama sesi darurat wajib terekam dalam log otomatis.
     - **Kewajiban Mutlak Pasca-Darurat (*Retroactive Review*):** Perubahan darurat tersebut **WAJIB didokumentasikan, diuji ulang, dan ditinjau/disetujui secara retroaktif (*ex-post facto / after-the-fact review*)** oleh CAB dan pemilik bisnis sesegera mungkin pada hari kerja berikutnya!
3. **Configuration Management & CMDB:**
   - Mencatat dan memelihara informasi akurat mengenai seluruh **Configuration Items (CI)** (server, perangkat jaringan, lisensi OS, versi aplikasi) beserta hubungan ketergantungannya di dalam **Configuration Management Database (CMDB)**.
   - Auditor memeriksa apakah perusahaan melakukan **Configuration Audit / Physical-to-CMDB Reconciliation** secara berkala untuk mendeteksi perubahan tanpa otorisasi (*unauthorized changes*).
4. **Patch & Release Management:**
   - Setiap *security patch* dari vendor **tidak boleh langsung dipasang di server produksi secara membabi buta**, melainkan harus **diuji terlebih dahulu di lingkungan *Test/Staging*** untuk memastikan *patch* tersebut tidak merusak kompatibilitas aplikasi produksi (kecuali risiko eksploitasi *zero-day* jauh lebih besar dan telah mendapat persetujuan darurat dengan rencana *rollback*).

---

## 6.5 Perbandingan SLA, OLA, dan Underpinning Contract (UC)

| Jenis Kesepakatan | Pihak yang Terlibat | Cakupan & Fungsi dalam Tata Kelola Layanan |
| :--- | :--- | :--- |
| **SLA** *(Service Level Agreement)* | **Departemen TI (atau Vendor) $\leftrightarrow$ Pelanggan / Unit Bisnis** | Kesepakatan formal tertulis mengenai target tingkat layanan bisnis (misal: *Core Banking* harus aktif $99.95\%$, waktu tanggap insiden Prioritas 1 maksimal 15 menit). |
| **OLA** *(Operational Level Agreement)* | **Tim Internal TI A $\leftrightarrow$ Tim Internal TI B** *(di dalam organisasi yang sama)* | Kesepakatan internal antar fungsi teknis TI (misal: Tim Network dan Tim Database berjanji kepada Tim Service Desk untuk merespons tiket eskalasi internal dalam 10 menit) guna mendukung tercapainya SLA kepada bisnis. |
| **UC** *(Underpinning Contract)* | **Organisasi $\leftrightarrow$ Vendor / Pemasok Eksternal** | Kontrak yang mengikat secara hukum dengan pihak ketiga di luar perusahaan (misal: ISP telekomunikasi atau vendor pemeliharaan perangkat keras server) yang target waktunya harus mendukung SLA organisasi. |
