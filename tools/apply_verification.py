"""Apply verification findings from tools/verification/log.jsonl to catalog records.

Each log line: {"id", "checked_on", "evidence", "finding", and any record fields to change
(url, licence, reuse_level, access, notes)}. A line with "verified": false records a check
that could not confirm the terms; the record stays unverified but gets the finding in notes.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / "tools" / "verification" / "log.jsonl"
SOURCES = ROOT / "catalog" / "sources"
CHANGEABLE = ("url", "licence", "reuse_level", "access", "update_frequency", "automated_access", "permitted_use")


def main():
    applied = 0
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        path = SOURCES / f"{entry['id']}.json"
        rec = json.loads(path.read_text(encoding="utf-8"))
        for field in CHANGEABLE:
            if field in entry:
                rec[field] = entry[field]
        rec["notes"] = f"{entry['finding']} Evidence: {entry['evidence']}"
        if entry.get("verified", True):
            rec["verification"] = "verified"
            rec["last_verified"] = entry["checked_on"]
        path.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        applied += 1
    print(f"applied {applied} log entries")


if __name__ == "__main__":
    main()
