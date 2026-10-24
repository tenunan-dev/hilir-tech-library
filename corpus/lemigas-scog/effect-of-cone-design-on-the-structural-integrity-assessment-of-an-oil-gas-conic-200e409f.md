---
source_id: "lemigas-scog"
title: "Effect of Cone Design on the Structural Integrity Assessment of an Oil Gas Conical Perforated Strainer Using C"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2130"
retrieved_at: "2026-10-24T14:30:17+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "200e409f09ec7b27e1da280baeab290ea02011a0def1e864a55175981409169e"
collected: "manual"
---

# Effect of Cone Design on the Structural Integrity Assessment of an Oil Gas Conical Perforated Strainer Using C

107 
 
https://doi.org/10.29017/scog.v49i3.2130 
 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 107 – 129 - http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Effect of Cone Design on the Structural Integrity 
Assessment of an Oil & Gas Conical Perforated Strainer 
Using CFD- Coupled Finite Element Analysis 
 
Mohd Azni Md Kasim1, Mohd Azahari Razali1*, Nur Syafiqah Adha Narrudin1, 
Norfakhira Mohd Nor1, Iman Fitri Ismail2, Masataro Suzuki3, and Amnur Akhyan4 
 
1Faculty of Mechanical and Manufacturing Engineering, Universiti Tun Hussein Onn Malaysia, 
86400 Parit Raja, Batu Pahat, Johor, Malaysia.  
2Tuah Energy Sdn Bhd, T4-1-4, Tower 4, Maju Link, 
Bandar Tasik Selatan, 57000 Kuala Lumpur, Malaysia. 
3Department of System Safety Engineering, Institute of GIGAKU, Nagaoka University of Technology, 
Nagaoka, Nigata, Japan.  
4Politeknik Caltex Riau, 
Umban Sari Street No. 1, Umban Sari, Rumbai District, Pekanbaru City, Riau 28265, Indonesia.  
*Corresponding author: Mohd Azahari Razali (azahari@uthm.edu.my) 
Mohd Azahari Razali: Scopus Id: https://www.scopus.com/authid/detail.uri?authorId=57210113966 
Orchid: https://orcid.org/0000-0001-5346-4325 
Received: 30 March 2026; Revised: in revised form 22 July 2026; Accepted: 03 September 2026 
Available: online 30 September 2026. 
  
 
 
ABSTRACT - Cone strainers play an important role in oil and gas process piping systems and are often subjected 
to high-pressure fluid flow. The early failure of a cone strainer in a Low Temperature Separation Unit (LTSU) 
during prolonged service motivated a detailed structural integrity investigation. A combined Computational Fluid 
Dynamics (CFD) and Finite Element Analysis (FEA) method was used to assess the structural behaviour of a 
conical perforated strainer under actual operating conditions (30.51 bar (a), 94.3 °C) and contingency conditions 
(36.61 bar (a), 113.16 °C), the latter representing the pressure and temperature excursions encountered 
intermittently during normal service. Pressure, temperature and wall shear stress obtained from steady-state CFD 
were applied to the structural model through one -way fluid–structure interaction, and structural adequacy was 
expressed as a Unity Check (UC), the ratio of the peak von Mises stress to an allowable stress of 336 MPa. The 
baseline 2 mm punching plate (Geometry A) was adequate under actual conditions (UC = 0.87) but failed under 
contingency conditions, reaching 371.8 MPa and UC = 1.11, as a result of flow-induced bending across the large, 
low-stiffness perforated cone surface. Thickening the punching plate to 4 mm (Geometry B) reduced the 
contingency peak stress by 13.4% to 322.0 MPa and the UC to 0.96, but transferred load into the ring plate, whose 
UC rose from 0.95 to 0.99 and which thereby became the new critical component. Repositioning the ring plate 
(Geometry C) reduced the punching plate UC to 0.91 and the ring plate UC to 0.30, at the cost of a 19.7% increase 
in pressure drop, from 7273 Pa to 10894 Pa. Geometry C is therefore proposed as the optimal configuration, and 
the CFD-informed FEA workflow provides a reliable framework for integrity evaluation and design optimisation 
of conical strainers used in the oil and gas industry. 
Keywords: conical strainer, finite element analysis , CFD - FEA coupling, fluid structure interaction,  pressure 
induced failure, structural integrity.

108 
 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
Razali et al. Scientific Contributions Oil and Gas 
How to cite this article: 
Mohd Azni Md Kasim, Mohd Azahari Razali, Nur Syafiqah Adha Narrudin, Norfakhira Mohd Nor, Iman 
Fitri Ismail, Masataro Suzuki, and Amnur Akhyan , 2026, Effect of Cone Design on the Structural 
Integrity Assessment of an Oil & Gas Conical Perforated Strainer Using CFD - Coupled Finite Element 
Analysis, Scientific Contributions Oil and Gas, 49 (3) pp. 107-129.  
  
1. Introduction 
Strainers are mechanical filtering devices used to prevent solid particles from entering and damaging the 
downstream equipment. Various types of strainers are used across numerous industries, including conical 
strainers, Y-strainers, and T -strainers (Patel et al., 2021) . A conical strainer is a cone -shaped filtering element 
installed directly between two flanges in a pipeline system , designed to  remove solid contaminants from fluids 
before they enter sensitive equipment such as heat exchangers, separators, and downstream valves. Conical 
strainers are widely used in oil and gas, chemical, and process industries due to their effective filtration 
performance, compact design, and low pressure drop (Mahmood et al., 2025; Sotoodeh 2019; Sumit et al., 2018). 
Although a conical strainer is an important piece of equipment in many industries, it is often exposed to extreme 
operating conditions, including high internal pressure, continuous fluid flow, and cyclic loading, which can lead 
to structural degradation and premature failure. A structural failure of a strainer can cause equipment damage, 
diminished flow efficiency, and compromised long-term process safety, therefore highlighting the importance of 
reliable structural design and assessment to ensure the security of process equipment (Sayinci 2015). 
Under operating conditions, the punching plate of the conical strainer is subjected to fluid pressure and flow 
acceleration through its perforations. Although these perforations are essential for the filtration process, they 
considerably reduce the effecti ve stiffness of the structure and lead to stress concentrations at the edges of the 
holes (Ghaderi et al., 2015 ; Lasenko et al., 2025 ; Luan et al., 2025 ; Xi et al., 2024) . Additionally, the inclined 
design of the conical shape introduces non -uniform stresses and complicates load transfer to supporting 
components, such as handles and ring plates, which makes it difficult to accurately predict the structure's behavior 
using conventional analytical methods (Carlomagno et al., 2012; Ruiz et al., 2015; Sayinci et al., 2015).  
Finite Element Analysis (FEA) is a computer -based engineering method used to predict how a structure or 
component will respond to real -world conditions, including forces, stress, pressure, and other loads. Various 
studies have used FEA to evaluate the inte grity of pressure -containing components, such as pressure vessels, 
piping systems, and perforated plates (Balac et al., 2018; Ganhao et al., 2021; Norske Veritas 2008), particularly 
for different types of strainers. However, prior analyses often relied on simplified geometries and assumptions 
about internal pressure loading, which did not accurately reflect the actual operational strains experienced by the 
strainers. The pressure load on strainers is significantly affected by fluid flow characteristics, obstructions, and 
flow acceleration in the vicinity of the strainers (Akhyan et al., 2025; Mahmood et al., 2025; Sotoodeh 2019).  
In 2018, (Umashankar et al., 2018)  conducted FEA to assess stress and deformation in strainer components 
subjected to internal pressure, comparing the FEA results with theoretical calculations. Their findings indicated 
that the FEA model was validated and that incorporating a stiffener into the conical strainer significantly enhanced 
safety and reduced deformation. Additionally, (Haiqal et al., 2025) used FEA to investigate stress concentration 
around holes subjected to internal pressure and flow -induced loads in strainer applications. This study 
demonstrated that FEA can accurately identify the location of maximum stress and assess the influence of hole 
patterns, plate thickness, and pressure on stress levels in strainer components.  Computational Fluid Dynamics 
(CFD) is regarded as an effective tool for modeling real behavior and pressure distribution in complex geometries. 
Several studies have investigated the combination of fluid loading based on CFD with finite element analysis 
(FEA), which can significantly enhance the reliability of structural integrity analyses for components exposed to 
flow (Bathe et al., 2004; Gu et al., 2023; Hagmeyer et al., 2022; Fadhil et al., 2021; Shakya et al., 2024; Yuan et 
al., 2022) . However, there has been limited research on CFD -FEA coupled analysis specifically for conical 
perforated strainers under contingency operating conditions in real industry applications.

109 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
While previous studies have analysed strainer stresses under idealised internal pressure, few have employed 
one-way FSI to evaluate a conical perforated strainer under contingency flow conditions in a Low Temperature 
Separation Unit, and fewer still have e xamined how a design modification intended to relieve one component 
redistributes load onto another. This study addresses that gap by coupling steady -state CFD with FEA for an in -
service strainer geometry, and by tracking the Unity Check of every structura l component — punching plate, 
strainer cap, handle and ring plate — across three design configurations and two operating conditions. 
 In this study, prolonged operation of the conical strainer in the Low Temperature Separation Unit (LTSU) led 
to structural failure, damaging the upper part of the conical punching plate near the handle connection. This failure 
indicates the need for a thorough numerical analysis to determine the governing failure mechanism and to assess 
potential design improvements. Therefore, this study aims to evaluate the structural integrity of each conic al 
strainer component using Finite Element Analysis (FEA) under fluid -induced loads. The fluid temperature, 
pressure and wall shear stress obtained from CFD are transferred to the FEA model using one-way Fluid-Structure 
Interaction (FSI) to ensure precise predictions of structural behaviour. The FEA results comprise the von Mises 
stress, displacement, strain and Unity Check (UC) of each component. Three configurations are compared: the as-
built 2 mm punching plate, a thickened 4 mm punching plate, and a 4 m m punching plate with the ring plate 
repositioned, so that changes in flow behaviour can be directly correlated with the corresponding structural 
response and the associated hydraulic penalty. 
 
2. Methodology  
2.1 Geometry and design configurations  
• Fundamental geometry  
Figure 1 illustrates the conical strainer's geometry. This geometry was developed using the design 
specifications and represents the configuration used in practical. It comprises several structural and 
functional components, including a mesh screen serving as the primary filtering surface, a ring plate 
connecting the strainer to the pipeline's flange, and a conical punching plate. This punched plate distributes 
differential pressure throughout the cone assembly and provides mechanical stability to the mesh. A 
stiffener ring and strainer cap are supplementary components that enhance the strainer's strength and 
stability during operation. This essential component of the conical strainer enables accurate modeling for 
coupled CFD-FEA analysis.  
 
Figure 1.  
LTSU Strainer Geometry

110 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
• Simulation geometry   
The fundamental geometry of the conical strainer was redrawn in SolidWorks to reflect the design 
modifications and to support both the CFD and the FEA simulations. The parameters varied in this study are 
the thickness of the conical punching plate and the axial position of the ring plate. Geometry A is the baseline 
model, reproducing the as-built strainer with a 2 mm punching plate and the ring plate in its original position. 
Geometry B doubles the punching plate thickness to 4 mm while retaining the original ring plate position, 
isolating the effect of cone stiffness alone. Geometry C retains the 4 mm punching plate but repositions the 
ring plate, achieved by extending the stiffener ring towards the region of peak stress on the upper cone, so 
that the effect of relocating the  structural support can be separated from the effect of plate thickness. The 
three configurations are summarised in Table 1 and illustrated in Figures 2 and 3. 
Table 1. 
 Conical Strainer Geometry Configuration in CFD (SolidWorks) 
 
Geometry Modification Punching Plate Thickness 
A As-built baseline model, original ring plate position 2 mm 
B Punching plate thickness doubled from the baseline model 4 mm 
C 4 mm punching plate with the ring plate repositioned by 
extending the stiffener ring 
4 mm 
 
 
Figure 2.  
Conical Strainer Model for Geometry A and B in SolidWorks (CFD), original ring plate position. 
 
 
Figure 3. 
 Conical Strainer Model for Geometry C in SolidWorks (CFD), with the ring plate repositioned.

111 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
2.2 Fluid properties  
• Thermophysical properties  
For this study, thermophysical properties were calculated from the PCHE datasheet to support 
computational fluid dynamics (CFD) and finite element analysis (FEA) of the conical strainers. These 
properties are essential for determining the specific heat at constant volume, the specific heat ratio, and the 
molecular mass. CFD and FEA analyses depend on these thermophysical properties to understand fluid 
movement and heat transfer in pipelines and strainers. Tables 2 and 3 present the thermophysical properties 
for both the standard and contingency cases in this study.  
• Actual Case: P = 30.51 bar (a), T = 94.3 °C 
Table 2. 
 Thermophysical Properties for Standard Case 
Property Value Unit  
Specific Heat Ratio (Cp/Cv) 1.202 -  
Molecular Mass 0.02897 kg/mol  
Dynamic Viscosity 0.000016 Pa*s  
Specific Heat (Cp) 1706 J/kg*K  
Thermal Conductivity 0.0370 W/(m*K)  
 
• Contingency Case: P = 36.61 bar (a), T = 113.16 °C 
Table 3. 
 Thermophysical Properties for Contingency Case 
 
 
 
 
 
• Boundary Conditions  
The initial and boundary conditions at the strainer inlet and outlet were obtained from the PCHE datasheet 
in order to reproduce the operating flow conditions and the resulting structural response. All pressures are 
specified as absolute values. Case 1 corresponds to the actual operating condition of the conical strainer. 
Case 2 corresponds to the contingency condition, in which the fluid pressure and temperature are 20% above 
Case 1. The c ontingency condition is not a hypothetical excursion: pressure spikes occur intermittently 
during normal LTSU operation, and Case 2 represents the envelope of those spikes. Simulating this condition 
is the standard means of exposing uncertainties and deficiencies in the existing strainer design, by examining 
the effect of elevated thermal and pressure loads on the pressure distribution, the pressure drop and the 
resulting mechanical stress. Table 4 summarises the boundary conditions for the two cases. 
Table 4. 
 Boundary Conditions for Case 1 and Case 2 
Boundary condition Case 1: actual Case 2: contingency Unit  
Inlet Flow Rate 653219 783862.8 kg/hr  
Outlet Flow Rate 650475 780570 kg/hr  
Inlet Fluid Pressure 30.51 36.61 bar (a)  
Temperature 94.3 113.16 °C  
Property Value Unit  
Specific Heat Ratio (Cp/Cv) 1.236 -  
Molecular Mass 0.02546 kg/mol  
Dynamic Viscosity 0.000016 Pa*s  
Specific Heat (Cp) 1706 J/kg*K  
Thermal Conductivity 0.0370 W/(m*K)

112 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
• Strainer porous media  
The filtering surface of the strainer consists of a 50 -mesh plain -weave wire screen supported by a 
perforated punching plate with a 60° staggered hole pattern. Resolving every perforation explicitly would 
require a prohibitive cell count, so the filtering surface was represented as a porous medium of equivalent 
resistance. This treatment reproduces the pressure drop and the pressure distribution across the strainer 
without modelling the individual apertures, while preserving the differential pressure that c onstitutes the 
structural load on the cone. The open area of each layer and the corresponding pressure drop were 
evaluated following Perry’s Chemical Engineers’ Handbook, Sections 6.19 –6.21(Green et al., 2008) , as 
set out below.  
For the perforated punching plate with a 60° staggered pitch, the open-area (porous) ratio is 
𝑑𝒑 =  0.91 (
𝑑
𝑃)
2
    (1) 
where d is the pore diameter (10.0 mm) and P is the hole pitch (12.0 mm), giving dp = 0.6319. 
For the plain-weave screen, the open-area ratio follows from the aperture and the wire pitch, 
𝑑𝒔 =  (
𝑂
𝑃𝒕)
2
 =  (
𝑃𝒕 − 𝑊𝒅
𝑃𝒕 )
2
,   𝑃𝒕 =
25.4
𝑛   (2) 
where O is the screen opening (0.315 mm), Wd the wire diameter (0.193 mm), and n the mesh number (50), 
giving Pt = 0.508 mm and ds = 0.3845. 
The effective opening area of the element, Ape, and the open -area ratio referred to the nozzle section area 
An are then,  
𝐴𝒑𝒆 =  𝐴𝒕 𝑑𝒑 𝑑𝒔,    𝑅 =  (
𝐴𝒑𝒆
𝐴𝒏 ) ×  100% (3) 
with At = 1.3671 m2 and An = 0.2739 m2, giving Ape = 0.3321 m2 and R = 122%. 
The total initial pressure drop across the strainer is the sum of the losses at the container nozzle, the wire 
screen, and the punching plate, 
𝛥𝑃𝒉 =  
𝐾 𝜌 𝑉𝒏2
2𝑔𝒄  , 𝑉𝒏 =  
𝑄𝒗
𝐴𝒏    (4) 
𝛥𝑃𝒔 = (
1
𝐶𝑫2) ·  (
(1 − 𝑑𝒔2)
𝑑𝒔2 ) ·  
𝜌 𝑉𝒔2 
(2𝑔𝒄)    (5) 
𝛥𝑃𝒑 =  𝑄𝒘2  (1 −(𝐴𝒇𝐴𝒕)2)2𝑔𝒄 𝜌 𝐶𝒐 2𝐴𝒇2     (6) 
𝛥𝑃𝒊 =  𝛥𝑃𝒉 +  𝛥𝑃𝒔 +  𝛥𝑃𝒑      (7) 
where 𝑘, ρ, gC, 𝑄𝑣, 𝑄𝑤,𝑉s =  𝑄v/𝐴t  𝐴𝑓, 𝐶𝐷 =  0.1 𝑁Re0.5 , and 𝐶o, are the nozzle loss coefficient (0.4), 
the fluid density, the gravitational conversion constant, the volumetric flow rate, the mass flow rate, the 
screen velocity, the open area of the punching plate (0.8638 m 2), the screen discharge coefficient and the 
orifice coefficient of the punching plate, obtained from 𝐶o(𝑃/𝑑)0.1 =  0.746 as 0.7325. The resulting 
parameters and losses are listed in Table 5.

113 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
Table 5. 
 Open-area and pressure-drop parameters of the strainer element 
Parameter Symbol Value Unit 
Pore diameter d 10.0 mm 
Hole pitch P 12.0 mm 
Plate porous ratio dp 0.6319 – 
Screen mesh number n 50 – 
Wire diameter Wd 0.193 mm 
Screen opening O 0.315 mm 
Screen porous ratio ds 0.3845 – 
Element area At 1.3671 m² 
Punching plate open area Af 0.8638 m² 
Nozzle section area An 0.2739 m² 
Element opening area Ape 0.3321 m² 
Open-area ratio R 122 % 
Nozzle loss ΔPh 0.0519 kg/cm² 
Screen loss ΔPs 0.000388 kg/cm² 
Punching plate loss ΔPp 0.0146 kg/cm² 
Total initial pressure drop ΔPi 0.0669 (0.0656 bar) kg/cm² 
 
2.3 CFD and FEA analysis  
• CFD analysis and fluid loading  
The CFD simulation evaluates the fluid flow behaviour through the conical strainer under the two 
operating conditions defined above. The analysis was performed as a steady-state, compressible calculation 
in SolidWorks Flow Simulation, which solves the Favre -averaged Navier –Stokes equations for mass, 
momentum and energy on a Cartesian immersed-body mesh. 
Turbulence was closed using the k–ε model with the damping functions of (Lam et al., 1981) , which 
describes laminar, turbulent and transitional flow of a homogeneous fluid through transport equations for the 
turbulent kinetic energy k and its dissipation rate ε: 
𝜕𝜌𝑘/𝜕𝑡 +  𝜕𝜌𝑘𝑢𝒊/𝜕𝑥𝒊 =  𝜕/𝜕𝑥𝒊 [(𝜇 +  𝜇𝒕/𝜎𝒌) 𝜕𝑘/ 𝜕𝑥𝒊]  +  𝜏𝒊𝒋𝑅   𝜕𝑢𝒊/𝜕𝑥𝒋 −  𝜌𝜀 +  𝜇𝒕𝑃𝑩             (8) 
𝜕𝜌𝜀/𝜕𝑡 +  𝜕𝜌𝜀𝑢𝒊/𝜕𝑥𝒊 =  𝜕/𝜕𝑥𝒊 [(𝜇 +  𝜇𝒕/𝜎𝜺) 𝜕𝜀/𝜕𝑥𝒊]  +  𝐶𝜺𝟏 (𝜀/𝑘) (𝑓𝟏𝜏𝒊𝒋𝑅 𝜕𝑢𝒊𝜕𝑥𝒋 
+𝐶𝑩𝜇𝒕𝑃𝑩) −  𝑓𝟐𝐶𝜺𝟐 𝜌𝜀2/𝑘      (9) 
𝜇𝒕 =  𝑓𝝁 𝐶𝝁 𝜌 𝑘2 / 𝜀          (10) 
with the standard coefficients  𝐶𝜇 = 0.09, 𝐶𝜺1 = 1.44, 𝐶ε2 =  1.92, σk =  1, σε =  1.3 and σB =  0.9, 
and with the damping functions 𝑓𝜇, 𝑓1,, and 𝑓2 acting to reduce the turbulent viscosity as the wall is 
approached (Sobachkin et al., 2014) . Near -wall behaviour is captured by the two -scale wall function 
treatment, which switches between an integrated Prandtl boundary-layer solution where the near-wall mesh 
is coarse and a direct resolution of the boundary layer where it is sufficiently refin ed. This treatment is 
important here because the filtering surface is represented as a porous medium rather than as resolved 
perforations: the wall shear stress transferred to the structural model is obtained from the boundary -layer 
solution on the equivalent porous surface rather than from the flow through individual apertures. 
Meshing used the Cartesian immersed -body approach with solution -adaptive refinement enabled at 
refinement level 3 and a cell limit of 1,563,182, so that cells were concentrated automatically in the regions 
of steepest gradient, principally the upstream fac e of the cone and the annulus around the ring plate. 
Convergence was monitored on goal -based criteria for inlet and outlet pressure, and the solution was

114 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
accepted once these goals had stabilised. It should be noted that solution -adaptive refinement improves the 
resolution of a given mesh budget but does not by itself constitute a formal grid -convergence study, since 
the refinement level and the cell limit still bound the final mesh. The solution is ran using solution-adaptive 
feature until three levels of refinement no longer changes the result of the solution by more than 3%. Because 
the comparison between the three geometries uses an identical meshing stra tegy and cell limit throughout, 
the relative differences between configurations, which form the basis of the conclusions drawn here, are 
considerably less sensitive to this uncertainty. 
• Fluid – structure interaction (FSI)  
A one-way fluid-structure interaction was adopted, whereby the pressure, temperature and wall shear 
stress fields obtained from the CFD solution were mapped onto the structural model as external loads. The 
deformation of the structure was not fed back into the CFD model, because the computed displacements are 
small relative to the flow passage dimensions — the largest resultant displacement obtained in any case was 
0.59 mm against a cone base diameter of 570 mm — and therefore have no appreciable influence on the flow 
field. This is an efficient and appropriate modelling strategy for the integrity assessment of pressure-retaining 
structural components. 
• Finite Element Analysis (FEA)  
• Material Properties 
The strainer is fabricated entirely from UNS S31803 duplex stainless steel, supplied to three 
product specifications depending on the component, as listed in Table 6. Since all components share a 
single alloy, a common set of mechanical properties was appl ied throughout the model; these are given 
in Table 7. 
Table 6. 
 Component material specifications 
Component Material specification  
Mesh screen ASTM A470 UNS S31803  
Punching plate ASTM A240 UNS S31803  
Handle ASTM A240 UNS S31803  
Strainer cap ASTM A240 UNS S31803  
Stiffener ring ASTM A815 UNS S31803  
Ring plate ASTM A815 UNS S31803  
 
Table 7. 
 Mechanical properties of UNS S31803 duplex stainless steel used in the FEA 
Property Value Unit  
Young's modulus, E 200 GPa  
Poisson's ratio, ν 0.30 –  
Density, ρ 7800 kg/m³  
Specified minimum yield strength 448 MPa  
Allowable stress adopted 336 MPa  
 
The allowable stress of 336 MPa was not derived from a pressure-vessel design code. It is the working 
stress adopted for this assessment, equal to 75% of the specified minimum yield strength of UNS S31803, 
so that the Unity Check functions as the reciprocal of the safety factor against that limit: UC = 1.0 
corresponds to a factor of 1.33 on yield, and the material remains elastic at UC = 1.0. The same allowable 
stress was applied at both 94.3 °C and 113.16 °C without te mperature derating. This is a stated 
assumption of the analysis rather than a code -based position, and it is mildly non -conservative at the 
contingency temperature, where the yield strength of duplex stainless steel is somewhat reduced relative

115 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
to its room-temperature value. The structural analysis of the conical strainer was conducted using finite 
element analysis. The finite element model used a blended curvature -based mesh comprising 88,340 
nodes and 43,659 elements, as shown in Figures 4 and 5. 
 
Figure 4.  
 Blended-Curvature Mesh 
 
Table 8. 
FEA Mesh Quality Metrics in CFD Software  
Mesh quality metrics Value Remarks 
Max element size 97.4mm None 
Min element size 4.87mm None 
Total nodes 88,340 None 
Total elements 43,659 None 
Max aspect ratio (AR) 75.483 None 
% of Elements with AR<3 = 97.86 97.86% Fulfilled FEA mesh criteria 
% of Elements with AR > 10 1.07% Fulfilled FEA mesh criteria 
 
This mesh was acceptable for stress analysis since more than 97% of the elements had an aspect ratio 
(AR) below 3, as shown in Figure 5. The aspect ratio influences the analysis outcome appreciably, since 
elements with high aspect ratios degrade solution accuracy. The Unity Check (UC), defined as the ratio 
of the maximum von Mises stress in a component to the allowable stress of 336 MPa, was used to evaluate 
the structural integrity of each conical strainer component in both cases. Values below unity indicate 
acceptable performance; values above unity indicate that the component is not structurally acceptable.

116 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 5.  
 Aspect Ratio (AR) of the conical strainer. 
 
3. Result and Discussion  
3.1 von Mises Stress, Displacement & Strain 
• Geometry A – 2 mm punching plate 
Figures 6 and 7 present the von Mises stress, displacement and strain distributions for Geometry A 
under actual (Case 1) and contingency (Case 2) conditions. In both cases the maximum stress and strain are 
concentrated on the upper surface of the conical punching plate n ear the handle connection, which is the 
location at which the in -service failure occurred. Under Case 1 the peak von Mises stress in the punching 
plate is 293.2 MPa, giving UC = 0.87, with a maximum resultant displacement of 0.4585 mm and a maximum 
equivalent strain of 1.051 × 10⁻³. The baseline design is therefore acceptable under normal operating 
conditions, although the margin against the allowable stress is only 13%. 
Under Case 2 the peak stress rises to 371.8 MPa, an increase of 26.8%, and exceeds the allowable stress 
to give UC = 1.11. The maximum displacement increases by 27.9% to 0.5863 mm and the maximum 
equivalent strain by 27.5% to 1.340 × 10⁻³, while the high -stress region spreads over a substantially larger 
portion of the cone. The governing mechanism is flow -induced bending rather than membrane action. The 
perforations remove a large fraction of the load -bearing area — the plate porous ratio is 0.6319, so only  
about 37% of the nominal plate section carries load — and the resulting loss of flexural stiffness allows the 
unsupported span of the cone between the ring plate and the handle to bend under the differential pressure. 
Bending stress concentrates in the ligaments between adjacent holes at the restrained upper edge, producing 
the localised peak observed. These results confirm that the 2 mm punching plate of Geometry A lacks 
structural integrity under the pressure spikes encountered during service and is susceptible to the failure that 
was observed in operation.

117 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 6.  
von Mises Stress, Displacement and Strain for Geometry A, Case 1 (actual condition)

118 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
 
Figure 7. 
 von Mises Stress, Displacement and Strain for Geometry A, Case 2 (contingency condition)

119 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
• Geometry B – 4 mm punching plate 
Doubling the punching plate thickness to 4 mm increases the flexural rigidity of the cone by 
approximately a factor of eight, and the effect on the punching plate is correspondingly large. Figures 8 
and 10 show the results for Case 1 and Case 2 respectively. Under Case 1 the peak stress in the punching 
plate falls from 293.2 MPa to 253.6 MPa, a reduction of 13.5%, giving UC = 0.75, while the maximum 
displacement falls by 6.6% from 0.4585 mm to 0.4284 mm. Under Case 2 the peak stress falls from 371.8 
MPa to 322.0 MPa, a reduction of 13.4%, bringing the Unity Check from 1.11 to 0.96 and thereby restoring 
compliance under contingency conditions. The maximum displacement under Case 2 falls by 7.0% from 
0.5863 mm to 0.5455 mm. 
The more important consequence of the modification, however, is not the reduction in punching plate 
stress but the redistribution of load that accompanies it. A stiffer cone transfers a greater share of the 
pressure load into its supports, and the peak str ess in the ring plate rises from 318.8 MPa to 333.8 MPa 
under Case 2, taking its Unity Check from 0.95 to 0.99. The critical component therefore migrates from 
the punching plate to the ring plate, which retains a margin of less than 1% against the allowabl e stress. 
The same effect explains an apparent anomaly in the strain results: the maximum equivalent strain 
increases marginally from 1.051 × 10⁻³ to 1.075 × 10⁻³ under Case 1 and from 1.340 × 10⁻³ to 1.362 × 10⁻³ 
under Case 2, despite the reduction in punching plate stress, because the location of peak strain has moved 
off the cone and onto the more highly loaded ring plate. Geometry B is thus structurally acceptable in both 
cases, but it is acceptable with a very small reserve, and it is acceptable at a different location from the one 
that the modification was designed to protect. The hydraulic cost is modest: the pressure drop increases by 
8.3% under Case 1 and 8.4% under Case 2. 
• Geometry C – 4 mm Punching Plate with Repositioned Ring Plate 
Geometry C retains the 4 mm punching plate of Geometry B but repositions the ring plate by extending 
the stiffener ring towards the upper cone, where the peak stress in Geometries A and B was located. Figures 
10 and 11 present the corresponding stress, displacement and strain distributions. Moving the support 
closer to the region of maximum differential pressure shortens the unsupported span of the cone and 
reduces the bending moment carried by the punching plate. The p eak stress in the punching plate falls 
further to 245.7 MPa under Case 1 (UC = 0.73) and 304.6 MPa under Case 2 (UC = 0.91), a reduction of 
5.4% relative to Geometry B and 18.1% relative to the baseline under contingency conditions. The 
maximum displacement falls to 0.4029 mm and 0.5133 mm for the two cases, 12.1% and 12.5% below the 
baseline values. 
The effect on the ring plate is more pronounced still. Its peak stress under Case 2 collapses from 333.8 
MPa in Geometry B to 100.8 MPa, taking its Unity Check from 0.99 to 0.30, a reduction of 70%. The 
repositioned ring plate no longer terminates the prim ary bending load path of the cone but instead shares 
the reaction with the extended stiffener ring, so that neither component approaches its allowable stress. 
Geometry C is consequently the only configuration in which every component retains a substantial reserve 
under contingency conditions, the highest Unity Check being 0.91 in the punching plate. The strainer cap 
and the handle remain lightly loaded throughout, with Unity Checks not exceeding 0.15 and 0.76 
respectively in any configuration or case, and neither is at any point critical.

120 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 8.  
 von Mises Stress, Displacement and Strain for Geometry B, Case 1 (actual condition)

121 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 9.  
von Mises Stress, Displacement and Strain for Geometry B, Case 2 (contingency condition)

122 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 10. 
 von Mises Stress, Displacement and Strain for Geometry C, Case 1 (actual condition)

123 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
 
Figure 11. 
von Mises Stress, Displacement and Strain for Geometry C, Case 2 (contingency condition)

124 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
3.2 Unity check values  
Figure 12 and Tables 8 and 9 summarise the Unity Check values for all four components across the three 
geometries and both operating conditions. The punching plate governs the structural integrity of the baseline 
design: the Unity Check of Geometry A is 0.87 under Case 1 and 1.11 under Case 2,  so that the as-built strainer 
is compliant in normal operation but is driven past its allowable stress by the pressure spikes represented by the 
contingency case. This is consistent with the observed service history, in which failure developed after prolonged 
operation rather than immediately on commissioning. 
Thickening the punching plate to 4 mm in Geometry B lowers its Unity Check to 0.75 and 0.96 for the two 
cases, restoring compliance, but simultaneously raises the ring plate to 0.99 under contingency conditions. The 
modification therefore relocates the criticality rather than eliminating it, and the resulting design is compliant only 
by a margin of about 1%. Repositioning the ring plate in Geometry C addresses both components at once, reducing 
the punching plate to 0.73 and 0.91 and the ring plate to 0.79 a nd 0.30. Geometry C is thus the recommended 
configuration. 
Table 8. 
 Maximum von Mises stress and Unity Check by component, Case 1 (actual condition) 
Component Geom. A Geom. B Geom. C  
Punching plate 293.2 / 0.87 253.6 / 0.75 245.7 / 0.73  
Strainer cap 39.5 / 0.12 35.1 / 0.10 35.1 / 0.10  
Handle 200.5 / 0.60 200.4 / 0.60 200.5 / 0.60  
Ring plate 250.4 / 0.75 262.4 / 0.78 264.0 / 0.79  
 
Values are given as maximum von Mises stress (MPa) / Unity Check (–). 
Table 9. 
Maximum von Mises stress and Unity Check by component, Case 2 (contingency condition) 
Component Geom. A Geom. B Geom. C 
 
Punching plate 371.8 / 1.11 322.0 / 0.96 304.6 / 0.91  
Strainer cap 50.2 / 0.15 44.6 / 0.13 47.1 / 0.14  
Handle 254.8 / 0.76 254.8 / 0.76 254.8 / 0.76  
Ring plate 318.8 / 0.95 333.8 / 0.99 100.8 / 0.30  
 
Values are given as maximum von Mises stress (MPa) / Unity Check ( –). The Unity Check exceeding unity 
for Geometry A under contingency conditions is shown in bold in Figure 12. 
Table 10. 
Global structural response and hydraulic penalty. Δ(%) is the change in pressure drop relative to the Geometry A baseline for 
the same case 
Geom. Case Displ. (mm) Strain (×10⁻³) Δp (Pa) Δ (%) 
 
A 1 0.4585 1.051 7273 –  
A 2 0.5863 1.340 9097 –  
B 1 0.4284 1.075 7873 +8.3  
B 2 0.5455 1.362 9862 +8.4  
C 1 0.4029 1.055 8705 +19.7  
C 2 0.5133 1.340 10894 +19.8  
 
The improvement in structural performance delivered by Geometry C is not free. As Table 10 shows, 
repositioning the ring plate increases the pressure drop across the strainer by 19.7% under Case 1 and 19.8% under 
Case 2 relative to the baseline, and by app roximately 10.5% relative to Geometry B. The extended stiffener ring

125 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
presents an additional obstruction to the flow on the lower side of the cone, forcing the flow to accelerate through 
a reduced passage and raising the local velocity on the upper side of the strainer, as shown in Figure 13. The trade-
off in this design is therefore between structural reserve and hydraulic performance, and not, as might be assumed, 
between adding material and degrading the structure. Whether the 19.8% pressure -drop penalty is acceptable 
depends on the available differential pressure budget of the LTSU; the total loss remains small in absolute terms, 
at approximately 0.11 bar under contingency conditions. 
 
Figure 12. 
Unity Check values by component for all geometries under both operating conditions 
 
 
Figure 13. 
 Increased flow velocity on the upper side of the strainer in Geometry C (CFD plot).

126 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
4. Conclusion  
This study presented a coupled CFD -FEA analysis for the structural integrity assessment of a conical 
perforated strainer subjected to fluid -induced loading under actual and contingency operating conditions. The 
punching plate was identified as the component governing the integrity of the baseline design, ow ing to the 
combination of a large pressure-acting area and the low flexural stiffness that results from its perforations. For the 
as-built 2 mm punching plate the Unity Check was 0.87 under actual conditions but 1.11 under contingency 
conditions, confirming that the design is compliant in normal operation yet driven past its allowable stress of 336 
MPa by the pressure spikes that occur intermittently in service, which is consistent with the failure observed after 
prolonged operation. Doubling the punching p late thickness to 4 mm reduced the peak contingency stress by 
13.4%, from 371.8 MPa to 322.0 MPa, and the Unity Check to 0.96. This modification did not, however, eliminate 
the criticality but relocated it: the stiffer cone transferred load into its suppor ts and raised the ring plate Unity 
Check from 0.95 to 0.99, leaving a reserve of less than 1%. Repositioning the ring plate by extending the stiffener 
ring towards the region of peak stress addressed both components simultaneously, reducing the punching pl ate 
Unity Check to 0.91 and the ring plate Unity Check to 0.30, at the cost of a 19.7% increase in pressure drop, from 
7273 Pa to 8705 Pa under actual conditions. This configuration is recommended as the optimal design, since it is 
the only one in which ev ery component retains a substantial reserve under contingency conditions while the 
hydraulic penalty remains small in absolute terms. 
The wider contribution of this work lies in the workflow rather than in the specific geometry. The sequence 
adopted here — representing the filtering surface as an equivalent porous medium, obtaining the pressure, 
temperature and wall shear stress fields from a steady-state CFD solution, mapping them onto the structure through 
one-way fluid-structure interaction, and then evaluating a Unity Check for every component rather than for the 
component presumed to be critical — can be standardised for the assessment of other pipeline filtration systems 
in the oil and gas industry, including Y-strainers, T-strainers and basket strainers. The component-wise evaluation 
is the essential element: had only the punching plate been assessed, Geometry B would have been repo rted as an 
adequate remedy, when in fact it leaves the ring plate within 1% of its allowable stress. Design modifications 
intended to relieve one component should therefore always be verified against the full set of load paths, and the 
associated hydraulic penalty quantified alongside the structural gain. 
 
5. Acknowledgement  
Communication of this research is made possible through monetary assistance by Universiti Tun Hussein Onn 
Malaysia and the UTHM Publisher’s Office via Publication Fund E15216. This research was also supported by 
the UTHM Research Management Centre (RMC) th rough the GPPS Fund Q797. The authors would also like to 
thank the Faculty of Mechanical and Manufacturing Engineering, Universiti Tun Hussein Onn Malaysia, for its 
support. 
 
6. Declarations  
The authors declare that this manuscript presents original work, has not been published previously, and is not 
under consideration for publication elsewhere.  
6.1 Author contributions  
The authors confirm contribution to the paper as follows: study conception and design: Mohd Azni Md 
Kasim and Mohd Azahari Razali; data collection: Mohd Azni Md Kasim and Iman Fitri Ismail; analysis and 
interpretation of results: Mohd Azni Md Kasim, Iman F itri Ismail, and Nur Syafiqah Adha Narrudin; draft 
manuscript preparation: Mohd Azni Md Kasim, Nur Syafiqah Adha Binti Narrudin, Iman Fitri Ismail, 
Norfakhira Mohd Nor, Amnur Akhyan, and Masataro Suzuki. All authors reviewed the results and approved 
the final version of the manuscript.

127 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
6.2 Funding statement  
This research received monetary assistance from UTHM Publisher’s Office via Publication Fund E15216 and 
was supported by the UTHM Research Management Center (RMC) through the GPPS Fund Q797.  
6.3 Competing interest 
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper.  
6.4 The use of AI or AI-assisted technologies  
During the preparation of this manuscript, the authors used AI -based writing and editing assistance tools to 
support language refinement, formatting, and reference organization. All scientific content, data interpretation, 
and conclusions are the sole responsibility of the authors, who reviewed and edited all AI-assisted output and take 
full responsibility for the content of this publication.  
 
7. Glossary of terms and symbols  
 Terms & 
symbols Definitions Unit 
 LTSU Low temperature separation unit - 
 CFD Computational fluid dynamics - 
 FEA Finite element analysis - 
 UC Unity check - 
 FSI Fluid-structure interaction - 
 Cp Specific heat J/kg*K 
 AR Aspect ratio - 
 Δ(%) The change in pressure drop relative - 
 
 
8. References  
Akhyan, A., Bin Razali, M. A., Hendriko, Mahzan @ Mohd Zin, S. Bin, & Bin Ismail, I. F. (2025). Porosity-
Controlled Flow Instability and Vibration Response in Conical Strainers: An Integrated Hydraulic -Structural 
Evaluation. Scientific Contributions Oil and Gas, 48(4), 309–321. https://doi.org/10.29017/scog.v48i4.1960 
Akhyan, A., Hussein, M. D., & Bin Razali, M. A. (2025). Influence of Installation Orientation and Cone Angle 
on Pressure Drop and Filtration Efficiency of Conical Strainers. Scientific Contributions Oil and Gas, 48(3), 
303–320. https://doi.org/10.29017/scog.v48i3.1910 
Balac, M., Grbovic, A., Petrovic, A., & Popovic, V. (2018). Fem analysis of pressure vessel with an investigation 
of crack growth on cylindrical surface. Eksploatacja i Niezawodność – Maintenance and Reliability, 20(3), 
378–386. https://doi.org/10.17531/ein.2018.3.5 
Bathe, K., & Zhang, H. (2004). Finite element developments for general fluid flows with structural interactions. 
International Journal for Numerical Methods in Engineering, 60(1), 213–232. https://doi.org/10.1002/nme.959 
Carlomagno, M., Rossin, S., Delvecchio, M., & Anichini, A. (2012). Experimental and Numerical Validation of 
Conical Strainer Fluid/Structural Performance Model. Volume 6: Oil and Gas Applications; Concentrating 
Solar Power Plants; Steam Turbines; Wind Energy, 155–171. https://doi.org/10.1115/GT2012-69751 
Ganhao, L. A., Perdomo, J. J., McVay, J., & Seijas, A. (2021). Failures of Pressure Vessels and Process Piping. 
In Analysis and Prevention of Component and Equipment Failures (pp. 565 –637). ASM International. 
https://doi.org/10.31399/asm.hb.v11A.a0006812

128 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
Ghaderi, M., Ayerden, N. P., de Graaf, G., & Wolffenbuttel, R. F. (2015). Minimizing stress in large-area surface 
micromachined perforated membranes with slits. Journal of Micromechanics and Microengineering, 25(7), 
074010. https://doi.org/10.1088/0960-1317/25/7/074010 
Gu, N., Liang, D., Zhou, X., & Ren, H. (2023). A CFD -FEA Method for Hydroelastic Analysis of Floating 
Structures. Journal of Marine Science and Engineering, 11(4), 737. https://doi.org/10.3390/jmse11040737 
Hagmeyer, N., Mayr, M., Steinbrecher, I., & Popp, A. (2022). One-way coupled fluid–beam interaction: capturing 
the effect of embedded slender bodies on global fluid  flow and vice versa. Advanced Modeling and Simulation 
in Engineering Sciences, 9(1), 9. https://doi.org/10.1186/s40323-022-00222-y 
Haiqal, M., Akhyan, A., Yanda Zaira, J., Novison, R., Rianto, R., & Azahari Bin Razali, M. (2025). Numerical 
Study of Finite Element Analysis (FEA) of Stress and Deformation in Strainer. Journal of Ocean, 69(2), 168–
177. www.isomase.org., 
Lam, C. K. G., & Bremhorst, K. (1981). A Modified Form of the k -ε Model for Predicting Wall Turbulence. 
Journal of Fluids Engineering, 103(3), 456–460. https://doi.org/10.1115/1.3240815 
Lasenko, I., Mironovs, V., Akishin, P., Osipova, M., Sirotkina, A., & Skromulis, A. (2025). Influence of 
Perforation on Elastic Modulus and Shear Modulus of Lightweight Thin -Walled Cylindrical Shells. Metals, 
15(11), 1263. https://doi.org/10.3390/met15111263 
Li, S., Davidson, L., & Peng, S.-H. (2024). A pressure-loss model for flow-through round-hole perforated plates 
of moderate porosity and thickness in laminar and turbulent flow regimes. International Journal of Heat and 
Mass Transfer, 226, 125490. https://doi.org/10.1016/j.ijheatmasstransfer.2024.125490 
Luan, Z., Zhong, L., Feng, W., Li, J., Gao, Z., & Li, J. (2025). A Review of Failures and Malfunctions in Hydraulic 
Sandblasting Perforation Guns. Applied Sciences, 15(9), 4892. https://doi.org/10.3390/app15094892 
Mahmood Kia, S., & Ahmad Kia, S. (2025). Numerical Optimization and Analysis of Pressure Drop in Industrial 
Basket Strainers for Diesel and Water Flows Citation. Journal of Environmental Engineering and Energy, 2(1), 
64–75. https://doi.org/10.22105/jeee.v2i1.34 
Min, I., Choi, J., Kim, G., & Jo, H. (2024). CFD Analysis of the Pressure Drop Caused by the Screen Blockage 
Rate in a Membrane Strainer. Processes, 12(4), 831. https://doi.org/10.3390/pr12040831 
Motriuk, R. W. (2003). A Perforated Conical Strainer as an Example of an Acoustic Noise Generator. Flow -
Induced Vibration, 185–191. https://doi.org/10.1115/PVP2003-2089 
Muhammad Fadhil, Aditya Prayoga, Andi Eriawan, Erwin Sulaeman, & Ari Legowo. (2021). Aerodynamic 
Pressure Mapping Technique from CFD to FEM Model of N219 Winglet. CFD Letters, 13(12), 90 –99. 
https://doi.org/10.37934/cfdl.13.12.9099 
Ogunnowo, E., Awodele, D., Parajuli, V., & Zhang, N.  (2015). Design and Development of New Debris Strainer 
in Water Treatment Plant. Procedia Computer Science, 76, 209 –216. 
https://doi.org/10.1016/j.procs.2015.12.344 
Norske Veritas, D. (2008). RECOMMENDED PRACTICE STRUCTURAL ANALYSIS OF PIPING 
SYSTEMS. http://webshop.dnv.com/global/, 
Ogunnowo, E., Awodele, D., Parajuli, V., & Zhang, N. (2023). CFD Simulation And Optimization Of A Cake 
Filtration System . International Mechanical Engineering Congress and Exposition. 
http://asmedigitalcollection.asme.org/IMECE/proceedings-
pdf/IMECE2023/87660/V009T10A009/7239804/v009t10a009-imece2023-112836.pdf 
Panmongkol, P., & Poljaroen, T. (2024). The Study And Optimum Design Of The Strainer Plate In The Filter 
Tank By Using The Finite Element Method . Pibulsongkram Rajabhat University Journal. https://ph02.tci-
thaijo.org/index.php/psru-jite/article/view/251900

129 
 
 
Razali et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2130 
 
 
Patel, M. A., & Saheb, S. H. (2021). Study on Design and Analysis of Industrial Y Type Strainer. IOP Conference 
Series: Materials Science and Engineering, 1126(1), 012025. https://doi.org/10.1088/1757-
899x/1126/1/012025 
Ruiz, R. O., Lopez-Garcia, D., & Taflanidis, A. A. (2015). An efficient computational procedure for the dynamic 
analysis of liquid storage tanks. Engineering Structures, 85, 206 –218. 
https://doi.org/10.1016/j.engstruct.2014.12.011 
Sayinci, B. (2015). Effect of strainer type, spray pressure, and orifice size on the discharge coefficient of standard 
flat-fan nozzles. Turkish Journal of Agriculture and Forestry, 39(5), 692 –704. https://doi.org/10.3906/tar-
1410-89 
Sayinci, B., & Kara Mazhar. (2015). The effects of strainer types on flow characteristics of anti -drift (AD) and 
multi-range (LU) flat -fan nozzles. Journal of Agricultural Sciences, 21(4), 558 –571. 
https://doi.org/10.1501/Tarimbil_0000001357 
Shakya, P., Thomas, M., Seibi, A. C., Shekaramiz, M., & Masoum, MohammadA. S. (2024). Fluid -structure 
interaction and life prediction of small -scale damaged horizontal axis wind turbine blades. Results in 
Engineering, 23, 102388. https://doi.org/10.1016/j.rineng.2024.102388 
Sobachkin, A., & Dumnov, G. (2014). Numerical Basis of CAD -Embedded CFD White. 
https://www.semanticscholar.org/paper/Numerical-Basis-of-CAD-Embedded-CFD-White-Sobachkin-
Dumnov/56f54b31c528c588cfb465d953c2b0f24ea9e297 
Sotoodeh, K. (2019). Handling the pressure drop in strainers. Marine Systems & Ocean Technology, 14(4), 220–
226. https://doi.org/10.1007/s40868-019-00063-2 
Sumit, S., & Santosh, W. (2018). Optimization of large size fabricated Y -Strainers for improvement in pressure 
drop value using CFD analysis. International Journal of Advance Research, 4(4). www.IJARIIT.com 
Tanner, P., Gorman, J., & Sparrow, E. (2019). Flow –pressure drop characteristics of perforated plates. 
International Journal of Numerical Methods for Heat & Fluid Flow, 29(11), 4310 –4333. 
https://doi.org/10.1108/HFF-01-2019-0065 
Umashankar, M., & Santhosh, G. S. (2018). Design of Conical Strainer and Analysis Using FEA. International 
Journal of Engineering Science Invention (IJESI), 7(2), 61–65. www.ijesi.org 
Wang, P., Pan, W., & Dai, G. (2020). A CFD‐based design scheme for the perforated distributor with the control 
of radial flow. AIChE Journal, 66(5). https://doi.org/10.1002/aic.16901 
W. Green, D., & H.Perry, R. (2008). Perry’s Chemical Engineers’ Handbook. 
https://mathguy.us/BySubject/Chemistry/Perrys_Chemical_Engineers_Handbook.pdf 
Xi, Y., Yao, Y., Chen, P., Li, J., Wang, H., & Li, H. (2024). Investigation of casing stress distribution and 
parameter optimization during the transient impact process of multi -hole perforation operations. Engineering 
Failure Analysis, 155, 107761. https://doi.org/10.1016/j.engfailanal.2023.107761 
Yuan, J., Shi, J., Fu, Y., Chen, H., Lu, R., & Hou, X. (2022). Analysis of Fluid -Structure Coupling Dynamic 
Characteristics of Centrifugal Pump Rotor System. Energies, 15(6), 2133. https://doi.org/10.3390/en15062133 
Zhang, H., Kong, N., Song, Y., Niu, Z., & Peng, C. (2024). Study on the safety of a magnetic strainer at the 
deaerator outlet under two-phase and large-scale flow fields. Chemical Engineering Research and Design, 205, 
802–821. https://doi.org/10.1016/j.cherd.2024.04.037
