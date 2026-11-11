#!/usr/bin/env python3
"""
COBIT 2019 Advanced IT Auditor & Governance Engine CLI (cobit_cli.py)
Zero-dependency Python CLI powered by data/cobit2019_database.json (40 Objectives, 231 Practices, 1,202 Activities, 33 Roles).
"""
import argparse
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "data", "cobit2019_database.json")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def load_db():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

PAIN_POINTS_MAP = {
    "PP01": ("Frustrasi unit bisnis atas proyek TI yang gagal/terlambat/over-budget", ["EDM02", "APO05", "APO08", "BAI01", "BAI02", "BAI03", "BAI11"]),
    "PP02": ("Insiden keamanan siber signifikan (ransomware/kebocoran data) atau downtime berulang", ["EDM03", "APO12", "APO13", "DSS02", "DSS03", "DSS04", "DSS05"]),
    "PP03": ("Masalah pengiriman layanan dari vendor / outsourcer / Cloud", ["APO09", "APO10", "DSS01", "MEA01", "MEA03"]),
    "PP04": ("Ketidakpatuhan regulasi (UU PDP, POJK, SPBE) atau temuan audit berulang", ["EDM01", "EDM03", "APO01", "MEA02", "MEA03", "MEA04"]),
    "PP05": ("Pengeluaran TI tersembunyi (Shadow IT) dan duplikasi proyek/aplikasi", ["EDM01", "EDM02", "APO03", "APO05", "APO06", "APO08", "BAI09"]),
    "PP06": ("Kekurangan SDM TI, burnout, turnover tinggi, key-person dependency", ["EDM04", "APO01", "APO07", "BAI08"]),
    "PP07": ("Board/Eksekutif enggan terlibat dalam TI atau model keputusan TI kabur", ["EDM01", "EDM02", "EDM05", "APO01", "APO08"]),
    "PP08": ("Biaya TI sangat tinggi/membengkak tanpa transparansi nilai bisnis", ["EDM02", "EDM04", "APO05", "APO06", "BAI04", "BAI09"]),
    "PP09": ("Arsitektur TI kaku/legacy menghambat inovasi dan ketangkasan bisnis", ["APO02", "APO03", "APO04", "BAI02", "BAI03", "BAI06"]),
    "PP10": ("Masalah kualitas data, laporan tidak sinkron, dan risiko privasi data", ["APO03", "APO14", "DSS06", "MEA01"])
}

SOD_RULES = [
    ("SOD-01", {"Board", "Executive Committee"}, {"Chief Information Officer", "Head IT Operations", "Head Development"}, "Governance vs Management Self-Oversight Conflict (EDM vs APO/BAI/DSS)"),
    ("SOD-02", {"Head Development"}, {"Head IT Operations"}, "Developer Access to Production / Uncontrolled Deployment Risk (BAI03 vs BAI06/DSS01)"),
    ("SOD-03", {"Chief Information Officer", "Head IT Operations"}, {"Chief Information Security Officer", "Information Security Manager"}, "IT Operations vs Security Independence Conflict (DSS01 vs APO13/DSS05)"),
    ("SOD-04", {"Chief Information Officer", "Head IT Operations", "Head Development"}, {"Audit", "Compliance"}, "Assurance Independence Violation: Management Controlling Internal Audit (MEA04)"),
    ("SOD-05", {"Data Management Function", "Head IT Operations"}, {"Information Security Manager", "Privacy Officer"}, "Database/Ops Admin vs Security/Privacy Monitoring Conflict (APO14/DSS01 vs DSS05)")
]

def rating_iso33000(score_pct):
    if score_pct <= 15:
        return "N (Not Achieved: 0-15%)"
    elif score_pct <= 50:
        return "P (Partially Achieved: >15-50%)"
    elif score_pct <= 85:
        return "L (Largely Achieved: >50-85%)"
    return "F (Fully Achieved: >85-100%)"

def cmd_lookup(args, db):
    target = args.id.strip().upper()
    objs = db["objectives"]
    egs = {e["id"]: e for e in db["enterprise_goals"]}
    ags = {a["id"]: a for a in db["alignment_goals"]}

    if target in objs:
        o = objs[target]
        print(f"=== [{o['id']}] {o['name']} ===")
        print(f"Area   : {o['area']} | Domain: {o['domain']} | Official PDF Pages: {o['page_start']}-{o['page_end']}")
        print(f"Desc   : {o['description']}")
        print(f"Purpose: {o['purpose']}")
        print(f"Primary EG: {', '.join(o['primary_enterprise_goals'])}")
        print(f"Primary AG: {', '.join(o['primary_alignment_goals'])} | Secondary AG: {', '.join(o['secondary_alignment_goals'])}")
        print(f"\nPractices ({len(o['practices'])}):")
        for pr in o["practices"]:
            acc = ", ".join(pr["raci"]["accountable"])
            print(f"  - {pr['id']}: {pr['name']} ({len(pr['activities'])} activities | Accountable: {acc})")
        return

    # Check if Practice ID (e.g. DSS04.04)
    for o in objs.values():
        for pr in o["practices"]:
            if pr["id"].upper() == target:
                print(f"=== [{pr['id']}] {pr['name']} (Objective: {o['id']} - {o['name']}) ===")
                print(f"Description: {pr['description']}")
                print(f"Accountable (A): {', '.join(pr['raci']['accountable'])}")
                print(f"Responsible (R): {', '.join(pr['raci']['responsible'])}")
                if pr["example_metrics"]:
                    print("\nExample Metrics:")
                    for m in pr["example_metrics"]:
                        print(f"  * {m}")
                print(f"\nActivities ({len(pr['activities'])}):")
                for a in pr["activities"]:
                    print(f"  [{a['index']}] (Level {a['capability_level']}) {a['text']}")
                if pr["related_guidance"]:
                    print("\nRelated Guidance:")
                    for rg in pr["related_guidance"]:
                        print(f"  - {rg}")
                return

    if target in egs:
        e = egs[target]
        print(f"=== [{e['id']}] {e['name']} (BSC: {e['bsc_dimension']}) ===")
        for m in e["metrics"]:
            print(f"  * {m}")
        return

    if target in ags:
        a = ags[target]
        print(f"=== [{a['id']}] {a['name']} (BSC: {a['bsc_dimension']}) ===")
        for m in a["metrics"]:
            print(f"  * {m}")
        return

    print(f"ID '{args.id}' not found. Use an Objective (EDM01..MEA04), Practice (DSS04.04), EG (EG01..EG13), or AG (AG01..AG13).")

def cmd_cascade(args, db):
    ag_to_eg = db["goals_cascade"]["ag_to_eg"]
    obj_to_ag = db["goals_cascade"]["obj_to_ag"]
    egs = {e["id"]: e for e in db["enterprise_goals"]}
    ags = {a["id"]: a for a in db["alignment_goals"]}
    objs = db["objectives"]

    if args.eg:
        sel_egs = [x.strip().upper() for x in args.eg.split(",") if x.strip()]
        print(f"=== TOP-DOWN GOALS CASCADE FROM ENTERPRISE GOALS: {', '.join(sel_egs)} ===")
        ag_scores = {}
        for ag_id, emap in ag_to_eg.items():
            s = 0
            for eg_id in sel_egs:
                rel = emap.get(eg_id)
                if rel == "P":
                    s += 2
                elif rel == "S":
                    s += 1
            if s > 0:
                ag_scores[ag_id] = s

        print("\n1. Prioritized Alignment Goals (AG):")
        for ag_id, sc in sorted(ag_scores.items(), key=lambda x: -x[1]):
            print(f"   - {ag_id} (Score: {sc:2d}): {ags[ag_id]['name']}")

        obj_scores = {}
        for obj_id, amap in obj_to_ag.items():
            s = 0
            for ag_id, ag_sc in ag_scores.items():
                rel = amap.get(ag_id)
                if rel == "P":
                    s += ag_sc * 2
                elif rel == "S":
                    s += ag_sc * 1
            obj_scores[obj_id] = s

        max_sc = max(obj_scores.values()) if obj_scores else 1
        print("\n2. Top Recommended Governance & Management Objectives (Audit Scope & Target Capability):")
        ranked = sorted(obj_scores.items(), key=lambda x: -x[1])
        for rank, (oid, sc) in enumerate(ranked[:args.top], 1):
            ratio = sc / max_sc if max_sc else 0
            t_lvl = 4 if ratio >= 0.75 else (3 if ratio >= 0.45 else (2 if ratio >= 0.20 else 1))
            print(f"   {rank:2d}. {oid} | Score: {sc:3d} | Target Capability: Level {t_lvl} | {objs[oid]['name']}")

    if args.obj:
        sel_objs = [x.strip().upper() for x in args.obj.split(",") if x.strip()]
        print(f"\n=== BOTTOM-UP BUSINESS RISK ESCALATION FROM OBJECTIVES: {', '.join(sel_objs)} ===")
        impacted_ags = {}
        for oid in sel_objs:
            if oid in obj_to_ag:
                for ag_id, rel in obj_to_ag[oid].items():
                    if rel == "P" or impacted_ags.get(ag_id) != "P":
                        impacted_ags[ag_id] = rel

        print("\n1. Impacted Alignment Goals (AG):")
        impacted_egs = {}
        for ag_id, rel in sorted(impacted_ags.items(), key=lambda x: (0 if x[1] == "P" else 1, x[0])):
            print(f"   - [{rel}] {ag_id}: {ags[ag_id]['name']}")
            print(f"         Key Metric at Risk: {ags[ag_id]['metrics'][0]}")
            if rel == "P":
                for eg_id, erel in ag_to_eg.get(ag_id, {}).items():
                    if erel == "P" or impacted_egs.get(eg_id) != "P":
                        impacted_egs[eg_id] = erel

        print("\n2. Impacted Enterprise Goals (Board-Level Risk / 5C 'Effect'):")
        for eg_id, erel in sorted(impacted_egs.items(), key=lambda x: (0 if x[1] == "P" else 1, x[0])):
            print(f"   - [{erel}] {eg_id} ({egs[eg_id]['bsc_dimension']}): {egs[eg_id]['name']}")
            print(f"         Board Metric at Risk: {egs[eg_id]['metrics'][0]}")

def cmd_raci(args, db):
    objs = db["objectives"]
    if args.role:
        q = args.role.strip().lower()
        for r in db["roles"]:
            if q in r["name"].lower():
                rname = r["name"]
                acc_list = []
                resp_list = []
                for o in objs.values():
                    for pr in o["practices"]:
                        if rname in pr["raci"]["accountable"]:
                            acc_list.append(f"{pr['id']} ({pr['name']})")
                        if rname in pr["raci"]["responsible"]:
                            resp_list.append(pr["id"])
                print(f"=== ROLE: {rname} ===")
                print(f"Description: {r['description']}")
                print(f"Accountable (A) in {len(acc_list)} practices:")
                for item in acc_list:
                    print(f"  * {item}")
                print(f"Responsible (R) in {len(resp_list)} practices: {', '.join(resp_list)}")
    if args.check_sod:
        held_roles = {x.strip() for x in args.check_sod.split(",") if x.strip()}
        print(f"=== SEGREGATION OF DUTIES (SoD) AUDIT CHECK FOR ROLES: {', '.join(held_roles)} ===")
        conflicts = 0
        for code, set_a, set_b, desc in SOD_RULES:
            ma = held_roles.intersection(set_a)
            mb = held_roles.intersection(set_b)
            if ma and mb:
                conflicts += 1
                print(f"  [!] CRITICAL CONFLICT {code}: {desc}")
                print(f"      Conflicting Roles Combined: {', '.join(ma)} <--> {', '.join(mb)}")
        if conflicts == 0:
            print("  [OK] No structural SoD conflict detected among the specified roles.")

def cmd_capability(args, db):
    oid = args.obj.strip().upper()
    if oid not in db["objectives"]:
        print(f"Objective {oid} not found.")
        return
    o = db["objectives"][oid]
    score_map = {}
    if args.scores:
        for pair in args.scores.split(","):
            if ":" in pair:
                lvl_s, pct_s = pair.split(":", 1)
                score_map[int(lvl_s.strip())] = float(pct_s.strip())

    # Count activities per capability level across all practices of the objective
    lvl_acts = {2: [], 3: [], 4: [], 5: []}
    for pr in o["practices"]:
        for act in pr["activities"]:
            lvl_acts.setdefault(act["capability_level"], []).append((pr["id"], act["index"], act["text"]))

    print(f"=== CAPABILITY ASSESSMENT ENGINE: {oid} — {o['name']} ===")
    achieved_level = 1
    gate_open = True
    for lvl in (2, 3, 4, 5):
        acts = lvl_acts.get(lvl, [])
        if not acts:
            continue
        pct = score_map.get(lvl, 0.0)
        rating = rating_iso33000(pct)
        status = "PASSED (>85%)" if (pct > 85.0 and gate_open) else ("BLOCKED BY LOWER LEVEL" if not gate_open else "NOT FULLY ACHIEVED")
        if pct > 85.0 and gate_open:
            achieved_level = lvl
        else:
            gate_open = False
        print(f"  Level {lvl}: {len(acts):2d} activities | Score: {pct:5.1f}% | Rating: {rating} | Gate: {status}")

    print(f"\n>>> OFFICIAL ACHIEVED CAPABILITY LEVEL FOR {oid}: Level {achieved_level} <<<")
    next_lvl = achieved_level + 1
    if next_lvl in lvl_acts and lvl_acts[next_lvl]:
        print(f"\nKey Activities Required to Achieve Level {next_lvl} ({len(lvl_acts[next_lvl])} activities):")
        for pid, idx, txt in lvl_acts[next_lvl][:8]:
            print(f"  - [{pid} Act.{idx}] {txt}")

def cmd_diagnose(args, db):
    objs = db["objectives"]
    if args.pain_points:
        pps = [x.strip().upper() for x in args.pain_points.split(",") if x.strip()]
        rec_objs = []
        print("=== PAIN POINT DIAGNOSTIC & PRIORITY OBJECTIVES ===")
        for pp in pps:
            if pp in PAIN_POINTS_MAP:
                desc, olist = PAIN_POINTS_MAP[pp]
                print(f"  * [{pp}] {desc}")
                print(f"    -> Recommended Objectives: {', '.join(olist)}")
                for o in olist:
                    if o not in rec_objs:
                        rec_objs.append(o)
        print("\nConsolidated Priority Audit/Implementation Scope:")
        for o in rec_objs:
            print(f"  - {o}: {objs[o]['name']}")

def cmd_search(args, db):
    q = args.query.strip().lower()
    print(f"=== SEARCH RESULTS FOR: '{args.query}' ===")
    hits = 0
    for oid, o in db["objectives"].items():
        for pr in o["practices"]:
            haystack = f"{pr['id']} {pr['name']} {pr['description']} {' '.join(pr['example_metrics'])} {' '.join(pr['related_guidance'])}".lower()
            act_matches = [a for a in pr["activities"] if q in a["text"].lower()]
            if q in haystack or act_matches:
                hits += 1
                print(f"  [{pr['id']}] {pr['name']} (Accountable: {', '.join(pr['raci']['accountable'])})")
                for am in act_matches[:3]:
                    print(f"      -> (Level {am['capability_level']}) Act.{am['index']}: {am['text']}")
                if hits >= args.limit:
                    return
    if hits == 0:
        print("  No matches found.")

def main():
    parser = argparse.ArgumentParser(description="COBIT 2019 Advanced IT Auditor & Governance CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_look = sub.add_parser("lookup", help="Look up an Objective (EDM01..MEA04), Practice (DSS04.04), EG, or AG")
    p_look.add_argument("id", help="Identifier to look up")

    p_casc = sub.add_parser("cascade", help="Run Top-Down (EG->AG->Obj) or Bottom-Up (Obj->AG->EG) Goals Cascade")
    p_casc.add_argument("--eg", help="Comma-separated Enterprise Goals (e.g. EG02,EG03,EG06)")
    p_casc.add_argument("--obj", help="Comma-separated Objectives for Bottom-Up risk translation (e.g. DSS04,DSS05)")
    p_casc.add_argument("--top", type=int, default=12, help="Number of top objectives to display")

    p_raci = sub.add_parser("raci", help="Inspect RACI responsibilities or check Segregation of Duties (SoD) conflicts")
    p_raci.add_argument("--role", help="Role name substring (e.g. 'Chief Information Security Officer' or 'Audit')")
    p_raci.add_argument("--check-sod", help="Comma-separated roles held by one person/unit to test for SoD conflicts")

    p_cap = sub.add_parser("capability", help="Calculate CMMI & ISO/IEC 33000 Process Capability Level with Hard Gate")
    p_cap.add_argument("--obj", required=True, help="Objective ID (e.g. DSS04)")
    p_cap.add_argument("--scores", default="2:90,3:70,4:30", help="Level percentage scores, e.g. '2:90,3:70,4:30'")

    p_diag = sub.add_parser("diagnose", help="Diagnose Pain Points (PP01..PP10) into priority COBIT Objectives")
    p_diag.add_argument("--pain-points", required=True, help="Comma-separated Pain Point IDs (e.g. PP02,PP04,PP10)")

    p_srch = sub.add_parser("search", help="Full-text search across all 40 Objectives, 231 Practices, and 1,202 Activities")
    p_srch.add_argument("query", help="Search keyword (e.g. 'ransomware', 'backup', 'ISO/IEC 27001', 'privacy')")
    p_srch.add_argument("--limit", type=int, default=15, help="Max practices to return")

    args = parser.parse_args()
    db = load_db()
    if args.cmd == "lookup":
        cmd_lookup(args, db)
    elif args.cmd == "cascade":
        cmd_cascade(args, db)
    elif args.cmd == "raci":
        cmd_raci(args, db)
    elif args.cmd == "capability":
        cmd_capability(args, db)
    elif args.cmd == "diagnose":
        cmd_diagnose(args, db)
    elif args.cmd == "search":
        cmd_search(args, db)

if __name__ == "__main__":
    main()
