#!/usr/bin/env python3
"""
IT Auditor Master Suite Orchestrator CLI (audit_suite_cli.py)
Unifies and searches across all 3 core domains:
1. cobit-it-auditor (ISACA COBIT 2019 — 40 Objectives, 231 Practices, 1,202 Activities, 13 Book Chapters)
2. cisa-it-auditor (ISACA CISA 27e/28e, ITAF 4e, IIA Sampling, 18 SOXIT Controls, 13 Book Chapters)
3. id-it-regulatory-auditor (Indonesian Regulations: POJK 11/2022, SEOJK 29/2022, BUMN PER-2/2023, Indeks KAMI v5, UU PDP 27/2022, SPBE 59/2020, 5 Book Chapters)
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

SUITE_SKILLS = [
    {
        "name": "cobit-it-auditor",
        "title": "ISACA COBIT 2019 Master Handbook & Engine",
        "path": SKILLS_ROOT / "cobit-it-auditor",
        "db": SKILLS_ROOT / "cobit-it-auditor" / "data" / "cobit2019_database.json",
        "cli": SKILLS_ROOT / "cobit-it-auditor" / "scripts" / "cobit_cli.py",
    },
    {
        "name": "cisa-it-auditor",
        "title": "ISACA CISA 27e/28e, ITAF 4e, IIA Sampling & SOX/ITGC Engine",
        "path": SKILLS_ROOT / "cisa-it-auditor",
        "db": SKILLS_ROOT / "cisa-it-auditor" / "data" / "cisa_database.json",
        "cli": SKILLS_ROOT / "cisa-it-auditor" / "scripts" / "cisa_cli.py",
    },
    {
        "name": "id-it-regulatory-auditor",
        "title": "Indonesian IT Regulatory Auditor (OJK, BUMN, BSSN KAMI v5, UU PDP, SPBE)",
        "path": SKILLS_ROOT / "id-it-regulatory-auditor",
        "db": SKILLS_ROOT / "id-it-regulatory-auditor" / "data" / "id_regulations_database.json",
        "cli": SKILLS_ROOT / "id-it-regulatory-auditor" / "scripts" / "id_reg_cli.py",
    },
    {
        "name": "it-auditor-master",
        "title": "Unified CAE Orchestrator & MCP Knowledge Graph Router",
        "path": SKILLS_ROOT / "it-auditor-master",
        "db": None,
        "cli": Path(__file__).resolve(),
    },
]


def cmd_status(_args):
    print("=" * 92)
    print("  IT AUDITOR MASTER SUITE — ECOSYSTEM INVENTORY & HEALTH STATUS")
    print("=" * 92)
    total_chapters = 0
    total_db_bytes = 0
    for s in SUITE_SKILLS:
        ref_dir = s["path"] / "references"
        chapters = sorted(ref_dir.glob("*.md")) if ref_dir.exists() else []
        total_chapters += len(chapters)
        db_size = s["db"].stat().st_size if s["db"] and s["db"].exists() else 0
        total_db_bytes += db_size
        print(f"\n[*] Skill : {s['name']} ({s['title']})")
        print(f"    Path  : {s['path']}")
        print(f"    CLI   : {s['cli'].name if s['cli'] else 'N/A'}")
        if db_size > 0:
            print(f"    DB    : {s['db'].name} ({db_size:,} bytes)")
        if chapters:
            print(f"    Books : {len(chapters)} Reference Chapters:")
            for ch in chapters:
                print(f"            - {ch.name}")
    print("\n" + "=" * 92)
    print(f"TOTAL SUITE CAPACITY: {len(SUITE_SKILLS)} Integrated Skills | {total_chapters} Book Chapters | {total_db_bytes:,} Bytes Structured JSON Data")
    print("=" * 92)


def cmd_omni_search(args):
    q = args.query
    print("=" * 92)
    print(f"  OMNI-SEARCH ACROSS COBIT 2019 + CISA/SOXIT + INDONESIAN REGULATIONS: '{q}'")
    print("=" * 92)

    # 1. Search COBIT 2019
    cobit_cli = SKILLS_ROOT / "cobit-it-auditor" / "scripts" / "cobit_cli.py"
    if cobit_cli.exists():
        print("\n>>> [1/3] COBIT 2019 Knowledge Base Matches:")
        subprocess.run([sys.executable, str(cobit_cli), "search", q], check=False)

    # 2. Search CISA & SOXIT
    cisa_cli = SKILLS_ROOT / "cisa-it-auditor" / "scripts" / "cisa_cli.py"
    if cisa_cli.exists():
        print("\n>>> [2/3] CISA 27e/28e, ITAF 4e & SOX/ITGC Matches:")
        subprocess.run([sys.executable, str(cisa_cli), "search", "--query", q], check=False)

    # 3. Search Indonesian Regulations
    reg_db_path = SKILLS_ROOT / "id-it-regulatory-auditor" / "data" / "id_regulations_database.json"
    if reg_db_path.exists():
        print("\n>>> [3/3] Indonesian IT Regulations (OJK / BUMN / BSSN / UU PDP / SPBE) Matches:")
        with open(reg_db_path, "r", encoding="utf-8") as f:
            reg_db = json.load(f)
        ql = q.lower()
        found = 0
        for r in reg_db.get("crosswalk_regulations", []):
            blob = json.dumps(r, ensure_ascii=False).lower()
            if ql in blob:
                found += 1
                print(f"  * [{r['id']}] {r['title']} -> COBIT: {', '.join(r['cobit2019_mapping'][:6])} | CISA: {', '.join(r['cisa_mapping'])}")
        if found == 0:
            print("  (No direct keyword hit in summary JSON; check chapters in id-it-regulatory-auditor/references/)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="IT Auditor Master Suite Orchestrator CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_stat = sub.add_parser("status", help="Display inventory and health of all 4 IT Auditor skills, 31 chapters, and 3 databases")
    p_stat.set_defaults(func=cmd_status)

    p_omni = sub.add_parser("omni-search", help="Search simultaneously across COBIT 2019, CISA/SOXIT, and Indonesian Regulations")
    p_omni.add_argument("--query", required=True, help="Search keyword")
    p_omni.set_defaults(func=cmd_omni_search)

    return parser


if __name__ == "__main__":
    parser = build_parser()
    parsed = parser.parse_args()
    parsed.func(parsed)
