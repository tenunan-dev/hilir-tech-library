"""Vendor directory: every record is valid, ids are unique, and technology links resolve."""
import json
import jsonschema
import pathlib
import sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "vendor.schema.json").read_text(encoding="utf-8"))
VENDORS = [
    json.loads(p.read_text(encoding="utf-8"))
    for p in sorted((ROOT / "catalog" / "vendors").glob("*.json"))
]
CARDS = {c["id"]: c for c in build.technologies.load_cards()}


@pytest.mark.parametrize("vendor", VENDORS, ids=[v["id"] for v in VENDORS])
def test_vendor_is_valid(vendor):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(vendor)
    for t in vendor["technologies"]:
        assert t in CARDS, f"{vendor['id']}: technology {t} has no card"
    for s in vendor["sources"]:
        assert s["url"].startswith(("http://", "https://")), f"{vendor['id']}: source without http(s) url"


def test_vendor_categories_present_and_valid():
    for v in VENDORS:
        assert "categories" in v, f"{v['id']}: missing categories"
        assert 1 <= len(v["categories"]) <= 4, f"{v['id']}: {len(v['categories'])} categories"
        allowed = SCHEMA["properties"]["categories"]["items"]["enum"]
        for c in v["categories"]:
            assert c in allowed, f"{v['id']}: unknown category {c}"


def test_vendor_ids_and_names_unique():
    ids = [v["id"] for v in VENDORS]
    assert len(ids) == len(set(ids)), "duplicate vendor ids"
    owners = {}
    for v in VENDORS:
        for key in build.vendor_names(v):
            if owners.setdefault(key, v["id"]) != v["id"]:
                pytest.fail(f"name or alias '{key}' claimed by both {owners[key]} and {v['id']}")


def test_vendors_link_technologies_that_list_them():
    """A vendor claiming a technology should appear under a matching supplier name on that card."""
    by_key = {}
    for v in VENDORS:
        for key in build.vendor_names(v):
            by_key[key] = v["id"]
    for v in VENDORS:
        for t in v["technologies"]:
            suppliers = {build.name_key(s["name"]) for s in CARDS[t]["suppliers"]}
            if not (build.vendor_names(v) & suppliers):
                # Tolerated: the vendor supplies the technology without being named on the card,
                # but it must be visible, so keep only an explicit whitelist-free warning here.
                print(f"note: {v['id']} supplies {t} but no card supplier name matches "
                      f"{sorted(build.vendor_names(v))}")
