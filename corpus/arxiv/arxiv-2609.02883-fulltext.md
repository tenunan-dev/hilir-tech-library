---
source_id: "arxiv"
title: "Repairing PBE-Spurious Metallicity for"
url: "https://arxiv.org/abs/2609.02883"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.02883. Abstract: Repairing PBE-Spurious Metallicity for
HSE06-Level Screening of 2D Photocatalysts for
Green Hydrogen Production
Ritam Chakraborty∗,† and Arpan Das∗,‡
†Theoretical Sciences Unit, Jawaharlal Nehru Centre for Advanced Scientific Research
(JNCASR), Bangalore 560064, India
‡Department of Science and Humanities, Audisankara (Deemed to be University), Gudur
524101, India
E-mail: ritamchakraborty454@gmail"
---

# Repairing PBE-Spurious Metallicity for

Repairing PBE-Spurious Metallicity for
HSE06-Level Screening of 2D Photocatalysts for
Green Hydrogen Production
Ritam Chakraborty∗,† and Arpan Das∗,‡
†Theoretical Sciences Unit, Jawaharlal Nehru Centre for Advanced Scientific Research
(JNCASR), Bangalore 560064, India
‡Department of Science and Humanities, Audisankara (Deemed to be University), Gudur
524101, India
E-mail: ritamchakraborty454@gmail.com; arpandas9236@gmail.com
Abstract
Semilocal PBE calculations can remove viable photocatalysts before screening by
labeling narrow-gap semiconductors as metals. We address this failure mode in the
Computational 2D Materials Database (C2DB) by combining leakage-aware repair
of PBE-spurious metallicity with HSE06–PBE ∆-learning. Stage I classifies HSE06-
unknown PBE metals using structural, chemical, magnetic, and stability descriptors,
while excluding HSE06/GW quantities and PBE electronic shortcuts. Stage II learns
EHSE06g −E PBEg for the corrected insulating population. The curated XGBoost regres-
sor reconstructs HSE06 gaps with a mean absolute error of 0.108 eV (R 2 = 0.989),
compared with 1.036 eV for raw PBE. The Stage I classifier is used only for triage be-
cause the labeled true-metal class contains 29 materials; its best holdout performance
gives 87.5% accuracy, 0.286 true-metal recall, and 0.643 balanced accuracy. The cor-
rected pH 0 electronic screen yields 10 strict and 29 initial relaxed green-hydrogen
1
arXiv:2609.02883v1  [cond-mat.mtrl-sci]  2 Sep 2026

photocatalyst candidates. Four strict and 18 relaxed candidates would fail the same
1.6–2.8 eV gap window at the PBE level. Targeted V ASP HSE06 calculations for
six ML-predicted compounds give material-level MAEs of 0.417, 0.182, and 0.110 eV
for the C2DB-native, Magpie+structural, and curated models, respectively;1AgBr-1
shifts above the upper gap cutoff, leaving 28 retained relaxed candidates. The workflow
shows that high-fidelity correction must be evaluated by candidate membership, not
only by global regression error.
Keywords
2D materials, C2DB, ∆-learning, HSE06 band gap, machine learning, target leakage, pho-
tocatalytic water splitting, solar hydrogen
1 Introduction
Photocatalytic water splitting is a materials route to green hydrogen because it converts
solar energy directly into chemical fuel. A useful screening candidate must satisfy electronic
constraints before more expensive calculations are justified: the gap must be large enough
for overall water splitting but still compatible with visible-light absorption, and the band
edges must straddle the water redox potentials on an absolute energy scale. 1,2 Stability,
optical absorption, carrier transport, excitonic effects, and catalytic overpotentials remain
essential later filters, but the first bottleneck is the reliable identification of semiconductors
with plausible gap and band-edge energetics. Two-dimensional (2D) materials are rele-
vant to this problem because reduced dimensionality exposes large interfacial area, shortens
carrier-transport distances, and allows electronic structure to be tuned through composition,
bonding, and dielectric environment. 3,4 Databases such as the Computational 2D Materials
Database (C2DB) enable such screening across thousands of monolayers generated with a
common first-principles workflow. 5,6
2

The database scale required for screening depends on semilocal density-functional theory,
and this creates a specific failure mode. PBE systematically underestimates semiconductor
band gaps.7 For ordinary ranking this gives a quantitative error, but near the metal–insulator
boundary it can become a classification error: a finite-gap semiconductor may be labeled
metallic and removed before any photocatalyst criterion is applied. Hybrid functionals such
as HSE06 reduce this band-gap bias for many semiconductors, 8,9 but database-wide HSE06
calculations remain too expensive for routine use. A practical screening workflow must
therefore do two things. It must recover PBE-spurious semiconductors from the nominal
metal pool, and it must correct the PBE gaps of the resulting insulating population toward
HSE06 accuracy.
∆-machine learning addresses the second task by predicting the difference between a low-
fidelity baseline and a high-fidelity reference rather than predicting the high-fidelity value
independently.10 This strategy has been applied successfully in molecular quantum chem-
istry and is now entering periodic electronic-structure workflows. Examples include HSE06
eigenvalue reconstruction from PBE inputs for crystalline compounds, 11 PBE-to-HSE06
correction for metal–nitrogen-doped graphene catalysts, 12 and OrbNet-Crystal learning of
EHSE06g −E PBEg on C2DB with HSE06-level band-gap errors near 0.12 eV. 13 These results
show that high-fidelity electronic gaps can be reconstructed from lower-cost information.
They do not, by themselves, solve the upstream population problem: a semiconductor-only
regressor cannot recover materials that PBE has already excluded as metals.
This upstream error matters for green-hydrogen photocatalyst discovery because candi-
date membership, not only regression accuracy, controls the final screen. Recent 2D pho-
tocatalyst studies combine high-throughput screening with machine-learned gaps, hybrid-
functional or many-body validation, optical descriptors, carrier-dynamics estimates, finite-
temperature tests, and electrochemical stability analysis. 14–17 In such multi-stage workflows,
the decisive question is whether the fidelity correction changes which materials pass the phys-
ically imposed thresholds. A small global mean absolute error is insufficient if the workflow
3

still removes viable materials upstream or makes incorrect decisions near the gap cutoff.
We address this issue with a leakage-aware two-stage workflow. Stage I treats PBE-
labeled metals with known HSE06 gaps as a classification problem and identifies PBE-
spurious metals using only structural, chemical, magnetic, and stability descriptors. HSE06
and GW quantities are excluded as direct target leakage, and PBE electronic quantities
are also withheld because they are target-proximal outputs of the same low-fidelity calcu-
lation being audited. 18 Stage II then reintroduces PBE electronic quantities as physically
meaningful low-fidelity inputs for HSE06–PBE ∆-learning. Thus, a descriptor that would
be an inappropriate shortcut in Stage I becomes the baseline to be corrected in Stage II.
Machine-learning classification of metals and insulators has been explored in other materials
contexts,19 but here the classifier is used specifically to repair the PBE-defined screening
population before high-fidelity gap correction.
We ask three questions. First, can PBE-spurious metallicity in C2DB be repaired without
using electronic leakage features? Second, how accurately can HSE06 band gaps be recon-
structed for the corrected insulating population by ∆-learning? Third, does the high-fidelity
correction change which 2D materials survive an electronic screen for green-hydrogen photo-
catalysis? We answer these questions by combining classification, regression, and a bounded
pH 0 water-splitting pre-screen. The resulting shortlist is a prioritized validation set for ex-
plicit HSE06 band edges, optical response, catalytic kinetics, and stability, not a final claim
of photocatalytic performance.
2 Computational Methods
2.1 Data source, labels, and dataset bookkeeping
All structures and properties were taken from C2DB. 5,6 No first-principles calculations from
the database were recomputed in the present workflow. Of the 16,905 entries in the working
C2DB snapshot, 8,686 have a reported PBE gap and form the modeling pool. UsingE PBEg <
4

0.05 eV as the operational PBE-metal criterion, this pool contains 4,351 PBE-labeled metals
and 4,335 PBE-labeled insulators.
The PBE-metal population is the focus of Stage I. Among the 4,351 PBE-labeled met-
als, 159 have an explicit HSE06 gap: 29 remain metallic at HSE06 (E HSE06g <0.05 eV),
whereas 130 become insulating (E HSE06g ≥0.05 eV). These 159 materials define the labeled
classification set, and the remaining 4,192 PBE metals constitute the unlabeled classification
target.
A separate bookkeeping point is important for the downstream screen. Across the com-
plete 8,686-material modeling pool, 3,363 entries have an explicit HSE06 gap, comprising
3,318 HSE06 insulators and 45 HSE06 metals. Because only 29 of those 45 HSE06 metals
occur in the PBE-metal labeled subset, 16 explicit HSE06 metals occur among PBE-labeled
insulators. Accordingly, whenever an HSE06 label is available it takes precedence over the
PBE label; the PBE-insulator subset is not treated as infallible. The 3,318 HSE06 insulators
form the ground-truth population for Stage II regression.
2.2 Stage-specific descriptor construction and leakage control
We compared three descriptor representations of increasing chemical and structural richness
(Table 1). The first uses C2DB-native metadata. The second contains Magpie composition
statistics generated withmatminer, together with basic lattice and density descriptors. 20,21
The third combines these branches with ionic, oxidation-state, and valence-orbital statistics
and local coordination descriptors extracted from relaxed structures usingpymatgenand the
Atomic Simulation Environment. 22,23
The raw curated representation contained 841 columns. We used pairwise Pearson cor-
relations only as a redundancy screen for this high-dimensional representation: for pairs
with|r|>0.95, we removed one member, eliminating 138 columns and leaving 703 columns
before stage-specific exclusions. The smaller C2DB-native and Magpie representations were
not correlation-pruned. The correlation structure of the compact C2DB-native classification
5

representation is shown in Figure S1 of the Supporting Information.
We made feature inclusion explicitly stage dependent. In Stage I, HSE06- and GW-
derived quantities are direct target leakage and were removed. We also withheld the PBE
gap, direct-gap flag, VBM, CBM, Fermi level, plasma frequency, and half-metal gap. These
PBE quantities do not constitute direct HSE06 target leakage, but they are target-proximal
electronic shortcuts from the same low-fidelity calculation whose metallic label is being au-
dited. Excluding them makes Stage I a chemistry/structure-based repair problem rather than
a continuation of the PBE electronic label. In Stage II, by contrast, the PBE gap, vacuum
level, Fermi level, VBM, and CBM are physically legitimate low-fidelity inputs because the
target is explicitly the HSE06 correction to PBE; only HSE06- and GW-level target quanti-
ties were excluded. This stage-specific feature policy produces 9/19 classification/regression
features for the C2DB-native representation, 141/141 for Magpie+structural, and 694/702
for the curated representation.
Table 1: Descriptor representations used in the two learning stages. Stage I excludes
HSE06/GW target information to prevent direct leakage and additionally withholds PBE
electronic quantities to avoid a low-fidelity shortcut; Stage II reintroduces PBE electronic
quantities as physically legitimate low-fidelity inputs for ∆-learning.
Representation Contents Class. Regr.
C2DB native Structural, symmetry, stability, magnetic,
and thermodynamic metadata native to
C2DB; PBE electronic quantities added
only for regression
9 19
Magpie +
structural
Composition-derived elemental statistics
(mean, range, average deviation, and
mode of atomic number, electronegativity,
valence counts, etc.) plus lattice/density
descriptors
141 141
Curated com-
bined
C2DB + Magpie branches,
ionic/oxidation-state/valence-orbital
statistics, and POSCAR-derived
coordination/bond-length descriptors;
high-dimensional representation pruned
at|r|>0.95
694 702
6

2.3 Stage I: PBE-spurious-metal versus true-metal classification
For the 159 HSE06-labeled PBE metals, the binary target wasy= 1 for a PBE-spurious
metal (E HSE06g ≥0.05 eV) andy= 0 for a true HSE06 metal (E HSE06g <0.05 eV), match-
ing the final notebook convention used to generate the confusion matrices. We used a
stratified 75/25 split (119 training, 40 test; random state 42) and compared four classi-
fiers for each descriptor representation: an RBF support-vector classifier in a standard-
ized pipeline (C= 1.0); a Random Forest with 50–100 trees, maximum depth 3–5, and
min samples leaf=5; Gradient Boosting with 50 estimators, maximum depth 3, learning
rate 0.01–0.03, andmin samples leaf=3; and XGBoost with 50 estimators, maximum depth
3, and learning rate 0.01–0.03. 24 We median-imputed missing values using statistics fitted
only on the training data.
We additionally assessed model stability by 5-fold stratified cross-validation on the train-
ing set; the complete comparison is reported in Table S1. We retained Random Forest as the
common classifier because it combines stable cross-validation behavior with the strongest or
near-strongest holdout accuracy across the descriptor sets, and because using one classifier
family keeps the representation comparison interpretable. Full holdout confusion matrices
for all four algorithms are provided in Figure S2.
We applied the selected classifier to the 4,192 HSE06-unknown PBE metals. Three
operational probability bands were used for triage using the predicted PBE-spurious-metal
probability:P spur ≥0.65 (predicted PBE-spurious metal, retained as an insulator candidate),
0.35< Pspur <0.65 (borderline, withheld from the screen), andP spur ≤0.35 (predicted true
metal). These thresholds are workflow cutoffs rather than calibrated posterior-probability
confidence intervals and are interpreted accordingly.
2.4 Stage II: HSE06–PBE∆-learning regression
The regression target was
∆Eg =E HSE06g −E PBEg ,(1)
7

and the reconstructed hybrid-functional gap was
\EHSE06g =E PBEg + d∆Eg.(2)
We split the 3,318 HSE06-insulator references 80/20 (2,654/664;random state=42) and
screened linear regression, Ridge regression (α= 1), RBF-SVR, Random Forest, Gradient
Boosting, and XGBoost. We subsequently refined XGBoost by manual hyperparameter
exploration for each representation. The final regularized models used 200 estimators/depth
3/learning rate 0.05 for C2DB-native descriptors, 1000 estimators/depth 3/learning rate
0.03 for Magpie+structural descriptors, and 1000 estimators/depth 5/learning rate 0.03 for
the curated representation; all usedsubsample=0.8,colsample bytree=0.8, and L1/L2
regularization. We implemented the models withscikit-learnand XGBoost. 24,25
We retain the fixed 80/20 split to provide a common descriptor-by-descriptor benchmark.
The available model-selection workflow does not constitute a fully nested external validation,
so the 664-material metrics are best interpreted as internal interpolation benchmarks rather
than deployment-level error estimates. For future deployment to chemically distinct material
families, repeated/nested model selection and composition- or prototype-grouped validation
would provide a more stringent estimate of extrapolative uncertainty.
2.5 Targeted first-principles validation of ML-predicted gaps
To complement the database-based test set with material-resolved validation, we performed
explicit PBE and HSE06 calculations for six compounds for which ML gap predictions were
available and the first-principles calculations were complete:1AgBr-1,1AgCl-1,1AgI-1,
1BrCu-1,1ClCu-1, and1CuI-1. The calculations were carried out with V ASP 6.4.3 using
the projector-augmented-wave method. 26–29 A plane-wave kinetic-energy cutoff of 550 eV
was used, and the Brillouin zone was sampled with Monkhorst–Pack meshes generated from
a reciprocal-space spacing of 0.003 ˚A−1. Periodic images of the monolayers were separated
8

by 15 ˚A of vacuum. PBE structural relaxations used an electronic self-consistency threshold
of 10−6 eV and were continued until all residual forces were smaller than 0.01 eV ˚A−1. The
relaxed geometries were then used for spin–orbit-coupled electronic-structure calculations.
For each material, a self-consistent PBE+SOC calculation was followed by a single-point
HSE06+SOC calculation using the standard HSE06 screened hybrid functional. The inde-
pendently recalculated PBE gaps agree closely with the corresponding C2DB PBE values
(mean absolute difference 0.023 eV; maximum difference 0.05 eV), providing a consistency
check before comparison with the new HSE06 references. The explicit HSE06 values are
used below as a prospective material-level validation set and, when a screened candidate is
affected, to update its screening status.
2.6 Stage III: electronic pre-screen for overall water splitting
We merged the Stage I and Stage II outputs after giving every explicit HSE06 label prece-
dence over its PBE label. The resulting partition contains 8,221 materials in the HSE06-
insulator screening pool (3,318 with DFT-calculated HSE06 gaps and 4,903 with ∆-learned
gaps), 57 excluded metals (45 HSE06-confirmed plus 12 predicted metals), and 408 borderline
cases. These corrected counts sum to the full 8,686-material modeling pool (Table 2).
We subjected the insulator pool to three electronic/thermodynamic filters: (i) a practical
visible-light gap window of 1.6≤E HSE06g ≤2.8 eV; (ii) a near-hull filter, usingE hull ≤
0.05 eV/atom as the strict criterion andE hull ≤0.10 eV/atom as a relaxed metastability
tolerance; and (iii) band-edge alignment with the pH 0 water redox potentials on an absolute
vacuum scale, requiringE CBM ≥ −4.44 eV for H+/H2 reduction andE VBM ≤ −5.67 eV for
O2/H2O oxidation. 30,31 The 1.6–2.8 eV interval is a screening choice intended to prioritize
visible-light absorbers and should not be confused with the 1.23 eV thermodynamic minimum
for overall water splitting.
Because the present model learns only the gap correction and not separate VBM and CBM
9

corrections, we constructed the screened band edges with a symmetric scissor approximation,
E∗VBM/CBM =E absFermi ∓ \EHSE06g 2 .(3)
This approximation treats the vacuum-referenced Fermi level as a proxy for the gap cen-
ter and opens the corrected gap symmetrically; it therefore does not capture asymmetric
HSE06 shifts of the individual band edges or uncertainty in the assumed center. The re-
sulting shortlist is therefore an electronic-structure pre-screen. Direct HSE06 band edges (or
edge-specific ∆-learning), pH dependence, kinetic overpotentials, and photo-/electrochemical
stability remain necessary validation steps.
Table 2: Dataset partition used by the corrected workflow. Explicit HSE06 labels take
precedence over PBE labels.
Quantity Count
Total C2DB entries in working snapshot 16,905
Entries with PBE gap (modeling pool) 8,686
PBE insulators (E PBEg ≥0.05 eV) 4,335
PBE metals (E PBEg <0.05 eV) 4,351
HSE06-labeled PBE metals: true / spurious 159: 29 / 130
Classification train / test 119 / 40
HSE06-unknown PBE metals classified downstream 4,192
Materials with explicit HSE06 gap (any PBE label) 3,363
HSE06 insulators / metals 3,318 / 45
∆-learning train / test 2,654 / 664
Final HSE06-insulator screening pool 8,221
DFT-HSE06 / ML-HSE06 gaps 3,318 / 4,903
Excluded HSE06-confirmed + predicted metals 57
Borderline classifier cases (withheld) 408
10

C2DB working snapshot
N= 16,905
PBE gap available
N= 8,686
PBE insulators
N= 4,335
PBE metals
N= 4,351
HSE06-labeled subset
N= 159 (29/130)
Magpie + structuralC2DB native Curated combined
4 classifiers; leakage-controlled features
CV and holdout evaluation
HSE06-unknown PBE metals
N= 4,192
Operational probability triage: insulator / borderline / metal
Figure 1: Stage I workflow for triaging PBE-predicted metals. HSE06/GW target infor-
mation is excluded to prevent direct leakage, while PBE electronic quantities are withheld
so that classification tests whether non-electronic materials information can repair the low-
fidelity metallic label. Explicit HSE06 labels anywhere in the 8,686-material pool supersede
PBE labels downstream.
11

Modeling pool
N= 8,686
HSE06-insulator pool
N= 8,221
Metals excluded
N= 57
Borderline withheld
N= 408
Ground-truth HSE06 insulators
N= 3,318; 80/20 split
HSE06–PBE ∆-regression
3 representations compared
ML-reconstructed HSE06 gaps
N= 4,903
Complete screening pool
N= 8,221
Electronic pre-screen
gap +E hull + pH 0 band alignment
Initial shortlist
10 strict / 29 relaxed
Current after targeted HSE: 10 / 28
Figure 2: Stages II–III: ∆-learning of the HSE06–PBE band-gap correction followed by the
water-splitting electronic pre-screen. The initial screen yields 10 strict and 29 relaxed can-
didates. Subsequent targeted HSE06 validation removes one relaxed candidate (1AgBr-1),
giving a current retained set of 10 strict and 28 relaxed materials.
12
