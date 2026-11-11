# Bab 9: COBIT 2019 Design Factors (DF1–DF11), Metodologi Tailoring Sistem Tata Kelola & Management Awareness Diagnostic

> **Sumber Otoritatif:** *COBIT® 2019 Design Guide: Designing an Information and Technology Governance Solution*, *COBIT® 2019 Framework: Introduction and Methodology (Chapter 5 & 7)*, dan *COBIT 2019 Toolkit v12 (`COBIT 2019_Management-Awareness-Diagnostic_v1.0.xls`)*.

---

## 1. Konsep Dasar *Design Factors* dalam COBIT 2019

Tidak ada dua organisasi yang memiliki profil strategi, risiko, dan arsitektur teknologi yang persis sama. Oleh karena itu, menerapkan seluruh 40 objektif COBIT 2019 pada tingkat kapabilitas tinggi secara merata adalah pemborosan sumber daya (*over-governance*).

**Design Factors (Faktor Desain)** adalah faktor-faktor kontekstual yang memengaruhi perancangan sistem tata kelola perusahaan dan memosisikannya untuk keberhasilan penggunaan I&T.

### Tiga Dampak Utama *Design Factors* (*Three Impacts of Design Factors*)
1. **Objective Priority & Target Capability Levels (Prioritas Objektif & Target Level Kapabilitas):** Menentukan objektif mana dari 40 objektif di *COBIT Core Model* yang lebih penting dibanding yang lain sehingga wajib mencapai **Capability Level 3 atau Level 4**, dan mana yang cukup berada di **Level 1 atau Level 2**.
2. **Component Variations (Variasi Komponen):** Memodifikasi komponen non-proses (Struktur Organisasi, Kebijakan, Keterampilan, Budaya, Alat Bantu) agar sesuai dengan konteks (mis. organisasi *DevOps* memerlukan variasi kontrol perubahan otomatis dibanding organisasi *Traditional Waterfall*).
3. **Specific Focus Areas (Area Fokus Spesifik):** Mengarahkan penggunaan panduan spesifik seperti *Cybersecurity*, *Cloud Computing*, *DevOps*, *Small and Medium Enterprises (SME)*, atau *Privacy*.

---

## 2. Katalog Lengkap 11 Design Factors (DF1 s.d. DF11)

```
+-----------------------------------------------------------------------------------+
|                        11 COBIT 2019 DESIGN FACTORS                               |
+-----------------------------------------+-----------------------------------------+
| Konteks Strategis & Tujuan              | Konteks Ancaman, Peran & Operasional TI |
| • DF1: Enterprise Strategy (4 Archetype)| • DF5: Threat Landscape (Normal / High) |
| • DF2: Enterprise Goals (EG01–EG13)     | • DF6: Compliance Requirements (L/N/H)  |
|                                         | • DF7: Role of IT (4 Peran McFarlan)    |
| Konteks Risiko & Masalah Saat Ini       | • DF8: Sourcing Model (Outsource/Cloud/ |
| • DF3: Risk Profile (19 Kategori Risiko)|        Insource)                        |
| • DF4: I&T-Related Issues (20 Isu A–T)  | • DF9: IT Implementation Methods        |
|                                         |        (Agile / DevOps / Traditional)   |
| Konteks Ukuran & Adopsi                 |                                         |
| • DF10: Tech Adoption Strategy          |                                         |
| • DF11: Enterprise Size (Large vs SME)  |                                         |
+-----------------------------------------+-----------------------------------------+
```

---

### DF1: Enterprise Strategy (Strategi Perusahaan)
Organisasi menilai tingkat kepentingan (skala `1` s.d. `5`) pada empat arketipe strategi bisnis berikut:

| Arketipe Strategi DF1 | Deskripsi Fokus Strategis | Objektif COBIT 2019 yang Diprioritaskan (Primary Boost) |
| :--- | :--- | :--- |
| **1. Growth / Acquisition** | Fokus pada pertumbuhan pendapatan, ekspansi pasar, dan akuisisi/merger perusahaan. | `EDM01`, `EDM02`, `APO02`, `APO03`, `APO05`, `BAI01`, `BAI05`, `BAI11` |
| **2. Innovation / Differentiation** | Fokus pada penawaran produk dan layanan baru yang berbeda dan inovatif kepada nasabah/pelanggan. | `EDM02`, `APO02`, `APO04`, `APO07`, `APO08`, `BAI02`, `BAI03`, `BAI05`, `BAI08` |
| **3. Cost Leadership** | Fokus pada minimalisasi biaya jangka pendek dan efisiensi operasional secara ketat. | `EDM04`, `APO05`, `APO06`, `APO09`, `APO10`, `BAI04`, `BAI09`, `DSS01` |
| **4. Client Service / Stability** | Fokus pada penyediaan layanan yang stabil, andal, aman, dan berorientasi pelanggan jangka panjang. | `EDM03`, `APO08`, `APO09`, `APO11`, `APO12`, `APO13`, `DSS01`, `DSS02`, `DSS03`, `DSS04`, `DSS05` |

---

### DF2: Enterprise Goals (Tujuan Perusahaan)
Menggunakan **13 Enterprise Goals (`EG01`–`EG13`)** pada *Goals Cascade* (lihat [Bab 2](02-goals-cascade-and-metrics-dictionary.md)), dinilai pada skala kepentingan `1` s.d. `5`.

---

### DF3: Risk Profile (Profil Risiko TI — 19 Kategori Skenario Risiko)
Mengukur eksposur risiko perusahaan saat ini pada **19 kategori skenario risiko TI** melalui rumus:
$$\text{Risk Rating} = \text{Impact } (1..5) \times \text{Likelihood } (1..5)$$

Berikut adalah pemetaan resmi ke-19 kategori risiko TI pada `DF3` ke objektif prioritas COBIT 2019:

| No. | Kategori Skenario Risiko TI (DF3) | Penjelasan Skenario Risiko | Objektif COBIT 2019 Prioritas (Mitigasi Utama) |
| :---: | :--- | :--- | :--- |
| **1** | **IT investment decision making, portfolio definition & maintenance** | Investasi TI salah sasaran, duplikasi sistem, atau tidak selaras strategi bisnis. | `EDM01`, `EDM02`, `APO02`, `APO05` |
| **2** | **Program & projects life cycle management** | Proyek terlambat, *over-budget*, gagal mencapai lingkup/manfaat (*scope creep*). | `EDM02`, `APO05`, `BAI01`, `BAI05`, `BAI07`, `BAI11` |
| **3** | **IT cost & oversight** | Pembengkakan biaya operasional/cloud TI (*cost overrun*) dan ketiadaan transparansi biaya. | `EDM04`, `APO05`, `APO06` |
| **4** | **IT expertise, skills & behavior** | Kekurangan talenta kunci TI, *turnover* tinggi, atau perilaku staf yang tidak etis/lalai. | `EDM04`, `APO01`, `APO07` |
| **5** | **Enterprise / IT architecture** | Arsitektur silo, kaku, usang (*legacy*), dan menghambat integrasi bisnis. | `APO02`, `APO03`, `BAI02`, `BAI03` |
| **6** | **IT operational infrastructure incidents** | Kerusakan perangkat keras, kegagalan pusat data, atau gangguan jaringan inti. | `BAI04`, `BAI09`, `BAI10`, `DSS01`, `DSS02`, `DSS03`, `DSS04` |
| **7** | **Unauthorized actions** | Penyalahgunaan hak akses (*privilege abuse*), perubahan ilegal, atau kecurangan (*fraud*) internal. | `APO13`, `BAI06`, `BAI10`, `DSS05`, `DSS06`, `MEA02` |
| **8** | **Software adoption / usage problems** | Pengguna bisnis gagal atau menolak menggunakan aplikasi baru yang telah dibangun. | `APO08`, `BAI02`, `BAI05`, `BAI07`, `BAI08` |
| **9** | **Hardware incidents** | Kegagalan fisik server/perangkat endpoint, pencurian aset, atau kehabisan kapasitas. | `BAI04`, `BAI09`, `DSS01`, `DSS05` |
| **10** | **Software failures** | *Bug* kritis aplikasi produksi, korupsi data akibat kesalahan logika kode, atau gagal rilis. | `APO11`, `BAI02`, `BAI03`, `BAI06`, `BAI07`, `DSS02`, `DSS03` |
| **11** | **Logical attacks (hacking, malware, etc.)** | Serangan *ransomware*, DDoS, *phishing*, peretasan aplikasi web/API, dan intrusi jaringan. | `EDM03`, `APO12`, `APO13`, `BAI03`, `BAI06`, `BAI10`, `DSS02`, `DSS04`, `DSS05` |
| **12** | **Third-party / supplier incidents** | Kegagalan layanan vendor Cloud/SaaS, kebangkrutan vendor, atau kebocoran data lewat vendor. | `APO09`, `APO10`, `DSS04`, `DSS05`, `MEA03` |
| **13** | **Noncompliance** | Pelanggaran UU PDP, POJK, aturan sektoral, atau pelanggaran lisensi perangkat lunak. | `EDM01`, `EDM03`, `APO01`, `BAI09`, `MEA02`, `MEA03`, `MEA04` |
| **14** | **Geopolitical issues** | Embargo teknologi, pembatasan transfer data lintas batas negara, atau gangguan wilayah. | `EDM03`, `APO10`, `APO12`, `DSS04`, `MEA03` |
| **15** | **Industrial action** | Pemogokan kerja, perselisihan ketenagakerjaan, atau sabotase oleh personel internal/outsourcing. | `APO07`, `APO10`, `DSS04`, `DSS05` |
| **16** | **Acts of nature** | Bencana alam (gempa bumi, banjir, kebakaran) yang melumpuhkan fasilitas Data Center utama. | `DSS01`, `DSS04`, `DSS05` |
| **17** | **Technology-based innovation** | Kegagalan mengidentifikasi/mengadopsi teknologi disruptif baru sehingga kalah bersaing. | `EDM02`, `APO02`, `APO04`, `APO08`, `BAI08` |
| **18** | **Environmental** | Ketidakpatuhan terhadap standar ramah lingkungan (*Green IT*), konsumsi daya berlebih, atau limbah elektronik (*e-waste*). | `EDM01`, `BAI09`, `DSS01`, `MEA03` |
| **19** | **Data & information management** | Kualitas data buruk, ketiadaan *master data*, pelanggaran privasi data, atau kehilangan data kritis. | `APO03`, `APO13`, `APO14`, `DSS05`, `DSS06`, `MEA03` |

---

### DF4: I&T-Related Issues (20 Masalah Aktual Terkait I&T — Kode A s.d. T)
Berbeda dengan `DF3` yang menilai potensi risiko, **`DF4` menilai masalah nyata (*realized risks / pain points*)** yang sedang dialami perusahaan saat ini (dinilai pada skala `1` = Tidak Ada Masalah, `2` = Ada Masalah, `3` = Masalah Serius):

| Kode | Deskripsi Masalah Aktual Terkait I&T (DF4) | Objektif COBIT 2019 Prioritas (Solusi Langsung) |
| :---: | :--- | :--- |
| **A** | Frustrasi antara berbagai entitas di dalam organisasi TI karena persepsi kontribusi yang rendah terhadap nilai bisnis. | `EDM01`, `EDM02`, `APO01`, `APO02`, `APO08` |
| **B** | Frustrasi antara departemen bisnis (sebagai pelanggan TI) dan departemen TI karena proyek yang gagal dan persepsi kontribusi yang rendah terhadap nilai bisnis. | `EDM02`, `APO02`, `APO08`, `APO09`, `BAI01`, `BAI11` |
| **C** | Insiden signifikan terkait I&T — seperti kehilangan data, kegagalan proyek, kesalahan aplikasi, atau kegagalan layanan — yang telah dialami secara nyata. | `EDM03`, `APO12`, `APO13`, `APO14`, `BAI06`, `DSS02`, `DSS03`, `DSS04`, `DSS05` |
| **D** | Masalah pengiriman layanan oleh penyedia pihak ketiga (*outsourcer* / vendor / Cloud). | `APO09`, `APO10`, `MEA01` |
| **E** | Kegagalan memenuhi persyaratan regulasi atau kontrak terkait TI (mis. denda/teguran OJK, BI, UU PDP, lisensi). | `EDM01`, `EDM03`, `APO10`, `BAI09`, `MEA02`, `MEA03`, `MEA04` |
| **F** | Temuan audit reguler atau laporan asurans lainnya tentang kinerja TI yang buruk atau masalah kualitas/keamanan layanan TI yang belum terselesaikan. | `EDM05`, `APO11`, `APO13`, `MEA01`, `MEA02`, `MEA04` |
| **G** | Pengeluaran TI yang tersembunyi dan tidak terkendali (*Shadow IT*), yaitu pengeluaran I&T oleh departemen pengguna di luar kendali mekanisme otorisasi investasi TI normal. | `EDM01`, `EDM02`, `APO05`, `APO06`, `APO08`, `BAI09` |
| **H** | Duplikasi atau tumpang tindih antara berbagai inisiatif/proyek, atau bentuk pemborosan sumber daya I&T lainnya. | `EDM02`, `EDM04`, `APO03`, `APO05`, `BAI01` |
| **I** | Sumber daya TI tidak mencukupi, staf mengalami kelelahan (*burnout*) atau ketidakpuasan kerja, dan *turnover* tinggi. | `EDM04`, `APO01`, `APO07` |
| **J** | Perubahan atau proyek yang diaktifkan oleh TI sering gagal memenuhi kebutuhan bisnis dan dikirimkan terlambat atau melebihi anggaran (*over budget*). | `APO05`, `APO11`, `BAI01`, `BAI02`, `BAI03`, `BAI05`, `BAI11` |
| **K** | Anggota dewan direksi/komisaris, eksekutif, atau manajemen senior enggan terlibat dengan TI, atau kurangnya sponsor bisnis yang berkomitmen untuk TI. | `EDM01`, `EDM02`, `EDM05`, `APO01`, `APO08`, `BAI01` |
| **L** | Model operasi TI yang kompleks dan/atau mekanisme keputusan yang tidak jelas untuk keputusan terkait TI. | `EDM01`, `APO01`, `APO03` |
| **M** | Biaya TI yang sangat tinggi atau terus membengkak tanpa kejelasan timbal balik nilai (*return on value*). | `EDM02`, `EDM04`, `APO05`, `APO06`, `BAI09` |
| **N** | Implementasi inisiatif atau inovasi baru terhalang atau diperlambat oleh arsitektur dan sistem TI saat ini (*legacy debt*). | `APO03`, `APO04`, `BAI02`, `BAI03` |
| **O** | Kesenjangan antara pengetahuan bisnis dan pengetahuan teknis, yang menyebabkan pengguna bisnis dan spesialis informasi/teknologi berbicara dalam "bahasa yang berbeda". | `APO01`, `APO07`, `APO08`, `BAI02`, `BAI08` |
| **P** | Masalah reguler dengan kualitas data dan integrasi data di berbagai sumber (laporan tidak sinkron). | `APO03`, `APO14`, `DSS06` |
| **Q** | Tingkat digitalisasi proses inti yang tinggi namun kematangan keamanan dan kontrol yang rendah. | `EDM03`, `APO12`, `APO13`, `DSS05`, `DSS06`, `MEA02` |
| **R** | Ketidakmampuan untuk mengeksploitasi teknologi baru atau berinovasi menggunakan I&T. | `EDM02`, `APO02`, `APO04`, `APO07`, `APO08`, `BAI08` |
| **S** | Ketergantungan yang berlebihan pada vendor pihak ketiga atau ketiadaan kendali atas kekayaan intelektual/kode sumber. | `APO03`, `APO10`, `BAI03`, `BAI09` |
| **T** | Banyaknya pengecualian (*exceptions*) dan tambal sulam (*workarounds*) dalam proses operasional TI sehari-hari. | `APO01`, `APO11`, `BAI06`, `DSS01`, `DSS03`, `MEA01`, `MEA02` |

---

### DF5 s.d. DF11: Faktor Kontekstual Ancaman, Kepatuhan, Peran, Sourcing, Metode, Adopsi & Ukuran

| Kode DF | Nama Design Factor | Nilai Parameter Resmi | Pengaruh Utama terhadap Prioritas Objektif & Variasi Komponen |
| :---: | :--- | :--- | :--- |
| **DF5** | **Threat Landscape** (Lanskap Ancaman) | • `Normal`<br>• `High` (Geopolitik, Sektor Kritis/Keuangan, Target APT) | Jika **`High`**: Meningkatkan drastis target kapabilitas pada `EDM03`, `APO12`, `APO13`, `BAI03`, `BAI06`, `BAI10`, `DSS02`, `DSS04`, `DSS05`, dan `MEA02` (minimal Level 3–4). |
| **DF6** | **Compliance Requirements** (Persyaratan Kepatuhan) | • `Low`<br>• `Normal`<br>• `High` (Perbankan/OJK, Kesehatan, BUMN, Publik) | Jika **`High`**: Meningkatkan drastis target kapabilitas pada `EDM01`, `EDM03`, `EDM05`, `APO12`, `APO13`, `APO14`, `DSS05`, `DSS06`, `MEA02`, `MEA03`, dan `MEA04`. |
| **DF7** | **Role of IT** (Peran TI — *McFarlan Grid*) | • `Support` (Pendukung back-office)<br>• `Factory` (Operasional saat ini kritis)<br>• `Turnaround` (Inovasi masa depan kritis)<br>• `Strategic` (Operasional saat ini & masa depan sama-sama kritis) | • **`Factory`**: Prioritaskan `BAI04`, `BAI06`, `DSS01`–`DSS05` (ketersediaan & kontinuitas).<br>• **`Turnaround`**: Prioritaskan `APO02`, `APO03`, `APO04`, `BAI01`–`BAI03`, `BAI11`.<br>• **`Strategic`**: Wajib kapabilitas tinggi pada domain `EDM`, `APO`, `BAI`, dan `DSS`. |
| **DF8** | **Sourcing Model for IT** (Model Pengadaan TI) | • `Outsourcing` (Managed Services)<br>• `Cloud` (IaaS/PaaS/SaaS)<br>• `Insourced` (Internal)<br>• `Hybrid` | • **`Outsourcing` / `Cloud`**: Meningkatkan prioritas `EDM03`, `APO09` (SLA), `APO10` (Vendor), `APO12`, `APO13`, `BAI06`, `MEA01`, `MEA03`.<br>• **`Insourced`**: Meningkatkan prioritas `EDM04`, `APO07` (SDM), `BAI03`, `DSS01`. |
| **DF9** | **IT Implementation Methods** (Metode Implementasi TI) | • `Agile`<br>• `DevOps`<br>• `Traditional` (Waterfall)<br>• `Hybrid` | Jika **`Agile` / `DevOps`**: Meningkatkan prioritas `APO03`, `BAI02`, `BAI03`, `BAI06` (Automated CI/CD Change Control), `BAI07`, `BAI10` (Infrastructure as Code), dan `DSS02`. |
| **DF10** | **Technology Adoption Strategy** (Strategi Adopsi Teknologi) | • `First Mover` (Pionir)<br>• `Follower` (Pengikut Cepat)<br>• `Slow Adopter` (Konservatif) | Jika **`First Mover`**: Meningkatkan prioritas `EDM02`, `EDM03`, `APO02`, `APO04` (Inovasi/PoC), `APO05`, `APO12`, `BAI01`, `BAI03`, `BAI05`. |
| **DF11** | **Enterprise Size** (Ukuran Perusahaan) | • `Large Enterprise` (>250 pegawai penuh waktu)<br>• `Small and Medium Enterprise (SME)` (50–250 pegawai) | Jika **`SME`**: Menggunakan *SME Focus Area* dengan penyederhanaan struktur komite, penggabungan peran RACI yang aman, dan target kapabilitas yang proporsional. |

---

## 3. Empat Langkah *Governance System Design Workflow*

Dalam merancang atau mengaudit kesesuaian sistem tata kelola TI organisasi, ikuti **4 Langkah Alur Kerja Desain Resmi COBIT 2019**:

```
+-----------------------------------------------------------------------+
| STEP 1: Understand the Enterprise Context and Strategy                |
|         Kaji DF1 (Strategy), DF2 (Goals), DF3 (Risk Profile),         |
|         dan DF4 (Current I&T Issues).                                 |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| STEP 2: Determine the Initial Scope of the Governance System          |
|         Hitung skor kontribusi DF1–DF4 terhadap 40 Objektif COBIT.    |
|         Hasilkan daftar prioritas awal (Initial Priority Scores).     |
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| STEP 3: Refine the Scope of the Governance System                     |
|         Terapkan bobot pengali/penyesuaian dari DF5 s.d. DF11         |
|         (Threat, Compliance, Role of IT, Sourcing, Agile/DevOps, dll).|
+-----------------------------------+-----------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
| STEP 4: Conclude the Governance System Design                         |
|         Selesaikan konflik matematis (Resolve Inherent Conflicts),    |
|         tetapkan Target Capability Level (1–4) yang disepakati,       |
|         dan sesuaikan variasi Komponen B s.d. G.                      |
+-----------------------------------------------------------------------+
```

### Aturan Konversi Skor Prioritas Desain ke Target Capability Level
Dalam *COBIT 2019 Design Guide Toolkit*, skor relatif setiap objektif (pada skala $-100$ hingga $+100$ terhadap baseline) dikonversi menjadi **Target Capability Level** sebagai berikut:
- **Skor Relatif $\ge +75$**: Target **Capability Level 4** (*Predictable*)
- **Skor Relatif $+25$ s.d. $+74$**: Target **Capability Level 3** (*Established*)
- **Skor Relatif $-25$ s.d. $+24$**: Target **Capability Level 2** (*Managed*)
- **Skor Relatif $< -25$**: Target **Capability Level 1** (*Performed*)

---

## 4. Management Awareness Diagnostic Tool (*COBIT 2019 Toolkit v12*)

Berdasarkan instrumen resmi `COBIT 2019_Management-Awareness-Diagnostic_v1.0.xls` di dalam Toolkit v12, auditor TI atau konsultan tata kelola dapat memfasilitasi lokakarya diagnostik cepat bersama manajemen eksekutif menggunakan **7 Parameter Diagnostik** untuk setiap dari 40 Objektif COBIT 2019:

| No. | Parameter Diagnostik | Skala / Pilihan Nilai Resmi | Kegunaan Analisis Audit & Tata Kelola |
| :---: | :--- | :--- | :--- |
| **1** | **Importance (Tingkat Kepentingan)** | Skala `1` s.d. `5`:<br>`1` = *Not Important*<br>`2` = *Somewhat Important*<br>`3` = *Important*<br>`4` = *Very Important*<br>`5` = *Critically Important* | Mengukur seberapa vital objektif tersebut bagi pencapaian tujuan bisnis dan mitigasi risiko saat ini. |
| **2** | **Performance (Kinerja Saat Ini)** | Skala `1` s.d. `5`:<br>`1` = *Very Poor*<br>`2` = *Poor*<br>`3` = *Average*<br>`4` = *Good*<br>`5` = *Very Good* | Mengukur persepsi/realitas efektivitas pelaksanaan objektif saat ini.<br>**Rumus Gap Prioritas Audit:** $\text{Gap} = \text{Importance} - \text{Performance}$. Objektif dengan $\text{Importance} \ge 4$ dan $\text{Performance} \le 2$ ($\text{Gap} \ge 2$) adalah **Sasaran Utama Audit (Immediate Audit & Remediation Target)**. |
| **3** | **Performed Outside IT / Outsourced** | `Yes` / `No` / `Partially` | Mengidentifikasi apakah proses tersebut dijalankan oleh unit bisnis di luar TI (*Shadow IT / Business-led*) atau diserahkan kepada vendor pihak ketiga (*Outsourced*). Jika `Yes`, wajib diuji kontrol `APO09`/`APO10`. |
| **4** | **Formality (Tingkat Formalitas)** | • `Ad-hoc / Informal`<br>• `Intuitive / Repeatable`<br>• `Documented / Standardized`<br>• `Monitored / Measured` | Indikator proksi cepat untuk mengestimasi *Current Capability Level* (Level 1 s.d. Level 4) sebelum pengujian mendalam. |
| **5** | **Audited Recently (Pernah Diaudit)** | `Yes` (dalam 12–24 bulan terakhir) / `No` | Mengidentifikasi *Audit Blind Spots*: objektif dengan `Importance = 5` namun `Audited = No` wajib dimasukkan ke dalam Rencana Audit Tahunan (*Annual IT Audit Plan*). |
| **6** | **Accountable (A)** | Nama Jabatan / Komite Saat Ini | Dibandingkan langsung dengan standar RACI COBIT 2019 untuk mendeteksi ketiadaan pemilik proses (*Orphan Process*) atau kesalahan penempatan akuntabilitas. |
| **7** | **Responsible (R)** | Nama Jabatan / Tim Pelaksana Saat Ini | Dibandingkan dengan standar RACI COBIT 2019 untuk mendeteksi konflik *Segregation of Duties (SoD)* (mis. pelaksana `R` merangkap sebagai penanggung jawab `A` pada proses pengawasan). |
