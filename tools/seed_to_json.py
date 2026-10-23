"""One-time import: turn the pipe-separated seed lists into one JSON record per source.

Existing JSON records are never overwritten, so edits made to catalog/sources/*.json survive a re-run.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SEED_DIR = ROOT / "tools" / "seed"
OUT_DIR = ROOT / "catalog" / "sources"
FIELDS = ["id", "name", "url", "source_type", "sectors", "disciplines", "publisher_org", "country",
          "regions", "access", "licence", "reuse_level", "quality_tier", "update_frequency", "notes"]
LIST_FIELDS = {"sectors", "disciplines", "regions"}

# Records whose URL and licence were checked by hand when the catalog was seeded.
VERIFIED = {"mdpi-energies": "2026-10-23"}


def parse(line):
    values = [v.strip() for v in line.split("|")]
    if len(values) != len(FIELDS):
        raise ValueError(f"expected {len(FIELDS)} fields, got {len(values)}: {line[:60]}")
    rec = dict(zip(FIELDS, values))
    for f in LIST_FIELDS:
        rec[f] = [v.strip() for v in rec[f].split(",") if v.strip()]
    rec["quality_tier"] = int(rec["quality_tier"])
    if not rec["notes"]:
        del rec["notes"]
    if not rec["update_frequency"]:
        del rec["update_frequency"]
    rec["verification"] = "verified" if rec["id"] in VERIFIED else "unverified"
    rec["last_verified"] = VERIFIED.get(rec["id"])
    return rec


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = skipped = 0
    for path in sorted(SEED_DIR.glob("*.psv")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            rec = parse(line)
            target = OUT_DIR / f"{rec['id']}.json"
            if target.exists():
                skipped += 1
                continue
            target.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            written += 1
    print(f"wrote {written} records, kept {skipped} existing")


if __name__ == "__main__":
    sys.exit(main())
