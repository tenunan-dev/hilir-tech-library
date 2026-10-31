"""Vendor directory records: loading and compact rows.

Records live in catalog/vendors/<id>.json (schema/schema/vendor.schema.json; validated by
tools/build.py and tests/test_vendors.py). One record per vendor, supplier or packager, with the
technology cards it supplies and the pages the record was written from.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
VENDORS = ROOT / "catalog" / "vendors"


def load_vendors(folder=None):
    base = pathlib.Path(folder or VENDORS)
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*.json"))] if base.is_dir() else []


def name_key(name):
    """Normalise a name for matching card suppliers to directory records (same rule as tools/build.py)."""
    return re.sub(r"\s+", " ", name.split(" (")[0]).strip().lower()


def vendor_keys(vendor):
    """Every key this record answers to: its name and its aliases."""
    return {name_key(n) for n in [vendor["name"]] + vendor.get("aliases", [])}


def summary(vendor):
    """Compact row for listings."""
    return {"id": vendor["id"], "name": vendor["name"], "country": vendor.get("country"),
            "roles": vendor.get("roles", []), "aliases": vendor.get("aliases", []),
            "products": vendor.get("products", []), "url": vendor.get("url"),
            "technologies": vendor.get("technologies", [])}


def coverage_queue(cards, records):
    """Supplier names on technology cards that no vendor directory record answers to, by sector.

    Same rules as catalog/index/vendors.md (tools/build.py): compound entries split on '/' and
    match part by part; leftovers are either nameable vendor candidates (queue) or descriptive
    phrases that are not company names (notes). `cards` are card dicts (id, sector, suppliers),
    `records` vendor dicts (name, aliases) — fed from the catalog files by web.py or from
    og.technology / og.vendor by pg.coverage_queue.
    """
    covered = set()
    for v in records:
        covered |= vendor_keys(v)
    note_start = re.compile(
        r"^(no |none |various |major |operators?|governments?|terminal |research |epc |contractors?|"
        r"producers|licensors|consortia|programmes?|projects |stage|doe-funded|see )", re.I)
    note_contains = re.compile(
        r"\b(vendors|licensors|contractors|producers|operators|groups|programmes|consortia|companies)\b|"
        r"none named|identified in", re.I)

    def nameable(text):
        head = re.sub(r"\([^)]*\)", "", text).strip()
        if not head or note_start.search(head) or note_contains.search(head):
            return False
        return len(head.split()) <= 6

    def classify(name):
        parts = [p.strip() for p in name.split("/") if p.strip()]
        leftovers = [p for p in parts if name_key(p) not in covered]
        if len(parts) > 1 and len(leftovers) < len(parts):
            return leftovers, []
        if nameable(name):
            return [name], []
        return [], [name]

    queue, notes = {}, {}
    for c in cards:
        for s in c["suppliers"]:
            raw = s["name"]
            if name_key(raw) in covered:
                continue
            q_parts, n_parts = classify(raw)
            for p in q_parts:
                queue.setdefault(c["sector"], {})[name_key(p)] = p
            for p in n_parts:
                notes.setdefault(c["sector"], {})[name_key(p)] = p
    return (sorted((code, sorted(names.values(), key=str.lower)) for code, names in queue.items()),
            sorted((code, sorted(names.values(), key=str.lower)) for code, names in notes.items()))
