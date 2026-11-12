# Bab 13: Masterclass "ISACA Exam Mindset" & Bank Skenario Soal CISA (QAE — Questions, Answers & Explanations)

> **Cakupan Materi:** Bab ini dirancang khusus untuk menguasai cara berpikir **ISACA Mindset** dalam menjawab soal-soal skenario jebakan ujian CISA (*FIRST, NEXT, BEST, MOST, PRIMARY, GREATEST CONCERN*) sekaligus panduan pengambilan keputusan cepat bagi auditor di lapangan melalui **30 Skenario Kasus Inti Lintas 5 Domain**.

---

## 13.1 Sepuluh Hukum Emas "ISACA Exam Mindset" (Cara Menjawab Soal CISA Tanpa Meleset)

Dalam ujian CISA, keempat pilihan jawaban (`A`, `B`, `C`, `D`) sering kali tampak benar secara teknis. Untuk memilih **1 Jawaban Terbaik menurut ISACA**, terapkan **10 Hukum Emas** berikut:

1. **Berpikirlah sebagai Auditor / Penasihat Strategis, BUKAN Teknisi TI (Think Like an Auditor/Manager, Not a Technician):**
   - IS Auditor **TIDAK PERNAH** memperbaiki sendiri konfigurasi firewall, menulis ulang kode program, mencabut langsung akun pengguna, atau menghentikan proyek TI!
   - Tugas auditor adalah **Mengevaluasi (*Evaluate*), Meninjau (*Review*), Memverifikasi (*Verify*), Menguji (*Test*), Mendokumentasikan (*Document*), dan Melaporkan/Merekomendasikan (*Report/Recommend*)** kepada manajemen.
2. **Perhatikan Kata Kunci Berhuruf Kapital: `FIRST` / `NEXT` vs. `BEST` / `MOST EFFECTIVE`:**
   - Jika soal bertanya **"What should the IS auditor do FIRST / NEXT?"**: Pilih jawaban yang berfokus pada **Memahami situasi, memverifikasi fakta, meninjau kebijakan/dokumentasi, melakukan analisis dampak (*Assess/Determine/Verify*)** sebelum mengambil tindakan eskalasi atau pelaporan!
   - Jika soal bertanya **"What is the BEST / MOST effective control?"**: Pilih jawaban yang bersifat **Preventive & Automated (Otomatis & Mencegah di Awal)** atau yang menyelesaikan **Akar Masalah (*Root Cause*)** secara menyeluruh!
3. **Keselamatan Jiwa Manusia Selalu Nomor 1 (Human Life Safety First):**
   - Dalam skenario bencana fisik atau kebakaran pusat data, jawaban yang menyangkut keselamatan nyawa manusia selalu mengalahkan penyelamatan data atau perangkat keras.
4. **Bisnis Mengemudikan TI, Bukan Sebaliknya (Business Drives IT):**
   - Setiap investasi TI, proyek SDLC, RPO/RTO, atau kebijakan keamanan harus didasarkan pada **Kebutuhan Bisnis (*Business Objectives*), Business Case, dan hasil Business Impact Analysis (BIA)**.
5. **Biaya Kontrol Tidak Boleh Melebihi Nilai Aset / Risiko ($\text{Cost of Control} \le \text{ALE}$):**
   - Kontrol keamanan terbaik bukanlah kontrol yang paling canggih/mahal, melainkan kontrol yang **paling seimbang secara biaya-manfaat (*Cost-Effective*)** untuk menurunkan risiko ke tingkat yang dapat diterima (*Acceptable Risk Level*).
6. **Akuntabilitas Tidak Pernah Bisa Dialihkan ke Vendor (Accountability Cannot Be Outsourced):**
   - Meskipun operasional TI atau *Cloud* dialihdayakan 100% ke pihak ketiga, **Manajemen Organisasi Klien tetap memikul akuntabilitas penuh** atas keamanan data dan kepatuhan regulasi.
7. **Pemisahan Tugas (SoD) vs. Kontrol Kompensasi pada Organisasi Kecil:**
   - Idealnya: **Segregation of Duties (SoD)** secara preventif.
   - Namun jika soal menyebutkan **"In a small organization with limited staff where SoD is not feasible..."**: Jangan menjawab *"Rekrut staf baru"*! Pilih **Compensating Control** berupa **Independent Review of Audit Trails / Activity Logs by Management**.
8. **Data Owner (Bisnis) Menyetujui, Security Admin Mengeksekusi:**
   - Hanya **Data Owner** (Manajer Unit Bisnis) yang berhak menentukan klasifikasi data dan menyetujui pemberian akses. Departemen TI / Security Admin hanya menjalankan instruksi tersebut.
9. **Ketika Menemukan Kelemahan Kontrol selama Compliance Testing:**
   - Langkah auditor selanjutnya adalah **Mengevaluasi potensi dampak risiko bisnis dan memperluas Pengujian Substantif (*Expand Substantive Testing*)** untuk mengetahui apakah kelemahan tersebut telah menyebabkan kesalahan data/kerugian nyata.
10. **Bukti Audit Paling Andal (*MOST Reliable Evidence*):**
    - Urutan pemenang mutlak: **Observasi/Ekstraksi/Re-performance langsung oleh Auditor** $>$ **Konfirmasi Pihak Ketiga Independen** $>$ **Log Sistem Otomatis** $>$ **Dokumen Internal** $>$ **Pernyataan Lisan (*Inquiry*)**.

---

## 13.2 Bank 30 Skenario Kasus Inti CISA (QAE) Lintas 5 Domain Beserta Bedah Logika

### A. Skenario Domain 1 — Proses Audit Sistem Informasi (Skenario 1–6)

| No | Skenario Pertanyaan Ujian CISA | Pilihan Jawaban Terbaik (ISACA) | Mengapa Pilihan Lain Salah (Bedah Jebakan)? |
| :-: | :--- | :--- | :--- |
| **1** | Manajemen meminta IS Auditor untuk ikut menandatangani persetujuan (*sign-off*) pada setiap tahap proyek implementasi ERP baru agar proyek terkendali. Apa yang harus dilakukan auditor? | **Menolak menandatangani persetujuan manajemen, namun tetap memberikan rekomendasi kontrol sebagai penasihat independen.** | Jika auditor ikut melakukan *sign-off* keputusan operasional proyek, auditor **kehilangan Objektivitas & Independensi (ITAF `1002/1003`)** saat harus mengaudit sistem tersebut pasca-implementasi (*Self-Review Threat*). |
| **2** | Saat menguji sampel 50 tiket perubahan program, auditor menemukan 3 perubahan dilakukan tanpa persetujuan UAT. Apa yang harus dilakukan auditor **PERTAMA KALI (FIRST)**? | **Memeriksa sifat dan dampak dari ketiga perubahan tanpa izin tersebut (apakah perubahan darurat atau menyentuh logika kritis).** | Jangan langsung melapor ke Komite Audit atau langsung menambah 100 sampel baru sebelum memahami *mengapa* deviasi tersebut terjadi dan seberapa material dampaknya! |
| **3** | Auditor ingin mendeteksi apakah terdapat minimal 1 kasus penyalahgunaan wewenang kritis (Zero Tolerance Fraud) dalam populasi 10.000 transaksi. Metode *sampling* apa yang **PALING TEPAT**? | **Discovery Sampling.** | *Attribute Sampling* biasa digunakan untuk mengestimasi persentase kepatuhan umum, *Stop-or-Go* untuk menghentikan sampel lebih cepat saat populasi diyakini bebas error, dan *Variable Sampling* untuk nilai moneter. |
| **4** | Auditor menemukan bahwa *Control Risk* pada proses perubahan database sangat tinggi (lemah). Bagaimana dampaknya terhadap *Detection Risk* dan strategi pengujian? | **Target *Detection Risk* harus DITURUNKAN dengan cara memperbesar ukuran sampel dan memperluas *Substantive Testing*.** | Menurut rumus $\text{AR} = \text{IR} \times \text{CR} \times \text{DR}$, ketika $\text{CR}$ naik, $\text{DR}$ wajib turun agar risiko audit total ($\text{AR}$) tetap rendah. |
| **5** | Pada *Exit Meeting*, manajemen *auditee* mengakui fakta temuan namun menolak rekomendasi auditor karena dinilai terlalu mahal dan mengusulkan kontrol alternatif. Apa langkah auditor? | **Mengevaluasi apakah kontrol alternatif yang diusulkan manajemen cukup efektif untuk memitigasi risiko ke tingkat yang dapat diterima.** | Auditor tidak boleh memaksakan satu cara teknis tertentu jika manajemen memiliki solusi alternatif yang lebih hemat biaya dan sama-sama mampu memitigasi risiko bisnis! |
| **6** | Teknik CAATs manakah yang memungkinkan pengujian transaksi aplikasi secara terus-menerus langsung di lingkungan produksi menggunakan entitas tiruan tanpa menghentikan sistem? | **Integrated Test Facility (ITF).** | Namun ingat: Risiko utama ITF adalah **kontaminasi data produksi** jika transaksi uji pada entitas tiruan tidak dikeluarkan dari laporan keuangan akhir! |

---

### B. Skenario Domain 2 — Tata Kelola & Manajemen TI (Skenario 7–12)

| No | Skenario Pertanyaan Ujian CISA | Pilihan Jawaban Terbaik (ISACA) | Mengapa Pilihan Lain Salah (Bedah Jebakan)? |
| :-: | :--- | :--- | :--- |
| **7** | Apa indikator **PALING PENTING** bahwa Tata Kelola TI (*IT Governance*) di suatu perusahaan telah berjalan efektif? | **Strategi dan proyek TI selaras penuh serta mendukung pencapaian tujuan strategis bisnis (*Business-IT Strategic Alignment*).** | Kepatuhan anggaran TI atau rendahnya jumlah insiden teknis adalah ukuran *manajemen operasional*, bukan ukuran utama keberhasilan *IT Governance*. |
| **8** | Siapakah yang paling tepat mengetuai **IT Steering Committee** dan apa tugas utamanya? | **Eksekutif Bisnis Senior; bertugas menentukan prioritas proyek TI, menyetujui alokasi sumber daya/anggaran proyek, dan memantau progres pengiriman proyek.** | Jika hanya diketuai oleh CIO tanpa kepemimpinan bisnis, prioritas proyek cenderung didorong oleh keinginan teknologi (*technology-driven*), bukan kebutuhan bisnis. |
| **9** | Dalam organisasi TI yang kecil, seorang DBA merangkap sebagai System & Security Administrator. Apa kontrol kompensasi **TERBAIK**? | **Mencatat seluruh aktivitas DBA/Admin ke dalam log yang tidak dapat diubah oleh DBA (*immutable remote log*) dan ditinjau secara berkala oleh manajemen independen.** | Mengandalkan kejujuran staf (*NDA*) atau *background check* saja tidak mendeteksi penyalahgunaan hak akses harian. |
| **10** | Perusahaan berencana mengalihdayakan pemrosesan *Payroll* dan *General Ledger* ke vendor Cloud SaaS. Laporan audit pihak ketiga manakah yang **PALING RELEVAN** untuk menilai efektivitas operasional kontrol keuangan vendor? | **Laporan SOC 1 Type 2.** *(Jika untuk mengevaluasi keamanan siber, ketersediaan, dan kerahasiaan teknis Cloud $\rightarrow$ **SOC 2 Type 2**).* | Laporan *Type 1* hanya menilai desain pada satu tanggal (*point-in-time*) dan tidak membuktikan bahwa kontrol beroperasi secara efektif selama periode waktu! |
| **11** | Seorang karyawan di posisi administrator jaringan diberhentikan secara tidak sukarela (*involuntary termination*). Kapan hak aksesnya harus dicabut? | **Segera sebelum atau tepat pada saat karyawan tersebut diberitahu mengenai pemberhentiannya.** | Menunggu hingga akhir bulan atau setelah *exit interview* memberi celah waktu bagi karyawan yang marah untuk melakukan sabotase atau mencuri data. |
| **12** | Nilai aset server adalah $\$500.000$, *Exposure Factor* $50\%$, dan *ARO* $0,1$ (sekali dalam 10 tahun). Vendor menawarkan solusi kontrol seharga $\$35.000/\text{tahun}$. Apa rekomendasi auditor? | **Tidak merekomendasikan pembelian kontrol tersebut karena biaya tahunan kontrol ($\$35.000$) melebihi nilai ALE ($\$25.000/\text{tahun}$).** | Hitungan: $\text{SLE} = \$500.000 \times 0,5 = \$250.000$; $\text{ALE} = \$250.000 \times 0,1 = \$25.000/\text{tahun}$. Biaya kontrol tidak boleh lebih mahal daripada potensi kerugian tahunan! |

---

### C. Skenario Domain 3 — Akuisisi, Pengembangan, & Implementasi SI (Skenario 13–18)

| No | Skenario Pertanyaan Ujian CISA | Pilihan Jawaban Terbaik (ISACA) | Mengapa Pilihan Lain Salah (Bedah Jebakan)? |
| :-: | :--- | :--- | :--- |
| **13** | Pada fase SDLC manakah kebutuhan kontrol keamanan aplikasi dan jejak audit (*audit trail*) harus didefinisikan? | **Fase Definisi Kebutuhan (*Requirements Definition Phase*) — sedini mungkin!** | Menambahkan kontrol keamanan setelah sistem selesai dikodekan (pada fase *Testing/Implementation*) akan membutuhkan biaya perombakan berkali-kali lipat lebih mahal. |
| **14** | Sebuah proyek pengembangan perangkat lunak memiliki $\text{BAC} = \$100.000$, $\text{PV} = \$60.000$, $\text{EV} = \$45.000$, dan $\text{AC} = \$55.000$. Bagaimana kondisi proyek tersebut? | **Proyek mengalami pembengkakan biaya (*Cost Overrun*, $\text{CV} = -\$10.000$, $\text{CPI} = 0,82$) DAN terlambat dari jadwal (*Behind Schedule*, $\text{SV} = -\$15.000$, $\text{SPI} = 0,75$).** | Jangan tertipu karena $\text{AC}$ ($\$55.000$) lebih kecil dari $\text{PV}$ ($\$60.000$)! Selalu bandingkan **EV (Earned Value)** terhadap AC (untuk biaya) dan terhadap PV (untuk jadwal). |
| **15** | Perusahaan menggunakan metodologi **Prototyping** untuk membangun sistem baru. Apa risiko **TERBESAR** yang harus diwaspadai oleh IS Auditor? | **Kurangnya kontrol perubahan (*poor change control*) dan tekanan untuk langsung mengoperasikan prototipe yang belum memiliki kontrol keamanan/dokumentasi sebagai sistem produksi.** | Dalam *Prototyping*, perubahan layar terjadi sangat cepat tanpa dokumentasi formal dan *prototype* sering kali tidak dirancang dengan kontrol keamanan/skalabilitas produksi. |
| **16** | Kontrol input aplikasi manakah yang **PALING EFEKTIF** untuk mendeteksi kesalahan pengetikan tunggal (*transcription*) dan tertukarnya posisi dua angka (*transposition*) pada nomor rekening nasabah? | **Check Digit (Digit Pemeriksa — misal Modulus 10 / 11).** | *Hash Total* mendeteksi kesalahan pada tingkat *batch* setelah dikumpulkan, sedangkan *Check Digit* mendeteksi kesalahan pengetikan nomor identifikasi **secara instan saat diketik**! |
| **17** | Tim pengembang meminta salinan *database* produksi berisi data nyata nasabah untuk melakukan *System Testing* di server pengembangan. Apa yang harus diwajibkan oleh auditor? | **Data produksi wajib disanitasi/disamarkan (*Data Masking / Anonymization*) terlebih dahulu sebelum disalin ke lingkungan pengujian.** | Lingkungan *Test/Dev* memiliki kontrol akses yang lebih longgar sehingga menyimpan data PII produksi mentah di sana melanggar prinsip privasi dan keamanan data. |
| **18** | Pengujian apakah yang dilakukan untuk memastikan bahwa perbaikan *bug* atau perubahan program baru **tidak merusak fungsi-fungsi lama yang sebelumnya sudah berjalan baik**? | **Regression Testing (Uji Regresi).** | *Sociability Testing* menguji kemampuan sistem baru hidup berdampingan dengan sistem lain; *Parallel Testing* membandingkan output sistem lama vs. sistem baru. |

---

### D. Skenario Domain 4 — Operasional SI & Ketahanan Bisnis (Skenario 19–24)

| No | Skenario Pertanyaan Ujian CISA | Pilihan Jawaban Terbaik (ISACA) | Mengapa Pilihan Lain Salah (Bedah Jebakan)? |
| :-: | :--- | :--- | :--- |
| **19** | Sebuah insiden kritis terjadi di produksi pada hari Minggu malam dan programmer harus menggunakan akses darurat (*Emergency Change*) untuk memperbaiki sistem sebelum Senin pagi. Apa yang paling penting diperiksa auditor? | **Memastikan perubahan darurat tersebut dicatat dalam log dan telah ditinjau/diuji serta disetujui secara retroaktif (*after-the-fact review*) oleh manajemen/CAB segera setelah insiden teratasi.** | Dalam kondisi darurat nyata, tidak mungkin menunggu rapat CAB reguler minggu depan, sehingga kontrol kuncinya adalah **pencatatan log penuh dan verifikasi pasca-implementasi**. |
| **20** | Apa perbedaan utama antara **Incident Management** dan **Problem Management**? | **Incident Management berfokus memulihkan layanan secepat mungkin (*workaround*), sedangkan Problem Management berfokus mencari dan menghilangkan akar penyebab (*Root Cause*).** | Keduanya saling melengkapi: insiden besar atau berulang dari *Incident Management* dieskalasi ke *Problem Management*. |
| **21** | Hasil *Business Impact Analysis (BIA)* menetapkan bahwa perusahaan tidak boleh kehilangan transaksi lebih dari **15 menit** saat bencana terjadi, dan sistem harus kembali menyala dalam **1 jam**. Metrik manakah yang bernilai 15 menit? | **RPO (Recovery Point Objective) = 15 menit** (menuntut replikasi data mendekati *real-time*), sedangkan **RTO (Recovery Time Objective) = 1 jam** (menuntut *Hot/Mirrored Site*). | Jangan tertukar: **RPO = Data Loss (mundur ke masa lalu)**; **RTO = System Downtime (maju ke masa depan setelah bencana)**. |
| **22** | Perusahaan melakukan *Full Backup* setiap Minggu malam dan **Differential Backup** setiap malam (Senin s.d. Sabtu). Jika server hancur pada hari **Jumat siang**, berapa set pita *backup* yang dibutuhkan untuk memulihkan data? | **Hanya 2 set: Full Backup hari Minggu + Differential Backup hari Kamis malam.** | Jika perusahaan menggunakan *Incremental Backup*, barulah dibutuhkan **5 set** (Minggu + Senin + Selasa + Rabu + Kamis). |
| **23** | Dua perusahaan menandatangani **Reciprocal Agreement** untuk saling meminjamkan pusat data jika salah satu terkena bencana. Apa kelemahan terbesar dari strategi ini? | **Kapasitas perangkat keras mitra mungkin tidak mencukupi untuk menampung beban dua perusahaan sekaligus dan perjanjian tersebut sulit dipaksakan saat krisis.** | Selain itu, ketidakcocokan versi OS/perangkat lunak akibat perubahan sistem di masing-masing perusahaan sering membuat *Reciprocal Agreement* gagal saat diuji. |
| **24** | Departemen Akuntansi menggunakan file **Spreadsheet Excel (EUC)** yang sangat kompleks untuk menghitung cadangan kerugian piutang laporan keuangan. Apa risiko terbesarnya? | **Kurangnya kontrol perubahan versi, tidak adanya penguncian sel rumus (*formula integrity*), dan ketiadaan peninjauan independen atas logika rumus.** | Spreadsheet EUC sering kali diperlakukan sebagai file biasa tanpa *access control*, *change control*, dan *backup* layaknya aplikasi produksi. |

---

### E. Skenario Domain 5 — Perlindungan Aset Informasi (Skenario 25–30)

| No | Skenario Pertanyaan Ujian CISA | Pilihan Jawaban Terbaik (ISACA) | Mengapa Pilihan Lain Salah (Bedah Jebakan)? |
| :-: | :--- | :--- | :--- |
| **25** | Fasilitas ruang server riset militer membutuhkan kontrol akses biometrik. Metrik biometrik manakah yang harus ditekan **SERENDAH MUNGKIN** untuk mencegah penyusup masuk? | **FAR (False Acceptance Rate / Type II Error).** *(Dan jika memilih perangkat terbaik secara keseluruhan, pilih yang memiliki **CER / EER [Crossover Error Rate] paling rendah**).* | *FRR (False Rejection Rate / Type I Error)* hanya menolak staf sah sehingga mereka harus memindai jari sekali lagi, sedangkan **FAR meloloskan penyusup yang tidak berhak**! |
| **26** | Di manakah server **Database Produksi** yang menyimpan data kartu kredit pelanggan harus ditempatkan dalam arsitektur jaringan yang memiliki **DMZ**? | **Di dalam Jaringan Internal (*Internal Protected Network*) di belakang Internal Firewall (TIDAK BOLEH di dalam DMZ!).** | Zona DMZ hanya boleh berisi *Web Server*, *Proxy*, atau *Email Relay* yang berhadapan dengan Internet; menempatkan Database di DMZ membuatnya terekspos langsung jika *Web Server* tertembus. |
| **27** | Pengirim (Alice) ingin mengirim dokumen kontrak elektronik kepada Penerima (Bob) dengan jaminan **Non-Repudiation** dan **Integritas** (Tanda Tangan Digital). Kunci apa yang digunakan Alice untuk menandatangani *hash* dokumen? | **Alice mengenkripsi *hash* dokumen menggunakan `PRIVATE KEY` milik ALICE sendiri, dan Bob memverifikasinya menggunakan `PUBLIC KEY` milik ALICE.** | Jika menggunakan *Public Key* milik Bob, itu adalah untuk **Kerahasiaan (*Confidentiality*)**, bukan *Digital Signature*! |
| **28** | Serangan aplikasi web manakah yang berhasil dicegah secara paling efektif dengan menerapkan **Parameterized Queries / Prepared Statements** di sisi server? | **SQL Injection (SQLi).** | *Input validation* di sisi *client/browser* (JavaScript) sangat mudah dilewati (*bypassed*) oleh penyerang menggunakan *proxy* seperti Burp Suite! |
| **29** | Saat merespons komputer yang diduga disusupi peretas aktif, bukti manakah yang harus dikumpulkan **PERTAMA KALI** berdasarkan *Order of Volatility*? | **Isi Memori RAM, Tabel Proses Aktif, dan Koneksi Jaringan Aktif (*sebelum mencabut kabel listrik komputer!*).** | Jika komputer langsung dimatikan listriknya, seluruh bukti di RAM dan kunci enkripsi di memori akan hilang selamanya. |
| **30** | Mengapa penyidik forensik digital wajib membuat **Bit-Stream Image** menggunakan *Write-Blocker* daripada sekadar menyalin file (*file backup*) biasa? | **Karena Bit-Stream Image menyalin seluruh sektor disk secara utuh termasuk file yang telah dihapus (*deleted files*) dan ruang kosong (*slack/unallocated space*) tanpa mengubah *timestamp* bukti asli.** | Menyalin file biasa (*logical copy*) hanya menyalin file yang masih terlihat di sistem operasi dan mengabaikan file tersembunyi/terhapus di *slack space*. |
