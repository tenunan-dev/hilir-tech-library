# Equipment catalog

28 equipment records (one per equipment class, schema `schema/equipment.schema.json`).
Each record carries specification ranges with their sources and the directory vendors that
supply the class. Start of the equipment layer per the owner: boiler first, next families
follow the registration queue.

## aeration

### Aeration systems (blowers and diffusers) (wwt-aeration-systems)

Primary code: WWT: Wastewater and water reuse
The energy centre of biological treatment: blowers (turbo, screw, lobe) and fine-bubble diffuser grids or mechanical aerators deliver oxygen to activated-sludge and MBBR basins.
Vendors: Xylem (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fine-bubble diffuser oxygen transfer efficiency | 2-4 %/m | published SOTE per metre of submergence |
| turbo blower sizes | 30-500 kW | typical single-unit range |

- **Xylem** Sanitaire: basin aeration systems

Recorded gaps:

- per-model blower efficiency tables — Read Sanitaire/GE turbo blower datasheets

## anaerobic-digesters

### Anaerobic digesters (sludge and organics) (wwt-anaerobic-digesters)

Primary code: WWT: Wastewater and water reuse
Complete-mix mesophilic/thermophilic digesters with heating, gas mixing and biogas handling; optionally preceded by thermal hydrolysis.
Vendors: Veolia, Cambi AS, Xergi A/S (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| volatile solids destruction | 40-55 % | published mesophilic range |
| biogas yield | 700-1100 m3/t VS destroyed | published sludge yields |

- **Cambi AS** THP: pre-THP boosts VS destruction and dewaterability

Recorded gaps:

- per-project digester sizes — Collect digester sizes from reference projects

## biogas-upgrading

### Biogas upgrading units (wwt-biogas-upgraders)

Primary code: WWT: Wastewater and water reuse
Water-wash, amine, membrane and PSA units upgrading raw biogas to 95-99% methane grid/vehicle spec.
Vendors: DMT Environmental Technology, Pentair (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product methane | 95-99 % CH4 | published grid/vehicle spec |
| methane recovery | 98-99.5 % | published upgrading recovery |

- **DMT Environmental Technology** DMT upgrading: 95-99% CH4 product

Recorded gaps:

- per-model Nm3/h ranges — Read DMT/Pentair model pages

## boiler

### Circulating fluidized-bed boiler (CFB) (boiler-circulating-fluidized-bed)

Primary code: PWR: Power and renewables
Solid-fuel boiler that burns particles in a circulating fluidized bed, recirculating the bed material through a cyclone so even difficult fuels — high-sulfur, high-ash, waste, biomass and refinery solids — burn cleanly at low furnace temperature with limestone capturing SOx in the furnace. Fluidized-bed steam generation for power and industrial steam where fuel flexibility and in-furnace desulfurization matter.
Vendors: Sumitomo SHI FW, Babcock & Wilcox (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| size range of delivered CFB plants | 0-36 GWe | Sumitomo SHI FW has delivered more than 500 CFB boilers totalling 36 GWe in power capacity |
| steam conditions, largest designs | ultra-supercritical steam at 257 bar and 603 C is available for large-scale p... | ultra-supercritical steam at 257 bar and 603 C is available for large-scale plants |
| SOx and NOx without flue-gas cleaning system | 50 ppm @ 6% O2 | less than 50 ppm SOx and NOx at 6% O2 with in-furnace limestone capture; NOx avoided by low-temperature combustion |
| particulate matter with ESP | 20 mg/m3 @ 6% O2 | below 20 mg/m3 with an electrostatic precipitator |
| boiler availability, fleet average | 98 % | average 98% boiler availability across the fleet (vendor statement) |
| biomass share in co-firing | 0-100 % | the multi-fuel CFB can co-fire a wide range of fuels, with up to 100% biomass or RDF streams |

- **Sumitomo SHI FW** CFB boilers: 500+ delivered, including in-house industrial steam generation through thermal power stations; own pressure-part workshops and a fuel test center at the Niihama Works
- **Babcock & Wilcox** IR-CFB (internal recirculation): one- or two-drum top-supported design for high-sulfur, high-ash and waste fuels with subcritical and supercritical applications

### Electric and electrode steam boiler (boiler-electric-electrode)

Primary code: PWR: Power and renewables
Steam generator heated directly by electricity — resistance elements in a pressure vessel, or current conducted through the boiler water by electrodes at high voltage. No combustion, no flue gas and no fuel system, so it avoids the chimney, fuel infrastructure and air-permit scope entirely, and pairs with cheap or surplus site power; the electrification option for on-site steam.
Vendors: Bosch Industriekessel, Cleaver-Brooks (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam output, packaged resistance-type | 350-8300 kg/h | Bosch ELSB: 350 to 8,300 kg/h (up to 8.3 t/h per appliance) |
| safety pressure, resistance-type | 0-24 bar | Bosch ELSB up to 24 bar, max temperature 224 C |
| conversion efficiency, resistance-type | 99-? % | over 99% efficiency level, surpassing combustion systems (Bosch); Cleaver-Brooks states electric boilers are nearly 100% efficient |
| supply voltage | Bosch ELSB supply 380/400/690 V | Bosch ELSB supply 380/400/690 V |
| Cleaver-Brooks Model S range | 12 to 2,250 kW, up to 7,875 lb per h, up to 600 V, 15/150/200/250 psig, no si... | 12 to 2,250 kW, up to 7,875 lb per h, up to 600 V, 15/150/200/250 psig, no site emissions, nearly 100% efficient |

- **Bosch Industriekessel** ELSB electric steam boiler: 350-8,300 kg/h, up to 24 bar, up to 224 C, supply 380/400/690 V, thyristor-modulated output across the load range
- **Cleaver-Brooks** Model S electric boiler: 12-2,250 kW, up to 7,875 lb/h, 15/150/200/250 psig

Recorded gaps:

- electrode boiler capacity ceiling at high voltage (MW-class hot-water and steam units) — read an OEM electrode boiler page (e.g. Precision Boilers) for the utility-class range

### Heat recovery steam generator (HRSG) (boiler-hrsg)

Primary code: PWR: Power and renewables
Boiler fired by hot combustion-turbine or furnace exhaust gas rather than by burners, raised in horizontal or vertical panels behind a gas turbine with one or more drum pressures and optionally reheat. Converts a gas turbine into a combined-cycle or cogeneration plant and is the deciding component for how much of the turbine exhaust energy becomes steam.
Vendors: Babcock & Wilcox, Cleaver-Brooks, Doosan Enerbility, IHI Corporation, Sumitomo SHI FW (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam-cycle efficiency by HRSG configuration | 20-30 % | about 20% for two-pressure without reheat, 26% for three-pressure, about 30% for three-pressure with reheat |

- **Babcock & Wilcox** HRSG systems, upgrades and components: reliable HRSG systems plus upgrades and replacement components — HARPs (high pressure evaporators), headers, finned tubing and other pressure parts — suitable for a wide range of combustion turbine applications
- **Cleaver-Brooks** packaged HRSG for small turbines: state-of-the-art customized packaged heat-recovery steam generators for gas-fired turbines from 1 to 60 MW

Recorded gaps:

- OEM HRSG specification ranges (steam pressures, temperatures, supplemental firing) for major suppliers — read Mitsubishi Power and B&W HRSG detail pages in the next equipment sweep

### Industrial water-tube package boiler (boiler-industrial-watertube-package)

Primary code: PWR: Power and renewables
Shop-assembled watertube boiler (steam and lower drum above a water-cooled membrane furnace) custom-engineered per project, with D-type and O-type two-drum layouts. The standard steam generator above the fire-tube class for refineries, petrochemical plants and industrial power, firing liquid or gaseous fuels including refinery byproduct gases.
Vendors: Babcock & Wilcox, John Zink Company (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam capacity range | 10000-1200000 lb/h | 4.5 to 544.2 T/h depending on type and design features |
| design pressure range | 250-2400 psig | 1.7 to 16.5 MPa |
| steam temperature | 0-1005 F | saturated to 1005 F (540 C) superheat |
| installed base | 5000-? units | more than 5,000 units and 150 years of experience (B&W industrial water-tube package and industrial boilers) |
| FM-series capacity range | 8200-275000 lb/h | FM 9 odd-number frames 8,200-40,000; FM 10-52/57/61/66/70/79 and FM 101-88 35,000-75,000; FM 103 70,000-100,000; FM 106/FM 117 100,000-155,000; FM 120/FM 160 155,000-275,000 (saturated steam) |
| HCFM / PFM / TSSG capacity, pressure, temperature limits | HCFM 200,000-350,000 lb/h to 1,250 psig (7.2 MPa) to 825 F (441 C); PFM 200,0... | HCFM 200,000-350,000 lb/h to 1,250 psig (7.2 MPa) to 825 F (441 C); PFM 200,000-600,000 lb/h to 1,800 psig (12.4 MPa) to 900 F (482 C); TSSG 300,000-1,200,000 lb/h to 2,400 psig (16.5 MPa) to 1006 F (540 C) |
| tube specification | 2.5-1.0 in | larger tube diameter 2.5 in spaced 1 in apart contributes to faster load response (design feature) |

- **Babcock & Wilcox** FM water-tube package: 8,200 to 1,200,000 lb/h across the series; D-type or O-type, single-drum or multi-drum; membrane-wall construction, fully drainable superheaters
- **John Zink Company** Coen burners paired with B&W packages: B&W packages boilers with JZHC Coen burners under an agreement between the two companies; Coen burners installed in more than 15,000 plants

Recorded gaps:

- efficiency and emission figures for the FM/HCFM/PFM/TSSG lines — read the FM brochure PDF (linked 'Download the Brochure') in a later sweep

### Packaged fire-tube steam boiler (boiler-fire-tube-package)

Primary code: PWR: Power and renewables
Shop-assembled shell boiler in which hot combustion gases pass through tubes surrounded by the water, typically in two to four passes with a reverse-flue turnaround. The standard packaged steam source for small and medium industrial loads and the workhorse of on-site utilities where steam demand runs from tens of thousands of pounds per hour downward.
Vendors: Cleaver-Brooks, Miura Boiler (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| capacity of current manufacturer lines | 50-800 BHP | Cleaver-Brooks CBLE 50 to 800 HP; Miura EX 100 to 300 BHP |
| steam output | 3450-10350 lb/h | Miura EX tables: 100 BHP = 3,450 lb/h, 150 BHP = 5,175 lb/h, 200 BHP = 6,900 lb/h, 250 BHP = 8,625 lb/h, 300 BHP = 10,350 lb/h (equivalent output from and at 212 F) |
| maximum allowable working pressure, steam | 170-300 psig | Miura EX standard 170 psig, optional 250/225 psig (EXH-SGO), high-pressure 300 psig MAWP models; Cleaver-Brooks CBLE steam up to 300 psig |
| fuel-to-steam efficiency (HHV) | 84-85 % | Miura EX standard-pressure and low-NOx-FGR tables 85%, high-pressure tables 84%, based on higher heating values of fuels at 68 F feed water |
| NOx emissions, cleanest configurations offered | 5 ppm | Cleaver-Brooks CBLE offers 60, 30, 9 and 5 ppm NOx rating options (natural gas firing); Miura EX as low as 30 ppm depending on model |
| cold start to full steam | 5 min | Miura EX: single-button cold start to full steam output in under 5 minutes |
| footprint vs conventional fire-tube | 33 % | Miura EX occupies 33% less floor space than typical fire-tube boilers (vendor statement) |

- **Cleaver-Brooks** CBLE fire-tube: 50-800 HP, steam to 300 psig, hot water to 125 psig, 4-pass, dryback or waterback; fuels natural gas/propane, #2 and #6 oil, combination
- **Cleaver-Brooks** CBEX Elite: 1,300-2,200 boiler horsepower sizes per Cleaver-Brooks O&M guide (specs not independently verified)
- **Miura Boiler** EX gas/oil dual-fuel: 100-300 BHP, 170/250/300 psig MAWP, 84-85% efficiency HHV, NOx to 30 ppm with FGR burner models, BL controller with scale monitor

Recorded gaps:

- turndown ratios and part-load efficiency curves for the main fire-tube lines — read Cleaver-Brooks and Miura turndown data during the next boiler sweep
- refinery large-firetube practice and which classes refineries specify below what load — look for refinery utility steam design references in corpus/

## busway

### Data centre busway (overhead busbar power distribution) (busway-data-centre)

Primary code: IDC: Data centres
Overhead extruded-aluminium busbar runs that carry power across a data hall and let plug-in tap-off units be added or moved at any point without shutting the run down — the reason busway has displaced cable trays for in-hall distribution. Starline's ranges illustrate the class: Track Busway 40-1250 A, Series-S 100-1200 A (IP54) and high-power enclosed busway 630-6000 A (to IP65), with plug-in units carrying integrated circuit protection and a metering family for branch-level monitoring.
Vendors: Vertiv, Schneider Electric, Eaton, Anord Mardix (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Track Busway amperage range | 40-1250 A | Starline Track Busway 40-1250 A; plug-in units connect at any location at any time without shutting down the busway |
| high-power enclosed busway amperage range | 630-6000 A | 630-6000 A per product listings, up to 6300 A in the higher-amperage section; ingress protection to IP65 |
| Series-S Track Busway rating | 100-1200 A | 100-1200 A, IP54 rated for harsh environments, UL857 listed |

- **Vertiv** Starline Track Busway (Vertiv brand): 40-6000 A across families; IP54/IP65 options

Recorded gaps:

- energy-loss comparison versus cable-based distribution — Find an engineering comparison study and record losses per 100 m
- Schneider/Eaton/Anord Mardix busway model lines — Read each vendor's busway range and add model lines

## clarifiers-thickeners

### Clarifiers and thickeners (wwt-clarifiers-thickeners)

Primary code: WWT: Wastewater and water reuse
Primary/secondary circular clarifiers and gravity/DAF thickeners with scraper bridges, plus lamella packs for high-rate duty.
Vendors: Veolia, WesTech Engineering (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| lamella effective area gain | 8-10 x | versus tank footprint |

- **Veolia** Actiflo/high-rate: 60-120 m/h loading

Recorded gaps:

- per-model tank sizes — Read WesTech/Veolia clarifier model pages

## compressor

### Centrifugal compressor (compressor-centrifugal)

Primary code: ROT: Rotating and static equipment
Dynamic compressor that raises gas pressure across one or more impeller stages — the standard machine for refinery and petrochemical process gas, pipeline boost, gas-lift and reinjection, and CO2 service, driven by gas turbines or electric motors through gears. Casing arrangements (overhung, integrally-geared, horizontally- or vertically-split/barrel) set the pressure class; barrel-style machines serve the highest-pressure gas reinjection duties.
Vendors: Siemens Energy, Baker Hughes, Atlas Copco, Mitsubishi Power (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| single-stage pressure ratio | 1-10 ratio | single-stage machines; ratios of about 8 are a helicopter-engine example and few centrifugal stages exceed 10:1 — process duty sits well below the top of this range |
| oilfield gas reinjection discharge pressure | 700 bar | approaching 700 bar with barrel-style casings, as stated |


Recorded gaps:

- per-vendor model-line ranges (flow, stage count, discharge pressure) for Siemens Energy STC, Baker Hughes BCL/DBL and PCL, MCO-I and Atlas Copco integrally-geared machines — fetch the OEM compressor family pages (browser session if needed) and add model lines with stated ranges
- CO2-specific compression train boundaries (inlet, discharge, density effects) — mine the ccs-co2-compression-dehydration card's sources and OEM CO2 compression references

## crah

### Data centre CRAH/CRAC room cooling (air side) (crah-room-cooling)

Primary code: IDC: Data centres
Per-hall air handlers that close the loop between the cold aisle and the heat-rejection plant: computer-room air handlers (CRAH, chilled water) and air conditioners (CRAC, direct expansion), now joined by water-free pumped-refrigerant economisers. The Vertiv Liebert DSE spans 50-165 kW per unit (packaged systems to about 400 kW) and provides free cooling with no water — a chilled-water plant serving 1 MW of IT load uses roughly 4 million gallons of water a year that the DSE avoids.
Vendors: Vertiv, Schneider Electric, Rittal (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| unit capacity range, Vertiv Liebert DSE free-cooling system | 50-165 kW | 50-165 kW standard range per unit; larger packaged configurations at about 250 kW and 400 kW |
| annual water use avoided versus chilled water at 1 MW IT load | 4000000 gallons/year | a chilled-water system for a 1 MW data centre uses about 4 million gallons of water annually, which the water-free DSE avoids |

- **Vertiv** Liebert DSE (pumped refrigerant economiser): 50-165 kW per unit, packaged systems to about 400 kW, water-free

Recorded gaps:

- containment-integrated efficiency figures (kW per kW of heat) — Read the DSE and Liebert CW/PCW datasheets for efficiency data
- Stulz and Schneider (Uniflair) model lines — Read both vendor ranges and add model lines

## daf-units

### Dissolved air flotation units (wwt-daf-units)

Primary code: WWT: Wastewater and water reuse
DAF clarifiers: air-saturation vessels release 30-100 um microbubbles into coagulated water; floated flocs are scraped off as a thick float sludge.
Vendors: Veolia, Evoqua Water Technologies (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| microbubble size | 30-100 um | published DAF design range |
| hydraulic loading | 5-15 m/h | typical design HLR |

- **Veolia** F flotation family: 5-15 m/h loading

Recorded gaps:

- per-model flow ranges — Read Veolia/Evoqua DAF model pages

## evaporator-crystallisers

### ZLD evaporators and crystallisers (wwt-evaporator-crystallisers)

Primary code: WWT: Wastewater and water reuse
Mechanical-vapour-recompression evaporators and forced-circulation crystallisers that end ZLD trains: distillate recycled, salts recovered as solids.
Vendors: Aquatech International, Veolia (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| distillate TDS | 1-10 mg/L | Aquatech published ZLD performance |
| brine concentration reached | 200000-280000 mg/L TDS | Aquatech published ZLD performance |

- **Aquatech International** Aquatech ZLD: full ZLD trains

Recorded gaps:

- per-model m3/d ranges — Read Aquatech/Veolia HPD model pages

## hv-circuit-breakers

### High-voltage circuit breakers (132-500 kV) (ele-hv-circuit-breakers)

Primary code: ELE: Electrical engineering
SF6 and vacuum circuit breakers at 132, 275 and 500 kV for grid and substation duty, with their interrupting ratings set by the Malaysian fault levels, to IEC 62271-100.
Vendors: Hitachi Energy, Siemens Energy, GE Vernova (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| interrupting rating at 500 kV | 50-63 kA | TNB 500 kV fault rating 50 kA at 1 s; breakers specified at or above it |
| interrupting rating at 275 kV | 40-50 kA | TNB 275 kV fault rating 40 kA at 3 s, 50 kA near power stations |
| interrupting rating at 132 kV | 31.5-40 kA | TNB 132 kV fault rating 31.5 kA at 3 s, 40 kA near power stations |

- **Hitachi Energy** Live tank / dead tank: 72.5-800 kV
- **Siemens Energy** 3AP / 3AT: 72.5-550 kV
- **GE Vernova** Dead tank breakers: 72.5-800 kV

Recorded gaps:

- SF6 leakage and operating-time figures — Read breaker datasheets and record leak rate and operating times

## lv-switchboards

### LV switchboards and distribution boards (ele-lv-switchboard)

Primary code: ELE: Electrical engineering
Form 1-4 rated low-voltage assemblies at 415/240 V: main switchboards with air circuit breakers, motor control centres and final distribution boards, built to IEC 61439.
Vendors: ABB, Schneider Electric, Siemens, Eaton (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| rated busbar current | 630-6300 A | typical LV switchboard busbar ratings for Malaysian industrial premises |
| rated operational voltage | 400-690 V | IEC 61439 LV assemblies cover 400-690 V; Malaysian LV supply is 400/415 V |
| short-circuit withstand | 25-100 kA | manufacturer catalogues for main switchboards; site value set by the LV fault level |

- **ABB** MNS: up to 6300 A
- **Schneider Electric** PrismaSeT / Blokset: 630-6300 A
- **Siemens** SIVACON S8: up to 7000 A
- **Eaton** xEnergy: up to 6300 A

Recorded gaps:

- per-form price tables — Ask a Malaysian panel builder for a quote benchmark

## membrane-systems

### MF/UF/RO membrane systems (wwt-membrane-systems)

Primary code: WWT: Wastewater and water reuse
Pressure-driven membrane systems for water reuse: hollow-fibre microfiltration/ultrafiltration (0.02-0.1 um) pretreatment and spiral-wound reverse osmosis trains that reject salts and micropollutants.
Vendors: SUEZ Water Technologies, DuPont Water Solutions, Toray Industries, Nitto / Hydranautics (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| UF pore size | 0.02-0.1 um | hollow-fibre MF/UF ratings |
| RO element sizes | 8-16 inch | standard 8-inch and large 16-inch elements |
| RO permeate recovery (reuse trains) | 75-85 % | typical municipal reuse design recovery |

- **SUEZ Water Technologies** ZeeWeed 500D/1000: submerged and pressurised UF modules
- **DuPont Water Solutions** FilmTec / IntegraFlux: brackish and low-energy RO elements
- **Toray Industries** ROMEMBRA / submerged flat sheet: RO and MBR modules

Recorded gaps:

- per-model flux and pressure tables — Read FilmTec and ZeeWeed datasheets and record per-model figures

## mv-switchgear

### MV switchgear and ring main units (11-33 kV) (ele-mv-switchgear)

Primary code: ELE: Electrical engineering
11 kV and 33 kV metal-clad or gas-insulated switchgear and compact ring main units used at TNB intake points and site substations, built to IEC 62271.
Vendors: ABB, Schneider Electric, Siemens, Eaton (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| rated voltage | 11-33 kV | TNB MV distribution levels at 11 kV and 33 kV |
| short-circuit rating at 11 kV | 20-25 kA | TNB 11 kV fault rating is 20 kA for 3 s; switchgear normally rated 20-25 kA |
| short-circuit rating at 33 kV | 25-31.5 kA | TNB 33 kV fault rating is 25 kA for 3 s; switchgear rated 25-31.5 kA |
| busbar current, typical RMU | 630-1250 A | typical RMU busbar rating |

- **ABB** SafeRing / SafePlus: 11-36 kV RMU
- **Schneider Electric** RM6 / Premset: 11-36 kV
- **Siemens** 8DJH: 11-36 kV
- **Eaton** Xiria: 12-24 kV

Recorded gaps:

- per-panel price tables — Ask a Malaysian switchgear panel builder for a quote benchmark

## ozone-generators

### Ozone generators (wwt-ozone-generators)

Primary code: WWT: Wastewater and water reuse
Corona-discharge ozone generation on oxygen feed with side-stream injection for micropollutant control and disinfection.
Vendors: Xylem (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ozone dose applied | 0.5-3 mg/L | published micropollutant dosing |

- **Xylem** Wedeco: oxygen-fed corona discharge

Recorded gaps:

- per-model kg-O3/h ranges — Read Wedeco generator model pages

## power-cables

### Power cables (LV to 500 kV) (ele-power-cables)

Primary code: ELE: Electrical engineering
XLPE-insulated power cables from 415 V building wiring through 11/33 kV distribution to 132 kV and 275 kV transmission cables, to IEC 60502 and IEC 60840/62067.
Vendors: Prysmian Group, Nexans (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| voltage grades covering the Malaysian system | 0.6-275 kV | 0.6/1 kV LV through 11-33 kV MV to 132-275 kV transmission cable grades |
| conductor material | 1 type | copper for LV and aluminium for HV conductors |

- **Prysmian Group** XLPE cables: 0.6 kV to 400 kV
- **Nexans** Power cables: LV to EHV

Recorded gaps:

- ampacity tables by installation method — Read IEC 60287/60364 ampacity tables

## power-transformers

### Power and distribution transformers (ele-power-transformers)

Primary code: ELE: Electrical engineering
Oil-immersed and dry-type transformers stepping between the Malaysian voltage tiers: 500/275 kV and 275/132 kV grid banks, 132/33/11 kV distribution units and 11-33 kV/415 V site transformers, to IEC 60076.
Vendors: Hitachi Energy, Siemens Energy, GE Vernova (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ratio tiers used in Malaysia | 0.415-500 kV | Malaysian tiers 500, 275, 132, 33, 11 kV and 415 V are joined by transformers |
| distribution transformer rating | 500-2500 kVA | typical 11-33 kV / 415 V distribution sizes |
| power transformer rating | 100-700 MVA | grid bank sizes at 275 and 500 kV |

- **Hitachi Energy** Power and distribution transformers: power and distribution
- **Siemens Energy** Transformers: distribution to UHV
- **GE Vernova** Transformers: distribution to UHV

Recorded gaps:

- loss tables (no-load and load) by rating — Read Hitachi/Siemens transformer datasheets and record loss figures

## protection-relays

### Protection relays and substation IEDs (ele-protection-relays)

Primary code: ELE: Electrical engineering
Numerical protection relays and IEC 61850 intelligent electronic devices for overcurrent, distance, differential and transformer protection on the Malaysian grid and industrial systems, to IEC 60255.
Vendors: Hitachi Energy, Siemens Energy, GE Vernova (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fault clearance basis at 500 kV | 50 kA | protection must clear the 50 kA, 1 s duty |
| communication protocol | 61850 standard | IEC 61850 substation automation is the standard for new installations |

- **Hitachi Energy** REL / RED: transmission protection
- **Siemens Energy** SIPROTEC: transmission and transformer
- **GE Vernova** UR (Universal Relay): transmission protection

Recorded gaps:

- operating times and setting ranges per model — Read manufacturer tech manuals for operating times

## pump

### Centrifugal pump (API 610 and general service) (pump-centrifugal)

Primary code: ROT: Rotating and static equipment
Rotodynamic pump that adds velocity to the liquid with an impeller and converts it to pressure in a volute or diffuser — the default mover for refinery, petrochemical, power and upstream water duties. API 610 (with ISO 13709) is the refinery-class standard and organises machines into overhung (OH), between-bearing (BB) and vertically-suspended (VS) arrangements; the specific family sets how much flow, head and suction pressure the machine takes.
Vendors: Sulzer, Flowserve, KSB (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| boiler feed pump flow per pump (350 MW unit, two in parallel) | 150 L/s | example given in the article: two pumps in parallel for a 350 MW unit at 21 MPa |
| boiler feed pump discharge pressure (350 MW unit) | 21 MPa | example given in the article for a 350 MW unit's feed system |

- **Sulzer** API 610 and ISO 13709 pump families: end-suction and overhung, between-bearing (axially- and radially-split, one/two and multi-stage) and vertically-suspended families; per-model flow and head ranges sit on the family pages

Recorded gaps:

- per-model flow, head and pressure ranges for the API 610 families (Sulzer ZE/ZP/ZPP, Flowserve Mark III/OH2/BB5, KSB) — fetch the Sulzer ZE/ZPP and Flowserve OH2/BB5 family pages (browser session if needed) and add per-model ranges
- energy-footprint and efficiency benchmark for process pumps — Hydraulic Institute (pumps.org) pumping-system assessment publication is the natural source

## sludge-dewatering

### Sludge dewatering equipment (wwt-sludge-dewatering-equipment)

Primary code: WWT: Wastewater and water reuse
Decanter centrifuges, belt filter presses, membrane filter presses and screw presses that turn conditioned sludge into 18-40% DS cake.
Vendors: Alfa Laval, ANDRITZ, Flottweg SE, HUBER SE (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| centrifuge cake DS on digested sludge | 22-30 % DS | published centrifuge performance |
| membrane press cake DS | 30-40 % DS | published filter-press performance |

- **Alfa Laval** decanters: municipal sludge duty
- **ANDRITZ** presses: 18-40% DS cake
- **Flottweg SE** Tricanter: simultaneous solids/oil/water separation
- **HUBER SE** Q-PRESS: 6-25% DS cake, low power

Recorded gaps:

- per-model capacities — Read Alfa Laval/Andritz/Flottweg model pages

## switchgear

### Data centre medium-voltage switchgear (mv-switchgear-data-centre)

Primary code: IDC: Data centres
The MV layer that takes utility or on-site generation supply into a data-centre campus and splits it to transformers and UPS halls: air-insulated (AIS) for flexible, expandable rooms and gas-insulated (GIS) where footprint or harsh conditions rule. ABB's MV switchgear covers 1-52 kV under IEC to IEC 62271, with SF6-free insulation (dry air or natural-origin gases, GWP below 1) available for most 6-24 kV applications and compliant with EU F-gas regulation 2024/573; data centres are a named served industry.
Vendors: ABB, Schneider Electric, Eaton, Anord Mardix, Hitachi Energy (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| medium-voltage switchgear range (IEC) | 1-52 kV | 1 kV to 52 kV according to IEC standards (vendor range statement); standards compliance to IEC 62271 |
| SF6-free insulation coverage | 6-24 kV | SF6-free GIS suitable for most 6-24 kV switching applications with dry air or natural-origin gases, GWP below 1, EU F-gas regulation (EU) 2024/573 compliant |

- **ABB** ABB medium-voltage switchgear (AIS and GIS): 1-52 kV IEC; SF6-free GIS for 6-24 kV; LSC2B/LSC2A/LSC2/LSC1 service continuity classes

Recorded gaps:

- rated current and short-circuit withstand per panel family — Read ABB UniGear and SafeRing datasheets for current/short-circuit figures
- Schneider PIX/SM6 and Hitachi Energy model lines — Read both ranges and add model lines

## turbine

### Industrial gas turbine (aeroderivative and heavy-frame) (turbine-gas-industrial)

Primary code: PWR: Power and renewables
Gas turbine for power generation and mechanical drive, in two families: aeroderivative units adapted from jet engines (fast start, high simple-cycle efficiency, modular exchange) and heavy-frame machines built for bulky base-load duty behind the grid or as compressor drives on pipelines and gas plants. Sets the exhaust energy that an HRSG converts in combined-cycle and cogeneration service.
Vendors: Baker Hughes, GE Vernova, Solar Turbines, Siemens Energy (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| aeroderivative output, LM6000PF+ (50 Hz, ISO) | 52.5-53.8 MW | 52.5 MWe at generator terminals (power generation); 53.8 MW mechanical drive; vendor spec table |
| aeroderivative simple-cycle efficiency, LM6000PF+ | 41-42 % | vendor spec table: 41% power generation, 42% mechanical drive |
| packaged aeroderivative output, LM2500XPRESS+ (50 Hz, ISO, natural gas) | 34.5-36.3 MW | G4 and G5 DLE UPT packaged variants |
| hydrogen-blend operating experience | 5-95 % hydrogen by volume | about 2 million operating hours on hydrogen-blend fuels across the fleet; headline capability up to 95% by volume |

- **Baker Hughes** LM6000PF+ aeroderivative gas turbine: 52.5 MWe power generation / 53.8 MW mechanical drive, 41-42% simple-cycle efficiency (ISO, 50 Hz)
- **GE Vernova** LM2500XPRESS+ packaged aeroderivative: 34.5-36.3 MW (50 Hz, ISO, natural gas); hydrogen-blend experience 5-95% by volume

Recorded gaps:

- heavy-frame (H/F-class) power and efficiency ranges per model — locate the current 9HA/SGT product pages (or fact-sheet PDFs) and add heavy-frame output/efficiency ranges and vendor model lines
- Solar Turbines Titan-family model ranges for the 1-25 MW industrial segment — fetch Titan 130 / Taurus 70 pages via a browser session and add model lines
- exhaust-temperature and exhaust-flow ranges that drive HRSG sizing — extract per-model exhaust data from the OEM spec tables already cited on the combined-cycle cards

## ups

### Data centre UPS (uninterruptible power supply) (ups-data-centre)

Primary code: IDC: Data centres
Double-conversion UPS systems sized per data hall and paralleled to multi-MW capacity, bridging the IT load between a mains disturbance and generator pickup. The class follows the same specification pattern as industrial UPS but is driven by hyperscale density, lithium-ion adoption and, increasingly, grid-interactive operation.
Vendors: Vertiv, Schneider Electric, Eaton, ABB (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| unit power range, Vertiv Liebert EXL S1 class | 100-1200 kW | 100-1200 kW per unit, transformer-free high-density design; parallel systems to about 9.6 MW |
| parallel system capacity, EXL S1 fleet | 9.6 MW | about 9.6 MW via parallel deployment, suitable for a 20 MW data-centre design |

- **Vertiv** Liebert EXL S1: 100-1200 kW per unit, parallel to about 9.6 MW

Recorded gaps:

- efficiency per operating mode (double-conversion vs eco) — Read the EXL S1 datasheet efficiency tables and record per-mode figures
- Schneider Galaxy VX/VL and Eaton 93PM capacity ranges — Read both vendor product pages and add model lines

## uv-reactors

### UV disinfection reactors (wwt-uv-reactors)

Primary code: WWT: Wastewater and water reuse
Closed-vessel or open-channel UV systems (low-pressure, medium-pressure, LED) delivering 20-100 mJ/cm2 with validated dose monitoring.
Vendors: Trojan Technologies, Xylem (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| delivered dose | 20-100 mJ/cm2 | published municipal range |

- **Trojan Technologies** UVSwift/UltraFlow: municipal open-channel and closed-vessel

Recorded gaps:

- per-model lamp counts and flows — Read Trojan/UVDI model pages
