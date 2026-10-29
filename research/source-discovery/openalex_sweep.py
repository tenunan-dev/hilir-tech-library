#!/usr/bin/env python3
"""A8 (channel 2): OpenAlex venue-frequency sweep over corpus documents.

Takes up to N document titles from corpus/manifest.jsonl, finds each work on OpenAlex
via curl, then pulls works citing it and groups those citing works by their venue.
Venues cited >= 3 times across the doc set that are absent from the catalog are
flagged. Writes research/source-discovery/openalex-venues.txt. Stdlib + curl only.
Requests go ONLY to https://api.openalex.org (fixed host constant).
"""
import json
import pathlib
import subprocess
import sys
import time
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[2]  # repo root (script lives in research/source-discovery/)
API = "https://api.openalex.org"  # fixed allowlisted host
PER_PAGE = 50
OUT = ROOT / "research" / "source-discovery" / "openalex-venues.txt"

cat_blob = (ROOT / "catalog" / "catalog.jsonl").read_text(encoding="utf-8", errors="ignore").lower()


def api_get(path_and_query, tries=3):
    url = f"{API}{path_and_query}"
    for i in range(tries):
        r = subprocess.run(["curl", "-sf", "--max-time", "30", url],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout:
            try:
                return json.loads(r.stdout)
            except json.JSONDecodeError:
                pass
        time.sleep(2 * (i + 1))
    print(f"FAIL {url}", flush=True)
    return None


def main():
    n_docs = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    titles = []
    for md in (ROOT / "corpus").rglob("*.md"):
        if "_inbox" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")[:600]
        for line in text.splitlines():
            if line.startswith("title:"):
                t = line.split(":", 1)[1].strip().strip('"').strip("'")
                # report-style titles: keep the head before any colon, max 12 words
                t = t.split(":")[0]
                words = t.split()
                if len(words) > 12:
                    t = " ".join(words[:12])
                if len(t) > 25:
                    titles.append(t)
                break
    titles = titles[:n_docs]
    print(f"{len(titles)} titles", flush=True)

    venue_counts = {}
    for i, title in enumerate(titles):
        q = urllib.parse.quote(title[:200])
        res = api_get(f"/works?filter=title.search:{q}&per-page=1&select=id,display_name")
        time.sleep(1.1)
        if not res or not res.get("results"):
            print(f"[{i+1}] no match: {title[:60]}", flush=True)
            continue
        wid = res["results"][0]["id"].rsplit("/", 1)[-1]
        cursor = "*"
        while cursor:
            page = api_get(f"/works?filter=cites:{wid}&per-page={PER_PAGE}"
                           f"&select=primary_location&cursor={cursor}")
            time.sleep(1.1)
            if not page:
                break
            for w in page.get("results", []):
                loc = w.get("primary_location") or {}
                src = (loc.get("source") or {}).get("display_name")
                if src:
                    venue_counts[src] = venue_counts.get(src, 0) + 1
            cursor = page.get("meta", {}).get("next_cursor")
        print(f"[{i+1}/{len(titles)}] {title[:60]} -> {wid}", flush=True)

    lines = ["OpenAlex venue sweep (venues of works citing our corpus docs)", "=" * 60]
    flagged = []
    for venue, n in sorted(venue_counts.items(), key=lambda kv: -kv[1]):
        low = venue.lower()
        absent = low[:40] not in cat_blob and low not in cat_blob
        if n >= 3 and absent:
            flagged.append((venue, n))
        lines.append(f"{n:4d}  [{'ABSENT' if absent else 'known'}]  {venue}")
    lines += ["", f"FLAGGED ({len(flagged)}) — queue as channel-2 candidates:"]
    for venue, n in flagged:
        lines.append(f"  {venue} ({n})")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}; flagged {len(flagged)} venues", flush=True)


if __name__ == "__main__":
    main()
