---
source_id: "lemigas-scog"
title: "Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator"
summary: "Flow assurance simulation of whether insulation limits wax deposition in a subsea carbon steel pipeline between two platforms in Field W."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2104"
retrieved_at: "2026-10-24T14:30:31+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "2d539e716bff56882b83c7c56cb3438841a978e3880cb76a2452c658f6d9ed1d"
collected: "manual"
---

# Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator

DOI org/10.29017/scog.v49i2.2104 I 609 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Investigation of Insulation Effect on Wax Deposition                                         
Using a Flow Assurance Simulator 
ABSTRACT - Wax deposition remains one of the most common and disruptive problems in oil and gas 
pipelines. To address this issue, various methods are developed for both onshore and offshore fields 
according to their field characteristics. Insulation is one of the mitigation methods that generally performs 
well, despite several implementation challenges. This study presents a wax -deposition model to assess the 
effectiveness of insulation as a mitigation method. The analyzed fluid flows from the MOON platform to 
the SELENA platform in Field W through a carbon -steel subsea pipeline. The pipeline is modeled over a 
simulated distance of approximately 0–1,900 m, with detailed wax -deposition analysis focused on the 
critical section of 0–700 m. Rubber and concrete are applied to evaluate their performance as pipeline 
insulation materials. This study uses five scenarios with two different materials. The results show that, in all 
cases, wax thickness reduction reaches 100%, while rubber insulation performs more effectively than 
concrete in reducing temperature decline and heat loss. In addition, other parameters, such as pressure, Wax 
Appearance Temperature (WAT), and flow rate, are analyzed in this study. 
Keywords: insulation, wax deposition, OLGA, rubber, concrete 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 609 - 622 
Universitas Pertamina, 
Teuku Nyak Arief Street, RT.7/RW.8, Grogol Selatan, Kebayoran Lama Subdistrict, South Jakarta City, 12220, Indonesia 
Corresponding author: Astra Agus Pramana (astraagus.p@universitaspertamina.ac.id) 
Manuscript received:  March 30th, 2026; Revised: April 13th, 2026 
Approved:  May 04th, 2026; Available online: June 15th, 2026; Published: June 23th, 2026. 
Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini 
 
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Astra Agus Pramana  and Inggrialianthari Rezkhi Trinugrahandin i, 2026, Investigation of 
Insulation Effect on Wax Deposition Using a Flow Assurance Simulator , Scientific 
Contributions Oil and Gas, 49 (2) pp. 609 - 622. DOI org/10.29017/scog.v49i2.2104.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
610 I DOI org/10.29017/scog.v49i2.2104 
INTRODUCTION 
Oil and gas demand has been increasing in 
recent years. According to Statista  data, global 
oil and gas demand reached 99.57 MBPD in 
2022 and is expected to increase to 101.89 
MBPD in 2023. In Indonesia alone, 
approximately 1.58MBPD of oil and gas was 
consumed in 2022. The increasing demand for 
oil and  gas requires higher production levels. 
Therefore, it is important to implement a  
hydrocarbon production process from the 
reservoir to the surface that is both technically 
and economically effective, known as flow 
assurance (FA). One flow assurance method to 
increase oil and gas production is to mitigate 
flowline problems in production systems, 
including hydrate formation, slugging, scaling, 
corrosion, emulsions, asphaltenes, naphthenates, 
and wax deposition (Theyab 2018) . 
Wax deposition occurs when hydrocarbon 
components crystallize into solid precipitates due 
to changes in petroleum fluid -phase behavior and 
wax-deposition mechanisms (Mansoori 2009; Yang 
et al., 2020). This phenomenon is triggered by a 
decrease in fluid temperature to or below the wax 
Appearance temperature (WAT) during 
hydrocarbon production from the reservoir to the 
surface. Wax deposition can cause formation 
damage around the wellbore, leading to reduced 
permeability and porosity, as well as changes in 
fluid rheology and composition. Several methods 
are available to overcome this problem, including 
mechanical, thermal, and chemical approaches 
(Singh et al., 2004; Sousa 2019; Theyab 2021).  
These methods include insulation, inhibition, 
thermal remediation, pigging, and others. 
Insulation (or isolation) is a method used to control 
blockage in production pipelines caused by 
deposition by maintaining the fluid temperature 
above the cloud point using suitable insulating 
materials (Theyab 2018). 
To ensure the effectiveness and efficiency of 
these methods, accurate prediction of wax content 
and appearance is required (Septiano et al., 2022; 
Tony et al., 2025). Failure in wax prediction can 
lead to unsuccessful mitigation processes. In more 
severe cases, failure to handle wax deposition may 
result in production shutdowns, plug -and-
abandonment, and site restoration (Huang et al., 
2015). As a preventive approach, OLGA software 
provides predictions of WAT, wax thickness, and 
wax appearance time (Schlumberger 2017). This 
paper discusses modelling a production pipeline 
with wax content in an oil and gas field using 
OLGA software, as well as the performance of 
different insulation materials in mitigating wax 
deposition, specifically on the SELENA –MOON 
platform system. 
Previous studies in Indonesian oil and gas 
production have focused on improving 
hydrocarbon recovery, treating waxy crude oil, and 
predicting wax deposition through various 
approaches. Tobing and Eni (2013) discussed 
production improvement through alkali–surfactant–
polymer injection at a laboratory scale, while 
Pramana and Pagpa (2023) evaluated the 
effectiveness of pour point depressant in waxy 
crude oil. In addition, Septiano et al. (2022) 
developed a machine -learning proxy model to 
predict the wax deposition rate in two-phase water–
oil flow, and Pramana et al. (2025) investigated 
alternative insulation materials for production 
pipelines through simulation. These studies 
indicate that wax mitigation and production 
optimization remain important issues. However, 
the comparative evaluation of rubber and concrete 
insulation at different thicknesses under specific 
subsea pipeline conditions remains limited.  
However, the comparative effect of insulation 
materials and thickness variations under a specific 
subsea pipeline condition remains limited. This 
study addresses this gap by using OLGA to 
evaluate rubber and concrete insulation scenarios in 
the SELENA –MOON pipeline, focusing on fluid 
temperature, heat loss, wax thickness, pressure, 
WAT, and flow rate. The novelty of this study 
lies in comparing variations in insulation 
materials and thicknesses using field -based fluid 
and pipeline data . 
 
METHODOLOGY 
The experiment was conducted to analyze the 
effect of insulation by comparing production 
pipeline conditions with and without wax 
deposition. The investigation focused on several

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 611 
wax deposition parameters, such as thickness, 
appearance time, location, and other factors 
affecting the phenomenon. 
Data 
To achieve the objective, the study used a case 
study approach based on Field W data, 
complemented by a literature review. This process 
involved data processing and analysis using 
simulation software. The field data were obtained 
from operational data, including fluid, production, 
and pipeline data, along with pipeline coordinates 
in the x - and y-directions. Field W is an offshore 
field located in Southeast Sumatra. Only 
operational data relevant to the flow assurance 
simulation were used in this study. 
Methodology 
The analysis and modelling of the obtained fluid 
were conducted using the RKS -Advanced method 
in Multiflash software, with Pressure –Volume–
Temperature (PVT) analysis applied to a two-phase 
gas–liquid system. Based on the available fluid 
data, the main modelled fluid properties included a 
water cut of 99.23%, a total mass flow rate of 
409.52 lb/s, a reported wax fraction of 53.14% in 
the fluid model input, a wax appearance 
temperature (WAT) of 106°F (41.1°C), and an 
ambient temperature of 77°F (25°C). 
The original flowline modelling without 
insulation was carried out in OLGA using a wax -
deposition case within a flow assurance model, 
which served as the base case. The simulation 
procedure was arranged into five scenarios: 
Scenario 1 was the base case without insulation; 
Scenarios 2, 3, and 4 applied rubber insulation with 
thicknesses of 0.1 in., 0.5 in., and 1.0 in., 
respectively; and Scenario 5 applied concrete 
insulation with a thickness of 0.5 in. The concrete 
case was used to compare the performance of 
rubber and concrete insulation at the same 
insulation thickness. The full pipeline model was 
simulated over approximately 0–1,900 m, while the 
detailed wax deposition analysis focused on the 
critical section of 0–700 m, where wax formation 
and changes in wax thickness were most 
significant. The investigation of wax deposition 
conditions was conducted based on model outputs, 
which showed changes in wax thickness along the 
pipeline distance and production time before and 
after insulation was applied. Error analysis was 
performed using the "output" feature of the 
OLGA program to identify errors during 
modelling and simulation . 
The observed OLGA output parameters include 
fluid temperature or mixture temperature (TM), 
Wax Appearance Temperature (WAT/WAXAP), 
wax thickness (DXWX), heat loss rate (QM), 
maximum pressure (PTMAX), and pipeline 
geometry. TM represents fluid temperature, WAT/
WAXAP indicates the wax crystallization 
temperature, DXWX refers to wax thickness, QM 
represents heat loss, PTMAX indicates maximum 
pressure, and geometry represents the pipeline 
elevation profile. 
 
RESULT AND DISCUSSION 
This section presents the OLGA simulation 
results on wax deposition behavior under the base 
case and insulation scenarios. The analysis focuses 
on temperature, heat loss, wax thickness, pressure, 
and flow rate to evaluate the effectiveness of 
insulation in mitigating wax deposition. 
Base case scenario 
Based on the obtained fluid data, the fluid was 
modeled as a two -phase mixture of gas and liquid, 
with a water cut of 99.23% and a total mass flow of 
409.52 lb/s. The fluid also contains 53.14% wax 
(paraffin) in the fluid model input. The ambient 
temperature, as one of the considerations in 
investigating the case, reaches 77°F (25°C), with a 
WAT of 106°F (41.1°C). This indicates a high 
likelihood of wax deposition as the fluid 
temperature decreases along the pipeline. Figure 1 
shows wax deposition forming as the temperature  
drops close to the WAT at a pipeline distance of 
350 m, and it continues to thicken to 0.08 inch as 
the fluid temperature passes the WAT. 
As a result of turbulence caused by the lower 
location of the pipe geometry, wax thickness 
depletion occurs again along the pipeline between 
560 m and 580 m. The wax thickens once again as 
the turbulence diminishes, the fluid flow stabilizes, 
and the fluid temperature moves closer to the

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
612 I DOI org/10.29017/scog.v49i2.2104 
 
 
 
Pipeline Distance (m) 
 
 
Pipeline Distance (m) 
Figure 1. Wax deposition forming graph along the pipe.                                                                                                            
That wax deposition begins when the fluid temperature approaches the wax appearance temperature (WAT) at 
approximately 350–400 m. Wax thickness then increases along the critical section and reaches its highest value     
around 650–700 m. 
Figure 2. The base-case parameter conditions in the 20th year before insulation is applied.  
The fluid temperature decreases along the pipeline and approaches the wax appearance temperature (WAT), which 
promotes wax formation in the critical section. Wax thickness increases around the 600–700 m section, while heat loss 
indicates thermal energy transfer from the fluid to the surroundings. Overall, the figure confirms that temperature 
decline and heat loss contribute to wax deposition in the uninsulated pipeline.

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 613 
 
 
 
Pipeline Distance (m) 
WAT; as observed at a pipeline distance of 674 m, 
it reaches 0.11 inch (2.79 mm). Figure 4 illustrates 
the general condition of the observed parameters 
for every 100 m along the pipeline. 
Insulation result analysis 
Rubber insulation 
The carbon -steel pipeline was insulated with 
rubber, which affected the thickness of the wax. 
The temperature was evaluated at a pipeline 
distance of 400 m. The simulation results show that 
the change in wax thickness was influenced by the 
reduction in heat loss rate (from 18.9 kW/m to 4.74 
kW/m) and by the increase in fluid temperature or 
the depletion of ΔT, making it less extreme than in 
the original scenario.  
The fluid temperature in the initial scenario was 
44°C, whereas it was effectively maintained at 60°
C after insulation with a rubber material. The wax 
thickness in Scenario 2 is significantly influenced 
by the insulator, reducing it from 0.1 in (2.54 mm) 
to 0 in (0 mm), or around a 100% reduction 
compared to the initial scenario. In addition, the 
peak wax thickness, which previously formed at a 
pipeline distance of 675 m, no longer exists. 
Scenario 3 represents a reduction in wax 
thickness that is as significant as in Scenario 2. 
Insulation with a thickness of 0.5 inch can handle 
wax deposition by reducing it to 0 inch (0 mm). In 
other words, this insulation causes the wax 
deposition to dissolve completely, or be 100% 
handled from the base case scenario (Figure 5). 
Due to a decrease in the temperature difference 
(ΔT) and reduced heat loss along the pipeline, the 
maximum wax thickness does not develop. This 
demonstrates that insulation with a thickness of 0.5 
inch (Scenario 3) produces better results than 0.1 
inch (Scenario 2). This important finding is 
reasonable, as each increase in rubber thickness 
results in its physical properties having a greater 
influence on changes in fluid temperature. As a 
Figure 3. Wax deposition forming graph after 0.1 inch of rubber insulation applied.  
The fluid temperature remains above the Wax Appearance Temperature (WAT) throughout the simulated distance, 
indicating that the insulation successfully reduces the temperature drop in the flowline. As a result, wax deposition does 
not form, as shown by the wax thickness remaining at 0 mm. This result indicates that 0.1-inch rubber insulation is 
already effective in preventing wax accumulation under the simulated pipeline conditions.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
614 I DOI org/10.29017/scog.v49i2.2104 
 
 
 
 
 
Pipeline Distance (m) 
 
 
 
 
Pipeline Distance (m) 
Figure 4. Condition of observed parameters after 0.1 in of rubber insulation applied.  
The graph shows that the fluid temperature is maintained above WAT, while the wax thickness remains at 0 mm along 
the pipeline. This condition indicates that the insulation reduces heat loss and prevents the fluid from reaching the 
critical temperature for wax crystallization. The pressure trend remains relatively stable, and the geometry profile does 
not cause significant changes in wax formation. Therefore, this scenario confirms that thin rubber insulation can provide 
effective thermal protection against wax deposition. 
Figure 5. Wax deposition forming graph after 0.5 inch of rubber insulation applied.  
The fluid temperature remains consistently above the Wax Appearance Temperature (WAT) along the pipeline, 
indicating that the insulation effectively maintains the thermal condition of the fluid. The wax thickness remains at 0 mm 
throughout the simulated distance, which confirms that wax formation is fully prevented in this scenario. Compared with 
the thinner insulation case, the 0.5-inch rubber insulation provides a more stable thermal margin and better protection 
against temperature decline.

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 615 
 
 
 
 
 
 
Pipeline Distance (m) 
result, the temperature drop along the pipe can be 
maintained more steadily and does not occur 
rapidly. Compared with the earlier scenarios, minor 
temperature fluctuations lead to wax dissolution 
and prevent accumulation over a longer period. 
Figure 6 displays the overall outcomes of the 
parameters observed in this scenario. 
The application of 1 in thick insulation in 
Scenario 4 shows the same result as the previous 
scenario (Scenario 3), either for the fluid 
temperature parameter or wax thickness. 
To be specific, the reduction of wax deposition 
is still totally effective (100%) as in the previous 
scenario, as well as the heat loss parameter, which 
relatively has the same result, and the dissolution 
of the wax deposition peak (Figure 7). This can be 
caused by the impact that has reached its maximum 
and is no longer visible in the resulting graph, since 
the physical characteristics of the insulator at 
decreasing temperature changes (ΔT) are no longer 
relevant. Given that installing insulation of this 
thickness would take more time and resources 
while having a roughly similar impact to the 
previous scenario, it is not advised to do so. 
Figure 8 also displays the results for all 
parameters that were observed. Regardless of the 
importance of the results presented, the condition of 
reducing T from the initial condition indicates that 
insulation was successfully installed. This result is 
also influenced by the wax thickness, which was not 
too high before insulation was applied (base -case 
scenario). Meanwhile, the PTMAX parameters did 
not show a significant change after the insulation was 
installed with rubber material, with thicknesses of 0.1 
in, 0.5 in, or 1 in. 
Concrete insulation 
The application of insulation with concrete 
material has quite a significant impact on the 
depletion of wax deposition thickness, but it is not 
as effective as rubber material in insulation. The 
research results on concrete insulation were based 
on the most effective rubber insulation thickness of 
0.5 in. As shown in the results, the fluid 
temperature decreased to 59°C from the base case 
at a pipeline distance of 400 m.  This result is 3 C 
lower than the rubber insulation case with the same 
thickness applied. It is shown on the chart that the 
temperature graph is steeper than that of Scenario 
Figure 6. Condition of observed parameters after 0.5 inch of rubber insulation applied.  
The fluid temperature remains above the wax appearance temperature (WAT), while wax thickness stays at 0 mm 
along the pipeline. The  lower heat-loss profile indicates improved thermal stability, and the pressure trend remains 
relatively stable. These results confirm that 0.5-inch rubber insulation effectively prevents wax deposition and supports 
flow assurance performance.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
616 I DOI org/10.29017/scog.v49i2.2104 
 
 
 
 
 
 
 
 
Pipeline Distance (m) 
 
 
 
 
 
 
 
Pipeline Distance (m) 
Figure 7. Wax deposition forming graph after 1 inch of rubber insulation applied.  
The fluid temperature remains above the Wax Appearance Temperature (WAT) along the entire pipeline, indicating that 
the thicker rubber insulation effectively maintains the thermal condition of the fluid. The wax thickness stays at 0 mm 
throughout the simulated distance, which confirms that wax formation is completely prevented. However, the result is 
similar to the 0.5-inch rubber insulation case, suggesting that increasing the insulation thickness to 1 inch does not 
provide a proportional improvement in wax-deposition reduction. 
Figure 8. Condition of observed parameters after 1 inch of rubber insulation applied.  
The fluid temperature remains above the Wax Appearance Temperature (WAT), while wax thickness stays at 0 mm 
along the pipeline. The heat-loss profile remains low, and the pressure trend shows no major change along the 
simulated distance. These results indicate that 1-inch rubber insulation effectively maintains the thermal condition of the 
fluid and prevents wax deposition.

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 617 
 
 
 
 
 
 
 
 
 
Pipeline Distance (m) 
3, which leads to larger ∆T. Nevertheless, no wax 
deposition was formed, and the wax deposition 
reduction is up to 100%, due to tolerable heat 
loss and ∆T. This event was mainly caused by 
the TM graph that does not reach WAT, as 
shown in Figure 9. As it was in the previous 
scenario, the other studied parameters are also 
influenced by concrete insulation. As shown in 
Figure 12, at a pipeline distance of 400, the 
PTMAX value dropped by 2.2 psig, and QM's 
value changed by ( -15.68) KW/m from the 
initial  scenario. The wax deposits that peaked in 
scenario 1 were fully resolved, as in scenarios 2 
to 4, at a pipeline distance of 500 -700 m. 
These two factors failed to deliver better outcomes 
than insulator rubber. Even though all of these 
occurrences showed that wax deposits could be 
handled, and while concrete insulation  and rubber 
both performed successfully, rubber's effectiveness 
was more clearly proved. Figure 10 and Tables 3 and 
4 provide a comparison of all parameters impacted 
following the application of insulation. 
The analysis at 400 m is a selected observation 
point used to compare the thermal and wax -
deposition responses between rubber and concrete 
insulation. This location was not a separate insulated 
section, but was selected because it shows relevant 
changes in fluid temperature, heat loss, pressure, and 
wax thickness. The 500–700 m interval represents a 
selected observation section used to evaluate changes 
in wax thickness and thermal behavior along the 
critical wax-prone section. 
Insulation effect on production 
This experiment proved that both insulation 
materials successfully prevented wax deposition 
Figure 9. Wax deposition forming graph after 0.5 inch of rubber insulation applied.  
The fluid temperature gradually decreases along the pipeline but remains above the wax appearance temperature 
(WAT). As a result, wax thickness stays at 0 mm throughout the simulated distance. This condition indicates that the 
applied insulation maintains a sufficient thermal margin to prevent wax formation along the pipeline. 
  No. MAPE percentage Classification  
 1 <10% Very Good  
 2 10% - 20% Good  
 3 20% - 50% Fair  
 4 >50% Inaccurate  
Table 1. MAPE classification (Lasifa et al., 2021).

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
618 I DOI org/10.29017/scog.v49i2.2104 
 
 
 
 
 
 
 
 
 
Pipeline Distance (m) 
 
 Parameter Rubber Insulation Concrete Insulation  
 Fluid temperature 62°C 59°C  
 Heat loss -1.12 kW/m -5.64 kW/m  
 Wax thickness 0 mm 0 mm  
 Pressure 165.6 psig 166.3 psig  
  Parameter Pipeline distance of 400 m Pipeline distance of 665 m  
 Fluid temperature 44°C 41°C  
 Heat loss -18.9 kW/m -3.3 kW/m  
 Wax thickness 0.14 mm 2.8 mm  
Table 2. Parameter values of base case scenario. 
Table 3. Parameter comparison of 0.5 in insulation effect at 400 m. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Parameter Rubber insulation Concrete insulation Unit  
 Fluid temperature 62.03 – 61.73 58.81 – 57.36 °C  
 Heat loss (-1.12) – (-1.11) (-5.5) – (-5.3) kW/m  
 Wax thickness 0 0 mm  
 Pressure 164.7–163.7 165.5–164.4 psig  
Table 4. Parameter comparison of 0.5 in insulation effect at 500-700 m. 
Figure 10. Condition of observed parameters after 0.5 inch of rubber insulation applied.  
The fluid temperature remains above the Wax Appearance Temperature (WAT), while wax thickness stays at 0 mm 
along the pipeline. The heat-loss profile remains low and stable, indicating that the insulation helps maintain the thermal 
condition of the fluid. The pressure trend also shows no major fluctuation. These results confirm that 0.5-inch rubber 
insulation prevents wax deposition under the simulated condition.

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 619 
 
 
 
 
 
 
 
 
 
 
Pipeline Distance (m) 
formation in the pipeline. This can be investigated 
by examining wax thickness and heat loss, with a 
negative correlation between the two. For instance, 
if we investigate those parameters at a pipeline 
distance of 300 m, there is a difference in the 
results for insulation using rubber for each 
thickness, as well as for concrete along the pipe 
(Figures 11 and 12). We can also see that there is 
an unusual habit around 300 m to 600 m pipeline 
distance of pipe, which can be caused by a change 
of geometry in the pipeline that affects the 
observed parameters. In addition, wax deposition 
that formed early, before the temperature graph 
reached WAT, may be due to back pressure 
along the flowline, which cannot be interpreted 
in this experiment because of the software's 
limitations.  This back -pressure phenomenon is 
considered common in deepwater pipelines. 
However, the pressure change was not 
particularly obvious. Therefore, it is necessary 
to directly observe the flow rate to determine 
whether production has increased. The oil flow 
rate in the initial scenario is 830.6 STB/D . 
This indicates that the wax deposition has not 
interfered with production from the beginning to 
the study's time period (20th year). As a result, the 
applied solution does not significantly alter the 
production process. However, it is important to 
note that this paper considered only wax 
deposition, neglecting other forms of deposition, so 
other deposition mechanisms may occur along the 
pipeline in the field. 
 
DISCUSSION 
Although 0.1 -inch rubber insulation already 
reduced the modeled wax thickness to 0 mm, the 
0.5-inch rubber insulation provides a better thermal 
margin by maintaining a higher fluid temperature 
and lower heat loss along the pipeline. Therefore, 
0.1-inch rubber insulation can be considered the 
minimum effective thickness in the simulation. In 
contrast, 0.5 -inch rubber insulation is considered 
the most suitable option because it provides 
complete reduction in wax thickness and more 
stable thermal performance. The 1 -inch rubber 
Figure 11. Wax thickness graph for each scenarios.  
The base-case condition shows wax accumulation in the critical section, with the highest wax thickness occurring 
around the 600–700 m pipeline distance. In contrast, all insulation scenarios maintain wax thickness at 0 mm along             
the pipeline. This indicates that both rubber and concrete insulation effectively prevent wax deposition under                      
the simulated conditions.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
620 I DOI org/10.29017/scog.v49i2.2104 
ψ =   𝜕𝑅𝑠
𝜕𝑝  𝑇
𝜕𝑝
𝜕𝑡 +  𝜕𝑅𝑠𝜕𝑝  𝑇 𝜕𝑝𝜕𝑧𝜕𝑧𝜕𝑡 +  𝜕𝑅𝑠𝜕𝑇  𝑝 𝜕𝑇𝜕𝑡 +  𝜕𝑅𝑠𝜕𝑇  𝑝 𝜕𝑇𝜕𝑧 𝜕𝑧𝜕𝑡  
          𝑚𝑔 +𝑚𝐿 +𝑚𝐷  
 𝜕𝑅𝑠
𝜕𝑇  𝑝 
 𝜕𝑅𝑠
𝜕𝑝  𝑇 
1
1 |1537 − 1568,15|1537
𝑛
𝑥=1
 ×  100% = 2,03% 
1
1 |98779,08 − 100149,75|98779,08
𝑛
𝑥=1
 ×  100% = 1,39% 
1
1 |768,91 − 830,61|768,91
𝑛
𝑥=1
 ×  100% = 8,02% 
Figure 12. Heat loss graph for each scenarios.  
The base-case condition shows higher heat loss along the pipeline, especially in the early section, which supports the 
decrease in fluid temperature and promotes wax deposition. After insulation is applied, the heat-loss values become 
lower and more stable. This indicates that both rubber and concrete insulation reduce thermal energy loss and help 
maintain the fluid temperature above the wax appearance temperature (WAT). 
 
 
 
 
 
 
 
 
 
 
 
Pipeline Distance (m) 
insulation produced a similar wax thickness 
response to the 0.5 -inch case; therefore,  the 
additional thickness may not provide a proportional 
improvement in the simulated results. Based on the 
input contained in the model within the OLGA 
software, where the parameters that can be input 
correlated to the flow rate are only the total flow 
rate, it is known that establishing the theoretical 
flow rate value in the software uses Equation 1 
(Bendiksen, K. H., et al., 1991). 
 
 
 
where ψ,   ,  ,  ,  ,  ,   ,   ,   ,         , and        , 
are the calculated flow term in the OLGA model, 
the solution gas ratio, the pressure, the temperature, 
the axial distance along the pipeline, the time, the 
gas mass flow rate, the liquid mass flow rate, the 
dispersed-phase mass flow rate, the change of    
with respect to pressure at constant temperature 
and teh change of    with respect to temperature at 
constant pressure, respectively. 
 
Using this approach, the simulated flow rate 
values for various phases are obtained. Matching 
the value obtained from the simulation with the 
original data is important to assess the accuracy of 
the experimental result. 
Matching is obtained using the flow rate 
parameter and the MAPE method. The actual 
field data for this parameter is 768.91 STB/D; 
the modelling findings show a flow rate 
parameter of 830.61 STB/D. Table 1 shows that 
the simulation model is classified as good or 
accurate based on its match with field data, as 
determined by the MAPE classification, as 
illustrated in the Equations 2 through 4 . 
 
 
 
 
 
 
 
 
(1)  
(2)  
(3)  
(4)

Investigation of Insulation Effect on Wax Deposition Using a Flow Assurance Simulator                                                       
(Astra Agus Pramana and Inggrialianthari Rezkhi Trinugrahandini) 
 
DOI org/10.29017/scog.v49i2.2104 I 621 
Terms & 
Symbol Definition Unit 
WAT Wax appearance temperature,  
the temperature at which wax 
begins to crystallize from 
hydrocarbon fluid 
°C 
TM Mixture temperature, the 
temperature of the fluid 
mixture flowing inside the 
pipeline 
°C 
QM Heat loss, the rate of thermal 
energy loss from the fluid to 
the surroundings along the 
pipeline 
kW/m 
DXWX Wax deposition thickness 
parameter in OLGA simulation 
representing wax layer 
formation 
mm / 
in 
Q Flow rate of produced fluid in 
the pipeline system 
STB/D
, lb/s 
WC Water cut, percentage of water 
content in produced fluid 
% 
𝛥𝑇 Temperature difference 
between fluid and 
surroundings along the 
pipeline 
°C 
𝑘 Thermal conductivity, ability 
of material to conduct heat 
W/m·
K 
𝜌 Density, mass per unit volume 
of fluid 
kg/m³ 
𝜇 Dynamic viscosity, resistance 
of fluid to flow 
cP 
𝑃 Pressure inside the pipeline 
system 
psig 
𝑃𝑇𝑀𝐴𝑋 Maximum pressure parameter 
observed along the pipeline 
psig 
𝐹𝑙𝑜𝑤  
𝐴𝑠𝑠𝑢𝑟𝑎𝑛𝑐𝑒 
Strategy to ensure continuous 
flow of hydrocarbons from 
reservoir to surface without 
blockage 
- 
 
The error value in the experiment results for 
each flow rate is considered acceptable, as it is still 
below 10%. Errors that do not reach 0% are caused 
by varying data assumptions and by random data 
collection at the applied scale. Meanwhile, 
modelling is carried out with a rough time step of 
15 minutes to 1 day over a 20-year simulation. As a 
result, some data may not be properly recorded. 
 
CONCLUSION 
     The simulation results show that insulation 
affects fluid temperature, heat loss, and wax 
thickness. Applying insulation reduces heat loss, 
maintains the fluid temperature above the wax 
appearance temperature (WAT), and reduces wax 
accumulation along the pipeline. All insulation 
scenarios, including rubber insulation with 
thicknesses of 0.1 inch, 0.5 inch, and 1 inch, as 
well as concrete insulation with a thickness of 0.5 
inch, reduced wax thickness by 100%. The 0.1-inch 
rubber insulation can be considered the minimum 
effective thickness in the simulation. In contrast, 
the 0.5 -inch rubber insulation is considered the 
most suitable option because it provides complete 
reduction in wax thickness and more stable thermal 
performance. The 1 -inch rubber insulation did 
not show a proportional improvement compared 
with the 0.5 -inch case. The application of 
insulation did not significantly affect the flow 
rate because the initial wax thickness in the base 
case was relatively small . 
 
ACKNOWLEDGEMENT 
The authors would like to express their 
sincere gratitude to Universitas Pertamina for 
the support, facilities, and resources provided 
throughout this research.  
 
DECLARATIONS 
Author contribution 
All authors contributed equally to the 
conception, research, analysis, and writing of this 
manuscript. All authors have read and approved the 
final version of the manuscript for publication. 
Funding statement 
None 
Competing interest 
The authors declare that there are no conflicts of 
interest related to this study or the publication of 
this manuscript.  
The use of AI or AI-assisted technologies 
None 
GLOSSARY OF TERMS AND SYMBOLS

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 609 - 622 
 
622 I DOI org/10.29017/scog.v49i2.2104 
𝑊𝑎𝑥  
𝐷𝑒𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛 
Formation of solid wax 
crystals due to temperature 
drop below WAT 
- 
𝐼𝑛𝑠𝑢𝑙𝑎𝑡𝑖𝑜𝑛 Method to maintain fluid 
temperature by reducing heat 
loss in pipeline 
- 
𝑂𝐿𝐺𝐴 Dynamic multiphase flow 
simulator used for pipeline 
flow assurance analysis 
- 
 
REFERENCES 
American Petroleum Institute (API), (2014), API 
RECOMMENDED PRACTICE 583 FIRST 
EDITION - Corrosion Under Insulation and 
Fireproofing. IHS Energy. 
Bauck, I. -J. T., (2013), Flow Assurance: A 
System Perspective. MEK4450 -FMC Subsea 
Technologie s. 
Bendiksen, K. H., Maines, D., Moe, R., & Nuland, 
S., (1991), The Dynamic Two -Fluid Model 
OLGA: Theory and Application. SPE 
Production Engineering, 6(02), 171–180. 
doi:10.2118/19451-pa 
Huang, Z., Zheng, S., & Fogler, H., (2015), Wax 
Deposition: Experimental Characterizations, 
Theoretical Modelling, and Field Practices. 
USA: Taylor and Francis Group. 
Lasifa, W. -A., (2021), Pencocokan Kurva 
Penderita Covid-19 Di Sumatera Barat Dengan 
Model Hampir Eksponensial. Universitas 
Andalas. 
Mansoori, G Ali., (2009), Phase Behavior in 
Petroleum Fluids. https://www.researchgate.net/
publication/237733355_PHASE_BEHAVIOR_I
N_PETROLEUM_FLUIDS/citation/download 
Pramana, A.A., et al., (2025), Introducing Cork 
as an Alternative Insulator to Polyurethane in 
Field X Production Pipelines: A Simulation 
Study Scientific Contributions Oil and Gas , 
48(3), 149 –159. https://doi.org/10.29017/
scog.v48i3.1871  
Pramana, A.A., & Pagpa, T.A., (2023), Analisis 
Keefektifan Pour Point Depressant pada 
Waxy Crude Oil pada Lapangan TAP. 
Lembaran Publikasi Minyak dan Gas Bumi  
(LPMGB), 57(1). https://doi.org/10.29017/
LPMGB.57.1.1312  
Schlumberger., (2017), OLGA User Manual. 
Septiano, J., Yasutra, A., & Rahmawati, S.D., 
(2022), Building a Machine Learning Proxy 
Model for the Prediction of Wax Deposition 
Rate in Two -Phase Flow Water -Oil Scientific 
Contributions Oil and Gas,  45(1), 27 –41. 
https://doi.org/10.29017/SCOG.45.1.922 
Singh, A., Benavides, M. S., Saint Marcoux, J. -F., 
& Barrufet, M. A., (2004), Dilution 
Strategies for Wax Management and Control 
for Deepwater Development from a Flow 
Assurance Perspective: Part I - Current 
Practice and Perspective. SPE Annual 
Technical Conference and Exhibition. 
doi:10.2118/90688 -ms 
Sousa, A. L., (2019), Preventing and removing wax 
deposition inside vertical wells. Journal of 
Petroleum Exploration and Production 
Technology. 
Tobing, E. M. L., & Eni, H., (2013), Peningkatan 
Perolehan Reservoir Minyak 'R' dengan Injeksi 
Alkali-Surfaktan-Polimer pada Skala 
Laboratorium. Lembaran Publikasi Minyak dan 
Gas Bumi, Vol. 4 7 No. 2, Agustus 2013, hlm. 
87–96. https://doi.org/10.29017/LPMGB.47.2.240  
Tony, B., et al., (2025), Transient Simulation to 
Analyze Wax Deposition and Flow Pattern 
Behavior Along Tubing Under ESP Installation 
and Gassy Well Condition. Scientific 
Contributions Oil and Gas  (LEMIGAS), 48(3). 
https://doi.org/10.29017/scog.v48i3.1731 
Theyab MA. Wax deposition process: mechanisms, 
affecting factors, and mitigation methods. Open 
Access J Sci. 2018;2(2):112–118. DOI: 
10.15406/oajs.2018.02.00054 
Theyab, M., (2021), A review of wax mitigation 
methods through hydrocarbon production, 
Journal of Petroleum Research, 11, 412. 
Yang, J., Lu, Y., Daraboina, N., & Sarica, C., 
(2020), Wax deposition mechanisms: Is the 
current description sufficient?, Fuel, 275.
