---
source_id: "lemigas-scog"
title: "An Integrated Analysis Approach for Identifying Water Influx Mechanism in Gas Well TMG Case Study"
summary: "Case study of a directional gas well that uses a quantitative workflow to tell water coning, channelling and aquifer movement apart as the cause of water production."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2139"
retrieved_at: "2026-10-24T14:29:52+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "2d0467c5eaf75a11cbda524a7e7615417f917c73c92826ac67732e2771914ce5"
collected: "manual"
---

# An Integrated Analysis Approach for Identifying Water Influx Mechanism in Gas Well TMG Case Study

257 
 
https://doi.org/10.29017/scog.v49i3.2139 
 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 257 – 277 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
An Integrated Analysis Approach for Identifying Water Influx 
Mechanism in Gas Well: TMG Case Study 
 
Tjok Gede Satryangga1,2*, Amega Yasutra1, Dedy Irawan1, Amritzar Aimar2, and Seno Kushidayat2 
 
1Petroleum Engineering, Faculty of Mining and Petroleum Engineering, Institut Teknologi Bandung, 
Ganesa Street No. 10, Bandung, West Java, 40132, Indonesia. 
2Foster Oil & Energy Pte Ltd., Sampoerna Strategic Square Building 
Jenderal Sudirman Street Kav. 45-46, South Jakarta, DKI Jakarta, Indonesia. 
*Corresponding author: Tjok Gede Satryangga (22224305@mahasiswa.itb.ac.id) 
Received: 13 February 2026; Revised: in revised form 29 May 2026; Accepted: 31 July 2026 
Available: online 30 September 2026. 
  
 
ABSTRACT - Produced water is a primary operational challenge in gas fields, as it can restrict gas flow and 
severely reduce well productivity. Diagnosing and identifying water influx sources in directional gas wells is 
critical to mitigating this phenomenon and optim izing well performance. This study details a quantitative 
workflow evaluating water -gas production dynamics to identify key drivers of water influx, water coning and 
channeling. Furthermore, it determines whether the reservoir aquifer boundary h as shifted. This study uses 
algorithms derived from classical model water-to-gas ratio diagnostic, reservoir and geological evaluations based 
on the transient analysis radius of investigation and predictive models to forecast cumulative gas production at 
breakthrough. By analyzing data from 4 wells, this study demonstrates that water -gas ratio trends and transient 
pressure behaviors can accurately classify fluid boundary geometries. Driven by localized reservoir 
heterogeneities and declining pressures, these dynamics accelerate water encroachment. This process culminates 
in water breakthrough, as confirmed by diagnostic log -log signatures of water channeling and water coning late 
channeling. The established method provides robust diagnostics for identifying produced water sources and 
improving predictive accuracy, directly guiding effective well management and field development strategies. 
Keywords: gas rate, water rate, drive mechanism, water gas -ratio, water -bearing zone, pressure derivative, 
heterogeneity, water breakthrough, water influx, water channeling, water coning. 
How to cite this article: 
Tjok Gede Satryangga, Amega Yasutra, Dedy Irawan, Amritzar Aimar, and Seno Kushidayat , 2026, An 
Integrated Analysis Approach for Identifying Water Influx Mechanism in Gas Well: T MG Case Study, 
Scientific Contributions Oil and Gas, 49 (3) pp. 257-277.

258 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
1. Introduction 
One of the major challenges in oil and gas operations is the entry of produced water into the wellbore from 
hydrocarbon-bearing reservoirs. This encroaching water may be associated with the vertical migration of the water 
contact toward perforation, a phen omenon known as water coning, or with the rapid intrusion of water from an 
aquifer that bypasses the hydrocarbon zone, referred to as water channeling. Both phenomena are common and 
can significantly detract from overall well productivity. 
This condition was validated at a research site within the West Java Basin. The TMG field is an active gas 
asset featuring four production wells with an average daily gas rate ( qg) of 12 MMscfd. This field's reservoir 
comprises middle shoreface bioclastic carbonate rocks of the Upper Cibulakan Formation (Reksalagora 1996) . 
High localized drawdown gradients established during production have accelerated water production across 
this sector.  
The production history of the TMG field from 2016 to 2025 exhibits a steady increase in dry gas production, 
followed by a subsequent rise in produced water volume. This behavior stems from declining reservoir pressure, 
which suppresses gas production while  water volumes continue to escalate (Figure 1). These trends support the 
hypothesis that water influx originates from an active bottom-water or edge-water drive, triggering localized water 
coning or channeling. Consequently, the affected gas wells lose the critical velocity required to lift liquids, causing 
fluids to accumulate at the bottom of the borehole and induce liquid loading. 
 
Figure 1. 
Profile production of TMG field 
Given this context, this research proposes an efficient solution to address the challenges associated with 
produced water influx in gas wells. This study applies a variety of empirical approaches to determine water 
production mechanisms, explicitly charact erizing active water channeling and coning behaviors in wells 
experiencing water breakthrough.  
 
 
 
0.00
100.00
200.00
300.00
400.00
500.00
600.00
0.00
2000.00
4000.00
6000.00
8000.00
10000.00
12000.00
14000.00
14/04/2016 14/04/2017 14/04/2018 14/04/2019 14/04/2020 14/04/2021 14/04/2022 14/04/2023 14/04/2024
Water Rate (BWPD)
Gas Rate (MSCFD)
Date
Gas rate Water rate
2 Wells
3 Wells 4 Wells

259 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
2. Methodology 
The study methodology is designed as an integrated workflow to identify water production mechanism, 
ultimately improving well production performance and reservoir development planning. This systematic approach 
is categorized into four primary stages:  
• Data acquisition 
• Diagnostic reservoir analysis 
• Diagnostic water production from wells 
• Reservoir and water production analysis Integration 
Figure 2 outlines the integrated workflow for the TMG field case study, which begins with a data acquisition 
phase. During this phase, quality control measures were applied to reservoir pressures, temperatures, fluid 
compositions, production histories, core analyses, and well logs to ensure data integrity. This research is divided 
into two primary sections: reservoir analysis and produced water evaluation. The reservoir analysis investigates 
reservoir drive mechanism identification, fluid types, fluid flow dynamics , and the prediction of cumulative gas 
production at breakthrough using a pressure derivative behavior model. Meanwhile, the produced water evaluation 
determines water influx mechanisms and sources, utilizing water -gas ratio (WGR) analysis to define water -
bearing gas zones and identify coning and channeling signatures.  
The results of both analyses are combined during the reservoir and water production  integration phase. 
This phase evaluates the water production signatures displayed on the log -log plots, which are characterized 
as water coning, channeling, or normal disp lacement. Furthermore, the source of produced water is 
determined using daily gas and water production histories, log -log water -gas ratio (WGR) plots, and 
cumulative gas ( Gp) versus cumulative water production ( Wp) plots. These diagnostics help identify wh ether 
the asset is a pore -water, bottom -water, or edge -water gas reservoir, which is subsequently used to predict 
cumulative gas production at a breaktrough.  
The comprehensive sequence of this study is shown in the following flow diagram (Figure 2).   
 
 
Figure 2. 
Flowchart of study 
Study Gase 
(TMG Field)
Data Acquisition
Reservoir Analysis Water Production from Wells 
Log & Well 
Integrity
Chan 
Diagnostic
Reservoir & Water Production 
Analysis Intergration
Result & Recommendation
Drive MechanismPVT W-B-G 
klasifikasi
Contact basis PTA

260 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
3.1 Data acquisition  
The datasets for this research comprise subsurface and production records. The primary inputs include daily 
gas and water production rates, tubing and wellhead pressures, and cumulative fluid volumes. These are supported 
by reservoir pressure and temperature measurements, core data (RCAL and SCAL) were incorporeted fluid and 
reservoir properties parameters. 
3.2 Diagnostic reservoir analysis 
Understanding the significance and types of reservoir drive mechanisms in actively producing gas fields is 
crucial, as they directly dictate the production behavior of the field under study. Typically, volumetric gas 
reservoirs are produced primarily throu gh the expansion of the gas contained within the formation. Because 
natural gas is significantly more compressible than connate water and the underlying aquifer, gas expansion serves 
as the dominant drive mechanism. However, depending on the characteristic s and geometry of the reservoir and 
aquifer, the primary depletion drive may shift toward a water -drive mechanism with varying drive indices (Fan 
2017). A 𝑃/𝑍 vs. 𝐺𝑝 plot is widely used to identify aquifer water influx. In a purely volumetric reservoir, the 
relationship between 𝑃/𝑍 and cumulative gas production ( 𝐺𝑝) is linear; any deviation from this straight line 
indicates the presence of water intrusion. Once water intrusion is established using the 𝑃/𝑍 vs. 𝐺𝑝 plot, the next 
step is to construct a Cole Plot, which provides greater sensitivity for identifying the reservoir's dominant drive 
mechanism. Figure 3 illustrates the relationship between 𝑃/𝑍 and 𝐺𝑝, as well as the corresponding Cole Plot. 
 
Figure 3 
General shapes of P/Z Vs Gp (a) and Cole plot as a function of aquifer strength (a) (Fan 2017) 
Another key feature that must be determined in long -term producing gas fields is the classification of the 
source water -gas zone. This classification can be determined from production behavior.  The water -gas ratio 
approach can categorize produced water sources based on structural geometry into bottom -water configurations 
with large contact area or edge-water configurations with smaller contact areas (Figure 4); both types are closely 
related to localized reservoir characteristics (Gao 2023). 
Figure 4b illustrates a bottom water gas reservoir, which features a sudden initial increase and a steady rise 
in the water -gas ratio (WGR) due to a clearly defined underlying aquifer contact boundary. Conversely, if the 
trend is gradual characterized by a low init ial WGR followed by a rapid escalation as gas production declines, 
and culminating in a stabilized, steady rise at late times the water source is classified as an edge -water gas 
reservoir (Figure 4a). In this configuration, the water contact boundary is structurally smaller than the reservoir 
boundary itself.  
A major challenge in the gas field is that when a gas reservoir is supported by a strong water-drive mechanism, 
it drives the migration of the gas -water contact, complicating reservoir development. Yaich (2012) developed a 
model to detect the presence and position of the fluid contact as a boundary observable through pressure derivative 
behavior in pressure transient analysis (PTA). Through this approach, the migration of the gas -water contact can 
(a) (b)

261 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
be extrapolated to predict cumulative gas production at the onset of water breakthrough. However, this predictive 
model must first classify the specific water -bearing gas zone, as the classification dictates the subsequent 
governing equations. Yaich (2012)  proposed two analytical models: the dome model, which accounts for 
simultaneous lateral water movement and bottom -water encroachment, and the tilted model, which assumes 
purely lateral water influx. In the tilted model, cumulative production is proportion al to the square of the 
equivalent radius, as illustrated in Figure 5 and Figure 6.  
The gas -water contact acts as a constant -pressure boundary within a radial composite reservoir model; 
thus, if the pressure derivative exhibits a slope deviation, it indicates migration of this fluid interface. This 
transient behavior is governed by the mo bility ratio (M), defined as the ratio of gas mobility to water mobility 
based on their respective effective permeabilities and fluid viscosities. The mobility ratio can be determined 
using the Equation 1. 
𝑀 =  
(𝑘/𝜇)𝑔𝑎𝑠
(𝑘/𝜇)𝑤𝑎𝑡𝑒𝑟
        (1) 
 
To quantitatively assess the movement of the GWC, (Yaich 2012) used the equivalent radius, which is  a circle 
with an area equal to that enclosed by the GWC in model. The equation for the equivalent radius is  
𝑟𝑒 = √
𝐴𝐺𝑊𝐶
𝜋         (2) 
 
The area (A) corresponds to a circle of radius (𝑟𝑖), determined from the radius equation. Quantitative 
calculation are then applied to extrapolate the cumulative gas prediction at breakthrough using either a conical or 
cylindrical water-influx model. 
 
𝐺 = 𝑉𝑖𝑛𝑖 − 𝑉𝑟𝑒𝑚𝑎𝑖𝑛 =  
𝜋.𝑟𝑖2.ℎ.∅.(𝑆𝑔𝑖−𝑆𝑔𝑟) 
𝐵𝑔
−
𝜋.𝑟𝑖2.ℎ.∅.(𝑆𝑔𝑖−𝑆𝑔𝑟) 
𝐵𝑔
 = 𝐴 + 𝐵. 𝑟𝑖2 (3) 
 
The equation for the conical model can be derived; 
 
𝐺 = 𝜋. 𝑟𝑖2. ℎ. ∅. (𝑆𝑔𝑖 − 𝑆𝑔𝑟) 𝐵𝑔 . − 𝜋. 𝑟𝑖2. ℎ. ∅. (𝑆𝑔𝑖 − 𝑆𝑔𝑟) 𝐵𝑔  
 
Since    
 
ℎ𝑡  =  𝑟𝑡. 𝑡𝑎𝑛 𝜃 
 
Therefore  
𝐺 =  𝐴 + 𝐵. 𝑟𝑖3       (4) 
 
Identifying water production mechanisms is essential to understand influx sources and optimize reservoir 
management. To improve well performance and reservoir development planning in the TMG field, this study 
implements an integrated analytical modeling approach to resolve these operational challenges.

262 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
 
 
 
 
 
Figure 4. 
Water bearing gas zone clasification. Edge water gas reservoir (a) and bottom water gas reservoir (b) (Gao 2023) 
 
 
(a) 
(b)

263 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
  
 
 
Figure 5. 
Tilted model derivative response a (Yaich 2012)

264 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
 
 
 
 
   
  
 
  
  
 
 
 
 
 
  
 
  
  
 
 
 
 
 
 
 
 
 
Figure 6 
Dome model derivative response (Yaich 2012)

265 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
3.3 Diagnostic water production from wells 
Al-Ghanim (2010) introduced this approach by expanding Chan's (1995) paradigm. Al-Ghanim (2010) noted 
that water production sources can be identified using the X-plot technique for production efficiency. Additionally, 
time-series data of water-to-oil or water-to-gas ratios versus production time, as introduced by Egbe (2005), can 
be utilized. This is integrated with numerical simulation studies evaluating log -log plots of the water -to-oil and 
water-to-gas ratios (WOR/WGR) and their time derivatives (dWOR/dt or dWGR/dt) to distinguish between 
coning and channeling mechanisms (Chan 1995) . However, in the case study by Al-Ghanim (2010) , it was 
established that Chan's (1995), diagnostic plotting technique provides the most practical and efficient strategy for 
analyzing rapid water encroachment and selecting precise water control treatments. This approach utilizes the 
water-gas ratio (WGR) and its derivative (WGR’) as primary indicators (Figure 7). The resulting log -log plot 
categorizes production behavior into normal displacement, water coning, or water channeling signatures based on 
WGR trends over time, while the WGR' derivative serves to isolate the exact onset of excessive water production. 
 
  
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 Figure 7 
Diagnosing reservoir mechanism based on log-log plot WOR and dWOR/dt Normal displacement (a), water coning (b), 
water channeling (c), water coning late channeling (d) based on log log plot WGR'/dt (Al-Ghanim 2010). 
 
 
(a) 
 (b) 
(c) 
 (d)

266 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
The mechanism can be diagnosed using the equation for finding the derivative WGR, where  
 
𝑑𝑊𝐺𝑅
𝑑𝑡 =
𝑊𝐺𝑅𝑖+1(𝑡𝑖−𝑡𝑖−1)+𝑊𝐺𝑅𝑖−1(𝑡𝑖−𝑡𝑖+1)+𝑊𝐺𝑅𝑖(𝑡𝑖−1−𝑡𝑖+1)
(𝑡𝑖+1−𝑡𝑖−1)(𝑡𝑖−𝑡𝑖−1)(𝑡𝑖−𝑡𝑖+1)    (5) 
 
For normal displacement, the dWGR/dt curve exhibits a flat trend. In contrast, during water coning, the 
dWGR/dt derivative decreases, showing a distinct negative slope pattern. Finally, a steep positive slope on the 
derivative curve indicates a water chann eling mechanism. During water coning with late channeling, the initial 
portion of the derivative curve (dWGR/dt) exhibits a downward or fluctuating negative slope. The derivative curve 
subsequently reverses, showing a distinct positive trend at late times (Al-Ghanim 2010). 
2.1 Reservoir and water production analysis Integration 
The integrated analysis of reservoir behavior and produced water is essential for accurately identifying drive 
mechanisms, refining original hydrocarbon -in-place estimates, and predicting water breakthrough. This 
predictive capability enables proactive dra wdown management and zone isolation before liquid loading occurs 
in the wellbore.  
 
3. Result and discussion 
A preliminary reservoir analysis was performed to evaluate drive mechanisms using the ( P/Z) method. The 
material balance calculation utilized the gas compressibility factor (z), reservoir pressure (Pi), and cumulative gas 
production (Gp). The plot of P/Z versus cumulative gas production (Fan 2017) shows a deviates from a straight 
line (Figure 8), showing the presence of water influx. A Cole plot can be used to determine the type of driving 
mechanism reservoir, where the cumulative relationship between gas and reserves suggests that the TMG field is 
moderate-strong water drive. 
 
 
Figure 8 
Reservoir drive mechanism in TMG Field. 
Presence of water drive based on (a) P/Z vs Gp and strong drive based on (b) Cole Plot  
(a) 
(b)

267 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
The analysis confirms a moderate-to-strong water drive mechanism, while the steady rise in water production 
indicates that water influx has already occurred. According to (Gao 2023), water-gas ratio (WGR) behavior can 
be used to identify water -bearing zones in gas reservoirs. Characterizing these zones plays a critical role in 
optimizing the development of the TMG field, particularly in improving well placement and perforation design  
for new wells. Based on the water and gas production behavior in well TMG -03 (Figure 9a), the water-bearing 
zone was characterized as an edge water -gas reservoir, as evidenced by a gradual, steady increase in the water -
gas ratio (Figure 9b) . Furthermore, the plot of cumulative gas versus cumulative water production exhibits a 
distinct two-phase trajectory. Initially, cumulative gas rises rapidly while water production remains negligible a 
phase known as the “water -free gas recovery stage.” F ollowing water breakthrough, water production escalates 
while the gas production rate declines, marking the “increasing WGR phase.” Following the increasing WGR 
phase, the water -gas ratio stabilizes as cumulative water production continues to rise, establi shing a linear 
relationship between cumulative gas and cumulative water during this stable WGR stage (Figure 9c). 
The classification of edge-water gas reservoirs is directly governed by their varied reservoir properties. Based 
on the porosity -permeability relationship derived from core data, the TMG gas reservoir exhibits significant 
heterogeneity, divided the formati on into multiple distinct rock types. These reservoir characteristics can 
accelerate the migration of encroaching water into the wellbore. This is further supported by the pressure 
derivative interpretation, which shows a sharp decline followed by an upwar d turn in the late -time region, 
indicating the presence of an active, encroaching aquifer boundary. This investigation was conducted utilizing 
well test data from well TMG -03 across both the pre -production phase and the subsequent gas and water co -
production period.  
Initial PBU data (Figure 10a) collected prior to gas production show a sharp downward turn in the late -time 
pressure derivative. This decline indicates a pressure maintenance boundary, likely marking the initial gas -water 
contact (GWC). Based on the onset of these boundary effects, the radius of investigation was calculated as 886 ft. 
According to recent PBU data (Figure 10b), the pressure derivative declines before turning upward in the late -
time region; this trend suggests the presence of an outer boundary, such as a fault or localized reservoir 
heterogeneity. As shown in Figure 11, well TMG-03 is separated from wells TMG-01, TMG-04 and TMG-02 by 
a fault. Evaluation of the fault seal using the Shale Gouge Ratio (SGR) Equation from (Yielding 2002) reveals a 
shale ratio of less than 15%, indicating that the fault is non-sealing and may allow fluid communication. 
Core data shows that the relationship between porosity and permeability reflects high reservoir heterogeneity. 
Figure 12 illustrates how the data distribution forms multiple distinct trends or clusters, representing variations in 
reservoir rock types. When modeling permeability, rock types with overlapping distributions are consolidated into 
a single Hydraulic Flow Unit (HFU). Consequently, Figure 13 depicts the cross-sectional and vertical distribution 
of the reservoir permeability and rock type model. 
Reservoir heterogeneity directly influences aquifer dynamics; a high permeability path connected to an aquifer 
with a strong water -drive mechanism accelerates water encroachment. This behavior is reflected in the pressure 
derivative curve 10b, indicating that the initial gas -water contact (GWC) boundary has shifted. Under these 
conditions, the radius of investigation was calculated as 694 ft. Figure 14 shows the projection of this calculated 
radius into the depth structure map. 
Flow resistance is proportional to the fluid mobility ratio (M). Using Equation 1, this reservoir is calculated to 
have a mobility ratio (M) of 30, indicating that the water rate more easily than gas. Water breakthrough can be 
predicted quantitatively usin g the Yaich (2012)  methodology. This predictive model incorporates the 
classification of the water -bearing zone, the severe water production observed in well TMG -03 and pressure 
derivative interpretations indicating fluid contact may be shifting. The quantify the movement o f the water zone 
contact boundary, Equation 2 is used to calculate the equivalent radius (re), which is then plotted against 
cumulative gas production (Gp). Assuming a cylindrical geometry (Equation 3), cumulative production scales 
proportionally with 𝑟𝑒2. This model serves to calculate water breakthrough driven by lateral water influx in an 
edge-water gas reservoir. Table 1 depicts the initial contact boundary at a radius of 886 ft prior to gas production, 
as well as its progression to a radius of 694 ft during the gas production period.

268 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
 
 
Figure 9. 
 Dynamic curves gas and water production in the TMG-03 well. 
(a) Curve daily gas and water production, (b) Water gas ratio, (c) relationship cumulative gas (Gp) and cumulative water production (Wp) 
0
50
100
150
200
250
300
350
400
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Water Production (bbl)
Gas Production (MMscfd)
Date
Production Performance TMG-03
Gas Rate
Water Rate
0.04
0.35
3.50
bbl/mscfd
Date
WGR TMG-03
WGR
TMG-03
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.00 200.00 400.00 600.00 800.00 1000.00 1200.00 1400.00 1600.00
Wp (mmstb)
Gp (mmscf)
Relationship between Gp and Wp 
0
50
100
150
200
250
300
350
400
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Water Production (bbl)
Gas Production (MMscfd)
Date
Production Performance TMG-03
Gas Rate
Water Rate
0.04
0.35
3.50
bbl/mscfd
Date
WGR TMG-03
WGR
TMG-03
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.00 200.00 400.00 600.00 800.00 1000.00 1200.00 1400.00 1600.00
Wp (mmstb)
Gp (mmscf)
Relationship between Gp and Wp 
0
50
100
150
200
250
300
350
400
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Water Production (bbl)
Gas Production (MMscfd)
Date
Production Performance TMG-03
Gas Rate
Water Rate
0.04
0.35
3.50
bbl/mscfd
Date
WGR TMG-03
WGR
TMG-03
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.00 200.00 400.00 600.00 800.00 1000.00 1200.00 1400.00 1600.00
Wp (mmstb)
Gp (mmscf)
Relationship between Gp and Wp 
(a) (b) 
(c)

269 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
  
  
  
 
 
Figure 10. 
The initial pressure derivative curve (a) and the pressure derivative curve from the latest measurement (b) at the TMG-03 well 
 
(a) 
(b)

270 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 11. 
Fault boundary TMG-03 gas well from other gas wells on depth structure map 
 
 
 
Figure 12. 
Crossplot porosity vs. permeability categorized by HFU rock typing method 
0.01
0.10
1.00
10.00
100.00
1,000.00
0.0200 0.0700 0.1200 0.1700 0.2200 0.2700 0.3200 0.3700
Perm, mD
Por, frac
Relationship Porosity and Permeability 
RT1
RT2
RT3
RT4
TMG-03
TMG-04
TMG-01
TMG-02
Relationship porosity permeability

271 
 
 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
Satryangga et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
Figure 13. 
Cross section of the rock-typing (a) distribution model and the permeability (b) distribution model at the TMG field 
TMG-3 TMG-4 TMG-1 TMG-2
TMG-3 TMG-4 TMG-1 TMG-2
TMG-3 TMG-4 TMG-1 TMG-2
TMG-3 TMG-4 TMG-1 TMG-2
(a) 
(b)

272 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
 
Figure 14. 
Initial and new contacts based on radius of investigation calculations from PBU data overlaid with the depth structure map 
Table 1.  
Cummulative gas production at the initial contact versus current contact 
GWC distance vs Cum. production TMG-03 
Year Test Cummulative 
prodcution 
GWC Distance 
equival ent radius 
 (MMscf) (ft) 
Dec-17 0 886.337727 
May-23 424.372081 619.928505 
 
According to the Table 1 and Figure 15, water breakthrough is expecated when total cumulative gas production 
exceeds 11.64 BCF (low case), 11.94 BCF (base case), or 12.18 BCF (high case). As of December 2025, 
cumulative production from the TMG-03 well stands at 18.37 BCF, surpassing the estimated total cumulative gas 
production at the time of breakthrough shown in Figure 16. This indicates that the TMG -03 well has already 
reached the water breakthrough stage.  
Water breakthrough is intimately related to the phenomena of water coning and water channeling in the TMG 
field’s production wells. These two phenomena can be identified utilizing Chan’s water control diagnostic 
approach. This approach uses Equation 5, which plots the water -gas ratio (WGR) and its derivative (WGR’) 
against time. The water control analysis includes wells with recorded gas and water production as well as those 
that have not yet experienced water coning or water channeling. 
 
re(2) 694 ft
re(1) 886 ft
TMG-03
TMG-01
TMG-02

273 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
Figure 15 Cumulative gas prediction at water breakthrough using the cylindrical model 
 
Figure 15. 
Prediction of cumulative gas production at the breakthrough time using a cylindrical model 
 
Figure 16. 
Cumulative gas production from the TMG-03 well has reached the forecasted value at the time of breakthrough 
 
0
50
100
150
200
250
300
350
400
0.0
200.0
400.0
600.0
800.0
1000.0
1200.0
1400.0
1600.0
1800.0
2000.0
05/12/21 05/05/22 05/10/22 05/03/23 05/08/23 05/01/24 05/06/24 05/11/24
bbl
mmscf
Date
Cummulative Gas vs Water Rate Production 
TMG-03 Well
Gp TMG-03
Water Rate TMG-03
Low Case
Base Case
High Case
y = -945.59x + 785595
R² = 1
 -
 100,000.00
 200,000.00
 300,000.00
 400,000.00
 500,000.00
 600,000.00
 700,000.00
 800,000.00
 900,000.00
0 100 200 300 400 500 600 700 800 900
R^2
Cumm. Production ( mmscf )
Cylindrical Model
High Case
Base Case
Low Case
Radius Sensitivty vs
Cumm.Gas Prediction
Cummulative Production at Breaktrough Result 
Case 
Eq. Radius 
Cummulative Production at 
Cyndrical Model 
(ft) (MMscf) 
High Case 200 793.7 
Base Case 250 769.7 
Low Case 300 740.4

274 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
 
Figure 17 
The dWGR/dt plot shows that the TMG-03 well has experienced water channeling. 
 
 
Figure 18 
The dWGR/dt plot shows that the TMG-02 well has experienced water coning late channeling.  
 
 
 
Figure 19 
The dWGR/dt plot shows that the TMG-01 well is still exhibiting normal displacement. 
1.E-07
1.E-06
1.E-05
1.E-04
1.E-03
1.E-02
1.E-01
1.E+00
1.E+01
1.E+02
1 10 100 1000 10000
WGR, WGR'
Days
Chan Plot JNG-03
WGR (bbl/Mscfd) WGR'
Z-14C channeling inception
Rapid Channeling inception water 
breaktrough
Production change effect
May’23 
Chan Plot TMG-3
1.E-10
1.E-09
1.E-08
1.E-07
1.E-06
1.E-05
1.E-04
1.E-03
1.E-02
1.E-01
1.E+00
1.E+01
1 10 100 1000 10000
WGR, WGR'
Days
Chan Plot TMG-02
WGR WGR'
2nd Coning 
Inception of Coning, oct’22
Production Change Effect 
Jan’23
1.E-10
1.E-09
1.E-08
1.E-07
1.E-06
1.E-05
1.E-04
1.E-03
1.E-02
1 10 100 1000 10000
WGR, WGR'
Days
Chan Plot TMG-01
WGR WGR'
WGR increased not significantly, and 
remains stable 
WGR relatively flat

275 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
The log-log plot of the WGR curve in Figure 17 reveals a high slope, while the WGR derivative has a sharp 
positive slope, indicating that water channeling and breakthrough have already occurred in the TMG -03 well. 
Conversely, well TMG-02’s WGR derivative originally showed a negative slope but later transitioned to a positive 
slope by the end of the period, a phenomenon known as water coning late channeling (Figure 18). The primary 
distinction between the two wells is that TMG-03 has already experienced breaktrough, as evidenced by its very 
steep positive derivative, whereas TMG-02 exhibits signs of water coning progressing toward channeling. Figure 
19 depicts a gradual, steady increase in the WGR over time. The WGR derivative behaves similarly, exhibiting 
no severe positive or negative slopes, which indicates normal production conditions in well TMG-01.  
 
4. Conclusion  
Based on the analysis of the P/Z versus cumulative gas production and the Cole plot, the TMG Field is 
characterized by a strong water -drive mechanism associated with active water intrusion, as supported by the 
sustained increase in water production. The ob served water influx indicates an edge -water drive mechanism, in 
which the gas -bearing zone is laterally bounded by an active aquifer. This reservoir behavior is influenced by 
reservoir heterogeneity and is further supported by the water -gas ratio (WGR) pro file, which shows a gradual 
increase before stabilizing at a relatively high rate. The movement of the gas-water boundary as water production 
increases is also reflected in the pressure derivative response, characterized by a rapid decline followed by a sharp 
positive slope in the late -time region, indicating an advancing water front that progressively restricts gas flow. 
Ultimately, the advancing water front resulted in water influx into the wellbore, as observed in well TMG -03, 
which exhibited water chann eling indicated by a sharp positive slope in the WGR profile, while well TMG -02 
showed a transition from early -stage water coning to late -stage water channeling. Overall, these integrated 
observations consistently demonstrate that active aquifer support and the progressive movement of the water front 
are the dominant factors controlling the production behavior of the TMG Field. 
 
5. Acknowledgement 
The authors would like to thank Foster Oil & Energy for their support and data facilities, which allowed this 
study to be completed successfully. 
 
6. Declarations 
6.1 Author contributions 
Tj. Gede Satryangga performed the data processing, conducted the analysis, developed the methodology, and 
drafted the manuscript. A. Yasutra and D. Irawan were involved in conceptualization, methodology development, 
supervision, and reviewed and edited the manuscript. A. Aimar contributed to the water production behavior 
conceptualization and supervision, and S. Kushidayat contributed to supporting field data record and processed. 
All authors read and approved the final version of the paper. 
6.2 Funding statement 
This research was self -funded by the authors and receied no specific grant from any funding agency in the 
public, commercial, or not-for-profit sectors. 
6.3 Competing interest 
The authors declare no competing financial interests or personal relationships that could have influenced the 
work reported in this paper.

276 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
6.4 The use of AI or AI-assisted technologies 
The author(s) used NotebookLm and Quillbot to assist. After using this tool, the authors review and edit the 
content as needed and take full responsibility for the publication’s content.   
 
7. Glossary of terms and symbols 
Terms & 
symbols Definition Unit 
qg Production gas rate mscf/day 
qw Production water rate bbl/day 
ti Production time initial day 
Dt Derivative time  day 
K Permeability mD 
Μ Fluid viscosyt cp 
Ri Radius investigation ft 
Bg Gas formation volume factor Bbl/mscf 
H Thickness ft 
ct Total compressibility psi⁻¹ 
Ø Porosity Frac 
AGWC Contact area m2 
re Equivalent radius Ft 
r2 Equivalent radius cylindrical model Ft 
Gp Cummulative production gas mmscf 
Wp Cummulative production water Mmstb 
SGR Shale gauge ratio % 
A, B Constants used to lump parameters - 
WGR Water gas ratio - 
WGR’ Water gas ratio  - 
 
8. References 
A. Dahroug, SPE, and S. Zheng and J. Baily. 2005. The Application of Transient Pressure Testing to Track Phase 
Boundaries During Production -A One -Well Case Study from UKCS. Presented an SPE Europec/EAGE 
Annual Conference held in Madrid. SPE-94446. https://doi.org/10.2118/94446-MS 
E. Yaich, N. Robertson, T. Whittle, SPE, A. Jamankulov , 2012, Use of Pressure Transient Analysis for the 
Detection of Gas/Water Contact Movement in a Gas Reservoir. Presented at SPETT Energy Conference and 
Exhibition held in Port of Spain. SPE-158827. https://doi.org/10.2118/158827-MS. 
Haijun Fan, Atif Zafar, S.G. Alam, Muhammad Kashif, Asif Mehmood. 2017. Analyses of Nature of Fault trough 
Production Data. Open Journal of Yangtze Gas and Oil. https://doi.org/10.4236/ojogas.2017.23014. 
Ibianga Sukubo, Olakunle Iyowu, Olalekan Balogun, Ifeyinwa Jude-Ofia, and Muyiwa Esho. 2016. An Integrated 
Approach to Water Diagnostic Analysis in A Mature Field: SPDC Case Study, presented SPE Nigeria Annual 
International Conference and Exhibition held in Lagos, SPE-184274-MS. https://doi.org/10.2118/184274-MS 
Jassim A. Al-Ghanim and Subhi A. Al-Nufaili. 2010. Middle East Field Water Production Mechanism. Presented 
at the SPE Oil and Gas India Conference and Exhibition held in Mumbai, India. SPE -127934. 
https://doi.org/10.2118/127934-MS

277 
 
Satryangga et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2139 
 
 
K.S Chan. 1995. Water Control Diagnostic Plots. Presented at the SPE Annual Technical Conference & Exhibition 
held in Dallas, U.SA., SPE-30775. https://doi.org/10.2118/30775-MS 
Larasati K., Wicaksono, D. S., Kristanto D., Hariyadi, Rahmadhini, R. S., & Azzaria, C. N.,  2026. Integrated 
Logging, Production, and Geological Analysis for Bypassed Oil Identification in CNA Field, Central Sumatra 
Basin. Scientific Contributions Oil and Gas, Vol. 49 No.2 (2026). https://doi.org/10.29017/scog.v49i2.2099 
Shusheng Gao, Jianzhong Zhang, Huaxun Liu, Liyou Ye, Wenqing Zhu, Wei Xiong. 2023. Water -gas ratio 
characteristics and development concepts for water -producing gas reservoirs. Elsevier  publish. 
https://doi.org/10.1016/j.heliyon.2023.e19201. 
Sena W. Reksalegora, Yohan Kusumanegara, Phillip Lawry. 1996. A Depositional Model for the “Main” Interval, 
Upper Cibulakan Formation: Its Implications for Reservori Distribution and Prediction, ARII ONWJ. 
Presented at the Indonesian Petroleum Association, Indonesia. IPA96 – 1.1 – 039. 
https://www.ipa.or.id/en/publications
