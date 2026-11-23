# Response to finding TL-S1 — "exact card ranked below unrelated cards"

Finding under test: *Technology Library (hilir-techlib) · TL-S1 · Low · search — exact card ranked
below unrelated cards* (`search(query="carbon capture amine", limit=5)`, `ccs-amine-post-combustion`
absent from the top 5).

Method: reproduced against the **live** MCP server (`techlib-api.hilir.app`) and the SQLite fallback;
read both ranking implementations (`db/schema.sql` `og.hybrid_search`, `agent/library.py`
`search()`); measured every proposed remedy against the production data before changing anything.
Shipped 2026-11-23 in commits `7e0a67c` and `4c47ec3` on `phase4-auth`; container api
`sha256:9ee3f58c724b…`, ui `sha256:03c3e6f9a545…`.

## Verdict

| Finding | Verdict | Evidence |
|---|---|---|
| TL-S1 — `search("carbon capture amine", limit=5)` omits `ccs-amine-post-combustion` | **Confirmed** | Live, before the fix: ranks 1–5 were DAC liquid solvent, electro-swing DAC, enzyme capture, syngas solvent, amine AGR; the card was **6th** |
| "The card is not in the top 5" | **Confirmed; worse in substance than reported** | It was **keyword rank 9** of its pool (fused 6th). The report's own control case was also confirmed |
| Diagnosis "the card matches one term" | **Not correct** | The card matches **two** of three terms (`amine`, `capture`, both in its name). See §2 |
| Proposed fix "boost the title/name field" | **Measured insufficient** | Title weighting alone moves the card from rank 9 to **rank 6** — still outside the reported top 5. See §2 |
| Acceptance test `search("carbon capture amine", limit=3)` includes the card | **Passes** | Live: **position 1** (0.0426). See §6 |

## 1. Reproduction (before the fix)

```
search("carbon capture amine", limit=5)          # live, kind="all"
1 Direct air capture with liquid solvent (KOH and calcium loop)   0.0395
2 Electro-swing and moisture-swing DAC                            0.0394
3 Enzyme-catalysed capture                                        0.0391
4 Chemical solvent capture from syngas (hydrogen plants)          0.0389
5 Amine acid gas removal (MDEA, formulated amines)                0.0387
6 Amine solvent post-combustion capture                           0.0386   <-- the answer
```

Two observations that shaped the fix:

- **The top six scores differ by 0.0009.** Reciprocal-rank fusion (`1/(60+rank)`) flattens the head,
  so reordering ranks 1–10 is cheap; micro-tuning the fusion constant would not have been a fix.
- **The card is rankable.** The report's control query `"post-combustion amine capture"` returned it
  **first** (0.0426) on the same server. The defect is therefore vocabulary and coverage, not the
  card or its metadata.

## 2. Where the diagnosis and the proposed fix do not hold

**The card does not match one term.** Its name is *Amine solvent post-combustion capture*: `amine`
and `capture` are both present. The term it lacks is **`carbon`**, because the card — correctly —
is written in **CO2**. The indexed text was `name || ' ' || category || ' ' || principle`
(`db/schema.sql`), and none of those three fields contains the string "carbon".

**Why that decided the order.** The keyword pool ranked on `ts_rank_cd` alone, which (a) is already a
term-wise sum — so more literal terms means a higher score — and (b) had **no title weight at all**
(the `tsv` was a flat concatenation, with no `setweight`). Cards that happen to write "carbon"
(BECCS 0.6, flue-gas carbon capture 0.6, DAC 0.5, molten carbonate 0.4) beat the card's 0.3 on
word count, not on relevance.

**The proposed remedy, measured.** Every candidate was run against the production data read-only:

| Candidate | Result for `carbon capture amine` |
|---|---|
| `setweight` on name (A) + body (B) — *the report's proposal* | kw rank **6** (2.4): still behind flue-gas carbon capture (3.6), molten carbonate (2.8), DAC (2.6) |
| Synonym expansion `carbon\|co2` alone | 0.6 tie cluster, ~rank 7 |
| Additive per-concept density | **identical** to the old score — `ts_rank_cd` already sums per term |
| **Concept coverage, then density** | kw rank 2, **#1 fused** — shipped |

The reason coverage wins: "carbon capture amine" is an implicit **conjunction**. A record that
answers all three parts (the amine card: amine ✓, capture ✓, carbon ✓ via CO2) must outrank a record
that answers one part very often (BECCS: carbon ✓, capture ✓, amine ✗). Lexicographic coverage is
also immune to the failure mode of a weighted sum — a long document that mentions everything.

## 3. Root cause, stated plainly

1. **No coverage signal and no title weight** in either engine. Neon had none at all; the SQLite
   path approximated coverage with a raw substring count over `title+text+tags`, which §5 shows was
   its own, worse defect.
2. **No vocabulary bridging.** The catalogue writes the molecule (`CO2`); users type the element
   (`carbon`). Nothing mapped them.
3. **The two engines did not index the same text.** Neon indexed name + category + principle; the
   SQLite index additionally carried aliases, applications, key equipment, supplier names, maturity
   and cost/performance metrics. The documented "the two paths rank alike" claim covered the boosts
   only.

## 4. What changed

- **`catalog/search-concepts.yaml`** — query-side concept groups; one group today,
  `carbon: [carbon, co2]`. Read by `agent/library.py`, seeded into the new **`og.search_concept`**
  table by `tools/load_postgres.py`, so both engines expand a query identically.
- **`og.hybrid_search`** (`db/schema.sql`) — the query is tokenised (subscript digits folded, so
  `CO₂` = `CO2`), expanded through the concept groups, and the keyword pool orders by
  `coverage DESC, ts_rank_cd DESC`.
- **`agent/library.py`** — same expansion and coverage key; keyword and vector pools are now
  **per kind** (50 candidates each, mirroring the SQL function).
- **`agent/technologies.search_text(card)`** and a `search_text` column on the four curated tables,
  with `tsv = setweight(name,'A') || setweight(search_text,'B')` — one index string for both engines.
- **`technologies.search_text` / `library.vendor_text|equipment_text|project_text`** are now the
  loader's input, closing the index-text gap.
- Tests: concept coverage + vocabulary bridging on the SQLite fixture; a cross-layer parity test
  asserting the acceptance query and the card's full text in the Postgres index.

## 5. Further defects found in the same area (not in the report)

| Defect | Evidence | Status |
|---|---|---|
| **Postgres indexed only name/category/principle.** A card's own supplier and process names found it on the baked index and *not at all* on Neon | `search("KS-1 solvent")`, `search("KM CDR")` → card #1 on SQLite, absent on Neon | Fixed: shared `search_text` |
| **The SQLite fallback fused one global rank pool** and sorted by raw substring count, so a corpus document's title claimed every query word | `search("carbon capture amine", kind="all", limit=50)` → **47 chunks, 1 vendor, 2 unrelated cards**, card absent. Now 24 cards, 8 vendors, 8 projects, 8 chunks, 1 equipment, 1 source | Fixed: per-kind pools |
| **`search(kind=…)` was empty for equipment, projects and passages on Neon** — the kind filtered a global top-k that the curated kinds dominate | `search("boiler blowdown", kind="equipment")` → `[]` on Neon, four boiler records on SQLite | Fixed: `hybrid_search_kind(…, kind_filter)` filters inside the ranking; the 7-argument `hybrid_search` stays as a wrapper so a schema apply never strands a running client |
| **A query with no words returned nearest vectors** (arbitrary cards) | `search("!!!")` → 3 unrelated cards | Fixed: both paths return `[]` |

## 6. Verification

- `python tools/build.py` → **526 records valid**; `pytest -q tests` → **1,429 passed, 13 skipped**
  (1,427 at the first cut, before the follow-up in §7 added its tests).
- Neon reloaded: 526 sources / 289 documents / 13,624 open-licence chunks / 391 cards / 537 vendors /
  37 equipment / 295 projects / 406 register / 4,391 nodes / 13,205 edges / 16,902 vectors;
  `og.search_concept` seeded (`carbon:carbon`, `carbon:co2`).
- **Acceptance test, live** (ZCode MCP, hosted server):

```
search("carbon capture amine", limit=3)
1 Amine solvent post-combustion capture      0.0426   <-- required card, first
2 Amine acid gas removal (MDEA, …)           0.0416
3 Emerging capture: water-lean solvents, …   0.0401
```

- Related live checks after the fix: `KS-1 solvent` → card returned (4th; was absent),
  `KS-1 amine solvent` → first, `kind=equipment` + `boiler blowdown` → three boiler records,
  `"!!!"` → empty, `boiler blowdown` (unfiltered) → unchanged in character.
- Containers re-shipped; VPS gate `mygis 303, techlib-origin 403, tlea-origin 403`.

## 7. The bare-product-code limitation — closed the same day

Recorded in the first pass and fixed in `2026.11.23.2`:

| Before | After |
|---|---|
| `KS-1 solvent` → card 4th, behind solvent-deasphalting | `KS-1 solvent` → card **first** (0.0615) |
| `MDEA` → amine acid gas removal, but by a thin margin | `MDEA` → amine acid gas removal, first |
| A code the user saw on a vendor page needed the catalogue's own phrasing added | the code alone is enough |

Cause: `ts_rank_cd` has no document-frequency term, so the common word ("solvent", 693 records)
counted as much as the code ("KS-1", 13), and reciprocal-rank fusion let the common word's vector
neighbourhood outvote the keyword pool's #1.

Fix: a **third rank pool** for rare query concepts. `og.search_term` holds the document frequency of
every term (copied from the baked index on load — the same raw-token form the query is tokenised to;
`ts_stat` was tried first and rejected because it returns *stemmed* lexemes, so "amine" would look
unknown beside "amin"). A concept whose rarest term appears in ≤1% of records (floor 8) is a
qualifier, and records carrying it are fused in with their own rank. The cut-off is measured, not a
hand-written list: production frequencies put codes at 13–130 records and ordinary domain words at
419–3,964, so an unfamiliar code behaves the same way.

Cases verified live: `KS-1 solvent` → amine post-combustion; `MDEA` → amine acid gas removal;
`Benfield` → hot potassium carbonate; `cryogenic capture` → cryogenic capture. Regression checks:
`carbon capture amine` and `boiler blowdown` unchanged, and `solvent` alone still returns the solvent
cards (no rare concept, so no third pool).

Remaining honest note: the rare pool is a *bonus on top of* coverage and vector fusion, not a filter.
A query made only of codes that the library does not hold returns whatever the other pools find —
which is the correct answer to "we do not have this".

## 8. Where to read more

- Release notes: `CHANGELOG.md` → `[2026.11.23]`.
- Session record (root cause, measurements, digests): `docs/STATUS.md` log entry 2026-11-23.
- Ranking contract and query guidance: `docs/MCP.md` (`search`), `docs/POSTGRES.md`
  (`hybrid_search` / `hybrid_search_kind`).
- Commits: `7e0a67c` (coverage ranking, index text, per-kind pools), `4c47ec3` (kind filter inside
  the ranking; tokenless queries).
