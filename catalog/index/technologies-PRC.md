# PRC technology options

5 technologies, from commercial to lab stage. Generated from catalog/technologies/; every figure links to its source.

| Technology | Category | Maturity | TRL | Suppliers | Cost figures |
| --- | --- | --- | --- | --- | --- |
| [Catalyst management (handling, regeneration, recycling)](#prc-catalyst-management) | Catalysis services | commercial |  | Eurecat (catalyst regeneration and reloading services); Topsoe (catalyst supply and life-cycle services); Johnson Matthey (catalyst supply and reclamation) |  |
| [Dynamic simulation and operator training simulators](#prc-dynamic-simulation-ots) | Process systems | commercial |  | AVEVA (Schneider Electric) (dynamic simulation and OTS (DYNSIM lineage)); Honeywell (UniSim dynamic simulation and OTS); AspenTech (Aspen Plus Dynamics / custom OTS) |  |
| [Pinch analysis and heat integration](#prc-pinch-analysis) | Process design and simulation | commercial |  | Pinchco (HeatIT (Excel-based)); Fives ProSim (Simulis Pinch (Excel)); CanmetENERGY (Integration); TLK-Energy (Pinch Analysis Tool (online)) |  |
| [Process intensification (rotating packed beds, dividing-wall columns, microreactors)](#prc-process-intensification) | Process design and simulation | commercial |  | Sulzer (dividing-wall columns and advanced column internals); Montz (structured packing and dividing-wall column internals) | capital cost reduction: 10-30 %<br>payback period: 1-3 years |
| [Steady-state and dynamic process simulation](#prc-process-simulation) | Process design and simulation | commercial |  | AspenTech (Aspen HYSYS and Aspen Plus steady-state and dynamic simulation); Honeywell (UniSim Design process simulation); Siemens (PSE) (gPROMS high-fidelity process modelling); AVEVA (AVEVA PRO/II process simulation) |  |

## Catalyst management (handling, regeneration, recycling)
<a id="prc-catalyst-management"></a>

Catalyst is a consumable with a managed life: fresh catalyst is loaded under inert atmosphere with density and distribution control; activity declines through coking, poisoning and sintering and is watched via bed pressure drop and product quality; spent catalyst is unloaded (often under inert, sometimes offline via skimming), then either regenerated in-situ or sent to a specialist reclaimer that recovers metals and reconditions the carrier. Life-cycle contracts bundle supply, loading, surveillance and disposal so the refiner pays for active-days rather than tonnes.

```mermaid
flowchart LR
    LOD["Fresh catalyst loaded with inert-atmosphere handling and loading-density control<br/><small>dense-loading equipment, inert entry systems</small>"]
    RUN["Activity tracked through temperature profiles, pressure drop and product quality<br/><small>bed instrumentation</small>"]
    REG["Regenerated in-situ (controlled burn) or sent for ex-situ regeneration<br/><small>regeneration facilities</small>"]
    REC["Spent catalyst reclaimed: metals recovered, carrier reconditioned or disposed<br/><small>reclamation plants</small>"]
    LOD --> RUN
    RUN --> REG
    REG --> REC
```

**Key equipment:** dense-loading services, inert-entry crews, regeneration furnaces, metal reclamation plants.

Sources: [1](https://www.eurecat.com/), [2](https://www.hydrocarbon-engineering.com/). Last reviewed 2026-11-08.

## Dynamic simulation and operator training simulators
<a id="prc-dynamic-simulation-ots"></a>

Dynamic simulation solves the plant's mass, energy and momentum balances over time rather than at steady state, reproducing transient behaviour: relief events, compressor surging, furnace trip response, control-loop interaction. The same high-fidelity model, connected to a replica of the plant DCS graphics, becomes an operator training simulator that lets crews rehearse startups, shutdowns and emergencies offline before touching the real unit.

```mermaid
flowchart LR
    MOD["Steady-state or first-principles model built from P&IDs and heat/material balance<br/><small>model development environment</small>"]
    DYN["Model made dynamic: holds, lags, controller actions, equipment limits<br/><small>dynamic solver</small>"]
    TUN["Tuned against plant history so transients reproduce observed behaviour<br/><small>plant historian data</small>"]
    OTS["Connected to a DCS-replica operator station for training scenarios<br/><small>OTS instructor station</small>"]
    USE["Used for control checkout, procedure trials and operator certification<br/><small>scenario library</small>"]
    MOD --> DYN
    DYN --> TUN
    TUN --> OTS
    OTS --> USE
```

**Key equipment:** solver, instructor station, DCS-replica operator stations, scenario libraries.

Sources: [1](https://process.honeywell.com/), [2](https://www.aspen.com/). Last reviewed 2026-11-08.

## Pinch analysis and heat integration
<a id="prc-pinch-analysis"></a>

Hot and cold process streams are plotted as heat load against temperature and combined into composite curves; the point of closest approach is the pinch. Targets for minimum hot and cold utility follow, and exchangers are placed above and below the pinch separately.

```mermaid
flowchart LR
    STREAMS["Extract hot and cold streams with heat load and temperatures<br/><small>data extraction</small>"]
    CURVES["Build hot and cold composite curves<br/><small>composite curves</small>"]
    PINCH["Locate the pinch at the chosen minimum temperature difference<br/><small>problem table</small>"]
    TARGET["Set minimum utility and area targets"]
    NETWORK["Design heat exchanger network above and below the pinch<br/><small>heat exchangers</small>"]
    STREAMS --> CURVES
    CURVES --> PINCH
    PINCH --> TARGET
    TARGET --> NETWORK
```

**Key equipment:** heat exchanger network, pinch software.

**Missing inputs:**
- typical energy savings reported by pinch studies (performance): The page read gives no savings figures. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: IEA, DOE industrial assessment centre and CanmetENERGY case studies (open). Next: Add savings with plant type and year from a case study.
- capital cost and operating or unit cost, with dollar year and basis (costs): No open source read so far gives costs for this technology. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: arXiv and open-access journals: techno-economic or review papers (MDPI is blocked by its CDN; use the manual inbox) (catalog: arxiv, open); Licensor and EPC studies; paid cost databases are catalog-only (paid); OSTI.GOV full-text reports from DOE labs: search the technology name plus 'techno-economic' (catalog: osti, blocked). Next: Look for an open techno-economic study; record each figure with metric, range, unit, dollar year, basis and source.
- named plants or projects with capacity and year (reference_plants): The sources read name no specific plant. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: Licensor and operator press releases for the suppliers listed (open). Next: Add one or two plants with country, capacity and start-up year.
- TRL with a cited source (trl): The IEA ETP Clean Energy Technology Guide has no matching entry. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: IEA ETP Clean Energy Technology Guide (collected): search for the technology name (catalog: iea-reports, open). Next: Find a TRL table that lists this technology, or leave maturity resting on the evidence on the card.

Sources: [1](https://en.wikipedia.org/wiki/Pinch_analysis). Last reviewed 2026-10-29.

## Process intensification (rotating packed beds, dividing-wall columns, microreactors)
<a id="prc-process-intensification"></a>

Intensification combines functions into compact multifunctional devices rather than tuning single unit operations. Examples include reactive distillation, membrane reactors, microreactors and dividing-wall columns.

```mermaid
flowchart LR
    BASE["Map unit operations and find functions that can be combined<br/><small>flowsheet review</small>"]
    PICK["Choose a device: reactive distillation, membrane reactor, microreactor or dividing-wall column<br/><small>intensified equipment</small>"]
    PILOT["Pilot and phase the change in, starting with lower-risk options<br/><small>pilot unit</small>"]
    RUN["Operate and compare energy and capital against the base case"]
    BASE --> PICK
    PICK --> PILOT
    PILOT --> RUN
```

**Key equipment:** reactive distillation column, membrane reactor, microreactor, dividing-wall column, rotating packed bed.

**Performance:**
- energy savings from intensification: 20-60 %; range stated by the Chemical Processing article; no baseline process given. [source](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources)
- microreactor channel size: 10-500 um; channel dimension quoted in the article. [source](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources)

**Costs:**
- capital cost reduction: 10-30 %; range stated in the article; no dollar amounts or year given. [source](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources)
- payback period: 1-3 years; range stated in the article; dollar year not stated. [source](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources)

**Reference plants:**
- Methyl acetate reactive distillation column replacing an eleven-step process: ; described, operator not named. [source](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources)

**Missing inputs:**
- dividing-wall column and rotating packed bed figures (performance): The Wikipedia pages for these were not found and the article gives no detail. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: Dividing-wall column studies in Chemical Engineering Progress (AIChE) (open); arXiv and open-access journals: techno-economic or review papers (MDPI is blocked by its CDN; use the manual inbox) (catalog: arxiv, open). Next: Add energy and capex figures for each device with source.
- TRL with a cited source (trl): The IEA ETP Clean Energy Technology Guide has no matching entry. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: IEA ETP Clean Energy Technology Guide (collected): search for the technology name (catalog: iea-reports, open). Next: Find a TRL table that lists this technology, or leave maturity resting on the evidence on the card.
- process steps and equipment are general engineering practice, not taken from one source (process): The sources read describe the principle but not a full step-by-step flow. Where: Licensor process descriptions and textbooks (open). Next: Check the steps against a licensor description and name it.

Sources: [1](https://www.chemicalprocessing.com/voices/energy-saver/article/55303778/energy-saver-process-intensification-maximizes-output-minimizes-resources). Last reviewed 2026-10-28.

## Steady-state and dynamic process simulation
<a id="prc-process-simulation"></a>

Software represents a plant as unit operations joined by streams and solves the mass and energy balances to find a stable operating point. Steady-state models ignore time; dynamic models add accumulation terms and so can be used for operator training, control design and troubleshooting.

```mermaid
flowchart LR
    DEF["Define feed stream: composition, flow, pressure, temperature<br/><small>property package</small>"]
    VLE["Choose property models or vapour-liquid equilibrium data<br/><small>thermodynamic model</small>"]
    UNIT["Specify unit operations and connect streams<br/><small>flowsheet</small>"]
    SOLVE["Solve mass and energy balances<br/><small>solver</small>"]
    RESULT["Read product stream properties, duties and costs<br/><small>reports</small>"]
    DEF --> VLE
    VLE --> UNIT
    UNIT --> SOLVE
    SOLVE --> RESULT
```

**Key equipment:** flowsheet simulator, thermodynamic property package, dynamic simulation engine, operator training simulator.

**Missing inputs:**
- key performance figures (energy use, yields, capture or conversion rate) (performance): No source read so far gives performance figures. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: Supplier datasheets and brochures for the companies listed on the card (open); arXiv and open-access journals: techno-economic or review papers (MDPI is blocked by its CDN; use the manual inbox) (catalog: arxiv, open); OSTI.GOV full-text reports from DOE labs: search the technology name plus 'techno-economic' (catalog: osti, blocked). Next: Add the figures that matter for comparing options, each with its basis and source.
- capital cost and operating or unit cost, with dollar year and basis (costs): No open source read so far gives costs for this technology. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: arXiv and open-access journals: techno-economic or review papers (MDPI is blocked by its CDN; use the manual inbox) (catalog: arxiv, open); Licensor and EPC studies; paid cost databases are catalog-only (paid); OSTI.GOV full-text reports from DOE labs: search the technology name plus 'techno-economic' (catalog: osti, blocked). Next: Look for an open techno-economic study; record each figure with metric, range, unit, dollar year, basis and source.
- named plants or projects with capacity and year (reference_plants): The sources read name no specific plant. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: Licensor and operator press releases for the suppliers listed (open). Next: Add one or two plants with country, capacity and start-up year.
- TRL with a cited source (trl): The IEA ETP Clean Energy Technology Guide has no matching entry. Web-checked 2026-10-28: suppliers recorded where applicable; remaining figures sit in vendor-selector, licensor or paywalled-standards material and were not verifiable open. Where: IEA ETP Clean Energy Technology Guide (collected): search for the technology name (catalog: iea-reports, open). Next: Find a TRL table that lists this technology, or leave maturity resting on the evidence on the card.

Sources: [1](https://en.wikipedia.org/wiki/Process_simulation). Last reviewed 2026-10-29.
