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


def source_urls(rec):
    """Every URL this equipment class cites, so an agent can open the original datasheet."""
    urls = [s.get("source", {}).get("url", "") for s in rec.get("specifications", [])]
    urls += [s.get("url", "") for s in rec.get("sources", [])]
    for line in rec.get("vendor_models", []):
        if line.get("url"):
            urls.append(line["url"])
    return list(dict.fromkeys(u for u in urls if u.startswith("http")))


def summary(rec):
    """Compact row for listings: the spec metrics and original source URLs, not every number."""
    return {"id": rec["id"], "name": rec["name"], "equipment_type": rec.get("equipment_type"),
            "sector": rec.get("sector"), "sector_codes": rec.get("sector_codes", []),
            "aliases": rec.get("aliases", []),
            "spec_metrics": [s["metric"] for s in rec.get("specifications", [])],
            "vendors": rec.get("vendors", []),
            "technologies": rec.get("technologies", []),
            "source_urls": source_urls(rec),
            "gaps": len(rec.get("gaps", []))}
