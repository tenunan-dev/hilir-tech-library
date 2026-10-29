---
source_id: "arxiv"
title: "A REINFORCEMENT-LEARNING-AUGMENTEDLIQUID-FUELED"
url: "https://arxiv.org/abs/2607.19281"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2607.19281. Abstract: A REINFORCEMENT-LEARNING-AUGMENTEDLIQUID-FUELED
REACTORNETWORKMODEL FORPREDICTINGLEAN
BLOWOUT INGASTURBINECOMBUSTORS
Philip John1, Eloghosa Ikponmwoba1, Pinaki Pal2, Opeoluwa Owoyele1∗
1Department of Mechanical and Industrial Engineering
Louisiana State University, Baton Rouge, LA 70803, USA
2Transportation and Power Systems Division
Argonne National Laboratory, 9700 S. Cass Ave, Lemont, IL 60439,"
---

# A REINFORCEMENT-LEARNING-AUGMENTEDLIQUID-FUELED

A REINFORCEMENT-LEARNING-AUGMENTEDLIQUID-FUELED
REACTORNETWORKMODEL FORPREDICTINGLEAN
BLOWOUT INGASTURBINECOMBUSTORS
Philip John1, Eloghosa Ikponmwoba1, Pinaki Pal2, Opeoluwa Owoyele1∗
1Department of Mechanical and Industrial Engineering
Louisiana State University, Baton Rouge, LA 70803, USA
2Transportation and Power Systems Division
Argonne National Laboratory, 9700 S. Cass Ave, Lemont, IL 60439, USA
ABSTRACT
This study introduces a reinforcement learning (RL) framework for generating optimal liquid-fueled
reactors to improve lean blowout (LBO) predictions in gas turbine combustors. Existing approaches
for determining cluster boundaries rely on manual heuristics or distance-based metrics in the input
space. In contrast, the proposed method is goal-oriented, explicitly accounting for the target metric
(e.g., LBO prediction accuracy) during cluster formation. The framework employs a multi-stage
clustering–classification strategy: an initial clustering step (e.g.,k-means clustering) generates a
large set of homogeneous micro-clusters, followed by an actor-critic RL agent that merges them
into optimal reactor zones. The validation study, performed using a Jet-A mechanism (119 species,
841 reactions), shows the RL framework offers improved predictive fidelity compared tok-means
and captures the correct LBO trends, while achieving substantial speedups relative to the high-
fidelity computational model. Overall, the RL-driven approach demonstrates strong potential as
a computationally efficient reduced-order modeling technique that can complement high-fidelity
simulations for rapid design-space exploration.
KeywordsReactor network modeling·Reinforcement learning·Lean blowout·Machine learning·Gas turbine
combustor·Reduced-order modeling
Novelty and Significance Statement
This study presents the first framework that integrates reinforcement-learning decision policies into chemical reactor
network construction, enabling reactor partitions and volumes to adapt based on physics-level objectives rather than
distance-based criteria. This also represents the first demonstration of a liquid-fueled reactor network capable of
reproducing parametric LBO trends across varying operating conditions. The significance of this work lies in the
ability of the proposed framework to produce physically consistent LBO trends at a fraction of the computational
cost of CFD, a capability that existing reduced-order methods fail to provide. This makes the framework a practical
complement to high-fidelity CFD for rapid design-space exploration of gas turbine combustors operating near the LBO
limit.
1 Introduction
Lean blowout (LBO) represents a critical operational limit in gas turbine combustors, particularly for systems oper-
ating at lean equivalence ratios [1, 2, 3]. In liquid-fueled systems, the underlying physics are additionally influenced
by droplet evaporation and fuel-air mixing processes, which introduce additional timescales prior to chemical reaction
∗Corresponding author:oowoyele@lsu.edu
arXiv:2607.19281v1  [cs.LG]  21 Jul 2026

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
Figure 1: Schematic of the RL–augmented liquid-fueled reactor network framework.
[4]. Accurate characterization of the LBO limit has traditionally relied on experimental diagnostics such as chemi-
luminescence imaging and direct flame visualization [5]. More recently, high-fidelity computational fluid dynamics
(CFD) approaches have emerged as powerful tools for studying LBO [6, 7, 8, 9], enabling detailed resolution of the
flow, spray, and combustion fields, as well as virtual testing of fuel and geometric effects. However, such approaches
remain computationally expensive, particularly for large eddy simulations (LES) of reacting two-phase flows [10, 11],
limiting their practicality for large parametric studies and combustor design optimization.
In response to these costs, chemical reactor networks (CRNs) have emerged as computationally efficient alternatives
for modeling gas turbines and other combustion systems [12, 13]. CRN modeling involves partitioning the CFD
domain into individual reactor zones, followed by the application of simplified governing equations for each reac-
tor [14, 12]. Several approaches have been developed to obtain these partitions. Early approaches relied on manual
partitioning, wherein an expert delineates the flow-fields into zones based ona prioriknowledge of the flow and com-
bustion physics [15, 16, 2]. To reduce dependence on expert intervention, automated approaches have been introduced,
including threshold-based filtering [17, 18, 19], and more recently, clustering-based methods that group computational
cells by thermochemical similarity [20]. However, the application of CRNs to liquid-fueled systems introduces ad-
ditional modeling challenges that are largely absent in gas-fueled configurations [21]. Specifically, the presence of a
dispersed liquid phase requires the reactor topology to accommodate not only gas-phase thermochemical variation,
but also spray-phase phenomena including droplet breakup, evaporation, and the spatial evolution of fuel-air mixing.
A common limitation of existing automated CRN clustering approaches is that the reactor partitions are constructed
solely from distances in the input feature space, without considering their impact on the target quantity of interest.
Because quantities such as NOx and LBO depend nonlinearly on the underlying thermochemical variables, distance-
based clustering can produce suboptimal reactor configurations. This limitation is particularly severe for LBO, where
small changes in the primary reaction zone can strongly affect extinction behavior. Consequently, prior CRN-based
LBO studies have largely been validated only at isolated operating conditions [22, 2], with limited demonstration of
trend prediction across parametric variations.
In this study, we address this limitation by introducing a reinforcement-learning (RL) framework for automated extrac-
tion of optimal reactors in a liquid-fueled reactor network (LFRN) aimed at minimizing LBO prediction error. Unlike
distance-based clustering approaches, the RL agent explores reactor partitions and is rewarded directly based on LBO
predictive accuracy, thereby promoting the discovery of physically relevant partitions that conventional feature-space
metrics may fail to capture. The approach is illustrated in Fig. 1. The main contributions are: (1) development of
an RL-based framework for goal-oriented reactor-network generation; (2) validation for liquid-fueled LBO prediction
using a 119-species Jet-A mechanism [23, 24]; and (3) quantitative demonstration of improved performance relative to
conventional distance-based clustering. The trained reactor network is intended to be locally predictive within the com-
bustor geometry and operating envelope represented by the baseline CFD data, consistent with standard CRN models
discussed above. However, the framework itself is general and can be reapplied to other configurations following the
same procedure.
2

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
2 Methodology
2.1 CFD Numerical Setup and Computational Domain
Figure 2: Liquid-fueled swirl-stabilized combustor geometry.
The combustor geometry (Fig. 2) features a cylindrical can combustor (radius 0.03 m, length 0.2 m) with a single outlet,
primary and secondary air inlets, and secondary/dilution holes (8 mm diameter) distributed along the liner walls. A
central fuel injector (250µm diameter) is surrounded by a six-vane swirl-stabilized primary inlet that generates a
central recirculation zone (CRZ) for flame stabilization. Air enters at 350 K through the primary and secondary
inlets, with 25% of the secondary inflow going through the effusion holes and the remaining 75% going through the
secondary and dilution holes. The resulting primary equivalence ratio is0.35. A Rosin–Rammler distribution with
d32 = 20µm [25, 26] and spread parametern= 2.8was employed for the spray injection, with a cone half-angle of
35◦ and injection velocity of 63 m/s. Primary/secondary air and dilution holes were modeled as mass-flow inlets, the
outlet as a pressure outlet, and the walls as no-slip adiabatic boundaries. Additional details are presented in Table 1.
Table 1: Baseline operating and boundary conditions.
Parameter Value
Combustor radius 0.03 m
Combustor length 0.2 m
Fuel injector diameter 250µm
Operating pressure 2 atm
Air inlet temperature 350 K
Fuel inlet temperature 327 K
Primary air flow rate 0.0487 kg/s
Secondary air flow rate 0.1135 kg/s
Fuel mass flow rate 0.0012 kg/s
Global equiv. ratio (ϕglobal) 0.35
The Flamelet Generated Manifold (FGM) approach [27] was employed to model turbulence-chemistry interactions,
pre-computing chemistry using flamelet equations in mixture fraction space [28] to generate a lookup table param-
eterized by a filtered progress variableec, defined as the normalized sumc= (Y CO2 +Y CO)/(Y eqCO2 +Y eqCO), where
superscript “eq” denotes equilibrium values, mixture fraction eZ, mixture fraction variance gZ ′′2, and enthalpy eh. The
flamelet library was generated for Jet-A using the HyChem kinetic mechanism (119 species, 841 reactions) [23, 24].
Liquid spray was modeled using Lagrangian particle tracking with the Taylor Analogy Breakup (TAB) model [29] for
breakup, Frossling correlation [30] for evaporation, and Rosin-Rammler distribution [31] for initial droplet size.
A Reynolds-Averaged Navier-Stokes (RANS)k–εsimulation was first conducted at a baseline condition to calibrate
the reactor network (RN) model as done in other studies [12, 20, 13, 14, 16], thus providing the mean flow and
thermochemical fields used for reactor zone construction. Parametric Large Eddy Simulations (LES) (using a dynamic
structure model [32]) were subsequently performed across a range of operating conditions to predict lean blowout
(LBO) equivalence ratios. A baseline LES is used for training the RL model, while other conditions are used for
comparison with the CRNs. The CFD simulations were fully 3-dimensional and performed using CONVERGE CFD
(v5.0.2) [33]. The RANS and LES meshes contained approximately 2 million and 3 million cells, respectively, with
the LES count corresponding to the peak adaptive mesh refinement (AMR) level. The LES employed AMR to refine
regions of high velocity and temperature gradients, with the grid dynamically refined from a 2.5 mm base size to a
minimum cell size of 0.625 mm in the primary reaction zone. The RANS used a reduced base grid of 2.0 mm which
3

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
was refined to a minimum of 1.0 mm in the reaction zone. AMR was activated after an initial flow-through time
to allow the bulk flow to develop before refinement. A grid convergence study showed that further refinements (to
the base grid or AMR level) did not alter the predicted blowout equivalence ratio. The LES simulations utilized 256
processors and required approximately 2–4 days per operating condition.
2.2 Reactor Network Development
Unlike CFD simulations that discretize the domain into millions of cells, the reactor network methodology partitions
the combustor volume into a relatively small number of zones, with each described by simplified transport equations.
In this study, we employ standard reactor types, including perfectly stirred reactors (PSRs) and plug flow reactors
(PFRs), alongside two specialized reactors introduced to account for the liquid-fuel physics. The reactor network is
solved using Cantera (v3.0)[34] with its in-built reactor classes. The plug flow zone is solved along the axial coordinate
(rather than as a chain of PSRs), and all reactors are solved at steady state. The choice of reactors is determined by
considering the dominant physical processes in each reactor.
A PSR assumes perfect spatial mixing within the reactor volumeV, so that all properties are uniform in space and may
only vary in time. A PFR, in contrast, permits spatial gradients only along the axial flow directionz. The equations
used to model the PSR and PFR are based on the standard equations used in combustion literature, and can be found
in a previous study by the authors [21]. Inter-reactor mass flow rates are determined from the RANS simulation of the
combustor. To capture the two-phase physics specific to liquid-fueled combustors, two additional specialized reactors
are introduced: anevaporator/breakup reactorand amixing reactor. Further details can be found in a previous study
by the authors [21]. In the evaporator/breakup reactor, the gas-phase species and energy equations are augmented with
source terms that account for the transfer of mass and energy from the droplet phase to the gas phase. The species
conservation equation becomes:
˙min(Yk,in −Y k) + ˙ωkWkV+ ˙Sevapk V= 0(1)
where ˙Sevapk is the evaporative mass source of fuel vapor from the droplet phase, computed from the Frossling evapo-ration correlation consistent with the CFD setup. The corresponding energy equation includes a spray enthalpy source
term to account for the latent heat consumed during evaporation and the sensible heat carried by the evaporating fuel:
˙min
X
k
Yk,inhk(Tin)−˙m out
X
k
Ykhk(T)
+ ˙Sevape V= 0,
(2)
where ˙Sevape is the net energy source from the evaporating droplets, which includes the latent heat of vaporization and
the sensible enthalpy of the released fuel vapor. The evaporator/breakup reactor also tracks the evolution of the droplet
size distribution through the breakup process, consistent with the TAB breakup model used in the CFD, providing an
updated mean droplet diameter as input to the downstream mixing reactor. The mixing reactor receives the partially
evaporated spray and models the continued evaporation of the remaining liquid fuel and the subsequent gas-phase
fuel-air mixing prior to combustion. It employs the same augmented species and energy equations (Eqs. 1–2), with the
evaporation source terms now representing the residual liquid fuel that did not evaporate in the upstream stage. Thus,
the evaporation/breakup reactor captures breakup and evaporation, while the mixer captures only further evaporation
and subsequent mixing. The outlet of the mixing reactor provides the fully gas-phase inlet conditions, including
fuel vapor concentration, mixture fraction, and temperature, for the downstream PSR and PFR combustion zones.
This sequential arrangement ensures that the overall reactor topology captures the physical order of events, namely
atomization, evaporation, mixing, and combustion, that governs LBO behavior in liquid-fueled combustion systems.
All the reactor networks used the same mechanism as the CFD simulations.
2.2.1k-means Clustering
Reactor network construction begins by extracting flow and thermochemical information from three-dimensional CFD
results at representative operating conditions. Each computational cell is characterized by a feature vector comprising
temperature, equivalence ratio, OH mass fraction, and streamwise distancex:θ i = [Ti, ϕi, YOH,i, xi].The full dataset
is organized in matrix form,Θ= [θ T1 ,θ T2 , . . . ,θTno ]T , withn o denoting the total number of CFD cells. Specifically,TandY OH characterize local reactivity and heat-release activity,ϕcaptures the local mixing state, and the streamwise
coordinatexenforces spatial coherence of the reactor partition. Since these variables were sufficient to capture the
observed LBO behavior, the feature set was not expanded further.
To maintain computational tractability with the large CFD dataset, which contains on the order of10 6 points, a hier-
archical clustering strategy is used. First, the domain is partitioned inton f = 70micro-clustersusingk-means, with
each micro-cluster represented by its centroid in feature space. Using the RL approach described in Section 2.2.2,
4

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
these 70 centroids are then mapped to a smaller set ofn c = 7larger clusters that define the final reactor zones. There-
fore, although the inter-reactor mass flow rates are extracted from CFD, the reactor networks remain strongly reduced
by collapsing the fully resolved reacting flow into a small number of idealized reactor zones with fixed inter-zone
exchange. Also, this two-level clustering approach addresses two limitations of a direct RL-based mapping. First, it
avoids the memory burden associated with operating directly on all10 6 CFD points. Second, it promotes smoother
and more physically coherent zone boundaries, whereas direct RL-based clustering produced irregular and noisy parti-
tions. For comparison in Section 3, a baseline reactor network is separately constructed by applyingk-means directly
to the CFD dataset withn c = 7, yielding 7 reactor zones in a single step without the intermediate micro-cluster stage.
This purelyk-means-derived network serves as the distance-based reference against which the RL-augmented network
(Section 2.2.2) is compared.
2.2.2 Reinforcement-Learning Cluster Refinement
Sincek-means clustering is purely distance-based, it can group together regions with dissimilar thermochemical be-
havior, thereby reducing the physical consistency of the reactor network (RN) model. To address this limitation, the
k-means micro-clusters were used as the initial partition, after which anactor–criticRL approach [35] was employed
to reassign the clusters for improved LBO prediction. At each iteration, given the current cluster-state descriptors t
(i.e., centroid thermochemical features), the actor networkπ θ(at |s t), parameterized byθ, outputs a stochastic policy
over possible cluster reassignmentsa t. In other words, the actor selects an action, corresponding to a reassignment
of clusters, based on the current state. The actor is implemented as a fully connected neural network with two hidden
layers of size 128 and ReLU activations. Its output layer contains seven neurons, corresponding to the possible cluster
assignments. These outputs are converted through a softmax function into a categorical probability distribution over
actions, from which an action is sampled during training to encourage exploration. During inference, the action with
the highest probability is selected, producing a deterministic policy.
The critic, by contrast, evaluates the quality of the current state by estimating the expected cumulative future reward
associated with it. Specifically, the critic networkV ψ(st), parameterized byψ, approximates the state-value function
and provides a baseline for assessing whether the actor’s chosen action leads to improvement. The critic uses the same
hidden-layer architecture as the actor. Together, the actor and critic are trained to refine the cluster boundaries in a
manner that improves the predictive accuracy of the RN model for lean blowout. At inference, only the trained actor
is retained. During training, we characterize lean blowout based on the maximum reactor temperature falling below
a critical temperature,T c.T c = 1300K is obtained by starting from a stable condition and progressively reducingϕ
while monitoring the maximum reactor temperature in the CRN. Near extinction, a rapid collapse inTmax is observed,
indicating that stable combustion can no longer be sustained below this temperature threshold (as shown in Fig. S2).
Using this temperature-based criterion avoids performing full transient LBO calculations during RL training, which
would be computationally prohibitive given the thousands of candidate reactor-network configurations explored.
0 6 12 18 24
10
5
0
5
Average Reward
a
0 6 12 18 24
0
100
200
300
400Avg. Temp Diff (K)
b
0 6 12 18 24
Episode
160
240
320Value Loss
c
0 6 12 18 24
Episode
0.14
0.16
0.18Entropy
d
Figure 3: RL training metrics as functions of training episode. One episode consists of 100 iterations.
During training, the RL procedure operates in reverse by fixing the reactor-network equivalence ratio at the LES-
derivedϕ LBO, which is obtained by running a single high fidelity LES. The objective is then to adjust the reactor
partition such that, at this known blowout condition, the reactor-network prediction produces a maximum temperature
as close as possible to the surrogate extinction marker,T c. Therefore, after each reactor-network simulation step, a
5

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
temperature-based reward that penalizes deviations fromT c is computed as:
Rt = exp

− |Tt −T c|100  −1,(3)
The actor parameters are updated following the policy gradient:
∇θJ(θ) =E

∇θ logπ θ(at|st)δ t

,(4)
whereδ t is the temporal difference error defined as:
δt =R t +γV ψ(st+1)−V ψ(st),(5)
while the critic minimizes the temporal-difference loss:
LV =

Rt +γV ψ(st+1)−V ψ(st)
2
.(6)
An additional entropy regularization termL H =− Pa πθ(at|st) logπ θ(at|st)is applied to encourage exploration.The overall optimization objective combines the policy-gradient objective, the value-function loss, and an entropy
regularization term:
Ltotal =−J(θ) +λ V LV −λ H LH ,(7)
whereλ V andλ H are weighting coefficients for stability. Training employed discount factorγ= 0.99,λ V = 0.5,
andλ H initially set to0.01and annealed exponentially to encourage policy convergence. These values are in line with
commonly used hyperparameter settings reported in the literature [36, 37, 38]. From Fig. 3, we see that during training,
the RL agent progressively reduces the mean temperature deviation across episodes, as seen by increasing reward
and decreasing entropy over the training horizon. After training, the reactor network was deployed to predictϕ LBO
using a staged equivalence-ratio reduction procedure analogous to the CFD approach described later in Section 3.3.
Starting from a stable operating condition, successive steady-state calculations were performed at progressively lower
equivalence ratios untilT max < Tc, which defines blowout during evaluation. During training, however, the target
ϕLBO is already known, so Eq. 3 penalizes deviations fromT c on either side, since temperatures above or belowT c
correspond to delayed or premature blowout prediction, respectively.
3 Results
3.1 CFD Flame Structure
Figure 4: (a) OH mass fraction and (b) temperature contours obtained from the CFD solution atϕ= 0.35.
6

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
Fig. 4 presents the spatial distribution of OH mass fraction and temperature on they= 0plane from the steady-
state CFD solution at the reference operating condition (ϕ= 0.35). Peak OH mass fractions of3.8×10 −3 are
concentrated within the central recirculation zone (x= 0.02–0.04m), where droplet evaporation, mixing, and primary
heat release occur simultaneously. Downstream ofx≈0.06m, OH concentrations decay sharply, marking the
completion of the principal heat release zone. The region of elevated temperature occupies a broader spatial volume,
with peak values near 2000 K coinciding with the high-OH region, yet retaining pockets of elevated temperature
further downstream (x >0.08m) due to the continued oxidation of intermediate combustion products beyond the
primary reaction zone. The spatial distributions of OH mass fraction and temperature revealed by these contours serve
as the primary thermochemical basis for reactor zone construction, and their structure directly influences the resulting
cluster boundaries, as discussed in the following section.
3.2 Reactor Zone Partitioning
The seven clusters in Fig. 5 correspond to the following reactor types: an evaporator/breakup PSR immediately
downstream of the injector (cluster/reactor 1); a mixing PSR after this region to capture continued evaporation (clus-
ter/reactor 7); four standard PSRs representing the 2 flame zones (reactors 3 and 4), recirculation (reactor 6), and
dilution regions (reactor 2); and a downstream post-flame PFR (reactor 5). The reactor interconnections are shown
schematically in Fig. S1 of the Supplemental Material. The reactor assignments follow the underlying flow physics:
zones characterized by strong transport effects are modeled as PSRs, while the downstream predominantly axial post-
flame region is modeled as a PFR. The evaporator/breakup and mixing reactors with modifications to capture breakup
or evaporation are placed downstream of the injector to capture primary atomization, evaporation, and fuel-air mixing
prior to combustion.
Figure 5: Reactor zones obtained from (a)k-means clustering and (b) the RL-based partitioning.
Fig. 5 compares the domain partitioning produced by thek-means algorithm and the RL policy for a seven-reactor
network. The most consequential difference between the two partitionings concerns Reactor Zone 3, which largely
overlaps with the primary combustion region identified in Fig. 4. Thek-means algorithm, operating purely on Eu-
clidean distance in the feature space, assigns Zone 3 a volume of approximately 28 cm 3. This compact zone captures
only the region of highest OH concentration and temperature, which is essentially the core of the primary flame re-
gion. The RL policy, in contrast, expands Zone 3 to approximately 39 cm 3, a 39% increase in volume relative to the
k-means partition. This broader zone encompasses not only the peak-reactivity core but also the surrounding region
of moderate heat release, including portions of the recirculation zone where OH is elevated but not at its maximum.
These differences between Figs. 5a and b arise from a fundamental difference between the two clustering objectives.
Thek-means algorithm minimizes intra-cluster variance across all spatial features uniformly, which naturally biases
it toward clusters with homogeneous representations. In contrast, the RL policy is driven exclusively by a reward
signal tied to the accuracy of LBO prediction. Since LBO is governed by the global extinction behavior of the pri-
mary reaction zone, the RL agent learns to include the moderate-reactivity periphery of the flame within Zone 3. This
has significant implications for the predictive accuracy of both approaches, as will be discussed in subsequent sec-
7

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
tions. Downstream zones that are less chemically active (Reactors 2, 5, and 6) remain largely unaffected by the RL
optimization, consistent with their limited influence on the LBO reward signal.
3.3 Transient LBO Simulation
Figure 6: V olume-averaged primary-zone temperature during transient ramp-down toward LBO.
A transient lean blowout simulation was conducted to validate the framework under dynamic operating conditions.
The vicinity of the LBO equivalence ratio was first identified using a coarse staged reduction of the fuel flow rate,
starting fromϕ≈0.35and reducing the equivalence ratio in decrements of∆ϕ= 0.0435until extinction occurred.
For the baseline case, three coarse staged reductions were required to reach the vicinity of the LBO condition. The
equivalence ratio was then further refined using smaller decrements of∆ϕ= 0.001to determine the final reported
ϕLBO more accurately. The reported LBO values correspond to the fine-step refinement rather than the initial coarse
staging procedure. The following results in this subsection and thereafter should be interpreted in the context that the
RL-derived reactor network is informed by data from a baseline LES, while thek-means only includes information
from RANS. The objective is therefore to assess the added improvements obtained from a goal-oriented partitioning
strategy, but this involves an additional upfront cost of a baseline LES.
Fig. 6 presents the volume-averaged mean temperature as a function of time for the CFD reference, the RL-based
LFRN and thek-means LFRN. All three results are averaged over the same fixed control volume (x∈[0,0.05]m,
y, z∈[−0.025,0.025]m) enclosing the primary reaction zone. The CFD result is smoothed with a 10 ms moving
average to suppress LES oscillations, and the early-time dip in temperature is a numerical artifact due to the presence
of a coarse mesh in the domain before the full activation of AMR. The CFD shows a gradual thermal decline with
decreasingϕ, followed by a sharp collapse atτ LBO ≈80ms (ϕ≈0.219). The RL-based LFRN reproduces this
behavior closely, predicting blowout at nearly the sameϕ, although with a slightly earlier temperature collapse due to
the reduced thermal inertia of the seven-reactor representation. Thek-means-based LFRN, by contrast, fails to predict
blowout entirely, with the volume-averaged temperature remaining elevated at approximately 1600 K throughout the
full equivalence ratio ramp, including at the final condition where both the CFD and the RL-based network indicate
global extinction.
3.4 Timescale Analysis of LBO
To explain the divergent LBO predictions of the RL-based andk-means reactor networks, a timescale analysis was
performed for Zone 3, identified in Section 3.1 as the primary combustion zone and region of highest OH activity.
Three representative times were considered:τ≈0.35τ LBO (far from LBO),τ≈0.8τ LBO (near LBO), andτ≈τ LBO
(at LBO). The flow timescale was defined asτ flow = ¯ρV /˙m, where¯ρis the zone-averaged density,Vis the zone
volume, and˙mis the mass flow rate through the zone. The chemical timescale was taken as the residence time at
blowout,τ chem =τ res, similar to Wang et al. [39], and the Damköhler number was defined asDa=τ flow/τchem.
8

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
Figure 7: Damköhler number in Zone 3 at three representative timesteps for the CFD reference, LFRN (RL), and
LFRN (k-means). The dashed line indicatesDa= 1.
We emphasize that the purpose of this analysis is not to directly compare the individual timescales of the LES and
reactor-network models. The LES resolves fully unsteady three-dimensional transport, whereas the reactor network
represents coarse averaged inter-zone exchange, making direct comparison of timescales (especially flow) across
frameworks of limited physical consistency. This mismatch is inherent to coarse CRN models constructed from RANS
mean fields, which cannot resolve the instantaneous turbulent fluctuations and recirculation dynamics associated with
transient LBO. Consequently, the reactor network evolves through a sequence of quasi-steady states as the equiva-
lence ratio is reduced. Therefore, the analysis focuses on whether the ratio of flow and chemical timescales within
each framework remains internally consistent as blowout is approached, and on why the RL-derived partition succeeds
while thek-means partition does not.
Figure 7 summarizes the resulting Damköhler-number evolution, with details about the individual timescales shown
in Table S1 in the Supplemental Material. Far from LBO (τ≈0.35τ LBO), all models remain in a stable combustion
regime withDa≫1. However, the RL andk-means networks already differ substantially in their chemical timescales.
The RL-derived Zone 3 predictsτ chem ≈4.72µs. This difference arises because thek-means partition isolates only
the peak-reactivity core of the flame, producing artificially high zone-averaged temperature and OH concentration, and
therefore unrealistically short chemical timescales. As the equivalence ratio is reduced toward blowout, the divergence
between the two reactor networks becomes more pronounced. Near LBO (τ≈0.8τ LBO), the RL-derived network
predicts a substantial increase in chemical timescale to approximately27.9µs. In contrast, thek-means network still
predicts a short chemical timescale of only1.15µs, indicating that its Zone 3 remains strongly reactive despite the
weakening global flame. Consequently, the RL-derived Damköhler number decreases significantly as extinction is
approached, while thek-means-derived value remains artificially large.
Finally, atτ≈τ LBO, both the CFD and RL-derived reactor network exhibit a sharp increase in chemical timescale,
reaching approximately1020µs and1300µs, respectively. In both cases, this producesDa <1(Da CFD ≈0.10,
DaRL ≈0.22), indicating that the reacting mixture is no longer able to sustain combustion before being convected
from the primary zone. Thek-means network, however, continues to predict a very short chemical timescale (τ chem ≈
2.22µs) and a large Damköhler number (Da≈116), showing no indication of impending blowout. These results
suggest that the RL model succeeds because, by learning from experience informed by the reward signal in Eq. 3, it
learns reactor boundaries that are consistent with the observed blowout. In particular, the RL-derived partition captures
the sharp increase inτ chem near extinction, causing the ratioτ flow/τchem to evolve in a manner qualitatively consistent
with the CFD behavior, as shown in Fig. 7.
3.5 Sensitivity to Number of Micro-Clusters
A sensitivity study was conducted by varying the number of micro-clustersn f over the range 35–280 while keeping
the number of coarse reactor zones fixed atnc = 7. Figure 8 summarizes the resulting error inϕLBO relative to the CFD
reference value (ϕLBO = 0.218). The results show thatn f = 70yields the lowest prediction error of 0.46%. Very small
values ofn f lead to higher errors due to coarser zone boundaries, since the number of micro-cluster centroids would
not provide the RL algorithm with sufficient degrees of freedom to precisely capture the optimal reactor boundaries.
Conversely, at larger values ofn f , the performance deteriorates as the increased number of micro-clusters introduces
9

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
noisier and less coherent zone boundaries. Despite this deterioration at both extremes, the errors remain relatively
small across the range ofn f values considered, which spans a broad eightfold increase fromn f = 35ton f = 280.
Figure 8: Percentage error inϕ LBO prediction as a function of the number of micro-clustersn f .
3.6 LBO Sensitivity to Primary Air Flow Rate and Inlet Temperature
A parametric study was conducted to examine the effect of the primary air mass flow rate on LBO limits. Fig. 9
compares LBO predictions from both reactor-network approaches against CFD simulations across a primary mass
flow rate range of 0.0387–0.0687 kg/s, which corresponds to primary equivalence ratios of 0.219 to 0.325 at the
baseline operating condition. The result from the 0.0487 kg/s air flow rate (baseline) was used to train the RL-driven
framework. The resulting network was then applied to the remaining operating conditions within the mass flow rate
range. The maximum mass flow rate corresponds to an increase of approximately 77% relative to the minimum value
considered.
Figure 9: Parametric effect of mass flow rate onϕ LBO.
The CFD results demonstrate a positive correlation between the primary air mass flow rate andϕLBO, with values rang-
ing from 0.219 to 0.325. This behavior is physically consistent. At fixed fuel flow, increasing˙mshortens the residence
time in the primary zone, sinceτ flow ∝ρV /˙m, thereby also lowering the Damköhler number, Da=τ flow/τchem. As
the mixture is leaned toward LBO,τ chem rises sharply (Section 3.4), so Da falls below unity at a richer mixture than it
would at the baseline flow rate, shifting the LBO point to a higherϕ. Increased turbulent mixing at higher˙mreinforces
this trend by raising local strain rates and entraining cooler unreacted gas into the reaction zone, but this is a secondary
effect. Thek-means approach, relying solely on distances within the input feature space, is unable to capture this
trend, resulting in a non-monotonic variation ofϕ LBO with increasing mass flow rate (i.e., a decrease, followed by a
slight increase). In contrast, the RL model captures the correct qualitative trend of increasingϕ LBO with increasing
mass flow rate across the entire range of conditions. At the baseline condition, unsurprisingly, the RL model produces
10

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
a very low error of approximately 0.46%, confirming that the RL agent successfully identified near-optimal cluster
boundaries. At non-baseline conditions, higher quantitative errors are observed. The sensitivity ofϕ LBO with respect
to the inlet mass flow rate at the reference condition is lower compared to the CFD solution, as evidenced by the lower
slope. This results in an overprediction ofϕ LBO at 0.0487 kg/s and an underprediction at 0.0587 kg/s. However, the
error levels remain acceptable given the low complexity of a seven-reactor reduced-order network.
Figure 10: Parametric effect of air inlet temperature onϕ LBO.
A second parametric study investigated variation inϕ LBO as the inlet temperature is varied from 350 K to 500 K.
Fig. 10 presents the LBO predictions from both reactor network approaches compared to the CFD reference. The CFD
results show that increasing inlet temperature from 350 K to 500 K reducesϕ LBO from 0.2187 to 0.197. This trend
is physically consistent, since higher inlet temperatures lead to increased reactivity of the mixture and shortens the
chemical timescale in the primary zone. As a result, combustion can be sustained for longer as the mixture is leaned.
The RL approach demonstrates a high level of accuracy, capturing both the magnitude and direction of this trend with
errors below 0.14% at both conditions. In contrast, thek-means approach exhibits substantial under-predictions of
41.47% and 65.48% at 350 K and 500 K, respectively, though it qualitatively captures the decreasing trend inϕ LBO.
3.7 Computational Efficiency
The LES computations employed in this study required 256 processors and 2–4 days per operating condition. In con-
trast, the reactor network predictedϕ LBO in approximately 22 s on a 12-core Intel Core i7 workstation, corresponding
to a speedup exceeding 7,800 while retaining the correct qualitative LBO trends. The entire RL training procedure
completed in approximately 3 h. It should be noted that this speedup estimation does not include the initial LES cost
required to generate the baseline training data. It only captures the reduced cost of evaluating additional operating
conditions once the baseline CFD-informed model has been constructed.
4 Conclusions
This study presented a reinforcement-learning-augmented liquid-fueled reactor network framework for predicting lean
blowout in gas turbine combustors using goal-oriented reactor partitioning. The results show that LBO prediction
depends strongly on how the domain is partitioned, and that goal-oriented zoning provides a more effective alternative
to conventional distance-based clustering. In practice, the lightweight liquid fueled reactor can be used to reduce the
number of expensive CFD simulations required during combustor design by rapidly screening candidate operating
conditions, identifying promising regions of the design space, and guiding targeted high-fidelity simulations. Future
work will extend the framework to additional fuels and combustor configurations and incorporate NOx prediction into
the RL reward formulation.
CRediT authorship contribution statement
Philip John: Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – original
draft.Eloghosa Ikponmwoba: Methodology, Software, Formal analysis, Investigation, Writing – original draft.
11

RL-Augmented Liquid-Fueled Reactor Network for Lean Blowout Prediction
Pinaki Pal: Methodology, Writing – review & editing.Opeoluwa Owoyele: Conceptualization, Funding acquisition,
Methodology, Supervision, Project administration, Resources, Writing – review & editing.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
Acknowledgments
This material is based upon work supported by the U.S. Department of Energy, Office of Energy Efficiency and
Renewable Energy, Bioenergy Technologies Office under Award Number DE-SC0023463. The CONVERGE soft-
ware licenses used in this work were provided through the CONVERGE Academic Program, and Convergent Science
provided the baseline geometry utilized in this study. Portions of this research were conducted with high perfor-
mance computational resources provided by Louisiana State University (http://www.hpc.lsu.edu). The sub-
mitted manuscript has been partly created by UChicago Argonne, LLC, Operator of Argonne National Laboratory
(Argonne). Argonne, a U.S. Department of Energy Office of Science Laboratory, operated under Contract No. DE-
AC02-06CH11357.
References
[1] S. Gupta, Philip C. Malte, Steven L. Brunton, and Igor V . Novosselov. Prevention of lean flame blowout using a
predictive chemical reactor network control.Fuel, 236:583–588, 2019.
[2] Abhishek Kaluri, Philip C. Malte, and Igor V . Novosselov. Real-time prediction of lean blowout using chemical
reactor network.Fuel, 234:797–808, 2018.
[3] Lei Cheng, Meng Zhang, Shiyao Peng, Jinhua Wang, and Zuohua Huang. Large Eddy Simulation of the effect
of hydrogen ratio on the flame stabilization and blow-off dynamics of a lean CH4/H2/air bluff-body flame.Appl.
Sci., 14:1846, 2024.
[4] G.M. Faeth. Evaporation and combustion of sprays.Progress in Energy and Combustion Science, 9:1–76, 1983.
[5] M. Stöhr, I. Boxx, C. Carter, and W. Meier. Dynamics of lean blowout of a swirl-stabilized flame in a gas turbine
model combustor.Proc. Combust. Inst., 33:2953–2960, 2011.
[6] Lucas Esclapez, Peter C. Ma, Eric Mayhew, Rui Xu, Scott Stouffer, Tonghun Lee, Hai Wang, and Matthias Ihme.
Fuel effects on lean blow-out in a realistic gas turbine combustor.Combust. Flame, 181:82–99, 2017.
[7] Makoto Endo, Kathleen M. Tacina, Yolanda R. Hicks, Tyler G. Capil, and Jeffrey P. Moder. Numerical simulation
of lean blowout of alternative fuels in 7-element lean direct injector. InAIAA Aviation 2021 F orum, pages AIAA
2021–3458. American Institute of Aeronautics and Astronautics, 2021.
[8] Debolina Dasgupta and Sibendu Som. Fuel property impact on lean blow out for sustainable aviation fuels in gas
turbine combustors. InProc. ASME Turbo Expo 2024: Turbomachinery Tech. Conf. Expo., page V03AT04A073,
2024. Paper No. GT2024-126789.
[9] Pier Carlo Nassini, Daniele Pampaloni, Roberto Meloni, and Antonio Andreini. Lean blow-out prediction in an
industrial gas turbine combustor through a LES-based CFD analysis.Combust. Flame, 229:111391, 2021.
[10] M. Boileau, G. Staffelbach, B. Cuenot, T. Poinsot, and C. Bérat. LES of an ignition sequence in a gas turbine
engine.Combustion and Flame, 154:2–22, 2008.
[11] Thomas Jaravel, Eleonore Riber, Bénédicte Cuenot, and Perrine Pepiot. Prediction of flame structure and pol-
lutant formation of sandia flame d using large eddy simulation with direct integration of chemical kinetics.
Combust. Flame, 188:180–198, 2018.
[12] M. Falcitelli, S. Pasini, and Leonardo Tognotti. Modelling practical combustion systems and predicting NOx
emissions with an integrated CFD based approach.Comput. Chem. Eng., 26:1171–1183, 2002.
[13] Jungkyu Park, Truc Huu Nguyen, Daero Joung, Kang Yul Huh, and Min Chul Lee. Prediction of NOx and
CO emissions from an industrial lean-premixed gas turbine combustor using a chemical reactor network model.
Energy Fuels, 27:1643–1651, 2013.
[14] Seyfettin Ertan Hataysal.A Coupled Flow and Chemical Reactor Network Model for Predicting Gas Turbine
Combustor Performance. PhD thesis, Middle East Technical University, Ankara, Turkey, 2016.
12
