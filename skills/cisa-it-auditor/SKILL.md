---
name: cisa-it-auditor
description: Buku induk dan mesin eksekusi Audit Sistem Informasi berstandar ISACA CISA Review Manual (27th Edition), ITAF (4th Edition), IIA Audit Sampling, dan Big-4 SOX/ITGC Fieldwork Playbook. Mengevaluasi proses audit SI, tata kelola TI, akuisisi & SDLC, kontrol aplikasi (ITAC), operasional TI, ketahanan bisnis (BIA/BCP/DRP), keamanan informasi (IAM, Jaringan, Kriptografi, PKI, Forensik Digital), perhitungan Statistical Sampling & Quantitative Risk (ALE/EVA/PERT), deteksi konflik Segregation of Duties (SoD) 12 Peran TI, serta penyusunan program kerja TDE/TOE, daftar PBC (SOXIT.01–04), dan Laporan Hasil Audit 5C.
---

# CISA IT Auditor — Master Handbook & Fieldwork Execution Engine (ISACA CRM 27e & ITAF 4e)

Skill ini adalah **Buku Induk Referensi (*Master Reference Book*)** sekaligus **Mesin Otomasi Kertas Kerja Audit Sistem Informasi (*IS Audit Workpaper Engine*)** yang mengintegrasikan secara utuh:
1. **ISACA CISA Review Manual (27th Edition)** & *Hemang Doshi CISA Study Guide* (**5 Domain**, **39 Task Statements `T1`–`T39`**).
2. **ISACA Information Technology Assurance Framework (ITAF™ 4th Edition)** (**17 Standar Wajib `1001`–`1402`** & **17 Pedoman `2001`–`2402`**) serta keselarasan **ISO 19011**, **ISO/IEC 27007**, dan **ISO/IEC TS 27008**.
3. **IIA Practice Guide: Internal Audit Sampling** (*Attribute*, *Stop-or-Go*, *Discovery*, *Variable / Stratified MPU*, dan *Monetary Unit Sampling / MUS* dengan tabel Poisson $R$-Factor & Normal $Z$-Factor).
4. **Matriks Lengkap SOX/ITGC Key Controls (`SOXIT.01` s.d. `SOXIT.04` — 18 Key Controls)** beserta atribut **TDE (*Test of Design Effectiveness*)**, **TOE (*Test of Operating Effectiveness*)**, dan **Daftar Permintaan Dokumen PBC (*Prepared-by-Client*)**.
5. **Panduan Teknis Walkthrough Sistem Operasi & Database (`S07_W100`)** untuk **Unix/Solaris/Linux**, **Oracle Database**, **Microsoft SQL Server**, dan **SAP ERP** beserta studi kasus nyata (**PT XYZ** & **PT Ramayana Lestari Sentosa Tbk**).

---

## 1. Peta Arsitektur Pustaka Buku CISA (`references/`, `data/`, `scripts/`)

Seluruh materi buku disimpan secara terstruktur di dalam direktori skill ini. **Baca bab referensi yang relevan menggunakan `read_file` dan jalankan `scripts/cisa_cli.py` untuk melakukan kalkulasi dan ekstraksi data presisi:**

### A. 13 Bab Buku Referensi (`references/`)
- **[Bab 1: Standar Profesional ISACA ITAF (4th Edition), Kode Etik, dan Audit Charter](references/01-itaf-standards-ethics-and-audit-charter.md)**
  - Bobot 5 Domain CISA, 7 Kode Etik ISACA, 17 Standar ITAF (`1001`–`1402`) & 17 Pedoman (`2001`–`2402`), perbandingan *Audit Charter vs. Engagement Letter*, *Attestation vs. Direct Engagement*, serta integrasi ISO 19011 / 27007 / 27008.
- **[Bab 2: Domain 1 — Proses Audit SI, Statistical Sampling (IIA), dan CAATs (21%)](references/02-domain1-is-auditing-process-sampling-and-caats.md)**
  - Siklus *Risk-Based Audit*, Model Risiko Audit ($\text{AR} = \text{IR} \times \text{CR} \times \text{DR}$), matriks kontrol (*Preventive, Detective, Corrective, Compensating*), *Compliance vs. Substantive Testing*, rumus lengkap **IIA Statistical Sampling** (Poisson $R$-Factor, Attribute, Discovery, Stop-or-Go, Variable MPU, MUS/PPS, dan tabel sampel ITGC), **CAATs** (GAS, Test Data, ITF, SCARF, Snapshot, Audit Hooks, CIS), hierarki keandalan bukti audit, *Control Self-Assessment* (CSA), dan format temuan **5C**.
- **[Bab 3: Domain 2 — Tata Kelola dan Manajemen TI (17%)](references/03-domain2-it-governance-and-management.md)**
  - *Enterprise Governance of IT* (EGIT), *IT Strategy Committee vs. IT Steering Committee*, hierarki *Policies/Standards/Procedures/Guidelines*, **Matriks Konflik Segregation of Duties (SoD) 12 Peran TI** & kontrol kompensasinya, kontrol HR (*Mandatory Vacation, Job Rotation, Immediate Termination*), analisis risiko kuantitatif ($\text{SLE} = \text{AV} \times \text{EF}$, $\text{ALE} = \text{SLE} \times \text{ARO}$, ROI Kontrol), **IT Balanced Scorecard (IT BSC)**, kontrak *Outsourcing/Cloud*, dan perbandingan laporan **SOC 1, SOC 2, SOC 3 (Type 1 vs. Type 2 & CUECs)**.
- **[Bab 4: Domain 3 (Bagian 1) — Tata Kelola Proyek, Metrik CPM/PERT/EVA, SDLC, dan Akuisisi (12%)](references/04-domain3-part1-project-governance-sdlc-and-acquisition.md)**
  - *Business Case* & *Feasibility Study*, peran *Sponsor vs. Steering Committee*, WBS, **Critical Path Method (CPM)**, rumus **PERT** ($T_e = \frac{O+4M+P}{6}$), rumus lengkap **Earned Value Analysis (EVA: BAC, PV, EV, AC, CV, SV, CPI, SPI, EAC, ETC)**, **Function Point Analysis (FPA)**, *Timeboxing*, perbandingan **10 Model SDLC** (*Waterfall, V-Model, Prototyping, RAD, Agile, DevOps, OO, CBD, Reengineering, Reverse Engineering*), RFP, dan **Software Escrow**.
- **[Bab 5: Domain 3 (Bagian 2) — Kontrol Aplikasi (ITAC), Metodologi Pengujian, dan Migrasi Data (12%)](references/05-domain3-part2-application-controls-testing-and-migration.md)**
  - Arsitektur **ITAC** (*Input, Processing, Output Controls*), *Batch Totals* (*Financial, Hash Total, Record Count*), **12 Jenis Edit Validation Checks** (termasuk *Check Digit Mod-10/11*), *Run-to-Run Totals*, kontrol transaksi elektronik (**EDI, EFT, POS, E-Banking**), **12 Metode Pengujian Software** (*Unit, Integration, System, Regression, Sociability, Pilot, Parallel, White/Black-Box, Alpha/Beta, UAT*), sanitasi data uji, serta strategi *Cutover* (*Parallel, Phased, Abrupt*).
- **[Bab 6: Domain 4 (Bagian 1) — Operasional SI, Perangkat Keras, Database, dan ITSM (23%)](references/06-domain4-part1-is-operations-hardware-db-and-itsm.md)**
  - Kontrol *Job Scheduling* & *Console Logs*, pemantauan perangkat keras, kontrol USB/RFID, ITAM & lisensi software, risiko **End-User Computing (EUC / Spreadsheet)**, arsitektur **DBMS** (*3-Schema, Normalization vs. Denormalization, Referential Integrity, Properti ACID, Concurrency Locking*), serta proses **ITSM / ITIL** (*Incident vs. Problem Management*, *Change Management*, *Emergency Change Retroactive Review*, CMDB, *Patch Management*, dan **SLA / OLA / UC**).
- **[Bab 7: Domain 4 (Bagian 2) — Ketahanan Bisnis, BIA, BCP/DRP, RAID, Backup, dan Situs Pemulihan (23%)](references/07-domain4-part2-business-resilience-bia-bcp-drp-and-backup.md)**
  - Linimasa & rumus metrik **BIA** (**RPO, RTO, WRT, MTD/MTO, SDO/MBCO, AIW** di mana $\text{RTO} + \text{WRT} \le \text{MTD}$), perbandingan **RAID 0, 1, 5, 6, dan 10**, redundansi telekomunikasi (*Alternative vs. Diverse Routing*), skema **Backup (Full, Incremental, Differential & Rotasi GFS)**, perbandingan **6 Jenis Alternate Recovery Sites** (*Mirrored, Hot, Warm, Cold, Mobile, Reciprocal*), serta **5 Metode Pengujian DRP**.
- **[Bab 8: Domain 5 (Bagian 1) — Keamanan Informasi, Kontrol Fisik, IAM & Biometrik, dan Keamanan Jaringan (27%)](references/08-domain5-part1-information-security-iam-and-network-security.md)**
  - Trias CIA, peran **Data Owner vs. Data Custodian**, keamanan fisik & lingkungan (*Mantrap*, detektor asap, **Dry-Pipe vs. Wet-Pipe**, gas bersih **FM-200 / Inergen** pengganti Halon, UPS + Generator, kelembapan $40\%-60\%$), model akses (*MAC, DAC, RBAC, ABAC*), grafik kesalahan biometrik (**FRR [Type I], FAR [Type II], dan CER/EER**), **SSO (Kerberos KDC & SAML)**, pemetaan **Model OSI 7 Layer**, **4 Jenis Firewall**, arsitektur **DMZ (Screened Subnet)**, **IDS vs. IPS**, VPN (*IPsec/TLS*), Wireless (*WPA2/WPA3 & 802.1X*), risiko *Hypervisor*, BYOD/MDM, dan DLP.
- **[Bab 9: Domain 5 (Bagian 2) — Kriptografi, PKI, Tanda Tangan Digital, Serangan Siber, Pentest, dan Forensik Digital (27%)](references/09-domain5-part2-cryptography-pki-attacks-pentest-and-forensics.md)**
  - Perbandingan kriptografi **Simetris (AES/3DES) vs. Asimetris (RSA/ECC/DH)**, fungsi **Hash (SHA-2/SHA-3) & HMAC**, aturan mutlak penguncian kunci untuk **Kerahasiaan vs. Digital Signature (Non-Repudiation) vs. Digital Envelope**, ekosistem **PKI (CA, RA, CPS, CRL, OCSP)**, **14 Serangan Siber & Mitigasinya** (*SQLi, XSS, CSRF, Buffer Overflow, MitM, ARP/DNS Poisoning, DDoS, Phishing, Ransomware, Logic Bomb*), **VA vs. Penetration Testing** (*Black/White/Gray/Double-Blind*), **6 Fase Incident Response**, dan prosedur **Digital Forensics** (*Order of Volatility, Write-Blocker, Bit-Stream Image, Hash Verification, Chain of Custody*).
- **[Bab 10: Matriks Lengkap SOX/ITGC Key Controls (`SOXIT.01`–`SOXIT.04`), Daftar PBC, Panduan Teknis Walkthrough, dan Studi Kasus Nyata](references/10-soxit-itgc-key-controls-pbc-walkthrough-and-case-studies.md)**
  - Matriks lengkap 18 kontrol kunci `SOXIT.01`–`SOXIT.04` (TDE, TOE, PBC), tabel perintah audit teknis **Unix/Solaris/Linux** (`/etc/passwd`, `/etc/shadow`, `UID=0`, `/etc/inetd.conf`, `cron.allow`), **Oracle Database** (`DBA_USERS`, `DBA_PROFILES`, `DBA_SYS_PRIVS`, `DBA_TAB_PRIVS`, `PUBLIC`, `DBA_AUDIT_TRAIL`), **SQL Server** (`sys.sql_logins`, `xp_cmdshell`), serta pembahasan lengkap **Studi Kasus 1: PT XYZ (SAP ERP)** dan **Studi Kasus 2: PT Ramayana Lestari Sentosa Tbk (MARIS/MAGIC)**.
- **[Bab 11: Pustaka Skrip Ekstraksi Bukti Teknis (Live Audit Queries) — SAP ERP/S4HANA, Active Directory, Cloud (AWS/Azure/GCP), & Kubernetes/CI-CD](references/11-live-technical-audit-scripts-sap-ad-cloud-k8s.md)**
  - Daftar lengkap **SAP T-Codes** (`SU01`, `SUIM`, `PFCG`, `SCC4`, `RZ10/RZ11`, `STMS`, `SM19/SM20`, `SM36/SM37`, `OB52`) & Tabel (`USR02`, `UST04`, `AGR_USERS`, `T000`, `E070`), skrip PowerShell **Active Directory**, kontrol keamanan **AWS/Azure/GCP**, serta audit **Docker/Kubernetes & GitHub/GitLab Branch Protection SoD**.
- **[Bab 12: Pembaruan Kurikulum CISA 28th Edition (2024–2026) — Audit Sistem AI/LLM, Zero Trust, & Playbook Ransomware](references/12-cisa-28e-ai-auditing-zero-trust-and-ransomware-playbook.md)**
  - Audit siklus hidup **AI/ML/LLM** (*Data Poisoning, Algorithmic Bias, Overfitting, Prompt Injection, Hallucination, Model Drift, Explainable AI*), **Playbook Audit Ketahanan Ransomware (3-2-1-1-0 Immutable Backup)**, serta audit **Blockchain, Smart Contracts, & IoT/OT SCADA**.
- **[Bab 13: Masterclass "ISACA Exam Mindset" & Bank 30 Skenario Soal CISA (QAE)](references/13-cisa-exam-qae-mindset-and-scenario-bank.md)**
  - 10 Hukum Emas menjawab soal jebakan CISA (*FIRST, NEXT, BEST, MOST, PRIMARY*) beserta 30 skenario kasus lintas Domain 1–5 dan bedah rasional jawaban benar vs. pengecoh.

---

## 2. Mesin CLI CISA (`scripts/cisa_cli.py`) & Database JSON (`data/cisa_database.json`)

Gunakan skrip Python bebas-dependensi `scripts/cisa_cli.py` untuk mengeksekusi perhitungan audit dan pencarian standar secara otomatis:

```powershell
# 1. Lookup Domain (D1-D5), Task (T1-T39), Standar ITAF (1001-1402), Kontrol SOXIT, atau Panduan Teknis (BIA, SDLC, UNIX, ORACLE)
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" lookup --id D5
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" lookup --id 1205
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" lookup --id SOXIT.03.00.00.C4
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" lookup --id ORACLE

# 2. Kalkulator IIA Statistical Sampling (Attribute, Discovery, MUS, Variable, atau Tabel ITGC)
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" sampling --method attribute --confidence 95 --tolerable-error 0.05 --expected-deviations 0 --population 1000
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" sampling --method mus --confidence 95 --book-value 5000000 --tolerable-misstatement 250000 --expected-deviations 0
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" sampling --method itgc --frequency all

# 3. Kalkulator Risiko Kuantitatif (SLE/ALE/ROI), Proyek (EVA & PERT), dan Model Risiko Audit (AR=IR*CR*DR)
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" risk-calc --mode ale --asset-value 1000000 --exposure-factor 0.40 --aro 0.20 --ef-post 0.10 --aro-post 0.20 --acs 15000
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" risk-calc --mode eva --bac 200000 --pv 100000 --ev 80000 --ac 110000
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" risk-calc --mode pert --optimistic 4 --most-likely 7 --pessimistic 16

# 4. Detektor Konflik Segregation of Duties (SoD) 12 Peran TI & Rekomendasi Kontrol Kompensasi
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" sod-check --roles "developer,operator,security_admin"

# 5. Generator Program Kerja Audit (TDE/TOE) & Daftar Permintaan Dokumen (PBC) SOX/ITGC
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" pbc --domain SOXIT.03

# 6. Pencarian Kata Kunci Lintas Seluruh Database CISA
python "C:\Users\erlangga.utama\.agents\skills\cisa-it-auditor\scripts\cisa_cli.py" search --query "FireCall"
```

---

## 3. Doktrin Eksekusi Audit CISA ("ISACA Mindset" & Standar Output)

Setiap kali pengguna meminta analisis audit SI, evaluasi kasus, perencanaan pengujian ITGC/ITAC, atau pembahasan soal/skenario CISA, terapkan **6 Aturan Doktrin CISA** berikut:

1. **Utamakan Risiko Bisnis & Keselamatan Jiwa di Atas Segala Hal:**
   - Dalam skenario bencana fisik (BCP/DRP), langkah pertama yang mutlak adalah **Keselamatan Jiwa Manusia (*Human Life Safety*)**.
   - Dalam keputusan investasi kontrol, biaya kontrol tahunan (**ACS**) tidak boleh melebihi pengurangan kerugian tahunan yang diharapkan (**ALE**).
2. **Tegakkan Pemisahan Tugas (SoD) & Prinsip Pemilik Bisnis (*Data Owner*):**
   - **Data Owner (Manajer Unit Bisnis)** adalah pihak yang berwenang menentukan klasifikasi data dan menyetujui hak akses secara tertulis; **Security Admin** hanya mengeksekusi pemberian akses; **Developer/Programmer** dilarang keras memiliki akses ubah/migrasi di lingkungan **Production**.
   - Jika organisasi terlalu kecil untuk menerapkan SoD penuh, wajibkan **Compensating Control** berupa **Independent Audit Trail / Activity Log Review** oleh manajemen.
3. **Bedakan Pengujian Desain (TDE) vs. Pengujian Efektivitas Operasional (TOE):**
   - **TDE (*Test of Design Effectiveness* / SOC Type 1):** Mengevaluasi apakah rancangan kontrol mampu mencegah/mendeteksi risiko pada satu titik waktu (*walkthrough*, inspeksi konfigurasi).
   - **TOE (*Test of Operating Effectiveness* / Compliance Testing / SOC Type 2):** Menguji sampel sepanjang periode waktu (misal 6–12 bulan) untuk membuktikan kontrol dijalankan secara konsisten oleh personel yang berwenang.
4. **Gunakan Bukti Audit Paling Andal (ITAF `1205`):**
   - Utamakan *re-performance*, hasil ekstraksi CAATs/SQL langsung oleh auditor, observasi langsung, dan konfigurasi sistem di atas pernyataan lisan (*inquiry*).
5. **Susun Temuan Audit dalam Format Baku 5C ISACA (ITAF `1401`):**
   - Setiap temuan wajib menguraikan secara tajam: **(1) Condition** (fakta & bukti kuantitatif), **(2) Criteria** (standar ITAF / SOXIT / CISA / kebijakan), **(3) Cause** (akar penyebab), **(4) Consequence / Effect** (dampak & risiko bisnis/keuangan), dan **(5) Corrective Action / Recommendation** beserta **Management Response, Action Owner, dan Target Date**.
6. **Lengkapi dengan Crosswalk Multi-Framework bila Relevan:**
   - Hubungkan temuan CISA (`Domain 1–5`, `ITAF`, `SOXIT.01–04`) dengan objektif **COBIT 2019** (`EDM`, `APO`, `BAI`, `DSS`, `MEA`), **ISO/IEC 27001:2022**, atau regulasi terkait (SOX 404, UU PDP, POJK) agar rekomendasi bernilai strategis bagi manajemen eksekutif dan Komite Audit.
