---
name: it-auditor-master
description: Orkestrator Utama (Chief Audit Executive / CAE Router & Knowledge Graph Engine) yang menggabungkan dan mengoordinasikan seluruh ekosistem skill Audit & Tata Kelola TI: cobit-it-auditor (ISACA COBIT 2019 — 40 Objektif, 1.202 Aktivitas, 11 Design Factors, 7 Fase Implementasi), cisa-it-auditor (ISACA CISA 27e/28e, ITAF 4e, IIA Statistical Sampling, CAATs Benford, SOXIT.01–04 TDE/TOE/PBC, Audit Teknis OS/DB/SAP/AD/Cloud/AI), dan id-it-regulatory-auditor (Regulasi Indonesia: POJK 11/2022, SEOJK 29/2022, BUMN PER-2/2023, Indeks KAMI BSSN v5.0, UU PDP No. 27/2022, & 47 Indikator SPBE) terintegrasi dengan Codebase Memory MCP Knowledge Graph.
---

# IT Auditor Master Orchestrator — Unified CAE Suite (`it-auditor-master`)

Skill ini adalah **Orkestrator Puncak (*Chief Audit Executive / CAE Master Router*)** yang mengintegrasikan **3 Pilar Utama Audit & Tata Kelola TI** ke dalam satu alur kerja terpadu beserta **Memori Pengetahuan Permanen (*Persistent Knowledge Graph*)** melalui `codebase-memory-mcp`:

```
+---------------------------------------------------------------------------------------------------+
|                         IT AUDITOR MASTER ORCHESTRATOR (it-auditor-master)                        |
|                        (Terindeks di Codebase Memory MCP: D:/Projects/IT_auditor)                 |
+---------------------------------------------------------------------------------------------------+
                 │                                       │                                    │
                 ▼                                       ▼                                    ▼
+---------------------------------+   +-----------------------------------+   +-----------------------------------+
| 1. cobit-it-auditor             |   | 2. cisa-it-auditor                |   | 3. id-it-regulatory-auditor       |
| (TATA KELOLA, DESAIN & KAPABILITAS) | (EKSEKUSI AUDIT, SAMPLING & TEKNIS)|   | (KEPATUHAN REGULASI INDONESIA)    |
+---------------------------------+   +-----------------------------------+   +-----------------------------------+
| • 13 Bab Buku COBIT 2019        |   | • 13 Bab Buku CISA 27e/28e & ITAF |   | • 5 Bab Buku Regulasi Nasional    |
| • 40 Objektif, 231 Praktik,     |   | • 5 Domain, 39 Tasks, 17 ITAF     |   | • POJK 11/2022 & SEOJK 29/2022    |
|   1.202 Aktivitas, 33 Peran RACI|   | • 18 SOXIT Key Controls (TDE/TOE) |   | • Permen BUMN PER-2/MBU/03/2023   |
| • 11 Design Factors & 7 Fase    |   | • IIA Sampling, ALE/EVA/PERT      |   | • Indeks KAMI BSSN v5.0 & PP 71   |
| • Focus Areas, AI & Zero Trust  |   | • CAATs Benford, SAP/AD/Cloud/AI  |   | • UU PDP No. 27/2022 & 47 Ind SPBE|
| • Mesin: cobit_cli.py           |   | • Mesin: cisa_cli.py              |   | • Mesin: id_reg_cli.py            |
+---------------------------------+   +-----------------------------------+   +-----------------------------------+
```

---

## 1. Aturan Routing & Kolaborasi Lintas-Skill (Kapan Menggunakan Skill yang Mana?)

Ketika pengguna mengajukan permintaan audit, asesmen, atau konsultasi tata kelola TI, gunakan matriks orkestrasi berikut:

| Skenario Permintaan Pengguna | Skill Utama yang Diaktifkan | Skill Pendamping & Mesin CLI yang Dijalankan Bersama |
| :--- | :--- | :--- |
| **1. Asesmen Maturity / Capability Level TI Korporat atau BUMN, Perancangan Tata Kelola (11 Design Factors), atau Peta Jalan Perbaikan 7 Fase** | **[`cobit-it-auditor`](../cobit-it-auditor/SKILL.md)** | • Jalankan `cobit_cli.py` (`cascade`, `capability`, `raci`, `diagnose`).<br>• Jika klien adalah **BUMN**, gabungkan dengan [`id-it-regulatory-auditor`](../id-it-regulatory-auditor/SKILL.md) (Bab 2: `PER-2/MBU/03/2023`). |
| **2. Perencanaan Fieldwork Audit SI, Penentuan Ukuran Sampel (IIA Sampling), Permintaan Dokumen PBC, Pengujian ITGC/ITAC, Audit Teknis (Unix/Oracle/SQL/SAP/AD/Cloud/AI), atau Persiapan Ujian CISA** | **[`cisa-it-auditor`](../cisa-it-auditor/SKILL.md)** | • Jalankan `cisa_cli.py` (`lookup`, `sampling`, `risk-calc`, `sod-check`, `pbc`, `caats`).<br>• Gunakan [`cobit-it-auditor`](../cobit-it-auditor/SKILL.md) untuk memetakan temuan teknis ke *Alignment Goals (AG)* & *Enterprise Goals (EG)*. |
| **3. Audit Kepatuhan Bank Umum (OJK/BI), Instansi Pemerintah (SPBE), Keamanan Informasi BSSN (Indeks KAMI v5.0), atau Audit Privasi & Kebocoran Data Pribadi (UU PDP No. 27/2022)** | **[`id-it-regulatory-auditor`](../id-it-regulatory-auditor/SKILL.md)** | • Jalankan `id_reg_cli.py` (`spbe-calc`, `kami-calc`, `ojk-cyber`, `uupdp-check`, `crosswalk`).<br>• Gunakan `cisa_cli.py` untuk menguji bukti teknisnya dan `cobit_cli.py` untuk mengukur kapabilitas prosesnya. |
| **4. Penyusunan Laporan Hasil Audit (LHA) Lengkap End-to-End (Segala Medan)** | **Ketiga Skill Sekaligus via [`audit_suite_cli.py`](scripts/audit_suite_cli.py)** | • **Criteria:** Kutip Praktik **COBIT 2019** + Standar **ITAF/SOXIT CISA** + Pasal **Regulasi Indonesia (POJK/UU PDP/SPBE/BUMN)**.<br>• **Condition & Sampling:** Gunakan **IIA Sampling & CAATs CISA**.<br>• **Cause:** Bedah **7 Komponen COBIT 2019** & **Matriks SoD**.<br>• **Consequence:** Kuantifikasi dengan **ALE / Denda 2% UU PDP / Goals Cascade**.<br>• **Corrective Action:** Susun Peta Jalan **COBIT Implementation Guide**. |

---

## 2. Integrasi Memory Base dengan `codebase-memory-mcp`

Seluruh ekosistem repositori **`D:/Projects/IT_auditor`** telah diindeks ke dalam **Codebase Memory MCP Knowledge Graph** (beserta *Architecture Decision Record* / ADR).
- Di awal sesi, panggil `list_projects` atau `manage_adr(project="D:/Projects/IT_auditor", mode="get")` pada server MCP `codebase-memory-mcp` untuk memuat peta memori arsitektur seluruh skill, skrip CLI, dan fungsi kalkulasi secara instan tanpa membebani *context window*.
- Gunakan `search_graph` atau `get_code_snippet` untuk melacak fungsi di dalam `cobit_cli.py`, `cisa_cli.py`, `id_reg_cli.py`, dan `audit_suite_cli.py`.

---

## 3. Mesin Orkestrator Terpadu (`scripts/audit_suite_cli.py`)

Gunakan skrip induk `scripts/audit_suite_cli.py` untuk memeriksa status seluruh ekosistem (31 Bab Buku Referensi + 3 Database JSON + 4 Mesin CLI) atau menjalankan pencarian lintas seluruh kerangka kerja (**COBIT 2019 + CISA + Regulasi Indonesia**) sekaligus dalam satu perintah:

```powershell
# 1. Tampilkan Status Kesehatan & Inventaris Lengkap Ekosistem IT Auditor Suite (31 Bab Buku + 3 Database)
python "C:\Users\erlangga.utama\.agents\skills\it-auditor-master\scripts\audit_suite_cli.py" status

# 2. Pencarian Terpadu Lintas COBIT 2019 + CISA/SOXIT + Regulasi Indonesia (OJK/BUMN/BSSN/UU PDP/SPBE)
python "C:\Users\erlangga.utama\.agents\skills\it-auditor-master\scripts\audit_suite_cli.py" omni-search --query "ransomware"
python "C:\Users\erlangga.utama\.agents\skills\it-auditor-master\scripts\audit_suite_cli.py" omni-search --query "backup"
```
