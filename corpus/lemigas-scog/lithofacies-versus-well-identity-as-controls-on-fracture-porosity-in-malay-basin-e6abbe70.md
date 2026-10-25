---
source_id: "lemigas-scog"
title: "Lithofacies Versus Well Identity as Controls on Fracture Porosity in Malay Basin Carbonates A Two Scale Statis"
summary: "Statistical study across 537 samples from 13 Malay Basin wells showing whether lithofacies or well identity better explains fracture porosity in carbonates."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2131"
retrieved_at: "2026-10-24T14:30:34+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "e6abbe7068a74c696d59443e490ee07f88616c704dbf904ccf4bae4af1d0a6a6"
collected: "manual"
---

# Lithofacies Versus Well Identity as Controls on Fracture Porosity in Malay Basin Carbonates A Two Scale Statis

233 
 
https://doi.org/10.29017/scog.v49i3.2131 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 233 – 255 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Lithofacies Versus Well Identity as Controls on Fracture Porosity 
in Malay Basin Carbonates: A Two-Scale Statistical Decomposition 
 
Simeão Lourenco Correia da Silva1,2, Muhammad Luqman Hasan1,2, Dejen Teklu Asfha1,3, and 
Krisna Oka Mahendra1,3 
 
1Center for Subsurface Seismic Imaging and Hydrocarbon Prediction, Universiti Teknologi Petronas, 
32610 Seri Iskandar, Perak Darul Ridzuan, Malaysia. 
2Petroleum Engineering Department, Universiti Teknologi Petronas, 
32610 Seri Iskandar, Perak Darul Ridzuan, Malaysia. 
3Department of Geoscience, Universiti Teknologi Petronas 
32610 Seri Iskandar, Perak Darul Ridzuan, Malaysia. 
*Corresponding author: Simeão L. C. da Silva (simeao_24007382@utp.edu.my) 
Simeão L. C. da Silva: https://orcid.org/0009-0004-8478-4013 
Received: 06 April 2026; Revised in revised form 03 July 2026; Accepted 21 August 2026 
Available online 30 September 2026. 
 
 
ABSTRACT - Carbonate fracture characterization typically conditions fracture porosity (Fpor) on lithofacies 
classification, on the assumption that facies labels capture the geological controls on fracture development. This 
study evaluates this premise by employing  a two -scale statistical decomposition of Fpor variance across 537 
samples from 13 wells within a single field in the Malay Basin. The analysis uses FMI -derived Fpor as the 
reference and the operator's three -class lithofacies scheme (clean limestone, mixed  carbonate, tight shaly 
carbonate) as the facies framework. The lithofacies classification produces a statistically detectable but 
quantitatively small effect on Fpor (one-way ANOVA F = 3.85, p = 0.022, η² = 0.014; Kruskal-Wallis H = 12.80, 
p = 0.0017, ε²H = 0.020), accounting for 1.4 to 2.0% of total variance. Tukey HSD pairwise testing localizes the 
signal to a single contrast between clean limestone and mixed carbonate (p -adj = 0.016); mixed and tight shaly 
carbonate classes are statistically indistingui shable (p -adj = 0.482). Well identity, in contrast, accounts for 
approximately 27% of total Fpor variance (Kruskal-Wallis ε²H = 0.271), an effect more than thirteen times larger 
than the facies effect. Ward hierarchical clustering on standardized per -well statistics partitions the wells into 
three internally consistent clusters that cross -cut lithofacies composition. Depth is excluded as a confounding 
variable through within -class correlation analysis. The dominant control on fracture porosity in this datas et 
operates at the well scale, not the facies scale. Geological similarity between the target and training wells is the 
binding constraint on the quality of blind -well fracture prediction. These results indicate that carbonate fracture -
prediction workflows  should replace facies -only conditioning with well -partitioned validation and well -scale 
distributional descriptors, since the current three -class lithofacies scheme resolves less than one -fifteenth of the 
variance that well identity alone explains. Struct ural compartmentalization is a plausible candidate mechanism, 
though untestable with the present dataset. 
Keywords: fracture porosity; lithofacies classification; carbonate reservoir; Malay Basin; statistical 
decomposition. 
 
How to cite this article: 
Simeão L. C. da Silva, Muhammad Luqman Hasan, Dejen Teklu Asfha, and Krisna Oka Mahendra, 
2026, Lithofacies Versus Well Identity as Controls on Fracture Porosity in Malay Basin Carbonates: a 
Two-Scale Statistical Decomposition, Scientific Contributions Oil and Gas, 49 (3) pp. 233-255.

234 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
1. Introduction 
Carbonate reservoirs supply a substantial fraction of global hydrocarbon production, and many of the most 
productive examples are matrix -tight systems in which natural fractures provide the dominant permeability 
pathway (Aguilera 1976; Kargarpour 2020; Nelson 1985). In such reservoirs, fracture porosity (Fpor) controls the 
flow capacity, sweep efficiency, and ultimate recovery, with even small absolute differences in Fpor translating 
into substantial production -rate variability across a field. Characterizing the spa tial distribution of Fpor from 
sparse well control is therefore a binding constraint on development planning. Direct measurement is restricted to 
wells imaged with borehole image logs; predictions into the surrounding volume rely on geological proxies, and  
the choice of proxy determines the geological scales at which predictions can succeed. 
Borehole image logs, principally the formation micro imager (FMI), provide the closest available proxy to 
direct fracture observation in subsurface intervals. FMI -derived Fpor serves as the operational ground truth for 
fracture characterization at well loc ations and as the conditioning data for inter -well prediction. Standard 
predictive workflows propagate Fpor from imaged wells into unimaged volumes using lithofacies classification 
as the organizing variable. The underlying assumption is that facies labels, generated from conventional wireline 
logs and calibrated against core or analog data, capture sufficient geological context governing fracture 
development to serve as stratification variables for Fpor modeling. This assumption underpins most carbonate 
fracture modeling workflows (Aghli et al., 2020 ; Bagheri & Mohebian 2025)  and is built into the geostatistical 
procedures of major reservoir simulation packages. Its empirical foundations have not been systematically tested 
in many basins. 
Carbonate fracture systems are known to vary at scales below conventional facies resolution. Mechanical 
stratigraphy at decimeter to meter scale, dolomitization fronts, cement distributions, and stylolite networks all 
develop largely independently of bulk lithofacies labels (Humphrey et al., 2020). Fracture propagation, aperture 
preservation, and network connectivity respond more directly to brittle -ductile mechanical contrasts and to local 
diagenetic state than to the gross compositional categories captured by petrophysical facies schemes. Inter -well 
variability in fracture intensity, aperture, and connectivity has been documented in carbonate fields globally 
(Marrett et al., 1999 ; Ortega et al., 2006) , typically as a qualitative observation about reservoir 
compartmentalization rather than a quantified comparison against the facies-scale signal. The empirical question 
of how much fracture-relevant variance lithofacies actually resolves, and how much resides at the well scale, has 
not been systematically addressed for many production-relevant carbonate provinces. 
The Malay Basin hosts substantial carbonate gas reservoirs whose development depends on accurate fracture 
characterization (Tjia 1994). The basin’s carbonate intervals are typically tight, naturally fractured, and laterally 
heterogeneous, with reported production behavior frequently diverging from facies -based predictions and these 
discrepancies often stem from a complex pore system where permeability is governed predominantly by fracture 
networks rather than primary matrix porosity (Garland et al., 2012; Talebian et al., 2021). The basin offers a useful 
test case because it combines operational stakes, sufficient well control for a multi-well statistical analysis, and a 
standardized petrophysical workflow that produces consistently classified lithofacies labels across operator wells. 
The dataset analyzed here is drawn from one such field, with 13 wells imaged by FMI and labeled under the same 
classification protocol. 
We address the facies-versus-well question through a two-scale statistical decomposition of Fpor variance in 
a 537 -sample dataset drawn from 13 anonymized wells in a single field in the Malay Basin. The analysis is 
structured around four specific questions. First, does lithofacies classification produce statistically distinguishable 
Fpor populations, and if so, how much variance does the classification resolve? Second, is depth a controlling 
variable for Fpor within each lithofacies class, or can depth be e xcluded as a confounding factor? Third, is the 
variation in Fpor controlled primarily by lithofacies, depth, or well identity, and what is the relative magnitude of 
each effect? Fourth, how does within -class variability manifest at the well scale, particul arly in wells whose 
lithofacies composition is constrained to a single class? FMI-derived Fpor provides the ground truth throughout, 
and the operator’s 3-class lithofacies scheme (LITH 0: clean limestone; LITH 1: mixed carbonate; LITH 2: tight 
shaly carbonate) provides the facies framework. Each test is reported with both p-values and effect-size measures

235 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
(η², ε²H, rank-biserial r) to separate statistical detection from geological magnitude.  The results establish that 
lithofacies classification, as currently applied in this dataset, captures only a small fraction of fracture porosity 
variance, and that the dominant signal resides at the well scale. The two -scale decomposition we develop is 
straightforward in implementation but consequential in interpretation. It identifies where the predictive signal 
actually resides, and it constrains what predictive workfl ows must represent to succeed at blind -well prediction. 
We interpret the finding geologically, identify the candidate mechanisms consistent with the observed cluster 
structure, and develop the implications for fracture prediction workflows that rely on fac ies-based conditioning. 
The paper is organized as follows: Section 2 summarizes the geological setting; Section 3 describes the dataset 
and statistical methods; Section 4 presents the analytical results; Section 5 discusses the geological interpretation 
and predictive implications; and Section 6 concludes. 
A limitation should be flagged at the outset: the dataset analyzed here carries no structural or seismic 
information. Well identities and locations are anonymized at the data provider's request, and no fault maps, seismic 
attributes, or well -specific structural picks (dip, azimuth, fault correlation) were made available to the authors. 
Recent 3D seismic work elsewhere in the Malay Basin (Jonge et al., 2024)  illustrates the kind of structural 
framework that could, in principle, be integrated with the well -scale patterns identified here; the present study is 
deliberately restricted to the conventional wireline log and FMI -derived dataset described in Section 3 , and the 
structural interpretation offered in Section 5 is accordingly framed as a set of candidate mechanisms rather than a 
tested explanation. 
1.1 Geological setting 
The Malay Basin is one of several Cenozoic extensional basins that developed across the Sundaland 
continental block during the late Eocene to Oligocene (Hall 2013; Pubellier & Morley 2014) . Sundaland itself 
records a Late Permian to Triassic amalgamation of Asian terranes (Metcalfe 2017), and its Cenozoic interior 
subsequently fragmented into a system of rift basins arranged across the Sunda Shelf. The Malay, Penyu, West 
Natuna, and Pattani basins share this rift history, with linked subsidence and inversion phases driven by India –
Eurasia collision to the north and Sunda Trench subduction to the south (Pubellier & Morley 2014). The Malay 
Basin occupies a central position within this basin system, offshore Peninsular Malaysia and southern Thailand 
(Figure 1). The field analyzed in this study is located within the Malay Basin proper; its precise location is not 
disclosed at the data provider’s request. 
The Malay Basin contains up to 14 km of Cenozoic sedimentary fill above a thinned continental crust, with 
stretching factors β reaching values close to 4 in the basin centre and decreasing toward 1.2 at the flanks (Madon 
& Watts 1998 ; Shahar 2008). Three tectonic phases structure the basin fill. Late Eocene to Oligocene synrift 
extension produced N –S oriented en -echelon ridges and grabens (Mansor et al., 2014) . Rapid Early to Middle 
Miocene post -rift subsidence followed, accommodating thick sediment accumulation under regional thermal 
contraction. From the Middle to Late Miocene, regional compression generated a phase of structural inversion, 
producing anticlin es along reactivated rift faults, en -echelon E –W folds, and sinistral and dextral wrench 
movements along the Hinge Fault Zone (Tjia 1994). Plio-Pleistocene sag completes the tectonic sequence. The 
basin remains thermally subsiding, with present surface heat flow ranging approximately 33 to 42 mW m −2 and 
corresponding geothermal gradients of 23 to 30 °C km−1 (Madon & Watts 1998). 
Malay Basin stratigraphy is conventionally subdivided using an alphabetic Group A –M seismic-stratigraphic 
framework that maps onto the basin’s tectonic phases (Madon & Watts 1998) . The lower groups (M –I) record 
synrift to early post -rift fill, dominated by lacustrine and fluvial -deltaic deposits. The middle groups (H –F) 
document fully developed post -rift subsidence under coastal -plain and marginal -marine conditions and include 
the source-rich shales together with the principal sandstone reservoirs of the basin’s petroleum system. The upper 
groups (E–A) record marine transgression following Late Miocene inversion, with shallow -marine clastics and 
intermittent carbonate deposition across the basin (Bishop 2002). The carbonate intervals of interest in this study 
sit within this upper post-inversion section, deposited on structural highs under shallow-marine conditions (Figure 
2). Southeast Asian Cenozoic carbonates developed under equatorial, bioclast -dominated conditions, with rare 
oolitic or pisolitic textures, restricted evaporite and dolomite associations, and persistent clastic influence from

236 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
the surrounding orogenic source areas (Wilson 2002). Carbonate platform initiation across the Sundaland margin 
was strongly controlled by tectonic topography: isolated platforms developed over antecedent structural highs 
account for more than 75% of the region’s economic carbonate hydrocarbon discoveries, even though only about 
30% of platforms initiated as isolated features (Wilson & Hall 2010). 
 
Figure 1. 
Regional location and tectonic framework of the Malay Basin within the Sundaland passive-margin system. 
Inset shows Sundaland and surrounding active margins (Sunda Trench to the south, India–Eurasia collision to the north). 
Main map identifies the Malay, Penyu, West Natuna, and Pattani basins, the Hinge Fault Zone, and the principal Middle to 
Late Miocene inversion folds. The study area rectangle indicates the general portion of the basin from which the dataset is 
drawn; specific field location is not disclosed. Modified after (Mansor et al., 2014; Pubellier & Morley 2014). 
 
Diagenetic modification of these carbonates spans marine, meteoric, and burial environments. Detailed work 
on analogous Miocene buildups of Central Luconia (offshore Sarawak) documents moldic porosity reaching 45% 
in the best intervals, alongside calcite and dolomite cementation, stylolitic compaction, and burial-related porosity 
destruction (Janjuhah et al., 2017). Late dissolution and microfracturing locally restore permeability against this 
background of progressive cementation. Fracture systems in Malay Basin carbonates arise from at least two 
distinct processes operating across the basin’s history. Tectonic fra ctures formed during the Middle to Late 
Miocene inversion phase, with orientations controlled by the regional compressional stress field and locally by 
reactivated rift faults (Madon 2007 ; Tjia 1994) . Wrench -related en -echelon and conjugate fracture sets are 
consistent with transtensional and transpressional movements along major bounding fault zones. Diagenetic 
fractures developed independently from burial compaction, stylolite -associated brittle fai lure, and dissolution 
along bedding-parallel surfaces. Analogue work on Central Luconia carbonate platforms documents fault-related 
selective cementation, with fracture-intensity peaks coinciding with low-porosity mounds (Rankey et al., 2019), 
demonstrating that fracture development and porosity preservation vary at sub -platform scale and across short 
lateral distances. Outcrop fracture -network analysis on Sarawak limestone buildups confirms that fracture 
intensity, topology, and connectivity vary substantially within a single carbonate unit (Ong & Jamaludin 2023). 
Both tectonic and diagenetic mechanisms contribute to the fracture porosity targeted in this study.

237 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
Figure 2. 
Generalized Cenozoic stratigraphy of the Malay Basin showing the alphabetic Group A–M seismic-stratigraphic framework, 
lithologies, and corresponding tectonic phases (synrift, post-rift, inversion, sag). 
The shaded band marks the upper post-inversion carbonate interval from which the dataset is drawn. 
Source-rock interval (Group H–I) shown for petroleum-system context. Modified after (Bishop 2002; Madon et al., 2020). 
 
Malay Basin gas reservoirs occur primarily in the post -rift sandstone groups and, in subordinate fashion, in 
the upper post-inversion carbonate intervals (Madon et al., 2006). The basin’s central depocenter is gas-rich, with 
hydrocarbon accumulations concentrated in late-inversion anticlinal traps and in combined structural-stratigraphic 
configurations (Bishop 2002). Carbonate reservoirs in these and analogous regional fields are commonly tight, 
with matrix permeabilities of order 1 mD or below, and depend on natural fracture networks for economic flow. 
Regional analogue studies of Late Miocene Malaysian carbonate bu ildups report that fractured carbonate 
platforms host a substantial fraction of national gas reserves, with reservoir quality varying significantly within 
and between platforms despite broadly similar bulk lithology (Janjuhah et al., 2017) . The field analyzed here is 
one such tight, fracture -controlled carbonate gas reservoir, and the well -scale Fpor variability quantified in 
subsequent sections is consistent with the within-platform heterogeneity documented across the region. 
Generalized Cenozoic stratigraphy of the Malay Basin

238 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
2. Dataset and methods 
2.1 Dataset and variables 
The dataset consists of 537 samples drawn from 13 wells in a single field in the Malay Basin. The wells are 
anonymized as W1 through W13 throughout this paper; the field name and operator are withheld at the data 
provider’s request. Per-well sample counts range from 23 (W9) to 66 (W3), reflecting both the length of the FMI-
imaged interval in each well and the density of usable fracture observations within those intervals. The 13 wells 
together span 808 ft of vertical range, from −2,532 to −3,395 ft TVDSS. 
Fracture porosity (Fpor) is the primary target variable throughout the analysis. Each Fpor value is derived from 
FMI image-log interpretation performed by the operator under their standard petrophysical workflow. We treat 
the resulting Fpor values as the o perational ground truth and do not re -interpret the underlying image data; the 
uncertainty in this interpretation is discussed in Section 5.4. The FMI interpretation delivered to the authors is 
limited to the Fpor value at each depth sample; no structural picks (dip, azimuth, or fault correlation) were 
provided with the dataset, so the structural characterization of individual wells lies outside the scope of the present 
study. Grouping variables include the lithofacies label (3 -class categorical), well iden tity (13-class categorical), 
and depth in TVDSS (continuous). Two auxiliary continuous variables, shallow resistivity (RS) and deep 
resistivity (RT), are used in Section 4.6 to characterize log–Fpor relationships. 
2.2 Lithofacies classification 
Lithofacies labels (LITH 0, LITH 1, LITH 2) are provided by the data owner as part of the operator’s standard 
petrophysical interpretation workflow. The classification draws on integrated analysis of conventional wireline 
logs, including gamma ray, bulk density, neutron porosity, sonic, and resistivity. It corresponds to clean limestone 
(LITH 0), mixed carbonate (LITH 1), and tight shaly carbonate (LITH 2). The specific cutoff values and decision 
rules underlying the classification are proprietary and were not disclosed to the authors. The classification is 
therefore treated as a given input throughout the analysis, and the implications of this dependency on a vendor -
supplied scheme are addressed in Section 5.4. 
2.3 Statistical procedures and effect-size measures 
The analysis applies parallel parametric and non -parametric tests to each question, with effect -size measures 
reported alongside p -values to distinguish statistical detection from geological magnitude. Distributional 
characterization begins with per -LITH and per-well descriptive statistics (sample size, mean, median, standard 
deviation, coefficient of variation, skewness, interquartile range, minimum, maximum) and a Shapiro -Wilk 
normality test applied to each LITH class. Normality is rejected for all three classes (p < 0.001), and the non -
parametric procedures are therefore reported in parallel with their parametric counterparts throughout. 
To test the lithofacies effect on Fpor (Section 4.2), we apply one -way ANOVA and Kruskal -Wallis as 
omnibus tests, followed by Tukey HSD post -hoc pairwise comparisons with the family -wise error rate 
controlled at α = 0.05. Effect sizes are reported as η² from ANOVA (SS_between / SS_total) and as ε²H derived 
from the Kruskal -Wallis statistic, computed as (H − k + 1) / (N − k). Interpretive thresholds follow the 
conventional small (<0.06), medium (0.06 –0.14), and large (>0.14) cutoffs (Berben et al., 2012 ; Cohen 1988; 
In & Lee 2024 ; Richardson 1996) . 
Within-class depth -Fpor relationships (Section 4.3) are characterized using Pearson and Spearman rank 
correlations together with ordinary least -squares regression slopes, computed separately for each LITH class to 
avoid the depth -LITH confound that arises from partially separated depth intervals among classes. Inter -well 
variability (Section 4.4) is tested with Kruskal -Wallis across the 13 wells, with Mann -Whitney U tests of each 
well against the pooled remainder, and with Dunn pairwise post -hoc comparisons using Bonferroni correction . 
The Mann-Whitney effect size is the rank-biserial correlation r = 1 − (2U / n₁n₂); positive values indicate the focal 
well sits below the reference distribution, and negative values indicate it sits above. Effect-size dominance, rather 
than p-value magnitude alone, is used to compare the relative strength of the facies and well effects.

239 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
 
Figure 3. 
Analytical workflow for the two-scale decomposition of fracture porosity (Fpor). 
Numbered steps denote processing sequence; hierarchical clustering (4.4) follows from the inter-well analysis (4.3). 
Lithofacies classification is operator-supplied and treated as a given input. 
Full methods are described in Section 3, results in Section 4, and interpretation in Section 5.

240 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
2.4 Hierarchical clustering 
The well -scale signature identified by the Mann -Whitney battery is characterized further through Ward 
hierarchical clustering of the 13 wells. The clustering operates on a 5 -feature representation of each well’s Fpor 
distribution: mean, standard deviation,  coefficient of variation, skewness, and interquartile range. These 
features capture central tendency (mean), dispersion (SD, CV, IQR), and distributional shape (skewness), and 
they are computed directly from the per -well Fpor samples without auxiliary cov ariates. Each feature is 
standardized (z -score across wells) before clustering, ensuring that the distance metric is not dominated by the 
variable with the largest absolute scale; CV values are reported in percent and would otherwise dominate the 
un-standardized distance.  
Ward linkage is selected because it minimizes the increase in total within-cluster variance at each merge step, 
producing compact clusters appropriate to the assumption that wells within a cluster represent an internally 
consistent population. The dendrogr am is cut at a linkage distance corresponding to three clusters, identified 
visually as the level at which a clear gap appears between merger heights. Robustness of the partition was checked 
by comparing the three -cluster assignment to the Mann -Whitney sig nificance pattern (Section 4.4); the two 
partitions are mutually consistent. 
2.5 Software and reproducibility 
All statistical procedures are implemented in Python 3, using the scipy.stats module for ANOVA, Kruskal -
Wallis, Mann-Whitney, Pearson and Spearman correlations, and Shapiro -Wilk testing; the statsmodels package 
for Tukey HSD via statsmodels.stats.multicomp; the scikit-posthocs package for Dunn pairwise comparisons with 
Bonferroni correction; and the scipy.cluster.hierarchy module for Ward linkage and dendrogram construction. 
Data management is handled in pandas. The analysis code is available from the corresponding author on 
reasonable request, subject to the data confidentiality agreement governing the underlying well-log dataset. 
 
3. Result and discussion 
3.1 Fracture porosity distributions by lithofacies class 
Fracture porosity is right-skewed in every lithofacies class (Figure 4a; skewness 1.26 to 1.78), with most values 
clustering between 0.030 and 0.040 and tails extending to roughly 0.18. Shapiro -Wilk tests reject normality for 
all three classes (p < 0.001), so the inferential analyses below use nonparametric methods alongside their 
parametric counterparts. 
The three class means sit within a narrow range (Table 1). LITH 0 (clean limestone, n = 74) averages 0.0384 
± 0.0257; LITH 1 (mixed carbonate, n = 205) averages 0.0485 ± 0.0279; LITH 2 (tight shaly carbonate, n = 258) 
averages 0.0456 ± 0.0261. The coefficient of variation is 66.8% for LITH 0 and close to 57% for  both LITH 1 
and LITH 2. Pooled across the 537 samples, Fpor has a mean of 0.0451 and a median of 0.0379. 
Table 1. 
Descriptive statistics of fracture porosity (Fpor) per lithofacies class. 
All three classes are non-normal (Shapiro-Wilk p < 0.001). 
LITH Description N Mean Median SD CV (%) Min Skewness 
0 Clean limestone 74 0.0384 0.0310 0.0257 66.8 0.0039 1.77 
1 Mixed carbonate 205 0.0485 0.0415 0.0279 57.5 0.0000 1.26 
2 Tight shaly carbonate 258 0.0456 0.0378 0.0261 57.2 0.0000 1.78 
— Pooled (all classes) 537 0.0451 0.0379 — — 0.0000 —

241 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
The histogram in Fig 4b shows substantial overlap among the three classes, especially in the 0.02-0.06 interval, 
which contains most observations. Class identity does not produce visually distinct modes. The three KDE peaks 
are separated by only a small horizontal offset: LITH 0 peaks near 0.025, while LITH 1 and LITH 2 both peak 
near 0.030 to 0.035 on otherwise similar curves. 
 
 
Figure 4. 
Distribution of fracture porosity (Fpor) per lithofacies class across the 537-sample dataset. 
(a) Kernel density estimates for LITH 0 (clean limestone, n = 74), LITH 1 (mixed carbonate, n = 205), and LITH 2 (tight 
shaly carbonate, n = 258). All three distributions are right-skewed (skewness 1.26 to 1.78), with closely overlapping modes 
near 0.025-0.035. (b) Stacked histogram showing distributional overlap among the three classes; the bulk of observations 
falls between 0.020 and 0.060. 
3.2 Lithofacies effect on Fpor 
One-way ANOVA detects a significant difference among the three class means (Figure 5; F = 3.85, p = 
0.022), and the Kruskal -Wallis test confirms it (H = 12.80, p = 0.0017). Both effect sizes are small: ANOVA -
based η² = 0.014, and the Kruskal -Wallis equivalent ε²H = (H − k + 1) / (N − k) = 0.020. Lithofacies 
classification accounts for 1.4  to 2.0% of total Fpor variance, well within the small -effect range under the 
standard η² < 0.06 cutoff (Table 2). 
Tukey HSD pairwise comparisons localize the effect to a single contrast. LITH 0 differs significantly from 
LITH 1 (mean difference 0.010, p-adj = 0.016), while LITH 0 versus LITH 2 is not significant (mean difference 
0.007, p-adj = 0.106), and LITH 1 versus LITH 2 is far from significant (mean difference −0.003, p-adj = 0.482). 
The omnibus signal arises entirely from the LITH 0 to LITH 1 separation; the remaining two contrasts cannot be 
distinguished from the null. 
Lithofacies class is therefore a statistically detectable but quantitatively minor control on Fpor, and the effect 
itself is narrowly localized: only the clean limestone class (LITH 0) separates from the others, while the mixed 
and tight shaly carbonate cl asses (LITH 1 and LITH 2) are statistically interchangeable on this measure. The p -
values reflect the sample size (n = 537) more than a wide separation between classes. Within -class variance is 
sufficiently wide that the facies label alone cannot reliably predict the Fpor of an individual sample, and in practice 
the 3-class scheme reduces to a 2-class one (LITH 0 versus LITH 1+2). 
3.3 Depth-Fpor relationships 
Within-class Pearson correlations between Fpor and depth (TVDSS) are weak and statistically nonsignificant: 
r = 0.051 for LITH 0 (p = 0.663), r = −0.102 for LITH 1 (p = 0.145), and r = −0.077 for LITH 2 (p = 0.219). 
Spearman correlations are similarly negligible (|ρ| ≤ 0.023, all p > 0.74). The pooled correlation across all samples 
reaches nominal significance (r = −0.099, p = 0.022) but is practically zero; the pooled signal arises from mixing 
samples drawn from facies classes occupying partially separated depth intervals (Table 3).

242 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
Table 2. 
Inferential tests of the lithofacies effect on Fpor. 
The ANOVA-based η² and the Kruskal-Wallis–based ε²H are reported as complementary effect-size measures. Asterisk (*) 
denotes Tukey HSD pairwise contrasts significant at the family-wise error rate of α = 0.05. 
Test Statistic df p-value Effect size  
One-way ANOV A F = 3.85 2, 534 0.022 η² = 0.014  
Kruskal-Wallis H = 12.80 2 0.0017 ε²H = 0.020  
Tukey HSD: LITH 0 vs LITH 1 mean diff = 0.010 — 0.016 * —  
Tukey HSD: LITH 0 vs LITH 2 mean diff = 0.007 — 0.106 —  
Tukey HSD: LITH 1 vs LITH 2 mean diff = −0.003 — 0.482 —  
 
 
Figure 5. 
Box plots of Fpor by lithofacies class. 
Boxes span the interquartile range, the central line is the median, whiskers extend to 1.5× IQR, and points beyond the 
whiskers are plotted individually. Summary statistics: ANOVA F = 3.85, p = 0.022, η² = 0.014. Tukey HSD post-hoc testing 
identifies the LITH 0–LITH 1 contrast as the only significant pairwise difference (p-adj = 0.016); LITH 1 and LITH 2 are 
statistically indistinguishable (p-adj = 0.482). 
 
Table 3. 
Depth–Fpor correlations within and across lithofacies classes. 
Within-class correlations are weak and non-significant for all three classes; the nominally significant pooled correlation 
reflects partially separated depth intervals among classes rather than a within-class trend. 
Group N Pearson r Pearson p Spearman ρ Spearman p Slope (Fpor/ft)  
Pooled (all) 537 −0.099 0.022 −0.097 0.025 −1.3 × 10−5  
LITH 0 74 +0.051 0.663 +0.016 0.891 +2.6 × 10−5  
LITH 1 205 −0.102 0.145 +0.023 0.749 −1.7 × 10−5  
LITH 2 258 −0.077 0.219 +0.015 0.808 −1.2 × 10−5  
 
Within-class regression slopes are essentially flat: +2.6 × 10−5 Fpor/ft for LITH 0, −1.7 × 10−5 for LITH 1, 
and −1.2 × 10−5 for LITH 2. The scatter in Figure 6, shows substantial vertical spread at every depth interval, 
without a systematic trend in any of the three panels. This rules out depth as a candidate explanation for the inter-
well variability reported in Section 4.4. The wells span 808 ft vertically (−2,532 to −3,395 ft TVDSS), and the 
between-well differences in Fpor are not attributable to systematic depth-dependence within facies.

243 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
Figure 6. 
Depth versus Fpor scatter plots by lithofacies class. 
Within-class Pearson correlations are weak and statistically nonsignificant: LITH 0 r = 0.051 (p = 0.663), LITH 1 r = −0.102 
(p = 0.145), LITH 2 r = −0.077 (p = 0.219). Dashed lines show within-class linear regressions with slopes near zero in every 
panel. Depth ranges differ across classes, reflecting the stratigraphic position of each facies in the sampled wells. 
 
3.4 Inter-well variability and clustering 
Treating well identity as the grouping variable, the Kruskal-Wallis test across the 13 wells returns H = 154.12 
(p = 8.3 × 10−27), with effect size ε²H = (154.12 − 12) / (537 − 13) = 0.271. Well identity accounts for 
approximately 27% of Fpor variance, about 13 times the variance attributable to lithofacies class. 
Per-well descriptive statistics (Table 4) show that mean Fpor ranges from 0.0274 (W13) to 0.0738 (W8), a 
2.7-fold spread that exceeds the 1.3 -fold spread between LITH classes. CV across wells ranges from 33% (W5) 
to 68% (W10). There is no monotonic relationship between mean and CV: W7 has a high mean (0.0679) with 
intermediate CV (42%), while W2 has a lower mean (0.0530) with comparable CV (53%). The box plots in Figure 
7, summarize the per-well distributions. 
 
Table 4. 
Per-well descriptive statistics with Ward-clustering assignment. 
Wells are anonymized (W1–W13). LITH composition indicates the lithofacies classes present in the well's sampled interval. 
Cluster assignment is from Ward hierarchical clustering on standardized statistics (mean, SD, CV, skewness, IQR). 
Well LITH N Depth (ft TVDSS) Mean Median SD CV (%) Skew Cluster  
W1 LITH 1+2 35 −2,786 to −2,613 0.0459 0.0398 0.0218 47.5 0.59 1  
W2 LITH 1+2 26 −2,791 to −2,665 0.0530 0.0407 0.0283 53.4 0.75 3  
W3 LITH 1+2 66 −3,078 to −2,755 0.0325 0.0320 0.0112 34.4 0.45 1  
W4 LITH 1+2 48 −2,990 to −2,755 0.0487 0.0420 0.0311 63.9 0.94 2  
W5 LITH 2 only 63 −3,290 to −2,980 0.0395 0.0358 0.0131 33.1 0.90 1  
W6 LITH 1+2 57 −2,935 to −2,650 0.0439 0.0397 0.0167 38.0 0.46 1  
W7 LITH 1+2 50 −3,395 to −3,150 0.0679 0.0611 0.0286 42.1 1.77 3  
W8 LITH 1+2 53 −2,953 to −2,695 0.0738 0.0649 0.0350 47.4 0.77 3  
W9 LITH 0 only 23 −2,694 to −2,584 0.0347 0.0262 0.0222 64.0 0.96 2  
W10 LITH 0 only 25 −2,738 to −2,618 0.0490 0.0346 0.0332 67.7 1.49 2  
W11 LITH 0 only 26 −2,654 to −2,532 0.0315 0.0287 0.0161 51.0 0.62 1  
W12 LITH 1 only 28 −2,900 to −2,765 0.0326 0.0300 0.0147 45.1 0.72 1  
W13 LITH 1+2 37 −2,943 to −2,765 0.0274 0.0266 0.0163 59.4 0.40 1

244 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
 
Figure 7. 
Box plots of Fpor per well for the 13 anonymized wells in the dataset. 
Sample sizes per well are annotated above each box and range from n = 23 (W9) to n = 66 (W3). Color coding identifies the 
cluster assignment from Ward hierarchical clustering (Cluster 1: low-to-moderate Fpor; Cluster 2: moderate Fpor, high CV; 
Cluster 3: highest Fpor). Wells are ordered by increasing mean Fpor. 
 
Mann-Whitney comparisons of each well against the pooled remainder identify seven wells that differ 
significantly from the dataset baseline at p < 0.05 (Table 5). Two wells are significantly elevated: W7 (effect r = 
0.584, p < 10−5) and W8 (effect r = 0.579, p < 10−5). Five wells are significantly depleted: W3 (r = 0.354), W9 (r 
= 0.299), W11 (r = 0.364), W12 (r = 0.319), and W13 (r = 0.492). The remaining six wells, W5 included, do not 
differ significantly from the baseline. 
 
Table 5. 
Mann-Whitney U test of each well against the pooled remainder of the dataset. 
Effect r is the rank-biserial effect size; positive values indicate the well is lower than the pooled remainder, negative values 
indicate higher. 
Well N Mean (well) Mean (others) U p Effect r Significant 
W1 35 0.0459 0.0457 9,388 0.497 −0.069 No 
W2 26 0.0530 0.0453 7,664 0.186 −0.154 No 
W3 66 0.0325 0.0475 10,037 < 0.0001 +0.354 Yes (lower) 
W4 48 0.0487 0.0454 12,722 0.337 −0.084 No 
W5 63 0.0395 0.0465 13,860 0.355 +0.072 No 
W6 57 0.0439 0.0459 14,199 0.640 −0.038 No 
W7 50 0.0679 0.0434 19,284 < 10−5 −0.584 Yes (higher) 
W8 53 0.0738 0.0426 20,257 < 10−5 −0.579 Yes (higher) 
W9 23 0.0347 0.0462 4,143 0.015 +0.299 Yes (lower) 
W10 25 0.0490 0.0455 6,315 0.911 +0.013 No 
W11 26 0.0315 0.0464 4,227 0.0017 +0.364 Yes (lower) 
W12 28 0.0326 0.0464 4,856 0.0045 +0.319 Yes (lower) 
W13 37 0.0274 0.0470 4,698 < 10−5 +0.492 Yes (lower)

245 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
Ward hierarchical clustering on five standardized per-well statistics (mean, SD, CV, skewness, IQR) produces 
three clusters (Figure 8). Cluster 1 contains seven wells (W1, W3, W5, W6, W11, W12, W13) with low -to-
moderate mean Fpor (0.027 to 0.046) and skewness between 0.40 and 0.90; these are the lower -Fpor wells with 
relatively well-behaved distributions. Cluster 2 contains three wells ( W4, W9, W10) with moderate mean Fpor 
(0.035 to 0.049) but the highest within -well CV values in the dataset (64 to 68%) and high positive skewness 
(0.94 to 1.49), indicating distributions dominated by occasional high -Fpor outliers. Cluster 3 contains the 
remaining three wells (W2, W7, W8), which have the highest mean Fpor (0.053 to 0.074) and elevated IQR values, 
combining a raised baseline with a wide spread. 
 
 
Figure 8. 
Hierarchical clustering of the 13 wells by Fpor distributional statistics. 
(Left) Ward linkage dendrogram computed on standardized per-well features (mean, SD, CV, skewness, IQR), producing 
three clusters at a linkage distance of approximately 3.5. (Right) Heatmap of the same standardized statistics underlying the 
clustering.Cluster 1 (n = 7 wells) contains low-to-moderate Fpor wells with controlled variance; Cluster 2 (n = 3 wells) 
contains wells with moderate Fpor but the highest within-well CV; Cluster 3 (n = 3 wells) contains the highest-Fpor wells 
with elevated IQR. 
 
The clusters cross-cut lithofacies composition. Cluster 1 contains wells of mixed LITH 1+2 composition (W1, 
W3, W6, W13), the LITH 2 -exclusive W5, and the LITH 0-exclusive W11. Cluster 3 likewise mixes LITH 1+2 
wells (W2, W7, W8). The statistical signature distinguishing the clusters is not reducible to facies composition. 
Dunn pairwise comparisons with Bonferroni correction identify 26 of the 78 well pairs as significantly 
different (Table 6). Most of these pairs involve Cluster 3 wells (W2, W7, W8) tested against Cluster 1 wells, 
consistent with the elevated Fpor means in Cluster 3. 
3.5 Within-class case study: the single-facies well (W5) 
W5 is the only well in the dataset composed entirely of LITH 2 samples (n = 63; depth range −2,980 to −3,290 
ft TVDSS). Its Fpor distribution has mean 0.0395, median 0.0358, and SD 0.0131. The CV is 33.1%, the second-
lowest in the dataset after W3 at 34.4%. A Mann-Whitney test of W5 against the pooled LITH 2 samples from all

246 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
other wells (n = 195) returns U = 5,421 with p = 0.161 and effect size r = 0.117. Against its facies peers, W5 is 
not statistically distinguishable in central tendency. By the standard within-class test, the well is unremarkable. 
Table 6. 
Significant pairwise comparisons between wells from the Dunn post-hoc test (Bonferroni-corrected, p < 0.05). 
Twenty-six of the 78 possible pairs reach significance; W7 and W8 (Cluster 3, highest Fpor) account 
for the majority of the contrasts. 
Well A Well B p-adj Well A Well B p-adj Well A Well B p-adj 
W1 W7 0.0202 W4 W8 0.0085 W7 W11 < 0.0001 
W1 W8 0.0213 W4 W13 0.0018 W7 W12 < 0.0001 
W1 W13 0.0098 W5 W7 < 0.0001 W7 W13 < 0.0001 
W2 W3 0.0497 W5 W8 < 0.0001 W8 W9 < 0.0001 
W2 W13 0.0034 W6 W7 0.0007 W8 W10 0.0106 
W3 W4 0.0321 W6 W8 0.0007 W8 W11 < 0.0001 
W3 W7 < 0.0001 W6 W13 0.0043 W8 W12 < 0.0001 
W3 W8 < 0.0001 W7 W9 < 0.0001 W8 W13 < 0.0001 
W4 W7 0.0082 W7 W10 0.0100    
 
W5 stands apart for three reasons that the facies label does not capture. It is the only well in the dataset 
composed entirely of a single lithofacies class. Its CV of 33.1% sits well below the LITH 2 population CV of 
57.2%, indicating a tighter Fpor distr ibution than its facies peers. Moreover, the depth profile in Figure 9 shows 
persistent low-amplitude variation across the full logged interval, unlike the high-amplitude excursions visible in 
the other LITH 2-bearing wells (W2, W4, W6, W7, W8, W10, W13). 
These features illustrate the principal limitation of facies-based fracture characterization in this dataset. A well 
can occupy a single lithofacies class and have a mean Fpor that is statistically ordinary, yet still carry a distinctive 
distributional signature in compositional purity, constrained variance, and depth -amplitude character. The well -
scale clustering in Section 4.4 captures that signature; the facies label does not. 
3.6 Conventional log-Fpor relationships 
Cross-plots of resistivity logs against Fpor (Figure 10) show a strong positive monotonic relationship for 
shallow resistivity (RS vs Fpor: r = 0.762, p < 0.0001) and a weaker but significant relationship for deep resistivity 
(RT: r = 0.432, p < 0.0001). LITH 0, LITH 1, and LITH 2 points are interleaved across both cross-plot planes, 
with no facies-specific cluster visible along either log axis. 
The RS-Fpor correlation is stronger than the correlation of Fpor with any facies -scale or depth-scale variable 
considered above. This indicates that information predictive of Fpor exists in continuous log space, and that the 
predictive signal is not stratified by lithofacies label.

247 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
 
 
 
 
Figure 9. 
Fpor depth profiles for all 13 wells, arranged by Ward cluster assignment. 
Each panel plots Fpor (horizontal axis) against depth (vertical axis, ft TVDSS) for a single well, with the well name and its cluster given in 
the panel title. Point colour denotes lithofacies class: LITH 0 (clean limestone) in blue, LITH 1 (mixed carbonate) in green, and LITH 
2 (tight shaly carbonate) in red. Row 1 contains the seven Cluster 1 wells (W13, W11, W3, W12, W5, W6, W1), which combine low 
to moderate Fpor with controlled variance. Row 2 contains the three Cluster 2 wells (W9, W4, W10), distinguished by the highest 
within-well coefficients of variation in the dataset. Row 3 contains the three Cluster 3 wells (W2, W7, W8), which carry the highest 
mean Fpor and the widest interquartile ranges. Horizontal and vertical axis limits are set independently for each panel to 
accommodate the differing Fpor ranges and logged intervals between wells; profiles should therefore be compared by shape and 
internal variability rather than by apparent spread on the page. W5 (Cluster 1, row 1) is the only single-facies well in the dataset, 
composed entirely of LITH 2, and shows persistent low-amplitude variation across its full logged interval, in contrast to the high-
amplitude excursions seen in the other LITH 2-bearing wells (W2, W4, W6, W7, W8, W10, W13).

248 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
 
Figure 10. 
Wireline log–Fpor cross-plots colored by lithofacies class. 
(Left) Shallow resistivity (RS) versus Fpor: r = 0.762, p < 0.0001. (Right) Deep resistivity (RT) versus Fpor: r = 0.432, p < 
0.0001. LITH 0, LITH 1, and LITH 2 points are interleaved across both planes, showing that the resistivity–Fpor relationship 
does not stratify by facies. 
 
 
3.7 Discussion 
• Why the lithofacies effect is small and asymmetric.  
The small effect size of lithofacies on fracture porosity ( η² = 0.014; ε² H = 0.020) is consistent with the 
geological scales at which fracture porosity is generated and modified in carbonate reservoirs. Lithofacies 
classification, as implemented in the operator’s petrophysical workflow, captures bulk mineral composition and 
shale content, both of which are gross attributes largely independent of the diagenetic, structural, and fluid-flow 
processes that govern fracture development. Mechanical stratigraphy at decimeter to meter scale, dolomitization 
fronts, cement distributions, and stylolite networks all vary at scales below the facies level (Lucia 2007). Fracture 
porosity inherits this sub -facies heterogeneity, and a facies -only classification scheme cannot recover it. The 
asymmetric pattern within the small lithofacies signal where the LITH 0 separates from LITH 1 and LITH 2, 
while LITH 1 and LITH 2 remain statistically interchangeable, points toward a single mechanical threshold 
rather than a graded compositional gradient. Clean limestone (LITH 0) appears to respond to imposed stress and 
to subsequent diagenetic sealing differently from mixed and shaly carbonate variants. Two candidate 
mechanisms are consistent with this pattern. First, clean limestone is me chanically more homogeneous and 
lacks the lithological interfaces that concentrate stress and nucleate fractures in mixed and shaly intervals 
(Laubach et al., 2016 ; Ortega et al., 2006) . Second, fracture preservation may be lower in clean limestone 
because diagenetic cementation seals open fractures more efficiently in the absence of clay -bound 
permeability barriers (Nelson 1985) . Either mechanism, or a combination of the two, would suppress 
preserved fracture porosity in LITH 0 relative to LITH 1 and LITH 2 without further distinguishing the mixed 
and shaly variants whose mechanical behavior is dominated by shared clay content.  
Neither mechanism can be confirmed from the data presented here. The small effect size, the narrow 
localization of the significant contrast, and the absence of further within -class differentiation are all consistent 
with inter-well variability (Section 4.4) dominating any facies-level signal. The lithofacies framework provides 
a coarse first-order partition of Fpor magnitude; the controlling processes operate at finer geological scales than 
the classification resolves. This contrasts with siliciclastic depositional systems, where facies architecture itself 
is often the dominant control on reservoir heterogeneity; in the fluvial -to-deltaic Balikpapan Formation of the 
Lower Kutai Basin, for example, channelised, mouth-bar/delta-front, and prodelta facies show systematic, order-
of-magnitude contrasts in porosity and permeability tied directly to depositional process (Wahid et al., 2026) . 
The weak facies signal recovered here therefore appears to be a feature of fracture-dominated carbonate systems 
specifically, rather than a general property of reservoir heterogeneity.

249 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
• Geological interpretation of well-scale variability 
Well identity accounts for approximately 27% of Fpor variance, more than an order of magnitude above 
the facies-scale effect. The geological interpretation of this signal requires identifying processes that operate at 
the well -to-well rather than the sampl e-to-sample scale. Four candidate mechanisms are consistent with the 
observed cluster structure, and the data presented here permit only partial discrimination among them. 
Structural compartmentalization is the most direct candidate. Wells located in different fault blocks or 
tectonic regimes experience distinct stress histories, fracture orientations, and shear -related porosity 
development (Madon & Watts 1998 ; Tjia 1994). Cluster 3 wells (W2, W7, W8), with the highest Fpor and 
elevated IQR, would, in this interpretation, occupy structurally active positions where fracture density and 
aperture are systematically enhanced. The deeper position of W7 (−3,150 to −3,395 ft TVDS S) and the 
consistently elevated Fpor of W7 and W8 lend qualitative support to a structural explanation. However, 
confirmation requires structural mapping, which is not available in this dataset. 
Diagenetic heterogeneity at the well scale is a second mechanism. Carbonate reservoirs typically preserve 
evidence of multiple diagenetic phases such as marine cementation, mixing -zone dolomitization, burial 
recrystallization, and late hydrothermal alterat ion, each of which affects fracture preservation, sealing, and 
reactivation (Esteban & Taberner 2003 ; Nikbin & Aminshahidy 2025) . Cluster 2 wells (W4, W9, W10), with 
high CV and strong positive skewness, are consistent with a diagenetic signature: a relatively uniform low-Fpor 
matrix punctuated by isolated high-Fpor intervals, as would arise where focused fluid pathways produced zones 
of intense dissolution or selective fracture -controlled cementation against a more uniform diagenetic 
background. 
A third candidate is variation in mechanical stratigraphy. Even where facies classification is similar across 
wells, the detailed bedding architecture and the distribution of brittle –ductile contrasts can differ substantially 
from well to well (Laubach et al., 2009) . Wells whose logged interval contains thinly bedded sequences with 
frequent mechanical interfaces would develop denser, more uniformly distributed fracture networks than wells 
dominated by thick homogeneous units. Cluster 1, which groups seven wells with low-to-moderate Fpor and 
controlled variance, would, in this interpretation, represent the dataset’s background mechanical state, against 
which Clusters 2 and 3 stand out. 
Fluid migration history may contribute independently of structure and diagenesis. Carbonate fracture 
networks are progressively modified by hydrocarbon emplacement, pressure cycling, and dewatering, and these 
processes operate at reservoir -compartment scale (Kargarpour 2020) . Differences in entrapment timing and 
reservoir pressure history among the 13 wells would contribute to the well-scale signature documented here. 
The cluster structure cannot uniquely identify which combination of these mechanisms operates in this 
field, but it does establish that the controlling variability is geological rather than random. The three Ward 
clusters represent stable, internally consi stent populations, not measurement noise, and their existence sets a 
quantitative target for any future characterization effort. Resolving the relative contributions of structure, 
diagenesis, mechanical stratigraphy, and fluid history would require detailed structural mapping, core-calibrated 
diagenetic studies, and burial history modeling beyond the scope of the present analysis. 
• Implications for fracture prediction in carbonate reservoirs 
The decomposition of Fpor controls into a small facies -scale effect and a dominant well -scale signal has 
direct consequences for fracture prediction workflows applied to carbonate reservoirs. Facies -based 
geostatistical models, in which Fpor is conditioned on a lithofacies framework and propagated across interwell 
space, systematically miss approximately 27% of the variance at the well scale. The missed component is not 
random; it is structured, with the well -scale residuals forming discrete clusters that s hare internal statistical 
signatures (mean, CV, skewness, IQR). Predicting Fpor without representing this structure means that some 
wells will be predicted accurately by chance, while others, particularly those belonging to Cluster 2 (high CV, 
skewed) and Cluster 3 (elevated baseline), will be systematically misrepresented.

250 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
Two adjustments follow from this result. First, well-scale distributional descriptors, such as per-well mean, 
CV, skewness, or membership in the Ward cluster structure, should be incorporated as explicit conditioning 
variables alongside or in place of lith ofacies labels in fracture porosity modeling. The information content of 
these descriptors is, by the analysis presented here, approximately thirteen times that of facies classification. 
Second, model performance assessment should be partitioned by well identity rather than by random sample. A 
predictive workflow that performs adequately under random cross-validation may fail at the well scale, and the 
failure mode is precisely the inter-well heterogeneity quantified in Section 4.4. Predictive frameworks operating 
at the well scale, including machine learning approaches investigated for this dataset in a companion analysis 
(Authors, in preparation), depend on the same well-scale signal documented here. 
For blind -well prediction in particular, the practical implication is that prediction quality is governed by 
the geological similarity between the target well and the wells available for training, not by the algorithmic 
capacity of the predictive model. A blind well belonging to Cluster 3 will be poorly predicted by a model 
trained predominantly on Cluster 1 wells, regardless of model choice. This reframes the operational question 
from 'which model performs best?' to 'whether the target well is geologically  representative of the available 
training set' . 
 
4. Conclusion 
In conclusion, we quantified the controls on fracture porosity in a Malay Basin carbonate dataset using two -
scale statistical decomposition. Lithofacies classification accounted for between 1.4 and 2.0% of the total Fpor 
variance (η² = 0.014; ε² H = 0.020), with the small signal localized to a single pairwise contrast between clean 
limestone (LITH 0) and mixed carbonate (LITH 1). The mixed and tight shaly carbonate classe s (LITH 1 and 
LITH 2) were statistically indistinguishable in terms of Fpor. In contrast, well identity accounted for 
approximately 27% of the total variance ( ε²H = 0.271), an effect more than thirteen times larger than the facies 
effect. The 13 wells were  partitioned into three internally consistent clusters whose boundaries cross -cut 
lithofacies composition. 
The dominant control on fracture porosity in this dataset operates at the well scale rather than the facies scale. 
The three clusters represent distinct populations in the Fpor mean, variance, and distributional shape, and they 
cannot be reduced to lithofa cies labels, depth position, or random measurement noise. The single -facies well in 
the dataset (W5, composed entirely of LITH 2) illustrates the limitation directly: its Fpor mean is statistically 
indistinguishable from its facies peers, yet its distribut ional signature (CV = 33.1%, persistent low -amplitude 
depth profile) is among the most distinctive signatures in the dataset. Lithofacies classification, as applied here, 
cannot resolve this type of well-scale uniqueness. 
For fracture prediction in this and comparable carbonate reservoirs, the results reframed the operational target. 
A facies-based geostatistical model systematically missed 27% of the variance at the well scale, with the missed 
component structured rather t han random. Predictive workflows should incorporate well -scale distributional 
descriptors, and performance should be assessed using well -partitioned validation rather than random cross -
validation. Geological similarity between the target and training wells  is the binding constraint on the quality of 
blind-well prediction. 
The mechanisms responsible for well -scale variability (candidates include structural compartmentalization, 
diagenetic heterogeneity, mechanical stratigraphy, and fluid history) cannot be distinguished from the present 
dataset. Structural compartmentalization is consistent in principle with the fault segmentation typically produced 
by reactivated rift faults and wrench structures during the Middle to Late Miocene inversion that shaped the basin 
(Madon 2007; Tjia 1994), recent 3D seismic mapping elsewhere in the Malay Basin indicates that fault-bounded 
compartments of this kind can exert first -order control on reservoir connectivity even where individual fault 
throws are modest (Jonge et al., 2024). Diagenetic heterogeneity could produce a comparable well-scale signature 
if dolomitization or cementation fronts are laterally discontinuous between wells, consistent with the diagenetic 
variability documented in the analogous Central Luconia platforms (Janjuhah et al., 2017) . Mechanical 
stratigraphy operating below facies resolution, and differences in burial and fluid -flow history between wells,

251 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
remain equally plausible candidates and are not mutually exclusive with the other two mechanisms. Resolving 
these issues requires integrated structural mapping, core -calibrated diagenetic studies, and burial history 
modeling. The decomposition presented here establishes the magnitude of the well-scale signal and identifies the 
cluster structure within which the geological investigation should be framed. 
Limitations 
Several limitations constrain the interpretation of these results. The dataset is drawn from a single field in the 
Malay Basin, and the two-scale decomposition demonstrated here may not generalize directly to other carbonate 
basins where structural, diagen etic, and fluid-history regimes differ. The qualitative observation that well -scale 
variability dominates facies-scale variability is likely robust across carbonate settings on geological grounds, but 
the specific proportions (1.4 to 2.0% for facies versus 27% for wells) should be treated as field-specific. 
FMI-derived Fpor carries interpretation uncertainty that we cannot quantify within this study. Fracture porosity 
from image logs depends on aperture estimation, fracture -versus-non-fracture discrimination, and processing 
decisions made by the interpreting petrophysicist. The conclusions drawn here are robust to interpretation noise 
at the magnitude typical of FMI workflows, since both the facies effect and the well effect are statistical signals 
operating across hundreds of samples; sample-level noise of a few percent on Fpor would not redistribute samples 
among wells or facies sufficiently to overturn the dominant patterns. Even so, calibration of FMI Fpor against 
core data, where available, would strengthen the foundation of any predictive workflow built on these labels.  
The dataset contains 13 wells with unequal sample sizes ( n = 23 to 66). The effect -size dominance of well 
identity over facies (ε²H = 0.271 versus 0.020) is sufficiently large that unequal group sizes are unlikely to be the 
source of the contrast, but a bootstrap -based confirmation under stratified equal -N resampling would provide 
additional robustness against this concern. The lithofacies classification used here (LITH 0, 1, 2) was provided as 
part of the operator’s standard petrophysical interpretation, with the underlying methodology proprietary. The 
reliance on a vendor -supplied classification scheme introduces an interpr etive depe ndency that we cannot 
independently audit. The three classes are described by their qualitative composition (clean limestone, mixed 
carbonate, tight shaly carbonate), and this analysis treats as given. 
Finally, the finding that LITH 1 and LITH 2 are statistically indistinguishable in Fpor (Tukey p-adj = 0.482) 
admits a more pointed reading than the one offered in Section 4.2. The 3 -class scheme used here may itself be 
suboptimal for fracture characterization. An alternative classification, such as distinguishing dolomitic from 
non-dolomitic interva ls, or a core -calibrated rock -typing scheme that incorporates mechanical and diagenetic 
attributes, could resolve a larger fraction of Fpor variance at the faci es scale than the bulk -mineralogy 
framework analyzed here. The small facies effect ( η² = 0.014) is therefore not only a finding about the geology 
of Malay Basin carbonates; it is also a finding about the limits of the specific classification scheme applied  to 
them. Future work using rock-typing schemes more directly aligned with fracture -relevant attributes is a natural 
extension of this study . 
 
5. Acknowledgement 
This research was supported by the Government of Timor -Leste through the Human Capital Development 
Fund (Fundo de Desenvolvimento do Capital Humano, FDCH), under whose scholarship the first author carried 
out this work. The authors acknowledge Universiti T eknologi PETRONAS (UTP) for the institutional 
framework within which this research was conducted. The work was based within the Centre of Seismic 
Imaging (CSI), a dedicated research facility whose working environment, drawing together Masters and 
doctoral candidates, postdoctoral researchers, and faculty across geophysics, reservoir characterization, and 
subsurface data analytics, shaped the technical and intellectual development of this study in ways that extend 
beyond any single acknowledgment.

252 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
6. Declarations 
6.1 Author contributions 
Simeão Da Silva: conceptualization, methodology, formal analysis, investigation, data curation, writing – 
original draft, writing – review & editing, visualization . Muhammad Luqman Hasan: supervision, 
conceptualization, writing – review & editing . Dejen Teklu Asfha: supervision, writing – review & editing. 
Krisna Oka Mahendra: validation, resources, writing – review & editing . All authors read and approved the 
final manuscript.  
6.2 Funding statement 
This work was supported by the Government of Timor -Leste through the Human Capital Development 
Fund (Fundo de Desenvolvimento do Capital Humano, FDCH)  and Centre for Graduate Studies  (CGS -UTP), 
which funded the first author’s postgraduate scholarship. The funder had no role in study design, data 
collection and analysis, interpretation, or the decision to publish.  
6.3 Competing Interest 
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper. 
6.4 The use of AI and AI-assisted Technologies 
During the preparation of this work, the authors used Grammarly for language refinement. After using this 
tool, the authors reviewed, verified, and edited the content as necessary and take full responsibility for the accuracy 
and integrity of the content of this publication, including all statistical results and scientific interpretations. 
 
7. Glossary of terms and symbols 
 Term & 
Symbols Definition Unit 
 Fpor Fracture porosity, derived from FMI image-log 
interpretation; the target variable throughout the analysis 
fraction (v/v) 
 FMI Formation MicroImager; borehole resistivity image log 
used as the ground-truth source for fracture observation 
— 
 LITH 0 Lithofacies class 0: clean limestone categorical 
 LITH 1 Lithofacies class 1: mixed carbonate categorical 
 LITH 2 Lithofacies class 2: tight shaly carbonate categorical 
 TVDSS True Vertical Depth Sub-Sea ft 
 RS Shallow resistivity log ohm·m 
 RT Deep (true) resistivity log ohm·m 
 N, n Total sample size (N) and subgroup sample size (n) count 
 k Number of groups compared in an omnibus test count 
 CV Coefficient of variation, SD / mean × 100 % 
 IQR Interquartile range of the Fpor distribution fraction (v/v) 
 F One-way ANOV A test statistic dimensionless 
 H Kruskal–Wallis test statistic dimensionless 
 U Mann–Whitney U test statistic dimensionless 
 p Probability value; statistical significance threshold set at α 
= 0.05 
dimensionless 
 η² (eta-
squared) 
ANOV A effect size, SS_between / SS_total dimensionless 
 ε²H (epsilon-
squared-H) 
Kruskal–Wallis effect size, (H − k + 1) / (N − k) dimensionless 
 r Pearson correlation coefficient, or rank-biserial effect size 
for the Mann–Whitney test 
dimensionless 
 ρ (rho) Spearman rank correlation coefficient dimensionless 
 α (alpha) Significance threshold / family-wise error rate for post-
hoc testing 
dimensionless

253 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
8. References 
Aghli, G., Moussavi -Harami, R., & Mohammadian, R. (2020). Reservoir heterogeneity and fracture parameter 
determination using electrical image logs and petrophysical data (a case study, carbonate Asmari Formation, 
Zagros Basin, SW Iran). Petroleum Science, 17(1), 51–69. https://doi.org/10.1007/s12182-019-00413-0  
Aguilera, R. (1976). Analysis of Naturally Fractured Reservoirs From Conventional Well Logs . 
https://doi.org/10.2118/5342-PA  
Bagheri, H., & Mohebian, R. (2025). Fracture facies estimation utilizing machine learning algorithm and 
Formation Micro -Imager (FMI) log. Petroleum Research , 10(4), 764 –781. 
https://doi.org/10.1016/j.ptlrs.2025.04.006  
Berben, L., Sereika, S. M., & Engberg, S. (2012). Effect size estimation: Methods and examples. In International 
Journal of Nursing Studies  (Vol. 49, Number 8, pp. 1039 –1047). 
https://doi.org/10.1016/j.ijnurstu.2012.01.015  
Bishop, M. G. (2002). PETROLEUM SYSTEMS OF THE MALAY BASIN PROVINCE, MALAYSIA. USGS 
Science for a Changing World. https://pubs.usgs.gov/of/1999/ofr-99-0050/OF99-50T/OF99-50T.pdf  
Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences  (Second Edition). 
https://doi.org/10.1016/C2013-0-10517-X  
Esteban, M., & Taberner, C. (2003). Secondary porosity development during late burial in carbonate reservoirs 
as a result of mixing and/or cooling of brines. Journal of Geochemical Exploration , 78–79, 355 –359. 
https://doi.org/10.1016/S0375-6742(03)00111-0  
Garland, J., Neilson, J., Laubach, S. E., & Whidden, K. J. (2012). Advances in carbonate exploration and reservoir 
analysis. Geological Society Special Publication, 370(1), 1–15. https://doi.org/10.1144/SP370.15  
Hall, R. (2013). The palaeogeography of Sundaland and Wallacea since the Late Jurassic. Journal of Limnology, 
72(S2), 1–17. https://doi.org/10.4081/jlimnol.2013.s2.e1  
Humphrey, E., Gomez -Rivas, E., Neilson, J., Martín -Martín, J. D., Healy, D., Yao, S., & Bons, P. D. (2020). 
Quantitative analysis of stylolite networks in different platform carbonate facies. Marine and Petroleum 
Geology, 114. https://doi.org/10.1016/j.marpetgeo.2019.104203  
In, J., & Lee, D. K. (2024). Alternatives to the P value: connotations of significance. Korean Journal of 
Anesthesiology, 77(3), 316–325. https://doi.org/10.4097/kja.23630  
Janjuhah, H. T., Mohammad A, A., & Parsed Gho, D. (2017). Sedimentology and Reservoir Geometry of the 
Miocene Carbonate Deposits in Central Luconia, Offshore, Sarawak, Malaysia. Journal of Applied Sciences, 
17(4), 153–170. https://doi.org/10.3923/jas.2017.153.170  
Jonge, A. De, Widyanita, A., Busch, A., Doster, F., & Nicholson, U. (2024). New Insights into the Structural and 
Stratigraphic Evolution of the Malay Basin Using 3D Seismic Data: Implications for Regional Carbon 
Capture and Storage Potential. https://doi.org/10.1111/bre.12885DigitalObjectIdentifier(DOI)  
Kargarpour, M. A. (2020). Carbonate reservoir characterization: an integrated approach. Journal of Petroleum 
Exploration and Production Technology, 10(7), 2655–2667. https://doi.org/10.1007/s13202-020-00946-w  
Laubach, S. E., FALL, A., COPLEY, L. K., MARRETT, R., & WILKINS, S. J. (2016). Fracture porosity creation 
and persistence in a basement -involved Laramide fold, Upper Cretaceous Frontier Formation, Green River 
Basin, USA. Geological Magazine, 153(5–6), 887–910. https://doi.org/10.1017/S0016756816000157  
Laubach, S. E., Olson, J. E., & Cross, M. R. (2009). Mechanical and fracture stratigraphy. AAPG Bulletin, 93(11), 
1413–1426. https://doi.org/10.1306/07270909094  
Lucia, F. J. (2007). Carbonate reservoir characterization : an integrated approach (2nd ed). Springer.

254 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
Madon. (2007). Overpressure development in rift basins: an example from the Malay Basin, offshore Peninsular 
Malaysia. Petroleum Geoscience, 13(2), 169–180. https://doi.org/10.1144/1354-079307-744  
Madon, M., Jong, J., Kessler, F. L., Damanhuri, M. H., & Amin, M. K. A. (2020). Pre-tertiary basement subcrops 
beneath the malay and penyu basins, offshore peninsular malaysia: Their recognition and hydrocarbon 
potential. Bulletin of the Geological Society of Malaysia, 70, 163–193. https://doi.org/10.7186/bgsm70202014  
Madon, & Watts, A. B. (1998). Gravity anomalies, subsidence history and the tectonic evolution of the Malay and 
Penyu Basins (offshore Peninsular Malaysia). In Basin Research (Vol. 10). https://doi.org/10.1046/j.1365-
2117.1998.00074.x  
Madon, Yang, J. -S., Abolins, P., Abu Hassan, R., Yakzan, A. M., Saiful, &, & Zainal, B. (2006). Petroleum 
systems of the Northern Malay Basin. In Bulletin (Vol. 49). https://gsm.org.my/articles/702001-100556/  
Mansor, M. Y., Rahman, A. H. A., Menier, D., & Pubellier, M. (2014). Structural evolution of Malay Basin, its 
link to sunda block tectonics. Marine and Petroleum Geology , 58(PB), 736 –748. 
https://doi.org/10.1016/j.marpetgeo.2014.05.003  
Marrett, R., Ortega, O. J., & Kelsey, C. M. (1999). Extent of power -law scaling for natural fractures in rock. 
Geology, 27(9), 799–802. https://doi.org/10.1130/0091-7613(1999)027<0799:EOPLSF>2.3.CO;2  
Metcalfe, I. (2017). Tectonic evolution of Sundaland. Bulletin of the Geological Society of Malaysia, Volume 63, 
June 2017, Pp. 27 - 60. https://doi.org/10.7186/bgsm63201702  
Nelson, R. A. (1985). Geologic Analysis of Naturally Fractured Reservoirs. Gulf Professional Publishing., Vol 1. 
https://books.google.com.my/books?hl=id&lr=&id=7TI516mt3s8C&oi=fnd&pg=PP11&dq=Geologic+Anal
ysis+of+Naturally+Fractured+Reservoirs,+2nd+Ed.,&ots=TjiJsX7eln&sig=aVzWklukJvFkmZeehLx0vGRfs
Mw&redir_esc=y#v=onepage&q=Geologic%20Analysis%20of%20Naturally%20Fractured%20Reservoirs
%2C%202nd%20Ed.%2C&f=false  
Nikbin, M., & Aminshahidy, B. (2025). An integrated petrographic and petrophysical study of diagenetic controls 
on elastic response in heterogeneous carbonate reservoirs. Journal of Petroleum Exploration and Production 
Technology, 15(10). https://doi.org/10.1007/s13202-025-02058-9  
Ong, P. Y., & Jamaludin, S. N. F. (2023). Fracture Network Analysis of Karstified Subis Limestone Build-Up in 
Niah, Sarawak. Applied Sciences (Switzerland), 13(22). https://doi.org/10.3390/app132212110  
Ortega, O. J., Marrett, R. A., & Laubach, S. E. (2006). A scale -independent approach to fracture intensity and 
average spacing measurement. American Association of Petroleum Geologists Bulletin , 90(2), 193 –208. 
https://doi.org/10.1306/08250505059  
Pubellier, M., & Morley, C. K. (2014). The basins of Sundaland (SE Asia): Evolution and boundary conditions. 
Marine and Petroleum Geology, 58(PB), 555–578. https://doi.org/10.1016/j.marpetgeo.2013.11.019  
Rankey, E. C., Schlaich, M., Mokhtar, S., Ghon, G., Ali, S. H., & Poppelreiter, M. (2019). Seismic architecture 
of a Miocene isolated carbonate platform and associated off -platform strata (Central Luconia Province, 
offshore Malaysia). Marine and Petroleum Geology , 102, 477 –495. 
https://doi.org/10.1016/j.marpetgeo.2019.01.009  
Richardson, J. T. E. (1996). Measures of effect size. In Behavior Research Methods, Instruments, & Computers  
(Vol. 28, Number 1). https://doi.org/10.3758/BF03203631  
Shahar, S. (2008). Durham E-Theses Structural evolution of the Tenggol Arch and its implication for basement 
fracture patterns in the Malay Basin, Malaysia  [Durham University]. 
https://etheses.durham.ac.uk/id/eprint/2233/  
Talebian, S. H., Enayati Najafabadi, M., & Fahimifar, A. (2021). Application of improved data-driven diagnostics 
workflow based on coupled hydro -mechanical model for stimulation candidate selection in a complex 
carbonate reservoir. SN Applied Sciences, 3(7). https://doi.org/10.1007/s42452-021-04695-1

255 
 
 
 
da Silva et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2131 
 
Tjia, H. D. (1994). Inversion tectonics in the Malay Basin: evidence and timing of events. In GeoL. Soc. 
MaLaYJia, BuLLetin  (Vol. 36). https://gsmpubl.wordpress.com/wp-
content/uploads/2014/09/bgsm1994027.pdf. 
Wahid, A., Sultan, Farida, M., Jamaluddin, & Ryka, H. (2026). Depositional facies influence on reservoir 
heterogeneity in the Balikpapan Formation, Lower Kutai Basin: Insights well log. Scientific Contributions Oil 
and Gas, 49(1), 219–234. https://doi.org/10.29017/scog.v49i1.1985 
Wilson, M. E. J. (2002). Cenozoic carbonates in Southeast Asia: implications for equatorial carbonate 
development. Sedimentary Geology, 147(3–4), 295–428. https://doi.org/10.1016/S0037-0738(01)00228-7  
Wilson, M. E. J., & Hall, R. (2010). Cenozoic carbonate systems of Australasia. SEPM (Society for Sedimentary 
Geology). https://doi.org/10.2110/sepmsp.095.013
