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
