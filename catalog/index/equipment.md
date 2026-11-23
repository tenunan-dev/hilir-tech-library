# Equipment catalog

58 equipment records (one per equipment class, schema `schema/equipment.schema.json`).
Each record carries specification ranges with their sources and the directory vendors that
supply the class. Start of the equipment layer per the owner: boiler first, next families
follow the registration queue.

## aeration

### Aeration systems (blowers and diffusers) (wwt-aeration-systems)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
The energy centre of biological treatment: blowers (turbo, screw, lobe) and fine-bubble diffuser grids or mechanical aerators deliver oxygen to activated-sludge and MBBR basins.
Vendors: Xylem (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fine-bubble diffuser oxygen transfer efficiency | 2-4 %/m | published SOTE per metre of submergence |
| turbo blower sizes | 30-500 kW | typical single-unit range |

- **Xylem** Sanitaire: basin aeration systems

Recorded gaps:

- per-model blower efficiency tables — Read Sanitaire/GE turbo blower datasheets

## air-separation-unit

### Air separation unit (ASU) (air-separation-unit)

Primary code: GAS: Gas processing and LNG
Cryogenic distillation plant that separates air into nitrogen, oxygen and argon. In ammonia plants the ASU supplies the nitrogen feed at high purity; in gasification, oxyfuel and CCS plants it supplies oxygen.
Vendors: Linde, Air Products (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| nitrogen purity | <1 ppm O2 | cryogenic distillation delivers almost pure nitrogen, typically below 1 ppm oxygen |
| product delivery pressure | 5-10 barg | typical gaseous product delivery pressure |
| main air compressor power | 50720 kWe | NETL design case for a 1.3 Mt/yr ammonia ATR plant |
| specific energy, conventional cryogenic ASU | 245 kWh/t O2 | conventional ASU at >99.5% oxygen purity, per tonne of contained oxygen; 20 C ambient, 15 C cooling water, 60% RH, sea level (oxygen basis, not ammonia nitrogen basis) |

- **Linde** Linde standard ASU families: NOVON 3,000-150,000 Nm3/h gaseous O2; LION 1,000-24,000 Nm3/h liquid; SPECTRA 8,000-90,000; INSPIRE 8,000-70,000; LOGO 3,000-30,000 Nm3/h at 90-95%
- **Air Liquide** Air Liquide standard ASU plants: SIGMA 110-350 t/d O2 at 96-99.6% and up to 40 barg; Yango 330-770 t/d O2 at 99.5-99.8%; APSA 1,000-50,000 Nm3/h N2 at 2-10 barg
- **Air Products** Cryogenic ASU: from 50 t/d oxygen up to single-train plants beyond 4,000 t/d, with development toward 7,000 t/d

Recorded gaps:

- ASU specific energy on a nitrogen basis (kWh/t N2) — fetch an OEM ASU datasheet that states capacity and kWh/t N2

## ammonia-converter

### Ammonia synthesis converter (ammonia-synthesis-converter)

Primary code: H2: Hydrogen and low-carbon fuels
Catalytic reactor in the Haber-Bosch loop where hydrogen and nitrogen combine over an iron catalyst to form ammonia. Conversion per pass is limited by equilibrium, so the loop circulates unreacted gas, condenses ammonia by refrigeration and returns the remainder to the converter.
Vendors: Topsoe, thyssenkrupp Uhde, KBR, Casale (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| operating pressure | 150-200 bar | typical ammonia synthesis pressure as stated |
| reactor temperature | 380-520 °C | NH3 synthesis reactor operating temperature |
| single-train capacity | small-3500 t/d | large single-train ammonia converters up to 3,500 MTPD; Uhde quotes 3,300 mtpd and more |
| conversion per pass | 15 % | about 15% of the gas turns into ammonia on each pass |

- **Topsoe** S-200 ammonia converter basket: two-bed radial flow with indirect cooling between beds; more than 130 units since 1976
- **Topsoe** S-300 ammonia converter basket: three-bed radial flow; higher conversion and production efficiency than S-200; more than 50 installations
- **KBR** KBR ammonia converter: vertical converters below 2,000 MTPD; horizontal units up to 6,000 MTPD; add-on bed gives 21-24% conversion
- **thyssenkrupp Uhde** uhde ammonia converter A30/A20 series: three radial catalyst beds in one or two converters; loop up to 210 bar; A30 4,000-5,000 mtpd

Recorded gaps:

- per-vendor converter model lines with casing, catalyst basket and pressure-drop data — fetch Topsoe S-200/S-300, KBR, Casale and Uhde converter pages and add model lines

## anaerobic-digesters

### Anaerobic digesters (sludge and organics) (wwt-anaerobic-digesters)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
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

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
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

### Gas-fired and gas-conversion circulating fluidized bed boiler (boiler-gas-cfb)

Primary code: PWR: Power and renewables
Circulating fluidized bed boiler in which fine solids are suspended in a high-velocity gas stream and circulated through a cyclone or U-beam collector back to the furnace. Commercial CFB lines from the OEMs read are dominated by solid and multi-fuel designs; natural-gas firing is evidenced as a solid-fuel-to-gas conversion offering and as gas firing in a circulating-bed alumina calciner, not as a dedicated gas-fired boiler product.
Vendors: Babcock & Wilcox, Valmet, ANDRITZ, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam capacity, B&W IR-CFB | 2200000 lb/h | B&W IR-CFB product specifications: 2.2 million lb/h (277 kg/s) or greater as required |
| steam pressure, B&W IR-CFB | 2600 psig | B&W: 'to 2600 psig' (17.9 MPa) |
| steam temperature, B&W IR-CFB | 1050 degF | B&W: 'as required, usually to 1050 F (566 C)' |
| size range, Valmet CFB | 30-1200 MWth | Valmet: boilers from 30 to 1,200 MWth (solid/multi-fuel range) |
| size range, ANDRITZ waste CFB | 50-200 t/h | ANDRITZ PowerFluid Waste CFB: 50-200 t/h steam (40-150 MW) |
| fluidizing velocity, CFB | 10-30 ft/s | EPA technology overview: about 10-30 ft/s for CFB versus 2-12 ft/s for conventional FBC; historical report, not a current guarantee |
| natural-gas NOx in circulating fluid bed calciner | 40 ppm | EPA report: 40 ppm NOx achieved with natural gas firing in a Lurgi circulating fluid bed alumina calciner at up to 2,650 F; this is NOT a steam boiler |


Recorded gaps:

- named 100% natural-gas-fired CFB boiler plant with owner, capacity, status and date — Read the Zeeco/ASME POWER2014-32258 paper and any operator conversion case study.
- gas-fired CFB burner counts, gas-train specifications and emission guarantees — Search OEM conversion case studies and burner datasheets.

### Gas-fired condensing hot-water boiler (boiler-gas-condensing-hot-water)

Primary code: PWR: Power and renewables
Packaged hydronic boiler that cools flue gas below its dew point to recover the latent heat of water vapour, using corrosion-resistant duplex or stainless heat-transfer surfaces. Available as one-pass firetube designs with premix or dual-fuel burners, with high turndown and integrated controls for commercial and institutional heating.
Vendors: Cleaver-Brooks, Fulton (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| minimum combustion efficiency, large commercial gas hot-water boiler | 96 % Ec | DOE FEMP purchasing requirement for 2.5-10 MMBtu/hr input gas-fired hot-water boilers, based on 10 CFR 431.86 |
| input capacity, Cleaver-Brooks ClearFire-CE | 500-6000 MBH | 11 models from 500 to 6,000 MBH input |
| AHRI thermal efficiency, ClearFire-CE | 94.7-96 % | AHRI thermal 96.0% and combustion 94.7%; the page's 'up to 99%' is marketing wording |
| turndown, ClearFire-CE | 10 :1 | 10:1 fully modulating on the ClearFire-CE product page |
| NOx, ClearFire-CE standard | 20 ppm | Under 20 ppm NOx standard, sub-7 ppm optional (OEM specification) |
| hydrogen blend capability | 20 % by volume | Manufacturer states burner and controls support up to 20% volumetric hydrogen-natural gas blend; not a certification |
| input capacity, Cleaver-Brooks SwitchFire | 6000-12000 MBH | 6,000 / 10,000 / 12,000 MBH models |
| AHRI thermal efficiency, SwitchFire | 95.6-96.3 % | AHRI combustion 95.6% / thermal 96.3%; 'up to 98%' is OEM wording |

- **Cleaver-Brooks** ClearFire-CE: 500-6,000 MBH, AHRI thermal 96%, 10:1 turndown, duplex stainless with TurboFer/AluFer tubes
- **Cleaver-Brooks** SwitchFire: 6,000-12,000 MBH, gas-only premix to 15:1 turndown or dual-fuel Weishaupt burner to 6:1

Recorded gaps:

- named condensing-boiler installations in Asia Pacific — Look for FEMP case studies and OEM reference lists with owner, capacity and date.

### Gas-fired industrial water-tube package boiler (boiler-gas-water-tube-package)

Primary code: PWR: Power and renewables
Shop-assembled water-tube boiler with water inside the tubes and combustion gas outside, served by a steam drum and mud drum with downcomers and risers and a finned membrane furnace wall. Natural circulation and the separation of steam and water from the heated circuit allow much higher pressures and outputs than a shell boiler, and the design can fire natural gas, refinery gas or dual fuel.
Vendors: Babcock & Wilcox, Cleaver-Brooks, Miura Boiler (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam output, power-station class | 500 kg/s | Spirax Sarco: 'high steam output (up to 500 kg/s)' |
| design pressure, power-station class | 160 bar | Spirax Sarco: 'high pressure steam (up to 160 bar)' |
| superheated steam temperature | 550 degC | Spirax Sarco: 'superheated steam (up to 550 C)' |
| capacity range of alternative water-tube layouts | 5000-180000 kg/h | Spirax Sarco: layouts 'available with capacities from 5 000 kg/h to 180 000 kg/h' |
| B&W industrial water-tube package capacity | 10000-1200000 lb/h | B&W package boiler range 10,000-1,200,000 lb/h (4.5-544.2 t/h) as recorded in the existing boiler-industrial-watertube-package record |
| NOx, ultra-low-NOx gas burner | 9 ppm at 3% O2 | Miura LX water-tube boiler with quenched-flame burner: 9 ppm at 3% corrected O2, natural gas or propane |
| fuel-to-steam efficiency | 85-87 % | Miura states 85% for LX and 87% with built-in energy recovery and water treatment, against 83% 'typical fire-tube' (vendor comparison) |

- **Miura Boiler** LX once-through vertical water-tube: 50-300 HP, 9 ppm NOx at 3% O2 on natural gas or propane

Recorded gaps:

- whether current OEM literature uses the D-type/O-type terminology on the earlier record — Confirm the layout names against a current B&W package-boiler brochure before relying on them.

### Gas-fired packaged fire-tube (shell) steam boiler (boiler-gas-fire-tube-package)

Primary code: PWR: Power and renewables
Shop-assembled shell boiler with the burner firing into a large furnace tube and hot gas making two to four passes through tubes surrounded by boiler water; the standard packaged steam source for small and medium gas-fired industrial loads. Wet-back reversal chambers give more heating surface than refractory-lined dry-back designs.
Vendors: Cleaver-Brooks, Fulton, Miura Boiler (2 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| furnace/flue tube wall thickness | 18-20 mm | Spirax Sarco: 'a compromise is reached with a furnace tube wall thickness of between 18 mm and 20 mm' |
| practical pressure limit | 27 bar | Spirax Sarco: that tube wall thickness 'translates to a practical pressure limit for shell boilers of around 27 bar'; most operate at 17 bar or less |
| gas temperature before reversal chamber, plain steel | 420 degC | Spirax Sarco: gas should be cooled to at least 420 C before entering the reversal chamber of a plain-steel shell boiler |
| gas temperature before reversal chamber, alloy steel | 470 degC | Spirax Sarco: 470 C minimum for alloy-steel construction |
| flame temperature in furnace tube | 1800 degC | Spirax Sarco: flame temperature 'may be up to 1800 C' |
| Cleaver-Brooks CBEX output range | 100-2500 HP | CBEX packaged firetube: 100-2,500 HP, steam to 300 psig, hot water to 125 psig, 2- or 3-pass |
| Cleaver-Brooks CBLE output range | 50-800 HP | CBLE four-pass packaged firetube: 50-800 HP, steam to 300 psig |
| NOx options, natural gas | 5 ppm | CBLE offers NOx ratings down to 5 ppm on natural gas (vendor options) |

- **Cleaver-Brooks** CBEX: 100-2,500 HP, 2/3-pass, extended heat-transfer tubes
- **Cleaver-Brooks** CBLE: 50-800 HP, 4-pass, NOx options to 5 ppm

Recorded gaps:

- turndown and part-load efficiency curves for the main gas fire-tube lines — Read distributor specification sheets for turndown data.

### Heat recovery steam generator (HRSG) (boiler-hrsg)

Primary code: PWR: Power and renewables
Boiler fired by hot combustion-turbine or furnace exhaust gas rather than by burners, raised in horizontal or vertical panels behind a gas turbine with one or more drum pressures and optionally reheat. Converts a gas turbine into a combined-cycle or cogeneration plant and is the deciding component for how much of the turbine exhaust energy becomes steam.
Vendors: Babcock & Wilcox, Cleaver-Brooks, Doosan Enerbility, IHI Corporation, Sumitomo SHI FW, GE Vernova, John Zink Company, Tetra Engineering Group, Entech Products Corp (6 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam-cycle efficiency by HRSG configuration | 20-30 % | about 20% for two-pressure without reheat, 26% for three-pressure, about 30% for three-pressure with reheat |
| installed HRSG fleet, GE Vernova | 1300 units | OEM statement: more than 1,300 HRSGs installed worldwide |
| once-through HRSG operating experience | 2.5 million hours | OEM statement: over 2.5 million operating hours for once-through HRSG technology |
| US combined-cycle capacity with duct burners | 208 GW | About 208 GW of 278 GW US combined-cycle fleet has duct burners, EIA-860/EIA-923, June 2022 |
| HRSG component scope | pressure parts and catalyst housings qualitative | B&W supplies HARPs, superheaters, reheaters, economisers, finned tubing, headers, casing, inlet ducting, HP/IP/LP drums and SCR/CO catalyst housings |

- **Babcock & Wilcox** HRSG systems, upgrades and components: reliable HRSG systems plus upgrades and replacement components — HARPs (high pressure evaporators), headers, finned tubing and other pressure parts — suitable for a wide range of combustion turbine applications
- **Cleaver-Brooks** packaged HRSG for small turbines: state-of-the-art customized packaged heat-recovery steam generators for gas-fired turbines from 1 to 60 MW
- **GE Vernova** Horizontal drum / horizontal once-through / vertical drum HRSG: supplementary firing, SCR/CO catalysts, bypass and modular construction; 1,300+ installed (OEM statement)
- **John Zink Company** HRSG duct burners: LDRW, VC and Coen-casting flame holders with igniters and flame scanners
- **GE Vernova** Horizontal drum / horizontal once-through / vertical drum HRSG: supplementary firing, SCR/CO catalysts, bypass and modular construction; 1,300+ installed (OEM statement)
- **John Zink Company** HRSG duct burners: LDRW, VC and Coen-casting flame holders with igniters and flame scanners

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

## burner

### HRSG duct burner (supplementary gas firing) (duct-burner-hrsg)

Primary code: PWR: Power and renewables
Burner installed in the gas-turbine exhaust duct to burn additional natural gas in the remaining oxygen and raise steam output. Two main forms are standard round gas burners and linear grid burners spanning the duct. Installed in the transition duct before the lead tube bank or between superheater stages, with flame holders, pilots, igniters and flame scanners.
Vendors: John Zink Company, Cleaver-Brooks, Entech Products Corp (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| heat input, Cleaver-Brooks Natcom | 10-500 MMBtu/hr | HRSG supplementary firing: 10-500 MMBtu/hr, natural gas and propane |
| emissions, Cleaver-Brooks Natcom | 7 ppm | Available to under 7 ppm NOx and under 50 ppm CO; attribute table also states under 0.1 lb/MMBtu |
| emissions, John Zink ProLine in-line | 0.03 lb/MMBtu | 0.03 lb/MMBtu for each of NOx and CO; gaseous fuels including natural gas and hydrogen |
| heat release per unit length, ProLine | 5 MMBtu/hr/ft | Up to 5 MMBtu/hr per foot of burner length (4.8 MW/m) |
| turndown, ProLine | 20 :1 | 20:1 stated for the in-line duct burner |
| runner sag inspection criterion | 2-3 in | Tetra Engineering: excessive sag above 2-3 in (5-8 cm) at runner midpoint; one improperly installed runner buckled in under 10,000 operating hours |
| US combined-cycle capacity with duct burners | 208 GW | About 208 GW of the 278 GW US combined-cycle fleet, EIA-860/EIA-923 data, article June 2022 |
| capacity factor with versus without duct firing | 47-59 % | EIA 2020: 59% for plants with duct firing versus 47% without; fleet average 56% |

- **John Zink Company** ProLine in-line duct burner: 0.03 lb/MMBtu NOx and CO, to 5 MMBtu/hr/ft, 20:1 turndown
- **John Zink Company** Duct-burner flame holders: LDRW low-draft reverse wing, VC V-cone tip wing and Coen castings, with igniters and flame scanners
- **Cleaver-Brooks** Natcom duct burner: 10-500 MMBtu/hr, under 7 ppm NOx / under 50 ppm CO

Recorded gaps:

- quantified duct-firing duty ranges for named HRSG projects — Find HRSG OEM duct-burner specification sheets with heat input and exhaust conditions.

### Low-NOx gas burner (package and ultra-low-NOx) (burner-gas-low-nox)

Primary code: PWR: Power and renewables
Burner that stages fuel and air, delays mixing or recirculates flue gas to lower flame temperature and NOx formation. Package gas burners span roughly 10-500 MMBtu/hr with 10:1 turndown; ultra-low-NOx versions reach single-digit ppm NOx with flue-gas recirculation or surface-stabilised premixed combustion. Used on fire-tube, water-tube and hot-water boilers and on refinery fired heaters.
Vendors: Cleaver-Brooks, Zeeco, John Zink Company, ALZETA, Miura Boiler (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| NOx, natural gas without FGR | 30 ppm at about 3% O2 | Cleaver-Brooks SBR-30: under 30 ppm at about 3% O2 across a wide load range |
| heat input, SBR-30 | 16.8-54.6 MMBtu/hr | 16,800-54,600 MBH (16.8-54.6 MMBtu/hr); 400-1,300 HP boilers |
| heat input, SBR-5 | 10.5-42 MMBtu/hr | 10,500-42,000 MBH (10.5-42 MMBtu/hr); 250-1,000 HP boilers, gas or ASTM 2D-S15 |
| NOx with induced FGR | 5 ppm | SBR-5: 5 ppm at about 3% O2 (body states 3-4%) with induced FGR |
| NOx ladder versus excess air, Zeeco PLN | 9-40 ppm | 40 ppm at 40%, 30 at 45%, 15 at 50%, 9 at 60% excess air without FGR; O2 reference basis not stated |
| heat release, Zeeco PLN/GO | 2.5-63 MMBtu/hr | 2.5-63 MMBtu/hr (0.73-18.5 MW), natural gas, LPG or other on request |
| NOx with staged flame and internal FGR | 30 ppm | Zeeco GO: 30 ppm at 15% excess air on natural gas/propane without external FGR; O2 basis not stated |
| NOx without FGR, ECOjet Edge+ | 15 ppm | John Zink: as low as 15 ppm without FGR in select applications; more than 350 ECOjet installations (vendor statement) |
| NOx, surface-stabilised premix burner | 5 ppm at 3% O2 | ALZETA: below 5 ppm corrected to 3% O2 for most commercial and industrial heating applications |
| turndown, package gas burners | 10 :1 | 10:1 stated for SBR-30/SBR-5 and Zeeco PLN/GO |

- **Cleaver-Brooks** ProFire SBR-30 / SBR-5: 16.8-54.6 and 10.5-42 MMBtu/hr; 10:1; 30 ppm without FGR / 5 ppm with FGR
- **Zeeco** PLN / GO: 2.5-63 MMBtu/hr; 10:1; 9-40 ppm versus excess air (PLN), 30 ppm at 15% excess air (GO)
- **John Zink Company** ECOjet Edge+: as low as 15 ppm NOx without FGR in select applications; natural gas to 100% hydrogen
- **ALZETA** surface-stabilised premix: below 5 ppm corrected to 3% O2

Recorded gaps:

- common O2 reference basis for the quoted NOx figures — Obtain emission test sheets stating both excess air and O2 reference.

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

## carbamate-condenser

### Urea carbamate condenser (urea-carbamate-condenser)

Primary code: PCH: Petrochemicals
High-pressure exchanger where ammonia and carbon dioxide from the stripper recombine into carbamate, releasing heat that is recovered as steam. Pool-condenser designs carry the reaction further in the condenser itself, which reduces the duty left for the reactor and the recycle section.
Vendors: Stamicarbon, thyssenkrupp Uhde, Toyo Engineering, Casale, Saipem (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| HP loop pressure | 150 bar | Saipem urea flowsheet, NH3-stripping process |
| condenser outlet temperature | 155 °C | Saipem urea flowsheet, NH3-stripping process |
| approach to equilibrium in a pool condenser | 60 % | reaction extent achieved in the pool condenser |

- **Stamicarbon** LAUNCH MELT pool condenser design: capacities from about 2,500 up to 6,000 mtpd
- **thyssenkrupp Uhde** Urea 2000plus pool condenser: horizontal high-pressure carbamate condenser with submerged U-tube bundle
- **Toyo Engineering** Vertical Submerged Carbamate Condenser (VSCC): 180 C and 152 bar; produces 5 bar steam

## clarifiers-thickeners

### Clarifiers and thickeners (wwt-clarifiers-thickeners)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
Primary/secondary circular clarifiers and gravity/DAF thickeners with scraper bridges, plus lamella packs for high-rate duty.
Vendors: Veolia, WesTech Engineering (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| lamella effective area gain | 8-10 x | versus tank footprint |

- **Veolia** Actiflo/high-rate: 60-120 m/h loading

Recorded gaps:

- per-model tank sizes — Read WesTech/Veolia clarifier model pages

## cleaning

### Boiler soot blower and online cleaning (soot-blower-boiler)

Primary code: PWR: Power and renewables
Online cleaning equipment that removes ash and soot deposits from heat-transfer surfaces to preserve efficiency, keep flue-gas temperatures within design and prevent gas-passage blockage. Saturated steam is the most widely used blowing medium because boiler-generated steam is available; SCR catalyst cleaning uses much lower steam velocity to avoid mechanical or erosive damage.
Vendors: Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| blowing medium | saturated steam qualitative | Saturated steam is the most widely used medium because boiler-generated steam avoids an external supply |
| SCR catalyst cleaning velocity | low velocity qualitative | Steam velocity is low compared with boiler sootblowing applications to avoid mechanical or erosive damage |


Recorded gaps:

- blower counts, stroke lengths, steam pressure and duty per surface — Read an OEM sootblower data sheet for a reference boiler.

## co2-stripper

### Urea CO2 stripper (urea-co2-stripper)

Primary code: PCH: Petrochemicals
High-pressure column that strips unconverted carbamate from the urea solution using feed CO2 as the stripping agent, decomposing carbamate and returning ammonia and CO2 to the condenser. CO2 stripping cut the steam demand of urea plants relative to conventional total-recycle designs.
Vendors: Stamicarbon, thyssenkrupp Uhde, Toyo Engineering (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| stripper effluent pressure | 140 bar | CO2-stripping process, effluent conditions as stated |
| stripper effluent temperature | 190 °C | CO2-stripping process, effluent conditions as stated |
| residual carbamate in stripper outlet solution | 1-2 % | solution leaving the stripper |
| stripping steam consumption | 0.8-1.0 t steam/t urea | steam used per tonne of urea in the stripping section |

- **Stamicarbon** High-pressure CO2 stripper: CO2 stripping; no medium-pressure recirculation stage downstream
- **Casale** SPLIT FLOW LOOP: best suited up to 2,300 MTD, or 3,500 MTD with medium-pressure stage
- **Saipem** Falling-film stripper 31/41 E-1: operates at 146 kg/cm2g

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

## controls

### Boiler controls and oxygen trim (boiler-controls-oxygen-trim)

Primary code: PWR: Power and renewables
Control system that holds the fuel-to-air ratio and steam conditions across load. A stand-alone PLC oxygen-trim package uses an O2 sensor, firing-rate sensor and actuator or variable-speed drive to compensate for temperature, barometric pressure and fuel changes; package burners add parallel positioning, remote monitoring and burner-management interlocks.
Vendors: Cleaver-Brooks, Honeywell, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| O2 trim architecture | PLC + O2 and firing-rate sensors qualitative | Stand-alone PLC-based system: O2 sensor + firing-rate sensor + PLC panel + actuator or VSD |
| control modes | air trim / fuel trim qualitative | Air trim or fuel trim; single-point/jackshaft with customisation for parallel positioning or alternate fuel |
| compensated variables | temperature, pressure, fuel qualitative | Compensates for temperature, barometric pressure and fuel changes |
| remote monitoring | parallel positioning + IoT qualitative | Parallel positioning and remote IoT monitoring included on ProFire SBR-30/SBR-5 |
| safety-limit supervision | interlocks + flame supervision qualitative | Interlocks/permissives, flame presence monitoring, safety-limit supervision, prepurge and controlled shutdown |


Recorded gaps:

- measured savings and set-point accuracy for O2 trim on gas boilers — Find a controlled trial or OEM datasheet stating O2 set point and fuel saving.

### Burner management and flame safeguard system (burner-management-safety-system)

Primary code: PWR: Power and renewables
Safety system that sequences purge, ignition and firing and trips the fuel on loss of flame or failed permissives. Designed to NFPA 85/86, IRI, ISA 84, FM and Gastec practice; flame supervision uses UV or IR viewing heads, with SIL3-capable assemblies available.
Vendors: Honeywell, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| UV detector spectral response | 185-260 nm | Honeywell S70X/S80X UV models: UVTron sensor, 185-260 nm, peak 210 nm |
| IR detector spectral response | 950-1710 nm | Honeywell IR models: germanium detector, 950-1,710 nm |
| functional safety capability | 3 SIL | S702/S802 and S706/S806 viewing-head families are SIL 3 capable |
| ambient temperature range | -40-85 degC | Standard S70X/S80X models rated -40 to +85 C |
| UV tube life | 10000-50000 hours | 10,000-50,000 hours depending on conditions, with monthly sensitivity check recommended |
| optical field of view | 1-5 degrees | IR models 1 degree, UV models 5 degrees |
| standards basis | NFPA 85/86, IRI, ISA 84, FM, Gastec qualitative | Honeywell states systems are engineered to NFPA 85/86, IRI, ISA 84, Factory Mutual and Gastec practice |


Recorded gaps:

- trip logic and proof-of-closure arrangements for specific boiler makes — Read the burner OEM's BMS sequence matrix and NFPA 85 (primary text is paywalled).

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

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
DAF clarifiers: air-saturation vessels release 30-100 um microbubbles into coagulated water; floated flocs are scraped off as a thick float sludge.
Vendors: Veolia, Evoqua Water Technologies (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| microbubble size | 30-100 um | published DAF design range |
| hydraulic loading | 5-15 m/h | typical design HLR |

- **Veolia** F flotation family: 5-15 m/h loading

Recorded gaps:

- per-model flow ranges — Read Veolia/Evoqua DAF model pages

## emissions-control

### SCR, SNCR and CEMS for boilers (scr-nox-control-boiler)

Primary code: PWR: Power and renewables
Post-combustion NOx control. SCR passes flue gas over a catalyst with a reagent, achieving up to 95% reduction on packaged systems; SNCR injects reagent into a 870-1,150 C window and gives 30-50% reduction alone or 65-75% with combustion controls. CEMS provides the continuous concentration and emission-rate measurement used to demonstrate compliance.
Vendors: Cleaver-Brooks, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| NOx reduction, packaged SCR | 95 % | Cleaver-Brooks states up to 95% reduction; the page says 1 ppm in its summary and 2 ppm in its body without burner rework |
| stack NOx with SCR, modular HRSG | 2 ppm | Available below 2 ppm NOx with SCR and integrated CO catalyst on 25-60 MW modular HRSGs |
| SCR scope of supply | full SCR scope qualitative | Reactor, DeNOx catalyst, oxidation catalyst, reagent storage/dosing/injection, PLC, silencers, CEMS, platforms and catalyst management |
| NOx reduction, SNCR alone | 30-50 % | EPA fact sheet: 30-50% reduction |
| NOx reduction, SNCR with combustion controls | 65-75 % | EPA fact sheet citing ICAC 2000: 65-75% with low-NOx burners |
| SNCR reaction temperature window | 870-1150 degC | 870-1,150 C (1,600-2,100 F); enhancers can lower the window |
| permitted ammonia slip | 2-10 ppm | Typical US permitted levels 2-10 ppm |
| SNCR capital cost, industrial boilers | 900-2500 USD per MMBtu/hr | USD 900-2,500 per MMBtu/hr for units above 100 MMBtu/hr, stated in 1999 dollars; not escalated |
| CEMS definition | analysers + conversion qualitative | Total equipment for gas/PM concentration or emission rate using analyser measurements plus a conversion equation, graph or program |


Recorded gaps:

- SCR ammonia-slip guarantee and catalyst life for gas-fired package boilers — Read an OEM SCR data sheet with slip, catalyst volume and temperature window.
- which of the Cleaver-Brooks SCR 1 ppm / 2 ppm statements is current — Confirm with the OEM or an updated product sheet.

## evaporator-crystallisers

### ZLD evaporators and crystallisers (wwt-evaporator-crystallisers)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
Mechanical-vapour-recompression evaporators and forced-circulation crystallisers that end ZLD trains: distillate recycled, salts recovered as solids.
Vendors: Aquatech International, Veolia (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| distillate TDS | 1-10 mg/L | Aquatech published ZLD performance |
| brine concentration reached | 200000-280000 mg/L TDS | Aquatech published ZLD performance |

- **Aquatech International** Aquatech ZLD: full ZLD trains

Recorded gaps:

- per-model m3/d ranges — Read Aquatech/Veolia HPD model pages

## fan

### Boiler forced-draft fan and inlet silencer (fd-fan-boiler)

Primary code: PWR: Power and renewables
Fan that pushes combustion air through the windbox, burner and gas passes, and can also convey flue gas through catalysts, economiser, FGR ducting and stack. Arrangements 3, 4 and 7 are offered; inlet silencers and filters reduce intake noise and protect the fan, and a variable-speed drive can replace damper control at part load.
Vendors: Halgo Power (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fan arrangements | arrangements 3, 4, 7 qualitative | Halgo Power lists AMCA arrangements 3, 4 and 7 |
| FGR mixing arrangement | FGR mixing box with dampers qualitative | A portion of flue gas is routed to the FD fan intake and mixed with fresh air; dampers regulate both streams to lower flame temperature and NOx |
| inlet silencer purpose | fan inlet silencer qualitative | Sized to attach directly to the fan inlet and reduce intake noise to a specified decibel limit |
| part-load control | VFD or damper qualitative | VFD offered in lieu of dampers; many package boilers operate at a fraction of nameplate |


Recorded gaps:

- fan duty, static pressure and power for named boiler sizes — Obtain a fan selection datasheet with flow, pressure and speed for a reference boiler.

### Induced-draft fan, stack and FGR ducting (id-fan-stack-fgr)

Primary code: PWR: Power and renewables
Induced-draft fan and flue-gas path that maintain furnace draft and discharge products to stack. Stacks and ductwork are engineered from flue-gas volume, temperature and space constraints; dampers hold a set draft loss and an SCR reactor house is sized from the catalyst mass required to meet the emission limit. FGR ducting returns a controlled share of flue gas to the forced-draft intake.
Vendors: Halgo Power (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| stack/duct design inputs | flow, temperature, space, catalyst qualitative | Flue-gas volumetric flow, flue-gas temperature, space constraints and optional catalyst modules |
| stack damper function | constant draft loss qualitative | Maintain a predetermined draft loss; parallel or opposed blade with pneumatic actuators common |
| SCR reactor house sizing basis | catalyst mass qualitative | Dimensions set by the amount and density of catalyst needed to meet the specified emission limit |
| FGR effect on burner NOx | 5 ppm | Induced FGR on the SBR-5 burner gives 5 ppm NOx at about 3% O2 |


Recorded gaps:

- ID fan datasheets and quantified FGR ratios — Read fan and FGR datasheets for a specific boiler or HRSG.

## feedwater

### Feedtank, deaerator and feedwater pump (feedwater-deaerator-system)

Primary code: PWR: Power and renewables
System that stores returned condensate and make-up, heats it and removes dissolved oxygen before the feedwater pump delivers it to the boiler. Atmospheric feedtanks operate at 85-90 C; pressurised deaerators at 0.2 bar g / 105 C with 10-20 minutes of storage, about 5:1 turndown and a vent rate of 0.5-2 kg per 1,000 kg/h of capacity.
Vendors: Spirax Sarco, TLV, Cleaver-Brooks (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| atmospheric feedtank temperature | 85-90 degC | Spirax Sarco: typically 85-90 C, giving about 2 mg/L dissolved oxygen |
| pressurised deaerator pressure | 0.2 bar g | 0.2 bar g, equivalent saturation temperature 105 C |
| deaerator storage on full boiler load | 10-20 min | 10-20 minutes |
| water supply pressure to nozzles | 2 bar | At least 2 bar for good nozzle distribution |
| steam supply pressure to pressure control valve | 5-10 bar | 5-10 bar |
| deaerator turndown | 5 :1 | Approximately 5:1 |
| deaerator vent rate | 0.5-2 kg per 1000 kg/h | Manufacturers tend to recommend 0.5-2 kg of steam/air mixture per 1,000 kg/h of capacity |
| feedwater pH | 8.5-9 pH | Maintain feedwater at not less than pH 8.5 to 9 to limit CO2 corrosion |
| dissolved oxygen, high-pressure water-tube boilers | 7 ppb | Typically less than 7 ppb where superheated steam is required |
| feedtank capacity convention | 1 hours | Traditional practice: sufficient capacity for one hour of steaming at maximum evaporation |
| condensate return cavitation risk | 80 % | Very high condensate return rates, typically over 80%, may cause excessive feedwater temperature and feedpump cavitation |


Recorded gaps:

- feedpump head, NPSH and duty for the packaged boiler lines — Read a feedpump selection sheet for a stated boiler duty.

## granulator

### Urea fluid-bed granulator (urea-fluid-bed-granulator)

Primary code: PCH: Petrochemicals
Fluid-bed unit that builds urea granules from sprayed melt onto seed particles, with internal recycling and classification to hold a target granule size. Granules are larger and harder than prills, which suits bulk blending and reduces caking.
Vendors: thyssenkrupp Uhde, Stamicarbon, Toyo Engineering, Casale (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| granulation unit capacity | 3600 t/d | SAFCO IV granulation unit; more than 20 plants have capacities of 3,000 t/d or more |
| granule size | 2-8 mm | product sizes produced in one plant |
| recycle ratio | 0.5 ratio | recycle to product in a TEC fluid-bed granulator |
| bed temperature | 110-119 °C | fluid-bed granulator bed temperature in the cited study |

- **thyssenkrupp Uhde** UFT Fluid Bed Granulation: 2-8 mm product sizes from one plant; more than 20 plants at 3,000 mt/d or more
- **Toyo Engineering** Spout-Fluid Bed Granulation: scaled from 50 to 3,250 MTPD; designed to 4,500 MTPD
- **Stamicarbon** Fluid-bed granulation technology: 98.5 wt.% melt; up to 0.3 wt.% formaldehyde; on-stream time more than 150 days
- **Casale** GREEN GRANULATION: feed concentration can be as low as 96-97%

## heat-exchanger

### Boiler air preheater (air-preheater-boiler)

Primary code: PWR: Power and renewables
Heat exchanger that transfers heat from outgoing flue gas to incoming combustion air. Regenerative (rotary) designs use a rotating matrix or baskets; recuperative designs use tubular or plate elements. B&W supplies air heaters and notes the cold-end metal temperature is generally approximated from the average gas and air temperatures.
Vendors: Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| cold-end metal temperature basis | average of gas and air inlet temperatures qualitative | B&W: general assumption is that cold-end metal temperature is approximately the average of the gas and air inlet temperatures (qualitative, no numeric value on the read page) |
| product scope | tubular and regenerative air heaters qualitative | B&W air-heater product page read during the sweep; no performance table was given |


Recorded gaps:

- quantified air-heater duty, cold-end corrosion allowance and leakage rates — Read an air-heater data sheet with gas/air temperatures and leakage guarantee.

### Boiler economizer (feedwater heat recovery) (economizer-boiler)

Primary code: PWR: Power and renewables
Heat exchanger that raises feedwater temperature using flue gas leaving the boiler or superheater, cutting fuel use. Spirax Sarco gives about a 2% efficiency gain per 10 C rise in feedwater temperature; condensing economisers cool gas below the dew point and need corrosion-resistant surfaces.
Vendors: Babcock & Wilcox, Cleaver-Brooks, Spirax Sarco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| efficiency improvement per feedwater temperature rise | 2 % per 10 degC | Spirax Sarco: in broad terms a 10 C increase in feedwater temperature gives about a 2% efficiency improvement |
| feedtank fuel effect | 1 % per 6 degC | Spirax Sarco: about 1% less fuel required for every 6 C temperature rise in the feedtank |
| economizer metal temperature rise offline | 17-28 degC/h | B&W: economiser metal temperature can increase at 30-50 F/h (17-28 C/h) during an offline/air-leakage period |
| integrated condensing heat-exchanger efficiency | 96 % | ClearFire-CE AHRI thermal efficiency 96.0% with condensing heat exchanger |
| boiler horsepower heat-transfer convention | 5 sq ft/BHP | US convention: 5 sq ft of heat-transfer surface per boiler horsepower is common after 1900 (10 before) |


Recorded gaps:

- economizer duty and surface area for the gas boiler lines — Read OEM economizer specification sheets with gas inlet/outlet temperatures.

### Boiler superheater and attemperator (superheater-boiler)

Primary code: PWR: Power and renewables
Heat exchanger that adds heat to saturated steam, usually as pendant or horizontal banks in the gas path, with a desuperheater or attemperator controlling final steam temperature. Water-tube power boilers can reach 550 C superheated steam; separate or supplementary-fired superheaters are used where gas-turbine exhaust is too cool.
Vendors: Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| superheated steam temperature, upper capability | 550 degC | Spirax Sarco: 'superheated steam (up to 550 C)' for water-tube boilers |
| gas-turbine exhaust temperature to waste-heat boiler | 500 degC | Spirax Sarco: hot exhaust gases from a gas turbine approximately 500 C |
| SCR minimum inlet gas temperature | 104 degC | B&W: recommended minimum average gas temperature entering SCR equipment is 220 F (104 C) for cold start-up |


Recorded gaps:

- superheater surface, metal temperature limits and attemperator spray rates — Read OEM superheater design descriptions and cycling guidance.

## hv-circuit-breakers

### High-voltage circuit breakers (132-500 kV) (ele-hv-circuit-breakers)

Primary code: ELE: Electrical engineering
SF6 dead-tank and live-tank circuit breakers at 132, 275 and 500 kV for grid and substation duty, with interrupting ratings set by the Malaysian fault levels, to IEC 62271-100.
Vendors: Hitachi Energy, Siemens Energy, GE Vernova (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| interrupting requirement at 500 kV | 50 kA | TNB 500 kV fault rating 50 kA for 1 s, so breakers are specified at or above it |
| interrupting requirement at 275 kV | 40-50 kA | TNB 275 kV 40 kA for 3 s, 50 kA near power stations |
| interrupting requirement at 132 kV | 31.5-40 kA | TNB 132 kV 31.5 kA for 3 s, 40 kA near power stations |
| indicative cost, 145 kV dead-tank breaker | 40000-95000 USD per set | Western/Japanese brand new dead-tank at 145 kV roughly USD 40,000-95,000 (a Siemens SPS-145 used unit listed near USD 95,000; a Spanish tender for 145 kV 3150 A 31.5 kA at about EUR 26,000); Chinese OEMs quote far lower, USD 2,500-45,000. Export price list basis (accepted on owner instruction 2026-11-13). |
| indicative cost, 245 kV dead-tank breaker | 85000-150000 USD per unit | A municipal utility PO for a Siemens SP2-245 at USD 85,650/unit; Chinese OEM 252 kV units USD 60,000-93,000. Export price list basis (accepted on owner instruction 2026-11-13). |
| indicative cost, 550 kV dead-tank breaker | 200000-520000 USD per three-phase set | Chinese OEM 550 kV about USD 210,000-270,000; an import record of a 3150 A 50 kA three-phase set near USD 520,000; EGAT tender about THB 6.0 million per unit (about USD 170,000). Indicative and highly configuration-dependent. |

- **Hitachi Energy** Live tank / dead tank: 72.5-800 kV
- **Siemens Energy** 3AP / 3AT / SPS: 72.5-550 kV
- **GE Vernova** Dead tank breakers: 72.5-800 kV

Recorded gaps:

- SF6 leakage rate and mechanical operating times from a manufacturer datasheet — Ask the owner for a manufacturer breaker datasheet, or read a GE/Hitachi technical guide

## lv-switchboards

### LV switchboards and distribution boards (ele-lv-switchboard)

Primary code: ELE: Electrical engineering
Form 1-4 rated low-voltage assemblies at 415/240 V: main switchboards with air circuit breakers, motor control centres and final distribution boards, built to IEC 61439.
Vendors: ABB, Schneider Electric, Siemens, Eaton (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| busbar rated current, ABB MNS 3.0 | 630-6300 A | ABB MNS 3.0 catalogue: copper busbars rated current Ie up to 6300 A; distribution bars up to 2000 A |
| rated peak withstand current Ipk, ABB MNS | 220 kA | ABB MNS 3.0 catalogue: rated peak withstand current Ipk up to 220 kA |
| rated short-time withstand current Icw, ABB MNS | 100 kA | ABB MNS 3.0 catalogue: Icw up to 100 kA (arc-rated to IEC 61641 criteria 1-7 at 300 ms) |
| rated operational voltage Ue, ABB MNS | 690 V | MNS 3.0: Ue up to 690 V AC, Ui up to 1000 V AC, Uimp 6/8/12 kV |
| degree of protection, ABB MNS | 30-54 IP | MNS 3.0: IP30 to IP54, internal subdivision up to Form 4 |
| busbar rated current, Siemens SIVACON S8 | 630-7000 A | SIVACON S8 catalogue: main busbars rated currents up to 7,000 A |
| rated short-time withstand current Icw, Siemens S8 | 150 kA | SIVACON S8: Icw up to 150 kA, Ipk up to 330 kA |
| section dimensions, ABB MNS | 2200 mm | MNS 3.0: standard height 2200 mm; width 400-1200 mm; depth 800-1200 mm |
| indicative cost, LV switchboard section (IEC 61439, 50 kA/1 s, IP54) | 1000-5000 USD per section | Export price list (accepted price basis, owner instruction 2026-11-13): about USD 1,000 for a basic section rising past USD 5,000 for drawout main sections; Western-brand boards typically 2-4x Chinese FOB. Manufacturer price books are distributor-only, so this is FOB pricing, not a delivered Malaysian price. |

- **ABB** MNS: up to 6300 A
- **Schneider Electric** PrismaSeT / Blokset: 630-6300 A
- **Siemens** SIVACON S8: up to 7000 A
- **Eaton** xEnergy: up to 6300 A

Recorded gaps:

- per-form price tables from the manufacturers themselves — Ask a Malaysian panel builder (IPP/TNB-registered) for a section price benchmark

## membrane-systems

### MF/UF/RO membrane systems (wwt-membrane-systems)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
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
11 kV and 33 kV metal-clad or gas-insulated switchgear and compact ring main units used at TNB intake points and site substations, built to IEC 62271-200/60298.
Vendors: ABB, Schneider Electric, Siemens, Eaton (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| rated voltage, Siemens 8DJH | 7.2-24 kV | 8DJH datasheet covers 7.2, 12, 15, 17.5 and 24 kV ratings; TNB distributes at 11 kV and 33 kV |
| busbar continuous current, Siemens 8DJH | 630 A | 8DJH datasheet: busbar rated continuous current 630 A |
| internal arc classification, Siemens 8DJH at 12 kV | 25 kA for 1 s | 8DJH: short-time withstand 25 kA for 1 s up to 17.5 kV (20-21 kA for 3 s); optional IAC A FL/FLR 21 kA 1 s |
| partition and continuity class, Siemens 8DJH | LSC 2, partition class PM class | 8DJH datasheet: partition class PM, loss of service continuity LSC 2, type-tested to IEC 62271-200 |
| busbar current, ABB SafeRing/SafePlus | 630 A | ABB product scope table: max rated continuous current (busbar) 630 A for both the SF6 and the SF6-free SafeRing Air/SafePlus Air ranges |
| rated voltage and short-time withstand, ABB SafeRing/SafePlus | 12-40.5 kV | ABB product scope: up to 40.5 kV; short-time withstand up to 20 kA for 3 s at 24 kV and up to 25 kA for 3 s at 12/36/40.5 kV (SF6-free Air variant: up to 24 kV, 20 kA for 3 s). SF6 tank sealed for life over 30 years with leakage below 0.1% per year |
| rated voltage, Eaton Xiria 630 | 3.6-24 kV | Xiria 630 technical data table: rated voltage 3.6, 7.2, 12, 17.5 and 24 kV; impulse withstand 40-125 kV, power-frequency withstand 10-50 kV for 1 min |
| busbar current and peak withstand, Eaton Xiria 630 | 630 A | Xiria 630: load-break switch and circuit-breaker rated current 630 A; rated peak withstand current 50 kA; short-time withstand 20 kA for 1 s or 20 kA for 3 s |
| internal arc classification, Eaton Xiria 630 | 21 kA for 1 s | Xiria 630: IAC AFLR 21 kA for 1 s (16 kA with absorber or cable compartment). Classification LSC2, partition class PM, degree of protection IP3X in service, ambient -25 to +40 C. SF6-free: switching and insulation by vacuum |
| rated voltage, Schneider RM6 | 24 kV | Schneider RM6 facts: gas-insulated RMU up to 24 kV, standard IEC 62271-200, 50 or 60 Hz |
| busbar and switching currents, Schneider RM6 | 630 A | RM6: busbar and load-break switch 630 A; circuit breaker 200 A for transformer protection or 630 A for feeder protection; single busbar system |
| short-circuit and arc ratings, Schneider RM6 | 20-21 kA | RM6: short-circuit rated current up to 21 kA for 1 s; internal arc classification up to 20 kA AFLR with options; loss of service continuity LSC 2 A, partition class PM |
| indicative cost, 12-24 kV SF6 RMU, unit | 2000-7000 USD per unit | Export price list (accepted price basis, owner instruction 2026-11-13): compact SF6 RMUs about USD 2,000-2,700, mainstream 12-24 kV units USD 3,400-4,700, outdoor GIS RMU USD 6,000-7,100; Western-brand equipment typically 2-4x these FOB figures. Not a delivered Malaysian price. |
| TNB 11 kV motorised RMU supply contract value (benchmark, not unit price) | 113.31 MYR million | TNB Letter of Award to EPE Switchgear (60% subsidiary of Pekat Group) for 11 kV motorised RMUs with interconnectors and remote control boxes, various configurations, two-year term from 29 December 2025; RM113.31 million inclusive of SST. A multi-configuration supply contract, so it bounds rather than fixes a per-unit price. |

- **ABB** SafeRing / SafePlus: 12-36 kV RMU
- **Schneider Electric** RM6 / Premset: 11-36 kV
- **Siemens** 8DJH: 7.2-24 kV type-tested, SF6 sealed for life
- **Eaton** Xiria: 12-24 kV

Recorded gaps:

- per-panel prices from ABB/Schneider/Eaton themselves — Ask a TNB-registered Malaysian switchgear supplier (EPE Switchgear, Inteflex, others) for a per-unit benchmark

## oily-water-separator

### Oily-water separators (API/CPI) (wwt-oily-water-separators)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
Gravity oil-water separators at the head of an industrial effluent train: long baffled API-type basins designed to API 421, or corrugated/tilted plate pack (CPI/PPI) coalescers that reach smaller droplets in a smaller footprint. Skimmed oil is recovered; the oily water flows on to flotation and biological treatment.
Vendors: WesTech Engineering, Veolia, Panam Environmental Products, FRC Systems (7 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| free-oil droplet removal threshold | 150 micron | API 421 traditional separators remove droplets down to about 150 micron under ideal conditions |
| design effluent free-oil concentration | 0-100 mg/L | effluent of 100 mg/L or less of non-emulsified free oil droplets 150 micron and larger |
| CPI removable droplet size | 40-60 micron | plate separators down to about 60 micron, 40 micron in enhanced designs |
| design residence time | 45 min | 45-minute design residence; velocity capped at 0.015 m/s; length-to-width ratio at least 5:1 |

- **Panam Environmental Products** API hopper-bottom oil water separator: flow rates from 15 GPM to over 1,000+ GPM; API 421; length-to-width at least 5:1
- **Panam Environmental Products** FB flat-bottom oil water separator: flow rates from 5 to 5,000 GPM
- **Panam Environmental Products** OS coated-steel oil water separator: flow rate range 5-5,000+ GPM; targets 10 mg/L or less of oil droplets 30 micron and larger
- **Panam Environmental Products** OSE stainless-steel oil water separator: flow rates from 5 to 250,000+ GPM (as written on the vendor page); 99.99% free-oil removal, meets EPA Method 1664 and EN 858-1
- **Panam Environmental Products** OSF fibreglass oil water separator: flow rates from 5 to 50 GPM
- **Panam Environmental Products** TPI tilted plate interceptor (CPI): customised to flow rate; removes up to 99% of free-floating oil, outlet typically below 10 ppm
- **FRC Systems** Corrugated Plate Interceptor (CPI): flow capacity up to 6,000+ GPM (1,363+ m3/h); effective separation area 32-3,101 sq ft (2.97-288.1 m2); stainless 304/316/duplex

Recorded gaps:

- per-vendor model lines for WesTech and Monroe — record WesTech/Monroe project references as reference plants rather than model lines

## ozone-generators

### Ozone generators (wwt-ozone-generators)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
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
XLPE-insulated power cables from 415 V building wiring through 11/33 kV distribution to 132 kV and 275 kV transmission cables, to IEC 60502 (LV/MV) and IEC 60840/62067 (HV/EHV).
Vendors: Southern Cable Group Berhad, Universal Cable (M) Berhad, PT Supreme Cable Manufacturing & Commerce Tbk (SUCACO), PT Voksel Electric Tbk, PT Jembo Cable Company Tbk, PT Kabelindo Murni Tbk, Prysmian Group, Nexans (8 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| voltage grades covering the Malaysian system | 0.6-275 kV | 0.6/1 kV LV through 6.35/11 and 19/33 kV MV to 132-275 kV transmission grades |
| indicative cost, 19/33 kV 3-core Cu XLPE/SWA/PVC 95 mm2 | 26.5-34.0 USD per metre | FOB China price guide at LME copper about USD 9,800-10,200/t: 19/33 kV 95 mm2 3-core copper USD 26.50-34.00/m; 240 mm2 USD 60-77/m; 400 mm2 USD 96-123/m. Aluminium conductor saves roughly 40-55%. |
| indicative cost, 6.35/11 kV 3-core Cu XLPE/SWA/PVC 185 mm2 | 31.0-39.3 USD per metre | Same price guide: 11 kV 185 mm2 copper USD 31.00-39.30/m; 95 mm2 USD 17.00-21.70/m; 300 mm2 USD 47.70-61.10/m |
| indicative cost, 11 kV and 33 kV underground cable per km (tender-derived) | 8100-44000 USD per km | Indian utility tender cost data: 33 kV 1Cx630 mm2 aluminium XLPE about USD 8,100/km; 33 kV 1Cx400 mm2 copper about USD 44,000/km; 11 kV 3x185 mm2 about USD 11,000/km; 11 kV 3x300 mm2 about USD 14,500/km. Tender-derived and useful for magnitude only. |

- **Southern Cable Group Berhad** XLPE power cables (LV to HV): 300 V to 132 kV; TNB-registered Malaysian maker
- **Universal Cable (M) Berhad** XLPE power cables (MV to EHV): 6.6 kV to 275 kV, TNB specification
- **PT Supreme Cable Manufacturing & Commerce Tbk (SUCACO)** SUPREME N2XSY / NA2XSY: up to 150 kV, IEC 60502-2 / SNI / SPLN
- **PT Voksel Electric Tbk** Voksel power cables: Indonesian PLN-supplied LV-MV
- **PT Jembo Cable Company Tbk** Jembo power cables: LV-MV plus instrumentation
- **PT Kabelindo Murni Tbk** Kabelindo conductors and cables: PLN 150 kV reconductoring references
- **Prysmian Group** XLPE cables: 0.6 kV to 400 kV
- **Nexans** Power cables: LV to EHV

Recorded gaps:

- ampacity tables by installation method (IEC 60287/60364) — Record a small derated ampacity table for the common 11/33 kV sizes
- 132 kV cable prices — Ask owner for a Prysmian/Nexans EHV quote if a project needs it

## power-transformers

### Power and distribution transformers (ele-power-transformers)

Primary code: ELE: Electrical engineering
Oil-immersed and dry-type transformers stepping between the Malaysian voltage tiers: 500/275 kV and 275/132 kV grid banks, 132/33/11 kV distribution units and 11-33 kV/415 V site transformers, to MS IEC 60076 (IEC 60076 adopted).
Vendors: Malaysia Transformer Manufacturing (MTM), Hitachi Energy, Siemens Energy, GE Vernova, HD Hyundai Electric (5 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ratio tiers used in Malaysia | 0.415-500 kV | Malaysian tiers 500, 275, 132, 33, 11 kV and 415-433 V are joined by transformers; the LV secondary is 415 V nominal or 433 V rated depending on specification |
| no-load loss, 1000 kVA 11 kV/433 V Dyn11 ONAN | 1600 W | Malaysian public-sector (JKR-type) specification for 11 kV/433 V Dyn11 hermetically sealed distribution transformers: 1,000 kVA no-load loss limit 1,600 W |
| load loss, 1000 kVA 11 kV/433 V Dyn11 ONAN | 6100 W | Same Malaysian schedule: 1,000 kVA load loss limit 6,100 W (other tiers 750 kVA 5,600 W; 1,500 kVA 10,000 W; 2,000 kVA 12,000 W; 2,500 kVA 13,900 W) |
| short-circuit impedance, distribution class | 4.5-6.5 % | Typical 11 kV distribution transformer impedance range; TNB specifications commonly fall at 4.5-6% |
| distribution transformer rating | 500-2500 kVA | Typical 11-33 kV / 415-433 V distribution sizes in Malaysian schedules |
| power transformer rating | 100-700 MVA | Grid bank sizes at 275 and 500 kV |
| distribution transformer rating, Malaysia Transformer Manufacturing (MTM) | 100-3000 kVA | MTM Products page: distribution transformers 100 kVA to 3,000 kVA for voltages up to 33 kV; overall production range stated as 300 kVA at 0.433 kV up to 90 MVA at 132/33 kV |
| power transformer rating, MTM | 5-90 MVA | MTM Products page: power transformers 5 MVA to 90 MVA, supporting up to 150 kV |
| indicative cost, 1000 kVA 11 kV/0.4 kV oil-immersed transformer (export price list) | 7000-20000 USD per unit | Foreign export price list, accepted as the price basis on owner instruction 2026-11-13. Aluminium-wound standard units about USD 7,000-12,000; copper-wound low-loss IEC units USD 12,000-20,000; 33 kV class USD 10,000-20,000. Malaysian landed cost adds roughly 30-60% for duties, SST, compliance testing and local margin (about MYR 80,000-150,000 for a compliant S13-class copper unit). FOB export, not a delivered Malaysian price. |

- **Malaysia Transformer Manufacturing (MTM)** MTM distribution and power transformers: 100 kVA to 100 MVA; refurbishment to 275 kV
- **Hitachi Energy** Power and distribution transformers: distribution to UHV
- **Siemens Energy** Transformers: distribution to UHV
- **GE Vernova** Transformers: distribution to UHV
- **HD Hyundai Electric** Transformers: grid class

Recorded gaps:

- manufacturer loss tables for power transformers (275-500 kV class) — Read a manufacturer power-transformer technical guide for loss ranges by rating
- Malaysian retail prices from a local manufacturer — Ask owner for a local transformer quote benchmark, or watch ePerolehan/TNB tender award notices for a like-for-like unit price

## pressure-part

### Boiler furnace and membrane water walls (furnace-waterwalls-boiler)

Primary code: PWR: Power and renewables
Radiant heat-release enclosure around the flame. Fire-tube boilers confine the flame in a large furnace tube surrounded by water; water-tube boilers use finned membrane wall panels in which the furnace walls themselves form evaporator surface. Cooling the gas before the reversal chamber and limiting metal subcooling during cycling are central to tube life.
Vendors: Babcock & Wilcox, Cleaver-Brooks (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| flame temperature | 1800 degC | Spirax Sarco: flame temperature in shell-boiler furnace tubes may be up to 1,800 C |
| gas temperature before reversal, plain steel | 420 degC | Minimum cooling to 420 C before a plain-steel reversal chamber |
| gas temperature before reversal, alloy steel | 470 degC | Minimum cooling to 470 C before an alloy-steel reversal chamber |
| lower-furnace subcooling limit | 100 degF | B&W: if lower-furnace subcooling is limited to 100 F (56 C) there is a low probability of cycling damage |
| furnace wall construction | finned membrane wall qualitative | Spirax Sarco: water-tube boilers use finned tube membranes for furnace walls |


Recorded gaps:

- heat-flux and refractory specification for gas-fired furnaces — Read a furnace design reference or OEM specification.

### Boiler heat-transfer tubes and tube sheets (heat-transfer-tubes-boiler)

Primary code: PWR: Power and renewables
The pressure-part surface across which heat passes from gas to water. Fire-tube boilers pass gas inside furnace and smoke tubes with water outside and tube sheets separating the two; water-tube boilers pass water inside tubes with gas outside. Extended and enhanced tube forms are claimed to raise effective surface area and heat transfer.
Vendors: Cleaver-Brooks, Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| furnace tube wall thickness | 18-20 mm | 18-20 mm compromise between pressure capability and heat transfer |
| practical shell boiler pressure limit | 27 bar | About 27 bar implied by the furnace tube wall thickness |
| heat-transfer increase, CBEX extended tubes | 85 % | Cleaver-Brooks claims extended heat-transfer tubes in EX systems increase heat transfer by 85% (vendor claim) |
| effective surface area, AluFer tube | 5 x | Cleaver-Brooks claims up to five times the effective heat-transfer surface area of other condensing boilers |
| number of passes, condensing firetube | 1 passes | ClearFire-CE technical data: number of passes 1 |
| boiler horsepower heat-transfer convention | 5 sq ft/BHP | US convention after 1900: 5 sq ft per boiler horsepower |


Recorded gaps:

- tube material, fin geometry and fouling allowance for gas firing — Read a boiler tube datasheet or design standard.

### Boiler steam drum and mud drum (steam-drum-boiler)

Primary code: PWR: Power and renewables
In drum-type water-tube boilers the upper steam drum is the point of steam/water separation and feedwater introduction, while the lower mud drum collects sediment; downcomers carry cooler dense water to the lower drum and risers return the heated mixture. Drum temperature stratification during cycling drives humping and connection stress, so drum design and circulation are central to load-change capability.
Vendors: Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| drum-type boiler pressure capability | 160 bar | Spirax Sarco: water-tube boilers with steam drums handle steam up to 160 bar |
| cycling drum temperature effect | drum humping and connection stress qualitative | B&W: top-to-bottom drum temperature variations can lead to drum humping and excessive stresses on connections (qualitative) |
| outlet-header thermal shock exposure | 100-400 degF | B&W: thermal shock differentials reduced from 200-400 F to below 100 F (56 C) in improved designs |


Recorded gaps:

- drum dimensions, retention time and circulation ratio for the package lines — Read a package-boiler data sheet with drum details.

## prilling-tower

### Urea prilling tower (urea-prilling-tower)

Primary code: PCH: Petrochemicals
Tall tower in which molten urea is sprayed from the top and solidifies in falling droplets cooled by rising air, producing small round prills. Tower height and airflow set the prill size and the product's cooling and hardening; prills are smaller and more spherical than fluid-bed granules.
Vendors: Stamicarbon, Saipem, Casale, Toyo Engineering (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| tower height | 80-140 m | height varies with plant load and weather |
| large-unit capacity | 3000-very high t/d | large prilling units of at least 3,000 t/d of urea prills |
| large-unit dimensions | at least 100 high and 20 in diameter m | large prilling towers |
| prill size | 1.65 mm | typical prill diameter, compared with 2.82-3.06 mm granules |

- **Stamicarbon** Prilling Design: rotating buckets distribute liquid urea droplets evenly in the tower; optional seeding

## protection-relays

### Protection relays and substation IEDs (ele-protection-relays)

Primary code: ELE: Electrical engineering
Numerical protection relays and IEC 61850 intelligent electronic devices for overcurrent, distance, differential and transformer protection on the Malaysian grid and industrial systems, type-tested to IEC 60255.
Vendors: Schweitzer Engineering Laboratories (SEL), Siemens Energy, Hitachi Energy, GE Vernova (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| distance protection operating time, SEL-421 high-speed | 0.8 cycles | SEL-421 high-speed element: 0.8 cycle maximum operating time at 70% of reach and SIR = 1; the standard SEL-421-1 is 1.5 cycles |
| timer accuracy, SEL-421 | +/-0.125 cycle plus 0.1% of setting cycles | SEL-421 data sheet: timer accuracy plus/minus 0.125 cycle plus 0.1% of setting; event time stamping better than 10 microseconds |
| trip time, SIPROTEC 7SA513 distance | 11 ms | Siemens 7SA513 shortest command time about 11 ms; 7SA86 tripolar minimum about 9 ms; distance function type-tested to IEC 60255-151 |
| overcurrent IDMT timing tolerance, SIPROTEC | <=5% +/-15 ms % | SIPROTEC technical data: IDMT tolerance within 5% plus/minus 15 ms for 2 to 20 x pickup and 1-20 s |
| communication standard | IEC 61850 (Ed2/Ed2.1 with 9-2 process bus) standard | SIPROTEC 7SA supports IEC 61850 Ed1/Ed2.1 and IEC 61850-9-2 process bus with PTP time sync; new substations in Malaysia follow IEC 61850 |
| fault duty protection must clear at 500 kV | 50 kA | TNB 500 kV 50 kA for 1 s |
| indicative cost, single-function overcurrent relay (export price list) | 120-900 USD per unit | Export price list, accepted as the price basis on owner instruction 2026-11-13. A 2026 microprocessor-relay price guide covering 96 manufacturers and 560 SKUs puts single-function overcurrent devices at about USD 120 through Chinese OEM channels, rising with function count and brand tier. |
| indicative cost, full IEC 61850 bay-controller IED (export price list) | 4000-12000 USD per unit | Same price guide: the spread reaches USD 12,000+ for a full IEC 61850 bay controller from Schweitzer Engineering Laboratories or GE Grid Solutions. Function class, brand tier and certification drive the 30x spread the source documents. |

- **Schweitzer Engineering Laboratories (SEL)** SEL-421 / SEL-411L: subcycle to 1.5-cycle distance protection
- **Siemens Energy** SIPROTEC 5: IEC 60255-151 type-tested
- **Hitachi Energy** Relion: transmission protection
- **GE Vernova** UR (Universal Relay): transmission protection

Recorded gaps:

- delivered Malaysian pricing from a panel integrator — Ask owner for an integrator quote if a project budget needs it

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

## safety

### Boiler safety valves, blowdown and level fittings (safety-valves-blowdown-boiler)

Primary code: PWR: Power and renewables
Fittings that protect the pressure boundary and control water quality: safety valves sized to at least the boiler's 'from and at 100 C' evaporation and fully open within 110% of design pressure; continuous/TDS blowdown from the water surface; bottom blowdown to remove sediment; and independent water-level indication and gauges.
Vendors: Spirax Sarco, TLV (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| safety valve discharge capacity | at least from-and-at 100 C rating qualitative | Total discharge capacity must be at least equal to the boiler's 'from and at 100 C' evaporation rating |
| full rated discharge pressure | 110 % of design pressure | Full rated safety-valve discharge capacity within 110% of boiler design pressure |
| minimum safety valve inlet bore | 20 mm | Minimum 20 mm inlet bore |
| TDS blowdown connection | 15-20 DN mm | Boiler connection typically DN15 or DN20 |
| bottom blowdown valve size | 25-50 DN mm | Usually DN25 to DN50 key-operated valve |
| bottom blowdown pulse | 4 s per 8 h | A single four-second blowdown every eight hours is described as more effective than one long blow |
| minimum blowdown line length | 7.5 m | Spirax Sarco: a reasonable minimum is 7.5 m, used for blowdown vessel sizing |
| blowdown vessel design pressure | 25 % of MWP | At least 25% of boiler maximum working pressure, quoting HSE Guidance Note PM60 |
| blowdown vessel vent limit | 0.35 bar g | Vent sized so vessel pressure does not exceed 0.35 bar g |
| blowdown vessel overflow temperature | 43 degC | Standing water volume must keep overflow temperature at or below 43 C |
| pressure gauge dial | 150 mm | At least 150 mm diameter and Bourdon tube type |
| water level indicators | 2 count | Boilers rated 100 kW or more have at least two water level indicators |
| recommended maximum TDS | 2000-10000 ppm | Engineering ToolBox: normally 2,000-10,000 ppm depending on boiler type |


Recorded gaps:

- code-specific setting and capacity certifies for ASME Section I versus EN 12953 — Verify against ASME BPVC Section I and EN 12953 before using these as design limits.

## sludge-dewatering

### Sludge dewatering equipment (wwt-sludge-dewatering-equipment)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
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

## steam-reformer

### Steam reformer (primary and secondary) (steam-reformer)

Primary code: H2: Hydrogen and low-carbon fuels
Fired tubular reactor in which natural gas or another light hydrocarbon reacts with steam over a nickel catalyst to make synthesis gas, followed in ammonia plants by a secondary reformer where air or oxygen is added and the remaining methane is converted. Reformers set the hydrogen-to-nitrogen ratio and the methane slip for the downstream shift and synthesis sections.
Vendors: Topsoe, KBR, thyssenkrupp Uhde (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| outlet temperature | 800-900 °C | optimal SMR operating range at medium pressure |
| operating pressure | 20-30 bar | medium-pressure SMR range |
| steam-to-carbon ratio | 2.5-3.0 mol/mol | typical S/C values; the NETL design case uses 2.60 |
| secondary reformer outlet temperature | 982 °C | syngas cooled from the secondary reformer outlet in the NETL design case |

- **Topsoe** Tubular radiant wall steam reformer: more than 250 units designed over 50+ years; low steam-to-carbon, high heat flux, high outlet temperature
- **KBR** KRES (KBR Reforming Exchanger): installed in parallel with the existing SMR and secondary reformer; up to 130% of SMR capacity
- **thyssenkrupp Uhde** uhde primary reformer: catalyst tube outlet about 800 C at approximately 45 bar

Recorded gaps:

- tube wall temperature and tube-life limits — fetch an OEM reformer datasheet or a metallurgy reference that states tube skin temperature

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

## urea-reactor

### Urea reactor (urea-reactor)

Primary code: PCH: Petrochemicals
High-pressure reactor in which ammonia and carbon dioxide form ammonium carbamate and then dehydrate to urea. Conversion per pass is incomplete, so the high-pressure loop strips and recycles unconverted carbamate; reactor pressure, temperature and the ammonia-to-CO2 ratio set conversion and downstream stripping duty.
Vendors: Stamicarbon, thyssenkrupp Uhde, Casale, Toyo Engineering, Saipem (5 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| operating pressure | 150 bar | Saipem urea flowsheet, NH3-stripping process |
| reactor outlet temperature | 188 °C | Saipem urea flowsheet, NH3-stripping process |
| NH3/CO2 (N/C) ratio | 3.2-3.4 mol/mol | Snamprogetti process; patents quote 2.5-3.5 with 3.0-3.2 preferred |
| CO2 conversion per pass | 62-64 % | share of CO2 entering the reactor converted to urea; the high-pressure loop reaches 85-90% overall |

- **Stamicarbon** LAUNCH MELT pool reactor design: suited to capacities up to about 2,500 mtpd; about 30 m plant height
- **Toyo Engineering** ACES21 process: reactor at N/C 3.7, 182 C and 152 bar
- **Toyo Engineering** ACES21-LP process: synthesis pressure lowered to 136 barG; 5-10% lighter synthesis equipment
- **Casale** HYPER-U: combined condenser/reactor; optimally designed up to 4,000 MTD
- **Saipem** Snamprogetti ammonia stripping urea process: synthesis conditions 188 C and 155 kg/cm2

## uv-reactors

### UV disinfection reactors (wwt-uv-reactors)

Primary code: WWT: Wastewater treatment / Effluent treatment (WWT/ETS)
Closed-vessel or open-channel UV systems (low-pressure, medium-pressure, LED) delivering 20-100 mJ/cm2 with validated dose monitoring.
Vendors: Trojan Technologies, Xylem (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| delivered dose | 20-100 mJ/cm2 | published municipal range |

- **Trojan Technologies** UVSwift/UltraFlow: municipal open-channel and closed-vessel

Recorded gaps:

- per-model lamp counts and flows — Read Trojan/UVDI model pages

## valve-train

### Boiler fuel gas train (double block and bleed) (gas-valve-train)

Primary code: PWR: Power and renewables
Pre-assembled piping that conditions and safely isolates gaseous fuel before the burner: regulator, main shutoff valves, vent, pressure switches and manual isolation. Cleaver-Brooks lists natural gas, refinery gas, hydrogen, landfill, digester and tail gas; trains are designed to NFPA 85, FM, CSA B149.3 and ASME B31.1/B31.3 with SIL and hazardous-area options.
Vendors: Cleaver-Brooks, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fuels handled | multiple gaseous fuels qualitative | Natural gas, refinery gas, hydrogen, landfill gas, digester gas and tail gas |
| design codes | NFPA 85 / FM / CSA B149.3 / ASME B31.1 or B31.3 qualitative | NFPA 85, FM, CSA B149.3, ASME B31.1 or B31.3; SIL and hazardous-location designs offered |
| main shutoff arrangement | dual block main shutoff with ventless regulator qualitative | Zeeco PLN/GO standard equipment: ventless regulator, ventless dual block main gas shutoff valves, high/low pressure switches and two manual gas valves |
| pilot train components | regulator + solenoid + manual valve qualitative | Pilot train has its own regulator, solenoid valve and manual valve |


Recorded gaps:

- explicit vent arrangement and valve proof-of-closure details — Read a fuel-train P&ID from an OEM or NFPA 85 primary text.
- gas booster/compressor sizing for low supply pressure — Find a gas-pressure and booster selection reference.
