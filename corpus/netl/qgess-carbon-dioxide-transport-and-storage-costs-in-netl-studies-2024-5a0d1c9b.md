---
source_id: "netl"
title: "QGESS: Carbon Dioxide Transport and Storage Costs in NETL Studies (DOE/NETL-2024/4852, 2024)"
url: "https://netl.doe.gov/projects/VueConnection/download.aspx?id=c6081462-66d8-4cf2-a8e8-cd3424dce3d9&filename=QualityGuidelinesforEnergySystemStudiesCarbonDioxideTransportandStorageCostsinNETLStudies_073124.pdf"
retrieved_at: "2026-10-25T15:49:29+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "CCS", "H2", "PWR"]
disciplines: ["PRC", "MAT"]
sha256: "5a0d1c9bbd2837a136ebf53c503c377321114ec1f2748d23877f957c794aa0b1"
collected: "manual"
summary: "NETL Quality Guidelines reference for CO2 transport and storage costs: break-even transport and storage costs in 2023 dollars against pipeline diameter, mass flow and distance, and storage cost sensitivity to injectivity and reservoir thickness."
---

# qgess carbon dioxide transport and storage costs in netl studies 2024

July 2024 
QUALITY GUIDELINES 
FOR ENERGY SYSTEM STUDIES 
Carbon Dioxide Transport and 
Storage Costs in NETL Studies 
DOE/NETL-2024/4852

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -2-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
 
 
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

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -3-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
 
 
 
Travis Warner1,2: Formal Analysis, Writing – Original Draft, Writing – 
Review & Editing, Visualization; Derek Vikara1,2: Conceptualization, 
Formal Analysis, Writing – Original Draft, Writing – Review & Editing; 
David Morgan1: Conceptualization, Methodology, Writing – Original 
Draft, Writing – Review & Editing, Supervision; Timothy Grant1*: 
Conceptualization, Methodology, Writing – Review & Editing, 
Supervision.  
 
1National Energy Technology Laboratory (NETL)  
2NETL support contractor 
*Corresponding contact: David.Morgan@netl.doe.gov, 412.386.7405 
 
 
 
 
 
 
 
 
 
 
 
 
Acknowledgements 
 
The authors wish to acknowledge the excellent guidance, contributions, and 
cooperation of NETL staff and additional support contractors, particularly: 
 
Marc Turner – NETL support contractor 
Sarah Leptinsky – NETL support contractor 
Indrajit Bhattacharya – NETL, Energy Process Analysis Team 
Robert James – NETL, Energy Systems Analysis Team 
Hannah Hoffman – NETL support contractor 
 
 
Suggested Citation: 
T. Warner, D. Vikara, D. Morgan, T. Grant, "Quality Guidelines for Energy System Studies: 
Carbon Dioxide Transport and Storage Costs in NETL Studies," National Energy 
Technology Laboratory, Pittsburgh, July 2024.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -4-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
 
This page intentionally left blank.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -5-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
TABLE OF CONTENTS 
List of Exhibits ............................................................................................................................ 6  
Acronyms and Abbreviations ................................................................................................. 7  
Executive Summary ................................................................................................................. 8  
1 Introduction ......................................................................................................................10  
2 Modeling Approach .......................................................................................................11  
2.1 Transport Cost Overview and Methods ..................................................................12  
2.1.1 Transport Cost Case Study 1: Regional Variation – Methodology .................16 
2.1.2 Transport Cost Case Study 2: CO2 Mass Flow Rate and Pipeline Distance 
Variations – Methodology ...............................................................................................18  
2.2 Storage Cost Overview and Methods ....................................................................18  
2.2.1 Storage Cost Case Study 1: Regional Variation – Methodology ...................21 
2.2.2 Storage Cost Case Study 2: Project Design Variations – Methodology ........23 
2.2.2.1 Storage Project Geologic Factors .............................................................24  
2.2.2.2 Storage Project Execution Factors ............................................................27  
2.2.3 Storage Cost Case Study 3: CO2 Mass Flow Rate Variations – Methodology
 29  
2.3 Guideline T&S Costs Methodology ..........................................................................29  
3 Modeling Results ..............................................................................................................30  
3.1 CO2 Transport Cost Results Overview ......................................................................30  
3.1.1 Transport Cost Case Study 1: Regional Variation – Results .............................30 
3.1.2 Transport Cost Case Study 2: CO2 Mass Flow Rate and Distance Variations – 
Results 31  
3.2 CO2 Storage Costs Results Overview ......................................................................31  
3.2.1 Storage Cost Case Study 1: Regional Variation – Results ...............................32 
3.2.2 Storage Cost Case Study 2: Project Design Variations – Results ....................33 
3.2.3 Storage Cost Case Study 3: CO2 Mass Flow Rate Variations – Results ..........35 
3.3 Guideline T&S Costs Results ......................................................................................36  
4 Revision Control ...............................................................................................................37  
References ..............................................................................................................................39

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -6-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
LIST OF EXHIBITS 
Exhibit ES-0-1. Guideline T&S Costs ......................................................................................... 9  
Exhibit 2-1. Idealized timeline for construction and operations of capture pipeline, and 
storage projects ......................................................................................................................11  
Exhibit 2-2. CO2 pipeline capital costs per mile using CO2_T_COM’s different regression 
equation options ....................................................................................................................14  
Exhibit 2-3. Financial parameters used in CO2_T_COM .......................................................15  
Exhibit 2-4. Brown et al., transportation regions ....................................................................17  
Exhibit 2-5. Brown et al., normalized total pipeline costs broken out by cost category ...17 
Exhibit 2-6. Financial parameters used/modeled in CO2_S_COM .....................................20  
Exhibit 2-7. Locations of four basins selected for this analysis .............................................22  
Exhibit 2-8. Regional storage variation case study basins, geologic formations and 
associated storage reservoirs ................................................................................................22  
Exhibit 2-9. Modeling parameters for low-cost, base, and high-cost scenarios ................23 
Exhibit 2-10. Reservoir quality against FYBE cost for base case ..........................................25  
Exhibit 2-11. Conceptual depiction of critical CO2 storage cost driver boundaries and 
definitions part of CO2_S_COM .............................................................................................26  
Exhibit 2-12. CO2 storage coefficients for the Mount Simon geologic formation ..............27 
Exhibit 2-13. CO2 mass flow rates and injection well count assessed in Storage Cost Case 
Study 3 scenarios ....................................................................................................................29  
Exhibit 3-1. Comparable CO2 transport costs by region ......................................................30  
Exhibit 3-2. FYBE cost sensitivity to pipeline length, pipeline capacity factor, and mass of 
CO2 transported .....................................................................................................................31  
Exhibit 3-3. Cumulative prospective CO2 storage resource cost supply curves for base 
case .........................................................................................................................................32  
Exhibit 3-4. Minimum FYBE CO2 storage cost in four basins at different cumulative 
prospective CO2 storage resource thresholds for base case .............................................33  
Exhibit 3-5. CO2 storage project FYBE cost, broken out by project phase, in the Mount 
Simon 3 for low-cost, base, and high-cost scenarios ...........................................................34  
Exhibit 3-6. Mount Simon 3 storage reservoir FYBE costs for different CO2 mass flow rates
 .................................................................................................................................................35  
Exhibit 3-7. Average annual CO2 injection rate impact on FYBE cost of CO2 storage in 
the Mount Simon 3 ..................................................................................................................36  
Exhibit 3-8. Guideline T&S Costs by study region ..................................................................36  
Exhibit 4-1. Revision table .......................................................................................................37

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -7-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
ACRONYMS AND ABBREVIATIONS 
2D Two dimensional 
3D Three dimensional 
AoR Area of review 
CCS Carbon capture and storage 
CO2 Carbon dioxide 
CO2_S_COM FECM/NETL CO 2 Saline 
Storage Cost Model 
CO2_T_COM  FECM/NETL CO 2 Transport 
Cost Model 
DOE Department of Energy 
EIA Energy Information 
Administration 
EPA Environmental Protection 
Agency 
FECM Fossil Energy and Carbon 
Management 
ft Foot, feet 
FYBE First-year break-even 
GDP Gross domestic product 
Gt Gigatonne (billion metric tons) 
in Inch 
IRROE Internal rate of return on equity 
km Kilometer 
mD Millidarcy 
mi2 Square mile 
Mt Megatonne (million metric 
tons) 
MW Megawatt 
NETL National Energy Technology 
Laboratory 
O&M Operation and maintenance 
PISC Post-injection site care 
psia  Pound per square inch 
absolute 
psig Pound per square inch gauge 
T&S Transport and storage 
tonne Metric ton (1,000 kilograms) 
U.S. United States 
yr Year

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -8-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
EXECUTIVE SUMMARY 
The National Energy Technology Laboratory (NETL) conducts multiple types of energy system 
studies on the costs associated with the capture of carbon dioxide (CO2) from electric power 
plants and industrial sources. These studies leverage comparative costs for CO2 pipeline 
transport and geologic storage (T&S) for handling the equivalent volumes of CO2 captured. This 
T&S Quality Guideline for Energy Systems Studies (QGESS) explains the modeling approaches and 
key assumptions used by NETL to estimate comparable transport, storage, and combined T&S 
costs in a transparent and reproducible way. This guideline provides representative transport, 
storage, and combined T&S costs for different scenarios, varying important T&S cost drivers, 
which can ultimately be used across a range of energy systems studies and reports.  
Transport, storage, and combined T&S costs are reported in this guideline as first-year break 
even (FYBE) costs in real 2023 dollars per metric ton (tonne) (2023$/tonne). These FYBE costs are 
from the perspective of a CO2 pipeline project owner and/or a CO2 saline storage project owner, 
and represent a minimum price the owner(s) can charge a CO2 capture project owner over 30 
operating years to transport and/or store a tonne of CO2 and remain economically viable.    
Two tools, developed by NETL and the Department of Energy (DOE) Office of Fossil Energy and 
Carbon Management (FECM) were used calculate T&S costs: 1) the FECM/NETL CO2 Transport 
Cost Model (CO2_T_COM) and 2) an updated version of the FECM/NETL CO2 Saline Storage Cost 
Model (CO2_S_COM). Both CO2_T_COM and CO2_S_COM are publicly available and can be 
modified to reflect assumptions listed throughout this guidance document.  
Six case studies were conducted to generate T&S costs under several modeling scenarios to 
provide demonstrable example applications. Two case studies were specific to generating 
transport costs, three were specific to generating storage costs, and one generated combined 
T&S costs. Three of the case studies focused on the impacts of regional variation, and these 
compared costs for identical projects located in four different geographic "Guideline Regions”:  
1) Midwest; 2) Texas; 3) North Dakota; and 4) Montana. These regions align with defined 
transportation regions for specific pipeline construction labor and pipeline operations and 
maintenance costs, with defined geologic basins of varying well construction material costs, 
and variable geologic constitution. Case studies that focused at the project level all assumed 
projects located within the Midwest region. 
The two transportation case studies evaluated the differences in CO2 pipeline transportation 
cost between regions as well as on the influence of CO2 mass flow rate and transport distance 
on transport cost. At the regional level, the transport regions corresponding with North Dakota 
and Montana had lower relative transportation costs, while the transport regions corresponding 
with the Midwest and Texas had higher relative transportation costs. At the project-level, higher 
CO2 mass flow rates, and shorter transportation distances result in reduced per tonne transport 
costs.  
The three storage case studies were conducted for evaluating the impact of key CO2 storage cost 
drivers on CO2 storage costs. One case study was regional and more broadly focused, evaluating

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -9-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
how prospective CO2 storage resource quality and quantity within and across the different 
basins modeled impacted associated CO2 storage costs. The other two case studies were 
focused on the individual storage project-level and included evaluating the effect of storage 
project design and the effect of annual CO2 mass flow rates on storage costs.  At the regional 
level, the basins corresponding with the Midwest and Texas regions had lower overall storage 
costs over a range of cumulative prospective CO2 storage resource thresholds (5 to 50 billion 
tonnes [gigatonnes; Gt]), while the basins corresponding with the North Dakota and Montana 
regions had higher storage costs. At the storage project-level, formations with better reservoir 
quality (i.e., having more accessible storage space due to geologic reservoir factors like 
thickness, porosity, permeability, and storage coefficient), lower project activity costs, shorter 
project phase durations, and higher annual CO2 mass flow injection rates all resulted in reduced 
per tonne storage costs.  
The combined regional T&S case study aggregated results from the regional transport case 
study and the regional storage case study to demonstrate the impact of geographic location on 
combined T&S costs.  A single comparable T&S cost in each region was generated for a specific 
scenario representative of a commercial scale carbon management project. These comparable 
aggregated T&S costs are referred to as “Guideline T&S Costs” . Guideline T&S Costs are based on 
a scenario where an average of 4.31 million tonnes (megatonnes [Mt]) of CO2 are captured each 
year from a stationary point source and transported along a dedicated greenfield 100-kilometer 
(62-mile) pipeline to a greenfield CO2 saline storage site. The scenario assumes that multiple 
saline storage projects of equivalent size are deployed in each region such that each region will 
cumulatively store 5 Gt of CO2 over 30 years. The 5 Gt threshold was chosen to make Guideline 
T&S Costs’ storage costs be analogous to nth-of-a-kind CO2 storage project costs that may be 
more likely as commercial CO2 storage industry becomes established, as opposed to pilot-scale 
first-of-a-kind projects which may have distorted storage costs. The Guideline T&S Costs’ storage 
costs are the highest-cost storage project among the low-cost storage projects needed to 
exceed the 5 Gt threshold in a particular region, and are shown in Exhibit ES-0-1. 
Exhibit ES-0-1. Guideline T&S Costs 
Guideline 
Region 
Transportation 
Region 
Geologic Storage 
Basin 
Guideline T&S Costs 
(2023$/tonne) 
Midwest Great Lakes Illinois 10.00 
Texas Southwest East Texas 10.34 
North Dakota Great Plains Williston 12.17 
Montana Rocky Mountain Powder River 16.48 
Variability in Guideline T&S Costs between the four selected regions reflect the unique geology 
of the different storage reservoirs in each associated basin, as well as regional variations in 
capital costs associated with drilling materials and labor (for storage) and pipeline materials and 
construction labor (for transportation).

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -10-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
1 INTRODUCTION 
Driving down carbon emissions requires dramatic expansion in the scale of deployment of 
different supporting technologies recognized as a pivotal towards aiding the transition to a low- 
or zero-emission future. Carbon dioxide (CO2) capture, transportation, and storage (CCS) 
receives significant attention by government, academic, and industry stakeholders towards this 
pursuit as of late. CCS includes a collection of technologies aimed to lessen the volume of CO2 
emitted to the atmosphere from various industrial or power generating sources or to remove 
CO2 from the air directly. The collection involves a sequence of integrated components, which 
collectively defines the CCS value chain. Necessary components include 1) separating and 
capturing CO2 from industrial and fossil-fuel power generation sources or directly from the air, 
purifying the CO2 stream as needed, and compressing it for transport; 2) transporting the CO2 to 
a geologic storage or utilization site, which can occur onshore via pipeline; and 3) injecting the 
delivered CO2 into a suitable geologic storage formation where the CO2 can be isolated from the 
atmosphere [1, 2].  
Advancing CCS requires analytical capability that can provide quantitative outlooks associated 
with the cost and economics of CCS where technical requirements intersect current regulations 
and cost drivers. The U.S. Department of Energy’s (DOE) National Energy Technology Laboratory 
(NETL) and Office of Fossil Energy and Carbon Management has developed models and 
methods that enable cost and economic evaluation of each component of the CCS value chain 
or CCS as an integrated whole [3]. The publicly available FECM/NETL CO2 Transport Cost Model 
(CO2_T_COM)a and an updated version of the publicly available FECM/NETL CO2 Saline Storage 
Cost Model (CO2_S_COM)b were developed to assess at the screening level cost and 
performance of pipelines for CO2 transportation and saline reservoirs for CO2 storage, 
respectively. These models are flexible and enable evaluation across a broad spectrum of 
integrated CCS scenarios [4, 5, 6, 7], and they can be used to focus on evaluating particular cost 
drivers associated with CO2 transport and/or storage [8, 9, 10]. Therefore, these models are 
effective when used to perform comparative analyses of the impacts of specific technologies or 
activities on overall transport or storage project costs. However, both the CO2_S_COM and 
CO2_T_COM are intrinsically complex. They each incorporate a multitude of user inputs and 
have many underlying factors to effectively evaluate CO2 transport and storage (T&S) projects 
and offer users effective decision support capability. Thus, it remains important to explain the 
modeling approaches and key assumptions used by NETL to estimate comparable T&S costs in a 
transparent and reproducible way.  
The purpose of this guideline is to provide an overview of the modeling approaches used by the 
NETL to estimate costs for transport, storage, and combined T&S. These cost estimation 
methods can be used by across various energy systems studies, reports by NETL and DOE, as 
well as by other stakeholders interested in evaluating technical and cost considerations for CO2 
 
a The model is available on NETL’s website [12, 33]. 
b It is important to note that a version of CO2_S_COM that is under development was used for this analysis. This version will 
eventually be released to the public. However, an earlier version of the model is available on NETL’s website [34, 35].

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -11-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
capture, transport, and storage systems. This guideline provides representative transport, 
storage, and combined T&S costs for a variety of situational case studies to demonstrate 
application. This guideline also discusses key cost drivers and how they affect overall transport, 
storage, and combined T&S costs.  
Transport, storage, and combined T&S costs are reported in this guideline as first-year break 
even (FYBE) costs in real 2023 dollars per metric ton (tonne) (2023$/tonne). These FYBE costs are 
from the perspective of a CO2 pipeline project owner and/or a CO2 saline storage project owner, 
and represent a minimum price the owner(s) can charge a CO2 capture project owner over 30 
operating years to transport and/or store a tonne of CO2 and remain economically viable.    
2 MODELING APPROACH 
NETL uses CO2_T_COM and CO2_S_COM to estimate the costs of CO2 pipeline transport and 
CO2 saline storage, respectively. CO2_S_COM and CO2_T_COM were designed to be able to 
incorporate a multitude of user inputs, enabling the flexibility needed to evaluate carbon 
management costs across a broad spectrum of integrated CCS scenarios [4, 5, 6, 7]. The large 
variety of user input options enable the tools to be used for focused evaluation on particular 
cost drivers associated with CO2 transport and/or storage. Examples have been demonstrated 
by Vikara et al. (2018), Warner et al. (2020), and Morgan et al. (2023) [8, 9, 10]. This section 
explains the modeling approaches and details key assumptions used by NETL to estimate the 
comparable transport, storage, and combined T&S costs from six case studies in a transparent 
and reproducible way.  
All the case studies and associated transport, storage, and combined T&S costs reported in this 
guideline share a common assumption about capture, transport, and storage project 
interconnectivity. The case studies all assume a single CO2 pipeline transport project transports 
CO2 to a single CO2 storage project, and that both projects are designed and sized to manage 
the annual CO2 mass flow rate of a single CO2 point source engaged in CO2 capture. A key 
assumption shared across both CO2_T_COM and CO2_S_COM methodologies is the alignment 
of the projects’ operational start dates. An idealized timeline for the construction and operation 
of a capture plant, pipeline, and storage site is shown in Exhibit 2-1, along with key 
development stages outlined for each.  
Exhibit 2-1. Idealized timeline for construction and operations of capture pipeline, and storage projects 
Year 1 2 3 4 5 6 7 … 34 35 36 … 84 85 
Capture 
Plant   
Capital Expenditure Period: 
 3–5 Years Operations: 30 Years   
Pipeline   Capital Expenditure Period: 3 Years Operations: 30 Years   
Storage  
Site: Base 
Case 
Site 
Screen-
ing 
Site Selection  
and Site 
Characterization 
Permitting and 
Construction Operations: 30 Years PISC and Site Closure:  50 Years

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -12-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
In both the CO2_T_COM and CO2_S_COM, the transport and storage projects’ start year (not 
the operations phase start year as shown in Exhibit 2-1) for cost estimates performed in this 
guideline was assumed to be 2023, to align with T&S costs being reported as first-year [of 
project] break even real 2023 dollars per tonne of CO2. The rest of the assumptions within the 
case studies vary in different ways, and are described in the following sections: 
 Section 2.1 describes the CO2_T_COM and its key underlying factors. Section 2.1 also 
outlines key financial and project design assumptions and model settings NETL used to 
generate comparable CO2 transport costs reported in the two transport cost case studies 
presented in this guideline.   
 Section 2.2 describes the CO2_S_COM and its key underlying factors. Section 2.2 also 
outlines key financial and project design assumptions and model settings NETL used to 
generate comparable CO2 storage costs reported in three storage cost case studies 
presented in this guideline.  
 Section 2.3 describes the assumptions used to select regional transport and regional 
storage case studies’ cost results to generate comparable combined T&S costs, termed 
“Guideline T&S Costs”.  
2.1 TRANSPORT COST OVERVIEW AND METHODS 
NETL estimates CO2 transport costs using the CO2_T_COM. CO2_T_COM is a Microsoft® Excel-
based model that estimates the cost of transporting liquid CO2 via pipeline [12] connecting 
point-to-point the CO2 source with the CO2 storage site. CO2_T_COM includes the capital costs 
for purchasing and installing the pipeline, a surge tank, a pipeline control system, and, if 
required, booster pumps along the pipeline to boost the pressure. The model accounts for the 
operation and maintenance (O&M) costs for the pipeline and pumps and the cost of the 
electricity used to power the pumps. CO2_T_COM also has a financial module that accounts for 
depreciation and taxes and uses the weighted average cost of capital to discount net earnings 
and account for the costs of debt and equity.  
One major assumption in the CO2_T_COM is that the owner (also assumed to be the operator) 
of the CO2 pipeline is an independent profit-seeking entity that charges a user for transporting 
CO2. The pipeline operator sets a price for transporting CO2 in dollars per tonne of CO2. This 
price results in revenues for the pipeline operator and these revenues are used to offset costs, 
including capital costs, operating and maintenance (O&M) costs, taxes and financing costs 
(principal and interest on debt and the minimum desired internal rate of return on equity) to 
build and operate the pipeline. An important output from CO2_T_COM is the FYBE CO2 
transport price which is the CO2 price that makes the net present value for the project equal to 
zero. The FYBE price is the lowest price the pipeline operator can charge for transporting CO2 
and still have a viable project, if just barely. The FYBE CO2 price of transportation from the 
pipeline operator’s perspective is also the FYBE CO2 cost of transportation from the capture 
facility’s perspective. In this analysis, the terms FYBE CO2 cost and FYBE cost are used, and these 
are the same as the FYBE CO2 price.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -13-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
CO2_T_COM assumes that CO2 is provided to the pipeline by the CO2 source at a pressure of 
2,200 pounds per square inch gauge (psig), and the cost and energy requirements of 
compression are provided by the CO2 source. The model assumes that CO2 is provided by the 
source at the pipeline operator’s specifications for purity. The model also assumes that CO2 is 
transported as a liquid since temperatures in the ground that surround a buried pipeline are not 
high enough to support CO2 in the supercritical phase.  
CO2_T_COM assumes that CO2 exits the pipeline terminus at the CO2 storage site at a pressure 
of 1,200 psig to ensure that CO2 remains in a dense phase liquid state throughout the length of 
the pipeline regardless of potential pressure drops due to pipeline elevation changes. If the 
pipeline has booster pumps, the pipeline is assumed to be divided into equal length segments 
with booster pumps at the end of all segments except the last. Pipeline design in this guideline 
for all transportation cost estimates assumed a pressure drop of 1,000 psia across the pipeline 
or pipeline segments if booster pumps were used, as described above. Additional pressure 
increases that may be required for injection into a storage reservoir are assumed to be provided 
by pumps owned and operated by the storage project.  
The CO2_T_COM can estimate the minimum pipeline diameter needed to transport the CO2 a 
user-specified distance without any pumps to boost the pressure. The model can also 
determine if a smaller diameter pipe can be used if one or more pumps are used at equal 
intervals along the pipeline to boost pressure sufficiently to assure that the outlet pressure is 
1,200 psig. It uses an iterative procedure to determine the diameter necessary to sustain a 
1,000-pounds per square inch absolute (psia) pressure drop over the specified pipeline length, 
or pipeline segment length, if pumps are installed along the pipeline. The model rounds up the 
diameter to the nearest standard pipe diameter. The pipeline diameter is determined based on 
the maximum CO2 mass flow rather than the average annual CO2 mass flow rate.  
The CO2_T_COM provides the option to use one of four sets of regression equations based on 
natural gas pipelines to calculate the capital costs for a CO2 pipeline. Each regression equation 
calculates costs for four categories: 1) materials, 2) labor, 3) right-of-way and damages, and 4) 
miscellaneous. The materials category includes the costs for pipe, pipe coating, and cathodic 
protection. The labor category and right-of-way and damages category are self-explanatory. The 
miscellaneous category includes costs for surveying, engineering, supervision, contingencies, 
telecommunications equipment, freight, taxes, allowances for funds used during construction, 
administration and overhead, and regulatory filing fees. The costs for each category are 
compiled by the Federal Energy Regulatory Commission for inter-state natural gas pipelines and 
these costs are published annually. One set of regression equations for pipeline capital costs 
was developed by Parker (2004) [13] using cost data from 1991 to 2003; these equations 
provide costs in 2000 dollars. A second set of regression equations was developed by McCoy 
and Rubin (2008) [14] using cost data from 1995 to 2005; these equations provide costs in 2004 
dollars. The third set of regression equations for pipeline capital costs was developed by Rui et 
al. (2011) [15] using cost data from 1992 to 2008; these equations provide costs in 2008 dollars. 
The fourth set of regression equations was developed by Brown et al. (2022) [16] using cost 
data from 1980 to 2017; these equations provide costs in 2018 dollars.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -14-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
While the four sets of regression equations have different functional forms, they all calculate 
natural gas pipeline capital costs as a function of pipeline length and diameter. The cost 
equations by McCoy and Rubin, Rui et al., and Brown et al., also considered regional cost 
differences, whereas cost equations by Parker were based on national data. Thus, the capital 
costs for pipelines (using equations other than Parker) with identical length and diameter will 
not be the same if they are in different defined regions. The defined regions are Northeast, 
Southeast, Midwest, Southwest, Central, and Western for McCoy and Rubin and Rui et al. For 
Brown et al., the defined regions are New England, Mid-Atlantic, Southeast, Great Lakes, Great 
Plains, Rocky Mountain, Pacific Northwest, Southwest, and California. The capital costs for all 
four sets of equations are adjusted (escalated, or de-escalated in the case of Brown et al.,) to 
2011 dollars in the CO2_T_COM using a variety of price indices. The resulting capital costs are 
for natural gas pipelines. CO2 pipelines operate at higher pressures than natural gas pipelines, so 
they require a thicker pipe wall, which affects the cost. The capital costs for materials and labor 
are therefore adjusted, depending on the pipe diameter, in CO2_T_COM using factors 
developed by ICF International [17].  
The four sets of regression equations for natural gas pipeline capital costs, adjusted for CO2 
pipelines, give different results as illustrated in Exhibit 2-2, which presents the cost per mile 
data escalated to 2023$ for 12-inch diameter pipelines of different lengths. The results in Exhibit 
2-2 for the Parker equations are national, while the results for McCoy and Rubin and Rui et al., 
are for the Midwest region, and Brown et al. is for the average costs across all regions in the 
United States.  
Exhibit 2-2. CO2 pipeline capital costs per mile using CO2_T_COM’s different regression equation options 
 
  
In general, the equations from Parker give significantly higher costs than the other three sets of 
regression equations. Brown et al., gave the highest cost of the remaining three, while Rui et 
0
400,000
800,000
1,200,000
1,600,000
2,000,000
0 100 200 300 400 500
Capital Cost (2023$/mi)
Pipeline distance (mi)
12-inch Diameter Pipeline 
Parker
McCoy and Rubin
Rui et al.
Brown et al.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -15-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
al., gave the lowest costs. Also note that regardless the capital cost regression equation used, 
capital costs on a per mile basis decrease as the pipeline distance increases, due to economies 
of scale. 
The regression equations from Brown et al., were used in the analysis for this guideline for all 
transport costs, over those of Parker, McCoy and Rubin and Rui et al., since the Brown et al. 
regression equations were based on the most recent costs of the four different sets of 
equations. 
The costs for a surge tank and pipeline control system were taken from an earlier NETL study 
[18]. These costs were in 2000$ and are adjusted to 2011$ in the CO2_T_COM using 
appropriate price indices. The capital costs for a booster pump were determined using an 
equation provided by McCollum and Ogden (2006) [19]. This equation needs the power 
requirements for the booster pumps that McCollum and Ogden also provided, which are based 
on the CO2 mass flow rate and pressure increase through the pump. The pump capital costs 
were in 2005 dollars and are adjusted to 2011$ in the model using appropriate price indices. 
The O&M costs for the pipeline were assumed to be 2.5 percent of the capital costs on an 
annual basis [19]. The O&M costs for the remaining pieces of equipment were assumed to be 4 
percent of the capital costs on an annual basis. The price of electricity used to estimate the cost 
of the electricity used by the pumps was assumed to be the national average electricity price for 
electricity provided to commercial operations in 2011 [20].  
As discussed above, the CO2_T_COM has a financial module that accounts for debt, equity, 
depreciation, and taxes. The model can determine the cost of CO2 (in $/tonne CO2 transported) 
that provides investors with their desired minimum internal rate of return on equity (IRROE). To 
use the financial module, several parameters must be specified. For this guideline’s evaluation, 
it was assumed that it takes three years to complete the construction of the pipeline and that 
the pipeline operates for 30 years (as shown in Exhibit 2-1). The financial parameters used in the 
CO2_T_COM for this guideline’s evaluations are shown in Exhibit 2-3. The model includes a 
project contingency cost calculated for all capital items. NETL guidelines for cost estimating [21] 
recommend using a project contingency factor between 15 percent and 30 percent for the 
budgetary-level type cost estimate that is provided by the CO2_T_COM. The lower factor of 15 
percent was used for the analysis in this guideline (Exhibit 2-3) because the pipeline costs 
provided by the Oil & Gas Journal may include contingency and some taxes. Table notes for 
Exhibit 2-3 provide definitions for the other financial parameters used. 
Exhibit 2-3. Financial parameters used in CO2_T_COM 
Financial Parameter Value 
Percent equity (remainder is debt) (%) A 45 
Cost of equity (%/yr)A 10.77 
Cost of debt (%/yr)A 3.91 
Tax rate (%/yr)B 25.74

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -16-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Financial Parameter Value 
Escalation rate from base year to project start year (%/yr) C 4.8 
Escalation factor from base year to project start year (unitless) D 1.755 
Escalation rate from project start year and beyond (%/yr) 0 
Project contingency factor (%) 15 
Note: Base year = 2011 and project start year = 2023 
APercent equity, cost of equity, and cost of debt are based on values from the largest natural gas transportation companies. These 
values are real rates and are based on a 2.30 percent average real gross domestic product (GDP) deflator (1990–2023) [22]. 
BTax rate is the effective rate (includes federal and state), which is the average rate a company’s pre-tax profits are taxed [23]. 
CCalculated by taking the average of the 2011–2023 percent change over time for the total transmission plant within The Handy-
Whitman Index of Public Utility Construction Costs, 1912 to January 1, 2023 – Cost Trends of Gas Utility Construction  across the six 
regions [11]. 
DObtained by using the equation Escalation factor = (1+ escalation rate from base year to project start year) ( project start year-base year). 
Based on user input settings, CO2_T_COM calculates cash flows for revenues, capital costs and 
O&M costs. These costs are provided initially in constant dollars in the first year of the project 
and then escalated to nominal dollars based on the assumed escalation rate from project start 
year and beyond. The nominal capital costs are depreciated and used to calculate taxes. The 
capital costs, O&M costs, and taxes are subtracted from revenues to give net earnings in 
nominal dollars. The net earnings are discounted using the weighted average cost of capital to 
provide discounted or present value net earnings. The present value net earnings are summed 
to give the net present value or NPV for the project [12]. The model uses the NPV metric to 
estimate the FYBE to transport a tonne of CO2. This occurs via iteration on the $/tonne transport 
price to achieve an NPV of $0 or close to $0. 
Two case studies are provided in this guideline to demonstrate how NETL estimates comparable 
CO2 transport costs varying different aspects of CO2 pipeline transportation. The first 
transportation case study evaluates the impact of regional changes in material and labor costs 
on transport costs. The second transportation case study evaluates the impact of CO2 mass flow 
rate and pipeline distance on transportation cost within a single region. The methodology 
unique to each transport cost case study are described in the following Sections 2.1.1 and 2.1.2.  
2.1.1 Transport Cost Case Study 1: Regional Variation – Methodology 
Transport Cost Case Study 1 evaluates the impact of regional variations in pipeline construction 
and labor costs on CO2 transportation costs. Four transport regions were selected that align 
with Brown et al., pipeline cost regression equations in CO2_T_COM: 1) Great Lakes, Southwest; 
2) Great Plains; and 3) Rocky Mountains. These transportation regions are geographically 
delineated, along with the other Brown et al. transportation regions, in Exhibit 2-4.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -17-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Exhibit 2-4. Brown et al., transportation regions 
 
Each transport region’s average pipeline costs, normalized by pipeline diameter and pipeline 
length, are shown in Exhibit 2-5 broken out by costs category (materials, labor, miscellaneous, 
and rights-of-way) to demonstrate how pipeline costs vary regionally. Exhibit 2-5 costs are 
derived from Brown et al. [15].   
Exhibit 2-5. Brown et al., normalized total pipeline costs broken out by cost category 
 
$0
$20,000
$40,000
$60,000
$80,000
$100,000
$120,000
$140,000
$160,000
$180,0002018$ / in - mi
Materials Labor Miscellaneous ROW

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -18-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
In each of the four transport regions, CO2_T_COM was used to estimate the FYBE cost to 
transport 100 km (62 mi) a maximum daily flow of 13,892 tonnes/day at an 85% capacity factor 
from a power plant. Capacity factor is the ratio of the average annual CO2 mass flow rate to the 
maximum CO2 mass flow rate converted to an annual basis. A 13,893 tonnes/day maximum CO2 
mass flow rate and an 85% capacity factor is equivalent to an average annual CO2 mass flow rate 
of 4.31 million tonnes per year (Mt/yr) of CO2 captured. The maximum mass flow rate is 
important in CO2_T_COM because pipelines must be designed to operate at maximum mass 
flow rates; however annual revenues are a function of average annual mass flow rate. In each 
region, a 100-km (62-mi) pipeline was assumed to connect the capture plant directly to a 
storage project.  
Results of Transport Cost Case Study 1 are shown and described later in Section 3.1.1. These 
regional transport costs are also aggregated with regional CO2 storage costs, as described in 
Section 2.3, to provide Regional T&S Costs reported in Section 3.3. 
2.1.2 Transport Cost Case Study 2: CO2 Mass Flow Rate and Pipeline 
Distance Variations – Methodology  
Transport Cost Case Study 2 evaluates the influence of CO2 mass flow rate and transport 
distance variations on transport cost. Cost data were calculated for two pipeline lengths (100 
km or 62 mi, and 200 km or 124 mi) and two capacity factors (85% and 80%) over maximum 
daily CO2 mass flow rates ranging from 4,000 to 20,000 tonnes/day using the average cost from 
each of the nine Brown et al., transportation regions (shown in Exhibit 2-4). These different 
scenarios represent a range of possible CO2 point sources that might be deploy a CO2 capture 
project. The Transport Cost Case Study 2 results are generated by averaging the transport cost in 
each of the nine transport regions for each unique transport scenario; the results are reported 
in Section 3.1.2.  
2.2 STORAGE COST OVERVIEW AND METHODS 
Storage costs were estimated for all storage case studies in this guideline using the 
CO2_S_COM. The CO2_S_COM is a Microsoft® Excel-based tool that estimates the FYBE cost for 
storing CO2 in a deep saline aquifer. To inject CO2 into the subsurface for storage in a saline-
bearing reservoir, the site owner must comply with the U.S. Environmental Protection Agency 
(EPA) regulations for Class VI injection wells under EPA’s Underground Injection Control Program 
[24], which is authorized under the Safe Drinking Water Act. The site owner must also comply 
with monitoring and reporting requirements under Subpart RR of the Greenhouse Gas 
Reporting Rule [25], which is authorized under the Clean Air Act. The FYBE cost estimated by 
CO2_S_COM accounts for the technology needed and associated cost to conduct storage 
operations in a way that complies with these regulations. The FYBE cost of storage also accounts 
for all financing costs, including interest and principal on debt and minimum desired return on 
equity. 
Most of the original cost data for wells, technology, and labor in the CO2_S_COM are from EPA’s 
economic analysis of the Class VI and Subpart RR regulations and are in 2008$ [26]. When

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -19-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
possible, costs have been updated. For example, the cost to drill and complete all deep wells in 
the model are based on the 2014 American Petroleum Institute-Joint Association Survey. Some 
other costs in the model have been updated based on conversations with industry personnel 
while at conferences.  
The publicly available version of CO2_S_COM has a database with 64 geologic formations from 
across the contiguous U.S. Each geologic formation in CO2_S_COM is divided into sub-areas 
which make up the storage reservoirs. The storage reservoirs were determined by geologists as 
areas within a geologic formation that have similar geologic properties. Because geologic 
properties are very heterogeneous, judgment was required to divide each geologic formation 
into storage reservoirs. Based on the judgment of the geologist, each storage reservoir was 
assigned geologic properties that are representative of that storage reservoir (such as depth to 
the top of the storage reservoir, and thickness, porosity and permeability of the storage 
reservoir). For this guideline, “geologic formation” will be used to define an entire formation 
(e.g., entire Mount Simon), while “storage reservoir” will be used to identify a sub-area of the 
geologic formation. The publicly available version of CO2_S_COM consists of 228 total storage 
reservoirs [27].  
Many of these storage reservoirs were further divided into two or more unique storage 
reservoirs in the modified version of the CO2_S_COM used in this guideline. Storage reservoirs 
that crossed state boundaries were split into one reservoir per state, and storage reservoirs that 
were especially thick were split into multiple thinner (typically 1000 feet thick) stacked reservoir 
intervals.  Other geologic formations and their associated reservoirs were also added. As a 
result, the modified version of the CO2_S_COM used in this guideline used a geologic database 
which includes geologic properties for 314 storage reservoirs from 88 geologic formations from 
across the contiguous U.S. For example, the Mount Simon geologic formation is present in three 
basins (Inter-Basin Arch, Michigan, and Illinois basins), and is present in five states (Illinois, 
Indiana, Michigan, Ohio, and Kentucky).  The Mount Simon is divided into 11 storage reservoirs 
(named Mount Simon 1, Mount Simon 2, and so forth). For example, The Mount Simon 1, 
Mount Simon 2, and Mount Simon 3 are located in the Illinois Basin, in the state of Illinois, and 
are differentiated by depth to the top of the storage reservoir (11,300 feet, 7,240 feet, and 
4,270 feet, respectively); the Mount Simon 4, Mount Simon 5, and Mount Simon 6 are similarly 
located in the Illinois basin, are similarly differentiated by depth, but are located in the state of 
Indiana. 
CO2_S_COM can calculate the prospective CO2 storage resource in each storage reservoir 
assessed. Prospective CO2 storage resource is the mass of CO2 that can potentially be stored in a 
storage reservoir if all the available pore space is utilized [27]. A subsurface reservoir’s 
prospective CO2 storage resource is a yet-to-be-proved CO2 storage capacity. The prospective 
CO2 storage resource for each storage reservoir is calculated in CO2_S_COM assuming pressure 
interference. Pressure interference is the potential impact on effective prospective CO2 storage 
resource that nearby CO2 storage projects in the same storage reservoir can have on each other 
[28]. The CO2_S_COM estimates the impact of pressure interference on prospective CO2 storage 
resource based on an approach proposed by Teletzke et al. (2020) [29] that uses the average 
permeability of the storage reservoir to calculate a factor that reduces the prospective CO2

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -20-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
storage resource. Accounting for pressure interference reduces the prospective CO2 storage 
resource in a given storage reservoir; this reduction, relative to estimates that do not consider 
pressure interference, can be as much as 94% less in storage reservoirs with relatively low 
permeability. All storage costs calculated in this guideline assume there is subsurface pressure 
interference between the multiple projects deployed in the same storage formation. 
Another factor that influences costs is the financial responsibility requirements of the Class VI 
regulations. The financial responsibility aspect requires the CO2 saline storage operator 
purchase a financial instrument that will cover the cost of certain aspects of storage. There are 
four aspects to financial responsibility. The first is the cost of corrective action which is finding 
legacy wells that were drilled into the storage reservoir, determining if they were properly 
plugged and abandoned, and plugging and abandoning those that were not properly plugged 
and abandoned. The second is the cost of plugging and abandoning the injection wells when 
injection ceases. The third is the cost of post-injection site care (PISC) and site closure. In the 
Class VI regulations, PISC is the requirement that the storage operator monitor the CO2 plume 
and pressures in the storage reservoir until the plume stabilizes and pressures decline to levels 
considered acceptable to the regulatory authority. The fourth is the cost of implementing an 
Emergency and Remedial Response (ERR) Plan. An ERR Plan outlines the actions the storage 
operator will take if fluid leaks out of the storage reservoir and into an underground source of 
drinking water (USDW). A USDW is defined by the Class VI regulations as any groundwater with 
salinity less than 10,000 parts per million (ppm). The Class VI regulations define financial 
instruments that are acceptable for meeting the requirements for financial responsibility. For 
this analysis, a trust fund was used to cover the first three aspects and an insurance policy was 
used for the last aspect (i.e., the cost of implementing the ERR Plan). 
Financial parameters used/modeled in the CO2_S_COM for storage cost analyses as part of this 
guideline are shown in Exhibit 2-6. The CO2_S_COM includes a project contingency cost 
calculated for all capital items and a process contingency cost for all monitoring activities. NETL 
guidelines for cost estimating [21] recommend using a project contingency factor of 15–30 
percent for the budgetary-level type cost estimate that is provided by the CO2_S_COM and a 
process contingency factor between 20 percent and 35 percent for small, pilot plant data (small, 
pilot plant storage projects have been completed). The lower factors of 15 percent and 20 
percent were used for the project contingency and process contingency, respectively, for the 
analysis in this guideline (Exhibit 2-6). Notes listed below Exhibit 2-6 provide definitions for the 
other financial parameters used/modeled. 
Exhibit 2-6. Financial parameters used/modeled in CO2_S_COM 
Financial Parameter Value 
Percent equity (remainder is debt) (%) A 45 
Cost of equity (%/yr)A  10.77 
Cost of debt (%/yr)A  3.91 
Tax rate (%/yr)B 25.74

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -21-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Financial Parameter Value 
Escalation rate from base year to project start year (%/yr) C 3.5 
Escalation factor from base year to project start year (unitless) D 1.663 
Escalation rate from project start year and beyond (%/yr) 0 
Project contingency factor (%) 15 
Process contingency factor (%) 20 
Financial responsibility instrument Trust Fund and Insurance 
Escalation rate for financial instrument (%/yr) E 2.32 
Trust Fund growth rate (%/yr) 5 
APercent equity, cost of equity, and cost of debt are based on values from the largest natural gas storage companies. These values 
are real rates and are based on a 2.30 percent average real GDP deflator (1990–2023) [22]. 
BTax rate is the effective tax rate (includes federal and state), which is the average rate a company’s pre-tax profits are taxed [23]. 
CCalculated by taking the average of the 2008–2023 percent change over time for the storage plant gas holders found within the 
Handy-Whitman Index of Public Utility Construction Costs, 1912 to January 1, 2023 – Cost Trends of Gas Utility Construction  across 
the six regions [11]. 
DObtained by using the equation Escalation factor = (1+ escalation rate from base year to project start year) ( project start year-base year). 
EAverage real gross domestic product deflator (1990–2023) [22]. 
Three case studies are provided in this guideline to demonstrate how NETL estimates 
comparable CO2 storage costs varying different aspects of CO2 saline storage. The first storage 
cost case study evaluates the impact of regional changes in the quality and availability of 
storage reservoirs on storage costs as cumulative CO2 storage thresholds increase. The second 
storage cost case study evaluates the impact of CO2 storage project design, specifically storage 
formation geology and storage project execution parameters on storage costs. The third storage 
cost case study evaluates how variation in annual CO2 mass flow rate impacts storage cost. The 
methodology unique to each storage cost case study are described in the following Sections 
2.2.1, 2.2.2, and 2.2.3.  
2.2.1 Storage Cost Case Study 1: Regional Variation – Methodology 
To demonstrate how storage costs vary regionally, CO2_S_COM was used to estimate storage 
costs for storage projects in basins associated with the four Brown et al., transport regions 
selected in Section 2.1.1. In each of the four regions, the storage projects modeled were 
assumed to inject a maximum daily mass flow rate of 13,892 tonnes/day of CO2 captured from a 
CO2 point source with a capacity factor of 85 percent (equivalent to 4.31 Mt per year on 
average). For each storage project modeled, financial assumptions were kept the same, as 
outlined in Exhibit 2-6. Each storage project’s design and geologic assumptions were assumed 
the base scenario described in the next section’s (Section 2.2.2) Exhibit 2-9. 
The four basins assessed for comparison in Storage Cost Case Study 1 are the Illinois Basin (in 
the Great Lakes region), the East Texas Basin (in the Southwest region), the Williston Basin (in 
the Great Plains region), and the Powder River Basin (in the Rocky Mountain region) are 
mapped in Exhibit 2-7. The unique storage reservoirs within the four basins, the reservoir’s

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -22-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
extents, and the geographic centroid of each, are also mapped in color in Exhibit 2-7.  These 
reservoirs are listed by basin in Exhibit 2-8. 
Exhibit 2-7. Locations of four basins selected for this analysis 
 
Exhibit 2-8. Regional storage variation case study basins, geologic formations and associated storage reservoirs 
Corresponding 
Transport 
Region 
Geologic 
Storage Basin Geologic Formations Storage Reservoirs in  CO2_S_COM Geologic Database 
Great Lakes Illinois 
Mount Simon;  
Saint Peter;  
Knox 
Mount Simon 1, 2, 3, 4, 5, and 6;  
Saint Peter 1, 2, 3, 4, 5, and 6;  
Knox 1, 2, 3, 4, 5, and 6 
Southwest East Texas Woodbine;  Paluxy Woodbine 1;  Paluxy 1, 2, and 3 
Great Plains Williston 
Basal Cambrian; 
Broom Creek; 
Inyan Kara; 
Madison Group- 
Mission Canyon; 
Red River; 
 
Basal Cambrian 2, 3, 4, 5, 6, 7, and 8; 
Broom Creek 1, 2, and 3 
Inyan Kara 1, 2, and 3 
Madison Group - Mission Canyon 1, 2, 3, and 4; 
Red River 1 and 2;

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -23-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Corresponding 
Transport 
Region 
Geologic 
Storage Basin Geologic Formations Storage Reservoirs in  CO2_S_COM Geologic Database 
Rocky Mountain Powder River 
Frontier; 
Lakota; 
Madison; 
Minnelusa; 
Muddy; 
Lower Sundance 
Frontier 1 and 2, 
Lakota 1 and 2; 
Madison 1;  
Minnelusa 1 and 2 
Muddy 4 and 7; 
Sundance 1 and 2 
CO2 cost-supply curves were generated for each basin to demonstrate each region’s cumulative 
prospective storage resource utilizing their available storage reservoirs.  The cost-supply curve 
plots the cumulative prospective CO2 storage resource available as FYBE storage cost increases, 
and therefore can be used to compare regional storage costs at specific cumulative storage 
thresholds.  The CO2 cost supply curves generated in this case study are used to report the 
minimum FYBE cost required in each basin to store CO2 at the following cumulative storage 
thresholds: 5 billion tonnes Gt, 10 Gt, 15 Gt, 25 Gt, and 50 Gt.  
The Storage Cost Case Study 1 results are shown in Section 3.2.1. The storage cost in each basin 
at the 5 Gt threshold, specifically, was used for the Guideline T&S Costs aggregated in Section 
3.3.  
2.2.2 Storage Cost Case Study 2: Project Design Variations – 
Methodology 
The first storage cost case study evaluates storage project design variations and their impact on 
storage costs. Storage project design includes storage project geology parameters and storage 
project execution parameters. Three storage project design scenarios were assessed in this case 
study: 1) low-cost; 2) base; and 3) high-cost. The modifications in CO2_S_COM input parameters 
across cases are illustrated in Exhibit 2-9.  
Exhibit 2-9. Modeling parameters for low-cost, base, and high-cost scenarios 
Parameter Modeled Low-Cost Case Base Case High-Cost Case 
Storage coefficient P90 P50 P10 
Structural setting Regional dip 
Site selection and site 
characterization 
2 yr  
(1 site) 
3 yr  
(1 site) 
3 yr  
(2 sites) 
Permitting and 
construction (yr) 2 2 4 
Injection operations (yr) 30 
PISC and site closure (yr) 25 50 50 
3D seismic (2008$/mi2) 60,000 67,000 80,000

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -24-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Deep monitoring wellsA 
1 dual-completed 
monitoring well per 
injection well with 
maximum of 15 wells 
1 dual-completed 
monitoring well per 
injection well with 
maximum of 25 wells 
1 dual-completed 
monitoring well per 
injection well with 
maximum of 50 wells 
Density of wells needing 
corrective action 
(well/mi2) 
0.01 0.1 0.2 
AThese are calculated values, not model inputs. Dual-completed monitoring wells are completed in the reservoir and above the 
seal. 
Cost parameters for each cost scenario modeled were modified from base case conditions to 
reflect a savings in cost or an additional cost burden due to potentially unique operational 
situations associated with changes to project design. The impact of these variations in geology 
and project execution variability are explored in more detail in Section 2.2.2.1 and Section 
2.2.2.2, respectively. 
2.2.2.1 Storage Project Geologic Factors 
Geologic factors that impact pore volume availability and accessibility are a primary cost driver 
for CO2 storage. These geologic factors include the available area of the reservoir, the thickness, 
the porosity, and the storage coefficient. The storage coefficient depends on the lithology, 
depositional environment, and structural setting.  
Additionally, reservoir thickness and permeability affect injectivity which, in turn, may influence 
the number of injection wells needed to safely inject the annual volume of CO2 delivered to a 
storage site. Thick, permeable reservoirs enable higher injectivity [30] and higher injectivity 
results in fewer injection wells needed to achieve the targeted injection rate for a given project, 
and thus a lower relative per tonne cost to store CO2. Furthermore, thick, porous reservoirs with 
high storage coefficients [31] will tend to generate a smaller areal extent for the CO2 plume and 
have lower testing and monitoring costs relative to thinner formations with lower storage 
coefficients, resulting in a lower relative per tonne cost to store CO2. 
Exhibit 2-10 is a cross-plot (log-log scale) of reservoir quality (the product of reservoir porosity 
[Φ], storage coefficient [E], and height [h]) and FYBE cost to store a tonne of CO2. Exhibit 2-10 
includes data from each storage reservoir within the CO2_S_COM, but specifically highlights 
storage reservoirs within the basins featured as part of this analysis. All data plotted in Exhibit 
2-10 align with the base case. In general, storage reservoirs with higher reservoir quality 
typically have lower FYBE costs for storage. On the other hand, reservoirs with lower reservoir 
quality typically have higher FYBE costs for storage. A cross-plot of the product of permeability 
and reservoir thickness will also show a similar distribution.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -25-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Exhibit 2-10. Reservoir quality against FYBE cost for base case 
 
Reservoir geologic have a significant influence on the resulting CO2 plume and pressure front. 
The areal extent of the CO2 plume, for instance, is another critical cost driver for a project. The 
monitoring and testing program that is part of a UIC Class VI permit is designed to monitor the 
extent of the CO2 plume as it evolves over the lifetime of a project. Larger plumes increase the 
areal extent of the monitoring program, possibly increasing the number of monitoring wells 
needed, and the areal extent of seismic surveys designated to track the plume. The areal extent 
of a CO2 plume can be calculated based on the storage reservoir’s geologic properties and the 
total CO2 injected over the duration of a project as indicated in Equation 1 [31]. 
 
𝐴஼ைଶ =  𝐺஼ைଶ ℎ𝜌஼ைଶ𝛷𝐸⁄  Equation 1 
 
Where: 
ACO2 = area of the CO 2 plume (ft2) 
GCO2 =  mass of total CO 2 stored (tonnes) 
h = thickness of the storage reservoir (ft) 
ρCO2 = density of the stored CO 2 at storage reservoir conditionsc (pounds per ft3) 
Φ = porosity of the storage reservoir rock (percent) 
E = storage coefficient for the storage reservoir rock (unitless) 
The areal extent of the CO2 plume is proportional to the mass of CO2 injected over the life of a 
project and inversely proportional to storage reservoir quality. The approximated area of a 
 
c The units for CO2 density (ρCO2) in Equation 1 must be converted to tonnes per cubic foot to attain A CO2 in 
square feet. The approximate conversion is 1 tonne = 2,204 pounds. 
0.01
0.10
1.00
10.00
100.00
$1 $10 $100 $1,000
Reservoir Quality (ΦEh) (ft)
FYBE Cost (2023$/tonne)
Non-evaluated reservoirs
Illinois
East Texas
Williston
Powder River

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -26-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
plume in the storage reservoir, as shown in Equation 1, is highly deterministic and does not 
account for geologic uncertainty. In the CO2_S_COM, an uncertainty factor of 1.25 is applied to 
the results of Equation 1 to account for geologic uncertainty in the subsurface in estimating the 
CO2 plume area size. Overall, Equation 1 shows how geologic factors like reservoir thickness, 
porosity, and storage coefficient as well as injected CO2 volumes, can all directly impact the size 
of the resulting CO2 plume.  
Exhibit 2-11. Conceptual depiction of critical CO 2 storage cost driver boundaries and definitions part of 
CO2_S_COM 
 
Other key cost-influencing factors are also subject to the approximate size of the resulting CO2 
plume. Exhibit 2-11 summarizes these critical cost driver boundaries considered within 
CO2_S_COM. For instance, the three dimensional (3D) seismic monitoring boundary is 
highlighted and is based off the size of the CO2 plume uncertainty area, depth to top of the 
storage reservoir, and angle from CO2 plume uncertainty edge to the ground surface (set at 45 
degrees). As the CO2 plume increases in size, so does the area in which 3D seismic monitoring is 
conducted to evaluate CO2 plume evolution. The pressure front represents EPA’s definition of 
the Area of Review (AoR). It is also an approximation, derived via the product of a multiplier (set 
at 10) and the CO2 plume uncertainty area. While an important attribute to evaluate and 
monitor as part of an EPA UIC Class VI injection project and can limit the number of viable 
storage projects per formation, the pressure front is not a major cost factor within CO2_S_COM.  
For each storage reservoir modeled, the prospective CO2 storage resource, as defined by 
Goodman et al. (2011) [31] and the Society of Petroleum Engineers (2017) [27], depends upon 
the available surface area, the porosity, reservoir thickness, CO2 density at depth, and the 
storage coefficient. Storage reservoirs with larger storage capacities can typically attain unit cost 
savings (i.e., $/tonne basis) via economies of scale by storing larger volumes of CO2 than smaller 
reservoirs [4, 8]. The storage coefficient depends on the lithology, depositional environment,

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -27-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
and structural setting, and is listed in the CO2_S_COM geologic database [32]. Exhibit 2-12 lists 
the storage coefficient for the Mount Simon geologic formation for the regional dip structural 
setting that was evaluated in this guideline for low-cost, base, and high-cost cases. The lithology 
and depositional environment is provided for reference.  
Exhibit 2-12. CO2 storage coefficients for the Mount Simon geologic formation  
Basin Geologic Formation  Lithology Depositional Environment 
Storage 
Coefficient 
(P10) - Low-
Cost Case 
Storage 
Coefficient 
(P50) - Base 
Case 
Storage Coefficient 
(P90) - High-Cost 
Case 
Illinois Mount Simon Clastic Strandplain 5.58% 5.63% 6.30% 
The impact of the storage coefficient variability reported in Exhibit 2-12 on storage costs are 
demonstrated for the Mount Simon 3 storage reservoir in Exhibit 3-5 in Section 3.2.2. 
2.2.2.2 Storage Project Execution Factors 
The important activities impacting costs for these stages as modeled for this guideline’s low-
cost, base, and high-cost scenarios in Exhibit 2-9 are: 
 Site screening: One year 
 Site selection and site characterization: One to two years 
o One or possibly two sites are subjected to an initial screening that involves 2 lines 
of a two-dimensional (2D) seismic survey covering the estimated CO2 plume 
uncertainty area (shown conceptually in Exhibit 2-11).    
o This is followed up with the drilling of one stratigraphic well, sampling and 
testing from this stratigraphic well and a 3D seismic survey covering the CO2 
plume uncertainty area; property access and the right to inject into pore space 
are also leased.  
o This stage concludes with submittal to the regulatory authority of required plans 
(AoR and corrective action plan, testing and monitoring plan, injection well 
plugging plan, PISC and site closure plan, and ERR plan) for Class VI injection well 
permit. The AoR is an area where injection of CO2 elevates pressures in the 
storage reservoir that may cause fluid to leak out of the storage reservoir and 
toward an USDW. 
 Permitting and construction: Two to four years 
o This stage begins with the regulatory authority responding to submitted 
documents, the operator responding to any requests from the regulatory 
authority and the operator receiving conditional approval of the Class VI permit.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -28-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
o The operator drills the injection wells and submits updated Class VI permit 
documents based on data collected during drilling to the regulatory authority. 
The regulatory authority then provides approval of the Class VI permit.  
o Demonstration of financial responsibility. 
o Installation of buildings, surface equipment, monitoring wells, and other 
monitoring equipment per submitted testing and monitoring plan. 
o Except for drilling injection wells, most of the capital costs described above are 
incurred during the last year of construction. 
 Operations: 30 years 
o Injection of an annual average mass of CO2 each year for 30 years . 
o Assumes all monitoring wells are sampled at least once annually and a 3D 
seismic survey is performed once every 5 years; seismic surveys are based on the 
size of the CO2 plume uncertainty area size. 
o AoR review and permit plans updates occur every five years. 
o Annual update of financial responsibility estimates/report. 
o Plugging injection wells at conclusion of injection operations. 
o Trust Fund is used to cover financial responsibility requirements for corrective 
action, injection well plugging, and PISC and site closure. Payments into the trust 
fund occur over a three-year period starting in the last year of permitting.  
o Emergency and remedial response is covered by an insurance policy with annual 
payments proportional to the mass of CO2 injected in that year. 
 PISC and site closure: 25 to 50 years 
o Monitoring continues per submitted post-injection and site care and site closure 
plan (i.e., monitoring wells continue to be sampled at least annually and 3D 
seismic surveys are conducted every 5 years per the plan). 
o Monitoring wells are plugged, and other monitoring equipment are removed, 
and the site is restored at the end of PISC. 
o While the trust fund is available to the regulatory authority, the regulatory 
authority can release money from the trust fund if they feel the fund is 
adequately funded. As such it was assumed that the costs during this period are 
covered by the storage site operator’s Trust Fund. 
 Long-term stewardship: This stage is not explicitly included in the model. The possible 
need to cover this cost is provided for by including in the model a state-sponsored Long-
term Stewardship Trust Fund that the storage operator pays into during operations.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -29-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
2.2.3 Storage Cost Case Study 3: CO2 Mass Flow Rate Variations – 
Methodology 
To demonstrate how CO2 mass flow rate impacts CO2 storage costs, CO2_S_COM was used to 
estimate storage costs for different saline storage projects sized to store from an average of 1.42 
Mt/yr to an average of 5.14 Mt/yr, and range in capacity factors from 80% to 85%, as shown in 
Exhibit 2-13.  
The CO2 storage project in each mass flow rate scenario was assumed to be located in the 
Illinois Basin’s Mount Simon 3 storage reservoir, using financial parameters outlined in Exhibit 
2-6 and the base project design scenario parameters outlined in Exhibit 2-9. The injection well 
count listed in Exhibit 2-13 is determined in CO2_S_COM by dividing the maximum annual CO2 
mass flow rate by the injection rate capacity per well, assumed in this guideline to be 1.336 
Mt/yr per well. 
Exhibit 2-13. CO2 mass flow rates and injection well count assessed in Storage Cost Case Study 3 scenarios 
Average Annual 
CO2 Injection Rate 
Maximum 
Annual CO2 
Injection Rate 
Capacity 
Factor 
CO2 Storage 
Project Injection 
Well Count 
Mt/yr Mt/yr % Count 
5.14 6.05 85 5 
4.89 5.75 85 5 
4.85 5.71 85 5 
4.62 5.44 85 5 
4.53 5.33 85 4 
4.31 5.07 85 4 
3.20 4.00 80 3 
3.17 3.96 80 3 
3.11 3.89 80 3 
1.84 2.16 85 2 
1.80 2.12 85 2 
1.71 2.01 85 2 
1.53 1.80 85 2 
1.50 1.76 85 2 
1.42 1.67 85 2 
 
2.3 GUIDELINE T&S COSTS METHODOLOGY 
The final case study in this guideline demonstrates combining regional transport and storage 
costs to create comparable T&S costs by region. This case study combined regional transport 
costs from the four U.S. regions, described in Section 2.1.1. with storage costs from 
corresponding basins as described Section 2.2.1. The transport cost in each region assumed fixed 
pipeline distance (100 km, 62 mi) scenarios. The storage costs in each region assumed the FYBE 
cost of a storage project in a basin storing a cumulative 5 Gt of CO2 over 30 years.  Both transport 
and storage cost scenarios assumed the same average CO2 mass flow rate (4.31 Mt/yr) and

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -30-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
capacity factor (85%). The resulting combined T&S costs are termed “Guideline T&S Costs”, and 
represent comparable T&S costs that can be used in energy systems studies. The Guideline T&S 
Costs are effectively the T&S expense paid by the CO2 capture project owner to transport and 
store each tonne of CO2 captured during the assumed 30-year operational period. 
3 MODELING RESULTS 
This section provides an overview of the modeling results from the various case studies used to 
generate T&S costs under different modeling scenarios. These case study results and sensitivity 
trends were generated to be able to be easily referenced by a variety of energy systems studies 
that would incorporate T&S costs. Results are from modeling runs performed with the 
CO2_T_COM and the CO2_S_COM using parameters described above as well as default values 
within the models.  
3.1 CO2 TRANSPORT COST RESULTS OVERVIEW 
This section provides the transport cost results of the CO2 pipeline transport cost modeling, 
broken out by the two CO2 transport cost case studies described in Sections 2.1.1 and 2.1.2.  
These case studies demonstrated the impact of regional variations in material and labor costs, 
and variations in CO2 mass flow rate and pipeline length, respectively, on the cost of transport. 
3.1.1 Transport Cost Case Study 1: Regional Variation – Results 
The case study described in Section 2.1.1 was designed to estimate the FYBE transportation cost 
for a 100 km (62 mi) pipeline between a capture project capturing an annual average of 4.31 
Mt/yr of CO2 and a storage project site in each of four transportation regions. Modeling results 
in each region estimated that the lowest cost configuration for pipelines will have a 12-in pipe 
diameter and one booster pump. Transport costs for this configuration are reported in Exhibit 
3-1. 
Despite all pipelines having the same length and diameter in their design, FYBE transportation 
costs vary between regions. This variation is due to the Brown et al., regression equations’ 
pipeline construction material and labor cost factors which vary by region (Exhibit 2-5).  
Exhibit 3-1. Comparable CO 2 transport costs by region  
Transport Region Transport Cost (2023$/tonne) 
Great Lakes 2.35 
Southwest 2.42 
Great Plains 1.58 
Rocky Mountain 1.58

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -31-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
3.1.2 Transport Cost Case Study 2: CO2 Mass Flow Rate and Distance 
Variations – Results 
The case study described in Section 2.1.2 was designed to estimate FYBE transportation cost as 
a function of CO2 mass flow rate, pipeline distance, and the CO2 source’s capacity factor (which 
defines the average to maximum CO2 mass flow rate ratio). Transportation costs for this 
configuration are shown in Exhibit 3-2.  
Exhibit 3-2. FYBE cost sensitivity to pipeline length, pipeline capacity factor, and mass of CO 2 transported 
 
Exhibit 3-2 indicates higher CO2 mass flow rates have lower FYBE transport costs on a per tonne 
of CO2 basis. This is largely due to economies of scale benefits related to pipeline diameter (i.e., 
a small increase in pipeline diameter and pipeline material can result in a large increase in CO2 
capacity). Additionally, higher capacity factor assumptions tend to offer a cost savings as shown 
by the relationship between the green and blue lines in Exhibit 3-2. As the mass flow rate 
increases, the diameter of the pipe or the number of pumps may change. There are some small 
discontinuities when the pipeline configuration changes (such as at 11,000 tonne/day for the 
100-km pipeline when the number of pumps increases from zero to one and at 14,000 
tonne/day for the 200-km pipeline when the number of pumps increases from two to three) 
which demonstrate where lower capacity factors cause a slight increase in FYBE costs. Exhibit 
3-2 also demonstrates that the longer the pipeline, the higher the FYBE cost, with the cost being 
roughly proportional to the length at the two lengths investigated. 
 
3.2 CO2 STORAGE COSTS RESULTS OVERVIEW 
This section provides the storage cost results of the CO2 saline storage cost modeling, broken 
out by the three CO2 storage cost case studies described in Sections 2.2.1, 2.2.2, and 2.2.3.  
These case studies demonstrated the impact of regional variations in drilling costs and geology, 
variations in project design, and variations in CO2 mass flow rate, respectively, on the cost of 
storage.  
$0
$1
$2
$3
$4
$5
$6
$7
$8
$9
$10
$11
2,000 4,000 6,000 8,000 10,000 12,000 14,000 16,000 18,000 20,000 22,000
FYBE Cost (2023$/tonne)
Maximum CO2 Flow in Pipe (tonnes/day)
100 km, 80% capacity factor
100 km, 85% capacity factor
200 km, 80% capacity factor
200 km, 85% capacity factor

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -32-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
3.2.1 Storage Cost Case Study 1: Regional Variation – Results 
As described in Section 2.2.1, the cost of storing a tonne of CO 2 in a basin at a given cumulative 
CO2 mass threshold varies depending on the basin’s reservoir-specific geologic attributions and 
regional changes in the cost of drilling. Exhibit 3-3 quantifies the regional variation in storage 
costs with a supply curve that presents the prospective cumulative resource potential for CO 2 
that can be theoretically stored in reservoirs within each of the four select basin along with 
their associated FYBE cost to store CO2, for the base case conditions outlined in Exhibit 2-9. 
Exhibit 3-3 graphs cumulative prospective CO2 storage resource thresholds (5 Gt, 10 Gt, 15 Gt, 
25 Gt, and 50 Gt CO2) to demonstrate the minimum FYBE saline storage FYBE costs at each 
threshold.  
Exhibit 3-3. Cumulative prospective CO 2 storage resource cost supply curves for base case  
 
The East Texas, Illinois, and Williston basins have a similar flat cost supply trend from 0-60 Gt., 
with the Williston Basin having slightly higher costs from 0-50 Gt, and the East Texas Basin’s 
cost increasing to be closer to the Williston Basin’s costs after 35 Gt. These three basins have 
abundant, large, high-quality storage reservoirs. The Powder River Basin’s cost supply curve is 
relatively steep by comparison, indicative of the basin having fewer, smaller high-quality 
$0
$5
$10
$15
$20
$25
$30
$35
$40
$45
$50
0 10 20 30 40 50 60 70 80 90 100
FYBE Cost (2023$/tonne) 
Cumulative Prospective CO2 Storage Resource (Gt)
Illinois
East Texas
Williston
Powder River
5 Gt
10 Gt
15 Gt
25 Gt
50 Gt

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -33-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
storage reservoirs. The geologic reservoir quality-determining properties like thickness, 
porosity, and area that influence these cost trends are discussed in detail in Section 2.2.2.1.  
The minimum FYBE cost data extracted from the curves in Exhibit 3-3 at the cumulative CO2 
storage thresholds are shown in tabular form in Exhibit 3-4. 
Exhibit 3-4. Minimum FYBE CO 2 storage cost in four basins at different cumulative prospective CO 2 storage 
resource thresholds for base case 
Basin 
Cumulative CO2 Injected and Stored 
5 Gt 10 Gt 15 Gt 25 Gt 50 Gt 
Minimum FYBE CO2 Cost [2023$/tonne] 
Illinois 7.65 8.12 
East Texas 7.92 10.31 
Williston 10.59 10.94 
Powder River 14.90 17.45 45.72 A 
 
APowder River Basin’s maximum cumulative prospective storage resource is less than 25 Gt in the base case modeling scenario. 
Reported costs of $45.72/tonne (2023$) reflect the cost to store the maximum cumulative potential CO 2 mass in the basin 23.4 
Gt. 
 
Guideline T&S Costs in Section 3.3 use the minimum FYBE cost of CO 2 storage at the 5 Gt 
threshold for the base case reported in Exhibit 3-4.  
3.2.2 Storage Cost Case Study 2: Project Design Variations – Results 
The FYBE storage cost in a single storage reservoir can vary with assumptions about geologic 
parameters, and assumptions about the execution of the storage project. Exhibit 3-5 illustrates 
the difference in FYBE cost of CO2, broken out by project phases (reported as a percent 
contribution), for a CO2 storage project in the Illinois Basin’s Mount Simon 3 storage reservoir 
for the low-cost, base, and high-cost scenarios outlined in Exhibit 2-9. Project phases imply 
capital costs unless marked “O&M”, in which case these costs are operations and maintenance 
expenditures. Storage project geology assumptions between the low-cost, base, and high-cost 
scenarios are discussed in more detail in Section 2.2.2.1, and are associated with storage 
coefficient. Storage project execution assumptions between the three scenarios are discussed in 
more detail in 2.2.2.2, and are associated with duration of pre-operational project phases (i.e., 
site selection and site characterization; permitting and construction), the duration of the post-
operational project phase (i.e., PISC), 3D seismic costs, the maximum count for deep monitoring 
wells, and the density of wells needing corrective action.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -34-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Exhibit 3-5. CO2 storage project FYBE cost, broken out by project phase, in the Mount Simon 3 for low-cost, base, 
and high-cost scenarios 
 
Overall storage costs increase from the low-cost case to the high-cost case due to changes in the 
following parameters listed in Exhibit 2-9: 
 Storage coefficient decreases, reducing the storage volume per unit area and increasing 
the plume size and associated monitoring costs (primarily 3D seismic costs). 
 Number of years to complete site selection and site characterization and permitting and 
construction increases, delaying operations and positive cash flow from injection 
revenue. 
 PISC and site closure period of 25 years in the low-cost case increases to the default 
period of 50 years for the base and high-cost cases, increasing monitoring and financial 
responsibility costs. 
 3D seismic costs increase from $60,000/mi2 to $80,000/mi2 (in 2008$). 
 Number of monitoring wells drilled increases. 
 Increasing number of wells requiring corrective action increases the cost to perform 
corrective action and increases the cost of the financial instrument to cover this cost for 
financial responsibility. 
0.02% 0.03% 0.02%
5.0% 3.0% 5.9%6.0% 7.6% 5.6%10.0%
10.7%
11.1%
49.1%
62.0%
45.6%
23.6%
12.6%
26.1%
6.2%
4.0%
5.7%
 $-
 $1.00
 $2.00
 $3.00
 $4.00
 $5.00
 $6.00
 $7.00
 $8.00
 $9.00
 $10.00
Mount Simon 3 Mount Simon 3 Mount Simon 3
Base Case Low-Cost High-Cost
FYBE Cost (2023$/tonne)
Site Screening
Site Selection & Site Characterization
Permitting & Construction
Operations
Operations (O&M)
PISC and Site Closure
PISC and Site Closure (O&M)
$7.65
$5.64
$9.51

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -35-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
 
3.2.3 Storage Cost Case Study 3: CO2 Mass Flow Rate Variations – 
Results 
Exhibit 3-6 reports the FYBE cost of storage for project scenarios of varying average annual CO2 
mass flow rate (Mt/yr) and maximum CO2 mass flow rate (converted to a Mt/yr equivalent). As 
described in Section 2.2.3, all the results in this case study are from CO2_S_COM runs for 
storage projects in the Illinois Basin’s Mount Simon 3 storage reservoir, which assumed the base 
project design scenario outlined in Exhibit 2-9.  
Exhibit 3-6. Mount Simon 3 storage reservoir FYBE costs for different CO 2 mass flow rates 
Average Annual 
CO2 Injection Rate 
Maximum 
Annual CO2 
Injection Rate 
Capacity 
Factor 
CO2 Storage Project 
Injection Well 
Count 
CO2 Storage Cost 
Mt/yr Mt/yr % Count 2023$/tonne 
5.14 6.05 85 5 $7.77 
4.89 5.75 85 5 $7.88 
4.85 5.71 85 5 $7.90 
4.62 5.44 85 5 $8.08 
4.53 5.33 85 4 $7.48 
4.31 5.07 85 4 $7.65 
3.20 4.00 80 3 $7.77 
3.17 3.96 80 3 $7.80 
3.11 3.89 80 3 $7.87 
1.84 2.16 85 2 $8.47 
1.80 2.12 85 2 $8.55 
1.71 2.01 85 2 $8.77 
1.53 1.80 85 2 $9.28 
1.50 1.76 85 2 $9.38 
1.42 1.67 85 2 $9.65 
The per tonne of CO2 FYBE storage cost in a storage reservoir tends to decrease as the CO2 mass 
flow rate (i.e., planned injection rate) increases, primarily due to economies of scale. Exhibit 3-7 
shows graphically the relationship between FYBE storage cost and the average CO2 mass flow 
rate from Exhibit 3-6, and highlights the impact of adding additional injection wells to a CO2 
storage project.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -36-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Exhibit 3-7. Average annual CO 2 injection rate impact on FYBE cost of CO 2 storage in the Mount Simon 3 
 
Note that the linear relationship between the CO2 mass flow rate and the FYBE cost in Exhibit 
3-7 changes when the required number of injection wells change; this is due to the increase in 
capital and operating costs associated with the additional well(s). For example, the jump in FYBE 
cost of $7.48/tonne at an average annual mass flow rate of 4.53 Mt/yr (equivalent to a 
maximum injection rate of 5.33 Mt/yr) to $8.08/tonne at 4.62 Mt/yr (equivalent to a maximum 
injection rate of 5.44 Mt/yr) is due mostly to the extra capital and operating expenses 
associated with adding a fifth injection well. The injection well count requirement is determined 
in CO2_S_COM by dividing the maximum annual CO2 mass flow rate by the injection rate 
capacity per well, (assumed in this guideline to be 1.336 Mt/yr per well). 
3.3 GUIDELINE T&S COSTS RESULTS 
Exhibit 3-8 reports the “Guideline T&S Costs” in the Midwest, Texas, North Dakota, and 
Montana study regions. The Guideline T&S Costs, as described in Section 2.3, are an aggregate 
of the regional transport cost results from the Regional Variation Transport Case Study, and the 
regional storage cost results at the 5 Gt storage threshold from the Regional Variation Storage 
Case Study. The study regions align with each of the transport regions described in Section 2.1.1 
and each of the storage basins in Section 2.2.1, as shown in Exhibit 3-8.  
Exhibit 3-8. Guideline T&S Costs by study region  
Guideline 
Region 
Transportation 
Region Storage Basin Transport Cost (2023$/tonne) Storage Cost (2023$/tonne) Total T&S Cost (2023$/tonne) 
Midwest Great Lakes Illinois 2.35 7.65 10.00 
Texas Southwest East Texas 2.42 7.92 10.34 
North 
Dakota Great Plains Williston 1.58 10.59 12.17 
 $7.00
 $7.50
 $8.00
 $8.50
 $9.00
 $9.50
 $10.00
0 1 2 3 4 5 6
FYBE Cost (2023$/tonne)
Average CO2 Mass Flow Rate (Mt/yr)
2 Injection Wells
3 Injection Wells
4 Injection Wells
5 Injection Wells

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -37-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Guideline 
Region 
Transportation 
Region Storage Basin Transport Cost (2023$/tonne) Storage Cost (2023$/tonne) Total T&S Cost (2023$/tonne) 
Montana Rocky Mountains Powder River 1.58 14.90 16.48 
 
The Guideline T&S Costs demonstrate that when transport distances are kept relatively low (in 
this case, 100 km (62 mi)), indicative of local siting of storage relative to the capture location, 
transport represents a minor constituent of the overall T&S costs; consequently, storage 
represents a larger portion of overall T&S costs.   
 
The range of Guideline T&S Costs can be used as a basis for energy systems studies 
incorporating T&S costs, provided transport and/or storage project specifics are not known, or 
unaccounted for. However, as the Guideline T&S Costs demonstrate, geographic location 
impacts cost drivers like material costs, labor costs, drilling costs, and availability of quality 
storage reservoir geology.  If possible, it is recommended project(s) locations be accounted for 
when performing energy systems studies. The variability in transport and storage costs 
presented in the two transportation case studies (Section 3.1) and the three storage case 
studies (Section 3.2), further demonstrate the importance of accounting for CCS project design 
specifics (e.g., CO2 mass flow rate, pipeline distance, and geographic location) in energy systems 
studies when feasible.  
  
4 REVISION CONTROL 
Exhibit 4-1. Revision table 
Revision 
Number Revision Date Description of Change 
1 September 30, 2013 Updated cost estimates. 
2 February 12, 2014 Document edited and formatted. 
3 November 30, 2016 Updated cost estimates. Document edited. 
4 July 31, 2017 Updated cost estimates. Document edited. 
5 November 6, 2017 Updated cost estimates for high-cost with water treatment case. Document edited. 
6 February 11, 2019 
Updated financial parameters and electricity price. 
New methodology for high-cost cases with water management and treatment 
Document edited. 
7 August 19, 2019 Updated financial parameters. New methodology for obtaining real costs.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -38-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
Revision 
Number Revision Date Description of Change 
Document edited. 
8 March 15, 2024 
Updated financial parameters to put results in real 2023$. 
Updated transport capital cost equations. 
Removed anticline and dome structural setting analyses. 
Removed high-cost cases with water management and treatment. 
Added storage results accounting for pressure interference. 
Document edited. 
9 July 11, 2024 
Report reorganized to separate transport, storage, and combined T&S case 
study modeling and results. 
Storage cost sensitivity case studies added to demonstrate impact of variability 
in regional variations, project design, and CO 2 mass flow rates on costs. 
“Guideline T&S Costs” for comparable combined T&S costs reported at the 5 Gt 
threshold as a separate case study. 
Document edited.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -39-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
REFERENCES 
 
[1]  National Petroleum Council (NPC), "Meeting the Dual Challenge: A Roadmap to 
At-Scale Deployment of Carbon Capture, Use, and Storage - Technology 
Introduction," NPC, 2021. 
[2]  Intermountain West Energy & Sustainability & Transitions, "On the raod to carbon 
neutrality in the Intermountain West - Phase One Final Report. Chapter 4: CO2 
Storage and Utilization," Los Alamos National Laboratory and the National Energy 
Technology Laboratory, Los Alamos, New Mexico, 2022. 
[3]  Vikara, D., Shih, C., Lin, S., Guinan, A., Grant, T., Morgan, D., and Remson, D., "U.S. 
DOE’s Economic Approaches and Resources for Evaluating the Cost of 
Implementing Carbon Dioxide Capture, Utilization, and Storage (CCUS)," Journal 
of Sustainable Energy Engineering, vol. 5, no. 4, pp. 307-340, 2017.  
[4]  T. Grant, A. Guinan, C. Shih, S. Lin, D. Vikara, D. Morgan and D. Remson, 
"Comparative analysis of transport and storage options from a CO2 source 
perspective," International Journal of Greenhouse Gas Control, vol. 72, no. 1750-
5836, pp. 175-191, 2018.  
[5]  A. Sheriff, A. Guinan, T. Grant and L. Cunha, "Comparative Economic Analysis of 
Capture, Transport, and Storage from a CO2 Source Perspective in the Central 
U.S.," National Energy Technology Laboratory, Pittsburgh, Pennsylvania, 2023. 
[6]  B. Chen, D. Vikara, Z. Ma, D. Morgan, B. Ahmed, R. Vactor, L. Cunha, T. Grant, G. 
Guthrie, D. Livingston, M. Mehana, R. Pratt, J. van Wijk and R. Pawar, "CO2 
Transport Infrastructure Modeling in the Intermountain West Region, USA," in 16th 
Greenhouse Gas Control Technologies Conference, Lyon, France, 2022.  
[7]  T. Warner, D. Vikara, E. Basista and T. Grant, "Evaluating the Impacts of the 
Bipartisan Budget Act of 2018 45Q Tax Credit on CCS Network Costs," National 
Energy Technology Laboratory, Pittsburgh, Pennsylvania, 2022. 
[8]  D. Vikara, C. Yan Shih, A. Guinan, S. Lin, A. Wendt, T. Grant and P. Balash, 
"Assessing Key Drivers Impacting the Cost to Deploy Integrated CO2 Capture, 
Utilization, Transportation, and Storage (CCUS)," in 36th USAEE/IAEE North American 
Conference, Washington, D.C., 2018.  
[9]  T. Warner, D. Rampton, D. Morgan, G. Bromhal, W. Harbert and Z. Wang, "Using 
Geophysical Technologies Deployed in Inexpensive Monitoring Wells to Monitor 
the Evolution of a CO2 Plume: Potential Benefits and R&D Needs," National Energy 
Technology Laboratory, Pittsburgh, Pennsylvania, 2020. 
[10] D. Morgan, A. Sheriff, A. Guinan, T. Grant, T. Warner, D. Vikara and L. Cunha, 
"NETL’s Techno-Economic Modeling Resources for Analyzing Decarbonization 
Strategies Using CCUS," in 2023 FECM/NETL Carbon Management R&D Project 
Review Meeting, Pittsburgh, Pennsylvania, 2023.

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -40-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
[11] National Energy Technology Laboratory, "FECM/NETL CO2 Transport Cost Model 
(2023): Description and User's Manual," U.S. Department of Energy, DOE/NETL-
2023/4385, Pittsburgh, Pennsylvania, 2023. 
[12] N. Parker, "Using Natural Gas Transmission Pipeline Costs to Estimate Hydrogen 
Pipeline Costs," Institute of Transportation Studies, University of California at Davis, 
UCD-ITS-RR-04-35, Davis, California, 2004. 
[13] S. McCoy and E. Rubin, "An engineering-economic model of pipeline transport of 
CO2 with application to carbon capture and storage," International Journal of 
Greenhouse Gas Control, vol. 2, no. 2, pp. 219-229, 2008.  
[14] Z. Rui, P. Metz, D. Reynolds, G. Chen and X. Zhou, "Regression models estimate 
pipeline construction costs," Oil & Gas Journal, vol. 109, no. 14, pp. 120-127, 2011.  
[15] D. Brown, K. Reddi and A. Elgowainy, "The Development of Natural Gas and 
Hydrogen Pipeline Capital Cost Estimating Equations," International Journal of 
Hydrogen Energy, vol. 47, pp. 33813-33826, 2022.  
[16] ICF International, "Developing a Pipeline Infrastructure for CO2 Capture and 
Storage: Issues and Challenges," INGAA Foundation, 2009. 
[17] National Energy Technology Laboratory, "Quality Guidelines for Energy System 
Studies: Estimating Carbon Dioxide Transport and Storage Costs in NETL Studies," 
U.S. Department of Energy, DOE/NETL-2010/1447, Pittsburgh, Pennsylvania, 2010. 
[18] D. McCollum and J. Ogden, "Techno-Economic Models for Carbon Dioxide 
Compression, Transport, and Storage and Correlations for Estimating Carbon 
Dioxide Density and Viscosity," Institute of Transportation Studies, University of 
California at Davis, UCD-ITS-RR-06-14, California, 2006. 
[19] U.S. Energy Information Administration (EIA), "Electric Power Monthly with Data 
from September 2018-Table 5.3. Average Price of Electricity to Ultimate Customers: 
Total by End-Use Sector, 2008 – September 2018 (Cents per Kilowatt-hour)," U.S. EIA, 
November 2018. [Online]. Available: 
https://www.eia.gov/electricity/monthly/archive/november2018.pdf. [Accessed 
26 June 2019]. 
[20] National Energy Technology Laboratory, "Quality Guidelines for Energy System 
Studies: Cost Estimation Methodology for NETL Assessments of Power Plant 
Performance," U.S. Department of Energy, DOE/NETL-2011/1455, Pittsburgh, 
Pennsylvania, 2011. 
[21] U.S. Bureau of Economic Analysis, "Real Gross Domestic Product [GDPC1]," FRED, 
Federal Reserve Bank of St Lewis, [Online]. Available: 
https://fred.stlouisfed.org/series/GDPC1/. [Accessed 1 March 2023]. 
[22] Investopedia, reviewed by Julia Kagan, "Effective Tax Rate," 12 March 2019. 
[Online]. Available: https://www.investopedia.com/terms/e/effectivetaxrate.asp. 
[Accessed 12 June 2019].

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -41-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
[23] Whitman, Requardt, and Associates, LLP, "The Handy-Whitman Index of Public 
Utility Construction Costs, 1912 to January 1, 2023 - Cost Trends of Gas Utility 
Construction," Whitman, Requardt and Associates, LLP, Baltimore, Maryland, 2023. 
[24] U.S. Environmental Protection Agency (EPA), Underground Injection Control 
Program: Criteria and Standards Applicable to Class VI Wells; 40 CFR 146.81-146.95, 
Washington, D.C.: U.S. EPA, 2017.  
[25] U.S. Environmental Protection Agency (EPA), Greenhouse Gas Reporting Program 
Subpart RR Geologic Sequestration of Carbon Dioxide - 40 CFR 98.440, 
Washington, D.C.: U.S. EPA, 2017.  
[26] U.S. Environmental Protection Agency, "Cost Analysis for the Final GS Rule 
Appendix A-C PDF," EPA 816-R-10-013, Washington, D.C., 2010. 
[27] National Energy Technology Laboratory, "FECM/NETL CO2 Saline Storage Cost 
Model (2017)," U.S. Department of Energy, 2017. [Online]. Available: 
https://netl.doe.gov/energy-analysis/details?id=a0076ebe-d297-4718-8554-
1598526cbe3f. [Accessed 15 March 2024]. 
[28] Society of Petroleum Engineers (SPE), "CO2 Storage Resources Management 
System," SPE, 2017. [Online]. Available: https://www.spe.org/en/industry/co2-
storage-resources-management-system/. [Accessed 7 March 2024]. 
[29] N. Wijaya, D. Vikara, D. Morgan, T. Grant and D. Remson, "Basin Management of 
Geologic CO2 Storage: Effect of Well Spacing on CO2 Plume and Pressure 
Interference," in Society of Petroleum Engineers (SPE) Western Regional Meeting 
(WRM), Bakersfield, California, 2022.  
[30] G. Teletzke, J. Palmer, E. Drueppel, M. B. Sullivan, K. Hood, G. Dasari and G. 
Shipman, "Evaluation of Practicable Subsurface CO2 Storage Capacity and 
Potential CO2 Transportation Networks, Onshore North America," in 14th 
Greenhouse Gas Control Technologies Conference Melbourne 21-26 October 
2018 (GHGT-14), Melbourne, Australia, 2020.  
[31] M. Valluri, S. Mishra and P. Ganesh, "Injectivity index: a powerful tool for 
characterizing CO2 storage reservoirs - a technical note," Greenhouse Gases 
Science and Technology, vol. 11, pp. 256-265, 2021.  
[32] A. Goodman, A. Hakala, G. Bromhal, D. Deel, T. Rodosta, S. Frailey, M. Small, D. 
Allen, V. Romanov, J. Fazio, N. Huerta, D. McIntyre, B. Kutchko and G. Guthrie, "U.S. 
DOE methodology for the development of geologic storage potential for carbon 
dioxide at the national and regional scale," International Journal of Greenhouse 
Gas Control, vol. 5, no. 4, pp. 952-965, 2011.  
[33] International Energy Agency Greenhouse Gas R&D Programme, "Development of 
Storage Coefficients for Carbon Dioxide Storage in Deep Saline Formations," 
2009/13, 2009. 
[34] National Energy Technology Laboratory, "FECM/NETL CO2 Transport Cost Model 
(2023)," U.S. Department of Energy, 2023. [Online]. Available:

National Energy Technology Laboratory Strategic Systems Analysis & Engineering -42-  
QUALITY GUIDELINES FOR ENERGY SYSTEM STUDIES:  
Carbon Dioxide Transport and Storage Costs in NETL Studies July 2024 
https://netl.doe.gov/energy-analysis/details?id=d3086f60-278d-4e97-a649-
8e4d5ce5e93c. [Accessed 15 March 2024]. 
[35] National Energy Technology Laboratory, "FECM/NETL CO2 Saline Storage Cost 
Model: Model Description and Baseline Results," U.S. Department of Energy, 2017. 
[Online]. Available: https://netl.doe.gov/energy-analysis/details?id=5a5cf87b-
9dd2-4d5c-b1cc-9c4645edc46d. [Accessed 15 March 2024].

www.netl.doe.gov 
Albany, OR • Anchorage, AK • Morgantown, WV • Pittsburgh, PA • Sugar Land, TX 
(800) 553-7681 
QUALITY GUIDELINES 
FOR ENERGY SYSTEM STUDIES
