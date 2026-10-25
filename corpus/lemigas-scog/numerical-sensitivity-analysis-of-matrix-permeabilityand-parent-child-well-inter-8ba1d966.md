---
source_id: "lemigas-scog"
title: "Numerical Sensitivity Analysis of Matrix Permeabilityand Parent Child Well Interaction on Estimated Ultimate R"
summary: "Compositional reservoir simulation study of how matrix permeability and parent-child well interference change estimated ultimate recovery in shale reservoirs."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2114"
retrieved_at: "2026-10-24T14:30:38+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "8ba1d966be57ecbdb62df55644d41fc07c2df3346df4f68ecc302db70fb53315"
collected: "manual"
---

# Numerical Sensitivity Analysis of Matrix Permeabilityand Parent Child Well Interaction on Estimated Ultimate R

1 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 1 – 40 - http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 https://doi.org/10.29017/scog.v49i3.2114 
 
Numerical Sensitivity Analysis of Matrix Permeability 
and Parent–Child Well Interaction on Estimated Ultimate Recovery 
in Unconventional Reservoirs 
 
Dike F. Putra1,2,3*, Ichsan A. Lukman1,4, M. Haidar Putra3,4, Fiki Hidayat1,4, and 
Muhammad Ariyon1,4  
 
1Petroleum Engineering Department, Engineering Faculty, Universitas Islam Riau, 
Kaharuddin Nasution No. 113, Perhentian Marpoyan, Marpoyan Damai Subdistrict, 
Pekanbaru City, Riau 28284, Indonesia. 
2Faculty of Chemical and Energy Engineering, Universiti Teknologi Malaysia, 
81310 UTM Johor Bahru Johor, Malaysia. 
3Department of Earth, Energy, and Environment, Faculty of Science, University of Calgary, 
2500 University Drive NW Calgary, AB, Canada. 
4Center of Energy Studies (PSE), Universitas Islam Riau, 
Kaharuddin Nasution No. 113, Perhentian Marpoyan, Marpoyan Damai Subdistrict,  
Pekanbaru City, Riau 28284, Indonesia. 
*Corresponding author: Dike F. Putra (dikefp@eng.uir.ac.id) 
Dike F. Putra: https://orcid.org/0000-0002-6772-130X 
Received:  11 May 2026; Revised in revised form 03 June 2026; Accepted 08 June 2026 
Available online 30 September 2026. 
  
 
ABSTRACT - Unconventional shale reservoirs hold vast hydrocarbon resources, but productivity is constrained 
by ultra -low matrix permeability and complex fracture behavio ur. While horizontal drilling and hydraulic 
fracturing are essential for commercial production, optimizing estimated ultimate recovery (EUR) remains 
challenging due to coupled interactions among permeability, pressure depletion, fracture effectiveness, and well 
interference. This study uses compositional reservoir simulation to numerically investigate how hypothetical 
matrix permeability enhancement and parent -child well interactions affect cumulative gas production.  Models 
were built using Eagle Ford shale properties with multi -stage hydraulic fractures and geomechanical effects. 
Matrix permeability was increased by factors of 10× and 100× relative to the base case, and bottom-hole pressure 
(BHP) was optimized across 100 synthetic scenarios. Results show that matrix permeability is the primary control 
on long-term production, with higher permeability significantly improving  matrix-to-fracture fluid transfer. The 
optimal single-well scenario produced approximately 9.8 × 10⁸ ft³ of gas. Geomechanical analysis revealed uneven 
strain distribution around fractures, indicating non-uniform stress redistribution. In the parent-child configuration, 
strong pressure interference was observed; notably, the child well outperformed the parent well under simulated 
conditions, likely due to greater pressure drawdown and enhanced fracture connectivity. This study establishes 
theoretical upper-bound recovery limits through hypothetical permeability scenarios rather than proposing field -
ready technologies. The findings emphasize that maximizing EUR requires an integrated evaluation of 
permeability, fracture effectiveness, pressure management, geomechanics, and well spacing. 
Keywords: unconventional reservoir, shale gas, matrix permeability, parent –child well, hydraulic fracturing, 
cumulative production, EUR, geomechanics.

2 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
How to cite this article: 
Dike F. Putra, Ichsan A. Lukman, M. Haidar Putra, Fiki Hidayat, and Muhammad Ariyon, 2026, 
Numerical Sensitivity Analysis of Matrix Permeability and Parent –Child Well Interaction on 
Estimated Ultimate Recovery in Unconventional Reservoirs, Scientific Contributions Oil and Gas, 
49 (3) pp. 1-40.  
 
 
 
1. Introduction 
The increasing global demand for energy and the decline of conventional hydrocarbon reserves have 
accelerated the development of unconventional resources such as shale gas and shale oil reservoirs. Among 
unconventional resources, shale formations are among  the largest potential energy sources due to their 
extensive areal distribution and substantial hydrocarbon content. However, shale reservoirs are characterized 
by ultra-low matrix permeability, nanoscale pore systems, low porosity, complex natural fractur es, and strong 
geomechanical heterogeneity, which significantly restrict hydrocarbon mobility and production performance 
(Fan et al., 2018) . Typical shale permeability ranges from the nano -Darcy to the micro -Darcy scale, causing 
hydrocarbons to remain trapped within the organic -rich matrix. Consequently, commercial production from 
shale reservoirs strongly depends on advanced technologies suc h as horizontal drilling and multi -stage 
hydraulic fracturing (King et al., 20 10). 
Unlike conventional reservoirs, shale formations commonly serve as source rock, reservoir rock, and seal rock 
simultaneously, resulting in unique hydrocarbon storage and flow mechanisms that require advanced stimulation 
technologies for commercial producti on (Junira & Wibowo 2016) . In addition, shale formations generally have 
permeability below 0.1 mD and porosity below 10%, making natural hydrocarbon flow extremely difficult without 
stimulation technologies (Junira & Wibowo 2016) . Therefore, horizontal drilling and hydraulic fracturing have 
become the primary methods for increasing reservoir contact area and improving hydrocarbon productivity from 
shale formations (King et al., 2010; Junira & Wibowo 2016). Experience from unconventional developments in 
North America further indicates that fracture -network complexity, hydraulic -fracture conductivity, and 
geomechanical behavior are key parameters that control the sustainability of shale production (Winderasta 2017). 
Hydraulic fracturing is applied to establish highly conductive flow pathways between the reservoir matrix 
and the wellbore through the creation of complex fracture networks that enlarge the stimulated reservoir volume 
(SRV). The effectiveness of these hydr aulic fractures is strongly influenced by fracture conductivity, stress 
redistribution, fracture propagation behavior, and matrix –fracture interaction (Taghichian et al., 2018) . In 
unconventional reservoirs, the primary objective is to maximize the contact area between the fracture system 
and the reservoir while maintaining economic feasibility. Therefore, understanding the interaction between 
hydraulic fractures, matrix permeab ility, and geomechanical behavior is essential for improving estimated 
ultimate recovery (EUR).  
Matrix permeability is recognized as one of the most influential parameters controlling long -term shale 
production performance. Although hydraulic fractures dominate early-time production, hydrocarbon transfer from 
the matrix toward the fracture network governs long-term recovery. Fan et al. (2018) emphasized that accurately 
determining shale matrix permeability remains a significant challenge because induced microfractures during core 
retrieval and transportation can alter laboratory permeability measurements. This uncertainty may lead to 
inaccurate forecasting of production performance and reservoir recovery.  
Hydraulic-fracture propagation is also strongly influenced by reservoir stress conditions and geomechanical 
behavior. Warpinski & Teufel (1987)  demonstrated that in situ stress conditions are the dominant factors 
controlling fracture propagation, compared with lithological boundaries and variations in elastic properties. 
Similarly, King (2010) explained that stress redistribution surrounding hydraulic fractures may significantly alter 
fracture geometry and long-term production behavior. Therefore, understanding the interaction between hydraulic 
fractures and geomechanical deformation is essential for improving shale recovery performance.

3 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The orientation of hydraulic fractures is strongly affected by the intersection angle between the wellbore 
trajectory and the principal horizontal stress direction. Lolon et al. (2009)  demonstrated that fracture spacing, 
fracture conductivity, and horizontal well orientation significantly affect production performance in 
unconventional formations. In addition, Le Calvez et al. (2007) showed that microseismic monitoring can provide 
valuable insight into fracture propagation and stress evolution during stimulation treatments. These findings 
indicate that successful unconventional reservoir development requires an integrated understandin g of hydraulic 
fracturing and reservoir geomechanics. 
Recent developments in unconventional reservoir engineering have highlighted that parent –child well 
interaction is controlled not only by well spacing but also by fracture -driven communication, depletion shadow, 
and stress redistribution around pre-existing wells. Wang et al. (2021) reported that pressure interference between 
parent and child wells can significantly alter production performance and EUR prediction, particularly in tightly 
spaced unconventional developments. Similarly, Liu et al. (2026)  demonstrated that fracture -hit behaviour 
becomes increasingly severe under tight well -spacing conditions, leading to dynamic fracture propagation and 
pressure communication between adjacent wells.  
The Eagle Ford shale reservoir, located in South Texas, United States, was selected as the case study in this 
research because it represents one of the most productive unconventional shale plays in North America. Eagle 
Ford shale has experienced rapid development following the success of Barnett, Haynesville, and Marcellus shale 
reservoirs (Tian et al., 2014). According to the U.S. Energy Information Administration (U.S. Energy 2011), the 
Eagle Ford shale contains approximately 21 Tcf of recoverable natural gas and 3 billion barrels of recoverable oil. 
The reservoir depth ranges from 2,500 to 14,000 ft, while permeability varies between 1 and 800 nano -Darcy 
(Inamdar et al., 2010 ; Stegent et al., 2010) . These characteristics make Eagle Ford shale highly sensitive to 
hydraulic-fracture design, pressure depletion, and reservoir-stimulation strategies. 
Several previous studies have investigated the influence of matrix permeability, stimulated reservoir volume, 
and fracture conductivity on the performance of unconventional reservoirs. While Al-Rbeawi & Al-Kaabi (2020) 
demonstrated that stimulated matrix permeability and non -Darcy fracture flow significantly influence pressure 
depletion and the productivity index, their study did not consider geomechanical coupling or parent -child well 
interactions, leaving key questions about coupled effects unanswered. Cipolla (2009) further showed that reducing 
fracture spacing can substantially improve gas recovery by increasing fracture-network complexity and reducing 
matrix drainage distance. Modern studies have also revealed that gas transport mechanisms in shale reservoirs 
differ substantially from those in conventional Darcy -flow systems due to nanopore confinement and stress -
sensitive permeability behaviour. 
Recent geomechanical studies have emphasized that permeability evolution and fracture conductivity may 
change dynamically during depletion processes. Bui (2023)  explained that stress -sensitive permeability and 
fracture-conductivity degradation are critical parameters that control long -term unconventional reservoir 
productivity. Similarly, Heydari et al. (2024) demonstrated that geomechanical deformation and reactive transport 
processes within shale microfractures can alter fracture aperture and the evolution of permeability during 
production depletion.  
The objective of this study is not to propose a field -scale permeability enhancement technology. Instead, the 
work investigates hypothetical permeability multipliers as numerical sensitivity scenarios to quantify theoretical 
upper-bound recovery limits and understand the relative contribution of matrix-to-fracture mass transfer on long-
term shale production. 
This study presents a comprehensive, integrated simulation framework for unconventional shale reservoirs 
that simultaneously evaluates hypothetical matrix permeability enhancement, BHP optimisation, anisotropic 
geomechanical behaviour, and parent –child well interference within a unified Eagle Ford shale model. Unlike 
previous studies that investigated these parameters separately, this work quantitatively evaluates the coupled 
relationship between matrix -flow capacity, stress redistribution, fracture -driven communication, and long -term 
cumulative production performance. The study also provides insight into the interaction between shear -strain 
evolution and production imbalance in parent–child well configurations.

4 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
1.1 Literature review 
Although matrix permeability enhancement has frequently been investigated in numerical studies, achieving 
uniform permeability increases of one or two orders of magnitude in field -scale shale formations remains 
technically challenging. Therefore, the prese nt work does not propose a deployable permeability enhancement 
technology. Instead, matrix permeability multipliers are employed as hypothetical numerical sensitivity scenarios 
to establish theoretical recovery limits and investigate the contribution of ma trix-to-fracture mass transfer under 
various depletion conditions. 
Shale reservoirs are categorized as unconventional hydrocarbon resources due to their ultra-low permeability, 
nano-scale pore structures, and highly heterogeneous rock properties. Despite containing enormous hydrocarbon 
potential, shale formations generall y exhibit poor natural productivity because fluid mobility within the matrix 
system is extremely limited (Fan et al., 2018). Therefore, advanced stimulation technologies, such as horizontal 
drilling and hydraulic fracturing, are required to achieve economically sustainable production (King et al., 2010).  
Junira & Wibowo (2016) explained that shale reservoirs differ significantly from conventional reservoirs as 
they simultaneously act as source rock, reservoir rock, and seal rock. In addition, shale reservoirs commonly have 
permeability below 0.1 mD and porosity below 10%, making hydrocarbon extraction extremely difficult without 
artificial stimulation. The study emphasized that horizontal drilling and hydraulic fracturing are the key 
technologies enabling commercial shale development worldwide. Furthermore, lessons learned from North 
American unconventional developments indicate that fracture-network complexity and stimulation effectiveness 
are critical factors governing the sustainability of shale production (Winderasta 2017). 
Matrix permeability governs the rate of hydrocarbon transfer from the nanoporous shale matrix to the 
hydraulic-fracture network and therefore represents a critical parameter controlling long -term unconventional 
reservoir recovery. Although hydraulic fractures create highly conductive flow pathways, the shale matrix remains 
the primary hydrocarbon storage medium. Consequently, hydrocarbon recovery strongly depends on the matrix's 
ability to transport fluids toward the fracture network. Although Fan et al. (2018)  emphasized the challenge of 
accurately measuring permeability, their study did not evaluate how uncertainty in matrix permeability affects 
EUR predictions across various well-spacing scenarios.  
Modern studies have also reported that gas transport mechanisms in shale reservoirs differ substantially from 
those in conventional Darcy -flow systems due to nanoscale pore confinement and stress -sensitive permeability 
behaviour. Ghanbarian et al. (2020)  demonstrated that gas relative permeability in unconventional reservoirs is 
strongly influenced by nano-pore structures and pressure-dependent permeability evolution. The study indicated 
that unconventional gas-flow behaviour may deviate significantly from conventional flow assumptions, especially 
during depletion processes in ultra-tight formations. 
Hydraulic fracturing creates SRV, which becomes the main productive region surrounding the horizontal 
wellbore. The performance of the SRV depends on fracture conductivity, fracture spacing, stress redistribution, 
and matrix-fracture interaction. Taghichian et al. (2018) reported that fracture propagation and fracture aperture 
behaviour are strongly controlled by stress conditions and rock toughness. Similarly, Lolon et al . (2009) 
demonstrated that horizontal well orientation, fracture spacing, and fracture conductivity significantly affect 
unconventional reservoir productivity. 
Several studies have investigated the influence of fracture spacing and fracture -network complexity on shale 
production performance. Cipolla (2009) demonstrated that reducing fracture spacing substantially improves gas 
recovery by accelerating hydrocarbon drainage from the matrix toward the fracture network. The study also 
suggested that highly complex fracture networks may partially compensate for u ltra-low matrix permeability 
conditions. Al-Rbeawi & Al-Kaabi (2020)  further developed a hybrid unconventional reservoir model 
incorporating anomalous diffusion, stimulated matrix permeability, and non -Darcy fracture flow. Their results 
demonstrated that increasing stimulated matrix permeability significantly reduces press ure drop and improves 
productivity index.

5 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Geomechanical behaviour is another important factor controlling fracture propagation and long -term 
production sustainability in unconventional reservoirs. Warpinski & Teufel (1987) explained that in situ stress 
conditions are the dominant factors governing hydraulic fracture propagation, compared with lithological 
discontinuities or variations in elastic properties. King (2010) also reported that hydraulic fracturing may alter 
local stress conditions and redistribute stress around the fracture network, potentially affecting fracture 
conductivity during long-term production. 
Recent geomechanical studies have emphasized that permeability evolution and fracture conductivity change 
dynamically during reservoir depletion. Bui (2023)  explained that stress -sensitive permeability and fracture -
conductivity degradation are critical parameters that control long -term unconventional reservoir productivity. 
Similarly, Heydari et al. (2024)  demonstrated that geomechanical deformation and reactive transport processes 
within shale microfractures can alter fracture aperture and the evolution of permeability during production 
depletion. These findings indicate that geomechanical deformation stro ngly influences fluid-flow behaviour and 
fracture sustainability in unconventional reservoirs. 
Real-time fracture monitoring has also become increasingly important for evaluating the effectiveness of 
hydraulic fracturing and the evolution of stress. Le Calvez et al. (2007)  demonstrated that microseismic 
monitoring can provide valuable information on fracture propagation and reservoir stress redistribution during 
hydraulic fracturing operations. Such monitoring technologies are useful for optimizing fracture geometry, 
fracture spacing, and stimulation efficiency. 
Another major challenge in unconventional reservoir development is parent –child well interference. Parent 
wells refer to existing producing wells, while child wells are newly drilled infill wells located near depleted parent 
wells. As unconventional develo pments become denser, hydraulic fractures from adjacent wells may interact, 
creating fracture -driven communication or “frac -hit” phenomena. Wang et al. (2021)  reported that pressure 
communication between parent and child wells significantly affects production forecasting and EUR optimization 
in unconventional reservoirs. Similarly, Liu et al. (2026)  demonstrated that fracture -hit behaviour becomes 
increasingly severe under tight well-spacing conditions, leading to dynamic fracture interactions and production 
interference between adjacent wells. 
1.2 Parent–Child Well Interference mechanism 
Parent–child well interaction has become one of the most critical technical challenges in modern 
unconventional reservoir development. As shale developments mature, operators increasingly adopt infill drilling 
strategies, placing new horizontal wells (chil d wells) adjacent to previously producing wells (parent wells) to 
maximize reservoir contact and improve field recovery. However, long -term production from parent wells alters 
the reservoir pressure distribution and local stress state, which may significan tly influence the performance of 
subsequently drilled child wells. Consequently, the production behaviour of child wells is controlled not only by 
well spacing but also by complex interactions involving depletion shadow, stress shadow, fracture shielding, and 
fracture-driven communication mechanisms (Wang et al., 2021). 
Parent–child well interaction has become one of the most critical technical challenges in modern 
unconventional reservoir development. As shale developments mature, operators increasingly adopt infill 
drilling strategies, placing new horizontal wells (chil d wells) adjacent to previously producing wells (parent 
wells) to maximize reservoir contact and improve field recovery. However, long -term production from parent 
wells alters the reservoir pressure distribution and local stress state, which may significan tly influence the 
performance of subsequently drilled child wells. Consequently, the production behaviour of child wells is 
controlled not only by well spacing but also by complex interactions involving depletion shadow, stress 
shadow, fracture shielding,  and fracture-driven communication mechanisms (Wang et al., 2021 ; Ajisafe et al., 
2019; Wang et al., 2021) . 
In addition to pressure depletion, production from the parent well also modifies the local geomechanical 
environment through stress shadow development. Reservoir pressure reduction increases effective stress in the 
rock matrix and alters the distribution of minimum horizontal stress surrounding existing hydraulic fractures. As

6 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
depletion progresses, the local stress field becomes increasingly heterogeneous, potentially affecting the 
propagation path of fractures generated during child -well stimulation. Soliman et al. (2019)  reported that 
depletion-induced stress changes can significantly influence fracture geometry and stimulation efficiency, 
particularly in tightly spaced unconventional developments where hydraulic fractures from adjacent wells are 
likely to interact. Conse quently, the performance of child wells depends not only on reservoir pressure but also 
on the evolving geomechanical conditions shaped by the parent well's production history. 
 Another important mechanism is fracture shielding, which occurs when preexisting hydraulic fractures alter 
the local stress field and impede the propagation of newly formed fractures. Under fracture-shielding conditions, 
child-well fractures may be unable to effectively access unstimulated reservoir rock, resulting in reduced 
stimulated reservoir volume (SRV) and lower hydrocarbon recovery. Fracture shielding is  Another important 
mechanism is fracture shielding, which occurs when preexisting hydraulic fractures alter the local stress field and 
impede the propagation of newly formed fractures. Under fracture-shielding conditions, child-well fractures may 
be unable to effectively access unstimulated reservoir rock, resulting in reduced stimulated reservoir vo lume 
(SRV) and lower hydrocarbon recovery. Fracture shielding is particularly severe in densely developed shale plays 
where inter -well spacing is limited and hydraulic fractures from adjacent wells overlap significantly. This 
mechanism has been identified as one of the principal causes of child -well underperformance in many 
unconventional reservoirs (Ajisafe et al., 2019). 
Despite the commonly observed depletion -shadow and fracture -shielding effects, recent studies have 
demonstrated that parent –child interactions do not always result in child -well underperformance. Under certain 
reservoir and completion conditions, depletion -induced stress redistribution may create favourable pathways for 
fracture propagation toward depleted regions surrounding the parent well. This phenomenon is commonly referred 
to as fracture -driven interaction (FDI) or frac -hit behaviour. Wang et al. (2021)  reported that strong pressure 
communication between adjacent wells may significantly alter production performance and reservoir drainage 
patterns. Similarly, Liu et al. (2026) demonstrated that FDI become increasingly severe under tight well-spacing 
conditions, creating highly conductive pathways that promote dynamic communication between neighbouring 
fracture systems. 
Frac-hit events occur when hydraulic fractures generated during child -well stimulation intersect or 
establish hydraulic communication with pre -existing fractures associated with the parent well. Such 
interactions may produce either beneficial or detrimenta l outcomes depending on reservoir conditions, 
completion design, and depletion severity. In many field developments, frac -hit behaviour causes temporary 
production disruption, pressure interference, or accelerated decline of the parent well. However, in so me 
cases, fracture -driven communication may enhance fluid transport efficiency by creating highly conductive 
fracture networks that improve connectivity between the reservoir matrix and hydraulic fractures (Wang et 
al., 2021 ; Liu et al., 2026) . These observations suggest that parent –child well behaviour cannot be interpreted 
solely through depletion -shadow mechanisms but must also consider dynamic fracture propagation and inter -
well communication processes.  
Figure 1  illustrates the principal mechanisms governing parent –child well interactions in unconventional 
reservoirs, including FDI, direct frac -hit communication, indirect hydraulic communication through natural 
fracture networks, and the influence of inter -well sp acing on fracture interference. These mechanisms have 
become increasingly important as operators adopt tighter well spacing and infill -drilling strategies to maximize 
reservoir contact and improve hydrocarbon recovery (Al-Rbeawi 2020). 
As shown in  Figure 1a , FDI may occur when hydraulic fractures generated during child -well stimulation 
propagate toward natural fractures and previously stimulated reservoir volumes associated with the parent 
well. The presence of interconnected natural fracture systems can sig nificantly enhance hydraulic 
communication between adjacent wells, thereby altering pressure distribution and reservoir drainage 
patterns. Wang et al. (2021)  reported that such FDI can substantially influence production performance and 
EUR in unconventional developments.

7 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
Figure 1b  illustrates direct frac -hit behaviour, in which hydraulic fractures generated from the child well 
physically intersect or establish direct communication with pre-existing parent-well fracture systems. Direct frac-
hit events may generate significant pressure interference, temporary production disruption, and changes in fracture 
conductivity. Liu et al. (2026) demonstrated that the severity of frac-hit behaviour increases as inter-well spacing 
decreases, thereby increasing the likelihood of hydraulic communication between neighbouring wells. 
In contrast, Figure 1c  illustrates indirect hydraulic communication, in which pressure interaction occurs 
through interconnected natural fractures and microfracture networks without direct fracture intersections. Under 
these conditions, pressure signals can be transmitted between wells despite the absence of a continuous hydraulic-
fracture connection. Such indirect communication may alter fluid -flow behaviour and influence hydrocarbon 
drainage efficiency over large portions of the stimulated reservoir volume. 
Figure 1d highlights the critical role of well spacing in controlling parent –child well interactions. Excessive 
spacing may result in isolated fracture systems with limited reservoir communication, whereas overly tight 
spacing can promote severe frac -hit behaviour a nd production interference. Intermediate spacing conditions 
generally provide a balance between reservoir contact and manageable fracture communication. Al-Rbeawi 
(2020) demonstrated that well spacing and fracture -cluster spacing are among the most influential parameters 
controlling production performance in unconventional reservoirs. 
Although Figure 1  illustrates several fracture -interaction mechanisms, it does not explicitly represent 
depletion-shadow effects. Depletion shadow is fundamentally a pressure -depletion phenomenon that develops 
when prolonged production from a parent well creates a localized low -pressure region surrounding the 
stimulated reservoir volume. The resulting pressure sink may subsequently influence fracture propagation, 
stress redistribution, and pressure communication during child -well stimulation. Therefore, depletion -shadow 
effects are more  appropriately visualized using reservoir pressure distribution maps rather than fracture 
geometry schematics.  
Collectively, these mechanisms demonstrate that parent –child well performance is governed by a complex 
interaction among hydraulic fractures, natural fractures, pressure depletion, and geomechanical evolution. 
Figure 1. 
Conceptual mechanism governing parent-child well interaction: (a). FDI through natural fractures, 
(b). Direct frac-hit, (c). Indirect hydraulic communication, (d). Well-spacing effect 
(adapted from Roussel et al (2013), Al-Rbeawi (2020), Wang et al. (2021), and Liu et al. (2026).

8 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Consequently, the successful development of unconventional reservoirs requires an integrated evaluation of 
fracture geometry, pressure communication, depletion history, and well -spacing optimization to maximize long-
term hydrocarbon recovery. 
1.3 Depletion shadow and its impact on child well performance 
One of the most widely recognized mechanisms affecting parent –child well performance in 
unconventional reservoirs is the development of a depletion shadow. A depletion shadow refers to the 
localized low -pressure region created around a producing parent wel l as reservoir fluids are continuously 
withdrawn. As production progresses, reservoir pressure declines in the vicinity of the parent well, creating 
a pressure sink that may extend beyond the stimulated reservoir volume and influence nearby infill drilling  
locations (Al-Rbeawi 2020).  
The formation of a depletion shadow affects both reservoir -flow behaviour and geomechanical conditions. 
From a reservoir -engineering perspective, pressure depletion reduces the available reservoir energy that drives 
hydrocarbon flow toward production wells . Consequently, child wells drilled within a depleted region often 
experience lower initial reservoir pressure, reduced productivity, and lower EUR compared with parent wells. 
Numerous field studies have reported significant production degradation in child  wells when infill drilling is 
conducted after substantial depletion of parent wells (Ajisafe et al., 2019; Wang et al., 2021). 
From a geomechanical standpoint, pressure depletion increases effective stress within the rock matrix 
according to Equation 1, 
σ'=σ – αP  (1) 
where σ’, σ, α, and P are effective stress, total stress, Biot coefficient, and pore pressure, respectively.  As pore 
pressure decreases, effective stress increases, resulting in stress redistribution around the parent -well fracture 
network. This phenomenon is commonly referred to as a stress shadow and may significantly alter hydraulic -
fracture propagation during  child-well stimulation. Soliman et al. (2019)  reported that depletion -induced stress 
redistribution can cause fractures generated from child wells to be either attracted to or repelled from previously 
depleted regions, depending on the local stress configuration. 
In addition to pressure depletion and stress redistribution, depletion shadows may promote FDI between parent 
and child wells. The pressure gradient established between newly stimulated child-well fractures and the depleted 
parent-well region may encourage fracture propagation toward the pressure sink. Under such conditions, hydraulic 
communication can develop through direct frac -hit events or indirect pressure communication through natural 
fracture networks. Wang et al. (2021)  and Liu et al. (2026)  demonstrated that these interactions become 
increasingly significant as well spacing decreases and fracture networks become more interconnected. 
Although depletion shadows are commonly associated with child -well underperformance, recent studies 
suggest that under specific reservoir and completion conditions, they may also contribute to temporary production 
enhancement. Severe pressure depletion aro und the parent well may create strong pressure gradients that 
accelerate hydrocarbon transfer toward newly stimulated fracture systems. When combined with FDI and 
favourable geomechanical conditions, this mechanism may result in localized child-well overperformance despite 
reservoir depletion. Therefore, parent –child well behaviour should not be interpreted solely through depletion -
shadow concepts but rather through the coupled effects of pressure depletion, fracture communication, and 
geomechanical evolution. 
Understanding depletion-shadow development is therefore essential for optimising well spacing, completion 
timing, hydraulic fracture design, and long-term unconventional reservoir recovery. Accurate characterization of 
depletion patterns can help operators minimize adverse parent –child interactions while maximizing stimulated 
reservoir volume utilization and hydrocarbon recovery efficiency. 
The complex interplay among depletion shadow, stress shadow, fracture shielding, and FDI highlights the 
importance of integrated reservoir-geomechanical analysis when evaluating parent–child well performance. While

9 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
conventional field experience generally indicates that child wells tend to underperform due to reservoir depletion, 
specific combinations of pressure communication, stress redistribution, and fracture -network connectivity may 
occasionally produce anomalous production behaviour. Therefore, understanding the coupled effects of reservoir 
depletion, fracture dynamics, and geomechanical evolution remains essential for optimizing well spacing, 
stimulation design, and long-term recovery strategies in unconventional shale reservoirs. 
 
 
Experiment Test effect parameters Matrix permeability induced Cumulative production index Reference 
Hybrid model 
(simulation) 
Anomalous 
diﬀusion, matrix 
permeability, non-
darcy ﬂow 
permeability 
1-1000 
stimulated coeficient 
Slightly 
increased 
Al-Rbeawi & Al-Kaabi 
2020 
Analytical 
model 
(simulation) 
Stimulated 
reservoir volume 
(srv) 
Equal to 
symmetrical constant 
& varied – 
asymmetrical srv 
No 
significantly 
impact 
Al-Rbeawi 2020 
Forcasting 
model 
(simulation) 
Matrix 
permeability, fracture 
spacing 
1-100 x times 
matrix permeability 
Significantly 
increased 
Cipolla 2009 
 
The Eagle Ford shale reservoir has become one of the most productive unconventional reservoirs in North 
America (Tian et al., 2014) . According to the U.S. Energy Information Administration (2011) , the Eagle Ford 
formation contains substantial recoverable hydrocarbon resources. The reservoir permeability ranges from 
approximately 1 to 800 nano-Darcy (Inamdar et al., 2010; Stegent et al., 2010), making production performance 
highly dependent on hydraulic-fracture effectiveness, pressure management, and geomechanical stability. 
The modelled data for gas-condensate and oil from the Eagle Ford shale reservoir located in South Texas, US, 
are used for this purpose (Figure 2 ). Eagle Ford shale has become one of the fastest -growing unconventional 
developments in the United States following the successful commercialization of the Barnett, Haynesville, and 
Marcellus shale plays (U.S. Energy 2011). According to reports published in 2009, the estimated natural gas and 
oil recoverable from Eagle Ford Shale were 21 Tcf and 3 billion barrels, respectively. The reservoir depth ranges 
from 2,500 to 14,000 ft; the thickness gap ranges from 50 to more than  300 ft; the pressure-gradient gap ranges 
from 0.4 to 0.8 psi/ft; and the TOC gap ranges from 2 to 9%. In the core analysis, the gas saturation gap ranges 
from 83% to 85%, and permeability varies from 1 to 800 nD. 
Although previous studies have independently investigated matrix permeability enhancement, hydraulic 
fracture conductivity, geomechanical deformation, and parent –child well interference, limited studies have 
quantitatively evaluated their coupled effects on long-term EUR optimization using an integrated compositional-
geomechanical simulation framework. This knowledge gap motivates the present study. Therefore, this study aims 
to bridge this gap by investigating the combined effects of hypothetical matrix permeability enhancement and 
parent–child well implementation on the cumulative production, pressure behaviour, and geomechanical response 
of the Eagle Ford shale reservoir. 
Despite significant advances in understanding matrix permeability, fracture effectiveness, and parent -child 
interactions individually, no previous study has quantitatively evaluated the coupled effects of hypothetical 
permeability enhancement, geomechanica l deformation, and fracture -driven communication within a unified 
compositional-geomechanical simulation framework using Eagle Ford shale properties. This gap motivates the 
present investigation. 
 
Table 1. 
Review impact matrix permeability on cumulative production.

10 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
2. Methodology 
2.1 Reservoir model development 
This study used a compositional reservoir simulation approach to evaluate the influence of hypothetical matrix 
permeability enhancement and parent –child well interactions on the EUR of an unconventional shale reservoir. 
The simulation integrates hydraulic -fracture modeling, production sensitivity analysis, and geomechanical 
evaluation using the GEM simulator and CMOST optimization tools. The Eagle Ford shale reservoir was selected 
as the case study because it is one of the most productive unconventional sha le formations, with ultra -low 
permeability and extensive use of hydraulic fracturing (Tian et al., 2014 ; Inamdar et al., 2010 ; Stegent et al., 
2010). The methodology also accounted for the unconventional characteristics of shale reservoirs, including ultra-
low permeability, nanoscale pore systems, stress -sensitive fracture conductivity, and complex geomechanical 
behaviour, as discussed by Junira & Wibowo (2016). In shale formations, the matrix simultaneously serves as a 
hydrocarbon source rock and a storage medium, leading to hydrocarbon flow behaviour that differs significantly 
from that in conventional reservoirs. Therefore, an integrated evaluation of fracture-network performance, matrix 
permeability evolution, and stress redistribution is essential for understanding unconventional reservoir 
productivity (King et al., 2010; Junira & Wibowo 2016). 
A conceptual reservoir model was developed to investigate the interaction between hydraulic fractures, stress 
redistribution, and production performance in horizontal wells. Two simulation scenarios were constructed. The 
first scenario consisted of a single horizontal well with multi-stage hydraulic fractures, while the second scenario 
involved a pair of horizontal wells representing the parent–child well configuration. The comparison between the 
two models was intended to evaluate the impact of interwell i nterference, pressure depletion, and fracture 
interaction on cumulative production and geomechanical behaviour (Wang et al., 2021; Al-Rbeawi 2020).  
The reservoir model utilized a Cartesian grid system of 211×211×5 (Figure 3). The reservoir top depth was 
defined at 11,800 ft with a total thickness of 100 ft. Reservoir properties included matrix porosity of 0.05 fraction, 
fracture porosity of 0.05 fraction, matrix permeability of 0.0075 mD, and fracture permeability of 0.00075 mD. 
The initial reservoir pressure was set to 10,000 psi at a depth of 12,000 ft, with the water-oil contact at 13,000 ft. 
These reservoir conditions were selected to represent the typical characteristics of Eagle Ford shale reservoirs 
(Tian et al., 2014; U.S. Energy 2011). 
Figure 2. 
Lateral extent of Eagle Ford shale reservoir

11 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
  
 
 
 
 
 
 
 
 
 
2.2 Fluid characterization 
The reservoir fluid system was modelled as a gas -condensate system using compositional fluid analysis. The 
fluid composition included hydrocarbon and non -hydrocarbon components such as N2, C1, C2, C3, C4−6, and 
heavy fractions (C7+, C11+, C15+, and C20+)  (Table 2 and Table 3). The compositional properties included 
molecular weight, specific gravity, acentric factor, critical temperature, critical pressure, and critical volume for 
each component (Heydari et al., 2024) . The Peng –Robinson equation of state (EOS) was used to model fluid 
property variation under reservoir conditions during depletion and production. 
2.3 Single well modeling 
 The first stage of the study focused on a single horizontal well equipped with multi-stage hydraulic fractures 
(Figure 4 and Figure 5). The well was completed with 20 hydraulic fractures distributed symmetrically along both 
sides of the lateral section. The fracture half -length was set to 500 ft, and the fracture width was 50 ft. Fracture 
permeability near the wellbore was assigned as 20 mD, whereas fracture-tip permeability was reduced to 5 mD to 
represent conductivity degradation away from the wellbore. The fracture behavior and conductivity distribution 
were designed based on unconventional fracture -network concepts discussed in previ ous studies (Winderasta 
2017; Lolon et al., 2009; Cipolla 2009).   
 
Component Z Gas  
N2 0.03  
C1 0.65  
C2 0.104  
C3 0.103  
C4-6 0.07  
C7+ 0.07  
Total 1.00  
Figure 3. 
Global cartesian grid used in the parent–child well simulation model 
 
Table 2. 
Initial condition of gas cap condensate

12 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
Composition MW Specific gravity Acentric factor Tc, R Pc, Psia Vc, cft/lbm 
 
 C1 16.064 0.35 0.013 343.3 673.1 1.5658  
 N2 28.01 0.808 0.04 227.2 492.3 1.4256  
 C2 30.07 0.48 0.0986 549.8 708.4 2.3556  
 C3 44.1 0.5077 0.1524 665.8 617.4 3.2294  
 CO2 44.01 0.8159 0.225 547.6 1071.3 1.5126  
 IC4 58.12 0.5631 0.1848 734.6 529.1 4.2127  
 NC4 58.12 0.5844 0.201 765.4 550.7 4.1072  
 IC5 72.15 0.6248 0.2223 828.7 483.5 4.9015  
 NC5 72.15 0.6312 0.2539 845.6 489.5 5.0232  
 NC6 86.18 0.6641 0.3007 914.2 439.7 5.9782  
 C7+ 114.4 0.7563 0.3739 1060.5 402.8 7.4093  
 C11+ 166.6 0.8135 0.526 1223.6 307.7 10.682  
 C15+ 230.1 0.8526 0.6979 1368.4 241.4 14.739  
 C20+ 409.2 0.9022 1.0456 1614.2 151.1 26.745  
 
 
 
Composition MW Specific gravity Acentric factor Tc, R Pc, Psia Vc, cft/lbm 
 
 C1 16.04 0.35 0.013 343.26 673.08 1.5658  
 N2 28.01 0.808 0.04 227.16 492.32 1.4256  
 C2 30.07 0.48 0.0986 549.774 708.35 2.3556  
 C3 44.1 0.5077 0.1524 665.82 617.38 3.2294  
 CO2 44.01 0.8159 0.225 547.56 1071.3 1.5126  
 IC4 58.12 0.5631 0.1848 734.58 529.06 4.2127  
 NC4 58.12 0.5844 0.201 765.36 550.66 4.1072  
 IC5 72.15 0.6248 0.2223 828.72 483.5 4.9015  
 NC5 72.15 0.6312 0.2539 845.64 489.52 5.0232  
 NC6 86.18 0.6641 0.3007 914.22 439.7 5.9782  
 C7+ 112 0.7527 0.3673 1051.39 408.59 7.261  
 C11+ 175 0.8201 0.5491 1245.9 296.89 11.2083  
 C15+ 210 0.8424 0.6435 1327.59 259.01 13.435  
 C20+ 250 0.8612 0.7527 1405.81 226.28 16.0488  
 
A horizontal well model was developed using the Prosper simulator to generate the tubing curve (Figures 6 
and 7) and employed the Kuchuk and Goode correlation. The objective of this well model is to optimize well 
productivity (Al-Rbeawi & Al-Kaabi 2020; Ghanbarian et al., 2020). 
2.4 Bottom-hole pressure sensitivity analysis 
A horizontal well model was developed using the Prosper simulator to generate the tubing curve (Figures 6 
and 7) and employed the Kuchuk and Goode correlation. The objective of this well model is to optimize well 
productivity. A sensitivity analysis was then performed using CMOST experimental design to evaluate the 
influence of pressure drawdown on cumulative production performance. The optimization process utilized 100 
experimental datasets with bottom -hole pressure (BHP) value s ranging from 3,000 psi to 10,000 psi at 
approximately 70 psi intervals , generating 100 distinct scenarios. CMOST optimization identified the BHP that 
maximized cumulative gas production while maintaining wellbore stability constraints (minimum BHP = 3, 000 
psi). The objective of this sensitivity analysis was to determine the optimum operating condition capable of 
maximizing cumulative gas production while maintaining stable reservoir performance. Previous studies reported 
that pressure -management optimization pla ys an important role in unconventional reservoir productivity and 
parent–child well performance (Le Calvez et al., 2007; Wang 2025). 
Table 3. 
Compositional data of Eagle Ford oil (Kamari et al., 2018). 
 
Table 4. 
Compositional data of Eagle Ford condensate (Stegent et al., 2010).

13 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
• Shear Stress and Shear Strain Analysis 
Geomechanical behaviour surrounding the hydraulic fractures was investigated by analyzing shear stress 
and shear strain distributions in selected grid blocks. The stress–strain evaluation was conducted in the IJ, 
JK, and IK directions to assess anisotropic deformation induced by hydraulic fracturing and reservoir 
depletion. Previous studies demonstrated that stress redistribution strongly influences fracture propagation, 
fracture conductivity, and permeability evolution in unconventional reservoirs  (King et al., 20 10; 
Taghichian et al., 2018; Bui 2023; Heydari et al., 2024). 
Three-dimensional visualization of stress and strain distributions was also performed to identify deformation 
patterns around the horizontal well and the fracture network. This geomechanical evaluation was intended to 
investigate the coupling effect between hydraulic -fracture propagation, stress redistribution, and production 
depletion. Recent studies have indicated that stress -sensitive fracture deformation may significantly influence 
long-term unconventional reservoir productivity and the evolution of permeability  (Bui 2023 ; Heydari et al., 
2024). Subsequently, two additional models were developed by increasing matrix permeability by factors of 10 
and 100 relative to the base case. 
The next stage is to evaluate BHP sensitivity in the base cases of the three models. The CMOST simulator is 
used to perform the sensitivity analysis, saving time when running the model. The sensitivity uses 100 different 
BHP datasets, ranging from 3,000 ps i to 10,000 psi in 70 Psi Increments. In this case, the experimental designs 
used are the same as those in the 100 ID and 100 BHP datasets. 
Figure 4. 
Multi-stage hydraulic -fracture configuration of the single horizontal well model.

14 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
 
 
Figure 5. 
Location of the well in the model 
 
Figure 6. 
Pressure distribution in the single model

15 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
The primary geomechanical outputs include shear stress and shear strain distributions evaluated at 6, 12, 60, and 
120 months. The grid blocks investigated in the model are shown in Figure 7. 
 
 
  
 
 
 
 
 
 
 
 
 
 
Figure 7. 
Tubing performance plot 
 
Figure 8. 
Grid name for shear strain and shear stress investigation 
Figure 9. 
Grid blocks location for stress and strain investigation

16 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Figure 7 and Figure 8 show one of the grids that was investigated for shear strain and shear stress. From the 
optimum solution, the shear strain and shear stress are investigated in certain grid blocks. For example, grid block 
106 106 3; Figure 9 exhibits the shear strain in block 106 106 3 in three directions. The shear strain in the IJ 
direction is positive (Figures 10 and 11). Oppositely, the shear stress in the JK direction is negative. Meanwhile, 
the shear strain in the IK direction changes direction from negative to positive. 
Figure 12 and Figure 13 show the different Figure 12 and Figure 13 show the differences between the toe and 
the heel of the well in the IJ direction. One side of the heel measures positive shear stress, while the toe measures 
negative shear stress. Oppositely, the phenomenon occurs in an opposite way on the other side. 
 
 
 
 
 
 
 
 
 
 
Figure 10. 
The shear strain in block 106 106 3 
 
Figure 11. 
The 3D virtual of shear strain in the IJ direction

17 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
 
 
 
 
 
2.5 Parent–child well model 
The second stage of this study investigated the interaction between adjacent horizontal wells using a 
parent–child well configuration. The parent –child well configuration was designed to evaluate fracture -
driven communication and pressure interference unde r relatively tight well -spacing conditions. Previous 
studies reported that closely spaced unconventional wells may experience fracture -hit behaviour, stress -
shadow effects, and dynamic fracture interaction during production and stimulation operations (Le Calvez 
et al., 2007 ; Wang et al., 2021 , Al-Rbeawi 2020) . 
Figure 12. 
Shear stress in grid block 106 106 3 
 
Figure 13. 
The 3D virtual of shear stress in the IJ direction

18 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
A second horizontal well, referred to as the child well, was positioned parallel to the parent well with a spacing 
of 1,500 ft between wellbores and approximately 500 ft between fracture tips. Both wells had identical completion 
designs consisting of 20 hydr aulic fractures and 5,000 ft horizontal lateral lengths. Gas saturation distribution, 
cumulative gas production, reservoir pressure behaviour, and wellhead -pressure performance were monitored 
throughout the simulation period. The parent –child interaction was analyzed to identify production interference, 
fracture-driven communication, and depletion-shadow effects, which are commonly observed in unconventional 
reservoir developments (Le Calvez et al., 2007; Wang et al., 2021, Al-Rbeawi 2020). 
 
 
 
 
 
 
The same simulation workflow was applied to all three permeability scenarios, including matrix-permeability 
variation, BHP sensitivity analysis using 100 hypothetical numerical datasets, and geomechanical evaluation 
through shear-stress and shear-strain analysis within selected grid blocks (Figure 14). 
2.6 Matrix–fracture transfer mechanisms in dual-porosity reservoir systems 
The production performance of unconventional shale reservoirs is strongly governed by fluid transfer between 
the ultra-low-permeability rock matrix and the highly conductive hydraulic-fracture network. Although hydraulic 
fractures provide the primary produ ction pathways, most hydrocarbons remain stored within the matrix. 
Consequently, long-term recovery is controlled by the efficiency of matrix-to-fracture mass transfer. 
One of the most widely accepted conceptual models describing this mechanism is the dual -porosity model 
proposed by Warren & Root (1963) and extended by Kazemi et al. (1976) . In this formulation, the reservoir is 
represented by two interacting continuous systems: a low -permeability matrix system that stores hydrocarbons 
and a high-permeability fracture system that serves as the primary flow conduit toward the wellbore. Fluid transfer 
between the matrix and fracture systems is expressed as: 
qmf= σ (km/µ)(Pm-Pf)  (2) 
where q mf, σ, km, µ, P m, and Pf are matrix-to-fracture transfer rate, shape factor, matrix permeability, fluid 
viscosity, matrix pressure, and fracture pressure, respectively. The relationship in Equation 1 demonstrates that 
matrix-fracture transfer is directly proportional to the product of matrix permeability and pressure differential. 
Therefore, any increase in matrix permeability increases hydrocarbon transfer efficiency and accelerates 
production response. 
Kazemi et al. (1976)  later extended the Warren –Root concept by introducing transient interporosity flow 
behaviour. Unlike the pseudo-steady-state assumption adopted by Warren & Root (1963), Kazemi's formulation 
allows fluid transfer to evolve dynamically as pressure depletion progresses within both matrix and fracture 
systems. This approach is particularly important for unconventional reservoirs because pressure gradients 
continuously evolv e during production, resulting in time -dependent matrix -fracture communication . The 
combined Warren –Root and Kazemi frameworks constitute the theoretical foundation of most modern dual -
porosity and dual-permeability reservoir simulators, including CMG-GEM. Consequently, matrix permeability is 
recognized as one of the most influential parameters governing long-term unconventional reservoir performance, 
Figure 14. 
The second part of case study (parent and child).

19 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
as it directly controls the rate at which hydrocarbons migrate from the storage -dominated matrix into the 
conductive fracture network. Several studies have further demonstrated the importance of matrix permeability in 
shale-gas production forecasting. Cipolla (2009) reported that matrix permeability significantly affects 
hydrocarbon drainage efficiency and cumulative recovery, particularly during late -time production periods. 
Similarly, Al-Rbeawi & Al-Kaabi (2020) demonstrated that stimulated matrix permeability and matrix -fracture 
interaction substantially influence productivity and pressure -depletion behaviour within unconventional 
reservoirs. These findings collectively indicate that matrix permeability remains a key parameter controlling long-
term EUR in hydraulically fractured shale formations. 
2.7 FDI, depletion shadow, and child-well performance 
As unconventional developments become increasingly dense, interactions between adjacent horizontal wells 
have emerged as one of the most important challenges affecting long -term reservoir performance. Parent wells, 
which are completed and produced first, p rogressively deplete reservoir pressure within the surrounding 
stimulated reservoir volume. This depletion creates a localized low -pressure region commonly referred to as a 
depletion shadow. 
 
 
 
Figure 15 illustrates the implementation of Local Grid Refinement (LGR) around the parent and child wells. 
The refined grids improve numerical accuracy in regions where strong pressure gradients and FDIs are expected. 
The use of LGR is particularly important becaus e depletion-shadow and fracture -driven communication occur 
within a relatively narrow region surrounding the hydraulic fractures. 
The depletion-shadow effect is generally associated with reduced child -well productivity because reservoir 
energy available for hydrocarbon displacement has already been partially consumed by the parent well. Similarly, 
Ajisafe et al. (2019)  demonstrated that depletion -shadow effects often reduce stimulation efficiency and limit 
access to undrained reservoir volumes. 
In addition to reservoir -pressure depletion, production from the parent well alters the local geomechanical 
environment through stress redistribution. Reducing pore pressure increases effective stress and modifies the local 
minimum horizontal stress field. This phenomenon is commonly referred to as stress shadowing.  
 
 
Figure 15. 
Local grid refinement (LGR) around parent and child wells 
 
Child Well 
LGR 7X7X1 
LGR 5X5X1 
Parent Well

20 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Another important mechanism is fracture shielding, in which previously formed hydraulic fractures 
modify local stress conditions and restrict the propagation of newly formed fractures. Fracture shielding 
frequently reduces stimulated reservoir volume and c ontributes to child -well underperformance. However, 
recent studies have shown that under certain conditions, depletion -induced stress reorientation may generate 
the opposite response.  
Wang et al. (2021) reported that strong pressure communication between neighbouring wells may create FDI, 
leading to dynamic communication between adjacent fracture networks. Similarly, Liu et al. (2026) demonstrated 
that frac-hit behaviour becomes increasingly severe as inter-well spacing decreases, allowing hydraulic fractures 
to propagate toward depleted regions surrounding parent wells. 
Frac-hit events occur when hydraulic fractures generated during child -well stimulation intersect or 
hydraulically communicate with pre -existing parent-well fracture systems. Depending on reservoir conditions, 
frac-hit behaviour may either impair or enhance  production performance. In some cases, highly conductive 
communication pathways may develop between fracture networks, creating preferential flow channels that 
accelerate hydrocarbon transfer and temporarily improve production performance. 
These observations indicate that parent–child well performance is governed by a complex interaction among 
depletion shadow, stress shadow, fracture shielding, and fracture -driven communication. Consequently, 
understanding the coupled effects of reservoir d epletion, fracture propagation, and geomechanical evolution is 
essential for optimizing well spacing, stimulation design, and long-term recovery in unconventional reservoirs. 
 
3. Result and discussion 
The integrated methodology enables comprehensive evaluation of the coupling among reservoir flow physics, 
hydraulic-fracture performance, pressure behaviour, depletion shadow, and geomechanical response in 
unconventional shale reservoir development. 
3.1 Effect of matrix permeability on cumulative production. 
The results of the three models show significant differences in cumulative oil and gas performance (Figure 16 
and Figure 17). The simulation results demonstrate that matrix permeability is one of the dominant parameters 
controlling long -term hydrocarbon recovery in unconventional shale reservoirs. Three permeability scenarios 
were evaluated: the base -case permeability, a 10× perm eability enhancement, and a 100× permeability 
enhancement. This behaviour confirms that hydrocarbon transfer from the shale matrix toward the hydraulic -
fracture network becomes more efficient when matrix-flow capacity improves. 
The results suggest that enhancing effective matrix permeability may be as important as increasing 
fracture complexity. While hydraulic fractures create conductive pathways, long -term production remains 
governed by the ability of hydrocarbons to diffuse an d flow from the matrix toward the fracture network. 
Consequently, technologies that improve matrix connectivity or stimulate secondary fracture networks may 
significantly enhance EUR.  
In the base -case scenario, production performance remained relatively limited because the ultra -low matrix 
permeability restricted fluid mobility within the shale formation. Hydrocarbons stored within the matrix could 
only migrate slowly toward the fractur e system, resulting in lower cumulative production and slower reservoir 
drainage. However, when matrix permeability was increased by factors of 10× and 100×, gas transport to the 
fracture network became substantially more efficient, leading to higher cumulative gas production and improved 
EUR. The difference in cumulative gas is up to 400,000 ft3, while the cumulative oil is up to 4,000 bbl. It means 
the matrix permeability is a key parameter for this model (Figure 18).

21 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
 
 
 
 
 
Figure 19 shows gas saturation distribution along both the wellbore and the vicinity near the wellbore. It seems 
the pressure drawdown in the child well (PROD2) is higher than the parent well (PROD). The impact of pressure 
drawdown is that gas production from the child well exceeds that from the parent well. 
3.2 Theoretical interpretation of matrix permeability sensitivity 
The simulation results demonstrate a substantial increase in cumulative gas production as matrix permeability 
increases from the base -case condition to the 10× and 100× permeability scenarios (Figure 18). Although this 
trend appears significant, it should be recognised that such behaviour is fundamentally consistent with the 
governing matrix -to-fracture transfer mechanisms implemented within dual -porosity and dual -permeability 
reservoir simulators. In unconventional shale reservoirs, hydraulic fractures provide the primary high-conductivity 
 
      
      
      
      
       
       
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
                  
                 
                  
                   
Figure 16. 
Comparison of cumulative gas production for the three matrix-permeability scenarios 
 
Figure 17. 
 Comparison of cumulative oil production for the three matrix-permeability scenarios

22 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
flow pathways, whereas the matrix serves as the dominant hydrocarbon storage medium. Consequently, long-term 
production performance depends largely on the efficiency of hydrocarbon transfer from the matrix toward the 
fracture network. According to the pseudo-steady-state formulation proposed by Warren & Root (1963), matrix-
fracture transfer is directly proportional to matrix permeability and the pressure differential between the matrix 
and fracture systems (Figure 20) . Similarly, Kazemi et al. (1976)  demonstrated that transient matrix -fracture 
transfer processes strongly influence production behaviour in naturally fractured and dual -porosity reservoirs. 
Therefore, increasing matrix permeability mathematically accelerates hydrocarbon migration from the  matrix to 
the fracture network, resulting in higher cumulative production and improved recovery efficiency. 
 
 
 
 
 
 
 
 
 
 
  
 
 Figure 18. 
Gas cumulative in the parent-child well model 
 
Parent well 
(a) 
Child well 
(b)

23 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The production enhancement observed in the present study should not be interpreted as evidence of a practical, 
field-scale permeability -enhancement technology. Instead, the permeability multipliers represent hypothetical 
numerical sensitivity scenarios designed to establish theoretical upper -bound recovery limits and quantify the 
relative importance of m atrix-flow capacity in unconventional reservoir performance. The results demonstrate 
that matrix permeability remains one of the most influential parameters governing long -term hydrocarbon 
recovery, particularly after fracture-dominated early-time production transitions into matrix-controlled depletion. 
Furthermore, the sensitivity analysis highlights significant uncertainty in matrix permeability 
characterisation in shale reservoirs. Because matrix permeability is commonly measured at the nano -Darcy 
scale and may be affected by core handling, microfractu re development, and laboratory testing conditions, 
production forecasting can vary substantially depending on the assumed matrix permeability value. 
Consequently, accurate characterisation of matrix permeability remains essential for reliable EUR predictio n 
and reservoir -development planning.  
 
 
 
 
 
 
 
Figure 19. 
Gas Saturation distribution illustrating pressure communication between the parent and child wells 
 
Figure 20. 
Pressure distribution in the parent-child well model

24 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
3.3 Geomechanical  response around hydraulic fractures 
In addition to flow -related mechanisms, production performance in unconventional reservoirs is strongly 
influenced by geomechanical responses induced by hydraulic fracturing and reservoir depletion. Changes in pore 
pressure alter the effective stress distr ibution surrounding the fracture network, leading to localized deformation 
and stress redistribution within the reservoir. As reservoir pressure declines during production, the increase in 
effective stress may modify fracture conductivity, alter permeabili ty evolution, and influence the mechanical 
stability of the stimulated reservoir volume (SRV). Consequently, understanding the geomechanical response of 
the reservoir is essential for interpreting long-term production behavior and parent–child well interaction. 
 
 
 
  
 
 
 
  
 
 
 
Figure 21. 
Three-dimensional shear strain distribution in the parent-child well configuration 
 
Figure 22. 
Shear strain evolution in grid block 106 106 3 for the parent-child well model

25 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Figures 21 and 22 shows the evolution of shear strain surrounding the hydraulic -fracture system. The results 
reveal significant strain localization near the fracture tips, indicating that reservoir deformation is concentrated in 
regions experiencing the highest pressure gradients. The asymmetric distribution suggests that hydraulic-fracture 
propagation and reservoir depletion do not  generate uniform mechanical responses throughout the stimulated 
reservoir volume. 
 
 
 
 
Figure 23 presents the corresponding shear-stress distribution. Positive and negative stress values are observed 
in different regions of the reservoir, indicating complex stress redistribution induced by hydraulic fracturing and 
pressure depletion. Such behaviour i s consistent with stress -shadow development commonly reported in 
unconventional reservoirs. 
 
 
 
 
 
Figure 23. 
Three-dimensional shear stress distribution in the parent-child well configuration 
Figure 24. 
Shear stress evolution in grid block 106 106 3 for the parent-child well model

26 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The shear stress distributions further demonstrate stress redistribution around the fracture network. Both 
positive and negative stress regions are observed, reflecting the complex geomechanical interactions between 
hydraulic fractures, reservoir depletion, and rock deformation. Such behaviour is consistent with the stress-shadow 
phenomenon commonly reported in unconvention al reservoirs, where pressure depletion and fracture 
development modify the local stress field and influence subsequent fracture growth.  
 
 
 
 
 
Basically, these two wells are set up using the same method, but the simulation results show that the WHP 
alteration in the child well exhibits a dynamic rhythm compared with that of the parent well (Figure 25). 
Overall, the geomechanical results demonstrate that unconventional reservoir performance is governed not 
only by matrix permeability and fluid -flow mechanisms but also by the coupled interaction between pressure 
depletion, stress evolution, and rock deformation. Therefore, integrating geomechanical analysis with production 
and pressure-distribution evaluation is essential for accurately characterising parent –child well behaviour and 
optimising long-term hydrocarbon recovery. 
Regions exhibiting severe pressure depletion correspond to zones of elevated shear strain and stress 
concentration. The reduction in pore pressure increases effective stress, resulting in localized rock deformation 
surrounding the hydraulic fractures. This behavior supports the stress-shadow mechanism commonly reported in 
unconventional reservoir developments. 
3.4 Parent–child well performance and pressure evolution 
The parent–child well simulations reveal strong production interference and pressure communication between 
adjacent horizontal wells. Compared with the single-well scenario, the introduction of a second well significantly 
altered pressure distribution, reservoir drainage patterns, and fracture-network utilisation. The simulation results 
indicate that reservoir depletion generated by the parent well creates a substantial pressure gradient that influences 
the hydraulic and geomechanical response of the subsequently completed child well. 
Figure 25. 
Comparison of the well head pressure behavior between the parent and child wells

27 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 26. 
Pressure distribution immediately before well completion (aerial) 
 
Figure 27. 
Pressure distribution immediately before production  (aerial) 
 
Figure 28. 
Pressure distribution 1 month after production (aerial)

28 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Pressure-distribution analysis prior to child -well completion shows the development of a pronounced 
depletion-shadow region surrounding the parent well. This low -pressure zone serves as a dominant control on 
subsequent fracture propagation and fluid-flow behaviour. The pressure sink generated by long-term parent-well 
production modifies local reservoir energy and creates strong pressure communication pathways between 
neighbouring wells. Such behaviour is consi stent with previous studies reporting that pressure interference can 
significantly influence production forecasting and recovery performance in tightly spaced unconventional 
developments (Wang et al., 2021). 
The pressure -map results further indicate that the depletion -shadow region extends beyond the immediate 
vicinity of the parent well and influences a substantial portion of the stimulated reservoir volume. Consequently, 
hydraulic fractures generated during child-well stimulation are subjected to altered stress and pressure conditions 
compared with those encountered during parent -well completion. These findings demonstrate the importance of 
considering depletion history and pressure communication when designi ng infill drilling programs in 
unconventional reservoirs. 
The observed pressure interaction confirms that parent –child well performance cannot be evaluated solely 
through geometric well spacing. Instead, reservoir pressure depletion, fracture connectivity, and dynamic stress 
redistribution collectively determine the efficiency of hydrocarbon recovery and long-term field performance. 
Figure 18 shows a significant difference in cumulative gas performance. The child well produced more than 
ten times the cumulative gas volume of the parent well. This behaviour suggests significant pressure depletion 
around the parent well prior to infill drilling, which altered local stress conditions and promoted preferential flow 
toward the child well (Figures 26, 27, and 28). Such behaviour is consistent with FDIs reported in unconventional 
reservoir developments (Figure 20). Dominantly, this is due to the high-pressure drawdown in the child wel. 
These findings are consistent with Fan et al. (2018) , who explained that shale matrix permeability strongly 
controls long-term unconventional reservoir productivity. Similarly, Al-Rbeawi & Al-Kaabi (2020) reported that 
stimulated matrix permeability significantly reduces pressure drop and improves productivity index during 
transient and boundary-dominated flow periods. The results also support the findings of Ghanbarian et al. (2020), 
who demonstrated that nano-scale pore confinement and stress-sensitive permeability strongly influence gas-flow 
behaviour in unconventional formations. 
The simulation results further indicate that permeability enhancement within SRV improves fluid 
communication between the matrix system and hydraulic fractures. As permeability  increases, pressure 
depletion propagates more effectively into the matrix region, accelerating hydrocarbon drainage toward the 
production well. This behaviour confirms that permeability enhancement is critical for sustaining long -term 
unconventional produc tion. 
The observed increase in cumulative production is consistent with the fundamental matrix-to-fracture transfer 
formulation described by Warren & Root (1963) and Kazemi et al. (1976) , in which the transfer rate is directly 
proportional to matrix permeability. Therefore, the present study should be interpreted as defining theoretical 
recovery limits under progressively improved matrix -flow conditions rather than predicting field -scale 
permeability enhancement outcomes. 
3.5 Long-term evolution of pressure communication 
Early Stage (2020–2022): During the early production period, pressure depletion remains concentrated around 
the parent-well fractures. Hydraulic communication between the wells remains limited, and the depletion shadow 
primarily forms around the parent well.

29 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 
 
 
Intermediate Stage (2023 –2026) : As production progresses, the depletion fronts expand outward from the 
parent-well fracture network. The pressure gradients between the wells gradually decrease, indicating increasing 
pressure communication and reservoir interaction . Late Stage (2027 –2030): In the late production stage, the 
fracture pressure distributions become increasingly interconnected. The pressure field suggests that both wells are 
partially draining from a shared reservoir volume, leading to stronger parent–child interaction. 
Figure 29. 
Pressure distribution in the parent–child well system (January 2020-2022).  
 
(a) 
(b) 
(c) 
(2020) 
(2021)

30 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
[2023] 
[2024] 
[2025] 
[2026] 
Figure 30. 
Pressure distribution in the parent–child well system (January 2023-2026). 
(c) 
(b) 
(a) 
(d)

31 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The pressure evolution observed in Figures 29 - 31 validates the need for Local Grid Refinement (Figure 4). 
Without the refined grids surrounding the hydraulic fractures, the steep pressure gradients and depletion -shadow 
boundaries would not be adequately captured. 
3.6 Influence of hydraulic fracture network and fracture conductivity 
The reservoir's production performance is also strongly affected by fracture-network complexity and fracture 
conductivity. The hydraulic fractures created conductive pathways that connect the low-permeability shale matrix 
to the production wellbore, thereby enlarging the effective drainage area surrounding the horizontal well. 
The fracture system created rapid pressure communication between the reservoir and the wellbore during the 
early production period. High fracture conductivity near the wellbore accelerated gas transport and improved 
initial production rates. However, condu ctivity degradation away from the fracture tips reduced flow efficiency 
in the outer stimulated region, indicating that fracture conductivity distribution significantly influences cumulative 
production behaviour. 
These observations are consistent with the findings of Taghichian et al. (2018) , who reported that fracture 
propagation and fracture aperture behaviour are strongly influenced by stress conditions and rock toughness. 
Lolon et al. (2009)  also demonstrated that fracture spacing and fracture conductivity significantly affect 
unconventional reservoir productivity. Furthermore, Cipolla (2009)  emphasised that  highly complex fracture 
networks may partially compensate for ultra-low matrix permeability by reducing hydrocarbon drainage distance 
within the shale matrix. 
The present simulation results indicate that fracture -network effectiveness becomes increasingly important 
during late production periods. As reservoir pressure declines, the fracture system acts as the primary conductive 
pathway controlling hydrocarbon movement from the matrix toward the wellbore. Therefore, maintaining fracture 
conductivity stability is essential for sustaining long-term production performance. 
3.7 Bottom-Hole Pressure Optimization 
Sensitivity analysis using CMOST demonstrated that BHP strongly affects cumulative gas production and 
reservoir depletion behaviour. The optimization process utilized 100 experimental datasets with BHP values 
ranging from 3,000 psi to 10,000 psi. The resul ts indicate that lower BHP values generally increase cumulative 
gas production because larger pressure drawdown enhances fluid transport from the reservoir toward the wellbore. 
CMOST optimisation identified an optimum operating condition yielding a cumulative gas production of 
approximately 9.8 × 10^8 ft3 under the optimised pressure conditions (Figure 32). The larger pressure differential 
between the reservoir and wellbore accelerated hydrocarbon drainage from the shale matrix toward the fracture 
network, thereby improving production efficiency. However, excessively aggressive pressure drawdown may also 
accelerate stress redistribution and degradation of fracture conductivity. Rapid pressure depletion near hydraulic 
fractures may induce stress-sensitive permeability reduction and fracture closure. Therefore, pressure optimisation 
must balance production acceleration with long-term fracture stability. 
These findings are consistent with Wang et al. (2021), who reported that pressure -management optimisation 
significantly affects unconventional reservoir productivity and EUR forecasting. Modern unconventional 
reservoir developments increasingly integrate production optimisation and geomechanical analysis to minimise 
fracture degradation while maximising cumulative production (Bui 2023). 
3.8 Geomechanical response and shear stress–strain behavior 
The geomechanical analysis demonstrated that hydraulic fracturing and reservoir depletion generated 
significant stress redistribution surrounding the fracture network. Shear stress and shear strain distributions 
exhibited anisotropic deformation in the IJ, JK, and IK directions, indicating that deformation around hydraulic 
fractures is highly non-uniform.

32 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 31. 
Pressure distribution in the parent–child well system (January 2027-2030). 
 
(a) 
(b) 
(c) 
(d)

33 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
 
 
 
 The highest stress concentration occurred near the fracture regions and surrounding the horizontal 
wellbore. As production time increased, the magnitude of shear strain also increased due to continuous reservoir 
depletion and pressure reduction. The deformation behaviour became increasingly pronounced duri ng the late 
production periods, particularly after 60 and 120 months. 
These findings are consistent with those of Warpinski & Teufel (1987) , who reported that in situ stress 
conditions strongly control fracture propagation and fracture geometry. King (2010) also explained that hydraulic 
fracturing may alter local stress conditions and generate stress redistribution surrounding fracture systems. 
Recent geomechanical studies further support these observations. Bui (2023)  emphasised that stress -
sensitive permeability and degradation of fracture conductivity are critical factors controlling 
unconventional reservoir productivity. Similarly, Heydari et al. (2024)  demonstrated that geomechanical 
deformation in shale microfractures significantly influences the evolution of permeability and fracture 
aperture behaviour during depletion.  
The present study confirms that geomechanical deformation strongly affects the long -term performance of 
unconventional reservoirs. Stress redistribution may gradually reduce fracture conductivity and alter the evolution 
of permeability around hydraulic fra ctures. Consequently, geomechanical effects should be integrated into 
unconventional reservoir development planning to ensure sustainable long-term hydrocarbon recovery. 
The observed shear -strain concentration near fracture tips suggests local stress redistribution that may 
contribute to fracture shielding and fracture-driven communication in the parent–child configuration. 
3.9 Parent–child well interaction 
The parent –child well simulation demonstrated strong pressure communication and FDI between adjacent 
horizontal wells. The child well exhibited significantly higher cumulative gas production compared with the 
parent well due to stronger pressure drawdown and more active fracture interaction within the stimulated reservoir 
volume. However, the simulation also revealed production interference and depletion-shadow effects between the 
wells, particularly under tight well spacing. These observations indicate tha t parent–child well performance is 
strongly influenced by fracture spacing, pressure redistribution, and stress-shadow behaviour. 
The production increase in the child well indicates that pressure redistribution between adjacent wells strongly 
affects fluid-flow behavior in the stimulated reservoir volume. Pressure depletion generated by the parent well 
altered the stress condition surrounding the child well, influencing fracture propagation and interwell 
communication behavior. 
 
Figure 32. 
Experimental design result from CMOST 
 
Experiment ID

34 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The simulation also revealed production interference between the parent and child wells. Hydraulic fractures 
from adjacent wells interacted dynamically, creating fracture -driven communication pathways between the 
stimulated reservoir volumes. This interact ion accelerated hydrocarbon drainage in certain regions while 
potentially reducing pressure support in others. 
These observations are consistent with Wang et al. (2021), who reported that pressure communication between 
parent and child wells significantly affects production forecasting and EUR optimization. Liu et al. (2026)  
similarly demonstrated that fracture -hit behaviour becomes increasingly severe under tight well -spacing 
conditions due to dynamic fracture propagation and stress redistribution. 
The results further support Al-Rbeawi (2020), who explained that fracture spacing and well spacing strongly 
influence pressure interference and productivity behaviour in unconventional reservoirs. Closely spaced wells 
may experience significant fracture communication, depletion shadow effects, and p roduction rerouting over 
the long term.  
3.10 Implications for unconventional reservoir development 
The overall simulation results indicate that the performance of unconventional reservoirs is governed by the 
coupled interactions among matrix permeability, fracture -network effectiveness, pressure depletion, and 
geomechanical behaviour. Hypothetical: Matr ix permeability enhancement improves hydrocarbon transfer from 
the shale matrix to hydraulic fractures, while fracture conductivity determines the efficiency of fluid transport to 
the wellbore. 
The study also demonstrates that parent –child well implementation requires careful optimisation of well 
spacing and pressure management to minimise fracture interference and depletion -shadow effects. Excessively 
tight well spacing may lead to strong fracture communication and production imbalances between adjacent wells. 
Furthermore, geomechanical behaviour plays a critical role in determining long -term fracture stability and 
the evolution of permeability. Stress redistribution from hydraulic fracturing and production depletion may 
gradually reduce fracture conductivity an d alter reservoir flow behaviour. Therefore, successful unconventional 
reservoir development requires integrated optimisation involving matrix permeability characterisation, 
hydraulic-fracture design, pressure -management strategies, and geomechanical evalu ation. These integrated 
approaches are essential for maximising EUR while maintaining sustainable long -term production performance 
in unconventional shale reservoirs.  
3.11 Mechanisms of child-well overperformance under FDI conditions 
One of the most notable observations in this study is the substantially higher cumulative production of the 
child well relative to that of the parent well. Although conventional field experience frequently reports child-well 
underperformance due to depletion-shadow effects, the numerical simulations indicate that specific combinations 
of pressure communication, FDI, and geomechanical response may generate the opposite behaviour. 
The primary mechanism responsible for this phenomenon is the development of a strong pressure sink 
surrounding the parent well. Long -term production from the parent well substantially reduces local reservoir 
pressure, creating a highly depleted region adja cent to the existing fracture network. When the child well is 
completed and stimulated, the pressure differential between the newly stimulated reservoir volume and the 
depleted parent -well region generates a strong driving force for fluid migration. This p ressure drawdown 
accelerates hydrocarbon movement toward the child -well fracture network, thereby contributing to elevated 
production rates.  A second contributing factor is depletion -induced stress redistribution. As reservoir pressure 
decreases around the parent well, effective stress increases, altering the local stress field. Previous studies have 
demonstrated that hydraulic fractures prefer entially propagate toward regions of lower minimum horizontal 
stress. Consequently, the depleted zone surrounding t he parent well may attract newly generated fractures from 
the child well, increasing the probability of fracture communication and FDI. Such behaviour has been reported 
in several unconventional developments where fracture propagation becomes increasingly asymmetric as 
depletion progresses.

35 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
The simulation results also suggest that fracture -hit behaviour plays an important role in establishing highly 
conductive communication pathways between adjacent wells. Once hydraulic connectivity develops between 
parent- and child -well fracture systems, f luid transport efficiency may increase substantially. Under these 
conditions, the fracture network acts as an integrated drainage system that accelerates hydrocarbon transfer from 
the matrix to production wells. 
Geomechanical analysis further indicates anisotropic shear -strain behaviour surrounding hydraulic fractures. 
The observed shear deformation may contribute to localised fracture dilation and temporary increases in effective 
permeability along fracture surfaces. This mechanism may enhance matrix-fracture communication and improve 
hydrocarbon drainage efficiency in the vicinity of the child well. 
It is important to emphasise that the observed child's well -overperformance should not be interpreted as 
representative of typical field behaviour. In many unconventional developments, depletion-shadow effects reduce 
child-well productivity and lead to low er recovery than in parent wells. The behaviour observed in the present 
study represents a specific numerical scenario characterised by strong pressure communication, FDI, and 
favourable geomechanical conditions. Therefore, the results should be viewed as a mechanistic investigation of 
potential parent–child interactions rather than a universal prediction of field performance. 
From a reservoir -management perspective, these findings highlight the importance of integrating depletion 
analysis, fracture -network characterization, geomechanical modeling, and well -spacing optimization during 
unconventional reservoir development. Failure to account for these coupled processes may lead to inaccurate EUR 
forecasts and suboptimal infill-drilling strategies. 
 
4. Conclusion 
This study investigated the coupled effects of matrix permeability, BHP optimisation, geomechanical 
behaviour, and parent –child well interaction on production performance in an Eagle Ford unconventional shale 
reservoir using an integrated compositional res ervoir simulation approach. The objective was not to propose a 
field-scale permeability enhancement technology, but rather to quantify the theoretical upper recovery limits 
associated with improved matrix -to-fracture fluid transfer and to evaluate the resu lting impact on production 
behaviour and reservoir depletion. 
The simulation results demonstrate that matrix permeability is one of the dominant parameters controlling 
long-term hydrocarbon recovery in unconventional reservoirs. Increasing matrix permeability significantly 
enhanced fluid transport from the ultra-low-permeability matrix toward the hydraulic fracture network, resulting 
in substantial increases in cumulative gas and oil production. The sensitivity analysis confirmed that even 
moderate improvements in matrix-to-fracture transfer efficiency can substantially improve EUR. 
BHP optimization further showed that production performance is highly sensitive to pressure drawdown 
management. The CMOST optimization results identified an operating pressure range capable of maximizing 
cumulative production while maintaining favorable r eservoir depletion behavior. These findings emphasize the 
importance of integrating reservoir management strategies with hydraulic -fracture design to achieve sustainable 
long-term recovery. 
Geomechanical evaluation revealed non -uniform distributions of shear stress and shear strain around the 
hydraulic fractures. Elevated deformation was observed near the fracture network, indicating localized stress 
redistribution and anisotropic rock response during depletion. The results suggest that pressure depletion, fracture 
conductivity evolution, and geomechanical deformation are strongly interconnected processes that collectively 
influence unconventional reservoir performance. 
The parent–child well simulations demonstrated strong pressure communication and production interference 
between adjacent wells. Contrary to conventional expectations that child wells typically underperform due to 
depletion-shadow effects, the simulated ch ild well generated higher cumulative gas production than the parent 
well under the investigated conditions. This behaviour is interpreted as the combined effect of depletion-induced

36 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
pressure gradients, FDI, and enhanced hydraulic communication between fracture networks. The findings indicate 
that parent–child well performance cannot be explained solely by depletion -shadow mechanisms but must also 
consider stress redistribution, fracture propagation behaviour, and dynamic reservoir communication. 
Overall, the study highlights that maximizing recovery from unconventional shale reservoirs requires an 
integrated understanding of matrix permeability, hydraulic -fracture effectiveness, pressure management, 
geomechanical evolution, and parent–child well interactions. The results provide valuable insights for optimizing 
well spacing, stimulation strategies, and production management in future unconventional reservoir 
developments. 
Future research should focus on incorporating explicit FDI modelling, stress -sensitive fracture conductivity, 
depletion-shadow evolution, and field -scale history matching to further improve the prediction of parent –child 
well performance and long-term unconventional reservoir recovery.  
 
5. Acknowledgement 
The authors thank the Centre of Energy Studies (PSE), Universitas Islam Riau (UIR), for technical advice 
and support. Financial support was provided by the Petroleum Engineering Department, Faculty of 
Engineering, UIR, and the Directorate of Research and C ommunity Service (DPPM), Universitas Islam Riau. 
The authors acknowledge additional support from Universiti Teknologi Malaysia for international 
collaboration. The authors also thank Computer Modeling Group Ltd. for providing the GEM and CMOST 
simulation s oftware used in this study.  
 
6. Declarations 
6.1 Author contribution  
D.F.Putra: conceptualization, methodology, running model CMG GEM & CMOST, deep analysis, writing 
result & discussion. I.A. Lukman: Supervision (co), develop model CMG GEM & CMOST, writing literature, 
visualization. M.H.Putra: Supervision (co), writing intr oduction, investigation data curation, writing review. F. 
Hidayat: Supervision (co), methodology, validation, model review. M. Ariyon: Supervision (co), methodology, 
validation, writing review & editing. 
6.2 Funding statement 
The authors declare that they have no known competing financial interest or personal relationships that could 
have influenced the work reported in paper. 
6.3 Competing interest 
The authors declare that they have known competing financial interest or personal relationships that could 
have influenced the work reported in paper. 
6.4 The use of AI-assisted technologies 
The author(s) used Chatgpt to assist, then authors review and edit the content as required. The authors take 
full responsibility for the publication’s content.

37 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
7. Glossary of terms and symbols 
 
Terms & Symbols Description Unit 
 km Matrix permeability mD 
 kf Fracture permeability mD 
 ϕ Porosity fraction 
 ϕf Fracture porosity fraction 
 qg Gas production rate MSCF/D 
 qo Oil production rate STB/D 
 EUR Estimated Ultimate Recovery ft³ or bbl 
 BHP Bottom Hole Pressure psi 
 WHP Well Head Pressure psi 
 SRV Stimulated Reservoir Volume ft³ 
 USRV Unstimulated Reservoir Volume ft³ 
 P Reservoir pressure psi 
 ΔP Pressure drawdown psi 
 σ Stress psi 
 τ Shear stress psi 
 γ Shear strain dimensionless 
 σH Maximum horizontal stress psi 
 σh Minimum horizontal stress psi 
 σv Vertical stress psi 
 Lf Fracture half-length ft 
 wf Fracture width ft 
 xf Fracture extension distance ft 
 hf Fracture height ft 
 Cf Fracture conductivity md-ft 
 rw Wellbore radius ft 
 t Time day/month/year 
 Sg Gas saturation fraction 
 So Oil saturation fraction 
 μg Gas viscosity cp 
 μo Oil viscosity cp 
 ρ Fluid density lbm/ft³ 
 TOC Total Organic Carbon % 
 nD Nano Darcy permeability nD 
 mD Milli Darcy permeability mD 
 ft Feet ft 
 psi Pound per square inch psi 
 GEM Generalized Equation-of-state 
Model simulator 
— 
 CMOST Computer Modelling Group 
Optimization & Sensitivity Tool 
— 
 Frac-Hit Hydraulic fracture interaction 
between adjacent wells 
— 
 Parent Well Existing producing horizontal well — 
 Child Well Newly drilled infill well near parent 
well 
—

38 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 Hydraulic 
Fracturing 
Reservoir stimulation by high-
pressure fluid injection 
— 
 Non-Darcy Flow Non-linear flow regime in fractures — 
 Drawdown Difference between reservoir 
pressure and flowing pressure 
psi 
 Eagle Ford Shale Unconventional shale formation in 
South Texas, USA 
— 
 IJ Direction Grid orientation in x-y plane — 
 JK Direction Grid orientation in y-z plane — 
 IK Direction Grid orientation in x-z plane — 
 Grid Block Numerical simulation cell in 
reservoir model 
— 
 Horizontal Well Well drilled laterally through 
reservoir layer 
— 
 Condensate Gas Gas reservoir fluid producing liquid 
condensate 
— 
 Recovery Factor 
(RF) 
Percentage of recoverable 
hydrocarbon produced 
% 
 Tubing Performance 
Curve 
Relationship between flow rate and 
pressure in tubing 
— 
 Pressure Depletion Reservoir pressure reduction during 
production 
psi 
 Stress 
Redistribution 
Change of in-situ stress due to 
depletion/fracturing 
— 
 Fracture 
Propagation 
Growth and extension of hydraulic 
fractures 
— 
 Reservoir Drainage 
Area 
Effective production area connected 
to the well 
acre or ft² 
 Cartesian Grid Rectangular reservoir simulation 
grid system 
— 
 Well Spacing Distance between adjacent wells ft 
 Fracture Spacing Distance between hydraulic 
fractures 
ft 
 Hydraulic 
Conductivity 
Ability of fracture system to 
transmit fluids 
md-ft 
 Production 
Interference 
Production interaction between 
neighboring wells 
— 
 Dynamic Interwell 
Fracture Interaction 
Pressure/fracture communication 
between wells 
— 
 
 
8. References 
Ajisafe, F. O., Weijers, L., & Watson, M. C. (2019). Understanding parent -child well interactions in 
unconventional reservoirs through hydraulic fracture diagnostics. In Proceedings of the SPE Hydraulic 
Fracturing Technology Conference and Exhibition. Soci ety of Petroleum Engineers. 
https://doi.org/10.2118/194347-MS 
 
Al-Rbeawi, S. (2020). An approach for the performance -impact of parent-child wellbores spacing and hydraulic 
fractures cluster spacing in conventional and unconventional reservoirs. Journal of Petroleum Science and 
Engineering, 185, Article 106570. https://doi.org/10.1016/j.petrol.2019.106570 
 
Al-Rbeawi, S., & Al-Kaabi, M. (2020). Hybrid modeling of unconventional gas reservoirs considering anomalous 
diffusion, stimulated matrix permeability, and non -Darcy flow. Journal of Natural Gas Science and 
Engineering, 77, Article 103271. https://doi.org/10.1016/j.jngse.2020.103271 
 
Bui, B. T. (2023). Geomechanics in unconventional resource development. arXiv preprint. 
https://arxiv.org/abs/2305.17642 
 
Cipolla, C. L. (2009). Modeling production and evaluating fracture complexity in unconventional gas reservoirs. 
In SPE Hydraulic Fracturing Technology Conference. The Woodlands, TX, USA. 
https://doi.org/10.2118/124898-MS

39 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
Fan, K., Dong, M., Elsworth, D., Li, Y., Yin, C., & Li, Y. (2018). A dynamic -pulse pseudo-pressure method to 
determine shale matrix permeability at representative reservoir conditions. International Journal of Coal 
Geology, 193, 61–72. https://doi.org/10.1016/j.coal.2018.04.011 
 
Ghanbarian, B., Liang, F., & Liu, H.-H. (2020). Gas relative permeability in unconventional reservoir rocks. arXiv 
preprint. https://arxiv.org/abs/2003.08988 
 
Heydari, M., Liang, F., Liu, H. -H., & Ghanbarian, B. (2024). Numerical simulations of geomechanical 
deformation, fluid flow and reactive transport in shale rough -walled microfractures. arXiv preprint. 
https://arxiv.org/abs/2411.07992 
 
Inamdar, A., Malpani, R., Atwood, K., Brook, K., Erwemi, A., Ogundare, T., & Purcell, D. (2010). Evaluation of 
stimulation techniques using microseismic mapping in the Eagle Ford shale. In SPE Tight Gas Completions 
Conference (pp. 136–146). San Antonio, TX, USA. https://doi.org/10.2118/136873-MS 
 
Junira, A., & Wibowo, A. D. (2016). Shale as hydrocarbon reservoirs. Scientific Contributions  Oil and Gas 
(SCOG), 39(2), 145–154. https://doi.org/10.29017/SCOG.39.2.104 
 
Kamari, A., Li, L., & Sheng, J. J. (2018). Effects of rock pore sizes on the PVT properties of oil and gas -
condensates in shale and tight reservoirs. Petroleum, 4(2), 148 –157. 
https://doi.org/10.1016/j.petlm.2017.06.002 
 
Kazemi, H., Merrill, L. S., Porterfield, K. L., & Zeman, P. R. (1976). Numerical simulation of water -oil flow in 
naturally fractured reservoirs. Society of Petroleum Engineers Journal, 16(6), 317 –326. 
https://doi.org/10.2118/5719-PA 
 
King, G. E. (2010). Thirty years of gas-shale fracturing: What have we learned? Journal of Petroleum Technology, 
62(11), 88–90. https://doi.org/10.2118/1110-0088-JPT 
 
Le Calvez, J. H., Klem, R. C., Bennett, L., Erwemi, A., Craven, M., & Palacio, J. C. (2007). Real -time 
microseismic monitoring of hydraulic fracture treatment: A tool to improve completion and reservoir 
management. In SPE Hydraulic Fracturing Technology Conference (pp. 336–342). College Station, TX, USA. 
https://doi.org/10.2523/106159-MS. 
 
Liu, Z., Zhao, H., & Chen, Y. (2026). Study on the fracturing and hit behavior of shale reservoirs under tight well 
spacing conditions. Processes, 14(2), Article 196. 
 
Lolon, E. P., Cipolla, C. L., Weijers, L., Hesketh, R. E., & Grigg, M. W. (2009). Evaluating horizontal well 
placement and hydraulic fracture spacing/conductivity in the Bakken formation, North Dakota. In SPE Annual 
Technical Conference and Exhibition (pp.  3626–3637). New Orleans, LA, USA. 
https://doi.org/10.2118/124905-MS 
 
Stegent, N. A., Wagner, A. L., Mullen, J., & Borstmayer, R. E. (2010). Engineering a successful fracture -
stimulation treatment in the Eagle Ford shale. In SPE Tight Gas Completions Conference (pp. 90 –109). San 
Antonio, TX, USA. https://doi.org/10.2118/136183-MS 
 
Taghichian, A., Hashemalhoseini, H., Zaman, M., & Beheshti Zavareh, S. (2018). Propagation and aperture of 
staged hydraulic fractures in unconventional resources in toughness -dominated regimes. Journal of Rock 
Mechanics and Geotechnical Engineering, 10(2), 249–258. https://doi.org/10.1016/j.jrmge.2017.08.003 
 
Tian, Y., Ayers, W. B., & McCain, W. D. (2014). Regional impacts of lithologic cyclicity and reservoir and fluid 
properties on Eagle Ford shale well performance. In SPE/AAPG/SEG Unconventional Resources Technology 
Conference (pp. 530–543). Denver, CO, USA. https://doi.org/10.2118/169007-MS 
 
U.S. Energy Information Administration. (2011). Review of emerging resources: U.S. shale gas and shale oil 
plays. Washington, DC. 
 
Wang, H., Wang, Y., Chen, Z., & Li, X. (2021). Production forecast and optimization for parent-child well patterns 
in unconventional reservoirs using machine learning methods. Journal of Petroleum Science and Engineering, 
208, Article 109715. https://doi.org/10.1016/j.petrol.2021.109715

40 
 
https://doi.org/10.29017/scog.v49i3.2114 
 
Putra et al. Scientific Contributions Oil and Gas 
 
Wang, L. (2025). Optimization strategies for hydraulic fracturing in unconventional reservoirs: Recent 
developments and production forecasting. International Journal of Earth Sciences Knowledge and 
Applications, 7 (1), 122-127. https://doi.org/10.5281/zenodo.15342893 
 
Warren, J. E., & Root, P. J. (1963). The behavior of naturally fractured reservoirs. Society of Petroleum Engineers 
Journal, 3(3), 245–255. https://doi.org/10.2118/426-PA 
 
Warpinski, N. R., & Teufel, L. W. (1987). Influence of geologic discontinuities on hydraulic fracture propagation. 
Journal of Petroleum Technology, 39(2), 209–220. https://doi.org/10.2118/13224-PA 
 
Winderasta, W. (2017). Unconventional Resources Development: Lessons Learned from North America success. 
In Joint Convention Malang HAGI–IAGI–IAFMI–IATMI. Malang, Indonesia.
