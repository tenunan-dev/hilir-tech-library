"""Validate every catalog record and regenerate the agent-facing indexes.

Outputs:
  catalog/catalog.jsonl         one record per line, for loaders and vector pipelines
  catalog/index/<CODE>.md       one Markdown page per sector and discipline code
  catalog/index/README.md       counts by code, region, source type and reuse level
  catalog/technologies.jsonl    technology cards, one per line
  catalog/index/technologies-<SECTOR>.md  comparison table and block diagrams per sector
  catalog/index/gaps.md         missing inputs: why, where to get them, next action
  catalog/vendors.jsonl         vendor records, one per line
  catalog/index/vendors.md      vendor directory with per-sector coverage and the supplier
                                names on cards that are not yet in the directory
  catalog/equipment.jsonl       equipment records, one per line
  catalog/index/equipment.md    equipment catalog grouped by equipment_type with spec tables
"""
import collections
import json
import pathlib
import re
import sys

import jsonschema
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
import technologies  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = ROOT / "catalog" / "sources"
VENDORS = ROOT / "catalog" / "vendors"
EQUIPMENT = ROOT / "catalog" / "equipment"
INDEX = ROOT / "catalog" / "index"


def load():
    schema = json.loads((ROOT / "schema" / "source.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    records, errors = [], []
    for path in sorted(SOURCES.glob("*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        for err in validator.iter_errors(rec):
            errors.append(f"{path.name}: {'/'.join(map(str, err.path))} {err.message}")
        if rec.get("id") != path.stem:
            errors.append(f"{path.name}: id '{rec.get('id')}' does not match file name")
        records.append(rec)
    return records, errors


def load_technologies(source_ids):
    schema = json.loads((ROOT / "schema" / "technology.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    cards, errors = [], []
    for path in sorted(technologies.CARDS.glob("*.json")):
        card = json.loads(path.read_text(encoding="utf-8"))
        errors += [f"technologies/{path.name}: {'/'.join(map(str, e.path))} {e.message}" for e in validator.iter_errors(card)]
        if card.get("id") != path.stem:
            errors.append(f"technologies/{path.name}: id does not match file name")
        if not errors:
            errors += [f"technologies/{path.name}: {p}" for p in technologies.check(card)]
        unknown = sorted({sid for sid in _source_ids(card) if sid not in source_ids})
        errors += [f"technologies/{path.name}: unknown source_id {sid}" for sid in unknown]
        cards.append(card)
    return cards, errors


def _source_ids(obj):
    if isinstance(obj, dict):
        if "source_id" in obj:
            yield obj["source_id"]
        for v in obj.values():
            yield from _source_ids(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _source_ids(v)


def load_vendors(card_ids, source_ids):
    schema = json.loads((ROOT / "schema" / "vendor.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    vendors, errors = [], []
    for path in sorted(VENDORS.glob("*.json")):
        vendor = json.loads(path.read_text(encoding="utf-8"))
        errors += [f"vendors/{path.name}: {'/'.join(map(str, e.path))} {e.message}" for e in validator.iter_errors(vendor)]
        if vendor.get("id") != path.stem:
            errors.append(f"vendors/{path.name}: id does not match file name")
        unknown = sorted(set(vendor["technologies"]) - card_ids)
        errors += [f"vendors/{path.name}: unknown technology id {t}" for t in unknown]
        unknown_src = sorted({s["source_id"] for s in vendor["sources"] if "source_id" in s} - source_ids)
        errors += [f"vendors/{path.name}: unknown source_id {s}" for s in unknown_src]
        vendors.append(vendor)
    return vendors, errors


def name_key(name):
    """Normalise a vendor name for matching card suppliers to directory records."""
    return re.sub(r"\s+", " ", name.split(" (")[0]).strip().lower()


def vendor_names(vendor):
    return {name_key(n) for n in [vendor["name"]] + vendor.get("aliases", [])}


def vendors_page(vendors, cards, labels):
    """catalog/index/vendors.md: directory by sector plus the coverage queue."""
    by_key = {}
    for v in vendors:
        for key in vendor_names(v):
            by_key[key] = v
    sector_of = {c["id"]: c["sector"] for c in cards}
    card_name = {c["id"]: c["name"] for c in cards}
    covered_sectors = sorted({sector_of[t] for v in vendors for t in v["technologies"]})
    lines = ["# Vendors, suppliers and packagers", "",
             f"{len(vendors)} vendor records covering {len({t for v in vendors for t in v['technologies']})} technologies. One record per vendor in",
             "`catalog/vendors/` (schema `schema/vendor.schema.json`); every record cites the pages it was written from.",
             "The directory grows sector by sector: batch 1 covers modular power plants and the power sector (PWR).", ""]
    for code in covered_sectors:
        hits = sorted((v for v in vendors if {sector_of[t] for t in v["technologies"]} & {code}),
                      key=lambda v: v["name"].lower())
        lines += [f"## {code}: {labels.get(code, code)}", "",
                  "| Vendor | Country | Roles | Supplies |", "| --- | --- | --- | --- |"]
        for v in hits:
            techs = "; ".join(card_name[t] for t in v["technologies"] if sector_of[t] == code)
            url = f"[{v['name']}]({v['url']})" if v.get("url") else v["name"]
            lines.append(f"| {url} | {v['country']} | {', '.join(v['roles'])} | {techs} |")
        lines.append("")
    # Coverage queue: supplier names on cards whose sector has directory entries, or everywhere, minus matches.
    # Compound entries split on "/" and match part by part; what remains is either a nameable
    # vendor candidate (queue) or a descriptive phrase that is not a company name (notes).
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

    queue, notes = {}, {}
    for c in cards:
        for s in c["suppliers"]:
            raw = s["name"]
            if name_key(raw) in by_key:
                continue
            parts = [p.strip() for p in raw.split("/") if p.strip()]
            leftovers = [p for p in parts if name_key(p) not in by_key]
            if len(parts) > 1 and len(leftovers) < len(parts):
                for p in leftovers:
                    bucket = queue if nameable(p) else notes
                    bucket.setdefault(c["sector"], {})[name_key(p)] = p
                continue
            bucket = queue if nameable(raw) else notes
            bucket.setdefault(c["sector"], {})[name_key(raw)] = raw
    lines += ["## Coverage queue: supplier names on cards not yet in the directory", "",
              "Names come from the `suppliers` lists of the technology cards (deduplicated, spelling as found).",
              "Compound entries are split on '/' and matched part by part; descriptive phrases that are not",
              "company names are listed as card notes below. Adding a record for a queue entry is the next",
              "batch of this directory.", ""]
    if queue:
        for code in sorted(queue):
            names = sorted(queue[code].values(), key=str.lower)
            lines.append(f"- **{code}** ({len(names)}): " + "; ".join(names))
    else:
        lines.append("Empty - every named supplier on the cards is in the directory.")
    if notes:
        lines += ["", "## Card notes: generic supplier descriptions (not nameable vendors)", "",
                  "These cards describe their suppliers generically; the strings are not company names.", ""]
        for code in sorted(notes):
            names = sorted(notes[code].values(), key=str.lower)
            lines.append(f"- **{code}** ({len(names)}): " + "; ".join(names))
    matched = sum(1 for c in cards if any(name_key(s["name"]) in by_key for s in c["suppliers"]))
    lines += ["", f"{matched} of {len(cards)} cards list at least one directory vendor.", ""]
    return "\n".join(lines)


def row(rec):
    flag = "" if rec["verification"] == "verified" else " (unverified)"
    regions = ", ".join(rec["regions"])
    return (f"| [{rec['name']}]({rec['url']}) | {rec['source_type']} | {regions} | "
            f"{rec['access']} | {rec['reuse_level']}{flag} |")


def write_indexes(records, taxonomy):
    INDEX.mkdir(parents=True, exist_ok=True)
    codes = {**taxonomy["sectors"], **taxonomy["disciplines"]}
    for code, info in codes.items():
        axis = "sectors" if code in taxonomy["sectors"] else "disciplines"
        hits = [r for r in records if code in r[axis]]
        # Asia Pacific and Southeast Asia first, then by quality tier and name.
        hits.sort(key=lambda r: (not ({"sea", "apac"} & set(r["regions"])), r["quality_tier"], r["name"].lower()))
        lines = [f"# {code}: {info['name']}", "",
                 f"{len(hits)} sources. Sub-topics: {', '.join(info['subtopics'])}.", "",
                 "| Source | Type | Regions | Access | Reuse level |", "| --- | --- | --- | --- | --- |"]
        lines += [row(r) for r in hits]
        (INDEX / f"{code}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def table(title, counter):
        out = [f"## {title}", "", "| Value | Sources |", "| --- | --- |"]
        out += [f"| {k} | {v} |" for k, v in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))]
        return out + [""]

    by_code = collections.Counter(c for r in records for c in r["sectors"] + r["disciplines"])
    summary = ["# Catalog summary", "", f"{len(records)} sources in total.", ""]
    summary += table("By sector and discipline code", by_code)
    summary += table("By region", collections.Counter(g for r in records for g in r["regions"]))
    summary += table("By source type", collections.Counter(r["source_type"] for r in records))
    summary += table("By reuse level", collections.Counter(r["reuse_level"] for r in records))
    summary += table("By verification", collections.Counter(r["verification"] for r in records))
    (INDEX / "README.md").write_text("\n".join(summary), encoding="utf-8")

    # Records a person needs to check by hand: the automated terms check could not confirm them.
    pending = sorted((r for r in records if r["verification"] == "unverified" and "Evidence:" in r.get("notes", "")),
                     key=lambda r: r["id"])
    lines = ["# Needs a manual terms check", "",
             f"{len(pending)} sources whose terms page could not be read automatically.", "",
             "| Source | Current reuse level | Finding |", "| --- | --- | --- |"]
    lines += [f"| [{r['name']}]({r['url']}) | {r['reuse_level']} | {r['notes'].split(' Evidence:')[0]} |" for r in pending]
    (INDEX / "needs-manual-check.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_equipment(vendor_ids, card_ids, source_ids):
    schema = json.loads((ROOT / "schema" / "equipment.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    equipment, errors = [], []
    for path in sorted(EQUIPMENT.glob("*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        errors += [f"equipment/{path.name}: {'/'.join(map(str, e.path))} {e.message}" for e in validator.iter_errors(rec)]
        if rec.get("id") != path.stem:
            errors.append(f"equipment/{path.name}: id does not match file name")
        unknown = sorted(set(rec["vendors"]) - vendor_ids)
        errors += [f"equipment/{path.name}: unknown vendor id {v}" for v in unknown]
        unknown = sorted(set(rec.get("technologies", [])) - card_ids)
        errors += [f"equipment/{path.name}: unknown technology id {t}" for t in unknown]
        unknown = sorted({s["source_id"] for s in rec["sources"] if "source_id" in s} - source_ids)
        errors += [f"equipment/{path.name}: unknown source_id {s}" for s in unknown]
        for line in rec.get("vendor_models", []):
            if line["vendor"] not in vendor_ids:
                errors.append(f"equipment/{path.name}: unknown vendor id {line['vendor']}")
        for spec in rec["specifications"]:
            if "USD" in spec.get("unit", "").upper() and "year" not in spec:
                errors.append(f"equipment/{path.name}: USD cost '{spec['metric']}' needs a dollar year")
        equipment.append(rec)
    return equipment, errors


def spec_cell(spec):
    """The value column of one spec row: single value or a low-high range."""
    if "value" in spec:
        val = spec["value"]
    elif "low" in spec or "high" in spec:
        low, high = spec.get("low", "?"), spec.get("high", "?")
        val = f"{low}" if low == high else f"{low}-{high}"
    else:
        val = spec.get("basis", "")
        return val if len(val) <= 80 else val[:77] + "..."
    return f"{val} {spec['unit']}".strip()


def equipment_page(equipment, vendor_names_by_id, labels):
    """catalog/index/equipment.md: one section per equipment_type with a spec table per record."""
    by_type = collections.defaultdict(list)
    for rec in equipment:
        by_type[rec["equipment_type"]].append(rec)
    lines = ["# Equipment catalog", "",
             f"{len(equipment)} equipment records (one per equipment class, schema `schema/equipment.schema.json`).",
             "Each record carries specification ranges with their sources and the directory vendors that",
             "supply the class. Start of the equipment layer per the owner: boiler first, next families",
             "follow the registration queue.", ""]
    for etype in sorted(by_type):
        lines += [f"## {etype}", ""]
        for rec in sorted(by_type[etype], key=lambda r: r["name"].lower()):
            sector = rec.get("sector", "")
            label = f"{sector}: {labels.get(sector, sector)}" if sector else ""
            site = f" [{rec['name']}]({rec.get('sources')[0]['url']})" if rec["sources"] else ""
            lines += [f"### {rec['name']} ({rec['id']})", ""]
            if label:
                lines.append(f"Primary code: {label}")
            lines.append(rec["description"])
            vendors_listed = [vendor_names_by_id.get(v, v) for v in rec["vendors"]]
            lines += [f"Vendors: {', '.join(vendors_listed)} "
                      f"({len(rec['vendor_models'])} model lines recorded).", "",
                      "| Specification | Value | Basis |", "| --- | --- | --- |"]
            for s in rec["specifications"]:
                basis = s.get("basis", "")
                lines.append(f"| {s['metric']} | {spec_cell(s)} | {basis} |")
            lines.append("")
            for m in rec.get("vendor_models", []):
                name = vendor_names_by_id.get(m["vendor"], m["vendor"])
                head = m.get("line", "")
                lines.append(f"- **{name}** {head}: {m.get('range') or m.get('note', '')}".rstrip())
            gaps = rec.get("gaps", [])
            if gaps:
                lines += ["", "Recorded gaps:", ""]
                lines += [f"- {g['what']} — {g['next_action']}" for g in gaps]
            lines.append("")
    return "\n".join(lines)


def main():
    records, errors = load()
    cards, tech_errors = load_technologies({r.get("id") for r in records})
    errors += tech_errors
    vendors, vendor_errors = load_vendors({c["id"] for c in cards}, {r.get("id") for r in records})
    errors += vendor_errors
    equipment, eq_errors = load_equipment({v["id"] for v in vendors}, {c["id"] for c in cards},
                                          {r.get("id") for r in records})
    errors += eq_errors
    if errors:
        print("\n".join(errors))
        print(f"{len(errors)} validation errors")
        return 1
    ids = collections.Counter(r["id"] for r in records)
    taxonomy = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    labels = {code: info["name"] for code, info in {**taxonomy["sectors"], **taxonomy["disciplines"]}.items()}
    with (ROOT / "catalog" / "catalog.jsonl").open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    write_indexes(records, taxonomy)
    with (ROOT / "catalog" / "technologies.jsonl").open("w", encoding="utf-8") as fh:
        for card in cards:
            fh.write(json.dumps(card, ensure_ascii=False) + "\n")
    with (ROOT / "catalog" / "vendors.jsonl").open("w", encoding="utf-8") as fh:
        for vendor in vendors:
            fh.write(json.dumps(vendor, ensure_ascii=False) + "\n")
    with (ROOT / "catalog" / "equipment.jsonl").open("w", encoding="utf-8") as fh:
        for rec in equipment:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    register = technologies.load_register(cards=cards)
    (INDEX / "technology-register.md").write_text(technologies.register_page(register, labels), encoding="utf-8")
    (INDEX / "gaps.md").write_text(technologies.gaps_page(technologies.gaps(cards, register)), encoding="utf-8")
    for sector in sorted({c["sector"] for c in cards}):
        (INDEX / f"technologies-{sector}.md").write_text(technologies.markdown_page(cards, sector), encoding="utf-8")
    (INDEX / "vendors.md").write_text(vendors_page(vendors, cards, labels), encoding="utf-8")
    (INDEX / "equipment.md").write_text(
        equipment_page(equipment, {v["id"]: v["name"] for v in vendors}, labels), encoding="utf-8")
    print(f"{len(records)} records valid, {len(ids)} unique ids, {len(cards)} technology cards, "
          f"{len(vendors)} vendor records, {len(equipment)} equipment records; indexes written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
