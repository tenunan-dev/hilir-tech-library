"""Repair the catalogue against the spec-provenance rule (`tools/spec_sources.py`).

Two operations, both reported before anything is written:

1. **Normalise** every specification's `source_url`: a reader proxy
   (`https://r.jina.ai/<publisher-url>`) becomes the publisher URL, so an agent
   opens the page it should cite.
2. **Prune foreign specifications from equipment records** — the parameter is a
   verbatim twin of another record's specification and this record does not cite
   that source (or the source is a chat transcript, which is not a source).
3. **Drop unevidenced `product.equipment` links** — the field means "classes this
   product supplies", so the class must name the manufacturer among its vendors;
   a link that only matched an equipment *type* is not a supply relationship
   (`tools/spec_sources.py::link_is_evidenced`). The reverse field, an equipment
   record's `vendors`, stays the authority.

Products' own specifications are left alone: they are what their page printed, and
an off-source spec there is a missing `sources` entry, not a foreign figure.

    python tools/spec_source_repair.py            # dry run: the report only
    python tools/spec_source_repair.py --apply    # write the files

Run from the repo root. After an apply: `tools/build.py`, regenerate the index
(`agent/library.py build`), `agent/embed.py --incremental`, then the Neon load
(see docs/PUBLISHING.md).
"""
from __future__ import annotations

import argparse
import collections
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))

import spec_sources as ss  # noqa: E402


def normalise(rec: dict) -> int:
    """Rewrite proxy source_urls in place; return how many specs changed."""
    changed = 0
    for spec in rec.get("specifications") or []:
        before = spec.get("source_url")
        after = ss.norm_url(before)
        if before and after != before:
            spec["source_url"] = after
            changed += 1
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the files (default: report only)")
    args = ap.parse_args()

    index = ss.spec_index()
    by_id = {rec["id"]: rec for _, rec in ss.records("equipment/*.json", "products/*.json")}
    paths = {rec["id"]: path for path, rec in ss.records("equipment/*.json", "products/*.json")}
    equipment_ids = {rec["id"] for _, rec in ss.records("equipment/*.json")}

    # 1. proxy URLs everywhere (equipment and products)
    rewritten = collections.Counter()
    for rec in by_id.values():
        n = normalise(rec)
        if n:
            rewritten[rec["id"]] = n
    total_rewritten = sum(rewritten.values())

    # 2. foreign specs on equipment records
    dropped = {}
    for rid, rec in by_id.items():
        if rid not in equipment_ids:
            continue
        bad = ss.foreign_specs(rec, index)
        if bad:
            dropped[rid] = bad

    total_dropped = sum(len(v) for v in dropped.values())
    emptied = [rid for rid, bad in dropped.items()
               if len(bad) == len(by_id[rid].get("specifications") or [])]

    # 3. unevidenced product -> equipment links
    vendors = ss.vendor_records()
    unlinked = {}
    for rid, rec in by_id.items():
        if rid in equipment_ids:
            continue
        links = rec.get("equipment") or []
        bad = [e for e in links
               if e not in by_id or not ss.link_is_evidenced(rec, by_id[e], vendors)]
        if bad:
            unlinked[rid] = bad

    print(f"proxy source_urls normalised: {total_rewritten} across {len(rewritten)} records")
    for rid, n in rewritten.most_common(5):
        print(f"   {n:4d}  {rid}")
    print(f"foreign specifications on equipment records: {total_dropped} "
          f"across {len(dropped)} records")
    for rid, bad in sorted(dropped.items(), key=lambda kv: -len(kv[1]))[:12]:
        hosts = sorted({ss.host(s.get("source_url")) for s in bad if s.get("source_url")})
        print(f"   {len(bad):4d}/{len(by_id[rid].get('specifications') or []):<4d} {rid}  <- {hosts[:4]}")
    print(f"records that would be left with no specification: {len(emptied)}"
          + (f" {emptied}" if emptied else ""))
    for rid in emptied:
        rec = by_id[rid]
        if not rec.get("gaps"):
            print(f"   ! {rid} would hold no spec and no gap — the build will reject it")
    print(f"unevidenced product -> equipment links: {sum(len(v) for v in unlinked.values())} "
          f"across {len(unlinked)} products")
    for rid, bad in sorted(unlinked.items(), key=lambda kv: -len(kv[1]))[:8]:
        print(f"   {len(bad):3d} {rid}  -> {bad[:3]}")

    if not args.apply:
        print("\ndry run: nothing written (pass --apply)")
        return 0

    for rid, rec in by_id.items():
        if rid not in rewritten and rid not in dropped and rid not in unlinked:
            continue
        if rid in dropped:
            bad_keys = {ss.spec_key(s) for s in dropped[rid]}
            rec["specifications"] = [s for s in rec.get("specifications") or []
                                     if ss.spec_key(s) not in bad_keys]
        if rid in unlinked:
            rec["equipment"] = [e for e in rec.get("equipment") or [] if e not in unlinked[rid]]
        rec["last_reviewed"] = "2026-11-26"
        paths[rid].write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\napplied: {len(set(rewritten) | set(dropped) | set(unlinked))} files rewritten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
