"""Validate every catalog record and regenerate the agent-facing indexes.

Outputs:
  catalog/catalog.jsonl         one record per line, for loaders and vector pipelines
  catalog/index/<CODE>.md       one Markdown page per sector and discipline code
  catalog/index/README.md       counts by code, region, source type and reuse level
"""
import collections
import json
import pathlib
import sys

import jsonschema
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = ROOT / "catalog" / "sources"
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


def main():
    records, errors = load()
    if errors:
        print("\n".join(errors))
        print(f"{len(errors)} validation errors")
        return 1
    ids = collections.Counter(r["id"] for r in records)
    taxonomy = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    with (ROOT / "catalog" / "catalog.jsonl").open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    write_indexes(records, taxonomy)
    print(f"{len(records)} records valid, {len(ids)} unique ids; indexes written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
