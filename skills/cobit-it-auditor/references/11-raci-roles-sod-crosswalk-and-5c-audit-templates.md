# Bab 11: Direktori 33 Peran RACI, Deteksi Konflik SoD, Multi-Framework Crosswalk (ISO/NIST/UU PDP/POJK/SPBE), dan Template Audit 5C & LHA

> **Sumber Otoritatif:** *COBIT® 2019 Framework: Governance and Management Objectives (Appendix B — Figure A.3 & Appendix C)*, *COBIT 2019 RACI by Role Matrix (April 2020)*, serta standar audit TI ISACA dan regulasi nasional Indonesia.

---

## 1. Direktori Lengkap 33 Peran & Struktur Organisasi Resmi (Figure A.3) Beserta Beban RACI

Tabel berikut merangkum seluruh **33 peran dan struktur organisasi resmi COBIT 2019** beserta deskripsi mandatnya dan daftar seluruh praktik di mana peran tersebut memegang akuntabilitas tunggal (**Accountable — A**) maupun tanggung jawab operasional (**Responsible — R**):

| No. | Peran / Struktur Organisasi | Deskripsi Mandat Resmi (Figure A.3) | Praktik Accountable (`A`) | Jumlah `R` & Domain Utama |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **Board** | Group of the most senior executives and/or nonexecutive directors accountable for governance and overall control of enterprise resources | **16 praktik:** `EDM01.01`, `EDM01.02`, `EDM01.03`, `EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM03.01`, `EDM03.02`, `EDM03.03`, `EDM04.01`, `EDM04.02` *(+4 lainnya)* | *0 praktik* |
| 2 | **Executive Committee** | Group of senior executives appointed by the board to ensure that the board is involved in, and kept informed of, major decisions (accountable for managing portfolios of I&T-enabled investments, I&T services and I&T assets) | **26 praktik:** `APO01.01`, `APO01.02`, `APO01.03`, `APO01.04`, `APO01.05`, `APO01.06`, `APO01.07`, `APO01.08`, `APO01.09`, `APO01.10`, `APO01.11`, `APO04.01` *(+14 lainnya)* | **22 praktik** (`EDM01.01`, `EDM01.02`, `EDM01.03`, `EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM03.01`, ...) |
| 3 | **Chief Executive Officer** | Highest-ranking officer charged with the total management of the enterprise | **4 praktik:** `BAI01.01`, `BAI05.01`, `BAI11.01`, `MEA01.01` | **20 praktik** (`EDM01.01`, `EDM01.03`, `EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM03.01`, `EDM03.02`, ...) |
| 4 | **Chief Financial Officer** | Most senior official accountable for all aspects of financial management, including financial risk and controls and reliable and accurate accounts | **1 praktik:** `APO06.01` | **18 praktik** (`EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `APO05.01`, `APO05.02`, `APO05.05`, `APO06.02`, ...) |
| 5 | **Chief Operating Officer** | Most senior official accountable for operation of the enterprise | **5 praktik:** `APO07.05`, `APO11.01`, `DSS04.01`, `DSS04.02`, `DSS04.05` | **28 praktik** (`EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM04.01`, `EDM04.02`, `EDM04.03`, `APO03.04`, ...) |
| 6 | **Chief Risk Officer** | Most senior official accountable for all aspects of risk management across the enterprise (an I&T risk officer function may be established to oversee I&T-related risk) | **5 praktik:** `APO12.01`, `APO12.02`, `APO12.03`, `APO12.04`, `APO12.05` | **33 praktik** (`EDM03.01`, `EDM03.02`, `EDM03.03`, `EDM05.01`, `EDM05.02`, `EDM05.03`, `APO01.02`, `APO01.03`, ...) |
| 7 | **Chief Information Officer** | Most senior official responsible for aligning IT and business strategies and accountable for planning, resourcing and managing delivery of I&T services and solutions | **65 praktik:** `APO02.01`, `APO02.02`, `APO06.02`, `APO06.03`, `APO06.04`, `APO06.05`, `APO07.01`, `APO07.02`, `APO07.03`, `APO07.04`, `APO07.06`, `APO08.01` *(+53 lainnya)* | **113 praktik** (`EDM01.01`, `EDM01.03`, `EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM03.01`, `EDM03.02`, ...) |
| 8 | **Chief Technology Officer** | Most senior official tasked with technical aspects of I&T, including managing and monitoring decisions related to I&T services, solutions and infrastructures | **30 praktik:** `APO09.01`, `APO09.02`, `APO09.03`, `APO09.04`, `BAI04.01`, `BAI04.03`, `BAI04.05`, `BAI09.01`, `BAI09.02`, `BAI09.03`, `BAI10.01`, `BAI10.02` *(+18 lainnya)* | **97 praktik** (`APO01.01`, `APO01.02`, `APO01.03`, `APO01.04`, `APO01.05`, `APO01.06`, `APO01.07`, `APO01.08`, ...) |
| 9 | **Chief Digital Officer** | Most senior official tasked with putting into practice the digital ambition of the enterprise or business unit | **1 praktik:** `APO02.03` | **74 praktik** (`APO01.01`, `APO01.02`, `APO01.03`, `APO01.04`, `APO01.05`, `APO01.06`, `APO01.07`, `APO01.08`, ...) |
| 10 | **I&T Governance Board** | Group of stakeholders and experts accountable for guiding I&T-related matters and decisions, including managing I&T-enabled investments, delivering value and monitoring risk | **16 praktik:** `APO02.04`, `APO02.05`, `APO02.06`, `APO05.01`, `APO05.02`, `APO05.03`, `APO05.04`, `APO05.05`, `APO10.01`, `APO10.02`, `APO10.03`, `APO10.04` *(+4 lainnya)* | **38 praktik** (`EDM01.01`, `EDM01.02`, `EDM01.03`, `EDM02.01`, `EDM02.02`, `EDM02.03`, `EDM02.04`, `EDM03.01`, ...) |
| 11 | **Architecture Board** | Group of stakeholders and experts accountable for guiding enterprise architecture-related matters and decisions and for setting architectural policies and standards | **5 praktik:** `APO03.01`, `APO03.02`, `APO03.03`, `APO03.04`, `APO03.05` | **1 praktik** (`APO01.09`) |
| 12 | **Enterprise Risk Committee** | Group of executives accountable for enterprise-level collaboration and consensus required to support enterprise risk management (ERM) activities and decisions | *0 praktik* | **18 praktik** (`EDM03.01`, `EDM03.02`, `EDM03.03`, `APO01.06`, `APO01.07`, `APO01.09`, `APO09.02`, `APO10.04`, ...) |
| 13 | **Chief Information Security Officer** | Most senior official accountable for all aspects of security management across the enterprise | **9 praktik:** `APO13.01`, `APO13.02`, `APO13.03`, `DSS05.01`, `DSS05.02`, `DSS05.03`, `DSS05.04`, `DSS05.05`, `DSS05.07` | **23 praktik** (`EDM03.03`, `APO01.02`, `APO01.03`, `APO12.01`, `APO12.06`, `APO14.01`, `APO14.02`, `APO14.03`, ...) |
| 14 | **Business Process Owner** | Individual accountable for performing processes and/or realizing process objectives, driving process improvement and approving process changes | *0 praktik* | *0 praktik* |
| 15 | **Portfolio Manager** | Individual responsible for guiding portfolio management, ensuring selection of correct programs and projects, managing and monitoring programs and projects for optimal value | *0 praktik* | **12 praktik** (`EDM02.04`, `APO05.01`, `APO05.02`, `APO05.03`, `APO05.04`, `APO05.05`, `APO06.01`, `APO06.02`, ...) |
| 16 | **Steering (Programs/Projects) Committee** | Group of stakeholders and experts accountable for guiding programs and projects, including managing and monitoring plans, allocating resources, delivering benefits and value, and managing program and project risk | *0 praktik* | *0 praktik* |
| 17 | **Program Manager** | Individual responsible for guiding a specific program, including articulating and following up on goals and objectives of the program and managing risk and impact on the business | *0 praktik* | **38 praktik** (`APO05.02`, `APO05.03`, `APO05.04`, `APO05.05`, `APO11.03`, `APO11.05`, `BAI01.01`, `BAI01.02`, ...) |
| 18 | **Project Manager** | Individual responsible for guiding a specific project, including coordinating and delegating time, budget, resources and tasks across the project team | *0 praktik* | **32 praktik** (`APO11.03`, `APO11.05`, `BAI02.01`, `BAI02.02`, `BAI02.03`, `BAI02.04`, `BAI03.01`, `BAI03.02`, ...) |
| 19 | **Project Management Office** | Function responsible for supporting program and project managers and for gathering, assessing and reporting information about the conduct of programs and constituent projects | *0 praktik* | **45 praktik** (`APO02.05`, `APO05.04`, `APO07.01`, `APO07.02`, `APO07.03`, `APO07.04`, `APO07.05`, `APO07.06`, ...) |
| 20 | **Data Management Function** | Function responsible for supporting enterprise data assets across the data life cycle and managing data strategy, infrastructure and repositories | *0 praktik* | *0 praktik* |
| 21 | **Head Human Resources** | Most senior official accountable for planning and policies regarding human resources in the enterprise | *0 praktik* | **12 praktik** (`APO01.04`, `APO01.09`, `APO04.01`, `APO07.01`, `APO07.02`, `APO07.03`, `APO07.04`, `APO07.05`, ...) |
| 22 | **Relationship Manager** | Senior individual responsible for overseeing and managing the internal interface and communications between business and I&T functions | *0 praktik* | **15 praktik** (`APO01.02`, `APO02.01`, `APO02.03`, `APO04.02`, `APO08.01`, `APO08.02`, `APO08.03`, `APO08.04`, ...) |
| 23 | **Head Architect** | Senior individual accountable for the enterprise architecture process | *0 praktik* | **42 praktik** (`APO01.07`, `APO01.08`, `APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, ...) |
| 24 | **Head Development** | Senior individual accountable for I&T-related solution development processes | *0 praktik* | **95 praktik** (`APO01.08`, `APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, `APO02.04`, ...) |
| 25 | **Head IT Operations** | Senior individual accountable for IT operational environments and infrastructure | *0 praktik* | *0 praktik* |
| 26 | **Head IT Administration** | Senior individual accountable for I&T-related records and responsible for supporting I&T-related administrative matters | *0 praktik* | *0 praktik* |
| 27 | **Service Manager** | Individual who manages the development, implementation, evaluation and ongoing maintenance of new and existing products and services for a specific customer or group of customers | *0 praktik* | **92 praktik** (`APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, `APO02.04`, `APO02.05`, ...) |
| 28 | **Information Security Manager** | Individual who manages, designs, oversees and/or assesses an enterprise's information security | *0 praktik* | **82 praktik** (`APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, `APO02.04`, `APO02.05`, ...) |
| 29 | **Business Continuity Manager** | Individual who manages, designs, oversees and/or assesses an enterprise's business continuity capability, to ensure critical functions continue to operate following disruptive events | **4 praktik:** `DSS04.03`, `DSS04.04`, `DSS04.06`, `DSS04.08` | **44 praktik** (`APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, `APO02.04`, `APO02.05`, ...) |
| 30 | **Privacy Officer** | Individual responsible for monitoring risk and business impact of privacy laws and for guiding and coordinating implementation of policies and activities that ensure compliance with privacy directives (DPO) | *0 praktik* | **42 praktik** (`APO01.09`, `APO01.10`, `APO01.11`, `APO02.01`, `APO02.02`, `APO02.03`, `APO02.04`, `APO02.05`, ...) |
| 31 | **Legal Counsel** | Function responsible for guidance on legal and regulatory matters | *0 praktik* | **25 praktik** (`APO07.02`, `APO07.06`, `APO09.03`, `APO09.04`, `APO10.01`, `APO10.03`, `APO10.05`, `APO14.08`, ...) |
| 32 | **Compliance** | Function responsible for all guidance on external compliance | **3 praktik:** `MEA03.01`, `MEA03.03`, `MEA03.04` | **1 praktik** (`MEA03.02`) |
| 33 | **Audit** | Function responsible for provision of internal audits | **9 praktik:** `MEA03.02`, `MEA04.01`, `MEA04.02`, `MEA04.03`, `MEA04.04`, `MEA04.05`, `MEA04.06`, `MEA04.07`, `MEA04.08` | **2 praktik** (`MEA03.01`, `MEA04.09`) |

---

## 2. Aturan Audit Matriks RACI & 12 Pola Konflik Segregation of Duties (SoD) Kritis

### A. Empat Hukum Pengujian Matriks RACI dalam Audit Tata Kelola TI
1. **Hukum Akuntabilitas Tunggal (*Single Point of Accountability*):** Setiap praktik proses **wajib memiliki tepat SATU peran `A` (Accountable)**. Jika suatu praktik tidak memiliki `A` (*Accountability Vacuum*), tidak ada pihak yang dapat dimintai pertanggungjawaban saat terjadi insiden. Jika memiliki lebih dari satu `A` (*Shared Accountability*), akan terjadi saling lempar tanggung jawab.
2. **Hukum Keberadaan Pelaksana (*Execution Sufficiency*):** Setiap praktik wajib memiliki minimal satu peran `R` (*Responsible*).
3. **Hukum Beban Akuntabilitas Eksekutif (*Accountability Overload Check*):** Apabila `CIO` menjadi `A` untuk seluruh proses operasional teknis tanpa pendelegasian ke `Head IT Operations`, `Head Development`, `Head Architect`, atau `Service Manager`, maka terjadi *bottleneck* pengambilan keputusan.
4. **Hukum Independensi Pengawasan (*Oversight Independence*):** Peran yang menyusun/mengeksekusi (`R`) tidak boleh menjadi pihak yang mengaudit atau memberi asurans independen atas pekerjaannya sendiri.

### B. 12 Pola Konflik Segregation of Duties (SoD) Kritis (ITGC & ITAC)

| Kode SoD | Kombinasi Peran / Hak Akses yang Bertabrakan | Objek Praktik COBIT | Risiko Kecurangan (*Fraud*) / Kegagalan Kontrol | Kontrol Kompensasi (Jika Organisasi Kecil / SME) |
| :---: | :--- | :--- | :--- | :--- |
| **SOD-01** | **Board / Governance (`EDM`)** dirangkap oleh **CIO / Manajemen Teknis (`APO/DSS`)** | `EDM01`–`EDM05` vs `APO01`–`DSS06` | Manajemen TI menilai dan mengawasi dirinya sendiri (*Self-Governance*); investasi TI bias dan risiko disembunyikan. | Pengawasan langsung oleh Direktur Utama/Komisaris Independen dan review Komite Audit berkala. |
| **SOD-02** | **Application Developer (`Head Development` / Programmer)** memiliki akses **Deployment / Admin ke Production (`Head IT Operations`)** | `BAI03` vs `BAI06`, `DSS01` | Developer dapat menyisipkan kode berbahaya (*backdoor/logic bomb*) atau mengubah data transaksi langsung di produksi tanpa terdeteksi. | Pipa CI/CD otomatis dengan persetujuan *Pull Request* + persetujuan CAB (`BAI06`), serta pencabutan akses tulis developer di produksi + *alert* SIEM. |
| **SOD-03** | **CIO / Head IT Operations** merangkap sebagai **CISO (`APO13`)** atau membawahi CISO tanpa garis pelaporan independen ke CRO/Direksi | `DSS01` vs `APO13`, `DSS05` | Konflik kepentingan antara target *uptime*/kecepatan rilis vs keamanan; insiden kebocoran data cenderung ditutupi agar SLA operasional terlihat hijau. | Garis pelaporan fungsional CISO langsung ke Direktur Manajemen Risiko (`CRO`) / CEO / Komite Risiko (`EDM03`). |
| **SOD-04** | **Fungsi TI Operasional (`CIO`/`Head IT Ops`)** merangkap atau mengendalikan **Internal Audit TI (`Audit`)** | `APO`–`DSS` vs `MEA04` | Kehilangan independensi asurans secara total; temuan kritis ditekan atau dihapus sebelum sampai ke Komite Audit. | **Tidak ada kompensasi yang mengizinkan TI mengendalikan Audit.** Fungsi Audit wajib melapor ke Komite Audit / Dewan Komisaris (`MEA04`). |
| **SOD-05** | **Database Administrator (DBA)** merangkap sebagai **Security Administrator / Pengelola Log Audit (SIEM)** | `DSS01`, `APO14` vs `DSS05` | DBA dapat memodifikasi saldo/data sensitif di database lalu menghapus jejak log auditnya sendiri (*log tampering*). | Pengiriman log database secara *real-time* ke server SIEM terpisah (*immutable syslog*) yang hanya dikelola oleh tim Security (`DSS05.04`). |
| **SOD-06** | **Pengusul Perubahan (Change Initiator / Developer)** merangkap sebagai **Penyetuju Perubahan (Change Approver / CAB)** | `BAI03` vs `BAI06.02` | Perubahan belum teruji atau tidak sah lolos ke produksi, memicu *downtime* atau celah keamanan. | Persetujuan wajib dari pemilik proses bisnis (*Business Process Owner*) dan manajer independen di CAB. |
| **SOD-07** | **Pemberi Persetujuan Hak Akses (Access Approver)** merangkap sebagai **Pelaksana Provisioning Akun (IAM/SysAdmin)** | `DSS05.04` vs `DSS06.03` | SysAdmin dapat membuat akun fiktif atau memberikan hak *Superuser* kepada dirinya/rekannya tanpa otorisasi pemilik bisnis. | Rekonsiliasi berkala antara tiket persetujuan akses dengan log pembuatan akun di Active Directory/IAM serta *User Access Review (UAR)* kuartalan. |
| **SOD-08** | **Pemilih/Negosiator Vendor TI** merangkap sebagai **Penerima Barang/Jasa (Berita Acara Serah Terima) & Penyetuju Pembayaran** | `APO10` vs `APO06`, `DSS06` | Risiko suap/kickback pengadaan TI, pembayaran atas lisensi/jasa fiktif (*phantom billing*). | Pemisahan fungsi Pengadaan (Procurement), Pemilik Proyek/Penerima Teknis, dan Keuangan (`CFO`), serta audit kontrak `APO10`. |
| **SOD-09** | **Arsitek / Pembuat Kebijakan Keamanan (`APO03`/`APO13`)** merangkap sebagai **Pemberi Pengecualian Risiko (*Risk Exception Approver*)** | `APO03`, `APO13` vs `APO12` | Standar keamanan/arsitektur diabaikan secara sepihak tanpa evaluasi dampak bisnis oleh pemilik risiko. | Setiap pengecualian kebijakan (*waiver/dispensation*) wajib disetujui oleh `CRO` / *Enterprise Risk Committee* dan dicatat di *Risk Register* (`APO12`). |
| **SOD-10** | **Pengembang Kode Aplikasi** merangkap sebagai **Penguji UAT / Penandatangan Lulus Uji (*QA & UAT Sign-off*)** | `BAI03` vs `APO11`, `BAI07` | Pengujian menjadi bias (hanya menguji skenario positif), *bug* kritis dan salah hitung finansial lolos ke produksi. | UAT wajib dieksekusi dan ditandatangani oleh `Business Process Owner` dan tim QA independen (`BAI07.05`). |
| **SOD-11** | **Aplikasi Bisnis (ITAC): Pembuat Master Data Vendor/Nasabah** merangkap sebagai **Pembuat/Penyetuju Transaksi Pembayaran** | `DSS06.02`, `DSS06.03` | Karyawan membuat rekening vendor fiktif lalu mencairkan dana perusahaan ke rekening pribadinya. | Penegakan matriks RBAC di ERP, kontrol *Maker-Checker-Approver* otomatis, dan pantauan perubahan *Master Data*. |
| **SOD-12** | **Penanganan Insiden Operasional (`DSS02`)** tanpa pemisahan kajian **Kepatuhan & Privasi (`Privacy Officer` / `MEA03`)** saat terjadi kebocoran data | `DSS02` vs `APO14`, `MEA03` | Tim teknis hanya memulihkan server namun gagal memenuhi kewajiban notifikasi 3x24 jam UU PDP karena konflik kepentingan. | Protokol respons insiden keamanan wajib melibatkan `Privacy Officer (DPO)`, `Legal Counsel`, dan `CISO` secara otomatis. |

---

## 3. Matriks Multi-Framework & Regulasi Crosswalk (Internasional & Nasional Indonesia)

Tabel ini memetakan **40 Objektif COBIT 2019** ke standar internasional utama serta regulasi wajib di Indonesia (**UU PDP No. 27/2022**, **POJK No. 11/POJK.03/2022 & SEOJK 29/2022**, dan **Perpres No. 95/2018 tentang SPBE**):

| Objektif COBIT 2019 | ISO/IEC & ITIL / TOGAF / PMBOK | NIST CSF 2.0 & NIST SP 800-53 / CIS v8 | Regulasi Indonesia (UU PDP, POJK 11/2022, SPBE, BSSN) |
| :--- | :--- | :--- | :--- |
| **`EDM01`** Governance Framework | ISO/IEC 38500 (Principles 1–6); King IV | NIST CSF `GV.OC`, `GV.RM`, `GV.RR`; 800-53 `PL-1`, `PM-1` | **POJK 11/2022** Bab II (Wewenang & Tanggung Jawab Direksi/Komisaris & KPTI); **SPBE** Indikator 1–10 (Kebijakan Internal) |
| **`EDM02`** Benefits Delivery | ISO/IEC 38500; Val IT | NIST CSF `GV.SC` | **POJK 11/2022** Realisasi nilai Rencana Strategis TI; **SPBE** Keterpaduan Rencana & Anggaran |
| **`EDM03`** Risk Optimization | ISO 31000; ISO/IEC 27005; COSO ERM | NIST CSF `GV.RM-01`..`07`; 800-53 `PM-9` | **POJK 11/2022** Manajemen Risiko TI & **SEOJK 29/2022** Ketahanan Siber; **UU PDP** Penilaian Dampak PDP |
| **`EDM04`** Resource Optimization | ISO/IEC 38500 | NIST CSF `GV.RR`; 800-53 `PM-3` | **POJK 11/2022** Kecukupan SDM & Infrastruktur TI; **SPBE** Pengelolaan SDM SPBE |
| **`EDM05`** Stakeholder Engagement | ISO/IEC 38500; King IV | NIST CSF `GV.OV`; 800-53 `PM-6` | **POJK 11/2022** Bab IX Pelaporan Kondisi Terkini & Insiden TI ke OJK; **UU PDP** Pasal 46 Notifikasi Kebocoran Data |
| **`APO01`** I&T Management Framework | ISO/IEC 27001 Kl. 4–5; ISO 20000-1 | NIST CSF `GV.PO`, `GV.RR`; 800-53 `PL-1`, `PS-1` | **POJK 11/2022** Struktur Organisasi TI & Kebijakan/Prosedur TI; **SPBE** Tata Kelola SPBE (Indikator 11–20) |
| **`APO02`** Managed Strategy | TOGAF ADM Phase A/B; ITIL 4 Strategy Mgmt | NIST CSF `GV.OC`; 800-53 `PL-2`, `PM-1` | **POJK 11/2022** Pasal 9–12 Rencana Strategis TI (ITSP); **SPBE** Rencana Induk SPBE (Indikator 14) |
| **`APO03`** Enterprise Architecture | TOGAF 9.2/10 ADM; IT4IT | NIST SP 800-53 `PL-8`, `SA-8` | **POJK 11/2022** Arsitektur TI; **SPBE** Arsitektur SPBE (Indikator 11) & Peta Rencana SPBE (Indikator 12) |
| **`APO04`** Managed Innovation | TOGAF; SAFe | NIST SP 800-53 `SA-1` | **POJK 11/2022** Kajian Produk/Layanan Bank Digital Baru; **SPBE** Inovasi Layanan Digital |
| **`APO05`** Managed Portfolio | PMBOK Portfolio Mgmt; ITIL 4 Portfolio Mgmt | NIST SP 800-53 `PM-3` | **POJK 11/2022** Portofolio Proyek Strategis TI; **SPBE** Keterpaduan Anggaran & Investasi |
| **`APO06`** Budget and Costs | ITIL 4 Service Financial Mgmt | NIST SP 800-53 `PM-3` | **POJK 11/2022** Pengendalian Biaya & Efisiensi TI; **SPBE** Indikator 13 (Rencana & Anggaran SPBE) |
| **`APO07`** Human Resources | SFIA V6; e-CF; ISO 27002 Kl. 6 (People) | NIST CSF `PR.AT`; 800-53 `AT-1`..`4`, `PS-1`..`8`; CIS 14 | **POJK 11/2022** Kompetensi SDM TI & Screening; **UU PDP** Pelatihan & Penunjukan DPO (Pasal 53); **Indeks KAMI** |
| **`APO08`** Managed Relationships | ITIL 4 Relationship Management | NIST CSF `GV.OC` | **POJK 11/2022** Sinergi Satuan Kerja Bisnis & TI; **SPBE** Tim Koordinasi SPBE |
| **`APO09`** Service Agreements | ISO/IEC 20000-1; ITIL 4 Service Level Mgmt | NIST CSF `GV.SC` | **POJK 11/2022** Perjanjian Tingkat Layanan (SLA) Internal & Eksternal; **SPBE** Manajemen Layanan |
| **`APO10`** Managed Vendors | ISO/IEC 27002 Kl. 5.19–5.23; ISO 20000-1 | NIST CSF `GV.SC-01`..`10`; 800-53 `SR-1`..`12`; CIS 15 | **POJK 11/2022** Bab VI Penyedia Jasa TI (Alih Daya, Cloud, Right to Audit); **UU PDP** Prosesor Data (Pasal 51) |
| **`APO11`** Managed Quality | ISO 9001; CMMI | NIST SP 800-53 `SA-11` | **POJK 11/2022** Jaminan Kualitas Pengembangan & Layanan TI; **SPBE** Manajemen Kualitas Layanan |
| **`APO12`** Managed Risk | ISO/IEC 27005; ISO 31000; COSO ERM | NIST CSF `ID.RA`; 800-53 `RA-1`..`7`, `PM-9` | **POJK 11/2022** Bab III Manajemen Risiko TI; **SEOJK 29/2022** Penilaian Risiko Siber; **SPBE** Indikator 21 (Manajemen Risiko) |
| **`APO13`** Managed Security (ISMS) | **ISO/IEC 27001:2022** (Kl. 4–10) | NIST CSF `GV`, `ID`, `PR`; 800-53 `PM-1`, `PL-2` | **POJK 11/2022** & **SEOJK 29/2022** Ketahanan & Keamanan Siber; **Peraturan BSSN 4/2021** & **Indeks KAMI**; **SPBE** Indikator 22 |
| **`APO14`** Managed Data | CMMI DMM; DAMA-DMBOK; ISO 27701 | NIST Privacy Framework; 800-53 `PT-1`..`8`, `MP-1` | **UU PDP No. 27/2022** (Pasal 16–54: Prinsip, Hak Subjek Data, Retensi, ROPA, DPIA); **POJK 11/2022** Bab V Pengelolaan Data & Satu Data Indonesia |
| **`BAI01`** Managed Programs | PMBOK Program Mgmt; MSP; SAFe | NIST SP 800-53 `SA-2`, `PM-4` | **POJK 11/2022** Manajemen Program Transformasi Digital; **SPBE** Pelaksanaan Peta Rencana |
| **`BAI02`** Requirements Definition | BABOK; TOGAF; ISO/IEC 27002 Kl. 8.26 | NIST SP 800-53 `SA-3`, `SA-4`, `SA-8` | **POJK 11/2022** Spesifikasi Kebutuhan & Keamanan Aplikasi; **UU PDP** *Privacy by Design*; **SPBE** Indikator 15 |
| **`BAI03`** Solutions Identification & Build | ISO/IEC 27002 Kl. 8.25–8.31; OWASP ASVS | NIST CSF `PR.PS`; 800-53 `SA-3`, `SA-11`, `SA-15`; CIS 16 | **POJK 11/2022** Secure SDLC, Pemisahan Lingkungan Dev/Test/Prod & Pengujian Keamanan; **BSSN** Standar Keamanan Aplikasi |
| **`BAI04`** Availability and Capacity | ISO/IEC 20000-1; ITIL 4 Availability & Capacity | NIST CSF `PR.IR`; 800-53 `CP-2`, `AU-4` | **POJK 11/2022** Pengelolaan Kapasitas & Ketersediaan Layanan TI; **SPBE** Infrastruktur SPBE |
| **`BAI05`** Organizational Change | PROSCI ADKAR; ITIL 4 OCM | NIST CSF `PR.AT` | **POJK 11/2022** Kesiapan Pengguna & Sosialisasi Sistem Baru; **SPBE** Manajemen Perubahan (Indikator 27) |
| **`BAI06`** Managed IT Changes | ISO/IEC 20000-1; ITIL 4 Change Enablement; ISO 27002 Kl. 8.32 | NIST CSF `PR.PS-02`; 800-53 `CM-3`, `CM-4`, `CM-5` | **POJK 11/2022** Pengendalian Perubahan (Change Management & Emergency Change); **Indeks KAMI** Pengelolaan Perubahan |
| **`BAI07`** Change Acceptance & Transition | ITIL 4 Release & Deployment; ISO 27002 Kl. 8.29 | NIST SP 800-53 `CA-2`, `CM-3`, `SA-11` | **POJK 11/2022** User Acceptance Testing (UAT), Migrasi Data & Post-Implementation Review (PIR) |
| **`BAI08`** Managed Knowledge | ISO 30401; ITIL 4 Knowledge Management | NIST SP 800-53 `AT-3` | **SPBE** Indikator 26 (Manajemen Pengetahuan SPBE); **POJK 11/2022** Dokumentasi Sistem TI |
| **`BAI09`** Managed Assets | ISO/IEC 19770 (ITAM); ISO 27002 Kl. 5.9–5.14 | NIST CSF `ID.AM-01`..`08`; 800-53 `CM-8`, `MP-6`; CIS 1 & 2 | **POJK 11/2022** Inventarisasi Aset TI & Sanitasi Media Penyimpanan; **SPBE** Indikator 23 (Manajemen Aset TI) |
| **`BAI10`** Managed Configuration | ITIL 4 Service Configuration Mgmt; ISO 20000-1 | NIST CSF `PR.PS-01`; 800-53 `CM-2`, `CM-6`, `CM-8`; CIS 4 | **POJK 11/2022** Pengelolaan Konfigurasi (CMDB) & Hardening Baseline; **BSSN** Panduan Hardening |
| **`BAI11`** Managed Projects | **PMBOK 6th/7th Ed.**; PRINCE2; Agile | NIST SP 800-53 `SA-3` | **POJK 11/2022** Manajemen Proyek TI (PMO, Waktu, Biaya, Mutu, Risiko Proyek) |
| **`DSS01`** Managed Operations | ITIL 4 Operations; ISO 27002 Kl. 7 (Physical) | NIST CSF `PR.IR`; 800-53 `PE-1`..`20`; CIS 12 | **POJK 11/2022** Operasional TI & Keamanan Fisik Data Center; **SPBE** Penyelenggaraan Pusat Data Nasional |
| **`DSS02`** Service Requests & Incidents | ISO/IEC 20000-1; ITIL 4 Incident & Service Desk; ISO 27002 Kl. 5.24–5.28 | NIST CSF `DE.AE`, `RS.MA`, `RS.AN`, `RS.MI`; 800-53 `IR-1`..`8`; CIS 17 | **POJK 11/2022** & **SEOJK 29/2022** Tanggap Insiden Siber (CSIRT/IRT); **UU PDP** Pasal 46 Notifikasi 3x24 Jam; **BSSN** CSIRT |
| **`DSS03`** Managed Problems | ISO/IEC 20000-1; ITIL 4 Problem Management | NIST CSF `RS.AN`; 800-53 `IR-4` | **POJK 11/2022** Analisis Akar Masalah (Root Cause Analysis / RCA) atas Gangguan Berulang |
| **`DSS04`** Managed Continuity | **ISO 22301**; ISO/IEC 27031; ITIL 4 Continuity | NIST CSF `RC.RP`, `RC.CO`; 800-53 `CP-1`..`10`; CIS 11 | **POJK 11/2022** Bab IV Rencana Pemulihan Bencana (DRP/BCP, BIA, RTO/RPO & Uji DRP Tahunan Wajib); **SPBE** Keberlangsungan Layanan |
| **`DSS05`** Managed Security Services | **ISO/IEC 27002:2022** (Kl. 5 & 8); CIS Controls v8 | NIST CSF `PR.AA`, `PR.DS`, `DE.CM`; 800-53 `AC`, `IA`, `SC`, `SI`, `AU`; CIS 3–10, 13, 18 | **SEOJK 29/2022** Pengujian Kerentanan, Pentest, IAM/PAM, Enkripsi, SIEM/SOC; **UU PDP** Pasal 35 Keamanan Teknis Data Pribadi |
| **`DSS06`** Business Process Controls | COSO ICIF (ITAC); ISACA IT Application Controls | NIST SP 800-53 `AC-5` (SoD), `SI-10` (Input Validation) | **POJK 11/2022** Pengendalian Aplikasi, Jejak Audit Transaksi, Rekonsiliasi & Pemisahan Fungsi (SoD); **UU PDP** Akurasi Pemrosesan |
| **`MEA01`** Performance & Conformance | ISO/IEC 20000-1; ISO/IEC 27004 | NIST CSF `GV.OV`; 800-53 `CA-7`, `PM-6` | **POJK 11/2022** Pemantauan Kinerja Layanan TI; **SPBE** Pemantauan & Evaluasi SPBE |
| **`MEA02`** System of Internal Control | COSO Internal Control; IIA Three Lines Model | NIST SP 800-53 `CA-2`, `CA-5`, `PM-14` | **POJK 11/2022** Sistem Pengendalian Intern TI (Lini Pertama & Lini Kedua) |
| **`MEA03`** External Compliance | ISO/IEC 27002 Kl. 5.31–5.36 | NIST CSF `GV.OC-03`; 800-53 `AU-1`, `PM-8` | **UU PDP No. 27/2022** Kepatuhan Pengendali/Prosesor Data; **POJK 11/2022** Kepatuhan Regulasi TI |
| **`MEA04`** Managed Assurance | **ISACA ITAF**; IIA IPPF; ISO 19011 | NIST SP 800-53 `CA-2`, `CA-7` | **POJK 11/2022** Bab VIII Audit Intern & Audit Ekstern TI Independen; **SPBE** Indikator 28–30 (Audit TIK) |

---

## 4. Kamus Penerjemah Temuan Teknis ke Risiko Bisnis (*Technical-to-Business Risk Translator*)

Seorang Auditor TI COBIT 2019 tidak pernah melaporkan temuan hanya dengan kalimat teknis seperti *"Port 22 terbuka"* atau *"Backup belum di-restore"*. Gunakan tabel penerjemah berikut untuk mengubah temuan teknis menjadi **Bahasa Risiko Bisnis Eksekutif** lengkap dengan keterkaitan Praktik, `AG`, dan `EG`:

| No. | Temuan Teknis di Lapangan (Condition) | Praktik COBIT | Cascade (`AG` $\rightarrow$ `EG`) | Terjemahan Risiko & Dampak Bisnis Eksekutif (Effect / Consequence) |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Backup harian berjalan sukses, namun **tidak pernah dilakukan uji pemulihan (*Restore Testing*)** dan uji *switch-over* DRC gagal melampaui RTO. | `DSS04.04`<br>`DSS04.07` | `AG05`, `AG07` $\rightarrow$<br>`EG02`, `EG06` | **Risiko Kelumpuhan Operasional & Kehilangan Data Permanen:** Saat terjadi serangan *ransomware* atau kegagalan pusat data utama, perusahaan berisiko tidak dapat memulihkan transaksi nasabah, melampaui batas toleransi *downtime* (`EG06`), dan melanggar kewajiban uji DRP POJK 11/2022. |
| **2** | **Developer memiliki akses tulis (*write/admin*) langsung ke server/database produksi** dan melakukan *hotfix* tanpa tiket perubahan CAB. | `BAI03.05`<br>`BAI06.01`<br>`DSS05.04` | `AG06`, `AG07` $\rightarrow$<br>`EG02`, `EG06` | **Risiko Manipulasi Transaksi (*Fraud*) & Gangguan Layanan:** Pelanggaran *Segregation of Duties (SoD)* memungkinkan penyisipan logika kode tidak sah atau perubahan saldo langsung di produksi tanpa jejak kontrol, serta memicu *downtime* mendadak akibat kode yang belum teruji. |
| **3** | **Data pribadi nasabah (NIK, rekening, nomor telepon) disalin mentah ke lingkungan UAT/Development** tanpa *data masking/anonymization*. | `APO14.06`<br>`BAI03.06`<br>`DSS05.04` | `AG07`, `AG10` $\rightarrow$<br>`EG02`, `EG03` | **Risiko Kebocoran Data Pribadi & Sanksi UU PDP:** Lingkungan non-produksi memiliki kontrol keamanan lebih longgar dan diakses pihak ketiga; kebocoran dari server UAT dapat memicu denda administratif hingga **2% dari pendapatan tahunan** sesuai Pasal 57 UU PDP (`EG03`). |
| **4** | **Akun milik mantan karyawan dan kontraktor vendor yang sudah resign (>6 bulan) masih aktif** di Active Directory dan aplikasi inti. | `APO07.06`<br>`DSS05.04`<br>`DSS06.03` | `AG07`, `AG11` $\rightarrow$<br>`EG02`, `EG11` | **Risiko Akses Tidak Sah (*Insider/Ex-Employee Threat*) & Pembajakan Akun:** Akun yatim (*orphan accounts*) dapat dieksploitasi oleh mantan personel atau penyerang eksternal untuk mencuri data rahasia perusahaan tanpa terdeteksi. |
| **5** | **Server produksi menggunakan OS/Database *End-of-Life (EoL)*** atau belum di-*patch* terhadap kerentanan kritis (*Critical CVE*) selama >90 hari. | `BAI03.10`<br>`BAI09.02`<br>`DSS05.01` | `AG02`, `AG07` $\rightarrow$<br>`EG02`, `EG06` | **Risiko Eksploitasi Siber & Pengambilalihan Sistem Inti:** Celah keamanan publik yang sudah memiliki *exploit* aktif membuka pintu masuk bagi *ransomware* dan pencurian data massal. |
| **6** | **Kontrak vendor Cloud/Core System kritis tidak memuat klausul *Right to Audit*, DPA (Perlindungan Data), dan *Exit Strategy*.** | `APO10.03`<br>`APO10.04`<br>`MEA03.03` | `AG01`, `AG05` $\rightarrow$<br>`EG02`, `EG03` | **Risiko Ketergantungan Ekstrem (*Vendor Lock-in*) & Ketidakpatuhan Regulasi:** Perusahaan kehilangan kendali hukum saat terjadi insiden di sisi vendor, terhambat saat ingin berpindah penyedia, dan melanggar ketentuan alih daya POJK 11/2022 & Pasal 51 UU PDP. |
| **7** | **Pengguna di aplikasi ERP memiliki hak akses gabungan membuat *Master Data Vendor* sekaligus menyetujui pembayaran (*Payment Approval*).** | `DSS06.02`<br>`DSS06.03`<br>`MEA02.01` | `AG04`, `AG08` $\rightarrow$<br>`EG02`, `EG04` | **Risiko Kecurangan Finansial (*Financial Fraud*) & Salah Saji Laporan Keuangan:** Ketiadaan kontrol pemisahan tugas di level aplikasi memungkinkan pencairan dana ke vendor fiktif tanpa terdeteksi sistem. |
| **8** | **Proyek transformasi digital bernilai besar telah *Go-Live*, namun tidak pernah dilakukan *Post-Implementation Review (PIR)* dan pengukuran manfaat.** | `EDM02.03`<br>`APO05.04`<br>`BAI01.07` | `AG03`, `AG09` $\rightarrow$<br>`EG01`, `EG12` | **Risiko Investasi TI Sia-sia (*Value Leakage*):** Anggaran modal (CAPEX) telah habis terserap namun manfaat penghematan biaya atau peningkatan pendapatan yang dijanjikan pada *Business Case* tidak pernah terwujud (`EG12`). |
| **9** | **CMDB tidak mutakhir dan terdapat puluhan server aktif di jaringan produksi yang tidak tercatat di inventaris aset TI.** | `BAI09.01`<br>`BAI10.02`<br>`BAI10.04` | `AG04`, `AG07` $\rightarrow$<br>`EG02`, `EG09` | **Risiko *Blind Spot* Keamanan (*Shadow Infrastructure*) & Pemborosan Biaya:** Aset yang tidak tercatat di CMDB pasti terlewat dari jadwal *vulnerability scanning*, *patching*, dan *backup*, sehingga menjadi titik terlemah serangan siber. |
| **10** | **Penggunaan akun `root` / `Administrator` bersama (*Shared Privileged Account*) tanpa MFA dan tanpa perekaman sesi (*Session Recording*).** | `DSS05.04`<br>`DSS06.03` | `AG07`, `AG11` $\rightarrow$<br>`EG02`, `EG11` | **Risiko Hilangnya Nir-Penyangkalan (*Non-Repudiation*):** Ketika terjadi sabotase atau penghapusan database produksi menggunakan akun bersama, perusahaan tidak dapat membuktikan secara forensik siapa individu pelaku sebenarnya. |

---

## 5. Template Standar Temuan Audit 5C ISACA & Laporan Hasil Audit (LHA) Eksekutif

### A. Template Temuan Audit TI Berstandar 5C ISACA

Setiap temuan yang dihasilkan oleh skill `cobit-it-auditor` **wajib** memuat 5 elemen **5C** berikut secara lengkap:

```markdown
### TEMUAN AUDIT #[NOMOR]: [JUDUL TEMUAN YANG SPESIFIK & BERORIENTASI RISIKO BISNIS]
- **Tingkat Risiko (Risk Rating):** [Critical / High / Medium / Low]
- **Domain & Praktik COBIT 2019:** `[Kode Praktik, mis. DSS04.04 & DSS04.07]` — [Nama Praktik]
- **Jejak Goals Cascade:** `[Praktik]` $\rightarrow$ `[AGxx: Nama AG]` (**P**) $\rightarrow$ `[EGxx: Nama EG]` (**P**)
- **Current vs. Target Capability Level:** Current: `Level [X]` | Target: `Level [Y]` (`Gap = [Y-X]`)

1. **Condition (Kondisi Faktual & Bukti Audit):**
   [Uraikan fakta objektif dan terukur yang ditemukan saat pengujian ToD/ToE, sebutkan populasi vs sampel, nomor dokumen/tiket/server, dan tanggal pemeriksaan.]

2. **Criteria (Kriteria Standar & Regulasi):**
   - **COBIT 2019:** Praktik `[Kode Praktik]` (*Activity [No]* — Capability Level `[2/3/4]`): *"[Kutipan aktivitas resmi COBIT 2019]"*
   - **Standar / Regulasi Terkait:** `[Sebutkan klausul ISO/IEC 27001, NIST CSF, POJK 11/2022, UU PDP No. 27/2022, atau Kebijakan Internal]`

3. **Cause (Akar Penyebab — 7 Komponen COBIT):**
   - **Komponen Proses / Kebijakan (A & E):** [Mis. Belum adanya SOP tertulis yang mengatur pengujian restore berkala]
   - **Komponen Struktur RACI / SDM / Budaya / Alat (B, D, F, G):** [Mis. Kekosongan peran Accountable atau belum tersedianya tool otomatis]

4. **Effect / Consequence (Dampak & Risiko Bisnis Eksekutif):**
   [Terjemahkan dampak teknis ke dalam risiko bisnis yang mengancam pencapaian `AGxx` dan `EGxx`: potensi kerugian finansial, gangguan layanan pelanggan, kompromi integritas data, atau sanksi hukum/regulasi.]

5. **Corrective Action / Recommendation (Rekomendasi Bertahap & Penanggung Jawab RACI):**
   - **Quick Win / Jangka Pendek (0–30 Hari):**
     - *Tindakan:* [Tindakan korektif segera untuk menutup eksposur risiko aktif]
     - *Accountable (`A`):* `[Peran RACI Resmi]` | *Responsible (`R`):* `[Peran RACI Resmi]`
   - **Perbaikan Struktural / Jangka Menengah-Panjang (30–180 Hari — Menuju Target Capability Level `[Y]`):**
     - *Tindakan:* [Perbaikan menyeluruh pada 7 Komponen: Proses, RACI, Informasi, SDM, Kebijakan, Budaya, dan Aplikasi/Infrastruktur]
     - *Metrik Keberhasilan (KPI/KGI):* `[Contoh Metrik Resmi COBIT 2019 untuk memverifikasi penutupan temuan]`
```

### B. Struktur Laporan Hasil Audit (LHA) Tata Kelola & Manajemen TI Eksekutif

1. **Ringkasan Eksekutif (*Executive Summary*):** Opini/Kesimpulan Umum Audit, Profil Maturitas Rata-rata vs Target, dan Peta Risiko Utama bagi Dewan Direksi & Komite Audit.
2. **Konteks Organisasi, Design Factors & Ruang Lingkup Audit (*Goals Cascade Scope*):** Pemetaan strategi korporat ke `EG`, `AG`, dan Objektif COBIT 2019 yang diuji.
3. **Peta Skor Kapabilitas Proses (*Process Capability Scorecard 0–5*):** Tabel perbandingan *Target Capability Level* vs *Assessed Capability Level* (beserta status *Rating N/P/L/F* ISO/IEC 33000) dan analisis keseimbangan 7 Komponen.
4. **Evaluasi Struktur Organisasi, RACI & Segregation of Duties (SoD):** Temuan ketiadaan akuntabilitas (`A`), tumpang tindih wewenang, dan konflik SoD kritis.
5. **Rincian Temuan Audit Berformat 5C ISACA:** Diurutkan dari tingkat risiko *Critical*, *High*, *Medium*, hingga *Low*.
6. **Peta Jalan Remediasi Terintegrasi (*7-Phase Implementation Roadmap*):** Rencana tindak lanjut manajemen (*Management Action Plan*) yang dikelompokkan dalam Gelombang 1 (*Quick Wins* 0–90 hari), Gelombang 2 (Standarisasi Level 3), dan Gelombang 3 (Optimisasi Level 4).
