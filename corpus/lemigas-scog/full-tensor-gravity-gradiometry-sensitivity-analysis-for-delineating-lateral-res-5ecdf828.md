---
source_id: "lemigas-scog"
title: "Full Tensor Gravity Gradiometry Sensitivity Analysis for Delineating Lateral Reservoir Boundaries and Subtle D"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2116"
retrieved_at: "2026-10-24T14:30:23+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "5ecdf82824e81ed4933aae5c614950423808d2b23e2be1154b3fa9b468db83c5"
collected: "manual"
---

# Full Tensor Gravity Gradiometry Sensitivity Analysis for Delineating Lateral Reservoir Boundaries and Subtle D

67 
 
https://doi.org/10.29017/scog.v49i3.2116 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 67 – 87 - http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
Full Tensor Gravity Gradiometry Sensitivity Analysis for Delineating 
Lateral Reservoir Boundaries and Subtle Density Contrasts 
 
Krisna Oka Mahendra1,2*, Muhammad Noor Amin bin Zakariah1,2, Soni Satiawan3,                               
Boko Nurdiyanto Suwardi4, and Edy Widjanarko5 
 
1Centre of Subsurface Imaging (CSI), Unversiti Teknologi Petronas 
Block 16 level 2 Universiti Teknologi Petronas, Seri Iskandar, Perak, Malaysia.  
 2Department of Geoscience, Universiti Teknologi Petronas 
Block 11 level 3 Universiti Teknologi Petronas, Seri Iskandar, Perak, Malaysia.  
3Geophysical Engineering Department Universitas Pertamina. 
Teuku Nyak Arief Street, RT.7/RW.8, Simprug, Grogol Sel, Kebayoran Lama, South Jakarta, Indonesia. 
4PT. Pertamina Hulu Energi : Upstream Innovation  
Level 17 PHE Tower, Letjen T.B. Simatupang Street Kav. 99, Kebagusan, Pasar Minggu, South Jakarta, Indonesia.  
5Testing Center for Oil and Gas LEMIGAS 
Ciledug Raya Street Kavling 109, Cipulir, Kebayoran Lama, South Jakarta, Indonesia. 
 
*Corresponding author: Krisna Oka Mahendra (krisna_24006742@utp.edu.my) 
Krisna Oka Mahendra: https://orcid.org/0009-0005-0731-7347  
Received: 02 June 2026; Revised in revised form 08 July 2026; Accepted 10 July 2026 
Available online 30 September 2026. 
 
ABSTRACT - The gravity method is frequently used for regional basin mapping. However, this method has 
limitations in resolving rock layers at shallow targets or detecting subtle density contrasts between rock formations 
in oil and gas exploration. This study investig ates the capability of Full Tensor Gravity (FTG) gradiometry to 
overcome these challenges in sedimentary basin delineation and shallow reservoir characterization. Forward 
numerical modeling was conducted using the SimPEG Python package to simulate a sedimentary basin containing 
a reservoir with varying thicknesses (100 –500 meters) and rock density contrasts under different saturation 
conditions. Quantitative analysis demonstrates the superior sensitivity of FTG compared to conventional methods. 
For a 500 -meter-thick gas-saturated reservoir, the horizontal FTG components ( 𝐺𝑥𝑥, 𝐺𝑦𝑦) showed an anomaly 
magnitude change of 66.7%, and the vertical gradient ( 𝐺𝑧𝑧) exhibited an increase of 62.5%. These values are 
higher than the change in the conventional gr avity anomaly ( 𝐺𝑧), which only reached 52.0%. Furthermore, 
horizontal gradients effectively delineate the reservoir's lateral boundaries, while the vertical component provides 
a clearer representation of the overall basin structural geometry. This study confirms that FTG analysis yields a 
quantitatively improved subsurface model, thereby reducing the ambiguity associated with conventional gravity 
methods in delineating shallow prospects. 
Keywords: density contrast, full tensor gravity, gravity modeling, reservoir characterization, SimPEG 
 
How to cite this article: 
Krisna Oka Mahendra, Muhammad Noor Amin bin Zakariah, Soni Satiawan, Boko Nurdiyanto Suwardi, 
and Edy Widjanarko, 2026, Full Tensor Gravity Gradiometry Sensitivity Analysis for Delineating Lateral 
Reservoir Boundaries and Subtle Density Contrasts , Scientific Contributions Oil and Gas, 49 ( 3) pp. 
67-87.

68 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
1. Introduction 
Earth's surface exploration relies heavily on various geophysical technologies to map sub surface structures 
precisely, accurately, and efficiently. In the oil and gas industry, companies routinely employ a variety of 
geophysical methods—such as gravity, magnetic, and seismic surveys —tailored to specific exploration needs 
(Anderson et al., 2015; Haldar 2018). Among these methods, conventional gravity is a well-established and widely 
used tool for regional basin mapping. This method provides a fundamental understanding of the structural 
architecture of sedimentary basins over large areas (Blakely 1996; Hinze et al., 2013) and helps identify shallow 
structural features below the surface (Kebede & Mammo 2021).  
However, critical limitations arise when exploration targets shal low structures or reservoirs characterized by 
low density contrast. While conventional gravity methods are expected to map these targets, in reality, they often 
struggle to distinguish anomalous responses from adjacent rock layers with relatively similar d ensity values. 
Previous efforts to address this weakness led to the development of full tensor gravity (FTG) gradiometry, which 
theoretically offers higher -frequency data and superior spatial resolution . (Murphy 2004) However, significant 
practical gaps remain: FTG data acquisition is significantly more expensive than conventional gravity surveying. 
Furthermore, its effectiveness is sometimes debated, as some researchers argue that FTG results can be 
conceptually approximated simply by mathematically differentiating conventional gravity data. This debate raises 
ambiguity regarding the efficiency and necessity of applying FTG in shallow prospect evaluation (Kebede et al., 
2022), even though init ial prospect-scale modeling demonstrated FTG's significant potential for defining rock 
body boundaries (Grandis & Dahrin 2014). 
To address this ambiguity and test the hypothesis that FTG can clearly resolve small density c ontrasts, this 
study applies a quantitative forward numerical modeling approach. Utilizing the SimPEG framework, synthetic 
FTG components are generated from a simulated sedimentary basin model. This modeling strategy enables the 
systematic isolation of geological variables by maintaining constant basin geometry and volume while varying 
only the thickness and density contrast of the fluid -saturated reservoir. This controlled environment eliminates 
interference from complex structural noise, providing a direct and mathematically robust comparison between the 
conventional gravity response and FTG components.  The specific expected output of this study is a definitive 
quantitative evaluation demonstrating the sensitivity differences between the co nventional gravity method, its 
vertical derivative, and the FTG components. By establishing measurable performance metrics on this synthetic 
model, the study findings will serve as a practical evaluation framework for processing and interpreting real -
world field data. For example, A thorough comprehension of the structural framework of gas reservoirs is 
essential not only for traditional hydrocarbon exploration but also for prospective uses like long -term 𝐶𝑂2 
sequestration (Iskandar et al., 2026 ) Ultimately, this study aims to provide a clear framework for stakeholders 
to reduce ambiguity in subsurface interpretation and improve the accuracy of delineating potential shallow 
reservoir geometries.  
 
2. Methodology 
2.1 Problem-Solving approach and assumptions 
To overcome the resolution limitations of conventional gravity data in defining shallow reservoir boundaries, 
this study utilizes a forward numerical modeling approach, which has proven essential for generating high -
resolution models (Montesinos-Flores et al., 2023). This approach allows for the isolation of subsurface variables. 
The baseline model consists of a simple sediment trap without complex structural settlements and is based on a 
regional basin exploration framework from eastern Indonesia (Argakoesoemah & Hughes 2017). Model Density 
parameters are assigned using regional geological references and standard rock/mineral density tables (Telford 
1990; Harsono 1997; Glover 2007). The mode l is assumed to have a dense (ϕ) matrix characterized by low 
porosity (<5%) for the dominant sedimentary rocks, whereas the reservoir is assigned a porosity of 20%.

69 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
2.2 FTG simulation calculation 
The gravity response and gradiometry components of full tensor gravity (FTG) modeling were executed in the 
spatial domain using the open -source Python framework, SimPEG (Cockett et al., 2015 ; Heagy et al., 2024 ). 
Unlike frequency domain (FFT) methods, SimPEG uses a volume integral approach to calculate the gravitational 
anomaly of a set of 3D rectangular prisms.  The gravitational potential (V) of a 3D block cell is calculated using 
Newton's Law of Gravitation. The FTG tensor component(𝐺𝑥𝑥, 𝐺𝑦𝑦, 𝐺𝑧𝑧, 𝐺𝑥𝑦, 𝐺𝑥𝑧, 𝐺𝑦𝑧s) are analytically extracted 
as the second -order spatial derivatives of the gravitational potential, which is mathematically based on the 
formulation of Nagy et al. (2000), Equation 1 
𝐺𝑖𝑗 = γ ∭ Δρ
∂2
∂𝑖 ∂𝑗 (
1
𝑟) 𝑑𝑥′𝑑𝑦′𝑑𝑧′         (1) 
where γ, Δρ, and 𝑟 are the gravitational constant, the density contrast, and the distance between the observation 
point and the center of mass, and 𝑖, 𝑗 ∈ {𝑥, 𝑦, 𝑧}, respectively. To calculate the specific density contrast (Δρ) in 
the reservoir zone, the bulk density (ρ𝑏𝑢𝑙𝑘) of both the fluid -saturated rock and the surrounding bedrock are 
calculated using the following petrophysical Equation 2 
ρ𝑏𝑢𝑙𝑘 = (1 − ϕ)ρ𝑚𝑎 + (ϕρ𝑓𝑙𝑢𝑖𝑑)           (2) 
The reservoir density contrast basin (Δρ𝑟𝑒𝑠−𝑏𝑎𝑠) and with respect to the bedrock background (Δρ𝑟𝑒𝑠−𝑏𝑎𝑐𝑘) is 
calculated as Equation 3 and Equation 4 
Δρ𝑟𝑒𝑠−𝑏𝑎𝑠 = ρ𝑟𝑒𝑠 − ρ𝑏𝑎𝑠                          (3) 
Δρ𝑟𝑒𝑠−𝑏𝑎𝑐𝑘 = ρ𝑟𝑒𝑠 − ρ𝑏𝑎𝑐𝑘                      (4) 
2.3 Application scenarios and analytical tools  
Modeling experiments were conducted using a basin geometry model with a depth and a reservoir geometry 
with a thickness of 1.5 km, a top area of 1.8 × 1.8 km, and a base area that nar rows to 0.8 × 0.8 km. The forward 
modeling scenario focused on observing anomalous responses due to variations in reservoir thickness (100 m to 
500 m) and fluid saturation conditions (empty, freshwater, oil, and methane). The FTG responses generated from 
the Python -based simulation were subsequently exported and integrated into Geosoft Oasis Montaj software 
(provided by PT PHE) for grid calculation analysis, advanced filtering, and qualitative comparison with actual 
field data responses. 
 
 
 
 Parameter category Properties Value / Description  
 Basin Geometry Depth to Top Basin 1.5 km  
 Basin thickness 1.5 km  
 Top basin size 1.8 x 1.8 km  
 Bottom basin size 0.8 x 0.8 km  
 Target reservoir 
thickness 
100 m –500 m  
 
Petrophysical (Density) 
Dominant sediment 
(sandstone) 
2.60 gr/cc (ϕ < 5%)  
 Basement rock 
(dolomite) 
2.70 gr/cc  
 Fresh water saturated 2.44 gr/cc  
 Oil saturated 2.425 gr/cc  
 Gas (Methane) Saturated 2.36 r/cc  
Table 1. 
 Basin Model Geometry and Petrophysical Parameters.

70 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
3. Result and Discussion 
3.1 Synthetic basin and reservoir model 
The initial stage of the computational analysis focused on reconstructing the geometry of a three-dimensional 
(3D) synthetic model representing a sedimentary basin and its associated reservoir zones. This model creation is 
crucial for understanding the dis tribution of subsurface physical properties prior to the computation of gravity 
anomalies and gradiometry tensor components. Based on predetermined parameters, the sedimentary basin is 
modeled as an inverted trapezoidal prism extending from the surface to a maximum depth of 1.5 km. The basin's 
geometry was defined by upper lateral dimensions of 1.8 x 1.8 km, which gradually narrowed to 0.8 x 0.8 km at 
the basin base, discretized using a minimum cell size of 100 m. 
This modeling scenario assumes an idealized sediment-trap system without the influence of complex faulting 
or folding structures, thereby allowing the physical response of the model to be isolated and evaluated more 
rigorously. A cross -section of the synth etic model variation along the Y = 0 plane is shown in (Figure 1). The 
distribution of rock and fluid saturation density values was injected into each cell block (right rectangular prism) 
of the mesh based on petrophysical calculations based on field geological parameters.  
The basement is represented by dolomite lithology with a density of 2.70 g/cc, which acts as the background 
density. The sedimentary basin is filled d with sandstone material with a matrix density of 2.60 g/cc in an unfilled 
basin. To evaluate the resolution limits of full tensor gravity (FTG) resolution sensitivity, a shallow reservoir zone 
was simulated within a basin with a porosity of 20% and a pure methane gas saturation level of 100%.  
According to Equatio n 2, the presence of this gas saturation significantly reduces the bulk density of the 
reservoir rock to 2.36 gr/cc, resulting in a local density contrast (Δρ) of -0.24 gr/cc relative to the surrounding 
basin rocks. The sensitivity analysis was then carried out comparatively by gradually changing the vertical 
thickness of the gas-saturated reservoir rock, starting from a thin thickness of 100 m, a medium thickness of 300 
m, to a thick compartment of 500 m, as illustrated in (Figure 1b-d). 
3.2 Qualitative anomaly response: conventional gravity vs. FTG 
A qualitative analysis was conducted to visually compare the delineation capabilities of conventional gravity 
and full tensor gravity (FTG) methods. The initial evaluation focused on the conventional vertical gravity anomaly 
(𝐺𝑧) response in an unfilled basin compared to a basin containing a gas-saturated reservoir (Figure 2).  
The modeling results show that the 𝐺𝑧 anomaly is characterized by a broad, low -frequency contour pattern 
that tends to be circular. Although the presence of a low -density gas reservoir (2.36 g/cc) reduces the anomaly 
value at the basin center to approximately -1.5 mGal, the change in contour pattern is minimal. As a result, the 
macroscopic geometry of the basin appears to dominate the response, while the lateral boundaries of the reservoir 
remain poorly resolved and cannot be clearly delineated.  
This limitation of the conventional gravity ( 𝐺𝑧) method is successfully overcome by the FTG tensor 
component, which demonstrates significantly higher visual sensitivity (Figure 3). The separation of the vertical 
and horizontal gravity gradient components provides specific str uctural information. In the vertical gradient, the 
Gzz component displays a centralized anomaly that emphasizes the location of mass deficit accumulation, while 
Gxz and Gyz begin to exhibit a bi-polar pattern indicating a density transition. 
The superior c apability of FTG for boundary delineation is strongly confirmed by its horizontal gradient 
components (𝐺𝑥𝑥 and 𝐺𝑦𝑦). Unlike the fuzzy 𝐺𝑧, the 𝐺𝑥𝑥 and 𝐺𝑦𝑦 components (Figure 3d–e) exhibit narrowing 
contours that spatially align closely with the physical boundaries of the reservoir compartment. The high spatial 
frequency of these horizontal components effectively defines the geometry of the edges of the target zone, 
qualitatively demonstrating that FTG gradiometry is  far superior to conventional gravity in mapping the 
boundaries of low-density reservoirs.

71 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
 
 
Figure 1. 
Cross-section of the Y=0 coordinate path of a synthetic sedimentary basin model (yellow indicates bedrock, grid  
pattern indicates sedimentary material). This model shows a variety of geometric trap conditions of the basin including: 
(a) Empty sedimentary basin with a density of 2.60 gr/cc without the presence of hydrocarbons; (b) Injection of a methane-
saturated reservoir (density of 2.36 gr/cc) with a vertical thickness of 100 m; (c) Gas-saturated reservoir with a thickness of 
300 m; and (d) Gas-saturated reservoir with a maximum thickness of 500 m. 
 
a 
b 
c 
d

72 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
Figure 2. 
Cross-section of the Y=0 coordinate path of a synthetic sedimentary basin model (yellow indicates bedrock, grid pattern 
indicates sedimentary material). This model shows a variety of geometric trap conditions of the basin including: (a) Empty 
sedimentary basin with a density of 2.60 gr/cc without the presence of hydrocarbons; (b) Injection of a methane-saturated 
reservoir (density of 2.36 gr/cc) with a vertical thickness of 100 m; (c) Gas-saturated reservoir with a thickness of 300 m; 
and (d) Gas-saturated reservoir with a maximum thickness of 500 m. 
 
 
 
To validate that the sharp anomalies originate purely from the gas reservoir and not from basin margin effects, 
the analysis continued by extracting difference maps. The difference maps isolate the reservoir fluid response by 
subtracting the reservoir data from the unfilled basin background response. The conventional gravity difference 
maps are still highly susceptible to interpretation ambiguity due to the biased distribution of anomalies (Figure 4). 
In contrast, the FTG difference maps, including both the vertical -gradient components (Figure 6 ) and the 
horizontal-gradient components (Figure 8) , strongly confirm that the strongest anomaly responses are 
concentrated along the reservoir boundaries. This finding qualitatively eliminates the interpretation ambiguity that 
is inherently common in conventional gravity methods. 
3.3 Quantitative sensitivity analysis 
The qualitative evaluation demonstrating the superior spatial resolution of FTG was further validated through 
a quantitative sensitivity analysis. This analysis quantified the percentage c hange in the maximum anomaly 
magnitude between the unfilled basin scenario and the methane-saturated basin scenario at various compartment 
thicknesses. This linear change in magnitude profile with respect to reservoir thickness can be precisely observed 
through a 1D curve cross-section. The comprehensive tabulated calculation results are summarized in Table 2.

73 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
 
 
 
 
Figure 3. 
Spatial response maps of full tensor gravity (FTG) gradiometry components for a empty, 100, 300, and 500 m thick                
gas-saturated reservoir model. The vertical components (𝐺𝑥𝑧, 𝐺𝑦𝑧, and 𝐺𝑧𝑧) shown at (a) empty, (b) 100m, (c) 300m, and               
(d) 500m thick gas-saturated reservoir. The horizontal components (𝐺𝑥𝑥, 𝐺𝑦𝑦 , and 𝐺𝑥𝑦) shown at (e) empty, (f) 100m,                     
(g) 300m, and (h) 500m thick gas-saturated reservoir, where the 𝐺𝑥𝑥 and 𝐺𝑦𝑦 components clearly delineate the reservoir 
geometry boundaries through the narrowing of the anomaly contours. (Red box: Basin Boundary,                                                  
Black Dashed Box: Reservoir Boundary). 
a 
b 
c 
d

74 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
 
Figure 3. 
Spatial response maps of full tensor gravity (FTG) gradiometry components for a empty, 100, 300, and 500 m thick                
gas-saturated reservoir model. The vertical components (𝐺𝑥𝑧, 𝐺𝑦𝑧, and 𝐺𝑧𝑧) shown at (a) empty, (b) 100m, (c) 300m, and               
(d) 500m thick gas-saturated reservoir. The horizontal components (𝐺𝑥𝑥, 𝐺𝑦𝑦 , and 𝐺𝑥𝑦) shown at (e) empty, (f) 100m,                     
(g) 300m, and (h) 500m thick gas-saturated reservoir, where the 𝐺𝑥𝑥 and 𝐺𝑦𝑦 components clearly delineate the reservoir 
geometry boundaries through the narrowing of the anomaly contours. (Red box: Basin Boundary, Black Dashed Box: 
Reservoir Boundary), (continued). 
 
e 
f 
g 
h

75 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
Figure 4.  
Difference maps between the gas-saturated basin model (100, 300, and 500 m) and the empty basin model. The panels 
represent the isolated fluid responses to: (a) Conventional gravity (Diff Gz), (b) Principal vertical gradient (Diff Gzz), and 
(c) Principal horizontal gradient (Diff Gxx). (White Box Basin Boundary, Black Dashed Box: Reservoir Boundary). 
 
 
 
 
 
Figure 5. 
1D profile curve graph (line profiles) from the results of conventional gravity difference analysis (Diff Gz) extracted 
across the center of the reservoir compartment on the Y = 0 trajectory. This graph quantitatively compares the magnitude of 
anomalies in reservoir thickness variations of 100 m, 300 m, and 500 m against the baseline value of the empty basin in 
mGal units (Red Box: Basin Boundary, Black Dashed Box: Reservoir Zone). 
 
 
Diff_Gz_100_300_500

76 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
Figure 6. 
Difference maps of vertical and cross-plane gradient components of FTG in Eötvös units, including Diff Gxz, Diff Gyz, 
and Diff Gzz components. This map isolates the dipole and centered anomalous responses due to the presence of target fluids 
at various reservoir thickness variations. a) 100m thickness, b) 300m thickness, c) 500m thickness (White Box Basin 
Boundary, Black Dashed Box: Reservoir Boundary). 
 
Table 2. Anomaly Changes Observation Table for Intial Condition Compared to Saturated Condition. 
 
  Observed anomaly Empty basin value Change at 100 m Change at 300 m Change at 500 m   
  Gz -1.25 mGal -0.15 mGal (12.0%) -0.45 mGal (36.0%) -0.65 mGal (52.0%)   
  Gzz -8.0 Eotvos -1.4 Eotvos (17.5%) -3.5 Eotvos (43.8%) -5.0 Eotvos (62.5%)   
  Gxz +4.0 Eotvos +0.6 Eotvos (15.0%) +1.5 Eotvos (37.5%) +2.2 Eotvos (55.0%)   
  Gyz +4.0 Eotvos +0.6 Eotvos (15.0%) +1.5 Eotvos (37.5%) +2.2 Eotvos (55.0%)   
  Gxx +4.2 Eotvos +0.8 Eotvos (19.0%) +1.8 Eotvos (42.9%) +2.8 Eotvos (66.7%)   
  Gyy +4.2 Eotvos +0.8 Eotvos (19.0%) +1.8 Eotvos (42.9%) +2.8 Eotvos (66.7%)   
  Gxy (+) +1.4 Eotvos +0.2 Eotvos (14.3%) +0.5 Eotvos (35.7%) +0.8 Eotvos (57.1%)   
  Gxy (-) -1.4 Eotvos -0.2 Eotvos (14.3%) -0.5 Eotvos (35.7%) -0.8 Eotvos (57.1%)   
a 
 
b 
 
c

77 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
Figure 7. 
1D line profile curve graph of the results of the vertical gradient component difference analysis of FTG extracted across 
the center of the reservoir compartment. The graph represents the Diff 𝐺𝑥𝑧, Diff 𝐺𝑦𝑧, and Diff 𝐺𝑧𝑧 components in Eotvos 
units which show a sharp spike in magnitude above the center of the anomaly. (Red Box: Basin Boundary, Black Dashed 
Box: Reservoir Zone). 
 
 
Physically, the presence of methane gas significantly reduces the bulk density of the reservoi r, generating a 
mass deficit relative to the surrounding rocks and consequently decreasing the observed gravity response. The 
results show that the percentage change in anomaly amplitude increases systematically with increasing reservoir 
thickness from 100 m to 500 m, confirming a direct relationship between the gravity response and the volume of 
the gas-saturated reservoir.  
For the model with a maximum reservoir thickness of 500 m, the conventional gravity field ( 𝐺𝑧) method 
exhibits a reduction in anoma ly amplitude of -0.65 mGal, equivalent to a 52.0% decrease relative to the 
baseline value. Although these changes are quite large, the effect of signal attenuation spreading over vertical 
distance causes the changes to be less sharp in gradient terms, as s een in the steepness of the difference 
profile curve (Figure 5 ). 
On the other hand, the FTG tensor component responds to this density contrast with far superior sensitivity, 
even in layers as thin as 100 m. The vertical gradient component (𝐺𝑧𝑧) curve shows a sharp systematic spike in 
changes directly above the anomaly center (Figure 7), reaching 62.5% (an absolute decrease of -5.0 Eotvos) in 
the 500 m reservoir. The highest percentage change is demonstrated by the main horizontal gradient components, 
𝐺𝑥𝑥 and 𝐺𝑥𝑥, which recorded a maximum percentage change of 66.7%, with an extreme anomaly peak at the 
Diff_Gyz_100_300_500 
Diff_Gzz_100_300_500 
 
Diff_Gxz_100_300_500

78 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
transition zone of the structural boundary (Figure 9). The high value of the change in the horizontal component is 
mathematically explained by its ability to measure the rate of change of gravity along the lateral axis, where the 
gradient will peak sharply at the vertical boundary of the fault or reservoir edge ( Δρ). This quantification proves 
the hypothesis that FTG gradiometry has higher analytical sensitivity to capture minor density changes (subtle 
density contrasts) that are often missed by conventional gravity methods. 
 
 
Figure 8. 
Difference maps of the main horizontal gradient components of FTG in Eotvos units, including the Diff 𝐺𝑥𝑥, Diff 𝐺𝑦𝑦, 
and Diff 𝐺𝑥𝑦 components. The extreme value contours laterally frame and delineate the edge of the reservoir area; a). 100m 
thickness, b). 300m thickness, c). 500m thickness (White Box Basin Boundary, Black Dashed Box: Reservoir Boundary). 
 
3.4 Field data application and validation 
Based on the understanding of the physical behavior of the synthetic model, FTG gradiometry principles were 
then applied to field data to validate its ability to delineate the basin geometry. The initial interpretation was based 
on the complete bouguer anomaly (CBA) map and residual anomaly maps (Figure 10). In the CBA data, the 
interpretation focused on the low -anomaly response, indicated by specific polygons, which were interpreted as 
potential depocenters associated with thick accumulations of low-density sedimentary rocks. 
 
a 
 
b 
 
c

79 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
 
Figure 9. 
1D profile curve graph (line profiles) from the results of the analysis of the difference in horizontal gradient components 
of FTG extracted across the center of the reservoir compartment. The graph represents the components of Diff 𝐺𝑥𝑥, Diff 𝐺𝑦𝑦, 
and Diff 𝐺𝑥𝑦 in Eotvos units which show the peak of the extreme gradient precisely at the density transition zone of the 
structure boundary (Red Box: Basin Boundary, Black Dashed Box: Reservoir Zone). 
 
 
 
Diff_Gxx_100_300_500 
Diff_Gyy_100_300_500  
 Diff_Gxy_(+)_100_300_500 
 
Diff_Gxy_(-)_100_300_500

80 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
Figure 10. 
Gravity anomaly map from actual field data used as a validation basis.  
The figure shows: (a) Complete Bouguer Anomaly (CBA) map in mGal units where the initial target zone was identified 
based on the presence of low anomalous response. 
 
The anomaly response in the field data showed very strong agreement with the simulation result predicted by 
the synthetic models lts (Figure 11). The field-derived vertical components (pseudo-𝐺𝑥𝑧 and 𝐺𝑦𝑧) exhibit behavior 
consistent with the synthetic FTG responses, effectively highlighting lateral density transitions and structural 
boundaries. Furthermore, when compared directly to the residual anomaly data (Figure 12), the 𝐺𝑧𝑧 component in 
the target zone has a higher frequency spectrum and much sharper boundaries between the low anomaly zones, 
indicating the presence of a previously blurred deficit density compartment. 
The superior capability of FTG in detecting lateral de nsity variations was again clearly confirmed in the 
mapping of the field's horizontal components (pseudo -𝐺𝑥𝑥, 𝐺𝑦𝑦, and 𝐺𝑥𝑦). The responses of the 𝐺𝑥𝑥 and 𝐺𝑦𝑦 
components consistently aligned with the simulated anomaly patterns, where the strai ghtening and narrowing of 
the contours precisely mapped the edges of the subsurface structure. 
 
b 
 
Gravity_Gradiometry_Project 
Residual_Airborne_Gravity_CBA 
Gravity_Gradiometry_Project 
Airborne_Gravity_CBA 
a

81 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
 
Figure 11. 
Full tensor gravity (FTG) map of the field in Eotvos units highlighting the similarity of the anomaly response pattern to 
the synthetic model. This combined image displays: (a) The vertical gradient components of the field (𝐺𝑥𝑧, 𝐺𝑦𝑧, and 𝐺𝑧𝑧) 
exhibiting a centralized and double-pole anomaly pattern that resembles the physical behavior of the model; and (b) The 
horizontal gradient components of the field (𝐺𝑥𝑥, 𝐺𝑦𝑦, and 𝐺𝑥𝑦) consistently exhibiting a similar contour narrowing pattern, 
demonstrating the good match of the delineation characteristics between the synthetic and real-world data. 
 
a 
b

82 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
 
Figure 12. 
Direct visual comparison map between: (a) conventional Residual Gravity Anomaly, and (b) vertical derived Gzz field 
component in the main target zone. This comparison validates that the Gzz component has a higher frequency spectrum and 
much sharper and more precise delineation boundaries in representing the Similar Anomaly Response compared to 
conventional residual data. 
 
To further enhance the interpretability of the FTG data, the multidirectional gradient components were 
calculated into magnitude -based data, namely total horizontal gradient (THG) and total horizontal curvature 
(THC) (Figure 13). These attributes are directly derived from the FTG tensor components using the following 
mathematical formulations:  
𝑇𝐻𝐺 = √𝐺𝑥𝑧2 + 𝐺𝑦𝑧2                                   (5) 
𝑇𝐻𝐶 = √(𝐺𝑥𝑥−𝐺𝑦𝑦
2 )
2
+ (𝐺𝑥𝑦)
2
                 (6) 
where 𝐺𝑥𝑧 and 𝐺𝑦𝑧 are the horizontal gradient component of FTG. And 𝐺𝑥𝑥, 𝐺𝑥𝑦, and 𝐺𝑦𝑦 are the horizontal 
curvature component of FTG respectively. 
a 
b

83 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
The THG map provides a significantly sharper and more detailed repressentation of the lower basin boundary 
than the residual CBA map. The THG map provides a significantly sharper and more detailed representation of 
the lower basin boundary than the residual CBA map. Meanwhile, the THC map showed an inversely proportional 
correlation with 𝐺𝑧𝑧 response within the prospective zone (Li, 2015), further strengthening the certainty of the 
localization of the basin target. All these findings from the application of field data demonstrate that the integration 
of gradiometri c analysis plays a crucial role in improving interpretation resolution and significantly reducing 
structural ambiguity in oil and gas exploration. 
 
 
Figure 13. 
Magnitude-based derived analysis maps of field data in Eotvos units for optimizing structural interpretation.  
The panels represent: (a) Total horizontal gradient (THG) map and (b) Total horizontal curvature (THC) map.  
The appearance of identical anomaly patterns in these attribute maps confirms that the spatial sensitivity of the synthetic 
modeling is actually applicable to field data. 
 
Overall, the findings from the field data application confirm the results of previous studies regarding the 
capabilities of FTG. The success of the horizontal gradient component in constraining basin boundaries sharply 
aligns with the study by Montesinos-Flores et al. (2023), who demonstrated that tensor-based gravity analysis and 
inversion pro vide substantially higher spatial resolution of shallow subsurface structures than conventional 
gravity. Furthermore, the sensitivity of the 𝐺𝑧𝑧 component to local anomalies demonstrated in the field data 
a 
b

84 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
reinforces the conclusion of Kebede et al. (2022) that the integration of spatial derivatives is crucial in reducing 
ambiguities in basin geometry, which regional Complete Bouguer Anomaly data often fail to resolve. 
Furthermore, the inverse correlation between THC and 𝐺𝑧𝑧 within the prospect zone is consistent with the 
curvature attribute principle outlined by Li (2015). 
While FTG data, particularly the 𝐺𝑧𝑧 component, demonstrate exceptional capability in delineating subtle 
density contrasts  with high spatial resolution for shallow targets, it is important to acknowledge its depth -
dependent limitations. Based on fundamental potential field theory, conventional gravitational acceleration ( 𝐺𝑧) 
attenuates at a rate proportional to the inverse square of the distance from the source ( 1/𝑟2) (Blakely, 1996 ). 
In contrast, the spatial gradients of the gravity field, such as 𝐺𝑧𝑧, represent the second derivatives of the 
gravitational potential and attenuate much faster, a t a rate proportional to 1/𝑟3 (Blakely, 1996). Because of this 
rapid 1/𝑟3 decay, FTG measurements are heavily dominated by the nearest sources, producing short -
wavelength signals that can only originate from shallow depths (Brewster & Murphy 2017 ). Conventional 
gravity, however, retains long -wavelength features that can arise from both shallow and deep regional sources 
(Brewster & Murphy 2017). Consequently, the resolution of the 𝐺𝑧𝑧 component degrades rapidly as target depth 
increases. This theoretically confirms that while conventional gravity remains essential for mapping deep 
basement architecture, FTG analysis is most appropriate for pr ospect-scale anomaly delineation and shallow 
reservoir characterization (Grandis & Dahrin 2014 ). 
 
4. Conclusion 
This study quantitatively and qualitatively demonstrates that full tensor gravity (FTG) gradiometry can 
overcome the fundamental limitations of conventional gravity methods in delineating shallow subsurface 
structures characterized by very low-density contrasts. Through high-resolution spatial numerical modeling of a 
gas-saturated sedimentary basin, the horizontal components of the FTG ( 𝐺𝑥𝑥 and 𝐺𝑦𝑦) demonstrated the highest 
sensitivity to reservoir-induced density variations, with a change rate of 66. 7%. This significantly outperformed 
the conventional method (Gz), which only responded to signal attenuation of 52.0%. Spatially, these tensor 
components not only successfully isolated the fluid response from the dominant regional basin anomalies but also 
precisely mapped the lateral edges of hydrocarbon reservoir compartments. 
Furthermore, the application of the spatial derivative approach to the complete bouguer anomaly (CBA) field 
data validated the effectiveness of this gradiometry physics concept in practical applications. The use of curvature 
attributes and spatial gradients in the field proved effective in detecting basin-boundary fault zones and reducing 
ambiguity in subsurface structure interpretation. The significance of this research provides technical justification 
for the exploration geophysics industry that the integration of gradiometry analysis —both through direct FTG 
data acquisition and through the efficient manipulation of higher-order derivatives of conventional gravity data—
is an essential analytical tool. The application of this comprehensive method is highly recommended to minimize 
the risk of structural uncertainty in the identification and development phase of future shallow prospects. 
 
5. Acknowledgement 
The authors wish to express their sincere gratitude to PT Pertamina Hulu Energi (PHE) - Upstream Innovation 
for providing the field data and the Oasis Montaj software essential for data processing. We also extend our 
appreciation to centre of subsurface imaging (CSI)  Universiti Teknologi Petronas and BBPMGB LEMIGAS for 
their support in facilitating the publication of this research. 
Special thanks are directed to Dr. M Amin Noor Zakariah for his invaluable role as a supervisor, his critical 
initial review of this manuscript, and for providing the financial support that made this study possible. The authors 
also gratefully acknowledge the continued guidance and support of our research mentors: Mr. Soni Satiawan from 
Universitas Pertamina, Mr. Boko Nurdiyanto Suwardi from  PT PHE - Upstream Innovation, and Mr. Edy 
Wijanarko from BBPMGB LEMIGAS.

85 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
Finally, we would like to thank the examiners of this research, Imam Baru Raharjo, Ph.D., and Dicky Ahmad 
Zaky, M.T., for their constructive feedback and corrections that significantly improved the quality of this work. 
 
6. Declarations 
6.1 Author contribution 
K. O. Mahendra: Conceptualization, Methodology, Develop Code and Algorithm, Formal analysis, Data 
curation, Visualization, Writing – original draft.  M. N. A. Zakariah: Supervision,  Methodology, Validation, 
Writing – review & editing. S. Satiawan : Supervision, Validation, Methodolgy and Writing – review & editing. 
B. N. Suwardi: Supervision, Validation, review & editing, providing software.  E. Widjanarko: Supervision, 
Validation, review & editing, providing software. 
6.2 Funding statement  
This research was financially supported by Universiti Teknologi PETRONAS (UTP) under the Graduate 
Assistantship (GA) scheme. 
6.3 Competing interest  
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper. 
6.4 The use of AI or AI-Assisted technologies  
During the preparation of this work, the authors used Google Gemini to assist with sentence restructuring, 
academic translation, and improving the overall readability of the manuscript. After using this tool, the authors 
reviewed and edited the content as needed and take full responsibility for the publication's content. 
 
7. Glossary of terms and symbols 
  Terms & Symbols Definition Unit   
  CBA Complete Bouguer Anomaly mGal   
  FTG Full Tensor Gravity Gradiometry Eotvos   
  SimPEG Simulation and Parameter Estimation in Geophysics (Open-source Python framework) -   
  THC Total Horizontal Curvature Eotvos   
  THG Total Horizontal Gradient Eotvos   
  Gz Vertical component of the conventional gravity anomaly mGal   
  Gxx,Gyy Horizontal diagonal components of the gravity gradient tensor Eotvos   
  Gzz Vertical diagonal component of the gravity gradient tensor Eotvos   
  Gxy,Gxz,Gyz Off-diagonal cross components of the gravity gradient tensor Eotvos   
  r Spatial distance between the observation points and the center of mass m   
  V Gravitational potential m2/s2   
  γ Universal gravitational constant m3/(kg⋅s2)

86 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
  Δρ Spatial density contrast between different rock volumes gr/cc   
  Δρres−bas Density contrast of the reservoir rock relative to the surrounding basin gr/cc   
  Δρres−back Density contrast of the reservoir rock relative to the background basement gr/cc   
  ρbulk Volumetric bulk density of a rock formation gr/cc   
  ρfluid Density of the saturating fluid (e.g., water, oil, gas) gr/cc   
  ρma Matrix density of the rock framework gr/cc   
  ϕ Matrix porosity of the rock %   
 
8. References 
Anderson, E. D., Dentith, M., & Mudge, S. T. (2015). Geophysics for the mineral exploration geoscientist. 
Mineralium Deposita, 50(2), 139–140. https://doi.org/10.1007/s00126-014-0557-9 
Argakoesoemah, R. M. I., & Hughes, J. D. E. (2017). Invited Papers: A review of Mesozoic exploration plays in 
the southern part of onshore East Papua, Indonesia. In SKK Migas Memoir #1: Petroleum Systems of the 
Eastern Indonesia Region  (pp. 427 -
474).https://www.researchgate.net/publication/323277525_A_review_of_Mesozoic_exploration_plays_in_th
e_southern_part_of_onshore_East_Papua_Indonesia  
Blakely, R. J. (1996). Potential theory in gravity and magnetic applications . Cambridge University Press.  
https://doi.org/10.1017/CBO9780511549816 
Brewster, J., & Murphy, C. (2020). Source Body Migration as a Method of Depth Separation of Gravity Gradient 
Data. SEG Technical Program Expanded Abstracts 2017 , 17 76-1780. https://doi.org/10.1190/segam2020-
3422619.1 
Cockett, R., Kang, S., Heagy, L. J., Pidlisecky, A., & Oldenburg, D. W. (2015). SimPEG: An open -source 
framework for simulation and gradient-based parameter estimation in geophysical applications. Computers & 
Geosciences, 85, 142-154. https://doi.org/10.1016/j.cageo.2015.09.015 
Glover, P. W. J. (2007). Petrophysics M.Sc. Course Notes. University of Aberdeen. 
Grandis, H., & Dahrin, D. (2014). Full tensor gradient of simulated gravity data for prospect scale delineation. 
Journal of Mathematical and Fundamental Sciences , 46(2), 107 -124. 
https://doi.org/10.5614/j.math.fund.sci.2014.46.2.1 
Haldar, S. K. (2018). Exploration geophysics. In Mineral Exploration  (pp. 103 –122). Elsevier. 
https://doi.org/10.1016/B978-0-12-814022-2.00006-X 
Harsono, A. (1997). Evaluasi formasi dan aplikasi log. Schlumberger Oilfield Services. 
Heagy, L. J., Kang, S., Capriotti, J., Fournier, D., Cockett, R., & Oldenburg, D. W. (2024). Opportunities for 
open-source software to accelerate research in applied geophysics. The Leading Edge , 43(2), 84 -91. 
https://doi.org/10.1190/tle43020084.1 
Hinze, W. J., von Frese, R. R. B., & Saad, A. H. (2013). Gravity and magnetic exploration: Principles, practices, 
and applications. Cambridge University Press. https://doi.org/10.1017/CBO9780511843129 
Iskandar, U. P., Arik, Panuju, Grandis, G., & Ilham, N. (2026). Optimizing CO2 Storage Strategies for Enhanced 
Mineral Trapping and Plume Containment in The Aquifer Zone of an Indonesi an Gas Reservoir. Scientific 
Contributions Oil and Gas, 49(2), 173-201. https://doi.org/10.29017/scog.v49i2.2067

87 
  
Mahendra et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2116 
 
Kebede, B., & Mammo, T. (2021). Processing and interpretation of full tensor gravity anomalies of Southern Main 
Ethiopian Rift. Heliyon, 7(10), e06872. https://doi.org/10.1016/j.heliyon.2021.e06872 
Kebede, B., Mammo, T., & Misgie, A. (2 022). Structural interpretation of Southern Main Ethiopian Rift basin 
using constrained full tensor gravity inversion of the basement morphology. Heliyon, 8(5), e09525. 
https://doi.org/10.1016/j.heliyon.2022.e09525 
Li, X. (2015). Curvature of a geometric surface and curvature of gravity and magnetic anomalies. Geophysics, 
80(1), G15–G26. https://doi.org/10.1190/geo2014-0108.1 
Montesinos-Flores, M., Orozco-Aguilar, C., & Urrutia-Fucugauchi, J. (2023). High resolution model of the Vinton 
Salt-Dome cap rock by joint inversion of the full tensor gravity gradient data with the simulated annealing 
global optimization method. Pure and Applied Geophysics , 180(3), 1025 -1045. 
https://doi.org/10.1007/s00024-023-03227-9 
Murphy, C. (2004). The Air-FTG airborne gravity gradiometer system. In Airborne Gravity 2004 - Abstracts from 
the ASEG -PESA Airborne Gravity 2004 Workshop  (pp. 7 -14). Geoscience Australia Record 2004/18.  
https://pid.geoscience.gov.au/dataset/ga/61129 
Nagy, D., Papp, G., & Benedek, J. (2000). The gravitational potential and its derivatives for the prism. Journal of 
Geodesy, 74(7-8), 552-560. https://doi.org/10.1007/s001900000116 
Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). Applied geophysics (2nd ed.). Cambridge University Press. 
https://doi.org/10.1017/CBO9781139167932
