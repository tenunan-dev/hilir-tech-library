---
source_id: "lemigas-scog"
title: "Process Simulation and Optimization of Green Hydrogen Production from Rubberwood Sawdust Pellets Via Gasificat"
summary: "Process simulation study of producing green hydrogen from rubberwood sawdust pellets by gasification in Indonesia."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2172"
retrieved_at: "2026-10-24T14:30:45+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "09764c99c9c9d266b26a519ced9ef9e9171fd141b766f4b997fb917feed76f3d"
collected: "manual"
---

# Process Simulation and Optimization of Green Hydrogen Production from Rubberwood Sawdust Pellets Via Gasificat

667 
 
https://doi.org/10.29017/scog.v49i3.2172 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 667 – 681 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Process Simulation and Optimization of Green Hydrogen Production from 
Rubberwood Sawdust Pellets Via Gasification 
Using Unisim Design for Oil Refining 
 
Basuki Rahmad Saleh1, Irdam Ahmad1, Herlina Juni Risma Saragih1, Agus Adriyanto1, Abdul Rozak 
Kodarif2,3, Fauzi Yusupandi2,3, Damayanti Damayanti2, Muhammad Rifqi2,3, 
Hanif Fawaz Za’im2,3, and Yazid Bindar4,5* 
 
1Universitas Pertahanan, 
Anyar Street, Sukahati, Bogor, West Java 16810, Indonesia. 
2Department of Chemical Engineering, Faculty of Technology industry, Institut Teknologi Sumatera, 
Jati Agung, South Lampung, Indonesia. 
3Process Engineering of Green and Sustainable Product Laboratory, Institut Teknologi Sumatera, 
Jati Agung, South Lampung, Indonesia. 
4Department of Chemical Engineering, Institut Teknologi Bandung 
Ganesa 10 Street, Bandung 40132, Indonesia. 
5Department of Bioenergy Engineering and Chemurgy, Institut Teknologi Bandung, 
Ganesa 10 Street, Bandung 40132, Indonesia. 
 
*Corresponding author: Yazid Bindar (ybybyb@itb.ac.id) 
Yazid Bindar: https://orcid.org/0000-0002-8075-6638 
Received:  13 March 2026; Revised: in revised form 02 July 2026; Accepted: 14 August 2026 
Available: online 30 September 2026. 
  
 
ABSTRACT - Indonesia pushes to expand renewable energy to create growing interest in low carbon hydrogen. 
Rubberwood processing generates large volumes of sawdust that are commonly pelletized for fuel, offering a locally 
available biomass feedstock for hydrogen rich gas production. This study evaluates the potential of producing green 
hydrogen from rubberwood sawdust pellets through gasification using process simulation. Feedstock properties were 
determined through proximate and ultimate analyses and implemented in a two stage simulation framework consisting 
of pyrolysis followed by gasification. The model was validated against published experimental data for steam 
gasification of wood residue, and the deviation between predicted and reference gas compositions was evaluated using 
the root mean square error. After validation, sensitivity analyses were conducted at a gasifier temperature of 700 °C 
for three gasifying agent configurations: steam only, steam with air, and steam with oxygen. Under steam -only 
operation, increasing S/B from 0 to 1.0 increased H₂ from approximately 44 to 56 mol%, while HEE increased from 
about 27 to 36% and LHV decreased from about 11.4 to 8.6 MJ/Nm³. Under steam plus air, increasing S+E/R to about 
1.0 reduced H₂ from approximately 56  mol% to near zero while CO₂ increased from about 30 to 85 mol%. Under 
steam plus oxygen, increasing O/B to 1.0 reduced H₂ from approximately 56 to 22 mol% and increased CO₂ from 
about 30 to 73 mol%. Overall, the results indicate that steam rich and oxygen  lean operation is the most favorable 
pathway for enhancing hydrogen rich gas production from rubberwood sawdust pellets and provide a simulation basis 
for selecting operating conditions to support national energy resilience. 
Keywords: hydrogen efficiency; lower heating value; cold gas efficiency; refining; sensitivity analysis.

668 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
How to cite this article: 
Basuki Rahmad Saleh, Irdam Ahmad, Herlina Juni Risma Saragih, Agus Adriyanto, Abdul Rozak Kodarif, 
Fauzi Yusupandi, Damayanti Damayanti, Muhammad Rifqi, Hanif Fawaz Za’im, and Yazid Bindar , 2026, 
Process Simulation and Optimization of Green Hydrogen Production From Rubberwood Sawdust Pellets Via 
Gasification Using Unisim Design for Oil Refining, Scientific Contributions Oil and Gas, 49 (3) pp. 667-681.  
 
 
1. Introduction 
Indonesia’s abundant renewable energy resources are widely regarded as a strategic advantage that could 
strengthen its position among global leaders in renewable energy development. In line with this potential, the 
Indonesian government has established ambi tious targets through the national energy policy, aiming to achieve an 
optimal energy mix of 23% renewable energy by 2025 and further increase it to 31% by 2050 (KESDM 2023). These 
targets require an accelerated transition away from fossil fuels, which remain a major source of CO₂ emissions, toward 
cleaner and more sustainable energy systems. In this context, hydrogen (H₂) is increasingly recognized as a promising 
renewable energy carrier due to its high energy content and its potential to support deep decarbonization.  
Currently, hydrogen is utilized in Indonesia within the industrial sector, particularly as a feedstock for fertilizer 
production. Hydrogen consumption in Indonesia presently stands at approximately 1.75 million tonnes per annum 
(IEA 2022), with utilization predominantly comprising urea production (88%), ammonia synthesis (4%), and 
petroleum refining (2%). The remaining utilization was for methanol and metal production. Refining is also a major 
global hydrogen-demand sector, where hydrogen is used in hydro processing to remove impurities and upgrade heavy 
petroleum fractions. 
Most hydrogen is still produced from fossil fuels, whereas renewable hydrogen remains a small share of total 
production (Bartoli et al., 2025; Parthasarathy & Narayanan 2014). A Biomass is attractive because it can be converted 
directly through thermochemical processes, while residues that would otherwise be discarded or burned can be 
valorized to produce hydrogen -rich gas (Lanjekar et al., 2023 ; Shen 2024). Biomass is broadly defined as organic 
material derived from plant or animal sources, which includes tree wood, pruning by -products, and waste materials 
generated from forestry activities. The rubber tree (Hevea brasiliensis) is one of the important fores try commodities 
in Indonesia, where  Indonesia is the second largest rubber producer in the world with a land area of 3.16 million 
hectares and widespread growth in Lampung Province with an area of 142,600 hectares (BPS 2024). Ministry of 
Agriculture of The Republic Indonesia has projected the growth of rubber production from 2026 to 2028 using neural 
network model as shown in Figure 2. Rubber tree wood is usually harvested when it no longer produces rubber sap. 
The processing of natural rubberwood in the furniture industry results in cutting and processing waste 
(sawdust/shavings) with percentages of 26.4% and 20.75%, respectively (Jawjit et al., 2024). When the production of 
rubber increases in the future, the large amount of waster in rubberwood processing was generated. 
Several studies showed the rubberwood pellets provide multiple benefits, including more consistent and efficient 
heat output per unit volume, reduced particulate matter emissions during combustion, and lower shipping costs thanks 
to their higher bulk density (Ali et al., 2021; Laosena et al., 2022; Saosee et al., 2020). Additionally, barkwood (BW) 
and sawdust (SD) of rubberwood has been utilized as a fuel through torrefaction process. The findings show that 
higher torrefaction temperatures and longer processing times substantially enhance the higher heating value of treated 
biomass to 17 –26 MJ/kg, which is similar to the energy content of sub -bituminous coal (Kasawapat et al., 2024) . 
Other works revealed the utilization of rubberwood pellet to produce synthesis gas via gasification (Anis & Zainal  
2013; Kaewluan & Pipatmanomai  2011). The recent work by Slatter et al. (2022)  exhibited that rubberwood pellet 
generated higher H2, carbon monoxide (CO) and LHV compared to eucalyptus wood chip through fixed bed gasifier 
with CaO as a tar removal catalyst.

669 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
 
Figure 1. 
Outlook of rubber’s productive total area, production, and productivity (Chafid, 2025). 
 
 
 Gasification represents a complex thermochemical conversion process involving the simultaneous 
occurrence of chemical transformations alongside heat and mass transport mechanisms. Process simulation of 
gasification based on experimental data provides valuable support for optimization (Mutlu & Zeng  2020). Aspen 
plus was generally used to simulate gasification process with root mean square error (RSME) ranged from 0.35% 
to 11.84% (Cao et al., 2025 ; Nemmour et al., 2022 ; Shi et al., 2025). On the other hand, an alternative software for 
gasification modelling was unisim design with more simple features and interface. A study by Paiva et al., (2021)  
showed the gasification process comprised of dryring and decomposition modelled by component splitter, then 
gasification and CO shift tailored by gibbs reactor to accommodate gasification reaction. The composition of gas 
was close to aspen plus modelling except CO 2 that had large difference about 15%. Moreover, Usmani's et al., 
(2020) work used a gasifier model consisting of pyrolysis and gasifier unit to conduct thermally integrated 
gasification . Despite the extensive use of complex simulators like Aspen Plus for biomass gasification modelling, 
there is a distinct research gap regarding the application of simpler, alternative software such as UniSim Design for 
evaluating local Indonesian biomass fe edstocks. Furthermore, comprehensive comparative analyses evaluating the 
effects of varying gasifying agents specifically steam, steam -air, and steam -oxygen configurations on the syngas 
quality derived from rubberwood sawdust pellets remain limited. To bri dge this gap, the novelty of this study lies in 
the development and validation of a simplified, two -stage process simulation framework using UniSim Design to 
model green hydrogen production from locally sourced rubberwood sawdust pellets in Lampung. By con ducting 
detailed sensitivity analyses on optimal steam and oxidant ratios, this research establishes a novel and practical basis 
for selecting operating conditions that maximize hydrogen-rich gas production to support national energy resilience. 
 
2. Methodology 
Figure 2 exhibited the methodology of this study utilizing UniSim Design R510 for plywood gasification with several 
performance evaluation. Firstly, the biomass analysis was conducted to obtain proximate and ultimate analysis. For 
validation, wood residue from Fremaux's work (2015) was put to the UniSim Design R510 for gasification modelling 
with some parameters. The RMSE was calculated to show the error between experimental data and simulation results. 
Therefore, the proximate and ultimate from plywood was put to the UniSim Design R510 to observe the variation of the 
gasifying agent such as steam, steam + O2, and steam + air. Finally, the several performance evaluations were undertaken 
based on different gasifying agent in plywood gasification modelling using UniSim Design R510. 
2023 2024 2025 2026 2027 2028
0
500
1000
1500
2000
2500
Productive Total Area (x 1000 ha)/Production (x 1000 Ton)
/Productivity (kg/ha)
Years
 Productive Total Area
 Production
 Productivity

670 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
 
Figure 2. 
Schematic workflow of the methodology for hydrogen-rich syngas production. 
 
2.1 Biomass Characterization 
The rubberwood sawdust pellet was collected from local company in Lampung, Indonesia.  Proximate and ultimate 
analyses was performed to determine its physicochemical characteristics. Proximate analysis  covered total moisture 
(ISO 18134-1:2015), ash (ISO 18122:2015), and volatile matter (ISO 18123:2015), while fixed carbon was calculated 
by difference. Moreover, ultimate analysis was performed using a CHN elemental analyzer  to determine elemental 
composition (C, H, N, S, and O) with oxygen content calculated by difference according to the Equation: O = 100 − 
(C + H + N + S + ash).  Moreover, the higher heating value (GCV) and lower heating value (LHV) of sample was 
determined by ISO 18125:2017 and ISO 1928:2020, respectively. 
2.2 Model Validation and Process Simulation 
Model development was conducted using UniSim Design R510 from Honeywell, a design suite software that 
enables the construction of both dynamic and steady-state models under variable environmental conditions. The model 
validation was referred to study by Fremaux et al., (2015) using wood residue from Aquitaine in France as a biomass 
feedstock. The proximate and ultimate analysis data of wood residue was shown in Table 1.

671 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
Table 1. 
Proximate and ultimate analysis of wood residue (Fremaux et al., 2015b) 
Ultimate analysis (wt%) Proximate analysis (wt%) 
Carbon 50.26 Ash 0.34 
Hydrogen 6.72 V olatile Matter (VM) 77.71 
Nitrogen 0.16 Fixed Carbon (FC) 16.94 
Oxygen 42.66 Moisture Content (MC) 5.01 
 
Steam gasification was carried out by the latter works and the validation was done by steam to biomass ratio (SBR) 
with range of 0.5 – 1.0 at 700oC. Model accuracy was assessed by quantifying the deviation between experimental 
observations and predicted values through the root mean square error (RMSE) by following Equation 1 with n denotes 
the number of data points for model validation. The result from UniSim was compared with Aspen Plus modelling 
investigated by Vikram et al., (2022) using same biomass feed.  
RMSE = √∑ (Expi−Simi)2𝑛𝑖=1
𝑛             (1) 
 
 
 
Figure 3. 
Process flow for hydrogen production from rubberwood sawdust pellets via gasification. 
 
The thermodynamic package of gasification simulation was Peng -Robinson (PR), similar with other works 
which used Aspen Plus (Ajorloo et al., 2025; Cao et al., 2025; De et al., 2025; Hantoko et al., 2025). The gasification 
process of rubberwood sawdust pellets consists of two stages: pyrolysis, and gasification. In pyrolysis process, 
de-volatilization and volatiles combustion are assumed to be instantaneous and adiabatic while gasification zone 
was simulated as one -dimension al tubular reactor with the flow field modelled as plug flow, so that axial mixing 
is negligible. In this process, non -conventional components are converted into conventional components such as 
carbon, carbon monoxide, hydrogen, carbon dioxide, methane, be nzene, H 2S and water. After model validation, 
the rubberwood sawdust pellets was proceed in gasifier with steam as gasifying agent. The optimal steam 
conditions produced higher H 2 will be identified using a sensitivity analysis for combined variable with oxygen 
and air to generate heat. Figure 3  exhibited the gasification model flowsheet for rubberwood sawdust pellet with 
UniSim Design R510.

672 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
2.3 Performance analysis 
In the present study, a detailed sensitivity analysis has been carried out on the influence of process parameters such 
as steam -to-biomass ratio (SBR). The optimal SBR was used for sensitivity of oxygen -to-biomass ratio and 
equivalence ratio (E/R) or air-to-biomass ratio. The observed parameters consisted of carbon char efficiency (CCE), 
lower heating value (LHV) of syngas, cold gas efficiency (CGE), gasification energy efficiency (GEE) and hydrogen 
energy efficiency (HEE) (Ranjan et al., 2024; Sandeep & Dasappa 2013). These parameters were calculated using Eq 
(2) – (6). An energy requirement for producing oxygen (O2), known as EO2, had a value of 305 kWh per ton O2 with 
95% purity while the O 2 purity of 99.5% needed an extra value to 15% (Adnan et al., 2017; Tijmensen et al., 2002). 
Meanwhile, the Esteam was the required energy for steam production calculated by enthalpy equation with 95% 
assumed efficiency of gas-fired boiler (Bless et al., 2017). 
𝐻𝑉𝑠𝑦𝑛𝑔𝑎𝑠(𝑀𝐽/𝑁𝑚3) =  10.8 × 𝑦𝐻2 +  12.6 × 𝑦𝐶𝑂 +  35.8 × 𝑦𝐶𝐻4  (2) 
 
𝐶𝐺𝐸 (%) =
𝐿𝐻𝑉𝑠𝑦𝑛𝑔𝑎𝑠×𝐹𝑙𝑜𝑤𝑟𝑎𝑡𝑒𝑠𝑦𝑛𝑔𝑎𝑠×100
𝐿𝐻𝑉𝐵𝑀×𝐹𝑒𝑒𝑑𝑟𝑎𝑡𝑒𝐵𝑀
    (3) 
 
𝐺𝐸𝐸 (%) =
𝐿𝐻𝑉𝑠𝑦𝑛𝑔𝑎𝑠×𝐹𝑙𝑜𝑤𝑟𝑎𝑡𝑒𝑠𝑦𝑛𝑔𝑎𝑠×100
 𝐿𝐻𝑉𝐵𝑀×𝐹𝑒𝑒𝑑𝑟𝑎𝑡𝑒𝐵𝑀+ 𝐸𝑠𝑡𝑒𝑎𝑚+ 𝐸𝑂2
    (4) 
 
𝐻𝐸𝐸 (%) =
𝐿𝐻𝑉𝐻2×𝐹𝑙𝑜𝑤𝑟𝑎𝑡𝑒𝐻2 ×100
 𝐿𝐻𝑉𝐵𝑀×𝐹𝑒𝑒𝑑𝑟𝑎𝑡𝑒𝐵𝑀+ 𝐸𝑠𝑡𝑒𝑎𝑚+ 𝐸𝑂2
    (5) 
 
𝐶𝐶𝐸 (%) = 12×𝐺𝑌×([𝐶𝑂]+ [𝐶𝑂2]+ [𝐶𝐻4])22.4×𝐶(%) × 100    (6) 
 
 
3. Result and discussion 
3.1 Proximate and ultimate analysis 
Proximate and ultimate tests of rubberwood sawdust pellet from local company in Lampung were conducted using 
international standards and calibrated equipment to guarantee data dependability. 
3.2 Model validation with experimental data 
Before presenting the effect of steam, oxygen and air ratio in rubberwood sawdust pellet  gasification, the 
developed model should first be validated to ensure its reliability. This validation is carried out by comparing the 
syngas composition predicted by UniSim Design with reference values reported in the literature, where 
experimental obser vations are complemented by simulation results obtained using Aspen Plus (Vikram et al., 2022). 
The detailed experimental and simulation gas compositions are presented in Figure 4. Across the investigated 
steam-to-biomass ratios, Aspen Plus consistently shows lower RMS than UniSim, indicating a closer match to the 
experimental data. The average RMS obtained is 5.8% for Aspen Plus and 11.3% for UniSim, confirming that 
Aspen Plus produ ces the best overall agreement for this case. Although UniSim yields higher deviations, its RMS 
values remain within an accep table validation range. Specifically, reference studies on gasification model 
validation reported RMS values in the range of 5.2% to 11.84%, and an RMS of approximately 10% is often 
considered indicative of high model accuracy (Nemmour et al., 2022) . Based on this  criteria, the UniSim model 
showing an average RMS close to 10% can still be regarded as reasonably accurate and sui table for predicting 
syngas composition trends in the subsequent simulation results .

673 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
Table 2. 
Proximate and ultimate analysis of rubberwood sawdust pellet 
Ultimate analysis (wt%) Proximate analysis (wt%) 
Carbon 46.3 Ash 1.6 
Hydrogen 6.13 VM 78.2 
Nitrogen  0.35 FC 15.4 
Oxygen 45.59 MC 4.8 
Sulfur 0.03   
HHV (MJ/kg)  18.30  
LHV (MJ/kg)  16.97  
 
3.3 Effect of steam to biomass ratio 
To evaluate the influence of the steam to biomass ratio (S/B) on dry syngas quality, the composition was analyzed 
at different steam flowrates an at a gasifier temperature of 700°C. The results are presented in the Figure 5. As the 
steam-to-biomass ratio increases, the dry syngas composition change noticeably CO decreases, while H₂ and CO₂ 
increase, and CH₄ slightly decreases. This behavior is consistent with the water gas shift reaction (WGS) where 
additional steam promotes CO conversion into H₂ and CO₂ (Lv et al., 2004). At higher S/B, the changes become more 
gradual, indicating diminishing gains in H₂ enrichment as the system approaches equilibrium. Consisten with the 
previous work done with (Hussain et al., 2017) that increasing S/B ratio strongly influences dry syngas compositon 
through WGS reaction especially hydrogen.  
As shown in Figure 6, LHV, CCE, CGE, GEE, and HEE was also influenced by S/B ratio where LHV decreases 
significantly when S/B increasing because the concentration of high -calorific components such as CH₄ and CO is 
reduce, which are the main contributors to syngas heating value. The CCE increasing a bit from 62.8 to 62.9% due to 
the increase of gas yield even though the composition of CH4 and CO decreased. Both CGE and GEE showed a lower 
value with increasing SBR. CGE is strongly dependent on the heating value of the produced syngas. Since LHV drops 
sharply with steam addition, CGE follows the same declining pattern. Similar with CGE, GEE depended on LHV 
syngas and Esteam when SBR raised, the Esteam also increased. In contrast, HEE increases with increasing SBR since 
water gas shift and steam reforming reaction occured more often for producing more H2. 
3.4 Effect of steam+air to biomass ratio 
To evaluate the influence of the steam + air-to-biomass ratio (S+E/R) on dry syngas quality, the optimal SBR was 
1.0 in the sensitivity analysis. Different air flowrates were applied to mointor the syngas composition at 700oC. The 
resulting dry syngas mole fractions are presented in Figure 7. 
As S+E/R increases, the dry gas shifts toward a more oxidative conditions CO decreases, while H₂ and CO₂ 
increase, and CH₄ decreases steadily. This trend indicates that additional air enhances CO conversion via oxidation 
and increasing CO2 toward WGS reaction and CO partial oxidation although the presence of steam can promote the 
WGS under oxygen lean conditions, the observed sharp reduction in H₂ at higher S+E/R suggests that hydrogen is 
increasingly consumed by oxidation. A consistent with similar observations reported in Aspen Plus simulation work 
by (Cao et al., 2024).

674 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
 
Figure 4. 
Validation of UniSim’s modelling using hardwood residue with experimental and Aspen Plus at 700 ℃

675 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
 
Figure 5. 
Dry Syngas Composition at Different S/B Ratios. 
 
 
 
 
Figure 6. 
LHV, CCE, CGE, GEE, and HEE dry syngas at different S/B ratios.

676 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
 
 
Figure 7. 
Dry syngas composition at different S+E/R ratios. 
 
The increasing of E/R reduced significantly of LHV, CGE, GEE and HEE. The LHV decreased due to more 
oxidation reaction to generate CO2, near combustion reaction. The CGE and GEE was influenced by lower LHV with 
increasing E/R. Meanwhile, the HEE also reduced shraply since H 2 was consumed by O 2 to perform oxidation 
reaction. On the other hand, the CCE increase from 0.1 to 0.2 then the trend was stagnan. This happened due to the 
oxidation reaction so that the char was converted to C-containing gas. The result for LHV, CCE, CGE, GEE and HEE 
was summarized in Figure 8. 
 
Figure 8. 
LHV, CCE, CGE, GEE, and HEE dry syngas at different S+E/R ratios.

677 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
3.5 Effect of steam+O2 to biomass ratio 
To evaluate the influence of the steam + oxygen-to-biomass ratio (S+O/B) on dry gas quality, the composition was 
analyzed at 1000 kg/h steam flowrates and at gasification temperature of 700oC. The resulting dry gas mole fractions 
are shown in Figure 9.  
 
Figure 9. 
Dry Syngas Composition at Different S+O/B Ratios. 
As S+O/B increases, the dry gas shifts toward a more oxidized. The most important change is the increase of 
CO₂ accompanied by a decrease of H₂, while CO and CH₄ also decline. This pattern indicates that adding oxygen 
strengthens oxidation reactions especially conversion of CO to CO₂ and consumption of H₂ to H₂O so the overall 
syngas quality decreases as combustible  components are progressively consumed. Steam -related reactions such as 
water gas shift may still occur, but under higher oxygen supply their positive contribution to H₂ is outweighed by 
H₂ oxidation. 
 
Figure 10. 
LHV, CCE, CGE, GEE, and HEE dry syngas at different O/B ratios.

678 
 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
Figure 10 revealed the result of LHV, CCE, CGE, GEE, and HEE dry syngas at different O/B ratios. The trend 
of O/B ratio was similar with E/R sensitivity. However, this sensitivity required E O2 as input energy for O 2 
production from air separation particularly to calculate GEE and HEE. The presence O2 or air led to more oxidative 
reaction and produced more CO2 that has no LHV. 
 
4. Conclusion 
This study demonstrates the feasibility of evaluating hydrogen-rich gas production from rubberwood sawdust 
pellets using a two -stage UniSim Design process simulation. The model validation gave an average RMSE of 
11.3% for UniSim, compared with 5.8% for Aspen Plus, so UniSim was considered suitable for screening process 
trends despite its larger deviation from the reference data. At 700 °C, steam -only operation increased H₂ from 
approximately 44 to 56 mol% as S/B increased from 0 to 1.0, while HEE increased from about 27 to 36% and 
LHV decreased from about 11.4 to 8.6 MJ/Nm³. Under steam -air operation, increasing S+E/R to around 1.0 
reduced H₂ from approximately 56 mol% to near zero and increased CO₂ from about 30 to 85 mol%. Under steam-
oxygen operation, increasing O/B to 1.0 reduced H₂ from approximately 56 to 22 mol% and increased CO₂ from 
about 30 to 73 mol%; HEE reached about 48% near O/B = 0.2 before declining. These results indicate that steam-
rich and oxygen-lean conditions are more favorable for producing hydrog en-rich gas from rubberwood sawdust 
pellets. The findings provide a process -level basis for further assessment of biomass -derived hydrogen as a 
potential contributor to national energy resilience, while experimental validation, energy-economic analysis, life-
cycle assessment, gas cleaning, and hydrogen separation remain necessary to establish practical hydrogen yield 
and system-scale impacts. 
 
5. Acknowledgement 
The authors would like to express their sincere gratitude to Indonesia Defense University for supporting this 
research. We also extend our appreciation to PT. Honeywell Indonesia for providing Unisim Design R510.. 
 
6. Declarations 
6.1 Author contributions 
Basuki Rahmad Saleh: Conceptualization, Writing – Original Draft. Irdan Ahmad: Methodology, Supervision, 
Writing – Review & Editing. Herlina Juni Risma Saragih : Investigation, Supervision. Agus Adriyanto : 
Investigation, Supervision. Abdul Rozak Kodarif : Funding Acquisition, Formal Analysis. Fauzi Yusupandi : 
Software, Validation. Damayanti Damayanti: Formal Analysis, Investigation. Muhammad Rifqi: Data Curation. 
Hanif Fawaz Za’im : Visualization. Melya Riniarti : Investigation . Yazid Bindar : Supervision, Project 
Administration, Writing – Review & Editing. 
6.2 Funding statement 
This work was funded by the Indonesia Universitas Pertahanan. 
6.3 Competing Interest 
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper. 
6.4 The use of AI or AI-assisted technologies 
During the preparation of this work the authors do not use any AI or AI assisted technologies.

679 
 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
7. Glossary of terms and symbols 
Terms and 
symbols Definition Unit 
BW Barkwood - 
CCE Carbon Char Efficiency % 
CGE Cold Gas Efficiency % 
CHN Elemental Analysis - 
E/R Equivalence Ratio - 
EO2 Oxygen Equivalence - 
FC Fixed Carbon % 
GEE Gasification Enegy Efficiency % 
HEE Hydrogen Efficiency % 
LHV Low Heating Value Mj/Nm3 
O/B Oxygen to Biomass Ratio - 
RMSE Root Mean Square Error % 
S/B Steam to Biomass Ratio - 
SBR Steam to Biomass Ratio - 
S+E/R Steam Equivalence Ratio - 
S+O/B Steam, Oxygen to Biomass Ratio - 
WGS Water gas Shift - 
 
 
8. References 
Adnan, M. A., Susanto, H., Binous, H., Muraza, O., & Hossain, M. M. (2017). Enhancement of hydrogen 
production in a modified moving bed downdraft gasifier – A thermodynamic study by including tar. 
International Journal of Hydrogen Energy , 42(16), 10971 –10985. 
https://doi.org/10.1016/j.ijhydene.2017.01.156 
Ajorloo, M., Ghodrat, M., Scott, J., & Strezov, V. (2025). Modeling and experimental validation of the Co -
gasification of plastic and biomass waste to estimate product yields. Energy, 317(January), 134718. 
https://doi.org/10.1016/j.energy.2025.134718 
Ali, L., Baloch, K. A., Palamanit, A., Raza, S. A., Laohaprapanon, S., & Techato, K. (2021). Physicochemical 
characterisation and the prospects of biofuel production from rubberwood sawdust and sewage sludge. 
Sustainability (Switzerland), 13(11), 1–16. https://doi.org/10.3390/su13115942 
Anis, S., & Zainal, Z. A. (2013). Upgrading producer gas quality from rubber wood gasification in a radio 
frequency tar thermocatalytic treatment reactor. Bioresource Technology , 150, 328 –337. 
https://doi.org/10.1016/j.biortech.2013.10.010 
Bartoli, M., Pirri, C. F., & Bocchini, S. (2025). A Comprehensive Review on Hydrogen Production from Biomass 
Gasification. Molecules, 31(1), 1–20. https://doi.org/10.3390/molecules31010099 
Bless, F., Arpagaus, C., Bertsch, S. S., & Schiffmann, J. (2017). Theoretical analysis of steam generation methods 
- Energy, CO 2 emission, and cost analysis. Energy, 129, 114 –121. 
https://doi.org/10.1016/j.energy.2017.04.088 
BPS. (2024). Luas Tanaman Perkebunan Menurut Provinsi . https://www.bps.go.id/id/statistics -
table/2/MTMxIzI=/luas-tanaman-perkebunan-menurut-provinsi--ribu-hektar-.html 
Cao, Y., Bai, Y., & Du, J. (2024). Parametric study on biomass gasification by using air, oxygen -enriched air, 
air/steam and oxygen-enriched air/steam agents: An ASPEN plus modeling. International Journal of Hydrogen 
Energy, 73(October 2023), 265–273. https://doi.org/10.1016/j.ijhydene.2024.06.037

680 
 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
Cao, Y., Bai, Y., & Du, J. (2025). Aspen plus modeling of steam O2-enriched air gasification of biomass with tar 
content evaluation: A comparative study. International Journal of Hydrogen Energy , 147(May), 149985. 
https://doi.org/10.1016/j.ijhydene.2025.06.175 
Chafid, M. (2025). Buku Outlook Komoditas Perkebunan Karet . Pusat Data dan Sistem Informasi Pertanian 
Sekretariat Jenderal Kementerian Pertanian. 
De, S., Yadav, S., Singh, D., & Sistla, Y. S. (2025). Simplified approach of modeling air gasification of biomass 
in a bubbling fluidized bed gasifier using Aspen Plus as a simulation tool. Journal of Environmental Chemical 
Engineering, 13(2), 115402. https://doi.org/10.1016/j.jece.2025.115402 
Fremaux, S., Beheshti, S. M., Ghassemi, H., & Shahsavan -Markadeh, R. (2015a). An experimental study on 
hydrogen-rich gas production via steam gasification of biomass in a research -scale fluidized bed. Energy 
Conversion and Management, 91, 427–432. https://doi.org/10.1016/j.enconman.2014.12.048 
Fremaux, S., Beheshti, S. M., Ghassemi, H., & Shahsavan -Markadeh, R. (2015b). An experimental study on 
hydrogen-rich gas production via steam gasification of biomass in a research -scale fluidized bed. Energy 
Conversion and Management, 91, 427–432. https://doi.org/10.1016/j.enconman.2014.12.048 
Halim, S. A., & Swithenbank, J. (2016). Characterisation of Malaysian wood pellets and rubberwood using slow 
pyrolysis and microwave technology. Journal of Analytical and Applied Pyrolysis , 122, 64 –75. 
https://doi.org/10.1016/j.jaap.2016.10.021 
Hantoko, D., Adnan, M. A., Dwijayanto, A., Putra, A. F. P., & Hossain, M. M. (2025). Chemical looping 
gasification of palm oil mill effluent for hydrogen production – An Aspen plus modeling. Biomass and 
Bioenergy, 203(May), 108258. https://doi.org/10.1016/j.biombioe.2025.108258 
Hussain, M., Tufa, L. D., & Yusup, S. (2017). Aspen Plus ® Simulation Studies of Steam Gasi fi cation in 
Fluidized Bed Reactor for Hydrogen Production Using Palm Kernel Shell . 628 –641. 
https://doi.org/10.1007/978-981-10-6463-0 
IEA. (2022). Global Hydrogen Review. https://www.iea.org/reports/global-hydrogen-review-2022 
Jawjit, S., Jawjit, W., Pibul, P., Wongcharee, S., & Suwannahong, K. (2024). Enhancing the sustainability of the 
sawn rubberwood industry through resource -efficient and cleaner production approaches. Journal of Cleaner 
Production, 479(December 2023), 143913. https://doi.org/10.1016/j.jclepro.2024.143913 
Kaewluan, S., & Pipatmanomai, S. (2011). Potential of synthesis gas production from rubber wood chip 
gasification in a bubbling fluidised bed gasifier. Energy Conversion and Management , 52(1), 75 –84. 
https://doi.org/10.1016/j.enconman.2010.06.044 
Kasawapat, J., Khamwichit, A., & Dechapanya, W. (2024). Waste -to-Energy Conversion of Rubberwood 
Residues for Enhanced Biomass Fuels: Process Optimization and Eco -Efficiency Evaluation. Energies, 
17(21). https://doi.org/10.3390/en17215444 
KESDM. (2023). Strategi Hidrogen Nasional. 
Lanjekar, P. R., Panwar, N. L., & Agrawal, C. (2023). A comprehensive review on hydrogen production through 
thermochemical conversion of biomass for energy security. Bioresource Technology Reports, 21(November 
2022), 101293. https://doi.org/10.1016/j.biteb.2022.101293 
Laosena, R., Palamanit, A., Leungchavanon, M., Kittijaruwattana, J., Nakason, C., Lee, S. H., & Chotikhun, A. 
(2022). Characterization of Mixed Pellets Made from Rubberwood (Hevea brasiliensis) and Refuse -Derived 
Fuel (RDF) Waste as Pellet. Materials, 15(3093), 1–11. 
Lv, P. M., Xiong, Z. H., Chang, J., Wu, C. Z., Chen, Y., & Zhu, J. X. (2004). An experimental study on biomass 
air-steam gasification in a fluidized bed. Bioresource Technology , 95(1), 95 –101. 
https://doi.org/10.1016/j.biortech.2004.02.003

681 
 
 
https://doi.org/10.29017/scog.v49i3.2172 
 
 
Bindar et al. Scientific Contributions Oil and Gas 
Mutlu, Ö. Ç., & Zeng, T. (2020). Challenges and Opportunities of Modeling Biomass Gasification in Aspen Plus: 
A Review. Chemical Engineering and Technology, 43(9), 1674–1689. https://doi.org/10.1002/ceat.202000068 
Nemmour, A., Inayat, A., Janajreh, I., & Ghenai, C. (2022). New performance correlations of municipal solid 
waste gasification for sustainable syngas fuel production. Biomass Conversion and Biorefinery, 12(10), 4271–
4289. https://doi.org/10.1007/s13399-021-02237-8 
Paiva, M., Vieira, A., Gomes, H. T., & Brito, P. (2021). Simulation of a downdraft gasifier for production of 
syngas from different biomass feedstocks. ChemEngineering, 5(2). 
https://doi.org/10.3390/chemengineering5020020 
Parthasarathy, P., & Narayanan, K. S. (2014). Hydrogen production from steam gasification of biomass: Influence 
of process parameters on hydrogen yield - A review. Renewable Energy , 66, 570 –579. 
https://doi.org/10.1016/j.renene.2013.12.025 
Ranjan, N., Kumar, S., & Mahajani, S. M. (2024). Autothermal downdraft oxy -steam co-gasification of biomass 
and plastic wastes for hydrogen -rich syngas production: An Aspen plus modelling. International Journal of 
Hydrogen Energy, 81(April), 1045–1061. https://doi.org/10.1016/j.ijhydene.2024.07.218 
Sandeep, K., & Dasappa, S. (2013). Oxy–steam gasification of biomass for hydrogen rich syngas production using 
downdraft reactor configuration. International Journal of Energy Research , 33(4), 23 –40. 
https://doi.org/10.1002/er 
Saosee, P., Sajjakulnukit, B., & Gheewala, S. H. (2020). Life cycle assessment of wood pellet production in 
Thailand. Sustainability (Switzerland), 12(17), 1–22. https://doi.org/10.3390/su12176996 
Shen, Y. (2024). Biomass pretreatment for steam gasification toward H 2-rich syngas production – An overview. 
International Journal of Hydrogen Energy , 66(January), 90 –102. 
https://doi.org/10.1016/j.ijhydene.2024.04.096 
Shi, H., Huang, Y., Qiu, Y., Zhang, J., Li, Z., Song, H., Tang, T., Xiao, Y., & Liu, H. (2025). Modelling of biomass 
gasification for fluidized bed in Aspen Plus: Using machine learning for fast pyrolysis prediction. Energy 
Conversion and Management, 332(February), 119695. https://doi.org/10.1016/j.enconman.2025.119695 
Slatter, N. L., Vichanpol, B., Natakaranakul, J., Wattanavichien, K., Suchamalawong, P., Hashimoto, K., Tsubaki, 
N., Vitidsant, T., & Charusiri, W. (2022). Syngas Production for Fischer -Tropsch Synthesis from Rubber 
Wood Pellets and Eucalyptus Wood Chips in a Pilot Horizontal Gasifier with CaO as a Tar Removal Catalyst. 
ACS Omega, 7(49), 44951–44961. https://doi.org/10.1021/acsomega.2c05178 
Tijmensen, M. J. A., Faaij, A. P. C., Hamelinck, C. N., & Van Hardeveld, M. R. M. (2002). Exploration of the 
possibilities for production of Fischer Tropsch liquids and power via biomass gasification. Biomass and 
Bioenergy, 23(2), 129–152. https://doi.org/10.1016/S0961-9534(02)00037-5 
Usmani, S., Gonzalez Quiroga, A., Vasquez Padilla, R., Palmer, G., & Lake, M. (2020). Simulation model of the 
characteristics of syngas from hardwood biomass for thermally integrated gasification using unisim design 
tool. Energy, 211, 118658. https://doi.org/10.1016/j.energy.2020.118658 
Vikram, S., Rosha, P., Kumar, S., & Mahajani, S. (2022). Thermodynamic analysis and parametric optimization 
of steam -CO2 based biomass gasification system using Aspen PLUS. Energy, 241, 122854. 
https://doi.org/10.1016/j.energy.2021.122854
