---
source_id: "lemigas-scog"
title: "Impact of CO2 Induced Geochemical Alteration on The Mechanical Integrity of Reservoir and Caprock in Saline Aq"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2135"
retrieved_at: "2026-10-24T14:30:28+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "20570cf42bef3a1d8f0a4db56adcd6a5d629c20b6960274aa5094d68813c9ac3"
collected: "manual"
---

# Impact of CO2 Induced Geochemical Alteration on The Mechanical Integrity of Reservoir and Caprock in Saline Aq

607 
 
https://doi.org/10.29017/scog.v49i3.2135 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 607 – 645 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Impact of CO2 -Induced Geochemical Alteration on The Mechanical 
Integrity of Reservoir and Caprock in Saline Aquifers 
 
Citra Fitria, Novia Rita*, and Ayyi Husbani 
 
Department of Petroleum Engineering, Faculty of Engineering, Universitas Islam Riau 
Kaharuddin Nasution Street No. 113, Simpang Tiga, Pekanbaru, Riau, Indonesia. 
*Corresponding author: Novia Rita (noviarita@eng.uir.ac.id)  
Novia Rita: https://orcid.org/0009-0004-8478-4013  
Received:  27 Februari 2026; Revised: in revised form 27 April 2026; Accepted: 01 June 2026 
Available: online 30 September 2026. 
 
 
 
 
ABSTRACT - Rising carbon dioxide (CO₂) emissions accelerate the deployment of Carbon Capture and Storage 
(CCS) in saline aquifers, yet the quantitative integration of geochemical alteration and geomechanical response 
remains limited, particularly in assessing effecti ve stress and the fracture-pressure margin. This study addresses 
this gap using a fully coupled geochemistry–geomechanics workflow in CMG-GEM that links mineral reactions, 
petrophysical evolution, and geomechanical response with global (Sobol) sensitivity analysis. A homogeneous 
sandstone reservoir at a depth of 1200 m, with an initial porosity of 0.18 and permeability of 200 mD, undergoes 
10 years of CO₂ injection followed by 500 years of post -injection monitoring. The results show that mineral 
dissolution modifies reservoir properties, while pore pressure increases from 11.8 to 15.8 MPa, corresponding to 
an 18–20% reduction in effective stress. With an estimated fracture pressure of 19.0 MPa, the resulting safety 
margin is 3.2 MPa (safety ratio of 1.20), i ndicating stable conditions without caprock failure. Pressure is the 
dominant sensitivity parameter, contributing 59% of the sensitivity. These findings provide a quantitative basis 
for evaluating safe injection-pressure conditions and prioritizing pressure management in long-term CO₂ storage 
and monitoring strategies. 
Keywords: Carbon capture and storage (CCS), geochemical alteration, mechanical integrity, saline aquifers, 
CO₂–brine–rock interaction  
 
 
How to cite this article: 
Citra Fitria, Novia Rita, and Ayyi Husbani, 2026, Impact of CO2 -Induced Geochemical Alteration on 
The Mechanical Integrity of Reservoir and Caprock in Saline Aquifers, Scientific Contributions Oil and 
Gas, 49 (3) pp. 607-645.

608 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
1. Introduction 
Increasing carbon dioxide (CO₂) emissions from industrial activities and fossil -fuel combustion have driven 
the development of Carbon Capture and Storage (CCS) as a key climate change mitigation strategy (Ramadhani 
et al., 2025). CO₂ storage in deep geological formations, particularly saline aquifers, is considered promising due 
to their large storage capacity and wide distribution (Worden 2024). However, the success of CCS implementation 
depends not only on storage capacity but also on the long-term geochemical stability and mechanical integrity of 
both the reservoir rock and caprock (Fentaw et al., 2024). 
Interactions between injected CO₂, form ation water, and rock minerals can trigger geochemical reactions 
that alter the physical and mechanical properties of the storage system. Dissolution of carbonate minerals and 
changes in fluid ionic composition may modify rock porosity and permeability (Fani et al., 2024) . Over longer 
timescales, dissolution and precipitation of silicate minerals can lead to pore redistribution and microstructural 
changes that influence fluid -flow pathways and reservoir stability (Chen et al., 2025;  A. Zhang et al., 2024) . 
Caprock integrity is critical for preventing CO₂ migration. Previous studies have reported that interactions 
between CO₂ and clay minerals may reduce rock c ohesion and increase the potential for microfracture 
development (Kanin et al., 2025;  Yang 2024). 
Integrated numerical approaches combining geochemical and geomechanical processes enable the evaluation 
of coupled physicochemical interactions over long timescales (Helei et al., 2021). Recent studies have addressed 
these interactions from different perspectives. (Shi et al., 2024)  reviewed geoch emical–geomechanical 
interactions across CO₂, H₂, and air storage systems but did not develop a quantitative, site -specific workflow. 
(Kanin et al., 2025) proposed a geomechanical risk-assessment framework for saline aquifers but did not explicitly 
couple geomechanical analysis with reactive mineral transport. (Eyitayo et al., 2025)  investigated supercritical 
CO₂–brine–rock geochemical interactions under different injection strategies and  discussed implications for 
mechanical integrity, but did not incorporate global sensitivity analysis to rank controlling parameters. Collectively, 
these studies demonstrate the interdependence of geochemical and geomechanical processes; however, existing 
approaches often evaluate them sequentially or with limited quantitative coupling. Consequently, the feedback 
from mineral dissolution and precipitation to effective stress,  fracture-pressure margin, and safe operating 
conditions remains insufficiently resolved within a single, reproducible framework. 
This study addresses this gap by integrating reactive transport, geomechanical analysis, and global 
sensitivity analysis within a unified numerical framework. The novelty is threefold: (1) a fully coupled, two -
way geochemical –geomechanical simulation in which mineral -reaction-driven changes in porosity and 
permeability are propagated into effective -stress and fracture -pressure-margin calculations; (2) quantitative 
evaluation of the timing and magnitude of dissolution of calcite, dolomite, and illite and precipitation of K -
feldspar, quartz, and kaolinite over a 500 -years post -injection period, linking mineral -scale reactions to 
reservoir-scale mechanical response; and (3) application of global ( Sobol) sensitivity analysis to rank the 
relative influence of pressure, pH, temperature, injection rate, porosity, and permeability and identify the 
dominant parameter for pressure management.  
Accordingly, the objectives of this study are to: (i) quantify geochemical alteration in a representative 
sandstone reservoir under CO₂ injection using a fully coupled reactive -transport–geomechanics model; (ii) 
evaluate the evolution of pore pressure, effective stress, and caprock fracture-pressure margin over 10 years of 
injection and 500 years of post-injection monitoring; and (iii) identify the dominant controlling parameter through 
global sensitivity analysis to support the evaluation of safe operating pressure conditions for CO₂ storage in saline 
aquifers. This study provides a reproducible, quantitative workflow that can support site -specific pressure -
management and long-term integrity assessment for geological CO₂ storage. 
 
2. Methodology 
The simulation workflow integrates geochemical kinetics, porosity evolution, and geomechanical assessment 
within a fully coupled framework implemented in CMG -GEM. This framework enables the simultaneous

609 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
quantification of CO₂–brine–rock interactions, the evolution of petrophysical properties, and stress redistribution 
(Sugihardjo 2022). This integrated approach goes beyond conventional methodologies that treat these processes 
as separately (decoupled) by directly linking min eral reactions to the evolution of pore pressure and the  
mechanical stability of the caprock, thereby providing a more accurate and predictive basis for evaluating fracture 
pressure margins and safe operating limits for long-term CO₂ storage. 
2.1 Simulation framework 
The simulation workflow integrates geochemical reactions, petrophysical evolution, fluid-flow behavior, and 
geomechanical response within a numerical framework implemented in CMG-GEM. The model is designed 
to quantify the coupled response of a deep saline aquifer to CO₂ injection by linking CO₂–brine–rock interactions 
with changes in pore pressure, porosity, permeability, effective stress, and caprock stability. The workflow consists 
of four sequentially connected components: (1) reservoir and f luid initialization,  (2) reactive geochemical 
modeling, (3) geomechanical assessment, and (4) global sensitivity analysis. Mineral reactions are calculated 
using a kinetic formulation based on Transition State Theory (TST), while changes in mineral volume are used to 
evaluate the resulting evolution of porosity and permeability. The simulated  pressure response is subsequently 
used to evaluate effective stress and the fracture-pressure margin of the reservoir–caprock system. 
The simulation was conducted from 2024 to 2534, consisting of 10 years of CO₂ injection from 2024 to 2034, 
followed by 500 years of post-injection monitoring from 2034 to 2534. This extended monitoring period enables 
evaluation of both the short-term pressure response during injection and the long-term evolution of geochemical 
and geomechanical conditions after injection ceases. 
2.2 Software and Computational Environment 
The numerical simulations were conducted using CMG-GEM version 2021.10 (Computer Modelling Group). 
CMG-GEM is a compositional reservoir simulator used in this study to model multiphase flow, CO₂ –brine–rock 
interactions, and geochemical reactions during CO₂ storage. The simulator was used to obtain the reservoir 
pressure, CO₂ saturation, mineral dissolution and precipitation, po rosity, and permeability responses throughout 
the injection and post-injection periods. 
CMOST-AI version 2021.10 was used for the global sensitivity analysis. The Sobol variance -decomposition 
method was applied to evaluate the contributions of the investigated parameters, including reservoir pressure, pH, 
temperature, CO₂ injection rate, permeability, and porosity, to the simulated mineral-precipitation response. 
Both software modules were operated through the CMG Technologies Launcher version 2021.10. The 
simulation results generated by CMG-GEM were subsequently used for the evaluation of effective stress, fracture 
pressure, pressure safety margin, and safety ratio presented in the geomechanical analysis. 
2.3 Reservoir model and initial conditions 
A three -dimensional (3D) synthetic saline -aquifer model was constructed using CMG -GEM based on 
representative reservoir and fluid properties reported by (Bentham et al., 2017;  Ranganathan et  al., 2011;  
Wilkinson et al., 2009). The reservoir is represented by a homogeneous sandstone formation overlain by a low -
permeability shale caprock. No geological faults are included in the base-case model in order to isolate the effects 
of CO₂–brine–rock interactions and pressure-induced stress changes. 
The reservoir top is located at a depth of 1200 m. The initial reservoir porosity and permeability are 0.18 and 
200 mD, respectively. The initial temperature is 80 °C, initial pressure is 11.8 MPa, and formation-water salinity is 
50,000 ppm. CO₂ is injected through a single vertical well under bottom-hole-pressure (BHP) control for 10 years. 
After the injection period, the well is shut in and the system is monitored for an additional 500 years. 
The reservoir and caprock are represented using a structured Cartesian grid. Grid refinement is applied in the 
vicinity of the injection well to represent the pressure and CO₂ -saturation gradients generated during injection, 
while larger cells away from the well represent the regional reservoir response.

610 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
A formal mesh-convergence study was not performed in the present work. Therefore, the selected grid resolution 
is considered a base-case representation rather than a demonstrated grid-independent solution. A systematic grid-
refinement analysis is recommended for future site-specific applications of the proposed workflow. 
Table 1.  
Grid properties 
Parameter Value Unit 
Grid Dimensions 11 × 11 × 10 Cels 
Reservoir Top Depth 1200 m 
Model Area 2,421,879 ft2 
Reservoir Thickness 50 m 
 
2.4 Flow, relative permeability and boundary conditions 
The multiphase flow simulation was performed using the CMG -GEM compositional formulation. The 
reservoir was represented by a homogeneous Cartesian grid consisting of 11 × 11 × 10 grid cells, with cell 
dimensions of 100 m × 100 m × 50 m. The initial reservoir porosity was 0.18, with horizontal and vertical 
permeabilities of 200 mD and 20 mD, respectively. The initial reservoir pressure and temperature were 11.8 MPa 
and 80 °C, respectively. 
CO₂ injection was specified at a rate of 3,000 m³/day with a maximum bottom-hole pressure constraint of 14 
MPa. The injection interval was located in the lower reservoir layers. The lateral and basal boundaries were treated 
as no-flow boundaries. The simulation consisted of 10 years of CO₂ injection followed by 500 years of post -
injection monitoring. 
The liquid-gas relative-permeability relationship was defined a s a function of gas saturation. The base -case 
model used the Liquid -Gas Table (Gas Saturation) implemented for Rock Type 1. The specified gas relative  
permeability (𝑘𝑟𝑔) increased from 0 at 𝑆𝑔 = 0.0006 to 0.9999 at 𝑆𝑔 = 0.80, while the corresponding relative 
permeability of the other liquid phase decreased from 1.00 to 0 over the specified saturation range. The complete 
relative-permeability data are provided in Table 2. No explicit capillary-pressure drainage curve was activated for 
Rock Type 1 in the base-case model. Gas-phase hysteresis was specified using the default Land hysteresis 
formulation, with a maximum residual gas saturation of 0.30. Oil and water hysteresis options were not activated. 
To support reproducibility, the multiphase-flow parameters adopted in the base-case model are further clarified 
as follows. The tabulated liquid-gas relative-permeability relationship (Table 2) is a Corey-type curve in which 
the liquid relative permeability decreases from 1.0 to 0 as gas saturation increases from 0.0006 to 0.80, with an 
irreducible water saturation of 0.20 and a maximum residual gas saturation of 0.30 applied through  the Land 
hysteresis formulation. An explicit capillary-pressure drainage curve was not activated for Rock Type 1 because, 
at the grid-block scale adopted in this study (100 m × 100 m × 50 m), CO₂ -brine displacement in reservoir-scale 
saline-aquifer storage models is generally dominated by viscous and  gravitational forces rather than pore -scale 
capillary forces, consistent with the compositional -simulation framework of CMG -GEM (Nghiem et al., 2004,  
2011). This simplification is common in reser voir-scale CCS simulation studies but may underestimate local 
capillary trapping and residual -saturation effects near the plume margin; incorporating an explicit capillary -
pressure curve is therefore recommended for future refinement of the workflow. The lateral and basal boundaries 
of the model domain were treated as no -flow (closed) boundaries, representing a laterally bounded or 
compartmentalized saline -aquifer unit; this closed -boundary formulation is consistent with the mass -balance 
verification described in Section K, in which the cumulative  injected CO₂ mass is retained within the model 
domain to within 1%. Under an open or laterally extensive aquifer boundary condition, pressure would dissipate 
more efficiently, so the simulated pore-pressure buildup, effective-stress reduction, and fracture-pressure margin 
reported in this study should be interpreted as a conservative (upper-bound) estimate of the true pressure response.

611 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
The CO₂ injection well was operated under a maximum bottom -hole-pressure (BHP) constraint of 14 MPa.  
The simulated maximum reservoir pore pressure reached 15.8 MPa. The two values represent different pressure 
metrics: the former is the imposed well -control constraint, whereas the latter represents the maximum por e 
pressure obtained within the simulated reservoir domain. Therefore, the 15.8 MPa value should not be interpreted 
as the prescribed BHP limit. 
The geochemical reactions were simulated using mineral kinetic parameters based on the Transition State 
Theory (TST)/Arrhenius formulation. Mineral dissolution and precipitation were incorporated into the reactive -
transport calculation to evaluate their effects on the long-term evolution of the reservoir and caprock system. 
2.5 Fluid properties and thermodynamic modeling 
The fluid system consists primarily of supercritical CO₂ and formation water. Fluid behavior is modeled using 
the compositional formulation of CMG -GEM, which accounts for pressure -, temperature -, and composition -
dependent phase behavior and fluid properties. 
 
Table 2.  
Simulation parameters and boundary conditions. 
Parameter Value Unit 
Reservoir Type Homogeneous Sandstone - 
Grid 11×11×10 Cels 
Cells Dimensions 100 × 100 × 50 m 
Reservoir Depth 1200 m 
Initial Temperature 80 ℃ 
Initial Pressure 11.8 MPa 
Initial Porosity 0.18 - 
Horizontal Permeability 200 mD 
Vertical Permeability 20 mD 
CO2 Injection Rate 3 m3/day 
Maximum bottom-hole pressure 14 MPa 
Rock Compressibility 5.8 ×10-7 1/psi 
Brine Density 68.42 lb/ft3 
Brine Viscosity 0.7 cP 
Salinity 50 ppm 
Lateral Boundary No-flow - 
Basal Boundary No-flow - 
Relative-Permeability Table Liquid-Gas  Table (Gas Saturation) - 
Maximum residual gas saturation 0.30 - 
Gas hysteresis model Land - 
Capillary-pressure drainage curve Not activated - 
Oil hysteresis Not activated - 
Water hysteresis Not activated - 
CO2 Injection Period 10 Years 
Post-Injection Monitoring 500 Years 
 
 
CO₂ dissolution into formation water is included to represent dissolution trapping. The dissolution process 
modifies the aqueous-phase composition and density and contributes to the coupled geochemical evolution of the 
reservoir. Mutual CO₂ –water solubility is incorporated into the simulation to represent c ompositional changes 
associated with CO₂ injection.  The fluid composition and thermodynamic properties are based on the 
representative data reported in the selected literature sources.

612 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Table 3.  
Liquid-Gas Relative permeability data used in the base-case model. 
𝑺𝒈 𝒌𝒓𝒈 𝒌𝒓𝒐𝒈 
0,0006 0,0000 1,0000 
0,0500 0,0000 0,8800 
0,0889 0,0010 0,7023 
0,1778 0,0100 0,4705 
0,2667 0,0300 0,2963 
0,3556 0,0500 0,1715 
0,4444 0,1000 0,0878 
0,5333 0,2000 0,0370 
0,6222 0,3500 0,0110 
0,6500 0,3900 0,0000 
0,7111 0,5600 0,0000 
0,8000 0,9999 0,0000 
 
 
 
Table 4.  
Fluid components. 
Component Molecular Weight (g/mol) Critical Pressure (bar) Critical Temperature (K) Acentric Factor 
CO2 44.01 72.8 304.2 0.225 
CH4 16.043 45.4 190.6 0.008 
H2O 18.015 217.6 647.3 0.344 
 
2.6 Geochemical reaction modeling 
Geochemical reactions between dissolved CO₂, formation water, and reservoir minerals are modeled using the 
geochemical module of CMG-GEM. Mineral reaction kinetics are represented using Transition State Theory 
(TST), which describes the rate of mineral dissolution and precipitation as a function of reaction affinity, reactive 
surface area, temperature, and mineral-specific kinetic parameters. 
The initial mineral assemblage consists of qua rtz (60%), calcite (10%), dolomite (5%), and clay minerals 
(25%). The modeled mineral reactions include carbonate dissolution and secondary mineral precipitation resulting 
from changes in aqueous composition during CO₂ injection.  The general mineral reaction rate is expressed by               
(A. Lasaga & Steefel 1998) as in Equation 1 
𝑟𝑖 = 𝑘𝑖𝐴𝑖 (1 −
𝑄𝑖
𝐾𝑒𝑞,𝑖
)                               (1) 
where 𝑟𝑖, i 𝑘𝑖, 𝐴𝑖, 𝑄𝑖, and 𝑘𝑒𝑞,𝑖  are the reaction rate of mineral, the reaction rate constant, the reactive surface area, 
the ion activity product, and the equilibrium constant of the reaction, respectively. The kinetic rate constant 𝑘𝑖 is 
modeled using the Arrhenius Equation, expressed as in Equation 2: 
       𝑘 = 𝑘0,𝑖 exp [−
𝐸𝑎
𝑅𝑇]                                                           (2) 
where 𝐸𝑎, R, and T, are the activation energy, the universal gas constant, and the absolute temperature, 
respectively. The modeled mineral reactions and corresponding kinetic parameters are summarized in Table 5.

613 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Table 5.  
Mineral reaction parameters. 
Mineral Reaction Reactive Surface Area (m2/m3) Activation Energy (J/mol) Log 10 (1/Sec) 
Quartz 718 87,500 -13.9 
K-Feldspar 176 67,830 -12.0 
Kaolinite 17,600 62,760 -13.0 
Calcite 88 41,870 -8.81 
Dolomite 88 41,870 -9.22 
Illite 26,400 58,620 -9.0 
 
The aqueous reactions considered in the model include water dissociation and CO₂–carbonate equilibria: 
H+ + OH- ⇌H2O 
CO2 + H2O ⇌ H+ +HC𝑂3− 
𝐶𝑂32−+ H+ ⇌ HC𝑂3−                             (3) 
The initial aqueous ionic concentrations are based on the representative formation-water composition 
adopted from (Nghiem et al., 2004, 2011; Ranganathan et al., 2011). 
2.7 Porosity and permeability evolution 
Mineral dissolution and precipitation modify the solid volume within the pore system. The resulting change 
in mineral volume is used to calculate the evolution of reservoir porosity through volumetric mass balance.The 
evolution of permeability is calculate d using a Kozeny –Carman Equation type relationship proposed by                  
(A. C. Lasaga 1984): 
𝑘 = 𝑘0 (
∅
∅0
)
𝑛                                                     (4) 
where 𝑘0 and ∅0represent the initial permeability and initial porosity, respectively, and nnn  is an empirical 
exponent that controls the sensitivity of permeability to porosity changes. Thus, the geochemical module provides 
the basis for evaluating changes in porosity and permeability associated with mineral alteration. These evolving 
petrophysical properties are used in the subsequent flow and pressure calculations. 
2.8 Geomechanical modelling 
The geomechanical response of the reservoir–caprock system is evaluated using an isotropic linear poroelastic 
formulation. Changes in effective stress caused by CO₂-induced pore-pressure changes are calculated using Biot's 
effective-stress relationship by (Biot 1941) further applied in reservoir geomechanics studies (Leal et al., 2015)  
and (Hashemi et al., 2022): 
𝜎′ = 𝜎 − 𝛼𝑝                               (5) 
where σ′, σ, α, and P, are the effective stress, the total  stress, the Biot Coefficient, and the pore pressure, 
respectively. The mechanical behavior of the reservoir and caprock is characterized using young’s modulus 
(E), Poisson’s ratio ( ν), cohesion (c), and internal friction angle ( ϕ). The corresponding values  used for the 
reservoir and caprock should be reported explicitly in the model -parameter table to ensure reproducibility by 
(Adu-Gyamfy et al., 2022) . 
Mechanical failure is evaluated using the Mohr –Coulomb criterion. The fr acture-pressure condition is 
determined by comparing the simulated stress state with the failure criterion. The resulting fracture pressure is 
then compared with the maximum simulated pore pressure to quantify the available pressure margin. The pressure 
safety ratio is calculated as (Guerriero 2022):

614 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
𝑆𝑅 =
𝑃𝑓
𝑃𝑚𝑎𝑥
                                       (6) 
where 𝑃𝑓 and 𝑃𝑚𝑎𝑥, are the estimated fracture pressure and the maximum simulated pore pressure, respectively. A 
value of 𝑆𝑅 > 1 indicates that the simulated maximum pressure remains below the estimated fracture pressure, 
whereas 𝑆𝑅 =1 represents the limiting condition. 
2.9 Integrated geochemistry-geomechanics workflow 
The workflow illustrates the propagation of information between ge ochemical reactions, petrophysical 
evolution, fluid-flow redistribution, and geomechanical response. The feedback loop represents the iterative 
interaction among these processes during CO₂ injection and post-injection monitoring. 
2.10 Simulation scenarios and global sensitivity analysis 
Sensitivity analysis is conducted to quantify the influence of key operational and geological parameters on the 
simulated CO₂-storage response (Ronlei et al., 2025; Wangen et al., 2016). The investigated parameters include 
pressure, temperature, pH, porosity, permeability, and CO₂ injection rate.  The base-case conditions are used as 
the reference scenario, while each sensitivity parameter is varied within a predefined range representing plausible 
saline-aquifer conditions. 
 
 
 
Figure 1.  
Integrated geochemistry–geomechanics workflow for CO₂ storage simulation, illustrating the interaction among geochemical 
reactions, petrophysical evolution, fluid-flow redistribution, and geomechanical response during  
CO₂ injection and post-injection monitoring.

615 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Table 6.  
Sensitivity-analysis parameters. 
Parameter Minimum Base Case Maximum Unit 
Pressure 5,000 11,800 15,000 kPa 
Temperature 30 80 150 °C 
pH 2 7 9 - 
Porosity 0,10 0,18 0,30 - 
Permeability 50 200 400 mD 
CO₂ injection rate 1,000 3,000 5,000 m³/day 
 
The base-case values in Table 6 correspond to the reservoir conditions defined in Table 2. In particular, the  
base-case porosity and temperature are maintained at 0.18 and 80 °C, respectively, to ensure consistency between 
the reservoir model and sensitivity analysis. 
The minimum and maximum bounds assigned to each parameter in Table 9 were selected to represent plausible 
geological and operational ranges reported for saline-aquifer CO₂ storage rather than arbitrary numerical intervals. 
The pressure range (5.0 –15.0 MPa) brackets the initial hydrostatic pressure and the maximum  bottom-hole-
pressure constraint applied at the injection well, consistent with the injection-pressure envelopes reported for saline-
aquifer storage operations by (Bentham et al., 2017; Ranganathan et al., 2011). The temperature range (30–150 °C) 
spans the geothermal gradients typical of sedimentary basins at depths of a few hundred to several kilometers, in line 
with the temperature-dependent reaction-kinetics behavior discussed by (Fang et al., 2022). The pH range  (2–9) 
covers the shift from strongly acidic conditions generated by carbonic -acid formation immed iately after CO₂ 
injection to near -neutral formation -water conditions, following  the pH  evolution reported for  CO₂-brine-rock 
systems by (De Silva et al., 2015). The porosity (0.10 –0.30) and permeability (50 –400 mD) ranges reflect the 
variability typically reported for siliciclastic saline-aquifer reservoirs suitable for CO₂ storage (Ranganathan et al., 
2011; Ronlei et al., 2025)  and the injection -rate r ange (1,000 –5,000 m³/day) reflects representative small -to-
moderate industrial injection rates for a single vertical well. The base -case value of each parameter corresponds 
directly to the reservoir and operating conditions defined in Table 2, so that the sensitivity analysis is anchored 
to, and directly comparable with, the base-case simulation results reported in this study. 
Global sensitivity analysis is performed using the Sobol variance -decomposition approach. The method 
quantifies the relative contribution of each uncertain input parameter to the variance of the selected model 
response. The analysis is used to rank the influence of pressure, temperature, pH, porosity, permeability, and 
injection rate on the simulated storage response (Hu et al., 2024). 
In this study, the response variable used for the global sensitivity analysis is the cumulative amount of 
secondary mineral precipitation (total moles of K-feldspar, quartz, and kaolinite precipitated) simulated at the end 
of the 500-years monitoring period, since this quantity integrates the combined influence of pressure, temperature, 
pH, and petrophysical evolution on the geochemical trapping response of the system. This response  variable was 
selected because secondary mineral precipitation directly reflects the cumulative effect of the coupled geochemical 
reactions evaluated in this study and is more sensitive to parameter variation over the simulated timeframe than 
the maximum pore pressure or effective-stress reduction, which are primarily controlled by the imposed injection-
pressure constraint. First-order Sobol indices quantify the individual contribution of each parameter, while total -
order indices additionally account for parameter interactions (Vilarrasa et al., 2016) . The resulting sensitivity 
ranking is then used to identify the parameter requiring the greatest attention in pressure management and long -
term storage-integrity assessment. 
2.11 Model limitations and reproducibility 
Several limitations should be considered when interpreting the simulation results. First, the reservoir model is 
homogeneous and does not explicitly represent geological heterogeneity, faults, fractures, or spatial variations in 
mineral composition. Second, a formal grid-convergence analysis was not conducted. Third, the model is based on

616 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
representative literature-derived reservoir and geochemical parameters rather than calibration against a specific 
field-scale CCS project. Accordingly, the results are interpreted as a mechanistic and quantitative base -case 
assessment. Future work should evaluate grid independence, incorporate heterogeneous reservoir and caprock 
properties, and validate the coupled workflow against i ndependent laboratory or field observations from 
established CO₂ storage sites. 
2.12 Model verification, validation, and benchmarking 
Model verification and model validation address distinct questions and are therefore explicitly distinguished 
in this study. Verification tests whether the numerical model correctly solves the governing mass -balance, 
geochemical-kinetic, and geomechanical equations, independent of whether those equations fully represent the 
real storage system; it is assessed here through  internal mass-balance closure, benchmarking of the reaction -
kinetics module against independently published dissolution -rate trends, and an analytical cross -check of the 
effective-stress and Mohr–Coulomb calculations. Validation, in contrast, tests whether the simulated behavior is 
consistent with independent physical observations, such as field -monitored pressure, geochemical, or 
geomechanical data from an operating CO₂ storage site. The exercises described  immediately below constitute 
model verification; they confirm the internal numerical and physical consistency of the coupled workflow but do 
not by themselves constitute validation against field observations.  A first step toward validation, in the form of a 
quantitative comparison against principal results reported for published CO₂-storage case studies, is provided at the 
end of this section, while a formal history-matching exercise against a specific field dataset (e.g., Sleipner or Ketzin) 
remains a priority for future work, as also noted in the Model Limitations section. 
Prior to sensitivity and scenario analysis, the coupled geochemistry–geomechanics workflow was checked for 
internal consistency and physical plausibility using mass -balance verification, literature -based reaction-kinetics 
benchmarking, and an  independent analytical check of the geomechanical formulation. First, mass -balance 
consistency was verified by confirming that the cumulative CO₂ trapped through structural, solubility, and mineral 
trapping pathways at the end of the 500-years monitoring period matched the total injected mass within a tolerance 
of less than 1%, consistent with the closed -boundary formulation adopted in this study. Second, the reaction -
kinetics module was benchmarked qualitatively against the calcite- and dolomite-dissolution rate trends reported 
for comparable sandstone–brine–CO₂ systems by (Xu et al., 2007) and (Zuo et al., 2024), for which the simulated 
pH decline and carbonate-dissolution onset in the present model were compared with the ranges reported in those 
studies. Third, the effective -stress and fracture -pressure calculations were cross -checked using an independent 
analytical evaluation of Equation 5 at the maximum  simulated pore pressure. Biot coefficients of 0.75 for the 
sandstone reservoir and 0.90 for the shale caprock  were applied consistently in the analytical and CMG-GEM 
calculations, and the resulting effective-stress values were found to agree within numerical rounding. The 
maximum simulated pressure of 15.8 MPa was also compared with the adopted fracture-pressure threshold of 19 
MPa, resulting in a safety margin of  3.2 MPa and a safety ratio of 1.20. A formal quantitative benchmarking 
exercise against a published field-scale history-matched dataset (e.g., Sleipner or Ketzin) was beyond the scope of 
the present synthetic-model study and is recommended as a priority for future work, as also noted in the Model 
Limitations section. 
2.13 Comparison with published CCS studies 
To provide context for the present results and to support the novelty claims made in the Introduction, the 
principal findings of this study are compared with several recently published CO₂ -storage case studies. At the  
Sleipner field (Utsira Sand, Norwegian North Sea), CO₂ has been injected into a laterally extensive, high-
permeability saline aquifer at approximately 1,000 m depth since 1996 at a rate of approximately 1 Mt/years, with 
monitoring indicating no significant pressure build-up or caprock integrity concern owing to the very large lateral 
extent and connectivity of the aquifer — in contrast, the present homogeneous, closed-boundary model represents 
a smaller, laterally bounded storage unit and therefore yields a comparatively larger simulated  pore-pressure 
increase (11.8 to 15.8 MPa)  and effective-stress reduction, which  is consistent with the conservative, closed -
system framing discussed above. At the Farnsworth oil-field CO₂-storage assessment, (Adu-Gyamfy et al., 2022)

617 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
reported that chemo-mechanical alteration of the caprock over a 1000-years post -injection period produced a 
negligible porosity change (about 0.0003%) but a stress -induced porosity increase of up to 1.4% and a 
corresponding permeability change of about 4%, with the caprock remaining far from Mohr –Coulomb failure; 
this is broadly consistent with the present results, in which the sim ulated maximum pore pressure (15.8 MPa) 
remains below the adopted fracture-pressure threshold (19.0 MPa), yielding a comparable margin of mechanical 
stability. (Kanin et al., 2025) proposed a geomechanical risk-assessment framework for saline-aquifer CO₂ storage 
but, as noted in the Introduction, did not explicitly couple geomechanical analysis with reactive mineral transport; 
the present study extends this line of work by directly propagating mineral-reaction-driven porosity changes into 
the effective -stress and fracture -pressure-margin calculation. Simil arly, (Eyitayo et al., 2025)  investigated 
supercritical CO₂-brine-rock geochemical interactions and their implications for mechanical integrity but did not 
rank the controlling parameters using global sensitivity analysis; the Sobol-based ranking obtained in the present 
study (pressure ≈ 59% of the total sensitivity, followed by pH and temperature) provides a quantitative complement 
to those qualitative assessments. Taken together, these comparisons indicate that the magnitude and direction of 
the geomechanical response obtained in the present study are consistent with the range of behavior reported in the 
literature for saline-aquifer and depleted-reservoir CO₂ storage systems, while the explicit two-way geochemistry–
geomechanics coupling and global sensitivity ranking represent the principal points of novelty relative to these 
previous studies. 
 
3. Result and discussion 
Mineral trapping is considered one of the most stable CO₂ storage mechanisms in geological systems because 
CO₂ that reacts with  reservoir minerals forms stable carbonate  minerals over geological  timescales. This  
mechanism is regarded as highly secure with a very low leakage risk compared to other trapping mechanisms, 
since mineralized CO₂ is no longer present in the fluid phase (Fatah et al., 2022; Luo et al., 2022). 
Reactive transport simulation results indicate that CO₂ mineralization occurs progress ively during both 
injection and post-injection periods. Interactions among dissolved CO₂, formation water, and rock minerals trigger 
carbonate dissolution and the precipitation of secondary minerals, which influence the evolution of reservoir 
porosity and permeability. These petrophysical changes subsequently affect pore pressure distribution and the 
effective stress response of the rock formation.  Sensitivity analysis shows that reservoir pressure is the dominant 
parameter controlling both geochemical reaction dynamics and the mechanical stability of the storage system. 
Increased pore pressure due to CO₂ injection directly affects the evolution of effective stress, which under certain 
conditions may approach the failure threshold of the caprock as defined b y the Mohr–Coulomb failure criterion. 
Therefore, controlling injection pressure is critical for maintaining the integrity of the storage system. 
The simulations were conducted using CMG-GEM with a homogeneous reservoir model as an initial approach 
to evaluate CO₂ trapping mechanisms and the long-term mechanical stability of the formation. The results provide 
a foundation for developing a leakage risk evaluation framework and determining safe operational pressure limits 
for CO₂ storage in saline aquifers (Xu et al., 2007). 
3.1 Model verification and grid-independence analysis 
(Ismail et al., 2025) systematically benchmarked lateral and vertical grid resolution for CO₂ storage in a saline 
aquifer of broadly similar areal extent, comparing coarser grids against a 2 m vertical, 150 m lateral fine -scale 
reference. Their results indicate that lateral cell sizes at or below 150–200 m reproduce plume extent and pressure 
evolution to within a few percent of the fine-scale reference during both injection and monitoring, whereas vertical 
resolution exerts a much stronger control during the post -injection monitoring phase, when CO₂ migration is 
dominated by buoyancy-driven gravity segregation beneath the caprock; coarsening the vertical grid from 2 m to 
5, 10, 25, and 50 m produced mean CO₂-saturation deviations of approximately 15%, 25–35%, 61–72%, and 79–
86%, respectively, relative to the fine-scale reference during the monitoring period. The lateral cell dimension  
adopted in the present base -case model (100 m × 100 m) falls  within the range identified as adequate for plume-
extent and pressure prediction. In contrast, the vertical cell dimension used here (50 m) coincides with the coarsest

618 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
resolution tested by (Ismail et al., 2025) , for which post -injection deviations of roughly 80% in mean CO₂ 
saturation were reported relative to a 2 m reference grid. 
The grid-independence analysis shows that the coarse, base-case, and fine configurations produce comparable 
results. The pressure difference between the coarse and base cases is 0.51%, while the difference between the fine 
and base cases is 0.25%.  For CO₂ saturation, the corresponding differences are 3.06% and 0.71%, respectively. 
Effective-stress differences are 0.88% and 0.27%, whereas mineral -alteration differences are 2.96% and 0.71%. 
These relatively small differences indicate that the base -case grid provides a consistent representation of the 
simulated reservoir response. 
 
 
 
Figure 2.  
Conceptual model of the synthetic saline-aquifer reservoir and overlying caprock used for the CO₂ storage simulation. 
 
 
Table 7.  
Grid-independence analysis of the CO₂ injection model. 
Grid NX × NY × NZ ΔZ 
Coarse 11 × 11 × 5 100 m 
Base 11 × 11 × 10 50 m 
Fine 11 × 11 × 20 25 m 
 
 
Table 8.  
Percentage differences of key simulation parameters relative to the base-case grid. 
Case Grid Size Pmax (MPa) CO2 Saturation 
Effective Stress 
(MPa) Mineral Alteration 
Coarse 100 m 15.72 0.412 14.95 8.20 
Base 50 m 15.80 0.425 14.82 8.45 
Fine 25 m 15.84 0.428 14.78 8.51

619 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Table 9.  
Percentage differences in key simulation parameters relative to the base-case grid. 
Case Pressure CO2 Saturation 
Effective Stress 
(MPa) Mineral Alteration 
Coarse vs Base 0.51% 3.06% 0.88% 2.96% 
Fine vs Base 0.25% 0.71% 0.27% 0.71% 
 
 
Figure 3.  
Convergence of maximum reservoir pressure with vertical grid size for the coarse, base-case, and fine grid configurations. 
 
 
 
This comparison indicates that while the lateral discretization of the present model is unlikely to materially affect 
the reported pressure, effective-stress, and areally averaged geochemical results, the coarse vertical resolution is 
likely to underestimate the sharpness and buoyancy-driven upward migration of the CO₂ saturation front beneath 
the caprock during the 500-years monitoring period, consistent with the stratification and gravity -number 
sensitivity reported for vertically discretized CO₂–brine systems by (Oh et al., 2015). 
𝑀 𝐴 (%) = ∆𝑛𝑀𝑖𝑛𝑒𝑟𝑎𝑙
𝑛𝑖𝑛𝑖𝑡𝑖𝑎𝑙 𝑀𝑖𝑛𝑒𝑟𝑎𝑙
× 100              (7) 
Coars vs Base 
=
8.20−8.45
8.45 × 100 = 2.96%                       (8) 
 
Fine vs Base 
=
8.51−8.45
8.45 × 100 = 0.71%                       (9) 
Coarse
Base
Fine
15,7
15,72
15,74
15,76
15,78
15,8
15,82
15,84
15,86
25 50 75 100
Maximum Reservoir Pressure, Pmax (MPa)
Vertical Grid Size, ΔZ (m)
Maximum Reservoir Pressure Convergence

620 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
                               
Figure 4.  
Comparison of CO₂ saturation for the coarse, base-case, and fine vertical grid configurations  
in the grid-independence analysis. 
 
                                          
Figure 5.  
Comparison of effective stress for the coarse, base-case, and fine vertical grid configurations in  
the grid-independence analysis. 
Coarse
Base
Fine
0,41
0,412
0,414
0,416
0,418
0,42
0,422
0,424
0,426
0,428
0,43
25 50 75 100
CO2 Saturation
Vertical Grid Size, ΔZ (m)
CO2 Saturation
Coarse
Base
Fine
14,76
14,78
14,8
14,82
14,84
14,86
14,88
14,9
14,92
14,94
14,96
25 50 75 100
Effective Stress (MPa)
Vertical Grid Size, ΔZ (m)
Effective Stress (MPa)

621 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
                                
Figure 6.  
Comparison of mineral alteration for the coarse, base-case, and fine vertical grid configurations in  
the grid-independence analysis. 
 
 
 
This comparison indicates that while the lateral discretization of the present model is unlikely to materially affect 
the reported pressure, effective-stress, and areally averaged geochemical results, the coarse vertical resolution is 
likely to underestimate the sharpness and buoyancy-driven upward migration of the CO₂ saturation front beneath 
the caprock during the 500-years monitoring period, consistent with the stratification and gravity -number 
sensitivity reported for vertically discretized CO₂ –brine systems by (Oh et al., 2015) . Consequently, the near -
caprock CO₂ saturation, and any geochemical or geomechanical response that depend s on the local CO₂-brine 
contact position, should be regarded as a base-case approximation rather than a grid-independent result; a refined 
vertical grid (on the order of 2–5 m near the reservoir-caprock interface) is recommended as a priority verification 
step in future work. 
3.2 Base case simulation initialization and CO₂ trapping evolution 
Injection of CO₂ into a saline aquifer significantly alters the geochemical conditions of the reservoir due to the 
dissolution of CO₂ in formation brine and th e subsequent formation of carbonic acid. This process occurs when 
CO₂ reacts with water to form H₂CO₃, increasing the hydrogen ion concentration in the fluid. The  formation of 
carbonic acid acts as the primary driver of chemical changes in the reservoir from the early stages of injection, as 
reported by (Zuo et al., 2024) and (Eyitayo et al., 2025). 
The formation of acidic fluids leads to a progressive decrease in reservoir pH, creating a highly reactive 
chemical environment. The reduction in pH accelerates chemical interactions between the fluid and rock-forming 
minerals, particularly under the high pressure and temperature conditions typical of deep reservoirs. Previous 
studies indicate that pH variation is a dominant factor controlling geochemical reaction rates and mineral stability 
in CO₂ storage systems (Shi et al., 2024). Acidic conditions induced by CO₂ injection promote the dissolution of 
carbonate and silicate minerals with varying reactivity. Carbonate minerals, especially calcite and dolomite, are 
generally more reactive to acidic fluids and therefore dissolve faster than silicate minerals. This dissolution 
process increases the concentration  of Ca²⁺ and Mg²⁺ ions in the formation fluid and alters the overall chemical 
Coarse
Base
Fine
8,15
8,2
8,25
8,3
8,35
8,4
8,45
8,5
8,55
25 50 75 100
MIneral Alteration
Vertical Grid Size, ΔZ (m)
Mineral Alteration

622 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
equilibrium of the system (Bokka et al., 2022; Fentaw et al., 2024; A. Zhang et al., 2024) . Changes in fluid and 
mineral composition  resulting from CO₂ –brine–rock interactions directly influence the  evolution of porosity, 
permeability, and the mechanical stability of the reservoir. Long-term geochemical alteration may either strengthen 
or weaken formation integrity depending on  whether mineral dissolution or secondary mineral precipitation 
dominates. Understanding the mechanisms of carbonic acid formation, pH reduction, and fluid –rock reactions is 
therefore critical for evaluating the safety and sustainability of CO₂ storage in saline aquifers (Hu et al., 2024). 
The base-case reservoir parameters and initial conditions used in the simulation include reservoir pressure, 
temperature, porosity, permeability, mineral composition, and formation fluid chemistry. These parameters serve 
as reference conditions for sensitivity analysis evaluating geochemical reaction dynamics and porosity evolution 
during CO₂ storage.  The base-case initialization and simulation in this stud y are conducted using CMG -GEM. 
CO₂ injection is simulated for 10 years (2024–2034), followed by a 500-years monitoring period (2034–2534) to 
evaluate long-term CO₂ storage stability in the saline aquifer and the evolution of mineralization processes over 
geological timescales. The results of the base-case initialization are presented in the Reservoir Simulation Model 
Initialization Table 10. 
 
Table 10.  
Reservoir simulation model initialization. 
No Parameter Unit Value 
1 Total Bulk Reservoir V olume M3 6.05000E+08 
2 Total Pore V olume M3 1.09066E+08 
 
 
 
Figure 7.  
Evolution of cumulative trapped CO₂ as a function of simulation time during CO₂ injection and post injection monitoring. 
 
Figure 7 illustrates the evolution of cumulative trapped CO₂ throughout the simulation period. During the CO₂ 
injection period from 2024 to 2034, the amount of trapped CO₂ increases progressively as the injected CO₂ 
accumulates within the saline aquifer and interacts with the formation water and reservoir minerals. The increase 
in trapped CO₂ reflects the contribution of geological trapping mechanisms, particularly structural and solubility 
trapping, which progressively retain CO₂ w ithin the storage formation. After the injection period ends in 2034, 
the trapped CO₂ continues to evolve during the post -injection monitoring period until 2534, although the rate of 
change becomes more gradual. This behavior indicates that CO₂ retention c ontinues after injection through fluid 
redistribution and ongoing geochemical interactions between dissolved CO₂, formation water, and reactive 
minerals. Therefore, the evolution of cumulative trapped CO₂ provides an indication of the progressive 
stabilization of CO₂ within the reservoir during long-term storage.

623 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
 
Figure 8.  
Evolution of cumulative trapped CO₂ during the CO₂ injection period, showing the increase in  
CO₂ retained within the saline-aquifer storage system. 
 
 
 
 
Figure 9.  
Spatial distribution of CO₂ saturation in the reservoir: (a) initial condition and (b) distribution at the end of the  
500-year post-injection monitoring period. 
a). 
b).

624 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
 
 
Figure 10.  
Simulated reservoir pressure response during CO₂ injection and post-injection monitoring. 
 
Based on the base-case simulation results, a CO₂ Trapped vs Time curve was obtained to evaluate the evolution 
of trapped CO₂ during the injection period and the long -term monitoring phase. This curve represents the 
cumulative amount of CO₂ retained through various trapping mechanisms within the geological storage system. 
During the first 10 years of injection (2024–2034), the amount of trapped CO₂ shows a significant increasing 
trend (Figure 7). This increase is associated with the accumulation of injected CO₂ within the saline  aquifer and 
the initial interactions among CO₂, formation fluids, and reservoir minerals. At this stage, Structural Trapping and 
Solubility Trapping begin to play important roles in restricting CO₂ migration within the reservoir. 
Figure 9 shows the spatial distribution of CO₂ saturation within the reservoir before and after the CO₂ storage 
period. Figure 9(a) represents the initial reservoir condition, while Figure 9(b) shows the CO₂ distribution at the 
end of the post -injection monitoring period. The initial condition indicates that the reservoir is predominantly 
occupied by formation brine, whereas the final distribution demonstrates the development and spatial migration 
of the CO₂ plume within the reservoir. The spatial distribution reflects the movement of injected CO₂ through the 
pore space and its redistribution during the post -injection period. The resulting CO₂ plume provides a spatial 
representation of the storage behavior and allows the extent of CO₂ migration within the reservoir to be evaluated. 
The distribution also provides an important basis for assessing the relationship between CO₂ migration, reservoir 
pressure, and the subsequent geochemical and geomechanical responses of the storage system. 
After the injection phase ends, the amount of trapped CO₂ remains relatively stable until the end of the 
monitoring period (Figure 8). This behavior indicates that the reservoir system has reached a relatively stable 
condition in which CO₂ is retained through a combination of trapping mechanisms. Therefore, the CO₂ Trapped 
vs Time curve obtained from the base-case simulation serves as a baseline reference for analyzing the contribution 
of different trapping mechanisms, particularly Mineral trapping, in long-term CO₂ storage. 
Figure 10 presents the evolution of reservoir pressure during CO₂ injection and post-injection monitoring. The 
initial reservoir pressure is 11.8 MPa, and the pressure increases progressively during the injection period from 
2024 to 2034 as CO₂ is introduced into the reservoir. The maximum s imulated reservoir pressure reaches 
approximately 15.8 MPa at the end of the injection period. This increase in pore pressure is associated with the 
accumulation of injected CO₂ within the reservoir pore space. After injection ceases in 2034, the pressure response 
is monitored through 2534 to evaluate the subsequent pressure evolution during the post -injection period. The 
pressure history obtained from the simulation is important for evaluating the geomechanical response of the 
reservoir because changes in pore pressure directly influence effective stress and the available pressure margin 
relative to the adopted caprock fracture-pressure threshold.

625 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
3.3 Geochemical alteration and mineral dissolution 
The CMG-GEM simulation indicates that CO₂ injection rapidly dec reased the reservoir fluid pH, initiating  
carbonate dissolution near the injection well. Calcite and dolomite exhibited the highest dissolution rates during the 
early injection stage due to their high reactivity under acidic conditions. These findings are consistent with (He et 
al., 2017), confirming that carbonate minerals are preferentially dissolved follow ing carbonic acid formation. 
(Khoi et al., 2025). 
Geochemical simulation results show an increase in Ca²⁺ and Mg²⁺ ion concentrations during the early stages  
of injection, associated with the dissolution of carbonate minerals near the injection well. The decrease in  pH 
accelerates the dissolution of carbonate minerals such as calcite and dolomite, which are more reactive under acidic 
conditions than silicate minerals (He et al., 2017). The initial reactions are controlled by the formation of carbonic 
acid through the interaction between CO₂ and formation water (Nghiem et al., 2011): 
CO₂ + H₂O → H₂CO₃ H₂CO₃ → H⁺ + HCO₃⁻                 (10)  
The dissociation of carbonic acid produces H⁺ ions that increase the acidity of the reservoir fluid and promote 
the dissolution of primary minerals. This process releases various dissolved ions such as SiO₂, Ca²⁺, Mg²⁺, K⁺, and 
Al³⁺, which may subsequently participate in the formation of secondary minerals by (Mulhim & Delshad 2025). 
Changes in fluid chemical composition resulting from CO₂ –brine–mineral interactions can modify reservoir 
petrophysical properties, particularly porosity and permeability, which ultimately influence the long-term stability 
of CO₂ storage (Fentaw et al., 2024; Kempka et al., 2013). In this simulation, the intensity of dissolution reactions is 
influenced by reservoir temperature, fluid pH, activation energy, reaction rate constants, and reactive surface area 
(RSA), which collectively control the evolution of geochemical reactions in the CO₂ storage system (Shi et al., 2024). 
 
 
 
 
Figure 11.  
Evolution of calcite dissolution during CO₂ storage over the injection and post-injection monitoring periods. 
 
Figure 11 illustrates the evolution of effective stress associated with changes in reservoir pore pressure during 
CO₂ injection and post -injection monitoring. The increase in pore pressure caused by CO₂ injection results in 
a reduction in effective stress according  to Biot’s effective stress principle. During the injection period from 
2024 to 2034, the increase in reservoir pressure from 11.8 MPa to approximately 15.8 MPa produces a 
corresponding change in the effective stress state of the reservoir and caprock syst em. Following the cessation 
of injection, the effective -stress response is monitored during the post -injection period until 2534 as reservoir 
pressure evolves. The effective -stress response is important for evaluating the mechanical behavior of the 
storage formation because a reduction in effective stress may influence the proximity of the reservoir and 
caprock to their mechanical failure conditions.

626 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Calcite exhibited the highest dissolution rate throughout the 500 -years simulation, indicating persistent 
carbonate instability under continuous CO₂ exposure. Unlike previous studies reporting equilibrium after 
approximately 300 years, the present model predicts ongoing dissolution, suggesting that mineral equilibrium was 
not achieved within the investigated period. 
Reservoir environmental conditions, particularly the acidic pH and a temperature of 65 °C, play a significant 
role in accelerating mineral dissolution. This observation is consistent with previous findings indicating that low 
pH and elevated temperatures significantly enhance carbonate dissolution rates (De Silva et al., 2015). 
Although calcite possesses a relatively limited reactive surface area (88 m²/m³), its low activation energy (41.8 
kJ/mol) and comparatively high reaction rate constant enabled continuous dissolution throughout the simulation. 
These kinetic characteristics explain why calcite remained the  dominant dissolving mineral despite its smaller 
reactive surface compared with illite. A similar dissolution trend was reported by (Xu et al., 2007) although the 
onset of illite dissolution occurred earlier in the present study because of the higher reservoir pressure adopted 
during CO₂ injection. 
The combination of acidic geochemical conditions, elevated reservoir temperature, low activation energy, and 
relatively high reaction rates leads to sustained calcite dissolution. This process increases the concentration of Ca²⁺ 
ions in the formation fluid and may locally enhance reservoir porosity near the reaction zone, potentially influencing 
fluid flow distribution and pore pressure evolution within the CO₂ storage system simulated using CMG-GEM. The 
dissolution of calcite occurs as reservoir fluids become more acidic following CO₂ injection. Dissolved CO₂ forms 
carbonic acid (H₂CO₃), which dissociates to produce hydrogen ions that drive mineral dissolution: 
CaCO₃ + H⁺ → Ca²⁺ + HCO₃⁻               (11) 
in addition to carbonate minerals, clay minerals such as Illite may also dissolve under acidic conditions. The 
dissolution reaction of illite can be expressed as Equation 12: 
KMgAl 3Si₃ O₁₀(OH)₂ + 8H⁺ → K⁺  
+ Mg²⁺ + Al³⁺ + SiO₂ + H₂O                  (12)        
This reaction occurs when hydrogen ions attack oxygen bonds within the mineral structure, weakening Al–O 
and Si–O bonds and releasing cations such as K⁺, Mg²⁺, and Al³⁺, along with dissolved silica species. These 
released ions may subsequently participate in secondary mineral formation,  contributing to the long -term 
evolution of reservoir mineralogy and pore structure. 
Mineralogical changes resulting  from the dissolution  of carbonate and clay  minerals have the potential to 
influence the long-term evolution of reservoir porosity and the mechanical properties of the rock. The timing and 
progression of Illite dissolution during the simulation period are illustrated in Figure 12. 
In addition, the relatively high reactive surface area (RSA) of Illite, approximately 26,400, provides a large  
reactive surface that facilitates geochemical reactions. This condition is supported by a relatively high dissolution 
rate constant (lo g k =  −9) and a moderate activation energy of 58,620 J/mol. The combination of these kinetic 
parameters enables the dissolution of illite to occur significantly during the simulation period (Figure12). 
Figure 13  shows the dissolution of Dolomite, indicated by negative values ( –), which signify that the 
dissolution process occurs continuously. The decreasing trend follows a relatively linear pattern with a nearly 
constant slope from the beginning of CO₂  injection in 2024 until the end of the monitoring period in 2510.The 
absence of a stabilization point on the curve indicates that dolomite dissolution continues throughout the entire 
simulation period. The chemical dissolution reaction of Dolomite under a cidic fluid conditions can be expressed 
as Equation 13: 
CaMg(CO₃)₂ + 2H⁺ → Ca²⁺  
+ Mg²⁺ + 2HCO₃⁻                                       (13)

627 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
 
Figure 12.  
Evolution of illite dissolution during CO₂ storage over the injection and post-injection monitoring periods. 
 
 
 
Figure 13.  
Evolution of dolomite dissolution during CO₂ storage over the injection and post-injection monitoring periods. 
 
This reaction indicates that Dolomite, which contains two carbonate groups (CO₃²⁻), reacts with hydrogen ions 
H⁺ to produce two bicarbonate ions (HCO₃⁻), accompanied by the release of calcium Ca²⁺ and magnesium  Mg²⁺ 
ions into the solution. The H⁺ ions derived from the dissociation of carbonic acid (H₂CO₃) lead to a decrease in the 
solution pH, thereby increasing the tendency for dolomite dissolution, particularly under undersaturated 
conditions. This finding is consistent with the study by (Nghiem et al., 2011), which reported that acidic conditions 
can accelerate the dissolution of carbonate minerals in geological CO₂ storage systems. 
In this study, dolomite dissolution is also influenced by reaction kinetic parameters. The relatively low 
activation energy of 41,870 J/mol, combined with a reactive surface area (RSA) of 88 and a relatively fast 
reaction rate, allows the dissolution process to continue even though dolomite is mineralogically considered 
relatively stable. In addition, the natu ral precipitation of dolomite typically occurs over very long geological 
timescales. According to (Banerjee 2016) , the formation of dolomite requires a much longer time than the 
simulation period used in this study. Therefor e, the 500 -years simulation period is insufficient to facilitate 
significant dolomite precipitation . 
Another factor limiting dolomite precipitation is the low concentration of Mg²⁺ in the system. Research by 
Mouallem J et al. 2023. shows that the rate of dolomite formation is strongly influenced by the availability of Mg²⁺ 
ions in the reservoir fluid. The limited availability of these ions prevents the precipitation process from developing 
significantly during the simulation period. Nevertheless, the dissolution of carbonate minerals such as Dolomite 
and Calcite still contributes to the geochemical evolution of the system through the release of dissolved ions that 
may participate in the formation of secondary minerals. Equilibrium reactions such as Equation 14:

628 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
H⁺ + CO₃²⁻ → HCO₃⁻ H⁺ + OH⁻ → H₂O        (14) 
These reactions control pH variations and the chemical equilibrium of the reservoir fluid. Over time, such 
changes may gradually create conditions favorable for long -term mineralization, including the formation of 
secondary minerals such as Kaolinite, K-feldspar, and Quartz, which contribute to improving the long-term security 
of CO₂ storage over timescales of hundreds to thousands of years (De Silva et al., 2015; Wilkinson et al., 2009). 
The precipitation of Kaolinite begins to show a significant increase around the years 2294, as indicated by the 
graph exhibiting an exponential growth pattern. This pattern suggests an acceleration in the precipitation rate until it 
reaches a maximum value in 2510. Based on the interpretation of the curve, kaolinite formation begins approximately 
270 years after the injection process has ceased. The delayed precipitation of kaolinite reflects the time required for 
dissolved aluminum and silica concentration s to reach supersaturation. This delay demonstrates that secondary 
mineral formation is primarily controlled by reaction kinetics rather than solely by thermodynamic equilibrium. From 
a geochemical perspective, the precipitation of kaolinite is closely associated with the dissolution of Illite, which 
increases the concentration of Al³⁺ ions and dissolved silica (SiO₂(aq)). The dissolution of illite supplies aluminum 
and silica as the primary precursors for kaolinite formation through clay mineral transforma tion. Conceptually, 
the reaction mechanism can be represented as follows Equation 15: 
Illite + H⁺ + H₂O → Al³⁺ + SiO₂(aq) + K⁺  
+mineral residu Al³⁺ + SiO₂(aq)  
+ H₂O → Kaolinite + H⁺                                 (15) 
This reaction indicates that the increased chemical activity of aluminum and silica in the pore fluid drives 
the system toward supersaturation with respect to Kaolinite, enabling mineral precipitation. Therefore, the 
formation of kaolinite represents a secondary mineralogical response to the instability of Illite under specific 
geochemical conditions . 
3.4 Secondary mineral precipitation and mineral trapping 
The simulation indicates that kaolinite precipitation starts approximately 270 years after the injection period. 
This delayed precipitation suggests that the reservoir requires a prolonged period to reach supersaturation 
with respect to kaolinite under the selected temperature (65°C).  According to Bert Metz, kaolini te precipitation 
generally occurs optimally at intermediate temperatures. The reservoir temperature in this study, approximately 65 
°C, falls within the thermodynamic stability range of Kaolinite, thus supporting its formation. 
However, the kaolinite precipitation process occurs over a long timescale, spanning hundreds of years. This is 
due to the high activation energy of 62,760 J/mol and the relatively slow reaction rate (log k = –13). From a kinetic 
perspective, high activation energy reduces the frequency of effective collisions between reactive species, thereby 
slowing new mineral formation. On the other hand, the relatively high reactive surface area (RSA) of kaolinite, 
17,600 m²/m³, increases the available reactive surface and enhances the likelihood of precipitation. The large RSA 
compensates for kinetic limitations imposed by high activation energy and slow reaction rates, as reflected in the 
sharp increase in mineral amount after a threshold time, indicating a transition from the kine tically controlled 
phase to an accelerated precipitation stage. 
Mineralogical changes due to dissolution and precipitation processes can modify reservoir porosity and stiffness, 
potentially affecting the mechanical stability of the reservoir–caprock system during long-term CO₂ storage. In the 
context of geological CO₂ storage, these mineralogical transformations not only influence geochemical 
characteristics but also alter petrophysical properties such as porosity and permeability, thereby impacting pore 
pressure distribution and effective stress within the reservoir –caprock system. The detailed timing of kaolinite 
deposition is shown in Figure 14.

629 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
 
Figure 14.  
Evolution of kaolinite precipitation during CO₂ storage over the injection and post-injection monitoring periods. 
 
 
 
Figure 15.  
Evolution of quartz precipitation during CO₂ storage over the injection and post-injection monitoring periods. 
 
In addition to Kaolinite, Quartz also forms as a secondary mineral within the geochemical system. Its presence 
indicates that fluid –rock interactions not only produce clay minerals but also promote the precipitation of 
thermodynamically more stable silica minerals. Both quartz and kaolinite are considered stable secondary 
minerals due to their relatively simple crystal structures and high chemical resistance, making them less prone to 
dissolution except under extreme conditions. Their stability is further supported by low dissolution rates and 
relatively high activation energies, whi ch are characteristic of secondary minerals (B. Zhang et al., 2022) . 
Geochemically, quartz precipitation occurs as a result of increased concentrations of dissolved silica (SiO₂(aq)) 
from the prior dissolution of silicate mine rals. When the solution reaches supersaturation with respect  to silica, 
the dissolved silica precipitates as quartz. Compared to kaolinite, quartz formation is slower due to its higher crystal 
stability, meaning that crystallization is primarily controlled by kinetic factors and the thermodynamic conditions 
of the system. The timing of quartz precipitation is shown in Figure 15. 
Figure 15  presents the evolution of secondary mineral precipitation during  CO₂ storage. Following the 
dissolution of reactive primary minerals, dissolved ions are redistributed through the aqueous phase and may reach 
conditions favorable for secondary mineral formation. The precipitation response therefore represents a 
subsequent stage of the geochemical reaction pathway initiated by CO₂ dissolution and mineral dissolution. The 
temporal variation in mineral precipitation indicates that different minerals react at different rates because their 
formation depends on the reaction env ironment, temperature, mineral properties, dissolution kinetics, reactive 
surface area, and aqueous ion concentrations. The precipitation of secondary minerals contributes to long -term 
mineral trapping and may subsequently influence the petrophysical properties of the reservoir.

630 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
The changes in mineral composition due to dissolution and precipitation processes directly impact the 
evolution of the reservoir rock’s petrophysical properties. Dissolution of carbonate and silicate minerals can 
increase porosity by creating new pore space, while the precipitation of secondary minerals such as Kaolinite and 
Quartz may reduce or clog pore pathways. The interaction between these processes generates complex dynamics 
in porosity and permeability over the coarse of CO₂ storage. 
Compared with kaolinite, quartz precipitated approximately 200 years earlier because silica supersaturation 
was achieved sooner than aluminum-controlled clay mineral formation. This observation is consistent with (Wang 
et al., 2016) . At this stage, porosity and permeability variations are analyzed to understand  how geochemical 
processes influence fluid flow characteristics within the reservoir during long-term CO₂ storage. 
Quartz precipitation begins around the years 2078, as indicated by the simulation curve, which rises 
exponentially until reaching its maximum value in 2510. According to the curve, quartz requires approximately 
57 years of CO₂ injection to start precipitat ing. In this simulation, quartz exhibits a high activation energy 
(87,500 J/mol) and a very slow dissolution rate (log k ≈ –13.9), reflecting its high mineral stability and 
resistance to dissolution.  
Although the reactive surface area (RSA) of quartz is re latively low, about 718  m²/m³, it precipitates earlier 
than Kaolinite. This is due to the higher initial concentration of ions forming quartz and the fact that its 
precipitation relies on a single primary component, dissolved silica. In contrast, kaolinite  formation requires  
multiple ions such as Al³⁺, Si, and H⁺, making its precipitation process more complex and relatively slower. 
These findings are consistent with (Wang et al., 2016) , which indicate that quartz precipitation is strongly  
controlled by dissolved silica concentration. Quartz precipitation is governed by the availability of dissolved silica 
released from silicate dissolution. Once silica reaches supersaturation, quartz precipitates and contributes to long-
term mineral trapping. The dissolution and precipitation of minerals during fluid–rock interactions can influence 
the evolution of reservoir petrophysical properties, particularly porosity and permeability. 
The precipitation of K -feldspar becomes significant around the years 2034, as indicated by the simulation 
curve, which shows a sharp increase at the early stage of the reaction. Afterward, the curve stabilizes from 
approximately 2078 until the end of the monitoring period in 2510, indica ting that no substantial additional 
mineral formation occurs after this period. These results suggest that K -feldspar precipitates earlier than quartz 
and kaolinite, which require longer times to reach supersaturation conditions. 
Figure 16  illustrates the evolution of K -feldspar precipitation during the CO₂ injection and post -injection 
monitoring periods. The change in mineral moles represents the progressive geochemical alteration of K-feldspar 
within the reservoir system. The p recipitation response develops as dissolved chemical species produced by 
mineral–fluid interactions become available under conditions favorable for secondary mineral formation. The 
different timing and magnitude of mineral precipitation demonstrate that mi neral reactions do not occur at a 
uniform rate throughout the simulation. These reactions continue during the post -injection period and contribute 
to the long-term geochemical evolution of the reservoir. 
In this simulation (Figure 16), K-feldspar exhibits an activation energy of 67,830  J/mol—relatively high but 
still lower than that of quartz —and a relatively faster dissolution rate (log  k = –12). This kinetic combination 
allows K-feldspar to reach supersaturation more quickly. Additionally, the high initial concentration of precursor 
ions, particularly K⁺ and SiO₂(aq), further accelerates its precipitation process. 
According to (Kempka et al., 2013), K-feldspar precipitation is generally rare because the mineral 
commonly dissolves and serves as a source of ions for silica minerals such as quartz. However, precipitation can 
occur if the concentrations of K⁺ and SiO₂ are sufficiently high to achieve supersaturation, despite relatively 
high activation energy and reaction rate. In this simulation, the total amount of K-feldspar formed is smaller than 
that of quartz and kaolinite, likely due to limitations in supporting ions, especially Al³⁺ and K⁺,  which cause the 
precipitation reaction to halt once one of the limiting ions is depleted (Zhu et al., 2020).

631 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
 
Figure 16.  
Evolution of K-feldspar precipitation during CO₂ storage over the injection and post-injection monitoring periods. 
 
 
     
Figure 17.  
Spatial distribution of mineral dissolution and precipitation in the reservoir:  
(a) initial condition and (b) distribution at the end of the 500-years post-injection monitoring period. 
 
 
The differences in precipitation timing among minerals i ndicate that the process is controlled by multiple 
factors, including reaction environment, temperature, mineral crystal structure, dissolution kinetics, 
activation energy, reactive surface area (RSA), and ion concentrations that determine supersaturation. 
Previous studies show that mineral trapping via precipitation can occur over a wide time span—from decades to 
thousands of years after CO₂ injection—depending on the geochemical conditions of the system (Xu et al., 2007). 
a). 
b).

632 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Figure 17 presents the spatial distribution of mineral dissolution and precipitation within the reservoir. Figure 
17(a) represents the initial mineral condi tion, whereas Figure 17(b) shows the mineral distribution at the end of 
the 500-year post-injection monitoring period. The comparison between the two conditions illustrates the spatial 
extent of geochemical alteration caused by CO₂–brine–rock interactions. Mineral dissolution and precipitation are 
spatially distributed according to the areas affected by the CO₂ -rich fluid, indicating that geochemical alteration 
is not uniform throughout the reservoir. The spatial mineral -alteration pattern provides additional information 
beyond the temporal mineral-reaction curves because it identifies the regions where dissolution and precipitation 
are concentrated during long-term CO₂ storage. 
Given the complexity of factors controlling mineral precipitation, this study further conducts a sensitivity analysis 
on key parameters affecting geochemical evolution, including temperature, pressure, pH, porosity, permeability, and 
CO₂ injection rate. Dominant parameters are identified using a CMOST-AI approach through iterative modeling to 
evaluate the relative influence of each variable on mineral precipitation and reservoir system evolution. 
 
 
3.5 Geomechanical response and caprock integrity 
As illustrated in Figure 18, CO₂ injection initially forms a CO₂ plume beneath the caprock while displacing 
formation brine (Figure 18a). Continuous injection increases pore pressure within the reservoir (Figure 18b), 
resulting in a  reduction in effective stress according to  Biot’s effective stress principle. If  reservoir pressure 
approaches or exceeds the caprock fracture pressure, fault reactivation, caprock fracturing, and surface uplift may 
occur (Figure 18c), potentially creating leakage pathways for stored CO₂. Therefore, evaluating effective stress, 
fracture pressure, safety margin, and safety ratio is essential to ensure long-term storage security. 
The increase in pore pressure due to CO₂ injection has a direct impact on the effective stress of the reservoir rock. 
Based on the simulation results, the pore pressure rises from 11.8 MPa to 15.8 MPa during the injection period. The 
change in effective stress is calculated using Biot’s effective stress principle (Biot 1941; Leal et al., 2015): 
𝜎′ = 𝜎 − 𝛼𝑃          (16) 
where σ ′, α, P, and σ are effective stress, total stress, Biot coefficient, and pore pressure, respectively. The initial 
reservoir conditions for the simulation are as Table 11. 
 
Figure 18.  
Conceptual illustration of geomechanical responses during geological CO₂ storage, showing CO₂ plume development, pore-
pressure increase, effective-stress reduction, and potential caprock failure pathways;adapted from (Rutqvist 2012).

633 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Table 11.  
Geomechanical parameters used in the model. 
Parameter Reservoir Sandstone Shale Caprock Unit 
Depth 1200 1200 m 
Initial pore pressure, P0 11.8 11.8 MPa 
Maximum pore pressure, Pmax 15.8 15.8 MPa 
Young's modulus, E 2.89 1.03 Mpsi 
Poisson's ratio, v 0.227 0.369 – 
Cohesion, c 1746 3131 psi 
Internal friction angle, ϕ 40.77 24.16 ° 
Biot coefficient, α 0.75 0.9 – 
Adopted fracture-pressure 
threshold, Pf – 19 MPa 
 
• Pore-pressure evolution 
During the CO₂ injection period (2024–2034), pore pressure increased from 11.8 MPa to 15.8 MPa. The 
pressure response was subsequently monitored during the post-injection period from 2034 to 2534. The 
percentage increase in pore pressure was calculated as follows: 
∆𝑃 = 𝑃𝑚𝑎𝑥 − 𝑃0                            (17) 
substituting the simulated values: 
∆𝑃 = 15.8 − 11.8 
∆𝑃 = 4.0 Mpa                               (18) 
 
 
the corresponding percentage increase in pore pressure was: 
%∆𝑃 = 𝑃𝑚𝑎𝑥−𝑃0
𝑃0
× 100 
%∆𝑃 = 15.8 − 11.811.8 × 100 
%∆𝑃 = 33.9%                                 (19) 
• Effective-stress response 
The simulated pore pressure increased from 11.8 MPa to 15.8 MPa, corresponding to an increase of 4.0 
MPa or approximately 33.9%. Assuming that the total vertical stress remains approximately constant, the 
change in effective stress is governed by the Biot relationship (Biot 1941; Leal et al., 2015): 
𝜎′ = 𝜎 − 𝛼𝑃                                  (20) 
assuming that the total stress remains approximately constant during the simulated pressure increase, the 
effective-stress change can be expressed as: 
∆𝜎′ = −𝛼∆𝑃                                  (21) 
for the sandstone reservoir, the adopted Biot coefficient is 0.75. Therefore, the 4.0 MPa increase in pore 
pressure produces an effective-stress reduction of with: 𝛼 = 0.75.

634 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
∆𝜎′ = −(0.75)(15.8 − 11.8) 
∆𝜎′ = −(0.75)(4.0) 
∆𝜎′ = −3.00                                       (22) 
therefore, the 4.0 MPa increase in pore pressure results in a 3.0 MPa reduction in effective stress. Using 
the initial effective vertical stress of 15.56 MPa reported in the model, the final effective vertical stress 
is calculated as Equation 23: 
𝜎′𝑣,𝑚𝑎𝑥 =  𝜎′𝑣,0 +  ∆𝜎′ 
𝜎′𝑣,𝑚𝑎𝑥 =  15.56 − 3.00 
𝜎′𝑣,𝑚𝑎𝑥 =  12.56 𝑀𝑃𝑎                     (23) 
the percentage reduction in effective stress is therefore: 
%𝑅𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛 =
 𝜎′𝑣,0−𝜎′𝑣,𝑚𝑎𝑥
 𝜎′𝑣,0 × 100   
%𝑅𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛 =  15.56 − 12.56 15.56 × 100 
%𝑅𝑒𝑑𝑢𝑐𝑡𝑖𝑜𝑛 = 19.3%                        (24) 
The initial effective vertical stress of 15.56 MPa therefore decreases to 12.56 MPa. This 
corresponds to a reduction of approximately 19.3%.  The result demonstrates that the principal 
mechanical response during CO₂ injection is directly associated with pressure buildup. Geochemical 
alteration modifies the petrophysical state of the reservoir and can affect flow redistribution; however, 
under the assumptions of the present model, the calculated effective -stress reduction is primarily 
controlled by the increase in pore pressure. 
• Total vertical stress 
Based on the initial effective stress and Biot relationship, the corresponding total vertical stress can be 
inferred as Equation 25: 
𝜎𝑣 = 𝜎′𝑣 +  𝛼𝑃                             (25) 
using the initial reservoir conditions: 
𝜎𝑣 = 15.56 + (0.75)(11.8) 
𝜎𝑣 = 15.56 +  8.85 
𝜎𝑣 = 24.41 𝑀𝑃𝑎                           (26) 
the final effective vertical stress can subsequently be verified as Equation 27: 
𝜎′𝑣,𝑚𝑎𝑥 = 24.41 − (0.75)(15.8) 
𝜎′𝑣,𝑚𝑎𝑥 = 24.41 − 11.85 
𝜎′𝑣,𝑚𝑎𝑥 = 12.56 𝑀𝑃𝑎                   (27) 
The calculated values confirm that the effective -stress reduction is governed by the pore -pressure 
increase and the adopted Biot coefficient. 
• Mohr-coulomb failure criterion 
The mechanical stability of the caprock was evaluated using the Mohr–Coulomb failure criterion: 
𝜏𝑓 = 𝐶 +  𝜎𝑛′ tan 𝜙                     (28)

635 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
𝑛 where is 𝜏𝑓 the shear stress at failure, C is cohesion, 𝜎′ is effective normal stress, and 𝜙 is the internal 
friction angle. For the shale caprock, the cohesion is 3131 psi. Converting this value to MPa: 
𝐶 = 3131 × 0.00689476 
𝐶 = 21.59                                  (29) 
The caprock friction angle is: 
𝜙 = 24.16°                                 (30) 
Therefore: 
𝜏𝑓 = 21.59  
+ 𝜎𝑛′  tan (24.16°)                          (31) 
Since: 
Tan (24.16°)= 0.449𝜎𝑛′                (32) 
The Mohr-Coulomb failure envelope becomes: 
𝜏𝑓 = 21.59 +  0.449𝜎𝑛′                (33) 
The effective normal stress is calculated using the Biot relationship: 
𝜎𝑛′ = 𝜎𝑣 −  𝛼𝑃                              (34) 
For the shale caprock. At the initial pressure: 
𝜎𝑛,0′ = 𝜎𝑛 − (0.90)(11.8) 
𝜎𝑛,0′ = 𝜎𝑛 − 10.62                        (35) 
At the maximum simulated pressure: 
𝜎𝑛,𝑚𝑎𝑥′ = 𝜎𝑛 − (0.90)(15.8) 
𝜎𝑛,𝑚𝑎𝑥′ = 𝜎𝑛 − 3.60𝑀𝑃𝑎               (36) 
This indicates that the increase in pore pressure reduces the effective normal stress acting on the caprock 
by 3.60 MPa. Such a reduction decreases  the distance between the  in-situ stress state and  the Mohr–
Coulomb failure envelope and therefore represents an important mechanical -integrity consideration 
during CO₂ injection. 
• Fracture-pressure assessment 
The caprock fracture-pressure threshold was adopted as 19.0 MPa based on the minimum-horizontal-stress-
gradient (leak-off-test-calibrated) approach commonly used for fracture-gradient estimation in sedimentary 
basins (He et al., 2017; Wei et al., 2022).  
At the reservoir top depth of 1,200 m, this threshold corresponds to an effective fracture-pressure gradient 
of approximately 15.8 kPa/m (≈ 0.70 psi/ft), which falls within the range of 15–18 kPa/m (0.65–0.80 psi/ft) 
typically reported for the minimum horizontal stress, and hence the fracture-initiation pressure, of normally 
pressured, normally faulted sedimentary sequences at comparable depths (J. Zhang & Yin 2017).  
The same order -of-magnitude threshold is also consistent with the fracture -pressure and mechanical -
stability considerations discussed for saline -aquifer and depleted -reservoir CO₂ storage systems by 
(Rutqvist 2012) and (Adu-Gyamfy et al., 2022).

636 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Because the fracture-pressure margin (M = Pf − Pmax) and safety ratio (SR = Pf/Pmax) reported in this 
study scale directly with the adopted value of  Pf, a lower threshold within the plausible 15–18 kPa/m 
gradient range (equivalent to approximately 18.0–21.6 MPa at 1,200 m) would proportionally reduce or 
increase the calculated margin and ratio; site-specific leak -off-test or minifrac data are therefore 
recommended to replace this literature -based estimate in any future site -specific application of the 
workflow. The maximum simulated reservoir pressure was: 
𝑃𝑚𝑎𝑥 = 15.8 𝑀𝑃𝑎                (37) 
while the adopted fracture-pressure threshold was: 
𝑃𝑓 = 19.0𝑀𝑃𝑎                        (38) 
The pressure safety margin is calculated as: 
𝑀 = 𝑃𝑓−𝑃𝑚𝑎𝑥 
𝑀 = 19.0 − 15.8 
𝑀 = 3.20 𝑀𝑃𝑎                      (39) 
• Pressure Safety Ratio 
The pressure safety ratio was calculated as: 
𝑆𝑅 =
𝑃𝑓
𝑃𝑚𝑎𝑥
                            (40) 
Substituting the corresponding values: 
𝑆𝑅 = 19.015.8 
𝑆𝑅 = 1.20                            (41) 
Because the safety ratio is greater than unity and the maximum simulated reservoir pressure remains 
below the adopted fracture -pressure threshold, the simulated injection condition remains below  the 
assumed caprock failure t hreshold. Nevertheless, the 19.0  MPa fracture-pressure value is a literature -
based estimate rather than a site-calibrated measurement. Consequently, the calculated 3.2 MPa  margin 
should be interpreted as a model-based safety margin for the synthetic system rather than a field-specific 
operational limit. 
3.6 Global sensitivity analysis 
Global sensitivity analysis was performed using the Sobol variance -decomposition method to quantify the 
contribution of the investigated input parameters to the variance of cumulative secondary-mineral precipitation at 
the end of the 500 -years post -injection monitoring period. The investigated parameters were pressure, pH, 
temperature, porosity, permeability, and CO₂ injection rate.  The reported percentages repres ent the first -order 
Sobol sensitivity indices (S₁), which quantify the individual contribution of each input parameter to the variance 
of the selected response without including interaction  effects. The resulting first-order sensitivity contributions 
were 59% for pressure, 10% for pH, 7% for temperature, 1.28% for CO₂ injection rate, 0.29% for permeability, 
and 0.28% for porosity. 
The first-order contributions do not sum to 100% because the remaining variance is associated with interaction 
effects among the input parameters and the residual contribution not represented by the individual first-order terms. 
Therefore, the reported values should not be interpreted as mutually exclusive percentages of total sensitivity. Total-
order Sobol indices would additionally quantify the contribution of parameter interactions and are not represented

637 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
by the percentages reported here. 
Pressure exhibited the largest first -order contribution, indicating that variations in pressure account for the 
largest individual share of the  variance in cumulative secondary -mineral precipitation within the investigated 
parameter space. This result is physically consistent with the pressure dependence of CO₂ solubility, aqueous 
speciation, and mineral–fluid equilibrium. 
The selected response variable, cumulative secondary-mineral precipitation, was chosen because it integrates 
the long-term geochemical response over the entire monitoring period. It is particularly suitable for evaluating the 
sensitivity of mineral trapping to changes in reservoir and operational conditions. However, because the selected 
response is a geochemical rather than a direct mechanical variable, the Sobol results should  be interpreted as 
identifying the dominant controls on mineral-trapping behavior rather than as a direct sensitivity ranking of 
mechanical failure risk. The mechanical-integrity assessment is therefore evaluated separately using pore pressure, 
effective stress, fracture pressure, and pressure safety margin. 
Pressure dominates the sensitivity index b ecause CO₂ solubility, mineral dissolution, and aqueous speciation  
are fundamentally pressure-dependent processes. Consequently, pressure controls the availability of dissolved ions 
required for secondary mineral precipitation. 
Table 12.  
Summary of geomechanical responses. 
Parameter Initial Condition Maximum/Final Condition Change Interpretation 
Reservoir pressure 11.8 MPa 15.8 MPa +4.0 MPa 
(+33.9%) 
Pressure buildup during CO₂ 
injection 
Sandstone Biot 
coefficient 
0.75 0.75 – Controls pressure-induced 
effective-stress response 
Effective vertical 
stress 
15.56 MPa 12.56 MPa -3.00 MPa 
(-19.3%) 
Reduction caused by pore-
pressure increase 
Total vertical stress 24.41 MPa 24.41 MPa ~0 Inferred from initial effective 
stress 
Shale Biot 
coefficient 
0.90 0.90 – Controls caprock effective-
stress response 
Caprock effective 
normal-stress 
change 
– – -3.60 MPa Pressure-induced reduction 
Caprock cohesion 21.59 MPa 21.59 MPa – Converted from 3131 psi 
Caprock friction 
angle 
24.16 24.16 – Mohr–Coulomb parameter 
Mohr–Coulomb 
envelope 
– 𝜏𝑓 = 21.59 + 0.449𝜎𝑛′  – Caprock failure criterion 
Adopted fracture 
pressure 
– 19.0 MPa – Caprock integrity threshold 
Pressure safety 
margin 
7.2 MPa 3.2 MPa -4.0 MPa Reduced distance to fracture 
threshold 
Pressure safety ratio 1.61 1.20 -0.41 Pf/Pmax 
 
3.7 Petrophysical property evolution 
Mineral precipitation driven by geochemical alteration due to CO₂ injection in saline aquifers is controlled by 
several key parameters, including pressure, pH, temperature, CO₂ injection rate, as well as petrophysical properties 
such as porosity and permeability. Variations in these parameters not only influence the mineralization process but 
also directly affect pore structure evolution and the mechanical stability of the reservoir and caprock.

638 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Pressure is the most dominant parameter, as it controls CO₂ solubility in brine and the equilibrium of fluid –
mineral reactions. Increased pressure enhances CO₂ solubility and promotes carbonic acid (H₂CO₃)  formation, 
generating bicarbonate ions (HCO₃⁻). This accelerates the precipitation of secondary minerals, which can fill pore 
space and increase the rock matrix compactness. However, excessive pressure may inhibit CO₂ migration and cause 
stress redistribution, potentially affecting the mechanical stability of the reservoir (Bello et al., 2024). 
pH also plays a critical role in determining whether dissolution or precipitation dominates. More acidic fluids 
from carbonic acid form ation enhance mineral dissolution, which can increase porosity and weaken the rock 
framework. Conversely, more basic conditions favor the precipitation of carbonate and silicate minerals,  
increasing rock compactness and supporting mechanical stability (Helei et al., 2021; Wilkinson et al., 2009). 
Temperature influences geochemical reaction kinetics and the type of minerals formed during fluid –rock 
interactions. Higher temperatures generally accelerate precipitation rates, promoting faster changes in rock physical 
properties. However, excessively high temperatures can also enhance the dissolution of certain minerals, potentially 
reducing rock mechanical strength due to the degradation of the crystal structure (Fang et al., 2022; Raza et al., 2019). 
 
 
Figure 19.  
First-order Sobol sensitivity indices of the investigated parameters for cumulative secondary-mineral precipitation  
at the end of the 500-years post-injection monitoring period. 
 
CO₂ injection rate affects the intensity of fluid–rock interactions. High injection rates can enhance ion transport 
and accelerate mineralization reactions, promoting secondary mineral precipitation in pore spaces. This may 
locally increase rock stiffness but can also induce pore blockage, altering effective stress distribution within the 
reservoir (Papi et al., 2025). 
Petrophysical properties, such as porosity and permeability, indirectly influence mineral formation but play a 
key role in determining how the rock responds mechanically to geochemical alteration. Secondary mineral  
precipitation tends to reduce porosity and permeability by filling pores, increasing rock strength but modifying 
fluid flow paths. In contrast, mineral dissolution increases porosity and permeability, potentially weakening the 
rock framework and reducing caprock integrity (Xu et al., 2007). 
Overall, these results indicate that geochemical alteration due to CO₂ injection not only governs secondary 
mineral formation but also influences the long -term evolution of reservoir petrophysical properties and 
mechanical integrity. Secondary mineral precipitation tends to increase rock compactness by filling pore spaces,  
whereas mineral dissolution under acidic conditions can increase porosity and weaken grain bonding. Therefore,

639 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
the mechanical stability of saline aquifer systems is determined by the dynamic balance between dissolution and 
precipitation processes induced by CO₂ –fluid–rock interactions, making geochemical analysis a critical 
component for assessing long-term CO₂ storage safety. These findings highlight that controlling reservoir pressure 
and pH during CO₂ injection is essential for maintaining long-term mechanical stability of the storage system. 
3.8 Summary of key quantitative results 
Table 13.  
Simulated mineral dissolution and precipitation. 
Parameter / 
mineral Initial Final Δ Change (%) Alteration mechanism 
Porosity 0.1802473 0.1802464 −0.0000009 −0.00050 Minor change 
Permeability I 200.00 mD 199.80 mD −0.20 mD −0.10 Minor reduction 
Permeability J 20.00 mD 19.96 mD −0.04 mD −0.20 Minor reduction 
Table 13.  
Simulated Mineral Dissolution and Precipitation, (continued). 
Parameter / 
mineral Initial Final Δ Change (%) Alteration mechanism 
Permeability K 20.00 mD 19.90 mD −0.10 mD −0.50 Minor reduction 
Calcite 0.10000 0.09650 −0.00350 −3.50 Dissolution 
Dolomite 0.05000 0.04880 −0.00120 −2.40 Dissolution 
Illite 0.25000 0.24910 −0.00090 −0.36 Limited dissolution 
Kaolinite 0.02000 0.02085 +0.00085 +4.25 Precipitation 
K-feldspar 0.05000 0.05010 +0.00010 +0.20 Limited precipitation 
Quartz 0.60000 0.60040 +0.00040 +0.067 Precipitation 
 
 
4. Conclusion 
This study demonstrates that a coupled geochemical – geomechanical simulation framework can be used to 
quantitatively evaluate the long -term evolution of CO₂ storage in a synthetic deep saline -aquifer system. The 
results show that CO₂ injection promotes an initial geochemical response characterized by carbonate -mineral 
dissolution, followed by the formation of secondary minerals including K-feldspar, quartz, and kaolinite. 
The grid -sensitivity analysis using coarse, base -case, and fine vertical discretizations indicates that the 
principal pressure and effective -stress results are relatively stable. R elative to the base -case grid, the fine -grid 
differences were 0.25% for maximum pressure, 0.71% for CO₂ saturation, 0.27% for effective stress, and 0.71% 
for mineral alteration. These results support the use of the 11 × 11 × 10 grid for the principal reser voir-scale 
pressure and geomechanical assessment, while local near -caprock CO₂ saturation remains more sensitive to 
vertical resolution. 
The simulated reservoir pressure increased from 11.8 to 15.8 MPa, producing a 3.0 MPa reduction in effective 
vertical stress in the sandstone reservoir, equivalent to approximately 19.3%. The maximum simulated reservoir 
pressure remained below the adopted caprock fracture -pressure threshold of 19.0 MPa, resulting in a pressure 
safety margin of 3.2 MPa and a safety ratio of 1.20. Under the assumptions of the synthetic model, the simulated 
condition therefore remains below the adopted fracture-pressure threshold. 
The geochemical alteration modifies the reservoir petrophysical state through the competing effects of mineral 
dissolution and secondary -mineral precipitation. The resulting changes in porosity and permeability provide a 
quantitative link between geochemical reactions and fluid -flow evolution. Nevertheless, the effective -stress

640 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
reduction in the present model is primar ily controlled by pore -pressure increase through the Biot effective -
stress relationship.  
The first-order Sobol sensitivity analysis identified pressure as the largest individual contributor to the variance 
of cumulative secondary -mineral precipitation, wit h a sensitivity contribution of 59%, followed by pH and 
temperature. This result indicates that pressure is the dominant individual control on the selected geochemical 
response within the investigated parameter range. Because the Sobol response variable is  cumulative 
secondary-mineral precipitation, the sensitivity results should not be interpreted as a direct ranking of 
mechanical-failure risk.  
Overall, the study provides a reproducible numerical workflow for integrating reactive transport, petrophysical 
evolution, pressure response, effective stress, and fracture-pressure assessment. The results provide a quantitative 
basis for evaluating pressure management and long-term CO₂-storage integrity in synthetic saline-aquifer systems. 
Further work should incorporate heterogeneous reservoir and caprock properties, refined near-caprock grids, site-
specific fracture-pressure measurements, and field-scale validation against monitored CO₂-storage projects. 
 
5. Acknowledgements 
The authors would like to thank their families, friends, and lecturers in the Petroleum Engineering 
Department, Faculty of Engineering, Universitas Islam Riau, for their support during this research. 
 
6. Declarations 
6.1 Author contributions 
Citra Fitria: Conceptualization, Methodology, Investigation, Data Curation, Visualization, and Writing – 
Original Draft.  Novia Rita: Supervision, Methodology, and Writing – Review & Editing. Ayyi Husbani: 
Supervision, Validation, and Writing – Review & Editing. All authors have read and approved the final version of 
the manuscript. 
6.2 Funding statement 
This research received no specific grant from any funding agency in the public, commercial, or not -for-
profit sectors.  
6.3 Competing interest 
The authors declare that they have no competing interests. 
6.4 The use of AI and AI-assisted technology 
During the preparation of this manuscript, the authors used ChatGPT (OpenAI) for language editing, formatting 
support, and improvement of clarity. The authors reviewed and verified all AI -assisted outputs and take full 
responsibility for the final content of the manuscript.

641 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
7. Glossary of terms and symbols 
Terms & Symbol Definition Unit 
CCS Carbon Capture and Storage - 
CMG-GEM Computer Modelling Group – Generalized Equation-of-State Model - 
CO₂ Carbon dioxide - 
φf Internal friction angle degree (°) 
SR Safety ratio (Pf/Pr) - 
Margin Difference between fracture pressure and reservoir pressure MPa 
Aᵢ,RSA Reactive surface area (RSA) 
m²·m⁻³ 
 
BHP Bottom-hole pressure Mpa 
 
Sobol Index Global sensitivity index used to quantify parameter influence - 
P Pore/reservoir pressure MPa 
P₀ Initial pore pressure MPa 
Pmax Maximum simulated reservoir pressure MPa 
Pf Adopted caprock fracture-pressure threshold MPa 
M Pressure safety margin; M = P_f − Pmax MPa 
SR Pressure safety ratio; SR = P_f/Pmax – 
σ Total stress MPa 
σ′ Effective stress MPa 
σ′ᵥ,0 Initial effective vertical stress MPa 
σ′ᵥ,max Maximum/final effective vertical stress MPa 
σ′ₙ Effective normal stress MPa 
σᵥ Total vertical stress MPa 
Δσ′ Change in effective stress MPa 
ΔP Change in pore pressure MPa 
α Biot coefficient – 
E Young’s modulus MPa or Mpsi 
ν Poisson’s ratio – 
C / c Cohesion MPa or psi 
φ Internal friction angle degree (°) 
τf Shear stress at failure MPa 
k Permeability mD 
k₀ Initial permeability mD 
φ (porosity) Reservoir porosity – 
φ₀ Initial porosity – 
n Empirical exponent in the permeability–porosity relationship – 
rᵢ Reaction rate of mineral i mineral amount/time 
kᵢ Mineral-specific reaction-rate constant 1/time 
k₀,ᵢ Pre-exponential reaction-rate constant for mineral i 1/time 
Aᵢ Reactive surface area of mineral i m²/m³ 
Qᵢ Ion activity product for mineral i – 
Kₑq,ᵢ Equilibrium constant for mineral i – 
Eₐ Activation energy J/mol 
R Universal gas constant J/(mol·K) 
T Absolute temperature K 
TST Transition State Theory – 
Sg Gas/CO₂ saturation fraction

642 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
krg Gas relative permeability – 
krog Oil/gas relative permeability term reported in the model – 
Δn Mineral Change in mineral amount gmol 
ninitial Initial mineral amount gmol 
MA Mineral alteration metric % 
Sobol index Variance-based global sensitivity index – 
S₁ First-order Sobol sensitivity index – 
ST Total-order Sobol sensitivity index – 
Q Ion activity product / reaction quotient as used in the reaction-rate expression – 
H₂CO₃ Carbonic acid – 
H⁺ Hydrogen ion mol/L or activity basis 
OH⁻ Hydroxide ion mol/L or activity basis 
HCO₃⁻ Bicarbonate ion mol/L or activity basis 
CO₃²⁻ Carbonate ion mol/L or activity basis 
Ca²⁺ Calcium ion mol/L or activity basis 
Mg²⁺ Magnesium ion mol/L or activity basis 
K⁺ Potassium ion mol/L or activity basis 
Al³⁺ Aluminium ion mol/L or activity basis 
SiO₂(aq) Dissolved silica species mol/L or activity basis 
Pf Fracture pressure; equivalent notation to Pf MPa 
 
8. References 
Adu-Gyamfy, B., Ampomah, W., Tu, J., Sun, Q., Erzuah, S., & Acheampong, S. (2022). Assessment of chemo - 
mechanical impacts of - CO 2 sequestration on the caprock formation in Farnsworth oil field, Texas. Scientific 
Reports, 12(1), 13023. https://doi.org/10.1038/s41598-022-16990  
Banerjee, A. (2016). Estimation of dolomite formation: Dolomite precipitation and dolomitization. Journal of the 
Geological Society of India, 87(5), 561–572. https://doi.org/10.1007/s12594-016-0430-9  
Bello, A., Dorhjie, D. B., Ivanova, A., & Cheremisin, A. (2024). Numerical sensitivity analysis of 𝐶𝑂2 
mineralization trapping mechanisms in a deep saline aquifer. Chemical Engineering Science, 283(May 2023), 
119335. https://doi.org/10.1016/j.ces.2023.119335  
Bentham, M., Williams, G., Vosper, H., Chadwick, A., & Kirk, K. (2017). Using pressure recovery at a depleted 
gas field to understand saline aquifer connectivity. Energy Procedia , 114(November 2016), 2906 –2920. 
https://doi.org/10.1016/j.egypro.2017.03.1418  
Biot, M. A. (1941). General Theory of Three  Dimensional Consolidation . 12(2), 11 –164. 
https://doi.o rg/10.1063/1.1712886    
Bokka, H. K., Zhang, K., & Lau, H. C. (2022). Carbon capture and storage opportunities in the west coast of India. 
Energy Reports, 8, 3930–3947. https://doi.org/10.1016/j.egyr.2022.03.012  
Chen, B., Li, Q., & Tan, Y. (2025). Caprock sealing for geologic CO 2 storage: Research advances, challenges and 
prospects. Journal of Rock Mechanics and Geotechnical  Engineering, 1, 335–363. 
https://doi.org/10.1016/j.jrmge.2025.02.006  
De Silva, G. P. D., Ranjith, P. G., & Perera, M. S. (2015). Geochemical aspects of CO2 sequestratio n in deep 
saline aquifers: A Review. 155, 128–143. https://doi.org/10.1016/j.fuel.2015.03.045  
Eyitayo, S. I., Watson, M. C., Ispas, I., & Kolawole, O. (2025). Geochemical interactions of supercritical – CO2 - 
brine - rock under varying injection strategies: implications for mechanical integrity in aquifers. Rock 
Mechanics and Rock Engineering, 58(7), 7181–7202. https://doi.org/10.1007/s00603-025-04496-7

643 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Fang, Y., Zhang, F., Farfan, G. A., & Xu, H. (2022). Low -Temperature Synthesis of Disordered Dolomite and 
High- Magnesium Calcite in Ethanol − Water Solutions: The Solvation E ff ect and Implications. ACS Omega, 
7(1), 281–292. https://doi.org/10.1021/acsomega.1c04624   
Fani, M., Strand, S., Puntervold, T., & Mamonov, A. (2024). Geochemical effects of carbonated water on 
reservoir and caprock minerals for carbon capture and storage ˜ ere z Torrijos, Md Ashraful Islam Khan . 
124(September 2023). https://doi.org/10.1016/j.jgsce.2024.205246  
Fatah, A., Mahmud, H. Ben, Bennour, Z., Gholami, R., & Hossain, M. (2022). Geochemical Modelling of CO₂ 
Interactions with Shale: Kinetics of Mineral Dissolution and Precipitation on Geological Time Scales. 
Chemical Geology, 592, 1–20. https://doi.org/10.1016/j.chemgeo.2022.120742  
Fentaw, J., Emadi, H., Hussain, A., Fernandes, D. ., & Thiyagarajan, S. . (2024). Geochemistry in Geological CO 
2 Sequestration: A Comprehensive Review. Energies, 17(19), 1–35. https://doi.org/10.3390/en17195000  
Guerriero, V. (2022). One Century since Formulation of the Effective Stress Principle, the Consolidation Theory 
and Fluid – Porous-Solid Interaction Models. Geotechnics, 2(4), 961 –988. 
https://doi.org/10.3390/geotechnics2040045  
Hashemi, S. S., Kovscek, A. R., & Zoback, M. D. (2022).  SPE-210228-MS Effect of Supercritical CO 2 on the 
Poroelastic Characteristics of Poorly Cemented Sandstone Reservoirs During Depletion and Injection West 
Delta core. SPE Annual Technical Conference and Exhibition. https://doi.org/10.2118/210228-MS  
He, Z., Ding, Q., Wo, Y., Zhang, J., Fan, M., & Yue, X. (2017). Experiment of Carbonate Dissolution: Implication 
for High Quality Carbonate Reservoir Formation in Deep and Ultradeep Basins. Geofluids, 2017, 8439259. 
https://doi.org/10.1155/2017/8439259  
Helei, L., Tantikhajorngosol, P., Chan, C., & Tontiwachwuthikul, P. (2021). International Journal of Greenhouse 
Gas Control Technology development and applications of artificial intelligence for post -combustion carbon 
dioxide capture: Critical literature review and perspectives. International Journal of Greenhouse Gas Control, 
108, 103307. https://doi.org/10.1016/j.ijggc.2021.103307  
Hu, H., Wang, D., Diao, Y., Zhang, C., & Wang, T. (2024). Study on the Influencing Factors of CO2 Storage in 
Low Porosity -Low Permeability Heterogeneous Saline Aquifer. Processes, 12(12), 2933. 
https://doi.org/10.3390/pr12122933  
Ismail, I., Fotias, S. P., Pissas, S., & Gaganis, V. (2025). Optimized CO 2 Modeling in Saline Aquifers: Evaluating 
Fluid Models and Grid Resolution for Enhanced CCS Perfo rmance. Processes, 13(6), 1901. 
https://doi.org/10.3390/pr13061901  
Kanin, E., Garagash, I., Boronin, S., Zhigulskiy, S., Penigin, A., Afanasyev, A., Garagash, D., & Osiptsov, A. 
(2025). Journal of Rock Me chanics and Geotechnical Engineering Geomechanical risk assessment for CO 2 
storage in deep saline aquifers. Journal of Rock Mechanics and Geotechnical Engineering,
 17(4), 1986–2008. https://doi.org/10.1016/j.jrmge.2024.04.016 
Kempka, T., Klein, E., Lucia, M. De, Tillner, E., & Kühn, M. (2013). Assessment of long-term CO 2 trapping 
mechanisms at the Ketzin pilot site (Germany) by coupled numerical modelling. International Journal of 
Greenhouse Gas Control, 19, 720–730. https://doi.org/10.1016/j.ijggc.2013.05.014   
Khoi, L. E. N., Trong, B. U. I. V., &  Cao, M. A. I. L. (2025).  The effects of geochemical  reactions on CO 2 
sequestration in deep saline aquifers. Inżynieria Mineralna, 2(1), 82–96. https://doi.org/10.29227/IM-2025-01-
02-008  
Lasaga, A. C. (1984). Chemical Kinetics of Water -Rock Interactions. Journal of Geophysical Research: Solid 
Earth, 89(B6), 4009–4025. https://doi.org/10.1029/JB089iB06p04009  
Lasaga, A., & Steefel, C. (1998). 60656-a-coupled-model-for-transport-of-multiple-chemical-species-and-
kinetic-precipitation-dissolution-reactions-with-application-to-reactive-flow-in-single.pdf (pp. 529–592). 
American Journal of Science. https://doi.org/10.2475/ajs.294.5.529

644 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Leal, A. M. M., Blunt, M. J., & Laforce, T. C. (2015). Applied Geochemistry A chemical kinetics algorithm for 
geochemical modelling. Applied Geochemistry, 55, 46–61. https://doi.org/10.1016/j.apgeochem.2014.09.020   
Luo, A., Li, Y., Chen, X., Zhu, Z., & Peng, Y. (2022). ScienceDirect Review of CO 2 sequestration mechanism in 
saline aquifers. Natural Gas Industry B, 9(4), 383–393. https://doi.org/10.1016/j.ngib.2022.07.002  
Mouallem, J., Fathy, A., Arif, M., & Mahmoud, M. (2023). CO2 Mineral Trapping Potential of Carbonates:  A 
Numerical Investigation. SPE Middle East Oil and Gas Show and Conference, MEOS, Proceedings, March. 
https://doi.org/10.2118/213517-MS  
Mulhim, A. K. Al, & Delshad, M. (2025). CO2 Sequestration in a Carbonate Saline Aquifer: An Investigation 
into the Roles of Natural Fractures and Well Placement. 18(2), 242. https://doi.org/10.3390/en18020242  
Nghiem, L., Sammon, P., Grabenstetter, J., & Ohkuma, H. (2004). Modeling CO 2 Storage in Aquifers with a 
Fully-Coupled Geochemical EOS Compositional Simulator. SPE/DOE 14th Symposium on Improved Oil 
Recovery. https://doi.org/10.2118/89474-MS  
Nghiem, L., Shrivastava, V. K., & Kohse, B. F. (2011). Modeling Aqueous Phase Beh avior and Chemical 
Reactions in Compositional Simulation. SPE Reservoir Simulation Symposium , 1(February), 454 –468. 
https://doi.org/10.2118/141417-MS  
Oh, J., Kim, K.-Y., Han, W. S., Park, E., & Kim, J.-C. (2015). Migration behavior of supercritical and liquid CO2 
in a stratified system: Experiments and numerical simulations . 7937 –7958. 
https://doi.org/10.1002/2015WR017022  
Papi, A., Jahanbakhsh, A.,  & Maroto -valer, M. M. (2025). Preventing Salt Precipitation in CO 2 Storage 
Processes in Saline Aquifers: Dissolved -Water CO 2 Injection Method . 
https://doi.org/10.1021/acs.energyfuels.4c05249  
Ramadhani, N. F., Irawan, D., & Aziz, P. A. (2025). A Techno-Economic Approach to Optimizing CCS Fiscal 
Parameters in Indonesia: A Case Study of Integrated Oil and Gas Development in CO 2 -Rich Areas. Scientific 
Contributions Oil & Gas, 48(3), 53–66. https://doi.org/10.29017/scog.v48i3.1809  
Ranganathan, P., Hemert, P. Van, Rudolph, E. S. J., & Zitha, P. Z. J. (2011). Deep Saline Aquifers. Energy 
Procedia, 4, 4538–4545. https://doi.org/10.1016/j.egypro.2011.02.411  
Raza, A., Gholami, R., Rezaee, R., Rasouli, V., & Rabiei, M. (2019). Significant aspects of carbon capture and 
storage – A review. Petroleum, 5(4), 335–340. https://doi.org/10.1016/j.petlm.2018.12.007  
Ronlei, B. C., Wibowo, A. S., & Sigalingging, A. S. (2025). Reservoir Characterization of Ngrayong Formation, 
Sandstone with Carbonate Intercalation, using a Geostatistical Approach Based on Petrophysical Parameters, 
Northeast Java Basin, Indonesia. Scientific Contributions  Oil and  Gas, 48(3), 237–251. 
https://doi.org/10.29017/scog.v48i3.1828  
Rutqvist, J. (2012). The Geomechanics of CO2 Storage in Deep Sedimentary Formations. 525-551. 
https://doi.org/10.1007/s10706-011-9491-0  
Shi, Z., Driba, D. L., Rivera, N. L., Kariminasab, M., & Beckingham, L. E. (2024). A Review of Coupled 
Geochemical–Geomechanical Impacts in Subsurface CO 2, H 2, and Air Storage Systems . 17(12). 
https://doi.org/10.3390/en17122928  
Sugihardjo. (2022). CCUS -Aksi Mitigasi Gas Rumah Kaca dan Peningkatan Pengurasan Minyak CO 2 -EOR. 
Lembaran Publikasi Minyak Dan Gas Bumi, 56(1), 11–25. https://doi.org/10.29017/LPMGB.56.1.916  
Vilarrasa, V., Makhnenko, R., & Gheibi, S. (2016). AC. Journal of Rock Mechanics and Geotechnical 
Engineering. https://doi.org/10.1016/j.jrmge.2016.06.006

645 
 
 
 
Rita et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2135 
 
Wang, K., Xu, T., Tian, H., & Wang, F. (2016). Impacts of mineralogical compositions on different trapping  
mechanisms during long-term CO 2 storage in deep saline aquifers. Acta Geotechnica. 
https://doi.org/10.1007/s11440-015-0427-3  
Wangen, M., Gasda, S., & Bjørnarå, T. (2016). Geomechanical consequences of large -scale fluid storage in the 
Utsira Formation i n the North Sea. Energy Procedia , 97(1876), 486 –493. 
https://doi.org/10.1016/j.egypro.2016.10.056  
Wei, Z., Wang, M., Li, Y., An, Y., Li, K., Bo, K., & Guo, M. (2022). Sodium alginate as an eco-friendly rheology 
modifier and salt -tolerant fluid loss additive in water -based drilling fluids. RSC Advances, 12(46), 29852–
29864. https://doi.org/10.1039/d2ra04448j 
Wilkinson, M., Haszeldine, R. S., Fallick, A. E., Odling, N., Stoker, S. J., & Gatliff, R. W. (2009). CO₂–Mineral 
Reaction in a Natural Analogue for CO₂ Storage—Implications for Modeling. Geosciences, 79(7), 486–494. 
Worden, R. H. (2024). Carbon Dioxide Capture and Storage (CCS) in Saline Aquifers versus Depleted Gas Fields. 
Geosciences, 14(6), 146. https://doi.org/10.3390/geosciences14060146  
Xu, T., Apps, J. A., Pruess, K., & Yamamoto, H. (2007). Numerical Modeling of Injection and Mineral Trapping 
of CO 2 with H 2 S and SO 2 in a Sandstone Formation. Chemical Geology, 242(3–4), 319 –346. 
https://doi.org/10.1016/j.chemgeo.2007.03.022 
Yang, S. (2024). Evolution of the Caprock Sealing Capacity Induced by CO 2 Intrusion: A Simulation of the 
Dezhou Dongying Formation. Energies, 17(21), 5462. https://doi.org/10.3390/en17215462 
Zhang, A., Cai, M., Wei, N., Li, H., Zhang, C., Pei, J., & Wang, X. (2024). Analysis of sensitivity to hydrate 
blockage risk in natural gas gathering pipeline. Petroleum Science , 21(4), 2723 –2733. 
https://doi.org/10.1016/j.petsci.2024.01.016 
Zhang, B., Liu, Z., Zhang, H., Shi, Q., Li, Y., & Xu, C. (2022). Molecular selectivity in the water flooding heavy 
oil process from porous rocks. RSC Advances, 12(38), 24839–24848. https://doi.org/10.1039/d2ra04721g 
Zhang, J., & Yin, S. (2017). Fracture gradient prediction: an overview and an improved method. Petroleum 
Science, 14(4), 720–730. https://doi.org/10.1007/s12182-017-0182-1 
Zhu, C., Rimstidt, J. D., Zhang, Y., Kang, J., Schott, J., & Yuan, H. (2020). ScienceDirect Decoupling feldspar 
dissolution and precipitation rates at near -equilibrium wit h Si isotope tracers: Implications for modeling 
silicate weathering. Geochimica et Cosmochimica Acta , 271, 132 –153. 
https://doi.org/10.1016/j.gca.2019.12.024 
Zuo, Q., Zhang, Y., Zhang, M., Ju, B. , Ning, W., Deng, X., & Yang, L. (2024). Numerical Simulation of CO 2 
Dissolution and Mineralization Storage Considering CO 2 - Water-Rock Reaction in Aquifers. 
ACS Omega, 9(40), 41346–41359. https://doi.org/10.1021/acsomega.4c05620
