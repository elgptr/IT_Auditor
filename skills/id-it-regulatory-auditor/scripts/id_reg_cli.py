#!/usr/bin/env python3
"""
Indonesian IT Regulatory & Compliance Auditor CLI Engine (id-it-regulatory-auditor)
Zero-dependency Python CLI tool for:
1. SPBE Index Calculator (PermenPANRB No. 59 Tahun 2020 — 4 Domains, 8 Aspects, 47 Indicators)
2. BSSN Indeks KAMI v5.0 Electronic System Category & ISO 27001:2022 Readiness Evaluator
3. OJK Cybersecurity Risk & Maturity Matrix Calculator (POJK 11/2022 & SEOJK 29/SEOJK.03/2022)
4. UU PDP No. 27/2022 Compliance, 72-Hour Breach Notification & Max 2% Fine Calculator
5. Crosswalk Mapper between Indonesian Regulations, COBIT 2019, and CISA Domains/SOXIT.
"""

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR.parent / "data" / "id_regulations_database.json"

# Official SPBE Aspect Weights (PermenPANRB No. 59 Tahun 2020)
SPBE_ASPECTS = [
    {"aspect": 1, "domain": 1, "name": "Kebijakan Internal Tata Kelola SPBE", "weight": 0.130, "indicators": "1-10"},
    {"aspect": 2, "domain": 2, "name": "Perencanaan Strategis SPBE", "weight": 0.100, "indicators": "11-14"},
    {"aspect": 3, "domain": 2, "name": "Teknologi Informasi dan Komunikasi (TIK)", "weight": 0.100, "indicators": "15-18"},
    {"aspect": 4, "domain": 2, "name": "Penyelenggara SPBE", "weight": 0.050, "indicators": "19-20"},
    {"aspect": 5, "domain": 3, "name": "Penerapan Manajemen SPBE", "weight": 0.120, "indicators": "21-28"},
    {"aspect": 6, "domain": 3, "name": "Pelaksanaan Audit TIK", "weight": 0.045, "indicators": "29-31"},
    {"aspect": 7, "domain": 4, "name": "Layanan Administrasi Pemerintahan Berbasis Elektronik", "weight": 0.275, "indicators": "32-41"},
    {"aspect": 8, "domain": 4, "name": "Layanan Publik Berbasis Elektronik", "weight": 0.180, "indicators": "42-47"},
]

# Official OJK SEOJK 29/SEOJK.03/2022 Composite Cyber Risk Matrix: [Inherent_Risk 1..5][Maturity_Level 1..5]
# Columns: Maturity 1 (Initial), 2 (Repeatable), 3 (Defined), 4 (Managed), 5 (Optimized)
OJK_CYBER_MATRIX = {
    1: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1},
    2: {1: 3, 2: 3, 3: 2, 4: 2, 5: 1},
    3: {1: 4, 2: 4, 3: 3, 4: 2, 5: 2},
    4: {1: 5, 2: 4, 3: 4, 4: 3, 5: 2},
    5: {1: 5, 2: 5, 3: 4, 4: 3, 5: 3},
}

OJK_RISK_LABELS = {
    1: "1 — Low (Rendah)",
    2: "2 — Low to Moderate (Rendah ke Sedang)",
    3: "3 — Moderate (Sedang)",
    4: "4 — Moderate to High (Sedang ke Tinggi)",
    5: "5 — High (Tinggi - Membutuhkan Tindakan Pengawasan Segera!)",
}


def load_db() -> dict:
    if not DB_PATH.exists():
        sys.stderr.write(f"Error: Database not found at {DB_PATH}\n")
        sys.exit(1)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_spbe_calc(args):
    scores_raw = [float(x.strip()) for x in args.aspect_scores.split(",") if x.strip()]
    if len(scores_raw) != 8:
        sys.stderr.write("Error: --aspect-scores must provide exactly 8 comma-separated numbers (1.0 to 5.0) for Aspek 1..8.\n")
        sys.exit(1)

    print("=== Kalkulator Indeks SPBE Resmi (PermenPANRB No. 59 Tahun 2020 — 4 Domain, 8 Aspek, 47 Indikator) ===")
    domain_weighted = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}
    domain_weights = {1: 0.130, 2: 0.250, 3: 0.165, 4: 0.455}
    total_index = 0.0

    for idx, asp in enumerate(SPBE_ASPECTS):
        sc = max(1.0, min(5.0, scores_raw[idx]))
        w_contrib = sc * asp["weight"]
        domain_weighted[asp["domain"]] += w_contrib
        total_index += w_contrib
        print(f"  * Aspek {asp['aspect']} ({asp['name']:<54} | Ind {asp['indicators']:<5} | Bobot {asp['weight']*100:>5.1f}%): Skor={sc:.2f} -> Kontribusi={w_contrib:.3f}")

    print("-" * 100)
    for d in range(1, 5):
        dom_idx = domain_weighted[d] / domain_weights[d]
        print(f"  Domain {d} Index (Bobot {domain_weights[d]*100:>4.1f}%) : {dom_idx:.2f} / 5.00")

    if total_index >= 4.20:
        predikat = "MEMUASKAN (4.20 - 5.00)"
    elif total_index >= 3.50:
        predikat = "SANGAT BAIK (3.50 - <4.20)"
    elif total_index >= 2.60:
        predikat = "BAIK (2.60 - <3.50)"
    elif total_index >= 1.80:
        predikat = "CUKUP (1.80 - <2.60)"
    else:
        predikat = "KURANG (< 1.80)"

    print("=" * 100)
    print(f"NILAI INDEKS SPBE AKHIR : {total_index:.2f} / 5.00   -->   PREDIKAT: {predikat}")


def cmd_kami_calc(args):
    se_score = args.se_score
    total_score = args.security_score

    if se_score <= 15:
        se_cat = "RENDAH (Skor 10 - 15)"
        thresholds = (175, 313, 536)
    elif se_score <= 34:
        se_cat = "TINGGI (Skor 16 - 34)"
        thresholds = (273, 456, 645)
    else:
        se_cat = "STRATEGIS / IIV (Skor 35 - 50)"
        thresholds = (334, 536, 710)

    if total_score < thresholds[0]:
        status = "TIDAK LAYAK"
    elif total_score < thresholds[1]:
        status = "PEMENUHAN KERANGKA KERJA DASAR"
    elif total_score < thresholds[2]:
        status = "CUKUP BAIK"
    else:
        status = "BAIK (SIAP SERTIFIKASI SNI ISO/IEC 27001:2022)"

    print("=== Evaluasi Indeks KAMI BSSN Versi 5.0 (SNI ISO/IEC 27001:2022) ===")
    print(f"Skor Area I (Kategori Sistem Elektronik) : {se_score} / 50  -->  Kategori SE: {se_cat}")
    print(f"Total Skor Area II-VI (Pengamanan)       : {total_score}")
    print(f"Ambang Batas Sertifikasi ISO 27001       : >= {thresholds[2]} (Kerangka Dasar >= {thresholds[0]}, Cukup Baik >= {thresholds[1]})")
    print(f"Predikat Kesiapan Indeks KAMI BSSN       : {status}")


def cmd_ojk_cyber(args):
    ir = max(1, min(5, args.inherent_risk))
    mat = max(1, min(5, args.maturity_level))
    comp = OJK_CYBER_MATRIX[ir][mat]

    print("=== Penilaian Tingkat Risiko & Maturitas Keamanan Siber Bank (SEOJK No. 29/SEOJK.03/2022) ===")
    print(f"Tingkat Risiko Inheren Siber (1-5)       : {OJK_RISK_LABELS[ir]}")
    print(f"Tingkat Maturitas Keamanan Siber (1-5)   : Level {mat}")
    print(f"Peringkat Risiko Siber Komposit (TKS)    : {OJK_RISK_LABELS[comp]}")
    print("Kewajiban Pelaporan Insiden Siber OJK    : Notifikasi Awal maks 24 Jam | Laporan Lengkap maks 5 Hari Kerja.")


def cmd_uupdp_check(args):
    rev = args.annual_revenue
    hours = args.hours_since_breach
    max_fine = rev * 0.02

    print("=== Evaluasi Kepatuhan & Eksposur Sanksi UU No. 27 Tahun 2022 (UU PDP) ===")
    print(f"Pendapatan Tahunan Korporasi             : Rp {rev:,.2f}")
    print(f"Batas Maksimum Denda Administratif (2%)  : Rp {max_fine:,.2f}  [Pasal 57 ayat (2) huruf d & ayat (3)]")
    print(f"Waktu Sejak Kebocoran Data Diketahui     : {hours:.1f} Jam (Batas Hukum Pasal 46: maksimal 3x24 Jam = 72.0 Jam)")
    if hours > 72.0:
        print(f"Status Kepatuhan Pasal 46 UU PDP         : PELANGGARAN BATAS WAKTU (+{hours - 72.0:.1f} jam melewati batas 72 jam!)")
    else:
        print(f"Status Kepatuhan Pasal 46 UU PDP         : DALAM BATAS WAKTU (Sisa waktu notifikasi tertulis: {72.0 - hours:.1f} jam)")

    if args.specific_data or args.large_scale:
        print("Kewajiban Tambahan (Pasal 34 & Pasal 53) : WAJIB melaksanakan DPIA (Data Protection Impact Assessment) dan WAJIB menunjuk DPO (Data Protection Officer)!")


def cmd_crosswalk(args):
    db = load_db()
    q = args.reg.strip().upper()
    regs = db.get("crosswalk_regulations", [])
    if q != "ALL":
        regs = [r for r in regs if q in r["id"].upper() or q in r["title"].upper() or q in r["sector"].upper()]

    for r in regs:
        print(f"=== [{r['id']}] {r['title']} ===")
        print(f"Sektor Target : {r['sector']}")
        print("Mandat Utama Regulasi:")
        for m in r["key_mandates"]:
            print(f"  * {m}")
        print(f"Pemetaan COBIT 2019 : {', '.join(r['cobit2019_mapping'])}")
        print(f"Pemetaan CISA       : {', '.join(r['cisa_mapping'])}")
        print("-" * 80)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Indonesian IT Regulatory & Compliance Auditor CLI (OJK, BUMN, BSSN KAMI, UU PDP, SPBE)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_spbe = sub.add_parser("spbe-calc", help="Calculate Official SPBE Index (PermenPANRB 59/2020) from 8 Aspect scores")
    p_spbe.add_argument("--aspect-scores", required=True, help="8 comma-separated scores (1.0-5.0) for Aspek 1..8, e.g. '3.5,3.2,3.8,3.0,3.4,3.0,4.0,3.8'")
    p_spbe.set_defaults(func=cmd_spbe_calc)

    p_kami = sub.add_parser("kami-calc", help="Evaluate BSSN Indeks KAMI v5.0 Electronic System Category & ISO 27001 Readiness")
    p_kami.add_argument("--se-score", type=int, required=True, help="Area I Electronic System Score (10 to 50)")
    p_kami.add_argument("--security-score", type=int, required=True, help="Total Security Score across Area II-VI")
    p_kami.set_defaults(func=cmd_kami_calc)

    p_ojk = sub.add_parser("ojk-cyber", help="Calculate OJK Bank Composite Cyber Risk Rating (SEOJK 29/SEOJK.03/2022)")
    p_ojk.add_argument("--inherent-risk", type=int, choices=[1, 2, 3, 4, 5], required=True)
    p_ojk.add_argument("--maturity-level", type=int, choices=[1, 2, 3, 4, 5], required=True)
    p_ojk.set_defaults(func=cmd_ojk_cyber)

    p_pdp = sub.add_parser("uupdp-check", help="Evaluate UU PDP No. 27/2022 72-Hour Breach SLA, DPIA/DPO Trigger & Max 2% Fine")
    p_pdp.add_argument("--annual-revenue", type=float, default=100000000000.0, help="Annual revenue in IDR")
    p_pdp.add_argument("--hours-since-breach", type=float, default=24.0, help="Hours elapsed since data breach discovery")
    p_pdp.add_argument("--specific-data", action="store_true", help="Processes specific/sensitive personal data (Pasal 4 ayat 2)")
    p_pdp.add_argument("--large-scale", action="store_true", help="Processes large-scale personal data")
    p_pdp.set_defaults(func=cmd_uupdp_check)

    p_cw = sub.add_parser("crosswalk", help="Lookup Indonesian IT Regulation mandates & COBIT 2019 / CISA mapping")
    p_cw.add_argument("--reg", default="ALL", help="ALL, POJK, SEOJK, BUMN, KAMI, PDP, or SPBE")
    p_cw.set_defaults(func=cmd_crosswalk)

    return parser


if __name__ == "__main__":
    parser = build_parser()
    parsed = parser.parse_args()
    parsed.func(parsed)
