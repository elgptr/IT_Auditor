# Bab 2: Regulasi Tata Kelola TI BUMN — Permen BUMN No. PER-2/MBU/03/2023 & Pedoman Asesmen Maturity Level COBIT 2019 BUMN

> **Cakupan Materi:** Bab ini mengkodifikasi aturan tata kelola teknologi informasi, digitalisasi, keamanan siber, dan penilaian tingkat kematangan (*IT Maturity Assessment*) pada Badan Usaha Milik Negara (BUMN) dan Anak Perusahaan BUMN berdasarkan **Peraturan Menteri BUMN Nomor PER-2/MBU/03/2023** tentang *Pedoman Tata Kelola dan Kegiatan Korporasi Signifikan BUMN*.

---

## 2.1 Mandat Utama Penyelenggaraan TI dalam Permen BUMN No. PER-2/MBU/03/2023

Sebagai regulasi *Omnibus* Kementerian BUMN, **PER-2/MBU/03/2023** mewajibkan Direksi dan Dewan Komisaris/Dewan Pengawas BUMN untuk menyelenggarakan Tata Kelola TI (*Enterprise Governance of IT*) yang terukur, terstandar, dan menghasilkan nilai tambah (*value creation*):

| Pilar Tata Kelola TI BUMN | Kewajiban Regulasi PER-2/MBU/03/2023 | Pemetaan Objektif COBIT 2019 & Kontrol CISA |
| :--- | :--- | :--- |
| **1. Perencanaan Strategis TI (IT Master Plan / RSTI)** | • Direksi wajib menyusun **Rencana Strategis TI (RSTI / IT Master Plan)** berjangka waktu 3–5 tahun yang diturunkan langsung dari **Rencana Jangka Panjang Perusahaan (RJPP)** dan dijabarkan setiap tahun ke dalam **RKAP (Rencana Kerja dan Anggaran Perusahaan)**.<br>• RSTI wajib memuat: evaluasi kondisi TI saat ini (*as-is*), arsitektur target (*to-be*), portofolio inisiatif proyek digital, rencana investasi/CAPEX-OPEX, dan manajemen risiko TI. | • **COBIT 2019:** `EDM01`, `EDM02`, `APO02`, `APO03`, `APO05`, `APO06`<br>• **CISA:** Domain 2 (`T5`, `T9`) |
| **2. Struktur Tata Kelola & IT Steering Committee** | • Pembentukan **Komite Pengarah TI (*IT Steering Committee*)** lintas direktorat untuk memastikan keselarasan investasi TI dengan bisnis, menghindari duplikasi aplikasi antar divisi/anak perusahaan (*silo*), dan memantau realisasi manfaat (*benefits realization*) proyek strategis TI. | • **COBIT 2019:** `EDM01.02`, `APO01.02`, `BAI01`<br>• **CISA:** Domain 2 (`T6`) |
| **3. Enterprise Architecture & Sinergi Grup BUMN** | • Penerapan **Enterprise Architecture (EA)** yang terintegrasi (Bisnis, Data, Aplikasi, Teknologi) serta mendukung **interoperabilitas dan sinergi antar-BUMN / Holding BUMN** (misal: *Shared Services*, integrasi ERP, dan *Satu Data BUMN*). | • **COBIT 2019:** `APO03`, `APO14`, `BAI03` |
| **4. Tata Kelola Data (Data Governance) & Kedaulatan Data** | • Penetapan kebijakan *Master Data Management (MDM)*, kualitas data, klasifikasi data, pelindungan data pribadi (**UU PDP No. 27/2022**), serta kewajiban penempatan pusat data kritis di wilayah hukum Indonesia. | • **COBIT 2019:** `APO14` (*Managed Data*)<br>• **CISA:** Domain 5 |
| **5. Ketahanan & Keamanan Siber (CSIRT BUMN)** | • BUMN wajib menerapkan Sistem Manajemen Keamanan Informasi (**ISO/IEC 27001**), membentuk tim **CSIRT (*Computer Security Incident Response Team*)** yang terdaftar di **BSSN**, melaksanakan *Vulnerability Assessment & Penetration Testing* berkala, serta memelihara **BCP/DRP** yang diuji setiap tahun. | • **COBIT 2019:** `EDM03`, `APO12`, `APO13`, `DSS02`, `DSS04`, `DSS05`<br>• **CISA:** Domain 4 & 5 |
| **6. Pengadaan Barang/Jasa TI & Manajemen Vendor** | • Pengadaan solusi TI wajib didasarkan pada *Business Case*, *Total Cost of Ownership (TCO)*, analisis *Buy vs. Build*, perjanjian tingkat layanan (**SLA**) dengan klausul denda/penalti, **Hak Audit (*Right to Audit*)**, dan *Software Escrow* / kepemilikan *source code* untuk aplikasi inti. | • **COBIT 2019:** `APO09`, `APO10`, `BAI02`, `BAI03`<br>• **CISA:** Domain 2 & 3 (`T14`, `T15`) |
| **7. Asesmen Berkala Tingkat Kematangan TI (*IT Maturity Assessment*) & Audit TI** | • BUMN wajib melaksanakan penilaian tingkat kematangan tata kelola TI (**IT Maturity Assessment berbasis COBIT 2019**) dan audit TI independen secara berkala, serta melaporkan hasilnya kepada Pemegang Saham / Kementerian BUMN. | • **COBIT 2019:** `MEA01`, `MEA02`, `MEA03`, `MEA04`<br>• **CISA:** Domain 1 |

---

## 2.2 Metodologi Asesmen *IT Maturity Level* BUMN Berbasis COBIT 2019

Dalam pelaksanaan asesmen tata kelola TI di lingkungan BUMN (dan anak perusahaan BUMN), penilaian menggunakan **Model Kapabilitas & Maturitas COBIT 2019 (Skala 0 s.d. 5)** dengan ketentuan teknis berikut:

### A. Ruang Lingkup Objektif Prioritas Standar Asesmen BUMN
Asesmen BUMN umumnya mengevaluasi pemilihan objektif prioritas yang ditentukan melalui **11 Design Factors (`DF1`–`DF11`)** atau mencakup **Core BUMN Objectives** berikut:
1. **Domain EDM (Governance):** `EDM01` (Governance Framework), `EDM02` (Benefits Delivery), `EDM03` (Risk Optimization), `EDM04` (Resource Optimization), `EDM05` (Stakeholder Engagement).
2. **Domain APO (Planning & Risk):** `APO01` (Management Framework), `APO02` (Strategy), `APO03` (Enterprise Architecture), `APO05` (Portfolio), `APO06` (Budget & Costs), `APO07` (HR), `APO09` (SLA), `APO10` (Vendors), `APO11` (Quality), `APO12` (Risk), `APO13` (Security), `APO14` (Data Governance).
3. **Domain BAI (Build & Acquire):** `BAI01` (Programs), `BAI02` (Requirements), `BAI03` (Solutions Build), `BAI04` (Availability & Capacity), `BAI06` (IT Changes), `BAI07` (Change Acceptance), `BAI09` (Assets), `BAI10` (Configuration), `BAI11` (Projects).
4. **Domain DSS (Operations & Resilience):** `DSS01` (Operations), `DSS02` (Requests & Incidents), `DSS03` (Problems), `DSS04` (Continuity / BCP-DRP), `DSS05` (Security Services), `DSS06` (Business Process Controls).
5. **Domain MEA (Monitoring & Assurance):** `MEA01` (Performance & Conformance), `MEA02` (Internal Control), `MEA03` (External Compliance), `MEA04` (Assurance).

### B. Target Baseline & Aturan Perhitungan Skor Kematangan BUMN
- **Target Baseline Kematangan TI BUMN:** Minimal mencapai **Capability / Maturity Level 3.00 (*Defined*)** untuk seluruh objektif inti (dan **Level 4.00 (*Managed*)** untuk BUMN sektor keuangan/perbankan, telekomunikasi, dan energi strategis).
- **Aturan Penilaian Bukti (Design vs. Implementation):**
  - Suatu aktivitas COBIT 2019 tidak boleh dinilai **Fully Achieved (`F` > 85%)** hanya karena memiliki dokumen Kebijakan/SOP (*Component E*), melainkan wajib dibuktikan dengan **artefak pelaksanaan nyata (*evidence of execution* — Component A & C)** minimal selama periode berjalan.
  - Perhitungan otomatis level kapabilitas per objektif menggunakan aturan *Hard Gate* **ISO/IEC 33000 (`F` > 85%)** dapat dieksekusi langsung menggunakan perintah `python cobit_cli.py capability`.
