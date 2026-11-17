"""The MCP tool surface: the figures, taxonomy, glossary and standards tools added 2026-11-17.

These run against the baked SQLite index (no DATABASE_URL), which is the same fallback path a
container uses when Neon is unreachable — so the test pins the shape an agent sees either way.
"""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
server = pytest.importorskip("server")
import projects  # noqa: E402  (country matcher used by the filter assertions)


def test_taxonomy_lists_both_axes_with_names():
    tax = server.taxonomy()
    sectors = {s["code"]: s for s in tax["sectors"]}
    disciplines = {d["code"]: d for d in tax["disciplines"]}
    assert {"UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS", "IDC", "WWT"} <= set(sectors)
    assert {"PRC", "ROT", "ELE", "CIV", "INS", "MAT", "HSE", "DIG"} <= set(disciplines)
    assert all(s.get("name") and s.get("subtopics") for s in tax["sectors"])
    assert tax["regions"], "region codes are needed for search filters"


def test_find_figures_returns_basis_and_source():
    rows = server.find_figures(kind="cost", technology_id="pwr-gas-engines")
    assert rows and all(r["kind"] == "cost" for r in rows)
    assert all(r["basis"] and r["source_url"] and r["metric"] and r["unit"] for r in rows)


def test_find_figures_unit_and_query_filters():
    usd_kw = server.find_figures(unit="USD/kW", limit=5)
    assert usd_kw and all("usd/kw" in r["unit"].lower() for r in usd_kw)
    heavy = server.find_figures(query="gas turbine", limit=20)
    assert heavy, "a substring over metric/basis/name should match the gas-turbine cards"


def test_find_figures_rejects_unknown_kind():
    with pytest.raises(ValueError):
        server.find_figures(kind="capex")


def test_glossary_browse_and_lookup():
    entries = server.list_glossary()
    assert len(entries) >= 40 and all("term" in e for e in entries)
    ccgt = server.get_glossary_term("CCGT")
    assert ccgt and ccgt["term"] == "CCGT"
    assert server.get_glossary_term("not-a-real-term-zzz") is None


def test_standards_browse_filter_and_lookup():
    assert len(server.list_standards()) >= 20
    api = server.list_standards(org="API")
    assert api and all(s["org"] == "API" for s in api)
    one = server.get_standard("IEC 60079")
    assert one and one["designation"].startswith("IEC 60079")


def test_every_documented_tool_exists():
    for name in ("search", "get_source", "get_document", "list_by_tag", "get_technology",
                 "compare_technologies", "find_figures", "list_vendors", "get_vendor",
                 "list_equipment", "get_equipment", "list_projects", "get_project",
                 "list_technology_register", "list_gaps", "taxonomy", "list_glossary",
                 "get_glossary_term", "list_standards", "get_standard", "library_stats",
                 "sql_query", "db_catalog", "graph_neighbors"):
        assert callable(getattr(server, name)), f"{name} is documented but not exposed"


def test_search_finds_projects():
    """The search docstring promises kind="project"; the SQLite path and the Neon hybrid_search
    (db/schema.sql) must both serve it — 2026-11-17 the Neon union silently dropped projects."""
    rows = server.search("Donaldsonville ammonia", kind="project")
    assert rows and all(r["kind"] == "project" for r in rows)
    assert "cf-donaldsonville" in {r["ref"] for r in rows}
    for r in rows:
        assert r.get("status"), "project search rows carry the status"


def test_list_projects_country_filter():
    """Country filter canonicalises mixed spellings: records store "US", "USA" and
    "United States"; a two-letter code must match only through the alias map, never as a
    stray substring ("ES" must not match "United States")."""
    us = server.list_projects(country="US")
    assert us and "cf-donaldsonville" in {p["id"] for p in us}
    assert all(projects.country_matches(p.get("country"), "US") for p in us)
    ca = server.list_projects(country="Canada")
    assert "nutrien-redwater" in {p["id"] for p in ca}
    assert not ({"nutrien-redwater"} & {p["id"] for p in us})
    es = server.list_projects(country="ES")
    assert es and all((p.get("country") or "").strip().lower() in ("es", "spain") for p in es)


def test_hybrid_search_schema_serves_projects():
    """Static guard on db/schema.sql: the Neon hybrid_search union must include the project
    table and the reuse-level pass-through must admit project records."""
    sql = (pathlib.Path(__file__).resolve().parent.parent / "db" / "schema.sql").read_text(encoding="utf-8")
    fn = sql.split("CREATE OR REPLACE FUNCTION hybrid_search", 1)[1].split("$$;", 1)[0]
    assert "SELECT 'project', p.id, p.name" in fn, "hybrid_search union lacks the project branch"
    assert "('technology', 'vendor', 'equipment', 'project') AND reuse_level = 'full-text-open'" in fn
