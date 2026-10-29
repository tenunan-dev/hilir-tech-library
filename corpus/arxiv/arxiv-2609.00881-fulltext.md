---
source_id: "arxiv"
title: "Towards Natural Gas Contract Selection"
url: "https://arxiv.org/abs/2609.00881"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.00881. Abstract: Towards Natural Gas Contract Selection
via Quantum-Guided Independent Set Reduction
Vivek Dixit,1,∗ Vaibhaw Kumar,1 Kentaro Ohno,1 Alberto Maldonado Romo, 1 and Larry Bowden 2,†
1IBM Research
2Woodside Energy
(Dated: September 2, 2026)
Selecting mutually compatible natural gas transportation contracts is a practically important
optimization task in which operators must choose from many candidate a"
---

# Towards Natural Gas Contract Selection

Towards Natural Gas Contract Selection
via Quantum-Guided Independent Set Reduction
Vivek Dixit,1,∗ Vaibhaw Kumar,1 Kentaro Ohno,1 Alberto Maldonado Romo, 1 and Larry Bowden 2,†
1IBM Research
2Woodside Energy
(Dated: September 2, 2026)
Selecting mutually compatible natural gas transportation contracts is a practically important
optimization task in which operators must choose from many candidate agreements subject to tem-
poral, infrastructural, and flow-related constraints. As the number of candidates grows, the resulting
search space becomes difficult to explore exhaustively. We study a pairwise abstraction of this task,
formulated as a Maximum Clique problem on a contract-compatibility graph, or equivalently as a
Maximum Independent Set (MIS) problem on the complement graph.
Building on recent work, this paper studies a quantum–classical framework for solving large-scale
MIS instances within the limitations of noisy quantum hardware. The approach combines iterative
classical graph reduction with quantum-guided optimization to progressively simplify the search
space while maintaining high solution quality. This enables large candidate spaces to be reduced to
smaller subproblems that are more suitable for execution on current quantum computers.
We evaluate the approach on fifteen benchmark instances from theQuantum Optimization Bench-
marking Library(QOBLIB), obtaining an average approximation ratio of 0.996 and recovering op-
timal solutions for fourteen instances, including graphs with up to 186 vertices. We further evaluate
the algorithm on six synthetic pairwise contract-compatibility graphs containing up to 900 contracts,
where the proposed method achieves an average approximation ratio of 0.989 and obtains optimal
solutions in four cases. These experiments demonstrate the ability of the hybrid MIS solver to re-
duce industrially motivated graphs. The pairwise abstraction serves as the first step of a two-stage
screening procedure that narrows the candidate contracts to a smaller set of mutually compatible
ones, which can then be verified against pipeline-capacity constraints.
I. INTRODUCTION
In large-scale energy transportation systems, efficiently
allocating limited pipeline capacity is an important oper-
ational and economic challenge. Selecting mutually com-
patible natural gas transportation contracts is a prac-
tically important optimization task in which operators
must choose from many candidate agreements subject to
temporal, infrastructural, and flow-related constraints.
As the number of candidate contracts grows, the search
space becomes increasingly difficult to explore exhaus-
tively. In this work, we consider a pairwise abstraction
of this task in which contracts are represented as ver-
tices of a compatibility graph and pairwise compatibility
relationships are represented as edges. Solving the Max-
imum Clique problem on this compatibility graph yields
the largest subset of mutually compatible contracts.
The Maximum Independent Set (MIS) problem is a
fundamental combinatorial optimization problem defined
on an undirected graphG= (V, E), where the objective
is to identify the largest subsetS⊆Vsuch that no two
vertices inSare adjacent [1]. The MIS problem is closely
related to the Maximum Clique through graph comple-
mentation: a maximum clique in a graphGcorresponds
exactly to a maximum independent set in its complement
graph ¯G[2]. As one of Karp’s original NP-complete prob-
∗ vivekdixit@ibm.com
† larry.bowden@woodside.com
lems [3], MIS has no known polynomial-time exact algo-
rithm unless P = NP, and remains notoriously difficult
to solve and approximate in the worst case [4]. Con-
sequently, exact algorithms exhibit exponential scaling,
while heuristic methods may return sub-optimal solu-
tions and lack optimality guarantees. The computational
challenges become particularly severe for large and dense
graphs encountered in practical applications, including
finance [5, 6], wireless network scheduling [7], bioinfor-
matics [8], compiler register allocation [9], and computer
vision feature matching [10]. The inherent computational
complexity of MIS has therefore motivated investigat-
ing alternative computing paradigms, including hybrid
quantum–classical optimization algorithms [6, 11–13].
A variety of exact algorithms has been developed for
MIS, each balancing generality against computational ef-
ficiency. Branch-and-bound methods systematically par-
tition the solution space, pruning subproblems whose
upper bounds fall below the incumbent solution [14].
The Bron–Kerbosch algorithm [15], applicable to MIS
via graph complementation, remains a foundational ref-
erence, with refinements by Tomita and Seki [16] improv-
ing performance on sparse graphs. For structured graphs,
dynamic programming yields polynomial-time solutions
on perfect graphs [17], interval graphs [18], and bounded-
tree width graphs [19]. Integer Linear Programming
(ILP) formulations encode MIS as a binary optimiza-
tion over vertex-selection variables subject to edge con-
straints, and modern solvers such as CPLEX and Gurobi
with branch-and-cut strategies have extended solvable in-
arXiv:2609.00881v1  [quant-ph]  1 Sep 2026

2
stance sizes considerably [20, 21]. More recently, branch-
and-reduce frameworks such as KaMIS combine exact
kernelization (data reduction) rules with branch-and-
bound search, enabling exact solutions on sparse real-
world graphs with millions of vertices that are intractable
for classical branch-and-bound alone [22, 23]. Never-
theless, all exact methods share exponential worst-case
complexity and can become prohibitive on dense, weakly
structured graphs beyond a few hundred vertices [24] —
precisely the regime encountered in large-scale natural
gas transportation networks.
Given the intractability of exact methods, heuristic
and approximation algorithms have been developed to
obtain high-quality solutions within acceptable time.
Greedy algorithms iteratively select the minimum-degree
vertex and remove its neighbours, running in polynomial
time but yielding solutions far from optimal on dense
or adversarially structured graphs [25, 26]. Metaheuris-
tics overcome this by exploring broader regions of the
solution space: Simulated Annealing accepts worsening
moves with a temperature-controlled probability to es-
cape local optima [27], while Tabu Search maintains a
memory structure that forbids recently visited configu-
rations [28]. Both have demonstrated substantially im-
proved quality over greedy initialization [29]. For mas-
sive sparse networks, ReduMIS intermixes polynomial-
time kernelization with an evolutionary local-search al-
gorithm, iteratively fixing likely-optimal low-degree ver-
tices to reopen the reduction space, and has been shown
to find near-optimal or provably optimal solutions on
graphs with millions of vertices where classical meta-
heuristics stall [22]. Semidefinite Programming (SDP)
relaxations represent the strongest known polynomial-
time approximation providing guarantees via the Lov´ asz
theta functionϑ(G) [30], yet no polynomial-time algo-
rithm can approximate MIS withinn 1−ϵ under standard
assumptions [31]. In natural gas transportation schedul-
ing, where solution quality directly impacts revenue, the
degraded performance of classical heuristics highlights
challenges that motivate the investigation of alternative
computational approaches.
Classical MIS methods face bottlenecks that limit
their applicability to large-scale, time-sensitive problems.
Heuristics alleviate computational cost but introduce a
quality–speed trade-off: greedy methods sacrifice opti-
mality, while metaheuristics require careful tuning with
no formal guarantee of solution quality [32] — a critical
limitation in revenue- and safety-sensitive applications.
Most fundamentally, local search methods are susceptible
to entrapment in local optima on the highly non-convex
MIS energy landscape [33]. In natural gas transportation
scheduling, where the conflict graph can involve hundreds
to thousands of nodes and decisions must be made in
near-real time [34], these limitations motivate investigat-
ing alternative algorithms, including quantum-classical
methods. A key enabler is the Quadratic Unconstrained
Binary Optimization (QUBO) formulation, which recasts
the MIS problem as the minimization of a quadratic ob-
jective over binary variables [35, 36], which is compat-
ible with many quantum optimization algorithms, such
as the Quantum Approximate Optimization Algorithm
(QAOA) [11]. QAOA employs parameterized variational
circuits to generate high-quality approximate solutions
and has been demonstrated for MIS on superconducting
quantum processors [12, 37]. However, the limitations of
noisy intermediate-scale quantum (NISQ) hardware [38],
including restricted qubit counts, shallow circuit depths,
and gate errors, currently prevent purely quantum meth-
ods from solving large industrial-scale optimization prob-
lems efficiently.
To overcome these limitations, quantum–classical algo-
rithms combine the strengths of classical preprocessing
with quantum-guided optimization. Schuetzet al.[13]
proposedqReduMIS, which integrates classical kernel-
ization with quantum-derived information to identify
vertices that are likely to belong to large independent
sets, thereby enabling additional graph reductions. The
method was validated on hardware-native random Union
Jack graph instances using Rydberg quantum hard-
ware, demonstrating improved performance relative to
the other quantum optimization methods considered in
that study. Similarly, Wyboet al.[39] introduced a hy-
brid MIS algorithm that combines shallow-depth QAOA
(p= 4) with a classical greedy heuristic using pre-
computed QAOA parameters. Their approach was im-
plemented on a 20-qubit superconducting quantum pro-
cessor and reported improved solution quality relative to
classical greedy heuristics on the regular graph instances
considered. More recently, Yalovetzkyet al.[6] proposed
a quantum–classical framework for portfolio diversifica-
tion, formulated as an MIS problem. Their method uses
QAOA measurements to identify likely optimal vertices,
enabling further optimal classical reductions rather than
relying on QAOA to directly construct the final solu-
tion. Evaluated on real financial datasets using QAOA
with depthp= 2 on a trapped-ion processor, the al-
gorithm solved quantum subproblems using up to 78
qubits, achieved average approximation ratios exceeding
0.96, and outperformed standalone QAOA on the largest
benchmark instances.
This work studies how quantum-informed recursive
MIS reduction can be adapted to superconducting
quantum hardware and applied to industrially moti-
vated natural-gas contract-selection problems. Build-
ing on recent qReduMIS-style ideas, we combine ex-
act graph reductions, QAOA-derived marginal selection,
hardware-aware circuit synthesis, and hierarchical pa-
rameter optimization. We test the algorithm on in-
stances from theQuantum Optimization Benchmarking
Library(QOBLIB) [40] as well as synthetic instances of
the considered contract scheduling problem, where it con-
sistently finds near-optimal solutions.
Concretely, the framework converts the problem into a
QUBO model, iteratively applies classical MIS reduction
rules to simplify the graph, and processes the resulting
irreducible kernel with the Quantum Approximate Opti-

3
mization Algorithm (QAOA), using the measured vertex-
inclusion probabilities to steer subsequent reductions un-
til the graph is fully resolved. Relative to prior hybrid
MIS solvers, the specific contributions of this paper are
as follows:
•Domain adaptation to natural gas contract
scheduling.We cast the contract-selection prob-
lem in natural gas pipeline transportation as a
Maximum Clique instance on a pairwise contract-
compatibility graph and, via graph complementa-
tion, solve it as an MIS problem with the pro-
posed hybrid solver. We formalize the compati-
bility model—temporal overlap, shared infrastruc-
ture, pairwise capacity screening, priorities, and
flow conflicts—and clearly delimit its scope, show-
ing where the pairwise abstraction departs from
a full pipeline schedule with cumulative segment–
period capacity constraints.
•Hardware-aware circuit synthesis.We intro-
duce a connectivity-aware circuit synthesis that
embeds the QUBO interaction graph onto the qubit
topology of an IBM superconducting processor
given a limited SW AP budget. Combined with a
hierarchical QAOA parameter schedule (depth-one
grid search, COBYLA refinement, and recursive
depth extension), this helps control the two-qubit
depth and enables finding high-quality solutions of
MIS kernels containing up to 125 qubits on 156-
qubit hardware.
•Systematic benchmarking on QOBLIB.We
evaluate the solver on fifteen MIS instances from
the Quantum Optimization Benchmarking Library
(QOBLIB), spanning 17–186 vertices and 39–5,173
edges. Against CPLEX-verified optima the hybrid
solver attains an average approximation ratio of
0.996 and recovers the exact optimum on fourteen
of fifteen instances, providing a hardware-executed
evaluation to the open benchmark suite.
•Empirical analysis of quantum marginals
versus uniform selection.We isolate the con-
tribution of the quantum stage using a matched
uniform-sampling baseline that differs only in how
candidate vertices are selected after each reduction
step. We then quantify the advantage of guid-
ing reductions using the full QAOA measurement
distribution rather than relying solely on a single
lowest-energy bitstring. For theC125-9instance
from QOBLIB, the quantum-guided strategy con-
centrates substantially more probability mass on
high-quality solutions—for example, it is 12×more
likely to reach an independent set of size 31 or
larger and recovers the optimum in cases where
uniform sampling never does—providing evidence
that the marginal probabilities contain valuable in-
formation for guiding reductions.
A word on scope is warranted before we pro-
ceed. At the problem sizes that fit today’s quan-
tum hardware, classical exact MIS solvers—branch-
and-reduce and kernelization-based tools such as
KaMIS/ReduMIS [22]—are both faster and exact, and
we make no claim to surpass them. Our contribu-
tion is instead methodological. The value lies in the
pipeline itself—hardware-aware embedding, the hierar-
chical QAOA schedule, and quantum-guided reduction—
which transfers to near-term quantum optimization more
broadly; here MIS is the measuring stick, not the prod-
uct. We adopt it as a testbed precisely because its
known optima and strong classical reductions let us iso-
late and quantify the quantum contribution, and be-
cause it admits a genuine hardware demonstration with
ground truth known at up to 125 qubits. The bet we
make explicit is that the quantum workload scales with
qubit count rather than with problem size, so the same
architecture is positioned to ride future hardware into
the dense regimes where exact classical methods break
down. This paper should therefore be read as near-term
quantum-optimization methods research validated on a
benchmarkable problem, not as a faster MIS solver.
The remainder of this paper is organized as fol-
lows. Section II presents the methodology, including the
QUBO and Ising formulation, the classical reduction and
decomposition stages, the hardware-aware circuit syn-
thesis, the QAOA parameter-optimization schedule, and
the quantum-guided reduction procedure together with
its randomized baseline. Section III reports the experi-
mental evaluation on the QOBLIB benchmarks and the
natural gas contract-compatibility graphs, including de-
tailed case studies, the statistical analysis of quantum
marginals versus random selection, and the runtime and
run-to-run reproducibility of the solver. Section IV con-
cludes and discusses directions for future work.
II. METHODOLOGY
Within this section we formally introduce the consid-
ered problem and describe each stage of the algorithm
in detail, from the contract-compatibility graph through
the iterative reduce–QAOA–select loop to the final inde-
pendent set, as summarized in Figure 1.
A. Problem F ormulation
As defined in Section I, the Maximum Independent
Set (MIS) problem seeks a maximum-cardinality subset
S⊆Vof an undirected graphG= (V, E) such that no
two vertices inSare adjacent.
We define binary decision variablesx i ∈ {0,1}for each
vertexi∈V, wherex i = 1 indicates that vertexiis
included in the independent set. The MIS problem can

4
FIG. 1. Overview of the proposed hybrid quantum–classical workflow. Transportation contracts form a compatibility graph
G, whose complement ¯Gis solved as a Maximum Independent Set (MIS) instance. The hybrid solver then alternates between
deterministic classical reduction, which fixes provably-optimal vertices, and hardware-aware QAOA, whose measured marginal
probabilitiesp i rank the remaining vertices; the highest-scoring vertex is added to the independent set and its closed neigh-
borhoodN[v] is removed. The reduced graph re-enters the loop until no vertices remain, at which point the accumulated set
Stotal, i.e., the constructed set of mutually compatible contracts, is returned.
be formulated as a Binary Linear Program (BLP)
max
x∈{0,1}n
X
i∈V
xi
subject tox i +x j ≤1,∀(i, j)∈E,
xi ∈ {0,1},∀i∈V.
(1)
Because the variables are binary, the adjacency con-
straintx i +x j ≤1 is equivalent to the quadratic con-
straintx ixj = 0 for every (i, j)∈E. This representation
is convenient for constructing a QUBO formulation, in
which violations of the independence constraints are in-
corporated into the objective through quadratic penalty
terms. The QUBO formulation reads
min
x∈{0,1}n
−
X
i∈V
xi +P
X
(i,j)∈E
xixj,(2)
whereP >1 is a penalty parameter that ensures any op-
timal solution of the QUBO corresponds to a maximum
independent set, and where we switched to minimization
to follow common conventions. The first term encour-
ages the selection of as many vertices as possible; the
second term penalizes simultaneous selection of adjacent
vertices. The conditionP >1 is sufficient because each
selected vertex lowers the objective by exactly 1, so any
edge violation incurs a penaltyP >1 that outweighs
the gain of the additional vertex; every optimal QUBO
solution is therefore edge-free and hence a maximum in-
dependent set.
For execution on quantum hardware, the QUBO is
mapped to an Ising Hamiltonian via the substitution
xi = (1−z i)/2, wherez i ∈ {−1,+1}are spin variables.
Replacing eachz i withZ i, the Pauli-Zoperator acting
on qubiti, yields the cost Hamiltonian
HC =
X
i∈V
hiZi +
X
(i,j)∈E
JijZiZj + const.(3)
where the coefficients are given by
hi = 12 − P4 Xj:(i,j)∈E 1 (4)
= 12 − P4 deg(i),(5)
Jij = P4 ,∀(i, j)∈E,(6)
with the constant offset equal to− 12 |V|+ P4 |E|. Any
ground state ofH C encodes an optimal MIS solution,
andH C serves as the cost operator in the quantum op-
timization.

5
B. Graph Preprocessing and Reduction
The hybrid solver begins with a classical preprocess-
ing stage that reduces the problem size before quantum
optimization. Deterministic graph reduction rules elimi-
nate vertices whose membership in a maximum indepen-
dent set (MIS) can be decided exactly, after which the
remaining graph is relabeled and decomposed into con-
nected components. While the reduction may eliminate
some globally optimal solutions when multiple optima
exist, it is guaranteed to preserve at least one maximum
independent set.
Given an input graphG= (V, E), reduction rules
are applied iteratively until no further simplifications are
possible. The vertex set is partitioned into three dis-
joint subsets: vertices provably belonging to a MIS, de-
notedS classical; vertices excluded from further consider-
ation, denotedR classical; and the remaining undecided
vertices, which induce the reduced graphG ′ = (V ′, E′).
Let deg(v) denote the degree of vertexvandN(v) =
{u∈V|(u, v)∈E}its neighborhood. The following
reduction rules are applied.
A vertex containing a self-loop cannot belong to an
independent set:
(v, v)∈E=⇒v∈R classical.(7)
An isolated vertex can always be included:
deg(v) = 0 =⇒v∈S classical.(8)
A degree-one vertex is always preferred over its unique
neighbour:
deg(v) = 1, N(v) ={u}=⇒
(
v∈S classical,
u∈R classical. (9)
If the neighborhood of a vertex forms a clique, the ver-
tex dominates all of its neighbours and can be selected:
∀u, w∈N(v),(u, w)∈E=⇒
(
v∈S classical,
N(v)⊆R classical.
(10)
The overall reduction is expressed as
(G′, Sclassical, Rclassical) =Reduce(G).
Vertices inS classical are immediately added to the par-
tial independent set, while only the reduced graphG ′ is
forwarded to the quantum optimization stage.
To simplify the subsequent QUBO formulation and es-
tablish a one-to-one correspondence between graph ver-
tices and qubits, the vertices ofG ′ are relabeled with
consecutive integers. Let
ϕ:V original → {0, . . . ,|V′| −1}
denote the relabeling map andϕ −1 its inverse. The rela-
beling preserves graph connectivity and enables measure-
ment outcomes to be mapped back to the original vertex
labels after quantum execution.
Finally, the reduced graph is decomposed into its con-
nected components,
G′i = (V ′i , E′i), i= 1, . . . , m,
which are processed independently in non-increasing or-
der of size,|V ′1 | ≥ |V′2 | ≥ · · · ≥ |V′m|. Since no edges exist
between distinct components, each component defines an
independent optimization problem. This decomposition
reduces the number of qubits required per quantum exe-
cution and enables multiple components to be solved in
parallel when quantum resources are available.
C. Hardware-Aware Quantum Circuit Generation
To reduce routing overhead and limit circuit depth dur-
ing compilation, the reduced problem graph is approxi-
mately mapped onto a hardware-compatible interaction
graph before constructing the quantum circuit. Figure 2
illustrates the overall procedure.
A hardware compatibility graph containing the same
number of vertices as the reduced problem graph is first
constructed by modeling the target hardware as a linear
qubit topology. In this graph, two qubits are considered
adjacent if they can interact within a specified SW AP
budget. A linear chain forms a subgraph of the heavy-
hex coupling architecture used by current IBM super-
conducting quantum processors. Consequently, target-
ing this topology allows us to reach full connectivity in
|V ′| −2 layers of SW AP gates [41, 42]. Crucially, since
noise deteriorates the performance of QAOA it is typi-
cally advantageous to generate the QAOA ansatz from
a sub-set of the edges of the reduced graph [43]. A
simulated-annealing heuristic is then used to map the
QUBO interaction graph onto the hardware compatibil-
ity graph, maximizing the number of problem interac-
tions that can be implemented within the SW AP budget
while preserving connectivity of the resulting interaction
graph.
Rather than being fixed in advance, the SW AP bud-
getk swap is determined individually for each problem
instance. Starting from a small value,k swap is incre-
mentally increased until the embedding produces a con-
nected interaction graph, i.e., a single connected compo-
nent without isolated qubits. The smallest budget satis-
fying this condition is selected. Since simulated anneal-
ing is inherently stochastic, different random seeds can
generate different valid embeddings, resulting in vary-
ing two-qubit gate counts and circuit depths. After de-
termining the minimum feasible SW AP budget, multi-
ple random seeds are therefore evaluated, and the em-
bedding producing the lowest two-qubit circuit depth is
retained. This criterion is motivated by the fact that
two-qubit gate count and depth are the primary contrib-
utors to noise accumulation on superconducting quan-
tum hardware. The selected hardware-compatible inter-
action graph directly defines the Hamiltonian generat-
ing the QAOA circuit. Because the mapped interaction

6
FIG. 2. Hardware-aware embedding of the problem interaction graph onto a linear qubit topology. The problem interaction
graph (left) is mapped by a simulated-annealing heuristic onto a linear hardware-compatibility graph, in which two qubits
interact only if they lie within the SW AP budgetk swap. At a small budget (center) some interactions exceed the budget and
the represented graph is disconnected; increasingk swap (right) yields a single connected component, and the smallest such
budget is retained. Solid arcs denote interactions realizable within the budget; dashed arcs denote interactions beyond it.
Among the seeds that achieve connectivity, the embedding with the smallest two-qubit depth is selected.
graph already conforms to the target hardware connec-
tivity, transpilation requires little or no additional rout-
ing, producing shallower quantum circuits with reduced
two-qubit gate overhead. Related work has applied sim-
ulated annealing to reduce SW AP overhead in QAOA
compilation. Montanez-Barreraet al.[44] use simu-
lated annealing to optimize qubit ordering within SW AP-
network and parity-twine-chain encodings, directly min-
imizing two-qubit gate count –similar in its use of an-
nealing, but operating within a fixed circuit encoding
rather than on an abstract hardware compatibility graph.
Dupontet al.[45] embedp=1 QAOA subgraphs onto a
linear qubit chain, sharing our line-topology target but
using a SAT-solver-based isomorphism search instead of
a stochastic heuristic, and without an instance-adaptive
SW AP budget. U.S. Patent No. 11,537,770 [46] describes
a simulated-annealing procedure that generates candi-
date qubit-to-hardware subgraphs via depth-first search
or swaps, accepted with a temperature-dependent prob-
ability – algorithmically the closest match to our search
mechanics, though it optimizes mapped-circuit fidelity
rather than connectivity and edge coverage, and is not
specific to a line topology or QAOA.
D. QAOA Parameter Optimization
The Quantum Approximate Optimization Algorithm
(QAOA) [47] of depthpis parameterized by
θ= (β 1, . . . , βp, γ1, . . . , γp)
whereβ i andγ i are the variational parameters associ-
ated with the mixer and cost layers, respectively. These
parameters define the variational quantum state|ψ(θ)⟩,
which is obtained by applying the parameterized QAOA
circuit to the initial uniform superposition state. The
parameters are optimized to minimize the expectation
value of the ideal QUBO cost Hamiltonian,
E(θ) =⟨ψ(θ)|H C|ψ(θ)⟩,(11)
whereH C denotes the original cost Hamiltonian derived
directly from the QUBO formulation. Note thatH C
is distinct from the Hamiltonian implemented by the
compiled quantum circuit. In our hardware-aware ap-
proach, the circuit realizes an approximate hardware-
compatible Hamiltonian obtained after the interaction
graph is modified to satisfy the connectivity constraints
of the target device. Consequently, the optimized quan-
tum state is prepared using the approximate compiled
Hamiltonian, while its quality is evaluated with respect
to the original objective HamiltonianH C. Because
the landscape is highly non-convex, a three-stage op-
timization strategy is employed, following operational
guidance on parameter-setting methods for utility-scale
QAOA [48] and implemented using the open-source
qaoa training pipeline[49].
a. Stage 1: depth-one grid search.Atp= 1 the en-
ergy can be evaluated exactly and efficiently from the
graph structure alone, without full statevector simula-
tion [50]. The parameter space is scanned on a uniform
40×40 grid overγ∈[0, π/2] andβ∈[0, π]; the lowest-
energy pair provides the initialization for Stage 2.
b. Stage 2: local refinement atp= 1.Starting from
the grid-search result, the derivative-free COBYLA opti-
mizer [51] is run for up to 500 iterations with initial trust-
region radiusρ= 0.05, yielding the optimized depth-one
parameters (γ ∗1 , β∗1 ).

7
c. Stage 3: recursive depth extension.The depth-
ksolution is extended to depthk+ 1 using the linear
interpolation scheme of Zhou et al. [52]. Treating the
koptimized parameters as samples at integer knot po-
sitions 1, . . . , k, a new vector ofk+ 1 values is formed
by re-sampling atk+ 1 evenly spaced points over [1, k],
with boundary values preserved exactly and interior val-
ues obtained by linear interpolation. The extended vec-
tor initializes COBYLA at depthk+ 1. This step is
repeated until the target depthpis reached. The tar-
get depthpis selected per instance in an incremental
fashion. The solver begins with a shallow circuit and in-
creasesponly when the current depth fails to recover a
satisfactory solution, exploiting the fact that the recur-
sive scheme reuses the depth-kparameters to warm-start
depthk+ 1. Easier kernels are therefore solved at low
depth (p= 2–3), while a larger depth (up top= 5) is
reserved for the hardest kernels, keeping the circuit as
shallow as possible for each problem. This accounts for
the range ofpvalues reported in Table IX. Forp≥2,
the objective is evaluated using the Pauli propagation
method [50, 53, 54], which evolves the observableH C
backwards through the circuit in the Heisenberg picture
and reads off the expectation value as the coefficient of
the identity string. Pauli strings with weight exceed-
ing six or absolute coefficient below 10 −3 are discarded,
keeping the classical cost polynomial for the circuits con-
sidered here.
E. Quantum-Guided Graph Reduction and
Iterative Optimization
The quantum component of the proposed hybrid solver
is used as a probabilistic oracle to provide vertex-
selection information for iterative graph reduction. The
QAOA variational parameters are optimized entirely on
a classical computer using the Pauli propagation method
described previously. After obtaining the optimized pa-
rameter vector
θ∗ = (β∗1 , . . . , β∗p , γ∗1 , . . . , γ∗p ),
the parameters are bound to the circuit, which is sub-
sequently executed on IBM superconducting quantum
hardware. Therefore, the quantum processor is used ex-
clusively for sampling candidate solutions, while the vari-
ational optimization remains entirely classical.
For each reduced subproblem, the optimized circuit is
executed forN shots measurements, generating a multiset
of bitstringsM={(b i, ni)}, whereb i ∈ {0,1}n andn i
denotes the number of occurrences of bitstringb i. Each
measured bitstring is evaluated using the implemented
Ising Hamiltonian
H=
X
i
hiZi +
X
(i,j)
JijZiZj,
with corresponding energy
E(b) =
X
i
hisi +
X
(i,j)
Jijsisj,
wheres i = 1 forb i = 0 ands i =−1 otherwise. The
samples are ranked according to increasing energy, with
lower-energy states corresponding to higher-quality can-
didate independent sets.
Rather than selecting only the single lowest-energy
solution, the solver exploits the statistical information
contained in the low-energy measurement distribution.
Specifically, only a fractionfof the lowest-energy bit-
strings is retained, corresponding to approximatelyN B ≈
f Nshots samples. The marginal inclusion probability of
vertexiis estimated from this filtered sample setBas
pi = 1NB Xb∈B, bi=1 nb, N B = Xb∈B nb.
These marginal probabilities provide an estimate of the
likelihood that a vertex belongs to a high-quality inde-
pendent set while reducing the impact of high-energy
noise-dominated measurements.
The estimated probabilities are then used to guide clas-
sical graph reduction. Vertices with inclusion probability
exceeding a confidence thresholdτ(set toτ= 0.9; Ta-
ble I) are selected directly. The remaining vertices are
ranked using
score(v) = pv
deg(v) + 1,(12)
which balances the probability of selecting a vertex
against the number of vertices removed when it is in-
cluded. Vertices are greedily selected in descending score
order while maintaining the independent-set constraint.
The score function admits an expected-gain interpre-
tation. LetI ∗ denote a target maximum independent set
and define the indicator variable
Xv =
(
1, v∈I ∗,
0,otherwise. (13)
Interpreting the estimated marginal probability as the
probability that vertexvbelongs to the target solution
gives
E[Xv] =p v.
Selecting vertexvremoves its closed neighborhoodN[v],
containing
|N[v]|= deg(v) + 1
vertices from further consideration. Therefore, the ex-
pected contribution per eliminated vertex is
E[∆] = E[Xv]|N[v]| = pvdeg(v) + 1,(14)

8
which corresponds directly to Eq. (12). Hence, the greedy
selection rule can be interpreted as maximizing the ex-
pected independent-set contribution per unit of graph
reduction.
The reliability of the estimated marginals depends on
the number of retained low-energy samples. Let ˆp v de-
note the empirical marginal estimated fromN B samples.
Since ˆpv is an empirical average of bounded binary vari-
ables, Hoeffding’s inequality gives
Pr[|ˆpv −p v| ≥ϵ]≤2 exp(−2NBϵ2).(15)
Applying a union bound over alln=|V ′|kernel ver-
tices, all marginals are estimated within an errorϵwith
confidence 1−δprovided
NB ≥ 12ϵ2 ln 2nδ .(16)
Because the score function divides the marginal by
deg(v) + 1≥1, the corresponding score estimates inherit
the same uniform accuracy bound. Thus, a sufficiently
large measurement budget enables a reliable estimation
of thep v produced by QAOA without explicit error mit-
igation [55].
The measured marginals exhibit strong non-
uniformity, indicating that the quantum circuit provides
informative vertex-selection probabilities rather than
random assignments. Figure 3 shows the marginal
probabilities obtained during the first reduction round
of QOBLIB instancees60fst02. The probabilities
range from values above 0.8 to almost zero, producing a
clear separation between frequently and rarely selected
vertices. In contrast, uniform random sampling would
assignp i = 0.5 to all vertices. This separation provides
the basis for the quantum-guided reduction strategy.
The complete hybrid optimization procedure is itera-
tive. LetG (0) = (V (0), E(0)) denote the input graph.
At each iteration, deterministic classical reduction rules
are first applied to remove vertices that can be safely
selected or discarded. The remaining connected com-
ponents are then processed using the hardware-aware
QAOA workflow and the quantum-guided selection pro-
cedure described above. After selecting a set of vertices
S(r), the selected vertices and their neighbours are re-
moved:
G(r+1) =G (r) \N[S (r)], N[S] =S∪ [
v∈S
N(v).
The process is repeated until the graph becomes empty or
the maximum iteration limit is reached. The final inde-
pendent set is obtained by combining all vertices selected
during deterministic reductions and quantum-guided it-
erations. The complete procedure is summarized in Al-
gorithm 1.
The algorithm terminates when eitherV (r) =∅or the
iteration limit is reached. In practice, most instances are
resolved before reaching the maximum iteration count
because deterministic reductions and quantum-guided se-
lections progressively decrease the graph size.
25 50 75 100 125
Vertices ranked by marginal probability
0.0
0.2
0.4
0.6
0.8
Marginal inclusion probability pi
uniform sampling: pi = 0:5
pmax = 0:816
30 vertices
above uniform baseline
FIG. 3. QAOA marginal inclusion probabilitiesp i for the first
reduction round ofes60fst02(124-vertex kernel), sorted in
decreasing order. The dashed horizontal line marks the value
pi = 0.5 expected from uniform random sampling; the 30 ver-
tices lying above this baseline (blue) carry the selection sig-
nal, with the largest marginal reachingp max = 0.816. The
non-uniform distribution of marginals provides the vertex-
selection information exploited by the proposed reduction
strategy.
Algorithm1Hybrid quantum-guided MIS solver
Require:graphG (0) = (V, E); max iterationsR; shots
Nshots; low-energy fractionf; confidence thresholdτ
Ensure:independent setS total
1:S total ← ∅;r←0
2:whileV (r) ̸=∅andr < Rdo
3:(G ′, Scl, Rcl)←Reduce(G (r))
4:S total ←S total ∪S cl
5:ifV(G ′) =∅then
6:break
7:end if
8:for allconnected componentsG ′i ofG ′ do
9:build hardware-aware QAOA circuit forG ′i
10:optimizeθclassically
11:sampleN shots bitstrings on QPU
12:retain low-energy fractionfand estimate
marginalsp i
13:select vertices usingp v/(deg(v) + 1) with threshold
τ
14:end for
15:update graph by removing selected vertices and neigh-
bors
16:r←r+ 1
17:end while
18:returnS total
F. Uniform Baseline for Quantum Sampling
To quantify the contribution of the quantum-guided
vertex selection mechanism, we introduce a uniform sam-
pling variant of the proposed hybrid MIS solver. This
experiment is designed as a controlled ablation study in
which the quantum sampling stage is replaced by uni-
formly random vertex priorities while all other compo-

9
nents of the algorithm remain unchanged. The objective
is to isolate the information provided by the quantum
stage and determine whether the quantum-generated sig-
nal offers meaningful guidance beyond uniform selection.
The uniform sampling baseline is therefore not in-
tended as a comparison against competitive classical MIS
heuristics. Replacing the quantum component with a
specialized classical method, such as degree-based greedy
selection or tabu search, would instead evaluate the rel-
ative performance of different node-selection strategies
rather than the contribution of quantum information
itself. The absolute performance of the proposed hy-
brid solver is evaluated separately against exact CPLEX
solutions (cf. Sections III A and III E). Thus, this
comparison should be interpreted as an ablation of the
quantum-guided component rather than a benchmark
against state-of-the-art classical MIS algorithms.
The uniform sampling baseline preserves the same it-
erative framework as the proposed hybrid method. At
each iteration, the current graph is first processed using
the identical classical reduction rules. Vertices that can
be deterministically included in the independent set or
safely removed are handled accordingly. If no vertices
remain after reduction, the algorithm terminates. Oth-
erwise, the quantum optimization stage is replaced by
a randomized greedy selection procedure. Each remain-
ing vertex is assigned an independent priority sampled
from a uniform distribution. The vertex with the high-
est remaining priority is selected and added to the in-
dependent set if none of its neighbors has already been
included. The selected vertex and all of its neighbors
are then removed from the graph, and the reduction and
randomized selection steps are repeated until the graph
becomes empty. The final independent set is obtained by
combining the vertices selected during the deterministic
reduction stage with those selected through the random-
ized procedure.
Because the classical preprocessing, graph updates,
and greedy selection mechanism are identical in both ap-
proaches, the only difference lies in the source of the
vertex-selection information: quantum-generated sam-
ples in the proposed solver and uniformly random pri-
orities in the ablation variant. Therefore, differences in
solution quality can be attributed to the additional in-
formation provided by the quantum optimization stage.
To account for the stochastic nature of the randomized
baseline, it is executed using multiple random seeds,
and the resulting distribution of independent-set sizes is
compared with that obtained from the proposed hybrid
solver.
The parameters governing the QUBO construction,
quantum sampling, and hybrid iteration are summarized
in Table I. Unless stated otherwise, these values were
held fixed across all reported experiments.
TABLE I. Solver and quantum-execution settings used
throughout the experiments (unless stated otherwise).
Parameter V alue
QUBO penalty parameterP2
Shots per circuitN shots 20,000
Low-energy fraction retained for marginalsf0.5
Direct-selection confidence thresholdτ0.9
Maximum hybrid iterations 25
Random-baseline runsN R 10–40
p= 1 grid-search resolution 40×40
COBYLA maximum iterations 500
COBYLA initial trust-region radiusρ0.05
Pauli-propagation weight cutoff 6
Pauli-propagation coefficient cutoff 10 −3
G. Quantum Optimization Benchmarking Library
(QOBLIB) Benchmark Instances
The proposed hybrid MIS solver was evaluated on in-
stances from QOBLIB [40]. QOBLIB defines ten clas-
sically hard combinatorial optimization problem classes,
including the Maximum Independent Set (MIS) problem,
along with corresponding problem instances and refer-
ence solutions to enable fair, reproducible benchmarking.
We selected 15 MIS instances from QOBLIB, varying in
size and structure; see Table II.
H. Pairwise Natural Gas Contract-Compatibility
Abstraction
The proposed hybrid MIS solver is evaluated on a nat-
ural gas pipeline transportation contract-selection prob-
lem. The objective is to identify the largest set of mu-
tually compatible transportation contracts that can be
executed simultaneously. This problem is formulated as
a Maximum Clique problem on a compatibility graph,
where vertices represent contracts and edges connect
pairwise compatible contracts. Since a maximum clique
in a graph is equivalent to a maximum independent set
in its complement, the proposed solver is applied to the
complement graph.
Each transportation contract is characterized by
its type (firm or interruptible), transportation capac-
ity, transportation rate, receipt and delivery locations,
pipeline segments, and delivery schedule. Synthetic
benchmark instances are generated by randomly assign-
ing one to four pipeline segments and delivery weeks to
each contract while varying an overlap factor. Increas-
ing the overlap factor increases competition for pipeline
resources, producing denser compatibility graphs with
more challenging conflict structures.
Two contracts are considered pairwise compatible if
they can be executed simultaneously without violat-
ing the graph-generation rules, which account for tem-
poral overlap, shared pipeline infrastructure, pairwise

10
capacity-screening thresholds, contract priorities, and
simulated flow conflicts. An edge is added between every
compatible pair, yielding a compatibility graph whose
complement defines the MIS instance solved by the pro-
posed algorithm.
The resulting graph is apairwise abstractionof the
underlying transportation problem. It does not explicitly
enforce cumulative segment–period capacity constraints
of the form
X
i∈S
aist ≤C st,
wherea ist denotes the load contributed by contraction
segmentsduring periodt, andC st is the corresponding
segment capacity. Consequently, a clique in the com-
patibility graph may still violate aggregate capacity lim-
its when three or more individually compatible contracts
collectively exceed the available capacity. The industrial
case study therefore evaluates the proposed algorithm on
synthetic pairwise compatibility graphs, and the reported
solutions should be interpreted as optimal with respect
to the pairwise compatibility model rather than as fully
validated pipeline schedules. Details of the benchmark
generation process are provided in Appendix A.
The following proposition characterizes precisely when
this pairwise abstraction is an exact representation of the
underlying feasibility structure.
Proposition 1(Exactness of the pairwise compatibil-
ity graph).LetFdenote the family of feasible contract
subsets, and suppose feasibility is hereditary (downward
closed), with every singleton contract feasible. Construct
a compatibility graphG c = (V, Ec)in which(i, j)∈E c if
and only if the pair{i, j}is feasible. Then the cliques of
Gc coincide exactly withFif and only if every infeasible
contract set contains an infeasible pair.
Proof.(⇐) Assume every infeasible set contains an in-
feasible pair. IfSis a clique ofG c, then every pair in
Sis feasible, soScontains no infeasible pair and must
therefore be feasible. Conversely, ifS∈ F, hereditary
feasibility implies that every pair of contracts inSis fea-
sible, so every pair forms an edge ofG c andSis a clique.
(⇒) Assume the cliques ofG c coincide withF. If
an infeasible setScontained only feasible pairs, then
every pair of vertices inSwould be adjacent, makingS
a clique and hence feasible, a contradiction. Therefore
every infeasible set must contain an infeasible pair.
Proposition 1 shows that the clique (equivalently, MIS)
formulation is exact only when infeasibility arises solely
from pairwise conflicts. It is no longer exact when higher-
order resource constraints, such as cumulative segment–
period capacity limits, render a set of pairwise compatible
contracts jointly infeasible.
Rather than a shortcoming of the overall selection
workflow, this motivates the intended role of the pair-
wise MIS solver as the first stage of a two-stage screen-
ing procedure. The purpose of the first stage is not to
certify a fully feasible operating schedule, but to nar-
row an intractably large selection space—exponentially
many contract subsets—down to a small family of mutu-
ally compatible, high-cardinality candidate sets that can
then be checked against the cumulative constraints. In
this second stage, each candidate independent setSis
verified against the cumulative segment–period capacity
constraints Pi∈S aist ≤C st for every pipeline segment
sand periodt. This verification is inexpensive: it is a
linear arithmetic check over the retained contracts rather
than a combinatorial search. Candidate sets that satisfy
all aggregate limits are directly feasible, whereas those
that violate a segment–period limit can be repaired by
removing the smallest-value conflicting contracts or by
re-solving the MIS on the residual graph. This decompo-
sition confines the computationally hard combinatorial
search—where the quantum-guided solver is applied—
to the pairwise-compatibility layer, while the aggregate-
capacity constraints are enforced by the cheap down-
stream verification stage.
For this two-stage decomposition to be sound in the
sense of discarding no truly feasible selection, the pair-
wise incompatibility rule must be arelaxationof the un-
derlying feasibility structure: a contract pair should be
declared incompatible only when that pair on its own al-
ready violates a capacity or operational limit, which is
a necessary condition for the joint feasibility of any set
containing it. Under such a rule every feasible set re-
mains pairwise compatible, so the compatibility graph
over-approximates the feasible family and the first stage
introduces no false negatives; the cumulative-capacity
check in the second stage then removes the surviving false
positives. We note that the synthetic generator used in
this study instead applies a conservative pairwise capac-
ity screen with a fractional thresholdθ(α)C s < Cs (Ap-
pendix A), which is a proxy chosen to control graph den-
sity rather than a strict relaxation; a deployment aiming
at the soundness guarantee above would set the pairwise
rule accordingly. A full evaluation of the complete two-
stage pipeline, including cumulative-capacity verification
and hydraulic constraints on realistic network data, is
left to future work.
III. RESUL TS AND DISCUSSION
The experimental evaluation of the proposed hybrid
quantum–classical framework is organized into five parts.
First (Section III A), we present benchmark results across
fifteen diverse QOBLIB instances, demonstrating solu-
tion quality and comparing against the uniform sam-
pling baseline. Second and third, we provide detailed
case studies of the iterative hybrid optimization pro-
cess on two representative benchmarks—C125-9 and
es60fst02—illustrating the synergy between classical re-
duction and quantum-guided optimization and analyz-
ing the statistical properties of the resulting solution
distributions. Fourth (Section III D), we report the

11
runtime, resource usage, and run-to-run reproducibil-
ity of the solver on the QOBLIB instances. Fifth
(Section III E), we evaluate performance on large-scale
synthetic compatibility graphs representing natural gas
contract-selection problems, validating practical applica-
bility at industrially relevant scales. Characteristics of
the transpiled QAOA circuits are summarized separately
in Appendix B.
A. Benchmark Performance and Comparison with
the Randomized Baseline
Table II evaluates 15 benchmark instances (17–186 ver-
tices, 39–5,173 edges), comparing the exact CPLEX op-
timum against a uniform-sampling baseline and the pro-
posed hybrid quantum–classical (Q–C) solver under iden-
tical run budgets.
The Q–C solver achieves an average best-solution ap-
proximation ratio of0.996, recovering the CPLEX opti-
mum on 14 of 15 instances (93.3%). The sole exception
issloane 1dc 128(best MIS of 15 vs. optimum 16, ratio
0.938). Optimal solutions are also recovered on larger,
harder instances such ases60fst02andC125-9(up to
186 vertices), indicating that quantum guidance remains
useful even when classical reduction leaves a substantial
residual search space.
By contrast, uniform sampling fails to reach the
optimum on four instances—ibm32,sloane 1dc 128,
es60fst02, andC125-9—with ratios of 0.92, 0.94, 0.99,
and 0.94, respectively. The Q–C solver closes this gap on
three of the four (ibm32,es60fst02,C125-9), matching
uniform sampling’s 0.94 only onsloane 1dc 128.
Search consistency also improves: across 200 total
runs, the Q–C solver recovers its best observed solution
in 42% of runs versus 28% for uniform sampling—a 50%
relative increase, with gains on 7 of 15 instances. The
largest improvements are onfootball(2/10→10/10),
farm(6/10→10/10),ibm32(2/10→8/10), and
insecta-ant-colony1-day38(3/10→9/10); smaller
gains appear fores60fst03,sloane 1dc 128, and
C125-9. Frequencies are unchanged on six instances, and
onlysloane 2dc 128declines (6/10→5/10).
The solution distributions show the clearest benefit.
Foribm32, the Q–C solver reaches the optimum in 8/10
runs versus 2/10 for uniform sampling. Fores60fst02,
uniform sampling never reaches the optimum of 88, while
Q–C does so in 5/20 runs. The largest shift is onC125-9:
uniform sampling has a mean MIS of 28.05 and reaches
size≥31 in only 5% of runs, while Q–C raises the mean
to 30.45, reaches size≥31 in 60% of runs, and hits the
optimum of 34 twice.
On easier instances—e.g.,karateandes60fst01,
where both methods reach the optimum every run—
quantum guidance offers little added benefit, since uni-
form priorities already suffice.
Overall, classical reduction removes most of the search
space, and the QPU supplies marginal probability in-
formation that biases the residual classical search to-
ward promising regions. This raises the aggregate best-
solution recovery frequency from 28% to 42% and the av-
erage approximation ratio from 0.986 to0.996, convert-
ing three previously suboptimal uniform-sampling cases
into optimal ones. The benefit is most apparent when
classical reduction leaves a sufficiently difficult residual
problem.
B. Detailed Case Study: C125-9 Benchmark
1. Iterative Hybrid Optimization Process
Table III presents the round-by-round execution of the
proposed hybrid quantum–classical MIS solver on the
C125-9 benchmark. Starting from the original graph
containing 125 vertices, the algorithm iteratively applies
classical reduction, executes the quantum MIS solver on
the reduced graph, and removes the selected MIS vertex
together with its neighbors. This process continues until
the graph is completely eliminated after 21 rounds.
During the first fifteen rounds, the classical reduc-
tion stage is unable to identify any mandatory MIS ver-
tices, resulting in ∆MIS C = 0 throughout this phase.
Consequently, the reduction in graph size is driven en-
tirely by the quantum solver, which consistently con-
tributes one vertex to the independent set in each it-
eration (∆MIS Q = 1). Depending on the degree of the
selected vertex, between two and six neighboring vertices
are removed in each round, reducing the graph from 125
vertices to 47 vertices while constructing an independent
set of size 15.
As the graph becomes smaller, the classical reduction
stage becomes increasingly effective. From Round 16 on-
ward, classical reductions contribute additional MIS ver-
tices with ∆MISC values of 1, 3, 4, 1, and 5, respectively.
These reductions substantially accelerate graph simplifi-
cation by identifying vertices that are guaranteed to be-
long to the maximum independent set without requir-
ing further quantum optimization. The largest reduction
occurs in Round 18, where four vertices are identified
through classical reduction and one additional vertex is
selected by the quantum solver. Together with the re-
moval of eight neighboring vertices, the graph size de-
creases from 30 to 17 vertices in a single iteration. In the
final round, the classical reduction identifies the remain-
ing five MIS vertices, leaving a residual graph of three
vertices that is eliminated without invoking the quantum
solver (∆MISQ = 0).
The hybrid solver constructs a maximum independent
set of size 34 after 21 iterations while completely elimi-
nating the graph. CPLEX verification confirms this is the
optimal solution, demonstrating the complementary roles
of the quantum and classical components: the quantum
solver provides steady progress when classical reductions
are initially ineffective, while the classical reduction stage
becomes increasingly powerful as the graph shrinks.

12
TABLE II. Comparison of uniform sampling and the proposed quantum–classical method across the benchmark instances.
“Best Approx. Ratio Run” denotes the number of runs that achieved the method’s best observed MIS size, reported as a
fraction of the total number of runs. The approximation ratio is defined as the best MIS size obtained by the method divided
by the CPLEX-optimal MIS size.
Uniform Sampling Quantum–Classical
Instance Nodes Edges CPLEX Runs Best Approx.Ratio Run Approx.Ratio Best Approx.Ratio Run Approx.Ratio
karate 34 78 20 10 10/10 1.00 10/10 1.00
farm 17 39 10 10 6/10 1.00 10/10 1.00
football 35 118 16 10 2/10 1.00 10/10 1.00
ibm32 32 90 13 10 2/10 0.92 8/10 1.00
es60fst01 123 159 60 10 10/10 1.00 10/10 1.00
chesapeake 39 170 17 10 2/10 1.00 2/10 1.00
sloane 1dc 64 64 543 10 20 1/20 1.00 1/20 1.00
insecta-ant-colony1-day38 56 1134 6 10 3/10 1.00 9/10 1.00
sloane 2dc 128 128 5173 5 10 6/10 1.00 5/10 1.00
es60fst03 113 142 55 10 2/10 1.00 5/10 1.00
es60fst04 162 238 78 10 1/10 1.00 1/10 1.00
sloane 1dc 128 128 1471 16 10 4/10 0.94 5/10 0.94
sloane 1zc 128 128 1120 18 10 1/10 1.00 1/10 1.00
es60fst02 186 280 88 20 5/20 0.99 5/20 1.00
C125-9 125 787 34 40 1/40 0.94 2/40 1.00
2. Statistical Analysis of Solution Quality
To evaluate the distributional advantage of quantum-
guided optimization, we compare solution quality across
repeated executions on C125-9. The random baseline
(NR = 40 runs) and quantum algorithm (N Q = 40 runs,
QAOA depthp= 3) produce markedly different distri-
butions (Table IV, Figure 4).
The quantum algorithm achieves substantially higher
central tendency: a mean MIS size of 30.45 versus 28.05
for the random baseline (a difference of 2.40 vertices),
with median values of 31 versus 28. More significantly,
the quantum approach exhibits pronounced advantages
in the high-quality tail. At thresholdk= 31 it is 12×
more likely to succeed (60.0% versus 5.0%), and this ad-
vantage widens to 14×atk= 32 (35.0% versus 2.5%).
Atk= 33 and at the optimal sizek= 34 the random
baseline never succeeds, whereas the quantum algorithm
still reaches these sizes in 17.5% and 5.0% of runs, re-
spectively (Table V). Overall, the quantum algorithm
places 60.0% of its probability mass on solutions of size
31 or larger, compared with only 5.0% for the random
baseline.
We quantify the separation between the two distribu-
tions with Cliff’sδ, a nonparametric effect-size measure
that requires no distributional assumptions and is defined
as
δ=
{(i, j) :Qi > Rj} − {(i, j) :Qi < Rj}
NQ ·N R
,(17)
whereQ i andR j range over theN Q quantum-classical
andN R uniform random MIS sizes. It equals the dif-
ference between the probability that a randomly drawn
quantum-classical solution exceeds a random baseline so-
lution and the reverse probability, soδ∈[−1,1]: val-
ues near 0 indicate stochastically identical distributions,
while|δ|>0.474 conventionally denotes a large ef-
fect [56]. Hereδ= 0.649 confirms a large effect size, in-
dicating that the quantum-classical distribution stochas-
tically dominates the random baseline to a substantial
degree. In concrete terms, a randomly drawn quan-
tum solution would be superior approximately 82.5% of
the time. These results provide strong evidence that
quantum-guided optimization learns non-trivial search
heuristics that bias sampling toward the high-quality re-
gion of the solution space, with the benefit most pro-
nounced precisely where it matters most: at the frontier
of best achievable solution quality.
C. Detailed Case Study:es60fst02Benchmark
1. Iterative Optimization Dynamics
Table VI presents the evolution of the hybrid solver on
es60fst02(186 vertices). The algorithm achieves com-
plete graph elimination after ten rounds, recovering the
optimal MIS size of 88 (verified by CPLEX).
Classical reduction demonstrates exceptional effective-
