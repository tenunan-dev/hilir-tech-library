---
source_id: "doe-hfto"
title: "Hydrogen Shot Water Electrolysis Technology Assessment 2024"
summary: "2024 DOE Hydrogen Shot assessment of water electrolysis technology pathways, comparing technologies and their cost and readiness against the Hydrogen Shot goal."
url: "https://www.energy.gov/sites/default/files/2024-12/hydrogen-shot-water-electrolysis-technology-assessment.pdf"
retrieved_at: "2026-10-24T05:14:03+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC", "MAT"]
sha256: "fa39036af3aecdf85b40a8840ede430b091a54fef6ed88323e0033910fbc8d33"
collected: "manual"
---

# Hydrogen Shot Water Electrolysis Technology Assessment 2024

HYDROGEN SHOT: 
Water Electrolysis Technology Assessment

2 
 
Hydrogen Shot: Water Electrolysis Technology Assessment 
 
Lead Authors: 
McKenzie Hubert, Hydrogen and Fuel Cell Technologies Office (HFTO) 
Anne Marie Esposito, HFTO 
David Peterson, HFTO 
Eric Miller, HFTO 
Joseph Stanford, HFTO 
 
Reviewed by:  
Jai-Woh Kim, Office of Fossil Energy and Carbon Management (FECM) 
Eva Rodezno, FECM 
Jennifer Roizen, Basic Energy Sciences 
Viviane Schwartz, Basic Energy Sciences 
Steve Capanna, Office of Policy (OP) 
Ryan Wiser, OP 
Brandon McMurtry, OP 
Sunita Satyapal, HFTO 
Katherine Rinaldi, HFTO 
James Vickers, HFTO 
Elias Pomeroy, HFTO 
Tomas Green, HFTO 
Michael Hahn, HFTO 
Rick Farmer, HFTO 
Michael Ulsh, National Renewable Energy Laboratory (NREL) 
Alex Badgett, NREL 
Bryan Pivovar, NREL 
Caitlin Murphy, NREL 
Micah Casteel, Idaho National Laboratory 
Brian James, Strategic Analysis Inc. 
Yaset Acevedo, Strategic Analysis Inc. 
Jacob Prosser, Strategic Analysis Inc.

3 
 
ACRONYMS 
AEM alkaline exchange membrane 
BOL beginning of life 
BOP balance of plant 
CO2 carbon dioxide 
DOE U.S. Department of Energy 
GHG greenhouse gas 
GREET Greenhouse Gases, Regulated Emissions, and Energy use in Technologies 
H2 hydrogen 
H2A-Lite Hydrogen Analysis Lite Production 
HTE high-temperature electrolyzer 
LA liquid alkaline 
LCOH levelized cost of hydrogen 
LTE low-temperature electrolyzer 
O-SOEC oxide-ion-conducting solid-oxide electrolyzer cell 
PEM proton exchange membrane 
PGM platinum group metal 
P-SOEC proton-conducting solid-oxide electrolyzer cell 
PTL porous transport layer 
RD&D research, development, and demonstration 
RDD&D research, development, demonstration, and deployment 
SOFC solid-oxide fuel cell 
TRL technology readiness level

4 
 
TABLE OF CONTENTS 
Executive Summary ................................................................................................................... 5 
Introduction ................................................................................................................................ 7 
Hydrogen Shot ....................................................................................................................... 7 
Impact .................................................................................................................................... 7 
Clean Hydrogen Technology Pathways .................................................................................. 7 
Technology Assessment vs. Commercial Liftoff ...................................................................... 9 
Water Electrolysis Overview ......................................................................................................10  
Techno-Economic Analysis .......................................................................................................13  
GHG Emissions and Water Consumption .................................................................................19  
Overview of RD&D Needs To Achieve Hydrogen Shot Goals ...................................................21  
Manufacturing: Status and Cost Reduction Potential................................................................. 24 
Electrolyzer Technologies: Status and Cost Reduction Potential ..............................................26  
PEM Electrolyzers .................................................................................................................26  
System Cost Analysis ........................................................................................................26  
RD&D Approaches for Cost Reduction ..............................................................................27  
LA Electrolyzers ....................................................................................................................30  
System Cost Analysis ........................................................................................................30  
RD&D Approaches for Cost Reduction ..............................................................................31  
O-SOECs ..............................................................................................................................34  
System Cost Analysis ........................................................................................................34  
RD&D Approaches for Cost Reduction ..............................................................................35  
AEM Electrolyzers .................................................................................................................38  
Status and R&D Cost Reduction Approaches ....................................................................38  
P-SOECs ...............................................................................................................................41  
Status and R&D Cost Reduction Approaches ....................................................................41  
Energy System Integration: Status and Cost Reduction Potential .............................................43  
Conclusion ................................................................................................................................45  
References ...............................................................................................................................46  
Appendix ...................................................................................................................................50

5 
 
EXECUTIVE SUMMARY 
In June 2021, the U.S. Department of Energy (DOE) announced the first of a series of 
department wide Energy Earthshots™ designed to accelerate breakthroughs of more abundant, 
affordable, and reliable clean energy solutions within the decade. The Hydrogen Shot™ seeks 
to reduce the cost of clean hydrogen (H2) production to $1 per 1 kilogram in 1 decade (“1 1 1”). 
As part of this initiative, DOE is developing in-depth technology assessments of three general 
pathways to clean hydrogen production: water electrolysis using renewable- or nuclear-
generated electricity (this report); thermal conversion (e.g., reforming of natural gas with carbon 
capture); and advanced pathways (e.g., direct solar water splitting or biological conversion of 
waste streams) [1]. As one in a series of Hydrogen Shot reports and assessments, this report, 
Hydrogen Shot: Water Electrolysis Technology Assessment, focuses primarily on current 
electrolyzer status and research, development, and demonstration (RD&D) needs to achieve 
$1/kg H2 based on current information and analysis. Updated assessments with more detailed 
analysis will follow as the technologies advance.  
 
Water electrolysis, the process of using electricity to convert water into hydrogen and oxygen 
gases, is a rapidly growing industry for hydrogen production. When electrolysis uses clean 
electricity, clean hydrogen can be produced with zero or near-zero carbon dioxide (CO2) 
emissions. However, hydrogen produced by water electrolysis is currently more expensive than 
incumbent hydrogen production methods that utilize fossil fuel feedstocks, such as natural gas. 
Steam methane reforming of natural gas is the most common method of low-cost hydrogen 
production today; however, this process emits approximately 10 tons of CO2 for every ton of 
hydrogen produced. In the near term, carbon capture, utilization, and storage can be employed 
with steam methane reforming to reduce CO2 emissions, but with added costs. In the long term, 
opportunities for deep decarbonization through clean hydrogen deployments will require 
sustainable approaches such as water electrolysis coupled with renewable and/or nuclear 
power generation. However, significant capital and operating cost reductions, as well as science 
and technology advancements, will be needed to meet the Hydrogen Shot goals and enable 
greater market demand for clean electrolytic hydrogen. 
 
This report documents the current state of development of five different electrolyzer 
technologies: proton exchange membranes, liquid alkaline, oxide-ion-conducting solid-oxide 
electrolyzer cells, alkaline exchange membranes, and proton-conducting solid-oxide electrolyzer 
cells. Boundary-level techno-economic analysis—using grid scenarios for electricity cost—
shows that the current cost of hydrogen produced from these types of electrolyzers ranges from 
approximately $6/kg to $8/kg (depending on the electrolyzer technology), while recognizing that 
grid electricity does not currently qualify as clean, and that indirect emissions from grid-
connected electrolysis can be significant. Further analysis also shows that the Hydrogen Shot 
goal of $1/kg for clean hydrogen produced by water electrolysis powered by clean electricity is 
aggressive, but potentially achievable in the future, if we develop advanced technologies, 
manufacture them at scale, and leverage ongoing cost reductions in clean electricity generated 
by diverse renewable and/or nuclear resources across the nation. Since the Hydrogen Energy 
Earthshot was launched, supply chain issues, higher electrolyzer system installation costs, and 
inflation have increased costs, making this goal even more challenging to achieve. In light of 
such challenges, this report describes the critical technology and manufacturing advancements,

6 
 
as well as integrated energy system developments, that will be needed through continued 
RD&D efforts. While each electrolyzer technology has its own specific development needs, all 
technologies can benefit from at-scale manufacturing processes, balance-of-plant cost 
reductions, and system optimization with clean energy resources. Deploying water electrolyzers 
that utilize low-cost clean electrons at or near the site of electricity generation is an important 
potential pathway to producing low-cost, clean hydrogen meeting the Hydrogen Shot goal.

7 
 
INTRODUCTION 
Hydrogen Shot 
The Hydrogen Shot1 is the first Energy Earthshot launched under the U.S. Department of 
Energy’s (DOE’s) Energy Earthshots Initiative, which will accelerate breakthroughs of more 
abundant, affordable, and reliable clean energy solutions within the decade. Achieving the 
Energy Earthshots will help America tackle the toughest remaining barriers to addressing the 
climate crisis and more quickly reach the Biden-Harris administration’s goal of net-zero carbon 
emissions by 2050 while creating good-paying union jobs and growing the economy. 
 
The Hydrogen Shot establishes a 
framework and foundation for the 
deployment of clean hydrogen (H2) 
across multiple sectors of the 
economy—most importantly in “hard-
to-decarbonize” applications. This 
framework includes support for 
research, development, 
demonstration, and deployment 
(RDD&D) projects. Industries are 
beginning to implement clean hydrogen to reduce emissions, yet many hurdles remain to 
deploying it at scale, requiring continued RDD&D. Currently, hydrogen from clean and 
renewable energy costs well over $5 per kilogram. Achieving the Hydrogen Shot’s 80% cost 
reduction goal can unlock new markets for hydrogen, including steel manufacturing, clean 
ammonia, energy storage, and heavy-duty trucks. This would create more clean energy jobs, 
reduce greenhouse gas (GHG) emissions, and position America to compete in the clean 
hydrogen market on a global scale. The needed RDD&D efforts should ensure that 
environmental protection and benefits for local communities remain a priority. 
 
Impact 
The Hydrogen Shot goal is aligned with the priorities for affordable clean hydrogen articulated in 
the U.S. National Clean Hydrogen Strategy and Roadmap [2]. If the national strategy is 
successfully implemented, scenarios show the opportunity for at least a fivefold increase in 
clean hydrogen use, including in end uses that are otherwise difficult to decarbonize. Estimates 
in the U.S. National Clean Hydrogen Strategy and Roadmap show the potential for clean 
hydrogen to contribute to substantial reductions in GHG emissions economywide by 2050, as 
well as the potential to create more than 100,000 direct and indirect jobs by 2030. The 
Hydrogen Shot will catalyze innovation in all clean hydrogen production pathways, encouraging 
investment in diverse regions across the country. 
 
Clean Hydrogen Technology Pathways 
In pursuit of the Hydrogen Shot, DOE focuses on the research, development, and 
demonstration (RD&D) of multiple technology pathways with the potential to achieve affordable 
 
1 www.energy.gov/eere/fuelcells/hydrogen-shot. 
The first Energy Earthshot, launched June 7, 2021— 
Hydrogen Shot—seeks to reduce the cost of clean hydrogen 
by 80% to $1 per 1 kilogram in 1 decade (“1 1 1”).

8 
 
clean hydrogen production in the near and longer terms, leveraging different resources across 
the nation. These technology pathways fall broadly into three main categories: 
 
• ELECTROLYSIS  
The electrolysis pathways are based on commercial and near-commercial 
technologies for splitting water into hydrogen and oxygen, which can be powered by low-
carbon sources such as wind, solar, hydropower, or nuclear energy (among others) to 
produce clean hydrogen. Examples include low-temperature electrolyzers (LTEs) using 
liquid alkaline (LA) solutions or proton exchange membranes (PEMs) as ionic 
conductors, as well as higher-temperature solid-oxide electrolyzers with the potential for 
higher electricity-to-hydrogen conversion efficiency. Hydrogen Shot strategic priorities for 
electrolysis pathways include improving performance and cost of electrolyzer systems 
(e.g., stacks and balance of plant [BOP]) at gigawatt scales; optimizing integration of 
electrolyzer systems with renewable or nuclear power to leverage low-cost on-site 
electricity; and facilitating expanded domestic manufacturing capacity. 
 
• THERMAL CONVERSION  
Thermal conversion processes use heat as a primary energy source to drive chemical 
reactions that convert carbon-based feedstocks into hydrogen and other byproducts. 
Examples include reforming, gasification, and pyrolysis processes. Carbon capture, 
utilization, and storage can be used in conjunction with thermal conversion to reduce the 
carbon footprint of the hydrogen produced. The Hydrogen Shot’s strategic priorities for 
thermal conversion include improving the performance and cost of integrated systems 
for natural gas reforming with carbon capture, and storage to achieve emissions targets, 
as well as developing diverse options such as gasification of waste feedstocks with 
carbon capture and storage and pyrolysis of natural gas into hydrogen and solid carbon 
to meet cost and emissions goals. These priorities are examined in detail in the report 
Hydrogen Shot Technology Assessment: Thermal Conversion Approaches, which was 
released in December 2023 [1]. 
 
• ADVANCED PATHWAYS 
As part of the longer-term vision, clean hydrogen can also be produced through a variety 
of new and advanced pathways requiring little or no electricity inputs. Examples include 
photoelectrochemical and thermochemical processes for direct solar water splitting, and 
biological processes that can convert biomass or waste streams into hydrogen with 
value-added coproducts (such as purified water). Additionally, advanced hybrid 
approaches combining electrochemical, thermochemical, pyrolytic, and/or 
photoelectrochemical processes producing clean hydrogen from water, biomass, or 
wastes are being explored. Other interesting opportunities, such as geological hydrogen, 
are also being investigated. The Hydrogen Shot’s strategic priorities for advanced 
pathways include high-risk, high-reward R&D to advance fundamental scientific 
understanding that can drive progress across multiple advanced hydrogen production 
pathways. These priorities will be examined in detail in the forthcoming report, Hydrogen 
Shot Technology Assessment: Advanced Pathways.

9 
 
Technology Assessment vs. Commercial Liftoff 
This report provides a technology assessment of electrolysis pathways for clean hydrogen 
production covered by the Hydrogen Shot. As noted above, other documents will provide 
technology assessments of thermal conversion pathways and advanced pathways [1]. 
Consistent with methodologies adopted in all of DOE’s Energy Earthshots, these assessments 
are intended to track status and RD&D improvements relative to a 10-year performance target 
that will directly support long-term national decarbonization goals. As such, a techno-economic 
framework has been adopted in this report referencing a static technology performance baseline 
separate from variable economic factors such as inflation. Specifically for the Hydrogen Shot, 
technology baselines for the various clean hydrogen production pathway costs were established 
on the basis of 2020 dollars (2020 $), and status and projected cost reductions compared to the 
baselines are reported in the same basis to emphasize the impact of RD&D on technology 
advancement and facilitate comparison between pathways, separate from consideration of 
macroeconomic factors. For consistency, all Energy Earthshots will use the same 2020 dollar 
basis for annual comparisons related to technology development but will also track 
corresponding values for nominal year dollars to facilitate comparisons with other analyses and 
reports. 
 
For example, DOE, through its Pathways to Commercial Liftoff initiative, tracks year-over-year 
changes in the commercial deployment status and prospects of different clean energy 
technologies reflective of the present economywide realities, including inflation and supply chain 
factors. The resulting reports are intended specifically to provide valuable information for 
industry stakeholders and investors who have the potential to take action that will accelerate 
deployment. The Pathways to Commercial Liftoff: Clean Hydrogen report addresses 
electrolyzer technologies, as well as the other Hydrogen Shot pathways; however, the techno-
economic framework is different and considers available costs in current-year dollars, as well as 
the impacts of various incentives [3]. The cost projections presented in this report are related to 
various cost scenarios in the Pathways to Commercial Liftoff report, including through the use of 
harmonized technical inputs and assumptions in both reports. However, it is important to 
emphasize that the interpretation of results relative to specific electrolyzer technologies must 
account for the different purposes of each document, as well as the different techno-economic 
frameworks employed. 
 
This Hydrogen Shot technology assessment presents a snapshot of various electrolyzer 
technology pathways for clean hydrogen production, including technology status and envisioned 
approaches for achieving the Hydrogen Shot goals through RD&D advances. This document, as 
well as the Pathways to Commercial Liftoff report, will be updated periodically by DOE to reflect 
progress reported by stakeholders from industry, academia, and the national labs.

10 
 
WATER ELECTROLYSIS OVERVIEW  
Hydrogen can be produced from water using electricity 
through an electrochemical process known as 
electrolysis. As shown in Figure 1, electrolysis splits 
water into hydrogen and oxygen gases; systems 
employing this process are called electrolyzers. 
Electrolyzer systems consist of stacks (groups of 
individual cells) and BOP equipment that manages the 
inputs (electricity and water) and outputs (hydrogen and 
oxygen) from the stack (Figure 2). The use of water 
electrolysis powered by the nation’s abundant clean 
energy resources is aligned with the Hydrogen Shot 
mission and is expected to play a critical role in achieving 
national decarbonization goals [4]. 
 
As electrolyzer technologies improve and their costs 
come down, global capacity is expected to increase 
substantially. By 2030, the global installed capacity of 
electrolyzers has the potential to grow to more than 300 GW (based on announced projects), 
from only about 1 GW installed as of October 2023 [5]. When these deployments are coupled 
with electricity from renewables or nuclear power, the clean hydrogen produced can offer 
significant decarbonization potential across multiple sectors [3] [6] [7].  
 
 
Figure 2. Electrolyzer systems are composed of stacks and BOP components. Stacks are composed of individual cells. 
The size and number of cells in a stack, the number of stacks in a system, and the BOP equipment in a system can all vary 
depending on the system’s configuration. 
 
Figure 1. PEM electrolyzer cell—showing 
water and electricity in and hydrogen and 
oxygen gases out.

11 
 
Current electrolyzer technologies are at different technology readiness levels (TRLs), use 
different electrolyte materials (liquid, solid polymer membranes, or solid ceramics), and operate 
at different temperatures, typically determined by the limits of the electrolyte material. 
Electrolyzer technologies are commonly grouped into two categories based on operating 
temperature: LTEs and high-temperature electrolyzers (HTEs). 
 
LTE technologies include:  
 
• PEMs 
• LA 
• Alkaline exchange membranes (AEMs). 
 
HTE technologies include: 
 
• Oxide-ion-conducting solid-oxide 
electrolyzer cells (O-SOECs) 
• Proton-conducting solid-oxide 
electrolyzer cells (P-SOECs). 
 
Figure 3 shows a classification of these key 
electrolyzer types according to operating 
temperature and electrolyte type. The color 
of each technology block represents the 
current domestic commercialization level, 
where dark blue is the most commercially 
mature.  
 
This assessment focuses on each of the five electrolyzer technologies described above. Each 
technology offers unique benefits and pathways to achieve the Hydrogen Shot goal (Table 1). 
The most commercially advanced technologies could more rapidly achieve manufacturing 
economies of scale, which would drive down capital costs and thereby reduce overall hydrogen 
cost, bringing it closer to the $1/kg-H2 target. While they are not yet at the same level of 
commercialization, other technologies in the laboratory, pilot, and early commercial stages have 
certain advantages and the potential to achieve even lower costs in the future than commercial 
technologies. 
  
 
Figure 3. Electrolyzer technologies as a function of 
electrolyte and operating temperature. The most 
commercially mature technologies are shown in dark 
blue.

12 
 
Table 1. Comparison of Electrolyzer Technologies 
Technology Commercial Status Advantages 
LA Commercial 
• Low-cost materials 
• Proven long lifetime 
• Established supply chain and manufacturing processes. 
PEM Commercial 
• High current density at high efficiency 
• Differential pressure operation 
• Dynamic operation capability. 
O-SOEC Early Commercial • High electrical efficiency • Thermal energy integration. 
AEM Pilot • Low-cost materials • Dynamic operation capability. 
P-SOEC Laboratory 
• High electrical efficiency 
• Thermal energy integration 
• Lower-cost materials and operating temperature than O-
SOEC. 
 
The following section discusses the cost status of clean hydrogen production from the three 
most commercially mature electrolyzer technologies and the major common cost drivers of 
electrolytic hydrogen production. Achieving the Hydrogen Shot goal will require addressing a 
unique set of challenges and RDD&D needs for each technology, which are summarized later in 
this document.

13 
 
TECHNO-ECONOMIC ANALYSIS  
The economics of clean hydrogen production via water electrolysis depend not only on the 
electrolyzer cost, performance, and system design, but also on the source of clean electricity. 
Some electrolyzer technologies may be better suited for integration with different clean energy 
sources or end uses, which can influence the optimal operating strategy and size of the 
electrolyzer system. For example, HTE technologies can take advantage of integration with 
thermal energy sources, such as those at nuclear power plants, while membrane-based LTE 
technologies are well suited for clean energy sources with either stable or variable energy 
output (both nuclear and variable renewable energy sources). 
 
The levelized cost of hydrogen (LCOH) in 2020 $ was estimated for PEM, LA, and O-SOEC (the 
three most commercially advanced technologies to date) using a simplified, boundary-level set 
of parameters. The Hydrogen Analysis Lite Production (H2A-Lite) model, a peer-reviewed 
national-laboratory-developed model, was used to compare the technologies using a consistent 
financial analysis framework [8]. Key inputs into the model, such as electrolyzer cost and 
efficiency, are based on feedback from industry and national laboratory experts and are 
generally consistent with other reported values, including those in the recent DOE Hydrogen 
Program Record Clean Hydrogen Production Cost Scenarios with PEM Electrolyzer 
Technology, when the dollar-year basis is accounted for appropriately [9]. The target-level 
approach considers a broad range of electricity prices and capacity factors from current and 
future plausible scenarios resulting in a range of LCOH estimates. 
 
As the Hydrogen Shot is directed at hydrogen production cost, the LCOH estimates in this 
document are focused on the hydrogen production component of the overall hydrogen 
production cost. Depending on the end use requirements (e.g., the need for a consistent 
hydrogen production rate, or capacity factor of the electricity source), there are other 
components (e.g., hydrogen storage) that will be needed that will add cost. In general, more 
hydrogen storage will be needed for systems with lower capacity factors to compensate for 
reduced hydrogen production at varying time intervals. There are other ongoing analyses that 
are investigating hydrogen cost for complete systems from the electricity source to the end use 
[10]. 
 
The LCOH can vary dramatically based on current technologies’ capital cost and performance, 
and when electricity is supplied from different sources, such as the U.S. electrical grid, land-
based wind, conventional nuclear power, or hybrid renewable energy systems [9]. Figure 4 
shows the projected LCOH using electricity from the current U.S. electrical grid (with limited 
renewable penetration), as well as conceptual scenarios for 2026 and 2031 for hydrogen 
production by different electrolyzer technologies using a projected future grid and different 
renewable and nuclear resources. The 2026 and 2031 target scenarios shown in the figure 
include projected electrolyzer technology and cost improvements over the current status, as well 
as aggressive reductions in the cost of renewable electricity generation. A detailed description 
of the analysis methods, key input parameters, references, and tabulated results for Figure 4 
can be found in the Appendix.

14 
 
 
Figure 4. Current and future LCOH from PEM, LA, and O-SOEC electrolyzers in 2020 $ per kilogram H2 for a range of 
scenarios based on different electricity sources. In the current case, error bars illustrate high and low LCOH due to a range 
of electrolyzer capital costs; in the future scenarios, error bars illustrate a range of costs based on different assumptions 
about the electricity source (e.g., future grid, wind, solar, nuclear, or hybrid wind and solar). See the Appendix for 
description of assumptions and corresponding cost data.

15 
 
For all electrolyzer types, the grid cases in Figure 4 (with varying degrees of renewable 
penetration, including a range of electricity pricing from $0.06/kilowatt-hour (kWh) to $0.10/kWh, 
and assuming a 97% capacity factor)2 result in the highest LCOH, due in part to the inclusion of 
transmission costs in the electricity prices. The hybrid renewable energy system cases included 
on-site electricity generation using both solar and wind power, assuming costs are reduced to 
$0.012/kWh with tax credits, and an upper-end capacity factor of 74%).3 The cases based on 
only direct coupling with the best available wind resources (with on-site electricity costs ranging 
from $0.017/kWh to $0.023/kWh in 2031, and a high-end capacity factor of 57%) still offer cost 
improvements relative to the grid cases, due to the low electricity generation costs and minimal 
or no transmission costs.4 For reference, current best available wind resources are 
~$0.026/kWh and 51% capacity factor, highlighting the need for continued development of 
renewable energy technologies to enable the Hydrogen Shot goal [11]. 
 
When current technology (see appendix for assumed capital costs) and grid electricity are used, 
the analysis shows that LA electrolyzers have the potential to produce the lowest-cost 
hydrogen—at approximately $5.80/kg, compared with PEM at approximately $6.70/kg and O-
SOEC at approximately $7.60/kg.5 This cost advantage can be attributed to LA electrolyzers’ 
lower capital cost, a consequence of today’s high-volume manufacturing and the relatively 
inexpensive materials used. In future years, PEM and LA capital costs will likely become more 
comparable, as the manufacturing rate of PEM technology continues to grow [3]. Compared 
with both PEM and LA, analysis shows future O-SOEC technology benefiting from higher 
electrical conversion efficiencies in cases where heat integration is available (e.g., at a nuclear 
power plant), helping to reduce the LCOH, in addition to significant reductions from increased 
manufacturing scale [12]. 
 
One key assumption made in this high-level techno-economic analysis is that each electrolyzer 
technology is capable of load-following dynamic power generation in the renewables (wind) and 
hybrid system scenarios. The demonstrated ability for PEM, LA, and O-SOEC electrolyzers to 
load follow in such configurations currently varies among the technology types, with PEM 
demonstrating the ability to load follow based on demonstrations to date [13]. Testing durability 
under dynamic loading in all electrolyzer technologies, as part of broader active research to 
 
2 The current grid scenarios are based on data from the U.S. Energy Information Administration, and the future grid scenarios for 
2026 and 2031 include corresponding levels of renewable penetration based on projections from a DOE study for achieving a 100% 
clean electricity grid by 2035. See the Appendix for further details and references. It should be emphasized that these cases are 
included for reference; they all entail different degrees of grid carbon dioxide (CO2) emissions, and therefore the hydrogen produced 
does not qualify as clean.  
3 The hybrid renewable energy scenarios in 2026 and 2031 are based on a preliminary study of complimentary wind and solar 
resources. These include advanced electrolyzer technologies collocated with both wind and solar resources found in parts of Texas, 
with aggressive reductions in the on-site electricity generation costs, potentially leveraging regional renewable tax credits. Different 
hybrid scenarios studied include the case of equal sizing (100 MW) for each of the three components, as well as the case of an 
electrolyzer capacity of 100 MW that matches the total wind and solar capacity (200 MW). See the Appendix for further details and 
references. 
4 The renewable and hybrid scenarios in this report do not include battery or hydrogen storage as a potential mitigation strategy 
addressing intermittency; more comprehensive analysis of regionally dependent scenarios is ongoing, including cost optimization 
based on various combinations of wind and solar energy with storage. Results will be included in future report updates. 
5 Uninstalled capital cost, system efficiency, and replacement interval are consistent with the range of values in [3], [27], and [35].

16 
 
optimize operating vs. capital costs, will contribute to meeting long-term goals for variable 
renewable energy resources.  
 
It is expected that the future market could be served by a mix of electrolyzer technologies as 
each technology develops further. Specific deployment choices will likely be based on the match 
between an application’s needs, including both end use and clean electricity source, and the 
electrolyzer’s properties, operating capabilities, and cost. While the scenarios in Figure 4 offer 
potential pathways for meeting LCOH cost targets, these scenarios depend on local availability 
of low-cost clean energy resources capable of providing high capacity factors, requiring 
significant electricity cost reductions and will require accelerated levels of technology and 
integrated systems RD&D focused on addressing key cost drivers for electrolyzers. 
 
The factors summarized in Figure 5 drive the cost of electrolytic hydrogen and are covered in 
much greater detail in subsequent sections of this document. Achieving the clean hydrogen cost 
target of $1/kg through electrolysis will require continued RDD&D to:  
 
1. Reduce capital cost, improve efficiency and performance, and increase lifetimes 
through scientific breakthroughs and technology advancements.  
2. Improve manufacturing processes and increase manufacturing throughput to 
reduce manufacturing costs and achieve economies of scale that drive down 
electrolyzer costs.  
3. Optimize integration of electrolyzers with low-cost, clean electricity sources, 
including through direct coupling.  
 
As shown by the large range of LCOH in Figure 4, the cost of clean electricity and the operating 
capacity factor6 of installed electrolyzers will play a large role in the overall cost of clean 
hydrogen production from electrolyzers. The DOE Hydrogen Program continues to explore 
integrated systems that optimize electricity price and capacity factor.  
 
Also of note is that since the Hydrogen Energy Earthshot was launched, supply chain issues, 
higher electrolyzer system installation costs, and inflation have increased costs, making the goal 
of $1/kg H2 more challenging to achieve. 
 
 
6 Capacity factor is defined here as annual average input energy divided by nameplate capacity if operated during all hours of the 
year.

17 
 
 
Figure 5. Key cost drivers for clean hydrogen production using electrolysis. 
 
Figure 6. Waterfall charts illustrating potential pathways to achieve the Hydrogen Shot target for LTE (PEM) and HTE (O-
SOEC). 
 
The waterfall charts in Figure 6 illustrate example pathways to achieve the Hydrogen Shot goal 
for LTE (PEM) and HTE (O-SOEC), respectively. See the appendix for further details, model 
assumptions and references. Similar to Figure 4, the 2026 and 2031 technology cases reflect 
improvements in electrolyzer cost, durability, and performance over the current technology case 
[14]. The first bar in each chart represents estimated LCOH based on today’s electrolyzer 
technology manufactured at low volumes and using average grid electricity pricing based on 
data from the U.S. Energy Information Administration. For both PEM and O-SOEC, the cost

18 
 
reductions needed for achieving the $1/kg-H2 goal require a combination of continued 
electrolyzer technology advances (in performance, durability, and cost), improvements in 
manufacturing technologies and processes, achieving manufacturing economies of scale, and 
optimizing integration with low-cost, clean electricity using regionally specific resources such as 
solar, wind, geothermal, hydropower, and nuclear power.7   
 
The grid cases for both PEM and O-SOEC are included for reference, but these do not qualify 
as clean hydrogen production cases due to the limited amount of clean energy resources in 
today’s grid. DOE-supported studies analyzing scenarios for 100% clean electricity by 2035 
project that clean electricity will cost approximately $60–$80/megawatt hour (MWh) on average 
across the United States, in part due to added transmission costs [15]. Even with optimized 
technology and economies of scale, achieving $1/kg H2 for PEM or O-SOEC electrolysis will 
require electricity costs less than approximately $20–$30/MWh with >90% capacity factor. 
Therefore, except for specific regional opportunities where renewable or nuclear power is sold 
at these low electricity rates and high capacity factors, grid-connected electrolysis will not 
generally achieve the Hydrogen Shot target. Other cases included in Figure 6 leverage the 
lower costs enabled by optimal integration of electrolyzers with diverse renewable and nuclear 
power generation. 
 
Regional opportunities based on collocation and tight integration of electrolysis with renewable 
or nuclear generation—with reduced or eliminated electricity transmission costs—offer potential 
pathways to meeting the Hydrogen Shot goal. The PEM example in Figure 6 illustrates that 
direct coupling with wind energy using today’s technology offers reduced LCOH compared with 
the grid case.8 Still, the cost savings are limited by the capacity factor of the renewable resource 
(around 50% in regions with good wind resources), which results in reduction of electrolyzer 
utilization and need for hydrogen storage to ensure customers are delivered hydrogen when 
needed). In certain regions, hybrid energy systems with optimized integration with both solar 
and wind energy can have increased effective capacity factors (as high as about 75%) that in 
conjunction with technology advances and economies of scale offer a pathway to the Hydrogen 
Shot goal. The O-SOEC example illustrates that this goal can be met with continued technology 
and manufacturing improvements along with direct coupling and thermal integration with the 
current fleet of nuclear power plants where they currently produce electricity with a 95% 
capacity factor [16]. To meet the cost goal, the plants would need to continue to produce 
electricity at levelized costs less than approximately $30/MWh; and a full accounting of both 
direct and indirect emissions will also be needed. Unlike with renewable integration, capacity 
factors can be near 100% in these cases, which is favorable to continuous hydrogen production 
at reduced cost. However, dynamic operation of the electrolyzer may be advantageous to allow 
varying rates of hydrogen production—for example, to ramp down the use of electricity for 
hydrogen production in favor of selling that electricity to the grid at times when market prices are 
favorable. 
 
7 Note that the 2031 technology cases in each chart reflect electrolyzer technology advances projected by 2031 coupled with current 
conceptual designs for integration with renewable or nuclear power, which by themselves approach but do not reach the $1/kg-H2 
target. Attaining the goal will require additional optimization of the integrated energy systems through continued RD&D innovations.  
8 For further details on the projected LCOH of grid- and renewable-connected PEM electrolysis, see [9], noting that results in this 
record are presented in inflated 2022 $ compared to those in this document presented in 2020 $, for reasons described in the 
Introduction.

19 
 
GHG EMISSIONS AND WATER CONSUMPTION 
To assess the decarbonization potential for all electrolyzer technologies, techno-economic 
analysis must be coupled with life cycle analysis to address emissions, water usage, and other 
environmental concerns related to hydrogen production. This section discusses the 
environmental impacts of hydrogen production via electrolysis, using different clean energy 
sources. 
 
The overall GHG emissions associated with hydrogen produced via electrolysis will be 
determined primarily by the electricity source and the upstream emissions that result from 
manufacturing processes. Currently, most analyses of GHG emissions from hydrogen 
production are conducted using a well-to-gate system boundary, which includes emissions 
associated with feedstock gathering, extraction, processing, and delivery to a hydrogen 
production facility (in the case of electrolysis, the feedstock is water, so associated emissions 
are minimal). It also includes the emissions associated with the hydrogen production process, 
inclusive of the electricity used by the hydrogen production facility.9 Notably, this method does 
not consider embodied emissions from the manufacturing of the electrolyzer or the clean energy 
equipment (e.g., solar panels or wind turbines). More detailed life cycle analysis with different 
system boundaries that include embodied emissions is currently underway [17]. The findings of 
this analysis will be included in future versions of this report. A key aim of such analytical efforts 
is to ensure that neither benefits nor penalties are counted twice in the overall carbon footprint 
determination. 
 
When the U.S. average grid mix is used as the electricity source for electrolysis, the direct GHG 
emissions calculated using Argonne National Laboratory’s Greenhouse Gases, Regulated 
Emissions, and Energy use in Technologies (GREET) model are significant, at approximately 24 
kg CO2e/kg H2 (CO2e is carbon dioxide equivalent). In contrast, when using electricity directly 
from nuclear, wind and/or solar, the model calculates near-zero well-to-gate direct GHG 
emissions [18].10 When the GHG emissions from manufacturing of renewable energy systems 
(e.g., solar panels or wind turbines) are included, direct GHG emissions can still be low, as low 
as 1 kg CO2e/kg H2, depending on the specific sources of the manufactured equipment [19].11 
For electrolysis directly coupled with nuclear power, when using a conventional light water 
reactor, GHG emissions related to the uranium supply chain activities, which include mining, 
transportation, and enrichment, can also be modest, at approximately 0.1 kg CO2e/kg H2, 
depending on the electricity needs of the electrolyzer [20]. Producing clean hydrogen via 
electrolysis will clearly rely on the use of clean electricity sources, including a decarbonized grid 
and direct coupling to sources such as solar, wind, and nuclear power. However, all upstream 
emissions sources will need to be accounted for. 
Water consumption requirements for electrolyzers depend on the electrolyzer and electricity 
source. Direct water consumption (the water consumed during electrolyzer operation, not 
including water used for cooling) is about 4 gallons per kilogram of hydrogen depending on the 
 
9 These include direct emissions in the case of direct coupling with a power generation source, as well as indirect emissions 
associated with grid-connected cases; all emissions must be accounted for in a comprehensive life cycle analysis. 
10 This does not account for induced grid emissions. 
11 This does not account for induced grid emissions.

20 
 
electrolyzer type and system size [21]. Additional consumption is required upstream of the point 
of hydrogen production to purify water and produce electricity. Including this upstream water 
consumption yields additional consumption of 3–65 gal H2O/kg H2, and this is highly dependent 
on the electricity source and electrolyzer system. The highest total water consumption occurs 
with geothermal- or nuclear-powered electrolyzers (about 69 gal H2O/kg H2 and 30 gal H2O/kg 
H2, respectively); though in the future, many of the advanced nuclear reactors will have a much 
smaller need for water.12 As little as 7 gal H2O/kg H2 are required for electrolyzers operating on 
solar or wind electricity sources [22].  
  
 
12 Advanced nuclear reactors will have a higher operating temperature, meaning more heat is converted into electricity, and they will 
be able to use dry cooling in areas where water is scarce. Some nuclear plants are also currently used for desalination and treating 
brackish water beyond power plant needs.

21 
 
OVERVIEW OF RD&D NEEDS TO ACHIEVE 
HYDROGEN SHOT GOALS 
Current status and technical targets for PEM, LA, and O-SOEC stacks and systems have been 
developed to guide electrolyzer RD&D efforts toward the Hydrogen Shot goal (Table 2). Status 
and target values were developed in collaboration with national laboratories and industry 
partners and are consistent with ranges reported in the literature (see the Appendix). There are 
many combinations of performance and cost targets (efficiency, lifetime, and capital cost) that 
can achieve $1/kg H2; the ones listed here can be considered a starting guidepost for 
technology developers. The higher-TRL electrolyzers (PEM, LA, and O-SOEC) are targeting to 
meet the interim target of an LCOH of $2/kg by 2026 and the ultimate target of $1/kg H2 by 
2031.13 AEM electrolyzers are aiming to achieve targets similar to PEM, and P-SOEC 
electrolyzers are expected to achieve targets similar to O-SOEC, though timelines for meeting 
cost goals will vary depending on investments. While the lower-TRL technologies may not 
achieve $1/kg H2 by 2031, investments in these technologies may eventually lead to even lower 
hydrogen production costs, as some approaches have advantages over current commercial 
technologies.  
 
13 For a full description of assumptions to reach these LCOHs, see [14].

22 
 
Table 2. Status and DOE Intermediate and Ultimate Technical Targets for Mature LTE and HTE Technologies14 
 
Parameter Units PEM LA O-SOEC 
 Status Interim Targets Ultimate Targets Status Interim Targets Ultimate Targets Status Interim Targets Ultimate Targets 
Stack 
Total 
platinum 
group metal 
(PGM) 
content15  
mg/cm2 3.0 0.5 0.125 - - - - - - 
g/kW 0.8 0.1 0.03 - - - - - - 
Performance A/cm2 @V/cell 2.0 A/cm2 @ 1.9 V 3.0 A/cm2 @ 1.8 V 3.0 A/cm2 @ 1.6 V 0.5 A/cm2 @ 1.9 V 1.0 A/cm2 @ 1.8 V 2.0 A/cm2 @ 1.7 V 0.6 A/cm2 @ 1.28 V 1.2 A/cm2 @ 1.28 V 2.0 A/cm2 @ 1.28 V 
Electrical 
efficiency kWh/kg H2 51 48 43 51 48 45 34 34 34 
Lifetime Operation hours 40,000 80,000 80,000 60,000 80,000 80,000 20,000 40,000 80,000 
Average 
degradation 
rate 
mV/kh 4.8 2.3 2.0 3.2 2.3 2.1 6.4 3.2 1.6 
Capital cost $/kW 450 100 50 250 100 50 300 125 50 
System Energy 
efficiency16 kWh/kg H2 55 51 46 55 52 48 47 44 42 
Uninstalled 
capital cost $/kW 1,000 250 150 500 250 150 2,500 500 200 
 
14 Target table reproduced from [14]. 
15 Total PGM content includes both electrodes combined. 
16 For O-SOEC, energy efficiency includes both electrical and thermal energy inputs.

23 
 
Manufacturing at high volume to achieve economies of scale, lower-cost manufacturing 
processes, and technology advances across the material, cell/stack, and system levels 
(including BOP components) are all critical to meet the targets outlined above. Figure 7 shows 
key aspects of each technology that would benefit from RD&D to address capital cost, durability, 
or efficiency challenges facing current technologies. The remainder of this document describes 
the current status and highlights opportunities for development in electrolyzer manufacturing, 
properties and performance, and integration with clean energy. 
 
 
Figure 7. Overview of R&D strategies that address cost reduction opportunities.

24 
 
MANUFACTURING: STATUS AND COST 
REDUCTION POTENTIAL 
The global manufacturing capacity for all electrolyzer 
technologies was about 10 GW per year in 2023 [23]. 
Projected growth in demand in 2025 and beyond will 
require significant manufacturing expansion, and—by one 
report—expansions could reach 155 GW per year by 2030 
[5]. In 2020, 85% of manufacturing capacity was for LA 
electrolyzers, less than 15% was for PEM electrolyzers, 
and a very small fraction was for O-SOEC and AEM 
electrolyzers. Most electrolyzer manufacturing today occurs 
in Europe and China. While limited electrolyzer manufacturing exists in the United Staes today, 
plans for expansion by several domestic manufacturers are underway [24]. Recently, DOE 
made an investment of more than $300 million in electrolyzer manufacturing RD&D to reduce 
manufacturing costs and enable greater economies of scale through manufacturing innovations, 
including automated manufacturing processes, design for processability and scale-up, quality 
control methods to maintain electrolyzer performance and durability, reduced critical mineral 
loadings, and design for end-of-life recovery and recyclability [25]. 
 
Low-cost and high-throughput manufacturing of electrolyzer components, cells, stacks, and 
systems is key to achieve $1/kg H2 across all electrolyzer technologies. As an example, a 
manufacturing cost curve for an electrolyzer is shown in Figure 8, which highlights the capital 
cost reduction potential through manufacturing at greater than gigawatt-scale volumes using 
currently available methods, and the potential for further cost reduction using advanced high-
throughput methods. These manufacturing economies of scale generally apply to all electrolyzer 
technologies, though the exact cost curves and cost reduction potential differ. 
 
 
Figure 8. Schematic of capital cost as a function of manufacturing production rate using currently available methods 
(solid) and advanced high-throughput methods (dashed). 
 
Scaling up manufacturing of newly developed materials requires either adjusting currently used 
manufacturing processes or designing and implementing new processes. While optimizing 
Manufacturing Throughput 
 
• Automation 
• Increased line speed 
• Quality assurance/quality 
control

25 
 
performance is a key design parameter for advanced materials, other considerations such as 
manufacturing scalability, end-of-life recovery, and use of environmentally friendly processing 
methods are also critical in achieving cost-effective and clean electrolysis.  
 
Economies of scale can be achieved by reducing processing time to increase manufacturing 
rates, but specific approaches to reducing processing time differ for each electrolyzer 
technology given their different materials and cell designs. For PEM electrolyzers, roll-to-roll 
manufacturing is one strategy to facilitate fast manufacturing of catalyst-coated membranes and 
substrates. For LA electrolyzers, development or validation of manufacturing techniques for 
zero-gap and emerging cell designs is crucial for reducing processing times while still meeting 
performance goals. For O-SOEC, reducing the time, temperature, and number of thermal 
processing steps in sintering and interconnect material processing, as well as replacing batch 
with continuous processes, will be essential for achieving faster production rates and therefore 
higher-volume manufacturing and reduced cost.  
 
For all electrolyzer technologies, automating cell/stack assembly and reducing the number of 
manufacturing steps can improve line throughputs and reduce costs. Challenges remain to 
implement quality control mechanisms for high-throughput processes, especially for large cell 
areas used in LTEs. The ongoing and rapidly advancing integration of manufacturing 
technologies and digitization (known as “Industry 4.0” or the “Fourth Industrial Revolution”) has 
the potential to vastly improve manufacturing capability and efficiency [26]. These new 
techniques can involve automating traditional manufacturing processes using any number of 
combinations of tools including robotics, Internet of Things, big data analytics, artificial 
intelligence, and autonomous systems. The primary challenge is to develop the high-throughput 
processes; once they have been established, expanding manufacturing capacity in the United 
States may occur more rapidly.

26 
ELECTROLYZER TECHNOLOGIES: STATUS AND 
COST REDUCTION POTENTIAL 
Achieving electrolyzer manufacturing economies of scale is 
necessary but not sufficient for achieving the goal of 
producing hydrogen for $1/kg—further advances in 
electrolyzer technology will be needed. RDD&D is needed 
to reduce material and equipment capital costs, improve 
efficiency and performance, and extend the lifetime of 
electrolyzer stacks and systems. This section summarizes 
the current status and unique technical challenges facing 
each electrolyzer technology.  
P
EM Electrolyzers 
H
istorically developed for use in underwater vessels 
and spacecraft for oxygen generation and applications 
requiring a small amount of hydrogen (e.g., gas 
chromatographs), PEM electrolyzers are now being 
developed for large-scale hydrogen production. 
Commercial stacks are typically 0.1–2.5 MW and can be 
combined to form multimegawatt (10–100-MW) systems 
[27]. The solid polymer membrane electrolyte allows for 
high-current-density operation with good efficiency that 
enables smaller system footprints compared to LA 
electrolyzers. The membrane also helps mitigate 
hydrogen gas crossover into the oxygen stream and 
allows for generation of hydrogen at differential 
pressure (e.g., 30 bar). The PEM electrolyzer design is 
amenable to fast, dynamic response, making it ideal for 
integrating with variable power sources such as wind 
and solar. The main drawback is the acidic operating 
environment, which limits the materials that can be used 
and currently requires the use of PGM catalysts and 
coatings.  
SYSTEM COST ANALYSIS 
R
ecent analysis has estimated the uninstalled capital cost of PEM electrolyzer systems at 
today’s manufacturing volumes to be $700–$1,100/kW [9] [28].17 At such capital costs, the 
LCOH ranges from $6.00 to $7.20/kg H2 assuming grid electricity and high capacity factors 
(Figure 4). Reducing the capital cost of the electrolyzer system can make a substantial impact 
17 Note that uninstalled capital cost applies a markup to the manufactured system cost. 
Figure 9. Schematic of PEM electrolyzer cell. 
Key Electrolyzer Properties 
• S
ystem lifetime
• System performance and
ef
ficiency
• Material, component, and
equipment costs

27 
 
on the LCOH and can enable these systems to operate at lower capacity factors, a key aspect 
of integrating electrolyzers with low-cost renewable power.  
Capital cost reductions in the near term are expected to be driven by improved processes 
enabling increased manufacturing volumes to achieve economies of scale (as discussed 
above). However, to achieve the $1/kg-H2 target, advanced stacks and systems with improved 
performance, efficiency, and lifetime are needed in addition to reducing capital cost (Table 2).  
 
As shown in Figure 10, for a 1-MW system manufactured at a rate of 1 GW per year, the stack 
constitutes about 30% of the system cost, with the greatest single contributor to the stack cost 
being the oxygen-evolution-reaction (OER) electrode, which includes the iridium catalyst. The 
membrane is another expensive component in the stack. RD&D efforts targeted at these high-
cost components are important to reduce overall capital costs, though those efforts must also 
consider trade-offs with system lifetime and efficiency, parameters that impact operating and 
maintenance costs. Priority RD&D opportunities for PEM electrolyzers are highlighted in Table 3 
and discussed in greater detail below. 
 
 
Figure 10. PEM electrolyzer system and stack cost breakdown assuming a 1-MW stack, 1-MW system, and 1-GW/yr 
manufacturing rate [28]. Note: HER refers to the hydrogen evolution reaction. 
RD&D APPROACHES FOR COST REDUCTION 
 
Materials and Components 
 
PEM electrolyzer technology is proven and has been utilized in niche applications, such as 
submarines, for many years; however, these commercial electrolyzers have been 
overengineered with a focus on reliability over cost and efficiency. This overengineering 
includes the materials and components used in commercial systems today, such as high 
amounts of platinum and iridium catalysts and thick membranes.

28 
 
Table 3. Cost Reduction Opportunities for PEM Electrolyzers 
Cost Reduction 
Opportunity Approaches 
Capital cost 
reduction 
• Reduced precious metal catalyst loading 
• Thinner membranes 
• Manufacturing at scale  
• Direct integration with renewables 
• Standardize BOP, including power electronics. 
Performance and 
efficiency 
improvement 
• Thinner, engineered membranes 
• Engineered interfaces 
• High intrinsic catalyst activity and utilization 
• Optimize porous transport layer (PTL) design for mass transport. 
Longer lifetime 
• Develop accelerated stress tests 
• Optimize membrane/catalyst layer/PTL interfaces 
• Improve and validate durability under dynamic operating conditions. 
 
One of the single most expensive components in the PEM electrolyzer stack is the iridium 
catalyst in the anode catalyst layer. Iridium is an expensive precious metal and suffers from a 
volatile market price, sensitive to disruptions in the supply chain and growing demand. Today’s 
electrolyzers utilize about 2 mgIr/cm2 (or 0.5–0.8 gIr/kW assuming 1.9 V to operate at 2 A/cm2) 
[27] [28]. Current research efforts explore how reducing the iridium loading by roughly an order 
of magnitude impacts the efficiency and durability of the stack. Near-term DOE targets for total 
PGM loading are 0.5 mg/cm2, including both platinum and iridium [14]. Ongoing research is 
examining ways to replace iridium catalysts with transition metal alternatives, but that research 
is further from commercialization [29]. Developing a less expensive anode catalyst layer with 
high performance, durability, and efficiency is a critical area of research to achieve the 
Hydrogen Shot goal.  
 
The membranes in commercial PEM stacks use perfluorinated polymers that are highly stable 
and have high proton conductivity. Such polymers have historically been employed in PEM fuel 
cells and chlor-alkali electrolyzers. However, membranes used in commercial PEM electrolyzer 
stacks today are fabricated thick enough to reduce hydrogen crossover and provide needed 
reliability. Developing novel membranes with properties optimized for electrolyzer operation, 
including reducing the membrane thickness by a factor of 3–4, will significantly improve the 
stack efficiency (by reducing resistive loss through the membrane) and decrease cost (by using 
less material). Membranes may need to be engineered to include gas recombination catalysts 
or reinforcement to achieve efficiency and durability targets. Furthermore, due to environmental 
concerns about “forever chemicals,” government and industry are investing in research to 
reduce or eliminate the use of perfluorinated polymers in membranes. This research focuses on 
the development of suitable hydrocarbon membranes that will provide the needed reliability in a 
commercial electrolyzer. 
 
PTLs influence stack performance and durability due to their mass transport properties and 
electrical resistance in PEM electrolyzer cells. PTL architectures need to be fully optimized for 
electrolyzers. In addition, current PTLs made of titanium require precious metal coatings at

29 
 
interfaces to prevent titanium oxidation, which leads to increased resistance and decreased 
efficiency. Significant cost reductions can be achieved by reducing material cost (without 
sacrificing performance, durability, or efficiency) and optimizing the PTL structure.  
 
Cells and Stacks 
 
As precious metal catalyst loadings are reduced, in order to maintain high performance and 
durability, it will be essential to have an optimally efficient and durable interface between the 
electrode structure and both the PTL and membrane.  
 
A major unknown inhibiting the commercialization of next-generation electrolyzer technology is 
whether advanced materials and components can provide the lifetimes required to meet the 
technical targets in Table 2. This question is especially important when considering the dynamic 
operating and start/stop conditions arising from the coupling of an electrolyzer to renewable 
energy sources. The effect of turning the electrolyzer system on and off repeatedly over time 
also has not been adequately studied for its impact on stack durability. Realistically, lifetime 
testing for 5 years to prove durability is not feasible and would significantly delay the 
introduction of new materials and technologies. Hence, an improved understanding of 
electrolyzer degradation mechanisms can be used to project anticipated lifetime and develop 
stress tests that accelerate these degradation processes, allowing durability testing to be 
completed in a matter of weeks or months instead of years.  
 
Systems 
 
BOP components represent a significant portion of overall system capital costs, especially as 
the cost of stacks comes down as stack manufacturing volumes increase and benefit from 
economies of scale. The BOP includes power electronics, heaters, pumps, and gas processing 
units. Of the BOP components, electrolyzer manufacturers have indicated that there is 
significant opportunity to reduce the cost of power electronics [30]. For example, standardized 
modular units reduce the need for custom designs and take advantage of economies of scale. 
This concept of standardization could apply to other BOP components as well. Modularizing the 
BOP or increasing the manufacturing capacity of BOP components may also lead to cost 
reductions.  
 
In order to fully realize the potential for PEM electrolyzers to produce low-cost, clean hydrogen, 
it will be critical to improve their integration with variable renewable energy sources. PEM 
electrolyzers can quickly respond to changes in load, making them well suited to operate on 
variable or intermitted power [31]. However, there is a need for more demonstrations of PEM 
electrolyzers directly coupled to renewable energy sources (i.e., with minimal power conversion 
steps from the renewable energy source to the electrolyzer, without a grid interconnection). 
Additional demonstrations will improve our understanding of the electrical BOP equipment 
needs, operating strategies, and stack durability requirements.

30 
 
LA Electrolyzers 
 
LA electrolyzers are the most mature electrolyzer 
technology today in terms of commercial 
availability and deployed capacity. Historically, the 
development of LA electrolyzer technology was 
driven by hydrogen demand for ammonia 
production in regions with low-cost hydroelectric 
power. Given the relatively steady availability of 
hydroelectricity, these systems were designed to 
operate on multimegawatt power continuously at 
steady state. Typical stack unit sizes range from 
0.5 to 5 MW, and these can be combined into 
larger systems, with some current system 
installations greater than 100 MW [27] [32]. Today, 
LA electrolyzers are being deployed to produce 
hydrogen for a wider range of applications, 
including mobility and power generation. Still, the 
relatively large footprint and continuous operating 
needs of these conventionally designed systems 
remain issues that can be improved [33]. 
 
Traditional LA electrolyzers are designed to circulate concentrated alkaline electrolytes (e.g., 7-
M KOH) instead of water to conduct ions between electrodes made primarily of nickel. A 
separator material, which is permeable to the electrolyte, mitigates hydrogen and oxygen 
crossover between the anode and cathode compartments, and the gaseous products are 
produced at near-atmospheric pressures. Historically, relatively large gaps between the 
electrodes resulted in a large ohmic resistance, and therefore it was economical to operate at 
low current density because it avoided high voltages, and hence low efficiencies. Zero-gap cells 
have been designed to address this issue by minimizing the distance between electrodes, but 
further improvements are still possible. Additionally, LA electrolyzer designs generally have not 
been amenable to dynamic operation (e.g., load-following solar or wind power) because they 
are vulnerable to both mechanical and chemical degradation under such variable operating 
conditions, and dynamic operation while using a hydrogen compressor is challenging. Despite 
limitations in current density and operating conditions, the alkaline operating environment allows 
for the use of low-cost materials such as stainless steel and non-precious-metal catalysts. As a 
result, while capital costs of LA electrolyzers are lower than their PEM counterparts, they are 
less efficient at higher current densities, so efficiency suffers at higher rates of hydrogen 
production. 
 
SYSTEM COST ANALYSIS 
 
The capital cost of LA electrolyzer systems varies significantly depending on the manufacturer, 
ranging from $500/kW to more than $1,500/kW uninstalled cost, although most costs are in the 
$500–$750/kW range [3] [34] [35]. Such a low capital cost results in a low LCOH today using 
grid electricity ($5.00–$5.50/kg H2, Figure 4). A recent design for manufacturing and assembly 
 
Figure 11. Schematic of an LA electrolyzer cell.

31 
 
cost analysis of a 4-MW stack and 50-MW BOP module was conducted to determine how each 
component contributed to the overall cost of the stack and system (assuming a 1-GW/yr 
manufacturing rate and current electrolyzer design, Figure 12) [34]. The cost breakdown of the 
stack reveals that bipolar plates and cell frames are the largest contributors to stack capital 
costs. This result is consistent with the fact that catalyst materials in LA stacks are less costly 
than those in PEM stacks. Additionally, this analysis revealed that the BOP accounts for about 
52% of the overall system capital cost, of which power electronics (“Electrical BOP” in Figure 
12) are the most expensive element.  
 
 
Figure 12. LA electrolyzer system (left) and stack (right) cost breakdown assuming a 1-GW/yr manufacturing rate, 4-MW 
stack, and 50-MW BOP module [34]. 
 
The system cost breakdown provides valuable insights for strategies to reduce capital costs. 
However, it is important to note that the high manufacturing capacities in place today for mature 
LA technologies result in a low system capital cost compared with other electrolyzer 
technologies [5]. 
 
RD&D APPROACHES FOR COST REDUCTION 
 
As a result of the relatively low system capital cost, improving system performance and 
efficiency while maintaining durability can drive significant cost reductions and progress toward 
the $1/kg goal. In addition, enabling variable and intermittent operation may be a significant 
driver of hydrogen cost reduction to enable LA electrolyzers to access low-cost electricity. 
These performance improvements will require RD&D of materials; interfaces; cell, stack, and 
system designs; and fabrication techniques. Specific RD&D needs and priorities are described 
further below and summarized in Table 4.

32 
 
Table 4. Cost Reduction Opportunities in LA 
Cost Reduction 
Opportunity Approaches 
Capital cost reduction 
• Novel components (e.g., separators) and cell/stack designs for high -
current-density operation while maintaining efficiency.  
• Standardized BOP, including power electronics. 
• Manufacturing-advanced multimegawatt systems at scale. 
Performance and 
efficiency improvement 
• Engineered interfaces with high catalyst utilization. 
• Novel separator materials and catalysts. 
• Improved component integration strategies. 
• Bubble management. 
• Novel cell/stack design. 
Longer lifetime 
• Novel materials. 
• C ell designs. 
• Dynamic operation considerations. 
 
Materials and Components 
 
Discussion at a recent experts’ meeting on advanced LA electrolyzers revealed that separator 
materials and catalysts have received little attention in recent decades [36]. Innovation in 
separator materials is necessary to reach higher current densities at lower voltages, which can 
drive down the capital cost (on a dollar-per-kilowatt or dollar-per-kilogram basis) and reduce 
operating costs via more efficient electrical operation. Ideal separator materials must be 
mechanically and chemically stable and tested at commercially relevant temperatures and 
pressures. While thinner separators can reduce resistance, and hence improve efficiency, 
mechanical stability can become a challenge, especially if operating the cell at elevated 
pressure. A balance is required between these two factors. 
 
Electrodes in commercial LA cells commonly consist of a nickel catalyst coated onto a low-
surface-area substrate (e.g., nickel-coated steel). The result is an extremely durable electrode 
but with relatively low performance. To achieve higher performance/efficiency, there remains a 
need for catalysts with higher intrinsic activity and for electrode structures with high surface area 
and catalyst utilization that are amenable to cell integration. To that end, understanding the 
relationship between structure, activity, and stability—and how different manufacturing 
processes affect structure—could lead to performance and efficiency improvements. Dynamic 
operation and advanced cell designs are also important considerations when developing 
catalysts and electrodes for next-generation LA electrolyzer technology.  
 
Cells and Stacks 
 
Next-generation LA electrolyzer cells will likely have a different architecture than traditional LA 
electrolyzer cells. Already, developments in cell design have included “zero-gap” architectures 
that improve performance by minimizing the distance between the electrodes and the separator. 
A high-priority focus area is on developing advanced cells that demonstrate chemical and 
mechanical stability under variable operation with high efficiency. Such designs must overcome

33 
 
numerous challenges, particularly during operational periods at low current density. Such 
challenges include minimizing shunt currents and managing electrolyte levels. Additional 
opportunities for improvement include cells that can operate at higher pressures, which can help 
reduce downstream compression costs for hydrogen, and novel components that can withstand 
operating pressures near 30 bar. 
 
Innovation in interface engineering and the integration of components into electrodes and cells 
could lead to improved efficiency, improved durability, and reduced cost. Interfaces and cell 
integration will become more critical with advanced cell designs. Leveraging PEM electrode 
developments, such as coating catalysts onto the separator material, could help achieve 
improved interfaces and higher manufacturing throughput. However, to design for improved 
performance, efficiency, and durability, additional research is needed to understand the 
interfaces in LA electrolyzer cells, which could include characterizing bubble and current 
distribution within the cell. As the dimensions of the cell increase from lab scale to commercial 
scale, it is also critical to characterize next-generation cells and stacks to determine degradation 
mechanisms. 
 
Commercial LA cells and stacks have a very long lifetime; however, the impact of advanced 
materials, new cell and stack designs, and dynamic operating conditions on durability are 
unknown. Similar to PEM electrolyzers, developing accelerated stress tests to understand 
degradation mechanisms and determine lifetime in a much shorter time frame is important to 
expedite commercialization of next-generation technology.  
 
Systems 
 
Similar to PEM electrolyzers, the BOP equipment represents a significant fraction of the overall 
system capital cost for LA electrolyzers (Figure 12), and the cost of power electronics are the 
dominant factor in BOP costs. Reducing the capital cost of the BOP equipment could include 
approaches such as process intensification and modularizing and standardizing components. 
For LA electrolyzers, reducing the need for BOP equipment for electrolyte management, such 
as eliminating the potassium hydroxide scrubber through innovative cell designs, could also 
reduce capital costs. 
 
Systems for advanced LA electrolyzers could also be designed for dynamic operation. In 
traditional LA electrolyzers, rapid changes in current density and gas production create 
challenges for differential pressure control and electrolyte level control systems that can lead to 
safety hazards. Mitigating shunt currents in the system also becomes increasingly important 
when operating at low current densities. Innovative system designs that can overcome these 
challenges can result in more durable LA electrolyzers when coupled to variable clean energy 
sources.

34 
 
O-SOECs 
 
O-SOECs operate at high temperatures, and they 
exhibit a higher electrical efficiency compared with 
LTEs. However, their shorter lifetimes and higher 
capital costs have hindered market entry and kept 
manufacturing volumes low. Their high-temperature 
operation (700°C–850°C) enables higher electrical 
efficiencies due to the improved kinetics of splitting 
water at higher temperatures. However, the high 
temperatures are also a major driver of lower cell 
durability and shorter stack lifetime. Thermal 
integration with a range of heat sources, including 
nuclear reactors and other industrial processes (e.g., 
steel production), can provide efficiency and cost 
benefits.  
 
O-SOECs have benefitted from decades of R&D of 
solid-oxide fuel cells (SOFCs), which have more 
extensive commercial deployment worldwide. The 
technology is based on a solid ceramic electrolyte 
that conducts oxide ions at high temperatures. Many of the cell and stack components 
developed for SOFCs—including the metal interconnects and seals—can be leveraged for O-
SOEC development. Additionally, given the similarities between SOFC and O-SOEC stacks, 
solid-oxide technologies have the potential to run as “reversible fuel cells”—to either generate 
electricity using hydrogen or generate hydrogen using electricity, with the same stack. This 
feature could make them an attractive technology for long-duration energy storage. O-SOECs 
have a lower TRL compared with PEM and LA electrolyzers, but early demonstrations (1–5-MW 
systems) have begun in the United States [33].  
 
SYSTEM COST ANALYSIS 
 
There are far fewer publicly available data on the current cost of O-SOEC electrolyzers than for 
LTE technologies, which may be due to their lower levels of deployment. Leaders in O-SOEC 
technology development and evaluation at Idaho National Laboratory estimate their current 
uninstalled capital cost to be $2,000–$2,500/kW (2020 $). Under this assumption, current O-
SOEC technology can produce hydrogen at a cost of $7.00–$8.00/kg using grid electricity and 
natural gas for heat (Figure 4). The natural gas for heat scenario was used to estimate current 
costs, as this is most representative of the current status. O-SOECs have high operating 
temperatures that require higher-grade heat, which can be provided from either a natural gas 
boiler or waste heat from a nuclear power plant or other high-temperature systems [12]. 
 
Recent design for manufacturing and assembly analyses have found that the capital cost of 
about $950/kW for O-SOEC systems could be achievable when stacks and systems are 
manufactured at the gigawatt scale with today’s technology [37]. This finding is significantly 
lower than today’s observed uninstalled cost ($2,000–2,500/kW) due to the specific scenario 
 
Figure 13. Schematic of an O-SOEC.

35 
 
studied: 1-GW/year stack manufacturing is considerably higher than most commercial 
production volumes today, and the 1-GW system size is much larger than typical system sizes 
available today, which are generally less than 1 MW [5]. Nonetheless, the design for 
manufacturing and assembly results provides useful information about the costs of equipment 
and components of the stacks and systems.  
 
The cost breakdown shown in Figure 14 is based on a 1-GW system (sized to match a single 
nuclear reactor) with 50-kW stacks produced at a manufacturing rate of 1 GW/year. The BOP 
represents about 85% of the overall system capital cost, while the stack represents only about 
15%. At a lower stack manufacturing rate (50 MW/year), the stack contribution is higher, about 
25% of the overall system cost [37]. Of the stack components, interconnect (bipolar plate) 
materials and supporting stack infrastructure (end plates) are the biggest contributors to overall 
cost. 
 
  
Figure 14. O-SOEC stack and system cost breakdown based on a 1-GW system and a 50-kW stack, with a manufacturing 
rate of 1 GW/year [12]. 
 
RD&D APPROACHES FOR COST REDUCTION 
 
Key cost reduction pathways include extending the lifetime of O-SOEC cells and stacks, 
developing a robust supply chain for BOP components, and decreasing stack and BOP capital 
costs. Achieving economies of scale in O-SOEC stack and system manufacturing will also be 
critical to meeting the capital cost target (Table 2). Here, we describe specific opportunities at 
the component, cell, and system levels.

36 
 
Table 5. O-SOEC Cost Reduction Opportunities 
Cost Reduction 
Opportunity Approaches 
Capital cost 
reduction 
• Develop low-cost interconnect materials and fabrication processes. 
• Enable lower-temperature operation to reduce thermal management costs. 
• Standardize BOP, including power electronics and heat recuperators. 
• System design and optimization for low capital costs. 
• Develop high-throughput manufacturing techniques. 
Performance and 
efficiency 
improvement 
• Decrease cell resistance. 
• Improve material contact. 
• Improve thermal integration. 
• Enable dynamic operation to access low-cost electricity scenarios. 
Longer lifetime 
• Reduce operating temperature. 
• Reduce electrode contamination and degradation. 
• Reduce degradation of interconnects. 
• Improve material stability with temperature cycling. 
• Develop accelerated stress tests to identify additional opportunities to 
improve lifetimes. 
 
Materials and Components 
 
Degradation of cells and stacks is a key reason for the shorter lifetimes of O-SOECs compared 
with the lifetimes of PEM and LA electrolyzers. Degradation generally would be reduced if lower 
operating temperatures were possible without affecting overall performance. Higher 
temperatures lead to accelerated degradation of interfaces in the cells, which can result in 
reduced performance of electrodes and/or electrolyte. Another source of degradation is the 
presence of impurities, which can come from glass seals and the inlet gas stream [38]. This 
process is also accelerated at higher temperatures. These impurities block active sites on both 
electrodes. Developing novel seal materials with less volatile components and scrubbing the 
inlet stream of impurities would help mitigate this source of degradation. 
 
In the hydrogen electrode, nickel depletion from the electrode-electrolyte interface and migration 
to the support layer is another source of degradation. The reason for this migration is unclear 
and requires further research. The oxygen electrode is a perovskite material, typically 
lanthanum strontium ferrite cobaltite (LSFC), and other perovskite oxides are being investigated 
as well. This high-performing electrode can suffer from degradation when directly in contact with 
the yttria-stabilized zirconia electrolyte. To mitigate oxygen electrode degradation, a barrier 
layer of gadolinium-doped ceria is commonly placed between the electrolyte and the electrode. 
Improvements to the oxygen electrode include focusing on controlling the LSFC oxidation state, 
particularly at the interface. 
 
Lastly, there is some evidence that high oxygen pressure within the electrolyte itself can result 
in crack formation between the electrolyte and the oxygen electrode, which can also reduce life

37 
 
spans. The cause of the high oxygen pressures is not well understood, but improvements to the 
performance of the oxygen electrode may reduce this issue. 
 
Cells and Stacks  
 
Metal interconnects complete the cell circuit and keep adjacent cells in the stack separate from 
each other. Most research on metal interconnects has been performed on SOFCs, but it is 
expected that the issues related to the interconnect are applicable to O-SOECs as well. High-
chromium-containing alloys are a common interconnect material, and they benefit from the 
formation of chromium oxides, which prevent breakaway oxidation while remaining electrically 
conductive. However, they are also prone to chromium volatilization, which causes 
contamination that reduces the stack’s durability. Degradation also occurs due to oxidative and 
reductive gas exposure at high temperature. The addition of protective coatings for the 
interconnects is being investigated, particularly for the oxygen electrode side. 
 
Silica glasses are a common seal material used in O-SOEC stacks. As described above, the 
seals are a potential source of contamination that contribute to stack degradation. These seals 
are a carryover from SOFC stacks, which suggests that there may be opportunities to reduce 
degradation by using seals optimized for O-SOEC operation, including under high steam 
concentration. The seals also contribute to limitations in the thermal cycling of these high-
temperature stacks. Therefore, a low-cost, easily processable seal material that can withstand 
many thermal cycles would be advantageous. 
 
As in the case of next-generation PEM electrolyzers that use new, low-cost materials, 
commercialization of O-SOEC technology will be hindered by the need to demonstrate improved 
lifetimes (e.g., 5 years). It will be important to complete lifetime testing in weeks or months 
instead of years. Hence, one of the biggest needs for O-SOEC technology development is to 
greatly improve the understanding of electrolyzer degradation mechanisms, which may require 
development of stress tests that effectively accelerate relevant degradation processes.  
 
Systems 
 
Thermal cycling during startup and shutdown periods exacerbates degradation, leading to 
shorter lifetimes. Changes in temperature expand and contract all stack components. If the 
thermal and chemical expansion of the various components are not adequately matched, the 
ceramic cells can fracture, resulting in stack failure. O-SOEC stacks can rapidly respond to 
changing loads; however, the impact on lifetime is unknown, and the ability for the overall 
system to respond rapidly needs to be further investigated. Larger system demonstrations can 
help to understand the ability of the overall system to respond to load cycling, as well as the 
impact of load cycling on system lifetimes. 
 
The high operating temperatures of O-SOECs enables extremely efficient use of electricity to 
produce hydrogen, and this efficiency can be further improved through integration with an 
external heat source. Designing systems that are well thermally integrated with heat sources is 
important to maximize the overall efficiency for hydrogen production and make the most of the 
available external heat source. Demonstration of O-SOEC systems that are highly integrated

38 
 
with external heat sources (e.g., heat from nuclear reactors, process heat from manufacturing) 
is key to maximizing the high electrical efficiency advantages of O-SOECs.  
BOP components represent a significant fraction of capital costs for O-SOECs, and this 
contribution to overall cost is expected to grow as stack costs come down through economies of 
scale. The BOP includes power electronics, steam generators, high-temperature heat 
exchangers, pressure vessels, pumps, and water and gas processing units. Of these 
components, power electronics are the most expensive. As with other electrolyzer types, 
developing a standard off-the-shelf modular unit is one approach to reduce the cost of power 
electronics. For power electronics or other BOP components, applying principles of process 
intensification to reduce the number of components may also lead to overall cost reductions. In 
addition, the stack operating temperature directly impacts the cost of the BOP. Based on current 
standards, at temperatures above about 650°C, more expensive nickel-based steel alloys are 
needed for some of the heat exchangers and piping in an O-SOEC, while lower temperatures 
would allow for the use of less expensive metals. Additional research on non-nickel-based 
materials for high-temperature operation may reduce the cost of the BOP without sacrificing 
thermal efficiency.  
 
AEM Electrolyzers 
 
AEM electrolyzers are a promising, lower-TRL 
hydrogen production technology. AEM electrolyzers 
operate at low temperature and use a solid polymer 
membrane to transport hydroxide ions between 
electrodes (Figure 15). The AEM electrolyzer design 
aims to combine the advantages of both PEM and 
LA electrolyzers: the alkaline environment enables 
the use of non-precious-metal catalysts and less 
expensive metal bipolar plates, and the membrane 
enables differential pressure operation and operation 
at higher current densities than traditional LA 
electrolyzers. Due to the inherent alkalinity in the 
membrane, pure water can be fed to the electrolyzer 
instead of alkaline electrolyte, although current 
technology performs better and has higher durability 
with an alkaline electrolyte feed. Research efforts are 
underway to optimize the electrolyte feed 
configuration and other components for high 
efficiency and durability.  
 
STATUS AND R&D COST REDUCTION APPROACHES 
 
A more thorough techno-economic analysis is ongoing to estimate the potential manufactured 
system cost of AEM electrolyzers produced at scale. Although they are still at low TRL and not 
produced commercially today, preliminary results suggest that AEM stacks may cost about 
$200/kW when manufactured at relatively low production volumes (about 20 MW/year) and 
ultimately have the potential to be even less expensive once higher manufacturing volumes 
  
Figure 15. Schematic of AEM electrolyzer cell.

39 
 
(about 300 MW/year) are achieved [39]. This potential for low capital cost is mainly due to lower 
material costs in AEM stack designs (e.g., using non-precious-metal catalysts like stainless 
steel and inexpensive membranes). 
 
The potential of this technology has been demonstrated, but to compete with existing 
technologies, AEM electrolyzers still require significant development to improve stability and 
performance while maintaining their low cost. AEM electrolyzers could ultimately achieve 
system costs lower than what is projected for PEM electrolyzers due to the lower material costs, 
assuming similar efficiency and durability targets can be met. The commercial development of 
AEM electrolyzers will likely benefit from the system design (including BOP) and high-
throughput manufacturing techniques developed for PEM electrolyzers, capitalizing on cost 
reductions achieved in processes and equipment that are common to both electrolyzer types.  
 
A summary of priority R&D areas for AEM electrolyzers is included in Table 6, with more 
detailed descriptions provided below.  
 
Table 6. Priority R&D Opportunities for AEM 
Technology Area Priority R&D Opportunities 
Materials and components 
• Durable membranes and ionomers with high conductivity. 
• PGM-free electrodes with high catalyst activity, utilization, and 
durability. 
Cells and stacks 
• Understanding the role of supporting electrolyte and degradation. 
• Opportunities to eliminate electrolyte. 
• Component integration strategies. 
 
Materials and Components 
 
R&D of chemically and thermally stable membranes and ionomers with high ionic conductivity 
could enable the longer stack lifetimes required for deployment of reliable AEM electrolyzers. 
Ionomers are the polymeric backbone of the membrane and serve as the catalyst binder in the 
electrode. The ionomer provides the ion-conducting properties both as electrolyte for the cell 
and as ion transport to and from the active catalyst sites. These materials can degrade in both 
the membrane and the catalyst layer (e.g., via oxidation reactions) and reduce the lifetime of the 
cell. Key design parameters for alkaline exchange ionomers and membranes include fast 
hydroxide ion transport, low chemical degradation rates, and thermal stability. More research is 
needed to understand the impacts of the electrolyte on membrane and ionomer stability. 
 
Improvements in cell and stack efficiency can be achieved through enhanced catalyst activity, 
greater catalyst utilization, and optimized electrolyte conditions. The catalytic needs for AEM 
electrolyzers are similar to those of LA electrolyzers. There are several PGM-free materials 
currently being researched to serve as the hydrogen and oxygen catalysts [40]. As with LA 
electrolyzers, nickel or nickel alloys are common catalyst materials, but other catalyst classes 
are being investigated as well. There has been limited testing of PGM-free catalysts in full cell 
configurations. Incorporating the catalyst into an electrode structure that also contains an

40 
 
ionomer has been challenging due to catalyst delamination and/or ionomer loss. Understanding 
the durability of electrodes as a function of ionomer, catalysts, the ionomer/catalyst interface, 
and supporting electrolyte is a significant challenge that requires additional research to improve 
AEM electrolyzer durability and performance.  
 
Cells and Stacks 
 
One potential advantage of AEM electrolyzers compared with LA electrolyzers is the use of pure 
water electrolyte instead of concentrated alkaline electrolyte. However, performance and 
durability can be significantly improved when a low concentration of supporting electrolyte (e.g., 
<0.5-M KOH or Na2CO3) is added to the water feed. A better fundamental understanding of the 
impact of supporting electrolyte on AEM cell, component, and material performance and 
durability is needed to determine if this performance and durability gap between pure water and 
supporting electrolyte operation can be closed. Following such studies, the trade-offs between 
performance (i.e., efficiency and durability) and cost (i.e., feedstock and maintenance) can be 
better quantified. Ultimately, the decision on whether to feed pure water or a low-concentration 
electrolyte to the electrolyzer will be based on overall economics across the lifetime of the 
electrolyzer. 
 
To achieve commercial viability, AEM electrolyzers will need carefully optimized improvements 
in membrane electrode assembly fabrication. A catalyst-coated membrane technique, similar to 
that used in PEM electrolyzers, is one approach for fabrication. However, there are a host of 
issues in applying this method to AEM electrolyzers. The hot-pressing technique used in PEM 
electrode design cannot be used for current AEM electrolyzer materials because it can damage 
the membrane and/or electrodes. Catalyst-coated, membrane-based cells can suffer from 
delamination of the catalyst layer, membrane degradation, ionomer degradation, drying of the 
membrane due to gas phase evolution, and loss of electrical contact with current collectors. 
Improved interface engineering between the membrane and catalyst layers, as well as 
optimization of the electrode structure and components, could alleviate these issues.

41 
 
 
P-SOECs 
 
P-SOECs are being developed as a lower-
temperature (450 Celsius [°C]–650°C) alternative to 
O-SOECs. The combination of lower operating 
temperatures and proton conduction provide cost 
advantages over O-SOECs. Lower temperatures are 
made possible by the lower activation energy of 
proton-conducting ceramic electrolytes compared 
with oxide-ion-conducting electrolytes. P-SOECs also 
have the potential for high efficiencies, similar to O-
SOECs. However, significant advances are needed to 
move this low-TRL technology from the R&D phase to 
commercial readiness.  
 
STATUS AND R&D COST REDUCTION 
APPROACHES 
 
Preliminary results indicate the costs associated with P-SOEC stacks can be similar to those of 
O-SOECs, given their similar cell design and energy efficiency [39]. P-SOECs have the potential 
for lower capital costs than their O-SOEC counterparts because their lower operating 
temperature enables the use of less expensive metals in both the stack and BOP. Additionally, 
P-SOECs can directly produce dry hydrogen, removing the need for an additional hydrogen-
drying system and providing opportunities to pressurize within the stack. Pressurizing within the 
stack can simplify the system design and reduce the overall cost of operation. The main barriers 
to commercial development of P-SOECs are the challenge of achieving both the needed 
material strength and high protonic conductivity (which are inversely related), and, similar to O-
SOECs, the high cost of thermal treatment to make dense electrolyte powders. Additional R&D 
will be needed in these areas to produce stable, efficient P-SOECs at low cost. 
 
Given the relatively low TRL and lack of commercial P-SOECs today, this technology may not 
be manufactured at a large enough scale to significantly contribute to commercial production of 
hydrogen that meets the Hydrogen Shot target by 2031. However, if P-SOECs can meet similar 
performance, efficiency, and durability targets as O-SOECs (Table 2), it is anticipated that P-
SOECs could ultimately achieve system costs lower than what is projected for O-SOECs. This 
is largely due to lower material costs (e.g., the potential to use conventional stainless steels 
instead of costly nickel-based superalloys or ceramic components) and simplified BOP. P-
SOECs will also benefit from the development, manufacturing, and commercialization of O-
SOECs due to similarities in system design, cell design, and some materials. A summary of 
priority areas for R&D of P-SOEC electrolyzers is shown in Table 7, with more detailed 
descriptions provided below. 
 
 
Figure 16. Schematic of a P-SOEC.

42 
 
Table 7. P-SOEC Priority RD&D 
Technology 
Area R&D Opportunities 
Materials and 
components 
• Stable, efficient, mechanically robust electrolyte 
capable of scale-up. 
• Improved oxygen electrode. 
Cells and 
stacks 
• Development of lower-cost metal interconnects. 
• Novel engineering solutions and fabrication methods. 
 
Materials and Components 
 
Electrolytes for P-SOECs must have high proton conductivity, low electronic conductivity, and 
sufficient mechanical properties and stability to withstand high-humidity atmospheres with either 
strong reducing or oxidizing effects. The leading candidates for these electrolytes are doped 
BaZrO3 and BaZr1-xCexO3 perovskite oxides. The former is relatively stable in steam 
environments; however, it has a relatively low proton conductivity and can suffer from poor 
sinterability and mechanical properties. The latter is an improvement on the BaZrO3-based 
material for sinterability and improved protonic conductivity but has limited stability in a high 
steam environment. Also, under some operating conditions relevant to P-SOEC electrolyzer 
operation (steam concentration, current density/voltage, and temperature), these materials, 
especially those with ceria, exhibit significant electronic conduction through the electrolyte, 
resulting in a decrease in cell and stack electrical efficiency. Additionally, these materials are not 
as mechanically strong as O-SOEC electrolytes. Materials R&D is needed to find the required 
combination of electrical, mechanical, and chemical properties to arrive at an electrolyte 
material that displays high performance, high efficiency, and long lifetime under the range of 
electrolyzer operating conditions of interest (e.g., less than 600°C, high steam concentration).  
 
Cells and Stacks 
 
Another approach to overcoming the challenges with the proton-conducting electrolyte is to 
engineer around the materials-based limitations. Possible approaches include depositing a very 
thin layer of a different compatible proton-conducting electrolyte on the BaZr1-xCexO3 electrolyte 
that is stable in steam, adding a sintering aid to decrease the sintering temperature of BaZrO3, 
and engineering the interfaces to improve electrochemical performance and durability. Also, 
new fabrication techniques that facilitate the manufacture of larger cells are needed to 
overcome the poor mechanical properties of some of these materials. 
 
As with O-SOECs, chromium poisoning from the metal interconnects is a concern, even at 
reduced temperatures. It is expected that the poisoning of the electrolyte and oxygen electrode 
with chromium species would reduce the lifetime of P-SOECs, perhaps even more significantly 
than in O-SOECs, due to the higher volatility of chromium species in the “wet” oxidizing 
environments unique to P-SOECs. However, few studies have investigated the effect of 
chromium on P-SOECs. Lower-cost metallic interconnects could also be an option to 
significantly reduce costs, but more research needs to be done to understand the corrosion and 
oxidation behavior in typical P-SOEC operating conditions and how this might affect lower-cost 
metals.

43 
 
ENERGY SYSTEM INTEGRATION: STATUS AND 
COST REDUCTION POTENTIAL 
To produce clean hydrogen, electrolyzers must be able to 
use electricity generated from renewable or nuclear energy 
sources. As the grid is decarbonized with renewable and 
nuclear energy, electrolyzers could tie directly to the grid to 
produce clean hydrogen. However, electricity price 
forecasts for a decarbonized grid are significantly higher 
than what is needed for electrolyzers to achieve the 
Hydrogen Shot [15]. While it may not be possible to 
achieve the Hydrogen Shot using electricity purchased 
from the grid, there may be economically viable 
opportunities for electrolyzers to use grid electricity. For example, renewable electricity that 
would otherwise be curtailed can be used to produce hydrogen for long-duration energy 
storage, thereby providing additional revenue to renewable generators and increasing the value 
of renewable electricity sources to the grid [41]. 
 
In addition to helping to meet the Hydrogen Shot goal, tying electrolyzers directly to renewable 
energy sources can also provide other advantages. For example, electrolyzers can be coupled 
to wind farms awaiting grid interconnection (which can involve delays of months or years) to 
start utilizing the available clean electricity immediately and avoid the costs associated with 
unused capital-intensive assets. The direct coupling of power from wind turbines or solar panels 
to electrolyzers can also eliminate some electrical BOP equipment, reducing the overall system 
cost.  
 
However, there are challenges that must be overcome to realize the full benefits of directly 
coupled electrolyzers. For example, an electrolyzer directly coupled to a variable renewable 
power source is likely to have a limited capacity factor, determined by the availability of 
renewable energy. Low capacity factors will drive up the cost of hydrogen, even more so with 
electrolyzers that have high capital cost. In addition, more research is needed to understand 
and quantify the impact of variable power load profiles on electrolyzer performance and lifetime. 
This is an active area of research supported by the DOE Hydrogen Program [42]. Potential 
solutions to these challenges could include: 
• Hybrid energy systems with multiple clean energy sources and backup energy 
storage systems can increase the electrolyzer’s capacity factor. In addition, there are 
opportunities for more complex, fully integrated hybrid systems to produce lower-cost 
hydrogen. For example, nuclear-renewable-hydrogen hybrid systems can provide grid 
services and coproduce low-cost, clean hydrogen (which can be used directly as a fuel 
or as a feedstock in the production of e-fuels) [43]. System-level decisions, such as the 
inclusion of load-leveling batteries, can also influence electrolyzer operation 
requirements (e.g., ramp rate, minimum turndown) that ultimately impact electrolyzer 
durability and replacement costs. Holistic system techno-economic analyses are 
important in quantifying those trade-offs and the overall impact on the cost of hydrogen. 
Key Factors for Energy 
System Integration 
 
• Integration with clean 
energy sources 
• Electricity price 
• Capacity factor 
• Installation costs

44 
 
• Optimizing operating strategies, such as turning down the electrolyzer rather than 
turning it off, to reduce wear related to startup and shutdown processes [10].  
• Redesigning renewable energy technologies, such as wind turbines, for optimal 
hydrogen production instead of optimal electricity production [44]. 
 
The DOE Hydrogen Program is investigating a number of scenarios to better understand the 
impact on overall system economics of the variable renewable power load profiles involved in 
direct coupling. The program is also conducting ongoing analysis to quantify potential cost 
reductions and other benefits associated with direct coupling of electrolyzers to renewable 
power and integration with thermal energy sources at existing nuclear power plants [45] [46].  
 
While RD&D efforts to reduce hardware costs (for stack and system) and operating costs of 
electrolyzers are important to enable commercial deployment, it is also important to look beyond 
hardware and operations costs and consider balance-of-system costs, or “soft” costs, 
associated with electrolyzer deployment, installation, and overall integration into the energy 
system. Soft costs include all expenses that can contribute to the total cost of ownership of the 
electrolyzer system, except for electrolyzer system hardware, feedstock, electricity, operations, 
and maintenance. Examples include site preparation (e.g., concrete pads, water and electrical 
hookups), land, permits, commissioning, and delivery. These costs today are nontrivial and can 
be comparable to system capital costs. Some soft costs may decrease as the industry matures 
and more large-scale (>100-MW) electrolyzer systems are installed. Optimizing system designs 
to minimize installation complexity, potentially through modularization and/or standardization, 
will also help reduce these costs. As hardware and operating costs continue to decrease, soft 
costs are becoming increasingly important to the economics of electrolytic hydrogen production 
[47].  
 
Current analysis tools for electrolyzer technologies, such as DOE’s H2A tool, estimate soft costs 
assuming a certain percentage of capital expenses, following guidance provided by the 
Association for the Advancement of Cost Engineering International [8]. However, it is important 
to differentiate between types of electrolyzer technologies, system sizes, end uses, and site 
locations, because those factors could significantly affect the soft costs. With a growing number 
of electrolyzer installations both domestically and internationally, more real-world soft cost data 
are becoming available. Quantifying soft costs from past and current installations will not only 
improve general understanding of electrolyzer economics, but also provide insight into potential 
impediments to deployment. Potential approaches to reducing soft costs for electrolyzer projects 
may include providing technical assistance to state and local governments to accelerate 
planning, siting, and permitting activities; developing modularized, designed-for-installation 
systems to reduce construction, installation, and engineering costs; and creating training 
materials and programs that support the growth of a skilled workforce.

45 
 
CONCLUSION 
The use of water electrolyzers for hydrogen production will be critical to meeting DOE’s 
Hydrogen Shot goal. This technology assessment pulls from numerous resources to summarize 
the current state of the field in terms of cost, commercial and manufacturing readiness, 
performance, lifetime, and deployment, while highlighting opportunities for advances through 
RDD&D across several different types of electrolyzers: PEM, LA, O-SOEC, AEM, and P-SOEC.  
 
With well-focused, sustained investments in RDD&D, and based on specific scenarios 
integrating with renewable and/or nuclear power generation, the three most commercially 
mature electrolyzer technologies—PEM, LA, and O-SOEC—show the potential to achieve the 
Hydrogen Shot goal and realize an LCOH of $1/kg within a decade. In the longer term, the two 
lower-TRL technologies—AEM and P-SOEC—have potential advantages over these three with 
successful further technology developments. The techno-economic analysis conducted here 
utilized technical inputs from a number of sources referenced throughout this document, using 
published electrolyzer technical targets. It is based on clean energy scenarios representing the 
current grid, current clean energy resources, and future projections of hybrid clean energy 
systems. Other factors that influence cost, such as the sale of byproducts or the Clean 
Hydrogen Production Tax Credit (45V), were not considered in this analysis but could further 
reduce the LCOH. 
 
The five electrolyzer technologies included in this assessment are on different technology 
development timelines and at different levels of commercialization. Furthermore, the different 
technologies will be more competitive in some end uses and with certain clean energy 
resources than others. With government and industry projections of significant growth in 
demand for clean hydrogen for multiple end uses, it is likely that there will be viable and 
important roles for all of these technologies. And with such a diverse array of applications for 
hydrogen across multiple sectors, each with their own particular needs, it appears unlikely that 
only one or two electrolyzer technologies will completely dominate the market.  
 
The key RDD&D opportunities to achieve the Hydrogen Shot goals can be bundled into three 
main areas: technology advancements, manufacturing and economies of scale, and clean 
energy system integration. Efforts in all three areas are needed; innovations in one alone will 
not be sufficient to reduce the cost of hydrogen to $1/kg. Achieving the Hydrogen Shot goal will 
require a strategic allocation of resources and efforts across these areas. DOE’s Hydrogen 
Program, as well as the Hydrogen Interagency Task Force, are well positioned to address these 
broad RD&D needs to enable cost-effective, clean H2 production in the years to come, and to 
play an important role in achieving national climate and energy goals [48].

46 
 
REFERENCES 
 
[1]  DOE, "Hydrogen Shot Technology Assessment: Thermal Conversion Approaches," 
December 2023. [Online]. Available: https://www.netl.doe.gov/energy-
analysis/details?id=38898e1c-4e2a-4677-81dd-4fa5812c73f3. 
[2]  DOE, "U.S. National Clean Hydrogen Strategy and Roadmap," 2023. [Online]. Available: 
https://www.hydrogen.energy.gov/library/roadmaps-vision/clean-hydrogen-strategy-
roadmap. 
[3]  DOE, "Pathways to Commercial Liftoff: Clean Hydrogen," March 2023. [Online]. Available: 
https://liftoff.energy.gov/wp-content/uploads/2023/03/20230320-Liftoff-Clean-H2-vPUB.pdf. 
[4]  Executive Order 14008, "Tackling the Climate Crisis at Home and Abroad," January 2021. 
[Online]. Available: https://www.federalregister.gov/documents/2021/02/01/2021-
02177/tackling-the-climate-crisis-at-home-and-ab. 
[5]  Hydrogen Council, "Hydrogen Insights 2023," 2023. [Online]. Available: 
https://hydrogencouncil.com/en/hydrogen-insights-2023-december-update/. 
[6]  DOE, "Industrial Decarbonization Roadmap," September 2022. [Online]. Available: 
https://www.energy.gov/industrial-technologies/doe-industrial-decarbonization-roadmap. 
[7]  DOE, "The U.S. National Blueprint for Transportation Decarbonization," January 2023. 
[Online]. Available: https://www.energy.gov/sites/default/files/2023-01/the-us-national-
blueprint-for-transportation-decarbonization.pdf. 
[8]  NREL, "H2A-Lite," 2022. [Online]. Available: https://www.nrel.gov/hydrogen/h2a-lite.html. 
[9]  DOE, "Clean Hydrogen Production Cost Scenarios with PEM Electrolyzer Technology," 
2024 May 20. [Online]. Available: 
https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/24005-clean-
hydrogen-production-cost-pem-electrolyzer.pdf.. 
[10]  J. King, "Hybrid Energy System to H2 to Green Steel/Ammonia," 6 June 2023. [Online]. 
Available: 
https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review23/sdi001_h
ammond_2023_o-pdf.pdf. 
[11]  NREL, "2023 Electricity ATB Technologies and Data Overview," 2023. [Online]. Available: 
https://atb.nrel.gov/electricity/2023/index. 
[12]  D. S. Wendt, "High Temperature Steam Electrolysis Process Performance and Cost 
Estimates," March 2022. [Online]. Available: doi:10.2172/1867883. 
[13]  D. Leighton, "ARIES / Flatirons Facility - Hydrogen System Capability Buildout," 8 May 
2024. [Online]. Available: 
https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review24/ta048_lei
ghton_2024_o.pdf?sfvrsn=1bc055ce_3. 
[14]  DOE, "Water Electrolyzer Technical Targets," 2022. [Online]. Available: 
https://www.energy.gov/eere/fuelcells/hydrogen-production-related-links#targets.

47 
 
[15]  P. Denholm, "Examining Supply-Side Options to Achieve 100% Clean Electricity by 2035," 
August 2022. [Online]. Available: https://www.nrel.gov/analysis/100-percent-clean-
electricity-by-2035-study.html. 
[16]  J. Remer, "Process for Significant Nuclear Work Function Innovation Based on Integrated 
Operations Concepts," August 2021. [Online]. Available: 
https://lwrs.inl.gov/content/uploads/11/2024/03/ProcessSignificantNuclearWorkFunctionInn
ovation.pdf. 
[17]  A. A. Elgowainy, "Electrolyzers for Hydrogen Production: Solid Oxide, Alkaline, and Proton 
Exchange Membrane," ANL, Elgowainy, A., et al. Electrolyzers for Hydrogen Production: 
Solid Oxide, Alkaline, and Proton Exchange Membrane. Argonne National Laboratory, 
ANL/ESIA-22/3 (2022)., 2022. 
[18]  A. A. Elgowainy, "Hydrogen Life-Cycle Analysis in Support of Clean Hydrogen Production," 
ANL, 2022. 
[19]  Hydrogen Council, "Hydrogen decarbonization pathways: A life-cycle assessment," 
January 2021. [Online]. Available: https://hydrogencouncil.com/wp-
content/uploads/2021/01/Hydrogen-Council-Report_Decarbonization-Pathways_Part-1-
Lifecycle-Assessment.pdf. 
[20]  ANL, "GREET," December 2023. [Online]. Available: https://greet.es.anl.gov. 
[21]  WaterSMART Solutions Ltd., "Water for the Hydrogen Economy," November 2020. 
[Online]. Available: https://watersmartsolutions.ca/wp-content/uploads/2020/12/Water-for-
the-Hydrogen-Economy_WaterSMART-Whitepaper_November-2020.pdf. 
[22]  E. Connelly, "Resource Assessment for Hydrogen," July 2020. [Online]. Available: 
https://www.nrel.gov/docs/fy20osti/77198.pdf. 
[23]  IEA, "Global Hydrogen Review 2023," December 2023. [Online]. Available: 
https://www.iea.org/reports/global-hydrogen-review-2023#overview. 
[24]  DOE, "H2 Matchmaker," April 2023. [Online]. Available: 
https://www.energy.gov/eere/fuelcells/h2-matchmaker. 
[25]  DOE, "Biden-Harris Administration Announces $750 Million to Support America’s Growing 
Hydrogen Industry as Part of Investing in America Agenda," 13 March 2024. [Online]. 
Available: https://www.energy.gov/articles/biden-harris-administration-announces-750-
million-support-americas-growing-hydrogen. 
[26]  SAP, "What is industry 4.0?," [Online]. Available: 
https://www.sap.com/products/scm/industry-4-0/what-is-industry-4-0.html. [Accessed 
January 2024]. 
[27]  Fraunhofer Institute, "Cost Forecast for Low Temperature Electrolysis – Technology Driven 
Bottom-up Prognosis for PEM and Alkaline Water Electrolysis Systems," October 2021. 
[Online]. Available: https://publica-rest.fraunhofer.de/server/api/core/bitstreams/459031bc-
d874-4a24-b2af-5300add8a045/content. 
[28]  A. Badgett, "Updated Manufactured Cost Analysis for Proton Exchange Membrane Water 
Electrolyzers," 2024. [Online]. Available: https://www.nrel.gov/docs/fy24osti/87625.pdf. 
[29]  DOE, "ElectroCat," 2024. [Online]. Available: https://www.electrocat.org/.

48 
 
[30]  DOE, "H2-PACE: Power And Control Electronics for Hydrogen Technologies Meeting," 
December 2021. [Online]. Available: https://www.energy.gov/eere/fuelcells/h2-pace-power-
and-control-electronics-hydrogen-technologies-meeting. 
[31]  K. Nagasawa, "Electrolyzer Grid Integration Study," November 2020. [Online]. Available: 
https://www.energy.gov/sites/default/files/2020/12/f82/h2iq-webinar-november2020.pdf. 
[32]  Y. M. Acevedo, "Hydrogen Production Cost with Alkaline Electrolysis," October 2023. 
[Online]. Available: doi:10.2172/2203367. 
[33]  IEA, "Hydrogen Project Database," October 2021. [Online]. Available: 
https://www.iea.org/data-and-statistics/data-product/hydrogen-projects-
database#overview. 
[34]  B. James, "Liquid Alkaline Techno-economic Review," January 2022. [Online]. Available: 
https://www.energy.gov/sites/default/files/2022-02/7-TEA-
Liquid%20Alkaline%20Workshop.pdf. 
[35]  IRENA, "Green Hydrogen Cost Reduction: Scaling up Electrolysers to Meet the 1.5⁰C 
Climate Goal," December 2020. [Online]. Available: https://www.irena.org/-
/media/Files/IRENA/Agency/Publication/2020/Dec/IRENA_Green_hydrogen_cost_2020.pd
f?rev=95b8c10569874148a44e1d17b301d263. 
[36]  DOE, "Advanced Liquid Alkaline Electrolysis Experts Meeting Report," January 2022. 
[Online]. Available: https://www.energy.gov/eere/fuelcells/advanced-liquid-alkaline-
electrolysis-experts-meeting. 
[37]  J. Prosser, "Cost Analysis of Hydrogen Production by High-Temperature Solid Oxide 
Electrolysis," Int. J. Hydrog. Energy, vol. 4, pp. 207-227, March 2023.  
[38]  S. D. Ebbesen, "Poisoning of Solid Oxide Electrolysis Cells by Impurities," Journal of The 
Electrochemical Society, vol. 10, no. 157, pp. B1419-B1429, 2010.  
[39]  B. James, "Final Report: H2 Production Pathways Cost Analysis (2016 - 2021)," 
December 2021. [Online]. Available: https://doi.org/10.2172/2280867. 
[40]  H. A. Miller, "Green hydrogen from anion exchange membrane water electrolysis: a review 
of recent developments in critical materials and operating conditions," Sustainable Energy 
Fuels, no. 5, pp. 2114-2133, 2020.  
[41]  A. Badgett, "Chapter 10 - Economic considerations for hydrogen production with a focus 
on polymer electrolyte membrane electrolysis," Electrochemical Power Sources: 
Fundamentals, Systems, and Applications, pp. 327-364, 2022.  
[42]  DOE, "H2NEW," 2024. [Online]. Available: https://h2new.energy.gov/. 
[43]  DOE, "Hybrid Energy Systems: Opportunities for Coordinated Research," April 2021. 
[Online]. Available: https://www.nrel.gov/docs/fy21osti/77503.pdf. 
[44]  C. Bay, "Optimal Wind Turbine Design for H2 Production," 7 June 2023. [Online]. 
Available: 
https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review23/ta061_ba
y_2023_o-pdf.pdf. 
[45]  A. Barker, "U.S. Wind to Hydrogen Modeling Analysis, Testing, and Collaboration," June 
2022. [Online]. Available: 
https://www.hydrogen.energy.gov/pdfs/review22/ta060_sprik_2022_o.pdf.

49 
 
  
[46]  DOE, "DOE Awards $22.1 Million to Advance Promising Nuclear Technologies," May 
2023. [Online]. Available: https://www.energy.gov/ne/articles/doe-awards-221-million-
advance-promising-nuclear-technologies. 
[47]  DOE, "Electrolyzer Installation Webinar," 27 Sept 2024. [Online]. Available: 
https://www.energy.gov/eere/fuelcells/electrolyzer-installation-webinar. 
[48]  DOE, "Hydrogen Interagency Task Force," 2023. [Online]. Available: 
https://www.hydrogen.energy.gov/interagency. 
[49]  DOE, "H2A," November 2020. [Online]. Available: https://www.nrel.gov/hydrogen/h2a-
production-models.html. 
[50]  EIA, "Average Price of Electricity to Ultimate Customers by End-Use Sector," 2022. 
[Online]. Available: https://www.eia.gov/electricity/annual/html/epa_02_10.html. 
[51]  Energy Information Administration, "Form ETA-860 detailed data with previous form data 
(EIA-860/860B)," 2022. [Online]. Available: https://www.eia.gov/electricity/data/eia860/. 
[52]  Lawrence Berkeley National Laboratory, "Wind Power Purchase Agreement Prices," 2022. 
[Online]. Available: https://emp.lbl.gov/wind-power-purchase-agreement-ppa-prices. 
[53]  C. Murphy, "Complementarity of Renewable Energy-Based Hybrid Systems," U.S. 
Department of Energy, Grid Modernization Laboratory Consortium, Vols. DOE/GO-
102023-5896, 2023.

50 
 
APPENDIX 
The Hydrogen Analysis Lite Production (H2A-Lite) model, a peer-reviewed, national-laboratory-
developed model and simplified successor to the original Hydrogen Analysis (H2A) model, was 
used to determine the levelized cost of hydrogen (LCOH) production in units of 2020 $/kg H2 for 
Figure 4 [8]. The modeled systems are stand-alone, grid-connected electrolyzers with a 
nominal hydrogen production capacity of about 50,000 kg/day.18 Methods from previously 
published H2A production models and reports were used to determine inputs into H2A-Lite [49]. 
Key assumptions summarized in the following tables are based heavily on U.S. Department of 
Energy (DOE) water electrolysis technical targets developed for generalized proton exchange 
membrane (PEM), liquid alkaline (LA), and oxide-ion-conducting solid-oxide electrolyzer cell (O-
SOEC) electrolyzers using inputs from several key industry and national laboratory collaborators 
with relevant experience in electrolyzer technology and techno-economic analysis [14]. 
Assumptions are also consistent with a number of previous reports.19 All other required 
parameters in H2A-Lite default to the assumptions for the “Central Grid Electrolysis (PEM)” 
(PEM and LA) and “Central Grid Electrolysis (SOEC)” (O-SOEC) case studies embedded in the 
model. 
  
  
 
18 This system size is consistent with the current trend in deployed electrolyzer systems. 
19 Uninstalled capital cost, system efficiency, and replacement interval are consistent with the range of values in [3], [27], and [35].

51 
 
Table A-1. Key Parameters Used To Determine Hydrogen Levelized Cost for PEM Electrolyzers in 
H2A-Lite20 
Parameter PEM – Current Status PEM – 2026 Target PEM – 2031 Target 
Nominal hydrogen production capacity 50,000 kg/day 50,000 kg/day 50,000 kg/day 
Stack rated power requirement (BOL) 106 MW 100 MW 90 MW 
System rated power requirement (BOL) 115 MW 106 MW 96 MW 
System rated power requirement 
(average) 120 MW 111 MW 100 MW 
Plant startup year 2020 2020 2020 
System life 30 yr 30 yr 30 yr 
Uninstalled capital cost (2020 $)21 $700–$1,100/kW $250/kW $150/kW 
Total installed capital (2020 $)22 $1,400–$2,200/kW $385/kW $210/kW 
Annual fixed operating cost (2020 $/yr)23 $70–$110/kW/yr $19/kW/yr $11/kW/yr 
Stack operating point (BOL) 2 A/cm2 @ 1.9 V/cell 3 A/cm2 @ 1.8 V/cell 3 A/cm2 @ 1.6 V/cell 
Stack replacement interval24 40,000 operating hours 80,000 operating hours 80,000 operating hours 
Voltage degradation rate 4.8 mV/kh 2.3 mV/kh 2 mV/kh 
Replacement costs25 11% of total installed cost 11% of total installed cost 11% of total installed cost 
Stack electricity usage (BOL) 51 kWh/kg 48 kWh/kg 43 kWh/kg 
System electricity usage (BOL) 55.2 kWh/kg 51 kWh/kg 46 kWh/kg 
System electricity usage (average) 57.5 kWh/kg 53.3 kWh/kg 47.9 kWh/kg 
System thermal energy usage - - - 
Water/steam usage 3.78 gal/kg 3.78 gal/kg 3.78 gal/kg 
  
 
20 Parameters for all years based on [14]. 
21 Uninstalled electrolyzer system capital cost in 2020 $/kW, which includes the cost of the electrolyzer stack and balance of plant 
(BOP) (including markup from the manufacturer), normalized by the rated beginning of life (BOL) stack power. 
22 Total installed capital cost normalized by the rated BOL stack power. Total installed capital estimated as about 2 times (Current 
Status), 1.55 times (2026 Target), and 1.4 times (2031 Target) the uninstalled capital cost to represent learning in installations over 
time from first-of-a-kind (Current Status) to nth-of-a-kind plants (2031 Target). 
23 Fixed operating costs estimated as 5% of the total installed capital cost and normalized by the rated BOL stack power.  
24 Replacement intervals given in units of operating hours will have variable replacement intervals in years depending on the 
capacity factor. 
25 11% of total installed cost corresponds to about 15% of direct capital cost, consistent with H2A methodology.

52 
 
Table A-2. Key Parameters Used To Determine Hydrogen Levelized Cost for LA Electrolyzers in 
H2A-Lite 26 
Parameter LA – Current Status LA – 2026 Target LA – 2031 Target 
Nominal hydrogen production capacity 50,000 kg/day 50,000 kg/day 50,000 kg/day 
Stack rated power requirement (BOL) 106 MW 100 MW 94 MW 
System rated power requirement (BOL) 115 MW 108 MW 100 MW 
System rated power requirement 
(average) 119 MW 113 MW 105 MW 
Plant startup year 2020 2020 2020 
System life 30 yr 30 yr 30 yr 
Uninstalled capital cost (2020 $)27 $500–$750/kW $250/kW $150/kW 
Total installed capital (2020 $)28 $1,000–$1,500/kW $385/kW $210/kW 
Annual fixed operating cost (2020 $/yr)29 $50–$75/kW/yr $19/kW/yr $11/kW/yr 
Stack operating point (BOL) 0.5 A/cm2 @ 1.9 V/cell 1 A/cm2 @ 1.8 V/cell 2 A/cm2 @ 1.7 V/cell 
Stack replacement interval30 60,000 operating hours 80,000 operating hours 80,000 operating hours 
Replacement costs31 11% of total installed cost 11% of total installed cost 11% of total installed cost 
Voltage degradation rate 4.8 mV/kh 2.3 mV/kh 2.1 mV/kh 
Stack electricity usage (BOL) 51 kWh/kg 48 kWh/kg 45 kWh/kg 
System electricity usage (BOL) 55 kWh/kg 52 kWh/kg 48 kWh/kg 
System electricity usage (average) 57.3 kWh/kg 54.3 kWh/kg 50.4 kWh/kg 
System thermal energy usage - - - 
Water/steam usage 3.78 gal/kg 3.78 gal/kg 3.78 gal/kg 
  
 
26 Parameters for all years based on [14]. Additionally, range of capital cost for Current Status based on 4.5-MW stacks and 10-MW 
system modules from [32]. 
27 Uninstalled electrolyzer system capital cost in 2020 $/kW, which includes the cost of the electrolyzer stack and BOP (including 
markup from the manufacturer), normalized by the rated BOL stack power. 
28 Total installed capital cost normalized by the rated BOL stack power. Total installed capital estimated as about 2 times (Current 
Status), 1.55 times (2026 Target), and 1.4 times (2031 Target) the uninstalled capital cost to represent learning in installations over 
time from first-of-a-kind (Current Status) to nth-of-a-kind plants (2031 Target). 
29 Fixed operating costs estimated as 5% of the total installed capital cost and normalized by the rated BOL stack power. 
30 Replacement intervals given in units of operating hours will have variable replacement intervals in years depending on the 
capacity factor. 
31 11% of total installed cost corresponds to about 15% of direct capital cost, consistent with H2A methodology.

53 
 
Table A-3. Key Parameters Used To Determine Hydrogen Levelized Cost for O-SOEC Electrolyzers 
in H2A-Lite32 
Parameter 
O-SOEC – 
Current 
Status 
O-SOEC – 
2026 Target 
O-SOEC – 
2031 Target 
Nominal hydrogen production capacity 50,000 kg/day 50,000 kg/day 50,000 kg/day 
Stack rated power requirement (BOL) 71 MWel 71 MWel 71 MWel 
System rated power requirement (BOL) 
100 MW  
(79 MWel, 21 
MWth) 
93 MW 
(75 MWel, 18 
MWth) 
89 MW 
(73 MWel, 16 
MWth) 
System rated power requirement 
(average) 
103 MW  
(82 MWel, 21 
MWth) 
97 MW 
(79 MWel, 18 
MWth) 
92 MW 
(76 MWel, 16 
MWth) 
Plant startup year 2020 2020 2020 
System life 30 yr 30 yr 30 yr 
Uninstalled capital cost (2020 $)33 $2,000–$2,500/kW $500/kW $200/kW 
Total installed capital (2020 $)34 $4,000–$5,000/kW $775/kW $280/kW 
Annual fixed operating cost (2020 $/yr)35 $200–$250/kW/yr $39/kW/yr $14/kW/yr 
Stack operating point (BOL) 0.6 A/cm2 @ 1.28 V/cell 1.2 A/cm2 @ 1.28 V/cell 2 A/cm2 @ 1.28 V/cell 
Stack replacement interval36 20,000 operating hours 40,000 operating hours 80,000 operating hours 
Replacement costs37 11% of total installed cost 11% of total installed cost 11% of total installed cost 
Voltage degradation rate 6.4 mV/kh 3.2 mV/kh 1.6 mV/kh 
Stack electricity usage (BOL) 34 kWh/kg 34 kWh/kg 34 kWh/kg 
System electricity usage (BOL) 38 kWh/kg 36 kWh/kg 35 kWh/kg 
System electricity usage (average) 40 kWh/kg 38 kWh/kg 37 kWh/kg 
System thermal energy usage38 9 kWh/kg 8 kWh/kg 7 kWh/kg 
Water/steam usage 2.38 gal/kg 2.38 gal/kg 2.38 gal/kg 
 
 
32 Parameters for all years based on [14]. For Current Status, uninstalled capital cost range is based on input from Idaho National 
Laboratory and is consistent with [3]. 
33 Uninstalled electrolyzer system capital cost in 2020 $/kW, which includes the cost of the electrolyzer stack and BOP (including 
markup from the manufacturer), normalized by rated BOL stack power. 
34 Total installed capital cost normalized by the rated BOL stack power. Total installed capital estimated as about 2 times (Current 
Status), 1.55 times (2026 Target), and 1.4 times (2031 Target) the uninstalled capital cost to represent learning in installations over 
time from first-of-a-kind (Current Status) to nth-of-a-kind plants (2031 Target). 
35 Fixed operating costs estimated as 5% of the total installed capital cost and normalized by the rated BOL stack power.  
36 Replacement intervals given in units of operating hours will have variable replacement intervals in years depending on the 
capacity factor. 
37 11% of total installed cost corresponds to about 15% of direct capital cost, consistent with H2A methodology. 
38 Natural gas assumed to be the thermal energy source in the LCOH calculation using default H2A-Lite price assumptions. In some 
applications, thermal energy may be provided by industrial processes.

54 
 
Table A-4. Financial Assumptions for All Scenarios (All Technologies, All Years) 
Financial Assumptions 
Real return on equity 10.89% 
Debt/equity 0.62 
Interest rate 5% 
Depreciation type Modified accelerated cost recovery system (MACRS) 
MACRS depreciation period 20 yr 
Total income tax rate 25.74% 
Cash on hand  1.0 month of operating expenses 
Dollar-year basis 2020 
 
Financial specifications were selected to result in a ~10% nominal weighted average cost of 
capital (WACC).

55 
 
Table A-5. LCOH (2020 $/kg) for Each Electricity Scenario Shown in Figure 4 
Scenario 
Electricity 
Price  
(cents/kWh) 
Capacity 
Factor39  
(%) 
LCOH  
(2020 $/kg) 
PEM LA O-SOEC 
Current Technology Status 
Grid, U.S. average industrial 7.4 97% 6.07–7.23 5.56–6.17 7.15–8.14 
2026 Target Scenarios 
Future grid, low estimate 6.5 97% 4.00 4.06 3.35 
Future grid, high estimate 10.0 97% 5.89 5.98 4.69 
Land-based wind, Class 1, 2026 advanced 2.0 54% 1.90 1.91 2.11 
Land-based wind, Class 1, 2026 conservative 2.4 50% 2.17 2.19 2.34 
Conventional nuclear power, low estimate 1.8 97% 1.46 1.48 1.56 
Conventional nuclear power, high estimate 3.0 97% 2.11 2.14 2.02 
Hybrid system, half size (with aggressive 
renewable generation cost reductions) 1.2 74% 1.26 1.27 1.52 
Hybrid system, same size (with renewable 
generation PTC) 1.0 40% 1.62 1.62 2.09 
2031 Target Scenarios 
Future grid, low estimate 6.0 97% 3.17 3.33 2.66 
Future grid, high estimate 7.0 97% 3.65 3.84 3.03 
Land-based wind, Class 1, 2031 advanced 1.7 57% 1.23 1.28 1.21 
Land-based wind, Class 1, 2031 conservative 2.3 51% 1.56 1.64 1.48 
Conventional nuclear power, low estimate 1.8 97% 1.14 1.19 1.10 
Conventional nuclear power, high estimate 3.0 97% 1.72 1.80 1.54 
Hybrid system, half size (with aggressive 
renewable generation cost reductions) 1.2 74% 0.91 0.95 0.94 
Hybrid system, same size (with aggressive 
renewable generation cost reductions) 1.0 40% 1.03 1.08 1.10 
 
  
 
39 This value corresponds to “Utilization” in the H2A-Lite tool.

56 
 
Table A-6. LCOH (2020 $/kg) for the PEM Electrolysis Pathway to H2 Shot Shown in Figure 6  
Technology 
Year40 Electricity Scenario 
Electricity 
Price  
(cents/kWh) 
Capacity 
Factor41  
(%) 
LCOH  
(2020 
$/kg) 
Current Grid, U.S. average industrial 7.4 97% 6.65 
Current Land-based wind, Class 1, 2023 moderate, without renewable generation PTC 2.6 51% 5.64 
Current Hybrid system, half size, without renewable generation PTC 2.9 74% 4.65 
2026 Hybrid system, half size, without renewable generation PTC 2.9 74% 2.18 
2031 Hybrid system, half size, without renewable generation PTC 2.9 74% 1.73 
2031 Hybrid system, half size, with renewable generation PTC 1.2 74% 0.91 
 
 
Table A-7. LCOH (2020 $/kg) for the High-Temperature Electrolysis Pathway to H2 Shot  
Shown in Figure 6  
Technology 
Year Electricity Scenario 
Electricity 
Price  
(cents/kWh) 
Capacity 
Factor42  
(%) 
LCOH  
(2020 
$/kg) 
Current Grid, U.S. average industrial 7.4 97% 7.34 
2026 Grid, U.S. average industrial 7.4 90% 4.17 
2026 Tight Integration with Nuclear Plant 3.0 95% 1.99 
2031 Tight Integration with Nuclear Plant 3.0 95% 1.50 
2031 Optimized Integration/Flexible Operation43  2.0 95% 1.00 
 
  
 
40 Current technology cases assume an average of high and low capital cost estimates from Table A-1. 
41 This value corresponds to “Utilization” in the H2A-Lite tool. 
42 This value corresponds to “Utilization” in the H2A-Lite tool. 
43 Includes oxygen sales offset of $0.1/kg-H2.

57 
 
Table A-5 shows the range of hydrogen levelized cost for PEM, LA, and O-SOEC technologies 
based on the parameters in Table A-1–Table A-4 for the different electricity source scenarios 
further detailed below: 
 
• Grid: While not considered “clean,” grid cases are included here as reference points 
using industrial electricity prices from the U.S. Energy Information Administration, which 
catalogues annual pricing across individual states and regions [50]. The average case 
represents the U.S. average grid electricity price for 2022 identified by the U.S. Energy 
Information Administration. 
• Future grid: The future grid scenarios are based on the Examining Supply-Side Options 
to Achieve 100% Clean Electricity by 2035 report [15]. The electricity prices are based 
on net system costs of achieving a 100% clean electricity grid by 2035, and combine 
electricity system costs, health costs, and climate costs. The 2026 scenario reflects an 
approximately 65% clean grid, and the 2031 scenario reflects an approximately 85% 
clean grid. 
• Land-based wind: The wind case is based on installations modeled in the National 
Renewable Energy Laboratory’s 2023 Annual Technology Baseline for land-based Class 
1 (best) wind conditions with high-resolution, location-specific resource data [11]. This 
case assumes R&D financial assumptions and does not include the renewable 
generation production tax credits (PTC). Values are adjusted from reported 2021 $ to 
2020 $ based on a 4.7% inflation rate. Many of the operational Class 1 wind farms in the 
United States are in south-central California, western Texas, the Plains states, and 
southern Minnesota [51]. Power purchase agreements have been established for some 
of the Class 1 wind sites located in Colorado, Iowa, Illinois, Kansas, New Mexico, Texas, 
and others. As an example, a power purchase agreement for an approximately 200-MW 
wind farm in the Southwest Power Pool region (which includes Iowa, Kansas, and 
Nebraska) had a price as low as about $0.016/kWh [51] [52]. While wind power 
purchase agreements vary, this example shows that high-quality wind resources are 
promising for low-cost hydrogen production in the near term.  
• Nuclear: Assumptions for the nuclear power scenario are based on baseload power 
from an existing conventional nuclear power plant that includes only operating, 
maintenance, and fuel costs in the levelized cost of electricity [16]. 
• Hybrid wind + solar: This case reflects combined hourly generation from collocated 
solar and wind energy sources in a hybrid system to produce low-cost electricity with a 
high capacity factor. The location was selected based on the complementarity of solar 
and wind resources, where a location with high complementarity will result in a high 
capacity factor due to the fact that wind and solar production happen at different times. 
The capacity factor and levelized cost of electricity assumed here were developed by the 
Grid Modernization Laboratory Consortium based on a published methodology [53] and 
actual historical weather data for a location in Texas with high complementarity. The 
“half-size” configuration is for an electrolyzer capacity sized to 50% of the total solar and 
wind generation capacity (i.e., 100-MW electrolyzer and 200 MW of combined solar and 
wind), while the “same-size” configuration is for an electrolyzer capacity equal to the total 
solar and wind generation capacity (i.e., 200-MW electrolyzer and 200 MW of combined

58 
 
solar and wind). Where specified, the levelized cost of electricity values include the 
renewable generation production tax credit (PTC) of $17/MWh.
