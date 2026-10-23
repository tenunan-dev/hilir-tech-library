"""Append verification findings: python add.py '<json list of entries>' (checked_on defaults to today)."""
import datetime, json, pathlib, sys
log = pathlib.Path(__file__).with_name("log.jsonl")
today = datetime.date.today().isoformat()
with log.open("a", encoding="utf-8") as fh:
    for e in json.loads(sys.stdin.read()):
        e.setdefault("checked_on", today)
        fh.write(json.dumps(e, ensure_ascii=False) + "\n")
