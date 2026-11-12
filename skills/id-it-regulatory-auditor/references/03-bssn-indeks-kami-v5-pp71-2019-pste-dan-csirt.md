# Bab 3: Keamanan Siber Nasional — Indeks KAMI BSSN Versi 5.0 (ISO/IEC 27001:2022), PP No. 71 Tahun 2019 (PSTE), dan Peraturan BSSN No. 4/2021

> **Cakupan Materi:** Bab ini mengkodifikasi instrumen evaluasi keamanan informasi nasional yang dikelola oleh **Badan Siber dan Sandi Negara (BSSN)** dan **Kementerian Kominfo (Komdigi)**:
> 1. **Indeks KAMI (Keamanan Informasi) BSSN Versi 5.0** — telah diselaraskan penuh dengan **SNI ISO/IEC 27001:2022**
> 2. **Peraturan Pemerintah Nomor 71 Tahun 2019 (PP PSTE)** tentang *Penyelenggaraan Sistem dan Transaksi Elektronik*
> 3. **Peraturan BSSN Nomor 4 Tahun 2021** tentang *Pedoman Manajemen Keamanan Informasi SPBE dan Standar Teknis dan Prosedur Keamanan SPBE* serta **Peraturan BSSN Nomor 10 Tahun 2020** tentang *CSIRT*.

---

## 3.1 Arsitektur & Metodologi Penilaian Indeks KAMI BSSN Versi 5.0

**Indeks KAMI (Keamanan Informasi) v5.0** adalah alat evaluasi untuk menganalisis tingkat kesiapan (*kelengkapan dan kematangan*) pengamanan informasi di instansi pemerintah, BUMN, maupun penyelenggara Infrastruktur Informasi Vital (**IIV**) berdasarkan **SNI ISO/IEC 27001:2022**.

### A. Tahap 1: Penentuan Kategori Sistem Elektronik (Area I — 10 Pertanyaan)
Sebelum menilai kontrol keamanan, auditor/asesor menghitung **Skor Kategori Sistem Elektronik (SE)** berdasarkan 10 parameter dampak dan ketergantungan TIK (nilai anggaran, jumlah pengguna, kekritisan layanan publik, sensitivitas data, dan keterhubungan jaringan):

| Kategori Sistem Elektronik (SE) | Rentang Skor Area I | Makna Risiko & Target Minimum Kepatuhan |
| :--- | :---: | :--- |
| **1. Kategori Rendah** | **$10 \text{ s.d. } 15$** | Ketergantungan TIK rendah; dampak gangguan terbatas pada internal satuan kerja. Target minimum: **Tingkat Kematangan II**. |
| **2. Kategori Tinggi** | **$16 \text{ s.d. } 34$** | Kegagalan sistem berdampak signifikan pada layanan publik, reputasi, dan kerugian finansial instansi. Target minimum: **Tingkat Kematangan III (*Defined*)** dan **Siap Sertifikasi ISO/IEC 27001**. |
| **3. Kategori Strategis (IIV)** | **$35 \text{ s.d. } 50$** | Sistem elektronik vital nasional (pertahanan, keuangan/perbankan, energi, transportasi, kesehatan nasional). Target wajib: **Tingkat Kematangan III+ s.d. IV (*Managed*)** dan **Wajib Bersertifikat SNI ISO/IEC 27001:2022**! |

---

### B. Tahap 2: Struktur 5 Area Inti + 2 Area Suplemen Indeks KAMI v5.0

Setiap pertanyaan kontrol di dalam Indeks KAMI v5.0 dikelompokkan ke dalam **3 Kategori Tahap Pengamanan** (Kategori **1** = Kerangka Kerja Dasar, Kategori **2** = Efektivitas & Konsistensi, Kategori **3** = Peningkatan Berkelanjutan) dan dinilai berdasarkan **Status Penerapan**:
- `Tidak Dilakukan` (Skor $0$)
- `Dalam Perencanaan` (Skor $1$ pada Kat. 1; Skor $2$ pada Kat. 2; Skor $3$ pada Kat. 3)
- `Dalam Penerapan / Sebagian` (Skor $2$ pada Kat. 1; Skor $4$ pada Kat. 2; Skor $6$ pada Kat. 3)
- `Diterapkan Secara Menyeluruh` (Skor $3$ pada Kat. 1; Skor $6$ pada Kat. 2; Skor $9$ pada Kat. 3)

| Area Evaluasi Indeks KAMI v5.0 | Fokus Pemeriksaan Audit & Pemetaan ISO/IEC 27001:2022 / COBIT 2019 |
| :--- | :--- |
| **Area II: Tata Kelola Keamanan Informasi** | • Keberadaan fungsi/komite keamanan informasi, penetapan peran dan tanggung jawab (**CISO**), kebijakan keamanan informasi tingkat instansi, alokasi anggaran keamanan, dan program audit internal keamanan informasi.<br>• **ISO 27001:2022:** Klausul 4, 5, 7, 9 \| **COBIT 2019:** `EDM03`, `APO01`, `APO13`, `MEA02` |
| **Area III: Pengelolaan Risiko Keamanan Informasi** | • Kerangka kerja manajemen risiko keamanan informasi, identifikasi aset dan pemilik risiko, penilaian kemungkinan & dampak, penetapan ambang batas risiko (*risk appetite*), dan pelaksanaan rencana mitigasi risiko (*Risk Treatment Plan*).<br>• **ISO 27001:2022:** Klausul 6.1, 8.2, 8.3 \| **COBIT 2019:** `EDM03`, `APO12` |
| **Area IV: Kerangka Kerja Keamanan Informasi** | • Dokumentasi kebijakan & SOP operasional keamanan (kontrol akses, enkripsi, pengembangan aman/SDLC, manajemen perubahan, pengelolaan insiden, kelangsungan bisnis/BCP, kepatuhan hukum & privasi), serta tinjauan manajemen.<br>• **ISO 27001:2022:** Klausul 5.2, 7.5, 9.3, 10 & Annex A.5 \| **COBIT 2019:** `APO13`, `BAI06`, `DSS04` |
| **Area V: Pengelolaan Aset Informasi** | • Inventarisasi seluruh aset informasi (data, aplikasi, server, jaringan, fasilitas fisik), penetapan pemilik aset (*Asset Owner*), **klasifikasi & pelabelan informasi**, prosedur penanganan media penyimpanan, penghapusan aman (*secure disposal*), dan pengamanan fisik pusat data.<br>• **ISO 27001:2022:** Annex A.5.9–A.5.14, A.7 (Physical) \| **COBIT 2019:** `APO14`, `BAI09`, `DSS01.05`, `DSS05.05` |
| **Area VI: Teknologi dan Keamanan Informasi** | • Penerapan kontrol teknis: pengamanan jaringan ( segmentasi VLAN, Firewall, IDS/IPS, VPN), pengerasan server (*OS/DB Hardening*), manajemen kerentanan (*VA/Pentest & Patching*), perlindungan *malware/EDR*, pencatatan log terpusat (*SIEM*), enkripsi, dan keamanan pengembangan aplikasi.<br>• **ISO 27001:2022:** Annex A.8 (Technological Controls) \| **COBIT 2019:** `BAI03`, `DSS05` |
| **Area VII (Suplemen): Pengamanan Keterlibatan Pihak Ketiga & Layanan Cloud** | • Evaluasi risiko vendor TI, perjanjian kerahasiaan (NDA), SLA keamanan, audit keamanan pihak ketiga, kedaulatan lokasi data *Cloud*, dan *exit strategy*. *(Catatan: Skor suplemen dihitung dalam persentase kepatuhan tersendiri).*<br>• **ISO 27001:2022:** Annex A.5.19–A.5.23 \| **COBIT 2019:** `APO09`, `APO10` |
| **Area VIII (Suplemen): Pelindungan Data Pribadi (PDP)** | • Kepatuhan terhadap **UU No. 27 Tahun 2022 (UU PDP)**: dasar pemrosesan data pribadi, persetujuan subjek data, *Data Protection Impact Assessment (DPIA)*, enkripsi PII, dan prosedur notifikasi kebocoran data $3 \times 24$ jam.<br>• **ISO 27701 & UU PDP 27/2022** \| **COBIT 2019:** `APO14`, `MEA03` |

---

### C. Ambang Batas Kelulusan (Readiness Status) & Tingkat Kematangan Indeks KAMI (I s.d. V)

Total skor dari **Area II s.d. Area VI** dibandingkan dengan **Kategori Sistem Elektronik (Area I)** untuk menentukan predikat kesiapan sertifikasi **ISO/IEC 27001:2022**:

| Kategori SE (Area I) | Tidak Layak | Pemenuhan Kerangka Kerja Dasar | Cukup Baik | **Baik / Siap Sertifikasi ISO 27001** |
| :--- | :---: | :---: | :---: | :---: |
| **SE Rendah (Skor $10-15$)** | $0 - 174$ | $175 - 312$ | $313 - 535$ | **$\ge 536$** |
| **SE Tinggi (Skor $16-34$)** | $0 - 272$ | $273 - 455$ | $456 - 644$ | **$\ge 645$** |
| **SE Strategis (Skor $35-50$)** | $0 - 333$ | $334 - 535$ | $536 - 709$ | **$\ge 710$** |

#### Lima Tingkat Kematangan Keamanan Informasi BSSN:
- **Tingkat I:** Kondisi Awal (*Initial*)
- **Tingkat I+ s.d. II:** Penerapan Kerangka Kerja Dasar (*Repeatable*)
- **Tingkat II+ s.d. III:** Terdefinisi & Konsisten (*Defined* — Syarat Minimum Kesiapan Sertifikasi ISO/IEC 27001!)
- **Tingkat III+ s.d. IV:** Terkelola dan Terukur (*Managed*)
- **Tingkat IV+ s.d. V:** Optimal (*Optimized*).

---

## 3.2 Peraturan Pemerintah Nomor 71 Tahun 2019 (PP PSTE)

**PP No. 71 Tahun 2019** tentang *Penyelenggaraan Sistem dan Transaksi Elektronik* membagi Penyelenggara Sistem Elektronik (**PSE**) menjadi dua rezim hukum yang sangat krusial bagi auditor TI:

| Dimensi Pengaturan PP 71/2019 | PSE Lingkup Publik *(Pasal 2 ayat 3 — Instansi Pemerintah & Institusi yang Ditunjuk)* | PSE Lingkup Privat *(Pasal 2 ayat 5 — Perusahaan Swasta, E-Commerce, Fintech, SaaS)* |
| :--- | :--- | :--- |
| **1. Kewajiban Pendaftaran PSE** | Wajib melakukan pendaftaran PSE sebelum sistem digunakan oleh publik. | Wajib memiliki tanda daftar PSE Kominfo/Komdigi sebelum beroperasi di Indonesia. |
| **2. Lokasi Pusat Data (Data Center) & DRC** | **Pasal 20 ayat (2) — WAJIB DI INDONESIA:** PSE Lingkup Publik **wajib melakukan pengelolaan, pemrosesan, dan/atau penyimpanan Sistem Elektronik dan Data Elektronik di wilayah Indonesia** (Pusat Data Nasional / PDN), kecuali teknologi penyimpanan belum tersedia di dalam negeri setelah mendapat persetujuan Menteri. | **Pasal 21 ayat (1):** PSE Lingkup Privat dapat mengelola/menyimpan data di dalam atau di luar wilayah Indonesia, **DENGAN SYARAT WAJIB** menjamin efektivitas pengawasan oleh Kementerian/Lembaga dan penegak hukum Indonesia (*kecuali sektor keuangan yang diatur khusus oleh OJK/BI di Pasal 21 ayat 2!*). |
| **3. Sertifikat Keandalan & Keamanan** | Wajib menerapkan standar keamanan informasi (BSSN) dan melakukan **audit kelaikan sistem elektronik secara berkala**. | Wajib memiliki Sertifikat Keandalan dan melindungi ketersediaan, keutuhan, serta kerahasiaan data pengguna. |
| **4. Rekam Jejak Audit (*Audit Trail*)** | **Pasal 18:** Setiap PSE wajib menyimpan dan mengamankan **rekam jejak audit (*audit trail*)** atas seluruh kegiatan penyelenggaraan sistem elektronik untuk keperluan pengawasan, penegakan hukum, penyelesaian sengketa, dan verifikasi. | Sama (Pasal 18 berlaku untuk seluruh PSE Publik maupun Privat). |
