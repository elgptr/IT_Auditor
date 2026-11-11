# IT Auditor & Governance Skills Collection

Kumpulan skill **Enterprise IT Auditor & IT Governance Architect** berstandar **ISACA (COBIT 2019 & CISA)** untuk AI Agent (Antigravity CLI & Claude Code).

---

## 📚 Daftar Skill

### 1. [`cobit-it-auditor`](./skills/cobit-it-auditor/SKILL.md) — *COBIT 2019 Enterprise Edition (Book-Grade Reference + Database + CLI Engine)*
Buku induk ensiklopedis dan mesin analisis audit/tata kelola TI berbasis **COBIT® 2019** (*Framework: Introduction & Methodology*, *Governance & Management Objectives*, *Design Guide*, *Implementation Guide*, dan *COBIT 2019 Toolkit v12*).

#### Fitur & Kemampuan Utama `cobit-it-auditor`:
- **100% Cakupan Model Inti COBIT 2019:** Memuat **40 Governance & Management Objectives** (`EDM01`–`MEA04`), **231 Practices**, **1.202 Activities** lengkap dengan **Capability Level (Level 2–5)**, Contoh Metrik Resmi, Komponen A–G, dan Kertas Kerja Audit (KKA / PBC / ToD & ToE / Red Flags).
- **Mesin Goals Cascade Dua Arah (`Top-Down` & `Bottom-Up`):** Matriks resmi **Figure A.1** (`13 Enterprise Goals` $\leftrightarrow$ `13 Alignment Goals`) dan **Figure A.2** (`13 Alignment Goals` $\leftrightarrow$ `40 Objectives`) untuk penentuan prioritas ruang lingkup audit maupun eskalasi temuan teknis menjadi risiko bisnis Dewan Direksi.
- **11 Design Factors (`DF1`–`DF11`) & Management Awareness Diagnostic:** Mencakup 4 Arketipe Strategi (`DF1`), **19 Kategori Risiko TI (`DF3`)**, **20 Masalah Aktual I&T (`DF4` A–T)**, Lanskap Ancaman, Kepatuhan, Peran TI (*McFarlan Grid*), Model Sourcing, Agile/DevOps, Adopsi Teknologi, Ukuran Perusahaan, serta 7 Parameter Diagnostik Kesadaran Manajemen.
- **Siklus Hidup Implementasi 7 Fase (*COBIT 2019 Implementation Guide*):** Panduan terperinci **Fase 1 s.d. Fase 7** dengan **3 Cincin Konsentris** (*Program Management [PM]*, *Change Enablement [CE]*, *Continual Improvement [CI]*), katalog **10 Pain Points (`PP01`–`PP10`)** & **8 Trigger Events (`TE01`–`TE08`)**, RACI tiap fase, serta template **EGIT Business Case**.
- **Matriks RACI 33 Peran & Deteksi Konflik Segregation of Duties (SoD):** Pemetaan `Accountable (A)` dan `Responsible (R)` untuk seluruh 231 praktik pada **33 Peran Resmi (`Figure A.3`)** dilengkapi **12 Aturan Deteksi Konflik SoD Kritis** (ITGC & ITAC).
- **Multi-Framework & Regulasi Indonesia Crosswalk:** Pemetaan langsung ke ISO/IEC 27001:2022, ISO/IEC 38500, ISO/IEC 20000-1, ISO 22301, NIST CSF 2.0, NIST SP 800-53 Rev. 5, ITIL 4, TOGAF, PMBOK, CIS Controls v8, COSO ERM, **UU No. 27/2022 tentang Pelindungan Data Pribadi (UU PDP)**, **POJK No. 11/POJK.03/2022 & SEOJK 29/2022**, **Perpres No. 95/2018 (SPBE)**, dan **Peraturan BSSN / Indeks KAMI**.
- **Zero-Dependency Python CLI (`scripts/cobit_cli.py`):** Mesin eksekusi langsung untuk `lookup`, `cascade`, `capability` (CMMI + ISO/IEC 33000 *N/P/L/F Hard Gate*), `raci` & `--check-sod`, `diagnose`, dan `search`.

#### Indeks Bab Buku `cobit-it-auditor/references/`:
1. [Bab 1: Fondasi Eksekutif, Prinsip, 7 Komponen & Model Kapabilitas CMMI / ISO 33000](./skills/cobit-it-auditor/references/01-foundations-principles-and-7-components.md)
2. [Bab 2: Mekanisme Goals Cascade, Matriks Figure A.1 & A.2, dan Kamus Metrik EG & AG](./skills/cobit-it-auditor/references/02-goals-cascade-and-metrics-dictionary.md)
3. [Bab 3: Domain EDM (Evaluate, Direct and Monitor) — EDM01 s.d. EDM05](./skills/cobit-it-auditor/references/03-domain-edm-governance-objectives.md)
4. [Bab 4: Domain APO Bagian 1 (Align, Plan and Organize) — APO01 s.d. APO07](./skills/cobit-it-auditor/references/04-domain-apo-management-objectives-part1.md)
5. [Bab 5: Domain APO Bagian 2 (Align, Plan and Organize) — APO08 s.d. APO14](./skills/cobit-it-auditor/references/05-domain-apo-management-objectives-part2.md)
6. [Bab 6: Domain BAI (Build, Acquire and Implement) — BAI01 s.d. BAI11](./skills/cobit-it-auditor/references/06-domain-bai-management-objectives.md)
7. [Bab 7: Domain DSS (Deliver, Service and Support) — DSS01 s.d. DSS06](./skills/cobit-it-auditor/references/07-domain-dss-management-objectives.md)
8. [Bab 8: Domain MEA (Monitor, Evaluate and Assess) — MEA01 s.d. MEA04](./skills/cobit-it-auditor/references/08-domain-mea-management-objectives.md)
9. [Bab 9: COBIT 2019 Design Factors (DF1–DF11), Tailoring & Management Awareness Diagnostic](./skills/cobit-it-auditor/references/09-design-factors-and-tailoring-methodology.md)
10. [Bab 10: COBIT 2019 Implementation Guide — Siklus Hidup 7 Fase (PM, CE, CI) & Business Case](./skills/cobit-it-auditor/references/10-implementation-guide-7-phases-lifecycle.md)
11. [Bab 11: Direktori 33 Peran RACI, Deteksi Konflik SoD, Crosswalk Regulasi & Template Audit 5C/LHA](./skills/cobit-it-auditor/references/11-raci-roles-sod-crosswalk-and-5c-audit-templates.md)

---

### 2. [`cisa-it-auditor`](./skills/cisa-it-auditor/SKILL.md)
Melakukan perancangan pengujian kontrol (*substantive* dan *compliance*), evaluasi IT General Controls (ITGC) & IT Application Controls (ITAC), SDLC, DRP/BCP, dan perlindungan aset informasi berdasarkan **5 Domain CISA (ISACA)** dengan format pelaporan temuan standar (*Condition, Criteria, Cause, Effect, Recommendation*).

---

## 📂 Struktur Repositori

```text
IT_Auditor/
├── README.md
└── skills/
    ├── cobit-it-auditor/
    │   ├── SKILL.md
    │   ├── data/
    │   │   └── cobit2019_database.json
    │   ├── scripts/
    │   │   └── cobit_cli.py
    │   └── references/
    │       ├── 01-foundations-principles-and-7-components.md
    │       ├── 02-goals-cascade-and-metrics-dictionary.md
    │       ├── 03-domain-edm-governance-objectives.md
    │       ├── 04-domain-apo-management-objectives-part1.md
    │       ├── 05-domain-apo-management-objectives-part2.md
    │       ├── 06-domain-bai-management-objectives.md
    │       ├── 07-domain-dss-management-objectives.md
    │       ├── 08-domain-mea-management-objectives.md
    │       ├── 09-design-factors-and-tailoring-methodology.md
    │       ├── 10-implementation-guide-7-phases-lifecycle.md
    │       └── 11-raci-roles-sod-crosswalk-and-5c-audit-templates.md
    └── cisa-it-auditor/
        └── SKILL.md
```
