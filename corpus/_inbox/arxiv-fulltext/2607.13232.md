---
source_id: "arxiv"
title: "arXiv:2607.13232"
url: "https://arxiv.org/abs/2607.13232"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2607.13232. Abstract:   1 
Design of Carbon Capture Processes Under  
Part-load Operating Conditions 
David Y. Shuab, Boxun Huanga, Yurim Kima, Randall Fieldb, Rahul Gandhic, and Sungho Shina* 
a Massachusetts Institute of Technology, Department of Chemical Engineering, Cambridge, MA 02139, USA 
b Massachusetts Institute of Technology, MIT Energy Initiative, Cambridge, MA 02139, USA 
c Shell Technology Center, Houston,"
---

# arXiv:2607.13232

  1 
Design of Carbon Capture Processes Under  
Part-load Operating Conditions 
David Y. Shuab, Boxun Huanga, Yurim Kima, Randall Fieldb, Rahul Gandhic, and Sungho Shina* 
a Massachusetts Institute of Technology, Department of Chemical Engineering, Cambridge, MA 02139, USA 
b Massachusetts Institute of Technology, MIT Energy Initiative, Cambridge, MA 02139, USA 
c Shell Technology Center, Houston, TX 77082, USA 
* Corresponding Author: sushin@mit.edu  
ABSTRACT 
Solvent-based carbon capture can reduce CO 2 emissions resulting from a continued reliance on fossil 
power plants for firm power. These capture processes remove CO2 from flue gases via a solvent. Careful 
design via process systems optimization can limit the overall cost of carbon capture, which is both capital- 
and energy intensive. As dispatchable power plants operate to meet varying load demand, t he design 
process needs to account for varying operating points. However, optimizing the design over multiple op-
erating points yields high computational complexity, which is why designs are often based on a single 
operating point in practice. Here, we identify optimal carbon capture process designs via stochastic opti-
mization, reducing computational complexity through a data-driven approach-to-equilibrium model of the 
absorption and desorption processes. We represent variable flue gas conditions based on part-load op-
eration data of a representative coal power plant. Accounting for this variability in the design substantially 
reduces equipment size and total plant cost by 6–9 % at the expense higher operating costs, yielding a 
reduction in total cost of carbon capture by 0.7–1.7 %. Given the capital intensity of carbon capture, var-
iability of flue gas conditions therefore should be considered at the design stage, particularly if capture is 
deployed on plants subject to load following.  
Keywords: Process Design, CCS, Stochastic Optimization, Technoeconomic Analysis 
INTRODUCTION 
Fossil power plants accounted for almost 60 % of power 
generation in the US in 2025 [1]. Renewed interest in natural 
gas power plants to supply firm power to data centers may 
lock in additional CO 2-emissions over their lifetime. These 
emissions can be reduced by carbon capture processes. 
Carbon capture processes are both capital- and energy-
intensive: Mature capture processes rely on solvents, remov-
ing CO2 from flue gases through contacting with a solvent in 
countercurrent flow in absorber columns (Fig. 1). The CO2-
rich solvent is regenerated in a desorber using steam, pro-
ducing a CO2 stream that needs to be conditioned for perma-
nent sequestration or utilization. 
Computational process system engineering is a crucial 
tool for designing capture processes that balance capital and 
operational costs , while meeting process targets and tech-
nical and regulatory constraints. Such designs should ac-
count for uncertainties which are prevalent in operational con-
ditions and in economic and technical parameters [2]. In cap-
ture processes, uncertainties arise, e.g., due to the varying 
flue gas characteristics of power plants : As fossil power 
plants provide grid-balancing flexibility, they are increasingly 
operated at part load with growing renewable penetration. Ac-
cordingly, carbon capture plants should be designed for a 
wide range of part-load conditions. 
However, accounting for uncertainty in process systems 
design can be computationally challenging [2]. To avoid ex-
cessive complexity in carbon capture design, rigorous han-
dling of uncertainties is sometimes avoided by applying over-
design margins to designs obtained from deterministic simu-
lation [3] or from optimization with detailed parametric studies 
[4]. Alternatively, computational complexity can be reduced 
by applying surrogate models  [5,6], or by focusing on select 
components [7,8].  
Uncertainty can be handled via r obust optimization, 
yielding designs that guarantee feasibility for considered un-
certainty sets [7,9,10] but may be overly conservative [2]. Al-
ternatively, uncertainty can be addressed by stochastic pro-
gramming which is risk-neutral [2].  
Prior research already considered the optimal sizing of 
the desorber and storage tanks via stochastic programming 
considering uncertain electricity and CO 2 prices or taxes [8]. 
Seo et al. [11] further applied stochastic optimization to the   

 
  2  
         
Figure 1. Process flow diagram of the carbon capture 
process considered for design optimization. 
design of carbon capture using typical days as scenarios, fo-
cusing on dynamic operation to respond to a varying electric-
ity price and demand.  
In contrast to previous studies, we apply two-stage sto-
chastic optimization to isolate the impact of part-load flue gas 
variability as a design driver for capture plants. To this end, 
we derive scenarios from real-world distributions of part-load 
operation levels of power plants. We model the capture pro-
cess as a set of interconnected unit operations, and include 
detailed technoeconomic models, allowing us to minimize the 
total annualized cost, while achieving capture targets. 
MODELING AND METHODOLOGY 
We formulate the design of the carbon capture process 
as a stochastic programming problem ( ((1)–((4)), assuming 
30 wt% monoethanolamine (MEA) as solvent.  
min
𝒙𝒙,{𝒚𝒚𝑠𝑠}𝑠𝑠∈𝒮𝒮
𝑐𝑐cap(𝒙𝒙) + � 𝑤𝑤𝑠𝑠
𝑠𝑠∈𝒮𝒮
 𝑐𝑐op(𝒙𝒙, 𝒚𝒚𝑠𝑠) (1) 
s.t.  𝒇𝒇𝑠𝑠(𝒙𝒙, 𝒚𝒚𝑠𝑠) ≤ 0, s ∈ 𝒮𝒮 (2) 
  𝒉𝒉(𝒙𝒙, {𝒚𝒚𝑠𝑠}𝑠𝑠∈𝒮𝒮) ≤ 0, (3) 
  𝒍𝒍𝒙𝒙 ≤ 𝒙𝒙 ≤ 𝒖𝒖𝒙𝒙, 𝒍𝒍𝒚𝒚 ≤ 𝒚𝒚𝑠𝑠 ≤ 𝒖𝒖𝒚𝒚,   𝑠𝑠 ∈ 𝒮𝒮 (4) 
The objective function ((1)) is the total annualized costs, 
where 𝑐𝑐cap(𝒙𝒙) represents the annualized total ownership cost 
of the equipment, 𝑐𝑐op(𝒙𝒙, 𝒚𝒚𝑠𝑠) the scenario-dependent operat-
ing costs, and 𝑤𝑤𝑠𝑠 the scenario weight. 𝒇𝒇𝑠𝑠 and 𝒉𝒉 are scenario-
dependent and scenario-coupling constraints, respectively, 
representing, e.g., techno-economic models, capture rate tar-
gets, and technical process models, such as thermodynamic 
properties, unit process models, connectivity of the unit pro-
cesses, and balance equations. 𝒍𝒍𝒙𝒙, 𝒖𝒖𝒙𝒙 and 𝒍𝒍𝒚𝒚, 𝒖𝒖𝒚𝒚 are the 
bounds of the first and second stage variables. 
The first-stage design variables 𝒙𝒙  size the unit -opera-
tions in the capture process ( Fig. 1), specifically the packing 
height and diameter of the columns, maximum pump flow 
rates, number of channels in the cross-heat exchanger, max-
imum compressor power, and heat-exchanger surface areas 
of reboiler, condenser, cooler, and intercooler. We relax the 
number of channels in the cross heat exchanger to a contin-
uous variable to maintain a nonlinear programming formula-
tion. The second-stage operating decisions 𝒚𝒚𝑠𝑠 for scenarios 
𝑠𝑠 ∈ 𝒮𝒮, include the operational variables , e.g., reboiler duty, 
solvent loading, or solvent flow rate. 
Technoeconomic Model 
The bare erected costs are estimated based on techno-
economic models [12], using the component sizes from the 
process model and assuming equipment made of stainless 
steel. The column heights are estimated using the same col-
umn to packing height ratio reported in [13] . The diameter is 
estimated based on a generalized pressure drop correlation 
for structured packing [14] at an 80 % approach to flooding. 
The costs of structured packing material are estimated as-
suming Mellapak 250Y [14] . The cross heat exchanger is 
costed as a plate-and -frame heat exchanger, while reboiler, 
condenser, cooler, and intercooler are estimated based on 
tube-and-shell heat exchangers. As the required size of the 
heat exchangers and variable speed pumps exceed the max-
imum sizes specified in [12] , we assume multiple maximum-
size units in parallel. For those units, the cost is estimated by 
scaling the cost of one maximum -size unit linearly with the 
number of units needed. We relax the number of units needed 
to a continuous variable to maintain a nonlinear programming 
formulation. The compressor power and cooling loads are es-
timated based on [15]. 
The bare erected costs are escalated to 2023 values 
using the Chemical Engineering Plant Cost Index . We esti-
mate engineering, procurement and construction costs and 
contingencies to arrive at total plant costs and further include 
preproduction, inventory, financing, and other costs using 
factors based on [16,17] to arrive at total ownership cost. The 
total ownership cost is  annualized using the capital charge 
factor from [17]. 
The operating costs include the utility costs of steam at 
150 psig, electricity, and cooling water at 90 °F [12]. We fur-
ther include f ixed operating costs for labor, maintenance, 
taxes and insurance, as well as variable operating costs for 
waste treatment and chemicals, scaled by the amount of CO2 
captured [16]. The cost of MEA makeup is estimated based 
on degradation rates  in [21] and prices in [22]  escalated to 
2023 [23]. 
Process Model 
The component sizing, utility demands, and amount of 
CO2 captured is determined using the process system model. 
The process models include material and energy balances. 
As a simplifying assumption, we calculate enthalpy changes 
in liquid and vapor phase using the pure- component models 
for heat capacity, heat of vaporization and heat of absorption 
[20], neglecting heat of mixing. In addition, we include equi-
librium reactions of MEA with CO 2 [24] in the absorber and 
desorber columns, condenser, reboiler, and cross heat ex-
changer.  
As a simplifying approximation, we assume vapor-liquid 
equilibrium in condenser and reboiler based on Henry's law  
treated flue gas
flue gas
power power
steam
cool.
water
CO2
cool.
water
make-
ups
cool.
water

 
  3  
 
Figure 2. Duration in part -load operation of sub-bituminous 
coal power plant units in Texas in 2025 [18]. A representative 
operation profile determined via k -medoids clustering is 
highlighted in orange. 
 
 
Figure 3. Simulated capture rates in comparison to 
measurements (reference) for validation. The inlet flue gas 
and lean solvent conditions of the measurements are 
summarized by [19,20]. Simulation results are shown for a 
varying number of column segments (seg.). 
for CO2 [25] and Raoult's law for water using the vapor pres-
sure [26]. For simplicity, we neglect the solubility of O2 and N2 
and assume MEA to be nonvolatile. 
To account for rate-limitations of chemical reactions and 
mass transfer between the liquid and vapor phase in the col-
umns, we use an approach-to-equilibrium model (((5)) to de-
termine how much CO 2 is absorbed or desorbed based on 
the equilibrium driving force. This modeling approach re-
duces problem complexity in comparison to a more rigorous 
rate-based model. We discretize the columns axially into seg-
ments 𝑗𝑗, which describe local vapor-liquid mass transfer and 
chemistry. Segments are numbered from the bottom of the 
column, and the approach-to-equilibrium model is applied to 
each 𝑗𝑗:  
𝑦𝑦CO2,𝑠𝑠,𝑗𝑗+1 = 𝑦𝑦CO2,𝑠𝑠,𝑗𝑗 − 𝜂𝜂�𝑘𝑘𝑠𝑠,𝑗𝑗, Δ𝑧𝑧� �𝑦𝑦CO2,𝑠𝑠,𝑗𝑗 − 𝑦𝑦CO2,𝑠𝑠,𝑗𝑗∗ � (5) 
Here, 𝑦𝑦CO2,𝑠𝑠,𝑗𝑗∗  is the CO2 mole fraction in the vapor phase 
at equilibrium and the function η depends on parameter 𝑘𝑘𝑠𝑠,𝑗𝑗 
and segment height Δ𝑧𝑧. We choose the function form so that 
η remains in [0,1] and is consistent across discretization res-
olutions (((6)). 
𝜂𝜂(𝑘𝑘, Δ𝑧𝑧) = 1 − 𝑒𝑒−𝑘𝑘Δ𝑧𝑧 (6) 
Parameter 𝑘𝑘𝑠𝑠,𝑗𝑗 lumps the effects of gas - and liquid-
phase mass transfer resistance, chemical reaction rates, in-
terfacial area and hydrodynamics, and modeling approxima-
tions on CO2 absorption and desorption.  Nevertheless, the 
liquid phase composition is always based on reaction equilib-
rium. The parameter 𝑘𝑘𝑠𝑠,𝑗𝑗 is obtained by evaluating the cali-
brated function 𝑘𝑘(⋅) at the local conditions 𝜽𝜽𝑠𝑠,𝑗𝑗: 𝑘𝑘𝑠𝑠,𝑗𝑗 = 𝑘𝑘�𝜽𝜽𝑠𝑠,𝑗𝑗�, 
where 𝛉𝛉𝑠𝑠,𝑗𝑗 includes the vapor-to-liquid molar flow rate ratio , 
inlet temperature, p ressure, inlet solvent CO2 loading, MEA 
mass fraction in the CO2-free inlet solvent, and superficial gas 
velocity. The calibrated function 𝑘𝑘(⋅) has the form: 
ln 𝑘𝑘 = 𝛽𝛽0 + � (𝛽𝛽𝑛𝑛𝜃𝜃𝑛𝑛)
𝑛𝑛∈𝒩𝒩
+ � �𝛽𝛽𝑛𝑛,𝑚𝑚 𝜃𝜃𝑛𝑛 𝜃𝜃𝑚𝑚�
(𝑛𝑛,𝑚𝑚)∈ℳ
 (7) 
Here, 𝒩𝒩 is the index set of c alibration variables and 
ℳ ⊆ 𝒩𝒩 × 𝒩𝒩 is a set of index pairs included to capture inter-
actions. The coefficients β0, β𝑛𝑛, and β𝑛𝑛,𝑚𝑚 are fitted to calibra-
tion data from experiments or detailed simulations. For clarity, 
(7) omits the normalization of the calibration data using mean 
and standard deviation. 
The plate-and-frame cross heat-exchanger is modeled 
following [27]. The tube-and-shell heat exchangers are sized 
assuming constant overall heat transfer coefficient from [28], 
and using Chen's approximation [29] of the logarithmic mean 
temperature difference. Finally, we assume an intercooler in 
the center of the absorber column with a target temperature 
range of 40 °C–50 °C. For density calculations, we assume 
ideal gases and constant solvent densities of 1000 kg m-3 for 
simplicity. 
The capture rate targets is specified for every operating 
point ((8)) or as an average over all scenarios ((9)). 
𝑉𝑉𝑠𝑠feed 𝑦𝑦CO2,𝑠𝑠feed − 𝑉𝑉𝑠𝑠abs,out 𝑦𝑦CO2,𝑠𝑠out ≥ 𝛾𝛾cap𝑉𝑉𝑠𝑠feed 𝑦𝑦CO2,𝑠𝑠feed ,  ∀ 𝑠𝑠
∈ 𝒮𝒮 
(8) 
� 𝑤𝑤𝑠𝑠�𝑉𝑉𝑠𝑠feed 𝑦𝑦CO2,𝑠𝑠feed − 𝑉𝑉𝑠𝑠abs,out 𝑦𝑦CO2,𝑠𝑠out �
𝑠𝑠∈𝒮𝒮
≥ 𝛾𝛾cap  � 𝑤𝑤𝑠𝑠�𝑉𝑉𝑠𝑠feed 𝑦𝑦CO2,𝑠𝑠feed �
𝑠𝑠∈𝒮𝒮
 
(9) 
Here, 𝑉𝑉𝑠𝑠feed and 𝑉𝑉𝑠𝑠abs,out are the absorber vapor inlet and 
outlet molar flows, and 𝑦𝑦CO2,𝑠𝑠feed  and 𝑦𝑦CO2,𝑠𝑠out  the CO2 molar frac-
tions. γcap is the capture rate target. 
CASE STUDY 
In the case study, we solve the design and operation 
problem (((1)–(4)) of the carbon capture process (Fig. 1), con-
sidering flue gases from coal power plants. For simplicity, we 
assume an end- of-pipe process and no changes to power 
plant operation or performance. 
To quantify the value of stochastic design, we compare 
four cases: As a reference, we design the process assuming 
a single scenario at the design operating point with 80  % 
power plant utilization (deterministic), reflecting design prac-
tice in industry. The operating costs are evaluated by optimiz-
ing the operation for the fixed deterministic design. 
 

 
  4  
Table 1. Optimal sizes of the main process equipment in 
the deterministic cases and relative changes in the sto-
chastic cases.  
 
variable deterministic  
reference 
stochastic  stochastic 
(avg.) 
packed height (abs.) 27.2 m -10.8 % -11.3 % 
diameter (abs.) 11.8 m +1.0 % -0.5 % 
packed height (des.) 6.1 m -13.6 % -12.3 % 
diameter (des.) 7.9 m +2.4 % -1.1 % 
cross HEX area 4.4×104 m2 -46.8 % -42.6 % 
condenser area 7.3×104 m2 -3.8 % -8.6 % 
cooler area 3.9×104 m2 +17.3 % +3.7 % 
intercooler area 6.2×104 m2 -8.8 % -12.9 % 
reboiler area 4.4×104 m2 +4.4 % -1.5 % 
compressor power 17.8 MW 0.0 % -3.0 % 
lean pump flow 1.8×104 gpm +5.3 % -3.0 % 
rich pump flow 1.9×104 gpm +4.9 % -3.0 % 
 
Next, we calculate a stochastic design, considering multiple 
weighted load scenarios (stochastic). In both, the stochastic 
and the deterministic cases, a 95 % capture rate needs to be 
achieved in all scenarios ((8)). We further include determinis-
tic and stochastic cases in which we assume that the capture 
rate needs to be achieved on average across all scenarios 
(deterministic (avg.) and stochastic (avg.), (9)).  
The scenarios 𝑠𝑠 ∈ 𝒮𝒮 represent operation at power plant 
loads from 40–100 % at increments of 10 %, and differ in the 
flue gas characteristics: We include flue gas flows and CO 2 
concentration at various operating loads for a representative 
coal power plant [30]. Due to the large flue gas mass flow of 
the plant , we assume two parallel carbon capture process 
trains. For simplicity, we assume the flue gas stream to be 
evenly distributed between trains, neglecting the option to 
shut down individual trains at low load or shared equipment 
between trains. As the H2O and O2 concentrations of the flue 
gas are not reported, we use constant values from [16].  
The relative duration at each operating load is based on 
a representative coal power plant. Specifically, we analyzed 
the operating points of sub- bituminous coal power plants in 
Texas in 2025 [18]: For each power plant, we allocate all op-
erating data points to the nearest 10 %-part-load bin, to esti-
mate the duration share in each part-load operating point. We 
then determine the medoid to select a power plant with rep-
resentative operation profile for the scenario weights in the 
case study (Fig. 2). 
The calibration coefficients β0, β𝑛𝑛, and β𝑛𝑛,𝑚𝑚 ((7)) are ob-
tained by a least-squares fit to 190,000 datapoints simulated 
using the CCSI steady state MEA model  [31], by sampling 
from a range of operating conditions  relevant for the case 
study. Predicting the CO2 concentration at the segment out-
put using the calibrated model results in an average predic-
tion error of 1.5 %. The 5th– 95th percentile prediction error 
ranges from -3.0 to 6.5 %. 
We validate the carbon capture process model by sim-
ulating a pilot plant capture process  from literature [19,20] . 
For validation, w e fix the flue gas and lean solvent 
characteristics, and the capture plant design based on  the 
cases reported in [20] , and compare our simulated capture 
rates to the ones reported in [20]. The simulated capture rates 
show agreement with the measurements, with the number of 
segments specified in our model having only a minor impact 
on the results (Fig. 3). 
To solve the design optimization, we obtain good initial 
values by simulating an open-loop capture process for a sin-
gle scenario at a column resolution of 5 segments. To do so, 
we tear the lean-solvent recycle stream, and fix the lean-sol-
vent characteristics, the plant design, and the reboiler duty at 
reasonable values. The simulation results then serve as start-
ing values for the optimization problem of the same resolu-
tion. From there, t he number of scenarios and the column 
resolution are increased successively, using the previous so-
lution as initial values and applying linear interpolation when 
increasing the column resolution. We select 30 segments as 
the final resolution for both columns, which is sufficiently high 
for the convergence of the capture rate (Fig. 3).  
The optimization problems are implemented in Julia us-
ing JuMP v1.29.3 and IPOPT v1.13.0 with the linear solver 
MA57. Thus, our results report local optima. 
RESULTS 
The optimal size of most units is reduced in the two sto-
chastic cases compared to the deterministic case (Tab. 1): 
Absorber and desorber packing heights are lowered by  11 –
13 %, and cross heat exchanger area is reduced by up to 
47 %. Smaller equipment reduces total plant cost by 6–9 % 
(Fig. 4 (a)). This reduction is driven by the columns and heat 
exchangers, which make up65 % of the cost in the determin-
istic case.  
The reductions in total plant cost are partially offset by higher 
operating costs. The operating costs are dominated by regen-
eration steam consumption, which increases in the stochastic 
cases by 4 –5 % ( Fig. 4  (b)) due to the smaller equipment, 
particularly the cross heat exchanger. Overall, the stochastic 
cases only reduce total annualized cost by 0.7 –1.7 % (Fig. 
4 (c)). 
Reductions of total annualized cost are slightly higher in 
the case in which the 95 % capture rate is achieved on an 
annual average. Here, additional operational flexibility is ex-
ploited by shifting CO2 capture from full-load to part-load pe-
riods: In the stochastic case, the capture rate increases from 
92 % at full load to up to 98 % at part load. This shift reduces 
peak mass flows and lowers total plant cost in the stochastic 
case. The deterministic case does not benefit from the addi-
tional flexibility, as its design is based on the design operating 
point. 
CONCLUSIONS 
This study applies two- stage stochastic optimization to 
simultaneously optimize the design and operation of a sol-
vent-based carbon capture process system under variable 
flue gas conditions. We model absorption and desorption  

 
  5  
        
(a) Total plant cost of the capture system. 
 
 
(b) Annual operating cost of the capture system. 
 
 
(c) Total annualized cost of the capture system. 
 
Figure 4. Cost overview of total plant cost and operating 
costs for the deterministic and stochastic designs, assuming 
95 % capture rate in every scenario or on average over the 
full year (avg.). 
processes in the columns using a data-driven approach-to - 
equilibrium model to approximate rate-limited capture. The 
total annualized cost is calculated using technoeconomic 
models as the objective function.  
Our case study of carbon capture from a coal power 
plant includes scenarios differing in flue gas conditions with 
scenario weights derived from the part -load operation of a 
representative power plant in Texas in 2025. The stochastic 
approach accounts for multiple part-load operating points and 
results in smaller sizes for most equipment, which translates 
into substantial reductions of the total plant cost by 6–9 %. 
Total annualized costs are  reduced by 0.7–1.7 % compared 
to the deterministic approach. Targeting an annual capture 
rate introduces additional flexibility that allows to shift CO2 
capture from full-load to part-load periods, enabling a further 
reduction in equipment size and total plant cost. 
This study demonstrates the cost reduction potential of 
stochastic optimization in carbon capture process design.  In 
future research, the stochastic problem formulation can be 
extended by parametric uncertainty in plant performance . 
Further, t he capture process can be co-designed with the 
power plant , enabling cost reductions  through integration. 
Crucially, the impacts of steam extraction can be explored 
through co-design. The increase in computational complexity 
resulting from these extensions needs to be addressed, e.g., 
via GPU-accelerated optimization [32]. 
ACKNOWLEDGEMENTS 
DS, BH, and SS received support from the Future En-
ergy Systems Center through the MIT Energy Initiative.  This 
publication is based on work supported by the U.S. Depart-
ment of Energy under contract DE-AC02-06CH11357. Fund-
ing was provided by the U.S. DOE Hydrocarbons and Geo-
thermal Energy Office under FWP -DOE-145-SE-
14205HPC4E-25.  
DECLARATION OF USE OF AI 
The authors used artificial intelligence tools to assist 
with grammar, spelling, and readability improvements in the 
manuscript. No AI tools were used to generate scientific con-
tent, analysis, or conclusions. All technical material reflects 
the authors' original work, and the authors are fully responsi-
ble for the accuracy of the content. 
REFERENCES 
1.  U.S. Energy Information Administration. Monthly Energy 
Review June 2026. U.S. Energy Information Administra-
tion (2026). 
2.  Li C, Grossmann IE. A review of stochastic programming 
methods for optimization of process systems under un-
certainty. Front Chem Eng 2 (2021). 
3.  Kuncheekanna VN, Gardarsdottir S, Roussanaly S. Con-
fidence analysis of design and cost performance for sol-
vent-based CO2 capture from a cement plant: a stochas-
tic modeling perspective. Front Chem Eng 7:1537880 
(2025). 
4.  Chatziasteriou CC, Kikkinides ES, Georgiadis MC. Re-
cent advances on the modeling and optimization of CO2 
capture processes. Comput Chem Eng 165:107938 
(2022). 
5.  Bahakim SS, Ricardez -Sandoval LA. Optimal design of 
a postcombustion CO 2 capture pilot -scale plant under 
process uncertainty: a ranking-based approach. Ind Eng 
Chem Res 54(15):3879–3892 (2015). 
6.  Giorgetti S, Coppitters D, Contino F, et al. Surrogate-as-
sisted modeling and robust optimization of a micro gas 
turbine plant with carbon capture. J Eng Gas Turbines 
Power 142(1):011010 (2020). 
7.  Cerrillo-Briones IM, Ricardez-Sandoval LA. Robust opti-
mization of a post-combustion CO2 capture absorber col-
umn under process uncertainty. Chem Eng Res Des 
144:386–396 (2019). 
8.  Zaman M, Jang H, Rizwan M, et al. Optimal design for 
flexible operation of the post -combustion CO 2 capture 
plant with uncertain economic factors. Comput Chem 
Eng 84:199–207 (2016). 

 
  6  
9.  Sherman JAF, Ostace AG, Allan DA, et al. Designing a 
robust MEA-based post-combustion carbon capture pro-
cess with capture rate guarantees. Ind Eng Chem Res 
65(25):13220−13240 (2026). 
10.  Akkor I, Iyer SS, Dowdle J, et al. Epistemic uncertainty 
analysis and robust optimization of a second-generation 
solvent-based post-combustion carbon capture process. 
Eng Rep 8(4):e70728 (2026). 
11.  Seo K, Retnanto AP, Martorell JL, et al. Simultaneous 
design and operational optimization for flexible carbon 
capture process using ionic liquids. Comput Chem Eng 
178:108344 (2023). 
12.  Seider WD, Lewin DR, Seader JD, et al. Product and 
Process Design  Principles: Synthesis, Analysis, and 
Evaluation. Fourth edition. John Wiley & Sons Inc. 
(2017). 
13.  Electric Power Research Institute, Elliott W. Front -End 
Engineering Design (FEED) Study for a Carbon Capture 
Plant Retrofit to a Natural Gas-Fired Gas Turbine Com-
bined Cycle Power Plant (2x2x1 Duct -Fired 758- MWe 
Facility with F Class Turbines). (2021). 
14.  Tsai RE. Mass transfer area of structured packing. Dis-
sertation. University of Texas at Austin (2010). 
15.  Kim S, Léonard G. CO2 capture technologies and 
shortcut cost correlations for different inlet CO 2 concen-
trations and flow rates. part 1: chemical absorption. Int J 
Greenh Gas Control 145:104391 (2025). 
16.  Cvetic P, Buchheit K, Kuehn N, et al. Natural Gas Com-
bined Cycle (NGCC) Power Plants with Carbon Capture 
and Exhaust Gas Recycle (EGR). (2023). 
17.  Theis J. Quality Guidelines for Energy System Studies: 
Cost Estimation Methodology for NETL Assessments of 
Power Plant Performance. (2021). 
18.  United States Environmental Protection Agency. Power 
sector data. (2026). https://campd.epa.gov/. 
19.  Morgan JC, Soares Chinen A, Omell B, et al. Develop-
ment of a rigorous modeling framework for solvent -
based CO2 capture. part 2: steady-state validation and 
uncertainty quantification with pilot plant  data. Ind Eng 
Chem Res 57(31):10464–10481 (2018). 
20.  Akula P, Eslick J, Bhattacharyya D, et al. Model devel-
opment, validation, and optimization of an MEA -based 
post-combustion CO 2 capture process under part -load 
and variable capture operations. Ind Eng Chem Res 
60(14):5176–5193 (2021). 
21.  Moser P, Wiechers G, Schmidt S, et al. Results of the 
18-month test with MEA at the post-combustion capture 
pilot plant at Niederaussem – new impetus to solvent 
management, emissions and dynamic behaviour. Int J 
Greenh Gas Control 95:102945 (2020). 
22.  Haslbeck JL, Kuehn NJ, Lewis EG, et al. Cost and Per-
formance Baseline for Fossil Energy Plants Volume 1: 
Bituminous Coal and Natural Gas to Electricity Revision 
2. National Energy Technology Laboratory (2010). 
23.  U.S. Bureau of Labor Statistics. Producer price index by 
commodity: chemicals and allied products: industrial 
chemicals [wpu061]. [Accessed: June 1, 2026] 
24.  Freguia S. Modeling of CO2 removal from flue gases with 
monoethanolamine. Master’s Thesis. University of Texas 
at Austin (2002). 
25.  Hartono A, Mba EO, Svendsen HF. Physical properties 
of partially CO 2 loaded aqueous monoethanolamine 
(MEA). J Chem Eng Data 59(6):1808–1816 (2014). 
26.  Perry RH, Green DW, Eds. Perry’s Chemical Engineers’ 
Handbook. 8th ed. McGraw-Hill (2008). 
27.  Akula P, Eslick J, Bhattacharyya D, et al. Modelling and 
parameter estimation of a plate heat exchanger as part 
of a solvent -based post -combustion CO 2 capture sys-
tem. In: Computer Aided Chemical Engineering. pp. 47–
52 Elsevier (2019). 
28.  Fisher KS, Searcy K, Rochelle GT, et al. Advanced 
Amine Solvent Formulations and Process Integration for 
Near-Term CO2 Capture Success. (2007). 
29.  Chen JJJ. Comments on improvements on a replace-
ment for the logarithmic mean. Chem Eng Sci 
42(10):2488–2489 (1987). 
30.  Roeder V, Kather A. Part load behaviour of power plants 
with a retrofitted post-combustion CO2 capture process. 
Energy Procedia 51:207–216 (2014). 
31.  U.S. Department of Energy. CCSI Steady State MEA 
Model (MEA ssm) User Manual Version 3.2.1. U.S. De-
partment of Energy (2022). 
32.  Shin S, Anitescu M, Pacaud F. Accelerating optimal 
power flow with GPUs: SIMD abstraction of nonlinear 
programs and condensed-space interior -point methods. 
Electr Power Syst Res 236:110651 (2024). 
