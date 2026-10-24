---
source_id: "netl"
title: "Cost of Capturing CO2 from Industrial Sources 2022"
url: "https://netl.doe.gov/projects/files/CostofCapturingCO2fromIndustrialSources_071522.pdf"
retrieved_at: "2026-10-24T04:53:06+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "CCS", "H2", "PWR"]
disciplines: ["PRC", "MAT"]
sha256: "1f9682335755950b22ee03e514f1519271aec7c6d43fc2e8bb64ca207eddf1df"
collected: "manual"
---

# Cost of Capturing CO2 from Industrial Sources 2022

COST OF CAPTURING CO2 
FROM INDUSTRIAL SOURCES 
 
SYDNEY HUGHES, ALEXANDER ZOELLE 
 
 
 July 15, 2022

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

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
 
Sydney Hughes1,2: Methodology, Software, Validation, Formal Analysis, Writing – 
Original Draft, Writing – Review & Editing, Visualization, Supervision; Alex Zoelle1,2: 
Methodology, Software, Validation, Formal Analysis, Writing – Original Draft, 
Writing – Review & Editing, Visualization, Supervision; Mark Woods1,2: 
Methodology, Writing – Review & Editing, Supervision; Sam Henry1,2: Software, 
Formal Analysis, Writing – Review & Editing; Sally Homsy1,2: Formal Analysis, 
Supervision; Sandeep Pidaparti1,2: Formal Analysis; Norma Kuehn1,2: Formal 
Analysis; Hannah Hoffman1,2: Writing – Review & Editing; Katie Forrest1,2: Writing – 
Review & Editing; Alana Sheriff1,2: Writing – Review & Editing; Tim Fout2*: 
Conceptualization, Methodology, Writing – Review & Editing, Supervision; W. 
Morgan Summers2: Writing – Original Draft, Conceptualization; Steve Herron2,3: 
Writing – Original Draft, Conceptualization 
 
*Corresponding contact: Tim.Fout@netl.doe.gov, 304-285-1341 
1National Energy Technology Laboratory (NETL) Support Contractor 
2NETL 
3Former NETL support contractor 
 
This report was peer reviewed by three independent peer reviewers with various 
affiliations and from relevant scientific disciplines to ensure that information presented is 
based on sound and credible science and considered technically adequate, 
competently performed, properly documented, and in compliance with established 
quality requirements. As a step beyond standard internal quality assurance and quality 
control procedures, the U.S. Department of Energy (DOE) Office of Fossil Energy and 
Carbon Management (FECM)/NETL are committed to rigorous peer review of key work 
products to meet the quality standards of the research community. The following 
individuals served on the peer review panel: 
 Richard Bohan, Portland Cement Association 
 Michael Matuszewski, AristoSys, LLC 
 Technical expert (anonymity requested) 
 
 
 
 
 
Suggested Citation: 
S. Hughes and A. Zoelle, "Cost of Capturing CO2 from Industrial Sources," National 
Energy Technology Laboratory, Pittsburgh, July 15, 2022. 
 
 
The authors wish to acknowledge the excellent guidance, contributions, and 
cooperation of the NETL staff, particularly: 
 
Timothy Fout, Technical Lead, Energy Process Analysis Team 
Travis Shultz, Supervisor, Energy Process Analysis Team

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
 
This page intentionally left blank.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
i  
TABLE OF CONTENTS 
List of Exhibits ................................................................................................................ vi 
List of Equations ............................................................................................................. x 
Acronyms and Abbreviations ...................................................................................... xi 
Executive Summary ...................................................................................................... 1 
1 Introduction ............................................................................................................ 9 
1.1 Assumptions ...................................................................................................... 9 
2 Plant Sites and CO2 End-Use ............................................................................... 11 
3 Economic Analysis Overview .............................................................................. 20 
3.1 Cost Estimating Methodology ...................................................................... 20 
3.1.1 Capital Costs ........................................................................................... 21 
3.1.2 Operation and Maintenance Costs ...................................................... 24 
3.2 Capital Charge Factors ................................................................................ 25 
3.3 Retrofit Factors ............................................................................................... 27 
4 Equipment ............................................................................................................. 28 
4.1 Compression ................................................................................................... 28 
4.1.1 Reciprocating Compressor .................................................................... 28 
4.1.2 Centrifugal Compressor .......................................................................... 28 
4.2 CO2 Capture and Purification ...................................................................... 29 
4.2.1 Cansolv Post-Combustion Capture ....................................................... 30 
4.2.2 ADIP-Ultra Pre-Combustion Capture ..................................................... 32 
4.3 Industrial Boiler ................................................................................................ 33 
4.4 Cooling Water Unit......................................................................................... 33 
4.5 Heat Exchangers ............................................................................................ 34 
4.6 Ancillary Equipment, Buildings, and Structures ........................................... 34 
5 Cost and Performance: High Purity Sources ...................................................... 35 
5.1 Ammonia ........................................................................................................ 35 
5.1.1 Size Range ................................................................................................ 35 
5.1.2 CO2 Point Sources ................................................................................... 35 
5.1.3 Design Input and Assumptions ............................................................... 36 
5.1.4 CO2 Capture System ............................................................................... 37 
5.1.5 BFD, Stream Table, and Performance Summary .................................. 37 
5.1.6 Capture Integration ................................................................................ 38 
5.1.7 Power Source ........................................................................................... 38 
5.1.8 Economic Analysis Results ...................................................................... 39

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
ii  
5.1.9 Plant Capacity Sensitivity Analysis ......................................................... 42 
5.1.10 Ammonia Conclusion .......................................................................... 42 
5.2 Ethylene Oxide ............................................................................................... 43 
5.2.1 Size Range ................................................................................................ 43 
5.2.2 CO2 Point Sources ................................................................................... 44 
5.2.3 Design Input and Assumptions ............................................................... 44 
5.2.4 CO2 Capture System ............................................................................... 44 
5.2.5 BFD, Stream Table, and Performance Summary .................................. 45 
5.2.6 Capture Integration ................................................................................ 46 
5.2.7 Power Source ........................................................................................... 46 
5.2.8 Economic Analysis Results ...................................................................... 47 
5.2.9 Plant Capacity Sensitivity Analysis ......................................................... 50 
5.2.10 Ethylene Oxide Conclusion ................................................................. 50 
5.3 Ethanol ............................................................................................................ 51 
5.3.1 Size Range ................................................................................................ 51 
5.3.2 CO2 Point Sources ................................................................................... 51 
5.3.3 Design Input and Assumptions ............................................................... 52 
5.3.4 CO2 Capture System ............................................................................... 53 
5.3.5 BFD, Stream Table, and Performance Summary .................................. 54 
5.3.6 Capture Integration ................................................................................ 55 
5.3.7 Power Source ........................................................................................... 56 
5.3.8 Economic Analysis Results ...................................................................... 56 
5.3.9 Plant Capacity Sensitivity Analysis ......................................................... 59 
5.3.10 Ethanol Conclusion .............................................................................. 59 
5.4 Natural Gas Processing ................................................................................. 60 
5.4.1 Size Range ................................................................................................ 60 
5.4.2 CO2 Point Sources ................................................................................... 61 
5.4.3 Design Input and Assumptions ............................................................... 61 
5.4.4 CO2 Capture System ............................................................................... 61 
5.4.5 BFD, Stream Table, and Performance Summary .................................. 61 
5.4.6 Capture Integration ................................................................................ 63 
5.4.7 Power Source ........................................................................................... 63 
5.4.8 Economic Analysis Results ...................................................................... 63 
5.4.9 Plant Capacity Sensitivity Analysis ......................................................... 67 
5.4.10 Natural Gas Processing Conclusion ................................................... 67 
5.5 Coal-to-Liquids ............................................................................................... 68

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
iii  
5.5.1 Size Range ................................................................................................ 68 
5.5.2 CO2 Point Sources ................................................................................... 68 
5.5.3 Design Input and Assumptions ............................................................... 68 
5.5.4 CO2 Capture System ............................................................................... 69 
5.5.5 BFD, Stream Table, and Performance Summary .................................. 69 
5.5.6 Capture Integration ................................................................................ 70 
5.5.7 Power Source ........................................................................................... 71 
5.5.8 Economic Analysis Results ...................................................................... 71 
5.5.9 Plant Capacity Sensitivity Analysis ......................................................... 74 
5.5.10 Coal-to-Liquids Conclusion ................................................................. 74 
5.6 Gas-to-Liquids ................................................................................................. 74 
5.6.1 Size Range ................................................................................................ 75 
5.6.2 CO2 Point Sources ................................................................................... 75 
5.6.3 Design Input and Assumptions ............................................................... 75 
5.6.4 CO2 Capture System ............................................................................... 75 
5.6.5 BFD, Stream Table, and Performance Summary .................................. 76 
5.6.6 Capture Integration ................................................................................ 77 
5.6.7 Power Source ........................................................................................... 77 
5.6.8 Economic Analysis Results ...................................................................... 77 
5.6.9 Plant Capacity Sensitivity Analysis ......................................................... 80 
5.6.10 Gas-to-Liquids Conclusion ................................................................... 81 
6 Cost and Performance: Low Purity Sources ...................................................... 82 
6.1 Refinery Hydrogen ......................................................................................... 82 
6.1.1 Size Range ................................................................................................ 82 
6.1.2 CO2 Point Sources ................................................................................... 82 
6.1.3 Design Input and Assumptions ............................................................... 83 
6.1.4 CO2 Capture System ............................................................................... 83 
6.1.5 BFD, Stream Table, and Performance Summary .................................. 84 
6.1.6 Capture Integration ................................................................................ 87 
6.1.7 Power Source ........................................................................................... 87 
6.1.8 Economic Analysis Results ...................................................................... 87 
6.1.9 Plant Capacity Sensitivity Analysis ......................................................... 94 
6.1.10 Refinery Hydrogen Conclusion ........................................................... 95 
6.2 Cement ........................................................................................................... 96 
6.2.1 Size Range ................................................................................................ 98 
6.2.2 CO2 Point Sources ................................................................................... 98

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
iv  
6.2.3 Design Input and Assumptions ............................................................... 99 
6.2.4 CO2 Capture System ............................................................................... 99 
6.2.5 BFD, Stream Table, and Performance Summary .................................. 99 
6.2.6 Capture Integration .............................................................................. 102 
6.2.7 Power Source ......................................................................................... 102 
6.2.8 Economic Analysis Results .................................................................... 102 
6.2.9 Plant Capacity Sensitivity Analysis ....................................................... 109 
6.2.10 FGD + SCR Sensitivity Case................................................................ 110 
6.2.11 Cement Conclusion ........................................................................... 119 
6.3 Iron/Steel ....................................................................................................... 120 
6.3.1 Size Range .............................................................................................. 120 
6.3.2 CO2 Point Sources ................................................................................. 120 
6.3.3 Design Input and Assumptions ............................................................. 121 
6.3.4 CO2 Capture System ............................................................................. 122 
6.3.5 BFD, Stream Table, and Performance Summary ................................ 122 
6.3.6 Capture Integration .............................................................................. 128 
6.3.7 Power Source ......................................................................................... 128 
6.3.8 Economic Analysis Results .................................................................... 128 
6.3.9 Plant Capacity Sensitivity Analysis ....................................................... 138 
6.3.10 Iron/Steel Conclusion ......................................................................... 139 
7 Economic Analysis .............................................................................................. 140 
7.1 Economic Results ......................................................................................... 140 
7.1.1 Cost and Performance Summaries ..................................................... 141 
7.2 Sensitivity Analyses ....................................................................................... 144 
7.2.1 Capital Charge Factor ......................................................................... 144 
7.2.2 Retrofit Factor ........................................................................................ 145 
7.2.3 Purchased Power Price ......................................................................... 146 
7.2.4 Natural Gas Price .................................................................................. 147 
7.2.5 Capacity Factor .................................................................................... 148 
8 Conclusion .......................................................................................................... 150 
9 Future Work ......................................................................................................... 152 
9.1 In-depth Process Analysis ............................................................................ 152 
9.2 Multiple Process Scenario ........................................................................... 152 
9.3 Additional Processes .................................................................................... 153 
9.4 Techno-economic Analysis of CO2 Distribution to EOR Fields ................. 153 
9.5 Life Extension Costs for Existing Facilities .................................................... 153

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
v  
10 References .......................................................................................................... 154 
Appendix: Carbon Balances ................................................................................... 159

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
vi  
LIST OF EXHIBITS 
Exhibit ES-1. Industrial sources of CO2 case summary ............................................... 1 
Exhibit ES-2. COC from industrial sources .................................................................... 3 
Exhibit ES-3. Capture system BEC and amount of CO2 captured versus capture 
rate ................................................................................................................................. 4 
Exhibit ES-4. COC versus CO2 partial pressure and CO2 concentration ................. 5 
Exhibit ES-5. U.S. industrial CO2 emissions by industry ................................................. 7 
Exhibit ES-6. Representative plant COC results versus U.S. industrial CO2 emissions
 ........................................................................................................................................ 7 
Exhibit 1-1. Process design assumptions .................................................................... 10 
Exhibit 2-1. Existing CO2 pipelines and active EOR injection sites .......................... 12 
Exhibit 2-2. Ammonia plant locations and existing CO2 pipelines and EOR 
injection sites ............................................................................................................... 13 
Exhibit 2-3. EO plant locations and existing CO2 pipelines and EOR injection sites
 ...................................................................................................................................... 14 
Exhibit 2-4. Ethanol plant locations and existing CO2 pipelines and EOR injection 
sites ............................................................................................................................... 15 
Exhibit 2-5. NGP plant locations and existing CO2 pipelines and EOR injection 
sites ............................................................................................................................... 16 
Exhibit 2-6. Refinery hydrogen (U.S. refineries) plant locations and existing CO2 
pipelines and EOR injection sites ............................................................................... 17 
Exhibit 2-7. Cement plant locations and existing CO2 pipelines and EOR injection 
sites ............................................................................................................................... 18 
Exhibit 2-8. Steel (BOF) plant locations and existing CO2 pipelines and EOR 
injection sites ............................................................................................................... 19 
Exhibit 3-1. Capital cost levels and their elements .................................................. 22 
Exhibit 3-2. Estimated amounts for owner’s costs .................................................... 23 
Exhibit 3-3. Financial assumptions for high purity sources ....................................... 26 
Exhibit 3-4. Financial assumptions for low purity sources ......................................... 26 
Exhibit 4-1. Reciprocating compressor cases specifications .................................. 28 
Exhibit 4-2. Integrally geared centrifugal compressor cases specifications ......... 29 
Exhibit 4-3. Shell’s Cansolv CO2 capture typical process flow diagram ................ 30 
Exhibit 4-4. ADIP-Ultra CO2 capture typical process flow diagram ........................ 32 
Exhibit 5-1. Ammonia production via NG reforming ............................................... 36 
Exhibit 5-2. Ammonia CO2 capture BFD ................................................................... 37 
Exhibit 5-3. Ammonia stream table ........................................................................... 37 
Exhibit 5-4. Performance summary ............................................................................ 38 
Exhibit 5-5. Owner’s costs for ammonia greenfield site ........................................... 39 
Exhibit 5-6. Capital costs for ammonia greenfield site ............................................ 40 
Exhibit 5-7. Initial and annual O&M costs for ammonia greenfield site ................. 41 
Exhibit 5-8. COC for 394,000 tonnes/year ammonia greenfield and retrofitA ....... 41 
Exhibit 5-9. Ammonia plant capacity sensitivity ....................................................... 42 
Exhibit 5-10. 2007 U.S. EO production facility capacities......................................... 43

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
vii  
Exhibit 5-11. EO CO2 capture BFD ............................................................................. 45 
Exhibit 5-12. EO stream table ..................................................................................... 45 
Exhibit 5-13. Performance summary .......................................................................... 46 
Exhibit 5-14. Owner’s costs for EO greenfield site .................................................... 47 
Exhibit 5-15. Capital costs for EO greenfield site ...................................................... 48 
Exhibit 5-16. Initial and annual O&M costs for EO greenfield site ........................... 49 
Exhibit 5-17. COC for 364,500 tonnes/year EO greenfield and retrofit .................. 49 
Exhibit 5-18. EO plant capacity sensitivity ................................................................. 50 
Exhibit 5-19 U.S. Ethanol plant capacities and quantities ....................................... 51 
Exhibit 5-20. U.S. ethanol plant locations .................................................................. 53 
Exhibit 5-21. Ethanol CO2 capture BFD ..................................................................... 54 
Exhibit 5-22. Ethanol stream table ............................................................................. 54 
Exhibit 5-23. Performance summary .......................................................................... 55 
Exhibit 5-24. Owner’s costs for ethanol greenfield site ............................................ 56 
Exhibit 5-25. Capital costs for ethanol greenfield site.............................................. 57 
Exhibit 5-26. Initial and annual O&M costs for ethanol greenfield site .................. 58 
Exhibit 5-27. COC for 50 M gallons/year ethanol greenfield and retrofit .............. 58 
Exhibit 5-28. Ethanol plant capacity sensitivity ......................................................... 59 
Exhibit 5-29. Michigan basin producing formation raw gas characteristics ......... 60 
Exhibit 5-30. NGP CO2 capture BFD........................................................................... 61 
Exhibit 5-31. NGP stream table .................................................................................. 62 
Exhibit 5-32. Performance summary .......................................................................... 63 
Exhibit 5-33. Owner’s costs for NGP greenfield site .................................................. 64 
Exhibit 5-34. Capital and costs for NGP greenfield site ........................................... 65 
Exhibit 5-35. Initial and annual O&M costs for NGP greenfield site ........................ 66 
Exhibit 5-36. COC for 330 MMSCFD NGP greenfield and retrofit ............................ 66 
Exhibit 5-37. NGP plant capacity sensitivity .............................................................. 67 
Exhibit 5-38. CTL CO2 capture BFD ............................................................................ 69 
Exhibit 5-39. CTL stream table .................................................................................... 69 
Exhibit 5-40. Performance summary .......................................................................... 70 
Exhibit 5-41. Owner’s costs for CTL greenfield site ................................................... 71 
Exhibit 5-42. Capital costs for CTL greenfield site ..................................................... 72 
Exhibit 5-43. Initial and annual O&M costs for CTL greenfield site .......................... 73 
Exhibit 5-44. COC for 50,000 BPD CTL greenfield ..................................................... 73 
Exhibit 5-45. CTL plant capacity sensitivity ................................................................ 74 
Exhibit 5-46. GTL CO2 capture BFD ............................................................................ 76 
Exhibit 5-47. GTL stream table .................................................................................... 76 
Exhibit 5-48. Performance summary .......................................................................... 77 
Exhibit 5-49. Owners’ costs for GTL greenfield site ................................................... 78 
Exhibit 5-50. Capital costs for GTL greenfield site ..................................................... 79 
Exhibit 5-51. Initial and annual O&M costs for GTL greenfield site ......................... 80 
Exhibit 5-52. COC for 50,000 BPD GTL greenfield ..................................................... 80 
Exhibit 5-53. GTL plant capacity sensitivity ............................................................... 81 
Exhibit 6-1. Stream characteristics of raw syngas from SMR ................................... 83

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
viii  
Exhibit 6-2. CO2 capture BFD ..................................................................................... 84 
Exhibit 6-3. Refinery hydrogen stream table for 99 percent capture .................... 85 
Exhibit 6-4. Refinery hydrogen stream table for 90 percent capture .................... 86 
Exhibit 6-5. Refinery hydrogen performance summary ........................................... 87 
Exhibit 6-6. Owners’ costs for refinery hydrogen cases ........................................... 88 
Exhibit 6-7. Capital costs for refinery hydrogen greenfield site with 99 percent 
capture ........................................................................................................................ 89 
Exhibit 6-8. Capital costs for refinery hydrogen greenfield site with 90 percent 
capture ........................................................................................................................ 90 
Exhibit 6-9. Initial and annual O&M costs for refinery hydrogen greenfield site with 
99 percent capture .................................................................................................... 92 
Exhibit 6-10. Initial and annual O&M costs for refinery hydrogen greenfield site 
with 90 percent capture ............................................................................................ 93 
Exhibit 6-11. COC for 87,000 tonnes H2/year refinery hydrogen cases .................. 93 
Exhibit 6-12. Refinery hydrogen plant capacity sensitivity ...................................... 94 
Exhibit 6-13. Refinery H2 capture system BEC and amount of CO2 captured versus 
capture rate ................................................................................................................ 95 
Exhibit 6-14. USGS cement production trends .......................................................... 96 
Exhibit 6-15. 2019 U.S. PC fuel consumption ............................................................. 97 
Exhibit 6-16. PC production process .......................................................................... 97 
Exhibit 6-17. St. Mary’s cement plant characteristics .............................................. 98 
Exhibit 6-18. Cement CO2 capture BFD .................................................................. 100 
Exhibit 6-19. Cement stream table for 99 percent capture .................................. 100 
Exhibit 6-20. Cement stream table for 90 percent capture .................................. 101 
Exhibit 6-21. Performance summary ........................................................................ 102 
Exhibit 6-22. Owners’ costs for cement cases ........................................................ 103 
Exhibit 6-23. Capital costs for cement greenfield site with 99 percent capture 104 
Exhibit 6-24. Capital costs for cement greenfield site with 90 percent capture 105 
Exhibit 6-25. Initial and annual O&M costs for cement greenfield site with 99 
percent capture ....................................................................................................... 107 
Exhibit 6-26. Initial and annual O&M costs for cement greenfield site with 90 
percent capture ....................................................................................................... 108 
Exhibit 6-27. COC for 1.3 M tonnes/year cement cases ....................................... 108 
Exhibit 6-28. Cement plant capacity sensitivity ..................................................... 109 
Exhibit 6-29. Cement capture system BEC and amount of CO2 captured versus 
capture rate .............................................................................................................. 110 
Exhibit 6-30. Capital costs for cement greenfield site with FGD and SCR and 99 
percent CO2 capture ............................................................................................... 112 
Exhibit 6-31. Capital costs for cement greenfield site with FGD and SCR and 90 
percent CO2 capture ............................................................................................... 113 
Exhibit 6-32. Owners’ costs for cement cases with FGD and SCR ........................ 116 
Exhibit 6-33. Initial and annual O&M costs for cement greenfield site with FGD 
and SCR at 99 percent capture .............................................................................. 117

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
ix  
Exhibit 6-34. Initial and annual O&M costs for cement greenfield site with FGD 
and SCR at 90 percent capture .............................................................................. 118 
Exhibit 6-35. COC for 1.3 M tonnes/year cement greenfield cases (base cases 
and FGD + SCR cases) ............................................................................................. 119 
Exhibit 6-36. BOF iron and steel plant characteristics [52] .................................... 121 
Exhibit 6-37. Braddock steel mill plot plan .............................................................. 121 
Exhibit 6-38. CO2 capture BFD for COG/BFS ........................................................... 122 
Exhibit 6-39. Iron/steel COG/BFS stream table with 99 percent capture ............ 123 
Exhibit 6-40. Iron/steel COG/BFS stream table with 90 percent capture ............ 124 
Exhibit 6-41. CO2 capture BFD for COG PPS ........................................................... 125 
Exhibit 6-42. Iron/steel COG PPS stream table with 99 percent capture ............ 125 
Exhibit 6-43. Iron/steel COG PPS stream table with 90 percent capture ............ 126 
Exhibit 6-44. Performance summary for iron/steel COG/BFS section ................... 127 
Exhibit 6-45. Performance summary for iron/steel COG PPS section ................... 127 
Exhibit 6-46. Owners’ costs for iron/steel retrofit cases .......................................... 129 
Exhibit 6-47. Capital costs for iron/steel COG/BFS section retrofit with 99 percent 
capture ...................................................................................................................... 130 
Exhibit 6-48. Capital costs for iron/steel COG PPS retrofit with 99 percent capture
 .................................................................................................................................... 131 
Exhibit 6-49. Capital costs for iron/steel COG/BFS section retrofit with 90 percent 
capture ...................................................................................................................... 133 
Exhibit 6-50. Capital costs for iron/steel COG PPS retrofit with 90 percent capture
 .................................................................................................................................... 134 
Exhibit 6-51. Initial and annual O&M costs for iron/steel site with 99 percent 
capture ...................................................................................................................... 136 
Exhibit 6-52. Initial and annual O&M costs for an iron/steel retrofit site with 90 
percent capture ....................................................................................................... 137 
Exhibit 6-53. COC for 2.54 M tonnes/year iron/steel retrofit cases ....................... 137 
Exhibit 6-54. Iron/steel plant capacity sensitivity .................................................... 138 
Exhibit 6-55. Iron/steel capture system BEC and amount of CO2 captured versus 
capture rate .............................................................................................................. 139 
Exhibit 7-1. COC summary ....................................................................................... 140 
Exhibit 7-2. Cost and performance summary comparison – high purity cases .. 142 
Exhibit 7-3. Cost and performance summary comparison – low purity cases .... 143 
Exhibit 7-4. COC vs. CCF .......................................................................................... 144 
Exhibit 7-5. COC vs. retrofit factor ........................................................................... 146 
Exhibit 7-6. COC vs. purchased power price ......................................................... 147 
Exhibit 7-7. COC vs. NG price .................................................................................. 148 
Exhibit 7-8. COC vs. CF ............................................................................................. 149 
Exhibit A-1. Ethanol case carbon balance ............................................................ 159 
Exhibit A-2. Ammonia case carbon balance ........................................................ 159 
Exhibit A-3. NGP case carbon balance.................................................................. 159 
Exhibit A-4. EO case carbon balance .................................................................... 160 
Exhibit A-5. CTL case carbon balance ................................................................... 160

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
x  
Exhibit A-6. GTL case carbon balance ................................................................... 160 
Exhibit A-7. Refinery hydrogen case with 99 percent capture carbon balance 160 
Exhibit A-8. Refinery hydrogen case with 90 percent capture carbon balance 161 
Exhibit A-9. Iron/steel case COG/BFS stream with 99 percent capture carbon 
balance ..................................................................................................................... 161 
Exhibit A-10. Iron/steel case COG/BFS stream with 90 percent capture carbon 
balance ..................................................................................................................... 161 
Exhibit A-11. Steel case COG PPS stream with 99 percent capture carbon 
balance ..................................................................................................................... 162 
Exhibit A-12. Steel case COG PPS stream with 90 percent capture carbon 
balance ..................................................................................................................... 162 
Exhibit A-13. Cement 99 percent capture case carbon balance ...................... 162 
Exhibit A-14. Cement 90 percent capture case carbon balance ...................... 162 
 
LIST OF EQUATIONS 
Equation ES-1 ................................................................................................................. 2 
Equation 1-1 ................................................................................................................... 9 
Equation 5-1 ................................................................................................................. 43 
Equation 5-2 ................................................................................................................. 52

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
xi  
ACRONYMS AND ABBREVIATIONS 
°C Degrees Celsius 
°F Degrees Fahrenheit 
AACE AACE International (formerly 
Association for the 
Advancement of Cost 
Engineering)  
abs Absolute 
AGR Acid gas removal 
Ar Argon 
Aspen Aspen Plus® 
atm Atmosphere 
B Billion 
BBR4 Cost and Performance Baseline 
for Fossil Energy Plants 
Volume 1: Bituminous Coal 
and Natural Gas to 
Electricity, Revision 4 
BEC Bare erected cost  
BFD Block flow diagram 
BFS Blast furnace stove 
BOF Basic oxygen furnace 
BPD Barrels per day 
Btu British thermal unit 
C2H6 Ethane 
C3H8 Propane 
C4H10 Butane 
CCF Capital charge factor 
CCS Carbon capture and 
storage/sequestration 
CCSI Carbon Capture Simulation 
Initiative 
CF Capacity factor 
CH4 Methane 
CH4S Methanethiol 
CO Carbon monoxide 
COC Cost of CO2 capture 
CO2 Carbon dioxide 
COG Coke oven gas 
CTL Coal-to-liquids 
DOE Department of Energy 
EAF Electric arc furnace 
Eng’g CM H.O & Fee Engineering 
construction management 
home office and fees 
EO Ethylene oxide  
EOR Enhanced oil recovery 
EPC Engineering/procurement/ 
construction 
EPCC Engineering, procurement, and 
construction cost  
EPRI Electric Power Research 
Institute 
FGD Flue gas desulfurization 
ft3 Cubic foot 
FT Fischer-Tropsch 
gal Gallon 
GHG Greenhouse gas 
gpm Gallons per minute 
GTL Gas-to-liquids 
h, hr Hour 
H2 Hydrogen 
H2O Water 
H2S Hydrogen sulfide 
He Helium 
HHV Higher heating value 
HX Heat exchanger 
I&C instrumentation and control 
IEAGHG IEA Greenhouse Gas R&D 
Programme 
kg Kilogram 
kJ Kilojoule 
KO Knockout 
kW, kWe Kilowatt electric 
lb Pound 
LHV Lower heating value 
M Million 
m3 Cubic meter 
MEA Monoethanethiol 
MMBtu Million British thermal units 
MMCFD  Million cubic feet per day 
MMSCFD  Million standard cubic feet per 
day 
mol% Mole percent 
MPa Megapascal 
MW, MWe Megawatt electric 
MWh Megawatt-hour 
N/A Not applicable/available 
N2 Nitrogen

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
xii  
NaOH Sodium hydroxide 
NETL National Energy Technology 
Laboratory 
NG Natural gas 
NGP Natural gas processing 
NOx Oxides of nitrogen 
O&M Operation and maintenance 
O2 Oxygen 
O-H Overhead 
PC Portland cement 
PPS Power plant stack 
PSA Pressure swing adsorption 
psia Pound per square inch 
absolute 
psig Pound per square inch gauge 
QGESS Quality Guidelines for Energy 
System Studies 
R&D Research and development 
scf Standard cubic feet 
SCR Selective catalytic reduction 
SMR Steam methane reforming 
SO2 Sulfur dioxide 
SOx Oxides of sulfur 
T&S Transport and storage  
TAG® Technical Assessment Guide 
TASC Total as-spent cost 
TEG Triethylene glycol 
TOC Total overnight cost 
tonne Metric ton (1,000 kg) 
TPC Total plant cost 
U.S. United States 
USD U.S. dollar 
USDA U.S. Department of Agriculture 
USGS United States Geological 
Survey 
V-L Vapor-liquid 
yr Year

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
1 
EXECUTIVE SUMMARY 
The objective of this report is to provide an estimate of the cost to capture carbon dioxide (CO2) 
from selected industrial processes. The following nine processes were chosen for analysis due to 
either the high purity of the CO2 emission source (99–100 mole percent CO2) or the large 
quantity of CO2 potentially available. The processes considered in this study are summarized in 
Exhibit ES-1, where “CO2 Available for Capture” represents the amount of pure CO2 in the 
capture stream described in the table for each case, at a 100 percent capacity factor (CF). 
Exhibit ES-1. Industrial sources of CO2 case summary 
Case 
Class Process 
Base Plant 
Production 
Capacity  
Capture Stream Description 
CO2 Available for Capture 
(M tonnes CO2/year) 
High 
Purity 
Ammonia 394,000 tonnes/year Stripping vent: 23.52 psia 0.486 
Ethylene Oxide 364,500 tonnes/year Acid gas removal CO2 stream: 43.5 psia 0.122 
Ethanol 50 M gal/year Fermenter off-gas: 17.40 psia 0.143 
Natural Gas 
Processing  330 MMSCFD CO2 vent: 23.52 psia 0.649 
Coal-to-Liquids 50,000 BPD AGR CO2 streams: 160 psia, 265 psia, and 300 psia 8.74 
Gas-to-Liquids 50,000 BPD AGR CO2 stream: 265 psia 1.86 
Low 
Purity 
Refinery 
Hydrogen 87,000 tonnes/year Raw syngas from SMR: 399.9 psia 0.405 
Cement 1.3 M tonnes/year Kiln off-gas: 14.7 psia 1.21 
Steel/Iron 2.54 M tonnes/year COG PPS: 14.7 psia COG/BFS: 14.7 psia 3.74 (total of both capture streams) 
Note: COG = coke oven gas; PPS = power plant stack; BFS = blast furnace stove 
For each industrial process considered, available plant information, such as existing average 
plant size, projected new development plant size, or existing plant operations data was used to 
develop a reference plant for this study. Plant size is one factor affecting the amount of CO2 
available for capture from an industrial process. Other factors are specific to each industry. For 
example, the ammonia industry captures and re-uses CO2 in urea production, and natural gas 
processing (NGP) plant CO2 emissions are dependent upon the raw gas compositions entering 
the facility. As such, specific assumptions related to CO2 availability are necessary to establish 
each representative plant and to suggest the industry’s average CO2 emissions.  
For each process, the CO2 capture cost for a greenfield facility and a retrofit facility was 
calculated with the latter being calculated by applying a retrofit factor to the greenfield total 
plant cost (TPC). For the iron/steel process, only a retrofit case is given since the representative

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
2 
plant is a basic oxygen furnace facility, which are no longer being constructed. For the coal-to-
liquids (CTL) and gas-to-liquids (GTL) cases, no retrofit case is given, since no plants currently 
exist domestically, and it is assumed that none will be constructed without CO2 capture. The 
cost metric of interest is the cost of CO2 captured in U.S. dollars per tonne, as calculated in 
Equation ES-1. In this report, costs are presented in December 2018 real dollars. 
 
Equation ES-1 
 
Where: 
TOC – Total overnight costs of equipment added for the application of CO2 capture 
CCF – Capital charge factor, based on industry-specific financial assumptions as detailed in 
Section 3.2 
FOM – Annual fixed operating & maintenance (O&M) costs 
VOM – Annual variable O&M costs 
PF – Purchased fuel 
PP – Purchased power 
The high purity emissions sources are inherently produced by their base plants at CO2 
concentrations suitable for pipeline transport, requiring only compression, associated 
intercooling, and, in some cases, glycol dehydration. The low purity sources considered offer 
emission streams with CO2 concentrations below that which is acceptable for pipeline use, per 
guidance in National Energy Technology Laboratory’s (NETL) “Quality Guidelines for Energy 
System Studies (QGESS): CO2 Impurity Design Parameters” specifications. [1] As such, the 
refinery hydrogen, cement, and iron/steel cases require CO2 removal systems along with 
compression, associated intercooling, and glycol dehydration. For the CO2 removal systems, two 
capture rates were evaluated, 90 and 99 percent, to evaluate the cost of capturing the CO2 from 
the emissions streams defined in Exhibit ES-1.a 
Exhibit ES-2 provides the resulting greenfield and retrofit cost of CO2 capture (COC), where 
appropriate, for each case considered in this study, along with the capital, variable and fixed 
O&M, purchased power and/or natural gas (NG) fuel cost components for each case. For each 
case, other than those of iron/steel, the individual cost components shown (i.e., capital costs, 
fixed O&M costs, variable O&M costs, and purchased power/natural gas) represent the cost 
components that add to the total COC in greenfield applications. For iron/steel, those individual 
cost components represent retrofit costs. In addition, each high purity source shows the total 
retrofit COC, which is estimated based on methodology described in Section 3.3, except for the 
CTL and GTL cases. As there are no existing CTL or GTL plants in the domestic industrial fleet, it 
 
a This report does not consider capture of the CO2 produced by the natural gas-fired boiler used for steam generation in 
the low purity cases (i.e., for solvent regeneration) or other process streams outside of those defined in Exhibit ES-1. If this 
CO2 was captured, it would greatly impact the results presented herein. Such an analysis is discussed in the future work 
considerations detailed in Section 9. 
𝐶𝑂𝐶 ( $𝑡𝑜𝑛𝑛𝑒 𝐶𝑂2) = 𝑇𝑂𝐶 ∗ 𝐶𝐶𝐹 + 𝐹𝑂𝑀 + 𝑉𝑂𝑀 + 𝑃𝐹 + 𝑃𝑃𝑡𝑜𝑛𝑛𝑒𝑠 𝐶𝑂2 𝑐𝑎𝑝𝑡𝑢𝑟𝑒𝑑 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
3 
is assumed that future (i.e., greenfield) builds would include carbon capture (i.e., retrofit 
capture applications at CTL or GTL facilities would not be expected). Further details regarding 
the estimation of capital, operating, and maintenance costs are provided within the body of the 
report. 
Exhibit ES-2. COC from industrial sources 
Case Capital Costs Fixed O&M Costs Variable O&M Costs Purchased Power/ Natural Gas Greenfield COC Retrofit  COC 
Ammonia 6.1 3.9 2.7 6.3 19.0 19.0 
Ethylene Oxide 9.4 9.8 1.7 5.2 26.0 26.2 
Ethanol 14.1 9.2 1.7 6.8 31.8 32.0 
NGP 6.2 3.4 1.5 5.0 16.1 16.2 
CTL 2.0 0.7 0.3 2.6 5.6 N/A 
GTL 2.9 1.2 0.3 1.9 6.4 N/A 
Refinery 
Hydrogen 
90% Capture 22.8 15.6 5.3 16.2 59.9 61.7 
99% Capture 21.3 14.4 5.1 16.5 57.3 58.9 
Cement 
90% Capture 22.8 11.1 6.1 22.6 62.7 64.3 
99% Capture 21.8 10.6 5.9 22.6 60.8 62.4 
Iron/Steel 
90% Capture 28.0 9.5 5.7 22.6 N/A 65.9 
99% Capture 27.8 9.3 5.6 22.6 N/A 65.4 
Note: All values expressed in December 2018 U.S. dollars per tonne CO2. 
The results show that CTL has the lowest greenfield COC, followed by GTL, NGP, ammonia, 
ethylene oxide (EO), ethanol, refinery hydrogen, and finally, cement, which has the highest 
greenfield COC. Retrofit applications exclude CTL and GTL, but follow the same cost pattern; 
however, the highest retrofit COC is the iron/steel case.  
For the low purity cases, the normalized COC ($/tonne CO2) decreases slightly with increasing 
capture rate (i.e., from 90 to 99 percent capture). The cost of the capture system and associated 
consumables increases at a lesser rate than that of the amount of CO2 captured (i.e., a 10 
percent increase from 90 to 99 percent capture). This is the effect of accuracy ranges of the 
capital cost estimates from the capture system vendor (-25/+40 percent) and the cost scaling 
methodology employed in this study. [2] [3] The margin of error associated with the cost 
estimate indicate that with increasing capture rate in the low purity cases, the COC is effectively 
the same. The reported minor increase in capital cost with increased capture rate (up to 99 
percent for sources with CO2 purity greater than 12 percent) based on vendor furnished cost 
and performance estimates has been validated by independent modeling performed by the 
carbon capture simulation initiative team at NETL and has been reported independently in 
literature. [4] Exhibit ES-3 shows the error in the calculated capture system BEC associated with 
the vendor’s quoted uncertainty rate alongside the amount of CO2 captured in the cement case

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
4 
from 90 to 99 percent capture rate. Similar graphs in for the refinery hydrogen and iron/steel 
cases can be found in Section 6.1.10 and Section 6.3.10, respectively. 
Exhibit ES-3. Capture system BEC and amount of CO 2 captured versus capture rate 
 
 
Exhibit ES-4 shows a plot of the COC versus the assumed CO2 stream partial pressure and the 
assumed CO2 concentrations for each of the base cases considered in this report. The general 
trend shows that as both the CO2 concentration and the CO2 partial pressure decrease, the COC 
of CO2 increases. The average COC for the six processes with CO2 concentration greater than 95 
percent is $17.5/tonne, while the average COC for the three processes with CO2 concentration 
less than 50 percent is $62.0/tonne. The partial pressure in the high purity cases is mainly 
reflective of the CO2 concentration.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
5 
Exhibit ES-4. COC versus CO2 partial pressure and CO2 concentration 
 
Note: Marker size is relatively indicative of CO2 captured (tonnes/year). 
The trends observed in this study may not be universally applicable because the assumptions 
made for each case in this study may not apply to all real-world examples of a specific industry. 
Additionally, concentration trends are emphasized due to the potential misleading nature of 
partial pressure values. In some instances, partial pressure can have directly recognizable effects 
on the COC; higher pressures will reduce the size of and duty of compression equipment, but 
this may not always be the case. For example, a stream with a total pressure of 1,000 psia, and a 
concentration of 10 percent CO2, would have a partial pressure of 100 psia. For the cases in this 
study, this partial pressure would be considered high, and might be expected to result in a low 
COC. However, for this example, capture and/or purification would be required, and therefore 
the resulting COC would not be expected to follow the partial pressure trend observed in Exhibit 
ES-4. 
There are also exceptions to these trends driven by economies of scale. Such a relationship is 
demonstrated in Exhibit ES-4 when comparing the results of NGP and ammonia. The CO2 stream 
partial pressures are equivalent, and the concentrations are also the same at 99 percent. 
However, the greenfield COCs were calculated to be $16.1/tonne CO2 for NGP and $19.0/tonne 
CO2 for ammonia, about an 18 percent difference. This is a result of the amount of CO2 available 
for capture in each case. Based on the assumptions made for each representative plant, NGP 
has 649,225 tonne/year CO2 available, while ammonia only has 486,227 tonne/year available. 
Therefore, while the CO2 stream partial pressures and concentrations are equivalent, there is 33 
percent more CO2 available for capture and sale at the NGP reference plant, resulting in a lower 
normalized CO2 capture cost. The factors noted above in Exhibit ES-4, namely CO2 partial 
pressure, concentration, and economies of scale (i.e., CO2 available at each representative

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
6 
plant), result in a significant range of CO2 capture costs. The highest greenfield COC, the cement 
case with 90 percent capture, is more than eleven times the price of the least expensive case 
(i.e., CTL). 
In addition, the assumptions regarding the quality of the CO2 emissions stream from the base 
plant in each case may greatly impact the COC. For instance, the base cement case assumes that 
the kiln off-gas is suitable to be sent directly for CO2 separation; however, cement industry 
members suggest that the kiln off-gas may have higher-than-acceptable levels of oxides of sulfur 
(SOx)/oxides of nitrogen (NOx) and would require the addition of selective catalytic reduction 
(SCR) and flue gas desulfurization (FGD). A sensitivity to this case was performed to evaluate the 
effect of adding these unit operations to the cement cases. The amount of SOx/NOx was not 
directly characterized; instead, the FGD and SCR costs were scaled from Case B12B of Revision 4 
of NETL’s “Cost and Performance Baseline for Fossil Energy Plants Volume 1: Bituminous Coal 
and Natural Gas to Electricity” based on the quantity of gas to be treated (i.e., the total flow of 
kiln off-gas). [5] Case B12B presents an SCR with a 78 percent NOx removal efficiency and an 
FGD that removes 2,000 ppm, by volume, of SOx from the coal boiler flue gas stream. The 
results of this sensitivity analysis show that the addition of a similar SCR and FGD to the cement 
plant’s CO2 capture system would increase greenfield COC by 23–25 percent with a COC of 
$74.8/tonne CO2 and $78.0/tonne CO2 for 99 and 90 percent capture, respectively. 
While the calculation of a COC demonstrates the capture costs across different industries based 
on a specific set of plant assumptions, another important consideration is the amount of CO2 
available from each industry. Neglecting CO2 transportation costs, if two industries demonstrate 
approximately equivalent normalized COCs, but one has a significantly larger supply, the 
industry with the larger supply would offer the more effective decarbonizationb application at 
the same or similar normalized cost. Exhibit ES-5 shows the CO2 emissions by industry in the 
United States, while Exhibit ES-6 presents a plot of COC versus the amount of domestic CO2 
emissions, both based on the Environmental Protection Agency  Facility Level Information on 
Greenhouse Gases Tool as of the 2020 reporting year.c [6] The COCs are those calculated in this 
study for greenfield sites except for iron/steel, which is for a retrofit application. This plot shows 
the cost of the source relative to the potentially capturable emissions in the United States. 
  
 
b Decarbonization within the context of this report is defined as the reduction of point-source emissions from industrial 
processes. Lifecycle analysis of decarbonization efforts as it relates to the CO2 capture operations evaluated in this 
report is not considered but could be considered in future work opportunities. 
c CO2 emissions related to EO production are not reported in Environmental Protection Agency’s Facility Level 
Information on Greenhouse Gases Tool; as such, the total emissions were estimated based on the total EO production as 
of 2019 [53] and an emissions factor of 1:3 CO2:EO on a molar basis, according to reaction stoichiometry as detailed in 
Section 5.2.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
7 
Exhibit ES-5. U.S. industrial CO2 emissions by industry 
Industry U.S. Total CO2 Emissions in 2020 (M tonnes CO2/year) [6] 
Ammonia 36 
Ethylene Oxide 0.95 
Ethanol 18 
Natural Gas Processing 56 
Coal-to-Liquids 0 
Gas-to-Liquids 0 
Refinery Hydrogen 30 
Cement 66 
Steel/Iron 62 
Exhibit ES-6. Representative plant COC results versus U.S. industrial CO2 emissions 
 
Note: Only the 99 percent capture cases are shown for low purity sources in Exhibit ES-6. 
Based on emissions rates, of the industrial plants with existing operations (i.e., excluding CTL 
and GTL), EO is the least impactful decarbonization option given the small amount of CO2 
available for capture (0.95 M tonnes/year), and cement manufacturing is the most impactful 
option with the largest amount of CO2 available (66 M tonnes/year). Based on normalized COC, 
NGP is the least expensive industrial source of CO2 within the existing U.S. fleet with a price of 
$16.1/tonne, and iron/steel is the most expensive option with a price of $64.8/tonne.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
8 
Sensitivities to CF, cost of purchased power, plant size in terms of CO2 emissions per year, and 
capital charge factor (CCF) were analyzed for each greenfield case. A sensitivity to natural gas 
price was also performed for the greenfield low purity cases. In these cases, natural gas is 
burned in an industrial boiler, described in Section 4.3, to generate steam for solvent 
regeneration in the CO2 capture process. Lastly, a sensitivity to the retrofit factor applied to 
generate retrofit application costs was evaluated for each case, excluding CTL and GTL, which do 
not have retrofit applications. The plant size sensitivity results for each case, evaluated across 
the typical plant size ranges specific to each industry, can be found in the corresponding 
sections, and all other sensitivity analyses can be found in Section 7.2. 
The general results of the sensitivities evaluated are as follows:  
• As CF varies from 65 to 95 percent, the COC for each case decreases, most notably in the 
Refinery H2 90 percent capture case where a $18.0/tonne CO2 decrease is observed 
across the sensitivity range. An 85 percent CF was assumed for the cases in this study. 
• As purchased power price increases, the COC also increases. This study assumes that all 
electricity requirements are provided by purchasing power from the grid. In cases 
requiring additional power beyond just compression, such as power for auxiliary loads in 
the CO2 separation processes, the COC increase is more dramatic. The largest increase 
across the sensitivity range was observed in the iron/steel and cement cases at 
$16.4/tonne. 
• The sensitivity to CCF is important as different industries may have access to different 
costs of capital. The CCF for each case was developed by NETL’s Energy Markets Analysis 
Team based on market financial data respective to each industrial sector. Details of the 
financial factors used in this study are given in Section 3.2. As CCF varies from 5 percent 
to 35 percent, the capture costs can increase by up to $150.2/tonne as observed in the 
refinery hydrogen case with 90 percent capture. 
• The final sensitivity to natural gas price showed that as the natural gas price varied over 
the range $3–10/MMBtu, the COC may rise as much as $30.6/tonne CO2 as was 
observed in the iron/steel 90 percent capture case.d 
This study uses the COC and CO2 supply to compare nine potential industrial CO2 sources. The 
results are representative of the assumptions regarding the reference plant and its CO2 
emissions stream(s). Scale and location will impact results for actual plants. Methods of CO2 
transport and storage (T&S) and the associated costs are considerations that could ultimately 
change the economic impact of implementing carbon capture at a specific plant. T&S costs were 
not considered in this study; however, Section 2 examines the location of individual plants in 
each industry relative to CO2 pipelines and current EOR sites to qualitatively identify relative 
advantages or disadvantages for decarbonization in each industry, as it relates to T&S. To 
estimate T&S costs, users may refer to NETL’s “Quality Guidelines for Energy System Studies 
(QGESS): Carbon Dioxide Transport and Storage Costs in NETL Studies” for guidance. [7] 
 
d This report does not consider capture of the CO2 produced by the NG-fired boiler. If this CO2 was captured, it would 
impact the results presented herein greatly, due to the lower concentration of CO2 in the flue gas stream compared to 
that of the low purity industrial sources considered. It would also increase the amount of CO2 available for capture, as 
NG consumption increases. Such an analysis is discussed in the future work considerations detailed in Section 9.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
9 
1 INTRODUCTION  
With a global initiative to reduce greenhouse gas (GHG) emissions, several common industrial 
processes have been identified as potential opportunities for carbon dioxide (CO2) capture. Of 
the 9 processes considered in this report, 7 have existing operations in the United States, 
contributing just under 270 M tonnes per year of CO2 emissions in 2020 based on reporting to 
the Environmental Protection Agency. [6] Industrial plant CO2 emissions sources offer 
advantages when considering decarbonization due to their relatively high concentrations of CO2 
in emissions streams, which may lead to lower normalized capture costs. With high CO2 
concentrations, separation equipment costs are minimized, or even eliminated in cases where 
CO2 streams are 99–100 percent pure. This study evaluates nine representative plants with CO2 
emissions sources having relatively high concentrations to determine the cost of CO2 capture. 
The cost of CO2 capture (COC) in each case, as defined by Equation 1-1, considers the 
equipment required for CO2 removal, if applicable, and compression, as well as the balance of 
plant equipment as detailed in Section 4.3 through Section 4.6, and operation and maintenance 
(O&M), purchased power, and fuel costs, as applicable. Throughout the report, “CO2 capture” 
refers to the incremental equipment required to prepare the CO2 emissions stream for pipeline 
transport (i.e., compression and intercooling, auxiliary equipment, CO2 removal systems, etc.).  
 
Equation 1-1 
 
Where: 
TOC – Total overnight costs of equipment added for the application of CO2 capture 
CCF – Capital charge factor, based on industry-specific financial assumptions as detailed in 
Section 3.2 
FOM – Annual fixed O&M costs 
VOM – Annual variable O&M costs 
PF – Purchased fuel 
PP – Purchased power 
Estimates of financing scenarios specific to each industry were applied to the capital 
costs to account for return on equity and financing costs. Financial methodology and 
the resulting financial factors for each case are presented in Section 3. 
1.1 ASSUMPTIONS 
There are many industrial processes that produce CO2 emissions, and as such, criteria were 
established to justify the inclusion of an industrial process in this report. First, an industrial plant 
must be representative of either a relatively large amount of CO2 emissions (i.e., an emissions 
source that could benefit from economies of scale) or of a 99–100 percent pure CO2 stream. The 
𝐶𝑂𝐶 ( $𝑡𝑜𝑛𝑛𝑒 𝐶𝑂2) = 𝑇𝑂𝐶 ∗ 𝐶𝐶𝐹 + 𝐹𝑂𝑀 + 𝑉𝑂𝑀 + 𝑃𝐹 + 𝑃𝑃𝑡𝑜𝑛𝑛𝑒𝑠 𝐶𝑂2 𝑐𝑎𝑝𝑡𝑢𝑟𝑒𝑑 𝑝𝑒𝑟 𝑦𝑒𝑎𝑟

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
10 
second criterion for inclusion is that an industrial plant is likely to provide a relatively low 
normalized COC. This condition is highly dependent upon the first criteria, as normalized COC 
values are a function of CO2 availability. Power production plants are not considered in this 
study, as they are evaluated in NETL’s collection of baseline studies, such as “Cost and 
Performance Baseline for Fossil Energy Plants Volume 1: Bituminous Coal and Natural Gas to 
Electricity.” [5] Process models were developed for each case based on guidance in NETL’s 
“Quality Guidelines for Energy Systems Studies (QGESS): Process Modeling Design Parameters,” 
and applicable model assumptions are shown in Exhibit 1-1. [8]  
Exhibit 1-1. Process design assumptions 
Site Characteristics  
Location Greenfield, Midwestern U.S. 
Topography Level 
Size, acres 10 
Particulate Matter Disposal  Off-Site 
Water Supply 50% Municipal and 50% Ground Water 
Site Ambient Conditions 
Elevation, meter (feet) 0 (0) 
Barometric Pressure, MPa (psia) 0.101 (14.696) 
Average Ambient Dry Bulb Temperature, °C (°F) 15 (59) 
Average Ambient Wet Bulb Temperature, °C (°F) 10.8 (51.5) 
Design Ambient Relative Humidity, % 60 
Cooling Water Temperature, °C (°F) 15.6 (60) 
Natural Gas Characteristics 
Component Volume % 
Methane CH4 93.1 
Ethane C2H6 3.2 
Propane C3H8 0.7 
n-Butane  C4H10 0.4 
Carbon Dioxide CO2 1.0 
Nitrogen N2 1.6 
MethanethiolA CH4S 5.75x10-6 
  LHV HHV 
kJ/kg (Btu/lb) 47,201 (20,293) 52,295 (22,483) 
Megajoule/standard 
cubic meter (Btu/scf) 34.52 (927) 38.25 (1,027) 
Air composition based on published psychrometric data, mass % 
Nitrogen N2 75.055 
Oxygen O2 22.998 
Argon Ar 1.280 
Water H2O 0.616 
Carbon Dioxide CO2 0.050 
A The sulfur content of natural gas is primarily composed of added Mercaptan (methanethiol [CH4S]) with trace 
levels of hydrogen sulfide (H2S)

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
11 
2 PLANT SITES AND CO2 END-USE 
The assumption made for this study is that the final CO2 product is transported via pipeline to 
be utilized in enhanced oil recovery (EOR) applications, and as such applies the specifications for 
CO2 product purity, pressure, and temperature after capture and compression per National 
Energy Technology Laboratory’s (NETL) “QGESS: CO2 Impurity Design Parameters” specifications. 
[1] The viability of adding capture to a representative plant would ultimately be dependent 
upon the costs for transport and storage (T&S) of the CO2 captured in addition to the COCs 
evaluated in this report. T&S costs are not considered in the metric of value, COC of CO2, in this 
study but should be considered by an owner evaluating capture implementation at an industrial 
facility. Other uses for the CO2 may be available to owners, but those alternate possibilities were 
not considered for the purpose of this report. In addition, analysis of the base plants for each of 
the nine processes considered falls outside the scope of this study (i.e., cost of cement 
production before and after CO2 capture). 
Leaving the system boundary of this study is a CO2 stream that has been purified, where 
necessary, and compressed to pipeline specifications of 2,200 psig per QGESS specification. [1] 
While detailed pipeline specifications such as pressure drop, length, and other characteristics, 
are not considered in this report, and as noted in Exhibit 1-1, the study assumes a generic 
midwestern plant for the purposes of consistency in process modeling, it is useful to highlight 
potential industrial CO2 capture locations and their relative locations to sites/transport 
mechanisms that could be utilized. Exhibit 2-1 shows existing CO2 pipelines and EOR injection 
sites, while the seven maps that follow, Exhibit 2-2 through Exhibit 2-7, illustrate the proximity 
of plants for each industrial source type to the existing CO2 pipeline and EOR infrastructure. 
There are currently no U.S. coal-to-liquids (CTL) or gas-to-liquids (GTL) plants in operation, so no 
map is given for these cases.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
12 
Exhibit 2-1. Existing CO2 pipelines and active EOR injection sites 
 
 
A large percentage of ammonia plants are in close proximity to existing CO2 pipelines and EOR 
injection sites, as shown in Exhibit 2-2. The bars on the chart represent gross (light blue) and net 
(dark blue) ammonia production at each plant. As noted in Section 5.1.2, the representative 
ammonia production in the United States was considered at gross capacity, but in some 
ammonia plants, portions of gross ammonia and CO2 produced are further utilized to make 
ammonia derivatives, such as ammonium nitrate or urea. Alternate use of CO2 in ammonia 
plants is outside the scope of this study, but net capacities are shown alongside gross capacities 
in Exhibit 2-2 for reference or future use.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
13 
Exhibit 2-2. Ammonia plant locations and existing CO 2 pipelines and EOR injection sites 
 
 
Exhibit 2-3 shows the location of EO plants and their relation to existing CO2 pipelines and EOR 
injection sites. U.S. EO production is concentrated in Texas and Louisiana. Of the 15 U.S. EO 
plants, 6 are located very close to existing EOR pipelines and injection sites. Therefore, from a 
location standpoint, EO presents a potentially advantageous option for capture integration. 
However, due to the small scale of the existing EO plants (i.e., the small amount of CO2 available 
for capture), diseconomies of scale may deter implementation.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
14 
Exhibit 2-3. EO plant locations and existing CO2 pipelines and EOR injection sites 
 
 
As shown in Exhibit 2-4, a large percentage of ethanol plant locations are not near existing CO2 
pipelines or EOR injection site locations; however, most of the ethanol processing facilities are 
grouped in the Midwest and could potentially realize economies of scale collectively to justify 
the addition of a new CO2 pipeline for connection to existing infrastructure. This scenario falls 
outside the scope of this study but could be considered in future work.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
15 
Exhibit 2-4. Ethanol plant locations and existing CO2 pipelines and EOR injection sites 
 
 
Exhibit 2-5 shows the location of natural gas processing (NGP) facilities and their relations to 
existing CO2 pipelines and EOR injection sites. Plant capacities are shown on this map; however, 
given the 471 NGP facilities, each treating a different amount of natural gas (NG) with widely 
varying CO2 concentrations, there may not be a direct correlation between capacity and CO2 
available. This means that a large facility processing NG with low CO2 concentration may have 
less CO2 available than a smaller facility processing NG with a much higher CO2 concentration.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
16 
Exhibit 2-5. NGP plant locations and existing CO 2 pipelines and EOR injection sites 
 
 
Exhibit 2-6 shows the location of U.S. refineries that produce hydrogen, and their proximity to 
existing CO2 pipelines and EOR injection sites. There are many refineries near existing EOR 
pipelines and injection sites. However, the map is only intended to show the relative crude 
throughput capacity of the refineries, and not the amount of CO2 available. There is not 
necessarily a direct relationship between refinery capacity and CO2 available for capture.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
17 
Exhibit 2-6. Refinery hydrogen (U.S. refineries) plant locations and existing CO 2 pipelines and EOR injection sites 
 
 
Exhibit 2-7 shows the location of cement plants and their relation to existing CO2 pipelines and 
EOR injection sites. Some cement plants are located relatively close to existing infrastructure 
and given the typically larger scale of cement production capacity, and consequently larger 
amount of CO2 emissions available, construction of a connecting pipeline for other cement 
facilities may be a viable means of decarbonization in the cement industry. This is scenario is 
not evaluated within the context of this study.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
18 
Exhibit 2-7. Cement plant locations and existing CO2 pipelines and EOR injection sites 
 
 
Exhibit 2-8 shows currently operating steel basic oxygen furnace (BOF) plants and their relation 
to existing CO2 pipelines and EOR injection sites. Steel does not appear to provide ease of 
implementation for EOR end-use because many facilities would not be able to utilize any of the 
existing EOR infrastructure. However, based on this study’s assumptions, steel plants represent 
the largest amount of CO2 available among the industries considered that are currently 
operating plants in the United States; therefore, construction of connecting pipelines may be a 
viable means of decarbonization in the steel industry. This scenario is not evaluated in the 
context of this study.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
19 
Exhibit 2-8. Steel (BOF) plant locations and existing CO2 pipelines and EOR injection sites

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
20 
3 ECONOMIC ANALYSIS OVERVIEW 
The industrial sources considered in this study are grouped into “High Purity” and “Low Purity” 
groups, based on the concentration of CO2 in the stream to be captured. The prior iteration of 
this report applied global financial assumptions based on the simple delineation between high 
and low purity sources. This approach relied on the fact that high purity sources would only 
require compression, whereas low purity sources would require CO2 removal and compression, 
and each would have distinct construction, and thus capital expenditure, periods. For this 
revision update, capital expenditure assumptions have been maintained, but additional detail 
regarding each specific industry’s financial assumptions have been added based on market data 
analysis performed by NETL’s Energy Markets Analysis Team in October 2021. 
3.1 COST ESTIMATING METHODOLOGY 
Detailed information pertaining to topics such as contracting strategy; engineering, 
procurement, and construction (EPC) contractor services; estimation of capital cost 
contingencies; owner’s costs; cost estimate scope; economic assumptions; and finance 
structures are available in the 2019 revision of the QGESS document “Cost Estimation 
Methodology for NETL Assessment of Power Plant Performance.” [9] Select portions are 
repeated in this report for completeness. 
Costs of Mature Technologies and Designs: 
The cost estimates for cases that only contain fully mature technologies, which have been 
widely deployed at commercial scale (e.g., high purity cases, which only require compression) 
reflect nth-of-a-kind on the technology commercialization maturity spectrum. The costs of such 
technologies have dropped over time due to “learning by doing” and risk reduction benefits 
that result from serial deployments as well as from continuing research and development 
(R&D). All process equipment in the estimates found herein is commercially available, so no 
process contingencies were added to those cases, except for those which require purification 
(i.e., low purity cases) via acid gas removal as detailed in Section 4.2. 
Costs of Emerging Technologies and Designs: 
The cost estimates for cases that include technologies that are not yet fully mature (e.g., 
capture systems for low purity cases) use the same cost estimating methodology as for mature 
technologies, which does not fully account for the unique cost premiums associated with the 
initial, complex integrations of emerging technologies in a commercial application. Thus, it is 
expected that addition of capture equipment in low purity cases may incur costs higher than 
those estimated for a mature technology. As such, process contingency of 17 percent is applied 
to the CO2 removal system for low purity cases based on engineering judgment and for 
consistency of process contingencies applied for similar technologies in other NETL studies. [5] 
Other Factors: 
Actual reported project costs for all the plant types are also expected to deviate from the cost 
estimates in this report due to project- and site-specific considerations (e.g., contracting 
strategy, local labor costs, seismic conditions, water quality, financing parameters, local

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
21 
environmental concerns, weather delays) that may make construction more costly. Such 
variations are not captured by the reported cost uncertainty. 
3.1.1 Capital Costs 
As illustrated in Exhibit 3-1, this report defines capital cost at five levels: BEC, EPCC, TPC, TOC, 
and TASC. BEC, EPCC, TPC, and TOC are “overnight” costs and are expressed in “base-year” 
dollars. The base year is the first year of capital expenditure. TASC is expressed in mixed, 
current-year dollars over the entire capital expenditure period, which is assumed to last one 
year in high purity cases and three years in low purity cases. The cost estimates presented in 
this study are considered Class 4 estimates, as defined by AACE International (AACE) 16R-90. 
[10] 
The Bare Erected Cost (BEC) comprises the cost of process equipment, on-site facilities and 
infrastructure that support the plant (e.g., shops, offices, labs, road), and the direct and indirect 
labor required for its construction and/or installation. The cost of EPC services and 
contingencies are not included in BEC.   
The Engineering, Procurement and Construction Cost (EPCC) comprises the BEC plus the cost of 
services provided by the EPC contractor. EPC services include detailed design, contractor 
permitting (i.e., those permits that individual contractors must obtain to perform their scopes of 
work, as opposed to project permitting, which is not included here), and project/construction 
management costs.   
The Total Plant Cost (TPC) comprises the EPCC plus project and process contingencies.   
The AACE 16R-90 states that project contingency for a “budget-type” estimate (AACE Class 4 or 
5) should be 15–30 percent of the sum of BEC, EPC fees, and process contingency. [10] 
Therefore, a 20 percent project contingency was added to each cost account across all cases. 
The Total Overnight Cost (TOC) comprises the TPC plus all other overnight costs, including 
owner’s costs. TOC does not include escalation during construction or interest during 
construction.   
The Total As-Spent Cost (TASC) is the sum of all capital expenditures as they are incurred during 
the capital expenditure period including their escalation. TASC also includes interest during 
construction, comprising interest on debt and a return on equity.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
22 
Exhibit 3-1. Capital cost levels and their elements 
 
3.1.1.1 Cost Estimate Basis and Classification 
The TPC and O&M costs for each of the cases in the report were estimated based on adjusted 
vendor-furnished data and scaled estimates from previous NETL studies. Reference costs are 
scaled based on direction from NETL’s QGESS “Capital Cost Scaling Methodology: Revision 4 
Report.” [3] An underlying assumption of this cost scaling methodology is that capital 
equipment is available and scalable at any size/capacity. In real applications, equipment may 
only be manufactured in discrete sizes, which would potentially differ from the costs presented 
herein. This is particularly applicable for the “Plant Capacity Sensitivity Analysis” found in the 
analysis subsections for each of the industrial plant types. Those sensitivity analyses are 
generated assuming continuous equipment capacities and costs and using generic scaling of 
cost components, rather than by following the QGESS capital cost scaling methodology for every 
capacity across the plant size range. For the purposes of this analysis, it is assumed that margins 
of error associated with discrete versus continuous costs and equipment capacities would be 
within the scope of an AACE Class 4 estimate. 
3.1.1.2 System Code-of-Accounts 
The costs are grouped according to a process/system-oriented code of accounts. This type of 
code-of-account structure has the advantage of grouping all reasonably allocable components 
of a system or process, so they are included in the specific system account.e 
 
e This would not be the case had a facility, area, or commodity account structure been chosen instead. 
process equipment
supporting facilities
direct and indirect 
labor
BEC EPCC
TPC
TOC
TASC
EPC contractor services
process contingency
project contingency
pre-production costs
inventory capital
financing costs
other owner’s costs
escalation during capital expenditure period
interest on debt during capital expenditure period
Bare Erected Cost
Engineering, Procurement 
and Construction Cost
Total Plant Cost
Total Overnight Cost
Total As-Spent Cost
BEC, EPCC, TPC and TOC are 
all “overnight” costs 
expressed in base-year dollars.
TASC is expressed in mixed-
year current dollars, spread 
over the capital expenditure 
period.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
23 
3.1.1.3 Price Fluctuations 
During the writing of this report, the prices of equipment and bulk materials used as reference 
costs fluctuated because of various market forces. All vendor quotes used to develop these 
estimates were adjusted to December 2018 dollars accounting for the price fluctuations. The 
Chemical Engineering Plant Cost Index [11] was used as needed for these adjustments. While 
such overall indices are nearly constant, it should be noted that the cost of individual 
equipment types may still deviate from the December 2018 reference point. 
In addition to year dollar effects on the costs presented in this study, the location of the actual 
installation can influence pricing due to transport and shipping constraints, workforce 
availability, etc. It is assumed that these contingencies are covered within the range of accuracy 
of the report (AACE Class 4). 
3.1.1.4 Owner’s Costs 
Owner’s costs were estimated based on the 2019 revision of the QGESS document “Cost 
Estimation Methodology for NETL Assessment of Power Plant Performance.” [9]  Owner’s costs 
are split into three categories: pre-production costs, inventory capital, and other costs.  
Pre-production allocations are expected to carry the specific plants through substantial 
completion, and to commercial operation. Substantial completion is intended to represent the 
transfer point of the facility from the EPC contractor (development entity) to the end user or 
owner, and is typically contingent on mutually acceptable equipment closeout, successful 
completion of facility-wide performance testing, and full closeout of commercial items. Exhibit 
3-2 presents descriptions of the owner’s costs estimated for the cases in this report. 
Exhibit 3-2. Estimated amounts for owner’s costs 
Owner’s Cost Estimated Amount 
Prepaid Royalties Any technology royalties are assumed to be included in the associated equipment cost, and thus are not included as an owner’s cost 
Production 
(Start-up) Costs 
• 6 months operating labor 
• 1 month maintenance materials at full capacity 
• 1 month non-fuel consumables at full capacity 
• 1 month waste disposal 
• 25% of one month’s fuel cost at full capacity 
• 2% of TPC 
Compared to AACE 16R-90, this includes additional costs for operating labor (6 
months versus 1 month) to cover the cost of training the plant operators, including 
their participation in startup, and involving them occasionally during the design and 
construction. AACE 16R-90 [10] and Electric Power Research Institute (EPRI) Technical 
Assessment Guide (TAG®) [12] differ on the amount of fuel cost to include; this 
estimate follows EPRI 
Inventory Capital • 0.5% of TPC for spare parts • 60-day supply (at full capacity) of fuel. Not applicable for NG

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
24 
Owner’s Cost Estimated Amount 
• 60-day supply (at full capacity) of non-fuel consumables (e.g., chemicals and 
catalysts) that are stored on site. Does not include catalysts and adsorbents that 
are batch replacements such as water gas shift, carbonyl sulfide, and selective 
catalytic reduction catalysts and activated carbon 
AACE 16R-90 [10] does not include an inventory cost for fuel, but EPRI TAG® [12] does 
Land • $3,000/acre, 10 acres • Note: This land cost is based on a site in a rural location 
Financing Costs 
• 2.7% of TPC 
This financing cost (not included by AACE 16R-90 [10]) covers the cost of securing 
financing, including fees and closing costs but not including interest during 
construction. The “rule of thumb” estimate (2.7% of TPC) is based on a 2019 
professional communication with Black & Veatch 
Other Owner’s 
Costs 
• 15% of TPC 
This additional lumped cost is not included by AACE 16R-90 [10] or EPRI TAG® [12]. 
The “rule of thumb” estimate (15% of TPC) is based on a 2019 professional 
communication with Black & Veatch 
3.1.2 Operation and Maintenance Costs 
The production costs or operating costs and related maintenance expenses pertain to those 
charges associated with operating and maintaining equipment over its expected life. The O&M 
costs calculated in this study are incremental costs related to the capture, compression, and 
ancillary equipment evaluated and thus are not indicative of the O&M costs of the base plant. 
These O&M costs include the following:  
• Operating labor 
• Maintenance – material and labor 
• Administrative and support labor 
• Consumables 
• Fuel 
• Waste disposal 
• Co-product or by-product credit (that is, a negative cost for any by-products sold) 
There are two components of O&M costs: fixed O&M, which is independent of production, and 
variable O&M, which is proportional to production. Taxes and insurance are included as fixed 
O&M costs, totaling two percent of the TPC. 
3.1.2.1 Operating Labor 
Operating labor cost was determined based on the number of operators required for the 
addition of capture and compression where applicable for each case. For high purity cases, 
which require only the addition of compression and associated utilities, one additional operator 
was considered. Low purity cases require acid gas removal (AGR) units and an industrial boiler 
alongside compression and the utilities associated with each additional process unit. As such,

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
25 
2.3 additional operators were considered for low purity cases, which is the difference in 
operating labor required for a supercritical pulverized coal power plant with and without 
capture, per NETL’s “Cost and Performance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity” results. [5] The average base labor rate used to 
determine annual cost is $38.50/hour. The associated labor burden is estimated at 30 percent of 
the base labor rate. 
3.1.2.2 Maintenance Material and Labor 
Maintenance cost was evaluated based on relationships of maintenance cost to initial capital 
cost. This represents a weighted analysis in which the individual cost relationships were 
considered for each major plant component or section. 
3.1.2.3 Administrative Support and Labor 
Labor administration and overhead charges are assessed at a rate of 25 percent of the burdened 
O&M labor. 
3.1.2.4 Consumables 
The cost of consumables, including fuel, was determined based on individual rates of 
consumption, the unit cost of each specific consumable commodity, and the plant annual 
operating hours.   
Quantities for major consumables such as NG for fuel and purchased power were taken from 
technology-specific energy and mass balance diagrams developed for each plant application. 
Fuel cost is $4.42/MMBtu, and power is purchased at a cost of $60/MWh. Sensitivity analyses 
relating COC to purchased power price and NG price are detailed in Section 7.2.3 and Section 
respectively. Other consumables were evaluated based on the quantity required using reference 
data. 
The quantities for initial fills and daily consumables were calculated on a 100 percent operating 
capacity basis. The annual cost for the daily consumables was then adjusted to incorporate the 
annual plant operating basis, or capacity factor (CF). An 85 percent CF was assumed for all 
cases. Initial fills of the consumables, fuels, and chemicals may be accounted for directly in the 
O&M tables or included with the equipment pricing in the capital cost. 
3.1.2.5 Waste Disposal 
Waste quantities and disposal costs were determined/evaluated similarly to the consumables. 
Waste streams are individually reported, and disposal costs are reported for each waste stream, 
where applicable. 
3.2 CAPITAL CHARGE FACTORS 
The financial assumptions for each case were developed by NETL’s Energy Markets Analysis 
Team in October 2021 based on market data respective to each industrial sector. These factors 
are summarized in Exhibit 3-3 and Exhibit 3-4. All values are expressed in real dollar terms.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
26 
Exhibit 3-3. Financial assumptions for high purity sources 
Financial Parameter Ammonia EO Ethanol NGP CTL/GTL 
Fixed Charge Rate 5.33% 4.63% 6.64% 5.82% 7.32% 
TASC/TOC Ratio 1.035 1.025 1.047 1.039 1.054 
Capital Charge Factor 5.51% 4.74% 6.96% 6.05% 7.71% 
Debt/Equity Ratio 54/46 48/52 36/64 43/57 32/68 
Payback Period 30 years 
Interest on Debt 5.15% 
Levered Return on Equity 
(Asset Weighted) 1.50% 0.04% 4.51% 2.96% 5.54% 
Capital Expenditure Period 1 year 
Capital Distribution 1st year – 100% 
Exhibit 3-4. Financial assumptions for low purity sources 
Financial Parameter Refinery Hydrogen Cement Iron/Steel 
Fixed Charge Rate 4.39% 5.08% 6.90% 
TASC/TOC Ratio 1.036 1.054 1.091 
Capital Charge Factor 4.55% 5.35% 7.53% 
Debt/Equity Ratio 33/67 42/58 39/61 
Payback Period 30 years 
Interest on Debt 5.15% 
Levered Return on Equity (Asset Weighted) 0.41% 1.42% 5.02% 
Capital Expenditure Period 3 years 
Capital Distribution 1st year – 10%; 2nd year – 60%; 3rd year – 30 % 
 
The result of the economic analysis is a calculated COC of CO2, which represents the cost to the 
owner, per tonne of CO2 captured. This cost includes the capital expenditures, escalated at the 
assumed nominal general inflation rate of two percent per year, providing the stipulated rate of 
return on equity over the entire economic analysis period. Assuming all annual costs also 
escalate at the same inflation rate, the COC is essentially the sum of the O&M costs and the 
annualized capital cost charges, all normalized to the annual plant CO2 flow rate. 
For a CO2 source with a higher flow rate (same CO2 purity and pressure), a corresponding 
increase in the flow rate of the captured CO2, requirement for consumables, size of capture 
equipment, etc., occurs; however, the COC is expected to be roughly equivalent or, in some 
cases, lower due to the economies of scale associated with the cost of the larger 
equipment. This is especially apparent when comparing the costs of each low purity case at two

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
27 
different capture rates (e.g., cement at 90 percent and 99 percent capture). Ultimately, the CCF, 
which is the product of the fixed charge rate and the TASC/TOC ratio, applied in each case can 
have a dramatic effect on the COC calculated. A sensitivity analysis evaluating this relationship is 
presented in Section 7.2.1. 
3.3 RETROFIT FACTORS 
Retrofit factors for power plants retrofitting amine solvent-based CO2 capture technologies 
were developed in the NETL study “Retrofit Cost Analysis for Post-combustion CO2 Capture” 
(Retrofit Study). [13] The retrofit factors, as presented in the Retrofit Study, are technology- and 
size-specific, and significant factors would be ignored when applying them to other 
configurations, such as the ones in this study. Examples of assumptions that would affect the 
implementation of the retrofit factors from the Retrofit Study include: 
The high purity sources do not require a CO2 separation system 
CO2 separation is performed using Shell Cansolv post-combustion amine-based capture process 
in the steel and cement cases, a process that differs from that of the monoethanethiol (MEA) 
systems that were used to develop the retrofit factors in the Retrofit Study [13] 
Shell’s ADIP-Ultra amine-based pre-combustion capture process is the basis for purification of 
the CO2 stream in the refinery hydrogen case, which differs greatly from the post-combustion 
MEA systems within the Retrofit Study [13] 
These industrial sources are significantly smaller than the utility scale power plants for which 
the retrofit factors in the Retrofit Study were developed [13] 
The areas where these retrofit factors would be more directly applicable are the ‘Ductwork & 
Stack’ accounts, which can have a retrofit factor as high as 1.6. The BEC of the ‘Ductwork & 
Stack’ account in the cement case with 99 percent capture, for example, is $15,274,000. 
Application of a 1.6 retrofit factor would add an additional $9,164,400 for the ‘Ductwork & 
Stack’ line item. With the cement plant case having a greenfield TOC of $424,897,000 
application of this 1.6 retrofit factor would represent a 2.2 percent increase in the TOC for 
‘Ductwork & Stack’ alone. 
Engineering judgment was used to determine a more generic factor to be applied to the cases in 
this report, in lieu of those presented in the Retrofit Study. As an alternative, for high purity 
cases a retrofit factor of 1.01 was applied to the TPC as a blanket retrofit cost increase, and a 
retrofit factor of 1.05 was applied to the TPC of low purity cases. Without a formalized 
procedure for applying the retrofit factors, it is best to consider the retrofit factor as a single 
capital cost sensitivity, from which the true cost of a retrofit (which has overriding project and 
site-specific considerations) can be refined as more information is available for a specific design 
case. A sensitivity analysis examining the effect on COC related to the retrofit factor applied is 
discussed in Section 7.2.2.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
28 
4 EQUIPMENT 
4.1 COMPRESSION 
Two different types of compressors are used for the cases in this study, an integrally geared 
centrifugal compressor and a reciprocating compressor. The type of compressor selected for 
each case is chosen based on the mass flow of CO2 to the first compression stage as well as the 
suction conditions at stage one. 
4.1.1 Reciprocating Compressor 
A quote for a five-stage reciprocating compressor was used to represent compression for cases 
listed in Exhibit 4-1. The referenced compression quoted a suction pressure of 17.4 psia, suction 
temperature of 80°F, and an inlet flow to stage one of 35,991 lb/hr. The discharge pressure was 
quoted as 2,200 psia with a total power requirement of 1.72 MW. The reciprocating compressor 
was modeled with alterations as applicable, resulting in the specifications shown in Exhibit 4-1. 
Exhibit 4-1. Reciprocating compressor cases specifications 
Case 
Number of 
Compression 
Stages 
Inlet Flow to 
Compression 
Stage 1 (lb/hr) 
Suction 
Pressure 
(psia) 
Suction 
Temperature 
(°F) 
Discharge 
Pressure 
(psia) 
Ammonia 5 122,946 23.5 69 2,214.7 
EO 4 30,578 43.5 96 2,214.7 
Ethanol 5 36,000 16.4 80 2,214.7 
4.1.2 Centrifugal Compressor 
Quotes for integrally geared centrifugal compressors were used to represent compression in the 
cases listed in Exhibit 4-2. Two separate quotes were used, the first of which was provided for 
the development of NETL’s “Cost and Performance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity," Revision 4 (BBR4). [5] The second quote for a 
centrifugal compressor was obtained as part of the development of this study, specifically for 
application in the refinery hydrogen case. 
Given that the CTL and GTL cases are taken from previous NETL reports, they implement the 
same compression train performance and cost used in their respective reports, converted to 
current year dollar. Those reports employ integrally geared centrifugal compressors specifically 
designed for their respective CO2 flowrates and conditions. This type of compressor is 
particularly advantageous for CTL and refinery hydrogen cases, where CO2 is available at 
multiple pressures, and requires a special compression train that can accommodate multiple 
suction pressures. Exhibit 4-2 shows the cases using integrally geared centrifugal compression 
and their case specifications.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
29 
Exhibit 4-2. Integrally geared centrifugal compressor cases specifications 
Case 
Number of 
Compression 
Stages 
Inlet Flow to 
Compression Stage 1 
(lb/hr) 
Suction 
Pressure  
(psia) 
Suction 
Temperature 
(°F) 
Discharge 
Pressure  
(psia) 
NGP 8 164,059 23.5 69 2,214.7 
Steel/Iron COG/BFS 
90% Capture 8 424,424 28.9 87.8 2,214.7 
Steel/Iron COG/BFS 
99% Capture 8 466,701 28.9 87.8 2,214.7 
Steel/Iron COG PPS 
90% Capture 8 426,791 28.9 87.8 2,214.7 
Steel/Iron COG PPS 
99% Capture 8 469,304 28.9 87.8 2,214.7 
Cement 
90% Capture 8 275,388 28.9 87.8 2,214.7 
Cement 
99% Capture 8 302,818 28.9 87.8 2,214.7 
Refinery Hydrogen 
90% Capture 7 93,136B, C  28.3/90.8D 104.0/215.6 2,214.7 
Refinery Hydrogen 
99% Capture 7 104,553B, C 28.3/90.8D 104.0/215.6 2,214.7 
CTL N/AA 2,200,423B 160/265/300E N/A 2,214.7 
GTL N/AA 467,794 265 100 2,214.7 
A Both CTL and GTL are assumed to use eight total compression stages, but this is not explicitly stated in the respective reports.  
B Flow reported is total. The individual flows at each of the multiple suction pressures sum to the total flow.  
C These flowrates fall below the lower operating limit detailed in Section 4.1.1, but a specific performance and cost quote was 
obtained for application in the refinery hydrogen cases. The quote data is proprietary; thus, details are not included within this 
report.  
D A second inlet to compression was considered as part of the compressor design (proprietary) for refinery hydrogen cases due 
to AGR specifications and process flow.  
E The CTL process produces three high purity CO2 streams at three pressures. Details related to the compressor for the CTL case 
are provided in Section 5.5. 
As mentioned, all compressors discharge at a pressure of 2,214.7 psia (2,200 psig). This is the 
pipeline pressure specification assumed in this study, which is given in the QGESS for CO2 for use 
in EOR applications. [1] However, it should be noted that EOR field pressure requirements can 
vary from location to location, and pressures as low as 1,200 psig could be acceptable. [14] 
4.2 CO2 CAPTURE AND PURIFICATIONf 
For cases requiring CO2 separation and purification prior to compression, an AGR unit was used. 
The AGR unit also provides polishing of residual sulfur components in the CO2 capture stream. 
 
f Much of the text and descriptions within this section were sourced, with permission, from data provided by Shell to NETL, unless otherwise 
noted. The information relates to a CO2 removal system designed by Shell.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
30 
The performance and cost information for the AGR units employed in this study are based on 
data provided by Shell in 2021. The quote provided specific cost and performance metrics at 
individual capture rates (i.e., 90, 95, and 99 percent) for each representative industrial plant. 
The unit cost is scaled based on CO2 product mass flow (60 percent) and inlet flow to the 
adsorber (40 percent), per specifications in “QGESS Capital Cost Scaling Methodology: Revision 
4 Report.” [3] Cases where an AGR is used include refinery hydrogen, iron/steel, and cement. 
The CO2 removal efficiency of the AGR unit is represented at two rates, 90 percent and 99 
percent, for each case. For the purposes of this study, performance and cost data for the AGR 
units was obtained from Shell for the specific flue gas streams representative of the low purity 
industrial sources, not scaled or applied from quotes provided for power-related capture 
systems. 
4.2.1 Cansolv Post-Combustion Capture 
The AGR system utilized in the iron/steel and cement cases is the Cansolv CO2 Capture 
technology commercially offered by Shell. This amine-based, post-combustion process is 
designed to recover high purity CO2 from dilute streams that contain O2, such as flue gas from 
coal-fired power plants, combustion turbine exhaust gas, and other industrial waste gas 
streams, such as those evaluated in this report. A typical flowsheet for the process is shown in 
Exhibit 4-3. 
Exhibit 4-3. Shell’s Cansolv CO2 capture typical process flow diagram 
 
4.2.1.1 Pre-scrubber 
The CO2-laden gas from the industrial source (cement or iron/steel plant) is sent through a 
booster fan to drive the gas through downstream equipment starting with the pre-scrubber 
inlet cooling section. The cooler is operated as a direct contact cooler that saturates and sub-
cools the feed gas stream. Saturation and sub-cooling are beneficial to the system as they 
improve the amine absorption capacity, thus reducing amine circulation rate. In cement or steel 
STRIPPER
LEAN/RICH EXCHANGER
RICH AMINE
RICH AMINE
LEAN AMINE
WATER VAPOR 
RECOMPRESSION
WATER VAPOR RECYCLE
LEAN AMINE/
WATER VAPOR
SOLVENT 
RECLAIMING
INDUSTRIAL
FEED GAS
LEAN AMINE
INDUSTRIAL
FEED GAS
TREATED GAS
TO STACK
PRESCRUBBER PRESCRUBBER
BLOWDOWN
REBOILER
STEAM
WASH WATER
INTERCOOLER
REFLUX
ACCUMULATOR
REFLUX PUMP
CONDENSER
CO2
ABSORBER

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
31 
applications, in or after the cooling section the feed gas is also scrubbed with caustic to capture 
residual acid compounds (SO2, hydrogen chloride, etc.). 
4.2.1.2 CO2 Absorber 
The Cansolv absorber is a single, rectangular, acid resistant, steel- or resin-lined concrete 
structure containing stainless-steel packing, a typical design for large-scale units. There is a 
packed section used for CO2 absorption, and another packed section used for water-wash. This 
specific absorber geometry and design provides several cost advantages over more traditional 
column configurations while maintaining equivalent or elevated performance. The feed gas 
enters the absorber and flows counter-current to the Cansolv solvent. 
The lean solvent absorbs 90–99 percent of the inlet CO2, depending on the design capture rate, 
and the remaining CO2 exits the main absorber section and enters the water-wash section of 
the absorber.  Prior to entering the bottom packing section, hot amine is collected, removed, 
and pumped through a heat exchanger (HX) to provide intercooling and maintain a low 
temperature favorable to absorption. The cooled amine is then sent back to the absorber just 
above the final packed section.   
The water-wash section at the top of the absorber is used to remove volatiles or entrained 
amine from the treated gas, as well as to condense and retain water in the system. The wash 
water is removed from the bottom of the wash section, pumped through a HX, and is then re-
introduced at the top of the wash section. This wash water is made up of recirculated wash 
water as well as water condensed from the treated gas; excess water resulting from 
condensation overflows to the lower absorption section through a chimney tray. The CO2-lean 
gas treated in the water-wash section is then released to the atmosphere. 
4.2.1.3 Amine Regeneration 
The rich amine is collected at the bottom of the absorber and pumped through multiple parallel 
rich/lean HXs where heat from the lean amine is exchanged with the rich amine. The Cansolv 
rich/lean solvent HXs are a stainless-steel plate and frame type with a typical 5°C (9°F) approach 
temperature. The rich amine continues and enters the stripper near the top of the column.  
The stripper is a stainless-steel vessel using structured stainless-steel packing. The regenerator 
reboiler uses low pressure steam to boil water vapor from the solvent; this vapor flows 
upwards, counter-current to the rich amine flowing downwards, and removes CO2 from the 
amine. Steam is provided by the NG-fired boiler described in Section 4.3. The Cansolv 
regenerator reboiler is a stainless-steel plate and frame type with a 3°C (5°F) approach 
temperature. Lean amine is collected in the stripper bottoms and flows to a flash vessel where 
water vapor is released. This lean solvent is then pumped through the same rich/lean HX to 
exchange heat from the lean amine to the rich amine and continues to the lean amine tank.   
The water vapor and stripped CO2 flow up the stripper where they are contacted with recycled 
reflux to condense a portion of the vapor and collect entrained solvent droplets. The remaining 
gas continues to the condenser where it is partially condensed. The two-phase mixture then 
flows to a reflux accumulator where the CO2 product gas is separated and sent to the CO2

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
32 
compressor at approximately 0.2 MPa (29 psia), and the remaining water is collected and 
returned to the stripper as reflux.   
The flow of steam to the regenerator reboiler is proportional to the rich amine flow to the 
stripper; however, the flow of low-pressure steam is also dependent on the stripper top 
temperature. 
4.2.1.4 Amine Purification 
The purpose of the amine purification, or amine reclaiming, section is to remove a portion of 
the heat-stable salts as well as ionic and non-ionic amine degradation products. The Cansolv 
amine purification (reclaiming) is essentially a distillation operation, in which the usable amine 
is boiled off the degraded solvent, which is recovered at the bottom of the column for disposal. 
4.2.2 ADIP-Ultra Pre-Combustion Capture 
The AGR utilized in the refinery hydrogen case is the ADIP-Ultra CO2 capture technology 
developed by Shell. This pre-combustion process, the latest evolution of the ADIP-Ultra process, 
uses a proprietary amine-based solvent capable of bulk removal of CO2 from high pressure gas 
streams. This technology has been deployed and is currently in operation at Shell’s Quest facility 
in Alberta, Canada. [15] A typical flowsheet is shown in Exhibit 4-4. 
Exhibit 4-4. ADIP-Ultra CO2 capture typical process flow diagram 
 
4.2.2.1 CO2 Absorber 
The feed gas is sent through a knockout vessel to remove water and liquid hydrocarbons if any 
are present. The knockout vessel produces a saturated vapor stream that is sent to the CO2 
absorber. A lean solvent stream enters the top of the absorber and flows down over trays to 
absorb CO2 from the feed gas stream. The feed gas stream flows countercurrent to the solvent 
stream, which absorbs 90–99 percent of inlet CO2, depending on the design capture rate.  
ABSORBER
REGENERATOR
LEAN/RICH EXCHANGER
RICH AMINE
RICH AMINE
LEAN AMINEINDUSTRIAL
FEED GAS
FEED GAS
FEED GAS 
KNOCKOUT
KNOCKOUT
LIQUIDS
REBOILER
STEAM
INTERCOOLER
REFLUX
ACCUMULATOR
REFLUX PUMP
CONDENSER
LOW-PRESSURE CO2
TREATED GAS 
KNOCKOUT
TREATED GAS
TO PSA
LEAN
AMINE
COOLER
FLASH VESSEL
MID-PRESSURE CO2
COOLING
WATER

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
33 
Treated gas exits through the top of the absorber and is sent through a second knockout vessel 
to remove entrained amine droplets using a mist pad before being routed to the pressure-swing 
adsorption unit for the production of high purity hydrogen. A rich solvent stream exits through 
the sump of the absorber and is routed towards the amine regeneration section. 
4.2.2.2 Amine Regeneration 
The rich solvent stream flows through a rich/lean HX, where rich solvent is heated by lean 
solvent moving to the absorber. To minimize reboiler duty and compression power, part of the 
CO2 (mid-pressure) in the rich amine is then flashed off in a hot flash vessel and routed towards 
compression and dehydration. 
The remaining rich amine liquid continues to the stripper, entering near the top of the column.  
The regenerator reboiler indirectly uses low pressure steam to produce water vapor that flows 
upwards, counter-current to the rich amine flowing downwards, and removes CO2 from the 
amine. Steam is provided by the NG-fired boiler described in Section 4.3. The lean solvent flows 
from the bottom of the regenerator tower and is pumped through the same rich/lean HX to 
exchange heat from the lean amine to the rich amine and continues to the absorber.   
The acid gas from the stripping section is washed in the water wash section of the regenerator 
to remove entrained amine. The gas is then cooled in an overhead condenser and sent to a 
reflux vessel where CO2 and water are separated. Low-pressure CO2 is sent to compression and 
dehydration, while water is returned to the stripper via regenerator reflux pumps. 
4.3 INDUSTRIAL BOILER 
AGR unit configurations detailed in the prior two sections require low pressure steam at 71 psia 
for solvent regeneration. Since no assumptions regarding available steam are made about the 
base plants, cases requiring CO2 separation and purification also require the addition of a boiler 
for steam production. 
A quote for an industrial steam boiler was obtained from CleaverBrooks in March 2021. [16] The 
boiler produces superheated steam at 100 psig. For each case requiring an AGR unit, the total 
heat required from 71 psia steam for solvent regeneration was calculated, and that amount of 
heat delivered from the referenced boiler was modeled as part of the Aspen Plus® (Aspen) 
simulation. Boiler auxiliary power requirements for pumps and compressors were scaled based 
on the quoted information. Consumables include NG fuel usage, as predicted by the Aspen 
model for each case, and feedwater makeup, calculated by methods consistent with those used 
to estimate feedwater makeup in BBR4 cases. 
4.4 COOLING WATER UNIT 
As previously stated, no characterization of the base plant for each process was assessed; as 
such, no assumptions were made regarding the existing plant’s cooling water system. Therefore, 
it is assumed for the purpose of this report that any cooling required by the compression train, 
and in some cases the AGR unit, must be supplied by a stand-alone cooling water unit.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
34 
Power consumption estimates for the cooling water system (i.e., circulating water pumps and 
cooling tower fans) were calculated based on methodology consistent with that of BBR4 cases. 
Cost estimates for the cooling water system were scaled from Case B11A-BR of NETL’s 
“Eliminating the Derate of Carbon Capture Retrofits” (Derate Study) based on QGESS guidance 
for capital cost scaling. [17] [3] This account was scaled from the Derate Study because Case 
B11A-BR is more representative of the size range for the cooling water system associated with 
the cases in this report. 
4.5 HEAT EXCHANGERS 
Cooling of the product CO2 is required for all cases following compression to meet the pipeline 
temperature specification of 86°F, and in some cases, cooling is also required preceding 
compression. For cases using a reciprocating compressor, post-cooling of the compressed 
product CO2 is included in the compressor quote. The quoted discharge temperature of the 
centrifugal compressors referenced are higher than the pipeline specification temperature of 
86°F and require cooling. For those cases, after-cooler costs were scaled from BBR4 Case B12B 
based on HX duty as predicted by Aspen, consistent with QGESS cost scaling methodology. 
Cases with reciprocating compression do not depict an aftercooler HX in the block flow 
diagrams (BFDs) throughout Section 5. For the cases with centrifugal compression, the HX is 
depicted downstream of the compressor in the BFDs throughout Section 5 and Section 6. 
Cooling of the CO2 at the inlet of the compression train is dependent on the quoted 
compression train suction temperature and the base plant assumptions regarding the 
temperature at which the CO2 is available. A pre-cooler HX is required only for the Ethanol case, 
where fermentation produces a CO2 stream with a temperature of 320°F, which far exceeds the 
suction temperature of the reciprocating compressor employed. The cost of this exchange was 
developed from heuristics in Analysis, Synthesis, and Design of Chemical Processes, assuming a 
floating head shell-and-tube HX with a heat transfer coefficient equal to 6.2 Btu/hour-square 
foot-°F. [18] 
4.6 ANCILLARY EQUIPMENT, BUILDINGS, AND STRUCTURES 
Ancillary equipment associated with implementing the capture and compression systems in this 
report include an accessory electrical plant and instrumentation and control (I&C) equipment. 
In addition, some site improvements, such as ground preparation and additional facilities, 
would be required for the construction and ongoing operation of the equipment considered. 
Estimates for these costs were scaled per QGESS guidance based on Case B11A-BR of the Derate 
Study, as the costs of this reference case are approximately comparable to those that would be 
incurred with the addition of the equipment detailed throughout the prior sub-sections. [17]

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
35 
5 COST AND PERFORMANCE: HIGH PURITY SOURCES 
The sources discussed in this section are considered high purity sources, meaning the available 
CO2 does not require AGR to meet EOR pipeline specifications. In some high purity cases, 
dehydration of the CO2 stream using a triethylene glycol (TEG) system may be required. 
5.1 AMMONIA 
It is estimated that the U.S. gross ammonia production in 2019 was over 19.2 M tonnes. [19] In 
all but one plant in the United States, the ammonia production process first reforms a NG 
feedstock to produce hydrogen (H2), carbon monoxide (CO), and CO2. The unconverted CO from 
reforming is then shifted to produce more H2 and CO2. The optimum ratio of H:N for ammonia 
synthesis is 3:1; therefore, the amount of CO2 removed from the post-shift stream must be high 
to optimize the H:N ratio. A portion of the CO2 removed from the post-shift stream is often 
captured and reused to produce urea, by reacting ammonia with CO2. The amount of CO2 
captured and reused for ammonia derivatives will vary from plant to plant based on production 
capacities and market opportunities for each product. With CO2 removal inherent to the 
ammonia process, coupled with the need for CO2 to convert ammonia into ammonia 
derivatives, ammonia processing is a potentially low-cost option for industrial CO2 capture. 
5.1.1 Size Range 
As of 2019, there were 32 ammonia plants in the United States, 19 of which fell in the range of 
0.1–0.6 M tonnes/year (0.11–0.66 M tons/year) production capacity, and nine had a capacity of 
600,000 tonnes/year or greater. The largest U.S. ammonia plant has a capacity of 4.3 M 
tonnes/year. [19] For the purposes of this study, the ammonia case is represented with a 
production capacity of 394,000 tonnes ammonia/year. 
5.1.2 CO2 Point Sources 
The main point sources of CO2 emissions in an ammonia plant comes from the flue gas from the 
primary reformer and the vent from the CO2 stripper that separates CO2 from the ammonia 
syngas. Of these two, only the CO2 stripper vent is considered a high purity source of CO2. The 
primary reformer flue gas has a CO2 concentration of approximately 18 mol% and would be 
considered a low purity source of CO2. [20] [21] As such, it is not considered in this study case 
but may be evaluated as part of future work, as discussed in Section 9.1. 
An article published by KBR Technology [22] concerning CO2 capture in the ammonia industry 
stated that for an average ammonia plant producing 660,000 tonnes/year ammonia, 
approximately 34 percent of CO2 emissions come from the primary reformer flue gas and 66 
percent are emitted by the CO2 stripper vent. The total CO2 produced in ammonia production 
(i.e., that of both the primary reformer and the CO2 stripper) is 1.87 tonnes CO2/tonne 
ammonia. [22] Applying this emissions factor and the fact that 66 percent of the CO2 emissions 
would be captured from the stripper vent as a high purity source, the representative 394,000 
tonnes ammonia/year plant produces 486,227 tonnes CO2 vented from the CO2 stripper. It is 
assumed that the stripper vent CO2 concentration is 99 percent by volume. [23] The ammonia

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
36 
production process, using NG as a feedstock, is depicted in a basic BFD (Exhibit 5-1) to further 
illustrate the point-sources of CO2 described in this section. 
Exhibit 5-1. Ammonia production via NG reforming 
 
In some ammonia production facilities, portions of the ammonia and the CO2 emissions are 
further processed to create ammonia derivatives. For this study, it is assumed that the ammonia 
produced by the representative plant is not used for derivative production, and as such, the CO2 
emitted is not needed for reprocessing within the plant. In practical applications, the amount of 
CO2 available would be affected by derivative manufacturing, as well as by process 
configurations and operating parameters affecting the ratio of CO2 emitted from the stripper 
and the primary reformer. This would have to be evaluated on a case-by-case basis, and the 
assumptions in this study are employed to present an illustrative COC in a representative 
ammonia production plant. 
5.1.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the ammonia process 
for the purpose of this study: 
• The representative ammonia plant has a capacity of 394,000 tonnes ammonia per year 
• The ammonia process feedstock is NG 
• The gas from the stripper vent is assumed 99 volume percent CO2 and the balance of the 
stream (1 volume percent) is assumed to be water 
• The total high purity CO2 amount produced by the plant is 736,750 tonnes CO2/year (at 
100 percent CF); the amount generated from the stripper vent is 486,227 tonnes 
CO2/year at 100 percent CF and neglecting process losses or CO2 reuse in ammonia 
derivative production 
• The temperature of the CO2 at the stripper vent outlet is 69°F 
• The pressure of the CO2 at the stripper vent outlet is 23.52 psia 
• The end product CO2 quality is based on the EOR pipeline standard as mentioned in the 
NETL QGESS for CO2 Impurity Design Parameters [1] 
Primary 
Reformer
Natural Gas
& Steam
CO2 in flue gas CO
(~34 percent of 
process emissions)
Secondary 
Reformer
Air
Shift & CO2 
removal
High purity CO 2 
(~66 percent of 
process emissions)
Synthesis Gas 
for Ammonia 
Production

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
37 
5.1.4 CO2 Capture System 
Only cooling and compression is required for the ammonia case. Reciprocating compression 
discussed previously in Section 4.1.1 is modeled and the costs for the compressor and ancillary 
equipment is estimated as outlined in Section 3 and Section 4. Based on mass flow rate, this 
represents a large scale with up to 3.39 times the quoted flow rate. 
5.1.5 BFD, Stream Table, and Performance Summary 
There is no cooling of the high purity CO2 stream from the ammonia plant since it is assumed 
that the overhead condenser of the stripping column discharges at a temperature of 69°F. A 
water knockout step is considered to avoid water condensation within the compression train. 
The costs for the water knockout were estimated using methods in Analysis, Synthesis, and 
Design of Chemical Processes. [18] After compression, the CO2 product stream is cooled and 
sent directly for EOR or other usage. Exhibit 5-2 gives the BFD for this process.  Exhibit 5-3 
provides the stream table. 
Exhibit 5-2. Ammonia CO2 capture BFD 
 
Exhibit 5-3. Ammonia stream table 
  1 2 3 
V-L Mole Fraction       
Ar 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 
CO2 0.9709 0.9887 0.9995 
SO2 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 
H2O 0.0291 0.0113 0.0005 
H2S 0.0000 0.0000 0.0000 
N2 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 
        
V-L Flowrate (kgmol/hr) 1,299 1,276 1,261 
V-L Flowrate (kg/hr) 56,189 55,767 55,488 
Temperature (°C) 21 21 30 
Pressure (MPa, abs) 0.16 0.2 15.3 
Ammonia 
Plant
Water 
Knockout
Desired 
Usage1 2 Compressor 3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
38 
  1 2 3 
Steam Table Enthalpy (kJ/kg)A 8,841 8,791 8,755 
Aspen Plus Enthalpy (kJ/kg)B -9,021 -8,968 -9,195 
Density (kg/m3) 3.0 2.9 630.1 
V-L Molecular Weight 43.3 43.7 44.0 
    
V-L Flowrate (lbmol/hr) 2,864 2,812 2,780 
V-L Flowrate (lb/hr) 123,876 122,946 122,330 
Temperature (°F) 69 69 86 
Pressure (psia) 23.5 23.5 2,214.7 
Steam Table Enthalpy (Btu/lb)A 3,801 3,779 3,764 
Aspen Plus Enthalpy (Btu/lb)B -3,878 -3,855 -3,953 
Density (lb/ft3) 0.184 0.183 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance results are based on the reciprocating compressor quote and are provided in 
Exhibit 5-4.  
Exhibit 5-4. Performance summary 
Performance Summary 
Item 394,000 tonnes ammonia/year (kWe) 
CO2 Compressor 5,770 
Circulating Water Pumps 60 
Cooling Tower Fans 30 
Total Auxiliary Load 5,860 
5.1.6 Capture Integration 
In an existing ammonia plant, a cooling water system that could accommodate the additional 
cooling needs of the compressor intercoolers modeled in this case may be in place to satisfy the 
condenser cooling duty for the CO2 removal system. This is especially true if an ammonia plant 
is designed to produce ammonia derivatives. However, for this study, a stand-alone cooling 
system is required to provide for the compressor’s intercooling needs. In real applications, the 
inclusion of an additional cooling water system would be evaluated on a case-by-case basis. 
5.1.7 Power Source 
Given the relatively small amount of CO2, the compression power consumption is 5.77 MW.  
Power consumption estimates for the cooling system were scaled as described in Section 4.4. 
The total power requirement was calculated to be 5.86 MW , which includes all power required

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
39 
by the compression train and the cooling water system. Purchased power cost is estimated at a 
rate of $60/MWh as discussed in Section 3.1.2.4. 
5.1.8 Economic Analysis Results 
The economic results for CO2 capture application in an ammonia plant are presented in this 
section. Owner’s costs (Exhibit 5-5), capital costs (Exhibit 5-6), and O&M costs are calculated as 
discussed in Section 3.1. Retrofit costs were determined by applying a retrofit factor to TPC as 
discussed in Section 3.3. The greenfield TOC for the ammonia case is $45.6 M. The 
corresponding greenfield COC is $19.0/tonne CO2, and the COC is $19.0/tonne CO2 in retrofit 
applications. The small difference between greenfield and retrofit COC in this case is not 
apparent due to rounding. 
Exhibit 5-5. Owner’s costs for ammonia greenfield site 
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $423 $1 
1-Month Maintenance Materials $35 $0 
1-Month Non-Fuel Consumables $70 $0 
1-Month Waste Disposal $3 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 
2% of TPC $747 $2 
Total $1,278 $3 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $134 $0 
0.5% of TPC (spare parts) $187 $0 
Total $321 $1 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $5,602 $12 
Financing Costs $1,008 $2 
TOC $45,587 $94 
TASC Multiplier (Ammonia, 31 year) 1.035  
TASC $47,162 $97

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
40 
Exhibit 5-6. Capital costs for ammonia greenfield site 
Case: Ammonia Estimate Type:  Conceptual 
Representative Plant Size:  394,000 tonnes ammonia/year Cost Base: Dec 2018 
Item 
No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.1 Inlet Water Knockout for Compression $11 $0 $2 $0 $14 $2 $0 $3 $19 $0 
5.4 CO2 Compression & Drying $6,192 $929 $2,070 $0 $9,192 $1,609 $0 $2,160 $12,960 $27 
5.5 CO2 Compressor Aftercooler w/5.4 w/5.4 w/5.4 w/5.4 $0 $0 $0 $0 $0 $0 
5.7 TEG Dryer (within compression train) $1,900 $285 $635 $0 $2,821 $494 $0 $663 $3,977 $8 
  Subtotal $8,104 $1,214 $2,708 $0 $12,026 $2,105 $0 $2,826 $16,957 $35 
 7 Ductwork & Stack 
7.3 Ductwork $0 $164 $114 $0 $277 $49 $0 $65 $391 $1 
  Subtotal $0 $164 $114 $0 $277 $49 $0 $65 $391 $1 
 9 Cooling Water System 
9.1 Cooling Towers $163 $0 $50 $0 $213 $37 $0 $50 $301 $1 
9.2 Circulating Water Pumps $13 $0 $1 $0 $14 $2 $0 $3 $20 $0 
9.3 Circulating Water System Aux. $321 $0 $42 $0 $364 $64 $0 $85 $513 $1 
9.4 Circulating Water Piping $0 $149 $135 $0 $283 $50 $0 $67 $399 $1 
9.5 Make-up Water System $52 $0 $67 $0 $119 $21 $0 $28 $167 $0 
9.6 Component Cooling Water System $23 $0 $18 $0 $41 $7 $0 $10 $58 $0 
9.7 Circulating Water System Foundations $0 $19 $31 $0 $50 $9 $0 $12 $71 $0 
  Subtotal $572 $167 $344 $0 $1,084 $190 $0 $255 $1,528 $3 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,725 $0 $148 $0 $1,873 $328 $0 $440 $2,642 $5 
11.3 Switchgear & Motor Control  $2,679 $0 $465 $0 $3,143 $550 $0 $739 $4,432 $9 
11.4 Conduit & Cable Tray $0 $348 $1,003 $0 $1,352 $237 $0 $318 $1,906 $4 
11.5 Wire & Cable $0 $922 $1,648 $0 $2,570 $450 $0 $604 $3,624 $7 
  Subtotal $4,404 $1,270 $3,265 $0 $8,939 $1,564 $0 $2,101 $12,604 $26 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $353 $282 $1,130 $0 $1,765 $309 $0 $415 $2,489 $5 
12.9 Other I&C Equipment $434 $0 $1,005 $0 $1,439 $252 $0 $338 $2,029 $4 
  Subtotal $787 $282 $2,135 $0 $3,204 $561 $0 $753 $4,518 $9 
 13 Improvements to Site 
13.1 Site Preparation $0 $22 $440 $0 $461 $81 $0 $108 $651 $1 
13.2 Site Improvements $0 $102 $136 $0 $238 $42 $0 $56 $336 $1 
13.3 Site Facilities $117 $0 $123 $0 $240 $42 $0 $56 $339 $1 
  Subtotal $117 $124 $698 $0 $940 $164 $0 $221 $1,325 $3 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $9 $7 $0 $17 $3 $0 $4 $23 $0 
  Subtotal $0 $9 $7 $0 $17 $3 $0 $4 $23 $0 
  Total $13,985 $3,231 $9,271 $0 $26,487 $4,635 $0 $6,225 $37,347 $77

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
41 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-7 while Exhibit 5-8 shows the COC for greenfield and retrofit sites for the representative 
ammonia plant. 
Exhibit 5-7. Initial and annual O&M costs for ammonia greenfield site 
Case:  Ammonia  Cost Base: Dec 2018 
Representative Plant Size:  394,000 tonnes ammonia/year  Capacity Factor (%): 85 
O&M Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $0.90 
Maintenance Labor:     $239,021 $0.49 
Administrative & Support Labor:     $169,365 $0.35 
Property Taxes and Insurance:     $746,941 $1.54 
Total:     $1,593,765 $3.28 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $358,532 $0.87 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 46 $1.90 $0 $27,119 $0.07 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 0.1 $550.00 $0 $24,747 $0.06 
Triethylene Glycol (gal): w/equip. 312 $6.80 $0 $658,287 $1.59 
Subtotal:    $0 $710,152 $1.72 
Waste Disposal 
Triethylene Glycol (gal):  312 $0.35 $0 $33,882 $0.08 
Subtotal:    $0 $33,882 $0.08 
Variable Operating Costs Total:    $0 $1,102,566 $2.67 
Exhibit 5-8. COC for 394,000 tonnes/year ammonia greenfield and retrofit A 
Component Greenfield Value, $/tonne CO2 Retrofit Value, $/tonne CO2 
Capital 6.1 6.1 
Fixed 3.9 3.9 
Variable 2.7 2.7 
Purchased Power 6.3 6.3 
Total COC 19.0 19.0 
ADifferences in COC for greenfield and retrofit applications of this case are not apparent due to rounding.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
42 
5.1.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to ammonia plant capacity is shown in Exhibit 
5-9. As the plant capacity increases, more CO2 is available for capture, thus realizing economies 
of scale. This generic scaling exercise assumes that equipment is available at continuous 
capacities; however, equipment is often manufactured in discrete sizes, which would possibly 
affect the advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 5-9. Ammonia plant capacity sensitivity  
 
Note: The data point for the COC at a 394,000 tonnes/year ammonia plant does not fall on the COC line due to data point 
increments and plot formatting. 
5.1.10 Ammonia Conclusion 
The high purity CO2 stream produced from ammonia plants makes them a relatively low-cost 
industrial process for CO2 capture since the plant itself acts as the separation medium. 
Economic analysis of the additional CO2 compression system required for capture resulted in a 
COC of CO2 equal to $19.0/tonne CO2 for a greenfield site and $19.0/tonne CO2 for a retrofit 
application. The small disparities (not visible due to roundingg) between greenfield and retrofit 
cases are the result of unknown difficulties required for a retrofit installation versus a greenfield 
application, assuming adequate plot plan space for the retrofit case exists. The sensitivity 
analysis for plant capacity, when varied from 0.1 M tonnes/year to 2.1 M tonnes/year ammonia 
production, showed a change in COC of $13.6/tonne CO2. 
 
g For instance, the TASC for the retrofit ammonia case is $47.5 million, which is higher in comparison to the TASC for the 
greenfield ammonia case (i.e., $47.2 million) as presented in Exhibit 5-5.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
43 
It should be noted that for existing U.S. ammonia plants producing excess high purity CO2, this 
CO2 may already be processed and sold for other uses. For example, in addition to urea and 
other ammonia derivative production, some ammonia plants also produce food-grade liquid 
CO2 as a sellable product. This would reduce or eliminate the amount of high purity CO2 
potentially available for capture as evaluated in this study. This scenario was not considered in 
this study as it would need to be evaluated on a case-by-case basis. 
5.2 ETHYLENE OXIDE 
Ethylene oxide (EO) is a colorless flammable gas that is mainly used as a raw material for 
production of several industrial chemical intermediates. When assessed by region, 73 percent of 
North American EO production goes directly to synthesis of ethylene glycol, which is used in 
antifreeze, polyester, liquid solvents, and plastics production. [24]  
EO is produced by direct oxidation of ethylene in the presence of a silver catalyst. The reaction 
conditions range 200–300°C and 10–30 bar. [24] Literature suggests that with the catalyst 
driving the competing reactions (Equation 5-1) towards more EO production, CO2 is produced 
during the oxidation reaction in a ratio of 6:2 EO:CO2 on a molar basis. As a result of the 
competing steam and CO2 producing, CO2 concentration of the emissions stream can range 30–
100 percent CO2 [25] with the balance of the emissions stream being water, but most references 
give a range of 95–100 percent CO2 concentration, indicating that a purification step (i.e., water 
removal from the emissions stream) is inherent to the EO production plant. [26]   
𝐶2𝐻4 + 1 2⁄ 𝑂2 𝑆𝑖𝑙𝑣𝑒𝑟 𝐶𝑎𝑡𝑎𝑙𝑦𝑠𝑡→           𝐶2𝐻4𝑂 
𝐶2𝐻4 + 5𝑂2
𝑦𝑖𝑒𝑙𝑑𝑠
→    2𝐶𝑂2 + 2𝐻2𝑂 
Equation 
5-1 
5.2.1 Size Range 
Current EO U.S. plant sizes range 105,000–770,000 tonnes. [27] Exhibit 5-10 shows the ten U.S. 
EO production facilities and their associated capacity as of 2007. 
Exhibit 5-10. 2007 U.S. EO production facility capacities 
Company Location Capacity (1,000 tonnes EO/year) 
BASF Geismar, Louisiana 220 
Dow Chemical Plaquemine, Louisiana 275 
Dow Chemical Seadrift, Texas 430 
Dow Chemical Taft, Louisiana 770 
Eastman Chemical Longview, Texas 105 
Formosa Plastics Point Comfort, Texas 250 
Huntsman Port Neches, Texas 460 
LyondellBasell Bayport, Texas 360 
Old World Industries Clear Lake, Texas 355 
Shell Chemicals Geismar, Louisiana 420

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
44 
The U.S. contains 10 major producers totaling an EO production of 3.6 M tonnes. The average 
2007 U.S. plant capacity is 364,500 tonnes EO, which is representative of the majority of EO 
plants and, thus, is the production capacity basis for the EO case in this study. With a 6:2 ratio of 
EO:CO2, a plant with a 3.6 M tonnes annual EO production capacity would produce 121,500 
tonnes CO2/year at 100 percent CF. The International Energy Agency Greenhouse Gas R&D 
Programme (IEAGHG) database gives an average annual emission for the 52 worldwide EO 
production sites of 150,000 tonnes CO2 per plant [24], which is within range of the assumed 
emissions rate for the representative EO plant evaluated. 
5.2.2 CO2 Point Sources 
EO is considered a high purity source of CO2. The process has a single CO2 source: the CO2 
removal system that is assumed an inherent part of the EO production process. The removal 
system may be one of several types—physical sorbents such as Rectisol or Selexol, chemical 
sorbents such as aqueous amines, or cryogenic separation systems. This study assumes that the 
base plant employs a physical sorbent Rectisol unit, with the CO2 stream to be captured 
available at a pressure of 43.5 psia and a temperature of 96°F. For this study, the concentration 
of the CO2 emissions stream is assumed to be 100 percent CO2. 
5.2.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the EO process for the 
purpose of this study: 
• The representative plant has a production capacity of 364,500 tonnes of EO/year 
• The CO2 generated at 100 percent CF is 121,500 tonnes CO2/year.  
• The CO2 stream is 100 percent CO2 
• Due to 100 percent purity, only compression and cooling are required 
• The CO2 stream temperature is 96°F 
• The CO2 stream pressure is 43.5 psia 
• The end product CO2 quality is based on the EOR pipeline standard as mentioned in the 
NETL QGESS for CO2 Impurity Design Parameters [1] 
5.2.4 CO2 Capture System 
For the EO case considered in this report, CO2 separation is an inherent part of base plant 
operations, and only the addition of compression and associated intercooling are required. 
Given the low CO2 flowrate, reciprocating compression is employed and scaled for this case. 
Based on mass flow rate, this represents a scale down of 15 percent versus the quoted flow rate 
as given previously in Section 4.1.2.   
The suction pressure to the first stage of the reciprocating compressor is quoted as 17.43 psia, 
which is below the assumed stream pressure for this case of 43.5 psia. However, the assumed 
CO2 stream pressure nearly matches the quoted 44.04 psia suction pressure to the second stage 
of the compressor. Therefore, when implementing this quote, the first stage is bypassed, and 
the CO2 stream is introduced into the second stage. This reduces the overall power consumption

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
45 
of the compression train. The cost was adjusted to account for the removal of the first stage by 
scaling on power requirement, resulting in a 21.4 percent reduction in cost, as compared to the 
quoted value. 
5.2.5 BFD, Stream Table, and Performance Summary 
Since the EO absorption/separation process releases 100 percent pure CO2, only cooling and 
compression is required for the CO2 stream to be sent directly for EOR or other usage.  As 
shown in Exhibit 5-11, the vent, which is at a lower temperature than required by the 
compressor, is sent directly to the compression train. Since the compression train includes a 
post-cooler, after-cooling is not represented here. Exhibit 5-12 provides the stream table. 
Exhibit 5-11. EO CO2 capture BFD 
 
Exhibit 5-12. EO stream table 
  1 2 
V-L Mole Fraction     
AR 0.0000 0.0000 
CH4 0.0000 0.0000 
CO 0.0000 0.0000 
CO2 1.0000 1.0000 
SO2 0.0000 0.0000 
H2 0.0000 0.0000 
H2O 0.0000 0.0000 
H2S 0.0000 0.0000 
N2 0.0000 0.0000 
Total 1.0000 1.0000 
      
V-L Flowrate (kgmol/hr) 315 315 
V-L Flowrate (kg/hr) 13,870 13,870 
Temperature (°C) 36 30 
Pressure (MPa, abs) 0.30 15.3 
Steam Table Enthalpy (kJ/kg)A 8,759 8,753 
Aspen Plus Enthalpy (kJ/kg)B -8,935 -9,193 
Density (kg/m3) 5.2 629 
V-L Molecular Weight 44.0 44.0 
   
V-L Flowrate (lbmol/hr) 695 695 
EO Plant Desired Usage1 Compressor 2

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
46 
  1 2 
V-L Mole Fraction     
V-L Flowrate (lb/hr) 30,578 30,578 
Temperature (°F) 96 86 
Pressure (psia) 43.5 2,214.7 
Steam Table Enthalpy (Btu/lb)A 3,765 3,763 
Aspen Plus Enthalpy (Btu/lb)B -3,841 -3,952 
Density (lb/ft3) 0.325 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance summary is provided in Exhibit 5-13. 
Exhibit 5-13. Performance summary 
Performance Summary 
Item 364,500 tonnes/year (kWe) 
CO2 Compressor 1,180 
Circulating Water Pumps 10 
Cooling Tower Fans 10 
Total Auxiliary Load 1,200 
5.2.6 Capture Integration 
The reactor effluent is received by the AGR absorber at a temperature of 410°F [28] and 
requires cooling, indicating an existing cooling water system. A cooling water system from the 
retrofit could potentially be integrated into the existing plant’s cooling water system; however, 
depending on the size of the existing cooling water system and the design cooling temperature 
range, it might be more economical to install a stand-alone cooling system rather than increase 
the existing cooling system. This would have to be evaluated on a case-by-case basis. If a power 
plant using a steam cycle is present within the EO facility, an efficient HX could capture this 
energy to heat condensate make-up. 
For the purposes of this study, it is assumed that an additional, stand-alone cooling water unit 
will perform the necessary cooling for compression intercooling. However, there is a potential 
for integration of make-up water to be used to feed or partially feed the cooler thereby 
reducing the unit’s size or replacing it with a simple heat exchanger depending on the size of the 
plant. These options are not evaluated within the scope of this study. 
5.2.7 Power Source 
Given the relatively small amount of CO2, the compressor power consumption is 1.18 MW.  
Power consumption estimates for the cooling water system were scaled as described in Section 
4.4. The total power requirement was approximated to be 1.2 MW , which includes all power 
required by the compression train and the cooling water system. Purchased power cost is

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
47 
estimated at a rate of $60/MWh as discussed in Section 3.1.2.4. Given that the EO reaction is 
exothermic, and this additional heat is possibly used to generate steam, an EO plant may 
already generate power on-site for other usage, and this power may be available as an 
alternative to purchasing power from the grid. The availability of on-site power would need to 
be evaluated on a case-by-case basis and is not considered within the scope of this report. 
5.2.8 Economic Analysis Results 
The economic results for CO2 capture application in an EO plant are presented in this section. 
Owner’s costs (Exhibit 5-14), capital costs (Exhibit 5-15), and O&M costs are calculated as 
discussed in Section 3.1. Retrofit costs were determined by applying a retrofit factor to TPC as 
discussed in Section 3.3. The greenfield TOC for the EO case is $20.4 M. The corresponding 
greenfield COC is $26.0/tonne CO2, and the COC is $26.2/tonne CO2 in retrofit applications. 
Exhibit 5-14. Owner’s costs for EO greenfield site 
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $341 $3 
1-Month Maintenance Materials $16 $0 
1-Month Non-Fuel Consumables $1 $0 
1-Month Waste Disposal $0 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 
2% of TPC $333 $3 
Total $690 $6 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $1 $0 
0.5% of TPC (spare parts) $83 $1 
Total $84 $1 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $2,495 $21 
Financing Costs $449 $4 
TOC $20,385 $168 
TASC Multiplier (EO, 31 year) 1.025   
TASC $20,892 $172

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
48 
Exhibit 5-15. Capital costs for EO greenfield site 
Case: Ethylene Oxide Estimate Type:  Conceptual 
Representative Plant Size:  364,500 tonnes EO/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.4 CO2 Compression & Drying $2,352 $353 $786 $0 $3,491 $611 $0 $820 $4,922 $41 
5.5 CO2 Compressor Aftercooler w/5.4 w/5.4 w/5.4 w/5.4 $0 $0 $0 $0 $0 $0 
 Subtotal $2,352 $353 $786 $0 $3,491 $611 $0 $820 $4,922 $41 
 7 Ductwork & Stack 
7.3 Ductwork $0 $41 $29 $0 $70 $12 $0 $16 $99 $1 
 Subtotal $0 $41 $29 $0 $70 $12 $0 $16 $99 $1 
 9 Cooling Water System 
9.1 Cooling Towers $52 $0 $16 $0 $68 $12 $0 $16 $95 $1 
9.2 Circulating Water Pumps $4 $0 $0 $0 $4 $1 $0 $1 $5 $0 
9.3 Circulating Water System Aux. $125 $0 $17 $0 $142 $25 $0 $33 $200 $2 
9.4 Circulating Water Piping $0 $58 $53 $0 $111 $19 $0 $26 $156 $1 
9.5 Make-up Water System $25 $0 $32 $0 $57 $10 $0 $13 $81 $1 
9.6 Component Cooling Water System $9 $0 $7 $0 $16 $3 $0 $4 $23 $0 
9.7 Circulating Water System Foundations $0 $8 $13 $0 $21 $4 $0 $5 $30 $0 
 Subtotal $215 $66 $138 $0 $418 $73 $0 $98 $590 $5 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $873 $0 $75 $0 $947 $166 $0 $223 $1,336 $11 
11.3 Switchgear & Motor Control  $1,355 $0 $235 $0 $1,590 $278 $0 $374 $2,241 $18 
11.4 Conduit & Cable Tray $0 $176 $507 $0 $684 $120 $0 $161 $964 $8 
11.5 Wire & Cable $0 $466 $834 $0 $1,300 $227 $0 $305 $1,833 $15 
 Subtotal $2,227 $642 $1,651 $0 $4,521 $791 $0 $1,062 $6,374 $52 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $287 $230 $919 $0 $1,437 $251 $0 $338 $2,026 $17 
12.9 Other I&C Equipment $353 $0 $818 $0 $1,171 $205 $0 $275 $1,651 $14 
 Subtotal $640 $230 $1,737 $0 $2,607 $456 $0 $613 $3,677 $30 
 13 Improvements to Site 
13.1 Site Preparation $0 $16 $320 $0 $336 $59 $0 $79 $474 $4 
13.2 Site Improvements $0 $75 $99 $0 $174 $30 $0 $41 $245 $2 
13.3 Site Facilities $85 $0 $90 $0 $175 $31 $0 $41 $247 $2 
 Subtotal $85 $90 $509 $0 $685 $120 $0 $161 $965 $8 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $4 $3 $0 $7 $1 $0 $2 $10 $0 
 Subtotal $0 $4 $3 $0 $7 $1 $0 $2 $10 $0 
 Total $5,520 $1,427 $4,852 $0 $11,799 $2,065 $0 $2,773 $16,636 $137

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
49 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-16, while Exhibit 5-17 shows the COC for greenfield and retrofit sites for the representative EO 
plant. 
Exhibit 5-16. Initial and annual O&M costs for EO greenfield site 
Case:  Ethylene Oxide Cost Base: Dec 2018 
Representative Plant Size:  364,500 tonnes EO/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $3.61 
Maintenance Labor:     $106,470 $0.88 
Administrative & Support Labor:     $136,227 $1.12 
Property Taxes and Insurance:     $332,718 $2.74 
Total:     $1,013,852 $8.34 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $159,705 $1.55 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 10 $1.90 $0 $6,099 $0.06 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 0.03 $550.00 $0 $5,260 $0.05 
Subtotal:    $0 $11,359 $0.11 
Variable Operating Costs Total:    $0 $171,063 $1.66 
Exhibit 5-17. COC for 364,500 tonnes/year EO greenfield and retrofit 
Component Greenfield Value, $/tonne CO2 Retrofit Value, $/tonne CO2 
Capital 9.4 9.4 
Fixed 9.8 9.9 
Variable 1.7 1.7 
Purchased Power 5.2 5.2 
Total COC 26.0 26.2

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
50 
5.2.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to EO plant capacity is shown in Exhibit 5-18. As 
the plant capacity increases, more CO2 is available for capture, thus realizing economies of 
scale. This generic scaling exercise assumes that equipment is available at continuous capacities; 
however, equipment is often manufactured in discrete sizes, which would possibly affect the 
advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 5-18. EO plant capacity sensitivity  
 
5.2.10 Ethylene Oxide Conclusion 
The high purity CO2 stream produced from EO plants makes them a relatively low-cost industrial 
process for CO2 capture, as the plant itself performs the separation of CO2 under normal 
operating conditions. A CO2 compression system for a 364,500 tonnes/year EO plant was 
modeled to estimate the COC of capturing CO2 from the AGR system. The results showed the 
COC of CO2 to be $26.0/tonne CO2 for a greenfield site and $26.2/tonne CO2 for a retrofit site. 
The small disparities between greenfield and retrofit cases are the result of unknown difficulties 
required for a retrofit installation versus a greenfield application, assuming adequate plot plan 
space for the retrofit case exists. 
The plant size sensitivity showed that as plant size decreased from 770,000 tonnes EO/year to 
105,000 tonnes EO/year, the COC increased by $26.3/tonne CO2. As the plant size is decreased, 
less CO2 is produced, and economies of scale are lost, resulting in a higher COC.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
51 
5.3 ETHANOL 
Ethanol production generates as a byproduct a high purity CO2 stream greater than 85 percent 
by volume. [29] Though not a large-scale CO2 producer, the COC is assumed to be relatively low. 
One project where CO2 is being captured from ethanol refining is the DOE-funded Archer 
Daniel’s Midlands project in Decatur, IL. The purpose of the project is to demonstrate how the 
next generation of technologies capture and store or reuse industrial CO2 emissions. [30] The 
project design states a goal to capture approximately 1 M tons of CO2/year using dehydration 
and compression and store the captured CO2 in the Mt. Simon Sandstone Formation saline 
reservoir. [30] 
5.3.1 Size Range 
There are 208 ethanol refineries in the United States demonstrating a wide range of production, 
with 90 percent of these refineries using the dry-mill process. [31]. Of the 208 ethanol refineries 
in the United States, 66 of the plants (approximately 32 percent) fall between 40 and 60 M 
gallons/year. [32] Exhibit 5-19 shows the quantities of ethanol production ranges and the 
number of plants in each designated range. It is important to note that plant capacities would 
affect the COC presented, and a sensitivity analysis evaluating the effect of plant size on COC is 
included in Section 5.3.9. However, the effects would be noted at the equipment selection level. 
For instance, CO2 produced from a 50 M gallons/year plant versus a 215+ M gallons/year plant 
requires a different type of compression (reciprocating versus centrifugal). This is due to the 
quantity of CO2 produced at each plant. Discussion of the different types of compression can be 
found in Section 4.1. 
Exhibit 5-19 U.S. Ethanol plant capacities and quantities 
Capacity Range (M gallons/year) Number of Plants 
0–50 59 
40–60 66 
51–100 81 
101–150 57 
>150 11 
 
Since a large portion of existing ethanol plants, 66 have smaller production capacities of 40–60 
M gallons/year, the plant size chosen was 50 M gallons/year, and utilized reciprocating 
compression. It was also assumed that the plant uses the dry mill process with corn as the 
feedstock of choice. 
5.3.2 CO2 Point Sources 
The major point sources of CO2 emissions at an ethanol plant result from the fermentation 
process and fuel burning to provide required process heat. Of these two sources, only the

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
52 
fermentation off-gas stream is considered high purity and is the basis for the ethanol case in this 
report. The fuel burning stream may be considered as future work, as detailed in Section 9.1.  
A study by the Illinois State Geological Survey [33] investigated the inventory of stationary CO2 
emissions in the Illinois Basin in 2007. The study reviewed a wide range of industrial processes, 
including ethanol plants. They used the relationship given in Equation 5-2 to calculate the 
amount of CO2 emissions from the fermentation point source. 
𝐶𝑂2 𝐹𝑒𝑟𝑚𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛 (𝑡𝑜𝑛𝑛𝑒𝑦𝑒𝑎𝑟 ) = [𝑒𝑡ℎ𝑎𝑛𝑜𝑙 𝑝𝑟𝑜𝑑𝑢𝑐𝑡𝑖𝑜𝑛 ( 𝑔𝑎𝑙𝑦𝑒𝑎𝑟) ∗ 𝐸𝐹 (𝑙𝑏𝐶𝑂2𝑔𝑎𝑙 )]2,000 𝑙𝑏𝑡𝑜𝑛 ∗ 1.01231 𝑡𝑜𝑛𝑡𝑜𝑛𝑛𝑒  Equation 5-2 
Where 
𝐸𝐹 = emission factor, feedstock dependent 
The generic plant assumed in the Illinois Stage Geological Survey study utilizes corn as the 
feedstock, giving an EF equal to 6.31 lb CO2/gallons ethanol. The EF was formulated in the 
Illinois Stage Geological Survey study through communication with representatives from existing 
ethanol plants in the Illinois Basin. [33] Using this relationship, the representative ethanol plant 
will generate approximately 143,042 tonnes CO2/year from fermentation (at 100 percent CF), 
with a production capacity of 50 M gallons of ethanol/year.   
A report published by the Global Carbon Capture and Sequestration (CCS) Institute in 2010 
states that “the emission in ethanol plants arise from fermentation of biomass such as sugar 
cane or corn. Fermentation results in a pure stream of CO2, which significantly reduces the cost 
for applying CCS.” [34] The fermentation process occurs at a temperature of 140–180 °C (284–
356 °F). [35] Therefore, the fermentation stream is assumed to be 100 percent CO2 and may be 
sent directly for cooling and compression. Other sources [30] have referenced the presence of 
water in the fermentation CO2 stream. This is a possibility; however, water knockout drums 
would be present in the CO2 compression train and, thus, further purification before processing 
would be unnecessary. 
5.3.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the ethanol process for 
the purpose of this study: 
• The base plant is representative of an ethanol plant producing 50 M gallons of 
ethanol/year 
• The plant uses the dry-mill process with corn as the feedstock 
• The fermentation off-gas, assumed to be 100 percent CO2, is the only high purity point 
source considered  
• The CO2 generated at 100 percent CF is 143,042 tonnes CO2/year  
• The CO2 temperature is 320°F 
• The CO2 pressure is 17.4 psia

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
53 
• The end product CO2 quality is based on the EOR pipeline standard as mentioned in the 
NETL QGESS for CO2 Impurity Design Parameters [1] 
5.3.4 CO2 Capture System 
Exhibit 5-20 [36] is a map provided by the U.S. Department of Agriculture (USDA) showing the 
production of corn by county in comparison to the location of U.S. ethanol plants, as of March 
2012. As expected, the ethanol plants are mostly located near areas of high corn production, 
namely the Midwest states. The highest density of ethanol plants occurs in Illinois, Iowa, 
Minnesota, and Nebraska.   
Exhibit 5-20. U.S. ethanol plant locations 
 
 
Source: USDA [36]

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
54 
The trend for the ethanol industry is smaller plants, which in turn produce smaller CO2 streams 
and require compression equipment capable of handling smaller flows. This requirement is 
satisfied by using reciprocating compression discussed in Section 4.1.1; however, an alternative 
to smaller equipment could be to combine the emissions streams from multiple nearby plants 
for a single, larger compressor to compress the aggregate CO2 for EOR use. Such a scenario is 
not considered in the scope of this study but could be evaluated in future work as described in 
Section 9.2. 
5.3.5 BFD, Stream Table, and Performance Summary 
Since the fermentation process releases 100 percent pure CO2, only cooling and compression is 
required for the CO2 stream to be sent directly for EOR or other usage.  As shown in Exhibit 
5-21, the fermentation vent is cooled through a HX, compressed (with interstage cooling and 
after-cooling) to meet EOR pipeline specifications for pressure and temperature. Exhibit 5-22 
provides the stream table.  
Exhibit 5-21. Ethanol CO2 capture BFD 
 
Exhibit 5-22. Ethanol stream table 
  1 2 3 
V-L Mole Fraction       
AR 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 
CO2 1.0000 1.0000 1.0000 
SO2 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 
H2O 0.0000 0.0000 0.0000 
H2S 0.0000 0.0000 0.0000 
N2 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 
        
V-L Flowrate (kgmol/hr) 371 371 371 
V-L Flowrate (kg/hr) 16,329 16,329 16,329 
Temperature (°C) 160 27 30 
Pressure (MPa, abs) 0.12 0.1 15.3 
Steam Table Enthalpy (kJ/kg)A 8,762 8,759 8,753 
Aspen Plus Enthalpy (kJ/kg)B -8,819 -8,941 -9,193 
Ethanol 
Plant HX Compressor Desired Usage1 2 3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
55 
  1 2 3 
V-L Mole Fraction       
Density (kg/m3) 1.5 2.0 629 
    
V-L Molecular Weight 44.0 44.0 44.0 
V-L Flowrate (lbmol/hr) 818 818 818 
V-L Flowrate (lb/hr) 36,000 36,000 36,000 
Temperature (°F) 320 80 86 
Pressure (psia) 17.4 16.4 2,214.7 
Steam Table Enthalpy (Btu/lb)A 3,767 3,766 3,763 
Aspen Plus Enthalpy (Btu/lb)B -3,791 -3,844 -3,953 
Density (lb/ft3) 0.092 0.125 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance results are based on compressor quotes discussed in Section 4.1.1 and scaled 
auxiliary loads for the cooling water system as discussed in Section 4.4. The performance 
summary is provided in Exhibit 5-23.  
Exhibit 5-23. Performance summary 
Performance Summary 
Item 50 M Gal Ethanol/year (kWe) 
CO2 Compressor 1,810 
Circulating Water Pumps 20 
Cooling Tower Fans 10 
Total Auxiliary Load 1,840 
5.3.6 Capture Integration 
The fermentation process occurs at a temperature of 140–180°C (284–356°F). Any cooling water 
system from the retrofit could be integrated into the existing plant’s cooling water system; 
however, depending on the size of the existing cooling water system and the design cooling 
temperature range, it might be more economical to install a stand-alone cooling system rather 
than increase the existing cooling system. For the purposes of this study, it is assumed that an 
additional, stand-alone cooling water unit will perform the necessary cooling for capture and 
compression since integration with the base plant is outside the scope of this report. However, 
there is a potential for integration of make-up water to be used to feed or partially feed the 
cooling unit, thereby reducing the unit’s size; there is also the potential that the heat removed 
from compression could be recycled within the plant to produce dried distiller grain solids. This 
product is produced by drying the solids that remain after fermentation. Heat for dried distiller 
grain solids drying is generally provided by NG.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
56 
5.3.7 Power Source 
Given the relatively small amount of CO2, the compression power consumption is 1.81 MW.  
Power consumption estimates for the cooling system were scaled as described in Section 4.4. 
The total power requirement was calculated to be 1.85 MW , which includes all power required 
by the compression train and the cooling water system. Purchased power cost is estimated at a 
rate of $60/MWh as discussed in Section 3.1.2.4. 
5.3.8 Economic Analysis Results 
The economic results for CO2 capture application in an ethanol plant are presented in this 
section. Owner’s costs (Exhibit 5-24), capital costs (Exhibit 5-25), and O&M costs are calculated 
as discussed in Section 3.1. Retrofit costs were determined by applying a retrofit factor to TPC 
as discussed in Section 3.3. The greenfield TOC for the ethanol case is $24.7 M. The 
corresponding greenfield COC is $31.8/tonne CO2, and the COC is $32.0/tonne CO2 in retrofit 
applications. 
Exhibit 5-24. Owner’s costs for ethanol greenfield site  
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $355 $2 
1-Month Maintenance Materials $19 $0 
1-Month Non-Fuel Consumables $2 $0 
1-Month Waste Disposal $0 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 
2% of TPC $404 $3 
Total $779 $5 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $2 $0 
0.5% of TPC (spare parts) $101 $1 
Total $103 $1 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $3,028 $21 
Financing Costs $545 $4 
TOC $24,672 $172 
TASC Multiplier (Ethanol, 31 year) 1.047  
TASC $25,840 $181

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
57 
Exhibit 5-25. Capital costs for ethanol greenfield site 
Case: Ethanol Estimate Type:  Conceptual 
Representative Plant Size:  50 M gallons ethanol/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.1 Inlet Cooler for Compression Train $63 $0 $13 $0 $76 $13 $0 $18 $107 $1 
5.4 CO2 Compression & Drying $3,053 $458 $1,021 $0 $4,532 $793 $0 $1,065 $6,390 $45 
5.5 CO2 Compressor Aftercooler w/5.4 w/5.4 w/5.4 w/5.4 $0 $0 $0 $0 $0 $0 
 Subtotal $3,116 $458 $1,034 $0 $4,608 $806 $0 $1,083 $6,497 $45 
 7 Ductwork & Stack 
7.3 Ductwork $0 $112 $78 $0 $190 $33 $0 $45 $268 $2 
 Subtotal $0 $112 $78 $0 $190 $33 $0 $45 $268 $2 
 9 Cooling Water System 
9.1 Cooling Towers $75 $0 $23 $0 $99 $17 $0 $23 $139 $1 
9.2 Circulating Water Pumps $5 $0 $0 $0 $6 $1 $0 $1 $8 $0 
9.3 Circulating Water System Aux. $171 $0 $23 $0 $193 $34 $0 $45 $273 $2 
9.4 Circulating Water Piping $0 $79 $71 $0 $150 $26 $0 $35 $212 $1 
9.5 Make-up Water System $32 $0 $41 $0 $73 $13 $0 $17 $102 $1 
9.6 Component Cooling Water System $12 $0 $9 $0 $22 $4 $0 $5 $31 $0 
9.7 Circulating Water System Foundations $0 $11 $18 $0 $28 $5 $0 $7 $40 $0 
 Subtotal $296 $90 $186 $0 $571 $100 $0 $134 $805 $6 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,049 $0 $90 $0 $1,139 $199 $0 $268 $1,606 $11 
11.3 Switchgear & Motor Control  $1,629 $0 $283 $0 $1,912 $335 $0 $449 $2,695 $19 
11.4 Conduit & Cable Tray $0 $212 $610 $0 $822 $144 $0 $193 $1,159 $8 
11.5 Wire & Cable $0 $561 $1,002 $0 $1,563 $274 $0 $367 $2,204 $15 
 Subtotal $2,678 $773 $1,985 $0 $5,436 $951 $0 $1,277 $7,665 $54 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $304 $243 $972 $0 $1,519 $266 $0 $357 $2,142 $15 
12.9 Other I&C Equipment $373 $0 $865 $0 $1,238 $217 $0 $291 $1,746 $12 
 Subtotal $677 $243 $1,837 $0 $2,757 $482 $0 $648 $3,887 $27 
 13 Improvements to Site 
13.1 Site Preparation $0 $17 $349 $0 $366 $64 $0 $86 $516 $4 
13.2 Site Improvements $0 $81 $108 $0 $189 $33 $0 $44 $267 $2 
13.3 Site Facilities $93 $0 $98 $0 $191 $33 $0 $45 $269 $2 
 Subtotal $93 $99 $554 $0 $746 $131 $0 $175 $1,052 $7 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $5 $4 $0 $9 $2 $0 $2 $13 $0 
 Subtotal $0 $5 $4 $0 $9 $2 $0 $2 $13 $0 
 Total $6,860 $1,779 $5,678 $0 $14,317 $2,505 $0 $3,364 $20,187 $141

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
58 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-26, while Exhibit 5-27 shows the COC for greenfield and retrofit sites for the representative 
ethanol plant.  
Exhibit 5-26. Initial and annual O&M costs for ethanol greenfield site 
Case:  Ethanol  Cost Base: Dec 2018 
Representative Plant Size:  50 M gallons ethanol/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $3.07 
Maintenance Labor:     $129,194 $0.90 
Administrative & Support Labor:     $141,908 $0.99 
Property Taxes and Insurance:     $403,732 $2.82 
Total:     $1,113,272 $7.78 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $193,791 $1.59 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 17 $1.90 $0 $9,946 $0.08 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 0.1 $550.00 $0 $8,577 $0.07 
Subtotal:    $0 $18,523 $0.15 
Variable Operating Costs Total:    $0 $212,314 $1.75 
Exhibit 5-27. COC for 50 M gallons/year ethanol greenfield and retrofit  
Component Greenfield Value, $/tonne CO2 Retrofit Value, $/tonne CO2 
Capital 14.1 14.2 
Fixed 9.2 9.2 
Variable 1.7 1.8 
Purchased Power 6.8 6.8 
Total COC 31.8 32.0

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
59 
5.3.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to ethanol plant capacity is shown in Exhibit 
5-28. As the plant capacity increases, more CO2 is available for capture, thus realizing economies 
of scale. This generic scaling exercise assumes that equipment is available at continuous 
capacities; however, equipment is often manufactured in discrete sizes, which would possibly 
affect the advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 5-28. Ethanol plant capacity sensitivity  
 
Note: The data point for the COC at a 50 M gallon/year ethanol plant does not fall directly on the COC line due to data point 
increments and plot formatting. 
5.3.10 Ethanol Conclusion 
The high purity CO2 stream produced in an ethanol plant makes them relatively low-cost 
industrial processes for CO2 capture since they require no costly separation equipment. A CO2 
compression system for a 50 M gallons/year ethanol plant was modeled to estimate the COC of 
capturing CO2 from the fermenter. The results showed the COC of CO2 to be $31.8/tonne CO2 
for a greenfield site and $32.0/tonne CO2 for a retrofit site. The small disparities between 
greenfield and retrofit cases are the result of unknown difficulties required for a retrofit 
installation versus a greenfield application, assuming adequate plot plan space for the retrofit 
case exists.  
The plant size sensitivity showed that as plant size decreased from 415 M gallons/year to 30 M 
gal/year, the COC increased by $20.1/tonne CO2. As the plant size is decreased, less CO2 is 
produced, and economies of scale are lost, resulting in a higher COC. Though outside of this 
study’s scope, literature discusses food-grade CO2 capture for potential use instead of EOR. This

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
60 
might be a more economical option, but further evaluation would be required to determine an 
applicable COC for this alternate CO2 end-use. 
5.4 NATURAL GAS PROCESSING 
Natural gas processing is considered a high purity industrial process with a CO2 discharge stream 
composition of 96–99 percent. Since in many applications CO2 removal is inherently necessary 
to the processing of natural gas, NGP presents a potentially low-cost source of industrial CO2 
capture. 
5.4.1 Size Range 
For the purposes of this study, it is assumed that the reference plant has a capacity of 330 
MMSCFD at 100 percent capacity. The composition of the raw gas processed is represented by 
that of a formation in the Michigan Basin producing formation with 10.2 percent CO2. [37] The 
full raw gas characteristics are given in Exhibit 5-29, and represent average concentrations of 
the gas produced in the referenced formation. Given this plant capacity and the raw natural gas 
CO2 composition, this plant would generate approximately 649,255 tonnes CO2/year at 100 
percent CF.h 
Exhibit 5-29. Michigan basin producing formation raw gas characteristics  
Michigan Basin Raw Gas Characteristics 
Component Average Mole % 
CH4 82.4 
C2H6 2.48 
C3H8 0.37 
n-Butane 0.00 
i-Butane 0.00 
n-Pentane 0.00 
i-Pentane 0.00 
c-Pentane 0.00 
Hexanes 0.00 
H2S 0.00 
CO2 10.2 
N2 2.23 
He 0.00 
Other 2.32 
 
 
h The assumptions for this study’s reference plant are not limited to the Michigan Basin. High CO2 content coupled with 
large capacity processing plants may also be found in the Gulf Coast region, the Williston Basin, and the Midwest region, 
referred to as the Foreland Province, according to the Gas Technology Institute database. [37]

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
61 
5.4.2 CO2 Point Sources 
Natural gas processing (or gas sweetening) takes raw NG containing 2–70 percent CO2 by 
volume and removes CO2 and other impurities to meet the required pipeline or liquefaction 
specifications. The single point source is the CO2 stream from the AGR system, which is 
generally vented to the atmosphere. The variation in raw natural gas CO2 content would affect 
the amount of CO2 available for capture; however, the concentration of the CO2 stream to be 
captured is high, 96–99 percent.  
5.4.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the natural gas 
processing plant for the purpose of this study: 
• The representative NGP plant has a capacity of 330 MMSCFD of raw gas processed 
• The raw gas CO2 content is 10.2 mole percent 
• The CO2 generated at 100 percent CF is 649,255 tonnes CO2/year  
• The CO2 stream temperature is 69°F 
• The CO2 stream pressure is 23.52 psia 
• The CO2 stream is 99 percent CO2 by volume, balanced with water 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1] 
5.4.4 CO2 Capture System 
Only compression, glycol dehydration, and associated cooling is required for this NGP case. 
Given the amount of CO2 available for capture, a centrifugal compressor, discussed in Section 
4.1.2, is used to attain 2,200 psig EOR pipeline pressure per QGESS specifications. [1] 
5.4.5 BFD, Stream Table, and Performance Summary 
Since the stripping column releases 99 volume percent CO2, only compression with glycol 
dehydration and cooling is required. Water knockout is used in the compression train to avoid 
liquid entering the compressors. There is no cooling of the inlet stream required, as it is 
assumed that the overhead condenser of the stripping column in the base plant discharges at a 
temperature of 69°F. After compression, the CO2 product stream is cooled to 120°F and sent 
directly for EOR or other usage. Exhibit 5-30 gives the BFD for this process. Exhibit 5-31 provides 
the stream table. 
Exhibit 5-30. NGP CO2 capture BFD 
 
Natural Gas 
Processing 
Plant
HX Desired Usage1 Compressor 2 3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
62 
Exhibit 5-31. NGP stream table 
  1 2 3 
V-L Mole Fraction       
AR 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 
CO2 0.9900 0.9995 0.9995 
SO2 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 
H2O 0.0100 0.0005 0.0005 
H2S 0.0000 0.0000 0.0000 
N2 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 
  
   
V-L Flowrate (kgmol/hr) 1,701 1,684 1,684 
V-L Flowrate (kg/hr) 74,416 74,109 74,109 
Temperature (°C) 21 83 30 
Pressure (MPa, abs) 0.16 15.3 15.3 
Steam Table Enthalpy (kJ/kg)A 8,787 8,758 8,755 
Aspen Plus Enthalpy (kJ/kg)B -8,965 -9,034 -9,195 
Density (kg/m3) 2.9 416 630 
V-L Molecular Weight 43.8 44.0 44.0 
    
V-L Flowrate (lbmol/hr) 3,750 3,713 3,713 
V-L Flowrate (lb/hr) 164,059 163,382 163,382 
Temperature (°F) 69 182 86 
Pressure (psia) 23.5 2,216.9 2,214.7 
Steam Table Enthalpy (Btu/lb)A 3,778 3,765 3,764 
Aspen Plus Enthalpy (Btu/lb)B -3,854 -3,884 -3,953 
Density (lb/ft3) 0.183 25.9 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance results are based on the centrifugal compressor discussed in Section 4.1.2 and 
scaled auxiliary loads for the cooling water system as discussed in Section 4.4. The performance 
summary is provided in Exhibit 5-32.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
63 
Exhibit 5-32. Performance summary 
Performance Summary 
Item 330 MMSCFD (kWe) 
CO2 Compressor 6,010 
Circulating Water Pumps 70 
Cooling Tower Fans 40 
Total Auxiliary Load 6,120 
5.4.6 Capture Integration 
In this instance, the capture system is inherent to the base plant design, under the assumption 
that the raw gas CO2 content is above that of pipeline specifications. Therefore, there is little 
opportunity for capture integration other than the necessary cooling for compression. Since the 
base plant is considered outside the scope of this study, a standalone cooling water system is 
assumed to provide the necessary intercooling for the compression process. However, in real 
applications, the necessity for a standalone cooling water system would need to be evaluated 
on a case-by-case basis. There could be potential to integrate make-up water to feed or partially 
feed the cooling system, thereby reducing the unit’s size, or replacing it completely with a 
simple HX. 
5.4.7 Power Source 
The compressor power consumption for this case is 6.01 MW. Power consumption estimates for 
the cooling water system were scaled as described in Section 4.4. The total power requirement 
was calculated to be 6.12 MW , which includes all power required by the compression train and 
the cooling water system. Purchased power cost is estimated at a rate of $60/MWh as discussed 
in Section 3.1.2.4. For practical applications for this type of facility with NG readily available, the 
power required to operate the cooling water system as well as the compression system could be 
generated on site. Depending on the size and location of the facility there could be other co-
beneficial reasons to produce the required power on-site. This scenario would need to be 
evaluated on a case-by-case basis and is outside of the scope of this study. 
5.4.8 Economic Analysis Results 
The economic results for CO2 capture application in an NGP plant are presented in this section. 
Owner’s costs (Exhibit 5-33), capital costs (Exhibit 5-34), and O&M costs are calculated as 
discussed in Section 3.1. Retrofit costs were determined by applying a retrofit factor to TPC as 
discussed in Section 3.3. The greenfield TOC for the NGP case is $56.8 M. The corresponding 
greenfield COC is $16.1/tonne CO2, and the COC is $16.2/tonne CO2 in retrofit applications.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
64 
Exhibit 5-33. Owner’s costs for NGP greenfield site 
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $461 $1 
1-Month Maintenance Materials $44 $0 
1-Month Non-Fuel Consumables $37 $0 
1-Month Waste Disposal $2 $0 
25% of 1 Months Fuel Cost at 100% CF $0 $0 
2% of TPC $934 $1 
Total $1,477 $2 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $68 $0 
0.5% of TPC (spare parts) $233 $0 
Total $302 $0 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $7,004 $11 
Financing Costs $1,261 $2 
TOC $56,764 $87 
TASC Multiplier (NGP, 31 year) 1.039  
TASC $58,977 $91

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
65 
Exhibit 5-34. Capital and costs for NGP greenfield site 
Case: Natural Gas Processing Estimate Type:  Conceptual 
Representative Plant Size:  330 MMSCFD natural gas Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.4 CO2 Compression & Drying $12,229 $1,834 $4,089 $0 $18,152 $3,177 $0 $4,266 $25,594 $39 
5.5 CO2 Compressor Aftercooler $86 $14 $37 $0 $136 $24 $0 $32 $192 $0 
 Subtotal $12,315 $1,848 $4,126 $0 $18,288 $3,200 $0 $4,298 $25,787 $40 
 7 Ductwork & Stack 
7.3 Ductwork $0 $200 $139 $0 $339 $59 $0 $80 $478 $1 
 Subtotal $0 $200 $139 $0 $339 $59 $0 $80 $478 $1 
 9 Cooling Water System 
9.1 Cooling Towers $183 $0 $57 $0 $239 $42 $0 $56 $338 $1 
9.2 Circulating Water Pumps $15 $0 $1 $0 $16 $3 $0 $4 $22 $0 
9.3 Circulating Water System Aux. $353 $0 $47 $0 $400 $70 $0 $94 $564 $1 
9.4 Circulating Water Piping $0 $163 $148 $0 $311 $54 $0 $73 $439 $1 
9.5 Make-up Water System $56 $0 $72 $0 $128 $22 $0 $30 $180 $0 
9.6 Component Cooling Water System $25 $0 $20 $0 $45 $8 $0 $11 $63 $0 
9.7 Circulating Water System Foundations $0 $21 $34 $0 $55 $10 $0 $13 $77 $0 
 Subtotal $632 $184 $378 $0 $1,194 $209 $0 $281 $1,683 $3 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,757 $0 $151 $0 $1,908 $334 $0 $448 $2,690 $4 
11.3 Switchgear & Motor Control  $2,728 $0 $473 $0 $3,201 $560 $0 $752 $4,514 $7 
11.4 Conduit & Cable Tray $0 $355 $1,022 $0 $1,377 $241 $0 $324 $1,941 $3 
11.5 Wire & Cable $0 $939 $1,679 $0 $2,618 $458 $0 $615 $3,691 $6 
 Subtotal $4,485 $1,294 $3,325 $0 $9,104 $1,593 $0 $2,139 $12,837 $20 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $355 $284 $1,136 $0 $1,775 $311 $0 $417 $2,503 $4 
12.9 Other I&C Equipment $436 $0 $1,011 $0 $1,447 $253 $0 $340 $2,040 $3 
 Subtotal $791 $284 $2,147 $0 $3,222 $564 $0 $757 $4,543 $7 
 13 Improvements to Site 
13.1 Site Preparation $0 $22 $443 $0 $465 $81 $0 $109 $656 $1 
13.2 Site Improvements $0 $103 $137 $0 $240 $42 $0 $56 $339 $1 
13.3 Site Facilities $118 $0 $124 $0 $242 $42 $0 $57 $342 $1 
 Subtotal $118 $125 $704 $0 $948 $166 $0 $223 $1,337 $2 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $10 $8 $0 $18 $3 $0 $4 $26 $0 
 Subtotal $0 $10 $8 $0 $18 $3 $0 $4 $26 $0 
 Total $18,342 $3,945 $10,826 $0 $33,114 $5,795 $0 $7,782 $46,690 $72

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
66 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-35, while Exhibit 5-36 shows the COC for greenfield and retrofit sites for the representative 
NGP plant. 
Exhibit 5-35. Initial and annual O&M costs for NGP greenfield site 
Case:  Natural Gas Processing Cost Base: Dec 2018 
Representative Plant Size:  330 MMSCFD natural gas  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $0.68 
Maintenance Labor:     $298,819 $0.46 
Administrative & Support Labor:     $184,314 $0.28 
Property Taxes and Insurance:     $933,808 $1.44 
Total:     $1,855,379 $2.86 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $448,228 $0.81 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 53 $1.90 $0 $31,518 $0.06 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 0.2 $550.00 $0 $27,728 $0.05 
Triethylene Glycol (gal): w/equip. 152 $6.80 $0 $321,580 $0.58 
Subtotal:    $0 $380,826 $0.69 
Waste Disposal 
Triethylene Glycol (gal):  152 $0.35 $0 $16,552 $0.03 
Subtotal:    $0 $16,552 $0.03 
Variable Operating Costs Total:    $0 $845,606 $1.53 
Exhibit 5-36. COC for 330 MMSCFD NGP greenfield and retrofit 
Component Greenfield Value, $/tonne CO2 Retrofit Value, $/tonne CO2 
Capital 6.2 6.3 
Fixed 3.4 3.4 
Variable 1.5 1.5 
Purchased Power 5.0 5.0 
Total COC of CO2 16.1 16.2

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
67 
5.4.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to NGP plant capacity is shown in Exhibit 5-37. As 
the plant capacity increases, more CO2 is available for capture, thus realizing economies of 
scale. This generic scaling exercise assumes that equipment is available at continuous capacities; 
however, equipment is often manufactured in discrete sizes, which would possibly affect the 
advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 5-37. NGP plant capacity sensitivity 
 
5.4.10 Natural Gas Processing Conclusion 
The high purity CO2 stream produced from NGP plants makes them a relatively low-cost 
industrial process since CO2 separation is inherent to normal operations. A CO2 compression 
system for a 330 MMSCFD NGP plant was modeled to estimate the COC of capturing CO2 from 
the plant’s existing AGR. The results showed the COC of CO2 to be $16.1/tonne CO2 for a 
greenfield site and $16.2/tonne CO2 for a retrofit site. The small disparities between greenfield 
and retrofit cases are the result of unknown difficulties required for a retrofit installation versus 
a greenfield application, assuming adequate plot plan space for the retrofit case exists.   
The plant size sensitivity, based on the design basis assumptions in this study, showed that as 
plant size decreased from 1,250 MMSCFD to 50 MMSCFD, the COC increased by $16.7/tonne 
CO2. With decreasing plant size, less CO2 is produced, and economies of scale are lost, resulting 
in a higher COC.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
68 
5.5 COAL-TO-LIQUIDS 
Economic and national security concerns related to liquid fuels have revived national interest in 
alternative liquid fuel sources. Coal-to-Fischer-Tropsch fuels production emerged as a major 
technology option for many states and the DOE. The 2014 NETL report “Baseline Technical and 
Economic Assessment of a Commercial Scale Fischer-Tropsch Liquids Facility” (“CTL Study”) [38] 
examined the technical and economic feasibility of a commercial 50,000 barrels per day (BPD) 
CTL facility. The facility employs gasification and Fischer-Tropsch (FT) technology to produce 
commercial-grade diesel and naptha liquids from medium-sulfur bituminous coal. The basis for 
the CTL case in this report is that of the CO2 sequestration case evaluated in the CTL Study. 
5.5.1 Size Range 
The CTL Study focuses on a 50,000 BPD CTL production facility, and this is the plant capacity 
assumed for this study to allow for comparisons across NETL reports. With the given capacity, 
the CTL facility will produce 8,743,312 tonnes/year of CO2 at 100 percent CF. The CTL study also 
considers power production, where the gas turbine and steam turbine produce power in excess 
of what base plant operations would require, and this excess 4.7 MW was exported to the grid. 
This reported excess power is on a net basis and does include auxiliary loads for CO2 
compressors. For the purposes of this study, all power requirements are met with power 
purchased from the grid; however, in some cases the base plant will have excess power 
available to meet compression and cooling power requirements, as is the case in the CTL study.  
5.5.2 CO2 Point Sources 
Within the CTL facility there are two main point sources of CO2 emissions; the AGR unit in the 
gasification section and the FT amine AGR unit in the FT section. The gasification section AGR 
generates CO2 at two pressures: 160 psia and 300 psia. The FT amine AGR generates CO2 at 265 
psia. These three streams are compressed in one compression train, with the higher-pressure 
streams added to the train between the appropriate compression stages. The CO2 product 
stream has a purity of 100 percent CO2. 
5.5.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the CTL process for the 
purpose of this study: 
• The representative CTL facility has a production capacity of 50,000 BPD 
• The CO2 generated is 8,743,312 tonnes CO2/year at 100 percent CF  
• The CO2 stream is 100 percent CO2 
• Due to 100 percent purity, only compression and cooling are required 
• The CO2 stream pressures are 160, 265, and 300 psia 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1]

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
69 
5.5.4 CO2 Capture System 
The CTL Study considers cases with CO2 compression for EOR export and, therefore, the base 
plant acts as the separation process. The specific AGR units used in the CTL Study discharge CO2 
at multiple pressures and, therefore, the compression trains used are configured specifically to 
handle these compression requirements. Of the vendor quotes discussed in Section 4.1, there is 
not a compression train quote that accounts for multiple inlet CO2 streams at multiple 
pressures. Therefore, the cost and performance specified in the NETL CTL Study are used here. 
This requires approximation of the amount of cooling water necessary for interstage cooling. 
[38] 
It should be noted that in the CTL Study, after the CO2 streams are combined, a portion is 
removed and sent back to the gasifier. For the purposes of this study, this stream is not 
considered, and all calculations are based on the reported mass flow of the product CO2 stream 
(at 2,200 psig) given in the CTL Study. [38] 
5.5.5 BFD, Stream Table, and Performance Summary 
Since the CTL process releases 100 percent pure CO2, only cooling and compression is required 
for the CO2 stream to be sent directly for EOR or other usage. The compression train used 
discharges the product CO2 at 2,200 psig and 121°F and, therefore, after-cooling is required. 
Exhibit 5-38 gives the BFD for this process, and Exhibit 5-39 provides the stream table.  
Exhibit 5-38. CTL CO2 capture BFD 
 
Exhibit 5-39. CTL stream table 
  1 2 3 4 5 
V-L Mole Fraction        
AR 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 1.0000 1.0000 1.0000 1.0000 1.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0000 0.0000 0.0000 0.0000 0.0000 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.0000 0.0000 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 1.0000 1.0000

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
70 
  1 2 3 4 5 
V-L Mole Fraction        
V-L Flowrate (kgmol/hr) 13,449 7,384 1,846 22,679 22,679 
V-L Flowrate (kg/hr) 91,870 324,980 81,245 498,095 498,095 
Temperature (°C) 38 16 16 49 30 
Pressure (MPa, abs) 1.8 1.1 2.1 15.3 15.3 
Steam Table Enthalpy (kJ/kg)A 8,759 8,759 8,758 8,755 8,753 
Aspen Plus Enthalpy (kJ/kg)B -8,948 -8,961 -8,972 -9,132 -9,188 
Density (kg/m3) 34.2 21.7 43.8 668.2 628.8 
V-L Molecular Weight 44.01 44.01 44.01 44.01 44.01 
      
V-L Flowrate (lbmol/hr) 29,649 16,280 4,070 49,998 49,998 
V-L Flowrate (lb/hr) 1,304,851 716,458 179,114 2,200,423 2,200,423 
Temperature (°F) 100 60 60 121 86 
Pressure (psia) 265.0 160.0 300.0 2,214.7 2,214.7 
Steam Table Enthalpy 
(Btu/lb)A 
3,766 3,766 3,765 3,764 3,763 
Aspen Plus Enthalpy (Btu/lb)B -3,847 -3,852 -3,857 -3,926 -3,950 
Density (lb/ft3) 2.14 1.36 2.74 41.7 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance results are taken from the CTL Study sequestration case that considered CO2 
capture. The performance summary is provided in Exhibit 5-40. 
Exhibit 5-40. Performance summary 
Performance Summary 
Item 50,000 BPD (kWe) 
CO2 Compressor 43,480 
Circulating Water Pumps 100 
Cooling Tower Fans 50 
Total Auxiliary Load 43,630 
5.5.6 Capture Integration 
For the purposes of this study, it is assumed that an additional, stand-alone cooling water 
system will perform the necessary cooling for capture and compression. No retrofit case is 
considered for CTL as any new builds would most likely include cooling. However, to make this 
case comparable to the other cases considered in this study, the cost for cooling must be 
included in the greenfield COC. Therefore, a stand-alone cooling system is included.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
71 
5.5.7 Power Source 
The auxiliary power required for this case is 43.6 MW.  The total power requirement was 
approximated to include all power required by the compression train and the cooling water 
system. Power requirement estimates for the cooling water system were scaled as described in 
Section 4.4. Purchased power costs are estimated at a rate of $60/MWh as discussed in Section 
3.1.2.4. However, for practical applications for this type of facility with power produced on-site 
and excess power sent to the grid, the power requirements may be met with power generated 
on-site. For instance, while the CTL Study sequestration case has excess power that would be 
able to satisfy a portion of this study’s power requirement, this scenario should be evaluated on 
a case-by-case basis, which is not included in the scope of this report. 
5.5.8 Economic Analysis Results 
The economic results for CO2 capture application in a CTL plant are presented in this section. 
Owner’s costs (Exhibit 5-41), capital costs (Exhibit 5-42), and O&M costs are calculated as 
discussed in Section 3.1. The greenfield TOC for the CTL case is $196.9 M. The corresponding 
greenfield COC is $5.6/tonne CO2.  
Exhibit 5-41. Owner’s costs for CTL greenfield site 
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $925 $0 
1-Month Maintenance Materials $153 $0 
1-Month Non-Fuel Consumables $42 $0 
1-Month Waste Disposal $0 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 
2% of TPC $3,257 $0 
Total $4,377 $1 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $39 $0 
0.5% of TPC (spare parts) $814 $0 
Total $853 $0 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $24,426 $3 
Financing Costs $4,397 $1 
TOC $196,924 $23 
TASC Multiplier (CTL, 31 year) 1.054  
TASC $207,583 $24

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
72 
Exhibit 5-42. Capital costs for CTL greenfield site 
Case: CTL Estimate Type:  Conceptual 
Representative Plant Size:  50,000 BPD Fischer-Tropsch liquids Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.4 CO2 Compression & Drying $59,197 $0 $20,070 $0 $79,267 $13,872 $0 $18,628 $111,766 $13 
5.5 CO2 Compressor Aftercooler $310 $49 $133 $0 $492 $86 $0 $116 $694 $0 
 Subtotal $59,507 $49 $20,203 $0 $79,759 $13,958 $0 $18,743 $112,461 $13 
 7 Ductwork & Stack 
7.3 Ductwork $0 $246 $171 $0 $417 $73 $0 $98 $588 $0 
 Subtotal $0 $246 $171 $0 $417 $73 $0 $98 $588 $0 
 9 Cooling Water System 
9.1 Cooling Towers $839 $0 $661 $0 $1,501 $263 $0 $353 $2,116 $0 
9.2 Circulating Water Pumps $233 $0 $17 $0 $250 $44 $0 $59 $352 $0 
9.3 Circulating Water System Aux. $2,663 $0 $351 $0 $3,014 $527 $0 $708 $4,250 $0 
9.4 Circulating Water Piping $0 $1,231 $1,115 $0 $2,346 $410 $0 $551 $3,307 $0 
9.5 Make-up Water System $307 $0 $394 $0 $701 $123 $0 $165 $988 $0 
9.6 Component Cooling Water System $192 $0 $147 $0 $339 $59 $0 $80 $478 $0 
9.7 Circulating Water System 
Foundations 
$0 $132 $220 $0 $352 $62 $0 $83 $497 $0 
 Subtotal $4,233 $1,363 $2,905 $0 $8,502 $1,488 $0 $1,998 $11,988 $1 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $4,090 $0 $351 $0 $4,441 $777 $0 $1,044 $6,261 $1 
11.3 Switchgear & Motor Control  $6,349 $0 $1,102 $0 $7,450 $1,304 $0 $1,751 $10,505 $1 
11.4 Conduit & Cable Tray $0 $825 $2,378 $0 $3,204 $561 $0 $753 $4,517 $1 
11.5 Wire & Cable $0 $2,186 $3,907 $0 $6,093 $1,066 $0 $1,432 $8,591 $1 
 Subtotal $10,439 $3,011 $7,738 $0 $21,188 $3,708 $0 $4,979 $29,874 $3 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $458 $367 $1,467 $0 $2,292 $401 $0 $539 $3,231 $0 
12.9 Other I&C Equipment $563 $0 $1,305 $0 $1,868 $327 $0 $439 $2,634 $0 
 Subtotal $1,022 $367 $2,771 $0 $4,160 $728 $0 $977 $5,865 $1 
 13 Improvements to Site 
13.1 Site Preparation $0 $33 $657 $0 $689 $121 $0 $162 $972 $0 
13.2 Site Improvements $0 $153 $203 $0 $356 $62 $0 $84 $502 $0 
13.3 Site Facilities $175 $0 $184 $0 $359 $63 $0 $84 $506 $0 
 Subtotal $175 $186 $1,043 $0 $1,404 $246 $0 $330 $1,980 $0 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $33 $26 $0 $60 $10 $0 $14 $84 $0 
 Subtotal $0 $33 $26 $0 $60 $10 $0 $14 $84 $0 
 Total $75,376 $5,255 $34,858 $0 $115,490 $20,211 $0 $27,140 $162,840 $19

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
73 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-43, while Exhibit 5-44 shows the COC for a greenfield site for the representative CTL plant. 
Exhibit 5-43. Initial and annual O&M costs for CTL greenfield site 
Case:  Coal-to-Liquids Cost Base: Dec 2018 
Representative Plant Size:  50,000 BPD Fischer-Tropsch liquids  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $0.05 
Maintenance Labor:     $1,042,178 $0.12 
Administrative & Support Labor:     $370,154 $0.04 
Property Taxes and Insurance:     $3,256,808 $0.37 
Total:     $5,107,578 $0.58 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $1,563,268 $0.21 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 387 $1.90 $0 $228,019 $0.03 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 1.2 $550.00 $0 $200,179 $0.03 
Subtotal:    $0 $428,198 $0.06 
Variable Operating Costs Total:    $0 $1,991,465 $0.27 
 Exhibit 5-44. COC for 50,000 BPD CTL greenfield 
Component Greenfield Value, $/tonne CO2 
Capital 2.0 
Fixed 0.7 
Variable 0.3 
Purchased Power 2.6 
Total COC 5.6

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
74 
5.5.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to CTL plant capacity is shown in Exhibit 5-45. As 
the plant capacity increases, more CO2 is available for capture, thus realizing economies of 
scale. This generic scaling exercise assumes that equipment is available at continuous capacities; 
however, equipment is often manufactured in discrete sizes, which would possibly affect the 
advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 5-45. CTL plant capacity sensitivity 
 
5.5.10 Coal-to-Liquids Conclusion 
The high purity CO2 streams produced from CTL plants makes them a relatively low-cost 
industrial process since the plant performs the CO2 separation as a part of normal operations. A 
CO2 compression system for a 50,000 BPD plant was modeled to estimate the COC of capturing 
CO2 from the process. The results showed the COC of CO2 to be $5.6/tonne CO2 for a greenfield 
site. The plant size sensitivity showed that as plant size decreased from 100,000 to 10,000 BPD, 
the COC increased by $2.7/tonne CO2. As the plant size is decreased, less CO2 is produced, and 
economies of scale are lost, resulting in a higher COC. 
5.6 GAS-TO-LIQUIDS 
Domestic FT GTL technology provides an alternative option for use of U.S. increasing supply of 
domestic NG. As with CTL, GTL can create a significant economic value while increasing the 
country’s energy security. In their report “Analysis of Natural Gas-to Liquid Transportation Fuels 
via Fischer-Tropsch” [39] (“GTL Study”) published in 2013, NETL evaluated the cost and 
performance of a 50,000 BPD FT liquids GTL facility. Of the total liquids production, 30 percent is 
allocated for finished motor gasoline, and 70 percent results in low-density diesel fuel. The

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
75 
system is calibrated to produce predominately liquid fuels; however, electrical power for export 
is also a co-product after satisfying internal plant power consumption. In its current 
configuration, the GTL plant exports 40.8 MWe to the grid. This study also considers CO2 
capture and compression with associated performance and cost. The case for this report is that 
of the GTL Study. 
5.6.1 Size Range 
The GTL Study plant size is a 50,000 BPD GTL production facility and, therefore, the plant size 
assumed for this study is 50,000 BPD to allow for comparisons across NETL reports. The 50,000 
BPD GTL facility produces 1,858,628 tonnes/year of CO2 at 100 percent CF. The NETL study also 
considered power production where the steam turbine produced power in excess of what base 
plant operations would require, and this excess power is exported to the grid. The GTL plant in 
the GTL Study has a net of 40.8 MWe available for export. While this study assumes that all 
power requirements are met with power purchased from the grid, in some cases, such as that 
of the GTL Study, the base plant will have excess power available to meet or partially meet 
compression and cooling power requirements.  
5.6.2 CO2 Point Sources 
Within the GTL facility, there is one main point source of CO2 emissions; the AGR unit in the FT 
section. The FT AGR generates CO2 at 265 psia and 100°F, with a purity of 100 percent CO2. 
5.6.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the GTL process for the 
purpose of this study: 
• The representative plant has a production capacity of 50,000 BPD 
• The CO2 generated is 1,858,628 tonnes CO2/year at 100 percent CF  
• The CO2 stream is 100 percent CO2 
• Due to 100 percent purity, only compression and cooling are required 
• The CO2 stream pressure is 265 psia 
• The CO2 stream temperature is 100 °F 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1] 
5.6.4 CO2 Capture System 
NETL’s GTL Study considers CO2 removal and compression for EOR export and, therefore, the 
base plant separates CO2 as part of its inherent process. The FT AGR unit used discharges CO2 at 
265 psia and, therefore, the compression train used is configured specifically to handle this 
higher inlet suction pressure. Of the vendors quotes discussed in Section 4.1, there is not a 
compression train quote that accounts for higher inlet CO2 stream pressures. Therefore, the cost 
and performance specified in the current GTL Study is replicated here, with its cost being

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
76 
adjusted to December 2018 dollars. This will require that the amount of cooling water 
necessary for interstage cooling be approximated, similar to the CTL case in this study. 
5.6.5 BFD, Stream Table, and Performance Summary 
Since the GTL process releases 100 percent pure CO2, only cooling and compression is required 
for the CO2 stream to be sent directly for EOR or other usage. The compression train used 
discharges the product CO2 at 2,200 psig and 117°F and, therefore, after-cooling is required. 
Exhibit 5-46 gives the BFD for this process. Exhibit 5-47 provides the stream table. 
Exhibit 5-46. GTL CO2 capture BFD 
GTL Facility Desired UsageCompressor1 2 HX 3
 
Exhibit 5-47. GTL stream table 
  1 2 3 
V-L Mole Fraction       
AR 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 
CO2 1.0000 1.0000 1.0000 
COS 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 
H2O 0.0000 0.0000 0.0000 
H2S 0.0000 0.0000 0.0000 
N2 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 
        
V-L Flowrate (kgmol/hr) 4,821 4,821 4,821 
V-L Flowrate (kg/hr) 212,188 212,188 212,188 
Temperature (°C) 38 47 30 
Pressure (MPa, abs) 1.827 15.270 15.270 
Steam Table Enthalpy (kJ/kg)A 8,758 8,754 8,753 
Aspen Plus Enthalpy (kJ/kg)B -8,948 -9,139 -9,188 
Density (kg/m3) 34.2 688.6 628.8 
V-L Molecular Weight 44.0 44.0 44.0 
    
V-L Flowrate (lbmol/hr) 10,629 10,629 10,629 
V-L Flowrate (lb/hr) 467,794 467,794 467,794 
Temperature (°F) 100 117 86 
Pressure (psia) 265.0 2,214.7 2,214.7 
Steam Table Enthalpy (Btu/lb)A 3,766 3,764 3,763

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
77 
  1 2 3 
V-L Mole Fraction       
Aspen Plus Enthalpy (Btu/lb)B -3,847 -3,929 -3,950 
Density (lb/ft3) 2.14 43.0 39.3 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance results given are taken from the current GTL Study case that considered CO2 
capture. The performance summary is provided in Exhibit 5-48. 
Exhibit 5-48. Performance summary 
Performance Summary 
Item 50,000 BPD (kWe) 
CO2 Compressor 6,700 
Circulating Water Pumps 20 
Cooling Tower Fans 10 
Total Auxiliary Load 6,730 
5.6.6 Capture Integration 
For the purposes of this study, it is assumed that a stand-alone cooling water unit will perform 
the necessary cooling for capture and compression. No retrofit case is considered for GTL as any 
new builds would most likely include compression. However, to make this case comparable to 
the other cases considered in this study, the cost for cooling is included in the greenfield COC. 
5.6.7 Power Source 
The power consumption is approximated as 6.73 MW , which includes all power required by the 
compression train and the cooling water system. Power requirement estimates for the cooling 
water unit were scaled as described in Section 4.4. For practical applications for this type of 
facility with power produced on-site and excess power sent to the grid, the power requirements 
may be met with power generated on-site. For instance, while the GTL Study has excess power 
that would be able to satisfy a portion of this study’s power requirement, this scenario should 
be evaluated on a case-by-case basis, which is not included in the scope of this report. 
5.6.8 Economic Analysis Results 
The economic results for CO2 capture application in a GTL plant are presented in this section. 
Owner’s costs (Exhibit 5-49), capital costs (Exhibit 5-50), and O&M costs are calculated as 
discussed in Section 3.1. The greenfield TOC for the GTL case is $59.7 M. The corresponding 
greenfield COC is $6.4/tonne CO2.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
78 
Exhibit 5-49. Owners’ costs for GTL greenfield site 
Description $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 
6 Months All Labor $471 $0 
1-Month Maintenance Materials $46 $0 
1-Month Non-Fuel Consumables $6 $0 
1-Month Waste Disposal $0 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 
2% of TPC $983 $1 
Total $1,507 $1 
Inventory Capital 
60-day supply of fuel and consumables at 100% CF $6 $0 
0.5% of TPC (spare parts) $246 $0 
Total $252 $0 
Other Costs 
Initial Cost for Catalyst and Chemicals $0 $0 
Land $30 $0 
Other Owner's Costs $7,375 $4 
Financing Costs $1,328 $1 
TOC $59,661 $32 
TASC Multiplier (GTL, 31 year) 1.054  
TASC $62,890 $34

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
79 
Exhibit 5-50. Capital costs for GTL greenfield site 
Case: GTL Estimate Type:  Conceptual 
Representative Plant Size:  50,000 BPD Fischer-Tropsch liquids  Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 5 Flue Gas Cleanup 
5.4 CO2 Compression & Drying $14,192 $0 $5,432 $0 $19,624 $3,434 $0 $4,612 $27,670 $15 
5.5 CO2 Compressor Aftercooler $77 $12 $33 $0 $122 $21 $0 $29 $172 $0 
 Subtotal $14,269 $12 $5,465 $0 $19,746 $3,456 $0 $4,640 $27,842 $15 
 7 Ductwork & Stack 
7.3 Ductwork $0 $75 $52 $0 $126 $22 $0 $30 $178 $0 
 Subtotal $0 $75 $52 $0 $126 $22 $0 $30 $178 $0 
 9 Cooling Water System 
9.1 Cooling Towers $197 $0 $61 $0 $257 $45 $0 $61 $363 $0 
9.2 Circulating Water Pumps $16 $0 $1 $0 $17 $3 $0 $4 $24 $0 
9.3 Circulating Water System Aux. $375 $0 $50 $0 $424 $74 $0 $100 $598 $0 
9.4 Circulating Water Piping $0 $173 $157 $0 $330 $58 $0 $78 $466 $0 
9.5 Make-up Water System $59 $0 $75 $0 $134 $23 $0 $31 $189 $0 
9.6 Component Cooling Water System $27 $0 $21 $0 $48 $8 $0 $11 $67 $0 
9.7 Circulating Water System Foundations $0 $22 $36 $0 $58 $10 $0 $14 $82 $0 
 Subtotal $673 $195 $401 $0 $1,269 $222 $0 $298 $1,789 $1 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,831 $0 $157 $0 $1,988 $348 $0 $467 $2,803 $2 
11.3 Switchgear & Motor Control  $2,842 $0 $493 $0 $3,335 $584 $0 $784 $4,702 $3 
11.4 Conduit & Cable Tray $0 $369 $1,065 $0 $1,434 $251 $0 $337 $2,022 $1 
11.5 Wire & Cable $0 $978 $1,749 $0 $2,727 $477 $0 $641 $3,845 $2 
 Subtotal $4,672 $1,348 $3,463 $0 $9,484 $1,660 $0 $2,229 $13,372 $7 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $359 $288 $1,150 $0 $1,797 $315 $0 $422 $2,534 $1 
12.9 Other I&C Equipment $442 $0 $1,023 $0 $1,465 $256 $0 $344 $2,066 $1 
 Subtotal $801 $288 $2,173 $0 $3,262 $571 $0 $767 $4,600 $2 
 13 Improvements to Site 
13.1 Site Preparation $0 $22 $452 $0 $474 $83 $0 $111 $669 $0 
13.2 Site Improvements $0 $105 $140 $0 $245 $43 $0 $58 $345 $0 
13.3 Site Facilities $120 $0 $126 $0 $247 $43 $0 $58 $348 $0 
 Subtotal $120 $128 $718 $0 $966 $169 $0 $227 $1,362 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $11 $9 $0 $19 $3 $0 $5 $27 $0 
 Subtotal $0 $11 $9 $0 $19 $3 $0 $5 $27 $0 
 Total $20,536 $2,056 $12,280 $0 $34,872 $6,103 $0 $8,195 $49,170 $26

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
80 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
5-51, while Exhibit 5-52 shows the COC for a greenfield site for the representative GTL plant. 
Exhibit 5-51. Initial and annual O&M costs for GTL greenfield site 
Case:  Gas-to-Liquids Cost Base: Dec 2018 
Representative Plant Size:  50,000 BPD Fischer-Tropsch liquids  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 1.0  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 1.0  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $438,438 $0.24 
Maintenance Labor:     $314,687 $0.17 
Administrative & Support Labor:     $188,281 $0.10 
Property Taxes and Insurance:     $983,396 $0.53 
Total:     $1,924,802 $1.04 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $472,030 $0.30 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 59 $1.90 $0 $34,632 $0.02 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 0.2 $550.00 $0 $29,863 $0.02 
Subtotal:    $0 $64,495 $0.04 
Variable Operating Costs Total:    $0 $536,526 $0.34 
Exhibit 5-52. COC for 50,000 BPD GTL greenfield 
Component Greenfield Value, $/tonne CO2 
Capital 2.9 
Fixed 1.2 
Variable 0.3 
Purchased Power 1.9 
Total COC 6.4 
5.6.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to GTL plant capacity is shown in Exhibit 5-53. As 
the plant capacity increases, more CO2 is available for capture, thus realizing economies of 
scale. This generic scaling exercise assumes that equipment is available at continuous capacities; 
however, equipment is often manufactured in discrete sizes, which would possibly affect the 
advantages of economies of scale and skew the results of this sensitivity analysis.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
81 
Exhibit 5-53. GTL plant capacity sensitivity 
 
5.6.10 Gas-to-Liquids Conclusion 
The high purity CO2 stream produced from GTL plants makes them a relatively low-cost 
industrial process since the plant performs the CO2 separation as a part of normal operations. A 
CO2 compression system for a 50,000 BPD plant was modeled to estimate the COC of capturing 
CO2 from the process. The results showed the COC of CO2 to be $6.4/tonne CO2 for a greenfield 
site. The plant size sensitivity showed that as plant size decreased from 100,000 to 10,000 BPD, 
the COC increased by $4.9/tonne CO2. As the plant size is decreased, less CO2 is produced, and 
economies of scale are lost, resulting in a higher COC.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
82 
6 COST AND PERFORMANCE: LOW PURITY SOURCES 
The sources discussed in this section are considered low purity sources, meaning the available 
CO2 requires purification to meet EOR pipeline specifications. The CO2 removal systems 
described in Section 4.2 are employed to purify the CO2 streams to meet QGESS specifications 
for EOR pipeline end-use. In all low purity cases, compression, cooling, and TEG dehydration of 
the CO2 stream is required following capture and purification. 
6.1 REFINERY HYDROGEN 
Refineries are an example of an industrial source that currently deploys gas separation 
technology to produce hydrogen. Like other gas processing, hydrogen production emits CO2 not 
only from the process gas, but from the SMR in the form of flue gas, like that of a power plant. 
NETL has studied hydrogen production with post-combustion CO2 capture as part of their 
“Comparison of Commercial, State-of-the-Art, Fossil-Based Hydrogen Production Technologies” 
[40], evaluating H2 production via SMR and coal gasification. 
6.1.1 Size Range 
Size range for hydrogen production varies widely depending on the industry. Ninety-five percent 
of hydrogen produced in the United States is done so by way of NG reforming in refineries. [41] 
The Shell Quest CCS facility in Alberta, Canada has successfully captured and stored over 5 
million tonnes of CO2 from a refinery hydrogen production process since its startup in 2015. [42] 
The Scotford Upgrader near Edmonton, Alberta, Canada includes three hydrogen manufacturing 
units and produces a total of 367 MMSCFD (322,461 tonnes/year) of hydrogen. As a result, 
approximately 1.5 M tonnes/year CO2 is available at the facility. The information provided by 
Shell regarding their ADIP-Ultra pre-combustion CO2 capture process detailed in Section 4.2.2 
provided cost and performance data for an 87,000 tonnes/year hydrogen production facility, 
with 404,700 tonnes/year CO2 available for capture (at 100 percent CF). [2] As such, the 
representative plant for the refinery hydrogen case will mirror that of the quote provided by 
Shell. [2] 
6.1.2 CO2 Point Sources 
When producing hydrogen via SMR, Shell indicates that advanced capture systems (i.e., 99 
percent CO2 capture rate or greater) are most economically implemented in the raw syngas 
stream from the SMR. At lower capture rates, a post-combustion CO2 unit would likely be more 
economically viable, but for the purpose of comparison of like technologies between cases, the 
ADIP-Ultra pre-combustion system is employed in both the 90 and 99 percent capture scenarios 
for the refinery hydrogen case. The pre-combustion AGR captures CO2 upstream of the 
pressure-swing adsorption (PSA) unit, which separates the high purity hydrogen from the syngas 
stream for further processing and end-use. The pre-PSA stream to be purified is characterized in 
Exhibit 6-1.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
83 
Exhibit 6-1. Stream characteristics of raw syngas from SMR 
Component Vapor Mole Fraction 
CO2 0.1918 
H2O 0.0032 
CH4 0.0272 
C2H6 0.0074 
C3H8 0.0017 
C4H10 0.0009 
CO 0.0015 
H2 0.7632 
N2 0.0030 
Component Liquid Weight Fraction 
CO2 0.0047 
H2O 0.9952 
Parameter Value 
Total Stream Vapor Faction 0.658 
Temperature 102.2°F 
Pressure 400.3 psia 
6.1.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the refinery hydrogen 
process for the purpose of this study: 
• The representative refinery hydrogen production unit has a capacity of 87,000 tonnes 
hydrogen/year 
• The raw syngas has a total stream CO2 concentration of 12.7 mole percent 
• The total CO2 generated at 100 percent CF is 404,700 tonnes CO2/year 
• As a low purity source, separation, compression, and cooling are required. 
Separation is accomplished using an ADIP-Ultra AGR unit 
• The temperature of the CO2 entering the AGR pre-scrubber is 102.2°F 
• The pressure of the stream entering the AGR pre-scrubber is 400.3 psia 
• CO2 capture rates of 90 percent and 99 percent are evaluated 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1] 
6.1.4 CO2 Capture System 
With an assumed concentration of only 12.7 mole percent CO2 in the raw syngas from SMR, 
separation is required to meet QGESS EOR pipeline specifications. In addition, water removal,

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
84 
compression, and cooling are necessary to create a CO2 product stream suitable for EOR end-
use. The Shell ADIP-Ultra pre-combustion AGR unit detailed in Section 4.2.2 is modeled to 
represent CO2 removal at 90 and 99 percent. AGR auxiliary loads are scaled based on CO2 
flowrate. 
The AGR unit requires low pressure steam at 74 psia to regenerate the amine-based solvent. 
These steam needs are met with the industrial boiler discussed in Section 4.3. In addition, 
cooling water is required for both the AGR unit and for compression intercooling and after-
cooler. The cooling water unit auxiliaries are scaled as described in Section 4.4. 
6.1.5 BFD, Stream Table, and Performance Summary 
The raw syngas from SMR (stream 1) is fed to ADIP-Ultra capture unit, resulting in four main 
process streams. Water (stream 4) is removed in the knock-out drum and is routed to waste 
treatment. In stream 5 of Exhibit 6-2, H2 and methane (CH4) (along with other hydrocarbons) 
are sent to the PSA where the H2 product is separated for end-use. The remaining process 
streams are the purified CO2 streams: one at “mid-pressure” (stream 2) and one at “low-
pressure” (stream 30). The CO2 streams are routed to the centrifugal compressor, like that 
described in Section 4.1.2, and an aftercooler is used to produce a high purity CO2 stream at 
2,214.7 psia and 86°F for EOR pipeline use. 
Exhibit 6-2. CO2 capture BFD 
 
The stream tables for 99 and 90 percent capture in the refinery hydrogen case are presented in 
Exhibit 6-3 and Exhibit 6-4, respectively.   
Steam 
Methane 
Reformer
HX Desired Usage1 Compressor
2
3
ADIP-Ultra 
CO2 
Capture 
System
4
5
6 7
To PSA
Water KO

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
85 
Exhibit 6-3. Refinery hydrogen stream table for 99 percent capture 
 1 2 3 4 5 6 7 
V-L Mole Fraction        
AR 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0179 0.0000 0.0000 0.0000 0.0336 0.0000 0.0000 
CO 0.0010 0.0000 0.0000 0.0000 0.0017 0.0000 0.0000 
CO2 0.1268 0.8644 0.9629 0.0020 0.0023 0.9995 0.9995 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.5020 0.0000 0.0000 0.0000 0.9427 0.0000 0.0000 
H2O 0.3438 0.1356 0.0371 0.9980 0.0039 0.0005 0.0005 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.0020 0.0000 0.0000 0.0000 0.0034 0.0000 0.0000 
C2H6 0.0049 0.0000 0.0000 0.0000 0.0091 0.0000 0.0000 
C3H8 0.0011 0.0000 0.0000 0.0000 0.0021 0.0000 0.0000 
C4H10 0.0006 0.0000 0.0000 0.0000 0.0011 0.0000 0.0000 
O2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 
                
V-L Flowrate (kgmol/hr) 8,320 593 546 2,848 4,431 1,040 1,040 
V-L Flowrate (kg/hr) 111,368 24,023 23,524 51,457 14,118 45,736 45,736 
Temperature (°C) 39 102 40 39 55 121 29 
Pressure (MPa, abs) 2.76 0.6 0.2 2.8 2.7 15.3 15.3 
Steam Table Enthalpy (kJ/kg)A 10,569 9,172 8,865 15,273 1,597 8,760 8,755 
Aspen Plus Enthalpy (kJ/kg)B -11,217 -9,144 -9,005 -15,873 -1,501 -8,952 -9,196 
Density (kg/m3) 21.3 8.3 3.3 918.8 3.1 283.1 640.4 
V-L Molecular Weight 13.4 40.5 43.0 18.1 3.19 44.0 44.0 
 
      
 
V-L Flowrate (lbmol/hr) 18,342 1,308 1,205 6,279 9,768 2,292 2,292 
V-L Flowrate (lb/hr) 245,524 52,962 51,861 113,443 31,124 100,830 100,830 
Temperature (°F) 102 216 104 102 131 250 85 
Pressure (psia) 399.9 90.8 28.3 399.9 394.4 2,215.9 2,214.7 
Steam Table Enthalpy (Btu/lb)A 4,544 3,943 3,811 6,566 686 3,766 3,764 
Aspen Plus Enthalpy (Btu/lb)B -4,822 -3,931 -3,871 -6,824 -645 -3,849 -3,954 
Density (lb/ft3) 1.33 0.518 0.204 57.4 0.196 17.7 44.0 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
86 
Exhibit 6-4. Refinery hydrogen stream table for 90 percent capture 
 1 2 3 4 5 6 7 
V-L Mole Fraction              
AR 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0179 0.0009 0.0000 0.0000 0.0328 0.0000 0.0000 
CO 0.0010 0.0000 0.0000 0.0000 0.0018 0.0000 0.0000 
CO2 0.1268 0.9493 0.9629 0.0020 0.0232 0.9995 0.9995 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.5020 0.0130 0.0000 0.0000 0.9219 0.0000 0.0000 
H2O 0.3438 0.0368 0.0371 0.9980 0.0047 0.0005 0.0005 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.0020 0.0000 0.0000 0.0000 0.0036 0.0000 0.0000 
C2H6 0.0049 0.0000 0.0000 0.0000 0.0090 0.0000 0.0000 
C3H8 0.0011 0.0000 0.0000 0.0000 0.0020 0.0000 0.0000 
C4H10 0.0006 0.0000 0.0000 0.0000 0.0011 0.0000 0.0000 
O2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 
                
V-L Flowrate (kgmol/hr) 8,320 496 492 2,848 4,524 945 945 
V-L Flowrate (kg/hr) 111,368 21,076 21,170 51,457 18,375 41,572 41,572 
Temperature (°C) 39 102 40 39 55 121 29 
Pressure (MPa, abs) 2.76 0.6 0.2 2.8 2.7 15.3 15.3 
Steam Table Enthalpy (kJ/kg)A 10,569 8,858 8,865 15,273 2,884 8,760 8,755 
Aspen Plus Enthalpy (kJ/kg)B -11,217 -8,938 -9,005 -15,873 -3,225 -8,952 -9,196 
Density (kg/m3) 21.3 8.7 3.3 918.8 4.0 283.1 640.4 
V-L Molecular Weight 13.4 42.5 43.0 18.1 4.06 44.0 44.0 
 
      
 
V-L Flowrate (lbmol/hr) 18,342 1,094 1,084 6,279 9,973 2,083 2,083 
V-L Flowrate (lb/hr) 245,524 46,464 46,672 113,443 40,510 91,651 91,651 
Temperature (°F) 102 216 104 102 131 250 85 
Pressure (psia) 399.9 90.8 28.3 399.9 394.4 2,215.9 2,214.7 
Steam Table Enthalpy (Btu/lb)A 4,544 3,808 3,811 6,566 1,240 3,766 3,764 
Aspen Plus Enthalpy (Btu/lb)B -4,822 -3,843 -3,871 -6,824 -1,387 -3,849 -3,954 
Density (lb/ft3) 1.33 0.542 0.204 57.4 0.250 17.7 40.0 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance summaries for 90 and 99 percent capture in the refinery hydrogen case are 
presented in Exhibit 6-5.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
87 
Exhibit 6-5. Refinery hydrogen performance summary 
Performance Summary 
Item 87,000 tonnes H2/year with 90 percent CO2 capture (kWe) 87,000 tonnes H2/year with 99 percent CO2 capture (kWe) 
CO2 Capture Auxiliaries 500 500 
Steam Boiler Auxiliaries 70 80 
CO2 Compressor 3,160 3,470 
Circulating Water Pumps 210 240 
Cooling Tower Fans 100 120 
Total Auxiliary Load 4,040 4,410 
6.1.6 Capture Integration 
The cost and performance implications of adding an NG-fired boiler, as described in Section 4.3, 
were estimated to meet the steam demands of the Shell ADIP-Ultra CO2 removal system. 
However, in real applications at refineries, if steam requirements for the AGR process are met 
with waste heat from the existing process, an additional boiler for solvent regeneration heating 
needs may not be necessary. The cooling water system is considered a stand-alone addition; 
however, there is potential to integrate existing make-up water systems to feed or partially feed 
the cooling water system, thereby reducing the unit’s size, or replacing it completely with a 
simple HX. 
6.1.7 Power Source 
The compressor power consumption for the 90 and 99 percent capture cases are 3.16 MW and 
3.47 MW , respectively. Power consumption estimates for the cooling water system in each case 
were scaled as described in Section 4.4. The total power requirements were calculated to be 
4.01 MW and 4.42 MW for the 90 and 99 percent capture rates, respectively, which includes all 
power required by the compression train, cooling water system, and ADIP-Ultra capture unit. 
Purchased power cost is estimated at a rate of $60/MWh as discussed in Section 3.1.2.4. To 
satisfy the steam requirements of the AGR system, an industrial boiler was modeled, and fuel 
consumption costs were estimated at a rate of $4.42/MMBtu as discussed in Section 3.1.2.4. 
6.1.8 Economic Analysis Results 
The economic results of CO2 capture application in a refinery hydrogen plant are presented in 
this section. Owner’s costs (Exhibit 6-6), capital costs (Exhibit 6-7 and Exhibit 6-8), and O&M 
costs are calculated as discussed in Section 3.1. Retrofit costs were determined by applying a 
retrofit factor to TPC as discussed in Section 3.3. The greenfield TOC for the refinery hydrogen 
case at 99 percent capture is $159.2 M, while for 90 percent capture, a greenfield TOC of $155.0 
M is estimated. The corresponding greenfield COC for the 99 percent and 90 percent capture 
cases are $57.3/tonne CO2 and $59.9/tonne CO2, respectively. The COC is $58.9/tonne CO2 and 
$61.7/tonne CO2 in retrofit applications for 99 percent and 90 percent capture, respectively.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
88 
Exhibit 6-6. Owners’ costs for refinery hydrogen cases 
Description $/1,000  $/tonnes/yr (CO2) $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 99% Capture 90% Capture 
6 Months All Labor $1,153 $3 $1,139 $3 
1-Month Maintenance Materials $123 $0 $120 $0 
1-Month Non-Fuel Consumables $46 $0 $42 $0 
1-Month Waste Disposal $0 $0 $0 $0 
25% of 1-Month Fuel Cost at 100% CF $89 $0 $78 $0 
2% of TPC $2,613 $7 $2,544 $7 
Total $4,024 $10 $3,923 $11 
Inventory Capital 99% Capture 90% Capture 
60-day supply of fuel and consumables at 
100% CF $786 $2 $693 $2 
0.5% of TPC (spare parts) $653 $2 $636 $2 
Total $1,439 $4 $1,329 $4 
Other Costs 99% Capture 90% Capture 
Initial Cost for Catalyst and Chemicals $0 $0 $0 $0 
Land $30 $0 $30 $0 
Other Owner's Costs $19,594 $49 $19,078 $52 
Financing Costs $3,527 $9 $3,434 $9 
TOC $159,244 $397 $154,978 $426 
TASC Multiplier (Refinery Hydrogen, 33 year) 1.036   1.036   
TASC $164,929 $412 $160,510 $441

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
89 
Exhibit 6-7. Capital costs for refinery hydrogen greenfield site with 99 percent capture 
Case: Refinery H2 Estimate Type:  Conceptual 
Representative Plant Size:  87,000 tonnes H2/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $237 $407 $203 $0 $847 $148 $0 $199 $1,195 $3 
3.2 Water Makeup & Pretreating  $552 $55 $313 $0 $921 $161 $0 $216 $1,298 $3 
3.3 Other Feedwater Subsystems $82 $27 $25 $0 $134 $23 $0 $32 $189 $0 
3.4 Industrial Boiler Package w/Deaerator $1,090 $0 $317 $0 $1,407 $246 $0 $331 $1,985 $5 
3.5 Other Boiler Plant Systems $19 $7 $18 $0 $44 $8 $0 $10 $62 $0 
3.6 NG Pipeline and Start-Up System $317 $14 $10 $0 $341 $60 $0 $80 $481 $1 
3.7 Waste Water Treatment Equipment $2,898 $0 $1,776 $0 $4,675 $818 $0 $1,099 $6,591 $16 
3.9 Miscellaneous Plant Equipment $68 $9 $34 $0 $111 $19 $0 $26 $157 $0 
 Subtotal $5,265 $518 $2,698 $0 $8,481 $1,484 $0 $1,993 $11,958 $30 
 5 Flue Gas Cleanup 
5.1 ADIP-Ultra CO2 Removal System $21,678 $9,377 $19,691 $0 $50,746 $8,881 $8,627 $13,651 $81,904 $204 
5.4 CO2 Compression & Drying $7,402 $1,110 $2,475 $0 $10,987 $1,923 $0 $2,582 $15,492 $39 
5.5 CO2 Compressor Aftercooler $81 $13 $35 $0 $129 $23 $0 $30 $182 $0 
5.12 Gas Cleanup Foundations $0 $4 $4 $0 $8 $1 $0 $2 $11 $0 
 Subtotal $29,162 $10,504 $22,204 $0 $61,870 $10,827 $8,627 $16,265 $97,589 $244 
 7 Ductwork & Stack 
7.3 Ductwork $0 $66 $46 $0 $112 $20 $0 $26 $158 $0 
7.4 Stack $0 $0 $0 $0 $0 $0 $0 $0 $0 $0 
7.5 Duct & Stack Foundations $0 $157 $187 $0 $344 $60 $0 $81 $485 $1 
 Subtotal $0 $223 $233 $0 $456 $80 $0 $107 $643 $2 
 9 Cooling Water System 
9.1 Cooling Towers $455 $0 $141 $0 $596 $104 $0 $140 $840 $2 
9.2 Circulating Water Pumps $41 $0 $3 $0 $44 $8 $0 $10 $62 $0 
9.3 Circulating Water System Aux. $744 $0 $98 $0 $843 $148 $0 $198 $1,188 $3 
9.4 Circulating Water Piping $0 $344 $312 $0 $656 $115 $0 $154 $925 $2 
9.5 Make-up Water System $100 $0 $128 $0 $228 $40 $0 $54 $322 $1 
9.6 Component Cooling Water System $54 $0 $41 $0 $95 $17 $0 $22 $134 $0 
9.7 Circulating Water System Foundations $0 $41 $68 $0 $109 $19 $0 $26 $154 $0 
 Subtotal $1,394 $385 $791 $0 $2,571 $450 $0 $604 $3,624 $9 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,527 $0 $131 $0 $1,658 $290 $0 $390 $2,338 $6 
11.3 Switchgear & Motor Control  $2,371 $0 $411 $0 $2,782 $487 $0 $654 $3,923 $10 
11.4 Conduit & Cable Tray $0 $308 $888 $0 $1,196 $209 $0 $281 $1,687 $4 
11.5 Wire & Cable $0 $816 $1,459 $0 $2,275 $398 $0 $535 $3,208 $8 
 Subtotal $3,898 $1,124 $2,890 $0 $7,912 $1,385 $0 $1,859 $11,156 $28

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
90 
Case: Refinery H2 Estimate Type:  Conceptual 
Representative Plant Size:  87,000 tonnes H2/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $340 $272 $1,089 $0 $1,701 $298 $0 $400 $2,399 $6 
12.9 Other I&C Equipment $418 $0 $969 $0 $1,387 $243 $0 $326 $1,955 $5 
 Subtotal $759 $272 $2,057 $0 $3,088 $540 $0 $726 $4,354 $11 
 13 Improvements to Site 
13.1 Site Preparation $0 $21 $415 $0 $436 $76 $0 $102 $615 $2 
13.2 Site Improvements $0 $97 $128 $0 $225 $39 $0 $53 $317 $1 
13.3 Site Facilities $111 $0 $116 $0 $227 $40 $0 $53 $320 $1 
 Subtotal $111 $117 $660 $0 $888 $155 $0 $209 $1,252 $3 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $21 $16 $0 $37 $6 $0 $9 $52 $0 
 Subtotal $0 $21 $16 $0 $37 $6 $0 $9 $52 $0 
 Total $40,588 $13,166 $31,550 $0 $85,303 $14,928 $8,627 $21,772 $130,630 $326 
Exhibit 6-8. Capital costs for refinery hydrogen greenfield site with 90 percent capture 
Case: Refinery H2 Estimate Type:  Conceptual 
Representative Plant Size:  87,000 tonnes H2/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $217 $372 $186 $0 $775 $136 $0 $182 $1,092 $3 
3.2 Water Makeup & Pretreating  $495 $49 $280 $0 $825 $144 $0 $194 $1,163 $3 
3.3 Other Feedwater Subsystems $73 $24 $23 $0 $119 $21 $0 $28 $168 $0 
3.4 Industrial Boiler Package w/Deaerator $971 $0 $282 $0 $1,254 $219 $0 $295 $1,768 $5 
3.5 Other Boiler Plant Systems $17 $6 $16 $0 $39 $7 $0 $9 $55 $0 
3.6 NG Pipeline and Start-Up System $298 $13 $10 $0 $320 $56 $0 $75 $451 $1 
3.7 Waste Water Treatment Equipment $2,807 $0 $1,721 $0 $4,528 $792 $0 $1,064 $6,385 $18 
3.9 Miscellaneous Plant Equipment $66 $9 $33 $0 $108 $19 $0 $25 $152 $0 
 Subtotal $4,944 $473 $2,551 $0 $7,968 $1,394 $0 $1,872 $11,234 $31 
 5 Flue Gas Cleanup 
5.1 ADIP-Ultra CO2 Removal System $21,409 $9,260 $19,447 $0 $50,116 $8,770 $8,520 $13,481 $80,888 $222 
5.4 CO2 Compression & Drying $6,991 $1,049 $2,338 $0 $10,377 $1,816 $0 $2,439 $14,632 $40 
5.5 CO2 Compressor Aftercooler $75 $12 $32 $0 $120 $21 $0 $28 $169 $0 
5.12 Gas Cleanup Foundations $0 $4 $4 $0 $8 $1 $0 $2 $11 $0 
 Subtotal $28,476 $10,325 $21,820 $0 $60,621 $10,609 $8,520 $15,950 $95,700 $263 
 7 Ductwork & Stack

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
91 
Case: Refinery H2 Estimate Type:  Conceptual 
Representative Plant Size:  87,000 tonnes H2/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
7.3 Ductwork $0 $66 $46 $0 $112 $20 $0 $26 $158 $0 
7.4 Stack $0 $0 $0 $0 $0 $0 $0 $0 $0 $0 
7.5 Duct & Stack Foundations $0 $156 $185 $0 $341 $60 $0 $80 $481 $1 
 Subtotal $0 $222 $231 $0 $454 $79 $0 $107 $640 $2 
 9 Cooling Water System 
9.1 Cooling Towers $405 $0 $125 $0 $530 $93 $0 $124 $747 $2 
9.2 Circulating Water Pumps $36 $0 $3 $0 $38 $7 $0 $9 $54 $0 
9.3 Circulating Water System Aux. $676 $0 $89 $0 $766 $134 $0 $180 $1,079 $3 
9.4 Circulating Water Piping $0 $313 $283 $0 $596 $104 $0 $140 $840 $2 
9.5 Make-up Water System $93 $0 $119 $0 $212 $37 $0 $50 $299 $1 
9.6 Component Cooling Water System $49 $0 $37 $0 $86 $15 $0 $20 $121 $0 
9.7 Circulating Water System 
Foundations $0 $37 $62 $0 $100 $17 $0 $23 $141 $0 
 Subtotal $1,258 $350 $719 $0 $2,327 $407 $0 $547 $3,281 $9 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $1,471 $0 $126 $0 $1,597 $280 $0 $375 $2,252 $6 
11.3 Switchgear & Motor Control  $2,284 $0 $396 $0 $2,680 $469 $0 $630 $3,779 $10 
11.4 Conduit & Cable Tray $0 $297 $856 $0 $1,152 $202 $0 $271 $1,625 $4 
11.5 Wire & Cable $0 $786 $1,405 $0 $2,191 $384 $0 $515 $3,090 $8 
 Subtotal $3,755 $1,083 $2,783 $0 $7,621 $1,334 $0 $1,791 $10,745 $30 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $336 $269 $1,077 $0 $1,682 $294 $0 $395 $2,372 $7 
12.9 Other I&C Equipment $414 $0 $958 $0 $1,371 $240 $0 $322 $1,933 $5 
 Subtotal $750 $269 $2,034 $0 $3,053 $534 $0 $718 $4,305 $12 
 13 Improvements to Site 
13.1 Site Preparation $0 $20 $408 $0 $428 $75 $0 $101 $604 $2 
13.2 Site Improvements $0 $95 $126 $0 $221 $39 $0 $52 $312 $1 
13.3 Site Facilities $109 $0 $114 $0 $223 $39 $0 $52 $315 $1 
 Subtotal $109 $115 $649 $0 $873 $153 $0 $205 $1,231 $3 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $19 $15 $0 $34 $6 $0 $8 $48 $0 
 Subtotal $0 $19 $15 $0 $34 $6 $0 $8 $48 $0 
 Total $39,291 $12,857 $30,802 $0 $82,950 $14,516 $8,520 $21,197 $127,184 $349

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
92 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
6-9 and Exhibit 6-10 for 99 percent and 90 percent capture, respectively, while Exhibit 6-11 
shows the COC for greenfield and retrofit sites for the representative refinery hydrogen plants 
at both capture rates. 
Exhibit 6-9. Initial and annual O&M costs for refinery hydrogen greenfield site with 99 percent capture 
Case:  Refinery Hydrogen Cost Base: Dec 2018 
Representative Plant Size:  87,000 tonnes H2/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $2.52 
Maintenance Labor:     $836,029 $2.09 
Administrative & Support Labor:     $461,109 $1.15 
Property Taxes and Insurance:     $2,612,591 $6.52 
Total:     $4,918,137 $12.28 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $1,254,044 $3.68 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 176 $1.90 $0 $103,543 $0.30 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 1.5 $550.00 $0 $261,093 $0.77 
CO2 Capture System ChemicalsA: Proprietary $29,128 $0.09 
Triethylene Glycol (gal): w/equip. 37 $6.80 $0 $78,191 $0.23 
Subtotal:    $0 $471,954 $1.39 
Waste Disposal 
Triethylene Glycol (gal):  37 $0.35 $0 $4,025 $0.01 
Subtotal:    $0 $4,025 $0.01 
Variable Operating Costs Total:    $0 $1,730,022 $5.08 
Fuel Cost 
Natural Gas (MMBtu) 0 2,653 $4.42 $0 $3,638,461 $10.68 
Total:      $0 $3,638,461 $10.68 
ACO2 capture system chemicals includes ADIP-Ultra Solvent

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
93 
Exhibit 6-10. Initial and annual O&M costs for refinery hydrogen greenfield site with 90 percent capture 
Case:  Refinery Hydrogen Cost Base: Dec 2018 
Representative Plant Size:  87,000 tonnes H2/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $2.77 
Maintenance Labor:     $813,977 $2.24 
Administrative & Support Labor:     $455,596 $1.25 
Property Taxes and Insurance:     $2,543,679 $6.98 
Total:     $4,821,660 $13.24 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $1,220,966 $3.94 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 151 $1.90 $0 $89,100 $0.29 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 1.4 $550.00 $0 $244,702 $0.79 
CO2 Capture System ChemicalsA: Proprietary $23,994 $0.08 
Triethylene Glycol (gal): w/equip. 34 $6.80 $0 $71,551 $0.23 
Subtotal:    $0 $429,347 $1.39 
Waste Disposal 
Triethylene Glycol (gal):  34 $0.35 $0 $3,683 $0.01 
Subtotal:    $0 $3,683 $0.01 
Variable Operating Costs Total:    $0 $1,653,996 $5.34 
Fuel Cost 
Natural Gas (MMBtu) 0 2,330 $4.42 $0 $3,194,817 $10.32 
Total:      $0 $3,194,817 $10.32 
ACO2 capture system chemicals includes ADIP-Ultra Solvent 
Exhibit 6-11. COC for 87,000 tonnes H2/year refinery hydrogen cases 
 99% Capture COC, $/tonne CO2 90% Capture COC, $/tonne CO2 
Component Greenfield Retrofit Greenfield Retrofit 
Capital 21.3 22.2 22.8 23.8 
Fixed 14.4 15.0 15.6 16.2 
Variable 5.1 5.3 5.3 5.5 
Purchased Power and Fuel 16.5 16.5 16.2 16.2 
Total COC 57.3 58.9 59.9 61.7

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
94 
6.1.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to refinery hydrogen plant capacity is shown in 
Exhibit 6-12. As the plant capacity increases, more CO2 is available for capture, thus realizing 
economies of scale. This generic scaling exercise assumes that equipment is available at 
continuous capacities; however, equipment is often manufactured in discrete sizes, which would 
possibly affect the advantages of economies of scale and skew the results of this sensitivity 
analysis. 
Exhibit 6-12. Refinery hydrogen plant capacity sensitivity 
 
As the cost of capturing CO2 is a normalized cost (i.e., $/tonne CO2), higher capture rates appear 
to cost less than lower capture rates. Comparing the true capital and O&M costs (i.e., not as 
normalized costs) shows that capital and O&M expenditures increase at higher capture rates. 
The cost of the capture system and associated consumables increases at a lesser rate than that 
of the amount of CO2 captured (i.e., a 10 percent increase from 90 to 99 percent capture). The 
margin of error associated with the financial assumptions and cost scaling methodology 
employed in this study indicate that with increasing capture rate in the low purity cases, the 
COC is effectively the same. The reported minor increase in capital cost with increased capture 
rate (up to 99 percent for sources with CO2 purity greater than 12 percent) has been validated 
by independent modeling performed by the carbon capture simulation initiative (CCSI) team at 
NETL and has been reported independently in literature. [4] Exhibit 6-13 shows the error in the 
calculated capture system BEC associated with the vendor’s quoted uncertainty rate (-25/+40 
percent) alongside the amount of CO2 captured in the refinery H2 case from 90 to 99 percent 
capture rate.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
95 
Exhibit 6-13. Refinery H2 capture system BEC and amount of CO2 captured versus capture rate 
 
6.1.10 Refinery Hydrogen Conclusion 
The low purity CO2 stream produced in a refinery hydrogen plant results in a higher COC when 
compared to the high purity cases evaluated in this report, but the quantity of CO2 to be 
captured from refinery H2 production processes makes them attractive industrial processes for 
CCS as it would represent a large GHG reduction at a relatively low cost. A CO2 capture and 
compression system for an 87,000 tonnes/year hydrogen plant was modeled to estimate the 
COC of capturing CO2 from the SMR raw syngas. The results showed the COC of CO2 to be 
$57.3/tonne CO2 and $59.9/tonne CO2 for a greenfield site with 99 and 90 percent capture, 
respectively. For a retrofit application, the COC is $58.9/tonne CO2 and $61.7/tonne CO2 for 99 
and 90 percent capture, respectively. The small disparities between greenfield and retrofit cases 
are the result of unknown difficulties required for a retrofit installation versus a greenfield 
application, assuming adequate plot plan space for the retrofit case exists. 
The plant size sensitivity showed that as plant size decreased from 170,000 to 50,000 
tonnes/year, the COC increased by $17.5/tonne CO2 and $18.9/tonne CO2, for 99 and 90 
percent capture, respectively. As the plant size decreases, less CO2 is produced, and economies 
of scale are lost, resulting in a higher COC. Though Shell indicates that for capture rates lower 
than 99 percent, post-combustion capture would be the optimal design, the pre-combustion 
capture system performance and cost was applied for the 90 percent capture case in this study 
for comparative purposes. As demonstrated by the resulting COCs and the sensitivity analysis, 
the normalized cost of 99 percent CO2 capture is less than that of 90 percent capture.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
96 
6.2 CEMENT 
Concrete is formed with a mixture of sand, gravel, water, and cement. Cement, when activated 
with water, is the binder that holds the concrete mixture together. In 2020, the U.S. cement 
industry produced approximately 89.3 M tonnes of Portland cement (PC) and masonry cement, 
with sales at approximately $12.7 billion (B). [43] In the same year, the U.S. apparent 
consumption of cement was 102 M tonnes of cement, meaning that imported cement filled the 
production gap. The United States Geological Survey (USGS) asserts in their 2021 Minerals 
Commodity Summary that U.S. cement production growth has been continuously constrained in 
recent years “by closed or idle plants, underutilized capacity at others, production disruptions 
from plant upgrades, and relatively inexpensive imports.” Production trends for cement, as 
reported by the USGS, are shown in Exhibit 6-14. [43] 
Exhibit 6-14. USGS cement production trends 
Year 2016 2017 2018 2019 2020A 
PC Production, M tonnes 84.7 86.4 86.4 88.0A 89.0 
Apparent PC Consumption, M tonnes 95.2 97.2 98.5 103.0A 102.0 
U.S. Market Satisfied by U.S. Production, % 89.0 88.9 87.7 85.4 87.3 
PC Price, $/tonneB 111 117 121 123A 124 
A Estimated 
B Average mill value 
There are two processes for producing PC: wet kiln and dry kiln. The number of the more 
energy-intensive wet process kilns in the United States has declined by 96 percent from 234, in 
1974, to 10, in 2019, while the number of dry process kilns was reduced from 198 to 110 over 
the same period. [44] Since 2008, approximately 85 percent of U.S. cement is produced using 
the dry-kiln process. [45] 
Both the dry- and wet-kiln processes utilize a multitude of different fuels to provide the heat 
necessary for drying, calcination, and sintering. Shown in Exhibit 6-15 is a breakdown of the fuel 
type consumed for 2019 as reported by the Portland Cement Association. [44] The values are 
given as a percentage of Btu consumed.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
97 
Exhibit 6-15. 2019 U.S. PC fuel consumption 
 
Fuel burning to provide kiln heat is one of two CO2 emissions sources, with the second resulting 
from the calcinations of calcium carbonate to form calcium oxide/calcium silicate species during 
the manufacturing process itself. PC is manufactured by crushing limestone and clay/shale raw 
materials to a powder, and then feeding in dry or slurry form to a kiln. Inside the kiln, the raw 
materials are heated to 2,600–3,000°F (1,430–1,650°C) and a chemical reaction takes place, 
fusing the raw materials into PC clinker, thus, generating CO2. The clinker exits the kiln, is 
cooled, and is ground with gypsum to form PC. [46] Exhibit 6-16 shows the traditional PC 
production process, as adapted from Hassan (2005). [47] 
Exhibit 6-16. PC production process

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
98 
6.2.1 Size Range 
In 2020, there were 96 U.S. cement plants, including both wet and dry processing kilns, in 
operation, with a total production capacity of 89.3 M tonnes/year. [43] The representative plant 
for this study is assumed to produce 1.3 M tonnes/year of PC and masonry cement. Of the 96 
cement plants in 2020, 69 plants fall within the range of 0.5–1.5 M tonnes cement/year, and 31 
plants fall within the range of 0.75–1.25 M tonnes cement/year, which adequately brackets the 
assumed plant size for this study. 
Cement production creates on average 0.922 tonnes CO2 per tonne cement [48]; however, this 
emissions factor may be broken down to two separate factors: an emissions factor for fuel 
burning and an emissions factor for calcium carbonate calcinations. The average fuel-burning 
emissions factor is 0.48 tonnes CO2 per tonne cement, and the average calcination emissions 
factor is 0.44 tonne CO2 per tonne cement. [48] For the reference plant capacity in this report, 
at 100 percent CF, these emissions factors give 631,737 tonnes CO2/year from calcinations of 
raw materials, and 579,092 tonnes CO2/year from fuel burning, totaling 1,210,829 tonnes 
CO2/year from one point source. It is assumed that there is no air in-leakage in the kiln off-gas.  
6.2.2 CO2 Point Sources 
A techno-economic analysis of CO2 capture from a cement plant used the St. Mary’s cement 
plant located in Ontario, Canada, as a reference plant. Specifics given for that plant as of 2004 
are shown below, in Exhibit 6-17. [47] 
Exhibit 6-17. St. Mary’s cement plant characteristics  
St. Mary’s Cement Plant Characteristics 
Kiln Off-Gas Temperature (°F) 320 
Kiln Off-Gas Pressure (psia) 14.7 
Composition (mole %) 
H2O 7.2 
CO2 22.4 
N2 68.1 
O2 2.3 
 
For this study, the main point source of CO2 available for capture is the kiln off-gas, and the 
concentrations given for the St. Mary’s cement plant are assumed as representative. It is 
assumed that the kiln off-gas requires only CO2 removal and compression and no other clean-
up; however, it is possible that other treatment of the off-gas would be necessary prior to AGR.  
A study done by the IEAGHG in 2009 estimated the cost per tonne of CO2 avoided and the cost 
per tonne of cement product when adding CO2 capture to a reference cement plant. [49] Their 
analysis points out that for post-combustion CO2 capture to be implemented, there are several 
issues that must be addressed, as operational problems may arise from: the SO2 concentration

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
99 
in the off-gas stream, which is dependent on the sulfide concentration in the raw meal; NO2 
concentration in the off-gas stream, which may cause solvent degradation; and dust present in 
the off-gas, which will reduce the efficiency of the post-combustion capture process. These 
issues are not considered in this study’s base case; rather, the kiln off-gas is assumed suitable 
for post-combustion amine capture. However, a sensitivity case is evaluated to account for 
these issues with the addition of a selective catalytic reduction (SCR) unit to treat NOx and flue 
gas desulfurization (FGD) to remove oxides of sulfur (SOx). 
6.2.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the cement process for 
the purpose of this study: 
• The representative cement plant has a production capacity of 1.3 M tonnes cement/year 
• The CO2 generated is 1,210,829 tonnes CO2/year at 100 percent CF  
• The CO2 stream available for capture is 22.4 mole percent CO2 
• As a low purity source, separation, compression, and cooling are required. Separation is 
accomplished using a Cansolv AGR unit 
• The temperature of the CO2 available is 320°F 
• The pressure of the CO2 available is 14.7 psia 
• CO2 capture rates of 90 percent and 99 percent are evaluated 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1] 
6.2.4 CO2 Capture System 
The kiln off-gas stream CO2 concentration is relatively low requires purification before 
compression to meet EOR pipeline standards. The purification system used is Shell’s Cansolv 
post-combustion capture system discussed in Section 4.2.1. Steam for solvent regeneration is 
provided by the industrial boiler discussed in Section 4.3. One integrally geared centrifugal 
compression train as discussed in Section 4.1.2 is employed and costs for the compressor are 
scaled based on product CO2 flow. 
6.2.5 BFD, Stream Table, and Performance Summary 
As shown in Exhibit 6-18, the kiln off-gas is sent to the Cansolv separation unit. Water and solids 
recovered from the AGR process are sent to waste treatment. The CO2 stream is then 
compressed with interstage cooling and then after-cooled before reaching the EOR pipeline. 
Exhibit 6-18 shows the BFD for this process, and Exhibit 6-19 and Exhibit 6-20 show the stream 
table for this process with 99 percent and 90 percent capture, respectively.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
100 
Exhibit 6-18. Cement CO2 capture BFD 
 
Exhibit 6-19. Cement stream table for 99 percent capture 
  1 2 3 4 5 
V-L Mole Fraction          
AR 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2240 0.9885 0.9995 0.9995 0.0032 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0720 0.0115 0.0005 0.0005 0.0205 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6810 0.0000 0.0000 0.0000 0.9444 
O2 0.0230 0.0000 0.0000 0.0000 0.0319 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 
           
V-L Flowrate (kgmol/hr) 14,012 3,142 3,107 3,107 10,104 
V-L Flowrate (kg/hr) 433,946 137,356 136,707 136,707 282,775 
Temperature (°C) 160 31 80 30 38 
Pressure (MPa, abs) 0.10 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,442 8,791 8,758 8,755 274 
Aspen Plus Enthalpy (kJ/kg)B -3,269 -8,959 -9,042 -9,195 -209.2 
Density (kg/m3) 0.9 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.0 43.7 44.0 44.0 28.0 
 
    
 
V-L Flowrate (lbmol/hr) 30,891 6,928 6,850 6,850 22,276 
V-L Flowrate (lb/hr) 956,688 302,818 301,387 301,387 623,412 
Temperature (°F) 320 88 177 86 100 
Pressure (psia) 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,480 3,780 3,765 3,764 118 
Aspen Plus Enthalpy (Btu/lb)B -1,406 -3,852 -3,887 -3,953 -89.9 
Density (lb/ft3) 0.054 0.217 27.0 39.3 0.069 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
HX Desired UsageCompressor
Cansolv 
CO2 
Capture 
System
4Kiln Off-gas 1 2 3
5

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
101 
Exhibit 6-20. Cement stream table for 90 percent capture 
 1 2 3 4 5 
V-L Mole Fraction          
AR 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2240 0.9887 0.9995 0.9995 0.0302 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0720 0.0113 0.0005 0.0005 0.0207 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6810 0.0000 0.0000 0.0000 0.9181 
O2 0.0230 0.0000 0.0000 0.0000 0.0310 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 
           
V-L Flowrate (kgmol/hr) 14,012 2,857 2,826 2,826 10,393 
V-L Flowrate (kg/hr) 433,946 124,914 124,334 124,334 295,281 
Temperature (°C) 160 31 80 30 38 
Pressure (MPa, abs) 0.10 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,442 8,791 8,758 8,755 631 
Aspen Plus Enthalpy (kJ/kg)B -3,269 -8,959 -9,042 -9,195 -580.6 
Density (kg/m3) 0.9 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.0 43.7 44.0 44.0 28.4 
 
    
 
V-L Flowrate (lbmol/hr) 30,891 6,300 6,230 6,230 22,912 
V-L Flowrate (lb/hr) 956,688 275,388 274,110 274,110 650,984 
Temperature (°F) 320 88 177 86 100 
Pressure (psia) 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,480 3,779 3,765 3,764 271 
Aspen Plus Enthalpy (Btu/lb)B -1,406 -3,852 -3,887 -3,953 -249.6 
Density (lb/ft3) 0.054 0.217 27.0 39.3 0.070 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
102 
The performance summary for both 90 and 99 percent capture cases is provided in Exhibit 6-21.  
Exhibit 6-21. Performance summary 
Performance Summary 
Item 1.3 M tonnes cement/year with 90 percent CO2 capture (kWe) 1.3 M tonnes cement/year with 99 percent CO2 capture (kWe) 
CO2 Capture Auxiliaries 3,100 3,500 
Steam Boiler Auxiliaries 330 370 
CO2 Compressor 9,570 10,460 
Circulating Water Pumps 980 1,040 
Cooling Tower Fans 500 540 
Total Auxiliary Load 14,480 15,910 
6.2.6 Capture Integration 
The cooling water system in this study is a stand-alone unit; however, there is potential to 
integrate make-up water to feed or partially feed the cooling water system, thereby reducing 
the unit’s size. This would be evaluated on case-by-case basis depending on the size of the 
plant, its layout, and size of the plant’s current cooling system. This evaluation is outside of the 
scope of this report. 
6.2.7 Power Source 
The compressor power consumption for the 90 and 99 percent capture cases are 9.57 MW and 
10.46 MW , respectively. Power consumption estimates for the cooling water system in each 
case were scaled as described in Section 4.4. The total power requirements were calculated to 
be 14.48 MW and 15.91 MW for the 90 and 99 percent capture rates, respectively, which 
includes all power required by the compression train, cooling system, and Cansolv capture unit. 
Purchased power cost is estimated at a rate of $60/MWh as discussed in Section 3.1.2.4. To 
satisfy the steam requirements of the AGR system, an industrial boiler was modeled, and fuel 
consumption costs were estimated at a rate of $4.42/MMBtu as discussed in Section 3.1.2.4. 
6.2.8 Economic Analysis Results 
The economic results of CO2 capture application in a cement plant are presented in this section. 
Owner’s costs (Exhibit 6-22), capital costs (Exhibit 6-23 and Exhibit 6-24), and O&M costs are 
calculated as discussed in Section 3.1. Retrofit costs were determined by applying a retrofit 
factor to TPC as discussed in Section 3.3. The greenfield TOC for the cement case at 99 percent 
capture is $414.0 M, while for 90 percent capture, a greenfield TOC of $386.0 M is estimated. 
The corresponding greenfield COC for the 99 percent and 90 percent capture cases are 
$60.8/tonne CO2 and $62.7 /tonne CO2, respectively. The COC is $62.4/tonne CO2 and 
$64.3/tonne CO2 in retrofit applications for 99 percent and 90 percent capture, respectively.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
103 
Exhibit 6-22. Owners’ costs for cement cases 
Description $/1,000  $/tonnes/yr (CO2) $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 99% Capture 90% Capture 
6 Months All Labor $1,986 $2 $1,922 $2 
1-Month Maintenance Materials $319 $0 $304 $0 
1-Month Non-Fuel Consumables $257 $0 $240 $0 
1-Month Waste Disposal $11 $0 $11 $0 
25% of 1-Month Fuel Cost at 100% CF $391 $0 $355 $0 
2% of TPC $6,779 $6 $6,457 $6 
Total $9,742 $8 $9,289 $9 
Inventory Capital 99% Capture 90% Capture 
60-day supply of fuel and consumables at 100% CF $3,550 $3 $3,239 $3 
0.5% of TPC (spare parts) $1,695 $1 $1,614 $1 
Total $5,245 $4 $4,853 $4 
Other Costs 99% Capture 90% Capture 
Initial Cost for Catalyst and Chemicals $0 $0 $0 $0 
Land $30 $0 $30 $0 
Other Owner's Costs $50,842 $42 $48,431 $44 
Financing Costs $9,152 $8 $8,718 $8 
TOC $413,960 $346 $394,192 $362 
TASC Multiplier (Cement, 33 year) 1.054  1.054  
TASC $436,252 $364 $415,418 $381

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
104 
Exhibit 6-23. Capital costs for cement greenfield site with 99 percent capture 
Case: Cement Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes cement/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $658 $1,127 $564 $0 $2,349 $411 $0 $552 $3,311 $3 
3.2 Water Makeup & Pretreating  $1,633 $163 $925 $0 $2,722 $476 $0 $640 $3,837 $3 
3.3 Other Feedwater Subsystems $305 $100 $95 $0 $500 $87 $0 $117 $704 $1 
3.4 Industrial Boiler Package 
w/Deaerator $4,061 $0 $1,181 $0 $5,242 $917 $0 $1,232 $7,391 $6 
3.5 Other Boiler Plant Systems $73 $27 $67 $0 $167 $29 $0 $39 $235 $0 
3.6 NG Pipeline and Start-Up System $654 $28 $21 $0 $703 $123 $0 $165 $992 $1 
3.7 Waste Water Treatment 
Equipment $3,003 $0 $1,840 $0 $4,843 $848 $0 $1,138 $6,829 $6 
3.9 Miscellaneous Plant Equipment $98 $13 $50 $0 $161 $28 $0 $38 $227 $0 
 Subtotal $10,485 $1,458 $4,743 $0 $16,686 $2,920 $0 $3,921 $23,527 $20 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $58,671 $25,377 $53,292 $0 $137,340 $24,034 $23,348 $36,944 $221,667 $185 
5.4 CO2 Compression & Drying $17,147 $2,572 $5,733 $0 $25,452 $4,454 $0 $5,981 $35,887 $30 
5.5 CO2 Compressor Aftercooler $137 $22 $59 $0 $218 $38 $0 $51 $307 $0 
5.12 Gas Cleanup Foundations $0 $65 $57 $0 $122 $21 $0 $29 $172 $0 
 Subtotal $75,955 $28,036 $59,141 $0 $163,132 $28,548 $23,348 $43,006 $258,033 $215 
 7 Ductwork & Stack 
7.3 Ductwork $0 $1,608 $1,117 $0 $2,725 $477 $0 $640 $3,842 $3 
7.4 Stack $7,699 $0 $4,474 $0 $12,174 $2,130 $0 $2,861 $17,165 $14 
7.5 Duct & Stack Foundations $0 $172 $204 $0 $376 $66 $0 $88 $530 $0 
 Subtotal $7,699 $1,779 $5,795 $0 $15,274 $2,673 $0 $3,589 $21,537 $18 
 9 Cooling Water System 
9.1 Cooling Towers $1,426 $0 $441 $0 $1,867 $327 $0 $439 $2,632 $2 
9.2 Circulating Water Pumps $147 $0 $10 $0 $157 $27 $0 $37 $221 $0 
9.3 Circulating Water System Aux. $1,895 $0 $251 $0 $2,146 $376 $0 $504 $3,025 $3 
9.4 Circulating Water Piping $0 $876 $794 $0 $1,670 $292 $0 $392 $2,355 $2 
9.5 Make-up Water System $207 $0 $265 $0 $472 $83 $0 $111 $666 $1 
9.6 Component Cooling Water 
System $137 $0 $105 $0 $241 $42 $0 $57 $340 $0 
9.7 Circulating Water System 
Foundations $0 $97 $161 $0 $258 $45 $0 $61 $363 $0 
 Subtotal $3,811 $973 $2,027 $0 $6,811 $1,192 $0 $1,600 $9,603 $8 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $2,650 $0 $227 $0 $2,878 $504 $0 $676 $4,058 $3 
11.3 Switchgear & Motor Control  $4,114 $0 $714 $0 $4,828 $845 $0 $1,135 $6,808 $6 
11.4 Conduit & Cable Tray $0 $535 $1,541 $0 $2,076 $363 $0 $488 $2,927 $2

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
105 
Case: Cement Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes cement/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
11.5 Wire & Cable $0 $1,416 $2,532 $0 $3,948 $691 $0 $928 $5,567 $5 
 Subtotal $6,765 $1,951 $5,014 $0 $13,730 $2,403 $0 $3,227 $19,360 $16 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $402 $322 $1,286 $0 $2,010 $352 $0 $472 $2,834 $2 
12.9 Other I&C Equipment $494 $0 $1,144 $0 $1,638 $287 $0 $385 $2,310 $2 
 Subtotal $896 $322 $2,431 $0 $3,648 $638 $0 $857 $5,144 $4 
 13 Improvements to Site 
13.1 Site Preparation $0 $27 $537 $0 $563 $99 $0 $132 $794 $1 
13.2 Site Improvements $0 $125 $166 $0 $291 $51 $0 $68 $410 $0 
13.3 Site Facilities $143 $0 $150 $0 $293 $51 $0 $69 $414 $0 
 Subtotal $143 $152 $853 $0 $1,148 $201 $0 $270 $1,618 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $50 $40 $0 $90 $16 $0 $21 $127 $0 
 Subtotal $0 $50 $40 $0 $90 $16 $0 $21 $127 $0 
 Total $105,754 $34,722 $80,043 $0 $220,519 $38,591 $23,348 $56,491 $338,949 $283 
Exhibit 6-24. Capital costs for cement greenfield site with 90 percent capture  
Case: Cement Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes cement/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $616 $1,056 $528 $0 $2,199 $385 $0 $517 $3,101 $3 
3.2 Water Makeup & Pretreating  $1,543 $154 $874 $0 $2,571 $450 $0 $604 $3,626 $3 
3.3 Other Feedwater Subsystems $280 $92 $87 $0 $459 $80 $0 $108 $647 $1 
3.4 Industrial Boiler Package 
w/Deaerator $3,731 $0 $1,085 $0 $4,816 $843 $0 $1,132 $6,790 $6 
3.5 Other Boiler Plant Systems $67 $25 $61 $0 $153 $27 $0 $36 $216 $0 
3.6 NG Pipeline and Start-Up System $624 $27 $20 $0 $671 $117 $0 $158 $946 $1 
3.7 Waste Water Treatment 
Equipment $2,872 $0 $1,760 $0 $4,632 $811 $0 $1,088 $6,531 $6 
3.9 Miscellaneous Plant Equipment $96 $13 $49 $0 $157 $27 $0 $37 $221 $0 
 Subtotal $9,829 $1,366 $4,464 $0 $15,659 $2,740 $0 $3,680 $22,079 $20 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $55,656 $24,073 $50,554 $0 $130,284 $22,800 $22,148 $35,046 $210,278 $193 
5.4 CO2 Compression & Drying $16,242 $2,436 $5,430 $0 $24,108 $4,219 $0 $5,665 $33,993 $31 
5.5 CO2 Compressor Aftercooler $127 $20 $54 $0 $201 $35 $0 $47 $284 $0 
5.12 Gas Cleanup Foundations $0 $65 $57 $0 $122 $21 $0 $29 $172 $0

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
106 
Case: Cement Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes cement/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 Subtotal $72,025 $26,595 $56,096 $0 $154,716 $27,075 $22,148 $40,788 $244,727 $225 
 7 Ductwork & Stack 
7.3 Ductwork $0 $1,608 $1,117 $0 $2,725 $477 $0 $640 $3,842 $4 
7.4 Stack $7,712 $0 $4,482 $0 $12,194 $2,134 $0 $2,866 $17,194 $16 
7.5 Duct & Stack Foundations $0 $171 $203 $0 $374 $65 $0 $88 $527 $0 
 Subtotal $7,712 $1,778 $5,802 $0 $15,293 $2,676 $0 $3,594 $21,563 $20 
 9 Cooling Water System 
9.1 Cooling Towers $1,343 $0 $415 $0 $1,759 $308 $0 $413 $2,480 $2 
9.2 Circulating Water Pumps $137 $0 $10 $0 $147 $26 $0 $35 $207 $0 
9.3 Circulating Water System Aux. $1,805 $0 $239 $0 $2,043 $358 $0 $480 $2,881 $3 
9.4 Circulating Water Piping $0 $834 $756 $0 $1,590 $278 $0 $374 $2,242 $2 
9.5 Make-up Water System $199 $0 $255 $0 $454 $80 $0 $107 $641 $1 
9.6 Component Cooling Water System $130 $0 $100 $0 $230 $40 $0 $54 $324 $0 
9.7 Circulating Water System 
Foundations $0 $93 $154 $0 $246 $43 $0 $58 $347 $0 
 Subtotal $3,614 $927 $1,929 $0 $6,470 $1,132 $0 $1,520 $9,122 $8 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $2,545 $0 $218 $0 $2,763 $484 $0 $649 $3,896 $4 
11.3 Switchgear & Motor Control  $3,951 $0 $685 $0 $4,636 $811 $0 $1,090 $6,537 $6 
11.4 Conduit & Cable Tray $0 $514 $1,480 $0 $1,994 $349 $0 $469 $2,811 $3 
11.5 Wire & Cable $0 $1,360 $2,431 $0 $3,791 $663 $0 $891 $5,346 $5 
 Subtotal $6,496 $1,874 $4,815 $0 $13,185 $2,307 $0 $3,098 $18,590 $17 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $397 $318 $1,271 $0 $1,985 $347 $0 $467 $2,799 $3 
12.9 Other I&C Equipment $488 $0 $1,130 $0 $1,618 $283 $0 $380 $2,282 $2 
 Subtotal $885 $318 $2,401 $0 $3,604 $631 $0 $847 $5,081 $5 
 13 Improvements to Site 
13.1 Site Preparation $0 $26 $527 $0 $553 $97 $0 $130 $780 $1 
13.2 Site Improvements $0 $123 $163 $0 $285 $50 $0 $67 $402 $0 
13.3 Site Facilities $140 $0 $147 $0 $288 $50 $0 $68 $406 $0 
 Subtotal $140 $149 $837 $0 $1,126 $197 $0 $265 $1,588 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $48 $38 $0 $86 $15 $0 $20 $122 $0 
 Subtotal $0 $48 $38 $0 $86 $15 $0 $20 $122 $0 
 Total $100,701 $33,054 $76,381 $0 $210,137 $36,774 $22,148 $53,812 $322,871 $296

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
107 
The initial and annual O&M costs for a greenfield site were calculated and are shown in Exhibit 
6-25 and Exhibit 6-26 for 99 percent and 90 percent capture, respectively, while Exhibit 6-27 
shows the COC for greenfield and retrofit sites for the representative cement plants at both 
capture rates. 
Exhibit 6-25. Initial and annual O&M costs for cement greenfield site with 99 percent capture 
Case:  Cement Cost Base: Dec 2018 
Representative Plant Size:  1.3 M tonnes cement/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $0.84 
Maintenance Labor:     $2,169,273 $1.81 
Administrative & Support Labor:     $794,420 $0.66 
Property Taxes and Insurance:     $6,778,980 $5.66 
Total:     $10,751,081 $8.98 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $3,253,910 $3.20 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 775 $1.90 $0 $457,112 $0.45 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 2.6 $550.00 $0 $440,049 $0.43 
CO2 Capture System ChemicalsA: Proprietary $1,215,644 $1.19 
Triethylene Glycol (gal): w/equip. 240 $6.80 $0 $507,172 $0.50 
Subtotal:    $0 $2,619,977 $2.57 
Waste Disposal 
Triethylene Glycol (gal):  240 $0.35 $0 $26,104 $0.03 
Thermal Reclaimer Unit Waste (ton)   0.69 $38.00 $0 $8,077 $0.01 
Prescrubber Blowdown Waste (ton)   6.7 $38.00 $0 $78,627 $0.08 
Subtotal:    $0 $112,809 $0.11 
Variable Operating Costs Total:    $0 $5,986,696 $5.88 
Fuel Cost 
Natural Gas (MMBtu) 0 11,625 $4.42 $0 $15,941,580 $15.66 
Total:      $0 $15,941,580 $15.66 
ACO2 capture system chemicals includes NaOH and Cansolv solvent

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
108 
Exhibit 6-26. Initial and annual O&M costs for cement greenfield site with 90 percent capture 
Case:  Cement Cost Base: Dec 2018 
Representative Plant Size:  1.3 M tonnes cement/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $0.93 
Maintenance Labor:     $2,066,376 $1.90 
Administrative & Support Labor:     $768,696 $0.71 
Property Taxes and Insurance:     $6,457,426 $5.93 
Total:     $10,300,905 $9.46 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $3,099,564 $3.35 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 717 $1.90 $0 $422,931 $0.46 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 2.4 $550.00 $0 $410,207 $0.44 
CO2 Capture System ChemicalsA: Proprietary $1,152,997 $1.25 
Triethylene Glycol (gal): w/equip. 219 $6.80 $0 $461,270 $0.50 
Subtotal:    $0 $2,447,404 $2.64 
Waste Disposal 
Triethylene Glycol (gal):  219 $0.35 $0 $23,742 $0.03 
Thermal Reclaimer Unit Waste (ton)   0.65 $38.00 $0 $7,713 $0.01 
Prescrubber Blowdown Waste (ton)   6.7 $38.00 $0 $78,627 $0.08 
Subtotal:    $0 $110,082 $0.12 
Variable Operating Costs Total:    $0 $5,657,051 $6.11 
Fuel Cost 
Natural Gas (MMBtu) 0 10,569 $4.42 $0 $14,493,467 $15.66 
Total:    $0 $14,493,467 $15.66 
ACO2 capture system chemicals includes NaOH and Cansolv solvent 
Exhibit 6-27. COC for 1.3 M tonnes/year cement cases 
 99% Capture COC, $/tonne CO2 90% Capture COC, $/tonne CO2 
Component Greenfield Retrofit Greenfield Retrofit 
Capital 21.8 22.6 22.8 23.7 
Fixed 10.6 11.0 11.1 11.6 
Variable 5.9 6.0 6.1 6.3 
Purchased Power and Fuel 22.6 22.6 22.6 22.6 
Total COC 60.8 62.4 62.7 64.3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
109 
6.2.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of greenfield COC to cement plant capacity is shown in Exhibit 
6-28. As the plant capacity increases, more CO2 is available for capture, thus realizing economies 
of scale. This generic scaling exercise assumes that equipment is available at continuous 
capacities; however, equipment is often manufactured in discrete sizes, which would possibly 
affect the advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 6-28. Cement plant capacity sensitivity 
 
As the cost of capturing CO2 is a normalized cost (i.e., $/tonne CO2), higher capture rates appear 
to cost less than lower capture rates. Comparing the true capital and O&M costs (i.e., not as 
normalized costs) shows that capital and O&M expenditures increase at higher capture rates. 
The cost of the capture system and associated consumables increases at a lesser rate than that 
of the amount of CO2 captured (i.e., a 10 percent increase from 90 to 99 percent capture). The 
margin of error associated with the financial assumptions and cost scaling methodology 
employed in this study indicate that with increasing capture rate in the low purity cases, the 
COC is effectively the same. The reported minor increase in capital cost with increased capture 
rate (up to 99 percent for sources with CO2 purity greater than 12 percent) has been validated 
by independent modeling performed by the CCSI team at NETL and has been reported 
independently in literature. [4] Exhibit 6-29 shows the error in the calculated capture system 
BEC associated with the vendor’s quoted uncertainty rate (-25/+40 percent) alongside the 
amount of CO2 captured in the cement case from 90 to 99 percent capture rate.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
110 
Exhibit 6-29. Cement capture system BEC and amount of CO 2 captured versus capture rate 
 
6.2.10 FGD + SCR Sensitivity Case 
As stated previously, a cement plant’s kiln off-gas may require additional treatment prior to 
purification to maximize the efficiency of the amine-based CO2 removal system and prevent 
solvent degradation. Definitive concentrations for cement kiln off-gas SOx and oxides of 
nitrogen (NOx) are not available, as SOx is highly dependent upon the sulfide concentration of 
the raw meal used, and NOx content varies widely. Therefore, to account for the addition of SCR 
and FGD units in terms of capital cost, as well as power and chemical requirements/costs, these 
values were scaled from BBR4 Case B12B [5] based on quantity of gas treated. The FGD 
employed in the reference case is a wet FGD; however, if SOx concentrations were low enough, 
a lower cost option, such as a dry FGD could also be used, which would reduce cost compared 
to the wet FGD estimated in this report.  
The economic results of this sensitivity case are presented in Exhibit 6-30 and Exhibit 6-31 for 
the 99 and 90 percent capture cases, respectively. The addition of SCR and FGD increases the 
TPC over the base case greenfield cost by approximately $124.5 M. Most of this additional 
capital is attributed to the FGD absorber vessels and accessories, which account for $110.7 M of 
the TPC increase.  
Fixed O&M and maintenance materials costs also increase, as some are calculated based on 
TPC. Consumables costs also increase by $2.3 M, due to the requirement of limestone for the 
FGD, as well as 19 weight percent ammonia for SCR injection. The initial SCR catalyst is assumed

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
111 
to be included with equipment purchase, but catalyst makeup cost is calculated on a 3-year 
replacement cycle. The auxiliary requirements for the FGD and SCR are scaled linearly from the 
BBR4 Case B12B, adding 672 kW to the auxiliary load requirements for capture integration in 
the representative cement plant. O&M costs for each cement sensitivity case are shown in 
Exhibit 6-33 and Exhibit 6-34 for 99 and 90 percent capture cases, respectively, while owner’s 
cost summaries for both cases are shown in Exhibit 6-32.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
112 
Exhibit 6-30. Capital costs for cement greenfield site with FGD and SCR and 99 percent CO 2 capture 
Case: Cement with FGD and SCR Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $658 $1,127 $564 $0 $2,349 $411 $0 $552 $3,311 $3 
3.2 Water Makeup & Pretreating  $1,633 $163 $925 $0 $2,722 $476 $0 $640 $3,837 $3 
3.3 Other Feedwater Subsystems $305 $100 $95 $0 $500 $87 $0 $117 $704 $1 
3.4 Industrial Boiler Package 
w/Deaerator $4,061 $0 $1,181 $0 $5,242 $917 $0 $1,232 $7,391 $6 
3.5 Other Boiler Plant Systems $73 $27 $67 $0 $167 $29 $0 $39 $235 $0 
3.6 NG Pipeline and Start-Up 
System $654 $28 $21 $0 $703 $123 $0 $165 $992 $1 
3.7 Waste Water Treatment 
Equipment $3,003 $0 $1,840 $0 $4,843 $848 $0 $1,138 $6,829 $6 
3.9 Miscellaneous Plant Equipment $98 $13 $50 $0 $161 $28 $0 $38 $227 $0 
 Subtotal $10,485 $1,458 $4,743 $0 $16,686 $2,920 $0 $3,921 $23,527 $20 
 4 Cement Kiln Accessories 
4.1 Selective Catalytic Reduction 
System $5,660 $0 $3,225 $0 $8,885 $1,555 $0 $2,088 $12,528 $10 
 Subtotal $5,660 $0 $3,225 $0 $8,885 $1,555 $0 $2,088 $12,528 $10 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $58,671 $25,377 $53,292 $0 $137,340 $24,034 $23,348 $36,944 $221,667 $185 
5.2 FGD Absorber Vessels & Accessories $64,703 $0 $13,834 $0 $78,537 $13,744 $0 $18,456 $110,737 $92 
5.3 Other FGD $290 $0 $327 $0 $617 $108 $0 $145 $870 $1 
5.4 CO2 Compression & Drying $17,147 $2,572 $5,733 $0 $25,452 $4,454 $0 $5,981 $35,887 $30 
5.5 CO2 Compressor Aftercooler $137 $22 $59 $0 $218 $38 $0 $51 $307 $0 
5.12 Gas Cleanup Foundations $0 $65 $57 $0 $122 $21 $0 $29 $172 $0 
 Subtotal $140,948 $28,036 $73,302 $0 $242,286 $42,400 $23,348 $61,607 $369,640 $309 
 7 Ductwork & Stack 
7.3 Ductwork $0 $1,608 $1,117 $0 $2,725 $477 $0 $640 $3,842 $3 
7.4 Stack $7,699 $0 $4,474 $0 $12,174 $2,130 $0 $2,861 $17,165 $14 
7.5 Duct & Stack Foundations $0 $172 $204 $0 $376 $66 $0 $88 $530 $0 
 Subtotal $7,699 $1,779 $5,795 $0 $15,274 $2,673 $0 $3,589 $21,537 $18 
 9 Cooling Water System 
9.1 Cooling Towers $1,426 $0 $441 $0 $1,867 $327 $0 $439 $2,632 $2 
9.2 Circulating Water Pumps $147 $0 $10 $0 $157 $27 $0 $37 $221 $0 
9.3 Circulating Water System Aux. $1,895 $0 $251 $0 $2,146 $376 $0 $504 $3,025 $3 
9.4 Circulating Water Piping $0 $876 $794 $0 $1,670 $292 $0 $392 $2,355 $2 
9.5 Make-up Water System $207 $0 $265 $0 $472 $83 $0 $111 $666 $1

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
113 
Case: Cement with FGD and SCR Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
9.6 Component Cooling Water 
System $137 $0 $105 $0 $241 $42 $0 $57 $340 $0 
9.7 Circulating Water System 
Foundations $0 $97 $161 $0 $258 $45 $0 $61 $363 $0 
 Subtotal $3,811 $973 $2,027 $0 $6,811 $1,192 $0 $1,600 $9,603 $8 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $2,698 $0 $231 $0 $2,929 $513 $0 $688 $4,130 $3 
11.3 Switchgear & Motor Control  $4,188 $0 $727 $0 $4,915 $860 $0 $1,155 $6,930 $6 
11.4 Conduit & Cable Tray $0 $544 $1,569 $0 $2,113 $370 $0 $497 $2,980 $2 
11.5 Wire & Cable $0 $1,442 $2,577 $0 $4,019 $703 $0 $945 $5,667 $5 
 Subtotal $6,886 $1,986 $5,104 $0 $13,977 $2,446 $0 $3,285 $19,707 $16 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $404 $323 $1,293 $0 $2,021 $354 $0 $475 $2,849 $2 
12.9 Other I&C Equipment $497 $0 $1,150 $0 $1,647 $288 $0 $387 $2,323 $2 
 Subtotal $901 $323 $2,444 $0 $3,668 $642 $0 $862 $5,172 $4 
 13 Improvements to Site 
13.1 Site Preparation $0 $27 $541 $0 $568 $99 $0 $133 $801 $1 
13.2 Site Improvements $0 $126 $167 $0 $293 $51 $0 $69 $414 $0 
13.3 Site Facilities $144 $0 $151 $0 $296 $52 $0 $70 $417 $0 
 Subtotal $144 $153 $860 $0 $1,157 $203 $0 $272 $1,632 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $50 $40 $0 $90 $16 $0 $21 $127 $0 
 Subtotal $0 $50 $40 $0 $90 $16 $0 $21 $127 $0 
 Total $176,534 $34,760 $97,540 $0 $308,834 $54,046 $23,348 $77,245 $463,473 $387 
Exhibit 6-31. Capital costs for cement greenfield site with FGD and SCR and 90 percent CO2 capture 
Case: Cement with FGD and SCR Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $616 $1,056 $528 $0 $2,199 $385 $0 $517 $3,101 $3 
3.2 Water Makeup & Pretreating  $1,543 $154 $874 $0 $2,571 $450 $0 $604 $3,626 $3 
3.3 Other Feedwater Subsystems $280 $92 $87 $0 $459 $80 $0 $108 $647 $1 
3.4 Industrial Boiler Package 
w/Deaerator $3,731 $0 $1,085 $0 $4,816 $843 $0 $1,132 $6,790 $6 
3.5 Other Boiler Plant Systems $67 $25 $61 $0 $153 $27 $0 $36 $216 $0 
3.6 NG Pipeline and Start-Up 
System $624 $27 $20 $0 $671 $117 $0 $158 $946 $1

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
114 
Case: Cement with FGD and SCR Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
3.7 Waste Water Treatment 
Equipment $2,872 $0 $1,760 $0 $4,632  $811 $0 $1,088 $6,531 $6 
3.9 Miscellaneous Plant Equipment $96 $13 $49 $0 $157 $27 $0 $37 $221 $0 
 Subtotal $9,829 $1,366 $4,464 $0 $15,659 $2,740 $0 $3,680 $22,079 $20 
 4 Cement Kiln Accessories 
4.1 Selective Catalytic Reduction 
System $5,660 $0 $3,225 $0 $8,885 $1,555 $0 $2,088 $12,528 $12 
 Subtotal $5,660 $0 $3,225 $0 $8,885 $1,555 $0 $2,088 $12,528 $12 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $55,656 $24,073 $50,554 $0 $130,284 $22,800 $22,148 $35,046 $210,278 $193 
5.2 FGD Absorber Vessels & Accessories $64,703 $0 $13,834 $0 $78,537 $13,744 $0 $18,456 $110,737 $102 
5.3 Other FGD $290 $0 $327 $0 $617 $108 $0 $145 $870 $1 
5.4 CO2 Compression & Drying $16,242 $2,436 $5,430 $0 $24,108 $4,219 $0 $5,665 $33,993 $31 
5.5 CO2 Compressor Aftercooler $127 $20 $54 $0 $201 $35 $0 $47 $284 $0 
5.12 Gas Cleanup Foundations $0 $65 $57 $0 $122 $21 $0 $29 $172 $0 
 Subtotal $137,018 $26,595 $70,257 $0 $233,869 $40,927 $22,148 $59,389 $356,334 $327 
 7 Ductwork & Stack 
7.3 Ductwork $0 $1,608 $1,117 $0 $2,725 $477 $0 $640 $3,842 $4 
7.4 Stack $7,712 $0 $4,482 $0 $12,194 $2,134 $0 $2,866 $17,194 $16 
7.5 Duct & Stack Foundations $0 $171 $203 $0 $374 $65 $0 $88 $527 $0 
 Subtotal $7,712 $1,778 $5,802 $0 $15,293 $2,676 $0 $3,594 $21,563 $20 
 9 Cooling Water System 
9.1 Cooling Towers $1,343 $0 $415 $0 $1,759 $308 $0 $413 $2,480 $2 
9.2 Circulating Water Pumps $137 $0 $10 $0 $147 $26 $0 $35 $207 $0 
9.3 Circulating Water System Aux. $1,805 $0 $239 $0 $2,043 $358 $0 $480 $2,881 $3 
9.4 Circulating Water Piping $0 $834 $756 $0 $1,590 $278 $0 $374 $2,242 $2 
9.5 Make-up Water System $199 $0 $255 $0 $454 $80 $0 $107 $641 $1 
9.6 Component Cooling Water 
System $130 $0 $100 $0 $230 $40 $0 $54 $324 $0 
9.7 Circulating Water System 
Foundations $0 $93 $154 $0 $246 $43 $0 $58 $347 $0 
 Subtotal $3,614 $927 $1,929 $0 $6,470 $1,132 $0 $1,520 $9,122 $8 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $2,595 $0 $223 $0 $2,818 $493 $0 $662 $3,973 $4 
11.3 Switchgear & Motor Control  $4,029 $0 $699 $0 $4,728 $827 $0 $1,111 $6,666 $6 
11.4 Conduit & Cable Tray $0 $524 $1,509 $0 $2,033 $356 $0 $478 $2,866 $3 
11.5 Wire & Cable $0 $1,387 $2,479 $0 $3,866 $677 $0 $909 $5,451 $5 
 Subtotal $6,624 $1,911 $4,910 $0 $13,444 $2,353 $0 $3,159 $18,957 $17 
 12 Instrumentation & Control

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
115 
Case: Cement with FGD and SCR Estimate Type:  Conceptual 
Representative Plant Size:  1.3 M tonnes/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
12.8 Instrument Wiring & Tubing $399 $320 $1,278 $0 $1,997 $350 $0 $469 $2,816 $3 
12.9 Other I&C Equipment $491 $0 $1,137 $0 $1,628 $285 $0 $383 $2,295 $2 
 Subtotal $890 $320 $2,415 $0 $3,625 $634 $0 $852 $5,111 $5 
 13 Improvements to Site 
13.1 Site Preparation $0 $26 $532 $0 $558 $98 $0 $131 $787 $1 
13.2 Site Improvements $0 $124 $164 $0 $288 $50 $0 $68 $406 $0 
13.3 Site Facilities $142 $0 $149 $0 $291 $51 $0 $68 $410 $0 
 Subtotal $142 $150 $845 $0 $1,136 $199 $0 $267 $1,602 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $48 $38 $0 $86 $15 $0 $20 $122 $0 
 Subtotal $0 $48 $38 $0 $86 $15 $0 $20 $122 $0 
 Total $171,489 $33,095 $93,884 $0 $298,468 $52,232 $22,148 $74,570 $447,417 $411

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
116 
Exhibit 6-32. Owners’ costs for cement cases with FGD and SCR 
Description $/1,000  $/tonnes/yr (CO2) $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 99% Capture 90% Capture 
6 Months All Labor $2,484 $2 $2,420 $2 
1-Month Maintenance Materials $436 $0 $421 $0 
1-Month Non-Fuel Consumables $366 $0 $349 $0 
1-Month Waste Disposal $11 $0 $11 $0 
25% of 1-Month Fuel Cost at 100% CF $391 $0 $355 $0 
2% of TPC $9,269 $8 $8,948 $8 
Total $12,958 $11 $12,505 $11 
Inventory Capital 99% Capture 90% Capture 
60-day supply of fuel and consumables at 100% CF $3,768 $3 $3,457 $3 
0.5% of TPC (spare parts) $2,317 $2 $2,237 $2 
Total $6,086 $5 $5,694 $5 
Other Costs 99% Capture 90% Capture 
Initial Cost for Catalyst and Chemicals $0 $0 $0 $0 
Land $30 $0 $30 $0 
Other Owner's Costs $69,521 $58 $67,113 $62 
Financing Costs $12,514 $10 $12,080 $11 
TOC $564,581 $471 $544,839 $500 
TASC Multiplier (Cement, 33 year) 1.054  1.054   
TASC $594,983 $497 $574,178 $527

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
117 
Exhibit 6-33. Initial and annual O&M costs for cement greenfield site with FGD and SCR at 99 percent capture 
Case:  Cement with FGD and SCR Cost Base: Dec 2018 
Representative Plant Size:  1.3 M tonnes/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $0.84 
Maintenance Labor:     $2,966,225 $2.48 
Administrative & Support Labor:     $993,658 $0.83 
Property Taxes and Insurance:     $9,269,455 $7.74 
Total:     $14,237,746 $11.89 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $4,449,338 $4.37 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 775 $1.90 $0 $457,112 $0.45 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 2.6 $550.00 $0 $440,049 $0.43 
SCR Catalyst (ft3):  w/equip.  0.0 $150.00 $0 $104,464 $0.10 
CO2 Capture System ChemicalsA: Proprietary $1,215,644 $1.19 
Triethylene Glycol (gal): w/equip. 240 $6.80 $0 $507,172 $0.50 
Limestone (ton): 0 0 $22.00 $0 $0 $0.00 
Ammonia (19 wt%, ton): 0.00 10.8 $300.00 $0 $1,008,681 $0.99 
Subtotal:    $0 $3,733,121 $3.67 
Waste Disposal 
Triethylene Glycol (gal):  240 $0.35 $0 $26,104 $0.03 
Thermal Reclaimer Unit Waste (ton)   0.69 $38.00 $0 $8,077 $0.01 
SCR Catalyst (ft3):   0 $2.50 $0 $1,741 $0.00 
Prescrubber Blowdown Waste (ton)   6.7 $38.00 $0 $78,627 $0.08 
Subtotal:    $0 $114,550 $0.11 
Variable Operating Costs Total:    $0 $8,297,009 $8.15 
Fuel Cost 
Natural Gas (MMBtu) 0 11,625 $4.42 $0 $15,941,580 $15.66 
Total:    $0 $15,941,580 $15.66 
ACO2 capture system chemicals includes NaOH and Cansolv solvent

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
118 
Exhibit 6-34. Initial and annual O&M costs for cement greenfield site with FGD and SCR at 90 percent capture 
Case:  Cement with FGD and SCR Cost Base: Dec 2018 
Representative Plant Size:  1.3 M tonnes/year  Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 2.3  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 2.3  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $1,008,407 $0.93 
Maintenance Labor:     $2,863,470 $2.63 
Administrative & Support Labor:     $967,969 $0.89 
Property Taxes and Insurance:     $8,948,343 $8.22 
Total:     $13,788,190 $12.66 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $4,295,205 $4.64 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 717 $1.90 $0 $422,931 $0.46 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 2.4 $550.00 $0 $410,207 $0.44 
SCR Catalyst (ft3):  w/equip.  0.0 $150.00 $0 $104,464 $0.11 
CO2 Capture System ChemicalsA: Proprietary $1,152,997 $1.25 
Triethylene Glycol (gal): w/equip. 219 $6.80 $0 $461,270 $0.50 
Limestone (ton): 0 0 $22.00 $0 $0 $0.00 
Ammonia (19 wt%, ton): 0.00 10.8 $300.00 $0 $1,008,681 $1.09 
Subtotal:    $0 $3,560,548 $3.85 
Waste Disposal 
Triethylene Glycol (gal):  219 $0.35 $0 $23,742 $0.03 
Thermal Reclaimer Unit Waste (ton)   0.65 $38.00 $0 $7,713 $0.01 
SCR Catalyst (ft3):   0 $2.50 $0 $1,741 $0.00 
Prescrubber Blowdown Waste (ton)   6.7 $38.00 $0 $78,627 $0.08 
Subtotal:    $0 $111,823 $0.12 
Variable Operating Costs Total:    $0 $7,967,577 $8.61 
Fuel Cost 
Natural Gas (MMBtu) 0 10,569 $4.42 $0 $14,493,467 $15.66 
Total:    $0 $14,493,467 $15.66 
ACO2 capture system chemicals includes NaOH and Cansolv solvent

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
119 
The COC for the greenfield FGD + SCR sensitivity cases at 99 and 90 percent capture are 
presented in Exhibit 6-35 alongside corresponding values for the base case cement plants. 
Exhibit 6-35. COC for 1.3 M tonnes/year cement greenfield cases (base cases and FGD + SCR cases)  
 COC at 99 percent capture, $/tonne CO2 COC at 90 percent capture, $/tonne CO2 
Component Base Case FGD + SCR Case Base Case FGD + SCR Case 
Capital 21.8 29.7 22.8 31.5 
Fixed 10.6 14.0 11.1 14.9 
Variable 5.9 8.2 6.1 8.6 
Purchased Power and Fuel 22.6 22.9 22.6 23.0 
Total COC 60.8 74.8 62.7 78.0 
 
The result of this sensitivity is that the total COC increases by $14.0/tonne CO2 and $15.3/tonne 
CO2 for 99 and 90 percent capture, respectively, with the addition of FGD and SCR systems for 
flue gas treating prior to AGR. At $78.0/tonne CO2, this cement sensitivity case with 90 percent 
capture is the highest COC of any of the processes considered in this report. This COC sensitivity 
is an approximation, as actual plant SOx/NOx concentrations were not available, and it is not 
clear whether this sensitivity would be common occurrence in U.S. cement plants, or a special 
isolated case due to raw materials used in a specific plant or region. 
6.2.11 Cement Conclusion 
The low purity CO2 stream produced in a cement plant results in a higher COC when compared 
to the high purity cases evaluated in this report, but the quantity of CO2 to be captured from 
such a process makes them attractive industrial processes for CCS as it would represent a 
significant GHG reduction. A CO2 capture and compression system for a 1.3 M tonnes/year 
cement plant was modeled to estimate the COC of capturing CO2 from the kiln off-gas. The 
results showed the COC of CO2 to be $60.8/tonne CO2 and $62.7/tonne CO2 for a greenfield site 
with 99 and 90 percent capture, respectively. For a retrofit application, the COC is $62.4/tonne 
CO2 and $64.3/tonne CO2 for 99 and 90 percent capture, respectively. The small disparities 
between greenfield and retrofit cases are the result of unknown difficulties required for a 
retrofit installation versus a greenfield application as discussed in Section 3.3, assuming 
adequate plot plan space for the retrofit case exists.  
The plant size sensitivity showed that as plant size decreased from 1.5 M tonnes/year to 0.5 M 
tonnes/year of cement production, the COC increased by $15.0/tonne CO2 and $15.8/tonne 
CO2, for 99 and 90 percent capture, respectively. As the plant size is decreased, less CO2 is 
produced, and economies of scale are lost, resulting in a higher COC. As demonstrated by the 
resulting COCs and the sensitivity analysis, the normalized cost of 99 percent CO2 capture is less 
than that of 90 percent capture.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
120 
For plants with SOx and/or NOx contaminants above that which is acceptable at the inlet of the 
AGR, an FGD and/or SCR system would be required to purify the stream before entering the CO2 
capture unit. An approximation of the additional cost of adding these systems showed an 
increase in greenfield COC by 23–25 percent. This approximation does not account for actual 
SOx/NOx concentrations in the kiln off-gas, and could be substantially higher or lower, 
depending on off-gas conditions and specific requirements of the AGR system deployed. 
6.3 IRON/STEEL 
According to the Environmental Protection Agency, in 2019 the industrial sector emitted 1.51 B 
tonnes of CO2, representing 23 percent of U.S. GHG emissions. [50] The Iron and Steel industry 
accounted for 4.8 percent or about 72 M tonnes of CO2 emissions in 2019. [6] Due to the large 
amounts of emissions available for capture from the iron and steel industry, these facilities 
present a great opportunity for the consideration of industrial decarbonization. 
6.3.1 Size Range 
According to the World Steel Association, there were 132 steel plants in the United States, 
accounting for approximately 86.6 M tonnes of steel production in 2018. Of these 86.6 M 
tonnes of steel produced, 32 percent was produced using an electric arc furnace (EAF) and the 
balance was produced using the more traditional BOF. [51] The main difference between the 
EAF and BOF processes involves the raw materials used as inputs as well as the furnace design.  
The resulting steel product from an EAF process contains approximately 100 percent recycled 
steel, whereas the BOF product contains 25 percent recycled steel on average. [51] The 
utilization of scrap steel results in lower CO2 emissions for an EAF process (0.6–0.9 tonne CO2 
per tonne steel) versus the BOF process (2.2 tonne CO2 per tonne steel). [52] The combination 
of generally smaller EAF plants and lower concentration of EAF plant CO2 emissions projects to a 
higher COC from an EAF process. Therefore, this study focuses on CO2 capture from BOF process 
steel plants. The total production capacity, as given by the World Steel Association for BOF 
plants in the United States in 2018, was 58.9 M tonnes. [51] 
6.3.2 CO2 Point Sources 
A study by Wiley, et al., (“Wiley Study”) published in 2010, assessed the opportunities for CO2 
capture in Australian iron and steel mills. [52] The Wiley Study utilized stream data from an 
Australian BOF steel mill, and within the base plant, the largest source of CO2 comes from the 
top gas of the blast furnace as is typical in an integrated steel mill; however, this stream is not 
directly vented. Instead, the blast furnace gas is cleaned and used in the plant as low-grade fuel, 
and instead of having a high-content CO2 point source from the blast furnace gas, the CO2 is 
distributed throughout the plant as smaller CO2 point sources. The resulting CO2 point sources 
available to be captured include the power plant stack (PPS), coke oven gas (COG), blast furnace 
stove (BFS), sinter stack, blown oxygen steelmaking stack, hot strip mill stack, plate mill stack, 
and lime kiln, based on the configuration detailed in the Wiley Study. [52] The three highest CO2 
concentrations of these point sources are the COG at 27 volume percent, the BFS at 21 volume 
percent, and the PPS at 23 volume percent.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
121 
Of the eight CO2 point sources listed by the Wiley Study, five have CO2 concentrations that 
would have capture costs comparable to those in a typical coal-fired power plant flue gas 
stream and are not included in this analysis. Only the three higher CO2 concentration streams, 
the PPS, COG, and BFS are evaluated, as shown in Exhibit 6-36. 
Exhibit 6-36. BOF iron and steel plant characteristics [52] 
Description PPS COG BFS 
CO2 Emitted/Tonne Steel produced 0.74 0.35 0.39 
Pressure (psia) 14.7 14.7 14.7 
Temperature (°F) 572 212 572 
Composition (vol %) 
N2 67.00 67.00 68.00 
H2O 8.00 5.00 10.00 
CO2 23.00 27.00 21.00 
O2 1.00 1.00 1.00 
 
Personal communication with a former U.S. Steel Braddock, PA, facility employee indicated that 
while the coke ovens are approximately five miles from the blast furnace, the COG is circulated 
back to the blast furnace to preheat the incoming air. Therefore, these two streams are located 
relatively close to one another and may be combined. Exhibit 6-37 is a simplified BFD of the plot 
plan description of the Braddock steel mill.  
Exhibit 6-37. Braddock steel mill plot plan 
 
6.3.3 Design Input and Assumptions 
The following is a list of design inputs and assumptions made specific to the iron/steel process 
for the purpose of this study: 
 
COKE 
OVENS
COG POWER 
PLANT STACK
BLAST 
FURNACECOKE OVEN GAS FOR PREHEATING AIR
5 Mile Distance
Distance between COG PPS and BFS PPS too 
large to be combined – Must be treated separately
COG PPS
 GAS
COG/BFS

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
122 
• The representative BOF integrated steel mill has a production capacity of 2.54 M 
tonnes/year 
• The CO2 generated is 3,738,928 tonnes CO2/year at 100 percent CF  
• There are three high purity point sources: COG, BFS, and COG PPS. The COG and BFS will 
be combined into one stream due to plot plan and totals 1,864,388 tonnes CO2/year (at 
100 percent CF); COG PPS will utilize its own separation and compression facility and 
generates 1,874,540 tonnes CO2/year at 100 percent CF 
• Since there are two separate capture systems, 4.6 operators are considered (i.e., 2.3 
operators per capture system) 
• As a low purity source, separation, compression, and cooling are required. Separation is 
accomplished using a Cansolv AGR unit 
• CO2 capture rates of 90 percent and 99 percent are evaluated 
• The CO2 quality is based on the EOR pipeline standard as mentioned in the NETL QGESS 
for CO2 Impurity Design Parameters [1] 
6.3.4 CO2 Capture System 
The COG/BFS and COG PPS stream CO2 concentrations require purification before compression 
to meet EOR pipeline standards. The purification system used is Shell’s Cansolv post-combustion 
capture system discussed in Section 4.2.1. Steam for solvent regeneration is provided by the 
industrial boiler discussed in Section 4.3. A separate capture unit, boiler, and ancillary 
equipment is modeled for each COG/BFS and COG PPS stream. One integrally geared centrifugal 
compression train as discussed in Section 4.1.2 is employed for the COG/BFS stream and a 
second is used to compress the COG PPS stream. Costs for the compressors are scaled based on 
product CO2 flow. 
6.3.5 BFD, Stream Table, and Performance Summary 
For the COG/BFS case, the COG stream and BFS stream are mixed and sent to the CO2 capture 
system. Water and solids recovered from the AGR process are sent to waste treatment. The CO2 
stream is then compressed with interstage cooling and after-cooled before reaching the EOR 
pipeline. Exhibit 6-38 shows the BFD for this process, and Exhibit 6-39 and Exhibit 6-40 show the 
stream table for this process with 99 percent and 90 percent capture, respectively.  
Exhibit 6-38. CO2 capture BFD for COG/BFS 
   
HX Desired Usage
2
Compressor
Cansolv 
CO2 
Capture 
System
5 6
BFS
1COG
Stream 
Mixer 3 4
7

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
123 
Exhibit 6-39. Iron/steel COG/BFS stream table with 99 percent capture 
 1 2 3 4 5 6 7 
V-L Mole Fraction              
AR 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2700 0.2100 0.2346 0.9879 0.9995 0.9995 0.0034 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0500 0.1000 0.0795 0.0121 0.0005 0.0005 0.0237 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6700 0.6800 0.6759 0.0000 0.0000 0.0000 0.9588 
O2 0.0100 0.0100 0.0100 0.0000 0.0000 0.0000 0.0141 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 
  
            
 
V-L Flowrate (kgmol/hr) 8,443 12,173 20,616 4,845 4,788 4,788 14,533 
V-L Flowrate (kg/hr) 269,106 370,224 639,331 211,692 210,637 210,637 405,309 
Temperature (°C) 100 300 219 31 80 30 38 
Pressure (MPa, abs) 0.10 0.1 0.1 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,700 3,593 3,638 8,793 8,758 8,755 309.0 
Aspen Plus Enthalpy (kJ/kg)B -3,638 -3,217 -3,394 -8,961 -9,042 -9,195 -240.1 
Density (kg/m3) 1.0 0.6 0.8 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.9 30.4 31.0 43.7 44.0 44.0 27.9 
 
      
 
V-L Flowrate (lbmol/hr) 18,613 26,837 45,450 10,681 10,555 10,555 32,041 
V-L Flowrate (lb/hr) 593,278 816,205 1,409,483 466,701 464,375 464,375 893,553 
Temperature (°F) 212 572 426 88 177 86 100 
Pressure (psia) 14.7 14.7 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,591 1,545 1,564 3,780 3,765 3,764 132.8 
Aspen Plus Enthalpy (Btu/lb)B -1,564 -1,383 -1,459 -3,852 -3,887 -3,953 -103.2 
Density (lb/ft3) 0.065 0.040 0.048 0.217 27.0 39.3 0.069 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
124 
Exhibit 6-40. Iron/steel COG/BFS stream table with 90 percent capture 
 1 2 3 4 5 6 7 
V-L Mole Fraction              
AR 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2700 0.2100 0.2346 0.9881 0.9995 0.9995 0.0322 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0500 0.1000 0.0795 0.0119 0.0005 0.0005 0.0237 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6700 0.6800 0.6759 0.0000 0.0000 0.0000 0.9303 
O2 0.0100 0.0100 0.0100 0.0000 0.0000 0.0000 0.0137 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 
               
V-L Flowrate (kgmol/hr) 8,443 12,173 20,616 4,405 4,354 4,354 14,978 
V-L Flowrate (kg/hr) 269,106 370,224 639,331 192,516 191,573 191,573 424,582 
Temperature (°C) 100 300 219 31 80 30 38 
Pressure (MPa, abs) 0.10 0.1 0.1 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,700 3,593 3,638 8,793 8,758 8,755 691.0 
Aspen Plus Enthalpy (kJ/kg)B -3,638 -3,217 -3,394 -8,960 -9,042 -9,195 -636.8 
Density (kg/m3) 1.0 0.6 0.8 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.9 30.4 31.0 43.7 44.0 44.0 28.3 
 
      
 
V-L Flowrate (lbmol/hr) 18,613 26,837 45,450 9,712 9,599 9,599 33,021 
V-L Flowrate (lb/hr) 593,278 816,205 1,409,483 424,424 422,347 422,347 936,044 
Temperature (°F) 212 572 426 88 177 86 100 
Pressure (psia) 14.7 14.7 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,591 1,545 1,564 3,780 3,765 3,764 297.1 
Aspen Plus Enthalpy (Btu/lb)B -1,564 -1,383 -1,459 -3,852 -3,887 -3,953 -273.8 
Density (lb/ft3) 0.065 0.040 0.048 0.217 27.0 39.3 0.070 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
In the same manner, the COG PPS stream is sent to the Cansolv CO2 capture system. Water and 
solids recovered from the AGR process are sent to waste treatment. The CO2 stream is then 
compressed with interstage cooling and after-cooled before reaching the EOR pipeline. Exhibit

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
125 
6-41 shows the BFD for this process, and Exhibit 6-42 and Exhibit 6-43 show the stream table for 
this process with 99 percent and 90 percent capture, respectively. 
Exhibit 6-41. CO2 capture BFD for COG PPS 
 
Exhibit 6-42. Iron/steel COG PPS stream table with 99 percent capture 
 1 2 3 4 5 
V-L Mole Fraction          
AR 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2323 0.9875 0.9995 0.9995 0.0034 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0808 0.0125 0.0005 0.0005 0.0242 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6768 0.0000 0.0000 0.0000 0.9581 
O2 0.0101 0.0000 0.0000 0.0000 0.0142 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 
  
        
 
V-L Flowrate (kgmol/hr) 20,931 4,873 4,814 4,814 14,785 
V-L Flowrate (kg/hr) 648,081 212,873 211,784 211,784 412,236 
Temperature (°C) 300 31 80 30 38 
Pressure (MPa, abs) 0.1 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,630 8,794 8,758 8,755 314.2 
Aspen Plus Enthalpy (kJ/kg)B -3,292 -8,961 -9,042 -9,195 -244.5 
Density (kg/m3) 0.7 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.0 43.7 44.0 44.0 27.9 
 
    
 
V-L Flowrate (lbmol/hr) 46,145 10,743 10,612 10,612 32,595 
V-L Flowrate (lb/hr) 1,428,775 469,304 466,905 466,905 908,825 
2 3 HX Desired UsageCompressor
Cansolv 
CO2 
Capture 
System
4COG PPS 1 2 3
5

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
126 
 1 2 3 4 5 
V-L Mole Fraction          
Temperature (°F) 572 88 177 86 100 
Pressure (psia) 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,561 3,781 3,765 3,764 135.1 
Aspen Plus Enthalpy (Btu/lb)B -1,415 -3,853 -3,887 -3,953 -105.1 
Density (lb/ft3) 0.041 0.217 27.0 39.3 0.069 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
Exhibit 6-43. Iron/steel COG PPS stream table with 90 percent capture 
 1 2 3 4 5 
V-L Mole Fraction          
AR 0.0000 0.0000 0.0000 0.0000 0.0000 
CH4 0.0000 0.0000 0.0000 0.0000 0.0000 
CO 0.0000 0.0000 0.0000 0.0000 0.0000 
CO2 0.2323 0.9878 0.9995 0.9995 0.0319 
SO2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2 0.0000 0.0000 0.0000 0.0000 0.0000 
H2O 0.0808 0.0122 0.0005 0.0005 0.0243 
H2S 0.0000 0.0000 0.0000 0.0000 0.0000 
N2 0.6768 0.0000 0.0000 0.0000 0.9300 
O2 0.0101 0.0000 0.0000 0.0000 0.0138 
Total 1.0000 1.0000 1.0000 1.0000 1.0000 
           
V-L Flowrate (kgmol/hr) 20,931 4,431 4,378 4,378 15,232 
V-L Flowrate (kg/hr) 648,081 193,589 192,617 192,617 431,610 
Temperature (°C) 300 31 80 30 38 
Pressure (MPa, abs) 0.1 0.2 15.3 15.3 0.1 
Steam Table Enthalpy (kJ/kg)A 3,630 8,793 8,758 8,755 691.6 
Aspen Plus Enthalpy (kJ/kg)B -3,292 -8,961 -9,042 -9,195 -636.6 
Density (kg/m3) 0.7 3.5 432.5 630.1 1.1 
V-L Molecular Weight 31.0 43.7 44.0 44.0 28.3 
 
    
 
V-L Flowrate (lbmol/hr) 46,145 9,768 9,652 9,652 33,581 
V-L Flowrate (lb/hr) 1,428,775 426,791 424,647 424,647 951,538

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
127 
 1 2 3 4 5 
V-L Mole Fraction          
Temperature (°F) 572 88 177 86 100 
Pressure (psia) 14.7 28.9 2,216.9 2,214.7 14.8 
Steam Table Enthalpy (Btu/lb)A 1,561 3,781 3,765 3,764 297.3 
Aspen Plus Enthalpy (Btu/lb)B -1,415 -3,853 -3,887 -3,953 -273.7 
Density (lb/ft3) 0.041 0.217 27.0 39.3 0.070 
ASteam table reference conditions are 32.02°F & 0.089 psia 
BAspen thermodynamic reference state is the component’s constituent elements in an ideal gas state at 25°C and 1 atm 
The performance summary for both 90 and 99 percent capture cases in the COG/BFS section of 
the steel mill is provided in Exhibit 6-44, while that of the COG PPS section is shown in Exhibit 
6-45.  
Exhibit 6-44. Performance summary for iron/steel COG/BFS section 
Performance Summary 
Item 2.54 M tonnes steel/year with 90 percent CO2 capture (kWe) 2.54 M tonnes steel/year with 99 percent CO2 capture (kWe) 
CO2 Capture Auxiliaries 4,800 5,400 
Steam Boiler Auxiliaries 510 560 
CO2 Compressor 14,660 16,120 
Circulating Water Pumps 1,480 1,610 
Cooling Tower Fans 770 830 
Total Auxiliary Load 22,220 24,520 
Exhibit 6-45. Performance summary for iron/steel COG PPS section 
Performance Summary 
Item 2.54 M tonnes steel/year with 90 percent CO2 capture (kWe) 2.54 M tonnes steel/year with 99 percent CO2 capture (kWe) 
CO2 Capture Auxiliaries 4,900 5,400 
Steam Boiler Auxiliaries 520 570 
CO2 Compressor 14,750 16,210 
Circulating Water Pumps 1,490 1,620 
Cooling Tower Fans 770 830 
Total Auxiliary Load 22,430 24,630

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
128 
6.3.6 Capture Integration 
The BOF process integrated steel mill makes use of the BFS and COG as low-grade fuel for 
electricity generation. Due to this set-up, integrating equipment with additional auxiliary needs, 
such as power, steam, or cooling loads for the capture system, into the existing plant systems 
may be capacity limited. 
The cooling water system considered in this study is a stand-alone unit; however, there is 
potential to integrate make-up water to feed or partially feed the cooling system thereby 
reducing the unit’s size or replacing it completely with a simple HX. This would be evaluated on 
case-by-case basis depending on the size of the plant, its layout, and size of the plant’s current 
cooling system, and such an evaluation is outside of the scope of this study. 
6.3.7 Power Source 
The compressor power consumption for the 90 and 99 percent capture cases in the COG/BFS 
section of the plant are 14.66 MW and 16.12 MW , respectively. The compressor power 
consumption for the 90 and 99 percent capture cases in the COG PPS section of the plant are 
14.75 MW and 16.21 MW , respectively. Power consumption estimates for the cooling water 
system in each case were scaled as described in Section 4.4. The total power requirements were 
calculated to be 22.22 MW and 24.52 MW for the 90 and 99 percent capture rates in the 
COG/BFS section, respectively, while the total power requirements were calculated to be 22.43 
MW and 24.63 MW for the 90 and 99 percent capture rates in the COG PPS section, 
respectively. These estimates include all power required by the compression train, cooling water 
system, and Cansolv capture unit. Purchased power cost is estimated at a rate of $60/MWh as 
discussed in Section 3.1.2.4. To satisfy the steam requirements of the AGR system, an industrial 
boiler was modeled, and fuel consumption costs were estimated at a rate of $4.42/MMBtu as 
discussed in Section 3.1.2.4. 
6.3.8 Economic Analysis Results 
The economic results of CO2 capture application in an iron/steel mill are presented in this 
section. Owner’s costs, capital costs, and O&M costs are calculated as discussed in Section 3.1. 
Retrofit costs were determined by applying a retrofit factor to TPC as discussed in Section 3.3. 
The retrofit TOC for the iron/steel case at 99 percent capture is $1,151 M, while for 90 percent 
capture, a retrofit TOC of $1,055 M is estimated. The corresponding retrofit COC for the 99 
percent and 90 percent capture cases are $65.4/tonne CO2 and $65.9/tonne CO2, respectively. 
Greenfield cost estimates for the iron/steel case are not estimated, as BOF steel mills are no 
longer being constructed; thus, any capture application in a BOF mill as evaluated in this study 
would be implemented as a retrofit. Capital and O&M costs for each section (COG/BFS and COG 
PPS) are presented separately (Exhibit 6-47 through Exhibit 6-50), while owners costs and COCs 
are presented in whole for 99 and 90 percent capture cases in Exhibit 6-46 and Exhibit 6-53, 
respectively. 
It should be noted that line-item capital costs were not estimated for retrofit cases, as the 
retrofit costs were estimated by applying a retrofit factor to the TPC of a greenfield plant as 
described in Section 3.3. As such, the account specific capital costs reported in this section are

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
129 
for a hypothetical greenfield plant but could be estimated for each account by applying a 
retrofit factor TPC as described in Section 3.3. As some O&M and owner’s costs are estimated 
based on TPC, the retrofit TPC value was used to estimate the owner’s costs and O&M costs 
presented in Exhibit 6-46 through Exhibit 6-52; thus, those values are indicative of a retrofit 
installation.  
Exhibit 6-46. Owners’ costs for iron/steel retrofit cases 
Description $/1,000  $/tonnes/yr (CO2) $/1,000  $/tonnes/yr (CO2) 
Pre-Production Costs 99% Capture 90% Capture 
6 Months All Labor $5,095 $3 $4,776 $3 
1-Month Maintenance Materials $902 $0 $827 $0 
1-Month Non-Fuel Consumables $802 $0 $750 $0 
1-Month Waste Disposal $33 $0 $32 $0 
25% of 1-Month Fuel Cost at 100% CF $0 $0 $0 $0 
2% of TPC $19,171 $10 $17,151 $10 
Total $26,003 $14 $23,536 $14 
Inventory Capital     
60-day supply of fuel and consumables at 100% CF $1,327 $1 $1,243 $1 
0.5% of TPC (spare parts) $4,793 $3 $4,394 $3 
Total $6,120 $3 $5,637 $3 
Other Costs     
Initial Cost for Catalyst and Chemicals $0 $0 $0 $0 
Land $0 $0 $0 $0 
Other Owner's Costs $143,780 $78 $131,820 $78 
Financing Costs $25,880 $14 $23,728 $14 
TOC $1,160,313 $627 $1,063,524 $632 
TASC Multiplier (Iron/Steel, 33 year) 1.091   1.091   
TASC $1,266,188 $684 $1,160,567 $690

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
130 
Exhibit 6-47. Capital costs for iron/steel COG/BFS section retrofit with 99 percent capture  
Case: Iron/Steel COG/BFS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $886 $1,519 $760 $0 $3,165 $554 $0 $744 $4,463 $2 
3.2 Water Makeup & Pretreating  $2,239 $224 $1,269 $0 $3,732 $653 $0 $877 $5,263 $3 
3.3 Other Feedwater Subsystems $448 $147 $139 $0 $734 $128 $0 $173 $1,035 $1 
3.4 Industrial Boiler Package 
w/Deaerator $5,968 $0 $1,735 $0 $7,703 $1,348 $0 $1,810 $10,861 $6 
3.5 Other Boiler Plant Systems $108 $39 $99 $0 $246 $43 $0 $58 $347 $0 
3.6 NG Pipeline and Start-Up 
System $808 $35 $26 $0 $869 $152 $0 $204 $1,226 $1 
3.7 Waste Water Treatment 
Equipment $4,113 $0 $2,521 $0 $6,633 $1,161 $0 $1,559 $9,353 $5 
3.9 Miscellaneous Plant 
Equipment $109 $14 $56 $0 $179 $31 $0 $42 $253 $0 
 Subtotal $14,680 $1,979 $6,604 $0 $23,263 $4,071 $0 $5,467 $32,801 $18 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $81,899 $35,424 $74,391 $0 $191,714 $33,550 $32,591 $51,571 $309,426 $168 
5.4 CO2 Compression & Drying $22,324 $3,349 $7,464 $0 $33,136 $5,799 $0 $7,787 $46,722 $25 
5.5 CO2 Compressor Aftercooler $196 $31 $84 $0 $312 $55 $0 $73 $440 $0 
5.12 Gas Cleanup Foundations $0 $89 $78 $0 $166 $29 $0 $39 $234 $0 
 Subtotal $104,419 $38,893 $82,017 $0 $225,328 $39,432 $32,591 $59,470 $356,822 $193 
 7 Ductwork & Stack 
7.3 Ductwork $0 $2,303 $1,600 $0 $3,903 $683 $0 $917 $5,503 $3 
7.4 Stack $7,869 $0 $4,573 $0 $12,442 $2,177 $0 $2,924 $17,543 $10 
7.5 Duct & Stack Foundations $0 $176 $209 $0 $386 $68 $0 $91 $544 $0 
 Subtotal $7,869 $2,479 $6,382 $0 $16,731 $2,928 $0 $3,932 $23,590 $13 
 9 Cooling Water System 
9.1 Cooling Towers $1,990 $0 $615 $0 $2,605 $456 $0 $612 $3,673 $2 
9.2 Circulating Water Pumps $213 $0 $15 $0 $228 $40 $0 $54 $321 $0 
9.3 Circulating Water System Aux. $2,489 $0 $329 $0 $2,818 $493 $0 $662 $3,974 $2 
9.4 Circulating Water Piping $0 $1,151 $1,042 $0 $2,193 $384 $0 $515 $3,092 $2 
9.5 Make-up Water System $255 $0 $328 $0 $583 $102 $0 $137 $823 $0 
9.6 Component Cooling Water 
System $179 $0 $138 $0 $317 $55 $0 $74 $447 $0 
9.7 Circulating Water System 
Foundations $0 $124 $207 $0 $331 $58 $0 $78 $467 $0 
 Subtotal $5,126 $1,275 $2,674 $0 $9,076 $1,588 $0 $2,133 $12,797 $7 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,192 $0 $274 $0 $3,466 $606 $0 $814 $4,887 $3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
131 
Case: Iron/Steel COG/BFS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
11.3 Switchgear & Motor Control  $4,955 $0 $860 $0 $5,815 $1,018 $0 $1,366 $8,199 $4 
11.4 Conduit & Cable Tray $0 $644 $1,856 $0 $2,500 $438 $0 $588 $3,526 $2 
11.5 Wire & Cable $0 $1,706 $3,049 $0 $4,755 $832 $0 $1,117 $6,704 $4 
 Subtotal $8,147 $2,350 $6,039 $0 $16,535 $2,894 $0 $3,886 $23,315 $13 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $425 $340 $1,361 $0 $2,126 $372 $0 $500 $2,998 $2 
12.9 Other I&C Equipment $523 $0 $1,210 $0 $1,733 $303 $0 $407 $2,444 $1 
 Subtotal $948 $340 $2,571 $0 $3,859 $675 $0 $907 $5,441 $3 
 13 Improvements to Site 
13.1 Site Preparation $0 $29 $585 $0 $614 $107 $0 $144 $866 $0 
13.2 Site Improvements $0 $136 $181 $0 $317 $56 $0 $75 $447 $0 
13.3 Site Facilities $156 $0 $164 $0 $320 $56 $0 $75 $451 $0 
 Subtotal $156 $165 $930 $0 $1,251 $219 $0 $294 $1,764 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $65 $52 $0 $117 $20 $0 $28 $165 $0 
 Subtotal $0 $65 $52 $0 $117 $20 $0 $28 $165 $0 
 Total $141,345 $47,546 $107,269 $0 $296,160 $51,828 $32,591 $76,116 $456,696 $248 
Retrofit Values $310,968 $54,419 $34,221 $79,922 $479,530 $260 
Exhibit 6-48. Capital costs for iron/steel COG PPS retrofit with 99 percent capture  
Case: Iron/Steel COG PPS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $890 $1,525 $763 $0 $3,177 $556 $0 $747 $4,480 $2 
3.2 Water Makeup & Pretreating  $2,249 $225 $1,274 $0 $3,748 $656 $0 $881 $5,284 $3 
3.3 Other Feedwater Subsystems $450 $148 $140 $0 $738 $129 $0 $173 $1,040 $1 
3.4 Industrial Boiler Package 
w/Deaerator $5,998 $0 $1,744 $0 $7,741 $1,355 $0 $1,819 $10,915 $6 
3.5 Other Boiler Plant Systems $109 $40 $99 $0 $248 $43 $0 $58 $349 $0 
3.6 NG Pipeline and Start-Up System $811 $35 $26 $0 $872 $153 $0 $205 $1,229 $1 
3.7 Waste Water Treatment Equipment $4,144 $0 $2,540 $0 $6,683 $1,170 $0 $1,571 $9,424 $5 
3.9 Miscellaneous Plant Equipment $109 $14 $56 $0 $179 $31 $0 $42 $253 $0 
 Subtotal $14,759 $1,986 $6,641 $0 $23,387 $4,093 $0 $5,496 $32,975 $18 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $81,456 $35,233 $73,989 $0 $190,678 $33,369 $32,415 $51,292 $307,755 $166 
5.4 CO2 Compression & Drying $22,399 $3,360 $7,489 $0 $33,249 $5,819 $0 $7,813 $46,881 $25

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
132 
Case: Iron/Steel COG PPS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O.& Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
5.5 CO2 Compressor Aftercooler $197 $31 $85 $0 $313 $55 $0 $74 $442 $0 
5.12 Gas Cleanup Foundations $0 $98 $86 $0 $184 $32 $0 $43 $259 $0 
 Subtotal $104,053 $38,722 $81,649 $0 $224,424 $39,274 $32,415 $59,223 $355,337 $192 
 7 Ductwork & Stack 
7.3 Ductwork $0 $2,591 $1,800 $0 $4,391 $768 $0 $1,032 $6,191 $3 
7.4 Stack $7,877 $0 $4,577 $0 $12,455 $2,180 $0 $2,927 $17,561 $9 
7.5 Duct & Stack Foundations $0 $176 $210 $0 $386 $68 $0 $91 $544 $0 
 Subtotal $7,877 $2,767 $6,587 $0 $17,232 $3,016 $0 $4,049 $24,297 $13 
 9 Cooling Water System 
9.1 Cooling Towers $1,998 $0 $618 $0 $2,616 $458 $0 $615 $3,689 $2 
9.2 Circulating Water Pumps $214 $0 $15 $0 $229 $40 $0 $54 $323 $0 
9.3 Circulating Water System Aux. $2,498 $0 $330 $0 $2,828 $495 $0 $665 $3,988 $2 
9.4 Circulating Water Piping $0 $1,155 $1,046 $0 $2,201 $385 $0 $517 $3,103 $2 
9.5 Make-up Water System $256 $0 $329 $0 $585 $102 $0 $137 $825 $0 
9.6 Component Cooling Water System $180 $0 $138 $0 $318 $56 $0 $75 $448 $0 
9.7 Circulating Water System 
Foundations $0 $125 $207 $0 $332 $58 $0 $78 $468 $0 
 Subtotal $5,146 $1,280 $2,684 $0 $9,110 $1,594 $0 $2,141 $12,845 $7 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,198 $0 $274 $0 $3,472 $608 $0 $816 $4,896 $3 
11.3 Switchgear & Motor Control  $4,965 $0 $861 $0 $5,826 $1,020 $0 $1,369 $8,215 $4 
11.4 Conduit & Cable Tray $0 $645 $1,860 $0 $2,505 $438 $0 $589 $3,532 $2 
11.5 Wire & Cable $0 $1,709 $3,055 $0 $4,764 $834 $0 $1,120 $6,718 $4 
 Subtotal $8,163 $2,355 $6,051 $0 $16,568 $2,899 $0 $3,893 $23,361 $13 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $425 $340 $1,362 $0 $2,127 $372 $0 $500 $3,000 $2 
12.9 Other I&C Equipment $523 $0 $1,211 $0 $1,734 $303 $0 $408 $2,445 $1 
 Subtotal $948 $340 $2,573 $0 $3,861 $676 $0 $907 $5,445 $3 
 13 Improvements to Site 
13.1 Site Preparation $0 $29 $586 $0 $615 $108 $0 $144 $867 $0 
13.2 Site Improvements $0 $137 $181 $0 $317 $56 $0 $75 $448 $0 
13.3 Site Facilities $156 $0 $164 $0 $320 $56 $0 $75 $451 $0 
 Subtotal $156 $166 $931 $0 $1,252 $219 $0 $294 $1,766 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $66 $52 $0 $117 $21 $0 $28 $166 $0 
 Subtotal $0 $66 $52 $0 $117 $21 $0 $28 $166 $0 
 Total $141,103 $47,682 $107,167 $0 $295,952 $51,792 $32,415 $76,032 $456,190 $246 
Retrofit Values $310,749 $54,381 $34,036 $79,833 $479,000 $258

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
133 
Exhibit 6-49. Capital costs for iron/steel COG/BFS section retrofit with 90 percent capture  
Case: Iron/Steel COG/BFS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $830 $1,423 $711 $0 $2,964 $519 $0 $697 $4,179 $2 
3.2 Water Makeup & Pretreating  $2,116 $212 $1,199 $0 $3,527 $617 $0 $829 $4,972 $3 
3.3 Other Feedwater Subsystems $411 $135 $128 $0 $674 $118 $0 $158 $951 $1 
3.4 Industrial Boiler Package 
w/Deaerator $5,483 $0 $1,594 $0 $7,077 $1,238 $0 $1,663 $9,979 $6 
3.5 Other Boiler Plant Systems $100 $36 $90 $0 $226 $40 $0 $53 $319 $0 
3.6 NG Pipeline and Start-Up 
System $772 $33 $25 $0 $830 $145 $0 $195 $1,170 $1 
3.7 Waste Water Treatment 
Equipment $3,935 $0 $2,412 $0 $6,346 $1,111 $0 $1,491 $8,948 $5 
3.9 Miscellaneous Plant 
Equipment $107 $14 $54 $0 $175 $31 $0 $41 $247 $0 
 Subtotal $13,753 $1,853 $6,214 $0 $21,819 $3,818 $0 $5,127 $30,765 $18 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $71,707 $31,016 $65,134 $0 $167,857 $29,375 $28,536 $45,154 $270,921 $161 
5.4 CO2 Compression & Drying $21,067 $3,160 $7,044 $0 $31,272 $5,473 $0 $7,349 $44,093 $26 
5.5 CO2 Compressor Aftercooler $182 $29 $78 $0 $288 $50 $0 $68 $406 $0 
5.12 Gas Cleanup Foundations $0 $89 $78 $0 $166 $29 $0 $39 $234 $0 
 Subtotal $92,956 $34,294 $72,333 $0 $199,583 $34,927 $28,536 $52,609 $315,655 $188 
 7 Ductwork & Stack 
7.3 Ductwork $0 $2,303 $1,600 $0 $3,903 $683 $0 $917 $5,503 $3 
7.4 Stack $7,883 $0 $4,581 $0 $12,464 $2,181 $0 $2,929 $17,575 $10 
7.5 Duct & Stack Foundations $0 $175 $208 $0 $384 $67 $0 $90 $541 $0 
 Subtotal $7,883 $2,478 $6,389 $0 $16,751 $2,931 $0 $3,936 $23,619 $14 
 9 Cooling Water System 
9.1 Cooling Towers $1,874 $0 $580 $0 $2,454 $429 $0 $577 $3,460 $2 
9.2 Circulating Water Pumps $199 $0 $14 $0 $213 $37 $0 $50 $301 $0 
9.3 Circulating Water System Aux. $2,370 $0 $314 $0 $2,684 $470 $0 $631 $3,784 $2 
9.4 Circulating Water Piping $0 $1,096 $993 $0 $2,089 $365 $0 $491 $2,945 $2 
9.5 Make-up Water System $246 $0 $316 $0 $562 $98 $0 $132 $792 $0 
9.6 Component Cooling Water 
System $171 $0 $131 $0 $302 $53 $0 $71 $426 $0 
9.7 Circulating Water System 
Foundations $0 $119 $198 $0 $317 $55 $0 $74 $446 $0 
 Subtotal $4,860 $1,215 $2,544 $0 $8,619 $1,508 $0 $2,026 $12,153 $7 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,060 $0 $262 $0 $3,322 $581 $0 $781 $4,684 $3

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
134 
Case: Iron/Steel COG/BFS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
11.3 Switchgear & Motor Control  $4,750 $0 $824 $0 $5,574 $975 $0 $1,310 $7,859 $5 
11.4 Conduit & Cable Tray $0 $617 $1,779 $0 $2,397 $419 $0 $563 $3,380 $2 
11.5 Wire & Cable $0 $1,635 $2,923 $0 $4,558 $798 $0 $1,071 $6,427 $4 
 Subtotal $7,810 $2,253 $5,789 $0 $15,851 $2,774 $0 $3,725 $22,350 $13 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $420 $336 $1,343 $0 $2,099 $367 $0 $493 $2,960 $2 
12.9 Other I&C Equipment $516 $0 $1,195 $0 $1,711 $299 $0 $402 $2,413 $1 
 Subtotal $936 $336 $2,538 $0 $3,810 $667 $0 $895 $5,372 $3 
 13 Improvements to Site 
13.1 Site Preparation $0 $28 $574 $0 $602 $105 $0 $142 $849 $1 
13.2 Site Improvements $0 $134 $177 $0 $311 $54 $0 $73 $438 $0 
13.3 Site Facilities $153 $0 $161 $0 $314 $55 $0 $74 $442 $0 
 Subtotal $153 $162 $912 $0 $1,227 $215 $0 $288 $1,730 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $62 $49 $0 $112 $20 $0 $26 $158 $0 
 Subtotal $0 $62 $49 $0 $112 $20 $0 $26 $158 $0 
 Total $128,351 $42,652 $96,769 $0 $267,772 $46,860 $28,536 $68,634 $411,802 $245 
Retrofit Values $281,161 $49,203 $29,963 $72,065 $432,392 $258 
Exhibit 6-50. Capital costs for iron/steel COG PPS retrofit with 90 percent capture  
Case: Iron/Steel COG PPS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
 3 Feedwater & Miscellaneous BOP Systems 
3.1 Feedwater System $833 $1,428 $714 $0 $2,975 $521 $0 $699 $4,195 $2 
3.2 Water Makeup & Pretreating  $2,125 $212 $1,204 $0 $3,541 $620 $0 $832 $4,993 $3 
3.3 Other Feedwater Subsystems $413 $136 $129 $0 $678 $119 $0 $159 $956 $1 
3.4 Industrial Boiler Package w/Deaerator $5,510 $0 $1,602 $0 $7,112 $1,245 $0 $1,671 $10,028 $6 
3.5 Other Boiler Plant Systems $100 $36 $91 $0 $227 $40 $0 $53 $321 $0 
3.6 NG Pipeline and Start-Up System $774 $33 $25 $0 $832 $146 $0 $196 $1,173 $1 
3.7 Waste Water Treatment Equipment $3,965 $0 $2,430 $0 $6,396 $1,119 $0 $1,503 $9,018 $5 
3.9 Miscellaneous Plant Equipment $107 $14 $54 $0 $175 $31 $0 $41 $247 $0 
 Subtotal $13,827 $1,860 $6,249 $0 $21,937 $3,839 $0 $5,155 $30,931 $18 
 5 Flue Gas Cleanup 
5.1 Cansolv CO2 Removal System $74,921 $32,406 $68,053 $0 $175,379 $30,691 $29,814 $47,177 $283,062 $168 
5.4 CO2 Compression & Drying $21,146 $3,172 $7,070 $0 $31,389 $5,493 $0 $7,376 $44,258 $26 
5.5 CO2 Compressor Aftercooler $182 $29 $78 $0 $289 $51 $0 $68 $408 $0

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
135 
Case: Iron/Steel COG PPS Section Estimate Type:  Conceptual 
Representative Plant Size:  2.54 M tonnes steel/year Cost Base: Dec 2018 
Item 
 No. Description Equipment Cost Material Cost Labor Bare Erected Cost Eng'g CM H.O. & Fee Contingencies Total Plant Cost Direct Indirect Process Project $/1,000 $/tonnes/yr (CO2) 
5.12 Gas Cleanup Foundations $0 $98 $86 $0 $184 $32 $0 $43 $259 $0 
 Subtotal $96,249 $35,705 $75,287 $0 $207,241 $36,267 $29,814 $54,665 $327,987 $194 
 7 Ductwork & Stack 
7.3 Ductwork $0 $2,591 $1,800 $0 $4,391 $768 $0 $1,032 $6,191 $4 
7.4 Stack $7,891 $0 $4,586 $0 $12,477 $2,183 $0 $2,932 $17,593 $10 
7.5 Duct & Stack Foundations $0 $175 $208 $0 $384 $67 $0 $90 $541 $0 
 Subtotal $7,891 $2,766 $6,594 $0 $17,252 $3,019 $0 $4,054 $24,325 $14 
 9 Cooling Water System 
9.1 Cooling Towers $1,882 $0 $582 $0 $2,465 $431 $0 $579 $3,475 $2 
9.2 Circulating Water Pumps $200 $0 $14 $0 $214 $37 $0 $50 $302 $0 
9.3 Circulating Water System Aux. $2,379 $0 $315 $0 $2,693 $471 $0 $633 $3,797 $2 
9.4 Circulating Water Piping $0 $1,100 $996 $0 $2,096 $367 $0 $493 $2,955 $2 
9.5 Make-up Water System $247 $0 $317 $0 $563 $99 $0 $132 $794 $0 
9.6 Component Cooling Water System $171 $0 $132 $0 $303 $53 $0 $71 $427 $0 
9.7 Circulating Water System 
Foundations $0 $119 $198 $0 $318 $56 $0 $75 $448 $0 
 Subtotal $4,879 $1,219 $2,553 $0 $8,652 $1,514 $0 $2,033 $12,199 $7 
 11 Accessory Electric Plant 
11.2 Station Service Equipment $3,072 $0 $264 $0 $3,336 $584 $0 $784 $4,703 $3 
11.3 Switchgear & Motor Control  $4,769 $0 $827 $0 $5,597 $979 $0 $1,315 $7,891 $5 
11.4 Conduit & Cable Tray $0 $620 $1,787 $0 $2,407 $421 $0 $566 $3,393 $2 
11.5 Wire & Cable $0 $1,642 $2,935 $0 $4,577 $801 $0 $1,076 $6,453 $4 
 Subtotal $7,841 $2,262 $5,813 $0 $15,916 $2,785 $0 $3,740 $22,441 $13 
 12 Instrumentation & Control 
12.8 Instrument Wiring & Tubing $420 $336 $1,345 $0 $2,102 $368 $0 $494 $2,963 $2 
12.9 Other I&C Equipment $517 $0 $1,196 $0 $1,713 $300 $0 $403 $2,416 $1 
 Subtotal $937 $336 $2,542 $0 $3,815 $668 $0 $897 $5,379 $3 
 13 Improvements to Site 
13.1 Site Preparation $0 $28 $575 $0 $603 $106 $0 $142 $851 $1 
13.2 Site Improvements $0 $134 $178 $0 $312 $55 $0 $73 $439 $0 
13.3 Site Facilities $153 $0 $161 $0 $314 $55 $0 $74 $443 $0 
 Subtotal $153 $162 $913 $0 $1,229 $215 $0 $289 $1,733 $1 
 14 Buildings & Structures 
14.5 Circulation Water Pumphouse $0 $63 $50 $0 $112 $20 $0 $26 $158 $0 
 Subtotal $0 $63 $50 $0 $112 $20 $0 $26 $158 $0 
 Total $131,779 $44,373 $100,001 $0 $276,154 $48,327 $29,814 $70,859 $425,154 $252 
Retrofit Values $289,961 $50,743 $31,305 $74,402 $446,411 $265

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
136 
The initial and annual O&M costs for an iron/steel retrofit site were calculated and are shown in 
Exhibit 6-51 and Exhibit 6-52 for 99 percent and 90 percent capture, respectively, while Exhibit 
6-53 shows the retrofit COC of the representative iron/steel plants at both capture rates. 
Exhibit 6-51. Initial and annual O&M costs for iron/steel site with 99 percent capture  
Case:  Iron/Steel Cost Base: Dec 2018 
Representative Plant Size:  2.54 M tonnes steel/year Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 4.6  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 4.6  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $2,016,815 $1.09 
Maintenance Labor:     $6,134,594 $3.32 
Administrative & Support Labor:     $2,037,852 $1.10 
Property Taxes and Insurance:     $19,170,607 $10.36 
Total:     $29,359,868 $15.87 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $9,201,891 $5.85 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 2,397 $1.90 $0 $1,413,167 $0.90 
Makeup and Waste Water Treatment 
Chemicals (ton): 
0 8.0 $550.00 $0 $1,369,239 $0.87 
CO2 Capture System ChemicalsA: Proprietary $3,832,974 $2.44 
Triethylene Glycol (gal): w/equip. 743 $6.80 $0 $1,567,150 $1.00 
Subtotal:    $0 $8,182,530 $5.20 
Waste Disposal 
Triethylene Glycol (gal):  743 $0.35 $0 $80,662 $0.05 
Thermal Reclaimer Unit Waste (ton)   2.12 $38.00 $0 $24,958 $0.02 
Prescrubber Blowdown Waste (ton)   19.8 $38.00 $0 $233,136 $0.15 
Subtotal:    $0 $338,756 $0.22 
Variable Operating Costs Total:    $0 $17,723,177 $11.27 
Fuel Cost 
Natural Gas (MMBtu) 0 35,931 $4.42 $0 $49,275,013 $31.33 
Total:    $0 $49,275,013 $31.33 
ACO2 capture system chemicals includes NaOH and Cansolv solvent

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
137 
Exhibit 6-52. Initial and annual O&M costs for an iron/steel retrofit site with 90 percent capture  
Case:  Iron/Steel Cost Base: Dec 2018 
Representative Plant Size:  2.5 M tonnes steel/year Capacity Factor (%): 85 
Operating & Maintenance Labor 
Operating Labor Operating Labor Requirements per Shift 
  Operating Labor Rate (base):  38.50  $/hour Skilled Operator: 0.0  
  Operating Labor Burden:  30.00  % of base Operator: 4.6  
  Labor O-H Charge Rate:  25.00  % of labor Foreman: 0.0  
    Lab Techs, etc.: 0.0  
    Total: 4.6  
Fixed Operating Costs 
     Annual Cost 
     ($) ($/tonnes/yr CO2) 
Annual Operating Labor:     $2,016,815 $1.20 
Maintenance Labor:     $5,624,341 $3.34 
Administrative & Support Labor:     $1,910,289 $1.14 
Property Taxes and Insurance:     $17,576,066 $10.44 
Total:     $27,127,511 $16.12 
Variable Operating Costs 
     ($) ($/tonnes/yr CO2) 
Maintenance Material:     $8,436,512 $5.90 
Consumables 
 Initial Fill Per Day Per Unit Initial Fill   
Water (/1000 gallons): 0 2,218 $1.90 $0 $1,307,481 $0.91 
Makeup and Waste Water Treatment 
Chemicals (ton): 0 7.5 $550.00 $0 $1,276,955 $0.89 
CO2 Capture System ChemicalsA: Proprietary $3,635,446 $2.54 
Triethylene Glycol (gal): w/equip. 676 $6.80 $0 $1,425,314 $1.00 
Subtotal:    $0 $7,645,197 $5.35 
Waste Disposal 
Triethylene Glycol (gal):  676 $0.35 $0 $73,362 $0.05 
Thermal Reclaimer Unit Waste (ton)   1.98 $38.00 $0 $22,754 $0.02 
Prescrubber Blowdown Waste (ton)   19.8 $38.00 $0 $233,136 $0.16 
Subtotal:    $0 $329,251 $0.23 
Variable Operating Costs Total:    $0 $16,410,960 $11.47 
Fuel Cost 
Natural Gas (MMBtu) 0 32,667 $4.42 $0 $44,798,673 $31.32 
Total:    $0 $44,798,673 $31.32 
ACO2 capture system chemicals includes NaOH and Cansolv solvent 
Exhibit 6-53. COC for 2.54 M tonnes/year iron/steel retrofit cases 
Component 99% capture COC, $/tonne CO2 90% capture COC, $/tonne CO2 
Capital 27.8 28.0 
Fixed 9.3 9.5 
Variable 5.6 5.7 
Purchased Power and Fuel 22.6 22.6 
Total COC 65.4 65.9

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
138 
6.3.9 Plant Capacity Sensitivity Analysis 
An analysis of the sensitivity of retrofit COC to iron/steel plant capacity is shown in Exhibit 6-54. 
As the plant capacity increases, more CO2 is available for capture, thus realizing economies of 
scale. This generic scaling exercise assumes that equipment is available at continuous capacities; 
however, equipment is often manufactured in discrete sizes, which would possibly affect the 
advantages of economies of scale and skew the results of this sensitivity analysis. 
Exhibit 6-54. Iron/steel plant capacity sensitivity 
 
As the cost of capturing CO2 is a normalized cost (i.e., $/tonne CO2), higher capture rates appear 
to cost less than lower capture rates. Comparing the true capital and O&M costs (i.e., not as 
normalized costs) shows that capital and O&M expenditures increase at higher capture rates. 
The cost of the capture system and associated consumables increases at a lesser rate than that 
of the amount of CO2 captured (i.e., a 10 percent increase from 90 to 99 percent capture). The 
margin of error associated with the financial assumptions and cost scaling methodology 
employed in this study indicate that with increasing capture rate in the low purity cases, the 
COC is effectively the same. The reported minor increase in capital cost with increased capture 
rate (up to 99 percent for sources with CO2 purity greater than 12 percent) has been validated 
by independent modeling performed by the CCSI team at NETL and has been reported 
independently in literature. [4] Exhibit 6-55 shows the error in the calculated capture system 
BEC associated with the vendor’s quoted uncertainty rate (-25/+40 percent) alongside the 
amount of CO2 captured in the cement case from 90 to 99 percent capture rate.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
139 
Exhibit 6-55. Iron/steel capture system BEC and amount of CO 2 captured versus capture rate 
 
6.3.10 Iron/Steel Conclusion 
The low purity CO2 streams produced in an iron/steel mill results in a higher COC when 
compared to the high purity cases evaluated in this report, but the quantity of CO2 to be 
captured from such a process makes them attractive industrial processes for CCS as it would 
represent a significant GHG reduction. Two CO2 capture and compression systems for a 2.54 M 
tonnes/year integrated steel mill were modeled to estimate the COC of capturing CO2 from the 
COG and BFS combined flue gas stream and from the COG PPS exhaust. The results showed the 
COC of CO2 to be $65.4/tonne CO2 and $65.9/tonne CO2 for a retrofit site with 99 and 90 
percent capture, respectively. No greenfield COC is calculated, as BOF steel mills are no longer 
being constructed; thus, any application of CO2 capture in such a facility would be a retrofit 
application.  
The plant size sensitivity showed that as plant size decreased from 6.8 M tonnes/year to 0.5 M 
tonnes/year of iron/steel production, the COC increased by $36.9/tonne CO2 and $37.6/tonne 
CO2, for 99 and 90 percent capture, respectively. As the plant size is decreased, less CO2 is 
produced, and economies of scale are lost, resulting in a higher COC. As demonstrated by the 
resulting COCs and the sensitivity analysis, the normalized cost of 99 percent CO2 capture is less 
than that of 90 percent capture.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
140 
7 ECONOMIC ANALYSIS 
7.1 ECONOMIC RESULTS 
Exhibit 7-1 shows the COC results of each industry considered in this study. When comparing 
high purity to low purity industrial sources, the former show lower COCs, as they require less 
equipment (i.e., no capture unit or boiler) and consumables (i.e., no solvents or NG fuel and less 
purchased power) than the low purity industrial sources. The low purity sources higher COC is 
notable not only in the additional capital costs, but in the O&M and purchased power and fuel 
costs as well. These cases require an industrial boiler, which is fueled by purchased NG, and the 
CO2 capture systems add consumables and additional electrical auxiliary loads that increase 
purchased power costs over that of high purity sources. 
Exhibit 7-1. COC summary 
 
 
Evaluating the capital portion of the COC for each source shows the effects of capital intensity. 
The financial assumptions assumed in this report are industry specific. For instance, ethanol 
financial factors suggest that ethanol facilities would incur higher capital intensity compared to 
the cement, steel, and refining industries due to the return on equity and financing scenarios 
prevalent within the ethanol production market. Another interesting observation regarding 
capital intensity is the relationship between the EO and ethanol results. Although ethanol 
presents a higher amount available CO2 for capture, its capital and power costs are higher than 
EO. This is counter-intuitive to the notion of economies of scale but illustrates the role that 
capture stream conditions (i.e., temperature, pressure, composition, and flow rate) plays on 
capture costs. In the ethanol case, the pure CO2 stream must first be cooled, due to the high 
temperature from the fermentation process, and then has a higher compression ratio 
(compared to the EO case) to reach the required pipeline pressure of 2,200 psig. The additional

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
141 
stage of compression and the additional HX impact the auxiliary load as well as the capital 
expenditure. 
Lastly, the CO2 available for capture is both process and market dependent. The process 
emissions detailed for each case throughout the report are average constants; however, as each 
individual market dictates production capacities, the total CO2 available from a plant could, with 
increasing market demand (e.g., plant expansions, increased CF, etc.), drive down the COC for 
that representative case. This trend could be estimated from the results of the plant size 
sensitivities for each case, but it should be noted that these estimates, and the sensitivities to 
plant size for each case, are dependent upon the assumption that equipment is available at any 
and every capacity or rating. However, equipment is often manufactured in discrete sizes, which 
would possibly affect the advantages of economies of scale and skew the results of the 
estimates provided herein. A general observation made under the assumptions of this report is 
demonstrated in the normalized COC elements and the total normalized COCs calculated: more 
CO2 available results in lower normalized costs and realizes economies of scale. 
7.1.1 Cost and Performance Summaries 
The cost and performance results presented in this study are summarized in Exhibit 7-2 and 
Exhibit 7-3 for the high purity and low purity cases, respectively. Of all cases examined in this 
study, the lowest COC of $5.6/tonne CO2 is achieved in a representative CTL facility. There are 
no CTL facilities currently in operation in the United States, but the low COC in such a facility 
implies that any new builds would include carbon capture in its greenfield design.  
Of the existing industrial plant types available in the United States, the lowest COC of 
$16.1/tonne CO2 is indicated at a representative NGP facility. The amount of CO2 available for 
capture in an NGP facility is dependent upon the raw gas CO2 content at the inlet of the plant. 
Capture costs for such a facility account for costs of CO2 compression and cooling, based on the 
design assumptions regarding the base NGP plant. Although COC would increase with 
decreasing CO2 availability, it is expected that integrating CO2 capture for EOR would be feasible 
in most NGP facilities since the AGR unit is often inherent to the facility design. 
Of the low purity cases, which require CO2 purification (i.e., AGR units) along with compression 
and cooling, the pre-combustion capture in the refinery hydrogen 99 percent capture case 
represents the lowest COC at $57.3/tonne CO2. In pre-combustion capture units, variable costs 
such as consumables, waste disposal, purchased power, and fuel are lower on a normalized 
basis when compared to post-combustion capture applications. It should be noted that the pre-
combustion capture system described in Section 4.2.2 would not be installed for design capture 
rates lower than approximately 99 percent. As such, the values reported for the 90 percent 
capture rate in the refinery hydrogen case are meant for comparison purposes only and likely 
represent a deviation from the optimal design operation.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
142 
Exhibit 7-2. Cost and performance summary comparison – high purity cases 
 Industrial Source Facilities Ammonia EO Ethanol NGP CTL GTL 
PERFORMANCE 
Capacity Factor 85% 85% 85% 85% 85% 85% 
Representative Plant Size 394,000  tonnes EO/year 364,500  tonnes EO/year 50 M gallons ethanol/year 330 MMSCFD natural gas 50,000 barrels F-T liquids/day 50,000 barrels F-T liquids/day 
CO₂ Captured (at 85% CF), tonnes/yearA 413,163 103,275 121,588 551,815 7,431,825 1,579,952 
CO₂ Captured (at 85% CF), tonnes/hour 47 12 14 63 848 180 
CO₂ Compressor Load, kW 5,770 1,180 1,810 6,010 43,480 6,700 
Cooling Water Flowrate, gpm 2,994 673 1,098 3,479 25,172 3,823 
Cooling Tower Duty, MMBtu/hour 30 7 11 35 252 38 
COST 
TPC, $/1,000 37,347 16,636 20,187 46,690 162,840 49,170 
BEC 26,487 11,799 14,317 33,114 115,490 34,872 
Home Office Expenses 4,635 2,065 2,505 5,795 20,211 6,103 
Project Contingency 6,225 2,773 3,364 7,782 27,140 8,195 
Process Contingency 0 0 0 0 0 0 
TOC, $M 46 20 25 57 197 60 
TOC, $/1,000 45,587 20,385 24,672 56,764 196,924 59,661 
Owner's Costs 8,240 3,749 4,485 10,074 34,084 10,491 
TASC, $/1,000 47,162 20,892 25,840 58,977 207,583 62,890 
Capital Costs, $/tonne CO2 6.1 9.4 14.1 6.2 2.0 2.9 
Fixed Costs, $/tonne CO2 3.9 9.8 9.2 3.4 0.7 1.2 
Variable Costs, $/tonne CO2 2.7 1.7 1.7 1.5 0.3 0.3 
Purchased Power and/or Fuel, $/tonne CO2 6.3 5.2 6.8 5.0 2.6 1.9 
COC (ex. T&S), $/tonne CO2 19.0 26.0 31.8 16.1 5.6 6.4 
ADue to simplification of BFDs and stream tables throughout the body of the report where minor process streams are omitted, actual CO2 captured as calculated in summary 
tables may be slightly less than that calculated at the capture rates applied in each case. This is due primarily to trace amounts of CO2 entrained in water vapor generated during 
dehydration. Such differences, where they appear, are not expected to have any meaningful impact on the key results of this study, as they account for less than 1 percent of the 
CO2 generated by the emitter.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
143 
Exhibit 7-3. Cost and performance summary comparison – low purity cases 
 Industrial Source Facilities 
 Refinery H2 99% Refinery H2 90% Cement 99% Cement 90% Iron/Steel (Retrofit) 99% Iron/Steel (Retrofit) 90% 
PERFORMANCE 
Capacity Factor 85% 85% 85% 85% 85% 85% 
Representative Plant Size 87,000 tonnes H2/year 87,000 tonnes H2/year 1.29 M tonnes cement/year 1.29 M tonnes cement/year 2.54 M tonnes steel/year 2.54 M tonnes steel/year 
CO₂ Captured (at 85% CF), tonnes/yearA 340,550 309,548 1,017,920 925,793 3,145,352 2,860,681 
CO₂ Captured (at 85% CF), tonnes/hour 39 35 116 106 359 327 
CO₂ Compressor Load, kW 3,470 3,160 10,460 9,570 32,330 29,410 
Cooling Water Flowrate, gpm 11,367 9,757 50,096 46,356 154,873 143,309 
Cooling Tower Duty, MMBtu/hour 11 10 20 18 61 56 
COST 
TPC, $/1,000 130,630 127,184 338,949 322,871 958,530 878,803 
BEC 85,303 82,950 220,519 210,137 621,718 571,122 
Home Office Expenses 14,928 14,516 38,591 36,774 108,801 99,946 
Project Contingency 21,772 21,197 56,491 53,812 159,755 146,467 
Process Contingency 8,627 8,520 23,348 22,148 68,257 61,268 
TOC, $M 159 155 414 394 1,160 1,064 
TOC, $/1,000 159,244 154,978 413,960 394,192 1,160,313 1,063,524 
Owner's Costs 28,614 27,794 75,011 71,320 201,783 184,720 
TASC, $/1,000 164,929 160,510 436,252 415,418 1,266,188 1,160,567 
Capital Costs, $/tonne CO2 21.3 22.8 21.8 22.8 27.8 28.0 
Fixed Costs, $/tonne CO2 14.4 15.6 10.6 11.1 9.3 9.5 
Variable Costs, $/tonne CO2 5.1 5.3 5.9 6.1 5.6 5.7 
Purchased Power and/or Fuel, $/tonne CO2 16.5 16.2 22.6 22.6 22.6 22.6 
COC (ex. T&S), $/tonne CO2 57.3 59.9 60.8 62.7 65.4 65.9 
ADue to simplification of BFDs and stream tables throughout the body of the report where minor process streams are omitted, actual CO2 captured as calculated in summary 
tables may be slightly less than that calculated at the capture rates applied in each case. This is due primarily to trace amounts of CO2 entrained in water vapor generated during 
dehydration. Such differences, where they appear, are not expected to have any meaningful impact on the key results of this study, as they account for less than 1 percent of the 
CO2 generated by the emitter.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
144 
7.2 SENSITIVITY ANALYSES 
In addition to the sensitivity analyses regarding plant capacities presented throughout Section 5 
and Section 6 for each case, evaluations of the COC effects of varying assumptions made in this 
report are presented in this section. 
7.2.1 Capital Charge Factor 
The CCFs used to estimate the capital portion of the COC for each case were determined by the 
NETL Energy Markets Analysis Team and are market dependent. The financial assumptions are 
detailed in Section 3.2, but those factors could vary depending on economic conditions, among 
other aspects. For instance, changing payback period assumptions (i.e., 20-year payback period 
instead of 30-year), debt-to-equity ratios, rates of return and taxes could each affect the capital 
charge factor. Ultimately, the result of the financial assumptions would be applied as the capital 
charge factor. As such, the COC for each case was evaluated across a range of CCFs of 5–35 
percent (Exhibit 7-4). 
Exhibit 7-4. COC vs. CCF

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
145 
The results show that changing financial assumptions can have a very large effect on the COC. In 
the high purity cases, the largest change when varying the CCF over a range of 5–35 percent is 
observed in the ethanol case, where an increase of $60.9/tonne CO2 is noted. In the low purity 
cases, the effect is larger, as the low purity cases require more capital investment due to the 
need for AGR equipment. The largest COC increase in the low purity cases when varying the CCF 
occurs in the refinery hydrogen cases, where a $140.3/tonne CO2 change in the COC is observed 
for the 99 percent capture case and a $150.2/tonne CO2 increase is noted in the 90 percent 
capture case.  
The CCFs used for the high purity and low purity cases, details of which have been given 
previously in Section 3.2, are representative of a project-specific CCF in each individual 
industrial sector. In addition to the industrial sectors’ market influences on CCF, the maturity of 
a technology, specifically a capture technology like the AGR units employed in this study, may 
also affect the CCF. As capture systems are becoming more prevalent, and the project learning 
curve has improved, the low end of the CCF sensitivity curve demonstrated in this analysis may 
be a more reasonable representation. 
7.2.2 Retrofit Factor 
The retrofit factors used to estimate retrofit COC for each case, excluding CTL and GTL, were 
applied as a multiplier to TPC. The basis for this methodology is detailed in Section 3.3, but such 
an overall retrofit factor could vary depending on installation specifics, technology 
considerations, existing site constraints, and other determinants. As such, the COC for each case 
was evaluated across a retrofit factor range of 1.0–1.35, where the values corresponding to a 
1.0 retrofit factor are indicative of a greenfield COC in each case (Exhibit 7-5).

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
146 
Exhibit 7-5. COC vs. retrofit factor 
 
 
Because the retrofit factors in this study are applied as a multiplier to TPC, the effect of varying 
those factors across a range of values is an increasing COC with increasing retrofit factor for all 
cases. An interesting observation from this sensitivity analysis is the differing slopes of the lines 
between the low purity and high purity cases, meaning that the retrofit factors applied do not 
have equal magnitude of effect on all cases. For instance, the change in COC for the high purity 
cases ranged $3.3–7.1/tonne CO2 with increasing retrofit factor, whereas that of the low purity 
cases ranged $11.9–13.3/tonne CO2. This is due to the higher capital costs required for purifying 
the CO2 prior to compression creating a larger TPC, which is the figure that is affected by the 
addition of the retrofit difficulty factor. 
7.2.3 Purchased Power Price 
The purchased power cost for each case is directly dependent upon the purchased power price 
assumed. For each case, a $60/MWh price was used to estimate the purchased power costs, but 
price can vary widely depending upon market scenario, location, economic conditions, fuel 
pricing, and more. As such, the total COC for each case was estimated across a range of $20–
140/MWh purchased power price. Purchased power price increase has the most dramatic effect 
in the cement and iron/steel cases, where an increase of $16.4/tonne CO2 is observed across 
the sensitivity range (Exhibit 7-6).

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
147 
Exhibit 7-6. COC vs. purchased power price 
 
7.2.4 Natural Gas Price 
The fuel cost required for the industrial boiler in each low purity case is directly dependent 
upon the NG price assumed. For each case, $4.42/MMBtu was used for the NG price but can 
vary widely depending upon market scenario, location, economic conditions, fuel availability, oil 
prices, and more. As such, the total COC for each case was estimated across a fuel price range of 
$3–10/MMBtu. NG price increase has the most dramatic effect in the iron/steel 90 percent 
capture case, where an increase of $30.6/tonne CO2 is observed across the sensitivity range 
(Exhibit 7-7).

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
148 
Exhibit 7-7. COC vs. NG price 
 
7.2.5 Capacity Factor 
Average capacity factors at industrial plants are variable, due to market fluctuations, 
differences in production cycles, operational upsets and planned shutdown 
requirements, regulatory constraints, and more. An 85 percent CF was assumed for the 
cases in this study, but it is important to consider how CFs affect the COCs calculated in 
this analysis. As CF varies from 65 to 95 percent, the COC for each case decreases, most 
notably in the Refinery H2 90 percent capture case where a $18.0/tonne CO2 decrease is 
observed across the sensitivity range.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
149 
Exhibit 7-8. COC vs. CF

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
150 
8 CONCLUSION 
Nine different industrial sources were examined in this study: ammonia, EO, ethanol, NGP , CTL, 
GTL, refinery hydrogen, cement, and iron/steel. Plant sizes were chosen based on different 
factors, including representative plant sizes expected to be built or already built in the industry 
(ammonia, refinery hydrogen), plant sizes representative of most of the production for the 
industry (ethanol, steel/iron, EO, cement), or plant sizes that would justify the addition of 
capture equipment (NGP). Plant sizes for CTL and GTL were determined based on those 
presented in previous NETL studies.  Both greenfield and retrofit application costs were 
determined. The retrofit costs were derived by application of a retrofit factor to calculated total 
greenfield plant cost. 
The results of this study show that CTL gives the lowest greenfield COC for the CO2 product, a 
value of $5.6/tonne. This result is driven by the highly pure CO2 sources produced from the CTL 
plant, as well as the largest amount of CO2 available for capture across the cases considered. 
This combination of high availability coupled with high purity results in the lowest COC. The 
costliest option for capturing CO2 in the group of industrial plants evaluated is iron/steel 
production, with a retrofit cost of $65.4/tonne CO2 and $65.9/tonne CO2 at 99 and 90 percent 
capture rates, respectively. The low purity CO2 emission streams from iron and steel mills 
require purification equipment to attain EOR pipeline standards.  
The greenfield COCs for the remaining cases fall in between the maximum and minimum cases 
as follows: GTL at $6.4/tonne, NGP at $16.1/tonne, ammonia at $19.0/tonne, EO at 26.0/tonne, 
ethanol at $31.8/tonne, refinery hydrogen with 99 percent capture at $57.3/tonne and with 90 
percent capture at $59.9/tonne, and finally, cement at $60.8/tonne and $62.7/tonne for 99 and 
90 percent capture, respectively. The assumed CO2 concentrations for GTL, NGP , EO, ammonia, 
and ethanol were relatively high purity, either equivalent to or nearly the same purity as the 
lowest-COC CTL case. The reason for the increasing COC given similar purity is related to the 
amount of CO2 available for capture, or economies of scale. 
Economies of scale have a notable impact when comparing 99 and 90 percent capture rates in 
the low purity cases. On a normalized (i.e., $/tonne CO2) basis, COC appears lower for higher 
capture rates in the refinery hydrogen, cement, and iron/steel analyses. This is also indicated in 
the plant size sensitivity analyses for each low purity case. As discussed in Section 6.1.8, Section 
6.2.8, and Section 6.3.8, capital and O&M costs rise with increasing capture rates, but as there is 
more CO2 captured, those costs result in a lower normalized costs at higher capture rates as 
presented. It is important to note that given the margin of error associate with the AACE Class 4 
estimates applied in this study, and the margin of error assigned to the quotation from the 
capture system vendor (-25/+40 percent), the change in normalized cost from 90 to 99 percent 
is insignificant.  
Sensitivity analyses of retrofit factor and purchased power price show minimal change in the 
COC for all cases. The most noticeable sensitivity effect is observed with plant size (economy of 
scale). For all cases, as the plant size is increased and, therefore, the amount of CO2 available for 
capture increased, the COC decreased. The largest effect is observed with the iron/steel plant 
size sensitivity, where the COC increased by $36.9/tonne CO2 and $37.6/tonne CO2, for 99 and

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
151 
90 percent capture cases, respectively, was observed when plant size was varied over the range 
of 0.5–6.8 M tonnes of steel per year. The base case production was 2.54 M tonnes of steel per 
year. All sensitivity analyses were evaluated in isolation, and it is possible that if individual 
design assumption changes were considered in combination, impacts on the COCs would 
potentially differ from the additive values of each change in design assumption. 
CO2 purity, as expected, plays a large role in the normalized COC; however, the amount of CO2 
and, therefore, the varying economies of scale from one industrial process to another, also has a 
dramatic effect on the cost of capturing CO2. This analysis evaluated potential decarbonization 
opportunities in representative industrial plant applications, and the results show that capturing 
CO2 can be cost-effective in the industrial sector, especially when a facility has two specific 
emissions stream characteristics: 1) high CO2 purity so that further purification is not required, 
and (2) large amounts of CO2 available.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
152 
9 FUTURE WORK 
Future work in this area should look to plants with the characteristics of relatively high CO2 
purity and large CO2 supply to expand upon the findings in the report. Potential 
recommendations include plants where CO2 removal is inherent to the base plant process. A 
perfect example of this is ammonia and urea production, where not only is CO2 removal crucial 
for maximizing ammonia synthesis loop efficiency and, therefore, production, but also reuse of 
the CO2 for producing urea justifies this removal and recycle. The following items are potential 
future work that could expand on the analysis presented in this study. 
9.1 IN-DEPTH PROCESS ANALYSIS 
There are several opportunities where the results herein could be used as a starting point for a 
more in-depth analysis of the industries covered in this study. For example, the ammonia case 
does not account for in calculations how the base ammonia plant might allocate CO2 for reuse 
in the urea or other derivative production processes. In addition, lesser products such as food-
grade liquid CO2, presumably captured from the high purity stripping vent point source, may 
also affect the amount of CO2 available for capture from any one plant. The potential for food-
grade liquid CO2 also appears in the literature as an option for ethanol plants. These types of 
lesser-known factors could be investigated to better frame the amount of CO2 available from 
different industries. 
In addition to alternate CO2 uses in the base plants, heat integration opportunities may exist, 
especially in greenfield cases or in plants where combined heat and power systems are in place 
or considered in the plant design. In retrofit cases, heat integration opportunities might increase 
retrofit difficulty factors, affecting capital expenditures, but lessening O&M costs. The heat 
requirements of the capture systems employed in the low purity cases analyzed in this study 
elicit the need for a standalone boiler, as discussed in Section 4.3. The flue gas from this NG-
fired boiler contains additional CO2 emissions over that of the base process, which were not 
captured based on the assumptions made in this analysis. Future work might consider an 
additional capture process or a mixing of this flue gas stream with the base plant emissions 
source to reduce those greenhouse gas emissions necessary for steam generation. Such 
scenarios may be evaluated with a more in-depth process analysis. 
9.2 MULTIPLE PROCESS SCENARIO 
Many chemical plants have two or more of the processes discussed in this analysis at the same 
industrial facility location. This could decrease the cost for CO2 capture and make some 
processes more feasible when combined with others. Combining processes could be viewed 
from the perspective of mixing flue gas streams to take advantage of the economy of scale of 
building a single, larger capture unit, versus multiple smaller units, or from the perspective of 
combining CO2 product streams in a larger trunk line to limit transport costs. Transport costs 
were not considered in this study.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
153 
9.3 ADDITIONAL PROCESSES 
Methanol and a variety of other commodity chemical manufacturing facilities could be potential 
processes for consideration, assuming appropriate feedstock to justify capture. Additionally, as 
mentioned in Section 6.1, the fluid catalytic cracking unit at refineries is another viable point 
source for CO2 capture. This may be investigated separately, or it could be included as a multiple 
process scenario, where the fluid catalytic cracking unit and the refinery hydrogen unit are 
combined to take advantages of economies of scale. 
Another means of hydrogen production that could be considered for decarbonation is hydrogen 
from coal gasification. NETL recently evaluated the cost of capturing CO2 in hydrogen production 
via gasification applications as part of the report “Comparison of Commercial, State-of-the-Art, 
Fossil-Based Hydrogen Production Technologies.” [40] Lastly, only the BOF steel plant 
configuration was considered in this study, but EAF plants make up 32 percent of steel 
production in current industry and are expected to be the only greenfield steel plants to be 
constructed. An analysis of EAF steel production for decarbonization would likely be impactful. 
9.4 TECHNO-ECONOMIC ANALYSIS OF CO2 DISTRIBUTION TO EOR 
FIELDS 
As stated previously in Section 4.1.2, pressures as low as 1,200 psig may be acceptable for EOR 
field usage. Reducing the pressure to which CO2 needs to be compressed would reduce the 
COC. A reduction in pressure would result in a lower compressor capital cost, as well as reduced 
power consumption resulting in a lower cost associated with purchasing power from the grid. 
The economics of CO2 transport with the existing pipeline infrastructure was not part of this 
analysis but does contribute to the true COC. 
9.5 LIFE EXTENSION COSTS FOR EXISTING FACILITIES 
The implicit assumption for the cases presented in this report is that the plants that have been 
retrofitted (i.e., cement, steel, etc.) have sufficient remaining life, such that the base plant 
remaining life will match the expected life of the retrofitted equipment (i.e., capture system, 
compression), assumed to be 30 years. This study does not consider, or include any costs to 
represent, life extension projects that a plant (i.e., a cement plant) may consider if adding 
capture and compression. Future work could include an analysis to identify the average age of 
the various industry’s plants, characterize the standard expected life for these plants by 
industry, and characterize the cost of typical life extension projects that would be considered as 
part of a capture retrofit. This would allow for a more complete cost for a retrofit project, when 
considering factors outside of just the capture and/or compression equipment.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
154 
10  REFERENCES 
 
[1]  NETL, "Quality Guidelines for Energy System Studies: CO2 Impurity Design 
Parameters," U.S. DOE/NETL, Pittsburgh, 2019. 
[2]  Shell, Proprietary Quote: CO2 Capture System, 2021.  
[3]  NETL, "Quality Guidelines for Energy System Studies: Capital Cost Scaling 
Methodology: Revision 4 Report," U.S. DOE/NETL, Pittsburgh, 2019. 
[4]  Y. Du, T. Gao, G. T. Rochelle and A. S. Bhown, "Zero- and negative-
emissions fossil-fired power plants using CO2 capture by conventional 
aqueous amines," International Journal of Greenhouse Gas Control, vol. 
111, October 2021.  
[5]  NETL, "Cost and Performance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity," U.S. DOE/NETL, Pittsburgh, 
2022. 
[6]  EPA, "Facility Level Information on Greenhouse Gases Tool (FLIGHT)," EPA, 
2020. [Online]. Available: 
https://ghgdata.epa.gov/ghgp/main.do#/facility/?q=Find%20a%20Facilit
y%20or%20Location&st=&bs=&et=&fid=&sf=11001100&lowE=-
20000&highE=23000000&g1=1&g2=0&g3=0&g4=0&g5=0&g6=0&g7=0&g8=
0&g9=0&g10=0&g11=0&g12=0&s1=0&s2=0&s3=1&s4=0&s5=0&s6=0&s7=0&s
8=0&s9=0&s10=0. [Accessed 3 September 2021]. 
[7]  NETL, "Quality Guidelines for Energy System Studies: Carbon Dioxide 
Transport and Storage Costs in NETL Studies," U.S. DOE/NETL, Pittsburgh, 
2019. 
[8]  NETL, "Quality Guidelines for Energy System Studies: Process Modeling 
Design Parameters," U.S. DOE/NETL, Pittsburgh, 2019. 
[9]  NETL, "Quality Guidelines for Energy System Studies: Cost Estimation 
Methodology for NETL Assessments of Power Plant Performance," U.S. 
DOE/NETL, Pittsburgh, 2019. 
[10]  AACE International, Cost Estimate Classification System – As Applied in 
Engineering, Procurement, and Construction for the Process Industries; 
TCM Framework 7.3 – Cost Estimating and Budgeting, AACE International, 
2005.  
[11]  Chemical Engineering, Chemical Engineering Plant Cost Index, Access 
Intelligence, LLC, Ed., 2021.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
155 
[12]  Electric Power Research Institute (EPRI), "Technical Assessment Guide 
(TAG®) – Power Generation and Storage Technology Options, EPRI 
Product ID No. 1017465," EPRI, Palo Alto, 2009. 
[13]  NETL, "Retrofit Cost Analysis for Post-combustion CO2 Capture," U.S. 
DOE/NETL, Pittsburgh, 2021. 
[14]  NETL, "Carbon Dioxide Enhanced Oil Recovery: Untapped Domestic 
Energy Supply and Long Term Carbon Storage Solution," U.S. DOE/NETL, 
Pittsburgh, Pennsylvania, 2010. 
[15]  Shell, "The Quest for less CO2: Learning from CCS Implementation in 
Canada," 2015. [Online]. Available: 
https://www.globalccsinstitute.com/archive/hub/publications/196788/qu
est-less-co2-learning-ccs-implementation-canada.pdf. [Accessed 29 
October 2021]. 
[16]  CleaverBrooks, Quotation for Industrial Water Boiler, Pittsburgh: 
CleaverBrooks, 2021.  
[17]  NETL, "Eliminating the Derate of Carbon Capture Retrofits," U.S. DOE/NETL, 
Pittsburgh, 2021. 
[18]  R. Turton, W. Whiting, J. Shaeiwitz and D. Bhattacharyya, Analysis, Synthesis 
and Design of Chemical Processes, New York: Pearson, 2018.  
[19]  Ammonia Industry, "Ammonia Capacity in North America," 5 August 2014. 
[Online]. Available: https://ammoniaindustry.com/download-ammonia-
capacity-in-north-america/. [Accessed 19 May 2020]. 
[20]  Coninck, Hellen, et. al, Carbon Capture and Storage in Industrial 
Applications: Technology Synthesis Report., United Nations Industrial 
Development Organization, 2010.  
[21]  K. Van Alphen, CO2 Capture: Industrial Sources - Global Technology 
Roadmap for CCS in Industry, 2010.  
[22]  R. Strait and M. Nagvekar, "Carbon Dioxide Capture and Storage in the 
Nitrogen and Syngas Industries," Carbon Capture, no. January-February, 
2010.  
[23]  T. Kuramochi, "CO2 Industries and Distributed Energy Systems: Possibilities 
and Limitations," Kanagawa, Japan, 2011. 
[24]  P. Zakkour, "CCS Roadmap for Industry: High-purity CO2 sources," Carbon 
Counts Company, UK, 2010. 
[25]  United Nations Industrial Development Organization, "Carbon Capture 
and Storage in Industrial Applications: Technology Synthesis Report," 
UNIDO, 2010.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
156 
[26]  D. K. van Alphen, "CO2 Capture: Industrial Sources Technology 
Roadmap," IEAGHG Summer School, 2011. 
[27]  F. Mirasol, "US Chemical Profile: Ethylene Oxide," ICIS, 11 June 2007. 
[Online]. Available: http://www.icis.com/Articles/2010/08/02/9380662/us-
chemical-profile-ethylene-oxide.html. [Accessed September 2021]. 
[28]  Huang, "Ethylene Oxide Reactor System," jEO & Associates, 8 October 
1999. [Online]. Available: 
http://www.owlnet.rice.edu/~ceng403/gr1599/finalreport3.html#details. 
[Accessed September 2021]. 
[29]  M. Rostam-Abadi, "Assessment of Carbon Capture and Sequestration 
Options for Power Plants," Madison, Wisconsin, 2006. 
[30]  NETL, "Archer Daniels Midland Company: CO2 Capture from Biofuels 
Production and Sequestration into the Mt. Simon Sandstone," U.S. 
DOE/NETL, Pittsburgh, Pennsylvania, 2011. 
[31]  Renewable Fuels Association (RFA), "Where is Ethanol Made?," RFA, 
February 2021. [Online]. Available: https://ethanolrfa.org/where-is-
ethanol-made/. [Accessed 3 September 2021]. 
[32]  DOE Office of Energy Efficiency and Renewable Energy, "Alternative Fuels 
Data Center, Ethanol Production and Distribution," DOE, [Online]. 
Available: https://afdc.energy.gov/fuels/ethanol_production.html. 
[Accessed 15 May 2020]. 
[33]  Y. Lu, D. Garner, C. Korose, S. Chen and M. Rostam-Abadi, "Inventory of 
Industrial Stationary CO2 Emissions in the Illinois Basin," Illinois State 
Geological Survey, Champaign, 2007. 
[34]  H. Karlsson and L. Bystrom, Global Status of BECCS Projects 2012, Australia: 
Global CCS Institute, 2010.  
[35]  Y. Lin and S. Tanaka, "Ethanol Fermentation from Biomass Resources: 
Current State and Prospects," Springer-Verlag, vol. 69, 2006.  
[36]  USDA, "Corn for Grain 2011 Production by County and Location of Ethanol 
Plants as of March 8, 2012," 2012. [Online]. Available: 
https://www.researchgate.net/figure/CORN-FOR-GRAIN-PRODUCTION-BY-
COUNTY-AND-ETHANOL-PLANTS-2011_fig1_342421027. [Accessed 29 
October 2021]. 
[37]  Gas Research Institute, Variability of Natural Gas Composition in Select 
Major Metropolitan Areas of the United States, Springfield: U.S. 
Department of Commerce, 1992.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
157 
[38]  NETL, "Baseline Technical and Economic Assessment of a Commercial 
Scale Fischer-Tropsch Liquids Facility," U.S. DOE/NETL, Pittsburgh, 2014. 
[39]  NETL, "Analysis of Natural Gas-to Liquid Transportation Fuels via Fischer-
Tropsch," U.S. DOE/NETL, Pittsburgh, 2013. 
[40]  NETL, "Comparison of Commercial, State-of-the-Art, Fossil-Based Hydrogen 
Production Technologies," U.S. DOE/NETL, Pittsburgh, 2021. 
[41]  DOE Office of Energy Efficiency and Renewable Energy, "Hydrogen 
Production: Natural Gas Reforming," DOE, [Online]. Available: 
https://www.energy.gov/eere/fuelcells/hydrogen-production-natural-gas-
reforming. [Accessed 3 September 2021]. 
[42]  Shell Canada, "Quest CCS Facility Captures and Stores Five Million Tonnes 
of CO2 Ahead of Fifth Anniversary," Shell Canada, 10 July 2020. [Online]. 
Available: https://www.shell.ca/en_ca/media/news-and-media-
releases/news-releases-2020/quest-ccs-facility-captures-and-stores-five-
million-tonnes.html. [Accessed 7 September 2021]. 
[43]  USGS, "National Minerals Information Center - Cement Statistics and 
Information," January 2021. [Online]. Available: 
https://pubs.usgs.gov/periodicals/mcs2021/mcs2021-cement.pdf. 
[Accessed 3 September 2021]. 
[44]  Portland Cement Association, "Plant Information Summary," PCA, Skokie, 
2019. 
[45]  Portland Cement Association, "Overview of the Cement Industry: Portland 
Cement Association," December 2009. [Online]. Available: 
http://www.cement.org/basics/cementindustry.asp. [Accessed 4 
December 2012]. 
[46]  Portland Cement Association, "History & Manufacture of Portland Cement: 
Portland Cement Association," December 2009. [Online]. Available: 
http://www.cement.org/basics/concretebasics_history.asp. [Accessed 4 
December 2012]. 
[47]  N. S. Hassan, "Techno-Economic Study of CO2 Capture Process for 
Cement Plants," Waterloo, Ontario, Canada, 2005. 
[48]  Portland Cement Association (PCA), "Environmental Product Declaration: 
Portland Cement," PCA, Skokie, 2021. 
[49]  D. Barker, S. Turner, P. Napier-Moore, M. Clark and J. Davison, "CO2 
Capture in the Cement Industry," Energy Procedia, vol. 1, no. 1, 2009.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
158 
[50]  EPA, "Sources of Greenhouse Gas Emissions," EPA, 2019. [Online]. 
Available: https://www.epa.gov/ghgemissions/sources-greenhouse-gas-
emissions#colorbox-hidden. [Accessed 7 September 2021]. 
[51]  World Steel Association, "World Steel in Figures," World Steel Association, 
[Online]. Available: https://www.worldsteel.org/steel-by-
topic/statistics/steel-statistical-yearbook/World-Steel-in-Figures.html. 
[Accessed 19 May 2020]. 
[52]  D. E. Wiley, M. T. Ho and A. Bustamante, "Assessment of Opportunities for 
CO2 Capture at Iron and Steel Mills: An Australian Perspective," 2011. 
[53]  Statista, "Ethylene oxide production in the United States from 1990 to 2019," 
Statista, 28 January 2022. [Online]. Available: 
https://www.statista.com/statistics/974787/us-ethylene-oxide-production-
volume/. [Accessed 2 June 2022].

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
159 
APPENDIX: CARBON BALANCES 
Note: All convergence tolerance values in the tables within this appendix are calculated by 
difference. 
The carbon balancei for the ethanol case is shown in Exhibit A-1. 
Exhibit A-1. Ethanol case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Fermentation Stream 4,457 (9,825) CO2 Captured Stream 4,457 (9,825) 
Total 4,457 (9,825) Total 4,457 (9,825) 
 
The carbon balance for the ammonia case is shown in Exhibit A-2. 
Exhibit A-2. Ammonia case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Stripping Vent 15,149 (33,398) CO2 Captured Stream 15,140 (33,379) 
  TEG Vent 9 (19) 
Total 15,149 (33,398) Total 15,149 (33,398) 
 
The carbon balance for the natural gas processing (NGP) case is shown in Exhibit A-3. 
Exhibit A-3. NGP case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Stripping Vent 20,266 (44,590) CO2 Captured Stream 20,221 (44,581) 
  TEG Vent 4 (9) 
Total 26,266 (44,590) Total 26,226 (44,590) 
 
The carbon balance for the ethylene oxide (EO) case is shown in Exhibit A-4. 
 
i Carbon balances may show carbon content of minor process streams, including the CO2 entrained in the water vapor 
vent from the TEG dehydration system and CO2 entrained in process water knockouts, that are not represented in the 
block flow diagrams throughout the report body. These process streams were omitted from the report body for simplicity 
and brevity. Cases where this simplification applies include ammonia, NGP, refinery H2, iron/steel, and cement.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
160 
Exhibit A-4. EO case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Rectisol Stream 3,785 (8,345) CO2 Captured Stream 3,785 (8,345) 
Total 3,785 (8,345) Total 3,785 (8,345) 
 
The carbon balance for the coal-to-liquids (CTL) case is shown in Exhibit A-5. 
Exhibit A-5. CTL case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Gasification AGR Unit 110,862 (244,411) CO2 Captured Stream 272,397 (600,525) 
FT AGR Unit 161,536 (356,114)   
Total 272,397 (600,525) Total 272,397 (600,525) 
 
The carbon balance for the gas-to-liquids (GTL) case is shown in Exhibit A-6. 
Exhibit A-6. GTL case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Stripping Vent 57,905 (127,665) CO2 Captured Stream 57,905 (127,665) 
Total 57,905 (127,665) Total 57,905 (127,665) 
 
The carbon balance for the refinery hydrogen case with 99 percent capture is shown in Exhibit 
A-7.  
Exhibit A-7. Refinery hydrogen case with 99 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
SMR Off-Gas Stream 16,102 (35,499) CO2 Captured Stream 12,480 (27,513) 
Amine Recycle 405 (893) TEG Vent 1 (2) 
   Gas to PSA 3,543 (7,812) 
  Recycle 378 (832) 
  Process Knockout Entrainment 106 (233) 
Total 16,507 (36,392) Total 16,507 (36,392) 
 
The carbon balance for the refinery hydrogen case with 90 percent capture is shown in Exhibit 
A-8.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
161 
Exhibit A-8. Refinery hydrogen case with 90 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
SMR Off-Gas Stream 16,102 (35,499) CO2 Captured Stream 11,343 (25,008) 
Amine Recycle 368 (811) TEG Vent 6 (14) 
   Gas to PSA 4,675 (10,307) 
  Recycle 378 (832) 
  Process Knockout Entrainment 67 (149) 
Total 16,470 (36,310) Total 16,470 (36,310) 
 
The carbon balance for the iron/steel case coke oven gas (COG)/blast furnace stove (BFS) stream 
with 99 percent capture is shown in Exhibit A-9. 
Exhibit A-9. Iron/steel case COG/BFS stream with 99 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
COG Stream 27,380 (60,363) CO2 Captured Stream 57,475 (126,710) 
BFS Stream 30,704 (67,690) TEG Vent 10 (23) 
  Clean Flue Gas 599 (1,320) 
Total 58,084 (128,053) Total 58,084 (128,053) 
 
The carbon balance for the iron/steel case COG/BFS stream with 90 percent capture is shown in 
Exhibit A-10. 
Exhibit A-10. Iron/steel case COG/BFS stream with 90 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
COG Stream 27,380 (60,363) CO2 Captured Stream 52,273 (115,242) 
BFS Stream 30,704 (67,690) TEG Vent 9 (21) 
  Clean Flue Gas 5,802 (12,790) 
Total 58,084 (128,053) Total 58,084 (128,053) 
 
The carbon balance for the steel case COG power plant stack (PPS) stream with 99 percent 
capture is shown in Exhibit A-11.

COST OF CAPTURING CO2 FROM INDUSTRIAL SOURCES 
162 
Exhibit A-11. Steel case COG PPS stream with 99 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
COG PPS Stream 58,400 (128,751) CO2 Captured Stream 57,788 (127,400) 
    TEG Vent 10 (23) 
  Clean Flue Gas 602 (1,328) 
Total 58,400 (128,751) Total 58,400 (128,751) 
 
The carbon balance for the steel case COG PPS stream with 90 percent capture is shown in 
Exhibit A-12.  
Exhibit A-12. Steel case COG PPS stream with 90 percent capture carbon balance  
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
COG PPS Stream 58,400 (128,751) CO2 Captured Stream 52,558 (115,870) 
    TEG Vent 9 (21) 
  Clean Flue Gas 5,833 (12,860) 
Total 58,400 (128,751) Total 58,400 (128,751) 
 
The carbon balance for the cement 99 percent capture case is shown in Exhibit A-13. 
Exhibit A-13. Cement 99 percent capture case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Kiln Off-Gas Stream 37,697 (83,108) CO2 Captured Stream 37,302 (82,237) 
  TEG Vent 7 (15) 
    Clean Flue Gas 389 (857) 
Total 37,697 (83,108) Total 37,697 (83,108) 
 
The carbon balance for the cement 90 percent capture case is shown in Exhibit A-14. 
Exhibit A-14. Cement 90 percent capture case carbon balance 
Carbon In Carbon Out 
 kg/hr (lb/hr)  kg/hr (lb/hr) 
Kiln Off-Gas Stream 37,697 (83,108) CO2 Captured Stream 33,926 (74,794) 
  TEG Vent 6 (13) 
    Clean Flue Gas 3,765 (8,301) 
Total 37,697 (83,108) Total 37,697 (83,108)

www.netl.doe.gov 
Albany, OR • Anchorage, AK • Morgantown, WV • Pittsburgh, PA • Sugar Land, TX 
(800) 553-7681
