---
source_id: "arxiv"
title: "SkillRefine: Cross-Source Skill Induction and Execution Validation"
url: "https://arxiv.org/abs/2609.30674"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.30674. Abstract: SkillRefine: Cross-Source Skill Induction and Execution Validation
for LLM Agents in Refinery Planning Software
Dongxiao Liu1,2, Boren Zhu2, Yuwen Ding2, Linghui Li1, Li Lei2, Xiaoyong Li1
1Beijing University of Posts and Telecommunications, Beijing, China
2Sinopec Engineering Incorporation, Beijing, China
liudongxiao@bupt.edu.cn, zhuboren.sei@sinopec.com, dingyuwen.sei@sinopec.com,
lilinghui@bupt"
---

# SkillRefine: Cross-Source Skill Induction and Execution Validation

SkillRefine: Cross-Source Skill Induction and Execution Validation
for LLM Agents in Refinery Planning Software
Dongxiao Liu1,2, Boren Zhu2, Yuwen Ding2, Linghui Li1, Li Lei2, Xiaoyong Li1
1Beijing University of Posts and Telecommunications, Beijing, China
2Sinopec Engineering Incorporation, Beijing, China
liudongxiao@bupt.edu.cn, zhuboren.sei@sinopec.com, dingyuwen.sei@sinopec.com,
lilinghui@bupt.edu.cn, lilei.sei@sinopec.com, lixiaoyong@bupt.edu.cn
Abstract
Operating industrial planning software such as AspenTech
PIMS (Process Industry Modeling System) requires an LLM
agenttocombinestructuralknowledge,proceduralknowledge
from expert records, and constraints revealed only during ex-
ecution. These evidence sources are heterogeneous and in-
dividually incomplete: documentation describes tables and
interfaces but omits task-level coordination, expert CASE
records expose multi-table modification patterns without ex-
plicitschemagrounding,andexecutionfeedbackrevealslatent
constraintsonlywhenaplanisexecuted.WepresentSkillRe-
fine, a framework that exploits the Documentation–Practice
Gapbetween documentedstructure andexpertpractice toex-
tractcandidatecoordinationpatterns,groundthemagainstta-
bledefinitionsandCOMspecifications,andcompiletheminto
progressively disclosed skill packages with provenance. The
library is then refined through label-free compliance screen-
ing, oracle-based match decomposition over table, row, col-
umn,andvaluedimensions,andsignal-conditionedtrajectory
attribution for localized repair. We evaluateSkillRefineon
PIMS-Bench, a benchmark built from two AspenTech PIMS
demonstration models, using disjoint construction and held-
out test tasks. On the held-out test set,SkillRefineachieves
absolutecomponent match F1gains of14%–30% acrossfour
LLMbackbones,withthelargestgainsoncomplexmulti-table
coordination tasks.
Introduction
AspenTech PIMS (Process Industry Modeling System) (As-
pen Technology, Inc. 2025) represents refinery planning
models through 85 interconnected spreadsheet tables that
are modified using a structured CASE interface. Operat-
ing PIMS requires translating business-level instructions—
such as “shut down the FCC unit” or “raise diesel price
to $148/bbl”—into precise CASE entries with valid table
names, row identifiers, column headers, values, and termi-
nators. Even a routine request such as changing diesel price
requires knowing that diesel is represented by the row tag
DSL and that its price is modified through the PRICE col-
umn rather than an intuitive alternative such as COST. In
operational terms, each instruction must be translated into a
set of structured modifications over table, row, column, and
value fields, while preserving cross-table feasibility.
Copyright©2027, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Request Consult Knowledge
Modeling Result
"The distillate 
hydrotreater must 
shut down…… "
Feedback
COM
Agent Result
Obj= 4162 ✓
Successful
✓ Match
+Caps
+Sell
Practice
Document
SKILL
Thinking
+PROCLIM
SKILL
PIMS Software
CASE 009
"TABLE | BLNSPEC",
" | TEXT | RRG |",
"XSUL | XSUL | 0.05 |"
Figure 1: Learning operational skills from cross-source
knowledge to autonomously operate PIMS.
Consider shutting down the FCC unit for maintenance.
In the evaluated Gulf Coast demonstration model, setting
FCC capacity to zero in CAPS alone may produce an infea-
sible plan because downstream tables encode related yield
and blending assumptions. A valid coordinated modifica-
tion may additionally update SLPR yield rows, BLNMIX
eligibilitycolumns,andrelevantpurchaselimits.Correctex-
ecution also requires setting both MIN and MAX in CAPS
tozero,targetingexactrowtagsratherthannatural-language
descriptions, and using column names that match the CASE
schema. Although the required modifications are specific to
the model and planning scenario, the example illustrates a
general operational challenge within PIMS: a short business
instruction may correspond to several coupled and schema-
sensitive modifications.
Theknowledgerequiredfortheseoperationsisdistributed
across three sources, each of which is incomplete in a dif-
ferent way (Figure 1). PIMS documentation provides broad
coverage of table schemas, column semantics, data types,
and interface conventions, but is organized by component
rather than by planning task. Expert CASE records provide
sparse task-level evidence about which tables and fields ex-
pertsmodifytogether,butomitschemadefinitions,business-
languageindexing,andexplicitexplanationsofwhythemod-
ifications are coordinated. COM specifications expose exe-
cutable methods but do not encode refinery planning logic.
We use the termDocumentation–Practice Gapto describe
arXiv:2609.30674v1  [cs.CE]  25 Sep 2026

this source asymmetry observed in PIMS. The three sources
arethereforecomplementaryratherthaninterchangeable:ex-
pertrecordscanproposetask-levelcoordinationhypotheses,
documentation can ground them to valid schemas and inter-
faces, and execution can reveal constraints that are not ex-
plicitlystatedineitherstaticsource.Consistentwiththisdis-
tinction, raw documentation produces small and backbone-
dependent gains, whereas compiling the evidence into task-
oriented skills improves performance consistently.
WeproposeSkillRefine,aframeworkthataddressesthis
gap through role-separated cross-source skill induction and
execution-driven refinement. During skill construction, ex-
pertCASErecordsareusedtoproposecoordinationpatterns,
while documentation grounds these patterns to valid table
schemas,columnsemantics,valueconstraints,andCOMin-
terfaces.Interfacestabilizationseparatesfailuresinsoftware
invocation from failures in business planning knowledge.
The resulting skill library is then refined through execution
evidence: label-free format and solver-compliance signals
providecoarsefailurescreening,structuredcomparisonwith
expertreferencesidentifiestable-,row-,column-,andvalue-
level mismatches, and tool-use trajectories are used as a lo-
calization heuristic to narrow the candidate skill content to
be repaired. The framework applies constrained add, mod-
ify,remove,orconstrainoperationsratherthanrewritingthe
library from a scalar score.
Importantly, the skill library is constructed and refined
onceusingDeepSeek-V4-Proandissubsequentlyfrozenand
reused unchanged by all four target LLM backbones. No
backbone-specific skill editing or refinement is performed
on the held-out evaluation tasks. The evaluation therefore
measures both held-out task performance and whether the
same skill artifact can be reused across different agent back-
bones within the two evaluated PIMS environments. It does
not establish transfer to unseen refinery models, production
deployments,orotherindustrialplanningplatforms.Overall,
we make the following contributions:
•We introducerole-separated cross-source skill induc-
tion for refinery planning software. Sparse expert
CASE records propose task-level coordination hypothe-
ses, documentation grounds these hypotheses to valid ta-
ble schemas, column semantics, value constraints, and
COM interfaces, and execution evidence determines
whether the resulting rules should be retained, con-
strained, or repaired.
•We formulateexecution-driven refinement as factor-
izeddiagnosisandlocalizedrepairoverstructuredop-
erations.SkillRefinedistinguishes format and solver-
compliance failures from table-, row-, column-, and
value-level mismatches, uses tool-use trajectories to nar-
row the candidate repair scope without claiming causal
attribution,andappliesadd,modify,remove,orconstrain
operations to relevant skill content.
•WedevelopPIMS-Bench,anexecution-groundedbench-
markcontaining140planningtasksacrossfivestructural
complexity levels and two PIMS demonstration models.
EvaluationusestheactualCOMandsolverenvironment,
expert-verifiedstructuredoperationreferences,100held-
out test tasks, and a single frozen skill library shared
unchanged across four target LLM backbones.
Related Work
Agent Skill Acquisition and Refinement.Agent skills
externalize reusable procedural knowledge so that agents
can acquire task-specific behavior without parameter up-
dates (Agent Skills 2026; Xu and Yan 2026). Existing meth-
odslearnskillsfromdifferentsupervision:Voyageraccumu-
lates executable programs through exploration (Wang et al.
2023); LGSD learns motor skills from language supervi-
sion(Rhoetal.2025);SkillRLusesskillsforhierarchicalre-
inforcementlearning(Xiaetal.2026).Anotherlineimproves
skillsfromexecutionfeedback:Reflexion(Shinnetal.2023)
andSelf-Refine(Madaanetal.2023)establishiterativeself-
improvement through verbal feedback; Trace2Skill converts
trajectories into reusable skills with fix validation (Ni et al.
2026);SkillOptacceptseditsthroughanexecution-basedval-
idationgate(Yangetal.2026);CREATOR(Qianetal.2023)
disentangles skill creation from execution; SkillGrad opti-
mizes via textual gradients (Wang et al. 2026). Recent sys-
temssynthesizeskillsfromexternalresources:SkillFoundry
minesheterogeneouswebevidence(Shenetal.2026),Skill-
Net connects skills into a reusable network (Liang et al.
2026), and SkillForge combines knowledge bases with sup-
portticketsandfailurediagnosis(Liuetal.2026).SkillRefine
differs by mining co-modification patterns fromsuccessful
expert records—rather than from failure cases—grounding
inferred coordination rules against documentation schemas,
anddiagnosingfailuresattable,row,column,andvaluelevel.
Implicit Procedures and Industrial Software Agents.
Beyond skill acquisition, recovering undocumented pro-
cedures connects to tacit knowledge (Polanyi 2009)—
knowledge that experts possess but cannot fully articulate.
The core challenge in PIMS is inferring not onlywhichta-
bles are co-modified butwhy: expert CASE records reveal
coordination patterns that documentation never describes,
and SkillRefine extracts these through LLM-guided cross-
source analysis (Phase 2a), grounding the inferred rationale
againstdocumentationschemas.LLMagentshavebeencon-
nectedtooptimizationandengineeringsoftware:OptiGuide
augments supply-chain solvers with natural-language what-
if interaction (Li et al. 2023), OptiChat helps practitioners
inspectanddiagnoseoptimizationmodels(Chenetal.2025),
and a chemical engineering agent operates process simula-
torsthroughmodel-contextinterfaces(Liang,Groll,andSin
2026). These systems assume curated solver interfaces or
pre-built model connections; SkillRefine instead learns the
proceduresthattranslateplanningintentintocoordinatedta-
ble edits within an existing PIMS environment. The solver
remains the authority for feasibility; its feedback refines the
procedural layer.
Skill Organization and Execution-Based Evaluation.
Beyond individual skills, large skill libraries introduce two
distinct risks: long-context degradation, where models un-
deruserelevantevidencedependingonitsposition(Liuetal.
2023), and skill shadowing (Song and Wei 2026), where
expanding the library increases selection errors even when

individual skills are correct. Progressive disclosure (Agent
Skills 2026)—loading skill metadata initially and full con-
tentondemand—mitigatesloadingcost.SkillRefinefollows
this separation and additionally records which skill was se-
lectedandwhichlocalizedoutcomefollowed,enablingjoint
revision of skill content and retrieval metadata. Evaluation
benchmarks for agent skills include SWE-bench (Jimenez
et al. 2024), which evaluates code modification via GitHub
issues,SkillsBench(Lietal.2026),whichevaluatesreusable
skillsacrossbroadtasksuites,SWE-Skills-Bench(Hanetal.
2026), which studies repository-level skill acquisition and
reuse,andSpreadsheetBench2(Zhuetal.2026),whichtests
realistic workbook manipulation. PIMS-Bench differs in its
unitofcorrectness:structuredoperations(table,row,column,
value)overindustrialplanningmodels,withfivecomplexity
levelsseparatingsimplefieldeditsfrommulti-objectcoordi-
nation procedures.
Method: SkillRefine
SkillRefine operates in four phases.Grounding(Phase 1)
constructs a structural and interface knowledge layer from
documentation.Pattern extraction(Phase 2) proposes can-
didate coordination hypotheses from expert CASE records
and expands them with documentation.Interface stabiliza-
tion(Phase 3) ensures the COM execution layer is reliable.
Structuredrefinement(Phase4)iterativelydiagnosesandre-
pairs skills through multi-signal execution feedback.
Skills are represented as standardSKILL.mddocuments
following the Agent Skills specification (Xu and Yan 2026):
a front matter with name and description for progressive
disclosure routing, a body with rules and procedures, and
optional reference files for source evidence.
Phase 1: Grounding Layer from Documentation
Phase 1 constructs a grounding layer rather than task-level
skills. PIMS documentation (3,126 HTML pages) is parsed
into two structured outputs:
•S struct:tableschemas,columnsemantics(name,datatype,
valid range, required/optional flags), and inter-table data
references for all 85 tables.
•S interface: COM automation method signatures (e.g., Set-
TableFile,ExecuteModel,GetObjectiveValue),parameter
conventions, and execution state rules.
Parsingisrule-based:eachtable’sHTMLpagesfollowacon-
sistent layout (description page, column reference page, op-
tional example page), from which we extract table-level and
column-levelmetadataintoaunifiedJSONschema.Phase1
does not generate business operation rules; it provides the
schema and interface knowledge used to validate candidate
patterns in Phase 2 and to ground skill content throughout
the pipeline.
Phase 2: Procedural Pattern Extraction and
Schema-Grounded Expansion
Phase 2 builds a candidate skill library through two sub-
phases.
Phase2a:Co-modificationExtraction.Weextractmulti-
tablemodificationpatternsfromCASErecordsshippedwith
PIMS demonstration models: Weight Sample (6 non-empty
records) and Gulf Coast Case Sets (317 records). For each
CASE recordh i, we identify the set of tables modified to-
gether:
Ci ={T 1, T2, . . . , Tk}(1)
Co-occurrence ofT a andT b inC i does not imply thatTa
requiresT b; it indicates only that experts modified both in
this scenario. The extracted patterns are therefore treated as
candidate coordination hypotheses, not as validated rules.
The limited CASE coverage is not assumed to span the full
task space; instead, CASE records seed a small set of task-
levelcoordinationhypotheses,whiledocumentationsupplies
broadstructuralcoverageandPhase4executionfeedbackde-
termineswhichhypothesesareretained,revised,orremoved.
The construction tasks are manually selected to cover repre-
sentative failure patterns rather than directly sampled from
all CASE records.
Phase 2b: Schema-Grounded Expansion.Phase 2a pat-
terns cover at most 5 unique tables per model. Phase 2b
expands coverage by reading documentation for tables not
present in expert CASE records, performing three opera-
tions:
1.Schema grounding: verify that table names, column
names, types, and value ranges in candidate patterns are
valid againstSstruct.
2.Intra-table rule extraction: identify column interaction
rules within a table (e.g., PROCLIM requires both MIN
andMAX),valuerangeconstraints,andformattingrules.
3.Cross-table hypothesis enrichment: for tables that ap-
pear in Phase 2a co-modification patterns, associate doc-
umentation schema knowledge with the observed co-
occurrence to produce candidate coordination explana-
tions.
All extracted rules are treated as hypotheses; their necessity
is tested empirically through execution-based refinement in
Phase 4.
Phase 3: COM Interface Stabilization
Phase 3 stabilizes the COM execution layer to prevent inter-
face failures from being confounded with skill failures. All
conditions use the same stabilized execution functions, in-
cluding state reset, model backup/restore, solver invocation,
and result extraction. Phase 3 introduces no business plan-
ningrules.All50executabletestcasespassed;11additional
cases were skipped because the corresponding methods are
unsupported in PIMS v22.0.11.
Phase 4: Structured Multi-Signal Refinement and
Targeted Skill Repair
Phases1–3produceacandidateskilllibrary(47documents,
∼52KB) organized in a three-level hierarchy: L0 (meta-
skills,∼200tokens: dependency awareness, format rules),
L1 (domain skills,∼500–1500 tokens: per-domain depen-
dency graphs and operation rules), L2 (task skills,∼2000

Skill Library Construction- Phases 1 & 2
Interface Stabilization- Phase 3
Execution-Driven Refinement- Phase 4
Expert CASE Records Co-modificationExtraction
Execution command
 PIMS COM API
LLM Agent
Execution Logs
PIMS Compliance
format, converge
Match Decomposition
add
modify
remove
Execution Errors 
Construction 
Dataset
• Table docs
• Column types
• Data refs
• COM API
PIMS 
Documentation
Phases 1 
 Phases 2a 
Candidate Patterns
Deep table 
semantics
Value range 
constraints 
Phases 2b 
Complex Skills
Executable script
LLM Agent
• SetTableFile
• ExecuteModel
• Get Case
•       • • • • 
L5
Match, table_f1, 
row_recall, col_recall
Task
Trajectory Attribution
Step_count, Read_operations,…
LLM-guided
Analyzer
constrainPIMS Skills
Figure2:SkillRefinepipeline.Phase1constructsagroundinglayerfromdocumentation.Phase2extractscandidatecoordination
patternsfromexpertCASErecordsandexpandsthemwithdocumentation.Phase3stabilizestheCOMinterface.Phase4refines
skills through compliance screening, match decomposition, and trajectory-guided attribution.
tokens:specificproceduresforbusinessscenarios).Progres-
sive disclosure (Xu and Yan 2026) loads the skill index ini-
tially; full bodies and evidence files are loaded on-demand.
Thisinitiallibraryconsistentlyimprovesperformanceover
unguidedbaselines,butfurtherimprovementrequiresidenti-
fyingandrepairingspecificskilldeficiencies.Weaddressthis
throughstructured multi-signal refinement: a framework
thatdecomposesexecutionfailuresintofactorizeddiagnostic
dimensionsandusestrajectory-guidedattributiontoidentify
candidate skills for repair.
Three diagnostic layers.
Layer 1: Compliance screening.Two binary indicators
screen for skill failures without requiring oracle answers:
c(d) =

fd, vd

∈ {0,1}2 (2)
wheref disformatvalidity(CASEsyntaxcorrectness:termi-
nators, table keywords, column alignment) andvd is solver
convergence (whether the LP solver accepted the modifica-
tions). A format failure indicates broken formatting guid-
ance; a convergence failure indicates coordination rules that
produce infeasible plans.
Layer2:Structuredmatchdiagnosis.Compliancedoesnot
imply correctness. When oracle answers are available, we
factorize task correctness into operation-level dimensions:
q(d) =

md, td, rd, cd

∈[0,1] 4 (3)
wherem discomponentmatchF1(acrosstable,row,column,
and value tuples),td is table F1,rd is row recall, andcd is
column recall. Value correctness is included in component
matchF1butisnotseparatelyreportedasadiagnosticmetric.
Lowt d suggests missing or over-generated table operations;
lowc dsuggestsincorrectoperation-to-columnmapping;low
rd suggests incorrect entity-to-row mapping.
Layer 3: Signal-conditioned trajectory attribution.When
Layer 1 or Layer 2 detects a failure, the recorded trajectory
Table 1: Signal–diagnosis–repair mapping.
Signal Diagnosis Repair
Format invalid CASE/alignment error Modify format
Solver failure Missing dependency Add constraint
Low table F1 Operation error Add/remove rule
Low row recall Entity–row mismatch Fix mapping
Low column recall Operation–column mismatch Fix mapping
Wrong skill Routing mismatch Update skill
Repeated reads Skill unclear Rewrite skill
Over-generation Rule too broad Restrict rule
τd ={consulted skills,tool sequence,reads,timing}nar-
rows the candidate repair scope. We derive two views from
the same trajectory:
τ compd = Πcomp(τd, c(d)), τ matchd = Πmatch(τd, ed),(4)
wheree d = Diff(ˆad, a∗d)is the structured table-, row-,
column-, and value-level mismatch. The first view localizes
candidate skills associated with format and solver failures,
whereasthesecondlinksstructurederrorstoconsultedskills.
Both are branches of a single attribution layer and are used
only as localization heuristics; they do not imply causality.
Signal–diagnosis–repair mapping.Table 1 maps ob-
served signals to candidate diagnoses and repair actions.
Offlinerefinementprocess.Unlikepriormethodsthatuse
boundededitswithascalarvalidationgate(Yangetal.2026)
or trajectory-level consolidation without factorized diagno-
sis (Ni et al. 2026), our refinement usestrajectory-guided
attribution. For each failing task, we (1) compute a struc-
tured diff when the output is parseable, or derive a compli-
ance diagnosis otherwise; (2) associate the diagnosed error
withconsultedskilldocumentsthroughread_skilltool-
call logs; and (3) apply targeted repairs from Table 1. This

process runs forR=5rounds onDconstr:
Kd = Trace(τd, c(d), ed,S),
S ′ = Repair(S, ed, Kd), (5)
whereK d denotescandidateskillslocalizedthroughthetwo
signal-conditioned attribution branches. Each round makes
surgical correctionsrather than blind edits: for example, a
ruleassociatedwithcolumnconfusion(e.g.,VPRICEinstead
ofPRICE)iscorrectedwithoutrewritingunrelatedskillcon-
tent. The output is a refined skill libraryS∗ deployed to the
evaluation agent. The held-out test setDtest is never used for
refinement (Algorithm 1).
Experimental Setup
Models.We evaluate on two AspenTech PIMS demonstra-
tion models: Weight Sample (10 crudes, 14 products, base
objective1036.12)andGulfCoast(49crudes,base1341.02).
Knowledge sources.We use 3,126 documentation pages
fromthePIMSCHMhelpsystemandCASErecordsfromthe
demonstrationmodels(6non-emptyWeightSamplerecords
and317GulfCoastrecords)forproceduralpatternextraction
in Phase 2a. Construction-task oracles supervise refinement
in Phase 4.
Benchmark.PIMS-Bench comprises 140 tasks
(70/model) across five complexity levels (28 each):
L1 single-value changes, L2 multi-table coordination,
L3 component-level modifications, L4 structural changes
(includingcross-modelunitmigration),andL5system-wide
coordinated modification. Tasks cover 31 tables and all four
CASE keywords. They are partitioned intoDconstr (40 tasks
forskillconstructionandrefinement)andD test (100held-out
tasks). No test task participates in any skill construction or
refinement decision. The tasks were jointly designed and
reviewed by three refinery design experts.
Conditions.Four LLM backbones—DeepSeek-V4-Pro,
DeepSeek-V4-Flash (Xu et al. 2026), Gemma-4-31B (Team
2026),andQwen-3.6-27B(Yangetal.2025)—areevaluated
under six conditions using a ReAct-style agent (Yao et al.
2022):Baseline(noexternalknowledge,5tools),DocOnly
(+rawdocumentation,6tools),Trace2Skill(Nietal.2026)
(trajectory-level patch induction and hierarchical consolida-
tionwithconstruction-setvalidation),SkillOpt(Yangetal.
2026) (bounded edits withDconstr validation gate),Skill-
Base(Phase 1–3 skills, unrefined, 7 tools), andSkillRe-
fine(multi-signal refined skills, same 7 tools).SkillBase
andSkillRefineshareidenticaltools;theonlydifferenceis
unrefined vs. refined skills. All conditions share the same
PIMS execution interface; knowledge-enabled conditions
differ only in their documentation or skill access.
Metrics.Primary metric is match F1 (component-level
F1 across table, row, column, and value tuples). For each
task,themeanandstandarddeviationarecomputedoverfive
independent executions and then averaged across the 100
held-out tasks. Table F1 is used as an internal diagnostic
signal during refinement, while row and column recall are
reported for error analysis.
Infrastructure.All experiments run on a Windows 11
workstation (Intel Core i7-12700, 64 GB RAM; CPU only,
Algorithm 1: SkillRefine Pipeline
Require:DocumentationD, expert recordsH, construction tasks
Dconstr, construction oraclesOconstr, PIMS execution environ-
mentE, refinement roundsR
Ensure:Frozen refined skill libraryS ∗
1:(S struct,S interface)←ParseDocs(D)
2:S op ←ExtractPatterns(H)
3:S op ←GroundAndExpand(S op,S struct,D)
4:S exec ←StabilizeInterface(Sinterface,E)
5:S 0 ←Encode(S struct ∪ Sop ∪ Sexec)
6:S ← S0
7:forr= 1toRdo
8: ExecuteD construsingS;collectoutputs,logs,andtrajectories
9:foreach taskd i in a fixed orderdo
10:c i ←Compliance(ˆai, ℓi)
11:q i ←MatchDecomposition(ˆai, a∗i )
12:ifc i indicates failure orMatchF1(qi)<1.0then
13:ifˆa i is structurally parseablethen
14:e i ←Diff(ˆai, a∗i )over table, row, column, and
value
15:else
16:e i ←ComplianceDiagnosis(c i, ℓi)
17:end if
18:K i ←Trace(τ i, ci, ei,S){signal-conditioned local-
ization; not causal}
19:S ←Repair(S, e i, Ki){add / modify / remove /
constrain}
20:end if
21:end for
22:end for
23:S ∗ ←Freeze(S)
24:returnS ∗
no local GPU). PIMS v22.0.11 with the FICO Xpress
v8.8.4 LP solver is operated via COM automation us-
ing Python 3.13 andpywin32. LLM backbones are ac-
cessed through an OpenAI-compatible API (temperature=
0.5, max_tokens= 8192, native function calling with
tool_choice=auto). DeepSeek-V4-Pro and DeepSeek-V4-
Flash support 1M-token context windows; Qwen-3.6-27B
supports32,768tokens.Eachbackbone–conditionpaircom-
prises 500 executions (100 tasks×5 runs, with a 50-step
limit per run).
Results
Knowledge Extraction Results
Structural knowledge(Phase 1): Documentation parsing
extracted structured descriptions for all 85 PIMS tables,
including column semantics, data types, and inter-table
data references. Documentation provides 119 table-pair co-
references (cascade-delete lists and data structure descrip-
tions), but does not provide operational coordination guid-
ance.
Procedural knowledge(Phase 2): Expert CASE records
from PIMS demonstration models (Weight Sample: 6 non-
empty records; Gulf Coast Case Sets: 317 records) show
which tables experts modify together, but do not explain
the underlying coordination rationale. Cross-source analy-
sis with documentation schemas identifies candidate coor-
dination rules grounded against column definitions and type

Table 2: Match F1 (m), Row Recall (rR), and Column Recall (cR) across four LLM backbones and six conditions onDtest (100
held-outtasks).Foreachtask,themeanandstandarddeviationarecomputedoverfiveindependentexecutions;thetablereports
their averages across the 100 tasks.
DS-V4-Pro DS-V4-Flash Gemma-4 Qwen-3.6
m r R cR m r R cR m r R cR m r R cR
Baseline .581±.150.852±.036.818±.106.618±.144.832±.072.808±.091.620±.074.830±.031.684±.080.468±.174.829±.055.704±.149
DocOnly .620±.148.858±.034.795±.104.638±.142.824±.076.809±.102.653±.078.827±.034.716±.084.443±.182.817±.067.703±.155
SkillBase .694±.139.860±.050.871±.092.705±.137.835±.094.858±.086.694±.104.835±.050.821±.103.590±.185.835±.087.790±.130
Trace2Skill .747±.092.884±.027.889±.057.698±.123.832±.091.824±.128.771±.039.868±.025.875±.026.656±.117.842±.044.822±.090
SkillOpt .742±.078.884±.034.886±.060.719±.122.862±.073.861±.114.778±.040.872±.023.886±.048.711±.113.852±.043.861±.079
SkillRefine .770±.088.882±.053.905±.045.757±.079.888±.040.897±.042.800±.026.893±.012.909±.015.764±.072.882±.035.897±.035
constraints.ExpertCASErecordsrevealco-modificationpat-
ternsthatencodehowexpertsjointlymodifytables,butcover
at most 5 unique tables per model.
COMinterfacestabilization(Phase3):Theagentwraps
174 COM methods into Python callable functions and de-
signs 61 test cases across 10 functional categories. Through
8 iterative rounds, all 50 executable test cases passed; 11
additional cases were skipped because the corresponding
methodsareunsupportedinPIMSv22.0.11.Noneofthe140
PIMS-Bench tasks depend on skipped methods.
Skill library statistics.Phases 1–3 produce an initial li-
braryof47skilldocuments(∼52KB).AfterPhase4refine-
ment,thelibrarygrowsto57documents(∼80KB):theana-
lyzeridentifiedfailurepatternsnotcoveredbyexistingskills
andsynthesized10newrules.Underprogressivedisclosure,
the agent initially loads only the skill index (∼8.5KB); full
bodies are loaded on-demand.
Skill Conditions and Performance
Acrossthefivedifficultylevels,taskcomplexityscalesstruc-
turally: the average number of tables modified per task in-
creases from 1.2 (L1) to 3.6 (L5), oracle modification com-
ponentsfrom3.5to7.9,andhiddencross-tabledependencies
from 0.7 to 3.5, confirming that PIMS-Bench spans a mean-
ingful range of planning challenges.
Table 2 reports results across four models and six con-
ditions. Figure 3 visualizes the efficiency–accuracy tradeoff
across difficulty levels.
Raw documentation provides inconsistent gains.Rel-
ative to Baseline, DocOnly changes match F1 by +0.039,
+0.020, +0.033, and -0.025 across the four backbones. In
contrast,SkillBaseconsistentlyimprovesmatchF1by0.074–
0.122, indicating that compiling evidence into task-oriented
skill packages is more effective than exposing raw docu-
mentation.SkillRefinefurtherimprovesSkillBaseby0.052–
0.174.
Externalmethodsimprovebutfallshort.Trace2Skill
usestrajectory-levelpatchinductionandhierarchicalconsol-
idation, with construction-set validation for skill selection,
whereasSkillOptapplies bounded edits through a scalar
validationgate.Bothimproveoverthebaseline,demonstrat-
ing the value of trajectory-derived knowledge and iterative
skilloptimization.Allrefinementmethodsusethesamecon-
/uni00000015/uni00000013 /uni00000017/uni00000013 /uni00000019/uni00000013 /uni0000001b/uni00000013 /uni00000014/uni00000013/uni00000013 /uni00000014/uni00000015/uni00000013 /uni00000014/uni00000017/uni00000013
/uni00000024/uni00000059/uni0000004a/uni00000011/uni00000003/uni00000037/uni00000052/uni0000004e/uni00000048/uni00000051/uni00000056/uni00000003/uni00000053/uni00000048/uni00000055/uni00000003/uni00000037/uni00000044/uni00000056/uni0000004e/uni00000003/uni0000000b/uni0000002e/uni0000000c
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019
/uni00000013/uni00000011/uni0000001a
/uni00000013/uni00000011/uni0000001b
/uni00000013/uni00000011/uni0000001c/uni00000030/uni00000044/uni00000057/uni00000046/uni0000004b/uni00000003/uni00000029/uni00000014
/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f/uni00000035/uni00000048/uni00000049/uni0000004c/uni00000051/uni00000048/uni00000003/uni0000000b/uni00000052/uni00000058/uni00000055/uni00000056/uni0000000c
/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f/uni00000025/uni00000044/uni00000056/uni00000048
/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f/uni00000032/uni00000053/uni00000057
/uni00000037/uni00000055/uni00000044/uni00000046/uni00000048/uni00000015/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f
/uni00000025/uni00000044/uni00000056/uni00000048/uni0000004f/uni0000004c/uni00000051/uni00000048
/uni00000027/uni00000052/uni00000046/uni00000032/uni00000051/uni0000004f/uni0000005c
/uni0000002f/uni00000014
/uni0000002f/uni00000015
/uni0000002f/uni00000016 /uni0000002f/uni00000017
/uni0000002f/uni00000018
/uni0000002f/uni00000014
/uni0000002f/uni00000015
/uni0000002f/uni00000016
/uni0000002f/uni00000017
/uni0000002f/uni00000018
/uni0000002f/uni00000014
/uni0000002f/uni00000015
/uni0000002f/uni00000016
/uni0000002f/uni00000017
/uni0000002f/uni00000018
/uni0000002f/uni00000014
/uni0000002f/uni00000015
/uni0000002f/uni00000016
/uni0000002f/uni00000017
/uni0000002f/uni00000018
/uni0000002f/uni00000014
/uni0000002f/uni00000015 /uni0000002f/uni00000016
/uni0000002f/uni00000017
/uni0000002f/uni00000018
/uni0000002f/uni00000014
/uni0000002f/uni00000015
/uni0000002f/uni00000016
/uni0000002f/uni00000017
/uni0000002f/uni00000018
Figure 3: Token efficiency versus accuracy across difficulty
levels (L1–L5). Each line represents one condition;Skill-
Refineachieves the best accuracy–efficiency trade-off, with
larger gains on harder tasks.
struction tasks and PIMS execution interface; they differ in
howexecutionfeedbackisconvertedintoskillupdates.How-
ever,Trace2Skilllacks factorized error diagnosis, while
SkillOpt’s scalar signal does not identify which skill con-
tent should be repaired. In contrast,SkillRefinedecom-
poses failures by compliance and structured match dimen-
sions, then uses signal-conditioned trajectories to localize
targeted repairs.
SkillRefine obtains the highest mean match F1 un-
der all four backbones.Compared with Baseline, Skill-
RefineimprovesmatchF1by0.189,0.139,0.180,and0.296
on DeepSeek-V4-Pro, DeepSeek-V4-Flash, Gemma-4-31B,
and Qwen-3.6-27B, respectively. Relative to SkillBase, the
corresponding improvements are 0.076, 0.052, 0.106, and
0.174. The second-best method is Trace2Skill on DS-V4-
Pro(0.747)andSkillOptonDS-V4-Flash(0.719),Gemma-4
(0.778), and Qwen-3.6 (0.711).
Column recall shows larger gains than row recall.
Amongthereporteddiagnosticmetrics,columnrecallshows
larger gains than row recall on all four backbones, with im-
provementsof0.087–0.225overBaseline.Thisindicatesthat
structured multi-signal refinement specifically helps agents

/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f/uni00000025/uni00000044/uni00000056/uni00000048 /uni0000005a/uni00000012/uni00000052/uni00000003/uni00000046/uni00000052/uni00000050/uni00000053/uni0000004f/uni0000004c/uni00000044/uni00000051/uni00000046/uni00000048/uni00000010
/uni00000046/uni00000052/uni00000051/uni00000047/uni0000004c/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000048/uni00000047/uni00000003/uni00000045/uni00000055/uni00000044/uni00000051/uni00000046/uni0000004b
/uni0000005a/uni00000012/uni00000052/uni00000003/uni00000050/uni00000044/uni00000057/uni00000046/uni0000004b/uni00000010
/uni00000046/uni00000052/uni00000051/uni00000047/uni0000004c/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000048/uni00000047/uni00000003/uni00000045/uni00000055/uni00000044/uni00000051/uni00000046/uni0000004b
/uni00000036/uni0000004e/uni0000004c/uni0000004f/uni0000004f/uni00000035/uni00000048/uni00000049/uni0000004c/uni00000051/uni00000048
/uni0000000b/uni00000032/uni00000058/uni00000055/uni00000056/uni0000000c
/uni00000013/uni00000011/uni00000018/uni00000018
/uni00000013/uni00000011/uni00000019/uni00000013
/uni00000013/uni00000011/uni00000019/uni00000018
/uni00000013/uni00000011/uni0000001a/uni00000013
/uni00000013/uni00000011/uni0000001a/uni00000018
/uni00000013/uni00000011/uni0000001b/uni00000013
/uni00000030/uni00000044/uni00000057/uni00000046/uni0000004b/uni00000003/uni00000029/uni00000014
/uni00000013/uni00000011/uni0000001a/uni0000001a/uni00000013
/uni00000013/uni00000011/uni0000001a/uni00000018/uni0000001a
/uni00000013/uni00000011/uni0000001b/uni00000013/uni00000013
/uni00000013/uni00000011/uni0000001a/uni00000019/uni00000017
/uni00000027/uni00000036/uni00000010/uni00000039/uni00000017/uni00000010/uni00000033/uni00000055/uni00000052
/uni00000027/uni00000036/uni00000010/uni00000039/uni00000017/uni00000010/uni00000029/uni0000004f/uni00000044/uni00000056/uni0000004b
/uni0000002a/uni00000048/uni00000050/uni00000050/uni00000044/uni00000010/uni00000017
/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000010/uni00000016/uni00000011/uni00000019
Figure 4: Ablation of the two signal-conditioned trajectory-
attributionbranches.Eachvariantremovesthecorresponding
localization branch while retaining its diagnostic signal.
identifycorrectcolumnnames—themostfine-grainedoper-
ational knowledge.
The advantage grows with task complexity.Averaged
across the four backbones, the SkillRefine–Baseline gap in-
creases from 10–15pp at L1–L2 to 18–28pp at L3–L5, con-
firming that cross-source skill induction provides the most
value on complex multi-table coordination tasks.
Ablation Study
Weisolatethetwosignal-conditionedattributionbranches.In
each ablation, the diagnostic signal remains available, while
only its trajectory-based localization is removed. Figure 4
reports match F1 across all four backbones.
Refinement is necessary.SkillBase, which uses cross-
source extraction without execution-driven refinement,
achieves match F1 values of 0.590–0.705 across the four
backbones. SkillRefine improves these results to 0.757–
0.800, corresponding to gains of 0.052–0.174, with the
largest improvement on Qwen-3.6-27B.
Both attribution branches contribute.Removing the
compliance-conditionedbranchreducesmatchF1by0.011–
0.041,whileremovingthematch-conditionedbranchreduces
it by 0.016–0.077. The full model performs best on every
backbone, showing that the two branches provide comple-
mentary localization evidence.
Signal-conditioned trajectory attribution is a key dif-
ferentiator.Unlike methods that rely only on execution out-
comes,SkillRefineoverlaystool-usecontextandconsulted
skillsonbothdiagnosticsignals,helpingidentifyrepaircan-
didates that the outcomes alone cannot localize.
Discussion
Cross-sourceinductionisrole-specific,notadditive.Skill-
Refine does not treat documentation and expert CASE
records as symmetric retrieval corpora. CASE records pro-
vide sparse task-level evidence for proposing coordination
patterns, while documentation supplies broad schema and
interface grounding. Execution feedback then filters unsup-
ported hypotheses and repairs incomplete rules. The contri-
bution therefore lies in role-specific evidence composition
rather than knowledge quantity alone.
SkillBase improvement validates induction; SkillRe-
fine validates refinement.The improvement from Base-
line to SkillBase (Table 2) indicates that compiling hetero-
geneous evidence into task-oriented skills is already use-
ful. The further improvement from SkillBase to SkillRefine
shows that execution-driven correction is necessary to re-
move unsupported coordination rules, repair fine-grained
column mappings, and constrain over-generalized proce-
dures. These two gains separately support cross-source in-
duction and execution-driven refinement.
Model-dependent refinement sensitivity.SkillRefine
improves over SkillBase by 0.076 on DeepSeek-V4-Pro,
0.052onDeepSeek-V4-Flash,0.106onGemma-4,and0.174
onQwen-3.6.Thevariationsuggeststhatdifferentbackbones
differ in how effectively they use localized skill corrections,
althoughfurtherevidenceisneededtoexplainthisdifference.
Generalization scope.This study evaluates held-out task
generalization within two PIMS demonstration environ-
ments. The results support execution-driven skill refine-
ment for structured industrial software within the evaluated
environments. Generalization to unseen refinery models,
production-scale deployments, or other industrial planning
platforms remains to be established.
Limitations.(1) Evaluation is limited to one industrial
planning platform (AspenTech PIMS v22.0.11) and two
demonstration models. (2) Construction and test tasks share
thesamemodelenvironmentsandschemavocabulary,sothe
studyevaluatesheld-outtaskgeneralizationratherthantrans-
fer to unseen refinery models. (3) Some planning tasks may
admit multiple valid solutions, while the current structured
matchmetricusesoneexpertreference.(4)Trajectory-based
error-to-skill attribution identifies plausible candidate skills
but does not establish causal responsibility.
Conclusion
We identified a Documentation–Practice Gap in PIMS,
where component-oriented documentation provides broad
structural coverage but lacks task-level coordination, while
expert CASE records expose sparse operational patterns
without explicit schema grounding. SkillRefine bridges this
gap by using expert records to propose coordination pat-
terns, documentation to ground them to valid schemas and
interfaces, and execution evidence to diagnose and repair
candidate skills. Its structured multi-signal refinement sepa-
rates compliance screening from table-, row-, column-, and
value-level diagnosis and uses agent trajectories to narrow
each repair to relevant skill documents. On 100 held-out
tasks from PIMS-Bench, task-oriented SkillBase packages
consistently outperform unguided baselines, and SkillRe-
fine further improves the library, obtaining the highest mean
match F1 under all four evaluated backbones. These results
support execution-driven skill refinement for structured in-
dustrial software, while generalization beyond the evaluated
PIMS environments remains to be established.

References
Agent Skills. 2026. Agent Skills Specification. Accessed:
2026-07-27.
AspenTechnology,Inc.2025.AspenPIMS:ProcessIndustry
ModelingSystem. AspenTechnology,Inc. Processindustry
planning and optimization software.
Chen,H.;Constante-Flores,G.E.;Mantri,K.S.I.;Kompalli,
S.M.;Ahluwalia,A.S.;andLi,C.2025. OptiChat:Bridging
OptimizationModelsandPractitionerswithLargeLanguage
Models.INFORMS Journal on Data Science.
Han,T.;Zhang,Y.;Song,W.;Fang,C.;Chen,Z.;Sun,Y.;and
Hu, L. 2026. SWE-Skills-Bench: Do Agent Skills Actually
Help in Real-World Software Engineering?arXiv preprint
arXiv:2603.15401.
Jimenez, C. E.; Yang, J.; Wettig, A.; Yao, S.; Pei, K.;
Press, O.; and Narasimhan, K. 2024. Swe-bench: Can lan-
guage models resolve real-world github issues? InInter-
national Conference on Learning Representations, volume
2024, 54107–54157.
Li, B.; Mellou, K.; Zhang, B.; Pathuri, J.; and Menache, I.
2023. Largelanguagemodelsforsupplychainoptimization.
arXiv preprint arXiv:2307.03875.
Li, X.; Liu, Y.; Chen, W.; You, B.; Di, Z.; He, Y.; Zheng,
S.; Choe, K. W.; Sun, J.; Wang, S.; et al. 2026. SkillsBench:
Benchmarking how well agent skills work across diverse
tasks.arXiv preprint arXiv:2602.12670.
Liang, J.; Groll, N.; and Sin, G. 2026. Large Language
Model Agent for User-friendly Chemical Process Simula-
tions.arXiv preprint arXiv:2601.11650.
Liang,Y.;Zhong,R.;Xu,H.;Jiang,C.;Zhong,Y.;Fang,R.;
Gu, J.-C.; Deng, S.; Yao, Y.; Wang, M.; et al. 2026. Skill-
net: Create, evaluate, and connect ai skills.arXiv preprint
arXiv:2603.04448.
Liu, N. F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua,
M.; Petroni, F.; and Liang, P. 2023. Lost in the middle:
How language models use long contexts.arXiv preprint
arXiv:2307.03172.
Liu, X.; Luo, X.; Li, L.; Huang, G.; Liu, J.; and Qiao, H.
2026. Skillforge: Forging domain-specific, self-evolving
agent skills in cloud technical support.arXiv preprint
arXiv:2604.08618.
Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.;
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang,
Y.; et al. 2023. Self-refine: Iterative refinement with self-
feedback.Advances in neural information processing sys-
tems, 36: 46534–46594.
Ni, J.; Liu, Y.; Liu, X.; Sun, Y.; Zhou, M.; Cheng, P.; Wang,
D.; Zhao, E.; Jiang, X.; and Jiang, G. 2026. Trace2skill:
Distill trajectory-local lessons into transferable agent skills.
arXiv preprint arXiv:2603.25158.
Polanyi, M. 2009. The tacit dimension. InKnowledge in
organisations, 135–146. Routledge.
Qian, C.; Han, C.; Fung, Y.; Qin, Y.; Liu, Z.; and Ji, H.
2023. Creator: Tool creation for disentangling abstract and
concrete reasoning of large language models. InFindings
of the Association for Computational Linguistics: EMNLP
2023, 6922–6939.
Rho,S.;Smith,L.;Li,T.;Levine,S.;Peng,X.B.;andHa,S.
2025.Languageguidedskilldiscovery.InInternationalCon-
ference on Learning Representations, volume 2025, 87731–
87752.
Shen, S.; Cheng, W.; Ma, M.; Turcan, A.; Zhang, M. J.;
and Ma, J. 2026. Skillfoundry: Building self-evolving agent
skilllibrariesfromheterogeneousscientificresources.arXiv
preprint arXiv:2604.03964.
Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K.; and
Yao, S. 2023. Reflexion: Language agents with verbal re-
inforcement learning.Advances in neural information pro-
cessing systems, 36: 8634–8652.
Song, H.; and Wei, S. 2026. More Skills, Worse Agents?
Skill Shadowing Degrades Performance When Expanding
Skill Libraries.arXiv preprint arXiv:2605.24050.
Team, G. 2026. Gemma 4 Technical Report.arXiv.
Wang, G.; Xie, Y.; Jiang, Y.; Mandlekar, A.; Xiao, C.; Zhu,
Y.; Fan, L.; and Anandkumar, A. 2023. Voyager: An open-
ended embodied agent with large language models.arXiv
preprint arXiv:2305.16291.
Wang, H.; Lan, Y.; Cao, B.; Lin, L.; and Chen, J. 2026.
SkillGrad: Optimizing Agent Skills Like Gradient Descent.
arXiv preprint arXiv:2605.27760.
Xia, P.; Chen, J.; Wang, H.; Liu, J.; Zeng, K.; Wang, Y.;
Han, S.; Zhou, Y.; Zhao, X.; Chen, H.; et al. 2026. Skillrl:
Evolvingagentsviarecursiveskill-augmentedreinforcement
learning.arXiv preprint arXiv:2602.08234.
Xu, A.; Lin, B.; Xue, B.; Wang, B.; Xu, B.; Wu, B.; Zhang,
B.; Lin, C.; Dong, C.; Ling, C.; et al. 2026. Deepseek-v4:
Towards highly efficient million-token context intelligence.
arXiv preprint arXiv:2606.19348.
Xu, R.; and Yan, Y. 2026. Agent skills for large language
models: Architecture, acquisition, security, and the path for-
ward.arXiv preprint arXiv:2602.12430.
Yang,A.;Li,A.;Yang,B.;Zhang,B.;Hui,B.;Zheng,B.;Yu,
B.;Gao,C.;Huang,C.;Lv,C.;etal.2025. Qwen3technical
report.arXiv preprint arXiv:2505.09388.
Yang, Y.; Gong, Z.; Huang, W.; Yang, Q.; Zhou, Z.; Huang,
Z.;Li,Y.;Gao,X.;Dai,Q.;Liu,B.;etal.2026. Skillopt:Ex-
ecutivestrategyforself-evolvingagentskills.arXivpreprint
arXiv:2605.23904.
Yao,S.;Zhao,J.;Yu,D.;Shafran,I.;Narasimhan,K.R.;and
Cao, Y. 2022. React: Synergizing reasoning and acting in
language models. InNeurIPS 2022 Foundation Models for
Decision Making Workshop.
Zhu, J.; Zhang, Y.; Ma, Z.; Zhang, B.; Schoepf, A.; Woloch,
D.; Wang, P. Y.; Yang, G. R.; Jacob, S.; Nagisetty, S.; et al.
2026. SpreadsheetBench 2: Evaluating Agents on End-
to-End Business Spreadsheet Workflows.arXiv preprint
arXiv:2606.29955.
