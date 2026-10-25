---
source_id: "netl"
title: "Cost and Performance of Retrofitting NGCC Units for Carbon Capture Rev3 2023"
summary: "NETL report (rev. 3, 2023) on the cost and performance of retrofitting existing natural gas combined cycle units for CO2 capture, including capture rates above 95%."
url: "https://www.netl.doe.gov/projects/files/CostandPerformanceofRetrofittingNGCCUnitsforCarbonCaptureRevision3_053123.pdf"
retrieved_at: "2026-10-24T04:53:06+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "CCS", "H2", "PWR"]
disciplines: ["PRC", "MAT"]
sha256: "4243e7a57204a7737cabc37c4bf046b41fd78e496a57c5e04e2d1999166c3e5f"
collected: "manual"
---

# Cost and Performance of Retrofitting NGCC Units for Carbon Capture Rev3 2023

COST AND PERFORMANCE OF 
RETROFITTING NGCC UNITS FOR 
CARBON CAPTURE – REVISION 3 
 
 
 
 
 May 31, 2023 
 
DOE/NETL-2023/3848

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

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
 
 
 
Tommy Schmitt1,2: Methodology, Software, Formal Analysis, Writing – 
Original Draft, Writing – Review & Editing; Sally Homsy1,2: Software 
Validation, Writing – Review & Editing, Supervision; Hari 
Mantripragada1,2: Writing – Review & Editing; Mark Woods1,2: Writing – 
Review & Editing, Supervision; Hannah Hoffman1,2: Writing – Review & 
Editing; Travis Shultz1: Conceptualization, Writing – Review & Editing; 
Timothy Fout1: Conceptualization, Writing – Review & Editing; Gregory 
Hackett1*: Writing – Review & Editing 
 
1National Energy Technology Laboratory 
2National Energy Technology Laboratory Support Contractor 
*Corresponding contact: Gregory.Hackett@netl.doe.gov 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Suggested Citation: 
NETL, "Cost and Performance of Retrofitting NGCC Units for Carbon Capture – Revision 
3," National Energy Technology Laboratory, May 31, 2023.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
 
 
This page intentionally left blank.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
i  
TABLE OF CONTENTS 
List of Exhibits ............................................................................................................................. ii 
Acronyms and Abbreviations ................................................................................................. iv 
Executive Summary ................................................................................................................. 1 
CO2 Capture Rates Above 95 Percent .............................................................................. 6 
1 Introduction ....................................................................................................................... 7 
1.1 CO2 Capture Rates Above 95 Percent .................................................................... 9 
2 General Evaluation Basis .................................................................................................10 
3 Performance Estimates ...................................................................................................12 
4 Cost Estimates ..................................................................................................................19 
4.1 Greenfield Cost Estimates ........................................................................................19 
4.2 Retrofit Cost Estimates ..............................................................................................21 
4.3 Levelized Cost of Electricity and Other Metrics .....................................................25 
5 Summary Comparison .....................................................................................................28 
6 Conclusion and Future Work ..........................................................................................34 
References ..............................................................................................................................35 
Appendix A: 97 Percent Capture Cases ..............................................................................36 
Appendix B: Cost Estimate Details ........................................................................................42

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
ii  
LIST OF EXHIBITS 
Exhibit ES-1. Case descriptions ................................................................................................ 1 
Exhibit ES-2. Net plant efficiency summary (HHV basis) ........................................................ 2 
Exhibit ES-3. Summary of Levelized Cost of Electricity (LCOE) .............................................. 3 
Exhibit ES-4. Summary cost of CO2 captured ........................................................................ 4 
Exhibit ES-5. Summary cost of CO2 avoided .......................................................................... 4 
Exhibit ES-6. Sensitivity of LCOE to retrofit difficulty factor (RDF) .......................................... 5 
Exhibit 1-1. Case descriptions.................................................................................................. 8 
Exhibit 2-1. Site characteristics ...............................................................................................10 
Exhibit 2-2. Natural gas composition .....................................................................................11 
Exhibit 3-1. Turbine model specifications ..............................................................................13 
Exhibit 3-2. F-frame NGCC plant performance summary ...................................................15 
Exhibit 3-3. H-frame NGCC plant performance summary ...................................................17 
Exhibit 4-1. Summary cost estimate data for F-frame greenfield cases .............................20 
Exhibit 4-2. Summary cost estimate data for H-frame greenfield cases ............................21 
Exhibit 4-3. Summary greenfield equivalent costs of the retrofit equipment .....................22 
Exhibit 4-4. Retrofit scope adjustment factors ......................................................................23 
Exhibit 4-5. Summary costs of the retrofit equipment ...........................................................25 
Exhibit 4-6. Summary LCOE of the retrofit cases ...................................................................26 
Exhibit 5-1. Summary LCOE ....................................................................................................28 
Exhibit 5-2. Summary cost of CO2 captured .........................................................................29 
Exhibit 5-3. Summary cost of CO2 avoided ...........................................................................30 
Exhibit 5-4. Sensitivity of LCOE to natural gas price ..............................................................31 
Exhibit 5-5. Sensitivity of LCOE to capacity factor ................................................................32 
Exhibit 5-6. Sensitivity of LCOE to retrofit difficulty factor (RDF) ...........................................33 
Exhibit A-1. F-frame NGCC plant performance summary ...................................................37 
Exhibit A-2. Summary cost estimate data for F-frame greenfield cases ............................39  
Exh
ibit A-3. Summary costs of retrofit ....................................................................................40 
Exhibit A-4. Summary LCOE of the retrofit cases ..................................................................41 
Exhibit B-1. B31A-BR.90 capital costs .....................................................................................43 
Exhibit B-2. B31A-BR.90 owner’s costs ....................................................................................45 
Exhibit B-3. B31A-BR.90 O&M costs ........................................................................................46 
Exhibit B-4. B31A-BR.95 capital costs .....................................................................................47 
Exhibit B-5. B31A-BR.95 owner’s costs ....................................................................................49 
Exhibit B-6. B31A-BR.95 O&M costs ........................................................................................50 
Exhibit B-7. B31A-BR.97 capital costs .....................................................................................51 
Exhibit B-8. B31A-BR.97 owner’s costs ....................................................................................53 
Exhibit B-9. B31A-BR.97 O&M costs ........................................................................................54 
Exhibit B-10. B32A-BR.90 capital costs ...................................................................................55 
Exhibit B-11. B32A-BR.90 owner’s costs ..................................................................................57 
Exhibit B-12. B32A-BR.90 O&M costs ......................................................................................58 
Exhibit B-13. B32A-BR.95 capital costs ...................................................................................59 
Exhibit B-14. B32A-BR.95 owner’s costs ..................................................................................61 
Exhibit B-15. B32A-BR.95 O&M costs ......................................................................................62 
Exhibit B-16. B32A-BR.97 capital costs ...................................................................................63 
Exhibit B-17. B32A-BR.97 owner’s costs ..................................................................................65

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
iii  
Exhibit B-18. B32A-BR.97 O&M costs ......................................................................................66

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
iv  
ACRONYMS AND ABBREVIATIONS 
A# Cost account number 
AGR Acid gas removal 
Ar Argon 
Aspen Aspen Plus® 
BAU Business as usual 
BEC Bare erected cost 
BOP Balance of plant 
Btu British thermal unit 
C2H6 Ethane 
C3H8 Propane 
C4H10 n-Butane 
CCS Carbon capture and storage 
CF Capacity factor 
CH4 Methane 
CH4S Methanethiol 
Circ. Circulating 
CO2 Carbon dioxide 
COE Cost of electricity 
CRF Capital recovery factor 
DOE Department of Energy 
Eng'g CM, H.O. & Fee  
Engineering, Construction 
Management, Home Office, 
& Fees  
FEBRev4a  Cost and Performance Baseline 
for Fossil Energy Plants 
Volume 1: Bituminous Coal 
and Natural Gas to Electricity 
– Revision 4a 
FO Fuel oil 
ft Foot 
GHG Greenhouse gas  
GJ Gigajoule 
gpm Gallons per minute 
GT Gas turbine 
H2O Water 
H2S  Hydrogen sulfide 
HHV Higher heating value 
h, hr Hour 
HRSG Heat recovery steam 
generator 
HVAC Heating, ventilating, and air 
conditioning 
I&C Instrumentation and control 
IEA International Energy Agency  
IOU Investor-owned utility 
IP Intermediate pressure 
kg Kilogram 
kJ Kilojoules 
kW, kWe Kilowatt electric 
kWh Kilowatt-hour 
kWt Kilowatt thermal 
lb Pound 
LCOE             Levelized cost of electricity 
LHV Lower heating value 
LP Low pressure 
m Meter 
m3/min Cubic meter per minute 
MJ/scm M egajoule per standard cubic 
meter 
MMBtu Million British thermal units (also 
shown as 106 Btu) 
MPa M egapascal 
MPC Makeup power cost 
MW, MWe Megawatt electric 
MWh Megawatt-hour 
N/A Not available/applicable 
N2 Nitrogen 
NETL National Energy Technology 
Laboratory 
NG Natural gas 
NGCC N atural gas combined cycle 
O2 Oxygen 
O&M Operation and maintenance 
PC Pulverized coal 
psia Pounds per square inch 
absolute 
psig Pounds per square inch gauge 
PSP Projected sales price 
QGESS Quality Guidelines for Energy 
System Studies 
RDF Retrofit difficulty factor 
RET Retrofit 
SC Supercritical 
scf Standard cubic foot 
SCR Selective catalytic reduction 
SOA State-of-the-art 
ST Steam turbine

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
v  
T&S Transport and storage 
TASC Total as-spent cost 
TOC Total overnight cost 
tonne Metric ton (1000 kg) 
TPC Total plant cost 
U.S.  United States 
y, yr Year 
°C Degrees Celsius 
°F Degrees Fahrenheit

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
1 
EXECUTIVE SUMMARY 
The purpose of this study is to present the cost and performance of retrofitting natural gas 
combined cycle (NGCC) power plants with commercial, state-of-the-art (SOA), solvent-based 
post-combustion carbon capture. The cases presented in this report are analogous to greenfield 
cases reported in the National Energy Technology Laboratory’s (NETL) “Cost and Performance 
Baseline for Fossil Energy Plants Volume 1: Bituminous Coal and Natural Gas to Electricity – 
Revision 4a”, hereafter referred to as FEBRev4a. [1] Cases are developed for NGCC plants with 
SOA F-frame and H-frame turbines with the case designations being listed in Exhibit ES-1. For 
the retrofit (brownfield) cases, it is assumed that the existing plant has been fully paid off, and 
the only capital outlay required is that for the capture process and associated modifications to 
the existing plant. The post-combustion carbon dioxide (CO2) capture system performance and 
costs are based on data from quotes; details can be found in FEBRev4a. The naming convention 
used follows previous naming conventions presented in FEBRev4a. For retrofit cases, the “-BR” 
designation represents that the base plant without capture (B31A or B32A) has now been 
retrofitted (R) with capture (B). 
Exhibit ES-1. Case descriptions 
CaseA Plant Type Steam Cycle, psig/°F/°F Combustion Turbine CO2 Separation Capture Rate Plant Type 
B31A 
F-frame 
NGCC 2378/1085/1084 
2× State-of-the-
art 2017  
F-frame 
N/A N/A Greenfield 
B31B.90 
Shell’s 
CANSOLV 
Process 
90% Greenfield 
B31B.95 95% Greenfield 
B31A-BR.90 90% Brownfield 
B31A-BR.95 95% Brownfield 
B32A 
H-frame 
NGCC 2668/1085/1044 
2× State-of-the-
art 2017  
H-frame 
N/A N/A Greenfield 
B32B.90 
Shell’s 
CANSOLV 
Process 
90% Greenfield 
B32B.95 95% Greenfield 
B32A-BR.90 90% Brownfield 
B32A-BR.95 95% Brownfield 
Al plants in this report are assumed to be located at a generic plant site in the midwestern United States 
The net plant efficiencies, based on the higher heating value (HHV), for NGCC plants with and 
without CO2 capture for each turbine type are illustrated in Exhibit ES-2. The lightly colored 
efficiencies represent those associated with greenfield cases while the darker colored 
efficiencies represent the brownfield cases. The capture system performance for a given turbine 
size is identical between the greenfield and retrofit cases aside from an off-design performance 
derate due to extracting steam prior to the low-pressure steam turbine. For the greenfield 
cases, the low-pressure steam turbine section is sized to account for the upstream steam

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
2 
extraction and does not experience an off-design performance derate. The balance of plant 
performance remains consistent with the greenfield assumptions. 
Exhibit ES-2. Net plant efficiency summary (HHV basis) 
 
The levelized cost of electricity (LCOE) for retrofitting the NGCC plants with CO2 capture for each 
turbine type is illustrated in Exhibit ES-3. The estimated LCOE values for the non-capture cases 
(assuming the existing plant is fully paid off) are also included in the chart for comparison. 
When comparing H-frame turbines to F-frame turbines in NGCC applications, overall plant 
efficiency increases while plant output also increases, decreasing LCOE, which is consistent with 
changes resulting from the economies of scale. The annual fuel cost makes up the largest 
portion of the annual operating costs. The total annual fuel cost remains the same for each 
turbine type before and after retrofit, but the cost per MWh increases after retrofitting due to 
the decrease in net power generation. Note that the 30-year levelized natural gas price was 
assumed to be $4.42/MMBtu as specified in “QGESS: Fuel Prices for Selected Feedstocks in 
NETL Studies” for natural gas delivered to large, combined cycle plants operating at high 
capacity factors in the Midwest. [2]

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
3 
Exhibit ES-3. Summary of Levelized Cost of Electricity (LCOE) 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. Cases B31A and B32A in this chart do not 
include capital costs, as to represent the plant prior to retrofit (i.e., capital costs are paid off) 
The cost of CO2 captured, and the cost of CO2 avoided are shown in Exhibit ES-4 and Exhibit ES-5 
for each case. These parameters are explained in detail in Section 4.3, but it should be noted 
the calculation for greenfield and retrofit applications differs. As the turbine design improves 
(increases in efficiency), the cost of CO2 captured and cost of CO2 avoided decrease. The 
inclusion of higher capture rates does not have a significant impact on the cost of CO2 captured 
or avoided, indicating that the incremental cost of achieving higher capture rates is offset by the 
additional CO2 captured. 
 
21.3 21.8 20.1 20.6
11.8 12.3 10.2 10.7
3.6
7.4 7.6
3.5
6.8 7.0
7.6 7.8 7.1 7.2
1.7
4.0 4.1
1.7
3.8 3.9
4.1 4.3 3.9 4.028.1
31.7 31.9
27.4
30.8 31.0
31.9 32.1
30.9 31.2
3.5 3.7
3.4 3.6
3.5 3.7
3.4 3.6
4.0 4.3
3.9 4.1
33.4
67.9 69.1
32.6
64.9 66.0
63.0 64.5
59.5 60.9
0
10
20
30
40
50
60
70
80
90LCOE [including T&S], $/MWh
MPC CO₂ T&S
Fuel Variable
Fixed Capital

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
4 
Exhibit ES-4. Summary cost of CO2 captured 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. B31A is used as a reference for all F-
frame retrofit case calculations. B32A is used as a reference for all H-frame retrofit case calculations. 
Exhibit ES-5. Summary cost of CO2 avoided 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. B31A is used as a reference for all F-
frame retrofit case calculations. B32A is used as a reference for all H-frame retrofit case calculations. 
32.8 32.3 29.7 29.3 33.7 33.1 30.2 29.7
11.0 10.8
9.8 9.7
10.2 10.0
9.1 8.9
6.7 6.6
6.3 6.2
6.3 6.2
5.9 5.8
10.3 10.3
10.0 10.0
11.5 11.5
11.5 11.5
60.7 59.9
55.9 55.2
61.8 60.8
56.7 55.9
0
10
20
30
40
50
60
70
80
90
B31B.90 B31B.95 B32B.90 B32B.95 B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95
Cost of CO2 Captured [excluding T&S], $/tonne
MPC
Fuel
Variable
Fixed
Capital
37.5 36.9 33.9 33.3 33.7 33.1 30.2 29.7
12.5 12.3
11.2 11.0 10.2 10.0
9.1 8.9
7.7 7.5
7.2 7.1 6.3 6.2
5.9 5.8
11.7 11.7
11.4 11.4
11.4 11.4
11.4 11.4
10.0 10.0
10.0 10.0
11.5 11.5
11.5 11.5
80.8 79.8
75.0 74.2 71.8 70.8
66.7 65.9
0
10
20
30
40
50
60
70
80
90
B31B.90 B31B.95 B32B.90 B32B.95 B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95
Cost of CO2 Avoided [includingT&S], $/tonne
MPC CO₂ T&S
Fuel Variable
Fixed Capital

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
5 
CO2 emissions from current SOA F-frame turbines and H-frame turbines in non-capture NGCC 
configurations for cases B31A and B32A are estimated at 741 lb/MWhgross and 723 lb/MWhgross, 
respectively. The modeled capture systems were designed for 90 and 95 percent CO2 capture 
from the flue gas. This results in a CO2 emission rate ranging 40–80 lb/MWhgross in F-frame cases 
and 39–78 lb/MWhgross in H-frame cases.  
Retrofit systems are subject to a cost premium relative to equivalent greenfield installations due 
to design, construction, and tie-in constraints imposed by the existing plant layout and 
operation. A retrofit difficulty factor (RDF) of 1.09 is used to account for this cost premium; 
capital costs are estimated by multiplying the RDF by the total plant cost (TPC) of an equivalent 
greenfield installation. A more detailed approach to estimating the total retrofit cost premium 
for brownfield projects would be to apply an RDF to each line item of an equivalent greenfield 
system. These values range 1.0–1.3 as outlined in the Quality Guidelines for Energy System 
Studies (QGESS) for retrofit applications. [3] However, this requires more detailed knowledge of 
the plant layout. The RDF of 1.09 used in this report represents the weighted average of the 
QGESS recommended account-level retrofit difficulty factors for an NGCC plant retrofit with 
post combustion capture. This indicates that $100 of installed greenfield equipment costs $109 
if installed as a retrofit for the configurations presented in this report. The retrofit premium 
estimated by either the detailed or simplified method is within the expected accuracy (-15 
percent/+25 percent for an AACE International Class 4 cost estimate) of the reference NGCC 
plants considered. 
The sensitivity of the LCOE to the single RDF was calculated and is shown in Exhibit ES-6. An RDF 
of 1.3 increases the overall LCOE by $2.8–3.5/MWh versus cases without a premium (RDF=1.0).  
Exhibit ES-6. Sensitivity of LCOE to retrofit difficulty factor (RDF) 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor 
50
55
60
65
70
75
 1.00  1.05  1.10  1.15  1.20  1.25  1.30
LCOE [including T&S], $/MWh
Retrofit Difficulty Factor
B31A-BR.90
B31A-BR.95
B32A-BR.90
B32A-BR.95
Retrofit Difficulty Factor = 1.09

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
6 
The conclusions of this study apply only to this level of conceptual design and economic 
analysis. Further analysis is needed for costing actual retrofit plant designs. Site and plant 
design-specific considerations (seismic conditions, water quality, local labor costs, local 
environmental regulations, etc.) are not included in this analysis. A more detailed analysis 
should explore scenarios where the existing capital costs are not zero at the time of retrofitting. 
In addition, the plant performance of today’s SOA F-class or H-class NGCC plants may or may 
not reflect the plant performance of existing NGCC plants that are candidates for capture 
retrofit. A more detailed analysis should also identify the combustion turbine types and vintages 
that represent sunk assets existing in the current fleet and apply today’s SOA capture system 
performance and cost as a retrofit to further refine the cost of capture. Finally, this study does 
not consider any upgrades or maintenance (outside of typical maintenance costs included in 
operation and maintenance) that may be necessary to extend the life of the plant such that it 
remains online for the 30-year duration estimated for the LCOE.  
CO2 CAPTURE RATES ABOVE 95 PERCENT 
Commercial-scale demonstration of solvent-based post-combustion CO2 capture systems at 
power generation facilities (specifically pulverized coal [PC] plants) has shown the ability to 
capture 90 percent of the CO2 in the flue gas stream. Moreover, field-testing of post-combustion 
CO2 capture technology as well as vendor and industry feedback on projects currently in the 
planning stages (including front-end engineering and design projects sponsored by the 
Department of Energy [DOE]) indicates that capture rates as high as 95 percent are feasible for 
both coal- and natural gas-fueled electricity generating units. Given the breadth of publicly 
available information supporting the capability for post-combustion capture systems to remove 
greater than 90 percent of the CO2 in the treated stream, cases for 90 percent and 95 percent 
capture on NGCC are presented in the main body of this report. 
It should be emphasized that technology suppliers (as reflected in vendor-supplied information 
provided to DOE that included cost and performance estimates for >95 percent carbon capture 
and storage [97 percent for NGCC and 99 percent for PC] study cases) as well as subject matter 
experts acknowledge and support that solvent-based post-combustion CO2 capture 
technologies are capable of achieving CO2 removal rates beyond 95 percent on low-purity 
streams representative of fossil-fueled combustion. Although techno-economic analyses of 
deep decarbonization (≥ 99 percent) of combustion flue gas have been published by others, the 
relatively limited experience with design and operation of capture systems that can routinely, 
reliably, and economically achieve very high removal rates requires further study. Techno-
economic analysis of the higher capture rate (97 percent for NGCC) is included as Appendix A.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
7 
1 INTRODUCTION 
This analysis is an evaluation of the cost and performance associated with retrofitting natural 
gas combined cycle (NGCC) plants for carbon capture and storage (CCS). The analysis is based on 
two previous National Energy Technology Laboratory (NETL) studies:  
• Cost and Performance Baseline for Fossil Energy Plants Volume 1: Bituminous Coal and 
Natural Gas to Electricity – Revision 4a, October 2022. [1] 
This report presents techno-economic assessment results for greenfield NGCC plants, 
with state-of-the-art (SOA) F-frame and H-frame turbines, with and without CCS.  Among 
other modifications, updated performance and costs based on a 2021 vendor quote for 
the capture system are reported in this revision of the report. Hereafter, this report is 
referenced as FEBRev4a. 
• Cost and Performance of Retrofitting NGCC Units for Carbon Capture – Revision 2, 
December 2020. [4] 
This report represents the most recent study of NGCC units retrofit with carbon capture 
and is based on a prior revision (Revision 4) of FEBRev4a. This report was compiled for 
internal use only. 
NGCC models were developed for greenfield cases in FEBRev4a using Aspen Plus® (Aspen) v10. 
[1] These models were modified to include case switching features for retrofit parameters, 
primarily consisting of a steam turbine derate, as outlined in Section 3. The derate is due to the 
off-design performance of the low-pressure (LP) section of the steam turbine. The reason for 
this is the lower inlet steam flow rate due to the extraction of steam for the capture system 
reboiler between the LP and intermediate-pressure (IP) sections of the turbine. 
The NGCC cases included in this study were based on two gas turbine designs: F-frame (7FA.05) 
and H-frame (7HA.02). Each turbine was modeled in three greenfield configurations—without 
carbon dioxide (CO2) capture and with 90 and 95 percent CO2 capture—and two retrofit 
(brownfield) configurations-with 90 and 95 percent CO2 capture. The case designations are 
listed in Exhibit 1-1. Each case was modeled as a 2×2×1 power system (two gas turbines, two 
heat recovery steam generators [HRSG], and one steam turbine). The naming convention used 
follows previous naming conventions presented in FEBRev4a. For retrofit cases, the “-BR” 
designation represents that the base plant without capture (B31A or B32A) has now been 
retrofitted (R) with capture (B).

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
8 
Exhibit 1-1. Case descriptions 
CaseA Plant Type Steam Cycle, psig/°F/°F Combustion Turbine CO2 Separation Capture Rate Plant Type 
B31A 
F-frame 
NGCC 2378/1085/1084 
2× State-of-the-
art 2017  
F-Class 
N/A N/A Greenfield 
B31B.90 
Shell’s 
CANSOLV 
Process 
90% Greenfield 
B31B.95 95% Greenfield 
B31A-BR.90 90% Brownfield  
B31A-BR.95 95% Brownfield 
B32A 
H-frame 
NGCC 2668/1085/1044 
2× State-of-the-
art 2017  
H-Class 
N/A N/A Greenfield 
B32B.90 
Shell’s 
CANSOLV 
Process 
90% Greenfield 
B32B.95 95% Greenfield 
B32A-BR.90 90% Brownfield 
B32A-BR.95 95% Brownfield 
Al plants in this report are assumed to be located at a generic plant site in the midwestern United States 
Cost estimates were developed for each turbine configuration as greenfield installations. In 
addition, the cost of retrofitting the non-capture case for each turbine type to include 90 and 95 
percent capture was estimated. The greenfield cost estimation methodology (including 
contingencies, owners’ costs, capital recovery factors [CRF], and levelized cost of electricity 
[LCOE] equations) is described in the NETL Quality Guidelines for Energy System Studies 
(QGESS) report “Cost Estimation Methodology for NETL Assessments of Power Plant 
Performance.” [5] The capital and operating and maintenance (O&M) costs for greenfield cases 
are presented in FEBRev4a. For the retrofit cases, it is assumed that the existing plant has been 
fully paid off, and the only capital outlay required is that for the capture process and associated 
modifications to the existing plant (excluding life-extension costs). Otherwise, costs were scaled 
as needed using the methodology specified for NGCC plants in “QGESS: Capital Cost Scaling 
Methodology: Revision 4 Report.” [6] The 30-year levelized natural gas price was assumed to be 
$4.42/MMBtu as specified in “QGESS: Fuel Prices for Selected Feedstocks in NETL Studies” for 
natural gas delivered to large, combined cycle plants operating at high capacity factors in the 
Midwest. [2] The costs of CO2 transport and storage (T&S) are specified in “QGESS: Carbon 
Dioxide Transport and Storage Costs in NETL Studies.” [7] The cost premiums associated with 
retrofitting an existing plant are specified in “QGESS: Carbon Capture Retrofit Studies.” [3] 
Owners’ costs (which are added to the total plant cost [TPC] to calculate the total overnight cost 
[TOC]) for the retrofitted cases were calculated based only on the additional retrofitted 
equipment and capital charges and the increase in consumables and other O&M above existing 
plant values.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
9 
1.1 CO2 CAPTURE RATES ABOVE 95 PERCENT 
Commercial-scale demonstration of solvent-based post-combustion CO2 capture systems at 
power generation facilities (specifically pulverized coal [PC] plants) has shown the ability to 
capture 90 percent of the CO2 in the flue gas stream. Moreover, field-testing of post-combustion 
CO2 capture technology as well as vendor and industry feedback on projects currently in the 
planning stages (including front-end engineering and design projects sponsored by the 
Department of Energy [DOE]) indicates that capture rates as high as 95 percent are feasible for 
both coal- and natural gas-fueled electricity generating units. Given the breadth of publicly 
available information supporting the capability for post-combustion capture systems to remove 
greater than 90 percent of the CO2 in the treated stream, cases for 90 percent and 95 percent 
capture on NGCC are presented in the main body of this report. 
It should be emphasized that technology suppliers (as reflected in vendor-supplied information 
provided to DOE that included cost and performance estimates for > 95 percent CCS [97 percent 
for NGCC and 99 percent for PC] study cases) as well as subject matter experts acknowledge and 
support that solvent-based post-combustion CO2 capture technologies are capable of achieving 
CO2 removal rates beyond 95 percent on low-purity streams representative of fossil-fueled 
combustion. Although techno-economic analyses of deep decarbonization (≥ 99 percent) of 
combustion flue gas have been published by others, the relatively limited experience with 
design and operation of capture systems that can routinely, reliably, and economically achieve 
very high removal rates requires further study. Techno-economic analysis of the higher capture 
rate (97 percent for NGCC) is included as Appendix A.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
10 
2 GENERAL EVALUATION BASIS 
The design criteria are identical to those used in FEBRev4a. All plants in this study are assumed 
to be located at a generic plant site in the midwestern United States, with site characteristics 
and ambient conditions as summarized in Exhibit 2-1.  The ambient conditions are the same as 
International Organization for Standardization conditions. An 85 percent capacity factor was 
selected for all cases. More detailed design criteria for the present study are outlined in the 
“Quality Guidelines for Energy System Studies (QGESS): Process Modeling Design Parameters”. 
[8] The natural gas composition is specified in “QGESS: Specification for Selected Feedstocks” 
and is summarized in Exhibit 2-2. [9]  
Exhibit 2-1. Site characteristics 
Parameter Value 
Location Midwestern U.S. 
Topography Level 
Size, acres 100 
Transportation Rail or Highway 
Water 50% Municipal and 50% Ground Water 
Elevation, m (ft) 0 (0) 
Barometric Pressure, MPa (psia) 0.101 (14.696) 
Average Ambient Dry Bulb Temperature, °C (°F) 15 (59) 
Average Ambient Wet Bulb Temperature, °C (°F) 10.8 (51.5) 
Design Ambient Relative Humidity, % 60 
Cooling Water Temperature, °C (°F)A 15.6 (60) 
Air composition based on published psychrometric data, mass % 
N2 75.055 
O2 22.998 
Ar 1.280 
H2O 0.616 
CO2 0.050 
Total 100.00 
AThe cooling water temperature is the cooling tower cooling water exit temperature. This is set to 4.8°C (8.5°F) above 
ambient wet bulb conditions in International Organization for Standardization cases

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
11 
 
Exhibit 2-2. Natural gas composition 
Component Volume Percentage 
Methane CH4 93.1 
Ethane C2H6 3.2 
Propane C3H8 0.7 
n-Butane  C4H10 0.4 
Carbon Dioxide CO2 1.0 
Nitrogen N2 1.6 
MethanethiolA CH4S 5.75x10-6 
  Total 100.0 
  LHV HHV 
kJ/kg (Btu/lb) 47,201 (20,293) 52,295 (22,483) 
MJ/scm (Btu/scf) 34.52 (927) 38.25 (1,027) 
AThe sulfur content of natural gas is primarily composed of added mercaptan (methanethiol [CH4S]) with trace 
levels of hydrogen sulfide (H2S)  
Note: Fuel composition is normalized, and heating values are calculated using Aspen

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
12 
3 PERFORMANCE ESTIMATES 
Steady state models for each case were developed using Aspen v10. The turbine model 
specifications are presented in Exhibit 3-1. Since NGCC net power output is determined by the 
turbine type and configuration selected, the natural gas flow differs between F-frame and H-
frame cases but remains constant in relation to the combustion turbine size (i.e., capture and 
non-capture cases have the same natural gas flow rate). In comparison to the previous report, 
[4] the most notable adjustments made were to reflect current post-combustion capture 
technology information as outlined in a 2021 vendor quote. The addition of post-combustion 
capture reduces the quantity of steam available to generate power in the LP turbine section as 
well as increases the cooling water required and overall water usage.  
The retrofit case performance for each turbine type was assumed to be identical to the 
greenfield capture case performance except for an off-design efficiency penalty applied to the 
steam turbine due to the throttled steam extraction upstream from the existing plant LP turbine 
stage resulting in operation at a significantly reduced flow relative to the full design flow. This 
causes a derate not only based on lower power production from decreased flow to the steam 
turbine, but also an additional derate due to an efficiency penalty caused by off-design flow to 
the steam turbine. 
The additional off-design efficiency penalty is a function of the percentage of steam extracted 
from the IP-LP crossover and is, therefore, a function of the capture system reboiler duty. The 
off-design steam turbine derate was calculated using data from the Lucquiaud et al. study, 
which was verified against published data from the International Energy Agency (IEA) 
greenhouse gas (GHG) study involving a collaboration between Alstom Power, Mitsui Babcock, 
Fluor, and Imperial College. [10, 11, 12] For 90 percent capture cases, the steam turbine derate 
was based on the ratio of the Lucquiaud et al.-reported steam turbine gross output for a 
throttled LP turbine due to CCS retrofit to the steam turbine gross output of a greenfield plant 
with CCS. The derate for higher capture cases was then scaled based on the linear relationship, 
reported by Lucquiaud et al., of steam turbine efficiency to the percent of steam extracted for a 
throttled LP turbine. This methodology remains consistent with previous iterations of this report 
for 90 percent capture, with slight adjustments for higher capture rates based on the 
assumption that greater steam extraction at higher capture rates will lead to increased off-
design efficiency penalties in the LP section of the steam turbine. The resulting derates range 
2.05–2.15 percent gross power in the steam turbine section for 90–95 percent capture from an 
NGCC system. 
The linear relationship of the off design derate can be approximated by: 
Steam turbine gross power derate = 0.0187 ∗ 𝐴𝐴 𝐵𝐵 + 0.0018 
for capture rates between 90 and 95 percent, where: 
A = Steam flow rate extracted prior to the LP steam turbine for the desired capture rate, lb/h 
B = Steam flow rate extracted prior to the LP steam turbine for the reference 90 percent 
capture case, lb/h 
The resulting value is then applied as a fractional decrease in the steam turbine gross power.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
13 
Exhibit 3-1. Turbine model specifications 
Case 
Turbine Technology Steam Cycle, psig/°F/°F Efficiency  (% HHV/LHV) 2×GT (MWe) ST (MWe)A Gross (MWe) Aux (MWe) Net (MWe) 
1 
SOA 
Based on F-frame 
B31A w/o CO2 capture 
2378/1085/1084 
53.6/59.4 477 263 740 14 727 
B31B.90 w/CO2 capture 47.6/52.7 477 215 692 47 645 
B31B.95 w/CO2 capture 47.3/52.4 477 212 690 49 640 
B31A-BR.90 w/CO2 capture retrofit 47.3/52.4 477 211 688 47 641 
B31A-BR.95 w/CO2 capture retrofit 46.9/52.0 477 208 685 49 636 
2 
SOA 
Based on H-frame 
B32A w/o CO2 capture 
2668/1085/1044 
55.1/61.0 686 324 1,009 17 992 
B32B.90 w/CO2 capture 49.0/54.3 686 260 945 62 883 
B32B.95 w/CO2 capture 48.7/54.0 686 256 942 65 877 
B32A-BR.90 w/CO2 capture retrofit 48.7/54.0 686 255 940 62 878 
B32A-BR.95 w/CO2 capture retrofit 48.4/53.6 686 251 936 65 872 
A Steam turbine value includes derate for off-design LP operation

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
14 
The models include Shell’s CANSOLV solvent-based chemical absorption process for CO2 capture 
as outlined and applied to NGCC cases in FEBRev4a. The performance results are listed in 
Exhibit 3-2 and Exhibit 3-3 for each turbine type and retrofit application.  
The performance of the greenfield and retrofit applications is nearly identical except for the 
addition of the LP steam turbine off-design efficiency penalty. This efficiency penalty reduces 
power generation in the steam turbine by about 4–5 MWe (about 2 percent of the steam 
turbine gross power output or less than 1 percent of net power). Overall steam cycle efficiency 
is reduced by about 1.0 percentage point in retrofit applications and HHV net plant efficiency is 
reduced by about 0.3 percentage points. The raw water withdrawal and consumption, shown in 
Exhibit 3-2 and Exhibit 3-3, remain constant between cases of similar turbine type but appear to 
increase in retrofit applications due to the reduction in net power causing the normalized water 
usage to increase.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
15 
Exhibit 3-2. F-frame NGCC plant performance summary 
Case 
7FA.05 
Without Capture 
(B31A) 
7FA.05 
with 90% Capture 
(B31B.90) 
7FA.05 
with 95% 
Capture 
(B31B.95) 
7FA.05 
Retrofitted with 
90% Capture 
(B31A-BR.90) 
7FA.05 
Retrofitted with 
95% Capture 
(B31A-BR.95) 
Plant Output 
Gas Turbine Power, MWe 477 477 477 477 477 
Steam Turbine Power, MWe 263 215 212 211 208 
Total, MWe 740 692 690 688 685 
Auxiliary Load 
Circulating Water Pumps, kWe 2,820 4,340 4,360 4,340 4,360 
Combustion Turbine Auxiliaries, kWe 1,020 1,020 1,020 1,020 1,020 
Condensate Pumps, kWe 150 170 170 170 170 
Cooling Tower Fans, kWe 1,460 2,240 2,260 2,240 2,260 
CO₂ Capture/Removal Auxiliaries, kWe – 13,600 14,400 13,600 14,400 
CO₂ Compression, kWe – 17,900 18,900 17,900 18,900 
Feedwater Pumps, kWe 4,830 4,830 4,830 4,830 4,830 
Ground Water Pumps, kWe 260 400 410 400 410 
Miscellaneous Balance of PlantA, kWe 570 570 570 570 570 
SCR, kWe 2 2 2 2 2 
Steam Turbine Auxiliaries, kWe 200 200 200 200 200 
Transformer Losses, kWe 2,250 2,220 2,220 2,210 2,200 
Total Auxiliaries, MWe 14 47 49 47 49 
Net Plant Power, MWe 727 645 640 641 636 
Plant Performance 
HHV Net Plant Efficiency, % 53.6% 47.6% 47.3% 47.3% 46.9% 
HHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 6,714 (6,363) 7,563 (7,169) 7,617 (7,220) 7,615 (7,218) 7,671 (7,270)

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
16 
Case 
7FA.05 
Without Capture 
(B31A) 
7FA.05 
with 90% Capture 
(B31B.90) 
7FA.05 
with 95% 
Capture 
(B31B.95) 
7FA.05 
Retrofitted with 
90% Capture 
(B31A-BR.90) 
7FA.05 
Retrofitted with 
95% Capture 
(B31A-BR.95) 
Plant Performance (continued) 
HHV Combustion Turbine Efficiency, % 35.2% 35.2% 35.2% 35.2% 35.2% 
LHV Net Plant Efficiency, % 59.4% 52.7% 52.4% 52.4% 52.0% 
LHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 6,060 (5,743) 6,827 (6,470) 6,875 (6,516) 6,873 (6,515) 6,924 (6,562) 
LHV Combustion Turbine Efficiency, % 39.0% 39.0% 39.0% 39.0% 39.0% 
Steam Turbine Cycle Efficiency, % 39.7% 46.9% 47.5% 45.9% 46.5% 
Steam Turbine Heat Rate, kJ/kWh (Btu/kWh) 9,074 (8,601) 7,678 (7,277) 7,586 (7,190) 7,838 (7,429) 7,750 (7,345) 
CO2 Capture Rate, % 0% 90% 95% 90% 95% 
Condenser Duty, GJ/h (MMBtu/h) 1,406 (1,332) 860 (815) 830 (787) 860 (815) 830 (787) 
AGR Cooling Duty, GJ/h (MMBtu/h) 0 (0) 1,194 (1,132) 1,232 (1,167) 1,194 (1,132) 1,232 (1,167) 
Natural Gas Feed Flow, kg/h (lb/h) 93,272 (205,630) 93,272 (205,630) 93,272 (205,630) 93,272 (205,630) 93,272 (205,630) 
HHV Thermal Input, kWt 1,354,905 1,354,905 1,354,905 1,354,905 1,354,905 
LHV Thermal Input, kWt 1,222,936 1,222,936 1,222,936 1,222,936 1,222,936 
Raw Water Withdrawal, (m3/min)/MWnet (gpm/MWnet) 0.015 (4.0) 0.026 (6.9) 0.027 (7.0) 0.026 (7.0) 0.027 (7.1) 
Raw Water Consumption, (m3/min)/MWnet (gpm/MWnet) 0.012 (3.1) 0.017 (4.6) 0.018 (4.7) 0.018 (4.6) 0.018 (4.7) 
Note: Values shown are for total 2×2×1 system 
AIncludes plant control systems, lighting, HVAC, and miscellaneous low voltage loads

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
17 
Exhibit 3-3. H-frame NGCC plant performance summary 
Case 
7HA.02 
Without Capture 
(B32A) 
7HA.02 
with 90% Capture 
(B32B.90) 
7HA.02 
with 95% Capture 
(B32B.95) 
7HA.02 
Retrofitted with 
90% Capture  
(B32A-BR.90) 
7HA.02 
Retrofitted with 
95% Capture  
(B32A-BR.95) 
Plant Output 
Gas Turbine Power, MWe 686 686 686 686 686 
Steam Turbine Power, MWe 324 260 256 255 251 
Total, MWe 1,009 945 942 940 936 
Auxiliary Load 
Circulating Water Pumps, kWe 3,510 5,530 5,570 5,530 5,570 
Combustion Turbine Auxiliaries, kWe 1,320 1,320 1,320 1,320 1,320 
Condensate Pumps, kWe 180 200 200 200 200 
Cooling Tower Fans, kWe 1,810 2,860 2,880 2,860 2,880 
CO₂ Capture/Removal Auxiliaries, kWe – 18,000 19,200 18,000 19,200 
CO₂ Compression, kWe – 23,810 25,130 23,810 25,130 
Feedwater Pumps, kWe 5,760 5,760 5,760 5,760 5,760 
Ground Water Pumps, kWe 330 520 520 520 520 
Miscellaneous Balance of PlantA, kWe 710 710 710 710 710 
SCR, kWe 3 3 3 3 3 
Steam Turbine Auxiliaries, kWe 230 230 230 230 230 
Transformer Losses, kWe 3,070 3,020 3,020 3,010 3,000 
Total Auxiliaries, MWe 17 62 65 62 65 
Net Plant Power, MWe 992 883 877 878 872 
Plant Performance 
HHV Net Plant Efficiency, % 55.1% 49.0% 48.7% 48.7% 48.4% 
HHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 6,537 (6,196) 7,342 (6,959) 7,393 (7,007) 7,387 (7,001) 7,439 (7,051) 
HHV Combustion Turbine Efficiency, % 38.0% 38.0% 38.0% 38.0% 38.0%

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
18 
Case 
7HA.02 
Without Capture 
(B32A) 
7HA.02 
with 90% Capture 
(B32B.90) 
7HA.02 
with 95% Capture 
(B32B.95) 
7HA.02 
Retrofitted with 
90% Capture  
(B32A-BR.90) 
7HA.02 
Retrofitted with 
95% Capture  
(B32A-BR.95) 
Plant Performance (continued) 
LHV Net Plant Efficiency, % 61.0% 54.3% 54.0% 54.0% 53.6% 
LHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 5,900 (5,592) 6,627 (6,281) 6,672 (6,324) 6,667 (6,319) 6,714 (6,364) 
LHV Combustion Turbine Efficiency, % 42.2% 42.2% 42.2% 42.2% 42.2% 
Steam Turbine Cycle Efficiency, % 39.1% 46.7% 47.3% 45.7% 46.3% 
Steam Turbine Heat Rate, kJ/kWh (Btu/kWh) 9,213 (8,732) 7,713 (7,311) 7,609 (7,212) 7,877 (7,466) 7,776 (7,370) 
CO2 Capture Rate, % 0% 90% 95% 90% 95% 
Condenser Duty, GJ/h (MMBtu/h) 1,757 (1,666) 1,031 (978) 992 (940) 1,031 (978) 992 (940) 
AGR Cooling Duty, GJ/h (MMBtu/h) 0 (0) 1,587 (1,505) 1,638 (1,552) 1,587 (1,505) 1,638 (1,552) 
Natural Gas Feed Flow, kg/h (lb/h) 124,025 (273,429) 124,025 (273,429) 124,025 (273,429) 124,025 (273,429) 124,025 (273,429) 
HHV Thermal Input, kWt 1,801,631 1,801,631 1,801,631 1,801,631 1,801,631 
LHV Thermal Input, kWt 1,626,150 1,626,150 1,626,150 1,626,150 1,626,150 
Raw Water Withdrawal, (m3/min)/MWnet (gpm/MWnet) 0.014 (3.6) 0.024 (6.4) 0.025 (6.5) 0.025 (6.5) 0.025 (6.6) 
Raw Water Consumption, (m3/min)/MWnet (gpm/MWnet) 0.011 (2.8) 0.016 (4.2) 0.016 (4.3) 0.016 (4.3) 0.016 (4.3) 
Note: Values shown are for total 2×2×1 system 
AIncludes plant control systems, lighting, HVAC, and miscellaneous low voltage loads

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
19 
4 COST ESTIMATES 
Detailed cost estimates (including capital and operation and maintenance [O&M] costs) were 
developed for greenfield installations in FEBRev4a. Those costs were used as the basis for 
scaling all the cost estimates in this study. The greenfield cost estimation methodology, 
including CRF and LCOE equations, is described in “QGESS: Cost Estimation Methodology for 
NETL Assessments of Power Plant Performance.” [5] The owner/developer is assumed to be an 
investor-owned utility (IOU). All NGCC plants are assumed to have financial structures 
consistent with three-year capital expenditure periods and thirty-year operational periods.  
Costs are scaled as needed using the methodology specified for NGCC plants in “QGESS: Capital 
Cost Scaling Methodology: Revision 4 Report.” [6] The 30-year levelized natural gas cost is 
assumed to be $4.42/MMBtu as specified in “QGESS: Fuel Prices for Selected Feedstocks in 
NETL Studies” [2] for natural gas delivered to large combined cycle plants operating at high 
capacity factors in the Midwest. The costs of T&S are assumed to be $10 per tonne of CO2 as 
specified in “QGESS: Carbon Dioxide Transport and Storage Costs in NETL Studies.” [7] The costs 
of retrofitting are estimated using the methodology outlined in the “QGESS: Carbon Capture 
Retrofit.” [3] All costs are presented in real 2018 dollars. 
To avoid capital cost estimation bias due to the number of processing trains considered, all 
cases assume that the flue gas can be processed in a single capture system process train. Future 
development of capture systems may prove that multiple trains are required for the flue gas 
flow rates considered, but that information was not available from the vendor. Different 
configurations of the advanced amine CCS process and equipment could be considered for 
operational flexibility at additional cost, but these options were not considered in the present 
study. The cost curves herein are representative costs based on cost models validated with 
recent vendor input. Since there have been no designs of this size constructed to date, these 
costs incorporate near-term projections for the deployment of carbon capture, utilization, and 
storage technology in the utility sector. 
The vendor data provided suggested that the flue gas flow rate available from the F-frame 
NGCC case would be able to be processed in a single train without issue. The flue gas flow rate 
available from the H-frame NGCC case was approximately 20 percent higher than the data 
provided by the vendor; however, the vendor did not specifically exclude this flow rate as too 
large for a single train, nor provide a maximum flow rate for single train processing. Therefore, 
it was assumed that a single train could be applied for H-frame cases. Typical scaling outlined in 
the capital cost scaling QGESS [6] was applied to the F-frame capture system vendor-quoted 
costs to achieve estimated costs for an NGCC H-frame capture system. 
4.1 GREENFIELD COST ESTIMATES 
The TPC estimates include the bare erected costs (BEC) for the equipment; engineering, 
construction management, home office & fees (Engineering CM, H.O. & Fee); and project and 
process. Owners’ costs are added to the TPC resulting in the TOC. Additionally, financing costs 
are estimated by applying a factor to the TOC value to calculate total as-spent costs (TASC). [5,

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
20 
6] The annual O&M costs are calculated using model results to determine consumable 
quantities. 
The greenfield cost estimates summaries (including capital and O&M) are listed in Exhibit 4-1 
and Exhibit 4-2 for each turbine type. Additional details can be found in FEBRev4a. 
Exhibit 4-1. Summary cost estimate data for F-frame greenfield cases 
Case B31A B31B.90 B31B.95 
Turbine 7FA.05 7FA.05 7FA.05 
Capture Rate 0% 90% 95% 
Bare Erected Cost by Account, $/1000 
  A3 – Feedwater & Misc. BOP Systems 66,159 78,523 78,722 
  A5 – Flue Gas Cleanup 0 294,169 305,145 
  A6 – Combustion Turbine and Accessories 82,353 82,353 82,353 
  A7 – HRSG, Ducting & Stack 83,482 79,769 79,656 
  A8 – Steam Turbine & Accessories 69,836 59,667 59,077 
  A9 – Cooling Water System 28,207 36,639 36,789 
  A11 – Accessory Electric Plant 29,946 50,215 51,131 
  A12 – Instrumentation & Controls 14,169 16,594 16,690 
  A13 – Improvements to Site 19,332 20,008 19,972 
  A14 – Building & Structures 14,087 13,289 13,232 
Total BEC, $/1000 407,571 731,225 742,768 
  Engineering CM, H.O.& Fee, $/1000 81,514 146,245 148,554 
  Process Contingencies, $/1000 0 45,859 47,658 
  Project Contingencies, $/1000 77,908 163,719 166,823 
TPC, $/1000 566,994 1,087,048 1,105,803 
TPC, $/kW 780 1,686 1,727 
TOC, $/1000 691,670 1,321,288 1,343,987 
TOC, $/kW 952 2,049 2,099 
TASC, $/1000 755,751 1,443,701 1,468,503 
TASC, $/kW 1,040 2,239 2,293 
First-Year Fuel Cost (100% CF), $/1000 179,012 179,012 179,012 
First-Year Fixed O&M Cost, $/1000 19,467 35,539 36,092 
First-Year Variable O&M Cost (100% CF), $/1000 10,854 22,782 23,228 
First-Year Total O&M (100% CF), $/1000 209,332 237,333 238,332 
Note: All costs are in real 2018 dollars

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
21 
Exhibit 4-2. Summary cost estimate data for H-frame greenfield cases 
Case B32A B32B.90 B32B.95 
Turbine 7HA.02 7HA.02 7HA.02 
Capture Rate 0% 90% 95% 
Bare Erected Cost by Account, $/1000 
  A3 – Feedwater & Misc. BOP Systems 82,401 97,785 98,031 
  A5 – Gas Cleanup & Piping 0 348,712 361,860 
  A6 – Combustion Turbine and Accessories 159,892 159,892 159,892 
  A7 – HRSG, Ducting & Stack 127,656 122,240 122,061 
  A8 – Steam Turbine Generator  76,023 64,027 63,342 
  A9 – Cooling Water System 32,281 42,582 42,765 
  A11 – Accessory Electric Plant 37,066 61,614 62,779 
  A12 – Instrumentation & Controls 14,807 17,433 17,540 
  A13 – Improvements to Site 22,295 23,090 23,050 
  A14 – Building & Structures 16,029 15,060 14,993 
Total BEC, $/1000 568,450 952,434 966,313 
  Engineering CM, H.O.& Fee, $/1000 113,690 190,487 193,263 
  Process Contingencies, $/1000 0 54,711 56,880 
  Project Contingencies, $/1000 107,880 209,774 213,506 
TPC, $/1000 790,020 1,407,406 1,429,961 
TPC, $/kW 796 1,593 1,630 
TOC, $/1000 962,719 1,710,262 1,737,565 
TOC, $/kW 970 1,936 1,980 
TASC, $/1000 1,051,912 1,868,712 1,898,546 
TASC, $/kW 1,060 2,115 2,164 
First-Year Fuel Cost (100% CF), $/1000 238,034 238,034 238,034 
First-Year Fixed O&M Cost, $/1000 26,046 44,989 45,655 
First-Year Variable O&M Cost (100% CF), $/1000 14,690 29,556 30,116 
First-Year Total O&M (100% CF), $/1000 278,770 312,579 313,805 
Note: All costs are in 2018 dollars 
4.2 RETROFIT COST ESTIMATES 
Retrofit factors provided in the carbon capture retrofit QGESS are applied to greenfield 
estimates to determine retrofit costs for adding a capture system. [3] The first step in 
determining the retrofit costs is to determine the greenfield equivalent cost of the retrofit 
equipment. Standard cost scaling techniques are used to estimate the cost of the new 
equipment, using the FEBRev4a costs for each turbine type as the reference costs. The 
greenfield equivalent costs for the retrofit equipment that are added to the non-capture plant 
designs for each turbine type are shown in Exhibit 4-3.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
22 
Exhibit 4-3. Summary greenfield equivalent costs of the retrofit equipment 
Case B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95 
Turbine 7FA.05 7FA.05 7HA.02 7HA.02 
Capture Rate 90% 95% 90% 95% 
Bare Erected Cost by Account, $/1000 
  A3 – Feedwater & Misc. BOP Systems 12,364 12,562 15,384 15,630 
  A5 – Gas Cleanup & Piping 294,169 305,145 348,712 361,860 
  A6 – Combustion Turbine and Accessories 0 0 0 0 
  A7 – HRSG, Ducting & Stack 0 0 0 0 
  A8 – Steam Turbine Generator  7,417 7,703 9,138 9,490 
  A9 – Cooling Water System 8,432 8,582 10,302 10,484 
  A11 – Accessory Electric Plant 21,428 22,407 26,190 27,444 
  A12 – Instrumentation & Controls 2,424 2,520 2,626 2,733 
  A13 – Improvements to Site 676 640 795 755 
  A14 – Building & Structures 226 230 280 285 
Total BEC, $/1000 347,137 359,790 413,426 428,681 
  Engineering CM, H.O.& Fee, $/1000 69,427 71,958 82,685 85,736 
  Process Contingencies, $/1000 45,250 47,050 54,081 56,250 
  Project Contingencies, $/1000 89,987 93,293 107,151 111,132 
Greenfield equivalent TPC, $/1000 551,801 572,091 657,343 681,799 
Greenfield equivalent TPC, $/kW 861 900 749 782 
Note: All costs are in 2018 dollars 
Typical TPC includes summing BEC; engineering, construction management, home office 
expenses and fees; and process and project contingencies. However, for retrofit applications, 
there is an increased difficulty associated with adding units after construction of the base plant, 
which can introduce additional costs. A retrofit difficulty factor (RDF) of 1.09 is used to account 
for this cost premium; the retrofit TPC is estimated by multiplying the RDF by the greenfield 
equivalent TPC. [3]  
Owners’ costs were calculated for only the additional equipment and O&M costs required for 
CO2 capture and added to the TPC to obtain the TOC. 
Line-item RDF applicable to NGCC plant designs are listed in Exhibit 4-4. While this study did not 
apply RDFs on an account line-item basis, if a given study has specific knowledge of an existing 
plant layout and restrictions, individual line-item factors should be applied to better reflect the 
difficulty of executing a retrofit at the specific plant. In cases such as this study, where generic 
plant locations and layouts are assumed with no space constraints, applying a RDF at the TPC 
level will represent an averaged increase in cost, equivalent to applying the 1.09 RDF to each 
account line item. The equipment and material retrofit factors are the cost premium addressing 
minor differences in equipment specifications, layout, duct routing, and items where additional 
complexity is likely to be encountered. Labor productivity adjustments account for productivity 
losses associated with working on an existing operating plant site, in potentially highly

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
23 
congested areas, and with modifications and tie-ins to existing equipment and/or systems. The 
RDF range 1.00–1.30 and are multiplied by the greenfield equivalent equipment, material, and 
labor costs for each cost account to estimate retrofit cost premiums. The accounts in Exhibit 4-4 
have been modified from the QGESS to align with cost accounts reported in FEBRev4a. 
Exhibit 4-4. Retrofit scope adjustment factors 
Retrofit Scope Adjustment 
Cost Category Equipment/Material Labor Productivity Low High Low High 
 3 FEEDWATER & MISC. BOP SYSTEMS     
3.1  Feedwater System 1.00 1.00 1.00 1.00 
3.2  Water Makeup & Pretreating  1.00 1.05 1.05 1.25 
3.3  Other Feedwater Subsystems 1.00 1.00 1.00 1.00 
3.4  Service Water Systems 1.00 1.05 1.05 1.25 
3.5  Other Boiler Plant Systems 1.00 1.00 1.00 1.00 
3.6  FO Supply System & Natural Gas 1.00 1.00 1.00 1.00 
3.7  Waste Treatment Equipment 1.00 1.05 1.05 1.25 
3.9  Misc. Equip. (Cranes, Air Comp., Comm.) 1.00 1.05 1.05 1.25 
 5 CO2 REMOVAL & COMPRESSION     
5.1 CO2 Removal System 1.00 1.05 1.00 1.15 
5.4 CO2 Compression & Drying 1.00 1.00 1.00 1.15 
 6 COMBUSTION TURBINE/ACCESSORIES     
6.1  Combustion Turbine Generator 1.00 1.00 1.00 1.00 
6.3  Combustion Turbine Accessories 1.00 1.00 1.00 1.00 
6.4  Compressed Air Piping 1.00 1.00 1.00 1.00 
6.5  Combustion Turbine Foundations 1.00 1.00 1.00 1.00 
 7 HRSG, DUCTING & STACK     
7.1  Heat Recovery Steam Generator 1.00 1.00 1.00 1.00 
7.2  HRSG Accessories 1.00 1.00 1.00 1.00 
7.3  Ductwork 1.00 1.10 1.05 1.20 
7.4  Stack 1.00 1.25 1.00 1.30 
7.5  Duct & Stack Foundations 1.00 1.10 1.00 1.25 
 8 STEAM TURBINE GENERATOR      
8.1  Steam Turbine Generator & Accessories 1.00 1.00 1.00 1.00 
8.2  Turbine Plant Auxiliaries 1.00 1.00 1.00 1.00 
8.3  Condenser & Auxiliaries 1.00 1.00 1.00 1.00 
8.4  Steam Piping 1.00 1.10 1.05 1.25 
8.5  Turbine Generator Foundations 1.00 1.00 1.00 1.00 
 9 COOLING WATER SYSTEM     
9.1  Cooling Towers 1.00 1.05 1.00 1.15 
9.2  Circulating Water Pumps 1.00 1.05 1.00 1.15

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
24 
Retrofit Scope Adjustment 
Cost Category Equipment/Material Labor Productivity Low High Low High 
9.3  Circ. Water System Auxiliaries 1.00 1.05 1.00 1.15 
9.4  Circ. Water Piping 1.00 1.10 1.00 1.15 
9.5  Make-up Water System 1.00 1.10 1.00 1.15 
9.6  Component Cooling Water System 1.00 1.05 1.00 1.15 
9.7  Circ. Water System Foundations & Structures 1.00 1.10 1.00 1.15 
11 ACCESSORY ELECTRIC PLANT     
11.1  Generator Equipment 1.00 1.00 1.00 1.00 
11.2  Station Service Equipment 1.00 1.05 1.00 1.15 
11.3  Switchgear & Motor Control  1.00 1.05 1.00 1.15 
11.4  Conduit & Cable Tray 1.00 1.10 1.00 1.15 
11.5  Wire & Cable 1.00 1.10 1.00 1.15 
11.6  Protective Equipment 1.00 1.05 1.00 1.15 
11.7  Standby Equipment 1.00 1.05 1.00 1.15 
11.8  Main Power Transformers 1.00 1.05 1.00 1.15 
11.9  Electrical Foundations 1.00 1.10 1.00 1.15 
12 INSTRUMENTATION & CONTROL     
12.1  NGCC Control Equipment 1.00 1.00 1.00 1.00 
12.2  Combustion Turbine Control 1.00 1.00 1.00 1.00 
12.3  Steam Turbine Control 1.00 1.00 1.00 1.00 
12.4  Other Major Component Control 1.00 1.00 1.00 1.00 
12.5  Signal Processing Equipment 1.00 1.00 1.00 1.00 
12.6  Control Boards, Panels & Racks 1.00 1.05 1.00 1.15 
12.7  Distributed Control System Equipment 1.00 1.05 1.10 1.30 
12.8  Instrument Wiring & Tubing 1.00 1.05 1.05 1.20 
12.9  Other I&C Equipment 1.00 1.05 1.05 1.20 
13 IMPROVEMENTS TO SITE     
13.1  Site Preparation 1.00 1.05 1.00 1.20 
13.2  Site Improvements 1.00 1.05 1.00 1.20 
13.3  Site Facilities 1.00 1.05 1.00 1.20 
14 BUILDINGS & STRUCTURES     
14.1  Combustion Turbine Area 1.00 1.00 1.00 1.00 
14.3  Steam Turbine Building 1.00 1.00 1.00 1.00 
14.4  Administration Building 1.00 1.00 1.00 1.00 
14.5  Circulation Water Pumphouse 1.00 1.05 1.00 1.15 
14.6  Water Treatment Buildings 1.00 1.05 1.05 1.25 
14.7  Machine Shop 1.00 1.00 1.00 1.00 
14.8  Warehouse  1.00 1.00 1.00 1.00 
14.9  Other Buildings & Structures 1.00 1.05 1.00 1.15

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
25 
Retrofit Scope Adjustment 
Cost Category Equipment/Material Labor Productivity Low High Low High 
14.10  Waste Treating Building & Structures 1.00 1.05 1.05 1.25 
The carbon capture retrofit QGESS states that the weighted average of these factors assuming 
high retrofit difficulty is 1.09, which was applied to the generic plant layout. [4] This simplified 
approach assumes that $100 of installed greenfield equipment tends to cost $109 if installed as 
a retrofit in NGCC applications. This approach also lends itself to a simple sensitivity analysis on 
a single retrofit factor that bounds the retrofit impact. The sensitivity analysis results are 
presented in Section 5.  
Exhibit 4-5 summarizes the total capital and O&M costs for cases B31A-BR.90, B31A-BR.95, 
B32A-BR.90, and B32A-BR.95. The total annual O&M costs after retrofitting were estimated 
based on the performance parameters presented in Section 3. 
Exhibit 4-5. Summary costs of the retrofit equipment 
Case B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95 
Turbine 7FA.05 7FA.05 7HA.02 7HA.02 
Capture Rate 90% 95% 90% 95% 
Bare Erected Cost by Account  
Greenfield equivalent TPC, $/1000 551,801 572,091 657,343 681,799 
Greenfield equivalent TPC, $/kW 861 900 749 782 
RDF 1.09 1.09 1.09 1.09 
TPC w/ RDF, $/1000 601,463 623,579 716,504 743,161 
TPC w/RDF, $/kW 939 981 816 852 
TOC w/ RDF, $/1000 727,657 754,405 866,916 899,161 
TOC w/ RDF, $/kW 1,136 1,186 987 1,031 
TASC w/ RDF, $/1000 795,072 824,298 947,233 982,466 
TASC w/ RDF, $/kW 1,241 1,296 1,079 1,127 
First-Year Fuel Cost (100% CF), $/1000 179,012 179,012 238,034 238,034 
First-Year Fixed O&M Cost, $/1000 36,475 37,074 46,168 46,889 
First-Year Variable O&M Cost (100% CF), $/1000 23,208 23,674 30,092 30,678 
First-Year Total O&M (100% CF), $/1000 238,695 239,760 314,294 315,601 
Note: All costs are in real 2018 dollars 
4.3 LEVELIZED COST OF ELECTRICITY AND OTHER METRICS 
The primary cost metric used in this study is LCOE, which is the revenue required to meet all 
capital and operational costs per net MWh levelized over the lifetime of the power plant. Since 
these are retrofit systems, it is assumed that the existing plant has been fully paid off, no

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
26 
additional costs are necessary for plant life extension, and the only capital outlay required is for 
the CCS process, which includes the removal technology process equipment, a CO2 compression 
train, and any modification to the existing plant required to accommodate the retrofitted 
technology (e.g. additional cooling tower capacity to support the CCS process requirements and 
additional steam piping). Existing NGCC plant fuel costs and fixed and variable O&M, as well as 
additional labor, maintenance and consumables required by the retrofit are included in the 
LCOE calculations. The owner/developer is assumed to be an IOU, and the CO2 capture retrofit 
was assumed to have financial structures consistent with a three-year capital expenditure 
period and a thirty-year operational period. This is consistent with the greenfield NGCC cases in 
FEBRev4a. The retrofit cost results for each case are listed in Exhibit 4-6. As the size of the 
turbine increases, the LCOE decreases, which is consistent with improvements in efficiency and 
typical economies of scale. The cost of CO2 captured and the cost of CO2 avoided are also 
included in the table. Upon retrofitting the NGCC plant with CCS, a derate in the net plant 
electrical output will be incurred due to the auxiliary electric load required to run the CCS 
system, as well as steam extraction from the steam cycle to satisfy the CCS reboiler duty, rather 
than produce power in the LP steam turbine section. It is recognized that this difference in 
power production from before retrofit to after retrofit constitutes a power makeup that will 
need to be financially accounted for within the electricity distribution system. This study 
assumes that the retrofitted plant needs to account for this charge and does so by including a 
makeup power cost (MPC) in the retrofitted plants’ LCOE. A charge for the makeup capacity 
needed to match the original plant net generation is added to the LCOE at an assumed 
projected sales price (PSP) for electricity of $30/MWh. This $30/MWh price is based on the 
approximate average Midcontinent Independent System Operator Market price with near 10 
percent renewable penetration. [13] The MPC is also included in the calculation of the cost of 
CO2 captured and the cost of CO2 avoided. 
Exhibit 4-6. Summary LCOE of the retrofit cases 
Case B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95 
Turbine 7FA.05 7FA.05 7HA.02 7HA.02 
Capture Rate 90% 95% 90% 95% 
LCOE, Total [Including T&S] 59.0 60.2 55.6 56.7 
LCOE, Total [Including T&S and MPC] 63.0 64.5 59.5 60.9 
    Capital, $/MWh 11.8 12.3 10.2 10.7 
    Fixed, $/MWh 7.6 7.8 7.1 7.2 
    Variable, $/MWh 4.1 4.3 3.9 4.0 
    Fuel, $/MWh 31.9 32.1 30.9 31.2 
    CO2 T&S, $/MWh 3.5 3.7 3.4 3.6 
    Makeup power cost @ PSP = $30/MWh, $/MWh 4.0 4.3 3.9 4.1 
Cost of CO2 Captured [Excluding T&S], $/tonne CO2  61.8 60.8 56.7 55.9 
Cost of CO2 Avoided [Including T&S], $/tonne CO2  71.8 70.8 66.7 65.9 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
27 
The cost of CO2 captured is the price at which the revenue generated by selling the recovered 
CO2 equals the costs of recovering it. The costs of recovering the CO2 include capital 
expenditures, fixed and variable O&M increases, fuel cost changes, and makeup power charges. 
For retrofit cases, the equation for calculating the cost of CO2 captured is 
Cost of CO2 Captured =
�PSP � $MWh�∗lost MWh�MWHyr @CF�+CRF∗Incremental TOC� $yr�+Incremental O&M� $yr@CF��
CO2 Captured �tonneyr @CF�   
where: 
PSP  = Projected sales price of electricity, $/MWh 
Lost MWh = MWhBAU - MWhRET 
MWhBAU  = Annual net generation for non-capture/business as usual, MWh/yr 
MWhRET  = Annual net generation for after retrofit, MWh/yr  
BAU  = Business as usual (i.e., existing plant) 
RET  = After retrofit 
CF   = Capacity factor 
CCF  = Capital recovery factor 
TOC  = Total overnight cost 
Incremental O&M costs associated with retrofit, $/yr  
= (Fixed O&M + Variable O&M + Fuel)BAU - (Fixed O&M + Variable O&M + Fuel)RET 
The cost of CO2 avoided is the cost of reducing emissions at which the penalty for not reducing 
the emissions is equal to the costs. If the price of allowances or fines for emissions are higher 
than this value, then there is an economic incentive for adding the capture system. The costs of 
recovering the CO2 include capital expenditures, fixed and variable O&M increases, fuel cost 
changes, T&S, and makeup power charges. 
For retrofit cases, the equation for calculating the cost of CO2 avoided is 
Cost of CO2 Avoided =
𝑃𝑃𝑃𝑃𝑃𝑃� $MWh�∗lost MWh (MWhyr @CF)+CRF∗Incremental TOC� $yr�+Incremental O&M� $yr@CF�+T&S Costs( $yr@CF)
�MWhBAU�MWhyr @CF�∗ CO2EmissionsBAU� tonneMWhBAU�−MWhRET�MWhyr @CF�∗ CO2EmissionsRET( tonneMWhRET)�   
where: 
Incremental O&M costs associated with retrofit, $/yr  
= (Fixed O&M + Variable O&M + Fuel)BAU - (Fixed O&M + Variable O&M + Fuel)RET

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
28 
5 SUMMARY COMPARISON 
The LCOE for both turbine types, retrofit with CCS, is illustrated in Exhibit 5-1. The estimated 
LCOE values for the non-capture cases (assuming the existing plant is fully paid off) are included 
in the chart for comparison. Greenfield applications were also added for comparison, but 
represent different cost assumptions than the other cases, as previously noted. As the size of 
the turbine increases, the LCOE decreases, which is consistent with improvements in efficiency 
and typical economies of scale. The annual fuel costs make up the largest portion of the annual 
operating costs. The total annual fuel cost remains the same for each turbine type before and 
after retrofit, but the cost per MWh increases due to the decrease in net power generation after 
retrofit. 
Exhibit 5-1. Summary LCOE 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. Capital costs for cases B31A and B32A are 
assumed to be paid off 
 
CO2 capture from power plants can be incentivized by selling the separated CO2 product at a 
price greater than the cost of capturing CO2. To match the previous economic attractiveness or 
profitability of the plant, the cost of CO2 captured for the retrofit case must cover the amortized 
cost of the new retrofitted equipment, the additional O&M costs associated with the CO2 
capture process, and the lost opportunity cost associated with the derate in electrical 
generation capacity. The costs for CO2 T&S are excluded from the cost of capture when the CO2 
is sold at the plant gate. The lost opportunity cost is due to the electricity sales that are forfeited 
21.3 21.8 20.1 20.6
11.8 12.3 10.2 10.7
3.6
7.4 7.6
3.5
6.8 7.0
7.6 7.8 7.1 7.2
1.7
4.0 4.1
1.7
3.8 3.9
4.1 4.3 3.9 4.028.1
31.7 31.9
27.4
30.8 31.0
31.9 32.1
30.9 31.2
3.5 3.7
3.4 3.6
3.5 3.7
3.4 3.6
4.0 4.3
3.9 4.1
33.4
67.9 69.1
32.6
64.9 66.0
63.0 64.5
59.5 60.9
0
10
20
30
40
50
60
70
80
90LCOE [including T&S], $/MWh
MPC CO₂ T&S
Fuel Variable
Fixed Capital

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
29 
due to the auxiliary load of the capture system and the reduced steam turbine output when 
steam is extracted to regenerate the capture solvent. 
The lost opportunity cost is the portion of the CO2 capture costs that covers the previous 
revenue from derated electrical generation sold at the PSP of electricity, with some built-in 
profit above the previous existing plant’s marginal LCOE. For this analysis, a PSP of electricity of 
$30/MWh is assumed. [13] 
The cost of CO2 captured/avoided for retrofit cases is shown in Exhibit 5-2 and Exhibit 5-3. These 
parameters are explained in more detail in Section 4.3. The reference case for each calculated 
value is the matching turbine non-capture case. As the turbine design increases in size, the costs 
per unit of CO2 captured decreases. Increasing the capture rate for a given turbine size has a 
negligible impact on the cost of CO2 captured/avoided. The increase in the CO2 capture rate 
offsets the associated increase in capital costs and reduced power generation. Greenfield costs 
for CO2 captured/avoided are included for comparison; however, the method for calculating the 
costs is slightly different in greenfield and retrofit applications so a direct comparison may not 
be appropriate. 
Exhibit 5-2. Summary cost of CO2 captured 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. B31A is used as a reference for all F-
frame retrofit case calculations. B32A is used as a reference for all H-frame retrofit case calculations. 
32.8 32.3 29.7 29.3 33.7 33.1 30.2 29.7
11.0 10.8
9.8 9.7
10.2 10.0
9.1 8.9
6.7 6.6
6.3 6.2
6.3 6.2
5.9 5.8
10.3 10.3
10.0 10.0
11.5 11.5
11.5 11.5
60.7 59.9
55.9 55.2
61.8 60.8
56.7 55.9
0
10
20
30
40
50
60
70
80
90
B31B.90 B31B.95 B32B.90 B32B.95 B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95
Cost of CO2 Captured [excluding T&S], $/tonne
MPC
Fuel
Variable
Fixed
Capital

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
30 
Exhibit 5-3. Summary cost of CO2 avoided 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor. B31A is used as a reference for all F-
frame retrofit case calculations. B32A is used as a reference for all H-frame retrofit case calculations. 
 
  
37.5 36.9 33.9 33.3 33.7 33.1 30.2 29.7
12.5 12.3
11.2 11.0 10.2 10.0
9.1 8.9
7.7 7.5
7.2 7.1 6.3 6.2
5.9 5.8
11.7 11.7
11.4 11.4
11.4 11.4
11.4 11.4
10.0 10.0
10.0 10.0
11.5 11.5
11.5 11.5
80.8 79.8
75.0 74.2 71.8 70.8
66.7 65.9
0
10
20
30
40
50
60
70
80
90
B31B.90 B31B.95 B32B.90 B32B.95 B31A-BR.90 B31A-BR.95 B32A-BR.90 B32A-BR.95
Cost of CO2 Avoided [includingT&S], $/tonne
MPC CO₂ T&S
Fuel Variable
Fixed Capital

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
31 
The sensitivity of the LCOE values to the price of natural gas is shown in Exhibit 5-4. The values 
at the $4.42/MMBtu price assumed for this study are along the vertical line shown in the chart. 
As the natural gas price increases, the LCOE values increase. The non-capture cases (not 
assuming the existing plant is fully paid off—greenfield installation) are slightly less sensitive 
than the capture cases. A natural gas price change of $1.00, on average, results in an increase in 
LCOE for non-capture cases of $6.28/MWh and for capture cases of $7.11/MWh. The impact of 
the price on the LCOE is approximately the same for all turbine designs because the annual fuel 
costs are a similar proportion of the LCOE values (approximately 50 percent of the retrofitted 
capture case values and 65 percent of the non-capture cases). Retrofit cases are slightly more 
sensitive to natural gas price (on a $/MWh basis) when compared to greenfield capture cases 
since the fuel portion of the LCOE for retrofit cases is slightly higher. 
Exhibit 5-4. Sensitivity of LCOE to natural gas price 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor 
 
  
20
30
40
50
60
70
80
90
100
110
1 2 3 4 5 6 7 8 9 10
LCOE [including T&S], $/MWh
Natural Gas Price, $/MMBtu
B31A
B31B.90
B31B.95
B31A-BR.90
B31A-BR.95
B32A
B32B.90
B32B.95
B32A-BR.90
B32A-BR.95
Natural Gas Price = $4.42/MMBtu

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
32 
The sensitivity of the LCOE values to capacity factor is shown in Exhibit 5-5. The values at the 
85 percent capacity factor assumed for this study are along the vertical line shown in the chart. 
As the capacity factor increases, the LCOE values decrease. The annual fuel cost is directly 
proportional to the annual electricity generated, so changes in the capacity factor do not impact 
the fuel portion of the LCOE. The fixed charges and the retrofitted capital annual charges are 
higher for the retrofitted capture cases, so the LCOE values for those cases increase more than 
the non-capture case LCOE values at lower capacity factors. The retrofitted capital annual 
charges are lower than greenfield capital annual charges, so the LCOE values for retrofit cases 
increase significantly less than the greenfield capture case LCOE values at lower capacity factors. 
The calculations were made with the assumption that no addition or reduction in equipment, 
operating, maintenance and support labor, or capital would be needed to operate at higher or 
lower capacity factors. The capacity factor has a smaller impact as the turbine designs 
(efficiencies) improve, and the base LCOE decreases. 
Exhibit 5-5. Sensitivity of LCOE to capacity factor 
 
Note: All costs are in real 2018 dollars 
 
  
40
50
60
70
80
90
100
110
120
130
0.3 0.4 0.5 0.6 0.7 0.8 0.9
LCOE [including T&S], $/MWh
Capacity Factor
B31A B32A
B31B.90 B32B.90
B31B.95 B32B.95
B31A-BR.90 B32A-BR.90
B31A-BR.95 B32A-BR.95
CF = 85%

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
33 
The cost estimates in this study utilize an RDF of 1.09 applied at the TPC level to estimate 
retrofit cost premiums. The sensitivity of the LCOE to this single retrofit difficulty cost factor was 
calculated and is illustrated in Exhibit 5-6. The simplified approach generates LCOE values 
approximately equal to the detailed estimates and bounds the edges of the more detailed 
estimate. The assumed RDF of 1.09 (as indicated by the vertical line on the graph) indicates that 
$100 of installed greenfield equipment tends to cost $109 if installed as a retrofit. The retrofit 
premium estimated by either the detailed or simplified method is within the expected accuracy 
(-15 percent/+25 percent for an AACE International Class 4 cost estimate) of reference NGCC 
plants considered. It is important to note that the retrofit premium is highly site specific, which 
is why it is presented as a range, and that extreme site conditions or plant configurations could 
render such a retrofit unfeasible. The range presented here is meant to represent a typical 
retrofit as an evaluation tool, rather than to replace the detailed engineering and design 
required for such a project. For both F-frame and H-frame cases, the marginal increase in LCOE 
over the entire range of RDFs is less than $4/MWh.  
Exhibit 5-6. Sensitivity of LCOE to retrofit difficulty factor (RDF) 
 
Note: All costs are in real 2018 dollars and calculated at 85% capacity factor 
50
55
60
65
70
75
 1.00  1.05  1.10  1.15  1.20  1.25  1.30
LCOE [including T&S], $/MWh
Retrofit Difficulty Factor
B31A-BR.90
B31A-BR.95
B32A-BR.90
B32A-BR.95
Retrofit Difficulty Factor = 1.09

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
34 
6 CONCLUSION AND FUTURE WORK 
The purpose of this revision is to align this report with the most recent revision of FEBRev4a. [1]  
The primary update to the NGCC power plants in FEBRev4a was an update to the CCS system 
cost and performance. Additionally, a higher CO2 capture rate (95 percent) was included. In 
comparison to the previous revision of this report, non-capture LCOE remained constant when 
assuming the base plant is fully paid off (zero capital costs). For retrofit cases with 90 percent 
capture, LCOE reduced by 10 percent ($70.5/MWh versus $63.0/MWh for F-frame NGCC and 
$66.2/MWh versus $59.5/MWh H-frame NGCC), the cost of CO2 captured reduced by 
34 percent, and the cost of CO2 avoided reduced by 41 percent in both F- and H-frame cases. 
This report shows that increasing the CO2 capture rate from 90 to 95 percent in retrofit 
applications increases the LCOE by 2 percent. The increase from 90 to 95 percent CO2 capture 
has a negligible impact on both the cost of CO2 captured and avoided. 
The study conclusions apply only to this level of conceptual design and economic analysis. 
Further analysis is needed to establish the influence of different retrofit scenarios on the cost of 
CO2 captured and the LCOE. The following future work is recommended: 
• Considering scenarios where the base plant is not fully paid off, or where the retrofit 
capture plant is owned and operated independently. 
• The plant performance of today’s SOA F-class or H-class NGCC plants may or may not 
reflect the plant performance of existing NGCC plants that are candidates for capture 
retrofit. A more detailed analysis should identify the combustion turbine types and 
vintages that represent the existing fleet and apply today’s SOA capture system 
performance and cost as a retrofit to further refine the cost of capture. 
• Accounting for the impact of possible costs associated with improvements necessary for 
plant life extension to maximize the utility of installing a new CCS system. 
• Different configurations of the CCS process and equipment could be considered for 
operational flexibility at additional cost. 
• Considering the influence of site-specific costs on LCOE and the cost of CO2 captured, 
such as the need for longer flue gas ducting, air cooling, and dedicated cooling systems 
and package boilers for steam generation.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
35 
REFERENCES 
[1]  NETL, "Cost and Performance Baseline for Fossil Energy Plants Volume 1: Bituminous 
Coal and Natural Gas to Electricity," DOE/NETL, Pittsburgh, PA, 2022. 
[2]  NETL, "Quality Guidelines for Energy System Studies: Fuel Prices for Selected 
Feedstocks in NETL Studies," DOE/NETL, Pittsburgh, PA, 2019. 
[3]  NETL, "Quality Guidelines for Energy System Studies: Carbon Capture Retrofit 
Studies," DOE/NETL, Pittsburgh, PA, 2019. 
[4]  NETL, "Cost and Performance of Retrofitting Existing NGCC Units for Carbon 
Capture - Revision 2," DOE/NETL, Pittsburgh, PA, 2020. 
[5]  NETL, "Quality Guidelines for Energy System Studies: Cost Estimation Methodology 
for NETL Assessments of Power Plant Performance. DOE/NETL-2011/1455," 
DOE/NETL, Pittsburgh, PA, 2019. 
[6]  NETL, "Quality Guidelines for Energy System Studies: Capital Cost Scaling 
Methodology: Revision 4 Report," DOE/NETL, Pittsburgh, PA, 2019. 
[7]  NETL, "Quality Guidelines for Energy System Studies: Carbon Dioxide Transport and 
Storage Costs in NETL Studies," DOE/NETL, Pittsburgh, PA, 2019. 
[8]  NETL, "Quality Guidelines for Energy System Studies: Process Modeling Design 
Parameters," DOE/NETL, Pittsburgh, PA, 2019. 
[9]  NETL, "Quality Guidelines for Energy System Studies: Specification for Selected 
Feedstocks," DOE/NETL, Pittsburgh, PA, 2012. 
[10]  M. Lucquiaud and J. Gibbins, "Retrofitting CO2 Capture Ready Fossil Plants with 
Post-combustion Capture Part 1: Requirements for Supercritical Pulverized Coal 
Plants Using Solvent-based Flue Gas Scrubbing," Proceedings of the Institution of 
Mechanical Engineers, Part A: Journal of Power and Energy. Mechanical 
Engineering Dept, Imperial College London, vol. 223, pp. 213-226, January 2009.  
[11]  International Energy Agency Greenhouse Gas (IEA GHG), "Improvement in Power 
Generation with Post-combustion Capture of CO2. Report Number PH4/33," 2004. 
[Online]. Available: 
http://www.canadiancleanpowercoalition.com/pdf/AS5%20-%20PH4-
33%20post%20combustion.pdf. [Accessed 28 July 2011]. 
[12]  NETL, "Post-Combustion Capture Retrofit Study Update, DOE/NETL-341/130104," 
DOE/NETL, Pittsburgh, PA, January 2013. 
[13]  Potomac Economics, "2019 State of the Market Report for the MISO Electricity 
Markets," Potomac Economics, 2020. 
[14]  Environmental Protection Agency, "40 CFR Part 60 - Carbon Pollution Emissions 
Guidelines for Existing Stationary Sources: Electric Utility Generating Units; Final Rule 
Vol. 80 No. 205," 23 October 2015. [Online]. Available: 
https://www.gpo.gov/fdsys/pkg/FR-2015-10-23/pdf/2015-22842.pdf. [Accessed 9 
October 2018].

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
36 
APPENDIX A: 97 PERCENT CAPTURE CASES 
Commercial-scale demonstration of solvent-based post-combustion carbon dioxide (CO2) 
capture systems at power generation facilities (specifically pulverized coal [PC] plants) has 
shown the ability to capture 90 percent of the CO2 in the flue gas stream. Moreover, field-
testing of post-combustion CO2 capture technology as well as vendor and industry feedback on 
projects currently in the planning stages (including front-end engineering and design projects 
sponsored by the Department of Energy [DOE]) indicates that capture rates as high as 95 
percent are feasible for both coal- and natural gas-fueled electricity generating units. Given the 
breadth of publicly available information supporting the capability for post-combustion capture 
systems to remove greater than 90 percent of the CO2 in the treated stream, cases for 90 
percent and 95 percent capture on natural gas combined cycle (NGCC) are presented in the 
main body of this report. 
It should be emphasized that technology suppliers (as reflected in vendor-supplied information 
provided to DOE that included cost and performance estimates for > 95 percent carbon capture 
and storage [97 percent for NGCC and 99 percent for PC] study cases) as well as subject matter 
experts acknowledge and support that solvent-based post-combustion CO2 capture 
technologies are capable of achieving CO2 removal rates beyond 95 percent on low-purity 
streams representative of fossil-fueled combustion. Although techno-economic analyses of 
deep decarbonization (≥ 99 percent) of combustion flue gas have been published by others, the 
relatively limited experience with design and operation of capture systems that can routinely, 
reliably, and economically achieve very high removal rates requires further study. Techno-
economic analysis of the higher capture rate (97 percent for NGCC) is included in this appendix.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
37 
Exhibit A-1. F-frame NGCC plant performance summary 
Case 
7FA.05 
Without Capture 
(B31A) 
7FA.05 
with 97% 
Capture 
(B31B.97) 
7FA.05 
Retrofitted with 
97% Capture 
(B31A-BR.97) 
7HA.02 
Without Capture 
(B32A) 
7HA.02 
with 97% 
Capture 
(B32B.97) 
7HA.02 
Retrofitted with 
97% Capture  
(B32A-BR.97) 
Plant Output 
Gas Turbine Power, MWe 477 477 477 686 686 686 
Steam Turbine Power, MWe 263 210 205 324 253 248 
Total, MWe 740 687 683 1,009 939 933 
Auxiliary Load 
Circulating Water Pumps, kWe 2,820 4,390 4,390 3,510 5,600 5,600 
Combustion Turbine Auxiliaries, kWe 1,020 1,020 1,020 1,320 1,320 1,320 
Condensate Pumps, kWe 150 170 170 180 200 200 
Cooling Tower Fans, kWe 1,460 2,270 2,270 1,810 2,890 2,890 
CO₂ Capture/Removal Auxiliaries, kWe – 15,200 15,200 – 20,200 20,200 
CO₂ Compression, kWe – 19,290 19,290 – 25,660 25,660 
Feedwater Pumps, kWe 4,830 4,830 4,830 5,760 5,760 5,760 
Ground Water Pumps, kWe 260 410 410 330 520 520 
Miscellaneous Balance of PlantA, kWe 570 570 570 710 710 710 
SCR, kWe 2 2 2 3 3 3 
Steam Turbine Auxiliaries, kWe 200 200 200 230 230 230 
Transformer Losses, kWe 2,250 2,210 2,200 3,070 3,020 3,000 
Total Auxiliaries, MWe 14 51 51 17 66 66 
Net Plant Power, MWe 727 637 632 992 873 867 
Plant Performance 
HHV Net Plant Efficiency, % 53.6% 47.0% 46.7% 55.1% 48.4% 48.1% 
HHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 6,714 (6,363) 7,659 (7,260) 7,716 (7,313) 6,537 (6,196) 7,433 (7,045) 7,482 (7,091) 
HHV Combustion Turbine Efficiency, % 35.2% 35.2% 35.2% 38.0% 38.0% 38.0%

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
38 
Case 
7FA.05 
Without Capture 
(B31A) 
7FA.05 
with 97% 
Capture 
(B31B.97) 
7FA.05 
Retrofitted with 
97% Capture 
(B31A-BR.97) 
7HA.02 
Without Capture 
(B32A) 
7HA.02 
with 97% 
Capture 
(B32B.97) 
7HA.02 
Retrofitted with 
97% Capture  
(B32A-BR.97) 
LHV Net Plant Efficiency, % 59.4% 52.1% 51.7% 61.0% 53.7% 53.3% 
LHV Net Plant Heat Rate, kJ/kWh (Btu/kWh) 6,060 (5,743) 6,913 (6,552) 6,964 (6,601) 5,900 (5,592) 6,709 (6,359) 6,753 (6,401) 
LHV Combustion Turbine Efficiency, % 39.0% 39.0% 39.0% 42.2% 42.2% 42.2% 
Steam Turbine Cycle Efficiency, % 39.7% 48.0% 47.0% 39.1% 47.9% 46.8% 
Steam Turbine Heat Rate, kJ/kWh (Btu/kWh) 9,074 (8,601) 7,495 (7,104) 7,666 (7,266) 9,213 (8,732) 7,514 (7,121) 7,687 (7,285) 
CO2 Capture Rate, % 0% 97% 97% 0% 97% 97% 
Condenser Duty, GJ/h (MMBtu/h) 1,406 (1,332) 803 (761) 803 (761) 1,757 (1,666) 955 (906) 955 (906) 
AGR Cooling Duty, GJ/h (MMBtu/h) 0 (0) 1,268 (1,201) 1,268 (1,201) 0 (0) 1,686 (1,598) 1,686 (1,598) 
Natural Gas Feed Flow, kg/h (lb/h) 93,272 (205,630) 93,272 (205,630) 93,272 (205,630) 124,025 (273,429) 124,025 (273,429) 124,025 (273,429) 
HHV Thermal Input, kWt 1,354,905 1,354,905 1,354,905 1,801,631 1,801,631 1,801,631 
LHV Thermal Input, kWt 1,222,936 1,222,936 1,222,936 1,626,150 1,626,150 1,626,150 
Raw Water Withdrawal, (m3/min)/MWnet (gpm/MWnet) 0.015 (4.0) 0.027 (7.1) 0.027 (7.2) 0.014 (3.6) 0.025 (6.6) 0.025 (6.7) 
Raw Water Consumption, (m3/min)/MWnet (gpm/MWnet) 0.012 (3.1) 0.018 (4.8) 0.018 (4.8) 0.011 (2.8) 0.017 (4.4) 0.017 (4.4) 
Note: Values shown are for total 2×2×1 system 
A Includes plant control systems, lighting, HVAC, and miscellaneous low voltage loads

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
39 
Exhibit A-2. Summary cost estimate data for F-frame greenfield cases 
Case B31A B31B.97 B32A B32B.97 
Turbine 7FA.05 7FA.05 7HA.02 7HA.02 
Capture Rate 0% 97% 0% 97% 
Bare Erected Cost by Account, $/1000 
  A3 – Feedwater & Misc. BOP Systems 66,159 78,645 82,401 97,937 
  A5 – Flue Gas Cleanup 0 311,908 0 369,925 
  A6 – Combustion Turbine and Accessories 82,353 82,353 159,892 159,892 
  A7 – HRSG, Ducting & Stack 83,482 79,623 127,656 121,983 
  A8 – Steam Turbine & Accessories 69,836 58,563 76,023 62,715 
  A9 – Cooling Water System 28,207 36,908 32,281 42,910 
  A11 – Accessory Electric Plant 29,946 51,715 37,066 63,454 
  A12 – Instrumentation & Controls 14,169 16,751 14,807 17,603 
  A13 – Improvements to Site 19,332 19,941 22,295 23,014 
  A14 – Building & Structures 14,087 13,184 16,029 14,931 
Total BEC, $/1000 407,571 749,592 568,450 974,365 
  Engineering CM, H.O.& Fee, $/1000 81,514 149,918 113,690 194,873 
  Process Contingencies, $/1000 0 48,810 0 58,255 
  Project Contingencies, $/1000 77,908 168,680 107,880 215,705 
TPC, $/1000 566,994 1,117,000 790,020 1,443,198 
TPC, $/kW 780 1,754 796 1,654 
TOC, $/1000 691,670 1,357,546 962,719 1,753,601 
TOC, $/kW 952 2,132 970 2,010 
TASC, $/1000 755,751 1,483,319 1,051,912 1,916,067 
TASC, $/kW 1,040 2,329 1,060 2,196 
First-Year Fuel Cost (100% CF), $/1000 179,012 179,012 238,034 238,034 
First-Year Fixed O&M Cost, $/1000 19,467 36,422 26,046 46,045 
First-Year Variable O&M Cost (100% CF), $/1000 10,854 23,528 14,690 30,494 
First-Year Total O&M (100% CF), $/1000 209,332 238,962 278,770 314,573 
Note: All costs are in real 2018 dollar

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
40 
Exhibit A-3. Summary costs of retrofit 
Case B31A-BR.97 B32A-BR.97 
Turbine 7FA.05 7HA.02 
Capture Rate 97% 97% 
Bare Erected Cost by Account, $/1000 
  A3 – Feedwater & Misc. BOP Systems 12,486 15,536 
  A5 – Gas Cleanup & Piping 311,908 369,925 
  A6 – Combustion Turbine and Accessories 0 0 
  A7 – HRSG, Ducting & Stack 0 0 
  A8 – Steam Turbine Generator  7,958 9,804 
  A9 – Cooling Water System 8,701 10,629 
  A11 – Accessory Electric Plant 23,046 28,198 
  A12 – Instrumentation & Controls 2,582 2,796 
  A13 – Improvements to Site 610 719 
  A14 – Building & Structures 233 289 
Total BEC, $/1000 367,524 437,897 
  Engineering CM, H.O.& Fee, $/1000 73,505 87,579 
  Process Contingencies, $/1000 48,201 57,625 
  Project Contingencies, $/1000 95,315 113,542 
Greenfield equivalent TPC, $/1000 584,545 696,643 
Greenfield equivalent TPC, $/kW 925 804 
Retrofit Difficulty Factor (RDF) 1.09 1.09 
TPC w/ RDF, $/1000 637,154 759,341 
TPC w/RDF, $/kW 1,008 876 
TOC w/ RDF, $/1000 770,830 918,744 
TOC w/ RDF, $/kW 1,219 1,060 
TASC w/ RDF, $/1000 842,245 1,003,863 
TASC w/ RDF, $/kW 1,332 1,158 
First-Year Fuel Cost (100% CF), $/1000 179,012 238,034 
First-Year Fixed O&M Cost, $/1000 37,441 47,327 
First-Year Variable O&M Cost (100% CF), $/1000 23,991 31,077 
First-Year Total O&M (100% CF), $/1000 240,444 316,438 
Note: All costs are in 2018 dollars

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
41 
Exhibit A-4. Summary LCOE of the retrofit cases 
Case B31A-BR.97 B32A-BR.97 
Turbine 7FA.05 7HA.02 
Capture Rate 97% 97% 
LCOE, Total [Including T&S] 61.1 57.5 
LCOE, Total [Including T&S and MPC] 65.6 61.8 
    Capital, $/MWh 12.7 11.0 
    Fixed, $/MWh 8.0 7.3 
    Variable, $/MWh 4.3 4.1 
    Fuel, $/MWh 32.3 31.3 
    CO2 T&S, $/MWh 3.8 3.7 
    Makeup power cost @ PSP = $30/MWh, $/MWh 4.5 4.3 
Cost of CO2 Captured [Excluding T&S], $/tonne CO2  61.1 56.2 
Cost of CO2 Avoided [Including T&S], $/tonne CO2  71.1 66.2 
Note: All costs are in real 2018 dollars, 85% capacity factor.

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
42 
APPENDIX B: COST ESTIMATE DETAILS 
Capital and O&M cost tables for the following cases are listed below. 
Case B31A-BR.90, 7FA.05 Turbines retrofitted with 90% Capture Rate 
Case B31A-BR.95, 7FA.05 Turbines retrofitted with 95% Capture Rate 
Case B31A-BR.97, 7FA.05 Turbines retrofitted with 97% Capture Rate 
Case B32A-BR.90, 7HA.02 Turbines retrofitted with 90% Capture Rate 
Case B32A-BR.95, 7HA.02 Turbines retrofitted with 95% Capture Rate 
Case B32A-BR.97, 7HA.02 Turbines retrofitted with 97% Capture Rate

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
43 
Exhibit B-1. B31A-BR.90 capital costs 
Case: B31A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 641 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $4 $1 $0 $1 $5 $0 
3.2 Water Makeup & Pretreating $1,339 $134 $759 $0 $2,231 $446 $0 $535 $3,213 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $1 $0 
3.4 Service Water Systems $406 $775 $2,511 $0 $3,693 $739 $0 $886 $5,318 $8 
3.7 Waste Water Treatment Equipment $3,990 $0 $2,445 $0 $6,435 $1,287 $0 $1,544 $9,266 $14 
 Subtotal $5,736 $912 $5,716 $0 $12,364 $2,473 $0 $2,967 $17,804 $28 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $101,663 $48,103 $101,017 $0 $250,783 $50,157 $45,141 $69,216 $415,297 $648 
5.4 Carbon Dioxide (CO2) Compression & Drying $26,989 $4,049 $11,197 $0 $42,234 $8,447 $0 $10,136 $60,817 $95 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $224 $36 $96 $0 $356 $71 $0 $85 $513 $1 
5.12 Gas Cleanup Foundations $0 $382 $413 $0 $795 $159 $0 $191 $1,145 $2 
 Subtotal $128,877 $52,570 $112,723 $0 $294,169 $58,834 $45,141 $79,629 $477,772 $746 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $5,278 $0 $2,139 $0 $7,417 $1,483 $0 $1,335 $10,236 $16 
 Subtotal $5,278 $0 $2,139 $0 $7,417 $1,483 $0 $1,335 $10,236 $16 
 9 Cooling Water System 
9.1 Cooling Towers $2,942 $0 $872 $0 $3,814 $763 $0 $687 $5,264 $8 
9.2 Circulating Water Pumps $389 $0 $27 $0 $416 $83 $0 $75 $574 $1 
9.3 Circulating Water System Auxiliaries $1,920 $0 $253 $0 $2,173 $435 $0 $391 $2,999 $5 
9.4 Circulating Water Piping $0 $684 $619 $0 $1,303 $261 $0 $235 $1,798 $3 
9.5 Make-up Water System $55 $0 $71 $0 $126 $25 $0 $23 $174 $0 
9.6 Component Cooling Water System $101 $0 $77 $0 $178 $36 $0 $32 $246 $0 
9.7 Circulating Water System Foundations $0 $158 $263 $0 $421 $84 $0 $101 $606 $1 
 Subtotal $5,407 $842 $2,183 $0 $8,432 $1,686 $0 $1,543 $11,661 $18 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,621 $0 $311 $0 $3,932 $786 $0 $708 $5,426 $8 
11.3 Switchgear & Motor Control $5,171 $0 $897 $0 $6,068 $1,214 $0 $1,092 $8,373 $13 
11.4 Conduit & Cable Tray $0 $1,249 $3,601 $0 $4,850 $970 $0 $873 $6,693 $10 
11.5 Wire & Cable $0 $1,865 $3,334 $0 $5,200 $1,040 $0 $936 $7,175 $11 
11.6 Protective Equipment $308 $0 $1,070 $0 $1,379 $276 $0 $248 $1,902 $3 
 Subtotal $9,100 $3,115 $9,213 $0 $21,428 $4,286 $0 $3,857 $29,571 $46 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $36 $0 $23 $0 $60 $12 $0 $11 $82 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
44 
Case: B31A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 641 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $58 $0 $37 $0 $95 $19 $0 $17 $132 $0 
12.4 Other Major Component Control Equipment $99 $0 $63 $0 $163 $33 $8 $30 $234 $0 
12.5 Signal Processing Equipment $82 $0 $3 $0 $84 $17 $0 $15 $116 $0 
12.6 Control Boards, Panels & Racks $22 $0 $13 $0 $35 $7 $2 $7 $50 $0 
12.7 Distributed Control System Equipment $1,216 $0 $38 $0 $1,254 $251 $63 $235 $1,803 $3 
12.8 Instrument Wiring & Tubing $100 $80 $322 $0 $502 $100 $25 $94 $722 $1 
12.9 Other Instrumentation & Controls Equipment $70 $0 $161 $0 $231 $46 $12 $43 $332 $1 
 Subtotal $1,683 $80 $661 $0 $2,424 $485 $109 $453 $3,471 $5 
 13 Improvements to Site 
13.1 Site Preparation $0 $19 $399 $0 $417 $83 $0 $100 $601 $1 
13.2 Site Improvements $0 $59 $81 $0 $140 $28 $0 $34 $202 $0 
13.3 Site Facilities $58 $0 $61 $0 $119 $24 $0 $28 $171 $0 
 Subtotal $58 $78 $540 $0 $676 $135 $0 $162 $974 $2 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $24 $12 $0 $35 $7 $0 $6 $49 $0 
14.6 Water Treatment Buildings $0 $100 $91 $0 $191 $38 $0 $34 $263 $0 
 Subtotal $0 $124 $102 $0 $226 $45 $0 $41 $312 $0 
 Pre-Retrofit Difficulty Factor Total $156,139 $57,720 $133,277 $0 $347,137 $69,427 $45,250 $89,987 $551,801 $861 
 Retrofit Adjusted Total    $601,463 $939

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
45 
Exhibit B-2. B31A-BR.90 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $2,986 $5 
1 Month Maintenance Materials $617 $1 
1 Month Non-fuel Consumables $406 $1 
1 Month Waste Disposal $7 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $12,029 $19 
Total $16,045 $25 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $682 $1 
0.5% of TPC (spare parts) $3,007 $5 
Total $3,689 $6 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $90,219 $141 
Financing Costs $16,240 $25 
Total Overnight Costs (TOC) $727,657 $1,136 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $795,072 $1,241

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
46 
Exhibit B-3. B31A-BR.90 O&M costs 
Case: B31A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  641 Heat Rate-net (Btu/kWh): 7,218 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $4.33 
Maintenance Labor:     $8,502,838 $13.27 
Administrative & Support Labor:     $2,819,867 $4.40 
Property Taxes and Insurance:     $22,375,890 $34.93 
Total:     $36,475,223 $56.95 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $12,754,257 $2.67 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $1,895,852 $0.40 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $1,634,796 $0.34 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $325,533 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $847,299 $144,041 $0.03 
CO2 Capture System ChemicalsA: Proprietary $1,969,571 $0.41 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $931,690 $0.20 
Subtotal:       $847,299 $6,901,483 $1.45 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $2,401 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $47,955 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $20,643 $0.00 
Subtotal:       $0 $70,998 $0.01 
Variable Operating Costs Total:       $847,299 $19,726,739 $4.14 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $152,160,133 $31.90 
Total:       $0 $152,160,133 $31.90 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
47 
Exhibit B-4. B31A-BR.95 capital costs 
Case: B31A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 636 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $4 $1 $0 $1 $5 $0 
3.2 Water Makeup & Pretreating $1,363 $136 $773 $0 $2,272 $454 $0 $545 $3,272 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $1 $0 
3.4 Service Water Systems $414 $790 $2,557 $0 $3,761 $752 $0 $903 $5,416 $9 
3.7 Waste Water Treatment Equipment $4,045 $0 $2,479 $0 $6,524 $1,305 $0 $1,566 $9,395 $15 
 Subtotal $5,824 $928 $5,810 $0 $12,562 $2,512 $0 $3,015 $18,089 $28 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $106,145 $49,875 $104,737 $0 $260,757 $52,151 $46,936 $71,969 $431,813 $679 
5.4 Carbon Dioxide (CO2) Compression & Drying $27,597 $4,140 $11,449 $0 $43,186 $8,637 $0 $10,365 $62,188 $98 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $235 $37 $101 $0 $372 $74 $0 $89 $536 $1 
5.12 Gas Cleanup Foundations $0 $399 $431 $0 $830 $166 $0 $199 $1,195 $2 
 Subtotal $133,977 $54,451 $116,717 $0 $305,145 $61,029 $46,936 $82,622 $495,733 $780 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $5,481 $0 $2,221 $0 $7,703 $1,541 $0 $1,387 $10,630 $17 
 Subtotal $5,481 $0 $2,221 $0 $7,703 $1,541 $0 $1,387 $10,630 $17 
 9 Cooling Water System 
9.1 Cooling Towers $2,996 $0 $889 $0 $3,885 $777 $0 $699 $5,361 $8 
9.2 Circulating Water Pumps $396 $0 $27 $0 $423 $85 $0 $76 $584 $1 
9.3 Circulating Water System Auxiliaries $1,953 $0 $258 $0 $2,211 $442 $0 $398 $3,051 $5 
9.4 Circulating Water Piping $0 $696 $630 $0 $1,326 $265 $0 $239 $1,830 $3 
9.5 Make-up Water System $56 $0 $72 $0 $128 $26 $0 $23 $177 $0 
9.6 Component Cooling Water System $103 $0 $79 $0 $181 $36 $0 $33 $250 $0 
9.7 Circulating Water System Foundations $0 $161 $267 $0 $428 $86 $0 $103 $617 $1 
 Subtotal $5,503 $857 $2,222 $0 $8,582 $1,716 $0 $1,570 $11,869 $19 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,784 $0 $325 $0 $4,108 $822 $0 $740 $5,670 $9 
11.3 Switchgear & Motor Control $5,403 $0 $937 $0 $6,340 $1,268 $0 $1,141 $8,749 $14 
11.4 Conduit & Cable Tray $0 $1,306 $3,762 $0 $5,068 $1,014 $0 $912 $6,994 $11 
11.5 Wire & Cable $0 $1,949 $3,484 $0 $5,433 $1,087 $0 $978 $7,497 $12 
11.6 Protective Equipment $326 $0 $1,132 $0 $1,458 $292 $0 $262 $2,012 $3 
 Subtotal $9,512 $3,255 $9,640 $0 $22,407 $4,481 $0 $4,033 $30,922 $49 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $38 $0 $24 $0 $62 $12 $0 $11 $85 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
48 
Case: B31A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 636 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $60 $0 $39 $0 $99 $20 $0 $18 $136 $0 
12.4 Other Major Component Control Equipment $103 $0 $66 $0 $169 $34 $8 $32 $243 $0 
12.5 Signal Processing Equipment $84 $0 $3 $0 $87 $17 $0 $16 $120 $0 
12.6 Control Boards, Panels & Racks $22 $0 $14 $0 $36 $7 $2 $7 $52 $0 
12.7 Distributed Control System Equipment $1,265 $0 $40 $0 $1,305 $261 $65 $245 $1,876 $3 
12.8 Instrument Wiring & Tubing $105 $84 $335 $0 $523 $105 $26 $98 $751 $1 
12.9 Other Instrumentation & Controls Equipment $73 $0 $168 $0 $240 $48 $12 $45 $345 $1 
 Subtotal $1,750 $84 $687 $0 $2,520 $504 $114 $471 $3,609 $6 
 13 Improvements to Site 
13.1 Site Preparation $0 $18 $377 $0 $395 $79 $0 $95 $569 $1 
13.2 Site Improvements $0 $56 $76 $0 $133 $27 $0 $32 $191 $0 
13.3 Site Facilities $55 $0 $58 $0 $112 $22 $0 $27 $162 $0 
 Subtotal $55 $74 $512 $0 $640 $128 $0 $154 $922 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $24 $12 $0 $36 $7 $0 $6 $50 $0 
14.6 Water Treatment Buildings $0 $102 $92 $0 $194 $39 $0 $35 $268 $0 
 Subtotal $0 $126 $104 $0 $230 $46 $0 $41 $318 $0 
 Pre-Retrofit Difficulty Factor Total $162,103 $59,774 $137,914 $0 $359,790 $71,958 $47,050 $93,293 $572,091 $900 
 Retrofit Adjusted Total    $623,579 $981

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
49 
Exhibit B-5. B31A-BR.95 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $3,083 $5 
1 Month Maintenance Materials $639 $1 
1 Month Non-fuel Consumables $422 $1 
1 Month Waste Disposal $7 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $12,472 $20 
Total $16,623 $26 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $711 $1 
0.5% of TPC (spare parts) $3,118 $5 
Total $3,829 $6 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $93,537 $147 
Financing Costs $16,837 $26 
Total Overnight Costs (TOC) $754,405 $1,186 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $824,298 $1,296

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
50 
Exhibit B-6. B31A-BR.95 O&M costs 
Case: B31A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  636 Heat Rate-net (Btu/kWh): 7,270 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $4.37 
Maintenance Labor:     $8,657,045 $13.61 
Administrative & Support Labor:     $2,858,418 $4.50 
Property Taxes and Insurance:     $22,781,697 $35.83 
Total:     $37,073,788 $58.30 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $12,985,567 $2.74 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $1,908,434 $0.40 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $1,645,645 $0.35 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $325,651 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $847,299 $144,041 $0.03 
CO2 Capture System ChemicalsA: Proprietary $2,055,608 $0.43 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $983,451 $0.21 
Subtotal:       $847,299 $7,062,830 $1.49 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $2,401 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $50,619 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $21,582 $0.00 
Subtotal:       $0 $74,602 $0.02 
Variable Operating Costs Total:       $847,299 $20,123,000 $4.25 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $152,160,133 $32.14 
Total:       $0 $152,160,133 $32.14 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
51 
Exhibit B-7. B31A-BR.97 capital costs 
Case: B31A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 632 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $4 $1 $0 $1 $5 $0 
3.2 Water Makeup & Pretreating $1,383 $138 $784 $0 $2,305 $461 $0 $553 $3,319 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $1 $0 
3.4 Service Water Systems $420 $801 $2,594 $0 $3,815 $763 $0 $916 $5,493 $9 
3.7 Waste Water Treatment Equipment $3,944 $0 $2,417 $0 $6,361 $1,272 $0 $1,527 $9,160 $14 
 Subtotal $5,748 $942 $5,796 $0 $12,486 $2,497 $0 $2,996 $17,980 $28 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $108,714 $51,104 $107,319 $0 $267,137 $53,427 $48,085 $73,730 $442,378 $700 
5.4 Carbon Dioxide (CO2) Compression & Drying $27,829 $4,175 $11,545 $0 $43,549 $8,710 $0 $10,452 $62,711 $99 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $239 $38 $102 $0 $379 $76 $0 $91 $546 $1 
5.12 Gas Cleanup Foundations $0 $405 $438 $0 $844 $169 $0 $202 $1,215 $2 
 Subtotal $136,782 $55,722 $119,404 $0 $311,908 $62,382 $48,085 $84,475 $506,850 $802 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $5,663 $0 $2,295 $0 $7,958 $1,592 $0 $1,432 $10,981 $17 
 Subtotal $5,663 $0 $2,295 $0 $7,958 $1,592 $0 $1,432 $10,981 $17 
 9 Cooling Water System 
9.1 Cooling Towers $3,039 $0 $902 $0 $3,940 $788 $0 $709 $5,438 $9 
9.2 Circulating Water Pumps $402 $0 $27 $0 $429 $86 $0 $77 $592 $1 
9.3 Circulating Water System Auxiliaries $1,979 $0 $261 $0 $2,240 $448 $0 $403 $3,091 $5 
9.4 Circulating Water Piping $0 $705 $639 $0 $1,344 $269 $0 $242 $1,855 $3 
9.5 Make-up Water System $57 $0 $73 $0 $130 $26 $0 $23 $180 $0 
9.6 Component Cooling Water System $104 $0 $80 $0 $184 $37 $0 $33 $254 $0 
9.7 Circulating Water System Foundations $0 $163 $271 $0 $434 $87 $0 $104 $625 $1 
 Subtotal $5,580 $868 $2,253 $0 $8,701 $1,740 $0 $1,592 $12,034 $19 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,890 $0 $334 $0 $4,224 $845 $0 $760 $5,828 $9 
11.3 Switchgear & Motor Control $5,554 $0 $964 $0 $6,518 $1,304 $0 $1,173 $8,994 $14 
11.4 Conduit & Cable Tray $0 $1,342 $3,868 $0 $5,210 $1,042 $0 $938 $7,190 $11 
11.5 Wire & Cable $0 $2,004 $3,581 $0 $5,585 $1,117 $0 $1,005 $7,707 $12 
11.6 Protective Equipment $338 $0 $1,173 $0 $1,510 $302 $0 $272 $2,084 $3 
 Subtotal $9,781 $3,346 $9,919 $0 $23,046 $4,609 $0 $4,148 $31,804 $50 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $38 $0 $25 $0 $63 $13 $0 $11 $87 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
52 
Case: B31A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 632 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $61 $0 $39 $0 $101 $20 $0 $18 $139 $0 
12.4 Other Major Component Control Equipment $106 $0 $68 $0 $173 $35 $9 $33 $249 $0 
12.5 Signal Processing Equipment $86 $0 $3 $0 $89 $18 $0 $16 $122 $0 
12.6 Control Boards, Panels & Racks $23 $0 $14 $0 $37 $7 $2 $7 $53 $0 
12.7 Distributed Control System Equipment $1,297 $0 $41 $0 $1,337 $267 $67 $251 $1,923 $3 
12.8 Instrument Wiring & Tubing $107 $86 $343 $0 $536 $107 $27 $100 $770 $1 
12.9 Other Instrumentation & Controls Equipment $74 $0 $172 $0 $246 $49 $12 $46 $354 $1 
 Subtotal $1,793 $86 $704 $0 $2,582 $516 $116 $482 $3,697 $6 
 13 Improvements to Site 
13.1 Site Preparation $0 $17 $359 $0 $376 $75 $0 $90 $542 $1 
13.2 Site Improvements $0 $54 $73 $0 $126 $25 $0 $30 $182 $0 
13.3 Site Facilities $52 $0 $55 $0 $107 $21 $0 $26 $154 $0 
 Subtotal $52 $70 $487 $0 $610 $122 $0 $146 $878 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $24 $12 $0 $37 $7 $0 $7 $50 $0 
14.6 Water Treatment Buildings $0 $103 $94 $0 $197 $39 $0 $35 $272 $0 
 Subtotal $0 $128 $106 $0 $233 $47 $0 $42 $322 $1 
 Pre-Retrofit Difficulty Factor Total $165,399 $61,162 $140,964 $0 $367,524 $73,505 $48,201 $95,315 $584,545 $925 
 Retrofit Adjusted Total    $637,154 $1,008

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
53 
Exhibit B-8. B31A-BR.97 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $3,142 $5 
1 Month Maintenance Materials $653 $1 
1 Month Non-fuel Consumables $434 $1 
1 Month Waste Disposal $8 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $12,743 $20 
Total $16,980 $27 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $734 $1 
0.5% of TPC (spare parts) $3,186 $5 
Total $3,920 $6 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $95,573 $151 
Financing Costs $17,203 $27 
Total Overnight Costs (TOC) $770,830 $1,219 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $842,245 $1,332

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
54 
Exhibit B-9. B31A-BR.97 O&M costs 
Case: B31A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  632 Heat Rate-net (Btu/kWh): 7,313 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $4.39 
Maintenance Labor:     $8,751,694 $13.84 
Administrative & Support Labor:     $2,882,080 $4.56 
Property Taxes and Insurance:     $23,030,773 $36.43 
Total:     $37,441,175 $59.23 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $13,127,541 $2.79 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $1,918,423 $0.41 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $1,654,259 $0.35 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $325,528 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $847,299 $144,041 $0.03 
CO2 Capture System ChemicalsA: Proprietary $2,142,137 $0.46 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $1,004,155 $0.21 
Subtotal:       $847,299 $7,188,542 $1.53 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $2,401 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $51,684 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $22,520 $0.00 
Subtotal:       $0 $76,605 $0.02 
Variable Operating Costs Total:       $847,299 $20,392,688 $4.33 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $152,160,133 $32.33 
Total:       $0 $152,160,133 $32.33 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
55 
Exhibit B-10. B32A-BR.90 capital costs 
Case: B32A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 878 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $5 $1 $0 $1 $7 $0 
3.2 Water Makeup & Pretreating $1,673 $167 $948 $0 $2,789 $558 $0 $669 $4,016 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $2 $0 
3.4 Service Water Systems $508 $969 $3,139 $0 $4,616 $923 $0 $1,108 $6,648 $8 
3.7 Waste Water Treatment Equipment $4,942 $0 $3,029 $0 $7,972 $1,594 $0 $1,913 $11,479 $13 
 Subtotal $7,126 $1,140 $7,118 $0 $15,384 $3,077 $0 $3,692 $22,152 $25 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $122,385 $57,227 $120,178 $0 $299,790 $59,958 $53,962 $82,742 $496,452 $565 
5.4 Carbon Dioxide (CO2) Compression & Drying $30,338 $4,551 $12,586 $0 $47,475 $9,495 $0 $11,394 $68,364 $78 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $284 $45 $122 $0 $451 $90 $0 $108 $649 $1 
5.12 Gas Cleanup Foundations $0 $479 $517 $0 $996 $199 $0 $239 $1,434 $2 
 Subtotal $153,007 $62,302 $133,403 $0 $348,712 $69,742 $53,962 $94,483 $566,900 $646 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $6,503 $0 $2,635 $0 $9,138 $1,828 $0 $1,645 $12,611 $14 
 Subtotal $6,503 $0 $2,635 $0 $9,138 $1,828 $0 $1,645 $12,611 $14 
 9 Cooling Water System 
9.1 Cooling Towers $3,677 $0 $1,092 $0 $4,768 $954 $0 $858 $6,580 $7 
9.2 Circulating Water Pumps $485 $0 $33 $0 $517 $103 $0 $93 $714 $1 
9.3 Circulating Water System Auxiliaries $2,267 $0 $299 $0 $2,566 $513 $0 $462 $3,541 $4 
9.4 Circulating Water Piping $0 $828 $750 $0 $1,578 $316 $0 $284 $2,178 $2 
9.5 Make-up Water System $64 $0 $82 $0 $146 $29 $0 $26 $202 $0 
9.6 Component Cooling Water System $122 $0 $94 $0 $216 $43 $0 $39 $298 $0 
9.7 Circulating Water System Foundations $0 $192 $318 $0 $510 $102 $0 $122 $734 $1 
 Subtotal $6,614 $1,020 $2,668 $0 $10,302 $2,060 $0 $1,885 $14,247 $16 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $4,391 $0 $377 $0 $4,768 $954 $0 $858 $6,580 $7 
11.3 Switchgear & Motor Control $6,270 $0 $1,088 $0 $7,358 $1,472 $0 $1,324 $10,154 $12 
11.4 Conduit & Cable Tray $0 $1,515 $4,367 $0 $5,882 $1,176 $0 $1,059 $8,117 $9 
11.5 Wire & Cable $0 $2,262 $4,043 $0 $6,305 $1,261 $0 $1,135 $8,701 $10 
11.6 Protective Equipment $420 $0 $1,457 $0 $1,877 $375 $0 $338 $2,590 $3 
 Subtotal $11,081 $3,777 $11,332 $0 $26,190 $5,238 $0 $4,714 $36,143 $41 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $39 $0 $25 $0 $64 $13 $0 $11 $88 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
56 
Case: B32A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 878 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $62 $0 $40 $0 $102 $20 $0 $18 $141 $0 
12.4 Other Major Component Control Equipment $108 $0 $69 $0 $176 $35 $9 $33 $254 $0 
12.5 Signal Processing Equipment $87 $0 $3 $0 $90 $18 $0 $16 $124 $0 
12.6 Control Boards, Panels & Racks $23 $0 $14 $0 $38 $8 $2 $7 $54 $0 
12.7 Distributed Control System Equipment $1,319 $0 $41 $0 $1,361 $272 $68 $255 $1,956 $2 
12.8 Instrument Wiring & Tubing $109 $87 $349 $0 $545 $109 $27 $102 $784 $1 
12.9 Other Instrumentation & Controls Equipment $76 $0 $175 $0 $250 $50 $13 $47 $360 $0 
 Subtotal $1,823 $87 $716 $0 $2,626 $525 $119 $490 $3,760 $4 
 13 Improvements to Site 
13.1 Site Preparation $0 $22 $469 $0 $491 $98 $0 $118 $706 $1 
13.2 Site Improvements $0 $70 $95 $0 $165 $33 $0 $40 $237 $0 
13.3 Site Facilities $68 $0 $72 $0 $140 $28 $0 $33 $201 $0 
 Subtotal $68 $92 $635 $0 $795 $159 $0 $191 $1,145 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $30 $15 $0 $45 $9 $0 $8 $62 $0 
14.6 Water Treatment Buildings $0 $123 $112 $0 $235 $47 $0 $42 $324 $0 
 Subtotal $0 $153 $127 $0 $280 $56 $0 $50 $386 $0 
 Pre-Retrofit Difficulty Factor Total $186,222 $68,571 $158,633 $0 $413,426 $82,685 $54,081 $107,151 $657,343 $749 
 Retrofit Adjusted Total    $716,504 $816

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
57 
Exhibit B-11. B32A-BR.90 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $3,488 $4 
1 Month Maintenance Materials $735 $1 
1 Month Non-fuel Consumables $540 $1 
1 Month Waste Disposal $9 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $14,330 $16 
Total $19,102 $22 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $907 $1 
0.5% of TPC (spare parts) $3,583 $4 
Total $4,489 $5 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $107,476 $122 
Financing Costs $19,346 $22 
Total Overnight Costs (TOC) $866,916 $987 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $947,233 $1,079

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
58 
Exhibit B-12. B32A-BR.90 O&M costs 
Case: B32A-BR.90 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  878 Heat Rate-net (Btu/kWh): 7,001 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $3.16 
Maintenance Labor:     $10,999,957 $12.53 
Administrative & Support Labor:     $3,444,146 $3.92 
Property Taxes and Insurance:     $28,947,255 $32.97 
Total:     $46,167,986 $52.58 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $16,499,935 $2.52 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $2,416,896 $0.37 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $2,084,093 $0.32 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $432,821 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $1,129,110 $191,949 $0.03 
CO2 Capture System ChemicalsA: Proprietary $2,619,004 $0.40 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $1,238,900 $0.19 
Subtotal:       $1,129,110 $8,983,662 $1.37 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $3,199 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $63,767 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $27,450 $0.00 
Subtotal:       $0 $94,416 $0.01 
Variable Operating Costs Total:       $1,129,110 $25,578,014 $3.91 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $202,328,910 $30.95 
Total:       $0 $202,328,910 $30.95 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
59 
Exhibit B-13. B32A-BR.95 capital costs 
Case: B32A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 872 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $5 $1 $0 $1 $7 $0 
3.2 Water Makeup & Pretreating $1,704 $170 $966 $0 $2,840 $568 $0 $682 $4,090 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $2 $0 
3.4 Service Water Systems $517 $987 $3,197 $0 $4,701 $940 $0 $1,128 $6,770 $8 
3.7 Waste Water Treatment Equipment $5,011 $0 $3,071 $0 $8,082 $1,616 $0 $1,940 $11,638 $13 
 Subtotal $7,234 $1,160 $7,235 $0 $15,630 $3,126 $0 $3,751 $22,507 $26 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $127,873 $59,335 $124,603 $0 $311,812 $62,362 $56,126 $86,060 $516,360 $592 
5.4 Carbon Dioxide (CO2) Compression & Drying $31,017 $4,653 $12,868 $0 $48,537 $9,707 $0 $11,649 $69,893 $80 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $297 $47 $127 $0 $472 $94 $0 $113 $679 $1 
5.12 Gas Cleanup Foundations $0 $500 $540 $0 $1,039 $208 $0 $249 $1,497 $2 
 Subtotal $159,187 $64,534 $138,138 $0 $361,860 $72,372 $56,126 $98,072 $588,429 $675 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $6,754 $0 $2,737 $0 $9,490 $1,898 $0 $1,708 $13,097 $15 
 Subtotal $6,754 $0 $2,737 $0 $9,490 $1,898 $0 $1,708 $13,097 $15 
 9 Cooling Water System 
9.1 Cooling Towers $3,744 $0 $1,112 $0 $4,856 $971 $0 $874 $6,701 $8 
9.2 Circulating Water Pumps $493 $0 $33 $0 $527 $105 $0 $95 $727 $1 
9.3 Circulating Water System Auxiliaries $2,305 $0 $304 $0 $2,610 $522 $0 $470 $3,601 $4 
9.4 Circulating Water Piping $0 $843 $763 $0 $1,606 $321 $0 $289 $2,216 $3 
9.5 Make-up Water System $65 $0 $84 $0 $149 $30 $0 $27 $205 $0 
9.6 Component Cooling Water System $124 $0 $95 $0 $220 $44 $0 $40 $303 $0 
9.7 Circulating Water System Foundations $0 $195 $324 $0 $519 $104 $0 $124 $747 $1 
 Subtotal $6,732 $1,037 $2,715 $0 $10,484 $2,097 $0 $1,918 $14,500 $17 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $4,597 $0 $394 $0 $4,992 $998 $0 $899 $6,889 $8 
11.3 Switchgear & Motor Control $6,564 $0 $1,139 $0 $7,703 $1,541 $0 $1,387 $10,630 $12 
11.4 Conduit & Cable Tray $0 $1,586 $4,571 $0 $6,158 $1,232 $0 $1,108 $8,497 $10 
11.5 Wire & Cable $0 $2,368 $4,233 $0 $6,601 $1,320 $0 $1,188 $9,109 $10 
11.6 Protective Equipment $445 $0 $1,545 $0 $1,990 $398 $0 $358 $2,747 $3 
 Subtotal $11,606 $3,954 $11,883 $0 $27,444 $5,489 $0 $4,940 $37,872 $43 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $40 $0 $26 $0 $66 $13 $0 $12 $91 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
60 
Case: B32A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 872 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $64 $0 $41 $0 $106 $21 $0 $19 $146 $0 
12.4 Other Major Component Control Equipment $112 $0 $72 $0 $184 $37 $9 $34 $264 $0 
12.5 Signal Processing Equipment $90 $0 $3 $0 $93 $19 $0 $17 $128 $0 
12.6 Control Boards, Panels & Racks $24 $0 $15 $0 $39 $8 $2 $7 $57 $0 
12.7 Distributed Control System Equipment $1,374 $0 $43 $0 $1,417 $283 $71 $266 $2,037 $2 
12.8 Instrument Wiring & Tubing $114 $91 $363 $0 $568 $114 $28 $106 $816 $1 
12.9 Other Instrumentation & Controls Equipment $79 $0 $182 $0 $261 $52 $13 $49 $375 $0 
 Subtotal $1,897 $91 $745 $0 $2,733 $547 $123 $510 $3,913 $4 
 13 Improvements to Site 
13.1 Site Preparation $0 $21 $445 $0 $466 $93 $0 $112 $671 $1 
13.2 Site Improvements $0 $66 $90 $0 $157 $31 $0 $38 $225 $0 
13.3 Site Facilities $65 $0 $68 $0 $133 $27 $0 $32 $191 $0 
 Subtotal $65 $87 $604 $0 $755 $151 $0 $181 $1,088 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $31 $15 $0 $46 $9 $0 $8 $63 $0 
14.6 Water Treatment Buildings $0 $125 $114 $0 $239 $48 $0 $43 $330 $0 
 Subtotal $0 $156 $129 $0 $285 $57 $0 $51 $393 $0 
 Pre-Retrofit Difficulty Factor Total $193,475 $71,021 $164,186 $0 $428,681 $85,736 $56,250 $111,132 $681,799 $782 
 Retrofit Adjusted Total    $743,161 $852

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
61 
Exhibit B-14. B32A-BR.95 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $3,604 $4 
1 Month Maintenance Materials $762 $1 
1 Month Non-fuel Consumables $561 $1 
1 Month Waste Disposal $10 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $14,863 $17 
Total $19,800 $23 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $945 $1 
0.5% of TPC (spare parts) $3,716 $4 
Total $4,661 $5 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $111,474 $128 
Financing Costs $20,065 $23 
Total Overnight Costs (TOC) $899,161 $1,031 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $982,466 $1,127

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
62 
Exhibit B-15. B32A-BR.95 O&M costs 
Case: B32A-BR.95 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  872 Heat Rate-net (Btu/kWh): 7,051 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $3.18 
Maintenance Labor:     $11,185,819 $12.83 
Administrative & Support Labor:     $3,490,612 $4.00 
Property Taxes and Insurance:     $29,436,367 $33.76 
Total:     $46,889,426 $53.78 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $16,778,729 $2.58 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $2,433,611 $0.37 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $2,098,506 $0.32 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $432,979 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $1,129,110 $191,949 $0.03 
CO2 Capture System ChemicalsA: Proprietary $2,733,410 $0.42 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $1,307,727 $0.20 
Subtotal:       $1,129,110 $9,198,183 $1.42 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $3,199 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $67,310 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $28,699 $0.00 
Subtotal:       $0 $99,207 $0.02 
Variable Operating Costs Total:       $1,129,110 $26,076,120 $4.02 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $202,328,910 $31.17 
Total:       $0 $202,328,910 $31.17 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
63 
Exhibit B-16. B32A-BR.97 capital costs 
Case: B32A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 867 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $1 $2 $1 $0 $5 $1 $0 $1 $7 $0 
3.2 Water Makeup & Pretreating $1,728 $173 $979 $0 $2,881 $576 $0 $691 $4,148 $5 
3.3 Other Feedwater Subsystems $1 $0 $0 $0 $1 $0 $0 $0 $2 $0 
3.4 Service Water Systems $524 $1,001 $3,242 $0 $4,768 $954 $0 $1,144 $6,866 $8 
3.7 Waste Water Treatment Equipment $4,886 $0 $2,995 $0 $7,881 $1,576 $0 $1,891 $11,348 $13 
 Subtotal $7,141 $1,177 $7,218 $0 $15,536 $3,107 $0 $3,728 $22,372 $26 
 5 Flue Gas Cleanup 
5.1 CANSOLV Carbon Dioxide (CO2) Removal System $130,962 $60,798 $127,675 $0 $319,434 $63,887 $57,498 $88,164 $528,983 $610 
5.4 Carbon Dioxide (CO2) Compression & Drying $31,283 $4,693 $12,978 $0 $48,954 $9,791 $0 $11,749 $70,494 $81 
5.5 Carbon Dioxide (CO2) Compressor Aftercooler $302 $48 $130 $0 $480 $96 $0 $115 $691 $1 
5.12 Gas Cleanup Foundations $0 $508 $549 $0 $1,057 $211 $0 $254 $1,522 $2 
 Subtotal $162,547 $66,046 $141,331 $0 $369,925 $73,985 $57,498 $100,282 $601,690 $694 
 8 Steam Turbine & Accessories 
8.4 Steam Piping $6,977 $0 $2,827 $0 $9,804 $1,961 $0 $1,765 $13,530 $16 
 Subtotal $6,977 $0 $2,827 $0 $9,804 $1,961 $0 $1,765 $13,530 $16 
 9 Cooling Water System 
9.1 Cooling Towers $3,797 $0 $1,128 $0 $4,925 $985 $0 $886 $6,796 $8 
9.2 Circulating Water Pumps $500 $0 $34 $0 $534 $107 $0 $96 $737 $1 
9.3 Circulating Water System Auxiliaries $2,336 $0 $308 $0 $2,644 $529 $0 $476 $3,649 $4 
9.4 Circulating Water Piping $0 $854 $773 $0 $1,627 $325 $0 $293 $2,246 $3 
9.5 Make-up Water System $66 $0 $85 $0 $151 $30 $0 $27 $208 $0 
9.6 Component Cooling Water System $126 $0 $97 $0 $222 $44 $0 $40 $307 $0 
9.7 Circulating Water System Foundations $0 $198 $328 $0 $526 $105 $0 $126 $757 $1 
 Subtotal $6,825 $1,051 $2,753 $0 $10,629 $2,126 $0 $1,945 $14,700 $17 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $4,721 $0 $405 $0 $5,126 $1,025 $0 $923 $7,074 $8 
11.3 Switchgear & Motor Control $6,741 $0 $1,170 $0 $7,911 $1,582 $0 $1,424 $10,917 $13 
11.4 Conduit & Cable Tray $0 $1,629 $4,694 $0 $6,323 $1,265 $0 $1,138 $8,726 $10 
11.5 Wire & Cable $0 $2,432 $4,347 $0 $6,779 $1,356 $0 $1,220 $9,355 $11 
11.6 Protective Equipment $460 $0 $1,599 $0 $2,059 $412 $0 $371 $2,842 $3 
 Subtotal $11,922 $4,061 $12,215 $0 $28,198 $5,640 $0 $5,076 $38,914 $45 
 12 Instrumentation & Control 
12.1 Natural Gas Combined Cycle Control Equipment $41 $0 $26 $0 $67 $13 $0 $12 $93 $0

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
64 
Case: B32A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Estimate Type: Conceptual Plant Size (MW, net): 867 Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/kW 
12.3 Steam Turbine Control Equipment $66 $0 $42 $0 $108 $22 $0 $19 $149 $0 
12.4 Other Major Component Control Equipment $115 $0 $73 $0 $188 $38 $9 $35 $270 $0 
12.5 Signal Processing Equipment $92 $0 $3 $0 $95 $19 $0 $17 $131 $0 
12.6 Control Boards, Panels & Racks $25 $0 $15 $0 $40 $8 $2 $8 $58 $0 
12.7 Distributed Control System Equipment $1,406 $0 $44 $0 $1,450 $290 $73 $272 $2,085 $2 
12.8 Instrument Wiring & Tubing $116 $93 $372 $0 $581 $116 $29 $109 $835 $1 
12.9 Other Instrumentation & Controls Equipment $81 $0 $186 $0 $267 $53 $13 $50 $384 $0 
 Subtotal $1,941 $93 $762 $0 $2,796 $559 $126 $522 $4,004 $5 
 13 Improvements to Site 
13.1 Site Preparation $0 $20 $424 $0 $444 $89 $0 $107 $639 $1 
13.2 Site Improvements $0 $63 $86 $0 $149 $30 $0 $36 $215 $0 
13.3 Site Facilities $62 $0 $65 $0 $126 $25 $0 $30 $182 $0 
 Subtotal $62 $83 $575 $0 $719 $144 $0 $173 $1,036 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $31 $15 $0 $47 $9 $0 $8 $64 $0 
14.6 Water Treatment Buildings $0 $127 $115 $0 $242 $48 $0 $44 $334 $0 
 Subtotal $0 $158 $131 $0 $289 $58 $0 $52 $398 $0 
 Pre-Retrofit Difficulty Factor Total $197,416 $72,669 $167,812 $0 $437,897 $87,579 $57,625 $113,542 $696,643 $804 
 Retrofit Adjusted Total    $759,341 $876

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
65 
Exhibit B-17. B32A-BR.97 owner’s costs 
Description $/1,000  $/kW 
Pre-Production Costs 
6 Months All Labor $3,674 $4 
1 Month Maintenance Materials $779 $1 
1 Month Non-fuel Consumables $577 $1 
1 Month Waste Disposal $10 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $15,187 $18 
Total $20,227 $23 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $976 $1 
0.5% of TPC (spare parts) $3,797 $4 
Total $4,772 $6 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $0 $0 
Other Owner's Costs $113,901 $131 
Financing Costs $20,502 $24 
Total Overnight Costs (TOC) $918,744 $1,060 
TASC Multiplier (IOU, 33 year) 1.093   
Total As-Spent Cost (TASC) $1,003,863 $1,158

COST AND PERFORMANCE OF RETROFITTING NGCC UNITS FOR CARBON CAPTURE – REVISION 3  
66 
Exhibit B-18. B32A-BR.97 O&M costs 
Case: B32A-BR.97 – 2x1 CT NGCC w/ CO₂ Capture Cost Base: Dec 2018 
Plant Size (MW, net):  867 Heat Rate-net (Btu/kWh): 7,091 Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50 $/hour Skilled Operator: 1.0  
  Operating Labor Burden:  30.00 % of base Operator: 3.3  
  Labor O-H Charge Rate:  25.00 % of labor Foreman: 1.0  
    Lab Techs, etc.: 1.0  
    Total: 6.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/kW-net) 
Annual Operating Labor:     $2,776,628 $3.20 
Maintenance Labor:     $11,298,639 $13.03 
Administrative & Support Labor:     $3,518,817 $4.06 
Property Taxes and Insurance:     $29,733,260 $34.30 
Total:     $47,327,343 $54.59 
Variable Operating Costs 
     ($) ($/MWh-net) 
Maintenance Material:     $16,947,958 $2.63 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 3,216 $1.90 $0 $2,446,871 $0.38 
Makeup and Waste Water 
Treatment Chemicals (ton): 0 9.6 $550 $0 $2,109,940 $0.33 
Ammonia (19 wt%, ton): 0 3.50 $300 $0 $432,815 $0.07 
SCR Catalyst (ft3): 5,649 3.10 $150 $1,129,110 $191,949 $0.03 
CO2 Capture System ChemicalsA: Proprietary $2,848,471 $0.44 
Triethylene Glycol (gal): w/equip. 442 $6.80 $0 $1,335,259 $0.21 
Subtotal:       $1,129,110 $9,365,304 $1.45 
Waste Disposal 
SCR Catalyst (ft3): 0 3.10 $2.50 $0 $3,199 $0.00 
Triethylene Glycol (gal): 0 442 $0.35 $0 $68,727 $0.01 
Thermal Reclaimer Unit Waste (ton): 0 1.751 $38.0 $0 $29,946 $0.00 
Subtotal:       $0 $101,872 $0.02 
Variable Operating Costs Total:       $1,129,110 $26,415,133 $4.09 
Fuel Cost 
Natural Gas (MMBtu): 0 110,955 $4.42 $0 $202,328,910 $31.34 
Total:       $0 $202,328,910 $31.34 
ACO2 Capture System Chemicals includes NaOH and CANSOLV Solvent

www.netl.doe.gov 
Albany, OR • Anchorage, AK • Morgantown, WV • Pittsburgh, PA • Sugar Land, TX 
(800) 553-7681
