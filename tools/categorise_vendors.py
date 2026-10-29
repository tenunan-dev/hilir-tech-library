#!/usr/bin/env python3
"""A4: rule-based backfill of the vendor `categories` field (schema/vendor.schema.json).

Rules run in order; first match wins within each rule family, and a record can earn up
to 4 categories. Categories describe what KIND of company it is (distinct from roles,
which describe what it does on a project). Idempotent: records that already carry
categories are left alone unless --overwrite.

    python tools/categorise_vendors.py [--overwrite]   # edits catalog/vendors/*.json in place
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VDIR = ROOT / "catalog" / "vendors"

# (category, patterns over the lowercased name+description+products) — checked in order
RULES = [
    ("shipyard", [r"shipyard", r"ship build", r"shipbuild", r"lng carrier", r"vlcc", r"drillship",
                  r"bulk carrier", r"tanker newbuild", r"naval vessel", r"cruise ship", r"offshore \w*yard"]),
    ("offshore-epc", [r"offshore (?:epc|epcic|engineering|contractor)", r"epcic", r"subsea", r"topsides",
                      r"floating (?:production|facility|wind|storage)", r"fpso", r"flng", r"semi-?sub", r"jacket\w*",
                      r"offshore platform", r"offshore wind (?:install|foundat)", r"offshore contractor",
                      r"pipelay", r"pipe-?laying"]),
    ("plant-epc", [r"\bepc\b.{0,40}(?:refin|petrochem|ethylene|ammonia|lng plant|gas plant|power plant|chemical)",
                   r"(?:refin|petrochem|ethylene|ammonia|lng|gas|power|chemical|fertiliz|fertilis)\w* (?:plant|complex).{0,30}\bepc\b",
                   r"\bepc\b", r"epc(?:ic)? (?:contractor|services|solutions)", r"turnkey",
                   r"engineering, procurement"]),
    ("power-rental", [r"power rental", r"rental (?:fleet|genset|power)", r"temporary power", r"mobile power"]),
    ("process-licensor", [r"licens\w+ (?:technolog|process|portfolio)", r"process licens", r"technology licens",
                          r"licens\w+ its? (?:own )?technolog"]),
    ("oilfield-service", [r"oilfield service", r"well (?:services|intervention|completion|abandonment)",
                          r"drilling (?:contractor|services|fluid|risk)", r"coiled tubing", r"wireline",
                          r"completion", r"cementing", r"mud logging", r"directional drilling",
                          r"seismic (?:contractor|acquisition|survey)", r"reservoir (?:service|consult)",
                          r"offshore drilling"]),
    ("engineering-consultancy", [r"consultanc", r"advisory", r"certification (?:body|society)|class(ification)? societ",
                                 r"technical (?:advisor|assurance)", r"inspector", r"\bLR\b|\bDNV\b|\bABS\b|bureau veritas|sgs"]),
    ("fabrication", [r"fabricat", r"weld\w+ shop", r"modular (?:fabrication|build)"]),
    ("utility", [r"electric (?:utility|company)|power (?:utility|company|generator)|electricity (?:generat|supplier)",
                 r"grid operator|transmission system operator|\btso\b|national grid|power producer|IPP\b",
                 r"geothermal (?:operator|developer)|district (?:heating|energy)",
                 r"electricity generation", r"power generation (?:company|group)"]),
    ("operator", [r"\boperator\b", r"operates? (?:power|refiner|plant|field|fleet|stations?|floaters?)",
                  r"independent power producer", r"\bNOC\b", r"national oil", r"supermajor",
                  r"exploration (?:and|&) production", r"\bE&P\b", r"upstream operator",
                  r"own\w* and operat", r"lease-?operator", r"chartered fleet"]),
    ("materials-supplier", [r"coating\w*", r"steel (?:pipe|plate|maker)", r"alloy", r"composite\w*",
                            r"thermoplastic", r"elastomer", r"cement (?:maker|producer)|refractor",
                            r"insulation", r"specialty chemical", r"catalyst (?:maker|manufactur|supplier)",
                            r"industrial[- ]gas", r"seal\w* (?:manufacturer|supplier)", r"polymer\w*"]),
    ("equipment-oem", [r".*"]),  # fallback: oem/supplier of equipment
]


def categories_for(v):
    text = " ".join([v.get("name", ""), v.get("description", ""),
                     " ".join(v.get("products", []) or []),
                     " ".join(v.get("aliases", []) or [])]).lower()
    roles = set(v.get("roles", []))
    out = []
    for cat, pats in RULES:
        if cat in out:
            continue
        for p in pats:
            if re.search(p, text):
                out.append(cat)
                break
    # role-based corrections: epc role without any epc-ish category
    if "epc" in roles and not ({"plant-epc", "offshore-epc"} & set(out)):
        out.insert(0, "plant-epc")
    if "rental" in roles and "power-rental" not in out:
        out.insert(0, "power-rental")
    if "licensor" in roles and "process-licensor" not in out:
        out.insert(1, "process-licensor")
    if not out:
        out = ["equipment-oem"]
    return out[:4]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = 0
    from collections import Counter
    tally = Counter()
    for p in sorted(VDIR.glob("*.json")):
        v = json.loads(p.read_text(encoding="utf-8"))
        if v.get("categories") and not args.overwrite:
            continue
        cats = categories_for(v)
        tally.update(cats)
        if args.dry_run:
            print(f"{v['id']}: {cats}")
            continue
        v["categories"] = cats
        p.write_text(json.dumps(v, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        changed += 1
    mode = "dry-run" if args.dry_run else "written"
    print(f"# {changed} records {mode}; distribution: {dict(tally.most_common())}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
