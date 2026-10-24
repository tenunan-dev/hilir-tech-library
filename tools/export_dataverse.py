"""Export the catalog and corpus as CSV files ready to import into Dataverse tables.

    python tools/export_dataverse.py [--out build/dataverse] [--include-restricted]

Writes sources.csv, documents.csv, taxonomy.csv and technologies.csv. By default, document text is included only
for open-licence documents, so the tables are safe in an environment shared with colleagues.
Restricted documents still get a row (title, url, licence) with no text. --include-restricted
adds their text too; use it only for a personal environment no one else can read.
"""
import argparse
import csv
import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "agent"))
import library  # noqa: E402
import technologies  # noqa: E402

SOURCE_COLUMNS = ["name", "source_id", "url", "publisher_org", "country", "source_type", "sectors", "disciplines",
                  "regions", "topics", "access", "licence", "reuse_level", "automated_access", "permitted_use",
                  "quality_tier", "update_frequency", "verification", "last_verified", "notes"]
# A Dataverse multiline text column holds at most 1,048,576 characters.
MAX_BODY = 1_000_000
DOCUMENT_COLUMNS = ["title", "document_id", "source_id", "url", "published", "retrieved_at", "licence", "reuse_level",
                    "permitted_use", "sectors", "disciplines", "content_type", "use_note", "text_included", "body"]


def _fit(body, url):
    if len(body) <= MAX_BODY:
        return body
    return body[:MAX_BODY] + f"\n\n[Truncated for Dataverse; full text at {url}]"


def labels():
    tax = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    return tax, {code: info["name"] for code, info in {**tax["sectors"], **tax["disciplines"]}.items()}


def export(out, include_restricted=False):
    out = pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)
    tax, names = labels()
    records = {r["id"]: r for r in library.load_records()}

    with (out / "sources.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, SOURCE_COLUMNS)
        w.writeheader()
        for rec in records.values():
            codes = rec["sectors"] + rec["disciplines"]
            w.writerow({**{k: rec.get(k, "") for k in SOURCE_COLUMNS}, "source_id": rec["id"],
                        "sectors": ";".join(rec["sectors"]), "disciplines": ";".join(rec["disciplines"]),
                        "regions": ";".join(rec["regions"]), "topics": "; ".join(names[c] for c in codes),
                        "last_verified": rec.get("last_verified") or ""})

    with_text = without_text = 0
    with (out / "documents.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, DOCUMENT_COLUMNS)
        w.writeheader()
        for path in sorted(library.CORPUS.glob("*/*.md")):
            if path.parent.name.startswith("_"):
                continue
            meta, body = library.read_document(path)
            rec = records.get(meta.get("source_id"), {})
            level = meta.get("reuse_level", rec.get("reuse_level"))
            include = level == "full-text-open" or include_restricted
            with_text += include
            without_text += not include
            w.writerow({"title": meta.get("title", "")[:4000], "document_id": meta.get("sha256", ""),
                        "source_id": meta.get("source_id", ""), "url": meta.get("url", ""),
                        "published": meta.get("published") or "", "retrieved_at": meta.get("retrieved_at", ""),
                        "licence": meta.get("licence", ""), "reuse_level": level,
                        "permitted_use": meta.get("permitted_use", ""), "sectors": ";".join(meta.get("sectors", [])),
                        "disciplines": ";".join(meta.get("disciplines", [])), "content_type": meta.get("content", ""),
                        "use_note": meta.get("use_note", ""), "text_included": "yes" if include else "no",
                        "body": _fit(body, meta.get("url", "")) if include else ""})

    with (out / "taxonomy.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["code", "axis", "name", "subtopics"])
        for axis in ("sectors", "disciplines"):
            for code, info in tax[axis].items():
                w.writerow([code, axis[:-1], info["name"], "; ".join(info["subtopics"])])
        for code, name in tax["regions"].items():
            w.writerow([code, "region", name, ""])
    cards = technologies.load_cards()
    with (out / "technologies.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "technology_id", "sector", "category", "maturity", "trl", "applications", "principle",
                    "process_steps", "key_equipment", "suppliers", "costs", "reference_plants", "block_diagram_mermaid",
                    "sources", "last_reviewed"])
        for card in cards:
            sm = technologies.summary(card)
            w.writerow([card["name"], card["id"], card["sector"], card["category"], card["maturity"], sm["trl"] or "",
                        "; ".join(card.get("applications", [])), card["principle"],
                        " -> ".join(s["name"] for s in card["process_steps"]), "; ".join(card["key_equipment"]),
                        "; ".join(sm["suppliers"]), "; ".join(sm["costs"]),
                        "; ".join(f"{p['name']}: {p.get('capacity', '')}" for p in card.get("reference_plants", [])),
                        technologies.mermaid(card), " ".join(s["url"] for s in card["sources"]), card["last_reviewed"]])
    with (out / "technology_register.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, ["name", "code", "area", "maturity", "examples", "card"])
        w.writeheader()
        for e in technologies.load_register(cards=cards):
            w.writerow({**e, "card": e["card"] or ""})
    return {"technologies": len(cards), "sources": len(records), "documents_with_text": with_text, "documents_without_text": without_text}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "build" / "dataverse"))
    ap.add_argument("--include-restricted", action="store_true")
    args = ap.parse_args()
    print(json.dumps(export(args.out, args.include_restricted)))
