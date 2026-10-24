---
source_id: "lemigas-scog"
title: "Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation and Response Surface Methodol"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2078"
retrieved_at: "2026-10-24T14:30:44+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "95ab09f76c4c4cb2368eceb98426347fec581113a81d52ed108227c44dbd221c"
collected: "manual"
---

# Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation and Response Surface Methodol

DOI org/10.29017/scog.v49i2.2078 I 487 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Predictive Modeling of Pipeline Erosion in Multiphase Flow 
Using OLGA Simulation and Response Surface Methodology (RSM) 
ABSTRACT - Pipeline erosion is a significant issue in the oil and gas production sector, especially in 
multiphase flow systems. Predicting erosion in the lab is expensive and time -consuming because it requires 
elaborate flow loops. This study developed a hybrid modeling framework integrating OLGA multiphase 
flow simulation with Response Surface Methodology (RSM) to predict the erosional velocity ratio (EVR) 
under clean service gas condensate flow conditions. The EVR was determined using the API RP 14E 
erosional velocity approach available in OLGA. A Box –Behnken design with 46 simulation cases was used 
to examine the influence of superficial gas velocity, superficial liquid velocity, pipe diameter, pressure, and 
temperature on EVR behavior. The results demonstrated that pipe diameter dominates EVR variation 
(75.28%), followed by superficial liquid velocity (18.38%) and gas velocity (6.59%), while temperature 
(0.31%) and pressure (0.03%) are negligible . An ANOV A (analysis of variance) also confirmed the OLGA 
simulation results by developing a robust quadratic model, achieving an R 2 of 0.9937 and validation R ², 
RMSE, and MAE values of approximately 0.9904, 0.016, and 0.011, respectively, indicating that the model 
accurately forecasts EVR across a range of operating conditions. This model could aid in pipeline design 
optimization and enable rapid monitoring of erosion to enhance flow pipeline safety and service life.  
Keywords: erosional velocity ratio, flow assurance, surrogate modeling, superficial fluid velocity, OLGA, DOE, 
ANOV A. 
 
  
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 487 - 507 
1Petroleum Engineering Department, Universiti Teknologi PETRONAS ,  
32610 Seri Iskandar, Perak, Malaysia. 
2Interdisciplinary Research Center for Hydrogen Technologies and Carbon Management, King Fahd University of Petroleum and 
Minerals  
Dhahran 31261, Saudi Arabia. 
Corresponding author: Fahd Saeed Alakbari (fahd.akbari@kfupm.edu.sa) 
Manuscript received:  February 25th, 2026; Revised: April 03th, 2026 
Approved:  May 12th, 2026; Available online: June 19th, 2026; Published: June 19th, 2026. 
Bilal Ahmed1, Syed Mohammad Mahmood1, Mysara Eissa Mohyaldinn1, Muhammad Jawad Khan1, and 
Fahd Saeed Alakbari2

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
488 I DOI org/10.29017/scog.v49i2.2078 
𝑉𝑒 =  𝐶 𝜌𝑚                                                                        
INTRODUCTION 
Reservoir fluids are most often transported 
through pipelines in the oil and gas sector due to 
their operational efficiency and cost -effectiveness 
(OBIOMAH 2025). However, pipeline erosion has 
become a widespread concern since it reduces the 
lifespan of pipelines by damaging the surface of 
their interior walls (Chen et al., 2006; Osman et al., 
2025). The risk is magnified in multiphase flow 
systems where solid particles accelerate internal 
degradation (Othman et al., 2024). The erosional 
velocity ratio (EVR) is a key parameter in erosion 
prediction, where values above 1 typically indicate 
an elevated risk of pipeline wear (Peters et al., 
2022;  Khor et al., 2023a: Khor et al., 2023b; Al 
Wardi 2020; Peters et al., 2022). Controlling 
EVR through production and design parameters 
is essential to ensuring long -term pipeline 
reliability and safety . 
A complementary technique for reducing 
erosional damage is operational control, which 
regulates the production velocities of particle -laden 
production fluids (Vieira 2014). Many scholars 
have spent many years focusing on this very 
determination. The American Petroleum Institute 
(API) issued the  API RP 14E paper in 1975, which 
provided recommendations on the permitted 
velocity of solid -free, non -corrosive production 
fluids to minimize erosion damage; it has been 
revised five times since its first release (Shirazi 
et al., 2025). According to these 
recommendations, (Grant & Tabakoff 1975; 
Bashir et al., 2024, Pleshkov et al., 2022, Deng 
et al., 2013) serious erosion should not occur if 
production velocities are kept below the 
erosional velocity determined by Equation 1 , 
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Bilal Ahmed, Syed Mohammad Mahmood, Mysara Eissa Mohyaldinn, Muhammad Jawad 
Khan, and Fahd Saeed Alakbari , 2026, Predictive Modeling of Pipeline Erosion in Multiphase 
Flow Using OLGA Simulation and Response Surface Methodology  (RSM), Scientific 
Contributions Oil and Gas, 49 (2) pp. 487 -507. DOI org/10.29017/scog.v49i2.2078.  
where Ve is the erosional velocity in feet per 
second, ρm is the carrier fluid density in pounds 
per cubic foot, and C is a constant. The API 
guidelines specify that C = 100 for continuous 
service and 125 for intermittent service. API RP 
14E states that less -dense fluids may experience 
greater erosion. However, experimental evidence 
shows that this is not the case. Furthermore, this 
rule does not account for several factors that 
influence erosion, including particle characteristics, 
particle geometry, impact angle, and the 
mechanical properties of the wall material.  Several 
researchers concluded that API RP 14E was 
inapplicable when sand was present, and efforts 
were started to develop alternative erosion models. 
Despite offering a commonly used empirical 
limit for erosional velocity, API RP 14E does not 
specifically account for geometric complexity, 
multiphase interactions, or sand production. Rather 
than serving as a complete erosion prediction 
model, API RP 14E is used in this study solely as a 
reference threshold for determining the erosional 
velocity ratio (EVR). Researchers such as Salama 
& Venkatesh (1983), Bourgoyne (1989), and 
Svedeman & Arnold (1993) attempted to improve 
these limitations by introducing modified empirical 
relationships that incorporated pipe diameter, 
impact angle, and erosion constants (Salama & 
Venkatesh 1983; Bourgoyne Jr, 1989; Svedeman  
& Arnold 1993). 
 In recent years, research has progressed toward 
high-fidelity numerical methods. For example, X. 
Chen et al. and B. Hong et al. (Chen et al., 2006; 
Hong et al., 2021) used Computational Fluid 
Dynamics (CFD) to simulate erosion in elbows and 
tees under multiphase conditions. These models 
demonstrated high accuracy in geometry -specific 
predictions but required significant computational 
resources. More recent work by (Othman et al., 
(1)

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 489 
2024) integrated CFD with artificial neural 
networks (ANN) to predict erosion rates, achieving 
enhanced precision but introducing dependency on 
extensive datasets and calibration. Further (Parsi et 
al., 2017) proposed a new dimensionless parameter 
derived from CFD analysis to estimate solid 
particle erosion in elbows. While these models are 
effective, their applicability is often limited to 
specific pipeline geometries or flow regimes, 
making it difficult to generalize or deploy in 
field operations . 
Although previous studies have applied CFD, 
ANN, and empirical methods for pipeline erosion 
prediction, most focus on direct erosion rate 
estimation using particle tracking, impact angle 
modeling, or geometry -specific simulations. CFD 
models provide high accuracy but are 
computationally intensive, while ANN 
approaches require large datasets and often have 
limited interpretability (Chang et al., 2025; 
Nadeem et al., 2025) . 
It is essential to clarify that solid -particle effects 
are not considered in this study, which focuses 
primarily on fluid -induced erosion under clean -
service conditions. Therefore, rather than 
particle -wall impact mechanisms, 
hydrodynamic  and multiphase flow parameters 
drive erosional behavior . 
The objectives of the study are: 1). To develop 
an RSM-based surrogate model for predicting EVR 
using OLGA simulations; ) To evaluate the 
effects of superficial gas velocity, superficial liquid 
velocity, pipe diameter, pressure, and temperature 
on EVR under clean -service conditions; 3). To 
establish operational guidelines for minimizing 
EVR; 4). To validate the predictive accuracy and 
statistical reliability of the developed surrogate 
model (code-to-code validation).  
 
 METHODOLOGY 
OLGA model development 
This section describes the step -by-step methods 
used to conduct parametric research on the 
erosional velocity ratio (EVR) with OLGA 
multiphase simulation software (OLGA 2021.2.0). 
OLGA has significant benefits for modeling long -
distance and energy storage pipelines (Liang et al., 
2023a, Venriza & Wahyuni 2024, Tony et al., 
2025). It specifically provides a technique for 
optimizing design and evaluating system 
performance while considering critical elements 
such as EVR, pipeline length , and height, and 
pressure (George et al., 2024). OLGA can model a 
wide range of fluid characteristics, including single
- and multiphase flow and sediment transport. 
Furthermore, OLGA enables rapid computation 
and accurate forecasting of complex flows, 
dynamic changes, and transient responses within 
the pipeline (Liang et al., 2023b; Auni et al., 2023). 
In the OLGA simulation setup, the erosional 
velocity threshold was guided by API RP 14E, 
which is defined by Equation 2, 
𝐸𝑉𝑅 = 1𝐶 𝐸𝑉𝑅𝑉𝐴𝐶𝑇𝑈𝐴𝐿  𝐸𝑉𝑅𝑅𝐻𝑂𝑀𝐼𝑋 1/2 
(2)  
where, EVRV ACTUAL= |Usg| + |Usl| + |Usd| EVRRHOMIX= 
[ρg|Usg| + ρl(|Usl| + |Usd)]/ (|Usg|+|Usl| + |Usd|) 
and C = 100 for U in ft/s and ρ in lb/ft3, C = 121.99 
for U in m/s and ρ in kg/m 3. Here |Usg|, |Usl| and 
|Usd| denote the absolute value of the superficial 
velocity for gas, liquid film and liquid droplets 
respectively. Similarly, ρg and ρl denote gas and 
liquid density. 
The OLGA simulation model represented a 
2000 m horizontal pipeline operating under steady -
state multiphase flow conditions. The pipeline was 
discretized into 200 computational sections to 
ensure sufficient spatial resolution for pressure and 
velocity calculations along the pipeline length. 
A parametric simulation strategy was adopted in 
which operating conditions were varied according 
to the Box –Behnken experimental design matrix. 
The investigated operating ranges included 
superficial gas velocities between 5 and 30 m/s, 
superficial liquid velocities between 0 and 4 m/s, 
pipe diameters between 4 and 18 inches, operating 
pressures between 500 and 1500 psi, and 
temperatures between 25 and 100 °C. 
The EVR values were extracted directly from 
OLGA using the API RP 14E -based erosional -
velocity formulation implemented in the simulator. 
The present work focused specifically on EVR 
prediction under clean -service conditions;

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
490 I DOI org/10.29017/scog.v49i2.2078 
 
 
  
 
Parameter Min. Max. Unit 
 
 Superficial Gas Velocity 5 30 m/s  
 Oil Superficial Velocity 0 4 m/s  
 Pipe Diameter 4 18 inches  
 Pressure 500 1500 psi  
 Temperature 25 100 °C  
 
Table 1. Ranges of parameters 
therefore, explicit sand particle tracking, particle -
wall impact modeling, and erosion-rate calculations 
were not included in the simulations. 
Each DOE design point corresponded to one 
independent OLGA simulation run. The identified 
influential residual points observed during 
statistical diagnostics were associated with 
physically meaningful extreme operating 
conditions rather than numerical instability or 
simulation failure. The pipe roughness is constant 
(5 × 10 ⁻⁵ m) throughout the simulation. In realistic 
systems, roughness changes over time resulting 
from erosion, corrosion, and deposition. Such 
alterations may affect wall shear stress and flow 
behavior; however, these impacts are outside the 
scope of the present study. A list of independent 
variables considered in the current study has been 
presented in the Table 1.  
Moreover, three operating pressures, such as 
500, 1000, and 1500 psi , and an operating 
temperature ranging from 25 °C to 100 °C were 
considered.  The composition of the gas 
condensate considered is presented in Table 1   
(Su et al., 2003) . 
In the OLGA simulations, the flow 
conditions were controlled using gas and liquid 
mass flow rates. These flow rates were 
subsequently converted  on superficial gas 
velocity (Vsg) and superficial liquid velocity 
(Vsl) using the pipe cross -sectional area for 
response surface methodology (RSM) modeling 
and statistical analysis. Therefore, the 
discussion of parametric effects in the RSM 
section is presented in terms of superficial 
velocities rather than direct mass flow rates.  
Assumptions and Limitations 
• The study focused only on EVR prediction 
under clean -service multiphase flow conditions 
using OLGA and RSM approaches. 
• The developed model is based on API RP 14E 
erosional velocity criteria and does not directly 
predict the actual erosion rate. 
• Explicit sand particle tracking, particle -wall 
interaction, and particle impact angle effects 
were not modeled. 
• Simulations were limited to a straight horizontal 
pipeline configuration. 
• Complex pipeline components such as elbows, 
tees, valves, and fittings were not considered. 
• Localized turbulence and severe erosion regions 
associated with fittings were outside the scope 
of the study. 
• Wax deposition, hydrate formation, and heat 
transfer effects were neglected. 
• Flow regime identification and analysis were 
not explicitly performed. 
• Pipe roughness was assumed  constant 
throughout the pipeline (5 × 10⁻⁵ m). 
• Pressure drop and phase behavior were 
calculated using OLGA ’s built -in governing 
equations but were not independently validated. 
• Validation was limited to computational 
agreement between OLGA simulations and the 
RSM surrogate model. 
• Additional calibration with real operational or 
experimental data is required before industrial 
application of the model. 
This methodology ensures a comprehensive 
assessment of gas -condensate multiphase flow 
dynamics under the given pipeline conditions 
using OLGA.  
Design of experiments (DOE):  
A Design of Experiments (DOE) method was 
employed to effectively explore the parameter 
range. To ascertain how various input factors

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 491 
 
impact the process's output, Sir R.A. Fisher created 
the Design of Experiments approach in the 1920s 
(Ghomian 2008; Ghorbani 2008; Al Shalabi 2014). 
Identifying the input or independent elements is the 
first and most crucial phase in the use of RSM as it 
has a big impact on the whole process, including 
the desired responses as outputs (Veza et al., 2023). 
 In order to determine the optimum target, the 
RSM uses a low -order polynomial equation to 
identify a certain region of the predictor variables, 
which is further evaluated to determine the best 
possible values of the predictor variables (Ceylan 
et al., 2008). Compared to conventional 
methodologies and a time -consuming one-factor-at
-a-time approach, optimization employing the RSM 
speeds up the collection of experimental study 
outcomes (Alim et al., 2008. Central Composite 
Design (CCD),  D-optimal designs, Box –Behnken, 
and historical data design are the most used forms 
in the RSM (Asghar et al., 2014).  
A randomized Box –Behnken Design (BBD) 
under Response Surface Methodology (RSM) was 
employed to systematically evaluate the effects of 
five independent variables on the erosional velocity 
ratio (EVR). The selected predictor variables were 
superficial gas velocity (Vsg), superficial liquid 
velocity (Vsl), pipe diameter, operating pressure, 
and temperature. The Box –Behnken approach was 
selected because it provides efficient quadratic 
model development with fewer simulation runs 
compared to full factorial designs while 
minimizing extreme combinations of variables. 
 The experimental design consisted of 46 
OLGA simulation runs generated using Design -
Expert software. Each simulation run corresponded 
to one unique combination of operating parameters 
within the selected design space. The predictor 
variables were coded into three levels ( −1, 0, and 
+1), representing low, center, and high operating 
conditions, respectively. The ranges of the 
investigated variables are summarized in Table 1. 
 The generated DOE matrix was directly 
mapped to OLGA simulations, with each design 
point simulated independently under steady -state 
conditions. The resulting EVR values obtained 
from OLGA were then used as the response 
variable for regression model development and 
statistical analysis. 
 The suggested response surface methodology 
(RSM) model, which forecasted the EVR in the 
pipeline, was constructed using the block diagram 
displayed in Figure 1. The elements of the block 
diagram were (1) gathering data, (2) developing an 
EVR model, (3) assessing the RSM model, and (4) 
investigating how the predictors affected EVR. 
EVR was utilized as a target response in the RSM 
for variables including fluid velocities, pipe 
 
Figure 1. Block diagram

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
492 I DOI org/10.29017/scog.v49i2.2078 
diameters, pressure, and temperature after the 
parameter ranges were first specified from the 
literature and run in OLGA to produce EVR.  
 The developed RSM model was then assessed 
using a variety of methods, such as fit statistics, 
diagnostic plots, Pareto charts, and analysis of 
variance (ANOVA). The next step was to apply the 
EVR model's contour and 3D surface response 
plots in Design -Expert software to assess the 
interactions between predictors and the target. 
From an engineering perspective, the developed 
OLGA-RSM surrogate model enables rapid EVR 
assessment without repeatedly performing 
computationally intensive multiphase simulations. 
This makes it useful for preliminary pipeline 
design, operational screening, flow assurance 
analysis, and production optimization. Compared 
with detailed CFD -based erosion models, the 
proposed approach provides a practical balance 
between physical representation and computational 
efficiency for rapid engineering evaluations under 
clean-service multiphase flow conditions. 
EVR correlation development using response 
surface methodology (RSM) 
RSM, also known as the response surface 
methodology, is a well -known approach to 
𝜂 =  ƒ  𝑥1,𝑥2,…𝑥𝑛 +ℰ 
(3)  
experimental design (DOE). RSM was employed to 
determine the relationship between goal variables 
(output variables) and predictor variables (input 
variables) to enhance the process. In addition, 
mathematical models of RSM were developed to 
investigate the impacts of the predictor factors. 
Equation 3 below represents the connection 
between the predictor and the target variables 
(Myers et al., 2016, Alakbari et al., 2025). 
 
Component Mole Percent Mole Weight (g/mol) Component Mole Percent Mole Weight (g/mol)  
 Water 0.057 18.015 Iso Pentane 0.108 72.151  
 Nitrogen 0.081 28.014 Normal Pentane 0.089 72.151  
 Carbon Dioxide 0.251 44.01 Hexanes 0.101 86.178  
 Methane 94.388 16.043 Heptanes 0.076 96  
 Ethane 3.207 30.07 Octanes 0.048 107  
 Propane 1.069 44.097 Nonanes 0.01 121  
 Iso Butane 0.241 58.124 C10+ 0.003 134  
 Normal Butane 0.272 58.124     
 
Table 2. Fluid composition 
Table 3. Data range and statistical 
 
Parameters Min. Max. Mean Std. Dev. Skewness  
 
 Vsg (m/s) 5 30 17.5 7.372098 3.86E-17  
 Vsl (m/s) 0 4 2 1.179536 0  
 Diameter (inch) 4 18 11.47 3.645957 0.819777  
 Pressure (psi) 500 1500 1000 285.3131 0.002654  
 Temperature (°C) 25 100 60 22.66539 0.029593  
 EVR 0.0723 2.1034 0.5218 0.371485 2.117483  
 
where η: in this study, the response is indicated by 
a specific EVR, f: the unknown function of 
response, x1, x2, . . . xn: the predictor variables. 
The objective was to identify the relationship 
between the inputs (Vsg, Vsl, diameter, pressure, 
and temperature) and the response EVR. Table 3 
shows how Design -Expert was used to generate 
new empirical correlations for EVR forecasts based 
on Vsg, Vsl, diameter, pressure, and temperature.  
In addition to using Design-Expert tools, regression 
analysis was employed to find the best fit to the 
data (Dawud and Shakya, 2019. (Satiyawira et al., 
2025 used RSM as a tool for the optimization of 
drilling fluid. A mathematical model that supports

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 493 
 
the relationship of the objective functions with the 
test factor group is obtained by regression analysis, 
assisting in developing a common relation  between 
the predictor and the target parameter (Deng & Cai 
2010; Marbun et al., 2025). In addition, the 
regression approach is utilized to examine response 
surface behavior. 
The extent to which the variable predictors Vsg, 
Vsl, diameter, pressure, and temperature affect the 
target variables and the EVR in the regression 
analysis is further evaluated using analysis of 
variance (ANOVA). ANOVA was used in 
statistical analyses to evaluate the contributions of 
predictor variables to response, i.e. , the EVR 
(Adalarasan et al., 2015; Derdour et al., 2018). 
 
RESULT AND DISCUSSION 
OFAT for Parameters in OLGA simulation. 
Diameter 
In Figure 2, the Erosion Velocity Ratio (EVR) 
and pipe diameter have a strong 
inverse relationship, based on the one -factor-at-a-
time (OFAT) study. 
As the diameter increases, the EVR decreases 
markedly, a trend effectively modeled by power -
law regression curves. Reducing the pipeline 
diameter increases EVR because it drives the fluid 
to move faster to maintain the same flow rate. This 
promptly increases the risk of erosion.(Supmea, 
2023 The chart shows that while larger diameters 
lead to lower EVR values, the rate of decrease 
varies with the specific settings of the other 
variables (Min, Mean, Max). Under all operating 
conditions, smaller diameters show noticeably 
higher EVR values.  In particular, the 4" and 8" 
pipes exhibit higher erosion risk, especially when 
temperature, pressure, and mass flow rate are at 
their highest, while pipes with diameters of 12" and 
larger consistently have low EVR levels under all 
operating situations. As the diameter increases, the 
influence of other parameters becomes negligible.  
 Effect of mass flow when varying diameter 
In Figure 3, for varying diameters, the OFAT 
analysis for mass flow reveals a strong linear 
relationship between mass flow rate and EVR 
across all test conditions, with R ² values of 0.9973 
to 1.0 indicating an excellent fit. As the flow rate 
increases, EVR rises steadily, with the rate of 
increase (slope m) being highest under Min 
conditions due to the lower -diameter effect and 
varying across Mean and Max settings. As mass 
flow increases from 10 to 30 kg/s, EVR 
consistently increases, with the steepest rise 
observed at the minimum setting. This suggests 
that mass flow has a predictable and proportional 
impact on EVR, making it a reliable parameter for 
tuning system performance. The linear trend also 
implies that incremental increases in mass flow 
result in  a steady increase in EVR.  
Figure 2. OFAT of diameter for EVR while keeping other variables constant at their Min, Mean and Max.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
494 I DOI org/10.29017/scog.v49i2.2078 
Effect of mass flow when the diameter is 
constant, 12 inches 
In Figure 3, for Constant Diameter as mass flow 
increases from 10 to 30 kg/s, the EVR 
demonstrates a linear and proportional increase for 
all three cases (Min, Mean, and Max). The slopes 
of the regression lines are nearly identical, 
indicating that increasing mass flow predictably 
and consistently enhances erosional velocity across 
all scenarios. This linearity suggests that EVR is 
directly dependent on flow rate under constant pipe 
diameter, and that increasing the mass flow rate in 
a pipeline (without increasing the diameter) 
immediately increases EVR and the risk of erosion.
(Othman et al., 2023). 
Temperature 
Figure 4 illustrates how the Erosional Velocity 
Ratio (EVR) varies with temperature (25–100 °C) 
under two conditions: varying diameter (left) and 
constant diameter (right). In the varying -diameter 
case, EVR min, EVR mean, and EVR max all increases 
linearly with temperature, with EVR max showing 
the steepest rise and exceeding the critical EVR 
threshold, suggesting a higher risk of erosion at 
elevated temperatures due to increased velocity 
imbalances. Conversely, the constant diameter 
yields lower, more stable EVR values, all of which 
remain below the threshold over the temperature 
range. As the temperature increases, the gas density 
drops due to expansion. Lower density (at constant 
mass flow) leads to higher gas velocity, which 
raises the actual velocity component of EVR. With 
small-diameter pipes, the velocity increase is 
greater, so EVR rises faster. 
Pressure  
Figure 5 shows the effect of pressure (500–1500 
psi) on the Erosional Velocity Ratio (EVR) under 
varying (left) and constant (right) diameter 
conditions. In the varying -diameter case, all EVR 
values (min, mean, max) decrease slightly with 
increasing pressure, as indicated by negative 
slopes, yet EVR max consistently exceeds the 
critical threshold, indicating ongoing erosional risk. 
In contrast, the constant -diameter configuration 
shows nearly flat trend lines with negligible slopes, 
and all EVR values remain well below the 
threshold, reflecting excellent flow stability. At 
constant temperature, increasing pressure increases 
gas density. For a fixed mass flow, higher density 
lowers the velocity, which in turn reduces EVR. 
However, the effect is marginal because gas 
compressibility at these moderate pressures (500–
1500 psi) doesn ’t cause significant velocity drops. 
Overall, Figure 5 suggests that pressure has 
minimal impact on EVR, and maintaining a 
constant diameter is key to reducing erosional risk. 
Figure 3. Effect of Mass Flow on EVR for constant and varying diameters

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 495 
Figure 4. Effect of Temperature on EVR for constant and varying diameters 
Figure 5. Effect of Pressure on EVR for constant and varying diameters 
 
 
EVR correlation 
The results of this study suggest that the 
developed RSM model for EVR prediction is 
satisfactory. The empirical relationship between 
EVR and the process variables was represented in 
equation 4 using the complete quadratic regression 
obtained from the Box –Behnken Response Surface 
Methodology. The final regression model in terms 
of actual factors is expressed as follows in Table 4.  
𝐸𝑉𝑅 =  2.99325 + 0.020240(𝐴) + 0.293276(𝐵)
− 0.462939(𝐶) + 0.000695(𝐷)
− 0.000031(𝐸) + 8.54291 × 10− 6(𝐴𝐵)
− 0.000914(𝐴𝐶) + 0.000032(𝐴𝐷)
− 7.05612 × 10− 7(𝐴𝐸)− 0.014814(𝐵𝐶)
+ 0.000290(𝐵𝐷)− 6.32577 × 10− 6(𝐵𝐸)
− 0.000089(𝐶𝐷) + 2.00876 × 10− 6(𝐶𝐸)
+ 2.26686 × 10− 7(𝐷𝐸) + 0.000052(𝐴2)
− 0.002070(𝐵2) + 0.016596(𝐶2)
− 1.58185 × 10− 6(𝐷2)− 2.01434 × 10
− 10(𝐸2)                      (4)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
496 I DOI org/10.29017/scog.v49i2.2078 
where A superficial gas velocity, Vsg (m/s), B 
superficial liquid velocity, Vsl (m/s), C pipe 
diameter (inches), D  temperature (°C), and E 
pressure (psi) using Equation 4. 
The EVR model has been evaluated through 
ANOVA, diagnostics plots, and fit statistics.  
 
  
 
Term Coefficient Term Coefficient 
 
 Intercept 2.99325 BD 0.000290  
 A (Vsg) 0.020240 BE -6.32577E-06  
 B (Vsl) 0.293276 CD -0.000089  
 C (Diameter) -0.462939 CE 2.00876E-06  
 D (Temperature) 0.000695 DE 2.26686E-07  
 E (Pressure) -0.000031 A² 0.000052  
 AB 8.54291E-06 B² -0.002070  
 AC -0.000914 C² 0.016596  
 AD 0.000032 D² -1.58185E-06  
 AE -7.05612E-07 E² -2.01434E-10  
 BC -0.014814    
 
  
Table 4. Coefficients of actual quadratic Equation 
Table 5. ANOVA For EVR 
Source Sum of squares df Mean square F-value P-value  
Model 6.31 20 0.3154 196.01 < 0.0001 significant 
A-Vsg (Superficial gas velocity) 0.4157 1 0.4157 258.36 < 0.0001 
 
B-Vsl (superficial liquid 
velocity) 
1.16 1 1.16 722.37 < 0.0001 
 
C-Diameter 4.75 1 4.75 2951.22 < 0.0001 
 
D-Temperature 0.0193 1 0.0193 11.98 0.0019 
 
E-pressure 0.0016 1 0.0016 0.9731 0.3334 
 
AB 1.83E-07 1 1.83E-07 0.0001 0.9916 
 
AC 0.0215 1 0.0215 13.35 0.0012 
 
AD 0.0009 1 0.0009 0.5717 0.4567 
 
AE 0.0001 1 0.0001 0.0483 0.8278 
 
BC 0.1443 1 0.1443 89.69 < 0.0001 
 
BD 0.0019 1 0.0019 1.18 0.288 
 
BE 0.0002 1 0.0002 0.0995 0.7551 
 
CD 0.0012 1 0.0012 0.7727 0.3877 
 
CE 0.0001 1 0.0001 0.0695 0.7943 
 
DE 0.0001 1 0.0001 0.0449 0.8339 
 
A² 0.0006 1 0.0006 0.3575 0.5553 
 
B² 0.0006 1 0.0006 0.3748 0.5459 
 
C² 1.95 1 1.95 1213.96 < 0.0001 
 
D² 0 1 0 0.0256 0.8741 
 
E² 2.14E-08 1 2.14E-08 0 0.9971 
 
Residual 0.0402 25 0.0016 
   
Lack of Fit 0.0402 16 0.0025 
   
Pure Error 0 9 0 
   
Cor Total 6.35 45 
    
 
Analysis of variance 
An analysis of variance (ANOVA) was 
performed at the 5% significance level to evaluate 
the influence of various process factors on the EVR 
response. The relative importance of each  factor 
and interaction in the model is shown by the F -
values and p-values in Table 5.

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 497 
The Model F-value of 196.01 implies the model 
is significant. There is only a 0.01% chance that an 
F-value this large could occur due to noise. P -
values less than 0.0500 indicate model terms are 
significant. In this case, A, B, C, D, AC, BC, and 
C² are significant model terms. Values greater tha n 
0.1000 indicate the model terms are not 
significant. If there are many insignificant model 
terms (excluding those required to support the 
hierarchy), model reduction may improve the 
model. These factors are statistically significant 
and have a considerable impact on the model 
response. However, E (p = 0.3334) is not 
statistically significant at the 95% confidence level, 
indicating that it has no major impact on the EVR 
under the conditions investigated. With a Residual 
Mean Square of 0.0016 and a Lack of Fit score of 
0.0025, suggesting a good model fit.(Zabeti et al., 
2010. Given the significance of several key terms, 
the model is refined for greater accuracy and 
confidence, ensuring a robust predictive response 
for the EVR quadratic model. 
The developed quadratic regression model 
satisfies the hierarchy principle, as all significant 
interactions and quadratic terms were retained 
together with their associated main effects. The 
lack-of-fit test was statistically insignificant (p > 
0.05), indicating that the model adequately 
represents the relationship between the operating 
parameters and EVR within the investigated design 
space. In addition, a Box –Cox transformation 
analysis was performed to evaluate the need for 
response transformation. The optimal lambda value 
was close to unity, indicating that no significant 
transformation of EVR was required. Therefore, 
the ANOVA and regression analyses were 
conducted using the original EVR response values.   
Fit statistics 
Table 6 shows the fit statistics for the developed 
model, indicating its excellent accuracy and 
reliability in forecasting EVR responses. The 
model has a good coefficient of determination (R ² 
= 0.9937), explaining 99.37% of the variability in 
the response. The adjusted R ² (0.9886) and 
predicted R ² (0.9539) are closely aligned, 
indicating that the model is not overfit and can 
accurately predict new data. Furthermore, the 
standard deviation (0.0401) and coefficient of 
variation (7.69%) show minimal residual 
variability and high accuracy.  
An initial quadratic RSM model containing 
linear, interaction, and quadratic terms was 
established and later simplified via backward 
elimination based on the statistical significance of 
the model terms, while preserving the hierarchical 
structure. Several diagnostic tests were then 
conducted to assess the suitability of the developed 
regression model. The Box–Cox analysis suggested 
that transformation of the response was 
unnecessary, indicating that the original EVR data 
were appropriate for model development. 
Examination of the residual plots showed a random 
scatter around the zero line without any noticeable 
pattern, which indicates stable variance and 
acceptable model behavior.  
In addition, the predicted values were in close 
agreement with the OLGA simulation results, 
demonstrating the surrogate model's strong 
predictive performance. The Cook ’s distance 
results also showed that most runs had minimal 
influence on the regression fit, with only a few 
points showing comparatively stronger influence 
due to extreme response values. Overall, the 
statistical diagnostics confirmed that the developed 
EVR model is reliable, stable, and capable of 
accurately representing the simulation data. 
The model's suitable signal -to-noise ratio and 
appropriateness for navigating the design space are 
demonstrated by its Adequate Precision value of 
70.6829, which is significantly greater than the 
minimum requirement of 4. These statistical 
analyses validate the regression model's validity 
and robustness, making it an effective tool for 
examining and refining the factors influencing the 
EVR response.  
Table 6.  FIT statistics analysis of RSM model 
Parameter R2 St. D. Mean COV (%) Adj. R2 Predicted R2 Ad. Precision 
Value 0.9937 0.0401 0.5219 7.69 0.9886 0.9539 70.6829

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
498 I DOI org/10.29017/scog.v49i2.2078 
EVR model verification 
To further evaluate the predictive capability of 
the developed RSM model, an external validation 
study was conducted using additional OLGA 
simulation cases outside the original DOE dataset. 
Ten independent operating conditions were 
selected and simulated separately in OLGA under 
clean-service multiphase flow conditions. This is a 
code-to-code validation in which the simulation 
tool's numerical behavior is replicated by the 
surrogate model.    
The predicted EVR values obtained from the 
RSM model were compared to the corresponding 
OLGA simulation results. The comparison 
demonstrated excellent agreement between 
predicted and simulated EVR values, confirming 
the generalization capability of the developed 
surrogate model outside the original design space. 
The developed model achieved high predictive 
accuracy with R ², RMSE, and MAE values of 
approximately 0.9904, 0.016, and 0.011, 
respectively, as shown in Figure . These results 
indicate that the proposed OLGA -RSM framework 
can reliably predict EVR within the investigated 
operational range while significantly reducing 
computational effort compared to repeated full 
multiphase simulations. 
 Effect of the Predictor Variables on EVR 
To assess the interactions among predictor 
variables, Design -Expert was used to interpret the 
contour and 3D surface response plots of the EVR 
model, including Vsg, Vsl, diameter, pressure, and 
temperature. i.e., the EVR, as Figures. From 7 to 8. 
Effect of Vsl and Vsg on EVR 
This graph Figure  (a) shows the relationship 
between superficial gas velocity (Vsg) on the x -
axis (ranging from 5 to 30 m/s) and superficial 
liquid velocity (Vsl) on the y -axis (from 0 to 4 m/
s), with EVR represented by contour lines. The 
contour lines labeled 0.2, 0.4, 0.6, 0.8, and 1.0 
show that EVR increases as both Vsg and Vsl 
increase, indicating a positive correlation. The 
diagonal trend of the lines from bottom -left (low 
Vsg and Vsl) to top -right (high Vsg and Vsl) 
means that combinations like Vsg = 10 m/s and Vsl 
= 0.5 m/s yield EVR ≈ 0.2, while Vsg = 25 m/s and 
Vsl = 3 m/s correspond to EVR ≈ 0.8. This implies 
that, to keep EVR constant, an increase in one 
velocity must be offset by decreases in the others.  
3D effect of Vsg and pipe diameter on EVR 
The combined effects of pipe diameter and 
superficial gas velocity (Vsg) on the Erosional 
Velocity Ratio (EVR) are shown in the 3D surface 
graphic Figure  (b). The graphic demonstrates that 
EVR rises as Vsg increases, emphasizing how Vsg 
increases EVR, although pipe diameter remains the 
dominant factor. However, as pipe diameter 
increases, the EVR tends to decrease, indicating 
that larger pipe diameters reduce velocity 
gradients, which in turn decrease EVR. The 
gradient flattens for larger diameters and is steeper 
for smaller ones, indicating that EVR's sensitivity 
to Vsg decreases with increasing pipe diameter. 
 Contour effect of Vsg and pipe diameter on 
EVR  
Figure  (c) shows the relationship between 
superficial gas velocity (Vsg) on the x -axis and 
pipe diameter on the y -axis, with EVR (Erosional 
Velocity Ratio) represented by color-coded contour 
lines. The contour lines trend mostly horizontally, 
indicating that EVR is highly sensitive to changes 
in pipe diameter, whereas changes in Vsg have a 
smaller effect than changes in diameter. 
Specifically, EVR increases as pipe diameter 
decreases the red zone at the bottom (small 
diameters) shows higher EVR values (e.g., 2 and 
3), while the blue zone at the top (larger diameters) 
shows lower EVR values (e.g., 0 and 1) (Onyegiri 
et al., 2020. This means that for a given Vsg, a 
smaller pipe diameter significantly increases the 
risk of erosion. The nearly horizontal lines suggest 
that diameter is the dominant factor influencing 
EVR in this scenario. 
Effect of Vsl and Pipe Diameter on EVR 
This graph Figure  (d), displays how EVR 
(Erosional Velocity Ratio) varies with superficial 
liquid velocity (Vsl) on the x -axis (ranging from 0 
to 4 m/s) and pipe diameter on the y-axis

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 499 
 
 
Figure  6.  External validation of RSM model vs OLGA for EVR at different operating conditions. 
 
(ranging from 2 to 18 inches). The contour 
lines, marked with EVR values 0, 1, 2, and 3, show 
that EVR increases significantly as diameter 
decreases, while increasing Vsl also causes a 
moderate rise in EVR. For instance, at a 2.5 -inch 
diameter and Vsl = 3 m/s, the EVR is about 3, 
indicating a high erosion risk. In contrast, at a 14 -
inch diameter and at the same Vsl = 3 m/s, the 
EVR is close to 0, reflecting a much lower erosion 
potential. The mostly horizontal contour lines 
suggest that pipe diameter has a stronger influence 
on EVR than liquid velocity in this scenario. 
Effect of Vsg and temperature on EVR 
The EVR contour plot Figure  (a) illustrates the 
relationship between superficial gas velocity (Vsg) 
and temperature, highlighting regions of potential 
erosional risk. Results indicate that EVR 
increases with Vsg, whereas higher temperatures 
slightly increase EVR. The contour line at EVR 
= 1.0 serves as a critical threshold, 
distinguishing safe (EVR < 1) and unsafe (EVR 
> 1) operational zones . 
Effect of diameter and temperature on EVR 
Figure  (b) shows the effect of diameter (C: 
inches) and temperature (D: °C) on the response 
EVR using a contour plot. EVR values decrease 
from 3 to below 1 as the diameter increases from 
around 2 to 8 inches, as shown by vertical contour 
lines that transition from red to blue. The near -
vertical contour lines indicate that EVR is strongly 
influenced by diameter, while temperature (25°C to 
100°C) has minimal effect. This confirms diameter 
as the primary factor affecting EVR in this system.  
Effect of Vsl and Temperature on EVR 
Figure  (c) shows EVR increases as superficial 
liquid velocity (Vsl) increases, whereas 
temperature has only a slight impact, according to 
the EVR contour plot for Vsl versus temperature. 
The safe and critical zones are indicated by the 
EVR <1 contour line, which shows that higher Vsl 
values make the system more vulnerable to erosion. 
This implies that regulating EVR  requires 
controlling Vsl, with temperature also affecting 
EVR in these scenarios.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
500 I DOI org/10.29017/scog.v49i2.2078 
 
(a) (b) 
(c) (d) 
Figure  7. Response surface and contour plots illustrating the interaction effects of process parameters  on  EVR. 
Contour plot in RSM (a) Vsg vs  Vsl, (b) 3D plot for Vsg vs Pipe Diameter, 
(c) Vsg vs Pipe Diameter, (d) Vsl vs Pipe Diameter 
The strong effect of pipe diameter on EVR is 
primarily due to its influence on flow velocity and 
turbulence inside the pipeline. For a constant mass 
flow rate, reducing the pipe diameter decreases the 
flow area, which increases fluid velocity, wall 
shear stress, and turbulence intensity, thereby 
increasing EVR. In multiphase flow, smaller 
diameters also intensify phase interactions and 
local velocity fluctuations, further increasing the 
tendency toward erosion. Conversely, larger 
diameters reduce turbulence and flow velocity, 
leading to lower EVR values and reduced erosion 
risk, which explains the dominant contribution of 
diameter observed in the ANOVA analysis. 
Despite having relatively little impact, temperature 
and pressure have an indirect relationship with 
fluid characteristics. Temperature increases cause 
condensate viscosity to decrease, which can change 
flow profiles and shear stress distribution and 
affect erosion behavior.

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 501 
 
Figure  8.  EVR contour plot illustrating the interaction effects of parameters. 
a). Vsg vs temperature, b). diameter vs temperature, c). Vsl vs temperature.   
b) a) 
c) 
The statistical insignificance of pressure in the 
ANOVA indicates that it contributes minimally to 
EVR variation within the investigated operating 
range. Physically, increasing pressure increases gas 
density, which may slightly reduce gas velocity for 
a fixed mass flow rate. However, within the 
investigated pressure range of 500–1500 psi, the 
resulting velocity variation was insufficient to 
significantly affect EVR relative to dominant 
parameters such as pipe diameter and superficial 
velocity. This finding suggests that pressure may 
potentially be excluded from simplified future EVR 
surrogate models under similar clean -service 
operating conditions without substantial loss of 
predictive accuracy.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
502 I DOI org/10.29017/scog.v49i2.2078 
Engineering implications and practical 
applications 
Real-world application scenario 
This study ’s regression -based EVR model 
offers a practical decision -support tool for pipeline 
design and real -time operational adjustments. For 
example, consider a typical gas -condensate 
pipeline with these conditions: 1). Operating 
pressure: 1000 psi; 2). Superficial gas velocity 
(Vsg): 20 m/s; 3). Superficial liquid velocity (Vsl): 
2 m/s; and 4). Pipe diameter: 6 inches.  
Using the proposed RSM -predicted model, the 
EVR is approximately 1.45, indicating a high risk 
of internal erosion. To lower the EVR below the 
critical threshold (EVR < 1), operators could 
increase the diameter to 10 inches, resulting in an 
EVR of about 0.78 under the same flow conditions. 
This adjustment would significantly reduce the risk 
of erosion without decreasing throughput. 
Compared to established models such as Salama 
and DNV correlations, the proposed RSM -based 
model offers improved computational efficiency 
and adaptability to multiphase simulation outputs. 
However, unlike empirical models derived from 
experimental data, the present model requires 
further validation to ensure predictive reliability 
under field conditions. 
Design guidelines based on EVR modeling 
The guidelines in Table  translate the 
relationship between velocity, diameter, and EVR 
into clear operational limits. By defining safe 
velocity ranges for each pipe size, they assist 
engineers in selecting diameters that maintain EVR 
< 1 during design and in verifying safe operating 
conditions during production. These limits also 
support system upgrades and integrity assessments 
by indicating when higher flow rates exceed 
erosion-safe thresholds. Overall, the design limits 
presented in Table 7 are derived for a gas 
condensate in a 2000 m straight pipeline 
configuration and do not account for complex 
geometrical features such as elbows, tees, valves, 
or fittings, where localized turbulence and erosion 
are typically more severe. Therefore, these values 
should be used only for preliminary assessment and 
not as definitive design criteria. 
 
CONCLUSION 
Based on simulation results, the following 
conclusions can be drawn: 1). The model predicts 
EVR, not actual erosion rate, and is valid only for 
clean-service straight pipeline conditions within the 
studied range; 2). EVR decreases significantly as 
diameter increases, a trend that power -law 
regression models effectively represent; 3). Mass 
flow demonstrates a clear linear relationship 
between mass flow rate and EVR. However, the 
higher slope of the EVR line at the minimum is 
caused by the most significant effect of the 
diameter at that point; 4). At a constant diameter of 
12”, EVR increases significantly with mass flow, 
decreases slightly with pressure, and is minimally 
affected by temperature; 5). The regression model's 
high predictive accuracy (R ² = 0.9937) was 
confirmed in forecasting EVR across different 
pressure, temperature, and flow conditions; 6). 
Diameter and fluid velocity have a much greater 
impact on EVR than other parameters.  
 
ACKNOWLEDGEMENT 
The corresponding author appreciatively 
acknowledges the Interdisciplinary Research 
Centre for Hydrogen Technologies and Carbon 
Management at King Fahd University of Petroleum 
Table 7. Guidelines for pipeline pre-selection. 
 
  
Pipe diameter 
(inches) 
Safe max Vsg 
(m/s) 
Safe max Vsl 
(m/s) Approximate EVR 
 
6" ≈ 5.0 ≈ 0.5 1  
8" ≈ 19.6 ≈ 1.96 0.997  
10" ≈ 34.1 ≈ 3.41 0.999  
12" ≈ 48.3 ≈ 4.83 0.999

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 503 
& Minerals, Dhahran 31261, Saudi Arabia, for 
supporting this study. The authors express their 
sincere appreciation to the Centre of Flow 
Assurance, Universiti Teknologi PETRONAS, for 
fostering a supportive working environment and 
financial support that contributed to the successful 
completion of this work. The authors also 
gratefully acknowledge the support from the 
Higher Education Commission (HEC), Pakistan, 
for providing financial assistance.  
 
DECLARATIONS 
Authors’ contributions 
Bilal Ahmed: conceptualization, data curation, 
methodology, software, validation, writing – 
original draft.  Syed Mohammad Mahmood: 
conceptualization, data curation, investigation, 
methodology, project administration, validation, 
visualization, writing – original draft. Mysara Eissa 
Mohyaldinn: conceptualization, supervision, 
writing – review & editing. Muhammad Jawad 
Khan: validation, formal analysis, software, writing 
– original draft. Fahd Saeed Alakbari: data 
curation, methodology, software, writing – original 
draft, writing – review & editing. 
Funding statement  
 The authors declare that they have no 
known competing financial interests or 
personal relationships that could have 
influenced the work reported in this paper.  
Competing interest 
The authors declare that they have no known 
competing financial interests or personal 
relationships that could have appeared to influence 
the work reported in this paper. 
The use of AI or AI-assisted technologies 
The author(s) used Deepseek Copilot to assist. 
After using this tool, the authors review and edit 
the content as needed and take full responsibility 
for the publication's content. 
GLOSSARY OF TERMS AND SYMBOLS 
 
Terms & 
Symbols Definition Unit 
EVR Erosional Velocity 
Ratio 
Dimensionless 
Vsg Superficial gas 
velocity 
m/s 
Vsl Superficial liquid 
velocity 
m/s 
Ve Erosional velocity 
(API RP 14E) 
m/s (or ft/s) 
ρm Mixture fluid density kg/m³ (or 
lb/ft³) 
ρg Gas density kg/m³ 
ρl Liquid density kg/m³ 
Usg Superficial gas 
velocity used in 
OLGA/API equation 
m/s 
Usl Superficial liquid film 
velocity 
m/s 
Usd Superficial liquid 
droplet velocity 
m/s 
C API RP 14E erosion 
constant 
Dimensionless 
D Pipe diameter inch 
P Operating pressure psi 
T Operating temperature °C 
ṁ (Mass 
flow) 
Total mass flow rate kg/s 
RSM Response Surface 
Methodology 
— 
DOE Design of Experiments — 
BBD Box–Behnken Design — 
CCD Central Composite 
Design 
— 
OLGA Dynamic multiphase 
flow simulation 
software 
— 
API RP 
14E 
American Petroleum 
Institute 
Recommended 
Practice for erosional 
velocity 
— 
ANOVA Analysis of Variance — 
CFD Computational Fluid 
Dynamics 
— 
ANN Artificial Neural 
Network 
— 
OFAT One-Factor-at-a-Time 
analysis 
—

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
504 I DOI org/10.29017/scog.v49i2.2078 
REFERENCES  
Adalarasan, R., Santhanakumar, M. & Rajmohan, 
M., (2015), Application of Grey Taguchi -based 
response surface methodology (GT -RSM) for 
optimizing the plasma arc cutting parameters of 
304L stainless steel. The International Journal 
of Advanced Manufacturing Technology ,  78 , 
1161-1170. https://doi.org/10.1007/s00170-014-
6744-. 
Al Shalabi, E. W., (2014), Modeling the effect of 
injecting low salinity water on oil recovery from 
carbonate reservoirs, Emad W. Al 
Shalabi.https://doi.org/10.2523/IPTC-17244-M: 
Al Wardi, K. H. M. S., (2020), Crude Oil 
Characterization, Hydraulic Analysis and 
Process Optimization of Real Case Study in 
Omani Oil Field, Sultan Qaboos University 
(Oman). 
Alakbari, F. S., Mohyaldinn, M. E., Mahmood, S. 
M., Hassan, A. M., Ashena, R. & Al -Fakih, A., 
(2025), A Statistics -Based Correlation for the 
Assessment of Water -Based Mud Performance: 
Yield Point Prediction. Arabian Journal for 
Science and Engineering,  50 ,  4927-4942. https://
doi.org/10.1007/s13369-024-09415-. 
Alim, M., Lee, J. -H., Akoh, C., Choi, M. -S., Jeon, 
M.-S., Shin, J. -A. & Lee, K. -T., (2008), 
Enzymatic transesterification of fractionated 
rice bran oil with conjugated linoleic acid: 
Optimization by response surface methodology. 
LWT-Food Science and Technology ,  41 ,  764-
770. https://doi.org/10.1016/j.lwt.2007.06.00. 
Asghar, A., Abdul Raman, A. A. & Daud, W. M. a. 
W., (2014), A comparison of central composite 
design and Taguchi method for optimizing 
Fenton process. The scientific world journal , 
2014,  869120. https://
doi.org/10.1155/2014/86912. 
Auni, N. R., Afdhol, M. K., Fikri, M. R. & 
Erfando, T., (2023), Potensi Polimer Sintetik 
Sebagai Bahan Chemical Enhaced Oil Recovery 
Untuk Meningkatkan Sweep Efficiency pada 
Skala Pengujian Laboratorium. Lembaran 
publikasi minyak dan gas bumi,  57 ,  9-21 . 
Bashir, I., Inam, S., Sana -Ul-Hussnain, M., Shafee, 
I., Aijaz, M., Ullah, R., Haider, M., Qureshi, H., 
Khan, M. & Ahmad, H., (2024), Erosion 
Mitigation During Testing of High 
Deliverability Gas Well -A Case Study.  
International Petroleum Technology 
Conference. IPTC, D031S135R001.https://
doi.org/10.2523/IPTC-23511. 
Bourgoyne Jr, A., (1989), Experimental study of 
erosion in diverter systems due to sand 
production.  SPE/IADC Drilling Conference 
and Exhibition, . SPE, SPE -18716-MS.https://
doi.org/10.2118/18716-M. 
Ceylan, H., Kubilay, S., Aktas, N. & Sahiner, N. 
(2008), An approach for prediction of optimum 
reaction conditions for laccase -catalyzed bio -
transformation of 1 -naphthol by response 
surface methodology (RSM). Bioresource 
technology,  99 ,  2025-2031. https://
doi.org/10.1016/j.biortech.2007.03.01. 
Chang, A., Dong, Q., Zhang, J., Shao, M. & Vafai, 
K., (2025), Investigation of the erosion wear 
mechanism of bend pipes for the action of 
 
RMSE Root Mean Square 
Error 
Same as 
response 
(EVR) 
MAE Mean Absolute Error Same as 
response 
(EVR) 
R² Coefficient of 
determination 
Dimensionless 
Adjusted 
R² 
Adjusted coefficient of 
determination 
Dimensionless 
Predicted 
R² 
Predicted coefficient 
of determination 
Dimensionless 
COV Coefficient of 
Variation 
% 
Std. Dev. Standard deviation Same as 
response 
η Response variable in 
the RSM equation 
(EVR) 
Dimensionless 
f(x) Unknown response 
function 
— 
x₁, x₂, …, 
xₙ 
Predictor 
(independent) 
variables 
Variable-
dependent

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 505 
multiphase flow in CO2 flooding industry. 
International Journal of Numerical Methods for 
Heat & Fluid Flow,  35 ,  2264-229 . 
Chen, X., Mclaury, B. S. & Shirazi, S. A., (2006), 
Numerical and experimental investigation of the 
relative erosion severity between plugged tees 
and elbows in dilute gas/solid two -phase flow. 
Wear,  261 ,  715-729. https://doi.org/10.1016/
j.wear.2006.01.02. 
Dawud, E. R. & Shakya, A. K., (2019), HPLC -
PDA analysis of ACE -inhibitors, 
hydrochlorothiazide and indapamide utilizing 
design of experiments. Arabian Journal of 
chemistry,  12 ,  718-728. https://doi.org/10.1016/
j.arabjc.2014.10.05. 
Deng, L. & Cai, C., (2010), Bridge model updating 
using response surface method and genetic 
algorithm. Journal of Bridge Engineering ,  15 , 
553-564. https://doi.org/10.1061/(ASCE)
BE.1943-5592.000009. 
Deng, Y., Liu, Y., Chen, J. & Zhang, Y. Numerical 
simulation of the erosion in the 90 elbow.  AIP 
Conference Proceedings, (2013), American 
Institute of Physics, 671 -683.https://
doi.org/10.1063/1.481692. 
Derdour, F. Z., Kezzar, M. & Khochemane, L., 
(2018), Optimization of penetration rate in 
rotary percussive drilling using two techniques: 
Taguchi analysis and response surface 
methodology (RMS). Powder technology ,  339 , 
846-853. https://doi.org/10.1016/
j.powtec.2018.08.03. 
George, I. S., Orji, C. U. & Douglas, I. E., (2024), 
Flow assurance analysis in Front End 
Engineering Design (FEED) of Subsea Flowline 
and Riser.https://doi.org/10.30574/
wjarr.2024.22.2.150.  
Ghomian, Y., (2008), Reservoir simulation studies 
for coupled carbon dioxide sequestration and 
enhanced oil recovery, The University of Texas 
at Austin. 
Ghorbani, D., (2008), Development of 
methodology for optimization and design of 
chemical flooding, The University of Texas at 
Austin. 
Grant, G. & Tabakoff, W., (1975), Erosion 
prediction in turbomachinery resulting from 
environmental solid particles. Journal of 
Aircraft,  12 ,  471-478. https://
doi.org/10.2514/3.5982. 
Hong, B., Li, Y., Li, X., Ji, S., Yu, Y., Fan, D., 
Qian, Y., Guo, J. & Gong, J., (2021), Numerical 
Simulation of Gas-Solid Two-Phase Erosion for 
Elbow and Tee Pipe in Gas Field. Energies ,  14 , 
6609. https://doi.org/10.3390/en14206609https://
doi.org/10.3390/en1420660. 
Khor, S., Limpasurat, B., Zhang, M. & Graa, I., 
(2023a), Integrated Pore -to-Process Modelling 
Approach for Confident Decision -Making in 
Field Development of a Complex Onshore Gas -
Condensate Asset in the Middle East.  Abu 
Dhabi International Petroleum Exhibition and 
Conference. SPE, D041S130R006.https://
doi.org/10.2118/216864-M: 
Khor, S. H., Limpasurat, T., Zhang, M. Q. & Graa, 
I., (2023b), Unlocking Ultimate Values of a 
Complex Gas -Condensate Light -Oil Asset in 
the Middle East with Integrated Pore -to-Process 
Solutions.  International Petroleum Technology 
Conference. IPTC, D012S003R002.https://
doi.org/10.2523/IPTC-23062-M. 
Liang, C., Xiong, W., Wang, H., Carriveau, R., 
Ting, D.-K. & Wang, Z., (2023a), Identification 
of slug flow in underwater compressed gas 
energy storage pipeline using pressure signals.  
IET Conference Proceedings CP833. IET, 7 -
14.https://doi.org/10.1049/icp.2023.154: 
Liang, C., Xiong, W., Wang, H. & Wang, Z.,
(2023b), Experimental and OLGA Modeling 
Investigation for Slugging in Underwater 
Compressed Gas Energy Storage Systems. 
Applied Sciences,  13 ,  9575 . 
Marbun, M., Nijusiho Manik, S. & Karim, A. G., 
(2025), Analisis Pengaruh Temperatur, pH dan 
Laju Alir Terhadap Pembentukan Scale. 
Lembaran Publikasi Minyak dan Gas Bumi,  59 , 
11-20 . 
Myers, R. H., Montgomery, D. C. & Anderson -
Cook, C. M., (2016), Response surface 
methodology: process and product optimization

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 487-507 
 
506 I DOI org/10.29017/scog.v49i2.2078 
using designed experiments, John Wiley & Sons 
Nadeem, A., Vieira, R. E. & Shirazi, S. 2025. Sand 
detection using acoustic sand monitors for 
liquid-dominated multiphase flow production. 
SPE Journal,  30 ,  210-224 . 
Obiomah, F., (2025), Pipeline Transportation of 
Hydrocarbons.  
Onyegiri, I. E., Briggs, T. A. & Ekwe, E. B., 
(2020), Investigation of the effects of flowline 
sizes, flow rates, insulation material, type and 
configuration on flow assurance of waxy crude. 
Innovative Systems Design and Engineering , 
11. https://doi.org/10.7176/ISDE/11-3-0. 
Osman, A., El-Shaib, M., Shehata, A. & Shehadeh, 
M., (2025), Advancing Pipeline Integrity: An 
Experimental Investigation into Acoustic 
Emission Monitoring of Erosion -Corrosion 
Mechanisms. Results in Engineering,  108820 . 
Othman, N. T. A., Putra, Z. A., Abidin, S. a. Z. & 
Ali, F. I. M., (2023), CFD analysis of erosion 
rate in oil and gas pipeline industry. Jurnal 
Teknologi (Sciences & Engineering) ,  85 ,  59-
66. https://doi.org/10.11113/
jurnalteknologi.v85.2047. 
Othman, N. T. A., Putra, Z. A., Abidin, S. a. Z. & 
Ali, F. I. M., (2024), Integration of CFD 
analysis and artificial neural networks for 
estimation of erosion rate in oil and gas 
pipelines. Results in Engineering ,  24 , 
103288. https://doi.org/10.1016/
j.rineng.2024.10328. 
Parsi, M., Al -Sarkhi, A., Kara, M., Sharma, P., 
Mclaury, B. S. & Shirazi, S. A., (2017), A new 
dimensionless number for solid particle erosion 
in natural gas elbows. Wear ,  390 ,  80-83. https://
doi.org/10.1016/j.wear.2017.07.00. 
Peters, A. E., Charlesugochukwu, O. & Samson, N. 
Parametric Analysis of Subsea Multiphase 
Pipeline.  
Peters, A. E., Charlesugochukwu, O. & Samson, 
N., (2022), Parametric Analysis of Subsea 
Multiphase Pipeline. 2022. 
Pleshkov, D., Corella Moya, C. A., Corella Moya, 
B. R., Ortiz, A. V. S., Paredes, L., Huaca, A., 
Chicaiza, F., Marin, G. A., Garcia, J. N., Tapia, 
R. a. V. & Rajain, A. K., (2022), Pipeline 
Transportation of Hydrocarbons. 
 Disruptive Dumpflooding Completion, Case Study 
Ecuador.  Offshore Technology Conference 
Asia. D041S029R003.https://
doi.org/10.4043/31533-m. 
Salama, M. & Venkatesh, E., (1983), Evaluation of 
API RP 14E erosional velocity limitations for 
offshore gas wells.  Offshore technology 
conference. OTC, OTC -4485-MS.https://
doi.org/10.4043/4485-M. 
Satiyawira, B., Maulani, M., Samura, L., 
Pramadika, H., Nugrahanti, A., Rosyidan, C., 
Prima, A., Arkaan, M. D. & Yanti, W., (2025), 
Drilling Fluid Optimization Using Response 
Surface Methodology. Scientific Contributions 
Oil and Gas,  48 ,  281-294 . 
Shirazi, S. A., Mclaury, B. S., Shadley, J. R., 
Roberts, K. P., Rybicki, E. F., Rincon, H. E., 
Hassani, S., Al‐Mutahar, F. M. & Al ‐Aithan, G. 
H., (2025), Erosion –Corrosion in Oil and Gas 
Pipelines. Oil and Gas Pipelines: Integrity, 
Safety, and Security Handbook,  2 ,  1078-1102 . 
Su, C., Rydahl, A. & Shea, R., (2003), Liquid 
Inventory Management in Wet Gas Pipelines.  
SPE Latin America and Caribbean Petroleum 
Engineering Conference. SPE, SPE -81177-
MS.https://doi.org/10.2118/81177-M. 
Supmea, (2023), Flow Rate And Pressure: 
Features, Relationship & Applications [Online]. 
Available: https://www.supmeaauto.com/
training/flow-rate-and-pressure#content-section- 
[Accessed 2025]. 
Svedeman, S. & Arnold, K., (1993), Criteria for 
sizing multiphase flow lines for erosive/
corrosive services. SPE 26569.  68th Annual 
Technical Conference of the Society of 
Petroleum Engineers, Houston, Texas. https://
doi.org/10.2118/26569-P. 
Tony, B., Chandra, S., Purba, R. J., Solihan, M. F. 
& Saputra, E. D., (2025), Transient Simulation 
to Analyze Wax Deposition and Flow Pattern 
Behavior Along Tubing Under Esp Installation 
and Gassy Well Condition. Scientific 
Contributions Oil and Gas ,  48 ,  91-112 . https://

Predictive Modeling of Pipeline Erosion in Multiphase Flow Using OLGA Simulation 
and Response Surface Methodology (RSM) (Alakbari et al.) 
 
DOI org/10.29017/scog.v49i2.2078  I 507 
doi.org/10.29017/scog.v48i3.1731.  
Venriza, O. & Wahyuni, C., (2024), Optimization 
of Crude Oil Transmission Process by Installing 
Electric Heat Tracing in Off -Plot Piping. 
Scientific Contributions Oil and Gas , 
LEMIGAS RD Center for Oil and Gas 
Technology,  47,  167-  175. https://
doi.org/10.29017/SCOG.47.3.1631. 
Veza, I., Spraggon, M., Fattah, I. M. R. & Idris, 
M., (2023), Response surface methodology 
(RSM) for optimizing engine performance and 
emissions fueled with biofuel: Review of RSM 
for sustainability energy transition. Results in 
Engineering,  18 ,  101213. https://
doi.org/10.1016/j.rineng.2023.10121. 
Vieira, R. E., (2014), Sand erosion model 
improvement for elbows in gas production, 
multiphase annular and low -liquid flow, The 
University of Tulsa. 
Zabeti, M., Daud, W. M. a. W. & Aroua, M. K.,  
(2010), Biodiesel production using alumina -
supported calcium oxide: An optimization 
study. Fuel Processing Technology ,  91 ,  243-
248. https://doi.org/10.1016/j.fuproc.2009.10.00.
