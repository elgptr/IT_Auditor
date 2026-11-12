# Bab 3: Domain 2 — Tata Kelola dan Manajemen TI (Governance & Management of IT — Bobot 17%)

> **Cakupan Materi:** Bab ini membahas **Domain 2 CISA (Governance and Management of IT — 17% / ~25 soal)** yang mencakup *Enterprise Governance of IT* (EGIT), perbandingan **IT Strategy Committee vs. IT Steering Committee**, hierarki kebijakan keamanan, matriks lengkap **Segregation of Duties (SoD) 12 Peran TI** dan kontrol kompensasinya, *Enterprise Architecture* (EA), *Enterprise Risk Management* (ERM) & perhitungan risiko kuantitatif (`ALE = SLE × ARO`), kontrol SDM (HR), **IT Balanced Scorecard (IT BSC)**, tata kelola *Outsourcing / Cloud* beserta perbandingan laporan **SOC 1, SOC 2, dan SOC 3 (Type 1 vs. Type 2)**, serta *Quality Assurance* (QA).

---

## 3.1 Enterprise Governance of IT (EGIT) & Tiga Pilar Utama

Tata Kelola TI (**IT Governance**) adalah bagian integral dari tata kelola korporat (*Corporate Governance*) yang menjadi tanggung jawab **Dewan Komisaris / Board of Directors (BoD)** dan manajemen eksekutif. Berdasarkan *ISACA CISA Review Manual* dan studi *Strategic Alignment & IT Governance* (`d2x1_itgov1.txt`, `bsc_itgov.txt`), EGIT bertujuan memastikan bahwa TI mendukung dan memperluas strategi serta tujuan organisasi melalui:

1. **Strategic Alignment (Keselarasan Strategis):** Memastikan rencana strategis TI (*IT Strategic Plan*) selaras penuh dengan strategi bisnis organisasi (*Business Strategy*). Indikator terpenting keselarasan strategis adalah ketika proyek dan investasi TI secara langsung mendukung pencapaian sasaran bisnis.
2. **Value Delivery (Penyampaian Nilai):** Memastikan investasi TI memberikan manfaat bisnis yang dijanjikan tepat waktu, sesuai anggaran (*on budget*), dan dengan kualitas yang disepakati.
3. **Risk Management & Resource Optimization (Manajemen Risiko & Optimasi Sumber Daya):** Mengidentifikasi dan mengelola risiko terkait TI sesuai *Risk Appetite* organisasi, serta mengoptimalkan penggunaan sumber daya TI (infrastruktur, aplikasi, informasi, dan manusia).

### Perbandingan IT Strategy Committee vs. IT Steering Committee

| Dimensi Perbandingan | IT Strategy Committee (Komite Strategi TI) | IT Steering Committee (Komite Pengarah TI) |
| :--- | :--- | :--- |
| **Tingkatan Organisasi** | **Tingkat Dewan (*Board-Level Committee*)** — Sub-komite dari *Board of Directors* / Dewan Komisaris. | **Tingkat Manajemen Eksekutif & Senior (*Executive / Management Level*)**. |
| **Keanggotaan Utama** | Anggota Dewan Komisaris / Direksi (*Board members*) dan penasihat spesialis non-eksekutif. | Eksekutif bisnis senior (CFO, COO), **Kepala Unit Bisnis (Business Unit Heads)**, CIO, serta perwakilan hukum/audit (sebagai pengamat). |
| **Fokus & Tanggung Jawab** | Memberikan arahan strategis tingkat tinggi, menyelaraskan tata kelola TI dengan arah korporat jangka panjang, meninjau eksposur risiko TI tingkat korporat, dan memberi nasihat kepada Dewan mengenai nilai investasi TI besar. | Memantau pelaksanaan rencana strategis TI, **menyetujui prioritas proyek TI, mengalokasikan anggaran & sumber daya proyek**, memantau biaya/jadwal proyek besar, dan menyelesaikan konflik prioritas antar unit bisnis. |
| **Siapa yang Mengetuai?** | Anggota Dewan Komisaris / *Board Member*. | Eksekutif Bisnis Senior (sebaiknya **BUKAN CIO** semata, agar keputusan proyek didorong oleh kebutuhan bisnis, bukan sekadar teknologi). |

---

## 3.2 Hierarki Dokumentasi Tata Kelola: Policies, Standards, Procedures, & Guidelines

Auditor SI wajib memahami urutan hierarki dokumen tata kelola dari tingkat strategis (mandatori) hingga panduan taktis:

| Dokumen | Sifat Kepatuhan | Definisi, Karakteristik, dan Siklus Tinjauan | Contoh Nyata di Lingkungan TI |
| :--- | :---: | :--- | :--- |
| **1. Policies** *(Kebijakan)* | **Mandatory** *(Wajib)* | Pernyataan tingkat tinggi (*high-level statement*) dari manajemen puncak yang mencerminkan filosofi, arah, dan niat manajemen (*management intent*). Harus jelas, ringkas, netral terhadap teknologi spesifik, dan **ditinjau minimal setahun sekali**. | *"Seluruh data rahasia nasabah harus dilindungi dari akses yang tidak sah baik saat disimpan maupun ditransmisikan."* |
| **2. Standards** *(Standar)* | **Mandatory** *(Wajib)* | Aturan, parameter, atau metrik spesifik yang wajib dipatuhi untuk mengimplementasikan *Policy*. Menentukan batas keras (*hard boundaries*) teknologi atau konfigurasi. | *"Seluruh data rahasia harus dienkripsi menggunakan AES-256 saat disimpan dan TLS 1.3 saat ditransmisikan; panjang password minimal 12 karakter."* |
| **3. Procedures** *(Prosedur / SOP)* | **Mandatory** *(Wajib)* | Langkah-langkah operasional terperinci (*step-by-step instructions*) mengenai bagaimana mencapai kepatuhan terhadap *Policies* dan *Standards*. Sering berubah mengikuti perubahan sistem/alat. | Langkah teknis bagi administrator untuk mengaktifkan BitLocker/TDE pada database Oracle dan merotasi kunci enkripsi setiap 180 hari. |
| **4. Guidelines** *(Pedoman)* | **Discretionary / Recommended** *(Saran)* | Rekomendasi, praktik terbaik (*best practices*), dan panduan fleksibel bagi pengguna/staf ketika tidak ada standar spesifik yang mengatur, atau untuk membantu menerapkan prosedur. | Panduan menyusun *passphrase* yang mudah diingat namun sulit ditebak oleh pengguna akhir. |

---

## 3.3 Struktur Organisasi TI & Matriks Segregation of Duties (SoD) 12 Peran TI

**Segregation of Duties (SoD / Pemisahan Tugas)** adalah kontrol preventif fundamental untuk memastikan bahwa **tidak ada satu individu pun** yang memiliki kendali penuh atas suatu transaksi atau proses sistem dari awal hingga akhir (mengurangi risiko *fraud* dan modifikasi tanpa otorisasi).

### A. Tugas Pokok 12 Peran Organisasi TI Standar CISA

1. **Systems Analyst (Analis Sistem):** Menerjemahkan kebutuhan pengguna bisnis menjadi spesifikasi fungsional dan desain sistem.
2. **Application Programmer (Pemrogram Aplikasi):** Menulis, menguji, dan memelihara *source code* di lingkungan pengembangan (*Development/Test*). **Dilarang keras memiliki akses ke lingkungan Produksi!**
3. **Computer Operator (Operator Komputer / Data Center):** Menjalankan *batch jobs* produksi, memantau konsol operasional, dan memuat media *backup*. **Dilarang memodifikasi kode program atau mengubah data produksi!**
4. **Data Entry / Control Group:** Menginput data atau memverifikasi kelengkapan *batch input/output* antara pengguna bisnis dan operasional TI.
5. **Database Administrator (DBA):** Merancang skema fisik database, mengelola kinerja, dan mengatur kontrol akses struktur DBMS. Karena DBA memiliki hak istimewa tinggi (*superuser*), aktivitasnya wajib dipantau melalui *audit trail* independen.
6. **System Administrator / Systems Programmer:** Memelihara sistem operasi (OS) dan perangkat lunak sistem jaringan. Memiliki akses level *root/admin* sehingga wajib diawasi ketat.
7. **Security Administrator (Administrator Keamanan):** Mengelola *user ID*, hak akses (*provisioning/deprovisioning*), dan memantau log pelanggaran keamanan berdasarkan otorisasi *Data Owner*.
8. **Quality Assurance (QA) / Change Control / Librarian:** Menguji kualitas sistem sebelum masuk produksi dan mengelola perpustakaan program (*Program Library*). Merupakan satu-satunya fungsi yang berwenang memigrasikan kode (*promote/transport code*) dari *Test* ke *Production*.
9. **Network Administrator:** Mengelola infrastruktur komunikasi, *router*, *switch*, dan ketersediaan jaringan.
10. **Help Desk / Service Desk:** Titik kontak pertama (*Single Point of Contact*) bagi pengguna untuk pelaporan insiden dan bantuan teknis tingkat pertama.
11. **End User / Business Data Owner:** Pemilik proses bisnis yang mengotorisasi transaksi, menentukan klasifikasi data, dan menyetujui pemberian hak akses pengguna.
12. **IS Auditor:** Fungsi independen yang mengevaluasi efektivitas kontrol internal; **tidak boleh** menjalankan fungsi operasional TI mana pun.

### B. Matriks Konflik Segregation of Duties (SoD Conflict Matrix)

Tabel berikut merangkum kombinasi peran yang **TIDAK BOLEH** dirangkap oleh satu orang (tanda `X` = Konflik SoD Kritis):

| Peran Utama \ Peran Rangkap | App Dev / Programmer | Computer Operator | Security Admin | DBA / SysAdmin | Librarian / Change Migration | End User / Business Owner | IS Auditor |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **App Dev / Programmer** | — | **`X` (Kritis)** | **`X` (Kritis)** | **`X` (Kritis)** | **`X` (Kritis)** | **`X` (Kritis)** | **`X`** |
| **Computer Operator** | **`X` (Kritis)** | — | **`X` (Kritis)** | **`X`** | **`X`** | **`X` (Kritis)** | **`X`** |
| **Security Admin** | **`X` (Kritis)** | **`X` (Kritis)** | — | **`X` (Kritis)** | **`X`** | **`X` (Kritis)** | **`X`** |
| **DBA / SysAdmin** | **`X` (Kritis)** | **`X`** | **`X` (Kritis)** | — | **`X`** | **`X` (Kritis)** | **`X`** |
| **Librarian / Migration** | **`X` (Kritis)** | **`X`** | **`X`** | **`X`** | — | **`X`** | **`X`** |
| **End User / Business** | **`X` (Kritis)** | **`X` (Kritis)** | **`X` (Kritis)** | **`X` (Kritis)** | **`X`** | — | **`X`** |

### C. Risiko Spesifik Konflik SoD & Kontrol Kompensasi (Compensating Controls)

| Kombinasi Konflik SoD | Risiko Spesifik yang Timbul | Kontrol Kompensasi (Jika Organisasi Kecil Tidak Mampu Memisahkan Staf) |
| :--- | :--- | :--- |
| **Programmer + Operator Produksi** *(atau Programmer punya akses ke Produksi)* | Programmer dapat menyisipkan kode jahat (*backdoor / Trojan horse / salami slicing*), menjalankannya langsung di produksi, lalu menghapus jejaknya. | • Cabut akses *write* permanen programmer di produksi; gunakan **Emergency / FireCall ID** sementara dengan persetujuan berjenjang.<br>• **Review 100% log aktivitas (*audit trail*) dan *transport log*** secara independen oleh manajer TI/pemilik bisnis. |
| **Programmer + Librarian / Change Control** | Programmer dapat mendorong (*promote*) perubahan kode yang belum diuji atau belum disetujui pengguna langsung ke server produksi. | • Rekonsiliasi berkala antara daftar *Change Request* yang disetujui dengan log perubahan *timestamp/hash* objek program di produksi oleh pihak independen. |
| **DBA / SysAdmin + Security Administrator** | DBA/SysAdmin dapat membuat akun fiktif, memberikan hak akses *superuser* pada dirinya sendiri, memanipulasi data, dan menghapus log keamanan (*security log*). | • Kirim seluruh log sistem dan database (*syslog / DBA_AUDIT_TRAIL*) secara *real-time* ke server **SIEM terpisah (*write-once / immutable*)** yang hanya dapat diakses oleh fungsi Kepatuhan/Audit.<br>• Lakukan *User Access Review* (UAR) dan *Activity Log Review* secara independen. |
| **End User (Bisnis) + Programmer / Security Admin** | Pengguna bisnis dapat membuat akun fiktif untuk menginput sekaligus menyetujui transaksi fiktif (misal: pencairan dana atau *master vendor* palsu). | • Rekonsiliasi transaksi harian secara independen oleh supervisor bisnis dan pemeriksaan silang (*cross-check*) log pembuatan akun terhadap surat keputusan HRD. |

---

## 3.4 Kontrol Sumber Daya Manusia (HR Controls) untuk Mengurangi Risiko Fraud

Selain SoD teknis, manajemen wajib menerapkan kontrol personel/SDM berikut pada posisi sensitif:

1. **Background Checks & Screening (Pra-Kerja):** Pemeriksaan latar belakang kriminal, riwayat pekerjaan, pendidikan, dan kredit sebelum kandidat diterima, khususnya untuk posisi DBA, Security Admin, dan Keuangan.
2. **Non-Disclosure Agreement (NDA) & Acceptable Use Policy (AUP):** Ditandatangani saat *onboarding* dan diperbarui secara berkala.
3. **Mandatory Vacations (Cuti Wajib Berurutan):** Mewajibkan staf di posisi sensitif mengambil cuti minimal **1–2 minggu berturut-turut** di mana pekerjaannya diambil alih sementara oleh orang lain. Sangat efektif sebagai kontrol **detektif** untuk mengungkap skema *fraud* yang membutuhkan manipulasi harian oleh pelaku.
4. **Job Rotation (Rotasi Jabatan):** Memindahkan staf antar fungsi secara berkala untuk mencegah kolusi jangka panjang dan menghilangkan ketergantungan pada satu orang (*single point of failure / key-person dependency*).
5. **Termination Procedures (Prosedur Pemberhentian — Kritikal!):**
   - Untuk **Terminasi Tidak Sukarela (*Involuntary Termination / Pemecatan*)**: Pencabutan seluruh hak akses logis (*Active Directory*, VPN, email, aplikasi, DB) dan kartu akses fisik harus dilakukan **SEGERA / SEBELUM** karyawan diberitahu mengenai pemecatannya, diikuti dengan pengawalan fisik (*escort*) saat mengemasi barang pribadi dan *exit interview*.

---

## 3.5 Manajemen Risiko TI (ERM) & Perhitungan Risiko Kuantitatif

### A. Siklus Manajemen Risiko TI
1. **Identifikasi Aset & Ancaman (*Asset & Threat Identification*)**
2. **Analisis Kerentanan & Dampak (*Vulnerability & Impact Analysis*)** — Kuantitatif atau Kualitatif
3. **4 Opsi Respons Risiko (*Risk Response Options*):**
   - **Risk Mitigation / Reduction (Mitigasi):** Menerapkan kontrol keamanan untuk menurunkan kemungkinan (*likelihood*) atau dampak (*impact*) hingga di bawah *Risk Tolerance*.
   - **Risk Avoidance (Penghindaran):** Menghentikan aktivitas bisnis atau mematikan sistem yang menimbulkan risiko karena tidak ada kontrol yang layak secara biaya.
   - **Risk Transfer / Sharing (Transfer/Berbagi):** Mengalihkan dampak finansial risiko ke pihak ketiga melalui **Asuransi Siber (*Cyber Insurance*)** atau klausul ganti rugi kontrak *outsourcing*. *(Catatan CISA: Anda dapat mentransfer risiko finansial, tetapi **AKUNTABILITAS (Accountability)** hukum/reputasi tidak pernah bisa ditransfer!).*
   - **Risk Acceptance (Penerimaan):** Menerima risiko secara sadar ketika biaya kontrol melebihi potensi kerugian (**Cost of Control > Asset Value / ALE**), dengan persetujuan tertulis dari manajemen senior.

### B. Rumus Analisis Risiko Kuantitatif (EF, SLE, ARO, ALE, & Control ROI)

$$\text{Single Loss Expectancy (SLE)} = \text{Asset Value (AV)} \times \text{Exposure Factor (EF)}$$
$$\text{Annualized Loss Expectancy (ALE)} = \text{SLE} \times \text{Annualized Rate of Occurrence (ARO)}$$
$$\text{Nilai Bersih Kontrol (Net Value / ROI Kontrol)} = (\text{ALE}_{\text{sebelum}} - \text{ALE}_{\text{sesudah}}) - \text{Annual Cost of Control (ACS)}$$

*Contoh Soal & Perhitungan CISA:*
- Sebuah pusat data memiliki nilai aset (**AV**) sebesar **$1,000,000**. Ancaman banjir diperkirakan merusak **40%** nilai aset (**EF = 0.40**), dan banjir terjadi rata-rata **sekali setiap 5 tahun** (**ARO = $1/5 = 0.20$**).
  - $\text{SLE} = \$1,000,000 \times 0.40 = \mathbf{\$400,000}$
  - $\text{ALE}_{\text{sebelum}} = \$400,000 \times 0.20 = \mathbf{\$80,000\text{ per tahun}}$
- Jika manajemen memasang sistem tanggul dan drainase seharga **$15,000/tahun (ACS)** yang menurunkan $\text{EF}$ menjadi $10\%$ ($\text{ALE}_{\text{sesudah}} = \$1,000,000 \times 0.10 \times 0.20 = \$20,000$):
  - $\text{Net Savings Kontrol} = (\$80,000 - \$20,000) - \$15,000 = \mathbf{+\$45,000\text{ per tahun (Layak dipasang!)}}$
  - Sebaliknya, jika biaya kontrol tahunan adalah **$90,000/tahun**, maka biaya kontrol melebihi $\text{ALE}$ awal ($\$80,000$), sehingga kontrol tersebut **tidak layak secara biaya (*not cost-effective*)**!

---

## 3.6 IT Balanced Scorecard (IT BSC) — Van Grembergen & De Haes

Berdasarkan materi Handout *Measuring and Improving IT Governance Through the Balanced Scorecard* (`bsc_itgov.txt`), **IT Balanced Scorecard** mengukur kinerja tata kelola dan departemen TI melalui **4 Perspektif** yang saling berelasi sebab-akibat:

| Perspektif IT BSC | Pertanyaan Misi Utama | Contoh Metrik / Key Performance Indicators (KPI) |
| :--- | :--- | :--- |
| **1. Corporate Contribution** *(Kontribusi Korporat — menggantikan Perspektif Finansial)* | *"Bagaimana manajemen eksekutif dan Dewan memandang kontribusi nilai bisnis dari departemen TI?"* | • *Strategic alignment index* proyek TI<br>• *Return on Investment* (ROI) / NPV portofolio proyek TI<br>• Pengendalian biaya anggaran TI vs. realisasi (*IT budget variance*)<br>• Nilai bisnis dari inovasi produk berbasis TI |
| **2. User Orientation** *(Orientasi Pengguna — menggantikan Perspektif Pelanggan)* | *"Bagaimana pengguna bisnis internal dan pelanggan eksternal memandang kualitas layanan TI?"* | • Indeks kepuasan pengguna (*Customer/User Satisfaction Score*)<br>• Tingkat pemenuhan *Service Level Agreement* (**SLA attainment %**)<br>• *First-call resolution rate* pada Service Desk |
| **3. Operational Excellence** *(Keunggulan Operasional — Proses Internal)* | *"Seberapa efektif dan efisien proses pengembangan aplikasi dan operasional TI dijalankan?"* | • Persentase proyek selesai tepat waktu dan sesuai anggaran<br>• *Mean Time to Resolve* (MTTR) insiden produksi<br>• Jumlah cacat (*defects*) pasca-implementasi per 1.000 baris kode<br>• Ketersediaan sistem (*System Uptime* — misal 99.95%) |
| **4. Future Orientation** *(Orientasi Masa Depan — Pembelajaran & Pertumbuhan)* | *"Seberapa baik TI diposisikan untuk memenuhi tantangan teknologi dan bisnis di masa depan?"* | • Jam pelatihan dan sertifikasi staf TI per tahun<br>• Tingkat perputaran (*turnover*) talenta kunci TI<br>• Usia rata-rata portofolio aplikasi dan infrastruktur (*technical debt*)<br>• Anggaran riset teknologi baru (*emerging tech R&D*) |

---

## 3.7 Tata Kelola Outsourcing, Cloud, dan Laporan Audit Pihak Ketiga (SOC 1, SOC 2, SOC 3)

Ketika organisasi mengalihdayakan (*outsource*) operasional TI atau menggunakan penyedia *Cloud* (IaaS/PaaS/SaaS), **manajemen organisasi klien tetap memikul akuntabilitas penuh (*ultimate accountability*)** atas keamanan data dan kepatuhan regulasi.

### A. Klausul Wajib dalam Kontrak Outsourcing / Cloud
1. **Right to Audit Clause (Klausul Hak Audit):** Memberikan hak hukum kepada auditor internal/eksternal klien (atau regulator) untuk mengaudit fasilitas, kontrol, dan catatan vendor.
2. **Service Level Agreement (SLA) dengan Penalti Finansial:** Metrik kinerja yang terukur (*uptime*, waktu respons, RTO/RPO) beserta mekanisme kompensasi/penalti jika gagal dicapai, serta hak pemutusan kontrak (*termination right*) jika terjadi pelanggaran berulang.
3. **Kepemilikan Data & Prosedur Exit/Decommissioning:** Penegasan bahwa seluruh data milik klien tetap menjadi milik klien, serta kewajiban vendor untuk mengembalikan data dalam format standar dan menghapus (*cryptographic erasure / secure wipe*) sisa data saat kontrak berakhir.
4. **Kewajiban Pelaporan Insiden Keamanan (*Breach Notification*):** Batas waktu maksimal (misal $1 \times 24$ jam) bagi vendor untuk melaporkan insiden kebocoran data kepada klien.

### B. Matriks Perbandingan Laporan SOC 1, SOC 2, dan SOC 3 (SSAE 18 / ISAE 3402)

Untuk mengevaluasi kontrol di *Service Organization* (vendor *Cloud/Data Center/Payroll*), auditor SI mengandalkan laporan **System and Organization Controls (SOC)**:

| Jenis Laporan | Fokus & Ruang Lingkup Kriteria | Distribusi Pembaca | Type 1 (Point-in-Time) vs. Type 2 (Period of Time) |
| :--- | :--- | :--- | :--- |
| **SOC 1** *(SSAE 18 / ISAE 3402)* | **Internal Control over Financial Reporting (ICFR):** Fokus pada kontrol di vendor yang berdampak langsung pada **laporan keuangan** klien (misal: pemrosesan *Payroll*, kliring pembayaran, *loan servicing*). | Terbatas: Manajemen klien, manajemen vendor, dan **Auditor Keuangan Eksternal (SOX)** klien. | • **Type 1:** Menilai kewajaran deskripsi sistem dan **kesesuaian desain kontrol (*Suitability of Design / TDE*)** pada **satu tanggal tertentu (*as of a specific date*)**. Tidak menguji efektivitas operasional!<br>• **Type 2:** Mencakup seluruh isi Type 1 **DITAMBAH pengujian efektivitas operasional (*Operating Effectiveness / TOE*)** selama **suatu periode waktu** (minimal **6 bulan**). |
| **SOC 2** *(AT-C 205)* | **Trust Services Criteria (TSC) — Operasional & Kepatuhan Teknis:** Mengevaluasi kontrol terkait **5 Prinsip TSC**:<br>1. *Security* (Keamanan)<br>2. *Availability* (Ketersediaan)<br>3. *Processing Integrity* (Integritas Pemrosesan)<br>4. *Confidentiality* (Kerahasiaan)<br>5. *Privacy* (Privasi) | Terbatas: Manajemen klien, tim keamanan/audit TI klien, dan mitra bisnis yang memahami sistem (memuat detail teknis kontrol dan hasil pengujian). | • **SOC 2 Type 1:** Hanya menguji **Desain Kontrol (TDE)** pada satu titik waktu.<br>• **SOC 2 Type 2:** Menguji **Desain (TDE) DAN Efektivitas Operasional (TOE)** selama periode waktu (6–12 bulan). **Merupakan laporan yang PALING bernilai bagi IS Auditor dalam menilai kontrol keamanan vendor Cloud!** |
| **SOC 3** | Sama dengan SOC 2 (**5 Trust Services Criteria**), namun **tidak memuat detail pengujian teknis** atau deskripsi rinci kontrol. | **Publik / Umum (*General Use*):** Dapat dipasang di situs web vendor sebagai segel pemasaran (*Trust Seal*). | Hanya berisi opini auditor apakah vendor memenuhi kriteria TSC tanpa rincian matriks kontrol dan pengecualian (*exceptions*). |

> [!CAUTION]
> **Kewajiban Auditor Klien saat Membaca Laporan SOC 2 Type 2:**
> Selain memeriksa apakah opini auditor vendor adalah *Unqualified* (Wajar Tanpa Pengecualian) dan periode laporan mencakup tahun berjalan (atau meminta *Bridge Letter* untuk celah waktu), auditor klien **WAJIB** memeriksa bagian **Complementary User Entity Controls (CUECs)** di dalam laporan SOC! CUECs adalah kontrol yang diasumsikan oleh vendor telah diterapkan oleh **organisasi klien sendiri** (misal: klien wajib mencabut akses staf klien yang resign). Jika klien gagal menerapkan CUECs, kontrol vendor menjadi tidak efektif!
