"""Equipment catalog records: loading and compact rows.

Records live in catalog/equipment/<id>.json (schema/schema/equipment.schema.json; validated by
tools/build.py and tests/test_equipment.py). One record per equipment class, with specification
ranges and their sources, the vendors in the directory that supply it, and recorded gaps.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EQUIPMENT = ROOT / "catalog" / "equipment"


def load_equipment(folder=None):
    base = pathlib.Path(folder or EQUIPMENT)
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*.json"))] if base.is_dir() else []


def summary(rec):
    """Compact row for listings: the spec metrics, not every number."""
    return {"id": rec["id"], "name": rec["name"], "equipment_type": rec.get("equipment_type"),
            "sector": rec.get("sector"), "sector_codes": rec.get("sector_codes", []),
            "aliases": rec.get("aliases", []),
            "spec_metrics": [s["metric"] for s in rec.get("specifications", [])],
            "vendors": rec.get("vendors", []),
            "technologies": rec.get("technologies", [])}
