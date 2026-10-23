# Maintainer manual

Procedures for people and AI agents who add to or update the library. Read [AGENTS.md](../AGENTS.md) for the rules first.

## Setup

```
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-collect.txt -r requirements-agent.txt pytest
python tools/build.py && pytest -q tests
```

Network note: collection needs direct access to publisher sites. Some cloud sandboxes block them through a proxy; run collectors on a normal machine or in GitHub Actions instead.

## 1. Add a source

1. Check it is not already there: `grep -il "<name>" catalog/sources/*.json`.
2. Create `catalog/sources/<id>.json`. Use a short kebab-case id that matches the file name. Fill every required field (see [ARCHITECTURE.md](ARCHITECTURE.md#catalog-record-schemasourceschemajson)). Start with `"verification": "unverified"`, `"last_verified": null`, and a cautious `reuse_level` (`summary-only` unless the licence is plainly open).
3. Tag at least one sector and one discipline. Add `sea` or `apac` to `regions` where they apply.
4. Run `python tools/build.py`, then commit the record and regenerated files together.

Paid or login-only sources are `catalog-only`, with `access: paywalled` or `free-registration`.

## 2. Verify a source's terms

1. Open the site's terms of use, copyright or licence page, and its `robots.txt`.
2. Decide the fields:

| Terms say | reuse_level | permitted_use |
| --- | --- | --- |
| Open licence (CC BY, public domain, OGL and similar) | full-text-open | any |
| Personal or non-commercial copies allowed | full-text-restricted | personal-non-commercial |
| Internal use within an organisation allowed | full-text-restricted | internal-organisation |
| No terms published, content freely downloadable | full-text-restricted | unstated |
| Copying or reproduction forbidden | summary-only | none |
| Bans AI or machine-learning use | catalog-only | none |
| Paywalled or login required | catalog-only | |

   Set `automated_access` to `prohibited` if the terms or robots.txt ban crawlers, `allowed` if they explicitly permit it, else `unstated`.
3. Append an entry to the log (one JSON object per line) and apply it:

```
echo '[{"id": "example", "evidence": "https://example.org/terms", "finding": "Terms allow personal non-commercial copies; robots.txt allows crawling.", "reuse_level": "full-text-restricted", "permitted_use": "personal-non-commercial", "automated_access": "unstated", "licence": "proprietary"}]' | python tools/verification/add.py
python tools/apply_verification.py
python tools/build.py
```

   If you could not read the terms, add `"verified": false` and say why in `finding`; the record then appears in `catalog/index/needs-manual-check.md` for a person to check.

## 3. Collect content

```
python collectors/collect.py --list                    # what is eligible, no network
python collectors/collect.py --source osti --limit 3   # trial run first
python collectors/collect.py --source osti --limit 25
python collectors/collect.py                           # all eligible sources
python tools/build.py && python agent/library.py build
```

For a new or changed source, always do the trial run (`--limit 3`) first and open one new file under `corpus/<id>/`. It must have front matter with `licence` and `url`, and a body of real article text (or the abstract), not navigation boilerplate or an empty page. If it fails, stop and look at the raw response (see Troubleshooting) before collecting more.

Before committing, open a few new files and check they are on topic (`grep -h '^title:' corpus/<id>/*.md` lists the titles). Remove off-topic files together with their lines in `corpus/manifest.jsonl` (match on `"path": "corpus/<id>/<file>"`). Then check the manifest still matches the files: these two numbers must be equal.

```
wc -l < corpus/manifest.jsonl
find corpus -name '*.md' -not -path 'corpus/_*' -not -name README.md | wc -l
```

Commit `corpus/` with a message naming the source and the count.

### Manual inbox (sites that ban crawlers or block the collector)

1. Download the PDF or save the HTML page by hand into `corpus/_inbox/<source-id>/`.
2. Next to each file, create `<file>.url` containing the original URL.
3. Run `python collectors/collect.py --manual`. The record must be verified with a full-text reuse level.

### Add an adapter

Write a generator in `collectors/adapters.py` that yields `(title, url, body_markdown, published, extra_dict)`, use `fetch()` for every request, and register it in `ADAPTERS` under the source id. Add an offline test in `tests/test_collectors.py` that replaces `fetch` with fixtures. If the source only needs RSS, add `feeds` to its record instead.

### Tuning the arXiv search

`ARXIV_QUERY` in `collectors/adapters.py` matches title phrases only. Bare words like "pipeline", "flare", "compressor" and "carbon capture" pulled in software, astronomy and biology papers, so use qualified phrases. After a change, run a collection of 25 and check how many results are on topic before committing.

## 4. Refresh and link checks

- `.github/workflows/refresh.yml` runs weekly (collection) and monthly (adds the link check). Trigger it by hand from the Actions tab.
- `python tools/check_links.py` writes `catalog/index/link-check.md`. A failing link is a prompt to re-check the record (many sites block bots); a redirect usually means the record's `url` should be updated through a verification log entry.

## 5. Search index and MCP server

- Rebuild after any change: `python agent/library.py build`, then `python agent/embed.py` if semantic search is used.
- To change ranking, edit `BM25`, `REGION_BOOST` or the coverage sort in `agent/library.py` and keep `tests/test_agent.py` passing. Spot-check with `python agent/library.py search <query>`.
- To add an MCP tool, add a function in `agent/library.py` with a test, then a thin `@server.tool()` wrapper in `agent/server.py`.

## 6. Finishing a session

1. `python tools/build.py && pytest -q tests` pass.
2. Update [STATUS.md](STATUS.md) and, for new rules or owner decisions, [DECISIONS.md](DECISIONS.md).
3. Commit with a message that says what changed and why. Push.

## 7. Troubleshooting

When a collector fails, look at what the server actually sent before changing code:

```
python - <<'EOF'
import sys; sys.path.insert(0, "collectors"); import requests, common
r = requests.get("<url>", headers={"User-Agent": common.USER_AGENT}, timeout=60)
print(r.status_code, r.headers.get("Content-Type")); print(r.text[:800])
EOF
```

Make the smallest fix that works, add or update an offline test with a fixture copied from the real response, and note the fix in STATUS.md.

| Problem | Cause and fix |
| --- | --- |
| `403` on every request | The host blocks the collector or the network proxy blocks the host. Do not work around a site's block; use the manual inbox or ask the publisher |
| `robots.txt disallows` | Respect it. A new exception needs the owner's approval and a DECISIONS.md entry |
| JSONDecodeError from an API | It returned XML or HTML; send an `Accept` header through `fetch(url, headers=...)` |
| `403` with an "Access Denied" HTML page (Akamai, Cloudflare), even for robots.txt | CDN bot protection for our user agent. Same rule as any block: no workaround. Record it in STATUS.md |
| XML `ParseError` on a feed | The feed URL returned HTML (an error or login page). Print the body and fix `feeds` in the record |
| Nothing written, no error | Empty bodies are skipped: the text extractor found no article in the page. Inspect the HTML; the site may need its own adapter or the manual inbox |
| Most collected documents off topic | The source query is too broad (see "Tuning the arXiv search"). Do not commit; narrow the query and rerun |
| CI fails on "Generated files are up to date" | Run `python tools/build.py` and commit `catalog/` |
| Duplicate documents not written | Expected: identical text is skipped by SHA-256 |
