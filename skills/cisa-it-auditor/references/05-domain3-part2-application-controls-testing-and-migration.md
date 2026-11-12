# Bab 5: Domain 3 (Bagian 2) — Kontrol Aplikasi (ITAC), Metodologi Pengujian, dan Migrasi Data (Bobot 12%)

> **Cakupan Materi:** Bab ini melengkapi **Domain 3 CISA** dengan membedah secara komprehensif seluruh **IT Application Controls (ITAC)** (*Input Controls*, algoritma *Check Digit*, *Batch Controls*, *Processing Controls*, *Output Controls*, serta kontrol transaksi elektronik **EDI / EFT / POS / E-Banking**), taksonomi lengkap **12 Jenis Pengujian Perangkat Lunak**, strategi **Konversi Data & Cutover** (*Parallel*, *Phased*, *Abrupt/Big-Bang*), serta **Post-Implementation Review (PIR)**.

---

## 5.1 Arsitektur IT Application Controls (ITAC): Input, Processing, dan Output

Berbeda dengan *IT General Controls (ITGC)* yang melindungi lingkungan TI secara menyeluruh (OS, DB, Jaringan, Change Management), **IT Application Controls (ITAC)** adalah kontrol otomatis atau manual yang tertanam langsung di dalam proses bisnis aplikasi spesifik untuk menjamin bahwa setiap transaksi adalah **Lengkap (*Complete*), Akurat (*Accurate*), Sah/Terotorisasi (*Valid/Authorized*), dan Tepat Waktu (*Timely*)** — sering disingkat **CAVR** (*Completeness, Accuracy, Validity, Restricted Access*).

```
+-----------------------------------------------------------------------------------+
|                        ALUR KONTROL APLIKASI (ITAC PIPELINE)                      |
+-----------------------------------------------------------------------------------+
|  [1. INPUT CONTROLS]               [2. PROCESSING CONTROLS]    [3. OUTPUT CONTROLS]|
|  • Otorisasi Sumber Dokumen        • Run-to-Run Totals         • Rekonsiliasi Akhir|
|  • Batch Totals (Financial,        • Limit & Reasonableness    • Laporan Exception |
|    Hash Total, Record Count)       • Referential Integrity     • Distribusi Aman   |
|  • Edit Checks (Field, Limit,      • Transaction Logging       • Retensi & Pemus-  |
|    Range, Validity, Check Digit,   • Exception Handling          nahan Laporan     |
|    Completeness, Duplicate Check)                                                  |
+-----------------------------------------------------------------------------------+
```

### A. Kontrol Input (Input Controls & Data Validation / Edit Checks)
Tujuan utama *Input Controls* adalah memastikan bahwa hanya transaksi yang **valid, akurat, lengkap, dan telah diotorisasi** yang masuk ke dalam sistem pemrosesan sejak awal.

#### 1. Kontrol Batch Input (Batch Controls & Balancing)
Ketika transaksi dikumpulkan dalam satu kelompok (*batch*) sebelum diproses, 3 jenis kontrol total berikut digunakan untuk mendeteksi data yang hilang, ganda, atau berubah:

| Jenis Batch Control | Definisi & Cara Perhitungan | Tujuan Spesifik Deteksi |
| :--- | :--- | :--- |
| **Financial Total** *(Total Finansial)* | Penjumlahan nilai uang (*monetary field*) dari seluruh dokumen dalam satu *batch* (misal: total rupiah dari 100 faktur). | Memastikan **akurasi nilai finansial (*accuracy*)** dan kelengkapan transaksi bernilai uang. |
| **Hash Total** *(Total Hash)* | Penjumlahan matematis atas *field* numerik yang **tidak memiliki makna kuantitatif/finansial** (misal: menjumlahkan seluruh **Nomor Rekening**, **NPWP**, atau **Nomor Induk Karyawan** dalam satu *batch*). | Memastikan **integritas dan akurasi identifikasi record** (mendeteksi jika nomor rekening berubah atau ada *record* yang tertukar/hilang). |
| **Record / Document Count** *(Jumlah Record)* | Penghitungan sederhana atas jumlah fisik dokumen atau baris transaksi dalam satu *batch* (misal: 100 dokumen). | Memastikan **kelengkapan jumlah transaksi (*completeness*)**, namun tidak mendeteksi jika nilai uang di dalamnya salah ketik. |

#### 2. Matriks Lengkap Data Validation / Programmed Edit Checks

| Jenis Edit Check | Cara Kerja Validasi di Dalam Aplikasi | Contoh Implementasi Nyata | Tujuan Utama |
| :--- | :--- | :--- | :--- |
| **Sequence Check** *(Pemeriksaan Urutan)* | Memeriksa apakah nomor dokumen/transaksi berurutan secara kronologis/numerik. | Mendeteksi nomor faktur `INV-1004` yang melompat dari `INV-1002` (*missing document*) atau muncul dua kali (*duplicate*). | **Completeness & Uniqueness** |
| **Limit Check** *(Pemeriksaan Batas Tunggal)* | Memastikan nilai input tidak melampaui satu batas atas (*ceiling*) atau batas bawah (*floor*) yang ditetapkan. | Jam kerja mingguan karyawan tidak boleh melebihi `60 jam`; penarikan ATM tidak boleh melebihi `Rp15.000.000`. | **Accuracy & Authorization** |
| **Range Check** *(Pemeriksaan Rentang)* | Memastikan nilai input berada di antara batas minimum **DAN** batas maksimum tertentu. | Kode bulan harus berada di antara `01` s.d. `12`; usia pemohon kredit harus antara `21` s.d. `65` tahun. | **Accuracy & Validity** |
| **Validity Check** *(Pemeriksaan Validitas)* | Membandingkan kode input terhadap daftar nilai yang sah atau tabel *Master Data* yang telah disetujui. | Memeriksa apakah `Kode Vendor` yang diinput benar-benar terdaftar di tabel *Approved Vendor Master*; kode jenis kelamin hanya `L` atau `P`. | **Validity / Existence** |
| **Reasonableness Check** *(Pemeriksaan Kewajaran)* | Membandingkan nilai suatu *field* secara logis terhadap **field lain** atau data historis transaksi. | Tagihan listrik rumah tangga bulan ini tiba-tiba naik $5.000\%$ dari rata-rata 6 bulan terakhir; tanggal pengiriman lebih awal dari tanggal pemesanan. | **Accuracy & Logic** |
| **Field / Format Check** *(Pemeriksaan Karakter)* | Memeriksa apakah jenis karakter yang dimasukkan sesuai dengan tipe data *field* (Alfabet, Numerik, Alfanumerik). | Menolak huruf `O` pada kolom Nomor Telepon atau kolom Nilai Rupiah. | **Accuracy** |
| **Sign Check** *(Pemeriksaan Tanda +/-)* | Memastikan tanda positif (`+`) atau negatif (`-`) pada angka sesuai dengan jenis transaksi. | Jumlah stok barang di gudang atau jumlah gaji pokok tidak boleh bernilai negatif (`-`). | **Accuracy** |
| **Size / Capacity Check** *(Pemeriksaan Panjang)* | Memastikan jumlah digit/karakter tidak melebihi atau kurang dari panjang *field* yang ditentukan. | Nomor Induk Kependudukan (NIK) harus tepat `16 digit`. | **Accuracy & Completeness** |
| **Completeness / Existence Check** | Memastikan seluruh kolom wajib (*mandatory fields*) telah terisi dan tidak dibiarkan kosong (*NULL/Blank*). | Menolak penyimpanan formulir nasabah jika kolom `Alamat` atau `Tanggal Lahir` kosong. | **Completeness** |
| **Duplicate Check** *(Pemeriksaan Duplikasi)* | Membandingkan transaksi baru terhadap transaksi yang sudah pernah diproses untuk mencegah pemrosesan ganda. | Menolak pembayaran jika kombinasi `Kode Vendor + Nomor Invoice + Tanggal + Nominal` sudah pernah dibayar. | **Uniqueness / Prevent Overpayment** |
| **Check Digit** *(Digit Pemeriksa — Mod 10 / Luhn)* | Menambahkan **1 digit ekstra yang dihitung secara matematis** di ujung nomor identifikasi (nomor kartu kredit, IMEI, ISBN, rekening) menggunakan algoritma seperti **Modulus 10 / Mod 11**. | Mendeteksi **kesalahan ketik tunggal (*transcription error*, misal `4` jadi `5`)** dan **kesalahan posisi tertukar (*transposition error*, misal `48` jadi `84`)** secara instan saat input! | **Accuracy of Primary Identifiers** |
| **Key Verification** *(Pengetikan Ulang)* | Dua operator berbeda mengetikkan data dokumen yang sama secara terpisah, lalu mesin membandingkan kedua hasil ketikan. | Digunakan pada sistem *data entry* kritis untuk mendeteksi kesalahan ketik manusia. | **Accuracy (Detective/Preventive)** |

---

### B. Kontrol Pemrosesan (Processing Controls) & Kontrol Output (Output Controls)

1. **Processing Controls (Kontrol Pemrosesan):**
   - Memastikan bahwa data yang sudah masuk diproses secara **lengkap dan akurat** hingga memperbarui file *master*:
     - **Run-to-Run Totals:** Memverifikasi bahwa total *batch* (jumlah *record* dan nilai uang) setelah tahap pemrosesan ke-1 sama persis dengan total input yang masuk ke tahap pemrosesan ke-2 ($\text{Saldo Awal} + \text{Transaksi Masuk} - \text{Transaksi Ditolak} = \text{Saldo Akhir}$).
     - **Limit & Reasonableness Checks on Calculated Values:** Memeriksa hasil perhitungan bunga atau gaji bersih sebelum dicetak ke cek/transfer.
     - **File Labels (Internal Header & Trailer Labels):** Memastikan program tidak membaca file magnetik/data dari periode yang salah atau menimpa (*overwrite*) file aktif yang belum kedaluwarsa.
     - **Transaction Log & Exception/Suspense File:** Mencatat seluruh transaksi yang gagal diproses ke dalam *Suspense Account / Error File* untuk diinvestigasi dan diperbaiki secara tepat waktu (auditor wajib mengaudit *aging* dari *Suspense File*!).
2. **Output Controls (Kontrol Keluaran):**
   - Memastikan laporan hasil pemrosesan akurat dan **hanya didistribusikan kepada penerima yang berhak (*authorized recipients*)**:
     - Rekonsiliasi *Output Batch Totals* dengan *Input Batch Totals* oleh *Control Group*.
     - Penyimpanan laporan sensitif / kertas cek kosong (*blank negotiable instruments*) di tempat terkunci, *spool file security* pada printer jaringan, pencantuman klasifikasi kerahasiaan pada *header/footer* laporan, dan penghancuran kertas laporan rahasia menggunakan *cross-cut shredder*.

---

## 5.2 Kontrol Transaksi Elektronik: EDI, EFT, POS, dan E-Banking

Transaksi tanpa warkat kertas (*paperless*) seperti **Electronic Data Interchange (EDI)** dan **Electronic Funds Transfer (EFT)** membawa risiko spesifik ketiadaan tanda tangan basah dan ketergantungan penuh pada kontrol jaringan/aplikasi:

| Komponen Sistem | Risiko Utama | Kontrol Wajib yang Harus Diverifikasi IS Auditor |
| :--- | :--- | :--- |
| **EDI (Electronic Data Interchange)**<br>*(Pertukaran dokumen bisnis standar seperti PO & Invoice antar komputer perusahaan mitra)* | • Pesan dikirim oleh pihak palsu (*spoofing*)<br>• Pesan hilang atau terduplikasi di jaringan<br>• Mitra menyangkal pernah memesan barang (*repudiation*)<br>• Pesan korup saat translasi format (ANSI X12 / EDIFACT) | • **Trading Partner Agreement:** Kontrak hukum formal sebelum pertukaran EDI dimulai.<br>• **Autentikasi & Non-Repudiation:** Penggunaan *Digital Signatures*, enkripsi jalur (VPN/TLS/VAN), dan *Functional Acknowledgments* (tanda terima elektronik otomatis).<br>• **Input/Translation Validation:** Pemeriksaan *Segment Count*, *Control Totals*, dan batas kewajaran (*Reasonableness Check* — misal: sistem otomatis menahan pesanan EDI jika mitra tiba-tiba memesan 100.000 unit padahal biasanya hanya 100 unit). |
| **EFT (Electronic Funds Transfer) & E-Banking** | • Penyadapan atau modifikasi instruksi transfer dana (*Man-in-the-Middle*)<br>• Pembuatan transfer tanpa otorisasi ganda | • **Dual Control / Two-Factor Approval (Maker-Checker-Approver):** Pemisahan tegas antara pembuat instruksi transfer dan penyetuju.<br>• Enkripsi *end-to-end*, *Session Timeout*, penggunaan *Hardware Security Module* (HSM), dan rekonsiliasi kliring harian otomatis. |
| **POS (Point of Sale) & Kartu Pembayaran** | • *Skimming* pita magnetik kartu / pencurian PIN<br>• Manipulasi harga barang oleh kasir di terminal POS | • **Harga barang diambil otomatis (*lookup*) dari Master File Server terpusat** melalui pemindaian *barcode* (kasir dilarang mengetik harga manual kecuali diotorisasi supervisor).<br>• Enkripsi PIN **sejak dari tombol PIN Pad (*Point-to-Point Encryption* / P2PE)** dan kepatuhan standar **PCI-DSS** (chip EMV). |

---

## 5.3 Taksonomi Lengkap 12 Metode Pengujian Perangkat Lunak (Software Testing)

Auditor SI wajib mampu membedakan setiap jenis pengujian beserta siapa yang melakukannya dan fokus utamanya:

| Jenis Pengujian | Pelaku Utama | Tujuan, Fokus, dan Cara Kerja |
| :--- | :--- | :--- |
| **1. Unit Testing** | **Developer / Programmer** | Menguji modul/fungsi/kelas terkecil secara terisolasi. Umumnya menggunakan pendekatan **White-Box Testing** (memeriksa logika internal percabangan `if/else`, *loop*, dan jalur kode). |
| **2. Integration Testing** | **Tim Developer / QA** | Menguji **antarmuka (*interfaces*) dan pertukaran parameter data antar modul** yang saling terhubung (*Top-Down*, *Bottom-Up*, atau *Big-Bang integration*). |
| **3. System Testing** | **Tim TI / QA Independen** | Menguji sistem secara utuh terhadap spesifikasi teknis dan fungsional, mencakup sub-pengujian: **Recovery Testing** (kemampuan pulih dari *crash*), **Security Testing**, **Load Testing** (beban puncak normal), **Stress Testing** (beban ekstrem melampaui kapasitas maksimum untuk mencari titik hancur/*breaking point*), dan **Volume Testing** (ukuran data besar). |
| **4. Regression Testing** | **QA / Automated Pipeline** | Menguji ulang sistem setelah adanya perubahan, perbaikan *bug*, atau *patch* untuk memastikan bahwa **perubahan baru TIDAK merusak fungsi lama yang sebelumnya sudah berjalan baik (*no new errors introduced*)**. Wajib menggunakan data uji yang sama dengan pengujian sebelumnya. |
| **5. Sociability / Interface Testing** | **Tim TI / Infrastruktur** | Menguji apakah aplikasi baru dapat hidup berdampingan (*co-exist*) dan berkomunikasi dengan sistem/aplikasi lain yang sudah ada di lingkungan produksi tanpa saling mengganggu atau merusak data bersama. |
| **6. Pilot Testing** | **Unit Bisnis Terpilih** | Menerapkan sistem baru secara terbatas di **satu cabang atau satu divisi percontohan (*pilot site*)** terlebih dahulu untuk mengevaluasi kinerja nyata sebelum diperluas ke seluruh perusahaan. |
| **7. Parallel Testing** | **Tim Proyek & Pengguna** | Memasukkan data transaksi yang sama ke dalam **sistem lama dan sistem baru secara bersamaan**, lalu **membandingkan hasil output kedua sistem** untuk memastikan akurasi logika pemrosesan sistem baru. |
| **8. White-Box (Glass-Box) Testing** | **Developer / Code Auditor** | Pengujian yang memeriksa **struktur internal dan logika *source code*** baris demi baris untuk memastikan tidak ada logika mati (*dead code*) atau *backdoor*. |
| **9. Black-Box Testing** | **QA / End User (UAT)** | Pengujian fungsional yang hanya melihat **Input dan Output** tanpa perlu mengetahui kode internal program (digunakan pada *System Testing* dan **UAT**). |
| **10. Alpha vs. Beta Testing** | **Internal vs. Pelanggan Luar** | • **Alpha Testing:** Pengujian awal oleh pengguna di **dalam lingkungan internal pengembang** (sering kali belum memuat seluruh fitur).<br>• **Beta Testing:** Pengujian versi pra-rilis oleh **pengguna akhir nyata di lingkungan bisnis mereka sendiri** di luar perusahaan pengembang. |
| **11. Final Acceptance Testing / UAT** *(User Acceptance Testing)* | **End Users / Business Owners** | Pengujian akhir oleh pemilik bisnis di lingkungan *Test/Staging* yang menyerupai produksi menggunakan skenario bisnis nyata untuk memastikan sistem memenuhi kebutuhan bisnis. **Sign-off UAT adalah syarat mutlak sebelum migrasi ke produksi!** |

> [!IMPORTANT]
> **Aturan Keamanan Data Uji (Test Data Rule — CISA Exam Trap):**
> Pengujian di lingkungan *Development/Test/UAT* **DILARANG KERAS menggunakan salinan langsung data produksi mentah (*raw production data*)** yang memuat data pribadi/rahasia nasabah karena lingkungan *Test* umumnya memiliki kontrol keamanan yang lebih longgar! Jika membutuhkan data realistis dari produksi, data tersebut **wajib disanitasi/disamarkan (*Data Masking / Anonymization / Obfuscation*)** terlebih dahulu atau mendapat persetujuan tertulis dari **Data Owner** dengan menerapkan kontrol keamanan tingkat produksi pada server *Test*.

---

## 5.4 Konversi Data (Data Migration) & Strategi Cutover (Go-Live)

### A. Audit Konversi / Migrasi Data (Legacy $\rightarrow$ Sistem Baru)
Saat memigrasikan data dari sistem lama ke sistem baru, tugas terpenting IS Auditor adalah memastikan **Kelengkapan (*Completeness*) dan Akurasi (*Accuracy*)** data yang dikonversi melalui:
1. Rekonsiliasi **Record Counts**, **Financial Control Totals**, dan **Hash Totals** antara *database* sumber (sebelum ekstraksi) dan *database* target (setelah *load*).
2. Pemeriksaan aturan pemetaan *field* (*Data Mapping Rules*), penanganan nilai kosong (*default values*), dan pembersihan data (*data cleansing*) yang disetujui oleh **Data Owner**.
3. Memastikan adanya **Fallback / Rollback Plan** yang teruji apabila migrasi gagal di tengah jalan.

### B. Perbandingan 3 Strategi Cutover (Changeover / Go-Live Techniques)

| Strategi Cutover | Cara Kerja Transisi | Tingkat Risiko | Keunggulan & Kelemahan Utama |
| :--- | :--- | :---: | :--- |
| **1. Parallel Changeover** *(Operasi Paralel)* | Sistem lama dan sistem baru dijalankan **secara bersamaan penuh** selama periode tertentu hingga sistem baru terbukti 100% stabil dan akurat, baru sistem lama dimatikan. | **Paling Rendah** *(Paling Aman)* | • **Keunggulan:** Memberikan jaring pengaman penuh jika sistem baru gagal.<br>• **Kelemahan:** Biaya operasional sangat mahal dan membebani staf karena harus menginput/memelihara dua sistem sekaligus. |
| **2. Phased / Pilot Changeover** *(Bertahap)* | Sistem baru diimplementasikan secara bertahap per modul bisnis atau per lokasi cabang (*site by site*). | **Sedang** | • **Keunggulan:** Membatasi dampak kegagalan pada satu area/modul dan memungkinkan pembelajaran bertahap.<br>• **Kelemahan:** Membutuhkan antarmuka sementara (*temporary bridges*) antara bagian yang sudah memakai sistem baru dan bagian yang masih memakai sistem lama. |
| **3. Abrupt / Direct / Big-Bang Cutover** *(Langsung Seketika)* | Sistem lama dimatikan pada waktu tertentu (misal Jumat malam) dan sistem baru langsung mengambil alih 100% operasi pada hari kerja berikutnya (Senin pagi). | **Paling Tinggi** *(Paling Berbahaya)* | • **Keunggulan:** Tidak ada biaya operasi ganda.<br>• **Kelemahan:** **Sangat berisiko fatal!** Jika sistem baru mengalami kegagalan kritis saat *Go-Live* dan tidak ada jalur *rollback* cepat, seluruh operasional perusahaan dapat lumpuh total. |
