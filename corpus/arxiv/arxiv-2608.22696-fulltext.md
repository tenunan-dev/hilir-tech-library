---
source_id: "arxiv"
title: "Unit-to-Plant Stability Shaping of Multi-Electrolyzer"
url: "https://arxiv.org/abs/2608.22696"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2608.22696. Abstract: Unit-to-Plant Stability Shaping of Multi-Electrolyzer 
ReP2H Plants via Interface Design and Dispatch 
Miao Zhang, Yiwei Qiu, Member, IEEE, Xiaoyu Wang, Linlin Wu, Yi Zhou, Member, IEEE, Shi Chen, Member, IEEE,  
Buxiang Zhou, Member, IEEE, and Kaigui Xie, Fellow, IEEE
Abstract—Alkaline water electrolysis (AWE) units supplied by 
insulated gate bipolar transistor rectifiers (IGBT-Rs) may experi-
e"
---

# Unit-to-Plant Stability Shaping of Multi-Electrolyzer

Unit-to-Plant Stability Shaping of Multi-Electrolyzer 
ReP2H Plants via Interface Design and Dispatch 
Miao Zhang, Yiwei Qiu, Member, IEEE, Xiaoyu Wang, Linlin Wu, Yi Zhou, Member, IEEE, Shi Chen, Member, IEEE,  
Buxiang Zhou, Member, IEEE, and Kaigui Xie, Fellow, IEEE
Abstract—Alkaline water electrolysis (AWE) units supplied by 
insulated gate bipolar transistor rectifiers (IGBT-Rs) may experi-
ence oscillations caused by coupling between rectifier control and 
electrolyzer (ELZ) dynamics. Because this risk varies with unit 
loading and power allocation, production-oriented dispatch may 
place a multi-ELZ renewable power-to-hydrogen (ReP2H) plant 
near or exceed its stability boundary. This paper proposes a sta-
bility-oriented framework for control design and plant production 
dispatch. A three-port admittance model links the ac port, dc link, 
and electrolysis stack. Unit-level dc-port analysis quantifies the ef-
fects of loading, temperature, Buck bandwidth, and dc-link capac-
itance, while plant -level aggregation evaluates how unit commit-
ment and power allocation  affect stability. Results show that 
higher loading reduces stability, whereas larger dc -link capaci-
tance and higher Buck bandwidth improve it. Under the same 
plant loading, different power allocations result in different plant-
level stability margins, with balanced allocation generally provid-
ing a larger margin than concentrated allocation. The plant-level 
model thus distinguishes the stability margins of admissible sched-
ules. Hardware-in-the-loop (HIL) tests validate these trends and  
the proposed redistribution rule . The resulting operating regions 
and dispatch rules can be used to screen unit commitment and 
power allocation decisions in plant production scheduling. 
Index Terms —Alkaline water electrolysis , three-port admit-
tance model, renewable power-to-hydrogen, stability regions 
I. INTRODUCTION 
A. Background and Motivation 
Large-scale renewable power -to-hydrogen (ReP2H) plants 
typically comprise multiple rectifier -fed electrolyzers (ELZs), 
connected in parallel at the point of common coupling (PCC) 
[1], [2]. These plants are often co-built and located near renew-
able energy bases and therefore operate under weak-grid condi-
tions with limited short-circuit capacity.  
As shown in Fig. 1, a typical industry-rated ELZ includes an 
alkaline water electrolysis (AWE) stack, a Buck converter, a dc 
link, and an insulated gate bipolar transistor rectifier (IGBT -R) 
[3]. The IGBT -R regulates the ac current and dc-link voltage, 
while the Buck converter controls the stack current. Their dy-
namics are coupled through the dc link, so stack current varia-
tions can affect the ac response  [4], [5]. A similar cascaded 
structure appears in railway traction systems, comprising a grid- 
connected converter, a regulated dc link, and a controlled 
downstream load , where f ast converter dynamics and dc -link 
coupling can interact with network impedance and cause low -
frequency oscillations [6], [7]. Such observations imply com-
parable oscillatory risks in ReP2H plants. 
Beyond converter control, the AWE stack introduces operat-
ing-point-dependent dynamics on the dc side [8]. Its voltage re-
sponse is governed by activation polarization, ohmic loss, and 
electric-double-layer (EDL) effects, which vary with tempera-
ture, current density , and degradation  [9], [10]. Variations in 
stack current pass through the Buck converter and perturb the 
dc link, while the IGBT-R responds through dc-link voltage and 
ac current control. This feedback interaction may also cause dc-
port oscillations that propagate to the ac side . Since stack dy-
namics vary with operating conditions, t he stability character-
istics depend on the operating point and are difficult to assess. 
The assessment of stability becomes more complex in large-
scale ReP2H systems, where the energy management system 
(EMS) determines the operating states and power references of 
individual ELZ units [11]. Different production schedules can 
place the ELZs at different operating points under the same total 
production command, changing the plant-level dynamic re-
sponse and stability margin. Recent small -signal stability stud-
ies show that control bandwidth, unit loading, stack temperature, 
gas pressure, and grid strength can shift system modes and sta-
bility boundaries [12], [13]. However, most studies address a 
single unit or homogeneous aggregation and l eave the com-
bined stability of ELZs at different operating points unresolved. 
A port-based framework is thus needed to retain dc-link cou-
pling, identify unit stability boundaries, and formulate stability 
constraints for unit commitment and power allocation.  
B. Literature Review and Research Gap 
Large-scale ReP2H plants commonly comprise multiple rec-
tifier-fed ELZs, with each rectifier supplying one unit . The 
plant at the China Energy Engineering Songyuan Hydrogen In-
dustry Park [14] employs 32 thyristor rectifiers and 32 IGBT 
rectifiers to supply 64 AWEs, and the Wind Solar Hydrogen 
Ammonia Integration Project [15] in Da’an uses 12 thyristor 
rectifiers and 24 IGBT -Rs for 36 AWEs. Zeng et al. [16] opti-
mized the portfolio of rectifiers. Gao et al. [17] and Koponen et 
al. [18] compared their techn o-economic performance, while 
Meng et al. [19] proposed a hybrid rectifier to improve power 
quality. These works support rectifier selection and steady-state 
design; however, t he dynamic  interaction among parallel 
IGBT-R-fed ELZs has received limited attention [20]. 
Multi-ELZ operation has been widely studied from the 
scheduling perspective. Zeng et al. [21] proposed coordinated 
active and reactive power dispatch. Qiu et al. [22] included ther-
mal and impurity constraints in plant scheduling . Li et al. [23] 
developed an energy management method for grid -connected 
Financial support came from the National Natural Science Foundation of 
China (52377116 and 52312076). (Corresponding author: Yi Zhou) 
M. Zhang, Y. Qiu, Y. Zhou, S. Chen, B. Zhou, and K. Xie are with the Col-
lege of Electrical Engineering, Sichuan University, Chengdu 610065, China. 
(yizhou3230@scu.edu.cn) 
X. Wang and L. Wu are with the State Grid Jibei Electric Power Co., Ltd. 
Research Institute, Beijing, China, and the North China Electric Power Re-
search Institute Co., Ltd., Beijing, China. L. Wu is also with the State Grid Jibei 
Zhangjiakou Wind-Solar-Storage-Transmission New Energy Co., Ltd., Zhang-
jiakou, China. 

multi-stack plants. Firdous et al. [24] studied the flexibility of 
large-scale P2H systems. These methods optimize unit commit-
ment, power allocation, and state transitions under power bal-
ance and process constraints  [25]. Although these decisions 
change the operating point and dynamic response of each unit , 
electrical stability has rarely been considered. 
The dc -side dynamics of AWE units have been studied 
through electrochemical and converter models . Ulleberg [26], 
Varela et al . [27], and Iribarren et al . [28] developed AWE 
models for system analysis and dispatch. Guilbert et al. [29] and 
Guo et al. [30] studied dc converters and power electronic in-
terfaces for electrolysis. These studies show that stack parame-
ters, operating conditions, and Buck control affect unit dynam-
ics. However, the reported analyses mainly characterize se-
lected operating conditions and do not determine the boundary 
between stable and unstable states in grid-connected operation. 
Impedance-based methods provide a suitable means of deter-
mining this boundary because they quantify stability from in-
teractions among connected ports  [31]. Pedra et al . [32] and 
Zong et al. [33] developed three-port and multiport models for 
common voltage-source converters (VSCs) that retain ac and dc 
coupling. Fang et al. [34] assessed weak-grid stability of a sin-
gle-unit rectifier-interfaced hydrogen system . These e xisting 
studies mainly consider generic converters or represent the hy-
drogen plant as a single unit.  They do not link the dc -port sta-
bility of each IGBT -AWE unit with the aggregated ac -port re-
sponse of units operating at different points. Consequently, the 
plant-level stability region associated with unit commitment 
and power allocation remains unavailable. Retaining the d-axis 
and q-axis ac ports together with the dc -link port is necessary 
because the dc-port termination changes each unit’s ac-port re-
sponse before aggregation at the PCC. The three -port frame-
work therefore supports both unit -level dc-port boundary deri-
vation and plant -level stability assessment without discarding 
the ac/dc coupling. 
C. Contributions of This Work 
To address these gaps, this paper develops a stability -ori-
ented operating framework for large-scale ReP2H plants. The 
main contributions are as follows: 
1) An operating -point-dependent three -port admittance 
model is established for the complete IGBT -AWE unit. The 
model retains the dc-link as an explicit port, enabling unit-level 
dc-port reduction and pl ant-level ac -port aggregation  within 
one formulation. Its accuracy is validated by a frequency sweep 
against a detailed switching model. 
2) For each ELZ, the dc-port stability margin is mapped over 
stack loading, temperature, Buck bandwidth, and dc-link capac-
itance to construct the stability region for operating and inter-
face design. A multi -input multi-output (MIMO) Nyquist dis-
tance is further introduced to evaluate the plant -level stability 
margin under different unit-commitment and power  allocation 
schemes in a multi-ELZ plant. 
3) A lookup-based stability-screening rule is developed for 
multi-ELZ dispatch. Analytical results and multi -unit hard-
ware-in-the-loop (HIL) tests show that different power alloca-
tions can produce different stability margins and dynamic re-
sponses under the same total production command. They also  
 
Fig. 1. Topology of a multi-ELZ ReP2H plant and the three-port representa-
tion of an IGBT-AWE unit 
confirm that stability-oriented power redistribution can increase 
the plant-level stability margin and suppress oscillations. 
The rest of this paper is organized as follows: Section II pre-
sents the three-port admittance model for the IGBT-AWE units 
and stability criteria. Section III analyzes the effects of operat-
ing conditions and interface parameters on stability. Section IV 
develops unit-level operating-and-design regions and derives a 
plant-level stability -oriented power -allocation rule. Section V 
presents the HIL validation. Section VI concludes the paper.  
II. PORT-BASED MODELING AND STABILITY CRITERIA OF THE 
MULTI-ELZ REP2H PLANT 
As shown in Fig. 1, a typical ReP2H plant consists of multi-
ple IGBT-AWE units connected in parallel. Each unit includes 
an IGBT-R, a capacitive dc link, a current-controlled Buck con-
verter, and an AWE stack. To characterize the coupling be-
tween the ac-grid interface and the dc-side electrolysis dynam-
ics, this section establishes a three-port admittance model for a 
representative unit, with the dq-frame ac port and the dc -link 
port explicitly retained. 
A. Three-Port Admittance Model of the IGBT-AWE Unit  
The IGBT -R connects the ac bus to the Buck -interfaced 
AWE stack through the dc link. A two -port ac representation 
would eliminate the dc -link termination through which the 
Buck-AWE dynamics affect the rectifier ’s ac -port response. 
The IGBT -R is therefore represented by a three -port admit -
tance model with the d-axis, q-axis, and dc ports. Linearization 
around a steady-state operating point gives: 
 
TT
d q dc IGBT-R d q dc
s s s si i i Y u u u      =       , (1) 
where 
 
dd dq d,dc
IGBT-R qd qq q,dc
dc,d dc,q dc,dc
Y Y Y
Y Y Y Y
YYY

=
 , (2) 
where the superscript s denotes the system dq-frame; ∆ denotes 
small-signal perturbation; ∆id, ∆iq and ∆idc are the d-axis, q-axis, 
PV
Wind
Battery
i
CBuck
u
idc
udcus
znet+zT L
AC Source IGBT-R Buck+AWE
ac-port dc-port
Cd
Grid
Unit 2
IGBT-AWE
Unit 1
IGBT-AWE
Unit n
IGBT-AWE


 
Fig. 2. Equivalent electrical model and steady-state characteristics of the 
AWE stack 
and dc-link current perturbations of the IGBT -R, respectively; 
∆ud, ∆uq and ∆udc are the corresponding voltage perturbations. 
In YIGBT-R, the upper -left 2× 2 block represents the ac -port dq 
admittance. The elements Yd,dc and Yq,dc represent the influence 
of dc-link voltage perturbation on the ac-port current response, 
while Ydc,d and Ydc,q characterize the coupling from the ac -port 
voltages to the dc-port current. The element Ydc,dc is the dc-port 
self-admittance. The detailed deriv ation of YIGBT-R is provided 
in Appendix A. 
B. DC-Port Model of the Buck-Interfaced AWE Stack 
The dc port of the IGBT -R is terminated by the dc -link ca-
pacitor and the Buck-interfaced AWE stack. The corresponding 
dc-side admittance is expressed as: 
 
dcrc d Buck-AWE ,Y sC Y=+  (3) 
where Cd is the dc-link capacitance and YBuck-AWE is the dc-input 
admittance of the Buck-interfaced AWE stack. The latter is de-
termined by the AWE stack, Buck power stage, and current con-
troller dynamics; the corresponding model is derived below. 
As shown in Fig. 2(a), the Buck -interfaced AWE model re -
tains the activation, ohmic, shunt, and EDL dynamics over the 
frequency range considered in this study. The electrochemical 
dynamics are formulated at the cell level, with the stack termi-
nal voltage and current defined in the final line of (4), as follows: 
 
dl bp
dl
cell dl ohm dl act
2[ ( )]cell
act dl
d( ), , d
, ( , ), ( 1) ,
ss
F uuRT
s T T
s
uu u r j j C j j j t
uj j f u T f er  −
 = + − = − −
 = = = −  (4) 
where ucell and udl are the single-cell terminal and EDL voltages, 
respectively; j, js and jact are the total, shunt, and activation cur-
rent densities; and  rohm, rs and Cdl are the area -specific ohmic 
resistance, shunt resistance, and EDL capacitance; the nonlinear 
function fT denotes the modified Tafel activation relation [35]; 
F denotes the Faraday constant ; R is the gas constant ; T is the 
temperature; α is the activation coefficient ; and β is the ex-
change current density. 
For a specified stack-current operating point, (4) is solved to 
determine the corresponding steady -state stack voltage and in-
ternal electrochemical variables. The resulting stack voltage -
current characteristic is shown in Fig. 2(b). 
For small-signal impedance modeling, the nonlinear activa-
tion relation is linearized around a steady-state operating point: 
 
( )T dl
act 1 dl 1
dl 0
,, f u Tj h u h u =  =  , (5) 
TABLE I 
PARAMETERS OF A TYPICAL 5-MW-RATED IGBT-AWE UNIT  
Symbols Parameter Value 
ud0 d-axis steady voltage 565 V 
id0 d-axis steady current 5993 A 
udc0 Steady dc-link voltage 1500 V 
f0 Fundamental frequency 50 Hz 
Rf, Lf Filter resistor and inductor 0.0015 Ω, 200 μH 
Rg, Lg Equivalent source resistor and in-ductor 0.0011 Ω, 35 μH 
Cd Dc-link capacitor 18 mF 
KP_PLL, Ki_PLL PLL control 0.08, 2 
KP_ACC, Ki_ACC ACC control 0.075, 2 
KP_DVC, Ki_DVC DVC control 15, 20 
LBuck,CBuck The inductor and capacitor of the Buck converter 1 mH, 9 mF 
KP_Buck, Ki_Buck Constant-current control of the Buck converter 8×10⁻⁵, 2×10⁻³ 
Ncell Number of series-connected cells 242 
Acell Active area of a single cell 20,000 cm² 
Urev Single-cell reversible voltage 1.228 V 
Rohm,e Stack-equivalent ohmic resistance 15.27 mΩ 
Rs,e Stack-equivalent shunt resistance 1.02 Ω 
Cdl,e Stack-equivalent double-layer ca-pacitance 15.69 F 
F Faraday constant 96485 C/mol 
R Gas constant 8.31 J/mol·K 
α Charge transfer coefficient 0.1521 
β Exchange current density 1.212×10⁻⁴ A/cm2 
T Stack temperature 353 K 
 
where h1 is the area -specific incremental activation conduct-
ance. For a stack with Ncell series connected cells and an active 
cell area of Acell, the terminal perturbations satisfy: 
 
ele cell cell ele cell ,u N u i A j =   =  . (6) 
The corresponding stack-level parameters are then obtained: 
 
cell ohm cell
ohm,e ,e
cell cell
cell dl cell 1
dl,e 1,e
cell cell
,,
,.
s
s
N r N rRR AA
A c A hCH NN
 ==
 ==  (7) 
The stack -terminal small -signal impedance is then directly 
obtained as 
 
AWE ,e ohm,e
dl,e 1,e
1() sZ s R R sC H=+  +
 . (8) 
Equation (8) explicitly retains the operating-point-dependent 
activation dynamics, the EDL effect, the ohmic voltage drop , 
and the shunt path, while avoiding separate definitions of inter-
mediate impedances. 
The obtained ZAWE is used as the load impedance of the cur-
rent-controlled Buck converter  [36]. Linearizing the Buck 
power stage and current controller around the sam e operating 
point gives: 
 
( )
1
Buck-AWE
()( ) I ()dc b b b bdcisY s C s A B D us −= = − + , (9) 
where Ab, Bb, Cb and Db are determined by the Buck inductor, 
output capacitor, current  controller and ZAWE. Substitution of  
(a) Equivalent circuit model (b) U-I and P-I curves 
iele
is
Dbp H2 Rohm
Rs
ubp uohmuele 0
Cdl
us
iact
udl
uact
6
4
2
0 Pele (MW)
200
400
600
0
Uele (V)
Iele (kA)
Pele
Uele
Boundary:
Ubp=Urev
0 4 6 82

 
Fig. 3. Frequency-sweep validation of the analytical three-port admittance 
model against the detailed switching model of the complete IGBT-AWE unit 
(9) into (3) gives the dc-side termination admittance Ydcrc used 
in the subsequent port-reduction and stability analyses. 
The parameters of a typical 5-MW-rated IGBT-AWE unit are 
listed in Table I [37]. The analytical model is validated against 
a detailed switching model by independent perturbations at the 
d, q, and dc ports from 1 to 1000 Hz. Fig. 3 shows that it repro-
duces the dominant ma gnitude, phase, and coupling character-
istics. The visible deviations occur mainly in weak coupling 
terms, whose relative errors are amplified by the logarithmic 
scale and switching ripple. The model is therefore adequate for 
the subsequent stability analysis. 
C. Unit-Level DC-Port SISO Stability Criterion 
The three-port model can be reduced at the dc port to evaluate 
the internal dc -link interaction of one IGBT -AWE unit  [38]. 
The external network admittance is expressed as:  
 
22
net 2 1
net
1 2 dcrc
0
0
Y Y
Y



=
 , (10) 
where Y
2× 2 
net  denotes the 2× 2 ac-network block in the system dq -
frame, and Ydcrc is the dc -side admittance defined in (3). The 
characteristic equation of the IGBT -R connected to the ac net-
work and dc-side admittance is: 
 
net IGBT-Rdet( ) 0YY += . (11) 
The matrix in (11) is partitioned according to the ac and dc 
ports as: 
 
12
IGBT-R net
34
QQYY QQ+=  , (12) 
where Q1 is the ac-port block; Q4 is the dc-port block; Q2 and Q3 
represent the coupling between the ac and dc ports.  Using the 
Schur complement, the dc-port reduced characteristic equation 
is obtained as: 
 
1
4 3 1 2 0Q Q Q Q−−= . (13) 
The equivalent dc -port admittance of the IGBT -R side is 
therefore defined as: 
 
1
dceq dc,dc 3 1 2Y Y Q Q Q −=− . (14) 
Accordingly, the unit -level dc -port characteristic equation 
becomes: 
 
Fig. 4. Port-reduced equivalent models for unit- and plant-level stability  
analysis 
 
dceq dcrcdet( ) 0YY += . (15) 
As illustrated in Fig. 4(a), Ydceq represents the equivalent ad-
mittance of the IGBT -R side reflected to the dc port, whereas  
Ydcrc represents the dc -link capacitor and the Buck -interfaced 
AWE stack. The critical frequency fc is determined by the mag-
nitude intersection 
 
dceq dcrc( 2 ) ( 2 )ccY j f Y j f = . (16) 
The phase difference at the critical frequency is defined as: 
 
dceq dcrc( 2 ) ( 2 )ccY j f Y j f   =  − . (17) 
The unit is regarded as stable when  ∆φ<180°, critical when  
∆φ=180°, and unstable when ∆φ>180°. This criterion is used in 
Section III to characterize the dc-port stability boundary under 
different operating and interface parameters. 
D. Plant-Level AC-Port MIMO Stability Criterion 
For plant -level analysis, the dc -side equivalent admittance 
Ydcrc,k is connected to the dc port of the kth IGBT-R. Using the 
same block partition as in (12), elimination of the dc port gives: 
 
( )
1
1, 2, 4, 3,det 0 k k k kQ Q Q Q −−= . (18) 
Although Q1,k contains the external ac network, it is not in-
cluded in the unit -equivalent admittance below. Since Ynet has 
no ac - and dc -coupling terms, Q2,k and Q3,k contain only the 
IGBT-R coupling dynamics. The block Q4,k contains the dc-port 
admittance of the IGBT-R and Ydcrc,k. Thus, the ac-port equiva-
lent admittance of the complete kth unit is 
 
2 2 1
aceq, IGBT-R, 2 4 3k k k k kY Y Q Q Q−=− . (19) 
Therefore, Yaceq,k retains the effects of the dc -link capacitor, 
Buck converter, and AWE stack, but does not include the exter-
nal ac network. When N units are connected in parallel at the 
PCC, the plant-level ac-port admittance is obtained as: 
 
plant aceq,
1
N
k
k
YY
=
= . (20) 
The characteristic equation of the p lant connected to the ex-
ternal ac network is: 
Mag/dBPhs/deg-180
0
180
10
0
-10
0
-20
-20
100
-10
5
0
-5
10
-20
20
15
10
0
-10
20
10
0
102 103
Frequency/Hz Frequency/Hz Frequency/Hz
Ydd Ydq Yd,dc
Yqd Yqq Yq,dc
Ydc,d Ydc,q Ydc,dc
-180
0
180
-180
0
180
-180
0
180
-180
0
180
-180
0
180
-180
0
180
-180
0
180
-180
0
180
102 103102103
Mag/dBPhs/degMag/dBPhs/deg
Theoretical Measured 
i
CBuck
uus
znet+zT L
Yacnet
Cd
i
CBuck
u
L
Cd
ac-port
Yaceq,1
Yaceq,k
CBuck
idc
udcus
znet+zT L
Cd
Ydcrc
dc-port
Ydceq
(a) DC-port SISO model
(b) AC-port MIMO model

 
22
net plantdet( ) 0YY += . (21) 
Defining the plant-level return-ratio matrix as: 
 
( )
122
ac plant ac ac net ,L Y Z Z Y
−== . (22) 
The plant -level stability is evaluated using the MIMO 
Nyquist trajectories of  Lac. Since the open -loop system has no 
right-half-plane poles over the operating range considered, 
plant stability requires the eigenvalue trajectories of Lac to have 
no encirclement of (−1, j0). A smaller distance to this point in-
dicates a lower stability margin. 
As illustrated in Fig. 4(b), the external ac network interacts 
with the aggregated admittance of all online IGBT-AWE units. 
Since Yaceq,k depends on the operating point of each unit, differ-
ent unit-commitment and power -allocation schemes may pro-
duce different Nyquist trajectories under the same total power 
command. This criterion forms the basis for the plant -level 
power allocation schemes in Section IV. 
III. UNIT-LEVEL DC-PORT STABILITY CHARACTERISTICS 
Fig. 5 applies the dc-port criterion to unit loading, stack tem-
perature, Buck current-loop bandwidth, and dc-link capacitance, 
with the remaining parameters fixed at the values in Table I. 
The first two are operating variables, while the latter two are 
interface parameters. The base line interface parameters in Ta-
ble I are deliberately selected near the dc -port stability bound-
ary to reveal parameter-dependent transitions. 
A. Effects of Operating Conditions 
Fig. 5(a) presents the dc -port admittances at different AWE 
current references. At the rated current of 8333 A, Ydceq and Ydcrc 
intersect at 122.3 Hz, where the phase difference is 183.1°. This 
value exceeds the 180° boundary and indicates an unstable dc -
port interaction. Reducing the current reference shifts the mag-
nitude intersection and decreases the phase difference. Lower 
unit loading therefore increases the dc-port stability margin. 
Fig. 5(b) shows the effect of stack temperature at the same 
current reference, with the steady stack voltage recalculated for 
each temperature. As the temperature increases from 343 to 373 
K, the intersection frequency rises from 119. 9 to 12 5.6 Hz, 
while the phase difference increases from 179.5° to 188.3°. The 
operating point crosses the stability boundary between 343 and 
353 K. Increasing the stack temperature therefore reduces the 
dc-port stability margin. This comparison isolates the electrical 
stability effect, while the stack voltage limit is included in the 
operating region constructed in Section IV. 
B. Effects of Interface Parameters 
Fig. 5(c) examines the Buck current -loop bandwidth  fbcl. 
Changing the bandwidth mainly reshapes Ydcrc, while the recti-
fier operating point and Ydceq remain nearly unchanged. Within 
the tested range, increasing the bandwidth reduces the phase 
difference at the magnitude intersection and moves the unit  
away from the critical condition. The Buck bandwidth sh ould 
therefore be selected by considering both current response and 
dc-port stability. 
 
Fig. 5. Unit-level dc-port stability characteristics 
Fig. 5(d) presents the effect of the dc-link capacitance. In-
creasing Cd raises the magnitude of Ydcrc near the critical fre-
quency and shifts the intersection toward a lower frequency. 
For example, increasing Cd from 16 to 18 mF reduces the phase 
difference from 206.6° to 183.1°. A larger dc-link capacitance 
therefore improves the stability margin within t he considered 
parameter range. 
IV. STABILITY-ORIENTED OPERATING REGIONS AND POWER 
ALLOCATION DISPATCH 
A. Stability-Oriented Dispatch Framework 
Large ReP2H plants use EMS to coordinate unit commitment 
and power allocation subject to loading, temperature , and gas 
impurity constraints under fluctuating renewable power supply 
[16], [17], [18]. These constraints ensure production feasibility 
but do not account for operating-point-dependent electrical sta-
bility. The proposed framework therefore uses offline operating 
and design regions to screen unit loading, temperature, Buck 
bandwidth, and dc-link capacitance, followed by plant -level 
MIMO Nyquist assessment of candidate unit-commitment and 
power-allocation schemes. Schedules with insufficient margins 
are rejected or adjusted before dispatch, and the resulting 
lookup maps avoid repeated online frequency-domain analysis. 
B. Unit-Level DC-Port Operating and Design Regions 
Based on the dc -port stability criterion in Section II -C, the 
phase difference between Ydceq and Ydcrc at their magnitude in-
tersection is used to characterize the proximity of an operating 
point to the dc -port oscillatory boundary. The corresponding 
dc-port phase margin is defined as 
 
dc 180PM = − , (23) 
where ∆φ is the phase difference at the magnitude intersection. 
An operating point without a magnitude intersection is regarded 
as stable. Otherwise, the operating points are classified as: 
 
dc dc
dc dc
Stable, 20 Low risk, 10 20
High risk, 0 10 Unstable, 0
PM PM
PM PM
  
  
      (24) 
30
20
10
0
100
0
-100
fc=122.3 Hz, Δφ=183.1°  
fc=125.2 Hz, Δφ=187.2°  
0
Frequency/Hz
40 12080 160 200
Mag/dBPhase /deg
 fbcl=10Hz
fbcl=200Hz
fbcl=50Hz
  fbcl=20HzYdcrc
Ydceq
 
 
30
20
10
100
0
-100
fc=122.3 Hz, Δφ=183.1°  
fc=139.2 Hz, Δφ=206.6°  
Mag/dBPhase /deg
0
Frequency/Hz
40 12080 160 200
 Cd=16mF
 Cd=22mF
 Cd=20mF
 Cd=18mFYdcrc
Ydceq
I
 30
Mag/dBPhase /deg
10
-10
-100
0
100
fc=122.3 Hz, Δφ=183.1°  
0
Frequency/Hz
40 12080 160 200
Iele=8333A
Iele=7000A
 Iele=5000A
Iele=3000AYdcrc
Ydceq
fc=122.3 Hz, Δφ=183.1°  
fc=125.6 Hz, Δφ=188.3°  
0
25
-100
0
100Phase /deg Mag/dB
Frequency/Hz
15
5
40 12080 160 200
 T=343K
T=363K
T =373K
T=353K
Ydceq
Ydcrc
fc=124.1 Hz, Δφ=185.9°  
fc=119.9 Hz, Δφ=179.5°  
(a) AWE current reference (b) Stack temperature
(c) Buck current loop bandwidth (d) DC link capacitance

 
Fig. 6. Unit-level dc-port operating region under fixed interface parameters 
 
Fig. 7. Unit-level dc-port design region at the rated operating condition 
The four levels classify operating points according to their 
proximity to the dc -port oscillatory boundary. For this case 
study, the 10°  and 20°  thresholds serve as adjustable engineer-
ing margins rather than universal limits. Low-risk and high-risk 
points remain stable but are increasingly sensitive to parameter 
variations and operating point changes, while points with PMdc 
≤ 0°  are classified as unstable. 
Fig. 6 presents the unit-level operating region in the load ratio 
and stack temperature plane, with th e Buck current-loop band-
width and dc -link capacitance fixed at 50 Hz and 18 mF, re-
spectively. As shown in Fig. 6(a), the dc -port phase margin re-
mains high over most low- and medium-load conditions, while 
it decreases rapidly as the load approaches its rate d value. In-
creasing the stack temperature further reduces the margin near 
the high-load boundary.  
The categorized map in Fig. 6(b) shows that most operating 
points are stable, whereas the high-risk and unstable regions are 
concentrated near the rated load. For visualization, points with-
out a magnitude intersection are displayed at PMdc=30°. The 
resulting map allows the EMS to determine the admissible unit 
loading according to the measured stack temperature. 
Fig. 7 evaluates the effects of the fbcl and Cd at the rated cur-
rent and 353 K. Fig. 7(a) shows that the dc-link capacitance has 
a dominant influence on the phase margin. Increasing Cd in-
creases the dc-port stability margin, while increasing the Buck 
bandwidth reduces the minimum capacitance required for  an 
adequate margin within the investigated range.  
The categorized design map in Fig. 7(b) identifies the com-
binations that satisfy the prescribed margin levels. Since the 
Buck bandwidth and dc-link capacitance are control and circuit 
parameters, respectively, Fig. 7 is used for controller and inter-
face design rather than online dispatch. 
 
Fig. 8. Comparison between Yaceq(2P) and 2Yaceq(P) under the same total 
power command 
 
Fig. 9. MIMO Nyquist trajectories of a 4-in-1 AWE module under different 
power allocation schemes with a total power command of 10 MW 
The two maps provide complementary information. Fig. 6 
defines the admissible operating range after the interface pa-
rameters have been selected, whereas Fig. 7 supports the offline 
coordination of the Buck controller and dc-link capacitor. Both 
maps can be generated through offline scanning and stored as 
lookup tables for  Buck-controller/dc-link capacitor coordina-
tion and multi-ELZ dispatch. 
C. Plant-Level Power Allocation Feasible Region 
At the plant level, the same hydrogen -production command 
can be achieved through different unit -commitment and power 
allocation schemes. Since the ac -port equivalent admittance of 
each IGBT-AWE unit depends on its own operating point, the 
aggregated plant admittance is not proportional to the total 
power command. Fig. 8 compares the ac -port admittance Ya-
ceq(2P) of one unit operating at power 2P with the aggregated 
admittance 2Yaceq(P) of two identical units operating at power  
P. The observed difference confirms that: 
 
aceq aceq(2 ) 2 ( )Y P Y P   (25) 
and therefore one heavily loaded unit is not electrically equiva-
lent to two lightly loaded units under the same total power com-
mand. 
A representative 4 -in-1 ELZ module comprising four inde-
pendently powered stacks is considered . In this configuration, 
four stacks share the gas separation and lye circulation equip-
ment within one balance of plant  (BoP) system , while each 
stack is supplied by an independent rectifier and can be con-
trolled separately. Each IGBT-AWE unit is rated at 5 MW, and 
the total power command is fixed at 10 MW. 
370
30
360
350
340
20
10
0
-10
-20
-30
-30
-10
10
30
370
360350340100%80%60%
40%
Load ratio T/K
PMdc/deg
40% 60% 80% 100%
Load ratio
(a) DC-port phase margin (b) Operating region
StableLow risk
High risk
Unstable
T/K
60
20
-20
50
100
15014 16 18 20 22
60
40
20
0
-20
-40
Cd/mF
22
20
18
16
20 60 100 140
fbcl/Hz
Cd/mFfbcl/Hz
PMdc/deg
StableLow risk
High risk
Unstable
(a) DC-port phase margin (b) Design region
100
Frequency / Hz
300 500 700 900 100 300 500 700 900
100 300 500 700 900 100 300 500 700 900
Frequency / Hz
Frequency / Hz Frequency / Hz
40Magnitude/dBPhase /deg
20
0
200
0
40
0
-100
100
-300 Magnitude/dBPhase /deg
50
-50
0
-400
-800
30
10
-400
-200
0
Magnitude/dBPhase /degMagnitude/dBPhase /deg
Ydd Ydq
Yqd Yqq
Y(2P)
2Y(P)
Imaginary
(a) Stable baseline
-1.5 -1 -0.5 0 0.5 1
-1
-0.5
0
0.5
1
-1.5 -1 -0.5 0 0.5 1
(-1,j0)
1
0.5
0
-0.5
-1
Real
Imaginary
Real
(b) Critical baseline
5:5:0:0
5:2:1.5:1.5
10/3:10/3:10/3:0
2.5:2.5:2.5:2.5
5:5:0:0
5:2:1.5:1.5
10/3:10/3:10/3:0
2.5:2.5:2.5:2.5
(-1,j0)

 
Fig. 10. Representative plant-level dispatch map under a fixed 10 MW com-
mand 
Fig. 9 compares the MIMO Nyquist eigenvalue trajectories 
of representative power allocations under the same 10 MW 
command. For both the stable and critical baselines, the con-
centrated allocation 5:5:0:0 MW produces the trajectory closest 
to the critical po int (-1, j0). Distributing the command among 
more units moves the trajectories away from the critical point, 
while equal allocation provides the largest margin among the 
examined cases. These results show that satisfying the total 
power command and unit ca pacity limits alone does not guar-
antee adequate plant stability. 
Based on the unit-level operating regions and the plant-level 
MIMO criterion, the set of acceptable schedules is defined as: 
 
 
min max
cmd
1
min rated
sch
dc,
enc ac
min req
{0,1 }, 1, ,
,
1, , ,( , )
( , ) , with 1,
( , ) 0
,
0.2
)
,
(
k
N
k k k k k k
k
kk
k k k k
b k N
P P b P P b P
P P k NbP
P T k b
N L b P
d b P d
=
  = 

 =  
 ==
   =
=
 
=

 , (26) 
where 𝓕sch denotes the set of acceptable schedules, and N is the 
number of IGBT-AWE units. The vector b=[b1,...,bN]T contains 
the unit states. The binary variable bk=1 denotes online produc-
tion, while  bk=0 denotes the zero -power state . The vector 
P=[P1,...,PN]T contains unit power commands, and Pcmd is the 
total production command. The parameters P
min 
k  and P
max 
k  denote 
the power limits of the kth online unit. To account for the mini-
mum load imposed by the hydrogen-in-oxygen (HTO) impurity 
limit, the minimum production power is set to 20% of the rated 
unit power. The stack temperature is denoted by Tk, and 𝓕dc,k is 
its unit -level dc -port operating region. The function Nenc[.] 
gives the number of encirclements of the critical point ( -1, j0) 
by the MIMO Nyquist eigenvalue trajectories. The quantities 
dmin and dreq denote the minimum Nyquist distance and its pre-
scribed threshold, respectively. 
The plant return ratio depends on the operating state and 
power command of each unit and is expressed as: 
( )
on st
ac aceq, aceq, ac
1
( , , ) ( , ) (1 ) ( ) ( )
N
k k k k k
k
L b P s b Y P s b Y s Z s
=
= + −
, (27) 
where Y
on 
aceq,k and Y
st 
aceq,k are the equivalent ac port admittances of 
the kth unit at the production and zero -power operating points , 
respectively. The matrix Zac is the external ac network imped-
ance defined in (22). 
The minimum distance between the MIMO Nyquist eigen-
value trajectories and the critical point is: 
 
 min , ac( , ) min 1 ( , , )mmd b P L b P j  =+ , (28) 
where λm[.] denotes the mth eigenvalue of the return ratio matrix; 
and ω is the angular frequency. A schedule is accepted when all 
production units remain within their dc -port operating regions, 
the Nyquist trajectories do not encircle the critical point, and 
dmin remains above dreq. 
Fig. 10 extends the discrete comparisons in Fig. 9 to a repre-
sentative continuous  dispatch slice under the fixed 10 MW 
command. We vary the powers of Units 1 and 2 independently 
and assign the remaining power equally to Units 3 and 4: 
 
   
12
34
10 , 1,5 MW, =1,2,3,42 0kPPP P k P −= −= . (29) 
In Fig. 10 , Pk=0 represents the zero -power state , while 
1≤Pk≤5 MW denotes online production. Operating points with 
0＜Pk＜1 MW are excluded by the 20% minimum load con-
straint. The color represents dmin, and the black contour marks 
dmin=0.25. The blue dashed line denotes the Nyquist stability 
boundary determined from the encirclement condition in (26). 
Equal sharing provides the largest margin, while concentrated 
allocations reduce dmin, consistent with Fig. 9. To further exam-
ine the predicted stability boundary, four representative operat-
ing points are selected. Their power allocations ([P1, P2, P3, P4]) 
are A= [4.90, 1.70, 1.70, 1.70] MW, B= [4.40, 1.70, 1.95, 1.95] 
MW, C= [4.90, 2.90, 1.10, 1.10] MW, and D= [4.30, 3.00, 1.35, 
1.35] MW, respectively. Cases A and C are predicted to be un-
stable, whereas Cases B and D are predicted to be stable. These 
four cases are subsequently examined by plant -level HIL tests 
in Section V . The map therefore identifies schedules that satisfy 
the production command and unit power limits but provide in-
sufficient electrical stability margin. 
For larger plants, the unit -level oper ating regions can first 
eliminate infeasible operating points. Plant-level MIMO analy-
sis can then evaluate the remaining unit commitment and power 
sharing schemes, reducing the required number of frequency -
domain evaluations.  
V. HARDWARE-IN-THE-LOOP VALIDATION 
A. HIL Platform and Test Setup 
Fig. 11 shows the HIL platform used to validate the proposed 
stability-oriented operating regions and power allocation 
schemes. The power stage and the interconnected plant model 
are configured in StarSim  and executed on an MT8020 real -
time simulator with a time step of 1 μs. The simulator repro-
duces the electrical dynamics of the IGBT-AWE unit, including 
the ac -grid interface, dc -link capacitor, Buck converter, and 
AWE stack. Voltage and current signals are exchanged with the 
DSP and FPGA controller, which returns the corresponding 
pulse-width modulation (PWM) commands to the real -time 
model. This closed -loop implementation preserves the 
A
B
C
D
20% production-load boundary 
dmin=0.25 boundary
Nyquist stability boundary
  
0.55
0.5
0.45
0.4
0.35
0.3
0.25
0.2
0.15
0.1
0.05
Minimum Nyquist distance dmin​
Power of Unit 2, P2​/MW
0 1 2 3 4 5
5
4.5
4
3.5
3
2.5
2
1.5
1
0.5
0
Power of Unit 1, P1​/MW
2.5:2.5:2.5:2.5

converter control and dc -link interactions required by the sta-
bility analysis. 
B. Unit-Level Validation of the DC-Port Stability Boundary 
Fig. 1 2 confirms the normal steady -state operation of the 
IGBT-AWE unit, with sinusoidal ac voltage and current, regu-
lated dc-link voltage, and stable AWE current and stack voltage.  
The operating point is then shifted toward the dc-port stabil-
ity boundary. As shown in Fig. 13(a), sustained oscillations ap-
pear simultaneously in the dc -link voltage, AWE current, and 
stack voltage. The enlarged waveforms in Fig. 13(b) exhibit the 
same domina nt oscillatory component, and the fast Fourier 
transform (FFT)  identifies a frequency of approximately 121  
Hz. This agrees well with the critical frequency predicted by the 
dc-port admittance analysis, validating the magnitude-intersec-
tion and phase-difference criterion in Section II-C. 
Fig. 14 further verifies the parameter trends obtained in Sec-
tion III. Increasing the Buck current-loop bandwidth from 20 to 
100 Hz suppresses the oscillation, consistent with the predicted 
increase in dc-port stability marg in. In contrast, increasing the 
stack temperature from 353 to 373 K enlarges the oscillation, 
confirming the adverse effect of temperature on the stability 
boundary. The HIL results therefore reproduce the effects of 
both interface and operating parameters  identified by the fre-
quency-domain analysis. 
 
Fig. 11. HIL platform for validating the IGBT–AWE electrolysis unit 
 
Fig. 12. Steady-state HIL waveforms of one IGBT-AWE unit 
 
Fig. 13. HIL validation of the dc-port oscillation near the stability boundary 
 
Fig. 14. HIL responses under parameter variations 
 
Fig. 15. Plant-level HIL response during power redistribution from 5:5:0:0 to 
2.5:2.5:2.5:2.5 MW 
 
Fig. 16. Plant-level HIL validation of representative Cases A to D across the 
predicted stability boundary 
C. Validation of Plant-Level Power Allocation 
Fig. 15 validates the stability -oriented power allocation rule 
derived from Figs. 9 and 10. Under the initial 5:5:0:0 MW allo-
cation, Units 1 and 2 operate at rated power beyond the unit -
level dc-port stability boundary identified in Section III, while 
Units 3 and 4 remain at zero power. Sustained oscillations ap-
pear in the dc -link voltages and stack voltages of the loaded 
units, consistent with the unit-level stability prediction.  
The power command is then redistributed to 2.5:2.5:2.5:2.5 
MW. All four units consequently operate at half load, which lies 
within the stable unit operating region, while the plant -level 
MIMO analysis also predicts an increased stability margin. The 
measured dc-link oscillations decay after redistribution and the 
four units converge to stable operating points. The HIL results 
therefore confirm that power redistribution can increase the sta-
bility margin and suppress oscillations under the same total pro-
duction command. 
Fig. 16 f urther evaluates the four nonuniform schedules 
marked in Fig. 10. Cases A and C are predicted to be unstable, 
whereas Cases B and D are stable. The enlarged segments in 
Fig. 16 highlight the relatively weak oscillatory component in 
Case A, while a pronounced sustained oscillation is observed in 
Case C. After the operating point is changed from A to B and 
from C to D, the oscillations decay and the responses converge 
to stable operating points. The alternating responses of Cases A 
to D agree with the stabili ty boundary predicted in Fig. 10 and 
confirm that power allocation can change the plant-level stabil-
ity margin under the same total production command. 
Oscilloscope
Simulator
DSP+FPGA
Host 
Computer #1
Host 
Computer #2
Udc(1000V/div)
Igrid(6200A/div)
t (9.4ms/div)
Ugrid(660V/div)
Udc(1000V/div)
Iele(6200A/div)
Uele(660V/div)
t (9.4ms/div)
(a) Grid (b) AWE
Udc(100V/div)
Iele(290A/div)
Uele(50V/div)t (2s/div)
Udc(250V/div)
Iele(440A/div)
Uele(50V/div)
t (13.2ms/div) FFT
121Hz
(a) Oscillation onset (b) Zoomed waveforms and FFT
t (1s/div)
Udc(100V/div)
Iele(290A/div)
Uele(50V/div)
fbcl=20 to 100Hz
(a)Buck  bandwidth increase (b) Stack temperature increase
Udc(1280V/div)
Iele(4200A/div)
Uele(500V/div)
T=353 to 373K
t (2s/div)
Uele1(110V/div)
Uele3(250V/div)
Uele2(110V/div)
Udc4(700V/div)
5:5:0:0 to 2.5:2.5:2.5:2.5
Udc1(700V/div)
Udc2(700V/div)
Udc3(700V/div)
Uele4(250V/div)
(a)Uele (b)Udc
t (2s/div) t (2s/div)
A to B B to C C to D
Udc1(500V/div)
Udc2(500V/div)
Udc3(500V/div)
Udc4(500V/div)
t (1.8s/div)
Iele2(1500A/div)
Iele4(1500A/div)
Iele1(1500A/div)
Iele3(1500A/div)
A to B
B to C C to D
(a)Udc (b)Iele


VI. CONCLUSION 
This paper develops a stability-oriented framework that links 
the dc-port dynamics of individual IGBT-AWE units with the 
aggregated ac-port behavior of multi-ELZ ReP2H plants. The 
analytical and HIL results yield the following findings. 
1) At the unit level, higher stack temperature and heavier 
loading reduce the dc -port stability margin. Incr easing 
the dc-link capacitance and Buck current -loop band-
width improves stability. The resulting design and oper-
ating regions identify parameter combinations and oper-
ating points close to the oscillation boundary. 
2) At the plant level, the aggregated ac-port admittance de-
pends on unit commitment and power allocation. The 
same total production power can therefore produce dif-
ferent stability margins. Balanced power allocation 
among more online units generally increases the stability 
margin, whereas concentr ated allocation moves the op-
erating point closer to the plant-level stability boundary.  
3) The proposed operating and design regions translate the 
identified stability margins into practical constraints for 
interface design and production dispatch. HIL tests ver-
ify the predicted stability boundaries and confirm that 
redistributing power from low -margin or unstable allo-
cations to higher-margin allocations can suppress oscil-
lations without changing the total production command.  
Future work will integrate the proposed stability-oriented op-
eration rule into the plant EMS to coordinately optimize pro-
duction cost, startup and standby losses, degradation, and pro-
cess constraints. Large plants with heterogeneous ELZs and 
rectifiers will be addressed through hierarchi cal screening and 
reduced-order aggregation. 
APPENDIX A 
Grid voltage perturbations produce the angle deviation ∆θ, 
and linearization gives the PLL coupling matrices: 
 
u
PLL
i
PLL
d PLL q d
q PLL d q
dc dc
d PLL q d
q PLL d q
dc dc
10
0 1 0
0 0 1
00
00
000
c s s
c s s
G
c s s
c s s
G
u G U u
u G U u
uu
i G I u
i G I u
iu
    
     = −     
        
    
     = −    
       
,
d
PLL
d PLL q d
PI_PLL
q PLL d q PLL
d PI_PLL
dc dc
00
00
0 0 0
c s s
c s s
s
G
d G D u Gd G D u G s U Gdu


     − 
     =  =     +        
,
,  (A1) 
where the superscript c denotes the controller dq-frame; GPI_PLL 
= KP_PLL+ Ki_PLL/s. 
The dc-link voltage loop gives the d-axis current reference: 
 
u
dref PI_DVC d
q
dc
00
0 0 0 0
0 0 0 0
s
s
H
i G u
u
u
   
   =−     
        
,  (A2) 
where GPI_DVC = KP_DVC+ Ki_DVC/s. 
Linearizing the power balance and modulation relation yields: 
 
m1
m2
abd dc d d
abq dc q q
dc d q dc
d
q
d q dc
0.5 0 0.5
0 0.5 0.5
0.75 0.75 0
0 0 0
0 0 0
0.75 0.75 0
ss
ss
G
s
s
G
u U D d
u U D d
i I I u
i
i
D D i
    
     =     
     − −    
 
+
− − 




,  (A3) 
where the first two variables on the left of (A3) are the d and q 
components of the rectifier bridge output voltage. Capital letters 
denote steady-state quantities. In particular, Dd and Dq are the 
steady-state d and q modulation ratios. 
The ac current loop, including the dq cross-coupling terms, 
is written as: 
i
ωl
abdref d PI_ACC dref d
abqref q PI_ACC qref q
dc dc dc
0d
0q
00
00
0 0 0 0
00
00
0 0 0
c c c
c c c
H
c
G
u u G i i
u u G i i
u u i
Li
Li


        − 
       =  −  −      
        −      

+ − 

 dc
c
i




,
 (A4) 
where GPI_ACC = KP_ACC + Ki_ACC/s, and ω0 is the fundamental 
angular frequency. 
The modulation reference is normalized by the dc-link volt-
age as: 
 
m3
1
dref dc d abdref
qref dc q abqref
dc dc
0.5 0 0.5
0 0.5 0.5
0 0 1
cc
cc
G
d U D u
d U D u
uu
−
    
     =     
        
,  (A5) 
With the PWM delay Td, the duty cycle becomes: 
 
d
d
d
d dref
q qref
dc dc
00
00
0 0 1
Tssc
Tssc
G
d e d
d e d
uu
−
−
   
    =     
       
,  (A6) 
The ac filter gives the port voltage and current relation: 
 
rl1 rl2
d abd d1 2 1 2
2 1 2 1 q abq q
dc dc dc
0fff
12 2 2 2
f f 0 f f f
00
00
0 0 0 0 0 1
,( ) ( )
s s s
s s s
GG
u u iF F F F
F F F F u u i
u i i
LR sLFF R sL L R sL 
                   − − − =                     −           
+== + + +
 2 2 2
0f L






 +
,
 (A7) 
where Rf and Lf are the filter resistance and inductance, respec-
tively. 

Combining (A1) to (A7) with the rectifier power balance 
equations gives the three-port admittance matrix: 
 
IGBT-R
1 1 1 s s
rl2 Nt rl2 rl1 Mt( ) ( ) .
Y
G G G G G u i− − −+ −  =
  (A8) 
where 
 
lPLL LMt d m1 m3 i u i ω
Nt d m1 m3 i ωlm
PLL P L
2
( ( ( )) )
()
u i dG G G G H H H G G
G G G G H G
G
G
G = + + + + = + +
 (A9) 
The matrices in (A9) collect the voltage-driven and current-
driven dynamics of the IGBT -R. Equation (A8) represents the 
IGBT-R three -port admittance. The dc -link capacitor and the 
Buck-interfaced AWE stack are connected externally to the dc 
port through the dc-side admittance defined in (3).  
REFERENCES 
[1] J. Li et al., “Redesigning electrification of China’s ammonia and 
methanol industry to balance decarbonization with power system 
security,” Nat. Energy, vol. 10, pp. 762–773, Jun. 2025. 
[2] J. Li et al., “Optimal investment of electrolyzers and seasonal storages in 
hydrogen supply chains incorporated with renewable electric networks,” 
IEEE Trans. Sustain. Energy, vol. 11, no. 3, pp. 1773–1784, Jul. 2020. 
[3] S. A. Grigoriev et al., “Current status, research trends, and challenges in 
water electrolysis science and technology,” Int. J. Hydrogen Energy, vol. 
45, no. 49, pp. 26036-26058, Oct. 2020. 
[4] J. Li et al., “Coordinated planning of HVDCs and power -to-hydrogen 
supply chains for interregional renewable energy utilization,” IEEE 
Trans. Sustain. Energy, vol. 13, no. 4, pp. 1913–1929, Oct. 2022. 
[5] H. Tüysüz, “Alkaline water electrolysis for green hydrogen production,” 
Acc. Chem. Res., vol. 57, no. 4, pp. 558–567, Feb. 2024. 
[6] Y. Zhou et al., “Impacts of dynamic frequency feedback loop in SOGI-
PLL on low-frequency oscillation in an electric railway system,” IEEE 
Trans. Transp. Electrific., vol. 9, no. 3, pp. 4080–4093, Sep. 2023. 
[7] Y. Zhou et al., “Impacts of quadrature signal generation-based PLLs on 
low-frequency oscillation in an electric railway system,” IEEE Trans. 
Transp. Electrific., vol. 7, no. 4, pp. 3124–3136, Dec. 2021. 
[8] R. Qi  et al.,  “Thermal modeling and controller design of an alkaline 
electrolysis system under dynamic operating conditions,” Appl. Energy, 
vol. 332, p. 120551, Feb. 2023. 
[9] M. Agredano -Torres et al.,  “Decentralized dynamic power sharing 
control for frequency regulation using hybrid hydrogen electrolyzer 
systems,” IEEE Trans. Sustain. Energy , vol. 15, no. 3, pp. 1847 –1858, 
Jul. 2024. 
[10] L. Sanchez et al., “Comparative analysis of power converter topologies 
for hydrogen electrolyzers,” IEEE J. Emerg. Sel. Topics Power Electron., 
vol. 12, no. 5, pp. 4325–4341, Oct. 2024. 
[11] J. Zhu et al., “Exploring the optimal size of grid-forming energy storage 
in an off -grid renewable P2H system under multi -timescale energy 
management,” Appl. Energy, vol. 407, Art. no. 127295, 2026. 
[12] C. Huang  et al.,  “Grid-integrated hydrogen production systems: A 
holistic analytical modeling framework for stability assessment and 
dynamic interaction,” Int. J. Hydrogen Energy, vol. 240, Art. no. 155391, 
2026. 
[13] B. Hamad, Y. A. -R. I. Mohamed, A. Al -Durra, and E. F. El-Saadany, 
“Small-signal modeling and analysis of a grid -forming PEM hydrogen 
electrolyzer,” IEEE Open J. Power Electron., vol. 7, pp. 642–669, 2026. 
[14] China Energy Engineering, “China Energy Engineering’s Songyuan 
hydrogen industry park,” 2023. [Online] . Available: 
http://www.ceehe.ceec.net.cn/art/2023/9/26/art_59190_802.html. 
[15] Da’an Municipal People’s Government, “Da’an integrated green 
hydrogen and ammonia demonstration project: Building momentum for 
a green future,” 2024. [Online]. Available: 
http://daan.jlbc.gov.cn/daxw/ztbd/202410/t20241007_1000080.html. 
[16] Y. Zeng et al., “Optimal investment portfolio of thyristor- and IGBT-
Based electrolysis rectifiers in utility-scale renewable P2H systems,” 
IEEE Trans. Sustain. Energy, vol. 17, no. 2, pp. 740–755, Apr. 2026. 
[17] Y. Gao, X. Wang, and X. Meng, “Advanced rectifier technologies for 
electrolysis-based hydrogen production: A comparative study and real -
world applications,” Energies, vol. 18, no. 1, Art. no. 48, Jan. 2025. 
[18] J. Koponen et al., “Comparison of thyr istor and insulated -gate bipolar 
transistor-based power supply topologies in industrial water electrolysis 
applications,” J. Power Sources, vol. 491, Art. no. 229443, Apr. 2021. 
[19] X. Meng, M. Chen, M. He, X. Wang, and J. Liu, “A novel high power  
hybrid rectifier with low cost and high grid current quality for improved 
efficiency of electrolytic hydrogen production,” IEEE Trans. Power 
Electron., vol. 37, no. 4, pp. 3763–3768, Apr. 2022. 
[20] A. F. El -Hamalawy, H. E. Z. Farag, and A. Asif, “Optimal desi gn and 
technology selection for electrolyzer hydrogen plants considering 
hydrogen supply and provision of grid services,” IEEE Trans. Sustain. 
Energy, vol. 16, no. 4, pp. 2327–2343, Oct. 2025. 
[21] Y. Zeng et al., “Scheduling multiple industrial electrolyzers in renewable 
P2H systems: A coordinated active-reactive power management method,” 
IEEE Trans. Sustain. Energy, vol. 16, no. 1, pp. 201–215, Jan. 2025. 
[22] Y. Qiu, B. Zhou, T. Zang, Y. Zhou, S. Chen, R. Qi, J. Li, and J. Lin, 
“Extended load flexibility of util ity-scale P2H plants: Optimal 
production scheduling considering dynamic thermal and HTO impurity 
effects,” Renew. Energy, vol. 217, Art. no. 119198, Nov. 2023. 
[23] J. Li, B. Yang, J. Lin, F. Liu, Y. Qiu, Y. Xu, R. Qi, and Y. Song, “Two-
layer energy management strategy for grid-integrated multi-stack power-
to-hydrogen station,” Appl. Energy, vol. 367, Art. no. 123413, Aug. 2024. 
[24] A. Firdous, C. P. Barala, P. Mathuria, et al. , “Short -term operation 
flexibility in modular power to hydrogen based ammonia industries, ” 
IEEE Trans. Sustain. Energy, vol. 16, no. 1, pp. 601-612, Jan. 2025. 
[25] G. He et al., “Hydrogen supply chain planning with flexible transmission 
and storage scheduling,” IEEE Trans. Sustain. Energy, vol. 12, no. 3, pp. 
1730–1740, Jul. 2021. 
[26] Ø. Ulleberg, “Modeling of advanced alkaline electrolyzers: A system 
simulation approach,” Int. J. Hydrogen Energy, vol. 28, no. 1, pp. 21–33, 
Jan. 2003. 
[27] C. Varela, M. Mostafa, and E. Zondervan, “Modeling alkaline water 
electrolysis for power-to-x applications: A scheduling approach,” Int. J. 
Hydrogen Energy, vol. 46, no. 14, pp. 9303–9313, Feb. 2021. 
[28] Á. Iribarren et al., “Dynamic modeling of a pressurized alkaline water 
electrolyzer: A multiphysics approach,” IEEE Trans. Ind. Appl., vol. 59, 
no. 3, pp. 3741-3753, May/Jun. 2023. 
[29] D. Guilbert, S. M. Collura, and A. Scipioni, “DC/DC converter 
topologies for electrolyzers: State-of-the-art and remaining key issues,” 
Int. J. Hydrogen Energy, vol. 42, no. 38, pp. 23966-23985, Sep. 2017. 
[30] X. Guo et al.,  “Review on power electro nic converters for producing 
hydrogen from renewable energy sources,” Autom. Electr. Power Syst., 
vol. 45, no. 20, pp. 185–199, Oct. 2021. (in Chinese) 
[31] L. Harnefors, M. Bongiorno, and S. Lundberg, “Input -admittance 
calculation and shaping for controlled voltage-source converters,” IEEE 
Trans. Ind. Electron., vol. 54, no. 6, pp. 3323–3334, Dec. 2007. 
[32] J. Pedra et al., “Three-port small signal admittance-based model of VSCs 
for studies of multi-terminal HVDC hybrid AC/DC transmission grids,” 
IEEE Trans. Power Syst., vol. 36, no. 1, pp. 732–743, Jan. 2021. 
[33] H. Zong, C. Zhang, X. Cai et al ., “Three -port impedance model and 
validation of VSCs for stability analysis,” in Proc. Annu. Meeting CSEE 
Study Committee HVDC Power Electron., 2021, pp. 293–298. 
[34] W. Fang, Y. Teng, S. Zhang, et al., “Impedance modeling and stability 
analysis of electrolysis system for hydrogen production under weak grid,” 
Fuel, vol. 374, Art. no. 132403, Oct. 2024. 
[35] P. Puranen et al., “Using the nonlinearity of a PEM water electrolyzer 
cell for its dynamic model characterization,” Electrochim. Acta, vol. 507, 
Art. no. 145085, 2024. 
[36] J. Li, M. Li, M. Zhang, R. Qi, and J. Lin, “Design of a photovoltaic -to-
hydrogen system for efficiency and safety under varying conditions,” J. 
Power Sources, vol. 638, Art. no. 236487, 2025. 
[37] L. Sha, J. Lin, R. Qi, Q. Li, W. Li, R. Lin, D. Gao, H. Li, X. Li, C. Yang, 
and Y. Song, “Semi-empirical equivalent circuit model and evaluation of 
energy losses for alkaline electrolysis stack in dynamic operations,” Int. 
J. Hydrogen Energy, vol. 138, pp. 859–873, 2025. 
[38] Y. Zhou, Q. Qin, H. Luo, Y. Qiu, T. Zang, and B. Zhou, “SISO stability 
criterion derived from a three -port admittance model of train -network 
system and its applications in low-frequency oscillation analysis,” IEEE 
Trans. Transp. Electrific., vol. 10, no. 4, pp. 8263–8274, Dec. 2024.  
