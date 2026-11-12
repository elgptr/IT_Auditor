# Bab 12: Pembaruan Kurikulum CISA 28th Edition (2024–2026) — Audit Sistem AI/LLM, Zero Trust, dan Playbook Audit Ketahanan Ransomware

> **Cakupan Materi:** Bab ini mengkodifikasi materi pembaruan silabus **ISACA CISA Job Practice (28th Edition)** yang menitikberatkan pada risiko teknologi mutakhir:
> 1. **Auditing Artificial Intelligence (AI), Machine Learning (ML), & Large Language Models (LLM)**
> 2. **Auditing Zero Trust Architecture (ZTA) & Cloud-Native Environments**
> 3. **Playbook Audit Kesiapsiagaan & Pemulihan Ransomware (*Ransomware Readiness & Resilience Audit*)**
> 4. **Auditing Blockchain, Smart Contracts, & IoT/OT Industrial Systems**.

---

## 12.1 Mengaudit Sistem Artificial Intelligence (AI), Machine Learning, dan LLM

Dalam ujian dan praktik audit CISA modern, sistem AI tidak lagi diperlakukan sebagai kotak hitam yang kebal audit. Auditor SI wajib mengevaluasi kontrol di sepanjang **Siklus Hidup Sistem AI (*AI System Lifecycle*)**:

```
[1. Data Acquisition & Prep] ──► [2. Model Training & Validation] ──► [3. Deployment & Guardrails] ──► [4. Continuous Monitoring]
 • Risiko: Data Poisoning,        • Risiko: Overfitting,               • Risiko: Prompt Injection,      • Risiko: Model Drift,
   Bias Populasi, Pelanggaran       Kurangnya Explainability (XAI),      Hallucination, Data Leakage      Concept Drift,
   Privasi (PII) & Hak Cipta        Manipulasi Bobot Model               via RAG / Shadow AI              Keputusan Otonom Salah
```

### Matriks Ancaman Spesifik AI/LLM & Kontrol Audit CISA

| Ancaman / Risiko Spesifik AI | Definisi & Mekanisme Terjadinya | Kontrol Kunci yang Wajib Diverifikasi oleh IS Auditor |
| :--- | :--- | :--- |
| **1. Data Poisoning** *(Keracunan Data Latih)* | Penyerang menyusupkan sampel data yang telah dimanipulasi ke dalam dataset pelatihan (*training dataset*) untuk merusak perilaku model atau menanamkan *backdoor* tersembunyi. | • Verifikasi integritas sumber data (*Data Provenance & Lineage*), pemeriksaan *hash* dataset, deteksi anomali statistik (*outlier filtering*) sebelum pelatihan, dan kontrol akses ketat pada repositori data latih. |
| **2. Algorithmic Bias & Fairness Risk** *(Bias Algoritmik)* | Model menghasilkan keputusan yang diskriminatif terhadap kelompok demografis tertentu (misal dalam *credit scoring* atau seleksi SDM) karena data historis yang tidak representatif. | • Pengujian keadilan statistik (*Fairness & Disparity Testing*) sebelum dan sesudah implementasi, penghapusan variabel sensitif/proksi, serta peninjauan oleh *AI Ethics Committee*. |
| **3. Overfitting vs. Underfitting** | **Overfitting:** Model terlalu menghafal *noise* pada data latih sehingga tampak 99% akurat saat pelatihan, namun **gagal total saat menghadapi data produksi baru**. | • Memastikan pemisahan tegas antara **Training Set**, **Validation Set**, dan **Independent Holdout Test Set** (data uji tidak boleh bocor ke dalam data latih!). |
| **4. Prompt Injection (Direct & Indirect)** | Penyerang merancang teks input khusus (atau menyembunyikan instruksi di dalam halaman web/dokumen yang dibaca oleh LLM) untuk membajak instruksi sistem LLM dan mengekstrak data rahasia. | • Pemisahan tegas antara instruksi sistem dan data eksternal, pemasangan **LLM Input/Output Guardrails**, serta pembatasan hak akses *tool/API* yang dapat dieksekusi oleh agen AI (*Least Privilege for AI Agents*). |
| **5. Model Hallucination / Confabulation** | LLM menghasilkan informasi palsu atau kutipan fiktif yang terdengar sangat meyakinkan. | • Arsitektur **RAG (*Retrieval-Augmented Generation*)** dengan kutipan sumber terverifikasi, pembatasan suhu (*low temperature*), dan kontrol **Human-in-the-Loop (HITL)** untuk setiap keputusan kritis. |
| **6. Model Drift / Concept Drift** | Akurasi model menurun seiring berjalannya waktu karena pola perilaku dunia nyata di produksi telah berubah dibanding saat model dilatih (misal pola *fraud* baru). | • Pemantauan metrik akurasi model secara berkelanjutan (*Continuous Model Monitoring*) dan prosedur *retraining* terjadwal dengan validasi regresi. |
| **7. Black-Box Opacity (Kurangnya Explainability)** | Manajemen tidak dapat menjelaskan kepada nasabah atau regulator *mengapa* model AI menolak pengajuan kredit mereka. | • Penggunaan teknik **Explainable AI (XAI)** (seperti SHAP/LIME) dan dokumentasi **Model Card** untuk sistem berisiko tinggi. |

---

## 12.2 Playbook Audit Ketahanan terhadap Serangan Ransomware

Serangan **Ransomware Modern (Double/Triple Extortion)** tidak hanya mengenkripsi server produksi, tetapi juga **mencuri data rahasia terlebih dahulu (*exfiltration*)** dan **mengincar sistem backup jaringan (*backup destruction*)** sebelum melancarkan enkripsi massal.

### Daftar Periksa Audit Kesiapsiagaan Ransomware (7 Lapis Pertahanan CISA)

1. **Immutable & Air-Gapped Backups (Aturan Backup 3-2-1-1-0):**
   - **3** salinan data, pada **2** jenis media berbeda, **1** disimpan di lokasi *Offsite/Cloud*, **1** salinan bersifat **Immutable (WORM — *Write-Once-Read-Many* / Object Lock)** atau **Offline (Air-Gapped)** yang **tidak dapat dihapus bahkan oleh akun Domain Admin sekalipun**, dan **0** kesalahan saat diuji *restore* berkala!
2. **Isolasi Kredensial Backup dari Active Directory Produksi:**
   - Konsol manajemen *backup* (misal Veeam/Commvault/Rubrik) **DILARANG bergabung ke dalam domain Active Directory produksi yang sama**! Jika penyerang mengambil alih *Domain Admin*, penyerang tidak boleh otomatis bisa masuk ke server *backup*.
3. **Phishing-Resistant MFA & Privileged Access Management (PAM):**
   - Seluruh akses jarak jauh (VPN, RDP, Citrix, Cloud Console) dan akun *privileged* wajib dilindungi MFA, dan protokol **SMB v1 / RDP eksternal** wajib ditutup.
4. **Endpoint Detection and Response (EDR/XDR) & Least Privilege:**
   - Mencabut hak *Local Administrator* dari laptop pengguna akhir dan memblokir eksekusi *macro Office* dari internet.
5. **Network Micro-Segmentation:**
   - Memisahkan segmen jaringan pengguna, server aplikasi, database, dan sistem cadangan sehingga infeksi di satu komputer staf tidak dapat menyebar secara lateral (*East-West traffic*).

---

## 12.3 Mengaudit Blockchain, Smart Contracts, dan Lingkungan IoT / OT (SCADA/ICS)

| Teknologi | Risiko Spesifik yang Diaudit CISA | Kontrol Kunci yang Wajib Diverifikasi |
| :--- | :--- | :--- |
| **Blockchain & Distributed Ledger (DLT)** | • **51% Attack:** Pada *public blockchain*, jika satu pihak menguasai $>50\%$ daya komputasi/konsensus, ia dapat membalikkan transaksi (*double-spending*).<br>• **Kehilangan Private Key:** Karena sifatnya terdesentralisasi, jika *Private Key* dompet kripto hilang atau dicuri, aset hilang selamanya tanpa bisa di-*reset*. | • Penggunaan **Enterprise Permissioned Blockchain** untuk proses bisnis korporat.<br>• Penyimpanan kunci privat di dalam **HSM (Hardware Security Module)** dengan skema **Multi-Signature (Multi-Sig / $M$-of-$N$ Approval)** agar tidak ada satu orang pun yang bisa memindahkan aset sendirian. |
| **Smart Contracts** | • Karena kode *Smart Contract* yang sudah di-*deploy* ke *blockchain* bersifat **Immutable (tidak dapat diubah)**, adanya celah logika (*bug* seperti *Re-entrancy Attack*) akan langsung dieksploitasi secara permanen. | • **Audit Kode Independen (*Formal Verification & Independent Smart Contract Code Review*)** secara menyeluruh di *Testnet* sebelum *deployment*, serta mekanisme *Circuit Breaker / Pause Function* darurat. |
| **IoT & Operational Technology (OT / ICS / SCADA)** | • Perangkat sensor/industri sering memiliki **password default pabrik yang di-*hardcode***, sistem operasi kuno yang **tidak bisa di-*patch***, dan tidak tahan terhadap pemindaian *vulnerability scanner* aktif (bisa langsung *crash*). | • **Isolasi Jaringan Ketat (Air-Gap / DMZ Industri Purdue Model)** yang memisahkan jaringan IT korporat dari jaringan OT pabrik.<br>• Mengubah seluruh *default password* pabrik sebelum perangkat dipasang.<br>• Menggunakan **Passive Network Monitoring** (bukan *active scanning* yang agresif) pada jaringan OT sensitif. |
