# Bab 10: COBIT 2019 Implementation Guide — Siklus Hidup 7 Fase Implementasi & Optimisasi Tata Kelola TI

> **Sumber Otoritatif:** *COBIT® 2019 Implementation Guide: Implementing and Optimizing an Information and Technology Governance Solution (ISACA, 2018)*.

---

## 1. Arsitektur Siklus Hidup Implementasi COBIT 2019 (7 Fase & 3 Cincin Konsentris)

Implementasi atau perbaikan sistem tata kelola I&T (*Enterprise Governance of Information and Technology — EGIT*) bukanlah proyek satu kali selesai (*one-off project*), melainkan **siklus hidup perbaikan berkelanjutan yang terdiri atas 7 Fase** dan digerakkan oleh **3 Cincin Konsentris yang Saling Terkait (*Three Interrelated Rings*)**:

```
               +---------------------------------------------------+
               |      FASE 1: What Are the Drivers?                |
               |      (Kenali Pain Points & Trigger Events)        |
               +-------------------------+-------------------------+
                                         |
      +----------------------------------+----------------------------------+
      |                                                                     |
      v                                                                     v
+-------------------------------+                                 +-------------------------------+
| FASE 7: Did We Get There?     |                                 | FASE 2: Where Are We Now?     |
| (Review Efektivitas &         |                                 | (Penilaian Current Capability |
|  Pertahankan Momentum)        |                                 |  & Diagnosis Kesenjangan)     |
+---------------+---------------+                                 +---------------+---------------+
                ^                                                                 |
                |               +---------------------------------+               |
                |               |   3 CINCIN KONSENTRIS (RINGS):  |               |
                |               |  1. Program Management (Outer)  |               |
                |               |  2. Change Enablement (Middle)  |               |
                |               |  3. Continual Improvement (Core)|               |
                |               +---------------------------------+               v
+---------------+---------------+                                 +---------------+---------------+
| FASE 6: Did We Get There? /   |                                 | FASE 3: Where Do We Want      |
| How Do We Keep the Momentum?  |                                 |         to Be?                |
| (Realisasi Manfaat & Metrik)  |                                 | (Target Capability & Desain)  |
+---------------+---------------+                                 +---------------+---------------+
                ^                                                                 |
                |                                                                 v
                |     +-------------------------------+     +-------------------------------+
                +-----+ FASE 5: How Do We Get There?  |<----+ FASE 4: What Needs to Be      |
                      | (Eksekusi Solusi & Operasional|     |         Done?                 |
                      |  Sehari-hari)                 |     | (Perencanaan Rinci & Roadmap) |
                      +-------------------------------+     +-------------------------------+
```

### Tiga Cincin Konsentris (*Three Interrelated Rings*) pada Setiap Fase
Pada setiap fase dari Fase 1 hingga Fase 7, tim implementasi maupun auditor harus memastikan ketiga cincin berikut berjalan secara serempak:

| Cincin (Ring) | Nama Komponen Siklus Hidup | Fokus Utama & Objektif COBIT Terkait | Konsekuensi Jika Cincin Ini Diabaikan |
| :--- | :--- | :--- | :--- |
| **1. Outer Ring (Cincin Luar)** | **Program Management (PM)** — Manajemen Program | Mengelola program perbaikan tata kelola secara terstruktur: *Business Case*, anggaran, *Steering Committee*, jadwal, dan risiko program.<br>*Objektif Inti:* `BAI01`, `BAI11`, `APO05` | Program kehilangan arah, kehabisan anggaran di tengah jalan, atau berhenti karena tidak ada akuntabilitas eksekutif. |
| **2. Middle Ring (Cincin Tengah)** | **Change Enablement (CE)** — Pemberdayaan Perubahan Budaya & Perilaku | Mengatasi resistensi manusia, membangun kesadaran (*awareness*), komunikasi pemangku kepentingan, pelatihan, dan memenangkan komitmen (*buy-in*).<br>*Objektif Inti:* `BAI05`, `APO01`, `APO07`, `APO08` | **Penyebab kegagalan #1 implementasi COBIT:** Kebijakan dan SOP selesai ditulis di atas kertas namun ditolak atau diabaikan oleh staf dan unit bisnis ("*shelfware governance*"). |
| **3. Inner Ring (Cincin Dalam)** | **Continual Improvement Life Cycle (CI)** — Siklus Peningkatan Berkelanjutan | Aktivitas teknis perancangan, asesmen kapabilitas, analisis *gap*, pembuatan kebijakan/kontrol/alat bantu, dan pengukuran metrik.<br>*Objektif Inti:* `EDM01`, `APO01`, `MEA01`, `MEA02` | Perubahan bersifat kosmetik tanpa perbaikan nyata pada kapabilitas proses dan kontrol. |

---

## 2. Katalog Resmi *Pain Points* & *Trigger Events* (Pemetaan Diagnostik Cepat)

 *COBIT 2019 Implementation Guide* menggunakan dua penggerak utama di Fase 1 untuk memulai atau memfokuskan perbaikan tata kelola TI:
1. **Pain Points (Titik Masalah Aktual):** Gejala kegagalan atau masalah kronis yang sedang dirasakan organisasi.
2. **Trigger Events (Peristiwa Pemicu):** Peristiwa perubahan strategis, bisnis, atau regulasi yang menuntut penyesuaian tata kelola TI.

### A. Pemetaan 10 *Pain Points* Utama ke Objektif COBIT 2019

| No. | Gejala *Pain Point* di Organisasi | Akar Masalah Tata Kelola / Manajemen | Objektif COBIT 2019 yang Wajib Diprioritaskan |
| :---: | :--- | :--- | :--- |
| **PP01** | **Frustrasi unit bisnis terhadap proyek TI yang selalu terlambat, *over-budget*, dan gagal memberi nilai bisnis.** | Lemahnya seleksi *Business Case*, manajemen program/proyek, dan definisi kebutuhan bisnis. | `EDM02`, `APO05`, `APO08`, `BAI01`, `BAI02`, `BAI03`, `BAI11` |
| **PP02** | **Insiden keamanan siber signifikan (ransomware, kebocoran data/PII) atau gangguan operasional (*downtime*) berulang.** | Lemahnya manajemen risiko, ISMS, *patching*, manajemen masalah (RCA), dan DRP/BCP. | `EDM03`, `APO12`, `APO13`, `DSS02`, `DSS03`, `DSS04`, `DSS05` |
| **PP03** | **Masalah kronis pada kualitas pengiriman layanan dari vendor / *outsourcer* / penyedia Cloud.** | Kontrak SLA lemah, tidak ada evaluasi vendor berkala, atau *vendor lock-in*. | `APO09`, `APO10`, `DSS01`, `MEA01`, `MEA03` |
| **PP04** | **Kegagalan mematuhi regulasi eksternal (teguran/sanksi OJK, BI, UU PDP, BSSN) atau temuan audit yang terus berulang.** | Ketiadaan pemantauan kepatuhan proaktif, kontrol internal lemah, dan tindak lanjut audit macet. | `EDM01`, `EDM03`, `APO01`, `MEA02`, `MEA03`, `MEA04` |
| **PP05** | **Maraknya pengeluaran TI tersembunyi (*Shadow IT*) di unit bisnis dan duplikasi aplikasi/proyek.** | Arsitektur enterprise tidak ditegakkan, birokrasi TI lambat, dan ketiadaan tata kelola portofolio. | `EDM01`, `EDM02`, `APO03`, `APO05`, `APO06`, `APO08`, `BAI09` |
| **PP06** | **Kekurangan SDM TI yang kompeten, kelelahan staf (*burnout*), *turnover* tinggi, dan ketergantungan pada individu kunci.** | Perencanaan kapasitas SDM buruk, kurangnya pelatihan/transfer pengetahuan, dan prioritas kerja kacau. | `EDM04`, `APO01`, `APO07`, `BAI08` |
| **PP07** | **Dewan Direksi/Komisaris enggan terlibat dalam urusan TI atau model pengambilan keputusan TI tidak jelas/lambat.** | Tidak ada *IT Governance Charter*, matriks RACI kabur, dan laporan ke Board terlalu teknis. | `EDM01`, `EDM02`, `EDM05`, `APO01`, `APO08` |
| **PP08** | **Biaya TI sangat tinggi/membengkak (*Cloud cost shock* / lisensi mahal) tanpa transparansi manfaat terhadap bisnis.** | Tidak ada model biaya TI, *showback/chargeback*, dan optimisasi aset/lisensi. | `EDM02`, `EDM04`, `APO05`, `APO06`, `BAI04`, `BAI09` |
| **PP09** | **Arsitektur TI kaku/usang (*legacy debt*) sehingga menghambat peluncuran produk digital baru dan inovasi.** | Utang teknis menumpuk, tidak ada modernisasi arsitektur, dan proses *change/release* manual. | `APO02`, `APO03`, `APO04`, `BAI02`, `BAI03`, `BAI06` |
| **PP10** | **Data tidak akurat/tidak konsisten antar-laporan manajemen (*multiple versions of truth*) dan risiko privasi data.** | Ketiadaan *Data Governance*, *Data Owner*, kamus metadata, dan kontrol validasi aplikasi. | `APO03`, `APO14`, `DSS06`, `MEA01` |

### B. Pemetaan 10 *Trigger Events* ke Objektif COBIT 2019

| No. | Peristiwa Pemicu (*Trigger Event*) | Fokus Penyesuaian Sistem Tata Kelola TI | Objektif COBIT 2019 Utama |
| :---: | :--- | :--- | :--- |
| **TE01** | **Merger, Akuisisi, atau Divestasi Perusahaan** | Integrasi arsitektur, konsolidasi aplikasi/data, harmonisasi kebijakan & RACI, serta manajemen perubahan budaya. | `EDM01`, `APO01`, `APO02`, `APO03`, `APO05`, `APO14`, `BAI01`, `BAI05` |
| **TE02** | **Pergantian CEO, CIO, atau Restrukturisasi Organisasi** | Peninjauan ulang mandat tata kelola, strategi TI, pelaporan eksekutif, dan struktur RACI. | `EDM01`, `EDM05`, `APO01`, `APO02`, `APO07`, `APO08` |
| **TE03** | **Perubahan Strategi Bisnis / Transformasi Digital** | Perancangan peta jalan digital, inovasi produk, adopsi *Agile/DevOps*, dan realisasi manfaat. | `EDM02`, `APO02`, `APO03`, `APO04`, `APO05`, `BAI01`, `BAI02`, `BAI03`, `BAI05` |
| **TE04** | **Terbitnya Regulasi Baru (mis. UU PDP, POJK 11/2022, SPBE, DORA)** | Pemetaan kewajiban kepatuhan, perlindungan data pribadi, manajemen risiko siber, dan pelaporan wajib. | `EDM01`, `EDM03`, `APO12`, `APO13`, `APO14`, `DSS05`, `MEA02`, `MEA03`, `MEA04` |
| **TE05** | **Migrasi Besar-besaran ke Cloud atau Alih Daya (*Outsourcing*)** | Penyesuaian kontrol vendor, SLA, keamanan cloud, manajemen biaya (*FinOps*), dan *Exit Strategy*. | `EDM03`, `APO06`, `APO09`, `APO10`, `APO12`, `APO13`, `BAI06`, `DSS04`, `DSS05` |
| **TE06** | **Implementasi Sistem Inti Baru (ERP / Core Banking / HIS)** | Pengendalian program/proyek, definisi kebutuhan, migrasi data, UAT, manajemen perubahan organisasi, dan kontrol aplikasi. | `APO05`, `BAI01`, `BAI02`, `BAI03`, `BAI05`, `BAI06`, `BAI07`, `BAI11`, `DSS06` |
| **TE07** | **Tekanan Efisiensi Biaya / Pemotongan Anggaran Korporat** | Rasionalisasi portofolio aplikasi, negosiasi ulang kontrak vendor, optimalisasi lisensi & kapasitas. | `EDM04`, `APO05`, `APO06`, `APO10`, `BAI04`, `BAI09` |
| **TE08** | **Persiapan IPO (*Initial Public Offering*) atau Audit Eksternal/Sertifikasi Baru (ISO 27001 / SOC 2)** | Formalisasi pengendalian internal (ITGC & ITAC), SoD, akurasi pelaporan keuangan TI, dan jejak audit. | `EDM01`, `EDM05`, `APO01`, `APO13`, `BAI06`, `DSS05`, `DSS06`, `MEA02`, `MEA03`, `MEA04` |

---

## 3. Bedah Lengkap 7 Fase Implementasi COBIT 2019 (Tugas PM/CE/CI, Input/Output, RACI & CSFs)

---

### FASE 1: What Are the Drivers? (Apa Penggeraknya?)
- **Tujuan Fase 1:** Memahami konteks bisnis dan strategis organisasi, mengenali *pain points* dan *trigger events* saat ini, membangun kesadaran (*desire to change*) di tingkat eksekutif, serta menyusun kerangka awal **Business Case**.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 1 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 1.1` | Mengenali kebutuhan untuk bertindak (*recognize the need to act*) berdasarkan sinyal risiko/kinerja. |
| | `PM 1.2` | Mengidentifikasi penggerak perubahan (*drivers*), *pain points*, dan *trigger events* bersama pemangku kepentingan. |
| | `PM 1.3` | Mengumpulkan informasi konteks lingkungan internal/eksternal, strategi bisnis, dan *Design Factors* awal. |
| | `PM 1.4` | Menentukan ruang lingkup tingkat tinggi (*high-level scope*), tujuan program, dan menyusun **Outline Business Case**. |
| **Change Enablement (CE)** | `CE 1.1` | Menilai kesiapan budaya organisasi terhadap perubahan dan mengidentifikasi potensi resistensi. |
| | `CE 1.2` | Mengidentifikasi pemangku kepentingan kunci (*key stakeholders*), kekuatan pengaruh mereka, dan seorang *Executive Sponsor*. |
| | `CE 1.3` | Merumuskan visi perubahan yang mendesak (*compelling case for change* / *wake-up call*) dalam bahasa bisnis. |
| **Continual Improvement (CI)** | `CI 1.1` | Memetakan konteks bisnis dan strategi organisasi ke *Enterprise Goals* (`EG01`–`EG13`) dan *Alignment Goals* (`AG01`–`AG13`). |
| | `CI 1.2` | Mengidentifikasi kebijakan, tata kelola, dan kerangka kerja yang sudah ada saat ini di perusahaan. |

- **Inputs Fase 1:** Strategi bisnis, laporan risiko korporat, laporan hasil audit terdahulu, keluhan bisnis (*pain points*), regulasi baru, dan tren industri.
- **Outputs Fase 1:** **Outline Business Case**, Peta Pemangku Kepentingan (*Stakeholder Map*), Daftar *Pain Points & Drivers*, dan Mandat Inisiasi Program dari Sponsor Eksekutif.
- **RACI Fase 1:**
  - **Accountable (`A`):** `Board` / `Executive Committee` / `Chief Executive Officer (CEO)`
  - **Responsible (`R`):** `Chief Information Officer (CIO)`, `Chief Risk Officer (CRO)`, `Business Process Owners`
  - **Consulted (`C`):** `CISO`, `CFO`, `Compliance`, `Audit`

---

### FASE 2: Where Are We Now? (Di Mana Posisi Kita Saat Ini?)
- **Tujuan Fase 2:** Menentukan objektif tata kelola dan manajemen mana yang relevan dengan penggerak Fase 1, lalu menilai kondisi saat ini (*As-Is / Current Capability Level*) untuk mengidentifikasi defisiensi yang berdampak paling kritis.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 2 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 2.1` | Membentuk tim asesmen dan menyepakati jadwal serta metodologi penilaian kondisi saat ini. |
| | `PM 2.2` | Memantau kemajuan penilaian kondisi saat ini dan mengelola ekspektasi eksekutif. |
| **Change Enablement (CE)** | `CE 2.1` | Mengomunikasikan tujuan penilaian (*assessment*) secara transparan agar staf tidak bersikap defensif/menyembunyikan masalah. |
| | `CE 2.2` | Melibatkan pemilik proses bisnis dan teknis dalam lokakarya diagnostik (*Management Awareness Diagnostic*) agar mereka mengakui bersama (*co-own*) masalah yang ditemukan. |
| **Continual Improvement (CI)** | `CI 2.1` | Memilih objektif COBIT 2019 yang masuk dalam ruang lingkup penilaian berdasarkan *Goals Cascade* dan *Design Factors* (`DF1`–`DF11`). |
| | `CI 2.2` | Melaksanakan penilaian kapabilitas proses saat ini (*As-Is Capability Level 0–5*) dan maturitas komponen A–G. |
| | `CI 2.3` | Menganalisis akar penyebab (*root causes*) dari kelemahan kapabilitas dan merangkum temuan posisi saat ini. |

- **Inputs Fase 2:** *Outline Business Case*, daftar *Drivers & Pain Points* dari Fase 1, bukti operasional, log insiden, dan laporan audit.
- **Outputs Fase 2:** **Laporan Asesmen Kapabilitas Saat Ini (*As-Is Capability Assessment Report*)**, Daftar Objektif Terpilih, dan Analisis Kekuatan/Kelemahan 7 Komponen.
- **RACI Fase 2:**
  - **Accountable (`A`):** `CIO` / `I&T Governance Board`
  - **Responsible (`R`):** `Business Process Owners`, `Head IT Operations`, `Head Development`, `Head Architect`, `CISO`, `Service Manager`
  - **Consulted (`C`):** `Audit`, `CRO`, `Compliance`

---

### FASE 3: Where Do We Want to Be? (Ke Mana Kita Ingin Menuju?)
- **Tujuan Fase 3:** Menetapkan target tingkat kapabilitas (*To-Be / Target Capability Level*) untuk setiap objektif yang dipilih, menganalisis kesenjangan (*Gap Analysis* antara *As-Is* dan *To-Be*), serta mengidentifikasi opsi-opsi perbaikan beserta *Quick Wins*.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 3 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 3.1` | Mengoordinasikan lokakarya penentuan target dan memastikan keselarasan dengan ketersediaan anggaran/sumber daya. |
| | `PM 3.2` | Memperbarui **Business Case** menjadi dokumen rinci (*Detailed Business Case*) dengan estimasi manfaat dan biaya awal. |
| **Change Enablement (CE)** | `CE 3.1` | Menyepakati visi kondisi masa depan (*To-Be Vision*) bersama para *Business Process Owners* dan pimpinan TI. |
| | `CE 3.2` | Mengidentifikasi dampak perubahan terhadap struktur peran, budaya kerja, dan kompetensi SDM, lalu merancang **Change Enablement Plan**. |
| **Continual Improvement (CI)** | `CI 3.1` | Menentukan **Target Capability Level (1–4/5)** menggunakan alur kerja 4 langkah *COBIT 2019 Design Guide* dan benchmark industri. |
| | `CI 3.2` | Melakukan **Gap Analysis** ($\text{Gap} = \text{Target Level} - \text{Current Level}$) di seluruh 7 Komponen (Proses, Struktur RACI, Informasi, SDM, Kebijakan, Budaya, Alat Bantu). |
| | `CI 3.3` | Merumuskan kandidat inisiatif perbaikan, termasuk mengidentifikasi **Quick Wins** (dampak tinggi, usaha rendah, selesai dalam 30–90 hari). |

- **Inputs Fase 3:** Laporan Asesmen *As-Is* Fase 2, hasil perhitungan *Design Factors*, dan tolok ukur (*benchmark*) regulasi/industri.
- **Outputs Fase 3:** **Dokumen Target Capability & Gap Analysis**, Daftar Kandidat Proyek Perbaikan & *Quick Wins*, serta *Detailed Business Case* draf.
- **RACI Fase 3:**
  - **Accountable (`A`):** `Executive Committee` / `I&T Governance Board`
  - **Responsible (`R`):** `CIO`, `CRO`, `CISO`, `Business Process Owners`, `Head Architect`
  - **Consulted (`C`):** `CFO`, `Head HR`, `Audit`, `Compliance`

---

### FASE 4: What Needs to Be Done? (Apa yang Perlu Dilakukan?)
- **Tujuan Fase 4:** Menerjemahkan kandidat perbaikan dari Fase 3 menjadi proyek-proyek yang dapat dieksekusi dengan prioritas yang jelas, menyusun **Master Implementation Roadmap**, memfinalisasi dan mendapatkan persetujuan resmi atas **Detailed Business Case** dan anggaran program.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 4 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 4.1` | Memprioritaskan dan mengelompokkan inisiatif perbaikan ke dalam paket kerja (*work packages*) / proyek terstruktur. |
| | `PM 4.2` | Menyusun **Program Plan / Master Roadmap** lengkap dengan jadwal, ketergantungan proyek, alokasi anggaran, dan sumber daya. |
| | `PM 4.3` | Memfinalisasi **Detailed Business Case** (termasuk ROI/NPV dan metrik keberhasilan) dan mempresentasikannya untuk persetujuan `Board` / `Executive Committee`. |
| **Change Enablement (CE)** | `CE 4.1` | Memilih *Change Agents / Champions* di setiap unit bisnis dan departemen TI untuk mengawal perubahan. |
| | `CE 4.2` | Menyusun rencana komunikasi, pelatihan, dan pemberdayaan pengguna yang terintegrasi ke dalam *Program Plan*. |
| **Continual Improvement (CI)** | `CI 4.1` | Merancang spesifikasi solusi tata kelola/manajemen dan menentukan metrik pemantauan keberhasilan (*Benefit & Performance Metrics*). |
| | `CI 4.2` | Mengintegrasikan proyek perbaikan tata kelola ke dalam portofolio investasi korporat (`APO05`). |

- **Inputs Fase 4:** Dokumen *Gap Analysis* & kandidat proyek dari Fase 3, batasan anggaran, dan kapasitas SDM.
- **Outputs Fase 4:** **Approved Detailed Business Case**, **Master Implementation Roadmap / Program Plan**, Register Risiko Program, dan Rencana Pengukuran Manfaat.
- **RACI Fase 4:**
  - **Accountable (`A`):** `Executive Committee` / `I&T Governance Board` (untuk persetujuan Business Case), `CIO` / `Program Manager` (untuk perencanaan program)
  - **Responsible (`R`):** `Portfolio Manager`, `Program Manager`, `PMO`, `Business Process Owners`, `CIO`
  - **Consulted (`C`):** `CFO`, `CRO`, `CISO`, `Head HR`

---

### FASE 5: How Do We Get There? (Bagaimana Kita Mencapainya?)
- **Tujuan Fase 5:** Mengembangkan, menguji, dan mengimplementasikan solusi perbaikan tata kelola dan manajemen (kebijakan baru, struktur komite/RACI baru, proses & SOP baru, pelatihan SDM, serta *tooling* GRC/ITSM/SIEM) ke dalam praktik operasional sehari-hari.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 5 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 5.1` | Mengarahkan dan memantau eksekusi seluruh proyek di dalam program perbaikan sesuai jadwal, anggaran, dan mutu (`BAI01`, `BAI11`). |
| | `PM 5.2` | Segera merealisasikan dan memublikasikan keberhasilan **Quick Wins** untuk membangun kredibilitas program. |
| **Change Enablement (CE)** | `CE 5.1` | Melaksanakan kampanye komunikasi, lokakarya sosialisasi kebijakan, pelatihan keterampilan baru, dan *coaching* bagi pemangku peran RACI. |
| | `CE 5.2` | Menangani kantong-kantong resistensi budaya dan memastikan pimpinan memberikan keteladanan (*walk the talk*). |
| **Continual Improvement (CI)** | `CI 5.1` | Mengembangkan atau mengakuisisi artefak seluruh 7 Komponen (SOP, piagam komite, template kontrol, konfigurasi sistem/alat bantu). |
| | `CI 5.2` | Menguji kelayakan solusi baru (*piloting*) dan mengoperasionalkannya ke dalam aktivitas rutin serta memasang mekanisme pengumpulan metrik kinerja (`MEA01`). |

- **Inputs Fase 5:** *Approved Program Plan*, *Change Enablement Plan*, dan standar/praktik terbaik COBIT 2019.
- **Outputs Fase 5:** **Komponen Tata Kelola & Manajemen yang Telah Diimplementasikan dan Beroperasi** (Kebijakan/SOP berlaku, Komite aktif, Alat bantu berjalan, Staf terlatih).
- **RACI Fase 5:**
  - **Accountable (`A`):** `Program Manager` / `CIO` / `Business Process Owners`
  - **Responsible (`R`):** `Project Managers`, `Head IT Operations`, `Head Development`, `Head Architect`, `Service Manager`, `Information Security Manager`
  - **Consulted (`C`):** `PMO`, `Head HR`, `Audit`, `Compliance`

---

### FASE 6: Did We Get There? (Apakah Kita Berhasil Mencapainya?)
- **Tujuan Fase 6:** Memantau apakah solusi yang diimplementasikan di Fase 5 benar-benar bekerja secara berkelanjutan, mengukur apakah **Target Capability Level** dan manfaat bisnis yang dijanjikan di dalam *Business Case* telah tercapai.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 6 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 6.1` | Mengevaluasi kinerja keseluruhan program perbaikan terhadap target waktu, anggaran, dan *deliverables* di *Business Case*. |
| | `PM 6.2` | Memantau dan melaporkan realisasi manfaat (*Benefits Realization Review*) kepada `Executive Committee` dan `Board` (`EDM02`, `APO05`). |
| **Change Enablement (CE)** | `CE 6.1` | Menilai tingkat adopsi budaya dan kepatuhan nyata di lapangan (apakah cara kerja baru sudah mendarah daging atau kembali ke kebiasaan lama). |
| | `CE 6.2` | Memberikan penghargaan (*recognition/rewards*) atas pencapaian target kepatuhan dan kinerja, serta mengoreksi perilaku yang menyimpang. |
| **Continual Improvement (CI)** | `CI 6.1` | Mengumpulkan data metrik dari Balanced Scorecard TI (`EG`, `AG`, dan metrik praktik) serta melakukan penilaian ulang kapabilitas proses (*Post-Implementation Capability Assessment*). |
| | `CI 6.2` | Mengidentifikasi deviasi terhadap target dan merumuskan tindakan korektif (*corrective actions*). |

- **Inputs Fase 6:** Metrik kinerja operasional, log kepatuhan proses, hasil survei pengguna, dan target pada *Approved Business Case*.
- **Outputs Fase 6:** **Scorecard Kinerja & Realisasi Manfaat Tata Kelola**, **Laporan Penilaian Kapabilitas Pasca-Implementasi**, dan Daftar Tindakan Korektif.
- **RACI Fase 6:**
  - **Accountable (`A`):** `Executive Committee` / `I&T Governance Board`
  - **Responsible (`R`):** `CIO`, `CRO`, `Business Process Owners`, `Portfolio Manager`, `Audit`
  - **Consulted (`C`):** `CFO`, `CISO`, `Compliance`

---

### FASE 7: How Do We Keep the Momentum Going? (Bagaimana Kita Menjaga Momentum?)
- **Tujuan Fase 7:** Meninjau efektivitas keseluruhan inisiatif tata kelola, mengidentifikasi kebutuhan tata kelola baru akibat perubahan lingkungan bisnis/teknologi, memperkuat budaya peningkatan berkelanjutan, dan menyiapkan iterasi berikutnya kembali ke **Fase 1**.

| Cincin | Kode Task | Deskripsi Aktivitas Resmi Fase 7 |
| :--- | :---: | :--- |
| **Program Management (PM)** | `PM 7.1` | Menutup secara formal iterasi program saat ini, mendokumentasikan pembelajaran (*lessons learned*), dan mengalihkan pemantauan ke operasi tata kelola rutin (`EDM01`). |
| **Change Enablement (CE)** | `CE 7.1` | Menginstitusionalisasikan budaya tata kelola dan perbaikan berkelanjutan ke dalam KPI individu, orientasi karyawan baru, dan komunikasi korporat. |
| | `CE 7.2` | Memelihara komitmen jangka panjang dari `Board` dan manajemen eksekutif. |
| **Continual Improvement (CI)** | `CI 7.1` | Mengidentifikasi peluang peningkatan lebih lanjut dari pengalaman operasional, tren teknologi baru, perubahan *Design Factors*, atau regulasi baru. |
| | `CI 7.2` | Memicu siklus hidup iterasi berikutnya (kembali ke **Fase 1**). |

- **Inputs Fase 7:** Laporan kinerja & realisasi manfaat dari Fase 6, *lessons learned*, dan perubahan strategi/lingkungan.
- **Outputs Fase 7:** **Laporan Tinjauan Efektivitas Program (*Program Effectiveness Review*)**, Pengetahuan Terdokumentasi (`BAI08`), dan **Pemicu Iterasi Baru ke Fase 1**.
- **RACI Fase 7:**
  - **Accountable (`A`):** `Board` / `Executive Committee`
  - **Responsible (`R`):** `I&T Governance Board`, `CIO`, `CRO`, `Business Process Owners`
  - **Consulted (`C`):** `CISO`, `Audit`, `Compliance`

---

## 4. Tantangan Umum (*Common Challenges*) & Faktor Penentu Keberhasilan (*CSFs*) Implementasi

| Tantangan Umum Kegagalan Implementasi | Akar Penyebab | Faktor Penentu Keberhasilan (*Critical Success Factors / CSFs*) |
| :--- | :--- | :--- |
| **Kehilangan Komitmen Eksekutif di Tengah Jalan** | Program dianggap sebagai "proyek internal departemen TI", bukan inisiatif bisnis. | • Pastikan seorang eksekutif bisnis senior menjadi *Sponsor* (`EDM01`).<br>• Gunakan **Business Case** berbasis nilai bisnis dan mitigasi risiko nyata, bukan jargon teknis COBIT. |
| **Lingkup Terlalu Ambisius (*Boiling the Ocean*)** | Mencoba mengimplementasikan 40 objektif sekaligus ke Level 3 dalam satu tahun. | • Batasi setiap iterasi siklus hidup hanya pada **5–8 objektif paling kritis** hasil *Design Factors*.<br>• Eksekusi **Quick Wins** dalam 60–90 hari pertama untuk membuktikan nilai. |
| **Resistensi Staf & Unit Bisnis ("Terlalu Birokratis")** | *Change Enablement (Middle Ring)* diabaikan; SOP dibuat kaku tanpa melibatkan pelaksana lapangan. | • Libatkan *Business Process Owners* dan tim teknis sejak Fase 2 dan Fase 3.<br>• Rancang kontrol yang terotomatisasi di dalam alur kerja (mis. CI/CD & ITSM), bukan formulir kertas berlapis-lapis. |

---

## 5. Template Standar *EGIT Business Case* (Siap Pakai untuk Fase 1–4)

Gunakan struktur resmi berikut saat menyusun proposal *Business Case* implementasi atau perbaikan tata kelola TI:

```markdown
# DOKUMEN BUSINESS CASE: PROGRAM PENINGKATAN TATA KELOLA & MANAJEMEN I&T (COBIT 2019)

## 1. Ringkasan Eksekutif (Executive Summary)
- **Sponsor Eksekutif:** [Nama & Jabatan, mis. Direktur Utama / Direktur Manajemen Risiko]
- **Tujuan Program:** [Ringkasan 2–3 kalimat mengenai sasaran bisnis dan mitigasi risiko yang ingin dicapai]
- **Total Estimasi Investasi vs. Estimasi Manfaat / Penghindaran Kerugian:** [Rp XXX Juta/Miliar]

## 2. Penggerak Bisnis, Pain Points & Trigger Events (Fase 1)
- **Pain Points Aktual:** [Sebutkan insiden nyata, temuan audit, denda regulasi, atau kegagalan proyek]
- **Trigger Events Strategis:** [Sebutkan regulasi baru seperti UU PDP / POJK 11/2022, transformasi digital, atau migrasi Cloud]
- **Keterkaitan Goals Cascade:**
  - *Enterprise Goals:* `[EGxx]` — [Nama EG]
  - *Alignment Goals:* `[AGxx]` — [Nama AG]

## 3. Penilaian Kondisi Saat Ini vs. Target Kapabilitas (Fase 2 & Fase 3)
| Kode Objektif | Nama Objektif | Current Level (As-Is) | Target Level (To-Be) | Gap | Masalah Utama Komponen A–G |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `[Objektif 1]` | `[Nama]` | Level `[X]` | Level `[Y]` | `[Y-X]` | `[Ringkasan kelemahan proses/RACI/kebijakan/alat]` |

## 4. Ruang Lingkup Solusi, Quick Wins & Peta Jalan Implementasi (Fase 4)
- **Gelombang 1 — Quick Wins (Bulan 1–3):** [Inisiatif berdampak cepat, mis. pembentukan ITSC/CAB, kebijakan akses darurat, backup restore test]
- **Gelombang 2 — Fondasi & Standarisasi (Bulan 4–8):** [Pembangunan proses & SOP Level 3, implementasi tooling ITSM/SIEM/PAM]
- **Gelombang 3 — Pengukuran Kuantitatif & Asurans (Bulan 9–12):** [Dashboard KPI/KGI, audit kepatuhan internal]

## 5. Analisis Manfaat Finansial & Non-Finansial (Benefits Realization)
- **Manfaat Finansial (Hard Benefits):** [Penghindaran denda regulasi, pengurangan kerugian downtime, penghematan lisensi/cloud]
- **Manfaat Non-Finansial (Soft Benefits):** [Kecepatan time-to-market, kepuasan nasabah, kepatuhan audit]

## 6. Estimasi Biaya, Sumber Daya & Risiko Program
- **Anggaran CAPEX & OPEX:** [Rincian biaya perangkat lunak, konsultansi, pelatihan, dan alokasi jam kerja internal]
- **Risiko Jika Tidak Bertindak (*Risk of Doing Nothing*):** [Konsekuensi bisnis jika status quo dibiarkan]
- **Risiko Program & Mitigasi:** [Risiko resistensi budaya, keterbatasan waktu staf, dan mitigasinya]
```
