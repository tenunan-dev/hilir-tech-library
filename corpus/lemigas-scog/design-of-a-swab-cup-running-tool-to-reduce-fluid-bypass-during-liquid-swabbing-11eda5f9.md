---
source_id: "lemigas-scog"
title: "Design of a Swab Cup Running Tool to Reduce Fluid Bypass during Liquid Swabbing Operations in Dual Size Tubing"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2155"
retrieved_at: "2026-10-24T14:29:54+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "11eda5f90e5d3fb7e726cbb089219d1e05ded63790832507ebb5d3a5a52dcaeb"
collected: "manual"
---

# Design of a Swab Cup Running Tool to Reduce Fluid Bypass during Liquid Swabbing Operations in Dual Size Tubing

279 
 
https://doi.org/10.29017/scog.v49i3.21555 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 279 – 298 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Design of a Swab Cup Running Tool to Reduce Fluid Bypass  
during Liquid Swabbing Operations in Dual Size Tubing  
Completion Oil and Gas Wells 
 
Karnando1,2*, Dedy Irawan1, and Amega Yasutra1 
 
1Petroleum Engineering, Faculty of Mining and Petroleum Engineering, Institut Teknologi Bandung,  
Ganesa Street No. 10, Bandung, West Java, 40132, Indonesia. 
2Pertamina Hulu Mahakam, 
Yos Sudarso Street No.1, Karang Jati, Mekar Sari, Balikpapan, Kalimantan Timur 76111, Indonesia 
*Corresponding author: Karnando (kno_nando@yahoo.com) 
Karnando: https://orcid.org/0009-0008-8342-7312  
Received: 13 April 2026; Revised: in revised form 08 June 2026; Accepted: 03 July 2026 
Available: online 30 September 2026. 
 
 
 
 
ABSTRACT - Swabbing is a liquid unloading method used in the oil and gas industry to reduce hydrostatic 
pressure caused by fluid accumulation in the wellbore. In wells with dual -size tubing completions (4.5 -inch 
and 3.5 -inch), tubing diameter transitions can reduce S wab Cup sealing performance, causing fluid bypass 
and lowering lifting efficiency. This study develops a modified Swab Cup Carrier and swab mandrel to 
support continuous fluid lifting in dual -size tubing completions. An engineering design research approach  
was applied, including field problem identification, conceptual design, Computer -Aided Design (CAD), 
Finite Element Analysis (FEA), prototype development, tubing simulation, and functional evaluation. The 
proposed design incorporates a cam -guided release -and-carry mechanism that enables the Swab Cup Carrier 
to release at the tubing X -over during Run In Hole and reconnect during Pull Out of Hole. FEA of AISI 4130 
alloy steel showed a maximum von Mises stress of 278.6 MPa, below the material yield strength o f 460 MPa, 
indicating adequate structural safety. Prototype testing using a PVC tubing simulation verified the proposed 
mechanism. The design has the potential to minimise fluid bypass, maintain lifting continuity, and improve 
swabbing effectiveness in dua l-size tubing completions. Further laboratory and field validation is required 
to confirm its operational performance.  
Keywords: swabbing, swab cup carrier, dual-size tubing completion. 
 
 
How to cite this article: 
Karnando, Dedy Irawan, and Amega Yasutra , 2026, Design of a Swab Cup Running Tool to Reduce 
Fluid Bypass during Liquid Swabbing Operations in Dual Size Tubing Completion Oil and Gas Wells, 
Scientific Contributions Oil and Gas, 49 (3) pp. 279-298.

280 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
1. Introduction 
In the oil and gas industry, sustained well production is highly dependen t on the ability of reservoir fluids 
to flow continuously to the surface. As producing fields mature, reservoir pressure commonly declines, which 
may lead to the accumulation of liquids within the production tubing. This condition is referred to as liquid 
loading, in which liquids such as water, condensate, or oil accumulate in the wellbore and increase the 
hydrostatic pressure acting against the reservoir.  
As oil and gas fields mature, declining reservoir pressure and deteriorating well performance often require 
appropriate production optimization and well intervention strategies to sustain or restore hydrocarbon production. 
Turnip et al. (2024)  demonstrated the importance of systematic well candidate selection for matrix acidizing in 
mature fields, where appropriate stimulation candidates can provide significant production improvement. Maurenza 
et al. (2023) further showed that changes in the production system, particularly the installation of artificial lift, can 
influence well production performance and the predicted productive life of the well. In addition, Hamzah et al. (2021) 
evaluated hydraulic-fractured well performance using empirical correlations and machine -learning approaches, 
highlighting the importance of systematic performance evaluation in supporting well candidate selection  and 
production enhancement. Collectively, these studies indicate that maintaining production from mature wells requires 
intervention strategies that are selected according to specific well conditions and dominant production constraints. 
In wells experienc ing liquid accumulation, one of the key operational constraints is the increasing hydrostatic 
pressure inside the tubing, which may restrict reservoir inflow and eventually lead to production decline or cessation. 
Liquid accumulation increases back pressur e on the reservoir, reduces hydrocarbon deliverability, and may 
eventually cause the well to stop producing if it is not properly mitigated. Lea et al. (2003) described liquid loading 
as one of the major causes of production performance decline in mature wells, particularly in low-pressure gas wells. 
Similarly, emphasized that liquid accumulation in the tubing can disturb flow stability and significantly reduce well 
productivity. One of the widely applied methods for mitigating liquid loading is liquid unloading through swabbing 
operations. Swabbing is a mechanical well intervention method used to lift accumulated fluids from the wellbore by 
means of a Swab Cup conveyed on wireline, either slickline or braidedline. The fundamental principle of this method 
is to reduce the hydrostatic pressure inside the tubing, thereby creating an underbalanced condition that enables 
reservoir fluids to resume flowing to the surface. 
Bourgoyne et al. (1991) stated that swabbing is commonly applied in low-pressure wells because of its 
operational flexibility and relatively lower cost compared with other liquid unloading methods. In line with this, 
Saputra et al. (2022)  reported that several wells in mature fields with depleted reservoir pressure req uire 
continuous liquid unloading before gas production can be restored. In certain applications, periodic dewatering is 
performed using rig-less intervention techniques, such as coiled tubing operations or slickline swab jobs. 
The success of swabbing operations is highly dependent on the ability of the Swab Cup to maintain sealing 
contact against the tubing wall during the fluid -lifting process. In wells with single size  tubing completion, 
swabbing operations are relatively stable because the tubing diamete r remains uniform along the operating path, 
allowing continuous contact between the Swab Cup and the tubing wall to be maintained. However, in wells with 
dual size tubing completion, changes in tubing diameter may become a technical constraint that reduces swabbing 
effectiveness. Lyons and Plisga (2004) explained that variations in tubing geometry can affect the interaction 
between intervention tools and the tubing wall,  particularly in terms of mechanical contact and flow stability. 
Economides et al. (1994) also stated that  changes in production conduit dimensions may influence differential 
pressure stability during fluid lifting, thereby potentially reducing operational efficiency. 
This problem was observed during swabbing operations in Oil and Gas Field X, particularly in wells with a 4.5-
inch and 3.5-inch dual size tubing configuration. Based on preliminary observations of operational conditions, 
when the Swab Cup moves  from the 3.5 -inch tubing into the 4.5 -inch tubing, sealing loss occurs due to the 
change in tubing diameter. This condition allows the lifted fluid to bypass through the clearance between the 
Swab Cup and the tubing wall and subsequently fall back into th e lower section of the well. As a result, the 
liquid unloading target becomes difficult to achieve optimally, the number of swabbing runs may increase, and 
the overall operation time becomes longer. This issue indicates that conventional Swab Cup designs, which are

281 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
generally intended for uniform tubing diameters, are not fully capable of accommodating operational 
requirements in dual size tubing completion.  
Although numerous studies have addressed liquid unloading methods, swabbing operations, and well 
intervention optimization, studies specifically focusing on the development of Swab Cup designs for dual size 
tubing completion applications remain limited. Most existing discussions emphasize unloading method selection, 
production evaluation after intervention, or operational aspects of swabbing units. Meanwhile, the design of Swab 
Cup components capable of adapting to tubing diameter transitions has not been extensively investigated. This gap 
indicates the need to develop a Swab Cup design that can accommodate changes in tubing diameter and reduce 
the potential for fluid bypass during swabbing operations. 
Based on these conditions, this study aims to develop a modified Swab Cup design concept incorporating  a 
cam groove and a cam -guided release-and-carry mechanism for the 4.5 -inch Swab Cup in dual size tubing 
completion applications. During Run in Hole, the 4.5-inch and 3.5-inch Swab Cups are lowered simultaneously as 
part of a single tool assembly. The 4.5-inch Swab Cup Carrier is designed to be released and temporarily positioned 
at the X-over area, while the 3.5-inch Swab Cup continues moving downward to reach the liquid level to be swabbed. 
During Pull Out of Hole, the 3.5-inch Swab Cup lifts fluid from the lower tubing section. When the assembly passes 
through the transition from the 3.5-inch tubing to the 4.5-inch tubing, the fluid-lifting function is then continued by 
the 4.5-inch Swab Cup. Through this mechanism, sealing contact between the Swab Cup and the tubing wall is 
expected to be maintained up to the surface, thereby improving the effectiveness of liquid lifting. 
This study focuses on the design stage using an engineering design approach, including problem identification, 
evaluation of existing design limitations, development of the modified design concept, and analysis of the proposed 
working mechanism. The results of this study are expected to provide a basis for developing an adaptive Swab Cup 
Carrier for swabbing operations in dual size tubing completion and serve as a reference for further studies involving 
numerical simulation, prototype fabrication, and field testing. 
 
2. Methodology 
2.1 Research approach 
This study was conducted through a sequential engineering design research approach, consisting of problem 
identification, evaluation of the  existing design, conceptual design development, computer-aided design (CAD) 
modelling, finite element analysis (FEA), prototype development, mock -up tubing testing, and analysis of the 
proposed working mechanism. 
2.2 Problem identification 
Problem identification was carried out through a review of swabbing operation reports, well diagrams, and 
observations of operations performed in wells with dual size tubing completion. The initial stage of the study 
focused on evaluating swabbing operations in Fi eld X, particularly wells with a combined completion 
configuration consisting of 3.5 -inch tubing in the lower section and 4.5 -inch tubing in the upper section.  Based 
on the operational review, fluid bypass was frequently observed when the Swab Cup passed t hrough the tubing 
diameter transition area. This condition is associated with the loss of sealing contact between the Swab Cup and 
the tubing wall as the tool moves across the X -over section. The well configuration with 4.5 -inch and 3.5-inch 
tubing is illustrated in Figure 1, while the mechanism of fluid bypass when the 3.5-inch Swab Cup enters the 4.5-
inch tubing section is illustrated in Figure 2. This condition resulted in several operational consequences, including 
loss of sealing integrity, reduced fluid-lifting efficiency, an increased number of swabbing runs, and failure to meet 
the targeted liquid -unloading performance. These operational issues were subsequently used as the basis for 
developing a new design concept.

282 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
 
Figure 1.  
Schematic well configuration showing the 4.5-inch tubing in the upper section,  
the 3.5-inch tubing in the lower section, and the X-over connecting the two tubing sizes.  
 
 
 
 
 
Figure 2.  
Schematic illustration of fluid bypass when a 3.5-inch Swab Cup enters the 4.5-inch tubing section during Pull Out of Hole. 
The clearance between the Swab Cup and the tubing wall allows part of the lifted fluid to flow downward.

283 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
2.3 Evaluation of the existing swab cup design 
The evaluation of the existing design was conducted on conventional Swab Cups commonly used in swabbing 
operations for wells with single size tubing completion. In this configuration, one Swab Cup size is specifically 
selected for one tubing size. A 3.5-inch Swab Cup is used in wells or intervals equipped with 3.5-inch tubing, whereas 
a 4.5-inch Swab Cup is used in 4.5-inch tubing. Therefore, each Swab Cup is designed to operate within a relatively 
uniform tubing diameter along its operating path. 
A conventional Swab Cup generally consists of an elastomeric sealing element mounted on a mandrel and 
designed to establish sealing contact against the inner wall of the tubing. During the Pull Out of Hole operation, the 
pressure differential between the lower and upper sides of the Swab Cup causes the elastomeric element to expand 
and press against the tubing wall, thereby enabling the fluid to be lifted toward the surface. The effectiveness of this 
mechanism is highly dependent on the dimensional compatibility between the outer diameter of the Swab Cup and 
the inner diameter of the tubing. 
The existing design does not incorporate a cam groove, guide pin, or  cam-guided release-and-carry 
mechanism. Consequently, the Swab Cup can only operate effectively within tubing sizes that correspond to its 
designed dimensions. A 3.5-inch Swab Cup is unable to maintain adequate sealing when entering a 4.5-inch tubing 
section because a clearance is formed between the sealing element and the tubing wall. Conversely, a 4.5 -inch 
Swab Cup cannot be run through a 3.5-inch tubing section because its outer diameter exceeds the available internal 
tubing clearance. 
The evaluation of the existing design focused on the geometry and dimensions of the Swab Cup, sealing  
mechanism, elastomer deformation capability, compatibility with the tubing inner diameter, and tool response when 
approaching the transition area or X-over. The analysis also considered the potential occurrence of fluid bypass 
caused by the loss of sealing contact when the 3.5-inch Swab Cup moves from  the smaller-diameter tubing into 
the 4.5-inch tubing section. The primary limitation of the existing design is the absence of a mechanism that enables 
the automatic transfer of the fluid -lifting function between the 3.5 -inch Swab Cup and the 4.5 -inch Swab Cup 
within a single operating assembly. This limitation makes the conventional design less suitable for direct 
application in wells with dual size tubing completion.  The analysis of these limitations was subsequently used as 
the basis for developing a modified Swab Cup Carrier and swab mandrel design incorporating a cam -guided 
release-and-carry mechanism. 
2.4 Design concept development 
The design development was carried out through a design modification approach applied to the c onventional 
Swab Cup system. The proposed concept is intended for wells with a dual size tubing completion configuration,  
consisting of 4.5-inch tubing in the upper section and 3.5-inch tubing in the lower section. The design integrates 
a 3.5-inch Swab Cup and a 4.5-inch Swab Cup within a single operating assembly, enabling the fluid -lifting 
process to be performed sequentially according to the tubing size encountered along the operating path. 
During the Run In Hole stage, the 4.5-inch Swab Cup and the 3.5-inch Swab Cup are lowered simultaneously 
as part of one tool assembly. The 4.5-inch Swab Cup Carrier is designed to reach the release position and remain 
temporarily retained at the X-over area between the 4.5-inch and 3.5-inch tubing sections. Meanwhile, the swab 
mandrel and the 3.5-inch Swab Cup are allowed to continue moving downward toward the lower section of the 
fluid column to be lifted. 
During the Pull Out of Hole stage, the 3.5-inch Swab Cup functions as the initial lifting element, lifting flui d 
from the lower tubing section toward the transition area. As the assembly moves from the 3.5-inch tubing section 
into the 4.5-inch tubing section, the swab mandrel re-engages with the 4.5-inch Swab Cup Carrier. Subsequently, 
the Swab Cup Carrier reaches the carry position and is pulled together with the assembly, allowing the 4.5 -inch 
Swab Cup to continue lifting fluid through the upper tubing section toward the surface. 
The main design modification involves the incorporation of a cam groove on the Swab Cup Carrier and a guide 
pin mechanism on the swab mandrel. The cam groove functions as a controlled guide path for the pin movement

284 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
to regulate the transition of the mechanism between the release and carry positions. During Run in Hole, the 
interaction between the cam groove and the guide pin is designed to release the 4.5-inch Swab Cup Carrier at the 
X-over area. During Pull Out of Hole, the same interaction is designed to reconnect the Swab Cup Carrier with the 
swab mandrel so that it can be retrieved to the surface. Based on the identified operational limitations and the 
required transfer of the fluid -lifting function across the tubing transition, the proposed design was formulated 
according to the following key functional requirements: 
• The use of two Swab Cup sizes within a single operating assembly 
• The use of the 3.5-inch Swab Cup as the initial lifting element in the lower tubing section 
• The use of the 4.5-inch Swab Cup as the subsequent lifting element in the upper tubing section 
• The implementation of a cam-guided release-and-carry mechanism to control the release and retrieval of the 
Swab Cup Carrier 
• The maintenance of sealing continuity according to the corresponding tubing diameter 
• The reduction of potential fluid bypass at the tubing diameter transition area. 
The critical design point is located at the X-over area, where the tubing diameter changes and the fluid-lifting 
function is transferred from the 3.5-inch Swab Cup to the 4.5-inch Swab Cup. Therefore, the design concept was 
focused on the cam groove geometry, guide pin trajectory, component clearance and tolerances, stability of the 
release and carry positions, and the ability of the system to operate repeatedly without disrupting the sealing 
function of each Swab Cup. This concept was subsequently evaluated through CAD modelling, FEA-based stress 
analysis, prototype development, and working mechanism simulation using a mock-up tubing model. 
Table 1.  
Main Modelling Parameters of the Swab Cup Carrier and Swab Mandrel. 
Parameter Value/Specification 
Completion configuration Dual size tubing completion 
Lower tubing section 3.5 inches 
Upper tubing section 4.5 inches 
Swab Cup size 3.5 inches and 4.5 inches 
Design focus 4.5-inch Swab Cup Carrier 
Main components Ring, main body, cam groove, guide pin, and swab mandrel 
Ring outer diameter Ø3.3000 inches 
Ring thread diameter Ø2.3200 inches 
Ring length 1.2000 inches 
Main swab mandrel diameter Ø2.3200 inches 
Main swab mandrel length 8.2000 inches 
Swab Cup Carrier length 5.5200 inches 
Carrier connection thread diameter Ø2.600 inches 
Number of cam grooves Two pairs 
Cam groove configuration 180° symmetrical arrangement 
Cam groove path radius R1.000 inches and R1.750 inches 
Mechanism system Cam-guided release-and-carry 
Swab Cup Carrier and swab mandrel material AISI 4130 alloy steel 
Sealing material Nitrile Butadiene Rubber (NBR) 
Fabrication method CNC machining 
General tolerance ±0.001 inches 
Modelling software SolidWorks

285 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
2.5 Software and data reproducibility 
The three -dimensional models of the Swab Cup Carrier and swab mandrel were developed using 
SolidWorks 2023 software, while the structural analysis was performed using SolidWorks Simulation 2023. 
The principal geometric par ameters, material specifications, and dimensional requirements used in the design 
are provided in Table 1  to facilitate reproduction of the proposed configuration. The Swab Cup Carrier and 
swab mandrel were specified using AISI 4130 alloy steel, whereas Ni trile Butadiene Rubber (NBR) was 
specified for the sealing element.  
The prototype used for preliminary functional verification was fabricated using a Creality K1 Max 3D printer 
with PLA+ filament. Functional testing was conducted using a simplified mock -up consisting of 4 -inch and 3 -
inch PVC pipes representing the inside diameter transition between the upper and lower tubing sections. The 
prototype and mock -up testing were intended to evaluate component fit, guide -pin movement, and the release -
and-carry sequence rather than actual downhole structural or sealing performance. 
The operational information used for problem identification was derived from swabbing ope ration reports, 
well diagrams, and field observations. These data were used to define the engineering problem and design 
requirements. The geometric parameters, working mechanism, material assumptions, and simulation approach 
required to reproduce the engi neering design are reported in this manuscript. Further reproducibility of the 
structural and operational performance will require validation using actual engineering materials, representative 
pressure and temperature conditions, and field-scale testing. 
2.6 Computer-aided design (CAD) modelling 
The design modelling of the  Swab Cup Carrier and swab mandrel was  performed using Computer -Aided 
Design (CAD) software. The modelling process aimed to generate a three-dimensional geometry that represents the 
interrelationship between components, the cam groove trajectory, pin position, inter-component clearances, and 
the overall configuration of the cam-guided release-and-carry mechanism. 
The model was developed for application in wells with a dual size tubing completion configuration, consisting 
of nominal 4.5-inch tubing in the upper section and nominal 3.5-inch tubing in the lower section. In the modelling 
process, the nominal tubing size was not directly used as the working diameter. The actual tubing inner diameter 
must be determined based on the tubing specifications, including nominal size, weight per unit length, grade, and 
wall thickness. These parameters were used to ensure the  dimensional compatibility of the Swab Cup, Swab Cup 
Carrier, and swab mandrel with the available internal tubing clearance. 
The sealing design employs two different Swab Cup sizes. The 3.5-inch Swab Cup is used for fluid lifting in 
the lower tubing section, whereas the 4.5 -inch Swab Cup is used to continue fluid lifting in the  upper tubing 
section. Therefore, the sealing element is not designed as a single adaptive component capable of accommodating 
both tubing sizes. Instead, each Swab Cup operates according to its corresponding tubing diameter. 
The main modification in the CAD model was applied to the 4.5-inch Swab Cup Carrier by incorporating two 
pairs of cam grooves arranged in an opposing configuration with 180° symmetry. The cam groove functions as a 
guided path for the pin on the swab mandrel to regulate the transition between the release and carry positions. The 
modelling parameters included the cam groove path length, groove depth, path radius, fillet radius, pin diameter, 
inter-component clearance, and the principal dimensions of the Swab Cup Carrier and swab mandrel. 
The actual design material for the Swab Cup Carrier and swab mandrel was specified as AISI 4130 alloy steel, 
while the sealing element was specified as nitrile butadiene rubber (NBR). The resulting CAD model was 
subsequently used as the basis f or stress analysis using Finite Element Analysis, prototype fabrication by 3D 
printing, and the preparation of technical drawings for fabrication using Computer Numerical Control machining. 
2.7 Finite element analisys (FEA)-based stress analysis 
Stress analysis was performed using the Finite Element Analysis (FEA) method with SolidWorks Simulation 
2023 software. This analysis aimed to evaluate the structural response of the Swab Cup Carrier and swab mandrel

286 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
design under the static loading conditions defined in the simulation. Particular  attention was given to the cam 
groove, guide pin area, and other geometric transitions that may induce stress concentration during the operation 
of the cam-guided release-and-carry mechanism. 
The three -dimensional model developed during the Computer -Aided Design stage was used as the  base 
geometry for the simulation. The material assigned to the model was AISI 4130 alloy steel. The material properties 
used in the simulation included density, elastic modulus, Poisson’s ratio, yield strength, and ultimate tensile 
strength, based on the material data adopted in this study. 
The simulation procedure included material assignment, contact condition definition, fixture or boundary 
condition application, load application, mesh generation, solving process, and result evaluation. The mesh was 
used to discretize the geometry into smaller elements so that the stress response could be numerically calculated. 
Mesh refinement was directed toward the cam groove, guide pin area, fillets, and other regions with relatively 
sharp geometric transitions. 
The primary parameter evaluated in this analysis was the equivalent von Mises stress. The maximum stress 
obtained from the simulation was compared with the material yield strength to assess the potential for plastic 
deformation. In addition, the stress distribution and the locations of stress concentration were examined to identify 
design areas requiring further evaluation or refinement. 
The structural evaluation criterion was established based on the requirement that the maximum von Mises 
stress should remain below the material yield strength under the simulated loading condition. When required, the 
factor of safety was calculated as the ratio between the material yield strength and the maximum von Mises stress. 
This analysis was used as a preliminary structura l evaluation and was not intended to replace strength testing 
under actual downhole pressure, temperature, fatigue, corrosion, and dynamic loading conditions. 
 
3. Result and discussion 
3.1 Problem analysis and evaluation of the existing design 
Swabbing operations are among the liquid unloading methods widely applied in oil and gas wells to reduce 
hydrostatic pressure caused by fluid accumulation inside the tubing. The success of this operation is strongly 
influenced by the ability of the Swab Cup system to maintain sealing contact against the tubing wall, thereby 
enabling fluids to be effectively lifted to the surface. According to, the effectiveness of unloading methods is highly 
dependent on the ability of the equipment to maintain differential pressure during the fluid-lifting process. Loss of 
differential pressure due to leakage or fluid bypass may reduce operational efficiency and prevent the unloading 
target from being achieved. 
• Analysis of swabbing operation problems in dual size tubing completion 
In Field X, the main operational problem was identified in wells with a dual size tubing completion 
configuration using a combination of 3.5 -inch and 4.5 -inch tubing. Based on the evaluation of previous 
swabbing operations, fluid bypass occurred  when the Swab Cup moved through the tubing diameter 
transition area. Under this condition, the contact between the sealing element and the tubing wall decreased, 
allowing part of the lifted fluid to flow back downward through the clearance formed between the Swab 
Cup and the tubing wall.  
This condition reduced the effectiveness of swabbing operations and potentially increased the number  of 
swabbing runs, overall operating time, and well intervention costs. The problem indicates that the currently 
used Swab Cup design still has limitations in accommodating significant tubing diameter changes. Therefore, 
design development is required to improve the geometric adaptability of the Swab Cup system for dual size 
tubing completion applications. 
• Evaluation of the existing swab cup design 
The existing design currently used in swabbing operations in Field X consists of a cylindrical main  body 
equipped with multiple elastomer layers that function as sealing elements. This geometry is designed to

287 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
generate contact pressure against the tubing wall, thereby forming a sealed chamber that enables fluid to be 
displaced toward the surface during the pulling process. 
Based on the technical drawing shown in Figure 3, the existing design has a relatively simple construction, 
with a multi -lip elastomer configuration arranged along the outer section of the body. This type of design 
is commonly used in conventional swabbing operations because it is relatively ea sy to manufacture and has 
a comparatively low fabrication cost. According to Ash-Shidiq and Suhartanto (2025) , conventional Swab 
Cups remain a key component in various well unloading operations due to their simple design and ease of 
field implementation.  
However, the existing design was developed for tubing conditions with a relatively uniform diameter. In dual 
size tubing completion applications, the change in tubing diameter causes the contact pressure distribution 
between the Swab Cup and the tubing wall to become non-uniform. Consequently, the sealing capability may 
decrease when the tool passes through the tubing diameter transition area. This condition is consistent with the 
explanation of Lyons and Plisga (20 04), who stated that changes in production conduit geometry can affect 
the effectiveness of contact between intervention tools and the tubing wall, thereby increasing the risk of fluid 
isolation loss during operation. 
 
 
 
Figure 3.  
Cross-sectional configuration of a conventional multi-lip Swab Cup, illustrating the inner diameter (ID), outer diameter 
(OD), and elastomeric sealing lips used for single-size tubing applications (adapted from CANAM Pipe & Supply 2018). 
 
3.2 Results of the modified design development 
Based on the problem identification and evaluation of the existing design, a modified system was developed by 
integrating a 4.5-inch Swab Cup Carrier and a swab mandrel for dual size tubing completion applications. The design 
incorporates a cam-guided release-and-carry mechanism, which enables the Swab Cup Carrier to be temporarily 
released at the X-over area during Run in Hole and reconnected during Pull Out of Hole. The design development 
involved geometric modifications to the Swab Cup Carrier, swab mandrel, cam groove, and guide pin to support the 
transfer of the fluid-lifting function from the 3.5-inch Swab Cup to the 4.5-inch Swab Cup.  
Based on the problems identified during swabbing operations in  wells with dual size tubing completion, this 
study developed a modified Swab Cup Carrier design concept intended to improve the adaptability of the tool to 
changes in tubing diameter. The well configuration considered in this study consists of 4.5-inch tubing in the upper 
section and 3.5-inch tubing in the lower section. Therefore, a swabbing system capable of maintaining liquid-lifting 
continuity across the tubing diameter transition area is required. 
The developed design does not only function as a Swab Cup holder, but also serves as an integral part of the cam-
guided release-and-carry mechanism. This mechanism enables the 4.5-inch Swab Cup to be lowered together with 
the 3.5-inch Swab Cup during Run In Hole and subsequently positioned or temporarily retained at the X-over area 
between the 4.5-inch and 3.5-inch tubing sections. Meanwhile, the 3.5 -inch Swab Cup remains able to continue 
moving downward until it reaches the lower section of the liquid column to be swabbed.

288 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
During Pull Out of Hole, the 3.5-inch Swab Cup functions to lift liquid from the lower 3.5-inch tubing section. 
When the 3.5-inch Swab Cup passes through the X-over area from the 3.5-inch tubing into the 4.5 -inch tubing 
section, the liquid-lifting process is then continued by the 4.5 -inch Swab Cup. Accordingly, the 4.5 -inch Swab 
Cup Carrier acts as a continuation system for liquid lifting in the upper tubing section up to the surface. This 
concept is intended to maintain sealing continuity, reduce the potential for fluid bypass, and improve liquid-lifting 
effectiveness in wells with dual size tubing completion. 
Geometrically, the modified Swab Cup Carrier design consists of several main components, namely the ring, 
main body, cam groove, and cam follower pin, which are integrated into a single mechanical system. The primary 
modification was applied to the holder section by incorporating a cam groove that forms several mechanical 
operating segments. Unlike the existing design, which does not include a cam groove for this mechanical 
operation, the proposed design uses the cam groove  as an additional mechanical feature that enables the tool to 
respond through a leave-and-carry sequence when it is run downward, reaches the transition between the 4.5-inch 
and 3.5-inch tubing sections, is temporarily retained at the X-over area, and is subsequently retrieved during Pull 
Out of Hole. 
The cam groove functions as a guided trajectory for the pin, a positional control feature for the release and 
carry states, and a mechanical interface governing the engagement between the Swab Cup Carrier and the swab 
mandrel. The cam groove is designed to guide the pin movement and control the positional transition of the Swab 
Cup Carrier between the release and carry conditions. The sealing function remains provided by the 4.5-inch Swab 
Cup element, which operates according to the inner diameter of the upper tubing section. Through the integrated 
configuration of the 4.5 -inch Swab Cup, Swab Cup Carrier, and s wab mandrel, the sealing area is expected to 
maintain contact with the tubing wall, particularly during the diameter transition from the 3.5-inch tubing section 
into the 4.5-inch tubing section. 
This concept was developed based on the principle of adaptive sealing, defined in this study as the capability 
of a mechanical system to maintain its sealing function despite dimensional changes in the operating environment. 
In this context, adaptive sealing is implemented through the combination of cam groove geometry and the leave-
and-carry mechanism, enabling the 4.5 -inch Swab Cup to accommodate the tubing diameter transition and 
maintain continuous liquid-lifting functionality. Budynas and Nisbett (2020)  stated that systems incorporating 
flexible elements generally exhibit better adaptability to geometric variations because such elements can distribute 
stress and contact pressure more uniformly. 
 
Table 2.  
Comparison Between the Existing Design and the Modified Design 
 
Aspect Existing design Modified design 
Swab Cup configuration One Swab Cup size for one 
tubing size 
Two Swab Cup sizes integrated 
within a single assembly 
Transfer lifting 
mechanism 
Not available Transfer from the 3.5-inch Swab 
Cup to the 4.5-inch Swab Cup 
Cam groove Not available Available 
Release-and-carry 
mechanism 
Not available Available 
Capability to pass through 
the X-over 
Limited Designed for dual size tubing 
completion 
Risk of fluid bypass High at the transition area Potentially lower 
Application Single size tubing completion Dual size tubing completion

289 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
 
Figure 4. 
 Modified 4.5-inch Swab Cup Carrier consist of Upper Ring, Main Body, Pin Groove and Pin groove stopper,  
all are incorporating the cam groove and guide-pin mechanism for release and reconnection at the tubing X-over.   
(Authors’ CAD model eveloped using SolidWorks). 
 
 
 
 
 
Figure 5.  
Three-dimensional view of the modified Swab Cup Running Tool assembly, consisting of the Swab Cup Carrier, swab 
mandrel, ring, cam groove, and guide-pin mechanism. (Authors’ CAD model developed using SolidWorks). 
 
In addition to the cam groove, the design is also equipped with a cam groove pin that functions as  a guiding 
and positional control element for the Swab Cup as it follows the cam groove trajectory. This component is 
designed to regulate the movement pattern o f the Swab Cup Carrier so that it operates in accordance with the 
intended mechanism, in which the Swab Cup remains temporarily retained during downward movement and is 
subsequently carried upward during retrieval as the assembly passes through the X-over between the 4.5-inch and 
3.5-inch tubing sections. 
The tool is also designed to ensure safe operation from both mechanical and operational perspectives. 
Accordingly, the flexibility of the Swab Cup Carrier can be improved without compromising the stability  and 
structural integrity of the main components. 
Through this design development, the 4.5 -inch Swab Cup Carrier is expected to perform three primary 
functions: as a component that can be temporarily retained at the X-over area, as a continuation system for liquid 
lifting from the 3.5 -inch Swab Cup, and as a sealing system capable of maintaining contact with the 4.5 -inch 
tubing wall until the liquid is lifted to the surface. 
3.3 FEA results of the swab cup carrier and swab mandrel based on computer-aided design 
The structural strength analysis of the Swab Cup Carrier and swab mandrel assembly was performed using the 
finite element analysis (FEA) method through SolidWorks Simulation 2023 software. The simulation was 
conducted to evaluate the stress distribution within the assembly and to identify critical regions with potential

290 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
failure risk.  The equivalent von Mises stress was used as the primary evaluation parameter to compare the induced 
stress with the yield strength of the selected material. 
The simulation results showed that the maximum von Mises stress occurred in the lock screw component, with 
a value of 278.6 MPa. The stress concentration was localized at the thread root area due to geometric discontinuity 
and cross-sectional variation, which generated a stress concentration effect. Since the lock screw exhibited the 
highest stress level compared with the other components, it was identified as the critical component. Accordingly, 
the maximum stress value of 278.6 MPa was used as the design governing stress for the structural evaluation and 
material selection. 
Material selection was performed by considering that the material yield strength must be higher than the design 
governing stress. In addition, the selected material must possess adequate toughness, resistance to repeated loading, 
manufacturability, and suitability for mechanical equipment applications  in oil and gas environments. Based on 
these criteria,  AISI 4130 alloy steel was selected as a candidate material because it provide s a favorable 
combination of strength, toughness, heat-treatability, and fatigue resistance, which supports its use in components 
subjected to tensile, compressive, torsional, and cyclic loading. 
The main mechanical properties of AISI 4130 used in the evaluation are as follows: 
• Yield strength, σᵧ = 460 Mpa 
• Ultimate tensile strength = 560–670 Mpa 
• Maximum von Mises stress, σmax = 278.6 MPa 
• The factor of safety against yielding was calculated using the following Equations 1 and 2 
𝐹𝑜𝑆 =
𝜎𝑦
𝜎𝑚𝑎𝑥  =
460
278,6 = 1,65            (1) 
therefore, 
278,6 𝑀𝑃𝑎 <  460 𝑀𝑃𝑎                  (2) 
These results indicate that the maximum stress remains below the yield strength of AISI 4130 and produces a 
static factor of safety of 1.65. Based on the boundary conditions and loading conditions applied in the simulation, 
the model theoretically remains within the elastic region and does not experience plastic deformation. 
In addition to satisfying the initial static strength requirement, AISI 4130 also has severa l characteristics that 
support its application in swabbing equipment, including relatively high mechanical strength, good toughness, 
fatigue resistance, heat-treatment capability, and widespread use in oilfield components such as tool joints, subs, 
connectors, and other downhole components. 
 
 
Figure 6.  
Finite Element Analysis results of the Swab Cup Carrier and swab mandrel assembly,  
showing the von Mises stress distribution and the maximum stress of 278.6 MPa at the lock-screw thread-root area.  
(Authors’ simulation using SolidWorks Simulation).

291 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
Nevertheless, the factor of safety value of 1.65 should be further evaluated against the applicable design criteria 
or minimum standard requirements. The final material selection should also consider fatigue analysis, corrosion, 
temperature, well fluid conditions, heat treatment, dynamic loading, and material standards for downhole 
equipment. Therefore, the FEA results in this study should be regarded as an initial structural evaluation and do 
not replace validation through material testing or testing under actual operating conditions. 
3.4 Prototype development and functional testing using a mock-up tubing model 
Prototype development and mock-up tubing testing were conducted to evaluate geometric conformity, inter-
component connectivity, and the preliminary functionality of the cam -guided release-and-carry mechanism. The 
Swab Cup Carrier and swab mandrel prototypes were fabricated using the fused filament fabrication method with 
a Creality K1 Max 3D printer and PLA+ filament. 
• Prototype Development Results of the Swab Cup Carrier and Swab Mandrel 
The Swab Cup Carrier and swab mandrel prototypes were successfully fabricated based on the Computer -
Aided Design model. The main components produced include d the Swab Cup Carrier, swab mandrel, ring, 
cam groove, guide pin, and connection sections. Each component was printed separately to facilitate 
inspection, assembly, and evaluation of the mechanical interaction between components. 
As shown in Figure 7, the primary geometry of the prototype was successfully realized in accordance with 
the CAD design. The Swab Cup Carrier and swab mandrel components could be assembled into an 
integrated mechanical unit, while the guide pi n was able to move along the cam groove trajectory. This 
condition enabled the evaluation of the mechanism position transition between the release and carry states.  
From visual and functional perspectives, the prototype demonstrated conformity in shape and configuration 
with the initial design. Nevertheless, the use of PLA+ filament was limited to geometric validation, 
assembly evaluation, and preliminary mechanical function testing. The prototype was not intended to 
represent structural strength, pressure resistance, temperature resistance, corrosion resistance, wear 
resistance, or actual downhole loading conditions. 
 
 
 
 
Figure 7.  
Assembly of the 3D-printed Swab Cup Carrier and swab mandrel prototype used to evaluate component fit,  
guide-pin movement, and mechanical engagement.  (Author’s documentation, Product manufactured  
by Creality K1 Max 3D printer and PLA+ filament). 
 
 
• Functional testing results using a mock-up tubing model 
Functional testing was conducted using a mock-up tubing model consisting of 4-inch and 3-inch Polyvinyl 
Chloride (PVC) pipes. The two pipes were assembled to form a diameter transition area that provides a 
simplified representation of the X-over configuration in a dual-size tubing completion. A specific section of 
the mock-up was made open to allow visual monitoring of the Swab Cup Carrier and swab mandrel positions 
during the Run In Hole and Pull Out of Hole stages. 
As shown in Figure 8, the prototype assembly was able to move through the 4-inch pipe toward the X-over 
area. During the Run In Hole stage, the Swab Cup Carrier reached the release position and remained retained 
at the transition area, while the swab mandrel was able to continue moving toward the 3 -inch pipe section.

292 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
During the Pull Out of Hole stage, the swab mandrel re -entered the Swab Cup Carrier, and the guide pin 
moved along the cam groove trajectory until it reached the carry position. After reconnection was 
achieved, the Swab Cup Carrier could be retrieved together with the swab mandrel toward the up per 
section of the mock -up. 
The test results showed that the release -and-carry sequence could be performed in accordance with the 
proposed design concept. No mechanical obstruction causing movement failure was observed during the 
tested stages. These results provide preliminary validation of the functional feasibility of the cam -guided 
release-and-carry mechanism. 
The field -scale mechanism simulation was carried out under simplified conditions using 4 -inch and 3 -
inch PVC pipes. A monitoring window was provided to observe the position of the Swab Cup Carrier and 
swab mandrel during Run In Hole (RIH) and Pull Out of Hole (POOH), as shown in Figure 8 . This 
arrangement enabled direct visual assessment of whether the tool could operate according to the inten ded 
working mechanism.  
The tool preparation procedure prior to operation was conducted as follows: 
• Installation of the Swab Cup into the Swab Cup Carrier 
• Insert the Swab Cup into the Swab Cup Carrier. 
• Secure the Swab Cup using the top nut. 
• Insert the Swab Cup Carrier into the Swab Cup Mandrel. 
• Install the swab mandrel into the slickline tool string assembly. 
• The Swab Cup Carrier and swab mandrel assembly is ready to be operated during Run in Hole. 
The Run in Hole and Pull Out of Hole procedures were performed as follows: 
• Run the tool assembly into the hole until it reaches the 4.5-inch × 3.5-inch tubing X-over depth. The 
X-over position is indicated by a reduction in the tool string weight. 
• Pull the tool string upward until the normal pulling weight is observed, approximately ±1 ft, to 
activate the leave-and-carry system of the 4.5-inch Swab Cup. 
• Continue running the 3.5-inch Swab Cup assembly down to the target depth, approximately 50 m to 
100 m below the fluid level. 
• Pull the assembly upward to perform swabbing. As the assembly approaches the X-over area, the 
pulling speed is reduced to allow the swab mandrel to re-enter the Swab Cup Carrier. The assembly is 
then pulled further upward to the surface or lubricator. 
The testing results only validate the movement sequence and mechanical interaction of the prototype. The  
test did not  evaluate sealing pressure, fluid -lifting capacity, fluid  bypass percentage, actual  pulling force, 
temperature effects, or dynamic downhole conditions. Therefore, further testing using actual engineering 
materials and a more representative testing facility is still required. 
3.5 Analysis of the working mechanism of the modified design 
The working mechanism of the modified design was analyzed based on the swa bbing operation sequence in 
wells with a dual size tubing completion configuration, consisting of 4.5-inch tubing in the upper section and 3.5-
inch tubing in the lower section. The analysis focused on the operating sequence of the 3.5-inch and 4.5-inch Swab 
Cups in maintaining the continuity of fluid lifting across the tubing diameter transition area or X-over. 
During the Run In Hole stage, the 3.5 -inch and 4.5-inch Swab Cups are lowered simultaneously as part of a 
single assembly. When the assembly reaches the X-over area from the 4.5-inch tubing section toward the 3.5-inch 
tubing section, the 4.5-inch Swab Cup Carrier is guided into the release position and temporarily retained at the 
transition area. Meanwhile, the swab mandrel and the 3.5 -inch Swab Cup remain able to move downward until 
they reach the lower section of the fluid level to be lifted. 
During the Pull Out of Hole stage, the 3.5-inch Swab Cup lifts fluid from the lower tubing section toward the X-
over area. When the swab mandrel re-engages with the 4.5-inch Swab Cup Carrier, the guide pin moves along the

293 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
cam groove trajectory until the mechanism reaches the carry position. The 4.5 -inch Swab Cup Carrier then 
reconnects with the swab mandrel and is retrieved toward the surface. 
As the assembly enters the 4.5 -inch tubing section, the fluid -lifting function is transferred from the 3.5 -inch 
Swab Cup to the 4.5 -inch Swab Cup. This  mechanism establishes the principle of transfer lifting, in which the 
lifting function is transferred according to the tubing diameter being traversed.  The 3.5-inch Swab Cup operates 
in the lower tubing section, while the 4.5-inch Swab Cup maintains sealing contact in the upper tubing section. 
The cam groove functions as a guide path for the guide pin to control the positional transition of the Swab Cup 
Carrier between the release and carry conditions. Therefore, the cam groove does not function as a sealing element 
or as a radial deformation zone. The sealing function is still provided by the elastomeric element of the 4.5 -inch 
Swab Cup, whose dimensions are matched to the inner diameter of the upper tubing section. 
The mock-up tubing test results showed that the release sequence during Run In Hole and the carry sequence 
during Pull Out of Hole could be performed in accordance with the design concept. This  mechanism enables the 
4.5-inch Swab Cup Carrier to be temporarily retained at the X-over area, th en re -engaged and retrieved to the 
surface without removing the lubricator during each operating cycle, as shown in Figure 9. 
Conceptually, the combination of the transfer lifting mechanism, cam groove, guide pin, and cam-guided 
release-and-carry system has the potential to maintain fluid -lifting continuity in dual size tubing completion 
configurations. Nevertheless, the present testing remains limited to mechanical motion validation. The ability of 
the design to mainta in sealing pressure, reduce fluid bypass, and improve liquid -lifting efficiency still requires 
further testing using actual engineering materials and more representative operating conditions. 
3.6 Engineering implications and potential implementation 
The results of the design development indicate that the 4.5-inch Swab Cup Carrier with a cam-guided release-
and-carry mechanism has potential applicability in swabbing operations for wells with dual size tubing completion. 
This design was developed to address sealing loss and fluid bypass that occur  when the tool assembly moves 
through the transition area from the 3.5-inch tubing section into the 4.5-inch tubing section. 
 
 
 
 
 
Figure 8.  
Functional testing of the Swab Cup Carrier and swab mandrel using a PVC mock-up tubing model.  
The test demonstrates carrier release at the X-over during Run In Hole and carrier reconnection during Pull Out of Hole.  
(Author’s documentation, Swab Cup Carrier Prototype manufactured by Creality K1 Max 3D printer and PLA+ filament and 
PVC mock up tubing was handmade).

294 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
 
 
Figure 9.  
Guide-pin positions along the cam-groove trajectory during Run In Hole and Pull Out of Hole, illustrating the transition 
between the release and carry positions.  (Authors’ illustration made by Solidwork 2023 software). 
 
From an engineering perspective, the modified design employs two Swab Cup sizes that operate sequentially 
according to the tubing diameter. The 3.5-inch Swab Cup functions to lift fluid from the lower tubing section, while 
the 4.5-inch Swab Cup continues the lifting process in the upper tubing section. This transfer lifting mechanism 
has the potential to maintain the continuity of fluid lifting up to the surface. 
The cam groove on the Swab Cup Carrier functions as a guide path for the guide pin to control the mechanism 
transition between the release and carry positions. During the Run In Hole stage, the 4.5-inch Swab Cup Carrier 
can b e released and temporarily retained at the X -over area. During the Pull Out of Hole stage, the carrier 
reconnects with the swab mandrel and is retrieved toward the surface. The sealing function remains provided by 
the 4.5-inch Swab Cup element, which is dimensionally matched to the inner diameter of the upper tubing section. 
This mechanism offers potential operational advantages because the carrier release and retrieval process  can 
be performed within a single operating sequence without removing the lubricator in each cycle.  Therefore, the 
proposed design has the potential to support swabbing operations that are more practical, continuous, and efficient 
in terms of operating time. 
From a manufacturing perspective, the main components, including the ring, main body, cam groove, guide 
pin, lock screw, and swab mandrel, can be produced using Computer Numerical Control machining. The modular 
configuration also facilitates fabrication, inspection, maintenance, and component replacement in th e event of 
wear or damage. 
The FEA results indicate that the design theoretically remains below the yield strength of AISI 4130 under the 
analyzed static loading condition. In addition, prototype testing using the mock -up tubing model provides 
preliminary validation that the  release-and-carry sequence can be performed in accordance with the design 
concept. Nevertheless, the test has not yet demonstrated sealing performance, fluid-lifting capacity, or quantitative 
fluid bypass reduction. 
Further research is required through more comprehensive FEA, including mesh convergence, contact analysis, 
fatigue analysis, dynamic loading, and variation of loading conditions. Laboratory testing using actual engineering 
materials is also necessary to evaluate sealing pressure, pulling force, wear resistance, fluid compatibility, 
temperature effects, and fluid-lifting performance prior to field validation. 
Overall, the combination of the cam-guided release-and-carry mechanism and the transfer lifting function from 
the 3.5-inch Swab Cup to the 4.5 -inch Swab Cup offers a potential engineering approach  for dual size tubing 
completion applications. With further validation, this design can serve as a basis for developing more adaptive 
swabbing equipment suitable for liquid unloading operations in wells with tappered tubing configurations.

295 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
4. Conclusion 
This study successfully developed a modified design of a 4.5 -inch Swab Cup Carrier and swab mandrel for 
swabbing applications in wells with dual size tubing completion, consisting of 3.5-inch tubing in the lower section 
and 4.5-inch tubing in the upper section. The design was developed to address sealing loss and potential fluid bypass 
occurring at the tubing diameter transition area or X-over. 
The proposed concept employs two Swab Cup sizes within a single assembly, integrated with a cam -guided 
release-and-carry mechanism. During the Run In Hole stage, the 4.5 -inch Swab Cup Carrier is released and 
temporarily retained at the X-over area, while the 3.5-inch Swab Cup moves downward toward the lower section of 
the fluid level. During the Pull Out of Hole stage, the 3.5-inch Swab Cup lifts fluid from the lower tubing section, 
after which the 4.5 -inch Swab Cup Carrier reconnects with the swab mandrel and continues t he lifting process 
through the upper tubing section. The FEA results showed that the maximum von Mises stress of 278.6 MPa occurred 
in the lock screw component. This value remains below the yield strength of AISI 4130, which is 460 MPa, and 
results in a static factor of safety of 1.65. Based on the boundary conditions and loading conditions applied in the 
simulation, the design theoretically remains within the elastic region and does not experience plastic deformation. 
The Swab Cup Carrier and swab mandrel prototypes fabricated using PLA+-based 3D printing were successfully 
assembled and tested using a PVC mock -up tubing model. The functional testing results showed that the release 
mechanism during Run In Hole and the carry mechanism during Pull Out of Hole could be performed in accordance 
with the design concept. These findings provide preliminary validation of the geometric and mechanical feasibility 
of the proposed design. 
Overall, the modified design has the potential to maintain movement continuity and transfer lifting in dual size 
tubing completion configurations. However, this study has not yet evaluated sealing performance, fluid -lifting 
capacity, or quantitative fluid bypass reduction. Therefore, further research is required through fatigue and 
dynamic loading analysis, pressure and sealing tests, fabrication using actual engineering materials, and laboratory 
and field validation. 
 
5. Acknowledgement 
The author would like to express sincere gratitude to Petroleum Engineering Lecturers, Institut Teknologi 
Bandung, especially for my research supervisors for the academic support provided throughout this research. 
Appreciation is also extended to the parties in Field Hantatun for providing access to operational data, technical 
information, and valuable input during the development of the Swab Cup Carrier design for swabbing operations 
in wells with dual size tubing completion. The author also expresses appreciation to the supervisors and 
professional colleagues for their guidance, technical discussions, and constructive suggestions that supported the 
completion of this paper. 
6. Declarations 
6.1 Author contributions 
Karnando: Conceptualization, Methodology, Formal Analysis, Investigation, Data Curation, Visualization, 
Writing – Original Draft, and Writing – Review & Editing. Dedy Irawan: Supervision, Validation, and Writing – 
Review & Editing. Amega Yasutra: Supervision, Validation, and Writing – Review & Editing. All authors have 
read and approved the final manuscript. 
6.2 Funding statement 
This research received no external funding.

296 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
6.3 Competing interest 
A patent application related to the Swab Cup Running Tool described in this manuscript is being considered. 
The authors declare no other financial or non-financial competing interests. 
6.4 The use of AI or AI-assisted technologies 
During the preparation and revision of this manuscript, the first author used ChatGPT to assist with language 
editing. All AI -assisted content was subsequently reviewed and edited by the authors. The authors take full 
responsibility for the accuracy, integrity, and final content of the manuscript. 
 
7. Glossary of terms and symbols 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Terms & 
Symbol Definition Unit 
3D Three-dimensional. - 
AISI American Iron and Steel Institute  - 
AISI 4130 Chromium–molybdenum low-alloy steel  - 
CAD Computer-Aided Design - 
CNC Computer Numerical Control - 
FEA Finite Element Analysis - 
FoS Factor of Safety Dimensionless 
ID Inner Diameter inch 
NBR Nitrile Butadiene Rubber - 
OD Outer Diameter inch 
PLA+ Modified polylactic acid filament  - 
POOH Pull Out of Hole - 
PVC Polyvinyl Chloride - 
RIH Run In Hole - 
σᵧ Yield strength MPa 
σmax Maximum equivalent von Mises stress MPa 
Ø Diameter inch 
R Radius  inch 
± Plus–minus - 
× Multiplication or dimensional-transition symbol - 
° Degree  degree 
MPa Megapascal, equal to 10610^6106 pascals MPa 
in Inch inch 
ft Foot ft 
m Metre m 
R1.000 Cam groove path radius of 1.000 inch. inch 
R1.750 Cam groove path radius of 1.750 inches. inch 
180° 
Angular arrangement in which the two pairs of 
cam grooves are positioned symmetrically 
opposite each other. 
degree

297 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
8. References 
Abhulimen, K. E., Abhulimen, K. E., & Oladipupo, A. D. (2023). Modelling of liquid loading in gas wells using 
a software -based approach. Journal of Petroleum Exploration and Production Technology, 13 , 1 –17. 
https://doi.org/10.1007/s13202-022-01525-x 
Ash-Shidiq, M. R., et al. (2025). Successful wellbore fluid unloading using locally manufactured swab cups for 
underbalance perforation: Swabbing operation case study from the Nubi -Mahakam Field, Indonesia. 
SPE/IATMI Asia Pacific Oil & Gas Conference and Exhibition . SPE-226527-MS. 
https://doi.org/10.2118/226527-MS 
Bourgoyne, A. T., Millheim, K. K., Chenevert, M. E., & Young,  F. S. (1991). Applied drilling engineering (2nd 
printing). Society of Petroleum Engineers. https://doi.org/10.2118/9781555630010 
Budynas, R. G., & Nisbett, J. K. (2020). Shigley’s mechanical engineering design (11th ed.). McGraw -Hill 
Education. McGraw-Hill book page  (https://www.mheducation.com.sg/shigley-s-mechanical-engineering-
design-11th-edition-si-units-9789813158986-asia-group) 
CANAM Pipe & Supply. (2018). Swab Cups – TA Style. CANAM Pipe & Supply. CANAM – Swab Cups TA 
Style PDF 
Chemmakh, A., Tomomewo, O. S., Ling, K., &  Shammari, A. (2023). Evaluation of liquid loading  in gas wells 
using machine learning. Petroleum & Petrochemical Engineering Journal, 7(1), 1 –11. 
https://doi.org/10.23880/ppej-16000333 
Economides, M. J., Hill, A. D., & Ehlig-Economides, C. (1994). Petroleum production systems. 
Elyasa, A., Hassan, A., Mahmoud, M., Gajbhiye, R., El -Husseiny, A., & Abu-Mahfouz, I. S. (2024). Mitigating 
liquid loading in gas wells using thermochemical fluid injection: An experimental and simulation study. ACS 
Omega, 9(28), 31081–31092. https://doi.org/10.1021/acsomega.4c04423 
Hamzah, K., Yasutra, A., & Irawan, D. (2021). Prediction of hydraulic fractured well performance using empirical 
correlation and machine learning. Scientific Contributions Oil and Gas, 44 (2), 141 –152. 
https://doi.org/10.29017/SCOG.44.2.589 
He, F., Huang, X., Yang, Y., Bu, C., Xing, H., Pu , L., & Zhang, S. (2024). Review on critical liquid loading 
models and their application in deep unconventional gas reservoirs. Frontiers in Energy Research, 12 , 
1407384. https://doi.org/10.3389/fenrg.2024.1407384 
Lea, J. F., Nickens, H. V., & Wells, M. R. (2003). Gas well deliquification: Solutions to gas well liquid loading 
problems. Gulf Professional Publishing. https://doi.org/10.1016/B978-0-7506-7724-0.X5000-5 
Lyons, W. C., & Plisga, G. J. (2004). Standard handbook of petroleum and natural gas engineering (2nd ed.). 
Gulf Professional Publishing. https://doi.org/10.1016/B978-0-7506-7785-1.X5011-8 
Maurenza, F., Yasutra, A., & Tungkup, I. L. (2023). Production forecasting using Arps decline curve model with 
the effect of artificial lift installation. Scientific Contributions Oil and Gas, 46 (1), 9 –18. 
https://doi.org/10.29017/SCOG.46.1.1310  
Musnal, A., & Melysa, R. (2023). Analy sis of Liquid Loading and Sandness in Gas Wells A1, A2 and Their 
Correction with the Plunger Lift Method in Field B. Journal of Earth Energy Engineering, 12 (1), 1 –9. 
https://doi.org/10.25299/jeee.2023.11083 
PTR Prentice Hall. Google Books catalog 
Saputra, M. N. W., Permana, I. B., Febryana, N. E., Satrio , A. B., & Wibowo, E. B. (2022). Continuous liquid 
unloading of gas well with high gas/liquid ratio production using electric submersible pump. Proceedings of 
the Indonesian Petroleum Association, 46th Annual Convention & Exhibition (IPA22-E-141). 
https://doi.org/10.29118/ipa22-e-141

298 
 
https://doi.org/10.29017/scog.v49i3.2155 
 
Karnando et al. Scientific Contributions Oil and Gas 
Turnip, J. F., Yasutra, A., Maulana, F., & Mustaqim, S. D. (2024). Mature field and well revitalization: Selection 
of matrix acidizing candidates. Scientific Contributions  Oil and Gas, 47 (1), 65 –74. 
https://doi.org/10.29017/SCOG.47.1.1613  
Virgia, Z., Rusdi, R. K., Umar, K., Kusumah, A. S., & Wahyudi, R. (2022). Thru-tubing ceramic screen application 
to unlock mature sandy well efficiently: Successful implementation in Sisi Nubi Field. Proceeding Simposium 
IATMI 2022, IATMI22-007. https://journal.iatmi.or.id/index.php/ojs/article/view/221
