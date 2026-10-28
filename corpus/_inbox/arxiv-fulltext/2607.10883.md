---
source_id: "arxiv"
title: "IEEE Vehicle Power and Propulsion Conference (VPPC) --- 5-9 October 2026, Lyon, France"
url: "https://arxiv.org/abs/2607.10883"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2607.10883. Abstract: IEEE Vehicle Power and Propulsion Conference (VPPC) --- 5-9 October 2026, Lyon, France
Model-Free Detection and Accommodation of Sensor Faults Fo r a PEM
Electrolyzer
Meziane Ait Ziane 1, Michel Zasadzinski 2, C´ edric Join2 and Michel Fliess 3
Abstract— We investigate the detection and accommodation
of sensor faults for a proton exchange membrane electrolyze r
coupled to a DC/DC converter powered"
---

# IEEE Vehicle Power and Propulsion Conference (VPPC) --- 5-9 October 2026, Lyon, France

IEEE Vehicle Power and Propulsion Conference (VPPC) --- 5-9 October 2026, Lyon, France
Model-Free Detection and Accommodation of Sensor Faults Fo r a PEM
Electrolyzer
Meziane Ait Ziane 1, Michel Zasadzinski 2, C´ edric Join2 and Michel Fliess 3
Abstract— We investigate the detection and accommodation
of sensor faults for a proton exchange membrane electrolyze r
coupled to a DC/DC converter powered by renewable energy
sources. The proposed method for detecting and accommodat-
ing the sensor fault is model-free and is based on the concept of
ultra-local model that is becoming classic in control engineering.
The existing literature on active control tolerant to senso r fault
dedicated to this question shows that no previous work has
addressed this topic. Our approach mitigates the effect of s ensor
fault on closed-loop behavior and guarantees the stability and
performance of the overall system. Numerical simulations u nder
variations in renewable energy sources validate our approa ch.
I. INTRODUCTION
Green hydrogen is playing an key part in reducing carbon
emissions in the industrial and transport sectors. This hyd ro-
gen is mainly produced using water electrolysers powered
by renewable energy sources. In this framework, Proton
Exchange Membrane Water Electrolyzers (PEMWE) tech-
nology is widely used for hydrogen production due to its
fast response to renewable energy sources variations and it s
ability to support high current densities of up to 2 A/cm 2 [1].
Due to its complexity, the PEMWE system is subject
to several types of faults: those occurring at the stack or
cell level, such as membrane drying, crossover, membrane
degradation, . . . , as well as those appearing at the system
level, including balance of plant (leaks in pumps, valves,
sensors, etc.). In recent years, many studies have been
devoted to the diagnosis of this system. A model-based
diagnosis approach via bond graph is proposed in [2]. The
detection and isolation of several stack faults as membrane
ﬂooding and drying, crossover, . . . are made by evaluating
residuals. A signal-based approach is proposed in [3] to
detect stack short circuits and water shortages and to detec t
pump fault in [4]. However, these methods consider the open
loop operation of the system.
A PEMWE operates at a voltage signiﬁcantly lower than
that provided by Renewable Energy Sources (RES), thereby
necessitating a DC/DC buck converter as an interface [5], [6 ].
An Active Fault-Tolerant Control (AFTC) strategy has been
*This work was not supported by any organization
1M. Ait Ziane is with Universit´ e de Lorraine, GREEN, F-54000 Nancy,
France. meziane.ait-ziane@univ-lorraine.fr
2M. Zasadzinski and C. Join are with Research Center
for Automatic Control of Nancy (CRAN), UMR CNRS
7039, Universit´ e de Lorraine, F-54000 Nancy, France
{michel.zasadzinski,cedric.join}@univ-lorraine.fr
3M. Fliess is with Laboratoire Jacques-Louis Lions (LJLL),
UMR CNRS 7598, Sorbonne Universit´ e, 75005 Paris, France
michel.fliess@sorbonne-universite.fr
proposed for a three-phase stacked interleaved buck conver ter
supplying a PEM electrolyzer [7], where a gate fault in one
phase is considered. The proposed strategy enables continu ed
operation under a degraded two-phase mode. Nevertheless,
AFTC strategies addressing sensor faults accommodation
for PEMWE systems remain largely unexplored and is the
purpose of this work.
This paper proposes an active sensor fault-tolerant con-
trol strategy for a PEMWE system coupled with DC/DC
converter supplied by RES. The proposed approach ensures
closed-loop operation under RES voltage variations and is
model-free, i.e. it does not rely on a mathematical modeling
of the system for fault detection and accommodation.
This paper is organized as follows. Section II describes
the PEMWE and DC/DC converter models which is used as
a test bench for validation and states the problem of sensor
AFTC. Section III presents the proposed model-free sensor
fault accommodation approach, accounting for variations i n
the input voltage. Simulation results are provided in Secti on
IV, and conclusions are drawn in Section V.
II. PEMWE MODELING AND CONTROL
OBJECTIVE
A. Modeling and control objective
The PEMWE model used in this paper is the one given
in [8] which has been identiﬁed using Electrochemical
Impedance Spectroscopy (EIS) method detailed in [9], [10].
The best obtained model in [8] is the one of order 6 and is
given by (1).
In order to obtain a model for the whole PEMWE + SIBC
converter, we need to express the transfer function in (1) wi th
passive electrical components. This can be achieved using t he
residue theorem [11] as follows
G(s) =
6∑
h=1
Rh
ChRhs + 1 + R0, (2)
where
R6 = 100.06 Ω, R 5 = 13.588 Ω, R 4 = 1.4068 Ω,
R3 = 0.20564 Ω, R 2 = 0.040826 Ω, R 1 = 0.0085339 Ω,
C6 = 1.0361 × 10−6 F, C 5 = 9.4843 × 10−5 F,
C4 = 0.0086629 F, C 3 = 0.72622 F, C 2 = 27.953 F,
C1 = 901.43 F, R 0 = 0.027366 Ω.
So the coupling of the PEMWE model given by (2) with
the SIBC converter is represented by Fig. 1 where VRES is
the voltage supplied by the RES, u is the control input and
arXiv:2607.10883v1  [eess.SY]  12 Jul 2026

G(s) = 0.02737s6 + 403s5 + 4.667e05s4 + 5.015e07s3 + 5.068e08s2 + 6.438e08s + 1.009e08s6 + 1.051e04s5 + 8.42e06s4 + 6.784e08s3 + 4.788e09s2 + 4.214e09s + 4.684e08 (1)
I
R1
C1
R6
C6
R0
V
vc1 vc6
vcs
Cp
Cs
Rℓs Ls is
Rℓp Lp ip
T4
T3
T2
T1
−
+VRES
PWM
u
Stacked interleaved
DC-DC buck converter
PEMWE equivalent electrical circuit
Fig. 1: Stacked interleaved DC-DC buck converter with pulse width modulation (PWM) and electrical model of PEMWE
the SIBC electrical components are given by: Lp = Ls =
426 × 10−6 H, Rℓp = Rℓs = 0 .06 Ω, Cp = 10 −4 F and
Cs = 10 −5 F.
Using the average state-space approach proposed in [12]
and detailed in [13], a state-space model for the system give n
in Fig. 1 is derived in [14] in the case of the number of
parallel RC cells is equal to 2 instead of 6 in (2). So using
straightforward developments, the state-space model in [1 4]
leads to the following one
˙x(t) = Ax(t) + BVRES (t)u(t) (3a)
y(t) = Cx(t) (3b)
where u(t), x(t) and y(t) are the control law, the state vector
and the regulated output respectively, where
x(t)T = [ip is V v cs vc1 . . . v c6] (4a)
y(t) = I(t). (4b)
The state-space matrices are given by
A =


−Rℓp
Lp
0 −1Lp 0 0 1×6
0 −Rℓs
Ls
−1
Ls
−1
Ls
01×6
1
Cp
1
Cp
−1
R0Cp
0 11×6
R0Cp
0 1Cs 0 0 0 1×6
06×1 06×1 A0 06×1 A


B =


1
Lp
1
Ls
08×1

 ,
C =
[
0 0 1R0 0 −11×6R0
]
where A ∈ I R6×6 and A0 ∈ I R6×1 are given by (for h =
1, . . . ,6 and q = 1, . . . ,6)
A(h, h) = −1RhCh + −1R0Ch ,
A(h, q) = −1R0Ch h ⁄= q,
A0(h) = 1R0Ch .
In this paper, the RES supplied voltage VRES (t) is known
and bounded as
VRES (t) ∈ [VRESm VRESM ] (5)
where VRESm = 25 V and VRESM = 55 V .
Based on Faraday’s law [15], the ﬂow rate hydrogen ˙mH2
produced by PEMWE is given by
˙mH2 = NcI2F ηH2 (6)
where Nc = 3 is the number of cells in the stack, F =
96485 is Faraday’s constant, and ηH2 is Faraday’s efﬁciency
coefﬁcient taken as 0.97. So, considering the hydrogen ﬂow
rate as the control objective is like controlling the curren t I
at the desired setpoint I ⋆.

B. Problem statement
The measured current ym is expressed as
ym = Im = y + f + ω (7)
where y is deﬁned in (4b), f is a sensor fault, and ω is a
zero-mean white Gaussian noise.
If the sensor fault f is not taken into account in the
synthesis of the control law, then it is Im and not I that
converges to the desired setpoint value I ⋆. So an AFTC is
therefore necessary to compensate the effect of f on the
closed-loop behavior in order to ensure that I converges to
I ⋆ despite f ⁄= 0 and the variations of VRES (t).
This problem is solved in Sect. III by employing our
model-free viewpoint on fault detection, estimation, and
accommodation.
Remark 1: It is important to note that the proposed ap-
proach detailed in Sect. III does not use Eq. (3), which will b e
used in Sect. IV to emulate the PEMWE + SIBC behavior. □
III. MODEL-FREE SENSOR FAULT
ACCOMMODATION FOR PEMWE
Before presenting the AFTC procedure, we brieﬂy de-
scribe the model-free control design that is used in this pap er.
A. Model-free control
Model-free control is based on an ultra-local model given
by [16], [17]
˙ym = F + αu (8)
where F corresponds to the unknown part, u and ym are
the control input and measured output, α is an appropriate
constant coefﬁcient. An estimation of F reads [16]
ˆF(t) = − 6τ 3
∫ t
t−τ
[(τ − 2σ)ym(σ) + ασ(τ − σ)u(σ)] dσ
The corresponding closed-loop control law, or intelligent
proportional controller (iP), reads [16]
u = −
ˆF − ˙y⋆ + Kpe
α (9)
where y⋆ = I ⋆ is the reference trajectory, e = ym − y⋆ is
the tracking error, while Kp is a tuning gain.
In the presence of a sensor fault f ⁄= 0, the tracking error
e converges to 0 but y does not track asymptotically y⋆ since
ym ⁄= y.
B. Model-free active fault tolerant control
1) Residual generation: We consider the following resid-
ual
r(t) = ym(t) − β(t)ˆym(t) (10)
where ˆym is given by
ˆym(t) =
∫ t
0
(
ˆF (σ) + αu(σ)
)
dσ + ˆym(0) (11)
and β(t) is a parameter to be determined. For sensor fault
detection and estimation purposes the residual in Eq. (10)
must satisfy the following conditions
• if f (t) = 0 , then r(t) = 0 , ∀ VRES (t),
• if f (t) ⁄= 0, then r(t) ⁄= 0, ∀ VRES (t).
So, when f (t) = 0 , the residual r(t) is equal to 0, if
β(t) = ym(t)ˆym(t) = ym(t)∫ t
0
(
ˆF (σ) + αu(σ)
)
dσ + ˆym(0)
(12)
where the steady-state values of the ym and ˆym are used. It
has been shown [18], [19] that β(t) in Eq. (10) is constant
for Linear Time Invariant (LTI) systems. But the PEMWE
system in (4) is not LTI due to the variations of VRES . Those
variations are inﬂuencing ˆym(t) and β(t). It follows that β(t)
should be expressed as depending on VRES (t). Since the iP
controller guarantees local stability, the steady-state i s still
achieved and the control input u(t) in steady-state can be
expressed as follows
u(t) = c(t)y(t) = c(t)ym(t) (13)
To approximate the integral in Eq. (12), the well-known
rectangle method is used, where Te is the sampling time:
∫ t
0
q(σ)dσ ≃
k∑
i=1
q(i)Te
and
˙q(t) ≃ δq(i) = q(i) − q(i − 1)Te
After straightforward computations, ˆym is expressed as
follows (see [20] for more details):
ˆym(kTe) = ym(kTe) + αTeu(kTe) − ym(0) + ˆym(0) (14)
where ˆF (kTe) is given by (see Eq. (8))
ˆF (kTe) = δym(kTe) − αu((k − 1)Te) (15)
Insert Eq. (13) in Eq. (14), assume that ym(0) ≃ ˆym(0),
then
β(kTe) = ym(kTe)ym(kTe) (1 + Teαc(kTe)) = 11 + Teαc(kTe)(16)
Let VRES i and ci be the values of VRES (kiTe) and
c(kiTe) where (kiTe) is a given time-instant in the steady-
state behavior, where k > k i.
Since the closed-loop stability and steady-state are
achieved, ˙x = 0 in Eq. (3), c(kTe) in Eq. (13) reads
c(kTe) = ci(1 + δc(kTe)) (17)
From
VRES (kTe) = VRES i(1 + δVRES (kTe)) (18)
we obtain
δc(kTe) = −δVRES (kTe)1 + δVRES (kTe) (19)
Via Eqs. (17), (18), (19) and (16), β(kTe) becomes
β(kTe) = 1
1 + VRESi (1 − βi)VRES (kTe)βi
(20)
where βi = β(kiTe).

2) Sensor fault estimation and accommodation: If f ⁄= 0
in Eq. (7), we obtain
u(kTe) = c(kTe)y(kTe)
= c(kTe)(ym(kTe) − f (kTe) − ω(kTe)) (21)
ˆym(kTe) = ym(kTe) + αTec(kTe)(ym(kTe) − ˆf (kTe))
(22)
where the initial condition is chosen by ˆym(0) ≃ ym(0), and
ˆf is the estimation of the sensor fault f to be determined.
Notice that ˆf is used in Eq. (22) in place of f since ˆym does
not depend explicitly of the noise ω.
Via Eqs. (20), (22), and (10), we get
r(kTe) = ym(kTe) − 11 + Teαc(kTe) ×(
ym(kTe)(1 + αTec(kTe)) − αTec(kTe) ˆf (kTe)
)
= αTec(kTe) ˆf (kTe)1 + αTec(kTe)
= ˆf (kTe)
(
1 − 11 + αTec(kTe) )
= ˆf (kTe)(1 − β(kTe)) (23)
and the best estimation of sensor fault f (kTe) is given by
ˆf (kTe) = r(kTe)1 − β(kTe) (24)
where β(kTe) ⁄= 1 (see Eq. (16)).
The threshold of the residual r(kTe) is called ρ(kTe). It
is given by
ρ(kTe) = ~f |1 − β(kTe)| (25)
where ~f is the minimal absolute value of the sensor fault
ˆf (kTe) to be detected and estimated.
Once the sensor fault is detected and estimated, i.e,
|r(t)| > |ρ(t)|, the sensor fault accommodation is made by
adapting the tracking error deﬁned in (9) as follows
e(kTe) = ym(kTe) − y⋆(kTe) − ˆf (kTe) (26)
IV. SIMULATIONS RESULTS
Two cases are considered: the 1st one with constant
VRES = 40 V corresponding to Fig. 3 and Fig. 4 and
the 2nd one with variable VRES which is shown in Fig. 2
corresponding to Fig. 5 and Fig. 6. In these two cases, there
is no sensor fault accommodation procedure in Fig. 3 and
Fig. 5, while the AFTC is applied in Fig. 4 and Fig. 6.
Transient behaviors can be distinguished from steady-stat e
behaviors: colored areas correspond to transient behavior s,
while uncolored areas are associated with steady-state be-
haviors.
In Fig. 3 to Fig. 6, ρ+(kTe) = ρ(kTe) and ρ−(kTe) =
−ρ(kTe) where ~f = 0 .5 A (see Eq. (25)). In the mea-
surement Eq. (7), ω is a zero-mean white Gaussian noise
with standard deviation σω = 0 .0231. The value of the iP
controller parameters are α = 9750 and Kp = 100.
0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
Time [s]
25
30
35
40
45
50
55Voltage [V]
Fig. 2: VRES variations
For all treated cases, we can see that the iP controller en-
sures closed-loop stability and asymptotic trajectory tra cking.
So, the AFTC procedure can be applied on the steady-state
behavior. For the 1st case, the sensor fault f = 2 A appears
at time t = 30 s (see Fig. 3c and Fig. 4c) and the threshold
ρ is constant (see Fig. 3b and Fig. 4b), while the occurrence
of the sensor fault f = −4 A appears at time t = 60 s for
the 2nd case (see Fig. 5c and Fig. 6c) and the threshold ρ is
slightly variable (see Fig. 5b and Fig. 6b).
For the case where there is no accommodation procedure,
the following comments can be made on Fig. 3 and Fig. 5:
• the residual r exceeds the threshold ρ at a time-instant
very close from the occurrence of the sensor fault,
allowing the fault detection and estimation (see Fig. 3b
and Fig. 5b);
• the sensor fault is well estimated (see Fig. 3c and Fig.
5c);
• after the fault occurrence, the measurement ym follows
the desired trajectory y⋆ instead of the regulated output
y (see Fig. 3a and Fig. 5a).
For the case where the AFTC procedure is applied, the
following comments can be made on Fig. 4 and Fig. 6:
• the residual r exceeds the threshold ρ at a time-instant
very close from the occurrence of the sensor fault,
allowing the fault detection and estimation (see Fig. 4b
and Fig. 6b). At this time-instant, the AFTC procedure
is triggered;
• the sensor fault is well estimated (see Fig. 4c and Fig.
6c);
• once the AFTC procedure is triggered, the regulated
output y follows the desired trajectory y⋆, which means
that the AFTC is effective (see Fig. 4a and Fig. 6a).
Notice that, the AFTC is not triggered in the transient
behavior, so the measurement ym follows the desired
trajectory y⋆ instead of the regulated output y;
• by comparing Fig. 3d and Fig. 4d on the one hand, and
Fig. 5d and Fig. 6d on the other, we can see how the
AFTC procedure has modiﬁed the control input u.

V. CONCLUSIONS
Detection and accommodation of current sensor fault for
the PEMWE were discussed. This measurement is essential
for controlling hydrogen production via a water electrolyz er.
The method developed does not rely on an analytical model
of the process: the detection and compensation of sensor
faults are model-free. The simulation results conﬁrm that the
actual current of the electrolyzer is regulated to the desir ed
current despite signiﬁcant variations in the voltage suppl ying
the process in the presence of a sensor fault.
The fact that our approach is model-free and based on an
ultra-local model makes it a good candidate for real-time
application on a test bench, with low computational burden.
The implementation of this method on a real test bench is
being considered as part of future work.
REFERENCES
[1] D. Falc˜ ao and A. Pinto, “A review on PEM electrolyzer mod elling:
guidelines for beginners,” J. Cleaner Production , vol. 261, p. ID
121184, 2020.
[2] S. Sood, O. Prakash, J.-Y . Dieulot, M. Boukerdja, B. Ould -Bouamama,
and M. Bressel, “Robust diagnosis of PEM electrolysers usin g LFT
bond graph,” International Journal of Hydrogen Energy , vol. 47,
no. 80, pp. 33 938–33 954, 2022.
[3] D. Shen, Y . Dong, Z. Lei, F. Y ang, L. Cheng, and J. Jing, “Fa ult
diagnosis of cells in pem electrolyzer stack under ﬂuctuati ng power
source,” International Journal of Hydrogen Energy , vol. 97, pp. 350–
361, 2025.
[4] F. Aubras, C. Damour, M. Benne, S. Boulevard, M. Bessaﬁ,
B. Grondin-Perez, A. J.-J. Kadjo, and J. Deseure, “A non-int rusive
signal-based fault diagnosis method for proton exchange me mbrane
water electrolyzer using empirical mode decomposition,” Energies,
vol. 14, no. 15, p. 4458, 2021.
[5] V . Guida, D. Guilbert, G. Vitale, and B. Douine, “Design a nd real-
ization of a stacked interleaved DC-DC step-down converter for PEM
water electrolysis with improved current control,” Fuel Cells, vol. 20,
pp. 307–315, 2020.
[6] B. Y odwong, D. Guilbert, W. Kaewmanee, M. Phattanasak, M . Hinaje,
and G. Vitale, “Improved sliding mode-based controller of a high
voltage ratio DC-DC converter for electrolyzers supplied b y renewable
energy,” IEEE Trans. Industrial Electronics , vol. 71, pp. 8831–8840,
2024.
[7] X. Guo, S. Zhang, Z. Liu, L. Sun, Z. Lu, C. Hua, and J. M.
Guerrero, “A new multi-mode fault-tolerant operation cont rol strategy
of multiphase stacked interleaved buck converter for green hydro-
gen production,” International Journal of Hydrogen Energy , vol. 47,
no. 71, pp. 30 359–30 370, 2022.
[8] M. Zasadzinski, M. Ait Ziane, and M. Alma, “Experimental identiﬁ-
cation approaches for a PEM water electrolyzer,” in Proc. IEEE Int.
Conf. Control, Decision and Information Technologies , Split, Croatia,
2025.
[9] T. Vidakovi´ c-Koch, T. Miliˇ ci´ c, L.ˇZivkovi´ c, H. Seng Chan, U. Krewer,
and M. Petkovska, “Nonlinear frequency response analysis: a recent re-
view and perspectives,” Current Opinion in Electrochemistry , vol. 30,
p. ID 100851, 2021.
[10] T. Miliˇ ci´ c, M. Sivasankaran, C. Bl¨ umner, A. Sorrent ino, and T. Vi-
dakovi´ c-Koch, “Pulsed electrolysis − explained,” Faraday Discus-
sions, vol. 246, pp. 179–197, 2023.
[11] K. Ogata, Modern Control Engineering . Englewood Cliffs, New
Jersey: Prentice Hall, 1970.
[12] R. Middlebrook and S. Cuk, “A general uniﬁed approach to modelling
switching-converter power stages,” in Proc. IEEE Power Electronics
Specialists Conf. , Cleveland, USA, 1976.
[13] N. Mohan, T. Undeland, and W. Robbins, Power Electronics, 2nd ed.
New Y ork: Wiley, 1995.
[14] R. Maamouri, D. Guilbert, M. Zasadzinski, and H. Rafara lahy, “Proton
exchange membrane water electrolysis: modeling for hydrog en ﬂow
rate control,” Int. J. of Hydrogen Energy , vol. 46, pp. 7676–7700,
2021.
[15] M. Ait Ziane, M. Zasadzinski, A. Bouramdane, E. Pahon, a nd
H. Rafaralahy, “Experimental control of a PEM water electro lyzer:
investigation of renewable energy source framework,” in Proc. IEEE
Int. Conf. Control, Decision and Information Technologies , Split,
Croatia, 2025.
[16] M. Fliess and C. Join, “Model-free control,” Int. J. Control , vol. 86,
pp. 2228–2252, 2013.
[17] ——, “An alternative to proportional-integral and prop ortional-
integral-derivative regulators: Intelligent proportion al-derivative reg-
ulators,” Int. J. Robust & Nonlinear Contr . , vol. 32, pp. 9512–9524,
2022.
[18] M. Ait Ziane, C. Join, and M. Zasadzinski, “Sensor fault ac-
commodation: a model-free framework,” Int. J. Control , 2025,
https://doi.org/10.1080/00207179.2025.2482182.
[19] M. Ait Ziane, M. Zasadzinski, C. Join, and M. P´ era, “Mod el-free
active sensor fault tolerant control for systems with linea r static
characteristic,” Int. J. of Dynamics and Control , vol. xx, pp. xx–xx,
2024, soumis.
[20] ——, “Model-free active sensor fault tolerant control f or systems with
linear static characteristic,” Int. J. of Dynamics and Control , vol. 13,
p. ID 267, 2025.

0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
Time [s]
0
2
4
6
8
10
12
14
16
18Current  [A]
(a) Trajectory tracking without AFTC
 (b) Residual r
(c) Estimated sensor fault ˆf
0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
Time [s]
0
0.02
0.04
0.06
0.08
0.1
(d) Control input u
Fig. 3: Constant VRES without AFTC
0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
Time [s]
0
5
10
15
20Current  [A]
(a) Trajectory tracking with AFTC
 (b) Residual r
(c) Estimated sensor fault ˆf
0 10 20 30 40 50 60 70 80 90 100 110 120 130 140
Time [s]
0
0.02
0.04
0.06
0.08
0.1
0.12
(d) Control input u
Fig. 4: Constant VRES with AFTC

0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
Time [s]
0
2
4
6
8
10
12
14
16
18
20Current  [A]
(a) Trajectory tracking without AFTC
 (b) Residual r
(c) Estimated sensor fault ˆf
0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
Time [s]
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
(d) Control input u
Fig. 5: V ariable VRES without AFTC
0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
Time [s]
0
2
4
6
8
10
12
14
16
18
20Current  [A]
(a) Trajectory tracking without AFTC
 (b) Residual r
(c) Estimated sensor fault ˆf
0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
Time [s]
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
(d) Control input u
Fig. 6: V ariable VRES with AFTC
