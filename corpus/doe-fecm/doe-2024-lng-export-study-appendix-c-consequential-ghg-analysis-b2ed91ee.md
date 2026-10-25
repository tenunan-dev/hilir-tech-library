---
source_id: "doe-fecm"
title: "DOE 2024 LNG Export Study Appendix C Consequential GHG Analysis"
summary: "Appendix to the 2024 US DOE LNG export study that estimates the consequential greenhouse gas effects of US LNG exports, prepared by NETL to inform DOE's public interest review."
url: "https://www.energy.gov/sites/default/files/2024-12/LNGUpdate_AppendixC_Dec2024.pdf"
retrieved_at: "2026-10-24T05:14:18+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "GAS", "CCS", "H2"]
disciplines: ["PRC"]
sha256: "b2ed91ee92bd9181bb681ccbdc277129e1d30566b4e73b0e45b3455088d30171"
collected: "manual"
---

# DOE 2024 LNG Export Study Appendix C Consequential GHG Analysis

APPENDIX C: CONSEQUENTIAL 
GREENHOUSE GAS ANALYSIS OF U.S. 
LNG EXPORTS 
December 2024

Consequential Analysis Appendix 
 
December 2024 
 
 
 
Prepared for: 
U.S. Department of Energy, Office of Fossil Energy and Carbon Management,  
Office of Resource Sustainability 
 
Prepared by: 
National Energy Technology Laboratory 
3610 Collins Ferry Road 
Morgantown, WV 26505

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-i 
CONTENTS 
Foreword ................................ ................................ ................................ ................................ .... 1 
Executive Summary ................................ ................................ ................................ ................... 2 
Background ................................ ................................ ................................ ................................  4 
Consequential LCA Modeling Approach for Assessing GHG Emissions from Increased U.S. LNG 
Exports ................................ ................................ ................................ ................................ ...... 6 
Step 1: Obtain Study Scenario GCAM GHG Emissions and U.S. LNG Export Results from 
GCAM ................................ ................................ ................................ ................................ .... 7 
Step 2: Obtain U.S. Natural Gas National Average Life Cycle GHG Performance (from NETL 
Natural Gas Baseline) ................................ ................................ ................................ ...........10 
Step 3: Model U.S. Liquefaction Plant National Average Life Cycle GHG Performance ......... 11 
Step 4: Align GCAM Natural Gas Production and Pipeline Transport to U.S. National Average 
GHG Performance ................................ ................................ ................................ .................18 
Step 5: Calculate GCAM-NETL-aligned Global GHG Emissions Results ............................... 19 
Step 6: Interpolate GCAM-aligned Results from 5-year Time Steps to Annual Results ..........20 
Step 7: Calculate GCAM-NETL-aligned Consequential GHG Intensity and SC-GHG per Unit of 
U.S. LNG Exports ................................ ................................ ................................ ..................22 
Step 8: Subtract National Average Upstream Natural Gas and Liquefaction Plant GHG 
Performance to Determine Project Non-Direct Emissions Intensity ................................ ........24 
Step 9: Add Project Direct Emissions to Project Non-Direct Emissions to Determine Individual 
Project GHG Emissions Intensity Inclusive of Consequential Market Effects .........................25 
Step 10: Demonstrate Estimation of Consequential GHG Intensity and SC -GHG for an 
Individual U.S. LNG Project ................................ ................................ ................................ ...25 
Metric #1: Comparative Environmental GHG Performance: Consequential GHG Intensity .26 
Metric #2: Comparative Environmental Performance: Consequential Social Costs of 
Greenhouse Gases ................................ ................................ ................................ ............27 
Consequential LCA Modeling Results for All Scenario Comparisons ................................ .........28 
A. Individual Project Direct Emissions Breakeven GHG Performance ................................ 33 
B. Evaluation of Model Sensitivity to Key Performance Attributes ................................ ......35 
1. Sensitivity Analysis 1: Upstream Methane Emissions Intensity ................................ ..36 
2. Sensitivity Analysis 2: Liquefaction Plant Emissions Representation within GCAM ....37 
C. Market Drivers for Changes in GHG Intensity of U.S. LNG Exports ............................... 38 
1. Change in Global Services ................................ ................................ ........................38 
2. GHG Intensity of U.S. LNG Exports per Unit of Global Services (Equivalent Unit of 
Service) ................................ ................................ ................................ .............................39 
3. Summary of Market Drivers of Total Consequential GHG Intensity of U.S. LNG Exports
 41 
D. Modeling Caveats and Limitations ................................ ................................ .................44 
Study Summary ................................ ................................ ................................ ........................45

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-ii 
Appendices to this Report ................................ ................................ ................................ .........47 
Appendix C-1: NEMS and NETL LCA Model Results Comparison ................................ ............48 
Appendix C-2: Incorporation, Assessment, and Adjustments to the Global Change Analysis Model 
(GCAM) Results ................................ ................................ ................................ ........................53 
A. GCAM and NETL (2020) Emissions Intensity Comparison and Adjustment ...................53 
B. Method and Scaling Factors Used for Service-Equivalent Analysis ............................... 58 
Appendix C-3: Social Cost of Greenhouse Gases Modeling and Additional Results ..................60 
Appendix C-4: Detailed Data Tables for Values Summarized in this Report ............................... 67 
C. Summary Consequential Result Tables ................................ ................................ ....... 110 
 
FIGURES 
Figure 1. GHG emissions and U.S. LNG export trends for the Defined Policies: Existing/FID and 
Defined Policies: Model Resolved Scenarios ................................ ................................ ............22 
 
Figure C-2.1. Mapping of NETL natural gas stages to GCAM sectors ................................ .......54 
 
TABLES 
Table 1. Scenario design and summary ................................ ................................ ..................... 7 
Table 2. Additional sensitivity scenarios in this study ................................ ................................ .. 8 
Table 3. Summary of cumulative model year (every five years, 2020 -2050) U.S. LNG exports, 
GHG emissions, and global services from GCAM ................................ ................................ ...... 9 
Table 4. 2020 LNG facility export volumes as reported in GHGRP Subpart W ..........................12 
Table 5. 2020 LNG facility GHG emissions as summarized in GHGRP ................................ .....12 
Table 6. 2020 LNG facility calculated CO2 emissions from acid gas removal units ....................13 
Table 7. 2020 ERCOT generation mix ................................ ................................ .......................14 
Table 8. 2020 LNG facility GHGRP Subpart W LNG import and export equipment emission 
sources ................................ ................................ ................................ ................................ .....15 
Table 9. 2020 LNG facility GHGRP Subpart W LNG import and export equipment emission 
sources (cont’d)26 ................................ ................................ ................................ ......................15 
Table 10. 2020 LNG facility GHGRP Subpart C general stationary fuel combustion26 ...............16 
Table 11. NETL stationary combustion emission factors and distillate fuel life cycle emissions .16 
Table 12. NETL liquefaction estimate - speciated emissions ................................ .....................17 
Table 13. Comparison of NETL liquefaction stage GHG emissions intensity with other literature
 ................................ ................................ ................................ ................................ .................18 
Table 14. GCAM unadjusted and NETL aligned sector emissions for Defined Policies: Existing/FID 
Scenario (AR6, 100-yr basis) ................................ ................................ ................................ ....19 
Table 15. Model-year GCAM-NETL-aligned GHG emissions for DP: ExFID Scenario ...............20 
Table 16. Modeled, interpolated, and cumulative GCAM -NETL-aligned GHG emissions for DP: 
ExFID Scenario ................................ ................................ ................................ .........................20 
Table 17. Default values for natural gas upstream and liquefaction facility operations (example 
DP:MR vs. DP:ExFID) ................................ ................................ ................................ ...............25 
Table 18. Hypothetical example 1: High GHG intensity liquefaction project example (based on 
difference in defined policies scenarios, Market-Resolved vs. Existing/FID Exports) .................26 
Table 19. Hypothetical example 2: Low GHG intensity liquefaction project example (based on 
difference in current policies scenarios, Market-Resolved vs. Existing/FID Exports) .................27 
Table 20. Social cost of greenhouse gases for hypothetical example 1: High GHG intensity 
liquefaction [base year 2024, dollar year 2020] ................................ ................................ .........27

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-iii 
Table 21. Social cost of greenhouse gases for hypothetical example 2: Low GHG intensity 
liquefaction [base year 2024, dollar year 2020] ................................ ................................ .........28 
Table 22. Cumulative consequential GHG intensities of U.S. exports, LHV, AR6, 100-yr basis .29 
Table 23. Changes in cumulative social cost of greenhouse gases (SC-GHG), 2020$ ..............30 
Table 24. Normalized changes per MJ exported in cumulative social cost of greenhouse gases
 ................................ ................................ ................................ ................................ .................31 
Table 25. Summary of consequential GHG intensities and project non-direct emissions values for 
all scenarios (versus ExFID), AR6, 100-yr basis................................ ................................ ........32 
Table 26. Summary of consequential GHG intensities and project non-direct emissions values for 
all scenarios (versus ExFID), AR6, 20-yr basis ................................ ................................ .........33 
Table 27. Breakeven percent changes (versus ExFID), AR6, 100-yr basis ................................ 34 
Table 28 Breakeven percent changes (versus ExFID), AR6, 20-yr basis ................................ ...35 
Table 29. Sensitivity analysis for upstream methane emissions rate (U.S. base is 0.56%), DP:MR 
versus DP: ExFID ................................ ................................ ................................ .....................36 
Table 30. Sensitivity analysis results for additional liquefaction emissions ................................ 38 
Table 31. Summary of GCAM modeled services provided in selected defined policies scenarios
 ................................ ................................ ................................ ................................ .................39 
Table 32. Cumulative (2020 -2050) GCAM results for DP:ExFID and DP:MR (with increased 
services) ................................ ................................ ................................ ................................ ...39 
Table 33. Summary of GCAM results for DP:ExFID and DP:MR (with equivalent services) .......40 
Table 34. Cumulative consequential GHG intensities of U.S. exports (LHV, AR6, 100 -yr, 
equivalent services basis) ................................ ................................ ................................ .........41 
Table 35. Summary of market drivers of total consequential GHG intensity of increased U.S. LNG 
exports, cumulative change, 2020 - 2050 (LHV, AR6, 100-yr), direct emissions end use of U.S. 
LNG represented as unabated combustion (no CCS) ................................ ............................... 43 
Table 36. Summary of market drivers of total consequential GHG intensity of increased U.S. LNG 
exports, cumulative change, 2020 - 2050 (LHV, AR6, 100-yr), direct emissions end use of U.S. 
LNG represented as 90% CCS at end use ................................ ................................ ................44 
 
Table C-1.1. Matching NEMS (Oil and Gas Methane Partnership states) to NETL states and 
regions ................................ ................................ ................................ ................................ ......48 
Table C-1.2. Regional dry production (Tcf) between 2020 and 2050, DP:MR ............................50 
Table C-1.3. Regional NG dry production shares, DP:MR ................................ .........................50 
Table C-1.4. Regional NG dry production shares, DP:MR ................................ .........................50 
Table C-1.5. GHG emissions intensity by techno-basin, production through transmission network 
boundary using U.S. average transmission data (g CO2e/MJ, IPCC AR6, 100-yr GWP) ...........51 
Table C -1.6. Estimated U.S. average GHG intensity (g CO 2e/MJ) across NEMS scenarios, 
production through transmission (2020-2050) ................................ ................................ ...........52 
 
Table C-2.1. Provided set of GCAM data documentation ................................ ..........................53 
Table C-2.2. LCA stage cross-mapping ................................ ................................ .....................54 
Table C-2.3. GCAM emissions intensities for sectors (DP:MR, 2020, USA region, AR6, 100 -yr 
basis) ................................ ................................ ................................ ................................ ........56 
Table C-2.4. GWP values used in this analysis ................................ ................................ .........57 
Table C-2.5. GCAM emissions intensities for sectors (S1, 2020, U.S. region, AR6, 20 -yr basis)
 ................................ ................................ ................................ ................................ .................58 
Table C-2.6. Scaling factors used for service adjustment calculation relative to the existing/fid 
levels of LNG export ................................ ................................ ................................ .................59 
 
Table C-3.1. Annual Unrounded Values in 2023 SC-GHG Estimates, 2020-2080 (2020$ per metric 
ton of emissions) ................................ ................................ ................................ .......................60

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-iv 
Table C-3.2. Social cost of greenhouse gases results for Defined Policies (base year 2024, trillion 
2020$) ................................ ................................ ................................ ................................ ......61 
Table C-3.3. Social cost of greenhouse gases results for Commitments (base year 2024, trillion 
2020$) ................................ ................................ ................................ ................................ ......62 
Table C-3.4. Social cost of greenhouse gases results for Net Zero 2050 (base year 2024, trillion 
2020$) ................................ ................................ ................................ ................................ ......63 
Table C-3.5. Social cost of greenhouse gases results for Defined Policies (base year 2024, trillion 
2022$) ................................ ................................ ................................ ................................ ......64 
Table C-3.6. Social cost of greenhouse gases results for Commitments (base year 2024, trillion 
2022$) ................................ ................................ ................................ ................................ ......65 
Table C-3.7. Social cost of greenhouse gases results for Net Zero 2050 (base year 2024, trillion 
2022$) ................................ ................................ ................................ ................................ ......65 
 
Table C-4.1. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-100 Basis) ................................ ................................ ................................ ...........68 
Table C-4.2. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-100 Basis) ................................ ................................ ................................ ...........69 
Table C -4.3. Global Emissions Summary for Defined Policies: High Exports (GCAM -NETL-
Aligned, AR6-100 Basis) ................................ ................................ ................................ ...........70 
Table C -4.4. Global Emissions Summary for Defined Policies: High Middle East Supply: 
Existing/FID Exports (GCAM_NETL-Aligned, AR6-100 Basis) ................................ ..................71 
Table C-4.5. Global Emissions Summary for Defined Policies: High Middle East Supply: Model 
Resolved (GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....72 
Table C-4.6. Global Emissions Summary for Defined Policies: High U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ .......73 
Table C-4.7. Global Emissions Summary for Defined Policies: High U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................74 
Table C-4.8. Global Emissions Summary for Defined Policies: Low U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ .......75 
Table C-4.9. Global Emissions Summary for Defined Policies: Low U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................76 
Table C-4.10. Global Emissions Summary for Commitments (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................77 
Table C -4.11. Global Emissions Summary for Commitments (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................78 
Table C-4.12. Global Emissions Summary for Commitments (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-100 Basis) ................................ ................................ ................................ .79 
Table C -4.13. Global Emissions Summary for Commitments (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ .......80 
Table C-4.14. Global Emissions Summary for Commitments (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................81 
Table C-4.15. Global Emissions Summary for Commitments (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................82 
Table C-4.16. Global Emissions Summary for Net Zero 2050 (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................83 
Table C-4.17. Global Emissions Summary for Net Zero 2050 (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................84 
Table C-4.18. Global Emissions Summary for Net Zero 2050 (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-100 Basis) ................................ ................................ ................................ .85 
Table C-4.19. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ .......86

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-v 
Table C-4.20. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................87 
Table C-4.21.Global Emissions Summary for Net Zero 2050 (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) ................................ ................................ ....................88 
Table C-4.22. Global Emissions Summary for Defined Policies: Existing/FID Exports (GCAM -
NETL-Aligned, AR6-20 Basis) ................................ ................................ ................................ ...89 
Table C-4.23. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-20 Basis) ................................ ................................ ................................ .............90 
Table C-4.24. Global Emissions Summary for Defined Policies: High Exports (GCAM -NETL-
Aligned, AR6-20 Basis) ................................ ................................ ................................ .............91 
Table C -4.25. Global Emissions Summary for Defined Policies: High Middle East Supply: 
Existing/FID Exports (GCAM_NETL-Aligned, AR6-20 Basis) ................................ ....................92 
Table C-4.26. Global Emissions Summary for Defined Policies: High Middle East Supply: Model 
Resolved (GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ......93 
Table C-4.27. Global Emissions Summary for Defined Policies: High U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .........94 
Table C-4.28. Global Emissions Summary for Defined Policies: High U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ......................95 
Table C-4.29. Global Emissions Summary for Defined Policies: Low U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .........96 
Table C-4.30. Global Emissions Summary for Defined Policies: Low U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ......................97 
Table C-4.31. Global Emissions Summary for Commitments (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ......................98 
Table C -4.32. Global Emissions Summary for Commitments (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ......................99 
Table C-4.33. Global Emissions Summary for Commitments (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-20 Basis) ................................ ................................ ................................ . 100 
Table C -4.34. Global Emissions Summary for Commitments (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ....... 101 
Table C-4.35. Global Emissions Summary for Commitments (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 102 
Table C-4.36. Global Emissions Summary for Commitments (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 103 
Table C-4.37. Global Emissions Summary for Net Zero 2050 (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 104 
Table C-4.38. Global Emissions Summary for Net Zero 2050 (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 105 
Table C-4.39. Global Emissions Summary for Net Zero 2050 (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-20 Basis) ................................ ................................ ................................ . 106 
Table C-4.40. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ ....... 107 
Table C-4.41. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 108 
Table C-4.42. Global Emissions Summary for Net Zero 2050 (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) ................................ ................................ .................... 109 
Table C-4.43. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Defined Policies Scenarios (AR6-100 Basis) ................................ ................................ ....... 111 
Table C-4.44. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High Middle East Supply Scenarios (AR6-100 Basis) ................................ .................... 112

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-vi 
Table C-4.45. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High U.S. Supply Scenarios (AR6-100 Basis) ................................ ...............................  113 
Table C-4.46. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP Low U.S. Supply Scenarios (AR6-100 Basis) ................................ ................................  114 
Table C-4.47. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Commitments (High CCS) Scenarios (AR6-100 Basis) ................................ ....................... 115 
Table C-4.48. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Commitments (Moderate CCS) Scenarios (AR6-100 Basis) ................................ ................ 116 
Table C-4.49. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Net Zero 2050 (High CCS) Scenarios (AR6-100 Basis) ................................ ...................... 117 
Table C-4.50. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Net Zero 2050 (Moderate CCS) Scenarios (AR6-100 Basis) ................................ ............... 118 
Table C-4.51. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Defined Policies Scenarios (AR6-20 Basis) ................................ ................................ ......... 119 
Table C-4.52. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High Middle East Supply Scenarios (AR6-20 Basis) ................................ ...................... 120 
Table C-4.53. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High U.S. Supply Scenarios (AR6-20 Basis) ................................ ................................ . 121 
Table C-4.54. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP Low U.S. Supply Scenarios (AR6-20 Basis) ................................ ................................ .. 122 
Table C-4.55. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Commitments (High CCS) Scenarios (AR6-20 Basis) ................................ ......................... 123 
Table C-4.56. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Commitments (Moderate CCS) Scenarios (AR6-20 Basis) ................................ .................. 124 
Table C-4.57.Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Net Zero 2050 (High CCS) Scenarios (AR6-20 Basis) ................................ ........................ 125 
Table C-4.58. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of Net Zero 2050 (Moderate CCS) Scenarios (AR6-20 Basis) ................................ ................. 126

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-vii 
ACRONYMS AND ABBREVIATIONS 
°C Degrees Celsius 
AEO Annual Energy Outlook 
AgLanduse Agricultural land use 
AR5 Fifth Assessment 
Report 
AR6 Sixth Assessment 
Report 
AR6, 100-yr Sixth Assessment 
Report, 100-year basis 
AR6, 20-yr Sixth Assessment 
Report, 20-year basis 
Bcf, BCF Billion cubic feet 
Bcf/d Billion cubic feet per 
day 
BECCS Bioenergy with carbon 
capture and storage 
BIL Bipartisan Infrastructure 
Law 
BP British Petroleum 
Btu British thermal unit 
C2F6 Hexafluoroethane 
C Asia + East Eur Central Asia and 
Eastern Europe 
ccf Climate–carbon cycle 
Feedback 
CCS Carbon capture and 
storage 
CCUS Carbon capture, 
utilization, and storage 
CDR Carbon dioxide removal 
CF4 Tetrafluoromethane 
CH4 Methane 
CO2 Carbon dioxide 
CO2e Carbon dioxide 
equivalent 
DAC Direct air capture 
DACCS Direct air carbon 
capture and storage 
DOE Department of Energy 
EIA Energy Information 
Administration 
EJ Exajoule (1018 joules) 
EPA Environmental 
Protection Agency 
EU European Union 
F-gases Fluorinated gases  
FECM Office of Fossil Energy 
and Carbon 
Management 
g Gram 
GCAM  Global Change Analysis 
Model 
GDP Gross domestic product 
GHG Greenhouse gas 
GoM, GOM Gulf of Mexico 
Gt Gigaton 
GWP Global warming 
potential 
H2 Hydrogen 
HFC Hydrofluorocarbons 
HHV Higher heating value 
HMM Hydrogen Market 
Module 
IEA International Energy 
Agency  
IPCC Intergovernmental 
Panel on Climate 
Change 
IRA Inflation Reduction Act 
ITC Investment tax credit  
LAC Latin American 
countries 
LCA Life cycle analysis 
LHV Lower heating value 
LNG Liquefied natural gas 
LUC Land use change 
LULUCF Land use, land use 
change, and forestry 
LC-GHG Market adjustment 
factor 
MAM Macroeconomic Activity 
Module 
Mcf Million cubic feet 
MJ Megajoule

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-viii 
MMBtu Million British thermal 
units 
MMscf Million standard cubic 
feet 
N2O Nitrous oxide 
NA Not available/applicable 
NEMS National Energy 
Modeling System 
NERA  NERA Economic 
Consulting  
NETL National Energy 
Technology Laboratory 
NG Natural gas 
NGA Natural Gas Act 
NGP Natural gas processing 
NZ New Zealand 
O&M Operating and 
Maintenance 
OGSM Oil and Gas Supply 
Module 
PNNL Pacific Northwest 
National Laboratory 
PTC Production tax credit 
ROW Rest of the World 
SC-GHG Social cost of 
greenhouse gas 
emissions 
SF6 Sulfur hexafluoride 
Tcf, TCF Trillion cubic feet 
Tg Teragram (1012 grams) 
U.S., USA United States 
yr Year

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-1 
FOREWORD 
This multi-volume study of U.S. LNG exports serves to provide an updated understanding of the 
potential effects of U.S. LNG exports on the domestic economy, U.S. households and consumers; 
communities that live near locations where natural gas is produced o r exported; domestic and 
international energy security, including effects on U.S. trading partners; and the environment and 
climate. Prior to this study, Department of Energy’s ( DOE’s) most recent economic and 
environmental analyses of U.S. LNG exports wer e published in 2018 and 2019, respectively. At 
that time, U.S. LNG exports were just getting underway and our export capacity was 4 billion 
cubic feet per day (Bcf/d), less than one -third of what it is today. Since then, our world and the 
global natural gas sector have changed significantly: the U.S. has become the top global exporter 
of LNG; Russia has invaded Ukraine and used energy as a weapon to undermine European and 
global security; the impacts and costs of extreme weather and natural disasters fueled by climate 
change have increased dramatically; and the pace of the energy transition and technological 
innovation has itself accelerated.   
These developments and others factor into a global energy system that is changing rapidly. The 
pace of change creates inherent uncertainty in projecting the potential pathways for U.S. LNG 
through 2050. Accordingly, several considerations should be borne in mind when interpreting this 
study and its results.  
• Given the global scope and timeframe examined in this study, there should be recognition 
of the inherent uncertainty in conclusions, especially given their size relative to the overall 
global economy and energy system. 
• This study is not intended to serve as a forecast of U.S. LNG exports and impacts. Rather, 
it is an exercise exploring alternative conditional scenarios of future U.S. LNG exports and 
examining their implications for global and U.S. energy systems, economic systems, and 
greenhouse gas ( GHG) emissions. This type of scenario analysis is a well -established 
analytical approach for exploring complex relationships across a range of variables.  
• The scenarios explored in this study span a range of U.S. LNG export outcomes. Each 
scenario relies on input assumptions regarding many domestic, international, economic, 
and non-economic factors, such as future socioeconomic development, technology and 
resource availability, technological advancement, and institutional change. A full 
uncertainty analysis encompassing all underlying factors is beyond the scope of this study.  
• For the portions of this study that have modeled results, the study does not attach 
probabilities to any of the scenarios examined.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-2 
EXECUTIVE SUMMARY 
The U.S. Department of Energy (DOE) is responsible for authorizing exports of domestically 
produced natural gas, including liquefied natural gas (LNG), to foreign countries under section 3 
of the Natural Gas Act (NGA), 15 U.S.C. § 717b. An application to export domestically produced 
natural gas to countries that have a free trade agreement (FTA) with the United States must be 
granted without delay or modification and is deemed to be consistent with the public interest by 
statute. For applications to export domestic natural gas to non -FTA countries, DOE must grant 
the application unless it finds that the proposed exportation will not be consistent with the public 
interest. 
Since 2012, to inform its public interest determination, DOE’s Office of Fossil Energy and Carbon 
Management (FECM) has commissioned multiple studies to help assess the various facets of the 
public interest that are affected by U.S. LNG exports. The purpos e of the current study is to 
provide a comprehensive update to our understanding of how varying levels of U.S. LNG exports 
impact all these facets. 
This appendix provides a consequential analysis  and focuses on i) the current baseline GHG 
intensity of U.S. upstream natural gas and liquefaction processes, and ii) the global emissions 
impacts from changes in U.S. LNG exports through 2050 as provided in the Global Analysis 
(Appendix A). This analysis uses results from the Global Change Analysis Model (GCAM) and 
explores scenario comparisons of GHG emissions, level of U.S. LNG exports, and levels of global 
services provided. Global services are defined as those products of the global economy that 
provide services to consumers, such as energy, commodities, fertilizers, etc. 
Key findings of this Appendix are:  
1. Differences in volumes of U.S. LNG exports lead to different levels both of GHG emissions 
and of global services provided. When compared to scenarios that assume export levels 
based on existing and under construction facilities ( Existing/FID), higher levels of U.S. 
LNG exports lead to higher global GHG emissions (ranging from 21 Tg CO2e to 1,452 Tg 
CO2e or about 0.002% to 0.1% ), as well as higher levels of global services provided 
(ranging from 0.006% to about 0.1%). 
2. The GCAM upstream GHG intensity values for all scenarios are within 1% of the values 
in the latest  NETL Natural Gas baseline study (representative of the base year of this 
study, 2020) on an IPCC AR6, 100-yr basis.  
a. Per MJ of natural gas scaled to account for liquefaction losses, the production through 
transmission (upstream) GHG intensity is 9.2 g CO 2e/MJ exported on an IPCC AR6, 
100-yr GWP , LHV basis and 15.7 g CO2e/MJ exported on an IPCC AR6, 20-yr GWP , 
LHV basis.  
b. Overall, adjustments to align to NETL national average performance data for GHG 
intensity added about 20 Tg CO2e emissions per model year, an increase of less than 
0.05% on an AR6, 100-yr basis, and subtracted about 100 Tg CO 2e emissions per 
model year, a decrease of less than 0.2% on an AR6, 20-yr basis. 
3. The national average GHG intensity for liquefaction operations in the base year is 
modeled using government reported data and expanded to provide representative life 
cycle system boundaries, resulting in a GHG emissions intensity of 5.3 g CO 2e/MJ of 
natural gas ready for export, reported on an IPCC AR6, 100-yr lower heating value (LHV) 
basis, and 5.6 g CO2e/MJ on an IPCC AR6, 20-yr lower heating value (LHV) basis. 
4. This analysis defines the upstream natural gas and liquefaction processes as project 
direct emissions, the direct emissions from export and use of the natural gas and direct 
and indirect market effects as project non-direct emissions, and the sum of them to be the 
consequential GHG intensity of U.S. LNG exports. Given the upstream natural gas and

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-3 
liquefaction values estimated above, the average U.S. project direct emissions for 2020, 
the baseline year for this study, is 9.2 + 5.3 = 14.5 g CO 2e/MJ (AR6, 100-yr), and 21.3 g 
CO2e/MJ (AR6, 20-yr). 
5. The consequential GHG intensity is the effect (inclusive of both direct and indirect 
emissions) of U.S. LNG on global emissions per unit of U.S. LNG exported. The 
consequential GHG intensity is defined as the difference in GHG emissions between the 
scenarios divided by the difference in U.S. LNG exports. For instance, for one of the 
scenario comparisons assessed ( Defined Polices: Model Resolved ) the consequential 
GHG intensity is +6.3 g CO2e/MJ (on both an AR6, 100-yr and AR6, 20-yr basis), indicating 
that the overall global effect of producing and exporting U.S. LNG leads to an increase in 
global GHG emissions resulting from consequential market effects.  
a. Analysis of the results shows that direct and indirect market substitutions result in a 
decrease in global GHG emissions intensity when compared on an equivalent global 
services basis. The increased availability of U.S. LNG on the global market enables 
increased demand for energy to be met with a lower cost energy supply option that 
often displaces more or equally GHG emissions -intensive fuels (e.g., coal and oil) 
within the model over the thirty-year study period. 
b. Results also show that increasing the availability of U.S. LNG on the global market 
(increased global energy supply) results in increased consumption of global services 
when compared to the baseline scenario ( e.g., Defined Policies: Existing/FID). The 
consequential effect of increased global consumption of energy and services directly 
contributes to increased global GHG emissions.  
c. The net result of these two market effects is an increase in global GHG emissions of 
+6.3 g CO2e/MJ of NG exported from the U.S. Across all scenarios, this GHG intensity 
figure ranges from 1.2 g CO2e/MJ to 12.6 g CO2e/MJ (AR6, 100-yr basis), and from -
1.4 g CO2e/MJ to 11.2 g CO2e/MJ (AR6, 20-yr basis). 
d. The increase in global GHG emissions between the Defined Policies: Model Resolved 
and Defined Policies: Existing/FID scenarios is estimated to result in a cumulative SC-
GHG impact of $74 billion using a discount rate of 2.5%, $130 billion using a discount 
rate of 2.0%, and $220 billion using a discount rate of 1.5% (all 2020$). Per MJ, this 
equates to a range of 0.02 cents/MJ to 0.15 cents/MJ (2.5%). The cumulative SC -
GHG of the increase in global emissions  across the study scenarios ranged from $3 
billion to $150 billion (2.5%) to $12 billion to $450 billion (1.5%) in 2020$.  
6. Estimated consequential GHG impacts and SC-GHG values for an individual U.S. export 
project can be calculated by using individual project values in place of the default of U.S. 
average values modeled in the study. 
a. For example, on an AR6, 100-yr basis, given the NETL average liquefaction 
emissions for a project of 5.3 g CO2e/MJ, if an individual project has a liquefaction 
process with emissions that are half of the average (2.65 g CO2e /MJ), the individual 
project consequential GHG intensity could be adjusted down by 2.65 g CO2e/MJ 
(calculated as the difference between the average of 5.3 g CO2e/MJ and the 
individual project emissions intensity of 2.65 g CO2e/MJ). If the average U.S. 
consequential GHG intensity is 6.3 g CO2e /MJ, the individual project consequential 
intensity would be 3.65 g CO2e /MJ. 
b. Total lifetime social costs of the project direct and project non -direct greenhouse gas 
emissions from a 1 Bcf/d facility operating for 30 years are estimated to be $8 billion 
to $23 billion ($2020) for a facility with default average intensity values (varying across 
assumed discount rates). A similar facility with half the liquefaction emissions would 
have social costs of greenhouse gases estimated to be $4.6 billion to $13  billion 
($2020).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-4 
BACKGROUND 
This portion of the study utilizes the global greenhouse gas (GHG) emissions and U.S. liquefied 
natural gas (LNG) export volumes determined from the Global Change Analysis Model (GCAM) 
(detailed in Appendix A with a description of its application to this analysis in Appendix C-2) for 
each scenario considered within the study to determine the consequential life cycle GHG 
emissions on a per unit (Megajoule [MJ]) of U.S LNG exported. The life cycle analysis (LCA) 
modeling approach used in this study is referred to as a “consequential LCA”.1,2,3 This type of LCA 
accounts for the direct emissions from production, delivery, and use of the U.S. exported natural 
gas and the indirect emissions from changes in market behavior. Market behavior includes 
consequences from the decision to use U.S. exported natural gas to meet demands for provision 
of global services (e.g., energy, commodities, fertilizers, etc.) , including fuel substitution and 
changes in demand for services. 
The consequential LCA approach used in this study differs from past DOE LNG LCA modeling 
approaches. Prior DOE LNG LCA studies conducted by the National Energy Technology 
Laboratory (NETL)4 and used to evaluate LNG project applications 5 directly compared the life 
cycle GHG emissions for producing and consuming a megawatt -hour (MWh) of baseload 
electricity in European and Asian markets using: (1) U.S. LNG exported from the Gulf Coast of 
the U.S.; (2) LNG exported from Oran, Algeria; (3) pipeline natural gas from Yamal, Russia; and 
(4) regionally-sourced coal. This type of LCA is referred to as an “attributional LCA”.  
An attributional LCA directly compares the environmental performance of each supply chain (e.g., 
LNG, pipeline natural gas, coal) to produce an equivalent service to society (e.g., 1 MWh of 
electricity)6. An attributional LCA modeling approach does not account for changes in market 
behavior in response to fuel availability. Comparing attributional LCA results provides information 
about the difference in environmental performance to provide an equivalent s ervice to society. 
The comparative difference is the result of one form of energy completely replacing another form 
in the market, often referred to as direct market substitution. Attributional LCA results do not seek 
to provide information about the potential indirect market effects from changes in supply and price 
resulting from a decision to use one form of energy over the other, nor do they provide information 
 
1 Ekvall, T. (2002). Cleaner production tools: LCA and beyond. Integrating Greener Product Development 
Perspectives, 10(5), 403–406. https://doi.org/10.1016/S0959-6526(02)00026-4  
2 Brandão, M., Weidema, B. P., Martin, M., Cowie, A., Hamelin, L., & Zamagni, A. (2024). Consequential 
Life Cycle Assessment: What, Why and How? In M. A. Abraham (Ed.), Encyclopedia of Sustainable 
Technologies (Second Edition) (pp. 181–189). Elsevier. https://doi.org/10.1016/B978-0-323-90386-
8.00001-2  
3 UNEP SETAC. (2011). Global guidance principles for life cycle assessment databases: a basis for 
greener processes and products. United Nations Environment Programme. https://www.lifecycle 
initiative.org/ wp-content/ uploads/2012/12/2011%20-%20Global%20Guidance%20Principles.pdf 
4 Khutal, H., et al. Life Cycle Analysis of Natural Gas Extraction and Power Generation: U.S. 2020 
Emissions Profile. National Energy Technology Laboratory, Pittsburgh, December 2024. 
https://www.netl.doe.gov/energy-analysis/details?id=546d4009-c43b-43f5-bcc9-64d5e63fc8d5 
5 Roman-White, S., Rai, S., Littlefield, J., Cooney, G., & Skone, T. J. (2019). Life cycle greenhouse gas 
perspective on exporting liquefied natural gas from the Unites States: 2019 update. NETL, Pittsburgh, 
September 12, 2019. 
6 An attributional Life Cycle Assessment (LCA) comparison is done for systems that provide equivalent 
services to society, i.e., an equivalent function (e.g., the 1 MWh mentioned above). In this study, the 
boundary is far larger than that of a typical LCA, and thus the total of all services provided globally, and 
annually over a 30-year study period, is considered. This study will show how the level of global services 
change across scenarios to help to assess whether equivalent services are being provided.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-5 
about how supply or demand for global services could change resulting from changes in supply 
and price. 
DOE has acknowledged that prior attributional LNG LCA results did not account for potential 
direct or indirect market effects. This study, by contrast, does consider reasonably foreseeable 
market effects using an integrated multisector model, GCAM, to bett er understand the market 
substitution (both direct and indirect) and changes in levels of global services provided (e.g., 
change in global energy or commodity consumption) that results from the increased availability 
of U.S. LNG on the global market. The GCAM model includes all GHG emissions from extraction, 
liquefaction, and use of the LNG, as well as all GHG emissions associated with global services 
produced. Consequential LCA results are reported with information about the change in global 
services to illuminate these differences when comparing results.  
A trade-off of the consequential modeling approach used in this study is a reduction in attribution 
for specific source -to-consumption pathways, as previously modeled and used by DOE. 
Therefore, as a result of the consequential life cycle modeling approach, this study does not 
present comparative results of natural gas compared to coal for production of a MWh of electricity, 
or other direct source-to-consumption pathways.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-6 
CONSEQUENTIAL LCA MODELING APPROACH FOR ASSESSING GHG EMISSIONS 
FROM INCREASED U.S. LNG EXPORTS 
The objective of the consequential LCA component of this study  is to estimate the direct and 
indirect market effects of additional U.S. LNG exports to better understand their effect on global 
GHG emissions. 
Two metrics are used to assess the consequential GHG emissions effects of increased U.S. LNG 
exports: (1) GHG intensity in carbon dioxide equivalents (CO 2e) using International Panel on 
Climate Change (IPCC) Sixth Assessment Report (AR6) global warming potentials (GWPs) - on 
100-year (AR6, 100-yr) and 20-year (AR6, 20-yr) time frames; and (2) social cost of greenhouse 
gas emissions (SC -GHG) using the estimates and methodology developed by the U.S. 
Environmental Protection Agency (EPA) in the regulatory analysis of its December 2023 Final 
Rule, “Standards of Performance for New, Reconstructed, and Modified Sources and Emissions 
Guidelines for Existing Sources: Oil and Natural Gas Sector Climate Review,” (2023 SC -GHG 
estimates).7 
This analysis establishes a GHG intensity performance of U.S. natural gas production and 
delivery to liquefaction plants and U.S. average liquefaction plant GHG emissions intensity 
performance in 2020 as a reference benchmark. The reference year of 2020 aligns with the start 
of the study period for market consequences derived from the GCAM model. 
A second objective of the LCA study is to determine the market drivers of the change in global 
GHG emissions with respect to changes in U.S. LNG export GHG intensity when providing an 
equivalent service to society (excluding increases in global services). 
The consequential LCA modeling approach consists of ten data conversion and interpretation 
steps, each of which is described in more detail below: 
1. Obtain study scenario GHG emissions and U.S. LNG export volumes from GCAM. 
2. Obtain national average life cycle GHG performance data for U.S. natural gas (from NETL 
natural gas baseline). 
3. Model national average life cycle GHG performance for U.S. liquefaction plants 
(developed as part of this study). 
4. Align GCAM natural gas production and pipeline transport to U.S. national average GHG 
performance in the baseline year. 
5. Calculate GCAM-NETL-aligned global GHG emissions results (for modeled years 2020 -
2050) 
6. Interpolate GCAM-aligned global GHG emissions and U.S. LNG export volumes from 5 -
year GCAM modeled time steps to annual values for the study period of 2020 to 2050. 
7. Calculate GCAM-NETL-aligned consequential GHG intensity per unit of U.S. LNG export 
(normalized over the study period of 2020 to 2050). 
8. Subtract the U.S. national average upstream natural gas and liquefaction plant 
performance to determine the project non-direct emissions intensity. 
 
7 DOE has preliminarily determined that the updated 2023 SC-GHG estimates, including the approach to 
discounting, represent a significant improvement in estimating the SC-GHG through incorporating the 
most recent advancements in the scientific literature and by addressing recommendations on prior 
methodologies. DOE explained the basis for its determination and made it available for public comment in 
a July 2024 NODA for consumer gas-fired instantaneous water heaters, 89 FR 59693, 59700. As DOE 
explained in the July 2024 NODA, the 2023 SC-GHG estimates represent a significant improvement 
because the 2023 SC-GHG estimates implement the key recommendations of the National Academies, 
and they incorporate the extensive scientific findings and methodological advances that have occurred 
since the last IWG substantive updates in 2013, 2015, and 2016.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-7 
9. Add the project direct emissions intensity (U.S. LNG project upstream natural gas supply 
and liquefaction plant GHG performance) to the project non-direct emissions intensity to 
determine individual project GHG emissions intensity inclusive of consequential market 
effects. 
10. Demonstrate estimation of consequential GHG intensity and SC -GHG for an individual 
U.S. LNG project. 
The sections below describe one potential modeling approach that shows initial example results 
using a consistent and specific set of scenarios within one global climate policy generated by the 
GCAM model for this study. Complete results for each scenario comparison are provided in the 
Results section and detailed tables in Appendix C-4.  
Step 1: Obtain Study Scenario GCAM GHG Emissions and U.S. LNG Export 
Results from GCAM 
This consequential analysis considers scenarios designed for this study with varying assumptions 
about future climate policy ambition, technology availability, and level of U.S. LNG exports 
(summarized in Table 1 and further defined in Appendix A). This study does not attach probabilities 
to any of the scenarios, and no inference about the relative likelihood of these scenarios occurring 
should be made.  
Table 1. Scenario design and summary 
Key Assumptions  
Scenario full name  Scenario abbreviation  Global climate policies Technology availabilitya U.S. LNG export levels 
Defined 
Policies  
  Model Resolved  Defined Policies: Model Resolved  DP: MR  
  Existing/FID Exportsc  Defined Policies: Existing/FID Exports  DP: ExFID  
  High Exports  Defined Policies: High Exports  DP: Hi Exp  
Commitments  
High CCS  
Model Resolved  Commitments (High CCS): Model Resolved  C (High CCS): MR  
Existing/FID 
Exports  
Commitments (High CCS): 
Existing/FID Exports  C (High CCS): ExFID  
High Exports  Commitments (High CCS): High Exports  C (High CCS): Hi Exp  
Moderate 
CCS  
Model Resolved  Commitments (Moderate CCS): Model Resolved  C (Mod CCS): MR  
Existing/FID 
Exports  
Commitments (Moderate 
CCS): Existing/FID Exports  C (Mod CCS): ExFID  
High Exports  Commitments (Moderate CCS): High Exports  C (Mod CCS): Hi Exp  
Net Zero 2050  
High CCS  
Model Resolved  Net Zero 2050 (High CCS): Model Resolved  NZ (High CCS): MR  
Existing/FID 
Exports  
Net Zero 2050 (High CCS): 
Existing/FID Exports  NZ (High CCS): ExFID  
High Exports  Net Zero 2050 (High CCS): High Exports  NZ (High CCS): Hi Exp  
Moderate 
CCSb  
Model Resolved  Net Zero 2050 (Moderate CCS): Model Resolved  NZ (Mod CCS): MR  
High Exports  Net Zero 2050 (Moderate CCS): High Exports  NZ (Mod CCS): Hi Exp

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-8 
Notes: 
a Technology availability assumptions (High CCS and Moderate CCS) are combined only with Commitments and Net 
Zero 2050 climate policy ambition assumptions.  
b  In the Net Zero 2050 (Moderate CCS): Model Resolved scenario, U.S. LNG exports fall below the existing/FID exports 
level. Thus, a Net Zero 2050 (Moderate CCS): Existing/FID Exports  scenario would resolve to the same outcomes 
as the Net Zero 2050 (Moderate CCS): Model Resolved  scenario and is therefore not shown (and not used in this 
consequential analysis).  
c  Existing/FID exports  refer to LNG capacity of currently operational LNG projects or LNG projects with export 
authorizations from DOE that have reached final investment decisions (FID) on their projects.  
In the broader study, the NEMS and GCAM models were used to represent economic and 
environmental changes associated with the defined changes in U.S. LNG exports. The NEMS 
modeling focused on domestic changes that would be expected to occur in the scenarios 
modeled, but results from NEMS were not used as a part of this consequential analysis.8  
Additional sensitivity scenarios on levels of domestic and rest of world natural gas production for 
the Defined Policies scenarios are listed in Table 2. 
Table 2. Additional sensitivity scenarios in this study 
Global 
climate 
policies 
Natural gas 
resources 
U.S. LNG 
export levels 
Sensitivity scenarios full 
name 
Sensitivity scenario 
abbreviation 
Defined 
Policies  
High U.S. Supply Model Resolved DP High U.S. Supply: Model Resolved DP Hi US Sup: MR 
High U.S. Supply Existing/FID Exports DP High U.S. Supply: Existing/FID Exports DP Hi US Sup: ExFID 
Low U.S. Supply Model Resolved DP Low U.S. Supply: Model Resolved DP Lo US Sup: MR 
Low U.S. Supply Existing/FID Exports DP Low U.S. Supply: Existing/FID Exports DP Lo US Sup: ExFID 
High Middle East 
Supply 
Model 
Resolved 
DP High Middle East 
Supply: Model Resolved DP Hi ME Sup: MR 
High Middle East 
Supply 
Existing/FID 
Exports 
DP High Middle East 
Supply: Existing/FID 
Exports 
DP Hi ME Sup: ExFID 
 
Results from all scenarios in Table 1 and Table 2 were provided to NETL as output files with results 
for each model year (i.e., in five-year increments from 2020-2050). Across all years and scenarios, 
GCAM has about 100 discrete sectors, hundreds of discrete technologies, and many sector -
technology pairs that can vary depending on the model configuration. However, only a subset of 
these sectors is relevant to this analysis (i.e., to the natural gas sectors). Detailed discussion of 
the formats and structures of received GCAM files is included in Appendix C-2. 
Table 3 summarizes cumulative data for model year (2020-2050) including GHG emissions, U.S. 
LNG export volumes, and summary measures of global services from GCAM for the scenarios in 
Table 1. By default, GHG values in this study are shown using IPCC AR6, 100-year GWP values. 
 
8 NETL reviewed the NEMS data to evaluate the magnitude of changes to the regional production mix of 
natural gas over time to assess whether the GHG intensity of U.S. natural gas produced would change as 
a result of production mix changes. No significant change in intensity was found (see Appendix C-1 for 
details).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-9 
Where noted, IPCC AR6, 20-yr GWP values are also provided.9 Shown here are GHG emissions 
in Teragrams of CO2-equivalents (Tg CO2e). The global services index is an aggregate weighted 
metric that summarizes the total services provided to global society as a result of the economic 
activity modeled in the scenarios over the 2020 -2050 period where, by assumption, the ExFID 
scenario has a value of 1.00 within each Global Climate Policy set of scenarios (see Appendix C-
2 for details). 
Table 3. Summary of cumulative model year (every five years, 2020-2050) U.S. LNG exports, 
GHG emissions, and global services from GCAM  
Scenario 
Geographical Scope / Global Service Type 
Global 
Weighted 
Index 
Global U.S. Global Global Industrial Global Transportation 
GHG 
Emissions 
(AR6, 100-yr) 
(Tg CO₂e) 
LNG 
Export 
Volumes 
(EJ) 
Energy 
Services 
(EJ) 
Commodity 
Products 
(Mt) 
Nitrogen 
Fertilizer 
(Mt) 
Freight, 
Million Ton-
Kilometers 
(Mt-km) 
Passenger, 
Million 
Passenger-
Kilometers  
(Mp-km) 
DP: Hi Exp 351,607 95 2,376 39,752 1,144 1.53E+09 1.78E+09 1.0015 
DP: MR 351,444 77 2,374 39,740 1,144 1.53E+09 1.78E+09 1.0008 
DP: ExFID 351,286 50 2,372 39,725 1,145 1.52E+09 1.78E+09 1.0000 
  
DP: Hi ME Sup: 
MR 352,433 74 2,382 39,801 1,143 1.53E+09 1.78E+09 1.00047 
DP: Hi ME Sup: 
ExFID 352,356 50 2,381 39,792 1,143 1.53E+09 1.78E+09 1.0000 
  
DP Hi US Sup: 
MR 351,649 88 2,376 39,750 1,144 1.53E+09 1.78E+09 1.00127 
DP Hi US Sup: 
ExFID 351,377 50 2,372 39,727 1,145 1.53E+09 1.78E+09 1.0000 
  
DP Lo US Sup: 
MR 350,692 53 2,370 39,720 1,145 1.52E+09 1.77E+09 1.00010 
DP Lo US Sup: 
ExFID 350,683 49 2,369 39,717 1,145 1.52E+09 1.77E+09 1.0000 
  
C (High CCS): 
Hi Exp 283,821 74 2,289 37,152 1,157 1.43E+09 1.76E+09 1.0009 
C (High CCS): 
MR 283,677 56 2,287 37,137 1,157 1.43E+09 1.76E+09 1.0002 
C (High CCS): 
ExFID 283,657 49 2,287 37,133 1,158 1.43E+09 1.76E+09 1.0000 
  
C (Mod CCS): Hi 
Exp 270,432 69 2,254 35,460 1,131 1.38E+09 1.76E+09 1.0008 
C (Mod CCS): 
MR 270,432 51 2,252 35,454 1,131 1.38E+09 1.76E+09 1.0001 
C (Mod CCS): 
ExFID 270,189 48 2,252 35,453 1,131 1.38E+09 1.76E+09 1.0000 
  
NZ (High CCS): 
Hi Exp 240,973 70 2,237 35,611 1,158 1.37E+09 1.76E+09 1.0008 
NZ (High CCS): 
MR 240,923 52 2,236 35,594 1,158 1.37E+09 1.76E+09 1.0001 
NZ (High CCS): 
ExFID 240,919 48 2,235 35,592 1,158 1.37E+09 1.76E+09 1.0000 
 
9 The use of GWP values converts emissions of distinct greenhouse gases into a single index of carbon 
dioxide equivalents to represent the global warming impact of the varied gases. The IPCC AR6, 100-yr 
GWP values (units kg CO2e/kg gas) used are: fossil CH4 (29.8), non-fossil CH4 (27.2), and N2O (273). 
See Appendix C-2 for GWP values used for other greenhouse gases (e.g., F-gases) and IPCC reports.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-10 
Scenario 
Geographical Scope / Global Service Type 
Global 
Weighted 
Index 
Global U.S. Global Global Industrial Global Transportation 
GHG 
Emissions 
(AR6, 100-yr) 
(Tg CO₂e) 
LNG 
Export 
Volumes 
(EJ) 
Energy 
Services 
(EJ) 
Commodity 
Products 
(Mt) 
Nitrogen 
Fertilizer 
(Mt) 
Freight, 
Million Ton-
Kilometers 
(Mt-km) 
Passenger, 
Million 
Passenger-
Kilometers  
(Mp-km) 
  
NZ (Mod CCS): 
Hi Exp 224,035 61 2,195 33,244 1,119 1.30E+09 1.76E+09 1.0005 
NZ (Mod CCS): 
MR 224,035 43 2,194 33,244 1,119 1.30E+09 1.76E+09 1.0000 
NZ (Mod CCS): 
ExFID 223,831 43 2,194 33,244 1,119 1.30E+09 1.76E+09 1.0000 
Notes: 
• The values in this table reflect the sums of the 5-year interval data provided by the GCAM output for the years 2020-
2050. 
• Global energy services include: agricultural energy use, commercial cooking, commercial cooling, commercial 
heating, commercial hot water, commercial non -building, commercial office, commercial other, commercial others, 
commercial refrigeration, residential computers, residential cooking, residential cooling, residential freezers, 
residential furnace fans, resid ential heating, residential hot water, residential other, residential others, residential 
refrigerators, residential televisions, chemical energy use, chemical feedstocks, construction energy use, 
construction feedstocks, mining energy use, other industria l energy use, other industrial feedstocks, process heat 
cement 
• Conversion of annual values from EJ/year to Bcf/d is 1:2.7759 
• Global commodities products include production of aluminum, alumina, cement, and iron & steel. 
• Freight transportation includes freight and international shipping. 
• Passenger transportation includes ground and aviation. 
• The weighted index is not provided in the GCAM results  but was created in collaboration with the GCAM modeling 
team and is included here to summarize the global services results. 
Step 2: Obtain U.S. Natural Gas National Average Life Cycle GHG Performance 
(from NETL Natural Gas Baseline)  
The 2024 NETL natural gas baseline study 10 describes the GHG emissions due to production, 
gathering and boosting, processing, transmission, storage, and distribution of domestic U.S. 
natural gas to consumers and is representative of the year 2020, which aligns with the temporal 
representation of upstream natural gas processes of this study period (2020-2050). These natural 
gas supply chain stages (or industry segments) generally align with categories used in other 
federal efforts, such as EPA’s Greenhouse Gas Reporting Program (GHGRP)11 and Greenhouse 
Gas Inventory.12 Results of this study are provided for two main scopes: production through 
transmission (end users after transmission typically include industrial and power sectors that 
receive natural gas via transmission pipeline directly), and production through distr ibution (end 
users after distribution typically include a combination of residential, commercial, industrial, and 
power sectors, where natural gas is delivered through the distribution pipeline network). 
Quantitatively, the NETL natural gas baseline reports estimated ranges of GHG emissions 
intensities for each species (i.e., type of gas molecule) of GHG emission and for each stage of 
the domestic natural gas supply chain following the principles of attributional LCA. For the scope 
 
10 Khutal, H., et al. Life Cycle Analysis of Natural Gas Extraction and Power Generation: U.S. 2020 
Emissions Profile. National Energy Technology Laboratory, Pittsburgh, December 2024. 
https://www.netl.doe.gov/energy-analysis/details?id=546d4009-c43b-43f5-bcc9-64d5e63fc8d5 
11 U.S. EPA, Greenhouse Gas Reporting Program, https://www.epa.gov/ghgreporting, last accessed Sept 
1, 2023. 
12 U.S. EPA, Inventory of U.S. Greenhouse Gas Emissions and Sinks,  
https://www.epa.gov/ghgemissions/inventory-us-greenhouse-gas-emissions-and-sinks, last accessed 
Sept 1, 2023.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-11 
of domestic natural gas production through the transmission stage, the U.S. average GHG 
emissions intensity is estimated at 7.79 grams (g) CO2e/megajoule (MJ) (with a 95 percent mean 
confidence interval of 4.6–11.1 g CO2e/MJ, using IPCC AR6, 100-yr GWP values, higher heating 
value [HHV] basis) or about 8.63 g CO2e/MJ (with a 95 percent mean confidence interval of 5.4 g 
CO2e/MJ –12.8 g CO2e/MJ, using the IPCC AR6, 100-yr GWP values, lower heating value [LHV] 
basis).13,14  
The production through transmission boundary represents emissions associated with natural gas 
delivered to liquefaction plants (plant input). However, due to natural gas consumption and losses 
at the liquefaction stage, the amount of natural gas delivered to a liquefaction plant is higher than 
the amount of natural gas throughput/exported (plant output). Adjusting from a “per MJ of NG 
delivered to liquefaction plant” (plant input) to “per MJ of NG through liquefaction plant” (plant 
output) basis, results in a h igher upstream GHG emissions intensity  value. As a result, the 
production through transmission (upstream) GHG intensity on a per MJ NG throughput from 
liquefaction plant basis is 9.2 g CO2e/MJ Exported (IPCC AR6, 100-yr GWP , LHV basis).15  
Step 3: Model U.S. Liquefaction Plant National Average Life Cycle GHG 
Performance 
As part of this study, a new national average life cycle GHG performance for U.S. liquefaction 
operations in the year 2020 was modeled to align the temporal representation of the liquefication 
data to the study period (2020 -2050) and the U.S. national average for upstream natural gas 
production and delivery  described in Step 2. U.S. Environmental Protection Agency’s GHGRP 
data representative of year 2020 emissions were used as the basis with adjustments to account 
for certain missing emission sources in GHG RP that are discussed in more detail below, while 
ensuring alignment with combustion emission factors modeled in the NETL natural gas baseline 
LCA.  
The resulting national average liquefaction process GHG emissions intensity for the year 2020 is 
5.27 (or 5.3) g CO2e/MJ (LHV) and is referred to as the 2024 NETL estimate throughout the rest 
of this section. 
Six facilities reported to GHGRP for the 2020 data year  and exported natural gas, as shown in 
Table 4. For the data tables and calculations shown for calculating the 2024 NETL estimate, only 
data from these six export facilities are used. These export volumes were also used to weight the 
calculated or reported facility-level GHG emissions. 
 
13 The rest of this report expresses GHG emissions intensity values on a lower heating value (LHV) basis 
(unless explicitly specified otherwise) to ensure alignment with the energy content basis used by the 
Global Change Analysis Model (GCAM). 
14 The higher heating value (HHV) of a fuel includes the heat released if all of the water vapor in the 
combustion products were condensed, while the lower heating value (LHV) is the heat released if all of 
the water vapor remained as vapor. A conversion factor of 1.108 MJ higher (HHV) basis per MJ lower 
(LHV) basis was used throughout the steps of this analysis. 
15 As per the updated NETL liquefaction stage modeling, around 1.07 kg of NG is delivered to the 
liquefaction plant per 1 kg of NG throughput from the plant.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-12 
Table 4. 2020 LNG facility export volumes as reported in GHGRP Subpart W16 
LNG Facility Name Quantity Exported (MMcf) 
SLNG Elba Island Terminal 36,272 
Sabine Pass LNG Terminal 926,901 
Cove Point LNG Facility 233,227 
Freeport 421,381 
Corpus Christi Liquefaction 395,716 
Cameron LNG LLC 385,662 
 
Facility-level GHG emissions are summarized by GHGRP, allowing a direct calculation of carbon 
intensity for all facilities, shown in Table 5. 
The speciated, summary emissions for each facility reported by GHGRP are shown in the AR4, 
100-yr columns in the table. These are then converted to AR6 , 100-yr to match this study (see 
Appendix C-2 for GWP values). LNG production is reported to GHGRP in terms of thousand cubic 
feet of gas, which is converted here to mass of LNG. The annual emissions and LNG production 
are used to calculate the speciated, AR6, 100-yr emission intensities, followed by the total in the 
last column. The production-weighted intensities are calculated in the bottom row  based on the 
facility-specific information. 
GHGRP data have known data gaps with regards to natural gas liquefaction facilities, including 
not accounting for GHG emissions from acid gas removal units  (AGRU) and electricity 
consumption for compressors (as indicated by the low 2020 GHGRP GHG emissions intensity of 
the electric-driven Freeport LNG plant in Table 5).  
Table 5. 2020 LNG facility GHG emissions as summarized in GHGRP17 
 
AR4, 100-yr, as-reported 
(Mt CO₂e/yr) 
AR6, 100-yr, converted 
(Mt CO₂e/yr) 
LNG 
Production, 
converted 
(Mt) 
Emission Intensity, 
calculated 
AR6, 100-yr 
(kg CO2e/kg LNG) 
AR6, 100-yr 
Emissions 
Intensity 
(kg CO2e/ 
kg LNG) 
U.S. LNG 
Facility Name CO₂ CH₄ N₂O CO₂ CH₄ N₂O CO₂ CH₄ N₂O Total 
SLNG Elba 
Island 
Terminal 
77,054 4,471 41 77,054 5,329 38 730,500 0.105 7.29E-03 5.19E-05 0.113 
Sabine Pass 
LNG Terminal 4,127,013 29,905 2,314 4,127,013 35,647 2,120 18,667,328 0.221 1.91E-03 1.14E-04 0.223 
Cove Point 
LNG Facility 1,120,158 4,616 614 1,120,158 5,502 562 4,697,068 0.238 1.17E-03 1.20E-04 0.240 
Freeport 52,688 5,664 27 52,688 6,752 25 8,486,405 0.006 7.96E-04 2.90E-06 0.007 
Corpus Christi 
Liquefaction 1,774,907 20,083 997 1,774,907 23,938 913 7,969,529 0.223 3.00E-03 1.15E-04 0.226 
Cameron LNG 
LLC 3,092,913 46,931 1,729 3,092,913 55,942 1,584 7,767,049 0.398 7.20E-03 2.04E-04 0.406 
       
Production 
Weighted 
Avg 
0.212 9.24E-05 3.97E-07 0.215 
 
 
16 U.S. EPA Greenhouse Gas Reporting Program (2021). Subpart W Reporting Year 2020. Available at 
www.epa.gov/ghgreporting. Date accessed: October 15, 2024. 
17 U.S. EPA Greenhouse Gas Reporting Program (2023). Summary GHG Data 2020. 
https://www.epa.gov/system/files/other-files/2023-12/ghgp_data_2020.xlsx. Date accessed: October 15, 
2024.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-13 
Additionally, there are minor differences in the combustion factors used in the calculation of 
emissions from GHGRP Subpart C 18 data and those used by NETL in its LNG modeling. To 
address these limitations, the following steps were taken: 
• When natural gas arrives at the LNG facility, it often contains some small amount of carbon 
dioxide that needs to be removed using acid gas removal  before the low -temperature 
liquefaction process. In general, the CO2 from acid gas removal (AGR) is simply vented to 
the atmosphere after being removed.  These AGR CO 2 venting emissions have been 
estimated and incorporated within the GHG emissions profile of each liquefaction facility 
using the appropriate regional post -processing NG compositions reported in the natural 
gas baseline report and assuming that all CO 2 is removed from the pipeline gas and 
vented. The facilities are first aligned to an appropriate production region (either southeast 
or southwest) from the 2024 NETL natural gas baseline study, and then the post -
processing natural gas composition is used t o assign the mass fraction of CO 2 in the 
natural gas entering AGR (southeast – 0.261 kg CO 2/kg NG and southwest – 0.405 kg 
CO2/kg NG19). The mass of CO2 removed is then calculated as: 
 
𝑚𝑎𝑠𝑠 𝐶𝑂2 𝑟𝑒𝑚𝑜𝑣𝑒𝑑 = 𝑚𝑎𝑠𝑠 𝑓𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝐶𝑂2 ⋅ 𝑚𝑎𝑠𝑠 𝑓𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝐿𝑁𝐺 𝑒𝑥𝑝𝑜𝑟𝑡1 − 𝑚𝑎𝑠𝑠 𝑓𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝐶𝑂2  
These data are summarized in Table 6, where the mass values are in metric tons (equal to Mg). 
Table 6. 2020 LNG facility calculated CO2 emissions from acid gas removal units20 
U.S. LNG Facility Name  
2024 NETL 
Natural Gas 
Baseline Study 
Production 
Region 
Mass Fraction 
CO₂ in Gas 
Entering AGU 
Facility 
LNG Mass 
Exported 
(Mt) 
Mass CO₂ 
Removed 
(Mt/yr) 
SLNG Elba Island Terminal Southeast 0.26% 730,500 1,911 
Sabine Pass LNG Terminal Southeast 0.26% 18,667,328 48,827 
Cove Point LNG Facility Southeast 0.26% 4,697,068 12,286 
Freeport Southwest 0.40% 8,486,405 34,500 
Corpus Christi Liquefaction Southwest 0.40% 7,969,529 32,399 
Cameron LNG LLC Southeast 0.26% 7,767,049 20,316 
 
• Emissions from electricity consumption for Freeport LNG terminal’s electric drive turbines 
(the only operating U.S. export facility using this configuration) are incorporated using the 
Electric Reliability Council of Texas (ERCOT) electricity generation mix for 2020. The 
amount of electricity used by the Freeport LNG terminal is available in the company’s 
 
18 Subpart C of the GHGRP is for General Stationary Fuel Combustion Sources. The EPA website 
summarizes these as “Stationary fuel combustion sources are devices that combust any solid, liquid, or 
gaseous fuel generally to produce electricity, steam, useful heat, or energy for industrial, commercial, or 
institutional use or reduce the volume of waste by removing combustible matter.” For this work, the 
subpart C data from only the LNG facilities are considered. 
19 Khutal, H., et al. Life Cycle Analysis of Natural Gas Extraction and Power Generation: U.S. 2020 
Emissions Profile. National Energy Technology Laboratory, Pittsburgh, December 2024. 
https://www.netl.doe.gov/energy-analysis/details?id=546d4009-c43b-43f5-bcc9-64d5e63fc8d5 
20 U.S. EPA Greenhouse Gas Reporting Program (2021). Subpart W Reporting Year 2020. Available at 
www.epa.gov/ghgreporting. Date accessed: October 15, 2024.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-14 
sustainability report: 3,469,942 MWh21. The ERCOT greenhouse gas emissions intensity 
(kg CO 2e/MWh, AR6, 100-yr) is calculated using a custom generation mix in the NETL 
Grid Mix Explorer.22 The generation mix was derived from the ERCOT Fuel Mix Report 23 
as shown in Table 7. The end result is an additional 0.204 kg CO 2/kg LNG (AR6, 100-yr) 
exported for the Freeport facility. 
 
Table 7. 2020 ERCOT generation mix24 
Fuel type Percent Mix CO₂ (kg/MWh) CH₄ (kg/MWh) N₂O (kg/MWh) GWP, AR6, 100-yr (kg CO2e/MWh) 
Biomass 0.09% 1.11 2.7E-04 3.4E-05 1.1 
Coal 18.00% 203.57 9.3E-02 3.3E-03 207.2 
Natural gas 45.66% 259.07 7.8E-01 9.9E-04 282.5 
Hydro 0.17% 0.02 8.1E-05 1.0E-09 0.0 
Nuclear 10.89% 1.48 1.7E-02 9.0E-05 2.0 
Solar 2.30% 0.47 1.1E-03 1.6E-06 0.5 
Wind 22.88% 6.23 1.4E-02 2.3E-05 6.7 
    Total 500.1 
 
• The reported facility-level emissions are separated by Subpart W25 (Table 8 and Table 9) 
and Subpart C (Table 10) to allow the incorporation of the NETL combustion factors. The 
fuel quantities in Table 10 are multiplied by the NETL combustion factors listed in  
• Table 11 to calculate the emissions for each combustion source. Combustion emissions 
for GHGRP are calculated using fuel use by the facility (e.g., gallons of diesel) and 
emissions factors (e.g., kg CO 2 per gallon diesel combusted) specified for reporting to 
GHGRP. NETL has developed its own emissions factors from open data sources that are 
used in its models. In order to make sure the liquefaction emissions used in this study 
would match future implementations in NETL products, NETL combustion factors are used 
to calculate the combustion emissions. Additionally, life cycle emissions for diesel 
production are included for completeness. 
• Flaring CO 2 emissions are calculated from the amounts of natural gas sent to flaring 
reported in Table 8 by assuming a 98% mass conversion efficiency from CH4 to CO2 with 
the remaining 2% emitted as CH 4. If only these combustion -specific changes were 
 
21 Freeport LNG Sustainability and Community Investment Report 2020. 
https://freeportlng.com/files/docs/2020-Freeport-LNG-SCIR.PDF  
22 NETL Grid Mix Explorer v4.2. https://netl.doe.gov/energy-analysis/details?id=f0f94954-3627-4e9b-
a5c0-c29cfe419d1c.  
23 ERCOT Fuel Mix Report: 2007-2020. 
https://www.ercot.com/files/docs/2021/03/10/FuelMixReport_PreviousYears.zip  
24 U.S. EPA Greenhouse Gas Reporting Program (2021). Subpart W Reporting Year 2020. Available at 
www.epa.gov/ghgreporting. Date accessed: October 15, 2024. 
25 Subpart W of the GHGRP is for emissions from petroleum and natural gas systems, and more 
specifically non-combustion emissions. The EPA website summarizes these as “Owners or operators of 
facilities that contain petroleum and natural gas systems and emit 25,000 metric tons or more of GHGs 
per year (expressed as carbon dioxide equivalents) report GHG data to EPA. Owners or operators collect 
GHG data; calculate GHG emissions; and follow the specified procedures for quality assurance, missing 
data, recordkeeping, and reporting. Subpart W consists of emission sources in ten segments of the 
petroleum and natural gas industry.”

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-15 
implemented, the 0.215 kg CO2e/kg LNG value in Table 5 would become 0.219 kg CO2e/kg 
LNG, a 2 percent increase. 
Table 8. 2020 LNG facility GHGRP Subpart W LNG import and export equipment emission 
sources26 
U.S. LNG 
Facility Name 
NG Sent to 
Flare 
(MMscf)  
Feed Gas 
Sent to 
Flare - CH4 
Mass 
Fraction 
Feed Gas 
Sent to 
Flare - CO2 
Mass 
Fraction 
Blowdown 
Vent Stack 
(tons CO2) 
Blowdown 
Vent Stack 
(tons CH4) 
Blowdown 
Vent Stack 
(tons N2O) 
SLNG Elba 
Island Terminal 770 0.3392 0.0234 0.1 5.1 0 
Sabine Pass 
LNG Terminal 3,741 0.8045 0.0771 0.0 258.6 0 
Cove Point LNG 
Facility 1,454 0.4538 0.2749 0.6 22.4 0 
Freeport 854 0.9750 0.0100 0.0 0.0 0 
Corpus Christi 
Liquefaction 4,338 0.8549 0.0039 0.0 0.0 0 
Cameron LNG 
LLC 22,041 0.8254 0.0079 0.0 0.0 0 
 
Table 9. 2020 LNG facility GHGRP Subpart W LNG import and export equipment emission 
sources (cont’d)26 
U.S. LNG Facility 
Name 
Equipment 
Leaks 
(tons CO2) 
Equipment 
Leaks 
(tons CH4) 
Equipment 
Leaks 
(tons N2O) 
Reciprocating 
Compressors 
(tons CO2) 
Reciprocating 
Compressors 
(tons CH4) 
Reciprocating 
Compressors 
(tons N2O) 
SLNG Elba Island 
Terminal 0 48.37 0 0.7 23.97 0 
Sabine Pass LNG 
Terminal 0 224.73 0 0 0 0 
Cove Point LNG 
Facility 0 19.88 0 2.7 93.09 0 
Freeport 0 9.39 0 0 0 0 
Corpus Christi 
Liquefaction 0 58.38 0 0 0 0 
Cameron LNG LLC 1.8 68.97 0 0 0 0 
 
 
26 U.S. EPA Greenhouse Gas Reporting Program (2021). Subpart W Reporting Year 2020. Available at 
www.epa.gov/ghgreporting. Date accessed: October 15, 2024.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-16 
Table 10. 2020 LNG facility GHGRP Subpart C general stationary fuel combustion26 
U.S. LNG 
Facility Name 
Simple 
Cycle 
Combustion 
Turbines - 
NG 
Combusted 
(MMscf/yr) 
Other 
Combustion 
Sources - 
NG 
Combusted 
(MMscf/yr) 
Thermal 
Oxidizer 
Direct Fired 
(MMscf/yr) 
Combined 
Cycle 
Combustion 
Turbines - 
NG 
Combusted 
(MMscf/yr) 
Other Boiler 
- NG 
Combusted 
(MMscf/yr) 
Process 
Heater - NG 
Combusted 
(MMscf/yr) 
Process 
Heater - 
Propane 
Combusted 
(MMscf/yr) 
Recipro-
cating 
Internal 
Combustion 
Engine - 
Distillate 
Fuel Oil 
No. 2 
(gal/yr) 
SLNG Elba Island 
Terminal  0 1,050 0 0 0 0 0 0 
Sabine Pass LNG 
Terminal 74,721 0 1,587 0 0 0 0 0 
Cove Point LNG 
Facility 2,897 0 0 14,492 2,516 290 0.358 0 
Freeport 0 0 0 0 0 0 0 0 
Corpus Christi 
Liquefaction 25,805 798 0 2,084 0 0 0 25,856 
Cameron LNG 
LLC 0 33,009 641 639 0 0 0 0 
 
Table 11. NETL stationary combustion emission factors and distillate fuel life cycle emissions 
Fuel CO2 CH4 N2O Units 
Distillate Fuel Oil No. 21 3.20 1.28E-04 2.51E-05 kg/kg diesel 
Distillate Fuel Oil No. 2 (Upstream)2 0.638 4.82E-03 2.82E-05 kg/kg diesel production 
Natural Gas Reciprocating Compressor3 2.83 3.31E-02 0 kg/kg natural gas 
Natural Gas Centrifugal Compressor3 2.66 2.08E-04 7.24E-05 kg/kg natural gas 
Natural Gas Combustion2 2.83 5.42E-05 0 kg/kg natural gas 
Propane4 0.155 0 0 kg/scf 
Notes: 
1 NETL (2014). NETL Life Cycle Inventory Data – Unit Process: Combustion of Diesel. U.S. Department of Energy, 
National Energy Technology Laboratory. Last Updated: January 2015 (version 02). www.netl.doe.gov/LCA 
2 NETL (2008). Development of Baseline Data and Analysis of Life Cycle Greenhouse Gas Emissions of Petroleum-
Based Fuels.  
3 NETL (2015). NETL Life Cycle Inventory Data – Unit Process: Combustion of Natural Gas. U.S. Department of 
Energy, National Energy Technology Laboratory. Last Updated: January 2015 (version 01). www.netl.doe.gov/LCA  
4 Propane emission factor is from Table C-1 to Subpart C – Default CO2 Emission Factors and High Heat Values for 
Various Types of Fuel. https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-98/subpart-C/appendix-
Table%20C-1%20to%20Subpart%20C%20of%20Part%2098  
Table 12 summarizes the total for each species of GHG emissions (i.e., “speciated emissions”) 
as calculated after the above adjustments and re -calculates the GHG intensity for each LNG 
facility (following the same columns/steps as used to create Table 5). These results show that 
accounting for the additional  emissions increases the production -weighted average emissions 
intensity from 0.215 (Table 5) to 0.258 kg CO2e/kg LNG. Additional unit conversion present results 
on a g CO2e/MJ basis, including a conversion to LHV to align with GCAM.27 
 
27 The higher heating and lower heating values for these conversions are 54.3 MJ/kg LNG and 49.0 
MJ/kg LNG, respectively, and are multiplied by the mass-based Facility GHG intensity (in kg CO2e/kg 
LNG).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-17 
Table 12. NETL liquefaction estimate - speciated emissions 
U.S. LNG 
Facility Name 
CO₂ 
(Mg CO₂e) 
CH₄ 
(Mg CO₂e) 
N₂O 
(Mg CO₂e) 
GWP, AR6, 
100-yr 
(Mg CO₂e) 
LNG Mass 
Exported 
(Mg) 
Facility GHG 
Intensity 
(kg CO₂e/kg 
LNG) 
Facility GHG 
Intensity 
(g CO₂e/MJ 
LNG HHV) 
Facility GHG 
Intensity 
(g CO₂e/MJ 
LNG LHV) 
SLNG Elba 
Island Terminal 76,214 5,477 0 81,691 730,500 0.112 2.06 2.28 
Sabine Pass 
LNG Terminal 4,304,382 59,889 29,753 4,394,024 18,667,328 0.235 4.33 4.80 
Cove Point LNG 
Facility 1,145,880 14,215 6,924 1,167,019 4,697,068 0.248 4.57 5.07 
Freeport 1,717,497 103,843 4,169 1,825,509 8,486,405 0.215 3.96 4.39 
Corpus Christi 
Liquefaction 1,770,920 49,755 11,105 1,831,780 7,969,529 0.230 4.23 4.69 
Cameron LNG 
LLC 2,960,706 221,601 254 3,182,562 7,767,049 0.410 7.54 8.36 
 
    Production Weighted 
Average 
0.258 4.76 5.27 
Below, the updated 2024 NETL liquefaction stage (2020 data year) GHG intensity estimates are 
compared to: 
• U.S. EPA Greenhouse Gas Reporting Program (GHGRP) data28,29 
• A 2021 paper that included liquefaction emissions as part of supplier-specific LCA for LNG 
supply chains (Roman-White et al., 2021)30  
• An August 2024 pre-print of a paper reporting greenhouse gas emissions estimates of two 
liquefaction facilities based on measured emissions (Zhu et al., 2024)31  
 
28 U.S. EPA Greenhouse Gas Reporting Program (2023). Summary GHG Data 2020. https://www.epa. 
gov/system/files/other-files/2023-12/ghgp_data_2020.xlsx. Date accessed: October 15, 2024. 
29 U.S. EPA Greenhouse Gas Reporting Program (2023). Summary GHG Data 2022. http://www.epa.gov/ 
ghgreporting. Date accessed: October 15, 2024. Calculations are based on emissions and exports from 
seven facilities for 2022. 
30 Roman-White, S. A., Littlefield, J. A., Fleury, K. G., Allen, D. T., Balcombe, P., Konschnik, K. E., Ewing, 
J., Ross, G. B., & George, F. (2021). LNG Supply Chains: A Supplier-Specific Life-Cycle Assessment for 
Improved Emission Accounting. ACS Sustainable Chemistry & Engineering, 9(32), 10857–10867. 
https://doi.org/10.1021/acssuschemeng.1c03307  
31 Zhu Y, Ross G, Khaliukova O, Roman-White S, George F, Hammerling D, et al. Multi-scale 
Measurements of Greenhouse Gas Emissions at U.S. Natural Gas Liquefaction Terminals. ChemRxiv. 
2024; doi:10.26434/chemrxiv-2024-h4flq (This content is a preprint and has not been peer-reviewed).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-18 
Table 13. Comparison of NETL liquefaction stage GHG emissions intensity with other literature 
Source 
Liquefaction Stage Emissions Intensity 
CO2 
(kg CO2/kg 
LNG) 
CH4 
(kg CH4/kg 
LNG) 
N2O 
(kg N2O/kg 
LNG) 
CO2e, AR6, 
100-yr GWP 
(kg CO2e/kg 
LNG) 
CO2e, AR6, 
100-yr GWP 
(g CO2e/MJ 
LHV) 
NETL 2024 – National 
Average  0.248 3.16E-04 3.96E-06 0.258 5.27 
GHGRP Reporting Year 
2020 0.212 9.24E-05 3.97E-07 0.215 4.39 
GHGRP Reporting Year 
2022 0.202 4.79E-05 3.82E-07 0.204 4.16 
Roman-White 
et al., 2021 
Sabine 
Pass, 2018 
data 
- 5.00E-05 - 0.26 5.31 
Zhu et al., 
2024  
Site 1 0.220 1.82E-04 - 0.225 4.59 
Site 2 0.243 2.22E-04 - 0.250 (0.211 – 0.281) 5.10 
Notes:  
• The 2024 NETL estimate uses 2020 GHGRP data as the reference data source and incorporates acid gas removal 
emissions for each facility and electricity consumption emissions for the Freeport LNG facility, while ensuring 
alignment with combustion emission factors modeled in the NETL natural gas baseline LCA to generate a 
representative national average liquefaction stage GHG intensity profile. 
• Upon accounting for emissions from electricity consumption for the Freeport LNG terminal (represents 18% of NG 
exports in 2020), the GHG intensity of the facility rises from 0.011 kg CO 2e/kg LNG to 0.22 kg CO 2e/kg LNG (AR6, 
100-year). Emissions from electricity consumption represent ~95% of the GHG emissions profile of the Freeport LNG 
terminal based on available data. 
 
The higher GHG emissions intensity for the 2024 NETL liquefaction result compared to the 2020 
and 2022 (20% and 26% higher, respectively) reporting year GHGRP estimates is driven by the 
additional AGRU CO2 emissions, carbon intensity of the ERCOT grid to support on site electricity 
use and ensuring consistency with NETL modeling emissions factors. On a n AR6, 100-yr basis, 
the 2024 NETL attributional GHG emissions intensity estimate for liquefaction generally aligns 
with estimates from other sources as noted below and provided in Table 13. 
 
• Roman-White et al., 2021: 2024 NETL liquefaction stage emissions intensity is equivalent 
(<1% difference) to the liquefaction stage estimate reported in the Roman -White et al. 
study. 
 
• Zhu et al., 2024: 2024 NETL estimate is around 3-15% higher than estimates reported by 
Zhu et al. However, NETL estimates are within the reported uncertainty range for site 2 
as reported by Zhu et al. Also, the 2024 NETL estimate represents a national average 
liquefaction stage GHG emissions intensity profile for the year 2020, whereas the Zhu et 
al. study focuses on two specific liquefaction terminals – Sabine Pass, LA and Corpus 
Christi, TX. 
Step 4: Align GCAM Natural Gas Production and Pipeline Transport to U.S. 
National Average GHG Performance 
NETL compared the GCAM model results to the year 2020 national average for upstream natural 
gas production through delivery to a large end user as reported in the NETL Baseline Study ( as 
described in Step 2). This was done to align the representation of U.S. natural gas production and

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-19 
pipeline transport GHG emissions representation to the study start period (Year 2020) based on 
U.S. industry average data. 
Specifically, NETL assessed and aligned the emissions estimates per unit of gas produced and 
delivered to large end users (e.g., LNG export facilities) in the U.S. from  GCAM to the NETL life 
cycle GHG intensity for U.S. average natural gas production and delivery to large end users (from 
Step 2), using a ratio of the NETL and GCAM results. Since GCAM uses lower heating value 
(LHV) to express energy content, the NETL model output figures were adjusted from HHV to LHV 
basis, resulting in a value of 8.63 g CO 2e/MJ ( AR6, 100 -yr, LHV basis). This comparison 
aggregated data only from three GCAM sectors in the USA region: natural gas, gas pipelines, and 
other industrial energy use32. 
The intensity values of upstream natural gas in GCAM and the 2024 NETL study were found to 
differ by 1.17% (with the NETL intensity of 8.63 g CO2e/MJ being slightly higher than the GCAM 
value found to be 8.53 g CO2e/MJ on an AR6, 100-yr LHV basis). See Appendix C-2 for additional 
details, including the alternate development of the adjustment factor on an AR6, 20-yr basis.  
Step 5: Calculate GCAM-NETL-aligned Global GHG Emissions Results 
Using the 1.17% adjustment factor calculated in Step 4, results for the three GCAM sectors listed 
in Step 4 were adjusted (increased by 1.17%) to align with NETL GHG intensity values. Non-U.S. 
region natural gas production and delivery GHG emissions intensity values for these same sectors 
were also adjusted up by 1.17% to align with NETL life cycle GHG intensity values. Note that the 
comparison and adjustment was done only to maintain the total CO 2e intensity value and not on 
a speciated emission basis. This adjustment was applied to all model years and regions for these 
three sectors reported by GCAM (i.e., every fifth year from 2020 -2050). The Defined Policies: 
Existing/FID Exports scenario is shown in Table 14 as an example of the overall unadjusted and 
adjusted GCAM GHG emissions results (across all sectors) and for the three aligned sectors. The 
majority of the increase in adjusted emissions are in the GCAM natural gas sector. Overall, the 
adjustments to align to NETL 2020 national average performance data for GHG intensity ( AR6, 
100-yr basis) added about 20 Tg CO2e emissions per model year, a net increase in overall global 
emissions of less than 0.05%. 
Table 14. GCAM unadjusted and NETL aligned sector emissions for Defined Policies: 
Existing/FID Scenario (AR6, 100-yr basis) 
Year 
GHG Emissions (Tg CO2e) 
GCAM Unadjusted GCAM-NETL Aligned 
Natural 
Gas 
Gas 
Pipeline 
Other 
Industrial 
Energy 
Use 
All Other 
Sectors 
Total 
Across 
All 
GCAM 
Sectors 
Natural 
Gas 
Gas 
Pipeline 
Other 
Industrial 
Energy 
Use 
All Other 
Sectors 
Total 
Across All 
GCAM 
Sectors 
2020 957 185 5,146 47,463 53,751 968 188 5,152 47,462 53,770 
2025 827 171 5,855 44,145 50,998 836 173 5,862 44,146 51,017 
2030 868 182 6,670 41,417 49,137 878 184 6,677 41,417 49,156 
2035 888 184 7,310 41,792 50,174 899 187 7,318 41,790 50,194 
2040 894 189 7,856 40,428 49,367 904 191 7,864 40,429 49,388 
 
32 The adjustment for the other industrial energy use sector was focused only on natural gas relevant 
technologies, which comprises a small part of the overall sector. As such the resulting adjustment factor 
for that sector was about 0.1%. Appendix C-2 shows details of the adjustment for that sector.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-20 
2045 955 193 8,445 39,651 49,244 966 195 8,454 39,652 49,267 
2050 1,013 195 8,936 38,471 48,615 1,025 197 8,945 38,472 48,639 
Note: As detailed above, only a subset of emissions in the other industrial energy use were adjusted. 
Table 15 shows how speciated emissions of CO 2 and CH 4 changed with the adjustments 
described above for the Defined Policies: Existing/FID Exports scenario. This shows that of the 
approximately 20 Tg CO2e adjusted per year, it is generally evenly split between CO2 and CH4 on 
a CO2e basis. The table also provides perspective on the contribution of the speciated emissions 
to the total global emissions profile. 
Table 15. Model-year GCAM-NETL-aligned GHG emissions for DP: ExFID Scenario 
Year 
GHG Emissions (Tg CO2e) 
GCAM Unadjusted GCAM-NETL Aligned 
CO2 
Energy 
CO2 
LUCa 
CH4 
Energy 
Other 
GHGs Total CO2 Energy CO2 LUC CH4 Energy Other GHGs Total 
2020 38,399 398  6,666 8,288  53,751 38,407 398  6,677 8,288  53,770 
2025 36,091 754  5,588 8,566  50,998 36,099 754  5,598 8,566  51,017 
2030 36,605  -2,679 5,785 9,425  49,137 36,615  -2,679 5,795 9,425 49,156 
2035 35,737  -1,233 5,763 9,906  50,174 35,748 -1,233 5,773 9,906  50,194 
2040 34,906 1,328 5,584 10,204  49,367 34,917 -1,328 5,595 10,204  49,388 
2045 34,047  -992 5,617 10,573  49,244 34,058  -992 5,628 10,573  49,267 
2050 32,900 -874 5,629 10,961  48,615 32,912 -874 5,641 10,961  48,639 
Note: In the global analysis, CO2 emissions from energy are subject to uncertainties in regional emission intensities of 
natural gas and other fossil fuels. The negative result for land use change CO2 emissions demonstrates that more CO2 
is removed from the atmosphere than released from changes in land use systems in the modeled timeframe. In the 
global analysis, emissions from land-use changes are driven in part by changes in energy production, including those 
driven by changes in demand (e.g., global demand or LNG). These emissions are also subject to greater uncertainties 
largely due to uncertainties in data. A detailed exploration of these uncertainties is beyond the scope of this study. 
Step 6: Interpolate GCAM -aligned Results from 5 -year Time Steps to Annual 
Results 
The results from Step 5 of every fifth-year model output (2020-2050) were interpolated to all 
intervening years via simple linear interpolation methods (e.g., the difference in five-year values 
divided by five and added as 1/5 th shares to subsequent years). This interpolation was done for 
both GHG emissions as well as for U.S. LNG exports, with an example for Defined Policies: 
Existing/FID Exports shown in Table 16. These annual results are also summed as cumulative 
values over the period 2020-2050. Interpolated U.S. LNG export values are provided in Table 16. 
Table 16. Modeled, interpolated, and cumulative GCAM-NETL-aligned GHG emissions for DP: 
ExFID Scenario 
Year CO2 Energy CO2 LUC CH4 Energy  Other GHGs Total U.S. LNG Exports 
Units (Tg CO2e/year) (AR6, 100-yr) EJ Bcf/d 
2020 38,407 398 6,677 8,288 53,770 2.44 6.8 
2021 37,946 469 6,461 8,344 53,220 3.22 8.9 
2022 37,484 540 6,245 8,399 52,669 4.00 11.1 
2023 37,023 611 6,029 8,455 52,118 4.78 13.3 
2024 36,561 683 5,814 8,511 51,567 5.55 15.4

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-21 
Year CO2 Energy CO2 LUC CH4 Energy  Other GHGs Total U.S. LNG Exports 
Units (Tg CO2e/year) (AR6, 100-yr) EJ Bcf/d 
2025 36,099 754 5,598 8,566 51,017 6.33 17.6 
2026 36,202 67 5,637 8,738 50,645 6.45 17.9 
2027 36,305 -619 5,677 8,910 50,273 6.58 18.3 
2028 36,409 -1,306 5,716 9,082 49,901 6.70 18.6 
2029 36,512 -1,992 5,755 9,254 49,529 6.83 19.0 
2030 36,615 -2,679 5,795 9,425 49,157 6.95 19.3 
2031 36,441 -2,389 5,791 9,522 49,364 7.27 20.2 
2032 36,268 -2,100 5,786 9,618 49,572 7.59 21.1 
2033 36,095 -1,811 5,782 9,714 49,779 7.90 21.9 
2034 35,921 -1,522 5,777 9,810 49,987 8.22 22.8 
2035 35,748 -1,233 5,773 9,906 50,194 8.54 23.7 
2036 35,582 -1,252 5,738 9,966 50,033 8.54 23.7 
2037 35,416 -1,271 5,702 10,025 49,872 8.54 23.7 
2038 35,249 -1,290 5,666 10,085 49,711 8.54 23.7 
2039 35,083 -1,309 5,631 10,144 49,550 8.54 23.7 
2040 34,917 -1,328 5,595 10,204 49,388 8.54 23.7 
2041 34,745 -1,261 5,602 10,278 49,364 8.54 23.7 
2042 34,574 -1,194 5,608 10,352 49,340 8.54 23.7 
2043 34,402 -1,127 5,615 10,425 49,315 8.54 23.7 
2044 34,230 -1,059 5,621 10,499 49,291 8.54 23.7 
2045 34,058 -992 5,628 10,573 49,267 8.54 23.7 
2046 33,829 -969 5,631 10,651 49,141 8.54 23.7 
2047 33,600 -945 5,633 10,728 49,016 8.54 23.7 
2048 33,370 -922 5,636 10,806 48,890 8.54 23.7 
2049 33,141 -898 5,638 10,883 48,765 8.54 23.7 
2050 32,912 -874 5,641 10,961 48,639 8.54 23.7 
Total 1,101,142 -28,818 178,896 301,120 1,552,340 227 - 
Using the interpolated data for Defined Policies: Model Resolved and Defined Policies: 
Existing/FID Exports , Speciated emissions for all years 2020 -2050, as well as total GHG 
emissions and U.S. LNG export volumes for all modeled scenarios are provided as data tables in 
Appendix C-4. 
 shows that while U.S. LNG export volumes (expressed as the dotted orange and blue lines) begin 
to appreciably change around 2030, and more than double in the modeled scenario by 2050, total 
global GHG emissions (shown as the solid orange and blue lines) do not begin to differ until 2040, 
and then by only 0.1 percent. The time effect of when the emissions differ is important and will be 
revisited in the discussion of subsequent steps. 
Speciated emissions for all years 2020 -2050, as well as total GHG emissions and U.S. LNG 
export volumes for all modeled scenarios are provided as data tables in Appendix C-4.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-22 
 
Figure 1. GHG emissions and U.S. LNG export trends for the Defined Policies: Existing/FID and 
Defined Policies: Model Resolved Scenarios 
Step 7: Calculate GCAM -NETL-aligned Consequential GHG Intensity and SC -
GHG per Unit of U.S. LNG Exports 
The emissions results provided by GCAM are total global emissions, including upstream and 
downstream emissions (accounting for direct emissions and direct and indirect market effects, 
and including use/combustion of fuels). The consequential GHG intensity is the effect (inclusive 
of both direct and indirect emissions) of U.S. LNG on global emissions per unit of U.S. LNG 
exported. To quantify the consequential GHG intensity of U.S. LNG , the GCAM -NETL-aligned 
results were used to estimate the change in global GHG emissions per unit of U.S. LNG exported 
between scenarios within a global climate policy. The consequential GHG intensity of increased 
U.S. LNG Exports is defined as shown in Equation 1: 
  
 
This intensity value in all scenarios was estimated in comparison to the Existing/FID scenario 
baseline within a policy scenario (e.g., Defined Policies: Model Resolved would be compared to 
the Defined Policies: Existing/FID  baseline, and this specific pairwise comparison will be used 
throughout this section of the report as an example). The consequential GHG intensity of 
increased U.S. LNG exports under this scenario can be calculated for every year (2020 –2050), 
and with cumulative values of GHG emissions and U.S. LNG exports over the time horizon of the 
model.  
𝐶𝑜𝑛𝑠𝑒𝑞𝑢𝑒𝑛𝑡𝑖𝑎𝑙 𝐺𝐻𝐺 𝐼𝑛𝑡𝑒𝑛𝑠𝑖𝑡𝑦
 𝑜𝑓 𝑈. 𝑆. 𝐸𝑥𝑝𝑜𝑟𝑡𝑠 𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜 𝑛
= 𝐺𝑙𝑜𝑏𝑎𝑙 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜 𝑛− 𝐺𝑙𝑜𝑏𝑎𝑙 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜 𝑏𝑎𝑠𝑒
𝑈.𝑆. 𝐿𝑁𝐺 𝐸𝑥𝑝𝑜𝑟𝑡𝑠𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜 𝑛−𝑈.𝑆. 𝐿𝑁𝐺 𝐸𝑥𝑝𝑜𝑟𝑡𝑠𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜 𝑏𝑎𝑠𝑒
  (1)

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-23 
For Defined Policies: Model Resolved  versus Defined Policies: Existing/FID Exports 33 the 
consequential GHG intensity is the total difference in annually estimated global GHG emissions 
over the 2020-2050 period (711 Tg CO 2e) divided by the total difference in exported U.S. LNG 
over the same period (113 EJ)34, or 6.3 g CO2e/MJ. The consequential GHG intensity of U.S. LNG 
exports is estimated for all scenarios (versus their ExFID baseline). Cumulative consequential 
GHG intensity results for all scenarios are provided in Table 22. Annual consequential GHG 
intensity results for each scenario are provided in Appendix C-4. 
Note that the study assumes that the difference in emissions between scenarios within a global 
climate policy is the total difference in life cycle emissions (and that the reason for the difference 
in emissions is the difference in U.S. LNG exported). By normalizing to the difference in U.S. LNG 
exports, the study assumes that the consequential GHG intensity result is showing the difference 
in total global emissions associated with an additional unit of U.S. LNG exported, inclusive of 
direct emissions and direct and indirect market effects. This leads to results on a g CO 2e/MJ of 
LNG exported basis (amount of GHGs emitted per unit of energy contained in LNG).35 
The speciated GHG emissions inputs to the consequential GHG intensity can also be used with 
the 2023 SC -GHG methodology to monetize the impacts of the changes in GHG emissions 
associated with increased U.S. LNG exports. The SC -GHG, as described by the Inte ragency 
Working Group (IWG) on SC-GHG, is “the monetary value of the net harm to society associated 
with adding a small amount of greenhouse gases to the atmosphere in a given year.”36 Estimates 
of the SC -GHG “allow analysts to incorporate the net social benefits of reducing emissions of 
greenhouse gases, or the net social costs of increasing such emissions, in benefit-cost analysis, 
and when appropriate, in decision making and other contexts.”37 In short, the SC-GHG monetizes 
the net harm to society caused by the release of an additional ton of GHGs into the atmosphere 
in a given year.  
The 2023 SC-GHG method uses a trio of discount rates (1.5%, 2.0% and 2.5%) to provide values 
of the SC-GHG for a particular base year (assumed in this study as 2024) and dollar year. The 
base year (which can also be considered the present value year) was chosen to be 2024 to align 
with the time of the study, consistent with the suggested choice aligning with a regulatory impact 
assessment time. The study used 2020 as the dollar year, consistent with the default year of 
damages provided in the framework. The  monetized SC-GHG values  for each of the three 
greenhouse gases for each of the three discount rates for each year of the study period  (in year 
2020 dollars) used by the method are summarized in Appendix C-3.  
 
33 Recall that from Table 1, the Defined Policies: Existing/FID Exports scenario in GCAM represents 
expected future trajectories of U.S. LNG exports and GHG emissions where U.S. LNG production is 
constrained to volumes equal to 90% of the capacity up to or past the point of final investment decision, 
while the Defined Policies: Model Resolved scenario calculates what economically-driven levels of U.S. 
LNG might be supplied into the global market without that constraint. Yet, this scenario comparison is just 
one of the many scenarios modeled and should not be considered the primary result.  
34 Results for each year 2020-2050 and IPCC AR6 20-year time horizons are shown in Appendix C-4.  
35 The underlying GCAM data is in Tg of GHG Emissions and EJ of LNG used, a Tg/EJ is equivalent to 
g/MJ. 
36 Interagency Working Group on Social Cost of Greenhouse Gases, U.S. Government. (February 2021). 
“Technical Support Document: Social Cost of Carbon, Methane, and Nitrous Oxide. Interim Estimates 
under Executive Order 13990”. https://www.whitehouse.gov/wp-content/uploads/2021/02/ 
TechnicalSupportDocument_SocialCostofCarbonMethaneNitrousOxide.pdf  
37 U.S. EPA (November 2023). Report on the Social Cost of Greenhouse Gases: Estimates Incorporating 
Recent Scientific Advances. https://www.epa.gov/system/files/documents/2023-12/epa_scghg_ 
2023_report_final.pdf

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-24 
For Defined Policies: Model Resolved versus Defined Policies: Existing/FID Exports , the 
cumulative difference in emissions from 2020 -2050 is estimated to have a cumulative SC -GHG 
impact of $70 billion using a discount rate of 2.5%, $130 billion using a discount rate of 2.0%, and 
$220 billion using a discount rate of 1.5% (all 2020$). SC -GHG estimates for all scenarios are 
provided in Table 23. 
Normalizing SC -GHG results per MJ of change in natural gas exported leads to estimated 
intensities ranging from $0.0007/MJ (2.5% discount rate) to $0.002/MJ (1.5% discount rate) . In 
other words, for this scenario, the social costs of the additional GHG emissions associated with 
increased U.S. LNG exports range from 0.07 cents/MJ (2.5% discount rate) to 0.2 cents/MJ (1.5% 
discount rate). SC-GHG estimates per unit of change in energy exported for all scenarios are 
provided in  
Table 24. SC-GHG estimates per unit of change in energy exported for all scenarios are provided 
in Appendix C-2. 
Step 8: Subtract National Average Upstream Natural Gas and Liquefaction Plant 
GHG Performance to Determine Project Non-Direct Emissions Intensity 
The overall consequential GHG intensity values include all emissions from direct emissions as 
well as direct and indirect market effects. To facilitate an approach to evaluating environmental 
GHG performance of individual LNG project s that accounts for consequential market effects, 
these overall consequential values need to be broken down into component parts. Overall, the 
consequential GHG intensity of U.S. exports can be split into two primary categories, project direct 
emissions and project non-direct emissions, expressed in Equation 2. 
Consequential GHG Intensity of US Exports = Project Direct Emissions + Project Non -Direct 
Emissions (2) 
where: 
Project direct emissions include liquefaction emissions and all upstream emissions of 
producing and processing the natural gas before liquefaction.  
Project non-direct emissions include emissions not included in the definition of project direct 
emissions. This includes direct emissions from ocean shipping, regasification, importing 
country transport of the gas, and use (unspecified) of the exported gas, plus the direct and 
indirect market effects.  
The project non-direct emissions factor is estimated by taking the consequential GHG intensity 
and subtracting the estimated project direct emissions intensity, as shown in Equation 3 (just a 
re-arranged version of Equation 2).  
Project Non -Direct Emissions = Consequential GHG Intensity of US Exports - Project Direct 
Emissions. (3) 
For the purposes of this study, project direct emissions values were assumed to be equal to the 
sum of Year 2020 U.S. average GHG emission intensity estimates for upstream natural gas 
production and delivery and liquefaction operations as described in Steps 2 and 3 (i.e., 9.2 and 
5.3 g CO2e/MJ, respectively, for upstream natural gas and liquefaction). The sum of project direct 
emissions is thus 14.5 g CO2e/MJ.  
Applying Equation 3 and the project direct emissions  factor above, the project non -direct 
emissions factor for Defined Policies: Model Resolved would be +6.3 – (9.2 + 5.3), or a net of -
8.2 g CO2e/MJ. Since the project direct emissions are substantially higher than the consequential 
GHG intensity, it follows that the project non-direct emissions would be negative given Equations 
2 and 3.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-25 
The project non-direct emissions value, which includes LNG usages across all technologies and 
options in global markets, represents the overall expected net global effect from ocean transport 
through use of the LNG plus direct and indirect market effects. The project non-direct emissions 
value is an interim value that enables comparison to GHG emissions from the U.S. default natural 
gas upstream and liquefaction values used in this study and should not be used as the basis for 
interpreting study findings. Table 25 summarizes the resulting project non-direct emissions values 
for all scenarios. 
Step 9: Add Project Direct Emissions to Project Non -Direct Emissions  to 
Determine Individual Project GHG Emissions Intensity Inclusive of 
Consequential Market Effects 
To understand how an individual U.S. export project may differ from the U.S. average liquefaction 
facility values modeled in the study, the various speciated emissions values, consequential GHG 
intensity, and project non-direct emissions can be compared.  
The default values used for individual project  analyses would be the average U.S. values 
described in Steps 2 and 3 (9.2 g CO2e/MJ for upstream U.S. natural gas and 5.3 g CO2e/MJ for 
liquefaction).  
Equations 2 and 3, defined above, are repeated here and used to help organize the consequential 
GHG intensities of the default facility. 
Consequential GHG Intensity of US Exports = Project Direct Emissions + Project Non -
Direct Emissions (2) 
Project Non -Direct Emissions = Consequential GHG Intensity of US Exports - Project 
Direct Emissions (3) 
For a default project, using the example of Defined Policies: Model Resolved compared against 
Defined Policies: Existing/FID Exports , the consequential GHG intensity can be organized into 
speciated components as shown in Table 17, with a total default U.S. average consequential GHG 
intensity of +6.3 g CO 2e/MJ. The values in Table 17, and its project non-direct emissions and 
consequential GHG intensity rows, could be used to subsequently compare individual project 
data.38 
Table 17. Default values for natural gas upstream and liquefaction facility operations (exam ple 
DP:MR vs. DP:ExFID) 
Stage Average Default GHG Intensity, (g CO2e/MJ) CO2 CH4 Total 
NG Upstream 5.6 3.6 9.2 
Liquefaction 5.1 0.2 5.3 
Project Non-Direct Emissions (Estimated) -4.8 -3.4 -8.2 
Consequential Global GHG Emissions Intensity 5.8 0.5 +6.3 
Step 10: Demonstrate Estimation of Consequential GHG Intensity and SC -GHG 
for an Individual U.S. LNG Project 
This step demonstrates how the study results can be used, starting with the default U.S. average 
LNG export results (from Step 9) and hypothetical project data, to estimate the consequential 
GHG intensity and SC-GHG for an individual U.S. LNG project. This methodology could be used 
 
38 Note that for the sake of this simple demonstration, all speciated GHG emissions in the consequential 
model have been aligned to just CO 2 and CH4 emissions (this includes all species of emissions shown in 
Step 5). CO2 emissions have been combined with N2O emissions, and CH4 emissions have been combined 
with F-gases.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-26 
to support a side -by-side comparison of the estimated consequential GHG intensity of an 
individual project against the U.S. default values. 
Two hypothetical projects are described below: one with higher liquefaction emissions than the 
U.S. default value (example 1) and one with lower liquefaction emissions than the U.S. default  
(example 2). Two metrics are used for comparing the GHG performance : (1) GHG intensity in 
CO2e using IPCC AR6, 100-yr GWPs and (2) SC-GHG estimates.  
Metric #1: Comparative Environmental GHG Performance: Consequential 
GHG Intensity 
Table 18 represents a hypothetical LNG export project side by side with the default values from 
Step 9. In this hypothetical scenario, the facility liquefaction emissions are double those of the 
default facility; values different from the default facility are bolded. 
The consequential GHG intensity per unit of LNG exported (in Table 18) is increased by 5.3 (the 
amount of ‘doubled’ liquefaction emissions estimated in Step 3) and is now +11. 5 g CO 2e/MJ, 
which is 84% higher than the default facility (6.3 g CO2e/MJ) from Step 9. 
The second hypothetical project case assumes a project with 50% lower GHG intensity for the 
liquefaction stage, as shown in Table 19. 
The consequential GHG intensity per unit of LNG exported (as shown in Table 19) is +3. 6 g 
CO2e/MJ (down 42% from +6.3 g CO 2e/MJ for the default). While both hypothetical scenarios 
focused on liquefaction information, the same framework could be used to evaluate emissions 
differences resulting from the upstream source of gas. 
Table 18. Hypothetical example 1: High GHG intensity liquefaction project example (based on 
difference in defined policies scenarios, Market-Resolved vs. Existing/FID Exports) 
Stage 
Average Default GHG Intensity 
(g CO2e/MJ) 
Project GHG Intensity 
(g CO2e/MJ) 
CO2 CH4 Total CO2 CH4 Total 
NG Upstream 5.6 3.6 9.2 5.6 3.6 9.2 (Avg Default) 
Liquefaction 5.1 0.2 5.3 10.1 0.4 10.5 (Project) 
Project Non-Direct 
Emissions  -4.8 -3.4 -8.2 -4.8 -3.4 -8.2 
Total Consequential 
Global GHG Emissions 
Intensity 
5.8 0.4 +6.3 10.9 0.6 +11.5

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-27 
Table 19. Hypothetical example 2: Low GHG intensity liquefaction project example (based on 
difference in current policies scenarios, Market-Resolved vs. Existing/FID Exports) 
Stage 
Average Default GHG Intensity 
(g CO2e/MJ) 
Project GHG Intensity 
(g CO2e/MJ) 
CO2 CH4 Total CO2 CH4 Total 
NG Upstream 5.6 3.6 9.2 5.6 3.6 9.2 (Avg Default) 
Liquefaction 5.1 0.2 5.3 2.6 0.1 2.6 (Project) 
Project Non-direct Emissions -4.8 -3.4 -8.2 -4.8 -3.4 -8.2 
Total Consequential Global 
LC GHG Emissions Intensity 5.8 0.4 +6.3 3.3 0.3 +3.6 
Metric #2: Comparative Environmental Performance: Consequential Social 
Costs of Greenhouse Gases 
The second metric uses the 2023 SC-GHG as introduced in Step 7 to identify and compare the 
monetized values of the damages associated with a project’s direct and non-direct emissions. 
The “Difference” between the U.S. average (Default Facility) and the hypothetical example 
(Project Specific) data shows the net change in social cost of greenhouse gases when liquefaction 
emissions are doubled  (high GHG intensity liquefaction example) and when liquefaction 
emissions are reduced  by 50% ( low GHG  intensity liquefaction example).  The project direct 
emissions associated with the default facility and this illustrative project-specific example were 
estimated using annual emissions estimates to calculate the SC-GHG results. 
In Metric #1, the metric is in g CO2e per MJ exported natural gas. To assess how liquefaction 
emissions could affect the SC-GHG, the GHG intensity in Metric #1 is used to determine the 
annual emissions, by species, for a hypothetical facility that exports 1 Bcf/d every year from 
2020 through 2050 (equivalent to 0.36 EJ/year or 360 billion MJ/yr). These annual export 
volumes are multiplied by the GHG intensities in Table 18 to generate the yearly speciated 
greenhouse gas emissions that are used in the SC-GHG calculations.  
Table 20 summarizes the SC-GHG results across the three discount rates for the first hypothetical 
project facility (high liquefaction) inclusive of market consequences.  
Table 20. Social cost of greenhouse gases for hypothetical example 1: High GHG intensity 
liquefaction [base year 2024, dollar year 2020] 
 
Social Cost of Greenhouse Gases ($billion) for 
a Facility Exporting 1 Bcf/d from 2020 through 2050 
2.5% Discount Rate 2% Discount Rate 1.5% Discount Rate 
CO2 CH4 N2O Total CO2 CH4 N2O Total CO2 CH4 N2O Total 
Default 
Facility $7.8 $0.28 $0.00 $8.1 $13 $0.37 $0.00 $13 $22 $0.51 $0.00 $23 
Project-
Specific  $15 $0.40 $0.03 $15 $24 $0.53 $0.05 $25 $42 $0.73 $0.08 $43 
Difference  $6.8 $0.12 $0.03 $6.9 $11 $0.16 $0.05 $11 $19 $0.22 $0.08  $19  
Percent 
Difference 87% 44% -0% 86% 87% 44% -0% 86% 87% 44% -0% 86%

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-28 
The results suggest that the total lifetime social costs of the project direct and project non-direct 
greenhouse gas emissions from a 1 Bcf/d facility are about $8 billion to $23 billion for a facility 
with default average intensity values (varying across discount rates), with the large majority of 
social costs related to GHG emissions being attributed to emissions of CO2. A 1 Bcf/d facility with 
double liquefaction emissions has a social cost of greenhouse gases that are about $15 billion to 
$43 billion, $7 billion to $20 billion higher than the average 1 Bcf/d facility, a difference of about 
86%.  
Table 21 summarizes the SC-GHG results under each of the three discount rates for the second 
hypothetical project facility, also assuming 1 Bcf/d capacity for the years 2020 -2050, based on 
Table 19. 
The SC-GHG results of this second example show that a hypothetical 1 Bcf/d facility with 50% 
lower liquefaction emissions has a SC-GHG of about $4.6 to $13 billion, $3.5 billion to $10 billion 
lower than the average 1 Bcf/d facility, a difference of -43%.  
Table 21. Social cost of greenhouse gases for hypothetical example 2: Low GHG intensity 
liquefaction [base year 2024, dollar year 2020] 
 
Social Cost of Greenhouse Gases ($billion) for 
a Facility Exporting 1 Bcf/d from 2020 through 2050 
2.5% Discount Rate 2% Discount Rate 1.5% Discount Rate 
CO2 CH4 N2O Total CO2 CH4 N2O Total CO2 CH4 N2O Total 
Default 
Facility $7.8 $0.28 $0.00 $8.1 $13 $0.37 $0.00 $13 $22 $0.51 $0.00 $23 
Project-
Specific  $4.4 $0.22 -$0.02 $4.6 $7.3 $0.29 -$0.03 $7.6 $13 $0.39 -$0.04 $13 
Difference  -$3.4 -$0.06 -$0.02 -$3.5 -$5.6 -$0.08 -$0.03 -$5.7 -$9.7 -$0.11 -$0.04 -$10 
Percent 
Difference -43% -22% -0% -43% -43% -22% -0% -43% -43% -22% -0% -43% 
CONSEQUENTIAL LCA MODELING RESULTS FOR ALL SCENARIO COMPARISONS 
The sections above detailed the steps of the consequential analysis and used a single comparison 
set ( Defined Policies: Model Resolved versus Defined Policies: Existing/FID Exports ) to 
demonstrate example results. This section summarizes the results for all other scenarios included 
in the broader study.  Note that due to adjustments made to the GCAM data  and described in 
Steps 4 and 5, these results differ slightly from the GHG emissions values shown in Appendix A 
of the broader study. 
Following the approach in  Step 7, Table 22 shows the cumulative change in GHG emissions, 
changes in U.S. LNG Exported, and consequential GHG intensities of U.S. exports for all 
scenarios (baseline scenario is Existing/FID within each scenario). Also included is the weighted 
index summary change in cumulative global services, as shown in Table 3. Differences in global 
services are included to provide the full picture of changes resulting from the change in U.S. LNG 
exports. Increased U.S. LNG exports are leading to higher emissions in the non-ExFID scenarios 
as well as increased global services.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-29 
Table 22. Cumulative consequential GHG intensities of U.S. exports, LHV, AR6, 100-yr basis  
Scenario 
Cumulative 
Change in GHG 
Emissions, 
2020-2050 
(Tg CO2e)a 
Cumulative 
Change in U.S. 
LNG Exported, 
2020-2050 
(EJ)a 
Change in 
Cumulative 
Global 
Servicesa,b 
Consequential 
GHG Intensity 
of U.S. LNG 
Exports 
(g CO2e/MJ)a 
Defined Policies 
DP: Hi Exp 1,452 189 1.0015 7.7 
DP: MR 711 113 1.0008 6.3 
DP: Hi ME Sup: MR 363 100 1.0005 3.6 
DP: Hi US Sup: MR 1,186 156 1.0013 7.6 
DP: Lo US Sup: MR 32 18 1.0001 1.8 
Commitments 
C (Hi CCS): Hi Exp 787 107 1.0009 7.3 
C (Hi CCS): MR 97 31 1.0002 3.1 
C (Mod CCS): Hi Exp 1,055 87 1.0008 12.1 
C (Mod CCS): MR 67 11 1.0001 5.9 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 324 93 1.0008 3.5 
NZ (Hi CCS): MR 21 17 1.0001 1.2 
NZ (Mod CCS): Hi Exp 955 76 1.0005 12.6 
NZ (Mod CCS): MR39 0 0 1.0000 - 
Notes:  
a  Changes for all scenarios found vs. Existing/FID within each scenario.  
b Scenarios modeled provide different levels of global services  in response to changes in U.S. LNG exports . Values 
are indexed to the Existing/FID results within each scenario.    
 
For the Defined Policies scenarios , the cumulative differences in U.S. LNG exported from the 
Existing/FID to other scenarios range from 18  EJ to 189 EJ over the study period . The 
consequential GHG intensity per unit of U.S. LNG exported values range from 1.8 to 7.7. The 
Defined Policies: Model Resolved and Defined Policies: High Exports scenarios provide 0.08% to 
0.15% more cumulative global services than the Defined Policies: Existing/FID Exports scenario 
baseline. 
For the Commitments scenarios, the cumulative differences in U.S. LNG exported from the 
Existing/FID to other scenarios range from 11 EJ to 107 EJ over the study period. As a result, the 
consequential GHG intensity per unit of U.S. LNG exported values range from 3.1 to 12.1. The 
High CCS and Mod CCS scenarios provide 0.01% to 0.09% more cumulative global services than 
the Commitments Existing/FID Exports scenario baselines. 
Finally, for the Net Zero 2050 scenario, the cumulative differences in U.S. LNG exported from the 
Existing/FID Exports to other scenarios range from 0 EJ to 93 EJ. As a result, the consequential 
GHG intensity per unit of U.S. LNG exported values range from 1.2 to 12.6 (not including the 
scenario where there is no difference in exports). The High CCS and Mod CCS scenarios provide 
0.01% to 0.08% more cumulative global services than the Net Zero 2050 Existing/FID Exports 
scenario baselines.  
The speciated GHG emissions inputs to the consequential GHG intensity can also be used with 
the 2023 SC -GHG methodology to monetize the impacts of the changes in GHG emissions 
associated with increased U.S. LNG exports. The base year (which can also be cons idered the 
 
39 Note that the results for the Net Zero 2050 market response scenario for moderate CCS adoption leads 
to an extraneous result due to the GCAM model estimation of negligible changes in LNG exports and 
emissions.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-30 
present value year) was chosen to be 2024 to align with the time of the study, consistent with the 
suggested choice aligning with a regulatory impact assessment time. The study used 2020 as the 
dollar year, consistent with the default year of damages provided in the framework. The SC-GHG 
values (in year 2020 dollars) used by the method are summarized in Appendix C-3.  
Cumulative results are included in Table 23. The SC-GHG values are generally highest for the 
High Export scenarios within a set of scenarios, and also generally highest for Defined Policies 
scenarios, followed by Commitments scenarios, followed by Net Zero 2050 scenarios. 
Table 23. Changes in cumulative social cost of greenhouse gases (SC-GHG), 2020$ 
Scenarioa 
Cumulative Change in 
Emissions, 2020-2050 
(Tg CO2e)a,b 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)a 
Cumulative 
Change in 
Global 
Servicesa,c 
Cumulative 
Change in SC-GHG 
($billion 2020)a 
CO2 CH4 N2O Total 2.5% 2.0% 1.5% 
Defined Policies 
DP: Hi Exp 1,401 79 -88 1,452 189 1.0015 $150 $250 $450 
DP: MR 709 17 -47 711 113 1.0008 $74 $130 $220 
DP: Hi ME Sup: MR 436 -68 -25 363 100 1.0005 $42 $72 $130 
DP: Hi US Sup: MR 1,135 72 -71 1,186 156 1.0013 $120 $210 $360 
DP: Lo US Sup: MR 42 -8 -6 32 18 1.0001 $3 $6 $11 
Commitments 
C (Hi CCS): Hi Exp 870 -95 -25 787 107 1.0009 $89 $150 $270 
C (Hi CCS): MR 143 -50 -4 97 31 1.0002 $12 $22 $40 
C (Mod CCS): Hi Exp 1,088 -60 0 1,055 87 1.0008 $120 $200 $360 
C (Mod CCS): MR 83 -18 0 67 11 1.0001 $8 $14 $25 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 402 -85 -22 324 93 1.0008 $36 $63 $120 
NZ (Hi CCS): MR 49 -29 -3 21 17 1.0001 $3 $6 $12 
NZ (Mod CCS): Hi Exp 1,007 -59 -11 955 76 1.0005 $110 $190 $330 
NZ (Mod CCS): MR 0 0 0 0 0 1.0000 $0 $0 $0 
a  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
b  Values shown on IPCC AR6, 100-yr basis. Total also includes F-gases (not shown in table). 
c  Scenarios modeled provide different levels of global services  in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
As shown in Table 23, in the Defined Policies scenarios, increasing U.S. LNG exports are 
generally leading to higher cumulative CO2 and CH4 emissions and lower N2O emissions globally, 
whereas, in the Commitments and Net Zero 2050 scenarios, cumulative CO 2 emissions are 
generally increasing, while CH 4 and N 2O emissions are generally decreasing. Similarly, the 
change in methane emissions are generally a small part of the total change in GHG emissions. 
 
The changes in SC-GHG between scenarios summarized in Table 23 were also normalized per 
change in MJ of U.S. LNG exported. Normalized results are included in  Table 24. Overall, the 
normalized SC-GHG ranges between 0.02 and 0.24 cents per MJ for Defined Policies Scenarios, 
0.04 cents per MJ and 0.41 cents per MJ for Commitments Scenarios, and 0.02 cents per MJ and 
0.43 cents per MJ in Net Zero 2050 Scenarios.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-31 
Table 24. Normalized changes per MJ exported in cumulative social cost of greenhouse gases 
Scenario 
Cumulative 
Change GHG 
Emissions 
2020-2050 
(Tg CO2e)a 
Cumulative 
Change in U.S. 
LNG Exported, 
2020-2050 
(EJ)a 
Cumulative 
Change in 
Global 
Servicesa,b 
Cumulative Change in 
SC-GHG per MJ 
(cents/MJ)a 
Discount Rate 
2.5% 2.0% 1.5% 
Defined Policies 
DP: Hi Exp 1,452 189 1.0015 0.08 0.14 0.24 
DP: MR 711 113 1.0008 0.07 0.11 0.20 
DP: Hi ME Sup: MR 363 100 1.0005 0.04 0.07 0.12 
DP: Hi US Sup: MR 1,186 156 1.0013 0.08 0.13 0.23 
DP: Lo US Sup: MR 32 18 1.0001 0.02 0.03 0.06 
Commitments 
C (Hi CCS): Hi Exp 787 107 1.0009 0.08 0.14 0.25 
C (Hi CCS): MR 97 31 1.0002 0.04 0.07 0.13 
C (Mod CCS): Hi Exp 1,055 87 1.0008 0.14 0.23 0.41 
C (Mod CCS): MR 67 11 1.0001 0.07 0.13 0.23 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 324 93 1.0008 0.04 0.07 0.12 
NZ (Hi CCS): MR 21 17 1.0001 0.02 0.04 0.07 
NZ (Mod CCS): Hi Exp 955 76 1.0005 0.15 0.24 0.43 
NZ (Mod CCS): MR 0 0 1.0000 N/A N/A N/A 
Notes:  
a  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario.  
b  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario.  
 
Following Step 8, Table 25 summarizes the consequential GHG intensities of U.S. LNG exports 
and project non-direct emissions values for all scenarios in this study (compared to a baseline of 
the Existing/FID Exports scenario within their global climate policy).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-32 
Table 25. Summary of consequential GHG intensities and project non-direct emissions values for 
all scenarios (versus ExFID), AR6, 100-yr basis 
Scenario 
Cumulative 
Change in 
GHG 
Emissions 
2020-2050 
(Tg CO2e)a 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)a 
Change in 
Cumulative 
Global 
Servicesa,b 
Consequential 
GHG Intensity 
of U.S. LNG 
Exports 
Project 
Non-Direct 
Emissions 
Factor 
(PNDE)c 
Grams of Carbon Dioxide 
Equivalents per Megajoule 
of U.S. LNG Exporteda 
(g CO2e/MJ) 
DP: Hi Exp 1,452 189 1.0015 7.7 -6.8 
DP: MR 711 113 1.0008 6.3 -8.2 
DP: Hi ME Sup: MR 363 100 1.0005 3.6 -10.9 
DP: Hi US Sup: MR 1,186 156 1.0013 7.6 -6.9 
DP: Lo US Sup: MR 32 18 1.0001 1.8 -12.7 
C (Hi CCS): Hi Exp 787 107 1.0009 7.3 -7.2 
C (Hi CCS): MR 97 31 1.0002 3.1 -11.4 
C (Mod CCS): Hi Exp 1,055 87 1.0008 12.1 -2.4 
C (Mod CCS): MR 67 11 1.0001 5.9 -8.6 
NZ (Hi CCS): Hi Exp 324 93 1.0008 3.5 -11 
NZ (Hi CCS): MR 21 17 1.0001 1.2 -13.3 
NZ (Mod CCS): Hi Exp 955 76 1.0005 12.6 -1.9 
NZ (Mod CCS): MR 0 0 1.0000 - - 
Notes:  
a  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario  
b  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
c  Assumes project direct emissions defined as including Natural Gas Upstream and Liquefaction of 14.5 g CO2e/MJ.  
 
The project non-direct emissions values are not specific to a receiving region and represent a 
result across all potential landing locations for LNG. Note that the consequential GHG intensity 
and project non-direct emissions results were aggregated in relation to estimated future volumes 
of exported LNG from the U.S. in the context of a global model. Project non-direct emissions 
results represent overall expected effects and not those of individual shipments of LNG. As shown 
in Table 25, t he consequential GHG intensity and corresponding project non-direct emissions 
values are different for each scenario pairing. This study does not prescribe likelihood of one 
scenario pairing over another, but rather, presents the range of derived results for a set of potential 
future scenarios modeled by the study, see Table 1 and Appendix A for description of study 
scenarios. 
Consequential analysis results using the IPCC AR6, 20-yr GWP values are summarized in Table 
26. As further described in Appendix C-2, this required converting all initially received GCAM 
values to the AR6, 20-yr basis, and aligning them with the NETL natural gas baseline study values 
on an AR6, 20-yr basis. The project direct emissions , comprised of natural gas upstream and 
liquefaction emissions, was also recalculated on an AR6, 20-yr basis, and found to be 21.3 g 
CO2e/MJ.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-33 
Table 26. Summary of consequential GHG intensities and project non-direct emissions values for 
all scenarios (versus ExFID), AR6, 20-yr basis 
Scenario 
Cumulative 
Change in 
GHG 
Emissions 
2020-2050 
(Tg CO2e)a 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)a 
Change in 
Cumulative 
Global 
Servicesa,b 
Consequential 
GHG Intensity 
of U.S. LNG 
Exports 
Project Non-
Direct 
Emissions 
Factor 
(PNDE)c 
Grams of Carbon Dioxide 
Equivalents per Megajoule of 
U.S. LNG Exporteda 
(g CO2e/MJ) 
DP: Hi Exp 1,533 189 1.0015 8.1 -13.1 
DP: MR 718 113 1.0008 6.3 -14.9 
DP: Hi ME Sup: MR 252 100 1.0005 2.5 -18.8 
DP: Hi US Sup: MR 1,262 156 1.0013 8.1 -13.2 
DP: Lo US Sup: MR 18 18 1.0001 1.0 -20.2 
C (Hi CCS): Hi Exp 626 107 1.0009 5.8 -15.4 
C (Hi CCS): MR 17 31 1.0002 0.6 -20.7 
C (Mod CCS): Hi Exp 943 87 1.0008 10.8 -10.4 
C (Mod CCS): MR 38 11 1.0001 3.4 -17.9 
NZ (Hi CCS): Hi Exp 176 93 1.0008 1.9 -19.4 
NZ (Hi CCS): MR -24 17 1.0001 -1.4 -22.7 
NZ (Mod CCS): Hi Exp 845 11.2 1.0005 11.2 -10.1 
NZ (Mod CCS): MR 0 0 1.0000 - - 
Notes:  
a  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario  
b  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
c  Assumes project direct emissions defined as including Natural Gas Upstream and Liquefaction of 14.5 g CO2e/MJ.  
 
In the Defined Policies scenarios, higher LNG exports generally lead to net higher cumulative CH4 
emissions, while in Commitments and Net Zero 2050 scenarios, cumulative CH4 emissions are 
decreasing. As the GWP value for CH4 is roughly 2.7 times higher for AR6, 20-yr than AR6, 100-
yr, scenarios with significant CH4 emissions increases or decreases (as compared to their 
Existing/FID baseline) have their cumulative CH4differences amplified as a result. In one scenario 
(Net Zero 2050 (High CCS): Model Resolved ), the effect is that the  amplified value of CH4 
emissions results in a net change in GHG emissions that goes from positive (in AR6, 100-yr) to 
negative (in AR6, 20 -yr), making  the consequential GHG intensity negative ( -1.4 g CO 2e/MJ) 
instead of the previous +1.2 g CO2e/MJ. Likewise, the project non-direct emissions values on the 
AR6, 20 -yr basis are more negative than those in AR6, 100 -yr, because the project direct 
emissions value is increased from the 14.5 g CO2e/MJ used in the AR6, 100-yr basis to 21.3 g 
CO2e/MJ on an AR6, 20-yr basis. 
A. Individual Project Direct Emissions Breakeven GHG Performance  
The project direct emissions and project non -direct emissions can be used to calculate a 
breakeven rate, which would be the percent change difference between an individual project’s 
emissions and the default factors that would result in a global consequential intensity of zero (i.e., 
0 g CO2e/MJ). As defined above, the U.S. average performance values are the 9.2 g CO2e/MJ for 
upstream and 5.3 g CO2e/MJ for liquefaction (the sum of which result in an average U.S. project 
direct emissions of 14.5). The project non-direct emissions values from Table 25 can be used with 
the average project direct emissions values to estimate the breakeven percent as shown here:

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-34 
𝐵𝑟𝑒𝑎𝑘𝑒𝑣𝑒𝑛 (%) = 𝐴𝑏𝑠𝑜𝑙𝑢𝑡𝑒 𝑉𝑎𝑙𝑢𝑒 𝑜𝑓 𝑃𝑟𝑜𝑗𝑒𝑐𝑡 𝑁𝑜𝑛𝑑𝑖𝑟𝑒𝑐𝑡 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠 − 𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑃𝑟𝑜𝑗𝑒𝑐𝑡 𝐷𝑖𝑟𝑒𝑐𝑡 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠𝐴𝑣𝑒𝑟𝑎𝑔𝑒 𝑃𝑟𝑜𝑗𝑒𝑐𝑡 𝐷𝑖𝑟𝑒𝑐𝑡 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑠  × 100 
Table 27 shows the resulting breakeven percent changes in project direct emissions needed for 
all scenarios modeled (versus ExFID) on an AR6,100-yr basis.  
Table 27. Breakeven percent changes (versus ExFID), AR6, 100-yr basis 
Scenarioa 
Cumulative 
Change in 
GHG 
Emissions, 
2020-2050 
(Tg CO2e)b 
Cumulative 
Change in U.S. 
LNG Exported, 
2020-2050 
(EJ)b 
Change in 
Global 
Servicesb,c 
Breakeven GHG 
Emissions Change 
in Project Direct 
Emissionsb 
DP: Hi Exp 1,452 189 1.0015 -53% 
DP: MR 711 113 1.0008 -43% 
DP: Hi ME Sup: MR 363 100 1.0005 -25% 
DP: Hi US Sup: MR 1,186 156 1.0013 -53% 
DP: Lo US Sup: MR 32 18 1.0001 -13% 
C (Hi CCS): Hi Exp 787 107 1.0009 -51% 
C (Hi CCS): MR 97 31 1.0002 -21% 
C (Mod CCS): Hi Exp 1,055 87 1.0008 -84% 
C (Mod CCS): MR 67 11 1.0001 -40% 
NZ (Hi CCS): Hi Exp 324 93 1.0008 -24% 
NZ (Hi CCS): MR 21 17 1.0001 -8% 
NZ (Mod CCS): Hi Exp 955 11.2 1.0005 -87% 
Notes:  
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario.  
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
 
To illustrate a specific example for the AR6, 100-yr results, for Defined Policies: Model Resolved, 
the project direct emissions  would need to be 43% lower to breakeven (the project direct 
emissions would have to decrease from 14.5 g CO2e/MJ to 8.2 g CO2e/MJ). In that scenario the 
project direct emissions would be 8.2 g CO2e/MJ and would offset the project non-direct emissions 
of -8.2 g CO2e/MJ, so the consequential GHG intensity would be zero. These results show that, 
depending on the assumed scenario, the project direct emissions would need to be reduced by 
at least 8% and up to 87% for U.S. LNG exports to have a zero consequential GHG intensity (i.e., 
to result in no net increase in global GHG emissions, holding all else equal). 
Building on the breakeven analysis for Defined Policies: Model Resolved  and its focus on the 
tradeoff between project direct and project non -direct emissions, the project direct upstream 
emissions of 9.2 g CO2e/MJ (production through transmission) include 3.6 g CO2e/MJ associated 
with methane emissions. The methane emissions correspond to an upstream methane emission 
rate of 0.56% (production through transmission). For example, if the upstream methane emission 
rate for a specific project was reported as 1.4%, the upstream methane emissions contribution to 
the project direct upstream emissions would increase by 5.4 g CO2e /MJ to 9.0 g CO 2e/MJ, 
resulting in project direct upstream emission s of 14.6 g CO 2e/MJ. Combined with the average 
project direct liquefaction emissions (5.3 g CO2e/MJ), the project direct emissions would be 19.9 
g CO2e/MJ. In order to breakeven, the project direct emissions would have to be lowered from 
19.9 g CO 2e/MJ to 8.2 g CO 2e/MJ. The required project direct emission reductions  (11.7 g 
CO2e/MJ) are greater than the average project direct liquefaction emissions. The implication is 
that a project  with upstream emissions of 1.4% would not breakeven even if  its liquefaction

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-35 
process had no emissions while the upstream natural gas methane emission rate  was 1.4%. In 
such a case, a completely carbon neutral liquefaction facility would result in a consequential GHG 
emissions intensity of 6.4 g CO2e/MJ, a 0.1 g CO 2e/MJ increase in GHG emissions per MJ of 
natural gas exported  (i.e., Upstream Project Direct Emissions + Liquefaction Project Direct 
Emissions + Project Non-Direct Emissions = Consequential GHG Emissions Intensity; or 14.6 + 
0 – 8.2 = 6.4). 
Table 28 summarizes the breakeven analysis on an AR6, 20-yr GHG emissions basis.  
Table 28 Breakeven percent changes (versus ExFID), AR6, 20-yr basis 
Scenarioa 
Cumulative 
Change in GHG 
Emissions, 
2020-2050 
(Tg CO2e)b 
Cumulative 
Change in U.S. 
LNG Exported, 
2020-2050 
(EJ)b 
Change in 
Global 
Servicesb,c 
Breakeven GHG 
Emissions 
Change in 
Project Direct 
Emissionsb 
DP: Hi Exp 1,533 189 1.0015 -38% 
DP: MR 718 113 1.0008 -30% 
DP: Hi ME Sup: MR 252 100 1.0005 -12% 
DP: Hi US Sup: MR 1,262 156 1.0013 -38% 
DP: Lo US Sup: MR 18 18 1.0001 -5% 
C (Hi CCS): Hi Exp 626 107 1.0009 -27% 
C (Hi CCS): MR 17 31 1.0002 -3% 
C (Mod CCS): Hi Exp 943 87 1.0008 -51% 
C (Mod CCS): MR 38 11 1.0001 -16% 
NZ (Hi CCS): Hi Exp 176 93 1.0008 -9% 
NZ (Hi CCS): MR -24 17 1.0001 +7% 
NZ (Mod CCS): Hi Exp 845 11.2 1.0005 -53% 
Notes:  
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario.  
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
 
To illustrate a specific example for the AR6, 20-yr results, for Defined Policies: Model Resolved, 
the project direct emissions  would need to be 30% lower to breakeven (the project direct 
emissions would have to decrease from 21.3 g CO2e/MJ to 14.9 g CO2e/MJ). In that scenario the 
decreased project direct emissions would be 14.9 g CO2e/MJ and would offset the project non-
direct emissions of -14.9 g CO2e/MJ, so the consequential GHG intensity would be zero. These 
results show that, depending on the assumed scenario, the project direct emissions would need 
to be reduced by up to 53%, or in one scenario increase by 7%, for U.S. LNG exports to have a 
zero consequential GHG. 
B. Evaluation of Model Sensitivity to Key Performance Attributes 
Sensitivity analyses were also conducted to evaluate the potential impact on the scenario results 
if key model aspects were underrepresented in the analysis. Specifically, upstream methane 
intensity of global natural gas production and representation of global liquefaction facility 
operating emissions were evaluated. In each sensitivity analysis case, GCAM results have been 
modified exogenously, as opposed to doing additional model runs in GCAM.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-36 
1. Sensitivity Analysis 1: Upstream Methane Emissions Intensity 
This analysis considers the sensitivity of the consequential results to the assumed upstream 
natural gas methane emissions rates in GCAM. To accomplish this, methane emissions rates for 
the U.S. and the other natural gas producing regions in GCAM were adjusted using an index 
based on the relative change in the U.S. methane emissions rate. 
To accomplish this, the GCAM -NETL-aligned U.S. upstream emissions estimates were aligned 
with the 2024 NETL Natural Gas Baseline on a speciated basis. As part of the alignment,  U.S. 
upstream CH4 emissions were scaled to match the 0.56% NETL methane emissions rate while 
keeping total CO 2e emissions of the natural gas sector consistent with the GCAM results . This 
provides a distinct and aligned estimate of upstream NG sector emissions for the sensitivity 
analysis.  
The range of U.S. upstream natural gas sector methane emission rates in this analysis is from 
0.2% (about one third of the NETL estimated rate) to 2.8% (a value at the high end of recently 
completed studies) and is done at increments of 0.2%. Table 29 includes the assumed U.S. 
methane emissions rate for the sensitivity cases and the relative level of upstream methane. The 
relative level of methane is the percentage applied to non-U.S. methane emissions rates to scale 
them for this sensitivity analysis. This approach preserves the unique country/regional methane 
emission rate differences within GCAM. 
Table 29 summarizes the consequential GHG intensity resulting from the assumed changes in 
the upstream natural gas  production methane emissions rate s applied globally  for Defined 
Policies: Model Resolved versus Defined Policies: Existing/FID Exports . In all other scenario 
pairings, the contribution of methane emissions are lower  (or are  decreasing with respect to 
increased U.S. exports) and therefore exhibit less sensitivity to changes in methane intensity of 
natural gas production. 
Note that in this comparison while the increase in methane emissions increases overall global 
GHG emissions, the increase is happening in both scenarios. Since the consequential intensity 
is calculated based on the difference between the scenarios , the increased methane emissions 
have limited impact  on the intensity  (e.g., if the same number is added to two different linear 
equations, the difference between the two equations remains the same). To the extent methane 
emissions associated with increased U.S. LNG exports are increasing, there would be offsetting 
changes in the global energy system as a result of substitution of the U.S. LNG for natural gas 
and other sources of energy. 
Table 29. Sensitivity analysis for upstream methane emissions rate (U.S. base is 0.56%), DP:MR 
versus DP: ExFID 
U.S. Methane 
Emission Rate 
Relative Level of 
Upstream Methane 
Consequential GHG 
Intensity 
(g CO2e/MJ) 
Percent Change in 
Consequential GHG 
Intensity from Base 
0.20% 35.7% 6.3 0% 
0.40% 71.4% 6.3 0% 
0.60% 107.1% 6.3 0% 
0.80% 142.9% 6.3 0% 
1.00% 178.6% 6.3 0% 
1.20% 214.3% 6.3 0% 
1.40% 250.0% 6.3 0% 
1.60% 285.7% 6.3 0% 
1.80% 321.4% 6.3 0%

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-37 
2.00% 357.1% 6.3 0% 
2.20% 392.9% 6.3 0% 
2.40% 428.6% 6.4 2% 
2.60% 464.3% 6.4 2% 
2.80% 500.0% 6.4 2% 
Note: Baseline U.S. Methane Emissions Rate is 0.56%. 
2. Sensitivity Analysis 2: Liquefaction Plant Emissions Representation within 
GCAM 
Within GCAM, GHG emissions from liquefaction are modeled in an aggregate other industrial 
energy use sector that comprises many activities. LNG-relevant processes and activities are only 
one of many modeled in each sector. Unlike other sectors in GCAM where activities are modeled 
from interactions with other sectors, growth in this sector is generally mo deled as a function of 
exogenously defined GDP (i.e., if GDP goes up then activity and associated emissions increase 
comparably). As part of this study, the connections between GHG emissions and GDP growth in 
GCAM were compared for several regions expected to provide significant LNG supplies over time, 
to assess how well the sectoral results from GCAM might be modeling expected increases in LNG 
activities. However, this analysis was unable to estimate a specific amount by which the values 
are under (or over) estimated in a particular region. As a result, instead of adjusting GCAM 
sectoral values (e.g., as done above for upstream natural gas methane intensity),  a sensitivity 
analysis was conducted to show the effects on model results associated with liquefaction 
processes. 
In this sensitivity case, the U.S. average performance values referenced above for liquefaction 
(5.3 g CO2e/MJ) are added exogenously for all global LNG exports for all regions, not just those 
exported by the U.S. This is done because the GCAM model is otherwise representing global 
emissions of all LNG produced, not just those exported by the U.S. While emissi ons are added 
for all LNG, the denominator for the consequential GHG intensity remains per additional unit of 
U.S. LNG exported. This case adds these liquefaction emissions on top of the existing baseline 
emissions of the modeled scenario. 
Table 30 summarizes the original results from Table 22 (referred to as the base case) as well as 
those from the sensitivity case (accounting for additional emissions for liquefaction). While it might 
be expected that the consequential results simply would shift by the intensity of emissions added, 
(i.e., by 5.3 g CO 2e/MJ), this is not the case because while all global LNG has its emissions 
intensity increased, the new result is divided only by the U.S. LNG exported. As a result, the net 
differences are smaller than the 5.3 g CO 2e/MJ value. For example, the values for the Defined 
Policies: Model Resolved scenario are 6.3 g CO2e/MJ in the base case, and 10 g CO2e/MJ in the 
Sensitivity Case, a difference of 3.7 g CO2e/MJ as opposed to the 5.3 g CO2e/MJ that were added 
per unit of global LNG produced. 
Generally, even in a worst case of adding additional full liquefaction emissions to the base case 
GHG emissions, the project non -direct emissions values remain negative. There are only two 
exceptions – the Commitments (Moderate CCS): High Exports and the Net Zero 2050 (Moderate 
CCS): High Exports scenarios.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-38 
Table 30. Sensitivity analysis results for additional liquefaction emissions  
Scenarioa 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)b 
Change in 
Global 
Servicesb,c 
Base 
Case 
Sensitivity 
Case: 
Added 
Liquefaction 
Base 
Case 
Sensitivity 
Case: 
Added 
Liquefaction 
Consequential GHG 
Intensity per Unit U.S. 
LNG Exported  
(g CO2e/MJ)b 
Project Non-Direct 
Emissions 
(g CO2e/MJ)b 
Defined Policies 
DP: Hi Exp 189 1.0015 7.7 11.8 -6.8 -2.7 
DP: MR 113 1.0008 6.3 9.9 -8.2 -4.6 
DP: Hi ME Sup: MR 100 1.0005 3.6 6.1 -10.9 -8.5 
DP: Hi US Sup: MR 156 1.0013 7.6 11.6 -6.9 -2.9 
DP: Lo US Sup: MR 18 1.0001 1.8 4.1 -12.7 -10.4 
Commitments 
C (Hi CCS): Hi Exp 107 1.0009 7.3 11.2 -7.2 -3.3 
C (Hi CCS): MR 31 1.0002 3.1 5.9 -11.4 -8.6 
C (Mod CCS): Hi Exp 87 1.0008 12.1 16.4 -2.4 +1.9 
C (Mod CCS): MR 11 1.0001 5.9 8.4 -8.6 -6.1 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 324 1.0008 3.5 7.5 -11 -7.1 
NZ (Hi CCS): MR 21 1.0001 1.2 3.7 -13.3 -10.8 
NZ (Mod CCS): Hi Exp 955 1.0005 12.6 18.1 -1.9 +3.6 
Notes:  
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario.  
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
C. Market Drivers for Changes in GHG Intensity of U.S. LNG Exports 
NETL completed an additional analysis to evaluate the market drivers of the change in global 
GHG emissions in GCAM with respect to changes in U.S. LNG export GHG intensity when 
providing an equivalent service to society.  
1. Change in Global Services 
As summarized in Table 3, in addition to volumes of LNG exported and GHG emissions for each 
scenario, the GCAM model also provides estimated outputs of various services including energy, 
transportation, commodity materials, and fertilizers. The results from GCAM show that as higher 
levels of U.S. LNG are exported, global services increase. An abridged summary of some of the 
aggregated service categories (now cumulative for all years 2020-2050, not just model years) is 
provided in Table 31. The first row shows that the Defined Policies: Existing/FID Exports scenario 
provides 10,158 EJ of energy services globally, and the Defined Policies: Model Resolved and 
DP:HighExp scenarios provide higher levels  of energy services, commensurate with more U.S. 
LNG being put into the global market.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-39 
Table 31. Summary of GCAM modeled services provided in selected defined policies scenarios 
Aggregate 
Economic Sector Type of Service Output (Unit) DP: ExFID DP: MR DP: High Exp 
Energy Energy Services (EJ) 10,158 10,168 10,176 
Industrial 
Commodity Products 
Million Metric Tons (MT) 175,861 175,926 175,979 
Nitrogen Fertilizer 
Million Metric Tons (MT) 5,079 5,077 5,076 
Transportation 
Freight Transportation 
(Billion-Ton-Kilometers) 6,742,516 6,745,127 6,747,250 
Passenger Transportation 
(Billion-Passenger-Kilometers) 7,863,606 7,863,998 7,864,321 
Weighted Index 1.0000 1.0008 1.001 
The results presented for the consequential LCA part of the study were estimated with the values 
in Table 31, i.e., those that show that increased LNG leads to increased levels of services provided 
(and will now be referred to as “increased services” results).  
2. GHG Intensity of U.S. LNG Exports per Unit of Global Services (Equivalent 
Unit of Service)   
As a result of the identified difference in services provided between scenarios within global climate 
policies, an additional analysis was performed to quantify the effect of this difference on the model 
results. A consequential LCA, unlike an attributional LCA, does not have to mainta in functional 
equivalence but must report the difference in the function (in this case, the services provided). In 
this additional analysis, the GHG emissions are compared based on the same level of global 
services provided. This helps explore how replacing one product or service with another affects 
emissions, both directly and indirectly, to offer the same service to society.  
In this additional analysis, the results of the increased services scenario models were adjusted to 
provide equivalent levels of global services. Table 32 expands the summarized results for Defined 
Policies: Model Resolved and Defined Policies: Existing/FID Exports . The consequential GHG 
emissions per unit of U.S. LNG as derived above (for the case of increased services provided) 
would be +6.3 g CO 2e/MJ, due to a 113 EJ difference in cumulative LNG exported and a 
cumulative difference of 711 Tg CO 2e of GHG emissions between the cases. However, there is 
also a cumulative difference of 9.7 EJ more global energy services provided in the Defined 
Policies: Model Resolved scenario versus Defined Policies: Existing/FID Exports. This means that 
the Defined Policies: Model Resolved scenario is providing more global services to society as 
compared to the Defined Policies: Existing/FID Exports scenario. This was a general finding 
across all scenarios when compared to the ExFID scenario, and not just Defined Policies: Model 
Resolved versus Defined Policies: Existing/FID Exports. 
Table 32. Cumulative (2020 -2050) GCAM results for DP:ExFID and DP:MR (with increased 
services) 
Scenario 
U.S. LNG 
Exports 
(EJ) 
Change in 
U.S. LNG 
Exports 
(EJ) 
Global 
Energy 
Services 
(EJ) 
Change in 
Global 
Energy 
Services 
(EJ) 
GHG 
Emissions 
(Tg CO2e) 
Change in 
GHG 
Emissions 
(Tg CO2e) 
Consequential 
GHG Intensity 
(g CO2e/MJ) 
DP: ExFID 227.4 - 10,158 - 1,552,340 - - 
DP: MR 340.6 113.2 10,168 9.7 1,553,051 710.8 6.3

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-40 
To make these two scenarios “equivalent on a functional unit basis of services delivered”, since 
the Defined Policies: Model Resolved scenario provides a higher level of global services (9.7 EJ), 
its U.S. LNG export volume and GHG emissions values are linearly scaled to meet the lower 
energy service levels of Defined Policies: Existing/FID Exports. In doing so, the difference across 
all service levels is found, and by assumption, the GHG emissions were scaled down by the same 
difference.40 
Using the derived weighted index value from Table 31 of 1.0008 as a scaling factor for changes 
in global services, results for Defined Policies: Model Resolved were scaled down for all service 
categories to meet the assumed weighted average level for Defined Policies: Existing/FID 
Exports. Global EJ of service supplied are scaled from 10,168 to 10,158 (making them equal), 
leading to updated estimates for Defined Policies: Model Resolved  of 112.9 EJ of U.S. LNG 
exported, and 1,551,825 Tg of CO2e emissions, as shown in Table 33.  
In making these adjustments, both the numerator and denominator of the consequential GHG 
intensity per unit U.S. LNG are changed. The cumulative GHG emissions difference is now 
negative (-515 Tg, was positive before), since emissions of Defined Policies: Model Resolved are 
now less than Defined Policies: Existing/FID Exports, and the cumulative U.S. LNG Exported is 
slightly lower than before (112.9 EJ instead of 113.2 EJ). Overall, for this example, the equivalent 
services-adjusted consequential GHG intensity per unit of LNG is now -4.6 g CO2e/MJ for Defined 
Policies: Model Resolved. 
The most prominent effect of this scaling down of GHG emissions is that the GHG emissions of 
the Defined Policies: Model Resolved scenario is lower than the Defined Policies: Existing/FID 
Exports scenario, suggesting that when excluding increases in global services, U.S. LNG 
substitutions for other energy services results in a net decrease in GHG intensity. In other words, 
U.S. LNG substitution in foreign markets results in lower global GHG emissions when accounting 
for all changes in energy services. 
Table 33. Summary of GCAM results for DP:ExFID and DP:MR (with equivalent services) 
Scenario 
U.S. LNG 
Exports 
(EJ) 
Change in 
U.S. LNG 
Exports 
(EJ) 
Global 
Energy 
Services 
(EJ) 
Change in 
Global 
Energy 
Services 
(EJ) 
GHG 
Emissions 
(Tg CO2e) 
Change in 
GHG 
Emissions 
(Tg CO2e) 
Consequential 
GHG Intensity 
(g CO2e/MJ) 
DP: ExFID 227.4 - 10,158 - 1,552,340 - - 
DP: MR 340.4 112.9 10,158 0 1,551,825 -515.4 -4.6 
 
Table 34 shows a summary of equivalent services-adjusted consequential GHG intensity values 
per unit of LNG exported for all scenarios, following the method presented above. 
 
 
40 The GCAM model provides outputs of various services including energy, transportation, commodity 
materials, and a weighted-average metric was provided by PNNL to help consider an appropriate scaling 
factor encompassing all services provided, not just those provided by energy (see Appendix C-2 for 
details).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-41 
Table 34. Cumulative consequential GHG intensities of U.S. exports (LHV, AR6 , 100-yr, 
equivalent services basis) 
Scenarioa 
Cumulative 
Change in GHG 
Emissions, 
2020-2050 
(Tg CO2e)b 
Cumulative 
Change in U.S. 
LNG Exported, 
2020-2050 
(EJ)b 
Change in 
Global 
Servicesb,c 
Consequential 
GHG Intensity 
per Unit U.S. 
LNG Exported 
(g CO2e/MJ)b 
Defined Policies 
DP: Hi Exp -838 188 0 -4.5 
DP: MR -515 113 0 -4.6 
DP: Hi ME Sup: MR -364 100 0 -3.6 
DP: Hi US Sup: MR -778 115 0 -5.0 
DP: Lo US Sup: MR -119 18 0 -6.8 
     
Commitments 
C (Hi CCS): Hi Exp -379 107 0 -3.6 
C (Hi CCS): MR -156 31 0 -5.0 
C (Mod CCS): Hi Exp 114 86 0 +1.7 
C (Mod CCS): MR -3 11 0 -0.3 
     
Net Zero 2050 
NZ (Hi CCS): Hi Exp -489 93 0 -5.3 
NZ (Hi CCS): MR -75 17 0 -4.4 
NZ (Mod CCS): Hi Exp 496 76 0 +6.6 
Notes:  
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario.  
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Scenarios modeled provide different levels of global services in response to changes in U.S. LNG exports. Values 
are indexed to the Existing/FID results within each scenario. 
 
The consequential GHG intensity per unit LNG generally switches from positive to negative for 
equivalent service adjusted scenarios (except for two of them). This occurs because the GCAM 
model results between scenarios, especially for GHG emissions, are very similar (within 1%) and 
tend to only vary by small amounts, even when cumulative over the 2020-2050 period. By making 
the scaling adjustment, what were small positive changes in emissions values become negative 
change emissions values when compared to the ExFID baselines.  
By revisiting the results for the Defined Policies: Model Resolved versus Defined Policies: 
Existing/FID Exports  scenario analysis above, the original (increased services) results were 
based on a cumulative difference of 711 Tg CO2e (Defined Policies: Model Resolved higher than 
Defined Policies: Existing/FID Exports). In scaling the scenario results to an equivalent services 
basis, it is revealed that 515 Tg of emissions were substituted for providing energy services and 
thus the difference (1,226 Tg) was associated with providing additional energy to society. 
3. Summary of Market Drivers of Total Consequential GHG Intensity of U.S. 
LNG Exports 
For additional comparative context, Tables 35 and 36 provide direct attributional life cycle GHG 
emissions and direct and indirect emissions from market effects from increased U.S. LNG exports. 
Attributional life cycle GHG emissions from production, export, and end use of the fuel in an Asian 
destination market is presented in Table 35 assuming 100% combustion of U.S. LNG exports with 
unabated emissions at the point of end use (i.e., no carbon capture and storage (CCS) installed 
at point of end use ). The illustrative attributional life cycle GHG emissions profile  has 76 g

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-42 
CO2e/MJ of LNG exported .41 This attributional GHG emission profile  would represent the 
expected contribution to global emissions if 100% of U.S. LNG exports resulted in an equivalent 
increase in global services, without any market substitution. To put this in the terms of exports, for 
1 Bcf/d of LNG exported to an Asian destination market, the annual unabated direct life cycle 
GHG emissions would total up to 27 Tg CO2e. 
Multiplying the total increase in U.S. LNG export by the attributional profile from production 
through end use equals the total direct GHG emissions  from increased U.S. LNG exports when 
market effects are not accounted for  (i.e., an approach similar to those of past studies ).42 For 
example, c omparing Model Resolved  to Existing/FID Exports levels in the Defined Policies 
scenario, the direct life cycle GHG emissions from production, export, and end use (assuming 
100% combustion without CCS) of increased U.S. LNG exports would cumulatively (2020-2050) 
contribute 8,588 Tg CO2e before accounting for market effects . In 2050, direct life cycle GHG 
emissions from all modeled U.S. LNG exports (56.3 Bcf/d) would be approximately 1,500 Tg CO2e 
before accounting for market effects.  
Consequential modeling  of direct and indirect market effects  provided by the GCAM model 
determined that both market substitution and increased global services occur when the supply of 
U.S. LNG is increased to the global market, compared to the Existing/FID levels for each scenario. 
The section above, GHG Intensity of U.S. LNG Exports per Unit of Global Services (Equivalent 
Unit of Service) , summarized the net market effects  from market substitution only ( excluding 
increased global services). The market substitution effect is larger when representing the direct 
life cycle GHG emissions from increased exports and accounting for the resulting change from 
direct and indirect market effects. This value is reported in Tables 35 and 36 as the Cumulative 
Change in Direct Attributional Emissions of Direct and Indirect Market Substitution Effects only, 
2020 – 2050 and is obtained by determining the difference between  the cumulative change in 
direct GHG emissions  and the cumulative change in GHG emissions from Table 34 on an 
equivalent services basis (also reproduced in Table 35 and Table 36 below). 
Combining the net market substitution effects with the change in GHG emissions from increased 
global services, the result equals the cumulative change in GHG emissions as determined in Step 
7 above and reported in Table 22. 
Table 36 summarizes the direct and indirect life cycl e GHG emissions contributions if 100% of 
U.S. LNG exports were consumed at end use facilities equipped with 90% carbon capture 
equipment and permanent sequestration of the captured carbon dioxide to prevent release to the 
atmosphere. The illustrative attributional life cycle GHG emissions profile of U.S. LNG consumed 
in an Asian market with 90% carbon capture on end use combustion is modeled as 30 g CO2e/MJ 
of LNG exported.  
Tables 35 and 36 provide bounding perspectives based on the end use of U.S.LNG exported fuel 
being combusted without or with CCS. The  consequential result determined from the GCAM 
model accounts for the variations in both end use destinations and end use applications. These 
tables are intended to help facilitate an understanding of consequential market effects in context 
of the attributional GHG emissions that result from production, export, and use of increased U.S. 
LNG exports for each scenario pairing.  
 
41 The attributional values found for use in this section were calculated using the natural gas upstream and 
liquefaction values updated in this study for the year 2020, the end use combustion values from the 2020 
NETL Natural Gas Report (Khutal et al, 2024), and the use and losses of gas and GHG emissions for ocean 
shipping through regasification values from the 2019 NETL LNG Update  (Roman-White et al, 2019). The 
combustion cases are representative of F and H-class NGCC plants (without CCS and with 90% CCS) from 
the 2020 (Khutal et al, 2024) study. The 90% CCS case was selected to match those of the GCAM model.  
42 See, for example, Roman-White et al, 2019.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-43 
Table 35. Summary of market drivers of total consequential GHG intensity of increased U.S. LNG 
exports, cumulative change, 2020 - 2050 (LHV, AR6, 100-yr), direct emissions end use of U.S. 
LNG represented as unabated combustion (no CCS) 
Scenarioa 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)b,c 
Cumulative 
Change in 
Direct 
Attributional 
Emissions 
from 
Increased 
U.S. LNG 
Exports if 
100% 
Combusted 
w/o CCS 
End Use, 
2020-2050 
(Tg CO2e)b,d 
Cumulative 
Change in 
Direct 
Attributional 
Emissions of 
Direct and 
Indirect 
Market 
Substitutions, 
2020-2050 
(Tg CO2e)b,e 
Cumulative 
Change in 
Direct and 
Indirect GHG 
Emissions 
Market 
Substitution 
Effects Only,  
2020-2050 
(Tg CO2e)b,f 
Cumulative 
Change in 
Indirect GHG 
Emissions 
from 
Increased 
Global 
Services 
Effects Only, 
2020-2050 
(Tg CO2e)b,g 
Cumulative 
Change in 
GHG 
Emissions, 
2020-2050 
(Tg CO2e)b,h,i 
Defined Policies 
DP: Hi Exp 188  14,288  -15,126 -838 2,290 1,452 
DP: MR 113  8,588  -9,103 -515 1,226 711 
DP: Hi ME Sup: MR 100  7,600  -7,964 -364 727 363 
DP: Hi US Sup: MR 115  8,740  -9,518 -778 1,964 1,186 
DP: Lo US Sup: MR 18  1,368  -1,487 -119 151 32 
Commitments 
C (Hi CCS): Hi Exp 107  8,132  -8,511 -379 1,166 787 
C (Hi CCS): MR 31  2,356  -2,512 -156 253 97 
C (Mod CCS): Hi Exp 86  6,536  -6,422 114 1,169 1,055 
C (Mod CCS): MR 11  836  -839 -3 70 67 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 93  7,068  -7,557 -489 813 324 
NZ (Hi CCS): MR 17  1,292  -1,367 -75 96 21 
NZ (Mod CCS): Hi Exp 76  5,776  -5,280 496 459 955 
Notes: 
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario. 
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Conversion of annual values from EJ/year to Bcf/d is 1:2.7759 
d Assumes every EJ of U.S. LNG exported is combusted at end use and released to the atmosphere (no CCS). Oceans 
shipping was modeled as 100% to Asian Market (27,500 nautical miles, round trip). Attributional life cycle result (76 
g CO2e/MJ LHV, AR6, 100-yr) is provided to illustrate the absolute cumulative emissions to the environment from 
2020 - 2050 for one example end destination and use. Consequential modeling results account for a range of end 
destinations and end uses with varying degrees of CCS deployment depending on the scenario. 
e Total direct emissions from increased U.S. LNG exports plus the indirect GHG emissions from market substitution 
effects, excludes GHG emissions from increases in global services. Direct emissions are estimated for illustrative 
purposes based on direct emissions from U.S. LNG exports if 100% combusted w/o CCS end use. 
f Results from Table 34, Cumulative Consequential GHG Intensities for U.S. Exports (LHV, AR6, 100 -yr, equivalent 
services basis). 
g Derived from the absolute difference between the cumulative change in GHG emissions from Table 22 (all 
consequences) and Table 34 (excludes change in global services). 
h Results from Table 22. Cumulative Consequential GHG Intensities of U.S. Exports, LV, AR6,100-yr Basis. 
i  Consequential GHG Intensity of U.S. LNG Exports (g CO2e/MJ), as reported in Table 22, can be obtained by dividing 
the Cumulative change in GHG Emissions, 2020 - 2050 (this column)  by the Cumulative Cha nge in U.S. LNG 
Exported, 2020 – 2050 (second column in the table).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-44 
Table 36. Summary of market drivers of total consequential GHG intensity of increased U.S. LNG 
exports, cumulative change, 2020 - 2050 (LHV, AR6, 100-yr), direct emissions end use of U.S. 
LNG represented as 90% CCS at end use 
Scenarioa 
Cumulative 
Change in 
U.S. LNG 
Exported, 
2020-2050 
(EJ)b,c 
Cumulative 
Change in 
Direct GHG 
Emissions 
from 
Increased 
U.S. LNG 
Exports if 
100% 
Combusted 
with 90% CCS 
End Use, 
2020-2050 
(Tg CO2e)b,d 
Cumulative 
Change in 
Direct 
Attributional 
Emissions of 
Direct and 
Indirect 
Market 
Substitutions, 
2020-2050 
(Tg CO2e)b,e 
Cumulative 
Change in 
Direct and 
Indirect GHG 
Emissions 
Market 
Substitution 
Effects Only,  
2020-2050 
(Tg CO2e)b,f 
Cumulative 
Change in 
Indirect GHG 
Emissions 
from 
Increased 
Global 
Services 
Effects Only, 
2020-2050 
(Tg CO2e)b,g 
Cumulative 
Change in 
GHG 
Emissions, 
2020-2050 
(Tg CO2e)b,h,i 
Defined Policies 
DP: Hi Exp 188  5,640  -6,478 -838 2,290 1,452 
DP: MR 113  3,390  -3,905 -515 1,226 711 
DP: Hi ME Sup: MR 100  3,000  -3,364 -364 727 363 
DP: Hi US Sup: MR 115  3,450  -4,228 -778 1,964 1,186 
DP: Lo US Sup: MR 18  540  -659 -119 151 32 
Commitments 
C (Hi CCS): Hi Exp 107  3,210  -3,589 -379 1,166 787 
C (Hi CCS): MR 31  930  -1,086 -156 253 97 
C (Mod CCS): Hi Exp 86  2,580  -2,466 114 1,169 1,055 
C (Mod CCS): MR 11  330  -333 -3 70 67 
Net Zero 2050 
NZ (Hi CCS): Hi Exp 93  2,790  -3,279 -489 813 324 
NZ (Hi CCS): MR 17  510  -585 -75 96 21 
NZ (Mod CCS): Hi Exp 76  2,280  -1,784 496 459 955 
Notes: 
a  Scenario NZ (Mod CCS): MR is not presented here because model-resolved LNG exports do not exceed existing/FID 
levels in this scenario. 
b  Changes for all scenarios found vs. Existing/FID within each global climate policy scenario. 
c  Conversion of annual values from EJ/year to Bcf/d is 1:2.7759 
d Assumes every EJ of U.S. LNG exported is combusted at end use and 90% of the end use carbon dioxide emissions 
are captured and sequestered from being released  to the atmosphere. Oceans shipping was modeled as 100% to 
Asian Market ( 27,500 nautical miles, round trip). Attributional life cycle result (30 g CO2e/MJ LHV, AR6, 100-yr) is 
provided to illustrate the absolute cumulative emissions to the environment from 2020 - 2050 for one example end 
destination and use.  Consequential modeling results account for a range of end destinations and end uses with 
varying degrees of CCS deployment depending on the scenario. 
e Total direct emissions from increased U.S. LNG exports plus the indirect GHG emissions from market substitution 
effects, excludes GHG emissions from increases in global services.  Direct emissions are estimated for illustrative 
purposes based on direct emissions from U.S. LNG exports with 90% CCS at end use combustion. 
f Results from Table 34, Cumulative Consequential GHG Intensities for U.S. Exports (LHV, AR6, 100 -yr, equivalent 
services basis). 
g Derived from the absolute difference between the cumulative change in GHG emissions from Table 22 (all 
consequences) and Table 34 (excludes change in global services). 
h Results from Table 22. Cumulative Consequential GHG Intensities of U.S. Exports, LV, AR6,100-yr Basis. 
i  Consequential GHG Intensity of U.S. LNG Exports (g CO2e/MJ), as reported in Table 22, can be obtained by dividing 
the Cumulative change in GHG Emissions, 2020 - 2050 (this column)  by the Cumulative Cha nge in U.S. LNG 
Exported, 2020 – 2050 (second column in the table). 
D. Modeling Caveats and Limitations 
The results of this study are dependent on various data sources, models, and assumptions that 
are highly connected. Important caveats and limitations of this analysis include: 
1. For the estimation of liquefaction emissions of projects, the basis of the NETL GHG 
intensity estimates are current practice and data. This affects the primary result as well as 
the framework for the individual project analysis. As modeled within this stud y, the U.S.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-45 
average performance for liquefaction facilities used as the default value is a static 
reference aligned to year 2020 industry performance. This liquefaction facility value is not 
adjusted in future modeling years for potential unknown industry changes, suc h as 
implementation of carbon capture and storage, electrification, etc. 
2. The upstream natural gas GHG intensity profile is currently based on the 2024 NETL 
Natural Gas baseline study. Measurement studies of the combined oil and gas sectors 
suggest methane emission rates could be higher for natural gas production than are 
represented in the NETL natural gas model. Sensitivity to upstream methane emissions is 
evaluated in the Results, Sensitivity Analysis section of this study.  
3. Changes in the quantity of natural gas liquefied globally result in direct changes in 
emissions from liquefaction operations represented in the GCAM model. Liquefaction 
operations are modeled as a component of other industrial emissions within GCAM and 
are responsive to changes in country GDP and not directly connected to changes in 
country-level LNG export volumes. Therefore, sensitivity to liquefaction operating 
emissions representation in the GCAM model is evaluated in the Results, Sensitivity 
Analysis section of this study. 
STUDY SUMMARY 
The purpose of this study was to examine the potential global GHG emissions implications of a 
wide range of levels of U.S. LNG exports. Key conclusions include:  
1. Differences in volumes of U.S. LNG exports lead to different levels both of GHG emissions 
and of global services provided. When compared to scenarios that assume export levels 
based on existing and under construction facilities ( Existing/FID), higher levels of U.S. 
LNG exports lead to higher global GHG emissions (ranging from 21 Tg CO2e to 1,452 Tg 
CO2e or about 0.002% to 0.1%), as well as higher levels of global services provided 
(ranging from 0.006% to about 0.1%). 
2. The GCAM upstream GHG intensity values for all scenarios are within 1% of the values 
in the latest NETL Natural Gas baseline study (representative of the base year of this 
study, 2020) on an IPCC AR6, 100-yr basis.  
a. Per MJ of natural gas scaled to account for liquefaction losses, the production 
through transmission (upstream) GHG intensity is 9.2 g CO 2e/MJ exported on an 
IPCC AR6, 100-yr GWP , LHV basis and 15.7 g CO2e/MJ exported on an IPCC 
AR6, 20-yr GWP , LHV basis.  
b. Overall, adjustments to align to NETL national average performance data for GHG 
intensity added about 20 Tg CO 2e emissions per model year, an increase of less 
than 0.05% on an AR6, 100-yr basis, and subtracted about 100 Tg CO2e emissions 
per model year, a decrease of less than 0.2% (AR6, 20-yr basis). 
3. The national average GHG intensity for liquefaction operations in the base year is modeled 
using government reported data and expanded to provide representative life cycle system 
boundaries, resulting in a GHG emissions intensity of 5.3 g CO2e/MJ of natural gas ready 
for export, reported on an IPCC AR6, 100 -yr lower heating value (LHV) basis, and 5.6 g 
CO2e/MJ on an IPCC AR6, 20-yr lower heating value (LHV) basis. 
4. This analysis defines the upstream natural gas and liquefaction processes as project direct 
emissions, the direct emissions from export and use of the natural gas and direct and 
indirect market effects as project non -direct emissions and the sum of them to  be the 
consequential GHG intensity of U.S. LNG Exports. Given the upstream natural gas and 
liquefaction values estimated above, the average U.S. project direct emissions for 2020, 
the baseline year for this study, is 9.2 + 5.3 = 14.5 g CO 2e/MJ (AR6, 100-yr), and 21.3 g 
CO2e/MJ (AR6, 20-yr).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-46 
5. The consequential GHG intensity is the effect (inclusive of both direct and indirect 
emissions) of U.S. LNG on global emissions per unit of U.S. LNG exported. The 
consequential GHG intensity is defined as the difference in GHG emissions between the 
scenarios divided by the difference in U.S. LNG exports. For instance, for one of the 
scenario comparisons assessed ( Defined Polices: Model Resolved ) the consequential 
GHG intensity is +6.3 g CO2e/MJ (on both an AR6, 100-yr and AR6, 20-yr basis), indicating 
that the overall global effect of producing and exporting U.S. LNG leads to an increase in 
global GHG emissions resulting from consequential market effects.  
a. Analysis of the results shows that direct and indirect market substitutions result in 
a decrease in global GHG emissions intensity when compared on an equivalent 
global services basis. The increased availability of U.S. LNG on the global market 
enables increased demand for energy to be met with a lower cost energy supply 
option that often displaces more or equally GHG emissions -intensive fuels (e.g., 
coal and oil) within the model over the thirty-year study period. 
b. Results also show that increasing the availability of U.S. LNG on the global market 
(increased global energy supply) results in increased consumption of global 
services when compared to the baseline scenario (e.g., Defined Policies: 
Existing/FID). The consequential effect of increased global consumption of energy 
and services directly contributes to increased global GHG emissions.  
c. The net result of these two market effects is an increase in global GHG emissions 
of +6.3 g CO 2e/MJ of NG exported from the U.S. Across all scenarios, this GHG 
intensity figure ranges from 1.2 g CO2e/MJ to 12.6 g CO2e/MJ (AR6, 100-yr basis), 
and -1.4 g CO2e/MJ to 11.2 g CO2e/MJ (AR6, 20-yr basis). 
d. The increase in global GHG emissions between the Defined Policies: Model 
Resolved and Defined Policies: Existing/FID scenarios is estimated to result in a 
cumulative SC -GHG impact of $74 billion using a discount rate of 2.5%, $130 
billion using a discount rate of 2.0%, and $220 billion using a discount rate of 1.5% 
(all 2020$). Per MJ, this equates to a range of 0.02 cents/MJ to 0.15 cents/MJ 
(2.5%). The cumulative SC -GHG of the increase in global emissions across the 
study scenarios ranged from $3 billion to $150 billion (2.5%) to $12 billion to $450 
billion (1.5%) in 2020$.  
6. Estimated consequential GHG impacts and SC-GHG values for an individual U.S. export 
project can be calculated by using individual project values in place of the default of U.S. 
average values modeled in the study. 
a. For example, on an AR6, 100-yr basis, given the NETL average liquefaction 
emissions for a project of 5.3 g CO2e/MJ, if an individual project has a 
liquefaction process with emissions that are half of the average (2.65 g CO2e 
/MJ), the individual project consequential GHG intensity could be adjusted down 
by 2.65 g CO2e/MJ (calculated as the difference between the average of 5.3 g 
CO2e/MJ and the individual project emissions intensity of 2.65 g CO2e/MJ). If the 
average U.S. consequential GHG intensity is 6.3 g CO2e /MJ, the individual 
project consequential intensity would be 3.65 g CO2e /MJ. 
b. Total lifetime social costs of the project direct and project non -direct greenhouse 
gas emissions from a 1 Bcf/d facility operating for 30 years are estimated to be $8 
billion to $ 23 billion ($2020) for a facility with default average intensity values 
(varying across assumed discount rates). A similar facility with half the liquefaction 
emissions would have social costs of greenhouse gases estimated to be $4.6 
billion to $13 billion ($2020).

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-47 
APPENDICES TO THIS REPORT 
Appendix C-1: NEMS and NETL LCA Model Results Comparison 
Appendix C-2: Incorporation, Assessment, and Adjustments to the Global Change Analysis Model 
(GCAM) Results 
Appendix C-3: Social Cost of Greenhouse Gases Modeling and Additional Results 
Appendix C-4: Detailed Data Tables for Values Summarized in this Report

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-48 
APPENDIX C-1: NEMS AND NETL LCA MODEL RESULTS COMPARISON 
The NEMS modeling done in this project focused on domestic changes that would be expected 
to occur in the scenarios modeled. NETL reviewed the NEMS data to evaluate if the regional 
production mix of natural gas would be expected to change over time. If the  NEMS results 
suggested that production would be expected to shift significantly from the current mix of regions, 
and especially if to distinctly higher or lower intensity regions, then NETL would have 
recommended adjustments to the assumed GHG intensity for U.S. natural gas in the results. 
For all scenarios, NEMS-modeled data of dry natural gas production of “Production by OGSM 
District” were mapped to a state and then to an NETL natural gas model region as shown in Table 
C-1.1. Note that several “states” are offshore regions. 
Table C -1.1. Matching NEMS (Oil and Gas Methane Partnership states) to NETL states and 
regions 
Production by OGSM District State Region 
Alabama, North Alabama Southeast 
Alabama, South Alabama Southeast 
Arizona Arizona Southwest 
Arkansas Arkansas Southeast 
California California Pacific 
Colorado Colorado Rocky Mountain 
Connecticut Connecticut Northeast 
Delaware Delaware Northeast 
Florida Florida Southeast 
Georgia Georgia Southeast 
Idaho Idaho Rocky Mountain 
Illinois Illinois Midwest 
Indiana Indiana Midwest 
Iowa Iowa Midwest 
Kansas Kansas Midwest 
Kentucky Kentucky Southeast 
Louisiana, North Louisiana Southeast 
Louisiana, South Louisiana Southeast 
Maryland Maryland Northeast 
Massachusetts Massachusetts Northeast 
Michigan Michigan Midwest 
Minnesota Minnesota Midwest 
Mississippi, North Mississippi Southeast 
Mississippi, South Mississippi Southeast 
Missouri Missouri Midwest 
Montana Montana Rocky Mountain 
Nebraska Nebraska Midwest 
Nevada Nevada Rocky Mountain 
New Hampshire New Hampshire Northeast

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-49 
New Jersey New Jersey Northeast 
New Mexico, East New Mexico Southwest 
New Mexico, West New Mexico Southwest 
New York New York Northeast 
North Carolina North Carolina Southeast 
North Dakota North Dakota Midwest 
Ohio Ohio Midwest 
Oklahoma Oklahoma Southwest 
Oregon Oregon Pacific 
Pennsylvania Pennsylvania Northeast 
Rhode Island Rhode Island Northeast 
South Carolina South Carolina Southeast 
South Dakota South Dakota Midwest 
Tennessee Tennessee Southeast 
Texas RRC 1 Texas Southwest 
Texas RRC 2 Texas Southwest 
Texas RRC 3 Texas Southwest 
Texas RRC 4 Texas Southwest 
Texas RRC 5 Texas Southwest 
Texas RRC 6 Texas Southwest 
Texas RRC 7B Texas Southwest 
Texas RRC 7C Texas Southwest 
Texas RRC 8 Texas Southwest 
Texas RRC 8A Texas Southwest 
Texas RRC 9 Texas Southwest 
Texas RRC 10 Texas Southwest 
Utah Utah Rocky Mountain 
Virginia Virginia Northeast 
Washington Washington Pacific 
West Virginia West Virginia Northeast 
Wisconsin Wisconsin Midwest 
Wyoming Wyoming Rocky Mountain 
Alabama State Offshore Alabama Southeast 
Louisiana State Offshore Louisiana Southeast 
Texas State Offshore Texas Southwest 
California State Offshore California Pacific 
North Atlantic Federal Offshore North Carolina Southeast 
Mid Atlantic Federal Offshore Federal Offshore - GoM Southeast 
South Atlantic Federal Offshore South Carolina Southeast 
Eastern GOM Federal Offshore Federal Offshore - GoM Southeast 
Central GOM Federal Offshore Federal Offshore - GoM Southeast

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-50 
Western GOM Federal Offshore Federal Offshore - GoM Southeast 
California Federal Offshore California Pacific 
Northern Pacific Federal 
Offshore Federal Offshore - GoM Southeast 
Alaska Federal Offshore Federal Offshore - GoM Southeast 
 
This classification enables the aggregation of dry production data (excluding extraction losses) 
by region for each respective year, as summarized with every 10 years of data in Table C-1.2. 
Table C-1.2. Regional dry production (Tcf) between 2020 and 2050, DP:MR 
Region 2020 2025 2030 2035 2040 2045 2050 
Southeast 4.59 6.64 6.01 6.28 7.21 8.01 8.11 
Southwest 11.26 13.08 13.38 14.00 16.43 19.38 21.18 
Pacific 2.69 2.08 2.09 1.98 2.19 2.61 2.78 
Rocky Mountain 3.32 2.92 2.88 2.57 2.65 2.66 2.67 
Northeast 10.33 11.80 11.93 12.94 14.49 15.21 15.31 
Midwest 0.97 0.95 0.96 0.95 0.92 0.91 0.91 
From this aggregated data, the production share is calculated by dividing the region -specific 
production by the total U.S. production for each year and is summarized in Table C-1.3. 
Table C-1.3. Regional NG dry production shares, DP:MR 
Region 2020 2025 2030 2035 2040 2045 2050 
Midwest 0.139 0.177 0.161 0.162 0.164 0.164 0.159 
Northeast 0.339 0.349 0.359 0.362 0.374 0.397 0.416 
Pacific 0.081 0.056 0.056 0.050 0.050 0.054 0.055 
Rocky Mountain 0.100 0.078 0.077 0.067 0.060 0.055 0.052 
Southeast 0.311 0.315 0.320 0.335 0.330 0.312 0.300 
Southwest 0.029 0.025 0.026 0.024 0.021 0.019 0.018 
 
The regional production shares estimated based on NEMS data are disaggregated to a techno -
basin level based on the proportion of regional natural gas production shares in the 2020 NETL 
Natural Gas model. Based on the 2020 NETL Natural Gas model, Table C-1.4 provides the 
techno-basin to region mapping details and Table C-1.5 reports the GHG emissions intensity 
results for natural gas production from all techno-basins, for the production through transmission 
network life cycle boundary, using U.S. average transmission network data.  
Table C-1.4. Regional NG dry production shares, DP:MR 
Techno-basin Region 
Alaska Offshore Pacific 
Anadarko Conventional Southwest 
Anadarko Shale Southwest 
Anadarko Tight Southwest 
Appalachian Shale Northeast 
Arkla Conventional Southeast 
Arkla Shale Southeast 
Arkla Tight Southeast

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-51 
Arkoma Conventional Southwest 
Arkoma Shale Southwest 
East Texas Conventional Southwest 
East Texas Shale Southwest 
East Texas Tight Southwest 
Fort Worth Shale Southwest 
GoM Offshore  Southeast 
Green River Conventional Rocky Mountain 
Green River Tight Rocky Mountain 
Gulf Conventional Southwest 
Gulf Shale Southwest 
Gulf Tight Southwest 
Permian Conventional Southwest 
Permian Shale Southwest 
Piceance Tight Rocky Mountain 
San Juan Coalbed Methane Southwest 
San Juan Shale Southwest 
South Oklahoma Shale Southwest 
Strawn Shale Southwest 
Uinta Conventional Rocky Mountain 
Uinta Tight Rocky Mountain 
Table C-1.5. GHG emissions intensity by techno-basin, production through transmission network 
boundary using U.S. average transmission data (g CO2e/MJ, IPCC AR6, 100-yr GWP) 
Techno-basin GHG Emissions Intensity (g CO2e/MJ) 
Alaska Offshore 6.99E+00 
Anadarko Conv 1.62E+01 
Anadarko Shale 9.68E+00 
Anadarko Tight 1.17E+01 
Appalachian Shale 6.41E+00 
Arkla Conv 6.40E+00 
Arkla Shale 6.39E+00 
Arkla Tight 1.16E+01 
Arkoma Conv 1.54E+01 
Arkoma Shale 1.22E+01 
East Texas Conv 7.70E+00 
East Texas Shale 8.01E+00 
East Texas Tight 7.74E+00 
Fort Worth Shale 1.32E+01 
GoM Offshore  6.20E+00 
Green River Conv 1.28E+01 
Green River Tight 1.32E+01 
Gulf Conv 8.51E+00

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-52 
Gulf Shale 7.44E+00 
Gulf Tight 9.38E+00 
Permian Conv 9.61E+00 
Permian Shale 1.03E+01 
Piceance Tight 8.55E+00 
San Juan Coalbed Methane 1.77E+01 
San Juan Shale 2.72E+01 
South Oklahoma Shale 8.64E+00 
Strawn Shale 1.34E+01 
Uinta Conv 3.44E+01 
Uinta Tight 1.84E+01 
Note: The GHG emissions intensity results are provided on a per MJ NG delivered, LHV basis. Results 
from the 2020 NETL Natural Gas Model were converted from HHV to LHV basis for this work. 
Overall, Table C -1.6 suggests that the NEMS -modeled changes in domestic natural gas 
production by region across the scenarios are not expected to significantly affect the projected 
GHG emissions intensities over time as evidenced by the 0 to 0.004 variance across the time 
horizon and scenarios.  
Table C -1.6. Estimated U.S. average GHG intensity (g CO 2e/MJ) across NEMS scenarios, 
production through transmission (2020-2050) 
Scenario 2020 2025 2030 2035 2040 2045 2050 
DP: MR 0.083 0.082 0.082 0.082 0.082 0.083 0.084 
DP: ExFID 0.083 0.082 0.082 0.082 0.082 0.082 0.082 
DP Hi US Sup: MR 0.083 0.083 0.084 0.083 0.084 0.084 0.084 
DP Hi US Sup: 
ExFID 0.083 0.083 0.084 0.084 0.083 0.083 0.083 
DP Lo US Sup: MR 0.083 0.081 0.081 0.080 0.080 0.081 0.081 
DP Lo US Sup: 
ExFID 0.083 0.081 0.081 0.080 0.080 0.080 0.081

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-53 
APPENDIX C-2: INCORPORATION, ASSESSMENT, AND ADJUSTMENTS TO THE 
GLOBAL CHANGE ANALYSIS MODEL (GCAM) RESULTS  
Across all years and scenarios, GCAM has over 100 discrete sectors, hundreds of discrete 
technologies, and many sector -technology pairs that can vary depending on the model 
configuration. However, only a subset of these factors is relevant to this analysis (i.e., with a focus 
on the natural gas sector). 
Results provided by PNNL for the various scenarios and years modeled were provided as 
described in Table C-2.1 and were processed accordingly.  
Table C-2.1. Provided set of GCAM data documentation  
File Data Represented 
co2_em_tech Provides data showing CO2 emissions in megatons per year for various sectors, energy sources or “technology” for different scenarios across each of 32 regions. 
non_co2_em_tech 
Provides data showing non-CO2 emissions in gigagrams, equivalent to metric 
kilotons or 1,000 metric tons, for various sectors, energy sources or “technology” 
and different scenarios across each of 37 regions. 
inputs.by.tech Provides detailed information about energy consumption in different regions and sectors along with specific technologies and years.  
outputs.by.tech Reports the energy production within the various regions, by sectors (sub -sector is not applicable in this dataset) along with specific technologies and years.  
Columns Description 
scenario 
Scenario or context for which the data is provided such as “Defined Policies: 
Existing/FID,” which suggests that the data corresponds to the existing capacity or 
infrastructure in the region. 
region  This column specifies the geo-political region under consideration. 
sector This column categorizes the different sectors or areas of activity for which CO 2 emissions are being measured, e.g., “agricultural energy use,” “cement,” etc. 
sub-sector 
Within a sector, there may be further divisions or subcategories to specify the 
specific aspect of the sector being measured, e.g., by type of fuel or “mobile,” 
“stationary,” etc., indicating different types of energy use within a single sector. 
technology This column identifies the specific technology or energy source being utilized within the subsector. For example, “gas CC” and “gas steam/CT.” 
year The specific year or period for which the CO2 emissions values are provided; this ranges from 2020 to 2050. 
value Numerical values for the activity being described given combination of scenario, region, sector, subsector, technology, and year.  
ghg Refers to the GHG that is being emitted (for non-CO2 data). It identifies the specific type of gas responsible for the emissions, e.g., CH 4, N2O, HFC125, C2F6, etc. 
input The energy or other input into sector/subsector/technology. 
output The commodity or service provided by the sector/subsector/technology. 
A. GCAM and NETL (2020) Emissions Intensity Comparison and Adjustment 
The GCAM model represents economic activity (and associated GHG emissions) by sectors and 
technologies, and their respective inputs and outputs, for regions, years, and scenarios. However, 
only three sectors in GCAM include GHG emissions relevant to the natural gas sector: natural

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-54 
gas, gas pipeline, and other industrial energy use . In this document, these GCAM sectors are 
italicized when referred to given their colloquial use in other ways such as in describing stages of 
the natural gas life cycle.  
Using the basis of process stages as represented in the NETL Natural Gas model, Figure C-2.1 
shows the relevant GCAM sectors that have associated CO 2 and non-CO2 emissions. While, 
overall, GCAM has 16 species of GHG emissions, for the three GCAM sectors above relevant to 
the upstream natural gas sector, only emissions of CO 2, CH4, and N 2O were represented. Most 
stages of the NETL Natural Gas model framework are accounted for in these three GCAM sectors, 
but not all are explicitly scaled to production amounts of natural gas or derivative products. Also, 
the Ocean Shipping stage is included as part of trn_shipping_intl but the effects could not be 
separated out for this analysis. As a result, the comparison in this report was focused on a 
comparison of emissions from production of natural gas in the U.S. through delivery to a large 
end user rather than LNG delivered around the world.  
 
Figure C-2.1. Mapping of NETL natural gas stages to GCAM sectors 
To assess the alignment of the modeling of natural gas upstream emissions in GCAM against the 
NETL Natural Gas model, quantitative values of emissions intensities in the year 2020 of the 
various GCAM sectors for the “USA” region for the three natural gas-relevant sectors were listed 
and compared to NETL natural gas model results. Note, in order to compare NETL and GCAM 
results, NETL model results were regenerated using an LHV basis as shown below and differ 
from those published (as HHV by default) and listed in Step 2 of the report. 
However, the other industrial energy use  sector contains a diverse set of activities without 
explicitly representing emissions related to natural gas. GCAM incorporates a variety of data 
sources to represent activity in this sector. Relevant to natural gas activities for this sector, 2015 
International Energy Agency (IEA) data on energy use by oil and gas production activities used 
by the GCAM modeling team were provided and utilized to apportion GHG emissions associated 
with natural gas activity, as in Table C-2.2. 
Table C-2.2. LCA stage cross-mapping 
NETL LCA Stage IEA Energy Flow GCAM Sector – Energy & CO2 
Extraction Oil and Gas Extraction other industrial energy use 
Gathering and Boosting Oil and Gas Extraction other industrial energy use 
Processing Gas Works other industrial energy use 
Domestic Pipeline Transport Pipeline Transport gas pipeline 
Liquefaction LNG/Regasification Plants other industrial energy use

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-55 
Ocean Transport International Marine Bunkers trn_shipping_intl 
Regasification LNG/Regasification Plants other industrial energy use 
Pipeline Transport (at destination) Pipeline Transport gas pipeline 
The IEA data is aggregated into oil and gas activities such as “Extraction, Gathering and 
Boosting,” “Processing,” and “Liquefaction and Regasification.” However, a challenge is that the 
IEA data represents aggregated activities of extraction of both oil and gas resources. Given the 
lack of data on liquefaction and regasification in the 2015 IEA data (including for the United 
States), emissions from those activities are excluded from the analysis, consistent with the focus 
on upstream natural gas effects. 
Overall, only four subsector/technology pair values of the other industrial energy use sector in 
GCAM were considered: gas/gas, gas/gas cogen, refined liquids/refined liquids, and refined 
liquids/refined liquids cogen (and are shown as aggregated to the subsector level).  
The emissions intensity cells in Table C-2.3 show the underlying equation used to generate values 
on an AR6, 100-yr basis, where the numerator is the total emissions from GCAM for the USA 
region for the Defined Policies: Model Resolved scenario for the year 2020 for each of the three 
GHGs (if available), normalized by the total production of U.S. natural gas and oil from GCAM in 
2020 (32.29 EJ and 22.32 EJ, respectively). Note that GCAM reports “production” of resources 
but actually maps more appropriately to “delivered product”. As such the basis of the GCAM and 
NETL boundaries match (all are in terms of NG del ivered). Units of emissions intensity follow 
those internal to GCAM, which are Tg CO 2 equivalent/EJ, which conveniently are equal to g 
CO2e/MJ, the same units as used in the NETL model. Thus, the bottom rows in Table C-2.3 show 
comparisons to those of the NETL model.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-56 
Table C-2.3. GCAM emissions intensities for sectors (DP:MR, 2020, USA region, AR6 , 100-yr 
basis) 
   
Estimated GCAM Emissions Intensity 
(LHV) 
(Tg CO2e/EJ, g CO2e/MJ) [IPCC AR6, 
100-yr] 
GCAM Sector NETL LCA Stage Comments/Potential Mapping Inaccuracy CO2 CH4 N2O 
gas pipeline Transmission and Storage 
Have assumed this fully 
represents the Transmission 
sector equivalent to the 
NETL Natural Gas model. 
38.0/32.3 = 
1.18 - - 
natural gas 
Production + 
Gathering & 
Boosting + 
Processing  
From discussions with 
GCAM team, this sector 
represents all other natural 
gas related activities, thus 
the mapping to all other 
NETL stages other than 
transmission. 
- 138.3/32.3 = 4.28 .014/32.3 = 4.5 E-4 
other industrial 
energy use 
(technology = 
gas or gas 
cogen)a 
For 2015, 
Extraction, 
Gathering & 
Boosting 
 
Estimates from IEA energy 
shares. 
 
For technology = gas or gas 
cogen, all GHG emissions 
allocated to the natural gas 
product. 
 
For technology = refined 
liquids or refined liquids 
cogen, GHG emissions are 
allocated to the natural gas 
and crude oil products on an 
energy (EJ) produced basis 
from GCAM output data. 
92.9/32.3 = 
2.88 
0.06/32.3 = 
0.002 
0.04/32.3 = 
0.001 
other industrial 
energy use 
(technology = 
refined liquids 
and refined 
liquids cogen)a 
10.3/(32.3+
22.3) = 0.2 
0.07/(32.3+
22.3) = 
0.001 
0.39/(32.3+
22.3) = 
0.007 
other industrial 
energy use 
(electricity)a 
- - - 
Total GCAM by gas (LHV) 
= 1.18 + 
2.88 + .2 = 
4.24 
4.28 0.009 
Total GCAM (LHV) 8.53 
Subtotal from NETL Model, Processing through 
Transmission boundary – LHV basis 8.63 
Adjustment factor (LHV) 8.63/8.53 = 1.0117 
 
Overall, the estimated upstream emissions intensity for the USA region in GCAM in the year 2020 
for Defined Policies: Model Resolved was about 8.53 g CO2e/MJ (AR6, 100-yr, LHV basis), which 
is slightly lower than the GHG emissions intensity estimated by the NETL model for the production 
through transmission boundary (8.63 g CO2e/MJ, AR6, 100-yr, LHV basis). Using the relationship 
between those estimates, emissions results in the three GCAM natural gas sectors identified 
above were adjusted by a factor of 8. 63/8.53, or 1.0117 (a 1.17% increase) to maintain 
consistency with past NETL studies of the natural gas sector. This adjustment factor was used for 
all regions and for all years in the model, and is directly applied to GHG emissions in all regions 
of the GCAM model results for the natural gas and gas pipeline sectors as they wholly related to 
natural gas activities. By linearly scaling all regional values in this way, the existing and diverse

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-57 
CH4 mitigation trends for each region in the underlying GCAM emissions factors for the natural 
gas sector were preserved by using this adjustment method. 
For the other industrial energy use sector, the adjustment is complicated by the fact that the sector 
includes many activities beyond those associated with natural gas, such as use of biomass and 
coal. If the adjustment factor were wholly applied to the GHG emissions of the sector, then the  
total emissions in GCAM would be reduced for both natural gas and non-natural gas activities. A 
compromise was made to estimate the total needed reductions in emissions associated with only 
natural gas activity for each region, and to reduce the emissions of the other industrial energy use 
sector by that amount. While this does not achieve a full alignment of these associated emissions 
(i.e., it does not lead to a 1.17% increase in emissions intensity for the sector), it avoids the 
outcome where that sector’s emissions are reduced for all of the other activities. Specifically, as 
delineated above only the emissions of the gas/gas cogen and refined liquids/refined liquids 
cogen subsectors were increased by 1.17%, and only for the share of activity within tho se 
subsectors associated with Extraction and Gathering/Boosting activities.  
These adjustments to emissions from all regions, all scenarios, and all years were applied to 
existing GCAM results (i.e., GCAM was not re -run based on these adjustments). As 99.5% of 
GHG emissions in the other industrial energy use sector are CO 2, only CO 2 emissions for that 
sector were adjusted. The net global adjustment of GHG emissions in this sector (an increase of 
0.11% in 2020) has negligible effects on GHG emissions. 
Table C -2.4 shows the GWP of GHG emissions estimates from GCAM that were used in 
conjunction with the emissions factors to derive the overall life cycle GHG intensity values. 
Table C-2.4. GWP values used in this analysis 
GHG AR6, 100-yr AR6, 20-yr 
CH4 (fossil) 29.8 82.5 
CH4 (non-fossil) 27.2 80.8 
N2O (fossil) 273 273 
N2O (non-fossil) 273 273 
HFC125 3740 6740 
HFC134a 1530 4140 
HFC143a 5810 7840 
HFC23 14600 12400 
HFC32 771 2690 
SF6 24300 18200 
HFC245fa 962 3170 
HFC365mfc 914 2920 
C2F6 12400 8940 
CF4 7380 5300 
HFC43 1600 3960 
HFC152a 164 591 
HFC227ea 3600 5850 
HFC236fa 8690 7450

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-58 
Note that unlike the natural gas system -specific emission comparisons and adjustments 
discussed above, which focus on CO 2, CH4, and N 2O, GCAM estimates emissions of 16 GHGs 
and all are included in this study.  
Using the same detailed approach as detailed in Table C-2.3, Table C-2.5 more succinctly 
summarizes the provided GCAM values and adjustments identified for the IPCC AR6, 20-yr 
values. 
Table C-2.5. GCAM emissions intensities for sectors (S1, 2020, U.S. region, AR6, 20-yr basis) 
GCAM Sector 
Estimated GCAM Emissions Intensity 
(Tg CO2e/EJ, g CO2e/MJ) [IPCC AR6, 20-
yr] 
CO2 CH4 N2O 
gas pipeline 1.18 - - 
natural gas - 11.86 4.5 E-4 
other industrial energy use (technology = gas or gas 
cogen) 2.88 0.005 0.001 
other industrial energy use (technology = refined liquids 
and refined liquids cogen) 0.2 0.006 0.007 
Total GCAM by gas (LHV) = 1.18 + 2.88 + .2 = 4.24 11.87 0.009 
Total GCAM (LHV) 16.1 
NETL (LHV basis) 14.6 
Adjustment Factor (LHV) 0.907 
In addition to the adjustment of GCAM results, the liquefaction and upstream natural gas GHG 
intensity values produced in Steps 2 and 3 were also updated to the AR6, 20-yr basis. The 
resulting values are 15.7 g CO2e/MJ and 5.6 g CO2e/MJ for the for the upstream natural gas GHG 
intensity and liquefaction GHG intensity, respectively. The sum of these is 21.3 g CO2e/MJ and is 
the estimate of project direct emissions for analysis on an AR6, 20-yr basis. 
B. Method and Scaling Factors Used for Service-Equivalent Analysis 
An additional analysis was done from the base set of scenarios that estimated results with 
increased services provided. The additional analysis normalized services delivered on an 
equivalent basis, as described in this section. 
An output file from GCAM provided aggregated summaries of domestic and global services 
provided from GCAM, which include end -use energy services (e.g., space heating and cooling, 
passenger and freight transportation, industrial energy) and output of some m ajor commodities 
(e.g., cement). Originally provided estimates of about 50 services are aggregated into about 15 
categories. 
A method was derived to compare and normalize the greenhouse gas emissions and U.S. LNG 
exports based on the changes in services provided between scenarios across the entire set of 
services provided. 
The “outputs” data is an export of GCAM modeling that shows the quantities of outputs for various 
services. These account for energy services that can be quantified using appropriate exajoule 
units, material production (e.g., cement and iron/steel) that ar e more appropriately quantified by 
mass, and transportation that can be for materials or people with appropriate units. For any 
scenario pair where the end, cumulative result is an increase in U.S. LNG exports, these 
cumulative global services increase by different amounts along with their GHG emissions. In order 
to compare the carbon intensity of two scenarios, the GHG emissions and U.S. LNG exports need

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-59 
to be adjusted to account for those changes in services. This is done by calculating a ratio of the 
service between two scenarios – for example scenario 1 cement production in million tonnes 
divided scenario 2 cement production in million tons. This is don e for all services, resulting in a 
vector of multiple (50 into 15) ratios. These ratios are weighted by the amount of energy input for 
that service, and then summed together to provide a single weighting factor to apply to the both 
the global GHG emissions and U.S. LNG production. 
In general, when adjusting scenarios to reach service-equivalence, the GHG intensity per unit of 
U.S. LNG is negative, suggesting that the global GHG intensity of services in general slightly 
decreases as a result of U.S. LNG exports. This is largely due t o removals of enough coal, oil, 
and more GHG -intense natural gas from energy use globally to offset the reductions in any 
renewable energy use that also occur. As a result, weighted average scaling factors for the 
service-equivalent analysis were developed  for all scenarios relative overall to the Defined 
Policies: Existing/FID Exports  scenario and within each set of scenarios to the specific ExFID 
scenario, as shown in Table C-2.6. 
Table C-2.6. Scaling factors used for service adjustment calculation relative to the existing/fid  
levels of LNG export 
Scenario Service Adjustment Scaling Factor 
Defined Policies: High Exports 1.001476 
Defined Policies: Model Resolved 1.00079 
Defined Policies: Existing/FID Exports 1 
Defined Policies: High Middle East Supply: Model Resolved 1.000467 
Defined Policies: High Middle East Supply: Existing/FID Exports 1 
Defined Policies: High US Supply: Model Resolved 1.001265 
Defined Policies: High US Supply: Existing/FID Exports 1 
Defined Policies: Low US Supply: Model Resolved 1.000098 
Defined Policies: Low US Supply: Existing/FID Exports 1 
Commitments (High CCS): High Exports 1.00092 
Commitments (High CCS): Model Resolved 1.000199 
Commitments (High CCS): Existing/FID Exports 1 
Commitments (Mod CCS): High Exports 1.000755 
Commitments (Mod CCS): Model Resolved 1.000058 
Commitments (Mod CCS): Existing/FID Exports 1 
Net Zero 2050 (High CCS): High Exports 1.000759 
Net Zero 2050 (High CCS): Model Resolved 1.000089 
Net Zero 2050 (High CCS): Existing/FID Exports 1 
Net Zero 2050 (Mod CCS): High Exports 1.000464 
Net Zero 2050 (Mod CCS): Model Resolved 1 
Net Zero 2050 (Mod CCS): Existing/FID Exports 1

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-60 
APPENDIX C-3: SOCIAL COST OF GREENHOUSE GASES MODELING AND 
ADDITIONAL RESULTS 
The speciated GHG emissions inputs to the consequential GHG intensity can also be used with 
the 2023 SC -GHG methodology to monetize the impacts of the changes in GHG emissions 
associated with increased U.S. LNG exports. The social cost of greenhouse gases (SC-GHG), as 
described by the Interagency Working Group (IWG) on SC -GHG, is “the monetary value of the 
net harm to society associated with adding a small amount of greenhouse gases to the 
atmosphere in a given year.” In short, the SC-GHG monetizes the net harm to society caused by 
the release of an additional ton of GHGs into the atmosphere in a given year.  
The 2023 SC -GHG method uses a trio of constant discount rates (1.5%, 2.0% and 2.5%) to 
provide estimate the SC-GHG for a particular base year (assumed in this study as 2024) and 
dollar year. The base year (which can also be considered the present value year) was chosen to 
be 2024 to align with the time of the study, consistent with the suggested choice alig ning with a 
regulatory impact assessment time. The study used 2020 and 2022 as the dollar year, consistent 
with the default year of damages provided in the framework43. The SC-GHG for a given quantity 
of emissions estimate the net social benefits in dollar values of reducing those emissions, or the 
net social costs of increasing emissions by that quantity. It also provides a common metric (social 
costs, in dollars) for identifying the effects of changes in inputs or assumptions on the final result. 
Using the 2023 SC-GHG guidance and analysis documents in this study requires only the input 
of annual speciated GHG emissions of carbon dioxide, methane, and nitrous oxide, which came 
from the NETL-aligned GCAM results. Table C-3.1 summarizes the monetized SC-GHG estimates 
in the 2023 SC -GHG method used in the study in 2020 dollars per metric ton of emissions by 
species, which are defined as having been set using near -term Ramsey discount rates. A GDP 
deflator is used to convert these values as needed for the 2022-dollar year basis. 
Table C -3.1. Annual Unrounded Values in 2023 SC -GHG Estimates, 2020 -2080 (2020$ per 
metric ton of emissions) 
Gas CO2 CO2 CO2 CH4 CH4 CH4 N2O N2O N2O 
Near-term 
Ramsey 
Discount 
Rate 
2.50% 2.00% 1.50% 2.50% 2.00% 1.50% 2.50% 2.00% 1.50% 
2020 117 193 337 1,257 1,648 2,305 35,232 54,139 87,284 
2021 119 197 341 1,324 1,723 2,391 36,180 55,364 88,869 
2022 122 200 346 1,390 1,799 2,478 37,128 56,590 90,454 
2023 125 204 351 1,457 1,874 2,564 38,076 57,816 92,040 
2024 128 208 356 1,524 1,950 2,650 39,024 59,041 93,625 
2025 130 212 360 1,590 2,025 2,737 39,972 60,267 95,210 
2026 133 215 365 1,657 2,101 2,823 40,920 61,492 96,796 
2027 136 219 370 1,724 2,176 2,910 41,868 62,718 98,381 
2028 139 223 375 1,791 2,252 2,996 42,816 63,944 99,966 
2029 141 226 380 1,857 2,327 3,083 43,764 65,169 101,552 
2030 144 230 384 1,924 2,403 3,169 44,712 66,395 103,137 
 
43 Generally, this Appendix refers to 2020-dollar year results, while the Summary report refers to 2022 dollar 
year results.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-61 
2031 147 234 389 2,002 2,490 3,270 45,693 67,645 104,727 
2032 150 237 394 2,080 2,578 3,371 46,674 68,895 106,316 
2033 153 241 398 2,157 2,666 3,471 47,655 70,145 107,906 
2034 155 245 403 2,235 2,754 3,572 48,636 71,394 109,495 
2035 158 248 408 2,313 2,842 3,673 49,617 72,644 111,085 
2036 161 252 412 2,391 2,929 3,774 50,598 73,894 112,674 
2037 164 256 417 2,468 3,017 3,875 51,578 75,144 114,264 
2038 167 259 422 2,546 3,105 3,975 52,559 76,394 115,853 
2039 170 263 426 2,624 3,193 4,076 53,540 77,644 117,443 
2040 173 267 431 2,702 3,280 4,177 54,521 78,894 119,032 
2041 176 271 436 2,786 3,375 4,285 55,632 80,304 120,809 
2042 179 275 441 2,871 3,471 4,394 56,744 81,714 122,586 
2043 182 279 446 2,955 3,566 4,502 57,855 83,124 124,362 
2044 186 283 451 3,040 3,661 4,610 58,966 84,535 126,139 
2045 189 287 456 3,124 3,756 4,718 60,078 85,945 127,916 
2046 192 291 462 3,209 3,851 4,827 61,189 87,355 129,693 
2047 195 296 467 3,293 3,946 4,935 62,301 88,765 131,469 
2048 199 300 472 3,378 4,041 5,043 63,412 90,176 133,246 
2049 202 304 477 3,462 4,136 5,151 64,523 91,586 135,023 
2050 205 308 482 3,547 4,231 5,260 65,635 92,996 136,799 
Results from the SC-GHG analyses for the 2020-dollar year basis are summarized in Table C-3.2 
through Table C-3.4. Note that unlike the consequential intensity and project non-direct emissions 
results shown earlier, these social costs of greenhouse gases are those associated with all global 
emissions over the 2020-2050 period for the scenarios, and not just those associated with U.S. 
LNG exports. 
Table C-3.2. Social cost of greenhouse gases results for Defined Policies (base year 2024, trillion 
2020$) 
    Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Defined Policies: High 
Exports 
CO2 $129.06 $213.68 $370.63 
CH4 $19.39 $25.34 $34.86 
N2O $14.31 $22.18 $35.93 
Total $162.76 $261.20 $441.42 
Defined Policies: Model 
Resolved 
CO2 $128.98 $213.54 $370.40 
CH4 $19.38 $25.34 $34.85 
N2O $14.31 $22.19 $35.94 
Total $162.68 $261.07 $441.19 
Defined Policies: 
Existing/FID Exports 
CO2 $128.90 $213.41 $370.16 
CH4 $19.38 $25.33 $34.85 
N2O $14.32 $22.20 $35.96 
Total $162.60 $260.95 $440.97

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-62 
Defined Policies: High 
Middle East Supply: Model 
Resolved 
CO2 $129.36 $214.19 $371.52 
CH4 $19.44 $25.41 $34.96 
N2O $14.30 $22.17 $35.90 
Total $163.11 $261.77 $442.39 
Defined Policies: High 
Middle East Supply: 
Existing/FID Exports 
CO2 $129.31 $214.10 $371.38 
CH4 $19.45 $25.42 $34.97 
N2O $14.30 $22.17 $35.91 
Total $163.06 $261.70 $442.26 
          
Defined Policies: High US 
Supply: Model Resolved 
CO2 $129.07 $213.69 $370.66 
CH4 $19.39 $25.34 $34.86 
N2O $14.31 $22.19 $35.93 
Total $162.77 $261.22 $441.45 
Defined Policies: High US 
Supply: Existing/FID 
Exports 
CO2 $128.94 $213.48 $370.28 
CH4 $19.39 $25.34 $34.86 
N2O $14.32 $22.20 $35.96 
Total $162.65 $261.01 $441.09 
          
Defined Policies: Low US 
Supply: Model Resolved 
CO2 $128.63 $212.95 $369.36 
CH4 $19.37 $25.32 $34.83 
N2O $14.32 $22.20 $35.95 
Total $162.32 $260.47 $440.14 
Defined Policies: Low US 
Supply: Existing/FID 
Exports 
CO2 $128.62 $212.94 $369.35 
CH4 $19.37 $25.32 $34.83 
N2O $14.32 $22.20 $35.95 
Total $162.31 $260.46 $440.13 
Table C-3.3. Social cost of greenhouse gases results for Commitments (base year 2024, trillion 
2020$) 
  Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Commitments (High CCS): 
High Exports 
CO2 $100.51 $165.67 $286.26 
CH4 $17.98 $23.47 $32.26 
N2O $13.68 $21.19 $34.29 
Total $132.16 $210.33 $352.81 
Commitments (High CCS): 
Model Resolved 
CO2 $100.43 $165.53 $286.02 
CH4 $17.98 $23.47 $32.27 
N2O $13.68 $21.19 $34.30 
Total $132.09 $210.20 $352.58 
Commitments (High CCS): 
Existing/FID Exports 
CO2 $100.41 $165.51 $285.97 
CH4 $17.98 $23.48 $32.27 
N2O $13.68 $21.19 $34.30 
Total $132.07 $210.17 $352.54 
          
CO2 $95.51 $157.29 $271.59

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-63 
Commitments (Mod CCS): 
High Exports 
CH4 $17.14 $22.37 $30.74 
N2O $13.29 $20.58 $33.30 
Total $125.94 $200.24 $335.64 
Commitments (Mod CCS): 
Model Resolved 
CO2 $95.39 $157.10 $271.25 
CH4 $17.14 $22.37 $30.75 
N2O $13.29 $20.58 $33.30 
Total $125.82 $200.05 $335.30 
Commitments (Mod CCS): 
Existing/FID Exports 
CO2 $95.38 $157.08 $271.22 
CH4 $17.14 $22.37 $30.75 
N2O $13.29 $20.58 $33.30 
Total $125.82 $200.04 $335.28 
Table C-3.4. Social cost of greenhouse gases results for Net Zero 2050 (base year 2024, trillion 
2020$) 
  Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Net Zero 2050 (High CCS): 
High Exports 
CO2 $79.78 $131.11 $225.96 
CH4 $17.06 $22.26 $30.60 
N2O $13.30 $20.60 $33.33 
Total $110.14 $173.97 $289.90 
Net Zero 2050 (High CCS): 
Model Resolved 
CO2 $79.75 $131.04 $225.85 
CH4 $17.06 $22.27 $30.61 
N2O $13.30 $20.60 $33.34 
Total $110.11 $173.91 $289.79 
Net Zero 2050 (High CCS): 
Existing/FID Exports 
CO2 $79.74 $131.03 $225.83 
CH4 $17.06 $22.27 $30.61 
N2O $13.30 $20.60 $33.34 
Total $110.11 $173.91 $289.78 
          
Net Zero 2050 (Mod CCS): 
High Exports 
CO2 $72.93 $119.68 $206.02 
CH4 $16.01 $20.89 $28.70 
N2O $12.80 $19.82 $32.06 
Total $101.74 $160.38 $266.78 
Net Zero 2050 (Mod CCS): 
Model Resolved 
CO2 $72.82 $119.48 $205.68 
CH4 $16.01 $20.89 $28.71 
N2O $12.80 $19.82 $32.06 
Total $101.63 $160.19 $266.45 
Net Zero 2050 (Mod CCS): 
Existing/FID Exports 
CO2 $72.82 $119.48 $205.68 
CH4 $16.01 $20.89 $28.71 
N2O $12.80 $19.82 $32.06 
Total $101.63 $160.19 $266.45

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-64 
Similarly, Table C-3.5 through Table C-3.7 show SC-GHG results for all scenarios for the 2022-
dollar year basis. 
Table C-3.5. Social cost of greenhouse gases results for Defined Policies (base year 2024, trillion 
2022$) 
  Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Defined Policies: High 
Exports 
CO2 $144.48 $239.21 $414.92 
CH4 $21.71 $28.37 $39.03 
N2O $16.02 $24.83 $40.22 
Total $182.20 $292.41 $494.16 
Defined Policies: Model 
Resolved 
CO2 $144.39 $239.06 $414.66 
CH4 $21.70 $28.36 $39.02 
N2O $16.02 $24.84 $40.23 
Total $182.12 $292.27 $493.91 
Defined Policies: 
Existing/FID Exports 
CO2 $144.30 $238.91 $414.39 
CH4 $21.70 $28.36 $39.02 
N2O $16.03 $24.85 $40.25 
Total $182.03 $292.13 $493.66 
          
Defined Policies: High 
Middle East Supply: Model 
Resolved 
CO2 $144.82 $239.78 $415.92 
CH4 $21.77 $28.45 $39.14 
N2O $16.01 $24.82 $40.19 
Total $182.60 $293.05 $495.25 
Defined Policies: High 
Middle East Supply: 
Existing/FID Exports 
CO2 $144.77 $239.69 $415.75 
CH4 $21.77 $28.46 $39.15 
N2O $16.01 $24.82 $40.20 
Total $182.55 $292.97 $495.10 
          
Defined Policies: High US 
Supply: Model Resolved 
CO2 $144.49 $239.23 $414.95 
CH4 $21.71 $28.37 $39.03 
N2O $16.02 $24.84 $40.23 
Total $182.22 $292.43 $494.20 
Defined Policies: High US 
Supply: Existing/FID 
Exports 
CO2 $144.35 $238.98 $414.52 
CH4 $21.70 $28.36 $39.02 
N2O $16.03 $24.85 $40.25 
Total $182.08 $292.20 $493.79 
          
Defined Policies: Low US 
Supply: Model Resolved 
CO2 $144.00 $238.40 $413.49 
CH4 $21.69 $28.34 $38.99 
N2O $16.03 $24.85 $40.25 
Total $181.71 $291.59 $492.73 
Defined Policies: Low US 
Supply: Existing/FID 
Exports 
CO2 $143.99 $238.39 $413.48 
CH4 $21.69 $28.34 $38.99 
N2O $16.03 $24.85 $40.25 
Total $181.71 $291.59 $492.72

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-65 
 
Table C-3.6. Social cost of greenhouse gases results for Commitments (base year 2024, trillion 
2022$) 
  Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Commitments (High CCS): 
High Exports 
CO2 $112.52 $185.47 $320.47 
CH4 $20.12 $26.27 $36.12 
N2O $15.31 $23.72 $38.39 
Total $147.96 $235.46 $394.97 
Commitments (High CCS): 
Model Resolved 
CO2 $112.43 $185.31 $320.19 
CH4 $20.13 $26.28 $36.12 
N2O $15.31 $23.72 $38.39 
Total $147.87 $235.31 $394.71 
Commitments (High CCS): 
Existing/FID Exports 
CO2 $112.41 $185.28 $320.14 
CH4 $20.13 $26.28 $36.13 
N2O $15.31 $23.72 $38.40 
Total $147.86 $235.29 $394.67 
          
Commitments (Mod CCS): 
High Exports 
CO2 $106.92 $176.09 $304.04 
CH4 $19.19 $25.04 $34.42 
N2O $14.88 $23.04 $37.28 
Total $140.99 $224.17 $375.74 
Commitments (Mod CCS): 
Model Resolved 
CO2 $106.79 $175.87 $303.66 
CH4 $19.19 $25.04 $34.42 
N2O $14.88 $23.04 $37.28 
Total $140.86 $223.96 $375.37 
Commitments (Mod CCS): 
Existing/FID Exports 
CO2 $106.78 $175.85 $303.63 
CH4 $19.19 $25.05 $34.42 
N2O $14.88 $23.04 $37.28 
Total $140.85 $223.94 $375.34 
 
Table C-3.7. Social cost of greenhouse gases results for Net Zero 2050 (base year 2024, trillion 
2022$) 
  Discount Rate 
Scenario Gas 2.50% 2.00% 1.50% 
Net Zero 2050 (High CCS): 
High Exports 
CO2 $89.32 $146.77 $252.96 
CH4 $19.09 $24.92 $34.26 
N2O $14.89 $23.06 $37.32 
Total $123.30 $194.76 $324.54 
Net Zero 2050 (High CCS): 
Model Resolved 
CO2 $89.27 $146.70 $252.83 
CH4 $19.10 $24.93 $34.27 
N2O $14.89 $23.07 $37.32 
Total $123.27 $194.69 $324.42 
CO2 $89.27 $146.69 $252.81

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
 C-66 
Net Zero 2050 (High CCS): 
Existing/FID Exports 
CH4 $19.10 $24.93 $34.27 
N2O $14.89 $23.07 $37.32 
Total $123.26 $194.69 $324.41 
          
Net Zero 2050 (Mod CCS): 
High Exports 
CO2 $81.65 $133.98 $230.63 
CH4 $17.92 $23.38 $32.13 
N2O $14.33 $22.19 $35.89 
Total $113.90 $179.54 $298.65 
Net Zero 2050 (Mod CCS): 
Model Resolved 
CO2 $81.52 $133.76 $230.25 
CH4 $17.92 $23.39 $32.14 
N2O $14.33 $22.19 $35.89 
Total $113.77 $179.34 $298.29 
Net Zero 2050 (Mod CCS): 
Existing/FID Exports 
CO2 $81.52 $133.76 $230.25 
CH4 $17.92 $23.39 $32.14 
N2O $14.33 $22.19 $35.89 
Total $113.77 $179.34 $298.29

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-67 
APPENDIX C-4: DETAILED DATA TABLES FOR VALUES SUMMARIZED IN THIS 
REPORT 
 
The first set of tables provided in this Appendix are archives of the speciated GHG emissions data 
for all scenarios used in the analysis, representing the GCAM-NETL-aligned values described in 
the Consequential Appendix. Values are provided on both AR6-100 and AR6-20 basis. 
 
The second set of tables provided in this Appendix summarize annual and cumulative values of 
GHG emissions, U.S. LNG exports, and the consequential GHG intensity and project non -direct 
emissions, for all scenarios.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-68 
Table C-4.1. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 100-year) 
2020 38,407 398 6,677 3,929 887 2,123 1,349 53,770 
2021 37,946 469 6,461 3,946 877 2,151 1,370 53,219 
2022 37,484 540 6,245 3,964 867 2,179 1,390 52,669 
2023 37,022 611 6,029 3,981 857 2,206 1,410 52,118 
2024 36,561 683 5,813 3,999 847 2,234 1,431 51,567 
2025 36,099 754 5,598 4,016 837 2,262 1,451 51,017 
2026 36,202 67 5,637 4,081 845 2,294 1,518 50,645 
2027 36,305 -619 5,677 4,145 853 2,326 1,586 50,273 
2028 36,409 -1,306 5,716 4,210 860 2,358 1,653 49,901 
2029 36,512 -1,992 5,755 4,274 868 2,390 1,721 49,529 
2030 36,615 -2,679 5,795 4,339 876 2,423 1,788 49,156 
2031 36,441 -2,389 5,791 4,399 869 2,448 1,806 49,364 
2032 36,268 -2,100 5,786 4,460 863 2,472 1,823 49,572 
2033 36,094 -1,811 5,782 4,520 857 2,497 1,840 49,779 
2034 35,921 -1,522 5,777 4,580 851 2,522 1,857 49,987 
2035 35,748 -1,233 5,773 4,640 844 2,547 1,874 50,194 
2036 35,582 -1,252 5,737 4,694 833 2,571 1,868 50,033 
2037 35,415 -1,271 5,702 4,747 822 2,595 1,861 49,872 
2038 35,249 -1,290 5,666 4,800 812 2,619 1,855 49,711 
2039 35,083 -1,309 5,631 4,853 801 2,643 1,848 49,549 
2040 34,917 -1,328 5,595 4,906 790 2,667 1,841 49,388 
2041 34,745 -1,261 5,602 4,962 791 2,698 1,827 49,364 
2042 34,574 -1,194 5,608 5,017 792 2,730 1,812 49,340 
2043 34,402 -1,127 5,615 5,073 793 2,761 1,797 49,315 
2044 34,230 -1,059 5,621 5,129 794 2,793 1,783 49,291 
2045 34,058 -992 5,628 5,185 796 2,824 1,768 49,267 
2046 33,829 -969 5,630 5,235 796 2,855 1,764 49,141 
2047 33,600 -945 5,633 5,286 797 2,885 1,759 49,016 
2048 33,370 -922 5,636 5,337 798 2,916 1,755 48,890 
2049 33,141 -898 5,638 5,388 798 2,946 1,751 48,765 
2050 32,912 -874 5,641 5,439 799 2,977 1,746 48,639 
Total 1,101,142 -28,818 178,895 143,533 25,770 78,914 52,903 1,552,340 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-69 
Table C-4.2. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 398 6,677 3,929 887 2,123 1,349 53,770 
2021 37,946 469 6,461 3,946 877 2,151 1,370 53,219 
2022 37,484 540 6,245 3,964 867 2,179 1,390 52,669 
2023 37,022 611 6,029 3,981 857 2,206 1,410 52,118 
2024 36,561 683 5,813 3,999 847 2,234 1,431 51,567 
2025 36,099 754 5,598 4,016 837 2,262 1,451 51,017 
2026 36,202 67 5,637 4,081 845 2,294 1,518 50,645 
2027 36,305 -619 5,677 4,145 853 2,326 1,586 50,273 
2028 36,409 -1,306 5,716 4,210 860 2,358 1,653 49,901 
2029 36,512 -1,992 5,755 4,274 868 2,390 1,721 49,529 
2030 36,615 -2,679 5,795 4,339 876 2,423 1,788 49,156 
2031 36,449 -2,397 5,791 4,399 869 2,447 1,806 49,365 
2032 36,282 -2,115 5,788 4,460 863 2,472 1,823 49,573 
2033 36,116 -1,833 5,784 4,520 857 2,497 1,840 49,781 
2034 35,950 -1,551 5,780 4,580 850 2,522 1,858 49,989 
2035 35,783 -1,269 5,777 4,640 844 2,546 1,875 50,197 
2036 35,631 -1,293 5,742 4,694 833 2,570 1,869 50,046 
2037 35,479 -1,317 5,707 4,747 822 2,594 1,863 49,894 
2038 35,327 -1,341 5,672 4,800 811 2,618 1,856 49,743 
2039 35,175 -1,364 5,637 4,853 800 2,641 1,850 49,592 
2040 35,023 -1,388 5,602 4,906 789 2,665 1,844 49,440 
2041 34,849 -1,315 5,607 4,962 790 2,696 1,829 49,418 
2042 34,674 -1,241 5,612 5,017 791 2,728 1,814 49,396 
2043 34,500 -1,167 5,617 5,073 792 2,759 1,800 49,374 
2044 34,325 -1,093 5,621 5,129 794 2,791 1,785 49,352 
2045 34,151 -1,020 5,626 5,185 795 2,822 1,770 49,329 
2046 33,913 -990 5,627 5,235 795 2,853 1,766 49,200 
2047 33,675 -960 5,628 5,286 796 2,883 1,761 49,070 
2048 33,437 -930 5,629 5,337 797 2,914 1,757 48,940 
2049 33,198 -900 5,630 5,388 797 2,944 1,752 48,810 
2050 32,960 -871 5,631 5,439 798 2,975 1,748 48,680 
Total 1,102,460 -29,427 178,912 143,533 25,756 78,881 52,936 1,553,051 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-70 
Table C -4.3. Global Emissions Summary for Defined Policies: High Exports (GCAM -NETL-
Aligned, AR6-100 Basis) 
Year 
CO2 
Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 398 6,677 3,929 887 2,123 1,349 53,770 
2021 37,946 469 6,461 3,946 877 2,151 1,370 53,219 
2022 37,484 540 6,245 3,964 867 2,179 1,390 52,669 
2023 37,022 611 6,029 3,981 857 2,206 1,410 52,118 
2024 36,561 683 5,813 3,999 847 2,234 1,431 51,567 
2025 36,099 754 5,598 4,016 837 2,262 1,451 51,017 
2026 36,202 67 5,637 4,081 845 2,294 1,518 50,645 
2027 36,305 -619 5,677 4,145 853 2,326 1,586 50,273 
2028 36,409 -1,306 5,716 4,210 860 2,358 1,653 49,901 
2029 36,512 -1,992 5,755 4,274 868 2,390 1,721 49,529 
2030 36,615 -2,679 5,795 4,339 876 2,423 1,788 49,156 
2031 36,462 -2,410 5,792 4,399 869 2,447 1,806 49,365 
2032 36,309 -2,142 5,790 4,460 863 2,472 1,824 49,574 
2033 36,156 -1,873 5,788 4,520 856 2,496 1,841 49,783 
2034 36,003 -1,605 5,785 4,580 850 2,520 1,859 49,992 
2035 35,850 -1,337 5,783 4,640 843 2,545 1,876 50,201 
2036 35,699 -1,349 5,748 4,694 832 2,569 1,870 50,062 
2037 35,549 -1,362 5,713 4,747 821 2,592 1,864 49,924 
2038 35,398 -1,375 5,678 4,800 810 2,616 1,858 49,785 
2039 35,248 -1,388 5,643 4,853 799 2,640 1,852 49,647 
2040 35,097 -1,400 5,608 4,906 788 2,663 1,846 49,508 
2041 34,921 -1,326 5,612 4,962 789 2,695 1,831 49,483 
2042 34,745 -1,252 5,616 5,017 791 2,726 1,816 49,458 
2043 34,568 -1,179 5,620 5,073 792 2,758 1,801 49,433 
2044 34,392 -1,105 5,624 5,129 793 2,789 1,787 49,409 
2045 34,215 -1,031 5,628 5,185 794 2,820 1,772 49,384 
2046 33,972 -999 5,628 5,235 795 2,851 1,767 49,250 
2047 33,730 -967 5,629 5,286 795 2,881 1,763 49,117 
2048 33,487 -935 5,629 5,337 796 2,912 1,758 48,984 
2049 33,244 -903 5,629 5,388 796 2,942 1,754 48,851 
2050 33,001 -872 5,629 5,439 797 2,973 1,749 48,717 
Total 1,103,609 -29,883 178,974 143,533 25,744 78,852 52,963 1,553,792 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-71 
Table C -4.4. Global Emissions Summary for Defined Policies: High Middle East Supply: 
Existing/FID Exports (GCAM_NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,416 397 6,678 3,929 887 2,123 1,350 53,780 
2021 37,955 468 6,462 3,946 877 2,151 1,370 53,230 
2022 37,495 540 6,247 3,964 867 2,179 1,390 52,681 
2023 37,035 611 6,031 3,981 857 2,206 1,411 52,131 
2024 36,574 682 5,815 3,999 847 2,234 1,431 51,582 
2025 36,114 753 5,599 4,016 837 2,262 1,451 51,032 
2026 36,227 56 5,640 4,081 845 2,294 1,519 50,662 
2027 36,340 -640 5,681 4,145 853 2,326 1,586 50,291 
2028 36,454 -1,336 5,722 4,210 860 2,358 1,654 49,921 
2029 36,567 -2,033 5,763 4,274 868 2,390 1,722 49,551 
2030 36,680 -2,729 5,804 4,339 875 2,422 1,789 49,180 
2031 36,529 -2,452 5,803 4,399 869 2,446 1,807 49,401 
2032 36,378 -2,175 5,803 4,460 863 2,471 1,825 49,623 
2033 36,227 -1,898 5,802 4,520 856 2,495 1,842 49,844 
2034 36,075 -1,621 5,802 4,580 850 2,520 1,860 50,065 
2035 35,924 -1,345 5,801 4,640 843 2,544 1,878 50,286 
2036 35,786 -1,363 5,771 4,694 832 2,568 1,872 50,158 
2037 35,647 -1,382 5,740 4,747 821 2,591 1,866 50,030 
2038 35,509 -1,400 5,710 4,800 810 2,615 1,860 49,903 
2039 35,370 -1,419 5,680 4,853 799 2,638 1,854 49,775 
2040 35,232 -1,438 5,650 4,906 788 2,662 1,848 49,647 
2041 35,073 -1,374 5,659 4,962 789 2,693 1,833 49,635 
2042 34,915 -1,311 5,668 5,017 790 2,724 1,818 49,623 
2043 34,757 -1,248 5,678 5,073 792 2,755 1,804 49,610 
2044 34,598 -1,184 5,687 5,129 793 2,786 1,789 49,598 
2045 34,440 -1,121 5,696 5,185 794 2,817 1,775 49,586 
2046 34,218 -1,100 5,702 5,236 794 2,847 1,771 49,468 
2047 33,997 -1,078 5,707 5,286 795 2,877 1,766 49,350 
2048 33,775 -1,057 5,712 5,337 796 2,907 1,762 49,232 
2049 33,553 -1,035 5,717 5,388 796 2,937 1,758 49,114 
2050 33,331 -1,014 5,722 5,439 797 2,967 1,753 48,996 
Total 1,107,190 -31,246 179,951 143,534 25,741 78,803 53,012 1,556,984 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-72 
Table C-4.5. Global Emissions Summary for Defined Policies: High Middle East Supply: Model 
Resolved (GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,416 397 6,678 3,929 887 2,123 1,350 53,780 
2021 37,955 468 6,462 3,946 877 2,151 1,370 53,230 
2022 37,495 540 6,247 3,964 867 2,179 1,390 52,681 
2023 37,035 611 6,031 3,981 857 2,206 1,411 52,131 
2024 36,574 682 5,815 3,999 847 2,234 1,431 51,582 
2025 36,114 753 5,599 4,016 837 2,262 1,451 51,032 
2026 36,227 56 5,640 4,081 845 2,294 1,519 50,662 
2027 36,340 -640 5,681 4,145 853 2,326 1,586 50,291 
2028 36,454 -1,336 5,722 4,210 860 2,358 1,654 49,921 
2029 36,567 -2,033 5,763 4,274 868 2,390 1,722 49,551 
2030 36,680 -2,729 5,804 4,339 875 2,422 1,789 49,180 
2031 36,535 -2,458 5,804 4,399 869 2,446 1,807 49,402 
2032 36,389 -2,186 5,803 4,460 862 2,470 1,825 49,624 
2033 36,243 -1,915 5,803 4,520 856 2,495 1,843 49,845 
2034 36,098 -1,643 5,803 4,580 850 2,519 1,861 50,067 
2035 35,952 -1,372 5,803 4,640 843 2,543 1,878 50,288 
2036 35,819 -1,390 5,772 4,694 832 2,567 1,872 50,166 
2037 35,686 -1,408 5,741 4,747 821 2,590 1,867 50,044 
2038 35,553 -1,426 5,710 4,800 810 2,614 1,861 49,922 
2039 35,420 -1,444 5,680 4,853 799 2,637 1,855 49,799 
2040 35,287 -1,462 5,649 4,906 788 2,661 1,849 49,677 
2041 35,126 -1,394 5,657 4,962 789 2,692 1,834 49,666 
2042 34,966 -1,327 5,665 5,017 790 2,723 1,820 49,654 
2043 34,806 -1,259 5,673 5,073 791 2,754 1,805 49,643 
2044 34,645 -1,192 5,681 5,129 792 2,785 1,791 49,632 
2045 34,485 -1,124 5,689 5,185 793 2,816 1,776 49,620 
2046 34,260 -1,103 5,693 5,236 794 2,846 1,772 49,497 
2047 34,035 -1,082 5,697 5,286 795 2,876 1,767 49,375 
2048 33,810 -1,061 5,701 5,337 795 2,906 1,763 49,252 
2049 33,585 -1,040 5,706 5,388 796 2,936 1,759 49,129 
2050 33,360 -1,019 5,710 5,439 797 2,966 1,754 49,006 
Total 1,107,917 -31,537 179,882 143,534 25,734 78,785 53,032 1,557,347 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-73 
Table C-4.6. Global Emissions Summary for Defined Policies: High U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,403 398 6,677 3,929 887 2,123 1,349 53,766 
2021 37,943 469 6,461 3,946 877 2,151 1,370 53,216 
2022 37,483 539 6,245 3,964 867 2,179 1,390 52,667 
2023 37,023 610 6,029 3,981 857 2,206 1,410 52,117 
2024 36,563 681 5,814 3,999 847 2,234 1,431 51,568 
2025 36,103 751 5,598 4,016 837 2,262 1,451 51,019 
2026 36,207 64 5,637 4,081 845 2,294 1,519 50,647 
2027 36,312 -623 5,677 4,145 853 2,326 1,586 50,276 
2028 36,416 -1,310 5,717 4,210 860 2,358 1,653 49,905 
2029 36,520 -1,997 5,756 4,274 868 2,390 1,721 49,534 
2030 36,625 -2,684 5,796 4,339 876 2,423 1,788 49,162 
2031 36,451 -2,393 5,791 4,399 869 2,447 1,806 49,371 
2032 36,276 -2,102 5,787 4,460 863 2,472 1,823 49,580 
2033 36,102 -1,811 5,782 4,520 857 2,497 1,840 49,788 
2034 35,928 -1,520 5,778 4,580 851 2,522 1,857 49,997 
2035 35,754 -1,229 5,773 4,640 844 2,547 1,874 50,205 
2036 35,589 -1,249 5,738 4,694 833 2,571 1,868 50,044 
2037 35,425 -1,270 5,702 4,747 823 2,595 1,861 49,883 
2038 35,260 -1,290 5,667 4,800 812 2,619 1,855 49,722 
2039 35,095 -1,311 5,631 4,853 801 2,643 1,848 49,560 
2040 34,931 -1,331 5,596 4,906 790 2,667 1,841 49,399 
2041 34,763 -1,266 5,602 4,962 791 2,698 1,827 49,377 
2042 34,595 -1,200 5,609 5,017 792 2,730 1,812 49,356 
2043 34,427 -1,135 5,616 5,073 793 2,761 1,798 49,334 
2044 34,259 -1,069 5,623 5,129 795 2,793 1,783 49,312 
2045 34,091 -1,004 5,630 5,185 796 2,824 1,768 49,290 
2046 33,866 -981 5,633 5,235 797 2,855 1,764 49,168 
2047 33,642 -959 5,635 5,286 797 2,885 1,760 49,047 
2048 33,417 -937 5,638 5,337 798 2,916 1,755 48,925 
2049 33,193 -914 5,641 5,388 799 2,946 1,751 48,803 
2050 32,968 -892 5,644 5,439 800 2,977 1,747 48,681 
Total 1,101,631 -28,959 178,923 143,533 25,773 78,913 52,906 1,552,720 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-74 
Table C-4.7. Global Emissions Summary for Defined Policies: High U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,403 398 6,677 3,929 887 2,123 1,349 53,766 
2021 37,943 469 6,461 3,946 877 2,151 1,370 53,216 
2022 37,483 539 6,245 3,964 867 2,179 1,390 52,667 
2023 37,023 610 6,029 3,981 857 2,206 1,410 52,117 
2024 36,563 681 5,814 3,999 847 2,234 1,431 51,568 
2025 36,103 751 5,598 4,016 837 2,262 1,451 51,019 
2026 36,207 64 5,637 4,081 845 2,294 1,519 50,647 
2027 36,312 -623 5,677 4,145 853 2,326 1,586 50,276 
2028 36,416 -1,310 5,717 4,210 860 2,358 1,653 49,905 
2029 36,520 -1,997 5,756 4,274 868 2,390 1,721 49,534 
2030 36,625 -2,684 5,796 4,339 876 2,423 1,788 49,162 
2031 36,462 -2,404 5,792 4,399 869 2,447 1,806 49,372 
2032 36,299 -2,125 5,789 4,460 863 2,472 1,823 49,581 
2033 36,137 -1,846 5,786 4,520 857 2,497 1,841 49,791 
2034 35,974 -1,566 5,782 4,580 850 2,521 1,858 50,000 
2035 35,812 -1,287 5,779 4,640 844 2,546 1,876 50,209 
2036 35,665 -1,312 5,745 4,694 833 2,570 1,869 50,064 
2037 35,519 -1,336 5,710 4,747 822 2,593 1,863 49,918 
2038 35,373 -1,361 5,675 4,800 811 2,617 1,857 49,772 
2039 35,227 -1,385 5,641 4,853 800 2,641 1,851 49,627 
2040 35,081 -1,410 5,606 4,906 789 2,664 1,845 49,481 
2041 34,915 -1,341 5,611 4,962 790 2,696 1,830 49,463 
2042 34,749 -1,272 5,616 5,017 791 2,727 1,816 49,444 
2043 34,582 -1,203 5,622 5,073 792 2,758 1,801 49,425 
2044 34,416 -1,134 5,627 5,129 793 2,789 1,786 49,407 
2045 34,250 -1,065 5,632 5,185 794 2,821 1,772 49,388 
2046 34,020 -1,037 5,633 5,235 795 2,851 1,767 49,265 
2047 33,790 -1,009 5,634 5,286 796 2,881 1,763 49,141 
2048 33,559 -981 5,635 5,337 797 2,912 1,758 49,017 
2049 33,329 -953 5,636 5,388 797 2,942 1,754 48,894 
2050 33,099 -925 5,637 5,439 798 2,972 1,750 48,770 
Total 1,103,858 -30,051 178,994 143,533 25,753 78,862 52,956 1,553,906 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-75 
Table C -4.8. Global Emissions Summary for Defined Policies: Low U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,431 396 6,678 3,929 887 2,123 1,350 53,794 
2021 37,958 472 6,462 3,946 877 2,151 1,370 53,236 
2022 37,484 548 6,245 3,964 867 2,179 1,390 52,678 
2023 37,011 625 6,029 3,981 857 2,206 1,410 52,119 
2024 36,538 701 5,812 3,999 847 2,234 1,431 51,561 
2025 36,065 777 5,595 4,016 837 2,261 1,451 51,003 
2026 36,159 93 5,634 4,081 845 2,294 1,518 50,624 
2027 36,254 -591 5,673 4,145 852 2,326 1,586 50,245 
2028 36,348 -1,275 5,712 4,210 860 2,358 1,653 49,866 
2029 36,443 -1,959 5,751 4,274 868 2,391 1,720 49,487 
2030 36,537 -2,643 5,790 4,339 875 2,423 1,788 49,108 
2031 36,359 -2,357 5,785 4,399 869 2,448 1,805 49,308 
2032 36,181 -2,071 5,780 4,460 863 2,473 1,822 49,508 
2033 36,004 -1,785 5,775 4,520 856 2,498 1,839 49,708 
2034 35,826 -1,498 5,770 4,580 850 2,523 1,856 49,907 
2035 35,648 -1,212 5,766 4,640 844 2,548 1,873 50,107 
2036 35,477 -1,232 5,730 4,694 833 2,571 1,867 49,940 
2037 35,306 -1,251 5,695 4,747 822 2,595 1,860 49,773 
2038 35,134 -1,271 5,659 4,800 811 2,619 1,854 49,606 
2039 34,963 -1,290 5,624 4,853 800 2,643 1,847 49,439 
2040 34,791 -1,310 5,588 4,906 789 2,667 1,841 49,273 
2041 34,602 -1,230 5,594 4,962 790 2,699 1,826 49,243 
2042 34,412 -1,149 5,600 5,017 791 2,730 1,811 49,213 
2043 34,222 -1,068 5,605 5,073 792 2,762 1,797 49,183 
2044 34,032 -988 5,611 5,129 794 2,793 1,782 49,153 
2045 33,842 -907 5,616 5,185 795 2,825 1,767 49,123 
2046 33,618 -904 5,619 5,235 795 2,856 1,763 48,982 
2047 33,394 -901 5,621 5,286 796 2,886 1,759 48,841 
2048 33,171 -898 5,624 5,337 796 2,917 1,754 48,701 
2049 32,947 -895 5,627 5,388 797 2,947 1,750 48,560 
2050 32,723 -892 5,629 5,438 798 2,978 1,746 48,419 
Total 1,097,878 -27,967 178,699 143,533 25,755 78,923 52,887 1,549,708 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-76 
Table C-4.9. Global Emissions Summary for Defined Policies: Low U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,431 396 6,678 3,929 887 2,123 1,350 53,794 
2021 37,958 472 6,462 3,946 877 2,151 1,370 53,236 
2022 37,484 548 6,245 3,964 867 2,179 1,390 52,678 
2023 37,011 625 6,029 3,981 857 2,206 1,410 52,119 
2024 36,538 701 5,812 3,999 847 2,234 1,431 51,561 
2025 36,065 777 5,595 4,016 837 2,261 1,451 51,003 
2026 36,159 93 5,634 4,081 845 2,294 1,518 50,624 
2027 36,254 -591 5,673 4,145 852 2,326 1,586 50,245 
2028 36,348 -1,275 5,712 4,210 860 2,358 1,653 49,866 
2029 36,443 -1,959 5,751 4,274 868 2,391 1,720 49,487 
2030 36,537 -2,643 5,790 4,339 875 2,423 1,788 49,108 
2031 36,359 -2,357 5,785 4,399 869 2,448 1,805 49,308 
2032 36,181 -2,071 5,780 4,460 863 2,473 1,822 49,508 
2033 36,004 -1,785 5,775 4,520 856 2,498 1,839 49,708 
2034 35,826 -1,498 5,770 4,580 850 2,523 1,856 49,907 
2035 35,648 -1,212 5,766 4,640 844 2,548 1,873 50,107 
2036 35,478 -1,232 5,730 4,694 833 2,571 1,867 49,940 
2037 35,307 -1,252 5,695 4,747 822 2,595 1,860 49,774 
2038 35,136 -1,273 5,659 4,800 811 2,619 1,854 49,607 
2039 34,966 -1,293 5,624 4,853 800 2,643 1,847 49,440 
2040 34,795 -1,313 5,589 4,906 789 2,667 1,841 49,274 
2041 34,607 -1,234 5,594 4,962 790 2,698 1,826 49,244 
2042 34,420 -1,156 5,599 5,017 791 2,730 1,812 49,214 
2043 34,232 -1,077 5,605 5,073 792 2,762 1,797 49,184 
2044 34,045 -999 5,610 5,129 794 2,793 1,782 49,154 
2045 33,857 -920 5,615 5,185 795 2,825 1,768 49,124 
2046 33,636 -918 5,618 5,235 795 2,855 1,763 48,984 
2047 33,414 -916 5,620 5,286 796 2,886 1,759 48,845 
2048 33,193 -914 5,623 5,337 796 2,916 1,755 48,705 
2049 32,971 -912 5,625 5,388 797 2,947 1,751 48,566 
2050 32,750 -910 5,627 5,438 797 2,977 1,746 48,426 
Total 1,098,051 -28,098 178,691 143,533 25,753 78,919 52,891 1,549,740 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-77 
Table C-4.10. Global Emissions Summary for Commitments (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 35,132 732 5,483 4,071 825 2,277 1,497 50,016 
2027 34,987 511 5,515 4,137 834 2,301 1,560 49,845 
2028 34,841 291 5,548 4,202 844 2,326 1,622 49,674 
2029 34,696 70 5,580 4,268 853 2,350 1,685 49,502 
2030 34,550 -150 5,612 4,334 863 2,374 1,747 49,331 
2031 33,222 -124 5,524 4,381 842 2,401 1,744 47,989 
2032 31,893 -98 5,435 4,428 820 2,428 1,741 46,648 
2033 30,565 -72 5,346 4,476 799 2,455 1,738 45,306 
2034 29,237 -46 5,257 4,523 777 2,482 1,735 43,965 
2035 27,908 -20 5,169 4,570 756 2,509 1,732 42,623 
2036 26,604 180 5,107 4,618 747 2,530 1,723 41,510 
2037 25,300 380 5,046 4,666 738 2,551 1,715 40,396 
2038 23,995 580 4,985 4,714 729 2,572 1,706 39,282 
2039 22,691 781 4,923 4,762 720 2,594 1,698 38,168 
2040 21,387 981 4,862 4,810 711 2,615 1,689 37,054 
2041 20,078 871 4,749 4,851 694 2,627 1,623 35,492 
2042 18,769 762 4,636 4,891 677 2,638 1,556 33,930 
2043 17,460 652 4,523 4,932 660 2,650 1,490 32,368 
2044 16,152 542 4,411 4,972 643 2,662 1,424 30,805 
2045 14,843 433 4,298 5,013 626 2,674 1,357 29,243 
2046 13,554 250 4,208 5,058 610 2,686 1,317 27,683 
2047 12,265 67 4,119 5,104 594 2,698 1,276 26,122 
2048 10,976 -116 4,029 5,149 578 2,710 1,236 24,561 
2049 9,687 -299 3,940 5,194 562 2,722 1,196 23,001 
2050 8,397 -481 3,850 5,240 545 2,734 1,155 21,440 
Total 810,240 11,127 158,531 141,167 23,148 76,699 47,315 1,268,227 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-78 
Table C -4.11. Global Emissions Summary for Commitments (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 35,132 732 5,483 4,071 825 2,277 1,497 50,016 
2027 34,987 511 5,515 4,137 834 2,301 1,560 49,845 
2028 34,841 291 5,548 4,202 844 2,326 1,622 49,674 
2029 34,696 70 5,580 4,268 853 2,350 1,685 49,502 
2030 34,550 -150 5,612 4,334 863 2,374 1,747 49,331 
2031 33,222 -124 5,524 4,381 842 2,401 1,744 47,989 
2032 31,893 -98 5,435 4,428 820 2,428 1,741 46,648 
2033 30,565 -72 5,346 4,476 799 2,455 1,738 45,306 
2034 29,237 -46 5,257 4,523 777 2,482 1,735 43,965 
2035 27,908 -20 5,169 4,570 756 2,509 1,732 42,623 
2036 26,609 172 5,107 4,618 747 2,530 1,724 41,507 
2037 25,309 365 5,046 4,666 738 2,551 1,715 40,390 
2038 24,010 557 4,985 4,714 729 2,572 1,707 39,273 
2039 22,710 750 4,923 4,762 719 2,594 1,698 38,157 
2040 21,411 942 4,862 4,810 710 2,615 1,690 37,040 
2041 20,100 845 4,748 4,851 693 2,626 1,624 35,487 
2042 18,789 747 4,634 4,891 677 2,638 1,557 33,934 
2043 17,478 650 4,520 4,932 660 2,650 1,491 32,381 
2044 16,168 552 4,407 4,972 643 2,662 1,424 30,828 
2045 14,857 455 4,293 5,013 626 2,673 1,358 29,274 
2046 13,566 269 4,202 5,058 610 2,685 1,317 27,708 
2047 12,275 84 4,112 5,104 594 2,697 1,277 26,142 
2048 10,984 -102 4,022 5,149 578 2,709 1,236 24,576 
2049 9,693 -287 3,932 5,194 562 2,721 1,196 23,010 
2050 8,402 -473 3,842 5,240 545 2,733 1,155 21,444 
Total 810,441 11,069 158,481 141,167 23,147 76,696 47,323 1,268,324 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-79 
Table C-4.12. Global Emissions Summary for Commitments (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 35,132 732 5,483 4,071 825 2,277 1,497 50,016 
2027 34,987 511 5,515 4,137 834 2,301 1,560 49,845 
2028 34,841 291 5,548 4,202 844 2,326 1,622 49,674 
2029 34,696 70 5,580 4,268 853 2,350 1,685 49,502 
2030 34,550 -150 5,612 4,334 863 2,374 1,747 49,331 
2031 33,239 -141 5,525 4,381 842 2,401 1,745 47,991 
2032 31,928 -132 5,438 4,428 820 2,428 1,742 46,651 
2033 30,617 -123 5,350 4,476 799 2,454 1,739 45,311 
2034 29,306 -114 5,263 4,523 777 2,481 1,737 43,971 
2035 27,994 -105 5,175 4,570 755 2,507 1,734 42,631 
2036 26,688 104 5,113 4,618 746 2,529 1,725 41,524 
2037 25,382 313 5,050 4,666 737 2,550 1,717 40,416 
2038 24,076 522 4,987 4,714 728 2,571 1,709 39,308 
2039 22,770 731 4,925 4,762 719 2,592 1,700 38,201 
2040 21,465 941 4,862 4,810 710 2,614 1,692 37,093 
2041 20,149 852 4,747 4,851 693 2,626 1,625 35,543 
2042 18,834 764 4,631 4,891 677 2,637 1,559 33,993 
2043 17,518 675 4,516 4,932 660 2,649 1,492 32,443 
2044 16,203 587 4,401 4,972 643 2,661 1,426 30,893 
2045 14,888 499 4,285 5,013 626 2,673 1,359 29,343 
2046 13,595 305 4,194 5,058 610 2,685 1,319 27,766 
2047 12,303 112 4,102 5,104 594 2,697 1,278 26,189 
2048 11,010 -81 4,011 5,149 578 2,709 1,237 24,612 
2049 9,718 -275 3,919 5,195 561 2,721 1,197 23,036 
2050 8,425 -468 3,828 5,240 545 2,733 1,156 21,459 
Total 811,367 10,870 158,436 141,167 23,143 76,678 47,352 1,269,014 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-80 
Table C -4.13. Global Emissions Summary for Commitments (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 35,123 503 5,319 4,040 804 2,266 1,472 49,527 
2027 34,980 279 5,350 4,108 815 2,291 1,535 49,359 
2028 34,838 55 5,381 4,175 827 2,317 1,598 49,191 
2029 34,695 -169 5,412 4,243 838 2,342 1,662 49,024 
2030 34,552 -393 5,444 4,311 850 2,367 1,725 48,856 
2031 33,267 -563 5,299 4,347 824 2,385 1,706 47,265 
2032 31,982 -732 5,155 4,383 797 2,402 1,687 45,674 
2033 30,696 -902 5,011 4,419 771 2,420 1,668 44,084 
2034 29,411 -1,071 4,867 4,456 745 2,438 1,648 42,493 
2035 28,126 -1,241 4,723 4,492 718 2,455 1,629 40,902 
2036 26,822 -1,576 4,617 4,532 702 2,466 1,607 39,170 
2037 25,518 -1,911 4,512 4,572 685 2,477 1,584 37,437 
2038 24,214 -2,246 4,406 4,611 669 2,488 1,562 35,704 
2039 22,910 -2,582 4,301 4,651 653 2,499 1,539 33,971 
2040 21,606 -2,917 4,196 4,691 636 2,511 1,517 32,239 
2041 20,283 -2,775 4,094 4,739 621 2,520 1,471 30,953 
2042 18,960 -2,633 3,993 4,786 606 2,530 1,425 29,668 
2043 17,638 -2,491 3,891 4,834 591 2,540 1,379 28,382 
2044 16,315 -2,349 3,789 4,881 576 2,550 1,333 27,097 
2045 14,992 -2,206 3,688 4,929 561 2,560 1,287 25,811 
2046 13,678 -2,224 3,612 4,979 553 2,575 1,256 24,429 
2047 12,364 -2,241 3,536 5,029 545 2,589 1,224 23,047 
2048 11,051 -2,258 3,460 5,079 536 2,603 1,193 21,664 
2049 9,737 -2,275 3,384 5,129 528 2,618 1,162 20,282 
2050 8,423 -2,293 3,308 5,180 520 2,632 1,131 18,900 
Total 813,197 -35,428 146,632 139,298 22,005 74,944 45,271 1,205,919 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-81 
Table C-4.14. Global Emissions Summary for Commitments (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 35,123 503 5,319 4,040 804 2,266 1,472 49,527 
2027 34,980 279 5,350 4,108 815 2,291 1,535 49,359 
2028 34,838 55 5,381 4,175 827 2,317 1,598 49,191 
2029 34,695 -169 5,412 4,243 838 2,342 1,662 49,024 
2030 34,552 -393 5,444 4,311 850 2,367 1,725 48,856 
2031 33,267 -563 5,299 4,347 824 2,385 1,706 47,265 
2032 31,982 -732 5,155 4,383 797 2,402 1,687 45,674 
2033 30,696 -902 5,011 4,419 771 2,420 1,668 44,084 
2034 29,411 -1,071 4,867 4,456 745 2,438 1,648 42,493 
2035 28,126 -1,241 4,723 4,492 718 2,455 1,629 40,902 
2036 26,823 -1,576 4,617 4,532 702 2,466 1,607 39,171 
2037 25,520 -1,911 4,512 4,572 685 2,477 1,584 37,440 
2038 24,217 -2,246 4,406 4,611 669 2,488 1,562 35,709 
2039 22,914 -2,581 4,301 4,651 653 2,500 1,539 33,978 
2040 21,612 -2,916 4,196 4,691 636 2,511 1,517 32,246 
2041 20,289 -2,774 4,094 4,739 621 2,520 1,471 30,960 
2042 18,967 -2,632 3,992 4,786 606 2,530 1,425 29,675 
2043 17,644 -2,489 3,890 4,834 591 2,540 1,379 28,389 
2044 16,321 -2,347 3,788 4,881 576 2,550 1,333 27,103 
2045 14,999 -2,205 3,686 4,929 561 2,560 1,287 25,817 
2046 13,684 -2,223 3,610 4,979 553 2,575 1,256 24,433 
2047 12,370 -2,241 3,533 5,029 545 2,589 1,224 23,050 
2048 11,055 -2,258 3,457 5,079 536 2,603 1,193 21,666 
2049 9,741 -2,276 3,381 5,129 528 2,618 1,162 20,283 
2050 8,426 -2,294 3,305 5,180 520 2,632 1,131 18,899 
Total 813,270 -35,419 146,614 139,299 22,005 74,944 45,273 1,205,985 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-82 
Table C -4.15. Global Emissions Summary for Commitments (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 35,123 503 5,319 4,040 804 2,266 1,472 49,527 
2027 34,980 279 5,350 4,108 815 2,291 1,535 49,359 
2028 34,838 55 5,381 4,175 827 2,317 1,598 49,191 
2029 34,695 -169 5,412 4,243 838 2,342 1,662 49,024 
2030 34,552 -393 5,444 4,311 850 2,367 1,725 48,856 
2031 33,276 -560 5,301 4,347 824 2,385 1,706 47,278 
2032 32,000 -728 5,157 4,383 797 2,402 1,687 45,700 
2033 30,724 -895 5,014 4,419 771 2,420 1,669 44,122 
2034 29,448 -1,063 4,871 4,456 745 2,438 1,650 42,545 
2035 28,172 -1,230 4,728 4,492 719 2,455 1,631 40,967 
2036 26,866 -1,566 4,621 4,532 702 2,467 1,609 39,230 
2037 25,561 -1,903 4,514 4,572 686 2,478 1,586 37,493 
2038 24,255 -2,239 4,407 4,611 669 2,489 1,563 35,756 
2039 22,950 -2,575 4,300 4,651 653 2,500 1,541 34,019 
2040 21,644 -2,912 4,193 4,691 636 2,511 1,518 32,282 
2041 20,325 -2,770 4,091 4,739 621 2,520 1,472 30,999 
2042 19,007 -2,628 3,988 4,786 606 2,530 1,426 29,716 
2043 17,688 -2,486 3,885 4,834 591 2,540 1,380 28,433 
2044 16,369 -2,344 3,782 4,882 576 2,550 1,334 27,149 
2045 15,050 -2,201 3,679 4,929 561 2,560 1,288 25,866 
2046 13,743 -2,220 3,602 4,979 553 2,574 1,257 24,489 
2047 12,436 -2,239 3,526 5,029 545 2,589 1,226 23,111 
2048 11,129 -2,257 3,449 5,080 536 2,603 1,194 21,734 
2049 9,822 -2,276 3,373 5,130 528 2,617 1,163 20,357 
2050 8,515 -2,295 3,296 5,180 519 2,632 1,132 18,979 
Total 814,186 -35,330 146,569 139,301 22,006 74,943 45,298 1,206,973 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-83 
Table C-4.16. Global Emissions Summary for Net Zero 2050 (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 33,803 423 5,351 4,051 798 2,275 1,471 48,171 
2027 32,329 -107 5,251 4,096 781 2,297 1,508 46,155 
2028 30,854 -636 5,151 4,141 764 2,319 1,545 44,138 
2029 29,380 -1,166 5,051 4,187 746 2,341 1,582 42,121 
2030 27,905 -1,695 4,951 4,232 729 2,364 1,618 40,105 
2031 26,454 -1,180 4,903 4,284 723 2,391 1,619 39,193 
2032 25,003 -666 4,854 4,336 717 2,418 1,619 38,281 
2033 23,552 -151 4,806 4,388 710 2,445 1,619 37,370 
2034 22,101 364 4,758 4,440 704 2,472 1,619 36,458 
2035 20,649 878 4,709 4,492 698 2,499 1,620 35,546 
2036 19,293 727 4,597 4,532 679 2,512 1,593 33,933 
2037 17,936 577 4,485 4,572 660 2,524 1,567 32,321 
2038 16,580 426 4,373 4,612 640 2,537 1,541 30,708 
2039 15,223 275 4,261 4,651 621 2,549 1,514 29,095 
2040 13,866 125 4,149 4,691 602 2,562 1,488 27,483 
2041 12,508 178 4,077 4,743 591 2,574 1,444 26,115 
2042 11,150 231 4,005 4,795 581 2,586 1,400 24,746 
2043 9,792 284 3,933 4,846 570 2,598 1,355 23,378 
2044 8,434 337 3,861 4,898 559 2,610 1,311 22,010 
2045 7,076 389 3,789 4,950 549 2,622 1,267 20,642 
2046 5,680 360 3,693 5,004 541 2,633 1,236 19,147 
2047 4,283 330 3,597 5,058 533 2,645 1,206 17,653 
2048 2,887 301 3,501 5,112 526 2,657 1,175 16,158 
2049 1,490 271 3,405 5,167 518 2,669 1,144 14,664 
2050 94 242 3,308 5,221 510 2,680 1,114 13,169 
Total 639,377 5,568 145,193 139,301 21,153 75,913 44,528 1,071,033 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-84 
Table C -4.17. Global Emissions Summary for Net Zero 2050 (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 33,803 423 5,351 4,051 798 2,275 1,471 48,171 
2027 32,329 -107 5,251 4,096 781 2,297 1,508 46,155 
2028 30,854 -636 5,151 4,141 764 2,319 1,545 44,138 
2029 29,380 -1,166 5,051 4,187 746 2,341 1,582 42,121 
2030 27,905 -1,695 4,951 4,232 729 2,364 1,618 40,105 
2031 26,454 -1,181 4,903 4,284 723 2,391 1,619 39,193 
2032 25,003 -666 4,854 4,336 717 2,418 1,619 38,281 
2033 23,551 -151 4,806 4,388 710 2,445 1,619 37,369 
2034 22,100 363 4,758 4,440 704 2,472 1,619 36,457 
2035 20,649 878 4,709 4,492 698 2,499 1,620 35,546 
2036 19,295 723 4,597 4,532 679 2,512 1,593 33,931 
2037 17,941 567 4,485 4,572 660 2,524 1,567 32,316 
2038 16,586 412 4,373 4,612 640 2,537 1,541 30,701 
2039 15,232 257 4,261 4,651 621 2,549 1,515 29,086 
2040 13,878 101 4,148 4,691 602 2,561 1,488 27,471 
2041 12,518 162 4,076 4,743 591 2,573 1,444 26,108 
2042 11,159 224 4,003 4,794 581 2,585 1,400 24,746 
2043 9,799 285 3,931 4,846 570 2,597 1,356 23,384 
2044 8,439 346 3,858 4,898 559 2,609 1,311 22,022 
2045 7,080 407 3,786 4,950 549 2,621 1,267 20,660 
2046 5,683 374 3,690 5,004 541 2,633 1,237 19,161 
2047 4,286 341 3,593 5,058 533 2,645 1,206 17,663 
2048 2,889 308 3,497 5,112 526 2,657 1,175 16,164 
2049 1,492 275 3,401 5,167 518 2,668 1,144 14,666 
2050 95 242 3,305 5,221 510 2,680 1,114 13,167 
Total 639,453 5,540 145,165 139,301 21,152 75,911 44,531 1,071,054 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-85 
Table C-4.18. Global Emissions Summary for Net Zero 2050 (High CCS): High Exports (GCAM-
NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,781 616 6,430 3,944 872 2,151 1,366 53,160 
2022 37,155 700 6,185 3,959 857 2,177 1,384 52,417 
2023 36,529 784 5,940 3,975 843 2,202 1,401 51,674 
2024 35,903 868 5,696 3,990 829 2,227 1,418 50,931 
2025 35,278 952 5,451 4,005 815 2,252 1,435 50,188 
2026 33,803 423 5,351 4,051 798 2,275 1,471 48,171 
2027 32,329 -107 5,251 4,096 781 2,297 1,508 46,155 
2028 30,854 -636 5,151 4,141 764 2,319 1,545 44,138 
2029 29,380 -1,166 5,051 4,187 746 2,341 1,582 42,121 
2030 27,905 -1,695 4,951 4,232 729 2,364 1,618 40,105 
2031 26,462 -1,196 4,904 4,284 723 2,391 1,619 39,187 
2032 25,020 -697 4,856 4,336 716 2,418 1,620 38,270 
2033 23,577 -197 4,809 4,388 710 2,445 1,620 37,352 
2034 22,134 302 4,761 4,440 704 2,472 1,621 36,434 
2035 20,692 801 4,714 4,492 697 2,499 1,622 35,517 
2036 19,337 662 4,601 4,532 678 2,511 1,595 33,916 
2037 17,982 522 4,487 4,572 659 2,523 1,569 32,315 
2038 16,628 382 4,374 4,611 640 2,536 1,543 30,714 
2039 15,273 243 4,261 4,651 621 2,548 1,516 29,113 
2040 13,919 103 4,147 4,691 602 2,560 1,490 27,512 
2041 12,556 173 4,073 4,743 591 2,573 1,446 26,154 
2042 11,193 243 3,999 4,794 581 2,585 1,401 24,796 
2043 9,830 313 3,926 4,846 570 2,597 1,357 23,438 
2044 8,467 383 3,852 4,898 560 2,609 1,313 22,080 
2045 7,104 453 3,778 4,950 549 2,621 1,268 20,722 
2046 5,704 407 3,681 5,004 541 2,632 1,237 19,207 
2047 4,304 360 3,584 5,058 533 2,644 1,207 17,691 
2048 2,904 313 3,487 5,113 525 2,656 1,176 16,175 
2049 1,504 267 3,390 5,167 518 2,668 1,145 14,659 
2050 104 220 3,293 5,221 510 2,679 1,114 13,143 
Total 640,017 5,330 145,109 139,300 21,148 75,896 44,556 1,071,356 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-86 
Table C -4.19. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 33,806 76 5,140 4,007 774 2,258 1,436 47,497 
2027 32,347 -576 4,992 4,042 757 2,276 1,463 45,300 
2028 30,888 -1,227 4,844 4,077 739 2,293 1,491 43,103 
2029 29,428 -1,879 4,696 4,112 721 2,310 1,518 40,906 
2030 27,969 -2,531 4,548 4,147 703 2,328 1,546 38,710 
2031 26,585 -2,788 4,429 4,189 685 2,338 1,535 36,973 
2032 25,201 -3,046 4,309 4,232 668 2,348 1,525 35,236 
2033 23,817 -3,304 4,189 4,275 650 2,358 1,514 33,499 
2034 22,433 -3,561 4,070 4,317 632 2,368 1,504 31,763 
2035 21,049 -3,819 3,950 4,360 614 2,378 1,493 30,026 
2036 19,668 -3,575 3,875 4,412 601 2,391 1,481 28,853 
2037 18,286 -3,331 3,799 4,463 588 2,404 1,470 27,679 
2038 16,904 -3,088 3,724 4,515 575 2,417 1,458 26,505 
2039 15,522 -2,844 3,649 4,567 562 2,430 1,446 25,332 
2040 14,140 -2,600 3,573 4,619 549 2,442 1,435 24,158 
2041 12,778 -2,738 3,468 4,670 541 2,449 1,396 22,563 
2042 11,416 -2,876 3,362 4,720 533 2,456 1,356 20,968 
2043 10,054 -3,014 3,256 4,771 524 2,463 1,317 19,372 
2044 8,692 -3,152 3,150 4,822 516 2,470 1,278 17,777 
2045 7,330 -3,290 3,044 4,873 508 2,477 1,239 16,181 
2046 5,916 -2,831 2,967 4,930 504 2,494 1,218 15,196 
2047 4,501 -2,373 2,890 4,987 500 2,510 1,196 14,212 
2048 3,086 -1,914 2,813 5,044 496 2,527 1,175 13,227 
2049 1,672 -1,455 2,735 5,101 492 2,544 1,154 12,242 
2050 257 -996 2,658 5,158 488 2,561 1,132 11,257 
Total 644,762 -58,952 130,012 137,111 19,953 73,393 43,049 989,329 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-87 
Table C-4.20. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 33,806 76 5,140 4,007 774 2,258 1,436 47,497 
2027 32,347 -576 4,992 4,042 757 2,276 1,463 45,300 
2028 30,888 -1,227 4,844 4,077 739 2,293 1,491 43,103 
2029 29,428 -1,879 4,696 4,112 721 2,310 1,518 40,906 
2030 27,969 -2,531 4,548 4,147 703 2,328 1,546 38,710 
2031 26,585 -2,788 4,429 4,189 685 2,338 1,535 36,973 
2032 25,201 -3,046 4,309 4,232 668 2,348 1,525 35,236 
2033 23,817 -3,304 4,189 4,275 650 2,358 1,514 33,499 
2034 22,433 -3,561 4,070 4,317 632 2,368 1,504 31,763 
2035 21,049 -3,819 3,950 4,360 614 2,378 1,493 30,026 
2036 19,668 -3,575 3,875 4,412 601 2,391 1,481 28,853 
2037 18,286 -3,331 3,799 4,463 588 2,404 1,470 27,679 
2038 16,904 -3,088 3,724 4,515 575 2,417 1,458 26,505 
2039 15,522 -2,844 3,649 4,567 562 2,430 1,446 25,332 
2040 14,140 -2,600 3,573 4,619 549 2,442 1,435 24,158 
2041 12,778 -2,738 3,468 4,670 541 2,449 1,396 22,563 
2042 11,416 -2,876 3,362 4,720 533 2,456 1,356 20,968 
2043 10,054 -3,014 3,256 4,771 524 2,463 1,317 19,372 
2044 8,692 -3,152 3,150 4,822 516 2,470 1,278 17,777 
2045 7,330 -3,290 3,044 4,873 508 2,477 1,239 16,181 
2046 5,916 -2,831 2,967 4,930 504 2,494 1,218 15,196 
2047 4,501 -2,373 2,890 4,987 500 2,510 1,196 14,212 
2048 3,086 -1,914 2,813 5,044 496 2,527 1,175 13,227 
2049 1,672 -1,455 2,735 5,101 492 2,544 1,154 12,242 
2050 257 -996 2,658 5,158 488 2,561 1,132 11,257 
Total 644,762 -58,952 130,012 137,111 19,953 73,393 43,049 989,329 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-88 
Table C -4.21.Global Emissions Summary for Net Zero 2050 (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-100 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,407 532 6,674 3,928 886 2,126 1,349 53,903 
2021 37,778 571 6,397 3,937 867 2,149 1,361 53,061 
2022 37,150 610 6,120 3,946 848 2,172 1,373 52,220 
2023 36,522 650 5,842 3,955 829 2,195 1,385 51,378 
2024 35,894 689 5,565 3,963 811 2,218 1,397 50,536 
2025 35,266 728 5,287 3,972 792 2,241 1,408 49,694 
2026 33,806 76 5,140 4,007 774 2,258 1,436 47,497 
2027 32,347 -576 4,992 4,042 757 2,276 1,463 45,300 
2028 30,888 -1,227 4,844 4,077 739 2,293 1,491 43,103 
2029 29,428 -1,879 4,696 4,112 721 2,310 1,518 40,906 
2030 27,969 -2,531 4,548 4,147 703 2,328 1,546 38,710 
2031 26,596 -2,796 4,429 4,189 685 2,338 1,535 36,978 
2032 25,223 -3,060 4,311 4,232 668 2,348 1,525 35,245 
2033 23,850 -3,325 4,192 4,275 650 2,358 1,515 33,513 
2034 22,477 -3,590 4,073 4,317 632 2,368 1,505 31,781 
2035 21,104 -3,855 3,954 4,360 614 2,378 1,495 30,049 
2036 19,727 -3,604 3,878 4,412 601 2,391 1,483 28,887 
2037 18,349 -3,354 3,802 4,463 588 2,404 1,471 27,724 
2038 16,972 -3,103 3,726 4,515 575 2,416 1,460 26,561 
2039 15,594 -2,852 3,650 4,567 562 2,429 1,448 25,399 
2040 14,217 -2,601 3,574 4,618 549 2,442 1,436 24,236 
2041 12,857 -2,740 3,467 4,669 541 2,449 1,397 22,639 
2042 11,497 -2,879 3,359 4,720 532 2,456 1,358 21,043 
2043 10,137 -3,018 3,251 4,771 524 2,463 1,318 19,446 
2044 8,777 -3,158 3,144 4,822 516 2,470 1,279 17,849 
2045 7,417 -3,297 3,036 4,873 508 2,477 1,239 16,253 
2046 6,010 -2,853 2,958 4,930 504 2,493 1,218 15,260 
2047 4,604 -2,410 2,880 4,987 500 2,510 1,197 14,267 
2048 3,198 -1,966 2,802 5,043 496 2,527 1,175 13,274 
2049 1,792 -1,523 2,723 5,100 491 2,543 1,154 12,282 
2050 386 -1,079 2,645 5,157 487 2,560 1,132 11,289 
Total 646,236 -59,419 129,959 137,105 19,949 73,386 43,066 990,283 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-89 
Table C-4.22. Global Emissions Summary for Defined Policies: Existing/FID Exports (GCAM-
NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,334 398 18,207 11,671 887 2,123 2,244 73,863 
2021 37,872 469 17,617 11,723 877 2,151 2,265 72,973 
2022 37,409 540 17,027 11,775 867 2,179 2,287 72,083 
2023 36,947 611 16,437 11,827 857 2,206 2,308 71,193 
2024 36,484 683 15,847 11,879 847 2,234 2,330 70,303 
2025 36,022 754 15,257 11,930 837 2,262 2,351 69,413 
2026 36,123 67 15,363 12,122 845 2,294 2,456 69,271 
2027 36,225 -619 15,470 12,314 853 2,326 2,561 69,129 
2028 36,326 -1,306 15,577 12,506 860 2,358 2,665 68,987 
2029 36,428 -1,992 15,684 12,697 868 2,390 2,770 68,845 
2030 36,529 -2,679 15,791 12,889 876 2,423 2,875 68,703 
2031 36,355 -2,389 15,778 13,068 869 2,448 2,898 69,025 
2032 36,180 -2,100 15,764 13,248 863 2,472 2,921 69,348 
2033 36,005 -1,811 15,751 13,427 857 2,497 2,944 69,670 
2034 35,831 -1,522 15,738 13,606 851 2,522 2,967 69,992 
2035 35,656 -1,233 15,725 13,785 844 2,547 2,990 70,314 
2036 35,489 -1,252 15,626 13,943 833 2,571 2,975 70,185 
2037 35,322 -1,271 15,527 14,100 822 2,595 2,960 70,056 
2038 35,155 -1,290 15,428 14,258 811 2,619 2,945 69,927 
2039 34,988 -1,309 15,329 14,416 801 2,643 2,931 69,798 
2040 34,821 -1,328 15,230 14,574 790 2,667 2,916 69,669 
2041 34,648 -1,261 15,245 14,739 791 2,698 2,884 69,744 
2042 34,475 -1,194 15,259 14,905 792 2,730 2,853 69,820 
2043 34,302 -1,127 15,274 15,070 793 2,761 2,821 69,896 
2044 34,130 -1,059 15,289 15,236 794 2,793 2,789 69,971 
2045 33,957 -992 15,303 15,401 796 2,824 2,758 70,047 
2046 33,727 -969 15,307 15,552 796 2,855 2,747 70,016 
2047 33,497 -945 15,311 15,703 797 2,885 2,737 69,985 
2048 33,267 -922 15,315 15,854 798 2,916 2,726 69,954 
2049 33,037 -898 15,318 16,005 798 2,946 2,716 69,923 
2050 32,807 -874 15,322 16,156 799 2,977 2,705 69,892 
Total 1,098,346 -28,818 487,115 426,377 25,770 78,914 84,293 2,171,997 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-90 
Table C-4.23. Global Emissions Summary for Defined Policies: Model Resolved (GCAM -NETL-
Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 100-year) 
2020 38,334 398 18,207 11,671 887 2,123 2,244 73,863 
2021 37,872 469 17,617 11,723 877 2,151 2,265 72,973 
2022 37,409 540 17,027 11,775 867 2,179 2,287 72,083 
2023 36,947 611 16,437 11,827 857 2,206 2,308 71,193 
2024 36,484 683 15,847 11,879 847 2,234 2,330 70,303 
2025 36,022 754 15,257 11,930 837 2,262 2,351 69,413 
2026 36,123 67 15,363 12,122 845 2,294 2,456 69,271 
2027 36,225 -619 15,470 12,314 853 2,326 2,561 69,129 
2028 36,326 -1,306 15,577 12,506 860 2,358 2,665 68,987 
2029 36,428 -1,992 15,684 12,697 868 2,390 2,770 68,845 
2030 36,529 -2,679 15,791 12,889 876 2,423 2,875 68,703 
2031 36,362 -2,397 15,779 13,068 869 2,447 2,898 69,027 
2032 36,194 -2,115 15,768 13,247 863 2,472 2,921 69,351 
2033 36,027 -1,833 15,757 13,427 857 2,497 2,944 69,675 
2034 35,859 -1,551 15,745 13,606 850 2,522 2,968 69,999 
2035 35,692 -1,269 15,734 13,785 844 2,546 2,991 70,323 
2036 35,538 -1,293 15,636 13,943 833 2,570 2,977 70,204 
2037 35,385 -1,317 15,539 14,100 822 2,594 2,962 70,086 
2038 35,232 -1,341 15,442 14,258 811 2,618 2,948 69,967 
2039 35,079 -1,364 15,344 14,416 800 2,641 2,934 69,849 
2040 34,925 -1,388 15,247 14,574 789 2,665 2,919 69,731 
2041 34,750 -1,315 15,257 14,739 790 2,696 2,888 69,806 
2042 34,575 -1,241 15,267 14,905 791 2,728 2,856 69,881 
2043 34,399 -1,167 15,278 15,070 792 2,759 2,824 69,956 
2044 34,224 -1,093 15,288 15,236 794 2,791 2,793 70,031 
2045 34,048 -1,020 15,298 15,402 795 2,822 2,761 70,106 
2046 33,810 -990 15,298 15,552 795 2,853 2,750 70,068 
2047 33,571 -960 15,297 15,703 796 2,883 2,740 70,030 
2048 33,332 -930 15,297 15,854 797 2,914 2,729 69,992 
2049 33,093 -900 15,296 16,005 797 2,944 2,718 69,954 
2050 32,855 -871 15,296 16,156 798 2,975 2,708 69,916 
Total 1,099,646 -29,427 487,141 426,378 25,755 78,881 84,340 2,172,715 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-91 
Table C -4.24. Global Emissions Summary for Defined Policies: High Exports (GCAM -NETL-
Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,334 398 18,207 11,671 887 2,123 2,244 73,863 
2021 37,872 469 17,617 11,723 877 2,151 2,265 72,973 
2022 37,409 540 17,027 11,775 867 2,179 2,287 72,083 
2023 36,947 611 16,437 11,827 857 2,206 2,308 71,193 
2024 36,484 683 15,847 11,879 847 2,234 2,330 70,303 
2025 36,022 754 15,257 11,930 837 2,262 2,351 69,413 
2026 36,123 67 15,363 12,122 845 2,294 2,456 69,271 
2027 36,225 -619 15,470 12,314 853 2,326 2,561 69,129 
2028 36,326 -1,306 15,577 12,506 860 2,358 2,665 68,987 
2029 36,428 -1,992 15,684 12,697 868 2,390 2,770 68,845 
2030 36,529 -2,679 15,791 12,889 876 2,423 2,875 68,703 
2031 36,375 -2,410 15,782 13,068 869 2,447 2,898 69,029 
2032 36,220 -2,142 15,773 13,247 863 2,472 2,922 69,356 
2033 36,066 -1,873 15,765 13,427 856 2,496 2,946 69,682 
2034 35,912 -1,605 15,756 13,606 850 2,520 2,969 70,008 
2035 35,757 -1,337 15,747 13,785 843 2,545 2,993 70,334 
2036 35,606 -1,349 15,650 13,943 832 2,569 2,979 70,228 
2037 35,454 -1,362 15,552 14,100 821 2,592 2,965 70,123 
2038 35,302 -1,375 15,455 14,258 810 2,616 2,950 70,017 
2039 35,151 -1,388 15,357 14,416 799 2,640 2,936 69,911 
2040 34,999 -1,400 15,260 14,574 788 2,663 2,922 69,806 
2041 34,821 -1,326 15,268 14,739 789 2,695 2,890 69,877 
2042 34,644 -1,252 15,277 14,905 791 2,726 2,858 69,948 
2043 34,466 -1,179 15,285 15,070 792 2,758 2,827 70,020 
2044 34,289 -1,105 15,294 15,236 793 2,789 2,795 70,091 
2045 34,111 -1,031 15,302 15,402 794 2,820 2,763 70,162 
2046 33,868 -999 15,300 15,552 795 2,851 2,753 70,120 
2047 33,625 -967 15,298 15,703 795 2,881 2,742 70,077 
2048 33,381 -935 15,296 15,854 796 2,912 2,731 70,035 
2049 33,138 -903 15,294 16,005 796 2,942 2,720 69,993 
2050 32,894 -872 15,292 16,156 797 2,973 2,710 69,950 
Total 1,100,779 -29,883 487,281 426,378 25,744 78,852 84,380 2,173,530 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-92 
Table C -4.25. Global Emissions Summary for Defined Policies: High Middle East Supply: 
Existing/FID Exports (GCAM_NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,342 397 18,209 11,671 887 2,123 2,244 73,874 
2021 37,881 468 17,620 11,723 877 2,151 2,266 72,985 
2022 37,420 540 17,030 11,775 867 2,179 2,287 72,097 
2023 36,959 611 16,440 11,827 857 2,206 2,309 71,208 
2024 36,497 682 15,850 11,879 847 2,234 2,330 70,319 
2025 36,036 753 15,261 11,930 837 2,262 2,351 69,431 
2026 36,148 56 15,371 12,122 845 2,294 2,456 69,292 
2027 36,259 -640 15,481 12,314 853 2,326 2,561 69,154 
2028 36,371 -1,336 15,591 12,506 860 2,358 2,666 69,016 
2029 36,483 -2,033 15,701 12,697 868 2,390 2,771 68,877 
2030 36,594 -2,729 15,812 12,889 875 2,422 2,876 68,739 
2031 36,442 -2,452 15,808 13,068 869 2,446 2,900 69,080 
2032 36,289 -2,175 15,804 13,247 863 2,471 2,923 69,421 
2033 36,136 -1,898 15,800 13,427 856 2,495 2,947 69,762 
2034 35,984 -1,621 15,796 13,606 850 2,520 2,971 70,104 
2035 35,831 -1,345 15,792 13,785 843 2,544 2,995 70,445 
2036 35,691 -1,363 15,706 13,943 832 2,568 2,981 70,357 
2037 35,551 -1,382 15,620 14,100 821 2,591 2,967 70,269 
2038 35,411 -1,400 15,534 14,258 810 2,615 2,953 70,181 
2039 35,272 -1,419 15,448 14,416 799 2,638 2,938 70,093 
2040 35,132 -1,438 15,362 14,574 788 2,662 2,924 70,005 
2041 34,972 -1,374 15,384 14,739 789 2,693 2,893 70,096 
2042 34,813 -1,311 15,405 14,905 790 2,724 2,862 70,188 
2043 34,653 -1,248 15,426 15,070 791 2,755 2,830 70,279 
2044 34,493 -1,184 15,448 15,236 793 2,786 2,799 70,370 
2045 34,334 -1,121 15,469 15,402 794 2,817 2,767 70,462 
2046 34,111 -1,100 15,479 15,553 794 2,847 2,757 70,442 
2047 33,889 -1,078 15,489 15,703 795 2,877 2,746 70,422 
2048 33,666 -1,057 15,499 15,854 796 2,907 2,736 70,402 
2049 33,444 -1,035 15,509 16,005 796 2,937 2,726 70,382 
2050 33,221 -1,014 15,519 16,156 797 2,967 2,715 70,362 
Total 1,104,327 -31,246 489,663 426,379 25,741 78,803 84,447 2,178,114 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-93 
Table C-4.26. Global Emissions Summary for Defined Policies: High Middle East Supply: Model 
Resolved (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,342 397 18,209 11,671 887 2,123 2,244 73,874 
2021 37,881 468 17,620 11,723 877 2,151 2,266 72,985 
2022 37,420 540 17,030 11,775 867 2,179 2,287 72,097 
2023 36,959 611 16,440 11,827 857 2,206 2,309 71,208 
2024 36,497 682 15,850 11,879 847 2,234 2,330 70,319 
2025 36,036 753 15,261 11,930 837 2,262 2,351 69,431 
2026 36,148 56 15,371 12,122 845 2,294 2,456 69,292 
2027 36,259 -640 15,481 12,314 853 2,326 2,561 69,154 
2028 36,371 -1,336 15,591 12,506 860 2,358 2,666 69,016 
2029 36,483 -2,033 15,701 12,697 868 2,390 2,771 68,877 
2030 36,594 -2,729 15,812 12,889 875 2,422 2,876 68,739 
2031 36,447 -2,458 15,809 13,068 869 2,446 2,900 69,081 
2032 36,300 -2,186 15,806 13,247 862 2,470 2,924 69,423 
2033 36,153 -1,915 15,802 13,426 856 2,495 2,948 69,766 
2034 36,006 -1,643 15,799 13,606 850 2,519 2,972 70,108 
2035 35,859 -1,372 15,796 13,785 843 2,543 2,996 70,450 
2036 35,724 -1,390 15,709 13,943 832 2,567 2,982 70,367 
2037 35,590 -1,408 15,622 14,100 821 2,590 2,968 70,283 
2038 35,455 -1,426 15,535 14,258 810 2,614 2,954 70,200 
2039 35,321 -1,444 15,447 14,416 799 2,637 2,940 70,116 
2040 35,186 -1,462 15,360 14,574 788 2,661 2,927 70,033 
2041 35,025 -1,394 15,378 14,739 789 2,692 2,895 70,123 
2042 34,863 -1,327 15,396 14,905 790 2,723 2,864 70,214 
2043 34,701 -1,259 15,414 15,070 791 2,754 2,832 70,304 
2044 34,540 -1,192 15,433 15,236 792 2,785 2,801 70,395 
2045 34,378 -1,124 15,451 15,402 793 2,816 2,769 70,485 
2046 34,152 -1,103 15,458 15,553 794 2,846 2,759 70,458 
2047 33,926 -1,082 15,465 15,704 795 2,876 2,748 70,432 
2048 33,700 -1,061 15,473 15,854 795 2,906 2,738 70,405 
2049 33,475 -1,040 15,480 16,005 796 2,936 2,727 70,379 
2050 33,249 -1,019 15,487 16,156 797 2,966 2,717 70,352 
Total 1,105,043 -31,537 489,486 426,379 25,734 78,785 84,476 2,178,366 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-94 
Table C-4.27. Global Emissions Summary for Defined Policies: High U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,330 398 18,207 11,671 887 2,123 2,243 73,858 
2021 37,869 469 17,617 11,723 877 2,151 2,265 72,970 
2022 37,408 539 17,027 11,775 867 2,179 2,287 72,081 
2023 36,947 610 16,437 11,827 857 2,206 2,308 71,192 
2024 36,486 681 15,847 11,879 847 2,234 2,330 70,304 
2025 36,026 751 15,257 11,930 837 2,262 2,351 69,415 
2026 36,128 64 15,364 12,122 845 2,294 2,456 69,274 
2027 36,231 -623 15,471 12,314 853 2,326 2,561 69,133 
2028 36,334 -1,310 15,578 12,506 860 2,358 2,665 68,992 
2029 36,436 -1,997 15,686 12,697 868 2,390 2,770 68,851 
2030 36,539 -2,684 15,793 12,889 876 2,423 2,875 68,710 
2031 36,364 -2,393 15,779 13,068 869 2,447 2,898 69,033 
2032 36,188 -2,102 15,766 13,248 863 2,472 2,921 69,356 
2033 36,013 -1,811 15,752 13,427 857 2,497 2,944 69,680 
2034 35,838 -1,520 15,739 13,606 851 2,522 2,967 70,003 
2035 35,662 -1,229 15,725 13,785 844 2,547 2,990 70,326 
2036 35,497 -1,249 15,627 13,943 833 2,571 2,975 70,197 
2037 35,331 -1,270 15,528 14,100 823 2,595 2,960 70,068 
2038 35,165 -1,290 15,429 14,258 812 2,619 2,946 69,939 
2039 35,000 -1,311 15,330 14,416 801 2,643 2,931 69,810 
2040 34,834 -1,331 15,232 14,574 790 2,667 2,916 69,681 
2041 34,665 -1,266 15,247 14,739 791 2,698 2,884 69,759 
2042 34,496 -1,200 15,262 14,905 792 2,730 2,853 69,837 
2043 34,327 -1,135 15,277 15,070 793 2,761 2,821 69,916 
2044 34,158 -1,069 15,292 15,236 795 2,793 2,790 69,994 
2045 33,989 -1,004 15,307 15,401 796 2,824 2,758 70,073 
2046 33,764 -981 15,312 15,552 797 2,855 2,748 70,046 
2047 33,539 -959 15,316 15,703 797 2,885 2,737 70,019 
2048 33,313 -937 15,321 15,854 798 2,916 2,726 69,992 
2049 33,088 -914 15,325 16,005 799 2,946 2,716 69,965 
2050 32,863 -892 15,330 16,156 800 2,977 2,705 69,938 
Total 1,098,830 -28,959 487,179 426,377 25,773 78,913 84,297 2,172,411 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-95 
Table C -4.28. Global Emissions Summary for Defined Policies: High U.S. Supply: Model 
Resolved (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,330 398 18,207 11,671 887 2,123 2,243 73,858 
2021 37,869 469 17,617 11,723 877 2,151 2,265 72,970 
2022 37,408 539 17,027 11,775 867 2,179 2,287 72,081 
2023 36,947 610 16,437 11,827 857 2,206 2,308 71,192 
2024 36,486 681 15,847 11,879 847 2,234 2,330 70,304 
2025 36,026 751 15,257 11,930 837 2,262 2,351 69,415 
2026 36,128 64 15,364 12,122 845 2,294 2,456 69,274 
2027 36,231 -623 15,471 12,314 853 2,326 2,561 69,133 
2028 36,334 -1,310 15,578 12,506 860 2,358 2,665 68,992 
2029 36,436 -1,997 15,686 12,697 868 2,390 2,770 68,851 
2030 36,539 -2,684 15,793 12,889 876 2,423 2,875 68,710 
2031 36,375 -2,404 15,782 13,068 869 2,447 2,898 69,036 
2032 36,211 -2,125 15,771 13,247 863 2,472 2,922 69,361 
2033 36,047 -1,846 15,760 13,427 857 2,497 2,945 69,687 
2034 35,883 -1,566 15,750 13,606 850 2,521 2,968 70,012 
2035 35,719 -1,287 15,739 13,785 844 2,546 2,992 70,338 
2036 35,572 -1,312 15,642 13,943 833 2,570 2,978 70,226 
2037 35,425 -1,336 15,546 14,100 822 2,593 2,963 70,113 
2038 35,277 -1,361 15,450 14,258 811 2,617 2,949 70,001 
2039 35,130 -1,385 15,353 14,416 800 2,641 2,935 69,889 
2040 34,983 -1,410 15,257 14,574 789 2,664 2,921 69,777 
2041 34,815 -1,341 15,268 14,739 790 2,696 2,889 69,856 
2042 34,648 -1,272 15,278 14,905 791 2,727 2,858 69,935 
2043 34,481 -1,203 15,289 15,070 792 2,758 2,826 70,014 
2044 34,314 -1,134 15,300 15,236 793 2,789 2,795 70,093 
2045 34,146 -1,065 15,311 15,402 794 2,821 2,763 70,172 
2046 33,915 -1,037 15,311 15,552 795 2,851 2,752 70,140 
2047 33,684 -1,009 15,310 15,703 796 2,881 2,742 70,108 
2048 33,453 -981 15,310 15,854 797 2,912 2,731 70,077 
2049 33,222 -953 15,310 16,005 797 2,942 2,721 70,045 
2050 32,991 -925 15,310 16,156 798 2,972 2,710 70,013 
Total 1,101,029 -30,051 487,331 426,379 25,753 78,862 84,370 2,173,673 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-96 
Table C-4.29. Global Emissions Summary for Defined Policies: Low U.S. Supply: Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,357 396 18,210 11,671 887 2,123 2,244 73,889 
2021 37,883 472 17,618 11,723 877 2,151 2,266 72,990 
2022 37,409 548 17,027 11,775 867 2,179 2,287 72,092 
2023 36,935 625 16,435 11,827 857 2,206 2,308 71,193 
2024 36,461 701 15,843 11,878 847 2,234 2,330 70,295 
2025 35,987 777 15,252 11,930 837 2,261 2,351 69,396 
2026 36,080 93 15,357 12,122 845 2,294 2,456 69,246 
2027 36,173 -591 15,462 12,314 852 2,326 2,560 69,097 
2028 36,266 -1,275 15,568 12,506 860 2,358 2,665 68,947 
2029 36,359 -1,959 15,673 12,697 868 2,391 2,769 68,797 
2030 36,452 -2,643 15,778 12,889 875 2,423 2,873 68,648 
2031 36,273 -2,357 15,764 13,068 869 2,448 2,896 68,962 
2032 36,094 -2,071 15,750 13,248 863 2,473 2,919 69,276 
2033 35,915 -1,785 15,736 13,427 856 2,498 2,943 69,590 
2034 35,736 -1,498 15,722 13,606 850 2,523 2,966 69,904 
2035 35,557 -1,212 15,707 13,785 844 2,548 2,989 70,218 
2036 35,385 -1,232 15,609 13,943 833 2,571 2,974 70,083 
2037 35,213 -1,251 15,510 14,100 822 2,595 2,959 69,949 
2038 35,041 -1,271 15,412 14,258 811 2,619 2,944 69,814 
2039 34,869 -1,290 15,313 14,416 800 2,643 2,930 69,680 
2040 34,696 -1,310 15,215 14,574 789 2,667 2,915 69,546 
2041 34,506 -1,230 15,227 14,739 790 2,699 2,883 69,615 
2042 34,315 -1,149 15,240 14,905 791 2,730 2,851 69,683 
2043 34,124 -1,068 15,252 15,070 792 2,762 2,820 69,752 
2044 33,934 -988 15,265 15,236 794 2,793 2,788 69,821 
2045 33,743 -907 15,277 15,401 795 2,825 2,756 69,890 
2046 33,518 -904 15,281 15,552 795 2,856 2,746 69,844 
2047 33,294 -901 15,284 15,703 796 2,886 2,735 69,798 
2048 33,070 -898 15,288 15,854 796 2,917 2,725 69,751 
2049 32,845 -895 15,292 16,005 797 2,947 2,715 69,705 
2050 32,621 -892 15,295 16,155 798 2,978 2,704 69,659 
Total 1,095,112 -27,967 486,663 426,377 25,755 78,923 84,267 2,169,129 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-97 
Table C-4.30. Global Emissions Summary for Defined Policies: Low U.S. Supply: Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,357 396 18,210 11,671 887 2,123 2,244 73,889 
2021 37,883 472 17,618 11,723 877 2,151 2,266 72,990 
2022 37,409 548 17,027 11,775 867 2,179 2,287 72,092 
2023 36,935 625 16,435 11,827 857 2,206 2,308 71,193 
2024 36,461 701 15,843 11,878 847 2,234 2,330 70,295 
2025 35,987 777 15,252 11,930 837 2,261 2,351 69,396 
2026 36,080 93 15,357 12,122 845 2,294 2,456 69,246 
2027 36,173 -591 15,462 12,314 852 2,326 2,560 69,097 
2028 36,266 -1,275 15,568 12,506 860 2,358 2,665 68,947 
2029 36,359 -1,959 15,673 12,697 868 2,391 2,769 68,797 
2030 36,452 -2,643 15,778 12,889 875 2,423 2,873 68,648 
2031 36,273 -2,357 15,764 13,068 869 2,448 2,896 68,962 
2032 36,094 -2,071 15,750 13,248 863 2,473 2,919 69,276 
2033 35,915 -1,785 15,736 13,427 856 2,498 2,943 69,590 
2034 35,736 -1,498 15,722 13,606 850 2,523 2,966 69,904 
2035 35,557 -1,212 15,707 13,785 844 2,548 2,989 70,218 
2036 35,386 -1,232 15,609 13,943 833 2,571 2,974 70,084 
2037 35,214 -1,252 15,511 14,100 822 2,595 2,959 69,949 
2038 35,043 -1,273 15,412 14,258 811 2,619 2,944 69,815 
2039 34,871 -1,293 15,314 14,416 800 2,643 2,930 69,681 
2040 34,700 -1,313 15,216 14,574 789 2,667 2,915 69,547 
2041 34,511 -1,234 15,227 14,739 790 2,698 2,883 69,616 
2042 34,323 -1,156 15,239 14,905 791 2,730 2,852 69,684 
2043 34,135 -1,077 15,251 15,070 792 2,762 2,820 69,753 
2044 33,946 -999 15,263 15,236 794 2,793 2,788 69,821 
2045 33,758 -920 15,275 15,401 795 2,825 2,757 69,890 
2046 33,536 -918 15,278 15,552 795 2,855 2,746 69,844 
2047 33,314 -916 15,281 15,703 796 2,886 2,736 69,799 
2048 33,091 -914 15,284 15,854 796 2,916 2,726 69,754 
2049 32,869 -912 15,288 16,005 797 2,947 2,715 69,708 
2050 32,647 -910 15,291 16,156 797 2,977 2,705 69,663 
Total 1,095,283 -28,098 486,640 426,377 25,753 78,919 84,273 2,169,147 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-98 
Table C-4.31. Global Emissions Summary for Commitments (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 35,054 732 14,948 12,093 825 2,277 2,424 68,351 
2027 34,907 511 15,036 12,288 834 2,301 2,521 68,399 
2028 34,760 291 15,125 12,484 844 2,326 2,618 68,446 
2029 34,613 70 15,214 12,679 853 2,350 2,714 68,493 
2030 34,466 -150 15,303 12,874 863 2,374 2,811 68,541 
2031 33,137 -124 15,060 13,014 842 2,401 2,802 67,133 
2032 31,809 -98 14,817 13,155 820 2,428 2,794 65,725 
2033 30,480 -72 14,575 13,295 799 2,455 2,786 64,317 
2034 29,152 -46 14,332 13,436 777 2,482 2,777 62,909 
2035 27,823 -20 14,089 13,576 756 2,509 2,769 61,501 
2036 26,519 180 13,921 13,719 747 2,530 2,749 60,365 
2037 25,215 380 13,753 13,862 738 2,551 2,730 59,228 
2038 23,910 580 13,584 14,004 729 2,572 2,711 58,091 
2039 22,606 781 13,416 14,147 720 2,594 2,691 56,954 
2040 21,302 981 13,248 14,289 711 2,615 2,672 55,817 
2041 19,994 871 12,937 14,410 694 2,627 2,547 54,079 
2042 18,685 762 12,626 14,530 677 2,638 2,422 52,340 
2043 17,377 652 12,315 14,650 660 2,650 2,297 50,601 
2044 16,069 542 12,004 14,771 643 2,662 2,172 48,863 
2045 14,760 433 11,693 14,891 626 2,674 2,047 47,124 
2046 13,473 250 11,448 15,026 610 2,686 1,971 45,463 
2047 12,186 67 11,202 15,161 594 2,698 1,894 43,802 
2048 10,898 -116 10,957 15,296 578 2,710 1,818 42,141 
2049 9,611 -299 10,712 15,430 562 2,722 1,742 40,479 
2050 8,324 -481 10,466 15,565 545 2,734 1,665 38,818 
Total 807,730 11,127 431,956 419,349 23,148 76,699 74,856 1,844,865 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-99 
Table C -4.32. Global Emissions Summary for Commitments (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 35,054 732 14,948 12,093 825 2,277 2,424 68,351 
2027 34,907 511 15,036 12,288 834 2,301 2,521 68,399 
2028 34,760 291 15,125 12,484 844 2,326 2,618 68,446 
2029 34,613 70 15,214 12,679 853 2,350 2,714 68,493 
2030 34,466 -150 15,303 12,874 863 2,374 2,811 68,541 
2031 33,137 -124 15,060 13,014 842 2,401 2,802 67,133 
2032 31,809 -98 14,817 13,155 820 2,428 2,794 65,725 
2033 30,480 -72 14,575 13,295 799 2,455 2,786 64,317 
2034 29,152 -46 14,332 13,436 777 2,482 2,777 62,909 
2035 27,823 -20 14,089 13,576 756 2,509 2,769 61,501 
2036 26,524 172 13,921 13,719 747 2,530 2,750 60,362 
2037 25,224 365 13,753 13,861 738 2,551 2,730 59,222 
2038 23,925 557 13,584 14,004 729 2,572 2,711 58,082 
2039 22,625 750 13,416 14,147 719 2,594 2,692 56,943 
2040 21,326 942 13,248 14,289 710 2,615 2,673 55,803 
2041 20,015 845 12,935 14,410 693 2,626 2,548 54,072 
2042 18,705 747 12,621 14,530 677 2,638 2,423 52,341 
2043 17,395 650 12,307 14,650 660 2,650 2,298 50,610 
2044 16,084 552 11,994 14,771 643 2,662 2,173 48,879 
2045 14,774 455 11,680 14,891 626 2,673 2,048 47,147 
2046 13,485 269 11,433 15,026 610 2,685 1,971 45,480 
2047 12,195 84 11,186 15,161 594 2,697 1,895 43,812 
2048 10,906 -102 10,939 15,296 578 2,709 1,818 42,144 
2049 9,617 -287 10,692 15,431 562 2,721 1,742 40,477 
2050 8,328 -473 10,445 15,565 545 2,733 1,666 38,809 
Total 807,928 11,069 431,827 419,349 23,147 76,696 74,867 1,844,882 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-100 
Table C-4.33. Global Emissions Summary for Commitments (High CCS): High Exports (GCAM -
NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 35,054 732 14,948 12,093 825 2,277 2,424 68,351 
2027 34,907 511 15,036 12,288 834 2,301 2,521 68,399 
2028 34,760 291 15,125 12,484 844 2,326 2,618 68,446 
2029 34,613 70 15,214 12,679 853 2,350 2,714 68,493 
2030 34,466 -150 15,303 12,874 863 2,374 2,811 68,541 
2031 33,155 -141 15,063 13,014 842 2,401 2,803 67,136 
2032 31,843 -132 14,824 13,155 820 2,428 2,795 65,732 
2033 30,532 -123 14,584 13,295 799 2,454 2,787 64,327 
2034 29,220 -114 14,345 13,436 777 2,481 2,779 62,923 
2035 27,909 -105 14,105 13,576 755 2,507 2,771 61,518 
2036 26,603 104 13,934 13,719 746 2,529 2,752 60,386 
2037 25,297 313 13,762 13,861 737 2,550 2,733 59,253 
2038 23,991 522 13,591 14,004 728 2,571 2,714 58,121 
2039 22,685 731 13,420 14,146 719 2,592 2,695 56,988 
2040 21,379 941 13,248 14,289 710 2,614 2,676 55,856 
2041 20,064 852 12,931 14,409 693 2,626 2,550 54,125 
2042 18,749 764 12,614 14,530 677 2,637 2,425 52,395 
2043 17,434 675 12,296 14,650 660 2,649 2,300 50,665 
2044 16,119 587 11,979 14,771 643 2,661 2,175 48,934 
2045 14,804 499 11,662 14,891 626 2,673 2,049 47,204 
2046 13,513 305 11,411 15,026 610 2,685 1,973 45,523 
2047 12,222 112 11,161 15,161 594 2,697 1,896 43,843 
2048 10,932 -81 10,910 15,296 578 2,709 1,820 42,162 
2049 9,641 -275 10,659 15,431 561 2,721 1,743 40,482 
2050 8,350 -468 10,409 15,566 545 2,733 1,667 38,801 
Total 808,839 10,870 431,707 419,348 23,143 76,678 74,905 1,845,490 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-101 
Table C -4.34. Global Emissions Summary for Commitments (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 35,046 503 14,501 12,000 804 2,266 2,381 67,501 
2027 34,902 279 14,587 12,202 815 2,291 2,478 67,554 
2028 34,758 55 14,673 12,403 827 2,317 2,575 67,608 
2029 34,613 -169 14,759 12,605 838 2,342 2,673 67,661 
2030 34,469 -393 14,845 12,806 850 2,367 2,770 67,714 
2031 33,184 -563 14,451 12,914 824 2,385 2,734 65,928 
2032 31,899 -732 14,058 13,021 797 2,402 2,697 64,143 
2033 30,614 -902 13,664 13,128 771 2,420 2,661 62,357 
2034 29,328 -1,071 13,271 13,236 745 2,438 2,625 60,571 
2035 28,043 -1,241 12,877 13,343 718 2,455 2,589 58,785 
2036 26,739 -1,576 12,588 13,462 702 2,466 2,545 56,926 
2037 25,436 -1,911 12,299 13,580 685 2,477 2,501 55,068 
2038 24,132 -2,246 12,010 13,699 669 2,488 2,457 53,209 
2039 22,829 -2,582 11,721 13,817 653 2,499 2,413 51,350 
2040 21,525 -2,917 11,432 13,935 636 2,511 2,369 49,492 
2041 20,204 -2,775 11,156 14,077 621 2,520 2,281 48,084 
2042 18,882 -2,633 10,880 14,218 606 2,530 2,192 46,676 
2043 17,561 -2,491 10,603 14,359 591 2,540 2,104 45,269 
2044 16,240 -2,349 10,327 14,501 576 2,550 2,015 43,861 
2045 14,918 -2,206 10,051 14,642 561 2,560 1,927 42,453 
2046 13,607 -2,224 9,846 14,791 553 2,575 1,869 41,017 
2047 12,295 -2,241 9,642 14,940 545 2,589 1,812 39,581 
2048 10,984 -2,258 9,437 15,089 536 2,603 1,754 38,145 
2049 9,673 -2,275 9,232 15,237 528 2,618 1,697 36,709 
2050 8,361 -2,293 9,027 15,386 520 2,632 1,639 35,273 
Total 810,811 -35,428 399,778 413,798 22,005 74,944 71,342 1,757,251 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-102 
Table C-4.35. Global Emissions Summary for Commitments (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 35,046 503 14,501 12,000 804 2,266 2,381 67,501 
2027 34,902 279 14,587 12,202 815 2,291 2,478 67,554 
2028 34,758 55 14,673 12,403 827 2,317 2,575 67,608 
2029 34,613 -169 14,759 12,605 838 2,342 2,673 67,661 
2030 34,469 -393 14,845 12,806 850 2,367 2,770 67,714 
2031 33,184 -563 14,451 12,914 824 2,385 2,734 65,928 
2032 31,899 -732 14,058 13,021 797 2,402 2,697 64,143 
2033 30,614 -902 13,664 13,128 771 2,420 2,661 62,357 
2034 29,328 -1,071 13,271 13,236 745 2,438 2,625 60,571 
2035 28,043 -1,241 12,877 13,343 718 2,455 2,589 58,785 
2036 26,741 -1,576 12,588 13,462 702 2,466 2,545 56,928 
2037 25,438 -1,911 12,299 13,580 685 2,477 2,501 55,071 
2038 24,136 -2,246 12,010 13,699 669 2,488 2,457 53,214 
2039 22,834 -2,581 11,721 13,817 653 2,500 2,414 51,357 
2040 21,531 -2,916 11,432 13,936 636 2,511 2,370 49,500 
2041 20,210 -2,774 11,155 14,077 621 2,520 2,281 48,091 
2042 18,889 -2,632 10,878 14,218 606 2,530 2,193 46,682 
2043 17,567 -2,489 10,600 14,359 591 2,540 2,104 45,273 
2044 16,246 -2,347 10,323 14,501 576 2,550 2,016 43,864 
2045 14,925 -2,205 10,046 14,642 561 2,560 1,927 42,456 
2046 13,613 -2,223 9,841 14,791 553 2,575 1,870 41,018 
2047 12,301 -2,241 9,636 14,940 545 2,589 1,812 39,581 
2048 10,989 -2,258 9,430 15,089 536 2,603 1,754 38,143 
2049 9,677 -2,276 9,225 15,238 528 2,618 1,697 36,706 
2050 8,365 -2,294 9,020 15,386 520 2,632 1,639 35,268 
Total 810,883 -35,419 399,732 413,799 22,005 74,944 71,345 1,757,289 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-103 
Table C -4.36. Global Emissions Summary for Commitments (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 35,046 503 14,501 12,000 804 2,266 2,381 67,501 
2027 34,902 279 14,587 12,202 815 2,291 2,478 67,554 
2028 34,758 55 14,673 12,403 827 2,317 2,575 67,608 
2029 34,613 -169 14,759 12,605 838 2,342 2,673 67,661 
2030 34,469 -393 14,845 12,806 850 2,367 2,770 67,714 
2031 33,193 -560 14,454 12,914 824 2,385 2,734 65,943 
2032 31,917 -728 14,063 13,021 797 2,402 2,698 64,171 
2033 30,641 -895 13,672 13,128 771 2,420 2,662 62,400 
2034 29,365 -1,063 13,282 13,236 745 2,438 2,627 60,629 
2035 28,088 -1,230 12,891 13,343 719 2,455 2,591 58,857 
2036 26,783 -1,566 12,598 13,462 702 2,467 2,547 56,992 
2037 25,478 -1,903 12,305 13,580 686 2,478 2,503 55,127 
2038 24,173 -2,239 12,012 13,699 669 2,489 2,459 53,262 
2039 22,868 -2,575 11,719 13,817 653 2,500 2,415 51,396 
2040 21,563 -2,912 11,426 13,936 636 2,511 2,372 49,531 
2041 20,245 -2,770 11,146 14,077 621 2,520 2,283 48,124 
2042 18,928 -2,628 10,866 14,218 606 2,530 2,194 46,716 
2043 17,610 -2,486 10,587 14,360 591 2,540 2,106 45,308 
2044 16,293 -2,344 10,307 14,501 576 2,550 2,017 43,901 
2045 14,975 -2,201 10,028 14,642 561 2,560 1,928 42,493 
2046 13,670 -2,220 9,822 14,791 553 2,574 1,871 41,061 
2047 12,366 -2,239 9,616 14,940 544 2,589 1,813 39,630 
2048 11,061 -2,257 9,410 15,089 536 2,603 1,756 38,198 
2049 9,757 -2,276 9,204 15,238 528 2,617 1,698 36,766 
2050 8,452 -2,295 8,998 15,387 519 2,632 1,641 35,334 
Total 811,784 -35,330 399,610 413,805 22,006 74,943 71,375 1,758,194 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-104 
Table C-4.37. Global Emissions Summary for Net Zero 2050 (High CCS): Existing/FID Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 33,725 423 14,586 12,033 798 2,275 2,384 66,223 
2027 32,250 -107 14,313 12,168 781 2,297 2,441 64,143 
2028 30,775 -636 14,041 12,303 764 2,319 2,498 62,063 
2029 29,300 -1,166 13,768 12,437 746 2,341 2,555 59,982 
2030 27,825 -1,695 13,495 12,572 729 2,364 2,611 57,902 
2031 26,373 -1,180 13,363 12,727 723 2,391 2,606 57,002 
2032 24,922 -666 13,231 12,881 717 2,418 2,600 56,103 
2033 23,471 -151 13,099 13,036 710 2,445 2,594 55,204 
2034 22,020 364 12,967 13,190 704 2,472 2,588 54,305 
2035 20,568 878 12,835 13,344 698 2,499 2,582 53,405 
2036 19,212 727 12,527 13,463 679 2,512 2,530 51,650 
2037 17,856 577 12,218 13,581 660 2,524 2,479 49,895 
2038 16,500 426 11,910 13,699 640 2,537 2,427 48,139 
2039 15,143 275 11,602 13,817 621 2,549 2,375 46,384 
2040 13,787 125 11,294 13,936 602 2,562 2,323 44,629 
2041 12,431 178 11,098 14,089 591 2,574 2,240 43,200 
2042 11,074 231 10,902 14,243 581 2,586 2,156 41,772 
2043 9,717 284 10,707 14,396 570 2,598 2,073 40,344 
2044 8,360 337 10,511 14,550 559 2,610 1,989 38,916 
2045 7,004 389 10,315 14,703 549 2,622 1,906 37,488 
2046 5,611 360 10,054 14,864 541 2,633 1,848 35,912 
2047 4,218 330 9,793 15,026 533 2,645 1,791 34,336 
2048 2,824 301 9,532 15,187 526 2,657 1,733 32,760 
2049 1,431 271 9,271 15,348 518 2,669 1,676 31,184 
2050 38 242 9,010 15,510 510 2,680 1,619 29,609 
Total 637,037 5,568 395,621 413,805 21,153 75,913 70,336 1,619,433 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-105 
Table C -4.38. Global Emissions Summary for Net Zero 2050 (High CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 33,725 423 14,586 12,033 798 2,275 2,384 66,223 
2027 32,250 -107 14,313 12,168 781 2,297 2,441 64,143 
2028 30,775 -636 14,041 12,303 764 2,319 2,498 62,063 
2029 29,300 -1,166 13,768 12,437 746 2,341 2,555 59,982 
2030 27,825 -1,695 13,495 12,572 729 2,364 2,611 57,902 
2031 26,373 -1,181 13,363 12,727 723 2,391 2,606 57,002 
2032 24,922 -666 13,231 12,881 717 2,418 2,600 56,103 
2033 23,471 -151 13,099 13,036 710 2,445 2,594 55,204 
2034 22,019 363 12,967 13,190 704 2,472 2,588 54,304 
2035 20,568 878 12,835 13,344 698 2,499 2,582 53,405 
2036 19,214 723 12,526 13,463 679 2,512 2,531 51,647 
2037 17,860 567 12,218 13,581 660 2,524 2,479 49,889 
2038 16,506 412 11,910 13,699 640 2,537 2,427 48,131 
2039 15,152 257 11,601 13,817 621 2,549 2,376 46,373 
2040 13,799 101 11,293 13,935 602 2,561 2,324 44,615 
2041 12,440 162 11,096 14,089 591 2,573 2,240 43,193 
2042 11,082 224 10,899 14,242 581 2,585 2,157 41,770 
2043 9,724 285 10,702 14,396 570 2,597 2,073 40,347 
2044 8,365 346 10,505 14,550 559 2,609 1,989 38,924 
2045 7,007 407 10,308 14,703 549 2,621 1,906 37,501 
2046 5,614 374 10,046 14,864 541 2,633 1,848 35,921 
2047 4,220 341 9,785 15,026 533 2,645 1,791 34,341 
2048 2,826 308 9,523 15,187 526 2,657 1,734 32,761 
2049 1,433 275 9,262 15,348 518 2,668 1,676 31,181 
2050 39 242 9,000 15,510 510 2,680 1,619 29,601 
Total 637,113 5,540 395,547 413,805 21,152 75,911 70,340 1,619,408 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-106 
Table C-4.39. Global Emissions Summary for Net Zero 2050 (High CCS): High Exports (GCAM-
NETL-Aligned, AR6-20 Basis) 
Year CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,707 616 17,531 11,716 872 2,151 2,260 72,853 
2022 37,080 700 16,863 11,761 857 2,177 2,277 71,716 
2023 36,454 784 16,195 11,807 843 2,202 2,294 70,579 
2024 35,827 868 15,527 11,852 829 2,227 2,311 69,441 
2025 35,200 952 14,859 11,898 815 2,252 2,327 68,304 
2026 33,725 423 14,586 12,033 798 2,275 2,384 66,223 
2027 32,250 -107 14,313 12,168 781 2,297 2,441 64,143 
2028 30,775 -636 14,041 12,303 764 2,319 2,498 62,063 
2029 29,300 -1,166 13,768 12,437 746 2,341 2,555 59,982 
2030 27,825 -1,695 13,495 12,572 729 2,364 2,611 57,902 
2031 26,382 -1,196 13,366 12,727 723 2,391 2,606 56,998 
2032 24,939 -697 13,236 12,881 716 2,418 2,601 56,094 
2033 23,496 -197 13,106 13,035 710 2,445 2,595 55,190 
2034 22,053 302 12,976 13,190 704 2,472 2,590 54,286 
2035 20,610 801 12,846 13,344 697 2,499 2,585 53,382 
2036 19,256 662 12,535 13,462 678 2,511 2,533 51,636 
2037 17,901 522 12,223 13,580 659 2,523 2,481 49,891 
2038 16,547 382 11,912 13,699 640 2,536 2,430 48,145 
2039 15,193 243 11,601 13,817 621 2,548 2,378 46,400 
2040 13,839 103 11,289 13,935 602 2,560 2,326 44,654 
2041 12,477 173 11,089 14,089 591 2,573 2,242 43,234 
2042 11,115 243 10,888 14,242 581 2,585 2,159 41,813 
2043 9,754 313 10,688 14,396 570 2,597 2,075 40,392 
2044 8,392 383 10,487 14,550 560 2,609 1,991 38,971 
2045 7,030 453 10,287 14,703 549 2,621 1,907 37,551 
2046 5,634 407 10,024 14,865 541 2,632 1,850 35,952 
2047 4,237 360 9,761 15,026 533 2,644 1,792 34,354 
2048 2,841 313 9,497 15,187 525 2,656 1,735 32,755 
2049 1,444 267 9,234 15,349 518 2,668 1,677 31,157 
2050 48 220 8,971 15,510 510 2,679 1,620 29,558 
Total 637,664 5,330 395,394 413,802 21,148 75,896 70,374 1,619,609 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-107 
Table C -4.40. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Existing/FID 
Exports (GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 33,730 76 14,012 11,903 774 2,258 2,324 65,077 
2027 32,270 -576 13,609 12,007 757 2,276 2,364 62,706 
2028 30,810 -1,227 13,206 12,110 739 2,293 2,404 60,335 
2029 29,350 -1,879 12,802 12,214 721 2,310 2,444 57,963 
2030 27,890 -2,531 12,399 12,318 703 2,328 2,484 55,592 
2031 26,507 -2,788 12,074 12,445 685 2,338 2,461 53,721 
2032 25,124 -3,046 11,748 12,572 668 2,348 2,437 51,850 
2033 23,741 -3,304 11,422 12,698 650 2,358 2,414 49,979 
2034 22,357 -3,561 11,097 12,825 632 2,368 2,390 48,108 
2035 20,974 -3,819 10,771 12,952 614 2,378 2,367 46,237 
2036 19,593 -3,575 10,567 13,106 601 2,391 2,341 45,024 
2037 18,213 -3,331 10,362 13,259 588 2,404 2,316 43,811 
2038 16,832 -3,088 10,158 13,413 575 2,417 2,290 42,597 
2039 15,451 -2,844 9,954 13,566 562 2,430 2,264 41,384 
2040 14,071 -2,600 9,750 13,720 549 2,442 2,239 40,171 
2041 12,712 -2,738 9,466 13,871 541 2,449 2,165 38,466 
2042 11,352 -2,876 9,182 14,022 533 2,456 2,091 36,760 
2043 9,993 -3,014 8,898 14,174 524 2,463 2,017 35,055 
2044 8,634 -3,152 8,614 14,325 516 2,470 1,943 33,350 
2045 7,275 -3,290 8,330 14,476 508 2,477 1,869 31,645 
2046 5,865 -2,831 8,122 14,645 504 2,494 1,823 30,621 
2047 4,455 -2,373 7,914 14,814 500 2,510 1,776 29,597 
2048 3,045 -1,914 7,706 14,984 496 2,527 1,730 28,573 
2049 1,635 -1,455 7,498 15,153 492 2,544 1,683 27,549 
2050 225 -996 7,290 15,322 488 2,561 1,636 26,525 
Total 642,673 -58,952 354,789 407,301 19,953 73,393 67,855 1,507,012 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-108 
Table C-4.41. Global Emissions Summary for Net Zero 2050 (Moderate CCS): Model Resolved 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 33,730 76 14,012 11,903 774 2,258 2,324 65,077 
2027 32,270 -576 13,609 12,007 757 2,276 2,364 62,706 
2028 30,810 -1,227 13,206 12,110 739 2,293 2,404 60,335 
2029 29,350 -1,879 12,802 12,214 721 2,310 2,444 57,963 
2030 27,890 -2,531 12,399 12,318 703 2,328 2,484 55,592 
2031 26,507 -2,788 12,074 12,445 685 2,338 2,461 53,721 
2032 25,124 -3,046 11,748 12,572 668 2,348 2,437 51,850 
2033 23,741 -3,304 11,422 12,698 650 2,358 2,414 49,979 
2034 22,357 -3,561 11,097 12,825 632 2,368 2,390 48,108 
2035 20,974 -3,819 10,771 12,952 614 2,378 2,367 46,237 
2036 19,593 -3,575 10,567 13,106 601 2,391 2,341 45,024 
2037 18,213 -3,331 10,362 13,259 588 2,404 2,316 43,811 
2038 16,832 -3,088 10,158 13,413 575 2,417 2,290 42,597 
2039 15,451 -2,844 9,954 13,566 562 2,430 2,264 41,384 
2040 14,071 -2,600 9,750 13,720 549 2,442 2,239 40,171 
2041 12,712 -2,738 9,466 13,871 541 2,449 2,165 38,466 
2042 11,352 -2,876 9,182 14,022 533 2,456 2,091 36,760 
2043 9,993 -3,014 8,898 14,174 524 2,463 2,017 35,055 
2044 8,634 -3,152 8,614 14,325 516 2,470 1,943 33,350 
2045 7,275 -3,290 8,330 14,476 508 2,477 1,869 31,645 
2046 5,865 -2,831 8,122 14,645 504 2,494 1,823 30,621 
2047 4,455 -2,373 7,914 14,814 500 2,510 1,776 29,597 
2048 3,045 -1,914 7,706 14,984 496 2,527 1,730 28,573 
2049 1,635 -1,455 7,498 15,153 492 2,544 1,683 27,549 
2050 225 -996 7,290 15,322 488 2,561 1,636 26,525 
Total 642,673 -58,952 354,789 407,301 19,953 73,393 67,855 1,507,012 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-109 
Table C -4.42. Global Emissions Summary for Net Zero 2050 (Moderate CCS): High Exports 
(GCAM-NETL-Aligned, AR6-20 Basis) 
Year 
CO2 Energy CO2 LUC CH4 Energy  CH4 Ag N2O Energy N2O Ag F Gases Total 
Units (Tg CO2e/year) (AR6, 20-year) 
2020 38,333 532 18,199 11,670 886 2,126 2,244 73,991 
2021 37,705 571 17,443 11,696 867 2,149 2,252 72,682 
2022 37,076 610 16,686 11,722 848 2,172 2,260 71,374 
2023 36,447 650 15,929 11,747 829 2,195 2,268 70,065 
2024 35,818 689 15,172 11,773 811 2,218 2,276 68,756 
2025 35,190 728 14,415 11,799 792 2,241 2,284 67,448 
2026 33,730 76 14,012 11,903 774 2,258 2,324 65,077 
2027 32,270 -576 13,609 12,007 757 2,276 2,364 62,706 
2028 30,810 -1,227 13,206 12,110 739 2,293 2,404 60,335 
2029 29,350 -1,879 12,802 12,214 721 2,310 2,444 57,963 
2030 27,890 -2,531 12,399 12,318 703 2,328 2,484 55,592 
2031 26,518 -2,796 12,076 12,445 685 2,338 2,461 53,727 
2032 25,145 -3,060 11,752 12,571 668 2,348 2,438 51,862 
2033 23,773 -3,325 11,428 12,698 650 2,358 2,415 49,996 
2034 22,401 -3,590 11,105 12,825 632 2,368 2,392 48,131 
2035 21,028 -3,855 10,781 12,951 614 2,378 2,369 46,266 
2036 19,652 -3,604 10,575 13,105 601 2,391 2,343 45,062 
2037 18,275 -3,354 10,369 13,259 588 2,404 2,317 43,859 
2038 16,899 -3,103 10,164 13,412 575 2,416 2,292 42,656 
2039 15,523 -2,852 9,958 13,566 562 2,429 2,266 41,452 
2040 14,146 -2,601 9,752 13,720 549 2,442 2,241 40,249 
2041 12,789 -2,740 9,464 13,871 541 2,449 2,167 38,539 
2042 11,432 -2,879 9,175 14,022 532 2,456 2,092 36,830 
2043 10,075 -3,018 8,887 14,173 524 2,463 2,018 35,121 
2044 8,717 -3,158 8,598 14,324 516 2,470 1,944 33,412 
2045 7,360 -3,297 8,310 14,475 508 2,477 1,870 31,702 
2046 5,959 -2,853 8,099 14,644 504 2,493 1,823 30,669 
2047 4,557 -2,410 7,888 14,813 500 2,510 1,776 29,635 
2048 3,156 -1,966 7,678 14,982 496 2,527 1,730 28,601 
2049 1,754 -1,523 7,467 15,151 491 2,543 1,683 27,567 
2050 353 -1,079 7,256 15,320 487 2,560 1,636 26,534 
Total 644,132 -59,419 354,650 407,283 19,949 73,386 67,876 1,507,858 
Note: Emissions shown have been interpolated for non-model years.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-110 
C. Summary Consequential Result Tables 
The remaining tables summarize values of U.S. LNG Exports and GHG emissions used for 
calculating the consequential GHG intensity and PNDE factors on an annual and cumulative basis 
for all scenarios (including sensitivity scenarios) in the Consequential Analysis Appendix. 
Note: U.S. LNG export and GHG emissions values were interpolated for non-model years. Also, 
consequential and PNDE results have been removed from these tables for years with zero or 
near-zero changes in GHG emissions or U.S. LNG exports that lead to extraneous annual results.

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-111 
Table C-4.43. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Defined Policies Scenarios (AR6-100 Basis) 
Year 
DP: ExFID   DP: MR DP: MR vs ExFID   DP: Hi Exp DP: Hi Exp vs ExFID 
US LNG GHG  US LNG GHG  LNG  GHG Cons GHG PNDE  US LNG GHG  LNG  GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,770  2.4 53,770 0.0 0.0      2.4 53,770 0.0 0.0     
2021 3.2 53,219  3.2 53,219 0.0 0.0      3.2 53,219 0.0 0.0     
2022 4.0 52,669  4.0 52,669 0.0 0.0      4.0 52,669 0.0 0.0     
2023 4.8 52,118  4.8 52,118 0.0 0.0      4.8 52,118 0.0 0.0     
2024 5.6 51,567  5.6 51,567 0.0 0.0      5.6 51,567 0.0 0.0     
2025 6.3 51,017  6.3 51,017 0.0 0.0      6.3 51,017 0.0 0.0     
2026 6.5 50,645  6.5 50,645 0.0 0.0      6.5 50,645 0.0 0.0     
2027 6.6 50,273  6.6 50,273 0.0 0.0      6.6 50,273 0.0 0.0     
2028 6.7 49,901  6.7 49,901 0.0 0.0      6.7 49,901 0.0 0.0     
2029 6.8 49,529  6.8 49,529 0.0 0.0      6.8 49,529 0.0 0.0     
2030 7.0 49,156  7.0 49,156 0.0 0.0      7.0 49,156 0.0 0.0     
2031 7.3 49,364  7.5 49,365 0.2 0.6 3.1 -11.4  7.8 49,365 0.6 1.3 2.4 -12.1 
2032 7.6 49,572  8.0 49,573 0.4 1.2 3.1 -11.4  8.7 49,574 1.1 2.7 2.4 -12.1 
2033 7.9 49,779  8.5 49,781 0.6 1.8 3.1 -11.4  9.6 49,783 1.7 4.0 2.4 -12.1 
2034 8.2 49,987  9.0 49,989 0.8 2.3 3.1 -11.4  10.4 49,992 2.2 5.3 2.4 -12.1 
2035 8.5 50,194  9.5 50,197 1.0 2.9 3.1 -11.4  11.3 50,201 2.8 6.7 2.4 -12.1 
2036 8.5 50,033  10.4 50,046 1.8 12.7 6.9 -7.6  12.5 50,062 4.0 29.3 7.3 -7.2 
2037 8.5 49,872  11.3 49,894 2.7 22.6 8.3 -6.3  13.8 49,924 5.3 51.8 9.9 -4.6 
2038 8.5 49,711  12.2 49,743 3.6 32.4 8.9 -5.6  15.0 49,785 6.5 74.4 11.5 -3.1 
2039 8.5 49,549  13.0 49,592 4.5 42.2 9.4 -5.2  16.3 49,647 7.7 97.0 12.5 -2.0 
2040 8.5 49,388  13.9 49,440 5.4 52.0 9.6 -4.9  17.5 49,508 9.0 119.6 13.3 -1.2 
2041 8.5 49,364  14.7 49,418 6.2 54.1 8.8 -5.7  18.7 49,483 10.1 119.1 11.8 -2.8 
2042 8.5 49,340  15.5 49,396 6.9 56.3 8.1 -6.4  19.8 49,458 11.3 118.6 10.5 -4.0 
2043 8.5 49,315  16.3 49,374 7.7 58.5 7.6 -6.9  20.9 49,433 12.4 118.1 9.5 -5.0 
2044 8.5 49,291  17.0 49,352 8.5 60.6 7.1 -7.4  22.1 49,409 13.5 117.6 8.7 -5.8 
2045 8.5 49,267  17.8 49,329 9.3 62.8 6.8 -7.7  23.2 49,384 14.7 117.1 8.0 -6.5 
2046 8.5 49,141  18.3 49,200 9.8 58.4 6.0 -8.5  24.1 49,250 15.5 109.3 7.0 -7.5 
2047 8.5 49,016  18.8 49,070 10.2 54.0 5.3 -9.3  24.9 49,117 16.4 101.5 6.2 -8.3 
2048 8.5 48,890  19.3 48,940 10.7 49.6 4.6 -9.9  25.8 48,984 17.2 93.8 5.4 -9.1 
2049 8.5 48,765  19.8 48,810 11.2 45.2 4.0 -10.5  26.6 48,851 18.1 86.0 4.8 -9.8 
2050 8.5 48,639  20.3 48,680 11.7 40.8 3.5 -11.0  27.5 48,717 18.9 78.2 4.1 -10.4 
Cum. 227 1,552,340  341 1,553,051 113 711 6.3 -8.2   416 1,553,792 189 1,452 7.7 -6.8

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-112 
Table C-4.44. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High Middle East Supply Scenarios (AR6-100 Basis) 
Year 
DP Hi ME Sup: 
ExFID   DP Hi ME Sup: MR DP Hi ME Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,780  2.4 53,780 0.0 0.0     
2021 3.2 53,230  3.2 53,230 0.0 0.0     
2022 4.0 52,681  4.0 52,681 0.0 0.0     
2023 4.8 52,131  4.8 52,131 0.0 0.0     
2024 5.6 51,582  5.6 51,582 0.0 0.0     
2025 6.3 51,032  6.3 51,032 0.0 0.0     
2026 6.5 50,662  6.5 50,662 0.0 0.0     
2027 6.6 50,291  6.6 50,291 0.0 0.0     
2028 6.8 49,921  6.8 49,921 0.0 0.0     
2029 6.9 49,551  6.9 49,551 0.0 0.0     
2030 7.1 49,180  7.1 49,180 0.0 0.0     
2031 7.4 49,401  7.6 49,402 0.2 0.5 2.2 -12.3 
2032 7.7 49,623  8.1 49,624 0.4 1.0 2.2 -12.3 
2033 8.0 49,844  8.6 49,845 0.7 1.5 2.2 -12.3 
2034 8.2 50,065  9.1 50,067 0.9 2.0 2.2 -12.3 
2035 8.5 50,286  9.7 50,288 1.1 2.5 2.2 -12.3 
2036 8.5 50,158  10.4 50,166 1.9 8.0 4.2 -10.3 
2037 8.5 50,030  11.2 50,044 2.6 13.4 5.1 -9.4 
2038 8.5 49,903  11.9 49,922 3.4 18.9 5.6 -9.0 
2039 8.5 49,775  12.7 49,799 4.1 24.3 5.9 -8.7 
2040 8.5 49,647  13.4 49,677 4.9 29.8 6.1 -8.4 
2041 8.5 49,635  14.1 49,666 5.5 30.8 5.6 -9.0 
2042 8.5 49,623  14.7 49,654 6.1 31.7 5.2 -9.4 
2043 8.5 49,610  15.3 49,643 6.8 32.7 4.8 -9.7 
2044 8.5 49,598  15.9 49,632 7.4 33.7 4.6 -10.0 
2045 8.5 49,586  16.5 49,620 8.0 34.7 4.3 -10.2 
2046 8.5 49,468  17.0 49,497 8.4 29.6 3.5 -11.0 
2047 8.5 49,350  17.4 49,375 8.8 24.5 2.8 -11.7 
2048 8.5 49,232  17.8 49,252 9.3 19.5 2.1 -12.4 
2049 8.5 49,114  18.2 49,129 9.7 14.4 1.5 -13.0 
2050 8.5 48,996   18.6 49,006 10.1 9.3 0.9 -13.6 
Cum. 228 1,556,984   329 1,557,347 100 363 3.6 -10.9

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-113 
 Table C-4.45. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High U.S. Supply Scenarios (AR6-100 Basis) 
Year 
DP Hi US Sup: 
ExFID   DP Hi US Sup: MR DP Hi US Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,766  2.4 53,766 0.0 0.0     
2021 3.2 53,216  3.2 53,216 0.0 0.0     
2022 4.0 52,667  4.0 52,667 0.0 0.0     
2023 4.8 52,117  4.8 52,117 0.0 0.0     
2024 5.6 51,568  5.6 51,568 0.0 0.0     
2025 6.3 51,019  6.3 51,019 0.0 0.0     
2026 6.5 50,647  6.5 50,647 0.0 0.0     
2027 6.6 50,276  6.6 50,276 0.0 0.0     
2028 6.8 49,905  6.8 49,905 0.0 0.0     
2029 6.9 49,534  6.9 49,534 0.0 0.0     
2030 7.0 49,162  7.0 49,162 0.0 0.0     
2031 7.3 49,371  7.6 49,372 0.3 0.8 2.8 -11.7 
2032 7.6 49,580  8.2 49,581 0.6 1.6 2.8 -11.7 
2033 7.9 49,788  8.8 49,791 0.9 2.4 2.8 -11.7 
2034 8.2 49,997  9.4 50,000 1.2 3.3 2.8 -11.7 
2035 8.5 50,205  10.0 50,209 1.5 4.1 2.8 -11.7 
2036 8.5 50,044  11.1 50,064 2.6 19.6 7.6 -6.9 
2037 8.5 49,883  12.2 49,918 3.7 35.2 9.5 -5.0 
2038 8.5 49,722  13.3 49,772 4.8 50.7 10.5 -4.0 
2039 8.5 49,560  14.5 49,627 5.9 66.2 11.2 -3.3 
2040 8.5 49,399  15.6 49,481 7.0 81.8 11.6 -2.9 
2041 8.5 49,377  16.7 49,463 8.2 85.1 10.4 -4.1 
2042 8.5 49,356  17.8 49,444 9.3 88.4 9.5 -5.0 
2043 8.5 49,334  18.9 49,425 10.4 91.7 8.8 -5.7 
2044 8.5 49,312  20.0 49,407 11.5 95.1 8.3 -6.3 
2045 8.5 49,290  21.1 49,388 12.6 98.4 7.8 -6.7 
2046 8.5 49,168  22.0 49,265 13.4 96.4 7.2 -7.3 
2047 8.5 49,047  22.8 49,141 14.2 94.4 6.6 -7.9 
2048 8.5 48,925  23.6 49,017 15.1 92.3 6.1 -8.4 
2049 8.5 48,803  24.4 48,894 15.9 90.3 5.7 -8.8 
2050 8.5 48,681   25.2 48,770 16.7 88.3 5.3 -9.2 
Cum. 228 1,552,720   383 1,553,906 156 1,186 7.6 -6.9

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-114 
Table C-4.46. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP Low U.S. Supply Scenarios (AR6-100 Basis) 
Year 
DP Lo US Sup: 
ExFID   DP Lo US Sup: MR DP Lo US Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,794  2.4 53,794 0.0 0.0     
2021 3.2 53,236  3.2 53,236 0.0 0.0     
2022 4.0 52,678  4.0 52,678 0.0 0.0     
2023 4.8 52,119  4.8 52,119 0.0 0.0     
2024 5.5 51,561  5.5 51,561 0.0 0.0     
2025 6.3 51,003  6.3 51,003 0.0 0.0     
2026 6.4 50,624  6.4 50,624 0.0 0.0     
2027 6.4 50,245  6.4 50,245 0.0 0.0     
2028 6.5 49,866  6.5 49,866 0.0 0.0     
2029 6.5 49,487  6.5 49,487 0.0 0.0     
2030 6.6 49,108  6.6 49,108 0.0 0.0     
2031 6.8 49,308  6.8 49,308 0.0 0.0     
2032 7.0 49,508  7.0 49,508 0.0 0.0     
2033 7.2 49,708  7.2 49,708 0.0 0.0     
2034 7.4 49,907  7.4 49,907 0.0 0.0     
2035 7.6 50,107  7.6 50,107 0.0 0.0     
2036 7.8 49,940  7.8 49,940 0.1 0.2 3.2 -11.3 
2037 8.0 49,773  8.1 49,774 0.1 0.5 3.2 -11.3 
2038 8.1 49,606  8.4 49,607 0.2 0.7 3.2 -11.3 
2039 8.3 49,439  8.6 49,440 0.3 1.0 3.2 -11.3 
2040 8.5 49,273  8.9 49,274 0.4 1.2 3.2 -11.3 
2041 8.5 49,243  9.1 49,244 0.6 1.2 2.0 -12.5 
2042 8.5 49,213  9.3 49,214 0.8 1.2 1.5 -13.1 
2043 8.5 49,183  9.6 49,184 1.0 1.2 1.1 -13.4 
2044 8.5 49,153  9.8 49,154 1.2 1.2 0.9 -13.6 
2045 8.5 49,123  10.0 49,124 1.5 1.2 0.8 -13.7 
2046 8.5 48,982  10.3 48,984 1.7 2.3 1.3 -13.2 
2047 8.5 48,841  10.5 48,845 2.0 3.4 1.7 -12.8 
2048 8.5 48,701  10.8 48,705 2.3 4.6 2.0 -12.5 
2049 8.5 48,560  11.1 48,566 2.5 5.7 2.3 -12.3 
2050 8.5 48,419   11.3 48,426 2.8 6.9 2.5 -12.1 
Cum. 221 1,549,708   238 1,549,740 18 32 1.8 -12.7

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-115 
Table C-4.47. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Commitments (High CCS) Scenarios (AR6-100 
Basis) 
Year 
C (High CCS): ExFID   C (High CCS): MR C (High CCS): MR vs ExFID   C (High CCS): Hi Exp C (High CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,903  2.4 53,903 0.0 0.0      2.4 53,903 0.0 0.0     
2021 3.2 53,160  3.2 53,160 0.0 0.0      3.2 53,160 0.0 0.0     
2022 4.0 52,417  4.0 52,417 0.0 0.0      4.0 52,417 0.0 0.0     
2023 4.8 51,674  4.8 51,674 0.0 0.0      4.8 51,674 0.0 0.0     
2024 5.6 50,931  5.6 50,931 0.0 0.0      5.6 50,931 0.0 0.0     
2025 6.3 50,188  6.3 50,188 0.0 0.0      6.3 50,188 0.0 0.0     
2026 6.4 50,016  6.4 50,016 0.0 0.0      6.4 50,016 0.0 0.0     
2027 6.5 49,845  6.5 49,845 0.0 0.0      6.5 49,845 0.0 0.0     
2028 6.5 49,674  6.5 49,674 0.0 0.0      6.5 49,674 0.0 0.0     
2029 6.6 49,502  6.6 49,502 0.0 0.0      6.6 49,502 0.0 0.0     
2030 6.7 49,331  6.7 49,331 0.0 0.0      6.7 49,331 0.0 0.0     
2031 6.9 47,989  6.9 47,989 0.0 0.0      7.3 47,991 0.4 1.6 4.4 -10.2 
2032 7.1 46,648  7.1 46,648 0.0 0.0      7.8 46,651 0.7 3.1 4.4 -10.2 
2033 7.3 45,306  7.3 45,306 0.0 0.0      8.4 45,311 1.1 4.7 4.4 -10.2 
2034 7.5 43,965  7.5 43,965 0.0 0.0      9.0 43,971 1.4 6.3 4.4 -10.2 
2035 7.8 42,623  7.8 42,623 0.0 0.0      9.6 42,631 1.8 7.8 4.4 -10.2 
2036 7.9 41,510  8.2 41,507 0.3 -2.8 -10.5 -25.0  10.3 41,524 2.4 14.1 5.8 -8.7 
2037 8.1 40,396  8.6 40,390 0.5 -5.7 -10.5 -25.0  11.1 40,416 3.1 20.3 6.6 -7.9 
2038 8.2 39,282  9.0 39,273 0.8 -8.5 -10.5 -25.0  11.9 39,308 3.7 26.5 7.2 -7.4 
2039 8.4 38,168  9.5 38,157 1.1 -11.4 -10.5 -25.0  12.7 38,201 4.3 32.7 7.6 -7.0 
2040 8.5 37,054  9.9 37,040 1.4 -14.2 -10.5 -25.0  13.5 37,093 5.0 38.9 7.8 -6.7 
2041 8.5 35,492  10.2 35,487 1.7 -5.1 -3.1 -17.6  14.2 35,543 5.6 51.0 9.1 -5.4 
2042 8.5 33,930  10.5 33,934 2.0 4.0 2.0 -12.5  14.8 33,993 6.3 63.2 10.0 -4.5 
2043 8.5 32,368  10.8 32,381 2.3 13.0 5.7 -8.8  15.5 32,443 7.0 75.3 10.8 -3.7 
2044 8.5 30,805  11.1 30,828 2.6 22.1 8.5 -6.0  16.2 30,893 7.6 87.4 11.5 -3.1 
2045 8.5 29,243  11.4 29,274 2.9 31.2 10.8 -3.7  16.8 29,343 8.3 99.5 12.0 -2.5 
2046 8.5 27,683  11.5 27,708 3.0 25.7 8.6 -5.9  17.3 27,766 8.8 83.3 9.5 -5.0 
2047 8.5 26,122  11.6 26,142 3.1 20.3 6.5 -8.0  17.8 26,189 9.2 67.1 7.3 -7.2 
2048 8.5 24,561  11.7 24,576 3.2 14.8 4.6 -9.9  18.2 24,612 9.7 50.9 5.3 -9.3 
2049 8.5 23,001  11.8 23,010 3.3 9.3 2.8 -11.7  18.7 23,036 10.1 34.6 3.4 -11.1 
2050 8.5 21,440   11.9 21,444 3.4 3.8 1.1 -13.4  19.1 21,459 10.6 18.4 1.7 -12.8 
Cum. 222 1,268,227   254 1,268,324 31 97 3.1 -11.4   329 1,269,014 107 787 7.3 -7.2

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-116 
 
Table C-4.48. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Commitments (Moderate CCS) Scenarios (AR6-
100 Basis) 
Year 
C (Mod CCS): ExFID   C (Mod CCS): MR C (Mod CCS): MR vs ExFID   C (Mod CCS): Hi Exp C (Mod CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG  LNG  GHG Cons GHG PNDE  US LNG GHG  LNG  GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,903  2.4 53,903 0.0 0.0      2.4 53,903 0.0 0.0     
2021 3.2 53,061  3.2 53,061 0.0 0.0      3.2 53,061 0.0 0.0     
2022 4.0 52,220  4.0 52,220 0.0 0.0      4.0 52,220 0.0 0.0     
2023 4.8 51,378  4.8 51,378 0.0 0.0      4.8 51,378 0.0 0.0     
2024 5.6 50,536  5.6 50,536 0.0 0.0      5.6 50,536 0.0 0.0     
2025 6.3 49,694  6.3 49,694 0.0 0.0      6.3 49,694 0.0 0.0     
2026 6.4 49,527  6.4 49,527 0.0 0.0      6.4 49,527 0.0 0.0     
2027 6.4 49,359  6.4 49,359 0.0 0.0      6.4 49,359 0.0 0.0     
2028 6.5 49,191  6.5 49,191 0.0 0.0      6.5 49,191 0.0 0.0     
2029 6.6 49,024  6.6 49,024 0.0 0.0      6.6 49,024 0.0 0.0     
2030 6.6 48,856  6.6 48,856 0.0 0.0      6.6 48,856 0.0 0.0     
2031 6.8 47,265  6.8 47,265 0.0 0.0      7.1 47,278 0.4 12.9 35.8 21.3 
2032 6.9 45,674  6.9 45,674 0.0 0.0      7.6 45,700 0.7 25.8 35.8 21.2 
2033 7.1 44,084  7.1 44,084 0.0 0.0      8.2 44,122 1.1 38.7 35.8 21.2 
2034 7.2 42,493  7.2 42,493 0.0 0.0      8.7 42,545 1.4 51.5 35.8 21.2 
2035 7.4 40,902  7.4 40,902 0.0 0.0      9.2 40,967 1.8 64.4 35.8 21.2 
2036 7.6 39,170  7.7 39,171 0.1 1.6 16.1 1.6  9.9 39,230 2.3 60.3 26.7 12.2 
2037 7.8 37,437  8.0 37,440 0.2 3.1 16.1 1.6  10.5 37,493 2.7 56.2 20.7 6.2 
2038 8.1 35,704  8.4 35,709 0.3 4.7 16.1 1.6  11.2 35,756 3.2 52.0 16.4 1.9 
2039 8.3 33,971  8.7 33,978 0.4 6.3 16.1 1.6  11.9 34,019 3.6 47.9 13.2 -1.3 
2040 8.5 32,239  9.0 32,246 0.5 7.8 16.2 1.6  12.6 32,282 4.1 43.7 10.7 -3.8 
2041 8.5 30,953  9.1 30,960 0.6 7.4 12.1 -2.4  13.1 30,999 4.6 46.0 10.1 -4.5 
2042 8.5 29,668  9.3 29,675 0.7 7.0 9.5 -5.0  13.6 29,716 5.1 48.2 9.5 -5.0 
2043 8.5 28,382  9.4 28,389 0.9 6.5 7.6 -6.9  14.1 28,433 5.5 50.5 9.1 -5.4 
2044 8.5 27,097  9.5 27,103 1.0 6.1 6.2 -8.3  14.6 27,149 6.0 52.7 8.7 -5.8 
2045 8.5 25,811  9.6 25,817 1.1 5.6 5.1 -9.4  15.0 25,866 6.5 54.9 8.4 -6.1 
2046 8.5 24,429  9.6 24,433 1.1 4.5 4.0 -10.5  15.4 24,489 6.9 59.9 8.7 -5.8 
2047 8.5 23,047  9.7 23,050 1.1 3.3 2.9 -11.6  15.8 23,111 7.2 64.9 9.0 -5.6 
2048 8.5 21,664  9.7 21,666 1.1 2.1 1.9 -12.6  16.1 21,734 7.6 69.8 9.2 -5.3 
2049 8.5 20,282  9.7 20,283 1.1 0.9 0.8 -13.7  16.5 20,357 8.0 74.8 9.4 -5.1 
2050 8.5 18,900   9.7 18,899 1.1 -0.2 -0.2 -14.7  16.9 18,979 8.3 79.7 9.6 -5.0 
Cum. 220 1,205,919   231 1,205,985 11 67 5.9 -8.6   307 1,206,973 87 1,055 12.1 -2.4

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-117 
 
Table C-4.49. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Net Zero 2050 (High CCS) Scenarios (AR6-100 
Basis) 
Year 
NZ (Hi CCS): ExFID   NZ (High CCS): MR NZ (High CCS): MR vs ExFID   NZ (High CCS): Hi Exp NZ (High CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG  LNG  GHG Cons GHG PNDE  US LNG GHG  LNG  GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,903  2.4 53,903 0.0 0.0      2.4 53,903 0.0 0.0     
2021 3.2 53,160  3.2 53,160 0.0 0.0      3.2 53,160 0.0 0.0     
2022 4.0 52,417  4.0 52,417 0.0 0.0      4.0 52,417 0.0 0.0     
2023 4.8 51,674  4.8 51,674 0.0 0.0      4.8 51,674 0.0 0.0     
2024 5.6 50,931  5.6 50,931 0.0 0.0      5.6 50,931 0.0 0.0     
2025 6.3 50,188  6.3 50,188 0.0 0.0      6.3 50,188 0.0 0.0     
2026 6.4 48,171  6.4 48,171 0.0 0.0      6.4 48,171 0.0 0.0     
2027 6.4 46,155  6.4 46,155 0.0 0.0      6.4 46,155 0.0 0.0     
2028 6.4 44,138  6.4 44,138 0.0 0.0      6.4 44,138 0.0 0.0     
2029 6.5 42,121  6.5 42,121 0.0 0.0      6.5 42,121 0.0 0.0     
2030 6.5 40,105  6.5 40,105 0.0 0.0      6.5 40,105 0.0 0.0     
2031 6.7 39,193  6.7 39,193 0.0 -0.1      7.0 39,187 0.4 -5.9 -16.4 -30.9 
2032 6.8 38,281  6.8 38,281 0.0 -0.2      7.6 38,270 0.7 -11.8 -16.4 -30.9 
2033 7.0 37,370  7.0 37,369 0.0 -0.3      8.1 37,352 1.1 -17.7 -16.4 -30.9 
2034 7.2 36,458  7.2 36,457 0.0 -0.4      8.6 36,434 1.4 -23.6 -16.4 -30.9 
2035 7.4 35,546  7.4 35,546 0.0 -0.5      9.2 35,517 1.8 -29.5 -16.4 -30.9 
2036 7.6 33,933  7.7 33,931 0.2 -2.8 -18.6 -33.1  9.9 33,916 2.3 -17.7 -7.7 -22.2 
2037 7.8 32,321  8.1 32,316 0.3 -5.2 -17.1 -31.6  10.7 32,315 2.8 -5.9 -2.1 -16.6 
2038 8.1 30,708  8.5 30,701 0.5 -7.6 -16.6 -31.1  11.4 30,714 3.3 5.8 1.8 -12.8 
2039 8.3 29,095  8.9 29,086 0.6 -9.9 -16.3 -30.8  12.2 29,113 3.8 17.6 4.6 -9.9 
2040 8.5 27,483  9.3 27,471 0.8 -12.3 -16.2 -30.7  12.9 27,512 4.4 29.4 6.7 -7.8 
2041 8.5 26,115  9.5 26,108 0.9 -6.2 -6.7 -21.2  13.4 26,154 4.9 39.6 8.1 -6.4 
2042 8.5 24,746  9.6 24,746 1.1 -0.1 -0.1 -14.6  14.0 24,796 5.4 49.9 9.2 -5.3 
2043 8.5 23,378  9.8 23,384 1.3 5.9 4.6 -9.9  14.5 23,438 6.0 60.2 10.1 -4.4 
2044 8.5 22,010  10.0 22,022 1.5 12.0 8.3 -6.2  15.0 22,080 6.5 70.4 10.8 -3.7 
2045 8.5 20,642  10.2 20,660 1.6 18.1 11.1 -3.4  15.6 20,722 7.0 80.7 11.5 -3.0 
2046 8.5 19,147  10.2 19,161 1.6 14.1 8.5 -6.0  16.0 19,207 7.4 59.3 8.0 -6.5 
2047 8.5 17,653  10.2 17,663 1.7 10.1 6.0 -8.5  16.3 17,691 7.8 37.8 4.9 -9.7 
2048 8.5 16,158  10.2 16,164 1.7 6.0 3.6 -11.0  16.7 16,175 8.2 16.4 2.0 -12.5 
2049 8.5 14,664  10.3 14,666 1.7 2.0 1.2 -13.3  17.1 14,659 8.6 -5.0 -0.6 -15.1 
2050 8.5 13,169   10.3 13,167 1.7 -2.0 -1.1 -15.7  17.5 13,143 8.9 -26.4 -3.0 -17.5 
Cum. 219 1,071,033   236 1,071,054 17 21 1.2 -13.3   312 1,071,356 93 324 3.5 -11.0

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-118 
  
Table C-4.50. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Net Zero 2050 (Moderate CCS) Scenarios (AR6-
100 Basis) 
Year 
NZ (Mod CCS):ExFID   NZ (Mod CCS): MR NZ (Mod CCS): MR vs ExFID   NZ (Mod CCS): Hi Exp NZ (Mod CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG  LNG  GHG Cons GHG PNDE  US LNG GHG  LNG  GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 53,903  2.4 53,903 0.0 0.0      2.4 53,903 0.0 0.0     
2021 3.2 53,061  3.2 53,061 0.0 0.0      3.2 53,061 0.0 0.0     
2022 4.0 52,220  4.0 52,220 0.0 0.0      4.0 52,220 0.0 0.0     
2023 4.8 51,378  4.8 51,378 0.0 0.0      4.8 51,378 0.0 0.0     
2024 5.6 50,536  5.6 50,536 0.0 0.0      5.6 50,536 0.0 0.0     
2025 6.3 49,694  6.3 49,694 0.0 0.0      6.3 49,694 0.0 0.0     
2026 6.3 47,497  6.3 47,497 0.0 0.0      6.3 47,497 0.0 0.0     
2027 6.4 45,300  6.4 45,300 0.0 0.0      6.4 45,300 0.0 0.0     
2028 6.4 43,103  6.4 43,103 0.0 0.0      6.4 43,103 0.0 0.0     
2029 6.4 40,906  6.4 40,906 0.0 0.0      6.4 40,906 0.0 0.0     
2030 6.4 38,710  6.4 38,710 0.0 0.0      6.4 38,710 0.0 0.0     
2031 6.5 36,973  6.5 36,973 0.0 0.0      6.9 36,978 0.4 4.7 12.9 -1.6 
2032 6.6 35,236  6.6 35,236 0.0 0.0      7.3 35,245 0.7 9.3 12.9 -1.6 
2033 6.7 33,499  6.7 33,499 0.0 0.0      7.7 33,513 1.1 14.0 12.9 -1.6 
2034 6.7 31,763  6.7 31,763 0.0 0.0      8.2 31,781 1.4 18.6 12.9 -1.6 
2035 6.8 30,026  6.8 30,026 0.0 0.0      8.6 30,049 1.8 23.3 12.9 -1.6 
2036 6.9 28,853  6.9 28,853 0.0 0.0      9.1 28,887 2.2 34.1 15.8 1.3 
2037 7.0 27,679  7.0 27,679 0.0 0.0      9.6 27,724 2.5 44.9 17.8 3.3 
2038 7.2 26,505  7.2 26,505 0.0 0.0      10.0 26,561 2.9 55.7 19.3 4.8 
2039 7.3 25,332  7.3 25,332 0.0 0.0      10.5 25,399 3.2 66.5 20.5 6.0 
2040 7.4 24,158  7.4 24,158 0.0 0.0      11.0 24,236 3.6 77.4 21.5 7.0 
2041 7.3 22,563  7.3 22,563 0.0 0.0      11.3 22,639 4.0 76.1 19.2 4.7 
2042 7.2 20,968  7.2 20,968 0.0 0.0      11.5 21,043 4.3 74.9 17.3 2.8 
2043 7.1 19,372  7.1 19,372 0.0 0.0      11.8 19,446 4.7 73.7 15.7 1.2 
2044 7.1 17,777  7.1 17,777 0.0 0.0      12.1 17,849 5.0 72.5 14.4 -0.1 
2045 7.0 16,181  7.0 16,181 0.0 0.0      12.4 16,253 5.4 71.3 13.2 -1.3 
2046 6.8 15,196  6.8 15,196 0.0 0.0      12.6 15,260 5.8 63.4 11.0 -3.5 
2047 6.7 14,212  6.7 14,212 0.0 0.0      12.8 14,267 6.1 55.5 9.1 -5.5 
2048 6.5 13,227  6.5 13,227 0.0 0.0      13.0 13,274 6.5 47.5 7.3 -7.2 
2049 6.3 12,242  6.3 12,242 0.0 0.0      13.2 12,282 6.8 39.6 5.8 -8.7 
2050 6.2 11,257   6.2 11,257 0.0 0.0      13.4 11,289 7.2 31.7 4.4 -10.1 
Cum. 195 989,329   195 989,329 0 0 N/A N/A   271 990,283 76 955 12.6 -1.9

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-119 
Table C-4.51. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Defined Policies Scenarios (AR6-20 Basis) 
Year 
DP: ExFID   DP: MR DP: MR vs ExFID   DP: Hi Exp DP: Hi Exp vs ExFID 
US LNG GHG  US LNG GHG  LNG  GHG Cons GHG PNDE  US LNG GHG  LNG  GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,863  2.4 73,863 0.0 0.0      2.4 73,863 0.0 0.0     
2021 3.2 72,973  3.2 72,973 0.0 0.0      3.2 72,973 0.0 0.0     
2022 4.0 72,083  4.0 72,083 0.0 0.0      4.0 72,083 0.0 0.0     
2023 4.8 71,193  4.8 71,193 0.0 0.0      4.8 71,193 0.0 0.0     
2024 5.6 70,303  5.6 70,303 0.0 0.0      5.6 70,303 0.0 0.0     
2025 6.3 69,413  6.3 69,413 0.0 0.0      6.3 69,413 0.0 0.0     
2026 6.5 69,271  6.5 69,271 0.0 0.0      6.5 69,271 0.0 0.0     
2027 6.6 69,129  6.6 69,129 0.0 0.0      6.6 69,129 0.0 0.0     
2028 6.7 68,987  6.7 68,987 0.0 0.0      6.7 68,987 0.0 0.0     
2029 6.8 68,845  6.8 68,845 0.0 0.0      6.8 68,845 0.0 0.0     
2030 7.0 68,703  7.0 68,703 0.0 0.0      7.0 68,703 0.0 0.0     
2031 7.3 69,025  7.5 69,027 0.2 1.6 8.6 -12.7  7.8 69,029 0.6 3.9 7.2 -14.1 
2032 7.6 69,348  8.0 69,351 0.4 3.3 8.6 -12.7  8.7 69,356 1.1 7.9 7.2 -14.1 
2033 7.9 69,670  8.5 69,675 0.6 4.9 8.6 -12.7  9.6 69,682 1.7 11.8 7.2 -14.1 
2034 8.2 69,992  9.0 69,999 0.8 6.5 8.6 -12.7  10.4 70,008 2.2 15.8 7.2 -14.1 
2035 8.5 70,314  9.5 70,323 1.0 8.2 8.6 -12.7  11.3 70,334 2.8 19.7 7.2 -14.1 
2036 8.5 70,185  10.4 70,204 1.8 18.9 10.3 -11.0  12.5 70,228 4.0 43.2 10.8 -10.5 
2037 8.5 70,056  11.3 70,086 2.7 29.7 10.9 -10.4  13.8 70,123 5.3 66.6 12.7 -8.6 
2038 8.5 69,927  12.2 69,967 3.6 40.4 11.2 -10.1  15.0 70,017 6.5 90.1 13.9 -7.4 
2039 8.5 69,798  13.0 69,849 4.5 51.2 11.4 -9.9  16.3 69,911 7.7 113.5 14.7 -6.6 
2040 8.5 69,669  13.9 69,731 5.4 61.9 11.5 -9.8  17.5 69,806 9.0 137.0 15.2 -6.0 
2041 8.5 69,744  14.7 69,806 6.2 61.3 9.9 -11.3  18.7 69,877 10.1 132.6 13.1 -8.2 
2042 8.5 69,820  15.5 69,881 6.9 60.7 8.8 -12.5  19.8 69,948 11.3 128.2 11.4 -9.9 
2043 8.5 69,896  16.3 69,956 7.7 60.1 7.8 -13.5  20.9 70,020 12.4 123.8 10.0 -11.3 
2044 8.5 69,971  17.0 70,031 8.5 59.5 7.0 -14.3  22.1 70,091 13.5 119.4 8.8 -12.4 
2045 8.5 70,047  17.8 70,106 9.3 58.9 6.4 -14.9  23.2 70,162 14.7 114.9 7.8 -13.4 
2046 8.5 70,016  18.3 70,068 9.8 52.0 5.3 -15.9  24.1 70,120 15.5 103.6 6.7 -14.6 
2047 8.5 69,985  18.8 70,030 10.2 45.0 4.4 -16.9  24.9 70,077 16.4 92.3 5.6 -15.6 
2048 8.5 69,954  19.3 69,992 10.7 38.1 3.5 -17.7  25.8 70,035 17.2 81.0 4.7 -16.6 
2049 8.5 69,923  19.8 69,954 11.2 31.1 2.8 -18.5  26.6 69,993 18.1 69.6 3.9 -17.4 
2050 8.5 69,892  20.3 69,916 11.7 24.2 2.1 -19.2  27.5 69,950 18.9 58.3 3.1 -18.2 
Cum. 227 2,171,997  341 2,172,715 113 718 6.3 -14.9   416 2,173,530 189 1,533 8.1 -13.1

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-120 
 Table C-4.52. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High Middle East Supply Scenarios (AR6-20 Basis) 
Year 
DP Hi ME Sup: 
ExFID   DP Hi ME Sup: MR DP Hi ME Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,874  2.4 73,874 0.0 0.0     
2021 3.2 72,985  3.2 72,985 0.0 0.0     
2022 4.0 72,097  4.0 72,097 0.0 0.0     
2023 4.8 71,208  4.8 71,208 0.0 0.0     
2024 5.6 70,319  5.6 70,319 0.0 0.0     
2025 6.3 69,431  6.3 69,431 0.0 0.0     
2026 6.5 69,292  6.5 69,292 0.0 0.0     
2027 6.6 69,154  6.6 69,154 0.0 0.0     
2028 6.8 69,016  6.8 69,016 0.0 0.0     
2029 6.9 68,877  6.9 68,877 0.0 0.0     
2030 7.1 68,739  7.1 68,739 0.0 0.0     
2031 7.4 69,080  7.6 69,081 0.2 1.0 4.6 -16.7 
2032 7.7 69,421  8.1 69,423 0.4 2.1 4.6 -16.7 
2033 8.0 69,762  8.6 69,766 0.7 3.1 4.6 -16.7 
2034 8.2 70,104  9.1 70,108 0.9 4.2 4.6 -16.7 
2035 8.5 70,445  9.7 70,450 1.1 5.2 4.6 -16.7 
2036 8.5 70,357  10.4 70,367 1.9 9.8 5.2 -16.1 
2037 8.5 70,269  11.2 70,283 2.6 14.4 5.5 -15.8 
2038 8.5 70,181  11.9 70,200 3.4 19.0 5.6 -15.7 
2039 8.5 70,093  12.7 70,116 4.1 23.6 5.7 -15.6 
2040 8.5 70,005  13.4 70,033 4.9 28.2 5.7 -15.5 
2041 8.5 70,096  14.1 70,123 5.5 27.2 4.9 -16.3 
2042 8.5 70,188  14.7 70,214 6.1 26.2 4.3 -17.0 
2043 8.5 70,279  15.3 70,304 6.8 25.2 3.7 -17.5 
2044 8.5 70,370  15.9 70,395 7.4 24.2 3.3 -18.0 
2045 8.5 70,462  16.5 70,485 8.0 23.2 2.9 -18.4 
2046 8.5 70,442  17.0 70,458 8.4 16.5 2.0 -19.3 
2047 8.5 70,422  17.4 70,432 8.8 9.8 1.1 -20.2 
2048 8.5 70,402  17.8 70,405 9.3 3.1 0.3 -20.9 
2049 8.5 70,382  18.2 70,379 9.7 -3.6 -0.4 -21.6 
2050 8.5 70,362   18.6 70,352 10.1 -10.3 -1.0 -22.3 
Cum. 228 2,178,114   329 2,178,366 100 252 2.5 -18.8

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-121 
Table C-4.53. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP High U.S. Supply Scenarios (AR6-20 Basis) 
Year 
DP Hi US Sup: 
ExFID   DP Hi US Sup: MR DP Hi US Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,858  2.4 73,858 0.0 0.0     
2021 3.2 72,970  3.2 72,970 0.0 0.0     
2022 4.0 72,081  4.0 72,081 0.0 0.0     
2023 4.8 71,192  4.8 71,192 0.0 0.0     
2024 5.6 70,304  5.6 70,304 0.0 0.0     
2025 6.3 69,415  6.3 69,415 0.0 0.0     
2026 6.5 69,274  6.5 69,274 0.0 0.0     
2027 6.6 69,133  6.6 69,133 0.0 0.0     
2028 6.8 68,992  6.8 68,992 0.0 0.0     
2029 6.9 68,851  6.9 68,851 0.0 0.0     
2030 7.0 68,710  7.0 68,710 0.0 0.0     
2031 7.3 69,033  7.6 69,036 0.3 2.4 8.1 -13.1 
2032 7.6 69,356  8.2 69,361 0.6 4.7 8.1 -13.1 
2033 7.9 69,680  8.8 69,687 0.9 7.1 8.1 -13.1 
2034 8.2 70,003  9.4 70,012 1.2 9.5 8.1 -13.1 
2035 8.5 70,326  10.0 70,338 1.5 11.9 8.1 -13.1 
2036 8.5 70,197  11.1 70,226 2.6 28.8 11.2 -10.1 
2037 8.5 70,068  12.2 70,113 3.7 45.7 12.4 -8.9 
2038 8.5 69,939  13.3 70,001 4.8 62.7 13.0 -8.2 
2039 8.5 69,810  14.5 69,889 5.9 79.6 13.4 -7.8 
2040 8.5 69,681  15.6 69,777 7.0 96.5 13.7 -7.6 
2041 8.5 69,759  16.7 69,856 8.2 97.0 11.9 -9.4 
2042 8.5 69,837  17.8 69,935 9.3 97.5 10.5 -10.7 
2043 8.5 69,916  18.9 70,014 10.4 98.1 9.4 -11.8 
2044 8.5 69,994  20.0 70,093 11.5 98.6 8.6 -12.7 
2045 8.5 70,073  21.1 70,172 12.6 99.1 7.9 -13.4 
2046 8.5 70,046  22.0 70,140 13.4 94.3 7.0 -14.2 
2047 8.5 70,019  22.8 70,108 14.2 89.4 6.3 -15.0 
2048 8.5 69,992  23.6 70,077 15.1 84.6 5.6 -15.6 
2049 8.5 69,965  24.4 70,045 15.9 79.8 5.0 -16.2 
2050 8.5 69,938   25.2 70,013 16.7 75.0 4.5 -16.8 
Cum. 228 2,172,411   383 2,173,673 156 1,262 8.1 -13.2

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-122 
Table C-4.54. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis 
of DP Low U.S. Supply Scenarios (AR6-20 Basis) 
Year 
DP Lo US Sup: 
ExFID   DP Lo US Sup: MR DP Lo US Sup: MR vs ExFID 
US 
LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e   EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,889  2.4 73,889 0.0 0.0     
2021 3.2 72,990  3.2 72,990 0.0 0.0     
2022 4.0 72,092  4.0 72,092 0.0 0.0     
2023 4.8 71,193  4.8 71,193 0.0 0.0     
2024 5.5 70,295  5.5 70,295 0.0 0.0     
2025 6.3 69,396  6.3 69,396 0.0 0.0     
2026 6.4 69,246  6.4 69,246 0.0 0.0     
2027 6.4 69,097  6.4 69,097 0.0 0.0     
2028 6.5 68,947  6.5 68,947 0.0 0.0     
2029 6.5 68,797  6.5 68,797 0.0 0.0     
2030 6.6 68,648  6.6 68,648 0.0 0.0     
2031 6.8 68,962  6.8 68,962 0.0 0.0     
2032 7.0 69,276  7.0 69,276 0.0 0.0     
2033 7.2 69,590  7.2 69,590 0.0 0.0     
2034 7.4 69,904  7.4 69,904 0.0 0.0     
2035 7.6 70,218  7.6 70,218 0.0 0.0     
2036 7.8 70,083  7.8 70,084 0.1 0.3 4.2 -17.0 
2037 8.0 69,949  8.1 69,949 0.1 0.6 4.2 -17.0 
2038 8.1 69,814  8.4 69,815 0.2 0.9 4.3 -17.0 
2039 8.3 69,680  8.6 69,681 0.3 1.3 4.3 -17.0 
2040 8.5 69,546  8.9 69,547 0.4 1.6 4.3 -17.0 
2041 8.5 69,615  9.1 69,616 0.6 1.2 2.0 -19.3 
2042 8.5 69,683  9.3 69,684 0.8 0.8 1.0 -20.3 
2043 8.5 69,752  9.6 69,753 1.0 0.4 0.4 -20.9 
2044 8.5 69,821  9.8 69,821 1.2 0.0 0.0 -21.3 
2045 8.5 69,890  10.0 69,890 1.5 -0.4 -0.3 -21.5 
2046 8.5 69,844  10.3 69,844 1.7 0.5 0.3 -21.0 
2047 8.5 69,798  10.5 69,799 2.0 1.4 0.7 -20.6 
2048 8.5 69,751  10.8 69,754 2.3 2.3 1.0 -20.2 
2049 8.5 69,705  11.1 69,708 2.5 3.2 1.3 -20.0 
2050 8.5 69,659   11.3 69,663 2.8 4.1 1.5 -19.8 
Cum. 221 2,169,129   238 2,169,147 18 18 1.0 -20.2

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-123 
Table C-4.55. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Commitments (High CCS) Scenarios (AR6 -20 
Basis) 
Year 
C (High CCS): ExFID   C (High CCS): MR C (High CCS): MR vs ExFID   C (High CCS): Hi Exp C (High CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,991  2.4 73,991 0.0 0.0      2.4 73,991 0.0 0.0     
2021 3.2 72,853  3.2 72,853 0.0 0.0      3.2 72,853 0.0 0.0     
2022 4.0 71,716  4.0 71,716 0.0 0.0      4.0 71,716 0.0 0.0     
2023 4.8 70,579  4.8 70,579 0.0 0.0      4.8 70,579 0.0 0.0     
2024 5.6 69,441  5.6 69,441 0.0 0.0      5.6 69,441 0.0 0.0     
2025 6.3 68,304  6.3 68,304 0.0 0.0      6.3 68,304 0.0 0.0     
2026 6.4 68,351  6.4 68,351 0.0 0.0      6.4 68,351 0.0 0.0     
2027 6.5 68,399  6.5 68,399 0.0 0.0      6.5 68,399 0.0 0.0     
2028 6.5 68,446  6.5 68,446 0.0 0.0      6.5 68,446 0.0 0.0     
2029 6.6 68,493  6.6 68,493 0.0 0.0      6.6 68,493 0.0 0.0     
2030 6.7 68,541  6.7 68,541 0.0 0.0      6.7 68,541 0.0 0.0     
2031 6.9 67,133  6.9 67,133 0.0 0.0      7.3 67,136 0.4 3.4 9.5 -11.7 
2032 7.1 65,725  7.1 65,725 0.0 0.0      7.8 65,732 0.7 6.9 9.5 -11.7 
2033 7.3 64,317  7.3 64,317 0.0 0.0      8.4 64,327 1.1 10.3 9.5 -11.7 
2034 7.5 62,909  7.5 62,909 0.0 0.0      9.0 62,923 1.4 13.7 9.5 -11.7 
2035 7.8 61,501  7.8 61,501 0.0 0.0      9.6 61,518 1.8 17.1 9.5 -11.7 
2036 7.9 60,365  8.2 60,362 0.3 -2.9 -10.6 -31.8  10.3 60,386 2.4 21.4 8.8 -12.5 
2037 8.1 59,228  8.6 59,222 0.5 -5.7 -10.6 -31.8  11.1 59,253 3.1 25.6 8.3 -12.9 
2038 8.2 58,091  9.0 58,082 0.8 -8.6 -10.6 -31.8  11.9 58,121 3.7 29.8 8.1 -13.2 
2039 8.4 56,954  9.5 56,943 1.1 -11.5 -10.6 -31.8  12.7 56,988 4.3 34.0 7.9 -13.4 
2040 8.5 55,817  9.9 55,803 1.4 -14.3 -10.6 -31.8  13.5 55,856 5.0 38.2 7.7 -13.6 
2041 8.5 54,079  10.2 54,072 1.7 -6.8 -4.1 -25.4  14.2 54,125 5.6 46.6 8.3 -13.0 
2042 8.5 52,340  10.5 52,341 2.0 0.7 0.4 -20.9  14.8 52,395 6.3 54.9 8.7 -12.5 
2043 8.5 50,601  10.8 50,610 2.3 8.3 3.6 -17.6  15.5 50,665 7.0 63.3 9.1 -12.2 
2044 8.5 48,863  11.1 48,879 2.6 15.8 6.1 -15.1  16.2 48,934 7.6 71.6 9.4 -11.9 
2045 8.5 47,124  11.4 47,147 2.9 23.4 8.1 -13.2  16.8 47,204 8.3 80.0 9.6 -11.6 
2046 8.5 45,463  11.5 45,480 3.0 16.8 5.6 -15.6  17.3 45,523 8.8 60.6 6.9 -14.4 
2047 8.5 43,802  11.6 43,812 3.1 10.3 3.3 -17.9  17.8 43,843 9.2 41.2 4.5 -16.8 
2048 8.5 42,141  11.7 42,144 3.2 3.8 1.2 -20.1  18.2 42,162 9.7 21.8 2.3 -19.0 
2049 8.5 40,479  11.8 40,477 3.3 -2.8 -0.8 -22.1  18.7 40,482 10.1 2.4 0.2 -21.0 
2050 8.5 38,818   11.9 38,809 3.4 -9.3 -2.7 -24.0  19.1 38,801 10.6 -17.0 -1.6 -22.9 
Cum. 222 1,844,865   254 1,844,882 31 17 0.6 -20.7   329 1,845,490 107 626 5.8 -15.4

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-124 
 
Table C-4.56. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Commitments (Moderate CCS) Scenarios (AR6-
20 Basis) 
Year 
C (Mod CCS): ExFID   C (Mod CCS): MR C (Mod CCS): MR vs ExFID   C (Mod CCS): Hi Exp C (Mod CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,991  2.4 73,991 0.0 0.0      2.4 73,991 0.0 0.0     
2021 3.2 72,682  3.2 72,682 0.0 0.0      3.2 72,682 0.0 0.0     
2022 4.0 71,374  4.0 71,374 0.0 0.0      4.0 71,374 0.0 0.0     
2023 4.8 70,065  4.8 70,065 0.0 0.0      4.8 70,065 0.0 0.0     
2024 5.6 68,756  5.6 68,756 0.0 0.0      5.6 68,756 0.0 0.0     
2025 6.3 67,448  6.3 67,448 0.0 0.0      6.3 67,448 0.0 0.0     
2026 6.4 67,501  6.4 67,501 0.0 0.0      6.4 67,501 0.0 0.0     
2027 6.4 67,554  6.4 67,554 0.0 0.0      6.4 67,554 0.0 0.0     
2028 6.5 67,608  6.5 67,608 0.0 0.0      6.5 67,608 0.0 0.0     
2029 6.6 67,661  6.6 67,661 0.0 0.0      6.6 67,661 0.0 0.0     
2030 6.6 67,714  6.6 67,714 0.0 0.0      6.6 67,714 0.0 0.0     
2031 6.8 65,928  6.8 65,928 0.0 0.0      7.1 65,943 0.4 14.5 40.2 18.9 
2032 6.9 64,143  6.9 64,143 0.0 0.0      7.6 64,171 0.7 28.9 40.1 18.9 
2033 7.1 62,357  7.1 62,357 0.0 0.0      8.2 62,400 1.1 43.4 40.1 18.9 
2034 7.2 60,571  7.2 60,571 0.0 0.0      8.7 60,629 1.4 57.8 40.1 18.9 
2035 7.4 58,785  7.4 58,785 0.0 0.0      9.2 58,857 1.8 72.3 40.1 18.9 
2036 7.6 56,926  7.7 56,928 0.1 1.6 16.2 -5.0  9.9 56,992 2.3 65.8 29.1 7.8 
2037 7.8 55,068  8.0 55,071 0.2 3.2 16.3 -5.0  10.5 55,127 2.7 59.2 21.8 0.5 
2038 8.1 53,209  8.4 53,214 0.3 4.7 16.3 -5.0  11.2 53,262 3.2 52.6 16.6 -4.7 
2039 8.3 51,350  8.7 51,357 0.4 6.3 16.3 -5.0  11.9 51,396 3.6 46.1 12.7 -8.6 
2040 8.5 49,492  9.0 49,500 0.5 7.9 16.3 -5.0  12.6 49,531 4.1 39.5 9.7 -11.6 
2041 8.5 48,084  9.1 48,091 0.6 6.8 11.2 -10.1  13.1 48,124 4.6 39.6 8.7 -12.6 
2042 8.5 46,676  9.3 46,682 0.7 5.7 7.8 -13.5  13.6 46,716 5.1 39.7 7.9 -13.4 
2043 8.5 45,269  9.4 45,273 0.9 4.6 5.4 -15.9  14.1 45,308 5.5 39.8 7.2 -14.1 
2044 8.5 43,861  9.5 43,864 1.0 3.5 3.6 -17.7  14.6 43,901 6.0 39.9 6.6 -14.7 
2045 8.5 42,453  9.6 42,456 1.1 2.4 2.2 -19.1  15.0 42,493 6.5 40.0 6.1 -15.1 
2046 8.5 41,017  9.6 41,018 1.1 1.0 0.9 -20.3  15.4 41,061 6.9 44.2 6.4 -14.8 
2047 8.5 39,581  9.7 39,581 1.1 -0.3 -0.3 -21.6  15.8 39,630 7.2 48.4 6.7 -14.6 
2048 8.5 38,145  9.7 38,143 1.1 -1.7 -1.5 -22.8  16.1 38,198 7.6 52.7 6.9 -14.3 
2049 8.5 36,709  9.7 36,706 1.1 -3.0 -2.7 -24.0  16.5 36,766 8.0 56.9 7.1 -14.1 
2050 8.5 35,273   9.7 35,268 1.1 -4.4 -3.9 -25.2  16.9 35,334 8.3 61.2 7.3 -13.9 
Cum. 220 1,757,251   231 1,757,289 11 38 3.4 -17.9   307 1,758,194 87 943 10.8 -10.4

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-125 
  
Table C-4.57.Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Net Zero 2050 (High CCS) Scenarios (AR6 -20 
Basis) 
Year 
NZ (Hi CCS): ExFID   NZ (High CCS): MR NZ (High CCS): MR vs ExFID   NZ (High CCS): Hi Exp NZ (High CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,991  2.4 73,991 0.0 0.0      2.4 73,991 0.0 0.0     
2021 3.2 72,853  3.2 72,853 0.0 0.0      3.2 72,853 0.0 0.0     
2022 4.0 71,716  4.0 71,716 0.0 0.0      4.0 71,716 0.0 0.0     
2023 4.8 70,579  4.8 70,579 0.0 0.0      4.8 70,579 0.0 0.0     
2024 5.6 69,441  5.6 69,441 0.0 0.0      5.6 69,441 0.0 0.0     
2025 6.3 68,304  6.3 68,304 0.0 0.0      6.3 68,304 0.0 0.0     
2026 6.4 66,223  6.4 66,223 0.0 0.0      6.4 66,223 0.0 0.0     
2027 6.4 64,143  6.4 64,143 0.0 0.0      6.4 64,143 0.0 0.0     
2028 6.4 62,063  6.4 62,063 0.0 0.0      6.4 62,063 0.0 0.0     
2029 6.5 59,982  6.5 59,982 0.0 0.0      6.5 59,982 0.0 0.0     
2030 6.5 57,902  6.5 57,902 0.0 0.0      6.5 57,902 0.0 0.0     
2031 6.7 57,002  6.7 57,002 0.0 -0.1      7.0 56,998 0.4 -4.7 -13.0 -34.3 
2032 6.8 56,103  6.8 56,103 0.0 -0.2      7.6 56,094 0.7 -9.4 -13.0 -34.3 
2033 7.0 55,204  7.0 55,204 0.0 -0.3      8.1 55,190 1.1 -14.1 -13.0 -34.3 
2034 7.2 54,305  7.2 54,304 0.0 -0.4      8.6 54,286 1.4 -18.8 -13.0 -34.3 
2035 7.4 53,405  7.4 53,405 0.0 -0.5      9.2 53,382 1.8 -23.5 -13.0 -34.3 
2036 7.6 51,650  7.7 51,647 0.2 -3.0 -19.7 -41.0  9.9 51,636 2.3 -13.6 -5.9 -27.1 
2037 7.8 49,895  8.1 49,889 0.3 -5.5 -18.2 -39.4  10.7 49,891 2.8 -3.7 -1.3 -22.6 
2038 8.1 48,139  8.5 48,131 0.5 -8.0 -17.7 -38.9  11.4 48,145 3.3 6.1 1.8 -19.4 
2039 8.3 46,384  8.9 46,373 0.6 -10.6 -17.4 -38.7  12.2 46,400 3.8 16.0 4.1 -17.1 
2040 8.5 44,629  9.3 44,615 0.8 -13.1 -17.3 -38.5  12.9 44,654 4.4 25.8 5.9 -15.3 
2041 8.5 43,200  9.5 43,193 0.9 -7.8 -8.3 -29.6  13.4 43,234 4.9 33.3 6.8 -14.5 
2042 8.5 41,772  9.6 41,770 1.1 -2.4 -2.2 -23.5  14.0 41,813 5.4 40.8 7.5 -13.8 
2043 8.5 40,344  9.8 40,347 1.3 2.9 2.3 -19.0  14.5 40,392 6.0 48.3 8.1 -13.2 
2044 8.5 38,916  10.0 38,924 1.5 8.2 5.6 -15.6  15.0 38,971 6.5 55.7 8.6 -12.7 
2045 8.5 37,488  10.2 37,501 1.6 13.5 8.3 -12.9  15.6 37,551 7.0 63.2 9.0 -12.3 
2046 8.5 35,912  10.2 35,921 1.6 9.2 5.6 -15.7  16.0 35,952 7.4 40.4 5.5 -15.8 
2047 8.5 34,336  10.2 34,341 1.7 4.9 2.9 -18.3  16.3 34,354 7.8 17.7 2.3 -19.0 
2048 8.5 32,760  10.2 32,761 1.7 0.6 0.4 -20.9  16.7 32,755 8.2 -5.1 -0.6 -21.9 
2049 8.5 31,184  10.3 31,181 1.7 -3.7 -2.1 -23.4  17.1 31,157 8.6 -27.9 -3.3 -24.5 
2050 8.5 29,609   10.3 29,601 1.7 -8.0 -4.6 -25.8  17.5 29,558 8.9 -50.6 -5.7 -26.9 
Cum. 219 1,619,433   236 1,619,408 17 -24 -1.4 -22.7   312 1,619,609 93 176 1.9 -19.4

ENERGY, ECONOMIC, AND ENVIRONMENTAL ASSESSMENT OF U.S. LNG EXPORTS  
  C-126 
 
Table C-4.58. Annual and Cumulative Emissions, U.S. LNG Exports, and Consequential Analysis of Net Zero 2050 (Moderate CCS) Scenarios (AR6-
20 Basis) 
Year 
NZ (Mod CCS):ExFID   NZ (Mod CCS): MR NZ (Mod CCS): MR vs ExFID   NZ (Mod CCS): Hi Exp NZ (Mod CCS): Hi Exp vs ExFID 
US LNG GHG  US LNG GHG D LNG D GHG Cons GHG PNDE  US LNG GHG D LNG D GHG Cons GHG PNDE 
EJ Tg CO2e  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ  EJ Tg CO2e EJ Tg CO2e g CO2e/MJ g CO2e/MJ 
2020 2.4 73,991  2.4 73,991 0.0 0.0      2.4 73,991 0.0 0.0     
2021 3.2 72,682  3.2 72,682 0.0 0.0      3.2 72,682 0.0 0.0     
2022 4.0 71,374  4.0 71,374 0.0 0.0      4.0 71,374 0.0 0.0     
2023 4.8 70,065  4.8 70,065 0.0 0.0      4.8 70,065 0.0 0.0     
2024 5.6 68,756  5.6 68,756 0.0 0.0      5.6 68,756 0.0 0.0     
2025 6.3 67,448  6.3 67,448 0.0 0.0      6.3 67,448 0.0 0.0     
2026 6.3 65,077  6.3 65,077 0.0 0.0      6.3 65,077 0.0 0.0     
2027 6.4 62,706  6.4 62,706 0.0 0.0      6.4 62,706 0.0 0.0     
2028 6.4 60,335  6.4 60,335 0.0 0.0      6.4 60,335 0.0 0.0     
2029 6.4 57,963  6.4 57,963 0.0 0.0      6.4 57,963 0.0 0.0     
2030 6.4 55,592  6.4 55,592 0.0 0.0      6.4 55,592 0.0 0.0     
2031 6.5 53,721  6.5 53,721 0.0 0.0      6.9 53,727 0.4 5.7 15.9 -5.4 
2032 6.6 51,850  6.6 51,850 0.0 0.0      7.3 51,862 0.7 11.4 15.9 -5.4 
2033 6.7 49,979  6.7 49,979 0.0 0.0      7.7 49,996 1.1 17.1 15.9 -5.4 
2034 6.7 48,108  6.7 48,108 0.0 0.0      8.2 48,131 1.4 22.9 15.9 -5.4 
2035 6.8 46,237  6.8 46,237 0.0 0.0      8.6 46,266 1.8 28.6 15.9 -5.4 
2036 6.9 45,024  6.9 45,024 0.0 0.0      9.1 45,062 2.2 38.4 17.8 -3.5 
2037 7.0 43,811  7.0 43,811 0.0 0.0      9.6 43,859 2.5 48.2 19.1 -2.1 
2038 7.2 42,597  7.2 42,597 0.0 0.0      10.0 42,656 2.9 58.1 20.2 -1.1 
2039 7.3 41,384  7.3 41,384 0.0 0.0      10.5 41,452 3.2 67.9 21.0 -0.3 
2040 7.4 40,171  7.4 40,171 0.0 0.0      11.0 40,249 3.6 77.8 21.6 0.3 
2041 7.3 38,466  7.3 38,466 0.0 0.0      11.3 38,539 4.0 73.8 18.6 -2.7 
2042 7.2 36,760  7.2 36,760 0.0 0.0      11.5 36,830 4.3 69.8 16.1 -5.1 
2043 7.1 35,055  7.1 35,055 0.0 0.0      11.8 35,121 4.7 65.8 14.0 -7.2 
2044 7.1 33,350  7.1 33,350 0.0 0.0      12.1 33,412 5.0 61.8 12.3 -9.0 
2045 7.0 31,645  7.0 31,645 0.0 0.0      12.4 31,702 5.4 57.8 10.7 -10.6 
2046 6.8 30,621  6.8 30,621 0.0 0.0      12.6 30,669 5.8 47.9 8.3 -13.0 
2047 6.7 29,597  6.7 29,597 0.0 0.0      12.8 29,635 6.1 38.0 6.2 -15.1 
2048 6.5 28,573  6.5 28,573 0.0 0.0      13.0 28,601 6.5 28.0 4.3 -16.9 
2049 6.3 27,549  6.3 27,549 0.0 0.0      13.2 27,567 6.8 18.1 2.6 -18.6 
2050 6.2 26,525   6.2 26,525 0.0 0.0      13.4 26,534 7.2 8.2 1.1 -20.1 
Cum. 195 1,507,012   195 1,507,012 0 0 N/A N/A   271 1,507,858 76 845 11.2 -10.1
