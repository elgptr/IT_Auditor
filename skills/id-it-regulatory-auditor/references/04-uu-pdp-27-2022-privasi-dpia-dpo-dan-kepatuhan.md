# Bab 4: Audit Kepatuhan Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)

> **Cakupan Materi:** Bab ini mengkodifikasi panduan audit kepatuhan teknis dan hukum atas **Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** — yang telah berlaku penuh secara efektif sejak **17 Oktober 2024** setelah masa transisi 2 tahun berakhir (Pasal 74) — diselaraskan dengan **COBIT 2019 (`APO14`, `APO13`, `DSS05`, `MEA03`)**, **CISA Domain 5**, dan **ISO/IEC 27701 (PIMS)**.

---

## 4.1 Klasifikasi Data Pribadi & Peran Hukum dalam UU PDP

### A. Dua Kategori Data Pribadi (Pasal 4 UU PDP)

| Kategori Data Pribadi | Rincian Jenis Data menurut Pasal 4 UU PDP | Persyaratan Kontrol Keamanan Teknis (COBIT / CISA) |
| :--- | :--- | :--- |
| **1. Data Pribadi Bersifat Spesifik** *(High-Risk / Sensitive PII — Pasal 4 ayat 2)* | 1. **Data dan informasi kesehatan**<br>2. **Data biometrik** (sidik jari, wajah, iris, DNA)<br>3. **Data genetika**<br>4. **Catatan kejahatan**<br>5. **Data anak**<br>6. **Data keuangan pribadi** (saldo, nomor kartu kredit, mutasi, pinjaman)<br>7. Data lainnya sesuai ketentuan peraturan perundang-undangan. | • Wajib dilakukan **Data Protection Impact Assessment (DPIA — Pasal 34)** sebelum pemrosesan!<br>• Wajib dienkripsi saat disimpan (*AES-256 at rest*) dan ditransmisikan (*TLS 1.3 in transit*).<br>• Wajib menerapkan **Data Masking / Tokenization / Pseudonymization** di lingkungan non-produksi.<br>• Pencatatan jejak akses tingkat baris (*Row-Level Audit Logging*). |
| **2. Data Pribadi Bersifat Umum** *(General PII — Pasal 4 ayat 3)* | 1. Nama lengkap<br>2. Jenis kelamin<br>3. Kewarganegaraan<br>4. Agama<br>5. Status perkawinan<br>6. **Data Pribadi yang dikombinasikan untuk mengidentifikasi seseorang** (NIK, Nomor Telepon, Alamat Email, Alamat Rumah, Alamat IP). | • Kontrol akses berbasis peran (**RBAC — Least Privilege**), persetujuan/dasar pemrosesan yang sah, dan pembatasan masa retensi. |

### B. Pengendali Data Pribadi (Data Controller) vs. Prosesor Data Pribadi (Data Processor)
- **Pengendali Data Pribadi (*Data Controller* — Pasal 1 angka 4):** Setiap orang, badan publik, dan organisasi internasional yang bertindak sendiri-sendiri atau bersama-sama dalam **menentukan tujuan dan melakukan kendali** pemrosesan Data Pribadi. **Memikul akuntabilitas hukum utama kepada Subjek Data dan Lembaga PDP!**
- **Prosesor Data Pribadi (*Data Processor* — Pasal 1 angka 5):** Pihak yang melakukan pemrosesan Data Pribadi **atas nama dan berdasarkan instruksi tertulis Pengendali Data Pribadi** (Pasal 51). Prosesor dilarang melibatkan sub-prosesor lain tanpa persetujuan tertulis dari Pengendali Data!

---

## 4.2 Tujuh Dasar Pemrosesan Data Pribadi yang Sah (Lawful Basis — Pasal 20 UU PDP)

Auditor TI wajib memverifikasi bahwa setiap sistem aplikasi yang mengumpulkan atau memproses Data Pribadi memiliki minimal **1 dari 7 Dasar Pemrosesan Sah** menurut **Pasal 20 ayat (2) UU PDP**:
1. **Persetujuan yang sah secara eksplisit (*Explicit Consent*)** dari Subjek Data Pribadi untuk 1 atau beberapa tujuan tertentu yang telah disampaikan (Pasal 20 ayat 2a & Pasal 22: wajib tertulis atau terekam secara elektronik, bukan *pre-ticked box*!).
2. **Pemenuhan kewajiban perjanjian/kontrak** di mana Subjek Data Pribadi merupakan salah satu pihak (Pasal 20 ayat 2b).
3. **Pemenuhan kewajiban hukum (*Legal Obligation*)** dari Pengendali Data Pribadi sesuai peraturan perundang-undangan (misal: pelaporan pajak atau KYC/AML perbankan — Pasal 20 ayat 2c).
4. **Pemenuhan pelindungan kepentingan vital (*Vital Interest*)** Subjek Data Pribadi (misal kondisi medis darurat — Pasal 20 ayat 2d).
5. **Pelaksanaan tugas dalam rangka kepentingan umum, pelayanan publik**, atau pelaksanaan kewenangan Pengendali Data Pribadi berdasarkan peraturan perundang-undangan (Pasal 20 ayat 2e).
6. **Pemenuhan kepentingan yang sah lainnya (*Legitimate Interest*)** dengan memperhatikan tujuan, kebutuhan, dan keseimbangan kepentingan Pengendali Data Pribadi dan hak Subjek Data Pribadi (Pasal 20 ayat 2f).

---

## 4.3 Hak Subjek Data Pribadi (Pasal 5 s.d. Pasal 15) & SLA Pemenuhannya

Sistem aplikasi organisasi wajib dirancang (*Privacy by Design*) agar mampu mengeksekusi **Hak Subjek Data Pribadi** berikut dalam batas waktu maksimal **3 x 24 jam (72 jam)** sejak permohonan diterima:

| Pasal UU PDP | Hak Subjek Data Pribadi | Batas Waktu SLA Hukum | Fitur Teknis yang Wajib Tersedia di Sistem Aplikasi |
| :---: | :--- | :---: | :--- |
| **Pasal 5** | Hak memperoleh informasi kejelasan identitas, tujuan permintaan, dan akuntabilitas (*Right to be Informed*). | Sebelum pengumpulan data | *Privacy Notice* yang jelas dan transparan pada layar pendaftaran/formulir. |
| **Pasal 6** | **Hak melengkapi, memperbarui, dan/atau memperbaiki kesalahan data (*Right to Rectification*).** | **Maksimal $3 \times 24$ Jam** *(Pasal 30 ayat 2)* | Fitur *Self-Service Profile Update* atau tiket koreksi data dengan log perubahan. |
| **Pasal 7** | **Hak mendapatkan akses dan memperoleh salinan Data Pribadi (*Right of Access*).** | **Maksimal $3 \times 24$ Jam** *(Pasal 32 ayat 2)* | Fitur ekspor data pengguna yang terverifikasi identitasnya. |
| **Pasal 8 & 43** | **Hak mengakhiri pemrosesan, menghapus, dan/atau memusnahkan Data Pribadi (*Right to Erasure / Right to be Forgotten*).** | Sesuai ketentuan retensi hukum | Prosedur penghapusan permanen (*hard delete / cryptographic erasure*) baik pada database utama maupun arsip setelah masa retensi undang-undang berakhir. |
| **Pasal 9 & 40** | **Hak menarik kembali persetujuan (*Right to Withdraw Consent*).** | **Maksimal $3 \times 24$ Jam** *(Pasal 40 ayat 2)* | Tombol pencabutan *consent* (*Opt-Out*) yang semudah saat memberikan *consent*. |
| **Pasal 10** | **Hak mengajukan keberatan atas tindakan pengambilan keputusan yang hanya didasarkan pada pemrosesan secara otomatis (*Automated Decision-Making / Profiling*, misal AI Credit Scoring).** | Sesuai prosedur keberatan | Mekanisme **Human-in-the-Loop (HITL)** untuk meninjau ulang keputusan otomatis AI jika diajukan keberatan oleh nasabah. |
| **Pasal 11** | **Hak menunda atau membatasi pemrosesan secara proporsional (*Right to Restrict Processing*).** | **Maksimal $3 \times 24$ Jam** *(Pasal 41 ayat 3)* | Flag pembekuan pemrosesan akun (`Restriction_Flag = True`) di database. |
| **Pasal 13** | **Hak menggunakan dan mengirimkan Data Pribadi ke Pengendali lain (*Data Portability*).** | Sesuai kemampuan interkonektivitas | Ekspor data dalam format terstruktur yang umum digunakan (JSON/CSV/XML) dan interkonektivitas API aman. |

---

## 4.4 Kewajiban Kritis Pengendali Data: ROPA, DPIA, DPO, Notifikasi 72 Jam, & Transfer Lintas Batas

### 1. Rekam Jejak Pemrosesan / ROPA (*Record of Processing Activities* — Pasal 31)
Pengendali Data Pribadi wajib melakukan **perekaman terhadap seluruh kegiatan pemrosesan Data Pribadi** (jenis data, tujuan, dasar hukum, lokasi penyimpanan, pihak penerima, masa retensi, dan kontrol keamanan).

### 2. Penilaian Dampak Pelindungan Data Pribadi / DPIA (*Data Protection Impact Assessment* — Pasal 34)
Pengendali Data **WAJIB melaksanakan DPIA** apabila pemrosesan memiliki **potensi risiko tinggi** terhadap Subjek Data, yang meliputi:
- Pengambilan keputusan secara otomatis (*automated decision-making / AI profiling*) yang menimbulkan akibat hukum atau dampak signifikan;
- Pemrosesan atas **Data Pribadi yang bersifat spesifik** (kesehatan, biometrik, keuangan, anak);
- Pemrosesan Data Pribadi dalam **skala besar (*large-scale processing*)**;
- Pemrosesan untuk kegiatan evaluasi, penskoran (*scoring*), atau pemantauan yang sistematis terhadap ruang publik; atau
- Penggunaan **teknologi baru** dalam pemrosesan Data Pribadi.

### 3. Kewajiban Menunjuk Pejabat Pelaksana Pelindungan Data Pribadi / DPO (*Data Protection Officer* — Pasal 53)
Pengendali Data dan Prosesor Data **WAJIB menunjuk DPO** apabila memenuhi **3 kondisi kumulatif/kriteria Pasal 53 ayat (1)**:
1. Pemrosesan Data Pribadi untuk **kepentingan pelayanan publik**;
2. Kegiatan inti Pengendali Data memiliki sifat, ruang lingkup, dan/atau tujuan yang memerlukan **pemantauan secara teratur dan sistematis atas Data Pribadi dengan skala besar**; dan/atau
3. Kegiatan inti Pengendali Data terdiri dari pemrosesan Data Pribadi dalam skala besar untuk **Data Pribadi yang bersifat spesifik** dan/atau berkaitan dengan **tindak pidana**.

### 4. Kewajiban Pemberitahuan Kegagalan Pelindungan Data Pribadi (Breach Notification $3 \times 24$ Jam — Pasal 46)
> [!CAUTION]
> **Aturan Mutlak Pasal 46 UU PDP (Sangat Kritis saat Audit Insiden Kebocoran Data!):**
> Dalam hal terjadi kegagalan Pelindungan Data Pribadi (*Data Breach / Ransomware Exfiltration*), Pengendali Data Pribadi **WAJIB menyampaikan pemberitahuan secara tertulis paling lambat $3 \times 24$ jam (72 Jam)** sejak kegagalan diketahui kepada:
> 1. **Subjek Data Pribadi** yang terdampak; DAN
> 2. **Lembaga Pelindungan Data Pribadi (Pemerintah)**.
>
> **Isi minimal pemberitahuan tertulis (Pasal 46 ayat 2):**
> - **(a)** Data Pribadi yang terungkap;
> - **(b)** Kapan dan bagaimana Data Pribadi terungkap; dan
> - **(c)** Upaya penanganan dan pemulihan atas terungkapnya Data Pribadi oleh Pengendali Data Pribadi.

### 5. Transfer Data Pribadi ke Luar Wilayah Hukum Indonesia (*Cross-Border Data Transfer* — Pasal 56)
Transfer Data Pribadi ke luar negeri hanya diizinkan secara bertingkat (**3-Tier Hierarchy Pasal 56**):
1. **Tingkat 1 (Kecukupan Negara — *Adequacy*):** Memastikan negara tempat kedudukan penerima memiliki tingkat pelindungan Data Pribadi yang **setara atau lebih tinggi** dari UU PDP;
2. **Tingkat 2 (Pelindungan Mengikat — *Appropriate Safeguards*):** Jika Tingkat 1 tidak terpenuhi, wajib memastikan terdapat **pelindungan Data Pribadi yang memadai dan bersifat mengikat** (misal *Standard Contractual Clauses [SCC]* / *Binding Corporate Rules [BCR]*);
3. **Tingkat 3 (Persetujuan Eksplisit — *Explicit Consent*):** Jika Tingkat 1 dan 2 tidak terpenuhi, **wajib memperoleh persetujuan eksplisit dari Subjek Data Pribadi**.

---

## 4.5 Sanksi Administratif (Denda 2% Pendapatan Tahunan) & Sanksi Pidana UU PDP

1. **Sanksi Administratif (Pasal 57 UU PDP):**
   - Peringatan tertulis;
   - Penghentian sementara kegiatan pemrosesan Data Pribadi;
   - Penghapusan atau pemusnahan Data Pribadi; dan/atau
   - **Denda administratif paling tinggi 2% (dua persen) dari pendapatan tahunan (*annual revenue/turnover*) atau penerimaan tahunan terhadap variabel pelanggaran!**
2. **Sanksi Pidana (Pasal 67 s.d. Pasal 73 UU PDP):**
   - Mengumpulkan, mengungkapkan, atau menggunakan Data Pribadi yang bukan miliknya secara melawan hukum: Pidana penjara **4 s.d. 5 tahun** dan/atau denda **Rp4 Miliar s.d. Rp5 Miliar**.
   - Memalsukan Data Pribadi untuk menguntungkan diri sendiri/merugikan orang lain: Pidana penjara **6 tahun** dan/atau denda **Rp6 Miliar**.
   - **Pidana Korporasi (Pasal 70):** Jika tindak pidana dilakukan oleh Korporasi, denda dapat dijatuhkan hingga **10 (sepuluh) kali lipat** dari ancaman denda maksimal (hingga **Rp60 Miliar**) ditambah perampasan keuntungan, pembekuan usaha, atau pembubaran korporasi!
