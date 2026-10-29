---
source_id: "arxiv"
title: "A Bilevel Market Equilibrium Model for Natural Gas Pipeline Network"
url: "https://arxiv.org/abs/2610.14339"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2610.14339. Abstract: A Bilevel Market Equilibrium Model for Natural Gas Pipeline Network
Operations: Convex Relaxations and Single-level Reformulations
Novel Kumar Dey 1, Afrooz Jalilzadeh 1, Erfan Yazdandoost Hamedani 1, Saif R. Kazi 2 and Anatoly Zlotnik 2
Abstract— We propose an integrated market equilibrium
model for determining the spot market prices and flow rates
in a natural gas pipeline network. The tradition"
---

# A Bilevel Market Equilibrium Model for Natural Gas Pipeline Network

A Bilevel Market Equilibrium Model for Natural Gas Pipeline Network
Operations: Convex Relaxations and Single-level Reformulations
Novel Kumar Dey 1, Afrooz Jalilzadeh 1, Erfan Yazdandoost Hamedani 1, Saif R. Kazi 2 and Anatoly Zlotnik 2
Abstract— We propose an integrated market equilibrium
model for determining the spot market prices and flow rates
in a natural gas pipeline network. The traditional approach
solves the market equilibrium model separately from the
natural gas network flow allocation problem in a sequential
manner. Our proposed framework synthesizes marketing and
operations by using a bilevel optimization formulation where
the market equilibrium model in the upper level is connected
and simultaneously solved with the natural gas network flow
model in the lower level. We introduce convex relaxations for
the nonconvex Weymouth pipe pressure drop equation and
a surrogate for the compressor operating cost. Furthermore,
we compare multiple single level reformulations of the bilevel
problem based on Karush-Kuhn-Tucker (KKT) optimality
conditions, Wolfe duality, and Lagrange duality conditions.
Numerical studies on a small 6-node network demonstrates
the efficacy and accuracy of our model and the comparison
between different duality and optimality based reformulations.
I. INTRODUCTION
The urgent need to increase electricity supplies worldwide
is driving rapid construction of natural gas-fired generators to
service base load in the power grid as well as to compensate
for variability and intermittency in concurrently expanding
renewable electricity sources [1]. The resulting interdepen-
dence between energy flows in gas pipelines and the power
grid, as well as markets for wholesale electricity and natural
gas has motivated methods to coordinate operations [2], [3]
as well as financial markets for wholesale power and gas in
day-ahead and in real-time markets [4]. Gas-electric system
interdependence results in complex market dynamics [1], in
which actions in one market influence outcomes in both.
A major difference between how the power grid and
gas pipelines function is the degree to which physical and
financial decision-making are integrated. For the power grid,
system operators dispatch generators based on the outcomes
of optimal power flow (OPF) optimization problems [5].
Generation asset managers provide structured bids to the
wholesale electricity market administrator, and the market
*Research presented in this article was supported by the Laboratory
Directed Research and Development program of Los Alamos National Lab-
oratory under Exploratory Research project number 20261039ER. Research
conducted at Los Alamos National Laboratory is done under the auspices
of the National Nuclear Security Administration of the U.S. Department of
Energy under Contract No. 89233218CNA0000001. Los Alamos National
Laboratory report number LA-UR-26-29038.
1Department of Applied Mathematics (Novel Dey) and Systems
and Industrial Engineering (Afrooz Jalilzadeh and Erfan Yazdandoost
Hamedani), University of Arizona, Tucson, USA.{ndey, afrooz,
erfany}@arizona.edu
2Applied Mathematics & Plasma Physics, Theoretical Division,
Los Alamos National Laboratory, Los Alamos, USA.{skazi,
azlotnik}@lanl.gov
is cleared day-ahead and in near real-time using optimiza-
tion. The OPF problem determines the power production
setpoints for participating generators that meet demand,
satisfy transmission constraints, and minimize cost. The dual
variables are interpreted as locational marginal prices of
power [6]. In contrast, gas pipelines are built to provide
a given transportation capacity on each segment, and gas
transportation service is sold to shippers [7], [8]. This first
stage typically uses capacity models, and does not consider
physical variables such as pressure or flow. Pipeline operators
then determine compressor settings and the flow allocation
on the pipeline that satisfy consumer nominations.
Researchers have examined problem formulations to syn-
thesize financial and operating processes in gas pipeline net-
works using optimization [9], [10], [11]. A proposed solution
is the optimal gas flow (OGF) problem, which has been ex-
amined in steady-state [12], [13] and dynamic contexts [14],
[15]. While it can be used to produce physical and financial
solutions, the OGF is a single-level nonlinear program (NLP)
formulation that additively includes competing terms that
maximize revenue and minimize compressor operating costs
in the objective function. While the OGF can be interpreted
as a representation of an efficient market for congestion
pricing on a pipeline network, it does not represent the actual
two-stage function of wholesale gas markets and operations.
In addition, the nonlinearity and nonconvexity of gas flow
equations warrants careful interpretation of the dual solution
in the OGF and other optimization problems for natural gas
networks.
To model the hierarchical interplay between economic
trading and physical transport in liberalized gas markets,
recent studies established multi-level equilibrium frameworks
where upper-level market participants optimize competitive
choices while lower-level transmission system operators
(TSOs) enforce physical network constraints [16], [17].
Because embedded lower-level physics that are governed
by non-convex equations like the Weymouth pressure-drop
relationship preclude standard Karush–Kuhn–Tucker (KKT)
or strong-duality reformulations, concurrent studies intro-
duced tailored convex relaxations (such as second-order
cone bounds) coupled with disjunctive cuts and branch-and-
bound techniques [18], [19]. This integration of physical
transport dynamics with convex relaxation schemes yields
computationally tractable single-level reformulations that rig-
orously account for TSO control, market power, and network
bottlenecks in large-scale natural gas grids.
In this study, we develop a bi-level optimization formu-
lation that represents the wholesale market and operating
arXiv:2610.14339v1  [math.OC]  9 Oct 2026

solution stages of decision making related to flow scheduling
in gas pipeline systems. The upper or outer level is a
capacity model that maximizes economic value for pipeline
users based on supply and demand bids, and accounts for
regulated tariffs on each pipeline segment. The lower or inner
level solves an optimal gas flow problem that minimizes
the cost of gas compressor operation to deliver the cleared
gas nominations subject to the physical and engineering
constraints used in the OGF. We then apply and compare
various convex relaxations and single-level reformulations,
including Karush-Kuhn-Tucker (KKT) based mathematical
program with complementarity constraints (MPCC) [20],
Wolfe-duality (WDP) [21], Mond-Weir (MDP) [22], and
Lagrange-dual [23] reformulations. Our key contribution is a
theorem on projection of feasible sets and lifting of feasible
points for these reformulations, and we use a market equi-
librium test case for a small synthetic network to compare
the latter using several performance metrics.
The remainder of the paper is as follows. In Section II, we
describe the bilevel market equilibrium problem expansion
of the OGF. In Section III, we describe convexification
of the equality constraints that represent steady-state gas
flow through a pipe. In Section IV, we describe single-level
reformulations of the bilevel problem, and then state and
prove our main feasibility equivalence theorem. We describe
the test case and numerical experiments in Section V, and
then conclude in Section VI.
II. BILEVELGASNETWORKMARKETMODEL
The Natural Gas market equilibrium flow model is formu-
lated as a bilevel optimization problem. The upper or outer
level optimization represents the market equilibrium problem
with a cost based economic objective function constrained
to limits on supply and demand of natural gas. The lower
or inner level problem is the traditional optimal gas flow
(OGF) which minimizes the operating cost of the pipeline
network constrained to the physical gas flow dynamics and
the pressure and network flow limits.
A. Market Equilibrium problem
The market equilibrium optimization (MEO) problem
maximizes the total economic surplus by minimizing the
production/injection cost minus the sales revenue from sup-
plying the natural gas demand. The objective function for
the upper problem (φ u) is written as:
Φu = ∑
j∈G
Cj(g j)− ∑
i∈D
Vi(di) +θcT ∑
i j∈P
fi j,(1)
where the sets of producer and consumer are denoted byG
andD,C j(g j)denote producerj’s production cost andV i(di)
the value of demand served to consumeri. Additionally, a
cost term on pipe flows in the network is included with
parameterθand per unit flow costc T . This term can rep-
resent network flow based tariffs or additional maintenance
cost of using the pipeline network. Also, there are capacity
based limits on the injection or production flowsg j and
the withdrawal or consumer flowsd i. The complete market
equilibrium problem can be formulated as:
(Pupper)ming j,di Φu = ∑j∈GCj(g j)− ∑i∈DVi(di) +θcT ∑i j∈P fi j
(2a)
s.t.g j ≤g j ≤ g j,(2b)
di ≤d i ≤ di,(2c)
∑
j
g j −∑
i
di =0.(2d)
Note that without the tariff term, i.e. ifθ=0, the market
equilibrium model is agnostic to the pipeline network.
B. Optimal Gas Flow (OGF) problem
The natural gas operations problem or the OGF requires
solving an optimization problem with physics based con-
straints on the pressure and flow rates of natural gas inside
the pipes and minimizing the operations cost for compres-
sors. This is done by modeling the natural gas pipeline
network as a connected graph with pipe junctions represented
by nodes with node-setNand arc/edges representing the
pipes and compressors with setE=P∪C, wherePandC
are the disjoint sets of pipes and compressors.
1) Nodal balance constraints:At each node in the net-
work, the net incoming (∂ −) and outgoing (∂ +) flow is
balanced with the total withdrawal of natural gas,
∑
i∈∂ −j
fi j − ∑
k∈∂ +j
f jk =g j −d j,∀j∈N.(3)
The nodal flow balance constraint can be rewritten in vector
form using the incidence matrixA∈R |N|×|E|,
Af=B gg−B dd.(4)
where the matricesB g ∈R |N|×|G| andB d ∈R |N|×|D| place pro-
ducers and consumers at their nodes. Each column of these
two matrices contains one unit entry and is zero otherwise.
Note that, the model does not consider the compressor fuel
withdrawals and other mass losses.
2) Pressure Drop Constraint:Across each pipe(i,j)∈P,
the pressure drop in natural gas flow is given by the steady-
state Weymouth equation
Πi −Π j =ω i j fi j|f i j|,i j∈P,(5)
whereΠ i =p 2 is the squared gas pressure at nodes andω i j =
a2λi jLi j
A2i jDi j is the pipe resistance coefficient withadenote the
wave speed of natural gas.λ,L,AandDdenote the friction
factor, length, cross-section area and diameter of the pipe
respectively [24]. The Weymouth equation is nonlinear and
nonconvex constraint because of thef|f|term.
3) Compressor balance:For compressors(i,j)∈C, the
pressure across the compressor is modeled as a simple
constraint using the compressor ratio variableαsuch that:
Π j −α i jΠi =0,i j∈C,(6)
with bounds on the compressor ratio as 1≤α≤α max.

4) Slack node:At each slack node in the network, the
pressure is fixed to a constant value,
Πs =K,(7)
whereΠ s denotes the squared slack pressure.
5) Gas-network limit constraints:Each pipe and compres-
sor edge in the networke∈Ehas finite flow capacities. Pipes
permit flow in either direction, whereas compressors operate
only in their prescribed direction:
− fi j ≤f i j ≤ fi j,i j∈P,(8)
0≤f i j ≤ f i j,i j∈C.(9)
At each node, squared pressure satisfies
Πi ≤Π i ≤ Πi,i∈N,(10)
whereΠ i and Πi are lower and upper pressure limits.
6) Compressor Work Objective:The objective of the
optimal gas flow problem is to minimize the operating cost
of compressors. The compressor cost is directly proportional
to the compressor work,
Wc = ∑
i j∈C
fi j(αmi j −1),(11)
wheremdenotes the isotropic coefficient andW c denotes the
total compressor work done by the compressors [25].
7) Problem Formulation:The complete formulation of the
optimal gas flow (OGF) problem is
(Plower)minα Φl =c eWc(α)(12)
s.t. Eq.(4)−(11).(13)
Herec e denotes the per-unit electricity cost andΦ l is the
total operating cost of compressors, which is used as the
lower level objective function.
C. Bilevel Problem
The bilevel gas network market model solves both the
market equilibrium optimization (MEO) jointly with the
optimal gas flow (OGF) problem. The upper level variables,
i.e., injection or productiongand withdrawal or consumer
flowsd, are the parameters in the lower level OGF problem
in Eq.(4), whereas the lower level variable viz. the pipe flow
rates appear in the upper level objective function. The entire
bilevel gas network problem can thus be formulated as:
(P)min
g j,di,α
Φu = ∑
j∈G
Cj(g j)− ∑
i∈D
Vi(di) +θcT ∑
j∈P
f j
(14a)
s.t. Eq.(2b)−(2c),(14b)
α=argmin α Φl =c eWc(α),(14c)
s.t. Eq.(4)−(11).(14d)
This bilevel problem formulation exactly represents the inter-
play between the natural gas market and the pipeline network
operations.
III. CONVEXRELAXATIONS
Bilevel optimization problems are structurally non-convex
and NP-hard [20], making it very difficult to find their
optimal solutions. Typical methods reformulate the bilevel
problem into a single level optimization problem using
either the optimality or duality conditions on the lower level
problem. It is known that optimal solutions of the single level
reformulation need not be optimal for the original bilevel
problem [20]. However, it has been shown that if the lower
level problem is convex and the global solution of the single
level reformulation lies in the interior of it’s feasible region,
then the solution is a global optimal point to the bilevel
problem [26].
The original bilevel gas network market optimization prob-
lem formulated in Eq. (14) is both nonlinear and nonconvex.
We thus propose convex relaxations to the lower level
problem such that the leader-follower formalism from [26]
is applicable in this case. The main non-convexities in the
lower level problem arise from the objective function, the
bilinear compressor equalities, and the nonlinear Weymouth
equation. In the following subsections, we propose convex
reformulations for the objective function which substitutes
the compressor ratios, and relax the Weymouth equalities
using a set of convex hull inequalities for fixed directional
flow.
A. Convex Objective
In the lower level OGF problem, the objective is to min-
imize the operating cost of compressors using the adiabatic
compression work expression, which is a non-convex func-
tion of the compressor ratioα(see Eq.(11)). Alternatively,
we can also use a convex surrogate for the compressor work
in the form of pressure drop across compressors,
˜Φl =β c ∑
i j∈C
(Π j −Π i),(15)
whereβ c can be used as a scaling parameter to adjust
the magnitude of surrogate function with the nonconvex
compressor work. This is based on the fact that gas pipeline
operators explicitly control the compressor discharge pres-
sure (Π j) and try to minimize the pressure rise i.e. difference
between inlet and outlet pressures as shown in Eq. (15).
B. Equivalent compressor constraints
The compressor equality (6) is bilinear in the decision
variablesα i j andΠ i. After replacing the compressor-work
objective by Eq. (15), the ratio variables appear only in this
equality and their bounds. Since operating pressures satisfy
Πi >0, eliminatingα i j gives the equivalent affine constraints
(
Πi −Π j ≤0,i j∈C,
Π j −α maxΠi ≤0,i j∈C. (16)
Conversely, every pressure pair satisfying Eq. (16) defines an
admissible ratioα i j =Π j/Πi ∈[1,α max]. Thus, this elimina-
tion preserves the feasible flow-pressure pairs and introduces
no additional relaxation. Hence the follower variables can
therefore be written asy= (f,Π).

C. Convexified Weymouth Equation
We obtain the convex relaxation of the nonlinear Wey-
mouth equation, through two distinct modeling steps: (i)
selecting an operating direction for each pipe and (ii) relaxing
the corresponding Weymouth equality.
1) Fixed-direction assumption:In the exact model, a pipe
(i j∈P) may carry gas in either direction. Its reference
orientation definesf i j >0 as flow fromitojandf i j <0 as
flow fromjtoi.
We now assume that each pipe operates only in its
reference orientation and impose
0≤f i j ≤ fi j,i j∈P.(17)
The permitted direction of each pipe is chosen during model
construction and held fixed throughout optimization. The
solver determines the nonnegative flow rate in that specified
direction. On this flow interval,f i j|f i j|=f 2i j term in the
Weymouth equation becomes
Πi −Π j =ω i j f 2i j,i j∈P.(18)
This restriction selects a single quadratic branch of the
signed Weymouth relation over a bounded flow interval.
However, the equality graph in Eq. (18) remains nonconvex;
selecting a direction alone does not convexify the pipe
constraint. For a fixed market allocationx, letY fd(x)denote
the exact network feasible set with the additional nonnegative
pipe-flow restrictions. Then
Yfd(x)⊆Y ex(x).(19)
Thus, fixing directions restricts the exact model rather than
relaxes it. Market allocations that are feasible with bidirec-
tional pipe flows may become infeasible under the selected
operating directions.
2) Convex relaxation of pipe constraints:Figure 1(a)
shows the exact bidirectional Weymouth relation. The di-
rection restriction in Eq. (17) selects its nonnegative branch,
Πi −Π j =ω i j f 2i j, whose equality graph remains nonconvex.
We now replace this graph by its convex envelope over
the prescribed flow interval. For a pipe (i j∈P), we write
∆Πi j =Π i −Π j. On the interval 0≤f i j ≤ fi j, the fixed-
direction Weymouth relation is the graph of the convex
function∆Π i j =ω i j f 2i j. The straight line joining its endpoints
(0,0)and( f i j,ω i j f 2i j)is∆Π i j =ω i j fi j fi j. Sincef 2i j ≤ fi j fi j
for 0≤f i j ≤ fi j, the quadratic Weymouth curve lies below
this chord. We replace the equality by
ωi j f 2i j ≤Π i −Π j ≤ω i j fi j fi j,(20)
while retaining the flow bounds in (17).
Together, these inequalities describe the convex hull of the
isolated forward-flow graph, shown as the shaded region in
Fig. 1(b). The marked interior point illustrates that satisfying
the relaxation does not imply satisfying the Weymouth
equality. The quadratic inequality in (20) admits the rotated
second-order-cone representation

Πi −Π j, 12 , √ωi j fi j

∈Q 3r ,(21)
Fig. 1. Single-pipe Weymouth relation and its fixed-direction relaxation. (a)
Exact bidirectional equality. (b) Convex envelope of the selected nonnegative
branch; the marked interior point violates the Weymouth equality. Here
∆Πi j =Π i −Π j, and the plots useω i j = f i j =1.
where
Q3r = (r,s,t)∈R 3 :r,s≥0,2rs≥t 2	 .
Substitution into the cone inequality givesΠ i −Π j ≥ω i j f 2i j.
The upper inequality in (20) is affine. Combining the
pipe envelopes (20) with the affine compressor constraints
(16), nodal balances, operating bounds, and prescribed slack
pressure gives a convex feasible set of each fixed market
allocation. For the relaxed model, letx= (g,d)denote the
upper-level market allocation andy= (f,Π)the lower-level
decision variables. The allocationxis fixed when solving the
lower-level problem. Define the equality mapping by
H(x,y):=

A f−B gg+B dd
Πs −K

.(22)
Thus,H(x,y) =0 imposes all nodal flow balances and the
prescribed squared pressure at slack nodes. Similarly, for
the mapping
G(y):=



ωi j f 2i j −Π i +Π ji j∈P
Πi −Π j −ω i j f i j fi j

i j∈P
−f i j

i j∈E
fi j − f i j

i j∈E
Πi −Π i

i∈N
Πi − Πi

i∈N
Πi −Π j

i j∈C
Π j −α maxΠii j∈C

 ,(23)
imposes all inequality constraints, where each indexed block
denotes a column vector. The conditionG(y)≤0 imposes
the pipe-envelopes, non-negative arc-flow bounds, pressure
bounds, and affine compressor constraints. Then for fixedx,
H(x,·)is affine and each component ofGis convex. With
Q(y):= ˜Φl(y)from Eq. (15), the relaxed follower response
set is
Srel(x):=argmin
y
Q(y)(24)
s.t.H(x,y) =0,
G(y)≤0.

Replacing the exact follower response set in Eq. (14) by
Srel(x)gives
min
x,y
Fθ (x,y)(25)
s.t.x∈X,
y∈S rel(x).
To obtain a single-level optimization problem, we re-
place the response constrainty∈S rel(x)by explicit condi-
tions characterizing the follower optimality. The next sec-
tion introduces four representations: the KKT-based MPCC,
Wolfe-duality reformulation (WDP), Mond-Weir reformula-
tion (MDP), extended Mond-Weir reformulation (eMDP),
and Lagrange-dual reformulation (LDR).
IV. SINGLE-LEVELREFORMULATIONS
Letmdenote the number of inequalities inG(y). Asso-
ciate multipliersu∈R m≥0 withG(y)≤0 and unrestricted
multipliersv∈R |N|+1 withH(x,y) =0. Then, the follower
Lagrangian, dual function, and dual value are
L(x,y,u,v):=Q(y) +u TG(y) +vTH(x,y),(26)
d(x,u,v):=inf
z
L(x,z,u,v),d ∗(x):=sup
u≥0,v
d(x,u,v),
where the infimum runs overz∈R |A|+|N| and may equal−∞.
Letϕ(x)denote the optimal value of the relaxed follower
problem in Eq. (24). Derivatives with respect to the network
variables treat the market allocationxas fixed.
The equivalence statements below are conditional on the
following assumption: for everyx∈Xwith a nonempty
relaxed follower feasible set, its Lagrangian dual attains the
follower’s optimal value. This assumption ensures the exis-
tence of KKT multipliers at follower minimizers. Convexity,
in turn, makes the KKT conditions sufficient for global
follower optimality [27].
Each formulation minimizesF θ (x,y)over the physical
variables and its certificate variables, subject to
x∈X,H(x,y) =0,G(y)≤0,(27)
and the additional conditions specified below.
All three dual-based formulations introduce an auxiliary
pointz= (f z,Π z)∈R |A|+|N| and require
∇zL(x,z,u,v) =0.(28)
The pointzis used to certify follower optimality; it is
not required to satisfyG(z)≤0 orH(x,z) =0. The same
market allocationxappears in the physical constraints and
the certificate conditions [28].
•KKT-based reformulation (MPCC):The MPCC supple-
ments the common constraints (27) with follower station-
arity, dual feasibility, and complementarity:
∇yL(x,y,u,v) =0,(29)
uℓGℓ(y) =0, ℓ=1, . . . ,m.
Together withu≥0 andG(y)≤0, the second condition
imposes the complementarity pairs 0≤u ℓ ⊥ −Gℓ(y)≥0.
Complementarity requires a strictly slack inequality to
have zero multiplier; an active inequality may have a
nonzero multiplier.
•Wolfe-duality reformulation (WDP):WDP introduces
the auxiliary network variableszand the multipliers(u,v).
It combines the stationarity condition (28) with the Wolfe-
gap inequality
Q(y)−Q(z)−u TG(z)−v TH(x,z)≤0.(30)
Stationarity and convexity makeL(x,y,u,v)a lower bound
on the follower’s optimal value. The gap inequality re-
quires the feasible responseyto attain that bound.
•Mond-Weir reformulation (MDP):MDP retains Eq. (28)
and replaces the combined Wolfe-gap inequality by
Q(y)−Q(z)≤0,(31)
uTG(z) +vTH(x,z)≥0.
That is, these conditions separate the follower-objective
comparison from an aggregate condition on the multiplier-
weighted constraints.
•Extended Mond–Weir reformulation (eMDP):eMDP
also retains Eq. (28) and imposes
Q(y)−Q(z)≤0,(32)
uℓGℓ(z)≥0, ℓ=1, . . . ,m,
viHi(x,z) =0,i∈N.
Notice that, the aggregate MDP condition is replaced by
componentwise conditions. Unlike MPCC complementar-
ity, the inequality products are required to be nonnegative
rather than zero.
•Lagrange-dual reformulation (LDR): The LDR formu-
lation uses the dual function in Eq. (26) by considering
common constraints (27) and the following single inequal-
ity foru≥0,
Q(y)≤d(x,u,v).(33)
Becausedis an infimum, Eq. (33) is the infinite family
Q(y)≤L(x,z,u,v)for allz∈R |A|+|N|, so LDR is a semi-
infinite program with a noncompact index set. Such prob-
lems are computationally expensive in general, because
evaluatingd(x,u,v)for a nonconvex lower level is itself
a global optimization problem [29], [30], [31]. In our
convex setting, the inner infimum is attained exactly at the
stationary points ofL(x,·,u,v), which is what the finite
formulations above exploit.
Assuming that every relaxed follower minimizer admits
KKT multipliers, then all five formulations have the same
feasible projection onto(x,y)asy∈S rel(x). For any follower
minimizer, its KKT multipliers satisfy the MPCC conditions,
and settingz=yalso satisfies each dual-based formulation.
Sinceyis then a stationary point of the convex Lagrangian
L(x,·,u,v)and complementarity givesL(x,y,u,v) =Q(y), the
same multipliers yieldd(x,u,v) =Q(y)and hence satisfy
the LDR inequality (33) as well. Nevertheless, the resulting
five single-level formulations remain nonconvex, so a local

numerical solution does not establish global optimality of the
leader objective.
The literature shows that MPCC, WDP, MDP, eMDP,
and LDR characterize the feasible set of Eq. (25) when
strong duality holds with dual attainment for everyx[21],
[22], [23], [28]. In this section, we make two extensions:
First, without assuming strong duality or dual attainment,
we show that all five formulations project onto the same set
of the certifiable part of the follower response graph. Thus,
none can generate a spurious follower response, and the
assumption is needed only to guarantee that every follower-
optimal response can be represented in the corresponding
reformulation. Second, when the objective comparison in a
dual-based formulation is enforced only within a toleranceε,
as in numerical computations, we show thatεsimultaneously
bounds the follower suboptimality ofy, the duality gap atx,
and the multiplier suboptimality. We also characterize the
smallest tolerance for which a given response can be lifted.
Forε≥0, theε-relaxed WDP, MDP, and eMDP replace
the objective comparison in Eqs. (30), (31), and (32) by
Q(y)−L(x,z,u,v)≤εandQ(y)−Q(z)≤ε, respectively. The
ε-relaxed LDR replaces Eq. (33) byQ(y)≤d(x,u,v) +ε. All
other conditions remain unchanged.
Theorem 1:LetQandGbe convex and continuously
differentiable andHaffine inyand defineX D :={x∈X:
d(x,u,v) =ϕ(x)for someu≥0,v}.
(i) The feasible sets of MPCC, WDP, MDP, eMDP, and
LDR have the same projection onto(x,y), namely
{(x,y):x∈X D,y∈S rel(x)}.(34)
In particular, every feasible point of any of the five
formulations is feasible for (25), and the projection
equals the feasible set of (25) if and only ifX D =X.
(ii) Every feasible point of anε-relaxed WDP, MDP,
eMDP, or LDR satisfies
Q(y)−ϕ(x)| {z }
follower subopt.
+ϕ(x)−d ∗(x)| {z }
duality gap
+d ∗(x)−d(x,u,v)| {z }
multiplier subopt.
≤ε,
(35)
and each of the three terms is nonnegative.
(iii) Letx∈X,y∈S rel(x), andτ(x):=ϕ(x)−d ∗(x). Then
(x,y)lifts to a feasible point of theε-relaxed LDR
for everyε>τ(x)and for noε<τ(x); atε=τ(x)a
lift exists if and only if the supremum definingd ∗(x)
is attained. The same holds for theε-relaxed WDP
whenever the infimum definingd(x,u,v)is attained at
the lifting multipliers, for instance whenQis strongly
convex. Ifx∈X D, then(x,y)lifts to every relaxed
formulation for everyε≥0.
Proof:(i) Let a point be feasible for one of the five
formulations. Feasibility ofyand weak duality giveQ(y)≥
ϕ(x)≥d ∗(x)≥d(x,u,v). Next, we showQ(y)≤d(x,u,v).
For LDR this is trivial from Eq. (33). For WDP, MDP, and
eMDP, stationarity (28) and convexity ofL(x,·,u,v)give
d(x,u,v) =L(x,z,u,v), and Eq. (30) then impliesQ(y)≤
d(x,u,v); the MDP conditions sum to Eq. (30), and the
eMDP conditions sum to the MDP conditions. For MPCC,
complementarity andH(x,y) =0 giveL(x,y,u,v) =Q(y),
and stationarity atygivesd(x,u,v) =L(x,y,u,v). Hence, the
claim holds and we obtainy∈S rel(x)andx∈X D. Conversely,
letx∈X D,y∈S rel(x), and(u,v)withd(x,u,v) =ϕ(x) =
Q(y). Then
d(x,u,v)≤L(x,y,u,v) =Q(y) +u TG(y)≤Q(y) =d(x,u,v),
sou TG(y) =0, which givesu ℓGℓ(y) =0 for everyℓbecause
each product is nonpositive, andyminimizesL(x,·,u,v),
which gives∇ yL(x,y,u,v) =0. Thus(x,y,u,v)is MPCC
feasible, andz=ymakes it feasible for WDP, MDP, eMDP,
and LDR. The last claim follows becauseS rel(x)is nonempty
for everyx∈X.
(ii) The argument of (i) applied to the relaxed conditions
givesQ(y)−d(x,u,v)≤ε. The three terms in Eq. (35) are
nonnegative by feasibility ofyand weak duality, and they
telescope toQ(y)−d(x,u,v).
(iii) BecauseQ(y) =ϕ(x), a lift to the relaxed LDR exists
if and only ifd(x,u,v)≥ϕ(x)−ε=d ∗(x) +τ(x)−εfor
some(u,v). Ifε>τ(x), the definition of the supremum
provides such(u,v). Ifε<τ(x), no(u,v)qualifies because
d(x,u,v)≤d ∗(x). Ifε=τ(x), the requirement isd(x,u,v) =
d∗(x). For WDP, letzattain the infimum definingd(x,u,v)at
the lifting multipliers. Thenzsatisfies Eq. (28) by convexity,
andQ(y)−L(x,z,u,v) =Q(y)−d(x,u,v)≤εis the relaxed
WDP inequality. Strong convexity ofQmakesL(x,·,u,v)
strongly convex, so its infimum is attained. Finally, ifx∈X D,
the exact lift constructed in (i) is feasible for every relaxed
formulation at everyε≥0.
Theorem 1 has two consequences from the computational
perspective. First, any local solution of the finite formulations
yields a follower-optimal response even at market allocations
where strong duality is not known to hold; therefore, no
follower constraint qualification must be verified in advance.
Second, for a computed WDP, MDP, or eMDP solution
whose stationarity condition (28) holds to solver precision,
the objective-comparison residualεprovides, by Eq. (35), a
certified upper bound on the follower suboptimalityQ(y)−
ϕ(x)without additional assumptions. However, MPCC pro-
vides no analogous bound because a complementarity resid-
ual does not controlQ(y)−ϕ(x)without additional error-
bound constants.
V. NUMERICALEXPERIMENTS
We compare MPCC, WDP, MDP, and eMDP on the six-
node network in Fig. 2, using both exact bidirectional pipe
physics and the fixed-direction convex relaxation. Consumer
data are given in Table I, with total requested demand
∑i∈D di =130 kg/s. Production is bounded by 1000 kg/s.
Nodal pressures lie between 3 and 6 MPa, with the slack
pressure prescribed asp 1 =4 MPa. Pressures are normalized
by 3 MPa before squaring, giving the numerical slack value
Π1 =16/9. Both experiments maximize−Φ u in Eq. (1), with
θ=0.05,c T =1, and a signed pipe flow tariff. For these
experiments, we use the convex surrogate compressor-work

Consumer Node di bi
1 2 30 3.0
2 3 40 4.0
3 4 20 5.0
4 3 30 2.5
5 4 10 3.0
TABLE I
CONSUMER DATA: di IS IN KG/S ANDV i(di) =bidi.
C1 P1 P2
C2
P3
P4
Producer
Slack node
Consumer 1 Consumers 2, 4
Consumers 3, 5
1 5 2 3
6 4
Pipe
Compressor
Fig. 2. Six-node network. Blue arrows indicate pipe reference orientations;
orange connections denote directed compressors. Pipe flows may reverse in
the exact model but not in the relaxation.
objective in (15) and (24) withβ c =1, that is
Q(y) = ∑
(i,j)∈C
(Π j −Π i).(36)
The same surrogate is used in both models, preserving
convexity of the relaxed follower.
A. Solvers and reference construction
The experiments use Python 3.12.14, Ipopt 3.14.19, and
Gurobi 12.0.2. Ipopt uses exact Hessians, stopping and
constraint-violation tolerances of 10−8, and a budget of 5600
iterations and 120 seconds per configuration. MPCC shares
this budget across Scholtes parameters 10 −2,10 −3, . . . ,10−8.
Gurobi uses feasibility and optimality tolerance of 10 −9,
exact model and relative gap tolerances of 10 −6. Refer-
ence verification also uses physical feasibility and follower
gap thresholds of 10 −6 and an upper gap threshold of
10−6 max{1,|Φ u|}. All Ipopt configurations use a common
prescribed physical starting point at zero, while MPCC
imposes 0≤u ℓ[−Gℓ(y)]≤tat each Scholtes stage, retain-
ing primal and dual feasibility. For Gurobi’s exact-network
model, the signed Weymouth equation is represented by
ri j ≥0,r 2i j =f 2i j,Π i −Π j =ω i j fi jri j,i j∈P.Thus,
ri j =|f i j|without restricting the sign off i j. The exact dual-
based models are experimental since the convex-follower
equivalence argument for the dual-based reformulations is
not assumed to hold for the exact follower [28]. Gurobi
provides a physical-network reference and a numerical lower
bound for each model. A separate follower solve fixes the
reference market allocation and checks its original network
response.
Method ∆Φu ∆Q ∆D
Convex-relaxed follower
MPCC 0% 0% 0%
WDP 0% 0% 0%
MDP 0% 0% 0%
eMDP∗ 58.1% 100.0% 70.1%
Exact nonconvex follower
MPCC 0% 0% 0%
WDP 0% 0% 0%
MDP 1.3% 52.4% 3.4%
eMDP∗ 37.3% 43.1% 36.2%
TABLE II
PERCENTAGE DIFFERENCES FROM THE BEST-KNOWNGUROBI SOLUTION. FOR
BOTH MODELS,THESE SOLUTIONS HAVE−Φ ∗u =241.952938,Q ∗ =4.669637,AND
TOTAL SERVED DEMAND OFD ∗ =123.682193KG/S OUT OF130KG/S REQUESTED.
AN ASTERISK MARKS AN UNRESOLVED SOLVER RUN IN THE MENTIONED BUDGET.
B. Results
We report relative differences in both objectives and total
served demand relative to the corresponding best-known
Gurobi reference. Network feasibility and follower stationar-
ity are measured through the mass-balance(R B), Weymouth
(RW ), and projected follower stationarity residualsR S =
∥y−Π Yop (y−s y)∥2 for the exact and relaxed models, where
ΠYop denotes Euclidean projection onto the flow and pressure
bounds, compressor limits, and prescribed slack-pressure
constraint, ands y contains the follower-objective gradient
and the multiplier contributions from the balance and pipe
constraints. Table II reports percentage changes in the upper
and lower objectives (∆ Φu,∆ Q) and the percentage shortfall
in total served demand (∆ D), using the following formulas
∆Φu =100 Φu −Φ ∗u|Φ∗u| ,
∆Q=100 Q−Q ∗
|Q∗| ,∆D=100 D∗ −DD∗ ,
where starred quantities are evaluated at the best-known
solution obtained using Gurobi. Table III reports∆R k =
max{0,R k −τ k},k∈ {B,W,S}.
Method ∆RB ∆RW ∆RS
Convex-relaxed follower
MPCC <10 −6 <10 −6 <10 −6
WDP <10 −6 <10 −6 <10 −6
MDP <10 −6 <10 −6 <10 −6
eMDP∗ <10 −6 0.279 <10 −6
Exact nonconvex follower
MPCC <10 −6 <10 −6 <10 −6
WDP <10 −6 <10 −6 2.16
MDP <10 −6 <10 −6 <10 −6
eMDP∗ <10 −6 <10 −6 1.22
TABLE III
RESIDUAL EXCESSES ABOVEτ B =τ W =τ S =10 −6 IN THE RESPECTIVE
RESIDUAL UNITS.∆R B IS IN KG/S;∆R W USES SQUARED PER-UNIT
PRESSURE. "−"INDICATES A RESIDUAL VALUE LESS THAN THE
REPORTED TOLERANCE.

Tables II and III show that relaxed MPCC, WDP, and
MDP match the Gurobi reference objective and service to
the reported tolerance with small residuals. For both the
convex-relaxed follower and the exact nonconvex follower,
the best Gurobi solutions have−Φ ∗u =241.952938,Q ∗ =
4.669637, and total served demand ofD ∗ =123.682193 kg/s
out of 130 kg/s requested. Table II shows the percentage
differences with respect to the best-known Gurobi solution
using four reformulations. Table III shows residual excesses
aboveτ B =τ W =τ S =10 −6 in the respective residual units.
For exact physics, MPCC also reproduced the reference
values with samll residuals, while WDP matches its objective
and service, but has a larger projected stationarity residual.
Moreover, MDP returns small residuals at an allocation with
lower service and a less favorable upper objective for exact
model. The relaxed eMDP run returns a point with a large
first-order optimality residual for the complete single-level
problem, whereas the exact run reaches the iteration limit.
VI. CONCLUSIONS
We developed a bilevel gas-market model coupling market
equilibrium model with network operation using a leader-
follower reformulation approach. For the convexified fol-
lower, we characterized the common certifiable response
set of five single-level formulations and bounded follower
suboptimality through dual-certificate tolerances. On the six-
node instance, relaxed MPCC, WDP, and MDP, and ex-
act MPCC, matched the best-known Gurobi objectives and
service with residuals below 10 −6. Exact WDP matched
these values but exceeded the stationarity threshold. These
numerical observations do not extend the convex follower
guarantees to the exact nonconvex model. Extending the
theoretical analysis to this setting is left for future work.
REFERENCES
[1] S. E. Jenkins. Interdependency of electricity and natural gas markets
in the united states: a dynamic computational model. Master’s thesis,
Massachusetts Institute of Technology, 2014.
[2] Chuan He, Xiaping Zhang, Tianqi Liu, Lei Wu, and Mohammad
Shahidehpour. Coordination of interdependent electricity grid and
natural gas network—a review.Current Sustainable/Renewable Energy
Reports, 5(1):23–36, 2018.
[3] Anatoly Zlotnik, Line Roald, et al. Coordinated scheduling for
interdependent electric power and natural gas infrastructures.IEEE
Trans. on Power Sys., 32(1):600–610, 2016.
[4] Anna Schwele, Christos Ordoudis, et al. Coordination of power
and natural gas markets via financial instruments.Computational
Management Science, 18(4):505–538, 2021.
[5] Hermann W. Dommel and William F. Tinney. Optimal power flow
solutions.IEEE Transactions on power apparatus and systems, pages
1866–1876, 1968.
[6] Michael C. Caramanis, Roger E. Bohn, and Fred C. Schweppe.
Optimal spot pricing: Practice and theory.IEEE Transactions on Power
Apparatus and Systems, pages 3234–3245, 1982.
[7] Kristina Mohlin. The US gas pipeline transportation market: An
introductory guide with research questions for the energy transition.
Environmental Defense Fund EDP, pages 21–01, 2021.
[8] Daan Hulshof et al. Market fundamentals, competition and natural-gas
prices.Energy policy, 94:480–491, 2016.
[9] Office of Economic Policy. Gas transportation rate design and the
use of auctions to allocate capacity. Technical report, Federal Energy
Regulatory Commission, 1987.
[10] E. G. Read, B. J. Ring, S. R. Starkey, and W. Pepper. An lp based
market design for natural gas. InHandbook of networks in power
systems II, pages 77–113. Springer, 2012.
[11] A. Rudkevich and A. Zlotnik. Locational marginal pricing of natural
gas subject to engineering constraints. InProc. of the 50th Hawaii
International Conference on System Sciences, pages 3092–3101, 2017.
[12] Fei Wu, Harsha Nagarajan, Anatoly Zlotnik, Ramteen Sioshansi, and
Aleksandr M. Rudkevich. Adaptive convex relaxations for gas pipeline
network optimization. In2017 American Control Conference (ACC),
pages 4710–4716. IEEE, 2017.
[13] Luke S. Baker, Kaarthik Sundar, et al. Bling: Bounded linearized
iteration for natural gas–large-scale optimization, market simulation,
and uncertainty quantification. InPSIG Annual Meeting, pages PSIG–
2622. PSIG, 2026.
[14] Anatoly Zlotnik, Kaarthik Sundar, Aleksandr M. Rudkevich, Alek-
sandr Beylin, and Xindi Li. Optimal control for scheduling and pricing
intra-day natural gas transport on pipeline networks. In2019 IEEE
58th Conference on Decision and Control (CDC), pages 4877–4884.
IEEE, 2019.
[15] Terrence W. K. Mak, Pascal Van Hentenryck, Anatoly Zlotnik, and
Russell Bent. Dynamic compressor optimization in natural gas pipeline
systems.INFORMS Journal on Computing, 31(1):40–65, 2019.
[16] Fränk Plein, Johannes Thürauf, Martine Labbé, and Martin Schmidt.
A bilevel optimization approach to decide the feasibility of bookings
in the European gas market.Mathematical Methods of Operations
Research, 94(3):401–437, 2021.
[17] Veronika Grimm, Julia Grübel, Alexandra Schwartz, Ann-Kathrin
Wiertz, Martin Schmidt, and Gregor Zöttl. On a tractable single-level
reformulation of a multilevel model of the European entry-exit gas
market with market power.Journal of Global Optimization, 91(4):953–
985, 2025.
[18] Lars Schewe, Martin Schmidt, and Johannes Thürauf. Global opti-
mization for the multilevel European gas market system with nonlinear
flow models on trees.Journal of Global Optimization, 82(3):627–653,
2022.
[19] Holger Heitsch, René Henrion, Thomas Kleinert, and Martin Schmidt.
On convex lower-level black-box constraints in bilevel optimization
with an application to gas market models with chance constraints.
Journal of Global Optimization, 87(1):171–203, 2023.
[20] Stephan Dempe. Bilevel optimization: theory, algorithms, applications
and a bibliography. InBilevel optimization: advances and next
challenges, pages 581–672. Springer, 2020.
[21] Yuwei Li, Gui-Hua Lin, Jin Zhang, and Xide Zhu. A novel ap-
proach for bilevel programs based on wolfe duality.arXiv preprint
arXiv:2302.06838, 2023.
[22] Yu-Wei Li, Gui-Hua Lin, and Xide Zhu. Solving bilevel programs
based on lower-level mond-weir duality.INFORMS Journal on
Computing, 36(5):1225–1241, 2024.
[23] Stephan Dempe and Patrick Mehlitz. Duality-based single-level refor-
mulations of bilevel optimization problems.Journal of Optimization
Theory and Applications, 205(2):26, 2025.
[24] Shriram Srinivasan and Kaarthik Sundar. The solution of potential-
driven, steady-state nonlinear network flow equations via graph parti-
tioning.IEEE Control Systems Letters, 2026.
[25] Kaarthik Sundar and Anatoly Zlotnik. State and parameter estimation
for natural gas pipeline networks using transient state data.IEEE
Transactions on Control Systems Technology, 27(5):2110–2124, 2018.
[26] Stephan Dempe and Joydeep Dutta. Is bilevel programming a special
case of a mathematical program with complementarity constraints?
Mathematical programming, 131(1):37–48, 2012.
[27] Lieven Vandenberghe and Stephen Boyd.Convex optimization, vol-
ume 1. Cambridge university press Cambridge, 2004.
[28] Yu-Wei Li, Gui-Hua Lin, and Xide Zhu. Theoretical and numerical
comparison of nine single-level reformulations for bilevel programs.
INFORMS Journal on Computing, 2026.
[29] Evren M. Turan, Johannes Jäschke, and Rohit Kannan. Bounding-
focused discretization methods for the global optimization of non-
convex semi-infinite programs.Computational Optimization and
Applications, 92(3):1035–1068, 2025.
[30] Sanjay Mehrotra and Dávid Papp. A cutting surface algorithm for
semi-infinite convex programming with an application to moment
robust optimization.SIAM Journal on Optimization, 24(4):1670–1697,
2014.
[31] Cody Melcher, Zeinab Alizadeh, Lindsey Hiett, Afrooz Jalilzadeh, and
Erfan Yazdandoost Hamedani. Semi-infinite nonconvex constrained
min-max optimization.Advances in Neural Information Processing
Systems, 38:114463–114487, 2026.
