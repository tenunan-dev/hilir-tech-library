---
source_id: "arxiv"
title: "IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 1"
url: "https://arxiv.org/abs/2609.12408"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.12408. Abstract: IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 1
GSO-Net: Visual State Machines for Hazardous
Freight Transfer Compliance at Petrochemical
Logistics Nodes
Yu Xie1, Bangshu Xiong 1∗, Zhibo Rao 1, Rui Gan 2, Chongxuan Liu 2, and Zechu Ouyang 2
Abstract—Hazardous-freight operations at petrochemical lo-
gistics nodes are safety-critical for intelligent transportation
systems, yet existing vis"
---

# IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 1

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 1
GSO-Net: Visual State Machines for Hazardous
Freight Transfer Compliance at Petrochemical
Logistics Nodes
Yu Xie1, Bangshu Xiong 1∗, Zhibo Rao 1, Rui Gan 2, Chongxuan Liu 2, and Zechu Ouyang 2
Abstract—Hazardous-freight operations at petrochemical lo-
gistics nodes are safety-critical for intelligent transportation
systems, yet existing vision benchmarks rarely address pro-
cedural compliance under realistic deployment constraints. In
large infrastructure networks, cameras often operate under
sparse round-robin polling, so transfer status must be inferred
from incomplete observations and localized evidence. We present
GSO-Net, a large-scale benchmark for visual understanding of
standard operating procedures (SOPs) in petrochemical unload-
ing scenarios. To our knowledge, GSO-Net is the first public
benchmark dataset dedicated to visual SOP understanding in
petrochemical hazardous-freight transfer scenarios. It contains
over 50,000 independently sampled frames from 64 real ex-
pressway petrochemical logistics nodes and adopts an SOP-
derived hierarchy linking 9 macroscopic procedural steps with
15 microscopic operational states. Two tasks are defined: joint
detection of microscopic states and macroscopic steps as the
core benchmark, and frame-level step classification as a di-
agnostic reference. Experiments with lightweight, transformer-
based, open-vocabulary, and holistic models reveal a clear gap
between object perception and transfer-stage understanding.
Current models remain weak on contact-level state grounding,
transient step recognition, and stage consistency, especially under
sparse polling, tiny critical targets, and long-tailed operational
evidence. GSO-Net provides a practical benchmark for fine-
grained state perception and vision-based safety monitoring
in hazardous freight transportation. The dataset is publicly
available at https://github.com/yuxieHarrison/GSO-Net.
Index Terms—Computer vision, Methods for safety, Freight
transportation and logistics, Road transportation, hazardous
freight transfer, benchmark dataset.
I. INTRODUCTION
T
HE safe transportation of hazardous freight is fundamen-
tal to transportation safety. Along expressway corridors,
oil transport and unloading are essential to highway service
support and petrochemical logistics. In such scenarios, tanker
vehicles must follow a regulated SOP covering grounding, fire
protection, hose connection, supervision, and disengagement.
Any omission or violation may cause serious risks such as
leakage, fire, or explosion. Automated SOP monitoring is
therefore important for hazardous freight transportation safety.
Practical deployment differs from standard vision settings.
Large infrastructure networks often monitor fixed camera feeds
1Yu Xie, Bangshu Xiong, and Zhibo Rao are with the School of Information
Engineering, Nanchang Hangkong University, Nanchang 330063, China (e-
mail: xieyuharrison@163.com; xiongbs@126.com; raoxi36@foxmail.com).
2Rui Gan, Chongxuan Liu, and Zechu Ouyang are with Jiangxi Ex-
pressway Petrochemical Co., Ltd., Nanchang 330063, China (e-mail:
2362762050@qq.com; 1040345268@qq.com; oyzcjxja@126.com).
∗Corresponding author: Bangshu Xiong.
Temporal Workflow Context  ＆  Fine-Grained  StatesSpatial Perception Labels
staff
fire extinguisher
static clamp
oil tanker
oil discharge
 fire extinguisher
static clamp
oil tanker(stopped+is_working)
oil discharge
staff（standing）
Step 6 Supervision
(deployed)
(connected)
(connected)
Fig. 1. Comparison of annotation paradigms.Left (existing paradigm):
Traditional object detection identifies generic object categories but does not
explicitly represent operational stages or states.Right (GSO-Net paradigm):
GSO-Net organizes macroscopic procedural tags (S macro) together with
microscopic interactive states (E micro), enabling state-aware analysis of
hazardous freight-transfer scenarios at petrochemical logistics nodes.
simultaneously, so they rely onround-robin visual polling. In
practice, each logistics node is typically observed for only
3–5 s before switching to the next logistics node. The key
challenge is not dense video understanding. It is reliable
transfer-stage inference from sparse visual evidence.
This setting pushes the task beyond conventional object
detection. The goal is not only to recognize visible objects.
It is to determine procedural status from small visual cues
across a hazardous freight-transfer scene in real deployments.
Existing benchmarks do not fully capture this requirement.
Most anomaly datasets, such as MVTec AD [1] and VisA
[2], focus on appearance defects. Safety and transportation
datasets, such as PPE benchmarks [3] and traffic-scene datasets
[44], [45], verify the presence of objects or scene elements, but
not whether a hazardous transfer procedure is being executed
in the correct stage of a logistics node.
As illustrated in Fig. 1, object-centric perception is not
sufficient for SOP-aware state understanding. Infrastructure-
side compliance analysis must infer operational progress and
procedural correctness from distributed visual evidence. This
shift introduces three structural challenges:
•Spatiotemporal aliasing:Adjacent workflow steps often
share nearly identical global layouts, and their differences
are confined to subtle local changes.
•Extreme foreground-background imbalance:Critical
contact states may occupy only a few pixels in large
scenes and are easily degraded by occlusion, illumination
variation, and viewpoint shift.
•Weak procedural priors in generic pre-training:Foun-
dation models provide strong semantic transfer across
domains, but they do not explicitly encode hazardous-
freight procedures or transfer-stage logic in practice.
arXiv:2609.12408v1  [cs.CV]  11 Sep 2026

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 2
These challenges suggest that infrastructure-side monitoring
of hazardous freight transfer should be studied as a hierarchical
state-understanding problem rather than as a pure detection
task. A practical system must detect local entities, infer their
functional states, and relate these cues to a broader transfer
stage under sparse and intermittent observations.
To this end, we introduceGSO-Net, a benchmark for visual
SOP understanding at petrochemical logistics nodes under
sparse polling in real deployments. GSO-Net translates SOP
rules into structured visual annotations by directly linking
macroscopic procedural steps with microscopic operational
states. It targets an underexplored setting where hazardous
freight-transfer understanding depends on joint modeling of
workflow order and localized functional states.
The main contributions are as follows:
1) To our knowledge, we presentGSO-Net,the first
publicly available dataset and benchmarkfor visual
SOP understanding in petrochemical hazardous freight-
transfer scenarios. It contains more than 50,000 indepen-
dently sampled frames from 64 unconstrained logistics
nodes in real-world infrastructure settings.
2) We propose ahierarchical annotation framework
coupling 9 macroscopic procedural steps with 15 micro-
scopic operational states. It translates SOP descriptions
into explicit visual evidence. This enables stage-aware
understanding in petrochemical transfer scenarios.
3) We establish abenchmark protocol. It centers on
joint step-state detection. It is complemented by frame-
level step classification. We also provide lightweight,
transformer-based, open-vocabulary, and holistic base-
lines forsystematic and comprehensiveevaluation.
4) We provideempirical analysis. It reveals the limitations
of current architectures. These limitations arise under
sparse polling, tiny safety-critical cues, and long-tailed
operational evidence. Our analysis thereby highlights
the practical challenges of visual SOP understanding in
petrochemical logistics nodes.
II. RELATEDWORK
GSO-Net targets visual SOP understanding for hazardous
freight transfer at petrochemical logistics nodes under sparse
infrastructure-side polling. It builds on related efforts in safety
monitoring, procedural understanding, and fine-grained visual
perception, while aiming to fill a gap at their intersection:
explicit workflow order, localized operational states, and SOP-
oriented supervision under sparse observations. To make these
differences explicit, Table I compares representative bench-
marks with GSO-Net along these three dimensions.
A. Benchmarks for Safety Monitoring and Procedural Com-
pliance
Existing public benchmarks for safety monitoring usually
focus on abnormality, object presence, or violation detec-
tion rather than SOP understanding. In industrial inspection,
datasets such as VisA [2], MVTec LOCO AD [14], MVTec
3D-AD [15], Eyecandies [16], Real-IAD [6], Real3D-AD [7],
Real-IAD D 3 [10], M3-AD [13], and MVTec AD 2 [12]
mainly study whether an object, part, or scene is defective or
anomalous. These datasets are valuable for inspection-oriented
perception, but their supervision centers on defectiveness
rather than operational correctness. A frame may be visually
normal in such benchmarks yet still correspond to an incorrect
stage in a hazardous freight-transfer procedure.
Safety-oriented datasets are closer to our application set-
ting, but they still do not capture the supervision structure
required in our problem. PPE benchmarks [3] focus on worker
protection and equipment presence, while transportation-side
benchmarks such as TrafficCAM [44], ParallelEye [45], and
V oxelScape [46] cover fixed-camera traffic flow segmentation,
synthetic traffic-scene generation, and simulated 3D traffic
perception. These datasets are valuable for traffic-scene per-
ception and infrastructure-side monitoring, but they still focus
on traffic participants, scene elements, or general perception
targets rather than node-level procedural compliance. In these
settings, the key question is typically whether a target object
or scene element is present. In contrast, the critical question in
hazardous freight transfer is whether grounding, extinguisher
deployment, hose connection, personnel supervision, and dis-
engagement occur at the correct procedural stage.
Therefore, the main gap in existing benchmarks is not sim-
ply scene domain, but supervision structure. Prior datasets do
not provide a public benchmark that jointly models workflow
order, localized operational states, and SOP-oriented com-
pliance in petrochemical hazardous freight-transfer scenarios.
GSO-Net addresses this gap by explicitly linking macroscopic
procedural stages with microscopic state annotations in a real
infrastructure-side transportation setting.
B. Procedural Understanding Under Sparse Infrastructure
Observation
Procedural understanding has been extensively studied in
video understanding and workflow analysis. Benchmarks such
as Assembly101 [4], EPIC-KITCHENS-100 [18], Ego4D [19],
HD-EPIC [21], MLVU [20], and OpenPack [9] provide rich
supervision for action recognition, anticipation, temporal pars-
ing, and long-horizon activity understanding. These works
have substantially advanced procedural reasoning, especially
in environments where temporal continuity is strong and
activities can be observed through dense sequential evidence.
However, this assumption does not hold in our deployment
setting. In large infrastructure networks, many fixed cameras
must share limited computational and transmission resources,
so monitoring systems often rely on round-robin polling rather
than continuous observation. Under this regime, each logistics
node is observed only intermittently, and critical procedural
transitions may appear in only one or two frames. As a
result, stage recognition cannot depend on dense motion cues,
temporal tracking, or long contiguous clips in the way that
many existing procedural benchmarks assume.
This distinction is fundamental. GSO-Net is not designed
for dense activity parsing from continuous video, but for pro-
cedural inference from sparse infrastructure observations. The
model must recover workflow stage from incomplete visual
evidence and small operational cues, rather than from stable

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 3
TABLE I
COMPARISON OFGSO-NET WITH REPRESENTATIVE RELATED BENCHMARKS. EXISTING DATASETS TYPICALLY EMPHASIZE ONLY ONE ASPECT OF THE
PROBLEM,SUCH AS ANOMALY CUES,WORKFLOW ORDER,OR SAFETY-OBJECT PERCEPTION. BY CONTRAST, GSO-NET JOINTLY MODELS WORKFLOW
ORDER AND LOCALIZED OPERATIONAL STATES FOR HAZARDOUS FREIGHT-TRANSFERSOPUNDERSTANDING AT PETROCHEMICAL LOGISTICS NODES
UNDER SPARSE VISUAL POLLING.
Dataset Venue Focus Scale Supervision Order States SOP
ParallelEye [45] T-ITS’19 Virtual traffic-scene
perception
40,251 images Multi-task dense annotations× × ×
Assembly101 [4] CVPR’22 Procedural activity
understanding
4,321 videos /
>1M segments
Dense temporal action annotations✓× ×
VisA [2] ECCV’22 Multi-instance
anomaly detection
10,821 images Image-/pixel-level anomaly labels× × ×
MVTec LOCO AD
[14]
IJCV’22 Structural and logical
anomaly detection
3,644 images Image-/pixel-level anomaly labels× × ×
MVTec 3D-AD [15] VISAPP’22 3D anomaly detection 4,147 depth maps
/ point clouds
Pixel-precise anomaly annotations× × ×
Eyecandies [16] ACCV’22 Multimodal anomaly
detection
10 categories /
RGB-D
Image-/pixel-level anomaly labels× × ×
V oxelScape [46] T-ITS’23 Simulated 3D traffic
perception
100K point-cloud
scans
Point-wise labels + 3D boxes× × ×
OpenPack [9] PerCom’24 Industrial workflow
recognition
53.0 hours /
20,129 labels
Multimodal operation annotations✓× ×
Real-IAD [6] CVPR’24 Real-world multi-view
anomaly detection
150K images / 30
objects
Image-/pixel-level anomaly labels× × ×
MMAD [11] ICLR’25 Industrial multimodal
reasoning
8,366 images /
39,672 QAs
QA-style multimodal annotations× × ×
TrafficCAM [44] T-ITS’25 Fixed-camera traffic
flow segmentation
4,364 labeled +
58,689 unlabeled
frames
Pixel-/instance-level annotations× × ×
MVTec AD 2 [12] IJCV’26 Advanced anomaly
detection
8 scenarios /
8,000+ images
Image-/pixel-level anomaly labels× × ×
GSO-Net (Ours) 2026 Hazardous
freight-transfer SOP
understanding
50,325 frames /
321,432 boxes
Macro-step labels + micro-state
boxes
✓ ✓ ✓
Note:“Order” indicates whether workflow order is an explicit target. “States” indicates whether localized functional states are explicitly annotated or
evaluated. “SOP” indicates whether the benchmark is explicitly designed for hazardous procedural understanding.
temporal evolution. Existing procedural benchmarks therefore
provide important conceptual context, but do not capture the
sparse, discontinuous observation regime that characterizes
infrastructure-side hazardous freight monitoring.
C. Fine-Grained State for Stage-Aware SOP Analysis
A second challenge of our setting is that procedural un-
derstanding depends on fine-grained operational evidence.
Modern detection methods, including Faster R-CNN [25],
DETR [27], DINO [30], RT-DETR [31], Relation DETR [32],
Hyper-YOLO [33], Mr. DETR [34], and RF-DETR [35],
have substantially improved localization and representation
learning. Transportation studies such as CLPD [47], SGV3D
[48], V oxelScape [46], and infrastructure-side point cloud
detection research [49] further show how perception systems
must adapt to realistic deployment conditions, while tiny-
object benchmarks such as CST Anti-UA V [5] and recent T-
ITS analysis of image- and video-based small object detection
[50] highlight the fragility of small-target recognition under
severe scale compression. These works are highly relevant
because decisive visual evidence in petrochemical unloading
scenes, such as clamp status or hose connection status, is often
tiny, localized, and easily degraded.
Recent foundation and open-vocabulary models further
strengthen semantic transfer. CLIP [36], GLIP [37], Grounding
DINO [38], YOLO-World [39], LLMDet [40], Dynamic-
DINO [41], and OW-OVD [42] improve phrase-level ground-
ing and category generalization, while DINOv2 [51],
Qwen2.5-VL [52], InternVL3 [53], AnomalyGPT [17], and
MMAD [11] provide stronger visual or multimodal priors
for inspection-oriented reasoning. Part-aware annotations in
PACO [43], together with fine-grained traffic-scene bench-
marks such as TrafficCAM [44] and ParallelEye [45], also
point toward more detailed visual perception.
However, stronger perception alone is insufficient for GSO-
Net. Object recognition does not directly resolve whether
local operational states are functionally valid or procedurally
consistent with the current workflow stage. In our setting,
microscopic state grounding and macroscopic stage inference
are tightly coupled. The core challenge is to bridge localized
semantic evidence and global procedural awareness, enabling
a transition from microscopic cue understanding to macro-
scopic state cognition. Existing perception models improve
localization and semantic transfer, but they do not explicitly
evaluate or supervise this relationship under sparse polling.
GSO-Net is designed to make this gap measurable through
unified annotations and evaluation.

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 4
S1:ENTRY S2:PROTECT S3:CHECK S4:CONFIRM S5:UNLOAD S6:SUPERVISE S7:ACCEPT S8:FINISH
Rainy
Sunny
Snowy
Occlusion
Night
Near View
Far View
Cloudy
Fig. 2. Overview of the GSO-Net benchmark. The dataset matrix summarizes the diversity of GSO-Net across illumination conditions (day and night),
weather conditions (rain and snow), dynamic occlusions, and the chronological progression of the 9 macroscopic SOP steps in petrochemical freight-transfer
operations.
III. GSO-NETCONSTRUCTION ANDANNOTATION
PROTOCOL
This section describes the construction of GSO-Net. Our
goal is to translate SOP rules for petrochemical freight-transfer
operations into a computable visual benchmark. As shown in
Fig. 2, GSO-Net covers substantial diversity in stage, weather,
illumination, viewpoint, and occlusion.
A. SOP Taxonomy and Hierarchical Semantic Mapping
Industrial SOPs are designed to reduce operational risk
under strict physical and procedural constraints. We translate
these textual procedures into a hierarchical taxonomy, shown
in Table II. This taxonomy links continuous workflow phases
to explicit and interpretable visual evidence.
Level 1: Macroscopic procedural steps (S macro).We
partition the unloading workflow into nine discrete and chrono-
logically dependent phases (S0 toS 8). Each phase corresponds
to a distinct operational stage and a distinct safety requirement.
•S 0: Idle.The logistics node is in an idle state, and no
unloading operation is active.
•S 1: Entry.The oil tanker arrives and enters the operating
zone.
•S 2: Safety protection.Grounding and fire-protection mea-
sures are deployed before unloading begins.
•S 3: Safety check.Personnel verify that the deployed
safety measures are correctly positioned and accessible.
•S 4: Pre-unload confirm.The unloading hose is positioned
near the discharge port, but fuel transfer has not started.
•S 5: Oil unloading.The unloading hose is physically
connected to the tanker port, and fuel transfer is in
progress.
•S 6: Supervision.Fuel transfer is underway, and personnel
remain on site for supervision.
•S 7: Receipt acceptance.Fuel transfer completion is ver-
ified, and the hose is disconnected and drained.
•S 8: Post-processing.The oil tanker departs, and the
logistics node returns to the idle state.
Level 2: Microscopic operational states (E micro).We
ground the procedural description into bounding-box annota-
tions and define 15 fine-grained operational states, such as
clamp connectedanddischarge disconnected. These states
provide visual evidence for stage understanding.
B. Step-State Correspondence Derived from SOPs
A central design principle of GSO-Net is the correspon-
dence between macroscopic steps and microscopic states. This
correspondence is directly derived from SOP documents and
operational practice. It is used to organize the annotation
system and interpret stage-specific visual evidence.
At the macroscopic level, each frame is assigned one of
the 9 procedural steps. At the microscopic level, the frame is
annotated with visible state-specific objects and interactions.
The two levels are related by operational meaning rather than
by a formally defined rule engine. In other words, we do
not define a complete logical protocol, symbolic solver, or
explicit constraint-based evaluation metric. Instead, we use

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 5
TABLE II
HIERARCHICAL TAXONOMY AND SEMANTIC DEFINITIONS OF MICROSCOPIC STATES(E micro)INGSO-NET.
Entity Category Micro-State Label Semantic Operational Significance
Oil Tanker00: tanker moving trueHigh-risk anomaly:Unauthorized vehicle displacement during active fluid transfer, with elevated
risk of structural failure or leakage.
01: tanker moving falseStandard transit:Vehicle in motion for entry, exit, or positioning, without active discharge.
02: tanker stopped trueActive transfer:Stationary vehicle during ongoing fuel discharge.
03: tanker stopped falseIdle/standby:Stationary vehicle without active discharge.
Personnel04: staff standingSupervision:On-site personnel monitoring the operational state.
05: staff bendingAuxiliary inspection:Personnel adjusting or checking components outside the discharge action.
06: staff walkingTask transit:Personnel moving toward a specific operational or safety-related task.
07: staff operatingActive interaction:Direct manual engagement with mechanical systems.
Static Clamp08: clamp connectedValidated grounding:Physical grounding is visibly established.
09: clamp disconnectedSafety violation:Grounding is absent during hazardous operation.
10: clamp floatingGrounding procedure:Personnel are deploying or adjusting the static clamp.
Extinguisher11: extinguisher deployedSafety readiness:Fire suppression equipment is positioned at the required safety point.
12: extinguisher carriedManual transit:Fire suppression equipment is being moved by personnel.
Oil Discharge13: discharge connectedSecured interface:The discharge hose is mechanically connected at the port.
14: discharge disconnectedDisengaged interface:The discharge hose is visibly disconnected from the port.
SOPs to guide the hierarchical label design and the semantic
interpretation of the full dataset.
For example, theContinuous Supervisionstage is typi-
cally associated with states such asclamp connected,dis-
charge connected, and the visible presence of on-site person-
nel. Similarly, pre-unloading and post-processing stages are
characterized by different local state combinations and differ-
ent operational focus. These correspondences help explain why
stage recognition in GSO-Net depends on small and localized
evidence rather than on global scene layout alone.
This design choice is important. It keeps the dataset faithful
to what is actually annotated. GSO-Net provides a structured
benchmark for hierarchical SOP understanding. It does not
claim to implement a full logic-verification protocol. Instead,
it offers a benchmark foundation on which future work may
build more explicit reasoning or verification modules.
C. Independent Frame Sampling and Environmental Complex-
ity
To reflect practical deployment, data collection was con-
ducted at scale. We sourced surveillance feeds from 64 active
expressway petrochemical logistics nodes over eight months.
We did not extract continuous high-frame-rate clips. Instead,
we adopted an independent frame-sampling strategy. This
design matches the round-robin visual polling widely used in
practical infrastructure-side edge systems.
These logistics nodes are not controlled laboratory envi-
ronments. They are unconstrained real-world logistics nodes.
The dataset therefore includes strong diurnal changes, seasonal
variation, and adverse weather. A substantial portion of the
dataset comes from night scenes and non-ideal weather con-
ditions. From the full surveillance pool, we curated more than
50,000 high-fidelity frames. This design reduces site-specific
bias and discourages simple background memorization.
D. Annotation Procedure and Quality Assurance
The annotation process was carried out over four months
by the core team of the smart logistics node project. All
labeling rules were derived from operational procedures used
in frontline petrochemical unloading. To improve annota-
tion reliability, a three-stage quality-assurance protocol was
adopted.
Stage 1: State-aware bounding-box annotation.All crit-
ical entities and operational states were manually annotated
at the bounding-box level. During this stage,functional en-
gagementwas explicitly distinguished fromspatial proximity.
For example, a grounding clamp was labeled as “connected”
only when the visible evidence supported an actual mechanical
connection rather than mere spatial closeness to the tanker.
Stage 2: Frontline expert verification.Because several
microscopic states are visually subtle and operationally sensi-
tive, targeted verification was performed with experienced gas
station operators. Ambiguous samples were reviewed against
real operational practice to ensure that the assigned labels
remained consistent with actual procedural meaning.
Stage 3: Multi-round semantic and procedural review.
After the initial annotation and expert verification, the labels
were further reviewed for semantic consistency and procedural
interpretability. Special attention was given to whether micro-
scopic states were supported by visible evidence and whether
macroscopic step labels were compatible with the observed
operational context. Importantly, this review did not enforce
that every sample satisfy an ideal SOP-compliant state. Sam-
ples showing unsafe, anomalous, or non-compliant operations
were intentionally retained when such conditions were clearly
visible. Samples with uncertain labels, inconsistent criteria, or
difficult visual evidence were returned for group discussion
and manual revision until a consensus label was reached.
This protocol ensures that the benchmark faithfully reflects
visible operational evidence, real procedural context, and

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 6
TOTAL
SAMPLES
50,325
Category Legend
Oil Tanker
Staff
Static Clamp
Oil Discharge
Fire Extinguisher
Total Temporal Volume
S0: IDLE
N=1,444 (2.9%) S1: ENTRY
N=3,885 (7.7%)
S2: PROTECT
N=2,050 (4.1%)
S3: CHECK
N=3,669 (7.3%)
S4: CONFIRM
N=4,749 (9.4%)S5: UNLOAD
N=6,271 (12.5%)
S6: SUPERVISEN=19,943 (39.6%)
S7: ACCEPT
N=4,317 (8.6%)
S8: FINISH
N=3,997 (7.9%)
(a)Macroscopic Spatiotemporal Density
Tanker Mov(T)Tanker Mov(F)Tanker Stop(T)Tanker Stop(F)
Staff StdStaff BendStaff WalkStaff OpClamp ConnClamp DisconnClamp FloatExting DepExting CarDischarge ConnDischarge Disconn
Microscopic Entity States (Emicro)
S0 Idle
S1 Entry
S2 Safety Protection
S3 Safety Check
S4 Pre Unload Confirm
S5 Oil Unloading
S6 Supervision
S7 Receipt Acceptance
S8 Post Processing
Macroscopic Temporal Steps (Smacro)
0.0
0.2
0.4
0.6
0.8
1.0
P(Emicro ∣ Smacro)
(b)Step-State Co-occurrence
20%
40%
Tanker Mov(T)
Tanker Mov(F)
Tanker Stop(T)
Tanker Stop(F)
Staff Std
Staff Bend
Staff Walk
Staff OpClamp Conn
Clamp Disconn
Clamp Float
Exting Dep
Exting Car
Discharge Conn
Discharge Disconn
Temporal Visual Focus Shift (Fstep)
SOP Steps
S0 Idle
S1 Entry
S2 Safety Protection
S3 Safety Check
S4 Pre Unload Confirm
S5 Oil Unloading
S6 Supervision
S7 Receipt Acceptance
S8 Post Processing
(c)Temporal Focus Shift
Fig. 3. Macroscopic and state-aware dynamics of GSO-Net.(a)Spatiotemporal density across the operational lifecycle.(b)Conditional probability heatmap
P(E micro |S macro), showing the correspondence between macro steps and micro states.(c)Temporal focus fingerprints, showing how semantic focus
shifts across adjacent SOP phases.
practically relevant abnormal cases rather than only idealized
SOP-compliant operational settings.
E. Dataset Characteristics and Structural Difficulty
Statistical analysis further shows that GSO-Net is inherently
challenging in several dimensions.
As summarized in Fig. 3, GSO-Net exhibits coupled macro-
scopic and microscopic structure across the SOP lifecycle.
Operational lifecycle structure.Fig. 3a shows strong
variation across the workflow timeline. Long-duration standby
and supervision stages dominate the temporal distribution.
Long-tailed microscopic distribution.Fig. 4 shows
that GSO-Net exhibits a pronounced long-tail distribution.
Frequent states, such astanker stopped trueandextin-
guisher deployed, contain many instances, whereas safety-
critical interaction states, such asclamp floatingand
clamp disconnected, are rarer. StepS 6 contributes the most
samples because fuel transfer lasts longer than the prepara-
tory and post-processing stages. This realistic imbalance also
makes the benchmark challenging for generic detectors.
Step-state correspondence.Fig. 3b visualizes the empirical
relationship betweenS macro andE micro, showing that specific
microscopic states cluster around specific procedural stages.
Temporal focus shift.Fig. 3c shows that adjacent SOP
phases may share similar global views while differing in
localized operational evidence. The model therefore needs
dynamic semantic focus rather than global scene matching.
F . Dataset Statistics
We summarize the benchmark with statistics in Tables III
and IV. Table III reports counts of all 15 microscopic states in
the training and validation sets. The numbers confirm the long-
tail nature of GSO-Net. Head classes such asstaff standing
andextinguisher deployedhave tens of thousands of instances,
whereas tail classes such asclamp floatingandstaff bending
contain fewer than 1,100.
Table IV summarizes the environmental and spatial diversity
of GSO-Net. The benchmark contains 50,325 curated frames
from 64 independent logistics nodes, with clear daylight
accounting for only 42.2% of the data. The remaining frames
cover night scenes, adverse weather, viewpoint variation, and
heavy occlusion, supporting evaluation under realistic degra-
dation rather than controlled-scene pattern matching.
G. Ethical Compliance and Data Integrity
Data collection was conducted within the authorized scope
of our smart logistics node project. All video feeds were
acquired through standard workplace safety monitoring sys-
tems. To preserve operational fidelity, we retained original

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 7
Exting DepStaff WalkStaff Std Staff OpStaff Bend
0
20
40
60
80
100
120
140
160
Instance Count
S0: IDLE
Tanker IdleStaff StdExting DepStaff WalkStaff OpClamp DiscHose DiscTanker StopExting Car
0
500
1000
1500
2000
2500
3000
3500
4000 S1: ENTRY
Staff Op
Tanker StopStaff WalkExting DepClamp FloatStaff StdExting CarClamp ConnStaff BendHose ConnHose DiscTanker IdleClamp Disc
0
500
1000
1500
2000 S2: PROTECT
Staff OpExting DepTanker StopClamp ConnStaff WalkHose DiscExting CarStaff StdClamp FloatHose ConnClamp Disc
0
1000
2000
3000
4000
5000Instance Count
S3: CHECK
Exting DepStaff OpTanker StopClamp ConnHose DiscStaff WalkStaff StdExting CarHose ConnStaff BendTanker WorkClamp Float
0
2000
4000
6000
8000
10000
12000
14000
S4: CONFIRM
Exting DepStaff OpClamp ConnHose ConnTanker WorkHose DiscStaff StdTanker StopStaff WalkExting CarStaff Bend
0
2500
5000
7500
10000
12500
15000
17500
S5: UNLOAD
Exting DepStaff StdHose ConnTanker WorkClamp ConnStaff WalkStaff OpExting CarStaff BendTanker StopClamp FloatHose Disc
0
10000
20000
30000
40000
50000Instance Count
S6: SUPERVISE
Exting DepStaff OpClamp ConnHose ConnTanker WorkStaff StdTanker StopStaff WalkHose DiscExting CarTanker IdleClamp FloatTanker MovClamp Disc
0
2000
4000
6000
8000
10000
12000
S7: ACCEPT
Exting DepStaff OpTanker IdleTanker StopStaff WalkStaff StdExting CarClamp ConnClamp DiscClamp FloatHose DiscHose ConnStaff BendTanker Work
0
2000
4000
6000
8000 S8: FINISH
Fig. 4. Microscopic scale imbalance in GSO-Net. The entity distribution is strongly long-tailed across the 9 SOP stages. Static and frequent states dominate
the benchmark, while safety-critical interaction states appear much less often. StepS 6 contributes the largest number of samples because it corresponds to
the longest operational phase. This distribution makes the benchmark difficult for standard detectors, especially on rare but safety-critical categories.
TABLE III
BOUNDING-BOX INSTANCE DISTRIBUTION ACROSS THE TRAINING AND
VALIDATION SETS FOR THE15MICROSCOPIC STATES INGSO-NET.
Microscopic State (E micro) Train Val Total
tanker moving true 4 0 4
tanker moving false 4,646 1,130 5,776
tanker stopped true 21,736 4,899 26,635
tanker stopped false 12,961 3,033 15,994
staff standing 34,141 7,907 42,048
staff bending 427 305 732
staff walking 9,847 2,405 12,252
staff operating 28,301 6,187 34,488
clamp connected 27,668 6,616 34,284
clamp disconnected 509 7 516
clamp floating 1,004 92 1,096
extinguisher deployed 88,430 18,641 107,071
extinguisher carried 3,977 337 4,314
discharge connected 22,353 4,931 27,284
discharge disconnected 7,638 1,300 8,938
Total Boxes 263,642 57,790 321,432
image frames during dataset construction. The acquisition,
annotation, and release pipeline follows local industrial data-
governance requirements and project-level ethical constraints.
TABLE IV
DISTRIBUTION OF FRAMES ACROSS ENVIRONMENTAL CONDITIONS,
VIEWPOINTS,AND VISUAL CHALLENGES INGSO-NET.
Condition / Viewpoint # Nodes # Images Percentage
Daylight (Clear) 27 21,215 42.2%
Night 9 6,058 12.0%
Near View 8 7,029 14.0%
Far View 7 6,085 12.1%
Snow & Cloud 5 3,426 6.8%
Rain 4 2,907 5.8%
Occlusion 4 3,605 7.2%
Total 64 50,325 100.0%
IV. EXPERIMENTS ANDANALYSIS
We evaluate GSO-Net as a benchmark rather than a task-
specific method. The experiments test whether current models
can recover procedural meaning from localized evidence under
sparse visual polling at hazardous freight logistics nodes. Two
tasks are considered.Task 1is the core benchmark and eval-
uates joint detection of microscopic states and macroscopic
steps.Task 2is a diagnostic reference that evaluates frame-
level classification of macroscopic SOP steps without explicit
state grounding. Together, these tasks expose the effects of
sparse polling, long-tailed states, small critical targets, and
stage-sensitive visual evidence.

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 8
A. Benchmark Protocol and Experimental Setup
A strictcross-node splitis adopted. Random frame-level
splitting is not used because it introduces scene leakage and
allows models to memorize node-specific backgrounds. The
training set contains 40,976 images from 51 logistics nodes.
The validation set contains 9,349 images from 13 unseen
logistics nodes. This protocol measures generalization to new
nodes rather than memorization within the same logistics node.
Two benchmark tasks are defined. The distinction is in-
tentional: Task 1 evaluates the full hierarchical formulation
of GSO-Net, whereas Task 2 quantifies the limitations of
transfer-stage recognition when localized state evidence is not
explicitly modeled in holistic prediction.
Task 1: Joint detection.Each detector predicts 24 cat-
egories in a unified label space, including 15 microscopic
states and 9 macroscopic procedural steps. The microscopic
states use their original bounding-box annotations, while the
macroscopic steps are represented as full-frame targets. Thus,
AP for microscopic states evaluates localized state detection,
whereas AP for macroscopic steps evaluates image-level step
recognition. Performance is measured byAP 50,AP 50-95, and
scale-aware metricsAP S,AP M , andAP L. Since the unified
label space contains both localized and full-frame targets,
the scale-aware metrics should be interpreted with care. This
is the main evaluation because GSO-Net focuses on stage
understanding together with localized operational evidence
under sparse infrastructure-side observation.
Task 2: Frame-level step classification.Each classifier
assigns one of the 9 macroscopic SOP steps to each full image
based on global visual evidence. Performance is evaluated
using Top-1 Accuracy, Top-5 Accuracy, and Macro F1. This
task is weaker than Task 1 and serves as a diagnostic reference
for node-level stage recognition from holistic appearance,
without explicit modeling of localized states.
All experiments were conducted within a unified PyTorch
framework on a server equipped with eight NVIDIA GeForce
RTX 3090 GPUs (24 GB VRAM each). All reported baselines
were trained solely on GSO-Net without supplementary indus-
trial data. For YOLO-based detection models, training was per-
formed for 100 epochs with input resolution640×640. Other
state-of-the-art detection models were trained and evaluated
using the default resolutions and hyperparameters specified
in their official codebases. For classification networks, input
resolutions varied according to the backbone, as detailed in
Table VIII. Unless otherwise specified, all methods followed
their official implementations and default configurations.
B. Task 1: Joint Detection of Microscopic States and Macro-
scopic Steps
Task 1 is the main benchmark task of GSO-Net. It tests
whether a detector can recover procedural meaning from
sparse local evidence under a unified step-state formulation.
The challenge is twofold. First, microscopic states and macro-
scopic steps differ sharply in spatial scale: decisive evidence is
often confined to tiny contact regions, whereas the step target
spans the full frame. Second, stage recognition depends on
localized functional cues rather than only global scene layout.
Small Medium Large0
20,000
40,000
60,000
80,000
100,000
120,000Number of Instances
49447
110025
104170
11932
23695 22163
(a) Micro-Entity Scale
Training Set
Validation Set
1920 x 10802560 x 14401280 x 7202688 x 15202304 x 1296
0
5,000
10,000
15,000
20,000
25,000
30,000
35,000
40,000Number of Images
27074
6980
4367
2151
404
5343
1978 942 1086
(b) Image Resolution
Train
Val
Fig. 5. Scale disparity and input diversity in GSO-Net.Left:Bounding-box
area distribution under the COCO size protocol. Safety-critical operational
cues are heavily concentrated in the extremely small-object regime.Right:
Resolution distribution of the raw surveillance frames. The benchmark com-
bines multi-megapixel inputs with tiny state indicators, which makes precise
localization difficult under practical resizing constraints.
TABLE V
TASK1RESULTS ON LIGHTWEIGHT DETECTORS(%).
Model Size Ep. Params(M) AP 50 AP50−95 APS APM APL
YOLOv8-n [54] 640 100 3.01 42.1 35.0 3.2 11.6 33.6
YOLOv9-t [55] 640 1001.98 44.0 36.53.0 13.1 33.5
YOLOv10-n [56] 640 100 2.27 37.5 31.4 3.5 12.5 38.0
YOLO11-n [57] 640 100 2.60 41.0 33.04.912.2 30.1
YOLO26-n [58] 640 100 2.38 41.7 34.5 4.113.9 42.2
The benchmark therefore requires both fine-grained evidence
grounding and robust scene-level stage discrimination.
Fig. 5 summarizes this difficulty. The raw surveillance
frames are high-resolution and visually diverse. However,
many states that determine stage recognition are encoded
by only a few local pixels. In particular, clamp status and
hose connection status are often much smaller than the main
foreground actors. As a result, the benchmark is not a standard
object detection problem. It is a multi-scale state-grounding
problem with strong semantic asymmetry.
1) Lightweight Detection Baselines:We first evaluate
lightweight detectors that are relevant to edge deployment.
The results are reported in Table V. YOLOv9-t provides
the strongest overall trade-off among the lightweight models.
It achieves44.0% AP50 and36.5% AP50-95 with only1.98M
parameters. YOLO26-n gives the highestAP M andAP L, at
13.9%and42.2%, respectively.
The main bottleneck is exposed byAP S. Across all five
models,AP S remains between3.0%and4.9%. The gap
betweenAP S andAP L is large for every model. These
numbers show that the critical difficulty of GSO-Net is not
generic object presence. It is the recovery of small, state-
sensitive evidence after aggressive feature downsampling.
A second observation is that parameter efficiency does not
translate into reliable SOP understanding. The best lightweight
baseline identifies major foreground actors and some stable
states. Yet the most safety-critical microscopic evidence is
still missed. These models should therefore be interpreted as
deployment baselines rather than complete solutions.
2) Comparison with Stronger Detectors:We next evaluate
stronger transformer-based and open-vocabulary detectors.
Table VI shows that stronger detectors yield clear gains.

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 9
TABLE VI
TASK1RESULTS ON STRONGER DETECTORS(%).
Method Venue AP 50 AP50−95 APS APM APL
RT-DETR [31] CVPR’24 35.1 28.7 4.0 11.2 32.4
YOLO-World [39] CVPR’24 45.6 36.3 6.8 15.7 35.0
Relation-DETR-ResNet50 [32] ECCV’24 43.8 35.1 9.8 19.8 42.9
Relation-DETR-SwinL [32] ECCV’2456.4 46.3 13.3 23.4 55.1
Hyper-YOLO [33] TPAMI’25 40.6 34.1 3.4 11.2 33.4
Mr.DETR-ResNet50 [34] CVPR’25 45.0 37.5 11.9 19.6 46.7
Mr.DETR-SwinL [34] CVPR’25 46.1 37.2 12.9 20.8 45.2
RF-DETR [35] ICLR’26 37.5 30.3 1.6 10.8 38.9
Relation-DETR-SwinL provides the best overall results on all
reported metrics. It reaches56.4% AP 50 and46.3% AP 50-95.
It also gives the best scale-aware performance, including
13.3% APS,23.4% AP M , and55.1% AP L.
Nevertheless, the small-object problem is not removed. Even
for Relation-DETR-SwinL,AP S remains far belowAP L.
Stronger global attention therefore helps, but decisive contact-
level evidence remains far from solved.
YOLO-World provides an informative reference point. It
reaches45.6% AP 50 and improvesAP S to6.8%, which
is higher than all lightweight closed-set YOLO baselines.
This suggests that language-aligned pre-training is helpful for
broad semantic transfer. However, the gain remains limited
on the smallest and most mechanically defined categories.
The benchmark requires more than semantic name transfer.
It requires precise state grounding.
3) Category-wise Diagnosis:The overall metrics in Ta-
bles V and VI are informative, but they do not fully reveal
which categories remain unsolved. We therefore further report
the per-classAP 50 results in Table VII.
Several clear patterns emerge.
(1) Frequent and visually salient states are learned
well.Categories such astanker stopped true,staff standing,
staff operating, andextinguisher deployedachieve relatively
high scores. These classes are more frequent in the dataset and
supported by larger visual extent.
(2) Mechanically decisive states remain difficult.
The main failure occurs on contact-level categories.
clamp connectedremains at or below5.3%across
all models.clamp floatingremains at or below6.0%.
discharge disconnectedreaches15.7%only for Relation-
DETR-SwinL and stays near zero for most other methods.
clamp disconnectedis essentially unresolved.
(3) Stable workflow phases are easier than tran-
sient phases.Among the macroscopic steps,Step0 Idleand
Step6 Supervisionare reliably detected by several models. By
contrast, the transition phasesStep2,Step3,Step4,Step5, and
Step7remain lower across most models. These steps differ by
localized evidence rather than overall scene layout.
(4) Strong object detection does not guarantee correct
SOP understanding.A model may detect the tanker, the
worker, and the extinguisher, yet still miss the decisive con-
nection state or the correct procedural phase. The unresolved
categories are not generic object classes. They are rare state
transitions, small contact points, and short procedural stages.
S0: IDLES1: ENTRYS2: PROTECTS3: CHECKS4: CONFIRMS5: UNLOADS6: SUPERVISES7: ACCEPTS8: FINISH
0
2,500
5,000
7,500
10,000
12,500
15,000
17,500
20,000
Number of Images
Macroscopic SOP Dataset Distribution
1,259
185
3,154
728
1,687
363
2,978
692
3,802
946
5,075
1,191
16,037
3,907 3,598
718
3,386
611
Training Set Validation Set
Fig. 6. Frame distribution of the 9 macroscopic SOP steps in the training
and validation sets. Long-duration phases dominate the benchmark, whereas
several transitional steps remain comparatively rare.
C. Task 2: Frame-Level SOP Step Classification
Task 2 is introduced as a diagnostic reference rather than a
parallel core benchmark target. It isolates frame-level macro-
scopic step recognition by removing explicit box supervision
and localized state grounding. Each classifier receives a full
frame and predicts one of the 9 SOP steps from holistic
visual evidence alone. We evaluate two YOLO classification
baselines, YOLOv8-cls and YOLO26-cls, together with re-
cent generic backbones, including ConvNeXt-V2 [59], EV A-
02 [60], and MambaOut [61]. Although the output space
is simpler than in Task 1, accurate step prediction remains
difficult because success still depends on sparse local cues
and on whether the model captures the operational meaning
of visible objects rather than only dominant scene content.
Fig. 6 illustrates the temporal imbalance in the benchmark.
Long-duration phases dominate frame counts, whereas short
transitional stages remain sparse. Top-1 accuracy is therefore
insufficient on its own, so Macro F1 is reported alongside Top-
1 and Top-5. The task tests whether SOP recognition can be
reasonably approximated by scene-level classification before
localized state evidence is introduced.
Table VIII shows that all models fall within a narrow Top-1
range (41.7%−44.3%). YOLO26-cls provides the strongest
overall classification result, reaching44.3%Top-1,86.2%Top-
5, and16.1%Macro F1, but the absolute level remains limited.
The large Top-1/Top-5 gap indicates that coarse procedural
context is captured, but precise stage boundaries remain unre-
solved. Short transition phases are especially difficult because
their decisive cues are sparse and localized.
These results indicate that frame-level step classification
remains under-constrained when localized state supervision is
absent. In the sparse polling setting, holistic appearance alone
cannot reliably capture subtle contact-level cues and short
transitional evidence that distinguish adjacent SOP stages. As
a result, image-level classifiers may recognize dominant or
visually stable phases, but they remain unreliable for fine-
grained stage discrimination across the workflow.
The limitation is structural: many step boundaries are de-
fined byfunctional state transitionsrather than global scene
changes. Holistic classifiers can learn broad stage priors, but

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 10
TABLE VII
COMPREHENSIVE PER-CLASSAVERAGEPRECISION(AP 50, %)FOR ALL24CATEGORIES ACROSS SELECTED MODELS. BEST RESULTS AREBOLDED,
AND SECOND-BEST ARE UNDERLINED .
Category YOLOv9-t YOLO26-n RT-DETR YOLO-World Relation-DETR-R50 Relation-DETR-SwinL Hyper-YOLO Mr.DETR-R50 Mr.DETR-SwinL RF-DETR
Microscopic Entity States (E micro)
00: tanker moving true 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
01: tanker moving false 73.4 74.9 58.7 80.1 88.3 89.5 58.2 65.7 68.3 61.6
02: tanker stopped true 93.7 92.8 78.2 92.6 94.7 99.3 85.7 90.6 88.6 92.9
03: tanker stopped false 81.5 71.6 76.8 87.1 83.395.0 76.8 83.0 81.5 67.2
04: staff standing 55.6 50.5 38.5 60.4 62.9 67.2 53.5 36.0 37.3 53.8
05: staff bending 38.5 62.1 51.1 34.4 30.564.0 10.0 17.6 37.5 30.1
06: staff walking 32.2 28.9 28.2 38.7 41.4 48.2 30.1 31.5 27.8 34.8
07: staff operating 56.3 52.5 45.0 62.368.266.2 56.6 42.5 41.0 51.8
08: clamp connected 0.1 0.5 0.5 1.3 2.9 5.3 0.3 0.5 1.3 0.4
09: clamp disconnected 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
10: clamp floating 0.0 0.0 0.0 0.1 3.2 6.0 0.0 0.2 0.1 0.0
11: extinguisher deployed 73.6 70.8 53.3 81.6 78.283.3 73.9 52.7 54.0 63.6
12: extinguisher carried 23.4 15.3 23.1 45.3 41.470.7 19.9 19.4 19.1 21.7
13: discharge connected 34.0 35.2 48.4 45.956.247.8 34.1 14.0 15.6 20.1
14: discharge disconnected 2.0 1.1 1.3 2.8 2.315.7 1.6 1.2 2.6 2.0
Macroscopic Procedural Steps (S macro)
15: Step0 Idle 87.0 84.2 81.4 83.0 78.7 87.4 93.690.2 88.7 87.1
16: Step1 Entry 54.0 58.9 53.1 62.8 53.073.9 57.2 50.5 48.3 58.8
17: Step2 Safety Protection 41.0 32.7 6.5 47.2 16.168.7 46.4 36.0 38.5 19.3
18: Step3 Safety Check 28.5 26.3 5.3 29.4 13.250.9 28.3 18.7 14.9 18.9
19: Step4 Pre Unload Confirm 37.0 22.7 25.1 23.7 25.147.2 28.2 28.2 28.9 10.5
20: Step5 Oil Unloading56.152.6 35.4 42.2 43.1 41.1 48.6 51.8 41.8 39.8
21: Step6 Supervision 87.6 81.6 68.8 87.4 90.696.2 82.7 95.3 86.5 88.9
22: Step7 Receipt Acceptance 29.6 27.0 18.9 21.2 21.040.7 28.0 20.0 16.2 18.4
23: Step8 Post Processing 25.7 17.1 8.8 19.5 12.733.9 19.1 16.2 17.1 21.7
TABLE VIII
FRAME-LEVEL MACROSCOPICSOPSTEP CLASSIFICATION RESULTS(%).
Model Size Epochs Top-1 Top-5 Macro F1
YOLOv8-cls 640 100 41.7 83.8 8.9
YOLO26-cls 640 10044.3 86.2 16.1
ConvNeXt-V2 224 100 41.8 75.3 6.8
EV A-02 224 100 43.6 80.9 14.1
MambaOut 224 100 41.8 78.9 6.6
remain weak when decisive signals are sparse and localized.
The issue is therefore not only temporal ambiguity, but also
the model’s ability to capture the operational meaning of small
objects, contact relations, and state-bearing components.
Task 2 thus serves as adiagnostic reference task. It
shows that SOP recognition cannot be reduced to holistic
image classification, because the required temporal logic is
expressed through localized functional state transitions rather
than coarse scene appearance. This directly motivates Task
1, where macroscopic steps provide procedural context and
microscopic states supply the local evidence needed for robust
stage recognition. From an engineering perspective, GSO-Net
should therefore be read as a benchmark for practical visual
state machines under sparse polling, small-object difficulty,
and long-tailed operational evidence.
D. Qualitative Analysis and Error Statistics
To further examine the failure modes behind the quantita-
tive results, Fig. 7 provides representative predictions from
YOLOv9-t, YOLO-World, Mr.DETR-SwinL, and Relation-
DETR-SwinL. All predictions are generated with a confidence
threshold of0.35and an IoU threshold of0.40. Row–column
indexing is used for reference, where the row denotes the SOP
phase (S 1–S8) and the column denotes the detector output.
Three recurrent behaviors are observed.
(1) Limited correct phase grounding.Accurate and vi-
sually consistent phase prediction appears only in a small
subset of cells, such as 1-3, 2-3, 4-2, 5-1, 5-2, and 5-4. When
decisive cues are clearly visible, current detectors can recover
the correct phase.
(2) Phase ambiguity.Many cells, including 1-4, 2-2, 2-4, 3-
4, 4-4, 5-3, 6-4, and 8-3, contain overlapping or poorly ranked
predictions. The ground-truth phase is often present, but not
ranked first. This behavior is consistent with the Top-1/Top-5
gap observed in Task 2.
(3) Semantic inconsistency.Cases such as 4-3, 6-3, and 7-3
show predictions that contradict visible operational evidence.
These cases indicate three main error sources: spatiotem-
poral ambiguity between adjacent phases, omission of de-
cisive microscopic evidence such as clamp or hose states,
and compositional inconsistency between predicted stages and
visible cues. Among the four detectors, Relation-DETR-SwinL
usually provides the most complete visual evidence and the
strongest phase sensitivity, consistent with Table VI. However,
even the strongest detector still suffers from ranking ambiguity
and incomplete evidence support.
E. Summary of Empirical Findings
The experiments support four main conclusions. First, the
strict cross-node split makes generalization to unseen logistics
nodes difficult. Second, current detectors recognize major
actors and stable phases, but still fail on the microscopic
contact states that determine procedural status. Third, image-
level step classification is biased toward dominant phases
and does not recover short transitions reliably. Fourth, the
remaining gap is structural rather than a simple matter of
stronger backbones.
Overall, the benchmark results suggest that accurate SOP
monitoring cannot be achieved by scene-level recognition

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 11
Input Image YOLOv9t YOLO-World Mr.DETR-SwinL
 Relation-DETR-SwinL
S1
S2
S3
S4
S5
S6
S7
S8
1-1 1-2 1-3 1-4
2-1 2-2 2-3 2-4
3-1 3-2 3-3 3-4
4-1 4-2 4-3 4-4
5-1 5-2 5-3 5-4
6-1 6-2 6-3 6-4
7-1 7-2 7-3 7-4
8-1 8-2 8-3 8-4
Fig. 7. Qualitative comparison of representative detectors across SOP phasesS 1–S8.Column 1:Input images with ground-truth phase labels.Columns
2–5:Predictions from YOLOv9-t, YOLO-World, Mr.DETR-SwinL, and Relation-DETR-SwinL. Three recurrent failure modes are observed: adjacent-step
confusion, omission of critical micro-states, and stage predictions inconsistent with visible evidence.
alone. Fine-grained state grounding is essential, which is
precisely why Task 1, rather than Task 2, constitutes the core
benchmark evaluation of GSO-Net.
V. DATASETADVANTAGES
The experimental results indicate that GSO-Net is neither a
standard object detection benchmark nor a conventional frame-
classification benchmark. Performance is reasonable on salient
objects and dominant workflow phases, but drops sharply when
the decision depends on tiny contact states, rare events, or
short transitions. This section discusses the implications of
these findings for vision-based safety monitoring at hazardous
freight logistics nodes.
From Object Detection to Stage-Aware Node Under-
standing.Mainstream detectors are designed to answer what
is present and where it is [25]–[27], [30], [37]–[39], [42].

IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS 12
GSO-Net requires an additional capability: linking local-
ized visual evidence to procedural stage understanding at an
infrastructure-side transportation node.
This difference appears in the results. In Table VII,
visually salient categories such as tanker and person-
nel states achieve high scores, whereas decisive cate-
gories such asclamp connected,clamp floating, anddis-
charge disconnectedremain difficult. A similar pattern ap-
pears for macroscopic steps, where stable phases are recog-
nized more reliably than short transitions. Correct detection
therefore does not guarantee correct SOP understanding.
Why Sparse Infrastructure Polling Makes the Prob-
lem Hard.Many existing video models and procedural
benchmarks assume dense temporal continuity [4], [9], [18],
[19], [23], [24]. GSO-Net follows a different setting. In
infrastructure-side deployment, cameras are observed through
sparse round-robin polling, so the visual stream is discontin-
uous and transitions may appear in only one frame.
This setting explains the weakness of frame-level classifi-
cation in Task 2. In Table VIII, the accuracy of Top-1 remains
limited, while Macro F1 is substantially lower. Short transition
phases are especially difficult because sparse observation shifts
stage discrimination toward localized state transitions rather
than global scene changes. Pure frame-level classification is
therefore insufficient for practical understanding of SOP.
Toward State-Aware SOP Reasoning under Sparse
Polling.The benchmark results suggest that stronger back-
bones alone are unlikely to close the gap. Larger detectors
improve overall metrics, but the hardest microscopic states,
rare cases, and transient phases remain unresolved. These
findings indicate that future progress will depend not only
on stronger perception, but also on mechanisms that preserve
local state evidence and relate it to sparse procedural context.
A practical direction for sparse visual polling may include:
1)Micro-Perception Module:to preserve state-sensitive
evidence such as contact points.
2)Sparse Temporal Memory:to accumulate partial ob-
servations across discontinuous frames.
3)Stage-Aware Reasoning Module:to relate observed
states to broader workflow context.
This decomposition is consistent with the benchmark find-
ings: the first component targets microscopic-state failure,
the second addresses sparse polling, and the third addresses
ambiguous stage prediction.
VI. DISCUSSION
1)Dataset Challenges.GSO-Net poses several challenges.
Hierarchical Step-State Coupling:Unlike conventional de-
tection benchmarks, it requires joint understanding of macro-
scopic SOP stages and microscopic operational states, so
object presence alone is insufficient.Sparse and Subtle
Evidence:Under round-robin polling, stage inference must
rely on isolated frames and highly localized cues, such as
clamp status and hose-port connection, which are often ex-
tremely small and visually subtle.Real-World Difficulty:
The benchmark further exhibits severe long-tail and scale
imbalance, together with occlusion, low illumination, adverse
weather, and cross-node viewpoint variation.
2)Limitations.This study remains limited in three main
aspects.Domain Scope:The current benchmark is restricted
to petrochemical unloading scenarios at logistics nodes.Tem-
poral Supervision:Its independently sampled frames do not
yet support richer temporal modeling or explicit association
across sparse observations.Reasoning Scope:Although GSO-
Net provides hierarchical step-state annotations and systematic
baselines, it does not yet implement an explicit rule-based or
consistency-aware reasoning protocol for SOP verification.
3)Future Work.Future work will extend the benchmark
to more hazardous-freight and infrastructure-side scenarios,
introduce sparse temporal annotations and association signals,
and develop stage-aware models that use the hierarchical rela-
tionship between microscopic states and macroscopic steps.
More broadly, this direction may improve safety-oriented
visual round-robin inspection in intelligent transportation and
infrastructure monitoring, while advancing visual detection
from perception toward structured semantic and procedure-
aware understanding. Cross-node continual evaluation will
also be important for reducing the gap between benchmark
performance and real-world reliability.
VII. CONCLUSION
This paper introduced GSO-Net, a large-scale bench-
mark for visual SOP understanding in petrochemical haz-
ardous freight-transfer scenarios under sparse infrastructure-
side polling. By coupling 9 macroscopic procedural steps
with 15 microscopic operational states, GSO-Net formulates
hazardous freight-transfer monitoring as a hierarchical stage-
aware state-grounding problem. Experiments on 64 real petro-
chemical logistics nodes show that current models remain
effective on salient objects and dominant phases, but still
struggle with contact-level state grounding, transient phase
recognition, and stage-consistent understanding under sparse
and localized evidence. These findings show that reliable
visual safety monitoring requires moving beyond surface-level
detection toward structured procedural understanding. GSO-
Net provides a practical benchmark for future research on
stage-aware reasoning and safety-oriented visual inspection in
intelligent transportation and freight logistics.
APPENDIXA
HYPERPARAMETERCONFIGURATIONS
To improve reproducibility, the YOLO-series baselines were
trained under a unified training configuration in the Ultralytics
framework. All YOLO-based models were trained for 100
epochs with a batch size of 16 and 8 dataloader workers. Early
stopping with a patience of 50 epochs was applied to reduce
overfitting on the imbalanced validation set.
Optimization was performed using stochastic gradient de-
scent (SGD). The initial learning rate was set to0.01, the final
learning-rate ratio was set to0.01, and the momentum was set
to0.937. A warmup schedule was used during the first 3.0
epochs, with the warmup momentum initialized at0.8.
For fair comparison, the input resolution was fixed at
640×640for all YOLO-based detection and classification
baselines. Standard data augmentation was applied during
