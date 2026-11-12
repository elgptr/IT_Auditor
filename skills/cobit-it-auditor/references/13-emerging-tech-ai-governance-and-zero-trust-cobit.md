# Bab 13: Tata Kelola Teknologi Baru dengan COBIT 2019 — Artificial Intelligence (AI / GenAI / ISO 42001) dan Zero Trust Architecture (NIST SP 800-207)

> **Cakupan Materi:** Bab ini memetakan bagaimana menggunakan kerangka kerja **COBIT® 2019** untuk mengaudit dan merancang tata kelola atas dua transformasi teknologi paling kritis saat ini:
> 1. **Tata Kelola Artificial Intelligence, Machine Learning, & Generative AI (LLM)** — diselaraskan dengan **ISO/IEC 42001:2023 (AIMS)**, **NIST AI Risk Management Framework (AI RMF 1.0)**, dan **EU AI Act**.
> 2. **Tata Kelola Zero Trust Architecture (ZTA)** — diselaraskan dengan **NIST SP 800-207** dan **CISA Zero Trust Maturity Model**.

---

## 13.1 Tata Kelola & Audit Artificial Intelligence (AI / GenAI) Berbasis COBIT 2019

Adopsi **Machine Learning (ML)** dan **Large Language Models (LLM / Generative AI)** menciptakan risiko baru yang belum pernah ada pada perangkat lunak deterministik tradisional: **Halusinasi (*Hallucination*)**, **Bias Algoritmik (*Algorithmic Bias*)**, **Keracunan Data Latih (*Data Poisoning*)**, **Suntikan Perintah (*Prompt Injection*)**, **Kebocoran Data Rahasia ke Model Publik (*Shadow AI Data Leakage*)**, dan **Pergeseran Model (*Model Drift*)**.

### Pemetaan 10 Objektif COBIT 2019 untuk Tata Kelola & Audit AI (AI Governance Matrix)

| Kode Objektif COBIT 2019 | Praktik Kunci | Kontrol Tata Kelola & Prosedur Audit Spesifik AI / GenAI (Selaras ISO/IEC 42001 & NIST AI RMF) |
| :---: | :---: | :--- |
| **`EDM01` & `EDM03`** *(Governance & Risk Optimization)* | `EDM01.01`<br>`EDM03.02` | • Membentuk **AI Ethics & Governance Committee** lintas fungsi (Hukum, Kepatuhan, Risiko, Data Science, Bisnis).<br>• Menetapkan **Acceptable Use Policy (AUP) untuk Generative AI** (melarang karyawan mengunggah *source code*, data pribadi pelanggan, atau rahasia dagang ke LLM publik yang menggunakan data input untuk melatih model eksternal). |
| **`APO04`** *(Managed Innovation)* | `APO04.03`<br>`APO04.05` | • Mengevaluasi *Proof of Concept (PoC)* penggunaan AI terhadap nilai bisnis nyata, kelayakan etika, dan dampak regulasi sebelum diadopsi secara luas. |
| **`APO12`** *(Managed Risk)* | `APO12.02`<br>`APO12.03` | • Memperbarui *IT Risk Register* dengan **Katalog Risiko Spesifik AI**:<br>  1. *Model Hallucination / Fabrication* (output salah yang tampak meyakinkan)<br>  2. *Algorithmic Bias & Unfairness* (diskriminasi kredit/rekrutmen)<br>  3. *Prompt Injection (Direct & Indirect)*<br>  4. *Training Data Poisoning & Model Extraction*<br>  5. *Intellectual Property / Copyright Infringement*. |
| **`APO14`** *(Managed Data — SANGAT KRITIS!)* | `APO14.01`<br>`APO14.06`<br>`APO14.07`<br>`APO14.08` | • **Data Lineage & Provenance:** Melacak asal-usul, hak cipta, dan izin hukum dari seluruh dataset pelatihan (*training data*) dan dokumen **RAG (*Retrieval-Augmented Generation*)**.<br>• **Data Quality & De-biasing:** Menguji keterwakilan populasi data latih untuk mencegah bias statistik.<br>• **Data Sanitisation & Privacy:** Menghapus/menyamarkan **PII (*Personally Identifiable Information*)** sebelum data dimasukkan ke *training pipeline* atau *vector database*. |
| **`BAI02` & `BAI03`** *(Requirements & Solutions Build)* | `BAI02.01`<br>`BAI03.03`<br>`BAI03.07` | • **Explainability (XAI) & Transparency:** Mewajibkan dokumentasi **Model Cards** (tujuan model, arsitektur, batasan akurasi, metrik keadilan) dan metode penjelasan keputusan (misal SHAP/LIME) untuk model AI berisiko tinggi (seperti *credit scoring* atau diagnosis medis).<br>• **Human-in-the-Loop (HITL):** Merancang kontrol agar keputusan berdampak hukum/finansial tinggi dari AI wajib divalidasi oleh manusia yang berwenang. |
| **`BAI06` & `BAI10`** *(Changes & Configuration)* | `BAI06.01`<br>`BAI10.02` | • **MLOps Versioning:** Mengelola versi bukan hanya pada *source code*, melainkan juga **Versi Dataset Latih, Versi Bobot Model (*Model Weights*), Hyperparameters, dan Sistem Prompt (*Prompt Templates*)** di dalam CMDB/Model Registry. |
| **`DSS05`** *(Managed Security Services)* | `DSS05.01`<br>`DSS05.04` | • **AI Guardrails & Firewall:** Menerapkan filter input/output pada LLM untuk memblokir *Prompt Injection*, *Jailbreaking*, dan kebocoran data sensitif.<br>• **Access Control pada RAG Vector DB:** Memastikan kueri RAG mematuhi **Role-Based Access Control (RBAC)** pengguna yang bertanya (pengguna biasa tidak boleh menarik dokumen rahasia direksi melalui *chatbot* internal!). |
| **`MEA01` & `MEA03`** *(Performance & Compliance)* | `MEA01.03`<br>`MEA03.01` | • **Continuous Model Drift Monitoring:** Memantau degradasi akurasi statistik model di produksi (*Data Drift & Concept Drift*) dan memicu pelatihan ulang (*retraining*) yang terkendali.<br>• Memastikan kepatuhan terhadap **UU PDP No. 27/2022** (hak subjek data atas pemrosesan otomatis/profiling), **ISO/IEC 42001**, dan **EU AI Act**. |

---

## 13.2 Tata Kelola & Audit Zero Trust Architecture (ZTA — NIST SP 800-207) dengan COBIT 2019

Arsitektur keamanan tradisional berbasis perimeter (*Castle-and-Moat* — di mana siapa pun yang sudah masuk ke jaringan LAN internal atau VPN langsung dipercaya) tidak lagi memadai menghadapi serangan *ransomware lateral movement* dan kerja jarak jauh (*hybrid work*). **Zero Trust Architecture (ZTA)** menegakkan prinsip **"Never Trust, Always Verify"** dan **"Assume Breach"**.

### Pemetaan 7 Pilar Zero Trust ke Objektif COBIT 2019

```
+-----------------------------------------------------------------------------------+
|                ARSITEKTUR ZERO TRUST (NIST SP 800-207 & COBIT 2019)               |
+-----------------------------------------------------------------------------------+
|  [Subjek: User/Service] + [Perangkat: Endpoint]                                   |
|            │                                                                      |
|            ▼                                                                      |
|  [Policy Engine (PE) & Policy Administrator (PA)]  ◄── COBIT APO13 / DSS05.04     |
|    • Evaluasi Konteks Dinamis (Identitas + MFA + Kesehatan Perangkat + Lokasi +   |
|      Perilaku Anomali + Klasifikasi Data)                                         |
|            │                                                                      |
|            ▼                                                                      |
|  [Policy Enforcement Point (PEP)] ──► Mengizinkan Akses Per-Sesi & Per-Aplikasi   |
|    • Micro-Segmentation (DSS05.02) & Enkripsi End-to-End (mTLS)                   |
+-----------------------------------------------------------------------------------+
```

| Pilar Zero Trust | Objektif COBIT 2019 | Kriteria Pengujian Audit (*Test of Design & Operating Effectiveness*) |
| :--- | :---: | :--- |
| **1. Identity (Identitas Kuat)** | `DSS05.04`<br>`APO13.02` | • Penggunaan **Phishing-Resistant MFA (FIDO2 / WebAuthn)** untuk seluruh pengguna, terutama akun *privileged*.<br>• Implementasi **Just-In-Time (JIT)** dan **Just-Enough-Access (JEA)** pada *Privileged Access Management (PAM)* (hak admin hanya aktif selama tiket perubahan berlangsung, lalu otomatis dicabut). |
| **2. Devices (Postur Perangkat)** | `DSS05.03`<br>`BAI09` | • Hanya perangkat yang terdaftar di inventaris aset (MDM/EDR), terenkripsi penuh, memiliki *patch* OS terbaru, dan agen EDR aktif yang diizinkan mengakses aplikasi korporat (*Device Health Attestation*). |
| **3. Network Micro-Segmentation** | `DSS05.02`<br>`APO03` | • Menghilangkan jaringan *flat LAN*; menerapkan **Micro-Segmentation** berbasis perangkat lunak (*Software-Defined Perimeter* / VLAN / Firewall antar-workload) sehingga kompromi pada 1 server tidak dapat berpindah secara lateral (*lateral movement*) ke server lain. |
| **4. Applications & Workloads** | `BAI03`<br>`DSS05.03` | • Akses diberikan langsung ke **aplikasi spesifik (ZTNA — Zero Trust Network Access)**, bukan memberikan akses terbuka ke seluruh subnet jaringan melalui VPN tradisional.<br>• Seluruh komunikasi antar-*microservice* menggunakan autentikasi timbal balik terenkripsi (**mTLS**). |
| **5. Data (Perlindungan Berpusat pada Data)** | `APO14`<br>`DSS05.06` | • Klasifikasi data otomatis, penerapan **DLP (Data Loss Prevention)**, enkripsi saat disimpan (*at rest*) dan saat transit (*in transit*), serta manajemen kunci kriptografi (KMS/HSM). |
| **6. Visibility, Analytics & Automation** | `DSS05.07`<br>`MEA01` | • Pemantauan telemetri berkelanjutan melalui **SIEM / SOAR / XDR** dan analisis perilaku pengguna (**UEBA — User and Entity Behavior Analytics**) untuk mencabut sesi secara otomatis jika terdeteksi anomali di tengah sesi aktif. |
