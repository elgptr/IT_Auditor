# Bab 1: Standar Profesional ISACA ITAF (4th Edition), Kode Etik, dan Piagam Audit (Audit Charter)

> **Cakupan Materi:** Bab ini mengkodifikasi fondasi profesional seluruh penugasan Audit Sistem Informasi berdasarkan **ISACA Information Technology Assurance Framework (ITAF™) 4th Edition**, **ISACA Code of Professional Ethics**, **CISA Job Practice Areas**, standar internasional (**ISO/IEC 19011**, **ISO/IEC 27007**, **ISO/IEC 27008**), serta arsitektur **Audit Charter** dan **Surat Perikatan (Engagement Letter)**.

---

## 1.1 Struktur Profesi CISA & Pembobotan 5 Domain ISACA

Sertifikasi **Certified Information Systems Auditor (CISA)** yang dikelola oleh ISACA mengukur kompetensi praktisi dalam melakukan audit, kontrol, pemantauan, dan penilaian terhadap sistem informasi dan bisnis organisasi. Kurikulum CISA (Review Manual 27th Edition) terbagi ke dalam **5 Domain Utama** dan **39 Task Statements (`T1`–`T39`)**:

| Domain | Nama Domain | Bobot Ujian | Estimasi Soal (dari 150) | Fokus Utama Audit | Task Statements Terkait |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Domain 1** | **Information Systems Auditing Process** | **21%** | ~32 Soal | Perencanaan audit berbasis risiko, ITAF, bukti audit, *statistical sampling*, CAATs, CSA, pelaporan 5C. | `T1`, `T2`, `T3`, `T4`, `T11`, `T36`, `T37`, `T38` |
| **Domain 2** | **Governance and Management of IT** | **17%** | ~25 Soal | Tata kelola TI (EGIT), komite strategi/steering, kebijakan, SoD 12 peran TI, ERM/ALE, outsourcing & SOC 1/2/3, IT BSC. | `T5`–`T12`, `T15`, `T20`, `T21`, `T25`, `T34`, `T39` |
| **Domain 3** | **IS Acquisition, Development and Implementation** | **12%** | ~18 Soal | Tata kelola proyek (CPM/PERT/EVA), SDLC, RFP, *Software Escrow*, *Application Controls* (ITAC), pengujian (UAT/Regression), migrasi data. | `T14`, `T16`, `T17`, `T18`, `T19`, `T27` |
| **Domain 4** | **IS Operations and Business Resilience** | **23%** | ~35 Soal | Operasional TI, OS/DBMS, ITSM (Incident/Problem/Change/Patch), BIA (`RPO`/`RTO`/`WRT`/`MTD`), RAID, backup, *Recovery Sites*, pengujian DRP. | `T13`, `T20`–`T28`, `T33` |
| **Domain 5** | **Protection of Information Assets** | **27%** | ~40 Soal | Klasifikasi data, keamanan fisik, IAM (RBAC/Biometrik/SSO), keamanan jaringan (Firewall/DMZ/IDS/IPS/VPN), kriptografi/PKI, serangan siber, VA/Pentest, *Digital Forensics*. | `T2`, `T26`, `T29`–`T35`, `T39` |

---

## 1.2 Kode Etik Profesional ISACA (ISACA Code of Professional Ethics)

Seluruh pemegang sertifikasi CISA dan praktisi audit SI wajib mematuhi **7 Butir Kode Etik Profesional ISACA**. Pelanggaran terhadap kode etik ini dapat berujung pada pencabutan sertifikasi (*revocation*):

1. **Mendukung Implementasi dan Kepatuhan Standar:** Mendukung implementasi serta mendorong kepatuhan terhadap standar dan prosedur yang tepat guna pengelolaan dan tata kelola sistem informasi serta teknologi perusahaan yang efektif (*support implementation of, and encourage compliance with, appropriate standards and procedures*).
2. **Melaksanakan Tugas dengan Objektivitas, Due Diligence, dan Professional Care:** Melaksanakan tugas secara objektif, dengan uji tuntas (*due diligence*) dan kehati-hatian profesional (*due professional care*), sesuai dengan standar profesional.
3. **Melayani Kepentingan Pemangku Kepentingan secara Sah (Lawful Manner):** Melayani kepentingan *stakeholders* dengan cara yang sah dan jujur, sambil mempertahankan standar perilaku serta karakter yang tinggi, dan tidak terlibat dalam tindakan yang mendiskreditkan profesi atau asosiasi.
4. **Menjaga Privasi dan Kerahasiaan (Privacy and Confidentiality):** Menjaga privasi dan kerahasiaan informasi yang diperoleh selama menjalankan tugas, **kecuali jika pengungkapan diwajibkan oleh otoritas hukum (legal authority)**. Informasi tersebut tidak boleh digunakan untuk keuntungan pribadi atau diberikan kepada pihak yang tidak berwenang.
5. **Mempertahankan Kompetensi (Maintain Competency):** Mempertahankan kompetensi di bidang sistem informasi, asurans, keamanan, dan tata kelola, serta hanya mengambil pekerjaan yang secara wajar diharapkan dapat diselesaikan dengan kompetensi profesional (*Continuing Professional Education* / CPE minimal **20 jam per tahun** dan **120 jam per periode 3 tahun**).
6. **Mengungkapkan Seluruh Fakta Material (Inform Appropriate Parties):** Menginformasikan kepada pihak yang tepat mengenai hasil pekerjaan yang dilakukan, termasuk mengungkapkan seluruh fakta signifikan/material yang diketahui oleh mereka, yang jika tidak diungkapkan, dapat **mendistorsi pelaporan (distort the reporting)** hasil kegiatan atau menyembunyikan praktik melanggar hukum.
7. **Mendukung Pendidikan Pemangku Kepentingan:** Mendukung pendidikan bagi para pemangku kepentingan untuk meningkatkan pemahaman mereka mengenai tata kelola, keamanan, dan audit sistem informasi.

> [!IMPORTANT]
> **Jebakan Ujian CISA (ISACA Mindset — Etika & Independensi):**
> - Jika auditor menemukan aktivitas ilegal/kecurangan (*fraud*), auditor **TIDAK BOLEH** langsung melapor ke penegak hukum/regulator eksternal terlebih dahulu, melainkan harus melaporkan ke **Komite Audit (Audit Committee)** atau manajemen puncak internal (kecuali manajemen puncak terlibat, maka ke Komite Audit/Dewan Komisaris).
> - Jika klien di negara lain memberikan hadiah mahal yang dianggap wajar secara budaya lokal, auditor tetap harus menolak hadiah tersebut jika berpotensi mengganggu **independensi dalam penampilan (*independence in appearance*)**.

---

## 1.3 Arsitektur Lengkap ISACA ITAF™ 4th Edition

**ITAF (Information Technology Assurance Framework)** edisi ke-4 menetapkan kerangka kerja tunggal yang mengikat praktisi audit SI melalui 3 kategori:
1. **ITAF Standards (Mandatory / Wajib):** Terdiri dari **17 Standar** yang terbagi menjadi *General Standards* (`1000 Series`), *Performance Standards* (`1200 Series`), dan *Reporting Standards* (`1400 Series`). Apabila auditor mengklaim audit dilakukan sesuai standar ISACA, kepatuhan terhadap seluruh *Standards* bersifat mutlak.
2. **ITAF Guidelines (Pedoman Penerapan):** Terdiri dari **17 Pedoman** (`2000`, `2200`, `2400 Series`) yang berpasangan 1-ke-1 dengan setiap *Standard*. Menjelaskan *bagaimana* menerapkan standar dan kapan *professional judgment* atau pengecualian yang dapat dibenarkan (*justifiable departure*) dapat diambil.
3. **ITAF Tools and Techniques (Alat & Teknik):** Contoh program kerja audit, buku putih (*whitepapers*), kuesioner kontrol, dan *audit programs* spesifik teknologi.

### A. General Standards (Seri 1000) & Guidelines (Seri 2000) — Prinsip Pemandu

| Kode Standar | Kode Pedoman | Judul Standar | Pernyataan Wajib & Ketentuan Kunci ITAF 4th Edition |
| :---: | :---: | :--- | :--- |
| **`1001`** | **`2001`** | **Audit Charter** *(Piagam Audit)* | • Fungsi audit SI harus mendokumentasikan fungsi audit secara tepat dalam **Audit Charter** yang mengukuhkan tujuan (*purpose*), tanggung jawab (*responsibility*), wewenang (*authority*), dan akuntabilitas (*accountability*).<br>• **Wajib disetujui** oleh tingkat tertinggi organisasi (**Board of Directors / Dewan Komisaris / Audit Committee**).<br>• Ditinjau secara berkala (minimal tahunan) untuk memastikan relevansi. |
| **`1002`** | **`2002`** | **Organizational Independence** *(Independensi Organisasional)* | • Fungsi audit SI harus independen dari area atau aktivitas yang sedang ditinjau untuk memungkinkan penyelesaian penugasan audit secara objektif.<br>• Secara struktural, Chief Audit Executive (CAE) harus memiliki jalur pelaporan fungsional langsung ke **Audit Committee** dan jalur administratif ke CEO. |
| **`1003`** | **`2003`** | **Auditor Objectivity** *(Objektivitas Auditor)* | • Praktisi audit SI harus bersikap objektif (*attitude of mind*) dalam seluruh hal yang berkaitan dengan penugasan audit.<br>• Konflik kepentingan (*conflict of interest* — aktual maupun potensial), misalnya mengaudit sistem yang pernah dirancang/diimplementasikan sendiri oleh auditor dalam 12 bulan terakhir, **wajib diungkapkan** dan auditor harus dialihkan dari area tersebut.<br>• Auditor **boleh** memberikan saran kontrol pada tahap desain SDLC (*pre-implementation review*), tetapi **tidak boleh** mengambil keputusan manajemen atau menjadi pemilik kontrol. |
| **`1004`** | **`2004`** | **Reasonable Expectation** *(Ekspektasi yang Wajar)* | • Praktisi audit SI harus memiliki ekspektasi yang wajar bahwa: (1) Penugasan dapat diselesaikan sesuai dengan standar audit SI; (2) Ruang lingkup (*scope*) tidak dibatasi hingga menghalangi penarikan kesimpulan; dan (3) Manajemen memahami kewajiban dan tanggung jawabnya untuk menyediakan akses penuh terhadap informasi, sistem, dan personel. |
| **`1005`** | **`2005`** | **Due Professional Care** *(Kehati-hatian Profesional)* | • Praktisi audit SI harus menerapkan *due professional care*, termasuk mematuhi standar audit profesional yang berlaku dalam perencanaan, pelaksanaan, dan pelaporan hasil.<br>• Mencakup sikap **skeptisisme profesional (*professional skepticism*)**, tidak menerima klaim lisan tanpa bukti koroboratif, namun tidak menuntut kesempurnaan mutlak (*infallibility*). |
| **`1006`** | **`2006`** | **Proficiency** *(Kecakapan / Kompetensi)* | • Praktisi audit SI secara kolektif beserta tim penugasannya harus memiliki kompetensi, keterampilan, dan pengetahuan yang memadai untuk melaksanakan penugasan, serta terus memelihara kompetensi melalui pendidikan berkelanjutan (CPE). |
| **`1007`** | **`2007`** | **Assertions** *(Asersi Manajemen)* | • Praktisi audit SI harus meninjau asersi (*assertions*) yang menjadi dasar penilaian pokok bahasan (*subject matter*) untuk menentukan bahwa asersi tersebut **dapat diaudit (*capable of being audited*)** serta memadai, valid, dan relevan. |
| **`1008`** | **`2008`** | **Criteria** *(Kriteria Evaluasi)* | • Praktisi audit SI harus memilih kriteria evaluasi terhadap *subject matter* yang **objektif, lengkap (*complete*), relevan, dapat diukur (*measurable*), dapat dipahami (*understandable*), diakui secara luas (*widely recognized*), dan otoritatif** (misal: COBIT 2019, ISO/IEC 27001, NIST SP 800-53, CIS Benchmarks, regulasi OJK/BI). |

### B. Performance Standards (Seri 1200) & Guidelines (Seri 2200) — Pelaksanaan Penugasan

| Kode Standar | Kode Pedoman | Judul Standar | Pernyataan Wajib & Ketentuan Kunci ITAF 4th Edition |
| :---: | :---: | :--- | :--- |
| **`1201`** | **`2201`** | **Risk Assessment in Planning** *(Penilaian Risiko dalam Perencanaan)* | • Fungsi audit SI harus menggunakan pendekatan penilaian risiko (*risk-based audit approach*) dan metodologi pendukung untuk mengembangkan rencana audit SI secara keseluruhan (*annual audit plan*) dan menentukan prioritas alokasi sumber daya audit yang terbatas.<br>• Rencana audit tahunan harus ditinjau minimal sekali setahun. |
| **`1202`** | **`2202`** | **Audit Scheduling** *(Penjadwalan Audit)* | • Praktisi audit SI harus merencanakan dan menjadwalkan setiap penugasan untuk memastikan ketersediaan sumber daya yang tepat pada waktu yang tepat serta koordinasi dengan *auditee*. |
| **`1203`** | **`2203`** | **Engagement Planning** *(Perencanaan Penugasan)* | • Untuk setiap penugasan spesifik, praktisi harus menyusun dan mendokumentasikan rencana penugasan (*audit program*) yang merinci: tujuan (*objectives*), ruang lingkup (*scope*), alokasi waktu (*timing*), kebutuhan sumber daya, kriteria, serta sifat dan luas prosedur pengujian berdasarkan profil risiko objek audit. |
| **`1204`** | **`2204`** | **Performance and Supervision** *(Pelaksanaan dan Supervisi)* | • Staf audit SI harus disupervisi secara memadai untuk memberikan asurans yang wajar (*reasonable assurance*) bahwa tujuan audit tercapai dan standar audit profesional dipenuhi.<br>• Seluruh kertas kerja (*Audit Working Papers* / KKA) wajib di-review dan diparaf oleh auditor senior/manajer audit. |
| **`1205`** | **`2205`** | **Evidence** *(Bukti Audit)* | • Praktisi audit SI harus memperoleh **bukti yang cukup dan tepat (*sufficient and appropriate audit evidence*)** untuk menarik kesimpulan yang wajar sebagai dasar hasil penugasan.<br>• **Sufficient (Cukup):** Ukuran kuantitas bukti (terkait ukuran sampel & risiko).<br>• **Appropriate (Tepat):** Ukuran kualitas bukti, yang ditentukan oleh **Relevansi (*Relevance*)** dan **Keandalan (*Reliability*)**. |
| **`1206`** | **`2206`** | **Using the Work of Other Experts** *(Menggunakan Pekerjaan Pakar Lain)* | • Ketika menggunakan pekerjaan pakar lain (misal: *penetration tester* eksternal, aktuaris, spesialis forensik, atau auditor internal lain), praktisi audit SI harus: (1) Menilai kompetensi, kapabilitas, independensi, dan objektivitas pakar; (2) Meninjau cakupan dan metodologi pekerjaan pakar; dan (3) **Tetap memikul tanggung jawab penuh (*ultimate responsibility*)** atas opini/kesimpulan audit akhir. |
| **`1207`** | **`2207`** | **Irregularities and Illegal Acts** *(Ketidakberesan & Tindakan Ilegal)* | • Praktisi harus menerapkan *professional skepticism* dan mempertimbangkan risiko adanya ketidakberesan (*irregularities/fraud*) dan tindakan ilegal selama perikatan.<br>• Jika ditemukan indikasi *fraud*/tindakan ilegal, auditor wajib mendokumentasikan dan mengomunikasikannya secara tepat waktu kepada manajemen yang tepat dan/atau **Audit Committee** (tidak mengonfrontasi pelaku secara langsung). |

### C. Reporting Standards (Seri 1400) & Guidelines (Seri 2400) — Pelaporan & Tindak Lanjut

| Kode Standar | Kode Pedoman | Judul Standar | Pernyataan Wajib & Ketentuan Kunci ITAF 4th Edition |
| :---: | :---: | :--- | :--- |
| **`1401`** | **`2401`** | **Reporting** *(Pelaporan Hasil Audit)* | • Praktisi audit SI harus menyediakan laporan tertulis dalam bentuk yang tepat setelah penyelesaian penugasan.<br>• Laporan harus mencakup: organisasi yang diaudit, penerima laporan, cakupan, tujuan, periode cakupan, sifat/luas pekerjaan, keterbatasan ruang lingkup (*scope limitations*), temuan (*findings*), kesimpulan/opini, rekomendasi, serta **tanggapan dan rencana aksi manajemen (*management response & action plan*)** beserta *Action Owner* dan *Target Date*. |
| **`1402`** | **`2402`** | **Follow-up Activities** *(Aktivitas Tindak Lanjut)* | • Praktisi audit SI harus memantau informasi yang relevan untuk menyimpulkan apakah manajemen telah merencanakan dan mengambil tindakan korektif yang efektif dan tepat waktu untuk mengatasi temuan dan rekomendasi audit sebelumnya, atau apakah manajemen senior telah menerima risiko untuk tidak mengambil tindakan (*risk acceptance*). |

---

## 1.4 Perbandingan Audit Charter vs. Engagement Letter

Salah satu topik ujian CISA yang paling sering diujikan adalah membedakan antara **Audit Charter (Piagam Audit)** dan **Engagement Letter (Surat Perikatan / Surat Tugas)**:

| Dimensi Perbandingan | Audit Charter (Piagam Audit — ITAF `1001`) | Engagement Letter (Surat Perikatan — ITAF `1203`) |
| :--- | :--- | :--- |
| **Cakupan & Sifat** | Dokumen **strategis tingkat tinggi (*overarching document*)** yang mendefinisikan mandat seluruh departemen/fungsi Audit Internal SI secara menyeluruh dan jangka panjang. | Dokumen **taktis/operasional** yang mendefinisikan **satu penugasan/proyek audit spesifik** (*individual audit assignment*). |
| **Isi Utama** | Tujuan (*purpose*), Wewenang (*authority* — hak akses ke seluruh catatan, sistem, dan staf), Tanggung Jawab (*responsibility*), dan Akuntabilitas (*accountability*) fungsi audit. | Ruang lingkup spesifik (*specific scope*), tujuan proyek audit, jadwal (*timeline*), *deliverables*, metodologi, dan batas tanggung jawab tim untuk proyek tersebut. |
| **Pihak yang Menyetujui** | Disetujui oleh **Board of Directors / Audit Committee** dan Manajemen Puncak (CEO). | Disepakati antara **CAE / Pimpinan Audit** (atau Partner KAP Eksternal) dengan **Manajemen Auditee / Klien**. |
| **Siklus Pembaruan** | Ditinjau secara tahunan; jarang berubah kecuali ada restrukturisasi tata kelola. | Dibuat baru untuk **setiap penugasan audit** sebelum *fieldwork* dimulai. |

---

## 1.5 Tiga Jenis Layanan Asurans (Types of Assurance Engagements)

Menurut ITAF 4th Edition, penugasan asurans diklasifikasikan berdasarkan bagaimana informasi atas pokok bahasan (*subject matter*) disajikan:

1. **Attestation Engagement (Penugasan Atestasi):**
   - Manajemen (*Responsible Party*) mengevaluasi *subject matter* terhadap kriteria dan menyusun pernyataan tertulis (**Written Assertion** — misal: *"Manajemen menyatakan bahwa kontrol internal atas pelaporan keuangan efektif per 31 Desember"*).
   - Praktisi audit memeriksa asersi tertulis manajemen tersebut dan memberikan opini atas kewajaran asersi tersebut (contoh: **SOC 1 / SSAE 18**, **SOX Section 404 Attestation**).
2. **Direct Engagement (Penugasan Langsung):**
   - Manajemen **tidak** membuat asersi tertulis formal atas efektivitas kontrol.
   - Praktisi audit SI secara langsung mengukur dan mengevaluasi *subject matter* (sistem, proses, konfigurasi keamanan) terhadap kriteria standar, lalu melaporkan kesimpulan langsung dalam Laporan Hasil Audit (umumnya terjadi pada **Internal IS Audit**).
3. **Levels of Assurance (Tingkat Keyakinan):**
   - **Reasonable Assurance (Keyakinan Memadai / Tinggi):** Bukti dikumpulkan secara ekstensif melalui inspeksi, observasi, *re-performance*, dan CAATs. Opini dinyatakan secara **positif** (*"Menurut opini kami, kontrol beroperasi secara efektif..."*).
   - **Limited Assurance (Keyakinan Terbatas / Review):** Bukti dikumpulkan terutama melalui *inquiry* dan prosedur analitis. Opini dinyatakan secara **negatif (*negative assurance*)** (*"Tidak ada hal yang menjadi perhatian kami yang menyebabkan kami percaya bahwa kontrol tidak efektif..."*).
   - **No Assurance (Advisory / Consulting / Agreed-Upon Procedures):** Auditor hanya melaporkan temuan faktual atas prosedur yang disepakati tanpa memberikan opini asurans.

---

## 1.6 Keselarasan dengan Standar Internasional (ISO 19011, ISO/IEC 27007, ISO/IEC 27008)

Dalam materi CISA (Handout *IT Audit Playbook*), standar ITAF diselaraskan dengan tiga standar ISO utama untuk audit sistem manajemen dan keamanan informasi:

```
+-----------------------------------------------------------------------------------+
|                      KERANGKA STANDAR AUDIT INTERNASIONAL                         |
+-----------------------------------------------------------------------------------+
|  1. ISACA ITAF 4th Edition                                                        |
|     -> Standar wajib profesi CISA (1000 General, 1200 Performance, 1400 Report)   |
|                                                                                   |
|  2. ISO 19011:2018 (Guidelines for Auditing Management Systems)                   |
|     -> 7 Prinsip Audit: Integrity, Fair Presentation, Due Professional Care,      |
|        Confidentiality, Independence, Evidence-Based Approach, Risk-Based Approach|
|     -> Mengatur pengelolaan Program Audit (PDCA) & evaluasi kompetensi auditor.   |
|                                                                                   |
|  3. ISO/IEC 27007 (Guidelines for Information Security Management Systems Audit)  |
|     -> Pedoman spesifik untuk mengaudit proses manajemen ISMS (ISO/IEC 27001)     |
|        mulai dari konteks organisasi, kepemimpinan, penilaian risiko, hingga SOA. |
|                                                                                   |
|  4. ISO/IEC TS 27008 (Guidelines for the Assessment of Information Security       |
|     Controls)                                                                     |
|     -> Pedoman teknis untuk menguji dan memverifikasi implementasi kontrol        |
|        keamanan informasi (ISO/IEC 27002) secara langsung pada aset TI.           |
+-----------------------------------------------------------------------------------+
```

### Tujuh Prinsip Audit (ISO 19011 & ITAF)
1. **Integritas (*Integrity*):** Dasar profesionalisme; bekerja dengan jujur, tekun, dan bertanggung jawab.
2. **Penyajian yang Wajar (*Fair Presentation*):** Kewajiban untuk melaporkan secara jujur dan akurat, termasuk hambatan signifikan dan perbedaan pendapat yang belum terselesaikan antara tim audit dan *auditee*.
3. **Kecermatan Profesional (*Due Professional Care*):** Penerapan ketekunan dan pertimbangan (*judgment*) dalam mengaudit.
4. **Kerahasiaan (*Confidentiality*):** Keamanan informasi; perlindungan atas informasi sensitif yang diakses selama audit.
5. **Independensi (*Independence*):** Dasar ketidakberpihakan audit dan objektivitas kesimpulan audit.
6. **Pendekatan Berbasis Bukti (*Evidence-Based Approach*):** Metode rasional untuk mencapai kesimpulan audit yang andal dan dapat direproduksi (*reproducible*) dalam proses audit yang sistematis.
7. **Pendekatan Berbasis Risiko (*Risk-Based Approach*):** Pendekatan audit yang secara substansial mempertimbangkan risiko dan peluang dalam perencanaan, pelaksanaan, dan pelaporan.

---

## 1.7 Kompetensi Auditor TI & Model Kematangan Fungsi Audit SI

Berdasarkan studi empiris *Kompetensi Teknologi Informasi terhadap Kualitas Hasil Audit* (`d1x2_kompetensi.txt` & `audit_playbook.txt`), kualitas hasil audit SI ditentukan oleh tiga pilar kompetensi yang harus dimiliki oleh tim audit secara kolektif (ITAF `1006`):

1. **Pengetahuan Akuntansi, Bisnis, dan Regulasi (*Business & Regulatory Knowledge*):** Memahami proses bisnis inti (misal: *Order-to-Cash*, *Procure-to-Pay*, *Record-to-Report*, *Core Banking*), risiko salah saji laporan keuangan (SOX), serta regulasi sektoral.
2. **Kompetensi Teknis Sistem Informasi (*Technical IT Competency*):** Pemahaman arsitektur OS (Unix/Linux/Windows), DBMS (Oracle/SQL Server), jaringan (Firewall/VLAN/DMZ), pengembangan aplikasi (SDLC/Agile/DevSecOps), dan penguasaan alat bantu audit berbantuan komputer (**CAATs / GAS**).
3. **Keterampilan Perilaku & Komunikasi (*Soft Skills & Communication*):** Kemampuan melakukan wawancara investigatif (*walkthrough inquiry*), negosiasi temuan pada *Exit Meeting*, serta penulisan laporan 5C yang persuasif bagi manajemen eksekutif.
