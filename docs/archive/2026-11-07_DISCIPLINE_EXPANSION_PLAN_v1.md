# Discipline Expansion Plan — ELE, CIV, INS deepening

**Status: FIRST BATCH COMPLETE 2026-11-07** — all 27 planned cards written (12 ELE, 10 CIV, 5 INS), build valid, tests green (884 passed). Vendor-directory and equipment rounds follow per §3. (owner instruction: "add other disciplines too, like electrical
generation/distribution/protection, civil & structure including modular/IBS, control and
instrumentation, etc."). Extends decision #19's cross-cutting-discipline model with two new codes
and a deepening pass on the existing thin ones.

## 1. Model changes (done 2026-11-07)

- `taxonomy.yaml`: new discipline codes **ELE** (Electrical engineering) and **CIV** (Civil and
  structural) with subtopics; INS subtopics widened (field-instrumentation, fire-gas-detection,
  machinery-control, vibration-monitoring, control-valves).
- `schema/technology.schema.json`: sector enum gains ELE, CIV.
- `agent/graph.py`: discipline node kind set gains ELE, CIV.
- `agent/web.py`: `SECTOR_SELECT` gains ELE, CIV.

## 2. Card plan

One technology card per topic, same schema and evidence rules as every other card
(own words, every figure tied to a source actually read; ≤40% of cards may lack a catalogued
citation per decision #21 — target 0% for these).

### ELE — Electrical engineering (12 planned)

| # | Card id | Topic | Status |
|---|---|---|---|
| 1 | ele-gt-power-generation | On-site gas turbine power generation | **done 2026-11-07** |
| 2 | ele-hv-switchgear-distribution | HV/MV switchgear and site power distribution | **done 2026-11-07** |
| 3 | ele-protection-relaying | Power system protection and relaying | **done 2026-11-07** |
| 4 | ele-transformers | Power and distribution transformers | **done 2026-11-07** |
| 5 | ele-motors-drives | Motors and variable speed drives | **done 2026-11-07** |
| 6 | ele-emergency-up-power | Emergency, standby and UPS power systems | **done 2026-11-07** |
| 7 | ele-hazardous-area-electrical | Hazardous area electrical equipment (Ex) | **done 2026-11-07** |
| 8 | ele-heat-tracing | Electrical heat tracing | **done 2026-11-07** |
| 9 | ele-cable-systems | Power and control cable systems | **done 2026-11-07** |
| 10 | ele-power-management-systems | Power management and electrical SCADA | **done 2026-11-07** |
| 11 | ele-earthing-lightning | Earthing and lightning protection | **done 2026-11-07** |
| 12 | ele-subsea-umbilicals-power | Subsea power and umbilical systems | **done 2026-11-07** |

### CIV — Civil and structural (10 planned)

| # | Card id | Topic | Status |
|---|---|---|---|
| 1 | civ-structural-steel-design | Plant structural steel design | **done 2026-11-07** |
| 2 | civ-modular-construction-ibs | Modular construction and IBS (industrialised building systems, SEA/Malaysia angle) | **done 2026-11-07** |
| 3 | civ-pipe-racks-supports | Pipe racks, sleepers and pipe supports | **done 2026-11-07** |
| 4 | civ-foundations-piling | Foundations and piling | **done 2026-11-07** |
| 5 | civ-offshore-platform-structures | Fixed platform topsides and substructure (incl. concrete GBS) | **done 2026-11-07** |
| 6 | civ-floating-structures-fpso | FPSO and floating production structures | **done 2026-11-07** |
| 7 | civ-blast-resistant-buildings | Blast-resistant buildings | **done 2026-11-07** |
| 8 | civ-fireproofing-passive-protection | Structural fireproofing and passive fire protection | **done 2026-11-07** |
| 9 | civ-seismic-design | Seismic design of process facilities | **done 2026-11-07** |
| 10 | civ-heavy-lift-temporary-works | Heavy lift, transport and temporary works | **done 2026-11-07** |

### INS — deepening (5 planned)

| # | Card id | Topic | Status |
|---|---|---|---|
| 1 | ins-field-instrumentation | Field instrumentation (transmitters, level/flow/temperature) | **done 2026-11-07** |
| 2 | ins-fire-gas-detection | Fire and gas detection systems | **done 2026-11-07** |
| 3 | ins-machinery-control | Turbomachinery control systems | **done 2026-11-07** |
| 4 | ins-vibration-monitoring | Machinery vibration monitoring and CMS | **done 2026-11-07** |
| 5 | ins-custody-transfer-metering | Custody transfer metering | **done 2026-11-07** |

## 3. Follow-on (after cards)

- Vendor directory round for the new disciplines (switchgear, E-houses, modular fabricators,
  Malaysian/SEA EPC + IBS players) on the equipment-layer pattern.
- Equipment classes for the discipline layer (switchgear, transformers, e-houses) on the
  owner's word — equipment stays per decision #33's model.
- Source cataloguing: discipline sources found while authoring are registered in
  `catalog/sources/` (per decision #29's acquisition stance).

## 4. Rules

- Cards follow `schema/technology.schema.json`; validated by `tools/build.py`.
- Figures need `basis` + `source`; guessed specs are forbidden (decision #33 rule, applied here).
- Batch status table above is updated as cards land; this file is the tracking doc.

## 5. Batch record (2026-11-07)

- Sources registered: `selinc`, `hitachi-energy`, `iecex`, `hse-uk`.
- Register extended with ELE (12), CIV (10) and INS (5) entries; all cards link.
- Schema enums (technology sector, source disciplines), `agent/graph.py` discipline set, `agent/web.py` SECTOR_SELECT updated.
- `tools/build.py` valid: 404 sources, 326 cards, 421 vendors, 8 equipment; tests 884 passed.
