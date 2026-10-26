#!/usr/bin/env python3
"""Convert catalog-sweep results into draft catalog records.

Reads the result JSONs produced by a /catalog-deep sweep, dedups against the
existing catalog, validates values against schema/source.schema.json, and
writes schema-valid DRAFT records into catalog/sources/ as
verification: unverified / reuse_level: catalog-only. Unverified records are
inert: collectors act only on verified records, so drafts wait for the normal
terms-verification workflow.

Result JSONs that cannot produce a valid record are moved to
<results_dir>/_needs_review/ with the reason in REVIEW_REASON.txt.
Raw page snapshots under results_dir/raw/ are left untouched. This tool never
writes to corpus/.

Usage:
    python tools/research_to_catalog.py <results_dir> [more_results_dirs...]
"""

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "source.schema.json"
CATALOG_JSONL = ROOT / "catalog" / "catalog.jsonl"
SOURCES_DIR = ROOT / "catalog" / "sources"

TODAY = date.today().isoformat()

# Conservatism: a sweep record exists because an agent fetched the page, so an
# unstated access defaults to open; everything rights-related stays in the
# project's verification lane.
DEFAULTS = {
    "verification": "unverified",
    "last_verified": None,
    "reuse_level": "catalog-only",
    "access": "open",
    "quality_tier": 3,
    "licence": "unknown",
    "regions": ["global"],
}

OPTIONAL_PROPS = [
    "subtopics", "country", "update_frequency", "content_formats",
    "feeds", "automated_access", "permitted_use", "notes",
]

FLAT_KEYS = ["id", "name", "url", "source_type", "sectors", "disciplines",
             "publisher_org"] + OPTIONAL_PROPS[:8] + list(DEFAULTS)


def load_schema():
    schema = json.loads(SCHEMA_PATH.read_text())
    props = schema["properties"]
    return props, schema.get("required", [])


def flatten(data):
    """Accept flat or category-nested result JSON; return a flat dict."""
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat.setdefault(sub_key, sub_value)
        else:
            flat.setdefault(key, value)
    return flat


def normalize_url(url):
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/")
    return f"{parts.netloc.lower()}{path}"


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:60].strip("-") or "unnamed"


def unique_id(slug, taken_ids):
    if slug not in taken_ids:
        return slug
    n = 2
    while f"{slug}-{n}" in taken_ids:
        n += 1
    return f"{slug}-{n}"


def valid_enum_list(values, enum):
    return (isinstance(values, list) and len(values) > 0
            and all(v in enum for v in values))


def needs_review(results_dir, filename, reason):
    review_dir = results_dir / "_needs_review"
    review_dir.mkdir(exist_ok=True)
    shutil.move(str(results_dir / filename), str(review_dir / filename))
    with open(review_dir / "REVIEW_REASON.txt", "a") as fh:
        fh.write(f"{filename}: {reason}\n")


def build_record(flat, taken_ids, props):
    blocking, advisory = [], []
    name = flat.get("name")
    url = flat.get("url")
    if not name or not isinstance(name, str):
        return None, "missing or non-string 'name'"
    if not url or not isinstance(url, str) or not url.startswith("https://"):
        return None, f"missing or non-https 'url' ({url!r})"

    source_type = flat.get("source_type")
    if source_type not in props["source_type"]["enum"]:
        blocking.append(f"invalid source_type {source_type!r}")
    sectors = flat.get("sectors")
    if not valid_enum_list(sectors, props["sectors"]["items"]["enum"]):
        blocking.append(f"invalid sectors {sectors!r}")
    disciplines = flat.get("disciplines")
    if not valid_enum_list(disciplines, props["disciplines"]["items"]["enum"]):
        blocking.append(f"invalid disciplines {disciplines!r}")
    publisher = flat.get("publisher_org")
    if not publisher or not isinstance(publisher, str) or publisher.strip() == "[uncertain]":
        blocking.append("missing publisher_org")
    if blocking:
        return None, "; ".join(blocking)

    access = flat.get("access")
    if access not in props["access"]["enum"]:
        advisory.append("access defaulted to 'open' (fetch succeeded)")
        access = DEFAULTS["access"]

    regions = flat.get("regions")
    if valid_enum_list(regions, props["regions"]["items"]["enum"]):
        pass
    else:
        if regions is not None:
            advisory.append(f"regions defaulted to ['global'] (sweep gave {regions!r})")
        regions = DEFAULTS["regions"]

    quality_tier = flat.get("quality_tier")
    if not (isinstance(quality_tier, int) and 1 <= quality_tier <= 3):
        advisory.append("quality_tier defaulted to 3 (sweep gave no valid tier)")
        quality_tier = DEFAULTS["quality_tier"]

    licence = flat.get("licence")
    if not isinstance(licence, str) or not licence.strip() or licence.strip() == "[uncertain]":
        licence = DEFAULTS["licence"]
    record = {
        "id": unique_id(slugify(name), taken_ids),
        "name": name.strip(),
        "url": url.strip().rstrip("/"),
        "source_type": source_type,
        "sectors": sectors,
        "disciplines": disciplines,
        "publisher_org": publisher,
        "access": access,
        "licence": licence,
        "reuse_level": DEFAULTS["reuse_level"],
        "quality_tier": quality_tier,
        "verification": DEFAULTS["verification"],
        "last_verified": None,
        "regions": regions,
    }

    dropped = []
    for prop in OPTIONAL_PROPS:
        value = flat.get(prop)
        if value in (None, "", []):
            continue
        spec = props[prop]
        if "enum" in spec and value not in spec["enum"]:
            advisory.append(f"dropped invalid {prop} {value!r}")
            continue
        if spec.get("type") == "array":
            items = spec.get("items", {})
            if "enum" in items and not all(v in items["enum"] for v in value):
                advisory.append(f"dropped invalid {prop} {value!r}")
                continue
            if "pattern" in items and not all(
                    isinstance(v, str) and re.match(items["pattern"], v) for v in value):
                advisory.append(f"dropped invalid {prop} {value!r}")
                continue
        if prop == "country" and isinstance(value, str):
            value = value.upper()
            if not re.match(props["country"]["pattern"], value):
                advisory.append(f"dropped invalid country {value!r}")
                continue
        record[prop] = value

    for key in flat:
        if key not in FLAT_KEYS and key not in props and key not in ("corroboration", "sources"):
            dropped.append(key)

    corroboration = flat.get("corroboration")
    sources = flat.get("sources") or []
    evidence = ""
    if isinstance(corroboration, int):
        evidence += f"corroboration={corroboration}; "
    if sources:
        listed = []
        for src in sources[:5]:
            if isinstance(src, dict) and src.get("url"):
                listed.append(f"{src.get('title', '')} <{src['url']}>".strip())
            elif isinstance(src, str):
                listed.append(src)
        evidence += "sweep sources: " + "; ".join(listed)
    if dropped:
        evidence += f" (unconverted sweep fields: {', '.join(sorted(set(dropped)))})"

    provenance = f"Drafted by catalog sweep {TODAY}; unreviewed. Source JSON: see research run."
    record["notes"] = " ".join(x for x in [provenance, "; ".join(advisory), evidence] if x)
    return record, None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    props, required = load_schema()
    known_ids, known_urls, known_names = set(), set(), set()
    if CATALOG_JSONL.exists():
        for line in CATALOG_JSONL.read_text().splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            known_ids.add(rec["id"])
            known_urls.add(normalize_url(rec["url"]))
            known_names.add(rec["name"].strip().lower())
    else:
        for path in SOURCES_DIR.glob("*.json"):
            rec = json.loads(path.read_text())
            known_ids.add(rec["id"])
            known_urls.add(normalize_url(rec["url"]))
            known_names.add(rec["name"].strip().lower())

    written, dupes, review = [], [], []
    for arg in sys.argv[1:]:
        results_dir = Path(arg)
        if not results_dir.is_dir():
            sys.exit(f"not a directory: {results_dir}")
        for path in sorted(results_dir.glob("*.json")):
            try:
                flat = flatten(json.loads(path.read_text()))
            except json.JSONDecodeError as exc:
                needs_review(results_dir, path.name, f"invalid JSON: {exc}")
                review.append((path.name, "invalid JSON"))
                continue

            url = flat.get("url")
            name = (flat.get("name") or "").strip().lower()
            if isinstance(url, str) and normalize_url(url) in known_urls:
                dupes.append((path.name, "URL already in catalog"))
                continue
            if name and name in known_names:
                dupes.append((path.name, "name already in catalog"))
                continue

            record, reasons = build_record(flat, known_ids, props)
            if record is None:
                needs_review(results_dir, path.name, reasons)
                review.append((path.name, reasons))
                continue

            out = SOURCES_DIR / f"{record['id']}.json"
            out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
            known_ids.add(record["id"])
            known_urls.add(normalize_url(record["url"]))
            known_names.add(record["name"].strip().lower())
            written.append(record["id"])

    print(f"\nWrote {len(written)} draft record(s) to {SOURCES_DIR.relative_to(ROOT)}:")
    for rid in written:
        print(f"  + {rid}")
    if dupes:
        print(f"\nSkipped {len(dupes)} duplicate(s):")
        for fname, why in dupes:
            print(f"  = {fname}: {why}")
    if review:
        print(f"\n{len(review)} file(s) moved to _needs_review/:")
        for fname, why in review:
            print(f"  ! {fname}: {why}")
    if written:
        print("\nNext steps: review the drafts, then `python tools/build.py` "
              "and the terms-verification workflow. Unverified records stay "
              "inert for collectors.")


if __name__ == "__main__":
    main()
