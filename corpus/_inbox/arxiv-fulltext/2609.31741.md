---
source_id: "arxiv"
title: "Pressure and temperature dependence of methane"
url: "https://arxiv.org/abs/2609.31741"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.31741. Abstract: Pressure and temperature dependence of methane
pyrolysis and hydrogen production in a micro flow
reactor
Mohammad Reza Razavia,∗, Ömer L. Güldera
aUniversity of Toronto Institute for Aerospace Studies, 4925 Dufferin Street, Toronto, M3H 5T6, Canada.
Abstract
Methane pyrolysis experiments were performed in a micro flow reactor to investigate the chemical mechanism
sensitivities at elevated pressure"
---

# Pressure and temperature dependence of methane

Pressure and temperature dependence of methane
pyrolysis and hydrogen production in a micro flow
reactor
Mohammad Reza Razavia,∗, Ömer L. Güldera
aUniversity of Toronto Institute for Aerospace Studies, 4925 Dufferin Street, Toronto, M3H 5T6, Canada.
Abstract
Methane pyrolysis experiments were performed in a micro flow reactor to investigate the chemical mechanism
sensitivities at elevated pressures and temperatures. The micro flow reactor used in this study provides independent
control over reaction parameters. Experiments were performed at temperatures from 1400 to 1800 K and pressures
from 1 to 10 bar at a fixed residence time of 60 ms. The yields of hydrogen, unreacted methane, and solid carbon
were quantified for comparison to predictive models. The mass of heterogeneous depositions was also quantified.
The presence of C 2 and PAH species were measured by GC-MS. The results were compared to 1D simulations
using a discrete sectional model for capturing the kinetics of particulate formation and surface deposition. The
simulations replicated the pressure trend well at high temperatures (1800 K), but the sensitivity to temperature
was in disagreement. Simulations generally found lower carbon and hydrogen yields and a stronger sensitivity
to temperature than the experiment. An abundance of PAH intermediates was measured at lower temperatures
and higher pressures. The simulated surface deposition rates were lower than the measured values but showed
similar profiles. The results demonstrate the utility of micro flow reactors in recreating pyrolysis environments for
hydrogen production from methane. The predictive capabilities of simulations could be improved by advancing the
fuel decomposition and PAH formation and consumption kinetics at low temperatures and by detailed treatment of
surface site density.
Keywords:Methane pyrolysis, Micro flow reactor, Carbon Formation, Hydrogen production, High pressure
∗Corresponding author: University of Toronto Institute for Aerospace Studies, 4925 Dufferin Street, Toronto,
M3H 5T6, Canada.
Novelty and significance statement
Pyrolysis studies in shock tubes or flow reactors
typically cannot resolve overlapping processes gov-
erning carbon formation. A micro flow reactor is used
to investigate carbon formation processes indepen-
dently at intermediate residence times and high pres-
sures — conditions for which experimental data re-
mains limited. The study found opposite pressure de-
pendencies between heterogeneous and homogeneous
carbon formation rates and revealed their temperature
sensitivity, trends that have not been previously re-
solved. PAH and H2 trends are reported which further
enrich the modelling database.
Current kinetic mechanisms for gas phase carbon
formation and surface deposition predict higher on-
set temperatures and lower deposition rates than mea-
sured and disagree with experimental pressure depen-
e-mail:m.razavi@mail.utoronto.ca(Mohammad
Reza Razavi)
dencies and temperature sensitivities for some condi-
tions. Insufficient surface reactions, constant site den-
sity, and fuel decomposition reactions are identified as
key areas for improvement. Models resolving surface
deposition and gas phase trends and intermediates at
wider conditions can improve predictive capabilities
for pyrolysis reactor design.
1. Introduction
Methane pyrolysis can be an effective substitute for
conventional steam methane reforming for H2 produc-
tion, retaining the carbon content in solid phase. It has
benefits of both preventing CO2 emissions and provid-
ing a source for carbon black production [1]. However
methane pyrolysis reactions can be difficult to char-
acterize. The enhancement of commercial methane
pyrolysis processes relies on accurate kinetics and re-
quires better understanding of the dependencies of
carbon formation mechanisms [2].
For commercial hydrogen production, these de-
pendencies are studied at low temperatures (less than
1300 K) and often in the presence of catalysts. How-
arXiv:2609.31741v1  [physics.chem-ph]  23 Sep 2026

2 Razavi et al./Combustion and Flame (2026)
ever in combustion environments such as in gas tur-
bines or diesel engines, fuel pyrolysis contributes to
formation of soot particulates at flame temperatures
(about 2200 K) and pressures up to 250 bar [3, 4]. In-
vestigating methane pyrolysis at engine relevant con-
ditions can provide a more robust understanding of the
underlying kinetics and lead to better characterization
of the carbon formation processes.
Soot formation in non-premixed methane combus-
tion follows mainly the chemistry of methane pyrol-
ysis. This begins with fuel decomposition and poly-
cyclic aromatic hydrocarbon (PAH) formation. Their
mechanisms have been developed extensively based
on shock tube and flow reactor measurements [5, 6].
Understanding of nucleation and soot growth has also
been developed from shock tubes [7], laminar diffu-
sion flames (LDF) [8] and turbulent flames [9], coun-
terflow diffusion flames (CDF) [10], and flow reactors
[11], among others. Discrete sectional models com-
bining the soot growth kinetics with fuel and PAH
chemistry work well to cover a range of reaction do-
mains [12]. However, further investigation is needed
to thoroughly characterize the soot and carbon forma-
tion processes and how they vary under different op-
erating conditions. The complicated kinetics of fuel
decomposition, nucleation, and gas-solid chemistry
makes this characterization challenging [13].
Studies in both shock tubes and flow reactors can
address this challenge but with limitations. Although
shock tubes can provide high temperatures and pres-
sures and are used to study methane pyrolysis [14, 15],
the isothermal condition fails for high fuel fractions
undergoing endothermic pyrolysis. Flow reactors are
more restrained in the reaction conditions, but offer
more flexibility with the fuel composition and oper-
ate over longer residence times [16, 17]. Micro flow
reactors providing isothermal conditions for high fuel
fractions are an alternative method, enabling isolation
of reaction parameters and flexibility in fuel compo-
sition with access to a wide range of residence times.
They have been adopted both for PAH chemistry and
soot formation studies [18, 19]. Typical operating
conditions from a survey of several shock tube and
flow reactor experiments are shown in Fig. 1 along
with the operating conditions of the micro flow reac-
tor used in the current work. While some overlap ex-
ists in the pressure-temperature regimes between the
three reactor types, the micro flow reactor provides
access to novel mass fractions and residence times in
between shock tube and flow reactor conditions.
1.1. Soot formation in gas phase
For gas turbines typical residence times in the com-
bustor range from 10 to 20 ms ([3]) and diesel engines
can vary around 100 ms. During this time many com-
bustion processes take place in addition to gas phase
pyrolytic soot formation such as spray vapourization
and oxidation. Due to the highly turbulent conditions
500 1000 1500 2000 2500
1
10
100Pressure (atm)
Temperature (K)
Shock
Tube
Micro Flow
Reactor
Flow Reactor
LDF/CDF
Engine
Conditions
0.001 0.01 0.1 1 10
0.0
0.2
0.4
0.6
0.8
1.0Fuel Mole Fraction
Residence Time (s)
Shock Tube
Micro
Flow
Reactor
Flow
Reactor
LDF/CDF
Engine
Conditions
*Engine and LDF/CDF showing local (pyrolysis zone) fractions
Fig. 1. Typical reactor operating regimes for methane py-
rolysis studies in shock tubes, flow reactors, and micro
flow reactors. Soot forming combustion conditions in non-
premixed LDFs, CDFs, and engines shown assuming local
mole fractions in the pyrolytic flame zone. For surveyed
studies see the supplementary material.
the time history of the pyrolysis reactions becomes in-
tractable. In laboratory LDF and laminar CDF this
temperature time history is better characterized but
not constant, with typical residence times of several
tens of ms over temperatures varying from 1500 K to
2000 K [13]. The typical operating pressures, tem-
peratures, residence times, and fuel mass fractions for
gas phase soot formation in both engines and labora-
tory flames are also shown in Fig. 1. The micro flow
reactor can access the engine relevant gas phase soot
forming conditions under constant temperature time
history.
In this work a micro flow reactor was used to study
methane pyrolysis at high temperature, high pres-
sures, and residence times typical of gas phase soot
formation at engine relevant conditions. Yields of
major gas species and both heterogeneous and homo-
geneous carbon were quantified. Experimental find-
ings were compared to numerical simulation results
obtained from the latest sectional models of soot for-
mation.
2. Methodology
2.1. Experimental
A micro flow reactor was built to provide isother-
mal high pressure pyrolysis conditions. The main
components consist of a ceramic tube (3.175 mm
ID) where the reaction takes place, a heated 6-way
valve (Valco) which prepares the inlet mixture, and a
solid and gas sampling system for measurement of the
products. A schematic of the apparatus is shown in
Fig. 2. Reactor heating is provided by H 2/O2 flames,

Razavi et al./Combustion and Flame (2026) 3
Insulation
Linear
rail
Two-color pyrometry
temperature measurement
H2/O2 flame heating manifold
Micro flow Reactor
Air
cooling
0 5 10 15 20 25 30
300
600
900
1200
1500
1800
Position (cm)
Temperature (K)
1800 K 
1600 K 
1400 K
Injection 
Valve
Solid/Gas
Sampling
Fig. 2. Schematic of the micro flow reactor.
and temperature measurement by two-color pyrome-
try (Optris CTRatio). Mixtures of CH 4 diluted in Ar
were preheated in the sample loop of the 6-way valve
and sent through the reactor using N2 carrier gas. The
novelty of the apparatus is in combining an injection
valve with a plug flow reactor, thereby providing con-
trol of the temperature, composition, and critically the
volume of the injected fuel mixture. This enables in-
termittent reactor operation for durations between 1 to
5 seconds while keeping reaction residence time con-
stant between 15 to 100 ms. The controlled duration
limits the accumulated carbon mass and enables car-
bon yields to be quantified.
At the reactor exit, gas products were sampled into
evacuated volumes of a sample trapping valve (Valco)
through a heated probe while solid products were col-
lected on a porous alumina filter. Solid products de-
posited on the tube walls were collected by cutting
the reactor into 20 mm segments along the length.
The cut segments and the porous filter were washed
with deionized water and dried in a thermal vacuum
prior to carbon burnoffmeasurement (Eltra SC800)
for quantification of total solid carbon mass. For ad-
ditional details the reader is refereed to the supple-
mentary material. Collected gas samples were split
and measured through GC-MS for qualitative analy-
sis of PAH and GC-TCD for quantification of light
gas species. Multiple gas samples were collected per
run by repeating the fuel mixture injections and purg-
ing with O2 between each injection. The collected gas
samples were analysed through an automated injec-
tion sequence.
2.2. Isothermal reaction conditions
Evaluation of the isothermal assumption in the mi-
cro flow reactor was performed by simulations, in-
ternal temperature measurements, and experiments.
Simulations using 2D non reacting flow with heat
transfer were performed to assess heat transfer rates
and internal temperature profiles. The analysis found
the carrier gas temperature at the centerline reaches
the wall temperature within 1 to 3 ms.
Internal temperature measurements were taken us-
ing a 1.6 mm diameter C-type thermocouple posi-
tioned inside the reactor. The closed radiative envi-
ronment prevents any heat loss in the thermocouple
and thereby the measured values are representative of
the internal wall temperature. The thermocouple was
used to calibrate the two-color pyrometry instrument
to represent internal wall temperatures by observation
of the external wall temperature. The temperature
drop was then observed during pyrolysis reactions and
found temperature drops by a maximum of about 100
K for the highest carbon loading cases. This is within
the temporal and spatial fluctuations of wall tempera-
ture on the order of±50 K. Typical wall temperature
profiles are shown in the inset in Fig. 2. Measurement
uncertainty analysis is provided in Section 2.5.
Further experiments were performed with varying
mass fractions of 10, 50, and 90% methane in Ar at
1800 K, from 1 to 10 bar, Fig. 3. For both the 10%
and 90% mass fractions the carbon yield increased
with increasing pressure, and had similar absolute val-
ues. For the 50% fuel mass fraction condition the
carbon yields decreased with increasing pressure, but
closely matched the 10 and 90% conditions in abso-
lute values. The differing trends are attributed to shifts
in underlying mechanisms sensitive to mass fraction.
They are not attributed to temperature shifts due to
endothermic pyrolysis, as all mass fractions (particu-
larly 10 and 90%) found similar yields. Despite the
90% case having 9 times higher energy loss from py-
rolysis compared to the 10% case the yields remained
comparable, indicating the heat transfer rate is far
higher than the heat absorption rate and the isother-
mal assumption is valid. To facilitate the instrument
limits of carbon deposition measurements simultane-
ously with gas species measurements, the 50% mass
fraction condition was selected for subsequent exper-
iments.
0 2 4 6 8 10
0.0
0.1
0.5
0.6
0.7
0.8
0.9
1.0
Carbon Yield ( )
Pressure (bar)
 10%  50%  90%
Fig. 3. Carbon yields from pyrolysis of methane at 10, 50,
and 90% fuel mass fraction, 60 ms residence time, 1800 K.

4 Razavi et al./Combustion and Flame (2026)
1300 1500 1700 1900 2100 2300
0.0
0.2
0.4
0.6
0.8
1.0
1730 K1500 K
Mass Fraction (Norm.) ( )
Temperature (K)
 Carbon
 
 
 Exp. Onset T
Fig. 4. Simulation results of methane pyrolysis at 60 ms res-
idence time and 1 atm pressure using the CRECK mecha-
nism. Simulated and experimental soot onset temperatures
shown.
2.3. Reaction onset temperature
Additional simulations of the pyrolysis reaction
were performed across a range of reaction tempera-
tures, see Fig. 4. Details of the simulation mechanism
are provided in Section 2.4. These were fixed at a resi-
dence time of 60 ms and a pressure of 1 atm. The sim-
ulations found an onset temperature for carbon forma-
tion of approximately 1500 K and maximum carbon
mass fractions at 1730 K. The range of temperatures
selected for the experiment covers this domain from
1400 K to 1800 K. Experimentally it was found that
at 1300 K, there was no carbon formation for the 60
ms residence time, while significant yields were mea-
sured at 1400 K. This suggests a true onset tempera-
ture between 1300 and 1400 K.
This range is in agreement with measurements in
LDF and spray pyrolysis experiments [20, 21, 22].
For CH4 Saito et al. found a soot onset temperature
of 1390 K along the centerline of LDFs [20]. For
other fuels up to benzene the onset temperature var-
ied between 1300 and 1400 K [20, 21], while forn-
dodecane spray pyrolysis it was measured at 1450 K
[22]. In LDFs the onset temperature is reduced by
the presence of trace oxidative radicals which are not
present in the current study. Koshi et al. suggested
that the surface depositions in high surface area flow
reactors may have a disordered structure acting as
a catalytic pyrocarbon [23]. The catalytic effect of
surface depositions may substitute the effect of trace
radicals found in LDFs and lead to the good agree-
ment observed in onset temperature. The selected ex-
periment temperature range of 1400 to 1800 K cap-
tures both onset carbon formation and high tempera-
ture phenomenon.
2.4. Simulations and kinetic mechanisms
Simulations of a 1D isothermal plug flow reac-
tor (PFR) were performed using the OpenSMOKE++
[24] solver. The CRECK mechanism [25] optimized
for CH 4 (C1-C16+Soot) was used to simulate soot
formation kinetics including a gas phase sectional
model for tracking soot growth. The model has been
extensively validated for many flame types (see for ex-
ample [12]), however further work remains to address
the complexities of pyrolysis reactions [23].
Simulations were also performed using a surface
kinetics mechanism initially developed for vapour de-
position [26] but modified with improved reaction
rates and combined with the CRECK mechanism for
gas phase kinetics [27]. The mechanism is vali-
dated with pyrolysis experiments in perfectly stirred
reactors (PSR) and PFRs for a range of conditions
[27, 26]. Simulations using the combined mechanism
here referred to as CRECK-Surf were performed with
a series of 1D PSRs in the OpenSmoke++framework
[24]. Due to the stiffness of the kinetic mechanism
at high temperatures, direct PFR solutions were not
obtainable. Surfaces in each PSR were initialized us-
ing equal distributions of zig-zag and armchair sites
as suggested in [27] and [26]. Surface site density
was kept constant at 1.33x10−9 mol/cm2. To replicate
equivalent PFR results, 15 PSR simulations in total
were linked for each condition and adjusted to match
the surface area of the 15 cut segments in the micro
flow reactor experiment. Calculated surface deposi-
tion rates were scaled by the experiment duration (be-
tween 100 to 1000 ms) to obtain predictions of depo-
sition mass for comparison to experimental measure-
ments.
2.5. Uncertainty analysis
A C-type thermocouple (5% W, 26% Re) was used
for internal wall temperature measurements. Between
1400 and 1800 K, it has maximum reported deviation
of 5 K from ASTM E-230 standard curve. The ther-
mocouple was used for a 5-point calibration of the
emissivity value for the two-color pyrometer between
1300 and 1900 K. Each calibration point tempera-
ture was held for several minutes to establish steady
state conditions between the inner wall temperature
and the thermocouple. Then, the temperature reading
was averaged over 2 minutes to obtain the calibration
point. The calibration points were used to adjust the
assumed emissivity to match the external wall tem-
perature measurement to the thermocouple reading.
The standard accuracy of the pyrometer is±(0.5 %
of reading+2 ◦C) and the repeatability is±0.3 % of
reading. Combined uncertainties for the thermocou-
ple, 5-point calibration, and pyrometer give a temper-
ature measurement uncertainty of±10 K.
For gas species measurement 5 to 14 samples
were collected consecutively in each experimental
run. Representative measurements of collected sam-
ples are shown in Fig. 5a. Leaks between loops are

Razavi et al./Combustion and Flame (2026) 5
0 2 4 6 8 10 12 14 16
−0.08
−0.04
0.00
0.04
0.08
Deviation from mean ( )
Measurement Number
 Zero mean      
 s =    0.037
 
0 2 4 6 8 10 12 14
0.00
0.02
0.04
0.06
0.08
0.10
0.12Mass Fraction
Sample Loop Number
H2
CH4
C2H4
A
B
Fig. 5.A:Representative gas species measurements for a
single experiment run at 1600 K, 7 atm, using the gas sam-
pling system and GC-TCD. Measurements show the vari-
ance between each sampling loop. Samples rejected due to
leakage shown in grey.B:Deviation from the mean of car-
bon yield measurements from multiple experiment runs at
varying conditions. Mean values shifted to zero for all con-
ditions. Standard deviation on carbon yield measurements
found as s=0.037.
minimal and neglected as all samples are repetitions.
Leaks out of some loops are apparent in high diffu-
sivity species such as hydrogen, seen in loop 9, 11,
13, and 14 in Fig. 5a. All the gas species measure-
ments from these loops are rejected from the final re-
porting including heavier species which show no leak-
age. For PAH measurements, the first few samples
are rejected due to skewed readings owing to adsorp-
tion along the sampling path. Once saturated, sub-
sequent loops found more consistent measurements.
The accepted measurements are averaged to obtain
gas species mass fractions at one condition. This pro-
cess is repeated 1 to 3 times for each condition. Sin-
gle run repeatability (between different loops) is well
within the uncertainty of the GC-TCD measurement.
Inter run repeatability (measurements from indepen-
dent experimental runs) can show variations of about
5 %, owing to variability in the reactor temperature
and the thermal conditions of the gas sampling probe
and sampling lines. The reported measurements are
averages of between 5 to 10 loops and 1 to 3 repeti-
tions of each condition, and show an average variation
of 7 %. The estimated instrument uncertainty includ-
ing the GC-TCD calibration mixtures and detector re-
sponse is 5 %. The combined standard uncertainty for
each measured gas mass fraction is 9 %.
For carbon yield, experiments were repeated 1 to
3 times for each condition and the measured yields
were averaged. The yields were corrected for baseline
carbon determined through blank measurements. The
deviation of yield from the zero centered mean at each
condition is shown in Figure 5b. The standard devia-
tion is s=0.037, and is mostly attributed to variations
in reactor temperature between each repetition. The
blank value varies between 60 to 160µg C. The inlet
carbon mass fraction has±1 % error from the mass
flow controllers supplying the CH4 and Ar. Finally up
to 5 % of each cut segment from the reactor walls may
be lost due to the blade thickness. Combining these
error sources gives the uncertainty for carbon yield as
+(6 %+0.042),−(1 %+0.037).
3. Results and Discussion
Methane pyrolysis reactions were studied at a
range of conditions (see Table 1). The selected range
accommodates sufficient gas product volumes for GC-
MS and GC-TCD detection, while limiting solid prod-
uct mass within the limits of carbon burnoffmeasure-
ment. The residence time was kept constant at 60 ms
for all conditions. Measurements of total solid car-
bon mass were normalized by the carbon mass in the
injection volume to give the carbon yield,CY, as
CY=m c/(YCViρi)=Y s/Yc,i,(1)
wherem c is the measured carbon mass,Y C the carbon
mass fraction in the inlet mixture, andV iρi the total
mass of the injected volume. The solid mass fraction
(Ys) and carbon mass fraction at the inlet (Y c,i) can be
similarly used when available from simulation results.
Measured and simulated carbon yields from methane
pyrolysis are shown in Fig. 6.
Table 1.
Range of experimental conditions
Parameter Value Units
Fuel mass fraction in Ar 50 %
Temperature 1400, 1600, 1800 K
Pressure 1, 4, 7, 10 bar
Residence time 60 ms
Major gas species in the products are unreacted
CH4 and H 2. The Ar mass fraction in the injection
mixture was used as an internal standard to calculate
the mass fraction of products independent of the level
of dilution with N2, which was used both as the reactor
carrier gas and for sample gas transfer. The measured
and simulated normalized mass fractions of unreacted
CH4 and H2 are shown in Figs. 7 and 8, respectively.
The measured values correspond to the time-averaged
composition over the entire experimental duration, as
the sampled volume is comparable to the injected vol-
ume. Considering the short residence time of 60 ms
and the experimental duration of about 1 second, the

6 Razavi et al./Combustion and Flame (2026)
0 2 4 6 8 10
0.0
0.2
0.4
0.6
0.8
1.0Carbon Yield ( )
Pressure (bar)
 1800 K  CRECK 1800 K
 1600 K  CRECK-S 1800 K
 1400 K  CRECK 1600 K
 CRECK-S 1600 K
Fig. 6. Carbon yield from pyrolysis of CH4, 60 ms residence
time, 50% mass fraction in Ar. Simulations with CRECK
and CRECK-Surf mechanism. Error bars are typical.
0 2 4 6 8 10
0.0
0.2
0.4
0.6
0.8
0.98
0.99
1.00 Unreacted ( )
Pressure (bar)
  CRECK  CRECK-S
  CRECK  CRECK-S
  CRECK  CRECK-S
Fig. 7. Normalized fraction of unreacted CH 4 from pyroly-
sis reactions, 60 ms residence time, 50% mass fraction in Ar.
Simulations with CRECK and CRECK-Surf mechanism. Er-
ror bars are typical.
measured composition is near to the steady state value
and is comparable to simulation results.
3.1. Reaction mass balance
The total mass balance of the reaction is plotted as
a cumulative mass fraction of the measured species,
shown in Fig. 9. Measured but unquantified species
include C 2 and PAH up to C 12. These are estimated
to account for 5 to 10 % of the mass fraction and
are included as "other" species, Fig. 9. The maxi-
mum possible carbon and H2 mass fractions are calcu-
lated based on complete conversion of the consumed
0 2 4 6 8 10
0.000
0.003
0.006
0.2
0.4
0.6
0.8
1.0 Yield ( )
Pressure (bar)
  CRECK  CRECK-S
  CRECK  CRECK-S
  CRECK  CRECK-S
Fig. 8. H 2 yield from pyrolysis of CH 4, 60 ms residence
time, 50% mass fraction in Ar. Simulations with CRECK
and CRECK-Surf mechanism. Error bars are typical.
1 bar, 1800 K
4 bar, 1800 K
7 bar, 1800 K
10 bar, 1800 K
1 bar, 1600 K
4 bar, 1600 K
7 bar, 1600 K
10 bar, 1600 K
1 bar, 1400 K
4 bar, 1400 K
7 bar, 1400 K
10 bar, 1400 K
0.0
0.2
0.4
0.6
0.8
1.0Cumulative Mass Fraction H
2  Max H 2  Other/Loss  Max C  C  CH 4
Fig. 9. Cumulative mass fraction of reaction products. Aver-
age mass recovery for quantified species was 80 % (+7 %,
−5 %).
methane. The difference between the measured car-
bon and maximum carbon indicates how much of the
carbon mass remains in the intermediates or is lost in
the measurement process. The same applies to H 2.
Across all experiment conditions the average mass re-
covery was 80% (+7 %,−5 %) for calibrated species
and about 90% including detected but unquantified
species.
3.2. Pressure and temperature dependence
The carbon yield was found to decrease with in-
creasing pressure across the range of temperatures
investigated, Fig. 6. The trend of pressure de-
pendence was evaluated by fitting the data to a

Razavi et al./Combustion and Flame (2026) 7
power law where the exponent of pressure isn=
log(Y/Yatm)/log(P/Patm). The 1400 and 1800 K con-
ditions show a dependence ofn=−0.28 andn=
−0.13 respectively, while the 1600 K condition shows
a stronger pressure dependence withn=−0.05. The
reduction of carbon yield with pressure is consistent
with other flow reactor studies, which attribute the
trend to the suppression of chain branching reactions
governing CH 4 decomposition [16]. However, the
simulated carbon yield increases with increasing pres-
sure at all temperatures. At 1800 K the predicted car-
bon yield values are in agreement with the experiment
measurements, but at 1600 and 1400 K they are lower
than the measurements. This strong sensitivity of car-
bon yield to temperature was not observed in the ex-
periments. The simulations display higher pressure
sensitivity at 1600 K, similar to the experiment find-
ings.
Carbon yield decreasing with pressure is in stark
contrast with LDFs, which find maximum soot yield
scaling withP n wheren≃2 [28]. While carbon for-
mation from pyrolysis and soot formation from com-
bustion follow similar mechanisms, the absence of ox-
idative species in pyrolysis may limit the available
pathways for radical formation and surface growth.
In numerical simulations of soot formation in a LDF,
the soot formation pressure dependence shows sen-
sitivity to both oxidative radicals and surface growth
mechanisms [29]. Normalized soot production rates
in CDFs also find strong pressure dependencies of
aboutn≃1.7 [30]. Numerical analysis of the forma-
tion processes in CDFs suggests the pressure depen-
dence has strong sensitivity to the precursor compo-
sition, which itself depends on temperature variations
[31]. The absence of oxidative species and the con-
stant reaction temperature are key differences between
PFR and LDF/CDF which may explain the observed
discrepancy in carbon and soot yield, however further
investigation is needed to address this disagreement.
The unreacted methane fraction was found to in-
crease with increasing pressure, Fig. 7. Like the
carbon yield, this trend is also attributed to suppres-
sion of the chain branching reactions by pressure [16],
which for the low residence time considered in this
study would result in lower fuel consumption and thus
higher fractions of unreacted CH4 remaining. The de-
crease in the methane decomposition and suppression
of the chain branching reactions may subsequently
inhibit radical formation and growth of intermediate
species involved in H 2 formation. This may explain
the reduction of H2 yields with increasing pressure ob-
served in the current study, Fig. 8.
The pressure dependence of unreacted CH 4 is pre-
dicted well at 1800 K by all the simulations. However
at lower temperatures they show reducing CH 4 frac-
tions with increasing pressure, Fig. 7. The reduction
in H2 yield with increasing pressure is also captured
well at 1800 K, but at 1600 and 1400 K the simu-
lated H2 yield shows increasing yields with pressure,
Fig. 8. The pressure dependence order of H2 yield and
unreacted CH4 was found to be similar at all the tem-
perature conditions. The order was averaged between
the temperatures and was found to ben=−0.25 and
n=0.78 for H 2 yield and unreacted CH4, respectively.
The simulations predict strong temperature sensitivity
of carbon yield, H2 yield, and unreacted CH4 fraction
at the pressures investigated. They predict a signifi-
cant reduction in reactant conversion at 1600 K while
the experiments show a slight reduction beginning at
1400 K. This discrepancy in the onset temperature
may be explained by low global reaction rates at the
lower temperatures.
3.3. Heterogeneous pyrolysis effects
Representative carbon burnoffmeasurements of
surface deposition profiles in the micro flow reactor
found significant deposition mass along the reactor
length, shown for varying pressures at 1600 K in Fig.
10 and for varying temperatures at 4 bar in Fig. 11.
The measurements are discrete measurements of 20
mm length segments of the reactor and approximate
the true deposition profile. The highest deposition
mass for most conditions was found near the reactor
inlet and decreased steadily towards the center of the
reactor. A slight increase in deposition mass was ob-
served near the exit for some conditions (see Fig. 10
at 1 bar). This effect may be partially due to devia-
tions from the nominal temperature in the temperature
profile, which decreased slightly near the ends of the
reactor and may induce a thermophoretic force on the
mobile carbon particles. It may also be attributable to
the kinetics of a secondary reaction regime observed
in some shock tube pyrolysis experiments [32, 33].
Increasing reaction pressure was found to suppress the
deposition mass across the reactor length, while the
position of the maximum deposition mass did not shift
significantly. Gas phase carbon and surface deposition
measurements are shown separately in Fig. 12. The
suppression of surface deposition by increasing pres-
sure is consistent across all temperatures, and may be
due to decreased diffusivity of the gas phase carbon at
higher pressures. This is also suggested through mod-
elling studies which found particle diffusion to signif-
icantly affect surface deposition rates [34].
Simulation results using the CRECK-Surf mech-
anism show similar trends to the experimental mea-
surements, Fig. 10. The simulations predict high
deposition masses at the reactor inlet which steadily
decrease along the reactor length as the reaction pro-
gresses. They also replicate the suppression of de-
position mass with increasing pressure, showing the
strongest suppression between 1 and 4 bar in agree-
ment with the experimental findings. However the
simulated deposition mass is lower than the measured
mass by a factor of about 100 for the range of pres-
sures at 1600 K.
Increasing temperatures from 1400 to 1800 K in-
creased the deposition mass and shifted the position

8 Razavi et al./Combustion and Flame (2026)
0 5 10 15 20 25 30
0
50
100
150
200
250
0.0
0.5
1.0
1.5
2.0
Carbon Deposition ( )
Axial Position (cm)
Fig. 10. Axial profiles of solid carbon deposition in micro
flow reactor at 1600 K and varying pressures. Reactor inlet
is at 0 cm. Experimental measurements shown (left axis).
Error bars are typical. Simulated profiles using the CRECK-
Surf mechanism with chained PSR shown (right axis).
of maximum deposition. At 1800 K, maximum de-
position mass was found at the reactor inlet while at
1400 K it was found at about 7 cm past the reactor in-
let and was lower. This reduction in deposition mass
and shift in the peak location was observed despite the
global yields at 4 bar remaining about constant with
decreasing temperature. Furthermore at 1 bar the sur-
face phase carbon deposition mass decreased with de-
creasing temperatures while the gas phase carbon in-
creased. Since these trends are opposite and not con-
sistent across all pressures, the reduction in surface
deposition cannot be explained solely by gas phase
kinetics and reflects the sensitivity of the surface de-
position rates to temperature.
Simulations of the deposition profile capture the
initial peak well at 1800 K, shown in Fig. 10. How-
ever for 1600 and 1400 K, they predict no shift in peak
location. The simulated surface deposition predicts
stronger sensitivity to temperature than pressure, pre-
dicting a significant reduction with reducing tempera-
ture. This is similar to the results of the gas phase ki-
netics models which show low reaction yields at 1400
K. This finding may indicate that the gas phase reac-
tions in the CRECK-Surf mechanism are not signif-
icantly influenced by the surface kinetics at the cur-
rent conditions. This is also in agreement with the
experimental measurements which found that compa-
rable carbon yields at different temperatures can have
varying amounts of surface carbon deposition, Fig.
12. These findings suggest the importance of hetero-
geneous pyrolysis effects on the global yield may be
challenged in the micro flow reactor experiment par-
ticularly at high pressures where the relative contribu-
tion of surface carbon to global yields is reduced.
0 5 10 15 20 25 30
0
50
100
150
200
250
0
1
2
3
4
5
Carbon Deposition ( )
Axial Position (cm)
Fig. 11. Axial profiles of solid carbon deposition in micro
flow reactor at 4 bar and varying temperatures. Reactor inlet
is at 0 cm. Experimental measurements shown (left axis).
Error bars are typical. Simulated profiles using the CRECK-
Surf mechanism with chained PSR shown (right axis).
0 2 4 6 8 10
0.0
0.5
1.0
1.5
2.0
2.5  1800 K
 1600 K
 1400 K
Carbon Mass (mg C)
Pressure (bar)
 1800 K
 1600 K
 1400 K
Gas Phase
Surface Phase
Fig. 12. Total gas phase (homogeneous) and surface phase
(heterogeneous) carbon measurements from CH 4 pyrolysis
at 60 ms residence time. Sum of values corresponds to global
carbon mass. Values are corrected to 4.2 mg injected carbon
for consistency between conditions.
The simulated deposition mass at 4 bar is lower
than the experiment measurements by a factor of
about 50 and 100 at 1800 K and 1600 K respectively.
The lower surface deposition predicted by the simula-
tions may be due to the residence time of the experi-
ments in this study being 60 ms, significantly shorter
compared to the validation experiments considered in
[27] which used residence times from 0.5 to 4 s. A
heuristic assessment of the surface reactions in the
CRECK-Surf mechanism found the majority involve

Razavi et al./Combustion and Flame (2026) 9
reactions with short chain C 2 to C4 species and some
aromatics. The low residence times may limit forma-
tion of these key species in the simulations. Further-
more, the inclusion of heavier PAH may be key in cap-
turing the deposition phenomenon. Detailed micro-
scopic investigation of the pyrolytic deposits in mi-
crowave formed carbon identified the depositions to
be a mixture of graphitic and amorphous segments
with a liquid-like film originating from PAH [35].
This composition provides exposed active sites and is
suggested to catalyze pyrolysis [23]. This would both
reduce the onset temperature and accelerate global re-
action rates compared to the gas phase kinetics, possi-
bly explaining the high surface depositions measured
in the current work and the temperature sensitivity
found in the simulations which do not consider the
development of the depositing surface. Analysis of
the relevant C2 to C4 and PAH species could provide
additional insight to address the discrepancy.
Investigations in a packed flow reactor at 1400
K and atmospheric pressure found the proportion of
deposited carbon is increased at higher surface-to-
volume (S/V) ratios [36]. They also found morpho-
logical differences with heavy deposition owing to
higher S/V , however noted that temperature plays a
more critical role. High temperatures resulted in less
amorphous carbon and more graphitic carbon [36].
Although the phenomenon governing the proportion
of deposition mass, its morphology, development of
active surface sites, and subsequent influence on the
gas phase kinetics are difficult to isolate in such ex-
periments, the complex interplay remains an area for
investigation. Understanding the relative significance
of S/V ratio and residence times can provide useful
insights into the sensitivity of the observed trends to
these surface effects.
3.3.1. Extended S/V ratios and residence times
The primary experiments in the current study (60
ms residence time, S/V=12.6 cm −1) were repeated at
key conditions with a reduced diameter reactor (S/V=
25.2 cm−1) or increased residence time (600 ms). The
experiments with higher S/V ratio were performed at
1800 K while experiments with higher residence time
were performed at both 1800 K and 1600 K. Carbon
yield measurements for the additional conditions are
shown overlaid with the corresponding primary con-
ditions in Fig. 13. Separated measurements of gas
phase and surface phase carbon mass are also shown.
At 1800 K and 4 bar increasing the residence time
increased the carbon yield owing to an increase in
surface phase carbon while the gas phase carbon re-
mained unchanged. For the 10 bar condition increas-
ing the residence time at 1600 K had no discernible
impact on the carbon yields, while at 1800 K higher
residence times found much lower carbon yields. This
result remains unexplained and suggests an appar-
ent reverse mechanism for pyrolysis and deposition at
longer residence times and high temperatures. These
findings also suggest that the equilibrium condition is
not readily reached for the 60 ms residence time and
further gas and surface reactions are ongoing. The ob-
served trends and sensitivities are thus representative
of carbon formation and deposition kinetics.
Increasing the S/V ratio at 1800 K and 1 and 4 bar
increased the surface phase carbon mass and reduced
the gas phase carbon mass. As a result the total car-
bon yields increased by about 16 and 7 % for 1 and 4
bar respectively. The proportion of surface phase car-
bon also increased from 70 % to 79 % at 1 bar and
from 39 % to 55 % at 4 bar. Considering that the S/V
of the reactor was doubled, the increase in the propor-
tion of surface deposition was mild. Furthermore the
pressure dependence of both the gas phase and sur-
face phase measurements are unchanged. As such the
increase in reactor S/V at the conditions in this study
had a weak effect on the yields of heterogeneous and
homogeneous carbon. Detailed investigation of its ef-
fect on the deposition morphology remains a subject
of future work.
3.4. PAH Measurements
GC-MS measurements of the sampled products
found a range of PAH species in the gas phase, Fig.
14. The results are reported as averages of repeated
gas sample measurements and are normalized for in-
jection volume using the internal standard, Ar (mea-
sured simultaneously for the same injection using GC-
TCD). The adjusted values are reported as peak area
and have an average variation of about 18%; Quantita-
tive calibration for the detected PAH species is not re-
ported in this work. The most abundant species found
were C6H6, C7H8, C8H8, and C10H8 respectively which
were detected in all temperature and pressure condi-
tions, Fig. 14a. Between 1 bar and 4 bar, major PAH
species amounts increased significantly. The largest
increase between 1 and 4 bar occurred at 1400 K. For
increasing pressures above 4 bar, the PAH amounts
increased but with lower sensitivity to pressure, Fig.
14a. However, the sensitivity of the PAH species to
temperature was found to be significant. At 1400
K the highest amounts of PAH were detected. The
PAH amounts reduced sharply as the temperature in-
creased. The high sensitivity to temperature is consis-
tent for the four major PAH species shown, but was
found to be most significant for C6H6.
Higher temperatures were found to suppress both
the amount and breadth of PAH species detected, Fig.
14b. Fewer types of PAH species were detected and at
lower amounts at 1800 K as compared to the 1400 K
condition. Notably, the lower temperatures also found
greater number of PAH with the same number of C
atoms but differing numbers of H atoms. The reduc-
tion of PAH types and amounts at higher temperatures
combined with the increase in amounts at higher pres-
sures may indicate the dominance of chain branch-
ing PAH breakup reactions. Such reactions may be
suppressed by increasing pressure and accelerated by

10 Razavi et al./Combustion and Flame (2026)
0 2 4 6 8 10
0.0
0.2
0.4
0.6
0.8
1.0Carbon Yield ( )
Pressure (bar)
 1800 K
 1800 K, High S/V
 1800 K, 600 ms
 1600 K
 1600 K, 600 ms
0 2 4 6 8 10
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5Carbon Mass, Surface Phase (mg C)
Pressure (bar)
0 2 4 6 8 10
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5Carbon Mass, Gas Phase (mg C)
Pressure (bar)A
 B C
Fig. 13. Carbon yields (A), gas phase carbon (B), and surface phase carbon (C) measurements for conditions with increased S/V
and residence time. Also shown is corresponding nominal conditions. Error shown as shading for clarity.
increasing temperature, potentially in agreement with
the observed trends. However, the assessment of the
dominant reactions is inconclusive without more de-
tailed PAH species measurements.
An analysis of the measured PAH trends from the
simulation results found PAH mass fractions depen-
dence on pressure shifted at different temperatures.
The highest PAH concentrations were predicted at
1600 K and 1 bar and decreased with increasing pres-
sure. At 1400 K and 1800 K, lower PAH concentra-
tions were predicted and they increased with pressure.
While the experiment trend is not replicated, a de-
tailed analysis of the reactions can provide additional
insight.
3.5. Rate of Production Analysis
Rate of production analysis (ROPA) of the most ac-
tive reactions involved in the formation and consump-
tion of benzene (C6H6) was performed at 1400, 1600,
and 1800 K and 4 bar for the gas phase CRECK mech-
anism, Fig. 15. The top 7 formation or consump-
tion reactions are reported. Benzene (C 6H6) repre-
sents the most simple PAH species containing a single
aromatic ring and was found to represent the trends of
larger PAH well in both experiment data and simula-
tion predictions. The ROPA was performed for each
simulation condition as a global rate analysis. The re-
sults found C6H6 formation at 1400 K was supported
mainly by short chain combination reactions involv-
ing C3 species, Fig. 15a. At this temperature, net for-
mation rates of C 6H6 were positive and PAH concen-
trations were increasing. This prediction supports the
low product yields predicted by the simulations, indi-
cating the reaction is in the early stages. At 1600 K,
C6H6 reactions were dominated by H-abstraction and
addition reactions through the methyl and hydrogen
radicals, Fig. 15b. The predicted reaction rates were
0
30
60
90
0
2
4
0
1
2
0 2 4 6 8 10
0
10
20
C6H6
C7H8
C8H8
 1800 K
 1600 K
 1400 K
Pressure (bar)
C10H8
1
4
7
10
10E4
10E6
10E8
Peak Area
1
4
7
10Pressure (bar)
1800 K
1600 K
40 80 120 160
1
4
7
10
Species Mass (AU)
A B
Fig. 14. GC-MS measurements of PAH from CH 4 pyrolysis
in a micro flow reactor.A:Pressure and temperature depen-
dence of average peak area in the 4 most abundant species
detected (C6H6, C7H8, C8H8, and C10H8). Error bars shown
for C6H6 represent average variation and are typical.B:Pres-
sure and temperature dependence of average peak areas mea-
sured for complete range of detected PAH species.
found to be significantly higher than at 1400 K. How-
ever the net production rate of C 6H6 after 60 ms was
negative, indicating consumption of C6H6 in the prod-
uct mixture. At the highest temperature of 1800 K,
the dominant reactions were found to be the forward
and reverse reactions of the H-abstraction reaction for
C6H6 with the H radical (H+C 6H6→H 2 +C 6H5),
Fig. 15c. The forward and backward reaction rates
dominated other reactions involved in C 6H6 forma-
tion, indicating that the global reaction is approaching

Razavi et al./Combustion and Flame (2026) 11
a b c1400 K 1600 K 1800 K
Fig. 15. Consumption and production rates of C 6H6 given by elementary reactions in order of decreasing contribution. Analysis
is based on the full CRECK mechanism (S1) in gas phase. Top 7 reactions are shown for global rate of C 6H6 production from
CH4 pyrolysis at 4 bar anda:1400 K,b:1600 K, andc:1800 K.
partial equilibrium for the H-abstraction reaction. The
net production rate was negative, but the consumption
of C6H6 at about−5x10−5 kmol/m3s was lower than at
the 1600 K condition by a factor of 100.
In summary, the simulations at 4 bar predict
low formation rates of C 6H6 at 1400 K, governed
by short chain combination reactions. At 1600
K, H-abstraction reactions increased, and at 1800
K the system approached partial equilibrium for
H+C 6H6→H 2 +C 6H5 and near steady state for
C6H6 production rate. Considering PAH as precursors
to carbon formation, the low production rates of C6H6
at 1400 K and the approach towards partial equilib-
rium at 1600 K may be inhibiting the formation of
sufficient concentrations of PAH to generate high car-
bon yields. This may partially explain the predictions
of low carbon yield compared to measurements.
The dominant formation and consumption reac-
tions in the CRECK-Surf mechanism were analysed
for carbon deposition, Fig. 16. This analysis was per-
formed for the global reactions involving the carbon
bulk species C(B) in a single stage of the PSR simu-
lation. The stage and condition were selected to in-
clude both high deposition rates and high PAH forma-
tion rates in the gas phase. This coincides with ear-
lier stages of the PFR simulation with total residence
times of about 10 ms. The selected condition was
1600 K and 4 bar. The dominant reactions in the sur-
face deposition of carbon were found to be reactions
involving the restructuring of the interface layer (first
and third reaction in Fig. 16), which produces a hy-
drogen radical in the process. The second most domi-
nant reaction was the direct deposition of a single car-
bon atom from the base CH 4 fuel. Interestingly PAH
species were not found to significantly contribute to
the carbon deposition rate in a single step at the simu-
lated conditions and instead contributed through multi
step elementary reactions within surface species at the
interface layer.
The findings indicate that the contribution of the
heterogeneous reactions to the overall carbon yield
predicted by the simulations is mainly in the creation
of gas phase radicals of methyl or hydrogen. The in-
Fig. 16. Consumption and production rates of dominant re-
actions involving bulk phase carbon, C(B), in a PSR simu-
lation performed at 10 ms of the PFR simulation using the
CRECK-Surf mechanism for pyrolysis at 1600 K and 4 bar.
teractions of the surface with short chain hydrocar-
bons or aromatics may be limited at the conditions
in this study. The earlier ROPA indicated PAH mass
fractions in the gas phase are dominated by elemen-
tary reactions that share the same key radicals. De-
viations in the predictions of PAH reactions and their
temperature and pressure sensitivity can thus lead to
changes in the surface deposition mass through com-
petition with the dominant radicals, namely methyl,
short chain hydrocarbons (C 2 to C 3) and H atom. It
should be noted that simulations were also performed
with non-constant surface site density which predicted
a sharp increase in the surface site density and an over
prediction of the deposition mass. While demonstrat-
ing the sensitivity of the system to site density, this
may not be representative of the true site density of a
graphitic carbon surface [27]. The complexity of the
deposition structure and morphology observed in sev-
eral studies [35, 36, 23] suggests the need for more
detailed treatment of the type of active sites and their
surface density.

12 Razavi et al./Combustion and Flame (2026)
3.6. Assessment of the discrepancies
The simulations performed with both gas and
gas/surface kinetics showed low pyrolysis yields at
1400 and 1600 K. Particularly at 1400 K, the sim-
ulations found near zero conversions of fuel to car-
bon. Measurements of the unreacted methane frac-
tion found that fuel consumption is significant at 1400
K. The discrepancy can possibly be attributed to low
reaction rates in the fuel decomposition reactions at
low temperatures. The increase in unreacted fuel
with increasing pressure at 1800 K found in both
simulations and experiments was not observed in the
simulations at 1400 K where the unreacted methane
fraction was found to decrease with pressure. This
may indicate that chain branching reactions such as
CH4→CH 3 +H which are prone to suppression at
higher pressures may be under represented at 1400 K.
Simultaneously, analysis of the PAH reaction path-
ways from the simulations predicts a rapid approach
to partial equilibrium for dominant PAH reactions
involving H-abstraction from methyl and hydrogen
atoms. At 1400 K this process was found to consume
short hydrocarbon radicals in the C2 to C3 range. This
may compete with radicals required for the decompo-
sition of the fuel which may further contribute to the
predictions of low fuel decomposition at 1400 K. The
increase in methane decomposition reaction rates at
1600 K would provide additional radicals for the PAH
growth process and may explain the higher predicted
yields and mass fraction of PAH species, although still
lower than the measured yields. At this intermediate
temperature the simulations predict high PAH mass
fractions compared to the 1400 and 1800 K condi-
tions, while the experiment predicts high PAH mass
fractions at 1400 K. Lower rates of PAH consumption
reactions at 1600 K may explain the prediction of high
PAH mass fractions and the low carbon and hydrogen
yields compared to measurements from the global py-
rolysis reaction.
The simulations with surface chemistry found that
its inclusion has a minor effect on the gas composi-
tion and does not significantly contribute to the yields
of pyrolysis products. This is also supported by the
experiment measurements which found similar total
carbon yields can occur with varying amounts of sur-
face deposition. Analysis of the dominant reactions
suggests that surface deposition rate at low residence
times is dominated by availability of methyl radicals,
which also directly competes with the fuel decompo-
sition reactions. However, the simulations at 1800 K
also predicted lower deposition mass than the mea-
surements, despite the apparent availability of inter-
mediate species and high product yields. This may
indicate that the deposition reaction rates at high tem-
peratures or the assumptions of constant surface site
density could be revised.
The mechanisms used have correctly replicated
many challenging flame and flow reactor experiments
used in their development [12, 27]. Based on the mea-
surements and simulations analysis of pyrolysis at the
conditions in the current study they may benefit from
accelerated fuel decomposition reactions at 1400 K,
accelerated PAH consumption reactions at 1600 K,
and increased surface deposition rates at all temper-
atures. Inclusion of more detailed processes such as
particle diffusion, adsorption kinetics, and endother-
mic heat loss may also be beneficial to account for all
the gas phase and surface deposition processes, fur-
ther isolating the effects of the kinetics from the exper-
iment structure and potentially addressing the discrep-
ancies with pressure dependencies observed in con-
ventional flames.
4. Conclusion
High temperature and high pressure methane py-
rolysis reactions were studied in a micro flow reac-
tor from 1 to 10 bar and 1400 to 1800 K. The yields
of carbon in the gas phase, carbon in surface depo-
sitions on the reactor walls, hydrogen, and unreacted
methane fraction were quantified. The measurements
found reaction yields decreased with increasing pres-
sure at all temperatures. This is attributed to the sup-
pression of chain branching reactions governing the
fuel decomposition.
Qualitative analysis of the detected PAH species
found PAH amounts were highest at low temperatures
and high pressures. Simulations using the CRECK
mechanism with discrete sectional models for track-
ing soot formation and simulations including surface
deposition mechanisms captured the pressure depen-
dence of pyrolysis yields well at 1800 K. At 1400 and
1600 K, the simulations predicted lower yields and
varying pressure dependence.
Analysis of the reaction pathways suggests the
rates of fuel decomposition reactions at 1400 K and
the rates of PAH consumption reactions at 1600 K
may be significant to the global yield. The mea-
sured proportion of heterogeneous carbon reduced at
high pressures. The surface kinetics in the simula-
tion were not found to be a significant contributor
to overall yields. Predictions of surface deposition
mass were strongly linked to the gas phase concen-
trations of methyl and short chain radicals. Improve-
ments to the reaction kinetics for fuel decomposition
and PAH consumption at the conditions of the current
study combined with the use of more detailed simu-
lation frameworks incorporating surface morphology
and diffusive effects may lead to greater insight in py-
rolysis reaction processes in the micro flow reactor.
CrediT authorship contribution statement
Mohammad Reza Razavi: Methodology, investi-
gation, formal analysis, visualization, writing - orig-
inal draft.Ömer Gülder: Conceptualization, re-
sources, methodology, writing - review & editing, su-
pervision.
