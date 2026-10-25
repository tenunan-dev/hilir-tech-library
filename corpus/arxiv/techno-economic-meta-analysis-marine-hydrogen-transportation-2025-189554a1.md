---
source_id: "arxiv"
title: "Techno-economic meta-analysis of marine hydrogen transportation (arXiv, 2025)"
url: "https://arxiv.org/pdf/2508.10923v1"
retrieved_at: "2026-10-25T15:48:47+00:00"
licence: "CC0-1.0 metadata; per-paper full text"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "189554a10276eadc6cf6d813223c84ea91f5f51d462d7dacf82e974173fd717e"
collected: "manual"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
summary: "Open-access meta-analysis of techno-economic studies of marine hydrogen chains (compressed gas, liquid hydrogen, LOHC, ammonia): ammonia is the lowest-cost option in the standard case, LOHC dehydrogenation consumes 30-40% of the hydrogen LHV, and no large-scale ammonia cracking facilities are operational."
---

# techno economic meta analysis marine hydrogen transportation 2025

1 
 
Interactive framework for techno-economic meta-analysis of marine hydrogen 
transportation  
Lucas Hanssens 1, Maarten Houlleberghs 1, Karel Van Acker ,2,3,4 , Johan A. Martens 1,5 and Eric 
Breynaert1,5,* 
Abstract 
As a result of the wide span of uncertainties and input variables considered in recent peer-reviewed 
studies on hydrogen supply chains, consensus and generalized insight are hard to  derive. This work 
presents a meta-analysis model, building upon a growing database of literature cost estimations and 
enabling dynamic investigation and comparison of hydrogen transportation chains under varying input 
scenarios. Also built into the framework is the evaluation of the impact of costing methodology and 
shipping fuel type. A convenient online interface allows to leverage increasing amounts of underlying 
cost data and assists users in gaining insight into generalized cost dynamics attributes . The method 
and toolbox are demonstrated via in-depth analysis  of compressed hydrogen (GH 2), liquefied 
hydrogen (LH 2), dibenzyltoluene (LOHC)  and ammonia as hydrogen carriers . Confined hydrogen 
clathrate hydrates are used as an example to demonstrate how one can deal with lower-TRL candidate 
technologies.  
Key words: Techno-economic, meta-analysis, hydrogen supply chains, interactive, hydrogen transport  
1 Introduction 
Avoiding drastic climate change , induced by excessive emission of greenhouse gases , requires a 
dramatic turnaround. In the European Green Deal, the EU has pledged to guide its  economy and 
 
1 Center for Surface chemistry and Catalysis, KU Leuven, Celestijnenlaan 200F  – box 2461 , 3001 
Heverlee, Belgium 
2 Department of Materials Engineering, KU Leuven, Kasteelpark Arenberg 44, 3001, Leuven, Belgium 
3 Flanders Make, Corelab, VCCM, Belgium  
4  Center for Economics and Corporate Sustainability (CEDON), KU Leuven, Warmoesberg 26, BE-1000, 
Brussels, Belgium 
5  X-ray/NMR platform for Convergence Research (NMRCoRe), KU Leuven, Celestijnenlaan 200F – box 
2461, 3001 Heverlee, Belgium

2 
 
society into climate-neutrality by 2050  [1]. These ambitious plans demand swift adoption of 
renewable energy strategies, also in geographic regions with limited potential for domestic production 
of renewable energy [2,3]. Currently these regions rely on the import of fossil energy for industrial 
production and power supply , but multiple options for decarbonization of key industrial production 
processes exist. Import of green hydrogen could for example replace import of fossil fuels [4]. On the 
flip side, there is the possibility of re-localization of energy-intensive production processes to foreign 
regions with large renewable energy potential (an effect known as “renewables pull”) [5,6]. The extent 
to which (part of) the value chain will be relocalized, critically depends on a complex interplay of the 
perspectives of private investors, policy makers and society on a given product [7]. The transportation 
cost for renewable energy , such as green hydrogen , clearly is a critical factor  in this consideration. 
Several marine transportation technologies can be considered for rapid scale -up of green hydrogen 
imports, but the optimal choice will depend on specific use cases. This renders the techno-economic 
comparison between different scenarios far from  straightforward and calls for high -quality and 
nuanced techno-economic assessment of hydrogen transportation. 
In recent years, literature has seen a sharp surge in techno -economic studies on hydrogen supply 
chains. Especially for marine supply chains, the large capital expenditures (CapEx) and long lifetimes 
of the infrastructure require strong commitment to a certain technology. Table 1 shows an extensive 
overview of recent peer-reviewed studies investigating the potential of a wide range of  hydrogen 
storage technologies under different  marine supply chain assumptions.  To make case -specific 
recommendations, most studies focus on real -world case s. Investigating costs along well -defined 
trading routes holds potential to highly impact policymakers looking to establish such routes [8–11]. 
Comparing the case studies in Table 1, a very  large span of supply chain variables emerges. This not 
only has led to a diverse range of  case-specific technology optima (indicated in bold in Table 1) , the 
strongly differing supply chain assumptions render benchmarking across case studies extremely 
difficult [12]. Clearly, t here is no “silver bullet ” in hydrogen supply chain literature . Even studies 
considering similar routes and using similar technologies tend to draw contradictive conclusions, due 
to the large variability of input variables (e.g. Ammonia cracking CapEx estimations can vary up to an 
order of magnitude  for infrastructure of similar capacity ). This lack of consistency is  confusing and 
lowers the confidence of policymakers and energy system researchers towards the outcomes of such 
studies.  
A major barrier to consensus is the absence of standardized frameworks that allow for dynamic, 
comparative analysis across a wide range of input assumptions and costing methodologies. The 
studies in Table 1 mostly rely on different, case-specific models and often also apply different techno-
economic assessment strategies. In most cases, they are either based on equivalent annual cost (EAC)

3 
 
or on net present value (NPV) methods. None of these studies systematically address the influence of 
the method used on conclusions of the study. As will be shown in the present study , the choice of 
economic assessment strategy can in itself have a large impact on the conclusions indicated by the 
modelling. Also key assumptions such as discount rate, asset lifetime, and energy cost vary widely 
between studies. Often this is insufficiently disclosed.  
Broader, interactive, energy system modelling tools, such as HOMER, TIMES, OSeMOSYS or PLEXOS, 
offer system-level insights into hydrogen flows but lack the process -level resolution to differentiate 
between marine carrier technology configurations and these models include limited specific literature 
data [13–16]. They are also not easily  and freely accessible, or quickly adaptable for rapid sensitivity 
or scenario analysis focused only on the hydrogen supply chains. 
To address these limitations, the present work introduces a flexible and publicly accessible  meta-
analysis modelling framework that builds on a growing database of  specialized techno-economic 
literature. The tool enables transparent comparison of hydrogen transport technologies under varying 
input conditions, including transport distance, energy price, infrastructure assumptions, fuel type, and 
costing methodology. By allowing users to explore the impact of such variables interactively, the 
model facilitates both high-level scenario analysis and granular sensitivity exploration. In addition to 
established carriers such as GH₂, LH₂, ammonia, and LOHC, the framework supports the inclusion of 
low-TRL technologies, broadening its applicability to emerging options.  Finally, our dashboard is 
designed to be intuitive. This provides experienced as well as less experienced readers the opportunity 
of gaining insight into cost dynamics. It makes our dashboard truly unique in its ability to engage 
researchers and policymakers that would otherwise not be able to explore their scenarios of interest, 
as most interested research ers, and especially policymakers, do not have access to licensed energy 
system modelling tools.  To the best knowledge of the authors, no comparable  open-access meta-
analysis tools are available for a broad readership to get insight into the specific literature of techno-
economic cost determination of hydrogen supply chains.  
This work kicks off with an elucidation of the input categories causing a large part of the variability in 
cost outcomes. These input categories are  critical parameters included in the  tool input dashboard. 
After introducing the general structure of the model, the method and toolbox are demonstrated by 
providing an in -depth analysis of compressed hydrogen (GH 2), liquefied hydrogen (LH 2), 
dibenzyltoluene (LOHC)  and ammonia. The choice for these technologies was made due to their 
prevalence in the present literature. Pipelines are not considered in this demonstration of the 
framework because of their limited application potential for trans-oceanic transport, but can be added 
to the framework in future work, providing improved results for short to medium distance routes. To

4 
 
demonstrate how one can deal with lower-TRL candidate technologies, confined hydrogen clathrates 
were added to the analysis. The discussion of the results focuses on the identification of technology-
specific cost drivers and underlying trends in the cost dynamics of the different technologies. Finally, 
the capability of the model to research different scenarios is demonstrated with a selectio n of 
sensitivity and scenario analyses deemed interesting by the authors. 
The data and analysis framework used in the study are available in the interactive online application 
‘Hydrogen Supply Chain Dashboard ’, which can be accessed at 
‘https://script.google.com/macros/s/AKfycbwoSX4K5dUJmykwXWmtsKj_UKAF_z0pdDaBjuj9j4v-
LSE6zgas3RPNsTnhx-TCMLVHcg/exec’. If the app does not open, using a private window can solve the 
issue. Further inquiries can be d irected to the corresponding author.

1 
 
Table 1: Overview of techno -economic analyses of hydrogen supply chains published starting from 2017. For comparative assessments, cost -optimal 
technologies are indicated in bold. EAC: Equivalent Annual Costing, LCOT: Levelized Cost of Transport, LCCA: Life-Cycle Cost Analysis. 
 Technologies considered Fuel for transport Method Reference  
Chapman et al. (2017) LH2 Fossil EAC [8] 
Niermann et al. (2019) LOHC  Fossil EAC [17] 
Heuser et al. (2019) LH2 Fossil EAC [9] 
Ishimoto et al. (2020) LH2, Ammonia Renewable LCOTNPV [11] 
Niermann et al. (2021) GH2, LH2, LOHC, HVDC, Pipeline Fossil EAC [18] 
d’ Amore Domenech et al. (2021) GH2, LH2, HVDC, Pipeline Renewable LCCA [19] 
Gallardo et al. (2021) LH2, Ammonia Fossil Not clear [20] 
Raab et al. (2021) LH2, LOHC Renewable EAC [21] 
Brändle et al. (2021) LH2, Pipeline Renewable EAC [22] 
Roos (2021) LH2, LOHC, Ammonia Fossil EAC [23] 
Collis et al. (2022) GH2, LH2, LOHC, Ammonia, Pipeline Not clear Not clear [24] 
Lee et al. (2022) LH2, LOHC, Ammonia Fossil EAC [25] 
Borsboom-Hanson et al. (2022) GH2, LH2, Pipeline Fossil EAC [26] 
Johnston et al. (2022) LH2, LOHC, Ammonia, S-LNG Fossil & Renewable EAC [10] 
Dickson et al. (2022) LH2, LOHC, Ammonia, S-LNG Fossil DCF [27] 
Perey and Mulder (2022) LH2, Ammonia, Pipeline Fossil LCOTNPV [28] 
Cui et al. (2023) Ammonia, Methanol Not clear LCOTNPV [29] 
d’ Amore Domenech et al. (2023) GH2, LH2, Pipeline  Renewable LCCA [12] 
Neumann et al. (2023) LH2, Fe Fossil  EAC [30] 
Hampp et al. (2023) LH2, LOHC, Ammonia, S-LNG, FTF, CH4 
(g), Pipeline 
Renewable EAC [31] 
Villalba-Herreros et al. (2023) LH2, Ammonia Renewable EAC [32] 
Kim et al. (2024) LH2 Renewable EAC [33]

2 
 
Hydrogen supply chain input categories 
Techno-economic analyses  on hydrogen supply chains  typically define case stud ies using a set of 
parameters including the investor’s perspective, the modelling scope and supply chain scale and 
distance. While t hese inputs can vary widely between studies, they are uniquely defined for each 
specific case. The most common hydrogen supply chain input variables can however be categorized 
into three main groups: ‘Case Specification’, ‘Location’ and ‘Technology’ (Figure 1). Even though case-
related assumptions cannot always be aligned, the consistency in the underlying methodology should 
be increased.  
‘Case Specification’ - To improve comparability between studies, this work identifies two important 
factors: (1) the fuel -type choice and ( 2) the sensitivity of the results towards different techno -
economic costing methodologies. Modelling the impact of renewable fuels on supply chain costs for 
competing technologies offers an avenue to evaluate the resilience of the technology towards future 
fuel adaptations and increasingly stringent regulations governing supply chain emissions. As shown in 
Table 1, there  is a large variability in the  fuel type considered in current literature, but in most 
published cases the impact of fuel type on the analysis is barely discussed. Table 1 also highlights the 
diversity of cost assessment methods used in the consulted studies. As awareness on the impact of 
the different assessment methods is critical, this study provides an in-depth discussion on assessment 
methods, mathematically deriving specific conditions for equivalence of the most popular methods , 
while providing the opportunity to assess case-specific costing methodology impacts in the modelling 
dashboard.

3 
 
 
Figure 1:   Diagram summarizing three types of input variables in hydrogen supply chain techno -
economic studies. 
‘Location’ -  The location of infrastructure determines  localized parameters including energy cost, 
climate and labour cost. These parameters tend to be very volatile in nature and can cause  strong 
discrepancies in modelling outcomes [20].  
‘Technology’ -  Based on case specifications and location, specific choices are made for transportation 
and stationary infrastructure.  As large-scale hydrogen supply chains are still in a conceptual stage , 
there is a high degree of uncertainty on how capital and operational costs for these technologies will 
evolve over the coming decades. Previously published studies often rely on a single process simulation 
or reference datapoint for estimating the capital and operational expenditures (CapEx & OpEx)  of 
infrastructure that ha s yet to be developed at scale. To illustrate the heterogeneity in  technology-
related input data across different techno-economic studies on marine hydrogen supply chains, Figure 
2 shows the distribution of (de)conditioning energy use and CapEx data extracted from a selection of 
published studies [8,11,19,20,22,25,27,29,34–47]. The presented data was normalized to 1 GWe and 
adjusted for inflation with respect to reference year 2022 (according to equation 7). These datapoints 
diverge strongly as authors have  (1) varying degrees of confidence in the development of 
(de)conditioning infrastructure at GW-scale, (2) different supply chain boundary conditions (hydrogen 
temperature, pressure, purity, …), (3) different process modelling methodologies, including varying 
modelling scopes and detail.

4 
 
 
Figure 2: Boxplots illustrating the heterogeneity of input data on (a) (de)conditioning energy use ( in 
kWhe/kgH2) and (b) CapEx for supply chain unit operations  (normalized to 1 GW e and adjusted for 
inflation with respect to reference year 2022) , used in a selection of techno-economic studies on 
hydrogen supply chains [8,11,19,20,22,25,27,29,34–47]. Specific information on the datapoints used 
can be found in the Supplementary Information ( A1.3-A1.5). Scale-related discrepancies in the data 
were minimized by sourcing data from studies with modelling scales within a factor 5 of 1 GWe.  
2 Experimental procedures 
The components of the marine transportation chain for the different technologies are schematically 
shown in Figure 3. The model calculates the transportation cost of a set amount of hydrogen delivered 
in gaseous form at 50 bar. As this work focuses on the transportation of the hydrogen, only hydrogen 
produced for compensation of hydrogen losses along the transportation chain are included in the cost 
assessment, to represent the transportation efficiency of the included technologies. Hydrogen losses 
occur through boil-off (LH2) and also include hydrogen used for dehydrogenation heat (LOHC and NH3) 
and propulsion. The modelling in this work starts from gaseous H2 at low pressure. Then, through the 
application of the different conditioning technologies, the volumetric energy density of the hydrogen 
is increased to allow for efficient transportation. Conditioned hydrogen is stored in buffer reserves

5 
 
adapted to the time between the arrival of ships. An essential part of the transportation chain 
estimations concerns the scaling of ship fleets. The size of the fleet depends on the quantity  of 
hydrogen that needs to be delivered and the number of deliveries per day for each ship (typically less 
than one), which depends on the distance from production to delivery site, according to Eq. 1: 
#transport ships =  ⌈
daily production [kg H2]
capacity transport ship [kg H2]
#deliveries 
day ∙ ship
⌉ 
Eq.1 
Inherently, vehicle supply chains scale imperfec tly, as no fractional vehicles can be employed.  This 
attribute is represented by the ceiling operator in Eq.1.  Optimal scaling points are achieved when all 
vehicles leaving the production facility are loaded at maximal capacity. This is a situation in which the 
buffer storage capacity is also optimally sized.   
In the base case, used to demonstrate the model, the  capacity of the marine supply case is set at 1 
GWe, corresponding to ca. 426 tonnes hydrogen per day. The input hydrogen pressure of the marine 
supply chain is assumed to be 5 bar. The output pressure is set at 50 bar, since it is assumed that at 
the receiving port, these large volumes of hydrogen will be loaded into a pipeline network [48]. Large 
ports often serve chemical clusters with interconnected hydrogen pipelines [49]. Further details on 
the build-up of the supply chains for the different technologies can be found in the Supplementary 
Information (A1.2-1.6).  
 
Figure 3: Modelling scope and components of the marine transportation supply chain. 
 
2.1 Model structure 
The modelling process is represented as a flowchart in Figure 4. A technology modelling back-end 
model (running in Google Sheets supported by automatization and solver protocols) is published on 
the web via a front-end application dashboard (Figure 5), optimized to structure user interactions with

6 
 
the back-end. The supply chain configuration and techno -economic assumptions are defined in the 
application dashboard. After s ubmitting these inputs to the back -end technology modelling 
framework, all technologies are modelled separately following the same basic modelling outline 
(Figure 3). First, the model is initialized using data from the database and the application dashboard. 
This yields the supply chain infrastructure dimensioning. The toolbox offers two options for using the 
available data: all data can be averaged, thus representing a general cost trend, or alternatively, one 
can select and compare specific data. Subsequently, process energy flows are calculated based on 
reference input data and process modelling. Finally, the supply chain infrastructure and energy 
requirements are valorized in a discounted cashflow analysis. In the following sections, the outline of 
each of these modelling blocks is further discussed.

7 
 
 
Figure 4: Modular structure of the modelling framework. 
 
Figure 5: Rendering of the supply chain web-app dashboard. 
 
2.1.1 Initialization Module 
2.1.1.1 Inputs from database and applications dashboard 
The initialization module receives input, both from the back -end database and from the front -end 
application dashboard. The back-end database delivers input on the hydrogen transportation 
technologies considered  and default costs associated with these technologies . These inputs are 
combined with the inputs provided by the application dashboard, including the supply chain 
configuration, the macro economic setting, as well as modifications to the default inputs retrieved

8 
 
from the back-end database. In what follows, the default database configurations and their associated 
costs are outlined.  
2.1.1.2 Hydrogen transportation technologies 
Table 1 shows an overview of the technologies collected from literature. The database contains 
information on well -established technologies including compressed hydrogen, liquefied hydrogen, 
LOHC (Dibenzyl toluene), and ammonia, as well as on one emerging technology: confined hydrogen 
clathrate hydrates. The option to define low Technology Readiness Level (TRL) technologies such as 
HCH and compare their performance to established technologies can yield valuable insights and is an 
asset of the presented methodology. 
An important disadvantage of H 2 as molecular energy carrier is its low volumetric energy density at 
atmospheric pressure. To compensate this, it is mostly stored and transported at high pressure or in 
liquefied state. Both technologies are mature at small scale and have been widely implemented across 
a broad range of applications. Technically, compressed hydrogen storage (GH2) is the least complex H2 
storage technology. Five types of storage vessels are available: Type I to V. Type I vessels are typically 
employed for stationary storage at pressures of up to 500 bar. They are mostly constructed in 
austenitic stainless steel alloys (e.g. AISI 304 and AISI 316). While these alloys are best fit to withstand 
hydrogen effects at ambient temperatures [50,51], their high specific density yields heavy vessels with 
limited application potential in transport. Lightweight vessels can be constructed using composite 
materials and are more expensive, but they are more suitable for transport of H 2. For Type II vessels, 
the load is distributed between the metal tank and a fiber wrap. Type III and type IV vessels consist of 
a thin liner, respectively in metal or high -density polyethylene, wrapped in a carbon fiber reinforced 
resin based shell, which carries the load [52,53]. Type V vessels consist entirely of composite material. 
Many disadvantages have been reported regarding the use of compressed or liquefied hydrogen as 
energy vectors in future sustainable energy distribution scenarios [18,19,36,54]. Major drawbacks for 
compressed H2 gas are the high energy penalty for compression, the need for heavy and/or expensive 
pressure vessels, and the specific safety precautions and regulations that need to be taken into 
account. Compared to gaseous H2 storage, the gravimetric energy density of liquified H2 is higher. Its 
extremely low boiling point (20 K) however limits t he options for storage and transport to costly 
vacuum-insulated vessels. Storage and transportation of liquefied H 2 also comes with a low en ergy 
efficiency as result of its extremely low temperature. Today, hydrogen liquefaction typically consumes 
between 30 and 40% of the chemical energy present in the liquid (on a lower heating value basis) . 
Boil-off during transport leads to loss of H2 in gaseous form [18], further decreasing the efficiency. In 
an attempt to improve the economics of H 2 storage and transport, alternative technologies for H 2

9 
 
storage and transportation are in high demand. Several are being developed and investigated, each 
with their own strengths and challenges. 
One of the alternative technologies makes use of liquid organic hydrogen carriers (LOHC) [2,18,54,55]. 
LOHCs are hydrocarbon molecules (often aromatic) , occuring as liquids at ambient pressure and 
temperature, which can catalytically be hydrogenated to store chemically bonded hydrogen. H 2 is 
recovered by catalytic dehydrogenation of the organic molecules. After returning the dehydrogenated 
carrier molecules to the hydrogenation site, the cycle is closed. Methanol, benzyltoluene and 
dibenzyltoluene (DBT), N-ethylcarbazole and 1,2 -dihydro-1,2-azaborineare are typical LOHC 
candidates [17,55]. As these compounds exhibit physicochemical characteristics similar to diesel fuel, 
they can be transported using the existing and well -established infrastructure for distribution of oil 
derivatives. In this application, the heavier, aromatic molecules are typically preferred because of their 
low vapor pressure. This minimizes evaporative losses and facilitates purification of the released H2 to 
fuel cell grade [56,57]. 
Another attractive hydrogen carrier is ammonia [41,58]. The gravimetric and volumetric capacity of 
hydrogen stored in liquid ammonia surpasses th at of liquid hydrogen [41,59]. Ammonia not only is 
already being produced on an industrial scale using an electrified Haber -Bosch process [58], it is 
transported around the globe in large volumes for fertilizer production and chemical applications [60]. 
This implies large parts of the supply chain  are already available. While t hese advantages make 
ammonia an attractive candidate for established marine transport businesses to engage in hydrogen 
transportation [61,62], ammonia technology also comes with severe downsides. Ammonia not only is 
extremely toxic and environmentally unfriendly, releasing its H2 content requires an energy-intensive 
cracking step. Ammonia cracking can be done using fire -heated cracking furnaces, much like steam 
methane reforming, but more effective (catalytic) cracking methods are actively being researched 
[45]. To the best of our knowledge, there are currently no large scale ammonia cracking facilities 
operational. Significant costs for purification are anticipated since H 2 applications typically have very 
low tolerance for ammonia contamination of the hydrogen feed [63]. Uncontrolled release and 
subsequent precipitation of atmospheric ammonia in natural reserves and large water bodies is 
problematic. Its toxicity further limits its application potential, especially when transport on public 
roads in densely populated areas is required [41,64,65]. This implies strict safety measures will have 
to be put in place to unlock the potential of ammonia as a widespread energy carrier. 
Finally, H2 ad- or absorbing materials such as activated carbon, metal organic frameworks and metal 
hydrides could play a role in future hydrogen supply chains [35]. Hydrogen storage in clathrate 
hydrates is another appealing option [66,67]. Clathrate hydrates are solid ordered water structures

10 
 
encapsulating guest molecules in molecular cages, at high storage densities. Methane filled clathrate 
hydrates are abundant in nature, occur in deep -sea sediments and permafrost [68,69], and are 
investigated as a potential alternative to LNG in marine natural gas supply chains [70–74]. Hydrogen 
clathrates do not occur in nature, but can be made synthetically [66,67,75,76]. The hydrogen storage 
capacity of  hydrogen clathrate hydrates  (HCH) depends on its crystallographic structure. Storage 
capacities of 3.2 wt% and 5.2 wt%, have been reported for structure I (sI) and structure II (sII) H 2 
hydrates, and  theoretically, clathrate structures could store up to 10 wt% H2 [76]. Using confined HCH, 
this technology could even be operated similar to an adsorption process. To the best of our 
knowledge, HCH technology has not yet been considered in the existing techno -economic literature, 
rendering it a valuable addition. Progress is being made in the understanding of the molecular aspects 
of synthetic clathrate formation [69]. Crystallization of bulk clathrate hydrates is particularly 
challenging and requires extreme pressures of several thousand bar or deep cooling. The use of 
tetrahydrofuran (THF) as clathrate crystallization promotor has resulted in a dramatic decrease in 
pressure and temperature requirements for the formation of sII hydrogen clathrate. Lee et al.  
achieved 4 wt% hydrogen storage density in sII clathrate hydrates stabilized using 0.2 mol% THF at 
120 bar and 270 K [77]. Similar to  THF, organic crystallization aids and hydrophobic surfaces can 
alleviate pressure and temperature requirements and improve both kinetics and thermodynamics of 
clathrate formation [78–84]. For the HCH supply chains used in this work, we used the results and 
conditions reported by Lee et al. and assumed that the promoting effect of THF can be matched by 
hydrophobic materials. 
2.1.1.3 Cost data 
2.1.1.3.1 CapEx 
Supply chain costs are broken down into CapEx and OpEx. In the available literature, typically, CapEx 
data is obtained either from process simulations or reference data. Chemical processes, however, can 
be very complex and cost outcomes are heavily dependent on process configuration and assumptions. 
As illustrated in the introduction, cost estimates in literature for emerging technologies , involved in 
large-scale hydrogen supply chains , can vary substantially. Relying on a single process simulation 
outcome for the complex chemical processes involved in hydrogen supply chains thus introduces a 
high degree of uncertainty into the cost outcomes. Therefore, to increase the robustness of our 
analysis, we incorporated an average of at least 3 reference data sources in our model as a more 
nuanced proxy for capital intensive infrastructure investments. In order to improve data compatibility, 
reference data was only selected when the reference modelling  scale was within a factor 5 of the 
standard modelling scale of 1 GW used in this work. A detailed description of included CapEx data can

11 
 
be found in A1.2-1.7. Indirect capital costs are assumed to be incorporated in the reference cost data, 
although we were unable to verify this for some datapoints due to their limited documentation. 
To date, no marine hydrogen supply chains have been established at scale. As a result, conceptual 
hydrogen carriers were compiled for the different hydrogen transportation technologies. Ship design 
details are summarized in Table 2 and are more elaborately available in section A1.7. The conceptual 
GH2 and HCH ship design is shown in Figure 6 and is based on available compressed natural gas carrier 
designs by Global Energy Ventures © [85]. Given the larger amount of available reference data, LH 2, 
LOHC and ammonia carrier designs were based on reference data. For each carrier, cost estimations 
are included for adaptations towards a renewably powered drivetrain.  
 
Figure 6: Conceptual HCH and GH2 ship design. The standard design for both ships involves a hall with 
stacks of interconnected pressure vessels (for the HCH ship the hull is insulated).

12 
 
Table 2: Marine hydrogen ship cost data and assumptions. Carrier molecule costs are included in LOHC 
ship cost estimations. Further detail is provided in section A1.7. 
  GH2 LH2 LOHC Ammonia HCH 
Capacity ship (ton H2)  300.54 9828.31 2400.00 7040.00 1283.00 
Cost ship (M€) 251 / 187 65 197 
Cost renewable ship (M€) * 271 397 207 80 210 
Lifetime ship (years) 20 
(Un)loading time (h) 36 48 48 48 60 
*: Including hydrogen storage agent (DBT for LOHC and porous material for HCH) 
2.1.1.3.2 OpEx 
Averaged reference data is used to estimate the energy requirements of the more chemically complex 
process chains (LH2, LOHC and ammonia), while GH2 and HCH chain energy use is modelled on a unit 
operation level using empirical relations for compressor energy use and Carnot efficiency calculations 
for cooling performance (A1.1.1 and A1.1.2). General OpEx assumptions of this study are detailed in 
Table 3. In the default setting, supply chains are assumed to be powered by fossil fuels. IFO 380 bunker 
fuel prices from the first quarter of 2021 were used. Marine hydrogen supply chains will be deployed 
to transport energy from regions with abundant renewable energy resources, to regions with a deficit 
in renewable energy. For the low-cost producer regions, we assumed an energy cost of 0.021 €/kWh, 
corresponding to the low-end figure of current LCOE estimates for onshore wind energy in the Lazard 
ltd. LCOE report [86]. The electricity cost for the consumer region is based on the average European 
non-household electricity price reported by Eurostat [87]. 2021 averages were incorporated to avoid 
using the disproportionately inflated 2022 energy prices. 
Table 3: Overview of the specific operational expense assumptions. 
Labor costs [88] 19.8 €/h 
Electrolysis efficiency 52.59 kWh/kgH2 
Maintenance costs [45] 5.0 % of capital investment 
Insurance costs [45] 2.0 % of capital investment 
Electricity cost producer region [86,87] 0.021 €/kWh 
Electricity cost consumer region [87]  0.130 €/kWh 
Fossil fuel cost [89,90] 309.73 €/tonne 
Fuel consumption [91] 90 tonne/day 
Working hours per day 12 
Size crew [88] 22 
Speed [91] 35 km/h 
2.1.2 Financial balance 
To make a direct comparison, the complex cost structure of each technology must be distilled into one 
appropriate performance indicator. Deriving a single cost figure from a supply chain, however, is an 
intricate task. Capital expenditures (CapEx) and oper ational expenditures (OpEx) occur scattered

13 
 
throughout the lifetime of the project. Consequently, the total cost figure is not merely a summation 
of costs, it must also consider concepts such as opportunity cost and time preference. In the case of 
hydrogen supply chains, the performance indicator of choice is often the levelized cost of hydrogen 
transport (LCOT), expressed in a certain currency, per mass or energy unit transported hydrogen. As 
in wholesale energy markets, prices are generally reported in €/MWh, since estimating the transport 
costs per MWh simplifies interpretation in the context of the energy market as a whole. 
2.1.2.1 Levelized cost of hydrogen transport (LCOT) 
Ideally, the LCOT can be compared directly to the levelized cost of energy (LCOE), which is a very 
impactful and widely implemented measure of energy cost [92,93]. Consequently, LCOT assessment 
methods are mostly analogous to the different LCOE assessment strategies present in literature. 
Currently, as Table 1 highlights, the predominant hydrogen -related LCOT approach is the equivalent 
annual cost strategy (EAC). E AC involves calculating the total yearly supply chain cost by summing 
annualized asset -specific CapEx contributions and yearly OpEx, akin to the LCOE as used by the 
National Renewable Energy Laboratory [92]. Some advantages of this method are its simple 
calculation, without the need for complicated data setup, the ability to compare costs for assets with 
different lifetimes and the ease of communicating a yearly cost figure [94]. The annuitization is done 
using a Capital Recovery Factor (CRF), for a specified depreciation period or over the complete useful 
lifetime. Importantly, using this method theoretically implies infinite project duration when the 
respective depreciation tim es of the considered appliances are different. In techno -economic 
assessments of a single asset, like LCOE calculation of renewable energy generators, the assessment 
period often coincides with the useful lifetime of the asset. However, the situation becom es more 
complicated in projects in which many assets are combined with different useful lifetimes. In that case 
the annualized CapEx of the different assets is combined in an overall system annuity (Equation 2 and 
3). The respective annualized cost figures  of the different assets represent a yearly cost considering 
their specified depreciation or lifetime. When the useful lifetimes of the assets in the system do not 
correspond, one cannot specify a certain project duration or assessment period without skewing the 
results. For infrastructure with a lifetime lower than that project duration, continuous replacement 
would be assumed, and the project duration would have to be a whole multiple of the asset’s lifetime. 
For long-lived infrastructure costs are spread over a period that is either longer than the assessment 
period (when their useful lifetime is used), or over a period that is significantly shorter than their useful 
lifetime (if their depreciation time is matched with the project duration).  This makes the EAC method 
in its standard form intrinsically awkward in dealing with strictly defined assessment periods and 
connected thereto, remaining (salvage) value of assets at the end of the project duration or 
assessment period. One should thus be careful appl ying the EAC method to multi -asset systems. To

14 
 
enable the inclusion of residual values of assets at the end of an assessment period, we included an 
adapted version of the EAC method (Eq . 4 and 5). In this version of the EAC meth od (referred to as 
EAC2), all CapEx contributions are annualized over the same assessment period. The CapEx figure to 
be annualized is determined based on how the asset’s depreciation time ( td) compares to the 
assessment period.  
              EAC [ €MWh] = OpExyearly + ∑ CapExii ∙ CRFiEyearly  Eq.2 
              CRFi = d(1 + d)ni
(1 + d)ni − 1 
Eq.3 
  
              EAC [ €MWh] = OpExyearly + CRFn ∙ ∑ CapExi ∙ ntd,iiEyearly  Eq.4 
              CRFn = d(1 + d)n
(1 + d)n − 1 
Eq.5 
with Eyearly the yearly energy transported, d the applied discount rate, ni the asset-specific depreciation 
time and n the assessment period. 
An alternative to the EAC approach is based on the net present value principle. This method is utilized 
by reputable commercial commentators such as Lazard © and Ernst and Young © [86,92]. While it 
involves a more complicated data setup, it offers more flexibility for the inclusion of inflation and 
complex cost assignment schemes. In contrast to the standard EAC method, this method, by default, 
requires the choice of a well -defined assessment period ( n), but can more conveniently integrate 
equipment replacements and residual values. All asset acquisitions and replacements are booked at 
the correct year during the project, leading to a more intuitive accounting scheme. However, 
transparency about the inclusion of residual value at the end of the project remains essential. Finally, 
the time resolution of cash flows may offer better insight into the investment timeline and time 
discounting can be done more intuitively. 
LCOTNPV [ €MWh] = ∑ CapExt + OpExt(1 + d)tnt=0∑ Et
(1 + d)t
n
t=0
 Eq.6 
Under certain specified conditions, the EAC (Eq.2) and LCOT NPV (Eq.6) method are equivalent [92]. In 
section A2.1, we provide mathematical proof of this claim in the context of a techno -economic 
assessment of systems comprising multiple assets with different depreciation times. Equation 2 and 5 
become mathematically equivalent when (1) the depreciation period for each asset in the EAC method 
is equal to the assessm ent period in the LCOT NPV method and no salvage value or decommissioning

15 
 
costs are considered, (2) yearly energy generation (or transport) remains constant over the 
assessment and (3) capital investments are done in year 0. Especially assumption (1) is unlikely to be 
met in assessments of hydrogen supply chains. Consequently, t o confidently compare results from 
different studies, in our opinion, attention must be paid to the sensitivity of the results towards the 
assessment method. To date, this concern has been overlooked in sensitivity analyses of hydrogen 
supply chain techno-economic assessments. 
2.1.2.2 Default methodology 
By default, the LCOT is calculated using the EAC method (Eq.2) in order to align our method with the 
majority of the available literature. Additionally, we included the option to use the adapted EAC (Eq.4 
and 5) and LCOT NPV approach, providing the user with the opportunity to experiment with and 
evaluate the effect of different costing methods on the estimated LCOT. Table 3  summarizes the 
general economic assumptions in this study. 2022 was chosen as the reference year of this study. The 
discount rate choic e has a large impact on the cost outcomes of renewable energy projects 
assessments [95,96]. In the context of techno -economic assessments of private investments, the 
discount rate is often interpreted as the minimal acceptable return for that investment, including the 
opportunity cost of invested capital and possible risk premiums [97]. However, in the context of a 
public investment by a government, one often applies the social discount rate (typically 3 -5%), 
representing a broader societally optimal rate at which cash flows should be discounted in projects 
with social relevance or that  are funded through public channels. The social discount rate is low in 
comparison to corporate discount rates in order to safeguard benefits in the near and more distant 
future and avoid preference towards projects with high initial gains and persistent l osses for future 
generations. The appropriate choice of discount rate thus depends on the perspective from which the 
assessment is made. In the default methodology of the assessment in this work, we assume a 
commercial perspective using region-specific weighted average cost of capital (WACC) as discount rate 
[98]. Large energy importing countries are often economically developed countries with a relatively 
low cost of capital. For energy exporters, generalization is not appropriate. Both highly developed 
economies like Australia or Oman, and emerging economies like Chile or Namibia, are determined to 
supply the worldwide hydrogen market [20,99–101]. As the intention of this work is to provide a more 
generalized insight into hydrogen supply chain costs, without considering specified routes, we chose 
a default general discount rate of 8% and provide the opportunity to alter this value in the application 
dashboard. Finally, it is not the intention of this work to evaluate business models. In corporate 
accounting, depreciation is used to allocate the costs incurred for an asset over its useful lifetime. 
Typically, accelerated depreciation schemes like th e Modified Accelerated Cost Recovery System 
(MACRS) are used to write off a larger portion of the costs in the first years after the acquisition of the

16 
 
asset in order to lower the tax burden during the first years of operation [102]. The scope of this study 
does not include corporate income evaluation. Instead, the study aims to provide robust insight into 
the underlying cost dynamics  with respect to  hydrogen supply chain  input variables. Therefore, we 
use the depreciation concept to reflect the economic reality of the asset (taking into account time 
preference), rather than as a tool for tax optimization or accounting. To this purpose, we have included 
the possibility to apply a linear depreciation scheme running for the assets’ estimated useful lifes (for 
the adapted EAC and LCOT NPV method, the standard EAC method depreciates assets over the whole 
useful lifetime). The choice for a linear depreciation scheme is motivated by the assumption that the 
supply chains provide a constant transportation volume or linear value accumulation throughout the 
project lifetime and that the infrastructure can be used beyond the span of the assessment period if 
its lifetime allows it. When the assets lifetime is shorter than the project duration, replacement of the 
asset is incorporated. Based on the asset depreciations, residual values are booked as negative costs 
(revenues).  
Table 4: General economic and accounting assumptions. 
Reference year 2022 
Discount rate 8% 
Project duration 20 years 
Depreciation linear 
Each process capital investment (CI0) from reference data is adapted to the reference year and supply 
chain scale according to Eq.7. The relative scale of the reference supply chain (Sc0), with respect to the 
scale of our model (Sc 1) is taken into account considering a scaling factor (SF). Finally, the cost 
estimation is adapted to include inflation effects through the Chemical Engineering Plant Cost Index 
(CEPCI) [103]. Because of geopolitical tension and (post)pandemic supply chain woes, the reference 
year 2022 was characterized by particularly high inflation. This translated in a dramatic spike in the 
CEPCI, a factor that needs to be taken into account when evaluating the CapEx cost contributors. 
𝐶𝐼 = 𝐶𝐼0 (𝑆𝑐1𝑆𝑐0)𝑆𝐹 (𝐶𝐸𝑃𝐶𝐼2022𝐶𝐸𝑃𝐶𝐼0 ) Eq.7 
The OpEx cost contribution is calculated as the sum of the energy requirements for the 
(de)conditioning steps, the energy consumption of storage after conditioning (for instance during 
transport), and general OpEx contributions like fuel consumption and labour costs. A general overview 
of the cost contributions and process steps that are incorporated into the model is provided in Table 
5.

17 
 
Table 5: General overview of the costs contributions incorporated in the different transportation supply chains.  1 
Marine 
transport   GH2 LH2 LOHC Ammonia HCH 
Production 
facility Conditioning Compression Compression  Compression Haber-Bosch process Compression 
    - Cooling  Hydrogenation - Cooling 
    - Liquefaction - - - 
  OpEx Maintenance  Maintenance  Maintenance  Maintenance  Maintenance  
    Insurance  Insurance  Insurance  Insurance  Insurance  
  CapEx Buffer tanks Buffer tanks Buffer tanks Buffer tanks Buffer tanks 
    
Compression 
installation 
Liquefaction 
installation Hydrogenation plant Haber-Bosch plant Compression installation 
    - Cooling installation - - Cooling installation 
    - Hydrogen pumps - - - 
  Losses - Boil-off Deconditioning heat Deconditioning heat - 
Transport OpEx Fuel Fuel Fuel Fuel Fuel 
    Labor Labor Labor Labor Labor 
    Maintenance  Maintenance  Maintenance  Maintenance  Maintenance 
    Insurance  Insurance  Insurance  Insurance  Insurance  
  CapEx GH2 ship LH2 ship  Tanker ship  Ammonia ship HCH ship  
    Pressure tanks - - - Clathrate tanks 
  Transport agent - - LOHC - Hydrophobic material 
Consumer  Deconditioning - - Dehydrogenation Ammonia cracking - 
  OpEx Maintenance  Maintenance  Maintenance  Maintenance  Maintenance  
    Insurance  Insurance  Insurance  Insurance  Insurance  
  CapEx Buffer tanks Buffer tanks Buffer tanks Buffer tanks Buffer tanks 
    - Regasification plant Dehydrogenation plant Cracking facility Compression installation 
2

18 
 
2.1.3 Energy consumption (de)conditioning 
The specific energy requirement of the different (de)condition processes  included in this base case 
model demonstration is shown in Figure 7. The energy requirements are reported on the electricity 
level, after factoring in electrolysis at 52.59 kWh e/kgH2 efficiency. The graph shows that LOHC 
technology requires the most energy to perform (de)conditioning of the transported hydrogen. LOHC 
dehydrogenation is the main contributor for energy use in the LOHC chain, amounting to ca. 16 
kWhe/kg when hydrogen burning is considered. It is often assumed in the literature that the 
dehydrogenation energy demand can significantly be lowered when large amounts of waste heat are 
available at the dehydrogenation plant [18,54]. However, given the considered process temperature 
of 573 K it is unlikely that large amounts of waste heat can drive the endothermic reaction. 
Consequently, reference data including dehydrogenation powered completely by waste heat was not 
considered. Details on the reference data used for the LOHC chain energy requirements can be found 
in Table A.4. Ammonia (de)conditioning energy use estimates are still a subject of active debate in the 
literature. Especially energy use estimates for the cracking step va ry substantially.  Based on 7 
independent literature sources (Table A.5), the energy need for ammonia cracking is estimated to be 
10.07 kWhe/kg. This value includes pressure swing adsorption purification and subsequent 
compression to 50 bar. For the LH 2 storage process, combining 10 reference sources (Table A.3), an 
energy use of 8.34 kWhe/kg is incorporated. This leaves room for improvement, as current liquefaction 
plants achieve energy efficiencies between 10 -13 kWhe/kg [36,38]. The GH 2 process, requiring only 
compression and compressor cooling, is energetically much more favorable. Finally, the conceptual 
HCH technology also has a particularly low energy requirement for the (de)conditioning.

19 
 
 
Figure 7: Specific energy consumption of the different hydrogen (de)conditioning technologies in the 
marine case. 
 
3 Results & discussion 
3.1 Supply chain costs 
Figure 8 shows the LCOT of fossil-powered marine supply chains transporting hydrogen over 10 000 
km at a 1 GWe capacity. At long overseas distances, the energy density of the carriers is the dominant 
cost determining parameter. As a result of low gravimetric energy density, GH2 ship transport capacity 
is low and a large fleet is built in order to reach the supply chain’s transportation capacity. Next to the 
large scale of the fleet, the unit cost of GH 2 ships is high owing largely to steel costs associated with 
the high-pressure vessels (see Table A.1). LH2 supply chain costs are dominated by CapEx for 
liquefaction infrastructure and buffer storage. The need for buffer storage is inversely correlated with 
the capacity of the transportation ships, as increasing transport capacity lowers the docking frequency 
of ships and thus increases the need for storage capacity storing production ad interim. While only a 
low number of ships is required, the high unit cost of LH 2 carriers results in considerable ship CapEx 
cost. Given the low energy pices assumed in the producer ’s region, extra hydrogen production to 
account for boil-off losses does not lead to a high cost contribution. Ammonia has the lowest LCOT for 
the standard case in Figure 8. By far the largest cost contribution originates from Haber -Bosch and 
cracking infrastructure, followed by (de)conditioning energy use.  Its high energy density  (17.6 wt%) 
results in a low number of required ships and associated fleet costs. LOHC technology needs a larger

20 
 
transportation fleet as the energy density is lower (6.2 wt%). However, the unit cost for LOHC ships is 
also lower due to the favorable diesel -like characteristics of the dibenzyltoluene ( DBT) carrier 
molecule and the scaled -up availability of suitable transportation ships.  The cost difference with 
ammonia is largely caused by the cost for the storage agent, i.e., DBT. Analogous to the GH2 case, HCH 
technology is more costly because of its large transportation fleet . The operation of the  large fleet 
results in elevated fuel and labor costs.  
 
Figure 8: Cost breakdown of marine supply chains for a transportation distance of 10 000 km. 
3.2 Scenario and sensitivity analyses 
Hydrogen supply chains are complex systems dependent on multiple unit operations affecting the 
total transportation cost. In the previous section, we discussed the results for the default settings of 
the model. While Figure 8 revealed clear cost drivers for each technology, the presented cost 
breakdown is not generally applicable.  This work aims to provide generalized insight into the cost 
dynamics of hydrogen supply chains. Generalized insight into cost dynamics can be achieved by 
identifying key cost driv ers for each technology through rigorous scenario and sensitivity analyses.  
Exploring relevant supply chain scenarios, we found that the LCOT, and the respective cost drivers per 
technology behind the LCOT, are strongly affected by a wide space of supply chain input variables. In 
earlier studies, transportation distance, supply chain scale, storage agent costs and CapEx assumptions 
were frequently identified as sensitive parameters [10,12,18,27]. However, the number of 
investigated parameters and their input range variation is often very limited. Additionally, the impact 
of parameters like fuel choice and assessment method have thus far been overlooked.

21 
 
Depending on the research field, definitions and procedures for uncertainty, sensitivity and scenario 
analysis may conflict. Following standard sensitivity analysis practice, many of the consulted  studies 
on hydrogen supply chains have performed sensitivity analysis by varying input parameters by 20% or 
less in both directions [10,17,18,20,34]. Given the degree of uncertainty in input parameters like CapEx 
data (Figure 1), we believe sensitivity analysis over a wider range of reasonable input data would more 
intuitively convey the impact that can be established from the wide span of reasonable input 
parameters. Additionally, current studies on hydrogen supply chains mostly perform single parameter 
sensitivity analyses and do not appreciate interaction effects. Next to multiparameter sensitivity 
analysis, we believe extensive scenario analysis is needed to assess possible supply chain scenarios.  
Without the constraints of a  highly specific use case, the large amount of possible supply chain 
iterations for the 5 different technologies prohibits a satisfactory sensitivity analysis in the context of 
this text . To enable exploration of the mult iparameter sensitivity of conceptual future hydrogen 
supply chains, the reader is provided with a user-friendly model interface allowing for detailed ‘DIY’ 
scenario analyses, building upon  the modelling framework developed with the literature data 
referenced in this work. By means of example, the following sections provide in -depth analysis of a 
selection of parameters, deemed interesting by the authors. Figure 9 provides a qualitative overview 
of technology sensitivities found for a range of key input parameters. All these parameters can be 
manipulated in the interactive tool. 
 
Figure 9: Heat map summarizing qualitative sensitivities of the supply chain costs of the different 
technologies towards prominent parameters relevant in case and local conditions setting. 
3.2.1 Supply chain distance and scale 
An increase in supply chain transportation distance, is typically associated with a rise in delivery time 
and lesser availability of transportation vehicles. Consequently, more vehicles must be deployed, thus 
causing a surge in LCOT. The need for fleet scaling is directly proportional to the energy density of the 
transportation technology, while the capital intensity of fleet expansion differs substantially between

22 
 
different technologies. Presently, hundreds of hydrogen supply chain routes are considered in the 
context of a worldwide hydrogen economy, ranging from a few hundred km to 25 000 km. 
Consequently, distance is typically considered  as one of the most sensitive modelling parameters in 
hydrogen supply chain assessments. Also supply chain scale initiates fleet scaling, in a similar manner 
as supply chain distance. Contrary to distance,  however, supply chain scale also directly affects 
stationary infrastructure costs. 
The cost dependency of the marine supply chains on distance and supply chain scale is shown in Figure 
10. In marine transport, the cargo capacity of a ship is indicated by weight or dead weight tonnage 
(DWT), since strict regulations are in place concerning the depth at which a cargo ship is allowed to sit 
in the water. Hence, transport using technologies having low gravimetric energy density (container 
included) can be limited by weight regulations, which will resul t in the need for quick scaling of the 
fleet. This effect can be witnessed in the graphs presented in Figure 8. GH2 and HCH graphs contain 
many steps, with each step expressing the need for expansion of the fleet by one ship. Because the 
clathrate ships need considerably less steel for the pressure vessels, the cost per ship is lower for the 
HCH transportation chains. Additionally, because the pressure vessels are more lightweight, the 
clathrate ships can carry more pressure tanks. In order to facilitate discussion of the trends in Figure 
10a, three distance ranges are identified: short distance (1 000-9 000 km), interm ediate distance (9 
000-17 000 km) and long distance (17 000 km -25 000 km). Each distance range is assigned a distinct 
color for clarity. For short distances up to 2 000 km, HCH and LOHC are the most cost effective. GH 2 
quickly becomes the most expensive option as a result of the limited capacity of the ships. At distances 
larger than 2 500 km, ammonia becomes the most cost effective technology. The exceptional energy 
density of ammonia , combined with relatively low -cost ships,  results in an almost flat cost curve.  
Figure 10b shows the effect of supply chain scale (input energy). LH2 technology is the most prominent 
benefactor of scale increase at a fixed distance of 2 000 km (Figure 10b). At scales above 2 GW, scale 
effects lower LH 2 CapEx costs sufficiently for entering competitive cost ranges. HCH is the most cost 
competitive technology at scales below 1 GW. At intermediate (10 000 km) and long distances (19 000 
km) (Figure 10b),  ammonia is the lowest -cost technology for all scales.  Especially at long distances, 
the LCOT of ammonia is uncontested at all scales.

23 
 
Figure 10: Distance dependency of marine transportation supply chain cost per MWh delivered 
hydrogen energy.  
3.2.2 Impact cost assessment method 
In section 2.1.2.1, the conditions for equivalence between the EAC and LCOT NPV method are 
introduced. When no residual values or decommissioning costs are considered, one of the conditions 
dictates that the depreciation period of each asset in the EAC method must be equal to the assessment 
period of the LCOTNPV method. In the standard EAC method, this condition can only be met if the useful 
lifetime for each asset in the supply chain is equal to the assessment period of the LCOT NPV method. 
In hydrogen supply chains, however, the involved unit operations can have different useful lifetimes  
and depreciation times . Expensive large -scale chemical infrastructure like Haber -Bosch plants or 
thermal crackers can have operational lifetimes exceeding 40 years. Their lifetime is often the result 
of project durations or within longer projects, careful cost -benefit analysis we ighing increased 
maintenance and modernization costs versus renewal of installations. In the default settings of this 
work, it is assumed that the chemical (de)conditioning infrastructure, i.e., the liquefaction plant, LOHC 
(de)hydrogenation reactors, and ammonia synthesis and cracking infrastructure, is replaced after 20 
years, while the assessment period is conveniently set equal to those operational lifetimes. As a result, 
the condition for equivalence of assessment methods is met in default settings of the EAC, EAC2 and 
LCOTNPV for the ammonia supply chain. In most real scenarios, however, this equivalence will not hold. 
Figure 11 introduces situations where the useful lifetime exceeds the assessment period. To include 
residual value at the end of the assessment period, a linear depreciation scheme is used in the EAC2 
and LCOTNPV method. For the standard EAC method the useful lifetime of the plants is increased. The

24 
 
graph shows the effect of increasing depreciation periods on the LCOT of the ammonia supply chain. 
When the infrastructure is depreciated in 20 years, the condition for equivalence of assessment 
methods is met and all methods are equivalent. As depreciation periods increase, supply chain costs 
lower. However, the decrease in LCOT is much stronger for the EAC 2 method. This discrepancy is 
caused by the fact that, in the LCOT NPV method, the remaining value of the asset at the end of the 
assessment period is booked in the final year of the assessment and is discounted accordingly. In the 
EAC2 method, time preference of cash flows is not directly considered. For the standard EAC method, 
no residual values can be booked, as there is no specified assessment period. However, the LCOT 
lowers because costs are spread over longer useful lifetimes. 
 
Figure 11: Effect of changing depreciation time of ammonia (de)conditioning infrastructure on 
ammonia supply chain cost for three different techno-economic assessment methods. 
Depending on model settings, the techno-economic assessment method can thus have an important 
impact on the modelling results . When looking at current case studies on hydrogen supply chains in 
the literature, it is too often insufficiently clear if and how infrastructure replacements and 
depreciation is handled. Given its implications on the final results , as highlighted in Figure 11, 
dissemination of techno-economic analysis results (for academic or policy purposes) should always be 
accompanied by t ransparent documentation on and a clear motivation of the assessment method  
used.

25 
 
3.2.3 Interaction effects 
3.2.3.1 Energy cost producer region 
Figure 8 shows a very low-cost contribution for the cost attribute “hydrogen losses” in the total cost 
of the LH2 supply chain, which means that in the default scenario of this study, hydrogen boil-off from 
the ships and buffer storage can be compensated for at low cost.  Figure 12 depicts the sensitivity of 
the “hydrogen losses” cost contribution to changes in buffer tank boil -off rate and producer region 
energy cost. Boil-off rates can vary depending on uncontrollable variables such as climate and they 
are strongly dependent on technology performance. Figure A.2 summarizes 11 reference sources for 
LH2 stationary boil-off in boxplot format. While dedicated renewable electricity generation capacity is 
often planned for green hydrogen production and long-term Power Purchase Agreements might lower 
the risk for strong energy cost perturbations in the producer region, geopolitical tensions and local 
energy shortage may still result in large swings in energy cost over the project duration. Performing a 
single-parameter sensitivity analysis (white lines in Figure 12) in default settings of the model does 
not reveal strong sensitivity  towards either parameter . However, one can clearly appreciate the 
interaction effect of both parameters when they are increased simultaneously, with the hydrogen loss 
cost escalating to extreme values within the considered  parameter ranges. At an energy cost of 
0.10 €/kWh (high-end LCOE off-shore wind [104]) and a boil-off rate of 0.5% per day  (maximal non-
outlier in Figure A.2), hydrogen losses amount to 30 €/MWh (point A in Figure 12), which represents 
a 1000% increase with respect to the default “hydrogen losses” cost contribution, and a 36% increase 
with respect to default total LH2 supply chain costs. The reason behind this strong interaction effect is 
that boil-off losses are compensated for by extra production in the producer region. Considering the 
high energy costs in the consumer region, it is far more cost effective to compensate for boil-off during 
transportation or at the consumer facility by foreseeing extra production and transport , rather than 
reliquefying boil-off on site.  
While this section might not reveal a surprising synergy, the extent to which costs can escalate merits 
prudence. The example in this section is provided to illustrate the complexity of interacting cost effects 
in techno -economic assessments with many degrees of freedom. Given a certain model ling 
framework, single parameter sensitivity analyses are sometimes insufficient to provide confidence in 
the resilience of modelling results under input parameters like energy cost or technology 
performance, that can vary substantially within cases, and more particularly between different case 
studies. Comprehensive scenario analysis or m ulti-parameter sensitivity analysis protocols like the 
Sobol method  might therefore be required to realistically assess the impact of volatile input 
parameters on complex techno-economic models [105].

26 
 
 
 
Figure 12: Heatmaps showing the sensitivity  of the cost contribution “Hydrogen Losses ” for LH 2 
technology with respect to buffer boil -off rate and producer region energy cost. The white lines 
represent single parameter sensitivity analyses for both parameters, keeping the other one at default 
model settings. 
3.2.3.2 Impact of fuel transition 
Another interesting interaction effect that can be identified is the impact of a transition to clean fuels 
on the cost evolution of the different technologies with increasing supp ly chain distance.  In the 
following years, the clean energy transition will rapidly change energy system needs. Western 
industrialized economies could need sizeable imports of clean molecules. Timely establishment of 
supply chains would be needed to avoid delays to the energy transition in such a scenario. Therefore, 
the assessment of hydrogen supply chains must be seen in the right timeframe. Fossil fuels for marine 
transportation will not be banned in the coming years and they must be considered to correctly assess 
competitivity of technologies at the moment of commissioning of the first applications. To date, most 
techno-economic analyses therefore assume fossil -powered propulsion systems (Table 1). Figure 13 
compares the cost evolution with distance  for supply chains powered by  renewable fuels with their 
fossil-fuel-powered alternatives. A first observation that can be made is that the cost evolution of all 
fossil-powered technologies is nearly linear, while renewably powered supply chains show an

27 
 
increasing slope throughout the distance range. This effect is caused by the assumption that the 
renewable drivetrains use their own cargo as fuel. With increasing distance, less deliverable capacity 
remains and thus costs increase more sharply. Importantl y, these scaling discrepancies are more 
articulate for the low-density carriers. Assuming all ships will eventually be powered by renewable 
fuels, assessing fossil powered drivetrains can thus lead to a significant bias towards low energy 
density technolog ies. As ammonia fuel ’s volumetric energy density approaches fossil fuels more 
closely, little effect is witnessed in ammonia supply chains . Since using hydrogen boil-off is the most 
economical choice in both scenarios, no distinction is made for the LH2 supply chains.  
 
Figure 13: Comparison between supply chain cost evolution of fossil-powered marine supply chains 
(solid lines) with respect to their renewably powered alternatives (dashed lines). The vertical dashed 
lines indicate the maximal distance GH2 and HCH ships can travel using their own cargo as fuel. 
3.3 Limitations and future work 
The present work brings perspective to the techno-economic literature on marine hydrogen supply 
chains by critically highlighting challenges and limitations  of existing studies and approaches. 
Simultaneously also the present framework comes with its own limitations. For example, it only covers 
the handling and delivery of hydrogen after it has been produced. The production itself is not included 
in the model  (except for an estimation of costs linked to  compensation of hydrogen losses in the 
different supply chains) . When comparing specific routes using the presented  framework, it is 
therefore harder to incorporate local conditions for hydrogen production. Practically, longer, more 
expensive routes might be lucrative if the costs associated with local hydrogen production are lower. 
In future versions of the toolbox, a production module could be incorporated.  
Another limitation of the toolbox concerns result validation. The prevalence of input uncertainty and 
modelling variability and connected thereto, output variability renders benchmarking of our results 
extremely difficult.  One-on-one comparison of our specific results will only yield accidental

28 
 
quantitative confirmation. To maximize our modelling robustness, each development step of the code 
included elaborate coding logic checks, looking into edge cases and comparing outcomes with 
common sense and the outcome range found in literature.  
The current model architecture also lacks optimization for automated execution of large -scale 
sensitivity and scenario analyses, which are essential for protocols like Monte Carlo or variance-based 
sensitivity assessments. Such assessments can increase the robustness of the results and identify more 
interaction effects. Improved automation scripts could enable such analys es in future versions. The 
web-app will also be updated when new data becomes available , and at some point also alternative 
energy carriers like HVDC lines and hydrogen pipelines should be implemented. Finally, the present 
model does not provide information on the sustainability of the different supply chains . In order to 
improve the value of the outputs for policymakers,  it would be interesting to add a Life Cycle 
Assessment functionality to assess the environmental impact of the alternatives. 
4 Conclusion  
Hydrogen is considered a key energy vector that could assist decarbonizing the global energy system. 
To optimally plan the integration of hydrogen energy in the global energy system , policymakers, 
industry and energy system researchers require, unbiased and widely applicable insight on energy 
transport cost dynamics. While in recent years, many studies have modelled hydrogen supply chains, 
looking for the most cost effective transportation technologies and supply chain configurations for 
specific trading routes , the vast span of possible supply chain  scenarios and  configurations, in 
combination with the cost uncertainty related the reto, complicate generalized conclusion -making. 
Interestingly, even within similar case studies,  supply chain cost outcomes diverge strongly. Most of 
the variability is caused by the many degrees of freedom in the d esign of a hydrogen supply chain 
assessment. Variability can come from case and model specification choice, local condition volatility 
or uncertainty in technology-related data. The large variation in technology performance estimations 
is often caused by differing (1) views on technology progress, (2) operational input/output parameters 
(temperature, pressure, hydrogen purity,…), (3) modelling detail, and (4) investor perspective 
(commercial, public). Additionally, information on these factors is not always available. As a result, it 
is hard to make comprehensive conclusions on supply chain competitivity across the different 
available studies. Building on this premise , a meta-analysis model was developed to allow dynamic 
investigation of hydrogen supply chains under varying input  scenarios. By providing a convenient 
model-interface that leverages an increasing amount of underlying cost data, users are enabled to 
identify and gain insight into more generalized cost dynamics attributes of hydrogen transportation

29 
 
technologies. Authors of new studies are encouraged to send in cost data and scenarios to be included 
in the cost database. 
The model is demonstrated in default settings, for which technology-specific characteristics and cost 
drivers are identified and discussed by performing a selection of sensitivity analyses deemed 
interesting by the authors.  Under the range of conditions studied, some general technology 
characteristics are noteworthy. GH 2 technology is fit  only for short-distance supply chains, as costs 
escalate quickly due to its low gravimetric energy density. While stationary infrastructure cost is low, 
costs are dominated by CapEx for storage tanks.  Due to its high energy efficiency, however, GH 2 can 
be an option for short distance routes sourcing from regions with relatively high energy cost.  LH2 
technology cost is dominated by liquefaction plant and storage costs , and scale effects strongly 
increase LH2’s cost competitivity. Additionally, low energy cost in the producer region is important as 
hydrogen liquefaction is by far the most energy intensive  unit operation in the supply chain. LOHC 
(DBT) technology is favored by low fleet expansion cost per ship and convenience, as current diesel 
carriers can be used. However, the mediocre energy density leads to sub -optimal scaling at the fleet 
level. Ammonia carrie r ships are both relatively low -cost and energy dense, which leads to cost -
effective scaling. Supply chain costs are dominated by stationary infrastructure cost. Finally, HCH 
technology shows strong similarities with GH2 technology, but is favored by more cost-efficient scaling 
due to improved gravimetric energy density. 
In techno-economic analyses, the goal is to translate technical complexities in given macro-economic 
conditions into a non -biased cost indicator, which can be compared to technology alternatives. 
Multiple methods are available to distil the same cost structures into an overall cost indicator. The 
two most popular methods used in hydrogen supply chain analyses were incorporated into the 
presented model and conditions for mathematical equivalence were investigated. Analyses outside 
these conditions showed that the different time discounting strategies in cost assessment methods 
can cause wide cost divergence when depreciation time of expensive infrastructure is not matched 
with the assessment period of the analysis. Clear communication on depreciation and time 
discounting strategies should therefore always be included in techno-economic assessments involving 
cost-intensive infrastructure with particularly short or long lifetimes.  
Figure 14 shows the cost evolution of the lowest -cost technology of the model in default settings 
throughout the considered distance range, combined with the optimal technology choice at specified 
distances from studies considered in this work  (Table 1). It is clear that there is no consensus in the 
literature when correcting for distance.  The LCOT of our findings in default settings  varies between 
30-66 €/MWh (roughly 1 -2 €/kgH2), without considering hydrogen production cost. While physical

30 
 
bounds limit energy efficiency of hydrogen supply chains indefinitely, large cost improvements for the 
required infrastructure can be achieved with scale and maturity in the hydrogen supply chain market. 
The sustainable energy and chemical feedstock transition will require a vast span of solutions. It is the 
task of academics to provide policymakers with unbiased information and tools to make informed and 
future-proof decisions for each part of the global transition towards climate neutrality. Whether, and 
to what extent, hydrogen imports are a part of that transition will depend on  geopolitics, economics 
and capital deployment across dispatchable energy alternatives and chemical feedstock options. With 
this work, we want to provide insight into hydrogen transportation economics, based on the currently 
available literature. The interactive application dashboard is available to gain insight into the vast span 
of possible scenarios involved in hydrogen supply chain economics and can be freely accessed online 
[106].  
 
 
Figure 14: Evolution of best case LCOT for the default settings of the model, combined with best 
technology outcomes of case studies in literature. The position of the literature sources on the graph 
is not indicative of the quantitative LCOT in the studies, as different scope and input parameters 
render quantitative comparison uninformative.  
Supplemental information 
Document A1. Figures A.1-A.4. Tables A.1-A.14. 
Acknowledgement 
The authors acknowledge VLAIO for Moonshot funding (ARCLATH, n° HBC.2019.0110, ARCLATH2, n° 
HBC.2021.0254). M.H. acknowledges FWO for an FWO -SB fellowship. J.A.M. acknowledges the

31 
 
Flemish Government for long -term structural funding (Methusalem) and department EWI for 
infrastructure investment via the Hermes Fund (AH.2016.134). NMRCoRe acknowledges the Flemish 
government, department EWI for financial support as International Research  Infrastructure 
(I001321N: Nuclear Magnetic Resonance Spectroscopy Platform for Molecular Water Research). 
J.A.M. acknowledges the European Research Council (ERC) for an Advanced Research Grant under the 
European Union’s Horizon 2020 research and innovatio n programme under grant agreement No. 
834134 (WATUSO).  
Credit author statement 
L.Hanssens: Conceptualization, Investigation, Methodology, Formal analysis, Validation, Original Draft 
and Visualization. K. Van Acker & M.Houlleberghs: Validation and Review & Editing. L. Hanssens & E. 
Breynaert: Implementation of the web -application. E.Breynaert & J.A.Martens: Conceptualization, 
Validation, Writing – Review & Editing, Supervision, Funding acquisition.  
Declaration of competing interest 
The authors declare that the research was conducted in the absence of any commercial, financial or 
personal relationships that could be constured as a potential conflict of interest. 
References 
[1] European Commission. Green Deal EU. Brussels: 2019. 
[2] Energy Transitions Commission. Making the Hydrogen Economy Possible: Accelerating Clean 
Hydrogen in an Electrified Economy. London: 2021. 
[3] International Energy Agency. World Energy Outlook 2023. Paris: 2023. 
[4] European Commission. A hydrogen strategy for a climate-neutral Europe. Brussels: 2020. 
[5] International Energy Agency. The Future of Hydrogen. Paris: 2019. 
[6] Samadi S, Fischer A, Lechtenböhmer S. The renewables pull effect: How regional differences in 
renewable energy costs could influence where industrial production is located in the future. 
Energy Res Soc Sci 2023;104. https://doi.org/10.1016/j.erss.2023.103257. 
[7] Verpoort PC, Gast L, Hofmann A, Ueckerdt F. Impact of global heterogeneity of renewable 
energy supply on heavy industrial production and green value chains. Nat Energy 2024;9:491–
503. https://doi.org/10.1038/s41560-024-01492-z.

32 
 
[8] Chapman AJ, Fraser T, Itaoka K. Hydrogen import pathway comparison framework 
incorporating cost and social preference: Case studies from Australia to Japan. Int J Energy Res 
2017;41:2374–91. https://doi.org/10.1002/er.3807. 
[9] Heuser PM, Ryberg DS, Grube T, Robinius M, Stolten D. Techno-economic analysis of a potential 
energy trading link between Patagonia and Japan based on CO2 free hydrogen. Int J Hydrogen 
Energy 2019;44:12733–47. https://doi.org/10.1016/j.ijhydene.2018.12.156. 
[10] Johnston C, Ali Khan MH, Amal R, Daiyan R, MacGill I. Shipping the sunshine: An open -source 
model for costing renewable hydrogen transport from Australia. Int J Hydrogen Energy 
2022;47:20362–77. https://doi.org/10.1016/j.ijhydene.2022.04.156. 
[11] Ishimoto Y, Voldsund M, Nekså P, Roussanaly S, Berstad D, Gardarsdottir SO. Large -scale 
production and transport of hydrogen from Norway to Europe and Japan: Value chain analysis 
and comparison of liquid hydrogen and ammonia as energy carriers. Int J Hydrogen Energy 
2020;45:32865–83. https://doi.org/10.1016/j.ijhydene.2020.09.017. 
[12] d’Amore-Domenech R, Meca VL, Pollet BG, Leo TJ. On the bulk transport of green hydrogen at 
sea: Comparison between submarine pipeline and compressed and liquefied transport by ship. 
Energy 2023;267. https://doi.org/10.1016/j.energy.2023.126621. 
[13] Simoes S, Nijs W, Ruiz P, Sgobbi A, Radu D, Bolat P, et al. The JRC -EU-TIMES model. 2013. 
https://doi.org/10.2790/97596. 
[14] HOMER - Hybrid Renewable and Distributed Generation System Design Software 2025. 
[15] Howells M, Rogner H, Strachan N, Heaps C, Huntington H, Kypreos S, et al. OSeMOSYS: The 
Open Source Energy Modeling System. An introduction to its ethos, structure and 
development. Energy Policy 2011;39:5850–70. https://doi.org/10.1016/j.enpol.2011.06.033. 
[16] PLEXOS Energy Modeling Software 2025. 
[17] Niermann M, Drünert S, Kaltschmitt M, Bonhoff K. Liquid organic hydrogen carriers (LOHCs) – 
techno-economic analysis of LOHCs in a defined process chain. Energy Environ Sci 
2019;12:290–307. https://doi.org/10.1039/C8EE02700E. 
[18] Niermann M, Timmerberg S, Drünert S, Kaltschmitt M. Liquid Organic Hydrogen Carriers and 
alternatives for international transport of renewable hydrogen. Renewable and Sustainable 
Energy Reviews 2021;135. https://doi.org/10.1016/j.rser.2020.110171.

33 
 
[19] d’Amore-Domenech R, Leo TJ, Pollet BG. Bulk power transmission at sea: Life cycle cost 
comparison of electricity and hydrogen as energy vectors. Appl Energy 2021;288. 
https://doi.org/10.1016/j.apenergy.2021.116625. 
[20] Gallardo FI, Monforti Ferrario A, Lamagna M, Bocci E, Astiaso Garcia D, Baeza -Jeria TE. A 
Techno-Economic Analysis of solar hydrogen production by electrolysis in the north of Chile 
and the case of exportation from Atacama Desert to Japan. Int J Hydro gen Energy 
2021;46:13709–28. https://doi.org/10.1016/j.ijhydene.2020.07.050. 
[21] Raab M, Maier S, Dietrich RU. Comparative techno -economic assessment of a large -scale 
hydrogen transport via liquid transport media. Int J Hydrogen Energy 2021;46:11956 –68. 
https://doi.org/10.1016/j.ijhydene.2020.12.213. 
[22] Brändle G, Schönfisch M, Schulte S. Estimating long -term global supply costs for low -carbon 
hydrogen. Appl Energy 2021;302. https://doi.org/10.1016/j.apenergy.2021.117481. 
[23] Roos TH. The cost of production and storage of renewable hydrogen in South Africa and 
transport to Japan and EU up to 2050 under different scenarios. Int J Hydrogen Energy 
2021;46:35814–30. https://doi.org/10.1016/j.ijhydene.2021.08.193. 
[24] Collis J, Schomäcker R. Determining the Production and Transport Cost for H2 on a Global Scale. 
Front Energy Res 2022;10. https://doi.org/10.3389/fenrg.2022.909298. 
[25] Lee JS, Cherif A, Yoon HJ, Seo SK, Bae JE, Shin HJ, et al. Large -scale overseas transportation of 
hydrogen: Comparative techno -economic and environmental investigation. Renewable and 
Sustainable Energy Reviews 2022;165. https://doi.org/10.1016/j.rser.2022.112556. 
[26] Borsboom-Hanson T, Patlolla SR, Herrera OE, Mérida W. Point -to-point transportation: The 
economics of hydrogen export. Int J Hydrogen Energy 2022;47:31541 –50. 
https://doi.org/10.1016/j.ijhydene.2022.07.093. 
[27] Dickson R, Akhtar MS, Abbas A, Park ED, Liu J. Global transportation of green hydrogen via 
liquid carriers: economic and environmental sustainability analysis, policy implications, and 
future directions. Green Chemistry 2022;24:8484–93. https://doi.org/10.1039/d2gc02079c. 
[28] Perey P, Mulder M. International competitiveness of low -carbon hydrogen supply to the 
Northwest European market. Int J Hydrogen Energy 2023;48:1241 –54. 
https://doi.org/10.1016/j.ijhydene.2022.10.011.

34 
 
[29] Cui J, Aziz M. Techno -economic analysis of hydrogen transportation infrastructure using 
ammonia and methanol. Int J Hydrogen Energy 2023;48:15737 –47. 
https://doi.org/10.1016/j.ijhydene.2023.01.096. 
[30] Neumann J, da Rocha RC, Debiagi P, Scholtissek A, Dammel F, Stephan P, et al. Techno -
economic assessment of long-distance supply chains of energy carriers: Comparing hydrogen 
and iron for carbon-free electricity generation. Applications in Energy and Combustion Science 
2023;14. https://doi.org/10.1016/j.jaecs.2023.100128. 
[31] Hampp J, Düren M, Brown T. Import options for chemical energy carriers from renewable 
sources to Germany. PLoS One 2023;18. https://doi.org/10.1371/journal.pone.0281380. 
[32] Villalba-Herreros A, d’Amore -Domenech R, Crucelaegui A, Leo TJ. Techno -Economic 
Assessment of Large -Scale Green Hydrogen Logistics Using Ammonia As Hydrogen Carrier: 
Comparison to Liquified Hydrogen Distribution and In Situ Production. ACS Sustain Che m Eng 
2023;11:4716–26. https://doi.org/10.1021/acssuschemeng.2c07136. 
[33] Kim S, Park J, Chung W, Adams D, Lee JH. Techno -economic analysis for design and 
management of international green hydrogen supply chain under uncertainty: An integrated 
temporal planning approach. Energy Convers Manag 2024;301. 
https://doi.org/10.1016/j.enconman.2023.118010. 
[34] Reuß M, Grube T, Robinius M, Preuster P, Wasserscheid P, Stolten D. Seasonal storage and 
alternative carriers: A flexible hydrogen supply chain model. Appl Energy 2017;200:290 –302. 
https://doi.org/10.1016/j.apenergy.2017.05.050. 
[35] Anastasopoulou A, Furukawa H, Barnett BR, Jiang HZH, Long JR, Breunig HM. Technoeconomic 
analysis of metal -organic frameworks for bulk hydrogen transportation. Energy Environ Sci 
2021;14:1083–94. https://doi.org/10.1039/d0ee02448a. 
[36] Preuster P, Alekseev A, Wasserscheid P. Hydrogen Storage Technologies for Future Energy 
Systems 2017. https://doi.org/10.1146/annurev-chembioeng. 
[37] Rong Y, Chen S, Li C, Chen X, Xie L, Chen J, et al. Techno-economic analysis of hydrogen storage 
and transportation from hydrogen plant to terminal refueling station. Int J Hydrogen Energy 
2023. https://doi.org/10.1016/j.ijhydene.2023.01.187. 
[38] Cebolla O, Dolci R, Dolci F. Assessment of Hydrogen Delivery Options Feasibility of Transport of 
Green Hydrogen within Europe. Brussels: 2023. https://doi.org/10.2760/869085.

35 
 
[39] United States Department of Energy. Fuel Cell Technologies Office Multi -Year Research, 
Development, and Demonstration Plan - Section 3.2 Hydrogen Delivery. 2015. 
[40] Connelly E, Penev M, Elgowainy A, Hunter C. Current Status of Hydrogen Liquefaction Costs. 
Washington: 2019. 
[41] Weichenchain U. Hydrogen transportation: The key to unlocking the clean hydrogen economy. 
2021. 
[42] Papadias DD, Peng JK, Ahluwalia RK. Hydrogen carriers: Production, transmission, 
decomposition, and storage. Int J Hydrogen Energy 2021;46:24169 –89. 
https://doi.org/10.1016/j.ijhydene.2021.05.002. 
[43] Jackson C, Fothergill K, Gray P, Haroon F, Makhloufi C, Kezibri N, et al. Ammonia to Green 
Hydrogen Project. 2020. 
[44] Brasington RD, Haslback JL, Kuehn NJ, Lewis EG, Pinkerton LL, Turner MJ, et al. Cost and 
Performance Baseline for Fossil Energy Plants Volume 2:   Coal to Synthetic Natural Gas and 
Ammonia. International Journal of Coastal & Offshore Engineering 2011. 
[45] Makhloufi C, Kezibri N. Large -scale decomposition of green ammonia for pure hydrogen 
production. Int J Hydrogen Energy 2021;46:34777 –87. 
https://doi.org/10.1016/j.ijhydene.2021.07.188. 
[46] Spatolisano E, Restelli F, Matichecchia A, Pellegrini LA, de Angelis AR, Cattaneo S, et al. 
Assessing opportunities and weaknesses of green hydrogen transport via LOHC through a 
detailed techno -economic analysis. Int J Hydrogen Energy 2023. 
https://doi.org/10.1016/j.ijhydene.2023.08.040. 
[47] Di Lullo G, Giwa T, Okunlola A, Davis M, Mehedi T, Oni AO, et al. Large-scale long-distance land-
based hydrogen transportation systems: A comparative techno-economic and greenhouse gas 
emission assessment. Int J Hydrogen Energy 2022;47:35293 –319. 
https://doi.org/10.1016/j.ijhydene.2022.08.131. 
[48] Wang A, van der Leun K, Peters D, Buseman M. European Hydrogen Backbone: How a 
dedicated hydrogen infrastructure can be created. 2020. 
[49] Waterstof Industrie Cluster. A Flemish Hydrogen Strategy. 2020. 
[50] Züttel A. Materials for hydrogen storage. Materials Today 2003;6:24 –33. 
https://doi.org/10.1016/S1369-7021(03)00922-2.

36 
 
[51] Reddi K, Elgowainy A, Rustagi N, Gupta E. Techno -economic analysis of conventional and 
advanced high -pressure tube trailer configurations for compressed hydrogen gas 
transportation and refueling. Int J Hydrogen Energy 2018;43:4428 –38. 
https://doi.org/10.1016/J.IJHYDENE.2018.01.049. 
[52] Zheng J, Liu X, Xu P, Liu P, Zhao Y, Yang J. Development of high pressure gaseous hydrogen 
storage technologies. Int J Hydrogen Energy 2012;37:1048 –57. 
https://doi.org/10.1016/j.ijhydene.2011.02.125. 
[53] Elberry AM, Thakur J, Santasalo-Aarnio A, Larmi M. Large-scale compressed hydrogen storage 
as part of renewable electricity storage systems. Int J Hydrogen Energy 2021;46:15671 –90. 
https://doi.org/10.1016/j.ijhydene.2021.02.080. 
[54] Hurskainen M, Ihonen J. Techno-economic feasibility of road transport of hydrogen using liquid 
organic hydrogen carriers. Int J Hydrogen Energy 2020;45:32098 –112. 
https://doi.org/10.1016/j.ijhydene.2020.08.186. 
[55] Schmidt R. Liquid Organic Hydrogen Carrier Technologies 2020. 
https://www.powerfuels.org/fileadmin/powerfuels.org/Dokumente/Presentations_Annual_C
onference_2021/S5-01_Schmidt_Hydrogenious.pdf (accessed May 2, 2022). 
[56] Brückner N, Obesser K, Bösmann A, Teichmann D, Arlt W, Dungs J, et al. Evaluation of 
industrially applied heat -transfer fluids as liquid organic hydrogen carrier systems. 
ChemSusChem 2014;7:229–35. https://doi.org/10.1002/cssc.201300426. 
[57] Müller K, Stark K, Emelyanenko VN, Varfolomeev MA, Zaitsau DH, Shoifet E, et al. Liquid Organic 
Hydrogen Carriers: Thermophysical and Thermochemical Studies of Benzyl - and Dibenzyl -
toluene Derivatives. Ind Eng Chem Res 2015;54:7967 –76. 
https://doi.org/10.1021/acs.iecr.5b01840. 
[58] Smith C, Hill AK, Torrente -Murciano L. Current and future role of Haber -Bosch ammonia in a 
carbon-free energy landscape †. Energy Environ Sci 2020;13:331. 
https://doi.org/10.1039/c9ee02873k. 
[59] Thomas G, Parks G. Potential Roles of Ammonia in a Hydrogen Economy A Study of Issues 
Related to the Use Ammonia for On-Board Vehicular Hydrogen Storage. Washington: 2006. 
[60] Thyssenkrupp. Ammonia in agriculture: The engine of plant growth 2022. 
https://www.thyssenkrupp.com/en/stories/sustainability-and-climate-protection/ammonia-
in-agriculture:-the-engine-of-plant-growth (accessed November 10, 2022).

37 
 
[61] Hydrogen Import Coalition. Hydrogen Import Coalition Final report: Executive summary -3-4. 
2020. 
[62] Australian Renewable Energy Agency. German -Australian Hydrogen Innovation and 
Technology Incubator (HyGATE) Funding Announcement. Canberra: 2022. 
[63] Lamb KE, Dolan MD, Kennedy DF. Ammonia for hydrogen storage; A review of catalytic 
ammonia decomposition and hydrogen separation and purification. Int J Hydrogen Energy 
2019;44:3580–93. https://doi.org/10.1016/J.IJHYDENE.2018.12.024. 
[64] Rispens JR, Jones SA, Clemmons NS, Ahmed S, Harduar -Morano L, Johnson MD, et al. 
Anhydrous Ammonia Chemical Release — Lake County, Illinois, April 2019. MMWR Morb 
Mortal Wkly Rep 2020;69:109–13. https://doi.org/10.15585/MMWR.MM6904A4. 
[65] Padappayil RP, Borger J. Ammonia Toxicity 2023. 
https://www.ncbi.nlm.nih.gov/books/NBK546677/ (accessed May 25, 2022). 
[66] Veluswamy HP, Kumar R, Linga P. Hydrogen storage in clathrate hydrates: Current state of the 
art and future directions. Appl Energy 2014;122:112 –32. 
https://doi.org/10.1016/j.apenergy.2014.01.063. 
[67] Gupta A, Baron G V., Perreault P, Lenaerts S, Ciocarlan RG, Cool P, et al. Hydrogen Clathrates: 
Next Generation Hydrogen Storage Materials. Energy Storage Mater 2021;41:69 –107. 
https://doi.org/10.1016/J.ENSM.2021.05.044. 
[68] Casco ME, Silvestre -Albero J, Ramírez -Cuesta AJ, Rey F, Jordá JL, Bansode A, et al. Methane 
hydrate formation in confined nanospace can surpass nature. Nat Commun 2015;6. 
https://doi.org/10.1038/NCOMMS7432. 
[69] Cruz FJAL, Mota JPB. Structure and thermodynamics of empty clathrate hydrates below the 
freezing point of water. Physical Chemistry Chemical Physics 2021;23:16033 –43. 
https://doi.org/10.1039/d1cp00893e. 
[70] Mannel D, Puckett D. Transportation and Storage of Natural Gas Hydrates. Oklahoma: 2008. 
[71] Nogami T, Watanabe S. Development of Natural -Gas Supply Chain by Means of Natural -Gas 
Hydrates. Journal of Petroleum Technology 2009;61:62 –4. https://doi.org/10.2118/0709 -
0062-JPT.

38 
 
[72] Javanmardi J, Nasrifar K, Najibi SH, Moshfeghian M. Natural gas transportation: NGH or LNG? 
World Review of Science, Technology and Sustainable Development 2007;4:258 –67. 
https://doi.org/10.1504/WRSTSD.2007.013585. 
[73] Kanda H. Economic Study on Natural Gas Transportation with Natural Gas Hydrate (NGH) 
Pellets. 2006. 
[74] Bortnowska M. Development of new technologies for shipping natural gas by sea. Polish 
Maritime Research 2009;16:70–8. https://doi.org/10.2478/v10012-008-0036-2. 
[75] Zhang Y, Bhattacharjee G, Kumar R, Linga P. Solidified Hydrogen Storage (Solid -HyStore) via 
Clathrate Hydrates. Chemical Engineering Journal 2022;431. 
https://doi.org/10.1016/j.cej.2021.133702. 
[76] Kumar R, Klug DD, Ratcliffe CI, Tulk CA, Ripmeester JA, Klug DD, et al. Low -Pressure Synthesis 
and Characterization of Hydrogen -Filled Ice  Ic. Angewandte Chemie International Edition 
2013;52:1531–4. https://doi.org/10.1002/ANIE.201208367. 
[77] Lee H, Lee JW, Kim DY, Park J, Seo YT, Zeng H, et al. Tuning clathrate hydrates for hydrogen 
storage. Nature 2005;434:743–6. https://doi.org/10.1038/nature03457. 
[78] Pera-Titus M, El -Chahal R, Rakotovao V, Daniel C, Miachon S, Dalmon JA. Direct Volumetric 
Measurement of Gas Oversolubility in Nanoliquids: Beyond Henry’s Law. ChemPhysChem 
2009;10:2082–9. https://doi.org/10.1002/CPHC.200900058. 
[79] Zhang G, Sun M, Liu B, Wang F. Adsorption -induced two -way nanoconvection enhances 
nucleation and growth kinetics of methane hydrates in confined porespace. Chemical 
Engineering Journal 2020;396:125256. https://doi.org/10.1016/J.CEJ.2020.125256. 
[80] Jazdzewska M, Śliwinska-Bartkowiak MM, Beskrovnyy AI, Vasilovskiy SG, Ting SW, Chan KY, et 
al. Novel ice structures in carbon nanopores: pressure enhancement effect of confinement. 
Physical Chemistry Chemical Physics 2011;13:9008–13. https://doi.org/10.1039/C0CP02797A. 
[81] Zhang G, Liu B, Xu L, Zhang R, He Y, Wang F. How porous surfaces influence the nucleation and 
growth of methane hydrates. Fuel 2021;291:120142. 
https://doi.org/10.1016/J.FUEL.2021.120142. 
[82] Beckwée EJ, Watson G, Houlleberghs M, Arenas Esteban D, Bals S, Van Der Voort P, et al. 
Enabling hydrate -based methane storage under mild operating conditions by periodic 
mesoporous organosilica nanotubes. Heliyon 2023;9. 
https://doi.org/10.1016/j.heliyon.2023.e17662.

39 
 
[83] Farrando-Perez J, Balderas-Xicohtencatl R, Cheng Y, Daemen L, Cuadrado-Collados C, Martinez-
Escandell M, et al. Rapid and efficient hydrogen clathrate hydrate formation in confined 
nanospace. Nat Commun 2022;13:5953. https://doi.org/10.1038/s41467-022-33674-2. 
[84] Beckwée EJ, Houlleberghs M, Ciocarlan RG, Chandran CV, Radhakrishnan S, Hanssens L, et al. 
Structure I methane hydrate confined in C8 -grafted SBA-15: A highly efficient storage system 
enabling ultrafast methane loading and unloading. Appl Energy 2024; 353. 
https://doi.org/10.1016/j.apenergy.2023.122120. 
[85] Global Energy Ventures Ltd. CNG Optimum – Global Energy Ventures Ltd 2022. 
https://gev.com/cng-optimum/ (accessed January 17, 2022). 
[86] Lazard ltd., Roland Berger. 2023 LCOE Lazard. 2023. 
[87] Eurostat. Electricity price statistics 2023. https://ec.europa.eu/eurostat/statistics -
explained/index.php?title=Electricity_price_statistics#Electricity_prices_for_non-
household_consumers (accessed November 28, 2023). 
[88] Deloitte. Challenge to the industry Securing skilled crews in today’s marketplace. 2011. 
[89] Weekly Oil Bulletin n.d. https://energy.ec.europa.eu/data-and-analysis/weekly-oil-bulletin_en 
(accessed June 6, 2022). 
[90] Rotterdam Bunker Prices - Ship & Bunker n.d. 
https://shipandbunker.com/prices/emea/nwe/nl-rtm-rotterdam#IFO380 (accessed June 3, 
2022). 
[91] Rodrigue J -P. The Geography of Transport Systems. 5th ed. New York: Routledge; 2020. 
https://doi.org/10.4324/9780429346323. 
[92] Aldersey-Williams J, Rubert T. Levelised cost of energy – A theoretical justification and critical 
assessment. Energy Policy 2019;124:169–79. https://doi.org/10.1016/j.enpol.2018.10.004. 
[93] Foster J, Wagner LD, Bratanova A, Wagner L. LCOE models: A comparison of the theoretical 
frameworks and key assumptions LCOE models. 2014. 
[94] Jones TW, Smith JD. An Historical Perspective of Net Present Value and Equivalent Annual Cost. 
Account Hist J 1982;9:103–10. 
[95] Oxera. Discount rates for low-carbon and renewable generation technologies Prepared for the 
Committee on Climate Change. 2011.

40 
 
[96] García-Gusano D, Espegren K, Lind A, Kirkengen M. The role of the discount rates in energy 
systems optimisation models. Renewable and Sustainable Energy Reviews 2016;59:56 –72. 
https://doi.org/10.1016/j.rser.2015.12.359. 
[97] Mohendroo M. Some common mistakes to avoid in estimating and applying discount rates. 
Deloitte Spring 2014 Middle East Point of View 2014:36–43. 
[98] International Renewable Energy Agency. Renewable Power Generation Costs 2020. Abu Dhabi: 
2021. 
[99] Australian Embassy Germany. ‘Shipping the Sunshine’, The Australia -Germany partnership. 
2022. 
[100] International Energy Agency. Renewable Hydrogen from Oman: A producer economy in 
transition. Paris: 2023. 
[101] Hyphen Hydrogen Energy. Pioneering the African Green Hydrogen Revolution - Namibia 2023. 
https://hyphenafrica.com/namibia/ (accessed November 27, 2023). 
[102] US Internal Revenue Service. Publication 946 (2022), How To Depreciate Property 2022. 
https://www.irs.gov/publications/p946 (accessed November 7, 2023). 
[103] The University of Manchester. Chemical Engineering Plant Cost Index 2023. 
https://personalpages.manchester.ac.uk/staff/tom.rodgers/Interactive_graphs/CEPCI.html?r
eactors/CEPCI/index.html (accessed October 26, 2023). 
[104] International Energy Agency. Projected Costs of Generating Electricity. 2020. 
[105] Wei W, Larrey-Lassalle P, Faure T, Dumoulin N, Roux P, Mathias JD. How to conduct a proper 
sensitivity analysis in life cycle assessment: Taking into account correlations within LCI data and 
interactions within the LCA calculation model. Environ Sci Technol 2015;49:377 –85. 
https://doi.org/10.1021/es502128k. 
[106] Hanssens L, Houlleberghs M, Van Acker K, Martens J, Breynaert E. Hydrogen Supply Chain 
Dashboard 2024. 
https://script.google.com/macros/s/AKfycbwoSX4K5dUJmykwXWmtsKj_UKAF_z0pdDaBjuj9j4
v-LSE6zgas3RPNsTnhx-TCMLVHcg/exec (accessed October 7, 2024).

41
