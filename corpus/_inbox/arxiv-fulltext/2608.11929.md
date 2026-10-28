---
source_id: "arxiv"
title: "arXiv:2608.11929"
url: "https://arxiv.org/abs/2608.11929"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2608.11929. Abstract:  
Coordinated Dynamic Operation of Integrated 
Electrolyzer–Compressor Systems 
 
Amin Salehi, Student Member, IEEE, Janne Seppänen, Senior Member, IEEE, Mahdi Pourakbari-Kasmaei, Senior 
Member, IEEE 
 
 Abstract— The increasing interaction between power and 
hydrogen sectors highlights the  importance of  coordinated 
operation of electrolyzers and electric-driven compressor stations 
(EDCSs). T"
---

# arXiv:2608.11929

 
Coordinated Dynamic Operation of Integrated 
Electrolyzer–Compressor Systems 
 
Amin Salehi, Student Member, IEEE, Janne Seppänen, Senior Member, IEEE, Mahdi Pourakbari-Kasmaei, Senior 
Member, IEEE 
 
 Abstract— The increasing interaction between power and 
hydrogen sectors highlights the  importance of  coordinated 
operation of electrolyzers and electric-driven compressor stations 
(EDCSs). This becomes particularly of higher importance under  
transient disturbances. However, coordinated dynamic 
interactions of these coupled subsystems remain largely 
unexplored. This article addresses such gap by developing a 
dynamic model for an integrated electrolyzer -EDCS system and 
designing appropriate PID control  schemes to address  the 
potential disturbances  affecting either component . To this end, 
linearized models of the electrolyzer and EDCS are first derived to 
enable systematic controller design. Then,  two PID controllers, 
representing conservative and fast-tracking designs, are developed 
to coordinate the system response. The developed coordinated 
model is examined and verified under four different cases. The 
results demonstrate the effectiveness of the proposed model under 
disturbances from the compressor driver or the electrolyzer . 
Controlling the electrolyzer flow in response to EDCS 
disturbances coordinates system dynamics and mitigates 
undesirable transient fluctuations. Conversely, under electrolyzer 
disturbances, regulating the EDCS torque eliminates inconsistent 
responses in pressure, flow, and rotational speed, while preventing 
hazardous transient under shoots and overshoots. Overall, the  
proposed framework guarantees transient stability and 
operational reliability of the integrated electrolyzer-EDCS system. 
 
Index Terms — Power and hydrogen integration, e lectrolyzer, 
compressor station, dynamic modeling, transient stability. 
I. INTRODUCTION  
HE widespread adoption of renewable energy resources 
and power -to-hydrogen technologies has facilitated 
greater integration of power and hydrogen  (H2) 
networks [1], [2], [3]. In such integrated systems, electrolyzers 
and electric -driven compressor stations (EDCSs) serve as the 
key coupling components  between the two  sectors [4], [5] . 
Electrolyzers can convert surplus renewable electricity into H2, 
providing grid flexibility and supporting the decarbonization of 
heavy industry and transport ation sectors  [6], [7] . 
Subsequently, compressors are deployed to raise H2 pressure to 
required level of transmission pipelines, refueling stations, and 
storage facilities  [4], [8] . As the H 2 sector grows, the 
interdependence between the power and H2 sectors becomes 
stronger, necessitating coordinated dynamic operation of joint 
electrolyzers and EDCSs, a topic that remains unexplored in the 
existing literature. Such coordination becomes particularly 
crucial as the sys tem’s stability needs to be guaranteed under 
disturbances affecting either the electrolyzer or EDCS in the 
 
This work has been submitted to the IEEE for possible publication. Copyright 
may be transferred without notice, after which this version may no longer be 
accessible. 
integrated system. 
The dynamic behavior of electrolyzers under variable 
electrical conditions has been broadly studied in the literature. 
The authors in [9], [10], [11], [12], [13]  developed dynamic 
modeling frameworks for utility-scale electrolyzers and showed 
their capability to provide fast frequency response and ancillary 
services in renewable-rich power systems . Control -oriented 
modeling and control of electrolyzers have also been widely 
investigated, highlighting the importance of dynamic models 
for designing effective operational and supervisory control 
strategies [14], [15], [16], [17], [18]. Furthermore, experimental 
and simulation studies have analyzed the response of 
electrolyzers to renewable fluctuations and their integration into 
power systems  [19], [20] . Collectively, these studies confirm 
the ability of electrolyzers to respond  dynamically to grid-side 
events. Nevertheless, their interaction with downstream H2 
compression stations remains insufficiently explored. 
EDCSs are another key coupling point between the power 
and H2 networks. Their motors are supplied by the power grid, 
whereas their operating conditions depend on H2 flow and 
pressure dynamics. These components are connected to the 
electrolyzer plants to increase the pressure level of the produced 
H2. Hence, two types of disturbances could impact their 
dynamic operation [4]. Variations in EDCS driver torque can 
affect compressor rotational speed, mass flow rate, suction 
pressure, and discharge pressure  [4], [21] . Moreover, 
electrolyzer flow rate fluctuations caused by power grid 
disturbances can alter the EDCS suction flow, thereby affecting 
its operation  [4]. Several studies have therefore focused on 
designing appropriate control schemes for the EDCS  to 
stabilize its operation [22], [23], [24], [25], [26] . However, the 
coordinated dynamic operation of the electrolyzer and EDCS 
has not been thoroughly analyzed. In large -scale integrated 
power–hydrogen systems, such dynamic interaction prevents 
lags or mismatches in the production –consumption chain, 
where electrical and hydrogen components are strongly 
interdependent. 
Despite the aforementioned developments, existing studies 
mainly consider electrolyzer flexibility, compressor control, or 
power-hydrogen coordination as separate problems. In 
particular, the bidirectional dynamic coordination between the 
electrolyzer and EDCS operation during disturbances has not 
been sufficiently investigated. This issue becomes critical when 
a disturbance reduces the EDCS driver torque without a 
corresponding adjustment in electrolyzer H2 production, 
thereby creating a supply-compression mismatch that may lead 
T  

 
to undesirable pressure and flow transients  [27]. Similarly, if 
the electrolyzer output changes while the EDCS driver torque 
remains unchanged, the compressor may exhibit inconsistent 
speed, flow, and pressure responses. Therefore, a coordinated 
control mechanism is required to regulate the electrolyzer flow 
rate in response to disturbances in the EDCS and, conversely, 
to regulate the EDCS torque in response to electrolyzer 
disturbances. 
This paper develops a coordinated control framework for an 
integrated electrolyzer -EDCS system. The electrolyzer is 
represented by a n already existing  linear dynamic model 
relating stack voltage to H2 production flow, whereas the EDCS 
is modeled using nonlinear pressure, flow, and mechanical  
speed dynamics. The EDCS model is linearized to enable 
controller design. Based on the linearized models, PID 
controllers are designed using pole placement and polynomial 
matching. The proposed framework incorporates two 
complementary control actions: 1) regulation of electrolyzer 
flow rate following a disturbance in the EDCS driver, and 2) 
regulation of the EDCS driver torque after a disturbance in 
electrolyzer H2 production. Accordingly, the main 
contributions of this work are summarized as follows. 
1) Developing an integrated dynamic model of the coupled 
electrolyzer-EDCS system to capture the interactions 
between H2 production and compression processes . 
Thus, the model fills the gap by relating the H2 flow rate 
produced by the electrolyzer  to the  compressor flow, 
suction and discharge pressures, rotational speed, and 
driver torque. 
2) Developing a linearized dynamic model for the EDCS 
and introducing a linear dynamic model for the 
electrolyzer. The relative state space representations are 
then formulated to facilitate systematic controller design. 
3) Designing conservative and fast-tracking PID controllers 
for bidirectional coordination: a) the electrolyzer control 
unit regulates H2 flow rate  when the EDCS driver is 
imposed by a driver torque  disturbance. This control 
action coordinates H 2 production with the compression 
system and mitigates undesirable pressure and flow 
transients; and b) the EDCS control unit  adjusts driver 
torque in response to disturbances in the output flow of 
the electrolyzer. The proposed control strategy 
eliminates inconsistent responses in rotational speed, 
flow, and pressure of the EDCS. Consequently, it 
prevents the compressor from approachin g the choke 
region under the disturbances. 
II. CONTROL CONCEPT AND OBJECTIVE IN A COUPLED 
ELECTROLYZER-COMPRESSOR SYSTEM 
An integrated renewable -electrolyzer-EDCS system is 
depicted in Fig. 1 as an example for the H2 transmission case. 
Under normal operating conditions, the electrolyzer produces  
H2 at a specified pressure. Then, the EDCS is employed to raise 
the pressure of the produced  H2 for transmission along the 
pipeline. This is necessary to fulfill network requirements, such 
as maintaining specific pressure levels and meeting certain gas 
demands [8]. Aside from normal operating conditions, two 
commonly occurring contingencies in such a system are loss of 
motor torque in the EDCS and  H2 flow-rate fluctuations in the 
electrolyzer [4], [28]. 
Electrolyzer Plant
Membrane
Cathode
Anode
Oxygen
Hydrogen
  
Electric-Driven
Compressor
Station
Electric
Motor
Tm Tc
Gearbox
Inlet 
Tank 
(Ps)
Outlet 
Tank
 (Pd)
     Qs
Ac
Lc
 
    Inlet Valve
Battery Storage
System
     Qc
     Qd
 
    Outlet Valve
The Rest of 
Network
Renewable 
Energy Sources
Controller
 Output
Input
Input
Fig. 1. Schematic diagram of an integrated electrolyzer-EDCS system. 
A. Contingency on the Compressor 
The EDCS might experience a disturbance from t he power 
grid side, resulting in torque fluctuations in its electric motor. 
In this situation, the electrolyzer's output flow rate should be 
controlled to mitigate EDCS fluctuations. This means that the 
EDCS suction flow rate would be controlled in response to its 
motor torque fluctuations. This will prevent the compressor 
from damaging and possible downstream load variations. 
Control signals corresponding to this situation are drawn with 
dashed red lines in Fig. 1. After sensing torque variations , a 
control command needs to be sent to the electrolyzer  to adjust 
its output flow. The closed -loop block diagram of the control 
system in this case is shown in Fig. 2, with the plant being the 
electrolyzer. QE and QE-ref are the electrolyzer flow rate and its 
reference flow rate, respectively. 
+ Controller
-
QEQE-ref
Electrolyzer
Controlled Unit
Fig. 2. Closed-loop block diagram of the control system when the EDCS is 
experiencing power grid disturbances. 
B. Contingency on the Electrolyzer 
A power grid disturbance could also trigger flow 
fluctuations in the  produced H2 flow by the electrolyzer plant. 
In such circumstances, the motor torque of the EDCS should be 
regulated to manage H2 fluctuations entering the compressor. 
That is the motor torque of the EDCS should be controlled in 
response to  its suction flow fluctuations. This prevent s 
equipment damaging and possible downstream load variations. 
Control signals for this case  are shown with dashed blue lines 
in Fig. 1. After sensing voltage variations in the electrolyzer , a 
control command needs to be sent to the EDCS to regulate its 
driver torque . The closed -loop block diagram of the control 
system in this case is presented in Fig. 3, where the plant is the 
EDCS. QC and Q C-ref are the compressor’s flow rate and its 
reference flow rate, respectively. 
+ Controller
-
QCQC-ref
EDCS
Controlled Unit
Fig. 3. Closed-loop block diagram of the control system when the electrolyzer 
is experiencing power grid disturbances. 

 
III. CONTROLLER DESIGN FOR THE PROPOSED SYSTEM 
To enable systematic controller synthesis, we start with the 
dynamic models of the electrolyzer and EDCS. For nonlinear 
models, all the nonlinearities will be first linearized around a 
nominal operating point corresponding to steady -state 
operation. Then, the linear state -space representation s are 
obtained using Jacobian linearization. Finally, two PID 
controllers are designed based on the resulting linear models. 
A. Linear State -Space Representation of the Electrolyzer 
System and Its PID Controller Design 
A linear dynamic model can be presented for both alkaline 
and proton exchange membrane electrolyzers based on the 
study performed in [29]. This model is represented by a second-
order transfer function  (1), in which the electrolyzer stack 
current is calculated from the electrolyzer stack DC voltage . 
Then, the electrolyzer current drives the electrolysis process, 
leading to H2 production. As presented in (2), t he H2 flow rate 
is proportional to the current [30]. 
( )( )
E
E
E
()() ()IG V ssss s = ++=
                                              (1) 
E
E
()
( ) 2
f s pNNQs
I s F

=
                                                                 (2) 
where, VE(s) and IE(s) are the Laplace transforms of the voltage 
and current of the electrolyzer stack, respectively ; α and β (α , 
β > 0) represent the poles of the stack transfer function ; QE is 
the H 2 production rate in kg/s,  ξ is the coefficient convert ing 
mol/s to kg/s,  ηf demonstrates the faraday efficiency ; F is the 
Faraday’s constant; and, Ns and Np denote the number of stack 
cells in series and parallel, respectively. Combining (1) and (2), 
the relation between QE and VE is presented in (3). 
( )
E
E 2
E
()() ()G V ssQss s   = + + +=
                                      (3) 
where, ψ is the coefficient equal to 
2
f s pNN
F
  .  
Let the input be u = VE and the output be y = QE. Then, a 
standard controllable state-space realization for the electrolyzer 
system can be demonstrated as follows. 
( ) E
0 1 0
1
E
x x V
yQ
  = +− − +
=
   
   

 
(4) 
Based on the closed -loop block diagram in Fig. 2 , the 
tracking error is e(t) = QE-ref(t) - QE(t). Also, s tandard PID 
representation and the closed-loop characteristic are shown in 
(5) and (6), respectively. 
2
PID() d p iipd K s K s KKC s K K s ss += + + = +
                         (5) 
cl PID E( ) 1 ( ) ( ) 0s C s G s = + =
            (6) 
Then, the closed-loop characteristic polynomial can be obtained 
by substituting (3) and (5) in (6). This is shown in (7). 
32
cl( ) ( ) ( ) 0 d p is s K s K s K      = + + + + + + =
         (7) 
Equation (7) is the key to PID design by pole placement and 
polynomial matching. To this end, we pick a desired stable third-
order polynomial, then match coefficients.  Without loss of 
generality, the desired closed-loop poles can be chosen such as 
s1,2,3 = p1, p2, p3 (p1, p2, p3 < 0). Then, matching the desired 
polynomial with the  closed-loop characteristic polynomial 
(Δd(s) = Δcl(s)), will determine PID gains as shown in (8). 
1 2 3 1 2 1 3 2 3 1 2 3
32
32
( ) ( )
( ) ( )
d p is K s K s K
s p p p p p p p p ps p s pp
     + + + + + + =
+ + + + + + +
 (8) 
where, PID gains are derived as follows. 
1 2 1 3 2 3
1 2 3
1 2 3
()
( ) ( )
p
i
d
K
p
p
K
p p p p
pK
p
pp
pp





+ + −=
=
+ + − +=
 (9) 
Finally, based on the closed-loop performance objectives 
(e.g., fast reference tracking and conservative response), the 
desired poles are selected and PID gains are calculated 
accordingly. For the conservative design, the dominant poles are 
placed closer to the imaginary axis, resulting in a lower closed-
loop bandwidth and slower response. In contrast, the fast -
tracking design uses poles farther into the left -half plane, 
resulting in a higher bandwidth and faster nominal tracking . 
Both designs are investigated via simulations in Section V. 
B. Linear State-Space Representation of the EDCS and Its PID 
Controller Design 
The EDCS dynamics are described by the following 
nonlinear differential equations [4], [27]. 
2
()s s c
s
aP Q QV= −

                                                                  (10) 
2
()
d
d c d
aP Q QV= −

                                                                  (11) 
( ( , ) )cc c c c s d
c
A
Q Q P P
L
= −

                                                (12) 
21 ()c m c clT T kJ= −−

                                                        (13) 
where, Ps and Pd are the inlet and outlet pressures at the 
compressor’s suction and discharge sides, respectively. Qs, Qc, 
and Qd are the inlet flow, the compressor flow, and the outlet 
flow, respectively; a is the speed of sound, and Vs, Vd, Ac, and 
Lc are the inlet tank volumes,  outlet tank volumes,  the cross 
section of the piping, and the duct length after the compressor, 
respectively; Πc (ωc, Qc) is a fitted polynomial map, presenting 
the pressure ratio ( Pd/Ps); ωc is the rotational speed of the 
compressor, J is the inertia of the mechanical system, Tm is the 
driver torque, Tc is the compressor torque, and kl is the rotating 
losses coefficient . Inlet and outlet flow s, compressor torque , 
and the polynomial map  can be modeled with ( 14)-(17), 
respectively. 
3
s in in ssQ k u P P= −
                                                               (14) 
3
d out d outdQ k u P P= −
                                                            (15) 
c c c cT k Q =
                                                                          (16) 

 
33
00
( , )
ij cc
ji
c c c ij QQ  
==
= 
                                              (17) 
where, ks and kd are the inlet and outlet valve gains, uin and uout 
are the extent of the inlet and outlet valve openings, and Pin and 
Pout are the boundary condition associated with the inlet and 
outlet headers, respectively; kc is the friction constant and αij is 
a 16 -dimensional parameter vector determined by the 
polynomial approximation. It is worth mentioning that Tm is the 
input to the EDCS, and the H2 generated by the electrolyzer 
serves as the inlet flow to the EDCS (i.e., QE = Qs). 
Unlike the electrolyzer, the EDCS dynamics include many 
nonlinear terms . Thus, linearization around steady -state 
operating points is required to design a proper PID controller. 
Let’s consider the state and input vectors as x = [Ps, Pd, Qc, ωc]T 
and u = Tm, respectively. The equilibrium points are also defined 
as x0 = [Ps0, Pd0, Qc0, ωc0]T and u0 = Tm0. Compressor flow (Qc) 
is considered the system output. The system can be generally 
written as ẋ = f(x, u) and y = h(x, u). Then, linearizing around an 
operating point (x0, u0) gives (18) and (19). 
x A x B u  = +

                                                                    (18) 
y C x D u  = +
                                                                   (19) 
where,  
0 0 0 0
0 0 0 0
( , ) ( , )
( , ) ( , )
,
,
x u x u
x u x u
ffAB xu
hhCD xu
==
==
 (20) 
Let’s start with matrix A. If Ṗs is considered as f1, then: 
00
0
00
23
2
1
( , ) 11
1
( , ) 13
2
in
in
s
xu
s ss
xu
cs
a k uf aP V P P
f a aQV
− == −
 = − =
 (21) 
All other partials in the first row of A are zero. If Ṗd is considered 
as f2, then: 
00
0
00
23
2
2
( , ) 22
2
( , ) 23
2
out
d
d
xu
d d out
xu
cd
a k uf aP V P P
f a aQV
− == −
 ==
 (22) 
All other partials in the second row of A are zero. If Q̇ c is 
considered as f3, then: 
0 0 0 0
00
0 0 0 00
0 0 0 00
33
0
33
0
3
( , ) 31
3
( , ) 32
13
( , ) 33
1
13
( , ) 34
1
( , )cx u c c c
sc
c
xu
dc
x u s
c ij
x u s
c ij
cc
cc
ji
ij
ji
ij
fA QaPL
fA aPL
f P i Q aQ
f P j Q a



−
==
−
==
 =  =
 = − =
 ==
 ==


 (23) 
Finally, if 
c
  is considered as f4, then: 
0 0 0
0 0 0 0
14
( , ) 43
14
( , ) 44 ( 2 )
xu
c
xu
c
cc
c c c l
f J k aQ
f J k Q k a


−
−
 = − =
 = − + =
 (24) 
All other partials in the fourth row of A are zero. Eventually, the 
state matrix A for the EDCS is drawn as follows. 
 
11 13
22 23
31 32 33 34
43 44
00
00
00
A
aa
aa
a a a a
aa
=




                                                  (25) 
Moreover, the input derivative is shown in (26).  This gives 
matrix B. 
00
14
( , ) 41xu
m
f JbT − ==
                                                          (26) 
All other partials in the remaining row s of matrix B are zero. 
Hence, the input matrix ( B) and the out matrix ( C) of the 
linearized compressor model are as follows. Matrix D is zero. 
 41000
T
Bb=
                                                         (27) 
 0 0 1 0C =
                                                             (28) 
Finally, the standard controllable state-space realization for 
the EDCS can be indicated as follows. 
   
 
m
TT
s d c c s d c c
T
s d c c
P P Q A P P Q BT
y C P P Q


= +
=


 
 (29) 
Now, the linearized transfer function of the EDCS can be 
obtained by forming C(sI - A)-1B + D, as shown in (30).  
41 34 11 22
C 4 3 2
m 3 2 1 0
( )( )()() ()CQ b a s a s aG T s c s c s c s css s −−= + + + +=
                            (30) 
where ci coefficients are calculated based on the A matrix 
elements, shown in (31).  
3 11 22 33 44
2 11 22 11 33 11 44 22 33 22 44 33 44
13 31 23 32 34 43
1 11 23 32 11 34 43 22 13 31 22 34 43 44 13 31
44 23 32 11 22 33 11 22 44 11 33 44 22 33 44
0
()
()
()
(
) ( )
c a a a a
c a a a a a a a a a a a a
a a a a a a
c a a a a a a a a a a a a a a a
a a a a a a a a a a a a a a a
ca
= − + + +
= + + + + +
− + +
= + + + + +
− + + +
= 11 22 33 44 11 22 34 43 11 44 23 32 22 44 13 31a a a a a a a a a a a a a a a−−−
 (31) 
In the case that the EDCS is controlled, the tracking error is 
e(t) = QC-ref(t) – QC(t), as shown in Fig. 3 . The closed-loop 
characteristic equation for the compression system , including 
the PID controller and the EDCS, is given in (32). 
( ) 1 ( ) ( ) 0cl PID Cs C s G s = + =
                (32) 
Then, the closed-loop characteristic polynomial can be obtained 
by subsituiting (5) and (30) in (32), as shown in (33). Equation 
(33) is the key for PID design. In this case, we pick a desired 
stable fifth -order polynomial, then match coefficients. The 
desired closed-loop poles are generally chosen such as s1,2,3,4,5 = 
p1, p2, p3, p4, p5 (pi < 0), as indicated in (34). 

 
54
3 41 34
3
2 41 34 11 22
2
1 41 34 11 22 11 22
0 41 34 11 22 11 22
41 34 11 22
( ) ( )
( ( ( ) ))
( ( ( ) ))
( ( ( )))
()
cl d
dp
d p i
pi
i
s s c K b a s
c b a K a a K s
c b a K a a K a a K s
c b a K a a K a a s
K b a a a
 = + +
+ + − + +
+ + − + +
+ + − +
+
 (33) 
5 4 3 2
4 3 2 1 0()d s s d s d s d s d s d = + + + + +
                               (34) 
where, coefficients di are calculated as follows. 
5
4
3
2
1
0
1
1 5
5
5
1
5
1
1
j
ji
j
i
i
ij
i
i j k
i j k l
i
i
i
k
kl
dp
d p p
d p p p
d p p p p
dp

  
  
=

=



=
=
=
=
=





 (35) 
Then, matching the desired polynomial with the  closed-loop 
characteristic equation obtained in (33) will determine PID 
gains. This is shown in (36).  
4
41 34 11 22
43
41 34
3 2 41 34 11 22
41 34
()()
i
d
d
p
dK b a a a
dcK ba
d c K b a a aK ba
=
−=
− − +=
 (36) 
It is important to note that, checking degree-of-freedom when 
matching Δd(s) = Δ cl(s) is required in this case . We have five 
equations but only three unknowns ( Kp, Ki, Kd). In another 
words, PID gains can be obtained by using three of the 
equations, and then the remaining two equations should be  
checked as consistency constraints. In (36), Kd, Kp, and Ki are 
obtained based on s4, s3, and the constant term , respectively. 
Hence, consistency constraints associated with s2 and s1 terms 
must be checked , as presented in (3 7). This ensures the 
feasibility of the designed PID controller. 
2 1 41 34 11 22 11 22
1 0 41 34 11 22 11 22
()
()
()
()
d p i
pi
d c b a a a K a a K K
d c b a a a K a a K
= + − + +
= + − +
 (37) 
Finally, the desired poles are selected based on the closed-loop 
performance targets and PID gains are calculated accordingly. 
Fast tracking and conservative responses will be also 
investigated in this case in Section V. 
IV. INPUT DATA AND SIMULATION SETUP 
A. Input Data 
This section provides the input data including all parameters 
and initial conditions considered for the simulation studies. Table 
I presents the related data to the electrolyzer plant and EDCS. The 
nominal active power of the electrolyzer plant and the EDCS are 
5.2 GW and 97.4 MW, respectively. At these power levels, the 
electrolyzer produces a constant hydrogen flow of 32.5 kg/s, while 
the EDCS raises the outlet pressure to the desired setpoint. The 
EDCS driver power consumption (kW) is computed using (38), 
as described in [27].  
1
d
c c m s
cs
D ave 14.276 ( ) 1Z
QT P
EP
P


  
−
−
= −


                            (38) 
where, Zave is the average compressibility factor of H2. Ec, ηc, and 
ηm are parasitic efficiency, compressor efficiency, and 
mechanical efficiency of the compressor driver, respectively ; 
EDCS’s flow rate, inlet temperature, inlet pressure, and outlet 
pressure are shown by Qc, Ts, Ps, and Pd, respectively; and κ is 
the ratio of specific heats of H2. 
TABLE I 
NUMERICAL PARAMETERS AND INITIAL CONDITIONS USED FOR THE 
INVESTIGATED EDCS. 
  Parameters Values [unit] 
EDCS 
Compressor 
Specifications 
Vs 0.2 m3 
Vd 0.1 m3 
a 340 m/s 
Ac / Lc 1×10-4 m 
J 0.1 kgm2 
ks 0.3 
kd 0.5 
kc 0.002 
kl 0.002 
Zave 1.06 
Ec 0.99 
ηc 0.87 
ηm 0.95 
Ts 288.14 K 
κ 1.41 
Boundary 
Conditions 
Pin 30.5 bar-g 
Pout 115 bar-g 
Valve 
Positions 
uin 60 % 
uout 40 % 
Initial 
Values 
Ps0 28 bar-g 
Pd0 125.4 bar-g 
Qc0 32.65 kg/s 
ωc0 4984 rad/min 
Electrolyzer Electrolyzer Specifications 
VES 40 V 
α 123.8 
β 61.1 
ηf 1 
Ns 24 
Np 1.3×106 
Additionally, the compressor map is approximated by a third-
order polynomial in ωc and Qc, see (17). In this regard, Table II 
lists the corresponding αij coefficients to this map. 
TABLE II 
COEFFICIENTS OF THE EDCS MAP. 
 
0
c  
1
c  
2
c  
3
c  
0
cQ
 
3.9093 1.088×10-4 7.8014×10-9 1.6728×10-13 
1
cQ
 1.4021×10-2 2.7584×10-6 -1.3803×10-10 1.2765×10-14 
2
cQ
 -8.3373×10-4 -1.106×10-7 1.7853×10-11 -1.093×10-15 
3
cQ
 1.1547×10-6 1.8473×10-9 -4.1134×10-13 2.4067×10-17 
B. Simulation Setup 
The integrated electrolyzer-EDCS system is implemented in 
MATLAB. Four case studies are considered to analyze the 
dynamic behavior of the system considered . Cases 1 and 2 
represent scenarios where the EDCS and the electrolyzer face 
power grid disturbances, respectively, without any control link 

 
between them. Cases 3 and 4 correspond to the implementation 
of PID controllers for Cases 1 and 2, respectively. 
Case 1: System response to power grid disturbances on the 
EDCS without control. 
In Case 1, a power disturbance is applied to the EDCS 
driver. The resulting impact on the system dynamics is then 
evaluated to illustrate the system response in the absence of a 
feedback controller for mitigating driver power deviations. The 
imposed driver power deviation is depicted in Fig. 4. 
Fig. 4. Power grid disturbance on the EDCS driver – Case 1. 
Case 2 : System response to power grid disturbances on the 
electrolyzer without control. 
In Case 2, the electrolyzer faces power disturbance. This 
disturbance applied to the input voltage of the electrolyzer 
stack, resulting in deviations in the H2 production. Figure 5 
demonstrates the resulting variations in the electrolyzer outlet 
H2 flow rate.  Then, the impact on the system dynamics is 
analyzed to observe the system response in the absence of a 
proper control mechanism. 
 
Fig. 5. Electrolyzer flow deviations – Case 2. 
Case 3: Controller implementation for the electrolyzer when the 
EDCS is imposed by power grid disturbance. 
In Case 3, a power disturbance similar  to Case 1 is applied 
on the compressor station. But in this case , the designed   PID 
controller is installed to adjust the electrolyzer operating point 
based on the EDCS driver deviations. This control mechanism 
would guarantee the safe operation of the system and reduce the 
risk of equipment damage . It is worth mentioning that 
inadequate coor dination between the electrolyzer and the 
compressor under these  conditions could create hazardous 
fluctuations in compressor operation, which may compromise 
reliability [27]. 
Case 4: Controller implementation for the EDCS when the 
electrolyzer is imposed by power grid disturbance. 
In Case 4, a power disturbance similar to Case 2 is applied 
on the electrolyzer. However, a PID controller is installed to 
adjust the dynamic operation of the EDCS in response to these 
H2 production deviations. This control mechanism would also 
be intended to coordinate the operation of the electrolyzer and 
the compressor and to maintain the safe operation of the system. 
Notably, ramp -shaped disturbance is considered at the 
electrolyzer outlet, as it more closely reflects realistic gas 
network dynamics [4], [31] . The proposed control scheme, 
however, is not limited to this disturbance type and can be 
extended to other disturbance profiles. 
V. SIMULATION RESULTS 
This section presents and analyzes the simulation outcomes 
obtained in this study . First, the system response s in Cases 1 
and 2 are examined to highlight the need for appropriate control 
links between the electrolyzer and the EDCS . Then, the results 
in Cases 3 and 4 are discussed to demonstrate coordinated 
system operation achieved with the design of PID controllers. 
Figure 6 demonstrates the driver power of the EDCS during 
power grid disturbance. Prior to the driver contingency, the 
EDCS power consumption (PD) is 97.87 MW, which decreases 
to 86.7 MW during the torque loss. This consumption drop is 
observed with a significant fluctuation at the beginning and the 
end of the disturbance. This affects all system variables. 
Fig. 6. Driver power of the EDCS during motor torque disturbance – Case 1. 
Fig. 7. State variables of the EDCS during motor torque disturbance – Case 1.  
Dynamics of the EDCS’s suction pressure ( Ps), discharge 
pressure (Pd), flow rate ( Qc), and rotational speed ( ωc) during 
the disturbance are depicted in Fig. 7. ωc drastically drops, then 
it recovers to its steady -state value after the contingency.  In 
        
                    
          
  
  
  
  
  
  
  
        
                    
       
  
  
  
   
   
   
        
  
   
   
        
  
   
                    
          
  
  
  
  
  
                    
          
   
   
   


 
contrast, the gas variables behave differently. Qc and Pd initially 
decrease during the disturbance but quickly recover due to the 
constant input flow. As the driver torque recovers, a peak in Qc 
and Pd is observed (see 30 -31 sec in Fig. 7). However, Ps 
behaves differently, and rises to a new level during the 
disturbance, as explained in [27]. 
Figure 8 stands for the dynamics of the EDCS state 
variables under electrolyzer contingency. When QE, which is 
also the suction flow (Qs) of the EDCS, is dropped, Qc, Ps, and 
Pd show similar behaviors and decrease accordingly. On the 
other hand, ωc just increases slightly during the contingency as 
the motor torque ( Tm) has remained constant at its nominal 
value (5×10 4 N.m.). Also, under this condition, PD decreases 
from 97.87 MW to 81.5 MW, which is proportional to the 
reductions of Qc, Ps, and Pd based on (37).  PD of the EDCS is 
demonstrated in Fig. 9. 
Fig. 8. State variables of the EDCS during electrolyzer deviations – Case 2.  
Fig. 9. Driver power of the EDCS during electrolyzer deviations – Case 2. 
To facilitate a better understanding of the EDCS dynamics 
in Cases 1 and 2, the behaviors of the state variables in these 
cases are summarized as follows. The normal expected dynamic 
behavior of the compressor variables and QE during compressor 
torque drop is presented in (39) [4]. 
 ,  ,Em c c s dT Q Q P P       
                        (39) 
However, observed dynamics in Case 1 are presented in (40). 
const. const.  , , , ,   Em c c d sT Q Q P P   = = 
             (40) 
Also, the normal expected dynamics of the EDCS variables and 
Tm during electrolyzer flow deviations are presented in (41). 

  ,
m
E
c c s dQ P PQ T       
                           (41) 
However, observed dynamics in Case 2 are presented in (42). 
const.,, ,, mE c s d cQ P P TQ      
                          (42) 
Based on the conceptual compressor map, shown in Fig. 10, 
both dynamic trajectories in Cases 1 and 2 can be justified 
theoretically by using (10) -(13). In Fig. 10, t he normal path  
presents dynamics seen in (39) and (41), while paths marked for 
Cases 1 and 2 shows dynamics in ( 40) and (42), respectively. 
Also, the operation trajectory of the EDCS in  Case 1 (see Fig. 
6) and Case 2 (see Fig. 8 ) is depicted in Fig. 11. Besides 
abnormal operation in both cases,  the EDCS approaches the 
choke line during the disturbance that happened in Case 1. This 
exactly corresponds to the moments that the compressor 
variables experience fluctuations with a large magnitude at the 
beginning and end of the event. This behavior is undesirable 
from the safety perspective [32], [33].  
Fig. 10. Normal and abnormal dynamic operation of the EDCS under motor 
torque and electrolyzer contingencies. 
Fig. 11. Operation trajectory of the EDCS in Cases 1 and 2. 
Overall, dynamic behaviors observed in Cases 1 and 2 
indicate inconsistencies in system response.  In real -world 
operations in Case 1 , all state variables of the compressor 
station should change accordingly when a driver power loss 
occurs. For instance, the compressor flow should decrease, and 
this reduction implies that the electrolyzer should also decrease 
its H2 production. Also, when the electrolyzer flow (=Qs=Qc) is 
disturbed in Case 2 , the compressor driver should control its 
torque accordingly. This prevents any damage to the 
compressor’s internal equipment. For instance, when Qc 
decreases, the compressor should decrease its torque, resulting 
in reducing ωc with a proper control action.  However, these  
actions do not occur in Case s 1 and 2 due to the absence of a 
proper control link between the electrolyzer and the EDCS. 
                    
          
  
  
  
  
                    
          
   
   
   
   
   
        
                    
       
  
  
  
   
   
   


 
This highlights the need for addressing the existing gap in the 
literature and de veloping an integrated control strategy for the 
coupled electrolyzer–compressor system. 
In Case 3, we investigate the necessity of the electrolyzer to 
regulate its output flow in response to the disturbance applied 
to the EDCS. To this end, two PID controllers are designed for  
QE: one to provide a conservative response and the other to 
provide a fast -tracking response.  Table I II lists the PID 
coefficients used in  Case 3.  For the conservative design, the 
desired closed-looped poles are chosen as s1 = −1.5, s2 = −60 
and s3 =  −125, with the corresponding PID gains obtained from 
(8) and (9). Here, s1 is the dominant pole and behaves like a slow 
integrator, reducing bandwidth and improving robustness to 
modeling uncertainty and noise. The remaining poles, s2 and s3, 
are placed close to the open -loop poles α and β, meaning that 
the PID controller does not significantly alter their dynamics . 
Overall, the dominant pole is selected to satisfy the desired 
settling time, estimated as ts = 4/∣s1∣, while the other poles are 
placed sufficiently far from it to remain non -dominant and to 
avoid affecting the primary closed -loop response. For the fast 
design, the desired closed-looped poles are chosen as s1 = −50, 
s2 = −100 and s3 =  −200, with the PID gains obtained from (8) 
and (9). All three poles are selected well beyond the imaginary 
axis with a dominant pole at s = −50 and a much wider closed-
loop bandwidth.  
TABLE III 
PID COEFFICIENTS DESIGNED FOR THE ELECTROLYZER. 
Conservative Response Value Fast-tracking Response Value 
Kp 0.086 Kp 11.13 
Ki 4.56 Ki 405.58 
Kd 6 × 10-4 Kd 0.067 
After applying the designed controller to the system, t he 
controlled flow rate of the electrolyzer, QE, can be traced in Fig. 
12. The figure compares QE for the case without a control link 
between the electrolyzer and the EDCS (Case 1) and for the 
cases in which PID controllers are designed to provide 
conservative and fast responses . As shown,  the electrolyzer 
effectively reduces its output flow  in response to the 
disturbance affecting the EDCS driver . In addition , the 
hazardous undershoot and overshoot transients observed in 
Case 1 are eliminated by the PID implementation . It is worth 
mentioning that both controllers achieve satisfactory reference 
tracking under nominal conditions . The conservative design 
uses dominant poles closer to the imaginary axis, resulting in a 
lower closed -loop bandwidth and a slower response. In 
contrast, the fast-tracking design employs poles farther into the 
left-half plane, leading to a higher closed -loop bandwidth and 
faster nominal tracking. 
Accordingly, the inconsistencies in the EDCS dynamics are 
resolved when QE is properly controlled, as shown in Figs. 13 
and 14. All EDCS state variables exhibit the expected behavior 
under motor disturbance, consistent with (39). In addition, the 
hazardous fluctuations in the compressor driver power are 
eliminated, and the power  consumption during the disturbance 
is correctly reduced from 97.87 MW to 67 MW (compare Figs. 
7 and 14). This consumption level is the actual expected driver 
power of the EDCS during the disturbance. Furthermore, the  
Fig. 12. Electrolyzer flow rate with and without the PID – Case 3. 
operation trajectory of the EDCS after controlling QE is 
demonstrated in Fig. 1 5. In this case, the compressor operates 
normally and does not approach the choke line. 
Fig. 13. State variables of the EDCS after applying the PID – Case 3. 
Fig. 14. Driver power of the EDCS after applying the PID – Case 3. 
In Case 4, the EDCS is required to control its torque in 
response to the disturbance applied to the electrolyzer. Similar 
to Case 3, two PID controllers with conservative and fast -
tracking responses are designed for controlling Tm. The 
obtained PID gains for this case are listed in Table IV. The 
desired closed-loop poles were selected as s = [−1, −20, −50, 
−100, −200] for the conservative design. Using the pole 
placement in (36), the PID gains are computed as given in Table 
IV. However, enforcing the consistency constraints in (37) with 
        
                    
         
  
  
  
  
  
  
  
  
  
            
                   
                  
            
  
  
  
  
  
  
        
    
  
    
  
                    
          
  
  
  
  
            
                   
                  
                    
          
   
   
   
          
                   
                  
        
                    
       
  
  
  
  
   
   
   
          
                   
                  

 
Fig. 15. Operation trajectory of the EDCS after applying the PID – Case 3. 
the computed PID coefficients, the resulting actual closed-loop 
poles are located at s = [−0.77, −15.03, −64.38 ± 58.69j, 
−226.44], which still indicates a stable closed -loop response. 
For the fast -tracking design, the desired closed -looped poles 
were chosen as  s = [−8, −40, −100, −200, −380] . After 
computing the PID gains and applying the consistency 
constraints, the actual closed -loop poles are obtained as  s = 
[−12.61, −27.84, −101.92 ± 76.11j, −418.73], again confirming 
stable closed -loop operation. Unlike small laboratory -scale 
compressor systems, the present study considers a large 
industrial compressor station in the 100 MW range. Therefore, 
the large PID gains obtained for the EDCS are consistent with 
the scale of the system, where the driver torque input operates 
in the range of  104–105 N.m., and the compressor flow output 
is 32 kg/s.  Accordingly, the controller must map a relatively 
small flow-rate error into a large torque correction. This scaling 
is also consistent with prior studies, where gains on the order of 
104 have been  reported even for significantly smaller 
compressor systems [26]. 
TABLE IV 
PID COEFFICIENTS DESIGNED FOR THE EDCS. 
Conservative Response Value Fast-tracking Response Value 
Kp 4.9 × 104 Kp 2.6 × 105 
Ki 4.3 × 104 Ki 5.2 × 106 
Kd 155 Kd 677 
Figure 16 illustrates the driver torque of the EDCS . It 
compares Tm in the uncontrolled case  (Case 2) , in which no 
control link exists between the electrolyzer and the EDCS, with 
the cas e employing the conservative and fast -tracking PID 
controllers (Case 4) . In the absence of this control link, Tm 
remains unchanged despite the disturbance applied to  QE. By 
contrast, once the PID controller is implemented, the EDCS 
adjusts its driver torque appropriately in response to the 
electrolyzer flow disturbance. This response confirms the 
effectiveness of the proposed control scheme in establishing the 
required dynamic interaction between the electrolyzer and the 
EDCS. Moreover, both the conservative and fast -tracking 
designs provide satisfactory reference-tracking performance. 
By properly controlling Tm, the undesirable EDCS behavior 
identified in Case 2 is resolved, as indicated in Figs. 17 and 18. 
The state variables exhibit the expected dynamics under 
electrolyzer flow disturbance, following (41). The compressor 
driver power during the disturbance decreases from 97.87  MW 
to 74.5 MW (compare Figs. 9 and 18).  This reduced level 
corresponds to the expected driver power of the EDCS under 
this operating condition. The operating trajectory of the EDCS  
is shown in Fig. 19, confirming acceptable performance for the  
Fig. 16. Motor torque of the EDCS with and without the PID – Case 4. 
compressor. The operating point stays mainly within the 
zoomed area, undergoes a temporary deviation from the base 
operating zone, and then returns, all without approaching the 
choke line. 
Fig. 17. State variables of the EDCS after applying the PID – Case 4.  
Fig. 18. Driver power of the EDCS after applying the PID – Case 4. 
VI. CONCLUSION 
This work investigates coordinated control of an integrated 
electrolyzer and electric -driven compressor station (EDCS) 
system under disturbances occurring to either component. In 
this regard, an integrated dynamic model has been developed to 
replicate the dynamic interactions between the electrolyzer and 
EDCS. Subsequently, it utilizes an existing linear  electrolyzer 
model and develops a linearized model for the EDCS to design 
conservative and fast-tracking PID controllers. 
                    
          
  
  
  
  
          
                   
                  
                    
          
   
   
   
   
   
          
                   
                  
        
                    
       
  
  
  
  
  
  
  
   
   
   
          
                   
                  

 
 
Fig. 19. Operation trajectory of the EDCS after applying the PID – Case 4. 
Simulation results showed that a mismatch dynamic 
response will occur under the absence of a coordination link 
between the electrolyzer and the EDCS. In particular, when a 
disturbance happens to the EDCS driver while the electrolyzer 
flow remains unchanged, undesirable pressure and flow 
transients were observed in the system, and the EDCS 
approached the choke region. Conversely, an electrolyzer flow 
disturbance with an unregulated EDCS driver torque results in 
inconsistent EDCS dynamic responses. 
The proposed coordination strategy addressed these 
negative impacts in both disturbance scenarios. Regulating the 
electrolyzer hydrogen flow in response to the EDCS driver 
disturbance, eliminated the observed transient fluctuations, and 
maintained the compressor away from the choke line. Similarly, 
controlling the  EDCS driver torque in response to the flow 
disturbances of the electrolyzer, restored the expected dynamic 
responses in the pressure, flow, and mechanical speed of the 
EDCS. Also, b oth conservative and fast -tracking controllers 
revealed satisfactory tracking performance suitable for practical 
purposes. 
REFERENCES 
[1] W. Jia, T. Ding, and Y. He, “Synergistic integration of green hydrogen in 
renewable power systems: A comprehensive review of key technologies, 
research landscape, and future perspectives,” Renewable and Sustainable 
Energy Reviews, vol. 226, p. 116375, 2026. 
[2] J. Zhang et al. , “Optimal planning for electricity –gas–hydrogen integrated 
energy systems considering intertemporal long -term hydrogen storage and 
multiple uncertainties,” IEEE Transactions on Power Systems, 2025. 
[3] D. Haoxin et al. , “A comprehensive review on renewable power -to-green 
hydrogen-to-power systems: Green hydrogen production, transportation, 
storage, re-electrification and safety,” Applied Energy, vol. 390, p. 125821, 
2025. 
[4] A. Salehi and M. Pourakbari-Kasmaei, “Dynamics of the Electric-Driven Gas 
Compressor Station Under Electric and Gas Network Disturbances,” IEEE 
Transactions on Industrial Informatics, 2026. 
[5] A. Salehi and M. Pourakbari -Kasmaei, “Wind farm capacity assessment for 
hydrogen production: A case study in Finland,” presented at the 2024 IEEE 
PES ISGT EUROPE, 2024, pp. 1–5. 
[6] S. D. Tavakoli et al., “Grid-forming services from hydrogen electrolyzers,” 
IEEE transactions on sustainable energy, vol. 14, no. 4, pp. 2205–2219, 2023. 
[7] A. Buttler and H. Spliethoff, “Current status of water electrolysis for energy 
storage, grid balancing and sector coupling via power -to-gas and power -to-
liquids: A review,” Renewable and Sustainable Energy Reviews, vol. 82, pp. 
2440–2454, 2018. 
[8] Y. Zhao, X. Xu, M. Qadrdan, and J. Wu, “Optimal operation of compressor 
units in gas networks to provide flexibility to power systems,” Applied Energy, 
vol. 290, p. 116740, 2021. 
[9] M. G. Dozein, A. Jalali, and P. Mancarella, “Fast frequency response from 
utility-scale hydrogen electrolyzers,” IEEE Transactions on Sustainable 
Energy, vol. 12, no. 3, pp. 1707–1717, 2021. 
[10] N. Taranin, M. G. Dozein, O. Saborío-Romano, and N. A. Cutululis, “On the 
ramp-rate limitation of electrolysis plants: Modeling fundamentals and 
system-level impact analysis,” IEEE Transactions on Sustainable Energy , 
2025. 
[11] M. G. Dozein, A. M. De Corato, and P. Mancarella, “Virtual inertia response 
and frequency control ancillary services from hydrogen electrolyzers,” IEEE 
Transactions on Power Systems, vol. 38, no. 3, pp. 2447–2459, 2022. 
[12] A. Bernabeu-Santisteban, S. D. Tavakoli, H. del-Pozo-Gonzalez, L. Trilla, F. 
Díaz-González, and O. Gomis -Bellmunt, “Modeling megawatt -scale 
hydrogen electrolysis plants with frequency support capability,” Applied 
Energy, vol. 421, p. 128225, 2026. 
[13] V. M. Lopez, H. Ziar, J. Haverkort, M. Zeman, and O. Isabella, “Dynamic 
operation of water electrolyzers: A review for applications in photovoltaic 
systems integration,” Renewable and Sustainable Energy Reviews , vol. 182, 
p. 113407, 2023. 
[14] Y. Ye et al., “Dynamic modelling of PEM Electrolyzers for power system 
frequency control with power HIL validation,” Applied Energy, vol. 413, p. 
127504, 2026. 
[15] S. Khodakaramzadeh, T. Faghihi, Q. Shafiee, P. Bauer, and H. Vahedi, “A 
Survey of Control and Energy Management in Hydrogen Production 
Systems,” IEEE Open Journal of the Industrial Electronics Society, 2026. 
[16] T. Yuan, J. Tan, and Y. Teng, “A review of dynamic modeling and control of 
grid-connected hydrogen production units using water electrolysis,” 
Renewable and Sustainable Energy Reviews, vol. 226, p. 116296, 2026. 
[17] M. A. Hossain, M. R. Islam, M. A. Hossain, and M. Hossain, “Control strategy 
review for hydrogen -renewable energy power system,” Journal of Energy 
Storage, vol. 72, p. 108170, 2023. 
[18] A. Taghavi, T. Niknam, S. Shojaeiyan, and J. Rodriguez, “The future of 
hydrogen as a strategic enabler in integrated energy systems: Technological 
developments, barriers, and policy implications,” Energy Strategy Reviews , 
vol. 63, p. 101999, 2026. 
[19] Y. Zhang, N. Zhang, X. Ji, Z. Dong, X. Dong, and F. Wen, “Optimal power 
allocation strategy for hydrogen production system of ALK-PEM electrolyzer 
considering second -level response characteristics,” IEEE Transactions on 
Smart Grid, 2026. 
[20] P. Lin, G. Gao, J. Ma, M. Zhu, X. Zhang, and A. Abu-Siada, “Transient power 
allocation control scheme for hybrid hydrogen electrolyzer –supercapacitor 
system with autonomous inertia response,” IEEE Transactions on Industry 
Applications, 2026. 
[21] A. Cortinovis, M. Mercangöz, T. O. Stava, and E. Lunde, “Dynamic time to 
surge computation for electric driven gas compressors during voltage dips,” 
IFAC-PapersOnLine, vol. 49, no. 7, pp. 949–954, 2016. 
[22] G. Torrisi, S. Grammatico, A. Cortinovis, M. Mercangöz, M. Morari, and R. 
S. Smith, “Model predictive approaches for active surge control in centrifugal 
compressors,” IEEE Transactions on Control Systems Technology, vol. 25, no. 
6, pp. 1947–1960, 2017. 
[23] T. J. Besselmann et al. , “Increasing the robustness of large electric driven 
compressor systems during voltage dips,” IEEE Transactions on Industry 
Applications, vol. 54, no. 2, pp. 1460–1468, 2017. 
[24] A. Cortinovis, H. Ferreau, D. Lewandowski, and M. Mercangöz, 
“Experimental evaluation of MPC -based anti-surge and process control for 
electric driven centrifugal gas compressors,” Journal of process control, vol. 
34, pp. 13–25, 2015. 
[25] J. T. Gravdahl, O. Egeland, and S. O. Vatland, “Drive torque actuation in 
active surge control of centrifugal compressors,” Automatica, vol. 38, no. 11, 
pp. 1881–1893, 2002. 
[26] R. Nanmaran et al., “Compressor speed control design using PID controller in 
hydrogen compression and transfer system,” International Journal of 
Hydrogen Energy, vol. 48, no. 73, pp. 28445–28452, 2023. 
[27] A. Salehi, M. Tofighi -Milani, S. Fattaheian -Dehkordi, M. Lehtonen, J. 
Seppänen, and M. Pourakbari-Kasmaei, “Investigating the Impact of Electrical 
Disturbances on the Dynamics of Coupled Electrolyzer -Compressor 
Systems,” presented at the 2025 IEEE PES ISGT Europe, 2025, pp. 1–5. 
[28] A. Salehi and M. Pourakbari-Kasmaei, “Electronic Companion: Dynamics of 
The Electric-Driven Gas Compressor Station Under Electric and Gas Network 
Disturbances,” Feb. 2026, doi: https://doi.org/10.13140/RG.2.2.35371.30248. 
[29] M. G. Dozein, A. M. De Corato, and P. Mancarella, “Virtual inertia response 
and frequency control ancillary services from hydrogen electrolyzers,” IEEE 
Transactions on Power Systems, vol. 38, no. 3, pp. 2447–2459, 2022. 
[30] M. G. Dozein, A. Jalali, and P. Mancarella, “Fast frequency response from 
utility-scale hydrogen electrolyzers,” IEEE Transactions on Sustainable 
Energy, vol. 12, no. 3, pp. 1707–1717, 2021. 
[31] A. Salehi, J. Seppanen, and M. Pourakbari -Kasmaei, “Comparative Analysis 
of Linepack Impact in Hydrogen and Natural Gas Networks under Dynamic 
Operating Conditions,” arXiv preprint arXiv:2607.16527, 2026. 
[32] R. Kurz, E. Fowler, R. Marechale, M. Ji, and M. Cave, “Operation of 
centrifugal compressors in choke conditions,” 2013. 
[33] O. Leufvén and L. Eriksson, “A surge and choke capable compressor flow 
model—Validation and extrapolation capability,” Control Engineering 
Practice, vol. 21, no. 12, pp. 1871–1883, 2013. 
  

