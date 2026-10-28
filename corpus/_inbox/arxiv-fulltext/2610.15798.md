---
source_id: "arxiv"
title: "Ionomer-free Iridium Anodes with Low Loading"
url: "https://arxiv.org/abs/2610.15798"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2610.15798. Abstract: Ionomer-free Iridium Anodes with Low Loading
for Zero-gap Electrolyzers via Direct Atomic
Layer Deposition
Peter M. Piechulla,∗,† Iris Blommestein,† Anne van Gerven,† Henri Pelzer,† Ezgi
Demir¨ oz,† Jonas Englhard,‡ Mingliang Chen,† Julien Bachmann,‡ and J. Ruud
van Ommen†
†Department of Chemical Engineering, Delft University of Technology, 2629 HZ, Delft, The
Netherlands
‡Chair ’Chemistry of Thin"
---

# Ionomer-free Iridium Anodes with Low Loading

Ionomer-free Iridium Anodes with Low Loading
for Zero-gap Electrolyzers via Direct Atomic
Layer Deposition
Peter M. Piechulla,∗,† Iris Blommestein,† Anne van Gerven,† Henri Pelzer,† Ezgi
Demir¨ oz,† Jonas Englhard,‡ Mingliang Chen,† Julien Bachmann,‡ and J. Ruud
van Ommen†
†Department of Chemical Engineering, Delft University of Technology, 2629 HZ, Delft, The
Netherlands
‡Chair ’Chemistry of Thin Film Materials’, Materials Chemistry section, Department of
Chemistry and Pharmacy, Friedrich-Alexander-Universit¨ at Erlangen-N¨ urnberg, IZNF,
Cauerstr. 3, 91058 Erlangen, Germany
E-mail: p.m.piechulla@tudelft.nl
Abstract
Proton exchange membrane water electrolysis (PEMWE) is among the most promis-
ing techniques to provide hydrogen as both energy carrier and feedstock for the chem-
ical industry, due to its compatibility with intermittent renewable electricity sources.
However, a major bottleneck in scaling up PEMWE is the limited supply of the an-
ode catalyst Ir. This work shows a novel approach to tailoring ionomer-free catalyst
layers based on custom-made microporous substrates and two different atomic layer
deposition (ALD) processes, both using Ir(EtCp)(CHD) precursor. Thermal ALD us-
ing O 3 as counter-reactant yields mostly metallic Ir/IrO x and an electrode Ir loading
1
arXiv:2610.15798v1  [cond-mat.mtrl-sci]  11 Oct 2026

of 0.21 mg·cm−2. The PEMWE cell-level performance is comparable to a commercial
catalyst-coated membrane anode despite 7×lower loading, and is maintained over an
accelerated durability test equivalent to 600 h of intermittent operation. Moreover, us-
ing a low-loading ALD-made cathode, the total platinum group metal loading is only
0.24 mg·cm−2. Plasma-enhanced ALD reduces the Ir loading to 0.04 mg·cm−2 by tailor-
ing the catalyst distribution, however, yields lower-activity IrO 2. Finally, direct ALD
catalyst deposition needs no ionomer-bearing ink. The anodes are therefore compatible
with various membrane materials, as demonstrated in a CO 2 electrolysis experiment
with an anion exchange membrane.
Introduction
The energy transition is in full swing, and solar and wind are now among the least ex-
pensive sources of newly installed electrical power. The new frontier is electrification of
material cycles which goes hand in hand with medium-term energy storage technology using
energy carriers such as hydrogen. Zero-gap, membrane-based electrolysis is among the most
promising technologies addressing both these challenges because of its high power densities
and compatibility with intermittent electricity supply. Proton exchange water membrane wa-
ter electrolysis (PEMWE) is a prominent example, providing hydrogen both as a feedstock
for the production of base chemicals and as an energy carrier, thereby replacing fossil fuels
in both of these functions. Alternatively, membrane-based electrolysis exhibits significant
potential to produce higher-value chemicals directly, such as direct electrolysis of CO 2 to
hydrocarbons. Key components for any electrolyzer are effective and stable electrocatalysts
for both the anode and cathode half-reactions.
Platinum group metal (PGM) catalysts are highly active and exceptionally stable, but
are also scarce and expensive. Especially for Ir as the classic catalyst for the oxygen evo-
lution reaction (OER), inelasticity of the supply may soon pose a major bottleneck when
scaling electrolysis technology to the magnitude required to replace fossil fuels. Technological
2

roadmaps 1,2 for PEMWE therefore include goals to reduce the required amount of Ir from
typically>1 mg·cm −2, for example to≤0.2 mg·cm −2 or, in terms of power-specific loading
≤0.4 g·kW−1.
Traditional wet deposition methods for catalyst layer fabrication reach limits in reducing
the loading in the sub– mg·cm −2 range. 3,4 The approach consists of multiple steps: first,
catalyst particles are synthesized; second, the particles are combined with a polymer elec-
trolyte binder and further additives into an ink or slurry formulation; third, the ink/slurry is
deposited onto a substrate by means of spray coating, doctor blading or slot-die coating. Es-
pecially in thin catalyst layers, the homogeneity of catalyst distribution is ultimately limited
by the finite size of the catalyst particles, which leads to non-contiguous layers and thus poor
electrical contact between catalyst particles and porous transport layers (PTLs). 3 Though
low power-specific Ir loadings (high mass-activity) can be achieved, the inhomogeneity harms
the performance of the electrolyzer by increasing the overpotential.
To simultaneously achieve both low power-specific Ir loading and low overpotential, meth-
ods that directly deposit catalytically active material onto a PTL have recently attracted
attention as an alternative to traditional wet deposition. 5 This approach reduces the com-
plexity of fabrication by uniting the three steps of catalyst synthesis, ink/slurry formulation
and deposition into a single deposition step. The resulting porous transport electrodes
(PTEs) are ionomer-free, and are therefore compatible with a variety of membrane materials
besides the traditional acidic, fluorinated ionomers such as Nafion™. Ionomer-free PTEs can
be made through a variety of methods, ranging from wet-chemical6 and electrodeposition, 7 to
physical vapor deposition (sputtering).8 Through all of these methods, low Ir weight loadings
between 0.08 and 0.34 mg·cm −2 have been achieved, while simultaneously reaching similar
or higher currents than their conventional CCM references, respectively. Notably, all of the
cited studies included pretreatment steps to increase the surface area before Ir deposition, 8
or used proprietary substrates and the Ir catalyst itself comprised a nano structure. 6,7
Atomic layer deposition (ALD) is well known for its facility to conformally coat rough and
3

three-dimensional structures, 9 its wide range of attainable catalyst materials, and facility to
tailor catalyst morphologies on the nano-scale. 10 Using ALD to coat commercial carbon-
based microporous layers (MPLs) directly with Pt, we recently demonstrated PEMWE PTE
cathodes with exceptionally low Pt loadings in the range of 1 to 5µg·cm −2, which is about
100×lower than the benchmark commercial CCM cathode. 11 These cathode PTEs achieved
similarly low overpotentials and maintained a stable performance over an accelerated dura-
bility test (ADT). This approach, in particular in combination with the recent advances
in scalable, spatial ALD technology bears significant potential to reduce both Pt consump-
tion and complexity of catalyst layer fabrication. 12,13 Similarly, ALD has been explored to
fabricate OER electrodes based on Ir, 14 but such anodes in a PEMWE experiment have
thus far been limited to current densities<0.2 A·cm −2. 15 Due to the sluggish OER kinetics,
high currents at acceptable overpotentials are difficult to achieve. 16,17 An obvious solution
is compensating the lower activity by increasing the catalytically active surface. 12 However,
commercially available PTLs with MPLs that provide high specific surface areas to deposit
Ir on are typically carbon-based, 11 and therefore not suitable for the oxidative potentials at
the anode. Additionally, it is unclear how the particular growth behavior of ALD will affect
the catalyst activity and loading of a PTE, since ALD is known for its conformality whereby
the coating can reach deep into porous structures. 9
In this study, we investigate the interplay of direct ALD of Ir/IrO x and custom-made
MPLs to fabricate low Ir loading anodes for PEMWE (Figure 1). We begin by showing
the differences between oxidization state and activity of PEMWE anode catalysts made by
thermal ALD (ThALD) and plasma-enhanced ALD (PEALD). We then enhance the surface
area and activity of the respective catalysts by introducing an MPL made from sintered Ti
nanoparticles. Crucially, the catalyst distribution within the MPL is accessible through the
choice of deposition process (ThALD or PEALD), which affects the Ir loading and perfor-
mance of the respective anodes. ThALD MPL anode shows stable performance, whereas
a PEALD anode shows significant degradation. For the case of a ThALD MPL anode, we
4

Figure 1: Schematic illustration of the PTE fabrication approach demonstrated in this work.
Ti fiber felts are either directly coated with Ir via ALD, or first equipped with an MPL, and
then coated with Ir. The fabricated anodes are tested against ALD-made ionomer-free
cathodes presented by Chen et al. 11
discuss the individual overpotential contributions (charge transfer, ohmic, mass transport)
which we distinguish through electrochemical impedance spectroscopy (EIS). This analysis
reveals a qualitative difference in mass transport overpotential compared to a traditional,
wet-deposited CCM anode. Zooming out from the discussion of individual anodes, we discuss
the power-specific Ir loading together with the current density for a range of different ALD-
made anodes, and show that each configuration of ALD process and PTL/MPL substrates
requires its own loading optimization. Finally, we demonstrate the versatility of ALD-made
ionomer-free anodes by showing their function in an anion exchange membrane (AEM)-based
CO2 electrolyzer.
Results
ALD of iridium
Two different ALD processes, ThALD and PEALD, are investigated throughout this study.
Both processes used the same Ir(EtCp)(CHD) precursor, and were carried out at 220°C
5

reactor temperature. Further parameters are described in the Methods section, and results
are discussed in the following.
Thermal ALD
The ThALD process has been presented in previous studies, 18,19 and uses O 3 as a counter-
reactant. To study the chemical composition and oxidation state, we analyzed a layer de-
posited by 75 ThALD cycles on planar reference samples using X-ray photoelectron spec-
troscopy (XPS). A survey scan (Supporting Information Figure S1a) of a ThALD sample
showed a composition of 48.9 % at Ir, 36.4 %at O and 14.9 %at C; the latter could stem from
unreacted precursor residues or adventitious C from the environment. The underlying Ti of
the substrate was not detected which indicates that 75 cycles led to a closed film.
The low ratio [O]/[Ir] suggests that Ir is to a large part metallic. Fitting to the Ir 4f peak
region of a high-resolution XPS scan (Figure 2a) indeed confirms that the ThALD process
produces metallic Ir 0 (88 %), which contained only about 12 % Ir4+. To elucidate the nature
of the Ir oxide detected, we further analyzed the O 1s region (Figure 2b). The peak near
530 eV and a satellite peak (summarized in green in Figure 2b) is associated with IrO 2. 20,21
The higher binding energy peak (around 532 eV, red) is associated with IrOH 21 or other
IrOx types. 20 We conclude that the metallic Ir layer is terminated with Ir oxide, which may
be partly hydroxylated.
According to X-ray reflectometry (XRR) measurements (Supporting Information Fig-
ure S2), the film was approximately 1.2 nm thick and the density lower than expected for
metallic Ir, indicating a rough layer. However, we note that the layer was close to the lower
detection limit of the XRR method, therefore these values are rather indicative, i.e., could
vary by±1 nm. Upon increasing the number of cycles to 150, the layer thickness increased
to 5 nm, and the density approached that of a dense metallic Ir layer. These two experiments
indicate a growth per cycle (GPC)≈0.5 ˚A, which is lower than the 0.6–0.9 ˚A reported ear-
lier for the same process, 19,22 however, these earlier studies used different substrates. Also,
6

we observe a significant growth delay of about 50 cycles due to due to substrate-inhibited
nucleation (Supporting Information Figure S4), which is also observed for the Ir loading of
PTL substrates that will be discussed later (Supporting Information Figure S7).
Figure 2: High resolution XPS scans of the Ir 4f (a, c) and O 1s (b, d) region for ThALD
(a,b) and PEALD (c,d).
Plasma-enhanced ALD
To explore the potential of different ALD processes, we additionally developed a PEALD
processes that uses O 2 plasma as a counter-reactant. The XPS survey scan of a PEALD
sample (Supporting Information Figure S1b) showed a composition of 27.5 %at Ir, 61.7 %at O
and 10.8 %at C. The ratio [O]/[Ir]=2.2≈2 indicates the presence of IrO 2, which is supported
by the Ir 4f region fit showing 97 % Ir 4+ (Figure 2c) and<3 % Ir 0. The O 1s region further
shows the distinct peak shape of crystalline IrO 2. 20,23 Fitting different components to the
O 1s region indeed supports the hypothesis that the layer consisted of IrO 2, 20,21 with a
minority of IrO x or IrOH that likely terminates the surface. Notably, this is different from
recent results of van de Poll et al., who observed mostly metallic Ir from PEALD at reactor
7

temperaturesT >200°C. 12 However, they used N 2 as carrier gas at atmospheric pressure
instead of the Ar carrier gas and vacuum conditions used in the PEALD of the present study.
Judging from the XRR-determined layer thicknesses (Supporting Information Figure S3),
IrO2 growth shows both a delay at low number of cycles, and a decrease of GPC beyond 300
cycle (Supporting Information Figure S4). On average, a GPC≈0.3 ˚A was obtained, which
is slightly lower than≈0.4 ˚A as previously reported for PEALD processes using the same
precursor. 12 Alongside IrO 2 film growth, we observe a growth of the underlying TiO x layer
(Supporting Information Figure S3) to up to 11 nm thickness after 600 PEALD cycles.
OER activities of bare Ir layers
To compare the OER activities of catalyst materials from the ThALD and PEALD process,
we coated two bare, commercial Ti fiber felt PTLs (Figure 4a) with 150 cycles of either one
process (Figure 3). We tested these anode PTEs in a PEMWE single cell experiment using
ALD-made Pt PTEs as cathodes for which we demonstrated high and stable performance
despite a Pt loading of only 22µg·cm −2 in a previous work. 11 A direct comparison between a
commercial, double-sided CCM and the anode CCM used as reference in this work is shown
in Supporting Information Figure S5, indicating no limitation from the PTE cathode used
here.
Figure 3: Performance of porous transport electrodes (PTEs) made by ALD of Ir/IrO 2 onto
bare Ti felt (BF) PTLs. a) Polarization curves. b) Tafel plots with fitted slopes in up to
10−2 A·cm−2.
8

Both anodes achieved currents>1 A·cm −2 within the tested cell voltage range up to
2 V (Figure 3a). However, the ThALD-made catalyst showed a higher performance than
the PEALD catalyst due to the lower activation overpotential, as indicated by the steep
increase ofV cell at low currents. Increasing the number of PEALD cycles beyond 150 did not
further increase the anode performance (Supporting Information Figure S6a), likely since
the Ir-based layer is already closed at 150 cycles.
To compare the activity of the catalysts in terms of a material property, we performed
additional measurements at low currents and fitted the Tafel equation (Equation 3 in the
Methods section) in the low current range up to 10 −2 A·cm−2. Even though this yields both
the exchange current densityj 0 and the Tafel slopeb, we focus the following discussion on
the Tafel slope, sincej 0 is obtained by extrapolating the current density over several orders
of magnitude, leading to high uncertainties. 17 For the PEALD anode, the observed slope of
66 mV·dec−1 is similar to the 72 mV·dec−1 observed for crystalline IrO2 by Reier et al.,23 and
therefore in line with the observation of IrO 2 via XPS from our PEALD process at 220°C.
The Tafel slope of the ThALD-made anode is 51 mV·dec −1, which in the range of reported
values of 40–60 mV·dec−1 for amorphous IrOx. 17,23,24 This agrees with the observation in the
XPS discussion (above) that the ThALD-deposited metallic Ir covered by a thin layer of
amorphous IrOx. In addition, metallic Ir typically oxidizes to amorphous IrO x under anodic
potentials. 25
Note that we limited the fitting range in Figure 3b to≤10 −2 A·cm−2 instead of the more
commonly used≤10 −1 A·cm−2 for effective Tafel slopes on the cell level in the literature.
The logarithmic plots (Figure 3b) show deviations from the ideal linear behavior already
for current densities between 10 −2 A·cm−2 and 10 −1 A·cm−2, indicating limitations beyond
bare catalyst activity such as mass transport limitations (to be discussed at a later stage).
Limiting the current range to lower currents was a deliberate choice to identify the bare
catalyst activity rather than an effective electrode activity.
The Ir loading of both anodes differ dramatically (Table 1), with 68×lower loading for
9

PEALD versus ThALD. During the PEALD process, Ir precursor is dosed while continu-
ously vacuum-pumping the reactor chamber due to technical reasons. In contrast to this,
for ThALD process, the precursor is dosed into the vacuum chamber while pumping is in-
terrupted through a valve between vacuum pump and reactor chamber. 18,26 This allows for
a soaking step to increase precursor utilization, during which the precursor can also diffuse
deeper into the Ti felt substrate. Thus, the coating reaches deeper into the PTL, where it
increases the anode loading, but has no effect on the electrocatalytic activity. Furthermore,
we suspect that the ozone counter-reactant of the ThALD process may have a longer life-
time than oxygen radicals from the plasma when diffusing into the PTL. 12 This aspect is
discussed in more detail in the context of MPL anodes.
PEMWE anodes on MPLs
Anodes based on bare Ti felt PTLs offer limited active surface areas which can be increased
by adding an MPL. Bare PTLs consist of a nonwoven mesh of microfibers, and therefore
exhibit a rather coarse structure on the microscale (Figure 4a). Upon assembly of the
membrane with the PTE, only part of the Nafion™membrane surface is in contact with
the catalyst coated fiber surface. Additionally, the fibers exhibit a smooth surface, with a
surface area close to their geometrical surface area. Both aspects contribute to a low active
surface area of the PTE for the samples discussed above. To smoothen the PTL surface on a
microscale (Figure 4b) and at the same time add texture to the fiber surface on a nanoscale
(Figure 4c,d), we developed a spray coating method to equip the PTLs with an MPL (see
Methods section for experimental details). These MPLs were then coated with the same
ALD processes as before the bare Ti felts.
Anode performances from both the ThALD and PEALD process benefited from the
increased surface area of the anode MPL (compare Figure 3a and 5a). For the ThALD
150c MPL anode the current increased by about 20 % at a benchmark voltageV cell = 1.8 V
compared to the ThALD 150c anode (Table 1). In contrast, the PEALD 450c MPL anode
10

Figure 4: SEM images of the anode substrates used in this paper. a) Bare Ti fiber felt (BF).
b)-d) Ti fiber felt coated with Ti MPL from Ti nanoparticles
more than doubled in current when compared to the PEALD 150c anode on bare felt.
The optimal number of cycles of the PEALD process to achieve the highest performance
differs per type of substrate (see optimization in Supporting Information Figure S6), pre-
sumably due to the difference in specific surface area. To accommodate for this aspect, we
increased the number of cycles from 150 (BF) to 450 (with MPL), while noting that adapting
the dosing time may have led to a similar result.
To characterize the catalyst activity, we again performed low-current measurements and
obtained the Tafel plots in Figure 5b. For consistency, the fitting range was limited to
the strictly linear range up to 10 −2 A·cm−2. The implications of the fitting range will be
discussed at a later stage. For the ThALD process, the Tafel slope decreased moderately by
4 mV·dec−1 to 47 mV·dec−1 due to the introduction of the MPL (Table 1), which is similar to
literature values for PEMWE anodes. 27 The PEALD MPL anode showed a clearer decrease
in Tafel slope by 11 mV·dec−1 to 55 mV·dec−1 compared to the BF substrate. This increase
in activity in both cases could be related to the nanoscale curvature of the MPL and thus
different structure of the Ir and IrO 2 film, respectively. It seems plausible that in both cases
the curvature led to more lowly-coordinated edge atoms compared to films grown on the
smooth microfibers of the BF substrate. 12 However, as the surface of the ThALD Ir was
already terminated by an amorphous IrOx with a non-crystalline structure, the effect in case
of the PEALD IrO 2 was stronger, leading to the more pronounced reduction of the Tafel
slope.
11

Figure 5: a) Polarization curves for three cells with ALD-made anodes using MPLs and one
commercial CCM anode reference. Series resistance-free (V cell −j·R Ω) polarization curves
are shown in lighter colors. b) Tafel plots of the same anodes from a separate, low current
measurement. Data points are marked with symbols; lines show linear fits in the range
from 10 −3 to 10 −2 A·cm−2; fit parameters are given in Table 1. c–e) Si reference samples,
with layer analog to MPL and deposited Ir. Samples were cleaved before recording electron
micrographs using a backscattered electron detector (BED) for enhanced material contrast.
Ir appears lighter in color, as independently confirmed through EDX linescans (Supporting
Information Figure S10, in this file below). Scaling is identical for figures c–e.
12
