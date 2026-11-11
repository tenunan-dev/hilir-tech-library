"""Project catalog records: loading and compact rows.

Records live in catalog/projects/<id>.json (schema/project.schema.json; validated by
tools/build.py and tests/test_projects.py). One record per named project or operating
plant: owners, contractors, offtakers, capacities, milestones, and the technology cards
it deploys.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "catalog" / "projects"


def load_projects(folder=None):
    base = pathlib.Path(folder or PROJECTS)
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*.json"))] if base.is_dir() else []


def summary(rec):
    """Compact row for listings: status, location and capacities, not every milestone."""
    return {"id": rec["id"], "name": rec["name"], "aliases": rec.get("aliases", []),
            "project_type": rec.get("project_type"), "sector": rec.get("sector"),
            "sector_codes": rec.get("sector_codes", []), "country": rec.get("country"),
            "location": rec.get("location"), "status": rec.get("status"),
            "capacities": rec.get("capacities", []),
            "technologies": rec.get("technologies", []),
            "owners": [p.get("vendor_id") or p["name"] for p in rec.get("owners", [])]}
