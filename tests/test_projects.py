"""Project catalog: every record is valid, ids are unique, and technology links resolve."""
import json
import jsonschema
import pathlib
import sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "project.schema.json").read_text(encoding="utf-8"))
PROJECTS = [
    json.loads(p.read_text(encoding="utf-8"))
    for p in sorted((ROOT / "catalog" / "projects").glob("*.json"))
]
CARDS = {c["id"]: c for c in build.technologies.load_cards()}


@pytest.mark.parametrize("rec", PROJECTS, ids=[r["id"] for r in PROJECTS])
def test_record_is_valid(rec):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(rec)
    for t in rec.get("technologies", []):
        assert t in CARDS, f"{rec['id']}: technology {t} has no card"
    for s in rec["sources"]:
        assert s["url"].startswith(("http://", "https://")), f"{rec['id']}: source without http(s) url"


def test_ids_unique():
    ids = [r["id"] for r in PROJECTS]
    assert len(ids) == len(set(ids)), "duplicate project ids"


def test_every_project_has_a_source_and_status():
    for rec in PROJECTS:
        assert rec["sources"], f"{rec['id']}: no sources"
        assert rec["status"] in ("proposed", "FID", "under-construction", "commissioning",
                                 "operating", "suspended", "decommissioned"), rec["id"]


def test_capex_carries_dollar_year():
    for rec in PROJECTS:
        for c in rec.get("capex", []):
            if "USD" in (c.get("unit") or "").upper():
                assert "year" in c, f"{rec['id']}: USD capex '{c['metric']}' without dollar year"


def test_party_vendor_ids_resolve():
    vendors = {v.stem for v in (ROOT / "catalog" / "vendors").glob("*.json")}
    for rec in PROJECTS:
        for group in ("owners", "contractors", "offtakers"):
            for p in rec.get(group, []):
                if "vendor_id" in p:
                    assert p["vendor_id"] in vendors, f"{rec['id']}: vendor {p['vendor_id']} not in directory"


def test_reference_plants_link_to_projects():
    """Every card reference plant points at a real project record, so the two layers cannot drift."""
    by_id = {r["id"]: r for r in PROJECTS}
    for card in CARDS.values():
        for rp in card.get("reference_plants", []):
            pid = rp.get("project_id")
            assert pid, f"{card['id']}: reference plant '{rp['name']}' has no project_id"
            assert pid in by_id, f"{card['id']}: project_id {pid} does not exist"
            assert card["id"] in by_id[pid].get("technologies", []), \
                f"{pid}: does not list card {card['id']} in technologies"
