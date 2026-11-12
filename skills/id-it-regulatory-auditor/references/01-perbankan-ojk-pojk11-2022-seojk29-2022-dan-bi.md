# Bab 1: Regulasi TI Perbankan & Jasa Keuangan Indonesia — POJK No. 11/POJK.03/2022, SEOJK No. 29/SEOJK.03/2022, POJK 4/2021, dan BI PJP

> **Cakupan Materi:** Bab ini mengkodifikasi standar audit kepatuhan regulasi teknologi informasi dan keamanan siber sektor perbankan dan jasa keuangan di Indonesia:
> 1. **POJK Nomor 11/POJK.03/2022** tentang *Penyelenggaraan Teknologi Informasi oleh Bank Umum (POJK PTI)*
> 2. **SEOJK Nomor 29/SEOJK.03/2022** tentang *Ketahanan dan Keamanan Siber bagi Bank Umum* (Matriks Risiko Inheren, 4 Fase Ketahanan Siber, Penilaian Maturitas Level 1–5, & Pelaporan Insiden 24 Jam)
> 3. **POJK Nomor 4/POJK.05/2021** tentang *Penerapan Manajemen Risiko dalam Penggunaan TI oleh LJK Non-Bank (LJKNB)*
> 4. **Peraturan Bank Indonesia (PBI No. 23/6/PBI/2021)** tentang *Penyedia Jasa Pembayaran (PJP)* & Standar SNAP BI.

---

## 1.1 Struktur & Mandat Utama POJK Nomor 11/POJK.03/2022 (POJK PTI Bank Umum)

**POJK No. 11/POJK.03/2022** terdiri atas **12 Bab dan 72 Pasal** yang mengatur penyelenggaraan TI secara menyeluruh pada Bank Umum (Konvensional maupun Syariah):

| Bab & Pasal Kunci | Pokok Pengaturan Wajib | Kriteria Pengujian Audit (ToD & ToE) & Pemetaan COBIT 2019 / CISA |
| :--- | :--- | :--- |
| **Bab II (Pasal 2–9): Tata Kelola TI Bank** | • Wewenang & tanggung jawab aktif **Direksi** dan **Dewan Komisaris**.<br>• Kewajiban memiliki **Rencana Strategis TI (RSTI)** jangka panjang yang selaras dengan Rencana Korporasi.<br>• Kewajiban membentuk **Komite Pengarah TI (*IT Steering Committee*)** yang diketuai anggota Direksi dan beranggotakan pimpinan satuan kerja TI & bisnis.<br>• Kewajiban menunjuk pejabat eksekutif penanggung jawab TI. | • **COBIT:** `EDM01`, `APO01`, `APO02`<br>• **CISA:** Domain 2 (`T5`, `T6`)<br>• **Bukti Audit:** Piagam Komite Pengarah TI, Notulen rapat minimal berkala, dokumen RSTI yang disahkan Direksi & dilaporkan ke OJK. |
| **Bab III (Pasal 10–15): Arsitektur TI** | • Bank wajib memiliki dan menerapkan **Arsitektur TI** yang komprehensif (mencakup arsitektur bisnis, data, aplikasi, dan infrastruktur/teknologi) untuk mendukung pemrosesan data yang terintegrasi. | • **COBIT:** `APO03` (*Managed Enterprise Architecture*)<br>• **CISA:** Domain 2 (2.5 EA)<br>• **Bukti Audit:** Dokumen *Enterprise Architecture Blueprint* & peta jalan integrasi sistem. |
| **Bab IV (Pasal 16–29): Manajemen Risiko & Pengamanan Informasi** | • Penerapan manajemen risiko TI (Identifikasi, Pengukuran, Pemantauan, Pengendalian).<br>• Pengamanan informasi pada tahap perencanaan, pengembangan, operasional, dan pemeliharaan.<br>• **Pengendalian akses logis & fisik**, kriptografi, dan pemisahan lingkungan pengembangan vs. produksi. | • **COBIT:** `EDM03`, `APO12`, `APO13`, `DSS05`<br>• **CISA:** Domain 3, 4, 5 (`SOXIT.01`–`04`)<br>• **Bukti Audit:** *IT Risk Register*, kebijakan keamanan informasi, bukti UAT & *segregation of environments*. |
| **Bab V (Pasal 30–34): Ketahanan & Keamanan Siber** | • Bank wajib menjaga ketahanan dan keamanan siber melalui pembentukan **unit/fungsi independen khusus keamanan siber** (terpisah dari fungsi pengembangan & operasional TI!).<br>• Pelaksanaan **pengujian keamanan siber berkala** (*Vulnerability Assessment, Penetration Testing, & Scenario-Based Cyber Exercise*). | • **COBIT:** `APO13`, `DSS02`, `DSS04`, `DSS05`<br>• **CISA:** Domain 5 (`T34`, `T35`)<br>• **Bukti Audit:** Struktur organisasi CISO/Unit Keamanan Siber yang independen dari Kepala Operasional TI; laporan Pentest tahunan. |
| **Bab VI (Pasal 35–42): Pemrosesan Transaksi, Pusat Data (DC), & DRC di Indonesia** | • **Pasal 35 & 39 (Kedaulatan Data On-Shore):** Bank **WAJIB menempatkan Sistem Elektronik pada Pusat Data (*Data Center*) dan Pusat Pemulihan Bencana (*DRC*) di wilayah Indonesia**, serta menyelenggarakan pemrosesan transaksi berbasis TI di wilayah Indonesia!<br>• **Pasal 38:** Penempatan sistem di luar wilayah Indonesia hanya untuk sistem penunjang/analisis global tertentu dan **wajib memperoleh izin tertulis terlebih dahulu dari OJK**.<br>• **Pasal 37 & 40 (DRP):** Bank wajib menyusun **Rencana Pemulihan Bencana (DRP)** dan melakukan **uji coba DRP minimal 1 (satu) kali dalam 1 tahun** atas seluruh aplikasi/sistem kritis. | • **COBIT:** `DSS01`, `DSS04` (*Managed Continuity*), `APO10`<br>• **CISA:** Domain 4 (`SOXIT.04.C2` & `C3`)<br>• **Bukti Audit:** Sertifikasi lokasi fisik DC & DRC di wilayah NKRI, jarak geografis DC–DRC di zona risiko bencana berbeda, serta **Berita Acara Uji Coba DRP (*Live Switchover Test*) tahunan**. |
| **Bab VII (Pasal 43–48): Pengelolaan Data & Pelindungan Data Pribadi** | • Kewajiban menerapkan **Tata Kelola Data (*Data Governance*)** untuk menjamin kualitas, keakuratan, dan keutuhan data.<br>• Persetujuan tertulis nasabah sebelum pertukaran/transfer data pribadi ke pihak ketiga. | • **COBIT:** `APO14` (*Managed Data*)<br>• **CISA:** Domain 5 (Data Classification & Privacy) |
| **Bab VIII (Pasal 49–55): Penyedia Jasa TI (Outsourcing & Cloud)** | • Kontrak dengan Penyedia Jasa TI (termasuk *Cloud Provider*) wajib memuat klausul: **Hak Audit oleh Bank dan OJK (*Right to Audit*)**, kepatuhan hukum Indonesia, SLA, kerahasiaan data, dan *Exit Strategy* (*pengembalian & penghapusan data saat kontrak berakhir*). | • **COBIT:** `APO09`, `APO10`<br>• **CISA:** Domain 2 (`T15`, SOC 2 Type 2) |
| **Bab IX (Pasal 56–59): Layanan Perbankan Digital** | • Keamanan aplikasi *Mobile Banking / Internet Banking / Open API*, autentikasi minimal **Two-Factor Authentication (2FA / MFA)** untuk transaksi finansial. | • **COBIT:** `BAI03`, `DSS05.04`, `DSS06` |
| **Bab X (Pasal 60–65): Audit Intern TI & Pelaporan ke OJK** | • **Pasal 60:** Bank wajib melaksanakan **Audit Intern atas Penyelenggaraan TI minimal 1 (satu) kali dalam 1 tahun** (dan audit eksternal independen sesuai kebutuhan/instruksi OJK).<br>• Pelaporan kondisi terkini TI (tahunan paling lambat **31 Januari**) dan pelaporan insiden TI kritis. | • **COBIT:** `MEA02`, `MEA03`, `MEA04`<br>• **CISA:** Domain 1 (ITAF `1201`–`1402`) |

---

## 1.2 Metodologi Penilaian Ketahanan & Keamanan Siber — SEOJK Nomor 29/SEOJK.03/2022

**SEOJK No. 29/SEOJK.03/2022** menetapkan metodologi kuantitatif dan kualitatif untuk menghitung **Tingkat Risiko Keamanan Siber Bank** yang menjadi komponen penilaian **Risiko Operasional dalam Tingkat Kesehatan Bank (TKS / RBBR)**.

```
[1. Nilai Risiko Inheren Siber (Skala 1–5)]      [2. Nilai Maturitas Keamanan Siber (Skala 1–5)]
  • Faktor: Produk/Layanan Digital,                • 4 Proses Ketahanan Siber (Identifikasi,
    Teknologi & Koneksi Pihak Ketiga,                Perlindungan, Deteksi, Respons & Pemulihan)
    Ancaman & Rekam Jejak Insiden Siber,             + Tata Kelola Keamanan Siber
    Organisasi & SDM
                    │                                              │
                    └──────────────────────┬───────────────────────┘
                                           ▼
                   [Matriks Komposit Tingkat Risiko Siber (1 s.d. 5)]
                   (1 = Low, 2 = Low-to-Moderate, 3 = Moderate, 4 = Moderate-to-High, 5 = High)
```

### A. Empat Parameter Penilaian Risiko Inheren Keamanan Siber
1. **Teknologi, Produk, dan Layanan Perbankan:** Kompleksitas arsitektur, volume transaksi digital, penggunaan *Open API / Cloud / Emerging Tech*.
2. **Ancaman Siber & Insiden Siber:** Frekuensi serangan (DDoS, *malware*, *phishing*), kerugian finansial/reputasi akibat insiden dalam 1 tahun terakhir.
3. **Keterhubungan Eksternal & Pihak Ketiga:** Jumlah integrasi dengan *Fintech*, PJP, vendor *Cloud*, dan akses jaringan jarak jauh (*remote access*).
4. **Organisasi & Sumber Daya Manusia:** Jumlah personel, tingkat perputaran (*turnover*) staf keamanan siber, dan ketergantungan pada tenaga alih daya.

### B. Empat Fase Proses Ketahanan Siber (Cyber Resilience Processes — SEOJK 29/2022)
1. **Identifikasi (*Identification*):** Inventarisasi aset informasi, pemetaan risiko rantai pasok (*supply chain*), dan intelijen ancaman siber (*Cyber Threat Intelligence*).
2. **Perlindungan (*Protection*):** Penerapan kontrol IAM (*Least Privilege*, PAM, MFA), enkripsi data, segmentasi jaringan, *patch management*, dan *secure SDLC*.
3. **Deteksi (*Detection*):** Pemantauan keamanan berkelanjutan **24/7 melalui SOC (Security Operations Center) & SIEM**, deteksi anomali, serta *threat hunting*.
4. **Penanggulangan dan Pemulihan (*Response & Recovery*):** Eksekusi *Cyber Incident Response Plan (CIRP)*, isolasi (*containment*), forensik digital, pemulihan dari *backup*, dan komunikasi krisis.

### C. Skala 5 Level Maturitas Keamanan Siber & Matriks Komposit Risiko Siber OJK

| Level Maturitas Keamanan Siber | Predikat OJK | Kriteria Pencapaian Kapabilitas |
| :---: | :--- | :--- |
| **Level 1** | **Initial / Ad-Hoc** | Kontrol keamanan siber belum terdokumentasi formal, bersifat reaktif saat insiden terjadi. |
| **Level 2** | **Repeatable** | Kebijakan dan prosedur keamanan siber sudah ada namun belum diterapkan secara merata di seluruh lini. |
| **Level 3** | **Defined** *(Target Minimum Standar)* | Seluruh kebijakan, standar, dan prosedur 4 fase ketahanan siber telah terdokumentasi, disahkan Direksi, dan diterapkan secara konsisten di seluruh organisasi. |
| **Level 4** | **Managed** | Pelaksanaan keamanan siber diukur secara kuantitatif menggunakan metrik (KRI/KPI), terintegrasi dengan SIEM/SOAR otomatis, dan diuji secara berkala (*Red Teaming*). |
| **Level 5** | **Optimized** | Peningkatan berkelanjutan berbasis analitik prediktif dan adaptasi *real-time* terhadap ancaman baru (*Zero-Day*). |

#### Matriks Penetapan Tingkat Risiko Siber Komposit (Inherent Risk vs. Cyber Maturity)

| Risiko Inheren \ Tingkat Maturitas | Level 5 (Sangat Kuat / Optimized) | Level 4 (Kuat / Managed) | Level 3 (Memadai / Defined) | Level 2 (Kurang Memadai / Repeatable) | Level 1 (Lemah / Initial) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1 — Rendah (*Low*)** | **1 (Low)** | **1 (Low)** | **1 (Low)** | **2 (Low-Mod)** | **3 (Moderate)** |
| **2 — Rendah ke Sedang (*Low-to-Mod*)** | **1 (Low)** | **2 (Low-Mod)** | **2 (Low-Mod)** | **3 (Moderate)** | **3 (Moderate)** |
| **3 — Sedang (*Moderate*)** | **2 (Low-Mod)** | **2 (Low-Mod)** | **3 (Moderate)** | **4 (Mod-High)** | **4 (Mod-High)** |
| **4 — Sedang ke Tinggi (*Mod-to-High*)** | **2 (Low-Mod)** | **3 (Moderate)** | **4 (Mod-High)** | **4 (Mod-High)** | **5 (High)** |
| **5 — Tinggi (*High*)** | **3 (Moderate)** | **3 (Moderate)** | **4 (Mod-High)** | **5 (High)** | **5 (High)** |

### D. Batas Waktu Pelaporan Insiden Siber ke OJK (Wajib Dihafal Auditor Perbankan!)
1. **Notifikasi Awal Insiden Siber (*Initial Notification*):** Wajib disampaikan kepada OJK paling lambat **24 (dua puluh empat) jam** sejak insiden siber diketahui/dikonfirmasi!
2. **Laporan Insiden Siber Lengkap (*Post-Incident Report*):** Wajib disampaikan secara tertulis kepada OJK paling lambat **5 (lima) hari kerja** setelah insiden siber berhasil ditanggulangi/dipulihkan.
