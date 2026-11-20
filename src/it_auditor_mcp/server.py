"""FastMCP / MCPServer definition for IT Auditor & Regulatory Suite."""

try:
    # mcp 2.x
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:
    # mcp 1.x fallback
    from mcp.server.fastmcp import FastMCP

from src.it_auditor_mcp.tools import (
    audit_crosswalk_mapper as _crosswalk,
    audit_sampling_calculator as _sampling,
    cobit_practice_lookup as _cobit,
    uupdp_lookup_control as _uupdp,
)

mcp = FastMCP("it-auditor-mcp")


@mcp.tool()
def uupdp_lookup_control(
    query: str,
    annual_revenue: float = 0.0,
    hours_since_breach: float = 0.0,
    specific_data: bool = False,
    large_scale: bool = False,
) -> dict:
    """Evaluate Indonesian Personal Data Protection (UU PDP No. 27/2022) obligations, 72h notification deadline, and maximum 2% fine exposure."""
    return _uupdp(
        query=query,
        annual_revenue=annual_revenue,
        hours_since_breach=hours_since_breach,
        specific_data=specific_data,
        large_scale=large_scale,
    )


@mcp.tool()
def audit_sampling_calculator(
    method: str = "attribute",
    population_size: int = 1000,
    confidence_level: int = 95,
    tolerable_error_rate: float = 0.05,
    expected_deviations: int = 0,
) -> dict:
    """Compute statistically valid audit sample sizes (IIA/CISA standard) for evidence verification."""
    return _sampling(
        method=method,
        population_size=population_size,
        confidence_level=confidence_level,
        tolerable_error_rate=tolerable_error_rate,
        expected_deviations=expected_deviations,
    )


@mcp.tool()
def cobit_practice_lookup(objective_id: str) -> dict:
    """Lookup ISACA COBIT 2019 governance and management objectives, practices, and activities."""
    return _cobit(objective_id=objective_id)


@mcp.tool()
def audit_crosswalk_mapper(query: str = "ALL") -> dict:
    """Map compliance frameworks (UU PDP, POJK 11/2022, SEOJK 29/2022, BUMN, BSSN Indeks KAMI) to COBIT 2019 and CISA."""
    return _crosswalk(query=query)


def main():
    """Run FastMCP server over standard I/O (stdio)."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
