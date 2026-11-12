# Bab 4: Domain 3 (Bagian 1) — Tata Kelola Proyek, Metrik CPM/PERT/EVA, SDLC, dan Akuisisi Sistem (Bobot 12%)

> **Cakupan Materi:** Bab ini membahas separuh pertama **Domain 3 CISA (Information Systems Acquisition, Development and Implementation — 12% / ~18 soal)** yang mencakup *Business Case*, Studi Kelayakan (*Feasibility Study*), Manajemen Proyek (*Project Triangle*, WBS, Gantt, **Critical Path Method [CPM]**, **PERT**, **Earned Value Analysis [EVA]**, **Function Point Analysis [FPA]**, *Timeboxing*), perbandingan lengkap **10 Metodologi SDLC**, proses akuisisi perangkat lunak (**RFP** vs. RFI/RFQ), serta klausul perlindungan **Software Escrow**.

---

## 4.1 Realisasi Manfaat (Benefits Realization) & Business Case

Setiap inisiatif akuisisi atau pengembangan sistem informasi harus diawali dengan **Business Case** yang disusun oleh **Business Sponsor / Process Owner** (bukan departemen TI semata).

1. **Peran Business Case:**
   - Bukan sekadar dokumen persetujuan anggaran satu kali di awal proyek (*one-time budgetary step*), melainkan **dokumen hidup (*living document*)** yang digunakan di sepanjang siklus hidup proyek untuk memvalidasi apakah manfaat bisnis yang dijanjikan masih dapat tercapai.
   - Jika selama proyek berlangsung asumsi bisnis berubah drastis sehingga *Business Case* tidak lagi valid, proyek harus dievaluasi ulang atau **dihentikan (*terminated*)** oleh *Project Steering Committee*.
2. **Feasibility Study (Studi Kelayakan):**
   - Menilai kelayakan solusi dari aspek: **Teknis (*Technical*)**, **Ekonomi/Finansial (*Economic* — ROI, NPV, Payback Period, IRR)**, **Operasional (*Operational* — kesiapan pengguna)**, **Hukum/Regulasi (*Legal*)**, dan **Jadwal (*Schedule*)**.
3. **Portfolio vs. Program vs. Project Management:**
   - **Project:** Upaya sementara (*temporary endeavor*) dengan awal dan akhir yang pasti untuk menghasilkan produk/sistem unik.
   - **Program:** Sekelompok proyek yang saling terkait (*interdependent projects*) yang dikelola secara terkoordinasi untuk memperoleh manfaat dan sinergi yang tidak dapat dicapai jika dikelola sendiri-sendiri.
   - **Portfolio:** Kumpulan seluruh program, proyek, dan operasi yang dikelola untuk mencapai **tujuan strategis korporat (*strategic objectives*)**.

---

## 4.2 Peran Kunci dalam Tata Kelola Proyek TI

| Peran Proyek | Tanggung Jawab Utama & Akuntabilitas CISA |
| :--- | :--- |
| **Project Sponsor** *(Sponsor Bisnis)* | Eksekutif bisnis yang menyediakan pendanaan, **memiliki Business Case**, menyetujui ruang lingkup akhir, dan memikul **akuntabilitas tertinggi (*ultimate accountability*) atas terealisasinya manfaat bisnis (*benefits realization*)** dari sistem baru. |
| **Project Steering Committee** *(Komite Pengarah Proyek)* | Komite lintas-fungsi senior yang memberikan pengawasan keseluruhan (*overall direction*), memantau pencapaian *milestone* utama, menyetujui perubahan ruang lingkup/anggaran yang signifikan, dan memikul akuntabilitas atas **keberhasilan pengiriman proyek (*project delivery*)**. |
| **Project Manager (PM)** | Mengelola operasional harian proyek (jadwal, sumber daya, anggaran harian, komunikasi tim, dan manajemen risiko proyek). |
| **System User / Business Owner** | Menentukan kebutuhan fungsional (*user requirements*), berpartisipasi aktif dalam **User Acceptance Testing (UAT)**, dan menandatangani persetujuan akhir (*final sign-off*) sebelum sistem masuk ke produksi. |
| **IS Auditor (Pre-Implementation Review)** | Berperan sebagai **penasihat/pengamat independen (*independent observer/advisor*)** yang mengevaluasi apakah kontrol aplikasi (ITAC), keamanan, dan jejak audit (*audit trail*) telah dirancang sejak awal fase desain, serta memastikan proses manajemen proyek berjalan efektif **tanpa mengambil keputusan manajemen**. |

---

## 4.3 Teknik Estimasi, Penjadwalan, dan Pengendalian Proyek (CPM, PERT, EVA, FPA)

### A. Work Breakdown Structure (WBS) & Gantt Chart
- **WBS:** Dekomposisi hierarkis seluruh pekerjaan proyek menjadi paket-paket kerja kecil (*work packages*) yang dapat diestimasi waktu, biaya, dan penanggung jawabnya.
- **Gantt Chart:** Grafik batang horizontal yang menunjukkan jadwal mulai dan selesai setiap tugas terhadap kalender, namun **tidak menunjukkan hubungan ketergantungan kritis (*interdependencies*)** antar tugas sebaik diagram jaringan (CPM/PERT).

### B. Critical Path Method (CPM) & Slack/Float Time
- **Critical Path (Jalur Kritis):** Jalur terpanjang (*longest path*) dalam diagram jaringan proyek dari awal hingga akhir yang menentukan **durasi tercepat (*shortest possible time*)** penyelesaian proyek secara keseluruhan.
- Setiap aktivitas yang berada di atas *Critical Path* memiliki **Slack / Float Time = 0 (Nol)**. Artinya, keterlambatan 1 hari saja pada aktivitas di jalur kritis akan langsung menunda penyelesaian seluruh proyek selama 1 hari!
- **Project Crashing:** Mempercepat durasi proyek dengan menambahkan sumber daya ke aktivitas di *Critical Path* dengan biaya tambahan paling minimum.
- **Fast Tracking:** Menjalankan aktivitas di *Critical Path* secara paralel (tumpang tindih) yang seharusnya berurutan — meningkatkan risiko pengerjaan ulang (*rework*).

### C. Program Evaluation and Review Technique (PERT)
Digunakan ketika durasi aktivitas memiliki ketidakpastian tinggi dengan menggunakan **3 angka estimasi waktu**:
- $O$ = *Optimistic Time* (Waktu paling optimis jika semua berjalan sempurna)
- $M$ = *Most Likely Time* (Waktu paling mungkin/realistis)
- $P$ = *Pessimistic Time* (Waktu paling pesimis jika terjadi hambatan)

$$\text{Expected Duration } (T_e) = \frac{O + 4M + P}{6}$$
$$\text{Standard Deviation } (\sigma) = \frac{P - O}{6}, \quad \text{Variance } (\sigma^2) = \left(\frac{P - O}{6}\right)^2$$

### D. Earned Value Analysis (EVA) — Pengendalian Biaya & Jadwal Terpadu
EVA mengukur kinerja proyek secara objektif dengan membandingkan rencana anggaran terhadap progres fisik pekerjaan yang telah diselesaikan:

| Metrik / Indeks EVA | Rumus Matematika | Interpretasi Audit (Baik vs. Buruk) |
| :--- | :--- | :--- |
| **BAC** *(Budget at Completion)* | Total anggaran dasar (*baseline*) untuk seluruh proyek. | Anggaran plafon proyek secara keseluruhan. |
| **PV** *(Planned Value)* | $\text{\% Rencana Jadwal} \times \text{BAC}$ | Nilai pekerjaan yang *seharusnya* sudah selesai hingga hari ini menurut jadwal. |
| **EV** *(Earned Value)* | $\text{\% Progres Fisik Aktual} \times \text{BAC}$ | Nilai anggaran dari pekerjaan yang **benar-benar telah selesai** hingga hari ini. |
| **AC** *(Actual Cost)* | Total biaya aktual yang telah dikeluarkan hingga hari ini. | Pengeluaran kas/biaya riil hingga titik pengukuran. |
| **CV** *(Cost Variance)* | $\text{CV} = \text{EV} - \text{AC}$ | • **$\text{CV} > 0$ (Positif):** *Under budget* (Hemat biaya)<br>• **$\text{CV} < 0$ (Negatif):** **Cost Overrun (Boros / Melebihi anggaran!)** |
| **SV** *(Schedule Variance)* | $\text{SV} = \text{EV} - \text{PV}$ | • **$\text{SV} > 0$ (Positif):** *Ahead of schedule* (Lebih cepat dari jadwal)<br>• **$\text{SV} < 0$ (Negatif):** **Behind Schedule (Terlambat!)** |
| **CPI** *(Cost Performance Index)* | $\text{CPI} = \frac{\text{EV}}{\text{AC}}$ | • **$\text{CPI} > 1.0$:** Efisien biaya<br>• **$\text{CPI} < 1.0$:** **Inefisien biaya / Overbudget** |
| **SPI** *(Schedule Performance Index)* | $\text{SPI} = \frac{\text{EV}}{\text{PV}}$ | • **$\text{SPI} > 1.0$:** Lebih cepat dari jadwal<br>• **$\text{SPI} < 1.0$:** **Terlambat dari jadwal** |
| **EAC** *(Estimate at Completion)* | $\text{EAC} = \frac{\text{BAC}}{\text{CPI}}$ *(jika tren efisiensi berlanjut)* | Estimasi total biaya akhir proyek pada saat proyek selesai 100%. |
| **ETC** *(Estimate to Complete)* | $\text{ETC} = \text{EAC} - \text{AC}$ | Estimasi sisa dana tambahan yang dibutuhkan mulai hari ini hingga proyek selesai. |

### E. Function Point Analysis (FPA) vs. Source Lines of Code (SLOC)
- **FPA (Function Point Analysis):** Teknik estimasi ukuran dan kompleksitas perangkat lunak secara **independen dari bahasa pemrograman** berdasarkan fungsionalitas yang diberikan kepada pengguna, yang dihitung dari **5 komponen transaksi/data**:
  1. *External Inputs (EI)* — layar input pengguna
  2. *External Outputs (EO)* — laporan dengan kalkulasi
  3. *External Inquiries (EQ)* — pencarian data *read-only*
  4. *Internal Logical Files (ILF)* — tabel data di dalam aplikasi
  5. *External Interface Files (EIF)* — referensi data dari aplikasi lain
- **Timeboxing:** Teknik manajemen proyek (umum pada Agile/RAD/Prototyping) yang menetapkan **batas waktu kalender yang kaku (*fixed deadline*)** untuk menyerahkan sistem/iterasi; jika waktu hampir habis, **cakupan fitur minor dikurangi**, bukan mengulur jadwal!

---

## 4.4 Fase Tradisional SDLC & Peran IS Auditor di Setiap Fase

```
[1. Feasibility Study] ──► [2. Requirements Definition] ──► [3. Design / Selection]
                                                                       │
[6. Post-Implementation] ◄── [5. Final Testing & Implementation] ◄── [4. Development / Config]
```

| Fase SDLC | Aktivitas Utama Proyek | Fokus Utama IS Auditor (*Control Checkpoints*) |
| :--- | :--- | :--- |
| **1. Feasibility Study** | Menyusun *Business Case*, menganalisis kelayakan teknis/ekonomi (ROI/NPV), menentukan alternatif *Buy vs. Build*. | Meninjau kewajaran asumsi *Business Case* dan memastikan keselarasan dengan strategi bisnis. |
| **2. Requirements Definition** *(Fase Paling Kritis untuk User)* | Mengidentifikasi kebutuhan bisnis fungsional, non-fungsional, dan **kebutuhan keamanan/kontrol** (*Baseline Freeze*). | Memastikan **spesifikasi kontrol aplikasi (ITAC), keamanan, dan kebutuhan jejak audit (*audit trail*) telah didefinisikan** serta disetujui (*sign-off*) oleh pengguna bisnis. |
| **3. System Design / Selection** | Merancang arsitektur database, antarmuka, alur program (jika *Build*), atau menyusun RFP & mengevaluasi vendor (jika *Buy*). | Mengevaluasi efektivitas desain kontrol (TDE), arsitektur pemisahan tugas (SoD), dan kecukupan rencana pengujian. |
| **4. Development / Configuration** | Menulis kode program, melakukan *code review*, dan melaksanakan **Unit Testing** & **Integration Testing**. | Memastikan pemisahan lingkungan pengembangan dari produksi dan kepatuhan terhadap standar *secure coding*. |
| **5. Final Testing & Implementation** | Melaksanakan **System Testing**, **User Acceptance Testing (UAT)**, konversi/migrasi data, pelatihan, dan *Go-Live*. | Memverifikasi **laporan hasil UAT dan tanda tangan *sign-off* pemilik bisnis**, serta memvalidasi rekonsiliasi kelengkapan/akurasi migrasi data (*completeness & accuracy*). |
| **6. Post-Implementation Review (PIR)** | Mengevaluasi sistem setelah beroperasi selama periode tertentu (biasanya 3–6 bulan setelah *Go-Live*) bersama pengguna dan sponsor. | Menilai **apakah sistem telah mencapai tujuan bisnis dan ROI yang dijanjikan dalam Business Case**, mengevaluasi kepuasan pengguna, dan mengidentifikasi kelemahan kontrol pasca-implementasi. |

---

## 4.5 Perbandingan Lengkap 10 Model Pengembangan Sistem (SDLC Models)

| Model SDLC | Karakteristik & Cara Kerja | Keunggulan Utama | Risiko Utama yang Harus Diawasi Auditor |
| :--- | :--- | :--- | :--- |
| **1. Traditional Waterfall** | Fase berurutan secara linier; satu fase harus 100% selesai (*signed-off*) sebelum fase berikutnya dimulai. | Disiplin dokumentasi tinggi; kontrol setiap *milestone* jelas untuk proyek berskala besar dengan kebutuhan yang stabil. | Pengguna baru melihat sistem di akhir proyek; perubahan kebutuhan di tengah jalan sangat mahal dan sulit diakomodasi. |
| **2. V-Model (Verification & Validation)** | Ekstensi *Waterfall* di mana setiap fase pengembangan di sisi kiri langsung dipasangkan dengan fase pengujian yang sesuai di sisi kanan (misal: *Requirements* $\leftrightarrow$ *UAT*; *High-Level Design* $\leftrightarrow$ *System Test*; *Detailed Design* $\leftrightarrow$ *Integration Test*; *Coding* $\leftrightarrow$ *Unit Test*). | Perencanaan pengujian dilakukan sejak hari pertama; menekan cacat desain sejak dini. | Sama kakunya dengan *Waterfall* terhadap perubahan kebutuhan yang dinamis. |
| **3. Prototyping** | Membuat model kerja cepat (*prototype* / layar simulasi) secara berulang untuk mendapatkan umpan balik cepat dari pengguna. | Sangat baik untuk memperjelas kebutuhan antarmuka pengguna (*UI/UX*) yang belum jelas. | **Risiko Terbesar:** Tekanan manajemen untuk langsung menjadikan *prototype* yang belum selesai sebagai **sistem produksi** tanpa dilengkapi kontrol keamanan, dokumentasi,backup, dan *audit trail* (*Poor Change Control & Scope Creep*). |
| **4. Rapid Application Development (RAD)** | Menggabungkan *prototyping*, alat pengembangan terotomatisasi (CASE tools / 4GL), penggunaan kembali komponen, dan **Timeboxing** dalam tim kecil (*JAD workshops*). | Waktu pengembangan sangat singkat untuk sistem yang terdefinisi baik. | Mengurangi waktu pengujian menyeluruh dan berisiko mengorbankan skalabilitas atau kontrol keamanan jika waktu terdesak. |
| **5. Agile / Scrum Development** | Pengembangan iteratif dan inkremental dalam siklus pendek (**Sprint 1–4 minggu**); mengutamakan *working software* dan kolaborasi pelanggan di atas dokumentasi kaku. | Sangat adaptif terhadap perubahan kebutuhan bisnis dan memberikan nilai bisnis secara cepat. | Dokumentasi teknis dan desain kontrol sering minim; pengujian regresi manual tidak cukup (wajib menggunakan *automated regression testing*). |
| **6. DevOps / DevSecOps** | Mengintegrasikan tim *Development* dan *Operations* melalui otomatisasi *pipeline* CI/CD (*Continuous Integration / Continuous Deployment*). | Rilis fitur sangat cepat dan terotomatisasi. | **Risiko Pelanggaran Segregation of Duties (SoD):** Developer berpotensi mendorong kode langsung ke produksi jika *automated gatekeepers*, *peer code review*, dan kontrol *pipeline* tidak dikunci secara kriptografis! |
| **7. Object-Oriented (OO) System Development** | Mengelompokkan data (*attributes*) dan prosedur (*methods*) ke dalam satu unit mandiri yang disebut **Object** (konsep *Encapsulation*, *Inheritance*, *Polymorphism*). | Reusabilitas tinggi, modular, dan mendukung aplikasi terdistribusi modern. | Kompleksitas pewarisan kelas (*inheritance*) membuat pengujian integrasi dan pelacakan dampak perubahan menjadi lebih rumit. |
| **8. Component-Based Development (CBD)** | Merakit aplikasi dari paket-paket modul/komponen perangkat lunak yang sudah teruji sebelumnya (*pre-built software components / microservices*). | Mengurangi waktu pengembangan, menekan biaya, dan meningkatkan kualitas karena komponen sudah teruji. | Ketergantungan pada komponen pihak ketiga (risiko kerentanan *supply chain* / pustaka *open-source*). |
| **9. Reengineering (Business Process Reengineering / BPR)** | Merombak dan mendesain ulang proses bisnis serta sistem lama secara radikal untuk mencapai peningkatan kinerja yang dramatis. | Menghilangkan proses birokratis yang tidak bernilai tambah. | **Risiko Utama:** Dalam upaya menyederhanakan proses dan memangkas tahapan, **kontrol internal kunci (*key internal controls*) dan SoD sering ikut terhapus secara tidak sengaja!** |
| **10. Reverse Engineering** | Menganalisis sistem/kode yang sudah ada (sering kali *legacy system* tanpa dokumentasi atau melalui *decompiler*) untuk mengekstrak spesifikasi desain dan logika bisnisnya. | Membantu memahami sistem warisan (*legacy*) sebelum dimigrasikan ke sistem baru. | Risiko pelanggaran hak kekayaan intelektual / lisensi perangkat lunak jika dilakukan pada produk vendor tanpa izin. |

---

## 4.6 Akuisisi Perangkat Lunak (Buy vs. Build), RFP, dan Software Escrow

Ketika organisasi memilih membeli paket perangkat lunak (*Commercial Off-The-Shelf* / COTS) daripada membangun sendiri:

1. **Request for Proposal (RFP) vs. RFI:**
   - **RFI (Request for Information):** Digunakan di awal untuk menjajaki solusi apa saja yang tersedia di pasar.
   - **RFP (Request for Proposal):** Dokumen formal yang mengundang vendor mengajukan proposal teknis dan harga berdasarkan kebutuhan yang telah ditetapkan.
   - **Tugas IS Auditor pada Fase RFP:** Memastikan bahwa kebutuhan fungsional, **kebutuhan kontrol keamanan (IAM, enkripsi, *audit trail*), dan kriteria evaluasi yang objektif** telah dimasukkan ke dalam dokumen RFP sebelum dikirim ke vendor.
2. **Aturan Emas Pembelian Paket Software (COTS):**
   - Sebisa mungkin **hindari memodifikasi/mengubah *source code* asli paket COTS (*avoid heavy customization*)**, karena kustomisasi berat akan menghanguskan garansi vendor dan membuat sistem tidak dapat menerima *patch*/pembaruan versi berikutnya. Lebih baik sesuaikan parameter konfigurasi atau sesuaikan proses bisnis non-inti.
3. **Software Escrow Agreement (Perjanjian Penitipan Kode Sumber):**
   - Jika organisasi membeli perangkat lunak yang **sangat kritis (*mission-critical*) dari vendor kecil/khusus** dan vendor menolak menyerahkan *source code*, mitigasi terbaik adalah mewajibkan **Software Escrow Agreement**.
   - Dalam *Software Escrow*, vendor menyimpan salinan **Source Code terbaru beserta dokumentasinya** pada **agen pihak ketiga yang tepercaya (*Trusted Third-Party Escrow Agent*)**. Apabila vendor bangkrut, menutup usaha, atau gagal memenuhi kewajiban pemeliharaan kontrak, *Escrow Agent* secara hukum menyerahkan *source code* tersebut kepada klien agar operasional bisnis klien tetap berjalan. Auditor juga wajib memastikan kode yang dititipkan di *Escrow* **diperbarui setiap kali ada rilis versi baru** dan telah diverifikasi dapat dikompilasi (*verified escrow*).
