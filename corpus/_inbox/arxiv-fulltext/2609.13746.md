---
source_id: "arxiv"
title: "Low-Ripple Modulation Strategy for a"
url: "https://arxiv.org/abs/2609.13746"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2609.13746. Abstract: Low-Ripple Modulation Strategy for a
Photovoltaic-Based Triple-Port Hydrogen Production
 System
Shiqi Zhang, Ziang Jiao, Jiaxin Su, Ning Wang, Zheng Li, Xiaoqiang Guo, and Changchun Hua
Accepted manuscript
DOI: https://doi.org/10.1109/TIE.2025.3639816
© 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other
uses, in any current or future media, i"
---

# Low-Ripple Modulation Strategy for a

Low-Ripple Modulation Strategy for a
Photovoltaic-Based Triple-Port Hydrogen Production
 System
Shiqi Zhang, Ziang Jiao, Jiaxin Su, Ning Wang, Zheng Li, Xiaoqiang Guo, and Changchun Hua
Accepted manuscript
DOI: https://doi.org/10.1109/TIE.2025.3639816
© 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other
uses, in any current or future media, including reprinting/republishing this material for advertising or promotional
purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works.
The following pages reproduce the authors' accepted manuscript and are not the IEEE Version of Record.


IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
  
Abstract—Among various production methods, hydrogen 
generation via electrolysis powered by renewable energy plays a 
key role in achieving large -scale green hydrogen production. The 
triple active bridge isolated DC -DC conversion system exhibits 
significant application potential in hydrogen production due to its 
advantages, such as high energy density, wide step-down ratio, and 
high reliability. However, the output current ripple at the 
hydrogen production port critically affects the efficiency of the 
electrolyzer and the hydrogen production rate. Existing studies 
have limited optimization effects on current ripple and struggle to 
achieve dynamic optimization, leading to constrained ripple 
suppression under dynamic operating conditions. To address this 
issue, this paper proposes a low-ripple modulation strategy based 
on coordinated optimization of inner and outer phase-shift angles 
for multi -port power conversion systems in renewable energy 
hydrogen production. By establishing an accurate mathematical 
model, the optimal phase -shift angle combination under minimal 
current rippl e conditions is derived. An improved differential 
evolution algorithm with adaptive parameter strategy is employed 
to achieve global optimization under dynamic conditions. 
Simulation and experimental results demonstrate that the 
proposed strategy effectively suppresses current ripple, providing 
an efficient and reliable solution for hydrogen production from 
fluctuating renewable energy sources.  
 
Index Terms —Hydrogen Production, Low -Ripple Modulation 
Strategy, Multi-port converter. 
I. INTRODUCTION 
lobal population growth and technological progress have 
led to a surge in demand for fossil fuels, but this is 
unsustainable and causes serious pollution  [1]. Renewable 
energy has become an ideal choice because of its environmental 
protection, low emissions , and continuous improvement in 
energy conversion efficiency [2]. Hydrogen energy plays a key 
role in the transition from fossil fuels to clean energy  [3]. It 
offers advantages such as diverse production methods, high 
combustion heat value [4], non-polluting combustion products, 
and energy storage capability  [5]. Water ele ctrolysis is the 
cleanest way to produce hydrogen and works well with 
renewable energy [6,7]. 
In a hydrogen production system, the triple -port DC -DC 
converter stabilizes voltage and current to enhance power 
quality and ensure efficient operation  [8-10]. It performs well 
 
 
 
under varying load conditions, especially in electrolyzer 
systems, and supports high voltage conversion, enabling 
integration with high-voltage DC buses [11,12]. 
Existing research primarily focuses on optimizing the energy 
flow, efficiency, and circuit structure of Dual Active Bridge 
(DAB) converters. A coordinated triple-phase-shift (TPS)  
control strategy has been deve loped for an isolated DAB 
converter, effectively eliminating bidirectional circulating 
current, achieving full soft -switching control, reducing current 
stress, and enhancing efficiency  [13]. To simplify traditi onal 
TPS control with three variables, an automatic TPS DAB 
converter was developed. It uses smart algorithms to track and 
predict system states, reducing power loss and improving 
efficiency [14]. Further, an optimized TPS controlled LCL -
DAB converter reduces conduction losses under zero -voltage 
switching (ZVS) [15]. 
For hydrogen production, the current ripple is a critical factor. 
Excessive current ripple can lead to unstable electrolysis 
reactions, increased energy losses, and reduced hydrogen 
production [16, 17]. Current ripple has been shown to decrease 
the hydrogen production efficiency  [18], Faraday efficiency  
[19], and lifetime of electrolyzers [20]. Its impact on hydrogen 
production efficiency is primarily reflected in changes to the 
electrolysis voltage and e lectrolysis current. Therefore, 
suppressing current ripple is particularly important for water 
electrolysis-based hydrogen production systems. 
For DAB converters,  a dual -phase-shift (DPS) control 
strategy has been proposed for isolated DAB  converters to 
effectively suppress surge current, enhance system efficiency, 
and reduce output current ripple [21]. Based on this idea, a DPS 
control method with bidirectional internal phase shift was 
developed, allowing  wider modulation range, lower reactive 
power, and reduced current ripple compared to traditional 
methods [22]. Furthermore, an extended phase -shift (EPS) -
based EPS-PT switching control technique has been introduced, 
wherein the switching process is discretized, and the internal 
and external phase-shift angles are determined according to the 
input voltage and output current levels [23]. This method offers 
rapid dynamic response under fluctuating conditions, 
suppresses voltage ripple, and improves overall power quality. 
The isolated triple -port converter is important in renewable 
hydrogen systems, offering flexible energy control a nd 
Shiqi Zhang, Graduate Student member, IEEE, Ziang Jiao, Jiaxin Su, Ning Wang 
Zheng Li, and Xiaoqiang Guo, Senior Member, IEEE, Changchun Hua, Fellow, IEEE 
Low-Ripple Modulation Strategy for a 
Photovoltaic-Based Triple-Port Hydrogen 
Production System 
G 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
improved efficiency.  However, research on output current 
ripple optimization for isolated triple -port converters remains 
limited. Existing studies have proposed an IPS modulation 
scheme for a triple active bridge (TAB) circuit to reduce ripple 
by introducing an inner phase -shift angle at the hydrogen 
production port, achieving optimal ripple suppression  [24]. 
Although this method reduces ripple, its  optimization results 
still require further improvement and are only applicable to a 
single operating point.  In actual renewable energy hydrogen 
production systems, power generation fluctuations cause the 
electrolyzer to often operate under dynamic conditi ons. As a 
result, the proposed scheme involves extensive computational 
complexity and fails to achieve continuous current ripple 
optimization under varying conditions, limiting its applicability 
in real-world scenarios. 
In order to solve the above problems , this paper proposes a 
low-ripple modulation strategy based on inner and outer phase-
shift angle optimization (IEPSM). An IEPSM strategy is 
proposed with analytical modeling to optimize the output 
current ripple at the electrolyzer port. An improved adaptive DE 
algorithm is employed to optimize the phase -shift angles, 
achieving faster convergence and higher accuracy. The 
proposed strategy adapts to continuous current ripple regulation 
under different operating conditions and has been validated 
through simu lations and experiments with a connected 
electrolyzer load model, demonstrating its effectiveness in 
practical hydrogen production applications. 
The rest of this article is structured as follows. Section II 
introduces the control principle of the TAB circuit and derives 
the output circuit expression of the hydrogen production port. 
Section III proposes an optimization algorithm for ripple 
suppression, which can achieve continuous ripple regulation 
under dynamic parameter changes. Section IV verifies the 
feasibility of the proposed method through simulation. Section 
V verifies the feasibility of the proposed method through 
experiments. Finally, Section VI summarizes the whole article. 
TABLE I 
COMPARISON OF EXISTING RESEARCH 
Ref. 
Converter 
Type 
Control Strategy Main Contribution 
Electrolyzer 
Load 
Considered 
[13] DAB 
Triple Phase Shift (TPS) control 
strategy 
Effectively eliminates bidirectional circulating current, achieves full soft-
switching, reduces current stress, and improves converter efficiency 
No 
[14] DAB 
Automated TPS DAB converter 
using intelligent algorithms to 
track and predict system states 
Reduces power losses and enhances converter efficiency No 
[15] DAB 
Optimized TPS-controlled LCL-
DAB converter based on 
Fundamental Harmonic Analysis 
Reduces conduction loss and ensures Zero Voltage Switching No 
[21] DAB Dual Phase Shift control strategy 
Suppresses surge current, enhances system efficiency, and reduces output 
current ripple 
No 
[22] DAB 
DPS method with bidirectional 
internal phase shift 
Offers wider modulation range, lower reactive power, and reduced 
current ripple compared to conventional methods 
No 
[23] DAB 
Extended Phase Shift (EPS)-based 
EPS-PT switching control 
technique 
Discretizes switching process and sets internal and external phase shift 
angles based on input voltage and output current levels 
No 
[24] TAB 
Hybrid control combining PWM 
and phase-shift in TAB circuit 
Suppresses current ripple by introducing internal phase shift at the 
hydrogen production port, achieving partial ripple optimization 
No 
The 
paper 
TAB 
IEPSM-based dynamic ripple 
optimization for electrolyzer load 
Achieves lower ripple at the hydrogen production port; dynamic ripple 
optimization validated with electrolyzer load model 
Yes 
II. OPTIMIZED CONTROL STRATEGIES FOR THE SYSTEMS 
A. Photovoltaic hydrogen production system composition 
According to the hydrogen production system design 
requirements, as shown in Fig. 1, Port 1 of the triple -port 
hydrogen production converter connects to the photovoltaic 
power generation unit, Port 2 connects to the battery, and Port 
3 connects to the elec trolyzer unit. The system consists of a 
photovoltaic module, DC bus, multi -port DC/DC converter, 
battery module, and electrolyzer module. The photovoltaic 
module has a maximum power output of 20 kW. The 
electrolyzer module adopts PEM technology and operate s at a 
rated power of 11.6 kW. In the triple-port hydrogen production 
converter, the turns ratio of the three-winding transformer is N1: 
N2: N3, and each full -bridge unit is composed of switching 
devices Sx1∼Sx4(x=a, b, c). 
The hydrogen production technology adopted in this paper is 
Proton Exchange Membrane (PEM) electrolysis. This type of 
electrolyzer offers advantages such as fast dynamic response 
and strong adaptability to the fluctuations of renewable energy 
sources, making it more suitable for water el ectrolysis driven 
by variable renewable energies like wind and solar [25]. The 
dynamic model of the PEM electrolyzer constructed in this 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
study is based on its electrochemical characteristics. Since the 
cathodic reaction proceeds much faster than the anodic reaction 
during actual operation, the model primarily f ocuses on the 
cathodic process [26].  
Fig. 2 shows the equivalent circuit model of the PE M 
electrolyzer, which consists of the following components: 1)  
Two resistors (Ra, Rc)–capacitor ( Ca, Cc) branches used to 
model the dynamic characteristics, Gibbs energy, and losses of 
the anode and cathode. 2) A resistor (Rmem) is used to represent 
the ohmic overvoltage and proton membrane losses. 3)  A DC 
voltage source (Erev) is used to simulate the reversible voltage. 
The model represents a minimum unit. The tot al power of the 
electrolyzer can be adjusted by varying the number of these 
minimum units. 
Port 1
Photovoltaic 
Module
V1
C1
A
B
UH2
L1
N1
C
E
F
Port 2
Port 3
Iin1
Da1
Sa1
Sa3 Sa4
Sa2
Da2
Da3 Da4
Sb1 Sb2
Sb4Sb3
L3
N2 Iin2
Db1 Db2
Db4Db3
D C2
V2
N3 Iin3
Sc1 Sc2
Sc4Sc3
UH3
Dc1
Dc2
Dc4Dc3
C3
V3
UH1
Battery 
Module
Electrolyzer 
Module
L2
 
Fig. 1.  Triple-Port Hydrogen Production Conversion System Topology. 
ηact,c ηohm ηact,a
+
Rc
Cc
Urev
Rmem
Ra
Ca
CATHODE
MEMBRANE
ANODE
Vcell
Icell
+
 
Fig. 2.  Equivalent Circuit Model of the PEM Electrolyzer. 
B. Equivalent circuit of photovoltaic hydrogen production 
triple-port power conversion system 
u1(t)
u'2(t)
u'3(t)
L13
L12 L23
i'12 i'32
i'13
i1
i'2
i'3
u1(t) u'2(t) u'3(t)
L1
i32
i1 i'2 i'3
L'2 L'3
 
(a) Y-type equivalent circuit     (b) Δ-type equivalent circuit 
Fig. 3.  TAB equivalent circuit diagram. 
For easier analysis, the voltages and currents of ports 2 and 3 
are referred to as port 1. The TAB circuit is simplified to a Y -
type circuit as shown i n Fig . 3(a). Here, u2 and u3 are the 
original port voltages, while u 2´  and u3´  are the converted 
voltages. Assume transformer ratios are N1: N2: N3= n1:n2:n3. 
L2´  and L3´  are the equivalent leakage inductances after 
conversion. Therefore, the calculated voltage inductance can be 
expressed as u2´= u2* n1/ n2, u3´= u3* n1/ n3, L2´= L2* n1/ n2, L3´= 
L3* n1/ n3. 
To simplify the description and calculation process, the Y-
circuit is converted to an equivalent delta circuit, as shown in 
Fig. 2(b)  [27]. Then calculate the equivalent inductances L12, 
L13, and L23 using the given formulas. 
 
12
12 1 2
3
23
23 2 3
1
13
13 1 3
2
LLL L L L
LLL L L L
LLL L L L
 = + + 
  = + +

 = + +   (1) 
C. Analysis of IEPSM Phase Shift Strategy 
t1-2
t1-3
t
t
t
u1
Sb1& Sb4 Sb2 & Sb3
Sc1 Sc3
u'2
u'3
Sc4 Sc2
Sc3
Sc2
t
t2t0 t3 t4 t5 t7 t8 t10(t0)t9
t3-3
Internal phase shift time
Internal phase shift time
u1
t1 t6
t
Sa3
Sa2
Sa1
Sa4
t
t1-1
t
t2t0 t3 t4 t5 t7 t8 t10(t0)t9t1 t6
t2t0 t3 t4 t5 t7 t8 t10(t0)t9t1 6
t2t0 t3 t4 t5 t7 t8 t10(t0)t9t1 t6
t2t0 t3 t4 t5 t7 t8 t10(t0)t9t1 t6
t2t0 t3 t4 t5 t7 t8 t10(t0)t9t1 t6
0.5Ts
 
Fig. 4.  Low ripple modulation based on IEPSM. 
Electrolyzers need a low DC voltage for hydrogen 
production, usually provided by a DC/DC step-down converter 
[28]. Current ripple can reduce hydrogen production efficiency 
[29]. Internal phase -shift modulation offers more control 
flexibility by adjusting phase shifts, helping to reduce ripple 
and improve efficiency and reliability. 
To reduce load port current ripple, this paper propo ses an 
IEPSM-based low -ripple modulation strategy. By applying 
internal phase shifts to ports 1 and 3, a three-level square wave 
voltage is generated, improving output current stability. Proper 
combinations of internal and external phase shifts help 
minimize ripple. Fig. 4 shows the port driving signals and load 
voltage under this strategy. 
Here, t1-1 and t3-3 are the phase shift time differences between 
diagonal switches at the load port.  As shown in Fig . 4, after 
introducing the internal phase shift angle  at ports 1 and 3, the 
voltage waveforms at these ports transition from the rectangular 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
square wave voltage under SPS (Single Phase Shift) control to 
a three -level AC voltage.  The energy flow modes can be 
divided into two categories: single-input dual-output and dual-
input single-output. The working principles of TAB converters 
under different power flows are very similar. This article only 
discusses the dual-input single-output mode. With port 1 as the 
main input,  Eq. (2) represents the power relationship among 
the three ports: 
 
1 1-2 1-3
2 1-2 2-3
3 1-3 2-3
( + )P P P
P P P
P P P
=−
 =−
 =+  (2) 
From Eq. (2), it can be inferred that to solve for the power 
P3 received by the load port, it is necessary to determine  P1-3 
and P2-3. Taking the solution of P1-3 as an example, the 
corresponding voltage waveforms are illustrated in Fig. 5: 
tt1t0 t2 t3 t4 t5 t6 t8 (t0)t7
u1(t)
u'3(t)t1-3 t3-3
tt2t0
t3 t4 t5
t7
t8
t10(t0)t9
i1-3(t)
U1
U'3
t1
t6
t9 t10
t1-1
 
Fig. 5.  1-port and 3-port voltage waveforms. 
Based on the equivalent circuit in Fig. 3(b), the relationship 
between ports 1 and 3 is given by Eq. (3): 
 
13
13 1 3
LdiL u udt =−   (3) 
By integrating the current between ports 1 and 3 over a full 
cycle, Eq. (4) gives the average current expression for both 
ports: 
 
13
13 13 1 3
13
1( ) ( ) LL dii t L u u dt dt L = = −    (4) 
Under steady -state conditions, the output current and port 
voltages vary periodically. Within the half-cycle from 0 to T/2, 
the maximum and minimum values of the waveform are equal 
in magnitude but opposite in sign, as described by Eq. (5). 
 
( ) ( / 2)f t f t T= − +   (5) 
Over the full period from 0 to T, the signal values repeat 
every T interval, which is expressed accordingly in the 
following equation. 
 
( ) ( )f t f t T=+   (6) 
Without considering system  losses, that is, assuming the 
input power equals the output power, P1−3 is given by Eq. (7): 
 
/2
1 3 1 13 0
1 ( ) ( )0.5 T LP u t i t dtT− =    (7) 
 
213
1 3 1 3 1 3 1 1 1 1 1 3
13
22
1 1 3 3 1 3 3 3 1 1 3 3 3 3
( 2 0.5 2
0.5 2 )
uuP Tt t Tt t tLT
t Tt t t t t t
− − − − − −
− − − − − − −
= − − + + −
+ − + − +   (8) 
Similarly, the power expression is transferred from port 2 to 
port 3, and the output current of the load port can be obtained. 
 
2223
2-3 2-3 2-3 3-3 2-3 3-3 3-3
23
( 2 +0.5 2 )UUP Tt t Tt t t tLT= − − −   (9) 
According to the power flow, the output current of port 3 can 
be solved using Eq. (10).  
22
1-3 2-3 2 2-3 2-3 3-3 2-3 3-3 3-3
out
3 23
22
1 1 3 1 1 3 3 1 1 1 3 1 3 3 3 1 1 3 3
13
( 2 0.5 2 )
( ( ) ( ) 0.5 ( ))
P P u Tt t Tt t t tI U L T
u Tt t t t t t t T t t
LT
− − − − − − − − −
+ − + − −= = +
+ − − − + − −
(10) 
The load’s DC output is rectified from the hydrogen port, so 
the transformer’s current waveform directly affects output 
quality. Therefore, suppressing the peak current at the 
transformer's hydrogen production port can effectively reduce 
the output current ripple. Under the IEPSM modulation strategy, 
the output voltage at the load port is a three -level high -
frequency AC voltage, and the spe cific equivalent circuit is 
shown in Fig. 3(b). Port current i'3 is influenced by  u1(t), u'2(t) 
and u'3(t), and can be expressed as Eq. (11): 
 
1 3 3 2
3 1-3 3-2
13 23
( ) ( ) ( ) ( )u t u t u t u ti i i LL   −−  = − = −   (11) 
TABLE Ⅱ 
CURRENT WAVEFORM AT THE LOAD PORT WITHIN HALF A CYCLE 
Current waveform Current expression Time period 
I3
t
t2
t0 t3 t4 t5 t6 t9t8 (t0)t7t1 t10
 
3 3 2
3 1 1 0 0
13 23
( ) ( )( )u u ui t t t i LL  −+ = − − +
 t0~t1 
I3
t
t2
t0 t3 t4 t5 t6 t9t8 (t0)t7t1 t10
 
1 3 3 2
3 2 2 1 1
13 23
( ) ( )( )u u u ui t t t i LL   + − + = − − +
 t1~t2 
I3
t
t2
t0 t3 t4 t5 t6 t9t8 (t0)t7t1 t10
 
1 3 3 2
3 3 3 2 2
13 23
( ) ( )( )u u u ui t t t i LL   + − − = − − +
 t2~t3 
I3
t
t2
t0 t3 t4 t5 t6 t9t8 (t0)t7t1 t10
 
12
3 4 4 3 3
13 23
( ) ( )( )uui t t t i LL  = + − +
 t3~t4 
I3
t
t2
t0 t3 t4 t5 t6 t9t8 (t0)t7t1 t10
 
1 3 3 2
3 5 5 4 4
13 23
( ) ( )( )u u u ui t t t i LL   −− = − − +
 t4~t5 
Table Ⅱ shows the load port current over one cycle. The 
maximum current occurs at time points t0 and t5. To find its 
expression, an iterative method is used to calculate the current 
at t5. Current segments from  t0 to t5 follow the relationships in 
Table Ⅱ and satisfy Eq. (12). 
 
3 0 3 5( ) ( )i t i t =−   (12) 
Each time period and the relationship between phase shift 
times satisfy Eq. (13). 
Using Eq. (12), Eq. (13) along with Table Ⅱ, the load port 
current waveform over one cycle is obtained. The peak current 
occurs at t0 and t5, when the absolute value of the load current 
is the largest. This paper uses an iterative method to derive the 
formula for peak current. The current relationships for each 
time segment t0 to t5 of i'3 are shown in Table Ⅱ: 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
 
1 0 1-1
2 1 1-2 1-1
3 2 1-3 1-2 2 3
4 3 3-3
5 4 1-3 3-3
-
0.5
t t t
t t t t
t t t t t
t t t
t t T t t
−
−=
 −= − = − =
 −=
 − = − −   (13) 
1 1 1 1 1 3 3 3 3 3 3
30
13
2 1 2 2 1 3 3 3 3 3 3
23
0.25 0.5 0.5 0.25()
0.25 0.5 0.25
Tu t u t u t u Tuit L
Tu t u t u t u Tu
L
− − −
− − −
  − + + − =−
    − + + −−
 (14) 
Then, by substituting it into the expression for i'3(t5), the peak 
current expression for the load port i'3(peak) can be obtained. 
 
1 1 1 1 1 3 3 3 3 3 3
3( )
13
2 1 2 2 1 3 3 3 3 3 3
23
0.25 0.5 0.5 0.25
0.25 0.5 0.25
peak
Tu t u t u t u Tui L
Tu t u t u t u Tu
L
− − −
− − −
  − + + − =
    − + + −+ (15) 
The phase shift time t1-2 of ports 1 and 2 is fixed to 12μs, and 
the influence of the phase shift time t1-1, t1-3, and t3-3 on i'3(peak) 
is analyzed.  
0
5
1
4
2
10
-5
1
3
10
-5
3
10
-5
4
0.52
1 0
300
350
400
450
500
550
Peak Output Current of Transformer Port 3 IPeak
1 port in-port 
phase shift t1-1/s
1, 3-port external 
phase shift t1-3/s
3-port in-phase shift t3-3/s
 
Fig. 6. Internal and external phase shift angles for 100 A output current. 
0
5
0.5
1
4
1.5
10
-5
1
2
10
-5
3
2.5
10
-5
3
0.52
1 0
300
350
400
450
500
550
Peak Output Current of Transformer Port 3 IPeak
1 port in-port 
phase shift t1-1/s
1, 3-port external 
phase shift t1-3/s
3-port in-phase shift t3-3/s
 
Fig. 7. Internal and external phase shift angles for 150 A output current. 
Figs. 6, 7, and 8 show how the peak current at port 3 changes 
at 100A, 150A, and 200A output settings. The diagram 
illustrates the impact of different ph ase-shift angle 
combinations on i'3(peak), highlighting the strong correlation 
between modulation parameters and ripple behavior. It provides 
intuitive insight into how coordinated phase adjustment affects 
current ripple. For each scenario, the three phase shift variables 
t1-1, t1-3, and t3-3 are evenly sampled within the range [0,  T/2], 
with 500 3 points in total across the three dimensions. The 
corresponding peak current is calculated for each parameter 
combination. The X-axis represents the internal phase shift time 
t1-1 at port 1, the Y-axis represents the external phase shift time 
t1-3 between port 1 and port 3, and the Z -axis represents the 
internal phase shift time t3-3 at port 3 . The color scale reflects 
the mag nitude of the peak current, with hues closer to blue 
denoting lower peak current values, and those nearer to yellow 
indicating higher peak current levels. 
0
4
0.5
1
10
-5
3 1
1.5
10
-5
10
-5
2
2 0.5
1 0
350
400
450
500
550
Peak Output Current of Transformer Port 3 IPeak
1 port in-port 
phase shift t1-1/s
1, 3-port external 
phase shift t1-3/s
3-port in-phase shift t3-3/s
 
Fig. 8. Internal and external phase shift angles for 200 A output current. 
III. ADAPTIVE DIFFERENTIAL EVOLUTION FOR OPTIMAL 
PHASE-SHIFT ANGLE COMBINATION 
To minimize the output current ripple of port 3, an improved 
DE algorithm with adaptive parameters is proposed to optimize 
the phase shift angles and minimize Ipeak, as shown in Fig. 9. 
Differential Evolution (DE) is a population -based stochastic 
search method [30,31]. Similar to all other evolutionary 
algorithms (EA), DE utilizes mutation, crossover, and selection 
operators in each generation to achieve global optimization,  
making it one of the most efficient EA currently in use [32].  
Since the initial population selection is random and global, 
the DE algorithm reduces reliance on initial values. However, 
when the objective function has multiple extreme values, it is 
easy to fall into a local optimum, and the solution fluctuate s 
widely, which is a limitation of the DE algorithm. To address 
the DE algorithm has large solution fluctuations and is easy to 
fall into local optimality in TAB phase shift angle optimization, 
this paper proposes a fusion strategy that combines the elite 
retention mechanism with the strengthening constraint 
mechanism to suppress the fluctuation range of the solution, 
and introduces an adaptive parameter strategy to enhance the 
algorithm's ability to jump out of the local optimality. 
To minimize the output current ripple at port 3 in the TAB 
circuit, this paper employs a differential evolution algorithm for 
optimization. The objective function is to minimize the peak 
value of the output port current, as expressed in Eq. (16). The 
constraints include power balance and constant output current, 
as represented in Eq. (17). 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
Step 1: Data Collection
Circuit parameters:
u1,u2,u3,L1,L2,L3,T
Determine the objective 
function:
obj=min(ipeak(t1-1,t1-3,t3-3))
Identify the constraints:
t1-1<t1-3
Iout(t1-1,t1-3,t3-3)
Step 2: Improved DE algorithm optimization process 
based on adaptive parameter strategy
( ) ( )
i
i
0 2 0 2 0 1 if rand 0 1 0 1
 otherwise
. . rand , , , .NF F,+  = 
Initialize DE parameters Initialize the population Xi
( ) ( )
i
i
0 8 0 2 0 1 if rand 0 1 0 1
 otherwise
. . rand , , , .NCR CR ,+  = 
Parameter 
adaptive 
strategy
( ) ( ) ( ) ( )e_
2
peak primi objective t constra int =  +   
( )1 k 2 Best 3 r1 r2V a X a X a X X=  +  +  −
t1-1,t1-3,t3-3are the three dimensional parameters of the 
global optimal solution
Crossover and 
mutation
Dynamic punishment and survival of the fittest
Global neighborhood
Generate new 
individuals
Step 3: Optimization Result 
Analysis
Calculate the circuit parameters 
of the equivalent circuit
I1out and Ipeak
Improved DE algorithm 
based on adaptive parameter 
strategy seeks the minimum 
current ripple of the internal 
and external phase shift 
angle combination
L13
L12 L23
i'1-2 i'3-2
i'1-3
i1
i'2
i'3
u1(t)
u'2(t)
u'3(t)
100A 125A 150A 175A 200A100
150
200
250
300
350
400
450
500
550
600
Particle Swarm Optimization
Genetic Algorithm
Conventional Differential
Evolutionary Algorithms
Improved Differential 
Evolutionary Algorithm
Electrolyzer module peak current
Electrolyzer module output current
Iterations
100A 125A 150A 175A 200A0
50
100
150
200
250
300
350
400
450
500
550 Improved DE algorithm based on adaptive parameters
Traditional DE Algorithm
Genetic Algorithms
Particle Swarm
Optimization
Electrolyzer module output current
 
Fig. 9.  Improved differential evolution algorithm with adaptive parameters for ripple optimization.
 
( )peak 1 1 1 3 3 3min  , ,objective i t t t − − −=   (16) 
 
out
in out loss
constant va
0
lue
PP
I
P
 =
− − =
   (17) 
Here, 𝐼peak denotes the peak transformer current at the 
hydrogen production port. 
A. Improved differential evolution algorithm 
Elite retention prevents the loss of high -quality solutions 
during the iteration process by retaining the historical optimal 
solution. However, excessive reliance on elites may lead to a 
decline in population diversity. This paper combines the elite 
retention strategy with a global neighborhood search strategy to 
avoid the algorithm falling into a specific local optimum while 
ensuring that the op timization direction does not deviate from 
the global optimum. 
To address the TAB power balance constraint Pin-Pout-Ploss=0, 
traditional static penalty function methods require manual 
adjustment of weight coefficients, which can easily lead to 
over-penalization or under -penalization. This paper adopts a 
dynamic penalty function, dynamically integrating the degree 
of constraint violation into the objective function: 
 
( ) ( ) ( ) ( )e_
2
peak primi objective t constraint   = +    (18) 
Among them, λ(t) increases as the iteration count t grows. 
 
( )
max
0
t
Tte =   (19) 
The initial penalty coefficient λ₀ is set to 10³ to allow flexible 
exploration in early iterations, while the final value λ(Tₘₐₓ) = 
10⁶ enforces strict constraint satisfaction at convergence. These 
values are chosen based on empirical tuning and reflect a 
gradual shift from exploration to exploitation  [33]. The 
dynamic adjustment mechanism allows for some constraint 
violations in the early stages to explore the global space, while 
enforcing strict constraint satisfaction in the later stages. 
The power balance constraint of the TAB exhibits strong 
nonlinear characteristics. The dynamic penalty function 
prevents the algorithm fro m falling into infeasible regions due 
to strict constraints in the early stages, while ensuring the 
engineering feasibility of the final solution. 
B. Parameter Adaptation Strategy 
The performance of the DE algorithm is significantly 
influenced by the scaling factor F and the crossover probability 
CR [34]. The scaling factor Fi and crossover probability CRi are 
key param eters in the adaptive DE algorithm. Fi controls the 
mutation amplitude and thus influences the exploration range, 
while CRi determines the recombination rate and affects 
population diversity. To avoid premature convergence, both 
parameters are probabilistically regenerated in each generation. 
Only successful updates are retained, allowing effective 
parameter values to be adaptively preserved throughout the 
optimization process [35]. To ensure that the algorithm exhibits 
strong adaptability and convergence when dealing with 
complex objective functions featuring multiple extrema, this 
paper adopts a global neighborhood search -based adaptive 
differential evolution algorithm. The algorithm adj usts 
parameters automatically and uses global search to improve 
individual quality toward the optimum. The adaptive parameter 
mechanism dynamically balances exploration and exploitation, 
avoiding the limitations imposed by global parameters on 
population diversity and reducing solution fluctuations. 
In the global neighborhood search -based adaptive 
differential evolution algorithm, each individual i in every 
generation has independent Fi and CRi. For individual i in the 
nth generation population, the scaling  factor is Fi, and the 
crossover probability is CRi. NFi and NCRi are the scaling factor 
and crossover probability of the trial individual Ui. For the nth 
generation, NFi and NCRi are modified as follows: 
 
( ) ( )
i
i
0.2 0.2 0,1 , if rand 0,1 0.1
, otherwise
randNF F+  =    (20) 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
 
( ) ( )
i
i
0.8 0.2 0,1 , if rand 0,1 0.1
, otherwise
randNCR CR+  =   (21) 
Eq. (20)regenerates Fi with a 10% probability, ensuring that 
Fi is distributed within 0.2, 0.4, thereby enhancing local 
exploitation capabilities. Eq. (21) regenerates CRi with a 10% 
probability, ensuring that CRi is distributed within 0.8, 1.0, 
thereby improving global exploration efficiency. The modified 
NFi and NCRi are used to generate the trial individual for the ith 
individual in the tth generation population. The updated values 
Finext and CRinext for the ith individual in the (n+1)th generation 
population are modified as follows: 
 
( ) ( )i i i
inext
i
, if   superior to 
, otherwise
NF fit U fit XF
F
=    (22) 
 
( ) ( )i i i
inext
i
, if   superior to 
, otherwise
NCR fit U fit XCR
CR
=    (23) 
The fit(X) denotes the fitness evaluation of individual X. It is 
calculated as the sum of the objective function and the dynamic 
penalty term associated with constraint violation. This value is 
used to assess the quality of an individual solution in the 
population. The Differential Evolution algorithm compares the 
fitness of the trial and current individuals. If t he trial 
individual's fitness is higher, it replaces the current individual, 
improving population fitness and advancing the optimization. 
The values of Fi and CRi are updated only when the generated 
trial solution is superior to the original solution, ther eby 
retaining successful parameter combinations. 
To address the issue of slow convergence in DE, this paper 
adopts a global neighborhood search strategy to accelerate 
convergence. This strategy generates new solutions by 
hybridizing the current optimal sol ution with random 
individuals, which are then compared with the original 
individuals to select the best for survival. 
Let Xk be an individual randomly selected from the nth 
generation population, XBest represent the most excellent 
individual in the current population, and Xr1 and Xr2 denote two 
individuals randomly chosen from the current population that 
are different from Xk. By applying the global neighborhood 
search strategy, a new individual V is obtained as follows: 
 
( )1 k 2 Best 3 r1 r2V a X a X a X X=  +  +  −   (24) 
In Eq. (24), a1, a2, and a3 are three random numbers between 
0 and 1, satisfying the constraint a1 + a2 + a3 = 1. After creating 
the new individual V, a selection operation is performed: if 
individual V is superior to individual Xk, then V replaces Xk; 
otherwise, V is discarded. 
The global neighborhood search -based adaptive differential 
evolution algorithm enhances its performance by integrating the 
global neighborhood search strategy. This strategy utilizes the 
information of the current optimal solution to guide the search 
direction, significantly improving local exploitation capabilities. 
Meanwhile, the random difference vector prevents premature 
convergence, making it suitable for complex optimization 
scenarios in TAB multi-port transmission. 
IV. SIMULATION VERIFICATION 
According to the proposed IEPSM strategy, simulations are 
conducted under three different operating conditions to observe 
the current ripple of the system under both the optimal phase 
shift strategy and the existing ripple optimization control  
scheme at the same output power. The parameters are shown in 
Table Ⅲ. This study conducted verification in a dual -input 
single-output configuration, comparing three strategies —SPS, 
IPS [24], and the proposed IEPSM —under three different 
output current settings to evaluate their performance in 
suppressing output current ripple. 
TABLE Ⅲ 
TRIPLE ACTIVE BRIDGE SYSTEM PARAMETER 
Parameter name Specific values 
Switching cycle T 100μs 
Port 1 voltage amplitude U1 144V 
Port 2 voltage amplitude U2 50V 
1-port inductance L1 8μH 
2-port inductance value L2 8μH 
3-port inductance L3 1μH 
Erev 4.38V 
Ra 0.035 Ω 
Rmem 0.088 Ω 
Ca 37.26 F 
Cc 37.26 F 
0.0998 0.0999 0.1 0.1001
Output Current (A)
90
100
110
120
Peak-to-peak current IP-P=15.7A
IP-P/IRMS =20.2%
0.0998 0.0999 0.1 0.1001
90
100
110
120
Peak-to-peak current IP-P=14.2A
IP-P/IRMS =18.2%
0.0998 0.0999 0.1 0.1001
90
100
110
120
Peak-to-peak current IP-P=7.6A
IP-P/IRMS  =10.9%
SPS IPS IEPSM
 
Fig. 10.  Output current ripple under SPS, IPS, and IEPSM (Iout=100A). 
0.0998 0.0999 0.1 0.1001
140
150
160
Peak-to-peak current IP-P=5.8A
IP-P/IRMS =5.3%
0.0998 0.0999 0.1 0.1001
140
150
160
Peak-to-peak current IP-P=9.6A
IP-P/IRMS =8.7%
0.0998 0.0999 0.1 0.1001
140
150
160
Peak-to-peak current IP-P=15.5A
IP-P/IRMS =13.6%
Output Current (A)
SPS IPS IEPSM
 
Fig. 11.  Output current ripple under SPS, IPS, and IEPSM (Iout=150A). 
0.0998 0.0999 0.1 0.1001
190
200
210Output Current (A)
Peak-to-peak current IP-P=14.2A
IP-P/IRMS =9.6%
0.0998 0.0999 0.1 0.1001
190
200
210
Peak-to-peak current IP-P=5.4A
IP-P/IRMS =3.8%
0.0998 0.0999 0.1 0.1001
190
200
210
Peak-to-peak current IP-P=4.86A
IP-P/IRMS =3.4%
SPS IPS IEPSM
 
Fig. 12.  Output current ripple under SPS, IPS, and IEPSM (Iout=200A). 
Figs. 10, 11, and 12 respectively show the comparison results 
of three different output current ripple suppression strategies 
when the output current is set to 100 A, 150 A, and 200 A. 
Taking 100 A as an example, the modulation strategies from 
left to right are SPS, IPS, and IEPSM. The output current ripple 
of the SPS strategy is 15. 7 A, with a ripple rate of 15. 7%; the 
output current ripple of the IPS strategy is 14.2 A, with a ripple 
rate of 14. 2%; and the output  current ripple of the IEPSM 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
strategy is 7. 1 A, with a ripple rate of 7. 1%. Furthermore, as 
shown in Figs. 10 and 11, the IEPSM strategy effectively 
suppresses the current ripple under different loads and achieves 
better performance than the traditional SPS and IPS strategies. 
Peak-to-peakcurrent IP-P=7.6A
IP-P/IRMS =10.9%
Output Current (A)
0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45
Time (s)
0
50
100
150
200
250
300
350
400
0.19995 0.2 0.20005140
145
150
155
160
0.39995 0.4 0.40005190
195
200
205
210
Peak-to-peakcurrent IP-P=5.7A
IP-P/IRMS =5.1%
Peak-to-peakcurrent IP-P=4.87A
IP-P/IRMS =3.3%
0.09995 0.1 0.10005
90
100
110
120
 
Fig. 13.  Current ripple optimization under different output current conditions 
(Iout=100/150/200A). 
The system sets the output current starting from 100A and 
increasing to 150A and 200A every 0.15 seconds. The 
experimental results demonstrate that IEPSM dynamically 
reduces ripple under changing electrolyzer loads . As shown in 
Fig. 13, the waveform quickly adapts to changes and matches 
the steady -state performance, verifying the dynamic response 
capability of the IEPSM strategy. 
V. EXPERIMENTAL RESULTS 
In order to verify the IEPSM strategy proposed in this paper, 
an experimental verification is carried out.  In this work, a 
hardware-in-the-loop (HiL) platform for the triple -port TAB 
system was developed using the OP5707 real-time simulator on 
the RT -LAB platform. Port 3's load is modeled as a PEM 
electrolyzer. The experimental platform is shown in Fig. 14, 
and the platform parameters are shown in Table Ⅲ. 
Figs. 15 and 16 present the comparison r esults of different 
strategies under varying output current conditions. CH 1 
represents the input voltage u1 at port 1, CH2 denotes the output 
voltage uout, CH 3 indicates the output current Iout, and CH 4 
shows the output current I3 at port 3. 
Computer
Oscilloscope
RT-LAB
Controller
Computer CPU AO
DI
AD
Drive 
Signal
DSP/FPGA
RT-LAB Controller
Circuit
AO
DI
 
Fig.14: Experimental platform. 
In the offline stage, experimental data of key variables 
(voltage, current, and load conditions) is collected to train the 
DE algorithm and obtain optimal hyperparameters, which are 
embedded into t he FPGA and DSP controller. In the online 
stage, real -time parameters such as Iₒᵤₜ are acquired, filtered, 
and processed to calculate the minimum Iₚₑₐₖ and corresponding 
phase-shift angles, which are dynamically adjusted to achieve 
continuous current ripple suppression. 
As shown in Fig. 15(a), the input voltage at port 1 is 144V, 
the output current is 150A, and the peak inductor current at port 
3 is 600A. Theoretical calculations and experimental results 
indicate that at the same set output current level, d ifferent 
strategies yield different current peaks, and the current ripple 
varies accordingly. In Fig. 15(d), the peak -to-peak output 
current is 16.4A; in Fig. 15(e), it is 9.6A; and in Fig. 15(f), it is 
around 5.8A. The experimental results show that under  the 
IEPSM strategy, the peak -to-peak value decreases to 3 5.4% of 
that observed under the SPS strategy and to 60. 4% of that 
observed under the IPS strategy. 
Fig. 16 presents the experimental waveforms for an output 
current of 200A. In Fig. 16(d), the peak -to-peak output current 
is 15.1A. In Fig. 16(e), the peak-to-peak output current is 6.2A, 
while in Fig. 16(f), it is 4.86A. 
u1
Iout
uout
I3
u1
Iout
uout
I3
u1
Iout
uout
I3
 
  (a)                                        (b)                                         (c)                                                               
u1
Iout
uout
I3
u1
Iout
uout
I3
u1
Iout
uout
I3
 
  (d)                                          (e)                                         (f)  
Fig. 15.  Comparison of output current waveforms under different phase-shift strategies (Iout = 150 A). (a) SPS strategy. (b) IPS strategy. (c) IEPSM strategy. (d) 
SPS strategy (enlarged). (e) IPS strategy (enlarged). (f) IEPSM strategy (enlarged). 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
u1
Iout
uout
I3
u1
Iout
uout
I3
u1
Iout
uout
I3
 
  (a)                                         (b)                                          (c) 
u1
Iout
uout
I3
u1
Iout
uout
I3
u1
Iout
uout
I3
 
  (d)                                         (e)                                          (f) 
Fig. 16.  Comparison of output current waveforms under different phase-shift strategies (Iout = 200 A). (a) SPS strategy. (b) IPS strategy. (c) IEPSM strategy. (d) 
SPS strategy (enlarged). (e) IPS strategy (enlarged). (f) IEPSM strategy (enlarged).
u1
uout
I3
Iout
Ipeak=289A
 Ipeak=312A
 Ipeak=352A
 
Fig. 17.  Continuous dynamic response of the system under different output 
current levels (Iout = 100A, 150A, 200A). 
The experimental results in Figs. 15 and 16 demonstrate that 
the proposed IEPSM strategy in this paper can meet the 
system's o utput requirements. Compared to the SPS and IPS 
strategies, the output current ripple has been optimized. In the 
photoelectrochemical hydrogen production system, the 
proposed scheme can improve hydrogen production efficiency 
by reducing current ripple. 
Fig. 17 shows the variation of the output current as the set 
value changes from 100A to 150A and then to 200A, simulating 
the fluctuation of the electrolyzer load.  By dynamically 
optimizing with the improved differential evolution algorithm 
using adaptive par ameters, the optimal phase -shift angle 
combination is rapidly obtained.  The output current ripple is 
dynamically optimized to the minimum value at different 
operating points. This verifies the dynamic performance of the 
proposed IEPSM strategy. 
TABLE Ⅳ 
ALGORITHM PARAMETERS 
Objective Function Minimum Ipeak value for a given Iout 
Population size 500 
Maximum number of iterations 500 
Initial zoom factor range 0.6-1 
Initial crossover probability range 0.8-1 
This paper compares the improved DE algorithm, the 
traditional DE algorithm, the Genetic Algorithm (GA), and 
Particle Swarm Optimization (PSO) under the IEPSM strategy. 
To ensure a fair comparison, the circuit parameters, population 
size, and maximum iteration count are kept consistent across all 
four algorithms. 
Following the flowchart shown in Fig. 9, this paper employs 
an improved differential evolution algorithm based on an 
adaptive parameter strategy to search for the optimal phase shift 
combination under the IEPSM strategy. The key para meters of 
the algorithm are listed in TABLE Ⅳ. Based on the 
optimization results shown in Fig. 18, it can be observed that 
under different electrolyzer load conditions, the improved DE 
algorithm exhibits superior stability compared to the other three 
optimization algorithms, including PSO, GA, and the 
conventional DE algorithm. The peak current optimization 
results of the triple -port system obtained by the improved DE 
algorithm are consistently better, demonstrating its 
effectiveness in minimizing current p eaks under various load 
conditions. 
100A 125A 150A 175A 200A100
150
200
250
300
350
400
450
500
550
600
Particle Swarm Optimization
Genetic Algorithm
Conventional Differential
Evolutionary Algorithms
Improved Differential 
Evolutionary Algorithm
Electrolyzer module peak current
Electrolyzer module output current
 
Fig. 18.  The peak current under different optimization algorithms ( Iout=100, 
125, 150, 175, 200A). 
As illustrated in Fig. 1 9, the comparison of output current 
ripple under different optimization strategies (SPS, IPS and 
IEPSM) shows that the IEPSM strategy can significantly reduce 
the current ripple. When the output current is 200A, the ripple 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
is reduced by 6 7.8% compared with the SPS strategy and by 
21.6% compared with the IPS strategy. 
100A 150A 200A
Electrolyzer module output current
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
20Electrolyzer module output ripple
SPS Strategy
IPS Strategy
IEPSM Strategy
 
Fig. 19.  Comparison of output current ripple magnitude under different 
modulation strategies. 
Iterations
100A 125A 150A 175A 200A0
50
100
150
200
250
300
350
400
450
500
550 Improved DE algorithm based on adaptive parameters
Traditional DE Algorithm
Genetic Algorithms
Particle Swarm
Optimization
Electrolyzer module output current
 
Fig. 20.  Comparison of iteration counts under different optimization 
algorithms. 
As shown in Fig. 20, when the Electrolyzer module  output 
current is 100A and 125A, the improved DE algorithm and the 
PSO algorithm exhibit similar iteration counts. However, the 
peak current of the improved DE algorithm achieves 
approximately 2 80A when the Electrolyzer module  output 
current is 100A and 295A when the Electrolyzer module output 
current is 125A. Compared with the PSO algorithm, the peak 
current of the improved DE algorithm is reduced by 45.1% and 
43.3% respectively. In contrast, the genetic algorithm and the 
traditional DE algorithm require more iterations  and result in 
higher peak currents. When the Electrolyzer module  output 
current is 150A, 175A, and 200A, the improved DE algorithm 
and the PSO algorithm yield phase -shift combinations with 
similar peak currents, but the improved DE algorithm 
converges fas ter with fewer iterations. The reduction in the 
number of iterations directly benefits real -time control 
applications by lowering the online computation cost and 
accelerating the system response. Again, the genetic algorithm 
and the traditional DE algorith m demonstrate higher iteration 
counts and larger peak currents. Across the Electrolyzer module 
output current range from 100A to 200A, the improved DE 
algorithm consistently requires fewer iterations and calculates 
phase-shift combinations with smaller peak currents, validating 
the effectiveness of the proposed algorithm. From Fig. 2 1, it is 
evident that the application of the global neighborhood search 
strategy accelerates convergence, while the adaptive parameter 
control and elite retention strategies enh ance the algorithm's 
exploitation capability, enabling it to seek global optimal 
solutions. 
100A 150A 200A
Electrolyzer module output current
54
56
58
60
62
64
66
68
Current strategy
Proposed strategy
H2 production efficiency (%)
 
Fig. 21. Comparison of hydrogen production efficiency between the existing 
strategy and the proposed strategy. 
This paper conducts a qu antitative analysis of the 
electrolyzer efficiency. The hydrogen production efficiency 
model of the electrolyzer is expressed as: 
 
22
el
el
HH LHV LHV
UI
nn
P

==

   (25) 
 
rev ohm actU U U U++=   (26) 
where nH2 represents the hydrogen production rate, LHV is 
the lower heating value of hydrogen, and Pel is the power 
consumption of the electrolyzer. The electrolyzer voltage U is 
composed of three parts: the reversible voltage Urev, the ohmic 
overvoltage Uohm, and the activation overvoltage  Uact. The 
electrolysis current is denoted as I. However, this model does 
not consider the influence of current ripple, which may affect 
the performance and durability of the system under fluctuating 
operating conditions.  
Current ripple leads to an increase in both ohmic losses a nd 
activation losses. It also increases the effective value of the 
electrolysis current[18, 19]. Therefore, the hydrogen production 
efficiency is calculated as follows:  
 
( )
2
2
re
el r
v
ipp
a
le
ct
2
ohm
H
DC AC
LHV
U U U
n
II

+ +

+
=，   (27) 
Therefore, based on Eq. (27) , and referring to the PEM 
electrolyzer efficiency model [36], combined with the 
experimental results shown in Fig. 19, the hydrogen production 
efficiency of the electrolyzer is obtained and illustrated. As 
shown in Fig. 21, the current strategy is implemented based on 
the SPS method. 

IEEE TRANSACTIONS ON INDUSTRIAL ELECTRONICS  
 
VI. CONCLUSION 
This paper presented a low-ripple modulation strategy based 
on inner and outer phase -shift angle optimization (IEPSM) for 
a photovoltaic -based triple -port hydrogen production system . 
The proposed method was thoroughly analyzed and validated. 
The major contributions are summarized as follows: 
1) IEPSM Strategy and Analytical Modeling: We introduced 
the IEPSM strategy to increase the system’s control flexibility 
by independently adjusting inner and outer phase shifts. 
Analytical expressions for the hydrogen production port’s 
output current and its peak value under IEPSM were derived, 
providing a precise basis for predicting and minimizing current 
ripple. 
2) Improved DE Algorithm for Optimization: A precise 
mathematical model of the triple-port converter was developed, 
and an improved Differential Evolution (DE) algorithm with an 
adaptive parameter strategy was implemented to optimize the 
phase-shift angles. This enhanced DE algorithm significantly 
accelerates convergence and improves computational accuracy. 
In our simulations, it c onsistently required fewer iterations (up 
to about 30 –40% fewer at higher load currents) to find the 
global optimum compared to the standard DE and genetic 
algorithm, while achieving lower peak currents. 
3) Simulation and Experimental Validation of Ripple 
Reduction: Extensive simulation and experimental results 
demonstrate that the proposed IEPSM scheme achieves 
superior ripple reduction compared to conventional single -
phase shift (SPS) and inner -phase shift (IPS) strategies. For 
example, at a 150  A output,  the IEPSM strategy reduced the 
peak-to-peak output current ripple from approximately 1 6.4 A 
(under SPS control) to about 5.8 A, which is only 35.4% of the 
baseline ripple (a 64.6% reduction). It also lowered the ripple 
to 60.4% of that under the IPS strat egy (around a 39.6% 
reduction). Even under dynamic load fluctuations (with the 
output current stepping from 100  A to 150  A to 200  A), the 
IEPSM approach rapidly recalculated the optimal phase -shift 
combination, minimizing the output current ripple at each 
operating point. This robust performance under varying 
conditions highlights the effectiveness of the proposed strategy 
in achieving optimal ripple performance during load transients. 
The proposed IEPSM -based modulation and optimization 
approach achieves dynamic ripple minimization in a triple-port 
photovoltaic electrolysis hydrogen production system. By 
dynamically optimizing and effectively reducing the ripple 
characteristics of the electrolyzer’s operating current, the 
proposed strategy can help enhance both its efficiency and 
operational longevity. In addition, its adaptability to fluctuating 
input makes it well -suited for renewable -powered hydrogen 
production systems, supporting stable operation under dynamic 
conditions. Future work will explore the int egration of 
advanced intelligent optimization algorithms and the extension 
of the proposed low -ripple control strategy to multi -energy 
complementary hydrogen production systems, aiming to 
improve system -level performance and broaden its practical 
engineering applicability.  
REFERENCES 
[1] R. Takahashi, H. Kinoshita, T. Murata  et al., “Output Power Smoothing 
and Hydrogen Production by Using Variable Speed Wind Generators,” 
IEEE Transactions on Industrial Electronics, vol. 57, no. 2, pp. 485-493, 
Feb. 2010. 
[2] Q. Song, X. Chen, J. Liu  et al., “Decentralized Energy Management of 
Renewable Hydrogen Production Systems Without Communication 
Networks,” IEEE Transactions on Industrial Electronics,  vol. 71, no. 8, 
pp. 8927-8937, Aug. 2024. 
[3] L. Zhang, Y. Qiu, Y. Chen, and A. T. Hoang, “Multi -objective particle 
swarm optimization applied to a solar-geothermal system for electricity 
and hydrogen production; Utilization of zeotropic mixtures for 
performance improvement,” Process Safety and Environmental Protection, 
vol. 175, pp. 814-833, Jul. 2023. 
[4] C. Zou, J. Li, X. Zhang  et al., “Industrial status, technological progress, 
challenges, and prospects of hydrogen energy,” Natural Gas Industry B,  
vol. 9, no. 5, pp. 427-447, Oct. 2022. 
[5] M. Yue, H. Lambert, E. Pahon et al., “Hydrogen energy systems: A critical 
review of technologies , applications, trends and challenges,” Renewable 
and Sustainable Energy Reviews, vol. 146, pp. 111180, Aug. 2021. 
[6] X. Meng, M. Chen, M. He et al., “A novel high power hybrid rectifier with 
low cost and high grid current quality for improved efficiency of 
electrolytic hydrogen production,” IEEE transactions on power 
electronics, vol. 37, no. 4, pp. 3763-3768, Apr. 2022. 
[7] M. El-Shafie, “Hydrogen production by water electrolysis technologies: A 
review,” Results in Engineering, vol. 20, pp. 101426, Dec. 2023. 
[8] O. E. Oyewole, A. A. Abdelaziz, I. A. Jimoh  et al. , “Optimised linear 
active disturbance rejection control of multiport -isolated DC -DC 
converter for hydrogen energy storage system integration,” Alexandria 
Engineering Journal, vol. 102, pp. 159-168, Sept. 2024. 
[9] A. Hassan, O. Abdel-Rahim, M. Bajaj, and I. Zaitsev, “Power electronics 
for green hydrogen generation with focus on methods, topologies, and 
comparative analysis,” Scientific Reports, vol. 14, no. 1, pp. 24767, Oct. 
2024. 
[10] L. Wang, H. Wang, M. Fu et al., “A Three-Port Energy Router for Grid-
Tied PV Generation Systems With Optimized Control Methods,” IEEE 
Transactions on Power Electronics,  vol. 38, no. 1, pp. 1218 -1231, Jan. 
2023. 
[11] L. Jiang, J. Qu, L. Kong  et al. , “Novel integrated  three-port DC/DC 
converter for different operating modes between renewable energy, 
electrolyser and fuel cell/battery,” Clean Energy, vol. 7, no. 1, pp. 174 -
189, Mar. 2023. 
[12] L. Xu, C. Dou, D. Yue et al., “Hybrid Modeling and Switching Control of 
Electric Vehicle Aggregation for Frequency Regulation,” IEEE 
Transactions on Sustainable Energy, pp. 1-14. 2025. 
[13] F. Wu, F. Feng, and H. B. Gooi, “Cooperative Triple-Phase-Shift Control 
for Isolated DAB DC–DC Converter to Improve Current Characteristics,” 
IEEE Transactions on Industrial Electronics, vol. 66, no. 9, pp. 7022-7031, 
Sept. 2019. 
[14] F. Lin, X. Zhang, X. Li et al., “Automatic Triple Phase-Shift Modulation 
for DAB Converter With Minimized Power Loss,” IEEE Transactions on 
Industry Applications, vol. 58, no. 3, pp. 3840-3851, May-Jun. 2022. 
[15] Z. Guo, M. Li, and X. Han, “Triple -Phase Shift Modulation Scheme of 
DAB Converter With LCL Resonant Tank,” IEEE Transactions on 
Transportation Electrification, vol. 8, no. 2, pp. 1734-1747, Jun. 2022. 
[16] A. Tello, F. A. Catañ o, A. Arunachalam  et al. , “Green hydrogen 
production by photovoltaic-assisted alkaline water electrolysis: A review 
on the conceptualization and advancements,” International Journal of 
Hydrogen Energy, vol. 107, pp. 378-395, Mar. 2025. 
[17] X. Guo, H. Zhu, and S. Zhang, “Overview of electrolyser and hydrogen 
production power supply from industrial perspective,” International 
Journal of Hydrogen Energy, vol. 49, pp. 1048-1059, Jan. 2024. 
[18] V. Ruuskanen, J. Koponen, A. Kosonen et al., “Power quality estimation 
of water electrolyzers based on current and voltage measurements,” 
Journal of Power Sources, vol. 450, pp. 227603, Feb. 2020. 
[19] H. P. C. Buitendach, R. Gouws, C. A. Martinson et al., “Effect of a ripple 
current on the efficiency of a PEM electrolyser,” Results in Engineering, 
vol. 10, pp. 100216, Jun. 2021. 
[20] F. Parache, H. Schneider, C. Turpin  et al., “Impact of Power Converter 
Current Ripple on the Degradation of PEM Electrolyzer Performances,” 
Membranes, vol. 12, no. 2, pp. 109, Jan. 2022. 
[21] H. Bai, and C. Mi, “Eliminate Reactive Power and Increase System 
Efficiency of Isolated Bidirectional Dual -Active-Bridge DC –DC 
