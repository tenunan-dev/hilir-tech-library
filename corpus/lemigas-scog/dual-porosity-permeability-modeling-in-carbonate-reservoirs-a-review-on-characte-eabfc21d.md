---
source_id: "lemigas-scog"
title: "Dual porosity Permeability Modeling in Carbonate Reservoirs A Review on Characterization Techniques Modeling A"
summary: "Review of how dual-porosity and related models (dual-permeability, MINC, discrete fracture networks) characterise heterogeneous carbonate reservoirs, including for CO2 storage."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2170"
retrieved_at: "2026-10-24T14:30:16+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "eabfc21dc92d8d597b3e5a8f90b22a3d2cb2b26ff5f29a1eac6825911a52923a"
collected: "manual"
---

# Dual porosity Permeability Modeling in Carbonate Reservoirs A Review on Characterization Techniques Modeling A

507 
 
https://doi.org/10.29017/scog.v49i3.2170 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 507 – 536 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Dual-porosity-Permeability Modeling in Carbonate Reservoirs:  
A Review on Characterization Techniques,  
Modeling Approaches, and CCS Applications 
 
Khalisha Shafa Yumnanisa1*, Siti Nur Fathiyah Jamaludin1, Numair Ahmed Siddiqui1,  
Jun Matsushima2, Alidu Rashid3, and Jamaluddin4 
 
1Department of Geoscience, Universiti Teknologi PETRONAS,  
Seri Iskandar 32610, Malaysia. 
2Department of Environment Systems, Graduate School of Frontier Sciences,  
The University of Tokyo, Tokyo 113-8654, Japan. 
3Centre for Subsurface Imaging, Universiti Teknologi PETRONAS,  
Seri Iskandar, Perak, 32610 Malaysia. 
4Program Studi Geologi, STT Migas,  
Balikpapan Utara, Kota Balikpapan, Kalimantan Timur 76127, Indonesia. 
*Corresponding author: Khalisha Shafa Yumnanisa (khalisha_24003615@utp.edu.my) 
Khalisa Shafa Yumnanisa: https://orcid.org/0009-0006-7808-8622 
Received:  20 April 2026; Revised: in revised form 15 June 2026; Accepted: 06 July 2026 
Available: online 30 September 2026. 
 
 
ABSTRACT - Carbonate reservoirs are extremely heterogeneous owing to fractures, vugs, micropores, and karst 
features. This heterogeneity complicates fluid-flow prediction, characterisation, and simulation in both naturally 
fractured reservoirs and carbon capture and storage (CCS). Dual -porosity modeling remains the dominant 
approach for capturing matrix –fracture interactions in these systems. This review critically assesses geological, 
petrophysical, geophysical, and dynamic characterization techniques alongside conventional dual-porosity, dual-
permeability, MINC, DFN, and hybrid continuum –discrete methods for carbonate reservoirs, with emphasis on 
CCS applications. Case studies from Central Luconia and Abu Dhabi demonstrate that dual -porosity workflows 
outperform single-porosity approaches in m ultiscale pore-system characterization, permeability prediction, and 
dynamic behavior forecasting. Nevertheless, significant uncertainties persist regarding fracture connectivity, 
multimodal pore networks, interporosity transfer functions, and history -matching non -uniqueness, directly 
impacting CO₂ injectivity, plume migration, and long -term containment security. The review further examines 
advances in digital rock physics, machine -learning-assisted workflows, uncertainty -aware simulation, and 
coupled therm al–hydraulic–mechanical–chemical modeling. Though no single framework is universally 
applicable, future progress depends on improved multiscale characterization, rigorous uncertainty quantification, 
coupled multiphysics simulation, and computationally effi cient workflows that balance geological realism with 
practical field-scale implementation. 
Keywords:  dual-porosity modeling, carbonate reservoirs, carbon capture and storage (CCS) 
 
How to cite this article: 
Khalisha Shafa Yumnanisa, Siti Nur Fathiyah Jamaludin, Numair Ahmed Siddiqui, Jun Matsushima, 
Alidu Rashid, and Jamaluddin, 2026, Dual-porosity-Permeability Modeling in Carbonate Reservoirs: A 
Review on Characterization  Techniques, Modeling Approaches, and  CCS Applications , Scientific 
Contributions Oil and Gas, 49 (3) pp. 507-536.

508 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
1. Introduction 
Carbonate reservoirs store more than 50% of the world's proven hydrocarbon reserves and remain essential to 
global energy production  and subsurface resource development (Garland et al., 2012; Malki et al., 2023) . 
However, characterization and simulation  of ca rbonate reservoirs are highly  challenging due to complex 
geological heterogeneity related to depositional variability, diagenesis, dissolution, dolomitization, and fracturing 
(Janjuhah et al., 2019; Malki et al., 2023; Xiong et al., 2025). These processes generate multiscale pore systems 
in which low -permeability matrix microporosity coexists with highly conductive fractures and vugs, creating 
strong contrasts in storage and flow behavior (Pruess & Narasimhan 1985; Janjuhah et al., 2019). 
A key feature of many carbonate reservoirs is dual-porosity behavior, in which the matrix primarily provides 
fluid storage while fractures and vugs dominate fluid flow (Wu et al., 1998; Berkowitz 2002; Cordero et al., 2019). 
This results in rapid early -time fracture flow followed by slower matrix -controlled drainage at later stages of 
production (Wu et al., 1998; Maulindani et al., 2021). In the classic dual-porosity model, fractures transport fluids 
that were initially stored in the matrix to the wellbore, emphasizing a non-direct flow pathway from the matrix to 
the wellbore. However, when matrix permeabil ity is non-negligible, as in vuggy or intercrystalline carbonates, 
fluid can migrate directly from the matrix to the wellbore, a condition represented by dual -permeability models. 
The duration and extent of matrix support for fluid flow are governed by sev eral critical parameters: 1) matrix 
permeability relative to fracture permeability, 2) fracture spacing or matrix block size, 3) capillary pressure and 
wet ability characteristics,  4) fluid viscosity  ratios, and 5) the prevailing  pressure gradient between matrix and 
fracture domains. In highly fractured systems with small matrix blocks and low matrix permeability, matrix 
drainage may persist for months to years. Conversely, in moderately fractured systems with larger matrix blocks 
and higher matrix permeability, direct matrix flow can sustain production over decades. 
To address these limitations, dual-porosity and dual-permeability models were developed to represent matrix 
and fracture systems as interacting continua. Since the pioneering work of Warren and Root (1963) and Barenblatt 
et al. (1960) , these approaches have evolved into  more advanced  formulations such as Multiple Interacting 
Continua (MINC), Discrete Fracture Network (DFN), and hybri d models (Pruess & Narasimhan 1985;  Cordero 
et al., 2019;  Moldabayeva et al., 2025) . Although these methods improve the representation of multiscale 
heterogeneity and fracture connectivity, significant challenges remain in parameter estimation, scale dependency, 
uncertainty quantification, and integration of geological and petrophysical datasets (De Boever et al., 2016;                 
Wei et al., 2021). 
The importance of dual -porosity modeling has also expanded into carbon capture and storage (CCS) 
applications. In naturally fractured carbonate reservoirs, fractures control CO₂ injectivity and migration, while the 
matrix contributes to long -term trapping through capillary and diffusion -driven processes (Janjuhah & Alansari 
2020; Xiong et al., 2025). Accurate modeling of these systems therefore requires reliable representation of coupled 
multiphase flow, matrix –fracture exchange, and reservoir heterogeneity (Zampetti et al., 2004;  Janjuhah & 
Alansari 2020; Yerima et al., 2024) . The durat ion of matrix support  in CCS is particularly important: during 
injection, fractures provide rapid conduits for CO 5₂, while matrix diffusion and capillary trapping operate over 
decades to centuries. The extent of matrix involvement depends on fracture-matrix contact area, matrix pore-throat 
size distribution, and the CO₂-brine interfacial tension. 
Despite considerable progress, existing studies remain fragmented, often focusing on specific  modeling 
techniques or isolated case studies without critically integrating geological characterization, modeling approaches, 
and CCS applications (De Boever et al., 2016;  Wei et al., 2021) . In addition, the strengths, limitations, and 
applicability of different dual-porosity frameworks are rarely evaluated systematically across varying carbonate 
reservoir conditions. 
This review critically examines current dual -porosity modeling approaches in carbonate reservoirs by 
synthesising advances in characteriza tion techniques, modeling frameworks, and CCS applications. Carbonate 
reservoirs in the Central Luconia Province, offshore Sarawak, are of particular interest because of their pronounced 
multiscale heterogeneity and dual-porosity behavior (Janjuhah et al., 2019). This area is also selected as a focus study 
because it has been the largest gas-producing province in Southeast Asia from the 1960s to the present day.

509 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
In addition, this paper includes a global analogue from the Abu Dhabi carbonate reservoir. It also identifies 
major research gaps in multimodal pore systems, parameter uncertainty, data integration, and computational 
limitations, while highlighting emerging directions in digital rock physics, machine learning, and coup led 
geomechanical reactive transport modeling. 
 
2. Methodology 
2.1 Critical review of modeling approaches 
2.1.1 Single porosity model 
Single porosity models treat the reservoir as a single, homogeneous continuum where all pore spaces are 
interconnected and contribute equally to fluid storage and flow (Warren & Root 1963; Ding 2022). This approach, 
governed by the classical Darcy equation  for a single medium, is computationally efficient and mathematically 
straightforward, making it widely adopted for conventional sandstone and clastic reservoirs. However, in 
carbonate reservoirs characterized by bimodal pore systems comprising low -permeability matrix and high-
permeability fractures, the single porosity assumption proves fundamentally inadequate (Jones & Xiao 2005). The 
absence of fracture-dominated flow pathways in these models leads to systematic underestimation of reserves by 
up to 30% in some complex carbonat e buildups and poor history matching against observed production data 
(Malki et al., 2023). Recent comparative studies show that single porosity simulations consistently underpredict 
early-time production rates and overestimate  late-time recovery because they cannot capture rapid, fracture -
dominated flow followed by slow matrix drainage (De Boever et al., 2016; March et al., 2018). 
2.1.2 Dual-porosity model 
The conceptualization of fluid flow in naturally fractured carbonate reservoirs has evolved significantly over 
the past six decades, driven by the need to reconcile idealised mathematical representations with the complex 
reality of multiscale pore systems. This secti on traces the development of dual -porosity and dual -permeability 
models, emphasising the evolving assumptions regarding matrix -fracture flow pathways and domain coupling 
mechanisms that distinguish these approaches. 
The classic dual -porosity model, pioneer ed by Warren and Root (1963)  and Barenblatt et al. (1960) , was 
predicated on a strict functional separation between matrix and fracture domains: the matrix served exclusively 
as a storage medium (characterized by high porosity but negligible permeability), while fractures provided the 
sole conduits for fluid flo w to the wellbore (Bai et al., 1994;  March et al., 2018) . Figure 1a  presents this 
conceptualization, where flow pathways (indicated by red arrows) show unidirectional transfer from matrix blocks 
to the fracture network, with no direct matrix-wellbore connection permitted. 
Although mathematically tractable, the classic dual -porosity assumption proved overly restrictive for many 
real-world carbonate reservoirs, particularly  when the  matrix possessed non-negligible permeability or when 
fracture networks were sparse. This limitation became especially apparent in carbonates, where matrix 
permeability arises from interconnected vugs, molds, or intercrystalline porosity. Dual -permeability models 
(DPM) addressed this constraint by allowing simultaneous and coupled flow in both matrix and fracture domains. 
In these formulations, fluid can migrate directly from matrix blocks to the wellbore, independent of the fracture 
network, capturing scenarios where both domains contribute meaningfully to production and pressure support 
(Egya et al., 2019; Matsushima et al., 2021). 
The distinction between these modeling frameworks fundamen tally rests on assumptions about flow-domain 
connectivity. Figure 2  shows a schematic of pore -scale flow pathways within a representative elementary 
volume (REV) of carbonate rock, highlighting four critical assumptions underpinn ing dual -
porosity/permeability formulations.

510 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
 
Figure 1.  
Evolution of dual-porosity modeling frameworks illustrating the progressive relaxation of domain-coupling assumptions from 
left to right. (a) The classic dual-porosity model is where the matrix acts solely as a storage medium with negligible 
permeability, and fractures provide the only flow pathways to the wellbore. (b) The dual-permeability model demonstrates both 
matrix and fractures contributing to fluid flow and storage, permitting direct matrix-wellbore communication. (c) The multiscale 
hybrid model incorporates explicit fracture geometry and discrete fracture networks for improved geological realism. 
 
 
 
 
Figure 2.  
Pore-scale flow pathways and domain coupling assumptions within a representative elementary volume (REV) of carbonate 
rock. (a) Schematic illustration of four critical assumptions underpinning dual-porosity/dual-permeability formulations: 
matrix block geometry, fracture connectivity, interporosity transfer mechanisms, and flow domain coupling. (b) 
Comparative schematic of dual-porosity and dual-permeability modeling approaches showing differences in matrix-
fracture flow connectivity and wellbore communication pathways. 
 
2.1.3 Dual-permeability model 
This paper compares five major modeling approaches and their underlying assumptions. These  include the 
Warren-Root model, the Kazemi model, the Dual -Permeability Model, the Multiple  Interacting Continua 
(MINC), and the Discrete Fracture Network (DFN). The Warren-Root model assumes no matrix flow and pseudo-
steady-state transfer, appropriate for highly fractured systems where matrix permeability is orders of magnitude 
lower than fracture permeability. Meanwhile, the dual-permeability model relaxes the "no matrix flow" constraint, 
permitting Darcy flow in both domains when the permeability contrast is moderate. The Kazemi (1969)  model 
a). b). c).

511 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
significantly advanced this framework by introducing a numerical formulation f or naturally fractured reservoirs. 
Unlike earlier analytical solutions, the Kazemi approach enabled simulation of more complex matrix -fracture 
geometries and transient flow behaviors, providing a critical foundation for modern dual-porosity simulators. For 
extreme matrix heterogeneity common in carbonates with separate vuggy porosity, the Multiple Interacting 
Continua (MINC) method subdivides the matrix into nested continua (Rahman & Pierson 2011) . This example 
addresses both porosity and permeability together. 
2.1.4 Advanced models 
• Multiple interacting continua (MINC) method 
The Multiple Interacting Continua (MINC) method was developed by Pruess and Narasimhan (1985)  to 
address the limitations of the classical dual -porosity formulation when matrix heterogeneity is extreme. 
Unlike the Warren and Root (1963) approach, which treats the entire matrix as a single continuum with a 
single interporosity transfer coefficient, MINC subdivides the matrix block into nested shells or layers, 
each with its own porosity, permeability, and exchange term. This nested struct ure captures the transient, 
spatially varying pressure gradients within the matrix that the pseudo-steady-state assumption of the classic 
model cannot resolve. In carbonate reservoirs with multimodal pore -throat distributions, such as those 
found in Centra l Luconia where microporosity, mesoporosity, and vuggy macroporosity coexist, MINC 
provides significantly more accurate representations of fluid exchange dynamics (Makhankova et al., 2021; 
Jiménez et al., 2024). 
• Discrete fracture network (DFN) model 
The Discrete Fracture Network (DFN) model represents an alternative paradigm that abandons the continuum 
approximation in favor of explicit, deterministic fracture geometry (Henglai et al., 2025). In DFN simulations, 
each fracture is mapped as a discrete planar feature with orientation, aperture, length, and connectivity derived 
from outcrop analogues, borehole image logs, or seismic attributes (Alabere et al., 2023) . This explicit 
representation is essential for carbonate reservoirs where fracture corridors and karst conduits create localized 
high-permeability pathways that dominate flow. Because DFN models remain computationally demanding 
at the field scale, hybrid DFN –dual-porosity workflows have been increasingly adopted, in which DFN 
characterizes near-wellbore or critical flow paths while dual-porosity approximations represent the far-field 
matrix (Gerke & Van Genuchten 1993; Cordero et al., 2019). 
• Hybrid models 
Hybrid models combine the computational efficiency of continuum dual -porosity or dual -permeability 
formulations with the geometric fidelity of discrete fracture networks (Yerima et al., 2024) . In a typical 
hybrid workflow, lar ge-scale deterministic fractures (e.g., seismic -scale fault corridors) are embedded 
explicitly within a continuum matrix -fracture grid, while smaller background fractures are homogenized 
into effective dual -porosity properties (Nguyen et al., 2018;  Zambrano et al., 2021) . This approach 
balances accuracy and efficiency: explicit fractures capture near-wellbore dynamics, injectivity, and early-
time breakthrough, while continuum approximations keep simulation times feasible for full -field 
forecasting. Hybrid models have shown promise for CCS applications, where accurately representing CO₂ 
migration along preferential pathways is critical for containment assessment (Nguyen et al., 2018;  
Zambrano et al., 2021). 
Recent advances have moved beyond continuum approximations to represent multiscale heterogeneity explicitly. 
The Discrete Fracture Network (DFN) model and hybrid continuum -discrete approaches incorporate spatial 
variability in fracture orientation, intensity, and connectivity directly into the simulation grid. These methods are 
particularly relevant for carbonate reservoirs where fracture corridors, karst features, and diagenetic alterations create 
deterministic heterogeneity that stochastic models cannot adequately represent (Zambrano et al., 2021). Integrating 
machine learning and digital rock physics represents the current frontier in dual -porosity characterization. These 
techniques enable direct identification and parameterization of multiscale pore features from core samples, borehole 
images, and digital reconstructions, providing the geological foundation necessary to select appropriate modeling 
assumptions (Al Hameli et al., 2022).

512 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
2.1.5 Comparative evaluation of modeling approaches 
The comparative assessment of modeling approaches highlights the evolution of reservoir simulation 
techniques from simplified homogeneous representations to increasingly sophisticated frameworks that capture 
the multiscale heterogeneity characteristic of carbonate reservoirs. The suitability of each modeling approach 
depends strongly on reservoir complexity, fracture connectivity, matrix permeability contribution, data 
availability, and computational constraints (Table 1). 
Single porosity models remain the simplest and most computationally efficient approach for reservoir 
simulation because they treat the reservoir as a homogeneous continuum with uniformly distributed porosity 
and permeability (Warren & Root 1963;  Ding 2022) . These models are generally adequate for relatively 
homogeneous clastic reservoirs where pore connectivity is continuous, and fracture influence is limited. However, 
their application to carbonate reservoirs is fundamentally limited because they cannot represent bimodal pore 
systems and matrix–fractureinteractions (Jones & Xiao 2005; Malki et al., 2023). In fractured carbonate systems, 
fluid flow is commonly dominated by highly conductive fractures and vugs, whereas the low-permeability matrix 
primarily controls hydrocarbon storage. Because single porosity models cannot separate these domains, they often 
underestimate reserves, misrepresent pressure behavior, and fail to reproduce characteristic production trends such 
as rapid early-time fracture flow followed by slower matrix drainage (De Boever et al., 2016; Malki et al., 2023). 
Dual-porosity models were developed to overcome these limitations by representing the matrix and fracture 
systems as separate interacting continua (Bai et al., 1994; March et al., 2018). In this framework, fractures primarily 
control fluid flow, while the matrix acts as the dominant storage domain. The separation significantly improves the 
representation of naturally fractured carbonate reservoirs and allows more realistic simulation of matrix –fracture 
exchange processes (March et al., 2018; Maulindani et al., 2021). Dual-porosity models are particularly effective in 
highly fractured systems where fracture permeability exceeds matrix permeability by several orders of magnitude 
(De Boever et al., 2016; Wei et al., 2021). Their ability to reproduce both early-time fracture-dominated production 
and late-time matrix-controlled drainage explains their widespread adoption in carbonate reservoir simulation. 
Nevertheless, these models rely heavily on pseudo-steady-state assumptions and typically neglect direct matrix flow, 
which may oversimplify carbonate reservoirs containing connected vuggy or intercrystalline pore systems (Zampetti 
et al., 2004; De Boever et al., 2016). Furthermore, the interporosity transfer coefficient (α), matrix block size, and 
fracture spacing are difficult to constrain directly at reservoir scale, introducing significant calibration uncertainty 
and non-uniqueness during history matching (Rahman & Pierson 2011; Wei et al., 2021). 
Dual-permeability models extend the dual-porosity concept by allowing simultaneous flow in both matrix and 
fracture domains (Zampetti et al., 2004;  Moldabayeva et al., 2025) . This provides a more physically realistic 
representation of carbonate reservoirs, where the matrix contributes meaningfully to fluid flow through connected 
vugs, interparticle pores, or intercrystalline permeability (Fuentes-Cruz & Valko 2015) . Compared with classic 
dual-porosity models, dual -permeability formulations improve predictions of pressure propagation, sweep 
efficiency, and long-term recovery behavior in moderately fractured systems (Egya et al., 2019;  Matsushima et 
al., 2021). However, this increased realism comes at the expense of greater model complexity. Dual permeability 
models require additional parameters, including separate permeability tensors and relative permeability functions 
for both continua, substantially increasing calibration difficulty and computational demand (Zampetti et al., 2004; 
Correia et al., 2011) . As a result, parameter non -uniqueness becomes a major challenge, particularly when  
geological and petrophysical constraints are limited. 
The Multiple Interacting Continua (MINC) method represents a further advancement designed to address 
transient matrix –fracture flow behavior and internal matrix heterogeneity (Jiménez et al., 2024;  Trianto et al., 
2026). Rather than treating the matrix as a single continuum, MINC subdivides matrix blocks into nested 
continua, enabling improved representation of diffusion -dominated flow and transient pressure equilibration 
processes (Makhankova et al., 2021) . This approach is particularly beneficial in carbonate reservoirs with 
multimodal pore -throat distributions and strong microporosity development, where fluid transfer between 
fractures and matrix occurs gradual ly rather than instantaneously. MINC models provide improved physical 
realism but are also significantly more computationally intensive than conventional dual -porosity approaches 
(Fleury & Soualem 2009;  Jabbari & Zeng 2011) . In addition, defining representative nested continua and

513 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
upscaling pore -scale heterogeneity to reservoir -scale simulation remain major sources of uncertainty. 
Consequently, MINC methods are often restricted to det ailed sector studies or research -oriented applications 
rather than routine full -field simulation.  
Discrete Fracture Network (DFN) models provide the highest degree of geological realism by explicitly 
representing fracture geometry, orientation, aperture, s pacing, and connectivity (Alabere et al., 2023; Henglai et 
al., 2025). Unlike continuum-based approaches, DFN models simulate fractures as discrete geological features, 
making them particularly effective for reservoirs dominated by fracture corridors, karst systems, and strongly 
anisotropic fracture networks (Zambrano et al., 2021) . These models are highly valuable for evaluating near -
wellbore flow behavior, fracture connectivity, and preferential  fluid migration pathways.  However, extreme 
computational demands and the scarcity of field-scale fracture characterizationdata severely limit their practical 
application (Moonen & Carmeliet 2013;  Alabere et al., 2025) . Fracture connectivity and scaling uncertainty 
remain major limitations because local fracture observations from cores or image logs may not accurately 
represent reservoir-scale fracture architecture. 
Hybrid continuum –DFN models balance computational efficiency with geological realism by combining 
explicit representations of major fractures with continuum approximations for smaller-scale fracture systems and 
matrix flow (Barenblatt et al., 1960;  Nguyen et al., 2018) . These approaches are  more relevant for complex 
carbonate reservoirs where deterministic fracture corridors coexist with diffuse background fracturing.  Hybrid 
models improve simulation of localized, fracture -dominated transport while remaining computationally feasible 
for larger-scale forecasting. Hybrid models are also particularly relevant for CCS applications, where accurately 
represented preferential CO₂ migration pathways are essential for injectivity and containment assessment (Nguyen 
et al., 2018). Nevertheless, hybrid approaches remain more computationally demanding than classic models and 
require careful coupling between discrete and continuum domains. Additionally, uncertainty in fracture upscaling 
and interactions between explicit and  homogenized fracture systems continue to pose significant modeling 
challenges (Alabere et al., 2025). 
The comparative evaluation (Table 1) demonstrates that no single modeling approach is universally applicable 
to all carbonate reservoirs.  Simpler continuum models offer computational efficiency but  often oversimplify 
geological complexity; conversely, advanced methods improve physical realism at the expense of increased 
parameter uncertainty, stringe nt data requirements, and high computational costs. Model selection should 
therefore be guided by reservoir heterogeneity, fracture intensity, pore system connectivity, available datasets, 
and the specific objectives of the simulation study. In practice, t he trade-off between geological realism and 
computational practicality remains a central challenge in dual-porosity reservoir modeling. 
2.1.6 Key limitations and uncertainties in dual-porosity-permeability modeling 
Despite their widespread application in carbonate reservoir simulation, models for dual porosity and dual 
permeability remain subject to several important limitations that affect predictive reliability and  field-scale 
applicability. Although representations of matrix–fracture systems in dual-porosity and dual-permeability models 
are practical, they rely on simplified assumptions that may not adequately capture the extreme heterogeneity and 
multiscale pore complexity characteristic of carbonate reservoirs (De Boever et al., 2016;  March et al., 2018) . 
Consequently, uncertainty in model structure, parameter estimation, and scale integration remains a major 
challenge in both hydrocarbon production forecasting and CCS applications. 
• Simplified matrix–fracture geometry 
One of the primary limitations of conventional dual -porosity and dual -permeability formulations is the 
assumption of simplified and idealised matrix–fracture geometry. Classic dual-porosity and dual-permeability 
models typically represent the reservoir as regularly shaped matrix blocks surrounded by uniformly distributed 
fractures (Bai et al., 1994;  March et al., 2018) . However, natural carbonate reservoirs rarely exhibit such 
regular fracture distrib utions. Instead, fracture systems are commonly characterized by strong anisotropy, 
irregular spacing, fracture corridors, and localized karst features that create  highly heterogeneous flow 
pathways (Correia et al., 2011; De Boever et al., 2016). This structural oversimplification can lead to an

514 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
inaccurate representation of fracture connectivity and pressure propagation, particularly in reservoirs where 
flow is strongly influenced by large vugs, dissolution channels, or fault-related fracture systems (Zambrano et 
al., 2021) . In highly heterogeneous carbonate reservoirs, continuum -based assumptions may therefore 
oversimplify localized flow behavior and underestimat e preferential transport pathways. Although DFN and 
hybrid continuum –discrete models improve  geological realism, they also introduce substantially  greater 
computational and data requirements (Barenblatt et al., 1960; Henglai et al., 2025). 
• Uncertainty in matrix–fracture transfer parameters 
The interporosity transfer coefficient ( α) remains one of the most uncertain parameters in dual -porosity and 
dual-permeability simulations because it gov erns fluid exchange between the matrix and fracture domains 
(Rahman & Pierson 2011;  Wei et al., 2021) . Although α can be estimated from analytical  relationships, 
laboratory experiments, or h istory matching, it cannot be measured directly at the reservoir scale in the 
subsurface. Consequently, multiple parameter combinations may produce equally acceptable history matches, 
leading to significant non -uniqueness in model calibration (Trianto et al., 2026) . Furthermore, transfer 
behavior is strongly scale-dependent and influenced by fracture spacing, matrix block geometry, wettability, 
and pore connectivity (De Boever et al.,  2016). Small variations in α may significantly alter production 
forecasts, pressure depletion behavior, and matrix drainage efficiency, particularly during late-time production 
(Barenblatt et al., 1960) . This uncertainty becomes even more pronounced in carbonate reservoirs with 
multimodal pore systems, where matrix –fracture exchange often deviates substantially from the pseudo -
steady-state assumptions used in classical dual-porosity models (Jiménez et al., 2024). 
• Limitations in multimodal carbonate pore systems 
Most dual-porosity models assume a binary separation between matrix storage and fracture flow. However, 
carbonate reservoirs commonly feature far  more complex pore architectures where m icropores, mesopores, 
vugs, fractures, and karst networks coexist within the same reservoir interval (De Boever et al., 2016; Jiménez 
et al., 2024). In many carbonate systems, connected vuggy or intercrystalline porosity contributes significantly 
to fluid flow, which violates the classical assumption that matrix permeability is negligible (Zampetti et al., 
2004; Moldabayeva et al., 2025) . As a result, conventional dual -porosity models may oversimplify pore 
connectivity and underestimate internal matrix flow dynamics. This limitation is particularly critical in 
reservoirs with strong microporous development, where fluid transfer occurs gradually through diffusion -
dominated processes rather than through instantaneous pressure equilibration (Makhankova et al., 2021;  
Jiménez et al., 2024). Although advanced approaches such as the MINC method improve the representation 
of transient matrix behavior, they also increase computational complexity and require a detailed 
characterization of the internal pore structure (Fleury & Soualem 2009;  Jabbari & Zeng  2011). 
• Scale dependency and data integration challenges 
Another major challenge in dual-porosity and dual-permeability modeling is integrating multiscale geological 
and petrophysical datasets into reservo ir-scale simulation models. Parameters derived from core analysis, 
nuclear magnetic resonance (NMR), mercury injection capillary pressure (MICP), and petrographic 
observations often reflect pore-scale or laboratory-scale conditions that are not directly tr ansferable to field-
scale simulations (Omidpour et al., 2022;  Rahman & Pierson 2011) . Upscaling these measurements while 
preserving representative matrix–fracture interactions remains highly uncertain, particularly in heterogeneous 
carbonate reservoirs. Furthermore, fracture characterizationintroduces additional uncertainty because fracture 
orientation, connectivity, and aperture distribution are often inferred indirectly from image logs, seismic 
attributes, or outcrop analogues (Alabere et al., 2023;  Henglai et al., 2025) . These datasets o ften may 
inadequately represent reservoir-scale fracture networks, resulting in discrepancies between static geological 
models and dynamic simulation behavior (Zambrano et al., 2021) . Consequently, extensive calibration and 
history matching are frequently required to  reconcile geological observations with production performance 
(De Boever et al., 2016; March et al., 2018).

515 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Table 1. 
Comparative Assessment of Dual-Porosity Modeling Approaches 
Model Major Strength Major Limitation Best Reservoir Type Main Uncertainty References 
Single 
Porosity 
Model 
Computationally efficient, 
mathematically simple, 
and suitable for rapid 
simulation and preliminary 
reservoir evaluation. 
Assumes homogeneous 
porosity and permeability, 
making it unable to 
represent fracture-
dominated flow or matrix–
fracture interactions in 
carbonate reservoirs. 
Homogeneous clastic 
reservoirs and low-
fracture formations 
with relatively uniform 
pore connectivity. 
Reservoir 
heterogeneity and 
fracture connectivity 
are poorly 
represented, leading 
to uncertainty in 
production 
prediction. 
(Warren & Root 
1963; Jones & Xiao 
2005; Ding 2022) 
Dual-porosity 
Model 
Separates matrix storage 
from fracture flow, 
allowing realistic 
representation of early-
time fracture-dominated 
production and late-time 
matrix drainage. 
Assumes negligible matrix 
permeability and pseudo-
steady-state matrix–
fracture transfer, which 
may oversimplify 
heterogeneous carbonate 
systems. 
Highly fractured 
carbonate reservoirs 
where fracture 
permeability dominates 
flow and the matrix 
primarily acts as 
storage. 
Interporosity transfer 
coefficient (α), 
matrix block size, 
and fracture spacing 
remain difficult to 
constrain at reservoir 
scale. 
(Bai et al., 1994; De 
Boever et al., 2016; 
March et al., 2018; 
Maulindani et al., 
2021; Wei et al., 
2021) 
Dual- 
Permeability 
Model 
Allows simultaneous flow 
in both matrix and fracture 
domains, improving 
realism in reservoirs with 
connected matrix 
permeability or vuggy 
systems. 
Requires additional 
parameters and calibration 
effort, increasing 
computational cost and 
numerical instability. 
Carbonate reservoirs 
with moderate 
permeability contrast 
and partially 
conductive matrix 
systems. 
Strong uncertainty in 
matrix–fracture 
permeability 
partitioning and 
relative permeability 
calibration. 
(Zampetti et al., 2004; 
Fuentes-Cruz & V alko 
2015; Egya et al., 
2019; Matsushima et 
al., 2021; 
Moldabayeva et al., 
2025) 
MINC 
(Multiple 
Interacting 
Continua) 
Model 
 
Captures transient matrix–
fracture exchange more 
accurately by subdividing 
the matrix into nested 
continua. 
Computationally intensive 
and difficult to implement 
efficiently at full-field 
scale. 
Carbonate reservoirs 
with strong matrix 
heterogeneity and 
multimodal pore throat 
distributions. 
Uncertainty in 
upscaling nested 
continua and defining 
representative matrix 
subdivisions. 
(Makhankova et al., 
2021; Jiménez et al., 
2024; Trianto et al., 
2026) 
Discrete 
Fracture 
Network 
(DFN) Model 
Explicitly represents 
fracture geometry, 
orientation, aperture, and 
connectivity, providing 
high geological realism. 
Highly data-intensive and 
computationally 
demanding, particularly 
for field-scale simulation. 
Reservoirs dominated 
by fracture corridors, 
karst systems, and 
strongly anisotropic 
fracture networks. 
Fracture connectivity, 
spatial distribution, 
and scaling of 
fracture properties to 
reservoir-scale 
models. 
(Gerke & V an 
Genuchten 1993; 
Moonen & Carmeliet 
2013; Alabere et al., 
2023; Henglai et al., 
2025) 
Hybrid 
Continuum–
DFN Model 
Combines continuum 
efficiency with explicit 
fracture representation, 
improving simulation of 
both matrix flow and 
localized fracture 
transport. 
Complex model 
construction and coupling 
between continuum and 
discrete domains increase 
calibration difficulty. 
Complex carbonate 
reservoirs containing 
both diffuse fractures 
and major deterministic 
fracture systems. 
Coupling consistency 
between DFN and 
continuum domains 
and uncertainty in 
fracture upscaling. 
(Barenblatt et al., 
1960; Nguyen et al., 
2018; Zambrano et 
al., 2021; Yerima et 
al., 2024) 
 
• Computational and numerical limitations 
Increasing geological realism generally comes at the expense of computational efficiency. While classical  
dual-porosity models remain relatively efficient for full-field simulation, advanced methods such as MINC, 
DFN, and hybrid continuum–discrete models require significantly greater computational resources  (Jabbari 
& Zeng 2011; Alabere et al., 2025). Because explicit fracture representation substantially increases 
grid complexity, numerical coupling requirements, and simulation runtime, these computational constraints 
become more pronounced, particularly in reservoirs with multiscale fracture networks (Cordero et al., 2019; 
Alabere et al., 2025) . Consequently, large -scale uncertainty  quantification and probabilistic forecasting 
become less feasible since multiple simulation realisations are required. As a result, many field -scale studies 
continue to rely on simplified dual -porosity approximations despite their known geological limitations 
(Barenblatt et al., 1960; De Boever et al., 2016) . Thus, balancing computational practicality with geological 
realism remains one of the central challenges in carbonate reservoir modeling.

516 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
• CCS-specific modeling limitations  
Additional challenges arise when dual -porosity models are applied to CCS systems. In fractured carbonate 
reservoirs, fractures enhance CO₂ injectivity and plume migration but may also serve as potential leakage 
pathways if fracture connectivity and geomechanical behavior are not accurately represented (Tsakiroglou et 
al., 2009;  Fuentes-Cruz & Valko 2015) . Conventional dual -porosity models often neglect co upled 
geomechanical effects, stress -dependent fracture permeability, and fracture reactivation, potentially 
underestimating long -term containment risks (Koša 2015;  Khalid et al., 2024) . Likewise, be cause many 
formulations do not explicitly incorporate reactive transport processes between CO₂, formation  brine, and 
carbonate minerals, they may miss effects on porosity evolution and long-term storage behavior        (Fuentes-
Cruz & Valko 2015;  Nguyen et al.,  2018). Capillary trapping and wet ability effects are also commonly 
simplified, introducing additional uncertainty in predictions of plume migration and storage efficiency 
(Berkowitz 2002; Koša 2015). Hence, reliable CCS forecasting in carbonate reservoirs increasingly requires 
coupled flow –geomechanical–reactive transport models capable of representing both fracture -controlled 
migration and long-term matrix trapping processes. These limitations demonstrate that no single dual-porosity 
modeling approach is universally applicable to all carbonate reservoirs. Model reliability depends strongly on 
reservoir heterogeneity, fracture architecture, pore connectivity, available datasets, and simulation objectives. 
Future developments should therefore focus on improving multiscale characterization, reducing parameter 
uncertainty, integrating coupled physical processes, and developing computationally efficient workflows that 
balance geological realism with practical field-scale applicability. 
 
3. Result and discussion 
3.1 Evaluation of characterization techniques for dual-porosity carbonate reservoirs 
Accurate characterizationof carbonate reservoirs is fundamental for reliable dual -porosity modeling because 
fluid storage and flow behavior are strongly controlled by multiscale heterogeneity, fracture connectivity,  and 
complex pore architectures (De Boever et al., 2016; Janjuhah et al., 2019). In contrast to relatively homogeneous 
clastic systems, carbonate reservoirs commonly contain interconnected micropores, vugs, fractures, and karst 
features that coexist across multiple spatial scales (Pruess & Narasimhan 1985; Jiménez et al., 2024). As a result, 
these heterogeneities significantly influence permeability distribution, matrix –fracture interaction, and reservoir 
performance, making reservoir characterization critical and high ly uncertain stage of dual -porosity simulation 
(Rahman & Pierson 2011;  Wei et al., 2021) . Because no single characterizationtechnique can fully capture the 
complexity of carbonate  pore systems and fracture networks, integrated  workflows combining geological, 
petrophysical, geophysical, and dynamic datasets are required to constrain reservoir heterogeneity and improve 
simulation reliability (Barenblatt et al., 1960; De Boever et al., 2016) . However, integrating multiscale datasets 
into reservoir-scale models remains highly challenging due to scale mismatch, data uncertainty, and incomplete 
fracture representation. Table 2 compares the various characterization techniques used in dual-porosity carbonate 
reservoir modeling. 
3.2 Core-based and petrophysical characterization techniques 
Core-based analyses remain among  the most important methods for  evaluating carbonate pore systems and 
matrix properties. Routine core analysi s (RCAL), special core analysis (SCAL), petrographic  analysis, and 
mercury injection capillary pressure (MICP) measurements are widely used to characterise porosity distribution, 
pore-throat geometry, wet ability, and capillary behavior (Egya et al., 2019;  Omidpour et al., 2022) . These 
techniques provide valuable pore -scale information that improves understanding of matrix storage capacity and 
fluid transport mechanisms. MICP and petrographic analyses are particularly useful for identifying microporosity 
development and pore throat  distributions in carbonate reservoirs (Omidpour et al., 2022). Figure 3 shows the 
image processing workflow applied to thin-section data, demonstrating how original images are segmented 
and analyzed to extract pore geometry, spatial distribution, and quantitative pore-structure characteristics.

517 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
 
 
Figure 3.  
Image processing workflow for pore structure identification and quantification in carbonate thin sections. (a) Original thin-
section photomicrograph under plane-polarized light showing the heterogeneous distribution of pore types. (b) Binary 
segmentation mask highlighting porosity (white) versus solid matrix (black) after image thresholding. (c) Quantified pore 
network map showing individual pore boundaries, size classification, and connectivity indices used to derive dual-porosity 
parameters for reservoir simulation. 
 
 
 
Carbonate reservoirs commonly exhibit strong spatial variability, which implies core-scale measurements may 
not accurately capture large-scale fracture connectivity  or vug distribution (Figure 4). As a result, laboratory -
derived petrophysical properties are often difficult to upscale into representative simulation  parameters for dual-
porosity models. Nuclear magnetic resonance (NMR) logging has become increasingly important for 
characterizing pore -size distribution and fluid mobility in car bonate reservoirs (Matsushima et al., 2021) . 
Furthermore, NMR measurements can effectively differentiate between movable and immovable fluids and 
improve the identification of microporous intervals. Nevertheless, permeabil ity estimation from NMR remains 
indirect and strongly dependent on calibration relationships that may vary significantly between carbonate facies 
(Rahman & Pierson 2011) . Consequently, this uncertainty in pore -system interpretation may propagate directly 
into matrix permeability estimations and interporosity transfer calculations. 
3.3 Well logging and borehole imaging techniques 
Well logs and borehole imaging tools are essential for evaluating fracture distributions, lithofacies variations, 
and dynamic reservoir properties. Conventional logs, including density, neutron, sonic, and resistivity logs, are 
widely used to estimate porosity and fluid saturation (Egya et al., 2019) . However, their abilit y to distinguish 
between matrix porosity, vugs, and fractures is often limited in highly heterogeneous carbonate systems                           
(De Boever et al., 2016).

518 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Formation microimager (FMI) logs and other borehole image logs provide improved fracture characterization 
by identifying fracture orientation, density, aperture, and dip (Henglai et al., 2025). These datasets are particularly 
valuable for constraining fracture network s in dual-porosity and DFN models. Additionally, sonic and acoustic 
logs also provide indirect indications of fracture intensity and  mechanical heterogeneity (Alabere et al., 2023). 
Despite their importance, borehole imaging tools characterize fractures only near the wellbore and may not 
adequately represent reservoir -scale fracture connectivity (Zambrano et al., 2021) . As a result, fracture 
interpretation often remains highly uncertain, particu larly in reservoirs with anisotropic fracture systems or 
localized fracture corridors. 
3.4 Seismic and dynamic characterization approaches 
Seismic interpretation and dynamic reservoir data provide larger -scale constraints on carbonate reservoir 
heterogeneity and fracture distributions. Three -dimensional (3D) seismic data are commonly used to identify 
major structural features, faults, and fra cture corridors that influence fluid flow behavior (Henglai et al., 2025). 
Additionally, time-lapse (4D) seismic techniques can provide insights into pressure depletion and fluid migration 
during production or CO₂ injection (Tsakiroglou et al., 2009). Pressure transient analysis and production history 
matching are also crucial in identifying fracture -dominated flow behavior and estimating matrix –fracture 
interaction (March et al., 2018). In many carbonate reservoirs, dual -porosity behavior is inferred primarily from 
dynamic production responses, such as early -time pressure decline and delayed matrix drainage (Maulindani et 
al., 2021). However, seismic methods are generally  unable to resolve small-scale fractures and microporous 
heterogeneities that strongly influence local flow behavior (Alabere et al., 2023). Likewise, production data may 
produce non -unique interpretations because multiple fracture configurations can generate similar pressure 
responses (De Boever et al., 2016). 
 
 
Figure 4. 
Core sample photograph of a carbonate rock exhibiting multimodal pore architecture. Large vugs developed through 
dissolution processes, creating macroporosity that dominates fluid flow. Subvertical fractures cutting across the matrix, 
providing additional high-permeability pathways. Microporous matrix between vugs and fractures acting as the primary 
storage domain. This heterogeneous pore assemblage exemplifies the bimodal to multimodal pore systems that necessitate 
dual-porosity modeling approaches.

519 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Table 2. 
Comparative evaluation of characterization techniques used in dual-porosity carbonate reservoir modeling. 
Technique Main Application Major Strength Major Limitation Scale 
Neutron–Density 
Crossplot Logs 
Porosity, lithology, and 
fluid-content evaluation. 
Differentiates microporous matrix 
from macroporous fracture/vug 
zones. 
Limited direct fracture 
characterization 
capability. 
Wellbore scale 
Sonic / Full Waveform 
Acoustic Logs 
Fracture and vug detection 
through acoustic velocity 
anomalies. 
Identifies fracture corridors and 
high-permeability zones. 
Indirect interpretation is 
affected by lithological 
variability. 
Wellbore scale 
NMR Logs Pore-size distribution and 
fluid mobility analysis. 
Confirms bimodal pore systems 
and evaluates storage versus flow 
potential. 
Strong dependence on 
calibration and 
interpretation models. 
Wellbore scale 
Electrical Image Logs 
(FMI) 
Fracture density, orientation, 
aperture, and fracture-
network characterisation. 
Enables DFN calibration and 
fracture mapping near the 
wellbore. 
Limited penetration depth 
and uncertain reservoir-
scale connectivity. 
Borehole scale 
Gamma Ray Logs 
 
 
Lithology and clay-content 
identification. 
Useful for facies correlation and 
carbonate differentiation. 
Limited capability for 
direct fracture or pore-
network characterisation. 
Wellbore scale 
Routine Core Analysis 
(RCA) 
Measurement of porosity, 
permeability, and grain 
density. 
Provides baseline matrix reservoir 
properties and calibration data for 
well logs. 
Limited 
representativeness in 
highly heterogeneous 
carbonate reservoirs. 
Core scale 
Special Core Analysis 
(SCAL) 
Determination of capillary 
pressure, relative 
permeability, and 
wettability. 
Essential for multiphase flow 
simulation and matrix–fracture 
interaction analysis. 
Laboratory conditions 
may not fully represent 
in-situ reservoir behavior. 
Core scale 
Mercury Injection 
Capillary Pressure 
(MICP) 
Pore throat size distribution 
and microporosity 
characterisation. 
Effective for quantifying bimodal 
pore systems and capillary 
behavior. 
Small sample size and 
uncertainty during 
reservoir-scale upscaling. 
Pore/core scale 
Core-Based NMR Pore-size distribution, fluid 
typing, and fluid mobility 
evaluation. 
Distinguishes bound and free 
fluids and confirms dual pore 
systems. 
Indirect permeability 
estimation and calibration 
dependency. 
Core/log scale 
Tracer and Displacement 
Tests 
 
 
 
Estimation of interporosity 
transfer coefficient (α) and 
matrix block size. 
Provides empirical calibration of 
matrix–fracture exchange 
behavior. 
Difficult to scale from 
laboratory conditions to 
field-scale simulations. 
Core scale 
Digital Rock Physics 
(DRP) 
Pore-scale flow simulation 
and pore-network 
characterisation. 
Direct visualization of pore 
connectivity and fluid-flow 
pathways. 
Computationally intensive 
and difficult to upscale. 
Pore scale 
Micro-CT Imaging Three-dimensional imaging 
of pore systems and 
fractures. 
High-resolution visualization of 
pore networks and fracture 
distribution. 
Limited sample size and 
high computational 
requirements. 
Pore scale 
Petrographic Analysis Identification of pore types, 
diagenetic features, and pore 
connectivity. 
Provides detailed understanding 
of carbonate pore architecture and 
dual-porosity behavior. 
Qualitative interpretation 
and difficult quantitative 
upscaling. 
Micron/core scale 
Scanning Electron 
Microscopy (SEM) 
Visualization of 
microporosity and 
nanoporosity. 
High-resolution imaging of 
microstructural pore systems. 
Limited sample coverage 
and expensive image 
processing. 
Micron scale 
Cathodoluminescence 
(CL) 
 
 
 
Identification of diagenetic 
alteration and cementation 
patterns. 
Improves understanding of pore 
evolution and diagenetic history. 
Mainly qualitative and 
interpretation dependent. 
Thin-section scale 
Digital Image Analysis 
(DIA) 
Quantification of pore 
geometry, pore size, and 
connectivity from thin 
sections. 
Improves quantitative pore 
characterization and permeability 
correlations. 
Image segmentation 
uncertainty and limited 
field-scale representation. 
Pore/core scale 
Seismic Attribute 
Analysis / 3D Seismic 
Structural interpretation, 
fracture corridors, and 
reservoir architecture 
mapping. 
Provides reservoir-scale structural 
characterisation. 
Cannot resolve small-
scale fractures and 
microporosity. 
Reservoir scale 
Pressure Transient 
Analysis (PTA) 
Evaluation of fracture 
behavior and matrix–
fracture interaction. 
Provides dynamic evidence of 
dual-porosity flow behavior. 
Non-unique interpretation 
of fracture connectivity. 
Reservoir scale 
Production History 
Matching 
Calibration and validation 
of dual-porosity simulation 
models. 
Integrates dynamic reservoir 
behavior into model calibration. 
Strong parameter non-
uniqueness and 
calibration uncertainty. 
Field scale 
Machine Learning 
Approaches 
Prediction of porosity, 
permeability, and fracture-
related properties from 
multiscale datasets. 
Rapid integration and analysis of 
large geological and petrophysical 
datasets. 
Dependent on training-
data quality and limited 
physical interpretability. 
Multiscale

520 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
3.5 Digital rock physics and emerging characterization technologies 
Recent advances in digital rock physics (DRP), micro -computed tomography (micro -CT), and  machine 
learning have significantly advanced pore-scale characterization of carbonate reservoirs (Yan et al., 2024). Digital 
rock workflows enable detailed visualization of pore geometry, fracture connectivity, and fluid-flow pathways at 
micron-scale resolution, thereby supporting the evaluation of  multimodal pore systems and improving 
understanding of matrix–fracture interactions (Jiménez et al., 2024). Concurrently, machine learning methods are 
increasingly applied to lithofacies classification,  permeability prediction, fracture detection, and pore -network 
analysis using integrated well log and seismic datasets (Shun et al., 2020) . Although these techniques offer 
potential improvements in  automated characterization and  uncertainty reduction, digital rock physics and AI -
assisted approaches remain computationally demanding and highly dependent on data quality and 
representativeness (Yan et al., 2024) . In addition, translating pore -scale digital  observations into field -scale 
simulation parameters remains a major unresolved challenge. 
3.6 Digital challenges in multiscale data integration 
A major limitation in carbonate reservoir characterization  is the difficulty of integrating datasets acquired at 
different spatial scales into a consistent reservoir simulation framework (Barenblatt et al., 1960; De Boever et al., 
2016). Core analyses provide detailed pore -scale information, whereas well  logs and seismic data represent 
progressively larger spatial scales with lower resolution. Preserving representative matrix –fracture relationships 
during upscaling remains highly uncertain, particularly in reservoirs with strong heterogeneity and anisotro pic 
fracture systems (Rahman & Pierson 2011). Furthermore, fracture characterization adds uncertainty because fracture 
orientation, aperture, and connectivity are often inferred indirectly from limited borehole observations and seismic 
interpretation (Alabere et al., 2023; Henglai et al., 2025). This structural uncertainty can result in inaccurate static 
and dynamic geological models, which misrepresent reser voir behavior during production or CO₂ injection 
(Zambrano et al., 2021). Extensive calibration and history matching are therefore commonly required to reconcile 
geological observations with reservoir simulation results (March et al., 2018). These uncertainties directly affect 
dual-porosity model reliability because matrix permeability, fracture connectivity, and interporosity transfer behavior 
are strongly dependent on characterization accuracy (Wei et al., 2021) . Poor characterization may lead to the 
incorrect estimation of fracture conductivity, storage capacity, and sweep efficiency, ultimately reducing forecasting 
reliability and increasing uncertainty in CCS containment assessment (Fuentes-Cruz & Valko 2015; Koša 2015). 
3.7 Implications for dual-porosity and CCS modeling 
The effectiveness of dual-porosity modeling is fundamentally dependent on the quality of reservoir the ability 
to represent multiscale heterogeneity realistically. In hydrocarbon reservoirs, inaccurate fracture characterization 
can lead to unreliable production forecasts, poor sweep efficiency estimations, and incorrect pressure dep letion 
behavior (De Boever et al., 2016) . In CCS applications, this uncertainty becomes even more critical because 
fracture connectivity and caprock integrity directly influence CO₂ migration and long -term storage security 
(Tsakiroglou et al., 2009). Although integrated characterization work flows have considerably improved carbonate 
reservoir modeling considerably, substantial uncertainties remain in multiscale data integration, fracture 
representation, and pore -network upscaling. Future research should therefore focus on improving uncertainty -
aware characterization work flows, integrating digital rock physics with reservoir-scale simulation, and applying 
machine learning approaches to automated fracture and pore-system characterization (Shun et al., 2020; Yan et 
al., 2024). Additionally, coupled geological–geomechanical–reactive transport characterization frameworks will 
likely become increasingly important for reliable CCS assessments in fractured carbonate reservoirs. 
3.8 Implications of dual-porosity modeling for CCS and subsurface energy systems 
Dual-porosity modeling has become increasingly important in carbon capture and storag e (CCS) and 
subsurface energy applications because fractures and multiscale pore systems strongly influence fluid migration, 
injectivity, pressure propagation, and long-term storage behavior (Fuentes-Cruz & Valko 2015; Janjuhah & 
Alansari 2020). In carbonate reservoirs, fractures commonly provide highly conductive flow pathways, whereas

521 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
the matrix acts as the primary storage domain through capillary trapping, dissolution, and diffusion -controlled 
processes (Zampetti et al., 2004;  Xiong et al., 2025) . Accordingly, accurately rep resenting matrix –fracture 
interaction is essential for predicting CO₂ plume evolution, containment security, and reservoir performance. 
Compared with relatively homogeneous  saline aquifers, carbonate  reservoirs present substantially greater 
uncertainty due to their strong heterogeneity, anisotropic fracture systems, connected vugs, and karst features (De 
Boever et al., 2016; Jiménez et al., 2024). These characteristics create complex flow pathways that can enhance 
injectivity while simultaneously increasing uncertainty in plume migration and long -term containment behavior 
(Fuentes-Cruz & Valko 2015) . As a result, dual -porosity modeling constitutes a crit ical component of CCS 
assessment and subsurface energy system evaluation. 
• Implications for CO₂ injectivity and storage efficiency 
Fractures significantly influence CO₂ injectivity by increasing permeability and providing rapid flow pathways 
during injection (Fuentes-Cruz & Valko 2015;  Janjuhah & Alansari 20 20). In many carbonate reservoirs, 
fracture-dominated flow improves injectivity performance and facilitates pressure dissipation, making 
fractured carbonate formations attractive candidates for large -scale CO₂ storage (Tsakiroglou et al., 2009) . 
At the same time, the matrix contributes to long -term storage through capillary trapping, dissolution 
trapping, and diffusion -driven transfer of CO₂ from fractures into lower -permeability pore systems 
(Zampetti et al., 2004) . Dual-porosity and dual - permeability models are therefore widely used to evaluate 
the balance between rapid fracture flow and slower matrix -controlled storage processes (Zampetti et al., 
2004; Wei et al., 2021) . These models improve the prediction of multiphase flow behavior and pressure 
propagation compared with conventional single -porosity approaches (March et al., 2018). However, storage 
efficiency in fractured carbonate reservoirs remains highly uncertain because preferential fracture flow can 
lead to uneven sweep efficiency, rapid plume migration, and localized breakthrough behavior (De Boever 
et al., 2016) . In reservoirs with connected vuggy porosity or karst systems, classical dual -porosity 
assumptions may oversimplify fluid migration pathways and underestimate internal matrix flow (Jiménez 
et al., 2024) . Regardless, the predi ction of long -term CO₂ distribution and storage efficiency remains 
strongly dependent on fracture characterizationquality, matrix permeability estimation, and interporosity 
transfer behavior (Rahman & Pierson 2011) . 
• Fracture-controlled leakage and containment uncertainty 
Although fractures improve injectivity, they can also create preferential leakage pathways that threaten long-
term storage security (Tsakiroglou et al., 2009;  Fuentes-Cruz & Valko 2015) . Fracture connectivity, fault 
transmissibility, and caprock integrity are therefore among the primary uncertainties in carbonate CCS systems 
(Khalid et al., 2024) . In highly fractured reservoirs, interconnected fracture corridors may facilitate rapid 
vertical CO₂ migration, particularly if fractures intersect sealing formations or fault systems (Koša 2015). 
Conventional dual -porosity model s commonly simplify fracture geometry and connectivity using 
homogenised continuum representations (March et al., 2018) . While computationally efficient, these 
assumptions may inadequately represent localized leakage pathways and anisotropic fracture behavior 
(Barenblatt et al., 1960) . In addition, fracture permeability may evolve dynamica lly during CO₂ injection 
due to stress changes, geochemical reactions, and pressure buildup (Khalid et al., 2024). Many conventional 
dual-porosity formulations do not explicitly capture these coupled processes, potentially und erestimating 
long-term leakage risk. Containment uncertainty is further complicated by the difficulty of accurately 
characterizing fracture networks at the reservoir scale (Alabere et al., 2023;  Henglai et al., 2025) . Fracture 
properties derived from borehole observations and seismic interpretation are often sparse and indirect, 
making reservoir -scale fracture predictions highly uncertain (Zambrano et al., 2021) . Consequently, CO₂ 
plume migration forecasts frequently remain strongly non -unique even after extensive history matching and 
model calibration (De Boever et al., 2016) . 
• Limitations of conventional dual-porosity models for CCS applications 
Despite their widespread use, conventional dual -porosity models exhibit several limitations that affect their 
applicability to CCS systems. One major limitation is the pseudo -steady-state assumption commonly used to 
represent matrix–fracture transfer behavior (Bai et al., 1994; March et al., 2018). During CO₂ injection, transient

522 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
multiphase flow conditions often dominate fluid exchange processes, particularly in reservoirs with strong 
microporosity development or complex pore connectivity (Jiménez et al., 2024).  
Under these conditions, simplified tra nsfer formulations may inadequately represent delayed diffusion and 
capillary trapping. Another important limitation is the neglect of coupled geomechanical effects. Injection -
induced pressure changes can alter fracture aperture, permeability, and connectivity through stress-dependent 
deformation and fracture reactivation (Koša 2015; Khalid et al., 2024) . Because conventional dual -porosity 
models frequently assume static fracture properties, they ris k oversimplifying permeability evolution and 
containment behavior during long-term storage operations (Fuentes-Cruz & Valko 2015). 
Reactive transport processes also introduce additional uncertainty. CO₂ interaction with  carbonate minerals 
may lead to dissolution, precipitation, and porosity alteration that progressively modify flow behavior and 
storage capacity (Moonen & Carmeliet 2013). However, many conventional dual-porosity formulations do not 
explicitly incorporate these geochemical reactions or dynamically evolving pore structures (Koša 2015). As a 
result, long-term predictions of injectivity, plume migration, and storage security often remain uncertain. 
Furthermore, in reservoirs containing multimodal pore systems, binary  matrix–fracture representations may 
further oversimplify carbonate heterogeneity (De Boever et al., 2016; Jiménez et al., 2024). Micropores, vugs, 
fractures, and karst conduits often coexist within the same reservoir interval and may contribute differently to 
flow and storage processes (Moldabayeva et al., 2025). As a result, more advanced approaches such as MINC, 
DFN, and hybrid continuum –discrete models are increasingly needed to better represent complex carbonate 
systems (Barenblatt et al., 1960; Makhankova et al., 2021). 
• Implications for other subsurface energy systems 
Beyond CCS applications, dual-porosity modeling also plays an important role in geothermal energy systems, 
underground gas storage, hydrogen storage, and enhanced oil recovery (EOR) operations (Tsakiroglou et al., 
2009; Janjuhah & Alansari 2020) . In geothermal reservoirs, fractures commonly dominate heat transfer and 
fluid circulation, while matrix diffusion controls long-term thermal recovery behavior (Fuentes-Cruz & Valko 
2015). Accurate representation of fracture connectivity is therefore essential for predicting thermal 
breakthrough and reservoir sustainability. Similarly, hydrogen s torage in depleted carbonate reservoirs and 
saline formations requires reliable modeling of gas migration, containment behavior, and cyclic pressure 
effects (Tsakiroglou et al., 2009) . Although fracture -controlled flow pa thways can improve injectivity and 
deliverability, they can also simultaneously increase uncertainty in gas containment and caprock integrity 
(Khalid et al., 2024). Similar challenges occur in underground gas storage systems, where repeated injection 
and withdrawal cycles may alter stress conditions and fracture permeability over time. In CO₂ -enhanced oil 
recovery (CO₂-EOR) operations, dual-porosity behavior strongly influences sweep efficiency, breakthrough 
timing, and matrix–fracture transfer processes (Zampetti et al., 2004). Fracture-dominated flow can improve 
injectivity but may also cause early gas breakthrough and reduced recovery efficiency if fracture connectivity 
is poorly characterized (De Boever et al., 2016) . Ultimately, the reliable modeling of matrix –fracture 
interaction remains essential across a broad range of subsurface energy applications. 
• Emerging directions and future challenges 
Recent advances in machine learning, digital rock physics, and coupled multiphysics simulation have 
significantly enhanced the ability to model complex carbonate reservoirs and CCS systems (Shun et al., 2020; 
Yan et al., 2024) . Machine learning approaches are increasingly used for fracture characterization, 
permeability prediction, uncertainty quantification, and surrogate modeling, offering substantial reductions in 
computational cost and simulation runtime (Shun et al., 2020). 
Coupled thermal –hydraulic–mechanical–chemical (THMC) modeling frameworks are also becoming 
increasingly important for CCS applications because they simultaneously evaluate multiphase flow, 
geomechanical deformation, fracture evolution, and reactive transport processes (Chang et al., 2026) . 
Although these approaches provide a more realistic representation of long -term reservoir behavior, they 
remain computationally demanding and highly dependent on data availability. 
Concurrently, digital rock physics and micro -CT imaging are further improving pore -scale understanding of 
matrix–fracture interaction and multimodal pore connectivity (Jiménez et al., 2024;  Yan et al., 2024) .

523 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Nevertheless, significant challenges remain when integrating these pore -scale observations into field -scale 
simulation workflows. Specifically, uncertainties in fracture characterization, scale depe ndency, and 
parameter non-uniqueness continue to limit predictive reliability in both carbonate CCS systems  and broader 
subsurface energy applications. Ultimately, the reviewed literature demonstrates that dual-porosity modeling 
provides a foundational framework for evaluating fractured carbonate reservoirs  in CCS and subsurface 
energy systems. However, substantial uncertainty remains regarding fracture connectivity, coupled physical 
processes, multiscale h eterogeneity, and long -term storage behavior.  Future developments must therefore 
prioritise a  tighter integration  of geological characterization, coupled multiphysics modeling, uncertainty 
quantification, and computationally efficient simulation workflows that can balance geological realism with 
field-scale practicality. 
 
Table 3.  
Critical Implications and Uncertainties of Dual-porosity Behavior in Carbonate CCS Systems. 
CCS Aspect Role of Dual-porosity Behavior Major Challenge Main Uncertainty 
CO₂ Injectivity Fractures enhance injectivity and 
pressure dissipation, while the 
matrix contributes to storage 
capacity. 
Preferential fracture flow may 
reduce sweep efficiency and 
create uneven plume distribution. 
Fracture connectivity and 
permeability anisotropy. 
CO₂ Plume 
Migration 
Matrix–fracture interaction 
controls short-term fracture flow 
and long-term matrix diffusion. 
Rapid fracture-controlled 
migration may reduce 
predictability of plume evolution. 
Interporosity transfer behavior 
and fracture-network 
continuity. 
Storage Efficiency Matrix porosity contributes to 
capillary trapping, dissolution 
trapping, and long-term CO₂ 
retention. 
Heterogeneous pore systems may 
produce inefficient sweep and 
bypassed storage zones. 
Matrix permeability 
distribution and multimodal 
pore connectivity. 
Containment 
Security 
Fractures and faults strongly 
influence leakage potential and 
caprock integrity. 
Connected fracture corridors may 
create preferential leakage 
pathways. 
Fault transmissibility, fracture 
reactivation, and caprock 
integrity. 
Pressure 
Evolution 
Fracture systems control pressure 
propagation and dissipation 
during injection. 
Pressure buildup may alter 
fracture permeability and induce 
geomechanical instability. 
Stress-dependent fracture 
behavior and reservoir 
compressibility. 
Reactive 
Transport 
Processes 
CO₂–brine–rock interaction 
influences porosity evolution and 
long-term storage behavior. 
Mineral dissolution and 
precipitation may alter 
permeability and flow pathways. 
Geochemical reaction kinetics 
and coupled THMC behavior. 
History Matching 
and Forecasting 
Dual-porosity models improve 
simulation of fracture-dominated 
flow and delayed matrix 
drainage. 
Multiple parameter combinations 
may produce similar simulation 
results. 
Parameter non-uniqueness and 
multiscale heterogeneity. 
Long-Term 
Storage 
Assessment 
Matrix diffusion and residual 
trapping improve long-term 
containment potential. 
Long-term prediction reliability 
decreases with increasing 
geological complexity. 
Fracture evolution, uncertainty 
propagation, and coupled 
physical processes. 
 
 
3.9 Comparative analysis of dual-porosity modeling applications in carbonate reservoirs 
Field-scale case studies provide important validation  for dual -porosity modeling approaches because they 
demonstrate how matrix–fracture interactions influence reservoir behavior under realistic geological conditions. 
In carbonate reservoirs, strong multiscale heterogeneity commonly involves fractures, vugs, microporosity, and 
karst systems that evolve through complex depositional and diagenetic processes (Janjuhah et al., 2019; Malki et 
al., 2023) . As such, field applications are essential for evalu ating the practical reliability, uncertainty, and 
limitations of dual-porosity workflows in both hydrocarbon production  and carbon capture and storage (CCS)

524 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
applications. The reviewed case studies from Central Luconia and Abu Dhabi collectively demonstrate that the 
interaction between matrix storage and fracture-dominated flow pathways strongly controls carbonate reservoir 
performance. They further show that successful modeling depends heavily on fracture characterization, pore -
system evaluation, and appropriate model selection based on reservoir heterogeneity. 
3.10 Central luconia carbonate reservoirs 
The Central Luconia Province offshore Sarawak represents one of the most important carbonate provinces in 
Southeast Asia and serves as a major reference system for evaluating dual-porosity behavior in Miocene carbonate 
reservoirs (Koša 2015; Koša et al., 2015;  Ismail et al., 2026) . In this region, extensive carbonate  build-ups are 
characterized by strong facies heterogeneity, microporosity development, fractures, dissolution features, and 
localized karst systems (Jamaludin et al., 2021;  Jiménez et al., 20 24; Henglai et al., 2025)  (Figure 5). These 
geological characteristics create highly heterogeneous pore systems that strongly influence permeability  
distribution, storage behavior, and fluid-flow dynamics. 
• Multimodal pore systems and matrix–fracture partitioning 
Petrographic and petrophysical studies from Central Luconia demonstrate that microporosity contributes 
significantly to total reservoir storage, particularly within mud-dominated carbonate facies (Rahman & Pierson 
2011; Janjuhah et al., 2019). Specifically, Janjuhah et al. (2019) conducted a detailed petrographic 
investigation using enhanced Digital Image Analysis (DIA) workflows to quantify microporosity development 
in Miocene carbonates from Central Luconia. Their results revealed that microporosity commonly accounts 
for 20% to 60% of total porosity, with moldic porosity representing the dominant pore type, followed by 
vuggy, intraparticle, interparticle, and fracture -related porosity. Furthermore, the study demonstrated that 
explicitly separating microporosity and macroporosity significantly improved prediction o f acoustic velocity 
and permeability behavior compared with conventional total -porosity approaches (Janjuhah et al., 2019) . 
These findings confirm that carbonate reservoirs in Central Luconia cannot be adequately represented  using 
homogeneous single-porosity assumptions because storage and flow are controlled by fundamentally different 
pore domains. In addition, the coexistence of low-permeability matrix microporosity and highly conductive 
fracture–vug systems creates charact eristic dual -porosity flow behavior: rapid early -stage fracture flow is 
followed by slower matrix drainage during later production stages (March et al., 2018; Egya et al., 2019). As 
a result, matrix–fracture partitioning plays a critical role in controlling production performance, pressure 
propagation, and reservoir forecasting reliability. 
• Evaluation of modeling approaches in central luconia 
Several studies from Central Luconia highlight the importance of selecting modeling approaches based on 
reservoir heterogeneity  and fracture complexity. Conventional dual -porosity models generally perform 
reasonably well in fracture-dominated carbonate systems where fractures provide the primary flow pathways 
and the matrix mainly acts as a storage medium (Warren & Root  1963; March et al., 2018) . However, in 
reservoirs with connected karst systems or highly heterogeneous vuggy porosity, classical dual -porosity 
assumptions become increasingly inadequate (Jiménez et al., 2024) . To address these limitations, Trianto et 
al. (2026) applied a hybrid modeling workflow combining conventional carbonate matrix models with three -
dimensional karst networks using Discrete Fracture Network (DFN) techniques in the JTN Carbonate Field, 
Central Luconia. Their workflow integrated seismic interpretation, core analysis, and petrophysical logs to 
construct a geological model that explicitly represents matrix –karst interactions and fluid -flow uncertainty 
under different karst-fill scenarios. 
The study demonstrated that explicitly representing karst connectivity improved reproduction of production 
heterogeneity and dynamic flow behavior compared with simplified continuum approaches (Trianto et al., 
2026). These findings indicate t hat model reliability decreases substantially when reservoirs contain 
deterministic heterogeneity, such as connected vugs, fracture corridors, or karst conduits, because simplified 
matrix–fracture assumptions cannot adequately represent them. Therefore, hi ghly heterogeneous carbonate 
reservoirs require advanced workflows incorporating DFN or hybrid continuum–discrete approaches, despite 
their greater computational cost and calibration complexity (Cordero et al., 2019; Zambrano et al., 2021).

525 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Figure 6 summarizes the key dual-porosity model results from Central Luconia, illustrating (a) the partitioning 
of porosity between matrix microporosity and fracture/vug macroporosi ty across multiple fields, (b) the 
distribution of pore types as quantified from detailed petrographic analyses, and (c –d) the improvements in 
velocity and permeability prediction correlations achieved through dual -porosity parameterisation. 
Collectively, these studies demonstrate that dual -porosity workflows significantly improve reservoir 
characterisation, permeability prediction, and history matching compared with conventional  single-porosity 
approaches (Janjuhah et al., 2019; Jiménez et al., 2024; Trianto et al., 2026). 
• Implications for CCS applications 
The Central Luconia case studies also provide important implications for CCS because the same fracture 
systems that enhance hydrocarbon productivity may strongly influence CO₂ injectivity,  migration, and 
containment behavior (March et al., 2018;  Xiong et al., 2025) . While fracture networks improve injectivity 
and pressure dissipation, matrix microporosity contributes to long -term CO₂ trapping through diffusion -
controlled transfer and capillary storage processes. However, these studies also highlight substantial 
uncertainty related to fracture connectivity and interporosity transfer behavior (Egya et al., 2019). In reservoirs 
with highly conductive karst pathways or anisotropic fracture corridors, preferential CO₂ migration can reduce 
storage predictability and increase containment uncertainty. Consequently, these observations emphasize the 
importance of fracture characterization and uncertainty -aware modeling workflows for reliable CCS 
forecasting in fractured carbonate reservoirs. 
 
 
 
Figure 5.  
Geographical location of the Central Luconia geological province and surrounding area in offshore Sarawak, Malaysia. The map 
shows the distribution of Miocene carbonate build-ups (shaded polygons) relative to major structural elements, shelf margins, 
and adjacent basinal areas. The study area represents the largest gas-producing carbonate province in Southeast Asia, providing 
an excellent natural laboratory for evaluating dual-porosity behavior in heterogeneous carbonate systems.  
Modified from Jamaludin et al. (2021).

526 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
 
Figure 6.  
Dual-porosity model results from Central Luconia carbonate reservoirs. (a) Porosity partitioning showing matrix 
microporosity versus fracture/vug macroporosity across different fields, illustrating the bimodal storage-flow architecture. 
(b) Pore type distribution from petrographic analysis of Well A (Miocene Cycle V), quantifying the relative abundance of 
moldic, vuggy, intraparticle, interparticle, and fracture porosity. (c) Velocity prediction improvement using microporosity-
based dual-porosity approach (R² improved from 0.61 to 0.87), demonstrating the importance of separating microporous and 
macroporous domains for acoustic property estimation. (d) Permeability prediction improvement using macroporosity-based 
dual-porosity approach (R² improved from 0.55 to 0.67), confirming that explicit macroporosity characterizationenhances 
flow property prediction. Data compiled from Janjuhah et al. (2019), Jiménez et al. (2024), and Trianto et al. (2026). 
 
3.11 Global analogue: Abu Dhabi carbonate reservoirs 
The Lower Cretaceous carbonate reservoirs of Abu Dhabi provide an important analogue for evaluating dual-
porosity behavior in heterogeneous carbonate systems (Alabere et al., 2023;  2025). Like C entral Luconia, these 
reservoirs exhibit strong multiscale heterogeneity controlled by depositional facies, micritisation, dissolution, 
stylolites, fractures, and vug development (Ehrenberg 2018; Alabere et al., 2023). Figure 7 illustrates the workflow 
for developing a dual-porosity model in an Abu Dhabi carbonate reservoir. Petrographic and digital rock studies 
from Abu Dhabi demonstrate that dual-porosity architecture is strongly facies-dependent (Alabere et al., 2023; 2025). 
Grain-dominated facies, such as grainstones and rudstones, commonly exhibit bimodal pore systems involving both 
intergranular macropores and microporosity, whereas mud-dominated facies are typically characterized by isolated 
micropores and fracture-dominated permeability (Alabere et al., 2023). These findings reinforce the conclusion that 
pore connectivity and flow behavior in carbonate reservoirs are highly sensitive to depositional textures and 
diagenetic evolution. Furthermore, imaging studies have revealed that pore-throat distributions become increasingly 
complex at higher imaging resolutions, highlig hting the scale dependency of carbonate pore characterization                
(Jouini et al., 2023; Alabere et al., 2025). 
Studies from Abu Dhabi also demonstrate that microporosity strongly influences resistivity behavior in low -
resistivity carbonate intervals, whereas macroporosity exhibits a weaker correlation with the resistivity response 
(Alabere et al., 2023; 2025). This finding highlights a key challenge in carbonate reservoir characterization because 
conventional petrophysical interpretations may underestimate productive intervals if dual-porosity behavior is not 
explicitly considered. The Abu Dhabi analogue therefore reinforces observations from Central Luconia indicating 
that depositional fabrics, diagenetic overprinting, and multimodal pore systems must be explicitly integrated into 
dual-porosity workflows for reliable flow simulation and reservoir characterization.

527 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
 
Figure 7.  
Workflow for dual-porosity model development in Abu Dhabi Lower Cretaceous carbonate reservoirs. The workflow 
progresses from core plug selection and petrographic facies identification, through digital rock physics analysis and pore-
network extraction, to upscaling of dual-porosity parameters for reservoir simulation. Key steps include thin-section 
petrography, SEM imaging, MICP analysis, micro-CT scanning, and permeability simulation, culminating in calibrated 
matrix–fracture transfer functions. Modified from Alabere et al. (2023). 
 
 
3.12 Comparative evaluation of case study findings 
The reviewed case studies collectively demonstrate that dual -porosity modelling substantially improves 
conventional single-porosity approaches for heterogeneous carbonate reservoirs. Across both the Central Luconia 
and Abu Dhabi systems, dual -porosity work flows improve the characterisation of multiscale pore systems, 
permeability prediction, and dynamic reservoir behaviour by explicitly separating matrix storage from fracture -
dominated flow pathways (March et al., 2018; Janjuhah et al., 2019; Alabere et al., 2023). Nevertheless, the studies 
also reveal several recurring limitations. First, model reliability remains strongly dependent on fracture 
characterisation quality, as fracture connectivity exerts a major control on flow behaviour, pressure propagation, 
and injectivity (Berkowitz 2002; Egya et al., 2019) . As such, sparse fracture observations and scale -dependent 
heterogeneity frequently produce non -unique interpretations during history -matching and uncertainty analysis. 
Second, conventional binary matrix –fracture representations often oversimplify multimodal carbonate pore 
systems (Zambrano et al., 2021; Jiménez et al., 2024). In reservoirs containing connected vugs, karst features, or 
extensive microporosity development, advanced approaches such as dual permeability, DFN, MINC, or hybrid

528 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
continuum–discrete workflows generally provide more realistic simulation behaviour than classical dual-porosity 
models (Nguyen et al., 2018;  Cordero et al., 2019) . Third, these reviewed case studies d emonstrate a persistent 
trade-off between geological realism and computational practicality. Advanced workflows incorporating DFN 
and hybrid approaches improve the fracture -geometry representation and localised flow pathways but require 
significantly greater computational resources and more detailed characterisation datasets (Zambrano et al., 2021). 
Dual-porosity models are particularly effective in highly fractured carbonate reservoirs. For instance, Putra et al. 
(2026) demonstrated through seismic inversion in the Natuna Basin that separating matrix storage from fracture 
flow pathways provides more realistic reservoir characterization, directly supporting dual -porosity modelling 
assumptions. Therefore, selecting an appropriate modelling approach remains strongly dependent on reservoir 
complexity, data availability, and simulation objectives. The reviewed field applications demonstrate that no 
single modelling framework is universally applicable to  all carbonate reservoirs. Instead, effective simulation 
requires workflows capable of integrating multiscale geological characterisation, petrophysical analysis, fracture-
network evaluation, and uncertainty-aware dynamic calibration within reservoir-specific modelling frameworks. 
3.13 Challenges and future research directions in dual-porosity                                                                   
modeling for carbonate reservoirs and CCS systems 
Despite major advances in carbonate reservoir characterization and dual -porosity simulation, significant 
challenges remain in accurately representing the complex interactions among matrix storage, fracture -controlled 
flow, and multiscale heterogeneity (De Boever et al., 2016;  Jiménez et al., 2024) . Carbonate reservoirs 
commonly feature highly heterogeneous pore architectures involving fractures,  vugs, micropores, and karst 
systems that evolve ac ross multiple spatial scales and strongly influence fluid -flow behavior (Janjuhah et al., 
2019; Henglai et al., 2025) . As a result, these complexities introduce substantial uncertainty into res ervoir 
characterisation, permeability prediction, history matching, and long -term forecasting for both hydrocarbon 
production and CCS applications. The reviewed literature demonstrates that, although dual -porosity modeling 
remains a widely applied  approach for fractured carbonate systems, no single modeling framework is universally 
applicable to all carbonate reservoirs. Instead, model performance depends strongly on fracture characterization 
quality, pore -system complexity, data integration strategy, and s imulation objectives. Future research must 
therefore focus on reducing uncertainty, improving multiscale integration, and developing more physically 
realistic and computationally efficient simulation frameworks. 
• Fracture characterizationand connectivity uncertainty 
One of the largest unresolved challenges in carbonate reservoir simulation is the accurate characterization of 
fracture networks and connectivity (Berkowitz 2002;  Egya et al., 2019) . Fractures commonly dominate 
permeability and fluid migration in carbonate reservoirs; however, fracture  properties are typically inferred 
indirectly from limited datasets such as cores, borehole image logs, seismic interpretation, and production 
responses (Alabere et al., 2023; Henglai et al., 2025). Because these datasets often provide localized or low-
resolution information, reservoir -scale prediction of fracture continuity and connectivity remains highly 
uncertain. In many carbonate reservoirs, fracture corridors, karst conduits, and fault -associated fracture 
systems create strongly anisotropic flow behavior that simplified continuum assumptions cannot adequately 
represent (Zambrano et al., 2021; Jiménez et al., 2024). Consequently, uncertainty in fracture geometry often 
propagates into pressure predictions, sweep efficiency estimations, and CO₂ plume migration forecasts (March 
et al., 2018). Although Discrete Fracture Network (DFN) and hybrid continuum–discrete approaches improve 
fracture realism, their computational expense and strong dependence on detailed fracture characterization 
datasets (Nguyen et al., 2018)  remain a challenge. Future research should therefore focus on in tegrating 
multiscale fracture characterization techniques, combining seismic interpretation, digital rock analysis, high -
resolution imaging, and uncertainty-aware modeling workflows. Automated fracture extraction and machine 
learning-assisted fracture identification may also improve characterization efficiency and reduce interpretation 
uncertainty in highly heterogeneous carbonate systems (Shun et al., 2020; Yan et al., 2024). 
• Challenges in multiscale pore-system representation 
Conventional dual-porosity models are fundamentally based on binary separation between matrix storage and 
fracture flow (Warren & Root 1963;  March et al., 2018 ). However, many carbonate  reservoirs exhibit far

529 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
more complex pore architectures with micropores, vugs, interparticle pores, fractures, and karst systems 
coexisting within the same reservoir interval (Janjuhah et al., 2019; Jiménez et al., 2024). These multimodal 
pore systems often display strong facies dependence and scale-dependent connectivity that simplified matrix–
fracture assumptions cannot adequately represent. Microporosity presents a p articularly important challenge 
because it contributes significantly to storage capacity while exhibiting extremely low permeability and 
delayed fluid-transfer behavior (Rahman & Pierson 2011; Janjuhah et al., 2019). Similarly, connected vuggy 
porosity and karst conduits may contribute directly to flow behavior rather than acting purely as storage 
domains (Jiménez et al., 2024). As a result, classical dual-porosity models may oversimplify internal matrix 
flow and underestimate preferential flow  pathways in highly heterogeneous carbonate systems. Future 
developments should therefore focus on advanced multiscale modeling approaches capable of re presenting 
dynamically connected pore systems more realistically. Hybrid workflows combining dual -porosity, dual -
permeability, MINC, DFN, and digital rock physics may provide improved representation of multiscale 
carbonate heterogeneity (Nguyen et al., 2018;  Cordero et al., 2019;  Makhankova et al., 2021) . However, 
balancing geological realism with computational practicality remains a major challenge, especially fo r full-
field applications with limited computational resources. 
• Interporosity transfer and history matching uncertainty 
The interporosity transfer coefficient ( α) remains among the most uncertain parameters in dual -porosity 
simulation because it controls fluid exchange between the matrix and fracture domains (Rahman & Pierson 
2011; Wei et al., 2021). Although α can be estimated using laboratory measurements, analytical solutions, or 
history matching, it cannot be directly measured at the reservoir scale. Consequently, multiple parameter 
combinations may reproduce similar production behavior, creating significant non -uniqueness during model 
calibration (De Boever et al., 2016) . This uncertainty becomes particularly severe in reservoirs containing 
multimodal pore systems or complex  fracture connectivity because matrix –fracture interaction may vary 
spatially and temporally throughout the reservoir (Jiménez et al., 2024). In addition, simplified pseudo-steady-
state transfer assumptions commonly used in conventional dual-porosity formulations may also inadequately 
represent transient flow conditions during CO₂ injection and long -term matrix drainage (March et al., 2018). 
Future research may benefit from developing more physically representative transfer functions that incorporate 
pore geometry, wet ability, capillary forces, and dynamically evolving fracture behavior. Machine learning 
approaches may additionally improve history matching efficiency, surrogate modeling, and uncert ainty 
quantification during large-scale reservoir calibration workflows (Shun et al., 2020). 
Computational challenges and advanced simulation workflows increasing geological realism generally comes 
at the expense of computation al efficiency. Advanced simulation approaches such as DFN, MINC, and 
coupled multiphysics models require high -resolution gridding, large computational resources, and complex 
numerical coupling schemes (Nguyen et al., 2018;  Alabere et al., 2025) . These requirements often limit the 
practical feasibility of uncertainty quantification, probabilistic forecasting, and large-scale field simulation in 
routine commercial workflows. Although hybrid continuu m–discrete workflows better represent fracture -
controlled flow behavior, they introduce additional challenges related to fracture upscaling, grid refinement, 
and numerical convergence (Zambrano et al., 2021) . Furthermore, co upling geological characterization, 
geomechanics, reactive transport, and multiphase flow within a unified simulation framework remains 
computationally demanding, particularly for long -term CCS forecasting. Future developments should 
therefore prioritize reduced-order modeling, surrogate simulation methods, and high-performance computing 
techniques that improve simulation efficiency while preserving geological realism. Integration of machine 
learning approaches with conventional physics -based workflows may further improve computational 
scalability and reservoir forecasting capability, particularly for uncertainty quantification, history matching, 
and long-term CCS risk forecasting (Shun et al., 2020; Yan et al., 2024). 
Challenges in CCS Forecasting and Long-Term Containment Assessment Carbon, capture, and storage (CCS) 
applications introduce additional complexities beyond conventional hydrocarbon reservoir simulation because 
long-term storage security depends strongly on fracture behavior, caprock integrity, reactive transport 
processes, and pressure evolution (Fuentes-Cruz & Valko 2015;  Xiong et al., 2025) . In fractured carbonate 
reservoirs, fractures improve CO₂ injectivity and pressure dissipation but may simultaneously create

530 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
preferential leakage pathways that are difficult to characterize and predict (Khalid et al., 2024) . Many 
conventional dual -porosity workflows only partially incorporate coupled thermal –hydraulic–mechanical–
chemical (THMC) processes, and even when THMC models are applied, their implementation is often limited 
to research -scale studies rather than routine field -scale commercial workflow s (Chang et al., 2026) . To 
improve practical CCS forecasting, these THMC models should be linked with 4D seismic monitoring, 
pressure data, tracer tests, and history -matched plume observations to validate  long-term containment 
predictions. Future research should also focus on developing reduced- order THMC models that balance 
physical realism with computational tractability for probabilistic CCS risk assessment.  Merging Research 
Directions Recent advances in digital rock physics, micro-CT imaging, artificial intelligence, and uncertainty-
aware simulation workflows are significantly enhancing the future of carbonate reservoir modeling (Shun et 
al., 2020; Yan et al., 2024; Alabere et al., 2025). Three priority areas stand out for near-term research. 
First, digital rock approaches now provide increasingly detailed visualisation of pore connectivity and fluid -
flow pathways at micron-scale resolution, which improve the understanding of matrix–fracture interaction and 
multimodal pore behavior (Alabere et al., 2025). However, the primary unsolved challenge remains upscaling 
these pore-scale observations to field -scale dual-porosity parameters in a  way that preserves representative 
connectivity, relative permeability functions, and flow behavior across scales. Bridging this gap requires the 
systematic development of upscaling workflows that integrate  digital rock physics wi th reservoir -scale 
simulation grids while honoring geological heterogeneity. 
Second, machine learning methods are increasingly applied to fracture detection, permeability prediction, 
lithofacies classification, automated history matching, and surrogate mod eling (Shun et al., 2020) . These 
approaches offer potential improvements in computational efficiency and uncertainty quantification, particularly 
when integrated with conventional physics-based simulation workflows. However, their success depends heavily 
on training-data quality, feature engineering, and the physical interpretability of the results. Future work should 
focus on hybrid physics -informed neural networks that embed conservation laws directly into the learning 
architecture, thereby improving generalisability beyond the training dataset. 
Third, an important emerging direction involves the development  of adaptive  and continuously  updated 
reservoir modeling workflows capable of incorporating newly acquired geological and dynamic reservoir data 
during production or CO₂ injection operations sometimes referred to as closed-loop reservoir modeling or data 
assimilation. In such workflows, static geological models are dynamically updated with real -time pressure, 
saturation, and 4D seismic data to reduce forecast uncertainty progressively. This approach is particularly 
promising for long-term CCS operations, where monitoring data accumulate over decades and can be used to 
refine containment risk assessments iteratively. Ultimately , future progress in dual -porosity modeling will 
likely depend on tighter integration of multiscale characterization, uncertainty -aware workflows, coupled 
multiphysics simulation, and computationally efficient modeling strategies capable of balancing geolo gical 
realism with practical field-scale implementation. 
 
4. Conclusion 
This review critically evaluated the characterization techniques, modeling approaches, integrated workflows, 
and field-scale applications of dual-porosity modeling in carbonate reservoirs, with particular emphasis on carbon 
capture and storage (CCS). As a foundation, the synthesis confirms that carbonate reservoirs remain among the 
most difficult geological systems to characterize and simulate because they exhibit multiscale heterogeneity 
spanning from tiny micropores to large fractures, vugs, and karst conduits. This complex coexistence of variable 
pore and fracture geometries governs fluid exchange between the matrix and fracture domains, as well as 
permeability distributions, fluid migration pathways, and long-term reservoir behavior. Regarding the current state 
of knowledge, dual -porosity modeling remains the most widely adopted framework for fracture -dominated 
carbonate flow, yet the reviewed literature exposes several unresolved contradictions. Conventional dual-porosity 
and dual-permeability models are computationally efficient and reproduce fracture-controlled behavior in systems 
where the matrix acts mainly as a storage domain; however, they become physically inadequate in reservoirs with 
connected vugs, karst networks, or multimodal pore structures. Although advanced formulations such as dual -

531 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
permeability, MINC, DFN, and hybrid continuum–discrete workflows improve geological realism, the literature 
remains divided regarding the optim al balance among accuracy, data demands, and computational tractability. 
While the Warren -Root model has been successfully implemented in modern commercial fluid flow reservoir 
simulators, the implementation of DFN and MINC approaches in future commercial simulators remains an active 
area of development. Several commercial platforms have begun incorporating DFN modules, and MINC -type 
approaches are available in research simulators, suggesting a trajectory toward greater adoption as computational 
capabilities improve. 
Because greater fracture explicitness raises computational costs and parameter non -uniqueness, no single  
framework is universally applicable, and this tension between representational fidelity and practical solvability 
remains the central unresolved debate in the field. 
Several gaps consistently emerged across the reviewed studies and the Central Luconia and Abu Dhabi case 
analyses. Matrix–fracture transfer functions remain poorly constrained and are frequently calibrated non-uniquely 
through history -matching. Fracture connectivity and multimodal pore partitioning are also inconsistently 
characterized across scales, and workflows integrating static geological descriptions with dynamic simulations 
are still immature. For CCS specifically, the  dual role of fractures —which enhance CO₂ injectivity but amplify 
uncertainty in plume migration and long -term containment —has not been resolved within conventional dual -
porosity assumptions, and long-term coupled trapping mechanisms remain insufficiently validated against field-
scale monitoring data. 
Methodologically, the review identified core and petrophysical analyses, well -log and borehole -imaging 
interpretations, seismic and dynamic (pressure-transient) characterisation, and digital rock physics as the principal 
techniques underpinning dual -porosity workflows. Although each method  resolves heterogeneity at a distinct 
scale, they are seldom integrated coherently. Future progress will therefore  depend on a  tighter multiscale 
integration of these techniques with digital rock physics, machine learning-assisted characterization and history 
matching, formal uncertainty quantification, and coupled thermal –hydraulic–mechanical–chemical (THMC) 
simulations capable of balancing geological realism with field -scale practicality. Ultimately, prioritising 
uncertainty-aware, data-integrated workflows over single-continuum idealisations offers the most promising path 
toward reliable forecasting for both hydrocarbon recovery and secure CO₂ storage in carbonate reservoirs. 
 
5. Acknowledgement 
The authors are grateful to the Department of Geoscience Universiti Teknologi PETRONAS for supporting 
this research. 
 
6. Declarations 
6.1 Author contributions 
Khalisha Shafa Yumnanisa: Conceptualization, methodology, investigation, writing – original draft, 
visualization. Siti Nur Fathiyah Jamaludin: Supervision, conceptualization, writing – review and editing, funding 
acquisition. Numair Ahmed Siddiqui: Writing – review and editing, validation. Jun Matsushima: Writing – review 
and editing, resources. Alidu Rashid: Writing – review and editing, resources. Jamaluddin: Writing – review and 
editing, resources. The authors declare that this manuscript is original, has not been published previously, and is not 
under consideration for publication elsewhere. All authors have approved the final version of this manuscript and 
agree to its submission to Scientific Contributions Oil and Gas (SCOG). 
6.2 Funding statement 
This research was supported by Universiti Teknologi PETRONAS (UTP) through the Ya yasan Universiti 
Teknologi PETRONAS (YUTP) research grant.

532 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
6.3 Competing interest 
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper. 
6.4 The use of AI or AI-assisted technologies 
During the preparation of this work, the authors used generative AI tools for language editing, grammar 
checking, and structural formatting assistance. After using these tools, the authors reviewed and edited the content 
as needed and take full responsibility for the content of the publication. 
 
7. Glossary of terms and symbols 
Terms & Symbol Definition Unit 
α (alpha) Interporosity transfer coefficient governing fluid exchange between matrix and fracture 
domains [m⁻²] 
- 
Bimodal pore system Reservoir pore architecture characterized by two distinct populations of pore sizes (typically 
micropores and macropores/vugs) 
- 
Capillary trapping Mechanism by which CO₂ is immobilized in pore spaces by capillary forces during 
multiphase flow 
- 
CCS Carbon Capture and Storage; the process of capturing CO₂ emissions and storing them in 
subsurface geological formations 
- 
DFN Discrete Fracture Network; a modeling approach representing individual fractures as explicit 
geometric features 
- 
Diagenesis Post-depositional chemical and physical processes that modify sedimentary rocks, including 
dissolution, cementation, and dolomitization 
- 
DIA Digital Image Analysis; computational technique for quantifying pore geometry and 
connectivity from thin-section images 
- 
Dissolution trapping Long-term CO₂ storage mechanism involving dissolution of CO₂ into formation brine - 
DPM Dual-Permeability Model; formulation allowing simultaneous Darcy flow in both matrix and 
fracture continua 
- 
DRP Digital Rock Physics; computational methods simulating fluid flow and transport properties 
on digital representations of rock microstructure 
- 
EOR Enhanced Oil Recovery; techniques used to increase the amount of crude oil extracted from 
reservoirs 
- 
FMI Formation MicroImager; borehole logging tool providing high-resolution electrical images 
of the borehole wall 
- 
Full-field simulation Reservoir simulation covering the entire producing area rather than a sector or pattern - 
History matching Process of adjusting reservoir model parameters until simulated production behavior matches 
observed field data 
- 
Homogenization Upscaling approach averaging small-scale heterogeneities into effective continuum 
properties 
- 
Hybrid model Simulation framework combining continuum dual-porosity formulations with explicit 
discrete fracture representations 
- 
Interporosity flow Fluid transfer between matrix and fracture pore systems - 
Karst Terrain characterized by dissolution features such as caves, conduits, and vugs formed by 
chemical weathering of carbonate rocks 
- 
MICP Mercury Injection Capillary Pressure; laboratory technique measuring pore throat size 
distribution 
- 
MICP Mercury Injection Capillary Pressure; laboratory technique for measuring pore throat size 
distribution and capillary entry pressure 
- 
MINC Multiple Interacting Continua; method subdividing matrix blocks into nested shells to 
capture transient exchange behavior 
- 
NMR Nuclear Magnetic Resonance; logging and laboratory technique for evaluating pore-size 
distribution and fluid properties 
- 
Non-uniqueness Condition where multiple combinations of model parameters produce equally acceptable 
simulation results 
- 
Pseudo-steady-state Assumption that matrix–fracture transfer rate is proportional to the instantaneous pressure 
difference between domains 
- 
PTA Pressure Transient Analysis; interpretation of pressure build-up or draw-down data to infer 
reservoir properties 
-

533 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
RCAL / RCA Routine Core Analysis; standard laboratory measurements of porosity, permeability, and 
grain density on core plugs 
- 
REV Representative Elementary V olume; smallest volume over which a measurement can be 
made that yields a value representative of the whole 
- 
SCAL Special Core Analysis; advanced laboratory measurements including relative permeability, 
capillary pressure, and wettability 
- 
THMC Thermal–Hydraulic–Mechanical–Chemical; coupled multiphysics framework incorporating 
heat transfer, fluid flow, geomechanics, and geochemistry 
- 
Time-lapse (4D) 
seismic 
Repeated 3D seismic surveys acquired at different times to monitor reservoir changes during 
production or injection 
- 
Transient flow Flow regime where pressure and saturation distributions change with time, not yet reaching 
equilibrium 
 
Upscaling Process of transferring measurements or simulation results from a fine scale to a coarser 
simulation grid 
 
Vug Large dissolution pore in carbonate rocks, typically much larger than matrix interparticle 
pores 
 
Warren-Root model Classical dual-porosity formulation assuming uniformly distributed fractures surrounding 
cubic matrix blocks with pseudo-steady-state transfer 
 
Wellbore Drilled hole used for hydrocarbon production, fluid injection, or data acquisition  
 
8. References 
Al Hameli, F., Suboyin, A., Al Kobaisi, M., et al., (2022), Modeling fracture propagation in a dual -porosity 
system: Pseudo -3D-carter-dual-porosity model, Energies (Basel) , vol. 15, pp. 6779 
https://doi.org/10.3390/en15186779 
Alabere, A.O., Alsuwaidi, M., Hassan, A.A., et al., (2023), Controls on the formation and evolution of multimodal 
pore network in lower cretaceous limestone reservoir, Abu Dhabi, United Arab Emirates, Mar Pet Geol, vol. 
152, pp. 106222 https://doi.org/10.1016/j.marpetgeo.2023.106222 
Alabere, A.O., Jouini, M.S., Alsuwaidi, M., et al., (2025), Pore to core plug scale characterization of porosity and 
permeability heterogeneities in a Cretaceous  carbonate reservoir using laboratory measurements and digital 
rock physics, Abu Dhabi, United Arab Emirates, Mar Pet Geol , vol. 172, pp. 107214 
https://doi.org/10.1016/j.marpetgeo.2024.107214 
Bai, M., Ma, Q., Roegiers, J., (1994), Dual -porosity behavior of naturally fractured reservoirs, Int J Numer Anal 
Methods Geomech, vol. 18, pp. 359–376 https://doi.org/10.1002/nag.1610180602 
Barenblatt, G.I., Zheltov, I.P., Kochina, I.N., (1960), Basic concepts in the theory of seepage of homogeneous 
liquids in fissured rocks [strata], Journal of applied mathematics and mechanics , vol. 24, pp. 1286 –1303 
https://doi.org/10.1016/0021-8928(60)90107-6 
Berkowitz, B., (2002), Characterizing flow and transport in fractured geological media: A review, Adv Water 
Resour, vol. 25, pp. 861–884 https://doi.org/10.1016/S0309-1708(02)00042-8 
Chang, J., Lin, K., Wei, N., et al., (2026), THMC Modeling for CO₂ Geological Storage: Advances, Challenges, 
and Prospects, ACS Omega, vol. 11, pp. 15642–15678 https://doi.org/10.1021/acsomega.6c00226 
Cordero, J.A.R., Sanchez, E.C.M., Roehl, D., (2019), Integrated discrete fracture and dual -porosity-dual 
permeability models for fluid flow in deformable fractured media, J Pet Sci Eng , vol. 17 5, pp. 644 –653 
https://doi.org/10.1016/j.petrol.2018.12.053 
Correia, M.G., Schiozer, D.J., Maschio, C., Santos, M.S., (2011), Comparison of Single Porosity and Dual 
Permeability Systems Applied to Naturally Fractured Carbonate Reservoirs, in 73rd EAGE Conference and 
Exhibition incorporating SPE EUROPEC 2011, European Association of Geoscientists & Engineers, pp. cp-
238 https://doi.org/10.3997/2214-4609.2025101157 
De Boever, E., Foubert, A., Oligschlaeger, D., et al., (2016), Multiscale approach to (micr o) porosity 
quantification in continental spring carbonate facies: Case study from the Cakmak quarry (Denizli, Turkey), 
Geochemistry, Geophysics, Geosystems, vol. 17, pp. 2922–2939 https://doi.org/10.1002/2016GC006382

534 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Ding, D.Y., (2022), Dual-porosity and dual-fracture model for fractured geothermal reservoir simulations, Transp 
Porous Media, vol. 143, pp. 169–194 https://doi.org/10.1007/s11242-022-01787-3 
Egya, D.O., Geiger, S., Corbett, P.W.M., et al., (2019), Analysing the limitations of the dual -porosity response 
during well tests in naturally fractured reservoirs, Petroleum Ge oscience, vol. 25, pp. 30 –49 
https://doi.org/10.1144/petgeo2017-053 
Ehrenberg, S.N., (2018), Porosity and permeability variations in a Lower Cretaceous limestone reservoir, onshore 
Abu Dhabi, United Arab Emirates, in Research and Development Petroleum Conference and Exhibition 2018, 
European Association of Geoscientists & Engineers, pp. 93–96 https://doi.org/10.1190/RDP2018-40216625.1 
Fleury, M., & Soualem, J., (2009), Quantitative analysis of diffusional pore coupling from T2 -store-T2 NMR 
experiments, J Colloid Interface Sci, vol. 336, pp. 250–259 https://doi.org/10.1016/j.jcis.2009.03.051 
Fuentes-Cruz, G.,  & Valko, P.P., (2015), Revisiting the dual -porosity/dual-permeability modeling of 
unconventional reservoirs: the induced -interporosity flow field, SPE Journal, v ol. 20, pp. 124 –141 
https://doi.org/10.2118/173895-PA 
Garland, J., Neilson, J., Laubach, S.E., Whidden, K.J., (2012), Advances in carbonate exploration and reservoir 
analysis https://doi.org/10.1144/SP370 
Gerke, H.H., & Van Genuchten, M.T., (1993), A dual -porosity model for simulating the preferential movement 
of water and solutes in structured porous media, Water Resour Res , vol. 29, pp. 305 –319 
https://doi.org/10.1029/92WR02339 
Henglai, P., Fongngern, R., Saller, A., et al., (2025), Diagenetic and depositional controls on reservoir quality in 
a Middle Miocene carbonate buildup, Central Luconia, offshore Malaysia, Mar Pet Geol, vol. 181, pp. 107528 
https://doi.org/10.1016/j.marpetgeo.2025.107528 
Ismail, H., Latiff, A.H.A., Rashid, A., Jamaludin, S.N.F., (2026), Seismic reservoir characteriz ation framework 
for geological modeling input of carbonate flank deposits (CFD) in central luconia, sarawak, Geomechanics 
and Geophysics for Geo-Energy and Geo-Resources https://doi.org/10.1007/s40948-025-01095-2 
Jabbari, H., & Zeng, Z., (2011), A Three -Parameter Dual-porosity Model for Naturally Fractured Reservoirs, in 
SPE Western Regional Meeting, SPE, pp. SPE-144560 https://doi.org/10.2118/144560-MS 
Jamaludin, S.N.F., Sautter, B., Pubellier, M., Arshad Beg, M., (2021), The succession of Upper Eocene -Upper 
Miocene limestone growth and corresponding tectonic events in Luconia Shelf, Sarawak, Malaysia, Frontier 
of Earth Science, vol. 9 https://doi.org/10.3389/feart.2021.588629 
Janjuhah, H.T., & Alansari, A., (2020), Offshore carbonate facies characterization and reservoir quality of 
Miocene rocks in the southern margin of South China Sea, Acta Geologica Sinica-English Edition, vol. 94, 
pp. 1547–1561 https://doi.org/10.1111/1755-6724.13880 
Janjuhah, H.T., Alansari, A., Vintaned, J.A.G., (2019), Quantification of microporosity and its effect on 
permeability and acoustic velocity in Miocene carbonates, Central Luconia, offshore Sarawak, Malaysia, J Pet 
Sci Eng, vol. 175, pp. 108–119 https://doi.org/10.1016/J.PETROL.2018.12.035 
Jiménez, G., Latiff, A.H.A., Habel, W.B., Poppelreiter, M., (2024), Effective application of geological p rocess 
modeling for unravelling carbonate build-up complexity: A case study from the EX- Carbonate build-up 
in central Luconia Province, Malaysia, Mar Pet Geol , vol. 170, pp. 107117 
https://doi.org/10.1016/j.marpetgeo.2024.107117 
Jones, G.D., & Xiao, Y., (2005), Dolomitization, anhydrite cementation, and porosity evolution in a reflux system: 
Insights from reactive transport models, Am Assoc Pet Geol Bull , vol. 89, pp. 577 –601 
https://doi.org/10.1306/12010404078 
Jouini, M.S., Alabere, A.O., Alsuwaidi, M., et al., (2023), Experimental and digital investigations of heterogeneity 
in lower cretaceous carbonate reservoir using fractal and mult ifractal concepts, Sci Rep, vol. 13, pp. 20306 
https://doi.org/10.1038/s41598-023-47681-w

535 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Kazemi, H., (1969), Pressure transient analysis of naturally fractured reservoirs with uniform fracture distribution, 
SPE Journal, vol. 9, pp. 451–462 https://doi.org/10.2118/2156-A 
Khalid, M.S., Mansour, A.S., Desouky, S.E.D.M., et al., (2024), Carbonate reservoir characterization and 
permeability modeling using Machine Learning a study from Ras Fanar field, Gulf of Suez, Egypt, Earth Sci 
Inform, vol. 17, pp. 4675–4694 https://doi.org/10.1007/s12145-024-01406-3 
Koša, E., (2015), Sea-level changes, shoreline journeys, and the seismic stratigraphy of Central Luconia, Miocene-
present, offshore Sarawak, NW Borneo, Mar Pet Geol , vol. 59, pp. 35 –55 
https://doi.org/10.1016/j.marpetgeo.2014.07.005 
Koša, E., Warrlich, G.M.D., Loftus, G., (2015), Wings, mushrooms, and Christmas trees: The carbonate seismic 
geomorphology of Central Luconia, Mioce ne–present, offshore Sarawak, northwest Borneo, Am Assoc Pet 
Geol Bull, vol. 99, pp. 2043–2075 https://doi.org/10.1306/06181514201 
Kucuk, F., & Sawyer, W.K., (1980), Transient flow in naturally fractur ed reservoirs and its application to 
Devonian gas shales, in SPE Annual Technical Conference and Exhibition, SPE, pp. SPE-9397. 
Makhankova, A., Sautter, B., Mathew, M., et al., (2021), Seismic stratigraphy and sedimentology of a Miocene 
carbonate platform in Luconia, South China Sea, Geological Journal , vol. 56, pp. 1 –17 
https://doi.org/10.2118/9397-MS 
Malki, M.L., Saberi, M.R., Kolawole, O., et al., (2023), Underlying mechanisms and controlling factors of 
carbonate reservoir characterization from rock physics perspective: A comprehensive review, Geoenergy 
Science and Engineering, vol. 226, pp. 211793 https://doi.org/10.1016/j.geoen.2023.211793 
March, R., Doster, F., Geiger, S., (2018), Assessment of CO₂ storage potential in naturally fractured reservoirs 
with dual-porosity models, Water Resour Res, vol. 54, pp. 1650–1668 https://doi.org/10.1002/2017WR022159 
Matsushima, J., Ali, M.Y., Bouchaala, F., (2021), Propagation of waves with a wide range of frequencies in digital 
core samples and dynamic strain anomaly detection: carbonate rock as a case study, Geophys J Int, vol. 224, 
pp. 340–354 https://doi.org/10.1093/gji/ggaa467 
Maulindani, S.F., Abdassah, D., Marhaendrajana, Prakoso, S., (2 021), Reservoir simulation study for dual -
porosity model to determine characteristic of naturally fractured reservoir, in AIP Conference Proceedings, 
AIP Publishing LLC, pp. 020006 https://doi.org/10.1063/5.0061130 
Moldabayeva, G., Ismailova, J., Khussainova, A., et al., (2025), Waterflood assessment in carbonate reservoirs, 
Heliyon, vol. 11 https://doi.org/10.1016/j.heliyon.2025.e43386 
Moonen, P., & Carmeliet, J., (2013), Modeling moisture transport in intact and fractured concrete, in Understanding 
the Tensile Properties of Concrete, Elsevier, pp. 98–122 https://doi.org/10.1533/9780857097538.1.98 
Nguyen, N.V.K., Nguyen, X.H., Do, Q.K., (2018), Dual -porosity model for history matching and production 
forecast for an oil reservoir at Cuu Long Basin, Offshore Vietnam, in Vietnam Symposium on Advances in 
Offshore Engineering, Springer, pp. 95–101 https://doi.org/10.1007/978-981-13-2306-5_11 
Omidpour, A., Mahboubi, A., Moussavi-Harami, R., Rahimpour-Bonab, H., (2022), Effects of dolomitization on 
porosity–Permeability distribution in depositional sequences and its effects on reservoir quality, a case from 
Asmari Formation, SW Iran, J Pet Sci Eng, vol. 208, pp. 109348 https://doi.org/10.1016/j.petrol.2021.109348 
Pruess, K., & Narasimhan, T.N., (1985), A practical method for modeling fluid and heat flow in fractured porous 
media, Society of Petroleum Engineers Journal, vol. 25, pp. 14–26 https://doi.org/10.2118/10509-PA 
Putra, G. A. S., Haris, A., Wibowo, R. A., & Wijanarko, E. (2026). Reservoir characterization of the Terumbu 
and Arang formations using model-based seismic inversion in the East Natuna Basin. Scientific Contributions 
Oil and Gas, 49(1), 105–123. https://doi.org/10.29017/scog.v49i1.1979

536 
 
 
 
Yumnanisa et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2170 
 
Rahman, M.H., & Pierson, B.J., (2011), Effects of microporosity on permeability and sonic velocity of Miocene 
carbonates and an approach to relate micrite microtextures with microporosity occurrences  in Miocene 
carbonate reservoirs of offshore Sarawak, Malaysia, in SEG Technical Program Expanded Abstracts, Society 
of Exploration Geophysicists, pp. 2059–2063 https://doi.org/10.1190/1.3627614 
Shun, L., Jun, N., Xianli, W., et al., (2020), A dual -porous and dual -permeable media model for imbibition in 
tight sandstone reservoirs, J Pet Sci Eng, vol. 194, pp. 107477 https://doi.org/10.1016/j.petrol.2020.107477 
Trianto, A., Jimenez, G., Latiff, A.H., Jamaludin, S.N.F., (2026), Unlocking the Complexities of Karstic 
Reservoirs Using Comprehensive Framework for Advanced 3D Static Modeling in JTN Carbonate Field in 
Central Luconia Province, Geological Journal, vol. 61, pp. 785–808 https://doi.org/10.1002/gj.70010 
Tsakiroglou, C.D., Ioannidis, M.A., Amirtharaj, E., Vizika, O., (2009), A new approach for the characterization 
of the  pore struc ture of dual -porosity rocks, Chem Eng Sci , vol. 64, pp. 847 –859 
https://doi.org/10.1016/j.ces.2008.10.046 
Warren, J.E., Root, P.J., (1963), The behavior of naturally fractured reservoirs, Society of Petroleum Engineers 
Journal, vol. 3, pp. 245–255 https://doi.org/10.2118/426-PA 
Wei, C., Cheng, S., Wang, Y., et al., (2021), Practical pressure-transient analysis solutions for a well intercepted 
by finite conductivity vertical fracture in naturally fractured reservoirs, J Pet Sci Eng , vol. 204, pp. 108768 
https://doi.org/10.1016/j.petrol.2021.108768 
Wu, Y.S., Pruess, K., Persoff, P., (1998 ), Gas flow in porous media with Klinkenberg effects, Transp Porous 
Media, vol. 32, pp. 117–137 https://doi.org/10.1023/A:1006535211684 
Xiong, W., Zhao, Y.L., Zhang, L.H., et al., (2025), Mechanism study of enhanced gas recovery and CO₂ storage 
in naturally fractured carbonate reservoirs using a dual-permeability model coupled with association equation 
of state, Gas Science and Engineering, vol. 139, pp. 205632 https://doi.org/10.1016/j.jgsce.2025.205632 
Yan, X., Qin, G.Y., Zhang, L.M., et al., (2024), A dual-porosity flow-net model for simulating water-flooding in 
low-permeability fractured reservoirs, Geoenergy Science and Engineering, vol. 240, pp. 213069 
https://doi.org/10.1016/j.geoen.2024.213069 
Yerima, A.I., Tsegab, H., Hermana, M., et al., (2024), Feasibility of CO₂ plume geothermal systems in Miocene 
carbonate reservoirs of Central Luconia p rovince, offshore Sarawak: A systematic review of technologies, 
challenges, mitigation mechanisms and economic prospects, J Clean Prod , vol. 468, pp. 143032 
https://doi.org/10.1016/j.jclepro.2024.143032 
Zambrano, M., Volatili, T., Mancini, L., et al., (2021), Pore -scale dual-porosity and dual-permeability modeling 
in an exposed multi -facies porous carbonate reservoir, Mar Pet Geol , vol. 128, pp. 105004 
https://doi.org/10.1016/j.marpetgeo.2021.105004 
Zampetti, V., Schlager, W., van Konijnenburg,  J.H., Everts, A.J., (2004), Architecture and growth history of a 
Miocene carbonate platform from 3D seismic reflection data; Luconia province, offshore Sarawak, Malaysia,  
Mar Pet Geol, vol. 21, pp. 517–534 https://doi.org/10.1016/j.marpetgeo.2004.01.006 
Zhang, N., Luo, Z., Chen, Z., et al., (2023), Thermal–hydraulic–mechanical–chemical coupled processes and their 
numerical simulation: a comprehensive review, Acta Geotech , vol. 18, pp. 6253 –6274. 
https://doi.org/10.1007/s11440-023-01976-4
