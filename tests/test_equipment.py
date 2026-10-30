"""Equipment catalog: every record is valid, ids are unique, and vendor/technology links resolve."""
import json
import jsonschema
import pathlib
import sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "equipment.schema.json").read_text(encoding="utf-8"))
EQUIPMENT = [
    json.loads(p.read_text(encoding="utf-8"))
    for p in sorted((ROOT / "catalog" / "equipment").glob("*.json"))
]
CARDS = {c["id"]: c for c in build.technologies.load_cards()}
VENDORS = {
    v["id"] for v in build.load_vendors(set(CARDS), set())[0]
}


@pytest.mark.parametrize("rec", EQUIPMENT, ids=[r["id"] for r in EQUIPMENT])
def test_record_is_valid(rec):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(rec)
    for v in rec["vendors"]:
        assert v in VENDORS, f"{rec['id']}: vendor {v} is not in the directory"
    for t in rec.get("technologies", []):
        assert t in CARDS, f"{rec['id']}: technology {t} has no card"
    for m in rec.get("vendor_models", []):
        assert m["vendor"] in VENDORS, f"{rec['id']}: model line vendor {m['vendor']} is not in the directory"
    for s in rec["sources"]:
        assert s["url"].startswith(("http://", "https://")), f"{rec['id']}: source without http(s) url"


def test_every_record_has_a_spec_with_basis():
    for rec in EQUIPMENT:
        assert rec["specifications"], f"{rec['id']}: no specifications"
        for s in rec["specifications"]:
            assert s.get("basis") or s.get("note"), f"{rec['id']}: spec '{s['metric']}' without basis"


def test_record_ids_unique():
    ids = [r["id"] for r in EQUIPMENT]
    assert len(ids) == len(set(ids)), "duplicate equipment ids"


def test_search_index_carries_equipment():
    import equipment
    import library
    rows = {r["id"]: json.loads(r["record"]) for r in library.connect().execute("SELECT id, record FROM equipment")}
    assert set(rows) == {r["id"] for r in EQUIPMENT}, "library.db equipment table stale or missing"
    hits = library.search("boiler specification", kind="equipment")
    assert hits, "equipment kind search returned nothing"
    first = equipment.summary(EQUIPMENT[0])
    assert first["id"] in {h["ref"] for h in hits} | {h["ref"] for h in library.search(EQUIPMENT[0]["name"], kind="equipment")}, \
        f"{first['id']}: does not surface in equipment search"
