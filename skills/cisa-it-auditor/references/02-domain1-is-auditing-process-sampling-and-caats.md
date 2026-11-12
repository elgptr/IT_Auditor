# Bab 2: Domain 1 — Proses Audit Sistem Informasi, Statistical Sampling (IIA), dan CAATs (Bobot 21%)

> **Cakupan Materi:** Bab ini membahas secara mendalam **Domain 1 CISA (Information Systems Auditing Process — 21% / ~32 soal)** yang mencakup metodologi *Risk-Based Audit Planning*, model matematika Risiko Audit (`AR = IR × CR × DR`), klasifikasi kontrol internal, strategi *Compliance vs. Substantive Testing*, metodologi lengkap **Statistical & Non-Statistical Sampling** (berdasarkan *IIA Practice Guide: Internal Audit Sampling* dan *ISACA CRM 27e*), teknik **CAATs** (*Generalized Audit Software*, ITF, SCARF, Snapshot, Audit Hooks, Continuous Auditing), aturan keandalan bukti audit, *Control Self-Assessment* (CSA), serta penulisan temuan 5C.

---

## 2.1 Siklus Hidup Proses Audit Berbasis Risiko (Risk-Based Audit Lifecycle)

Berdasarkan **ITAF 1201** dan *CISA Review Manual 27e*, setiap penugasan audit SI harus mengikuti alur 9 langkah sistematis berikut:

```
[1. Memahami Bisnis & Konteks Strategis]
               │
               ▼
[2. Identifikasi & Klasifikasi Aset Informasi Kritis]
               │
               ▼
[3. Penilaian Risiko (Inherent Risk & Control Risk)]
               │
               ▼
[4. Penyusunan Rencana Audit & Program Kerja (Audit Program)]
               │
               ▼
[5. Survei Pendahuluan & Walkthrough (Understand Design)]
               │
               ▼
[6. Evaluasi Desain Kontrol (TDE - Test of Design Effectiveness)]
     ├── Desain TIDAK Efektif ──► [Perluas Substantive Testing & Catat Temuan Desain]
     └── Desain Efektif
               │
               ▼
[7. Pengujian Kepatuhan / Operasional (TOE - Compliance Testing)]
     ├── Kepatuhan Rendah ──────► [Perluas Substantive Testing & Catat Temuan TOE]
     └── Kepatuhan Tinggi
               │
               ▼
[8. Pengujian Substantif Terbatas (Substantive Testing)]
               │
               ▼
[9. Penyusunan Temuan 5C, Opini, Exit Meeting, LHA & Follow-up]
```

---

## 2.2 Model Matematika Risiko Audit (Audit Risk Model)

Risiko Audit (**Audit Risk / AR**) adalah risiko bahwa auditor memberikan opini yang salah (menyatakan kontrol efektif atau laporan bebas salah saji material, padahal terdapat kelemahan/salah saji material). Rumus fundamentalnya adalah:

$$\text{AR} = \text{IR} \times \text{CR} \times \text{DR}$$

| Komponen Risiko | Nama Lengkap | Definisi & Karakteristik | Siapa yang Mengendalikan? |
| :---: | :--- | :--- | :--- |
| **$\text{IR}$** | **Inherent Risk** *(Risiko Bawaan)* | Kerentanan suatu asersi, proses, atau aset terhadap kesalahan/kerugian material **dengan asumsi tidak ada kontrol internal yang diterapkan**. (Contoh: transaksi kas/kripto likuid memiliki IR jauh lebih tinggi daripada aset tetap gedung). | Tidak dikendalikan oleh auditor; melekat pada sifat bisnis/teknologi. |
| **$\text{CR}$** | **Control Risk** *(Risiko Kontrol)* | Risiko bahwa suatu kesalahan material yang terjadi **tidak dapat dicegah atau dideteksi secara tepat waktu oleh sistem pengendalian internal** organisasi. (Contoh: konfigurasi *password* lemah atau tidak adanya *Segregation of Duties*). | Dikendalikan oleh **Manajemen** melalui penerapan kontrol internal (ITGC & ITAC). |
| **$\text{DR}$** | **Detection Risk** *(Risiko Deteksi)* | Risiko bahwa prosedur pengujian dan *sampling* yang dilakukan oleh **auditor gagal mendeteksi** kesalahan atau kelemahan material yang sebenarnya telah lolos dari kontrol internal. | Dikendalikan **100% oleh Auditor** melalui ukuran sampel dan kualitas prosedur pengujian. |
| **$\text{AR}$** | **Audit Risk** *(Risiko Audit Total)* | Tingkat risiko keseluruhan yang bersedia diterima oleh auditor bahwa kesimpulan auditnya keliru (biasanya ditetapkan pada tingkat rendah, misal $5\%$ atau $1\%$). | Ditetapkan oleh **Auditor** sebagai target tingkat keyakinan (*Confidence Level* = $1 - \text{AR}$). |

> [!TIP]
> **Hubungan Terbalik dalam Ujian CISA:**
> Karena $\text{DR} = \frac{\text{AR}}{\text{IR} \times \text{CR}}$, apabila **Inherent Risk ($\text{IR}$)** dan **Control Risk ($\text{CR}$)** dinilai **TINGGI**, maka untuk menjaga **Audit Risk ($\text{AR}$)** tetap rendah, auditor wajib menurunkan **Detection Risk ($\text{DR}$)** menjadi **RENDAH** dengan cara **MEMPERBESAR ukuran sampel (*sample size*)** dan memperluas pengujian substantif!

---

## 2.3 Matriks Klasifikasi Kontrol Internal (Nature vs. Category)

Auditor SI mengevaluasi kontrol berdasarkan **Fungsi/Waktu Kerja (*Control Category*)** dan **Sifat Implementasi (*Control Nature*)**:

| Kategori Kontrol | Tujuan Utama | Contoh Kontrol Administratif / Manajerial | Contoh Kontrol Teknis / Logis (ITGC & ITAC) | Contoh Kontrol Fisik / Lingkungan |
| :--- | :--- | :--- | :--- | :--- |
| **Preventive** *(Pencegahan — Sebelum Kejadian)* | Mencegah terjadinya kesalahan, kelalaian, atau tindakan berbahaya sebelum masuk ke sistem. | • Kebijakan keamanan informasi<br>• *Segregation of Duties* (SoD)<br>• *Background check* karyawan baru<br>• Pelatihan *security awareness* | • *Access Control List* (ACL) & RBAC<br>• Enkripsi data & komunikasi (TLS/AES)<br>• *Input validation / Field check* pada form<br>• Firewall *packet filtering* | • *Mantrap* / *Turnstile*<br>• Pagar keliling & kunci biometrik<br>• Penempatan ruang server di lantai tengah |
| **Detective** *(Deteksi — Saat / Setelah Kejadian)* | Mendeteksi dan melaporkan kesalahan atau pelanggaran yang gagal dicegah oleh kontrol preventif. | • *Review* berkala log aktivitas oleh supervisor<br>• Audit internal / eksternal berkala<br>• Rotasi jabatan (*job rotation*) & cuti wajib (*mandatory vacation*) | • *Intrusion Detection System* (IDS) & SIEM<br>• *Hash totals* & *Batch balancing*<br>• *Check digit verification*<br>• Laporan *exception* & *error log* | • Kamera CCTV (rekaman)<br>• Sensor gerak (*motion detector*)<br>• Detektor asap & panas (*smoke detector*) |
| **Corrective** *(Korektif — Pemulihan Dampak)* | Meminimalisir dampak ancaman, memperbaiki kesalahan, dan memulihkan operasional ke kondisi normal. | • Prosedur *Business Continuity Plan* (BCP) & DRP<br>• Tindakan disipliner SDM<br>• Klaim asuransi siber (*cyber insurance*) | • *Restore* data dari *backup tape/cloud*<br>• *Database rollback / Transaction log recovery*<br>• *Antivirus quarantine & removal*<br>• *Patching* kerentanan | • Pemadam api *FM-200 / Dry-pipe sprinkler*<br>• UPS & Generator listrik cadangan |
| **Compensating** *(Kompensasi — Pengganti)* | Kontrol alternatif ketika kontrol utama tidak dapat diterapkan (misal karena keterbatasan jumlah staf pada organisasi kecil). | • **Supervisi ketat & *review* jejak audit (*audit trail*) secara independen oleh manajemen** atas seluruh aktivitas pengguna yang memiliki konflik SoD. | • Pencatatan log otomatis yang tidak dapat diubah (*immutable logging / WORM*) atas penggunaan akun *FireCall / Emergency ID*. | • Pendampingan fisik (*escort*) penuh waktu bagi vendor di ruang server. |

---

## 2.4 Pengujian Kepatuhan (Compliance Testing) vs. Pengujian Substantif (Substantive Testing)

| Dimensi | Compliance Testing (Test of Controls / TOE) | Substantive Testing (Test of Details & Balances) |
| :--- | :--- | :--- |
| **Pertanyaan Inti** | *"Apakah kontrol internal diterapkan secara konsisten sesuai kebijakan/prosedur?"* | *"Apakah integritas data, transaksi, atau saldo laporan benar dan bebas dari salah saji material?"* |
| **Fokus Pengujian** | Menguji **atribut proses/kontrol** (Ada/Tidak ada persetujuan, tepat waktu/terlambat). | Menguji **nilai moneter, kuantitas, dan akurasi data** transaksi secara langsung. |
| **Contoh Prosedur Audit TI** | Memeriksa sampel 25 tiket *Change Request* untuk memastikan seluruhnya memiliki *sign-off* UAT dan persetujuan CAB sebelum migrasi ke produksi. | Menjalankan skrip SQL/GAS untuk merekonsiliasi 100% total nilai *General Ledger* (GL) dengan *Sub-ledger* piutang, atau menghitung ulang bunga kredit nasabah. |
| **Metode Sampling yang Digunakan** | **Attribute Sampling** (termasuk *Stop-or-Go* dan *Discovery Sampling*). | **Variable Sampling** (termasuk *Stratified Mean per Unit* dan *Monetary Unit Sampling / MUS*). |
| **Keterkaitan Timbal Balik** | Jika hasil *Compliance Testing* menunjukkan kontrol **andal (kuat)** $\rightarrow$ cakupan *Substantive Testing* dapat **dikurangi**. Jika kontrol **lemah** $\rightarrow$ *Substantive Testing* wajib **diperluas** (atau auditor langsung ke *Substantive Testing* jika *Control Risk* sudah 100%). | Membuktikan dampak aktual (moneter/data) dari kelemahan kontrol yang ditemukan pada *Compliance Testing*. |

---

## 2.5 Metodologi Lengkap Audit Sampling (ISACA CRM & IIA Practice Guide)

Berdasarkan **IIA Whitepaper: Internal Audit Sampling** dan **ISACA CISA Review Manual**, *sampling* adalah penerapan prosedur audit terhadap kurang dari $100\%$ item dalam suatu populasi sehingga seluruh unit *sampling* memiliki peluang untuk dipilih.

### A. Statistical vs. Non-Statistical (Judgmental) Sampling

| Aspek | Statistical Sampling (Probabilistik) | Non-Statistical / Judgmental Sampling |
| :--- | :--- | :--- |
| **Pemilihan Sampel** | Menggunakan metode pemilihan acak berbasis probabilitas (*Random Number Generator* atau *Monetary Interval*). | Berdasarkan pertimbangan subjektif (*professional judgment*) auditor (misal: *Haphazard* atau *Block Selection* / memilih semua transaksi berisiko tinggi). |
| **Kuantifikasi Risiko Sampling** | Risiko *sampling* dapat diukur secara matematis (*Confidence Level* & *Precision*). | Risiko *sampling* **tidak dapat diukur secara matematis**. |
| **Ekstrapolasi ke Populasi** | Hasil sampel **DAPAT diekstrapolasi (diproyeksikan)** secara sah ke seluruh populasi. | Hasil sampel **TIDAK BOLEH diekstrapolasi** secara matematis ke seluruh populasi (hanya berlaku untuk sampel yang diuji). |

### B. Lima Metode Pemilihan & Jenis Sampling Utama CISA

1. **Attribute Sampling (Pengujian Kepatuhan / Biner):**
   - Menilai tingkat keterjadian (*occurrence rate*) suatu karakteristik/atribut (Patuh vs. Tidak Patuh; Ada Otorisasi vs. Tidak Ada Otorisasi).
   - Digunakan untuk **Compliance Testing (TOE)**.
2. **Stop-or-Go Sampling (Sequential Attribute Sampling):**
   - Turunan dari *Attribute Sampling* yang digunakan ketika auditor meyakini bahwa **hampir tidak ada kesalahan (very few errors)** yang akan ditemukan dalam populasi.
   - Memungkinkan auditor menghentikan pengujian sedini mungkin (*stop early*) setelah memeriksa jumlah sampel minimum dengan 0 deviasi, sehingga menghemat waktu audit.
3. **Discovery Sampling:**
   - Varian dari *Attribute Sampling* dengan **Expected Error Rate = 0%**, digunakan khusus ketika auditor mencari **kasus kritis tunggal (Zero Tolerance)** seperti kecurangan (*fraud*), penggelapan, atau pelanggaran hukum/keamanan fatal.
   - Begitu **1 deviasi/kasus ditemukan**, *sampling* dihentikan dan auditor beralih ke investigasi penuh.
4. **Variable Sampling (Pengujian Substantif / Kuantitatif):**
   - Digunakan untuk mengestimasi nilai moneter, berat, atau besaran numerik suatu populasi (digunakan dalam **Substantive Testing**).
   - Varian utamanya adalah **Stratified Mean Per Unit (MPU)** (membagi populasi menjadi beberapa *strata* nilai untuk menurunkan standar deviasi $\sigma$ dan memperkecil ukuran sampel), **Unstratified MPU**, dan **Difference/Ratio Estimation**.
5. **Monetary Unit Sampling (MUS) / Probability-Proportional-to-Size (PPS) / Dollar-Unit Sampling:**
   - Hibrida antara metode atribut dan variabel di mana setiap **$1 (atau Rp1) mata uang** dalam populasi menjadi 1 unit *sampling*.
   - Item bernilai besar secara otomatis memiliki peluang terpilih lebih tinggi (bahkan $100\%$ jika nilai item $\ge$ *Sampling Interval*). Sangat efektif untuk mendeteksi **lebih saji (*overstatement*)** pada nilai aset atau transaksi.

### C. Parameter & Rumus Matematika Statistical Sampling (IIA Standard)

#### 1. Tabel Faktor Keandalan Poisson ($R$-Factor) untuk Attribute Sampling & MUS
Berdasarkan *IIA Internal Audit Sampling Guide*, faktor keandalan (**Reliability Factor / $R$**) berdasarkan distribusi Poisson untuk tingkat keyakinan (*Confidence Level*) dan jumlah kesalahan yang diharapkan (*Expected Deviations*):

| Jumlah Deviasi Diharapkan ($c$) | Confidence Level 90% ($\alpha = 10\%$) | Confidence Level 95% ($\alpha = 5\%$) | Confidence Level 99% ($\alpha = 1\%$) |
| :---: | :---: | :---: | :---: |
| **0 Deviasi (Zero Error)** | **$2.31$** | **$3.00$** | **$4.61$** |
| **1 Deviasi** | $3.89$ | $4.75$ | $6.64$ |
| **2 Deviasi** | $5.33$ | $6.30$ | $8.41$ |
| **3 Deviasi** | $6.69$ | $7.76$ | $10.05$ |

#### 2. Rumus Ukuran Sampel Attribute Sampling & Discovery Sampling
Untuk populasi besar ($N > 500$) dengan pendekatan Poisson:
$$n = \frac{R(\text{Confidence Level}, \text{Expected Deviations})}{\text{Tolerable Error Rate (TER)}}$$

*Contoh Perhitungan:*
- Jika auditor menginginkan **Confidence Level = 95%**, **Expected Error = 0**, dan **Tolerable Error Rate (TER) = 5% (0.05)**:
  $$n = \frac{3.00}{0.05} = \mathbf{60\text{ sampel}}$$
- Untuk pendekatan distribusi Normal (ketika *Expected Error Rate* $p > 0$):
  $$n_0 = \frac{Z^2 \times p \times (1 - p)}{\text{Precision}^2}, \quad n = \frac{n_0}{1 + \frac{n_0}{N}}$$
  Di mana nilai koefisien normal standar ($Z$, *two-tailed*): **90% = $1.645$**, **95% = $1.960$**, **99% = $2.576$**.

#### 3. Rumus Monetary Unit Sampling (MUS / PPS)
Diketahui nilai buku populasi total (**Book Value / $BV$**), salah saji yang dapat ditoleransi (**Tolerable Misstatement / $TM$**), dan faktor keandalan Poisson $R$:
$$\text{ Ukuran Sampel MUS } (n) = \frac{BV \times R}{TM}$$
$$\text{ Sampling Interval } (SI) = \frac{BV}{n} = \frac{TM}{R}$$
- Setiap transaksi yang memiliki nilai buku $\ge SI$ akan terpilih **100% secara otomatis (*Top-Stratum Items*)**.

#### 4. Rumus Variable Sampling (Mean-Per-Unit / MPU)
Diketahui ukuran populasi $N$, estimasi standar deviasi populasi $\sigma$, koefisien $Z$, dan presisi/toleransi total salah saji $A$ (di mana presisi per unit $e = A / N$):
$$n_0 = \left( \frac{N \times Z \times \sigma}{A} \right)^2 = \left( \frac{Z \times \sigma}{e} \right)^2$$
Dengan koreksi populasi terbatas (*Finite Population Correction* / FPC):
$$n = \frac{n_0}{1 + \frac{n_0}{N}}$$

#### 5. Tabel Pedoman Praktis Ukuran Sampel ITGC (SOX / Big-4 Rule of Thumb)
Ketika menguji kontrol manual berbasis frekuensi tetap dalam ITGC (seperti *SOXIT.01*–*SOXIT.04*), standar praktik industri menetapkan ukuran sampel minimum berikut untuk mencapai *Confidence Level* 90%–95% dengan **0 deviasi**:

| Frekuensi Pelaksanaan Kontrol | Estimasi Populasi Tahunan ($N$) | Ukuran Sampel Minimum ($n$) | Contoh Kontrol ITGC |
| :--- | :---: | :---: | :--- |
| **Tahunan (Annually)** | $1$ | **$1$** | Pengujian *Disaster Recovery Plan* (DRP) tahunan; peninjauan kebijakan keamanan tahunan. |
| **Kuartalan (Quarterly)** | $4$ | **$2$** | *User Access Review* (UAR) kuartalan atas hak akses pengguna aplikasi/DB; *review* akun *dormant*. |
| **Bulanan (Monthly)** | $12$ | **$2\text{ s.d. } 3$** | Laporan kinerja kapasitas bulanan; rekonsiliasi log *backup* bulanan. |
| **Mingguan (Weekly)** | $52$ | **$5$** | *Backup full tape offsite* mingguan; rapat *Change Advisory Board* (CAB) mingguan. |
| **Harian (Daily)** | $250 - 365$ | **$20\text{ s.d. } 25$** | Pemantauan *batch job* harian; pencocokan log operator harian. |
| **Berulang / Transaksional (>250/thn)** | $> 250$ | **$25\text{ s.d. } 60$** | Tiket pengguna baru (*New Hire*), mutasi/terminasi SDM, tiket *Change Request* aplikasi/infrastruktur. |
| **Automated Control (Kontrol Otomatis)** | Konsisten | **$1\text{ (Sample of One)}$** | Parameter *password policy* di OS/DB (`PASS_MIN_LEN`, `FAILED_LOGIN_ATTEMPTS`), dengan syarat **ITGC atas Change Management & Access Control terbukti efektif**! |

> [!WARNING]
> **Prinsip "Sample of One" untuk Kontrol Otomatis (Benchmarking):**
> Auditor hanya boleh menguji **1 sampel transaksi (*Sample of One*)** untuk kontrol aplikasi otomatis (misal validasi sistem atau konfigurasi parameter) **HANYA JIKA** *General Controls* (khususnya *Program Change Management* dan *Logical Access Control*) telah diuji dan terbukti efektif sehingga konfigurasi tidak berubah sepanjang periode audit.

---

## 2.6 Computer-Assisted Audit Techniques (CAATs) & Continuous Auditing

Dalam lingkungan terkomputerisasi yang memproses jutaan transaksi tanpa jejak kertas (*paperless*), auditor SI tidak boleh lagi hanya melakukan *auditing around the computer* (hanya mencocokkan input dan output), melainkan wajib melakukan *auditing through the computer* menggunakan **CAATs**:

| Teknik CAATs / Continuous Auditing | Cara Kerja Teknis | Keunggulan Utama | Risiko / Kelemahan yang Harus Diwaspadai Auditor |
| :--- | :--- | :--- | :--- |
| **GAS (Generalized Audit Software)**<br>*(IDEA, ACL/Galvanize, SQL, Python)* | Perangkat lunak yang mengekstrak dan menganalisis **100% populasi data** dari berbagai sistem/DBMS secara *read-only* tanpa mengubah data produksi. | Mampu mendeteksi *fraud* (analisis Hukum Benford, *gap detection* nomor urut faktur, *duplicate payment*, *join* tabel karyawan aktif vs. *user ID* aktif). | Membutuhkan pemahaman skema *database* (*data dictionary*) dan integritas proses ekstraksi data (*completeness check*). |
| **Test Data (Data Uji)** | Auditor memasukkan serangkaian transaksi tiruan (valid dan tidak valid) ke dalam salinan program aplikasi di lingkungan uji (*non-production*). | Menguji logika *input validation* dan perhitungan aplikasi tanpa mengotori data produksi. | Sulit memastikan bahwa *source code* di lingkungan uji 100% identik dengan program yang sedang berjalan di produksi. |
| **ITF (Integrated Test Facility)** | Membuat **entitas tiruan (*dummy entity/branch/customer*)** di dalam **database produksi langsung**, lalu memproses transaksi uji bersama transaksi nyata selama operasi normal. | Menguji aplikasi secara langsung di lingkungan produksi nyata secara berkelanjutan tanpa menghentikan operasi. | **Risiko Kontaminasi Data Produksi:** Transaksi uji pada *dummy entity* harus dihapus (*reversed/excluded*) agar tidak menggelembungkan laporan keuangan perusahaan! |
| **SCARF (Systems Control Audit Review File)** | Menanamkan modul audit (*embedded audit module*) di dalam kode aplikasi produksi untuk terus-menerus memantau transaksi dan mencatat transaksi yang melewati ambang batas ke dalam file khusus auditor (*SCARF file*). | Mendeteksi anomali secara terus-menerus (*continuous monitoring*) untuk transaksi yang memenuhi kriteria risiko auditor. | Membebani performa/CPU sistem produksi jika logika penyaringan terlalu kompleks. |
| **Snapshot (Pemotretan Memori)** | Mengambil "potret" status memori dan variabel data sebelum dan sesudah pemrosesan instruksi program yang kritis. | Membantu melacak perubahan nilai variabel secara presisi pada titik eksekusi logika program tertentu. | Membutuhkan keahlian pemrograman tingkat tinggi dan dukungan fitur dari sistem aplikasi. |
| **Audit Hooks (Kait Audit)** | Rutin perangkat lunak (*exit routines*) yang ditanamkan dalam sistem untuk memberi peringatan instan (*real-time alert*) kepada auditor/keamanan sebelum atau sesudah transaksi mencurigakan terjadi. | Memungkinkan intervensi *real-time* sebelum dana keluar atau kerusakan meluas (contoh: mendeteksi perubahan *master vendor bank account*). | Harus dilindungi secara ketat agar tidak dimodifikasi oleh programmer. |
| **CIS (Continuous and Intermittent Simulation)** | Sistem manajemen database (DBMS) mensimulasikan instruksi aplikasi untuk setiap transaksi yang memenuhi kriteria, lalu membandingkan hasil simulasi dengan hasil aplikasi. | Memverifikasi akurasi pemrosesan transaksi bernilai tinggi secara langsung di dalam DBMS. | Menambah *overhead* waktu pemrosesan transaksi pada DBMS. |

---

## 2.7 Hierarki Keandalan Bukti Audit (ITAF 1205 — Audit Evidence Reliability)

Dalam soal ujian CISA yang menanyakan *"Manakah bukti audit yang PALING andal (MOST reliable)?"*, gunakan urutan hierarki mutlak berikut dari yang **Paling Andal (1)** hingga **Paling Kurang Andal (5)**:

1. **Bukti Teknis/Objektif yang Dihasilkan Langsung oleh Auditor (*Auditor-Generated / Re-performance / Direct Observation*):**
   - Hasil eksekusi skrip CAATs/SQL oleh auditor sendiri, hasil *penetration test* independen, observasi langsung proses *physical inventory* atau hasil query konfigurasi langsung dari *server* produksi di hadapan auditor.
2. **Bukti Dokumenter dari Pihak Ketiga Independen (*External Independent Confirmation*):**
   - Konfirmasi saldo langsung dari bank/klien eksternal ke auditor, laporan **SOC 1 Type 2 / SOC 2 Type 2** dari auditor independen pihak ketiga.
3. **Bukti Sistem Otomatis Internal dengan ITGC yang Kuat (*System-Generated Logs with Strong Controls*):**
   - Log sistem (*immutable syslog*, log *firewall*, *transport log* SAP) di mana auditor tidak memiliki akses *write*/admin.
4. **Bukti Dokumenter Internal yang Dibuat oleh Auditee (*Internal Documentary Evidence*):**
   - Formulir permintaan akses bertanda tangan, notulen rapat CAB, tangkapan layar (*screenshot*) yang dikirim oleh staf TI (wajib diverifikasi keasliannya termasuk *timestamp* dan nama *host/server*!).
5. **Pernyataan Lisan / Wawancara (*Oral Inquiry / Self-Reporting / Representation*):**
   - Jawaban wawancara staf atau kuesioner mandiri. **Tidak pernah cukup berdiri sendiri** tanpa bukti koroboratif!

---

## 2.8 Control Self-Assessment (CSA) & Format Temuan Audit 5C

### A. Control Self-Assessment (CSA)
CSA adalah metodologi di mana **manajemen dan staf operasional lini pertama** terlibat langsung dalam menilai efektivitas kontrol internal dan risiko di area kerja mereka sendiri (melalui *Facilitated Workshops*, kuesioner, atau analisis manajemen).
- **Manfaat Utama CSA:** Meningkatkan kesadaran kontrol (*control awareness*), mendeteksi risiko lebih dini oleh pemilik proses (*process owners*), dan membantu fungsi audit internal memfokuskan sumber daya pada area berisiko tinggi.
- **Batas CSA (Jebakan Ujian CISA):** CSA **BUKAN pengganti (*NOT a substitute*)** fungsi Audit Internal independen! Dalam CSA, peran auditor SI berubah menjadi **fasilitator (*facilitator*)**, bukan pengambil keputusan kontrol.

### B. Struktur Baku Temuan Audit 5C ISACA
Setiap temuan dalam Laporan Hasil Audit (LHA) sesuai **ITAF 1401** harus memuat 5 elemen (**5C**) ditambah Tanggapan Manajemen:
1. **Condition (Kondisi / Fakta Aktual):** Apa yang ditemukan secara faktual beserta jumlah sampel dan referensi bukti (*working paper*).
2. **Criteria (Kriteria / Standar):** Apa yang seharusnya terjadi menurut kebijakan perusahaan, standar (COBIT/ISO 27001), atau regulasi.
3. **Cause (Sebab Akar / Root Cause):** Mengapa deviasi terjadi (ketiadaan kontrol otomatis, kegagalan prosedur terminasi SDM, kurangnya supervisi).
4. **Consequence / Effect (Dampak / Risiko Bisnis):** Apa risiko nyata atau potensi kerugian finansial/operasional/kepatuhan jika kondisi dibiarkan.
5. **Corrective Action / Recommendation (Rekomendasi):** Tindakan perbaikan yang praktis, terukur, dan hemat biaya (*cost-effective*), dilengkapi dengan **Management Response, Action Owner, dan Target Implementation Date**.
