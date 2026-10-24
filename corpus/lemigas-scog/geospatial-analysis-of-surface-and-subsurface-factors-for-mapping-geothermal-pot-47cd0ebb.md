---
source_id: "lemigas-scog"
title: "Geospatial Analysis of Surface and Subsurface Factors for Mapping Geothermal Potential Zones in Central Wester"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2167"
retrieved_at: "2026-10-24T14:30:25+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "47cd0ebb91572447f7e0a5cc0dbf41a11a56050eeb72a862ce5be9ab15a2f9fd"
collected: "manual"
---

# Geospatial Analysis of Surface and Subsurface Factors for Mapping Geothermal Potential Zones in Central Wester

411 
 
https://doi.org/10.29017/scog.v49i3.2167 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 411 – 440 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Geospatial Analysis of Surface and Subsurface Factors for Mapping 
Geothermal Potential Zones in Central-Western Taiz, Yemen 
 
Anwar Abdullah1, Ghareb Hamada2*Abbas Al-Khudafi1,3, Ibrahim Farea4, and Fahd Alakbari5 
 
1Geology Department, Faculty of Applied Sciences, Taiz University, 
Habail Salman, Taiz City, At Ta'iziyah District, Taiz, Republic of Yemen. 
2Oil and Gas Engineering Department, Arab Academy for Science, Technology & Maritime Transport, 
Abu Qir Campus, Alexandria, Egypt. 
3Oil and Gas Engineering Department, Emirates International University, 
Beirut St, Hadda, Sana'a, Yaman. 
4Petroleum & Natural gas Department, Sana’a University, Sana’a, 
Sana'a University, Sana'a, Yaman. 
5Interdisciplinary Research Center for Hydrogen Technologies and Carbon Management, 
King Fahd University of Petroleum & Minerals, 
Dhahran 31261, Saudi Arabia.  
*Corresponding author: Ghareb Hamada (ghareb.hamada@aast.edu) 
Ghareb Hamada: Scholar id: https://scholar.google.com/citations?hl=en&user=rKaaJHkAAAAJ 
Received:  27 February 2026; Revised: in revised form 24 June 2026; Accepted: 06 August 2026 
Available: online 30 September 2026. 
  
 
 
ABSTRACT - This study evaluates the application of remote sensing and GIS techniques for mapping geothermal 
potential areas in the central-western Taiz, Yemen. The objective is to identify prospective areas for hydrothermal 
water exploration. Geothermal potential map ping was based on nine factors derived from remote sensing, 
geological, and geophysical datasets. Several steps were used to prepare these factors such as rasterization, re -
projection, re-sampling, classification and weighting. The weighted values of the classes for each factor map were 
assigned based on their spatial correlation with eight known hydrothermal water locations. A GIS-based Weighted 
Overlay Technique (WOT) was applied. The resulting geothermal potential map categorizes the area into five 
classes: very high, high, moderate, low, and very low, covering 5.08%, 9.65%, 14.65%, 50.46%, and 20.16% of 
the study area, respectively. However, 7 of the 8 hydrothermal occurrences identified (87.5%) are located in the 
very high potential zone. The observed c oncentration is approximately seventeen times greater than random 
expectation, providing further evidence that the model is able to identify areas favorable for geothermal 
occurrence. This supports logical consistency but is not proof of independent valida tion. Independent field data 
are needed to validate the predictive power of the map. Given the limited number of validation points, the results 
should be considered as a regional screening tool. 
Keywords: remote sensing, GIS, weighted overlay technique, geothermal potential mapping. 
  
 
How to cite this article: 
Anwar Abdullah, Ghareb HamadaAbbas Al-Khudafi, Ibrahim Farea, and Fahd Alakbari , 2026, 
Geospatial Analysis of Surface and Subsurface Factors for Mapping Geothermal Potential Zones in 
Central-Western Taiz, Yemen, Scientific Contributions Oil and Gas, 49 (3) pp. 411-440.

412 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
1. Introduction 
Geothermal energy represents a sustainable and reliable renewable energy resource derived from the Earth’s 
internal heat and can be utilized for electricity generation, direct heating, and various industrial applications. 
Geothermal systems are commonly associated with regions characterized by elevated heat flow, active tectonics, 
and volcanic or magmatic processes, where fractures and faults facilitate the circulation of heated fluids within 
the crust (Zhou & Liu 2021; Kumar & Singh 2019; Macharia et al., 2018). 
Hydrothermal systems form when meteoric water infiltrates the subsurface through fractures and permeable 
zones, is heated at depth by hot rocks or magmatic sources, and subsequently migrates upward, sometimes 
manifesting at the surface as hot springs  (Baker & Johnson 2020). In other cases, hydrothermal fluids remain 
trapped at depth due to insufficient permeability and can only be accessed through drilling. Structural features 
such as faults, joints, and lithological contacts play a critical role in controlling fluid flow and geothermal reservoir 
development (Heasleret al., 2009; Taillefer et al., 2017).  
Here, the term "hydrothermal water" is defined as naturally occurring groundwater heated by the Earth's 
internal heat during circulation through permeable rocks, fractures, and fault systems. Hydrothermal water 
represents the fluid component of hydrothermal geothermal systems and commonly occurs as hot springs or warm 
groundwater, although it may also remain confined at depth. In contrast, the term "geothermal systems" is broader 
and includes all geological environments capable of storing and transferring g eothermal heat, including 
hydrothermal systems, vapor -dominated systems, and enhanced geothermal systems (EGS). Since the present 
study aims to identify zones favorable for hot-water resources, the term "hydrothermal water" is used throughout 
the manuscript to emphasize groundwater-based geothermal occurrences. 
The Taiz Governorate in southwestern Yemen is located within a tectonically active zone influenced by the 
opening of the Red Sea and the Gulf of Aden (Abdullah et al., 2010; Abdullah et al., 2013; Nassr & Abdullah 
2015). This regional extensional regime has resulted in complex fault systems trending predominantly NW –SE 
and NE –SW, creating favorable conditions for geothermal activity. Numerous geothermal manifestations, 
including hot springs and warm domestic wells with t emperatures ranging from approximately 32 °C to 75 °C, 
have been reported in the Taiz region (Alnethary et al., 2024). However, these studies mainly provide regional -
scale information and they do not offer a detailed assessment of geothermal potential in the study area. These 
characteristics indicate a significant but underexplored geothermal potential. There are no publ ished heat-flow 
measurements or detailed geothermal gradient data for the study area. Thus, the evaluation of geothermal potential 
is based mainly on geological, geomorphological, hydrothermal and geophysical indicators. 
Recent advances in remote sensing and Geographic Information Systems (GIS) have facilitated the efficient 
integration of surface and subsurface geospatial data for geothermal exploration (Ramsey 2013). Furthermore, 
GIS-based multi-criteria approaches, particularly weighted overlay techniques, have been extensively employed 
to delineate geothermal potential zones by integrating geological, geomorphological, and geophysical controlling 
factors (Ramsey & Harris 2013; Haselwimmer & Prakash 2013; Bernard 2020; El Morabit et al., 2021; David & 
Pablo 2019; Reda et al., 2022 ; Abdulkadir et al., 2022) . More recently, machine learning techniques have been 
coupled with GIS and remote sensing datasets for improved geothermal prospectivity mapping. For example, 
Kehinde et al. (2023)  showed the success of GIS -based machine learning algorithms for geothermal energy 
potential modeling in Southwestern Nigeria based on geophysical and remote sensing data. Al-Kadasi et al. (2020) 
analyzed aeromagnetic data to estimate Curie point depths in southwestern Yemen. Their results revealed 
relatively shallow magnetic sources, suggesting areas of increased subsurface heat flow. This evidence further 
reinforces the view that southwestern Yemen has promising geothermal potential. 
Recent advances in artificial intelligence (AI) have significantly improved geothermal exploration by 
integrating machine learning with geological, geophysical, and remote sensing data. In Yemen, Al-Fakih et al. 
(2025) developed Bayesian-optimized machine learning models for geothermal temperature prediction, while Al-
Gathe et al. (2025) proposed a hybrid AI framework that further enhanced prediction accuracy. Similarly, Aydınlı 
et al. (2026)  demonstrated the effectiveness of combining remote sensing and machine learning for early -stage 
geothermal prospecting in Türkiye. A recent review by Aliyu et al. (2026)  further highlighted that AI -driven

413 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
approaches are becoming the preferred methodology for geothermal prospectivity mapping worldwide. These 
advances indicate that AI techniques provide a promising direction for future geothermal exploration in Yemen, 
complementing conventional GIS-based approaches adopted in the present study. 
Despite the presence of known hydrothermal manifestations in the Taiz region, geothermal exploration 
remains limited and largely unsystematic. Existing studies are fragmented and do not provide a comprehensive 
spatial assessment of geothermal potential tha t integrates surface and subsurface controlling factors. Moreover, 
field-based investigations are constrained by accessibility, cost, and security challenges, highlighting the need for 
an efficient, data -driven, and reproducible methodology to identify pro spective geothermal zones. To date, no 
integrated GIS-based geothermal potential mapping framework has been systematically applied to the central –
western part of the Taiz Governorate. 
The main objective of this study is to delineate geothermal potential zones in the central –western Taiz 
region, Yemen, using an integrated remote sensing and GIS -based weighted overlay approach. Note that this 
study is for hot water dominated geothermal systems and does not include high enthalpy steam or EGS systems. 
We suggest that structural features (faults, lineaments) are the main controls on geothermal potential in this 
rift-influenced setting.  
This study investigates the geospatial factors influencing geothermal resource distribution in the central –
western Taiz region, evaluates the integration of remote sensing, geological, and geophysical data within a GIS -
based framework to identify geothermal potential zones, maps their spatial distribution, and quantifies their areas. 
It also assesses the correspondence between predicted high -potential zones and known hydrothermal water 
occurrences to validate the model's accuracy. Figure 1 illustrates the location of the Taiz region in Yemen and the 
detailed study area. 
 
2. Methodology 
In geothermal exploration, hydrothermal mapping is concerned with identifying surface and subsurface 
conditions that control the circulation, storage, and discharge of thermally heated groundwater. In this study, 
remote sensing, geological, and geophysical  datasets are integrated within a GIS framework to delineate zones 
favorable for geothermal and hydrothermal water occurrence in the central –western Taiz region. The chosen 
methodology places a strong emphasis on subsurface geophysical indicators —such as t hose affecting 
permeability, fluid pathways, and heat transfer—along with structural controls (faults, lineaments, and lithological 
contacts) and geomorphological factors. 
The methodology consists of five main sequential stages: data acquisition, data pre -processing, factors maps 
generation, application of the Weighted Overlay Technique (WOT), and validation of the final geothermal 
potential map. Figure 22 presents overall workflow of the methodology used to map geothermal potential, 
illustrating the main stages of the study, including data acquisition, preprocessing, preparation of thematic factor 
maps, factor weighting, weighted overlay analysis, and validation of the final results. 
2.1 Data acquisition  
Three categories of datasets were used to generate nine geospatial factors controlling geothermal 
occurrence. DEM processing and drainage extraction was carried out using PCI Geomatica. Lineament 
interpretation and weighted overlay modelling was done using  ILWIS. Density mapping and raster processing 
was done using ArcGIS.  
2.2 Digital data  
Shuttle Radar Topography Mission (SRTM) digital elevation data with a spatial resolution of 30 m were used 
to generate a Digital Elevation Model (DEM) (Figure 2). The DEM was further processed to produce a shaded 
relief image (Figure 3) and to derive slope, drainage, and lineament information.

414 
 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 1. 
Location of the Taiz region in Yemen (red) and the detailed study area (yellow).

415 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
The slope layer, derived from the DEM, represents terrain steepness. It is a critical factor influencing surface 
runoff, infiltration rates, and hydrothermal fluid circulation. 
Gentle slopes generally favor water infiltration, while steep slopes promote rapid runoff. Geothermal 
manifestations and hydrothermal waters are often associated with relatively low topographic areas; therefore, the 
slope elevation steepness factors was used to assess the relationship between terrain characteristics and geothermal 
potential. 
Drainage networks were automatically extracted from the DEM using the DRAIN function in PCI Geomatica. 
Drainage patterns may indicate structural controls and pathways favorable for hydrothermal fluid migration 
(Figure 4) . 
Lineaments, representing natural zones of structural weakness within the crust (Rutty 1993; Bai et al., 2010, 
Abdullah et al., 2013 , Nassr & Abdullah 2015), were manually interpreted from the shaded relief image using 
ILWIS software based on visual interpretation and user experience (Figure 5). These features are important 
indicators of potential pathways for geothermal fluid movement. The SRTM 30 m DEM used in this study has a 
typical absolute vertical accuracy of about ±10 m. While such uncertainty may be acceptable for local topographic 
details, it is generally acceptable for local and regional -scale analysis of slope, drainage pattern and structural 
features (lineaments) mapping. Hence, the impact of the DEM vertical error on the results is expected to be limited. 
Although some degree of interpreter subjectivity is involved in the manual extraction of lineaments, all 
lineaments were identified and digitized by the same experienced analyst, applying uniform interpretation criteria 
to ensure methodological consistency throughout the study. 
 
Figure 2. 
Digital elevation model of the study area derived from SRTM data.

416 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
 
 
Figure 3. 
Shaded relief map generated from the DEM of the study area. 
 
2.3 Geological data    
A 1:250,000 scale geological map of the Taiz area (Geological Survey of Yemen (GSY 1990)  was used to 
create three factors. 
• Rock Units: The different rock units were digitized from the geological map (Figure 6). Variations in 
porosity, permeability, and the presence of joints, fissures, and fractures influence hydrothermal water 
movement. 
357998 
 1525866 
414078 
 1525866 
 1463057 
357998 
 1463057 
414078 
25 km 0

417 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
• Geological Faults:  Faults were digitized from the geological map (Figure 7) . These structures act as 
critical conduits for the movement of hydrothermal fluids from depth to the surface (Ibrahim & 
Juhari 1990) . 
• Lithological Contacts: Contacts between different rock types were digitized (Figure 8). These zones often 
represent planes of weakness that can facilitate fluid movement. 
 
 
Figure 4.  
Drainage pattern extracted from the DEM of the study area. 
Geophysical data reveal subsurface geological structures such as faults. Three faults’ datasets at different 
depths were interpreted from residual, regional, and reduced -to-pole aeromagnetic anomaly maps. Datasets at 
different depths, derived from magnetic data analysis by Al Kadasi (2014), were used: 
 
357998 
 
1525866 
414078 
 
1525866 
357998 
 1463057 
 
 
 1463057 
 
 414078 
25 km 0

418 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
Faults at −38.3 m depth from residual magnetic anomalies (Figure 9) . Faults at −95.5 m depth from the 
regional magnetic map (Figure 10). Faults at −144.4 m depth from the reduced-to-the-pole (RTP) aeromagnetic 
map (Figure 11). 
 
 
 
Figure 5. 
Lineament map interpreted from the shaded relief image of the study area 
The depths of −38.3 m, −95.5 m, and −144.4 m represent the quantitative results of spectral analysis applied 
to the aeromagnetic data (Al-Kadasi 2014). These values were derived from the slope of the power spectrum curve 
during the transformation from the spatial to the frequency domain. It is important to note that the decimal 
precision reflects the mathematical outcome of the Fourier analysis and the subsequent depth calculation 
formula Depth=−Slope/4π, rather than an absolute vertical measurement accuracy. 
 
 
1525866 357998 
357998 
 1525866 
414078 
 1525866 
357998 
 1463057 
414078 
 1463057 
25 km 0

419 
 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
 
Figure 6. 
Digitized rock units of the study area (Digitized and adapted from Geological Survey of Yemen (1990) with modifications for GIS integration)

420 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
 
Figure 7. 
Digitized geological faults of the study area 
(digitized and adapted from Geological Survey of Yemen 1990, with modifications for GIS integration). 
 
2.4 Geophysical data 
The depths of −38.3 m, −95.5 m, and −144.4 m represent the quantitative results of spectral analysis applied 
to the aeromagnetic data (Al-Kadasi 2014). These values were derived from the slope of the power spectrum curve 
during the transformation from the spatial to the frequency domain. It is important to note that the decimal 
precision reflects the mathematical outcome of the Fourier analysis and the subsequent depth calculation 
formula Depth=−Slope/4π, rather than an absolute vertical measurement accuracy. 
25 km 0 
357998 
 1525866 
414078 
 1525866 
 1463057 
357998 
 1463057 
414078

421 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 8. 
Digitized lithological contacts of the study area 
(digitized and adapted from Geological Survey of Yemen 1990, with modifications for GIS integration). 
2.5 Data pre-processing 
The following steps were applied to prepare the datasets for GIS integration: 
• Generation of the DEM (elevation) and creation of a gradient shader image for lineament extraction. 
• Automatic extraction of the drainage network using the DRAIN function in PCI Geomatica. 
• Manual digitization of rock units , geological faults and lithological contacts, from the geological map. 
And subsurface geophysical faults with different depth  (shallow, intermediate and deep) from previous 
work. 
• Reprojection and spatial alignment of all datasets to a unified coordinate system. 
• Conversion of all vector layers (drainage, lineaments, faults, contacts) into raster density maps using a 
circular search radius of 1000 m. Because the original datasets have a spatial resolution of 30 m, a 
circular search radius of 1000 m was used to generate the density maps. This radius was chosen as it 
offers a practical balance between preserving local spatial variations and reducing noise. As a result, the 
357998 
 1525866 
414078 
 1525866 
 1463057 
357998 414078 
 1463057 
25 km 0 
 
1525866 
357998

422 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
generated density maps are smoother, more reliable, and easier to interpret while still retaining the key 
spatial patterns relevant to the analysis. 
• All vector layers—including drainage networks, lineaments, geological faults, lithological contacts, and 
faults determined from magnetic anomaly map systems were converted into raster density maps using 
the Line Density tool in ArcGIS (equivalent kernel density functions in PCI Geomatica and ILWIS). This 
tool calculates the density of linear features within a neighbourhood surrounding each raster cell. 
A circular search radius of 1000 m was applied based on the spatial distribution of known hydrothermal 
manifestations and the average spacing of structural features in the study area. The density calculation 
follows the kernel density estimation principle, where a smooth curved surface is fitted over each line 
segment, with the surface value highest at the lin e location and decreasing to zero at the search radius 
distance. The density at each output raster cell is computed by summing the values from all overlapping 
kernel surfaces. 
 
Figure 9. 
Shallow faults interpreted from residual magnetic anomalies at a depth of −38.3 m 
(digitized and adapted from Al-Kadasi 2014, with modifications for GIS integration). 
 
357998 
 1525866 
414078 
 1525866 
414078 357998 
 1463057  1463057 
25 km 0

423 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
The search radius of 1000 m was chosen to be twice the average nearest -neighbor distance between known 
hydrothermal points (~500 m), so that each point would influence at least one adjacent cell. 
 
 
Figure 10. 
Intermediate faultsinterpreted from residual magnetic anomalies at a depth of −95.5 m 
(digitized and adapted from Al-Kadasi 2014, with modifications for GIS integration). 
 
 
 
357998 
 1525866 
414078 
 
1525866 
357998 
 1463057 
414078 
 1463057 
25 km 0

424 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 11. 
Deep faults interpreted from residual magnetic anomalies at a depth of −144.4 m 
(digitized and adapted from Al-Kadasi 2014, with modifications for GIS integration). 
2.6 Factor Maps Generation 
Nine geothermal controlling factor maps were produced, including elevation steepness, drainage density, 
lineament density, geological fault density, lithological contact density, three levels of faults determined from 
magnetic anomaly map density, and rock unit distribution. Each raster layer was reclassified into five categories 
representing different levels of geothermal influence. The resulting reclassified factor maps are presented in 
Figure 13–Figure 20. In general, the chart of workflow used in this study was illustrated in the Figure 12. 
357998 
 1525866 
414078 
 1525866 
414078 357998 
 1463057  1463057 
25 km 0

425 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 12. 
Workflow for geothermal potential mapping 
 
 
Figure 13. 
Reclassified elevation steepness map of the study area.

426 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 14. 
Drainage density map of the study area. 
 
 
 
Figure 15. 
Lineament density map of the study area.

427 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 16. 
Geological fault density map of the study area 
 
 
 
Figure 17. 
Lithological contacts density layer of the study area

428 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 18. 
Faults determined from magnetic anomaly maps with -38.3 m in depth density layer of the study area. 
 
 
 
Figure 19. 
Density map of intermediate-depth faults determined from magnetic anomaly maps at −95.5 m.

429 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Figure 20. 
Density map of deep faults determined from magnetic anomaly maps at −144.4 m depth. 
 
2.7 Weighted overlay analysis 
A point map of eight known hydrothermal water locations was generated (Figure 21). A matching analysis 
was performed between these points and the classes of each sliced factor map. The number of matching points 
per class was used to calculate a weight value (WV) using equation (1): 
If 8 hydrothermal locations correspond to the weight value (WV) for each class was calculated based on the 
number of hydrothermal locations (𝑁𝐻𝐿𝐶) falling within that class, scaled to a maximum weight of 5, as follows: 
𝑊𝑉 =
𝑁𝐻𝐿𝐶×5
8     (1) 
 
where  𝑊𝑉, and 𝑁𝐻𝐿𝐶 are weight value of class,  the number of hydrothermal locations matching the class , 
respectively. 
The calculated weights for all classes across the nine factor maps range from 0 to 5 and are presented in 
Table 1 . A weight of 5 indicates a class highly correlated with known hydrothermal sites, while 0 indicates no 
correlation. 
The limited number of known hydrothermal points (n=8) is an acknowledged limitation and the weighting 
scheme and validation should be considered preliminary until further field data become available. 
2.8 Justification of the weighting scheme 
The weighting scheme applied here is based on an empirical frequency -ratio approach in which the class 
weights are proportional to the spatial coincidence with known hydrothermal manifestations. This is based on the

430 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
assumption that areas with higher numbers of known sites per class are more prospective. The linear scaling from 
0 to 5 is heuristic but preserves the relative ranking of factor classes without introducing arbitrary expert bias. The 
geothermal relevance labels reported in Table 1 were assigned consistently with the empirically calculated class 
weights derived from the spatial correspondence between hydrothermal occurrences and each factor class. 
However, this approach does not take into account nonlinear interactions between factors, a limitation that should 
be addressed in future studies using probabilistic or machine learning models. 
Table 1. 
Thematic map layers and weighted values for mineral potential mapping 
A. 
Topographic and geophysical data 
Map layer Classes Number of points Weighted value Geothermal relevance 
Elevation (m) 
<500 m 0 0 Very Low 
500-1000 m 3 1.875 Low 
1000-1500 m 3 1.875 Low 
1500-2000 m 1 0.625 Very Low 
>2000 m 0 0 Very Low 
Reduced to Pole Aeromagnetic 
Faults 
<500 km/km² 4 2.5 Moderate 
500-1000 km/km² 3 1.875 Low 
1000-1500 km/km² 1 0.625 Very Low 
1500-2000 km/km² 0 0 Very Low 
>2000 km/km² 0 0 Very Low 
Residual Magnetic Anomalies 
<350 km/km² 5 3.125 High 
350-700 km/km² 1 0.625 Very Low 
700-1050 km/km² 2 1.25 Low 
1050-1400 km/km² 0 0 Very Low 
>1400 km/km² 0 0 Very Low 
 
B. 
Structural features 
Map layer Classes Number of points Weighted value Geothermal relevance 
Drainage Pattern  
<500 km/km² 0 0 Very Low 
500-1000 km/km² 3 1.875 Low 
1000-1200 km/km² 0 0 Very Low 
1200-1500 km/km² 0 0 Very Low 
1500-1800 km/km² 0 0 Very Low 
1800-2400 km/km² 0 0 Very Low 
>2400 km/km² 0 0 Very Low 
Faults 
<700 km/km² 6 3.75 High 
700-1400 km/km² 0 0 Very Low 
1400-2100 km/km² 2 1.25 Low 
2100-2800 km/km² 0 0 Very Low 
>2800 km/km² 0 0 Very Low 
Regional Magnetic 
Faults 
 
  
<300 km/km² 5 3.125 High 
300-600 km/km² 2 1.25 Low 
600-900 km/km² 0 0 Very Low 
900-1200 km/km² 1 0.625 Very Low 
>1200 km/km² 0 0 Very Low 
Lineaments 
<1000 km/km² 3 1.875 Low 
1000-2000 km/km² 5 3.125 High 
2000-3000 km/km² 0 0 Very Low 
3000-4000 km/km² 0 0 Very Low 
>4000 km/km² 0 0 Very Low

431 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
C. 
Lithological Units 
Map layer Classes Number of points Weighted value Geothermal relevance 
Rock Units 
Paragneiss 0 0 Very Low 
Amran limestone 0 0 Very Low 
Tawilah sandstone 2 1.25 Low 
Basalt 3.5 2.187 Moderate 
Trachyte 0 0 Very Low 
Rhyolite and dacite 1 0.625 Very Low 
Ignimbrite and ashflow deposits 1.5 0.937 Very Low 
Contact Types 
<800 km/km² 7 4.375 Very Low 
800-1600 km/km² 1 0.625 Very Low 
1600-2400 km/km² 0 0 Very Low 
2400-3200 km/km² 0 0 Very Low 
>3200 km/km² 0 0 Very Low 
Granite 0 0 Very Low 
Granodiorite 0 0 Very Low 
Gabbro 0 0 Very low 
Active alluvium 0 0 Very Low 
Gravels 0 0 Very Low 
Loess and ancient dunes 0 0 Very Low 
Colluvium 0 0 Very Low 
 
 
Figure 21. 
Field locations of known hydrothermal water occurrences used for model validation.  
 1463057 
357998 
357998 
 1525866 
414078 
 1525866 
 1463057 
25 km 0 
 414078

432 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
2.9 GIS model and the geothermal potential map 
All geo-factors layers used in the geothermal potential assessment were first converted into raster format and 
standardized before being combined. To maintain spatial consistency across the analysis, all datasets were re -
projected to the Universal Transverse Mercator (UTM) coordinate system, Zone 38N, and re-sampled to a uniform 
spatial resolution of 100 m. This pre -processing step ensured that the different geothermal conditioning factors 
could be directly compared and accurately overlaid. 
The weighted factor maps were imported into a GIS model within ILWIS software. All maps were re -
projected, geo-referenced, and re-sampled spatially to a uniform 100 m resolution. The cell size was selected to 
align with the spatial resolution of the availa ble hydrothermal occurrence data and the regional scope of the 
geothermal assessment. Then the thematic layers were combined using Weighted Overlay Technique (WOT). 
Factor classes were weighted according to their spatial correspondence to known occurrences  of hydrothermal 
activity. For each thematic layer, class weights were assigned according to the number of hydrothermal 
manifestations within each class using the empirical weighting approach described in previous section. Then the 
weighted layers were combined to give the final map of geothermal potential. 
The final geothermal potential map was generated using the WOT model by calculating the arithmetic mean 
of the nine weighted factor maps using the Equation 2. The resulting continuous suitability values were then 
classified into five geothermal potential categories: very high, high, moderate, low, and very low (Figure 22). 
Potential Map =
1
9 ∑ 𝑊𝐹𝑀𝑖9𝑖=1    (2) 
where 𝑊𝐹𝑀 and 9 are weighted factor maps, total number of factors being integrated, respectively. 
  
3. Result and Discussion 
Although the sample size was small (n = 8), a preliminary receiver operating characteristic (ROC) analysis 
was performed by binarizing the potential map (very high + high = positive; moderate, low, and very low = 
negative). The resulting area under the ROC  curve (AUC) was 0.81, indicating moderate predictive 
discrimination. Because the analysis was based on only eight validation points, the AUC estimate is subject to 
considerable statistical uncertainty and should therefore be interpreted as exploratory rather than definitive. 
However, this result is exploratory and should be interpreted with caution given the circularity noted above. 
This study represents the first effort to integrate remote sensing data, geological mapping, and aeromagnetic 
fault interpretations at multiple de pths within a GIS -based weighted overlay framework to assess geothermal 
potential in the Central -Western Taiz region. In this study, the term 'Elevation' is used to refer to the absolute 
value in meters above sea level, while the term 'Slope' is used to re fer to the degree of terrain inclination 
measured in degrees (°). Nine key controlling factors were selected: elevation steepness, slope, drainage 
density, lineament density, rock units, rock contact density, and faults determined from magnetic anomaly map  
density at three depths . 
Spatial analysis revealed elevations ranging from 404 m to 2690 m above sea level (Figure 13). Slope values 
in the study area range from 0° to >45°, with gentle slopes (<10°) covering approximately 35% of the area, 
predominantly in valleys and low -lying regions. Analysis of the relationship between slope classes and known 
hydrothermal sites indica tes that areas with gentle slopes (0 -10°) show higher correlation with geothermal 
manifestations, as these areas typically facilitate groundwater recharge and hydrothermal fluid circulation (Figure 
12). Lower elevations (<500 m) also correlate with higher geothermal potential, likely due to their association 
with regional base levels and fault -controlled valleys. A total of 354 lineaments and 216 geological faults were 
identified with a predominant NW-SE and NE-SW trends (Figure 5 and Figure 15). High densities of lineaments, 
faults, and lithological contacts were consistently associated with enhanced secondary porosity and permeability, 
thereby correlating with elevated geothermal potential (Figure 7 – Figure 8 and Figure 16 – Figure17). Similarly,

433 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
areas of low drainage density favored groundwater infiltration and fluid movement (Figure 4 and Figure 14). 
Geological analysis identified fifteen rock units, with Early Tertiary basalts and fractured Cretaceous sandstones 
showing strong association with hydrothermal manifestations. 
Applying the weighted overlay technique, the final potential map classified the area as: Very High (5.08%± 
X%), High (9.65%± X%), Moderate (14.65%± X%), Low (50.46%± X%), and Very Low (20.16%± X%). Very 
high geothermal potential zones are concentrated in c entral-northeastern (Taiz city to Qaedah), central -southern 
(Dabab), central-northwestern (Rubayi to Resyan), and southern sectors (J. Habashi, Maafir, Brakani to Safyah). 
Validation was performed using the eight documented hydrothermal occurrences availab le in the study area. 
Seven out of eight points (87.5%) fall within the “very high” potential zone. 
 
Table 2. 
Preliminary confusion matrix for the binary geothermal potential classification 
 Predicted  
Actual 
 (Very High + High) (Moderate + Low + Very Low) 
 
Hydrothermal 
occurrence present 7 1 
 
Hydrothermal 
occurrence absent - -  
 
Binarizing the map (very high + high = positive) yielded a true positive rate of 0.875. A preliminary receiver 
operating characteristic (ROC) analysis gave an AUC of 0.81 (95% CI wide due to small n), suggesting moderate 
predictive discrimination. However,  this result is exploratory and must be interpreted with caution given the 
circularity noted above (Table 2). 
Although the small number of validation sites limits statistical robustness, the observed spatial agreement is 
substantially higher than random expectation and provides indicative support for the model’s predictive capability. 
Therefore, the map should be interpreted primarily as a regional screening tool rather than as a rigorous 
quantitative assessment of predictive accuracy. It should be emphasized that the current validation reflects internal 
consistency rather than independent predictive validation bec ause the weighting procedure and the model 
evaluation relied on the same hydrothermal occurrence dataset. Therefore, future studies should validate the 
proposed framework using an independent dataset collected from additional hydrothermal occurrences, fiel d 
investigations, drilling results, or newly acquired geothermal observations to provide a more rigorous assessment 
of the model's predictive capability. 
While seven of the eight documented hydrothermal manifestations (87.5%) were successfully identified within 
the very high geothermal potential zone. occurrence was located in an area classified as having lower geothermal 
potential. This discrepancy may reflect local geological characteristics that are not fully captured by the regional-
scale datasets used in the present study. In particular, the occurrence may be associated with small-scale fractures, 
localized zones of enhanced permeability, or subsurface fluid pathways that fall below the spatial resolution of 
the available geological, geophysical, and remote sensing data. Furthermore, the weighted overlay method is 
primarily designed to highlight broad regional patterns and therefore may not adequately re present isolated 
geothermal features that are weakly connected to the dominant structural controls recognized across the study 
area. This limitation underscores the need for integrating higher -resolution geophysical investigations, detailed 
structural fiel d mapping, and hydrochemical analyses in future research to improve the identification and 
characterization of localized geothermal systems. 
Lineament density, geological faults, and shallow faults determined from magnetic anomaly maps emerged as 
the most important factors, showing a strong spatial relationship with areas of high geothermal potential and 
existing hydrothermal manifestations. Th is finding supports the widely recognized role of structural features in 
controlling fluid movement within geothermal systems, particularly in extensional tectonic environments such as

434 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
the East African Rift and the margins of the Red Sea (Macharia et al., 2018 ; Levi & Antony 2014; Reda et al., 
2022). The observed relationship may also be linked to the tectonic influence of Red Sea and Gulf of Aden rifting 
processes, which has likely contributed to geothermal activity in southwestern Yemen, as suggested by recent 
work of Alnethary et al. (2024) . Nevertheless, although these spatial patterns provide valuable insights, the 
underlying processes governing geothermal occurrence in the study area remain uncertain. Additional field 
investigations, geophysical surveys, and subsurface studies are needed to confirm these relationships and better 
understand the mechanisms controlling geothermal resource distribution. 
Al-Kadasi et al. (2020) reported Curie point depths of approximately 10–15 km in the Taiz region, indicating 
a comparatively warm crust and higher thermal gradients. These findings provide independent geophysical 
support for the geothermal manifestations and potential zones mapped in this study. 
Methodologically, while the GIS-based weighted overlay approach follows established frameworks (Abdullah 
et al. 2025 ; Bernard 2020; El Morabit et al., 2021) , this study advances prior work by integrating multi -depth 
aeromagnetic fault data to explicitly model subsurface structural controls (Figure 9 – Figure 11, Figure 18 – Figure 
20). The resulting framework offers a transferable, optimized tool for site selection in future geothermal or 
groundwater drilling campaigns, enhancing exploration success rates in underexplored rift settings. A cross -
analysis between the factor layers and th e high -potential zone area was performed to determine the relative 
importance of each factor (Table 3) . Lineaments (73.6%), geological faults (65.9%), and shallow faults 
determined from magnetic anomaly maps (−38.3 m depth, 60.4%) were the most significant factors, underscoring 
the strong relationship between geothermal potential and geological structural features. This highlights the 
important role of the regional tectonic setting (Red Sea and Gulf of Aden rifting) in geothermal occurrence in the 
study area. 
 
Figure 22. 
Final geothermal potential zonation map of the study area produced using the weighted overlay technique. 
 
 
357998 414078 
  1525866 1525866 
 1463057 
357998 
 
414078 
1463057 
0 25 km

435 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
Table 3. 
Relative contribution of each factor to the high geothermal potential zones 
No. Factors Importance, % 
1 Elevation Steepness 18.3 
2 Drainage 44.2 
3 Lineament 73.6 
4 Geological Faults 65.9 
5 Rock Units 43.6 
6 Rock Contacts 46.8 
7 Faults from magnetic anomaly maps at -38.3 m depth 60.4 
8 Faults from magnetic anomaly maps at -95.5 m depth 27.4 
9 Faults from magnetic anomaly maps at -144.4 m depth 31.7 
 
In this study, a purely deterministic GIS -based weighted overlay approach is adopted. Such methods are 
good for regional screening, but do not provide a measure of uncertainty in the prediction, or learn complex 
nonlinear relationships. Future geothermal p otential mapping in Yemen should explore complementary 
pathways such as recent advances in machine learning (e.g. random forest, MaxEnt) and probabilistic Bayesian 
networks, once a larger validation data set becomes available.  The deterministic GIS -based weighted overlay 
approach adopted in this study offers high interpretability and is particularly suitable for data -scarce 
environments such as Yemen. Nevertheless, recent studies suggest that machine learning algorithms —
including Random Forest, Gradient Boo sting, Bayesian Optimization, and hybrid ensemble models —can better 
capture nonlinear interactions among geothermal controlling factors when sufficiently large training datasets 
are available (Al-Fakih et al., 2025 ; Al-Gathe et al., 2025 ; Aydınlı et al., 2026) . Therefore, the geothermal 
potential map developed in this work may serve as an initial knowledge base for future AI -assisted geothermal 
exploration and probabilistic resource assessment.  There are no published heat -flow measurements or detailed 
geothermal gradient data for the study area. Thus, the evaluation of geothermal potential is based mainly on 
geological, geomorphological, hydrothermal and geophysical indicators. A limitation of th e present study is the 
lack of direct thermal subsurface data, which points to the need for future geothermal gradient measurements, 
heat-flow investigations, and exploratory drilling to confirm the predicted zones of geothermal potential. 
Although the model shows a strong spatial relationship with known hydrothermal occurrences, it should be 
viewed as a tool for generating hypotheses rather than providing definitive confirmation. The mapped geothermal 
potential zones highlight areas that are more likely to host geothermal resources based on the integration of surface 
and subsurface geospatial indicators, but they do not serve as direct proof of their existence. Therefore, these 
results are best used to prioritize exploration efforts and guid e field investigations. Ultimately, any predicted 
geothermal systems must be verified through independent studies, including hydrogeological surveys, 
geochemical and geophysical analyses, and exploratory drilling. 
3.1 Thermal characteristics of Central-Western Taiz 
The geothermal potential of the central–western Taiz region is controlled not only by geological structures but 
also by the regional thermal conditions linked to the tectonic evolution of south western Yemen. The study area 
lies within the Red Sea –Gulf of Aden rift system, a major extensional zone characterized by crustal thinning, 
faulting, and enhanced upward heat transfer from deeper parts of the Earth. Such tectonic settings are widely 
recognized as favorable environments for geothermal activity because  they often exhibit elevated geothermal 
gradients and increased heat flow.  Although direct measurements of geothermal gradients, heat flow, and 
subsurface temperatures are scarce in the study area, several indirect indicators point to favorable thermal 
conditions. Thermal manifestations, including hot springs and warm groundwater wells with temperatures ranging 
from about 32°C to 75°C, have been reported across southwestern Yemen (Alnethary et al., 2024). These features 
suggest that groundwater is circulating through deep-seated fractures and faults, where it is heated before returning 
to the surface. Regional magnetic studies provide further evidence of elevated subsurface temperatures.

436 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
Using aeromagnetic data, Al-Kadasi et al. (2020) estimated Curie Point Depth (CPD) values for south western 
Yemen. The Curie Point Depth corresponds to the depth at which magnetic minerals lose their magnetic properties 
due to high temperatures, typically around 580°C for magnetite. In general, shallower CPD values are associated 
with higher geothermal gradients and greater crustal heat flow. The CPD estimates reported for south western 
Yemen indicate relatively warm crustal conditions that are consistent with the region’s active rift-related tectonic 
setting. While the main focus of this study is the identification of structural and hydrogeological controls using 
remote sensing, geological, and geophysical data, the available thermal evidence provides important support for 
the geothermal interpretation. The regional rift setting, the presence of thermal manifestations, and the Curie Point 
Depth results collectively suggest the existence of a favorable heat source at depth. Therefore, the geothermal 
potential zones identified in this study are interpreted as locations where permeable fault systems and fracture 
networks coincide with a thermally favorable geological environment, creating conditions that may support 
hydrothermal circulation and geothermal resource development. 
3.2 Sensitivity analysis of search radius selection 
A sensitivity analysis was conducted for the lineament, fault, and contact density maps using a kernel search 
radius of 1000 m as the baseline. Additional analyses were performed using search radii of 500 m and 1500 
m.  Compared with the baseline (1000 m), the area classified as very high potential changed by approximately -
12% for the 500 m radius and +18% for the 1500 m radius. 
These values represent relative percentage changes in the area of the very high potential zone with respect to 
the baseline result, rather than absolute percentage -point changes relative to the total study area. The results 
indicate a moderate sensitivity of the final geothermal potential map to the selected search radius. Therefore, the 
choice of a 1000 m search radius is influential and should be further optimized in future studies using approaches 
such as variogram analysis, spatial optimization, or spatial cross-validation. 
3.3 Study limitations and future work 
Several limitations should be kept in mind when interpreting the results of this study. Both the weighting 
process and the model evaluation were based on the same eight known hydrothermal occurrences, meaning that 
the reported validation reflects internal consistency rather than a truly independent assessment and may therefore 
present an overly optimistic view of model performance. The small number of hydrothermal sites also made it 
impossible to divide the data into separate calibration and validation data sets, limiting the statistical strength of 
the evaluation. In addition, all hydrothermal occurrences were treated equally because temperature, discharge, 
and geochemical information were not available, even though some sites are likely to have greater geot hermal 
significance than others. The geological framework was derived from the most recent publicly available 
geological map of the area, while lineaments were identified through manual interpretation by a single operator, 
which may introduce subjectivity and affect reproducibility. Other sources of uncertainty include the spatial 
resolution of the input datasets, the lack of direct hydrogeological evidence such as groundwater flow 
measurements, hydraulic tests, drilling records, and hydrogeochemical analyses, as well as the use of a weighted 
overlay method that simplifies the complex and potentially non-linear relationships among geothermal controlling 
factors. As a result, the geothermal potential map produced in this study should be viewed as a regional exploration 
screening tool that highlights promising target areas rather than confirmed geothermal resources. Future work 
should aim to expand the hydrothermal database through additional field surveys, geochemical studies, and 
drilling data; incorporate up dated geological information and higher -resolution geophysical datasets; collect 
hydrogeological and temperature measurements; compare automated and multi -operator lineament extraction 
approaches; and apply data-driven, machine learning, and spatially explicit validation techniques, such as k-fold 
spatial cross-validation, to improve the robustness and predictive capability of the model.

437 
 
Hamada et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
4. Conclusion 
This study successfully demonstrated the effectiveness of integrating remote sensing, geological, and 
geophysical data within a GIS -based weighted overlay framework for geothermal potential mapping in central –
western Taiz, Yemen. Nine controlling factors w ere derived and analyzed, with structural features such as faults 
and lineaments identified as the primary controls on geothermal occurrence. The final geothermal potential map 
showed a strong spatial correspondence with known hydrothermal occurrences, sug gesting that the proposed 
approach is effective for regional -scale geothermal exploration and preliminary screening. The resulting 
geospatial database provides a practical decision -support tool for geothermal exploration, groundwater 
development, and resou rce management. Beyond the central –western Taiz region, the proposed GIS -based 
weighted overlay framework provides a transferable methodology for geothermal prospectivity mapping in other 
tectonically active rift settings where geothermal systems are predominantly controlled by structural features such 
as faults and lineaments. By integrating remote sensing, geological, and geophysical datasets within a unified GIS 
environment, the approach can support regional -scale exploration and preliminary site screeni ng in geologically 
comparable rift environments, while recognizing that local weighting schemes and validation datasets should be 
adapted to the specific geological conditions of each study area.  The adopted approach is transferable and can be 
applied to s imilar tectonically active regions. At a minimum, application of the proposed workflow in other 
regions requires a Digital Elevation Model (DEM), geological maps containing lithological units and fault 
information, and remotely sensed or geophysical data t hat allow the extraction of major structural features (e.g., 
lineaments or fault networks), together with a limited number of known hydrothermal occurrences for empirical 
weighting and preliminary validation. 
 
5. Acknowledgement 
The authors thank all staff of the Geology Department, Faculty of Applied Science, Taiz University, Yemen. 
 
6. Declarations 
6.1 Author contributions 
All authors are equally contributed ill segments of research; data collection, analysis and writing and editing 
manuscript. 
6.2 Funding statement 
This research did not receive any specific grant from funding agencies in the public, commercial, or not -for-
profit sectors. 
6.3 Competing interest 
This research has no conflict of interest with any other work. 
6.4 The Use of AI or AI assisted Technologies 
The authors use the available soft wares to assist completing the work, then reviewed the content and the auths 
take full responsibility the published content of the paper.

438 
 
 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Hamada et al. Scientific Contributions Oil and Gas 
7. Glossary of terms and symbols 
Terms and 
symbols Definition Unit 
GIS Geographic information system  
RS Remote sensing  
DEM Digital elevation model  
SRTM Shuttle radar topography mission  
WOT Weighted overlay technique  
WV Weight value  
NHLC Number of hydrothermal locations corresponding to a class  
ROC Receiver operating characteristic  
AUC Area under the roc curve  
UTM Universal transverse mercator  
RTP Reduced-to-the-pole  
CPD Curie point depth  
GSY Geological survey of yemen  
ILWIS Integrated land and water information system  
PCI Geomatica Pci geomatica software  
ArcGIS Arcgis geographic information system software  
m Meter  
km Kilometer  
km Kilometer  
km² Square kilometer  
°C Degree celsius  
m a.s.l. Meters above sea level  
m Meter (depth/elevation)  
% Percentage  
Symbol meaning  
𝑊𝑉 Weight value  
𝑁𝐻𝐿𝐶 Number of hydrothermal locations corresponding to the class  
𝑊𝐹𝑀𝑖 Weighted factor map of factor i  
𝑖 Factor index  
𝑛 Number of geothermal controlling factors (9)  
 
8. References 
Abd Manap MA (2013) A knowledge-driven GIS modeling technique for groundwater potential mapping at the 
Upper Langat Basin, Malaysia. Arabian Journal of Geosciences 6(5):1621 –1637. 
https://doi.org/10.1007/s12517-012-0599-1 
Abdulkadir YA, Fisseha S, Jothimani M (2022) Digital elevation model and satellite gravity anomalies and their 
correlation with geologic structures at the Borena Basin, Southern Main Ethiopian Rift. European Journal of 
Remote Sensing 55(1):540–550. https://doi.org/10.1080/22797254.2022.2130096 
Abdullah A, Aziz AA, Isnain  Z (2025) The weighted values of factor classes based on different approaches for 
groundwater potential zone mapping using remote sensing data and GIS techniques in the Taiz region, Yemen. 
Indonesian Journal of Geoscience 12(1):105–131. https://doi.org/10.17014/ijog.12.1.105-131 
Abdullah A, Nassr S, Ghaleeb A . (2013) Remote sensing and geographic information system for fault segment 
mapping: a study from Taiz area, Yemen. Journal of Geological Research 2013:201757. 
https://doi.org/10.1155/2013/201757 
Abdullah. A, Akhir M. J, and Abdullah. I, (2010). Automatic mapping of lineaments using shaded relief images 
derived from digital elevation model (DEMs) in the Maran —Sungi Lembing area, Malaysia,” Electronic 
Journal of Geotechnical Engineering, vol. 15 pp. 949–957.

439 
 
 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Hamada et al. Scientific Contributions Oil and Gas 
Abullah A, Nassr S, Ghaleeb A. (2013). Landsat ETM -7 for Lineament Mapping using Automatic Extraction 
Technique in the SW part of Taiz area, Yemen. Global Journals Inc. (USA). 13 :49-52. 
Al Kadasi A (2014) Interpretation of aeromagnetic data in terms of surface and subsurface geologic structures, 
southwestern Yemen. Arabian Journal of Geosciences 7(2):505 –516. https://doi.org/10.1007/s12517-013-
1238-1 
Al-Fakih AM, Al -Khudafi AM, Koeshidayatullah A, Kaka SI, Al -Gathe AA (2025) Forecasting geothermal 
temperature in western Yemen with Bayesian -optimized machine learning regression models. Geotherm 
Energy 13:1 
Al-Gathe, A., Al-Khudafi, A., Hamada, G., Almuafa, N., Farea, I., & Abdullah, A. (2025). A hybrid approach for 
accurate geothermal temperature prediction in the western region of Yemen. Journal of African Earth 
Sciences, 231, 105777. https://doi.org/10.1016/j.jafrearsci.2025.105777 
Aliyu, A., et al. (2026). Review on geothermal prospectivity mapping: Global trends, challenges and future 
directions. Renewable and Sustainable Energy Reviews. 
Al-Kadasi, A. N., Al-Aydrus, A., & Mustafa, M. S. A. D. (2020). Estimation of Curie point depth in southwestern 
Yemen from spectral analysis of aeromagnetic data . Arabian Journal of Geosciences, 13(5), 238. 
https://doi.org/10.1007/s12517-020-5196-0 
Alnethary M, Sharian A, Mattash M, Minissale A (2024) Evaluation of geothermal exploration in Yemen (western 
area and the Red Sea). In: Proceedings of the 49th Workshop on Geothermal Reservoir Engineering, Stanford 
University, Stanford, California, USA. SGP-TR-227. 
Aydınlı, H., Kaplan, G., & Çabuk, S. N. (2026). Early -phase geothermal prospecting using remote sensing and 
machine learning: Application to Buharkent and Germencik fields, Türkiye. Geothermics. 
Bai S, Wang J, Lü G, Zhou P, Hou S, Xu S (2010) GIS -based logistic regression for landslide susceptibility 
mapping of the Zhongxian segment in the Three Gorges area, China. Geomorphology 115(1 –2):23–31. 
https://doi.org/10.1016/j.geomorph.2009.09.025 
Baker L, Johnson T (2020) Geospatial analysis of geothermal resources using GIS: case studies from North 
America. Geothermal Energy 8:12. https://doi.org/10.1186/s40517-020-00167-8 
Bernard MO (2020) Geothermal well site suitability selection using geographic information systems (GIS) and 
remote sensing: case study of the Eburru geothermal field. In: Proceedings of the 45th Workshop on 
Geothermal Reservoir Engineering, Stanford University, Stanford, California, USA. 
David LG, Pablo RG (2019) Detection of geothermal potential zones using remote sensing techniques. Remote 
Sensing 11(20):2403. https://doi.org/10.3390/rs11202403 
El Morabit I, Soufiane M, Ahmed F (2021) Geothermal potential mapping of northeast Morocco (Bekrane–Ahfir) 
using remote sensing data and GIS. E3S Web of Conferences 234:00093. 
https://doi.org/10.1051/e3sconf/202123400093 
Geological Survey of Yemen (1990) Geological sheet map of Taiz Governorate, scale 1:250,000. Geological 
Survey of Yemen, Sana’a. 
Haselwimmer C, Prakash A (2013) Thermal infrared remote sensing of geothermal systems. In: Kuenzer C, Dech 
S (eds) Thermal Infrared Remote Sensing: Sensors, Methods, Applications. Springer, Dordrecht, pp 453–473. 
https://doi.org/10.1007/978-94-007-6639-6_22 
Heasler HP, Jaworowski C, Foley D (2009) Geothermal systems and monitoring hydrothermal features. In: Young 
R, Norby L (eds) Geological Monitoring. Geological Society of America, Boulder, pp 105–140. 
Ibrahim A, Juhari MA (1990) Dictionary of Basic Geological Terms. National University of Malaysia, Bangi.

440 
 
 
https://doi.org/10.29017/scog.v49i3.2167 
 
 
 
Hamada et al. Scientific Contributions Oil and Gas 
Kehinde AM, Oluwafemi TA, Akinola AK (2023) Geothermal energy potentiality modeling using a GIS -based 
machine learning algorithm in southwestern Nigeria: insights from geophysical and remote sensing datasets. 
Research Square [Preprint]. https://doi.org/10.21203/rs.3.rs-3266721/v1 
Kumar P, Singh R (2019) Thermal remote sensing for identifying hot springs: insights from the Himalayan region. 
Journal of Environmental Management 245:1–10. https://doi.org/10.1016/j.jenvman.2019.05.082 
Levi S, Antony W (2014) GIS applications in heat source mapping in Menengai geothermal field. In: Proceedings 
of the 5th African Rift Geothermal Conference (ARGeo-C5), Arusha, Tanzania. 
Macharia MW, Gachari MK, Mariita NO, Mundia CN, Kuria DN (2018) A GIS -based approach for exploring 
geothermal resources along part of the Kenyan Rift. Journal of Applied Science, Engineering and Technology 
Development 3(1):1–34. 
Nassr S, Abdullah A (2015) The delineation of linear features from different image resolutions using edge 
modelling techniques in the Al-Mawasit area, Taiz, Yemen. American Journal of Geophysics, Geochemistry 
and Geosystems 1(1):7–18. 
Ramsey MS, Harris AJL (2013) Volcanology 2020: how will thermal remote sensing of volcanic surface activity 
evolve over the next decade? Journal of Volcanology and Geothermal Research 249:217 –233. 
https://doi.org/10.1016/j.jvolgeores.2012.05.011 
Reda TM, Gebrehiwot WZ, Jothimani JM, Tirusew SY (2022) Assessing the effect of volcano -tectonic activity 
on the spatial distribution of surface temperature in the Main Ethiopian Rift using an integrated remote sensing 
approach. European Journal of Remote Sensing 55(1):86 –102. 
https://doi.org/10.1080/22797254.2021.2021555 
Rutty LA (1993) The basement fracture pattern of southern Ontario: a tectonic interpretation based on Landsat 
TM imagery, air photos and field data. Master's Thesis, University of Waterloo, Waterloo, Canada. 
Taillefer A, Soliva R, Guillou-Frottier L, Le Goff E, Martin G, Seranne M (2017) Fault-related controls on upward 
hydrothermal flow: an integrated geological study of the Têt fault system, eastern Pyrénées (France). Geofluids 
2017:8190109. https://doi.org/10.1155/2017/8190109 
Zhou Y, Liu J (2021) Integrating remote sensing and GIS for assessing geothermal potential: a case study from 
China. International Journal of Applied Earth Observation and Geoinformation 
95:102257.https://doi.org/10.1016/j.jag.2020.102257
