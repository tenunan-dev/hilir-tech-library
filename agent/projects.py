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
    # A blank location/capacities/owners row is often a RECORDED gap, not an oversight —
    # surface the gap count so callers can tell the two apart (get_project has the detail).
    gaps = len(rec.get("gaps", []))
    stub = bool(rec.get("stub")) or (
        gaps == 0 and not rec.get("location") and not rec.get("capacities", []) and not rec.get("owners", []))
    return {"id": rec["id"], "name": rec["name"], "aliases": rec.get("aliases", []),
            "project_type": rec.get("project_type"), "sector": rec.get("sector"),
            "sector_codes": rec.get("sector_codes", []), "country": rec.get("country"),
            "location": rec.get("location"), "status": rec.get("status"),
            "capacities": rec.get("capacities", []),
            "technologies": rec.get("technologies", []),
            "owners": [p.get("vendor_id") or p["name"] for p in rec.get("owners", [])],
            "gaps": gaps, "stub": stub}


# Records store countries in mixed spellings ("US" and "United States", "CA" and "Canada"), so a
# country filter canonicalises both sides through this map before comparing.
COUNTRY_ALIASES = {
    "us": "united states", "usa": "united states", "ca": "canada", "uk": "united kingdom",
    "gb": "united kingdom", "uae": "united arab emirates", "kr": "south korea",
    "id": "indonesia", "my": "malaysia", "sg": "singapore", "nl": "netherlands",
    "sa": "saudi arabia", "jp": "japan", "au": "australia", "no": "norway",
}


def country_matches(value, param):
    """Case-insensitive country filter: canonicalise both sides, then exact match, or substring
    only when the shorter side is at least four characters ("united" matches "United States";
    a two-letter code matches only through the alias map, never as a random substring)."""
    want = (param or "").strip().lower()
    have = (value or "").strip().lower()
    if not want:
        return True
    if not have:
        return False
    want = COUNTRY_ALIASES.get(want, want)
    have = COUNTRY_ALIASES.get(have, have)
    if want == have:
        return True
    return (len(want) >= 4 and want in have) or (len(have) >= 4 and have in want)
