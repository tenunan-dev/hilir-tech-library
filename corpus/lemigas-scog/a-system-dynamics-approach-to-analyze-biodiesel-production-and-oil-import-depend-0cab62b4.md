---
source_id: "lemigas-scog"
title: "A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia"
summary: "Indonesian policy study combining system dynamics and Monte Carlo simulation to test how biodiesel blending and production capacity affect diesel import dependency."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2019"
retrieved_at: "2026-10-24T14:29:47+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "0cab62b4c81e4a55f6f88e3aa0238ad9210d161451af2e0a71d4c5b96672e56a"
collected: "manual"
---

# A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia

DOI org/10.29017/scog.v49i2.2019 I 335 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
A System Dynamics Approach to Analyze Biodiesel Production 
and Oil Import Dependency in Indonesia 
ABSTRACT - Indonesia’s persistent dependence on imported diesel fuel poses significant challenges to 
national energy security, fiscal stability, and exposure to global market volatility. In response, the 
government plans to implement a mandatory B50 biodiesel blending policy starting in 2026 to reduce diesel 
imports by leveraging domestic bioenergy resources. While higher blending mandates are often assumed to 
directly lower imports, existing studies largely rely on static or deterministic approaches that inadequately 
capture feedback dynamics and long -term uncertainty. This study addresses this gap by integrating system 
dynamics modelling with Monte Carlo simulation to analyze the impact of biodiesel blending policies on 
diesel import dependency under structural and parametric uncertainty. The model incorporates biodiesel 
production growth, domestic allocation after exports, diesel demand growth, and blending effectiveness 
within a feedback -based framework calibrated using historical data from 2013 to 2024. Simulation results 
indicate that the B50 policy consistently reduces diesel import requirements relative to the baseline; 
however, absolute imports may continue to rise without sufficient domestic supply expansion. Cumulative 
results show that by 2035, the B50 policy achieves import reductions of approximately 55–58 million 
kiloliters, increasing to around 60 million kiloliters when combined with accelerated biodiesel production 
growth. Monte Carlo analysis reveals robust medium -term outcomes by 2030 but increasing uncertainty by 
2035. The findings highlight that blending mandates must be accompanied by sustained supply -side 
development to ensure long-term effectiveness and resilience. 
Keywords: biodiesel blending policy, crude import dependency, system dynamics, monte carlo simulation, 
energy security 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 335 - 351 
1Department of Petroleum Engineering, Faculty of Earth and Energy Technology, Universitas Trisakti,   
Campus A, Building D, 5th Floor, Kyai Tapa Street, Grogol, Jakarta 11440, Indonesia. 
2Lazaridis School of Business and Economics, Wilfrid Laurier University ,75 University Avenue West,  
Waterloo, Ontario, N2L 3C5, Canada. 
3Mining Engineering Department, Faculty of Earth and Energy Technology, Universitas Trisakti, 
Campus A, Building D, 5th Floor, Kyai Tapa Street, Grogol, Jakarta 11440, Indonesia.  
Corresponding author: Andry Prima (andry.prima@trisakti.ac.id) 
Manuscript received:  February 18th, 2026; Revised: March 27th, 2026 
Approved:  May 04th, 2026; Available online: June 15th, 2026; Published: June 15th, 2026. 
Andry Prima1, Bayu Satiyawira1, Havidh Pramadika1, Daud Asrun Nauw1, Lisa Samura1, Mustamina 
Maulani1, Cahaya Rosyidan1, Maman Djumantara1, Djunaedi Agus Wibowo1, Wiwik Dahani3, and 
Osama Jawaid Butt2

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
336 I DOI org/10.29017/scog.v49i2.2019  
INTRODUCTION 
Indonesia’s energy system continues to face 
structural challenges due to its high dependence on 
imported diesel fuel, most notably  in the 
transportation and industrial sectors  (Fischer & 
Meyer 2020). Although Indonesia has made 
significant progress in developing biodiesel based 
on domestic palm oil resources, overall diesel 
demand has surged, resulting in persistent import 
dependency and exposure to international price 
volatility, supply disruptions, and fiscal pressures  
(PASPI 2024). Diesel imports not only affect 
energy security but also have broader 
macroeconomic implications through foreign 
exchange outflows and subsidy burdens. 
Addressing this dependency has therefore become 
a central objective of national energy policy  
(Wirawan et al., 2024). 
In response to these challenges, the government 
of Indonesia has progressively strengthened 
biodiesel blending mandates as a strategic 
instrument to substitute imported fossil diesel with 
domestically produced biofuel  (ESDM 2025). 
According to an official statement by the Ministry 
of Energy and Mineral Resources, the government 
plans to implement a mandatory B50 biodiesel 
blending policy starting in 2026 as part of a 
broader strategy to stop diesel imports and enhance 
national energy security  (Pambudi et al., 2019; 
Veza et al., 2021; Widrian et al., 2022). This policy 
represents a significant escalation from previous 
blending levels and reflects strong political 
commitment to leveraging domestic bioenergy 
resources. However, while higher blending 
mandates are often assumed to directly reduce 
diesel imports, their actual effectiveness depends 
on complex interactions among biodiesel 
production capacity, domestic allocation versus 
export behaviour , and ongoing growth in diesel 
demand (Dharmawan et al., 2020). Existing policy 
debates and analytical studies frequently treat 
biodiesel blending targets as a linear substitution 
mechanism, implicitly assuming that higher 
blending rates will proportionally reduce diesel 
imports. In practice, biodiesel policy outcomes are 
shaped by dynamic feedback mechanisms, capacity 
constraints, and time -dependent system behavior  
(Silalahi et al., 2019). If domestic biodiesel 
production growth does not keep pace with diesel 
demand expansion, or if a significant share of 
biodiesel output is diverted to exports, the import 
substitution effect of blending mandates may 
weaken over time. These dynamics highlight the 
need for an analytical framework capable of 
capturing feedback -driven behavior and structural 
constraints rather than relying solely on static or 
short-term assessments.  
Previous studies on biodiesel and biofuel policy 
impacts have predominantly employed econometric 
approaches, partial equilibrium models, or scenario
-based accounting analyses. While these methods 
provide valuable insights into historical 
relationships and short -term policy effects, they 
often lack the ability to represent nonlinear 
interactions, feedback loops, and delays that 
characterize real -world energy systems  
(Ismukurnianto 2022; Jumardi et al., 2025; Rahman 
2022; Usman & Haans 2017). More recent research 
has applied system dynamics modeling to energy 
policy analysis, recognizing its suitability for 
capturing endogenous system behavior (Anggoro et 
al., 2023). Meanwhile, Monte Carlo simulations 
have been widely used to quantify uncertainty in 
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Andry Prima, Bayu Satiyawira, Havidh Pramadika, Daud Asrun Nauw, Lisa Samura, 
Mustamina Maulani, Cahaya Rosyidan, Maman Djumantara, Djunaedi Agus Wibowo, Wiwik 
Dahani, and Osama Jawaid Butt , 2026, A System Dynamics Approach to Analyze Biodiesel 
Production and Oil Import Dependency in Indonesia, Scientific Contributions Oil and Gas, 
49 (2) pp. 335-351. DOI org/10.29017/scog.v49i2.2019.

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 337 
energy demand forecasts and policy outcomes  
(Wicaksono et al., 2019). However, studies that 
integrate system dynamics modeling with 
probabilistic Monte Carlo analysis in the context of 
biodiesel blending and diesel import dependency 
remain limited, particularly for emerging 
economies such as Indonesia.  
This study addresses these gaps by developing 
an integrated modeling framework that combines 
system dynamics and Monte Carlo simulation to 
analyze the impacts of biodiesel blending policies 
on diesel import dependency under uncertainty. 
The analysis explicitly incorporates biodiesel 
production growth, domestic allocation after 
exports, diesel demand growth, and policy blending 
effectiveness within a feedback-based structure. By 
focusing not only on annual outcomes but also on 
cumulative import reductions and probabilistic risk 
profiles, the study provides a more comprehensive 
assessment of long -term policy performance. 
The framework is explicitly aligned with 
Indonesia ’s planned B50 mandate starting in 
2026, ensuring strong policy relevance and 
timeliness  (Nuva et al., 2019).   
The findings of this study are intended to inform 
multiple stakeholders. For policymakers and 
government agencies, the results provide evidence -
based insights into the conditions under which 
biodiesel blending mandates can effectively reduce 
diesel import dependency and mitigate long -term 
risk. For energy planners and regulators, the 
modeling framework offers a practical tool to 
evaluate alternative policy and supply -side 
strategies under uncertainty. For industry 
stakeholders, particularly biodiesel producers and 
feedstock suppliers, the study highlights the 
importance of sustained production capacity 
expansion and domestic market allocation. For the 
academic community, this research contributes to 
the literature by demonstrating the value of 
integrating system dynamics and probabilistic 
simulation for policy -oriented energy system 
analysis in developing and emerging economies. 
METHODOLOGY 
This study adopts a mixed -method modeling 
approach that integrates system dynamics modeling 
with probabilistic Monte Carlo simulation to 
analyze the impact of biodiesel blending policies 
on diesel import dependency in Indonesia  (Jiao et 
al., 2014; Nemeth & Fearnhead 2021).  The 
methodological framework is designed to capture 
both the structural behavior of the energy system 
and the uncertainty associated with long -term 
policy implementation. The analysis is conducted 
through a sequence of interrelated stages, 
beginning with conceptual modeling and 
followed by quantitative simulation and 
uncertainty assessment . 
Research framework and data sources 
The research framework is grounded in a 
system dynamics perspective, which is particularly 
suitable for analyzing energy systems characterized 
by feedback loops, nonlinearity, and time delays. 
The model focuses on the interaction between 
diesel demand, biodiesel production, domestic 
biodiesel allocation, exports, and diesel imports 
as a residual component . 
The primary data source for the supply -side 
calibration is historical biodiesel data for Indonesia 
spanning 2013–2024, including biodiesel 
production, domestic utilization, diesel fuel 
demand (B0) and exports  (ESDM, 2024) . These 
data are compiled from the national biodiesel 
dataset and cross -referenced with the 2024 
Handbook of Energy & Economic Statistics of 
Indonesia. The data are used to establish baseline 
trends and parameter ranges rather than to perform 
direct econometric estimation, consistent with the 
exploratory and policy -oriented nature of system 
dynamics modeling. 
Conceptual model development: causal loop 
diagram 
The first stage of model development involves 
the construction of a causal loop diagram (CLD) to 
identify the dominant feedback structures 
governing biodiesel production and diesel import

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
338 I DOI org/10.29017/scog.v49i2.2019  
dependency (Crabolu et al., 2023) . The CLD 
captures reinforcing and balancing feedback loops 
linking biodiesel production growth, domestic 
biodiesel availability, blending mandates, diesel 
demand, and diesel imports. Export allocation is 
explicitly incorporated as a leakage mechanism that 
reduces the volume of biodiesel available for 
domestic substitution. 
The CLD serves two key purposes. First, it 
provides a transparent conceptual representation of 
policy-relevant system behavior. Second, it guides 
the selection of state variables, flows, and auxiliary 
relationships in the subsequent quantitative model. 
Particular attention is given to identifying capacity 
constraints and feedback dominance under 
different policy scenarios, which later inform 
scenario design and interpretation. 
Quantitative system dynamics model 
Based on the CLD, a simplified stock -flow 
system dynamics model is developed to simulate 
diesel import requirements over the study horizon. 
Diesel demand is modeled as an exogenous growth 
process, while biodiesel production follows a 
growth trajectory calibrated to historical trends and 
scenario assumptions, following commonly 
adopted approaches in energy system dynamics 
modeling  (Prima et al., 2026) . Domestic biodiesel 
availability is calculated as total production minus 
exports, and diesel imports are determined 
residually after accounting for biodiesel 
substitution under specified blending mandates. 
Two main deterministic scenarios are simulated. 
The baseline scenario assumes the continuation of 
existing blending levels throughout the simulation 
horizon. The policy scenario implements a B50 
biodiesel blending mandate scheduled to take effect 
in 2026, consistent with current government plans. 
An additional enhanced supply scenario combines 
the B50 mandate with accelerated biodiesel 
production growth to assess the role of supply -side 
readiness. Simulation outputs include annual diesel 
import requirements, import dependency 
indicators, and cumulative import reductions 
relative to the baseline. 
Uncertainty and Monte Carlo Simulation 
To account for uncertainty in long -term 
projections, the deterministic system dynamics 
model is extended using Monte Carlo simulation. 
Key uncertain parameters include diesel demand 
growth rates, biodiesel production growth rates, 
export shares, and blending effectiveness. 
Probability distributions are assigned to these 
parameters based on historical variability and 
plausible policy ranges. 
Thousands of Monte Carlo iterations are 
conducted to generate probabilistic distributions of 
outcomes for selected target years, specifically 
2030 and 2035. The results are analyzed using 
histograms, cumulative distribution functions 
(CDFs), boxplots, and fan charts to assess not 
only expected policy impacts but also the 
associated uncertainty and risk profiles. This 
probabilistic approach enables a more robust 
evaluation of policy performance under 
structural and parametric uncertainty . 
Visualization and scenario interpretation 
Model outputs are visualized using a 
combination of time -series plots, cumulative 
impact curves, probabilistic distributions, and 
uncertainty envelopes. 
These visualizations support comparative 
interpretation across scenarios and time horizons, 
highlighting both central tendencies and variability 
(Ridaliani et al., 2025; Samura et al., 2025; 
Satiyawira et al., 2025) . The integrated use of 
deterministic and probabilistic visual tools ensures 
that policy conclusions are informed by both 
expected outcomes and uncertainty considerations. 
This is illustrated in Figure 1. 
 
RESULT AND DISCUSSION  
The findings derived from the CLD and 
descriptive data analysis are highly relevant to 
recent policy developments in Indonesia ’s energy 
sector. According to an official statement released 
by the Ministry of Energy and Mineral Resources, 
the Indonesian government plans to implement a 
mandatory B50 biodiesel blending policy by 2026

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 339 
 
                       Figure 1. Flow of chart. Research framework integrating system dynamics modelling and Monte Carlo 
simulation for evaluating biodiesel policy impacts on diesel import dependency.  
 
Figure 2. Causal loop diagram illustrating feedback relationships among biodiesel production, domestic allocation, 
diesel demand, blending policy, and diesel import dependency.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
340 I DOI org/10.29017/scog.v49i2.2019  
Table 1. Biodiesel production, domestic utilization, and export in Indonesia (2013–2024) Source: Processed from 
national biodiesel statistics (Excel dataset) and handbook of energy & economic statistics of Indonesia 2024. 
as part of a broader strategy to stop diesel imports 
and strengthen national energy security (ESDM, 
2025). This policy direction provides an important 
real-world context for interpreting the dynamic 
relationships identified in this study (Figure 2). 
The CLD illustrates the fundamental feedback 
mechanisms governing biodiesel production and 
diesel import dependency. An increase in biodiesel 
production enhances the availability of domestic 
biodiesel supply, which in turn increases the 
volume of biodiesel absorbed into the diesel fuel 
mix in accordance with mandatory blending 
targets. Higher biodiesel utilization directly reduces 
the demand for fossil diesel, thereby lowering 
diesel import volumes and import dependency. 
This reduction in imports contributes positively to 
national energy security and reinforces policy 
justification for higher blending mandates. At the 
same time, the CLD explicitly captures a 
counteracting mechanism through biodiesel 
exports. Rising export volumes reduce the 
biodiesel supply available for domestic blending, 
constraining the import substitution effect. 
Consequently, the CLD emphasizes that the 
effectiveness of biodiesel blending policies is not 
determined solely by the blending target, but also 
by the dynamics of biodiesel production growth, 
diesel demand growth, and export allocation. 
The CLD is translated into a simplified 
quantitative system dynamics model that retains the 
core structure relevant to the research objective. 
The model links diesel demand, biodiesel 
production, domestic biodiesel availability after 
exports, and diesel imports as a residual variable 
after biodiesel substitution. Historical biodiesel 
data from the dataset (2013–2024) are used to 
anchor the supply side of the model.  
Table 1 presents the historical series of 
biodiesel production, domestic utilization, and 
exports over this period. It also highlights why 
export share is explicitly modelled, since exports 
represent a non-negligible leakage that can weaken 
the effectiveness of domestic blending policies. 
Moreover, the observed fluctuations in export 
volumes suggest that external market dynamics and 
price differentials play a significant role in shaping 
supply allocation decisions.  
Simulation results are presented through a series 
of figures. Figure 2 compares diesel import 
requirements under the baseline and the B50 policy 
scenario. The baseline represents a continuation of 
existing blending levels. The policy scenario 
incorporates the actual policy trajectory 
implemented in Indonesia, consisting of B35 up to 
2023, B40 during 2024–2025, and B50 starting in 
2026, which are in line with government plans to 
gradually eliminate diesel imports through higher 
biodiesel mandates. The policy curve consistently 
lies below the baseline curve, indicating reduced 
import requirements. The vertical gap between the 
two curves represents the magnitude of import 
substitution achieved by the policy. From a 
system dynamics perspective, this reduction 
reflects not only the higher blending target but 
also the system ’s capacity to supply sufficient 
biodiesel domestically . 
 
Year Biodiesel production (Thousand KL) Domestic utilization (Thousand KL) Biodiesel export (Thousand KL)  
 2013 2,8 1.1 1.7  
 2014 3,4 1.6 1.8  
 2015 3,7 1.9 1.8  
 2016 4,1 3.1 1.0  
 2017 6,5 4.7 1.8  
 2018 7,6 6.1 1.5  
 2019 8,4 6.4 2.0  
 2020 8,8 7.2 1.6  
 2021 9,3 8.2 1.1  
 2022 10,4 9.6 0.8  
 2023 12,2 11.3 0.9  
 2024 13,9 13.1 0.8

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 341 
 
    Figure 3 displays the import dependency 
indicator, approximated as the ratio of diesel 
imports to total diesel demand. This indicator is 
particularly relevant for energy policy analysis, as 
it captures relative dependence rather than absolute 
volumes. Under the B50 policy scenario, import 
dependency declines compared to the baseline. 
However, the reduction is not strictly proportional 
to the increase in blending rates, as the system is 
constrained by biodiesel supply availability. If 
biodiesel production growth does not keep pace 
with diesel demand growth, import dependency 
may stabilize or even increase despite higher 
blending targets. This outcome is consistent with 
the CLD logic, which highlights capacity 
constraints and export leakage as limiting factors. 
 Figure 4. Diesel import dependency ratio under 
baseline and biodiesel blending policy scenarios. 
This graph presents the ratio of diesel imports to 
total diesel demand. The decline under the B50 
scenario indicates the impact of the blending 
policy, but changes are not strictly proportional due 
to supply limitations and export allocations. 
This outcome is consistent with the CLD logic, 
which highlights capacity constraints and export 
leakage as limiting factors. In particular, the 
Figure 3. Projected diesel import requirements under baseline and biodiesel policy scenarios.                                                    
The curve shows annual diesel import requirements under the baseline and B50 scenarios. The vertical gap between 
the curves represents import reduction achieved by the B50 policy, emphasizing that the effectiveness depends on 
domestic biodiesel supply capacity. 
effectiveness of higher blending mandates is 
strongly moderated by the ability of the domestic 
biodiesel sector to expand production capacity and 
allocate sufficient volumes to the domestic market. 
When production growth lags behind demand 
expansion, the balancing effect of biodiesel 
substitution weakens over time, allowing 
reinforcing demand -driven dynamics to dominate 
the system. As a result, import dependency 
becomes increasingly sensitive to structural 
conditions on the supply side rather than policy 
ambition alone. These findings suggest that 
blending mandates must be accompanied by 
coordinated measures aimed at strengthening 
biodiesel feedstock availability, processing 
capacity, and domestic allocation mechanisms in 
order to achieve sustained reductions in diesel 
import dependency. 
Figure 4 illustrates the cumulative reduction in 
diesel imports relative to the baseline scenario 
under the two policy -oriented cases, namely the 
implementation of the B50 mandate from 2026 and 
the B50 mandate combined with accelerated 
biodiesel production growth. The accelerated 
growth assumption is derived from historical

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
342 I DOI org/10.29017/scog.v49i2.2019  
 
 Figure 4. Diesel import dependency ratio under baseline and biodiesel blending policy scenarios. 
This graph presents the ratio of diesel imports to total diesel demand. The decline under the B50 scenario indicates the 
impact of the blending policy, but changes are not strictly proportional due to supply limitations and export allocations. 
 
Figure 5.Cumulative diesel import reduction under B50 and enhanced biodiesel production scenarios. 
This figure highlights cumulative diesel import reduction relative to the baseline for two scenarios. The widening 
difference between standard B50 and B50 with accelerated biodiesel production underscores the cumulative benefits of 
domestic supply capacity development.

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 343 
 
 Monte Carlo distribution of import reduction vs baseline (2030) 
Figure 6. Probability distribution of diesel import reduction from Monte Carlo simulation in 2030. 
The histogram shows the probabilistic distribution of diesel import reduction in 2030 from Monte Carlo simulation.              
The unimodal distribution around a median of ~5.2 million kL indicates a stable medium-term outcome with relatively 
low variability. 
production trends, national biodiesel expansion 
targets reported by ESDM, and projections from 
previous studies on biofuel capacity development. 
This scenario represents a policy -consistent upper-
bound trajectory of supply -side readiness. The 
cumulative representation highlights the long -term 
impact of policy interventions by aggregating 
annual import savings over time, thereby providing 
a clearer indication of structural change in import 
dependence. Following the introduction of the B50 
policy, cumulative import reductions increase 
steadily in both scenarios, indicating that the 
benefits of higher blending mandates are not 
instantaneous but accumulate progressively as 
the system adjusts to new production and 
consumption patterns . 
Figure 5.Cumulative diesel import reduction 
under B50 and enhanced biodiesel production 
scenarios. This figure highlights cumulative diesel 
import reduction relative to the baseline for two 
scenarios. The widening difference between 
standard B50 and B50 with accelerated biodiesel 
production underscores the cumulative benefits of 
domestic supply capacity development. 
The cumulative simulation results (Figures 2–4) 
further emphasize the long -term and path -
dependent nature of biodiesel policy impacts. By 
2035, the B50 policy scenario achieves cumulative 
diesel import reductions of approximately 55–58 
million kiloliters relative to the baseline trajectory. 
When the blending mandate is combined with 
accelerated biodiesel production growth, 
cumulative import savings increase further to 
around 60 million kiloliters. The widening gap 
between these two scenarios illustrates the 
compounding benefits of early and sustained 
supply-side expansion, whereby relatively modest 
annual reductions in diesel imports translate into 
substantially larger cumulative gains over time. 
These results confirm that the long -term 
effectiveness of biodiesel policy is shaped less by 
the nominal blending target itself and more by the 
trajectory of domestic supply capacity development 
and retention for domestic use. 
Beyond deterministic outcomes, the Monte 
Carlo simulation provides critical insight into the 
uncertainty and risk associated with these policy 
impacts. For 2030, the distribution of diesel import 
reduction is centered around a median value of 
approximately 5.2 million kiloliters, with relatively

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
344 I DOI org/10.29017/scog.v49i2.2019  
limited dispersion (Figure 5). This indicates that 
medium-term policy outcomes under the B50 
mandate are comparatively robust to uncertainty in 
key parameters such as diesel demand growth, 
biodiesel production expansion, export share, and 
blending effectiveness. In contrast, the 2035 
distribution shifts to a higher median import 
reduction of approximately 6.8 million kiloliters 
and exhibits substantially wider dispersion. This 
widening uncertainty reflects the cumulative 
propagation of structural and parameter uncertainty 
over longer time horizons, as reinforcing feedback 
mechanisms increasingly amplify differences in 
biodiesel production growth trajectories and 
domestic allocation performance (Figure 6). 
The divergence between the two policy curves 
becomes increasingly pronounced over time, with 
the scenario incorporating faster biodiesel 
production growth consistently achieving higher 
cumulative import reductions. This widening gap 
illustrates the compounding effect of supply -side 
readiness, whereby incremental annual reductions 
in diesel imports translate into substantially larger 
cumulative savings in the long run. In contrast, the 
policy-only scenario exhibits a more moderate 
accumulation of import reductions, reflecting 
limitations imposed by production capacity and 
export allocation. From a system dynamics 
perspective, this behavior reflects the strengthening 
of balancing feedback loops in the presence of 
enhanced production growth, which progressively 
suppress the reinforcing demand -driven forces that 
otherwise sustain import dependency. 
Overall, the figure underscores that the long -
term effectiveness of biodiesel blending policies is 
determined not only by the level of the blending 
mandate itself, but also by the trajectory of 
domestic biodiesel supply expansion. The 
cumulative nature of the results further emphasizes 
the strategic importance of early and sustained 
investments in production capacity, as delays in 
supply-side development can result in permanently 
lower cumulative import savings even when 
ambitious blending targets are eventually achieved. 
Given the increasing uncertainty associated with 
longer-term projections, the study complements 
deterministic scenario analysis with Monte Carlo 
simulation. Monte Carlo methods are applied to 
key uncertain parameters, including diesel demand 
growth, biodiesel production growth, export share, 
and policy blending effectiveness . A total of 
10,000 simulation iterations are performed to 
ensure statistical robustness of the results with key 
uncertain parameters that include diesel demand 
growth rates, biodiesel production growth rates, 
export shares, and blending effectiveness. By 
running thousands of iterations, the model 
generates probabilistic distributions of outcomes 
such as diesel import reduction and import 
dependency for 2030 and 2035. This probabilistic 
framework allows policy impacts to be assessed 
not only in terms of expected values but also in 
terms of risk and uncertainty. 
For 2030, the Monte Carlo simulation projects a 
probability distribution of diesel import reduction 
relative to the baseline scenario. The distribution 
exhibits a unimodal shape centred around a median 
value of approximately 5.2 million kiloliters, 
indicating the most likely magnitude of import 
reduction under the assumed uncertainty ranges. 
The relatively moderate spread of the distribution 
suggests that, in the medium term, the effectiveness 
of the biodiesel policy remains comparatively 
stable despite variability in demand growth, 
production expansion, export allocation, and 
blending performance. Most simulation outcomes 
cluster within a narrow band around the median, 
implying that the policy impact by 2030 is 
reasonably robust and less sensitive to extreme 
parameter realizations. This pattern reflects the 
dominance of structural policy effects during the 
early implementation phase, when system inertia 
and shorter accumulation periods limit the 
amplification of uncertainty. 
In contrast, the Monte Carlo distribution for 
2035 displays a noticeably wider spread and a 
rightward shift in the median value to 
approximately 6.8 million kiloliters. This indicates 
that the potential magnitude of diesel import 
reduction increases over the longer term, but is 
accompanied by substantially higher uncertainty. 
The broader distribution reflects the cumulative 
effect of uncertainty propagation over time, as 
small deviations in growth rates, export shares, 
and blending effectiveness compound across 
successive years. While higher import

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 345 
reductions become increasingly probable, the 
dispersion of outcomes highlights that long -term 
policy performance is more vulnerable to 
structural constraints and supply side variability. 
From a system dynamics perspective, this 
behavior is consistent with reinforcing feedback 
mechanisms, whereby differences in biodiesel 
production growth trajectories and domestic 
allocation increasingly shape the system ’s 
evolution as the time horizon extends . 
To further explore the probabilistic 
characteristics of diesel import reduction beyond 
central tendency and dispersion, the analysis 
extends from frequency -based representations to 
cumulative probability assessment. While 
histogram distributions provide insight into the 
range and likelihood of outcomes, they do not 
directly convey the probability of achieving a 
specific level of import reduction. To address this 
limitation, the cumulative distribution function 
(CDF) is employed to evaluate policy performance 
in probabilistic terms, enabling a more explicit 
interpretation of risk, confidence levels, and 
threshold-based outcomes under uncertainty. 
Figure 7 depicts the cumulative distribution 
functions of diesel import reduction relative to the 
baseline scenario for the years 2030 and 2035 
under the B50 policy. The CDF curves reveal a 
clear rightward shift from 2030 to 2035, indicating 
an increasing probability of achieving larger import 
reductions as the policy effects accumulate over 
time. The 2030 curve rises more steeply and 
reaches higher cumulative probabilities at lower 
reduction levels, reflecting comparatively lower 
uncertainty in medium -term outcomes. In contrast, 
the 2035 curve exhibits a more gradual ascent, 
signifying a wider dispersion of possible outcomes 
and greater long -term uncertainty. This divergence 
highlights the compounding effect of uncertainty 
propagation within the system dynamics 
framework, where variations in biodiesel 
production growth, export allocation, and demand 
trajectories increasingly influence outcomes over 
longer horizons. Importantly, the separation 
between the two curves illustrates that although 
higher import reductions become more attainable 
by 2035, the probability of achieving any given 
reduction level depends critically on sustained 
supply-side performance and policy consistency. 
Ultimately, the CDF analysis confirms that long -
term reductions in diesel import dependency 
require combining ambitious blending mandates 
with adaptive and resilient supply -side strategies 
capable of mitigating uncertainty and maintaining 
policy effectiveness over time. 
While CDF provides a clear probabilistic 
perspective on the likelihood of achieving specific 
levels of diesel import reduction, it does not 
explicitly summarize the central tendency and 
dispersion of outcomes in a compact comparative 
form. To complement the CDF analysis, the results 
are further examined using boxplot representations, 
which allow direct comparison of median 
outcomes, interquartile ranges, and extreme values 
across different target years. This approach 
facilitates a more intuitive assessment of how 
uncertainty and risk evolve over time under the 
same policy framework. Figure 8 illustrates the 
boxplot comparison of Monte Carlo simulation 
results for diesel import reduction relative to the 
baseline scenario in 2030 and 2035. The boxplot 
for 2030 exhibits a relatively narrower interquartile 
range with a median centered around moderate 
import reduction levels, indicating that medium -
term policy outcomes are comparatively stable and 
clustered within a limited range of variability. In 
contrast, the 2035 boxplot shows a higher median 
value accompanied by a substantially wider 
interquartile range and a greater number of extreme 
observations. This pattern confirms that, although 
the expected magnitude of import reduction 
increases over the longer term, the associated 
uncertainty also expands significantly. The 
presence of wider whiskers and more pronounced 
outliers in 2035 reflects the cumulative 
amplification of uncertainty inherent in long -term 
system dynamics, where variations in biodiesel 
production growth, export behavior, and demand 
trajectories progressively diverge. The CDF results 
and the boxplot analysis show that long -term 
reductions in diesel import dependency offer 
greater potential benefits but are inherently subject 
to higher risk, underscoring the importance of 
adaptive policy mechanisms and continuous 
monitoring of supply-side performance.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
346 I DOI org/10.29017/scog.v49i2.2019  
 
 Monte Carlo distribution of import reduction vs baseline (2035) 
Figure 7. Probability distribution of diesel import reduction from Monte Carlo simulation in 2035. 
The 2035 distribution shows a median of ~6.8 million kL with a wider spread, reflecting higher long-term uncertainty due 
to cumulative variability in supply, demand, and blending effectiveness. 
 
Figure 9. Boxplot comparison of  Monte Carlo simulation results for diesel import reduction in 2030 and 2035. 
The boxplot compares median, interquartile range, and outliers between 2030 and 2035. The wider interquartile range 
and whiskers in 2035 highlight increasing risk and uncertainty over the long term. 
Monte Carlo results: import reduction vs baseline 
(Boxplot comparison)

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 347 
 
Figure 10. Fan chart of diesel import requirements under baseline and B50 policy scenarios with P5–P95 uncertainty intervals.  
The fan chart illustrates how uncertainty evolves over time. The B50 scenario shows a lower median and narrower uncertain-
ty band than the baseline,highlighting the stabilizing effect of biodiesel substitution on the energy system. 
Although the boxplot analysis effectively 
summarizes differences in central tendency and 
variability at selected target years, it does not 
adequately represent the dynamic evolution of 
uncertainty across the simulation period.  
To overcome this limitation, the analysis uses a 
fan chart to explicitly illustrate how uncertainty 
propagates over time under both baseline and 
policy scenarios. By integrating median trajectories 
with percentile-based uncertainty intervals, the fan 
chart offers a more holistic depiction of the 
temporal development of diesel import 
requirements and the associated risk profile 
throughout the modeling horizon. 
Figure 9 shows the fan chart of diesel import 
requirements under the baseline and B50 policy 
scenarios, incorporating uncertainty bounds 
defined by the P5 –P95 percentile range. The 
baseline trajectory exhibits a steadily increasing 
median import requirement over time, 
accompanied by an expanding uncertainty 
envelope. This widening fan reflects the 
compounding effect of uncertainty in demand 
growth and structural system dynamics, indicating 
that reliance on imports becomes increasingly 
exposed to risk in the absence of stronger 
substitution mechanisms. In contrast, the policy 
scenario displays a markedly lower median import 
trajectory, particularly after the implementation of 
the B50 mandate, demonstrating the stabilizing 
influence of biodiesel substitution on diesel import 
needs. Although the uncertainty band under the 
policy scenario also widens over time, its overall 
range remains consistently lower than that of the 
baseline case, suggesting a risk-mitigating effect of 
the policy intervention. 
The increasing separation between the baseline 
and policy fan charts highlights the dual function of 
biodiesel policy in reducing both the expected level 
of diesel imports and the degree of long -term 
uncertainty. From a system dynamics standpoint, 
the policy scenario reinforces balancing feedback 
mechanisms associated with domestic fuel 
substitution, thereby attenuating the reinforcing 
effects of demand growth that characterize the 
baseline trajectory. The partial overlap of 
uncertainty bands in the early years indicates that 
short-term outcomes remain sensitive to structural 
and parameter variability, whereas more 
pronounced divergence in later years underscores 
the cumulative advantages of sustained policy 
implementation. Overall, these findings

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
348 I DOI org/10.29017/scog.v49i2.2019  
demonstrate that biodiesel blending mandates play 
a critical role not only in lowering anticipated 
diesel import volumes but also in enhancing the 
resilience of the energy system to long -term 
uncertainty, supporting the need for integrated 
policy approaches that align demand -side 
mandates with continous development of 
domestic supply capacity . 
 
CONCLUSION 
This study applies a system dynamics 
framework combined with probabilistic Monte 
Carlo simulation to examine the impact of 
biodiesel blending policies on diesel import 
dependency in Indonesia. The results demonstrate 
that increasing biodiesel blending mandates, as 
represented by the B50 policy scenario 
implemented from 2026, can significantly reduce 
diesel import requirements relative to the baseline 
scenario. However, the analysis also reveals that 
the effectiveness of blending mandates is 
fundamentally conditioned by domestic biodiesel 
supply growth and allocation to the domestic 
market. Under the policy -only scenario, diesel 
imports decline relative to the baseline but may 
continue to increase in absolute terms due to 
persistent growth in diesel demand, indicating that 
blending mandates alone are insufficient to fully 
counter demand-driven pressures. 
The cumulative system dynamics results 
highlight the long -term and path -dependent nature 
of policy impacts. By 2035, the B50 policy 
scenario achieves cumulative diesel import 
reductions of approximately 55–58 million 
kiloliters relative to the baseline trajectory. When 
the blending mandate is complemented by 
accelerated biodiesel production growth, 
cumulative import savings increase further to 
around 60 million kiloliters. This divergence 
illustrates the compounding benefits of early and 
sustained supply -side expansion, where relatively 
modest annual reductions translate into 
substantially larger cumulative gains over time. 
These findings confirm that the long -term 
effectiveness of biodiesel policy is shaped more by 
the trajectory of domestic supply capacity 
development than by the blending target itself. 
The Monte Carlo simulation further reveals the 
risk and uncertainty profile associated with these 
policy outcomes. For 2030, the distribution of 
diesel import reduction is centered around a 
median of approximately 5.2 million kiloliters, 
with relatively limited dispersion, indicating that 
medium-term policy impacts are comparatively 
robust to uncertainty in diesel demand growth, 
biodiesel production expansion, export share, and 
blending effectiveness. In contrast, the 2035 results 
exhibit a higher median import reduction of 
approximately 6.8 million kiloliters accompanied 
by substantially wider dispersion. This widening 
uncertainty reflects the cumulative propagation of 
structural and parameter uncertainty over longer 
time horizons, as reinforcing feedback mechanisms 
amplify differences in production growth and 
domestic allocation performance.  
The probabilistic analyses using cumulative 
distribution functions, boxplots, and fan charts 
consistently show that while larger import 
reductions become increasingly attainable over 
time, long-term outcomes are inherently subject to 
higher variability. Importantly, the fan chart 
analysis demonstrates that the B50 policy scenario 
not only lowers the median trajectory of diesel 
imports relative to the baseline but also maintains a 
narrower uncertainty envelope, indicating a 
stabilizing effect of biodiesel substitution on the 
energy system. Nevertheless, partial overlap of 
uncertainty bands in the early years suggests that 
short-term outcomes remain sensitive to structural 
conditions and implementation dynamics. 
From a policy perspective, these results imply 
that the B50 blending mandate should be regarded 
as a necessary but not sufficient instrument for 
achieving sustained reductions in diesel import 
dependency. To maximize policy effectiveness and 
reduce long-term risk exposure, blending mandates 
must be accompanied by coordinated measures that 
expand biodiesel feedstock availability, strengthen 
processing capacity, and manage export leakage to 
ensure sufficient domestic supply. Consequently, 
an integrated policy strategy that aligns demand -
side blending mandates with continuous supply -
side development and adaptive monitoring 
mechanisms is essential to enhance national energy

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 349 
Terms & 
Symbols Definition Unit 
B50 Mandatory biodiesel 
blending of 50% 
biodiesel with diesel 
fuel 
% (v/v) 
B35 Mandatory biodiesel 
blending of 35% 
biodiesel with diesel 
fuel 
% (v/v) 
Biodiesel Renewable fuel 
derived from 
biological sources 
used as diesel 
substitute 
– 
CLD Causal loop diagram – 
Diesel 
Demand 
Total domestic 
demand for diesel fuel 
kiloliters 
(kL) 
Diesel 
Import 
Volume of diesel fuel 
imported to meet 
domestic demand 
kiloliters 
(kL) 
 
GLOSSARY OF TERMS AND SYMBOLS 
security, reduce vulnerability to import shocks, and 
improve the resilience of Indonesia ’s fuel system 
under long-term uncertainty. 
 
ACKNOWLEDGEMENT 
The authors gratefully acknowledge the 
academic and financial support provided by 
Universitas Trisakti, including the study program, 
faculty, and the university management, throughout 
all stages of research  and manuscript preparation. 
The authors also acknowledge that portions of the 
writing, language refinement, and structuring of 
this manuscript were assisted by artificial 
intelligence (AI) –based tools, under the full 
supervision and responsibility of the authors. All 
analyses, interpretations, and conclusions 
presented in this paper remain the sole 
responsibility of the authors . 
 
DECLARATIONS 
The authors declare that there is no conflict of 
interest regarding the publication of this paper. 
This research was conducted independently and has 
not been published or submitted simultaneously to 
another journal. All authors have reviewed and 
approved the final version of the manuscript. 
Author contribution 
Andry Prima contributed to conceptualization, 
methodology development, supervision, and 
manuscript review. Bayu Satiyawira, Havidh 
Pramadika, and Daud Asrun Nauw contributed to 
data analysis, system dynamics modeling, and 
simulation. Lisa Samura, Mustamina Maulani, and 
Cahaya Rosyidan contributed to literature review, 
data interpretation, and manuscript preparation. 
Maman Djumantara and Djunaedi Agus Wibowo 
contributed to validation and technical review. 
Wiwik Dahani contributed to data verification and 
visualization. Osama Jawaid Butt contributed to 
manuscript editing, language refinement, and 
academic review. All authors have read and 
approved the final manuscript. 
Funding statement 
This research did not receive any specific grant 
from funding agencies in the public, commercial, 
or not -for-profit sectors. The authors declare that 
there are no financial interests or financial 
relationships that could have influenced the work 
reported in this study. 
Competing interest 
The authors declare that there are no competing 
interests related to authorship, institutional 
affiliations, personal relationships, academic 
interests, or professional activities that could have 
influenced the preparation, interpretation, or 
publication of this manuscript. 
The use of AI-assisted technology 
During the preparation of this manuscript, the 
authors used artificial intelligence (AI) –assisted 
tools to support language refinement, text 
organization, and manuscript editing. All scientific 
content, data analysis, interpretation of results, and 
final decisions remain under the full responsibility 
and supervision of the authors.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 335-351 
 
350 I DOI org/10.29017/scog.v49i2.2019  
Import 
Dependency 
Ratio of diesel imports 
to total diesel demand 
– 
Monte 
Carlo 
Simulation 
Probabilistic 
simulation method 
using random 
sampling 
– 
System 
Dynamics 
Modeling approach 
for analyzing 
feedback-driven 
systems 
– 
Domestic 
Utilization 
Biodiesel volume 
absorbed by the 
domestic market 
kiloliters 
(kL) 
Biodiesel 
Production 
Total annual 
production of 
biodiesel 
kiloliters 
(kL) 
Biodiesel 
Export 
Biodiesel volume 
allocated for export 
markets 
kiloliters 
(kL) 
Baseline 
Scenario 
Scenario assuming 
continuation of 
existing policies 
– 
Policy 
Scenario 
Scenario reflecting 
implementation of 
new policy (B50) 
– 
Feedstock Raw material used for 
biodiesel production 
– 
Energy 
Security 
Ability of a nation to 
ensure reliable energy 
supply 
– 
Import 
Substitution 
Replacement of 
imported fuel with 
domestic alternatives 
– 
CDF Cumulative 
distribution function 
– 
Fan Chart Graphical 
representation of 
uncertainty over time 
– 
 
REFERENCES 
Anggoro, P. W., Yuniarto, T., Bawono, B., 
Setyohadi, D. B., Murdapa, P. S., & Jamari, J., 
(2023), System dynamics modelling for 
calculation of carbon footprint on a non -
homogeneous production system: A case in a 
ceramic studio. Results in Engineering, 17. 
https://doi.org/10.1016/j.rineng.2022.100812. 
Crabolu, G., Font, X., & Eker, S., (2023), 
Evaluating policy complexity with Causal Loop 
Diagrams. Annals of Tourism Research, 100. 
https://doi.org/10.1016/j.annals.2023.103572. 
Dharmawan, A. H., Fauzi, A., Putri, E. I. K., 
Pacheco, P., Dermawan, A., Nuva, N., Amalia, 
R., & Sudaryanti, D. A., (2020), Bioenergy 
policy: The biodiesel sustainability dilemma in 
Indonesia. International Journal of Sustainable 
Development and Planning, 15(4). https://
doi.org/10.18280/ijsdp.150414. 
ESDM, (2024), The Handbook of Energy and 
Economic Statistics of Indonesia 2024. the 
Ministry of Energy and Mineral Resources 
(MEMR). www.esdm.go.id/assets/media/
content/content-handbook-of-energy-and-
economic-statistics-of-indonesia-2024.pdf. 
ESDM, (2025 December 23), Kementerian ESDM 
RI - Media Center - Arsip Berita - Pemerintah 
Tetapkan Alokasi Biodiesel Tahun 2026 sebesar 
15,65 juta kL. Direktorat Jenderal Minyak Dan 
Gas Bumi Kementerian ESDM Republik 
Indonesia. https://www.esdm.go.id/id/media -
center/arsip-berita/pemerintah-tetapkan-alokasi-
biodiesel-tahun-2026-sebesar-1565-juta-kl. 
Fischer, C., & Meyer, T., (2020), Baptists and 
Bootleggers in the Biodiesel Trade: EU -
Biodiesel (Indonesia). World Trade Review, 19
(2). https://doi.org/10.1017/
S1474745620000075. 
Ismukurnianto, D. A, (2022), Mitigation Of Carbon 
Dioxide And Green House Gas Emission From 
Oil And Gas Industry In Indonesia. Scientific 
Contributions Oil and Gas , 31(1). https://
doi.org/10.29017/scog.31.1.856. 
Jiao, J.-L., Han, K. -Y., Wu, G., Li, L. -L., & Wei, 
Y.-M, (2014). The effect of an SPR n the oil 
price in China: A system dynamics approach. 
Applied Energy, 133, 363–373. https://
doi.org/10.1016/j.apenergy.2014.07.103. 
Jumardi, A., Yusgiantoro, P., & Siagian, U., 
(2025), Development of Energy System 
Modeling to Forecast 2060 Oil and Gas 
Demand in The Household Sector of East 
Kalimantan Using Bottom -Up Method. 
Scientific Contributions Oil and Gas, 48(1), 159
–177. https://doi.org/10.29017/scog.v48i1.1732. 
Nemeth, C., & Fearnhead, P., (2021), Stochastic 
Gradient Markov Chain Monte Carlo. In Journal 
of the American Statistical Association (Vol. 
116, Number 533). https://

A System Dynamics Approach to Analyze Biodiesel Production and Oil Import Dependency in Indonesia 
(Prima et al.) 
 
DOI org/10.29017/scog.v49i2.2019 I 351 
doi.org/10.1080/01621459.2020.1847120. 
Nuva, N., Fauzi, A., Dharmawan, A. H., & Kumala 
Putri, E. I., (2019), Political Economy of 
Renewable Energy and Regional Development: 
Understanding Social and Economic Problems 
of Biodiesel Development in Indonesia. 
Sodality: Jurnal Sosiologi Pedesaan, 7(2). 
https://doi.org/10.22500/sodality.v7i2.19727. 
Pambudi, A., Puspitawati, E., & Nursechafia, N., 
(2019), The Determinants of Biodiesel Export 
in Indonesia. Signifikan: Jurnal Ilmu Ekonomi, 
8(2). https://doi.org/10.15408/sjie.v8i2.10961. 
PASPI (2024, March 15), Biodiesel Indonesia: 
Produksi, Konsumsi dan Ekspor (2024). Palm 
Oil Agribusiness Strategic Policy Institute. 
Prima, A., Moengin, P., Astuti, P., Sari, E., 
Nugrahanti, A., & Jawaid Butt, O., (2026), 
Determining The Dynamics of The Petroleum 
Buffer Reserve of Indonesia. Scientific 
Contributions Oil and Gas , 49(1), 65 –81. 
https://doi.org/10.29017/scog.v49i1.1987. 
Rahman, M., (2022), Cadangan Strategis Minyak 
untuk Keamanan Energi Indonesia. Lembaran 
Publikasi Minyak Dan Gas Bumi , 45(1), 47–53. 
https://doi.org/10.29017/lpmgb.45.1.681. 
Silalahi, M., Santoso, A., & Hidayat, D., (2019), A 
Scientometric Study on Biodiesel Development 
in Indonesia. STI Policy and Management 
Journal, 4(1). https://doi.org/10.14203/
stipm.2019.148. 
Usman, & Haans, A., (2017), Mengoptimalkan 
Perolehan Minyak pada Lahan Terbatas 
Menggunakan Sumur Berarah dan Pendesakan 
Air. (Optimizing Oil Recovery on Limited Land 
Area using Directional Wells and 
Waterflooding ). Lembaran Publikasi Minyak 
dan Gas Bumi , 51(1), 1 –12. http://
www.journal.lemigas.esdm.go.id. https://
doi.org/10.29017/LPMGB.51.1.9 
Veza, I., Said, M. F. M., Djamari, D. W., Abas, M. 
A., Latiff, Z. A., & Perang, M. R. M., (2021), 
Future Direction of Microalgae Biodiesel in 
Indonesia. Journal of Advanced Research in 
Applied Sciences and Engineering Technology, 
25(1). https://doi.org/10.37934/araset.25.1.16. 
Wicaksono, F. D., Bin Arshad, Y., & Sihombing, 
H., (2019), Monte Carlo net present value for 
techno-economic analysis of oil and gas 
production sharing contract. International 
Journal of Technology, 10(4). https://
doi.org/10.14716/ijtech.v10i4.2051. 
Widrian, A. F., Arifianto, B. S., Nurbaiti, & 
Sasongko, N. A., (2022), Review of Biodiesel 
Policy in Indonesia. IOP Conference Series: 
Earth and Environmental Science, 1034(1). 
https://doi.org/10.1088/1755-
1315/1034/1/012062. 
Wirawan, S. S., Solikhah, M. D., Setiapraja, H., & 
Sugiyono, A., (2024), Biodiesel implementation 
in Indonesia: Experiences and future 
perspectives. In Renewable and Sustainable 
Energy Reviews (Vol. 189). https://
doi.org/10.1016/j.rser.2023.113911.
