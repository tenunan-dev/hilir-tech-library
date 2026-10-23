"""Check every catalog url and write catalog/index/link-check.md.

Uses HEAD, then GET when HEAD is refused, one request per host every 3 seconds. A failure here
is a prompt to re-verify the record, not proof the source is gone: many sites block bots.
"""
import collections
import datetime
import json
import pathlib
import sys
import time
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "collectors"))
from common import USER_AGENT  # noqa: E402


def check(url):
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = requests.head(url, headers=headers, timeout=30, allow_redirects=True)
        if resp.status_code in (403, 405, 501):
            resp = requests.get(url, headers=headers, timeout=30, allow_redirects=True, stream=True)
            resp.close()
        moved = resp.url.rstrip("/") != url.rstrip("/")
        return resp.status_code, resp.url if moved else ""
    except requests.RequestException as exc:
        return None, type(exc).__name__


def main():
    records = [json.loads(line) for line in (ROOT / "catalog" / "catalog.jsonl").read_text(encoding="utf-8").splitlines()]
    last, rows, counts = {}, [], collections.Counter()
    for rec in sorted(records, key=lambda r: urllib.parse.urlsplit(r["url"]).netloc):
        host = urllib.parse.urlsplit(rec["url"]).netloc
        wait = 3.0 - (time.monotonic() - last.get(host, 0.0))
        if wait > 0:
            time.sleep(wait)
        last[host] = time.monotonic()
        status, note = check(rec["url"])
        ok = status is not None and status < 400
        counts["ok" if ok else "problem"] += 1
        if not ok or note:
            rows.append(f"| {rec['id']} | {rec['url']} | {status or '-'} | {note} |")
    today = datetime.date.today().isoformat()
    lines = [f"# Link check, {today}", "", f"{counts['ok']} reachable, {counts['problem']} with problems. "
             "Listed below: problems, and urls that redirect elsewhere (consider updating the record).", "",
             "| Source | URL | Status | Redirect or error |", "| --- | --- | --- | --- |"] + sorted(rows)
    (ROOT / "catalog" / "index" / "link-check.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{counts['ok']} ok, {counts['problem']} problems")


if __name__ == "__main__":
    main()
