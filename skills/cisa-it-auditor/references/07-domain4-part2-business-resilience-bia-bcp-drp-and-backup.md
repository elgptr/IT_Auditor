# Bab 7: Domain 4 (Bagian 2) — Ketahanan Bisnis (Business Resilience), BIA, BCP/DRP, RAID, Backup, dan Situs Pemulihan (Bobot 23%)

> **Cakupan Materi:** Bab ini melengkapi **Domain 4 CISA (Information Systems Operations and Business Resilience — 23%)** dengan membedah secara menyeluruh arsitektur **Business Impact Analysis (BIA)** beserta linimasa metrik pemulihan (**RPO, RTO, WRT, MTD/MTO, SDO, AIW, MBCO**), teknologi toleransi kegagalan (**RAID 0, 1, 5, 6, 10**, *Clustering*, *Telecom Redundancy*), skema pencadangan data (**Full, Incremental, Differential**, dan rotasi **GFS**), perbandingan **6 Jenis Alternate Recovery Sites** (*Mirrored, Hot, Warm, Cold, Mobile, Reciprocal*), serta **5 Metode Pengujian DRP**.

---

## 7.1 Business Continuity Planning (BCP) vs. Disaster Recovery Planning (DRP)

1. **Business Continuity Plan (BCP):** Rencana strategis dan operasional menyeluruh untuk menjaga kelangsungan **seluruh proses bisnis kritis organisasi** (SDM, fasilitas kerja, komunikasi pelanggan, rantai pasok, dan keuangan) saat terjadi gangguan besar.
2. **Disaster Recovery Plan (DRP):** Komponen **teknis/TI** di dalam BCP yang berfokus khusus pada pemulihan **infrastruktur teknologi informasi, pusat data, jaringan, aplikasi, dan database** setelah bencana.
3. **Prioritas Nomor Satu dalam Setiap Bencana (ISACA Golden Rule):**
   - Dalam skenario bencana fisik apa pun (kebakaran, gempa bumi, banjir, ledakan, ancaman bom), prioritas **PERTAMA** adalah selalu **Keselamatan Jiwa Manusia (*Human Life and Safety*)**, bukan menyelamatkan *backup tape* atau mematikan server!

---

## 7.2 Business Impact Analysis (BIA) & Metrik Waktu Pemulihan

**Business Impact Analysis (BIA)** adalah langkah fondasi paling kritis dalam menyusun BCP/DRP yang bertujuan mengidentifikasi proses bisnis mana yang paling vital, mengukur dampak finansial/operasional jika proses tersebut berhenti dari waktu ke waktu, dan menentukan urutan prioritas pemulihan.

### Diagram Linimasa Bencana (BIA Recovery Timeline)

```
     Masa Operasi Normal                  BENCANA TERJADI!               Batas Kehancuran Bisnis
◄───────────────────────────────►                 │                                 │
                                                  ▼                                 ▼
──────────────●───────────────────────────────────⚡─────────────────────●───────────●───────────►
              │                                   │                     │           │
   [Backup Terakhir Berhasil]          [Sistem Mati / Down]     [Sistem TI Pulih] [Operasi Bisnis Normal]
              │                                   │                     │           │
              ◄─────────────── RPO ───────────────►                     │           │
              (Maksimal Data Hilang / Waktu)      ◄──────── RTO ────────►           │
                                                  (Waktu Pemulihan Sistem TI)       │
                                                                        ◄─── WRT ───►
                                                                    (Verifikasi & Sinkronisasi Data)
                                                  ◄────────────── MTD / MTO ────────►
                                                    (Maximum Tolerable Downtime: RTO + WRT <= MTD)
```

### Tabel Definisi & Aturan Matematis Metrik BIA CISA

| Metrik BIA | Kepanjangan | Definisi, Makna Bisnis, dan Konsekuensi Teknis |
| :---: | :--- | :--- |
| **RPO** | **Recovery Point Objective** | • **Toleransi maksimum kehilangan data (*maximum acceptable data loss*) yang diukur dalam satuan WAKTU mundur ke belakang** dari titik terjadinya bencana.<br>• Menentukan **seberapa sering pencadangan (*backup* / replikasi) harus dilakukan**.<br>• *Contoh:* Jika RPO = **4 jam**, maka *backup*/replikasi harus dilakukan minimal setiap 4 jam. Jika RPO mendekati **0 detik**, organisasi wajib menggunakan **Synchronous Data Mirroring**. |
| **RTO** | **Recovery Time Objective** | • **Waktu maksimum yang diizinkan untuk memulihkan sistem TI/aplikasi** sejak bencana dideklarasikan hingga sistem TI hidup kembali.<br>• Menentukan **pemilihan jenis situs pemulihan (*Hot Site* vs. *Warm Site* vs. *Cold Site*)**.<br>• *Contoh:* Jika RTO = **2 jam**, organisasi tidak mungkin menggunakan *Cold Site* (yang butuh berminggu-minggu), melainkan wajib menggunakan **Hot Site** atau **Mirrored Site**. |
| **WRT** | **Work Recovery Time** | • Waktu tambahan yang dibutuhkan setelah sistem TI pulih (setelah RTO tercapai) untuk **memverifikasi integritas data, menginput ulang transaksi manual yang tertunda selama bencana (*backlog catch-up*), dan menyinkronkan database** sebelum sistem siap melayani pelanggan secara normal. |
| **MTD / MTO** | **Maximum Tolerable Downtime** *(atau Maximum Tolerable Outage)* | • Total waktu maksimum suatu proses bisnis dapat berhenti beroperasi sebelum organisasi mengalami **kerugian fatal yang tidak dapat dipulihkan (*irreparable business failure*)**.<br>• **Aturan Matematis Mutlak:** $$\text{RTO} + \text{WRT} \le \text{MTD}$$ |
| **SDO / MBCO** | **Service Delivery Objective** *(Minimum Business Continuity Objective)* | • **Tingkat layanan operasional minimum** yang harus dicapai pada mode darurat selama beroperasi di situs pemulihan (*alternate site*) sebelum kembali ke pusat data utama (misal: mampu melayani $60\%$ volume transaksi normal). |
| **AIW** | **Acceptable Interruption Window** | • Periode waktu maksimum sistem dapat mati sebelum berdampak buruk pada kelangsungan finansial normal perusahaan (sering disamakan dengan MTD). |

### Hubungan Biaya Pemulihan vs. Biaya Downtime (Titik Optimal BCP)
- Semakin kecil (ketat) nilai **RTO dan RPO** (mendekati nol), maka:
  - **Biaya Kerugian Gangguan (*Downtime Loss Cost*)** semakin **RENDAH**.
  - **Biaya Solusi Pemulihan (*Recovery Solution Cost*)** meroket menjadi **SANGAT MAHAL**.
- Tugas manajemen bersama pemilik bisnis adalah memilih titik keseimbangan di mana **Total Biaya ($\text{Biaya Pemulihan} + \text{Biaya Kerugian Downtime}$) berada pada titik paling minimum**!

---

## 7.3 Toleransi Kegagalan Perangkat Keras (RAID) & Redundansi Telekomunikasi

### A. Perbandingan Lengkap Konfigurasi RAID (Redundant Array of Independent Disks)

| Level RAID | Teknik Penyimpanan | Jumlah Disk Minimum | Toleransi Kegagalan Disk | Karakteristik & Penggunaan Audit CISA |
| :---: | :--- | :---: | :---: | :--- |
| **RAID 0** | **Disk Striping (Tanpa Parity / Tanpa Mirroring)** | **2 Disk** | **0 Disk (TIDAK ADA Fault Tolerance!)** | • Hanya memecah data ke beberapa disk untuk meningkatkan kecepatan baca/tulis (*performance*).<br>• **Bukan solusi ketahanan!** Jika **1 disk saja rusak, 100% seluruh data hilang total!** |
| **RAID 1** | **Disk Mirroring / Duplexing** | **2 Disk** *(Genap)* | **1 Disk** per pasangan *mirror* | • Menyalin data secara identik 1:1 ke dua disk berbeda (*Duplexing* jika menggunakan 2 *disk controller* terpisah).<br>• Keandalan sangat tinggi untuk OS/Log transaksi, namun efisiensi kapasitas penyimpanan hanya **50%** (biaya per GB paling mahal). |
| **RAID 5** | **Block-Level Striping with Distributed Single Parity** | **3 Disk** | **Maksimal 1 Disk** | • Informasi *parity* (XOR) disebar merata di seluruh disk (kapasitas efektif = $N - 1$ disk).<br>• Seimbang antara biaya, kecepatan baca, dan keamanan. Namun jika **2 disk rusak bersamaan**, seluruh data hilang! |
| **RAID 6** | **Block-Level Striping with Dual Distributed Parity** | **4 Disk** | **Maksimal 2 Disk Bersamaan** | • Menyimpan **dua blok parity independen** di setiap *stripe* (kapasitas efektif = $N - 2$ disk).<br>• Tetap aman meskipun **2 disk gagal secara bersamaan** saat proses *rebuild* disk berkapasitas besar. |
| **RAID 10 (1+0)** | **Mirrored Stripes (Gabungan RAID 1 & RAID 0)** | **4 Disk** *(Genap)* | **1 Disk di setiap set Mirror** | • Memberikan performa baca/tulis tercepat sekaligus pemulihan (*rebuild*) tercepat untuk **Database Produksi Kritis berkinerja tinggi**, dengan biaya kapasitas 50%. |

### B. Redundansi Jaringan & Telekomunikasi (Telecom Continuity)
1. **Alternative Routing (Jalur Alternatif):** Menggunakan media transmisi yang berbeda (misal: jalur utama serat optik bawah tanah, jalur cadangan gelombang mikro/*microwave* atau satelit).
2. **Diverse Routing (Rute Berbeda):** Menggunakan dua jalur kabel fisik yang melewati **jalur geografis/pipa bawah tanah yang berbeda (*split cable / dual entrance*)** agar tidak terputus bersamaan oleh satu ekskavator (*Single Point of Failure*).
3. **Last-Mile Circuit Protection:** Melindungi jalur kabel lokal terakhir dari gardu telekomunikasi ke gedung perusahaan agar tidak menjadi *single point of failure*.
4. **Voice Recovery:** Mengalihkan panggilan pelanggan ke pusat panggilan cadangan atau sistem IVR otomatis saat PABX utama lumpuh.

---

## 7.4 Strategi Pencadangan Data (Backup Schemes) & Rotasi Media

### A. Perbandingan 3 Metode Backup: Full, Incremental, dan Differential

| Metode Backup | Data Apa yang Disalin ke Media Backup? | Kecepatan Waktu Backup (Malam Hari) | Kecepatan Waktu Restore (Saat Bencana) | Jumlah Set Media yang Dibutuhkan Saat Restore |
| :--- | :--- | :---: | :---: | :--- |
| **1. Full Backup** | Menyalin **100% seluruh file/data yang dipilih**, terlepas dari apakah file tersebut berubah atau tidak, lalu mereset *archive bit* (menjadi `0`). | **Paling Lambat** *(Memakan kapasitas penyimpanan terbesar)* | **Paling Cepat** | **Hanya 1 Set** (*Full Backup* terakhir). |
| **2. Incremental Backup** | Hanya menyalin file yang **berubah sejak Backup terakhir jenis apa pun** (baik sejak *Full* maupun *Incremental* kemarin), lalu **mereset *archive bit***. | **Paling Cepat** *(Kapasitas media paling hemat)* | **Paling Lambat** | **Banyak Set:** Butuh **1 Full Backup terakhir + SELURUH Incremental Backup berurutan** sejak *Full Backup* tersebut! (Jika 1 pita di tengah rusak, data setelahnya gagal dipulihkan). |
| **3. Differential Backup** *(Kumulatif)* | Menyalin seluruh file yang **berubah sejak Full Backup terakhir**, tanpa mereset *archive bit* (sehingga ukurannya makin membesar setiap hari hingga *Full Backup* berikutnya). | **Sedang** *(Lebih cepat dari Full, lebih lambat dari Incremental)* | **Cepat** | **Hanya 2 Set:** Cukup **1 Full Backup terakhir + 1 Differential Backup terakhir** saja! |

### B. Skema Rotasi Grandfather-Father-Son (GFS) & Offsite Storage Controls
- **Rotasi GFS:**
  - **Son (Anak):** *Backup* harian (biasanya *Incremental* atau *Differential*).
  - **Father (Ayah):** *Backup* mingguan (*Full Backup* setiap akhir pekan).
  - **Grandfather (Kakek):** *Backup* bulanan/tahunan (*Full Backup* yang disimpan di lokasi *Offsite* untuk arsip jangka panjang dan kepatuhan regulasi).
- **Kontrol Penyimpanan Offsite (Offsite Backup Vault):**
  - Lokasi *Offsite* harus cukup jauh agar **tidak terkena bencana alam/regional yang sama** dengan pusat data utama, memiliki kontrol keamanan fisik dan lingkungan (suhu, kelembapan, pemadam api FM-200) yang **setara dengan pusat data produksi**, seluruh media *backup* **wajib dienkripsi**, dan **diuji *restore* secara berkala** (karena *backup* yang tidak pernah diuji *restore* tidak dapat diandalkan!).

---

## 7.5 Perbandingan Lengkap 6 Jenis Situs Pemulihan (Alternate Recovery Sites)

| Jenis Situs Pemulihan | Kesiapan Perangkat Keras, Jaringan, & Data | Waktu Kesiapan (Target RTO) | Tingkat Biaya | Karakteristik & Risiko Audit |
| :--- | :--- | :---: | :---: | :--- |
| **1. Mirrored Site** *(Situs Cermin Aktif)* | Fasilitas identik 100% dengan pusat data utama; perangkat keras, aplikasi, dan **data disinkronkan secara *real-time* (Synchronous)** dan dikelola sendiri oleh organisasi. | **Instan ($\text{RTO} \approx 0$, $\text{RPO} \approx 0$)** | **Paling Mahal** | Kesiapan tertinggi untuk sistem perbankan/bursa efek vital yang tidak boleh mati sedetik pun. |
| **2. Hot Site** *(Situs Panas)* | Gedung sudah dilengkapi listrik, AC, jaringan telekomunikasi, **server, perangkat penyimpanan, dan sistem operasi yang siap pakai**. Data dimuat dari *mirroring asynchronous* atau *backup* terbaru saat bencana. | **Hitungan Jam ($1 - 24\text{ jam}$)** | **Tinggi** | Jika menyewa *Commercial Hot Site* (seperti Sungard/IBM), auditor wajib memastikan vendor **tidak melakukan *oversubscription*** (menyewakan kapasitas yang sama ke terlalu banyak perusahaan di zona bencana yang sama!). |
| **3. Warm Site** *(Situs Hangat)* | Gedung sudah memiliki listrik, AC, koneksi komunikasi, dan **sebagian perangkat keras (sering kali kapasitas lebih kecil atau generasi lama)**, namun aplikasi/data utama harus di-*restore* dari *Offsite Backup*. | **1 s.d. Beberapa Hari** | **Sedang** | Cocok untuk sistem bisnis penting yang memiliki RTO $24 - 72\text{ jam}$. |
| **4. Cold Site** *(Situs Dingin)* | Hanya berupa **ruangan kosong yang memiliki infrastruktur dasar** (pasokan listrik, AC, lantai *raised floor*, dan jalur komunikasi), tetapi **BELUM ada server atau perangkat komputer** sama sekali! | **Hitungan Minggu ($1 - 4\text{ minggu}$)** | **Rendah** | Server baru harus dibeli/dikirim dan diinstal terlebih dahulu saat bencana terjadi. Tidak cocok untuk sistem kritis dengan RTO singkat! |
| **5. Mobile Site** | Pusat data portabel di dalam kontainer truk besar yang dapat dikendarai ke dekat lokasi perusahaan saat bencana. | **Beberapa Hari** | **Sedang - Tinggi** | Bergantung pada akses jalan raya dan kapasitas ruang yang terbatas. |
| **6. Reciprocal Agreement** *(Kesepakatan Timbal Balik)* | Perjanjian antara dua organisasi yang memiliki perangkat keras serupa untuk **saling menampung operasional satu sama lain** jika salah satu mengalami bencana. | **Sulit Dijamin** | **Paling Murah** | **Sangat Tidak Andal (Unreliable):** Kapasitas server mitra biasanya sudah penuh untuk operasionalnya sendiri, masalah kompatibilitas versi sistem, risiko kerahasiaan data, dan **tidak dapat dipaksakan secara hukum (*legally unenforceable*)** saat krisis! |

---

## 7.6 Lima Metode Pengujian DRP (DRP Testing Methods)

Urutan metode pengujian DRP dari yang paling sederhana hingga paling komprehensif:

1. **Checklist Review (Tinjauan Daftar Periksa):** Mendistribusikan salinan dokumen BCP/DRP kepada setiap anggota tim pemulihan untuk diperiksa secara mandiri apakah nomor telepon darurat, daftar aset, dan prosedur masih mutakhir.
2. **Structured Walkthrough / Tabletop Test (Simulasi Meja Rapat):** Seluruh anggota tim tanggap darurat berkumpul di ruang rapat dan **mendiskusikan langkah demi langkah (*role-play* di atas kertas)** bagaimana mereka akan merespons skenario bencana tertentu untuk menemukan celah koordinasi logika.
3. **Simulation Test (Uji Simulasi Operasional):** Menguji respons tim di lapangan terhadap skenario bencana tiruan (termasuk mobilisasi staf dan komunikasi darurat), namun **belum mengaktifkan pemrosesan transaksi di situs pemulihan**.
4. **Parallel Test (Uji Paralel di Situs Pemulihan):** Mengaktifkan server dan memulihkan data di *Alternate Recovery Site*, lalu memproses transaksi uji di sana untuk membuktikan kesiapan situs pemulihan, **sementara pusat data utama tetap beroperasi normal melayani bisnis**.
5. **Full Interruption Test (Uji Penghentian Penuh):** **Mematikan pusat data utama secara nyata** dan mengalihkan 100% operasional bisnis ke situs pemulihan. Merupakan pengujian paling realistis, namun **sangat berisiko mengganggu bisnis nyata** sehingga jarang dilakukan kecuali dengan persiapan matang di luar jam puncak.
