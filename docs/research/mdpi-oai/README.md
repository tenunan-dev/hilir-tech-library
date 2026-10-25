# MDPI OAI-PMH metadata harvest (2026-10-25)

www.mdpi.com blocks automated fetchers (CDN 403), so metadata and abstracts were harvested from the
compliant OAI-PMH endpoint `https://oai.mdpi.com/oai/oai2.php` only. Full text stays on the blocked site
and remains a manual-browser item for the owner — see `docs/LOGIN_REQUIRED.md`.

Contents:

- `<journal>_dedup.jsonl` — deduplicated records (title, authors, abstract, datestamp, DOI, identifier,
  setSpec) per journal: Energies, Catalysts, Processes, Sustainability, Gases, Materials. 850 unique records
  from a ~1.6% sample of the `from=2025-01-01` pool (completeListSize 697,250; MDPI repeats each record once
  per setSpec, up to 6x, hence dedup by identifier).
- `top15.json` — the 15 abstracts most relevant to card gaps (CCUS solvents, CO2-to-methanol/FTS, small-scale
  LNG, gas hydrates, refracturing, tight oil, LOHC, GTL catalysts), each with the DOI and the gap it could inform.
- `parse_summary.json` — per-journal counts.

Harvest scripts (ListRecords oai_dc, sleep 3, default UA, identifier-level ISSN filter) were run from
`/tmp/mdpi_oai/` and are not committed; re-run by following `parse_summary.json` counts and the method note
above. The resumption stream is one global sequence, so extending coverage means resuming pagination.

Ethical note: abstracts are used for card-gap research only; MDPI articles are CC BY but the site's CDN block
on automated access is respected (no full text collected by automation).
