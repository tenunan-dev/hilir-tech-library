---
source_id: "lemigas-scog"
title: "Multi objective Optimization of Risk Based Inspection Planning for Oil and Gas Piping Systems Using NSGA II Al"
summary: "Optimisation study using the NSGA-II genetic algorithm to set inspection intervals for oil and gas piping, trading probability of failure against inspection cost."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2084"
retrieved_at: "2026-10-24T14:30:36+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "97f6f3d7581eb3337a403cc3ee347f7eff7e5ece5a0be8c24faf6af3dcb51bf7"
collected: "manual"
---

# Multi objective Optimization of Risk Based Inspection Planning for Oil and Gas Piping Systems Using NSGA II Al

DOI org/10.29017/scog.v49i2.2084 I 393 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Multi-Objective Optimization of Risk-Based Inspection Planning                         
for Oil and Gas Piping Systems Using NSGA-II Algorithm 
ABSTRACT - The systematic examination of piping is essential in the successful implementation of risk -
based inspection (RBI). The ineffective execution of this activity increases the risk of equipment failure and 
unnecessary costs. Therefore, this study aims to address the challenge of optimizing inspection planning for 
oil and gas piping systems in budget and operational constraints. The most effective inspection methods 
were selected to determine the optimal inspection interval. A multi -objective optimization model based on 
non-dominated sorting genetic algorithm -II was also applied to simultaneously minimize probability of 
failure as well as optimize total inspection costs. The adopted methodology, which is dissimilar to 
traditional methods, eliminated reliance on predefined risk thresholds and explicit failure -consequence 
evaluations by directly incorporating inspection costs. Additionally, the best -performing model achieved an 
efficient solution by reducing the total probability of failure from 1.631 10 -1 to 0.8975 10-1. The application 
model further provided a robust decision-support tool for efficient inspection planning, increased inspection 
effectiveness, and reduced risk of failure (RoF). The developments formed the basis for effective decision -
making to support the implementation of asset integrity management through efficient inspection planning. 
Keywords : inspection planning, multi-objective optimization, oil and gas, piping, risk-based inspection.  
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 393 - 408 
1Department of Interdisciplinary School Management and Technology, Institut Teknologi Sepuluh Nopember 
ITS Main Road, Keputih, Sukolilo District, Surabaya, East Java 60111, Indonesia 
2Asset Integrity & Reliability, PT Pertamina Hulu Rokan,                                                                                                                                  
Prof. DR. Satrio Street No. 30, RT. 17/RW. 4, Karet Kuningan, Setiabudi Subdistrict, South Jakarta City, 12940 
3Department of Mathematics, Institut Teknologi Sepuluh Nopember 
ITS Main Road, Keputih, Sukolilo District, Surabaya, East Java 60111, Indonesia 
4Department of Materials and Metallurgical Engineering, Institut Teknologi Sepuluh Nopember 
ITS Main Road, Keputih, Sukolilo District, Surabaya, East Java 60111, Indonesia 
Corresponding author: Endah R.M. Putri (endahrmp@matematika.its.ac.id) 
Manuscript received:  February 27th, 2026; Revised: April 01st, 2026 
Approved:  May 04th, 2026; Available online: June 15th, 2026; Published: June 15th, 2026. 
Tri Wahono1,2, Endah R.M. Putri3, Imam Mukhlash3, and Agung Purniawan4 
 
Copyright © 2026 by Authors, Published by LEMIGAS

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
394 I DOI org/10.29017/scog.v49i2.2084 
How to cite this article: 
Tri Wahono, Endah R.M. Putri, Imam Mukhlash, and Agung Purniawan , 2026, Multi-
Objective Optimization of Risk -Based Inspection Planning for Oil and Gas Piping Systems 
Using NSGA-II Algorithm, Scientific Contributions Oil and Gas, 49 (2) pp. 393 - 408. DOI 
org/10.29017/scog.v49i2.2084.  
INTRODUCTION 
The equipment supporting oil and gas 
operations is presumed to face challenges posed by 
complex related procedures and aging facilities 
(Asyik et al., 2026). Inspection is the main tool for 
verifying that all equipment in production facilities 
is in optimal condition for operational 
functionality. It also ensures the prevention of 
damages in advance. However, inspecting all 
equipment equally is inefficient, considering the 
extremely large and complex number of operation 
facilities (Rachman & Ratnayake 2019). The asset 
integrity management system also plays an 
important role in preventing failure. The process is 
actualized by reducing degradation, minimizing 
risk, and ensuring the safe operation of lifecycle 
assets (Wahono et al., 2025). Risk-based inspection 
(RBI) has become a central solution in the new 
global economy to reduce excessive financial 
losses, including impairment, for companies in oil 
and gas sector (Aditiyawarman et al., 2023). 
Based on this perspective, RBI was conducted 
to develop an optimal plan for inspection 
implementation, alongside improving safety and 
integrity to maintain efficient operations and 
equipment (Campari et al., 2024). This also offered 
a common framework for evaluating equipment 
risk, as well as facilitated the identification of 
connections between breakdown mechanisms and 
related failure modes (Abubakirov et al., 2020). 
Meanwhile, a typical example of a lack of an 
inspection program for piping systems is Richmond 
refinery pipe rupture and fire case (Weber 2006). 
This led to the two main activities of RBI program, 
namely risk assessment and inspection planning 
(API RP 580 2023). Previous studies reported that 
inspection planning has several challenges, namely 
prioritizing the equipment to inspect, determining 
when to conduct inspection, and selecting the most 
appropriate method based on risk level.  
Considering the widespread adoption of RBI in 
oil and gas sector, existing inspection planning 
methods often depended on deterministic or single-
objective methods. These processes do not 
adequately account for trade -offs between safety 
and inspection costs. For example, Teurupun et al., 
(2024), proposed RBI methodology for pressure 
safety valves and stripper acid gas removal with a 
fixed inspection interval. Reliability -based FFS 
studies focused on predicting present risks and 
determining the remaining life, including the 
ability of the equipment to withstand internal 
pressures since the last inspection. Seo et al. (2015) 
reported that it was difficult to accurately predict 
inspection planning, alongside the level of risk 
encountered during the operating period. The 
determination of inspection intervals was also 
based on probability of failure and the potential 
undesirable effects of the transferred fluid (Sözen 
et al., 2022). With budget constraints, RBI not only 
reduces failures but also minimizes costs. 
Several studies have advanced RBI planning in 
recent years. For example, Moura et al. (2015) 
proposed coupling RBI methodology with multi -
objective genetic algorithm (MOGA). The study 
focused on oil and gas separator vessel that 
experienced both internal and external corrosion, 
leading to material thinning. The results showed 
that the methodology provided an effective tool for 
making efficient decisions concerning equipment 
mechanical integrity. In 2019, Abubakirov et al. 
(2020) introduced a method for determining 
optimal inspection intervals for underground oil 
pipelines. This study used a utility function to 
optimize the inspection interval by combining risk 
and annual related program cost. Y. Javid (2025) 
developed inspection optimization methods in the 
petrochemical industry to reduce overall risk 
exposure while optimizing expenditures. This 
included the integration of RBI principles with a

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 395 
 
novel two -objective mathematical model, which 
led to the formulation of a comprehensive 
framework for equipment inspection programs. 
In line with the optimization method proposed 
by previous studies, the implementation across 
multiple industries and equipment categories 
remained inadequately investigated. Considering 
the identified gap, this study addressed the earlier 
mentioned challenges by developing a multi -
objective optimization framework for planning oil 
and gas piping RBI. The proposed framework 
simultaneously optimized inspection intervals, 
safety performance, and costs to support more 
effective decision -making regarding planning. 
Additionally, the framework aimed to improve 
the efficiency and reliability of piping inspection 
programs. The entire procedure was actualized 
by integrating risk assessment with multi -
objective optimization.   
This study aims to show the application of a 
multi-objective optimization perspective to RBI 
planning. A case study dataset of piping systems 
were adopted for the upstream oil and gas sector. 
The benefits of the proposed method were 
evaluated by comparing it with the conventional 
method, namely manual inspection planning. 
Based on this perspective, the remaining part of 
the study was organized as follows in the 
subsequent sections. The second section focused on 
the study methodology, which comprised RBI 
method per API RP 581 and multi -objective 
optimization using non-dominated sorting genetic 
algorithm-II (NSGA-II). This was followed by the 
third section , which provided the results and 
analysis. Finally, the fourth section centered on the 
concluding aspect of the study. 
 
METHODOLOGY 
The proposed method in Figure 1 aims to 
balance optimization objectives by minimizing the 
risk of piping system failure and inspection costs 
alongside satisfying expenditure and operational 
constraints. API RP 581, the common practice 
standard for RBI, stated that risk of failure (RoF) 
model integrates probability and consequences. 
Inspection costs are calculated based on three 
components, namely related method, personnel, 
and equipment downtime expenses. The purpose 
was supported by using a multi -objective 
optimization model which integrating NSGA -II 
(Deb et al., 2002; Javid 2021). 
Risk-based inspection 
Risk-based method prioritized equipment in line 
with risk of failure. The prioritization enabled an 
organization to focus inspection efforts on high -
risk equipment. Previous studies reported that it 
prevented over -inspection of low -risk equipment 
Figure 1. The proposed multi-objective optimization model framework for RBI planning.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
396 I DOI org/10.29017/scog.v49i2.2084 
𝐷𝑓𝑤  𝑡, 𝑟𝑖 = 𝐷𝑓𝑤  𝑡, 𝑟𝑖 ∙ 𝐹𝐼𝑃 ∙ 𝐹𝐷𝐿 ∙ 𝐹𝑊𝐷 ∙ 𝐹𝑀𝐴 ∙ 𝐹𝑆𝑀𝐹𝑂𝑀    
𝑃𝑓_𝑤ℎ  𝑡  
𝐷 (𝑡)𝑓𝑤  
𝐷 (𝑡)𝑓𝑤  
𝐴𝑟𝑡𝑤  𝑡, 𝑖 =    1 − 𝑡𝑟𝑑𝑤  𝑡, 𝑖  −  𝑟𝑖 ∙ 𝑎𝑔𝑒𝑡𝑚𝑖𝑛  +  𝐶𝑎𝑙𝑙𝑜𝑤  , 0.0        
𝐷 (𝑡)𝑓𝑤  
𝑃𝑓_𝑤ℎ  𝑡  
𝐷 (𝑡)𝑓𝑤  
 Method 1 Method 2 Method 3 
Period 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 
Inspection plan 0 1 0 0 1 0 1 0 1 1 0 0 1 0 0 0 0 1 
 
𝑃𝑓_𝑤ℎ  𝑡 = 𝑔𝑓𝑓ℎ ∙ 𝐷𝑓_𝑤ℎ  𝑡 ∙ 𝐹𝑀𝑆 
(Rachman & Ratnayake 2019). Furthermore, the 
reference used in RBI determination is API RP 581 
(API RP 581 2025). In RBI, risk of failure refers to 
the result of integrating probability of failure (PoF) 
with the consequences (CoF). This section provides 
a contextual analysis of the quantitative RBI 
methodology. The processes of estimating 
probability of failure Pf(t) and the financial 
consequences (FC) were outlined to determine the 
risk level R(t) over time (t). 
The representative example of inspection 
planning is shown in Table 1, where six -time 
intervals alongside three distinct inspection methods 
were clarified. In addition, inspection method 1 was 
applied during the first and fourth periods. Methods 2 
and 3 were implemented in the second to fifth, and 
third to sixth periods, respectively. 
Probability of failure 
The probability of failure is associated with a 
specific damage mechanism, denoted as w which is 
calculated using the following Equation 1                  
        
 
where   represents a specific time frame, and ℎ 
denotes the size of the release hole. Additionally, 
four distinct values for ℎ were considered 0.25", 1", 
4", and 16", and these corresponded to small, 
medium, large, and rupture, respectively. In the 
generic failure frequency (    ℎ) for a particular 
piece of equipment and hole size, ℎ was derived 
from a representative failure database. The 
equation          = ∑ℎ    ℎ ·              refers to 
the damage factor and the generic failure frequency 
corresponding to a specific mechanism of failure 
( ). The management system factor that reflects 
how the facility influences the mechanical integrity 
of the plant is    . It is often assessed through a 
questionnaire that produces scores ranging from 0 
to 1000.     = 10 (-0.02 ·        + 1), where        = 
0.1     . Therefore,             is calculated for 
failure mechanism   with different hole sizes ℎ. 
The equation shows that the only aspect subject to 
change over time is                , which functions as a 
time-dependent variable, while the factors    ℎ 
and     remain constant. This study focused on 
failure mechanism of piping systems due to 
corrosion, both internal (w1) and external (w2).  
Calculation of the damage factor  
            is the damage factor derived from data 
gathered during prior inspection. The outcomes 
showed that corrosion rates (r) have inherent 
uncertainties, which directly affected the 
calculations of         and         . Therefore, 
increasing the confidence level when determining 
corrosion rates depended on the effectiveness of 
inspection methods. 
The metal loss parameter, Art, is the duration of 
the last inspection (age) and the corrosion rate, 
which is calculated as Equation 2 
 
 
where trd represents the thickness reading, tmin 
denotes the minimum required wall thickness, and 
Callow depicts the corrosion allowance. 
The damage factor, was determined by 
considering Art, alongside the quantity and 
effectiveness of prior inspection. Subsequently, it 
was adjusted using Equation 3, with FOM, F IP, F DL, 
FWD, FMA, and FSM as adjustment factors. 
 
 
Ineffective inspection methods led to a 
distinction, and the actual corrosion rate (r) became 
uncertain, potentially deviating from the calculated 
value. The effectiveness of an inspection method 
was measured as probability that its values 
Table 1. Typical inspection plan  
(1)  (2)  
(3)

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 397 
𝑃 𝑡 =  𝑃𝑓−𝑤ℎ  𝑡 
𝑤
𝑤=1
−  𝑃𝑓−𝑤ℎ  𝑡 
𝑤
𝑤=1
                           
𝑃𝑓−𝑤ℎ  𝑡 =  𝑃𝑓−𝑤ℎ  𝑡 
𝐼
ℎ=1
                                                   
 Inspection 
effectiveness 
description 
The inspection 
effectiveness 
levels 
Description 
 
 Highly Effective  A Inspection methods are expected to accurately show 
the extent of damage in every situation, with a 
confidence level of 80% to 100%. 
 
 Usually Effective B The inspection methods should accurately determine 
the actual damage condition most of the time, with a 
confidence level ranging from 60% to 80%. 
 
 Fairly Effective C The inspection methods should accurately determine 
the actual damage condition approximately half of the 
time, with a confidence level between 40% and 60%. 
 
 Poorly Effective D The inspection methods should offer limited 
information for accurately determining the actual 
damage condition, with a confidence level of 20% to 
40%. 
 
 Ineffective E The inspection methods should provide minimal to no 
information for accurately determining the actual 
damage condition, as well as considered ineffective 
for detecting the specific damage mechanism, with 
less than 20% confidence. 
 
 
𝑃𝑓_𝑤ℎ  𝑡  
𝑃𝑓_𝑤ℎ  𝑡 =  𝑃𝑓_𝑤ℎ  𝑡, 𝑟𝑖 
𝐼
𝑖=1
∙ 𝜋𝑡 𝑟𝑖|𝑟 , 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒,     
𝑃𝑓_𝑤ℎ  𝑡 =  𝑃𝑓_𝑤ℎ  𝑡, 𝑟𝑖 
𝐼
𝑖=1
∙ 𝜋𝑡 𝑟𝑖 , 𝑓𝑜𝑟 𝑡 = 0,              
𝑃𝑓_𝑤ℎ  𝑡  
𝐷 (𝑡)𝑓𝑤  
𝐷 (𝑡)𝑓𝑤  
accurately reflected piping actual corrosion 
condition. The more effective the inspection 
results, the higher the likelihood of matches 
between predicted and actual corrosion rates. This 
method effectively minimized the uncertainty 
related to the corrosion rate, as well as subsequent 
uncertainties in            and            . The damage 
factor    ( ,    varied following the values of 
the diverse types, namely 1 (r 1 = r), 2 (r 2 = 2r), 
and 3  (r 3 = 4r). Equation 5 was used to calculate 
the value of considering the variation of 
estimated hole sizes (h) . 
 
 
 
 
 
where t > 0, Equation 4 was used to update the 
confidence in failure state rate.             changes 
over time were reflected in the effectiveness of 
the  inspection during each period. Probability 
of failure associated with failure mechanism w is 
equivalent to the total sum. This corresponded 
with the various hole sizes and was calculated 
using Equation 6.   
 
  
The total probability of failure at period t was 
computed using Equation 7. The calculation was 
repeated twice, for each failure mechanism, namely 
internal and external corrosion. 
 
 
Table 2 shows the classification of effectiveness 
inspection into five distinct levels, with A and E 
representing the highest and lowest degree of 
effectiveness, respectively. Therefore, greater 
accuracy and effectiveness in terms of detecting 
the corrosion mechanism "w" were associated 
with more expensive inspection methods. These 
increased probability of detection as well as 
improved the accuracy of predicting the 
corrosion rate . 
Consequence of failure 
Financial terms (FC) represent the 
consequences of failure. This procedure outlines 
the steps for analyzing the consequences of 
equipment operating at constant pressure. 
According to API RP 581, the consequence of 
(4)  
(5)  
Table 2. Inspection effectiveness levels (API RP 581 2025). 
(6)  
(7)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
398 I DOI org/10.29017/scog.v49i2.2084 
𝑀𝑖𝑛𝑃𝑓 𝑥 =  𝑝𝑓 𝑡 
𝑚
𝑡=1
                                                 
𝑣𝑜𝑙𝑒𝑛𝑣  ℎ  
𝐹𝐶𝑒𝑛𝑣𝑖𝑟𝑜𝑛 =    𝑔𝑓𝑓ℎ4ℎ=1 ∙  𝑣𝑜𝑙𝑒𝑛𝑣  ℎ  𝑔𝑓𝑓𝑡𝑜𝑡𝑎𝑙  ∙ envcost 
𝐹𝐶𝑖𝑛𝑗 = 𝐶𝐴𝑖𝑛𝑗 ∙ popdense ∙ injcost 
𝐹𝐶𝑝𝑟𝑜𝑑 = 𝑂𝑢𝑡𝑎𝑔𝑒𝑐𝑚𝑑 ∙ 𝑂𝑢𝑡𝑎𝑔𝑒𝑎𝑓𝑓𝑎 ∙ prodcost 
𝐹𝐶𝑎𝑓𝑓𝑎 = 𝐶𝐴𝑐𝑚𝑑 ∙ 𝑒𝑞𝑢𝑖𝑝𝑐𝑜𝑠𝑡 
𝐹𝐶𝑐𝑚𝑑 =    𝑔𝑓𝑓ℎ4ℎ=1 ∙ ℎ𝑜𝑙𝑒𝑐𝑜𝑠𝑡ℎ𝑔𝑓𝑓𝑡𝑜𝑡𝑎𝑙  ∙ matcost       
FC = FCcmd + FCaffa + FCprod + FCinj + FCenviron 
failure is kept constant over time. It is calculated 
using Equation 8 by summing up overall costs. 
 
 
Level 1 consequence analysis mainly focuses on 
assessing the impact of releasing hazardous liquids 
by evaluating hole size (h) and overall costs. API 
RP 581 classified these costs by considering the 
cost for performing repair and replacement ( FCcmd) 
for damaged piping systems. In addition, this cost 
is calculated using Equation 9 
 
 
 
where holecosth is the cost of equipment repair 
related to steel price. Other materials used matcost 
as a cost factor to update FCcmd. In the event of a 
fire explosion, the cost of failure to adjacent piping 
systems in the affected areas ( FCaffa) was also 
computed using Equation 10 
 
 
where CAcmd denotes the total consequence area 
(m2), and the cost of replacing the process unit per 
square meter ($/m2) represents the equipcost. When 
assessing the costs of repairing or replacing 
damaged piping systems, it is crucial to factor in 
both operational downtime and resulting 
production losses. The costs associated with the 
calculations covered damaged piping systems and 
all equipment affected in the area, starting from the 
time of failure for each piece of equipment. The 
calculation costs are stated using Equation 11 
 
 
where           = (∑ ℎ    ℎ·      ℎ /           
·           is the weighted duration to restore 
piping systems during the investigation (measured 
in days).       ℎ refers to the number of days 
required to repair damages associated with the 
release hole size ℎ. The increase factor of the 
equipment hole size was denoted as           . 
The duration (days) required to repair equipment in 
(8)  
the affected area is           . Additionally, 
         represented the daily production loss 
cost incurred during therepair process ($/day). 
Equation 12 was used to calculate the cost 
associated with hidden personnel and 
community impacts.     
 
    
where CAinj represents the people impact area (m 2), 
popdens is the people or workforce density per 
square meter (people/m 2), and injcost depicts the 
cost related to serious injuries or people fatalities 
($). The cost of environmental cleanup is 
calculated using Equation 13 
 
 
 
where envcost refers to the cost of environmental 
cleanup and              is the leak rate during cleanup 
for each of the four distinct hole sizes. 
The purpose of this study is to develop an 
efficient inspection planning framework. RBI 
method is prominent for its multi -objective 
nature and does not inherently necessitate the 
calculation of FC. According to API RP 581, FC 
remains constant over time, and probability of 
failure is updated only by recalculation of failure 
factor at interval t. This feature of RBI method 
greatly reduced the computational effort 
required to formulate an inspection plan in a 
multi-objective framework.   
Problem statement and formulation 
Problem of multi -objective optimization 
included selecting efficient inspection programs   
that balanced between   (   and  (  , was 
formally described as follows (Javid 2025) 
 
 
Equation 14 was designed to minimize the 
overall risk level, specifically by reducing the 
total probability of failure. Additionally, the 
essence was to establish the most efficient 
inspection plans (Javid 2025) . 
(9)  
(10)  
(11)  
(12)  
(13)  
(14)

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 399 
𝑀𝑖𝑛𝐶 𝑥 =   𝐶𝑗  𝑋𝑗 ,𝑡
𝑚
𝑡=1
 
𝑛
𝑗 =1
 +  𝐶𝑝,𝑗
𝑛
𝑗 =1
 𝑋𝑗 ,𝑡
𝑚
𝑡=1
      
      +  𝐶𝑑,𝑗
𝑗𝜖 𝑗 ′
 𝑋𝑗 ,𝑡
𝑚
𝑡=1
                          
𝑥1 ≻ 𝑥2 ⇔ 𝑓𝑖 𝑥1  ≤  𝑓𝑖 𝑥2 , ∀𝑖  
𝑎𝑛𝑑  𝑓𝑖 𝑥1 < 𝑓𝑖 𝑥2 , for some 𝑖,                                                     
In this equation, the total probability of failure 
during period t is denoted by , where t ∈ T = {1, 2,…, 
m} signifies the various time frames. The objective 
was to minimize the overall RBI cost, as determined 
by Equation 15. The total cost consisted of inspection 
method, personnel, and downtime costs. In this 
context, Cj depicts the cost associated with 
conducting an inspection using method type j, Cp,j 
refers to the personnel cost per inspection of type j. 
Xj,t is assigned a value of 1 if inspection method j is 
performed within time ( t), otherwise it is 0. Cd,j 
represents the cost of operational downtime per 
inspection of type j. Furthermore, j ∈ J = {1, 2,…, n 
refers to different types of inspection methods, and j 
∈ Jʹ = {1, 2,…, n} pertains to the methods of 
inspection that demand a shutdown. Multi-objective 
model established RBI program, which depended on 
the following assumptions: 
• Any inspection method is permissible. 
• Various inspection methodologies can be 
adopted at any stage. 
• Minimizing the total probability of failure is the 
main objective function. 
• Minimizing overall inspection costs is the 
subsequent objective function. 
• The inspection duration must not exceed the 
maximum permitted time. 
• A single effectiveness inspection technique can 
be used for any corrosion rate. 
• The corrosion rate associated with the 
degradation mechanism must remain below the 
permissible corrosion rate. 
Multi-objective optimization model 
In the field of multi -objective optimization, a 
solution that simultaneously supports all 
objectives, considering the often exhibited 
conflicting characteristics tends to be rare. The 
solution obtained represents a set of efficient, or 
non-dominated, outcomes that reflect trade -offs 
among the objectives. It is considered non -
dominated if the improvement of one or more 
objectives deteriorated an equivalent number of 
other objectives, as formally stated in Equation 
16 (Javid 2025).  
 
 
 
where dominatesin a minimization problem. 
However, when these conditions are not fully 
satisfied, both solutions tend to be efficient, with 
each dominating the other in certain objectives. 
These collectively formed Pareto frontier, where all 
solutions were considered equally valid. MOGA 
based on non -dominated sorting genetic algorithm 
II (NSGA-II) was proposed. The algorithm enabled 
genetic operators to generate only feasible 
inspection intervals, which led to the reduction of 
the search space, thereby avoiding the exploration 
of infeasible regions. It also minimized 
unnecessary fitness evaluations, as well as 
eliminated the need for penalty functions. 
Initial population generation 
The process of initial population generation was 
described using a sample case. The representation 
of the initial solution shows a sequence of binary 
numbers corresponding to the decision variables. 
The maximum intervals for a scenario across 6 
periods using 3 inspection methods, are t 1, max = 3; 
t2, max = 5; and t 3, max = 7. Therefore, if an 
equipment is inspected using method 1 during the 
second period, the next inspection using the same 
method must be conducted within < 3 periods. 
Crossover operator 
Segments of chromosomes from the current 
generation were swapped to generate new offspring 
during the crossover process. In addition, this study 
used two-point and uniform crossover method. The 
two-point crossover, with a given chromosome 
vector (e.g., 1 × 6 for one inspection method over 
six periods), led to the selection of 2 parents and 
random points along the chromosome. The genes 
between these points were then swapped to 
generate offspring. All chromosome positions were 
considered in uniform crossover, with a randomly 
generated binary mask used to determine which 
parent contributed a specific gene to the first child. 
Meanwhile, the second child was determined by 
reversing the mask assignment. Considering that 
(16)  
(15)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
400 I DOI org/10.29017/scog.v49i2.2084 
uniform crossover increases population diversity, it 
does not preserve the memory of each chromosome 
as effectively as a two -point crossover . Figure 2 
shows the case of a single -point intersection 
function applied to the variable X chromosome.  
The two -point crossover method entailed the 
selection of two random points, with the gene values 
exchanged between the parent chromosomes, rather 
than the preference for a single random point. Figure 
3 shows the application of a two-point crossover on a 
variable X chromosome. 
Mutation operator 
The mutation operator introduced random 
chromosomal changes, including genes absent from 
the original population. This study initially applied 
a comprehensive mutation, namely a random 
number between 0 and 1 was generated for each 
gene. If the random number is less than 0.1, then 
the gene is inverted (1 becomes 0, and                
0 becomes 1).   
The mutation enhanced diversity, as shown in 
Figure 4. Additional innovative mutations were 
further applied to improve the efficiency of the 
metaheuristic algorithm and quicken convergence 
toward Pareto -optimal solutions. This was shown 
using a sample chromosome of dimensions 6 × 3 
(six time periods and three inspection methods). 
The selection of a particular solution from 
Pareto set for practical application generally 
depended on the strategic preferences and priorities 
of the decision -maker or stakeholders (Omar & 
Moselhi, 2026. The process was supported by 
 
 
Figure 2. An representation of a single-point intersection function on a variable X chromosome. 
Figure 3. An representation of a two-point crossover operation on a variable X chromosome.

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 401 
 
adopting various strategies, either individually or 
by combining it, such as: 
• Simple preference -based methods: Decision -
makers determined weights or priorities to 
define an objective. This was actualized by 
referring to criteria including acceptable risk 
and budget constraints, as well as selecting 
Pareto solution that best reflected the 
preferences. 
• Multi-criterion decision-making methods: AHP, 
TOPSIS, and weighted sum ranked Pareto 
solutions by combining several objectives into a 
single weighted score to identify the best option.  
• Clustering-based methods: Pareto solutions 
were grouped into categories, enabling 
stakeholders to select a cluster and a 
representative solution that best fits respective 
priorities.  
• Trade-off-based (compromise) solution 
methods: This included knee -point and utopia -
point methods, which assisted in the selection of 
balanced Pareto solutions. The process was 
carried out by identifying trade-offs or selecting 
the option closest to an ideal (elbow) method 
that identified Pareto solution. Additionally, a 
slight improvement in an objective led to a large 
change in the other (Huang, 2020; Tang et al., 
2023; Zhang et al., 2021. Another method is the 
selection of the closest solution to the ideal 
scenario (minimum total cost and PoF), also 
known as utopia (ideal) point method (Niu & Li, 
2025; Omar & Moselhi, 2026; Szparaga et al., 
2019. In this context, utopia method was used to 
determine efficient solutions.  
Case study and model implementation 
The proposed method was applied using real 
data from oil and gas piping systems. This 
equipment is critical for processing hydrocarbons 
while ensuring operational continuity and 
managing fluctuating demand. Piping systems were 
selected as the main case study because of the 
extensive network, high exposure to degradation 
mechanisms, and significant influence on overall 
plant reliability. When compared to other static 
equipment, the pipes showed a higher failure rate 
and were more prone to leaks and ruptures, leading 
to unplanned shutdowns, safety hazards, and 
substantial economic losses. A higher failure rate 
was also observed, because the pipes were prone to 
leaks and ruptures. This led to unplanned 
shutdowns, safety hazards, and substantial 
economic losses. Furthermore, due to the scale and 
high failure frequency, piping systems posed 
complex inspection challenges, offering an ideal 
case study for RBI optimization. Piping 
information data is shown in Table 3. The proposed 
NSGA-II method was further applied to generate 
non-dominated inspection programs. 
Inspection was planned for a 20 -year time 
horizon, using 3 common methods, namely 
ultrasonic thickness measurement (UTM), guided 
wave testing (GWT), and hydrostatic testing (HT). 
These methods varied in respective effectiveness at 
identifying internal and external flaws.  
Tables 4 and 5 show supplementary data 
gathered from the facilities, such as initial and 
minimum thicknesses, corrosion rates for internal 
and external surfaces, alongside inspection 
Figure 4. An representation of a mutation function on a variable X chromosome.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
402 I DOI org/10.29017/scog.v49i2.2084 
 Parameters Value  
 r 0.1 mmpy  
 trd 5 mm  
 tmin 4.17 mm  
 FMA = FOM = FIP=FSM=FMS = FDL = 
FWD 1  
 gff 0.0000306  
 Callow 1 mm  
 
 Method Cj Cp,j Cd,j tj,max Inspection effectiveness 
in detecting internal 
corrosion 
Inspection effectiveness 
in detecting external 
corrosion 
 
 j = 1 (UTM) 1,000 300 0 3 C C  
 j = 2 (GWT) 5,000 500 0 5 B B  
 j = 3 (HT) 10,000 1,000 10,000 15 A A  
 
 Parameter Data  
 Diameter (inch) 24  
 Nominal thickness (mm) 6.35  
 Segment length (m) 500  
 Service life (years) 26  
 Operating pressure (psig) 260  
 Operating temperature (°F) 200  
 Service fluid Crude oil   
 Construction material CS API 5L B PSL 2  
 Piping condition Aboveground  
 
Table 3. Piping information data. 
Table 4. The parameter of the case study. 
Table 5. Supporting parameters to solve the case study. 
frequency. This also included the effectiveness of 
different inspection methods in detecting defects, 
associated costs, reducing factors, as well as 
personnel and equipment downtime. Further details 
required to complete the model, including the 
general failure factor and metal loss rate, were also 
provided in accordance with API RP 581. 
The period, quantity of inspection methods, 
frequency, types of damages encountered, sizes of 
holes, and, most significantly, aggregate of prior 
inspection alongside respective effectiveness, are 
shown in Table 6 All sourced data were collected 
from oil and gas piping systems operating at a 
gathering station of an upstream processing 
facility. The critical factors in NSGA -II that 
influence problem -solving mechanism should be 
properly configured. Furthermore, the main 
variables that influenced problem -solving 
process included : 
• Maximum iterations: The proper setting of the 
maximum iteration parameter is essential for 
reducing the time required to solve the problem

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 403 
 Period 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  
 j = 1 (UTM) 0 0 1 0 0 1 0 0 1 0 0 1 0 1 0 0 1 0 0 0  
 j = 2 (GWT) 0 0 0 1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0  
 j = 3 (HT) 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
 
 Period 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20  
 j = 1 (UTM) 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0  
 j = 2 (GWT) 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1  
 j = 3 (HT) 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0  
 
 Variables Value  
 Inspection period 20  
 Inspection method 3  
 Hole size 4  
 Damage mechanism 2  
 Total of prior inspection and 
effectiveness of internal corrosion (w1)  1D  
 Total of prior inspection and 
effectiveness of external corrosion (w2) 1D  
 
 Parameter Optimum value  
 Initial population Npop 250  
 Maximum iteration Maxit 100  
 Mutation rate Pm 0.08  
 Crossover rate Pc 0.9  
 
Table 6. The size of the case study. 
as well as obtaining nearly optimal solutions . 
• Initial population: The accurate determination of 
its size is crucial in terms of achieving a diverse, 
representative set of solutions, ensuring that all 
potential solutions are addressed. 
• Mutation and crossover rate: These parameters 
influenced the algorithm balance between 
exploration and exploitation. If the values are 
not set correctly, the algorithm may lose the 
historical memory. 
The parameter used to address the case study 
problem is shown in Table 7. Furthermore, the 
optimal parameter was developed through a 
combination of experiences, including trial-and-error. 
RESULT AND DISCUSSION 
Based on this context, tables 8 and 9 focused on 
comparing the initial and effective solutions. Table 
8 specifically shows that the inspection process 
carried out with the UTM method must be 
conducted in the period 3 -6-9-12-15-18. GWT and 
HT methods must also be conducted in the periods 
5-10-15-20, and 15, respectively. The initial 
inspection program was determined based on the 
maximum time required for each method. 
Meanwhile, the results of the optimal inspection 
planning from NSGA -II simulation are shown in 
Table 9. This implied that the inspection process 
carried out with UTM, GWT, and HT must be 
Table 7. Parameters of NSGA-II algorithm. 
Table 8. Inspection methods over the time period used in the initial plan. 
Table 9. Inspection methods over time result in an efficient plan generated using NSGA-II.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
404 I DOI org/10.29017/scog.v49i2.2084 
  Initial solution Efficient solution   
 Total inspection cost (first 
objective function) 
50,800 50,800  
 Total probability of failure 
(second objective function) 
1.631 10-1 0.8975 10-1  
 
 
conducted in the periods 2 -5-8-11-14-17, 2 -7-11-
16, and 7, respectively. The results met the 
established limitation rule because the inspection 
interval for each method remained in the maximum 
inspection interval.  
Pareto-optimal solutions obtained from NSGA -
II algorithm were further analyzed to enhance 
understanding of respective behavioral characteristics. In 
this context, Pareto front of multi-objective optimization 
problem comprised a set of non-dominated solutions. 
Each represented distinct trade -offs between 
minimizing probability of piping system failure and 
reducing total inspection costs, which included both 
direct and indirect expenses. 
Figure 5 shows the convergence of NSGA -II 
algorithm for the case study across 250 
generations. The convergence of the algorithm was 
developed by a normalized hypervolume indicator 
(Beume et al., 2007; Kuo et al., 2023. In addition, 
the algorithm converged after 62 generations, 
showing its ability to minimize probability of 
failure and the total inspection cost across diverse 
probabilities, namely mutation rates. 
The objective function values derived from both 
the initial and efficient solutions are shown in 
Table 10. The efficient solution was determined 
using utopia method, as shown in Figure 6. 
Based on the results, the efficient solution was 
also analyzed using the same inspection cost. 
This was achieved by combining inspection 
methods during the final period with different 
related effectiveness, thereby significantly 
reducing probability of failure . 
Figure 5. Convergence of NSGA-II algorithm for the case study. 
Table 10. The comparison of the solutions results derived from addressing the case study.

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 405 
 
The service life of piping systems can be 
extended by improving the accuracy of corrosion 
rate estimation using data collected across multiple 
inspection periods. The method helped reduce the 
uncertainty associated with corrosion rate 
predictions, making it more reliable and predictable 
over time. Considering that the corrosion rate is the 
main source of uncertainty in integrity assessments, 
improving its accuracy is critical to extending asset 
life. In addition, more precise and reliable 
inspection methods are required to effectively 
detect equipment flaws, particularly in piping 
systems, where early identification of defects is 
essential for maintaining structural integrity and 
ensuring safe operation. 
This present study has practical implications for 
asset integrity management. This was observed by 
enabling the integration of NSGA -II-generated 
dynamic inspection schedules into existing 
maintenance systems, such as CMMS and RBI 
platforms. Optimized inspection intervals and 
priorities can be directly translated into work 
orders and inspection plans. Meanwhile, multi -
objective outputs (risk –cost trade -offs) supported 
informed decision -making under operational 
constraints. The framework also served as a 
decision-support module, which continuously 
refined the schedule. The updated inspection data 
received, further enabled adaptive, risk -informed 
maintenance planning. 
The results of this study may have inherent 
limitations that require further investigation. 
Although the effectiveness of each NDE method 
has been evaluated, uncertainties arising from data 
inaccuracies in corrosion rate estimation, 
particularly in relation to inspection tools and 
operator performance, have not been explicitly 
integrated into the model. Another limitation 
centered on the estimation of probability of failure, 
which was strongly governed by the corrosion rate. 
Furthermore, this was determined using a 
deterministic method. The model could be further 
improved by adopting a less conservative and more 
realistic method to estimating corrosion rates. For 
example, the integration of multiple inputs to 
identify potential corrosion mechanisms, including 
fluid characteristics (Effendi et al., 2020; Noegroho 
Hadi 2023; Permana et al., 2025). 
Figure 6. Selection of the optimal solution from Pareto front using utopia point method.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
406 I DOI org/10.29017/scog.v49i2.2084 
Term & 
Symbol Definition Unit 
AHP Analytical Hierarchy 
Process 
 
API American Petroleum 
Institute 
 
Callow Corrosion Allowance mmpy 
CMMS Computerized 
Maintenance 
Management Systems 
 
CoF Consequence of Failure  
Df Damage Factor  
FC Financial Consequence  
FMS Management System 
Factor 
 
gff Generic Failure 
Frequency 
 
GWT Guided Wave Testing  
HT Hydrostatic Testing  
MOGA Multi-objective Genetic 
Algorithm 
 
NSGA-II Non-dominated sorting 
genetic algorithm-II  
 
 
PoF Probability of Failure  
tmin Minimum required wall 
thickness 
mm 
TOPSIS Technique for Order of  
   
   
 
CONCLUSION 
In conclusion, this study focused on 
inspection methods of piping systems that 
balanced risk reduction and cost optimization. 
The method enabled effective inspection that 
accounted for acceptable risk thresholds and 
budget constraints. It examined different 
methods used to identify the safest and most cost
-effective options. Optimized solution reduced 
the total probability of failure from 1.631 10 -1 to 
0.8975 10 -1 while maintaining the same total 
inspection cost of 50,800, showing a substantial 
improvement in reliability without additional 
economic burden.   
The results showed that reasonable spending 
produced an extremely low risk profile and 
avoided unnecessary costs. The framework 
allowed for customized inspection plans across 
real-world applications. Moreover, probability of 
failure and overall costs served as optimization 
objectives, which relieved users of the need to 
determine the maximum acceptable risk or 
perform complex calculations.  
This study also included ingenious mutations 
to improve algorithm performance and find 
faster solutions. The method has been proven to 
solve practical challenges in oil and gas sector, 
showing its effectiveness. Further studies need to 
incorporate additional optimization algorithms 
such as NSGA -III and MOPSO. Uncertainties 
arising from data inaccuracies must also be 
systematically incorporated to improve the 
robustness and reliability of the model. The 
proposed model could be enhanced by 
integrating artificial intelligence to handle 
complex data, thereby achieving faster and better 
performance, considering that the objective 
function is data driven.   
 
DECLARATIONS 
Author contribution 
Tri Wahono: Writing - original draft, 
Conceptualization, Methodology, Visualization. 
Imam Mukhlash: Writing - review & editing, 
Methodology, Supervision. Endah R.M. Putri: 
Writing - Review & Editing, Methodology, 
Supervision. Agung Purniawan: Writing - Review 
& Editing, Methodology, Supervision. 
Funding statement  
None. 
Competing interest  
The authors declare no known competing 
financial interests or personal relationships that 
could have influenced the work reported in this 
study. 
 The use of AI or AI-assisted technologies  
None. 
 
GLOSSARY OF TERMS AND SYMBOLS

Multi-Objective Optimization of Risk-Based Inspection Planning                                                                                              
for Oil and Gas Piping Systems Using NSGA-II Algorithm (Putri et al.) 
 
DOI org/10.29017/scog.v49i2.2084 I 407 
 Preference by Similarity 
to Ideal Solution 
 
trd Thickness reading mm 
UTM Ultrasonic Thickness 
Measurement 
 
 
REFERENCES 
Abubakirov, R., Yang, M., et al., (2020), A risk -
based approach to determination of optimal 
inspection intervals for buried oil pipelines. 
Process Safety and Environmental Protection, 
134, 95 –107. https://doi.org/10.1016/
j.psep.2019.11.031 
Aditiyawarman, T., Kaban, A. P. S., et al., (2023), 
A Recent Review of Risk -Based Inspection 
Development to Support Service Excellence in 
the Oil and Gas Industry: An Artificial 
Intelligence Perspective. ASCE -ASME Journal 
of Risk and Uncertainty in Engineering 
Systems, Part B: Mechanical Engineering, 9(1). 
https://doi.org/10.1115/1.4054558 
API RP 580. (2023). Elements of a Risk -Based 
Inspection Program. In API (Fourth Ed., Issue 
August). American Petroleum Institute. 
API RP 581, (2025), Risk -Based Inspection 
Technology. January. 
Asyik, N., Latief, R. U., et al., (2026), Testing 
Center for Oil and Gas Risk - Informed 
Strategic Governance in Precast Concrete 
Production as A High - Risk Industry : Cross - 
Sector Evidence from The Construction and Oil 
& Gas Industries. Scientific Contributions Oil 
and Gas , 49(1), 459 –474. https://
doi.org/10.29017/scog.v49i1.1956 
Beume, N., Naujoks, B., et al., (2007), SMS -
EMOA: Multi -objective selection based on 
dominated hypervolume. European Journal of 
Operational Research, 181(3), 1653–1669. 
https://doi.org/10.1016/j.ejor.2006.08.008 
Campari, A., Vianello, C., et al., (2024), Machine 
learning-aided risk-based inspection strategy for 
hydrogen technologies. Process Safety and 
Environmental Protection, 191(PA), 1239–1253. 
https://doi.org/10.1016/j.psep.2024.09.031 
Deb, K., Pratap, A., et al., (2002), A fast and elitist 
multi-objective genetic algorithm: NSGA -II. 
IEEE Transactions on Evolutionary 
Computation, 6(2), 182–197. https://
doi.org/10.1109/4235.996017 
Effendi, D., Hani, B., et al., (2020), Determination 
of Water Characteristics at Gathering Station oil 
Field Y According to Minister of Environment 
Regulation No . 19 Year 2010. Lembaran 
Publikasi Minyak Dan Gas Bumi , 54(2), 111 –
125. 
Huang, W. L. Z. Z. S., (2020), Knee Point ‐Guided 
Multi-objective Optimization Algorithm for 
Microgrid Dynamic Energy Management.pdf. 
Wiley. 
Javid, Y., (2021), A bi -objective mathematical 
model to determine risk -based inspection 
programs. Process Safety and Environmental 
Protectionpro, 11(1), 893–904. https://
doi.org/10.1016/j.psep.2020.12.022 
Javid, Y., (2025), Efficient risk -based inspection 
framework: Balancing safety and budgetary 
constraints. Reliability Engineering and System 
Safety, 253(January 2024), 110519. https://
doi.org/10.1016/j.ress.2024.110519 
Kuo, R. J., Edbert, E., et al., (2023), Applying 
NSGA-II to vehicle routing problem with 
drones considering makespan and carbon 
emission. Expert Systems with Applications, 
221(February), 119777. https://doi.org/10.1016/
j.eswa.2023.119777 
Moura, M. D. C., Lins, I. D., et al., (2015), A 
multi-objective genetic algorithm for 
determining efficient risk -based inspection 
programs. Reliability Engineering and 
System Safety, 133, 253–265. https://
doi.org/10.1016/j.ress.2014.09.018  
Niu, Y. Y., & Li, X. J., (2025), A dynamic utopia 
point updating strategy for multi -objective 
optimization. ISA Transactions, 162(April), 37–
46. https://doi.org/10.1016/j.isatra.2025.04.030 
Noegroho Hadi., (2023), Pengawasan Korosi Di 
Unit Pengolahan Minyak Mentah. Lembaran 
Publikasi Minyak Dan Gas Bumi, 18. 
Omar, A., & Moselhi, O. (2026). Multi -objective

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 393 - 408 
 
408 I DOI org/10.29017/scog.v49i2.2084 
optimization model for automated risk -based 
inspection planning for concrete bridges. 
Automation in Construction, 181(PA), 106608. 
https://doi.org/10.1016/j.autcon.2025.106608 
Permana, M. S., Soeweify, M. P., et al., (2025), 
Innovation in Inspection Planning Using the 
Corrosion Assessment Information System 
(CAIS) Analytical Tool to Prevent Stationary 
Equipment Failure in Crude Distillation Unit 
(CDU). Scientific Contributions Oil and Gas, 48
(3), 203 –214. https://doi.org/10.29017/
scog.v48i3.1848 
Rachman, A., & Ratnayake, R. M. C., (2019), 
Machine learning approach for risk -based 
inspection screening assessment. Reliability 
Engineering & System Safety, 185, 518–532. 
https://doi.org/https://doi.org/10.1016/
j.ress.2019.02.008 
Seo, J. K., Cui, Y., et al., (2015), A risk -based 
inspection planning method for corroded subsea 
pipelines. Ocean Engineering, 109, 539–552. 
https://doi.org/10.1016/j.oceaneng.2015.07.066 
Sözen, L., Yurdakul, M., et al., (2022), Risk -based 
inspection planning for internal surface 
defected oil pipelines exposed to fatigue. 
International Journal of Pressure Vessels and 
Piping, 200(August). https://doi.org/10.1016/
j.ijpvp.2022.10480 4 
Szparaga, A., Stachnik, M., et al., (2019), Multi -
objective optimization based on the utopian 
point method applied to a case study of 
osmotic dehydration of plums and its storage. 
Journal of Food Engineering, 245 (December 
2017), 104 –111. https://doi.org/10.1016/
j.jfoodeng.2018.10.014  
Tang, J., Wang, H., et al., (2023), Surrogate -
assisted multi -objective optimization via knee -
oriented Pareto front estimation. Swarm and 
Evolutionary Computation, 77(September 
2022), 101252. https://doi.org/10.1016/
j.swevo.2023.101252 
Teurupun, A., Nugroho, B. S., et al., (2024), Risk -
Based Inspection Analysis of Api 581 Pressure 
Safety Valve and Stripper Acid Gas Removal 
Unit at PT. XY. Scientific Contributions Oil and 
Gas, 47(3), 313 –325. https://doi.org/10.29017/
SCOG.47.3.1645 
Wahono, T., Purniawan, A., et al., (2025), Risk -
based asset integrity management in the oil and 
gas industry from traditional to machine 
learning approaches: A systematic review. 
Results in Engineering, 28(September), 107287. 
https://doi.org/10.1016/j.rineng.2025.107287 
Weber, M., (2006), Some Safety Aspects on the 
Design of Sparger Systems for the. Process 
Safety Progress, 25(4), 326–330. https://
doi.org/10.1002/prs 
Zhang, K., Shen, C., et al., (2021), Knee based 
multimodal multi -objective evolutionary 
algorithm for decision making. Information 
Sciences, 544, 39–55. https://doi.org/10.1016/
j.ins.2020.07.057
