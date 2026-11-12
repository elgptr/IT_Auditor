---
name: id-it-regulatory-auditor
description: Buku induk dan mesin kalkulasi Audit Kepatuhan Regulasi TI, Tata Kelola, Keamanan Siber, dan Privasi Data Indonesia. Mencakup POJK 11/POJK.03/2022 & SEOJK 29/SEOJK.03/2022 (Perbankan & Siber OJK), Permen BUMN No. PER-2/MBU/03/2023 (Asesmen COBIT 2019 Maturity BUMN), Indeks KAMI BSSN Versi 5.0 (SNI ISO/IEC 27001:2022) & PP 71/2019 (PSTE), UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), serta Perpres 95/2018 & PermenPANRB No. 59 Tahun 2020 (Evaluasi 47 Indikator SPBE) beserta pemetaan crosswalk ke COBIT 2019 dan CISA.
---

# Indonesian IT Regulatory & Compliance Auditor (`id-it-regulatory-auditor`)

Skill ini adalah **Buku Induk Kepatuhan Regulasi TI Nasional Indonesia** sekaligus **Mesin Kalkulasi Indeks Kepatuhan** untuk mengaudit organisasi di Indonesia (Bank Umum, LJK Non-Bank, BUMN & Anak Perusahaan, Kementerian/Lembaga/Pemda, serta PSE Publik/Privat) dan memetakan setiap pasal langsung ke **COBIT 2019** dan **CISA**.

---

## 1. Peta Pustaka Buku Regulasi TI Indonesia (`references/`, `data/`, `scripts/`)

### A. 5 Bab Buku Referensi Regulasi Nasional (`references/`)
- **[Bab 1: Regulasi TI Perbankan & Jasa Keuangan — POJK 11/POJK.03/2022, SEOJK 29/SEOJK.03/2022, POJK 4/2021, & BI PJP](references/01-perbankan-ojk-pojk11-2022-seojk29-2022-dan-bi.md)**
  - Bedah 12 Bab POJK PTI (termasuk kewajiban penempatan **Data Center & DRC di wilayah Indonesia Pasal 35–39** & uji DRP tahunan), matriks penilaian **Risiko Inheren vs. Maturitas Keamanan Siber Level 1–5 (SEOJK 29/2022)**, serta kewajiban notifikasi insiden siber ke OJK dalam **24 Jam** (awal) dan **5 Hari Kerja** (lengkap).
- **[Bab 2: Regulasi Tata Kelola TI BUMN — Permen BUMN No. PER-2/MBU/03/2023 & Asesmen Maturity COBIT 2019 BUMN](references/02-bumn-per2-mbu-2023-cobit-maturity-dan-sinergi.md)**
  - Mandat penyusunan RSTI/Master Plan TI selaras RJPP/RKAP, *IT Steering Committee*, *Enterprise Architecture*, Sinergi & Satu Data BUMN, pembentukan CSIRT BUMN, serta metodologi penilaian **COBIT 2019 Maturity Level BUMN (Target Baseline $\ge 3,00$)**.
- **[Bab 3: Keamanan Siber Nasional — Indeks KAMI BSSN Versi 5.0 (ISO/IEC 27001:2022), PP 71/2019 (PSTE), & Peraturan BSSN No. 4/2021](references/03-bssn-indeks-kami-v5-pp71-2019-pste-dan-csirt.md)**
  - Rumus evaluasi **Kategori Sistem Elektronik (Rendah: 10–15, Tinggi: 16–34, Strategis/IIV: 35–50)**, 6 Area Inti & 2 Suplemen Indeks KAMI v5.0, ambang batas kesiapan sertifikasi SNI ISO/IEC 27001:2022, serta perbedaan kewajiban penempatan pusat data **PSE Lingkup Publik (Pasal 20 PP 71/2019) vs. PSE Lingkup Privat (Pasal 21 PP 71/2019)**.
- **[Bab 4: Audit Kepatuhan UU Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)](references/04-uu-pdp-27-2022-privasi-dpia-dpo-dan-kepatuhan.md)**
  - Klasifikasi Data Pribadi Spesifik vs. Umum (Pasal 4), 7 Dasar Pemrosesan Sah (Pasal 20), SLA **3 x 24 Jam** pemenuhan Hak Subjek Data, kewajiban **ROPA (Pasal 31)**, **DPIA (Pasal 34)**, **DPO (Pasal 53)**, **Notifikasi Tertulis Kebocoran Data 3 x 24 Jam / 72 Jam (Pasal 46)**, aturan 3 tingkat Transfer Data Lintas Batas (Pasal 56), serta **Denda Administratif Maksimal 2% Pendapatan Tahunan (Pasal 57)**.
- **[Bab 5: Evaluasi Sistem Pemerintahan Berbasis Elektronik (SPBE) — Perpres 95/2018 & PermenPANRB No. 59 Tahun 2020 (47 Indikator)](references/05-pemerintahan-spbe-permenpanrb-59-2020-47-indikator.md)**
  - Struktur bobot **4 Domain (Kebijakan 13%, Tata Kelola 25%, Manajemen 16,5%, Layanan 45,5%)**, **8 Aspek**, dan daftar lengkap **47 Indikator Evaluasi SPBE** beserta pemetaan langsung ke objektif COBIT 2019 dan CISA.

---

## 2. Mesin CLI Kepatuhan Regulasi Indonesia (`scripts/id_reg_cli.py`)

Jalankan `scripts/id_reg_cli.py` untuk melakukan perhitungan skor kepatuhan dan *crosswalk* otomatis:

```powershell
# 1. Hitung Nilai Indeks SPBE Resmi (PermenPANRB 59/2020) dari Skor 8 Aspek SPBE
python "C:\Users\erlangga.utama\.agents\skills\id-it-regulatory-auditor\scripts\id_reg_cli.py" spbe-calc --aspect-scores "3.5,3.2,3.8,3.0,3.4,3.0,4.0,3.8"

# 2. Evaluasi Kategori Sistem Elektronik & Kesiapan ISO 27001 pada Indeks KAMI BSSN v5.0
python "C:\Users\erlangga.utama\.agents\skills\id-it-regulatory-auditor\scripts\id_reg_cli.py" kami-calc --se-score 38 --security-score 725

# 3. Hitung Peringkat Risiko Siber Komposit Bank Umum (SEOJK 29/SEOJK.03/2022)
python "C:\Users\erlangga.utama\.agents\skills\id-it-regulatory-auditor\scripts\id_reg_cli.py" ojk-cyber --inherent-risk 4 --maturity-level 2

# 4. Uji Kepatuhan SLA 72 Jam Kebocoran Data & Hitung Denda Maksimal 2% Pendapatan Tahunan (UU PDP No. 27/2022)
python "C:\Users\erlangga.utama\.agents\skills\id-it-regulatory-auditor\scripts\id_reg_cli.py" uupdp-check --annual-revenue 500000000000 --hours-since-breach 80 --specific-data --large-scale

# 5. Tampilkan Crosswalk Regulasi Indonesia ke COBIT 2019 & CISA
python "C:\Users\erlangga.utama\.agents\skills\id-it-regulatory-auditor\scripts\id_reg_cli.py" crosswalk --reg ALL
```
