# ELE technology options

17 technologies, from commercial to lab stage. Generated from catalog/technologies/; every figure links to its source.

| Technology | Category | Maturity | TRL | Suppliers | Cost figures |
| --- | --- | --- | --- | --- | --- |
| [Earthing and lightning protection](#ele-earthing-lightning) | Electrical safety | commercial |  | nVent ERICO (earthing and lightning protection systems); Dehn (lightning and surge protection); Furse (lightning protection systems) |  |
| [Electrical heat tracing](#ele-heat-tracing) | Electrical heating | commercial |  | nVent (Raychem heat tracing systems); Chromalox (industrial heat tracing); Emerson (industrial heat tracing (Bergman Series)) |  |
| [Emergency, standby and UPS power systems](#ele-emergency-up-power) | Emergency power | commercial |  | Cummins (generator sets); Eaton (UPS systems); ABB (UPS and emergency power); Schneider Electric (Galaxy UPS systems); Vertiv (critical power UPS) |  |
| [Grid connection and interconnection studies](#ele-grid-connection) | Power generation and distribution | commercial |  | Grid System Operator (GSO) (Malaysian grid code administration); Tenaga Nasional Berhad (TNB) (connection offer and network access); Siemens PTI (PSS/E modelling and grid studies) |  |
| [HV/MV switchgear and site power distribution](#ele-hv-switchgear-distribution) | Power distribution | commercial |  | ABB (MV/LV switchgear, UniGear, HySec); Schneider Electric (MV switchgear, RM6, SM6); Siemens Energy (switchgear and grid solutions); Hitachi Energy (HV switchgear, GIS); Eaton (MV/LV switchgear and MCCs) |  |
| [Hazardous area electrical equipment](#ele-hazardous-area-electrical) | Explosion protection | commercial |  | Eaton Crouse-Hinds (Ex enclosures and lighting); R. Stahl (Ex equipment and IS barriers); Pepperl+Fuchs (intrinsic safety interfaces); ABB (Ex motors and instrumentation); Emerson (Ex-rated instrumentation) |  |
| [Low-voltage distribution (415/240 V)](#ele-lv-distribution) | Power generation and distribution | commercial |  | Schneider Electric (Prisma/Blokset switchboards, Acti9 MCBs); ABB (MNS boards, S200 MCBs); Siemens (Sivacon switchboards); Eaton (xEnergy boards) |  |
| [Medium-voltage distribution (11 kV and 33 kV)](#ele-mv-distribution) | Power generation and distribution | commercial |  | ABB (SafeRing/SafePlus RMUs, UniGear MV switchgear); Schneider Electric (RM6, Premset, SM6); Siemens (8DJH RMU, NXPlusC); Eaton (Xiria medium-voltage switchgear) |  |
| [Motors and variable speed drives](#ele-motors-drives) | Electrical drives | commercial |  | ABB (motors and drives, ACS family); WEG (motors and MV drives); Siemens Energy (large drives and motors); Nidec (industrial motors) |  |
| [On-site gas turbine power generation](#ele-gt-power-generation) | Power generation | commercial |  | Siemens Energy (industrial and aeroderivative gas turbines); Mitsubishi Heavy Industries (gas turbines); Baker Hughes (NovaLT and aeroderivative gensets); MAN Energy Solutions (gensets) |  |
| [Overhead transmission lines (132-500 kV)](#ele-transmission-lines) | Power generation and distribution | commercial |  | Siemens Energy (grid transmission equipment); GE Vernova (grid solutions); Hitachi Energy (FACTS and transmission equipment); Tenaga Nasional Berhad (TNB) (owner and operator of the Peninsular grid) |  |
| [Power and control cable systems](#ele-cable-systems) | Power distribution | commercial |  | Prysmian (power and submarine cable systems); Nexans (power, instrument and subsea cables); LS Cable & System (power cables) |  |
| [Power and distribution transformers](#ele-transformers) | Power transformation | commercial |  | Hitachi Energy (power, distribution, GIT and dry-type transformers); Siemens Energy (power and distribution transformers); GE Vernova (power transformers); WEG (distribution and special transformers) |  |
| [Power management and electrical SCADA](#ele-power-management-systems) | Electrical automation | commercial |  | GE Vernova (power management systems); ABB (electrical SCADA and PMS); Schneider Electric (EcoStruxure Power and PMS); Hitachi Energy (grid automation) |  |
| [Power system protection and relaying](#ele-protection-relaying) | Power protection | commercial |  | Schweitzer Engineering Laboratories (protective relays and automation platforms); ABB (Relion protection and control); Schneider Electric (Easergy protection relays); Siemens Energy (SIPROTEC protection relays); GE Vernova (Multilin protection relays) |  |
| [Subsea power and umbilical systems](#ele-subsea-umbilicals-power) | Subsea electrical | commercial |  | Aker Solutions (umbilicals and subsea power); Nexans (subsea cables and umbilicals); Siemens Energy (subsea power grids and drives) |  |
| [UHV and HV substations (275-500 kV)](#ele-uhv-substations) | Power generation and distribution | commercial |  | Hitachi Energy (power transformers, GIS and HVDC); Siemens Energy (GIS, transformers and substation automation); GE Vernova (high-voltage equipment); Hyundai Electric (transformers and switchgear) |  |

## Earthing and lightning protection
<a id="ele-earthing-lightning"></a>

Earthing connects metalwork and neutral points to earth so that fault current, lightning and static charge have a safe, low-impedance path and touch voltages stay within limits; lightning protection intercepts strikes with air terminals and down conductors and disposes of the surge through the earth grid. Plant design separates power, instrument and clean earths, bonds across structures and pipelines, and fits surge protective devices on vulnerable circuits. Design rules come from IEC 62305 (lightning), IEC 60364 (installations) and company earth-grid studies for soil resistivity and fault current.

```mermaid
flowchart LR
    STU["Soil resistivity surveyed; earth grid sized for fault current and step/touch limits<br/><small>earth rods, grid conductors</small>"]
    BND["Metalwork, structures and cable armour bonded into the grid<br/><small>bonding conductors</small>"]
    LPS["Air terminals, down conductors and earth termination intercept and discharge strikes<br/><small>air terminals, down conductors</small>"]
    SPD["Surge protective devices staged on power and signal circuits<br/><small>SPDs</small>"]
    STU --> BND
    BND --> LPS
    LPS --> SPD
```

**Key equipment:** earth rods and grid, bonding conductors, air terminals, surge protective devices, test links.

**Performance:**
- transmission voltage levels needing insulation coordination: 132-500 kV; TNB transmission at 132-500 kV drives arresters and clearances. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per substation earthing system (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.hse.gov.uk/electricity/), [2](https://www.dehn-international.com/en), [3](https://www.iec.ch/standards), [4](https://www.tnb.com.my/), [5](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Electrical heat tracing
<a id="ele-heat-tracing"></a>

Electrical heat tracing maintains or raises the temperature of pipes, tanks and instruments by applying heat along the surface. Self-regulating parallel trace cables vary their resistance with temperature and cannot overheat a dry section, constant-wattage cables deliver fixed power, and mineral-insulated or skin-effect systems serve long, hot or high-power duties. Heating replaces or supplements steam tracing, and digital control panels monitor every circuit for current and temperature alarms.

```mermaid
flowchart LR
    SEL["Cable type and output selected from heat-loss calculation<br/><small>heat-loss software, trace cable</small>"]
    INS["Cable applied along the line with terminations and junction boxes<br/><small>trace cable, junction boxes</small>"]
    INSU["Insulation installed; trace and sensor routing verified<br/><small>insulation, RTDs</small>"]
    CTL["Control panels switch and monitor circuits by ambient or line temperature<br/><small>control panels, contactors</small>"]
    SEL --> INS
    INS --> INSU
    INSU --> CTL
```

**Key equipment:** self-regulating trace cable, constant-wattage cable, mineral-insulated cable, control and monitoring panels, RTDs.

**Performance:**
- heat-tracing supply voltage: 230-415 V; single-phase 230 V and three-phase 415 V tracing at Malaysian LV. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per metre of traced pipe (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.chromalox.com/), [2](https://www.nvent.com/), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Emergency, standby and UPS power systems
<a id="ele-emergency-up-power"></a>

A facility secures loads that must not fail through layers: battery-backed uninterruptible power supplies (classified VFI, VI or DXI by output dependency under IEC 62040-3) ride through the first seconds, standby generating sets start and close onto the emergency bus, and automatic transfer switching restores normal supply after the outage. Emergency generation is sized for essential process, fire and life-safety loads; batteries carry instrumentation, control and safety systems through the transition and support black-start of larger units.

```mermaid
flowchart LR
    FLT["Normal supply fails; undervoltage detected<br/><small>protection relays, voltage sensing</small>"]
    UPS["UPS carries critical loads from batteries<br/><small>UPS, battery bank</small>"]
    GEN["Standby genset starts and closes onto the emergency bus<br/><small>diesel genset, automatic transfer switch</small>"]
    RES["Load shed/blocks restored in priority sequence<br/><small>load-shed scheme</small>"]
    REC["Normal supply returns; retransfer and battery recharge<br/><small>charger, ATS</small>"]
    FLT --> UPS
    UPS --> GEN
    GEN --> RES
    RES --> REC
```

**Key equipment:** standby diesel or gas gensets, UPS units, battery banks (VRLA, lithium), automatic transfer switches, battery chargers.

**Performance:**
- LV standby supply voltage: 400-415 V; standby generators and UPS output at the TNB LV level. [source](https://www.tnb.com.my/)
- required periodic inspection for MV installations: 4 visits/month; Energy Commission inspection frequency above 11 kV to 132 kV. [source](https://www.st.gov.my/)

**Missing inputs:**
- cost per kVA of standby capacity installed (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.iec.ch/standards), [2](https://www.hse.gov.uk/electricity/), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Grid connection and interconnection studies
<a id="ele-grid-connection"></a>

A connection must satisfy the Malaysian Grid Code, which the Grid System Operator owns and administers. The chain is load-flow, short-circuit and transient-stability modelling of the proposed connection, then compliance checks for voltage limits, fault ride-through and reactive capability, then a connection agreement with TNB and GSO approval before energisation. Industrial loads above about 25,000 kVA take supply at 132 kV or 275 kV, which places them inside grid-code territory.

```mermaid
flowchart LR
    APP["Connection application and data pack<br/><small>load or generation data, single-line diagram, network model (PSS/E or DIgSILENT)</small>"]
    STUDY["Grid impact study<br/><small>load-flow, short-circuit, transient-stability simulation</small>"]
    COMPLY["Grid-code compliance<br/><small>voltage and fault ride-through checks, reactive capability, protection coordination</small>"]
    AGREE["Connection agreement and approval<br/><small>TNB connection offer, GSO approval</small>"]
    COMM["Commissioning and energisation<br/><small>witnessed acceptance tests, protection settings handover</small>"]
    APP --> STUDY
    STUDY -->|compliance findings| COMPLY
    COMPLY -->|compliance report to GSO| AGREE
    AGREE --> COMM
```

**Key equipment:** network modelling software, protection coordination tools, commissioning test sets.

**Performance:**
- TNB 132/275 kV supply threshold: 25000 kVA; TNB supplies 132 kV and 275 kV for demands above about 25,000 kVA. [source](https://www.tnb.com.my/)
- transmission voltage tolerance at 132/275 kV: -5-10 %; TNB limits at 132 kV and 275 kV. [source](https://www.tnb.com.my/)

**Missing inputs:**
- study cost per MW connected, with a Malaysian consultant benchmark (costs): Consultancies do not publish study prices. Where: Ask the owner for a benchmarked study cost. Next: Ask owner for a priced reference.

Sources: [1](https://www.gso.org.my/). Last reviewed 2026-11-13.

## HV/MV switchgear and site power distribution
<a id="ele-hv-switchgear-distribution"></a>

Medium-voltage switchgear receives, protects and distributes electrical power across a facility. Power arrives from utility infeed or site generation at high voltage (typically 132 kV and above for large plants), is transformed to a main distribution voltage (usually 11 kV or 33/36 kV onshore, 11 kV offshore), and flows through switchboards to transformers, motors and downstream boards. Air-insulated, gas-insulated (GIS) and hybrid designs exist; modern breakers use vacuum or SF6 interrupting technology.

```mermaid
flowchart LR
    IN["Incoming supply from utility infeed, generators or interconnector<br/><small>HV switchgear, cable terminations</small>"]
    SW["Main switchboard switches, protects and meters the bus<br/><small>circuit breakers, busbars, protection relays</small>"]
    TR["Distribution transformers step down to LV or lower MV levels<br/><small>power transformers</small>"]
    LD["Motor control centres and LV boards feed process loads<br/><small>MCCs, LV switchboards</small>"]
    BK["Downstream faults are cleared selectively by graded protection<br/><small>relays, fuses</small>"]
    IN --> SW
    SW --> TR
    TR --> LD
    LD --> BK
```

**Key equipment:** circuit breakers (vacuum, SF6), switchboards, busbars, ring main units, power transformers, protection relays, surge arresters.

**Performance:**
- IEC 62271-200 rated voltage range of metal-enclosed MV switchgear: 1-52 kV; IEC 62271-200 covers AC metal-enclosed switchgear and controlgear above 1 kV up to and including 52 kV. [source](https://www.iec.ch/standards)

**Missing inputs:**
- cost per panel by voltage class (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.iec.ch/standards), [2](https://www.hitachienergy.com/products-and-solutions/transformers), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Hazardous area electrical equipment
<a id="ele-hazardous-area-electrical"></a>

Where flammable atmospheres can occur, electrical equipment is selected to exclude or contain ignition sources. Areas are classified by likelihood and duration (gas: Zone 0/1/2; dust: Zone 20/21/22) under IEC 60079-10 or DSEAR in the UK, then protected by equipment protection concepts matched to the zone: intrinsic safety (Ex ia/ib) for instrumentation, flameproof enclosures (Ex d), increased safety (Ex e), pressurisation (Ex p), encapsulation (Ex m) and others. The IECEx certification system covers equipment certification, conformity of installation and personnel competence across member countries.

```mermaid
flowchart LR
    CLA["Hazardous area classification maps zones from leak sources and dispersion<br/><small>dispersion studies</small>"]
    SEL["Ex protection concept selected per zone and equipment group<br/><small>Ex-rated equipment</small>"]
    INS["Certified installation with correct glands, bonding and segregation<br/><small>cable glands, earthing</small>"]
    CHK["Initial and periodic inspections verify Ex integrity<br/><small>inspection records</small>"]
    CLA --> SEL
    SEL --> INS
    INS --> CHK
```

**Key equipment:** flameproof enclosures, intrinsically safe circuits and isolators, purge and pressurisation panels, Ex lighting and motors, sealing glands.

**Performance:**
- LV equipment used in hazardous areas: 400-415 V; hazardous-area equipment operates at the TNB LV level in process plants. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost premium of Ex-rated over standard equipment (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.iecex.com/), [2](https://www.iec.ch/standards), [3](https://www.hse.gov.uk/electricity/), [4](https://www.tnb.com.my/), [5](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Low-voltage distribution (415/240 V)
<a id="ele-lv-distribution"></a>

The Malaysian LV level: TNB supplies 415/240 V (also written 400/230 V) three-phase four-wire to premises up to roughly 1,000 kVA via CT metering. Within the installation a main switchboard divides into sub-boards, motor control centres and final circuits; discrimination between breakers and the fault level at each board set the breaking capacities. Per the Electricity Regulations, LV work is done by licensed wiremen/chargemen and needs a Test Certificate (Form H) before TNB energises.

```mermaid
flowchart LR
    SUPPLY["TNB LV supply point (415/240 V, CT metered above 100 A)<br/><small>service cable, meter, main switch</small>"]
    MSB["Main switchboard: incomer and busbar<br/><small>air circuit breaker (ACB) incomer, busbar 630-3200 A, surge protective device</small>"]
    MCC["Motor control centre<br/><small>moulded-case breakers, contactors and overloads, variable-speed drives</small>"]
    DB["Distribution boards and final circuits<br/><small>MCBs (6-63 A), RCBOs for socket circuits, 30 mA RCD protection</small>"]
    LOAD["Utilisation<br/><small>motors, lighting, socket outlets, HVAC</small>"]
    SUPPLY -->|415 V three-phase four-wire| MSB
    MSB -->|motor and process boards| MCC
    MSB -->|lighting, small power and UPS boards| DB
    MCC -->|motors and drives| LOAD
    DB -->|final loads| LOAD
```

**Key equipment:** main switchboard with ACB, motor control centre, distribution board, MCB and RCBO devices, surge protective devices.

**Performance:**
- LV supply voltage, three-phase: 400-415 V; TNB supply-voltage table; both 400/230 V and 415/240 V describe the same LV level. [source](https://www.tnb.com.my/)
- LV supply available up to (CT metered): 1000 kVA; TNB three-phase four-wire CT metered up to about 1,000 kVA; above that an 11 kV supply applies. [source](https://www.tnb.com.my/)
- LV steady-state voltage tolerance: -6-10 %; TNB voltage-fluctuation limits at 400/230 V under normal conditions. [source](https://www.tnb.com.my/)
- required RCD sensitivity for socket circuits: 30 mA; Malaysian practice for socket-outlet final circuits (30 mA RCD). [source](https://www.st.gov.my/)

**Missing inputs:**
- cost per board or per kVA of installed LV distribution (costs): Vendor and licensee sites do not publish installed prices. Where: Manufacturer price books or a Malaysian licensed-contractor benchmark. Next: Ask owner for a priced reference or a quote from a licensed contractor.

Sources: [1](https://www.tnb.com.my/). Last reviewed 2026-11-13.

## Medium-voltage distribution (11 kV and 33 kV)
<a id="ele-mv-distribution"></a>

Malaysia's MV distribution levels: TNB supplies 11 kV for roughly 1,000-5,000 kVA and 33 kV up to about 25,000 kVA (22 kV appears in parts of Johor and Perak). At site level an intake substation receives the supply and ring-main units feed substation transformers, often with redundant transformers and an N+1 scheme for critical process loads. MV installations carry the highest periodic-inspection frequency under the Electricity Regulations.

```mermaid
flowchart LR
    INTAKE["TNB 11 kV or 33 kV supply point<br/><small>ring main unit (RMU) or received section, TNB metering cubicle</small>"]
    PHASE["Main MV switchgear<br/><small>vacuum circuit breakers, busbar 630-2500 A, current transformers and protection relays</small>"]
    TF["Distribution transformers<br/><small>11 kV/415 V or 33 kV/415 V transformers (1000-2500 kVA)</small>"]
    FR["Feeder route<br/><small>MV cables or overhead lines</small>"]
    SUB["Site substations<br/><small>package substations with RMU-fed transformers</small>"]
    LV["Low-voltage distribution boards<br/><small>see the low-voltage distribution card</small>"]
    INTAKE -->|nominal 11 kV or 33 kV| PHASE
    PHASE -->|transformer feeders| TF
    PHASE -->|outgoing site feeders| FR
    TF -->|415 V to the LV boards| LV
    FR -->|remote substations| SUB
    SUB --> LV
```

**Key equipment:** ring main units, vacuum circuit breakers, distribution transformers, MV cables, protection relays.

**Performance:**
- 11 kV supply range for TNB customers: 1000-5000 kVA; TNB three-phase three-wire 11 kV for 1,000-5,000 kVA. [source](https://www.tnb.com.my/)
- 33 kV supply range for TNB customers: 5000-25000 kVA; TNB three-phase three-wire 33 kV for 5,000-25,000 kVA. [source](https://www.tnb.com.my/)
- MV steady-state voltage tolerance: -5-5 %; TNB limits at 6.6 kV, 11 kV, 22 kV and 33 kV. [source](https://www.tnb.com.my/)
- 33 kV fault level rating: 25 kA; TNB 33 kV short-circuit rating 25 kA for 3 s. [source](https://www.tnb.com.my/)
- 11 kV fault level rating: 20 kA; TNB 11 kV short-circuit rating 20 kA for 3 s. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per substation installed, ring versus radial, with a Malaysian contractor benchmark (costs): Vendor and licensee sites do not publish installed prices. Where: Malaysian electrical contractor tender benchmarks. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.tnb.com.my/). Last reviewed 2026-11-13.

## Motors and variable speed drives
<a id="ele-motors-drives"></a>

Three-phase induction motors remain the workhorse driver; synchronous machines serve large compressors and high-efficiency duties. Efficiency classes IE1 to IE5 are defined in IEC 60034-30-1 for line-operated motors. Variable frequency drives rectify the supply and synthesise an adjustable-voltage, adjustable-frequency output, giving soft starts, process speed control, energy savings on centrifugal loads (affinity laws: power roughly follows speed cubed) and regenerative braking on hoisting duties. Drives inject harmonics, so input filters or multi-pulse/active front ends are applied.

```mermaid
flowchart LR
    REC["Drive rectifier converts AC supply to DC bus<br/><small>rectifier, DC link</small>"]
    INV["Inverter synthesises variable-frequency output<br/><small>IGBT inverter, output filter</small>"]
    MOT["Motor converts electrical to mechanical power<br/><small>induction or synchronous motor</small>"]
    CTRL["Closed-loop control (V/f, flux vector) tracks torque and speed references<br/><small>drive controller, encoder</small>"]
    REC --> INV
    INV --> MOT
    MOT --> CTRL
```

**Key equipment:** induction motors, synchronous motors, variable frequency drives, soft starters, harmonic filters, motor protection relays.

**Performance:**
- LV motor supply voltage: 400-415 V; TNB LV supply voltage for compatible LV motors and drives. [source](https://www.tnb.com.my/)
- MV motor supply voltage: 11 kV; TNB 11 kV supply is the standard MV motor voltage in Malaysia. [source](https://www.tnb.com.my/)
- MV voltage tolerance the drive must ride through: -5-5 %; TNB steady-state limits at 11 kV and 33 kV. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per kW by drive size and voltage (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.energy.gov/eere/amo/motors), [2](https://www.iec.ch/standards), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## On-site gas turbine power generation
<a id="ele-gt-power-generation"></a>

Facilities generate their own power with gas turbine generator sets when the grid is weak, absent or considered unreliable, or when waste heat from exhaust can drive steam for process use (cogeneration). Industrial and aeroderivative turbines from about 5 MW to well above 100 MW are installed per train; multiple units run with a power management system, spinning reserve and load-shed logic. Offshore and remote platforms historically ran at 4.16 kV or 11 kV with closed-bus transfer between boards.

```mermaid
flowchart LR
    CMP["Compressor raises combustion air<br/><small>axial compressor</small>"]
    BUR["Fuel burns in combustors; turbine expands hot gas<br/><small>combustors, turbine</small>"]
    GEN["Generator converts shaft power to electricity<br/><small>synchronous generator</small>"]
    EXH["Exhaust heat raised to steam where cogeneration applies<br/><small>HRSG</small>"]
    DIS["PMS dispatches generation against demand, reserve and shed priority<br/><small>power management system</small>"]
    CMP --> BUR
    BUR --> GEN
    GEN --> EXH
    EXH --> DIS
```

**Key equipment:** gas turbine generator sets, HRSG, generators, power management system, fuel gas conditioning.

**Performance:**
- generator connection voltage to TNB grid: 11-275 kV; embedded generation connects at 11 kV through to 275 kV by size. [source](https://www.tnb.com.my/)
- 132/275 kV supply threshold for large connections: 25000 kVA; TNB supplies 132 kV and 275 kV above about 25,000 kVA. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per MW installed, open cycle and combined cycle (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.siemens-energy.com/global/en/home.html), [2](https://www.mhi.com/), [3](https://www.eia.gov/electricity/), [4](https://www.tnb.com.my/), [5](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Overhead transmission lines (132-500 kV)
<a id="ele-transmission-lines"></a>

The transmission backbone: TNB operates 132 kV, 275 kV and 500 kV lines. Insulator creepage and clearance are set by the phase voltage and local pollution; the tower type (lattice steel or monopole) follows terrain and corridor constraints; ACSR or AAAC conductors are sized by ampacity and sag; earth wires or line surge arresters protect against lightning, which matters heavily in Malaysia's thunderstorm climate. Live-line working and patrols carry the lifecycle.

```mermaid
flowchart LR
    FEAS["Route selection and clearance study<br/><small>survey, environmental assessment, PLS-CADD modelling</small>"]
    TOWER["Foundation and tower erection<br/><small>lattice steel towers or monopoles, insulators (glass, porcelain, composite)</small>"]
    STRING["Conductor stringing<br/><small>ACSR or AAAC conductors, OPGW earth wire, tension stringing rigs</small>"]
    PROT["Protection and monitoring<br/><small>distance protection and line differential, line fault locators, sag and meteorology monitoring</small>"]
    MAINT["Lifecycle maintenance<br/><small>patrols and thermography, live-wire working, vegetation management</small>"]
    FEAS --> TOWER
    TOWER --> STRING
    STRING -->|protection and control| PROT
    PROT -->|maintenance records| MAINT
```

**Key equipment:** lattice towers, ACSR or AAAC conductor, insulators, OPGW, distance protection relays.

**Performance:**
- transmission voltage levels in Peninsular Malaysia: 132-500 kV; TNB transmission at 132 kV, 275 kV and 500 kV. [source](https://www.tnb.com.my/)
- 500 kV fault level rating: 50 kA; TNB 500 kV short-circuit rating 50 kA for 1 s. [source](https://www.tnb.com.my/)
- 132 kV fault level rating: 31.5-40 kA; TNB 132 kV 31.5 kA for 3 s, 40 kA near power stations. [source](https://www.tnb.com.my/)
- 500 kV steady-state voltage tolerance: -5-5 %; TNB 500 kV voltage limits. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per kilometre by voltage and terrain (costs): Network operators do not publish line costs. Where: Energy Commission or GSO tariff filings. Next: Ask owner for a priced reference.

Sources: [1](https://www.tnb.com.my/). Last reviewed 2026-11-13.

## Power and control cable systems
<a id="ele-cable-systems"></a>

Cable systems move power and signals between equipment and boards. Construction is chosen per duty: XLPE or EPR insulation for power, fire-resistant (circuit integrity) cables for safety circuits that must keep working during a fire, armoured and lead-sheathed designs for direct burial and submarine routes, and segregated tray/ladder routing with derating for bunching, ambient temperature and harmonic heating. Standards such as IEC 60502 (1–30 kV) and IEC 60332 (fire behaviour) govern selection and testing.

```mermaid
flowchart LR
    SEL["Cable type, size and rating selected for load, voltage drop and fault level<br/><small>cable sizing studies</small>"]
    ROU["Routes engineered with segregation by voltage class and fire zoning<br/><small>cable trays, ladder racks</small>"]
    INS["Cable installed, glands and terminations made<br/><small>glands, terminations, joints</small>"]
    TST["Insulation resistance and withstand tests prove the circuit<br/><small>test sets</small>"]
    SEL --> ROU
    ROU --> INS
    INS --> TST
```

**Key equipment:** XLPE power cables, fire-resistant cables, armoured and submarine cables, cable trays, glands and terminations.

**Performance:**
- MV cable working voltage: 11-33 kV; TNB MV distribution voltages for cable rating. [source](https://www.tnb.com.my/)
- LV cable working voltage: 400-415 V; TNB LV supply for LV power and control cables. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per metre by voltage class and conductor size (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.prysmian.com/), [2](https://www.nexans.com/), [3](https://www.iec.ch/standards), [4](https://www.tnb.com.my/), [5](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Power and distribution transformers
<a id="ele-transformers"></a>

Transformers couple windings through a magnetic core to change voltage levels at essentially constant power. Oil-filled units (mineral oil, ester or gas-insulated) dominate power ratings, with ONAN/ONAF/OFAF/ODAF cooling stages; dry-type cast-resin units suit fire-sensitive or confined locations. An on-load tap changer (OLTC) regulates the output voltage under load. Losses, sound level and thermal behaviour are standardised in the IEC 60076 series.

```mermaid
flowchart LR
    PRI["Primary winding energised, core flux established<br/><small>core, windings</small>"]
    SEC["Secondary winding delivers transformed voltage<br/><small>windings, bushings</small>"]
    TAP["Tap changer regulates turns ratio, on-load or off-circuit<br/><small>OLTC, DETC</small>"]
    COOL["Cooling system removes load and no-load losses<br/><small>radiators, fans, oil pumps</small>"]
    PRO["Gas, pressure and temperature devices protect the unit<br/><small>Buchholz relay, winding temperature indicators, pressure relief</small>"]
    PRI --> SEC
    SEC --> TAP
    TAP --> COOL
    COOL --> PRO
```

**Key equipment:** core, windings, on-load tap changer, bushings, cooling system, Buchholz relay.

**Performance:**
- 800 kV UHVDC power transformers delivered: 20 units (more than); Hitachi Energy states its power transformer fleet includes more than 20 units of 800 kV UHVDC and more than 500 units in the 735-765 kV AC class. [source](https://www.hitachienergy.com/products-and-solutions/transformers)
- 735-765 kV AC power transformers delivered: 500 units (more than); same statement as above. [source](https://www.hitachienergy.com/products-and-solutions/transformers)

**Missing inputs:**
- cost per MVA installed, by transformer class and voltage (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.hitachienergy.com/products-and-solutions/transformers), [2](https://www.iec.ch/standards), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Power management and electrical SCADA
<a id="ele-power-management-systems"></a>

A power management system supervises generation, tie-lines and major loads: it schedules and dispatches running generator sets, synchronises and parallels them, maintains frequency and voltage, arms staged load shedding for generator or tie loss, and manages islanding and re-synchronisation with the grid. PMS logic sits on electrical SCADA above the protection relays and complements them — protection clears faults in milliseconds while the PMS re-balances the network in seconds.

```mermaid
flowchart LR
    MEAS["Network measured from IEDs and meters over IEC 61850/Modbus<br/><small>IEDs, gateway</small>"]
    DSP["Generation dispatched and synchronised against demand and reserve targets<br/><small>PMS controller, synchronisers</small>"]
    SHD["Staged load shedding armed and executed on disturbance<br/><small>load-shed relays</small>"]
    ISL["Islanding, closed-bus transfer and re-sync managed<br/><small>transfer schemes</small>"]
    MEAS --> DSP
    DSP --> SHD
    SHD --> ISL
```

**Key equipment:** PMS controllers, electrical SCADA, protection relays and IEDs, synchronisers, load-shed schemes.

**Performance:**
- voltage limits the SCADA must alarm on at 132 kV: -5-10 %; TNB 132 kV and 275 kV voltage limits. [source](https://www.tnb.com.my/)
- 500 kV voltage limit monitored by the system: -5-5 %; TNB 500 kV voltage limit. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per substation of SCADA and automation (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.gevernova.com/), [2](https://www.iec.ch/standards), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Power system protection and relaying
<a id="ele-protection-relaying"></a>

Protection relays continuously compare measured current, voltage, frequency, phase and differential quantities against settings and command circuit breakers to isolate faults before equipment or people are harmed. Modern numerical relays combine many protection functions (ANSI 50/51 overcurrent, 87 differential, 27/59 voltage, 81 frequency, 46 negative sequence) with recording, metering and IEC 61850 communication in one device. Selectivity is achieved through current grading, time grading or zone-based differential schemes, with breaker-failure back-up tripping the surrounding breakers when the primary trip fails.

```mermaid
flowchart LR
    SEN["Current and voltage transformers scale primary quantities to relay inputs<br/><small>CTs, VTs</small>"]
    MEA["Relays compute protection elements and compare with settings<br/><small>numerical protection relays</small>"]
    DIS["Grading and zone logic discriminate in-zone faults from load<br/><small>protection schemes</small>"]
    TRP["Trip output opens the correct breaker(s); breaker-failure back-up trips wider if needed<br/><small>trip circuits, breaker-fail relays</small>"]
    REC["Event and disturbance records support post-fault analysis<br/><small>event recorders</small>"]
    SEN --> MEA
    MEA --> DIS
    DIS --> TRP
    TRP --> REC
```

**Key equipment:** numerical protection relays, current transformers, voltage transformers, trip coils, breaker failure protection, disturbance recorders.

**Performance:**
- 11 kV clearing requirement implied by fault rating: 20 kA; protection must clear the 20 kA, 3 s 11 kV fault duty. [source](https://www.tnb.com.my/)
- 500 kV fault ratings protection must handle: 50 kA; 50 kA for 1 s at 500 kV. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per protection panel or per feeder (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.selinc.com/products/), [2](https://www.hse.gov.uk/electricity/), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## Subsea power and umbilical systems
<a id="ele-subsea-umbilicals-power"></a>

Subsea electrical systems take power from a platform or shore through a power umbilical — cable plus steel tubes for hydraulic signals — to subsea distribution units, transformers, variable speed drives and motors on the seabed. Moves toward higher voltage and longer step-outs have already delivered megawatt-class subsea compression, where the whole drive train sits on the seabed without an topsides compressor. Reliability engineering, connector technology and dynamic cable design for floating hosts dominate the design space.

```mermaid
flowchart LR
    SHP["Topside or onshore supply conditioned and stepped for export<br/><small>VSD, transformer</small>"]
    UMB["Power umbilical and static/dynamic cable delivered to the seabed<br/><small>umbilical, riser cable</small>"]
    SDU["Subsea distribution and step-down feed seabed loads<br/><small>SDU, subsea transformer</small>"]
    LD["Motors, drives and valve actuators run on the seabed<br/><small>subsea motors, actuators</small>"]
    SHP --> UMB
    UMB --> SDU
    SDU --> LD
```

**Key equipment:** power umbilicals, subsea transformers, subsea distribution units, subsea drives, wet-mate connectors.

**Missing inputs:**
- cost per kilometre of umbilical (costs): Vendor and licensee sites do not publish installed prices. Where: Ask the owner for a Malaysian contractor benchmark. Next: Ask owner for a priced reference or a contractor quote.

Sources: [1](https://www.nexans.com/), [2](https://www.siemens-energy.com/global/en/home.html), [3](https://www.tnb.com.my/), [4](https://www.gso.org.my/). Last reviewed 2026-11-13.

## UHV and HV substations (275-500 kV)
<a id="ele-uhv-substations"></a>

The 275 kV and 500 kV bulk nodes of the Malaysian grid. Air-insulated switchyard designs (dead-tank breakers, disconnectors, CTs and VTs, surge arresters, lattice busbars) dominate on land, with gas-insulated switchgear for space-constrained urban sites. Transformer banks step 500/275 kV and 275/132 kV; shunt reactors and capacitor banks or SVC/STATCOM manage voltage on long lines; IEC 61850 substation automation runs protection and monitoring.

```mermaid
flowchart LR
    BAY["Incoming line bays<br/><small>line disconnectors, surge arresters, capacitor voltage transformers</small>"]
    BUS["Busbars and transfer schemes (AIS or GIS)<br/><small>double busbar, bus coupler and transfer breakers</small>"]
    TRF["Power transformer banks<br/><small>500/275 kV and 275/132 kV banks, on-load tap changers, Buchholz and protection devices</small>"]
    COMP["Reactive compensation<br/><small>shunt reactors, capacitor banks, SVC or STATCOM</small>"]
    PROT["Substation automation and protection<br/><small>IEC 61850 IEDs, SCADA gateway, redundant protection schemes</small>"]
    BAY -->|busbar| BUS
    BUS -->|transformer bays| TRF
    BUS -->|reactive compensation| COMP
    TRF -->|protection and control| PROT
    COMP --> PROT
```

**Key equipment:** power transformers, dead-tank and GIS circuit breakers, disconnectors and earthing switches, current and voltage transformers, surge arresters, protection IEDs.

**Performance:**
- 275 kV fault level rating: 40-50 kA; TNB 275 kV 40 kA for 3 s, 50 kA near power stations. [source](https://www.tnb.com.my/)
- 500 kV fault level rating: 50 kA; TNB 500 kV 50 kA for 1 s. [source](https://www.tnb.com.my/)

**Missing inputs:**
- cost per bay or per MVA of substation capacity (costs): Network operators do not publish substation costs. Where: GSO or Energy Commission regulatory filings. Next: Ask owner for a priced reference.

Sources: [1](https://www.tnb.com.my/). Last reviewed 2026-11-13.
