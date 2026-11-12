#!/usr/bin/env python3
"""
CISA IT Auditor CLI Engine (ISACA CISA 27th Edition / ITAF 4th Edition / IIA Sampling / SOX ITGC)
Zero-dependency Python CLI tool for CISA Domain/Task/ITAF/SOXIT lookup, IIA Statistical Sampling,
Quantitative Risk & Project EVM/PERT Calculation, 12-Role IT Segregation of Duties (SoD) Analysis,
and Prepared-by-Client (PBC) & TDE/TOE Workprogram Generation.
"""

import argparse
import json
import math
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DB_PATH = SCRIPT_DIR.parent / "data" / "cisa_database.json"


def load_db() -> dict:
    if not DB_PATH.exists():
        sys.stderr.write(f"Error: Database not found at {DB_PATH}\n")
        sys.exit(1)
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# Poisson Reliability Factors (R) from IIA Internal Audit Sampling Whitepaper
POISSON_R_TABLE = {
    90: {0: 2.31, 1: 3.89, 2: 5.33, 3: 6.69, 4: 8.00, 5: 9.28},
    95: {0: 3.00, 1: 4.75, 2: 6.30, 3: 7.76, 4: 9.16, 5: 10.52},
    99: {0: 4.61, 1: 6.64, 2: 8.41, 3: 10.05, 4: 11.61, 5: 13.11},
}

# Normal Distribution Z-Scores (Two-Tailed)
NORMAL_Z_TWO_TAILED = {80: 1.282, 85: 1.440, 90: 1.645, 95: 1.960, 98: 2.326, 99: 2.576}

ITGC_RULE_OF_THUMB = {
    "annual": {"population": "1", "sample_size": "1", "examples": "Annual DRP Test, Annual Security Policy Review"},
    "quarterly": {"population": "4", "sample_size": "2", "examples": "Quarterly User Access Review (UAR), Dormant Account Review"},
    "monthly": {"population": "12", "sample_size": "2 - 3", "examples": "Monthly Backup Restoration Test, Capacity Review"},
    "weekly": {"population": "52", "sample_size": "5", "examples": "Weekly Offsite Backup Tape Rotation, Weekly CAB Meeting"},
    "daily": {"population": "250 - 365", "sample_size": "20 - 25", "examples": "Daily Batch Job Monitoring, Daily Backup Log Check"},
    "transactional": {"population": "> 250", "sample_size": "25 - 60", "examples": "New Hire Access Requests, Terminations, Program Change Tickets (RFC)"},
    "automated": {"population": "N/A (System Parameter)", "sample_size": "1 (Sample of One / Benchmarking)", "examples": "OS/DB Password Configuration, Automated Input Edit Check (Requires effective ITGC!)"},
}

BIA_METRICS = [
    {"metric": "RPO", "name": "Recovery Point Objective", "definition": "Maximum acceptable data loss measured in time prior to disaster (determines backup/replication frequency)."},
    {"metric": "RTO", "name": "Recovery Time Objective", "definition": "Maximum acceptable time to restore IT system/application after disaster (determines Hot/Warm/Cold site choice)."},
    {"metric": "WRT", "name": "Work Recovery Time", "definition": "Time required after RTO to verify data integrity, catch up manual backlog, and synchronize databases."},
    {"metric": "MTD / MTO", "name": "Maximum Tolerable Downtime / Outage", "definition": "Total time business can survive without the process before irreparable failure (Rule: RTO + WRT <= MTD)."},
    {"metric": "SDO / MBCO", "name": "Service Delivery Objective", "definition": "Minimum level of operational service required during alternate site mode."},
]

TECHNICAL_GUIDES = {
    "UNIX": [
        ("/etc/passwd & UID=0", "Verify only 'root' has UID=0 (awk -F: '($3==\"0\"){print}' /etc/passwd) and system daemons use /sbin/nologin."),
        ("/etc/shadow & /etc/default/passwd", "Verify password hashes reside in /etc/shadow (0400 root) and PASSLENGTH>=8, MAXWEEKS, MINWEEKS, HISTORY are enforced."),
        ("/etc/default/login & sshd_config", "Verify RETRIES lockout (<=5) and CONSOLE=/dev/console or PermitRootLogin no to prevent direct remote root login."),
        ("/etc/inetd.conf & Services", "Verify insecure cleartext services (Telnet, FTP, rlogin, rsh, finger) are disabled in favor of SSH/SFTP."),
        ("/etc/cron.d/cron.allow & at.allow", "Verify batch job scheduling access is restricted exclusively to authorized administrators/operators."),
    ],
    "ORACLE": [
        ("DBA_USERS", "Inspect all DB accounts; ensure default accounts (SCOTT, DBSNMP, OUTLN, MDSYS) are EXPIRED & LOCKED."),
        ("DBA_PROFILES", "Verify PASSWORD_LIFE_TIME (<=90), FAILED_LOGIN_ATTEMPTS (<=5), PASSWORD_REUSE_MAX, and PASSWORD_VERIFY_FUNCTION (!= NULL)."),
        ("DBA_SYS_PRIVS & DBA_ROLE_PRIVS", "Verify DBA, SYSDBA, SYSOPER, and 'ANY' privileges are restricted to authorized DBAs (no Developers or End Users)."),
        ("DBA_TAB_PRIVS (PUBLIC)", "Ensure the PUBLIC group does NOT have SELECT/INSERT/UPDATE/DELETE privileges on production business tables."),
        ("V$PARAMETER (audit_trail) & DBA_AUDIT_TRAIL", "Verify audit_trail is enabled (DB/OS) and audit_sys_operations=TRUE with protected audit logs."),
        ("SQL Server: sys.sql_logins & xp_cmdshell", "Verify 'sa' is disabled/renamed, is_policy_checked=1, sysadmin role is restricted, and xp_cmdshell=0."),
    ],
    "SAP": [
        ("SU01 / SUIM & Table USR02", "Extract active users, lock status (UFLAG), user types (USTYP), validity dates, and last logon (TRDAT) to detect dormant/terminated users."),
        ("Table UST04 & AGR_USERS", "Identify all accounts holding SAP_ALL, SAP_NEW, S_TABU_DIS (02), S_DEVELOP (01/02 in Prod), or S_USER_GRP."),
        ("SCC4 & Table T000", "Verify Production Client is closed to direct changes (CCCORACTIV = 2 'No changes allowed')."),
        ("RZ10 / RZ11 / RSPARAM", "Verify login/min_password_lng (>=8), login/password_expiration_time (<=90), login/fails_to_user_lock (<=5), login/no_automatic_user_sapstar (1)."),
        ("STMS & Table E070", "Extract 100% of production transports; verify Developer != Importer (SoD on S_CTS_ADMI) and verify UAT sign-off."),
        ("SM19 / SM20 & Firefighter", "Verify Security Audit Log is active and all Emergency/FireCall sessions have post-session supervisory sign-off."),
    ],
}

ROLE_ALIASES = {
    "dev": "Application Programmer / Developer",
    "developer": "Application Programmer / Developer",
    "programmer": "Application Programmer / Developer",
    "operator": "Computer Operator (Production)",
    "ops": "Computer Operator (Production)",
    "sec": "Security Administrator",
    "security": "Security Administrator",
    "security_admin": "Security Administrator",
    "dba": "Database Administrator (DBA)",
    "sysadmin": "System Administrator / Systems Programmer",
    "system_admin": "System Administrator / Systems Programmer",
    "librarian": "Librarian / Change Migration Control",
    "change_control": "Librarian / Change Migration Control",
    "qa": "Quality Assurance (QA) / Tester",
    "user": "End User / Business Data Owner",
    "end_user": "End User / Business Data Owner",
    "business": "End User / Business Data Owner",
    "auditor": "IS Auditor",
    "analyst": "Systems Analyst",
    "system_analyst": "Systems Analyst",
    "network": "Network Administrator",
    "network_admin": "Network Administrator",
    "helpdesk": "Help Desk / Service Desk",
    "help_desk": "Help Desk / Service Desk",
}

SOD_RULES = [
    {
        "pair": ("Application Programmer / Developer", "Computer Operator (Production)"),
        "severity": "CRITICAL",
        "risk": "Developer with production operations access can insert unauthorized code (backdoor/Trojan/fraud logic), execute it directly against live data, and conceal evidence.",
        "compensating_control": "Revoke developer write/operational access in production; implement controlled Emergency/FireCall ID with formal approval and 100% independent review of production activity & job logs.",
    },
    {
        "pair": ("Application Programmer / Developer", "Librarian / Change Migration Control"),
        "severity": "CRITICAL",
        "risk": "Developer can promote/transport untested or unauthorized code changes directly into production without business UAT sign-off or CAB approval.",
        "compensating_control": "Restrict transport/deployment permissions (e.g., SAP STMS / CI-CD deploy) exclusively to an independent Librarian/Basis Admin, and reconcile production object timestamps/hashes against approved RFC tickets.",
    },
    {
        "pair": ("Application Programmer / Developer", "Security Administrator"),
        "severity": "CRITICAL",
        "risk": "Developer can grant themselves superuser privileges in production and modify both application logic and access control lists.",
        "compensating_control": "Strict separation of Security Administration; independent periodic User Access Review (UAR) by Business Data Owners and immutable SIEM logging of all user/role changes.",
    },
    {
        "pair": ("Application Programmer / Developer", "Database Administrator (DBA)"),
        "severity": "HIGH",
        "risk": "Developer can modify production database schemas and manipulate raw production tables bypassing application edit controls.",
        "compensating_control": "Restrict developer access to read-only or non-production databases; log all DDL/DML queries executed by DBA accounts on an independent syslog/SIEM server.",
    },
    {
        "pair": ("Application Programmer / Developer", "End User / Business Data Owner"),
        "severity": "CRITICAL",
        "risk": "Individual can design/alter system logic AND initiate/approve live business transactions, enabling undetected financial fraud.",
        "compensating_control": "Remove transaction-initiation rights from technical staff; perform independent supervisory transaction reconciliation.",
    },
    {
        "pair": ("Database Administrator (DBA)", "Security Administrator"),
        "severity": "CRITICAL",
        "risk": "DBA with Security Admin authority can create ghost accounts, assign SYSDBA/DBA privileges, manipulate sensitive data, and purge database audit trails.",
        "compensating_control": "Forward all database audit logs (DBA_AUDIT_TRAIL / audit_sys_operations) in real time to an independent, write-once SIEM managed by InfoSec/Compliance, and conduct independent DBA activity reviews.",
    },
    {
        "pair": ("System Administrator / Systems Programmer", "Security Administrator"),
        "severity": "CRITICAL",
        "risk": "SysAdmin can create unauthorized root/UID=0 accounts, bypass OS authentication controls, and alter local system logs (/var/log).",
        "compensating_control": "Centralize authentication (IAM/SSO with MFA), enforce remote immutable syslog, and perform independent review of /etc/passwd, /etc/shadow, and privileged command logs (sulog/sudo).",
    },
    {
        "pair": ("Computer Operator (Production)", "Security Administrator"),
        "severity": "HIGH",
        "risk": "Operator can reset user passwords or grant unauthorized access during night shifts and execute transactions.",
        "compensating_control": "Restrict user provisioning exclusively to Security Administrators based on written Data Owner approval; review console and security logs daily.",
    },
    {
        "pair": ("End User / Business Data Owner", "Security Administrator"),
        "severity": "CRITICAL",
        "risk": "Business user can provision fictitious accounts or grant themselves incompatible business roles (e.g., Vendor Master Creation + Payment Approval).",
        "compensating_control": "Security Admin must be independent of business transaction processing; Data Owner approves access in writing while Security Admin executes provisioning.",
    },
]


def cmd_lookup(args):
    db = load_db()
    target = args.id.strip().upper()

    # 1. Check Domains (D1..D5 or 1..5)
    for dom in db.get("domains", []):
        dom_id = dom["id"].upper()
        dom_num = dom_id.replace("D", "")
        if target in (dom_id, dom_num, f"DOMAIN {dom_num}", f"DOMAIN{dom_num}"):
            print(f"=== CISA {dom['id']}: {dom['name']} ({dom['weight_pct']}% / ~{dom['approx_questions']} Questions) ===")
            for part in dom.get("parts", []):
                print(f"\n[{part['part']}]")
                for t in part.get("topics", []):
                    print(f"  - {t}")
            print(f"\nMapped Task Statements: {', '.join(dom.get('tasks', []))}")
            return

    # 2. Check Tasks (T1..T39)
    for task in db.get("tasks", []):
        if target == task["id"].upper():
            print(f"=== CISA Official Task Statement {task['id']} ===")
            print(f"Statement : {task['text']}")
            print(f"Domains   : {', '.join(task.get('domains', []))}")
            return

    # 3. Check ITAF Standards (1001..1402 or 2001..2402 or ITAF)
    if target == "ITAF":
        print("=== ISACA ITAF 4th Edition Standards & Guidelines (17 Pairs) ===")
        for std in db.get("itaf_standards", []):
            print(f"  [{std['id']} / {std['guideline_id']}] ({std['category']}) {std['name']}")
        return

    for std in db.get("itaf_standards", []):
        if target in (std["id"].upper(), std["guideline_id"].upper()):
            print(f"=== ISACA ITAF 4th Edition: Standard {std['id']} / Guideline {std['guideline_id']} ===")
            print(f"Category : {std['category']}")
            print(f"Title    : {std['name']}")
            print("Mandatory Statements:")
            for stmt in std.get("statements", []):
                print(f"  * {stmt}")
            return

    # 4. Check SOXIT Key Controls
    matching_soxit = []
    for kc in db.get("soxit_key_controls", []):
        cid = kc["id"].upper()
        short_id = cid.replace(".00.00", "")
        if target == cid or target == short_id or cid.startswith(target):
            matching_soxit.append(kc)

    if matching_soxit:
        for kc in matching_soxit:
            print(f"=== {kc['id']} [{kc['domain']}] ===")
            print(f"Control Description:\n  {kc['description']}\n")
            print("Test of Design Effectiveness (TDE):")
            for tde in kc.get("tde_attributes", []):
                print(f"  [{tde['code']}] {tde['text']}")
            print("\nTest of Operating Effectiveness (TOE):")
            for toe in kc.get("toe_attributes", []):
                print(f"  [{toe['code']}] {toe['text']}")
            if kc.get("pbc_documents"):
                print("\nPrepared-by-Client (PBC) Requirements:")
                for item in kc["pbc_documents"]:
                    print(f"  * {item}")
            print("-" * 72)
        return

    # 5. Check Technical Walkthrough / Reference Modules
    if target == "BIA":
        print("=== Business Impact Analysis (BIA) Recovery Metrics ===")
        for m in BIA_METRICS:
            print(f"  * {m['metric']} ({m['name']}): {m['definition']}")
        return
    if target in ("UNIX", "SOLARIS", "LINUX"):
        print("=== UNIX / Solaris / Linux Technical Audit Walkthrough Guide (S07_W100) ===")
        for area, desc in TECHNICAL_GUIDES["UNIX"]:
            print(f"  * [{area}]\n    Audit Check: {desc}")
        return
    if target in ("ORACLE", "SQLSERVER", "DB", "DATABASE"):
        print("=== Oracle & SQL Server Database Technical Audit Walkthrough Guide (S07_W100) ===")
        for area, desc in TECHNICAL_GUIDES["ORACLE"]:
            print(f"  * [{area}]\n    Audit Check: {desc}")
        return
    if target == "SAP":
        print("=== SAP ERP / S/4HANA Technical Audit T-Codes & Tables Guide ===")
        for area, desc in TECHNICAL_GUIDES["SAP"]:
            print(f"  * [{area}]\n    Audit Check: {desc}")
        return

    print(f"No direct ID match for '{args.id}'. Try 'search --query {args.id}' or IDs like D1..D5, T1..T39, 1001..1402, SOXIT.01..SOXIT.04, BIA, UNIX, ORACLE, SAP.")


def cmd_sampling(args):
    method = args.method.lower()
    cl = args.confidence
    r_table = POISSON_R_TABLE.get(cl, POISSON_R_TABLE[95])
    z_two = NORMAL_Z_TWO_TAILED.get(cl, 1.960)

    if method in ("attribute", "discovery", "stop-or-go"):
        exp_dev = 0 if method == "discovery" else args.expected_deviations
        r_factor = r_table.get(exp_dev, r_table[0] + exp_dev * 1.55)
        ter = args.tolerable_error
        if ter <= 0 or ter >= 1:
            sys.stderr.write("Error: --tolerable-error must be a decimal between 0 and 1 (e.g., 0.05 for 5%).\n")
            sys.exit(1)

        n_poisson = math.ceil(r_factor / ter)
        n_fpc = math.ceil(n_poisson / (1.0 + (n_poisson / args.population))) if args.population > 0 else n_poisson

        print(f"=== IIA / CISA Statistical Sampling: {method.upper()} SAMPLING ===")
        print(f"Confidence Level (1 - Audit Risk) : {cl}% (Acceptable Risk = {100 - cl}%)")
        print(f"Population Size (N)               : {args.population if args.population > 0 else 'Large (> 500)'}")
        print(f"Tolerable Error Rate (TER)        : {ter * 100:.2f}%")
        print(f"Expected Deviations (c)           : {exp_dev}")
        print(f"Poisson Reliability Factor (R)    : {r_factor:.2f}")
        print(f"Unadjusted Sample Size (n = R/TER): {n_poisson}")
        if args.population > 0:
            print(f"Finite Population Adjusted (n_FPC): {n_fpc}")
            if method == "discovery":
                prob_detect = (1.0 - ((1.0 - ter) ** n_fpc)) * 100.0
                print(f"Discovery Detection Probability   : {prob_detect:.2f}% chance of finding >=1 critical fraud/error")
        print("\nAudit Interpretation:")
        print(f"  Select {n_fpc} items randomly. If <= {exp_dev} deviations are found, you are {cl}% confident")
        print(f"  that the true population deviation rate does not exceed {ter * 100:.2f}%.")

    elif method == "mus":
        bv = args.book_value
        tm = args.tolerable_misstatement
        exp_dev = args.expected_deviations
        r_factor = r_table.get(exp_dev, r_table[0])
        if bv <= 0 or tm <= 0:
            sys.stderr.write("Error: --book-value and --tolerable-misstatement must be > 0 for MUS.\n")
            sys.exit(1)
        n_mus = math.ceil((bv * r_factor) / tm)
        si = bv / n_mus
        print("=== IIA / CISA Monetary Unit Sampling (MUS / PPS) ===")
        print(f"Total Population Book Value (BV)  : {bv:,.2f}")
        print(f"Tolerable Misstatement (TM)       : {tm:,.2f} ({(tm / bv) * 100:.2f}% of Book Value)")
        print(f"Confidence Level & R-Factor       : {cl}% (R = {r_factor:.2f} at {exp_dev} expected errors)")
        print(f"Required MUS Sample Size (n)      : {n_mus} monetary units")
        print(f"Sampling Interval (SI = BV / n)   : {si:,.2f}")
        print(f"100% Top-Stratum Cutoff           : Every individual ledger item >= {si:,.2f} is automatically selected 100%!")

    elif method == "variable":
        N = args.population if args.population > 0 else 1000
        sigma = args.std_dev
        tm = args.tolerable_misstatement
        if sigma <= 0 or tm <= 0:
            sys.stderr.write("Error: --std-dev and --tolerable-misstatement must be > 0 for Variable Sampling.\n")
            sys.exit(1)
        precision_per_unit = tm / N
        n0 = ((z_two * sigma) / precision_per_unit) ** 2
        n_fpc = math.ceil(n0 / (1.0 + (n0 / N)))
        print("=== IIA / CISA Variable Sampling (Mean-Per-Unit / Substantive Testing) ===")
        print(f"Population Count (N)              : {N:,}")
        print(f"Population Std Deviation (sigma)  : {sigma:,.2f}")
        print(f"Total Tolerable Misstatement (A)  : {tm:,.2f} (Precision per unit e = {precision_per_unit:,.2f})")
        print(f"Confidence Level & Normal Z       : {cl}% (Z = {z_two:.3f})")
        print(f"Unadjusted Sample Size (n0)       : {math.ceil(n0):,}")
        print(f"FPC-Adjusted Sample Size (n)      : {n_fpc:,}")

    elif method == "itgc":
        freq = args.frequency.lower()
        print("=== CISA / SOX ITGC Operational Control Sample Size Table (Zero Deviation) ===")
        if freq in ITGC_RULE_OF_THUMB:
            info = ITGC_RULE_OF_THUMB[freq]
            print(f"Frequency : {freq.upper()}")
            print(f"Population: {info['population']}")
            print(f"Min Sample: {info['sample_size']}")
            print(f"Examples  : {info['examples']}")
        else:
            for k, v in ITGC_RULE_OF_THUMB.items():
                print(f"  * {k.upper():<14} | Pop: {v['population']:<22} | Min Sample: {v['sample_size']:<30} | {v['examples']}")


def cmd_risk_calc(args):
    mode = args.mode.lower()
    if mode == "ale":
        av = args.asset_value
        ef = args.exposure_factor
        aro = args.aro
        sle = av * ef
        ale_pre = sle * aro
        print("=== CISA Quantitative Risk Analysis (SLE / ALE / Control ROI) ===")
        print(f"Asset Value (AV)                  : ${av:,.2f}")
        print(f"Exposure Factor (EF)              : {ef * 100:.2f}%")
        print(f"Annualized Rate of Occurrence(ARO): {aro:.4f} events/year")
        print(f"Single Loss Expectancy (SLE)      : ${sle:,.2f}  [AV x EF]")
        print(f"Pre-Control ALE (ALE_before)      : ${ale_pre:,.2f}/year  [SLE x ARO]")

        if args.acs > 0 or args.ef_post is not None or args.aro_post is not None:
            ef_p = args.ef_post if args.ef_post is not None else ef
            aro_p = args.aro_post if args.aro_post is not None else aro
            sle_post = av * ef_p
            ale_post = sle_post * aro_p
            net_value = (ale_pre - ale_post) - args.acs
            print("-" * 64)
            print(f"Post-Control EF & ARO             : EF={ef_p * 100:.2f}%, ARO={aro_p:.4f}")
            print(f"Post-Control ALE (ALE_after)      : ${ale_post:,.2f}/year")
            print(f"Annual Cost of Safeguard (ACS)    : ${args.acs:,.2f}/year")
            print(f"Net Value / ROI of Control        : ${net_value:,.2f}/year  [(ALE_before - ALE_after) - ACS]")
            if net_value > 0:
                print("CISA Audit Decision               : COST-EFFECTIVE (Recommend implementing control; net savings > $0).")
            else:
                print("CISA Audit Decision               : NOT COST-EFFECTIVE (Cost of control exceeds risk reduction; consider Risk Acceptance/Transfer).")

    elif mode == "eva":
        bac = args.bac
        pv = args.pv
        ev = args.ev
        ac = args.ac
        cv = ev - ac
        sv = ev - pv
        cpi = ev / ac if ac > 0 else 0.0
        spi = ev / pv if pv > 0 else 0.0
        eac = bac / cpi if cpi > 0 else 0.0
        etc = eac - ac
        print("=== CISA Domain 3: Project Earned Value Analysis (EVA) ===")
        print(f"Budget at Completion (BAC)        : ${bac:,.2f}")
        print(f"Planned Value (PV)                : ${pv:,.2f}")
        print(f"Earned Value (EV)                 : ${ev:,.2f}")
        print(f"Actual Cost (AC)                  : ${ac:,.2f}")
        print("-" * 64)
        print(f"Cost Variance (CV = EV - AC)      : ${cv:,.2f}  ({'UNDER BUDGET [Good]' if cv >= 0 else 'COST OVERRUN [Risk!]'})")
        print(f"Schedule Variance (SV = EV - PV)  : ${sv:,.2f}  ({'AHEAD/ON SCHEDULE [Good]' if sv >= 0 else 'BEHIND SCHEDULE [Risk!]'})")
        print(f"Cost Performance Index (CPI=EV/AC): {cpi:.3f}  ({'Efficient' if cpi >= 1.0 else 'Overbudget (< 1.0)'})")
        print(f"Schedule Perf. Index (SPI=EV/PV)  : {spi:.3f}  ({'On/Ahead of Track' if spi >= 1.0 else 'Delayed (< 1.0)'})")
        print(f"Estimate at Completion (EAC)      : ${eac:,.2f}  [BAC / CPI]")
        print(f"Estimate to Complete (ETC)        : ${etc:,.2f}  [EAC - AC]")

    elif mode == "pert":
        o, m, p = args.optimistic, args.most_likely, args.pessimistic
        te = (o + 4.0 * m + p) / 6.0
        sd = (p - o) / 6.0
        var = sd ** 2
        print("=== CISA Domain 3: Project PERT Three-Point Estimation ===")
        print(f"Optimistic (O)={o}, Most Likely (M)={m}, Pessimistic (P)={p}")
        print(f"Expected Duration (Te = (O+4M+P)/6): {te:.2f} time units")
        print(f"Standard Deviation (sigma=(P-O)/6) : {sd:.2f} time units")
        print(f"Variance (sigma^2)                 : {var:.2f}")
        print(f"95% Confidence Range (Te +/- 2*sd) : {max(0.0, te - 2*sd):.2f} to {te + 2*sd:.2f} time units")

    elif mode == "audit-risk":
        ar, ir, cr = args.ar, args.ir, args.cr
        dr = ar / (ir * cr) if (ir * cr) > 0 else 0.0
        print("=== CISA Domain 1: Audit Risk Model (AR = IR x CR x DR) ===")
        print(f"Target Audit Risk (AR)            : {ar * 100:.2f}%")
        print(f"Assessed Inherent Risk (IR)       : {ir * 100:.2f}%")
        print(f"Assessed Control Risk (CR)        : {cr * 100:.2f}%")
        print(f"Max Allowable Detection Risk (DR) : {dr * 100:.2f}%  [DR = AR / (IR x CR)]")
        if dr <= 0.10:
            print("Audit Strategy                    : LOW Detection Risk Required -> MUST INCREASE sample size and expand substantive testing!")
        else:
            print("Audit Strategy                    : Moderate/High Detection Risk Allowable -> Standard sample size and reliance on controls permitted.")


def cmd_sod_check(args):
    raw_roles = [r.strip().lower() for r in args.roles.split(",") if r.strip()]
    normalized = []
    for r in raw_roles:
        canonical = ROLE_ALIASES.get(r, r.title())
        if canonical not in normalized:
            normalized.append(canonical)

    print("=== CISA Domain 2 & 5: Segregation of Duties (SoD) Conflict Analysis ===")
    print(f"Evaluated Roles Held by Single Individual/Group ({len(normalized)}):")
    for idx, r in enumerate(normalized, 1):
        print(f"  {idx}. {r}")
    print("-" * 72)

    conflicts_found = []
    if "IS Auditor" in normalized and len(normalized) > 1:
        conflicts_found.append({
            "pair": ("IS Auditor", "Operational/IT/Business Roles"),
            "severity": "CRITICAL (ITAF 1002/1003 Violation)",
            "risk": "IS Auditor performing operational IT or business duties loses Organizational Independence and Objectivity (Self-Review Threat).",
            "compensating_control": "Immediately remove operational privileges from IS Auditor; assign an independent auditor who had no involvement in the system to perform the audit.",
        })

    for rule in SOD_RULES:
        r1, r2 = rule["pair"]
        if r1 in normalized and r2 in normalized:
            conflicts_found.append(rule)

    if not conflicts_found:
        print("Result: NO CRITICAL SoD CONFLICTS DETECTED among the specified roles.")
    else:
        print(f"Result: {len(conflicts_found)} CRITICAL SoD CONFLICT(S) DETECTED!\n")
        for i, c in enumerate(conflicts_found, 1):
            print(f"[{i}] CONFLICT: {c['pair'][0]}  <===>  {c['pair'][1]}  (Severity: {c['severity']})")
            print(f"    * Specific Fraud/Error Risk : {c['risk']}")
            print(f"    * CISA Compensating Control : {c['compensating_control']}\n")


def cmd_pbc(args):
    db = load_db()
    target = args.domain.strip().upper()
    controls = db.get("soxit_key_controls", [])
    if target != "ALL":
        controls = [c for c in controls if target in c["id"].upper() or target in c["domain"].upper()]

    print(f"# CISA / SOX ITGC Audit Workprogram & PBC Request List (Scope: {target})\n")
    for kc in controls:
        print(f"## {kc['id']} — {kc['domain']}")
        print(f"- **Key Control:** {kc['description']}")
        print("- **Test of Design (TDE):**")
        for tde in kc.get("tde_attributes", []):
            print(f"  - `{tde['code']}`: {tde['text']}")
        print("- **Test of Operating Effectiveness (TOE):**")
        for toe in kc.get("toe_attributes", []):
            print(f"  - `{toe['code']}`: {toe['text']}")
        if kc.get("pbc_documents"):
            print("- **Required PBC Documents:**")
            for p in kc["pbc_documents"]:
                print(f"  - [ ] {p}")
        print()


def cmd_search(args):
    db = load_db()
    q = args.query.strip().lower()
    hits = []

    for dom in db.get("domains", []):
        blob = json.dumps(dom, ensure_ascii=False).lower()
        if q in blob:
            hits.append(f"[Domain {dom['id']}] {dom['name']} ({dom['weight_pct']}%)")

    for t in db.get("tasks", []):
        if q in t["text"].lower() or q == t["id"].lower():
            hits.append(f"[Task {t['id']}] {t['text']}")

    for s in db.get("itaf_standards", []):
        blob = json.dumps(s, ensure_ascii=False).lower()
        if q in blob:
            hits.append(f"[ITAF {s['id']}/{s['guideline_id']}] ({s['category']}) {s['name']}")

    for kc in db.get("soxit_key_controls", []):
        blob = json.dumps(kc, ensure_ascii=False).lower()
        if q in blob:
            hits.append(f"[{kc['id']}] ({kc['domain']}) {kc['description']}")

    print(f"=== CISA Knowledge Base Search Results for '{args.query}' ({len(hits)} matches) ===")
    for h in hits[:30]:
        print(f"  * {h}")


def cmd_caats(args):
    """Execute CAATs Benford's Law First-Digit Fraud Analysis or HR-vs-Active User Reconciliation."""
    if args.test == "benford":
        raw_vals = [x.strip() for x in args.values.split(",") if x.strip()]
        first_digits = {d: 0 for d in range(1, 10)}
        total_valid = 0
        for val in raw_vals:
            clean = val.lstrip("-$Rp ").replace(",", "")
            for ch in clean:
                if ch in "123456789":
                    first_digits[int(ch)] += 1
                    total_valid += 1
                    break
        if total_valid == 0:
            sys.stderr.write("Error: No valid non-zero numbers provided for Benford analysis.\n")
            sys.exit(1)

        print(f"=== CISA Domain 1 CAATs: Benford's Law First-Digit Fraud & Anomaly Analysis (N = {total_valid}) ===")
        print(f"{'Digit':<7} | {'Observed':<10} | {'Obs %':<9} | {'Benford Expected %':<19} | {'Deviation':<10} | {'Status'}")
        print("-" * 78)
        chi_sq = 0.0
        for d in range(1, 10):
            expected_pct = math.log10(1.0 + 1.0 / d)
            expected_cnt = total_valid * expected_pct
            obs_cnt = first_digits[d]
            obs_pct = obs_cnt / total_valid
            diff_pct = (obs_pct - expected_pct) * 100.0
            if expected_cnt > 0:
                chi_sq += ((obs_cnt - expected_cnt) ** 2) / expected_cnt
            flag = "SPIKE (Investigate!)" if diff_pct > 10.0 else "Normal"
            print(f"{d:<7} | {obs_cnt:<10} | {obs_pct*100:>6.2f}%  | {expected_pct*100:>16.2f}%  | {diff_pct:>+7.2f}%  | {flag}")
        print("-" * 78)
        # Critical Chi-Square at df=8, alpha=0.05 is 15.507
        verdict = "HIGH ANOMALY / POTENTIAL MANIPULATION (Chi-Square > 15.51 at alpha=0.05)" if chi_sq > 15.507 else "CONFORMS TO BENFORD'S LAW (Chi-Square <= 15.51)"
        print(f"Chi-Square Statistic (df=8) : {chi_sq:.3f}  -->  {verdict}")
        print("CISA Audit Note             : Spikes on digits 8 or 9 often indicate artificial splitting just below approval thresholds!")

    elif args.test == "reconcile-users":
        terminated = {u.strip().lower() for u in args.terminated.split(",") if u.strip()}
        active = {u.strip().lower() for u in args.active.split(",") if u.strip()}
        orphans = sorted(terminated.intersection(active))
        print("=== CISA Domain 5 / SOXIT.03.C3 CAATs: HR Terminated vs. Active System Users Reconciliation ===")
        print(f"Terminated HR List Count : {len(terminated)}")
        print(f"Active System User Count : {len(active)}")
        print(f"Orphaned Active Accounts : {len(orphans)}")
        if orphans:
            print("CRITICAL FINDING (SOXIT.03.C3 Violation): Terminated employees still active in production:")
            for acc in orphans:
                print(f"  [!] {acc}  --> Immediate revocation & substantive transaction log review required!")
        else:
            print("Result: PASS (Zero terminated employees found in active user population).")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CISA IT Auditor CLI Engine (ISACA CRM 27e / ITAF 4e / IIA Sampling / SOX ITGC)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_lookup = sub.add_parser("lookup", help="Lookup CISA Domain (D1-D5), Task (T1-T39), ITAF (1001-1402), SOXIT Control, or Technical Guide (BIA, UNIX, ORACLE)")
    p_lookup.add_argument("--id", required=True, help="Identifier to lookup (e.g., D1, T15, 1205, SOXIT.03.00.00.C4, BIA, UNIX, ORACLE)")
    p_lookup.set_defaults(func=cmd_lookup)

    p_samp = sub.add_parser("sampling", help="Calculate IIA Statistical Audit Sample Sizes (Attribute, Discovery, MUS, Variable, or ITGC Frequency)")
    p_samp.add_argument("--method", choices=["attribute", "discovery", "stop-or-go", "mus", "variable", "itgc"], default="attribute")
    p_samp.add_argument("--confidence", type=int, choices=[80, 85, 90, 95, 98, 99], default=95)
    p_samp.add_argument("--tolerable-error", type=float, default=0.05, help="Tolerable Error Rate decimal (e.g. 0.05 for 5%%)")
    p_samp.add_argument("--expected-deviations", type=int, default=0, help="Expected number of deviations in sample (0-5)")
    p_samp.add_argument("--population", type=int, default=0, help="Total population count N (optional for FPC)")
    p_samp.add_argument("--book-value", type=float, default=1000000.0, help="Total Book Value for MUS")
    p_samp.add_argument("--tolerable-misstatement", type=float, default=50000.0, help="Tolerable Monetary Misstatement for MUS/Variable")
    p_samp.add_argument("--std-dev", type=float, default=250.0, help="Estimated population standard deviation for Variable sampling")
    p_samp.add_argument("--frequency", default="all", help="Control frequency for ITGC table (annual, quarterly, monthly, weekly, daily, transactional, automated)")
    p_samp.set_defaults(func=cmd_sampling)

    p_risk = sub.add_parser("risk-calc", help="Calculate Quantitative Risk (SLE/ALE/ROI), Earned Value (EVA), PERT, or Audit Risk (AR=IR*CR*DR)")
    p_risk.add_argument("--mode", choices=["ale", "eva", "pert", "audit-risk"], required=True)
    p_risk.add_argument("--asset-value", type=float, default=1000000.0)
    p_risk.add_argument("--exposure-factor", type=float, default=0.50)
    p_risk.add_argument("--aro", type=float, default=0.20)
    p_risk.add_argument("--ef-post", type=float, default=None)
    p_risk.add_argument("--aro-post", type=float, default=None)
    p_risk.add_argument("--acs", type=float, default=0.0, help="Annual Cost of Safeguard/Control")
    p_risk.add_argument("--bac", type=float, default=100000.0)
    p_risk.add_argument("--pv", type=float, default=50000.0)
    p_risk.add_argument("--ev", type=float, default=40000.0)
    p_risk.add_argument("--ac", type=float, default=55000.0)
    p_risk.add_argument("--optimistic", type=float, default=4.0)
    p_risk.add_argument("--most-likely", type=float, default=7.0)
    p_risk.add_argument("--pessimistic", type=float, default=16.0)
    p_risk.add_argument("--ar", type=float, default=0.05)
    p_risk.add_argument("--ir", type=float, default=0.80)
    p_risk.add_argument("--cr", type=float, default=0.80)
    p_risk.set_defaults(func=cmd_risk_calc)

    p_sod = sub.add_parser("sod-check", help="Evaluate IT Segregation of Duties (SoD) conflicts across 12 IT & Business roles")
    p_sod.add_argument("--roles", required=True, help="Comma-separated roles (e.g., 'developer,operator,security_admin' or 'dba,security')")
    p_sod.set_defaults(func=cmd_sod_check)

    p_pbc = sub.add_parser("pbc", help="Generate SOX/ITGC Prepared-by-Client (PBC) & TDE/TOE Audit Program")
    p_pbc.add_argument("--domain", default="ALL", help="ALL, SOXIT.01, SOXIT.02, SOXIT.03, or SOXIT.04")
    p_pbc.set_defaults(func=cmd_pbc)

    p_search = sub.add_parser("search", help="Full-text search across CISA Domains, Tasks, ITAF Standards, and SOXIT Controls")
    p_search.add_argument("--query", required=True, help="Keyword to search")
    p_search.set_defaults(func=cmd_search)

    p_caats = sub.add_parser("caats", help="Run CAATs Data Analytics (Benford's Law First-Digit Test or HR Terminated vs Active Users)")
    p_caats.add_argument("--test", choices=["benford", "reconcile-users"], default="benford")
    p_caats.add_argument("--values", default="", help="Comma-separated transaction values for Benford test")
    p_caats.add_argument("--terminated", default="", help="Comma-separated terminated user IDs from HR")
    p_caats.add_argument("--active", default="", help="Comma-separated active user IDs from system")
    p_caats.set_defaults(func=cmd_caats)

    return parser


if __name__ == "__main__":
    parser = build_parser()
    parsed_args = parser.parse_args()
    parsed_args.func(parsed_args)
