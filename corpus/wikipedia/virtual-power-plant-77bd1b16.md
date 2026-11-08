---
source_id: "wikipedia"
title: "Virtual_power_plant"
url: "https://en.wikipedia.org/wiki/Virtual_power_plant"
retrieved_at: "2026-11-08T15:35:02+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "77bd1b1673c7bf1e5464543a8d6e12aeeec0480ca237eec4445735c49d09ada5"
collected: "manual"
summary: "Wikipedia overview of virtual power plants: aggregating distributed generation, storage and flexible demand into one dispatchable resource for grid operation."
---

# Virtual_power_plant

# Virtual power plant

| Virtual power plant |  | 
|---|---|
| Process type | Network | 
|---|---|
| Industrial sector(s) | Electrical power | 
| Inventor | Shimon Awerbuch | 

A **virtual power plant** (**VPP**) is a system for aggregating distributed energy resources (DERs) to function as a single power plant.<sup>\[1\]</sup> Operators coordinate these resources to balance supply and demand, provide grid services, and participate in energy markets.<sup>\[2\]</sup><sup>\[3\]</sup><sup>\[4\]</sup> A VPP typically sells its output to an electric utility.<sup>\[5\]</sup><sup>\[2\]</sup><sup>\[3\]</sup><sup>\[6\]</sup><sup>\[4\]</sup><sup>\[7\]</sup> VPPs allow energy resources that are individually too small to be of interest to a utility to aggregate and market their power.<sup>\[4\]</sup>

VPPs typically access dispatchable and non-dispatchable resources, including microCHPs, natural gas-fired reciprocating engines, wind power plants, photovoltaics (PV), run-of-river hydroelectricity, biomass, backup generators, battery energy storage systems (BESS) such as home or vehicle batteries. VPPs can manage demand as well as supply; e.g., heat pumps and other devices can be turned on or off based on available energy supply.<sup>\[8\]</sup>

Heterogeneity and numbers reduce dependence on any single resource, improving system stability.<sup>\[9\]</sup>

Vehicle-to-grid allows grid-connected electric vehicles to participate.

Storage-based VPPs ramp faster than thermal generators, e.g., helping grids with high ramp needs avoid the duck curve.

A management system securely controls operations, billing, and payments to power suppliers and consumers.<sup>\[10\]</sup>

VPPs provide peak shaving by delivering power during high demand, avoiding expensive peaker plants (saving 40–60%).<sup>\[11\]</sup><sup>\[12\]</sup> They offer load following and ancillary services such as frequency regulation and operating reserves, responding in seconds to minutes.

VPPs can trade energy in wholesale markets, acting as dispatchable plants. Strategies hedge risks in markets:

- Info-gap decision theory (IGDT)<sup>\[2\]</sup>
- Robust optimization (RO)<sup>\[3\]</sup>
- Conditional value at risk (CVaR)<sup>\[6\]</sup>
- First-order Stochastic Dominance (FSD)<sup>\[4\]</sup>
- Second-order Stochastic Dominance (SSD)<sup>\[7\]</sup>

## History

\[edit\]
Shimon Awerbuch proposed the VPP concept in 1997.<sup>\[13\]</sup> Early work remained theoretical due to technology and regulatory limits. Papers in the early 2000s examined renewable aggregation. Challenges included communication costs and risks.

RWE launched the first VPP in 2008, aggregating nine hydroelectric plants for 8.6 MW. The University of Kassel piloted one linking solar, wind, biogas, and hydroelectricity for load following. Kraftwerke started in 2011, expanding across seven countries, aggregating biogas, solar, and wind.<sup>\[13\]</sup>

In 2011, Elektro Ljubljana presented a virtual power plant in Amsterdam with partners including CyberGrid. The project was undergoing trials in Slovenia and was described by *Naš stik* as the first VPP in Southeastern Europe.<sup>\[14\]</sup> According to the FutureFlow project's final report, CyberGrid introduced its cyberNOC product in 2013 with functionality supporting tertiary-reserve (mFRR) processes.<sup>\[15\]</sup>

In the United States, VPPs built on demand response programs. The 2009 American Recovery and Reinvestment Act supported smart grids. Federal Energy Regulatory Commission Order 745 (2011) treated demand reductions as generation in wholesale markets. Order 2222 (2020) enabled direct DER bidding.<sup>\[13\]</sup>

AGL Energy started a 5 MW VPP in Adelaide in 2016 with batteries and PV for 1,000 homes. Tesla opened a VPP in South Australia in 2018, reaching 50,000 homes by 2022; AGL acquired the program in 2025, reaching 25 MW solar and 37 MW storage.<sup>\[16\]</sup>

UK Power Networks and Powervault launched London's first VPP in 2018 (0.32 MWh); Tesla partnered with Octopus Energy there in 2020,<sup>\[13\]</sup> installing BESS at 40+ homes across Barnet, with capacity of 0.32 MWh,<sup>\[17\]</sup> expanding it in 2020.<sup>\[18\]</sup> In 2019, SMS plc launched a VPP following the acquisition of Irish firm, Solo Energy.<sup>\[19\]</sup> In 2020, Tesla launched its Tesla Energy Plan in the UK in partnership with Octopus Energy. Participant homes are powered with renewable energy either from solar panels or from Octopus Energy.<sup>\[20\]</sup>

By 2023, U.S. capacity reached 30–60 GW (4–8% of peak demand). Tesla operated VPPs in Texas and California.

In 2024, Enpal and Entrix (via Flexa) planned Europe's largest VPP, targeting 1 GW by 2026 with solar, batteries, and EVs; launch occurred later that year.<sup>\[21\]</sup>

Virginia mandated a Dominion Energy VPP pilot (up to 450 MW) in 2025; the utility proposed it by December.<sup>\[22\]</sup> Vermont VPPs saved $3 million during 2025 heat waves.<sup>\[11\]</sup> North American capacity reached 37.5 GW in 2025.<sup>\[23\]</sup>

## Distributed energy resources

\[edit\]
VPPs typically aggregate large numbers of distributed energy resources (DER). Resources can be dispatchable or non-dispatchable, controllable or flexible load (CL or FL). Resources can include micro-CHPs, natural gas-fired reciprocating engines, wind power (WPP), photovoltaics (PV), run-of-river hydroelectricity, small hydro, biomass, backup generators, and BESS, as well as devices whose consumption is adjustable (such as water heaters and appliances). The numbers and heterogeneity mean that system output is not dependent on any single resource, offering the potential for stable output even if the output of any single resource is not.

Vehicle-to-grid (V2G) technology allows grid-connected EVs to participate in VPPs. The VPP controls the rate at which each vehicle charges/discharges (accepts/delivers power).

The same principle applies to consuming systems, such as heat pumps or air conditioners that can lower their power demands to reduce demand.<sup>\[24\]</sup>

VPPs based on storage can ramp at higher rates than thermal generators (such as fossil fuel plants), which is especially valuable in grids that experience a duck curve and must satisfy high ramping requirements in the morning and evening.

VPPs can be as dependable as conventional plants, while costing 40–60 percent less. One study forecasted that decentralized generation would comprise 500,000 megawatts of capacity compared to centralized generation of 280,000 megawatts.<sup>\[12\]</sup>

## Operation

\[edit\]
Power delivery is controlled by a management system. The distributed nature of VPPs requires software to respond appropriately and securely to power requests, utility billing, payments to resource owners, etc.<sup>\[25\]</sup><sup>\[26\]</sup>

## Services

\[edit\]
Typically, the VPP provides power (only) when requested by the utility.

### Peak shaving

\[edit\]
With the appropriate resources, a VPP can deliver incremental power on short notice, helping utilities to manage peak loads that would otherwise require purchasing expensive power from a peaker plant (typically powered by natural gas).

### Load following

\[edit\]
Given sufficient scale, a VPP can operate as a load-following generator, supplying output dynamically as demand changes throughout the day/night cycle.

### Ancillary services

\[edit\]
Virtual power plants can provide ancillary services that help maintain grid stability such as frequency regulation and providing operating reserve. These services are primarily used to maintain the instantaneous balance of electrical supply and demand. These services must respond to signals to increase or decrease load on the order of seconds to minutes.

## Energy trading

\[edit\]
Electrical energy markets are wholesale, international markets that trade electrical energy.<sup>\[27\]</sup><sup>\[4\]</sup> Market prices fluctuate with demand and supply (e.g., when the wind subsides). The VPP behaves as a conventional dispatchable power plant from the point of view of other market participants. A VPP arbitrages between diverse energy markets (e.g., bilateral and purchase power agreements (PPA), forward and futures markets, and the pool).<sup>\[2\]</sup><sup>\[3\]</sup><sup>\[6\]</sup><sup>\[7\]</sup>

Five risk-hedging strategies have been applied to VPP decision-making to measure the degree of conservatism of VPPs' decisions in energy trading (e.g., day-ahead electricity market, derivatives exchange market, and bilateral contracts):

- IGDT: Information Gap Decision Theory<sup>\[2\]</sup>
- RO: Robust optimization<sup>\[3\]</sup>
- CVaR: Conditional value at risk<sup>\[6\]</sup>
- FSD: First-order Stochastic Dominance<sup>\[4\]</sup>
- SSD: Second-order Stochastic Dominance<sup>\[7\]</sup><sup>\[28\]</sup>

## Markets

\[edit\]
### United States

\[edit\]
In 2023 the Department of Energy estimated VPP capacity at around 30 to 60 GW, some 4–8% of peak electricity demand.<sup>\[11\]</sup>

Texas has two Tesla-operated VPPs. Eligible Tesla Electric members automatically join the Virtual Power Plant, consisting of Tesla Powerwall batteries. Tesla pays the owner a monthly fee in addition to payment per unit of energy delivered.<sup>\[29\]</sup>

California has two electric markets: retail and wholesale. As of 2022 PG&E paid VPP providers $2/kWh during peak demand.<sup>\[30\]</sup> As of August/September 2022, SunRun VPP often delivered 80 MW at peak times,<sup>\[31\]</sup> while Tesla VPP supplied 68 MW.<sup>\[32\]</sup><sup>\[33\]</sup> By 2025, California was testing 100,000 residential batteries at a combined 535 MW.<sup>\[34\]</sup> That amount of electricity can power a mid-sized city. It is part of the process to advance the smart grid, where utilities don't just send power to customers but the process is interactive. In September 2026, two bills that will create new opportunities for virtual power plants to reduce utility costs, SB 905 and SB 913, both authored by state Sen. Josh Becker, were signed into law.<sup>\[35\]</sup>

Virginia's Virtual Power Plant (VPP) pilot program is a state-mandated initiative requiring Dominion Energy Virginia (a Phase II Utility) to implement a pilot VPP.<sup>\[36\]</sup> The pilot is capped at 450 MW.<sup>\[37\]</sup> It is to include incentives for 15 MW+ of distributed BESS, including residential, commercial, and industrial customers.<sup>\[38\]</sup> As of early 2026, the program represented one of the US' largest VPP pilots.<sup>\[38\]</sup> A program for electrification of school buses must be filed by December 31, 2027.<sup>\[39\]</sup>

Vermont's Green Mountain Power works with Tesla to offer a Powerwall to participating customers at a discounted rate.<sup>\[11\]</sup>

Three Massachusetts utilities, National Grid, Eversource, and Cape Light Compact, operate a VPP.<sup>\[11\]</sup> The Massachusetts Clean Energy Center (MassCEC) is implementing a vehicle‑to‑everything (V2X) demonstration program as part of its VPP that installs free, bi‑directional EV chargers at school districts, municipalities, and residents.<sup>\[40\]</sup>

### Europe

\[edit\]
The Institute for Solar Energy Supply Technology of Germany's University of Kassel pilot-tested a VPP that linked solar, wind, biogas, and pumped-storage hydroelectricity to provide load-following power from renewable sources.<sup>\[41\]</sup>

The isolated Scottish Inner Hebrides island of Eigg generates electricity using renewable sources and balances demand using batteries.<sup>\[42\]</sup><sup>\[43\]</sup>

Kraftwerke operates a VPP in seven European countries that provides peak-load resources, power trading and grid balancing. The company aggregates energy from biogas, solar and wind as well as large-scale power consumers.<sup>\[44\]</sup>

A London VPP is supported by UK Power Networks, and Powervault.<sup>\[17\]</sup> SMS plc operates a UK VPP.<sup>\[19\]</sup>

Tesla operates in the UK in partnership with Octopus Energy. Participant homes are powered with renewable energy from solar panels or from Octopus Energy.<sup>\[20\]</sup>

German companies Enpal and Entrix operate Europe's largest VPP that integrates PV, BESS, and electric vehicles. Enpal is a solar installer with more than 70,000 installed systems, connects thousands of solar/BESS households to the VPP.<sup>\[45\]</sup><sup>\[46\]</sup>

### Australia

\[edit\]
AGL Energy operates a 25 MW virtual-power-plant scheme in Adelaide. The company supplies BESS and photovoltaic systems, to >8,000 customers. The systems cost consumers A$3500 with a  7 year payout. As of 2025, the program provided 25 MW solar and 37 MW storage.<sup>\[47\]</sup><sup>\[48\]</sup>

## See also

\[edit\]
## References

\[edit\]
1. ↑ Landsbergen, Patrick (17 June 2009). *Feasibility, beneficiality, and institutional compatibility of a micro-CHP virtual power plant in the Netherlands* (BSc thesis) – via repository.tudelft.nl.
2. 1 2 3 4 5 Shabanzadeh M; Sheikh-El-Eslami, M-K; Haghifam, P; M-R (January 2015). "Decision Making Tool for Virtual Power Plants Considering Midterm Bilateral Contracts". *3rd Iranian Regional CIRED Conference and Exhibition on Electricity Distribution, at Niroo Research Institute (NRI), Tehran, Iran*. **3** (3): 1–6. doi:10.13140/2.1.5086.4969.
3. 1 2 3 4 5 Shabanzadeh M; Sheikh-El-Eslami, M-K; Haghifam, P; M-R (October 2015). "The design of a risk-hedging tool for virtual power plants via robust optimization approach". *Applied Energy*. **155**: 766–777. Bibcode:2015ApEn..155..766S. doi:10.1016/j.apenergy.2015.06.059.
4. 1 2 3 4 5 6 Shabanzadeh M; Sheikh-El-Eslami, M-K; Haghifam, P; M-R (January 2017). "Risk-based medium-term trading strategy for a virtual power plant with first-order stochastic dominance constraints". *IET Generation, Transmission & Distribution*. **11** (2): 520–529. doi:10.1049/iet-gtd.2016.1072. S2CID 114478127.
5. ↑ Zurborg, Aaron (2010). "Unlocking Customer Value: the Virtual Power Plant" (PDF). *Energy.gov*. Retrieved 15 January 2023.
6. 1 2 3 4 Shabanzadeh M; Sheikh-El-Eslami, M-K; Haghifam, P; M-R (May 2016). "A medium-term coalition-forming model of heterogeneous DERs for a commercial virtual power plant". *Applied Energy*. **169**: 663–681. Bibcode:2016ApEn..169..663S. doi:10.1016/j.apenergy.2016.02.058.
7. 1 2 3 4 Shabanzadeh M; Sheikh-El-Eslami, M-K; Haghifam, P; M-R (April 2016). "Modeling the cooperation between neighboring VPPS: Cross-regional bilateral transactions". *2016 Iranian Conference on Renewable Energy & Distributed Generation (ICREDG)*. Vol. 11. pp. 520–529. doi:10.1109/ICREDG.2016.7875909. ISBN 978-1-5090-0857-5. S2CID 16453458.
8. ↑ Lee, Zachary E.; Sun, Qingxuan; Ma, Zhao; Wang, Jiangfeng; MacDonald, Jason S.; Zhang, K. Max (Feb 2020). "Providing Grid Services With Heat Pumps: A Review". *Journal of Engineering for Sustainable Buildings and Cities*. **1** (1) 011007. doi:10.1115/1.4045819. S2CID 213898377.
9. ↑ Landsbergen, Patrick (17 June 2009). *Feasibility, beneficiality, and institutional compatibility of a micro-CHP virtual power plant in the Netherlands* (BSc thesis) – via repository.tudelft.nl.
10. ↑ Fang, Xi; Misra, Satyajayant; Xue, Guoliang; Yang, Dejun (2012). "Smart Grid — The New and Improved Power Grid: A Survey". *IEEE Communications Surveys & Tutorials*. **14** (4): 944–980. doi:10.1109/SURV.2011.101911.00087. ISSN 1553-877X.
11. 1 2 3 4 5 Kim, June (February 7, 2024). "How virtual power plants are shaping tomorrow's energy system". *MIT Technology Review*. Retrieved 2024-02-28.
12. 1 2 Silverstein, Ken. "Electricity Users and Virtual Power Plants". *Forbes*. Retrieved December 16, 2024.
13. 1 2 3 4 Minai, Ahmad Faiz; Khan, Akhlaque Ahmad; Kitmo; Ndiaye, Mouhamadou Falilou; Alam, Tabish; Khargotra, Rohit; Singh, Tej (2024-05-01). "Evolution and role of virtual power plants: Market strategy with integration of renewable based microgrids". *Energy Strategy Reviews*. **53** 101390. doi:10.1016/j.esr.2024.101390. ISSN 2211-467X.
14. ↑ Brane Janjič (2011-10-17). "Elektro Ljubljana v Amsterdamu predstavil prvo virtualno elektrarno". *Naš stik* (in Slovenian).
15. ↑ Carlo Degli Esposti (2019-12-20). D7.6 Final project conference proceedings to disclose the consortium conclusions and recommendations (PDF) (Report). FutureFlow. p. 31.
16. ↑ Slezak, Michael (5 August 2016). "Adelaide charges ahead with world's largest 'virtual power plant'". *The Guardian*. Retrieved 2016-08-05.
17. 1 2 "Electricity network plan to launch London's first virtual power station". *UK Power Networks*. 22 June 2018. Retrieved 15 October 2021.
18. ↑ "London pioneers first 'virtual power station'". *GOV.UK*. 6 March 2020. Retrieved 1 July 2021.
19. 1 2 Grundy, Alice (27 March 2020). "Smart Metering Systems reveals Solo Energy acquisition as it enters VPP market". *Current News*. Retrieved 1 July 2021.
20. 1 2 Lempriere, Molly (27 October 2020). "Tesla Energy Plan launched inviting homes to become part of Virtual Power Plant". *Current News*. Retrieved 1 July 2021.
21. ↑ "Enpal, Entrix reveal plans for Europe's biggest VPP". *PV Magazine*. 14 June 2024. Retrieved 25 September 2024.
22. ↑ Gribbins, Savannah. "Smart Grid, Smart Move: Virginia Governor Greenlights Virtual Power Plant Pilot". *blog.advancedenergyunited.org*.
23. ↑ "Virtual power plant capacity expands 13.7% year-over-year to reach 37.5 GW, according to Wood Mackenzie". *Wood Mackenzie*.
24. ↑ Lee, Zachary E.; Sun, Qingxuan; Ma, Zhao; Wang, Jiangfeng; MacDonald, Jason S.; Zhang, K. Max (Feb 2020). "Providing Grid Services With Heat Pumps: A Review". *Journal of Engineering for Sustainable Buildings and Cities*. **1** (1) 011007. doi:10.1115/1.4045819. S2CID 213898377.
25. ↑ Fang, Xi; Misra, Satyajayant; Xue, Guoliang; Yang, Dejun (2012). "Smart Grid — The New and Improved Power Grid: A Survey". *IEEE Communications Surveys & Tutorials*. **14** (4): 944–980. doi:10.1109/SURV.2011.101911.00087. ISSN 1553-877X.
26. ↑ "Manage the Virtual Power and prevent a blackout!". *Next Kraftwerke*. Retrieved 2 December 2019.
27. ↑ JEAN-PHILIPPE TAILLON, CFA (2021-10-14). "Introduction to the World of Electricity Trading". Investopedia. Retrieved 2022-01-04.
28. ↑ Shabanzadeh, Morteza; Sheikh-El-Eslami, Mohammad-Kazem; Haghifam, Mahmoud-Reza (2017). "An interactive cooperation model for neighboring virtual power plants". *Applied Energy*. **200**: 273–289. Bibcode:2017ApEn..200..273S. doi:10.1016/j.apenergy.2017.05.066. S2CID 157309706.
29. ↑ "Tesla Electric Virtual Power Plant Beta with ERCOT". *tesla.com*. Retrieved February 29, 2024.
30. ↑ "PG&E, Tesla virtual power plant delivers 16.5 MW to California grid amid calls for energy conservation". *Utility Dive*. 23 August 2022.
31. ↑ Colthorpe, Andy (8 September 2022). "California's fleet of battery storage working to avert energy crisis". *Energy Storage News*.
32. ↑ Lambert, Fred (2022-09-02). "Tesla virtual power plant is rocketing up, reaches 50 MW". *Electrek*. Retrieved 2022-09-08.
33. ↑ "Tesla's Virtual Power Plant Tracker". *Lastbulb*. Retrieved 2022-09-08.
34. ↑ Driscoll, William (6 August 2025). "100,000 residential batteries in California tested as one distributed power plant". *Energy Storage*.
35. ↑ 
St. John, Jeff (2026-10-01). "Newsom finally says yes to virtual power plants". *Canary Media*. Retrieved 2026-10-10.
36. ↑ "§ 56-585.1:16. Virtual power plant pilot program". *Virginia Law*. Retrieved February 6, 2026.
37. ↑ "Virginia utility-scale VPP pilot mandate is first amid national push". *Utility Dive*. May 12, 2025. Retrieved February 6, 2026.
38. 1 2 "New Laws: Sharing and Distributing Clean Energy Through Virtual Power Plants". *Virginia Conservation Network*. July 25, 2025. Retrieved February 6, 2026.
39. ↑ No later than December 1, 2025, each Phase II Utility shall petition the State\_Corporation\_Commission (the Commission) for approval to conduct a pilot program to evaluate methods to optimize demand through various technology applications including the establishment of virtual power plants. Such pilot program shall evaluate electric grid capacity needs and the ability of such virtual power plants to provide grid services, including Peak-shaving, during times of peak electric demand. Such pilot program shall consist of aggregations of distributed energy resources totaling up to 450 megawatts for a Phase II Utility and shall include Distributed\_energy\_resources located in multiple geographic regions of the Commonwealth. An electric utility may utilize any existing or proposed distributed energy programs as part of the pilot program and to further the development of virtual power plants in the Commonwealth. An electric utility that petitions the Commission for such pilot program shall demonstrate that the utility has evaluated funding opportunities from the U.S. Department of Energy. In furthering the goals of such pilot program, the electric utility shall (i) propose programs of at least 15 megawatts incentivizing residential customers to purchase battery storage devices and (ii) notwithstanding the provisions of § 56-585.1:13 of the Code of Virginia, propose a broader electric school bus program as part of a grid transformation filing no later than December 31, 2027, and the Commission may require competitive solicitation open to utility-owned and non-utility-owned resources. The electric utility shall not own the electric school buses as a part of its proposed program, but such electric utility may own the related storage batteries. The electric utility shall only use the bus storage batteries to access the stored electricity at times when the participating school system determines that the electric school buses are not needed to transport students. https://law.lis.virginia.gov/vacode/title56/chapter23/section56-585.1:16/
40. ↑ Lewis, Michelle (2026-02-03). "Free V2X chargers will let Massachusetts EVs power the grid". *Electrek*. Retrieved 2026-02-06.
41. ↑ "The Combined Power Plant: the first stage in providing 100% power from renewable energy". SolarServer. January 2008. Archived from the original on 2008-10-14. Retrieved 2008-10-10.
42. ↑ Gardiner, Karen (30 March 2017). "The small Scottish isle leading the world in electricity". *www.bbc.com*. Retrieved 2023-07-17.
43. ↑ BBC Radio 4. Costing the Earth- Electric Island
44. ↑ "Next Kraftwerk Reimagines & Redefines The Electrical Grid With Virtual Power Plants". Clean Technica. October 2016. Retrieved 2019-03-13.
45. ↑ "Enpal, Entrix reveal plans for Europe's biggest VPP". *PV Magazine*. 14 June 2024. Retrieved 25 September 2024.
46. ↑ "So baut Solar-Installateur Enpal das größte virtuelle Kraftwerk in Europa". *Frankfurter Allgemeine Zeitung*. 14 June 2024. Retrieved 25 September 2024.
47. ↑ "Tesla's South Australian virtual power plant sold to utility AGL". *Energy Storage*. 4 July 2025.
48. ↑ Heynes, George (2025-07-07). "AGL Energy buys the South Australia Virtual Power Plant from Tesla". *Energy-Storage.News*. Retrieved 2026-02-06.
