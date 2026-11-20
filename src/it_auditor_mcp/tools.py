"""Core audit & regulatory inspection engines for FastMCP tools."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Paths to existing databases in IT_Auditor skills
IDREG_DB_PATH = REPO_ROOT / "skills" / "id-it-regulatory-auditor" / "data" / "id_regulations_database.json"
CISA_DB_PATH = REPO_ROOT / "skills" / "cisa-it-auditor" / "data" / "cisa_database.json"
COBIT_DB_PATH = REPO_ROOT / "skills" / "cobit-it-auditor" / "data" / "cobit2019_database.json"

POISSON_R_TABLE = {
    90: {0: 2.31, 1: 3.89, 2: 5.33, 3: 6.69, 4: 8.00, 5: 9.28},
    95: {0: 3.00, 1: 4.75, 2: 6.30, 3: 7.76, 4: 9.16, 5: 10.52},
    99: {0: 4.61, 1: 6.64, 2: 8.41, 3: 10.05, 4: 11.61, 5: 13.11},
}


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def uupdp_lookup_control(
    query: str,
    annual_revenue: float = 0.0,
    hours_since_breach: float = 0.0,
    specific_data: bool = False,
    large_scale: bool = False,
) -> Dict[str, Any]:
    """Inspect UU No. 27/2022 obligations, 72-hour breach deadline, and maximum 2% administrative fine."""
    max_fine = annual_revenue * 0.02
    within_72h = hours_since_breach <= 72.0
    hours_overdue = max(0.0, hours_since_breach - 72.0)

    requirements: List[str] = [
        "Pemberitahuan tertulis wajib disampaikan kepada Subjek Data dan Lembaga PDP maksimal 3x24 jam (Pasal 46)."
    ]
    if specific_data or large_scale:
        requirements.append("Wajib melaksanakan Data Protection Impact Assessment (DPIA - Pasal 34).")
        requirements.append("Wajib menunjuk Pejabat/Petugas Pelindungan Data Pribadi (DPO - Pasal 53).")

    return {
        "query": query,
        "annual_revenue": annual_revenue,
        "max_fine": max_fine,
        "hours_since_breach": hours_since_breach,
        "within_72h_limit": within_72h,
        "hours_overdue": hours_overdue,
        "compliance_status": "COMPLIANT_TIMEFRAME" if within_72h else "BREACH_DEADLINE_VIOLATION",
        "legal_reference": "UU No. 27 Tahun 2022 Pasal 46, Pasal 57 ayat (2) & (3)",
        "requirements": requirements,
    }


def audit_sampling_calculator(
    method: str = "attribute",
    population_size: int = 1000,
    confidence_level: int = 95,
    tolerable_error_rate: float = 0.05,
    expected_deviations: int = 0,
) -> Dict[str, Any]:
    """Calculate IIA/CISA compliant statistical audit sampling for evidence testing."""
    cl = confidence_level if confidence_level in POISSON_R_TABLE else 95
    r_table = POISSON_R_TABLE[cl]
    r_factor = r_table.get(expected_deviations, r_table[0] + expected_deviations * 1.55)

    if tolerable_error_rate <= 0 or tolerable_error_rate >= 1:
        tolerable_error_rate = 0.05

    n_poisson = math.ceil(r_factor / tolerable_error_rate)
    n_fpc = (
        math.ceil(n_poisson / (1.0 + (n_poisson / population_size)))
        if population_size > 0
        else n_poisson
    )

    return {
        "method": method,
        "confidence_level": cl,
        "population_size": population_size,
        "tolerable_error_rate": tolerable_error_rate,
        "expected_deviations": expected_deviations,
        "poisson_r_factor": r_factor,
        "unadjusted_sample_size": n_poisson,
        "adjusted_sample_size": n_fpc,
        "guidance": (
            f"Select {n_fpc} items randomly. If <= {expected_deviations} deviations found, "
            f"you have {cl}% confidence that error rate does not exceed {tolerable_error_rate*100:.1f}%."
        ),
    }


def cobit_practice_lookup(objective_id: str) -> Dict[str, Any]:
    """Retrieve COBIT 2019 objective details, practices, and governance activities."""
    db = _load_json(COBIT_DB_PATH)
    objs = db.get("objectives", {})
    target = objective_id.strip().upper()

    if target not in objs:
        return {
            "found": False,
            "objective_id": target,
            "message": f"Objective '{target}' not found. Available prefixes: EDM, APO, BAI, DSS, MEA.",
        }

    o = objs[target]
    practices_summary = []
    for p in o.get("practices", []):
        practices_summary.append({
            "id": p.get("id"),
            "name": p.get("name"),
            "description": p.get("description"),
            "activities_count": len(p.get("activities", [])),
        })

    return {
        "found": True,
        "objective_id": o.get("id"),
        "name": o.get("name"),
        "area": o.get("area"),
        "domain": o.get("domain"),
        "description": o.get("description"),
        "practices_count": len(practices_summary),
        "practices": practices_summary,
    }


def audit_crosswalk_mapper(query: str = "ALL") -> Dict[str, Any]:
    """Map regulations (POJK, UU PDP, BSSN Indeks KAMI) against COBIT 2019 and CISA domains."""
    db = _load_json(IDREG_DB_PATH)
    regs = db.get("crosswalk_regulations", [])
    q = query.strip().upper()

    if q != "ALL":
        filtered = [
            r for r in regs
            if q in r.get("id", "").upper()
            or q in r.get("title", "").upper()
            or q in r.get("sector", "").upper()
        ]
    else:
        filtered = regs

    return {
        "query": query,
        "total_matched": len(filtered),
        "matches": filtered,
    }
