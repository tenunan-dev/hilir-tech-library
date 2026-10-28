---
source_id: "arxiv"
title: "Hybrid electrolyzer systems: Smart strategy or economic fallacy?"
url: "https://arxiv.org/abs/2607.06093"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2607.06093. Abstract: Hybrid electrolyzer systems: Smart strategy or economic fallacy?
Marie Arnold∗,a,b, Jonathan Brandt∗,b, Geert Tjarksa, Richard Hanke-Rauschenbachb
aEWE GASSPEICHER GmbH, Oldenburg, 26122, Lower Saxony, Germany
bLeibniz Universität Hannover , Institute for Electric Power Systems, Hanover , 30167, Lower Saxony, Germany
Abstract
Hybrid electrolyzer systems combining alkaline water electrolysis and pr"
---

# Hybrid electrolyzer systems: Smart strategy or economic fallacy?

Hybrid electrolyzer systems: Smart strategy or economic fallacy?
Marie Arnold∗,a,b, Jonathan Brandt∗,b, Geert Tjarksa, Richard Hanke-Rauschenbachb
aEWE GASSPEICHER GmbH, Oldenburg, 26122, Lower Saxony, Germany
bLeibniz Universität Hannover , Institute for Electric Power Systems, Hanover , 30167, Lower Saxony, Germany
Abstract
Hybrid electrolyzer systems combining alkaline water electrolysis and proton exchange membrane water electrolysis
have been investigated in the literature motivated by the expectation that their contrary techno-economic character-
istics compensate for the individual technical and economic restrictions of each technology, thereby improving the
profitability of green hydrogen production. To reassess the economic potential of hybrid electrolyzer systems be-
yond these technology-specific assumptions, we independently vary two key characteristics, electrolyzer efficiency
and investment cost, in a large-scale sensitivity analysis. For each generated parameter configuration, we performed
a techno-economic optimization of a green hydrogen supply chain, including two electrolyzers. The resulting system
design, cost objective, and dispatch behavior are subsequently analyzed. Consequently, hybrid electrolyzer systems
are identified as optimal if they provide a cost benefit over single electrolyzer systems. The analysis reveals that
hybrid electrolyzer systems represent the optimal solution in at most 5.0% of the investigated cases. Furthermore, the
maximum cost benefit is 0.057€/kgH2, which corresponds to only about 1% of the total green hydrogen production
cost. Additional analyses considering variations in energy purchase prices, storage fees, availability of renewable
energy, and baseline electrolyzer efficiency yield negligible changes to these results. Hence, considering that hybrid
electrolyzer systems offer marginal cost benefits and prove economically optimal in very few cases, they seem more
likely to represent an economic fallacy than a smart strategy.
Keywords:Hybrid electrolyzer system, Green hydrogen production, Techno-economic optimization, Renewable
energy
Supplementary material for this preprint is available as the ancillary file Supplementary_material.pdf on arXiv.
1. Introduction
Motivation
Global green hydrogen production is facing an implementation gap due to early market risks as well as technical
and economic challenges [1, 2]. The latter, particularly in Europe, result from high investment cost for electrolyzer
technologies as well as high electricity purchase prices for renewable energy sources (RES), which are required for
green hydrogen production [3, 4]. The technical challenges arise from uncertainties in efficiency and degradation,
with the latter becoming increasingly relevant under the fluctuating electrolyzer operation characteristic of RES-based
power supply [5, 6]. Both uncertainties are associated with additional cost, since efficiency directly affects electricity
consumption, while degradation reduces efficiency and shortens stack lifetime [7]. Thus, these technical uncertainties
lead to increased costs and represent additional economic challenges for a proceeding hydrogen market ramp-up
[8]. The lowest technical uncertainties are currently associated with alkaline water electrolysis (AWE) and proton
exchange membrane water electrolysis (PEMWE), which have the highest levels of technological readiness [9]. Both
technologies are attributed with different technical and economic properties. For instance, AWE is generally assigned
with lower investment cost and lower efficiency in the literature, whereas PEMWE is considered to be more expensive
yet more efficient [10]. Therefore, an advantage could result from the combination of both electrolyzer technologies
to benefit from the mentioned techno-economic differences, thus addressing technical and economic challenges [11].
∗Corresponding authors. Emails: marie.arnold@ewe.de, brandt@ifes.uni-hannover.de
arXiv:2607.06093v1  [cs.CE]  7 Jul 2026

Literature review
The techno-economic differences of AWE and PEMWE mentioned above form the basis of various studies that com-
pare both technologies. While Guo et al. [12] perform a review based comparison, Wang et al. [13] conducted an
experimental comparison and Munther et al. [14] simulated both technologies on a large scale. In all three studies,
investment cost and efficiency are assumed to be contrary for AWE and PEMWE as indicated above. This contrary
difference motivated several studies to examine both technologies within a hybrid electrolyzer system (HES), enabling
the aforementioned potential techno-economic advantages to be investigated. The objective of several of these stud-
ies is to optimize dispatch, while assuming a fixed, predefined design of the respective HES. As a result, Tan et al.
[11], Zhang et al. [15], Wang et al. [16] and Yang et al. [17] achieved a higher efficiency in hydrogen production.
Additionally, Tan et al. [11] reached higher revenues, which Yu et al. [18] did as well. Moreover, Yu et al. [18] found
a longer lifetime of the HES compared to the single AWE, respectively, PEMWE system. These techno-economic
advantages have also been identified in other studies that specifically focus on configuring the design of HES. Using
various optimization approaches, Hu et al. [10], Xu et al. [19], Shi et al. [20] and Tang et al. [21] come to the same
conclusion, in which the HES configuration contains a smaller proportion of PEMWE than AWE. Similar results are
found in Liang et al. [22] and Mingxuan et al. [23], which analyze various AWE and PEMWE ratio configurations
based on scenario analyses. A comparable approach is used in Shin et al. [24]; however, the most cost-effective
configuration identified in this study consists solely of PEMWE. This is also consistent with one finding in Ma et al.
[25], where different optimization methods were compared.
This clarifies that the results of studies on HES vary significantly depending on the underlying model assumptions
and that the selection of a HES does not necessarily correspond to the most techno-economic efficient solution.
Nevertheless, although the topic of HES has been widely studied, only Hu et al. [10] and Shin et al. [24] conducted
a compact sensitivity analysis of investment cost to verify their findings. Furthermore, current manufacturer data
sheets and literature references indicate that the contrary ratio between efficiency and investment cost cannot be
clearly attributed to the technologies AWE and PEMWE [26–34]. Thus, this study applies a comprehensive sensitivity
analysis varying both investment cost and efficiency to prove the profitability of HES independent of uncertain contrary
techno-economic properties of AWE and PEMWE. In addition, this study applies a free design optimization approach
that allows zero capacities and does not enforce the implementation of a HES. This technology-independent and
design-open approach enables a direct evaluation of whether HES represent a smart strategy or rather an economic
fallacy with negligible techno-economic benefits.
Aim and contribution
To answer this research question, we proceed as follows: Design and dispatch of an integrated hydrogen supply chain
including Power Purchase Agreement (PPA) contracting, two electrolyzers, hydrogen cavern storage and hydrogen
demand are optimized by a cost minimization. The methodology is presented in Section 2. An extensive sensitivity
analysis is conducted to comprehensively examine the model including the techno-economic feasibility of HES. The
underlying approach is described in the study design in Section 3, along with a guide through the result sections. Sec-
tion 4.1 initially presents a specific exemplary HES result to support the understanding of the model behavior. Section
4.2 contains the key results for the entire sensitivity analysis space comprising design optima as well as cost objective
for the comprehensive techno-economic investigation of HES. Also based on the sensitivity analysis methodology
conducted in this study, this section contains a quantitative deep dive into the trade-offbetween investment cost and
efficiency of a single electrolyzer system to provide a cost-based ratio of both parameters. Section 4.3 completes
the results by presenting the dispatch of single electrolyzer systems and HES, highlighting their differing operational
behavior and indicating how electrolyzers are optimally utilized under varying parameter conditions.
2

2. System under consideration
This study takes the perspective of a hydrogen provider that operates two electrolyzers integrated into a hydrogen
supply chain, which is shown in Figure 1. On the left, the renewable PPA options including onshore wind, offshore
wind and solar power are shown. In addition, the grid as an option for the surplus electricity sales is shown on this side.
In the middle, the electrolyzers are presented, which produce green hydrogen using the booked PPA capacities. The
produced hydrogen can then be injected into the hydrogen cavern storage or delivered directly to the customer having
a predefined hydrogen demand. Both last-mentioned components of the hydrogen supply chain are presented on the
right. In the following analysis, design and dispatch of this infrastructure are optimized according to Equation (1). The
corresponding optimization variables, grouped in vectorX, include the design of PPA options, electrolyzers and cavern
storage, as well as the dispatch of surplus sales, electrolyzer power and cavern storage utilization. These variables are
used to mathematically minimize total expenditures, which comprises PPA contracting costs (C PPA), cavern storage
booking and operating costs (CStorage) and the costs ofN∈{1,2}electrolyzer systems ( PNi=1 CiElectrolyzer), minus surplus
sales revenues (RSurplus).
min
X
CPPA +C Storage +
NX
i=1
CElectrolyzeri −R Surplus (1)
The solved optimization problem provides various variables of interest such as PPA and cavern storage sizing as well
as the sizing of one or two electrolyzer systems. These variables of interest are used to calculate the levelized cost of
hydrogen (LCOH), which serves as an indicator for the economic performance of the analyzed infrastructure. For this
purpose, the minimized annual costs are divided by the annual sum of the predefined hydrogen demand. Equation (2)
shows this calculation.
LCOH= CPPA +C Storage + PNi=1 CElectrolyzeri −R SurplusPT
t=1 ˙mDemandt ·∆t (2)
Figure 1: Set up of the system under consideration. The dashed box on the left shows the available power purchase options including onshore
wind, offshore wind and solar energy as well as the electricity grid. The middle dashed box presents two electrolyzer options. The right dashed
box shows the hydrogen cavern storage as well as a consumer characterized by a certain hydrogen demand. BB1 marks the electricity bus bar, BB2
marks the hydrogen bus bar.
3

The complete optimization problem formulation including all constraints is linear. The corresponding set of con-
straints is listed in Appendix A. The optimization time frame is one year with an hourly resolution, ensuring compli-
ance with European regulations for green hydrogen production [35]. The PPA options are pay-as-produced. To ensure
comparability within Europe, this study, using Germany as an example, assumes that no grid fees or taxes are charged
for the electrolyzer operation [36, 37]. Regarding the surplus sales, a constant pricing assumption is used. For both
electrolyzers, annualized installation cost occur. For simplicity, the electrolyzers are modeled as single stacks, omit-
ting any modular system architecture. The storage fees consist of bundled capacity booking plus operational costs.
The hydrogen demand is set to 5500 kg/h, which leads to a total electrolyzer capacity of approximately 500 MW
with 5000 full load hours (FLH), depending on the respective parameter assumptions. The constant hydrogen demand
assumption is representative of large-scale industrial applications, such as the chemical sector, which is one of the first
major consumers of domestically produced green hydrogen in Europe [38, 39]. Further information on the cost and
technical assumptions as well as the underlying capacity factor time series for the PPAs are provided in Appendix B.
All economic input parameters are set to present cost values derived from recent publications and converted into 2024
euros (€2024) using the Chemical Engineering Plant Cost Index (CEPCI) [40].
3. Study design
In this study a comprehensive sensitivity analysis is performed that varies both investment cost and efficiency of the
two electrolyzer options shown in Figure 1 to investigate the research question of HES as a smart strategy or an eco-
nomic fallacy. The investment cost correspond to the capital expenditures (CAPEX) and the efficiency corresponds
to the specific energy consumption (SEC) in the following. CAPEX have a direct impact on the total cost and ar
e measured in€/kW. The SEC’s cost influence is indirect, as it defines the energy consumption of the electrolyzer
in kWh per kg produced hydrogen. Thus, the higher the SEC, the more energy is needed for hydrogen production
and must be procured accordingly via PPAs. Therefore, the SEC’s cost impact is reflected in the PPA cost. For the
analysis of this study, both CAPEX and SEC are fixed for electrolyzer 1 to baseline values of 1450€/kW and 52
kWh/kg, respectively. Starting from this baseline, both parameters are varied between a 50% decrease and a 50%
increase for electrolyzer 2. The resulting parameter variation space is illustrated in Figure 2. CAPEX deviation of
electrolyzer 2 from electrolyzer 1 in % is shown on the y-axis. SEC deviation of electrolyzer 2 from electrolyzer
1 in % is shown on the x-axis. The dashed lines indicate where electrolyzer 2 has the same baseline CAPEX and
SEC value as electrolyzer 1. In the corners, the quadrants of the coordinate system are numbered. The light green
square marks the fixed baseline value of electrolyzer 1, the dark green arrows visualize the variation of electrolyzer 2.
For each parameter combination assigned to electrolyzer 1 and electrolyzer 2, the optimization problem described in
Section 2 is solved.
The following guide explains the structure of the subsequent analysis of the results from the parameter variation space.
First, a specific, exemplary HES result is shown and discussed regarding cost, design and dispatch in Section 4.1. This
ensures a detailed insight and understanding of the modeled hydrogen supply chain. Based on this knowledge, the
entire parameter variation space is examined in the next step. In Section 4.2, the key results regarding design and cost
are investigated first. This involves determining the resulting designs of all components of the considered hydrogen
supply chain as well as the cost objectiveLCOH. This analysis is complemented by an examination of the results
regarding the sensitivities energy price, storage fee, availability of RES and baseline SEC value. Independent of
HES, this section provides a deeper analysis of the cost ratio between CAPEX and SEC. The same methodology and
parameter variation space are considered for this purpose, but with focus on a single electrolyzer system. The result
is further evaluated with respect to the sensitivities energy price, storage fee, availability of RES and baseline SEC
value as well. Finally, beyond evaluating system design and cost, a detailed analysis of the electrolyzer operation
is conducted in Section 4.3 to understand the optimal dispatch behavior of HES and single electrolyzer systems.
The identified operational behaviors provide the basis for deriving fundamental techno-economic efficient operating
mechanisms.
4

Figure 2: Illustration of CAPEX/SEC parameter variation space. CAPEX deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the
y-axis. SEC deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the x-axis. The dashed lines mark where electrolyzer 2 has the same
CAPEX value respectively SEC value as electrolyzer 1. In the corners, the quadrants of the coordinate system are numbered. The light green
square marks the fixed baseline value of electrolyzer 1, the dark green arrows visualize the variation of electrolyzer 2.
4. Results and discussion
4.1. Exemplary hybrid electrolyzer system
This section presents and discusses an exemplary HES case to provide a detailed understanding of the modeled hy-
drogen supply chain described in Section 3. A representative data point located in quadrant II of the CAPEX/SEC
parameter variation space shown in Figure 2 is selected, resulting in a HES. Figure 3 presents the optimized cost,
design and dispatch of the exemplary HES. Figure 3 a) showsLCOHfor the exemplary HES and the next best single
electrolyzer system with respect to cost in comparison, Figure 3 b) shows the designs of the exemplary HES infras-
tructure, Figure 3 c) shows the power flows, Figure 3 d) shows the electrolyzer operation, Figure 3 e) shows the
hydrogen mass flows and Figure 3 f) shows the storage operation and dimension. In every subfigure, onshore wind is
presented in blue, solar power is presented in yellow, surplus power is presented in orange, electrolyzer 1 is presented
in light green, electrolyzer 2 is presented in dark green and storage is presented in brown.
TheLCOHin€/kgH2 are shown in Figure 3 a). The different cost components are stacked and visualized in different
colors for the exemplary HES on the left and for the next best single electrolyzer system on the right. The totalLCOH
resulting for the exemplary HES are 6.006€/kgH2. The biggestLCOHshare is given by the PPA cost of 3.5€/kgH2
followed by the total electrolyzer cost of about 1.7€/kgH2. The storage cost are approximately 0.8€/kgH2 and the
surplus revenues make up 0.07€/kgH2. In comparison, the total cost of the single electrolyzer system amounts to
6.010€/kgH2. Thus, the cost benefit of the exemplary HES over the single electrolyzer system is 0.004€/kgH2. The
higher cost of the single electrolyzer system result from higher total electrolyzer cost. The design of the exemplary
HES and the corresponding hydrogen infrastructure are shown in Figure 3 b). The left y-axis shows the dimension in
megawatts (MW) and the right y-axis shows the dimension in tonnes of hydrogen (t). The different component dimen-
sions are type-dependently stacked and visualized in different colors. On the left, the PPA dimensions are presented
consisting of onshore wind and solar power with a total dimension of about 1100 MW. The onshore wind dimension is
about 600 MW, which is slightly larger than the dimension of 500 MW solar power. In comparison, the resulting total
electrolyzer dimension presented in the middle is clearly smaller with in total 400 MW. This indicates a substantial
oversizing of booked PPAs compared to electrolyzer dimension, which is typical given the volatile nature of RES.
5

The dimension of electrolyzer 2 is approximately three times larger at 290 MW than the dimension of electrolyzer 1,
which is sized at 105 MW. On the right, the resulting storage capacity of about 2750 t is shown. The power flow is
shown in Figure 3 c), with the power in MW as a function of time in hours over a two-week period in summer. The
PPA power and the electrolyzer power are stacked independent of each other. The results show that electrolyzer 1
primarily operates during periods of peak solar power, while electrolyzer 2 operates more continuously. In addition,
solar power peaks often exceed the total electrolyzer capacity, resulting in surplus power. Therefore, surplus sales do
not appear to affect the electrolyzer dispatch. The electrolyzer operation is shown in Figure 3 d) in the form of annual
power duration curves (APDCs) of both electrolyzers, which present power as a function of sorted hours per year. The
operation of electrolyzer 2 is characterized by a continuous, base load behavior, reflected by 6272 FLH. Electrolyzer
1, by contrast, achieves approximately 1817 fewer FLH and predominantly operates during peak-load periods. This
underlines the operating behavior of the electrolyzers described in Figure 3 c). The mass flow is shown in Figure 3
e) by tonnes of hydrogen as a function of the same two-week period in summer as in Figure 3 c). The electrolyzer
mass flow is stacked. The mass flow shows that the storage injection periods correlate with the solar power periods
in Figure 3 c). This demonstrates the need for storage to balance short-term fluctuations in hydrogen production by
RES in order to meet the predefined constant hydrogen demand. However, storage is also required to compensate for
longer-term fluctuations in RES. For example, solar power generation is typically higher during summer months than
during winter. The impact of these long-term fluctuations is illustrated in Figure 3 f), which presents the storage level
and storage capacity in tonnes as a function of the hours of the year. Generally, the storage level increases during
summer period and decreases during winter period. This confirms the storage injection correlation with solar power
periods observed in Figure 3 e), as these periods are mostly given in summer. Moreover, Figure 3 f) demonstrates, that
the storage level never reaches the available storage capacity. This is due to the bundled marketing of storage capacity
and operation, as mentioned in Section 2. Further details on the optimization constraints are provided in Appendix A.
Overall, the detailed analysis of the exemplary HES case shows that the resulting system configuration and opera-
tion are consistent with the underlying techno-economic characteristics of the modeled supply chain. With respect to
LCOH, the difference between the HES and the single electrolyzer system is rather small. Furthermore, regarding the
operation of the HES, electrolyzer 2 tends to operate in base load behavior, whereas electrolyzer 1 operates rather in
peak load behavior. The subsequent analyses investigate these results across the entire parameter variation space for
verification and a more comprehensive understanding of these findings.
6

a)
Single system
3400 3450 3500 3550 3600 3650
Time (in h)
-200
0
200
400
600
800
Power (in MW)
Onshore Solar
Surplus Electrolyzer 2
Electrolyzer 1
c)
3400 3450 3500 3550 3600 3650
Time (in h)
2
3
4
5
6
7
8
9Mass ﬂow (in t)
Storage withdrawal
Storage injection Electrolyzer 2
Electrolyzer 1
Demand
e)
PPA Electrolyzer Storage
0
200
400
600
800
1000
1200Dimensioning  (in MW)
0
500
1000
1500
2000
2500
3000
Storage capacity (in t)
Onshore
Solar
Electrolyzer 2
Electrolyzer 1
Storage capacity
b)
0 2000 4000 6000 8000
Sorted hours per year
0
50
100
150
200
250
300
350Power (in MW)
Power Electrolyzer 2
Power Electrolyzer 1
Dimension Electrolyzer 2
Dimension Electrolyzer 1
FLH Electrolyzer 2
FLH Electrolyzer 1
d)
0 2000 4000 6000 8000
Time (in h)
0
500
1000
1500
2000
2500
3000Storage level (in t)
Storage level
Storage capacity
f)
Figure 3: Results of exemplary HES. a)LCOHof exemplary HES and single electrolyzer system. b) Dimensioning of the components of the
system under consideration: PPA and electrolyzers in MW and storage in tonnes (t). c) Hourly power flow in MW for a two week summer period.
d) Annual power duration curves for electrolyzer 1 and electrolyzer 2. e) Hourly hydrogen mass flow for a two week summer period. f) Storage
level and storage capacity in tonnes of hydrogen depending on the hours of one year.
7

4.2. System design and cost
This section investigates system design and cost for the entire parameter variation space based on the knowledge
gained from the exemplary HES analysis in Section 4.1. Figure 4 presents system design heat maps illustrated in
Figure 2 and described in Section 3. Every subfigure 4 a)-e) shows the CAPEX deviation of electrolyzer 2 from
electrolyzer 1 in % on the y-axis and the SEC deviation of electrolyzer 2 from electrolyzer 1 in % on the x-axis. The
dashed lines mark where electrolyzer 2 has the same CAPEX value respectively SEC value as electrolyzer 1. In the
corners, the quadrants of the coordinate system are numbered. Parameter combinations of CAPEX and SEC leading
to HES are marked by black dots. The exemplary HES result is marked by a red cross for orientation. The marked
HES regions are the same in every subfigure of Figure 4. Generally, HES result in quadrant II as well as in quadrant
IV . In quadrant II, SEC is decreased and CAPEX is increased for electrolyzer 2. Thus, electrolyzer 2 is more expen-
sive and more efficient in this area than electrolyzer 1. In quadrant IV , SEC is increased and CAPEX is decreased for
electrolyzer 2. Thus, electrolyzer 2 is less expensive and less efficient in this area than electrolyzer 1. Consequently,
HES result if the parameters of electrolyzer 1 and electrolyzer 2 are opposite. In total, the HES share is 3.3% of the
investigated cases. Electrolyzer 1 as a single system accounts for 47.4% of the parameter variation space. Electrolyzer
2 as a single system accounts for 49.3% of the parameter variation space. Thus, in total, shares of electrolyzer 2 are
higher than shares of electrolyzer 1. In comparison to single electrolyzer system shares, HES share is minor.
Figure 4 a) shows the dimensioning heat map of electrolyzer 1. Parameter combinations resulting in an electrolyzer 1
dimension of zero are visualized in white. The heat map shows a broad plateau in quadrant I, where only electrolyzer
1 is installed, with a constant dimension of about 430 MW. In this quadrant, electrolyzer 1 is more efficient and
less expensive than electrolyzer 2, which is why it is cost optimal as a single system. Entering the HES regions in
quadrants II and IV , the size of electrolyzer 1 decreases. The decline in electrolyzer 1 size is steeper in quadrant II than
in quadrant IV . This indicates that the more efficient electrolyzer 2 dominates the sizing decision in the HES region of
quadrant II. In contrast, electrolyzer 1 dominates the sizing decision in the HES region of quadrant IV due to its higher
efficiency. Consequently, in a HES configuration, the more efficient electrolyzer is assigned a larger dimension than
the less efficient one. This indicates a higher SEC impact compared to CAPEX. Figure 4 b) shows the dimensioning
heat map of electrolyzer 2. Parameter combinations resulting in an electrolyzer 2 dimension of zero are visualized
in white. In quadrant III, electrolyzer 2 is installed as a single electrolyzer system because it is both less expensive
and more efficient. The size of electrolyzer 2 increases slightly with increasing SEC. The largest size of electrolyzer
2, and the largest electrolyzer size overall, occurs in quadrant IV left next to the HES region, reaching approximately
470 MW. When entering the HES regions, the size of electrolyzer 2 decreases. This trend in quadrant II and quadrant
IV is consistent with the behavior observed for electrolyzer 1. This observation further confirms the dominant impact
of SEC on electrolyzer sizing. Figures 4 c) and d) present dimensioning heat maps of the PPA options onshore wind
and solar power. In general, solar power dimension is about 100 MW smaller than onshore wind power dimension,
which is similar to the finding in Section 4.1. Both heat maps demonstrate a similar sizing trend, with the largest
sizes occurring at low SEC values and further increasing as SEC increases. Thereby, the onshore power size varies
more than the solar power size across the entire parameter variation space. Notably, both heat maps exhibit a peak
in the same region in quadrant IV where electrolyzer 2 reaches its maximum size, as shown in Figure 4 b). In this
region, the maximum electrolyzer size leads to the highest PPA demand. Figure 4 e) shows the storage dimensioning
in tonnes of hydrogen. Generally, the variation in the storage dimension resulting from variations in CAPEX and
SEC is relatively small, with a maximum difference of 3 t, corresponding to only 0.1% of the maximum storage size
of 2729,6 t. This maximum occurs at lowest SEC and CAPEX values, where PPA size is minimal. For increasing
SEC and CAPEX values, the storage size decreases within the regions of the single electrolyzer system. The smallest
storage dimensions are given in both HES regions. This suggests, that HES configurations can slightly reduce storage
requirements, potentially due to the increased operational flexibility provided by the combination of both electrolyzer
systems.
8

II
III IV
I
-50% -25% 0% +25% +50%
SEC deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
-50%
-25%
0%
+25%
+50%CAPEX deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
Electrolyzer 2 = Electrolyzer 1 (SEC)
Electrolyzer 2 = Electrolyzer 1 (CAPEX)
0
50
100
150
200
250
300
350
400
450
Dimension of Electrolyzer 1 (in MW)
Hybrid electrolyzer system
Exemplary HES result
a)
II
III IV
I
-50% -25% 0% +25% +50%
SEC deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
-50%
-25%
0%
+25%
+50%CAPEX deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
Electrolyzer 2 = Electrolyzer 1 (SEC)
Electrolyzer 2 = Electrolyzer 1 (CAPEX)
300
350
400
450
500
550
600
650
700
Onshore nominal power (in MW)
Hybrid electrolyzer system
Exemplary HES result
c)
II
III IV
I
-50% -25% 0% +25% +50%
SEC deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
-50%
-25%
0%
+25%
+50%CAPEX deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
Electrolyzer 2 = Electrolyzer 1 (SEC)
Electrolyzer 2 = Electrolyzer 1 (CAPEX)
2727
2727.5
2728
2728.5
2729
2729.5
Storage capacity (in t)
Hybrid electrolyzer system
Exemplary HES result
e)
II
III IV
I
-50% -25% 0% +25% +50%
SEC deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
-50%
-25%
0%
+25%
+50%CAPEX deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
Electrolyzer 2 = Electrolyzer 1 (SEC)
Electrolyzer 2 = Electrolyzer 1 (CAPEX)
0
50
100
150
200
250
300
350
400
450
Dimension of Electrolyzer 2 (in MW)
Hybrid electrolyzer system
Exemplary HES result
b)
II
III IV
I
-50% -25% 0% +25% +50%
SEC deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
-50%
-25%
0%
+25%
+50%CAPEX deviation of Electrolyzer 2 from Electrolyzer 1 (in %)
Electrolyzer 2 = Electrolyzer 1 (SEC)
Electrolyzer 2 = Electrolyzer 1 (CAPEX)
300
350
400
450
500
550
600
650
700
Solar nominal power (in MW)
Hybrid electrolyzer system
Exemplary HES result
d)
Figure 4: Heat maps of hydrogen infrastructure component designs for the entire parameter variation space. CAPEX deviation of electrolyzer 2
from electrolyzer 1 in % is shown on the y-axis. SEC deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the x-axis. The dashed lines
mark where electrolyzer 2 has the same CAPEX, respectively SEC value as electrolyzer 1. CAPEX/SEC parameter combinations leading to HES
are marked by black dots. The exemplary HES result is marked by a red cross. (a) Dimension heat map of electrolyzer 1 in MW. (b) Dimension
heat map of electrolyzer 2 in MW. (c) Dimension heat map of onshore wind power in MW. (d) Dimension heat map of solar power in MW. (e)
Dimension heat map of storage capacity in t.
9

Having discussed the system design, the corresponding cost results of the HES are now analyzed across the entire pa-
rameter variation space. Figure 5 presents the resultingLCOHintroduced in Equation 2 and the cost benefit of HES.
Figure 5 a) shows theLCOHheat map, equivalent to the presentation of the design heat maps in Figure 4. A plateau
of the highestLCOHof about 6€/kgH2 are observed in yellow in the same region in quadrant I as the plateau of the
electrolyzer 1 dimension shown in Figure 4 a). The lowestLCOHof approximately 3.5€/kgH2 occur for the lowest
SEC and CAPEX values in quadrant III. Although increases in both SEC and CAPEX lead to higherLCOH, the effect
of SEC is considerably more dominant than that of CAPEX. This indicates a generally higher impact of SEC on the
economics of the system under consideration. Independent of the specific characteristics observed in the subfigures
of Figure 4 with respect to the dimensioning of the system components, the increase inLCOHremains continuous
across the parameter variation space. For example, the region in quadrant IV with the highest overall electrolyzer and
PPA dimensions does not correspond to the region with the highestLCOHvalues. This suggests that no single design
characteristic dominates the overall cost performance. The indicates that the combined effects of the different design
characteristics tend to offset each other, resulting in the continuousLCOHgradient observed across the parameter
space. Figure 5 b) and c) show theLCOHbenefit of the HES relative to the cheapest single electrolyzer system. The
LCOHbenefit is calculated by comparing theLCOHof each HES configuration with those of both single electrolyzer
systems and selecting the minimum difference. Negative values indicate a cost benefit of the HES, meaning that the
hybrid configuration achieves lower hydrogen production costs than the cheapest single electrolyzer system. Figure 5
b) presents the HES region in quadrant II. The maximumLCOHbenefit of 0.02€/kgH2 occurs for CAPEX values of
+45% and above. Figure 5 c) presents the HES region in quadrant IV . The maximumLCOHbenefit of 0.048€/kgH2
occurs for CAPEX values of -47% and below. Both CAPEX values represent outliers with regard to recent literature
references.
10

a)
b)
c)
Figure 5:LCOHheat map andLCOHbenefit. CAPEX deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the y-axis. SEC deviation
of electrolyzer 2 from electrolyzer 1 in % is shown on the x-axis. CAPEX and SEC parameter combinations leading to HES are marked by black
dots. The exemplary HES result is marked by a red cross. a)LCOHheat map in€/kgH2. The dashed lines mark where electrolyzer 2 has the same
CAPEX value respectively SEC value as electrolyzer 1. b)LCOHbenefit of quadrant II in€/kgH2. c)LCOHbenefit of quadrant IV in€/kgH2.
To get a comprehensive picture of these results, Figure 6 presents theLCOHbenefit for varying PPA prices in quad-
rant II and quadrant IV . Subfigures a)–e) correspond to quadrant II and subfigures f)–j) to quadrant IV , each showing
PPA price variations of -60%, -30%, 0%,+30%, and+60%. Accordingly, Figure 6 c) and h) show the same as Figure
5 b) and c). Regarding theLCOHbenefits, the maximum of 0.048€/kgH2 is observed in Figure 6 h) without PPA
price variation, showing the results for the base PPA price assumption already presented in Figure 5 c). Regarding the
appearance of the HES regions in quadrant II, a tilt to the left is notable for lower PPA values in a) and b), as well as a
tilt to the right for higher PPA values in d) and e). The opposite behavior is visible for the HES region in quadrant IV .
11

These tilting effects result from changes in the relative techno-economic relevance of SEC and CAPEX with varying
PPA price. For lower PPA values, the optimization increasingly favors lower CAPEX over lower SEC. Consequently,
in quadrant II, electrolyzer 1 with the lower CAPEX value compared to electrolyzer 2 becomes more favorable, shift-
ing the HES region to the left and reducing the single electrolyzer 2 region. In quadrant IV , the opposite effect occurs,
shifting the HES region to the right and reducing the single electrolyzer 1 region. For higher PPA values, however,
SEC becomes more techno-economically relevant and CAPEX become less relevant, resulting in the opposite shifting
and tilting behavior.
In addition to the discussed PPA price variation, Figure 7 presents theLCOHbenefit of varying the baseline SEC
values following the same presentation as in Figure 6. However, the baseline SEC fixed for electrolyzer 1 is only
varied within a range of±30% relative to the baseline introduced in Section 3, since larger deviations would not be
technically feasible. The maximumLCOHbenefit of 0.057€/kgH2 is observed in Figure 7 f) for a baseline SEC
increase of 30%. As the baseline SEC increases from -30% to+30%, the HES regions in both quadrants decrease
considerably, from approximately 5.0% to 2.5%. Concurrently, the shares of both single electrolyzer systems increase
steadily, with electrolyzer 1 increasing from 46.3% to 47.8% and electrolyzer 2 from 48.7% to 49.7% across the same
baseline SEC range. This behavior can be explained by the parameterization of the SEC variation. Since the SEC of
electrolyzer 2 is defined as a relative deviation from the baseline SEC fixed to electrolyzer 1, a lower baseline SEC
results in smaller SEC differences between both technologies, whereas a higher baseline SEC leads to larger SEC dif-
ferences. Consequently, for lower baseline SEC values and smaller SEC differences, HES become economically more
favorable leading to an increasing HES share. In contrast, for higher baseline SEC values and larger SEC differences,
single electrolyzer systems become economically more favorable leading to a decreasing HES share. In contrast to
the effects discussed for the PPA price variation, neither a tilting nor a shifting effect is present here.
a)
b)
c)
d)
e)
f)
g)
h)
i)
j)
Figure 6:LCOHbenefit of HES depending on PPA price variation. CAPEX deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the
y-axis. SEC deviation of electrolyzer 2 from electrolyzer 1 in % is shown on the x-axis. The dashed lines mark where electrolyzer 2 has the same
CAPEX value respectively SEC value as electrolyzer 1. CAPEX and SEC parameter combinations leading to HES are marked by black dots. The
exemplary HES result is marked by a red cross. For HES results,LCOHbenefit in€/kgH2 is shown. Labeled contour lines clarifyLCOHbenefit
values. a) Quadrant II is shown for a PPA deviation of -60%. b) Quadrant II is shown for a PPA deviation of -30%. c) Quadrant II is shown for
no PPA deviation. d) Quadrant II is shown for a PPA deviation of+30%. e) Quadrant II is shown for a PPA deviation of+60%. f) Quadrant IV
is shown for a PPA deviation of -60%. g) Quadrant IV is shown for a PPA deviation of -30%. h) Quadrant IV is shown for no PPA deviation. i)
Quadrant IV is shown for a PPA deviation of+30%. j) Quadrant IV is shown for a PPA deviation of+60%.
12
