---
source_id: "arxiv"
title: "arXiv:2508.10923"
url: "https://arxiv.org/abs/2508.10923"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2508.10923. Abstract: 1 
 
Interactive framework for techno-economic meta-analysis of marine hydrogen 
transportation  
Lucas Hanssens 1, Maarten Houlleberghs 1, Karel Van Acker ,2,3,4 , Johan A. Martens 1,5 and Eric 
Breynaert1,5,* 
Abstract 
As a result of the wide span of uncertainties and input variables considered in recent peer-reviewed 
studies on hydrogen supply chains, consensus and generalized insight are har"
---

# arXiv:2508.10923

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
