---
source_id: "arxiv"
title: "Enhancing hydrogen production in alkaline"
url: "https://arxiv.org/abs/2607.26750"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2607.26750. Abstract: Enhancing hydrogen production in alkaline
electrolyzers by using an ultra-fast kinetics surfactant
D. Fernández-Martíneza,b, G. Martín-Zazoa, A. Rubio-Gonzáleza,b, J. L.
Serrano-Marcosc, J. M. Montaneroa,b, F. J. Perosanzc, E. J. Vegaa,b,∗
aDepto. de Ingeniería Mecánica, Energética y de los Materiales, Universidad de
Extremadura, E-06006 Badajoz, Spain
bInstituto de Computación Científica Avanzada"
---

# Enhancing hydrogen production in alkaline

Enhancing hydrogen production in alkaline
electrolyzers by using an ultra-fast kinetics surfactant
D. Fernández-Martíneza,b, G. Martín-Zazoa, A. Rubio-Gonzáleza,b, J. L.
Serrano-Marcosc, J. M. Montaneroa,b, F. J. Perosanzc, E. J. Vegaa,b,∗
aDepto. de Ingeniería Mecánica, Energética y de los Materiales, Universidad de
Extremadura, E-06006 Badajoz, Spain
bInstituto de Computación Científica Avanzada (ICCAEx), Universidad de Extremadura,
E-06006 Badajoz, Spain
cUnidad de Conversión Electroquímica de Energía-H2 (UCEEH2), Departamento de
Energía CIEMAT, Madrid, Spain
Abstract
We study the effect of surfactant adsorption kinetics on water electrolysis
performance using Surfynol 465, an ultrafast-kinetics surfactant. High-speed
optical diagnostics reveal that Surfynol 465 reduces bubble residence time
by an order of magnitude. Compared to the slower surfactant Triton X-100
and the surfactant-free baseline, it also prevents the growth of large bubbles
(>200µm). We validated these results on an anion-exchange membrane
electrolyzer (AEMEL) test bench. Adding Surfynol 465 to the1M KOH
electrolyte decreases cell overpotential by 140–150 mV. It nearly triples the
current density (from 0.13 to 0.37 A/cm2 at 2 V) and increases average
power by 40% during a week-long test. Furthermore, downstream corrosion
analyses reveal a strong alloy-dependent response. The surfactant reduces
degradation in stainless steel and brass but accelerates corrosion in carbon
steel.
Keywords:
water electrolysis, surfactants, hydrogen bubble dynamic, hydrogen
production rate
∗Corresponding author: E. J. Vega,ejvega@unex.es
arXiv:2607.26750v1  [physics.flu-dyn]  29 Jul 2026

1. Introduction
Water electrolysis powered by renewable energy sources represents a ma-
jor pathway toward clean hydrogen production. Among the available tech-
nologies, alkaline water electrolysis (AWE) and anion exchange membrane
water electrolysis (AEMWE or AEMEL, anion exchange membrane elec-
trolyzer) are highly attractive due to their cost-effectiveness and robustness
[1, 2, 3, 4]. However, their operating efficiency remains limited by transport
phenomena in the electrodes [5]. During operation, the rapid generation of
hydrogen gas produces a dense population of bubbles that adhere to the cat-
alytic surface. This bubble accumulation isolates the electrode from the elec-
trolyte, causing fluctuations in the reaction potential, increasing local ohmic
resistance, and reducing the electrochemically active surface area [6, 7]. Con-
sequently, the development of effective methods to eliminate or reduce these
adverse effects and accelerate detachment is widely recognized as a crucial
step to minimize these energy losses [8, 9].
Strategies toregulate bubble detachmentcan be broadly classified into ac-
tive and passive methods [7, 9]. Active regulation involves introducing exter-
nal energy sources, such as applying ultrasonic fields to induce acoustic flow
[10] or external magnetic fields to trigger magnetic convection [11, 12]. Al-
thougheffective, theseactivestrategiesrequireadditionalequipment, thereby
increasing the cost of the water electrolysis system [9, 13]. In contrast, pas-
sive regulation methods do not require external energy. These primarily focus
on altering the electrode morphology to minimize the contact area between
the electrode and the bubble [8]. However, manufacturing these complex
geometries on an industrial scale remains a challenge. Alternatively, adding
surfactants to the electrolyte solution represents a highly practical and cost-
effective passive strategy to enhance bubble detachment [14, 15, 16].
An adhered bubble becomes unstable and detaches when the forces pro-
moting release, such as buoyancy, inertial force, and pressure force, overcome
the forces preventing detachment. This resistance is primarily driven by the
surface tension force and the Marangoni force resulting from local thermal or
solutal gradients. Mechanically, the liquid-gas surface tensionσdirectly dic-
tates both the capillary anchoring and the strength of the Marangoni stress.
By accumulating at the interface, surfactants lowerσ, weakening these re-
sistive forces and reducing the bubble departure diameter. Surfactants are
conventionally evaluated based on their equilibrium surface tensionσeq, as-
suming a fully developed interfacial layer. Nevertheless, in many dynamic
2

Figure 1: Sketch showing surfactant adsorption during hydrogen bubble nucleation.
processes, the actual speed of surfactant adsorption dictates the effective sur-
face tension during the event, making the evolution of this reduction more
critical than the final equilibrium value [17, 18].
Driven by rapid growth and coalescence, an electrolytic bubble nucleates,
expands, and detaches on characteristic timescales spanning from a few mil-
liseconds down to the sub-millisecond regime [9, 19, 20]. When a bubble
grows this rapidly, a new liquid-gas interface is generated at a rate that may
outpace the transport and adsorption of surfactant molecules from the bulk
solution [21, 22] (Fig. 1). As a result, the local surface tension at the ex-
panding interface changes dynamically over time. This transient behavior is
described by the dynamic surface tension (DST) [23, 24]. If the surfactant
molecules diffuse and adsorb too slowly, the interface could remain depleted
of surfactant during the bubble’s short lifetime [18]. In such a scenario, the
surfactant might fail to assist bubble detachment, regardless of how low its
surface tension is at equilibrium.
Despite its potential relevance, the role of surfactant adsorption kinetics
and dynamic surface tension in water electrolysis remains largely unexplored.
To the best of our knowledge, no prior studies have investigated how the
timescale of surfactant adsorption couples with the rapid expansion of gas
3

bubbles under electrolytic conditions. Whether “ultrafast” surfactants [25]
can noticeably improve bubble detachment in water electrolysis compared to
slower alternatives remains an open question.
This work aims to address this question by establishing a link between
surfactant kinetics and macroscopic electrolyzer performance. To achieve
this, we evaluate the performance of two non-ionic surfactants: Surfynol 465
as an ultrafast candidate and Triton X-100 as a standard, slower alterna-
tive. First, a simple laboratory-scale cell is used to conduct high-speed opti-
cal diagnostics, enabling us to compare bubble detachment dynamics in the
pure electrolyte with those in surfactant-laden solutions. Our experiments
reveal that Surfynol 465 substantially modifies the electrolysis process, yield-
ing clear improvements in bubble residence time and hydrogen production
compared to Triton X-100 and baseline solutions. Second, the performance
of Surfynol 465 is validated under more realistic operating conditions in a
larger-scale AEMEL electrolyzer test bench. These validation tests confirm
a significant reduction in cell overpotential, improved stability, increased en-
ergetic efficiency, and reduced corrosion kinetics compared to the baseline
electrolyte.
The manuscript is organized as follows. The experimental methodology is
described in Secs. 2 and 3. Section 4 shows the high-speed optical diagnostics
using a simple laboratory-scale cell, while the results of the more realistic
AEMEL electrolyzer are shown in Sec. 5. The paper concludes with remarks
in Sec. 6.
2. Materials and methods for high-speed optical diagnostics
2.1. Experimental setup, surfactants and experimental procedure
A simplified AEMEL-type (AWE) electrolyzer model was implemented
using a custom-made methacrylate cell allowing optical access to the pro-
cess. The cell has internal dimensions of 40×40×40 mm and contains ap-
proximately 50 ml of solution. The electrodes were approximately 40 mm
high and 3 mm wide, with an immersion length of about 20 mm, correspond-
ing to an immersion surface area of 60 mm2. They were made of sintered
stainless-steel fiber felt, a porous material characterized by high mechani-
cal, thermal, and corrosion resistance, and a three-dimensional reticulated
structure.
Figure 2 shows the experimental apparatus, consisting of the experimen-
tal cell (A), electrical wiring (B), electrodes (C), a light source (D), a power
4

Figure 2: Experimental setup: cell (A), electrical wiring (B), electrodes (C), light source
(D), power supply (E), high-speed camera (F), adjustable support (G).
supply (E), a high-speed camera (F), and a height-adjustable support (G).
Electrolysis was driven by applying a potential difference between the elec-
trodes using a laboratory power supply. Electrical connections were made
using cables with crocodile clips and standard terminals. Two multimeters
were used to monitor the applied voltage and the electrical current. Partic-
ular care was taken to maintain the cleanliness of all components to ensure
reproducible experimental conditions.
Bubble dynamics were recorded at 125 frames per second with an expo-
sure time of 12.5µs using a high-speed CMOS camera (Photron, F AST-
CAM Mini UX50). The camera was equipped with an optical system con-
sisting of a 1×zoom objective (OPTEM HR) combined with an additional
lenssystem(OPTEM 70 XL)providing3×magnification, resultinginaspa-
tial resolution of 2.315µm per pixel. A dedicated light source provided uni-
form illumination of the observation region. All components were mounted
on an optical table equipped with a pneumatic vibration isolation system
(Thorlabs). Experiments were conducted at an ambient temperature of
approximately 20 ◦C.
The working fluid consisted of ultrapure water (W) (Type III) and potas-
sium hydroxide (KOH) at a concentration of 1 M. The addition of KOH
increases the electrical conductivity of the solution W+KOH, while the use
of ultrapure water minimizes the presence of impurities. For the concen-
5

1 0
- 5
1 0
- 3
1 0
- 1
1 0
1
2 0
4 0
6 0
8 0
W + K O H/S u r f y n o l  4 6 5
W + K O H / T r i t o n  X - 1 0 0
 c( m o l / m
3
)
σ ( m N / m )
 
Figure 3: Surface tensionσas a function of the surfactant volumetric concentrationc
for W+KOH/Triton X-100 and W+KOH/Surfynol 465. The arrows indicate the selected
concentrations.
trations considered, the density and viscosity remain close to those of pure
water. Ultrapure water was supplied by aDirect-Q®3purification system.
Either Triton X-100 or Surfynol 465 was added to the base solution. The
surface tensionσof both surfactants dissolved in the aqueous electrolytic
solution was characterized as a function of the surfactant concentrationc
(Fig.3). From these curves, the critical micelle concentrationccmc was de-
termined to be 0.08 mol/m3 for Triton X-100 and 0.21 mol/m3 for Surfynol
465. A preliminary analysis showed that the effect of Surfynol 465 was max-
imized forc= 0.1mol/m 3. We selected this concentration for the rest of
our analysis. The Triton X-100 concentrationc= 0.038mol/m3 was chosen
to ensure the same equilibrium surface tension of approximately 40 mN/m.
Remarkably, this yields an identical concentration ratioc/ccmc ≈0.48.
Surfynol 465 rapidly adsorbs at the gas–liquid interface and efficiently re-
duces surface tension under dynamic conditions [26]. Its presence is expected
to affect bubble size, coalescence, and adhesion to the electrode surface,
thereby facilitating bubble detachment. In contrast, the adsorption char-
acteristic time of Triton X-100 is significantly longer than that of Surfynol
465. The differences observed in the presence of the two surfactants can be
attributed to their adsorption rates.
To determine the appropriate experimental procedure, the polarization
curve was measured over three consecutive voltage ramps (Fig. 4), with a 1-
minuterestat0.9Vbetweenramps. Oneachramp, thevoltagewasincreased
from 1.3 to 2.7 V in 0.2 V steps every 2 minutes. The results of ramps 2
6

1 . 0 1 . 5 2 . 0 2 . 5 3 . 0
0
2 5
5 0
7 5
1 0 0
R a m p  1
R a m p  2
R a m p  3
V  ( V )
I  (m A)
Figure 4: Polarization curvesI(V)for the solution with Surfynol 465.
and 3 practically overlapped over almost the entire potential range (Fig.
4). This indicates that once ramp 1 was completed, the electrode interface
had reached an adequate state of stabilization and maturation, in which
heterogeneity and material-history effects were eliminated, thereby ensuring
maximum reproducibility in subsequent long-term tests.
In the activation-loss region (V≲2V),Iis very low due to the energy
required to overcome the metal’s initial chemical inertia and activate its cat-
alytic sites. The rate of hydrogen generation is minimal, and the bubbles
do not obstruct the surface. ForV≳2V, the system transitioned to a
quasi-linear behavior (the ohmic-resistance-loss region). In this regime, the
initial chemical barriers have already been overcome, and the current is pri-
marily controlled by the resistance of both the liquid electrolyte and the gas
generated as it passes.
Based on the results above, we followed the following experimental proce-
dure. In each experiment, the solution was first prepared, and new electrodes
were installed. The cell was left at rest for 15 minutes to wet the stainless
steel felt (hydration), followed by a thermal stabilization phase at 1.9 V for 10
minutes and an activation potential ramp from 1.3 V to 2.7 V (ramp 1). The
voltage was then adjusted to a permanent operating value of 2.2 V, marking
the start of the experimental run (t= 0). Six consecutive videos of bubble
dynamics at the lower margins of the cathode (three of each face/side) were
recorded at specific instants over the 48-hour duration of the experiment.
The videos were analyzed using in-house MATLAB code to determine the
bubble-size distribution, the fraction of the electrode surface free of bubbles,
7

and the hydrogen production rate, as explained in the next section.
2.2. Image processing and evaluation metrics
As noted earlier,H2 bubble dynamics were analyzed via high-speed opti-
cal imaging. Dense bubble curtains, coalescence, and overlapping pose signif-
icant challenges to tracking individual bubble trajectories. To address this,
an automated image-processing framework was developed in MATLAB to
characterize the spatial gas occupancy and its collective transport dynamics.
It should be noted that the images analyzed represent two-dimensional pro-
jections of an inherently three-dimensional bubbly flow. Consequently, the
extracted metrics are not absolute physical quantities. Instead, they serve as
relative indices for comparative analysis between different electrolytes.
The primary objective of the algorithm is to decouple the stagnant gas
fraction from the ascending one. This physical separation is achieved by
evaluating the temporal persistence of the gas phase close to the electrode.
The algorithm applies a moving time window centered on each frame. Pixels
exhibiting high local occupancy fraction within this window are classified as
persistent, stagnant gas.
The decoupling of the stagnant gas fraction from the ascending one is
obtained by the generated binary masks (Fig. 5a), which isolate the total
(St), stagnant (Ss), and ascending (Sa) gas surfaces near the electrode wall.
The algorithm accuracy is demonstrated by tracking these projected surface
areas across each framekof the sequence (Fig. 5b). While the total gas area
seriesS t(k)reflects the continuous accumulation and intermittent detach-
ment of large structures, the ascending gas seriesSa(k)exhibits remarkably
stationary behavior.
Once the areasS t(k)andS a(k)have been calculated, we compute the
ratio between the mean ascending gas area and the mean total gas area
(free-wall percentageZ) as
Z= Sa
St
×100(1)
where Sa =N −1 PNk=1 Sa(k)and St =N −1 PNk=1 St(k), andNis the number
of frames considered.
Now, we consider the ascending gas fraction to determine the “bubble
curtain’s vertical velocity”. To do this, the image is divided intoMhorizontal
windows, 192 pixels in height. For each windowi, the two-dimensional gas
8

Original
k =1454
(a) (b)
St Ss Sa
Figure 5: (a) Binary masks identifying the totalSt, stagnantS s, and ascendingS a gas
surfaces near the electrode wall at framek= 1454. (b) Surface areaSas a function of
the frame numberk. The vertical dashed line indicates the instant corresponding to the
masks shown in (a).
distribution is reduced to a one-dimensional vertical profile by horizontally
averaging the binary values (1 for gas, 0 for liquid) of the ascending gas mask.
As in Particle Image Velocimetry (PIV), theith window vertical velocityvi
is determined by cross-correlating these profiles across different time steps
[27]. To ensure statistical robustness, the local velocity is filtered using the
median over multiple time intervals. Finally, the bubble curtain’s vertical
velocityv b is calculated as
vb = 1M
MX
i=1
vi,(2)
The gas evacuation efficiency is evaluated through the hydrogen produc-
tion rate index
iQ = Sa ·v b,(3)
and the mean bubble residence time
tr = Ss
iQ
,(4)
where Ss =N −1 PNk=1 Ss(k). We evaluated the energetic efficiency of the
electrochemical process by the index
iE = I·ViQ .(5)
9

Finally, we also developed a routine to isolate individual bubble contours and
calculate the bubble size distribution across the experiments.
3. Materials and methods for the AEMEL electrolyzer experiments
Electrochemical evaluation was performed using a single cell Anion Ex-
change Membrane Electrolysis (AEMEL) system (Fig. 6-above) configured
in a zero gap architecture with a dry cathode concept and circular geometry
on both the anode and cathode sides, providing a geometric active area of
63.6 cm2. The cell (A) incorporated a commercial anion exchange membrane
(Fumasep®), compressed symmetrically between two porous transport lay-
ers: a stainless steel mesh (around 0.3 mm in thickness) acting as the gas
diffusion layer (GDL), and a nickel foam (3 mm in thickness) serving as the
porous transport layer (PTL). No catalyst layers were employed in any of
the experiments. Stainless steel meshes were used directly in contact with
the membrane, representing a fully catalyst-free configuration.
The electrolyte consisted of 1 M KOH and was continuously recirculated
using a chemically resistant positive-displacement pump to ensure uniform
hydration and temperature distribution across the membrane–electrode as-
sembly. The power source (B) operated in potentiostatic mode following a
predefined activation and stabilization protocol: (i) 24 hours of electrolyte
circulation for membrane hydration and homogenization; (ii) 7 days of base-
line operation under fixed voltage control; (iii) and sequential potentiostatic
sweeps (I-Vcurves) performed at the beginning, midpoint, and end of the
test campaign, using a ramp rate of 0.1 V/min to track the evolution of
cell performance. We conducted experiments with the tank (C) filled with
W+KOH and W+KOH/Surfynol 465.
In addition, material degradation under alkaline conditions was quanti-
fied using downstream electrochemical corrosion probes (D) installed on the
anodic outlet line (Fig. 6-below). Each probe consisted of a metallic rod
representative of industrially relevant alloys:
- Cu based alloy: Muntz metal (Cu–Zn–Sn), typical in brazing and in-
dustrial fittings.
- Fe based alloy: A106 carbon steel (F e >98%, C≈0.3%, M n≈0.3−
1%), representative of high pressure piping.
10

C
D
BA
ZONE 1
Figure 6: (Above) Experimental setup for the AEMEL electrolyzer: single cell (A), power
source (B), tank (C), probes (D). (Below) Scheme of the electrochemical corrosion testing
bench with probes of several alloys for online corrosion/water contamination diagnostic.
11

- Stainlesssteel: 316LTIGweldingrod(Fe–Cr–Ni–Mo), compatiblewith
alkaline structural components.
Each through-wall probe housed three electrodes made of the same alloy:
a reference electrode electrically connected to the stainless steel cell body,
a potential measurement electrode, and a working electrode. This config-
uration establishes a galvanic couple between the alloy and the stainless
steel cell, enabling simultaneous measurement of the free corrosion potential
Vcorr and galvanic corrosion currentI corr using a high impedance acquisi-
tion system equipped with Zero Resistance Ammeters (ZRA) (Fig. 6-below).
Signals were recorded continuously throughout the 7-day experiment. The
time-integrated corrosion chargeQ, derived fromIcorr, was used to estimate
the kinetics of material loss.
Please note that, although a precise conversion of charge into mass loss
would require defining an electrochemical equivalent for each alloy, the gal-
vanic corrosion current measured by the ZRA is directly proportional to the
rate of material dissolution. Consequently,Qprovides a robust comparative
indicator of corrosion kinetics across the different alloys, allowing the iden-
tification of trends and relative susceptibility even without applying a full
faradaic quantification.
4. Results. High-speed optical diagnostics
This section presents the main results of our high-speed optical diag-
nostics using a simple laboratory-scale cell described in Sec. 2. Hydrogen
bubble size is expected to affect electrolyzer efficiency, since large bubbles
on the electrode mask the electrode’s active area, increasing ohmic losses.
We determined the bubble size distribution histograms att= 35min, 4 h,
and 48 h for W+KOH, W+KOH/Triton X-100, and W+KOH/Surfynol 465
(Fig. 7). As observed, the surfactant has no significant effect on the overall
bubble size distribution. In the three cases, the mean diameter is of the or-
der of 100µm with a noticeable degree of polydispersity. However, adding
Surfynol 465 prevents the growth of bubbles larger than approximately 200
µm att= 35min and 4 h. This can also be observed in Fig. 8, which shows
the interfacial control exerted by Surfynol 465 during the first phase of the
process. It should be noted that the large bubbles produced in the absence
of Surfynol 465 constitute a significant fraction of the gas volume.
Figure 9 shows the (normalized) time during which a small surface ele-
ment of the image was occupied by gas. Att= 35min, the gas occupies a
12
