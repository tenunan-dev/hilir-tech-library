"""Collect documents from verified sources into corpus/.

Usage:
  python collectors/collect.py                 # every collectable source with an adapter
  python collectors/collect.py --source mdpi-energies --limit 5
  python collectors/collect.py --manual        # convert files dropped in corpus/_inbox/<id>/
  python collectors/collect.py --list          # show what would be collected, fetch nothing
"""
import argparse
import sys

from adapters import adapter_for, manual
from common import collectable, load_catalog, write_document


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", action="append", help="source id; repeat for several")
    ap.add_argument("--limit", type=int, default=20, help="documents per source")
    ap.add_argument("--manual", action="store_true", help="only convert hand-downloaded files")
    ap.add_argument("--list", action="store_true", help="list eligible sources and exit")
    args = ap.parse_args(argv)

    catalog = load_catalog()
    ids = args.source or sorted(catalog)
    unknown = [i for i in ids if i not in catalog]
    if unknown:
        print(f"unknown source ids: {', '.join(unknown)}")
        return 2

    jobs = []
    for sid in ids:
        rec = catalog[sid]
        if args.manual:
            # Hand-downloaded files are allowed for any verified source that permits private copies.
            if rec["verification"] == "verified" and rec["reuse_level"] in ("full-text-open", "full-text-restricted"):
                jobs.append((rec, manual))
            continue
        fn = adapter_for(rec)
        if fn and collectable(rec):
            jobs.append((rec, fn))
        elif args.source:
            print(f"skip {sid}: not collectable automatically (verification, reuse level, automated access or no adapter)")

    if args.list:
        for rec, fn in jobs:
            print(f"{rec['id']:28} {fn.__name__:8} {rec['reuse_level']}")
        return 0

    written = errors = 0
    for rec, fn in jobs:
        try:
            for title, url, body, published, extra in fn(rec, args.limit):
                if write_document(rec, title, url, body, published, extra):
                    written += 1
        except Exception as exc:  # one failing source must not stop the run
            errors += 1
            print(f"{rec['id']}: {type(exc).__name__}: {exc}")
    print(f"{written} documents written, {errors} sources failed")
    return 1 if errors and not written else 0


if __name__ == "__main__":
    sys.exit(main())
