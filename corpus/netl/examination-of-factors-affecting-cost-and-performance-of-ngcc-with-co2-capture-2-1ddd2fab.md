---
source_id: "netl"
title: "Examination of Factors Affecting Cost and Performance of NGCC with CO2 Capture 2025"
summary: "NETL 2025 examination of the factors that drive cost and performance of natural gas combined cycle plants with CO2 capture."
url: "https://netl.doe.gov/projects/files/ExaminationofFactorAffectingCostPerformanceNaturalGasCombineCycleEquipCarbonDioxideCaptur_031425.pdf"
retrieved_at: "2026-10-24T04:53:06+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "CCS", "H2", "PWR"]
disciplines: ["PRC", "MAT"]
sha256: "1ddd2fab49775540c661e8b5808aaa7df32895d0fe5dac386c94e4f0f97e1f8f"
collected: "manual"
---

# Examination of Factors Affecting Cost and Performance of NGCC with CO2 Capture 2025

EXAMINATION OF FACTORS 
AFFECTING THE COST AND 
PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED 
WITH CARBON DIOXIDE CAPTURE 
 
 
 
 March 14, 2025 
 DOE/NETL-2025/4923

Disclaimer 
 
This project was funded by the United States Department of Energy, National Energy 
Technology Laboratory, in part, through a site support contract. Neither the United 
States Government nor any agency thereof, nor any of their employees, nor the 
support contractor, nor any of their employees, makes any warranty, express or implied, 
or assumes any legal liability or responsibility for the accuracy, completeness, or 
usefulness of any information, apparatus, product, or process disclosed, or represents 
that its use would not infringe privately owned rights. Reference herein to any specific 
commercial product, process, or service by trade name, trademark, manufacturer, or 
otherwise does not necessarily constitute or imply its endorsement, recommendation, or 
favoring by the United States Government or any agency thereof. The views and 
opinions of authors expressed herein do not necessarily state or reflect those of the 
United States Government or any agency thereof. 
 
All images in this report were created by NETL, unless otherwise noted.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
 
 
 
Sarah Leptinsky1: Methodology, Formal Analysis, Investigation, Writing 
– Original Draft, Visualization; Marc Turner1: Methodology, Validation, 
Formal Analysis, Writing – Original Draft, Writing – Review and Editing, 
Visualization, Supervision; Matthew Oakes1: Methodology, Formal 
Analysis, Writing – Original Draft, Supervision; Danny Quinn1: 
Methodology, Formal Analysis, Writing – Original Draft; James 
Gummoe1: Methodology, Formal Analysis, Writing – Original Draft; 
Sally Homsy2: Writing – Review and Editing, Validation;  Troy Teel1: 
Writing – Review and Editing, Validation; Patricia Cvetic1: Writing – 
Review and Editing; Norma Kuehn1: Writing – Review and Editing, 
Validation;  Mark Woods1: Writing – Review and Editing, Supervision; 
Travis Shultz2: Conceptualization, Writing – Review and Editing, 
Supervision, Project Administration; Hannah Hoffman1: Writing – 
Review and Editing  
 
1National Energy Technology Laboratory (NETL) support contractor 
2NETL 
Corresponding contact: Indrajit Bhattacharya, Indrajit.Bhattacharya@netl.doe.gov, 
412-386-7389 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Suggested Citation: S. Leptinsky et al. (2025). Examination of Factors Affecting the Cost 
and Performance of a Natural Gas Combined Cycle Equipped with Carbon Dioxide 
Capture. National Energy Technology Laboratory, Pittsburgh.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
 
  
This page intentionally left blank.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
1 
1 INTRODUCTION  
Techno-economic analyses (TEAs) are performed to evaluate the cost and performance of a 
power-generation technology for a variety of purposes, including to establish a commercial 
benchmark; estimate the commercial potential of a technology; inform research and 
development priorities and business or policy decisions; compare—on a common basis—
technologies for a given purpose; project the economic benefit of a technology; identify 
feasibility, performance, and cost issues; inform testing, modeling, or design priorities; and 
assess economic uncertainty and risk. TEA study data are routinely used as input for energy 
system modeling efforts (e.g., capacity expansion, production cost) engaged in planning, 
performing scenario analyses, or developing energy sector regulations. Others, while 
conducting research or performing a feasibility study, may seek to approximate the cost and 
performance of a plant’s technology and configuration to be constructed at a particular location 
and time. For all of these uses, it’s important to understand the impact of deviations from a 
study’s assumptions on the reported cost and performance.  
TEAs of fossil fuel power plants incorporating CO2 capture are published by multiple sources 
(e.g., National Energy Technology Laboratory [NETL], Wood Group, Energy Information 
Administration [EIA], Lazard). As demonstrated in Exhibit 1-1, cost and performance estimates 
for a particular technology and plant configuration will differ due to a host of factors embodied 
in the study’s assumptions. These differences may include technology selection, production 
scale, vintage of data, finance structure and assumptions, market assumptions (e.g., feedstock 
prices), operational assumptions (e.g., capacity factor), construction assumptions, and 
performance assumptions.  
Exhibit 1-1. Published TEA comparison studies (NETL, 2022-a) (Lazard, 2018) (EIA, 2016) (Wood Group, 2018) 
 
NGCC = natural gas combined cycle; T&S = transport and storage

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
2 
 
While the variation in reported cost estimates due to the AACE International (AACE) uncertainty 
classification associated with a study may be acknowledged, potential deviations due to other 
factors are often not extensively reported. Details associated with the location, design, 
construction, operation, and finance of the subject plant, in actual practice, will entail multiple 
deviations from a reference study’s assumptions, potentially resulting in substantial differences 
in cost and performance. 
The purpose of this Technical Note is to report the findings of an examination of the effect of 
plausible deviations in select study assumptions on the reported cost and performance 
estimates for a power plant case drawn from NETL’s “Cost and Performance Baseline for Fossil 
Energy Plants Volume 1: Bituminous Coal and Natural Gas to Electricity” (known as the Fossil 
Energy Baseline [FEB]) (NETL, 2022-b). An F-Class NGCC power plant equipped with state-of-the-
art, solvent-based, post-combustion carbon dioxide (CO2) capture (95 percent carbon capture 
rate)—designated as Case B31B.95—was selected for this work. This sensitivity analysis 
provides insight into the effects of parameter variations within and across selected categories—
ambient conditions, construction cost, natural gas (NG) price, capacity factor, and finance—on 
the plant performance and capital and operating and maintenance (O&M) costs, and the 
subsequent impact on common figures of merit.  
The capital cost estimate of Case B31B.95 is intended to represent the next commercial offering, 
with an uncertainty range of -15 percent/+25 percent—consistent with AACE Class 4 cost 
estimates—based on the level of engineering design performed (NETL, 2019-b) (AACE, 2003) 
(AACE, 2005). The capital costs rely on vendor cost estimates for component technologies and 
apply process contingencies at the appropriate subsystem levels to account for expected but 
undefined costs, which can be a challenge for emerging technologies such as CO2 capture.  
As the cost estimate uses the same cost estimating methodology as mature plant designs, the 
unique cost premiums associated with the initial, complex integrations of emerging 
technologies such as CO2 capture in a commercial application are not fully accounted for. Thus, 
it is anticipated that early deployments of NGCC plants with CO2 capture may incur costs higher 
than those reflected within the FEB and this Technical Note. Continuing research, development, 
and demonstration is expected to result in designs that are more advanced than those assessed 
in the FEB, leading to cost reductions over time. 
Actual reported project costs are also expected to deviate from the FEB and Technical Note cost 
estimates due to project- and site-specific considerations (e.g., contracting strategy, permitting, 
water quality, local environmental concerns, weather delays) that may make construction more 
costly. Such variations are not captured by the reported cost uncertainty.   
2 METHODS 
The FEB estimates the full-load, steady-state cost and performance of specific greenfield power 
plant configurations using a common set of assumptions to enable direct comparison of the 
evaluated cases. The levelized cost of electricity (LCOE) and cost of capture (COC) are derivative 
figures of merit.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
3 
To the extent possible, the plant design of each sensitivity in this Technical Note is maintained 
consistent with the B31B.95 base case to isolate the effects of each factor, modifying only the 
performance and cost parameters necessary to accurately assess the factor’s impact.a 
Some of the key assumptions supporting the base case cost estimates include the following: 
• Basic design with average material specifications, limited redundancy and plant 
automation, and optimized plant layout to minimize cost 
• Greenfield site, free from hazardous materials or archeological artifacts 
• Ideal site conditions (flat and level site, no rock excavation, limited seismic or wind 
considerations, no piles, easily accessible, etc.) 
• Competitive bidding environment 
• Low-cost labor market with relatively high productivity  
• Adequate supply of skilled craft labor available locally 
• Optimized construction schedule  
The parameter values for the ambient condition category sensitivities—selected to span 
plausible ranges for power plant locations in the United States—are listed in Exhibit 2-1. Base 
case values correspond to those of the B31B.95 reference case. Aspen Plus® was used to model 
plant performance at each set of ambient conditions. The capital costs were scaled from FEB 
costs using select process parameters extracted from the performance models using the 
methodology established by NETL (NETL, 2019-a). 
Exhibit 2-1. Ambient condition sensitivity ranges 
Parameter 
Value Basis Case Name 
Site Elevation 
0 m International Organization for Standardization (ISO) (NETL, 2022-a) Base 
1,609 m Denver, CO (USGS, 2005) High 
Ambient Temperature 
5.3 °C Annual Average – North Dakota (NCEI, n.d.-a) Cold 
15.0 °C ISO (NETL, 2022-a) Base 
22.4 °C Annual Average – Florida (NCEI, n.d.-a) Hot 
Ambient Relative Humidity 
20% Annual Average (afternoon) – Las Vegas, Nevada (NCEI, n.d.-b) Dry 
60% ISO (NETL, 2022-a) Base 
 
a While the cases within this study include CO2 capture, the effect of ambient conditions on the capture system could 
not be accounted for as the available vendor data were insufficient to determine the effect on cost or performance 
across the range of factors assessed.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
4 
Parameter 
Value Basis Case Name 
90% Annual Average (morning) – Lake Charles, Louisiana (NCEI, n.d.-b) Hum 
USGS = U.S. Geological Survey; NCEI = National Centers for Environmental Information 
The parameter sensitivity ranges for the construction cost category are shown in Exhibit 2-2. 
Base case values correspond to those of the B31B.95 reference case. In many of the accounts, 
the low range value represents the base case, meaning the base case is already at ideal 
conditions and cannot be reduced further.  
Exhibit 2-2. Construction conditions sensitivity ranges 
Parameter Low Base High 
Use of Piles No No Yes 
Cost of Concrete 1.00 1.00 1.25 
Cost of Steel 0.90 1.00 1.30 
Seismic – Equipment – Purchase 1.00 1.00 1.04 
Seismic – Equipment – Install 1.00 1.00 1.01 
Seismic – Foundations – Purchase 1.00 1.00 1.25 
Seismic – Foundations – Install 1.00 1.00 1.15 
Seismic – Steel – Purchase 1.00 1.00 1.50 
Seismic – Steel – Install 1.00 1.00 1.30 
Labor Productivity 0.95 1.00 1.25 
Labor Rate (Merit: Low; Union: High) 0.85 1.00 1.29 
Process Contingency 1.00 1.00 2.00 
Project Contingency 1.00 1.00 1.50 
 
For projects having identical scope, the labor cost is primarily driven by location, labor pool, and 
market conditions. These factors will determine wage rates and anticipated local productivity. 
The labor rate explores variations in cost resulting from the use of union versus merit shop 
(non-union) labor, whereas labor productivity explores the variations in cost resulting from 
either improved or reduced productivity relative to the expected regional labor productivity for 
the selected construction labor market. The labor productivity sensitivity is applied as a factor 
to labor cost—low productivity results in labor costs increasing by 25 percent, and high 
productivity results in labor costs decreasing by 5 percent.  
The potential severity of seismic activity will have an impact on the project design 
requirements, and therefore costs. The base case estimates consider a project location with 
minimal seismic activity and no requirement for special design considerations. Therefore, the 
base case estimates also represent the low case sensitivity. For the high case sensitivity, a 
location in the area roughly between St. Louis and Memphis was selected. This is representative

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
5 
of areas with potentially more severe seismic activity across the United States but does not 
encompass the more extreme conditions typically associated with the West Coast.  
Site-specific soil conditions determine whether the project foundations require piles. For the 
purposes of this Technical Note, a case with piles was evaluated relative to the base case 
without piles.  
For the cost-of-concrete sensitivity, only the cost associated with the purchase and delivery of 
concrete was evaluated.  
The cost of steel explores variations in the supply and delivery cost of all products containing 
steel: building structural steel, miscellaneous steel, pipe and valves, concrete reinforcing steel, 
mechanical equipment, electrical equipment, and electrical bulks.  
Sensitivities were performed to explore variations in cost related to adjusting levels of project 
and process contingencies, respectively. Contingencies account for anticipated but unspecified 
costs due to a lack of complete project definition and engineering. Project contingency was 
added as a percentage of the total plant cost (TPC). The process contingency is intended to 
compensate for uncertainty in cost estimates caused by performance uncertainties associated 
with the development status of a technology; as applied here, it is associated with the less 
mature CO2 capture and associated instrumentation and control elements. 
For the finance category, four parameters were assessed: effective tax rate, return on equity, 
interest on debt, and debt-to-equity ratio. The parameter sensitivity ranges for the finance 
category are shown in the Exhibit 2-3. Base case values correspond to those of the B31B.95 
reference case. 
Exhibit 2-3. Financial parameter sensitivity ranges 
Parameter Low Base High 
Effective Tax Rate, % 15.0 25.7 36.3 
Return on Equity, % 8.5 10 13.8 
Interest on Debt, % 4.7 5.0 7.5 
Debt-to-Equity Ratio 1.00 1.22 1.50 
 
Additionally, sensitivities were performed on the capacity factor and the NG price, with the 
parameter sensitivity ranges for each shown in Exhibit 2-4.  
Exhibit 2-4. Financial parameter sensitivity ranges 
Parameter Low Base High 
Capacity Factor, % 30 85 90 
NG Price, $/GJ 1.90 4.19 7.54

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
6 
The costs within this study are all reported on a December 2018-dollar basis, consistent with 
the FEB. There are many indices available to adjust costs to alternate dollar bases. Sensitivities 
were performed to explore the variations in cost resulting from the use of several indices, 
including the Consumer Price Index (CPI), Handy Whitman (HW), and Chemical Engineering 
Plant Cost Index (CEPCI)b to adjust the year-dollar basis to 2022. The results of these 
sensitivities were then used to determine the impact on the TPC, LCOE, and COC.c 
3 COST AND PERFORMANCE RESULTS 
The cost and performance results for the parameter sensitivities within each category are 
summarized in the following exhibits. Exhibit 3-1 and Exhibit 3-2 demonstrate the impact of air 
density (as a function of altitude, temperature, and humidity) on the combustion turbine and 
the bottoming cycle output, respectively. The net power and net plant efficiency for the 
ambient condition sensitivity cases are shown in Exhibit 3-3 and Exhibit 3-4. Exhibit 3-5 through 
Exhibit 3-7 demonstrate the ambient condition sensitivity impacts on TPC, LCOE, and COC.  
Exhibit 3-1. Ambient condition (elevation, temperature, and humidity) impacts on combustion turbine output  
 
 
b As many indices provide reference data at a variety of granularities, the CEPCI sensitivity is completed at two levels: 1) 
using the final index values (CEPCI) and 2) using more granular index values for equipment, construction labor, buildings, 
and engineering (CEPCI Gran). While many indices, including CEPCI, allow for even further refinement, offering values for 
specific types of equipment (e.g., heat exchangers, pumps, electrical), this study does not include a sensitivity at this 
level of granularity. 
c The COC is calculated using the LCOE from the analogous non-capture case with the same sensitivities applied.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
7 
Exhibit 3-2. Ambient condition (elevation, temperature, and humidity) impacts on bottoming cycle output 
 
 
Exhibit 3-3. Ambient condition NGCC net plant output sensitivity

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
8 
Exhibit 3-4. Ambient condition NGCC net plant efficiency sensitivity 
 
 
Exhibit 3-5. Ambient condition NGCC sensitivity impact on TPC

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
9 
Exhibit 3-6. Ambient condition NGCC sensitivity impact on LCOE 
 
 
Exhibit 3-7. Ambient condition NGCC sensitivity impact on COC 
 
 
The results of the impact of the natural gas price on the base case LCOE and COC are presented 
in Exhibit 3-8 and Exhibit 3-9, respectively.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
10 
Exhibit 3-8. NG price impact on LCOE 
 
 
Exhibit 3-9. NG price impact on COC 
 
 
The results of the impact of the capacity factor on the base case LCOE and COC are presented in 
Exhibit 3-10 and Exhibit 3-11, respectively.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
11 
Exhibit 3-10. Capacity factor impact on LCOE 
 
 
Exhibit 3-11. Capacity factor impact on COC 
 
 
For the finance category, the impact of debt/equity, effective tax rate, interest rate on debt, 
and return on equity parameters on LCOE and COC can be found in Exhibit 3-12 and Exhibit 
3-13, respectively.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
12 
Exhibit 3-12. LCOE sensitivity to debt/equity, effective tax rate, interest rate on debt, and return on equity

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
13 
Exhibit 3-13. COC sensitivity to debt/equity, effective tax rate, interest rate on debt, and return on equity 
 
 
The impact of cost scaling on TPC, LCOE, and COC using several cost indices is provided in 
Exhibit 3-14, Exhibit 3-15, and Exhibit 3-16, respectively.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
14 
Exhibit 3-14. Cost index impact on TPC when adjusting for inflation 
 
 
Exhibit 3-15. Cost index impact on LCOE when adjusting for inflation

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
15 
Exhibit 3-16. Cost index impact on COC when adjusting for inflation 
 
 
The collective results of the construction, ambient conditions, and finance sensitivities on the 
TPC, LCOE, and COC are shown in Exhibit 3-17, Exhibit 3-18, and Exhibit 3-19.  
Exhibit 3-17. Collective construction, ambient conditions, and financial category sensitivities for TPC

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
16 
Exhibit 3-18. Collective construction, ambient conditions, and financial category sensitivities for LCOE   
 
 
Exhibit 3-19. Collective construction, ambient conditions, and financial category sensitivities for COC

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
17 
 
Exhibit 3-20 and Exhibit 3-21 demonstrate the cumulative impact of the sensitivities within each 
category on the LCOE and COC.  
Exhibit 3-20. Cumulative category sensitivities for LCOE

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
18 
Exhibit 3-21. Cumulative category sensitivities for COC 
 
 
Exhibit 3-22, Exhibit 3-23, Exhibit 3-24, and Exhibit 3-25 show the compounding effect of the 
combined best- and worst-case ambient conditions, construction cost considerations, NG price, 
and financial assumptions on the LCOE and COC. The waterfalls illustrate the stepwise impact of 
modifying the base case using the cumulative sensitivity category extremes.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
19 
Exhibit 3-22. Best cumulative LCOE waterfall sensitivity 
 
 
Exhibit 3-23. Best cumulative COC waterfall sensitivity

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
20 
 
Exhibit 3-24. Worst cumulative LCOE waterfall sensitivity 
 
 
Exhibit 3-25. Worst cumulative COC waterfall sensitivity

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
21 
4 SUMMARY 
TEAs of fossil power plants incorporating CO2 capture are published by multiple sources, 
including NETL’s FEB. Cost and performance estimates for a particular technology and plant 
configuration may differ across these studies—and from real-world projects—due to a host of 
factors. Many of those factors are embodied in the design basis assumptions. This Technical 
Note assesses the impact of several of the factor values that can impact a fossil energy plant’s 
cost and performance. 
As shown in Exhibit 4-1, of the individual parameters assessed in this study, the capacity factor 
had the most significant impact on both LCOE and COC, followed by NG price and return on 
equity. While the cost of steel has the next most significant impact on LCOE (followed by labor 
rate, ambient pressure, and interest rate on debt), the labor rate has the next most significant 
impact on COC (followed by seismic zone, interest rate on debt, and ambient pressure). 
Exhibit 4-1. Summary of parameters’ impacts on LCOE and COC 
Parameter  
(Ranked by LCOE Impact) LCOE, % Parameter  (Ranked by COC Impact) COC, % 
Capacity Factor -2 to +78 Capacity Factor -4 to +132 
Natural Gas Price -25 to +37 Natural Gas Price -9 to +14 
Return on Equity -3 to +8 Return on Equity -5 to +14 
Cost of Steel -2 to +6 Labor Rate -5 to +9 
Labor Rate -2 to +5 Seismic Zone 0 to +10 
Ambient Pressure 0 to +6 Interest Rate on Debt -1 to +9 
Interest Rate on Debt -1 to +5 Ambient Pressure 0 to +10 
Seismic Zone 0 to +5 Cost of Steel -2 to +7 
 
In terms of aggregate sensitivity categories, Exhibit 4-2 shows that the capacity factor and NG 
price sensitivities’ impact on LCOE exceeded the cumulative impact of each of construction 
costs, financial parameters, and ambient conditions. However, while the capacity factor 
sensitivity impact on COC also exceeded the cumulative impacts of each of construction costs, 
financial parameters, and ambient conditions, the NG price sensitivity impact on COC only 
exceeded the cumulative impact of ambient conditions.  
Exhibit 4-2. Summary of aggregate sensitivity categories’ impacts on LCOE and COC 
Parameter (Ranked by LCOE Impact) LCOE, % Parameter (Ranked by COC Impact) COC, % 
Capacity factor -2 to +78 Capacity Factor -4 to +132

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
22 
Parameter (Ranked by LCOE Impact) LCOE, % Parameter (Ranked by COC Impact) COC, % 
Natural Gas Price -25 to +37 Cumulative Construction Costs -9 to +55 
Cumulative Construction Costs -5 to +28 Cumulative Financial Parameters -9 to +33 
Cumulative Financial Parameters -5 to +19 Natural Gas Price -9 to +14 
Cumulative Ambient Conditions -2 to +8 Cumulative Ambient Conditions -1 to +10 
 
While plausible ranges were selected for each factor, it is unlikely that the extreme values—high 
or low—would coincide simultaneously. Nevertheless, a combination of the extremes illustrates 
the importance of careful, collective consideration of these parameters for a given application. 
When the cumulative impacts of all the factors are assessed together, LCOE ranges from -38 to 
285 percent, and the impact to COC ranges from -30 to 427 percent relative to the base case. 
The low end of the cumulative sensitivity is designated as the best case, and the high end of the 
cumulative sensitivity is designated as the worst case. It is evident that the assumptions of the 
B31B.95 base case are collectively favorable to a low LCOE—within the uncertainly range  
(-15/+25 percent) for the majority of the sensitivities.d 
Certain market factors could incentivize plants in more adverse situations, such as financial 
structure, local fuel and electricity markets, geographic isolation, necessity for reliable power, or 
government incentives. There are additional factors that can affect the cost of a plant that are 
not quantitatively addressed in this study, such as construction delays or severe weather events, 
that can lead to further escalating costs. 
The assumptions made in a TEA have a significant impact on cost and performance results, 
beyond the reported accuracy of the particular study. This work emphasizes the need to take 
study assumptions into account when comparing estimates from different sources and when 
using study results for research purposes, feasibility studies, energy system modeling, etc. This 
work also emphasizes the need to complete detailed, site-specific front-end engineering design 
studies to obtain accurate performance and cost estimates for real projects.  
 
d The only outlier being the cost of natural gas, where a cost of $1.90/GJ can decrease the LCOE by -25 percent.

EXAMINATION OF FACTORS AFFECTING THE COST AND PERFORMANCE OF A NATURAL 
GAS COMBINED CYCLE EQUIPPED WITH CARBON DIOXIDE CAPTURE 
23 
5 REFERENCES 
AACE. (2003). Conducting Technical and Economic Evaluations – As Applied for the 
Process and Utility Industries; TCM Framework: 3.2 – Asset Planning, 3.3 Investment 
Decision Making. AACE International. Retrieved November 20, 2013, from 
http://www.aacei.org/non/rps/16R-90.pdf 
AACE. (2005). Cost Estimate Classification System – As Applied in Engineering, 
Procurement, and Construction for the Process Industries; TCM Framework 7.3 – 
Cost Estimating and Budgeting. AACE International. Retrieved November 20, 
2013, from http://www.aacei.org/non/rps/18R-97.pdf 
EIA. (2016). Capital Cost Estimated for Utility Scale Electricity Generating Plants. U.S. 
Energy Information Adminstration. 
Lazard. (2018). Lazard's Levelized Cost of Energy Analysis - Version 12.0. Lazard. 
NCEI. (n.d.-a). Climate-at-a-Glance: Statewide Mapping. (National Centers 
Environmental Information) Retrieved July 18, 2022, from 
https://www.ncei.noaa.gov/access/monitoring/climate-at-a-
glance/statewide/mapping 
NCEI. (n.d.-b). Comparative Climatic Data. Observed Data (CCD): Average Relative 
Humidity: Morning (M), Afternoon (A). (National Centers Environmental 
Information) Retrieved July 18, 2022, from 
https://www.ncei.noaa.gov/products/land-based-station/comparative-climatic-
data 
NETL. (2019-a). Quality Guidelines for Energy System Studies: Capital Cost Scaling 
Methodology: Revision 4 Report. Pittsburgh: U.S. Department of Energy. 
NETL. (2019-b). Quality Guidelines for Energy System Studies: Cost Estimation 
Methodology for NETL Assessments of Power Plant Performance. Pittsburgh, PA: 
U.S. Department of Energy. 
NETL. (2022-a). Cost and Performance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity, Revision 4a. Pittsburgh, PA: U.S. 
Department of Energy. 
NETL. (2022-b). Cost and Performance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity. Pittsburgh, PA: U.S. Department of 
Energy. 
USGS. (2005). Elevation and Distances in the United States. United States Geological 
Survey. 
Wood Group. (2018). Assessing the Cost Reduction Potential and Competitiveness of 
Novel (Next Generation) UK Carbon Capture Technology.

www.netl.doe.gov 
Albany, OR • Houston, TX • Morgantown, WV • Pittsburgh, PA  
(800) 553-7681
