"""Material catalog: schema validity, link integrity, and index presence."""
import json
import pathlib
import sys

import jsonschema
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "material.schema.json").read_text(encoding="utf-8"))
MATERIALS = [json.loads(p.read_text(encoding="utf-8"))
             for p in sorted((ROOT / "catalog" / "materials").glob("*.json"))]
VENDORS = {v.stem for v in (ROOT / "catalog" / "vendors").glob("*.json")}
EQUIPMENT = {p.stem for p in (ROOT / "catalog" / "equipment").glob("*.json")}


@pytest.mark.parametrize("rec", MATERIALS, ids=[r["id"] for r in MATERIALS])
def test_record_is_valid(rec):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(rec)
    assert all(v in VENDORS for v in rec.get("suppliers", [])), rec["id"]
    assert all(e in EQUIPMENT for e in rec.get("equipment", [])), rec["id"]
    assert all(s["url"].startswith(("http://", "https://")) for s in rec["sources"]), rec["id"]


def test_ids_unique():
    ids = [r["id"] for r in MATERIALS]
    assert len(ids) == len(set(ids))


def test_every_material_has_a_sourced_spec():
    for rec in MATERIALS:
        assert rec["specifications"], rec["id"]
        for spec in rec["specifications"]:
            assert spec.get("basis") or spec.get("note"), (rec["id"], spec["metric"])
            assert "source" in spec, (rec["id"], spec["metric"])


def test_search_index_carries_materials():
    import library
    rows = {r["id"] for r in library.connect().execute("SELECT id FROM materials")}
    assert rows == {r["id"] for r in MATERIALS}
