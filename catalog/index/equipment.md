# Equipment catalog

430 equipment records (one per equipment class, schema `schema/equipment.schema.json`).
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

## ammonia

### Ammonia condensation/refrigeration, flash vessels, let-down and storage tanks (ammonia-refrigeration-storage)

Primary code: PCH: Petrochemicals
Ammonia condensation/refrigeration, flash vessels, let-down and storage tanks | Refrigeration / cold condensation for ammonia synthesis loop | Tank farms / ammonia storage
Vendors: SPG Steiner GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ammonia normal boiling point | -33.34 deg C at 1 atm | Ammonia properties infobox/text |
| Ammonia critical point | 132.4 deg C | Critical temperature; critical pressure 111.3 atm (11,280 kPa) |
| Pressurised ammonia storage vessel design pressure | 250 psi (1.7 MPa) | A storage vessel capable of 250 psi is suitable to contain liquid anhydrous ammonia |
| Water content to avoid carbon-steel corrosion | 0.2 wt% minimum in ammonia | Ammonia with at least 0.2 wt% water is not corrosive to carbon steel; such tanks can last >50 years |
| Ammonia separation temperature from recycle gas | -20 deg C | Resulting ammonia must be separated from residual H2/N2 at about -20 deg C |
| Ammonia explosive limits in air | 15.0-33.6 vol% | Ammonia hazards infobox |
| Global ammonia shipped annually | 18-20 Mt/year | Industrial ammonia transported by road, rail, sea and pipeline (CRS figure cited) |
| Ammonia separation temperature | -20 degC | Resulting ammonia must be separated from residual hydrogen and nitrogen at -20 C |
| Refrigeration working fluids | ammonia, nitrogen and carbon dioxide list | In some situations ammonia, nitrogen and CO2 are used as refrigeration working fluids |
| Refrigeration utility selection (design study) | utility matching inlet/outlet temperature range for -43.3 C qualitative | UBC ammonia plant design report section 4.2 Selecting a utility |
| Cryogenic ammonia tank capacity (planned project) | 40000 tonnes each | SPG Steiner BEDP for two 40,000-tonne cryogenic ammonia tanks at Allied Green Ammonia, Gove (July 2024) |
| Detection applications in tank farms | compressor rooms, pump bays, valves, dike walls, access points list | MSA technical guide lists tank farms/transfer skids for ultrasonic, catalytic bead and electrochemical detectors |
| Clean syngas consumption per tonne ammonia | 2650 Nm3/t NH3 (equivalent to less than 2000 Nm3 H2) | Value as printed in the cited source; no further qualifier stated. |
| Reaction heat recovery per tonne ammonia | 600000 Kcal/t NH3 (more than) | Value as printed in the cited source; no further qualifier stated. |
| Plant turndown | 10-100 % | Value as printed in the cited source; no further qualifier stated. |
| Ramp-up/down rate | ?-3 %/min | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Named storage tank vendors, tank capacities, refrigeration package duty and flash/let-down vessel design — Fetch authoritative pages on ammonia storage tanks (e.g. API/EFMA guidance or a tank OEM).
- Named storage tank vendors, tank capacities, refrigeration package duty and flash/let-down vessel design — Fetch authoritative pages on ammonia storage tanks (e.g. API/EFMA guidance or a tank OEM).

### Ammonia feed pumps (urea-ammonia-feed-pumps)

Primary code: PCH: Petrochemicals
Ammonia feed pumps
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ammonia feed physical state | liquid n/a | Wikipedia Urea: 'the ammonia is available from the ammonia production plant in liquid form, which can be pumped into the system much more economically' (vs compressing CO2 gas) |


Recorded gaps:

- Ammonia feed pump flow, discharge pressure, NPSH, materials, vendor/model — Fetch a pump OEM datasheet or an EPC urea plant equipment list.
- Ammonia feed pump flow, discharge pressure, NPSH, materials, vendor/model — Fetch a pump OEM datasheet or an EPC urea plant equipment list.

### Ammonia plant control system, analysers and safety systems (ammonia-control-safety-systems)

Primary code: PCH: Petrochemicals
Ammonia plant control system, analysers and safety systems | Instrumentation and control rooms
Vendors: Topsoe, Casale, thyssenkrupp Industrial Solutions (Uhde), Howden (a Chart Industries company; KK&K, CKD brands), Yokogawa Electric, Aramis Group (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Uhde dual-pressure compressor size comparison | syngas compressor for 3300 t/day dual-pressure plant same size as conventional 2200 t/day plant qualitative | thyssenkrupp Uhde two-pressure process, indicating lower equipment stress through cooled HP casing |
| Casale FlexAMMONIA plant turndown | 10-100 % of load | Green ammonia synthesis loop performance claim |
| Casale FlexAMMONIA ramp rate | ?-3 %/min | Green ammonia synthesis loop ramp-up/down rate |
| PASB Kerteh OTS control systems | Yokogawa CS3000 emulation system | Aramis provided PASB OTS on INDISS platform with Yokogawa CS3000 emulation; gas plants used Honeywell PKS Experion and Foxboro I/A |
| Natural gas to ammonia process control example | steam flow control with control valve CV-101 and emergency shutdown valve control scheme | UBC design report describes feed preheat exchanger E-101 heated by high-temperature steam with control valve and emergency shutdown valve |


Recorded gaps:

- DCS/PLC vendor names, analyser types (H2, CO, CO2, NH3, moisture) and SIL-rated SIS architecture — Fetch Honeywell/Yokogawa/Emerson/Siemens ammonia or process-safety pages and AIChE ammonia safety material.
- DCS/PLC vendor names, analyser types (H2, CO, CO2, NH3, moisture) and SIL-rated SIS architecture — Fetch Honeywell/Yokogawa/Emerson/Siemens ammonia or process-safety pages and AIChE ammonia safety material.

## ammonia-converter

### Ammonia synthesis converter (ammonia-synthesis-converter)

Primary code: H2: Hydrogen and low-carbon fuels
Catalytic reactor in the Haber-Bosch loop where hydrogen and nitrogen combine over an iron catalyst to form ammonia. Conversion per pass is limited by equilibrium, so the loop circulates unreacted gas, condenses ammonia by refrigeration and returns the remainder to the converter.
Vendors: Topsoe, thyssenkrupp Uhde, KBR, Casale, thyssenkrupp Industrial Solutions (Uhde), Howden (a Chart Industries company; KK&K, CKD brands) (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| operating pressure | 150-200 bar | typical ammonia synthesis pressure as stated |
| reactor temperature | 380-520 °C | NH3 synthesis reactor operating temperature |
| single-train capacity | small-3500 t/d | large single-train ammonia converters up to 3,500 MTPD; Uhde quotes 3,300 mtpd and more |
| conversion per pass | 15 % | about 15% of the gas turns into ammonia on each pass |
| Ammonia synthesis loop operating pressure (general) | 60-180 bar | Synthesis loop pressure range depending on method (Haber process page) |
| Typical modern synthesis pressure | 150-200 bar | Plants built 1964-1992: syngas manufacture 25-35 bar, ammonia synthesis 150-200 bar |
| M.W. Kellogg Texas City syngas centrifugal compression | 152 bar | Four-case centrifugal compressor compressed syngas to 152 bar; reciprocating compressor gave final 324 bar operating pressure |
| Uhde two-pressure process: LP once-through converter suction pressure | 110 bar (approx.) | Suction flange of LP casing of syngas compressor, 3-bed intercooled once-through converter makes about 1/3 of total ammonia |
| Uhde two-pressure process: HP synthesis loop pressure | ?-210 bar | Remaining syngas compressed in HP casing to loop operating pressure up to 210 bar; makes remaining 2/3 of ammonia |
| Ammonia condensed from once-through converter effluent | 85 % of ammonia produced in that converter | Mixture leaving the once-through converter is cooled; 85% of ammonia made there separated as liquid |
| Single-pass conversion per reactor pass | 15 % | About 15% conversion per pass; overall conversion ~97-98% with recycle |
| Synthesis temperature range | 300-500 deg C | Ammonia synthesis loop temperature range |
| Howden reciprocating gas compressor ratings | ?-20 MW | Howden/Peter Brotherhood reciprocating gas compressors rated to 20 MW, 260-1000 rpm |
| Howden steam turbine mechanical-drive range | 10-40 MW | Steam turbines as mechanical drive for rotating equipment such as pumps, compressors and fans |
| Plant applications | 110-? plants designed/engineered/commissioned | TOYO states >110 urea plants using its technologies |
| Selected capacity | 1.15 million t/y urea | Fakfak, West Papua urea plant BED selection, Nov 2026 |
| Detection range | 17-28 m | Typical range depends on microphone technology |
| Minimum pressurised installation | 2 bar | Only suitable for pressurised installations from 2 bar (29 psi) or more |
| Reference plant capacity | 1200 MTD (coal-based ammonia) | Value as printed in the cited source; no further qualifier stated. |
| Achieved capacity shortly after start-up | 110 % of nameplate | Value as printed in the cited source; no further qualifier stated. |
| Stable extended operation | 130 % load | Value as printed in the cited source; no further qualifier stated. |
| Tank capacity | 40000 tonnes each | July 2024 BEDP contract for two cryogenic ammonia tanks, Gove |
| Quantity | 2 tanks | CSIRO HyResource project entry |
| Scope | process licence and ammonia plant engineering scope | Allied Green Ammonia May 2024 entry; Oct 2023 first Australian green ammonia contract |
| Project capacity linked | 958500 t/y ammonia | Allied Green Ammonia project design capacity |
| Steam-to-carbon ratio | 0.6 mol/mol | Value as printed in the cited source; no further qualifier stated. |

- **Topsoe** S-200 ammonia converter basket: two-bed radial flow with indirect cooling between beds; more than 130 units since 1976
- **Topsoe** S-300 ammonia converter basket: three-bed radial flow; higher conversion and production efficiency than S-200; more than 50 installations
- **KBR** KBR ammonia converter: vertical converters below 2,000 MTPD; horizontal units up to 6,000 MTPD; add-on bed gives 21-24% conversion
- **thyssenkrupp Uhde** uhde ammonia converter A30/A20 series: three radial catalyst beds in one or two converters; loop up to 210 bar; A30 4,000-5,000 mtpd

Recorded gaps:

- per-vendor converter model lines with casing, catalyst basket and pressure-drop data — fetch Topsoe S-200/S-300, KBR, Casale and Uhde converter pages and add model lines
- Refrigeration compressor OEM/model data for ammonia service and circulator sizing rules — Locate working OEM URLs for process-gas compressors and ammonia refrigeration packages.
- Refrigeration compressor OEM/model data for ammonia service and circulator sizing rules — Locate working OEM URLs for process-gas compressors and ammonia refrigeration packages.

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

## architecture

### Data-centre power architecture and tier/redundancy (data-centre-power-architecture)

Primary code: IDC: Data centres
Data-centre power architecture and tier/redundancy (N, N+1, 2N, distributed redundancy) | Standards and guidance for data-centre standby/prime generation | Data-centre power integration (gas-engine off-grid / BTM microgrid)
Vendors: Schneider Electric, Vertiv, Eaton, Caterpillar, Schneider Electric, INNIO Jenbacher (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Tier I-IV definitions | Tier I basic UPS + engine generator; Tier II redundant capacity components; Tier III concurrently maintainable with redundant distribution paths; Tier IV fault tolerant with multiple independent, physically isolated systems classification | Uptime Institute Tier Classification System; Tiers progressive; Tier definitions set in the Tier Standard: Topology; 4300+ certifications issued in 120+ countries |
| EPA emergency-engine non-emergency hours | 50 h/year | EPA Clean Air Act Resources for Data Centers: certain emergency engines may operate 50 hours/year in non-emergency situations under 40 CFR 63.6640(f)(3)-(4), 60.4211(f)(3), 60.4243(d)(3) |
| EPA default assumption for emergency-generator potential to emit | 500 h/year | EPA page quoting 1995 PTE guidance: '500 hours is an appropriate default assumption for estimating the number of hours that an emergency generator could be expected to operate under worst-case conditions'; alternatives case-by-case |
| Applicable US emission rules for data-centre engines | 40 CFR part 60 subparts IIII (stationary compression-ignition) and JJJJ (stationary spark-ignition); 40 CFR part 63 subpart ZZZZ (RICE NESHAP); 40 CFR part 60 subpart TTTT (GHG for electric generating units); NSPS for stationary gas/combustion turbines regulation set | EPA Clean Air Act Resources for Data Centers page |
| 2026 DOE 202(c) emergency orders effect on engine hours | Operation under these emergency orders does not count toward the 50 h non-emergency allowance regulatory interpretation | EPA alert: spring/summer 2026 DOE orders directing RTOs to require data centres/large loads to run backup generation as last resort before Energy Emergency Alert Level 3 |
| Uptime Tier certification scale | Over 4,300 Tier Certifications issued in 120+ countries count | Uptime Institute Tier Classification System page |
| Study availability target | 99.999% (about five minutes downtime per year); avoided event = loss of power to IT servers for more than 20 ms % / minutes / ms | Schneider Electric White Paper 286, electrical design section |
| Engine plant start / load acceptance (10 MW medium-speed gas engine) | start, synchronise and reach nominal speed within 15 s; additional 35 s to support site full load; steps of about 20% of nominal output seconds / % | Schneider Electric White Paper 286, 'Gas engine attributes important for large data centre applications' and Figure 4 start-up curves |
| Example 10 MW-class plant configuration | 9 gas generator units (7+2 redundancy), four data-centre buildings at 17.5 MW each, 15 kV MV switchgear, 18 MVA grid backup for Block 1 only units / MW / kV / MVA | Schneider Electric White Paper 286, electrical distribution architecture and Figure 7 |
| Data-centre cooling share / CCHP efficiency claim | cooling usually accounts for up to 40% of a data centre's energy requirements; Jenbacher CCHP electrical + thermal efficiency up to 95%; pipeline-gas CCHP can cut DC CO2 footprint by up to 50% depending on energy mix and save >20% primary energy % | INNIO Jenbacher Data Centers industry page (vendor claims) |
| Wärtsilä DC plant scale / deployment claim | power plants of 10-23 MW engines can provide over 450 MW; large-scale plants operational 12 months after manufacturing completion; CAPEX stated 20-30% lower including primary + reserve capacity MW / months / % | Wärtsilä Data center power solutions page (vendor claims) |


Recorded gaps:

- No independently published, non-vendor comparison of 2N vs distributed-redundancy availability for gas-engine-fed (rather than diesel-fed) data centres — Search Uptime Institute journal / IEEE/IET literature for measured availability of BTM gas-engine data-centre power architectures
- Short-circuit ratings for a gas-engine plant bus tied into an existing data-centre 2N topology — Obtain site-specific fault study; no generic figure accepted
- ASHRAE-specific guidance for data-centre standby/prime generation — Fetch ASHRAE datacom series / ANSI-ASHRAE 9.9 or ASHRAE Journal articles on on-site generation and note exact document titles and dates
- IEEE standards specific to data-centre genset integration (e.g. IEEE 446, IEEE 1100) exact editions and clauses — Fetch IEEE Xplore standards pages and record designation, year and scope
- Malaysia/Singapore national equivalents of NFPA 110 / emissions limits for prime gas engines at data centres — Fetch DOE Malaysia, EMA Singapore and local environmental department guidance

## bagging

### Bagging machines and big-bag (bulk-bagging-fibc-filling)

Primary code: PCH: Petrochemicals
Bagging machines and big-bag (FIBC) filling
Vendors: Bühler (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Bagging machines and big-bag (FIBC) filling | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Bagging rate (bags/h), bag sizes, weighing accuracy, dust extraction flow, OEM models and prices — Fetch a packaging OEM page (BEUMER, Bühler, Cronos, TAGMAS) via verified URL.
- Bagging rate (bags/h), bag sizes, weighing accuracy, dust extraction flow, OEM models and prices — Fetch a packaging OEM page (BEUMER, Bühler, Cronos, TAGMAS) via verified URL.

## belt

### Belt conveyors (bulk-belt-conveyors)

Primary code: PCH: Petrochemicals
Belt conveyors (incl. chevron/cleated and elevator belts)
Vendors: Sandvik, Intralox, AUMUND France / Larsen & Toubro / ABB (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| pipe conveyor maximum incline | 35 degrees | Wikipedia Conveyor belt: pipe conveyor for material paths requiring sharper bends and inclines up to 35 degrees |
| sandwich belt maximum incline | 90 degrees | Wikipedia Conveyor belt: sandwich belt design enables travel along high inclines up to 90-degree angles |
| highest steel-cord belt strength class | 10000 N/mm | Wikipedia: highest strength class conveyor belt installed, steel cord, at Chuquicamata mine, Chile |
| aramid belt strength range | 630-3500 N/mm | Wikipedia: aramid used in range 630-3500 N/mm; advantages energy savings, enhanced lifetimes, improved productivity |
| aramid belt example | 2250 N/mm, 3400 m long, >15% energy savings n/a | Wikipedia: underground belt at Baodian Coal Mine, Yanzhou Coal Mining Company, China |
| longest single-span conveyor | 31 km | Wikipedia: Boddington bauxite mine Western Australia, cable belt conveyor feeding a 20 km conveyor (world's longest single flight) |
| impumelelo conveyor capacity | 2400 t/h | Wikipedia: 26.8 km trough belt near Secunda, South Africa, transporting coal to a refinery |
| India-Bangladesh cross-border conveyor | 17 km, 960 t/h, 1.8 MW n/a | Wikipedia: limestone/shale conveyor from Meghalaya, India to cement factory at Chhatak, Bangladesh; engineered by AUMUND France and Larsen & Toubro; drives by ABB |
| belt scale / weigher | material flowing over belt may be weighed in transit using a beltweigher n/a | Wikipedia Conveyor belt applications |
| belt components | drive pulley, idler pulley, reducer gearboxes, motors, couplings, scrapers, chutes, skirts, take-up assembly, safety switches n/a | Wikipedia Conveyor belt structure/applications |
| conveyor safety devices | trip cords, belt sway switches, speed switches, belt rip switches, emergency stops; OSHA 1926.555 n/a | Wikipedia Conveyor belt safety system section |


Recorded gaps:

- Urea-specific belt conveyor capacity (t/h), belt width, speed, chevron/cleated belt profile dimensions and OEM model numbers — Retry with verified OEM URLs (Continental, Fenner Dunlop, Goodyear, BEUMER, Metso, FLSmidth) obtained from a working search integration.
- Urea-specific belt conveyor capacity (t/h), belt width, speed, chevron/cleated belt profile dimensions and OEM model numbers — Retry with verified OEM URLs (Continental, Fenner Dunlop, Goodyear, BEUMER, Metso, FLSmidth) obtained from a working search integration.

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
| CFB technology name | PowerFluid product/technology name | Thermal power page, 'CFB TECHNOLOGY - PowerFluid': flue gas velocity higher, bed expanded and entrained, material separated by cyclones and returned to lower furnace |
| Emissions mechanism | Low emissions of CO, hydrocarbons and nitric oxides qualitative | Thermal power page: efficient mixing and relatively low combustion temperatures contribute to low emissions |
| Fuel range | Biomass, demolition wood, RDF, SRF, peat, various sludges, waste fuel options | Thermal power page |
| Related BFB technology | EcoFluid product/technology name | Thermal power page BFB TECHNOLOGY - EcoFluid section |
| Boiler size range | 30-1200 MWth | Product page: 'The wide size range covers boilers from 30 to 1200 MWth' |
| Cyclone construction | High-efficiency cylindrical cyclones of membrane walls covered by light refractory construction | Product page 'High steam parameters' section; no hot expansion joints between furnace and cyclone |
| Steam parameters | High steam parameters without severe corrosion qualitative | Product page: enabled by fluidized bed heat exchangers located in the loop seal; dedicated superheaters for corrosive fuels |
| Low-load operation | Partial bed operation available operating mode | Product page section 'Low-load operation available for CFB boilers' |
| Fuels | Biomass, agricultural waste streams, recovered fuels, coals, solid petrochemical residues (pet coke, asphaltene, solidified pitch), any combination fuel flexibility | Product page 'High fuel flexibility'; more than 100 references worldwide, mostly multifuel boilers |


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
| Input capacity | 500-6000 MBH (11 models) | Product bullets: 11 models from 500 MBH to 6,000 MBH; Technical Data table 500-6,000 |
| AHRI combustion efficiency | 94.7 % | Technical Data table |
| AHRI thermal efficiency | 96 % | Technical Data table; narrative states up to 99% efficient |
| Design temperature | 210 deg F | Technical Data table |
| NOx emissions | 7-20 ppm NOx | Bullet 'Standard less than 20 ppm NOx, sub 7 ppm NOx available'; table <20 ppm standard, lower emission optional |
| Turndown | 10 :1 fully modulating | Product bullet and narrative |
| Sound level | 70 dBA at 3 feet (less than) | Product Overview attribute list |
| Heat exchanger construction | Duplex stainless steel; TurboFer/AluFer tubes material | Product Overview; AluFer tube technology increases effective heat transfer surface up to five times and thermal conductivity ten times greater than stainless steel alone |
| Hydrogen readiness | 20 % volumetric hydrogen-natural gas blend | Product narrative: supports RNG and up to 20% volumetric mix hydrogen-natural gas blends |
| Input capacity | 399000-6000000 BTU/hr | Product page Size Range: 399,000-6,000,000 BTU/HR; model table EXE-399 to EXE-6000 MBH |
| Thermal efficiency | 96.2-98.0 % AHRI Thermal Efficiency | Specifications & Dimensions table, model-by-model values 96.2-98.0%; page headline 'Efficiency up to 99%' |
| Turndown ratio | 8-15 :1 | Specifications table by model (8:1 EXE-399, 10:1 EXE-500, 13:1 EXE-650, 15:1 EXE-750 through EXE-3000 etc.) |

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
| Input capacity | 2000-6000 MBH | Product bullet 2,000-6,000 MBH Input; Technical Data table 2,000-6,000 |
| Design pressure (steam) | 15-500 psig | Product bullet: 15-500 psig Design Pressure (Steam) |
| Design pressure (hot water) | 160-250 psig | Product bullet: 160-250 psig Design Pressure (Hot Water) |
| Boiler horsepower | 48-143 HP | Technical Data table |
| NOx emissions | 20 ppm NOx (less than; standard, without FGR) | Product bullet 'Standard sub-20 ppm NOx'; narrative <20 ppm NOx without FGR and <10 CO as standard on natural gas |
| Turndown | 5 :1 (up to) | Product Overview attribute list; linkageless premix burner |
| Design temperature options | 235, 340, 355, 380, 410 deg F | Technical Data table |
| Input capacity | 1500-25000 MBH | Product bullet 1,500-25,000 MBH Input; Technical Data table 1,500-25,000 |
| Design pressure | 15-250 psig | Product bullet: 15-250 psig Design Pressure |
| Boiler horsepower | 36-600 HP | Technical Data table |
| Thermal efficiency | 81-85 % | Product narrative: efficiency ratings up to 81% (steam) and 85% (hot water); 5-pass bent water-tube design |
| NOx emissions | 9 ppm NOx (option, less than) | Product bullet 'Available to <9 ppm NOx'; table lists Standard, <30, <20, <9 |

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
| Steam design pressure | 300 psig | Product page bullet: 'Steam up to 300 psig', CBEX firetube boiler |
| Hot water design pressure | 125 psig | Product page bullet: 'Hot water up to 125 psig' |
| Boiler horsepower range | 100-2500 HP | Technical Data table: 100-2,500 (CBEX-2W), 250-800 (CBEX-2D), 250-800 (CBEX-3W) |
| Input capacity | 4000-102000 MBH (per Technical Data table label 'Input Capacity') | Technical Data table; page prints 4,000-102,000 without unit, MBH inferred from same manufacturer's M5M/FLX tables that label input capacity in MBH |
| NOx emissions | 5-9 ppm NOx at 3% O2 | Bullet: 30 ppm NOx with 3% O2 across 10:1 turndown; sub 5 ppm NOx without SCR on most models. Table: <5 (CBEX-2W 250-1200), <9 (CBEX-2D 250-800), <9 (CBEX-2W 100-2500), <9 (CBEX-3W 250-800) |
| CO emissions | 10 ppm (meets 10 ppm CO requirement) | Product page bullet; narrative also states <10 ppm CO without SCR |
| Turndown | 10 :1 | Product page bullet: '30 ppm NOx with 3% O2 across the 10:1 turndown range'; 3-pass model offers integral pre-piped feedwater economizer |
| Number of passes | 2 or 3 passes | Product page: 2 Pass and 3 Pass; waterback or dryback design |
| Heat transfer enhancement | 85 % increase in heat transfer | Product Overview: extended heat transfer tubes using CFD to optimize tube geometry and increase heat transfer by 85% |
| Boiler horsepower | 50-800 HP | Product page bullet and Technical Data table |
| Steam design pressure | 300 psig | Product page bullet: 'Steam up to 300 psig' |
| Hot water design pressure | 125 psig | Product page bullet: 'Hot water up to 125 psig' |

- **Cleaver-Brooks** CBEX: 100-2,500 HP, 2/3-pass, extended heat-transfer tubes
- **Cleaver-Brooks** CBLE: 50-800 HP, 4-pass, NOx options to 5 ppm

Recorded gaps:

- turndown and part-load efficiency curves for the main gas fire-tube lines — Read distributor specification sheets for turndown data.

### Heat recovery steam generator (HRSG) (boiler-hrsg)

Primary code: PWR: Power and renewables
Boiler fired by hot combustion-turbine or furnace exhaust gas rather than by burners, raised in horizontal or vertical panels behind a gas turbine with one or more drum pressures and optionally reheat. Converts a gas turbine into a combined-cycle or cogeneration plant and is the deciding component for how much of the turbine exhaust energy becomes steam.
Vendors: Babcock & Wilcox, Cleaver-Brooks, Doosan Enerbility, IHI Corporation, Sumitomo SHI FW, GE Vernova, John Zink (Koch Engineered Solutions), Tetra Engineering Group, Entech Products Corp (6 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| steam-cycle efficiency by HRSG configuration | 20-30 % | about 20% for two-pressure without reheat, 26% for three-pressure, about 30% for three-pressure with reheat |
| installed HRSG fleet, GE Vernova | 1300 units | OEM statement: more than 1,300 HRSGs installed worldwide |
| once-through HRSG operating experience | 2.5 million hours | OEM statement: over 2.5 million operating hours for once-through HRSG technology |
| US combined-cycle capacity with duct burners | 208 GW | About 208 GW of 278 GW US combined-cycle fleet has duct burners, EIA-860/EIA-923, June 2022 |
| HRSG component scope | pressure parts and catalyst housings qualitative | B&W supplies HARPs, superheaters, reheaters, economisers, finned tubing, headers, casing, inlet ducting, HP/IP/LP drums and SCR/CO catalyst housings |
| Gas turbine range | 25-60 MW | Product bullet 25-60 MW gas turbine-generators; Technical Data 'Gas Turbine Size 25 MW-60 MW' |
| Turbine exhaust gas flow | 500000-1000000 lb/hr | Product bullets and narrative |
| Steam generation | 500000 lb/hr (500,000+) | Product bullet: Steam generation to 500,000+ lbs/hr |
| Design pressure | 1800 psig (up to) | Product bullet and narrative |
| Superheater outlet temperature | 1050 deg F | Product bullet and Technical Data table |
| NOx with SCR | 2 ppm NOx (less than, available) | Product bullet |
| Construction | Vertical tube natural circulation with steam drum; field erected; single or multiple pressure levels construction | Product bullets, Technical Data table and narrative |
| Exhaust gas flow | 1000000 lb/hr (up to) | Product bullet and Technical Data table 'Exhaust Gas Flows (lb/hr) Up to 1,000,000' |
| Steam generation | 10000-500000 lb/hr | Product bullet 10,000-500,000 lb/hr; Technical Data 'Steam Flows Up to 500,000' |
| Design pressure | 1800 psig (up to) | Product bullet: Design pressure up to 1,800 psig |
| Steam temperature | 1050 deg F (up to) | Product bullet and Technical Data table |
| Duct firing temperature | 2800 deg F (up to) | Technical Data table; membrane/water-cooled furnace allows firing up to 2800 F without high-maintenance refractory |

- **Babcock & Wilcox** HRSG systems, upgrades and components: reliable HRSG systems plus upgrades and replacement components — HARPs (high pressure evaporators), headers, finned tubing and other pressure parts — suitable for a wide range of combustion turbine applications
- **Cleaver-Brooks** packaged HRSG for small turbines: state-of-the-art customized packaged heat-recovery steam generators for gas-fired turbines from 1 to 60 MW
- **GE Vernova** Horizontal drum / horizontal once-through / vertical drum HRSG: supplementary firing, SCR/CO catalysts, bypass and modular construction; 1,300+ installed (OEM statement)
- **John Zink (Koch Engineered Solutions)** HRSG duct burners: LDRW, VC and Coen-casting flame holders with igniters and flame scanners
- **GE Vernova** Horizontal drum / horizontal once-through / vertical drum HRSG: supplementary firing, SCR/CO catalysts, bypass and modular construction; 1,300+ installed (OEM statement)
- **John Zink (Koch Engineered Solutions)** HRSG duct burners: LDRW, VC and Coen-casting flame holders with igniters and flame scanners

Recorded gaps:

- OEM HRSG specification ranges (steam pressures, temperatures, supplemental firing) for major suppliers — read Mitsubishi Power and B&W HRSG detail pages in the next equipment sweep

### Industrial water-tube package boiler (boiler-industrial-watertube-package)

Primary code: PWR: Power and renewables
Shop-assembled watertube boiler (steam and lower drum above a water-cooled membrane furnace) custom-engineered per project, with D-type and O-type two-drum layouts. The standard steam generator above the fire-tube class for refineries, petrochemical plants and industrial power, firing liquid or gaseous fuels including refinery byproduct gases.
Vendors: Babcock & Wilcox, John Zink (Koch Engineered Solutions) (2 model lines recorded).

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
- **John Zink (Koch Engineered Solutions)** Coen burners paired with B&W packages: B&W packages boilers with JZHC Coen burners under an agreement between the two companies; Coen burners installed in more than 15,000 plants

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

## boilers

### Boilers and steam system (utility-steam-system)

Primary code: PCH: Petrochemicals
Boilers and steam system (HP/MP/LP, waste-heat and package boilers)
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| HP steam pressure | 40 bar | Typical site HP steam about 40 bar, condensing temperature 250 C |
| MP steam pressure | 20 bar | Typical MP main about 20 bar, condensing temperature 212 C |
| LP steam pressure | 3 bar | Typical LP main about 3 bar, condensing at 134 C |
| Cogeneration overall thermal efficiency | 70-80 % | Overall thermal efficiency of gas-turbine cogeneration with HRSG can be in the range 70-80% |
| Boiler types in Pusri cradle-to-gate boundary | package boiler; waste heat boiler; coal boiler list | PT Pupuk Sriwidjaja Palembang urea EPD utilities |


## bucket

### Bucket elevators (bulk-bucket-elevators)

Primary code: PCH: Petrochemicals
Bucket elevators
Vendors: Bühler (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| continuous discharge speed | 6 m/s (20 ft/s) | Wikipedia Bucket elevator: continuous discharge elevator uses speed around 6 m/s to achieve required centrifugal force |
| construction | buckets, belt carrying buckets and transmitting pull, drive, loading/discharge accessories, belt tensioning, enclosure n/a | Wikipedia Bucket elevator component list |
| materials handled | grain or fertilizer (explicitly named) n/a | Wikipedia Bucket elevator lead: mechanism for hauling flowable bulk materials, most often grain or fertilizer |


Recorded gaps:

- Elevator capacity (t/h), lift height, bucket size/spacing, belt speed range, drive power, OEM models — Fetch a verified bucket elevator OEM page (Bühler, BEUMER, AUMUND, 4B Elevator Components).
- Elevator capacity (t/h), lift height, bucket size/spacing, belt speed range, drive power, OEM models — Fetch a verified bucket elevator OEM page (Bühler, BEUMER, AUMUND, 4B Elevator Components).

## burner

### HRSG duct burner (supplementary gas firing) (duct-burner-hrsg)

Primary code: PWR: Power and renewables
Burner installed in the gas-turbine exhaust duct to burn additional natural gas in the remaining oxygen and raise steam output. Two main forms are standard round gas burners and linear grid burners spanning the duct. Installed in the transition duct before the lead tube bank or between superheater stages, with flame holders, pilots, igniters and flame scanners.
Vendors: John Zink (Koch Engineered Solutions), Cleaver-Brooks, Entech Products Corp (3 model lines recorded).

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
| Flame holder models | LDRW (Low Draft Reverse Wing), VC (V-Cone Tip Wing), Coen Castings model designations | Product page 'Model Options' section with descriptions of each |
| Application | HRSG supplementary firing, combined cycle, dual cycle, cogeneration application | Product page Overview and Features |
| Hydrogen readiness | Hydrogen and alternative fuels fuel capability | Product page Feature: 'Hydrogen-Ready Capabilities' |
| Integrated equipment | Proprietary igniters, flame scanners, optional instrumentation packages scope of supply | Product page Features |
| Support design | Self-supporting; eliminates internal fixed structural support design feature | Power Burners page teg+ section: reduces installation time and material costs |
| Flame stabilizer | Optimized drilled wing orifice pattern producing short, compact flame design feature | Power Burners page teg+ section; nozzle design uses pilot flame propagation drilling and varying orifice sizes |
| Application | HRSG and Turbine Exhaust Gas (TEG) supplementary firing application | Power Burners page Duct burners and teg+ sections |

- **John Zink (Koch Engineered Solutions)** ProLine in-line duct burner: 0.03 lb/MMBtu NOx and CO, to 5 MMBtu/hr/ft, 20:1 turndown
- **John Zink (Koch Engineered Solutions)** Duct-burner flame holders: LDRW low-draft reverse wing, VC V-cone tip wing and Coen castings, with igniters and flame scanners
- **Cleaver-Brooks** Natcom duct burner: 10-500 MMBtu/hr, under 7 ppm NOx / under 50 ppm CO

Recorded gaps:

- quantified duct-firing duty ranges for named HRSG projects — Find HRSG OEM duct-burner specification sheets with heat input and exhaust conditions.

### Low-NOx gas burner (package and ultra-low-NOx) (burner-gas-low-nox)

Primary code: PWR: Power and renewables
Burner that stages fuel and air, delays mixing or recirculates flue gas to lower flame temperature and NOx formation. Package gas burners span roughly 10-500 MMBtu/hr with 10:1 turndown; ultra-low-NOx versions reach single-digit ppm NOx with flue-gas recirculation or surface-stabilised premixed combustion. Used on fire-tube, water-tube and hot-water boilers and on refinery fired heaters.
Vendors: Cleaver-Brooks, Zeeco, John Zink (Koch Engineered Solutions), ALZETA, Miura Boiler (4 model lines recorded).

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
| Firing capacity | 450 MMBTU/hr HHV (up to) | Product page: 'firing capacity of up to 450 MMBTU/HR HHV' |
| NOx reduction mechanism | Advanced air/fuel premixing and fuel staging; internal FGR design feature | Product page Overview and Features |
| Fuels | Natural gas, produced gas, syn gas, #2 fuel oil, bitumen fuel options | Product page Features; narrative also states gas and #2/light oil firing |
| Application | Once-through steam generators (OTSGs) and heaters application | Product page Overview |
| NOx emissions | 30 ppm NOx (less than, without FGR) | Product bullets and Technical Data table: <30 ppm, ~3% O2 across wide load range |
| Natural gas input | 16.8-54.6 MMBTU/hr | Product narrative: natural gas fuel option from 16.8 to 54.6 MMBTU/hr; Technical Data Input Capacity 16,800-54,600 |
| Boiler horsepower | 400-1300 HP | Technical Data table |
| Oil input | 120-390 US GPH | Technical Data table (#2 fuel oil backup) |
| Turndown | 10 :1 (up to, gas) | Product bullet and Technical Data table |
| Furnace pressure | 3.6-5.6 inches water column (unit not printed in table) | Technical Data table value 3.6-5.6; unit not stated on page, so not asserted as a named unit |
| Minimum gas pressure | 5 table value (unit not printed) | Technical Data table |
| Mode of operation | Full modulation; parallel positioning standard control mode | Technical Data table |

- **Cleaver-Brooks** ProFire SBR-30 / SBR-5: 16.8-54.6 and 10.5-42 MMBtu/hr; 10:1; 30 ppm without FGR / 5 ppm with FGR
- **Zeeco** PLN / GO: 2.5-63 MMBtu/hr; 10:1; 9-40 ppm versus excess air (PLN), 30 ppm at 15% excess air (GO)
- **John Zink (Koch Engineered Solutions)** ECOjet Edge+: as low as 15 ppm NOx without FGR in select applications; natural gas to 100% hydrogen
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
Vendors: Stamicarbon, thyssenkrupp Uhde, Toyo Engineering, Casale, Saipem (ex-Micoperi 7000), Casale SA, Alleima (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| HP loop pressure | 150 bar | Saipem urea flowsheet, NH3-stripping process |
| condenser outlet temperature | 155 °C | Saipem urea flowsheet, NH3-stripping process |
| approach to equilibrium in a pool condenser | 60 % | reaction extent achieved in the pool condenser |
| condenser pressure regime (stripping process) | full system pressure n/a | Wikipedia: stripped ammonia carried directly to a carbamate condenser 'also under full system pressure' |
| condenser type (conventional recycle) | falling-film n/a | Wikipedia: recombining CO2 and NH3 in a falling-film carbamate condenser before pumping carbamate solution back to reactor |
| outside diameter stocked | 19.05 mm and 25.4 mm mm | UreaKnowHow news item: one-week delivery for critical heat exchanger needs |

- **Stamicarbon** LAUNCH MELT pool condenser design: capacities from about 2,500 up to 6,000 mtpd
- **thyssenkrupp Uhde** Urea 2000plus pool condenser: horizontal high-pressure carbamate condenser with submerged U-tube bundle
- **Toyo Engineering** Vertical Submerged Carbamate Condenser (VSCC): 180 C and 152 bar; produces 5 bar steam

Recorded gaps:

- Condenser duty, heat transfer area, tube material/dimensions, approach temperature — Read a carbamate condenser datasheet or licensor technical paper.
- Condenser duty, heat transfer area, tube material/dimensions, approach temperature — Read a carbamate condenser datasheet or licensor technical paper.

## cf-system

### Compressor drivers, sealing and auxiliary systems (cf-compressor-drivers-sealing-and-auxiliary-systems)

Primary code: PWR: Power and renewables
Provide shaft power, prevent process-gas leakage to atmosphere, and support lube/seal-oil and capacity control. On offshore platforms electric motors or gas turbines are most common; steam turbines are offered as integrated drivers on some turbo compressors.
Vendors: CPI by Howden, Howden Turbo UK (Peter Brotherhood) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Howden steam turbine power range | 75-40000 kW | Howden steam turbines 75 kW to 40 MWe; mechanical drive for rotating equipment 10 kW to 40 MW; inlet pressures to 70 bar |
| Packing vent-gas reduction | 20173000 Nm3 prevented | Howden/CPI EMISSIONGUARD TR2 packing rings stated to have prevented an estimated 20,173,000 Nm3 (693,144,000 scf) of vented gas, equivalent to 60,500 t CO2 |
| Compressor improvement standard | API 618 standard | Howden lists N2 buffer system per API 618 and 'compressor improvements API 618' in revamp services |


Recorded gaps:

- Named compressor train with driver power, seal type and auxiliaries for an offshore gas export duty — Fetch a Siemens Energy or GE Vernova compressor-train data sheet and an FPSO topsides equipment list
- Named compressor train with driver power, seal type and auxiliaries for an offshore gas export duty — Fetch a Siemens Energy or GE Vernova compressor-train data sheet and an FPSO topsides equipment list

### Diesel engine generator sets (cf-diesel-engine-generator-sets-offshore-and-onshore-4cb391)

Primary code: PWR: Power and renewables
Prime/standby/emergency electrical power for platforms and plants, driving emergency lighting, fire pumps, drilling equipment and process loads. Compact high-power-to-weight packages are favoured offshore; paralleling and system controls are provided by integrated power systems.
Vendors: Cummins Inc., Rolls-Royce Power Systems (mtu), Caterpillar, INNIO / Wartsila (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Cummins diesel genset rating range | 15-3750 kVA | Cummins APAC diesel generator page: 'generator sets from 15 - 3750 kVA'; 50/60 Hz quiet and standard product families |
| Cummins start/load acceptance | <10 seconds to assume load | Cummins commercial generators 'start and assume load in less than 10 seconds, and rated load in a single step' |
| Cummins natural-gas genset range | 13-2000 kW | Cummins generators overview: natural gas generator sets 13 to 2000 kW; diesel 15-3750 kVA; HVO-capable |
| MTU diesel genset portfolio ceiling | 3250 kWe @60 Hz | MTU diesel generator set page: 'up to 3,250 kWe (60 Hz) and up to 4,000 kVA (50 Hz)'; 85% load factor standby, 75% prime |
| MTU Series 2000 rating | 680-1250 kWe @60 Hz (770-1400 kVA @50 Hz) | MTU diesel generator sets page series table |
| MTU offshore design basis | classified by all major classification societies qualitative | MTU offshore O&G solutions: compact, high power-to-weight gensets; backup/standby/continuous power; emergency supply and fire-extinguishing pumps; mud pumps/frac drives; explosion-risk safety designs and certifications such as NFPA 20 |


Recorded gaps:

- Numeric EPA Tier 4 Final / EU Stage V emission limits for nonroad diesel gensets (g/kWh NOx, PM) and applicability dates — Fetch the current EPA nonroad diesel rule page and the EU mobile-machinery regulation page directly, then record exact limits and dates
- Paralleling/load-sharing and black-start control architecture for a named offshore platform — Fetch an OEM integrated power-system or operator case study
- Offshore genset derating at ambient/altitude and exact per-model offshore ratings — Fetch mtu/Cummins offshore specification sheets

### Diesel engine generator sets (cf-diesel-engine-generator-sets-offshore-and-onshore)

Primary code: PWR: Power and renewables
Prime/standby/emergency electrical power for platforms and plants, driving emergency lighting, fire pumps, drilling equipment and process loads. Compact high-power-to-weight packages are favoured offshore; paralleling and system controls are provided by integrated power systems.
Vendors: Cummins Inc., Rolls-Royce Power Systems (mtu), Caterpillar, INNIO / Wartsila (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Cummins diesel genset rating range | 15-3750 kVA | Cummins APAC diesel generator page: 'generator sets from 15 - 3750 kVA'; 50/60 Hz quiet and standard product families |
| Cummins start/load acceptance | <10 seconds to assume load | Cummins commercial generators 'start and assume load in less than 10 seconds, and rated load in a single step' |
| Cummins natural-gas genset range | 13-2000 kW | Cummins generators overview: natural gas generator sets 13 to 2000 kW; diesel 15-3750 kVA; HVO-capable |
| MTU diesel genset portfolio ceiling | 3250 kWe @60 Hz | MTU diesel generator set page: 'up to 3,250 kWe (60 Hz) and up to 4,000 kVA (50 Hz)'; 85% load factor standby, 75% prime |
| MTU Series 2000 rating | 680-1250 kWe @60 Hz (770-1400 kVA @50 Hz) | MTU diesel generator sets page series table |
| MTU offshore design basis | classified by all major classification societies qualitative | MTU offshore O&G solutions: compact, high power-to-weight gensets; backup/standby/continuous power; emergency supply and fire-extinguishing pumps; mud pumps/frac drives; explosion-risk safety designs and certifications such as NFPA 20 |
| Generator set power range | 15-3750 kVA | We offer a diverse range of generator sets from 15 - 3750 kVA |
| Frequency | 50 / 60 Hz | Quiet Diesel Generators: Frequency (Hz) 60, 50; Standard Diesel Generators: Frequency (Hz) 50, 60 |
| Load acceptance | 10 s (less than) | Commercial and Industrial solutions: Able to start and assume load in less than 10 seconds, and rated load in a single step |
| Sunny Central UP maximum power | 4600 kW | Central Inverters for PV Power Plants: Sunny Central UP maximum 4,600 kW |
| Sunny Highpower PEAK3 power | 100-180 kW (100 / 150 / 172 / 180) | Sunny Highpower PEAK3 100 kW / 150 kW / 172 kW / 180 kW |
| Sunny Tripower 125 power | 125 kW | Sunny Tripower 125 125 kW - The ideal PV inverter for large commercial systems |
| Sunny Tripower X 60 power | 50-60 kW | Sunny Tripower X 60 50 kW / 60 kW - The smart solution for commercial applications |
| Sunny Tripower X 25 power | 12-25 kW (12 / 15 / 20 / 25) | Sunny Tripower X 25 12 kW / 15 kW / 20 kW / 25 kW |
| Portfolio maximum (60 Hz) | 3250 kWe | Our product portfolio covers diesel generator sets up to 3,250 kWe (60 Hz) and up to 4,000 kVA (50 Hz) |
| Portfolio maximum (50 Hz) | 4000 kVA | Our product portfolio covers diesel generator sets up to 3,250 kWe (60 Hz) and up to 4,000 kVA (50 Hz) |
| Series 4000 power range | 1600-4000 kVA (50 Hz); 1,125-3,250 kWe (60 Hz) | mtu Series 4000 POWER RANGE: 50 Hz: 1,600 - 4,000 kVA; 60 Hz: 1,125 - 3,250 kWe |
| Series 2000 power range | 770-1400 kVA (50 Hz); 680-1,250 kWe (60 Hz) | mtu Series 2000 POWER RANGE: 50 Hz: 770 - 1,400 kVA; 60 Hz: 680 - 1,250 kWe |


Recorded gaps:

- Numeric EPA Tier 4 Final / EU Stage V emission limits for nonroad diesel gensets (g/kWh NOx, PM) and applicability dates — Fetch the current EPA nonroad diesel rule page and the EU mobile-machinery regulation page directly, then record exact limits and dates
- Paralleling/load-sharing and black-start control architecture for a named offshore platform — Fetch an OEM integrated power-system or operator case study
- Offshore genset derating at ambient/altitude and exact per-model offshore ratings — Fetch mtu/Cummins offshore specification sheets

### Flare gas recovery (cf-flare-gas-recovery-fgr-and-enclosed-ground-flare-packages-047094)

Primary code: PWR: Power and renewables
Captures gas that would otherwise be flared, using a liquid seal vessel for backpressure control and flashback prevention, plus compression (ejector or compressor) and optional H2S sweetening. Reduces emissions, light, noise and odour and extends flare tip life.
Vendors: John Zink (Koch Engineered Solutions) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| FGR application scope | refineries to FPSO offshore platforms qualitative | John Zink states FGR systems are 'custom-engineered' for applications from petroleum refineries to FPSO offshore platforms |
| FGR emissions reduced | NOx, CO, CO2, SOx qualitative | John Zink FGR benefit statement; also reduces purchased fuel gas and steam and can lower carbon taxes/fines |
| Ground flare heat/visibility control | refractory-lined steel box or cylinder qualitative | Ground flares hide the flame and reduce thermal radiation and noise; open at top with base air openings; multiple tips for turndown; used onshore in sensitive areas and on FPSOs |


Recorded gaps:

- Named FGR installation with recovered gas flow, seal pressure and payback — Fetch an operator or John Zink FGR case study with data

### Flare gas recovery (cf-flare-gas-recovery-fgr-and-enclosed-ground-flare-packages)

Primary code: PWR: Power and renewables
Captures gas that would otherwise be flared, using a liquid seal vessel for backpressure control and flashback prevention, plus compression (ejector or compressor) and optional H2S sweetening. Reduces emissions, light, noise and odour and extends flare tip life.
Vendors: John Zink (Koch Engineered Solutions) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| FGR application scope | refineries to FPSO offshore platforms qualitative | John Zink states FGR systems are 'custom-engineered' for applications from petroleum refineries to FPSO offshore platforms |
| FGR emissions reduced | NOx, CO, CO2, SOx qualitative | John Zink FGR benefit statement; also reduces purchased fuel gas and steam and can lower carbon taxes/fines |
| Ground flare heat/visibility control | refractory-lined steel box or cylinder qualitative | Ground flares hide the flame and reduce thermal radiation and noise; open at top with base air openings; multiple tips for turndown; used onshore in sensitive areas and on FPSOs |


Recorded gaps:

- Named FGR installation with recovered gas flow, seal pressure and payback — Fetch an operator or John Zink FGR case study with data

### Flare stack / boom system with knockout drum, seal drum, flare tips, pilots and ignition (cf-flare-stack-boom-system-with-knockout-drum-seal-drum-flare-tip)

Primary code: PWR: Power and renewables
Safely disposes of relieved and waste gas from PSVs and shutdowns. Header routes gas to a KO (vapour-liquid separator) drum, then a water/liquid seal drum preventing flashback, then an elevated stack or ground flare with pilots and continuous ignition. Stack height or boom reach is set by permissible thermal radiation.
Vendors: John Zink (Koch Engineered Solutions), FlareTech, Zeto (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Continuous personnel thermal radiation limit | 1.58 kW/m2 | Recommended maximum for continuous exposure of personnel wearing appropriate industrial clothing; 500 Btu/hr.ft2 |
| Short-exposure thermal radiation (3-4 min) | 4.73 kW/m2 | 4.73 kW/m2 (1500 Btu/hr.ft2) limits exposure to 3-4 minutes |
| Short-exposure thermal radiation (30 s) | 6.31 kW/m2 | 6.31 kW/m2 (2000 Btu/hr.ft2) limits exposure to 30 seconds |
| Sonic flare tip upstream pressure threshold | 5-? bar (greater than) | Wikipedia gas-flare tip configurations: 'sonic tip - upstream pressure >5 bar' |
| Enclosed biogas flare combustion temperature | 1000-1200 degC | Flare specification for enclosed flares: >1000 and <1200 degC to ensure 98% destruction efficiency and avoid NOx formation; 0.3 s residence time in chimney |
| Flare destruction efficiency (LRGO multi-point ground flare) | 99.5-? % (typically greater than) | John Zink LRGO: 'highest destruction efficiency (typically >99.5%) of any flare type'; API 537 compliance available |
| Turndown | unlimited turndown (as printed) | Features: Unlimited Turndown - Some of the systems can offer unlimited turndown, making them highly adaptable to varying operational conditions |
| Assist medium | 0 no assist medium required | Features: No Assist Medium Required - These flares produce short, smokeless flames without the need for an assist medium, allowing for shorter boom lengths and simpler mounting structures |
| Service history | 30 years (over) | John Zink's pressure-assisted flares have been successfully used in a wide range of applications for over 30 years |
| Destruction efficiency | >99.5 % | Low Emissions: This system has demonstrated the highest destruction efficiency (typically > 99.5%) of any flare type |
| API compliance | API 537 standard (available) | Features: Available API 537 Compliance - Ensures compliance with the latest Industry flare standards |
| Smokeless operation | 100 % at high flow rates | Benefits: Design is capable of producing 100% smokeless operation at high flow rates, reducing the offsite impact of the flare system |
| Electric operation | 100 % electric (as printed) | Features: 100% Electric Operation - No need for pilot fuel gas or instrument air, reducing utility consumption |
| Power options | grid, battery, or solar charging power supply options (as printed) | Flexible Power Options - Operates on grid power, battery, or solar charging |
| Destruction rate efficiency | >98 % | offering greater than 98% destruction rate efficiencies for methane and other gases / Features: Achieves greater than 98% destruction rate efficiencies |
| Instantaneous turndown | 10:1 ratio (up to) | this system provides up to 10:1 instantaneous turndown from maximum design without the need for external adjustments |
| Capacity | 6000 SCFM | Features: Exceptional Capacity - Processes up to 6,000 SCFM at 50% methane concentration |
| Methane concentration basis | 50 % | Processes up to 6,000 SCFM at 50% methane concentration |


Recorded gaps:

- Direct text of API Std 521 and API Std 537 (edition, scope, definitive radiation/noise limits) — Use the API webstore or IBR reading room; record exact edition and clause before citing limits as normative
- ISO 25457 scope, edition and relationship to API 537 — Locate the correct ISO catalogue record via iso.org search and fetch it
- Quantified flare noise limits and flare-stack height design method — Fetch a dedicated flare-noise/stack-height engineering reference or an operator design standard
- KO drum and seal drum sizing rules (holdup, residence time, diameter) — Fetch API 521 text or an engineering-design reference with worked sizing
- Direct text of API Std 521 and API Std 537 (edition, scope, definitive radiation/noise limits) — Use the API webstore or IBR reading room; record exact edition and clause before citing limits as normative
- ISO 25457 scope, edition and relationship to API 537 — Locate the correct ISO catalogue record via iso.org search and fetch it

### Floating / offshore solar PV (cf-floating-offshore-solar-pv-fpv-and-hybridisation-9b286c)

Primary code: PWR: Power and renewables
PV mounted on buoyant structures over water; relevant to offshore/nearshore facilities where land is unavailable. Water cooling can improve yield; salt-water installations need corrosion resistance, wave/wind design and robust anchoring.
Vendors: Sungrow, Oceans of Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sungrow FPV global installed capacity | 4-? GW (greater than) | Sungrow floating PV page: 'With Over 4GW of Floating PV Application'; No.1 global market share stated; 290+ patents |
| Sungrow Cirata FPV project | 192 MW | Sungrow FPV case: world's largest floating PV project at a hydroelectric power station, Cirata, Indonesia, reservoir, 192 MW |
| Global installed FPV capacity | 13 GW in 2022 | Wikipedia floating solar: grew from 3 GW in 2020 to 13 GW in 2022; World Bank estimates >4,000 GW technical capacity at 10% coverage of 6,600 large water bodies |
| FPV energy-yield gain from water cooling | 5-15 % | Wikipedia floating solar 'cooling effect of the water ... leads to an energy gain that ranges from 5% to 15%' |
| FPV installation cost premium | 10-25 % higher than ground-mount (2023) | Wikipedia floating solar: 'installation was about 10-25% higher in 2023', attributed mainly to anchoring (NREL researcher) |
| First offshore FPV at sea | 15 kWp pilot, Maldives, 2014 | Wikipedia: Swimsol installed world's first offshore floating solar PV at sea, 15 kWp pilot in Maldives with TU Wien and Fraunhofer; 2019 Oceans of Energy first open rough-sea North Sea farm |


Recorded gaps:

- Verified offshore FPV installation on an operating oil & gas platform, with MW and metocean design basis — Search operator/engineering pages for an offshore platform PV pilot and fetch a data sheet
- Reconciliation of conflicting FPV yield-gain figures (5-15% vs 0.6-4.4%) — Fetch the underlying peer-reviewed LCA/yield papers cited in that page

### Floating / offshore solar PV (cf-floating-offshore-solar-pv-fpv-and-hybridisation)

Primary code: PWR: Power and renewables
PV mounted on buoyant structures over water; relevant to offshore/nearshore facilities where land is unavailable. Water cooling can improve yield; salt-water installations need corrosion resistance, wave/wind design and robust anchoring.
Vendors: Sungrow, Oceans of Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sungrow FPV global installed capacity | 4-? GW (greater than) | Sungrow floating PV page: 'With Over 4GW of Floating PV Application'; No.1 global market share stated; 290+ patents |
| Sungrow Cirata FPV project | 192 MW | Sungrow FPV case: world's largest floating PV project at a hydroelectric power station, Cirata, Indonesia, reservoir, 192 MW |
| Global installed FPV capacity | 13 GW in 2022 | Wikipedia floating solar: grew from 3 GW in 2020 to 13 GW in 2022; World Bank estimates >4,000 GW technical capacity at 10% coverage of 6,600 large water bodies |
| FPV energy-yield gain from water cooling | 5-15 % | Wikipedia floating solar 'cooling effect of the water ... leads to an energy gain that ranges from 5% to 15%' |
| FPV installation cost premium | 10-25 % higher than ground-mount (2023) | Wikipedia floating solar: 'installation was about 10-25% higher in 2023', attributed mainly to anchoring (NREL researcher) |
| First offshore FPV at sea | 15 kWp pilot, Maldives, 2014 | Wikipedia: Swimsol installed world's first offshore floating solar PV at sea, 15 kWp pilot in Maldives with TU Wien and Fraunhofer; 2019 Oceans of Energy first open rough-sea North Sea farm |


Recorded gaps:

- Verified offshore FPV installation on an operating oil & gas platform, with MW and metocean design basis — Search operator/engineering pages for an offshore platform PV pilot and fetch a data sheet
- Reconciliation of conflicting FPV yield-gain figures (5-15% vs 0.6-4.4%) — Fetch the underlying peer-reviewed LCA/yield papers cited in that page

### Gas export / reinforcement centrifugal compressor train (cf-gas-export-reinforcement-centrifugal-compressor-train-integral-a5a9f5)

Primary code: PWR: Power and renewables
Raises gas pressure for export pipeline or reservoir reinjection. Integrally geared and multistage centrifugal machines cover high-volume pipeline/process duty; drivers are electric motors or steam/gas turbines, with dry gas seals and oil systems as auxiliaries.
Vendors: Howden (a Chart Industries company; KK&K, CKD brands), Siemens Energy (incl. ex-Dresser-Rand), GE Vernova / Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Single-stage flow range | 1500-600000 m3/h | Howden/KK&K single-stage centrifugal model range (SF 15,000-600,000; SFG 5,000-300,000; ST 1,500-150,000; SL 15,000-450,000 m3/h), pressure ratio up to 3.5 |
| Multistage flow range | 400-200000 m3/h | Howden/KK&K + CKD multistage range (RS 400-65,000; RV 400-85,000 / 400-170,000 back-to-back), pressure ratio up to 10.0 |
| Periflow maximum discharge pressure | 350 bar | Howden Periflow compressor performance, capacity flow 10-20,000 m3/h, variable speed 1000-6000 rpm |
| Compressor design life / installed base | 4000 installations | Howden industrial centrifugal turbo compressors, 'proven over 100 years and 4000 installations' |
| Screw compressors in FLNG service | Howden states screw compressors 'selected for a number of FLNG projects for t... | Howden states screw compressors 'selected for a number of FLNG projects for their compact design, high performance and reliability' (FLNGscrewcompressor.pdf listed on page); no numeric rating printed on fetched page |
| Single-stage model range flow | 3000-600000 m3/h | Howden single stage centrifugal compressors model range serves applications requiring flows of between 3,000 m3/h and 600,000 m3/h with pressure ratios up to 3.5 |
| Multistage model range flow | 400-200000 m3/h | Howden multistage centrifugal compressors model range serves applications requiring flows of between 400 m3/h and 200,000 m3/h with pressure ratios up to 10.0 |
| SF model flow | 15000-600000 m3/h | Model table: SF, Flow (m3/h) 15,000-600,000; Pressure Ratio up to 3.5; Impeller Dia. (mm) up to 2240; Drive Electric or turbine |
| SFG model flow | 5000-300000 m3/h | Model table: SFG, Flow (m3/h) 5,000-300,000; Pressure Ratio up to 3.5; Impeller Dia. (mm) up to 1120 |
| ST model flow | 1500-150000 m3/h | Model table: ST, Flow (m3/h) 1,500-150,000; Pressure Ratio up to 3.5; Impeller Dia. (mm) up to 900; Drive Steam turbine (integrated) |
| SL model flow | 15000-450000 m3/h | Model table: SL, Flow (m3/h) 15,000-450,000; Pressure Ratio up to 1.45; Impeller Dia. (mm) up to 1800; application Coke oven gas |
| SFG Twin model flow | 3000-200000 m3/h | Multistage model table: SFG Twin, Flow (m3/h) 3,000-200,000; Pressure Ratio up to 6.0; Impeller Dia. (mm) up to 900 |
| SFG Back-to-Back model flow | 3000-75000 m3/h | Multistage model table: SFG Back-to-Back, Flow (m3/h) 3,000-75,000; Pressure Ratio up to 6.0; Impeller Dia. (mm) up to 560 |
| RS model flow | 400-65000 m3/h | Multistage model table: RS, Flow (m3/h) 400-65,000; Pressure Ratio up to 10.0; Impeller Dia. (mm) up to 700 |
| RV model flow | 400-85000 m3/h | Multistage model table: RV, Flow (m3/h) 400-85,000; 400-170,000 (back-to-back); Pressure Ratio up to 10.0; Impeller Dia. (mm) up to 780 |
| CKD multistage discharge pressure | 20 MPa | CKD compressors serve flow requirements up to 1700,000 m3/h (as printed) and discharge pressures of up to 20 MPa |
| SFO/SFP/SFN pressure | 50 bar | SFO, SFP and SFN series formerly branded as Kühnle, Kopp & Kausch. Single and multi-stage turbo compressors for the chemical and petrochemical industries with pressures up to 50 bar and flow rates up to 200,000 m3/hr |


Recorded gaps:

- Named offshore/onshore gas-export compressor train with duty (MMSCFD, suction/discharge bar, absorbed MW) and driver — Fetch Siemens Energy 'compression' product pages and a named operator/EPC case study with an equipment data sheet
- Dry-gas seal and wet-seal leakage / seal-gas consumption figures for export compressors — Fetch a dry-gas seal OEM data sheet (e.g. Flowserve/John Crane) and Howden/CPI sealing bulletin

### Gas export / reinforcement centrifugal compressor train (cf-gas-export-reinforcement-centrifugal-compressor-train-integral)

Primary code: PWR: Power and renewables
Raises gas pressure for export pipeline or reservoir reinjection. Integrally geared and multistage centrifugal machines cover high-volume pipeline/process duty; drivers are electric motors or steam/gas turbines, with dry gas seals and oil systems as auxiliaries.
Vendors: Howden (a Chart Industries company; KK&K, CKD brands), Siemens Energy (incl. ex-Dresser-Rand), GE Vernova / Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Single-stage flow range | 1500-600000 m3/h | Howden/KK&K single-stage centrifugal model range (SF 15,000-600,000; SFG 5,000-300,000; ST 1,500-150,000; SL 15,000-450,000 m3/h), pressure ratio up to 3.5 |
| Multistage flow range | 400-200000 m3/h | Howden/KK&K + CKD multistage range (RS 400-65,000; RV 400-85,000 / 400-170,000 back-to-back), pressure ratio up to 10.0 |
| Periflow maximum discharge pressure | 350 bar | Howden Periflow compressor performance, capacity flow 10-20,000 m3/h, variable speed 1000-6000 rpm |
| Compressor design life / installed base | 4000 installations | Howden industrial centrifugal turbo compressors, 'proven over 100 years and 4000 installations' |
| Screw compressors in FLNG service | Howden states screw compressors 'selected for a number of FLNG projects for t... | Howden states screw compressors 'selected for a number of FLNG projects for their compact design, high performance and reliability' (FLNGscrewcompressor.pdf listed on page); no numeric rating printed on fetched page |


Recorded gaps:

- Named offshore/onshore gas-export compressor train with duty (MMSCFD, suction/discharge bar, absorbed MW) and driver — Fetch Siemens Energy 'compression' product pages and a named operator/EPC case study with an equipment data sheet
- Dry-gas seal and wet-seal leakage / seal-gas consumption figures for export compressors — Fetch a dry-gas seal OEM data sheet (e.g. Flowserve/John Crane) and Howden/CPI sealing bulletin

### High-pressure / hermetic injection compressors (cf-high-pressure-hermetic-injection-compressors-diaphragm-hybrid-ce91d6)

Primary code: PWR: Power and renewables
Handles high-pressure, toxic, flammable or high-purity gases where hermetic separation or zero leakage is required; applicable to CO2 injection and hydrogen compression packages as well as specialty gas service.
Vendors: Ariel Corporation (with Hoerbiger), Howden / Burton Corblin (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ariel KBH suction pressure | 25 bar | Ariel KBH hydrogen compressor suction 370 psig (25 bar) |
| Ariel KBH discharge pressure | 500 bar | Ariel KBH discharge 7,250 psig (500 bar); flow at design point 250 kg/h; stroke 4.25 in (108 mm); max 1000 rpm |
| Howden hybrid pressure increase | 450 bar | Howden hybrid reciprocating compressor, horizontal or vertical, up to five compression stages, with inter-stage cooling and condensate purging; suitable for virtually all dry gases incl. helium, hydrogen, nitrogen |
| Diaphragm compressor package electrolyser sizing | 5-10 MW | Howden TFC90 and TFC180 standardised diaphragm compressor packages designed for 5 MW and 10 MW electrolyser modules; skid mounted, zero process-gas leakage |


Recorded gaps:

- CO2 injection compressor duty, material selection and phase behaviour (dense/supercritical CO2) for a named CCS/EOR project — Fetch an OEM CO2 compressor page (e.g. Siemens/man-es-oss or Ariel CO2 bulletin) and a named CO2-EOR injection case study
- Seal leakage rate and seal-gas consumption for high-pressure hydrogen/CO2 packages — Fetch CPI/Howden sealing bulletin or a dry-gas seal data sheet

### High-pressure / hermetic injection compressors (cf-high-pressure-hermetic-injection-compressors-diaphragm-hybrid)

Primary code: PWR: Power and renewables
Handles high-pressure, toxic, flammable or high-purity gases where hermetic separation or zero leakage is required; applicable to CO2 injection and hydrogen compression packages as well as specialty gas service.
Vendors: Ariel Corporation (with Hoerbiger), Howden / Burton Corblin (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ariel KBH suction pressure | 25 bar | Ariel KBH hydrogen compressor suction 370 psig (25 bar) |
| Ariel KBH discharge pressure | 500 bar | Ariel KBH discharge 7,250 psig (500 bar); flow at design point 250 kg/h; stroke 4.25 in (108 mm); max 1000 rpm |
| Howden hybrid pressure increase | 450 bar | Howden hybrid reciprocating compressor, horizontal or vertical, up to five compression stages, with inter-stage cooling and condensate purging; suitable for virtually all dry gases incl. helium, hydrogen, nitrogen |
| Diaphragm compressor package electrolyser sizing | 5-10 MW | Howden TFC90 and TFC180 standardised diaphragm compressor packages designed for 5 MW and 10 MW electrolyser modules; skid mounted, zero process-gas leakage |


Recorded gaps:

- CO2 injection compressor duty, material selection and phase behaviour (dense/supercritical CO2) for a named CCS/EOR project — Fetch an OEM CO2 compressor page (e.g. Siemens/man-es-oss or Ariel CO2 bulletin) and a named CO2-EOR injection case study
- Seal leakage rate and seal-gas consumption for high-pressure hydrogen/CO2 packages — Fetch CPI/Howden sealing bulletin or a dry-gas seal data sheet

### Process, gas-transmission and power piping codes and pipe classes (cf-process-gas-transmission-and-power-piping-codes-and-pipe-class)

Primary code: PWR: Power and renewables
Defines materials, design, fabrication, assembly, erection, examination, inspection and testing for piping. B31.3 governs plant process piping, B31.8 gas transmission/distribution including offshore gathering appurtenances, and B31.1 power/boiler-external piping.
Vendors: ASME, API (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| B31.3 latest edition | 2024 edition year | ASME B31.3 Process Piping page states 'B31.3 - 2024' |
| B31.8 latest edition | 2025 edition year | ASME B31.8 Gas Transmission and Distribution Piping Systems page states 'B31.8 - 2025' |
| B31.1 latest edition | 2026 edition year | ASME B31.1 Power Piping page states 'B31.1 - 2026' |
| B31.3 key 2024 changes | Unlisted valves, flexibility/SIF, impact testing, flange attachment welds, heat treatment, high-pressure fluid service design & fatigue clause list | ASME B31.3 product page 'Key changes' list with paragraph references (307, 319 & 320, 323.2.2/323.3.1, 328.5.2, 330.1/331.1, K302.3.2, K302.3/K304.8) |
| B31.1 key 2026 changes | Appendices Q/R, B31J reference, joint exposure during pressure test, wind/earthquake factors, API 579-1/ASME FFS-1 reference clause list | ASME B31.1 product page 'Key changes' list |
| Product lineage | 1947 year introduced (as printed) | Since the introduction of the Swagelok tube fitting in 1947, industrial professionals have relied on Swagelok fittings to achieve leak-tight connections in their analytical, instrumentation, and small-bore process fluid systems |
| Flange adapter standards families | ANSI / DIN / EN / Lap Joint flange families (as printed) | Flange Adapters categories listed: ANSI Flanges, DIN Flanges, EN Flanges, Lap Joint Flanges |
| Pipe joining product families | Rigid / Flexible / Transition / Reducing / Outlet / Plain End / Flange Adapters / Expansion Joints / Press families (as printed) | Pipe Joining category listing on the Products page |
| Fitting materials | carbon steel, stainless steel, copper, HDPE, PVC/CPVC and other pipe materials materials (as printed) | Fittings section: hundreds of pipe fittings and a range of adapters and outlets in carbon steel, stainless steel, copper, HDPE, PVC/CPVC and other pipe materials |


Recorded gaps:

- Full normative text and allowable stress tables of B31.3/B31.8/B31.1 — Procurement of standards; do not infer allowable stresses from public pages
- Typical offshore vs onshore piping class differences (materials, corrosion allowance, supports, insulation, expansion) — Fetch a project piping specification or a recognised piping-engineering reference (e.g. ASTM/API material specs, offshore operator standard)
- Valve, flange and fitting standards (API 600/602/605, ASME B16.5/B16.9, MSS) and their numeric dimensions/ratings — Fetch ASME/API product pages for the specific component standards
- Full normative text and allowable stress tables of B31.3/B31.8/B31.1 — Procurement of standards; do not infer allowable stresses from public pages
- Typical offshore vs onshore piping class differences (materials, corrosion allowance, supports, insulation, expansion) — Fetch a project piping specification or a recognised piping-engineering reference (e.g. ASTM/API material specs, offshore operator standard)

### Reciprocating gas compressor frames (cf-reciprocating-gas-compressor-frames-export-gas-lift-reinjectio-e3043e)

Primary code: PWR: Power and renewables
Positive-displacement compression where high pressure ratio, turndown or intermittent duty is required. Ariel frames are separable, engine- or motor-driven, with high-pressure cylinders for gas lift, gas reinjection and CNG; large frames are recommended for pipeline transmission and high-pressure injection.
Vendors: Ariel Corporation (with Hoerbiger), Howden / Peter Brotherhood (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Small-frame rated power (1-throw / 2-throw) | 126-280 BHP | Ariel JGN/JGQ, 1 throw JGN 126 BHP @1500 rpm, JGQ 140 BHP @1800 rpm; 2 throw JGN 252 BHP, JGQ 280 BHP. Rod load 18,000-20,000 lb; stroke 3.5 in (JGN) / 3.0 in (JGQ) |
| Large-frame rated power | 6668-10000 BHP | Ariel KBB/KBV, 4-throw 6668 BHP and 6-throw 10,000 BHP; stroke 7.25 in (KBB) / 8.50 in (KBV); total rod load 190,000 lb; max 900/750 rpm |
| Reciprocating compressor power rating | 20 MW | Howden / Peter Brotherhood reciprocating compressors rated to 20 MW, operating 260-1000 rpm |
| Compressors manufactured | 70000 units since 1966 | Ariel '70,000+ compressors manufactured since 1966'; 550+ cylinder-to-frame combinations |
| Downstream rod-load limit | 10000 lbf | Ariel process/refining/chemical compressors 'rod load up to 10,000 lbs' |


Recorded gaps:

- Actual gas-lift / reinjection discharge pressures and capacities for Ariel frames in named fields — Fetch Ariel product spec-sheet PDFs and an operator gas-lift case study

### Reciprocating gas compressor frames (cf-reciprocating-gas-compressor-frames-export-gas-lift-reinjectio)

Primary code: PWR: Power and renewables
Positive-displacement compression where high pressure ratio, turndown or intermittent duty is required. Ariel frames are separable, engine- or motor-driven, with high-pressure cylinders for gas lift, gas reinjection and CNG; large frames are recommended for pipeline transmission and high-pressure injection.
Vendors: Ariel Corporation (with Hoerbiger), Howden / Peter Brotherhood (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Small-frame rated power (1-throw / 2-throw) | 126-280 BHP | Ariel JGN/JGQ, 1 throw JGN 126 BHP @1500 rpm, JGQ 140 BHP @1800 rpm; 2 throw JGN 252 BHP, JGQ 280 BHP. Rod load 18,000-20,000 lb; stroke 3.5 in (JGN) / 3.0 in (JGQ) |
| Large-frame rated power | 6668-10000 BHP | Ariel KBB/KBV, 4-throw 6668 BHP and 6-throw 10,000 BHP; stroke 7.25 in (KBB) / 8.50 in (KBV); total rod load 190,000 lb; max 900/750 rpm |
| Reciprocating compressor power rating | 20 MW | Howden / Peter Brotherhood reciprocating compressors rated to 20 MW, operating 260-1000 rpm |
| Compressors manufactured | 70000 units since 1966 | Ariel '70,000+ compressors manufactured since 1966'; 550+ cylinder-to-frame combinations |
| Downstream rod-load limit | 10000 lbf | Ariel process/refining/chemical compressors 'rod load up to 10,000 lbs' |


Recorded gaps:

- Actual gas-lift / reinjection discharge pressures and capacities for Ariel frames in named fields — Fetch Ariel product spec-sheet PDFs and an operator gas-lift case study

### Solar PV modules and inverters (cf-solar-pv-modules-and-inverters-onshore-gas-plant-and-remote-hy-fa78bf)

Primary code: PWR: Power and renewables
Converts sunlight to DC and then AC for facility auxiliary loads; hybrids with diesel/BESS reduce fuel use at remote onshore sites. Utility-scale modules and string/modular inverters are the core hardware.
Vendors: LONGi, Sungrow, SolarEdge, Trina Solar (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| LONGi Hi-MO 9 module maximum power | 670 W | LONGi Hi-MO 9 product page 'Up to 670 W'; HPBC 2.0 technology, 0BB front design |
| LONGi Hi-MO 9 module efficiency | 24.8 % | LONGi Hi-MO 9 'Module efficiency of up to 24.8%' |
| LONGi Hi-MO 9 STC Pmax (LR7-72HYD-660M) | 660 W | STC table: Voc 54.00 V, Isc 15.41 A, Vmp 44.85 V, Imp 14.72 A |
| LONGi Hi-MO 9 mechanical dimensions and mass | 2382 x 1134 x 30 mm (33.5 kg) | Mechanical parameters: 144 cells (6x24), split junction box IP68 with 3 diodes; 36 pcs/pallet, 720 pcs/40HC |
| LONGi Hi-MO 9 mechanical load | 2400-5400 Pa | Max static load front 5400 Pa (snow/wind), back 2400 Pa (wind) |
| Sungrow product categories | string inverter, modular inverter, MLPE, floating PV system, ESS, EV charger category list | Sungrow products page lists these categories; company states No.1 PV inverter shipment in 2025 (S&P Global estimate cited) |


Recorded gaps:

- Named diesel-solar hybrid installation for a remote oil & gas platform/plant with PV MW, diesel MW and fuel-saving figure — Fetch an operator/OEM hybrid-power case study with numeric capacity and diesel displacement
- Onshore solar capacity at a named gas processing plant — Locate and fetch a gas-plant PV project page

### Solar PV modules and inverters (cf-solar-pv-modules-and-inverters-onshore-gas-plant-and-remote-hy)

Primary code: PWR: Power and renewables
Converts sunlight to DC and then AC for facility auxiliary loads; hybrids with diesel/BESS reduce fuel use at remote onshore sites. Utility-scale modules and string/modular inverters are the core hardware.
Vendors: LONGi, Sungrow, SolarEdge, Trina Solar (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| LONGi Hi-MO 9 module maximum power | 670 W | LONGi Hi-MO 9 product page 'Up to 670 W'; HPBC 2.0 technology, 0BB front design |
| LONGi Hi-MO 9 module efficiency | 24.8 % | LONGi Hi-MO 9 'Module efficiency of up to 24.8%' |
| LONGi Hi-MO 9 STC Pmax (LR7-72HYD-660M) | 660 W | STC table: Voc 54.00 V, Isc 15.41 A, Vmp 44.85 V, Imp 14.72 A |
| LONGi Hi-MO 9 mechanical dimensions and mass | 2382 x 1134 x 30 mm (33.5 kg) | Mechanical parameters: 144 cells (6x24), split junction box IP68 with 3 diodes; 36 pcs/pallet, 720 pcs/40HC |
| LONGi Hi-MO 9 mechanical load | 2400-5400 Pa | Max static load front 5400 Pa (snow/wind), back 2400 Pa (wind) |
| Sungrow product categories | string inverter, modular inverter, MLPE, floating PV system, ESS, EV charger category list | Sungrow products page lists these categories; company states No.1 PV inverter shipment in 2025 (S&P Global estimate cited) |
| Global FPV application | 4 GW (over, as printed) | With Over 4GW of Floating PV Application, We Set the Standard / >4 GW Global Application |
| FPV patents | 290 patents (over, as printed) | 290 + Patents (page stat) |
| Reference project - Indonesia | 192 MW | Cases & Stories: Capacity 192 MW, Location Indonesia, Application Scenario Reservoir |
| Reference project - Anhui China | 200 MW | Cases & Stories: Major 200MW Floating Solar Plant Launched on Anhui's Former Coal Mines; Capacity 200 MW, Application Scenario Subsidence Area |
| Reference project - Philippines | 4.99 MW | Cases & Stories: Philippines' First Megawatt-Scale Floating Solar Plant; Capacity 4.99 MW, Application Scenario Reservoir |
| Module power | 670 W (up to) | Up to 670 W Module Power (page header stat) |
| Module efficiency | 24.8 % (up to) | Up to 24.80 % Module Efficiency (page header stat) |
| Product warranty | 12 years | 12 Years Product Warranty (page header stat) |
| Power warranty | 30 years | 30 Years Power Warranty (page header stat) |
| Pmax STC (LR7-72HYD-635M to 660M) | 635-660 W | Electrical Performance Parameters (STC Test) table: Maximum power (Pmax/W) 635 / 640 / 645 / 650 / 655 / 660 |
| Voc STC | 53.5-54.0 V | Electrical Performance Parameters (STC Test) table: Open-circuit voltage (Voc/V) 53.50 to 54.00 |
| Isc STC | 15.01-15.41 A | Electrical Performance Parameters (STC Test) table: Short circuit current (Isc/A) 15.01 to 15.41 |


Recorded gaps:

- Named diesel-solar hybrid installation for a remote oil & gas platform/plant with PV MW, diesel MW and fuel-saving figure — Fetch an operator/OEM hybrid-power case study with numeric capacity and diesel displacement
- Onshore solar capacity at a named gas processing plant — Locate and fetch a gas-plant PV project page

## chemical-dosing

### Boiler water chemical dosing (boiler-chemical-dosing)

Primary code: PWR: Power and renewables
After mechanical deaeration, chemically remove residual dissolved oxygen, maintain alkaline pH for magnetite passivation, neutralise CO2 acidity in condensate with volatile amines, condition residual hardness into removable sludge with phosphate/polymer/chelant, and inhibit foaming and caustic attack.
Vendors: Veolia Water Technologies & Solutions, Wilhelmsen, LANXESS (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Theoretical sodium sulphite demand | 7.88 ppm pure Na2SO3 per 1.0 ppm dissolved O2 | Veolia Water Handbook Ch.11 (2Na2SO3 + O2 → 2Na2SO4); practical ~10 lb/lb O2 with technical grade and losses |
| Spirax-design sodium sulphite dosing rate | 8 ppm per 1 ppm O2 + 4 ppm reserve; 45% active in liquid catalysed product ppm | Spirax Sarco worked example and dosing guidance |
| Sulphite/oxygen reaction rate | doubles per 18 °F temperature rise; rapid at >=212 °F; fastest at pH 8.5–10.0 °F / pH | Veolia Water Handbook Ch.11 |
| Catalysed vs uncatalysed sodium sulphite oxygen removal after 25 s contact | catalysed: complete; uncatalysed: <50% % of O2 removed | Veolia Water Handbook Ch.11, Figure 11-12 discussion |
| Hydrazine dosing ratio | theoretical 1.0 ppm per 1 ppm O2; practical 1.5–2.0 parts per part O2 ppm per ppm O2 | Veolia Water Handbook Ch.11; 35% solution with flash point >200 °F; decomposition begins ~400 °F, rapid at 600 °F; optimum pH 9.0–10.0 |
| Sulphite vs organic scavenger pressure split | sulfite below 900 psig (62 barg); organic DEHA/carbohydrazide above 900 psig (62 barg) psig / barg | Veolia feedwater-treatment-chemicals product page; Ch.11 states sulfite typically below 1000 psig and hydrazine/organic at 1000 psig and above |
| Boiler-water sulphite residual | 30 to 70 (shell) / 60 to 100 (coil) ppm | CEA BG04 Table 2 |
| Boiler-water tannin / ascorbic acid / DEHA / filming amine residual | tannin 120–160 shell; ascorbic acid 15–30; DEHA 0.1–1.0 in feedwater; film-forming amines 0.2–1.0 in feedwater ppm | CEA BG04 Table 2 |
| Boiler-water phosphate residual | 30 to 60 (shell) / 30 to 70 (coil) ppm | CEA BG04 Table 2; notes 9–10: phosphate reserve not essential if carbonate alkalinity >=250 ppm; phosphate should not exceed 10% of minimum caustic alkalinity; chelant max 10 ppm |
| Caustic alkalinity as fraction of TDS under phosphate conditioning | 10-15 % of dissolved solids | CEA BG04 Table 2 note 8 |
| Silica-to-caustic-alkalinity ratio to prevent silicate scale | <0.4:1 ratio | CEA BG04 Table 2 note 11 |
| Boiler-water pH for magnetite film | 10.5 to 12.0 pH units | Spirax Sarco (BS 2486 recommendation for shell boilers at 10 bar; higher pH only in higher-pressure boilers); CEA BG04 Table 2 boiler-water shell 10.5–12.0 at 25 °C |
| Feedwater pH for corrosion control | not less than 8.5 to 9 pH units | Spirax Sarco Pressurised Deaerators: lowest level at which CO2 is absent |
| Low-pressure hot-water boiler treatment | 200–400 ppm P-alkalinity; sodium sulfite + pH adjustment + polymer dispersant ppm | Veolia Water Handbook Ch.11, Low-Pressure Steam and Hot Water Heating Systems |
| Lay-up sulphite reserve | 150 ppm (<48 h); >250 ppm (48 h–7 d); >500 ppm (7 d–1 month); pH 10–11.5 for up to one month ppm as sulphite / pH | CEA BG04 §8 idle boilers |
| FDA food-contact approval | 21 CFR 173.310 regulation | Veolia states many Solus/OptiSperse products approved where steam may contact food; Steamate FM1007 OMRI-listed |
| Feed pressure | ?-3,600 psi | Printed as 'Up to 3,600 psi feed pressures' under Chemical Feed Skid Capabilities |
| Feed rate | ?-2,200 gallon/hour | Printed as 'Up to 2,200 gallon/hour feed rate' on same page |
| Pump types | solenoid, peristaltic or hydraulically driven n/a | Printed under Chemical Feed Skid Capabilities |
| Frame materials | painted carbon steel; stainless steel; non-metallic n/a | Printed under Chemical Feed Skid Capabilities |
| Piping materials | PVC; CPVC; stainless steel (tubing or welded); Alloy 20; PVDF n/a | Printed under Chemical Feed Skid Capabilities |


Recorded gaps:

- Exact amine dosing rates (morpholine, cyclohexylamine, MEA) in ppm per ppm CO2 for HRSG — Retry TP1206EN via alternate host or fetch a Veolia Steamate NA series product bulletin with feed-rate basis
- Hydrazine replacement/DEHA dosing limits in modern gas-fired HRSGs — Fetch GE Vernova or Siemens HRSG water-chemistry manual excerpt
- Cost data with dollar year — Fetch the linked PDF case studies and record currency and dollar year before adding any cost figure

### SCR reagent systems (ammonia/urea storage, dosing, injection grids; ammonium sulfate/bisulfate in HRSGs) (scr-reagent-system)

Primary code: PWR: Power and renewables
Store and deliver aqueous ammonia (or anhydrous ammonia / urea) to an ammonia injection grid (AIG) upstream of the SCR catalyst; tuning of AIG distribution controls NOx removal, ammonia slip and downstream ammonium bisulfate (ABS) / ammonium sulfate (AS) deposition on air-preheater or HRSG tube surfaces. Flow-correction devices (turning vanes, static mixers, graduated straightening grids) and CFD are used to obtain uniform NH3/NOx distribution.
Vendors: Concord Environmental, Fuel Tech, John Zink (Koch Engineered Solutions), Cleaver-Brooks, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Aqueous ammonia concentration and injection rate at a 2x1 combined cycle | 28% aqueous solution, 150 lb/hr wt% and lb/hr | At plant design operating conditions for HRSG SCR; W501FC+ gas turbines, gas-only full-load rating 480 MW at 120 F/15% RH |
| HRSG module gas-side pressure drop before/after dry-ice cleaning | 2.1-6.8 inches H2O (clean condition 2.1; rises to 6.8 or more) | Module 5 (LP evaporator, IP economiser, HP economiser) of each HRSG; fouling attributed to ammonium bisulfate deposition; ~5 in H2O increase cost about 1-1.5 MW output |
| Storage vessel capacity | ?-65,000 gallons | Printed under 'Storage System Module': 'Vessel storage up to 65,000 gallons' |
| Storage vessel construction | single & double wall carbon steel vessels n/a | Printed under Storage System Module |
| Anhydrous vaporizer | Integraheat Electric Vaporizer ASME Code Stamped (locally mounted) n/a | Printed under Distribution System Module (Anhydrous) |
| Vessel code | ASME Section VIII, National Board Registered n/a | Printed under Industry Standards |
| Piping design code | ANSI B31.1 / ANSI B31.3 n/a | Printed under Industry Standards |
| Pipe fabrication code | ASME Section IX n/a | Printed under Industry Standards |
| Structural steel assembly code | AWS D1.1 n/a | Printed under Industry Standards |
| System design standard | API RP 550 & K61.1 n/a | Printed under Industry Standards |
| Hazardous location option | Class 1, Div 2 n/a | Printed under Optional Features |


Recorded gaps:

- Urea-to-NOx stoichiometry, urea storage/dosing equipment details and urea SCR vendor scope not found in fetched pages — Fetch a urea-SCR OEM datasheet (e.g. fuel/chemical dosing skid vendor) with explicit kg urea/kg NOx basis.
- Ammonium sulfate concerns in gas-fired HRSGs specifically (as opposed to coal air preheaters) only partly evidenced — Find HRSG-specific catalyst SO2/SO3 conversion and ABS dew-point guidance for gas turbine exhaust with low sulfur.
- No reagent storage tank sizes, material specifications or safety distances evidenced — Fetch an ammonia storage/delivery system datasheet or CCJ 'Ammonia delivery mod' best-practice article.

## chiller

### Waste-heat recovery from gas engines: absorption chillers, heat exchangers, hot water; CHP for data centres (gas-engine-waste-heat-chiller)

Primary code: PWR: Power and renewables
Waste-heat recovery from gas engines: absorption chillers, heat exchangers, hot water; CHP for data centres
Vendors: Thermax, Johnson Controls (YORK, Silent-Aire), Carrier (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Thermax exhaust-gas absorption chiller capacity | 50-3000 TR (refrigeration tons) | Thermax Exhaust Gas-Driven Absorption Chiller-Heater technical data; page header also states 30 TR to 3000 TR / 100 kW to 9 MW |
| Thermax exhaust-gas absorption chiller COP | 1.53 COP (cooling) | Thermax product page: cooling COP up to 1.53; up to 40% heating-energy savings and 20% water savings claimed |
| Thermax exhaust temperature and output temperatures | Exhaust 250-600 C; chilled water -5 to 35 C; hot water up to 110 C deg C | Thermax product page technical data; double-effect design based on exhaust temperature; LiBr-water solution |
| Inlet diameter | 2-12 inch | Product page Design section |
| Casing diameter | 8-24 inch | Product page Design section |
| Standard design temperature | 250 deg C | Product page Design section |
| Enhanced noise attenuation | ?-50+ dB | Product page: 'Typical acoustic performance (no guaranteed noise attenuation)' |
| Capacity | 50-3000 TR (table); header states 30-3000 TR | Value as printed in the cited source; no further qualifier stated. |
| Cooling COP | 1.53 up to | Value as printed in the cited source; no further qualifier stated. |
| Exhaust temperature | 250-600 deg C | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Measured COP and heat-recovery rate for absorption chillers coupled specifically to a named gas engine model at a data centre — Request thermodynamic datasheet from engine OEM and chiller vendor for a specific engine exhaust mass flow/temperature
- Thermax capacity discrepancy (30-3000 TR header vs 50-3000 TR table) — Query Thermax for a certified capacity table; do not choose either value silently

## ci-system

### Analysers (ci-analysers-gas-and-liquid-35ae64)

Primary code: UPS: Upstream
Online composition and quality measurement for process and emissions monitoring.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product families attested by catalogue | Gas Analyzers, Liquid Analyzers, Analyzer System; Advanced Analytical Instrument Management System (AMADAS) families | Yokogawa product catalogue navigation |


### Analysers (ci-analysers-gas-and-liquid)

Primary code: UPS: Upstream
Online composition and quality measurement for process and emissions monitoring.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product families attested by catalogue | Gas Analyzers, Liquid Analyzers, Analyzer System; Advanced Analytical Instrument Management System (AMADAS) families | Yokogawa product catalogue navigation |


### Calibration and field device management (ci-calibration-and-field-device-management)

Primary code: UPS: Upstream
Configuration, calibration, proof testing and asset management of field instruments across their lifecycle.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| tool types attested | Pressure Calibrators, Device Smart Communicators, FieldMate, Plant Resource Manager (PRM), Field Asset Analytics (InsightSuiteAE) tools | Yokogawa product catalogue navigation |
| temporary masters on FOUNDATION Fieldbus | handheld field communicators, laptops/tablets, documenting calibrators tool types | FieldComm Group Foundation Fieldbus page |


### Control valves and actuators (ci-control-valves-and-actuators)

Primary code: UPS: Upstream
Final control elements modulating or isolating process flow, driven by pneumatic/electric/hydraulic actuators; safety-rated versions used in ESD.
Vendors: Fisher (Emerson) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Final control elements modulating or isolating process flow, driven by pneumatic/electric/hydraulic actuators; safety-rated versions used in ESD. | Qualitative function from pages read in this sweep. |


### Data historians / edge computing / digital twin / IIoT (ci-data-historians-edge-computing-digital-twin-iiot)

Primary code: UPS: Upstream
Time-series data capture, edge analytics, process digital twins and IIoT connectivity for optimisation and remote operations.
Vendors: Yokogawa Electric, Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| offering attested | Data Historian; Plant Information Management System; Process Data Analytics; OpreX Intelligent Manufacturing Hub; process digital twin for LNG plants and for oil & gas upstream; Intelligent Edge Controllers (A8) offerings | Yokogawa product/solutions catalogue navigation |


### Field transmitters (ci-field-transmitters-pressure-temperature-flow-level-82501c)

Primary code: UPS: Upstream
Primary measurement instruments converting process variables to standard analog/digital signals for control and safety.
Vendors: Yokogawa Electric, Emerson (duplex stainless steel option on Roxar 2600, page read) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product families attested by catalogue | Pressure Transmitters, Flowmeters, Temperature Transmitters, Level Meters, Pressure Calibrators, Valve Manifolds families | Yokogawa product catalogue navigation (measured/field instruments and components) |
| HART device family specifications | Temperature (HCF_SPEC-160-04), Pressure (HCF_SPEC-160-05), Level and PID Control families specifications | HART Protocol Specifications - Device Families Command Specification HCF_SPEC-160 Rev.3.0 |


### Field transmitters (ci-field-transmitters-pressure-temperature-flow-level)

Primary code: UPS: Upstream
Primary measurement instruments converting process variables to standard analog/digital signals for control and safety.
Vendors: Yokogawa Electric, Emerson (duplex stainless steel option on Roxar 2600, page read) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product families attested by catalogue | Pressure Transmitters, Flowmeters, Temperature Transmitters, Level Meters, Pressure Calibrators, Valve Manifolds families | Yokogawa product catalogue navigation (measured/field instruments and components) |
| HART device family specifications | Temperature (HCF_SPEC-160-04), Pressure (HCF_SPEC-160-05), Level and PID Control families specifications | HART Protocol Specifications - Device Families Command Specification HCF_SPEC-160 Rev.3.0 |
| Reference accuracy | up to 0.075 (Standard) / up to 0.055 (Platinum) % | 'Reference Accuracy: Standard: up to 0.075 %; Platinum: up to 0.055 %' |
| Measuring cell | 400 mbar-400 bar mbar / bar (6 psi...6,000 psi) | 'Measuring cell: 400 mbar...400 bar (6psi...6,000psi)' |
| Process temperature | -40-125 deg C standard; diaphragm seal -70...+400 deg C | 'Process temperature: Standard: -40°C…+125°C; Diaphragm seal: -70°C...+400°C' |
| Ambient temperature | -40-85 deg C | 'Ambient temperature: -40°C...+85°C (-40°F...+185°F)' |
| Supply voltage | 10.5-35 V DC (Ex d, Ex e, non-Ex); Ex i 10.5...30 V DC | 'Ex d, Ex e, non-Ex: 10.5...35V DC; Ex i: 10.5...30V DC' |
| Max. turn down | 100:1 ratio | 'Max. Turn down: 100:1' |
| Smallest calibratable span | 20 mbar (0.3 psi) | 'Smallest calibratable span: 20 mbar (0.3 psi)' |
| Communication | 4...20 mA, 4...20 mA HART, PROFINET with Ethernet-APL, Bluetooth wireless (optional) protocol | 'Communication' field in specification table |
| Safety approvals | SIL approval | 'Safety approvals: SIL' |
| Design approvals | EN 10204-3.1, NACE MR0175, NACE MR0103 approval | 'Design approvals' field in specification table |
| Reference accuracy | up to 0.05 (Standard) / up to 0.025 (Platinum) % | 'Reference Accuracy: Standard: up to 0.05 %; Platinum: up to 0.025 %' |
| Pressure measuring range / measuring cell | 400 mbar-700 bar mbar / bar (6 psi...10,500 psi) | 'Measuring cell: 400 mbar...700 bar (6 psi...10,500 psi)' |


### FOUNDATION Fieldbus (ci-foundation-fieldbus)

Primary code: UPS: Upstream
All-digital fieldbus for process automation with multivariable measurement, device diagnostics, control-in-the-field and integration of wireless devices.
Vendors: FieldComm Group (specification owner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| cable / power | two-wire twisted pair cable; intrinsically safe or non-incendive device power suitable for all hazardous areas wiring | FieldComm Group Foundation Fieldbus page |
| registered interoperable products | 1000 products (over) | FieldComm Group 'FOUNDATION Technology Explained': 'over 1,000 registered products' interoperate across manufacturers |
| control architecture | Control-in-the-field (CIF): field instruments can communicate directly during host system failure to maintain safe operations architecture | FieldComm Group Foundation Fieldbus page |
| data rate | H1: 31.25 kbit/s (NOT confirmed on fetched page - record as gap) kbit/s | Not stated on fetched FieldComm overview page |


### Gas detectors and flame detectors (ci-gas-detectors-and-flame-detectors)

Primary code: UPS: Upstream
Fixed and portable detection of combustible/toxic gas and flame, interfaced to fire & gas systems and SIS.
Vendors: MSA, Honeywell Analytics, Dräger (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| gas/flame detection effectiveness guidance | ISA-TR84.00.07-2026: Guidance on the Evaluation of Fire, Combustible Gas, and Toxic Gas System Effectiveness - covers detection coverage, response times and system reliability technical report | ISA-84 Standards page |


### HART (ci-hart-wired-4-20-ma-digital-protocol-171e8a)

Primary code: UPS: Upstream
Bi-directional digital communication over 4-20 mA analog current loops connecting field instruments to control/monitoring systems; preserves analog wiring while exposing diagnostics.
Vendors: FieldComm Group (specification owner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| installed base | 40000000 field instruments | FieldComm Group HART page: 'over 40 million field instruments supporting HART technology installed worldwide' |
| physical medium | 4-20 mA analog current loops; instrumentation-grade wiring and standard terminations signal | FieldComm Group HART technology page |
| specification kit size | 17 documents | HART Protocol Specifications Kit is a collection of 17 documents |
| standards status | IEC standard; three major revisions with backward compatibility standard | FieldComm Group HART page |


### HART (ci-hart-wired-4-20-ma-digital-protocol)

Primary code: UPS: Upstream
Bi-directional digital communication over 4-20 mA analog current loops connecting field instruments to control/monitoring systems; preserves analog wiring while exposing diagnostics.
Vendors: FieldComm Group (specification owner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| installed base | 40000000 field instruments | FieldComm Group HART page: 'over 40 million field instruments supporting HART technology installed worldwide' |
| physical medium | 4-20 mA analog current loops; instrumentation-grade wiring and standard terminations signal | FieldComm Group HART technology page |
| specification kit size | 17 documents | HART Protocol Specifications Kit is a collection of 17 documents |
| standards status | IEC standard; three major revisions with backward compatibility standard | FieldComm Group HART page |


### Industrial Wi-Fi / 4G / 5G / private LTE (ci-industrial-wi-fi-4g-5g-private-lte)

Primary code: UPS: Upstream
Higher-bandwidth wireless backhaul and mobile connectivity for plant and offshore platforms.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Higher-bandwidth wireless backhaul and mobile connectivity for plant and offshore platforms. | Qualitative function from pages read in this sweep. |


### Instrument cabling, junction boxes, instrument air and impulse lines (ci-instrument-cabling-junction-boxes-instrument-air-and-impulse-l)

Primary code: UPS: Upstream
Physical signal/power cabling, field junction boxes, pneumatic supply and impulse tubing connecting instruments to ICSS.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fieldbus wiring | FOUNDATION Fieldbus uses two-wire twisted pair cable; intrinsically safe or non-incendive device power suitable for all hazardous areas cabling | FieldComm Group Foundation Fieldbus page |
| wireless vs wired installation | No additional instrument wiring needed for WirelessHART; 30%-60% lower installation cost claimed vs adding traditional wired instruments % cost reduction | FieldComm Group WirelessHART page |
| related Yokogawa components | Valve Manifolds, Current to Pneumatic Converter, Signal Conditioners, Surge Arresters, Network Converters, Multi-Sensing Remote I/O components | Yokogawa product catalogue navigation |


### Integrated Control and Safety System (ci-integrated-control-and-safety-system-icss-dcs-1bd06b)

Primary code: UPS: Upstream
Integrated process control and safety platform for offshore and onshore plants; unifies control, safety, monitoring and enterprise data.
Vendors: Honeywell, Siemens, Yokogawa Electric, ABB (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Honeywell installed base - refineries | 45 % of refineries | Honeywell Process Automation overview: '45% Of Refineries' |
| Honeywell installed base - ammonia | 30 % of ammonia production | Honeywell Process Automation overview: '30% Ammonia Production' |
| Honeywell O&G processing plants | 500 plants (over) | Honeywell overview: '>500 O&G Processing Plants' |
| Honeywell LNG liquefaction trains | 86 trains | Honeywell overview: '86 Liquefacation trains' |
| Honeywell LNG carriers/FSRU | 221 vessels (221+) | Honeywell overview: '221+ TLNG carriers/ FSRU vessels' |
| Siemens PCS 7 version / cybersecurity | V10.0; NIS2-compliant; full IEC 62443-4-1 and IEC 62443-3-3 compliance standard/version | Siemens SIMATIC PCS 7 product page (fetched 2026-11-18) |
| Siemens MTP startup improvement | 75 % (up to) | Siemens PCS 7 page: 'MTP integration for up to 75% faster startup' |
| Siemens high-availability I/O | SIMATIC ET 200SP HA compact robust remote I/O designed for high availability product | Siemens PCS 7 product page |
| Siemens installed base | in use in thousands of installations worldwide installations | Siemens PCS 7 product page |


### Integrated Control and Safety System (ci-integrated-control-and-safety-system-icss-dcs)

Primary code: UPS: Upstream
Integrated process control and safety platform for offshore and onshore plants; unifies control, safety, monitoring and enterprise data.
Vendors: Honeywell, Siemens, Yokogawa Electric, ABB (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Honeywell installed base - refineries | 45 % of refineries | Honeywell Process Automation overview: '45% Of Refineries' |
| Honeywell installed base - ammonia | 30 % of ammonia production | Honeywell Process Automation overview: '30% Ammonia Production' |
| Honeywell O&G processing plants | 500 plants (over) | Honeywell overview: '>500 O&G Processing Plants' |
| Honeywell LNG liquefaction trains | 86 trains | Honeywell overview: '86 Liquefacation trains' |
| Honeywell LNG carriers/FSRU | 221 vessels (221+) | Honeywell overview: '221+ TLNG carriers/ FSRU vessels' |
| Siemens PCS 7 version / cybersecurity | V10.0; NIS2-compliant; full IEC 62443-4-1 and IEC 62443-3-3 compliance standard/version | Siemens SIMATIC PCS 7 product page (fetched 2026-11-18) |
| Siemens MTP startup improvement | 75 % (up to) | Siemens PCS 7 page: 'MTP integration for up to 75% faster startup' |
| Siemens high-availability I/O | SIMATIC ET 200SP HA compact robust remote I/O designed for high availability product | Siemens PCS 7 product page |
| Siemens installed base | in use in thousands of installations worldwide installations | Siemens PCS 7 product page |


### ISA100.11a (ci-isa100-11a-industrial-wireless-c7641c)

Primary code: UPS: Upstream
Wireless systems for industrial automation: process control and related applications, from non-critical monitoring to supervisory and closed-loop control.
Vendors: ISA / ISA100 Wireless Compliance Institute (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| standard designation | ISA-100.11a-2011, Wireless Systems for Industrial Automation: Process Control and Related Applications standard | ISA-100 Series of Standards page |
| data rate class | low-data-rate wireless communication qualitative | ISA-100.11a key focus areas |
| application scope | monitoring, supervisory control, open-loop and closed-loop control; oil and gas listed as applicable industry scope | ISA-100 standards page, 'Versatility for Critical and Non-Critical Applications' |
| supporting technical reports | ISA-TR100.14.01 trustworthiness; ANSI/ISA-TR100.15.01-2012 backhaul architecture over untrusted/trusted networks; ISA-TR100.20.01-2017 common network management documents | ISA-100 Series of Standards page |


### ISA100.11a (ci-isa100-11a-industrial-wireless)

Primary code: UPS: Upstream
Wireless systems for industrial automation: process control and related applications, from non-critical monitoring to supervisory and closed-loop control.
Vendors: ISA / ISA100 Wireless Compliance Institute (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| standard designation | ISA-100.11a-2011, Wireless Systems for Industrial Automation: Process Control and Related Applications standard | ISA-100 Series of Standards page |
| data rate class | low-data-rate wireless communication qualitative | ISA-100.11a key focus areas |
| application scope | monitoring, supervisory control, open-loop and closed-loop control; oil and gas listed as applicable industry scope | ISA-100 standards page, 'Versatility for Critical and Non-Critical Applications' |
| supporting technical reports | ISA-TR100.14.01 trustworthiness; ANSI/ISA-TR100.15.01-2012 backhaul architecture over untrusted/trusted networks; ISA-TR100.20.01-2017 common network management documents | ISA-100 Series of Standards page |


### Multiphase meters (ci-multiphase-meters)

Primary code: UPS: Upstream
Measurement of oil/water/gas flow rates without full separation, used in wellhead and subsea/onshore applications.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Measurement of oil/water/gas flow rates without full separation, used in wellhead and subsea/onshore applications. | Qualitative function from pages read in this sweep. |


### OT cybersecurity (ci-ot-cybersecurity)

Primary code: UPS: Upstream
Security of industrial automation and control systems (IACS) across the lifecycle for offshore/onshore ICSS and SCADA.
Vendors: ISA / ISAGCA / ISCI (ISASecure), Yokogawa Electric, Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| standard family | ISA/IEC 62443 (world's only consensus-based IACS cybersecurity standard series); IEC recognised it as a horizontal standard in 2021; endorsed by the United Nations standard | ISA/IEC 62443 Series of Standards page |
| key parts | 62443-2-1:2024 (asset owners), 62443-3-2:2020 (risk assessment), 62443-3-3:2013 (system security requirements and security levels), 62443-4-1:2018 (secure product development), 62443-4-2:2018 (component technical requirements) standards | ISA/IEC 62443 page |
| ISAGCA membership | 50-? member companies (more than) | ISA/IEC 62443 page: 'more than 50 member companies representing more than $1.5 trillion in aggregate revenue across more than 2,400 combined locations' and '31 different industries' |
| Siemens PCS 7 cybersecurity | NIS2-compliant cybersecurity; IEC 62443-4-1 and IEC 62443-3-3 compliance; secure communication protocols and centralised Microsoft update deployment compliance | Siemens SIMATIC PCS 7 product page |


### PLC / RTU / edge controllers (ci-plc-rtu-edge-controllers)

Primary code: UPS: Upstream
Local control and remote telemetry/IO for onshore well sites and offshore modules.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| product families attested | Programmable Logic Controllers (PLC/PAC), Process Control PLC/RTU, Intelligent Edge Controllers (A8), Single Loop Controllers families | Yokogawa product catalogue navigation |


### Profibus / Modbus (ci-profibus-modbus-fieldbus-and-serial-protocols-620677)

Primary code: UPS: Upstream
Wired digital field and host communication protocols commonly used in ICSS/SIS/PLC environments.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Wired digital field and host communication protocols commonly used in ICSS/SIS/PLC environments. | Qualitative function from pages read in this sweep. |


### Profibus / Modbus (ci-profibus-modbus-fieldbus-and-serial-protocols)

Primary code: UPS: Upstream
Wired digital field and host communication protocols commonly used in ICSS/SIS/PLC environments.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Wired digital field and host communication protocols commonly used in ICSS/SIS/PLC environments. | Qualitative function from pages read in this sweep. |


### Safety Instrumented System (ci-safety-instrumented-system-sis-esd-fire-gas-0765e4)

Primary code: UPS: Upstream
Independent safety layer that detects hazardous conditions and drives the process to a safe state; ESD and fire & gas are core SIFs on offshore and onshore facilities.
Vendors: Yokogawa Electric, Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| functional safety standard (process industry) | ANSI/ISA-61511-1-2018 / IEC 61511-1:2016+AMD1:2017 CSV standard | ISA-84 Standards page: defines SIS lifecycle framework and performance targets based on Safety Integrity Levels (SIL) |
| SIL determination guidance | ANSI/ISA-61511-3-2018 / IEC 61511-3:2016 - guidance for determination of required SIL; covers tolerable risk and methodologies standard | ISA-84 Standards page |
| SIL verification | ISA-TR84.00.02-2022: SIL Verification of Safety Instrumented Functions - random and systematic failures, spurious trip rates, failure probabilities technical report | ISA-84 Standards page |
| wireless in non-SIS protection layers | ISA-TR84.00.08-2017: Guidance for Application of Wireless Sensor Technology to Non-SIS Independent Protection Layers technical report | ISA-84 Standards page |
| safety lifecycle scope | design, installation, operation, maintenance, decommissioning; plus ISA-TR84.00.09-2024 cybersecurity related to the safety lifecycle scope | ISA-84 Standards page |


### Safety Instrumented System (ci-safety-instrumented-system-sis-esd-fire-gas)

Primary code: UPS: Upstream
Independent safety layer that detects hazardous conditions and drives the process to a safe state; ESD and fire & gas are core SIFs on offshore and onshore facilities.
Vendors: Yokogawa Electric, Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| functional safety standard (process industry) | ANSI/ISA-61511-1-2018 / IEC 61511-1:2016+AMD1:2017 CSV standard | ISA-84 Standards page: defines SIS lifecycle framework and performance targets based on Safety Integrity Levels (SIL) |
| SIL determination guidance | ANSI/ISA-61511-3-2018 / IEC 61511-3:2016 - guidance for determination of required SIL; covers tolerable risk and methodologies standard | ISA-84 Standards page |
| SIL verification | ISA-TR84.00.02-2022: SIL Verification of Safety Instrumented Functions - random and systematic failures, spurious trip rates, failure probabilities technical report | ISA-84 Standards page |
| wireless in non-SIS protection layers | ISA-TR84.00.08-2017: Guidance for Application of Wireless Sensor Technology to Non-SIS Independent Protection Layers technical report | ISA-84 Standards page |
| safety lifecycle scope | design, installation, operation, maintenance, decommissioning; plus ISA-TR84.00.09-2024 cybersecurity related to the safety lifecycle scope | ISA-84 Standards page |


### Satellite and microwave link and radio telemetry (ci-satellite-and-microwave-link-and-radio-telemetry)

Primary code: UPS: Upstream
Long-haul offshore-to-shore and remote telemetry backhaul for platforms and onshore wells.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Long-haul offshore-to-shore and remote telemetry backhaul for platforms and onshore wells. | Qualitative function from pages read in this sweep. |


### Telemetry & SCADA / remote monitoring (ci-telemetry-scada-remote-monitoring)

Primary code: UPS: Upstream
Remote acquisition and supervision of dispersed onshore wells/pipelines and offshore assets.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| telemetry/wide-area products attested | Wide Area Monitoring System; Multi-Sensing Remote I/O; Wireless Data Acquisition (920 MHz); Data Connectivity; Integrated Operations Center (IOC) for efficient remote plant operations products/solutions | Yokogawa product/solutions catalogue navigation |
| Honeywell SCADA | Honeywell offers advanced SCADA alongside Experion PKS, bridging operations and strategy offering | Honeywell Process Automation overview page |


### WirelessHART (ci-wirelesshart-industrial-wireless-mesh-024e52)

Primary code: UPS: Upstream
Wireless field instrumentation communications for process automation; mesh networking adds redundant routes in difficult radio environments of process facilities. Applicable offshore and onshore.
Vendors: FieldComm Group (specification owner), Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| wireless mesh topology | Each device can act as a router; redundant communication routes extend range and improve reliability topology | FieldComm Group WirelessHART technology page, descriptive claim |
| installation cost reduction vs wired instruments | 30-60 % | FieldComm Group WirelessHART page citing WirelessHART User Case Studies: '30%-60% lower installation costs than adding traditional wired instruments' |
| RF physical layer | 2.4 GHz DSSS O-QPSK, based on IEEE STD 802.15.4-2006 2.4GHz DSSS Physical Layer GHz / modulation | HART Protocol Specifications: 2.4GHz DSSS O-QPSK Physical Layer Specification (HCF_SPEC-65 FCG TS20065) Rev. 1.1 |
| MAC / DLL | TDMA Data-Link Layer over IEEE 802.15.4-2006 PHY; secure, reliable, error-free mesh communication protocol | HCF_SPEC-75 FCG TS20075 Rev. 1.2 (TDMA Data-Link Layer) |
| messaging modes | one-way publishing, exception notification, ad-hoc request/response, auto-segmented block transfers modes | FieldComm Group WirelessHART technology page |
| Data reliability | >99-? % | Page states 'over 99% data reliability' for WirelessHART (IEC 62591) mesh; also 'delivering over 99% data reliability even in environments with interference, extreme temperatures, or physical obstructions' |
| WirelessHART standard | IEC 62591 standard | 'WirelessHART® is the global industry standard (IEC 62591) for process automation wireless' |
| Encryption | AES-128 encryption | 'AES-128 encryption on every message' under 'How is industrial wireless secured against cyber threats?' |
| Host protocols | HART-IP, OPC UA, Modbus TCP protocol | 'Wireless field devices send data over a secure self-organizing mesh network to a gateway, which translates that data into protocols your DCS, PLC, or SCADA already understands such as HART-IP, OPC UA, and Modbus TCP' |
| Installation cost saving vs wired instrumentation | ?-60 % lower | 'Up to 60% lower installation costs vs. traditional wired instrumentation' under 'What ROI can I expect' |
| Payback period | 12-24 months | 'Most industrial wireless deployments deliver payback within 12 to 24 months' |
| Example wireless gateway models | 1410S1, 1410S2 model | 'Emerson Wireless Gateway to aggregate data and connect to your host system (1410S1 or 1410S2)' in tank-level deployment FAQ |
| Hazardous-area certifications | FM, CSA, ATEX, IECEx certification | 'Emerson offers devices certified for use in intrinsically safe and explosion-proof areas under FM, CSA, ATEX, and IECEx standards' |
| WirelessHART mesh installation cost saving vs wired instruments | 30-60 % lower installation costs | Quoted on the WirelessHART technology page from the 'WirelessHART User Case Studies - web publishing' brochure: 'WirelessHART offers 30%-60% lower installation costs than adding traditional wired instruments' |
| WirelessHART radio technology | self-organizing, self-healing mesh; each device can route for other devices  qualitative | As printed on the page: 'By design, WirelessHART using mesh networking technology' and 'a device doesn't have to communicate directly to a gateway, but just forward its message to the next closest device' |
| WirelessHART mesh installation cost saving vs wired instruments | 30-60 % lower installation costs | Quoted on the WirelessHART technology page from the 'WirelessHART User Case Studies - web publishing' brochure: 'WirelessHART offers 30%-60% lower installation costs than adding traditional wired instruments' |
| WirelessHART radio technology | self-organizing, self-healing mesh; each device can route for other devices  qualitative | As printed on the page: 'By design, WirelessHART using mesh networking technology' and 'a device doesn't have to communicate directly to a gateway, but just forward its message to the next closest device' |


### WirelessHART (ci-wirelesshart-industrial-wireless-mesh)

Primary code: UPS: Upstream
Wireless field instrumentation communications for process automation; mesh networking adds redundant routes in difficult radio environments of process facilities. Applicable offshore and onshore.
Vendors: FieldComm Group (specification owner), Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| wireless mesh topology | Each device can act as a router; redundant communication routes extend range and improve reliability topology | FieldComm Group WirelessHART technology page, descriptive claim |
| installation cost reduction vs wired instruments | 30-60 % | FieldComm Group WirelessHART page citing WirelessHART User Case Studies: '30%-60% lower installation costs than adding traditional wired instruments' |
| RF physical layer | 2.4 GHz DSSS O-QPSK, based on IEEE STD 802.15.4-2006 2.4GHz DSSS Physical Layer GHz / modulation | HART Protocol Specifications: 2.4GHz DSSS O-QPSK Physical Layer Specification (HCF_SPEC-65 FCG TS20065) Rev. 1.1 |
| MAC / DLL | TDMA Data-Link Layer over IEEE 802.15.4-2006 PHY; secure, reliable, error-free mesh communication protocol | HCF_SPEC-75 FCG TS20075 Rev. 1.2 (TDMA Data-Link Layer) |
| messaging modes | one-way publishing, exception notification, ad-hoc request/response, auto-segmented block transfers modes | FieldComm Group WirelessHART technology page |


## civ-civil

### Blast-resistant walls, blast doors and windows (civ-blast-resistant-walls-blast-doors-and-windows)

Primary code: PWR: Power and renewables
Protect personnel and equipment from accidental or intentional explosion by reinforced concrete/steel barriers and rated doors/glazing designed for specified peak reflected pressure, impulse and standoff.
Vendors: SDI Certified Manufacturers, Pillar Consulting Group, BakerRisk (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Blast design standards | ACI 370R-14 / UFC 3-340-02 / ASCE 2025 3rd ed / PIP STC01018 standards | SDI 133-26 lists blast test methods and design criteria: ASTM F2927-21 doors, ASTM F2912-17 glazing, ASTM F1642-17, GSA-TS01-2003, ASCE 2025 3rd edition, PIP STC01018-2014, UFC 4-010-01 2018 |
| Sample blast design criteria (non-DoD door) | 4 psi peak reflected pressure, 100 ms duration, 50% rebound psi / ms / % | SDI 133-26 sample criteria: 3 ft x 7 ft door and frame, seated in frame, welded to steel subframe, Category II response, ASTM F2927-21 |
| Sample DoD criteria | Charge Weight II, 250 ft standoff, Medium level of protection category / ft / level | SDI 133-26 sample DoD blast quote request form referencing UFC 4-010-01 12 Dec 2018 |


Recorded gaps:

- Blast wall thickness vs charge/standoff design tables — Fetch UFC 3-340-02 or TM 5-1300 public PDF from WBDG
- APAC blast-resistant building suppliers — Search APAC blast protection suppliers

### Bored cast-in-situ piles — Kelly, CFA, FDP, secant/c contiguous walls (civ-bored-cast-in-situ-piles-kelly-cfa-fdp-secant-c-contiguous-w)

Primary code: PWR: Power and renewables
Replace soil with a drilled, concreted cylindrical pile transferring load to deep bearing strata; also used contiguous/secant to form excavation support and groundwater cut-off walls. CFA concretes from bottom up through the hollow auger as it is withdrawn.
Vendors: BAUER Spezialtiefbau GmbH, Liebherr, BAUER Equipment Australia Pty Ltd (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Secant pile wall example | 880 mm diameter x 16 m deep mm x m | BAUER geotechnical solutions page, Businesspark Hannover Germany: secant pile wall with double-head drilling method |
| BAUER Seabed Drill current capability | 12 knots | BSD 3000 underwater drilling rig works in currents up to 12 knots, remotely operated via umbilicals |
| Liebherr LRB 23 operating weight | 72.6-78.5 t | Liebherr LRB 23 product page; max torque 300 kNm, crowd 320 kN, engine 600 kW, max pile length with slim vibrator 22.0 m |


Recorded gaps:

- CFA pile load-test acceptance criteria and integrity testing frequencies — Fetch EN 1997-1 / local code requirements on pile testing
- APAC CFA contractors with published diameter/depth ranges — Search APAC specialist contractors

### Driven precast piles (civ-driven-precast-piles-concrete-steel-h-steel-pipe)

Primary code: PWR: Power and renewables
Displacement piles installed by hammer or vibrator, transferring load by end bearing and shaft friction to deeper competent strata; used where soft near-surface soils overlie bearing layers.
Vendors: Liebherr, BAUER Maschinen GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Displacement piles installed by hammer or vibrator, transferring load by end bearing and shaft friction to deeper competent strata; used where soft near-surface soils overlie bearing layers. | Qualitative function from pages read in this sweep. |
| monopiles produced | >2,200 count | Value as printed in the cited source; no further qualifier stated. |
| projects supplied | >80 count | Value as printed in the cited source; no further qualifier stated. |
| IQ8 blow energy | >7,500 kJ | Value as printed in the cited source; no further qualifier stated. |
| total range | 30 to >7,500 kJ | Value as printed in the cited source; no further qualifier stated. |
| SW-series water depth | up to 2,000 m | Value as printed in the cited source; no further qualifier stated. |
| length | 120 m (up to) | Value as printed in the cited source; no further qualifier stated. |
| diameter | 11 m (up to) | Value as printed in the cited source; no further qualifier stated. |
| wall thickness | 160 mm (max) | Value as printed in the cited source; no further qualifier stated. |
| weight | 2,000 (prose) / >2,500 (tile) t | Value as printed in the cited source; no further qualifier stated. |
| diameter classes | 5-6 / 6-8 / 8-13 m (regular/XL/XXL) | Value as printed in the cited source; no further qualifier stated. |
| length | 20 to >120 m | Value as printed in the cited source; no further qualifier stated. |
| weight | 1,000-3,500 t | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Named driven-pile contractors and project case studies in APAC — Search and fetch project pages from APAC piling contractors
- Pile driving refusal/wave-equation numeric acceptance criteria — Fetch FHWA NHI-05-042 driven pile manual

### Formwork and shuttering (civ-formwork-and-shuttering-wall-column-slab-circular)

Primary code: PWR: Power and renewables
Temporary moulds that contain fresh concrete until it hardens; system formwork must resist fresh concrete pressure and meet surface finish tolerances (DIN 18202 / EN 13670 etc.).
Vendors: PERI GmbH, Doka (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Temporary moulds that contain fresh concrete until it hardens; system formwork must resist fresh concrete pressure and meet surface finish tolerances (DIN 18202 / EN 13670 etc.). | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Doka and MEVA formwork product specifications — Fetch Doka/MEVA product data sheets
- Slipform and precast/IBS system specifications for industrial structures — Search and fetch slipform/IBS system provider pages

### Ground improvement — stone columns, vibrocompaction, grouting (civ-ground-improvement-stone-columns-vibrocompaction-grouting)

Primary code: PWR: Power and renewables
Densify loose granular soils, reinforce soft cohesive soils, accelerate consolidation and mitigate liquefaction before placing foundations; includes vibro-replacement stone columns, vibro-compaction, dynamic compaction and permeation/compaction/jet grouting.
Vendors: Menard, BAUER Spezialtiefbau GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Densify loose granular soils, reinforce soft cohesive soils, accelerate consolidation and mitigate liquefaction before placing foundations; includes vibro-replacement stone columns, vibro-compaction, dynamic compaction and permeation/compac | Qualitative function from pages read in this sweep. |


Recorded gaps:

- APAC ground-improvement contractor names and completed projects — Search and fetch APAC specialist contractor project pages

### Heavy transport and installation — SPMT, jacking, skidding, cranes and rigging (civ-heavy-transport-and-installation-spmt-jacking-skidding-crane)

Primary code: PWR: Power and renewables
Move and set heavy equipment (reactors, columns, transformers, modules, vessel topsides) from laydown to foundation with precision, including self-propelled modular transporters, towed modular trailers, hydraulic jacking/skidding and crane lifts.
Vendors: TII SCHEUERLE, Cometto, Goldhofer AG, Barnhart Crane & Rigging (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Scheuerle SPMT axle load | 60 t per axle line | TII Scheuerle SPMT page: max 60 t axle load, 530 HP power, 700 mm axle compensation; 3–6 axle line modules; positioning accuracy +/-1–2 mm |
| Scheuerle SPMT platform payloads | 166.5-333.9 t | TII Scheuerle technical data: 3-axle 166.5 t, 4-axle 222.2 t, 5-axle 278.3 t, 6-axle 333.9 t; width 2430 mm |
| Scheuerle PPU outputs | 180-390 kW | TII Scheuerle: PPU Z180 180 kW (244 HP); PPU Z390 390 kW (530 HP); ePPU Z390 electric 320 kWh battery, 300 kW charging, 390 kW performance |
| Cometto MSPE axle load range | 48-70 t per axle line | Cometto MSPE product page: 48T, 60T, EVO3 70T families; up to 70 t/axle line, +/-135 deg electronic steering, 700 mm suspension stroke, bending moment 7250 kN.m standard / 9400 kN.m heavy duty |
| Goldhofer THP/SL axle load | 45 t at 1 km/h | Goldhofer THP/SL page: axle load 45 t at 1 km/h, axle compensation 600 mm, width 3000 mm, axle spacing 1500/1800 mm, max steering +/-55 deg, 2–8 axles, dead weight 13.85 t (4 axles) |
| SPMT world record load | 23000 t | TII Scheuerle success story: 23,000-tonne ship transported on 880 SCHEUERLE SPMT axle lines |
| SPMT convoy capacity | 25000 t (and beyond) | Cometto MSPE FAQ: modules combine lengthways and side-by-side, convoys up to 25,000 tons and beyond |
| Axle load max | 70 t | Value as printed in the cited source; no further qualifier stated. |
| Steering | ±135 deg | Value as printed in the cited source; no further qualifier stated. |
| Bending moment | 7250 / 9400 kNm | Value as printed in the cited source; no further qualifier stated. |
| Axle load | 60 t | Value as printed in the cited source; no further qualifier stated. |
| Axle compensation | 700 mm | Value as printed in the cited source; no further qualifier stated. |
| Positioning accuracy | ±1–2 mm | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Hydraulic jacking/skidding system capacities (e.g. Enerpac, Holmatro) and crane lift plans — Fetch Enerpac/Holmatro heavy-lift system data and Liebherr crawler crane load charts
- Rigging gear (slings, shackles, lifting beams) WLL tables — Fetch Crosby/Gunnebo rigging catalogue pages
- APAC heavy-lift contractors with published project data — Search APAC heavy-lift contractor case studies

### Micropiles (civ-micropiles)

Primary code: PWR: Power and renewables
Small-diameter drilled and grouted replacement piles carrying axial and/or lateral loads; used in restricted access, under existing structures, in hard rock and for seismic retrofit.
Vendors: BAUER Equipment Australia (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Small-diameter drilled and grouted replacement piles carrying axial and/or lateral loads; used in restricted access, under existing structures, in hard rock and for seismic retrofit. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Current live BAUER micropile product URL — Locate current BAUER micropile page on equipment.bauer.de

### Passive fire protection — intumescent coatings and fireproofing (civ-passive-fire-protection-intumescent-coatings-and-fireproofin)

Primary code: PWR: Power and renewables
Insulate structural steel, vessels, raceways and divisions from cellulosic and hydrocarbon fires to maintain load-bearing capacity for a specified rating (e.g. H-0/H-60/H-120, R30–R180, 1–4 hours).
Vendors: Carboline, Altex Coatings, IGSB (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Carboline Thermo-Lag 3000-P/SP solids content | 95 % by volume | Carboline product page and PDS: two-component epoxy intumescent fireproofing; tested UL 1709, UL 2431 Category I-A, ISO 834-3, IMO FTP Code (H-0/H-60/H-120), ASTM E84, ASTM E119, ISO 20340, NFPA 290 extended to 150 minutes |
| FRP fire protection | Tyfo CFP coating / Tyfo RR finish system | Fyfe FAQ: FRP does not reduce existing fire rating; no special protection for intermittent seismic/blast loads; Class 1/A flame & smoke per ASTM E84 may be needed for egress; Tyfo CFP for gravity-load cases |


Recorded gaps:

- Hydrocarbon jet-fire vs pool-fire DFT tables for specific section factors — Fetch full Thermo-Lag 3000 PDS/UL listing PDF via a browser that supports PDFs
- APAC fireproofing applicators and approvals — Search APAC fireproofing supplier pages

### Pile caps and pile-to-structure connections (civ-pile-caps-and-pile-to-structure-connections)

Primary code: PWR: Power and renewables
Rigid reinforced concrete blocks that distribute column/equipment loads to a pile group and tie piles together; include pile head connections, shear reinforcement and anchor/sole-plate interfaces.
Vendors: Fosroc (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Cementitious grout for baseplates (gap range) | 10-75 mm | Fosroc Conbextra GP product page: free-flow non-shrink cementitious grouting of gap thicknesses 10 to 75 mm; BS EN 1504-3 Class R4 and EN 1504-6 |


Recorded gaps:

- Pile cap punching shear / strut-and-tie design numeric examples — Fetch a public DOT or ACI pile cap design example

### Pipe racks, cable trays, access platforms, stairs, handrails, gratings (civ-pipe-racks-cable-trays-access-platforms-stairs-handrails-gra)

Primary code: PWR: Power and renewables
Provide supported routes for process piping and electrical/instrument cables and safe access/egress and working surfaces around pipe racks, vessels and structures.
Vendors: Hai Nam, India Electricals (IES), Vinfab Engineers India, NPES, FDG (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide supported routes for process piping and electrical/instrument cables and safe access/egress and working surfaces around pipe racks, vessels and structures. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Steel grating, handrail, stair and access platform manufacturer specifications (load classes, span tables) — Fetch a grating manufacturer catalogue (e.g. AMICO, Nucor, Treadwell) with load tables
- Pipe rack design standards and typical bay dimensions — Fetch a public pipe rack design guideline

### Reinforced concrete — high-performance / sulfate-resistant concrete (civ-reinforced-concrete-high-performance-sulfate-resistant-concr)

Primary code: PWR: Power and renewables
Provide durable structural concrete for foundations, slabs, walls and machine blocks in aggressive ground/process environments; sulfate-resistant cement, low permeability mixes and corrosion inhibition used where required.
Vendors: Sika, Fosroc (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide durable structural concrete for foundations, slabs, walls and machine blocks in aggressive ground/process environments; sulfate-resistant cement, low permeability mixes and corrosion inhibition used where required. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Sulfate-resistant cement types (ASTM C150 Type II/V, EN 197 CEM I/II/III) with sourced property tables — Fetch a cement manufacturer's public datasheet for sulfate-resistant cement
- Concrete mix design numeric ranges for aggressive sulfate/chloride exposure — Fetch ACI 318 durability chapter public summary or DOT spec

### Scaffolding (civ-scaffolding-module-rosette-systems-for-industrial-access)

Primary code: PWR: Power and renewables
Provide temporary worker access, guardrails, loading platforms and birdcage/scaffold support around tanks, vessels, pipe racks and structures during construction and maintenance.
Vendors: Layher, PERI (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Layher Allround connections per rosette | 8 connections | Layher Allround product page: up to eight connections in one Allround Connector at one level and various angles; bolt-free wedge-head with AutoLock; launched 1974; steel or aluminium |
| Layher approvals | Z-8.22-64 / Z-8.22-939 / Z-8.22-26.1 approval nos. | Layher: Allround Scaffolding Steel Z-8.22-64 on basis of EN 12811; Lightweight Z-8.22-939; Aluminium Z-8.22-26.1 |
| Connections per rosette | 8 count | Value as printed in the cited source; no further qualifier stated. |
| Approvals | Z-8.22-64 / Z-8.22-939 / EN 12811 standard | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- APAC scaffolding supplier specifications and local loading regulations — Fetch local scaffold supplier pages in Malaysia/Singapore

### Seismic design — base isolation, dampers, structural monitoring (civ-seismic-design-base-isolation-dampers-structural-monitoring)

Primary code: PWR: Power and renewables
Decouple structure from ground motion using laminated rubber/lead-rubber/friction-pendulum bearings and dissipate energy; monitored by robotic total stations, GNSS and geotechnical sensors.
Vendors: Bridgestone Corporation, Dynamic Isolation Systems (DIS), Trimble Geospatial (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Bridgestone seismic isolation product line | HDR / LRB / NRB / Elastic Sliding Bearing product types | Bridgestone products page: HDR uses high damping rubber (spring + damping); LRB lead plug in laminated natural rubber (G0.40) with elasto-plastic hysteresis; NRB low damping about 2–3% with G0.30/G0.35/G0.40/G0.45; Elastic Sliding Bearing uses PTFE + stainless plate, used with NRB/LRB/HDR |
| Trimble S9 angular accuracy | 0.5 or 1 arc-second | Trimble S9 product page: EDM accuracy 1.0 mm + 2 ppm prism / 2.0 mm + 2 ppm DR; max range 5500 m; DR PLUS; used for monitoring, rail, mining, tunneling |
| Trimble S9 HP EDM accuracy | 0.8 mm + 1 ppm prism / 3.0 mm + 2 ppm DR mm + ppm | Trimble comparison table: S9 HP max range 7000 m, angular accuracy 0.5 or 1 arc-second |


Recorded gaps:

- Fluid viscous damper and tuned mass damper manufacturer data — Fetch Taylor Devices / Fyfe dampers datasheets
- Strain gauge / SHM sensor specifications (vibrating wire, fibre optic) — Fetch Geokon or Micron Optics sensor datasheets

### Shallow / raft / pad foundations (civ-shallow-raft-pad-foundations)

Primary code: PWR: Power and renewables
Transfer column, wall and equipment loads to near-surface bearing strata by spread footings, combined pads, rafts or mat foundations; commonly used for tanks, pumps, pipe-rack columns and small equipment where surface soils are competent.
Vendors: BAUER Spezialtiefbau GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Eurocode 7 scope | EN 1997-1:2004 / EN 1997-2:2007 standard | EC7 applies to geotechnical aspects of design of buildings and civil engineering works, used with EN 1990:2002; Part 2 covers ground investigation and testing |
| Axle load | 45 t at 1 km/h | Value as printed in the cited source; no further qualifier stated. |
| Axle compensation | 600 mm | Value as printed in the cited source; no further qualifier stated. |
| Width | 3000 mm | Value as printed in the cited source; no further qualifier stated. |
| edition | 2021-12 n/a | Value as printed in the cited source; no further qualifier stated. |
| rated mooring capacity | 80 t | Value as printed in the cited source; no further qualifier stated. |
| ViscoCrete-1000 water reduction | 30 % max | Value as printed in the cited source; no further qualifier stated. |
| Sika AIR dosage | 7–400 mL/100 kg | Value as printed in the cited source; no further qualifier stated. |
| thickness | 12-15 mm | Value as printed in the cited source; no further qualifier stated. |
| diameter | up to 52 m | Value as printed in the cited source; no further qualifier stated. |
| stock thickness | 1/4-4 in | Value as printed in the cited source; no further qualifier stated. |
| condition | normalized n/a | Value as printed in the cited source; no further qualifier stated. |
| material | needle-punched nonwoven geotextile filled with sand n/a | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Bearing-capacity and settlement calculation examples for pad/raft footings to EC7 / ACI — Fetch a public EC7 worked example or state DOT shallow foundation manual
- APAC-specific shallow foundation practice (Malaysia, Singapore) — Fetch BCA Singapore / JKR Malaysia foundation guidance pages

### Steel connections — bolting, welding, fabricated details (civ-steel-connections-bolting-welding-fabricated-details)

Primary code: PWR: Power and renewables
Join beams, columns, bracing and equipment supports by shop/site welding and high-strength bolting; seismic designs require predictable yield and ductility at connections.
Vendors: Portland Bolt, ArcelorMittal Orange Book (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| A992 welding filler | E70 series low-hydrogen filler metal | A992 is prequalified base metal under AWS D1.1; normally E70 series low-hydrogen filler by SMAW/FCAW/GMAW/SAW; preheat per D1.1 tables; heavy flanges >2 in need access-hole grinding + MT/PT |
| Rebar welding code | AWS D1.4/D1.4M standard | ASTM A615 Note 3: welding should be approached with caution; latest AWS D1.4/D1.4M recommended for filler selection and preheat/interpass |


Recorded gaps:

- RCSC 2020 pretension table values — Fetch RCSC Specification for Structural Joints Using High-Strength Bolts public page
- Welding consumable manufacturer catalogues (ESAB, Lincoln Electric, Kobelco) — Fetch AWS D1.1 filler metal classification pages from manufacturers

### Structural steel corrosion protection systems (civ-structural-steel-corrosion-protection-systems)

Primary code: PWR: Power and renewables
Protect structural steel from atmospheric and process corrosion via barrier coatings, galvanizing, metallizing or weathering steel; often specified in a system with primer/intermediate/topcoat and DFT schedule.
Vendors: Carboline, Jotun / Hempel / PPG / Sherwin-Williams (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Weathering steel grades | ASTM A588 Grade 50 / A242 Grade 42, 46, 50 grade | AISC steelwise: W-shapes with atmospheric corrosion resistance obtainable to A588 Gr 50 or A242 Gr 42/46/50 |


Recorded gaps:

- Named anti-corrosion coating systems with DFT schedules for carbon steel in C5-M / offshore environments — Fetch ISO 12944 system datasheets from a protective coatings manufacturer

### Structural steel — fabricated beams, columns, bracing (civ-structural-steel-fabricated-beams-columns-bracing)

Primary code: PWR: Power and renewables
Primary gravity and lateral load-resisting frame for process structures, pipe racks, equipment supports and buildings; fabricated from rolled or welded sections in carbon, HSLA or high-strength grades.
Vendors: ArcelorMittal Europe, SSAB, American Steel & Aluminum (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ASTM A992 yield strength | 50-65 ksi (345–450 MPa) | ASTM A992 preferred grade for W-shapes: 50 ksi min / 65 ksi max yield, 65 ksi min tensile, Fy/Fu <=0.85, CE <=0.45 (0.47 for flanges >2 in); AISC 341 expected yield = 1.1 x specified min |
| edition | 25th edition, 2025 with 2026 amendment n/a | Value as printed in the cited source; no further qualifier stated. |
| annexes | 8 normative + 11 informative count | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- APAC structural steel grade equivalents (JIS SM490, AS/NZS 300PLUS, Chinese Q355) — Fetch JIS/AS/NZS steel grade datasheets from mills

### Survey, setting out, geotechnical investigation and laboratory testing (civ-survey-setting-out-geotechnical-investigation-and-laboratory)

Primary code: PWR: Power and renewables
Establish control points and setting-out, characterize ground and groundwater via drilling, sampling and in-situ tests, and determine soil/rock properties by laboratory testing for foundation design.
Vendors: Trimble Geospatial, Leica Geosystems / Topcon (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Trimble S9 EDM accuracy (prism) | 1.0 mm + 2 ppm mm + ppm | Trimble S9 page: DR PLUS EDM; 2.0 mm + 2 ppm DR; 5500 m max range; angular accuracy 0.5 or 1 arc-second; ISO 17123-3/-4 on spec sheet |
| Eurocode 7 Part 2 | EN 1997-2:2007 Ground investigation and testing standard | JRC Eurocode 7 page: Part 2 covers ground investigation and testing; actions from ground (earth pressures, groundwater) calculated per EN 1997 |


Recorded gaps:

- Geotechnical lab test standards and typical result ranges (Atterberg, SPT N, consolidation mv/Cv) — Fetch a public geotechnical laboratory manual
- Leica/Topcon instrument specifications — Fetch Leica/Topcon product pages

### Temporary works — cofferdams, dewatering, shoring, excavation support (civ-temporary-works-cofferdams-dewatering-shoring-excavation-sup)

Primary code: PWR: Power and renewables
Exclude water and soil from excavation areas, temporarily retain excavation faces and protect adjacent assets while foundations are constructed; includes sheet-pile cofferdams, diaphragm/secant walls, ground anchors, struts, wellpoints and dewatering pumps.
Vendors: BAUER Spezialtiefbau, Layher (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Secant wall example (BAUER) | 880 mm dia x 16 m mm x m | BAUER: secant pile wall to support excavation pit / seal groundwater, double-head method, Businesspark Hannover |
| Layher shoring/heavy-duty support | Shoring TG 60 / Heavy-Duty Tower system | Layher Allround product page lists Shoring TG 60, Heavy-Duty support/Heavy-Duty Tower and Allround Bridging System accessories |


Recorded gaps:

- Cofferdam design water-head/steel sheet pile section data — Fetch USACE cofferdam design manual or sheet-pile supplier datasheet
- Dewatering pump capacities and wellpoint spacing — Fetch a dewatering equipment manufacturer datasheet

## civil

### Drainage, spill containment and wastewater (gas-engine-drainage-spill)

Primary code: PWR: Power and renewables
Drainage, spill containment and wastewater
Vendors: Wärtsilä (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Concrete pad / spill containment | reinforced concrete, 28-day compressive strength at least 2500 psi (17,236.89 kPa); pad at least 6 in (150 mm) deep and extending at least 9 in (230 mm) beyond skid on all sides; serviceability and spill containment to be considered psi / mm | Cummins Gas Power Plant Application Manual, section 3.6.5.2 |
| Oil overflow and waste oil | overflow pipe on make-up tank in case of level sensor failure; overflow oil routed to receptacle to avoid spills; waste lube oil tank recovers used oil before recycling/off-site disposal qualitative | Cummins Gas Power Plant Application Manual, sections 3.2.4.2 and 3.2.2 |
| Exhaust condensate drainage | piping must slope down and away from exhaust turbo and include condensate drains; rain cap/trap may be needed on vertical outlets (freeze risk noted) qualitative | Cummins Gas Power Plant Application Manual, exhaust system section |


### Foundations, plinths and vibration isolation (gas-engine-foundation-vibration)

Primary code: PWR: Power and renewables
Foundations, plinths and vibration isolation
Vendors: Cummins Inc. (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pad levelness / flatness | 0.25 inch (6.35 mm) | Cummins Gas Power Plant Application Manual section 3.6.5.1: mounting pad or piers level and flat within 0.25 in (6.35 mm); isolate from rest of concrete flatwork with flexible caulking |
| Massive foundation ratio | at least 1.5 times installed equipment weight | Cummins Gas Power Plant Application Manual section 3.6.5.1: further vibration control with massive mounting foundation at least 1.5x weight of installed equipment |
| Steel spring isolator damping | ?-98 % of generator set vibration energy | Cummins Gas Power Plant Application Manual section 3.6.5.3: lean-burn natural gas gensets come standard with steel spring isolators which 'can dampen up to 98%' of vibration energy |
| Pad concrete strength and geometry | 28-day compressive strength at least 2500 psi (17,236.89 kPa); depth at least 6 in (150 mm); extends at least 9 in (230 mm) beyond skid on all sides psi / mm | Cummins Gas Power Plant Application Manual section 3.6.5.2 |


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

## co2

### CO2 compression and purification (urea-co2-compression)

Primary code: PCH: Petrochemicals
CO2 compression and purification (from ammonia plant)
Vendors: Stamicarbon, Casale SA, SensoTech GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| CO2 feed pressure for carbamate formation | 110 atm | Thermodynamic condition for carbamate formation reaction (2 NH3 + CO2 -> NH4CO2NH2, delta H = -117 kJ/mol at 110 atm and 160 C), Urea industrial production |
| urea synthesis pressure range (as printed) | 1.4-1.75 MPa | Wikipedia Urea, Industrial production: process conditions compromise for carbamate formation vs urea formation at ~190 C |
| synthesis temperature | 190 degC | temperature needed for the slow urea formation reaction, per Wikipedia Urea industrial production |
| CO2 conversion in reactor (Split Flow Loop) | 62 percent | Casale SPLIT FLOW LOOP performance claim: 'CO2 conversion in the reactor as high as 62%' |
| carbamate thermal conversion temperature/pressure | 130-200 bar | SensoTech: thermal conversion of ammonium carbamate at 200 C and 130-200 bar |


Recorded gaps:

- CO2 compressor OEM/model, polytropic efficiency, stage count, seal type, capacity range — Fetch a named OEM CO2 compressor page (e.g. MAN Energy Solutions, Siemens Energy, Ariel) directly if a URL can be obtained.
- CO2 purification spec (H2S, sulfur, oil, inerts limits) and purifier vendor — Locate an authoritative urea process licence brochure or plant specification.
- CO2 compressor OEM/model, polytropic efficiency, stage count, seal type, capacity range — Fetch a named OEM CO2 compressor page (e.g. MAN Energy Solutions, Siemens Energy, Ariel) directly if a URL can be obtained.
- CO2 purification spec (H2S, sulfur, oil, inerts limits) and purifier vendor — Locate an authoritative urea process licence brochure or plant specification.

### CO2 removal - amine (ammonia-co2-removal)

Primary code: PCH: Petrochemicals
CO2 removal - amine (MDEA/MEA) absorbers and regenerators; Benfield/Selexol/Rectisol; solvent reclamation
Vendors: Linde AG, Air Liquide, UOP LLC, Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| MDEA concentration in aqueous solution | 30-55 wt% | Typical amine concentration for removing H2S and CO2 (Kohl & Nielsen, Gas Purification, cited on page) |
| MEA concentration for H2S and CO2 removal | 20 wt% | Typical MEA concentration; ~30 wt% when removing only CO2 where plant metallurgy is appropriate |
| DEA concentration | 25-35 wt% | Typical DEA concentration for H2S and CO2 removal |
| MEA/DEA CO2 loading limit | 0.55 mol CO2 per mol amine | Stoichiometric loading capacity limit for primary/secondary amines (Idem 2006 cited) |
| Stripping energy share of amine unit operating cost | ?-70 % | MEA/DEA require large regeneration energy, up to 70% of total operating costs (Idem 2006 cited) |
| Amine absorber typical operating temperature | 35-50 deg C | Simplified absorption column typical operating range (Amine gas treating page) |
| Amine absorber typical operating pressure | 5-205 atm absolute | Simplified absorption column typical operating range |
| Selexol absorption pressure | 300-2000 psia (2.07-13.8 MPa) | Selexol process acid-gas absorption pressure; capacity reduced below ~300 psia (2.07 MPa) |
| Rectisol absorption temperature | -40 deg C (-40 deg F) | Cold methanol solvent absorbs acid gases at high pressure |
| Rectisol absorption pressure | 400-1000 psia (2.76-6.89 MPa) | Rectisol process acid-gas absorption pressure |


Recorded gaps:

- Benfield hot-potassium-carbonate process details and supplier — Locate and fetch an authoritative Benfield process page (e.g. Fluor/BASF licensed solvent).
- MDEA specifically in ammonia CO2 service (as opposed to general gas treating) and solvent reclamation design — Fetch an OEM/EPC page on ammonia CO2 removal and amine reclamation.
- Benfield hot-potassium-carbonate process details and supplier — Locate and fetch an authoritative Benfield process page (e.g. Fluor/BASF licensed solvent).
- MDEA specifically in ammonia CO2 service (as opposed to general gas treating) and solvent reclamation design — Fetch an OEM/EPC page on ammonia CO2 removal and amine reclamation.

## co2-stripper

### Urea CO2 stripper (urea-co2-stripper)

Primary code: PCH: Petrochemicals
High-pressure column that strips unconverted carbamate from the urea solution using feed CO2 as the stripping agent, decomposing carbamate and returning ammonia and CO2 to the condenser. CO2 stripping cut the steam demand of urea plants relative to conventional total-recycle designs.
Vendors: Stamicarbon, thyssenkrupp Uhde, Toyo Engineering, Casale SA, Yara (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| stripper effluent pressure | 140 bar | CO2-stripping process, effluent conditions as stated |
| stripper effluent temperature | 190 °C | CO2-stripping process, effluent conditions as stated |
| residual carbamate in stripper outlet solution | 1-2 % | solution leaving the stripper |
| stripping steam consumption | 0.8-1.0 t steam/t urea | steam used per tonne of urea in the stripping section |
| stripping process operating pressure | at or near full reactor pressure n/a | Wikipedia: stripping process developed early 1960s by Stamicarbon in the Netherlands, operates at or near full pressure of the reaction vessel |
| hydrolysis residence time | short (designed) n/a | urea hydrolyses back to ammonium carbamate in hottest stages, especially the stripper, so residence times there are designed to be short |
| HYPER-U benefit | medium-high pressure (MHP) carbamate decomposition step reduces steam and cooling water demand n/a | Casale HYPER-U self-stripping process description |
| CO2 conversion in reactor | 62 percent (as high as) | Casale performance claim |
| sections | HP synthesis + LP purification/carbamate recovery; optional MP section for high capacity n/a | Casale technology page |

- **Stamicarbon** High-pressure CO2 stripper: CO2 stripping; no medium-pressure recirculation stage downstream
- **Casale** SPLIT FLOW LOOP: best suited up to 2,300 MTD, or 3,500 MTD with medium-pressure stage
- **Saipem (ex-Micoperi 7000)** Falling-film stripper 31/41 E-1: operates at 146 kg/cm2g

Recorded gaps:

- Stripper tube count/length/diameter, duty, stripping efficiency number, corrosion allowance — Read Casale HP stripper news detail pages and the HYPER-U brochure via PDF-capable fetch.
- Stripper tube count/length/diameter, duty, stripping efficiency number, corrosion allowance — Read Casale HP stripper news detail pages and the HYPER-U brochure via PDF-capable fetch.

## compressed

### Compressed air and instrument air (utility-instrument-air)

Primary code: PCH: Petrochemicals
Compressed air and instrument air
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Instrument air mains pressure | 6 bar | Air normally distributed at mains pressure of 6 bar (100 psig) |
| Instrument air quality | dry and clean (free from oil) qualitative | Instrument air must be dry and clean; usually dried over packed molecular sieve adsorbent regenerated by temperature swing |


## compressed-air

### Instrument air / plant compressed air systems (dampers, control valves, actuators) (instrument-air-system)

Primary code: PWR: Power and renewables
Supply dry, oil-free, particulate-controlled compressed air to pneumatic actuators on dampers and control valves and to instrument/control devices; dryers, filters, separators and receivers condition the air; dew-point sensors monitor dryness at critical points. Seal air for HRSG bypass dampers is a separate but related air system.
Vendors: Atlas Copco, CS Instruments, E+E Elektronik (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Minimum pressure dew point margin below coldest exposed instrument | 10 degrees C (18 F) below the lowest temperature any part of the instrument system is exposed to | Atlas Copco citing ANSI/ISA-7.0.01-1996; measured at dryer outlet |
| Maximum pressure dew point at line pressure | 4 degrees C (39 F) | Atlas Copco citing ANSI/ISA-7.0.01-1996; companion to the 10 C margin rule |
| Working pressure | 4-13 bar(g) | Printed in Technical specifications table; imperial equivalent 109-189 psig also printed |
| Capacity FAD | 30-5,082 m3/h | Printed in Technical specifications table; imperial equivalent 18-2,988 cfm also printed |
| Installed motor power | 5.5-500 kW | Printed in Technical specifications table; imperial equivalent 7.5-670.5 HP also printed |
| Capacity FAD | 8-1,410 l/s | Printed in separate row of Technical specifications table |
| Standards compliance | ISO 9001, ISO 14001, ISO 1217 n/a | Printed under 'Designed for efficiency' |
| Energy recovery from motor and element oil circuit | ?-up to 78 % | Printed under 'Recover energy' on GA series page |
| VSD average energy savings claim | 50 % | Printed vendor claim: 'GA VSD+ achieves average energy savings of 50%' |


Recorded gaps:

- Typical instrument-air supply pressure range for boiler damper/valve actuators not found on an authoritative page — Fetch ISA-7.0.01 summaries or actuator OEM (Fisher, Emerson, Siemens, Parker) datasheets stating supply pressure (e.g. 20-100 psig) with basis.
- No Ingersoll Rand, Parker, Emerson or Fisher instrument-air page was actually read — Fetch named OEM pages for air preparation and instrument actuators before adding them as evidenced vendors.
- No SE Asia-specific instrument-air ambient-design example found — Look for ISA-7.0.01 ambient/PDP chart reproduced by a regional vendor and cite its exact values.

## compressor

### Centrifugal compressor (compressor-centrifugal)

Primary code: ROT: Rotating and static equipment
Dynamic compressor that raises gas pressure across one or more impeller stages — the standard machine for refinery and petrochemical process gas, pipeline boost, gas-lift and reinjection, and CO2 service, driven by gas turbines or electric motors through gears. Casing arrangements (overhung, integrally-geared, horizontally- or vertically-split/barrel) set the pressure class; barrel-style machines serve the highest-pressure gas reinjection duties.
Vendors: Siemens Energy (incl. ex-Dresser-Rand), Baker Hughes, Atlas Copco, Mitsubishi Power (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| single-stage pressure ratio | 1-10 ratio | single-stage machines; ratios of about 8 are a helicopter-engine example and few centrifugal stages exceed 10:1 — process duty sits well below the top of this range |
| oilfield gas reinjection discharge pressure | 700 bar | approaching 700 bar with barrel-style casings, as stated |


Recorded gaps:

- per-vendor model-line ranges (flow, stage count, discharge pressure) for Siemens Energy STC, Baker Hughes BCL/DBL and PCL, MCO-I and Atlas Copco integrally-geared machines — fetch the OEM compressor family pages (browser session if needed) and add model lines with stated ranges
- CO2-specific compression train boundaries (inlet, discharge, density effects) — mine the ccs-co2-compression-dehydration card's sources and OEM CO2 compression references

### Fuel gas booster / compressor for low supply pressure to burners (fuel-gas-booster)

Primary code: PWR: Power and renewables
Raises incoming utility gas pressure to the net regulated pressure required at the burner gas-train inlet when mains pressure is insufficient; packaged skids combine a hermetically sealed centrifugal blower, check valve, inlet/outlet pressure switches, isolating valves, gauges and a factory control panel, usually installed just downstream of the gas meter. Selection basis: gas flow = burner firing rate / calorific value; pressure lift = minimum required burner pressure minus available mains pressure.
Vendors: Eclipse Combustion (BoostPak; spec sheets hosted on Kromschroeder docuthek), ETTER Engineering / BoosterWorx, Cleaver-Brooks, Brittania Industries (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ETTER compact booster package capacity | 1000-1600 cfh natural gas | E101-P rated up to 1,000 CFH; E101-PHC up to 1,600 CFH; hermetically sealed, UL-listed factory-assembled packages |
| Volume flow | 50-38,000 m3/h | Printed under Technical data (metric view) on AERZEN product page |
| Differential pressure (delta p) | 150-2,000 mbar | Printed under Technical data (metric view) on AERZEN product page |
| Medium | Process Gases n/a | Printed under Technical data |
| Conveying | Oil-free n/a | Printed under Technical data |
| Stage configuration | 1 or 2 stage design n/a | Printed in product description |
| Shaft sealing | magnetic coupling n/a | Printed under 'advantages at a glance': low-maintenance sealing system with magnetic coupling |
| Rotor design | robust two-lobe rotor design (gas-tight sealed) n/a | Printed under 'advantages at a glance' |


Recorded gaps:

- No fetchable OEM page giving a complete booster selection table keyed to boiler HP with both flow and pressure basis for HRSG duct burners or CFB plants — Search GE Vernova / B&W / Mitsubishi HRSG duct-burner fuel-train specifications and gas-compressor OEMs (e.g. Honeywell/Eclipse) for a fetchable duty table.
- No named Asia-Pacific gas-booster vendor or installed plant found — Search local-language terms (e.g. 'gas booster boiler Malaysia/Indonesia/China', 'gas pressure booster burner') and check KOSHA/KTL-listed suppliers.
- Pressure range of 1-3 psi for power generation is printed in a presentation; conversion to inches wc not printed — Find an OEM table printing power-generation burner pressure in a single unit.

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
| Control type | Stand-alone PLC-based oxygen trim control for steam or hot water boilers control type | Product bullets and Product Overview |
| Trim modes | Air trim or fuel trim; variable-speed drive option modes | Product Overview bullets |
| Compensation | Temperature, barometric pressure, fuel characteristics and normal hysteresis compensated variables | Product Overview: system automatically compensates for these |
| Sensors | Oxygen and firing rate sensors; custom C-B O2 Probe or industrial O2 probes such as Yokogawa scope | Product Overview |
| Fuel train compatibility | Standard or compact fuel trains such as the Siemens valve assembly compatibility | Product Overview bullet |
| Hawk Boiler Controls features | Touchscreen HMI, economizer and O2-trim options, burner sequencing, fault history, lead/lag operation feature set | Boiler Controls catalog listing |
| Hawk 4500 features | Complete control system for new or retrofit industrial watertube boilers/burners; economizer control, draft control, full metering options feature set | Boiler Controls catalog listing |


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
| Platform types | DCS (plant-wide Distributed Control System) and PLC platform | Product page: 'Burner Management Systems are implemented in two general types of platforms'; DCS most common for utilities |
| Engineering scope | Forney designs and engineers BMS logic; physical programming at Forney or DCS supplier location; PLC programming and Factory Acceptance Test at Forney facility scope | Product page DCS Platform and PLC Platform sections |
| Display | Standard 7-inch touchscreen HMI | Boiler Controls catalog listing: 'comes with a standard 7" touchscreen' |
| Positioning | High-performance industrial and commercial burner control system product class | Boiler Controls catalog listing |
| Components | PLCs, HMIs, complex relay logic, transmitters for all measurements scope of supply | Industrial Burners page Burner management systems section |
| Panel certifications | UL certified panel shop; ATEX, CSA and UL certifications; IEC and NEC standards certifications | Industrial Burners page Burner management systems section |


Recorded gaps:

- trip logic and proof-of-closure arrangements for specific boiler makes — Read the burner OEM's BMS sequence matrix and NFPA 85 (primary text is paywalled).

### Engine control / genset controller / paralleling controls / protection relays / synchronising (gas-engine-controls-paralleling)

Primary code: PWR: Power and renewables
Engine control / genset controller / paralleling controls / protection relays / synchronising | Power monitoring / DCIM / microgrid and genset paralleling controllers
Vendors: ComAp, Woodward, Basler Electric, Deep Sea Electronics, DEIF, Schneider Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Genset paralleling capacity | 1-32 gensets | Woodward easYgen-3000XT isochronous operation; functions include synchronization, protection, AVR, configurable PIDs, genset automation, load and power factor control |
| Generator/mains voltage range | 15-415 V AC phase-to-neutral | Deep Sea DSE7320 MKII generator and mains sensing; 25-720V phase-to-phase; frequency 3.5-75 Hz |
| Excitation current | 10000 A DC | Basler DECS-2100 digital excitation control system, up to; controls/protects/monitors synchronous generators and motors |
| ComAp InteliGen 1000 coordinated units | 64 additional gen-sets/mains/tie controllers | ComAp InteliGen 1000 product page: CAN FD inter-controller communication, up to 64 additional controllers; ISA 62443 level 2-3 security; hot-swap and CAN redundancy (software key); 3x Ethernet Modbus TCP/SNMP, 1x RS-485 Modbus RTU; enclosure 262x182x47 mm |
| ComAp InteliGen 1000 functions | Automatic mains failure, start-up synchronisation, kW/kVAr sharing, dynamic spinning reserve, peak shaving, load shedding, droop regulation, user-defined protections function set | ComAp InteliGen 1000 product page extended feature list; compliant with EN 50549, VDE-AR-N 4105/4110, G99, TOR, IEEE 1547 |
| ComAp bank-controller scalability | 63-4032 controllable units | ComAp extended feature 'Bank controller': up to 63 source controllers under one bank controller, up to 64 bank controllers on a common bus, theoretical maximum 4,032 control units |
| Isochronous gensets | 1-32 gensets | Value as printed in the cited source; no further qualifier stated. |
| Measurement | Class I true RMS accuracy class | Value as printed in the cited source; no further qualifier stated. |
| Redundancy | cold / warm / hot modes (search-verified detail) | Value as printed in the cited source; no further qualifier stated. |
| Cooperating controllers | 64 additional units | Value as printed in the cited source; no further qualifier stated. |
| Cybersecurity | ISA 62443 level 2-3 compliance claim | Value as printed in the cited source; no further qualifier stated. |
| Enclosure | 262 x 182 x 47 mm | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Full IEC 61850 / protection-relay model list for MV gas-engine switchgear — Fetch ABB/Siemens/Schneider protection relay and switchgear datasheets
- Site-specific grid-code certification for a named Jenbacher/Wartsila installation — Fetch project grid-code compliance statements
- DEIF and Woodward specific genset/microgrid controller models and specs — Fetch official DEIF and Woodward product pages and record model numbers with URLs
- Evidence that a specific data centre uses a named paralleling controller with gas engines — Seek case studies from ComAp/DEIF/Woodward with named sites

## cooling

### Cooling utilities for the data centre directly coupled to the gas-engine energy story (data-centre-cooling-utilities)

Primary code: IDC: Data centres
Cooling utilities for the data centre directly coupled to the gas-engine energy story
Vendors: Johnson Controls (YORK, Silent-Aire), Vertiv, Trane (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Cooling utilities for the data centre directly coupled to the gas-engine energy story | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Actual cooling-system water consumption and COP at a gas-engine-powered data centre — Seek operator sustainability reports with measured WUE for JAK2 or similar sites

### Cooling water system and cooling towers (utility-cooling-water-towers)

Primary code: PCH: Petrochemicals
Cooling water system and cooling towers
Vendors: Dynaflow Research Group BV, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Cooling-water usable temperature floor | 40 degC | Natural/forced-draft towers generally used unless river or lake water in sufficient quantity; cooling water usable down to about 40-50 C, below that chilled water or refrigeration is used |
| Loop arrangement | parallel configuration | Each process cooler served in parallel; cooling water almost never flows through two coolers in series; blowdown upstream of tower, make-up plus biocide/corrosion/fouling inhibitors |
| Number of distinct cooling systems at one ammonia plant | 2 systems | Australian ammonia plant commissioned mid-2000s with Sea Cooling Water (SCW) high-capacity system and secondary closed-loop Fresh Cooling Water (FCW), both with mainly underground composite piping |
| Seawater / brackish water use | requires more expensive heat-exchanger materials of construction qualitative | Coastal sites and offshore operations |


### Engine cooling: jacket-water system, radiator, cooling tower, heat exchanger, circulating pumps (gas-engine-cooling-system)

Primary code: PWR: Power and renewables
Engine cooling: jacket-water system, radiator, cooling tower, heat exchanger, circulating pumps | Cooling water / cooling towers (open and closed) and heat rejection | Closed-loop jacket water / HT and LT circuits, expansion and monitoring
Vendors: INNIO Jenbacher, Wärtsilä, Cummins Inc., MWM / Everllence, MWM / Everllence (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Heat-recovery design temperatures | 70 / 90 degC return / hot water | Jenbacher J920 FleXtra CHP module; heating-water circuit with 70C return and 90C+ hot water for ~94% total efficiency |
| Radiator design | flat fins / appropriate fin distance qualitative | Jenbacher cooling system (radiators) BOP: sufficient surface area and cooling capacity, easy cleaning; special coatings/materials near coast; special soldering/heating for extremely cold environments |
| CHP total efficiency | 95 % | Jenbacher Type 6 CHP module, up to; engine and alternator on frame, control panel, gas train, heat exchangers including exhaust-gas heat exchanger |
| Cooling tower with heat exchanger; water treatment obligations | Cooling towers typically used with heat exchangers; chemical water treatment, make-up system, discharge and special maintenance must be planned qualitative | Cummins Gas Power Plant Application Manual A049Z057 section 3.1.9.2; Figure 24 'Tower cooling system connection to generator set' |
| Closed-loop cooling process water consumption (data-centre application) | ?-<5 litres/hour | Wärtsilä Data center power solutions: closed-loop cooling with water-to-air radiators keeps process water consumption near zero; 'consume less than 5 liters (1.3 gallons) of water per hour' |
| Ambient operating range / altitude (same closed-loop plant) | -45-50 deg C | Wärtsilä Data center power solutions: full power from -45 C to 50 C; 100% output above 1,200 m altitude |
| Cooling system functions (fill/drain/vent) | maintain temperature at design flow, maintain design pressure, accommodate expansion/contraction/overfill/loss, provide vent path for entrapped air, provide fill/drain/sample points qualitative | Cummins Gas Power Plant Application Manual, section 3.1 cooling system introduction |


Recorded gaps:

- Radiator thermal duty, design ambient, coolant flow and pump head for a named engine — Fetch Jenbacher Type 6 engine type sheet PDF (innio.com/images/medias/files/167/...) with a PDF reader
- Cooling tower and circulating-pump vendor/models — Fetch EVAPCO/Baltimore Aircoil/SPX cooling tower data centre brochures

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

## damper

### Stack/breeching dampers, bypass dampers and sealing systems for HRSG simple-cycle operation (hrsg-bypass-damper)

Primary code: PWR: Power and renewables
Diverter/bypass damper systems route gas-turbine exhaust either to the bypass stack (simple cycle, HRSG offline) or through the HRSG (combined cycle), with mechanically interlocked isolation and seal-air systems so personnel can enter the isolated HRSG while the turbine runs. Stack dampers slow HRSG cooling between starts, prevent rain ingress and provide overpressure relief.
Vendors: Forney Corporation, NEM Energy, GSD (Genel Sistem Dizaynı), Boldrocchi Group, Fox Equipment, METCO Technologies, Energylink International, Hangguo (HGTYBypass) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Forney dual BiPlane interlock positions | 10-80 degrees: open damper locked >80 degrees while mating damper closes >10 degrees | Forney article; mechanical interlock requires one damper at least 80% open so turbine exhaust cannot be fully blocked |
| Forney seal-air fans and allowable entry temperature | 2 fans at 200% capacity; seal-air curtain designed to maintain temperatures below 140 F (OSHA confined-space requirement) for HRSG entry | Forney article; truss blade cavity forms air-seal plenum, flexible seal packs at blade tips |
| Carbon packing temperature limit and shaft material | 400 degrees C (753 F) oxidising temperature limit for carbon components; 17-4PH stainless shaft | Forney article; purged lantern ring prevents exposure to corrosion and temperature above the oxidising limit |
| Configuration | two BiPlane Dampers - one on HRSG inlet, one isolating the stack n/a | Printed in product overview |
| Safety interlock | mechanical interlock prevents both dampers closing at the same time; allows both open n/a | Printed under Safety System |
| Sealing | dual set of seals; seal air system interlocked if pressure falls indicating a leak n/a | Printed under Safety System |
| Claimed advantages | soft start flow distribution; control capability; reduced time to open; eliminates guillotine damper; smaller actuators n/a | Printed under Features & Benefits; no numeric performance figures printed |
| Independent actuation | independent actuator on each damper n/a | Printed in product overview |


Recorded gaps:

- No named SE Asia HRSG bypass-damper project (Malaysia/Indonesia/Philippines) found — Search regional EPC project references for 'bypass damper HRSG' and check Hangguo/Chinese vendor project lists.
- No design basis for seal-air pressure relative to exhaust pressure (other than 'higher than exhaust pressure' and >500 mm wc from two vendors) — Fetch a damper datasheet giving seal-air differential pressure, flow and fan sizing basis.
- No damper leakage class tied to a named standard (e.g. ASME N510 / EN 12237) found — Look for an HRSG damper specification citing a leakage test standard.

## decomposers

### Decomposers / carbamate decomposer (urea-carbamate-decomposer)

Primary code: PCH: Petrochemicals
Decomposers / carbamate decomposer (LP/MP)
Vendors: SensoTech GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| first decompression stage | 1.8-2.5 MPa | Wikipedia: conventional recycle process depressurizes reaction solution in stages, first to 1.8-2.5 MPa |
| second decompression stage | 0.2-0.5 MPa | Wikipedia: then to 0.2-0.5 MPa, each stage through a steam-heated carbamate decomposer |
| inline analyser installation point | outlet of the decomposer, typically DN80 pipeline n/a | SensoTech LiquiSonic immersion sensors at decomposer outlet |


Recorded gaps:

- Decomposer heating-medium pressure, heat duty, vendor equipment details — Fetch a process-licensor technical paper or plant equipment list.
- Decomposer heating-medium pressure, heat duty, vendor equipment details — Fetch a process-licensor technical paper or plant equipment list.

## demineralised

### Demineralised water and raw water treatment (utility-demin-water-treatment)

Primary code: PCH: Petrochemicals
Demineralised water and raw water treatment
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Dissolved solids in demineralised water | ?-1 ppm | Water with less than 1 part per million of dissolved solids can be produced by mixed/multiple-bed ion exchange |
| Demin water cost multiple | 2 x raw water price | Demineralised water typically costs about double raw water, varying with mineral content and demin blowdown disposal cost |
| Utility units in a named urea/ammonia plant cradle-to-gate boundary | filter water treatment; demin water treatment; cooling water treatment list | PT Pupuk Sriwidjaja Palembang urea EPD system boundary, utilities section |


## drag

### Drag conveyors / tubular drag conveyors (bulk-drag-conveyors)

Primary code: PCH: Petrochemicals
Drag conveyors / tubular drag conveyors
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| equipment class | tubular drag conveyors listed among stationary bulk handling systems n/a | Wikipedia Bulk material handling |


Recorded gaps:

- Drag conveyor capacity, chain speed, tube diameter, bend radius, vendor — Fetch a drag conveyor OEM page.
- Drag conveyor capacity, chain speed, tube diameter, bend radius, vendor — Fetch a drag conveyor OEM page.

## ducting

### Expansion joints, flexible connectors and pipe supports in hot flue-gas / steam ducts (expansion-joints-ducting)

Primary code: PWR: Power and renewables
Accommodate thermal expansion, vibration and directional movement in boiler/flue-gas ducts and steam piping; protect ductwork, equipment and supports from cyclic stress and fatigue (dB Noise Reduction; vendor catalogues search-verified).
Vendors: dB Noise Reduction Inc., EagleBurgmann (KE-A/S), Unaflex / Kadant, Megaflexon, Thorburn Flex, BOA Group (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| flexible connection function | absorbs vibration and cyclic stresses from temperature changes, airflow turbulence and excessive vibration qualitative | dB Noise Reduction flexible connections page (read) |


Recorded gaps:

- Temperature, pressure, movement and life ratings for fabric vs metallic expansion joints in HRSG/CFB flue gas — Download catalogues locally, extract rating tables with model numbers and design codes, then cite page numbers.
- Pipe support/anchor/guide spacing rules for hot steam lines — Find ASME B31.1 or vendor pipe-support design guide with exact tables and record basis.
- Asia-Pacific expansion-joint suppliers and local fabricators — Run a targeted regional search for ASEAN fabric expansion joint suppliers with fetchable datasheets.

## dust

### Dust collection, scrubbers, ammonia/urea dust recovery (urea-dust-collection-scrubbers)

Primary code: PCH: Petrochemicals
Dust collection, scrubbers, ammonia/urea dust recovery | Warehouses and packaging
Vendors: Toyo Engineering, SensoTech GmbH (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| urea dust after Toyo scrubber | ?-30 mg/Nm3-Air | Toyo low-pressure drop dust scrubber with circulating water |
| ammonia removal option | acid scrubbing using sulfuric acid or nitric acid n/a | Toyo: applied where ammonia discharged to atmosphere also needs reduction |
| baghouse collection efficiency | ?-100 percent (more than 99%) | Wikipedia Dust collector: fabric collectors can achieve collection efficiency of more than 99% for very fine particulates |
| wet scrubber pressure drop - low energy | 0.5-2.5 inches water gauge (124.4-621.9 Pa) | Wikipedia Dust collector spray-tower scrubber categorisation |
| wet scrubber pressure drop - low/medium | 2.5-6 inches water gauge (0.622-1.493 kPa) | Wikipedia Dust collector |
| wet scrubber pressure drop - medium/high | 6-15 inches water gauge (1.493-3.731 kPa) | Wikipedia Dust collector |
| wet scrubber pressure drop - high energy | 15-? inches water gauge (>3.731 kPa) | Wikipedia Dust collector: greater than 15 inches water gauge |
| ESP operating voltage | 50-100 kV | Wikipedia Dust collector: particles passed through strong 50-100 kV electrostatic field |
| unit collector capacity | 200-2000 ft3/min (90-900 L/s) | Wikipedia Dust collector unit collectors for bins, silos, remote belt-conveyor transfer points |
| Urea package size | 50 kg per bag | Pusri urea EPD: product packaged in 50 kg bag |
| Warehouse in system boundary | Warehouse and packaging process block | Pusri urea EPD cradle-to-gate boundary explicitly includes 'f. Warehouse and packaging' |


Recorded gaps:

- Urea-specific dust collector models, filter media, air-to-cloth ratio, dust return method, emission guarantees — Fetch a vendor page for fertilizer dust collection (e.g. a baghouse OEM) with a known URL.
- Urea-specific dust collector models, filter media, air-to-cloth ratio, dust return method, emission guarantees — Fetch a vendor page for fertilizer dust collection (e.g. a baghouse OEM) with a known URL.

## electrical

### Boiler motor control centres / variable speed drives and electrical supply for fans and pumps (boiler-mcc-vfd)

Primary code: PWR: Power and renewables
Provide motor starting, protection and speed control for forced-draft/induced-draft fans, combustion-air blowers and boiler feedwater/service water pumps. VFDs replace throttling valves/inlet dampers with speed control, reducing energy use, wear and start-up current; BMS/CCS panels integrate VFDs with burner control.
Vendors: TMEIC, ABB, SCC Inc., Zeeco, Emerson Copeland VFDs (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide motor starting, protection and speed control for forced-draft/induced-draft fans, combustion-air blowers and boiler feedwater/service water pumps. VFDs replace throttling valves/inlet dampers with speed control, reducing energy use, | Qualitative function from the pages read in this sweep. |


Recorded gaps:

- No named boiler MCC (motor control centre) product page or MCC bus/voltage/current rating found — Search 'boiler motor control centre MCC OEM' on Siemens/ABB/Schneider/Eaton sites and fetch a product page with bus rating and standards.
- No electrical supply voltage/frequency figures for package boiler fans and pumps from an authoritative plant spec — Fetch a package boiler electrical utility requirement datasheet (OEM) listing site supply.
- CrossCo VFD article not directly read (403) — Try the article via a cached/alternate URL or cite only the search-verified summary.

### Electrical substation and power distribution (utility-electrical-substation)

Primary code: PCH: Petrochemicals
Electrical substation and power distribution
Vendors: ABB Australia (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| US transmission voltages | 135, 220, 550 or 750 kV | In the United States power is usually transmitted over long distances at 135, 220, 550 or 750 kV; local substations step down |
| On-site power generation in Pusri boundary | gas turbine generator; steam turbine generator list | Pusri urea EPD cradle-to-gate boundary lists production of electricity by gas turbine and steam turbine generator |
| Micro-grid MOU | ABB Australia supplier | Allied Green Ammonia: ABB Australia MOU for scalable electrical micro-grid solution (September 2024) |


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
| NOx reduction | 95 % post-combustion NOx reduction (up to) | Product page: 'designed to deliver up to 95% post-combustion NOx reduction' |
| Reductant options | Aqueous ammonia, anhydrous ammonia, urea reductants | Product page: 'multiple ammonia solutions (Aqueous, Anhydrous, Urea, etc.)' |
| Additional catalyst | CO or VOC catalyst available for lowest stack emissions option | Product page first paragraph |
| Applications | Power plants, refineries, chemical plants applications | Product page Features: Versatile Applications |


Recorded gaps:

- SCR ammonia-slip guarantee and catalyst life for gas-fired package boilers — Read an OEM SCR data sheet with slip, catalyst volume and temperature window.
- which of the Cleaver-Brooks SCR 1 ppm / 2 ppm statements is current — Confirm with the OEM or an updated product sheet.

## engine

### Gas engine prime mover (gas-engine-prime-mover)

Primary code: PWR: Power and renewables
Gas engine prime mover (lean-burn / stoichiometric spark-ignition / dual-fuel; cylinders, turbochargers, intercoolers)
Vendors: Wartsila Energy, INNIO Jenbacher, Everllence, MAN Engines, Rolls-Royce Power Systems (mtu), Caterpillar (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rated electrical power | 18834 kW | Wartsila 50SG 18V50SG, 50Hz, generator terminals, 100kPa ambient, 25C suction air, 30% RH, without engine-driven pumps, PF 1.0 |
| Electrical efficiency | 50.2 % | Wartsila 50SG 18V, 50Hz, same reference conditions; stated with 5% tolerance |
| Cylinder bore / stroke | 500 / 580 mm | Wartsila 50SG, 18V configuration; engine speed 500 rpm (50Hz) / 514 rpm (60Hz) |
| Rated electrical power range | 5840-9795 kW | Wartsila 34SG, 12V/16V/20V, 50Hz, generator terminals, 100kPa, 25C, 30% RH, PF1.0 |
| Electrical output | 10606 kW | INNIO Jenbacher J920 FleXtra genset, 50Hz, natural gas, output at generator terminals, DIN ISO 3046/DIN 6271, +5% tolerance, NOx basis 250/500 mg/Nm3 @5% O2 dry |
| Electrical efficiency | 48.7 % | Jenbacher J920 FleXtra, up to, 50/60Hz, generator terminals, ISO 3046 basis, NOx 250/500 mg/Nm3 @5% O2 dry |
| Electrical output | 4499 kW | Jenbacher Type 6 (J624), up to, 50Hz, generator terminals, DIN ISO 3046 / DIN 6271, +5% tolerance, NOx 250/500 mg/Nm3 @5% O2 dry |
| Engine speed | 1500 rpm | Jenbacher Type 6, 50Hz; 1500 rpm with gearbox for 60Hz; mean piston speed 11 m/s at 1500 rpm (Type 6 fact sheet, search-verified) |
| Mechanical output | 12900 kWm | Everllence (ex-MAN) 35/44G and 35/44G TS, up to; 720/750 rpm; 60/50 Hz |
| Mechanical output | 20700 kWm | Everllence 51/60G and 51/60G TS, up to; 500/514 rpm; 50/60 Hz |
| Power range | 37-750 kW | MAN Engines natural-gas engine programme (E0834-E3872), continuous operation; special gas 68-750 kW; overall efficiency >90% |
| Electrical power range | 776-2547 kWe | Rolls-Royce mtu gas gensets, 50Hz (60Hz 30-2,522 kWe); Time Before Overhaul 84,000 h |
| Voltage | 400 / 6.3 / 10.5 kV @50Hz | Value as printed in the cited source; no further qualifier stated. |
| Service life | 60000 operating hours before first major overhaul (fact sheet, search-verified) | Value as printed in the cited source; no further qualifier stated. |
| Ramp rate | >14 MW/min hot | Value as printed in the cited source; no further qualifier stated. |
| Hydrogen admixture | 25 % | Value as printed in the cited source; no further qualifier stated. |
| Voltage | 10.5 / 11 kV @50Hz | Value as printed in the cited source; no further qualifier stated. |
| Start to full power | 2 min | Value as printed in the cited source; no further qualifier stated. |
| Applications | gas gensets / CHP qualitative | Value as printed in the cited source; no further qualifier stated. |
| Grid codes | EN 50549-1/-2, VDE-AR-N 4105/4110, TOR A/B standards (search-verified detail) | Value as printed in the cited source; no further qualifier stated. |
| Time to full load | 2 minutes | POWER magazine article: 'achieves full load within two minutes' |
| Engine portfolio rating (Jenbacher Type 9 page navigation) | ?-10606 kW/engine | Jenbacher data-centre page navigation labels 'Jenbacher Type 9 Up to 10606 kW/engine' |
| Full-load start time | <2 min (fast start) | Value as printed in the cited source; no further qualifier stated. |
| Efficiency | >51 % with two-stage turbocharging | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Stoichiometric/rich-burn three-way-catalyst engine-out NOx/CO figures for the named large-bore engines — Fetch Cat G3500H/G3516H rich-burn TWC specification sheet and Jenbacher rich-burn factsheet
- Intercooler/charge-air cooler duty, approach temperature and pressure drop — Fetch Jenbacher Type 6 engine type sheet or Wartsila 50SG leaflet (wartsi.ly/41mQHgo)
- Named dual-fuel liquid-fuel day-tank sizing — Fetch Everllence 51/60DF fact sheet

## evaporation

### Evaporation / concentration (urea-evaporation-concentration)

Primary code: PCH: Petrochemicals
Evaporation / concentration (pre-concentrator, evaporators)
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| isocyanic acid decomposition risk | worst when urea solution is heated at low pressure during concentration for prilling or granulation n/a | Wikipedia Urea side reactions; products volatilize and recombine on condensation, contaminating process condensate |
| crystallization condition (vendor description) | urea solution evaporated, urea crystallized under vacuum; crystals centrifuged and dried n/a | SensoTech urea production process description |
| feed-solution concentration effect on granulation steam use | steam 0.01 MT/MT depends on concentration of feed urea solution MT steam per MT product | Toyo Spout Fluid Bed Granulation consumption per unit of service |


Recorded gaps:

- Evaporator stages, operating pressures/temperatures, melt concentration (wt%), heat duty, vendor — Fetch a urea finishing/evaporation OEM or licensor page directly.
- Evaporator stages, operating pressures/temperatures, melt concentration (wt%), heat duty, vendor — Fetch a urea finishing/evaporation OEM or licensor page directly.

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

## ex-wellhead

### CALM/SPM buoys, FPSO offtake, loading arms and custody transfer (ex-calm-spm-buoys-fpso-offtake-loading-arms-and-custody-transfer)

Primary code: UPS: Upstream
Offshore transfer of liquid cargo between floating production/storage facility or pipeline and tanker: mooring, weathervaning, hose transfer, swivel, PLEM and metering.
Vendors: Bluewater Energy Services, EPCM Holdings, OCIMF (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| PLEM footprint | 3-10 m (about 3x5 to 8x10 m) | EPCM SPM CALM guide: gravity base or piled, perimeter skirts for scour protection |
| Floating hose string length | 150-250 m (individual hoses 9-12 m); typical life 3-5 years | EPCM SPM CALM guide |
| Mooring hawser load capacity | 1000 metric tons (sometimes over, for VLCCs) | Nylon hawser for VLCC; typical life up to 2,000 hours of use |
| Anchor chain length (shallow SPM) | 200-400 m | EPCM SPM CALM guide; shallow water to 150 m typically stud-link chain; deep water uses Dyneema/HMPE composite legs |
| Flushing filtration | 50 micron particle removal | Treated seawater flushing with biocide, oxygen scavenger and corrosion inhibitor |


### Export to shore: onshore receiving terminal and sales specifications (ex-export-to-shore-onshore-receiving-terminal-and-sales-specifica)

Primary code: UPS: Upstream
Receive gas/condensate from export pipeline offshore, separate, stabilize, store, meter and dispatch to market to sales specifications.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Receive gas/condensate from export pipeline offshore, separate, stabilize, store, meter and dispatch to market to sales specifications. | Qualitative function from pages read in this sweep. |


### Flexible pipes, jumpers and bundled flowlines (ex-flexible-pipes-jumpers-and-bundled-flowlines)

Primary code: UPS: Upstream
Compliant pipe for connection of floating vessels/subsea equipment; flowlines, jumpers, risers, fluid transfer lines; bundled multiple services in one carrier pipe.
Vendors: Baker Hughes, TechnipFMC (CDS Separation Systems), Subsea7 (Swagelining all-polymer liner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Compliant pipe for connection of floating vessels/subsea equipment; flowlines, jumpers, risers, fluid transfer lines; bundled multiple services in one carrier pipe. | Qualitative function from pages read in this sweep. |


### Rigid flowlines, export pipelines and trunklines (ex-rigid-flowlines-export-pipelines-and-trunklines)

Primary code: UPS: Upstream
Transport oilfield fluids from wellhead/manifold to processing facility and from offshore facilities to onshore receiving terminals.
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, Subsea7 (Swagelining all-polymer liner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rigid pipeline diameter range | 4-18 inch | TechnipFMC rigid pipelines: 4-inch oilfield service fluids to 18-inch infield lines to larger export trunk lines |
| Installed pipe-in-pipe length | 1100 km | TechnipFMC more than 1,100 km installed pipe-in-pipe |


### Risers: SCR, top-tensioned, hybrid and free-standing (ex-risers-scr-top-tensioned-hybrid-and-free-standing)

Primary code: UPS: Upstream
Carry fluids between seabed flowlines/PLET and surface host; accommodate vessel motion and environmental loads.
Vendors: TechnipFMC (CDS Separation Systems), Subsea7 (Swagelining all-polymer liner), ABS (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Carry fluids between seabed flowlines/PLET and surface host; accommodate vessel motion and environmental loads. | Qualitative function from pages read in this sweep. |


### Subsea control and distribution systems (ex-subsea-control-and-distribution-systems-scm-sdu-mux-all-electr)

Primary code: UPS: Upstream
Remote monitoring and control of trees, manifolds, valves and chokes; distribute hydraulic power, electrical power, chemical injection and communications; enable ROV intervention.
Vendors: OneSubsea (SLB/Aker Solutions JV), Baker Hughes, Proserv, TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Remote monitoring and control of trees, manifolds, valves and chokes; distribute hydraulic power, electrical power, chemical injection and communications; enable ROV intervention. | Qualitative function from pages read in this sweep. |


### Subsea gas compression (ex-subsea-gas-compression)

Primary code: UPS: Upstream
Boost unprocessed well-stream gas on the seabed to reduce downstream pressure drop and defer or replace topside compression.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Boost unprocessed well-stream gas on the seabed to reduce downstream pressure drop and defer or replace topside compression. | Qualitative function from pages read in this sweep. |


### Subsea installation and protection (ex-subsea-installation-and-protection-anchors-trenching-burial-ro)

Primary code: UPS: Upstream
Stabilize and protect pipelines/umbilicals/structures against hydrodynamic loads, scour, dropped objects, trawling and iceberg scour; prepare seabed and correct spans.
Vendors: DeepOcean, Subsea7 (Swagelining all-polymer liner), CTC Marine (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| T1500+ jet trenching ROV depth | 500 m | DeepOcean T1500+: 1500 hp (1125 kW), up to 3.5 knots current, 3 m maximum burial capacity |
| UT-1 jetting ROV power | 2.1 MW total power | DeepOcean UT-1 described as world's most powerful jetting ROV |
| AMP1500 plough product handling | 1500 mm diameter | DeepOcean Advanced Multi-Pass Plough for pre-cut/post-lay ploughing of large diameter pipelines/trunklines |
| ACP2 cable plough capability | 300 mm diameter product; 5 m minimum bend radius | DeepOcean ACP2 for large diameter power cables |


### Subsea manifolds and templates (ex-subsea-manifolds-and-templates-production-injection-cluster-pl)

Primary code: UPS: Upstream
Gather and distribute production/injection flows, enable testing, isolation, sampling, metering and allocation; provide tie-in termination of flowlines and risers.
Vendors: OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Manifold water depth capability | 10000 ft | OneSubsea manifolds capability up to depths of 10,000 ft |
| Manifold pressure | 15000 psi | OneSubsea manifolds up to 15,000 psi |
| Manifold temperature | 175 deg C | OneSubsea manifolds up to 175 C |
| Manifold pressure rating | 20000 psi | TechnipFMC manifold and tie-in systems up to 20K psi |
| Manifold temperature rating | 350 deg F | TechnipFMC manifolds up to 350 F |
| Connection diameter | 30 ft | TechnipFMC manifolds up to 30 ft connection diameter |
| Pressure | 20000 psi | Value as printed in the cited source; no further qualifier stated. |
| Temperature | 350 deg F | Value as printed in the cited source; no further qualifier stated. |


### Subsea multiphase pumping and boosting (ex-subsea-multiphase-pumping-and-boosting)

Primary code: UPS: Upstream
Lower wellhead pressure, increase flow and recovery, compensate tieback pressure drop, mitigate slugging and manage hydrates/wax via pump heat.
Vendors: OneSubsea (SLB/Aker Solutions JV), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Lower wellhead pressure, increase flow and recovery, compensate tieback pressure drop, mitigate slugging and manage hydrates/wax via pump heat. | Qualitative function from pages read in this sweep. |


### Subsea separation, water handling and metering (ex-subsea-separation-water-handling-and-metering)

Primary code: UPS: Upstream
Separate gas/liquid and oil/water on the seabed, remove solids, and measure multiphase/wet-gas flows for allocation and control.
Vendors: OneSubsea (SLB/Aker Solutions JV), Baker Hughes / Emerson Roxar, TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Metering technology | Emerson Roxar wet-gas flow meter + Baker Hughes electric choke in IPM product | Baker Hughes Integrated Process Module |


### Subsea trees (ex-subsea-trees-christmas-trees)

Primary code: UPS: Upstream
Installed on the subsea wellhead to control flow into and out of the well; connect tubing and downhole devices to the seafloor and surface host; provide valve, choke and intervention interfaces.
Vendors: OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Operating temperature range | -18-176 deg C | OneSubsea subsea trees designed to operate in extreme temperature range |
| Maximum pressure | 15000 psi (>1,000 bar) | OneSubsea trees 'up to 15,000 psi, or more than 1,000 bar' |
| Production bore (wellhead vertical tree) | 7 inch | OneSubsea full deep-water capability and 7-inch production bore size for wellhead vertical trees |
| Tree pressure rating | 20000 psi | TechnipFMC vertical and horizontal subsea tree solutions for pressures up to 20,000 psi |
| Tree temperature rating | 400 deg F | TechnipFMC trees temperatures to 400 F |
| Tree water depth rating | 10000 ft | TechnipFMC trees water depths up to 10,000 ft |
| Deepest subsea completion record | 9627 ft | TechnipFMC EVDT subsea tree holds deepest subsea completion record |
| Tree sizes | 5-7 inch | Baker Hughes provides both 5-inch and 7-inch systems with up to 15,000 psi, water depths up to 10,000 ft; >1,600 trees supplied since 1962 |
| HPHT flowing temperature | 350 deg F | Baker Hughes HPHT tree system up to 15,000 psi and flowing temperatures up to 350 F |
| Aptara framework rating | 10000 psi (690 bar), 10,000 ft / 3,048 m, 300 F / 149 C | Aptara suite built around this framework |
| Depth | 10000 ft | Value as printed in the cited source; no further qualifier stated. |
| Pressure | 15000 psi | Value as printed in the cited source; no further qualifier stated. |
| Temperature | 175 deg C | Value as printed in the cited source; no further qualifier stated. |


### Subsea umbilicals (ex-subsea-umbilicals-electro-hydraulic-electrical-steel-tube-hybr)

Primary code: UPS: Upstream
Link surface and seafloor equipment: electric and fiber-optic signals, electrical power, hydraulic and chemical injection fluids; power boosting/compression and provide flowline heating.
Vendors: OneSubsea (SLB/Aker Solutions JV), Prysmian Group, Nexans, TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Link surface and seafloor equipment: electric and fiber-optic signals, electrical power, hydraulic and chemical injection fluids; power boosting/compression and provide flowline heating. | Qualitative function from pages read in this sweep. |


### Subsea wellheads, conductors and mudline wellhead systems (ex-subsea-wellheads-conductors-and-mudline-wellhead-systems-hpht)

Primary code: UPS: Upstream
Primary pressure barrier of a subsea well; anchor and suspension point; seal element for casing strings; supports BOP, tree and downhole control line pass-through.
Vendors: OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Welding procedure standards | API Spec 6A and 17D; ASME Section IX; NACE MR0175/ISO 15156; DNVGL-RP-C203 fatigue classes F3, D or C1 standard | OneSubsea subsea wellheads |


## exhaust

### Combustion air intake, filtration and silencers; exhaust system, mufflers, expansion joints (gas-engine-exhaust-emissions)

Primary code: PWR: Power and renewables
Combustion air intake, filtration and silencers; exhaust system, mufflers, expansion joints | Emissions control: oxidation catalyst, SCR, NOx/CO figures | Exhaust stacks, silencers and emission after-treatment
Vendors: INNIO Jenbacher, Johnson Matthey, Burgess-Manning (CECO Environmental), SVI BREMCO (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| BOP elements | Activated carbon absorber; exhaust gas silencer; exhaust gas heat exchanger qualitative | Jenbacher Type 6 and J920 Balance of Plant element lists |
| NOx reduction | 95-? % (greater than) | Johnson Matthey SCR systems for stationary diesel and gas engines; can be coupled with ammonia-slip or oxidation catalyst for CO, HC, NH3 and VOCs |
| Converter power range | 50-500 HP | Johnson Matthey Modulex C catalytic converter, stainless steel; Modulex B 250-2250 HP carbon/stainless; DualOx 2000 HP and larger |
| NOx emission basis | 250 / 500 mg/Nm3 @ 5% O2 dry exhaust | Jenbacher Type 6 and J920 published technical data; engine/genset emissions setting |
| NOx reduction vs Tier 2 diesel | 95-? % (greater than) | Jenbacher 100% hydrogen data-centre generator option; search-verified? NO - value is on the fetched Jenbacher data-centre page |
| Exhaust routing height | 8-? feet (2.3 m) above (personnel-work areas / combustible surfaces context) | Cummins Gas Power Plant Application Manual, exhaust section: route exhaust piping at least 8 feet (2.3 metres) above... (qualifier as printed in the manual) |
| Carbon steel exhaust thermal expansion | 0.0078 inches per foot of pipe per 100 deg F rise (1.17 mm per metre per 100 deg C) mm per m per 100 deg C | Cummins Gas Power Plant Application Manual, exhaust section; expansion joints required in long straight runs and every change of direction |
| Catalyst / SCR notes | oxidation catalyst located as close to engine as possible; catalyst bypass at start-up to protect from high exhaust temperatures; DEF approx. one-third urea and two-thirds water; SCR costly, heavy, needs careful doser sizing and ammonia-slip control qualitative | Cummins Gas Power Plant Application Manual, exhaust after-treatment section |
| Burgess-Manning preset vent silencer sizes | inlet diameter 2-12 in; casing diameter 8-24 in; standard design temperature 250 deg C; enhanced noise attenuation up to 50+ dB (typical, no guaranteed attenuation) inch / deg C / dB | Burgess-Manning Preset Vent Silencers product page, Technical Data / Design sections |
| Engine power | 50-500 / 250-2250 / >=2000 HP for Modulex C / Modulex B / DualOx | Value as printed in the cited source; no further qualifier stated. |
| Service interval | 15000 hours before maintenance, stated | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Silencer insertion-loss spectrum, exhaust backpressure and expansion-joint specification — Fetch a silencer/expansion-joint OEM datasheet (e.g. Veeder-Root/AMF/Beair)
- Combustion-air intake filtration classes for gas engines specifically — Fetch Jenbacher/Wartsila air-intake BOP datasheets
- CO and formaldehyde outlet figures with explicit basis (mg/Nm3, O2, temperature) — Fetch JM power-generation brochure PDF and Jenbacher EPA Tier 4 factsheet with a PDF reader
- Catalyst poison limits for siloxanes/sulphur in biogas — Fetch Wartsila 50SG leaflet and JM fuel-specification guidance

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
| Fan design | High efficiency backward curve blade design design feature | Zeeco Industrial Burners page Packaged Burners section |
| Scope | Each package burner system comes complete with automatic flame monitoring and shut-off, rotary air dampers, and a combustion air fan scope | Zeeco Industrial Burners page Packaged Burners section |
| Air fan design | Advanced combustion air fan wheel using less horsepower and less noise; silent operation design feature | SBR-30 product page Product Overview bullet 'Silent operation with an advanced combustion air fan wheel using less horsepower and less noise' |
| Air housing | Easy access air housing for internal components design feature | SBR-30 Product Overview bullet |


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

## feed

### Feed gas treatment - hydrotreating / hydrodesulfurisation and ZnO guard beds (ammonia-feed-gas-treatment)

Primary code: PCH: Petrochemicals
Feed gas treatment - hydrotreating / hydrodesulfurisation and ZnO guard beds
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| sulfur removal chemistry (H2S + ZnO -> ZnS + H2O) | ZnO fixed bed qualitative | Natural-gas feed, upstream of reformer; sulfur deactivates subsequent catalysts |
| HTZ-3 / HTZ-31 ZnO absorbent duty | high sulfur concentrations qualitative | Topsoe ammonia purification catalyst portfolio, high-density ZnO absorbent |
| HTZ-5 / HTZ-51 ZnO absorbent duty | low sulfur concentrations or low-temperature operation qualitative | Topsoe ammonia purification catalyst portfolio, high-purity large-surface-area ZnO |
| TK-250 / TK-261 hydrotreating catalyst feed range | natural gas to naphtha qualitative | Topsoe catalyst descriptions: TK-250 CoMo/alumina; TK-261 NiMo; hydrogenation of sulfur, chlorine and unsaturated compounds |
| desulfurisation section in conventional vs SynCOR ammonia | standard in both concepts qualitative | Topsoe SynCOR Ammonia comparison table |


Recorded gaps:

- ZnO sulfur capacity (wt%), operating temperature and space velocity for each absorbent grade — Fetch individual catalyst data sheets, e.g. https://www.topsoe.com/our-resources/knowledge/our-products/catalysts/htz-31
- Feed preheat exchanger train duty/temperature details — Find an authoritative ammonia plant heat-integration or EPC design page.
- ZnO sulfur capacity (wt%), operating temperature and space velocity for each absorbent grade — Fetch individual catalyst data sheets, e.g. https://www.topsoe.com/our-resources/knowledge/our-products/catalysts/htz-31
- Feed preheat exchanger train duty/temperature details — Find an authoritative ammonia plant heat-integration or EPC design page.

## feedwater

### Boiler feedwater pretreatment (boiler-feedwater-pretreatment)

Primary code: PWR: Power and renewables
Remove suspended solids, chlorine/oxidants, scale-forming calcium/magnesium hardness and alkalinity from raw/make-up water before it reaches the boiler, reducing scale, foaming, carryover and chemical demand. External (pre-boiler) treatment is preferred where possible; conditioning is only a supplement.
Vendors: Veolia Water Technologies, LANXESS, SUEZ Water Technologies (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ion-exchange resin bead diameter | 0.5 to 1.0 mm | Spirax Sarco description of resin beads in packed-bed GRP pressure vessel |
| Brine concentration for softener regeneration | 7-12 % NaCl solution | Base-exchange softening activation/regeneration (Spirax Sarco) |
| TDS reduction by sodium base exchange | 0 % reduction (none) | Spirax Sarco: no reduction in TDS and no change in pH; only exchange of scale-forming for non-scale-forming salts |
| Condensate return threshold for successful softener use in high alkaline hardness areas | >=50 % of condensate returned | Spirax Sarco, base exchange softening |
| Condensate return below which more sophisticated ion exchange / dealkalisation is preferable | <40 % | Spirax Sarco, shell boiler plant selection |
| pH after dealkalisation + degassing | 8.5-? pH (minimum) | CEA/ICOM BG04 §2.14: sodium hydroxide solution added after degassing to raise pH to at least 8.5 |
| Feed water total hardness — shell boiler | 2 max ppm as CaCO3 | CEA BG04 Table 2, recommended water characteristics for shell or coil boilers up to 32 bar g |
| Feed water pH at 25 °C — shell boiler / coil boiler | 8.5 to 9.5 / 9.5 to 11 pH units | CEA BG04 Table 2; note 1: with copper alloys in feed system shell-boiler value should not exceed pH 9.2 |
| Feed water alkalinity threshold for CO2 carryover | 25 ppm | CEA BG04 Table 2 note 5: >=25 ppm alkalinity results in about 10 ppm CO2 in the steam; dealkalisation or RO then recommended |
| Thermal conductivity of calcium carbonate scale | 0.9-2.6 W/mK | CEA BG04 Table 1, typical boiler scales (6.0–18.0 Btu in/h ft2 °F) |
| Steam velocity in well-designed steam system | 25-40 m/s | CEA BG04 §1.3 note: 25 m/s = 90 kph and up to 40 m/s = 145 kph; above 40 m/s deemed bad practice |
| Design principle | inclined plate clarification assuring laminar flow conditions n/a | Printed on Raw Water Pretreatment page |
| Installation attribute | reduced space; can be located indoors or relocated n/a | Printed on Raw Water Pretreatment page |
| Clarifier type | high rate, solids contact, sludge recirculation type n/a | Qualitative design description printed on Raw Water Pretreatment page; no numeric rating printed |
| Functions integrated in single unit | chemical addition and mixing, flocculation, upflow clarification n/a | Printed on Raw Water Pretreatment page |
| Applications | clarification, lime softening, silica reduction, organics reduction n/a | Printed on Raw Water Pretreatment page |
| Filter type | heavy duty, high rate gravity filter n/a | Printed on Raw Water Pretreatment page |
| Design duty | treating high turbidity loads and sticky particulates following polymer/coagulant treatment n/a | Printed on Raw Water Pretreatment page; no filtration rate printed |


Recorded gaps:

- Vendor-specific datasheet for activated-carbon filters / media sized for boiler make-up — Fetch a Veolia/Suez activated-carbon filter datasheet and record media type, bed depth and service-flow basis
- Dow/DuPont RO membrane element datasheet for boiler make-up — Fetch a current Dow/DuPont FILMTEC datasheet for brackish-water elements and record salt rejection, flow and test-pressure basis
- CFB-specific feedwater pretreatment guidance — Search DOE/EPRI or a CFB OEM (e.g. B&W) for CFB water chemistry guidance

### Deaerator vent condensers and feedtank internals (spray nozzles, trays, sparge pipes) (deaerator-vent-condenser-internals)

Primary code: PWR: Power and renewables
Mechanically remove dissolved oxygen and carbon dioxide by heating feedwater to saturation and breaking it into droplets/thin sheets in a steam atmosphere; collect deaerated water in a storage section under a steam blanket; vent non-condensables with a small controlled steam loss. Feedtank internals condense returned flash steam and mix cold make-up uniformly.
Vendors: Spirax Sarco, Veolia Water Technologies & Solutions, Warren Controls (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pressurised deaerator operating pressure / saturation temperature | 0.2 bar g / 105 bar g / °C | Spirax Sarco typical operating parameters |
| Deaerator storage capacity | 10-20 minutes of full-load boiler feed | Spirax Sarco typical operating parameters |
| Water supply pressure to deaerator | >=2 bar | Spirax Sarco: required for good distribution at the nozzle (1.8 bar assumed at nozzle inlet in worked example) |
| Steam supply pressure to pressure control valve | 5-10 bar | Spirax Sarco typical operating parameters |
| Maximum deaerator turndown | 5:1 ratio | Spirax Sarco; below this, nozzle/spray atomisation may be poor; multi-dome units used |
| Recommended deaerator vent rate | 0.5-2 kg steam/air mixture per 1000 kg/h deaerator capacity | Spirax Sarco: manufacturer recommendation on practical experience; DN20 steam-duty ball valve typically used part-open |
| Air and oxygen content of feedwater at 80 / 85 °C | 5.9 g air per 1000 kg at 80 °C; 2.3 g O2 per 1000 kg at 85 °C g per 1000 kg water | Spirax Sarco deaerator venting capacity worked example |
| Dissolved oxygen target — high-pressure water-tube / superheat plant | <7 ppb | Spirax Sarco: rate of attack rises rapidly with temperature; pressurised deaerators used |
| Feedtank operating temperature and residual oxygen | 85–90 °C leaves about 2 mg/L O2 °C / mg/L | Spirax Sarco Pressurised Deaerators; atmospheric practical maximum ~85 °C |
| Pressurised deaerator oxygen removal | 7 to 40 ppb O2 | DOE Steam Sourcebook: feedwater oxygen content by design of deaerator/deaerating heater |
| Feedtank vent size | DN80 on 2000 L tank-DN250 on 30000 L tank nominal diameter | Spirax Sarco feedtank design and atmospheric deaerator guidance; vent head with internal baffle |
| Feedtank storage capacity | 1 hour of steaming at maximum boiler evaporation | Spirax Sarco traditional practice; larger plants may use smaller hotwell plus cold treated-water storage |
| Fuel saving per feedtank temperature rise | 1 % less fuel per 6 °C rise in feedtank temperature | Spirax Sarco, condensate return |
| Feedpump cavitation risk threshold | >80 % condensate return (typical) | Spirax Sarco caution: excessive feedwater temperature can cause pump cavitation |
| Deaerator internal corrosion locations | Stainless-steel tray chamber SCC; inlet spray-valve spring cracking; vent-condenser oxygen pitting; impingement-baffle erosion near steam inlet qualitative | Veolia Water Handbook Ch.11, Deaerators section |


Recorded gaps:

- Vent-condenser duty/specification sizing method and tray vs spray nozzle performance comparison table — Fetch an OEM deaerator datasheet (e.g. Spirax, Warren Controls via alternate host) with textual tray/spray comparison and vent-condenser sizing basis
- Named deaerator OEM for gas-fired HRSG duty in Southeast Asia — Search for Siemens/GE Vernova/Veolia deaerator packages at regional combined-cycle plants

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
| Capacity TMV | 30000-500000 lb/hr | Product bullets: Model TMV 30,000-500,000 lb/hr |
| Capacity TMH | 500000-1000000 lb/hr | Product bullets: Model TMH 500,000-1,000,000 lb/hr |
| Residual dissolved oxygen | 0.005 cc/liter (7 ppb), less than | Product Overview: 'reducing dissolved oxygen content in boiler feedwater to levels less than .005 cc/liter (7 ppb)' |
| Configuration | Vertical or horizontal tray column; two-stage deaeration in a common vessel configuration | Product bullets and Product Overview |
| Standard | Exceeds ASME recommendations for oxygen level standard | Product Overview bullet |
| Capacity | 1500-135000 lb/hr | Product bullets: 1,500-135,000 lbs/hr |
| Type | Pressurized packed column deaerator type | Product bullets and narrative |
| Storage capacity | 10-30 minutes | Product Overview attribute: 'Storage capacities from 10 to 30 minutes' |
| Pumping | On/off or variable speed pumping configuration | Product bullets and Product Overview |


Recorded gaps:

- feedpump head, NPSH and duty for the packaged boiler lines — Read a feedpump selection sheet for a stated boiler duty.

## fire

### Fire protection and ammonia deluge/suppression (utility-fire-protection)

Primary code: PCH: Petrochemicals
Fire protection and ammonia deluge/suppression
Vendors: JBW Consulting Engineers (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Water uses on a chemical site | fire hydrants use | Raw water used for process cleaning and to supply fire hydrants |


## fl-system

### Blowout preventers (fl-blowout-preventers-annular-ram-bops-subsea-bop-stack-control-s-d23380)

Primary code: UPS: Upstream
Contain wellbore pressure and divert formation fluids/gases; shear pipe in emergency; provide surface, subsea and land pressure control.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Large-bore drilling BOP pressure rating | 20000 psi (stated as 20,000+ psi) | SLB/Cameron pressure control equipment page: 'first to engineer large-bore drilling BOPs rated 20,000+ psi for deepwater drilling' |
| Shear ram capability | can shear hardbanding on tool joints n/a | SLB/Cameron page: 'first to manufacture rams that can shear the hardbanding on tool joints' |
| Bore size | 7 1/16-21 1/4 in | Specifications | Bore sizes | 7 1/16 in to 21 1/4 in |
| Working pressure | 2,000-10,000 psi | Specifications | Working pressures | 2,000 to 10,000 psi |
| Body styles | Single and dual - | Specifications | Body styles | Single and dual |
| Optional gas bleed port | 3 in | Optional 3-in gas bleed port that runs from the ID to the OD |
| Packer elastomer | High-performance CAMULAR annular elastomer technology - | Specifications | Packer | High-performance CAMULAR annular elastomer technology |
| Bore size / working pressure (7 1/16, 11, 13 5/8 in) | 3,000-15,000 psi | Bore sizes and working pressures | 7 1/16, 11, and 13 5/8 in: 3,000 to 15,000 psi |
| Bore size / working pressure (16 3/4 in) | 3,000-10,000 psi | Bore sizes and working pressures | 16 3/4 in: 3,000 to 10,000 psi |
| Bore size / working pressure (20 3/4 in) | 3,000 psi | Bore sizes and working pressures | 20 3/4 in: 3,000 psi |
| Bore size / working pressure (21 1/4 in) | 2,000-10,000 psi | Bore sizes and working pressures | 21 1/4 in: 2,000, 5000, and 10,000 psi |
| Bore size / working pressure (26 3/4 in) | 3,000 psi | Bore sizes and working pressures | 26 3/4 in: 3,000 psi |
| Body styles | Single, double, triple, or quad - | Specifications | Body styles | Single, double, triple, or quad |
| Lock types | Standard: Manual; Optional: Hydraulic - | Specifications | Lock types | Standard: Manual Optional: Hydraulic |


### Blowout preventers (fl-blowout-preventers-annular-ram-bops-subsea-bop-stack-control-s)

Primary code: UPS: Upstream
Contain wellbore pressure and divert formation fluids/gases; shear pipe in emergency; provide surface, subsea and land pressure control.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Large-bore drilling BOP pressure rating | 20000 psi (stated as 20,000+ psi) | SLB/Cameron pressure control equipment page: 'first to engineer large-bore drilling BOPs rated 20,000+ psi for deepwater drilling' |
| Shear ram capability | can shear hardbanding on tool joints n/a | SLB/Cameron page: 'first to manufacture rams that can shear the hardbanding on tool joints' |


### Christmas trees (fl-christmas-trees-surface-and-subsea-dual-bore-horizontal-mudlin-bb5ee8)

Primary code: UPS: Upstream
Control flow in and out of wells, connect tubing to seafloor/above-water facilities, and provide pressure barrier and intervention access.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), TechnipFMC (CDS Separation Systems), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| OneSubsea subsea tree temperature range | -18-176 degrees Celsius | OneSubsea subsea trees page: 'extreme temperature ranging from minus 18 degrees Celsius to plus 176 degrees Celsius' |
| OneSubsea subsea tree pressure rating | 15000 psi (stated as 'up to 15,000 pounds per square inch, or more than 1,000 bar') | OneSubsea subsea trees page |
| Wellhead vertical tree production bore | 7 inches | OneSubsea subsea trees page, Features: '7-inch production bore size for wellhead vertical trees' |
| TechnipFMC subsea tree pressure rating | 20000 psi (pressures up to) | TechnipFMC well control page: vertical and horizontal subsea tree solutions for pressures up to 20,000 psi |
| TechnipFMC subsea tree temperature rating | 400 degrees Fahrenheit (temperatures to) | TechnipFMC well control page |
| TechnipFMC subsea tree water depth | 10000 ft (water depths up to) | TechnipFMC well control page |
| EVDT deepest subsea completion record | 9627 ft | TechnipFMC well control page: 'Our EVDT subsea tree holds the deepest subsea completion record at 9,627 feet' |


### Christmas trees (fl-christmas-trees-surface-and-subsea-dual-bore-horizontal-mudlin)

Primary code: UPS: Upstream
Control flow in and out of wells, connect tubing to seafloor/above-water facilities, and provide pressure barrier and intervention access.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), TechnipFMC (CDS Separation Systems), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| OneSubsea subsea tree temperature range | -18-176 degrees Celsius | OneSubsea subsea trees page: 'extreme temperature ranging from minus 18 degrees Celsius to plus 176 degrees Celsius' |
| OneSubsea subsea tree pressure rating | 15000 psi (stated as 'up to 15,000 pounds per square inch, or more than 1,000 bar') | OneSubsea subsea trees page |
| Wellhead vertical tree production bore | 7 inches | OneSubsea subsea trees page, Features: '7-inch production bore size for wellhead vertical trees' |
| TechnipFMC subsea tree pressure rating | 20000 psi (pressures up to) | TechnipFMC well control page: vertical and horizontal subsea tree solutions for pressures up to 20,000 psi |
| TechnipFMC subsea tree temperature rating | 400 degrees Fahrenheit (temperatures to) | TechnipFMC well control page |
| TechnipFMC subsea tree water depth | 10000 ft (water depths up to) | TechnipFMC well control page |
| EVDT deepest subsea completion record | 9627 ft | TechnipFMC well control page: 'Our EVDT subsea tree holds the deepest subsea completion record at 9,627 feet' |
| Design temperature | -18-176 degC | We design trees that can work in extreme temperature ranging from minus 18 degrees Celsius to plus 176 degrees Celsius |
| Design pressure | 15,000 psi | and at pressures of up to 15,000 pounds per square inch |
| Design pressure (metric equivalent) | 1,000 bar (more than) | or more than 1,000 bar |
| Production bore - wellhead vertical trees | 7 in | Features | Full deep-water capability and 7-inch production bore size for wellhead vertical trees |
| Tree configurations offered | Horizontal, wellhead vertical, and tubing head spool vertical trees - | Application | Horizontal, wellhead vertical, and tubing head spool vertical trees offered |
| Design temperature | -18-176 degC | We design trees that can work in extreme temperature ranging from minus 18 degrees Celsius to plus 176 degrees Celsius |
| Design pressure | 15,000 psi | and at pressures of up to 15,000 pounds per square inch |
| Design pressure (metric equivalent) | 1,000 bar (more than) | or more than 1,000 bar |
| Production bore - wellhead vertical trees | 7 in | Features | Full deep-water capability and 7-inch production bore size for wellhead vertical trees |
| Tree configurations offered | Horizontal, wellhead vertical, and tubing head spool vertical trees - | Application | Horizontal, wellhead vertical, and tubing head spool vertical trees offered |


### Connectors (fl-connectors-subsea-wet-mate-dry-mate-quick-flange-clamp-electri-a9a246)

Primary code: UPS: Upstream
Make separable hydraulic, electrical and optical connections subsea/downhole, and connect flowlines/tie-ins; provide sealing and corrosion protection in hostile environments.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Connection system internal pressure qualification | 20000 psi | TechnipFMC subsea infrastructure: all connection systems 'extensively tested and are qualified for internal pressures up to 20,000 psi and 3,000 m of water' |
| Connection system water depth qualification | 3000 m of water | Same TechnipFMC statement |
| Installed connection systems | 3000 systems (more than) | TechnipFMC: 'More than 3,000 of our connection systems are installed and operating worldwide' |
| Wet connector sealing architecture | dual-barrier system for mechanical and electrical sealing; dielectric-filled compensation wiper system protects receptacle contacts; crimped cable terminations; male pin gives immediate corrosion protection on de-mating n/a | OneSubsea wet connectors page, Application and Features |
| Wet connector environment capability | deepwater and high-pressure/high-temperature wellhead and downhole applications; many dry- and wet-mateable connectors resistant to sour environments and sand/silt ingress n/a | OneSubsea wet connectors page, Core benefits |
| Mated pressure rating, IE2-BC / IERD2-BC / IE4-BC / IE6,8 BC / IEB2 / IEB6,8 | 10000 psi | Wet Mate Series table, column 'Mated Pressure Rating (PSI)' |
| Mated pressure rating, IESQ4-BC / IESQ32-BC | 5000 psi | Wet Mate Series table |
| Mated pressure rating, IEB34 | 20000 psi | Wet Mate Series table |
| Voltage rating, IE series | 300 VDC | Wet Mate Series table, 'Voltage Rating (VDC)' |
| Voltage rating, IE Underwater Pluggable Series 3 | 600 VDC | Wet Mate Series table |
| Number of contacts, IE2-BC | 2-8 contacts | Wet Mate Series table, '# of Contacts' |
| Bulkhead thread, IE2-BC | 7/16"-20 in thread | Wet Mate Series table, 'Bulkhead Thread' |
| Contacts | 4 contacts | Main Characteristics: '4 contacts' |
| Rated current | 100 A | Main Characteristics: 'Rated current: 100 A' |
| Service voltage | 3,6/6 (7,2) kV | Main Characteristics: 'Service voltage: 3,6/6 (7,2) kV' |
| Pressure | ?-300 bar | Main Characteristics: 'Pressure: up to 300 bar' |
| Temperature | -5-40 degC | Main Characteristics: 'Temperature: -5°C to 40°C' |


### Connectors (fl-connectors-subsea-wet-mate-dry-mate-quick-flange-clamp-electri)

Primary code: UPS: Upstream
Make separable hydraulic, electrical and optical connections subsea/downhole, and connect flowlines/tie-ins; provide sealing and corrosion protection in hostile environments.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Connection system internal pressure qualification | 20000 psi | TechnipFMC subsea infrastructure: all connection systems 'extensively tested and are qualified for internal pressures up to 20,000 psi and 3,000 m of water' |
| Connection system water depth qualification | 3000 m of water | Same TechnipFMC statement |
| Installed connection systems | 3000 systems (more than) | TechnipFMC: 'More than 3,000 of our connection systems are installed and operating worldwide' |
| Wet connector sealing architecture | dual-barrier system for mechanical and electrical sealing; dielectric-filled compensation wiper system protects receptacle contacts; crimped cable terminations; male pin gives immediate corrosion protection on de-mating n/a | OneSubsea wet connectors page, Application and Features |
| Wet connector environment capability | deepwater and high-pressure/high-temperature wellhead and downhole applications; many dry- and wet-mateable connectors resistant to sour environments and sand/silt ingress n/a | OneSubsea wet connectors page, Core benefits |


### Hoses (fl-hoses-hydraulic-chemical-injection-mud-choke-and-kill-loading-c28966)

Primary code: UPS: Upstream
Flexible transfer of hydraulic power, chemicals, drilling fluids and fluids/gases between equipment; in umbilicals, hose elements carry hydraulic and chemical services.
Vendors: TechnipFMC (CDS Separation Systems), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Thermoplastic hose umbilical attributes | highly dynamic; short lead time; cost effective n/a | TechnipFMC umbilicals page, 'Umbilical products' list |
| Next-generation thermoplastic hose drivers | harsh environments, ultra-deepwater, elevated temperatures, longer tiebacks; shorter manufacturing lead time; simpler hose-to-end-fitting termination n/a | TechnipFMC umbilicals page, 'Next generation thermoplastic hose' |
| Hydraulic/chemical service in steel-tube umbilical | hydraulic fluid for control; various chemical fluids for injection into the flowline n/a | OneSubsea steeltube umbilicals page |
| Maximum working pressure | 14 bar | Page summary block 'Pressure 14 bar' and Additional Specifications 'Maximum Working Pressure: 14 BAR' |
| Temperature range | -30-100 degC | Additional Specifications: 'Temperature Range: -30°C to + 100°C' |
| Standard duty sizes | 1 in – 4 in (25 mm – 100 mm) in / mm | Additional Specifications: 'Standard Duty: 1” – 4” (25MM – 100MM)' |
| Heavy duty sizes | 4 in – 10 in (100 mm – 250 mm) in / mm | Additional Specifications: 'Heavy Duty: 4” – 10” (100MM – 250MM)' |
| Petrol hose standard, working pressure | 700 kPa at 20 degC | Petrol Hose Range overview, code 1000, 'Max Working Pressure (kPa @ Ambient Temp)' |
| Petrol hose heavy duty, working pressure | 1400 kPa at 20 degC | Petrol Hose HD code 901 table, 'Working Pressure kPa at 20ºC' |
| Chemical hose range standard | AS 2594-1983 standard | Chemical Hose Range AS 2594-1983 overview |
| Chemical hose PTSS working pressure | 1400 kPa at 20 degC | Chemical hose PTSS code 2200 table |
| Petrol hose temperature range | -30-80 degC | Code 1000 / 901 / 1003 product blocks: 'Temperature Range: -30ºC to +80ºC' |
| Chemical hose temperature range | -30-100 degC | Code 951 / 952 / 969 product blocks: 'Temperature Range: -30ºC to +100ºC' |
| Hot bitumen hose temperature range | -30-180 degC | Code 966 block: 'Temperature Range: -30ºC to +180ºC' |
| Kind 1 electrical resistance | ?-1.0 ohm/m | Petrol hose range overview: 'Kind 1 hose has an electrical resistance not greater than 1.0 ohm/m.' |


### Hoses (fl-hoses-hydraulic-chemical-injection-mud-choke-and-kill-loading)

Primary code: UPS: Upstream
Flexible transfer of hydraulic power, chemicals, drilling fluids and fluids/gases between equipment; in umbilicals, hose elements carry hydraulic and chemical services.
Vendors: TechnipFMC (CDS Separation Systems), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Thermoplastic hose umbilical attributes | highly dynamic; short lead time; cost effective n/a | TechnipFMC umbilicals page, 'Umbilical products' list |
| Next-generation thermoplastic hose drivers | harsh environments, ultra-deepwater, elevated temperatures, longer tiebacks; shorter manufacturing lead time; simpler hose-to-end-fitting termination n/a | TechnipFMC umbilicals page, 'Next generation thermoplastic hose' |
| Hydraulic/chemical service in steel-tube umbilical | hydraulic fluid for control; various chemical fluids for injection into the flowline n/a | OneSubsea steeltube umbilicals page |


### Injectors and injection systems (fl-injectors-and-injection-systems-water-injection-gas-injection-f8f339)

Primary code: UPS: Upstream
Provide reservoir pressure support and lift; inject treating chemicals for flow assurance and asset integrity; deliver seawater/gas/chemicals to the reservoir or production stream.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), Baker Hughes, SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| OneSubsea subsea pump operational hours | 5000000 operational hours (over) | OneSubsea subsea water injection page: 'track record of over 5 million operational hours' |
| OneSubsea subsea pumps delivered globally | 130 pumps (more than) | Same page: 'more than 130 pumps delivered globally' |
| OneSubsea subsea pumps for water injection | 14 pumps delivered and installed | Same page: 'OneSubsea has delivered and installed 14 of its subsea pumps for water injection purposes' |
| Seawater treatment configuration levels | 4 named configurations (raw seawater; coarse filtration; disinfection and particle removal; ultrafiltration and sulfate removal) | OneSubsea subsea water injection page, 'Seawater quality requirements' |
| Chemical injection case duration / scale | 9 months across 1,400 wells months / wells | Same SLB case-study headline |
| Standard temperature rating | 250 degF (121 degC) | A standard temperature rating of up to 250°F (121°C) |
| Standard temperature rating (metric) | 121 degC | A standard temperature rating of up to 250°F (121°C) |
| Discharge pressure | 350 bar | Periflow Compressors Performance: Up to 350 bar |
| Capacity flow | 10-20000 m3/hr | Periflow Compressors Performance: 10 to 20,000 m3/hr capacity flow |
| Variable speed | 1000-6000 rpm | Periflow Compressors Performance: Variable speed from 1000 to 6000 rpm |
| Compression stages | 5 stages (up to) | The Howden hybrid reciprocating compressor is available in horizontal or vertical configurations of up to five compression stages |
| Pressure increase | 450 bar (up to) | offering pressures increases of to 450 bar while providing inter-stage cooling and purging of condensates |
| Compression stages | 5 stages (up to) | The Howden hybrid reciprocating compressor is available in horizontal or vertical configurations of up to five compression stages |
| Pressure increase | 450 bar (up to) | offering pressures increases of to 450 bar while providing inter-stage cooling and purging of condensates |
| Flow rate range | 5 ml/h-180 m3/h ml/h to m3/h | Our portfolio includes systems featuring a flow rate between 5 ml/h and 180 m3/h at discharge pressure levels of up to 3500 bar |
| Discharge pressure - diaphragm pumps | 1,200 bar (up to) | With diaphragm pumps, the system is able to operate pressure levels of up to 1200 bar. |
| Discharge pressure - plunger pumps | 3,500 bar (up to) | Plunger pumps, meanwhile, enable discharge pressure levels of as much as 3500 bar to be achieved. |


### Injectors and injection systems (fl-injectors-and-injection-systems-water-injection-gas-injection)

Primary code: UPS: Upstream
Provide reservoir pressure support and lift; inject treating chemicals for flow assurance and asset integrity; deliver seawater/gas/chemicals to the reservoir or production stream.
Vendors: SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), Baker Hughes, SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| OneSubsea subsea pump operational hours | 5000000 operational hours (over) | OneSubsea subsea water injection page: 'track record of over 5 million operational hours' |
| OneSubsea subsea pumps delivered globally | 130 pumps (more than) | Same page: 'more than 130 pumps delivered globally' |
| OneSubsea subsea pumps for water injection | 14 pumps delivered and installed | Same page: 'OneSubsea has delivered and installed 14 of its subsea pumps for water injection purposes' |
| Seawater treatment configuration levels | 4 named configurations (raw seawater; coarse filtration; disinfection and particle removal; ultrafiltration and sulfate removal) | OneSubsea subsea water injection page, 'Seawater quality requirements' |
| Chemical injection case duration / scale | 9 months across 1,400 wells months / wells | Same SLB case-study headline |


### Pipelines and flowlines (fl-pipelines-and-flowlines-rigid-flexible-pipe-in-pipe-heated-tru-509b41)

Primary code: UPS: Upstream
Transport produced fluids from well/tie-back to host and export, and injection fluids from host to wells; flow assurance (heating/insulation) where required.
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rigid pipeline water depth | tens to thousands m (descriptive) | TechnipFMC subsea infrastructure page |
| Global spoolbases | 4 facilities | TechnipFMC subsea infrastructure: 'use of our four strategically located global spoolbases' |
| Flexible pipe vs rigid installation speed | 20 times faster (up to, method-dependent) | Baker Hughes flexible pipe systems: minimizes offshore welding; flexible pipes can be recovered and redeployed |


### Pipelines and flowlines (fl-pipelines-and-flowlines-rigid-flexible-pipe-in-pipe-heated-tru)

Primary code: UPS: Upstream
Transport produced fluids from well/tie-back to host and export, and injection fluids from host to wells; flow assurance (heating/insulation) where required.
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rigid pipeline water depth | tens to thousands m (descriptive) | TechnipFMC subsea infrastructure page |
| Global spoolbases | 4 facilities | TechnipFMC subsea infrastructure: 'use of our four strategically located global spoolbases' |
| Flexible pipe vs rigid installation speed | 20 times faster (up to, method-dependent) | Baker Hughes flexible pipe systems: minimizes offshore welding; flexible pipes can be recovered and redeployed |
| Nominal pressure rating | 500 psi (3.45 MPa) | Specifications table: '500 psi (3.45 MPa) API 15S Nominal Pressure Rating (NPR)' |
| Maximum temperature | 140 degF (60 degC) | Product Offering table: 'Max Temp | 140°F (60°C)' |
| Inside diameter, DF 3in 500 | 72 mm | Series 500 Product Properties table, column 'DF 3" 500', row 'Inside Pipe Diameter' |
| Inside diameter, DF 4in 500 | 91 mm | Series 500 Product Properties table, column 'DF 4" 500', row 'Inside Pipe Diameter' |
| Inside diameter, DF 6in 500 | 142 mm | Series 500 Product Properties table, column 'DF 6" 500', row 'Inside Pipe Diameter' |
| Outside diameter, DF 6in 500 | 173 mm | Series 500 Product Properties table, column 'DF 6" 500', row 'Outside Pipe Diameter' |
| Pipe weight, DF 6in 500 | 8.53 kg/m | Series 500 Product Properties table, column 'DF 6" 500', row 'Pipe Weight' |
| Factory hydrotest | 1.5x nominal pressure rating ratio | Product Offering: '100% hydrotested at the factory to 1.5x the nominal pressure rating.' |
| Connection | Flange and pipe to pipe n/a | Product Offering table, row 'Connection' |
| Rated power (4 throw / 6 throw) | 6668-10000 BHP | Product tables: Rated Power 6,668 (4 Throw) and 10,000 (6 Throw); page text: rated up to 10,000 BHP |
| Stroke | 7.25-8.5 in (KBB 7.25 / KBV 8.50) | Product table: Stroke (in) KBB 7.25, KBV 8.50 |
| Max RPM | 750-900 rpm (KBB 900 / KBV 750) | Product table: Max RPM KBB 900, KBV 750 |


### Risers (fl-risers-rigid-scr-top-tensioned-flexible-hybrid-free-standing-542b1e)

Primary code: UPS: Upstream
Convey produced fluids or injection/power services between subsea wells/tie-backs and a fixed or floating surface host; accommodate platform motion, pressure and thermal load.
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flexible pipe high-pressure resistance | high-pressure resistant (qualitative; no numeric rating published on page) n/a | TechnipFMC flexible-pipe page: helically wound corrosion-resistant steel wires give high-pressure resistance and bending characteristics; independent layers adapted per field |
| Rigid pipeline water depth capability | tens to thousands m of water (descriptive range, not a precise figure) | TechnipFMC subsea infrastructure: rigid pipelines installed 'in water depths from tens to thousands of meters offshore'; four global spoolbases and pipelay fleet |
| Flexible pipe installation speed advantage | 20 times faster (depending on method) | Baker Hughes flexible pipe systems: manufactured onshore, ready to install, minimizes offshore welding; 'up to 20 times faster depending on the method' |
| FSHR tensioning method | near-surface buoyancy can n/a | TechnipFMC FSHR description: vertical steel pipe tensioned by a near-surface buoyancy can; flexible jumper to production platform; foundation at seabed; rigid base jumper to PLET |
| Fluid transfer line applications | riser, flowline, jumper, fluid transfer line; high H2S, dense CO2, high temperature n/a | Baker Hughes flexible pipe systems overview and applications list |
| installed base - refineries | 45 % | Value as printed in the cited source; no further qualifier stated. |
| O&G processing plants | 500 plants (over) | Value as printed in the cited source; no further qualifier stated. |
| Global FPV applications | 4 GW (over) | Value as printed in the cited source; no further qualifier stated. |
| Example project | 192 MW (Cirata, Indonesia) | Value as printed in the cited source; no further qualifier stated. |
| Documented application | oil-in-water separation (Oman case study) n/a | SLB Processing and Separation page case-study title |
| Max power | 670 W | Value as printed in the cited source; no further qualifier stated. |
| Module efficiency | 24.8 % | Value as printed in the cited source; no further qualifier stated. |
| STC Pmax (660M) | 660 W | Value as printed in the cited source; no further qualifier stated. |
| Front static load | 5400 Pa | Value as printed in the cited source; no further qualifier stated. |
| Pmax temp coefficient | -0.26 %/degC | Value as printed in the cited source; no further qualifier stated. |
| RF physical layer | 2.4 GHz DSSS O-QPSK (IEEE 802.15.4-2006) GHz | Value as printed in the cited source; no further qualifier stated. |
| MAC | TDMA data-link layer protocol | Value as printed in the cited source; no further qualifier stated. |


### Risers (fl-risers-rigid-scr-top-tensioned-flexible-hybrid-free-standing)

Primary code: UPS: Upstream
Convey produced fluids or injection/power services between subsea wells/tie-backs and a fixed or floating surface host; accommodate platform motion, pressure and thermal load.
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flexible pipe high-pressure resistance | high-pressure resistant (qualitative; no numeric rating published on page) n/a | TechnipFMC flexible-pipe page: helically wound corrosion-resistant steel wires give high-pressure resistance and bending characteristics; independent layers adapted per field |
| Rigid pipeline water depth capability | tens to thousands m of water (descriptive range, not a precise figure) | TechnipFMC subsea infrastructure: rigid pipelines installed 'in water depths from tens to thousands of meters offshore'; four global spoolbases and pipelay fleet |
| Flexible pipe installation speed advantage | 20 times faster (depending on method) | Baker Hughes flexible pipe systems: manufactured onshore, ready to install, minimizes offshore welding; 'up to 20 times faster depending on the method' |
| FSHR tensioning method | near-surface buoyancy can n/a | TechnipFMC FSHR description: vertical steel pipe tensioned by a near-surface buoyancy can; flexible jumper to production platform; foundation at seabed; rigid base jumper to PLET |
| Fluid transfer line applications | riser, flowline, jumper, fluid transfer line; high H2S, dense CO2, high temperature n/a | Baker Hughes flexible pipe systems overview and applications list |
| registered interoperable products | 1000 products (over) | Value as printed in the cited source; no further qualifier stated. |
| wiring | two-wire twisted pair; IS/non-incendive power wiring | Value as printed in the cited source; no further qualifier stated. |
| Sealing | dual-barrier mechanical and electrical sealing; dielectric-filled wiper protection; crimped terminations n/a | OneSubsea wet connectors page |
| Environment | deepwater, HPHT wellhead and downhole; sour-resistant options n/a | OneSubsea wet connectors page |
| Single-stage flow envelope | 1500-600000 m3/h | Value as printed in the cited source; no further qualifier stated. |
| Multistage flow envelope | 400-200000 m3/h | Value as printed in the cited source; no further qualifier stated. |
| Pressure ratio | 3.5-10 ratio depending on series | Value as printed in the cited source; no further qualifier stated. |
| CKD discharge pressure | 20 MPa | Value as printed in the cited source; no further qualifier stated. |
| Global FPV applications | 4 GW (over) | Value as printed in the cited source; no further qualifier stated. |
| Example project | 192 MW (Cirata, Indonesia) | Value as printed in the cited source; no further qualifier stated. |
| installed base - refineries | 45 % | Value as printed in the cited source; no further qualifier stated. |
| O&G processing plants | 500 plants (over) | Value as printed in the cited source; no further qualifier stated. |


### Separators (fl-separators-2-3-phase-horizontal-vertical-spherical-compact-in-46519c)

Primary code: UPS: Upstream
Separate and treat oil, water and gas; remove solids and liquids; prepare hydrocarbons for export or injection.
Vendors: SLB (Cameron pressure control equipment), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Separation design objective | separate and treat oil, water and gas using minimal chemicals and energy to reduce capex and opex n/a | SLB Processing and Separation overview; process pilot testing used to optimize technology selection |
| Produced-water oil recovery case result | 98 % of oil content recovered | SLB Processing and Separation page case-study title: 'Advanced Media Filter Technology Recovers 98% of Oil Content from Heavily Emulsified Produced Water' |
| Subsea separation control | all-electric control systems n/a | OneSubsea water injection page, related resource 'Subsea separation': 'phase and fluid separation features all-electric control systems' |
| Working pressure rating | 500-2,000 psi | Product specifications | Rated for working pressures from 500 to 2,000 psi |
| Inlet diameter | 84 in (up to) | Product specifications | Inlet diameter up to 84 in |
| Phase configurations | Two-, three-, or four-phase separator test units - | Product specifications | Two-, three-, or four-phase separator test units |
| Vessel orientation | Horizontal or vertical - | Product specifications | Horizontal or vertical orientation of vessels |
| Service rating | Sweet or sour service rated - | Product specifications | Sweet or sour service rated |
| Design code / sour service | ASME Section VIII, Division 1 and NACE MR0175 for H2S environments - | The 3-phase separator is built in compliance with ASME Section VIII, Division 1 and NACE MR0175 for H2S environments. |
| Working pressure rating | 500-2,000 psi | Product specifications | Rated for working pressures from 500 to 2,000 psi |
| Inlet diameter | 84 in (up to) | Product specifications | Inlet diameter up to 84 in |
| Phase configurations | Two-, three-, or four-phase separator test units - | Product specifications | Two-, three-, or four-phase separator test units |
| Vessel orientation | Horizontal or vertical - | Product specifications | Horizontal or vertical orientation of vessels |
| Service rating | Sweet or sour service rated - | Product specifications | Sweet or sour service rated |
| Design code / sour service | ASME Section VIII, Division 1 and NACE MR0175 for H2S environments - | The 3-phase separator is built in compliance with ASME Section VIII, Division 1 and NACE MR0175 for H2S environments. |


### Separators (fl-separators-2-3-phase-horizontal-vertical-spherical-compact-in)

Primary code: UPS: Upstream
Separate and treat oil, water and gas; remove solids and liquids; prepare hydrocarbons for export or injection.
Vendors: SLB (Cameron pressure control equipment), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Separation design objective | separate and treat oil, water and gas using minimal chemicals and energy to reduce capex and opex n/a | SLB Processing and Separation overview; process pilot testing used to optimize technology selection |
| Produced-water oil recovery case result | 98 % of oil content recovered | SLB Processing and Separation page case-study title: 'Advanced Media Filter Technology Recovers 98% of Oil Content from Heavily Emulsified Produced Water' |
| Subsea separation control | all-electric control systems n/a | OneSubsea water injection page, related resource 'Subsea separation': 'phase and fluid separation features all-electric control systems' |


### Subsea umbilicals (fl-subsea-umbilicals-electro-hydraulic-electrical-fibre-optic-ste-15ccf3)

Primary code: UPS: Upstream
Provide the critical link between onshore/offshore hosts and subsea facilities: control, hydraulic power, chemical injection, electrical power and communications.
Vendors: TechnipFMC (CDS Separation Systems), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), Nexans (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Steeltube umbilical service content | hydraulic fluid for control; various chemical fluids for injection into flowline; electrical power; electrical- or fibre-optic signal transmission n/a | OneSubsea steeltube umbilicals page, opening definition |
| Steeltube umbilical armour / bending | no armour; can be bent in any direction, eliminating 'bird caging'; long lay (pitch) length with components supported within channel elements n/a | OneSubsea steeltube umbilicals core benefits and features |
| Umbilical systems track record | 40 years | TechnipFMC umbilicals page: 'Supplying customized subsea umbilical systems for 40 years'; 40-year record of excellence in project execution |
| Umbilical manufacturing locations | 3 plants (United Kingdom, United States, Angola) | TechnipFMC umbilicals page: strategically located plants in UK, US and Angola |
| Dynamic cable voltage (subsea compression power) | 145 kV HVAC | Nexans Jansz-Io project: turnkey design, manufacturing and installation of a 145 kV HVAC dynamic cable |


### Subsea umbilicals (fl-subsea-umbilicals-electro-hydraulic-electrical-fibre-optic-ste)

Primary code: UPS: Upstream
Provide the critical link between onshore/offshore hosts and subsea facilities: control, hydraulic power, chemical injection, electrical power and communications.
Vendors: TechnipFMC (CDS Separation Systems), SLB OneSubsea (SLB / Aker Solutions / Subsea7 joint venture), Nexans (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Steeltube umbilical service content | hydraulic fluid for control; various chemical fluids for injection into flowline; electrical power; electrical- or fibre-optic signal transmission n/a | OneSubsea steeltube umbilicals page, opening definition |
| Steeltube umbilical armour / bending | no armour; can be bent in any direction, eliminating 'bird caging'; long lay (pitch) length with components supported within channel elements n/a | OneSubsea steeltube umbilicals core benefits and features |
| Umbilical systems track record | 40 years | TechnipFMC umbilicals page: 'Supplying customized subsea umbilical systems for 40 years'; 40-year record of excellence in project execution |
| Umbilical manufacturing locations | 3 plants (United Kingdom, United States, Angola) | TechnipFMC umbilicals page: strategically located plants in UK, US and Angola |
| Dynamic cable voltage (subsea compression power) | 145 kV HVAC | Nexans Jansz-Io project: turnkey design, manufacturing and installation of a 145 kV HVAC dynamic cable |
| Umbilical types | Steel Tube Umbilicals; Thermoplastic Hose Umbilicals; Power Umbilicals; IWOCS Umbilicals n/a | Products page headings and captions. |
| Flying lead conduit | Steel tubes or thermoplastic hoses; modular hydraulic, electro-hydraulic and hybrid designs n/a | Hydraulic Flying Leads section: 'Combining a primary conduit section—typically steel tubes or thermoplastic hoses...' |
| Uta configuration | Modular components; configurable side panels for hydraulic, electrical and fiber optic connectivity n/a | Subsea Umbilical Termination Assemblies section. |
| Ancillary hardware | Umbilical I- and J-Tube Seals; Pull-In and Hang Off Systems; Subsea Umbilical Termination Interfaces; Tie Back or Tie Down Collars; Subsea Umbilical Weak Links n/a | Topside Connection Hardware and Ancillary Equipment section. |
| Power rating per connection | 66 kV | Benefits callout: '66kV / Power rating per connection' |
| Maintenance-free life | 30 yr | Benefits callout: '30 yrs / Maintenance-free life' |
| Water depth | ?-1500 m | Benefits callout: '↓ 1500m / Water depth' |
| Mating | Wet-mate-only cable connections; seabed-resident, reconnection without retrieval n/a | Overview: 'Subsea junction boxes offer versatile, wet-mate-only cable connections on the seafloor.' |
| Power rating per connection | 66 kV | Benefits callout: '66kV / Power rating per connection' |
| Maintenance-free life | 30 yr | Benefits callout: '30 yrs / Maintenance-free life' |
| Water depth | ?-1500 m | Benefits callout: '↓ 1500m / Water depth' |
| Mating | Wet-mate-only cable connections; seabed-resident, reconnection without retrieval n/a | Overview: 'Subsea junction boxes offer versatile, wet-mate-only cable connections on the seafloor.' |


## flare

### Flare, relief, vent gas recovery and fugitive emission control (ammonia-flare-vent-control)

Primary code: PCH: Petrochemicals
Flare, relief, vent gas recovery and fugitive emission control | Flare and relief systems (ammonia and urea relief, liquid seal drums)
Vendors: Howden (a Chart Industries company; KK&K, CKD brands), American Petroleum Institute, Zeeco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flare sonic tip upstream pressure threshold | 5 bar | Sonic flare tip used when upstream pressure > 5 bar |
| Personnel continuous-exposure thermal radiation limit | 1.58 kW/m2 (500 Btu/hr.ft2) | Maximum recommended radiation for continuous exposure of personnel in appropriate clothing (API Std 521 Table 12 cited) |
| Short-time flare radiation limits | 4.73 kW/m2 (3-4 min); 6.31 kW/m2 (30 s) kW/m2 | Higher radiation permitted for reduced exposure times (API Std 521 cited) |
| Howden EMISSIONGUARD TR2 packing ring vent-gas reduction (cumulative company figure) | 20,173,000 Nm3 (693,144,000 scf) of gas prevented from leaking Nm3 | Estimated cumulative reduction through packing-case vents, mainly petrochemical/natural-gas compression; equivalent to 60,500 t CO2 |
| Number of flare types typically used in a urea plant | 4 types | Urea plants typically employ four flare types for various relief streams: ammonia, discontinuous, continuous and main |
| Ammonia flare design exit velocity | restricted / low qualitative | Ammonia has low flame propagation speed, low heating value and low flame temperature; exit velocity must be restricted for residence time and flame stability; tip diameter controls maximum design exit velocity |
| Continuous flare minimum exit velocity | higher than flame velocity of waste stream design rule | Prevents flashback into flare stack and upstream equipment where oxygen is present |
| Liquid seal drum interaction with ammonia | ammonia dissolves in water forming corrosive ammonia solution qualitative | LSD commonly separates flare system from upstream header; often designed so all water is carried out during flaring and refilled afterwards |


Recorded gaps:

- Ammonia plant relief scenario list, flare header sizing and ammonia-specific vent recovery design — Fetch EFMA/AIChE ammonia safety guidance or an EPC flare-design page.
- Ammonia plant relief scenario list, flare header sizing and ammonia-specific vent recovery design — Fetch EFMA/AIChE ammonia safety guidance or an EPC flare-design page.

## fluidised

### Fluidised bed cooler / product cooler (urea-fluid-bed-cooler)

Primary code: PCH: Petrochemicals
Fluidised bed cooler / product cooler
Vendors: Toyo Engineering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fluidising cooler power | 24 kWh/MT | Toyo typical, in case of fluidizing product cooler |
| bulk flow cooler power | 19 kW/MT (as printed) | Toyo note for bulk flow cooler by cooling water |


Recorded gaps:

- Cooler duty, air volume, residence time, vendor models other than Toyo — Fetch a bulk-solids cooler OEM page.
- Cooler duty, air volume, residence time, vendor models other than Toyo — Fetch a bulk-solids cooler OEM page.

## fuel-gas

### Fuel gas system: pressure regulation, gas train, filters, scrubbers, booster/compressor, day tank (gas-engine-fuel-gas-system)

Primary code: PWR: Power and renewables
Fuel gas system: pressure regulation, gas train, filters, scrubbers, booster/compressor, day tank (liquid) | Fuel gas storage, compression, drying and pressure-reduction train
Vendors: INNIO Jenbacher, Everllence, Woodward, AERZEN (Aerzener Maschinenfabrik GmbH), Cummins Inc., Schneider Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Fine filter rating | 3 um | Jenbacher gas train, 3 micrometre fine filter as a security filter; part of minimum scope of supply |
| Hydrogen admixture (pipeline gas) | 25 vol % | Jenbacher 'Ready for H2' option, up to 25 vol% hydrogen in pipeline gas; data-centre page |
| Hydrogen admixture | 25 % | Everllence 51/60G and 35/44G TS gas mixture; gas fuel engines overview |
| Gas filter rating | 50 micron | Cummins Gas Power Plant Application Manual section 3.4.3.1: 'This is a 50 micron rating filter used for all gases and air' |
| Regulator outlet pressure (adjustable range) | 100-160 mbar | Cummins Gas Power Plant Application Manual section 3.4.3.1: regulator output pressure generally adjustable between 100 and 160 mbar |
| Regulator inlet pressure (general range) | 1.25-4.0 bar | Cummins Gas Power Plant Application Manual section 3.4.3.1: depends on valve seat diameter of the pressure regulating valve |
| LNG storage volume for 12 h operation of one 10 MW engine | ?-<50 m³ (~1,700 ft³) | Schneider Electric White Paper 286, section 'Storing gas on site for increased availability': less than 50 m³ sufficient for 12 hours at 10 MW; LNG kept below -162 C in insulated cryogenic tanks |
| On-site fuel storage design requirement (hyperscale DC study) | 48 hours at full load capacity hours | Schneider Electric White Paper 286, 'A gas power plant architecture overview': study set the on-site gas storage requirement at 48 h assuming full load |
| Gas distribution redundancy | fully redundant 2 x 100% gas distribution; physically separated main feeders; LNG storage A/B with pressure reduction stations A/B; gas-leak sections automatically isolated qualitative | Schneider Electric White Paper 286, 'Gas supply system architecture' and Figure 10 |
| Medium-speed engine gas admission pressure | 6-7 bar (85-100 psi) | Schneider Electric White Paper 286, 'Gas engine technology': medium-speed engines supply gas individually to each cylinder inlet, requiring around 6-7 bar |
| AERZEN GM-HP gas booster volume flow | 50-38000 m³/h | AERZEN product page Technical data: High Pressure Gas Booster Series GM-HP, positive displacement blowers, oil-free conveying of process gases |
| AERZEN GM-HP differential pressure | 150-2000 mbar | AERZEN product page Technical data (1 or 2 stage design, separate pressurised oil lubrication, oil-free gas transport) |
| Volume flow | 50-38000 m³/h | Product page Technical data; positive displacement blower, 1 or 2 stage |
| Differential pressure | 150-2000 mbar | Product page Technical data |
| Conveying | oil-free; medium process gases; magnetic-coupling sealing; two-lobe gas-tight rotors qualitative | Product page advantages/technical data |


Recorded gaps:

- Gas inlet pressure range, pressure-regulation setpoints, booster/compressor curve and scrubber sizing — Fetch gas-train data sheet from Jenbacher resource hub and a gas booster OEM datasheet
- Liquid day-tank capacity for dual-fuel standby — Fetch Everllence 51/60DF fact sheet

## gas

### Gas detection (utility-gas-detection)

Primary code: PCH: Petrochemicals
Gas detection (ammonia detectors, fire and gas system)
Vendors: MSA Safety (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ultrasonic leak detector range | 17-28 m | Typical detection ranges 17-28 m depending on microphone technology; suitable only for pressurised installations from 2 bar (29 psi); MSA Observer i |
| Laser open-path NH3 measuring range | ?-15000 ppm.m | Measuring range up to 0-15000 ppm.m; path lengths 5-40 m and 40-120 m; MSA Senscient ELDS |
| Point catalytic bead range | 0-100 %LEL | Typical measuring range 0-100 %LEL; MSA ULTIMA X5000 / General Monitors S5000 / TG5000 / PrimaX P |
| Point electrochemical NH3 range | 0-100 ppm and 0-1,000 ppm ppm | Typical measuring ranges for direct measurement of ammonia at occupational exposure levels; sensor life 1-2 years (XCell ammonia sensor >5 years per footnote) |


## generator

### Generator / alternator (gas-engine-alternator)

Primary code: PWR: Power and renewables
Generator / alternator (synchronous, brushless, PMG excitation, AVR)
Vendors: Mecc Alte, Cummins Generator Technologies, Basler Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rating range | 800-1300 kVA | Mecc Alte ECO43, 4-pole brushless synchronous MV/HV, @50Hz / class H / 40C / PF0.8, referred to an 11kV unit; up to 13.8 kV |
| Voltage | 13.8 kV | Mecc Alte ECO43/46/47/49 medium and high voltage, up to; 50/60Hz, 1500/1800 rpm; IP23 (up to IP45 on request for ECO43-47) |
| Alternator rating range | 7.5-11200 kVA | Cummins STAMFORD / AvK alternators, combined range; HQ England, UK; operations in 116 countries |
| Generator voltage | 10.5 / 11 kV | Jenbacher J920 FleXtra 50Hz genset scope of supply; 60Hz 480V-13.8kV |
| Combined range | 7.5-11200 kVA | Value as printed in the cited source; no further qualifier stated. |
| Global coverage | 116 countries | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Alternator efficiency and short-circuit withstand for the specific gas-genset voltage ratings — Fetch Mecc Alte ECO-series technical data sheets and STAMFORD AvK product selector
- Confirm PMG use for large MV/HV gas gensets (>3 MVA) — Fetch Mecc Alte Quick Selection Guide REV 8.1 and Jenbacher J920 alternator data

## genset

### Skid / packaged genset and enclosure (gas-engine-packaged-genset-enclosure)

Primary code: PWR: Power and renewables
Skid / packaged genset and enclosure (containerised, outdoor, acoustic) | Acoustic enclosures and noise barriers
Vendors: INNIO Jenbacher, Rehlko, Rolls-Royce Power Systems (mtu), Burgess-Manning (CECO Environmental) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Container length | 12192 mm | Jenbacher Type 2/3/4 generator container, standard 40 ft; width 8 ft (~2438 mm) or ~10 ft (~3000 mm); height 2591-2896 mm |
| Sound pressure level | 65 dB(A) at 10 m | Jenbacher Type 2/3/4 container overall package, surface sound pressure level per DIN 45635; lower levels on request |
| Ambient temperature range | -25-34 degC | Jenbacher Type 2/3/4 container standard ventilation; option for -40C and (most variants) +45C |
| Type 6 container dimensions | 13,500-20,500 / 3,000-4,000 / ~7,500 mm L/W/H | Jenbacher Type 6 single-bank (two-module) container; main unit without roof-mounted equipment; capacity 1634-4507 kW |
| Enclosure acoustic design measures | sound attenuation built into air inlet/outlet; linings of fibreglass, drywall with fibreglass, insulated perforated airfoils or foam; evaluate flame retardance and resistance to oil/contaminants; 90-degree duct bend reduces high-frequency noise; high-mass line-of-sight barriers (sand-filled cement block or brick) qualitative | Cummins Gas Power Plant Application Manual, Noise Attenuation Support (3.6.7) |
| Enclosure doors and windows | shall meet the site noise reduction requirement qualitative | Cummins Gas Power Plant Application Manual, enclosure design section |
| Vendor enclosure product families | Acoustic Enclosures, Acoustic Buildings, Acoustic Shrouds, Acoustic Walls and Noise Barriers, Acoustic Louvers, Acoustic Containers, Engine Test Cells product families (no figures) | Burgess-Manning product navigation and company page read this session |
| Power | 249-1562 / 1634-4507 kW for Type 2/3/4 / Type 6 | Value as printed in the cited source; no further qualifier stated. |
| Sound | 65 dB(A) at 10 m, DIN 45635 (Type 2/3/4); 65/70/75/80 for Type 6 | Value as printed in the cited source; no further qualifier stated. |
| Ambient | -25 to +34 / -25 to +40 degC, Type 2/3/4 / Type 6 standard ventilation | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Verified Rehlko POD enclosure sound and dimension table — Fetch the Rehlko POD PDF directly via a different fetch path or PDF reader
- Bus duct and container fire-system specifications — Fetch Jenbacher container factsheet and Rehlko POD standard-features list

## granulator

### Urea fluid-bed granulator (urea-fluid-bed-granulator)

Primary code: PCH: Petrochemicals
Fluid-bed unit that builds urea granules from sprayed melt onto seed particles, with internal recycling and classification to hold a target granule size. Granules are larger and harder than prills, which suits bulk blending and reduces caking.
Vendors: thyssenkrupp Uhde, Stamicarbon, Toyo Engineering, Casale, Casale, UreaKnowHow B.V. (4 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| granulation unit capacity | 3600 t/d | SAFCO IV granulation unit; more than 20 plants have capacities of 3,000 t/d or more |
| granule size | 2-8 mm | product sizes produced in one plant |
| recycle ratio | 0.5 ratio | recycle to product in a TEC fluid-bed granulator |
| bed temperature | 110-119 °C | fluid-bed granulator bed temperature in the cited study |
| product total nitrogen | 46.3 wt% | Toyo typical standard product quality, design-condition dependent |
| product biuret | 0.8 wt% | Toyo typical product quality |
| product moisture | 0.2 wt% | Toyo typical product quality |
| product formaldehyde | 0.45 wt% | Toyo typical product quality |
| product size 2-4 mm | 95 wt% | Toyo typical product quality |
| granule hardness | 3.5 kg/granule for 3 mm | Toyo typical product quality |
| steam consumption | 0.01 MT/MT product | Toyo consumption per unit of service, typical standard depending on atmospheric conditions, utility conditions and feed urea solution concentration |
| power consumption (fluidising product cooler) | 24 kWh/MT product | Toyo typical standard in case of fluidizing product cooler |
| power consumption (bulk flow cooler with cooling water) | 19 kW/MT (as printed) | Toyo note: 'In case of bulk flow cooler by cooling water, power consumption becomes 19kW/MT' |
| cooling water | Nil n/a | Toyo consumption per unit of service for the standard granulation configuration |
| urea dust emission | ?-30 mg/Nm3-Air | Toyo low-pressure-drop dust scrubber: air containing urea dust washed with circulating water to reduce urea dust to less than 30 mg/Nm3-Air |
| Casale GREEN GRANULATION acquisition | 2022 year | Casale: technology developed by GREEN GRANULATION Ltd, fully acquired by Casale in 2022 |
| service scope | training, desk studies, online Q&A, site visits, troubleshooting, revamp proposals, dynamic simulator n/a | UreaKnowHow service list |
| formaldehyde use | minimum or no use n/a | Casale benefits list |
| application | critical items in urea plants / high-pressure strippers n/a | Casale news items 'Yara selects Uremium 29' and HP stripper made with Uremium 29 |
| total nitrogen | 46.3 wt% | typical product quality |
| biuret | 0.8 wt% | typical product quality |
| size 2-4 mm | 95 wt% | typical product quality |
| steam | 0.01 MT/MT | typical consumption |
| power | 24 kWh/MT | typical, fluidizing product cooler |
| urea dust | 30 mg/Nm3-Air (less than) | scrubber design target |

- **thyssenkrupp Uhde** UFT Fluid Bed Granulation: 2-8 mm product sizes from one plant; more than 20 plants at 3,000 mt/d or more
- **Toyo Engineering** Spout-Fluid Bed Granulation: scaled from 50 to 3,250 MTPD; designed to 4,500 MTPD
- **Stamicarbon** Fluid-bed granulation technology: 98.5 wt.% melt; up to 0.3 wt.% formaldehyde; on-stream time more than 150 days
- **Casale** GREEN GRANULATION: feed concentration can be as low as 96-97%

Recorded gaps:

- UFT (Uhde fluidised bed) granulation specifics - capacity range, fluidisation velocity, product size, official page — Locate and fetch a current thyssenkrupp uhde fertilizer/urea UFT page via a working URL.
- Granulator capacity range, bed area, spray nozzle count, seed recycle ratio — Read the Casale GREEN GRANULATION brochure PDF with a PDF-capable tool.
- UFT (Uhde fluidised bed) granulation specifics - capacity range, fluidisation velocity, product size, official page — Locate and fetch a current thyssenkrupp uhde fertilizer/urea UFT page via a working URL.
- Granulator capacity range, bed area, spray nozzle count, seed recycle ratio — Read the Casale GREEN GRANULATION brochure PDF with a PDF-capable tool.

## heat-exchanger

### Boiler air preheater (air-preheater-boiler)

Primary code: PWR: Power and renewables
Heat exchanger that transfers heat from outgoing flue gas to incoming combustion air. Regenerative (rotary) designs use a rotating matrix or baskets; recuperative designs use tubular or plate elements. B&W supplies air heaters and notes the cold-end metal temperature is generally approximated from the average gas and air temperatures.
Vendors: Babcock & Wilcox (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| cold-end metal temperature basis | average of gas and air inlet temperatures qualitative | B&W: general assumption is that cold-end metal temperature is approximately the average of the gas and air inlet temperatures (qualitative, no numeric value on the read page) |
| product scope | tubular and regenerative air heaters qualitative | B&W air-heater product page read during the sweep; no performance table was given |
| Function | Advanced combustion solutions for indirect-fired process gas heating applications qualitative | John Zink Products page product card for Air Heaters & Recuperators |
| Characteristics | Clean air contact with products and high efficiency in heat transfer qualitative | John Zink Products page product card |


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
| Applicable boiler size | 2500 HP (up to) | Product bullet: 'Boilers up to 2,500 HP'; accommodates all boiler design pressures |
| Construction | Two-stage: separate non-condensing stack section and condensing section configuration | Product bullets and narrative |
| Tube material | 316 stainless steel tube with aluminum fins (Al-Fuse) material | Product Overview: tube core assemblies individually removable; all gas side surfaces 316 stainless steel to eliminate corrosion |
| Condensing fuel basis | Condenses on natural gas only; near-condensing mode on #2 oil fuel basis | Product Overview bullet and narrative |
| Efficiency boost | 3-5 % | Economizers catalog listing: 'Boost efficiency 3-5% with the ClearFire Economizer (ECF)' |
| Applicable boilers | ClearFire-H and CBT boilers from 10-80 HP, high or low pressure steam applicability | Economizers catalog listing |


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
| Superheater outlet temperature | 1050 deg F (up to) | Max-Fire Technical Data table: Steam Temperature up to 1,050 deg F; narrative: furnace and evaporator and superheater, if applicable |
| Superheater design | Dedicated superheaters for corrosive fuels; easily replaceable superheaters in back pass design feature | Valmet CFB Boiler page bullets and 'High steam parameters' section |
| High steam parameters | Possible without severe corrosion even with recovered fuels qualitative | Valmet CFB Boiler page: fluidized bed heat exchangers in loop seal |


Recorded gaps:

- superheater surface, metal temperature limits and attemperator spray rates — Read OEM superheater design descriptions and cycling guidance.

## heat-recovery

### Continuous/TDS blowdown control, flash vessels, blowdown heat-recovery exchangers (blowdown-heat-recovery)

Primary code: PWR: Power and renewables
Continuously remove concentrated boiler water to hold TDS below foaming/carryover limits; reduce energy and water loss by flashing to low pressure, recovering flash steam to the feedtank/deaerator, and cooling residual blowdown through a heat exchanger that preheats make-up before discharge.
Vendors: Spirax Sarco, TLV, Veolia Water Technologies & Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Conventional shell-boiler boiler-water TDS operating range | 2000-3500 ppm | Spirax Sarco: 2000 ppm very small boilers to 3500 ppm larger boilers, provided near design pressure and moderate load |
| Automatic TDS control example dead-band | open at 3000 ppm; close at 2700 ppm (10% band) ppm | Spirax Sarco on/off blowdown valve control illustration |
| Continuous blowdown orifice example | 1111 kg/h through ~3.6 mm orifice; 10 mm seat with needle set to 9.33 mm kg/h / mm | Spirax Sarco worked example; downstream pressure assumed 0.5 bar g |
| Volume increase across blowdown orifice | >1000 times liquid volume | Spirax Sarco: water at saturation drops almost full boiler pressure across the orifice |
| Flash fraction from 10 bar g to 0.5 bar g | 14.1 % of blowdown water flashed | Spirax Sarco heat-recovery worked example; boiler saturation 184 °C; hfg at 0.5 bar g = 2226 kJ/kg |
| Flash steam energy share of blowdown | about 49 % of blowdown energy flow | Spirax Sarco example (97 kW recoverable in flash steam vs 241 kW total blown down, 0 °C datum) |
| Flash-vessel steam velocity limit | 3 m/s maximum in top section | Spirax Sarco equipment requirement; vessels built to recognised pressure-vessel standard e.g. PD 5500 |
| Blowdown heat recovery via flash vessel | about 40 % of energy in boiler blowdown | Spirax Sarco (flash vessel and associated equipment, before residual heat recovery) |
| Residual blowdown temperature after heat exchanger | about 20 °C | Spirax Sarco: residual blowdown from 0.5 bar g flash vessel at about 105 °C cooled to ~20 °C heating make-up water |
| Total recovery with flash steam + residual heat exchanger | 82% of original blowdown energy; 14% by mass of water recovered % | Spirax Sarco summary of complete heat-recovery arrangement |
| Bottom blowdown example (10 bar g, 40 mm line, 10 m equivalent length) | 6.2 kg/s; hf 782 kJ/kg → 4.85 MW; 16% flashes to atmosphere kg/s / kJ/kg / MW / % | Spirax Sarco Bottom Blowdown worked example; minimum reasonable blowdown line length 7.5 m |
| Blowdown vessel design pressure | >=25% of boiler maximum working pressure % | Spirax Sarco extracting HSE Guidance Note PM60; design temperature >= saturation temperature at vessel design pressure |
| Bottom blowdown restriction | should never be permitted unless recommended by boiler manufacturer; above 700 psig may cause water starvation psig | DOE Steam Sourcebook, Boiler Blowdown System section |
| BDV60 blowdown vessel design standard | ASME VIII Div 1 2015; Pressure Equipment Safety Regulations 2016; CEA BG03 standard | Spirax Sarco Malaysia product page |
| Function | Recover flash steam and heat from boiler blowdown n/a | Category description printed on page; no product model or numeric spec printed |
| Maximum operating pressure (PMO) | 7 psig | Printed in Product Details table for SR-3 and SR-8; PMO defined on page as Maximum Operating Pressure |
| Maximum operating temperature (TMO) | 285 deg F | Printed in Product Details table for SR-3 and SR-8; TMO defined on page as Maximum Operating Temperature |
| Maximum steam flow rate SR-3 | 660 lb/h | Printed in Product Details table; row also printed an unlabelled '212' in an adjacent cell whose metric is not resolvable from the markdown table, so it is not recorded as a spec |
| Maximum steam flow rate SR-8 | 1,760 lb/h | Printed in Product Details table |
| Body / heat transfer coil material | Stainless (SUS304) n/a | Printed in Product Details table |


Recorded gaps:

- Blowdown heat-recovery vendor datasheet with duty and approach-temperature basis — Fetch a Spirax/TLV blowdown heat-recovery package datasheet and record design duty, terminal temperatures and materials
- HRSG-specific continuous blowdown rates and flash recovery at high pressure — Fetch GE Vernova/Siemens HRSG water-chemistry or O&M guidance
- Dollar-year cost of blowdown heat loss — Only add after fetching a dated DOE tip sheet or BoE with explicit price year

## hv-circuit-breakers

### High-voltage circuit breakers (132-500 kV) (ele-hv-circuit-breakers)

Primary code: ELE: Electrical engineering
SF6 dead-tank and live-tank circuit breakers at 132, 275 and 500 kV for grid and substation duty, with interrupting ratings set by the Malaysian fault levels, to IEC 62271-100.
Vendors: Hitachi Energy, Siemens Energy (incl. ex-Dresser-Rand), GE Vernova (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| interrupting requirement at 500 kV | 50 kA | TNB 500 kV fault rating 50 kA for 1 s, so breakers are specified at or above it |
| interrupting requirement at 275 kV | 40-50 kA | TNB 275 kV 40 kA for 3 s, 50 kA near power stations |
| interrupting requirement at 132 kV | 31.5-40 kA | TNB 132 kV 31.5 kA for 3 s, 40 kA near power stations |
| indicative cost, 145 kV dead-tank breaker | 40000-95000 USD per set | Western/Japanese brand new dead-tank at 145 kV roughly USD 40,000-95,000 (a Siemens SPS-145 used unit listed near USD 95,000; a Spanish tender for 145 kV 3150 A 31.5 kA at about EUR 26,000); Chinese OEMs quote far lower, USD 2,500-45,000. Export price list basis (accepted on owner instruction 2026-11-13). |
| indicative cost, 245 kV dead-tank breaker | 85000-150000 USD per unit | A municipal utility PO for a Siemens SP2-245 at USD 85,650/unit; Chinese OEM 252 kV units USD 60,000-93,000. Export price list basis (accepted on owner instruction 2026-11-13). |
| indicative cost, 550 kV dead-tank breaker | 200000-520000 USD per three-phase set | Chinese OEM 550 kV about USD 210,000-270,000; an import record of a 3150 A 50 kA three-phase set near USD 520,000; EGAT tender about THB 6.0 million per unit (about USD 170,000). Indicative and highly configuration-dependent. |

- **Hitachi Energy** Live tank / dead tank: 72.5-800 kV
- **Siemens Energy (incl. ex-Dresser-Rand)** 3AP / 3AT / SPS: 72.5-550 kV
- **GE Vernova** Dead tank breakers: 72.5-800 kV

Recorded gaps:

- SF6 leakage rate and mechanical operating times from a manufacturer datasheet — Ask the owner for a manufacturer breaker datasheet, or read a GE/Hitachi technical guide

## ignition

### Pilot and ignition systems (pilots, igniters, flame scanners, BMS sequencing) (boiler-pilot-ignition-system)

Primary code: PWR: Power and renewables
Provide a reliable ignition source for pilot and main burners and prove flame presence before fuel is admitted; burner management system (BMS) sequences purge, pilot trial-for-ignition, flame proof, main flame light-off and shutdown, while a separate combustion control system meters fuel/air. Flame scanners with background-flame discrimination allow light-off and verification from the control room.
Vendors: John Zink (Koch Engineered Solutions), Zeeco, Forney Corporation, Siemens, Profire Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| InstaFire pilot flame-loss detection time | 6-20 seconds | John Zink vendor page; stated faster than thermocouples which can take more than 9 minutes; control panel up to 1,000 ft from pilot; no compressed air required |
| FFG remote ignition distance and service life | 1000 ft (distance from pilot; 'over 1,000 feet'); >40 years proven performance | John Zink vendor page; schedule 80 carbon or stainless steel piping; natural gas, propane, hydrogen; manual piezoelectric or automatic line-powered transformer |
| Zeeco ProFlame scanner hazardous-area models | ZPF-110 (Zone 1, II 2G EExd IIC T6), ZPF-120 (Zone 2), ZPF-130 (nonhazardous) model designations | Zeeco Flame Scanners product page; ProFlame+ utility grade ZPF-1100UV/IR/DS, ZPF-1200UV/IR/DS, fiber optic ZPF-1200UF/IF |
| Vortex-cooled scanner temperature drop | 28 degrees C (50 F) below incoming compressed air | Zeeco product page: vortex tube uses compressed air, no moving parts; cools scanner internals |
| Zeeco Free Jet Power Burner emissions and turndown | 9-50 ppm NOx (9 ppm), sub-50 ppm CO, 20:1 fuel turndown; 30 ppm NOx potential without flue-gas recirculation | Chemical Engineering magazine interview with Zeeco CTO; small external flue-gas recirculation |
| John Zink Solex burner NOx | 5 ppm NOx across fuel compositions and furnace temperatures | Chemical Engineering magazine; two combustion zones, compact flame length, designed to avoid SCR |
| Profire 3100 BMS modular capacity | 32 modules combinable from one user interface | Chemical Engineering magazine; modules certified with regulatory bodies; can manage multiple burners or multiple pilots; forced-air I/O |
| Igniter class | Class 3 n/a | Printed on Forney igniters list page |
| Duty | direct spark ignition of oil or gas igniters, small burners, and combustion turbines n/a | Printed on Forney igniters list page |
| Approval | Standard HESI is FM approved; CE Version meets Low Voltage Directive n/a | Printed on Forney igniters list page |
| Fuel | air atomized No. 2 oil n/a | Printed on Forney igniters list page |
| Design feature | protected primary combustion zone n/a | Printed on Forney igniters list page; claimed self-stabilized and highly reliable |
| Nominal capacity range, whole series | 0.3-50 MBtu/hr | Printed: 'Capacities (nominal) range from 1 mmBtu/hr to 50 mmBtu/hr' in overview and '0.3 to 50 MBtu/hr' in Features & Benefits; both printings retained |
| Model 110 capacity | 0.3-1.5 MBtu/hr | Printed in Specifications table |
| Model 130 capacity | 1.5-6.0 MBtu/hr | Printed in Specifications table |
| Model 135 capacity | 5.0-15 MBtu/hr | Printed in Specifications table |
| Model 140 capacity | 5.0-25 MBtu/hr | Printed in Specifications table |
| Model 150 capacity | 10-50 MBtu/hr | Printed in Specifications table |
| Fuel | Natural gas or propane n/a | Printed in Specifications table |


Recorded gaps:

- Laser/tunable-diode-laser ignition is not evidenced; only laser-based combustion *diagnostics* (John Zink ZoloSCAN WM-TDLAS, Yokogawa TDLS O2 analyzer) were found — Search specifically for 'laser ignition boiler burner' or 'laser-induced ignition pilot' vendor literature before recording laser igniters as a type.
- No fetchable NFPA 85 document (paywalled); trial-for-ignition numbers quoted second-hand via AFRC (NFPA 86) and magazine articles — Use NFPA 85 handbook summaries or insurer/BOCA guidance pages that print the trial-for-ignition and purge requirements.
- Asia-Pacific flame scanner/pilot vendors not yet evidenced beyond Zeeco/John Zink regional offices — Search KOSHA/KTL-certified ignition suppliers and Chinese/Japanese flame scanner OEMs.

## ins-platform

### Decommissioning / removal technologies (ins-decommissioning-removal-technologies-reverse-installation-sing)

Primary code: UPS: Upstream
Prepare structure (clean, cut, install lifting points), remove topsides and jacket by reverse installation (piece-small or module), single-lift heavy lift, or controlled toppling where permitted; transport to shore for recycling/disposal.
Vendors: Heerema Marine Contractors, Allseas (OEM design), Boskalis (Dockwise heritage), Thunder Cranes, Mammoet (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Heerema removal vessel capacity | up to approximately 20,000 metric tons metric tons | Heerema jacket and topside removal page |
| Largest single-lift jacket removal | 10,100 metric tons — Brent Alpha jacket, 2020 metric tons | Heerema decommissioning page (world record claim) |
| Recycling/repurposing rate | 98% of structures safely repurposed or recycled % | Heerema decommissioning page |
| Rigs-to-Reefs decommissioning example | Red Hawk cell spar decommissioned in 2014 under BSEE Rigs-to-Reefs program; deepest floating platform decommissioned at the time date / description | Wikipedia Spar (platform), lead section |


### Float-over topside installation (ins-float-over-topside-installation-barge-float-over-tidal-float-o)

Primary code: UPS: Upstream
Transport an integrated topside on a heavy-lift/transport barge, maneuver the barge between pre-installed jacket legs, align deck legs with leg-mating units, ballast the barge (or use tidal change) to transfer weight to the substructure, then weld out.
Vendors: Trelleborg Marine and Infrastructure, Mammoet, Orca Offshore, Hi-Tech Elastomers, SeaCamel (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Float-over hardware set | LMU + Sway and Surge Fenders (SSF) + Deck Support Units (DSU) list | Trelleborg LMU page, Overview |
| Topsides weight where crane-free float-over is advantageous | >10,000 t (many topsides now exceed this) t | Mammoet topside load-out page |
| Innovation | direct welding after set-down; no sand-jack lowering phase mechanism | Value as printed in the cited source; no further qualifier stated. |


### Floating platform installation — semi-submersible ballasting/mooring (ins-floating-platform-installation-semi-submersible-ballasting-moo)

Primary code: UPS: Upstream
Float a semi-submersible hull to site, ballast to operational draft, connect chain/wire/polyester mooring or hold with DP; can be used from 60 m to 6,000 m water depth.
Vendors: Boskalis (Dockwise heritage), Allseas (OEM design) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Semi-submersible platform water depth range | 60 to 6,000 m (200 to 20,000 ft) m | Wikipedia Oil platform, Semi-submersible platform |
| Semi-submersible heavy transport ballast method | flood ballast tanks to lower well deck below water; float cargo over; pump out to raise deck description | Wikipedia Heavy-lift ship, Semi-submersible ships |
| Pioneering Spirit semi-sub operation | 48,000 t topside lift achieved by operating as a semi-submersible t | Wikipedia Pioneering Spirit, Design |


### FPSO/FSO hook-up, offloading and commissioning (ins-fpso-fso-hook-up-offloading-and-commissioning)

Primary code: UPS: Upstream
Bring a tanker-based FPSO/FSO to site, moor it, connect risers/flowlines/umbilicals and offloading system, hook up pre-laid moorings (often with AHTS + ROV), then commission and hand over.
Vendors: Acteon, Fugro, Oceaneering, Vantris Energy (Sapura Energy) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| FPSO/FSO definition | FPSO = large monohull, usually ship-shaped, with processing facilities, moored for extended periods and not drilling; FSO/FSU used exclusively for storage with little process equipment description | Wikipedia Oil platform, Floating production systems |


### Gravity-based structure (ins-gravity-based-structure-gbs-installation)

Primary code: UPS: Upstream
Concrete or steel gravity structure built in sheltered deep water near shore, floated to site, sunk by controlled ballasting onto prepared seabed, then topsides installed by float-over or crane.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| GBS float-out and sinking | built close to shore in Norwegian fjords/Scottish firths, floated to final position and sunk to seabed description | Wikipedia Oil platform, Fixed platforms |
| Fixed platform economic depth limit | up to about 520 m (1,710 ft) m | Wikipedia Oil platform, Fixed platforms |
| Troll A gravity platform | founded in 330 m depth with 30 m long skirts; world's biggest gravity platform m | Wikipedia Suction caisson, Gravity oil platforms |
| Ekofisk first North Sea gravity platform | foundation area as big as a football field; designed for waves up to 24 m description / m | Wikipedia Suction caisson, Gravity oil platforms |


### Hook-up, commissioning and close-out (ins-hook-up-commissioning-and-close-out)

Primary code: UPS: Upstream
After set-down: weld out LMU/leg connections, install conductors/risers/umbilicals, connect utilities, test systems, survey as-built position and hand over; for float-over, release LMU load and weld topside leg cans to substructure.
Vendors: Acteon, Fugro (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Post-float-over close-out step | topside leg cans securely welded to substructure after installation description | Trelleborg LMU page, Overview |
| Direct-weld LMU close-out | topside welded directly to jacket after set-down; sand-jack lowering phase eliminated description | Orca Offshore LMU page |


### Impact pile driving hammers (ins-impact-pile-driving-hammers-hydraulic-diesel-underwater)

Primary code: UPS: Upstream
Drive tubular piles/conductors/monopiles to target penetration using controlled high-energy blows; hydraulic double-acting hammers give higher frequency and control; underwater hammers use power packs and compensators.
Vendors: IQIP, Menck (Acteon Marine Foundations; sale to Cadeler announced Aug 2026), Vulcan Iron Works (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| IQIP Hydrohammer S-series energy range | 30 kJ (S-30) to 2,000 kJ (S-2000) kJ | IQIP Hydrohammer S-series page: 'Models range from S-30 to S-2000, with energy capacities from 30kJ to 2000kJ' |
| IQIP S-2000 max blow energy / blow rate / hammer weight | 2,000 kJ; 35 bl/min; 230 t hammer (100 t ram) kJ / bl/min / t | IQIP S-series datasheet table on product page |
| IQIP S-150 max blow energy / blow rate / hammer weight | 150 kJ; 44 bl/min; 16.5 t hammer (7.5 t ram) kJ / bl/min / t | IQIP S-series datasheet table |
| IQIP minimum energy setting | about 10% of max (standard); 2-5% in high-frequency/low-energy mode % of max energy | IQIP S-series datasheet footnote |
| Menck double-acting hammer energy range (whole spread) | 100 kJ to 6,250 kJ kJ | Acteon/Menck hydraulic hammers page: 'hammer spread unites double-acting hydraulic hammers (100 kJ to 6,250 kJ)' |
| Menck MHU6000W max energy / blow rate / oil flow / pressure | 6,250 kJ; 30 bl/min; 12,800 L/min; 210 bar kJ / bl/min / L/min / bar | Acteon/Menck hydraulic hammers page, MHU6000W specification block |
| Menck MHU300S / MHU800S / MHU3500S energy ranges | 27-300 kJ / 75-820 kJ / 320-3,500 kJ kJ | Acteon/Menck hydraulic hammers page, individual model blocks |
| Saipem 7000 hammer spread | 2 x Menck MHU 3000 (3,000 kJ each); 2 x MHU1700; 2 x MHU1000; 2 x MHU600; 1 x MHU220; 1 x MHU195; 2 underwater power packs; 1 hydraulic hammer compensator list | Wikipedia Saipem 7000, Platform installation equipment |
| Diesel hammer principle | two-stroke diesel engine; piston is ram, cylinder connects to pile head; fuel ignites on compression, rebounding ram description | Wikipedia Pile driver, Diesel hammer |
| Underwater noise mitigation | bubble curtains, balloons, internal combustion water hammers list | Wikipedia Pile driver, Environmental effects |
| Tandem lift | 14000 t | Value as printed in the cited source; no further qualifier stated. |
| Per-crane main hook at 40 m | 7000 t | Value as printed in the cited source; no further qualifier stated. |
| Ballast transfer rate | 24000 t/h | Value as printed in the cited source; no further qualifier stated. |
| J-lay tension (friction clamps) | 2000 t | Value as printed in the cited source; no further qualifier stated. |
| Energy range | 30-2,000 kJ | Value as printed in the cited source; no further qualifier stated. |
| S-2000 max blow energy | 2000 kJ | Value as printed in the cited source; no further qualifier stated. |
| S-2000 blow rate | 35 bl/min | Value as printed in the cited source; no further qualifier stated. |
| S-2000 hammer weight | 230 t | Value as printed in the cited source; no further qualifier stated. |
| Operating angle | 0-90 degrees | Value as printed in the cited source; no further qualifier stated. |
| Energy range | 200-6,250 kJ | Value as printed in the cited source; no further qualifier stated. |
| Blow rate | 30 bl/min | Value as printed in the cited source; no further qualifier stated. |
| Oil flow | 12800 L/min | Value as printed in the cited source; no further qualifier stated. |


### Jack-up installation (ins-jack-up-installation-self-elevating-units)

Primary code: UPS: Upstream
Tow to site with legs up, jack legs down to seabed, preload with ballast to ensure legs do not penetrate further in service, then jack hull above water to a predetermined air gap so waves act on slender legs rather than hull.
Vendors: Seaway7 (Subsea7), Noble Drilling (Noble Lloyd Noble) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Typical water depth limit | generally less than 120 m; premium/ultra-premium 150-190 m (490-620 ft) m | Wikipedia Jackup rig, Process of operation |
| Tallest jack-up legs | Noble Lloyd Noble, legs 214 m, completed 2016 m | Wikipedia Jackup rig, lead section |
| Global fleet size | about 540 jackup drilling rigs at end of 2013 count | Wikipedia Jackup rig, lead section |
| Jacking mechanism | rack and pinion; pinions driven by hydraulic or electric motors, rack affixed to legs description | Wikipedia Jackup rig, Process of operation |
| Yme MOPU removal by Pioneering Spirit | 13,500 t jack-up type platform on three 3.5 m diameter steel legs t / m | Wikipedia Pioneering Spirit, Projects |


### Launch barge and jacket launching (ins-launch-barge-and-jacket-launching-skid-rails-rocker-arms-launc)

Primary code: UPS: Upstream
Fabricate jacket horizontally, load out onto a launch barge, tow to site, ballast the barge to trim, winch/slide the jacket over skid rails and rocker arms into the water, let it float near-horizontal (head-up), then upend and set on seabed.
Vendors: DNV (Installjac software), Mermaid Consultants, TheNavalArch, Heerema Marine Contractors (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Principal launch stages | 1 winching to overcome friction; 2 sliding; 3 point of rotation; 4 rotating and sliding; 5 jacket clear of barge list | TheNavalArch, 'Launching Steel Jackets' by Alan Crowle, Figure 1 |
| Typical launch barge draft | 60-65% of barge depth; up to 80% possible if strength adequate % of depth | TheNavalArch launch article, Barge choice |
| Maximum allowable barge trim | usually about 10 degrees degrees | TheNavalArch launch article, Launch constraints |
| Friction coefficients (greased timber on Teflon) | dynamic 0.035 (3.5%); static as low as 0.05 (5%) dimensionless | TheNavalArch launch article, Launch constraints |
| Jacket auxiliary buoyancy | typically over 10% of launch weight % of launch weight | TheNavalArch launch article, Jacket auxiliary buoyancy |
| Jacket reserve buoyancy (floating after launch) | at least 15% of total jacket weight % | Mermaid Consultants, Jacket Launching — Jacket Reserve Buoyancy |
| Minimum bottom clearance during launch | 10% of water depth or 5 m, whichever is greater m / % | Mermaid Consultants, Jacket Bottom Clearance |
| Stability criterion during launch | transverse and longitudinal GM > 1 m m | Mermaid Consultants, Barge and Jacket Stability |
| Hydrodynamic coefficients used in launch analysis | Cd 0.7; Cm 2.0 dimensionless | TheNavalArch launch article, Structural analysis (Morison's equation) |
| Launch sea state limit (personnel transfer / boarding) | significant wave height typically less than 2 m m Hs | TheNavalArch launch article, Offshore operations; Mermaid Consultants, Environmental Conditions |


### Leg Mating Units (ins-leg-mating-units-lmu-elastomeric-shock-absorbers)

Primary code: UPS: Upstream
Absorb vertical and horizontal compression as topside deck-leg cans land on jacket legs during float-over; manage static and dynamic loads and horizontal movement from sea state; allow load release after set-down.
Vendors: Trelleborg Marine and Infrastructure, Hi-Tech Elastomers, Orca Offshore / SeaCamel (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Full-scale compression load test up to | 18300 MT | Trelleborg LMU page, Benefits: 'Full-scale testing compression loads up to 18,300 MT' |
| LMU construction | robust steel structure with high-performance elastomeric pads description | Trelleborg LMU page, Overview |
| Load-relief mechanism | sand released from valve lowers plunger assembly, unloading rubber elements description | Hitech Elastomers LMU page, INTRO |
| Alternative LMU build | standard rubber elements + standard steel pipe + flush steel plates description | Orca Offshore LMU page |


### Load-out and transport — SPMT, skidding, strand jacking, barge load-out, sea-fastening (ins-load-out-and-transport-spmt-skidding-strand-jacking-barge-load)

Primary code: UPS: Upstream
Move completed topsides/jackets from fabrication yard onto a transport barge or heavy-lift vessel using SPMTs, skid tracks or strand jacks; analyze quay strength and CoG; ballast vessel and install sea-fastening for the voyage.
Vendors: Mammoet, ALE, Lampson, Allseas (OEM design) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Strand-jack unit capacity / skid speed | up to 1,045 t per unit; load-outs up to 50 m per hour t per unit / m per hour | Mammoet topside load-out page |
| Hydraulic compensated skid shoe load-out capacity | in excess of 20,000 t using multiple skid shoes t | Mammoet topside load-out page |
| Typical topside weight driving load-out design | many now exceed 10,000 t t | Mammoet topside load-out page |
| Dongfang 18,000 t load-out equipment | 4 x 850 t strand jacks; 4 x 2,400 t ballast pumps; 12 x 1,000 t de-ballast pumps count x t | Mammoet case study, 18,000 t topside load-out |


### Mooring and anchoring systems (ins-mooring-and-anchoring-systems-incl-ahts-and-anchors)

Primary code: UPS: Upstream
Position and hold floating facilities and assist installation vessels using anchors, chain/wire/polyester lines, AHTS vessels and DP systems; includes pre-laid mooring line hook-up for FPSOs.
Vendors: Heerema Marine Contractors, Acteon / Intermoor, Smit (Boskalis) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sleipnir 12-point mooring | 12 Stevpris Mk-6 anchors of 12 t each with 1,750 m wire rope count / t / m | Wikipedia SSCV Sleipnir, Stationkeeping |
| Thialf mooring for shallow water | 12 Flipper Delta anchors at 22.5 t with 2,500 m of 80 mm mooring wire count / t / m / mm | Wikipedia SSCV Thialf, Layout |
| Saipem 7000 mooring system | 16 anchor lines, each 3,350 m of 96 mm wire + 50 m of 92 mm chain + 40 t anchor; usable to 450 m water depth count / m / mm / t | Wikipedia Saipem 7000, Mooring system |
| AHTS bollard pull | 200 t and 212 t (Heerema Bylgia and Kolga) t | Heerema fleet page |
| Spar mooring configuration | spread mooring of chain-wire-chain or chain-polyester-chain description | Wikipedia Spar (platform), lead section |


### Pile handling, levelling, grouting and connection hardware (ins-pile-handling-levelling-grouting-and-connection-hardware)

Primary code: UPS: Upstream
Handle/upend piles and jacket legs, level and align before grouting, seal annulus, grip jacket piles and provide lifting/release tools.
Vendors: Hi-Tech Elastomers, IQIP, Acteon / Menck (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Saipem 7000 levelling systems | two internal systems, 66-72 in diameter, 900 t each; two external levelling systems, 1,000 t each in / t | Wikipedia Saipem 7000, Platform installation equipment |
| Saipem 7000 pile slings | 16 x 35 cm diameter x 60 m long cable-laid slings count / cm / m | Wikipedia Saipem 7000, Platform installation equipment |
| Grout/seal product families | Passive Grout Seal, Inflatable Grout Packer, Diaphragm Closure, Jacket Pile Gripper list | Hi-Tech Elastomers offshore products navigation |
| IQIP handling/lifting tools | Upending Frame, Pile Upending Tool, Flanged Jacket Lifting Tool, Hydraulic Release Shackle, Skidding System, Pile Guiding & Positioning Frame list | IQIP product navigation |


### Provider register — installation contractors and vessel owners (ins-provider-register-installation-contractors-and-vessel-owners-c)

Primary code: UPS: Upstream
Consolidated evidence-backed list of contractors/vessel owners for installation scope, including those named in the task brief for which only partial or search-verified evidence was obtained.
Vendors: Heerema Marine Contractors, Allseas (OEM design), Saipem (ex-Micoperi 7000), Subsea7 / Seaway7, Boskalis (Dockwise heritage), Van Oord, Jan De Nul, Scaldis, ALE, Mammoet, Lampson, COOEC (CNOOC Engineering), Sapura / Vantris Energy (incl. L&T Sapura JV), Micoperi, TechnipFMC / Technip, DOF, DeepOcean, IQIP, Menck / Acteon (sale to Cadeler announced 2026), Trelleborg Marine and Infrastructure, Hi-Tech Elastomers, Orca Offshore / SeaCamel, Fugro, Oceaneering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Provider evidence tiers | tier A = primary OEM/contractor page read; tier B = Wikipedia page read; tier C = search-verified snippet only classification | Compiled by this research from sources listed per vendor |


### Semi-submersible crane vessel (ins-semi-submersible-crane-vessel-sscv-heavy-lift-crane-installati)

Primary code: UPS: Upstream
Lift integrated topsides, jackets and large modules in a single lift or tandem lift; ballast down to submerge pontoons and reduce wave/swell motion; use revolving cranes with main/auxiliary/whip hoists, heave-compensated where fitted.
Vendors: Heerema Marine Contractors, Allseas (OEM design), Saipem (ex-Micoperi 7000), Boskalis (Dockwise heritage), Seaway7 (Subsea7), Jan De Nul, Van Oord, COOEC (CNOOC Engineering), Sapura / Vantris Energy (incl. L&T Sapura JV), Micoperi, Scaldis (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sleipnir tandem lifting capacity | 20000 metric tons | Heerema fleet page: pair of revolving cranes can lift 20,000 metric tons |
| Sleipnir main hoist capacity vs radius | 10,000 t @ 27-48 m; 7,000 t @ 62 m; 4,000 t @ 82 m; max radius 102 m t / m radius | Wikipedia SSCV Sleipnir, Design>Cranes, citing Heerema Sleipnir page |
| Sleipnir lowering/hoisting reach | 20 m below waterline to 135 m above waterline at 32 m draft m | Wikipedia SSCV Sleipnir, Design>Cranes (main hoist) |
| Thialf tandem lift capacity | 14200 metric tons | Heerema fleet page and Wikipedia SSCV Thialf (combined maximum) |
| Saipem 7000 tandem lift / per-crane capacity | 14,000 t tandem; 7,000 t per crane at 40 m radius t | Wikipedia Saipem 7000, Description>Heavy lift |
| Aegir lifting capacity | 5000 metric tons | Heerema fleet page: monohull heavy lift vessel with 5,000 metric tons lifting capacity |
| Balder guyed-mode tandem lift | 6300 metric tons | Heerema fleet page |
| Boskalis Bokalift 1 / Bokalift 2 crane capacity | 3,000 t / 4,000 t t | Boskalis heavy lift vessels page |
| Saipem 7000 ballast transfer capacity | 24000 tonnes of water per hour | Wikipedia Saipem 7000, Ballast system (4 pumps) + free flooding via 2 m valves |
| Stable-lift assessment methods | Virtual CoG; Kaps; Nikitin; numerical simulation (standard & extensive) list | DNV expert story 'New guidance on achieving stable lifting operations' (28 Nov 2024), Guidance on Stability of Lifts by Heavy Lift Exchange Forum |
| Tandem lift | 20000 t | Value as printed in the cited source; no further qualifier stated. |
| Main hoist at 27-48 m radius | 10000 t | Value as printed in the cited source; no further qualifier stated. |
| Max main-hoist radius | 102 m | Value as printed in the cited source; no further qualifier stated. |
| Auxiliary hoist | 2500 t | Value as printed in the cited source; no further qualifier stated. |
| design weight range | 2000-40000 tonnes | facility design range, from simple wellhead platforms to large integrated facilities |
| substructure types served | jacket, GBS, semi-submersible, FPSO, drilling rig, TLP list | Stord yard topside projects |


### Single-lift topsides/jacket installation by catamaran ballast-lift vessel (ins-single-lift-topsides-jacket-installation-by-catamaran-ballast)

Primary code: UPS: Upstream
Straddle a platform with a bow slot, ballast down, extend motion-compensated lifting beams under the payload, de-ballast to transfer weight, then fast-lift clear; also carries jackets at stern tilting beams/sheerlegs.
Vendors: Allseas (OEM design), Huisman Equipment (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Topsides single-lift capacity (current page) | 60000 tonnes | Allseas Pioneering Spirit page: 'installation or removal of platform topsides up to 60,000 tonnes' |
| Jacket lift capacity (Allseas current page) | 20000 tonnes | Allseas Pioneering Spirit page: jackets up to 20,000 tonnes |
| S-lay tension capacity | 2000 tonnes | Allseas Pioneering Spirit page: unmatched S-lay tension capacity of 2000 tonnes |
| Number of azimuth thrusters | 12 count | Allseas Pioneering Spirit page |
| Bow slot dimensions | 122 m x 59 m (L x W); widened from 52 m to 59 m m | Wikipedia Pioneering Spirit, Design and Construction |
| Fast-lift stroke / time | 2.5 m in 15 s m / s | Wikipedia Pioneering Spirit, Design (citing IV-Consult) |
| Largest recorded single-lift removal | 31000 tonnes | Wikipedia Pioneering Spirit, Projects (Brent Charlie, July 2024) |
| Crane capacity | 4000 t | Value as printed in the cited source; no further qualifier stated. |
| Free deck space | 7500 m2 | Value as printed in the cited source; no further qualifier stated. |
| Monopile handling up to | 3000 mt | Value as printed in the cited source; no further qualifier stated. |
| Topsides single-lift capacity | 60000 t | Value as printed in the cited source; no further qualifier stated. |
| Jacket lift capacity | 20000 t | Value as printed in the cited source; no further qualifier stated. |
| S-lay tension | 2000 t | Value as printed in the cited source; no further qualifier stated. |
| Azimuth thrusters | 12 count | Value as printed in the cited source; no further qualifier stated. |
| Crane capacity | 3000 t | Value as printed in the cited source; no further qualifier stated. |
| Deck | 165 x 43 m | Value as printed in the cited source; no further qualifier stated. |
| Tandem lift | 14200 t | Value as printed in the cited source; no further qualifier stated. |
| DP class | III class | Value as printed in the cited source; no further qualifier stated. |


### SPAR platform installation — upending, ballasting and spread mooring (ins-spar-platform-installation-upending-ballasting-and-spread-moor)

Primary code: UPS: Upstream
Transport spar hull horizontally (wet tow or dry tow), upend by controlled ballasting/flooding, connect spread mooring (chain-wire-chain or chain-polyester-chain), then install topsides by crane or float-over.
Vendors: Technip (now TechnipFMC), J. Ray McDermott (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Spar configurations | classic (one-piece cylinder); truss (hard tank + truss + soft tank); cell (cluster of small cylinders) list | Wikipedia Spar (platform), lead section; Wikipedia Oil platform, Spar platforms |
| Deepest spar / deepest mooring | Perdido truss spar, 2,438 m mean water depth; deepest seabed mooring 2,383 m m | Wikipedia Spar (platform), lead and list; Wikipedia Oil platform, deepest platforms table |
| APAC spar example | Kikeh truss spar, 1,310 m, Malaysia, 2007, Murphy Oil, designed by Technip m / year | Wikipedia Spar (platform), list of spar platforms |
| Cell spar example | Red Hawk: 7 cells of 8 m diameter; decommissioned 2014 under Rigs-to-Reefs count / m | Wikipedia Spar (platform), lead section |
| First production spar | Neptune, classic spar, 588 m, Gulf of Mexico, installed September 1996 m / date | Wikipedia Spar (platform), list and lead |


### Suction bucket / suction pile (ins-suction-bucket-suction-pile-suction-caisson-installation)

Primary code: UPS: Upstream
Inverted open-bottom tube sealed at top; penetrate by self-weight then by pumping water out to create negative pressure (suction); removable by pumping water in to create overpressure. Used as anchors for floating platforms and as foundations for fixed structures and wind turbines.
Vendors: NGI (Norwegian Geotechnical Institute), IQIP (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Installation mechanism | push or pump water out of skirt to create negative pressure; removal by overpressure description | Wikipedia Suction caisson, Description |
| Installed population / depth (as of 2002 statistics) | 485 caissons at more than 50 localities, depths to about 2,000 m count / locations / m | Wikipedia Suction caisson, lead section (statistics from 2002) |
| Diana platform suction anchors | 30 m high, 6.5 m diameter, installed at about 1,500 m water depth on soft clay (1999) m / m / m | Wikipedia Suction caisson, History |
| Gorm field first suction caissons | 12 caissons for a loading buoy at 40 m depth, Shell, 1981 count / m | Wikipedia Suction caisson, History |
| Snorre A TLP suction caissons | 12 m long vs up to 90 m long piles that would otherwise be required m | Wikipedia Suction caisson, History (Saga Petroleum/NGI) |
| Gravity platform skirt lengths | Gullfaks C 22 m skirts; Troll A 30 m skirts at 330 m water depth m | Wikipedia Suction caisson, Gravity oil platforms |
| Aasta Hansteen suction anchors | 17 suction anchors for the Aasta Hansteen platform, Norwegian Sea count | Wikipedia Suction caisson, image caption |


### Survey, positioning and ROV support (ins-survey-positioning-and-rov-support-dp-gps-underwater-inspectio)

Primary code: UPS: Upstream
Provide hydrographic/geophysical survey, positioning and navigation of installation vessels, subsea inspection and intervention with ROVs, and penetration/position monitoring during installation.
Vendors: Fugro, Oceaneering, Vantris Energy (Sapura Energy), COOEC (CNOOC Engineering) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sleipnir DP accuracy | position held within 30 cm x 30 cm in simulated sea trials cm x cm | Wikipedia SSCV Sleipnir, Stationkeeping |
| Pioneering Spirit DP | DP3 via 12 azimuth thrusters DP class | Wikipedia Pioneering Spirit, Design |
| Saipem 7000 saturation diving system | containerized 14-man system movable to any of three moon pools persons | Wikipedia Saipem 7000, Platform installation equipment |
| DP class on Boskalis heavy-lift vessels | DP2 (Bokalift 1 and Bokalift 2) DP class | Boskalis heavy lift vessels page |


### Tension-leg platform (ins-tension-leg-platform-tlp-tendon-installation)

Primary code: UPS: Upstream
Vertically moor a floating platform with high-axial-stiffness tendons/tethers grouped at corners, eliminating most vertical motion so wellheads can be on deck; install hull/topsides, then connect pre-installed tendons to seabed anchors.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Suitable water depth | >300 m and <1,500 m m | Wikipedia Tension-leg platform, lead section |
| Hutton TLP (first, 1980s) | 16 tension legs; 100-1,000 m design depth; 46,500-55,000 t moored, up to 61,580 t floating freely count / m / t | Wikipedia Tension-leg platform, lead section |
| Deepest ETLPs | Big Foot 1,580 m; Magnolia 1,425 m; Marco Polo 1,300 m; Neptune 1,300 m; Kizomba A 1,177 m; Ursa 1,200 m m | Wikipedia Tension-leg platform, list of deepest (E)TLPs |
| Snorre A TLP caisson alternative | 12 m long suction caissons instead of up to 90 m driven piles m | Wikipedia Suction caisson, History |


### Tow-out and wet tow of jackets / gravity-based structures (ins-tow-out-and-wet-tow-of-jackets-gravity-based-structures)

Primary code: UPS: Upstream
Transport launched or floated substructures from fabrication yard to site with tug boats; use controlled ballasting for self-installing GBS; DP-assisted positioning for final placement.
Vendors: Heerema Marine Contractors, Boskalis (Dockwise heritage), COSCO Shipping (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Steel GBS installation method | pulled off yard by wet-tow and/or dry-tow; self-installs by controlled ballasting of compartments with seawater description | Wikipedia Oil platform, Gravity-based structure |
| Steel GBS use case | predominantly where no or limited crane barges available (e.g. Caspian Sea) description | Wikipedia Oil platform, Gravity-based structure |
| Heerema AHTS bollard pull | 200 t (Bylgia) and 212 t (Kolga) metric tons bollard pull | Heerema fleet page: both tugs 72 m long, 18 m wide |
| Semi-sub heavy transport speed advantage | roughly 3 to 4 times the speed of a self-deploying rig ratio | Wikipedia Heavy-lift ship, Semi-submersible ships |
| Example heavy transport: Thunder Horse PDQ | world's largest semi-submersible oil platform (at the time), transported 2004 event | Wikipedia Heavy-lift ship, Incidents/Examples (Blue Marlin, DSME South Korea to Kiewit, Ingleside Texas) |


### Vibratory and press-in pile installation (ins-vibratory-and-press-in-pile-installation)

Primary code: UPS: Upstream
Install piles rapidly with vertical vibration from counter-rotating eccentric weights (can also extract), or press piles hydraulically where vibration/noise must be minimised.
Vendors: IQIP, Junttan (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Vibratory hammer frequency range | 1,200 to 2,400 vibrations per minute (VPM) VPM | Wikipedia Pile driver, Vibratory pile driver/extractor |
| Vibratory hammer mechanism | counter-rotating eccentric weights powered by hydraulic motors; horizontal vibrations cancel, vertical transmitted to pile description | Wikipedia Pile driver, Vibratory pile driver/extractor |
| Reaction-based hydraulic press-in noise | 69 dB at 23 ft dB at ft | Wikipedia Pile driver, Hydraulic press-in |
| Combined vibro + impact recommendation | vibro enables rapid initial penetration in suitable soils; impact hammer drives to final depth/bearing description | IQIP S-series FAQ: 'Why combine the S-series hydrohammer with an F-series or Z-series vibro hammer?' |


## instrumentation

### Boiler water sampling and analysis (boiler-water-sampling-analysis)

Primary code: PWR: Power and renewables
Obtain a representative, cooled sample for TDS/conductivity, pH, phosphate, silica, sulphite and iron testing without flash loss or scalding; increasingly use continuous online analysers linked to automatic blowdown and dosing control.
Vendors: Spirax Sarco, Veolia Water Technologies & Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Cooled sample temperature for conductivity measurement | <25 °C | Spirax Sarco: add phenolphthalein then 5% acetic acid drop-by-drop until colourless before measuring |
| Hydrometer sensitivity | 0.0001 relative density at 15.5 °C ≈ 110 ppm TDS ppm per 0.0001 relative density | Spirax Sarco relative-density method |
| AC excitation frequency for boiler-water conductivity probe | ~1000 Hz | Spirax Sarco: high frequency needed to avoid electrolytic polarisation at high boiler-water conductivity |
| Representative sample point | TDS blowdown connection qualitative | Spirax Sarco: do not sample from gauge glasses, external control chambers or near feedwater inlet |
| Condensate analysis frequency | daily (minimum) per day | CEA BG04 §5: basic condensate analysis daily to prove steam quality and system health |
| Inline vs offline analytical alignment | online photometric methods aligned with routine offline methods; inline probes add operational data qualitative | Veolia TrueSense Analyze boiler water analyzer product page |
| Conductivity vs TDS measurement practice | only one of the two needs to be measured; same method/readout must be used consistently qualitative | CEA BG04 Table 2 notes 12–13 |
| Body and coil material | austenitic stainless steel 316L n/a | Printed in Technical Information section TI-P403-09 |
| Cooling-water connection size | 1/2 in BSP or 1/2 in NPT | Printed in Construction and connections |
| Sample connection | 6 mm outside-diameter tube | Printed in Construction and connections; clamp version uses 1/2 in adaptor |
| Cooler weight | 3.1 kg | Approximate weight printed in Dimensions and weights table |
| SCS20 assembly weight | 4.2 kg | Approximate weight printed in Dimensions and weights table |
| Envelope dimension A | 410 mm | Approximate dimension printed in Dimensions and weights table |
| Envelope dimension H | 450 mm | Approximate dimension printed in Dimensions and weights table |
| Performance example: boiler pressure | 10 barg | Worked selection example, explicitly NOT an unconditional rating |
| Performance example: sample flow | 30 l/h | Worked selection example, explicitly NOT an unconditional rating |
| Performance example: cooling-water flow | 0.3 l/s | Worked selection example, explicitly NOT an unconditional rating |
| Performance example: temperature approach | 4 deg C | Worked selection example, explicitly NOT an unconditional rating |
| Performance example: sample outlet with 15 deg C cooling water | approximately 19 deg C | Worked selection example, explicitly NOT an unconditional rating |


Recorded gaps:

- Online silica analyser specification for HRSG/utility boilers — Fetch a Veolia Sievers/online silica analyser datasheet or equivalent OEM page
- Full analytical method standard BS 1427:2009 contents — Record as a standard reference and fetch only if a public summary is available

## insulation

### Thermal insulation / lagging and cladding for boilers and steam lines (heat-loss figures) (boiler-insulation-heat-loss)

Primary code: PWR: Power and renewables
Reduce heat loss from boiler surfaces, steam and condensate piping, protect personnel and maintain steam pressure/temperature; insulation also reduces condensate formation and trap load (DOE steam tip sheets, search-verified; Engineering ToolBox; TLV).
Vendors: SVI BREMCO (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| bare steam pipe heat loss | 54 to 1,852 W/m | Engineering ToolBox table for uninsulated horizontal steam pipes, still air, ambient 10-25°C; pipes 56-194 mm, temperature difference 15-150°C; min value 54 W/m at 56 mm/ΔT15, max 1,852 W/m at 194 mm/ΔT150 |
| insulation thermal conductivity basis | 0.036 W/(m·K) | fibreglass insulation assumption for Engineering ToolBox insulated-pipe heat-loss diagrams |
| worked insulated-pipe heat loss | ~20 W/m | 2 1/2 inch steel pipe, 80 mm fibreglass, fluid 90°C, ambient 10°C (ΔT 80°C), read from 80 mm diagram |
| TD trap cap insulating cover effect | steam loss can be halved qualitative | Spirax Sarco energy-loss tutorial: insulating cap on thermodynamic trap under no-load conditions |
| bimetallic trap lagging restriction | requires 1-3 m unlagged cooling leg m | Spirax Sarco thermostatic trap page |
| Fire door surface temperature (uninsulated) | around 350 deg F | Printed under 'Boiler Temperatures': 'Surface temperatures may reach around 350°F in fire doors' |
| Mud drum cover surface temperature (uninsulated) | around 200 deg F | Printed under 'Boiler Temperatures' |
| Typical insulation material | 1 in fiberglass in | Printed under Cost-Effective: 'We typically utilize 1” fiberglass for boiler insulation' |
| Warranty | 5 year years | Printed: 'come with a 5 year warranty' and '5 year guarantee' |
| Closure system | velcro and D-rings n/a | Printed under Convenient |
| Equipment covered | Boiler Access Doors; Steam Drum Covers; Mud Drum Covers n/a | Printed under 'Types of boiler doors and covers we regularly encounter' |


Recorded gaps:

- Cladding material/thickness and weatherproofing specifications for outdoor steam lines in Southeast Asia — Find boiler OEM or insulation contractor specification with cladding gauge, material and fastening details.
- Numeric heat-loss chart values for insulated HRSG/boiler casings (as opposed to pipes) — Fetch a boiler/HRSG OEM thermal performance datasheet or ASTM C680 based calculation example.

## jetty-civil

### Berth and jetty structures — piled jetties, quay walls, caissons, sheet piles, trestles and dredging (jetty-berth-and-jetty-structures-piled-jetties-quay-walls-caissons)

Primary code: MID: Midstream
Provide the load-bearing berth face and access structure that transfers vessel berthing/mooring loads and terminal loads to the seabed, with dredged approach channels and berth pockets providing navigable depth.
Vendors: Trelleborg Marine & Infrastructure (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide the load-bearing berth face and access structure that transfers vessel berthing/mooring loads and terminal loads to the seabed, with dredged approach channels and berth pockets providing navigable depth. | Qualitative function from pages read in this sweep. |


### Fender design standards and guidance — PIANC, BS 6349, ACI, ASTM (jetty-fender-design-standards-and-guidance-pianc-bs-6349-aci-astm)

Primary code: MID: Midstream
Provide the calculation framework for berthing energy, fender selection, reaction loads, mooring loads and marine concrete durability; used by designers worldwide as guidance or by reference in codes.
Vendors: Trelleborg Marine & Infrastructure (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| PIANC WG33 publication year and status | 2002 year | PIANC USA webinar page: WG33 published Guidelines for the Design of Fenders Systems: 2002; 'the one reference document to which all other national guidelines and codes that specify or prescribe fender design refer' |


### Floating pneumatic rubber fenders (jetty-floating-pneumatic-rubber-fenders-yokohama-type)

Primary code: MID: Midstream
Floating shock absorber between two vessels (STS) or vessel and quay; accommodates tidal range and ship vertical movement; soft, non-linear reaction force protects hull and jetty under overload and inclined berthing.
Vendors: The Yokohama Rubber Co., Ltd., ShibataFenderTeam, Doowin Marine, Pacific Marine & Industrial (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pneumatic 50 — guaranteed energy absorption (GEA) across standard sizes | 6-6473 kNm | Yokohama published 'Pneumatic 50 Standard Sizes' table, from 500x1000 mm (GEA 6 kNm) to 4500x12000 mm (GEA 6473 kNm), initial internal pressure 50 kPa |
| Pneumatic 80 — guaranteed energy absorption (GEA) across standard sizes | 8-9037 kNm | Yokohama 'Pneumatic 80 Standard Sizes' table, from 500x1000 mm (GEA 8 kNm) to 4500x12000 mm (GEA 9037 kNm), initial internal pressure 80 kPa |
| Inclined berthing energy retention | no decrease up to 15 degrees | Yokohama page: 'energy absorption does not decrease at inclined compression up to 15 degrees' for Yokohama Pneumatic Rubber Fenders (comparative diagrams vs solid and foam fenders) |
| Low-pressure pneumatic fender GEA | 676-1565 kNm | Yokohama low-pressure table, 10 kPa initial pressure: 2500x9100 mm -> 676 kNm, reaction 1901 kN, hull pressure 88 kPa; 3300x12700 mm -> 1565 kNm, reaction 3439 kN, hull pressure 89 kPa |
| ISO 17357-1:2014 bead-ring requirement | less than 0.20 D ratio (D = fender diameter) | Yokohama explanation of ISO 17357-1:2014 new requirements, to keep metal parts safe from permanent deformation at ~80% over-compression |


### Marine / shore-to-ship loading arms and transfer systems (jetty-marine-shore-to-ship-loading-arms-and-transfer-systems)

Primary code: MID: Midstream
Articulated pipework with swivel joints connecting shore or offshore facility to ship for transfer of oil, LNG, LPG, chemicals, high-pressure gas, CO2 and hydrogen; includes emergency release systems (ERS) and quick connect/disconnect couplers (QC/DC).
Vendors: Technip Energies, Flowtork Technologies Corporation, TBG Technologies (Chokusen), Japan (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flowtork/Technip Energies refining & petrochemical loading arm diameter | 6-24 inches | Flowtork (Philippines distributor) page for Technip Energies loading systems: 'Diameter 6 to 24 inches, design pressure up to 50 bar'; options heat tracing, insulation, EasyDrive, automatic connection |
| ATOL 20 inch full-bore product line | 20 inches full bore | Flowtork page: 'ATOL – Articulated Tandem Offshore Loader: Rigid transfer system for LNG transfer with high-flow performance and 20 inch full-bore product lines' |
| Technip Energies installed base / patents / experience | +15,000 installed loading arms; 57 patents; 70+ years count / years | Technip Energies Loading Systems page figures: '57 patents', '70+ years of experience', '+15K installed loading arms', '300+ employees worldwide' |
| installed loading arms | 15000 count (+15K stated) | Value as printed in the cited source; no further qualifier stated. |
| patents | 57 count | Value as printed in the cited source; no further qualifier stated. |
| diameter | 6-24 inches | Value as printed in the cited source; no further qualifier stated. |
| design pressure | 50 bar (up to) | Value as printed in the cited source; no further qualifier stated. |


### Marine utility and navigation systems (jetty-marine-utility-and-navigation-systems-fire-water-foam-draina)

Primary code: MID: Midstream
Support safe terminal operation: fire protection, oily-water/drainage handling, sewage, electrical power and lighting, and navigation aids.
Vendors: Vikoma International Ltd (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Support safe terminal operation: fire protection, oily-water/drainage handling, sewage, electrical power and lighting, and navigation aids. | Qualitative function from pages read in this sweep. |


### Mooring quick release hooks (jetty-mooring-quick-release-hooks-qrh-bollards-and-load-monitoring)

Primary code: MID: Midstream
Secure mooring lines at jetties/berths/dolphins, release safely under load, and monitor line tension to warn of surging or overload.
Vendors: Trelleborg Marine & Infrastructure, ShibataFenderTeam (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Trelleborg QRH installed base and service dates | since 1972; over 600 mooring facilities worldwide; SmartMoor over 100 FPSO facilities (hawser hooks) count/year | Trelleborg QRH product page (installed since 1972) and company brochure search snippets ('installed in over 600 mooring facilities worldwide'; hawser hooks 'installed in over 100 FPSO facilities') |
| LMT2 T-head bollard rated mooring capacity | 80 tonnes | ShibataFenderTeam LMT2 project: 37 T-head bollards with a rated mooring capacity of 80 tonnes |


### Motion-compensated access gangways / boarding bridges (jetty-motion-compensated-access-gangways-boarding-bridges)

Primary code: MID: Midstream
Transfer personnel and cargo between vessel and fixed or floating structure with active compensation of vessel motions (6 degrees of freedom), extending the weather window for crew change and transfer.
Vendors: Ampelmann Operations B.V. (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ampelmann E-type significant wave height compensation | 4.5 m Hs | Ampelmann E-type product page: 'safely transferring personnel in sea states up to 4.5m Hs'; full 6-DOF compensation, zero movement of gangway during operation |
| Ampelmann E-type gangway length / footprint / weight | 30 m / 8.4 x 9.5 m / 105 mt m, m x m, metric tonnes | Ampelmann E-type page specification tiles |
| wave compensation | 4.5 m Hs | Value as printed in the cited source; no further qualifier stated. |
| gangway length | 30 m | Value as printed in the cited source; no further qualifier stated. |
| footprint | 8.4 x 9.5 m | Value as printed in the cited source; no further qualifier stated. |
| system weight | 105 metric tonnes | Value as printed in the cited source; no further qualifier stated. |


### Oil spill response — containment booms, skimmers and recovery (jetty-oil-spill-response-containment-booms-skimmers-and-recovery)

Primary code: MID: Midstream
Contain spilled oil on water, protect jetty/harbour intake areas and recover oil with skimmers, pumps and temporary storage.
Vendors: Vikoma International Ltd, DESMI (Ro-Clean) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Boom materials and deployment characteristics | Neoprene (vulcanised) or polyurethane; air or foam filled material/configuration | Vikoma Information Hub article (page fetched): neoprene gives wave-following flexibility; polyurethane is lower cost but less robust; foam-filled needs no inflation but more storage; air-filled inflation time depends on design |
| inflated height (catalogue range) | 750-1500 mm | Value as printed in the cited source; no further qualifier stated. |
| freeboard | 335-600 mm | Value as printed in the cited source; no further qualifier stated. |


### Rubber fenders — cone, cell, element and V/arch types (jetty-rubber-fenders-cone-cell-element-and-v-arch-types-fixed-jett)

Primary code: MID: Midstream
Absorb berthing kinetic energy and limit reaction force and hull pressure transmitted to the vessel and the berth structure; remain functional when a vessel is moored ('lean-on' loads).
Vendors: ShibataFenderTeam Group, Trelleborg Marine & Infrastructure, The Yokohama Rubber Co., Ltd., Pacific Marine & Industrial (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| SPC cone fender overall height, range across published sizes | 300-2000 mm | ShibataFenderTeam SPC cone fender standard size table, SPC 300 to SPC 2000; page states 'heights between 300 and 2,000 mm' in 3 main rubber grades |
| SPC 2000 cone fender diameter / weight / anchors | 3090 mm outer diameter (Ø D); weight 9,560 kg; 10 x M56 anchors | Largest size in the published SPC dimension table (SPC 2000, H 2000 mm, Ø d 1750 mm) |
| V-fender SX/SH standard height range | 250-1000 mm | ShibataFenderTeam V-fender page: standard heights 250-1,000 mm, standard lengths 1,000-3,500 mm, 3 rubber grades |
| SX 1000 V-fender dimensions | 1000 mm H; W 1800 mm; w 800 mm; t 47 mm; C 610 mm; PW 1550 mm; anchors M48 | Published SX fender dimension table, row SX 1000 |
| Pneumatic 50 GEA range | 6-6473 kNm | Value as printed in the cited source; no further qualifier stated. |
| Pneumatic 80 GEA range | 8-9037 kNm | Value as printed in the cited source; no further qualifier stated. |
| initial internal pressure | 50 or 80 kPa | Value as printed in the cited source; no further qualifier stated. |
| height range | 300-2000 mm | Value as printed in the cited source; no further qualifier stated. |
| SPC 2000 mass | 9560 kg | Value as printed in the cited source; no further qualifier stated. |
| SPC 2000 anchor bolts | 10 x M56 count/size | Value as printed in the cited source; no further qualifier stated. |
| SX standard heights | 250-1000 mm | Value as printed in the cited source; no further qualifier stated. |
| standard lengths | 1000-3500 mm | Value as printed in the cited source; no further qualifier stated. |
| SX 1000 width | 1800 mm | Value as printed in the cited source; no further qualifier stated. |


### Storage tanks, bunds and tank-farm equipment (jetty-storage-tanks-bunds-and-tank-farm-equipment-api-650-api-620)

Primary code: MID: Midstream
Bulk liquid storage at terminals: fixed cone roof, internal floating roof (IFR), external floating roof (EFR), double-deck floating roof (DDFR); secondary containment/bunds; associated pumps, metering and loading.
Vendors: L-Vision Engineering Pte Ltd, Tank Built Pte Ltd, HAIL (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Bulk liquid storage at terminals: fixed cone roof, internal floating roof (IFR), external floating roof (EFR), double-deck floating roof (DDFR); secondary containment/bunds; associated pumps, metering and loading. | Qualitative function from pages read in this sweep. |


## laboratories

### Laboratories (utility-laboratories)

Primary code: PCH: Petrochemicals
Laboratories
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Product specification context | urea prill -6+18 US Mesh; max biuret 0.5% specification | Pusri urea EPD describes product as prills -6+18 US Mesh with main N content and maximum biuret 0.5% |


## lube-oil

### Lube oil system: pumps, filters, coolers, sump (gas-engine-lube-oil-system)

Primary code: PWR: Power and renewables
Lube oil system: pumps, filters, coolers, sump | Lube-oil storage, transfer, filtration and make-up
Vendors: INNIO Jenbacher, Rehlko, Cummins Inc. (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Scope inclusion | Lube oil supply system qualitative | Jenbacher Type 6 containerised solution, usual scope of supply; alongside container ventilation, cooling systems and control panel/gas train |
| Lube oil grade | mono-grade SAE 40 (most Cummins lean-burn gas gensets); never use diesel engine oil in a natural gas engine SAE viscosity grade | Cummins Gas Power Plant Application Manual section 3.2.1 |
| Service (day) tank base elevation above floor for gravity feed | 1-4 m | Cummins Gas Power Plant Application Manual section 3.2.3: tank base between 1 and 4 m above floor level for adequate gravity feed to engine sump |
| Minimum oil make-up tank capacity | 100 litres (27 US gallons) | Cummins Gas Power Plant Application Manual section 3.2.4.2: design not specified but tank must contain a minimum of 100 liters; total capacity depends on expected running hours and genset datasheet oil consumption |
| Make-up tank connection pipe internal diameter | 0.75-? inch I.D. minimum | Cummins Gas Power Plant Application Manual section 3.2.4.2: make-up tank mounted away from engine, connected by suitable pipework of at least 3/4 inch I.D. |
| Fresh oil piping / siphon protection | pickled or cold-drawn pickled pipe; strainer and foot valve on storage tank suction; solenoid valve if service tank lower than storage tank to prevent siphon overfill qualitative design rule | Cummins Gas Power Plant Application Manual section 3.2.3 |
| Lubrication system in common plant architecture | Lubrication System listed among power-plant common systems (alongside gas piping/pressure reduction, gas storage, electrical distribution, control, fire detection) qualitative | Schneider Electric White Paper 286, Figure 5 'A high-level presentation of the power plant components' |


Recorded gaps:

- Sump capacity, oil pump flow/pressure, filter micron ratings and cooler duty — Fetch OEM engine data sheets and lube-oil system P&IDs from Jenbacher customer portal (login required)
- Named independent lube-oil pump/filter/cooler suppliers — Search and fetch OEM/specialist datasheets (e.g. Boleng, Facet, Hilliard)

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

## maintenance

### Maintenance and workshops (utility-maintenance-workshops)

Primary code: PCH: Petrochemicals
Maintenance and workshops
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Maintenance and workshops | Qualitative function from pages read in this sweep. |


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

## methanation

### Methanation and syngas drying/purification (ammonia-methanation-purification)

Primary code: PCH: Petrochemicals
Methanation and syngas drying/purification
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| PK-5 ring-shaped methanation catalyst pressure-drop reduction | 30-70 % lower pressure drop | Topsoe PK-5 versus conventional sphere- or cylindrical-shaped methanation catalysts |
| Methanation reactions | CO + 3H2 -> CH4 + H2O; CO2 + 4H2 -> CH4 + 2H2O qualitative | Final hydrogen-purification step in Haber process |
| Typical methanation section pressure | 25-35 bar absolute | Steam reforming, shift, CO2 removal and methanation each operate at about 25-35 bar absolute |
| SynCOR syngas cleaning | nitrogen wash with purge and nitrogen addition qualitative | Topsoe comparison: conventional uses methanation; SynCOR uses nitrogen wash, enabling inert-free synthesis loop with no purge |
| Pressure drop reduction vs sphere/cylinder catalysts | 30-70 % | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Syngas dryer type/design (molecular sieve vs glycol) andOutlet moisture specification — Fetch a syngas drying/purification OEM page or ammonia plant design reference.
- Syngas dryer type/design (molecular sieve vs glycol) andOutlet moisture specification — Fetch a syngas drying/purification OEM page or ammonia plant design reference.

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

## near-civil

### Bridges, helidecks and accommodation modules (near-bridges-helidecks-and-accommodation-modules)

Primary code: UPS: Upstream
Connect platforms, enable helicopter transfer, and house crew.
Vendors: Vantris Energy Berhad (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| living quarter + bridge fabrication scope, East Piatu | 4161 metric tonnes (combined topside scope) | Newfield Malaysia, includes topside, CPP, living quarter and bridge |
| permanent living quarters and office cabins, Cakerawala gas field | supply and installation scope n/a | Carigali Hess, Feb 2013-Aug 2013 |


### Concrete gravity-base structures (near-concrete-gravity-base-structures-gbs-and-caissons)

Primary code: UPS: Upstream
Self-weight founded structures avoiding piling; cells can provide oil storage and separation.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Brent GBS weight | several hundred thousand tonnes each tonnes | Shell description of Brent Bravo/Charlie/Delta gravity base structures |
| Brent storage/separation cells | 64 total (42 used for storage/separation), each 60 m tall count / m | Shell Brent decommissioning process |
| ISO concrete offshore structures standard | ISO 19903:2019 (Published); ISO/AWI 19903 under development n/a | ISO/TC 67/SC 7 catalogue |
| caisson types in ISO 19902 scope | free-standing and braced caissons n/a | ISO 19902:2020 abstract |


### Deck cranes, davits and lifting appliances (near-deck-cranes-davits-and-lifting-appliances)

Primary code: UPS: Upstream
Pedestal/knuckle-boom and active-heave-compensated cranes for supply vessel transfers, subsea lifts and module handling.
Vendors: PALFINGER, Liebherr, Huisman Equipment (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| PALFINGER AHC hoisting capacity / jib radius / wire | up to 250 t / up to 50 m / 3,000 m wire (standard range) t / m / m | PALFINGER AHC Cranes feature list |
| PALFINGER winterization | reliable performance down to -50 °C; DNV, BV, LRS, ABS compliance °C | PALFINGER AHC Cranes winterization section |
| hoisting capacity | up to 250 t | Value as printed in the cited source; no further qualifier stated. |
| jib radius | up to 50 m | Value as printed in the cited source; no further qualifier stated. |
| wire capacity | 3000 m | Value as printed in the cited source; no further qualifier stated. |
| winterization | -50 °C | Value as printed in the cited source; no further qualifier stated. |


### Drilling, grouting and seabed preparation (near-drilling-grouting-and-seabed-preparation)

Primary code: UPS: Upstream
Drill through difficult ground (drive-drill-drive), grout pile-to-sleeve or monopile connections, prepare seabed and clear UXO before foundation installation.
Vendors: Acteon / Menck, Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| 3D method purpose | combines pile driving and drilling to reach target depth in hard, rocky or variable ground n/a | Acteon brochure listing 'Drive-drill-drive (3D) method for monopiles' |
| Veja Mate seabed preparation | UXO detection and removal before scour protection; rock placement by fallpipe vessel Rockpiper; each piling operation ~24 hours including driving through pre-laid scour protection n/a | Boskalis project page |
| Boskalis Aberdeen Bay scope | UXO survey and removal; seabed preparation; 11 suction bucket jacket installations n/a | Boskalis related-project card |


### Fixed steel jacket (near-fixed-steel-jacket-oil-gas)

Primary code: UPS: Upstream
Bottom-founded tubular space frame that transfers topsides, wind, wave, current and seismic loads into piled foundations; supports conductors and risers.
Vendors: Vantris Energy Berhad, Malaysia Marine & Heavy Engineering, Jan De Nul / Hitachi consortium (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| 8-legged jacket substructure net weight, Kebabangan (Malaysia) | 13393 metric tonnes | KBB substructure, engineering/procurement/fabrication/inspection/testing/pre-commissioning/loadout, Apr 2011-Sep 2012 |
| jacket with piles and appurtenances, Tapis R (Malaysia) | 5475 metric tonnes | ExxonMobil EMEPMI, Mar 2012-Jul 2013 scope |
| 6-legged jacket fabrication weight, Deen Dayal West (India) | 4530 metric tonnes | Larsen & Toubro / GSPC fabrication, loadout and seafastening Apr 2010-Jan 2011 |
| NASR field jacket net installed weight | 2270-3070 metric tonnes | 2 topsides and 3 jackets (Accommodation, Separation, Gas Treatment platforms), NASR and Umm Shait fields |


### Floating production interfaces (near-floating-production-interfaces-fpso-flng-fso)

Primary code: UPS: Upstream
Floating host for process, storage and offloading; interfaces with risers, moorings and fixed structures; relevant to CCS conversion of existing platforms.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Jotun A FPSO size / production | 92,000 DWT / 70,000 bpd DWT / bpd | Boskalis related-project card; producing on Jotun field (Norway) since 1999 |
| Porthos CO2 injection host | P18-A former gas production platform converted to CO2 injection platform; >20 km offshore pipeline laid n/a | Porthos official project site |


### Impact piling hammers (near-impact-piling-hammers-hydraulic-double-acting)

Primary code: UPS: Upstream
Drive jacket piles, conductors and monopiles by controlled hydraulic blows; integrated with drivability analysis and noise mitigation.
Vendors: Menck (Acteon Marine Foundations; sale to Cadeler announced Aug 2026), IQIP (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Menck hammer range energy | 100-6250 kJ | Acteon 'Hydraulic double acting impact hammers' page - hammer spread range |
| MHU800S energy range / oil flow / pressure / blow rate | 75-820 kJ / 1,600 L/min / 250 bar / 38 bl/min kJ / L/min / bar / blows per min | Acteon product specification table |
| MHU3500S energy range / oil flow / pressure / blow rate | 320-3,500 kJ / 5,800 L/min / 240 bar / 32 bl/min kJ / L/min / bar / blows per min | Acteon product specification table |
| MHU6000W energy range / oil flow / pressure / blow rate | 200-6,250 kJ / 12,800 L/min / 210 bar / 30 bl/min kJ / L/min / bar / blows per min | Acteon product specification table; largest in range |
| IQIP IQ8 blow energy | >7500 kJ | IQIP Hydrohammer page - 'strongest hydraulic impact hammer in the world' |
| Hydrohammer total range / operating history | 30 kJ to >7,500 kJ; >5.5 million piles installed; >97% availability kJ / count / % | IQIP Hydrohammer FAQ |
| energy range (spread) | 100-6,250 kJ | Value as printed in the cited source; no further qualifier stated. |
| MHU6000W | 200-6,250 kJ; 12,800 L/min; 210 bar; 30 bl/min kJ / L/min / bar / bl/min | Value as printed in the cited source; no further qualifier stated. |


### Inspection: ROV, AUV and drone-based remote inspection (near-inspection-rov-auv-and-drone-based-remote-inspection)

Primary code: UPS: Upstream
Close-up visual inspection, UT thickness measurement, corrosion mapping and CP verification in splash zone, tanks, risers and subsea structures without confined-space entry.
Vendors: Flyability, Deep Trekker, Oceaneering / Subsea 7 (ROV services) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| inspection time: rope/boat vs drone | 2-7 h vs days | Flyability comparison table: rope access/boat 3-7 days, drone 2-4 hours |
| crew footprint | 4-6 technicians vs 2 operators on deck persons | Flyability comparison table |
| Saipem COT/WBT inspection speed | 80-90% faster with zero human entry % | Saipem interview cited by Flyability; class-approved inspection |
| TotalEnergies FPSO hull digitalization cost reduction | 45 % | Flyability testimonial reference |
| BP confined-space hours saved | >1700 hours | Flyability: drones supporting BP offshore operations since 2023 |
| RIT acceptance | ABS, BV, LR, ClassNK, DNV, RINA rulebooks accept remote inspection techniques; IMO defines RIT as alternative means for close-up survey n/a | Flyability offshore drone inspection guide |


### Jack-up rigs (near-jack-up-rigs-mobile-offshore-units)

Primary code: UPS: Upstream
Mobile self-elevating drilling/workover platform with independent legs and jack houses; used for nearshore and shelf drilling.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| jack-up standard (elevated at a site) | ISO 19905-1:2023 (Amd 1:2025 corrections to tubular member strength, Table B-2, simplified free-field liquefaction method) n/a | ISO/TC 67/SC 7 catalogue |
| jack-up installation/removal standard | ISO 19905-4:2026 n/a | ISO/TC 67/SC 7 catalogue |
| jack-ups within fixed steel structure standard scope | included (site-specific assessment referred to ISO 19905-1) n/a | ISO 19902:2020 abstract / NOTE 2 |
| self-erected tender rig & derrick equipment set KM-I tonnage | 8750 metric tonnes | Kencana Mermaid Drilling, 2009-2010 |


### Legs, pile foundations, conductors and risers (near-legs-pile-foundations-conductors-and-risers)

Primary code: UPS: Upstream
Transfer structural and drilling loads to seabed; conductors guide and support wellheads; risers connect subsea wells to topsides.
Vendors: EEW Group, IQIP (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| wind jacket pin pile diameter / max length / max weight | 3 m / 82 m / 310 t m / m / t | Changhua TPC Phase 1 demonstration: 4 pin piles per jacket, 84 total, 21 jackets |


### Lifeboats, liferafts, davits and evacuation systems (near-lifeboats-liferafts-davits-and-evacuation-systems)

Primary code: UPS: Upstream
TEMPSC/free-fall lifeboats, rescue boats and launched liferafts for evacuation from fixed platforms, rigs and FPSOs.
Vendors: VIKING Life-Saving Equipment, Survitec Group (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| VIKING Norsafe free-fall approved drop height | 50 m | VIKING product insights: 'world record free-fall performance of up to 50 m approved drop height' |
| VIKING offshore evacuation system height capability | 81 m | VIKING offshore evacuation systems: chute- or slide-based, for heights up to 81 m |
| VIKING compact lifeboat capacities | 40 / 52 persons | VNJY range of enclosed lifeboats |


### Monopile foundations (near-monopile-foundations-offshore-wind-nearshore)

Primary code: UPS: Upstream
Single large-diameter tubular driven into seabed carrying wind-turbine or platform loads; commonly used with transition piece or TP-less design.
Vendors: Sif Group, CS WIND Offshore, EEW Group (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| monopile length | ?-120 m | Sif 'up to 120 metres' |
| monopile diameter | ?-11 m | Sif metric tile |
| maximum wall thickness | 160 mm | Sif metric tile |
| maximum monopile weight | 2000-2500 tonnes | Sif page states 'weigh a maximum of 2,000 tonnes each' in prose and '>2500 tonnes' in metric tile |
| monopile weight range (fabricator) | 1000-3500 tonnes | CS WIND Offshore monopile page |
| foundations fabricated since 2002 | >3100 count | CS WIND Offshore |
| Veja Mate monopile weight / height and water depth | 1,230-1,302 t; 85 m tall; water depth 39-41 m t / m / m | Boskalis Veja Mate EPCI project, German North Sea |


### Nearshore submerged tunnels and bridges (near-nearshore-submerged-tunnels-and-bridges)

Primary code: UPS: Upstream
Fixed crossings and immersed-tunnel elements in nearshore waters; relevant to platform/bridge interface structures and marine construction.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| bridges within ISO 19902 scope | bridges and connecting structures listed as related offshore structures n/a | ISO 19902:2020 abstract |
| Boskalis tunnels and bridges capability | listed market (no numeric spec) n/a | Boskalis site navigation |


### Offshore structural design standards (near-offshore-structural-design-standards-umbrella)

Primary code: UPS: Upstream
Governing codes for planning, design, fabrication, transport, installation, in-service management and removal of offshore structures.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ISO 19902:2020 | Edition 2, published 2020-11, 565 pages; being replaced by ISO/CD 19902 edition 3 n/a | ISO standard page |
| ISO 19901-3:2024 topsides structure | published (stage 60.60) n/a | ISO/TC 67/SC 7 catalogue |
| DNV-ST-0126 support structures for wind turbines | Edition 2021-12; general principles for structural design of wind turbine support structures n/a | DNV standards page |
| AWS D1.1/D1.1M:2025 | 25th edition; ANSI approved 2025-03-19; Amendment 1 January 2026; 8 normative and 11 informative annexes n/a | AWS standard page and preview PDF |


### Pipe racks, cable trays, gratings, handrails and access platforms (near-pipe-racks-cable-trays-gratings-handrails-and-access-platfor)

Primary code: UPS: Upstream
Secondary steel that routes piping/cables and provides safe access and walkways on topsides and wind foundations.
Vendors: CS WIND Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| external platforms and anodes | CS WIND fabricates/mounts external platforms and both static anodes and dynamic ICCP systems n/a | CS WIND monopile page |
| heated gangways, stairs, ladders and railings | listed as winterization features on PALFINGER offshore cranes n/a | PALFINGER AHC cranes page |
| secondary steel scope | CS WIND Offshore product line 'Secondary Steel' n/a | CS WIND solutions navigation |


### Scour protection (near-scour-protection-rock-dumping-mattresses-bags)

Primary code: UPS: Upstream
Prevent seabed erosion around monopiles/jackets and over cables; filter layer plus armour layer, or flexible mattresses / sand containers.
Vendors: Boskalis (Dockwise heritage), Naue GmbH & Co. KG, Ridgeway Marine, ContiTech (Continental Group), Van Oord / DEME / Jan De Nul (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| West of Duddon Sands armour rock grading | 8-18 inch (20-45 cm) in / cm | 108 turbines; filter layer at 108 locations before monopile installation; side-dump armour placement after installation |
| Meerwind armour rock mass | 100-700 kg | 80 monopile locations; pre-installation 1-5 inch filter material |
| Anholt filter / armour grading | 1-4 inch filter + 2-8 inch armour in | 42 WTG foundations |
| Ridgeway filter bag design life | 50 years | polyester filter bag, 61% recycled bottles, filled with stones; produced by Sumisho Kyowa, used at EDF Teesside |
| ContiTech mat thickness / diameter | 12-15 mm / up to 52 m mm / m | conveyor-belt type mat tested at Deltares under simulated extreme storms and streams |
| NAUE Secutex Soft Rock | needle-punched nonwoven geotextile sand container; used at Amrumbank West n/a | offshorewind.biz scour protection article |


### Structural health monitoring (near-structural-health-monitoring-shm-and-fatigue-management)

Primary code: UPS: Upstream
Instrument critical details with strain/acceleration/acoustic sensors to support fatigue assessment, early crack detection and operational decisions.
Vendors: Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| fatigue design standard | DNV-RP-C203, Edition 2024-10, amended 2025-10 n/a | DNV standards page |


### Structural integrity management and decommissioning planning (near-structural-integrity-management-and-decommissioning-planning)

Primary code: UPS: Upstream
Lifecycle process: data, evaluation, strategy, inspection programme, fitness-for-purpose assessment, risk reduction and decommissioning.
Vendors: Allseas (OEM design), Able UK (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ISO structural integrity management standard | ISO 19901-9:2019 (published); ISO/CD 19901-9 under development n/a | ISO/TC 67/SC 7 catalogue |
| Brent topsides reuse/recycling target | 97 % | Shell Brent decommissioning: Allseas single-lift removal, Able UK reuse/recycling |


### Topsides, decks and module support frames (near-topsides-decks-and-module-support-frames)

Primary code: UPS: Upstream
Process, drilling, utilities and accommodation modules carried above the jacket; module support frames distribute loads to jacket legs.
Vendors: Vantris Energy Berhad, Malaysia Marine & Heavy Engineering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| CUQ / DPP float-over topside weight, Bayu Undan (Timor Sea) | 11,500 t / 15,000 t t | ConocoPhillips Bayu Undan floatover, Feb 2004 |
| Angel Platform topside floatover weight, Western Australia | 7700 tonnes | Woodside Angel gas field, Nov 2005-Jun 2008 EPCI |
| Maari wellhead platform (base + support + process deck), New Zealand | 10000 tonnes (approx.) | OMV New Zealand EPIC contract, Taranaki Basin |
| topside + CPP + living quarter + bridge, East Piatu (Malaysia) | 4161 metric tonnes | Newfield Peninsular Malaysia fabrication scope Jul 2010-Aug 2011 |
| Brent Delta accommodation capacity | 161 persons | topsides house accommodation block, helipad, drilling and operational areas; kitchen/cinema/gym |


### Vibratory piling and vibratory/suction installation equipment (near-vibratory-piling-and-vibratory-suction-installation-equipmen)

Primary code: UPS: Upstream
Alternative to impact driving for sheet piles, tubular piles and jackets in granular soils; suction installation uses differential pressure.
Vendors: IQIP (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| IQIP vibratory product families | VibroLift VQ; Vibrohammer F-series and Z-series n/a | IQIP product navigation |
| PULSE effect | extends hammer impact duration to reduce underwater noise, pile fatigue and operating costs n/a | IQIP Hydrohammer FAQ |
| suction bucket jacket installations | 11 count | Aberdeen Bay suction bucket jacket project (Boskalis) |


### Wind-turbine jacket foundations and suction-bucket jackets (near-wind-turbine-jacket-foundations-and-suction-bucket-jackets)

Primary code: UPS: Upstream
Four-legged lattice substructure for offshore wind; pin piles or suction buckets transfer loads to seabed.
Vendors: Samkang (South Korea), Edgen Murray (yard manager) / Ming Rong Yuan (Taiwan fabricator), Boskalis (Dockwise heritage) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Changhua jacket height / weight / steel | 60 m / >1,100 t each / >23,000 t total for 21 jackets m / t / t | TPC Changhua Phase 1 demonstration, fabricated by Samkang, South Korea |
| transition piece maximum diameter / height | 5.40 m / 7 m m / m | Changhua jackets for 5.2 MW turbines |
| Aberdeen Bay suction bucket jackets | 11 count | Boskalis scope: design/fabrication of jacket foundations, UXO survey/removal, installation of 11 suction bucket jackets, scour protection, 66 kV cables |


## nitrogen

### Nitrogen and inert gas supply (utility-nitrogen-inerting)

Primary code: PCH: Petrochemicals
Nitrogen and inert gas supply
Vendors: Air Liquide Japan (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Inert-gas supply | usually nitrogen utility | Site utility list includes inert-gas supplies (usually nitrogen); ammonia, nitrogen and CO2 also used as refrigeration working fluids in some situations |
| Nitrogen source for synthesis | air separation process | Hydrogen reacts with nitrogen derived from air separation; relatively pure N2 can be obtained by air separation with additional oxygen removal possibly required |
| Cryogenic nitrogen generator BEDP contractor | Air Liquide Japan supplier | Allied Green Ammonia project: Air Liquide Japan contracted for BEDP for cryogenic nitrogen generator (July 2024) |


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

## palletisers

### Palletisers (bulk-palletisers)

Primary code: PCH: Petrochemicals
Palletisers
Vendors: OCME S.r.L. (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| high-level infeed | 7-10.33 ft (2.13-3.15 m) | Wikipedia Palletizer: conventional and robotic palletizers can receive product at high elevation |
| floor-level infeed | 2.5-3.0 ft (0.76-0.91 m) | Wikipedia Palletizer: low 'floor level' elevation |
| first mechanized palletizer | 1948 year | designed, built and installed by a company formerly known as Lamson Corp |
| end effector package types | cases, bags, pails, drums, bottles n/a | Wikipedia Palletizer: end of arm tooling evolved to accommodate variation of pack patterns and package types |


Recorded gaps:

- Palletizer throughput (layers/hour), bag patterns, pallet sizes, OEM model specs — Fetch a palletizer OEM page.
- Palletizer throughput (layers/hour), bag patterns, pallet sizes, OEM model specs — Fetch a palletizer OEM page.

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
Vendors: Malaysia Transformer Manufacturing (MTM), Hitachi Energy, Siemens Energy (incl. ex-Dresser-Rand), GE Vernova, HD Hyundai Electric (5 model lines recorded).

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
- **Siemens Energy (incl. ex-Dresser-Rand)** Transformers: distribution to UHV
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
| Furnace firing temperature | 2800 deg F (up to) | Max-Fire Product Overview: 'integral water-cooled furnace utilizing membrane-wall construction for firing temperatures up to 2800 F', avoiding high-maintenance refractory |
| Furnace construction | 100% membrane water-cooled, refractory free; welded front and rear walls also water cooled construction | CBCW Product narrative and Product Overview |
| Styles | D-type and O-type styles | CBCW Technical Data table |


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
| Standard straight tube length | 50-510 inches | Boiler Tubes page 'Types of Boiler Tubes': Standard Straight Boiler Tubes available from 50-510 in |
| Rifled (XID) tube length | 50-366 inches | Boiler Tubes page: Rifled tubes available from 50-366 in; internal grooves increase heat transfer by creating turbulence |
| Material | Premium ERW SA178 steel produced to ASME Boiler & Pressure Vessel Code requirements material | Boiler Tubes page 'OEM Quality You Can Trust' |
| Heat exchanger tube bending | 0.75-1.5 inch OD | Boiler Tubes page Tube Fabrication: ¾-1½ in OD tubes, radius sizes 2-15½ in, stainless and mild steel |
| Tube replacement bending | 1.5-4 inch OD | Boiler Tubes page: hot and cold bending capabilities include 1½ up to 4 in OD |
| Other products | Membrane tubes, tube panels, economizer tubes, superheater tubes, swaging scope | Boiler Tubes page Tube Replacement section |
| Quality documentation | Material traceability, MTR documentation, non-destructive testing, ASME compliance quality | Boiler Tubes page 'Certified Materials' |
| Heat transfer increase | 85 % | CBEX Product Overview: extended heat transfer tubes with CFD-optimized geometry increase heat transfer by 85% |
| Effective heat transfer surface | 5 times greater than other condensing boilers | ClearFire-CE Product Overview: AluFer tube technology increases effective heat transfer surface area up to five times |
| Thermal conductivity | 10 times greater than stainless steel alone | ClearFire-CE Product Overview |


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
| Drum arrangement | Large separate steam drums with high efficiency drum internals design feature | Modular HRSG Product Overview bullets |
| Circulation | Vertical tube natural circulation; hydraulically matched downcomers and risers design feature | Modular HRSG Product Overview bullets and Technical Data table 'Vertical Tube with Steam Drum' |
| Drum design | Large steam drums to assure ample steaming area; downcomers on both ends of boiler design feature | Max-Fire Product Overview bullets |


Recorded gaps:

- drum dimensions, retention time and circulation ratio for the package lines — Read a package-boiler data sheet with drum details.

## prilling-tower

### Urea prilling tower (urea-prilling-tower)

Primary code: PCH: Petrochemicals
Tall tower in which molten urea is sprayed from the top and solidifies in falling droplets cooled by rising air, producing small round prills. Tower height and airflow set the prill size and the product's cooling and hardening; prills are smaller and more spherical than fluid-bed granules.
Vendors: Stamicarbon, Saipem (ex-Micoperi 7000), Casale, Toyo Engineering (1 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| tower height | 80-140 m | height varies with plant load and weather |
| large-unit capacity | 3000-very high t/d | large prilling units of at least 3,000 t/d of urea prills |
| large-unit dimensions | at least 100 high and 20 in diameter m | large prilling towers |
| prill size | 1.65 mm | typical prill diameter, compared with 2.82-3.06 mm granules |
| prill size limit | 2.1 mm diameter | Wikipedia: prills limited to about 2.1 mm diameter, with low crushing strength and caking/crushing in bulk storage and handling |
| prill formation mechanism | drops of melted material congeal/freeze in mid-air after dripping from top of a tall prilling tower n/a | Wikipedia Prill; material must be solid at room temperature and low-viscosity liquid when melted |
| prilling displacement trend | prilling of ammonium nitrate and urea replaced in recent years by fluid bed granulation giving stronger, more abrasion-resistant granules n/a | Wikipedia Prill, citing Van't Land, Industrial Crystallization of Melts (2004), p.117 |
| formaldehyde additive | added during production of both prills and granules to increase crushing strength and suppress caking n/a | Wikipedia Urea finishing |

- **Stamicarbon** Prilling Design: rotating buckets distribute liquid urea droplets evenly in the tower; optional seeding

Recorded gaps:

- Tower height/diameter, airflow, droplet size distribution, nozzle/bucket design and capacity — Find a prilling tower vendor/OEM page or old engineering design paper.
- Tower height/diameter, airflow, droplet size distribution, nozzle/bucket design and capacity — Find a prilling tower vendor/OEM page or old engineering design paper.

## process

### Process condensate treatment and sour water stripping (ammonia-sour-water-stripping)

Primary code: PCH: Petrochemicals
Process condensate treatment and sour water stripping | Effluent / wastewater treatment (ammonia stripping and urea hydrolysis)
Vendors: SnamProgetti SpA (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Sour gas classification threshold | 5.7 mg H2S per m3 natural gas (~4 ppmv at STP) | Natural gas usually considered sour above this level; Texas Railroad Commission uses >100 ppmv for pipelines, TCEQ >24 ppmv upstream |
| Effluent quantity from urea synthesis reaction | 300 kg water per tonne urea | One mole of water formed per mole of urea from 2NH3 + CO2 |
| Total effluent to treatment | 500 kg per tonne urea | Adds ~150 kg/t urea wash/flushing water and ejector drive steam plus intermittent discharges; for a 1700 t/d plant about 850 m3/day |
| Indicative urea effluent composition | NH3 2-5 wt%; CO2 1-2.5 wt%; urea 0.5-2 wt%; balance water wt% | Indicative composition stated in patent description (a second table gives CO2 1-1.25 wt%) |
| Hydrolysis residence time | 20-40 min | Hydrolysis of urea/biuret at 200-240 C and 20-40 bar gauge; longer time has no appreciable effect |
| Stripping column operating conditions | 1.5-4 bar gauge | Stripping stages at 128-150 C; live steam to column base or reboiler |
| Treated effluent residual NH3 and urea | 0.4-10 ppm each | Residual content of between 10 and 0.4 ppm for each pollutant; below 1 ppm possible with preferred conditions, suitable as boiler feed water up to 110 bar steam |
| Process condensate treatment in urea plant boundary | process condensate treatment unit | Pusri urea EPD cradle-to-gate system boundary includes crystallizer, prilling and process condensate treatment |


Recorded gaps:

- Ammonia-plant process condensate stripper design (number of trays, steam rate, overhead NH3 concentration) — Fetch an EPC/OEM sour-water stripping page or ammonia plant environmental-control reference.
- Ammonia-plant process condensate stripper design (number of trays, steam rate, overhead NH3 concentration) — Fetch an EPC/OEM sour-water stripping page or ammonia plant environmental-control reference.

### Process control, analysers, safety and ventilation (urea-control-safety-ventilation)

Primary code: PCH: Petrochemicals
Process control, analysers, safety and ventilation
Vendors: SensoTech GmbH, Stamicarbon, LESER, Badotherm, AMMO (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| LiquiSonic measuring range - concentration | 0-100 m% | SensoTech typical measuring range |
| LiquiSonic measuring range - temperature | -10-140 degC | SensoTech typical measuring range |
| controller capacity | 4 sensors per LiquiSonic Controller 30 | SensoTech: Controller 30 can be connected with up to 4 sensors |
| analyser vs lab time saving | 1 hour per day | SensoTech stated customer benefit: time required 1 h per day for laboratory measurements reduced by inline analysis |
| sensor line size | DN80 nominal pipeline diameter | SensoTech: immersion sensors installed at outlet of decomposer, typically DN80 pipelines |
| conveyor safety devices | trip cords, belt sway switches, speed switches, belt rip switches, emergency stops; OSHA 1926.555 n/a | Wikipedia Conveyor belt safety system |
| silo confined-space ventilation | dedicated electric fan or silo blower to blow fresh air before entry; methane can displace oxygen n/a | Wikipedia Silo safety - unloading process |
| ammonia leak incident reporting | 13 Sept 2026: two workers dead, up to 114 injured; 14 Sept 2026: up to 14 injured n/a | UreaKnowHow home page news headlines on ammonia leaks at nitrogen fertilizer plants |
| installed base | technology used in half of the world's urea plants n/a | Stamicarbon profile claim on UreaKnowHow |
| concentration range | 0-100 m% | typical measuring range |
| temperature range | -10-140 degC | typical measuring range |
| sensors per Controller 30 | 4 count | controller specification |


Recorded gaps:

- Safety instrumented system (SIS) design, gas detector models/setpoints, ventilation rates for urea bagging buildings, DCS vendor — Fetch an HSE/OSHA guidance page with a working URL and a process-safety vendor page.
- Safety instrumented system (SIS) design, gas detector models/setpoints, ventilation rates for urea bagging buildings, DCS vendor — Fetch an HSE/OSHA guidance page with a working URL and a process-safety vendor page.

## product

### Product storage, warehouses, bagging plants and loading-station dust extraction (bulk-warehousing-dust-extraction)

Primary code: PCH: Petrochemicals
Product storage, warehouses, bagging plants and loading-station dust extraction
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| unit collector applications | bins and silos or remote belt-conveyor transfer points n/a | Wikipedia Dust collector unit collectors section |
| unit collector capacity range | 200-2000 ft3/min (90-900 L/s) | Wikipedia Dust collector |
| dust explosion risk | finely granulated dust in air plus spark can trigger dust explosion powerful enough to destroy a concrete silo n/a | Wikipedia Silo, Dry-material/bin hazards section |


Recorded gaps:

- Warehouse storage capacity, bagging line count, dust-extraction air volumes and duct velocities — Fetch a fertilizer terminal/bagging plant case study.
- Warehouse storage capacity, bagging line count, dust-extraction air volumes and duct velocities — Fetch a fertilizer terminal/bagging plant case study.

## protection-relays

### Protection relays and substation IEDs (ele-protection-relays)

Primary code: ELE: Electrical engineering
Numerical protection relays and IEC 61850 intelligent electronic devices for overcurrent, distance, differential and transformer protection on the Malaysian grid and industrial systems, type-tested to IEC 60255.
Vendors: Schweitzer Engineering Laboratories (SEL), Siemens Energy (incl. ex-Dresser-Rand), Hitachi Energy, GE Vernova (4 model lines recorded).

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
- **Siemens Energy (incl. ex-Dresser-Rand)** SIPROTEC 5: IEC 60255-151 type-tested
- **Hitachi Energy** Relion: transmission protection
- **GE Vernova** UR (Universal Relay): transmission protection

Recorded gaps:

- delivered Malaysian pricing from a panel integrator — Ask owner for an integrator quote if a project budget needs it

## pump

### Boiler circulation pumps / forced-circulation pumps (HRSG, once-through, controlled circulation) (boiler-circulation-pump)

Primary code: PWR: Power and renewables
In forced/controlled-circulation HRSGs and boilers, a pump circulates water/steam-water mixture from the drum through parallel evaporator circuits and back, maintaining tube-wall wetting where natural density head is insufficient (horizontal tubes, limited drum-to-evaporator height, long circuits). Natural-circulation and once-through units need no circulation pump in normal operation (once-through with superimposed circulation uses one at start-up/low load).
Vendors: Cleaver-Brooks (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Circulation ratio rule of thumb for forced-circulation HRSG | 5 ratio (5:1 circulating flow to steam flow) | Esteem Projects HRSG tutorial; 20-25% steam generation by weight is the film-boiling 'danger' zone; 3:1 may suffice where drum is far below/above evaporator |


Recorded gaps:

- No named OEM of HRSG circulation pumps (e.g. KSB, Grundfos, Sulzer) with a fetchable HRSG-specific product page — Search 'HRSG circulation pump KSB / Sulzer / Ruhrpumpen' and fetch datasheets with flow/head/NPSH basis.
- No pump duty point (flow, head, NPSHr) for a specific HRSG circulation pump found — Locate an HRSG vendor proposal or EPC datasheet with forced-circulation pump duty.
- No SE Asia HRSG forced-circulation plant example found — Search regional EPC/HRSG supplier case studies.

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

### Condensate return pumps, hot wells / collection tanks and condensate return lines (pumping vs pressure return; (condensate-pump-hot-well)

Primary code: PWR: Power and renewables
Collect and return hot condensate to the boiler/feedwater system. Where trap inlet pressure cannot overcome return-line backpressure (lift + friction + receiver pressure = TDH), use electric centrifugal/turbine pumps, non-electric steam/air-driven mechanical pumps (SPDs/pump-traps), or ejector-assisted low-NPSH condensate pumps (TLV; Spirax Sarco).
Vendors: Spirax Sarco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| cavitation onset, condensate temperature | 80 °C | TLV: cavitation more typical with high-RPM motors when pumped liquid temperature rises above 80°C and NPSHA < NPSHR |
| elevated collection tank filling head above pump NPSHR | 3-5 m (10-16 ft) | TLV mitigation for hot condensate to raise NPSHA (if added backpressure acceptable) |
| ejector-assisted condensate pump minimum NPSHA | 1 m (3 ft) | TLV specialty pump with suction ejector; low filling-head installation |
| pump speed example affecting local pressure drop | 1,750 vs 3,500 RPM | TLV cavitation article: higher speed raises impeller velocity and local pressure drop |
| return-line backpressure components (TDH) | lift + pipe friction + receiver static pressure qualitative | TLV definition of Total Dynamic Head |


Recorded gaps:

- Hot-well sizing criteria and recommended storage minutes for each boiler type — Obtain vendor commissioning manuals or DOE steam system survey guide and cite the exact design rule.
- Condensate return line velocity/erosion limits and flash-steam allowance in sizing — Fetch TLV 'Condensate Recovery Piping' and Spirax block 13 pages for velocity and flash allowances.

### Feedwater pump duty, NPSH and selection for package boilers (boiler-feedwater-pump)

Primary code: PWR: Power and renewables
Maintain drum water level by delivering feedwater at flow above evaporation rate and at head above boiler pressure plus valve/piping losses; NPSH available must exceed pump NPSH required at hot feedwater temperature to avoid cavitation. Arrangements: direct feed per boiler or booster set feeding a common manifold with modulating feedwater valves.
Vendors: Grundfos, Cleaver-Brooks, Atlantic Feedwater Systems, Changyu Pump (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Applicability of the 16-step selection method | 100-1200 boiler horsepower; design pressure 150-500 psig | HPAC Engineering article by Steve Connor (Cleaver-Brooks) and Jim Swetye (Grundfos) |
| Base flow formula | boiler maximum-capacity HP x 0.069 x C; C=1.50 intermittent, C=1.15 continuous gpm (as presented) | HPAC article step 2; 0.069 is a stated constant |
| Continuous blowdown and bypass allowance | 10-20 percent of pump best-efficiency-point flow | HPAC steps 3-4: continuous blowdown often ~10% of BEP flow; bypass recirculation often 10-20% of BEP flow |
| Base head formula | max boiler operating pressure x 2.31 x 1.03 / liquid specific gravity feet of head | HPAC step 6; factor 1.03 is the safety margin on boiler pressure |
| Shutoff head above safety-valve setting | 3 percent | HPAC steps 10 and 14; shutoff head must be at least 3% above safety-valve setting |
| NPSHa definition | absolute pressure in feedwater tank +/- elevation of minimum water level above pump - vapor pressure of water in tank - suction-line friction loss formula (head units) | HPAC step 12; NPSHr vs NPSHa must be checked for every installation (step 15) |
| Guardian pump capacity | 10-18 GPM | Printed in Product Details table |
| Guardian discharge pressure | 20 psig | Printed in Product Details table |
| Guardian motor power | 1/3 HP | Printed in Product Details table |
| Guardian motor speed | 3450 RPM | Printed in Product Details table |
| Guardian tank capacity | 6-21 gal (cast iron); 10-20 gal carbon steel rectangular; 49-117 gal carbon steel cylindrical | Printed in Product Details table with three tank material/configuration rows |
| Guardian-Plus pump capacity | 1.5-150 GPM | Printed in Product Details table |
| Guardian-Plus discharge pressure | 10-70 psig | Printed in Product Details table |
| Guardian-Plus motor power | 1/3-10 HP | Printed in Product Details table |
| Guardian-Plus motor speed | 1750 or 3450 RPM | Printed in Product Details table |
| Guardian-Plus motor voltage | 115/208-230 V | Printed in Product Details table; single/three phase |
| Guardian-Plus tank capacity | 15-110 gal (cast iron); 21-110 rectangular; 49-1000 cylindrical | Printed in Product Details table |
| Water temperature capability | 250 deg F | Printed under Benefits and Features: 'Versatile compatibility of handling 250˚F water' |


Recorded gaps:

- A specific manufacturer pump curve selection (model, flow, head, NPSHr) for a named package boiler was not read — Fetch a Grundfos/KSB/Sulzer boiler-feed pump datasheet and record model, flow, head, NPSHr and temperature basis.
- KSB feedwater-pump product page not found/read — Target ksb.com boiler feedwater pump pages directly.
- No NPSHr value from an OEM for a package-boiler feed pump — Obtain OEM curve with NPSHr at the actual duty point.

## rectifying

### Rectifying columns / distillation columns (urea-rectifying-columns)

Primary code: PCH: Petrochemicals
Rectifying columns / distillation columns
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| distillation temperature (vendor description) | 70 degC | SensoTech: reaction mixture decompressed to atmospheric pressure and freed from ammonium carbamate in distillation columns at 70 C |


Recorded gaps:

- Column diameter/height, tray/packing type, reflux ratio, number of stages — Locate an authoritative urea process flowsheet/design paper.
- Column diameter/height, tray/packing type, reflux ratio, number of stages — Locate an authoritative urea process flowsheet/design paper.

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
| Method | Safe, proven, economical flash purification process for blowdown effectiveness and disposal process | Blowdown Systems catalog listing: 'Cleaver-Brooks model BDS blowdown separators and model BDT tanks use a safe, proven, economical flash purification process' |


Recorded gaps:

- code-specific setting and capacity certifies for ASME Section I versus EN 12953 — Verify against ASME BPVC Section I and EN 12953 before using these as design limits.

### Fire protection and gas detection (gas-engine-fire-gas-detection)

Primary code: PWR: Power and renewables
Fire protection and gas detection
Vendors: Wärtsilä (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Fire protection design requirements (genset enclosure) | design by competent licensed professional and reviewed by Cummins; uninterruptible emergency power for critical functions; smoke and heat detection in all non-sprinkled areas; alarms monitored 24/7 at constantly attended location qualitative | Cummins Gas Power Plant Application Manual, section 5.6.3 Fire Arrangements |
| Minimum fire rating of enclosure boundaries | 1 hour (walls, shutters, ceiling, doors and windows) | Cummins Gas Power Plant Application Manual, section 5.6.3 |
| Fire Detection System in plant common systems | listed as a common power-plant system and classified 'Non Critical' in the Schneider/Wärtsilä study (gas piping/pressure reduction, gas storage, electrical distribution, control system classified Critical) qualitative | Schneider Electric White Paper 286, Figure 5 |
| Ventilation damper fire behaviour | gravity-type dampers close on actuator failure or loss of AC power, starving enclosure of air and helping extinguish fire; dampers to be used with screen qualitative | Cummins Gas Power Plant Application Manual, section 3.3 ventilation/dampers |


## screw

### Screw conveyors (bulk-screw-conveyors)

Primary code: PCH: Petrochemicals
Screw conveyors
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| rate control | volume transfer rate proportional to rotation rate of the shaft n/a | Wikipedia Screw conveyor: used as variable rate feeder by varying shaft rotation |
| inclination effect | capacity of a given unit rapidly decreases as angle of inclination increases n/a | Wikipedia Screw conveyor |
| construction | trough or tube with spiral blade around a shaft (driven one end, held at other) or shaftless spiral driven at one end and free at the other n/a | Wikipedia Screw conveyor |
| Reciprocating gas compressor rating | ?-20 MW | Value as printed in the cited source; no further qualifier stated. |
| Reciprocating compressor speed | 260-1000 rpm | Value as printed in the cited source; no further qualifier stated. |
| Steam turbine electrical output range | 75-40000 kW | Value as printed in the cited source; no further qualifier stated. |
| Steam turbine mechanical drive range | 10-40 MW | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Screw conveyor diameter/pitch/capacity/power for urea service — Fetch a screw conveyor OEM engineering guide.
- Screw conveyor diameter/pitch/capacity/power for urea service — Fetch a screw conveyor OEM engineering guide.

## secondary

### Secondary reformer / autothermal reformer (ammonia-secondary-reformer-atr)

Primary code: PCH: Petrochemicals
Secondary reformer / autothermal reformer (ATR)
Vendors: Topsoe, Casale (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ATR syngas outlet temperature | 950-1100 deg C | Autothermal reforming outlet syngas temperature |
| ATR syngas outlet pressure | ?-100 bar | Outlet pressure can be as high as 100 bar (ATR) |
| ATR H2:CO ratio with CO2 | 1.0 mol/mol | ATR using carbon dioxide produces H2:CO = 1:1 |
| ATR H2:CO ratio with steam | 2.5 mol/mol | ATR using steam produces H2:CO = 2.5:1 |
| Methane at primary reformer exit after air addition to secondary | 1-2 % | Braun Purifier process: air added to secondary reformer reduces methane content of primary reformer exit stream to 1-2% |
| SynCOR Ammonia steam-to-carbon ratio | 0.6 mol/mol | Topsoe SynCOR Ammonia ATR-based grassroot concept; conventional comparison value 3.0 |
| Casale HyPURE-N (ATR) CO2 recovery | ?-99 % | Casale ATR-based blue ammonia process, all CO2 sent to sequestration or use |
| Energy consumption | 7.4-7.6 Gcal/MT LHV basis, including utilities and final CO2 compression at battery limits | Value as printed in the cited source; no further qualifier stated. |
| CO2 recovery | ?-99 % | Value as printed in the cited source; no further qualifier stated. |
| Best-suited capacity | 3500 MTD and above | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- ATR refractory/burner design details and oxygen-only ATR reference plants not tied to ammonia — Fetch Topsoe SynCOR ATR equipment page and Casale HyPURE-N brochure.
- ATR refractory/burner design details and oxygen-only ATR reference plants not tied to ammonia — Fetch Topsoe SynCOR ATR equipment page and Casale HyPURE-N brochure.

## separator

### Steam separators / dryers and steam headers (moisture carryover limits) (steam-separators-dryers)

Primary code: PWR: Power and renewables
Remove entrained water droplets from steam that traps cannot catch; protect turbines, control valves and heat-transfer equipment from erosion, water hammer and reduced heat transfer; provide dry steam at point of use (TLV; Spirax Sarco).
Vendors: Spirax Sarco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| entrainment onset velocity | 10 m/s | TLV: at flow velocities as low as 10 m/s, directional changes and pressure differentials can entrain bottom condensate |
| entrained droplet transport velocity | up to 30 m/s | TLV separator article |
| TLV cyclone separator efficiency | up to 98 % | vendor claim using all four separation principles (mechanical impediment, velocity, directional change, impingement) |
| steam dryness fraction definition | dryness = 100% - % entrained water by mass % | TLV basics; boilers do not generate 100% dry saturated steam without superheater |
| sodium in steam indicating mechanical carryover | <=2 ppb | Chemical Engineering steam purity limit; saturated-steam sampling used to check drum mechanical carryover / failed separators |
| steam velocity in superheated mains | up to 100 m/s | Spirax Sarco: possible with superheated steam if pressure drop acceptable, allowing smaller distribution pipelines |


Recorded gaps:

- Generic steam dryer moisture carryover limit (e.g. % by mass) for each boiler type — Locate turbine OEM (GE Vernova/Siemens) steam purity specification or ASME steam purity guidance and cite exact wetness limit with basis.
- Separator pressure drop and capacity curves — Fetch TLV Valve Calculator / product datasheets for cyclone separator models.

## service

### Chemical cleaning and passivation of new boilers (pre-commissioning) (boiler-chemical-cleaning-passivation)

Primary code: PWR: Power and renewables
Remove welding slag, iron oxides, grease and construction debris from a newly built boiler before start-up; then form a protective magnetite film (passivation) to minimise corrosion and pitting during commissioning and lay-up.
Vendors: Veolia Australia & New Zealand — Industrial Services, Veolia Water Technologies & Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Nyrstar Port Pirie new-boiler clean — degreasing temperature | 70 °C | Veolia ANZ case study: degreasing of a 140,000 L system |
| Nyrstar passivation conditions | ammonia + sodium nitrate at pH 9 and 60 °C pH / °C | Veolia ANZ case study, 'The benefits' section |
| Nyrstar clean duration / system volume / hours worked | 3 weeks / 140,000 L / 3,489 hours worked / 0 injuries weeks / L / hours / count | Veolia ANZ case study summary panel |
| Hydrochloric acid cleaning reaction with magnetite | Fe3O4 + 8HCl → FeCl2 + 2FeCl3 + 4H2O stoichiometric reaction | Veolia Water Handbook Ch.11; ferric chloride corrosive, can dissolve metallic copper leading to copper replating and galvanic pitting unless complexing agent added |
| Hydrazine/hydroquinone passivation reactions | N2H4 + 6Fe2O3 → 4Fe3O4 + 2H2O + N2; C6H4(OH)2 + 3Fe2O3 → 2Fe3O4 + C6H4O2 + H2O stoichiometric reactions | Veolia Water Handbook Ch.11, Metal Passivation section |
| Acid-cleaning failure modes | Inhibitor breakdown from overheating cleaning solution; excessive exposure; high cleaning-agent concentration; incomplete neutralisation before start-up qualitative | Veolia Water Handbook Ch.11, Acidic Corrosion section |
| Neutralisation pH before drain after chemical flush (hot-water systems) | 6.0 to 8.5 pH units | CEA BG04 §6.16 final full system flush |
| Chemical cleaning time saving claim | up to 90% reduced cleaning time; up to two days saved on large vessels vs steaming-out % / days | Veolia ANZ chemical cleaning service page (company claim) |
| System type | Coagulation and Flocculation Units; pH Neutralization Systems; Chemical Oxidation Systems; Precipitation and Complexation; Disinfection Systems; Integrated Dosing Skids n/a | Capabilities list printed verbatim on WOG Chemical Treatment Systems page |
| Control logic | flow-paced, pH-based and ORP-based n/a | Printed under 'Integrated Dosing Skids' |
| Compliance referenced | US EPA, EU REACH and other global regulatory standards n/a | Printed claim on page; no numeric limit printed |


Recorded gaps:

- Detailed chemical-cleaning procedure for gas-fired HRSGs (drum/pressure-part-specific) — Fetch an OEM HRSG commissioning/cleaning manual excerpt or Veolia technical paper on pre-operational cleaning of combined-cycle HRSGs
- Southeast Asian chemical-cleaning contractor/vendor for new boilers — Search for Veolia/Suez industrial cleaning services in Malaysia, Singapore and Indonesia and record service scope with URLs

## shift

### Shift conversion - HT/LT shift reactors and catalysts (ammonia-shift-conversion)

Primary code: PCH: Petrochemicals
Shift conversion - HT/LT shift reactors and catalysts
Vendors: Topsoe, Johnson Matthey (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Medium-temperature shift catalyst operating range | 190-330 deg C | Topsoe LK-813 / LK-819 catalyst descriptions (middle/bottom layer) |
| WGS reaction enthalpy | -41 kJ/mol CO | CO + H2O <=> CO2 + H2, mildly exothermic |
| Equilibrium constant K at 400 deg C (N2+3H2<=>2NH3 context table) | 16.4 x 10^-5 dimensionless | Haber-process equilibrium table; illustrates temperature constraint on synthesis, not shift |


Recorded gaps:

- HTS/LTS inlet-outlet CO concentrations, space velocity, catalyst life and reactor dimensions — Fetch individual catalyst leaflets and AIChE ammonia production material (AIChE CEP page returned 403).
- HTS/LTS inlet-outlet CO concentrations, space velocity, catalyst life and reactor dimensions — Fetch individual catalyst leaflets and AIChE ammonia production material (AIChE CEP page returned 403).

## silencer

### Silencers (fan inlet, stack/breeching, PRV/steam vent) (boiler-stack-vent-silencers)

Primary code: PWR: Power and renewables
Attenuate noise from fans/inlets, stack and breeching gas flow, and high-energy steam/gas vents through relief, safety, control or start-up valves; ensure acoustic compliance and personnel safety (Burgess-Manning; IMI; SVI BREMCO; dB Noise Reduction).
Vendors: Burgess-Manning (CECO Environmental), IMI Process Automation, SVI BREMCO, dB Noise Reduction (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| guaranteed vent silencer attenuation | up to 60 dBA | Burgess-Manning custom vent silencer claim (transformative + absorptive principles) |
| silencer design codes | ASME B31.1, B31.3, B31.8, ASME VIII Div 1, EN 13480, EN 13445 code list | Burgess-Manning custom vent silencer design codes |
| fan inlet silencer selection inputs | fan type; duct configuration; allowable pressure drop; required noise reduction qualitative design inputs | dB Noise Reduction fan inlet silencer page (read) |
| vent silencer service range | all kinds of flow rates, pressures and temperatures; no inlet/casing diameter limit qualitative | Burgess-Manning custom vent silencer page |


Recorded gaps:

- Site-specific insertion loss and pressure-drop curves for each silencer type — Request vendor selection sheets with flow, pressure, temperature and required sound level; record insertion loss by octave band and allowable dP.
- Fan inlet silencer design inputs for boiler forced-draft/induced-draft fans specifically — Find boiler OEM (B&W/GE Vernova) or silencer case study for FD/ID fan installations.

## silos

### Silos and storage bins (bulk-silos-storage-bins)

Primary code: PCH: Petrochemicals
Silos and storage bins
Vendors: Harvestore, Buffer Valley Industries (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| storage silo diameter | 3-27 m (10-90 ft) | Wikipedia Silo: storage silos cylindrical, typically 10-90 ft diameter |
| storage silo height | 10-90 m (30-275 ft) | Wikipedia Silo: 30-275 ft height; taller/wider ones slipform and jumpform concrete |
| mobile powder silo capacity | 100-750 tons | Wikipedia Silo, Cement storage silos section; fully mobile, with electronic weighing system |
| static upright powder silo capacity | 200-800 tons | Wikipedia Silo, Cement storage silos section |
| rigid silo size range | 2-1000 m3 (2 m3 to over 1000 m3) | Wikipedia Silo, Rigid silos section; may have multiple vertical partitions |
| flexible silo minimum particle size | 2 microns | Wikipedia Silo: flexible silos made from trevira tissue can handle particle size down to 2 microns and be pneumatically loaded without dust collector |
| silo hazards | dust explosion; grain entrapment; methane asphyxiation in enclosed stores n/a | Wikipedia Silo Safety sections |


Recorded gaps:

- Urea-specific silo capacity, caking/anti-caking measures, lining, aeration, reclaim system vendor — Fetch a bulk-solids silo OEM page (e.g. BEUMER, AUMUND, Cemen Tech) via verified URL.
- Urea-specific silo capacity, caking/anti-caking measures, lining, aeration, reclaim system vendor — Fetch a bulk-solids silo OEM page (e.g. BEUMER, AUMUND, Cemen Tech) via verified URL.

## sizing

### Sizing screens and crushers (bulk-sizing-screens-crushers)

Primary code: PCH: Petrochemicals
Sizing screens and crushers
Vendors: Toyo Engineering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| screen type | double-deck screen separates product size from over- and undersize granules n/a | Toyo granulation process outline |
| crusher type | double roller type crusher for oversize granules; crushed oversize recycled with undersize as seeds n/a | Toyo granulation process outline |
| product size fraction | 95 wt% in 2-4 mm | Toyo typical product quality |
| crusher setting optimization | proper settings of the crusher listed as an issue solved by UreaKnowHow FBG optimisation services n/a | UreaKnowHow Fluid Bed Granulation Optimization page |


Recorded gaps:

- Screen area, mesh apertures, crusher gap/capacity, crusher OEM — Fetch a screening/crushing OEM page with a known working URL.
- Screen area, mesh apertures, crusher gap/capacity, crusher OEM — Fetch a screening/crushing OEM page with a known working URL.

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

## starting

### Starting system: starting air/motors, batteries (gas-engine-starting-instrument-air)

Primary code: PWR: Power and renewables
Starting system: starting air/motors, batteries | Compressed air / instrument air and starting air
Vendors: Deep Sea Electronics, ComAp, Atlas Copco, Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| DC control supply | 8-35 V DC | Deep Sea DSE7320 MKII controller continuous supply range; cranking dropout survives 0 V for 100 ms if supply >=10 V before dropout and recovers to 5 V |
| Instrument air / starting air in plant architecture | Instrument Air and Starting Air Unit are listed as generator-unit auxiliaries; starting air unit and controller unit are engine-dedicated in the study plant qualitative | Schneider Electric White Paper 286, Figure 5 and accompanying text |


Recorded gaps:

- Starting-air compressor/receiver and starter-motor power for large gas engines — Fetch Wartsila/Everllence starting-system datasheets or EPC specification
- Battery capacity (Ah/CCA) for a named gas genset — Fetch a specific gas genset specification sheet

## steam-reformer

### Steam reformer (primary and secondary) (steam-reformer)

Primary code: H2: Hydrogen and low-carbon fuels
Fired tubular reactor in which natural gas or another light hydrocarbon reacts with steam over a nickel catalyst to make synthesis gas, followed in ammonia plants by a secondary reformer where air or oxygen is added and the remaining methane is converted. Reformers set the hydrogen-to-nitrogen ratio and the methane slip for the downstream shift and synthesis sections.
Vendors: Topsoe, KBR, thyssenkrupp Uhde, Wood, Casale (3 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| outlet temperature | 800-900 °C | optimal SMR operating range at medium pressure |
| operating pressure | 20-30 bar | medium-pressure SMR range |
| steam-to-carbon ratio | 2.5-3.0 mol/mol | typical S/C values; the NETL design case uses 2.60 |
| secondary reformer outlet temperature | 982 °C | syngas cooled from the secondary reformer outlet in the NETL design case |
| SMR optimal reactor temperature | 800-900 deg C | Optimal SMR reactor operating temperature range (Speight, The refinery of the future, cited on page) |
| SMR operating pressure | 20-30 bar | Optimal SMR medium-pressure range (same source) |
| SMR steam-to-carbon molar ratio | 2.5-3.0 mol/mol | Typical S/C ratio values (Steam reforming page) |
| SMR pressure, conventional plant practice (wide range) | 14-40 bar | Conventional steam reforming plants, 200-600 psi (Steam reforming page) |
| SMR outlet temperature, conventional plant practice | 815-925 deg C | Conventional steam reforming plants (Steam reforming page) |
| SMR reaction enthalpy | 206 kJ/mol CH4 | CH4 + H2O <=> CO + 3H2, standard steam reforming reaction enthalpy |
| Steam reforming thermal efficiency | 65-75 % | Steam reforming of natural gas efficiency (Steam reforming page, hydrogen fact sheet) |
| Two-step (Low Energy Ammonia) process capacity | ?-3500 MTPD ammonia | Topsoe Low Energy Ammonia Process, steam and air reforming, small and large scale up to 3500 MTPD |
| Tubular radiant-wall reformer arrangement | catalyst tubes in single line, one or two fired boxes, burners on walls at several elevations qualitative | Topsoe equipment description |
| NOx | 110 mg/Nm3 (standard scheme; lower possible with proper burner) | Value as printed in the cited source; no further qualifier stated. |
| Energy consumption, grey configuration | ?-6.5 Gcal/MT (basis as stated on page) | Value as printed in the cited source; no further qualifier stated. |
| Energy consumption, blue configuration | 7.9 Gcal/MT | Value as printed in the cited source; no further qualifier stated. |
| NOx | 110 mg/Nm3 standard scheme | Value as printed in the cited source; no further qualifier stated. |
| CO2 emissions | 0.1-0.15 t CO2/t NH3 | Value as printed in the cited source; no further qualifier stated. |
| Energy consumption | 7.9 Gcal/MT LHV basis | Value as printed in the cited source; no further qualifier stated. |

- **Topsoe** Tubular radiant wall steam reformer: more than 250 units designed over 50+ years; low steam-to-carbon, high heat flux, high outlet temperature
- **KBR** KRES (KBR Reforming Exchanger): installed in parallel with the existing SMR and secondary reformer; up to 130% of SMR capacity
- **thyssenkrupp Uhde** uhde primary reformer: catalyst tube outlet about 800 C at approximately 45 bar

Recorded gaps:

- tube wall temperature and tube-life limits — fetch an OEM reformer datasheet or a metallurgy reference that states tube skin temperature
- Tube dimensions, alloy specification, tube count, heat flux and burner ratings for named reformer designs — Fetch individual equipment product pages from Topsoe (e.g. tubular radiant wall steam reformer) and EPC design papers.
- Tube dimensions, alloy specification, tube count, heat flux and burner ratings for named reformer designs — Fetch individual equipment product pages from Topsoe (e.g. tubular radiant wall steam reformer) and EPC design papers.

## steam-trap

### Steam traps (thermodynamic, float, thermostatic, inverted bucket) (steam-traps-condensate-return)

Primary code: PWR: Power and renewables
Automatically discharge condensate, air and non-condensable gases from steam lines and heat-using equipment while holding back live steam; protects against waterlogging, water hammer, erosion and corrosion (Spirax Sarco; TLV).
Vendors: Spirax Sarco, Armstrong International (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| thermodynamic trap minimum inlet pressure | 0.25 bar g | typical minimum differential for disc-type operation; source: Spirax Sarco 'Thermodynamic Steam Traps' |
| thermodynamic trap maximum backpressure | 80 % of inlet pressure | Spirax Sarco design limit for TD traps |
| TD trap closed period | 20-40 s | typical cycling interval, depends on steam temperature and ambient conditions; Spirax Sarco |
| no-load steam loss, thermostatic / inverted-bucket / thermodynamic traps | up to ~0.5 kg/h | laboratory tests for 1/2-inch traps at low/no-load; Spirax Sarco energy-loss tutorial (thermostatic 'up to 0.5', inverted bucket 'around 0.5', TD 'generally around 0.5, doubled in severe weather, halved with insulating cap') |
| TD trap radiation loss | not more than 0.25 kg/h | independent tests, small TD trap; at least a quarter of equal-sized inverted bucket traps; Spirax Sarco |
| bimetallic trap cooling leg | 1-3 m | unlagged pipe needed to avoid waterlogging when trap discharges below saturation; Spirax Sarco |
| liquid-expansion trap discharge temperature setting | 60-100 °C | adjustable discharge range of oil-filled element; Spirax Sarco |
| balanced-pressure trap superheat tolerance | up to 70 °C of superheat | modern welded stainless capsule type; Spirax Sarco |
| steam mains drainage interval | 30-50 m | general rule with adequately sized drain pockets; also drain bottom of every riser; Spirax Sarco |
| free-float trap upper pressure application | up to 12 MPaG | certain TLV free-float models in high-pressure service |
| disc trap upper pressure application | up to 26 MPaG | certain TLV disc-type models; cited for supercritical steam/condensate service |
| Maximum operating pressure (PMO) | 230 psig | Printed in Product Details table |
| Minimum operating pressure | 0.03 psig | Printed in Product Details table |
| Maximum operating temperature (TMO) | 428 deg F | Printed in Product Details table |
| Discharge capacity | 1660 lb/h | Printed in Product Details table |
| Body material | Ductile Cast Iron (FCD450) n/a | Printed in Product Details table |
| Connection | Screwed n/a | Printed in Product Details table |
| Body design condition | PN63 n/a | Printed under 'Pressure, temperature and backpressure envelope' |
| Maximum allowable pressure | 63 bar g at 100 deg C | Printed under 'Pressure, temperature and backpressure envelope' |
| Maximum allowable / operating temperature | 400 deg C at 42 bar g | Printed under 'Pressure, temperature and backpressure envelope' |
| Recommended maximum operating pressure | 42 bar g | Printed under 'Pressure, temperature and backpressure envelope' and in pressure/temperature limits note |
| Minimum allowable / operating temperature | 0 deg C | Printed under 'Pressure, temperature and backpressure envelope'; consult manufacturer below this |
| Minimum operating differential pressure | 0.25 bar g | Printed under 'Pressure, temperature and backpressure envelope' |


Recorded gaps:

- Per-model trap capacity tables (kg/h vs differential pressure) and connection sizes — Fetch manufacturer selector tools (TLV Valve Calculator, Spirax datasheets) or request datasheets and record model-specific capacity with differential pressure basis.
- Trap failure-mode distribution by boiler type (fire-tube vs HRSG vs CFB) — Locate plant-specific steam trap survey reports or EPRI/DOE case studies broken out by boiler type.
- Monetised annual steam-trap loss with stated dollar year — Find a dated DOE/Armstrong publication and record dollar year and escalation basis.

## storage

### Battery energy storage / lithium-ion UPS / flywheels integrated with gensets for bridging and peak shaving (data-centre-bess-bridging)

Primary code: IDC: Data centres
Battery energy storage / lithium-ion UPS / flywheels integrated with gensets for bridging and peak shaving
Vendors: Active Power (Piller group), Vertiv, Fluence, Tesla Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Battery energy storage / lithium-ion UPS / flywheels integrated with gensets for bridging and peak shaving | Qualitative function from pages read in this sweep. |


Recorded gaps:

- No verified datasheet for a Tesla BESS product specifically configured for data-centre UPS bridging — Fetch Tesla Megapack product page and NERC Large Loads Task Force presentation directly
- Measured round-trip efficiency and degradation for Li-ion UPS vs flywheel in a hot, high-cycling AI load profile — Seek independent test or operator data

## sub-platform

### Articulated tower / articulated loading platform (sub-articulated-tower-articulated-loading-platform-rare)

Primary code: UPS: Upstream
Bottom-founded tower connected by a universal joint or articulated base, allowing the structure to rotate with environmental loads while supporting loading or wellhead facilities.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| concrete articulated loading column example | Maureen ALC, concrete base articulated loading column, 92 m water depth, North Sea UK, Phillips, 1982, later removed description | Wikipedia Offshore concrete structure major structures table, row 20 |
| Hutton TLP topsides redeployed to Prirazlomnoye | Hull and topsides separated; topsides redeployed to Prirazlomnoye field in Barents Sea (ice-resistant platform) description | Wikipedia Tension-leg platform |


### Artificial island / sea island (sub-artificial-island-sea-island-oil-and-gas)

Primary code: UPS: Upstream
Constructed landmass or caisson-supported island providing a land-like drilling and production site in shallow water.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| maximum feasible water depth | 75 m | Wikipedia Artificial Island: technological advancements make it feasible to build artificial islands in waters as deep as 75 m; wave size and structural integrity determine maximum depth |
| Ekofisk Tank sea-island form | C G Doris platform shaped like a marine sea island, surrounded by perforated breakwater wall (Jarlan patent); 71 m North Sea, 1973 description | Wikipedia Offshore concrete structure, C G DORIS type and table row 1 |
| legal status | Under UNCLOS not harbour works (Art 11); no own territorial sea/EEZ; only coastal state may authorise within 200 nm (Art 56, 60); on high seas any state may construct (Art 87) description | Wikipedia Artificial Island, Legal status |


### Barge-based platforms, pontoons and floaters (sub-barge-based-platforms-pontoons-and-floaters)

Primary code: UPS: Upstream
Shallow-draft buoyant hulls used as drilling/production/support bases; spud barges, swamp barges and deck barges can be moored or jack-up supported.
Vendors: Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| generic use | bottom-founded drilling rigs include jackup barges and swamp barges; MODUs include jackups, semi-submersibles, drillships and barges description | Wikipedia Oil platform intro; Wikipedia Offshore drilling |
| turbine rating, WindFloat Atlantic | 8.4 MW | Wikipedia Floating offshore wind operational table |


### Braced templates (sub-braced-templates-subsea-drilling-templates)

Primary code: UPS: Upstream
 seabed frame that positions and guides wells or manifold equipment; may be piled or suction-founded.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Snorre concrete foundation templates | 3 cells with suction anchors at 310 m water depth description | Wikipedia Offshore concrete structure, major structures table, row 33 (Saga, 1992) |


### Compliant tower (sub-compliant-tower)

Primary code: UPS: Upstream
Slender flexible bottom-founded tower with piled foundation and conventional deck, designed for significant lateral deflection in deep water.
Vendors: J. Ray McDermott, Aker Gulf Marine (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| typical water depth | 450-900 m | Wikipedia Compliant tower: typically 1,500-3,000 ft (450-900 m); Wikipedia Oil platform states 370-910 m |
| lateral deformation | up to 2.5% vs 0.5% for land-based structures % of height | Wikipedia Compliant tower |
| economic limit | 1000 m | Wikipedia Compliant tower: uneconomical beyond depths greater than 1,000 m; floating production more appropriate |
| Baldpate structural heights and masses | base 351 ft, 140×140 ft tapering to 90×90 ft, 8,700 t; tower 1,320 ft, 90×90 ft, 20,200 t; storm sway ~30 s period, up to 10 ft lateral description | Offshore Technology Baldpate project |
| Baldpate tubular sizes | legs up to 144 in diameter / 3.5 in-8 in wall (base); 128 in / 3.3 in-4 in (tower) in | Offshore Technology Baldpate |
| Petronius deepest compliant tower | 623 m | Wikipedia Compliant tower: deepest is Chevron Petronius in 623 m; platform 640 m to flare tip; topsides 7,500 t |
| Benguela Belize BBLT base tower launch | base tower first 250 m of >400 m tower; launched from barge H-851 on 15 April 2005; heaviest compliant tower installed; first outside GoM description | Wikipedia Compliant tower |


### Concrete gravity base structure (sub-concrete-gravity-base-structure-gbs-cgs-caisson)

Primary code: UPS: Upstream
Large reinforced/prestressed concrete caisson that resists overturning and sliding by self-weight; often provides oil storage and flotation during tow-out.
Vendors: Norwegian Contractors, Arup, DORIS / C G DORIS (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| number of major concrete offshore structures built | 47 structures | Wikipedia Offshore concrete structure: at least 47 major concrete offshore structures built since first North Sea installation in 1973 |
| economic water depth | 150 m+ | Wikipedia Offshore concrete structure: concrete gravity platforms economical for water depths larger than 150 m; most need no additional fixing due to large foundation and weight |
| Troll A total height | 472 m | Wikipedia Condeep: tallest Condeep, total height 472 m, deployed 1995, placed at 300 m depth and dug 35 m into seabed |
| Gullfaks C total height | 380 m | Wikipedia Condeep: Gullfaks C rests 217 m below sea surface, total height 380 m, displacement 1.4-1.5 million t |


### Drillship (sub-drillship)

Primary code: UPS: Upstream
Ship-shaped self-propelled drilling vessel with moonpool, derrick and dynamic positioning; used for exploratory and development drilling in deep/ultra-deep water.
Vendors: Transocean (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| maximum drilling water depth | 3700 m | Wikipedia Oil platform, Drillships: can drill in water depths up to 3,700 m (12,100 ft) |
| MODU operational limit | 3000 m | Wikipedia Offshore drilling: deepwater MODUs capable of operating in water depths up to 3,000 m; >1,500 m uses dynamic positioning |
| water-depth capability by vintage | CUSS I 350 ft (1961); Discoverer 534 7,000 ft (1975); Enterprise 10,000 ft (1999); Inspiration 12,000 ft (2009) ft | Wikipedia Drillship, Design table |
| relocation time GoM to Angola | 20 days drillship vs 70 days towed semi-submersible days | Wikipedia Drillship, Design section citing Leffler et al. |
| depth record, Dhirubhai Deepwater KG1 | 3107 m | Wikipedia Drillship: 2011 world water-depth record 10,194 ft, working for Reliance, India |
| Chikyū scientific drilling depth | 7.0 km below seabed | Wikipedia Drillship: research vessel can drill to 7.0 km below seabed, 2-4 times any other drillship |


### Driven pile and skirt-pile foundations (sub-driven-pile-and-skirt-pile-foundations)

Primary code: UPS: Upstream
Transfer jacket/tower loads into soil by axial and lateral resistance; skirt piles are driven through sleeves at jacket base corners.
Vendors: Sif Group, Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| skirt-pile sleeves, Baldpate | 12 sleeves | Offshore Technology Baldpate: three 84 in-diameter, 530 ft skirt-pile sleeves at each of four bottom corners; 12 foundation piles installed by Heerema; penetrations approaching 430 ft |
| pile mass and length, Mexilhão | 3150 t | Offshore Technology Mexilhão: 3,150 t tubular steel piles up to 120 m long |


### Fixed steel jacket platform (sub-fixed-steel-jacket-platform-conventional-4-leg-6-leg-8-leg)

Primary code: UPS: Upstream
Bottom-founded tubular steel lattice that transfers deck, drilling and environmental loads to the seabed, normally via driven piles through the jacket legs.
Vendors: Aker Solutions, Saipem (ex-Micoperi 7000), Sif Group, Heerema Marine Contractors (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| typical economic water depth limit | 150 m | Wikipedia Fixed platform: fixed platforms economically feasible to about 500 ft (150 m); deeper usually floating or subsea tieback |
| quoted general water depth feasibility | 520 m | Wikipedia Oil platform, Fixed platforms section: economically feasible up to about 520 m (1,710 ft) |
| jacket mass, Gudrun platform | 7400 t | Offshore Technology project profile: fixed processing platform supported by 7,400 t steel jacket; water depth 361 ft; 16 well slots |
| jacket height / mass, Mexilhão PMXL-1 | 180 m | Offshore Technology: 180 m tall tubular jacket ~10,500 t; topsides 12,000 t; platform water depth 172 m; piles 3,150 t up to 120 m long |
| water depth | 180-1300 m | Wikipedia Oil platform |
| Iron Lady deck | SPMT-equipped deck with ballast system (no capacity figure printed) description | Value as printed in the cited source; no further qualifier stated. |
| Load-out capability | >20,000 t | Value as printed in the cited source; no further qualifier stated. |
| Load relief | sand release valve lowers plunger assembly mechanism | Value as printed in the cited source; no further qualifier stated. |
| Tandem lift (guyed mode) | 6300 t | Value as printed in the cited source; no further qualifier stated. |
| Lifting capacity | 5000 t | Value as printed in the cited source; no further qualifier stated. |
| Qingdao annual production | 300000 tons/yr | single onshore unit 50,000 t; floating unit 300,000 t; up to 15,000 t onshore transport |
| Qingdao slideways | five, 4,000-50,000 t bearing capacity capacity | plus two 800 t and one 600 t gantry cranes |
| Zhuhai annual production | 250000 tons/yr | deepwater floating structures, semi-submersibles, TLPs, spars, FLNG/FPSO topsides |
| Zhuhai slideway 1 | 35000 T | slideway 3 is 12,000 T |
| Ranking | world's largest barge (Heerema claim) description | Value as printed in the cited source; no further qualifier stated. |
| Energy range | 320-3,500 kJ | Value as printed in the cited source; no further qualifier stated. |


### FLNG (sub-flng-floating-liquefied-natural-gas-facility)

Primary code: UPS: Upstream
Floating facility that extracts, processes, liquefies, stores and offloads LNG at sea, removing the need for a pipeline to shore.
Vendors: Shell, Technip Samsung Consortium, SBM Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Petronas Kanowit FLNG contract | Technip/DSME consortium EPCI contract awarded June 2012 description | Wikipedia FPSO History section |


### Floating concrete structures (sub-floating-concrete-structures-concrete-semisub-concrete-tlp-con)

Primary code: UPS: Upstream
Concrete hulls used where corrosion resistance, low maintenance and heavy topside capacity are valuable.
Vendors: DORIS (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| only concrete semi-submersible | Troll B platform | Wikipedia Offshore concrete structure: 'The only concrete semi-submersible in existence is Troll B'; table lists Troll B, 325 m depth, 1995 |
| only concrete TLP hull | Heidrun TLP platform | Wikipedia Offshore concrete structure: Statoil's Heidrun TLP is the only one with a concrete hull; table lists 350 m depth, 1994/1995 |
| first prestressed concrete barge | Ardjuna Field LPG barge, Indonesia, 43 m, 1974 description | Wikipedia Offshore concrete structure: major structures table row 2 and Floating structures/Barge-Ship Design section |
| concrete LNG terminal | Adriatic LNG terminal, 29 m, 2008 description | Wikipedia Offshore concrete structure table row 49 |


### Floating power / desalination units and power service vessels (sub-floating-power-desalination-units-and-power-service-vessels)

Primary code: UPS: Upstream
Floating hulls carrying power plants or desalination plants to supply offshore assets or shore grids without fixed infrastructure.
Vendors: American Bureau of Shipping, DNV (Installjac software) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Floating hulls carrying power plants or desalination plants to supply offshore assets or shore grids without fixed infrastructure. | Qualitative function from pages read in this sweep. |


### Floating wind turbine floaters (sub-floating-wind-turbine-floaters-spar-semi-submersible-tlp-barge)

Primary code: UPS: Upstream
Buoyant substructures that support wind turbines in water depths where fixed foundations are uneconomic, moored by catenary, taut or tension-leg systems.
Vendors: Equinor, Principle Power, SBM Offshore / IFPEN (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| operational floating wind capacity | 245 MW operational, 266 GW pipeline as of October 2024 MW / GW | Wikipedia Floating offshore wind intro |
| Hywind Scotland | 5 × 6 MW Siemens turbines, 30 MW, commissioned 2017, 54% capacity factor first 5 years description | Wikipedia Floating offshore wind, Operational table |
| WindFloat Atlantic | 3 × Vestas 8.4 MW, 25 MW, semi-submersible, 100 m water depth, 20 km offshore, 34% capacity factor description | Wikipedia Floating offshore wind, Operational table |
| catenary mooring radius | turbine-to-anchor radius approximately 6-8 × water depth ratio | Wikipedia Floating offshore wind, Mooring systems |
| floater concept count | over 100 concepts counted in a 2026 study concepts | Wikipedia Floating offshore wind intro |


### FPSO / FSO / FSU / FDPSO / FSRU (sub-fpso-fso-fsu-fdpso-fsru)

Primary code: UPS: Upstream
Ship-shaped or circular floating vessel that receives, processes and stores hydrocarbons from subsea wells or nearby platforms and offloads to shuttle tankers; FSO/FSU store only.
Vendors: SBM Offshore, MODEC Inc., BW Offshore, Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| global fleet count | over 270 vessels deployed worldwide as oil FPSOs vessels | Wikipedia FPSO, History section |
| deepest FPSO, BW Pioneer | 2600 m | Wikipedia FPSO Record vessels: moored at 2,600 m, Walker Ridge 249, GoM; rated 80,000 bbl/d; conversion at MMHE Pasir Gudang, Malaysia; disconnectable APL turret |
| Kizomba A storage / dimensions | 2.2 million bbl; 285 m L × 63 m B × 32 m H; 81,000 t; cost over US$800m description | Wikipedia FPSO Record vessels |
| Skarv FPSO dimensions | 292 m × 50.6 m × 29 m; ~100 people; hull Aker Solutions Tentech975 description | Wikipedia FPSO Record vessels |


### Guyed tower (sub-guyed-tower-rare)

Primary code: UPS: Upstream
Compliant tower stabilised by inclined guy lines and anchors rather than relying solely on pile fixity; reduces base moment in deep water.
Vendors: Brown & Root (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| first tower | Exxon's Lena oil platform, early 1980s description | Wikipedia Compliant tower |


### Ice-resistant / Arctic caisson and artificial drilling island (sub-ice-resistant-arctic-caisson-and-artificial-drilling-island)

Primary code: UPS: Upstream
Bottom-founded structure or constructed island designed to resist iceberg impact, sea ice and ice scour in Arctic and sub-Arctic waters.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Tarsiut Island | 4 hollow caissons, 16 m water depth, Beaufort Sea, Amoco Canada, 1981, removed description | Wikipedia Offshore concrete structure table row 19 |
| Super CIDS | CGS caisson island, 16 m, Beaufort Sea, Global Marine, 1984, removed description | Wikipedia Offshore concrete structure table row 24 |
| Northstar Island | artificial island used for oil drilling in the Beaufort Sea north of Alaska description | Wikipedia Artificial Island gallery and Wikipedia Offshore drilling main fields |
| iceberg scour protection | subsea wells set in glory holes; seabed burial used as protection against drifting ice gouging description | Wikipedia Offshore drilling (Terra Nova subsea layout and challenges) |


### Jack-up rig / self-elevating unit (sub-jack-up-rig-self-elevating-unit-independent-leg-and-mat-suppor)

Primary code: UPS: Upstream
Mobile buoyant hull with movable legs jacked to the seabed; hull raised above waves for drilling, workover, production or wind-turbine service.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| typical water depth | 120 m | Wikipedia Jackup rig: typically used in water depths up to 120 m (390 ft), some designs to 170 m |
| premium/ultra-premium water depth | 150-190 m | Wikipedia Jackup rig: premium/ultra-premium jackups 150-190 m (490-620 ft) |
| tallest jackup leg length, Noble Lloyd Noble | 214 m | Wikipedia Jackup rig: completed 2016, legs 214 m (702 ft) tall |
| world jackup fleet | about 540 jackup drilling rigs in operation at end 2013 rigs | Wikipedia Jackup rig |
| leg configurations | 3 or 4 legs typical; also 6 and 8 movable legs description | Wikipedia Jackup rig, Name section |
| preloading | hull weight + ballast water drive legs into seabed before jacking hull to air gap; rack-and-pinion jacking driven by hydraulic/electric motors description | Wikipedia Jackup rig, Process of operation |


### Minimal / minimum-facility jacket and wellhead platform (sub-minimal-minimum-facility-jacket-and-wellhead-platform-nui-toad)

Primary code: UPS: Upstream
Small unmanned well bay and process/wellhead structure tied back by flowline or umbilical to a host platform.
Vendors: Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| configuration | well bay + helipad + emergency shelter; operated remotely, occasional visits description | Wikipedia Oil platform, Normally unmanned installations section |
| configuration (conductor support) | well bay + small process plant; linked to static production platform by flow lines and/or umbilical description | Wikipedia Oil platform, Conductor support systems section |


### Mobile offshore production unit (sub-mobile-offshore-production-unit-mopu)

Primary code: UPS: Upstream
Reusable mobile production facility (converted jack-up, liftboat, semi-submersible or barge) with wellbay, processing and accommodation, used for phased/early production.
Vendors: Aquaterra Energy, Noble Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Reusable mobile production facility (converted jack-up, liftboat, semi-submersible or barge) with wellbay, processing and accommodation, used for phased/early production. | Qualitative function from pages read in this sweep. |


### Monopod / tripod / tripile bottom-founded structures (sub-monopod-tripod-tripile-bottom-founded-structures)

Primary code: UPS: Upstream
Single-leg (monopod) or three-leg (tripod/tripile) bottom-founded substructure supporting a small deck or a wind turbine.
Vendors: Sif Group (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| concrete monotower example (Draugen) | 251 m water depth | Wikipedia Condeep platforms table: Draugen Condeep Monotower, Shell, 1993, 251 m |


### Mudmats and jacket base templates (sub-mudmats-and-jacket-base-templates)

Primary code: UPS: Upstream
Distribute jacket base load over weak seabed during installation and before piling; templates guide piles and drill slots.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Distribute jacket base load over weak seabed during installation and before piling; templates guide piles and drill slots. | Qualitative function from pages read in this sweep. |


### Semi-submersible platform (sub-semi-submersible-platform-production-and-modu)

Primary code: UPS: Upstream
Floating hull with submerged pontoons and columns supporting a deck; ballastable, moored or dynamically positioned; used for drilling, production, crane work and accommodation.
Vendors: Heerema Marine Contractors, Saipem (ex-Micoperi 7000), Petrobras (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| water depth range | 60-6000 m | Wikipedia Oil platform, Semi-submersible platform: can be used in water depths from 60 to 6,000 m (200 to 20,000 ft) |
| transition from fixed structures | 520 m | Wikipedia Semi-submersible platform: drilling in water depth greater than around 520 m requires a floating vessel since fixed structures are not practical |
| nominal generations | 1st ~200 m (early 1960s); 2nd ~300 m (1969-74); 3rd ~500 m (early 1980s); 4th ~1,000 m (1990s); 5th ~2,500 m (1998-2004); 6th ~3,000 m (2005-2010) classification | Wikipedia Semi-submersible platform, Classification table |
| heaviest SSCV lift capacity | Thialf 14,200 t; Saipem 7000 14,000 t t | Wikipedia Semi-submersible platform, SSCV section |
| largest production semi-submersible | Thunder Horse PDQ (GVA40000 design) platform | Wikipedia Semi-submersible platform, Offshore production platforms section |


### Spar platform (sub-spar-platform-classic-truss-cell)

Primary code: UPS: Upstream
Deep-draft vertical buoyant cylinder(s) moored by spread mooring; deep draft gives low wave sensitivity and supports dry-tree or subsea production.
Vendors: Technip (now TechnipFMC), J. Ray McDermott (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| cell spar cell count and diameter, Red Hawk | 7 cells of 8 m diameter cells | Wikipedia Spar (platform): '7 ea. 8 m (26 ft) diameter cells'; first and only cell spar, 1,615 m water depth, 2004 |
| deepest spar water depth, Perdido | 2383 m | Wikipedia Spar (platform): deepest seabed to which a spar moored is 2,383 m; mean water depth 2,438 m; truss spar, Shell, 2010 |
| first production spar water depth, Neptune | 588 m | Wikipedia Spar (platform) list: Neptune, Classic, 1996, Oryx Energy, 588 m, designed by Technip |


### Submersible drilling rig (sub-submersible-drilling-rig-shallow-water-bottom-founded-barge)

Primary code: UPS: Upstream
Floodable barge that rests on the seabed for drilling in very shallow water, often in marsh/swamp or inland waters.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| classification | listed as one of the MODU types alongside jackup, semi-submersible and drillship description | Wikipedia Offshore drilling, Drilling platforms section; Wikipedia Drillship types list |
| first mobile steel barges | developed by The Texas Company (Texaco) in early 1930s for brackish coastal Gulf areas description | Wikipedia Offshore drilling history |


### Subsea-to-surface / subsea completion tie-back to host facility (sub-subsea-to-surface-subsea-completion-tie-back-to-host-facility)

Primary code: UPS: Upstream
Subsea wells and manifolds tied back by flowlines and umbilicals to a surface host (fixed platform, FPSO, spar), avoiding a dedicated platform at the well location.
Vendors: TechnipFMC (CDS Separation Systems), Saipem (ex-Micoperi 7000), Subsea7 (Swagelining all-polymer liner) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| system classification | subsea production control system; subsea structures and manifold system; subsea intervention system; subsea umbilical system; subsea processing system classification | Wikipedia Subsea production system citing NORSOK U-001 |
| deepest tieback example | Shell's Coulomb tie to NaKika, 2,307 m (7,570 ft), 2004 m | Wikipedia Oil platform, Types of offshore oil and gas structures caption (2005 data) |


### Suction bucket / suction caisson jacket foundations (sub-suction-bucket-suction-caisson-jacket-foundations)

Primary code: UPS: Upstream
Open-bottomed inverted-bucket foundation embedded by pumping water out (negative pressure); resists lateral and axial loads and is removable by reverse pumping.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| historical installation count | 485 caissons | Wikipedia Suction caisson: statistics from 2002 showed 485 suction caissons installed in more than 50 localities, in depths to about 2,000 m |
| Diana suction caisson dimensions | 30 m height | Wikipedia Suction caisson: 12 caissons at Gorm (1981, 40 m depth); Diana caissons 30 m high, 6.5 m diameter, installed ~1,500 m on soft clay (1999) |
| Diana suction caisson diameter | 6.5 m | Same Wikipedia Suction caisson passage |
| Snorre A suction anchor length vs conventional pile | 12 m | Wikipedia Suction caisson: analysis showed safe fixity with 12 m suction caissons vs up to 90 m piles where pebbles at 60 m depth prevented piling; production started 1992 |
| Troll A concrete skirt length | 30 m | Wikipedia Suction caisson, Gravity oil platforms: Troll A founded in 330 m depth with 30 m long skirts; Gullfaks C 22 m skirts |


### Tension leg platform (sub-tension-leg-platform-tlp-extended-tlp-mini-tlp)

Primary code: UPS: Upstream
Vertically moored buoyant platform with high-axial-stiffness tendons that eliminate nearly all vertical motion, permitting deck-mounted dry-tree wellheads and rigid risers.
Vendors: Technip / TechnipFMC, Heerema Marine Contractors (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| preferred water depth range | 300-1500 m | Wikipedia Tension-leg platform: particularly suited to water depths greater than 300 m and less than 1,500 m; proposed for offshore wind |
| upper general water depth | 2000 m | Wikipedia Oil platform: TLPs used in water depths up to about 2,000 m |
| mini-TLP water depth | 180-1300 m | Wikipedia Oil platform: Seastar and MOSES mini TLPs used in 180-1,300 m; utility/satellite/early production roles |
| Hutton TLP tendon count / mass | 16 tension legs; 46,500-55,000 t moored; up to 61,580 t free-floating description | Wikipedia Tension-leg platform: first TLP, Conoco Hutton field, hull built at Nigg, deck at Ardersier, mated 1984; designed for 25 years in 100-1,000 m North Sea |
| deepest ETLP, Big Foot | 1580 m | Wikipedia Tension-leg platform list of deepest (E)TLPs: Big Foot 5,185 ft (1,580 m) |


### Tension-leg wellhead platform (sub-tension-leg-wellhead-platform-mini-tlp-tlwp)

Primary code: UPS: Upstream
Small vertically moored wellhead or utility platform for satellite/early production, using tensioned tendons to support dry trees at lower cost than a full TLP.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| water depth | 180-1300 m | Wikipedia Oil platform: proprietary Seastar and MOSES mini TLPs used in water depths 180-1,300 m, low cost, utility/satellite/early production |


### Wellhead caisson / conductor-guided single-well structure (sub-wellhead-caisson-conductor-guided-single-well-structure)

Primary code: UPS: Upstream
Single- or few-well structure in which the conductor(s) provide primary lateral support for a small wellhead deck.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| structural concept | small unmanned platform with well bay and small process plant, connected to a static production platform by flowlines/umbilical description | Wikipedia Oil platform, Conductor support systems |
| Diana caisson | 30 m high × 6.5 m diameter m | Wikipedia Suction caisson |


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

### Generator circuit breaker, LV/MV switchgear, bus ducts, ATS / CTTS (gas-engine-switchgear-ats)

Primary code: PWR: Power and renewables
Generator circuit breaker, LV/MV switchgear, bus ducts, ATS / CTTS
Vendors: ABB, Eaton, ComAp, Cummins (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Generator circuit breaker, LV/MV switchgear, bus ducts, ATS / CTTS | Qualitative function from pages read in this sweep. |


Recorded gaps:

- All switchgear/GCB/ATS figures independently fetched — Use PDF-layout reader or terminal download, then re-record with page_read:true
- Bus duct / busway manufacturer and ampacity range — Fetch ABB/Schneider/Eaton busway data-centre pages
- Medium-voltage generator neutral grounding and earthing arrangements — Fetch project single-line diagrams or OEM switchgear guides

## testing

### Load banks, commissioning and testing equipment for gensets (data-centre-load-bank)

Primary code: IDC: Data centres
Load banks, commissioning and testing equipment for gensets
Vendors: Avtron Power Solutions, Trystar, Buckeye Power Sales (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Load banks, commissioning and testing equipment for gensets | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Primary NFPA 110 standard text and exact clause numbers for load-bank test profiles — Consult NFPA LiNK or adopted edition via AHJ before specifying acceptance criteria
- Load bank requirements specific to gas-engine (spark-ignition) prime plants running continuously rather than standby — Check engine OEM (INNIO/Wärtsilä) commissioning manuals for gas engine run-in procedures

## top-platform

### Accommodation / living quarters topsides (top-accommodation-living-quarters-topsides)

Primary code: UPS: Upstream
Provides habitability for the offshore workforce, with helideck access nearby and maximum segregation from hazardous process equipment, flare and high-noise sources.
Vendors: Leirvik AS, KBR / Kvaerner JV (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Miller living quarter | five levels, 98 cabins, 196 beds n/a | independent module with integrated bathroom facilities |
| Olympus TLP accommodation | 192 crew members | up to 192 crew housed; 342,000 ft2 deck space |
| Kizomba A living quarters design | 100 pax | platform design includes 100-man living quarters |


### Flare platform topsides and flare booms/stacks (top-flare-platform-topsides-and-flare-booms-stacks)

Primary code: UPS: Upstream
Vent and flare structures discharge and burn gaseous products; placed outside hazardous areas and away from the helideck, with tip elevation above the helideck and heat radiation checked.
Vendors: Worley (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| flare tip elevation above helideck | 100 ft minimum | vent and flare tip shall exceed helideck elevation by at least 100 ft; heat radiation to be checked |


### FLNG topsides and turrets (top-flng-topsides-and-turrets)

Primary code: UPS: Upstream
Floating LNG facility topsides consolidate gas pretreatment, liquefaction, fractionation, utilities, accommodation, flare and offtake on a ship-shaped hull; turret mooring enables weathervaning and fluid/power transfer.
Vendors: Babcock International, CNOOC Research Institute (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| South China Sea FLNG side-by-side layout | bow-to-stern: single point - flare - pretreatment - liquefaction - offloading - power/utility - living quarter layout sequence | CNOOC Research Institute recommended layout; used by Prelude in benign environments |
| South China Sea FLNG tandem layout | bow-to-stern: living quarter - offloading - single point - power/utility - pretreatment - flare - liquefaction - tandem offloading layout sequence | recommended for harsh environments / small FLNG in South China Sea |
| FLNG side-by-side offloading sea state limit | 2.5 m Hs | side-by-side offloading requires Hs <2.5 m |
| FLNG tandem offloading sea state limit | 5.5 m Hs | tandem offloading can operate at Hs <5.5 m |


### Float-over topsides (top-float-over-topsides)

Primary code: UPS: Upstream
Fully integrated and pre-commissioned deck transported on a barge, floated over the substructure and lowered by ballasting or quick-drop mechanisms (or by deballasting a floating substructure). Avoids heavy-lift crane capacity limits.
Vendors: COOEC (CNOOC Engineering) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| AMP1 floatover installation vessel | Dockwise Mighty Servant 3 vessel | 11,970 t integrated topsides installed by floatover |
| floatover jacket load path | four legs instead of eight legs | jacket designed for floatover transfer of topsides weight directly to four leg rows with added bracing |


### FPSO topsides and turrets (top-fpso-topsides-and-turrets)

Primary code: UPS: Upstream
Ship-shaped floating production topsides with process, utility, accommodation and offloading systems; turret mooring allows weathervaning and transfers fluids/power between subsea and topsides through a swivel.
Vendors: SOFEC, SBM Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| FPSO topsides weight vs oil capacity regression (all sample) | {'intercept': 113.9, 'slope': 104.7} TW tonnes; OIL thousand bbl/d (Mbd) | TW = 113.9 + 104.7 OIL, R2=0.55, sample of 50 FPSOs |
| FPSO topsides weight vs oil capacity (zero intercept) | 114.5 t per Mbd | TW = 114.5 OIL, R2=0.85 |
| FPSO topsides weight (gas fields removed) | {'intercept': -5506, 'slope': 145.7} TW tonnes; OIL Mbd | TW = -5506 + 145.7 OIL, R2=0.74 |
| FPSO topsides weight vs oil+water capacity | 45.1 t per Mbd liquids | TW = 45.1 LIQUIDS, R2=0.81; oil capacity alone is better descriptor |
| FPSO topsides weight vs BOE capacity | 36.7 t per Mboe/d | TW = 36.7 BOE, R2=0.84 |
| FPSO sample topsides weight distribution | about 20% <5,000 t; about 10% >35,000 t tonnes | sample of 50 FPSOs from OTC and trade publications |
| FPSO topsides weight as share of deadweight | 7.4 % average (SD 4.5%) | sample of 50 FPSOs; about half between 5-10%, ~20% between 10-15% |
| FPSO conversion multi-deck vs single-deck fixed weight difference | 10294 t | DRL Engineering inferred relations: TW(m)=13,824+23.5 BOE vs TW(s)=3,530+23.5 BOE |
| module support: pin vs sliding stool | one pinned stool per module longitudinal frame, other stools sliding n/a | sliding stools reduce hull hogging/sagging stress; one pin allows rotation but restricts translation |


### Hybrid / semi-integrated topsides (top-hybrid-semi-integrated-topsides)

Primary code: UPS: Upstream
Mixed concept where most equipment is integrated into a single lifted structure and smaller modules are added afterwards, balancing crane capacity, weight and offshore HUC cost.
Vendors: Technip-Coflexip (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| semi-integrated option rationale | lift semi-integrated topsides then install additional smaller modules on top n/a | described as more cost-effective than fully modularised installation when crane capacity is limiting |
| Perdido living quarter installed after topsides | 3 days after topsides lift | single-lift topsides 9 March 2009? topsides lift completed 13 March, living quarters added three days later |


### Integrated (top-integrated-single-lift-topsides)

Primary code: UPS: Upstream
All equipment is arranged, hooked up and commissioned onshore on one integrated deck, minimising offshore hook-up and commissioning (HUC). Single-lift topsides are integrated topsides designed specifically to reduce total weight so the whole unit can be installed by one crane lift.
Vendors: KBR, Aibel (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| integrated topsides concept first introduced | 1973 year | North Sea gravity-based structure project |
| original integrated GBS deck girder depth | 7-10 m | girder-type plate deck mounted on concrete towers capable of housing machinery and equipment |
| Amenam/Kpono AMP1 integrated topsides weight | 11970 tons | three decks (weather, main, cellar) plus mezzanine; floatover installation by Dockwise Mighty Servant 3 |
| systems installed, connected and commissioned at yard on AMP1 | 130 systems | Elf Petroleum Nigeria project |
| Shearwater single-lift record (2000) | 11883 tons | Shell topsides lifted by Thialf; world record at the time |
| Sabratha single-lift record | 12150 tons | lifted by Saipem 7000; record cited as still standing in source |
| Thialf nominal lifting capacity | 14200 t | SSCV nominal capacity |
| Saipem 7000 nominal lifting capacity | 14000 t | SSCV nominal capacity |
| structural steel share of total topsides weight | 50 % (approximately) | cited estimate ('some estimation says approximately half') |
| commissioning effort for five modules of a BP project | 25000 person-hours | example of offshore HUC effort cited in book chapter |
| single-lift offshore HUC schedule saving | 3-4 months | same published articles |


### Integrated deck with drilling rig (top-integrated-deck-with-drilling-rig)

Primary code: UPS: Upstream
A topsides concept combining drilling and production facilities on one structure, either as a fully integrated deck with a permanent/skiddable rig module or as a lightweight single-lift deck with a rig added later.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| TLP full drilling package typical weight | 4000-6000 tons | multiwell deepwater TLP |
| TLP drilling riser tension load examples | Snorre ~450 t (22-in riser); Heidrun ~950 t (26-in riser) tons | tentative figures in 1992 OGJ article |
| Snorre TLP BOP stack movement allowance | 3.0 m vertical | 16 3/4-in 5,000 psi BOP stack of 40 tons; BOP envelope total height ~7.5 m |
| TLP horizontal acceleration design | Snorre ~0.18 g; Heidrun ~0.12 g g | affects tubular handling and structural design |
| Hutton TLP drilling module share | large share of 20,000 Te topsides n/a | Hutton had a full drilling package on an integrated deck |


### Large topsides: central processing / integrated production-utility-accommodation platforms (top-large-topsides-central-processing-integrated-production-utilit)

Primary code: UPS: Upstream
Large multi-module topsides carrying separation, gas processing, water handling, utilities, power and living quarters, often with drilling and riser systems. Weight and dimensions are driven primarily by platform function.
Vendors: Aker Solutions, Fluor / COOEC-Fluor (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Johan Sverdrup P2 topsides weight | 24000 t (rounded) | Aibel's largest designed/built topside; three modules, flare tower and bridge, weighed by load cells and displacement |
| Johan Sverdrup drilling platform (DP) topsides weight | 22000 t (rounded) | Aibel project 2018 |
| Kvitebjørn topsides weight | 14400 t (rounded) | Aibel project 2003 |
| Gudrun topsides weight | 10500 t (rounded) | Aibel project 2014 |
| Dolwin Beta offshore HVDC platform topsides | 22000 t (rounded) | Aibel project 2015 - non-O&G comparator |


### Large topsides: riser, compression, pump, gas processing/reinjection, separation and water-injection platforms (top-large-topsides-riser-compression-pump-gas-processing-reinjecti)

Primary code: UPS: Upstream
Function-specific large topsides that host risers and manifolds, gas compression for export or reinjection, produced-water separation and injection, and power/utility support, often tied back to a central hub.
Vendors: Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| gas compression need driver | reservoir pressure declines with production n/a | future compression may be needed for acceptable export pipeline flow |
| water/gas injection need driver | oil production declines after some years n/a | reservoir requires stimulation by injection of water |


### Modular multi-module topsides (top-modular-multi-module-topsides)

Primary code: UPS: Upstream
Several modules are fabricated onshore, transported offshore and installed onto a module support frame (MSF) mounted on the substructure; hook-up and commissioning then occurs offshore. Modularisation enables parallel work, accommodates the gap between total topsides weight and available crane capacity, and allows module replacement during field life.
Vendors: Lamprell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Miller topsides module count | 12 modules | BP North Sea platform |
| Petronius topsides total weight | 7500 tons | Chevron compliant tower; two installable modules (North and South) |
| Petronius North Module weight | 4000 tons (close to) | half of the whole topsides, multi-deck |
| module-to-module clearance | 1000 mm | generally accepted spacing between FPSO modules; can be reduced to 600 mm between module and rack |
| module-to-rack clearance (minimum) | 600 mm | reduced spacing between module and pipe rack |
| accommodation safe zone gap | 20 m | 20 m gap or safe zone between accommodations and all process/utility modules on FPSO |
| hull deck to module underside air gap | 3 m minimum | free zone between hull, marine and topsides systems |
| module length design ratio | ship length / 10 ratio | maximum length between outer module supports for FPSO modular sections |


### Module Support Frame (top-module-support-frame-msf-and-deck-structures)

Primary code: UPS: Upstream
A space frame that supports modules and transfers their loads to the jacket/tower substructure; may also house storage tanks, pig launchers/receivers, metering devices and piping. Provides the structural skeleton for integrated or modular decks.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| truss vs portal frame longitudinal rows | 2-3 rows | 20-25 m wide deck: trusses at centreline and both outer walls; portal frames in 2 rows ~14-16 m apart |
| portal frame row spacing | 14-16 m | allowing floor cantilevers of approximately 5 m |
| conventional steel floor share of deck steel weight | 50 % (approximately) | conventional steel floor contributes about half the steel structure weight of an offshore deck |
| GBS topside steel yield stress | 355 MPa | high strength steel commonly used at present; trend to 420-460 MPa |
| typical production deck spans | floor plate 1 m; stringer 5 m; deck beam 15 m; main structure 15 m m | typical floor design dimensions |


### Offshore topsides (top-offshore-topsides-definition-function-and-structural-scope)

Primary code: UPS: Upstream
The above-water steel structure, consisting of one or more decks, that holds all facilities for exploration/production and human activity; it is designed and fabricated separately from the substructure and integrated inshore or offshore. Its three common design elements are: hold all equipment needed for operations, provide a safe and sustainable healthy living environment, and optimise dimensions and weight.
Vendors: Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| definition | steel structure consisting of more than one deck holding facilities for exploration/production and human activities n/a | book chapter definition; topsides and deck often used interchangeably |
| inter-deck vertical distance | 6-9 m | vertical distance between topside decks, North Sea practice |
| cellar deck air gap above design wave crest | 1.5 m minimum | max elevation of design wave crest including tide and storm sway plus minimum 1.5 m air gap |
| heavy deck threshold requiring MSF | 10000 tons | decks over 10,000 t are provided with a module support frame onto which modules are placed |
| weight prognosis uncertainty surcharge | ?-30 % | conceptual design phase surcharge, reducing to +5% at final fabrication phase |
| main deck live load | 20 kN/m2 | generally accepted figure for main decks; API-RP2A does not specify live loads |
| concentrated deck live load | 10-25 kN on 0.3 x 0.3 m area | generally accepted figures for main decks |
| floor plate thickness | 6-10 mm | chequered or flat steel plate; usually 8-10 mm, 6 mm for lighter loaded floors |
| stringer centres | 1000-1200 mm | hot rolled beams typical spacing; IPE 240-270 / HE 240-280A at ~1 m centres spanning 5 m |
| jacket transverse column spacing | 9-15 m | Dutch sector North Sea: 9 m wellhead platform to 15 m production platform; longitudinal ~15 m |
| deck beam section | HE 800-1000 (or HL 1000 400 mm wide / HX 1000 450 mm wide) section designation | deck beams supporting floor panels or major equipment |


### Self-installing topsides (top-self-installing-topsides)

Primary code: UPS: Upstream
Topsides installed without a heavy-lift crane vessel, using self-contained jacking/lifting systems, skidding or the support structure's own buoyancy; reduces dependence on scarce heavy-lift tonnage.
Vendors: Kiewit (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Topsides installed without a heavy-lift crane vessel, using self-contained jacking/lifting systems, skidding or the support structure's own buoyancy; reduces dependence on scarce heavy-lift tonnage. | Qualitative function from pages read in this sweep. |


### Semi-submersible production topsides (top-semi-submersible-production-topsides)

Primary code: UPS: Upstream
Topsides placed on column-stabilised floating hulls held by catenary moorings; can be integrated and commissioned at dock, with installation method (heavy lift, jacking, float-over, multiple lifts) strongly affecting selection.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Topsides placed on column-stabilised floating hulls held by catenary moorings; can be integrated and commissioned at dock, with installation method (heavy lift, jacking, float-over, multiple lifts) strongly affecting selection. | Qualitative function from pages read in this sweep. |


### Small topsides: portable / mobile (top-small-topsides-portable-mobile-mopu-topsides)

Primary code: UPS: Upstream
Portable or reusable offshore production facility where the topsides can be moved and reused; includes ship-shaped FPSOs, spars, TLPs, jack-ups, semi-submersible production units and production barges.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Portable or reusable offshore production facility where the topsides can be moved and reused; includes ship-shaped FPSOs, spars, TLPs, jack-ups, semi-submersible production units and production barges. | Qualitative function from pages read in this sweep. |


### Small topsides: unmanned wellhead / minimal process (top-small-topsides-unmanned-wellhead-minimal-process-uwhp-nnm-mono)

Primary code: UPS: Upstream
Minimalist topsides for wellhead-only or very small production functions, normally unattended, with no process facilities in the simplest cases. Used where wells are tied back to existing facilities, or for marginal/small fields.
Vendors: Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Visund Gas topsides weight | 1000 t (rounded) | Aibel project 2005 |
| Sleipner B topsides weight | 2000 t (rounded) | Aibel project 2008 |


### Spar topsides (top-spar-topsides)

Primary code: UPS: Upstream
Topside supported on a deep-draft single vertical cylinder (classic, truss or cell spar) with a typical fixed-platform-style deck carrying drilling and production equipment and dry-tree risers; low heave motion suits ultra-deepwater.
Vendors: Kiewit Offshore Services (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Perdido single-lift spar topsides | 9500 ton (8,618 metric ton) | installed by Thialf March 2009 with living quarter added three days later; heaviest single-lift topsides in GOM by HLCV at the time |
| Perdido spar water depth | 2450 m | deepest spar in world at time of source |
| Perdido topsides deck count | 3 decks | support oil and gas processing, drilling rig and living quarters |


### Tension leg platform (top-tension-leg-platform-tlp-topsides)

Primary code: UPS: Upstream
Topside carried on a column-stabilised buoyant hull held by tensioned tendons; supports drilling, production and accommodation. Enables surface BOP/wellhead access but adds drilling-package weight, riser tension and motion design constraints.
Vendors: McDermott, SBM Atlantia / SOFEC (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Hutton TLP topsides weight | 20000 Te | largest integrated deck built at Ardersier; client Conoco, 1984 |
| Hutton TLP water depth | 143 m | installation depth in Hutton Field; production 1984-2001 |
| Olympus TLP displacement | 126000 tons | largest Shell TLP in US GOM; more than twice displacement of neighbouring Mars TLP |
| Olympus TLP deck area | 342000 ft2 | accommodates 100,000 BOEPD processing capacity and up to 192 crew |
| Kizomba A TLP overall platform weight | 35000 tonnes | 100-man living quarters, two 6,000 t topsides modules, 7,500 t drilling rig, two support modules, 36 well slots |
| full drilling package deepwater TLP typical weight | 4000-6000 tons | depends on topside concept and site conditions |
| skidable North Sea drilling rig dry weight | 2000-3000 tons | operating weight 4,000-6,000 t with variable loads |
| mud and drilling supply facilities weight | 2000-4000 tons | lower figure typical integrated topside, upper figure separate module; module operating weight up to 8,000 t with pipe rack |


### Topside systems (top-topside-systems-process-layout-piping-electrical-icss-f-g-esd)

Primary code: UPS: Upstream
The distributed systems carried by the topside structure: process equipment and pipe racks; power generation/distribution and control; fire & gas and emergency shutdown; heating/ventilation/air conditioning; material-handling cranes; escape/lifesaving; helicopter decks; and inter-platform bridges.
Vendors: Alliance Engineering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| helideck location requirement | near living quarters; usually on obstacle-free area on top of living quarters n/a | to enable fast evacuation |
| deck crane siting | outside helideck obstacle-free area; maximum deck coverage; operator eye contact with load and supply vessel n/a | layout requirement |
| pipe rack arrangement | central longitudinal pipe rack with process/utility modules on either side n/a | FPSO best practice; rack floor at same elevation as common lower deck level |
| electrical building strategy | main electrical building aft plus auxiliary electrical building forward n/a | distributes cable tray runs, allows smaller electrical buildings and lower module weights |
| FPSO process optimisation example module count and weight saving | 10 modules; 7,000 t weight reduction and ~$300 million savings | 100,000 b/d oil, 250 mmcf/d gas, 100,000 b/d produced water, 275,000 b/d water injection at 5,000 psig; oil stabilisation vs conventional stage separation |
| escapeway width criterion | sufficient to allow evacuation of personnel on stretchers n/a | walkways, ladders and stairs kept obstacle-free and non-slippery |


### Topside weight and area benchmarks (top-topside-weight-and-area-benchmarks-small-vs-large)

Primary code: UPS: Upstream
Empirical relations and published weight tables used for early-stage sizing and checking whether a proposed topsides weight is within historical ranges.
Vendors: Heerema (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Eiffel Tower comparator weight | 9000 tonnes | comparator used in Aibel weight article |
| Aibel project weight range (listed examples) | 1000-24000 t (rounded) | Visund Gas 1,000 t (2005) to Johan Sverdrup P2 24,000 t (2022) |
| weight cells used simultaneously for P2 weighing | 50-60 cells | up to 50-60 weight cells lift the module from grillage; process repeated three times |
| minimum equipment weight logged for weighing | 1 tonne | Aibel follows ISO weighing standard; all equipment over one tonne weighed before installation |
| Aker Solutions design weight envelope | 2000-40000 tonnes (over 40,000 at top end) | company facility design range |


## tp-wellhead

### Amine sweetening (tp-amine-sweetening-mdea-and-formulated-amines)

Primary code: UPS: Upstream
Absorb H2S and CO2 from sour gas in a contactor using lean amine; regenerate in a still/reboiler; route acid gas to flare, vent or sulphur recovery unit.
Vendors: BASF, Kinder Morgan Treating, SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| MDEA CAS number | 105-59-9 CAS | BASF OASE Formulations & Solvents page; page read |
| Other amine solvents (CAS) | ADEG 929-06-6; MEA 141-43-5; DEA 111-42-2; DIPA 110-97-4; NFM 4394-85-8; NAM 1696-20-4 CAS list | BASF page; page read |
| Amine regeneration temperature | ~225 degF | Kinder Morgan Treating 'How Amine Treating Sweetens Natural Gas'; page read |
| Reference plant capacity | 2 x 30 MMSCFD amine trains (60 MMSCFD sour gas plant) MMSCFD | SPEC Amine Sweetening page; page read |


### Chemical injection systems — methanol/MEG, corrosion/scale inhibitor, demulsifier, defoamer, biocide (tp-chemical-injection-systems-methanol-meg-corrosion-scale-inhibi)

Primary code: UPS: Upstream
Inject hydrate inhibitors, corrosion/scale inhibitors, demulsifiers, defoamers and biocides via dosing pumps and tanks to maintain flow assurance, separation performance and asset integrity.
Vendors: SLB (Cameron pressure control equipment), SPEC Oil & Gas Technologies (fabricator), US EPA Natural Gas STAR Program (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Methanol/EG hydrate-inhibition regime | EG above -40 degF; methanol below -140 degF degF | Digital Refining article; page read |
| Chemical injection skid configuration | dosing pumps + tank on skid; supplied with process equipment or standalone configuration | SPEC Utility Systems page; page read |


### Compact / in-line separation and debottlenecking (tp-compact-in-line-separation-and-debottlenecking-cross-cutting-t)

Primary code: UPS: Upstream
Increase existing separator capacity and reduce topside weight/footprint by bulk phase bypass and high-efficiency internals rather than new large vessels.
Vendors: TechnipFMC (CDS Separation Systems), OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| InLine ElectroCoalescer claim | drastically enhances liquid-liquid separation; reduces footprint/cost; ideal for debottlenecking qualitative | TechnipFMC Production page; page read |
| Subsea compact separation envelope | 1,015 metric tons CO2e elimination claim (electrified subsea approach) t CO2e | OneSubsea subsea separation page; page read |


### Dew point control and gas cooling / hydrocarbon recovery (tp-dew-point-control-and-gas-cooling-hydrocarbon-recovery)

Primary code: UPS: Upstream
Meet water and hydrocarbon dew point sales specs by cooling/condensing heavy components, with upstream dehydration to prevent hydrate/ice formation; low-temperature separation, refrigeration, silica gel and LTS options.
Vendors: Pietro Fiorentini (TEG packages), SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Hydrate inhibitor temperature applicability | EG above -40 degF; methanol down to below -140 degF degF | Digital Refining article; page read |
| Dehydration route economics | glycol absorption less capex/opex than molecular sieve for 1-7 lb/MMSCF target comparison | Digital Refining article; page read |
| Available dew-point product families | silica gel WDP/HDP control; hydrocarbon recovery/LTS dew point control; gas heat exchangers; indirect water/glycol bath heaters list | Pietro Fiorentini gas-treatment product family links; page read |


### Electrical distribution, instrument/plant air, nitrogen, hydraulic power, seawater/lift pumps, HVAC, firewater (tp-electrical-distribution-instrument-plant-air-nitrogen-hydrauli)

Primary code: UPS: Upstream
Support utilities and safety systems that make the process train operable: power distribution, pneumatic control air, inerting, actuation power, cooling/firewater, lifting and living quarters.
Vendors: SPEC Oil & Gas Technologies (fabricator), Siemens Energy (incl. ex-Dresser-Rand) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Instrument air package equipment | rotary screw, oil-free screw or reciprocating compressors; KO drum, filters, refrigerated or adsorption dryers; receiver tanks, piping, instrumentation, valves list | SPEC Utility Systems page; page read |
| Utility scope linkage | utility scope follows process equipment: what has to be heated, cooled, driven, instrumented and drained qualitative | SPEC Utility Systems page; page read |


### ESD / F&G / ICSS — emergency shutdown, fire and gas, safety instrumented systems, HIPPS (tp-esd-f-g-icss-emergency-shutdown-fire-and-gas-safety-instrument)

Primary code: UPS: Upstream
Detect fire/gas and execute SIL-rated shutdown and mitigation actions, integrated with process control on offshore/floating facilities.
Vendors: Honeywell, TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Safety Manager SIL capability | SIL 1-3 IEC 61508/61511 | Honeywell Safety Manager product page; page read |
| Operating temperature | -40 to 70 degC (remote cabinet); -5 to 70 degC (Safety Manager cabinet) degC | Honeywell Safety Manager specifications table; page read |
| Safety/F&G standards listed | IEC 61508, IEC 61511, ISA S84.01, NFPA 72/85/86, EN54-2, ATEX, UL/FM standards | Honeywell Safety Manager page specifications + Honeywell F&G case study; page read |
| HIPPS offering | High Integrity Pressure Protection System listed system | TechnipFMC Production page Safety and Control list; page read |


### Flare and vent system — flare stack/boom, flare tips, KO drums, gas recovery/VRU (tp-flare-and-vent-system-flare-stack-boom-flare-tips-ko-drums-gas)

Primary code: UPS: Upstream
Safely dispose of relief/blowdown/start-up gas by controlled combustion; knock out entrained liquid upstream to prevent flaming rain; recover gas where feasible.
Vendors: FlareTech Inc., CRA (Combustion Research Associates), NAO Inc., Allmarc Industries (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flare KO drum size range (fabricator) | 2 to 600 BBL | FlareTech Inc. Flare Knockout Drums page; page read |
| size range | 2-600 BBL BBL | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| PORTA-TEST REVOLUTION installations | >500 worldwide installations | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| configuration | horizontal or vertical configuration | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| company installations | >800 in >25 countries since 1993 count | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |


### Free-water knockout (tp-free-water-knockout-fwko-and-desanders-desanding-hydrocyclones)

Primary code: UPS: Upstream
Remove bulk free water before downstream heating/chemical treating; remove sand/solids from wellstream or produced water upstream of separation and oil-in-water separation.
Vendors: TechnipFMC (CDS Separation Systems), OneSubsea (SLB/Aker Solutions JV), Enerflex, Enhydra Ltd, eProcess Technologies (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| FWKO suitable duty | separate-phase water only; not stable emulsions qualitative | SPEC FWKO page, 'Free Water, Not Emulsion'; page read |


### Gas compression — reciprocating, centrifugal/axial, rotary screw; suction/discharge scrubbers (tp-gas-compression-reciprocating-centrifugal-axial-rotary-screw-s)

Primary code: UPS: Upstream
Raise associated/export gas pressure, provide gas lift/reinjection/vapour-recovery/refrigeration duty; scrub liquids ahead of and after compressors.
Vendors: SPEC Oil & Gas Technologies (fabricator), Siemens Energy (incl. ex-Dresser-Rand), OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Compressor types offered (package) | high-speed reciprocating; rotary screw list | SPEC Compressor Packages page; page read |
| Topside pump/compressor skid envelope (TechnipFMC standard pumps) | up to 10,000 psi and 1,500 gpm psi / gpm | TechnipFMC Production page 'Standard pumps and complete skid systems'; page read |
| Subsea processing envelope (context for topside debottlenecking) | 2,500 m water depth; 350 degF; 15,000 psi m / degF / psi | TechnipFMC Subsea processing page; page read |


### Gas export / sales specification compliance (tp-gas-export-sales-specification-compliance-cross-cutting)

Primary code: UPS: Upstream
Ensure dehydrated, sweetened, dew-point-controlled gas meets pipeline/sales requirements for water content, H2S/CO2, hydrocarbon dew point and heating value before custody transfer.
Vendors: Honeywell, Emerson (duplex stainless steel option on Roxar 2600, page read) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pipeline water content target | 1-7 lb/MMSCF (20-140 ppmv) | Digital Refining article; page read |
| Pipeline requirement (operator practice) | 7 lb/mmcf or less | Kinder Morgan Treating dehydration page; page read |
| Standard TEG dry-gas guarantee | 3-7 lb water/MMSCF | Pietro Fiorentini page; page read |


### Glycol (tp-glycol-teg-dehydration)

Primary code: UPS: Upstream
Contact wet gas with lean triethylene glycol in an absorber/contactor, then regenerate glycol in a reboiler/still to meet water-content and water-dew-point specification and prevent hydrates/corrosion.
Vendors: Pietro Fiorentini (TEG packages), Kinder Morgan Treating, SPEC Oil & Gas Technologies (fabricator), Cimarron Energy (Aereon) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pipeline water-content specification range | 1-7 lb/MMSCF (20-140 ppmv) | Digital Refining (PTQ) article 'Controlling the dew point of natural gas', Fluor Enterprises; page read |
| Dry gas spec from TEG unit | 3-7 lb water/MMSCF gas | Pietro Fiorentini gas dehydration packages page; page read |
| Regenerated TEG purity, conventional | ~99 wt% | Digital Refining article; page read |
| TEG thermal degradation threshold | 404 degF (207 degC) | Digital Refining article; page read |
| Water dew point from 99.96 wt% lean TEG | -40 degF (-40 degC) WDP at 80 degF contactor | Digital Refining article; page read |
| Rich TEG pressure at contactor outlet | 250-800 psig | US EPA Natural Gas STAR 'Glycol Dehydrators'; page read |
| Dehydrator capacity range | ~1 to ~400 MMscfd | Kinder Morgan Treating dehydration page; page read |
| CO2 pipeline water limit (Kinder Morgan spec) | ≤30 lb water/MMSCF vapour phase; no free water | Kinder Morgan Treating dehydration page; page read |
| Project reference capacity | 2 x 30 MMSCFD TEG trains (60 MMSCFD sour gas plant) MMSCFD | SPEC Glycol Dehydration project reference; page read |


### Inlet scrubbers / gas scrubbers / slug catchers (tp-inlet-scrubbers-gas-scrubbers-slug-catchers)

Primary code: UPS: Upstream
Remove free liquid and solids from gas entering a treatment facility before additional processing; protect compressors and downstream equipment.
Vendors: SLB (Cameron pressure control equipment), SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Gas filter separator standard design pressure | 1440 psi (99 bar) | SPEC Gas Filter Separator 'Mechanical Features' table; page read |


### Mercury removal (tp-mercury-removal)

Primary code: UPS: Upstream
Remove elemental mercury from gas to protect brazed aluminium plate-fin heat exchangers in cryogenic recovery/liquefaction plants.
Vendors: Pietro Fiorentini (TEG packages) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Typical inlet mercury concentration | 1-10 micrograms/Nm3 (approx. 0.1-10 ppbv) | Pietro Fiorentini Gas mercury removal page; page read |
| Designed outlet mercury concentration | 0.001 micrograms/Nm3 | Pietro Fiorentini page; page read |


### Metering and export quality — oil/gas/water meters, multiphase flow meters, custody transfer, sampling, sales  (tp-metering-and-export-quality-oil-gas-water-meters-multiphase-fl)

Primary code: UPS: Upstream
Measure oil, gas and water rates (with or without separation), support allocation and custody transfer, sample fluids at or above hydrocarbon dew point, and demonstrate compliance with sales specifications.
Vendors: SLB (Cameron pressure control equipment), Emerson (duplex stainless steel option on Roxar 2600, page read), TechnipFMC (CDS Separation Systems), Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Roxar 2600 MPFM operating envelope | 0-100% GVF and 0-100% WLR; 6 sizes; duplex stainless steel to Inconel % / sizes | Emerson Roxar 2600 product page; page read |
| TechnipFMC MPM GVF range | 0-100 % GVF | TechnipFMC Production page; page read |
| GVF / WLR | 0-100% / 0-100% % | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| sizes | 6 sizes; 1.5-8 in in | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| design pressure | 3,750 psi ANSI / 5,000 psi hub psi | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |


### Molecular sieve dehydration and solid desiccants (tp-molecular-sieve-dehydration-and-solid-desiccants)

Primary code: UPS: Upstream
Adsorb water to very low dew points upstream of cryogenic processing/LNG/NGL recovery; swing-bed adsorption with heated regeneration gas.
Vendors: Pietro Fiorentini (TEG packages), SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Water content achievable | as low as 1 ppm vol | Pietro Fiorentini fixed-bed dehydration page; page read |
| Water content / dew point capability | <0.1 ppmv water; WDP as low as -150 degF (-100 degC) or less ppmv / degF | Digital Refining article; page read |
| Regeneration gas temperature | ~550 degF (290 degC) | SPEC Molecular Sieve Dehydration page 'Key Figures'; page read |
| Reference duty | 100 tonne/day LPG facility tonne/day | SPEC Umutu LPG plant, Delta State, Nigeria 2009; page read |


### Oil heating and crude/condensate stabilisation (tp-oil-heating-and-crude-condensate-stabilisation)

Primary code: UPS: Upstream
Heat emulsion or crude; strip light ends from crude/condensate to meet Reid vapour pressure (RVP) and H2S limits for storage/export; supply heat from hot-oil or fired systems.
Vendors: SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Water bath heater maximum outlet temperature | 87 degC | SPEC Ancillary Equipment overview and Water Bath Heater page; page read (ancillary overview) |
| Stabiliser configuration | column with trays/packing + reboiler (gas, hot oil or steam) configuration | SPEC Crude & Condensate Stabilization page; page read |


### Oil treatment — mechanical heater treaters, electrostatic treaters/dehydrators, desalters (tp-oil-treatment-mechanical-heater-treaters-electrostatic-treater)

Primary code: UPS: Upstream
Break produced-water-in-oil emulsions with heat and residence time or an applied electrostatic field; reduce BS&W and salt content to export specification.
Vendors: SPEC Oil & Gas Technologies (fabricator), SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Mechanical treater capacity | >20,000 barrels of liquid per day (BLPD) | SPEC Mechanical Heater Treater typical design data; page read |
| Electrostatic vs mechanical treater (qualitative) | lower BS&W, lower salt content, smaller footprint comparison | SPEC Electrostatic Heater Treater & Desalter comparison table; page read |
| Desalting reference plant capacity | 50,000 BOPD | SPEC TAQA Atrush project scope: 2 electrostatic dehydrators + 2 crude cross exchangers; page read |
| regeneration gas temperature | ~550 degF (290 degC) degF | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| towers | minimum 2, fixed switching cycle count | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| treating capacity | >20,000 BLPD, including low-API crude BLPD | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| reference facility | 50,000 BOPD; 2 dehydrators + 2 cross exchangers BOPD | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| reference trains | 2 x 30 MMSCFD MMSCFD | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| TEG outlet spec (Fiorentini) | 3-7 lb water/MMSCF lb/MMSCF | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |


### Power generation — gas turbines and diesel (tp-power-generation-gas-turbines-and-diesel)

Primary code: UPS: Upstream
Supply electrical power and mechanical drive for topside process, compression, water injection and utilities; combined-cycle and single-lift modular packages for offshore use.
Vendors: Siemens Energy (incl. ex-Dresser-Rand) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| SGT-800 combined cycle range | 150-450 MW | Siemens Energy SeaFloat page; page read |


### Produced water treatment — deoiling hydrocyclones, flotation (tp-produced-water-treatment-deoiling-hydrocyclones-flotation-igf)

Primary code: UPS: Upstream
Reduce oil-in-water from produced water to discharge or reinjection specification; bulk removal by hydrocyclone, polishing by flotation and filtration.
Vendors: SPEC Oil & Gas Technologies (fabricator), ISS Process (Innovative Synergy Solutions), TechnipFMC (CDS Separation Systems), Veolia Water Technologies / VWS Westgarth, CECO Environmental (Peerless Separation & Filtration), Wasco Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Hydrocyclone outlet quality | as low as 25 ppm oil in water | SPEC Hydrocyclone Separators typical design data table; page read |
| IGF outlet quality | as low as 10 ppm oil in water | SPEC Induced Gas Flotation typical design data; page read |
| Nutshell filter outlet quality | as low as 5 ppm oil in water | SPEC Nutshell Filters typical design data; page read |
| Malaysia BOKOR CPP guarantee | 80,000 BWPD; 30 ppm OIW outlet (monthly) BWPD / ppm | ISS Process project page; page read |
| Malaysia PEGAGA guarantee | 12,000 BWPD; 2,000 ppm inlet -> 20 ppm OIW outlet (monthly) BWPD / ppm | ISS Process project page; page read |
| Malaysia SK408W Jerun guarantee | 3,200 BWPD; 3,000 ppmV inlet -> 20 ppmV OIW outlet BWPD / ppmV | ISS Process project page; page read |


### Three-phase (tp-three-phase-production-test-separator-horizontal-vertical-sphe)

Primary code: UPS: Upstream
Split well effluent into gas, oil and free water; absorb inlet momentum, provide liquid retention, demist gas and control each outlet. Commonly used as a free-water knockout (FWKO).
Vendors: SLB (Cameron pressure control equipment), TechnipFMC (CDS Separation Systems), SPEC Oil & Gas Technologies (fabricator) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Separator orientation | horizontal, vertical or spherical configuration | SLB Energy Glossary definition of three-phase separator; page read |
| Design code | ASME Section VIII, Division 1 code | SPEC two-/three-phase separator page, 'Design basis' table; page read |
| Inlet device types | Diverter plate, half pipe, vane, cyclonic list | SPEC two-/three-phase separator page, 'How the vessel works'; page read |


### Water injection, reinjection pumps and seawater treatment (tp-water-injection-reinjection-pumps-and-seawater-treatment)

Primary code: UPS: Upstream
Provide reservoir pressure support/disposal by filtering seawater or produced water and injecting at high pressure; remove solids/sulphate/divalent ions that cause scaling/souring.
Vendors: Baker Hughes, OneSubsea (SLB/Aker Solutions JV), Siemens Energy (incl. ex-Dresser-Rand), TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide reservoir pressure support/disposal by filtering seawater or produced water and injecting at high pressure; remove solids/sulphate/divalent ions that cause scaling/souring. | Qualitative function from pages read in this sweep. |


## truck-rail

### Truck/rail loaders, shiploaders and bulk loading stations (bulk-loading-stations)

Primary code: PCH: Petrochemicals
Truck/rail loaders, shiploaders and bulk loading stations | Jetty / loading and rail loading
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| equipment class | shiploaders, truck dumpers, railcar dumpers/wagon tipplers, mobile hopper loaders/unloaders listed as bulk handling systems n/a | Wikipedia Bulk material handling |
| silo discharge to transport | silos can be unloaded into rail cars, trucks, or conveyors n/a | Wikipedia Silo, Tower silo section |
| Export terminal | deep wharf at Butterworth, Penang facility | Petronas Chemicals Fertiliser Kedah uses a deep wharf terminal in Butterworth as primary maritime gateway; granular urea moved from Kuala Muda by dedicated railway connection |
| Marine export facility (planned) | CALM buoy single-point mooring about 4.6 km offshore facility | Murchison Green Hydrogen full-scale scope includes marine export facility with pipelines and single-point mooring, plus desalination plant 5 GL/a |


Recorded gaps:

- Loading rates (t/h), spout sizes, dust capture, OEM model data — Fetch a bulk loader OEM page (BEUMER, Siwertell, AUMUND) via verified URL.
- Loading rates (t/h), spout sizes, dust capture, OEM model data — Fetch a bulk loader OEM page (BEUMER, Siwertell, AUMUND) via verified URL.

## turbine

### Industrial gas turbine (aeroderivative and heavy-frame) (turbine-gas-industrial)

Primary code: PWR: Power and renewables
Gas turbine for power generation and mechanical drive, in two families: aeroderivative units adapted from jet engines (fast start, high simple-cycle efficiency, modular exchange) and heavy-frame machines built for bulky base-load duty behind the grid or as compressor drives on pipelines and gas plants. Sets the exhaust energy that an HRSG converts in combined-cycle and cogeneration service.
Vendors: Baker Hughes, GE Vernova, Solar Turbines, Siemens Energy (incl. ex-Dresser-Rand) (2 model lines recorded).

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

### UPS systems (data-centre-ups-flywheel)

Primary code: IDC: Data centres
UPS systems (double-conversion, modular, flywheel, lithium-ion)
Vendors: Eaton, Vertiv, Schneider Electric, Active Power / Piller (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | UPS systems (double-conversion, modular, flywheel, lithium-ion) | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Measured field efficiency curves of high-efficiency UPS modes when fed by a gas engine with frequency variation — Look for independent test reports (LBNL/Uptime/IEEE) on UPS-generator interaction

## urea

### Urea melt / melting and hot-urea-solution handling (urea-melt-handling)

Primary code: PCH: Petrochemicals
Urea melt / melting and hot-urea-solution handling
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| melting point | 132.4 degC | Urea physical property (CRC97 cited by Wikipedia) |
| molten urea decomposition onset | 152 degC | molten urea decomposes into ammonium cyanate at about 152 C |
| urea water solubility | 1200 g/L | solubility in water at 25 C (CRC97) |


Recorded gaps:

- Melt tank capacity, material, pump specs, pipe tracing design — Seek a urea melt handling vendor datasheet.
- Melt tank capacity, material, pump specs, pipe tracing design — Seek a urea melt handling vendor datasheet.

### Urea solution / hot urea solution tanks and pumps (urea-solution-handling)

Primary code: PCH: Petrochemicals
Urea solution / hot urea solution tanks and pumps (UAN, UAS, AdBlue)
Vendors: SensoTech GmbH, Stamicarbon (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| UAN nitrogen content | 32 wt% N | Wikipedia: UAN stable solution total nitrogen content 32%, approaching solid ammonium nitrate 33.5%, urea itself 46% |
| UAN share of US liquid fertilizers | 80 percent | Wikipedia Urea liquid forms, citing Ren et al. 2021 |
| DEF/AdBlue composition | 32.5% urea, 67.5% de-ionized water wt% | Wikipedia Urea Miscellaneous section |
| inline urea concentration measurement range | 0-100 m% (mass percent) | SensoTech LiquiSonic typical measuring range for urea |
| STAMI SPECIALTIES liquid products | enables production of liquid UAN and granular UAS n/a | Stamicarbon profile on UreaKnowHow |


Recorded gaps:

- Hot urea solution tank design temperature, material, pump specs, storage capacity — Fetch a urea solution tank/pump OEM page.
- Hot urea solution tank design temperature, material, pump specs, storage capacity — Fetch a urea solution tank/pump OEM page.

## urea-reactor

### Urea reactor (urea-reactor)

Primary code: PCH: Petrochemicals
High-pressure reactor in which ammonia and carbon dioxide form ammonium carbamate and then dehydrate to urea. Conversion per pass is incomplete, so the high-pressure loop strips and recycles unconverted carbamate; reactor pressure, temperature and the ammonia-to-CO2 ratio set conversion and downstream stripping duty.
Vendors: Stamicarbon, thyssenkrupp Uhde, Casale, Toyo Engineering, Saipem (ex-Micoperi 7000), Casale SA (5 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| operating pressure | 150 bar | Saipem urea flowsheet, NH3-stripping process |
| reactor outlet temperature | 188 °C | Saipem urea flowsheet, NH3-stripping process |
| NH3/CO2 (N/C) ratio | 3.2-3.4 mol/mol | Snamprogetti process; patents quote 2.5-3.5 with 3.0-3.2 preferred |
| CO2 conversion per pass | 62-64 % | share of CO2 entering the reactor converted to urea; the high-pressure loop reaches 85-90% overall |
| carbamate formation enthalpy | -117 kJ/mol | 2 NH3 + CO2 <-> NH4CO2NH2 at 110 atm and 160 C; fast exothermic |
| urea conversion enthalpy | 15.5 kJ/mol | NH4CO2NH2 <-> CO(NH2)2 + H2O, slow endothermic, at 160-180 C |
| world urea production capacity | 180000000 tonnes/year | worldwide production capacity in 2020, cited to IFASTAT |
| biuret formation suppression | excess ammonia n/a | 2 urea -> biuret + NH3; suppressed in synthesis reactor by maintaining excess ammonia |
| corrosion mitigation | continuous small oxygen (air) injection; duplex stainless (1990s); zirconium or zirconium-clad titanium tubing (2000s) n/a | ammonium carbamate highly corrosive even to resistant stainless; passive oxide layer maintained by oxygen injection |
| synthesis pressure / temperature (vendor description) | 200 C, 130-200 bar n/a | SensoTech application note: thermal conversion of ammonium carbamate at a temperature of 200 C and pressure 130 to 200 bar |
| process type | self-stripping with MHP carbamate decomposition n/a | Casale Urea technology page |

- **Stamicarbon** LAUNCH MELT pool reactor design: suited to capacities up to about 2,500 mtpd; about 30 m plant height
- **Toyo Engineering** ACES21 process: reactor at N/C 3.7, 182 C and 152 bar
- **Toyo Engineering** ACES21-LP process: synthesis pressure lowered to 136 barG; 5-10% lighter synthesis equipment
- **Casale** HYPER-U: combined condenser/reactor; optimally designed up to 4,000 MTD
- **Saipem (ex-Micoperi 7000)** Snamprogetti ammonia stripping urea process: synthesis conditions 188 C and 155 kg/cm2

Recorded gaps:

- Reactor volume, design pressure/temperature, liner material, number of trays/compartments, residence time — Read the Casale HYPER-U / SPLIT FLOW LOOP PDFs via a PDF-capable tool, and seek Stamicarbon Urea brochure.
- Reactor volume, design pressure/temperature, liner material, number of trays/compartments, residence time — Read the Casale HYPER-U / SPLIT FLOW LOOP PDFs via a PDF-capable tool, and seek Stamicarbon Urea brochure.

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

## valve-station

### Pressure-reducing valves (PRVs) and desuperheating / attemperation stations (prv-desuperheating-station)

Primary code: PWR: Power and renewables
Reduce and stabilise steam pressure for process users (self-acting or actuated), and, where superheated steam is used for heating, inject water to control superheat to a temperature above saturation; protect downstream equipment and stabilise control (Spirax Sarco; TLV).
Vendors: Spirax Sarco (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| direct-acting bellows PRV proportional band | 30-40 % of upstream pressure | Spirax Sarco pressure control applications |
| pilot-operated PRV proportional band | typically <200 kPa | Spirax Sarco: narrow band and low hysteresis give tight repeatable control |
| practical maximum pressure ratio per reducing stage | 10:1 ratio | Spirax Sarco series pressure reducing stations; example 25 barg -> 5 barg -> 1 barg |
| globe control valve flow rangeability | 50:1 ratio | Spirax Sarco stated acceptable rangeability for pneumatic/electropneumatic pressure reduction |
| diaphragm PRV pressure drop capability | 50:1 small sizes; 10:1 large sizes ratio | Spirax Sarco direct-operated diaphragm type |
| desuperheated steam temperature above saturation (control setpoint) | 5-10 °C above saturation | Spirax Sarco pressure control applications; basic theory page says minimum typically within 3°C of saturation |
| single-nozzle spray desuperheater minimum approach / turndown | 10°C above saturation; turndown max 3:1 °C / ratio | Spirax Sarco basic desuperheater types; radial and axial single-nozzle types |
| multi-nozzle axial desuperheater turndown | 8:1 fixed area; 9:1 spring-assisted; 12:1 variable area ratio | Spirax Sarco basic desuperheater types |
| tube-bundle desuperheater envelope | typically around 60 bar and 450°C; within 5°C of saturation bar / °C | Spirax Sarco indirect-contact type; high max operating temperature and pressure |
| desuperheater steam inlet velocity | 40-60 m/s | typical velocity entering a desuperheater in good piping design; Spirax Sarco |
| attemperation water pressure | must exceed steam pressure at injection point qualitative | Spirax Sarco water spray desuperheating; booster pump may be required |
| steam enthalpy split example | at 10 bar a / 300°C: water 763, evaporation 2015, superheat 274 kJ/kg | Spirax Sarco worked example; illustrates why desuperheating is needed for heating applications |


Recorded gaps:

- Numeric attemperation/spraywater purity limit (conductivity, sodium, silica, solids) — Fetch GE Vernova/Siemens steam turbine or boiler attemperation water specification and cite exact limits and basis.
- PRV noise prediction and silencer sizing method — Fetch Spirax control-valve noise module and IEC 60534-8-3 based vendor sizing notes.

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
| Scope | BMS / combustion controls / valve trains / installation / commissioning scope of supply | Zeeco Power Burners page GB burner bullet 'Total system approach: Full Scope of supply with BMS/combustion controls/valve trains/installation/commissioning' |
| Fuel skid customization | Custom fuel skids for various applications worldwide; any required dimension and specified feature capability | Zeeco Industrial Burners page Burner management systems section |


Recorded gaps:

- explicit vent arrangement and valve proof-of-closure details — Read a fuel-train P&ID from an OEM or NFPA 85 primary text.
- gas booster/compressor sizing for low supply pressure — Find a gas-pressure and booster selection reference.

## vibratory

### Vibratory conveyors (bulk-vibratory-conveyors)

Primary code: PCH: Petrochemicals
Vibratory conveyors
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| vibrator-assisted discharge | hard-to-handle products discharged from 45-degree fabric silo cone, minimally assisted by a small vibrator fitted to the discharge transition n/a | Wikipedia Silo, Flexible silo storage system section |


Recorded gaps:

- Vibratory conveyor capacity, trough width, frequency/amplitude, OEM models — Fetch a vibratory conveyor OEM engineering page.
- Vibratory conveyor capacity, trough width, frequency/amplitude, OEM models — Fetch a vibratory conveyor OEM engineering page.

## waste

### Waste heat boilers, steam generation, economisers and superheaters (ammonia-waste-heat-boiler)

Primary code: PCH: Petrochemicals
Waste heat boilers, steam generation, economisers and superheaters | Boilers and steam system (HP/MP/LP, waste-heat and package boilers)
Vendors: Topsoe, Chart Industries / Howden (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Ammonia-loop waste heat boiler design feature | patented bayonet tube design keeps all low-alloy metal parts out of temperature zones where nitriding is a concern qualitative | Topsoe waste heat boiler (ammonia loop) equipment description |
| Historical energy intensity reduction | 27-100 GJ per tonne ammonia | Energy consumption reduced from 100 GJ/t ammonia in 1920 to 27 GJ in 2019 (Ramskov 2019 cited) |
| HP steam pressure | 40 bar | Typical site HP steam about 40 bar, condensing temperature 250 C |
| MP steam pressure | 20 bar | Typical MP main about 20 bar, condensing temperature 212 C |
| LP steam pressure | 3 bar | Typical LP main about 3 bar, condensing at 134 C |
| Cogeneration overall thermal efficiency | 70-80 % | Overall thermal efficiency of gas-turbine cogeneration with HRSG can be in the range 70-80% |
| Boiler types in Pusri cradle-to-gate boundary | package boiler; waste heat boiler; coal boiler list | PT Pupuk Sriwidjaja Palembang urea EPD utilities |


Recorded gaps:

- Steam pressure levels, duty (t/h), tube material and economiser/superheater specifications — Fetch a waste-heat boiler OEM page or ammonia plant steam-balance reference.
- Steam pressure levels, duty (t/h), tube material and economiser/superheater specifications — Fetch a waste-heat boiler OEM page or ammonia plant steam-balance reference.

## wastewater

### Wastewater treatment / process condensate (urea-wastewater-treatment)

Primary code: PCH: Petrochemicals
Wastewater treatment / process condensate
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| contamination mechanism | thermal decomposition products volatilize into overhead vapours and recombine on condensation, contaminating process condensate n/a | Wikipedia Urea side reactions (isocyanic acid + ammonia from ammonium cyanate) |
| scrubber water reuse | circulating water wash in granulator dust scrubber n/a | Toyo granulation clean emission section |


Recorded gaps:

- Effluent limits (NH3-N, urea, COD), treatment package vendor, steam consumption per m3, design flow — Fetch an effluent-treatment OEM or urea plant environmental specification page.
- Effluent limits (NH3-N, urea, COD), treatment package vendor, steam consumption per m3, design flow — Fetch an effluent-treatment OEM or urea plant environmental specification page.

## water-treatment

### Condensate polishing systems for HRSG / once-through boilers (filtration, ion exchange; conductivity/sodium ta (condensate-polishing-system)

Primary code: PWR: Power and renewables
Remove ionic and particulate contaminants (sodium, chloride, sulfate, silica, iron/copper oxides) from returned condensate and makeup before it reaches the boiler/steam generator, protecting boilers, turbines and HRSG evaporators from scaling, corrosion, hydrogen damage and turbine deposition (Graver; Chemical Engineering/ChemTreat).
Vendors: Graver Technologies, WOG Technologies Limited, Kurita Water Industries (Kurita ASEAN), Veolia Water Technologies, Purolite (Ecolab), Ion Exchange (India) Ltd, Ovivo (Christ Water Technology / Kennicott) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| makeup treatment effluent specific conductivity | <=0.1 µS/cm | recommended normal upper limit for final MBIX/EDI effluent; Chemical Engineering (ChemTreat), 2019 |
| condensate pump discharge cation conductivity (CACE) | <=0.2 µS/cm | recommended continuous CPD analysis for HRSG; Chemical Engineering (ChemTreat), 2019 |
| feedwater cation conductivity (AVT(O)) | <=0.2 µS/cm |  Chemical Engineering (ChemTreat) AVT(O) recommended limit for high-pressure steam generators |
| steam purity sodium / silica / CACE | Na <=2 ppb; SiO2 <=10 ppb; CACE <=0.2 µS/cm ppb / µS/cm | core steam purity monitoring parameters, Chemical Engineering (ChemTreat), 2019 |
| CPU outlet quality claimed by vendor | conductivity <0.2 µS/cm; silica <10 ppb µS/cm / ppb | WOG Technologies CPU FAQ, dependent on feed quality and design |
| Service pressure | ?-800 psi | Printed: 'designed to handle service pressures of up to 800psi' and in Advantages list 'Up to 800psi service pressure' |
| Flow rate | ?-50 gpm/sq.ft. | Printed in Advantages list: 'Up to 50 gpm/sq. ft. flowrate' |
| Cation:anion resin ratio for All Volatile Treatment (AVT) high pH | 2:1 ratio | Printed under Resin Optimization |
| Regeneration design | two-vessel SepraEight external regeneration n/a | Printed in page description |
| Resin | Gravex Bead Resin n/a | Printed under Resin Optimization |
| Contaminants removed | iron, copper, silica, salts, suspended solids n/a | Printed in page description |


Recorded gaps:

- Licensed primary EPRI/IAPWS tables for polisher outlet, drum HRSG and once-through HRSG action levels — Obtain EPRI 3002001381/TR-110051 or free IAPWS guidance and re-record targets with table numbers.
- Polisher resin bed depth, flow rate (BV/h), differential pressure and temperature limits — Download and parse the Graver/Purolite datasheets via local PDF tooling, recording exact model and basis.
-  Asia-Pacific refinery/petrochemical condensate polisher installations with named units and dates — Search utility tender awards and vendor press releases with plant name and commissioning year.

### Reverse osmosis (RO), electrodeionisation (EDI/CEDI) and demineralisation for boiler make-up; conductivity/sil (boiler-makeup-ro-edi)

Primary code: PWR: Power and renewables
Produce high-purity make-up water with very low dissolved solids, silica and CO2 to allow high cycles of concentration, low blowdown and safe operation of high-pressure drums and superheaters. RO is the main corrective pre-treatment after softening; EDI/CEDI polishes RO permeate without acid/caustic regenerants.
Vendors: Veolia Water Technologies, LANXESS, SUEZ Water Technologies (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| RO membrane element permeate recovery without fouling | 10-15 % of raw feed per membrane | CEA BG04 §2.9 (single membrane pass, no recirculation) |
| RO system recovery with concentrate recirculation | 75-85 % | CEA BG04 §2.9; achieved without significant fouling especially with softened feed |
| Optimum RO recovery with pre-softening | 75-80 % | CEA BG04 §2.10 balance of permeate quality and volume |
| Membrane useful life | 3-5 years | CEA BG04 §2.7 commercial-grade thin-film polymeric membranes; up to 10 years if feed is base-exchange softened |
| Example RO permeate TDS at 99% rejection of 400 ppm feed | 4 ppm | CEA BG04 §2.11 worked illustration (400 ppm raw feed, 99% rejection) |
| Terion S MkII salt rejection | >99.5 % | Veolia product page: combined high-pressure RO membranes and CEDI |
| Terion S MkII product water resistivity | up to 18 MOhm·cm | Veolia Terion S MkII product page |
| Terion S MkII flow-rate range | 110-4000 L/h | Veolia product page; 7 standard models, container-transportable |
| PROflex EDI footprint reduction | up to 40 % smaller than separate RO and EDI systems | Veolia PROflex EDI product page |
| Boiler-water silica limit — shell boiler | 150 max ppm | CEA BG04 Table 2; note 11 ratio of silica to caustic alkalinity <0.4:1 prevents silicate scale |
| Boiler-water dissolved solids (TDS) limit — shell boiler | 3500 max ppm | CEA BG04 Table 2 (or manufacturer's standard); coil boiler = manufacturer's standard |
| Conductance-to-TDS conversion | 0.7 TDS ppm per µS/cm at 25 °C | Spirax Sarco, Controlling TDS in the Boiler Water |
| Temperature coefficient of boiler-water conductivity | 2 % of the 25 °C value per 1 °C temperature rise | Spirax Sarco; automatic temperature compensation essential if pressure varies widely |
| Feedwater contaminant targets for 900 psig boiler (ASME consensus quoted by Veolia) | <7 ppb O2 / 20 ppb Fe / 15 ppb Cu ppb | Veolia Water Handbook Ch.11 quoting ASME Consensus for Industrial Boilers; pH 8.5–9.5 |
| Operating cost reduction vs mixed bed DI | 40-50 % lower | Printed claim on Graver ElectroFlex page: '40-50% lower operating costs when compared to mixed bed DI' |
| Floor space vs ion exchange demineralization | 50-75 % less | Printed claim under 'Operating Cost Savings' |
| Recycle of EDI reject to RO feed | 100 % recovery, zero waste production | Printed as a capability: 'Can be recycled upstream to the RO feed for 100% recovery, zero waste production' |
| Typical application | Power Generation: Steam makeup water n/a | Printed under Typical Applications |
| Membrane size/type | 8 x 40 in (TFC high rejection BW membranes) | Printed under 'Standard Design Features'; the page prints 'TFC 8”x40” high rejection BW membranes' |
| High pressure piping material | 316L SS sch. 40 n/a | Printed under Standard Design Features |
| Low pressure piping material | PVC sch. 80 n/a | Printed under Standard Design Features |
| Membrane vessel material | FRP, side-ported n/a | Printed under Standard Design Features |
| Motor supply | 460/60/3, TEFC V / Hz / phase | Printed under Standard Design Features as '460V/60HZ/3PH, TEFC motor' |
| Pump type | stainless steel vertical centrifugal pump n/a | Printed under Standard Design Features |
| Typical application | Boiler Water Make-Up n/a | Printed under Typical Applications |


Recorded gaps:

- Specific make-up-water conductivity/silica targets for HRSG high-pressure drums and once-through steam generators — Fetch ASME Consensus / EPRI guideline table or an OEM (GE Vernova, Siemens) HRSG water-chemistry datasheet and record drum-pressure-specific limits
- Siemens water-treatment product page — Fetch Siemens water treatment / RO-EDI product page and record vendor specs
- GE Vernova water chemistry guidance for HRSG — Fetch GE Vernova HRSG water-chemistry or service page

## weigh

### Weigh belts / beltweighers (bulk-weigh-belts)

Primary code: PCH: Petrochemicals
Weigh belts / beltweighers
Vendors: Topsoe (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| in-transit weighing | material flowing over the belt may be weighed in transit using a beltweigher n/a | Wikipedia Conveyor belt applications |


Recorded gaps:

- Belt scale accuracy class, capacity range, calibration method, OEM models (Schenck/Siemens etc.) — Fetch a verified weigh-belt OEM datasheet.
- Belt scale accuracy class, capacity range, calibration method, OEM models (Schenck/Siemens etc.) — Fetch a verified weigh-belt OEM datasheet.

## wh-wellhead

### Caisson platform / conductor-supported caisson (wh-caisson-platform-conductor-supported-caisson-csp)

Primary code: UPS: Upstream
Vertical large-diameter caisson(s) used as the substructure and often as conductor(s) for a small wellhead topside; cheaper and installable by jack-up rig.
Vendors: Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Vertical large-diameter caisson(s) used as the substructure and often as conductor(s) for a small wellhead topside; cheaper and installable by jack-up rig. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Design basis for caisson conductor support under ship impact and seismic loading — Fetch detailed design papers or classification notes.

### Chemical injection system (wh-chemical-injection-system-methanol-meg-scale-corrosion-inhibit)

Primary code: UPS: Upstream
Doses chemicals at the well or flowline to prevent hydrates, corrosion, scale, wax, foaming and demulsification problems.
Vendors: Johnson Controls (YORK, Silent-Aire), Petro Controls Europe BV, Veetech Automation FZE, ABB Wellhead Management System (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| hydrate prevention via kill wing valve | kill wing valve used primarily for injection of corrosion inhibitors or methanol to prevent hydrate formation qualitative | Wikipedia Christmas tree (oil well) |


Recorded gaps:

- MEG injection rates and hydrate inhibition design basis for a named field — Fetch flow assurance design paper or operator project paper.

### Christmas tree (wh-christmas-tree-surface-and-subsea)

Primary code: UPS: Upstream
Assembly of valves, spools and fittings mounted on the wellhead to control production or injection flow, provide chemical injection and intervention access, and monitor pressure/temperature/sand.
Vendors: OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems), Baker Hughes, CDI Oil & Gas (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| surface tree valve arrangement | basic: two or three manual gate valves; sophisticated: four or five valves in crucifix pattern with upper and lower master valves, production wing valve, kill wing valve (NASA in North Sea), swab valve configuration | Wikipedia Christmas tree (oil well), Valves section |
| hydraulic wing valve fail-safe mode | fail-safe closed; requires active hydraulic pressure to stay open qualitative | Wikipedia Christmas tree (oil well) |
| deepest installed subsea tree (as stated on page) | 9000 ft (2,700 m), approximately, Gulf of Mexico | Wikipedia Christmas tree (oil well) overview |
| subsea tree current technical limits (as stated on page) | -50-350 degrees F (-46 to 177 C); pressure up to 15,000 psi (100 MPa); water depth up to around 3,000 m | Wikipedia Christmas tree (oil well) overview |
| subsea tree mass range | 1-70 tons, approximately; up to about 70 tons for HPHT deepwater (>3,000 ft / 910 m) guidelineless trees | Wikipedia Christmas tree (oil well) |
| OneSubsea subsea tree temperature range | -18-176 degrees Celsius | OneSubsea subsea trees page |
| OneSubsea subsea tree pressure rating | ?-15000 psi (more than 1,000 bar), up to | OneSubsea subsea trees page |
| OneSubsea wellhead vertical tree production bore | 7 inch | OneSubsea subsea trees page, Features |
| TechnipFMC subsea tree ratings | ?-20000 psi; up to 400 F; up to 10,000 ft water depth | TechnipFMC subsea trees page |
| API specifications for tree valves | API Spec 6A (surface) and API Spec 17D (subsea) standard | Wikipedia Christmas tree (oil well), Valves section |
| ISO standard for wellhead/tree equipment | ISO 10423:2009 (also ISO 13628-4:2010 for subsea wellhead and tree equipment) standard | Wikipedia Wellhead and Christmas tree reference lists; ISO 13628-4:2010 from API international usage report |
| temperature range | -18-176 C | Overview |
| pressure | ?-15000 psi (>1000 bar) | Overview |
| production bore (wellhead vertical tree) | 7 inch | Features |
| Pressure | 15000 psi | Value as printed in the cited source; no further qualifier stated. |
| Flowing temperature | 350 deg F | Value as printed in the cited source; no further qualifier stated. |
| pressure | ?-20000 psi | Subsea trees page |
| temperature | ?-400 F | Subsea trees page |
| water depth | ?-10000 ft | Subsea trees page |
| Pressure | 20000 psi | Value as printed in the cited source; no further qualifier stated. |
| Temperature | 400 deg F | Value as printed in the cited source; no further qualifier stated. |
| Water depth | 10000 ft | Value as printed in the cited source; no further qualifier stated. |
| standards for welding | API 6A, 17D, ASME Section IX, NACE MR0175/ISO 15156, DNVGL-RP-C203 F3/D/C1 standard list | Application section of fetched page |


Recorded gaps:

- Reconciliation of deepest-tree records (9,000 ft Wikipedia vs 9,627 ft TechnipFMC) — Fetch original source cited by Wikipedia and TechnipFMC record press release.

### Conductors, conductor guides and subsea templates (wh-conductors-conductor-guides-and-subsea-templates)

Primary code: UPS: Upstream
Protect and guide the drill string and well casing from topside to below the mudline; a subsea template guides conductors before jacket installation and may group several wells.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| conductor function and depth below seabed | 40-100 m below sea bottom | ESDEP glossary: tubular protecting and guiding drill string from topside down to 40-100 m under sea bottom; after drilling protects well casing |
| conductor size protected by jacket | 26-30 inch | ESDEP 15A.1 section 4.1 |


Recorded gaps:

- Conductor centralizer and guide bushing standard sizes/loads from an OEM — Fetch OEM conductor guide and template product pages.

### Downhole safety valve (wh-downhole-safety-valve-dhsv-sssv-scssv)

Primary code: UPS: Upstream
Fail-safe downhole barrier that isolates reservoir fluids at surface if wellhead/tree containment is lost.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| typical valve mechanism | uni-directional flapper valve which opens downwards; hydraulic pressure from surface opens against a spring; loss of pressure closes it qualitative | Wikipedia Downhole safety valve, Operation section |
| minimum setting depth below mudline (MMS regulation) | 100 ft (30 m) | Wikipedia Downhole safety valve, Positioning section, citing MMS regulations |
| control method | hydraulically controlled from surface via a control line linked to a well control panel qualitative | Wikipedia Downhole safety valve |
| legal status in United Kingdom | not a direct legal requirement; 1974 Health & Safety at Work Act requires prevention of uncontrolled release, so DHSVs are company policy for many UKCS operators regulatory context | Wikipedia Downhole safety valve, Legal requirement section |


Recorded gaps:

- OEM DHSV pressure ratings, bore sizes and metallurgy — Fetch OEM subsurface safety valve product sheets.

### Fire and gas, deluge and ESD/HIPPS (wh-fire-and-gas-deluge-and-esd-hipps)

Primary code: UPS: Upstream
Detect fire and gas, mitigate fire escalation with water deluge, and shut down or blow down the installation safely.
Vendors: Johnson Controls (YORK, Silent-Aire) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Detect fire and gas, mitigate fire escalation with water deluge, and shut down or blow down the installation safely. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Installation-specific F&G voting logic and deluge coverage density — Fetch safety case or F&G philosophy documents.

### Fixed jacket wellhead platform (wh-fixed-jacket-wellhead-platform)

Primary code: UPS: Upstream
A fixed, pile-founded tubular steel substructure supporting a topside that houses wellheads, Christmas trees, well control and minimum processing; the wells are drilled and completed from the platform.
Vendors: TechnipFMC (CDS Separation Systems), Aquaterra Energy, OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
|  economically feasible water depth (fixed platforms generally) | 500 m (about 150 m cited on Fixed platform page) | Fixed platforms economically feasible up to about 500 feet (150 m); Oil platform page separately states up to about 520 m (1,710 ft) — conflicting figures between two fetched pages, neither preferred |
| jacket function | braced tubular steel substructure; supports laterally and protects well conductors and pipeline riser qualitative | ESDEP lecture 15A.1 section 4.1 |
| well conductor size protected by jacket | 26-30 inch | ESDEP lecture 15A.1 section 4.1 |
| typical air gap (topside clearance above maximum wave) | 1.5 m (approximately) | ESDEP lecture 15A.1 section 2.2; to be increased if reservoir depletion causes subsidence |
| applicable structural standard | API RP 2A (worldwide leading code); ISO 19902:2020; DNV rules; AISC and AWS D1.1 for topsides and welding standard designation | ESDEP 15A.1 section 2.4 and references; ISO 19902:2020 abstract (search-verified) |
| reboiler heat media | gas fired, hot oil or steam list | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| inlet mercury | 1-10 ug/Nm3 (0.1-10 ppbv) ug/Nm3 | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| design outlet | 0.001 ug/Nm3 ug/Nm3 | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| scope | HPU, methanol injection skids, WHCP, TUTU, IWOCS, ESD, HIPPS product list | Production Systems page |
| Depth | 500 m | Value as printed in the cited source; no further qualifier stated. |
| Power | 1125 kW | Value as printed in the cited source; no further qualifier stated. |
| Burial capacity | 3 m | Value as printed in the cited source; no further qualifier stated. |
| SIL | 1-3 (IEC 61508/61511) SIL | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| operating temperature | -40 to 70 degC remote cabinet; -5 to 70 degC cabinet degC | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| supply voltage | 110/48/24 VDC VDC | As printed on the manufacturer page/data sheet at the product url; page read with WebFetch |
| AMP1500 product diameter | 1500 mm | Value as printed in the cited source; no further qualifier stated. |
| ACP2 product diameter | 300 mm | Value as printed in the cited source; no further qualifier stated. |


Recorded gaps:

- Current edition/date of API RP 2A (WSD and LRFD) and its exact status versus ISO 19902 — Fetch API standards catalogue pages for RP 2A-WSD and RP 2A-LRFD current editions.

### Flare boom / flare stack (wh-flare-boom-flare-stack)

Primary code: UPS: Upstream
Safely combust waste gas during normal operation and emergencies; height/length set by radiation and noise limits.
Vendors: Tai Crest Resources (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Safely combust waste gas during normal operation and emergencies; height/length set by radiation and noise limits. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Flare tip diameter, radiation limit and stack height for a specific WHP — Fetch flare design paper or project specification.

### Helideck, bridge link and accommodation/control rooms (wh-helideck-bridge-link-and-accommodation-control-rooms)

Primary code: UPS: Upstream
Provides helicopter landing and personnel transfer, a safe bridge connection between platforms, and living quarters/control room spaces.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provides helicopter landing and personnel transfer, a safe bridge connection between platforms, and living quarters/control room spaces. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Detailed helideck D-value, load classification and obstacle-free sector requirements — Fetch full CAAP 71 PDF and extract section 5 tables.

### Hydraulic and control lines, umbilicals (wh-hydraulic-and-control-lines-umbilicals)

Primary code: UPS: Upstream
Carry hydraulic power, electrical power, signals and chemicals between the surface control system and subsea/downhole devices.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| OneSubsea umbilical product lines | steeltube umbilicals, power umbilicals and cables, integrated production umbilicals, direct electrical heating systems product list | OneSubsea subsea umbilical systems navigation on fetched wellhead/trees pages |


Recorded gaps:

- Umbilical tube count, conductor cross-sections and design pressure for a named project — Fetch an OEM umbilical datasheet.

### J-tubes, guide tubes and bend restrictors/stiffeners (wh-j-tubes-guide-tubes-and-bend-restrictors-stiffeners)

Primary code: UPS: Upstream
Guide, protect and control curvature of flexible risers, umbilicals and cables at platform and subsea terminations.
Vendors: CRP Subsea (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Guide, protect and control curvature of flexible risers, umbilicals and cables at platform and subsea terminations. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- MBR and design load tables for specific bend restrictor models — Retry CRP page or fetch range sheet PDF.

### Jacket substructure and pile foundation (wh-jacket-substructure-and-pile-foundation)

Primary code: UPS: Upstream
Transfers topside and environmental loads to the seabed; piles are driven through jacket legs or skirt sleeves and fixed by grouting, welding or swaging.
Vendors: Sika, CAPE Holland (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| open-ended tubular steel pile diameter | ?-2 m (up to) | ESDEP 15A.1 section 4.2 |
| pile penetration | 40-80 m; in some cases 120 m | ESDEP 15A.1 section 4.2 |
| sacrificial anode mass | 3 kN each, approximately | ESDEP 15A.1 section 4.4; zinc/aluminium bar cast about a steel tube and welded to structure |
| anode mass as fraction of jacket weight | 5 % typically | ESDEP 15A.1 section 4.4 |
| splash zone corrosion allowance | 12 mm sacrificial wall thickness | ESDEP 15A.1 section 4.4 |


Recorded gaps:

- Current API RP 2A pile design equations and fatigue criteria — Fetch API preview or ISO 19902 OBP sample.

### Landing nipples and packers (wh-landing-nipples-and-packers)

Primary code: UPS: Upstream
Provide downhole loci for wireline tools/valves and isolate annuli or zones within the completion.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Provide downhole loci for wireline tools/valves and isolate annuli or zones within the completion. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Named landing nipple and packer products with bore, pressure rating and setting depth — Fetch completion equipment catalogs (e.g. packer and nipple datasheets) and add specs.

### Manifolds and piping (wh-manifolds-and-piping-production-test-injection)

Primary code: UPS: Upstream
Gather flow from multiple wells, route to production/test headers, distribute injection fluids and chemicals, and provide isolation and pigging interfaces.
Vendors: Baker Hughes, OneSubsea (SLB/Aker Solutions JV), Deepsea Technologies, Inc. (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Gather flow from multiple wells, route to production/test headers, distribute injection fluids and chemicals, and provide isolation and pigging interfaces. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Design pressure/temperature of named manifold models — Fetch full Baker Hughes catalog or datasheet pages.

### Master valves, wing valves, choke valves and actuators (wh-master-valves-wing-valves-choke-valves-and-actuators)

Primary code: UPS: Upstream
Provide well isolation, flow routing, flow control and remote/fail-safe actuation on trees and manifolds.
Vendors: Hydropneumatic S.r.l., TechnipFMC (CDS Separation Systems) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| master valve operating practice | normally fully open; never opened or closed while well is flowing except in emergency, to prevent erosion of sealing surfaces operating rule | Wikipedia Christmas tree (oil well) |
| lower master valve operation | manually operated; upper master valve often hydraulically actuated for remote shut-in configuration | Wikipedia Christmas tree (oil well) |
| actuated wing valve | normally used to shut in the well when flowing; built fail-safe closed configuration | Wikipedia Christmas tree (oil well) |


Recorded gaps:

- Valve bore sizes, Cv and actuator thrust for specific tree models — Fetch named OEM gate valve and choke datasheets.

### Minimal / satellite / conductor-supported wellhead platform (wh-minimal-satellite-conductor-supported-wellhead-platform)

Primary code: UPS: Upstream
Low-cost unmanned wellhead platform, often supported directly by the well conductors, used for marginal fields and step-outs tied back to a host facility by flowline or umbilical.
Vendors: Aquaterra Energy, 2H Offshore, Synergy Engineering (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| description from Oil platform article | small unmanned platforms consisting of little more than a well bay and a small process plant; operate with a static production platform connected by flow lines or umbilical qualitative | Wikipedia Oil platform, Conductor support systems section |


Recorded gaps:

- Detailed conductor size/grade and fatigue design factors for each minimal platform — Fetch project PDFs or papers via operator/EPC sites.

### Mobile wellhead units / MODU-served wellhead (wh-mobile-wellhead-units-modu-served-wellhead)

Primary code: UPS: Upstream
Wellheads and trees served from a mobile offshore drilling unit or intervention vessel instead of a permanent platform; includes subsea wellheads tied back to a host.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| jack-up rig depth range for exploration wells | 100-120 m | ESDEP 15A.1 section 3.1 |
| offshore wellhead location terminology | surface wellhead on production platform; subsea/mudline wellhead below water qualitative | Wikipedia Wellhead |


Recorded gaps:

- Named mobile wellhead unit products and their ratings — Search OEM catalogs for riserless/mobile wellhead systems and fetch.

### Pig traps and pigging loops (wh-pig-traps-and-pigging-loops)

Primary code: UPS: Upstream
Launch and receive pigs to clean or inspect flowlines between manifold and platform.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Launch and receive pigs to clean or inspect flowlines between manifold and platform. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Pig trap pressure class, size and supplier for a named platform — Fetch pig trap/pigging system OEM datasheet.

### Platform utilities: cranes, lifeboats, power generation, HVAC and drainage (wh-platform-utilities-cranes-lifeboats-power-generation-hvac-and)

Primary code: UPS: Upstream
Support safe operation and habitation: lifting, evacuation, electrical power, environmental control and liquid drainage.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| major offshore crane vessel lifting capacity | 1600-14000 tonnes (table of vessels from ESDEP, historical) | ESDEP 15A.1 Table 1; e.g. Hermod 8,164 t fixed dual crane, Micoperi M7000 14,000 t revolving dual crane |
| heaviest sling breaking load and SWL | approximately 350 mm diameter; breaking load approximately 48 MN; safe working load 16 MN; shackles up to 10 MN SWL mm / MN | ESDEP 15A.1 section 7.3.2 |
| AMAL-C local power generation | two diesel generators, one providing emergency back-up generator count | Aquaterra AMAL-C case study |


Recorded gaps:

- Named platform crane and lifeboat models with capacities — Fetch OEM datasheets for pedestal cranes and enclosed lifeboats.

### Risers (wh-risers-top-tensioned-flexible-scr)

Primary code: UPS: Upstream
Convey production/injection fluids between subsea wellheads/manifolds and the host platform or floating facility.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Convey production/injection fluids between subsea wellheads/manifolds and the host platform or floating facility. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Actual riser diameters, wall thicknesses and tensioner ratings for named installations — Fetch project-specific riser papers.

### Tender-assisted drilling (wh-tender-assisted-drilling-tad-wellhead-platform)

Primary code: UPS: Upstream
Wellhead platform where drilling facilities and accommodation are provided by an adjacent tender vessel or barge rather than being permanently installed on the platform.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| function | Wellhead platform where drilling facilities and accommodation are provided by an adjacent tender vessel or barge rather than being permanently installed on the platform. | Qualitative function from pages read in this sweep. |


Recorded gaps:

- Absolute topside/jacket weights for a representative TAD WHP — Fetch operator or yard project sheets for a TAD WHP.

### Topsides decks and module support frame (wh-topsides-decks-and-module-support-frame-msf)

Primary code: UPS: Upstream
Carries wells, process equipment, utilities, accommodation and helideck; either a single integrated deck lifted in one piece or a module support frame carrying multiple modules.
Vendors: OneSubsea (SLB/Aker Solutions JV) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| integrated deck weight limit | ?-100 MN, approximately (about 10,000 tonnes) | ESDEP 15A.1 section 5.2.1 |
| modularized topside weight range | 200-400 MN | ESDEP 15A.1 section 5.2.3 |
| equipment module weight range | 20-75 MN | ESDEP 15A.1 section 6 |
| living quarter module weight range | 5-25 MN | ESDEP 15A.1 section 6 |
| deck leg support elevation | 4-6 m above Low Astronomical Tide | ESDEP 15A.1 section 5.2.2; down to top of piles |
| topside installed CAPEX (historical) | 20 ECU/kg, approximately | ESDEP 15A.1 section 9.1; historical figure, NOT a current USD cost |


Recorded gaps:

- Current topside structural steel design code (API 2TOP vs AISC) and load factors — Fetch API 2TOP preview and ISO 19901-3 scope.

### Unmanned wellhead platform (wh-unmanned-wellhead-platform-uwhp)

Primary code: UPS: Upstream
Normally unmanned installation with well bay, minimal facilities, remote operation and occasional visit for maintenance or well work.
Vendors: Shell Malaysia Exploration and Production (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| definition of NUI | small platforms consisting of little more than a well bay, helipad and emergency shelter; operated remotely under normal conditions qualitative | Wikipedia Oil platform, Normally Unmanned Installations section |


Recorded gaps:

- W2W transfer criteria and manning model for UWHPs — Fetch full SODIR PDF.

### Wellhead assembly (wh-wellhead-assembly-casing-head-casing-spools-tubing-head-hanger)

Primary code: UPS: Upstream
Provides structural suspension and pressure seals for casing and tubing strings, annulus monitoring/pumping access, BOP attachment during drilling and Christmas tree attachment during production.
Vendors: OneSubsea (SLB/Aker Solutions JV), TechnipFMC (CDS Separation Systems), OMS (Oilfield Manufacturers and Supplies), CAMTOP Oilfield Tools, Cameron (SLB) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| primary component list | casing head, casing spools, casing hangers, choke manifold, packoffs, test plugs, mudline suspension systems, tubing heads, tubing hangers, tubing head adapter component list | Wikipedia Wellhead, Components section |
| nominal pressure ratings (general wellheads) | 2-15 x1000 psi working pressure (i.e. 2,000-15,000 psi); five ratings: 2, 3, 5, 10, 15 | Wikipedia Wellhead, Design specification section |
| operating temperature range (general) | -50-250 degrees Fahrenheit | Wikipedia Wellhead, Design specification section |
| material yield strength range | 36000-75000 psi | Wikipedia Wellhead, Design specification section |
| subsea wellhead primary barrier statement | Wellheads are the primary pressure barrier for a subsea well; anchor and suspension point and seal element for casing strings qualitative | OneSubsea subsea wellheads page |
| welding/qualification standards cited by OneSubsea | API Spec 6A and 17D, ASME Section IX, NACE MR0175/ISO 15156, DNVGL-RP-C203 fatigue classes F3, D or C1 standard list | OneSubsea subsea wellheads page, Application section |


Recorded gaps:

- API 6A 21st edition full pressure/temperature derating table and PSL minimums by material class — Fetch full SLB API 6A brochure PDF and exal technology PDF.

### Wellhead control panel and surface control system (wh-wellhead-control-panel-and-surface-control-system-whcp)

Primary code: UPS: Upstream
Controls and monitors surface and subsurface valves, choke, ESD and fire/gas functions for one or multiple wells from a local or remote panel.
Vendors: Johnson Controls (YORK, Silent-Aire), Hydropneumatic S.r.l., FST, IPS Group BV, INTECH Automation & Intelligence, Hitec Products AS (NORWEP listing) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Johnson Controls product scope | HPU, chemical/methanol injection skids, WHCP, TUTU, IWOCS, ESD and HIPPS; integrator for API 674 and API 675 pump packages product list | Johnson Controls Production Systems page |


Recorded gaps:

- WHCP response times and hydraulic pressure settings for specific projects — Fetch project datasheets with performance standards.

### Wireline, coiled tubing and snubbing/workover equipment (wh-wireline-coiled-tubing-and-snubbing-workover-equipment)

Primary code: UPS: Upstream
Provide well access for logging, fishing, cleanout, pumping, completions and interventions from the wellhead platform or an intervention vessel.
Vendors: NOV (Bondstrand), Halliburton, Balance Point Control (BPC), International Snubbing Services (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| coiled tubing diameter | 1-3.25 inch (25 to 83 mm) | Wikipedia Coiled tubing |
| common coiled tubing steel yield strength | 55000-120000 psi | Wikipedia Coiled tubing |


Recorded gaps:

- Deck load/footprint and crane limits for CT and snubbing spreads on small WHPs — Fetch rig-up drawings or intervention engineering papers.

## whp-control-safety-comms

### Condition monitoring instrumentation (whp-condition-monitoring-instrumentation)

Primary code: UPS: Upstream
Wireless and wired instrumentation monitors annulus/wellhead pressure and structural vibration to cut manual rounds and detect integrity issues early; LoRaWAN battery-powered sensors suit unmanned offshore wells.
Vendors: Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Yokogawa Sushi Sensor wireless pressure  — Gateway distance in cited case | 4 km | wireless pressure sensor at wellhead equipment to a gateway located approximately 4 km away; maximum distance varies with environment |
| Yokogawa Sushi Sensor wireless pressure  — Data collection interval | 1-? qualitative | intervals ranging from one minute to three days (low in minutes, high in days) |
| Reliability — Pressure monitoring frequency | 1-? qualitative | one minute to three days, more frequent than traditional operator rounds |
| Price — 4-20 mA wellhead pressure transmitter (onshore proxy) | 300-800 USD | Quality oilfield pressure transmitters from major industrial instrumentation manufacturers; US onshore guide dated 6 May 2026; dollar year 2026. |


Recorded gaps:

- Annulus pressure monitoring — Fetch an OEM annulus sensor datasheet with printed range and accuracy
- Vibration monitoring — Source a vendor datasheet with printed frequency range and sensitivity
- Condition monitoring cost — Obtain a USD quotation with scope basis

### ESD (whp-esd)

Primary code: UPS: Upstream
ESD is a safety instrumented system that drives the wellhead control panel and shutdown valves to a safe state. Offshore Norge recommended guidance assigns SIL 3 to isolation of the production/injection bore of a topside well; US OCS rules require de-energize-to-trip or supervised ESD stations.
Vendors: Offshore Norge (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| ESD logic (wellhead control panel) incl. — Required SIL - ESD isolation of production/injection bore in one topside well | 3 SIL | Table A.6.5 Summary of SIL requirements - Isolation of topside well functions |
| Reliability — Required SIL - ESD isolation of production/injection bore | 3 SIL | Offshore Norge guideline No. 070 rev 06, Table A.6.5 |
| Reliability — Required SIL - ESD isolation of annulus in one topside gas lift well | 3 SIL | Offshore Norge guideline No. 070 rev 06, Table A.6.5 |


Recorded gaps:

- ESD with dual redundant logic — Obtain a named WHP cause-and-effect matrix and SIS architecture diagram
- ESD SDV valves — Find an accessible copy and extract the closing sequence, PST and proof-test interval
- ESD SDV valves — Source a priced ESD package with dollar year

### Fire and Gas (whp-fire-and-gas)

Primary code: UPS: Upstream
F&G detection covers flame (UV/IR), smoke, heat, combustible/toxic gas and pneumatic fusible plug loops, interfaced to deluge, ESD, PAGA and the ICSS. Offshore Norge assigns SIL 2 to single-detector fire and gas detection sub-functions.
Vendors: Consilium Safety (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Consilium CS-PH Ex programmable intrinsi — PFDavg | 0.00029 dimensionless | PFDavg 2.9 x 10^-4; calculated for MTTR 8 h and proof test interval 1 year |
| Consilium CS-PH Ex programmable intrinsi — Safe failure fraction | 92 % | Functional Safety Data: Type B, HFT 0, SFF 92 % |
| Consilium CS-PH Ex programmable intrinsi — Operating voltage | 16-38 VDC | Operating voltage 16-38 VDC |
| Consilium CS-PH Ex programmable intrinsi — Proof test interval used in PFD calculation | 1 year | PFDavg is calculated for MTTR 8 h and proof test interval 1 year |
| Consilium CS-PH Ex programmable intrinsi — SIL certification | 2 SIL | SIL Certificate no. TUV NORD 44 788 13082116; SIL 2 certified according to IEC 61508; suitable for SIL 1 and SIL 2 |
| F&G logic and detector sub-functions (1o — Fire detection total PFD - smoke | 0.0019 dimensionless | Table A.8.1 total for function: Smoke 1.9 x 10^-3 (detector 7.0 x 10^-4 + F&G logic 1.2 x 10^-3) |
| F&G logic and detector sub-functions (1o — Fire detection total PFD - heat | 0.0028 dimensionless | Table A.8.1 total for function: Heat 2.8 x 10^-3 (detector 2.2 x 10^-3 + logic 1.2 x 10^-3) |
| F&G logic and detector sub-functions (1o — Fire detection total PFD - flame | 0.0027 dimensionless | Table A.8.1 total for function: Flame 2.7 x 10^-3 (detector 1.5 x 10^-3 + logic 1.2 x 10^-3) |
| Reliability — PFDavg | 0.00029 dimensionless | Consilium CS-PH Ex, MTTR 8 h, 1-year proof test interval |
| Reliability — F&G logic PFD (single I/O, redundant CPU) | 0.0012 dimensionless | Offshore Norge Table A.8.1, voting 1oo1 |
| Reliability — Required SIL - fire detection with one detector | 2 SIL | Offshore Norge section A.7: fire detector (heat, flame or smoke) + F&G logic incl I/O |
| Reliability — Required SIL - gas detection with one detector | 2 SIL | Offshore Norge section A.8.1: catalytic, IR point, IR line or H2S detector + F&G logic incl I/O |


Recorded gaps:

- Fusible plug loops — Find an accessible OEM datasheet with printed fusible element rating
- F&G detector coverage on a WHP — Locate a published F&G mapping result with basis
- F&G system cost — Source a USD quote with dollar year and scope basis

### Navigation aids (whp-navigation-aids)

Primary code: UPS: Upstream
Offshore structures are marked as a single unit, block or field under IALA G1162: white main/secondary lanterns flashing Morse U, red subsidiary lights, ID panels, fog signals, racon and optional aviation obstruction lighting.
Vendors: MSM Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Main and secondary marine lanterns (IALA — Main/secondary light range | 10 nautical miles | Intensity range 10 nm (main and secondary lights) |
| Main and secondary marine lanterns (IALA — Subsidiary light range | 3 nautical miles | Flashing red light, Morse U every 15 secs, intensity range 3 nm |
| Fog signal (main/secondary) — Main sound range | 2 nautical miles | Sound range 2 nm in any direction (MAIN) |
| Fog signal (main/secondary) — Secondary sound range | 0.5 nautical miles | Minimum sound range 1/2 nm in any direction (SECONDARY) |
| Fog signal (main/secondary) — Independent power autonomy | 96 h | Autonomy 96h for a power source independent |
| Phalcon-EX-SS Zone 1 racon — Weight | 20 kg | Mechanical Specification: Weight 20 kg |
| Phalcon-EX-SS Zone 1 racon — Input voltage | 9-36 VDC | Electrical Specification: Input Voltage 9-36V DC |
| Phalcon-EX-SS Zone 1 racon — Average power | 3 W | Average Power 3W, based on traffic |
| Phalcon-EX-SS Zone 1 racon — Antenna gain | 3-5 dBi | Antenna Gain: X-band 5dBi, S-band 3dBi |
| Zone 1 Nav Aid Skid System — Battery backup autonomy | 96 h | Skid includes 10NM lantern, 2NM/0.5NM fog signal, fog detector and battery backup; calculated autonomy of 96 hours |
| Zone 1 Nav Aid Skid System — FA-250 10NM lantern power | 3.33 W average | FA-250 10NM: 20W LED array providing flashing 10NM Morse U white light; Average power 3.33W |
| Zone 1 Nav Aid Skid System — ICAO Type A obstruction light | 3 W DC | ICAO TYPE A: 3W DC, 3.5W AC, 10cd, Red LED array aviation light |
| Reliability — Independent power autonomy | 96 h | IALA G1162 main/secondary fog signal autonomy for independent power source |


Recorded gaps:

- Navigation aids — Find an operator AtoN schedule with printed ranges and autonomy
- Navigation aids — Obtain a priced skid quotation with dollar year

### Platform telecom: VHF/UHF radio, satellite communication (whp-platform-telecom-vhf-uhf-radio-satellite-communication)

Primary code: UPS: Upstream
Offshore telecom combines terrestrial two-way radio (VHF/UHF, DMR/P25), satellite voice and VSAT broadband, safety-critical public address/general alarm, CCTV and cyber-secured links back to shore.
Vendors: VMD Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Offshore satellite broadband (Ku-band Gl — Broadband data speed | 300-? Mbps | High Data Speeds Internet (over 300Mbps) service using the Ku band Global Xpress technology |


Recorded gaps:

- PA/GA system — Fetch OEM datasheets and extract printed sound coverage basis
- VSAT on WHP — Source an operator service sheet with availability and dollar year
- CCTV — Locate a project CCTV specification with Ex certification

### Process control and monitoring via SCADA/DCS, remote from shore or hub platform (whp-process-control-and-monitoring-via-scada-dcs-remote-from-shore-or-hub)

Primary code: UPS: Upstream
Minimum-facility WHPs are normally unmanned; supervisory control gathers wellhead/process data to a hub platform or onshore centre over radio, cellular, fibre or satellite links. Control loops stay in local PLC/RTU, with SCADA as supervisory layer; safety functions are implemented in a separate SIS.
Vendors: Rockwell Automation, AVEVA, Yokogawa Electric (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Tatsoft FrameworX SCADA/IIoT — Native connectors included in licence | 120-? connectors | more than 120 connectors are included in the license |
| Tatsoft FrameworX SCADA/IIoT — Router-embedded deployment scale | 300-? sites | A large United States oil and gas operator runs FrameworX inside Cisco industrial routers at more than 300 production sites, onshore and offshore |
| Rockwell ICSS on wellhead platforms (Con — Safety integrity capability | 2-3 SIL | Safety instrumented systems for SIL 2 and SIL 3 functions on AADvance and Trusted, including ESD and Fire & Gas |
| Price — Wellhead monitoring installed hardware per well (onshore proxy, NOT offshore WHP) | 3000-8000 USD | US onshore Permian wellhead monitoring hardware: two pressure transmitters, temperature sensor, cellular gateway, panel, solar/battery, install labour; vendor guide dated 6 May 2026; dollar year 2026. |
| Price — Upfront implementation, traditional on-premise SCADA for 10 wells (onshore proxy) | 80000-200000 USD | vendor guide dated 6 May 2026; onshore US, not an offshore platform quote; dollar year 2026. |


Recorded gaps:

- Process control and monitoring via SCADA/DCS — Find a named offshore WHP automation contract with USD value and dollar year
- Process control and monitoring via SCADA/DCS — Source a printed latency/availability specification with basis

## whp-production-process

### Chemical injection system (whp-chemical-injection-system)

Primary code: UPS: Upstream
Chemical injection skids dose inhibitors into the well stream or flowline to maintain flow assurance, separation performance and asset integrity. SPEC describes a 'Skid with dosing pumps and tank that injects chemicals into the process' supplied with the process equipment or standalone. The kill wing valve on a tree is primarily used to inject corrosion inhibitors or methanol to prevent hydrate formation. Digital Refining (PTQ, Jul-2015) states EG is considered above -40 degF and methanol for te
Vendors: ChampionX, Clariant (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Chemical injection skid (dosing pumps an — Methanol / EG hydrate-inhibition regime | -140--40 degF | Digital Refining article: 'EG can be considered when downstream processing temperatures are not excessively low (above -40°F), and methanol is adequate for much lower downstream processing temperatures (as low as below -140°F)'. Low is a printed 'below -140 degF' qualifier, high is 'above -40 degF' qualifier. |
| Methanol injection pump and timer packag — Methanol dose volume per pump cycle | 10 cc | US6981848B1: 'a selected quantity of methanol, e.g., 10 cc, may be pumped from the storage tank 12 to the pipeline 14 each time the pump is cycled' |
| Methanol injection pump and timer packag — Timer interval | 7 s | US6981848B1: 'Timer 18 may be set by the operator to cycle the pump in a selected time interval of, for example, 7 seconds' |
| Methanol injection pump and timer packag — Control battery voltage | 4.5 V DC | US6981848B1: timer, motor, controller and sensors 'may all be powered by a conventional 4.5-volt DC battery 40' |
| Methanol injection pump and timer packag — Line temperature activation setpoint | 30 degF | US6981848B1: controller may open valve when line sensor drops below 30 degF, or ambient sensor below 28 degF (ambient value separately reported) |
| Methanol injection pump and timer packag — CIMV ultrasonic flow meter range | 0.5-26500 L/h | WO2016067222A1: 'an ultrasonic flow meter 20 configured to measure a range of flow rates between approximately 0.5 liters per hour to 26,500 liters per hour, or more' |


Recorded gaps:

- MEG/methanol injection rates and hydrate-inhibition design basis for a named WHP — Fetch a named field design paper and record rates with basis
- Storage tank sizes and dosing pump turndown for a named WHP chemical injection package — Fetch OEM datasheet and record printed ranges
- Capital/operating cost of chemical injection system — Record with dollar year and scope basis only when a source is read

### Chokes and choke manifolds (whp-chokes-and-choke-manifolds)

Primary code: UPS: Upstream
Choke valves and choke manifolds provide well isolation, flow routing and flow control on trees and manifolds. A choke is described as the smallest restriction in a Christmas tree, used to control production rate (and in some cases sand production), with two types: positive chokes with interchangeable beans and adjustable chokes. Master valves are normally fully open and not operated while flowing; the lower master is normally manual, the upper often hydraulically actuated for remote shut-in, an
Vendors: TechnipFMC (CDS Separation Systems), Aker Solutions, Velan, Flowserve (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Choke valve (positive/bean and adjustabl — Conventional choke-manifold circuit arrangement | 2 choke circuits | US20120273228A1 background: conventionally 'at least two choke circuits in which two adjustable chokes are arranged such that one adjustable choke may be isolated and taken out of service for repair and refurbishment while well flow is directed through the other' |
| Choke valve (positive/bean and adjustabl — Series subsea production choke pressure-difference capability | 4500-5500 psi | WO2008045381A2 claims 5-6: difference between well pressure and riser pressure 'greater than 4500 psi' / 'greater than 5500 psi'; patent states pressure difference between chokes typically less than 4000 psi, more typically less than 2500 psi |
| Choke valve (positive/bean and adjustabl — Combined choke flow coefficient range (two chokes in series) | 0.05-1.2 GPM*psi^0.5 | WO2008045381A2 claim 9: 'combined range of Cv of between 1.2 and 0.05 GPM*psi0 5' (most preferred 1.0 to 0.1 in claim 10) |


Recorded gaps:

- Choke valve bore sizes, Cv and actuator thrust for named tree models — Fetch datasheets and record printed ranges with basis
- Failure rate (per demand/hour) and proof-test interval for production chokes — Record numeric rates only from a page actually read

### Closed drain system and open/slop drain with sump caisson (whp-closed-drain-system-and-open-slop-drain-with-sump-caisson)

Primary code: UPS: Upstream
Drainage is part of platform utility scope alongside lifting, evacuation, power and environmental control. No primary page describing closed drain, open/slop drain and sump caisson design for a WHP was read in this sweep; the HILIR tech library has an equipment record ('Platform utilities: cranes, lifeboats, power generation, HVAC and drainage') whose cited pages were about crane vessels and a Gulf of Suez jacket case study, not drain design. Recorded as a gap rather than an estimate.
Vendors: American Petroleum Institute (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| List membership | Recorded from the Mistral-chat WHP component list n/a | Item listed in the source chat; no numeric specification was found in the pages read. |


Recorded gaps:

- Closed drain system design basis — Fetch an open design basis or standards preview and record pressure, turndown and routing with basis
- Open/slop drain and sump caisson sizing — Fetch a named design paper and record dimensions/capacity
- Drain system failure rates, availability and proof-test interval — Record numeric data only from a page actually read
- Drain system cost — Find cost with dollar year and basis

### Export risers and subsea pipeline tie-ins to the CPP or FSO (whp-export-risers-and-subsea-pipeline-tie-ins-to-the-cpp-or-fso)

Primary code: UPS: Upstream
Rigid flowlines and export pipelines carry oilfield fluids from wellhead/manifold to the processing facility and from offshore facilities to onshore receiving terminals; risers accommodate vessel motion and environmental loads between seabed flowlines/PLET and the surface host. TechnipFMC lists single pipelines, plastic-lined pipelines, corrosion-resistant alloy pipelines, direct electrically heated pipelines, pipe-in-pipe, electrically trace-heated pipe-in-pipe, piggybacked pipelines, steel cat
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, Aker Solutions, American Bureau of Shipping (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Rigid flowlines, export pipelines and tr — Rigid pipeline diameter range | 4-18 inch | TechnipFMC rigid pipelines: 'range from small diameter 4-inch pipes for oilfield service fluids, to 18-inch infield lines, to larger diameter export trunk lines connecting offshore processing facilities to onshore receiving facilities' |
| Rigid flowlines, export pipelines and tr — Installed pipe-in-pipe length (company track record) | 1100 km | TechnipFMC: 'more than 1,100 kilometers of installed pipe-in-pipe' (value recorded as 1100 with 'more than' qualifier) |


Recorded gaps:

- Actual riser diameters, wall thicknesses and tensioner ratings for a named WHP/FSO tie-in — Fetch project-specific riser paper and record printed dimensions
- Riser/pipeline failure rate or availability for WHP export systems — Record numeric reliability only from a page actually read

### Pig launcher / receiver for the export pipeline (whp-pig-launcher-receiver-for-the-export-pipeline)

Primary code: UPS: Upstream
Pig traps launch and receive pigs to clean or inspect flowlines between manifold and platform / along export pipelines. SPEC Oil & Gas lists pig launchers and receivers among its ancillary equipment (page read). Patent US4135949A describes the safety interlock problem: inadvertent opening of a pressurised receiver or admission of fluid while the closure is off is a hazard to personnel and the environment.
Vendors: Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pig launcher / receiver (pig trap) — Example pig receiver station diameter vs pipeline | 42 inch | US4135949A: 'a thirty inch diameter pipeline can have a forty-two inch diameter station which usually will be of length considerably greater than the diameter of the pipe' |
| Pig launcher / receiver (pig trap) — Interlock preferred setpoint | 5 psig | US4135949A: pressures up to about ten pounds preferred; 'a pressure of about 5 psig is most preferred because of convenience' |
| Pig launcher / receiver (pig trap) — Safe-to-open closure pressure setpoint | 0.5-1 psig | US4135949A: 'By choosing a setpoint of about 1/2 to about 1 psig it can be assured that the vessel is free of dangerous pressure levels before the operation of opening the vessel can begin' |


Recorded gaps:

- Pig trap pressure class, size and supplier for a named WHP — Fetch a pig trap datasheet and record size, pressure class and material with basis
- Capital cost of pig launcher/receiver — Find cost with dollar year and scope basis

### Production manifold / headers with production and test headers to commingle fluids (whp-production-manifold-headers-with-production-and-test-headers-to-commin)

Primary code: UPS: Upstream
Wellhead gathering manifold and headers that commingle flows from multiple wells, route them to production and test headers, distribute injection fluids/chemicals and provide isolation and pigging interfaces. On a typical platform the process train is listed as wellhead, production manifold, production separator, glycol dehydration, gas compressors, water injection pumps, oil/gas export metering and main oil line pumps (Wikipedia Oil platform, read). OEM manifold/tie-in systems include tradition
Vendors: TechnipFMC (CDS Separation Systems), Baker Hughes, Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Production / test manifold and headers — Manifold pressure rating (upper) | 20000 psi | TechnipFMC Manifolds page: 'Up to 20K psi' (as printed) |
| Production / test manifold and headers — Manifold temperature rating (upper) | 350 degF | TechnipFMC Manifolds page: 'Up to 350F' (as printed) |
| Production / test manifold and headers — Connection diameter (upper) | 30 ft | TechnipFMC Manifolds page: 'Up to 30’ connection diameter' (as printed) |


Recorded gaps:

- Design pressure/temperature of a named topside production/test header (not subsea manifold) — Fetch a named topside manifold or production/test header datasheet and record ratings with basis
- Capital cost of production manifold/headers — Find a cost figure with explicit dollar year and scope basis; leave as gap until then

### Sampling connections and gauging (whp-sampling-connections-and-gauging)

Primary code: UPS: Upstream
Sampling and gauging connections provide fluid property data for allocation, custody transfer and sales-specification compliance. A Christmas tree often provides chemical injection points, monitoring points (pressure, temperature, corrosion, erosion, sand detection, flow rate, flow composition, valve and choke valve position feedback) and connection points for downhole pressure and temperature transducers (Wikipedia, read). Emerson's Roxar 2600 MPFM gives real-time three-phase measurement withou
Vendors: Baker Hughes / Emerson Roxar, TechnipFMC (CDS Separation Systems), Honeywell (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Multiphase flow meter (Roxar 2600) / met — MPFM operating envelope (GVF / WLR) | 0-100 % | Emerson Roxar 2600 FAQ: 'high accuracy multiphase flow measurement for all phases within the full range of flowing conditions, 0-100% GVF and 0-100% WLR' |
| Multiphase flow meter (Roxar 2600) / met — Meter sizes available | 6 sizes | Emerson FAQ: 'Roxar™ 2600 MPFM is available in 6 sizes, with material options ranging from duplex stainless steel to Inconel' |


Recorded gaps:

- Design pressure of Roxar 2600 MPFM (3,750 psi ANSI / 5,000 psi hub) and 1.5-8 in sizes — Fetch the datasheet and record the figures with exact basis
- Sampling point count, location and sampler model for a named WHP — Fetch a design page and record printed connections and sampling devices
- Cost of metering/sampling package — Record with dollar year and basis only when a source is read

### Vents / flare tip (whp-vents-flare-tip)

Primary code: UPS: Upstream
Flare and vent systems dispose of relief/blowdown/start-up gas by controlled combustion; a knock-out drum upstream removes entrained liquid to prevent liquid carryover, flame instability and hazardous 'flaming rain' (CRA Energy page, read). FlareTech states its knockout drums range from 2 to 600 barrels. The claim that cold vent is common on unmanned WHPs is not supported by a page read in this sweep and is left as a gap.
Vendors: Allmarc Industries, John Zink (Koch Engineered Solutions) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Flare stack / boom and flare tip — Flare KO drum size range (fabricator) | 2-600 BBL | FlareTech Inc. Flare Knockout Drums page: 'designed and manufactured Flare Knockout Drums from small 2 Barrels (BBL) to large 600BBL volumes' |


Recorded gaps:

- Cold vent prevalence on unmanned WHPs — Fetch a regulator/operator page and record the venting practice with its exact wording
- Flare tip diameter, radiation limit and stack height for a specific WHP — Fetch a flare design paper and record printed values
- Flare tip failure rate, availability and proof-test interval — Record numeric data only from a page actually read
- Flare/vent system capital cost — Find cost with dollar year and basis
- Flare tip patent — Open a patent page directly and read assignee and publication year before recording

## whp-safety-emergency

### Escape routes, muster points, signs and safety lighting (whp-escape-routes-muster-points-signs-and-safety-lighting)

Primary code: HSE: Health, safety and environment
Arrangements that let personnel reach muster and embarkation stations: at least two widely separated means of escape, marked routes, photoluminescent strip indicators, emergency lighting, assembly/mimic plans, EEBDs and handrail strength requirements. Sources are SOLAS II-2/13, IMO MODU Code, classification and regulator pages.
Vendors: IMO text hosted by imorules.com / classification register (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Escape route marking and emergency light — Number of means of escape | 2 widely separated means from all spaces or group of spaces | SOLAS II-2/13.2.1 (read on imorules.com) |
| Escape route marking and emergency light — Strip indicator height above deck | 300 mm (maximum) | SOLAS II-2/13.3.2.5.1: escape routes marked by lighting or photoluminescent strip indicators placed not more than 300 mm above deck at all points including angles and intersections |
| Escape route marking and emergency light — Maximum dead-end corridor length | 7 m | SOLAS II-2/13.3.3.4 for cargo ships; IMO 2009 MODU Code 9.4.1.3 and RS Class Rules 9.2.6 (search extracts) |
| Escape route marking and emergency light — Quick-release escape door force | 67 N (maximum) | SOLAS II-2/13.3.2.6.2: latch releases when force not exceeding 67 N applied; actuating bar at least 760 mm and not more than 1120 mm above deck |
| Escape route marking and emergency light — Handrail / handhold strength | 750 N/m (horizontal and vertical distributed load) | SOLAS II-2/13.7.3.1 |
| Escape route marking and emergency light — Minimum clear width of escape stairway with single escape | 800 mm | SOLAS II-2/13.3.2.1.2 with handrails on both sides |
| Escape route marking and emergency light — Minimum EEBDs in accommodation | 2 devices | SOLAS II-2/13.3.4.2: all ships shall carry at least two emergency escape breathing devices within accommodation spaces |
| Reliability — General alarm test frequency (MODU) | 1 per week | 46 CFR 109.301(d)(3): 'The general alarm system must be tested' under weekly inspections and tests |


Recorded gaps:

- Offshore-specific illumination levels (lux) for muster areas, temporary refuge and escape routes — Retrieve the HSE circular from an archived copy and WebFetch it, or obtain EN 1838 text
- Named vendors for photoluminescent escape-route systems on offshore units — Search OEM datasheets for photoluminescent escape guidance systems with printed lux/endurance specs

### Fire extinguishers, hydrant hoses, SCBA sets on manned platforms (whp-fire-extinguishers-hydrant-hoses-scba-sets-on-manned-platforms)

Primary code: HSE: Health, safety and environment
Portable and semi-portable extinguishers, fire-main hydrants and hoses, and self-contained breathing apparatus for fire teams on manned offshore installations. Evidence is from USCG Outer Continental Shelf and Deepwater Port regulations, SOLAS/IMO sources, US 46 CFR emergency-equipment rules and an OEM product catalogue.
Vendors: US Coast Guard (OFR) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Self-contained breathing apparatus (SCBA — Minimum air supply | 30 min | 46 CFR 77.30-5(a): each SCBA must be pressure-demand open-circuit type, MSHA and NIOSH approved, with at minimum a 30-minute air supply and a full facepiece |
| Reliability — Monthly extinguisher inspection | 1 per month | 33 CFR 145.01(b)(2): monthly inspections required by NFPA 10 may be conducted by owner, operator, person-in-charge or designated crew member |
| Reliability — Annual extinguisher maintenance and hydrostatic test | 1 per year | 33 CFR 145.01(b)(1) and (4): annual maintenance/recharging to NFPA 10; hydrostatic pressure tests by qualified servicing facility |


Recorded gaps:

- Fire extinguisher, hydrant hose and SCBA purchase prices with dollar year — Obtain OEM distributor quotations with explicit dollar year
- SCBA cylinder and duration figures from a WebFetch-readable page — Fetch accessible HTML mirrors or read PDFs with a PDF-capable tool
- Offshore-platform-specific fire-hose and hydrant spacing — WebFetch those eCFR sections directly

### Life rafts, retrieval nets, sea rescue baskets (whp-life-rafts-retrieval-nets-sea-rescue-baskets)

Primary code: HSE: Health, safety and environment
Inflatable liferafts (float-free and davit-launched), their canisters and hydrostatic release units, plus personnel transfer baskets / rescue baskets. Retrieval nets were not directly evidenced in the pages read; this is recorded as a gap.
Vendors: IMO text mirrored by SOLAS/LSA Code (Vercel) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Mass limit for side-to-side transfer | 185 kg | 46 CFR 133.150(c)(1): craft boarded from deck less than 4.5 m above waterline and mass not more than 185 kg need not have launching appliance; LSA Code 4.1.2.2 equivalent |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Inflation time at 18-20 C | 1 min | LSA Code 4.2.2.3: inflation completed within 1 min at ambient 18-20 C |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Inflation time at -30 C | 3 min | LSA Code 4.2.2.3: inflation completed within 3 min at -30 C |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Buoyancy chamber compartment withstand pressure | 3 times working pressure | LSA Code 4.2.2.4 (numbered 4.2.7.4 in OCR mirror): each inflatable compartment withstand at least 3 times working pressure |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Carrying capacity divisor - tube volume | 0.096 m3 per person | LSA Code 4.2.3.1: greatest whole number from volume of main buoyancy tubes divided by 0.096 |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Carrying capacity divisor - floor area | 0.372 m2 per person | LSA Code 4.2.3.2: inner horizontal cross-sectional area divided by 0.372 |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Boarding ramp load | 100 kg | LSA Code 4.2.4.1: at least one entrance with semi-rigid boarding ramp capable of supporting a person weighing 100 kg sitting or kneeling and not holding onto the raft |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Boarding ladder lowest step below waterline | 0.4 m | LSA Code 4.2.4.2 for entrances without a boarding ramp |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Towing speed with full complement | 3 knots in calm water | LSA Code 4.2.5.3 |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Water pockets fill time | 60 % of capacity within 25 s of deployment | LSA Code 4.2.5.4.2 in OCR mirror |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Water pocket aggregate capacity, up to 10 persons | 220 L (minimum) | LSA Code 4.2.5.4.3 in OCR mirror |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Davit-launched raft suspension load | 4 times mass of full complement of persons and equipment | LSA Code 4.2.8.1.1: at 20 +/- 3 C with all relief valves inoperative |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Service interval (MODU) | 12 months | 46 CFR 109.301(g)(1): each inflatable lifesaving appliance serviced within 12 months of initial packing and each subsequent servicing (5-month delay allowed to next scheduled inspection) |
| Inflatable liferaft (SOLAS / USCG-SOLAS  — Aggregate capacity, manned offshore installation | 100 % of persons on board | Canada OGI Regs s.22(1)(b): one or more inflatable liferafts with combined capacity at least 100% of total POB, float-free capability, Class A equipment |
| Hydrostatic release unit (HRU) and float — HRU service interval (MODU) | 12 months | 46 CFR 109.301(h)(1): each hydrostatic release unit other than disposable serviced within 12 months of manufacture and each subsequent servicing |
| Offshore personnel transfer basket / res — Capacity, SAFE-TRANSFER 8-person | 8 persons | Viking Life product page 1145-8: 'Capacity: 8 persons' |
| Offshore personnel transfer basket / res — Payload, SAFE-TRANSFER 8-person | 1000 kg | Viking Life product page: 'Max load (payload): 1000 kg' |
| Offshore personnel transfer basket / res — Rescue basket capacity, Canadian offshore rule | 6 persons (minimum) | Canada OGI Regs s.22(1)(f)(iii): 'a rescue basket capable of accommodating at least six persons' |
| Offshore personnel transfer basket / res — Buoyant personnel transfer baskets, Canadian offshore rule | 2 baskets | Canada OGI Regs s.22(1)(f)(viii) |
| Reliability — Inflatable liferaft service interval | 12 months | 46 CFR 109.301(g)(1) for MODUs |
| Reliability — Hydrostatic release unit service interval | 12 months | 46 CFR 109.301(h)(1) |
| Price — Revere USCG/SOLAS 'A' liferaft, low profile container - list price from | 4095 USD | Dollar year not stated; SurvivalAtSea.com listing shows copyright 2026; 'From $4095'; dollar year not stated. |
| Price — Survitec Zodiac USCG/SOLAS 'A' liferaft, low profile container - list price from | 3450 USD | Dollar year not stated; SurvivalAtSea.com listing ©2026; 'From $3450'; dollar year not stated. |
| Price — Survitec Zodiac XTREM USCG/SOLAS 'A' liferaft - list price from | 6250 USD | Dollar year not stated; SurvivalAtSea.com listing ©2026; 'From $6250'; dollar year not stated. |
| Price — Revere USCG-approved compact liferaft - list price from | 5000 USD | Dollar year not stated; SurvivalAtSea.com listing ©2026; 'From $5000'; dollar year not stated. |
| Price — Pre-owned Crewsaver USCG/SOLAS 6-person liferaft | 1995 USD | Dollar year not stated; SurvivalAtSea.com listing ©2026; was $3,595, now $1,995 (out of stock); dollar year not stated. |


Recorded gaps:

- Retrieval nets (liferaft retrieval / boarding nets) — Search OEM catalogues (Survitec, Viking, Zodiac) for 'liferaft retrieval net' datasheets and record printed specs
- Liferaft service cost and replacement cost with dollar year — Find a dated USD service/replacement quotation from a US or APAC service station
- Quantitative liferaft deployment reliability / failure-on-demand rate — Locate an open lifecycle/reliability study and WebFetch the text

### Lifeboat / TEMPSC with davit (whp-lifeboat-tempsc-with-davit)

Primary code: HSE: Health, safety and environment
Totally Enclosed Motor Propelled Survival Craft (TEMPSC) launched by davit or free-fall, required on manned offshore units, together with lifebuoys (life rings) and their self-igniting lights, self-activating smoke signals and buoyant lifelines. Evidence spans USCG/US regulations, the IMO LSA Code, Canadian offshore rules, a manufacturer datasheet, two patents and historical records.
Vendors: IMO text mirrored by SOLAS/LSA Code (Vercel) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Totally Enclosed Motor Propelled Surviva — Offered capacity range, manufacturer | 16-150 persons | Gohi Marine GLB series product table, 'Capacity 16-150 Persons'; 'Max. Capacity of 150 persons lifeboat is also available' |
| Totally Enclosed Motor Propelled Surviva — Design mass per person, manufacturer option | 95 kg/person | Product title 'SOLAS Approved 95KG Per Person ... TEMPSC'; seat design can meet 100 kg per person |
| Totally Enclosed Motor Propelled Surviva — Full-load speed | 6-? knots | Gohi Marine table 'Speed >=6' for all GLB50C/F to GLB117C/F models |
| Totally Enclosed Motor Propelled Surviva — Minimum speed, Canadian offshore rule | 6 knots | Canada Oil and Gas Installations Regulations s.22(2)(e): 'be capable of a speed of not less than 6 knots' |
| Totally Enclosed Motor Propelled Surviva — Self-contained air supply | 10 min | Canada OGI Regs s.22(2)(f): 'a self-contained air supply sufficient for at least 10 minutes' |
| Totally Enclosed Motor Propelled Surviva — Aggregate capacity, manned installation | 200 % of persons on board | Canada OGI Regs s.22(1)(a): two or more totally enclosed survival craft with combined capacity at least 200% of total POB |
| Totally Enclosed Motor Propelled Surviva — Launch time, all survival craft | 10 min | 46 CFR 133.150(a): capable of being launched with full complement within 10 minutes of abandon-ship signal |
| Totally Enclosed Motor Propelled Surviva — Embarkation preparation time, 2 crew | 5 min | Canada OGI Regs s.22(2)(j): stowed so two crew members can complete preparations for embarkation and launching in less than 5 minutes |
| Davit / launching appliance and winch wi — Structural attachment strength factor | 4.5 times load | 46 CFR 133.150(f): structural attachment designed to at least 4.5 times the load imparted and the ultimate strength of the material |
| Davit / launching appliance and winch wi — Board davit-launched craft | 3 min | 46 CFR 133.150(g)(6): each davit-launched liferaft boardable by full complement within 3 minutes of instruction to board |
| Davit / launching appliance and winch wi — Release gear proof load | 1.1 times total loaded mass | 46 CFR 109.301(i)(5): release gear operationally tested under load of 1.1 times total mass of lifeboat with full complement, whenever overhauled or at least once every 5 years |
| Davit / launching appliance and winch wi — Launching appliance examination interval | 5 years (maximum) | 46 CFR 109.301(i)(2): thoroughly examined at intervals not exceeding 5 years, followed by dynamic test of winch brake |
| Davit / launching appliance and winch wi — Fall renewal interval | 5 years (maximum) | 46 CFR 109.301(j): each fall inspected annually and renewed when necessary or at intervals of not more than 5 years, whichever earlier |
| Davit / launching appliance and winch wi — Winch lowering speed, training mode | 30 m/min | WO2013122479A1: first flow control valve 'set to control the lowering speed at approximately 30 m/min' when isolating valve closed |
| Davit / launching appliance and winch wi — Winch lowering speed, standby/evacuation mode | 60 m/min | WO2013122479A1: second primary flow control valve permits 'increasing the lowering speed to 60 m/min'; isolating valve normally open ready for evacuation |
| Davit / launching appliance and winch wi — Accumulator normal working pressure | 200 bar | WO2013122479A1: 'normal working pressure of the accumulators is 200bar and the opening pressure of the multi disk brakes ... typically 18bar' |
| Lifebuoy (life ring) with self-igniting  — Outer diameter | 800 mm (maximum) | LSA Code 2.1.1.1 as printed on SEAFDEC/TD page: 'outer diameter of no more than 800 mm' |
| Lifebuoy (life ring) with self-igniting  — Inner diameter | 400 mm (minimum) | LSA Code 2.1.1.1: 'inner diameter of not less than 400 mm' |
| Lifebuoy (life ring) with self-igniting  — Buoyancy | 14.5 kg iron in fresh water for 24 h | LSA Code 2.1.1.3 |
| Lifebuoy (life ring) with self-igniting  — Mass | 2.5 kg (minimum) | LSA Code 2.1.1.4 |
| Lifebuoy (life ring) with self-igniting  — Mass with quick-release for light/smoke | 4 kg (minimum) | LSA Code 2.1.1.7: if intended to operate quick-release arrangement for self-activated smoke signals and self-igniting lights |
| Lifebuoy (life ring) with self-igniting  — Drop test height | 30 m (or stowage height, whichever greater) | LSA Code 2.1.1.6 |
| Lifebuoy (life ring) with self-igniting  — Grab line diameter | 9.5 mm (minimum) | LSA Code 2.1.1.8, secured at four equidistant points to form four equal loops |
| Lifebuoy (life ring) with self-igniting  — Fire resistance | 2 s (no burning/melting after total envelopment) | LSA Code 2.1.1.5 |
| Lifebuoy (life ring) with self-igniting  — Number on manned offshore installation | 8-14 lifebuoys | Canada OGI Regs s.22(1)(f)(ii): 8 if <=100 m; 10 if >100 and <150 m; 12 if >=150 and <200 m; 14 if >=200 m |
| Lifebuoy (life ring) with self-igniting  — Lifebuoys with lights / smoke | 50 % of total (at least half), with not fewer than 2 with smoke signals | Canada OGI Regs s.22(4) |
| Lifebuoy (life ring) with self-igniting  — Buoyant lifeline length | 30 m (or 1.5 x stowage-to-waterline distance, whichever greater) | Canada OGI Regs s.22(5) for two lifebuoys not equipped with lights and smoke signals |
| Reliability — Release gear proof test load factor | 1.1 x total loaded mass | 46 CFR 109.301(i)(5): at least once every 5 years or whenever overhauled |
| Reliability — Launching appliance thorough examination interval | 5 years max | 46 CFR 109.301(i)(2), with dynamic test of winch brake on completion |
| Reliability — Weekly lifeboat engine run time | 3 min ahead and astern | 46 CFR 109.301(d)(2) |


Recorded gaps:

- Quantity/availability/reliability figures for lifeboats and davits on offshore platforms — Fetch the PDFs by an alternate method and record failure probabilities with basis
- Lifeboat/TEMPSC purchase price in USD with dollar year — Obtain a dated USD quotation from an OEM such as Survitec, Viking or Norsafe

### Overboard dump valves and ESD-initiated isolation of all wells and pipelines (whp-overboard-dump-valves-and-esd-initiated-isolation-of-all-wells-and-pip)

Primary code: HSE: Health, safety and environment
Emergency shutdown (ESD) systems that isolate wells and pipelines, using surface safety valves (SSV), boarding shutdown valves (BSDV), subsurface safety valves (SSSV) and shutdown valves; plus overboard dump valves used on offshore water injection / drain systems. Evidence is primarily from BSEE regulation, API RP 14C definitions (search extract), API 6A (search extract), OEM datasheets and an incident-derived engineering article.
Vendors: SLB (Cameron pressure control equipment), Cameron (SLB), Baker Hughes (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Surface Safety Valve (SSV) / Boarding Sh — Pressure class | 2000-20000 psi working pressure | Indus Hydraulics IH-OFE-SSV |
| Surface Safety Valve (SSV) / Boarding Sh — Temperature range | -46-180 deg C | Indus Hydraulics IH-OFE-SSV |


Recorded gaps:

- Full text of API RP 14C 8th edition with safety analysis tables (SACs) and ESD appendix C — Read the standard PDF with a PDF-capable tool or obtain licensed copy
- ESD proof-test results / availability figures for offshore platforms — Search for OREDA/operator ESD reliability data with printed figures
- Prices for SSV, BSDV and overboard dump valves with dollar year — Request dated quotations

## whp-structural-marine

### Helideck (whp-helideck)

Primary code: CIV: Civil and structural
The read sources treat a helipad/helideck as an appurtenance: an NUI is described as little more than a well bay, helipad and emergency shelter; US4679964A describes a cantilevered helideck on single- or multi-well conductor-supported configurations; US4932811A describes an upper heliport deck carried by piles around a caisson. No page read in this sweep stated a helideck D-value, load classification, obstacle-free sector or a visit-frequency rule, and the CAP 437 PDF was refused.
Vendors: Wikipedia (Wikimedia Foundation) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| List membership | Recorded from the Mistral-chat WHP component list n/a | Item listed in the source chat; no numeric specification was found in the pages read. |


Recorded gaps:

- Helideck D-value, load class and obstacle-free sectors — Read an HTML CAP 437 / ICAO helideck page, or fetch the PDF by another method, then record sections and values.
- Visit frequency rule for crewed visits — Find an operator or regulator page stating the actual visit interval for Malaysian WHPs.
- Malaysian helideck aviation standard — Locate and read the applicable Malaysian offshore helideck standard page.

### Jacket structure (whp-jacket-structure)

Primary code: CIV: Civil and structural
A fixed steel jacket is a braced tubular, pile-founded substructure that carries the topside and laterally supports and protects well conductors and the pipeline riser; ESDEP states the overwhelming majority of platforms are piled-jacket with steel deck structures. For smaller/marginal fields the read sources describe conductor-supported minimum-facility platforms (MFP/CoSMOS), monopile or caisson alternatives. Appurtenances evidenced on read pages are a clamp-on boat landing (US4679964A, US4932
Vendors: 2H Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Fixed steel jacket (3-/4-legged tubular, — Well conductor size protected by jacket | 26-30 inch | ESDEP Lecture 15A.1 section 4.1: jackets "support laterally and protect the 26-30 inch well conductors and the pipeline riser". |
| Fixed steel jacket (3-/4-legged tubular, — Typical air gap (topside clearance above maximum wave) | 1.5 m (approximately) | ESDEP 15A.1 section 2.2: clearance usually taken at approximately 1.50 m, to be increased if reservoir depletion creates significant subsidence. |
| Fixed steel jacket (3-/4-legged tubular, — Jacket pile diameter | ?-2 m (up to) | ESDEP 15A.1 section 4.2: open-ended tubular steel piles "with diameters up to 2m". |
| Fixed steel jacket (3-/4-legged tubular, — Jacket pile penetration, typical | 40-80 m | ESDEP 15A.1 section 4.2: piles driven approximately 40 - 80 m into the seabed. |
| Fixed steel jacket (3-/4-legged tubular, — Jacket pile penetration, deep case | 120 m (in some cases) | ESDEP 15A.1 section 4.2: "and in some cases 120 m deep into the seabed". |
| Fixed steel jacket (3-/4-legged tubular, — Economically feasible water depth, fixed platform | 500 ft (about 150 m) | Wikipedia Fixed platform: "economically feasible for installation in water depths up to about 500 feet (150 m)". Conflicts with the 520 m figure on the Oil platform page; neither preferred. |
| Fixed steel jacket (3-/4-legged tubular, — Economically feasible water depth, fixed platform (second source) | 520 m (about 1,710 ft) | Wikipedia Oil platform: "Fixed platforms are economically feasible for installation in water depths up to about 520 m (1,710 ft)". Conflict noted; neither figure preferred. |
| Boat landing / barge impact protection ( — Conductor diameter for clamp-on boat landing | 26-30 inch | US4679964A description: conductor pipe "typically in the range of about 26 to about 30 inches in diameter" with wall thickness about one inch; boat landing clamped to it at the water line. |
| Boat landing / barge impact protection ( — Example anchor pile length | 70 ft | US4679964A description: "the piling is 70 feet in length" with about 52 feet protruding into the seabed. |
| Boat landing / barge impact protection ( — Clamp-base footprint of prior-art Sea Horse system | 40 ft (approximately, square) | US4932811A background: "The base of the sea horse clamp is approximately forty by forty feet square where piling are driven through the cans". |
| Conductor-supported / monopile substruct — Conductor-supported platform water depth applicability | ?-120 m (up to) | 2H Minimum Facility Platforms: conductor-supported MFPs "suitable for water depths up to 120m". |
| Reliability — Offshore inspection, maintenance and repair share of OPEX | 20 % of OPEX (North Sea) | ESDEP 15A.1 section 9.3: "In the North Sea approximately 20 percent of OPEX are required for offshore inspection, maintenance and repair (IMR)". |
| Reliability — Dynamic analysis trigger | 3 seconds (natural period) | ESDEP 15A.1 section 8.1: dynamic analysis performed for system behaviour under wave attack if the natural period exceeds 3 seconds. |


Recorded gaps:

- Barge bumper and pull-in tube sizing — Fetch a jacket appurtenance specification page or engineering-company detail sheet and read it with WebFetch.
- ISO 19902 full text — Locate and WebFetch a readable ISO 19902 landing page, or read the standard under licence.
- Current API RP 2A edition — Fetch an API page that prints the current RP 2A-WSD edition and status.
- Conflicting fixed-platform water-depth limits — Seek a primary standard or API text stating the applicability range.
- Kebabangan platform description conflict — Cross-check against KPOC / operator or contractor sources.
- Jacket-only cost with dollar year — Fetch a project page with a named-year USD contract value.

### Malaysian WHP operating context: normally unmanned, no separators/produced-water treatment/g (whp-malaysian-whp-operating-context-normally-unmanned-no-separators-produc)

Primary code: CIV: Civil and structural
Read pages establish that Anjung Kecil WHP is a Tarpon "minimum facility and unmanned platform typically installed in shallow water", tied to the MaMPU-1 FPSO which carries crude stabilisation (Sep-iSYS), a low-pressure condensate recovery unit and storage. The NUI articles describe remote operation with occasional visits and emergency shelter. 2H describes an unmanned MFP tied back by flexible flowline. The specific claims of no separators/produced-water treatment/gas compression onboard and fo
Vendors: 2H Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Host FPSO / MOPU with processing (MaMPU- — FPSO storage capacity | 318000 barrels | Offshore Technology Anjung Kecil: storage capacity of the MaMPU-1 FPSO is 318,000 barrels. |
| Host FPSO / MOPU with processing (MaMPU- — FPSO oil production capacity | 15000 barrels of oil per day | Offshore Technology Anjung Kecil: production capacity of 15,000 barrels of oil per day. |
| Host FPSO / MOPU with processing (MaMPU- — FPSO gas handling capacity | 25 million metric standard cubic feet per day (mmscfd) | Offshore Technology Anjung Kecil: gas handling capacity of 25 million metric standard cubic feet per day. |
| Host FPSO / MOPU with processing (MaMPU- — Incremental oil from LP-CRS | 50 barrels of oil per one million square cubic feet of flared gas (as printed) | Offshore Technology Anjung Kecil: CRS and Sep-iSYS expected to add approximately 50 barrels of oil per one million square cubic feet of flared gas. |
| Host FPSO / MOPU with processing (MaMPU- — Flaring emissions reduction | 25-30 % on daily flaring rates | Offshore Technology Anjung Kecil: technology will reduce carbon emissions by 25% to 30% on daily flaring rates. |
| Host FPSO / MOPU with processing (MaMPU- — Dynamic subsea power cable | 1.26 km | Offshore Technology Anjung Kecil: dynamic subsea power cable between FPSO and well-head platform. |
| KMSE / AJK WHPs (PETRONAS Carigali) — Water depth | 70-85 m | Tarpon KMSE/AJK project page. |
| KMSE / AJK WHPs (PETRONAS Carigali) — Design life | 20 years | Tarpon KMSE/AJK project page. |
| KMSE / AJK WHPs (PETRONAS Carigali) — Distance offshore | 200 km (approximately, offshore Bintulu, Sarawak) | Tarpon KMSE/AJK page: fields located in Block SK315 approximately 200km offshore from the coast of Bintulu, Sarawak. |
| Price — Kebabangan FEED contract value (USD-equivalent as printed) | 30 USD million (as printed) | As printed: "The four-year contract is valued at Nkr170m (approximately $30m)". Dollar year not stated; article dated 5 May 2016. USD-equivalent only; Nkr figure not converted here.; dollar year not stated. |
| Price — Kebabangan topsides fabrication contract | 380 USD million (as printed) | As printed: "A $380m (RM1.15bn) contract to fabricate the topsides of the platform was awarded to Sime Darby Engineering in April 2011". Dollar year not stated; article dated 5 May 2016.; dollar year not stated. |


Recorded gaps:

- No separators / produced-water treatment / gas compression onboard — Fetch a PETRONAS/Vestigo WHP facilities-scope page listing equipment excluded from the WHP.
- Fortnightly visits — Verify with an operator or regulator page before recording.
- All processing on CPP/FSO/MOPU — Fetch operator pages describing the host-processing split.
- Malampaya, Tangguh and Kebabangan WHP-specific details — Fetch and WebFetch those project pages before adding figures.
- Dollar-year on Kebabangan USD figures — Find a source with an explicit dollar year.

### Minimum-facility WHP logistics: designed for jack-up-rig installation, little or no onboard (whp-minimum-facility-whp-logistics-designed-for-jack-up-rig-installation-l)

Primary code: CIV: Civil and structural
2H Offshore describes conductor-supported minimum facility platforms (MFP, MFP+ and the CoSMOS variant) that can be entirely installed from a jack-up drilling rig, eliminating conventional offshore installation spread. The SE Asia project used a multiphase flow meter and three power sources (solar panels, nitrogen racks, diesel-powered cranes) to reduce topside payload, with an 8 km flexible flowline tieback and two-stage installation. Tarpon describes relocatable, 20-year-life, three-slot minim
Vendors: 2H Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Conductor-supported minimum facility pla — Applicable water depth | ?-120 m (up to) | 2H Minimum Facility Platforms: conductor-supported MFPs "suitable for water depths up to 120m". |
| Conductor-supported minimum facility pla — Stated design and delivery expertise | 15 years | 2H MFP page: "With 15 years’ expertise in the design and delivery of MFPs" (page undated). |
| Conductor-supported minimum facility pla — Production wells on SE Asia MFP | 2 wells | 2H project: "an unmanned minimum facilities wellhead platform housing two production wells along with provisions for future gas lift". |
| Conductor-supported minimum facility pla — Flexible flowline tieback length | 8 km | 2H project: tied back "using an 8km flexible flowline". |
| Conductor-supported minimum facility pla — Number of diversified power sources | 3 power sources | 2H project: "diversifying power supply from three different power sources (solar panels, nitrogen racks and diesel powered cranes)". |
| Conductor-supported minimum facility pla — Design, delivery and installation duration | 10 months | 2H project: CoSMOS platform "successfully designed, delivered and installed within 10 months, and ahead of schedule". |
| Conductor-supported minimum facility pla — Project man-hours | 225000 man hours (approximate) | 2H project: milestone achieved "with approx. 225,000 man hours and zero lost time incidents (LTI)". |
| Conductor-supported minimum facility pla — Installation campaign stages | 2 stages | 2H project: two-part installation campaign; substructure installed early so drilling ran in parallel with topside fabrication, topside installed in second phase. |
| Jack-up rig (installation and drilling u — Jack-up drilling water depth | 100-120 m | ESDEP 15A.1 section 3.1: jack-up drilling rigs used for exploration wells for water depths up to 100 - 120 m. |
| Jack-up rig (installation and drilling u — Jack-up typical water depth | ?-120 m (390 ft), some designs 170 m (560 ft) | Wikipedia Oil platform, Jack-up drilling rigs section. |
| Jack-up rig (installation and drilling u — Jack-up depth in patent background | ?-300 ft (generally designed up to) | US5513929A background: "the jack-up is generally designed for water depths up to three hundred feet". |
| Tarpon relocatable WHP — Conductor slots per platform | 3 slots (20-inch, internal to caisson) | Tarpon KMSE/AJK page: each platform has three 20-inch conductor slots internal to the caisson, two utilised and one spare. |
| Tarpon relocatable WHP — Design life | 20 years (operational lifespan) | Tarpon KMSE/AJK page: platforms designed for a 20-year operational lifespan and made relocatable. |
| Tarpon relocatable WHP — Water depth range | 70-85 m | Tarpon KMSE/AJK page: water depths varying from 70m to 85m. |
| Reliability — Lost time incidents on CoSMOS project | 0 LTI (lost time incidents) | 2H project: approx. 225,000 man hours and zero lost time incidents, attributed to QHSE procedures. |


Recorded gaps:

- MFP cost with dollar year — Fetch a project page printing a dated USD cost.
- Onboard processing inventory for the SE Asia MFP — Fetch a facilities scope page to confirm which processing equipment is omitted.
- Fortnightly visit interval — Find a Malaysian operator page stating visit frequency.
- Jack-up installation sea-state limits — Fetch an installation-method statement with stated weather window.

### Risers and J-tubes for pipelines and subsea cables (whp-risers-and-j-tubes-for-pipelines-and-subsea-cables)

Primary code: CIV: Civil and structural
ESDEP defines a pipeline riser as the piping rising from seabed to topside level and describes conductors as protecting and guiding the drill string from topside to 40-100 m below the seabed. US5513929A describes conventional casing guides and tensioned-casing production risers; US4679964A shows a prefabricated riser pipe from a conductor-mounted miniplatform to a remote flowline. At Anjung Kecil a 1.26 km dynamic subsea power cable links the FPSO to the wellhead platform. No page read during th
Vendors: FGG Web (FGG, Uni Ljubljana) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pipeline riser / conductor-guided riser — Conductor depth below seabed | 40-100 m (under sea bottom) | ESDEP 15A.1 glossary, "CONDUCTORS": tubular protecting and guiding the drill string from topside down to 40 to 100 m under the sea bottom. |
| Pipeline riser / conductor-guided riser — Conventional conductor diameter examples | 24-30 inch | US5513929A background: conductors "usually from twenty-four to thirty inches" in diameter. |
| Pipeline riser / conductor-guided riser — Sump / discharge pipe depth below water level | 5-10 m below water level | ESDEP 15A.1 glossary, "SUMPS": vertical pipes from topside down to 5-10 m below water level for intake or discharge. |
| Dynamic subsea power cable (FPSO to WHP) — Dynamic subsea power cable length | 1.26 km | Offshore Technology Anjung Kecil: "A 1.26km-long dynamic subsea power cable will be laid between the FPSO and the well-head platform as part of the field modification plan". |
| Reliability — Dynamic analysis trigger for slender members and conductors | 3 seconds (natural period) | ESDEP 15A.1 section 8.1: dynamic analysis if natural period exceeds 3 seconds; slender jacket members and conductors listed as locally dynamic. |


Recorded gaps:

- J-tube sizing and bend restrictor data — Fetch and WebFetch a manufacturer J-tube/bend-restrictor data page.
- Riser design standard — Fetch readable HTML pages naming the applicable riser standards and read them.
- Riser fatigue life and inspection interval — Fetch an operator or integrity-management page with stated intervals.

### Topside decks (whp-topside-decks)

Primary code: CIV: Civil and structural
Read sources describe topside structural concepts (single integrated deck, split deck, integrated deck with living quarters, modular topside on a module support frame), weight bands and one-lift installation limits, plus equipment module and living-quarter module construction. ESDEP lists major deck functions including well control, separation, pumps/compressors, power generation and accommodation. No page read during this sweep explicitly names the cellar/main/mezzanine three-level arrangement 
Vendors: 2H Offshore (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Integrated / modular topside deck and mo — Single integrated deck weight limit | ?-100 MN (up to approximately) | ESDEP 15A.1 section 5.2.1: "the single integrated deck (up to approx 100 MN)". |
| Integrated / modular topside deck and mo — Topside single-lift installation limit | ?-120 MN (up to approximately) | ESDEP 15A.1 section 7.2.4: "For topsides up to approximately 120 MN, the topside may be installed in one lift". |
| Integrated / modular topside deck and mo — Major modularized topside weight | 200-400 MN | ESDEP 15A.1 section 5.2.3: "A major modularized topside weighs 200 to 400 MN". |
| Integrated / modular topside deck and mo — Equipment module weight | 20-75 MN | ESDEP 15A.1 section 6: equipment modules (20-75 MN), rectangular boxes with one or two intermediate floors. |
| Integrated / modular topside deck and mo — Living quarter module weight | 5-25 MN | ESDEP 15A.1 section 6: living quarter modules (5-25 MN). |
| Wellhead area / deck level arrangement — Kebabangan deck content and mass | 17000 t (deck weight) | Offshore Technology Kebabangan: deck weighs 17,000 t and features a tender-assisted drilling (TAD) rig, utilities and accommodation for staff. |
| Reliability — Design life of Tarpon KMSE/AJK WHPs | 20 years (operational lifespan, design) | Tarpon Systems project page: platforms designed for a 20-year operational lifespan and made relocatable. |
| Price — Topsides fabrication contract, Kebabangan | 380 USD million (as printed) | As printed: "A $380m (RM1.15bn) contract to fabricate the topsides of the platform was awarded to Sime Darby Engineering in April 2011". Dollar year not stated; article dated 5 May 2016. Not a unit-rate or full project cost.; dollar year not stated. |


Recorded gaps:

- Cellar / main / mezzanine deck naming — Fetch a WHP topside GA description page and confirm the deck naming and functions.
- Deck steel weight for an unmanned WHP — Fetch a minimum-facility topside weight statement.
- USD deck cost with stated dollar year — Find a dated-cost source or record literal basis "dollar year not stated" as done here.

## whp-utility

### Crane (whp-crane)

Primary code: UPS: Upstream
Unmanned and manned WHPs use pedestal/deck cranes for supply-boat transfers, wireline/coiled-tubing equipment and module handling. PALFINGER AHC crane data gives printed capacity/radius/wire ranges; Ramboll/NPD gives crane sizes by UWHP type. No page read gave a quantified laydown-area specification.
Vendors: PALFINGER (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Pedestal/deck crane - PALFINGER active h — SWL range | 5-250 tons | PALFINGER can deliver AHC cranes with SWL ranging from 5 to 250 tons and wire capacities exceeding 3,000 meters |
| Pedestal/deck crane - PALFINGER active h — Hoisting capacity | 250 metric tons (up to) | Hoisting capacity up to 250 metric tons |
| Pedestal/deck crane - PALFINGER active h — Jib radius | 50 m (up to, engineering to order) | Jib radius up to 50 meters (engineering to order) |
| Pedestal/deck crane - PALFINGER active h — Main winch wire capacity | 3000 m | 3,000-meter wire capacity for standard range |
| Pedestal/deck crane - PALFINGER active h — Winterisation temperature | -50 degC | PALFINGER has developed a range of innovative solutions that ensure safe and reliable performance at temperatures as low as -50 °C |
| UWHP pedestal crane sizing by platform t — Type 0 crane sizing | 50-60 tonnes (coiled tubing equipment) | The platform has a crane sized for coiled tubing equipment (50-60 tonnes) |
| UWHP pedestal crane sizing by platform t — Type 1 crane sizing | 10-50 tonnes (well intervention equipment) | The platform has a crane sized for well intervention equipment (10-50 tonnes) |
| UWHP pedestal crane sizing by platform t — Type 2 crane sizing | 1-2 tonnes | The platform has a small crane (1-2 tonnes) |


Recorded gaps:

- Crane and laydown areas — Fetch a WHP topside layout/general arrangement drawing or structural design basis with deck load ratings
- Crane and laydown areas — Fetch an OEM quotation or project equipment cost report

### Diesel storage and transfer (whp-diesel-storage-and-transfer)

Primary code: UPS: Upstream
Bulk marine gasoil is bunkered from shore/vessel to the installation, held in storage and day tanks, and transferred to emergency gensets, fire pumps and crane engines. The read guidance sets fuel quality, microbial and water limits, tank inspection and bunkering controls; JIP33 S-714/S-721 give day-tank and fuel-system design requirements.
Vendors: Marine Safety Forum (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Marine gasoil (MGO) bulk storage and day — Maximum sulphur content (SECA) | 0.1 % | Offshore Installations in the North Sea fall within a Sulphur Emission Control Area (SECA) that limits ships to use fuel with a maximum sulphur content of 0.1% |
| Marine gasoil (MGO) bulk storage and day — Minimum flash point | 60 degC | According to the International Convention for Safety of Life at Sea (SOLAS) the Flash Point must be a minimum of 60°C |
| Marine gasoil (MGO) bulk storage and day — Pour point, summer / winter | -6-0 degC | This is 0°C in summer and -6°C in winter |
| Marine gasoil (MGO) bulk storage and day — Cold filter plugging point, summer / winter (BS 2869) | -12--4 degC | The BS:2869 specification is -4°C in Summer and -12°C in Winter |
| Marine gasoil (MGO) bulk storage and day — Maximum fuel retained onboard before testing | 30 days | fuel is not retained onboard for more than 30 days |
| Marine gasoil (MGO) bulk storage and day — Day tank minimum operating level above fuel injection pump inlet | 300 mm | The day tank minimum operating level shall be 300 mm (12 in) above inlet of the fuel injection pump where a positive static head is required |
| Reliability — Water content - negligible / moderate / heavy | 100-200 mg/kg | Water content (e.g. by IP438): Negligible <100 mg/kg; Moderate 100 - 200 mg/kg; Heavy >200 mg/kg |
| Reliability — Total viable count of culturable bacteria/yeasts/moulds | 10000-100000 CFU/Litre | Total Viable Count of culturable bacteria, yeasts and/or moulds (e.g. by IP385 / ASTM D6974 or IP613): Negligible <10^4 CFU/Litre; Moderate 10^4 - 10^5 CFU/Litre; Heavy >10^5 CFU/Litre |
| Price — Diesel standby fuel infrastructure - day tank | 2000-8000 USD | a day tank (2,000–8,000) ... fuel infrastructure cost ranges, 2026 vendor pricing guide; dollar year 2026. |
| Price — Diesel standby fuel infrastructure - bulk storage tank | 8000-60000 USD | bulk storage tank (8,000–60,000+ depending on capacity); dollar year 2026. |
| Price — Fuel infrastructure for 500 kW / 72 h autonomy | 25000-50000 USD | For a 500 kW facility requiring 72 hours of autonomous runtime, fuel infrastructure can add 25,000–50,000 to the total project; dollar year 2026. |
| Price — Diesel fuel cost | 0.08-0.15 USD/kWh | Fuel cost per kWh - Diesel Standby: 0.08–0.15; dollar year 2026. |


Recorded gaps:

- Diesel storage and transfer — Fetch a named WHP/BEP design basis or utility specification with tank sizes and pump ratings
- Diesel storage and transfer — Fetch an OEM fuel-transfer-pump datasheet with flow, head and material specs

### Diesel-driven emergency generator with UPS/battery banks (whp-diesel-driven-emergency-generator-with-ups-battery-banks)

Primary code: UPS: Upstream
Emergency/essential diesel generator packages supply emergency, essential and main loads on ISO/IEC offshore units; JIP33 S-714-1J sets starting, battery, cooling, excitation and testing requirements. UPS/battery banks bridge the gap to generator pickup and support black start; the Equinor patent and Shell Timi design give battery/UPS architecture and energy levels. USCG/IEEE practice defines essential-generation loads including HVAC, potable water, instrument air and crane auxiliaries.
Vendors: Cummins, Caterpillar, Shell Malaysia Exploration and Production (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Diesel generator package (emergency/esse — Independent starting systems for emergency service | 2 systems | Diesel engines in emergency generator service shall have two independent starting systems |
| Diesel generator package (emergency/esse — Cranking cycles without recharge | 3 cycles of 15 s cranking + 15 s rest | Starting systems shall be rated for handling three consecutive cranking cycles, each of 15 s of cranking and 15 s of rest, without recharging the battery or pressurizing the air vessel or hydraulic oil accumulator |
| Diesel generator package (emergency/esse — Radiator / air cooler design margin | 110 % of heat load at maximum engine power | Radiators or external air coolers shall be designed for 110 % of the heat load at the maximum engine power, at the maximum ambient design temperature |
| Diesel generator package (emergency/esse — Water-cooled heat exchanger design margin | 110 % of maximum heat load | Water-cooled heat exchangers shall be designed for 110 % of the maximum heat load at the maximum cooling medium inlet temperature |
| Diesel generator package (emergency/esse — Insulated bearing threshold | 350 mV RMS shaft voltage | Bearing insulation shall be provided for generators with shaft voltage greater than 350 mV RMS value |
| Diesel generator package (emergency/esse — Personnel hot-surface protection threshold | 60 degC | In areas that are accessible during operation and inspection, protection against potential injury from surfaces exceeding 60 °C (140 °F) shall be provided |
| Diesel generator package (emergency/esse — Baseplate mounting pad flatness | 0.15 mm/m | Baseplate mounting pads shall be flat and parallel with each other to within 0,15 mm/m (0,002 in/ft) |
| Diesel generator package (emergency/esse — Baseplate surface finish | 3.2 µm Ra | The surface finish of baseplate mounting areas shall not exceed Ra 3,2 µm (125 µin) |
| Diesel generator package (emergency/esse — Lifting provision threshold | 25 kg | Components over 25 kg (55 lb) requiring removal for maintenance shall have lifting lugs or provisions for lifting eyebolts |
| UPS and battery bank with black-start ca — Low-power UPS-side energy level | 50-100 kWh | the first energy level may be in the range 50-100 kWh whereas the second energy level may be in the range 500-1000 kWh or higher |
| UPS and battery bank with black-start ca — High-power storage energy level | 500-1000 kWh | the first energy level may be in the range 50-100 kWh whereas the second energy level may be in the range 500-1000 kWh or higher |
| UPS and battery bank with black-start ca — Example battery bank (patent) | 1000 kWh (two batteries at 500 kWh) | In this example there are two batteries 66 rated at 500 kWh allowing for 1000 kWh for the second power supply apparatus when powered by the batteries 66 alone |
| UPS and battery bank with black-start ca — Emergency power rail | 400 V | a 400 V rail 72 for emergency power, which may be supplied from the first power supply apparatus 60 |
| UPS and battery bank with black-start ca — Generator rating in patent example | 5 MW | The gas turbine 68 is rated at 25 MW and generator, where present, might be 5 MW |
| Price — 500 kW diesel standby genset total installed (factory-direct) | 135000-305000 USD | A 500 kW commercial standby generator set costs 135,000 to 305,000 installed, with factory-direct options typically 30-50% below Tier 1 dealer quotes; dollar year 2026. |
| Price — 500 kW diesel standby genset total installed (Tier 1 dealer) | 320000-600000 USD | 500 kW ... Total Installed (Tier 1): 320,000-600,000; dollar year 2026. |
| Price — 100 kW diesel standby genset total installed (factory-direct) | 28000-73000 USD | 100 kW system runs 28,000-73,000 installed (factory-direct); dollar year 2026. |
| Price — 1,000 kW diesel standby genset total installed (factory-direct) | 300000-620000 USD | 1,000 kW ... Total Installed (Factory-Direct): 300,000-620,000; dollar year 2026. |
| Price — Diesel genset equipment cost | 180-400 USD/kW | Equipment costs for diesel standby gensets typically fall in the 180-400 per kW range for factory-direct units; dollar year 2026. |
| Price — US large industrial total installed cost | 250-450 USD/kW | United States - Total installed cost: 300-600/kW (small commercial), 250-450/kW (large industrial); dollar year 2026. |
| Price — Southeast Asia total installed cost | 280-550 USD/kW | Southeast Asia (Indonesia, Philippines, Vietnam) - Total installed cost: 280-550/kW; dollar year 2026. |
| Price — ATS 500-1,000 kW total cost | 23000-60000 USD | 500-1,000 kW ATS Equipment 15,000-40,000; ATS Installation 8,000-20,000; Total ATS Cost 23,000-60,000; dollar year 2026. |


Recorded gaps:

- Emergency generator and UPS — Fetch an EPC/operator project cost report or OEM offshore genset quotation with a stated dollar year
- Emergency generator and UPS — Fetch operator reliability data, OREDA-style handbook figures, or NFPA 110 test-frequency page with exact figures
- Emergency generator and UPS — Fetch an OEM offshore/marine UPS datasheet with printed efficiency and battery specs

### Firewater pumps, deluge/sprinkler system, hydrants and hose reels (whp-firewater-pumps-deluge-sprinkler-system-hydrants-and-hose-reels)

Primary code: UPS: Upstream
Offshore firewater systems use self-contained firewater pump packages (vertical suspended deep-well/wet-pit or horizontal OH/BB types, diesel or electric driven) feeding fixed deluge, hydrants and hose reels. IOGP S-721 and NFPA 20 set performance and testing; Ramboll/NPD report describes deluge and firewater philosophy on unmanned WHPs.
Vendors: NFPA 37 (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Firewater pump package (diesel or electr — Shutoff/deadhead pressure rise | 110-140 % of rated pressure at design conditions | The shutoff or deadhead pressure rise shall lie between 110 % and 140 % of rated pressure at design conditions |
| Firewater pump package (diesel or electr — Column pipe flow velocity at 100% rated flow | 4 m/s | column pipe flow velocity at 100 % rated flow not to exceed 4 m/s (13 ft/s) |
| Firewater pump package (diesel or electr — Screens/strainer blockage allowance in submergence calculation | 50 % | Submergence calculations shall include 50 % blockage of screens or strainer area |
| Firewater pump package (diesel or electr — Wave trough design return period for impeller submergence | 100 years | First stage impeller submergence for offshore pumps shall be the depth required to provide NPSH required by pump at end of curve duty point allowing for the specified 100 year wave trough depth |
| Firewater pump package (diesel or electr — Diesel engine site-rated power margin | 110 % of maximum required pump kW at peak load | Site rated engine power after NFPA 20 deductions shall be at least 110 % of the maximum required pump kW (bhp) at peak load, including gear and other transmission losses |
| Firewater pump package (diesel or electr — Diesel engine proven field operating service | 24000 hours | Design and mechanical construction of diesel engines, accessories, and auxiliary system components shall have at least 24 000 hours of field operating service |
| Firewater pump package (diesel or electr — Right-angle gearbox continuous operating capability | 15000 hours | Right angled gearboxes shall be capable of transmitting maximum power continuously for a minimum of 15 000 hours of operation |
| Firewater pump package (diesel or electr — Coupling service factor - electric motor via gearbox | 1.25 dimensionless | A service factor of 1,25 shall be used for pumps driven by an electric induction motor via a gearbox |
| Firewater pump package (diesel or electr — Coupling service factor - diesel engine via gearbox | 1.5 dimensionless | A service factor of 1,5 shall be used for pumps driven by a diesel engine via a gearbox |
| Firewater pump package (diesel or electr — Gearbox oil temperature to bearings / return oil | 50-80 degC | The temperature of the oil supply to the gearbox bearings shall not exceed 50 °C (120 °F); The temperature of the returning oil from the drain/sump ... shall not exceed the lesser of 80 °C (176 °F) or gearbox manufacturer’s maximum allowable oil temperature |
| Firewater pump package (diesel or electr — Independent starting systems | 2 systems | Engines shall be provided with two starting systems in accordance with NFPA 20 as primary and secondary starts |
| Reliability — Uptime of simple unmanned platforms | 95-99.5 % | Types 2 and 3 have very a high availability (uptime) - in the range of 95% - 99.5% |


Recorded gaps:

- Firewater system — Fetch NFPA 15 / ISO 13702 application pages or a WHP firewater design basis with densities and coverage
- Firewater system — Fetch the S-721D data sheet for a named project or an OEM firewater pump datasheet

### HVAC for equipment/MCC rooms (whp-hvac-for-equipment-mcc-rooms)

Primary code: UPS: Upstream
HVAC for electrical equipment/MCC rooms maintains temperature, humidity and pressurisation, provides dilution ventilation and isolates on fire/gas detection. Sources read: IEEE Houston offshore electrical design seminar (USCG ambient and HVAC rules) and PDHonline M332 HVAC Design for Oil & Gas Facilities (ISO 15138/NORSOK H-001 basis).
Vendors: IEEE Houston Section / PCIC (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| HVAC system for electrical/MCC rooms (DX — General design ambient temperature | 40 degC | Ambient temperature of 40 oC (104 oF) except for the following |
| HVAC system for electrical/MCC rooms (DX — Rotating electrical equipment in machinery rooms/weather decks | 50 degC | 50 oC (122 oF) for rotating electrical equipment in “Machinery Rooms” and “Weather Decks” [unless 45 oC (113 oF) can be shown as a maximum for these spaces] |
| HVAC system for electrical/MCC rooms (DX — Cables and non-rotating electrical equipment in machinery rooms/weather decks | 45 degC | 45 oC (113 oF) for Cables and other non-rotating electrical equipment for “Machinery Rooms” and “Weather Decks” |
| HVAC system for electrical/MCC rooms (DX — Air-conditioned space design temperature | 30 degC | 30 oC (86 oF) is permitted in air conditioned spaces (but 40 oC is norm) – duplication of HVAC recommended |
| HVAC system for electrical/MCC rooms (DX — Control and instrumentation equipment ambient | 55 degC | 55 oC (131 oF) for all control and instrumentation equipment |
| HVAC system for electrical/MCC rooms (DX — Electrical substation maximum temperature | 40 degC | The temperatures are generally not required to exceed 40° C in the electrical substations |
| HVAC system for electrical/MCC rooms (DX — Relative humidity target | 50 % +/- 5% | Offshore facilities are high in humidity, which needs to be controlled to comfortable levels of 50 ± 5% |
| HVAC system for electrical/MCC rooms (DX — Hazardous/non-hazardous pressure differential | 30-70 Pa | Maintenance of a pressure differential between hazardous and non-hazardous areas (generally in the range of 30 to 70 Pa) is essential to prevent ingress of toxic or hazardous gases |
| HVAC system for electrical/MCC rooms (DX — Process area mechanical ventilation rate | 12 air changes per hour (minimum) | The process areas should be provided with mechanical ventilation systems capable of continuously providing at least 12 air changes per hour |
| HVAC system for electrical/MCC rooms (DX — Supply / return duct pressure drop | 500-1500 Pa | The pressure drop in supply air ducting will be in the range of 1000 to 1500 Pa and that in return air ducting will be in the range of 500 to 1000 Pa |
| HVAC system for electrical/MCC rooms (DX — Minimum outside air in manned areas | 20 CFM per person | In all manned areas, HVAC systems should provide a minimum of 20 CFM of outside air per person |
| HVAC system for electrical/MCC rooms (DX — Minimum separation of air intake and extract outlet | 4.5 m | The separation between air intakes and extract outlets should be a minimum of 4.5m, but greater where practicable |
| HVAC system for electrical/MCC rooms (DX — HVAC motor rating | 50 degC rated motors | 50 degree C rated motors |
| Battery room ventilation (UPS/battery ba — Hydrogen concentration limit | 2 % by volume | Size the battery room ventilation system to prevent hydrogen concentration in the room from exceeding 2 percent by volume |
| Battery room ventilation (UPS/battery ba — Battery room air changes (if battery data unavailable) | 12 air changes per hour | In event the battery data is not available “maintain at least 12 air changes per hour” |
| Battery room ventilation (UPS/battery ba — ABS large battery room ventilation | 30 air changes per hour | ABS requires 1 air change every two minutes (30/hr) unless fewer are proven required through hydrogen emission calculations |
| Battery room ventilation (UPS/battery ba — Threshold for large battery room classification | 2 kW of connected charging device output (lead acid) | Large Battery Room > 2kW of connected charging device output (based on lead acid service) |


Recorded gaps:

- HVAC for equipment/MCC rooms — Fetch a named WHP HVAC design basis/equipment list
- HVAC for equipment/MCC rooms — Fetch an OEM HVAC package quotation or project cost report with dollar year

### Instrument/utility air compressors, receivers and dryers (whp-instrument-utility-air-compressors-receivers-and-dryers)

Primary code: UPS: Upstream
Instrument/utility air packages comprise rotary-screw, oil-free screw or reciprocating compressors, knock-out drum, filters, refrigerated or adsorption dryers, receiver tanks, piping, instrumentation and valves. Instrument air must be dry and oil-free and is typically distributed at 6 bar (100 psig).
Vendors: Booksite (Elsevier) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Instrument air package - compressor, KO  — Instrument air mains pressure | 6 bar | Air normally distributed at a mains pressure of 6 bar (100 psig) |
| Price — Cost of drying air for instrument air | 0.005 USD per standard m3 | Drying the air, for example for instrument air, typically adds about $0.005 per standard m 3 ($0.14/1000 scf) - Chemical Engineering Design 2nd ed., ©2013, no separate dollar year stated; dollar year 2013. |


Recorded gaps:

- Instrument/utility air — Fetch ISO 8573 (or equivalent) publisher page and an OEM dryer datasheet with pressure dew point
- Instrument/utility air — Fetch a named WHP utility design basis or OEM instrument-air skid datasheet

### Potable water storage and hot water system (whp-potable-water-storage-and-hot-water-system)

Primary code: UPS: Upstream
Potable water is bunkered to the installation, stored in dedicated tanks and distributed through domestic pipework with chlorination; hot water is provided by calorifiers where fitted. The Marine Safety Forum guidance gives water-quality limits, tank management and disinfection practice for offshore installations.
Vendors: Marine Safety Forum (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Potable water storage tank and domestic  — Free chlorine at point of delivery to vessel | 0.2-? ppm | The free chlorine concentrations in water must be maintained above 0.2ppm at the point of delivery to the vessel |
| Potable water storage tank and domestic  — Installation disinfection maintenance range | 0.2-0.5 ppm free chlorine | Can the installation demonstrate that it has maintained chlorination levels between 0.2ppm and 0.5ppm over a prolonged period of time? |
| Potable water storage tank and domestic  — Good-practice maximum storage before disposal | 14 days | Good practice would be to dispose of all water in such tanks after 14 days continuous storage |
| Potable water storage tank and domestic  — Super-chlorination concentration | 50 ppm (mg/l) | In order to achieve 50ppm (50mg/l) disinfectant in solution ... The disinfected water at 50ppm should be allowed to remain in the whole system for at least 1 hour |
| Potable water storage tank and domestic  — Coliforms / E.coli / Enterococci limit | 0 counts per 100 ml | Legislative limit is 0 counts per 100ml |
| Potable water storage tank and domestic  — Chlorides limit | 250 mgCl/l (less than) | Chlorides Legislative limits <250 mgCl/l |
| Potable water storage tank and domestic  — Total viable count at 22 degC / 37 degC | ?-300 cfu/ml | In the UKCS, a workable limit of 300cfu/ml at 22 oC and 100cfu/ml at 37 oC is regarded as acceptable |
| Potable water storage tank and domestic  — Hydrocarbons limit | 10 ppb (less than) | Hydrocarbons <10 ppb ... Less than 10ppb is the stated limit value as this is generally the limit of detection |
| Potable water storage tank and domestic  — Legionella limit | 100 cfu/litre (less than) | Legislative limit is <100 cfu/l |
| Price — Raw water rough cost estimate | 2 USD per 1000 gal | A very rough estimate of water costs can be made by assuming $2 per 1000 gal ($0.5 per metric ton) - Chemical Engineering Design 2nd ed., ©2013, dollar year not separately stated; dollar year 2013. |
| Price — Demineralised water cost multiple | 2 x raw water price | Demineralized water typically costs about double the price of raw water; dollar year 2013. |


Recorded gaps:

- Potable water and hot water — Fetch a named WHP design basis or accommodation-utilities specification with tank sizes and hot-water duties
- Potable water and hot water — Fetch an OEM potable-water/hot-water package datasheet

### Power generation (whp-power-generation)

Primary code: UPS: Upstream
Wellhead-platform power can be imported by subsea power cable from a host/CPP, generated locally by diesel or gas turbine, or supplied by a solar-PV/wind/battery hybrid with a standby diesel. Shell Timi (Malaysia) is the first SMEP wellhead platform fully powered by a solar-wind hybrid system; the Equinor patent describes a cascaded UPS/battery/black-start architecture for unmanned platforms.
Vendors: Shell Malaysia Exploration and Production (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Timi solar-wind hybrid power system with — Solar PV array rating | 14 kWp | an 80-m 2, 14-kWp solar photovoltaic array must be installed to generate the 25 kWh/d required to supply the load and charge the batteries during the day in the worst-case solar insolation conditions |
| Timi solar-wind hybrid power system with — Solar PV array area | 80 m2 | an 80-m 2, 14-kWp solar photovoltaic array must be installed to generate the 25 kWh/d required to supply the load and charge the batteries during the day in the worst-case solar insolation conditions |
| Timi solar-wind hybrid power system with — Solar daily energy target | 25 kWh/day | to generate the 25 kWh/d required to supply the load and charge the batteries during the day in the worst-case solar insolation conditions |
| Timi solar-wind hybrid power system with — Solar panel conversion efficiency | 18-22 % | Even given recent developments in solar-panel technology, the conversion efficiency of the panels is 18–22% |
| Timi solar-wind hybrid power system with — Total daily energy demand (Timi) | 73.6 kWh/day | The total daily energy demand will be 73.6 kWh, which corresponds to an average load of 3 kW |
| Timi solar-wind hybrid power system with — Average electrical load (Timi) | 3 kW | The total daily energy demand will be 73.6 kWh, which corresponds to an average load of 3 kW |
| Timi solar-wind hybrid power system with — Standby diesel generator rating (Timi) | 40 kWe | Standby power will be supplied by a diesel generator rated at 40 kWe |
| Timi solar-wind hybrid power system with — Selected battery autonomy (Timi) | 4 days | a 4-d autonomy was selected for Timi, which results in a smaller battery footprint and lower overall weight |
| Timi solar-wind hybrid power system with — Normal regional solar-platform autonomy | 5 days | A solar-powered platform in this region is normally designed for an autonomy of 5 d to cater for the cloudy days during the monsoon season |
| Timi solar-wind hybrid power system with — Solar panel tilt angle | 5 degrees | a solar panel tilt angle of 5°, instead of the 15° specified in the Shell design and engineering practice for solar energy installations, will be used for better optimisation of insolation |
| Timi solar-wind hybrid power system with — Solar PV frame maximum design wind speed | 33 m/s | The solar photovoltaic panel frame supports are designed for a maximum wind speed of 33 m/s, which is much higher than the typical maximum 10-min wind speed of 20 m/s experienced in Malaysian waters in recent years |
| Timi solar-wind hybrid power system with — Typical maximum 10-min wind speed, Malaysian waters | 20 m/s | much higher than the typical maximum 10-min wind speed of 20 m/s experienced in Malaysian waters in recent years |
| Timi solar-wind hybrid power system with — Average wind speed offshore Malaysia | 3-6 m/s | According to wind data from NASA, the average wind speed in the waters offshore peninsular Malaysia and Sabah and Sarawak states is 3–6 m/s |
| Timi solar-wind hybrid power system with — Generation-level DC voltage | 48 V DC | A higher voltage, 48 instead of 24 V DC, will be used at the power generation level to reduce the size of the cables and batteries and the number of controllers required |
| Subsea power cable from host/CPP to unma — Power cable rating (low-power host supply) | 50-200 kW | the power supply via the power cable may be rated at 50-200 kW, such as at about 100 kW |
| Subsea power cable from host/CPP to unma — Low-power first energy level | 50-100 kWh | the first energy level may be in the range 50-100 kWh whereas the second energy level may be in the range 500-1000 kWh or higher |
| Subsea power cable from host/CPP to unma — High-power second energy level | 500-1000 kWh | the first energy level may be in the range 50-100 kWh whereas the second energy level may be in the range 500-1000 kWh or higher |
| Subsea power cable from host/CPP to unma — Gas turbine rating in example | 25 MW | a gas turbine is used then it may be rated at the power level higher than the high-power energy storage system ... a 25 MW turbine may be present |
| Reliability — Availability of simple unmanned platforms (Types 2 and 3) | 95-99.5 % uptime | Generally, there are good experiences with the UWHPs. Types 2 and 3 have very a high availability (uptime) - in the range of 95% - 99.5% |
| Price — Wholesale electricity benchmark (North America) | 0.06 USD/kWh | Wholesale electricity prices vary regionally ... but are typically about $0.06/kWh in North America at the time of writing (Chemical Engineering Design, 2nd ed., ©2013); dollar year 2013. |


Recorded gaps:

- Power generation — Fetch a Shell/operator detailed Timi electrical design paper or EPC vendor data sheet
- Power generation — Fetch an umbilical/cable OEM datasheet and a host-to-WHP power-from-shore project page
- Power generation — Seek a project cost breakdown or Shell announcement with figures and dollar year

### Seawater lift pumps (whp-seawater-lift-pumps)

Primary code: UPS: Upstream
Seawater lift pumps draw seawater from caissons/wells for cooling, firewater, washing and ballast duties. BP Shah Deniz 2 project description gives MODU/water-system duties and extraction rates; IOGP S-721 sets vertical-pump submergence, anti-fouling and column-pipe requirements; Celeros/S&N and ClydeUnion are named suppliers.
Vendors: BP (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Vertical seawater lift pump (MODU/rig an — Seawater lift pump capacity (Heydar Aliyev MODU) | 960 m3/hr | 6 seawater lift pumps, but typically 2 used which are designed to lift up to 960m 3/hr from a depth below sea level of between 17.5 and 19.5m |
| Vertical seawater lift pump (MODU/rig an — Suction depth (Heydar Aliyev MODU) | 17.5-19.5 m below sea level | designed to lift up to 960m 3/hr from a depth below sea level of between 17.5 and 19.5m |
| Vertical seawater lift pump (MODU/rig an — Seawater lift pump capacity (Istiglal MODU) | 230 m3/hr | Seawater lift pumps designed to lift up to 230m 3/hr from a depth below sea level of 9.8m |
| Vertical seawater lift pump (MODU/rig an — Suction depth (Istiglal MODU) | 9.8 m below sea level | designed to lift up to 230m 3/hr from a depth below sea level of 9.8m |
| Vertical seawater lift pump (MODU/rig an — Maximum seawater extraction per pump (SD2 platform caisson) | 2173 m3/hr | Seawater will be extracted from 1 of the 2 vertical seawater lift pump caissons at a depth of -75m below sea level. The maximum seawater extraction design flow rate per pump will be approximately 2,173m3/hr |
| Vertical seawater lift pump (MODU/rig an — Sea intake screen mesh | 200 mm diameter | The design of the seawater intake caissons on the platform will incorporate a mesh of 200mm diameter |
| Vertical seawater lift pump (MODU/rig an — Filtration after lift | 50 microns | and then filtered to remove any particles that are above 50 microns in diameter |
| Vertical seawater lift pump (MODU/rig an — Column pipe velocity at 100% rated flow (S-721) | 4 m/s | column pipe flow velocity at 100 % rated flow not to exceed 4 m/s (13 ft/s) |
| Price — Cooling-water system make-up and chemical treatment cost | 0.02 USD/1000 gal | The costs of water make-up and chemical treatment usually add about $0.02/1000 gal - Chemical Engineering Design 2nd ed., ©2013; dollar year 2013. |
| Price — Recirculating cooling water pumping power | 1-2 kWh/1000 gal circulated | The power used in a typical recirculating cooling water system is usually between 1 and 2 kWh/1000 gal of circulating water; dollar year 2013. |


Recorded gaps:

- Seawater lift pumps — Fetch an S&N Pumps or ClydeUnion seawater lift pump datasheet
- Seawater lift pumps — Seek operator reliability data or an OEM maintenance manual

## whp-well-system

### Drilling slots / well bays (whp-drilling-slots-well-bays)

Primary code: UPS: Upstream
Malaysian Tarpon minimum-facility WHPs for PETRONAS Carigali were built with three 20-inch conductor slots internal to the caisson (two used, one spare) in 70-85 m water, while the West Desaru conductor-supported WSS grew from 18 wellhead flowline connections at the outset to 28 in the final design.
Vendors: Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Conductor slot / well bay slot (Tarpon p — conductor slots per platform | 3 slots | KMSE and AJK WHPs: three 20-inch conductor slots internal to caisson, two utilised and one spare |
| Conductor slot / well bay slot (Tarpon p — water depth | 70-85 m | Detailed design, fabrication, transport and installation of WHPs in water depths varying from 70 m to 85 m |
| Conductor slot / well bay slot (Tarpon p — wellhead flowline connections (design growth) | 18-28 connections | West Desaru WSS topsides: wellhead flowline connections grew from 18 slots at outset to 28 because of drilling/completion scope growth |
| Reliability — operational design life | 20 years | Tarpon platforms designed for a 20-year operational lifespan and relocatable |
| Reliability — minimum design fatigue life | 10 years | West Desaru WSS minimum 10-year design fatigue life; structure re-designed after slot growth |


Recorded gaps:

- 4-12 slots typical range — Find a primary page or standard that prints a slot-count range before recording it
- slot spacing and wellbay layout — Source a GA drawing with printed slot spacing
- price/cost per slot — Find a sourced USD cost with dollar year and basis

### ESD stations at strategic locations (whp-esd-stations-at-strategic-locations)

Primary code: UPS: Upstream
Offshore Magazine reports a wellhead control panel and control and safety systems on the West Desaru WSS, and the cited API RP 14C training slides print a five-level shutdown hierarchy driven by manual, fire-and-gas and hydraulic-pressure inputs.
Vendors: IPS Group BV (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Emergency shutdown (ESD) system and manu — shutdown levels | 5 levels | Shutdown logic: Level 1 APS abandon platform; Level 2 ESD I total; Level 3 ESD II partial; Level 4 PSD total; Level 5 PSD partial |
| Emergency shutdown (ESD) system and manu — levels of protection | 2 levels | Premises for basic analysis and design include two levels of protection with primary and secondary activation order |
| Emergency shutdown (ESD) system and manu — low-pressure sensor exemption length | 10 ft (3 m) | SAC A.1 Wellheads and Flow Lines: PSL installed; flow line segment between well and first choking device less than 10 feet (3 m) |
| Emergency shutdown (ESD) system and manu — ESD actions on SCSSV | 1 function | ESD actions may include closure of SSVs and, where included in the engineered safety design, initiation of SCSSV closure |
| Reliability — SIL 1 probability of dangerous failure on demand (low demand) | 0.01-0.1 PFD | PFD 0.1-0.01, RRF 10-100, low demand operation per IEC EN 61508 as printed in table |
| Reliability — SIL 2 probability of dangerous failure on demand (low demand) | 0.001-0.01 PFD | PFD 0.01-0.001, RRF 100-1000, low demand operation per IEC EN 61508 |
| Reliability — SIL 3 probability of dangerous failure on demand (low demand) | 0.0001-0.001 PFD | PFD 0.001-0.0001, RRF 1000-10,000, low demand operation per IEC EN 61508 |
| Reliability — SIL 4 probability of dangerous failure on demand (low demand) | 1e-05-0.0001 PFD | PFD 0.0001-0.00001, RRF 10,000-100,000, low demand operation per IEC EN 61508 |


Recorded gaps:

- ESD station locations (boat landing, cellar deck, tree area) — Find an WHP ESD philosophy or layout drawing
- SIL target for WHP ESD functions — Find a project-specific SIL study
- proof-test interval for ESD final elements — Source a printed proof-test interval
- price/cost of ESD stations — Find a sourced USD cost with year and basis

### Gas lift manifold and flowlines for artificial lift (whp-gas-lift-manifold-and-flowlines-for-artificial-lift)

Primary code: UPS: Upstream
The West Desaru conductor-supported WSS topsides were designed with gas lift flowlines alongside oil production and water injection flowlines, and Baker Hughes supplies injection-pressure and production-pressure-operated gas lift valves for continuous or intermittent lift.
Vendors: Baker Hughes, Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Gas lift valves and mandrels — valve operating principles | 2 types | Baker Hughes lists injection pressure and production pressure-operated valves |
| Gas lift valves and mandrels — mandrel compatibility | 0 count | Designed for any Baker Hughes side pocket and tubing retrievable mandrel and fully compatible with other manufacturers' mandrels |
| Gas lift flowlines (WHP topsides) — gas lift flowline presence | 1 system | West Desaru WSS topsides accommodate 28 dry tree completions and associated oil production, gas lift and water injection flowlines |


Recorded gaps:

- gas lift manifold size, pressure and material — Source an OEM gas lift manifold datasheet
- injection gas rate and pressure — Find a project design basis with gas injection figures
- price/cost of gas lift manifold and flowlines — Find a sourced USD cost with year and basis

### Water injection manifold and W.I. pig launcher/receiver (whp-water-injection-manifold-and-w-i-pig-launcher-receiver)

Primary code: UPS: Upstream
The West Desaru WSS houses water injection flowlines, manifolds and a pig launcher, with produced oil routed to the FP5 MOPU and exported through a 14-km subsea pipeline to an FSO via an 8-in flexible riser.
Vendors: Aquaterra Energy (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Water injection flowlines and manifold — water injection flowline presence | 1 system | West Desaru WSS topsides accommodate oil production, gas lift and water injection flowlines plus manifolds |
| Pig launcher and flexible riser — flexible riser diameter | 8 in (20 cm) | West Desaru WSS houses a pig launcher and an 8-in (20-cm) flexible riser |
| Pig launcher and flexible riser — subsea export pipeline length | 14 km | Produced oil processed at MOPU then returned to WSS for export via 14-km (8.7-mi) subsea pipeline to an FSO |


Recorded gaps:

- W.I. pig receiver location and size — Source a project P&ID showing the pig trap pair
- water injection manifold rating and number of slots — Find an OEM water injection manifold datasheet
- price/cost of W.I. manifold and pig launcher — Find a sourced USD cost with year and basis

### Well test facilities: test manifold with either a test separator or a multiphase flow meter (whp-well-test-facilities-test-manifold-with-either-a-test-separator-or-a-m)

Primary code: UPS: Upstream
OilGasz states a test manifold routes a selected well to a test separator, an MPFM or other measurement equipment, and Emerson describes the Roxar 2600 MPFM as a compact vertical inline meter giving three-phase rates without separation across 0-100% GVF and 0-100% WLR.
Vendors: SLB (Cameron pressure control equipment) (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Roxar 2600 Multiphase Flow Meter — available sizes | 6 sizes | Roxar 2600 MPFM available in 6 sizes, with materials from duplex stainless steel to Inconel and enclosures in SS316 or painted aluminum |
| Roxar 2600 Multiphase Flow Meter — gas volume fraction range | 0-100 % GVF | Both gamma and non-gamma versions deliver reliable performance across 0-100% GVF and 0-100% WLR |
| Roxar 2600 Multiphase Flow Meter — water liquid ratio range | 0-100 % WLR | 0-100% WLR operating envelope printed on Emerson multiphase flow page |
| Roxar 2600 Multiphase Flow Meter — measurement update rate | 10 per second | Phase fraction and flow rate calculations at high resolution of 10 times a second |
| Roxar 2600 Multiphase Flow Meter — field experience | 30 years | Emerson states over 30 years of field experience and a global presence for its MPFMs |
| Vx Spectra surface multiphase flowmeter — high-GVF threshold | 95 % GVF | Triple-energy source improves liquid rates and water/liquid ratio at GVF greater than 95% |
| Test separator / test manifold — test separator vs MPFM trade-off | 0 count | Test separators may offer lower uncertainty in controlled conditions; MPFMs provide higher operational efficiency and reduce space, weight and piping |
| Reliability — calibration/verification interval | 1 year | Typical recommendation is yearly checks and verification; calibration verified using test separator data or sampling |
| Reliability — moving parts | 0 count | Roxar 2600 has no moving parts, reducing wear and maintenance needs and the need for spare parts |


Recorded gaps:

- test separator sizing and duty for a Malaysian WHP — Source a test separator datasheet
- MPFM turndown figures from a fetched page — Fetch the specific product datasheet that prints turndown
- price/cost of MPFM or test separator — Find a sourced USD cost with year and basis

### Wellhead Control Panel (whp-wellhead-control-panel)

Primary code: UPS: Upstream
A multi-well hydraulic wellhead control panel described by IPS Group BV operates nine wells (seven installed, two spare) using four pressure levels - 480 bar for SCSSVs, 280 bar for SSVs/SDVs, 150 bar for the field loop and 6 bar control pressure.
Vendors: IPS Group BV (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Wellhead control panel (multi-well, hydr — wells controlled | 9 wells | System designed to operate nine production wells, seven installed and two spare |
| Wellhead control panel (multi-well, hydr — VHP header pressure | 480 bar | 480 bars (VHP header) for the 9 x SCSSV |
| Wellhead control panel (multi-well, hydr — MHP header pressure | 280 bar | 280 bar (MHP header) for the 9 x SSV and 9 x SDV valves |
| Wellhead control panel (multi-well, hydr — HP header pressure | 150 bar | 150 bar (HP header) for field loop of 9 ROCV, 10 ESDV, 14 SDV and 4 BDV |
| Wellhead control panel (multi-well, hydr — LP header pressure | 6 bar | 6 bar (LP header) control pressure, generated by reduction from HP header through two regulators |
| Wellhead control panel (multi-well, hydr — VHP accumulator volume | 5 litre | VHP header equipped with 5 litre bladder accumulators, nitrogen precharge 357.2 bar |
| Wellhead control panel (multi-well, hydr — MHP/HP accumulator volume | 35 litre | MHP header 35 litre bladder accumulators precharge 170.9 bar; HP header 35 litre precharge 98.9 bar |
| Wellhead control panel (multi-well, hydr — actuated valve pressure capability | 15000 psi | INTECH modular single and multi-well panels can operate valves of up to 15,000 psi |
| Single-well wellhead control panel — wells controlled | 1 well | System designed to operate one production well; operates SCSSV, production master valve, production wing valve, choke valve and methanol injection valve |
| Reliability — accumulator precharge check interval | 1 year | The pre-charge pressure must be checked at least once per year and if necessary charged again |
| Reliability — pump redundancy | 2 pumps per pressure level | Each pressure level has two dedicated electric driven pumps (A and B) |
| Reliability — design operational life | 25 years | INTECH panels can be designed for up to 25 years of operational life, with optional extended O&M support |
| Reliability — hydraulic system low-pressure trip | 0 count | API RP 14C training slides list 'Low pressure hydraulic system' as an input to ESD II |


Recorded gaps:

- WCP/HPU specification on a named Malaysian WHP — Find a project-specific WHCP datasheet
- hydraulic fluid type and HPU power rating — Source an HPU datasheet
- price/cost of WCP/HPU — Find a sourced USD cost with year and basis

### Wellheads and Christmas trees (whp-wellheads-and-christmas-trees)

Primary code: UPS: Upstream
The West Desaru WSS carried 28 dry-tree completions using single, dual and triple splitter wellheads, and ISO 10423:2022 states that it supplements API Spec 6A, 21st edition (2018), for wellhead and tree equipment.
Vendors: Baker Hughes, TechnipFMC (CDS Separation Systems), Aker Solutions (0 model lines recorded).

| Specification | Value | Basis |
| --- | --- | --- |
| Dry-tree (surface) Christmas tree assemb — master valve redundancy | 2 valves | Typically two master valves (lower and upper) provide redundancy; if one fails the other can perform the function |
| Dry-tree (surface) Christmas tree assemb — pressure rating (subsea tree systems) | 15000 psi | Baker Hughes provides 5-inch and 7-inch systems with up-to 15,000 psi pressure rating capability |
| Dry-tree (surface) Christmas tree assemb — water depth capability | 10000 ft | Baker Hughes tree systems facilitate control of intelligent completions in water depths up to 10,000 ft |
| Dry-tree (surface) Christmas tree assemb — HPHT flowing temperature | 350 degF | Baker Hughes HPHT Tree system: production pressures up to 15,000 psi, flowing temperatures up to 350 degF |
| Dry-tree (surface) Christmas tree assemb — tree configuration count | 28 completions | West Desaru WSS topsides accommodate 28 dry tree well completions comprising single, dual and triple splitter wellheads |
| IC conventional wellhead system (SLB/Cam — pressure rating | 10000 psi | Rated up to 10,000 psi, can be configured for many service conditions |
| IC conventional wellhead system (SLB/Cam — load shoulder angle | 45 degrees | IC wellhead system uses a straight-bore design with a 45-degree load shoulder |
| Reliability — two master valves used for redundancy | 2 valves | DrillingFormulas: two master valves provide redundancy so another can perform the function if one fails |
| Reliability — fail-safe closed hydraulic wing valve | 0 count | Hydraulic operated wing valves usually fail safe closed, requiring active hydraulic pressure to stay open; loss of control fluid shuts the well in |


Recorded gaps:

- printed pressure class table for API 6A (2,000/3,000/5,000/10,000/15,000/20,000 psi) — Read the standard or an OEM datasheet that prints the class table
- single/dual/triple splitter dimensional details — Find a manufacturer datasheet for splitter wellheads
- price/cost of dry trees — Find a sourced USD figure with year and basis
