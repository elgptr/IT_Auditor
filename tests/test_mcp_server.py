"""TDD test suite for IT_Auditor FastMCP Server bridge."""

import pytest
import os
import sys

# Ensure repo root is on sys.path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)


def test_mcp_server_initialization():
    """Server module should expose an initialized FastMCP instance."""
    from src.it_auditor_mcp.server import mcp

    assert mcp is not None
    assert mcp.name == "it-auditor-mcp"


def test_uupdp_lookup_control_returns_structured_summary():
    """UU PDP lookup should return penalty, timeframe, and requirements."""
    from src.it_auditor_mcp.tools import uupdp_lookup_control

    result = uupdp_lookup_control(query="kebocoran", annual_revenue=10_000_000_000.0, hours_since_breach=48.0)
    assert isinstance(result, dict)
    assert "max_fine" in result
    assert result["max_fine"] == 200_000_000.0  # 2% of 10B
    assert result["within_72h_limit"] is True
    assert "Pasal 46" in result["legal_reference"]


def test_uupdp_lookup_control_over_72h():
    """Over 72 hours should flag deadline violation."""
    from src.it_auditor_mcp.tools import uupdp_lookup_control

    result = uupdp_lookup_control(query="insiden", annual_revenue=5_000_000_000.0, hours_since_breach=80.0)
    assert result["within_72h_limit"] is False
    assert result["hours_overdue"] == 8.0


def test_audit_sampling_calculator_attribute():
    """Sampling calculator should return sample size and Poisson factors."""
    from src.it_auditor_mcp.tools import audit_sampling_calculator

    res = audit_sampling_calculator(
        method="attribute",
        population_size=1000,
        confidence_level=95,
        tolerable_error_rate=0.05,
        expected_deviations=0,
    )
    assert isinstance(res, dict)
    assert res["confidence_level"] == 95
    assert res["unadjusted_sample_size"] == 60  # ceil(3.00 / 0.05)
    assert res["adjusted_sample_size"] > 0
    assert res["adjusted_sample_size"] <= res["unadjusted_sample_size"]


def test_cobit_practice_lookup():
    """COBIT practice lookup should return practice details and activities."""
    from src.it_auditor_mcp.tools import cobit_practice_lookup

    res = cobit_practice_lookup(objective_id="APO13")
    assert isinstance(res, dict)
    assert res["found"] is True
    assert res["objective_id"] == "APO13"
    assert "practices" in res
    assert len(res["practices"]) > 0


def test_audit_crosswalk_mapper():
    """Crosswalk mapper should resolve mappings for standard."""
    from src.it_auditor_mcp.tools import audit_crosswalk_mapper

    res = audit_crosswalk_mapper(query="PDP")
    assert isinstance(res, dict)
    assert "matches" in res
    assert len(res["matches"]) > 0
    first = res["matches"][0]
    assert "cobit2019_mapping" in first
    assert "cisa_mapping" in first
