# Bab 1: Fondasi Eksekutif COBIT 2019, Prinsip Tata Kelola, 7 Komponen & Model Kapabilitas

> **Sumber Otoritatif:** *COBIT® 2019 Framework: Introduction and Methodology*, *COBIT® 2019 Framework: Governance and Management Objectives*, *COBIT® 2019 Overview v1.1*, dan *COBIT® 2019 Major Differences with COBIT 5 v1.1*.

---

## 1. Definisi Eksekutif: Enterprise Governance of Information and Technology (EGIT)

Dalam era transformasi digital, **Informasi dan Teknologi (I&T)** bukan lagi sekadar fungsi pendukung teknis di ruang server, melainkan tulang punggung penciptaan nilai bisnis (*value creation*). **Enterprise Governance of Information and Technology (EGIT)** adalah bagian integral dari tata kelola korporat (*Corporate Governance*) yang dijalankan oleh **Dewan Komisaris / Dewan Pengawas dan Dewan Direksi (*Board*)**.

EGIT berfokus pada pengawasan terhadap definisi dan implementasi proses, struktur, serta mekanisme relasional dalam organisasi yang memungkinkan jajaran bisnis dan TI melaksanakan tanggung jawab mereka dalam menyelaraskan strategi bisnis-TI serta menciptakan nilai dari investasi teknologi.

### Tiga Hasil Utama Tata Kelola TI (*Three Governance Outcomes*)
Seluruh aktivitas tata kelola dan audit COBIT 2019 bermuara pada tiga hasil strategis (*Value Creation*):

```
                      +-----------------------------------+
                      |         VALUE CREATION            |
                      |   (Penciptaan Nilai Bisnis I&T)   |
                      +-----------------+-----------------+
                                        |
         +------------------------------+------------------------------+
         |                              |                              |
         v                              v                              v
+-------------------------+  +-------------------------+  +-------------------------+
|  1. BENEFITS REALIZATION|  |   2. RISK OPTIMIZATION  |  | 3. RESOURCE OPTIMIZATION|
|    (Realisasi Manfaat)  |  |   (Optimalisasi Risiko) |  | (Optimalisasi Sumber    |
|                         |  |                         |  |         Daya)           |
| • Investasi TI memberi  |  | • Risiko siber, operasi,|  | • SDM, anggaran, data,  |
|   nilai bisnis nyata    |  |   & kepatuhan berada di |  |   aplikasi & infrastruk-|
| • Layanan TI mendukung  |  |   dalam Risk Appetite   |  |   tur digunakan secara  |
|   daya saing & inovasi  |  | • Integrasi IT Risk ke  |  |   efisien, efektif, dan |
| • Fokus: EDM02, APO05   |  |   ERM (EDM03, APO12)    |  |   tepat guna (EDM04)    |
+-------------------------+  +-------------------------+  +-------------------------+
```

---

## 2. Pemisahan Tegas: *Governance* vs. *Management*

Prinsip paling fundamental dalam COBIT 2019 yang wajib diuji oleh setiap Auditor TI adalah pemisahan tegas antara **Tata Kelola (*Governance*)** dan **Manajemen (*Management*)**:

| Dimensi Perbandingan | Tata Kelola (*Governance*) | Manajemen (*Management*) |
| :--- | :--- | :--- |
| **Aktor Utama (Accountable)** | **Board** (Dewan Komisaris / Dewan Direksi), *Executive Committee*, *I&T Governance Board* | **Manajemen Eksekutif & Senior** (`CIO`, `CTO`, `CDO`, `CISO`, `CRO`, `CFO`, `COO`, *Business Process Owners*, Kepala Divisi TI) |
| **Mandat Utama** | **Evaluate, Direct and Monitor (EDM)**: Mengevaluasi kebutuhan pemangku kepentingan, memberikan arahan strategis melalui prioritisasi & pengambilan keputusan, serta memantau kinerja dan kepatuhan terhadap arah yang ditetapkan. | **Plan, Build, Run and Monitor (PBRM)**: Merencanakan, membangun, menjalankan, dan memantau seluruh aktivitas operasional sejalan dengan arah yang ditetapkan oleh badan tata kelola untuk mencapai tujuan korporat. |
| **Domain COBIT 2019** | **1 Domain Tata Kelola (`EDM`)** — terdiri atas **5 Governance Objectives** (`EDM01`–`EDM05`) | **4 Domain Manajemen (`APO`, `BAI`, `DSS`, `MEA`)** — terdiri atas **35 Management Objectives** |
| **Fokus Pertanyaan Audit** | *"Apakah kita melakukan hal yang benar (Doing the right things), dengan cara yang benar (Doing them the right way), dan mendapatkan manfaatnya (Are we getting the benefits)?"* | *"Apakah strategi dieksekusi secara efektif, solusi dibangun tepat waktu/mutu, layanan dikirimkan secara aman/andal, dan kontrol dipantau secara konsisten?"* |

> [!IMPORTANT]
> **Implikasi Audit Kritis:** Apabila dalam suatu organisasi `CIO` atau `Head IT Operations` menetapkan sendiri arah strategis TI, menyetujui *Risk Appetite* TI, dan menilai sendiri kinerjanya tanpa keterlibatan aktif `Board` / `Executive Committee`, maka terdapat **Kegagalan Struktur Tata Kelola (*Governance Vacuum / Self-Governance Conflict*)** yang melanggar `EDM01` dan prinsip *Segregation of Duties (SoD)*.

---

## 3. Enam Prinsip Sistem Tata Kelola vs. Tiga Prinsip Kerangka Kerja

COBIT 2019 membagi prinsip dasarnya menjadi dua kelompok yang berbeda:

### A. 6 Prinsip Sistem Tata Kelola (*6 Principles for a Governance System*)
1. **Provide Stakeholder Value (Memberikan Nilai bagi Pemangku Kepentingan):** Setiap perusahaan memerlukan sistem tata kelola untuk memenuhi kebutuhan pemangku kepentingan dan menghasilkan nilai dari penggunaan I&T melalui keseimbangan antara manfaat, risiko, dan sumber daya.
2. **Holistic Approach (Pendekatan Holistik):** Sistem tata kelola I&T dibangun dari sejumlah komponen (7 komponen) yang terdiri atas berbagai jenis yang bekerja secara bersama-sama dan saling bergantung.
3. **Dynamic Governance System (Sistem Tata Kelola yang Dinamis):** Sistem tata kelola harus bersifat dinamis; setiap kali satu atau lebih *Design Factors* berubah (mis. perubahan strategi, regulasi baru, pergeseran ke Cloud/DevOps), dampak terhadap sistem tata kelola harus dipertimbangkan.
4. **Governance Distinct from Management (Tata Kelola Terpisah dari Manajemen):** Sistem tata kelola harus membedakan dengan jelas antara aktivitas dan struktur tata kelola (`EDM`) dengan manajemen (`APO`, `BAI`, `DSS`, `MEA`).
5. **Tailored to Enterprise Needs (Disesuaikan dengan Kebutuhan Perusahaan):** Sistem tata kelola harus dirancang sesuai konteks spesifik perusahaan menggunakan serangkaian **11 Design Factors** sebagai parameter penyesuaian dan prioritisasi.
6. **End-to-End Governance System (Sistem Tata Kelola Ujung-ke-Ujung):** Sistem tata kelola harus mencakup perusahaan secara menyeluruh (*end-to-end*), tidak hanya berfokus pada departemen TI, melainkan seluruh informasi dan pemrosesan teknologi yang digunakan di unit bisnis mana pun (termasuk *Shadow IT* dan *Cloud/SaaS* pihak ketiga).

### B. 3 Prinsip Kerangka Kerja Tata Kelola (*3 Principles for a Governance Framework*)
1. **Based on a Conceptual Model (Berbasis Model Konseptual):** Mengidentifikasi komponen utama dan hubungan antar-komponen untuk memaksimalkan konsistensi dan memungkinkan otomatisasi.
2. **Open and Flexible (Terbuka dan Fleksibel):** Mengizinkan penambahan konten baru dan mampu mengakomodasi isu-isu baru (melalui *Focus Areas* seperti Cybersecurity, DevOps, Cloud, SME, Privacy) dengan tetap menjaga integritas dan konsistensi model inti.
3. **Aligned to Major Standards (Selaras dengan Standar Utama):** Selaras dengan standar, kerangka kerja, dan regulasi global yang relevan (ISO/IEC, NIST, ITIL, TOGAF, PMBOK, CIS, CMMI, COSO, King IV) tanpa menyalin atau bertentangan dengannya.

---

## 4. Evolusi Utama: Perbedaan COBIT 5 vs. COBIT 2019

| Aspek Perubahan | COBIT 5 (2012) | COBIT 2019 | Dampak bagi Auditor & Praktisi TI |
| :--- | :--- | :--- | :--- |
| **Jumlah Proses / Objektif** | 37 Proses | **40 Governance & Management Objectives** | Penambahan 3 objektif baru (`APO14 Managed Data`, `BAI11 Managed Projects`, `MEA04 Managed Assurance`) dan penggabungan/pemisahan proses. |
| **Komponen / Enablers** | 7 Enablers | **7 Components of a Governance System** | Terminologi diselaraskan; seluruh 7 komponen (A–G) kini dirinci langsung di dalam setiap bab dari 40 Objektif. |
| **Goals Cascade** | 17 Enterprise Goals $\rightarrow$ 17 IT-related Goals | **13 Enterprise Goals $\rightarrow$ 13 Alignment Goals** | Disederhanakan, dikonsolidasikan, dan diganti namanya dari *IT-related Goals* menjadi **Alignment Goals** untuk mencegah kesalahpahaman bahwa tujuan tersebut hanya milik departemen TI. |
| **Penilaian Kapabilitas (*Capability*)** | Berbasis ISO/IEC 15504 (Process Assessment Model / PAM dengan 9 Process Attributes) | **Berbasis CMMI v2.0 (Level 0–5)** di mana setiap *Activity* sudah dipetakan langsung ke Capability Level 2–5 + **Maturity Level (0–5)** untuk *Focus Areas* | Penilaian kapabilitas jauh lebih praktis, objektif, dan langsung berbasis pemenuhan aktivitas proses tanpa harus membedah atribut generik yang rumit. |
| **Tailoring & Desain** | Tidak memiliki panduan kuantitatif penyesuaian | **11 Design Factors** & *COBIT 2019 Design Guide* | Auditor dapat menghitung secara matematis objektif mana yang wajib memiliki target kapabilitas Level 3 atau Level 4 sesuai profil risiko perusahaan. |
| **Perubahan Spesifik Objektif** | • `BAI01 Manage Programs and Projects` (digabung)<br>• `MEA03 Monitor Compliance`<br>• Data tersebar di `APO01`/`APO03`/`BAI02` | • Dipecah menjadi `BAI01 Managed Programs` & **`BAI11 Managed Projects`**<br>• Dipecah menjadi `MEA03` (Kepatuhan Eksternal) & **`MEA04 Managed Assurance`**<br>• **`APO14 Managed Data`** berdiri sendiri | Tata kelola Data (`APO14`), Manajemen Proyek (`BAI11`), dan Asurans Independen (`MEA04`) kini menjadi objektif mandiri dengan praktik dan metrik lengkap. |

---

## 5. Struktur 5 Domain & 40 Objektif Inti (*COBIT Core Model*)

Model Inti COBIT 2019 terdiri atas **40 Governance and Management Objectives**, yang mencakup **231 Practices** dan **1.202 Activities**:

| Area | Domain | Kode Domain | Jumlah Objektif | Jumlah Praktik | Jumlah Aktivitas | Referensi Bab Buku Ini |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Governance** | Evaluate, Direct and Monitor | `EDM` | 5 (`EDM01`–`EDM05`) | 16 | 85 | [Bab 3](03-domain-edm-governance-objectives.md) |
| **Management** | Align, Plan and Organize | `APO` | 14 (`APO01`–`APO14`) | 84 | 428 | [Bab 4](04-domain-apo-management-objectives-part1.md) & [Bab 5](05-domain-apo-management-objectives-part2.md) |
| **Management** | Build, Acquire and Implement | `BAI` | 11 (`BAI01`–`BAI11`) | 74 | 401 | [Bab 6](06-domain-bai-management-objectives.md) |
| **Management** | Deliver, Service and Support | `DSS` | 6 (`DSS01`–`DSS06`) | 37 | 178 | [Bab 7](07-domain-dss-management-objectives.md) |
| **Management** | Monitor, Evaluate and Assess | `MEA` | 4 (`MEA01`–`MEA04`) | 20 | 110 | [Bab 8](08-domain-mea-management-objectives.md) |
| **TOTAL** | **5 Domain** | **EDM–MEA** | **40 Objektif** | **231 Praktik** | **1.202 Aktivitas** | **Bab 3 s.d. Bab 8** |

---

## 6. Tujuh Komponen Sistem Tata Kelola (*7 Components of a Governance System*)

Untuk mencapai suatu objektif tata kelola atau manajemen, organisasi tidak cukup hanya memiliki "dokumen prosedur". COBIT 2019 mewajibkan evaluasi **7 Komponen** secara holistik (Komponen A s.d. G):

| Kode | Nama Komponen Resmi | Deskripsi & Pertanyaan Pengujian Audit TI |
| :---: | :--- | :--- |
| **A** | **Processes (Proses)** | Kumpulan praktik dan aktivitas terstruktur untuk mencapai tujuan tertentu dan menghasilkan serangkaian output yang mendukung pencapaian tujuan terkait TI.<br>*Pertanyaan Audit:* Apakah seluruh praktik (`XX01.01`..`XX01.0n`) dan aktivitas pada level kapabilitas target telah dijalankan secara konsisten dan diukur dengan metrik yang tepat? |
| **B** | **Organizational Structures (Struktur Organisasi)** | Entitas pengambil keputusan utama dalam suatu perusahaan (komite, dewan, dan peran struktural). Mencakup matriks **RACI** (*Responsible, Accountable, Consulted, Informed*) pada 33 peran standar.<br>*Pertanyaan Audit:* Apakah setiap praktik memiliki tepat **satu** peran *Accountable (A)*, tidak ada konflik *Segregation of Duties (SoD)*, dan komite memiliki mandat resmi? |
| **C** | **Information Flows and Items (Aliran dan Item Informasi)** | Mencakup seluruh informasi yang diproduksi (*Outputs*) dan digunakan (*Inputs*) oleh perusahaan, baik yang mengalir antar-proses COBIT maupun dari/ke luar COBIT.<br>*Pertanyaan Audit:* Apakah dokumen/laporan output dari suatu proses (mis. *Risk Treatment Plan* dari `APO13.02`) benar-benar diterima dan digunakan sebagai input oleh proses tujuan? |
| **D** | **People, Skills and Competencies (SDM, Keterampilan dan Kompetensi)** | Diperlukan untuk penyelesaian seluruh aktivitas dengan baik dan untuk membuat keputusan yang tepat serta mengambil tindakan korektif. Dipetakan ke **SFIA V6** (*Skills Framework for the Information Age*) dan **e-CF** (*European e-Competence Framework*).<br>*Pertanyaan Audit:* Apakah personel yang memegang peran `R` dan `A` memiliki sertifikasi, jam pelatihan, dan kompetensi teknis yang dipersyaratkan? |
| **E** | **Policies and Procedures (Kebijakan dan Prosedur)** | Menerjemahkan perilaku yang diinginkan menjadi panduan praktis untuk manajemen sehari-hari.<br>*Pertanyaan Audit:* Apakah kebijakan terkait objektif tersebut telah disahkan, mutakhir (ditinjau $\le 1$ tahun), dikomunikasikan, dan didukung oleh SOP teknis? |
| **F** | **Culture, Ethics and Behavior (Budaya, Etika dan Perilaku)** | Dari individu dan perusahaan; sering kali diremehkan sebagai faktor penentu keberhasilan dalam kegiatan tata kelola dan manajemen.<br>*Pertanyaan Audit:* Apakah *Tone at the Top* mendukung kepatuhan (mis. eksekutif tidak memotong jalur *Change Management* atau mengabaikan protokol keamanan)? |
| **G** | **Services, Infrastructure and Applications (Layanan, Infrastruktur dan Aplikasi)** | Menyediakan kemampuan sistem pemrosesan teknologi dan informasi bagi perusahaan untuk menjalankan tata kelola dan manajemen I&T.<br>*Pertanyaan Audit:* Apakah terdapat *tooling* otomatis yang memadai (mis. SIEM, ITSM, CMDB, GRC tool, PAM) untuk menjalankan dan memantau proses? |

---

## 7. Manajemen Kinerja COBIT (*COBIT Performance Management — CPM*)

COBIT 2019 menggunakan model penilaian yang menggabungkan **CMMI v2.0** dan standar **ISO/IEC 33000 (SPICE)**:

### A. Skala Level Kapabilitas Proses (*Process Capability Levels 0–5*)
Digunakan untuk menilai masing-masing dari **40 Governance & Management Objectives** (Komponen A — Proses):

| Level | Nama Level Kapabilitas | Kriteria Pencapaian & Indikator Bukti Audit |
| :---: | :--- | :--- |
| **Level 0** | **Incomplete (Tidak Lengkap)** | Kurangnya kapabilitas dasar; pendekatan tidak lengkap untuk memenuhi tujuan tata kelola dan manajemen; mungkin ada atau tidak ada niat untuk mencapai tujuan proses. |
| **Level 1** | **Performed (Dilaksanakan)** | Proses kurang lebih mencapai tujuannya melalui penerapan serangkaian aktivitas yang belum lengkap dan bersifat *ad-hoc* / reaktif / bergantung pada heroisme individu, tanpa standarisasi yang kuat. |
| **Level 2** | **Managed (Terkelola)** | Proses mencapai tujuannya melalui penerapan serangkaian aktivitas dasar namun lengkap yang dapat dikarakterisasi sebagai **terkelola (direncanakan, dipantau, dan disesuaikan)**. Seluruh aktivitas berlabel `Capability Level 2` pada panduan COBIT 2019 telah dijalankan. |
| **Level 3** | **Established (Mapan / Terstandarisasi)** | Proses mencapai tujuannya dengan cara yang jauh lebih terorganisasi menggunakan aset organisasi. Proses **didefinisikan secara baku di seluruh organisasi** (kebijakan, SOP, template standar, pelatihan wajib). Seluruh aktivitas berlabel `Capability Level 3` telah dipenuhi. |
| **Level 4** | **Predictable (Terukur / Dapat Diprediksi)** | Proses beroperasi dalam batas-batas yang ditentukan untuk mencapai hasilnya secara konsisten dan **diukur secara kuantitatif** menggunakan metrik statistik/KPI/KGI. Seluruh aktivitas berlabel `Capability Level 4` telah dipenuhi. |
| **Level 5** | **Optimizing (Optimal / Berkelanjutan)** | Proses **ditingkatkan secara terus-menerus (*continual improvement*)** untuk memenuhi tujuan perusahaan saat ini dan masa depan yang relevan, didukung analitik prediktif dan otomatisasi penuh. Seluruh aktivitas berlabel `Capability Level 5` telah dipenuhi. |

### B. Aturan Penilaian *Rating Scale* ISO/IEC 33000 (N / P / L / F) dan Aturan *Hard Gate*
Dalam menguji apakah suatu proses berhak naik dari Level $N$ ke Level $N+1$, auditor menggunakan skala pemenuhan aktivitas berikut:

| Rating | Nama Peringkat | Rentang Skor Pemenuhan | Makna & Keputusan Kenaikan Level (*Gate Rule*) |
| :---: | :--- | :---: | :--- |
| **N** | **Not Achieved** | **0% – 15%** | Tidak ada atau sangat sedikit bukti pencapaian atribut/aktivitas pada level tersebut. **Gagal mencapai level.** |
| **P** | **Partially Achieved** | **>15% – 50%** | Ada beberapa bukti pendekatan dan pencapaian aktivitas, namun beberapa aspek masih tidak terduga dan tidak lengkap. **Gagal mencapai level.** |
| **L** | **Largely Achieved** | **>50% – 85%** | Ada bukti pendekatan sistematis dan pencapaian signifikan atas aktivitas di level tersebut, meskipun masih ada kelemahan minor. Level tersebut dapat diklaim sebagai *Largely Achieved*, namun **TIDAK BOLEH naik ke penilaian level di atasnya** sebelum mencapai **F (>85%)**. |
| **F** | **Fully Achieved** | **>85% – 100%** | Ada bukti pendekatan yang lengkap dan sistematis, serta pencapaian penuh atas seluruh aktivitas pada level tersebut tanpa kelemahan material. **Memenuhi syarat (*Gate Passed*) untuk dinilai pada Level berikutnya ($N+1$).** |

> [!WARNING]
> **Aturan Emas Penilaian Kapabilitas COBIT 2019 (*Strict Hierarchical Gate*):**
> Suatu proses **hanya** dapat diklaim mencapai **Capability Level $k$** secara penuh apabila seluruh aktivitas pada **Level 2 s.d. Level $k$** memperoleh skor **Fully Achieved (>85%)**. Sebagai contoh, jika organisasi sudah memiliki dashboard analitik canggih (aktivitas Level 4 = 90%), tetapi aktivitas dasar pada Level 2 baru tercapai 60% (*Largely Achieved*), maka kapabilitas resmi proses tersebut **tetap tertahan di Level 1 (atau Level 2 *Largely Achieved*)**, bukan Level 4!

### C. Skala Level Maturitas Area Fokus (*Focus Area Maturity Levels 0–5*)
Berbeda dengan *Capability Level* yang menilai satu proses secara tunggal, **Maturity Level (0–5)** digunakan untuk menilai kumpulan objektif dan seluruh 7 komponennya pada suatu **Focus Area** (mis. *Cybersecurity Maturity*, *Data Governance Maturity*, atau keseluruhan *Enterprise Governance Maturity*):
- **Level 0 — Incomplete:** Pekerjaan belum selesai atau tidak konsisten.
- **Level 1 — Initial:** Pekerjaan selesai secara reaktif, namun tujuan penuh dan maksud dari focus area belum tercapai.
- **Level 2 — Managed:** Perencanaan dan pengukuran kinerja telah berjalan, namun belum menggunakan standar seragam di seluruh enterprise.
- **Level 3 — Defined:** Standar di tingkat enterprise telah ditetapkan dan memberikan panduan di seluruh unit organisasi.
- **Level 4 — Quantitative:** Perusahaan digerakkan oleh data (*data-driven*) dengan peningkatan kinerja kuantitatif yang terukur.
- **Level 5 — Optimizing:** Fokus penuh pada perbaikan berkelanjutan (*continuous improvement*) dan adaptasi proaktif.
