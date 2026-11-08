---
source_id: "wikipedia"
title: "Grid forming_inverter"
url: "https://en.wikipedia.org/wiki/Grid-forming_inverter"
retrieved_at: "2026-11-08T15:34:59+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "0d2497cd65269b65ae56bffdde3d7e5279e7b129b0a752328491aeb4c20e7a33"
collected: "manual"
summary: "Wikipedia overview of grid-forming inverters: inverter controls that establish voltage and frequency rather than following the grid, relevant to high-renewables and island power systems."
---

# Grid forming_inverter

# Inverter-based resource

An **inverter-based resource** (**IBR**) is a source of electricity that is asynchronously connected to the electrical grid via an electronic power converter ("inverter"). The devices in this category, also known as **converter interfaced generation** (**CIG**) and **power electronic interface** source, include the variable renewable energy generators (wind, solar) and energy storages such as battery, super capacitors, etc..<sup>\[1\]</sup><sup>\[2\]</sup> These devices lack the intrinsic behaviors (like the inertial response of a synchronous generator) and their features are almost entirely defined by the control algorithms, presenting specific challenges to system stability as their penetration increases,<sup>\[1\]</sup> for example, a single software fault can affect all devices of a certain type in a contingency (cf. section on Blue Cut fire below). IBRs are sometimes called *non-synchronous generators*.<sup>\[3\]</sup> The design of inverters for the IBR generally follows the IEEE 1547 and NERC PRC-024-2 standards.<sup>\[4\]</sup>

The term **unconventional sources** includes IBRs as well as other generators that behave differently than synchronous generators.<sup>\[5\]</sup>

## Grid-following

\[edit\]
A **grid-following** (**GFL**) device is synchronized to the local grid voltage and injects an electric current vector aligned with the voltage (in other words, behaves like a current source<sup>\[6\]</sup>). The GFL inverters are built into an overwhelming majority of installed IBR devices.<sup>\[1\]</sup> Due to their following nature, the GFL device will shut down if a large voltage/frequency disturbance is observed.<sup>\[7\]</sup>  The GFL devices cannot contribute to the grid strength, dampen active power oscillations, or provide inertia.<sup>\[8\]</sup>

## Grid-forming

\[edit\]
A **grid-forming** (**GFM**) device partially mimics certain attributes of a synchronous generator: its voltage is controlled by a locally controlled oscillator that slows down when more energy is withdrawn from the device.<sup>\[9\]</sup> Unlike a conventional generator, the GFM device has no overcurrent capacity and thus will react very differently in the short-circuit situation.<sup>\[1\]</sup> Adding the GFM capability to a GFL device is not expensive in terms of components, but affects the revenues: in order to support the grid stability by providing extra power when needed, the power semiconductors need to be oversized and energy storage added. GFM has higher standby consumption than GFL.<sup>\[10\]</sup> Modeling demonstrates, however, that it is possible to run a power system that almost entirely is based on the GFL devices.<sup>\[11\]</sup> A combination of GFM battery storage power station and synchronous condensers ("SuperFACTS") is being researched.<sup>\[12\]</sup>

European Network of Transmission System Operators for Electricity (ENTSO-E) groups the GFM devices into three classes from 1 to 3, with Class 1 being at the lowest level of contribution to the grid stability (the original classification had the numbers in reverse, with class 1 being the highest). Class 2 is further subdivided in to 2A, 2B, 2C, with 2A being the most basic of the three:<sup>\[13\]</sup>

- Class 1 devices primarily deal with their own survival (full frequency and voltage operating ranges) and have minimal contributions to the grid, including basic reactive power management to maintain the unity power factor and limited frequency sensitive mode (LFSM-O).
- Class 2 devices provide additional capabilities:
  - 2A supports the fault ride-through and voltage control for the steady state;
  - 2B adds the dynamic voltage control, frequency sensitive mode (FSM) as well as the LFSM-U;
  - 2C also provides voltage control at zero active power, oscillations damping, and fast fault current injection (FFCI) for periods B and C (the AC periods immediately following the "A" one with the fault)
- Class 3 is capable of fully autonomous operation with no support from the grid. It creates system voltage, capable of handling fault level in the period A, contributes to the total system inertia (TSI) of the grid, can handle low frequency demand disconnection (LFDD), provides a sink for harmonics and interharmonics of the system voltage, and a sink for the voltage unbalance.

## Features

\[edit\]
Compliance with IEEE 1547 standard makes the IBR to support safety features:<sup>\[14\]</sup>

- if the sensed line voltage significantly deviates from the nominal (usually outside the limits of 0.9 to 1.1 pu), the IBR shall disconnect from the after a delay (*ride-through time*), the delay is shorter if the voltage deviation is larger. Once the inverter is off, it will stay disconnected for a significant time (minutes);
- if the voltage magnitude is unexpected, the inverter shall enter the *momentary cessation* state: while still connected, it will not inject any power into the grid. This state has a short duration (less than a second).

Once an IBR ceases to provide power, it can come back only gradually, ramping its output from zero to full power.<sup>\[15\]</sup>

The electronic nature of IBRs limits their overload capability: the thermal stress causes their components to even temporarily be able to function at no more than 1-2 times the nameplate capacity, while the synchronous machines can briefly tolerate an overload as high as 5-6 times their rated power.<sup>\[16\]</sup>

A typical failure of a conventional synchronous generator (like a loss of prime mover) is slow (seconds), while the IBR has to disconnect quickly due to low margin for overload.<sup>\[17\]</sup>

North American Electric Reliability Corporation (NERC) notes that IBR, like conventional generators, can provide essential reliability services, and summarizes the differences as follows:<sup>\[18\]</sup>

| Differences between IBRs and synchronous generators |  | 
|---|---|
| IBR | Synchronous generator | 
|---|---|
| Behavior determined by power converter and control software | Behaviour driven mostly by the physical properties of the machine | 
| Non-existent to small inertia | Large inertia of the rotor | 
| Low fault current | High fault current | 
| Based on sensitive electronics | Design can withstand extreme conditions | 
| Fast ramping | Ramping limited by mechanical limits | 
| Fast frequency control | Inertial response by design | 
| Dispatchability limited be environmental conditions | Full dispatchability | 
| Very little plant equipment outside the generator | Extensive auxiliary equipment adding to the risk of tripping | 

### Protection functions

\[edit\]
The IBR devices come with many protection functions built into the inverters. Experience of the late 2010s and early 2020s had shown that some of these protections are unnecessary, as they were designed with an expectation of a strong grid with little IBR penetration. NERC 2018 guidelines suggested removing some of these checks in order to avoid unnecessary disconnections ("trips") of the IBRs, and newer devices might not have them. The remaining checks are essential for the self-protection of the inverters that, compared to a synchronous generator, have relatively little tolerance for overvoltage and overcurrent.<sup>\[17\]</sup> The typical protections include:<sup>\[19\]</sup>

- **instant AC overvoltage**. A high-amplitude voltage surge can damage sensitive electronics of the inverter. The voltage sensor measures the waveform with little filtering. In some cases, gating off the inverter during a disturbance can exacerbate the voltage problem (cf. subcycle overvoltage);
- **instant AC overcurrent** prevents the inverter, with little tolerance for overload, from feeding the current into a fault. A speedy response is also essential, so very little filtering is applied to the current sensor data;
- **DC overvoltage** indicates a problem on the DC bus of the inverter (and a fault internal to the inverter electronics);
- **DC unbalance** for multi-level inverter designs (like a 3-level neutral point clamped, NPC) have multiple DC buses. A voltage imbalance between these buses, that can occur due to waveform distortion caused by an external transient fault, requires a trip to clear;
- **voltage and frequency ride-through** disconnect the inverter when a sever waveform distortion is encountered. After the Blu Cut fire incident, the NERC guidelines require the data to be extensively filtered to avoid tripping the device during a short-duration external fault;
- **phase jump protection** detects a change in the phase difference between the voltage and current waveforms that might indicate accidental islanding;
- **loss of synchronism**. If the "PLL angle" (an IBR equivalent of the rotor angle) changes rapidly, it might indicate malfunctioning of the device, and requires a trip to avoid future damage. However, with weaker grids and high penetration of IBRs, a false alarm is possible.

Once tripped, the IBRs will restart based on a timer or through manual intervention. A typical timer setting is in the seconds to minutes range (the IEEE-1547 default is 300 seconds).<sup>\[20\]</sup>

## Vulnerabilities

\[edit\]
New challenges to the system stability came with the increased penetration of IBRs. Incidences of disconnections during contingency events where the fault ride-through was expected, and poor damping of subsynchronous oscillations in weak grids were reported.<sup>\[1\]</sup>

The widespread mass disconnections of IBRs in the event of a fault pose a "notable" reliability risk to the grids.<sup>\[21\]</sup> As of mid-2020s, IBRs, including battery energy storage systems (BESS), demonstrated a tendency to trip or significantly reduce output due to normally non-consequential faults that the protection systems routinely clear.<sup>\[22\]</sup> This risk is compounded by the retirement of synchronous machines, which increases the grid's reliance on IBRs for essential reliability services and ride-through performance.<sup>\[23\]</sup> Western Interconnection in the US, with its high penetrations of solar PV and wind resources, exhibited 4 events with loss of more than 500MW in the spring-summer of 2024.<sup>\[24\]</sup> Analysis of these disturbances indicated that a significant portion of inverter settings were not optimized for the equipment's maximum capability, resulting in underused ride-through capacity.<sup>\[23\]</sup> Firmware updates to control equipment were observed to inadvertently revert algorithm settings to default configurations, undoing previous mitigations and leaving facilities vulnerable to tripping.<sup>\[25\]</sup>

One of the most studied major power contingencies that involved IBRs is the Blue Cut Fire of 2016 in Southern California, with a temporary loss of more than a gigawatt of photovoltaic power in a very short time.<sup>\[15\]</sup>

### Blue Cut fire

\[edit\]
The Blue Cut fire in the Cajon Pass on August 16, 2016, has affected multiple high-voltage (500 kV and 287 kV) power transmission lines passing through the canyon. Throughout the day thirteen 500 kV line faults and two 287 kV faults were recorded.<sup>\[26\]</sup> The faults themselves were transitory and self-cleared in a short time (2–3.5 cycles, less than 60 milliseconds), but the unexpected features of the algorithms in the photovoltaic inverter software triggered multiple massive losses of power, with the largest one of almost 1,200 megawatts<sup>\[27\]</sup> at 11:45:16 AM, persisting for multiple minutes.<sup>\[28\]</sup>

The analysis performed by the North American Electric Reliability Corporation (NERC) had shown that:

1. 700 MW of loss were caused by the poorly designed frequency estimation algorithm. The line faults had distorted the AC waveform and fooled the software into a wrong estimate of the grid frequency dropping below 57 Hz, a threshold where an emergency disconnect shall be initiated. However, the actual frequency during the event had never dropped below 59.867 Hz,<sup>\[29\]</sup> well above the low limit of the normal frequency range (59.5 Hz for the Western Interconnection).
2. Additional 450 MW were lost when low line voltage caused the inverters to immediately cease to inject current, with gradual return to operative state within 2 minutes. At least one manufacturer had indicated that injecting the current when the voltage level is below 0.9 pu would involve a major redesign.<sup>\[30\]</sup>

As a result of the incident, NERC had issued multiple recommendations, involving the changes in inverter design and amendments to the standards.<sup>\[4\]</sup>

## References

\[edit\]
1. 1 2 3 4 5 Gu & Green 2022, p. 1.
2. ↑ ENTSO-E 2020, p. 1.
3. ↑ Khan & Minai 2023, p. 1.
4. 1 2 NERC 2017, p. 10.
5. ↑ Kasztenny 2022, p. 1.
6. ↑ Khan & Minai 2023, pp. 1–2.
7. ↑ Khan & Minai 2023, p. 4.
8. ↑ AEMO 2021, p. 15.
9. ↑ Song, Guanhong; Cao, Bo; Chang, Liuchen (March 2022). "Review of Grid-forming Inverters in Support of Power System Operation". *Chinese Journal of Electrical Engineering*. **8** (1): 1–15. doi:10.23919/CJEE.2022.000001. ISSN 2836-4619.
10. ↑ Heynes, George (2 September 2025). "Grid-forming battery storage: 'Standby consumption will be higher' says Australia's AGL". *Energy-Storage.News*.
11. ↑ Gu & Green 2022, p. 2.
12. ↑ Gevorgian, V.; Shah, S.; Yan, W. (2021). "Hybridizing synchronous condensers with grid forming batteries for PV integration – a solution to enhance grid reliability and resiliency". *11th Solar & Storage Power System Integration Workshop (SIW 2021)*. IET Conference Proceedings. Vol. 2021. pp. 85–108. doi:10.1049/icp.2021.2488. ISBN 978-1-83953-680-9.
13. ↑ ENTSO-E 2020, pp. 20–21.
14. ↑ Popiel 2020, pp. 4–5.
15. 1 2 Popiel 2020, p. 5.
16. ↑ AEMO 2021, p. 16.
17. 1 2 Pattabiraman & Inzunza 2024, p. 1.
18. ↑ NERC 2023, p. 4.
19. ↑ Pattabiraman & Inzunza 2024, pp. 1–2.
20. ↑ Pattabiraman & Inzunza 2024, p. 2.
21. ↑ WECC 2025, p. 2.
22. ↑ WECC 2025, pp. 2, 4.
23. 1 2 WECC 2025, p. 11.
24. ↑ WECC 2025, pp. 2, 5.
25. ↑ WECC 2025, p. 8.
26. ↑ NERC 2017, p. v.
27. ↑ NERC 2017, p. 2.
28. ↑ NERC 2017, p. 5.
29. ↑ NERC 2017, p. 8.
30. ↑ NERC 2017, p. 9.

## Sources

\[edit\]
- AEMO (August 2021). *Application of Advanced Grid-scale Inverters in the NEM* (PDF). Australian Energy Market Operator.
- ENTSO-E (2020). *High Penetration of Power Electronic Interfaced Power Sources and the Potential Contribution of Grid Forming Converters* (PDF). ENTSO-E Technical Group on High Penetration of Power Electronic Interfaced Power Sources.
- Gu, Yunjie; Green, Timothy C. (2022). "Power System Stability With a High Penetration of Inverter-Based Resources" (PDF). *Proceedings of the IEEE*. **111** (7): 832–853. doi:10.1109/JPROC.2022.3179826. eISSN 1558-2256. ISSN 0018-9219.
- Kasztenny, Bogdan (2022). *Line Distance Protection Near Unconventional Energy Sources*. 16th International Conference on Developments in Power System Protection. Newcastle Gateshead, United Kingdom.
- Nabil Mohammed; Hassan Haes Alhelou; Behrooz Bahrani, eds. (28 February 2023). *Grid-Forming Power Inverters: Control and Applications*. CRC Press. ISBN 978-1-00-083929-6.
  - Khan, Akhlaque Ahmad; Minai, Ahmad Faiz (13 January 2023). "Introduction to Grid-Forming Inverters". *Grid-Forming Power Inverters*. CRC Press. pp. 1–14. doi:10.1201/9781003302520-1. ISBN 978-1-003-30252-0.
- NERC (June 2017). *1,200 MW Fault Induced Solar Photovoltaic Resource Interruption Disturbance Report* (PDF). North American Electric Reliability Corporation.
- NERC (June 2023). "Introductory Guide to Inverter-Based Resources on the Bulk Power System" (PDF). Retrieved 2025-05-11.
- Pattabiraman, Dinesh; Inzunza, Ruben (2024-05-06). "Mitigating IBR Trips During Grid Disturbances Using Low Risk Control Approaches" (PDF). *2024 IEEE/PES Transmission and Distribution Conference and Exposition (T&D)*. IEEE. pp. 1–5. doi:10.1109/TD47997.2024.10555915. ISBN 979-8-3503-1637-7. Retrieved 2025-05-11.
- Popiel, Caroline Rose (2020). *The Incidence of Inverter Incidents: Understanding and Quantifying Contributions to Risk in Systems with Large Amounts of Inverter-Based Resources* (MSc). The University of Vermont.
- WECC (October 2025). Inverter-Based Resource Disturbances in the Western Interconnection: CAISO, NERC, and WECC Staff Report (PDF) (Report). North American Electric Reliability Corporation.
