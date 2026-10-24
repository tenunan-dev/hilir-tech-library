---
source_id: "lemigas-scog"
title: "Enhancing Economic Resilience in Marginal Oilfields Through Discrete Event Simulation Optimization of Coiled T"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2149"
retrieved_at: "2026-10-24T14:30:20+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "397421cb445feb16a9d90e6a6303f13d6cfe4773d97cb114f0b716f4fdbbf01a"
collected: "manual"
---

# Enhancing Economic Resilience in Marginal Oilfields Through Discrete Event Simulation Optimization of Coiled T

387 
 
https://doi.org/10.29017/scog.v49i3.2149 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 387 – 410 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Enhancing Economic Resilience in Marginal Oilfields Through  
Discrete Event Simulation Optimization of Coiled Tubing Reutilization 
 
Warno* and Suharjito 
Industrial Engineering Department, BINUS Graduate Program – Master of Industrial Engineering,  
Bina Nusantara University, Jakarta 11480, Indonesia. 
*Corresponding author: Warno (warno@binus.ac.id) 
Warno: https://orcid.org/0009-0003-0518-4558 
Received:  04 March 2026; Revised: in revised form 08 May 2026; Accepted: 09 June 2026 
Available: online 30 September 2026. 
 
 
 
ABSTRACT - Coiled Tubing Gas Lift (CTGL) is an artificial lift method contributing the majority of oil 
production in marginal fields. These fields face a double challenge: reserves continue decreasing while operational 
costs tend to increase. This research aims to de velop optimization models for reutilizing coiled tubing, shifting 
from current practices where CTGL installations always use new coiled tubing materials . A Discrete Event 
Simulation (DES) mirrors current operational practices based on empirical historical data (2019-2024) from the 
mature marginal oilfield Kutai Basin,  with a target reservoir interval of 700 to 8000 ft in East Kalimantan, 
Indonesia. A baseline model (Scenario 0) and four optimization models (Scenarios 1- 4) of DES were developed 
to evaluate the most optimal strategies incorporating recycling and distinctive cutting policies. Scenario 1 
(Dynamic Recycle) emerged as the best -performing model, delivering the highest Net Present Value (NPV) of 
$58.53 million with 100% demand fulfillment; Scenario 4 (Hybrid Cut) performed equivalently but generated 
slightly more scrap, while the fixed -cut policies (Scenarios 2 –3) were operationally unviable. Compared to the 
current practice (Scenario 0), which incurs an average Coiled Tubing (CT) cost of $69,000 pe r well, Scenario 1 
improves NPV by 7.62% (~ $4.1 million), creating significant value for marginal fields to maintain profitability 
and continuity. It also drastically reduces CT consumption by 53% and metal scrap by 60% while fulfilling 100% 
of job demand. The DES approach successfully validated that recycling CT is highly viable without compromising 
operational continuity. Earlier studies on coiled tubing are related to technical and operational failure factors and 
quality of service, while this research a ddresses problems such as the permanent application of CTGL in long -
term project economies. Using DES, decision-makers can quantify the economic trade-offs of strategies without 
risk before implementation in the oil and gas industry. 
Keywords: Coiled tubing gas lift, simulation, marginal field, recycle, use and scrap. 
 
How to cite this article: 
Warno and Suharjito , 2026, Enhancing Economic Resilience in Marginal Oilfields Through Discrete 
Event Simulation Optimization of Coiled Tubing Reutiliza tion, Scientific Contributions Oil and Gas, 
49 (3) pp. 387-410.

388 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
1. Introduction 
As reservoir pressure declines naturally in mature oilfields, artificial lift methods such as gas lift are deployed 
to sustain production (Effa et al., 2019; Khalid et al., 2020; Maurenza et al., 2023). Coiled Tubing Gas Lift (CTGL) 
serves as a highly effective artificial lift, utilizing continuous tubing as a conduit to inject gas and lift wellbore 
liquids to the surface (Suharjito & Warno 2025). CTGL has proven an essential artificial lift solution for marginal 
fields, successfully reviving non -economic wells in Pakistan and doubling production in the Wafa field by 
countering declining pressures without expensive workovers (Khalid et al., 2020;  Kolawole et al., 2020;                                            
Sherik et al., 2019).  
Despite these operational benefits, CTGL applications face significant technical and economic hurdles. While 
coiled tubing offers practicality and safety advantages over jointed tubing (Alagoz & Tali 2023; Wiranata et al., 
2020), its deployment involves repeated bending that induces plastic-elastic deformation and fatigue failure over 
time (Shaohu et al., 2019;  Tong & Gao 2019) . These structural vulnerabilities are further accelerated by high 
internal pressures, tensile loads, mechanical strain, and corrosion (Hagianu et al., 2020; Shaohu et al., 2020; Yan 
et al., 2021). Although previous studies have examined these failure mechanisms using inspection methods such 
as magnetic flux testing (Long et al., 2020; Zhou et al., 2020), rising material costs and the lack of a standardized 
method to verify the integrity of retrieved coiled tubing for reuse remain critical challenges for sustainable long -
term installations. To navigate this complex trade-off between the technical uncertainties of reused tubing and the 
economic necessity of lowering installation costs, decision -makers require a robust modeling tool capable of 
simulating dynamic operational variables.  
While traditional analytical methods struggle to capture the dynamic complexity of  inventory management 
under stochastic demand, Discrete Event Simulation (DES) offers a robust framework for modelling  these 
uncertainties. Therefore, this study utilizes DES to bridge the gap between technical asset management and long-
term economic plann ing. Simulation models are fundamental decision support tools to design mathematical 
representations of complex stochastic systems for short - and long-term strategic planning (Marshall et al., 2020; 
Ordu et al., 2021) . DES is widely applied to model, evaluate, and optimize cascading decisions across various 
sectors by representing operations as sequences of discrete events (Ala & Chen 2020) . These models manage 
uncertainty in dynamic environments, supporting decision -making in logistics (Coelho et al., 2021) , complex 
transportation planning (de la Torre et al., 2021) , sustainable space planning (Okeke 2020) . Hybrid models 
integrating DES with forecasting and optimization have become increasingly popular for resource allocation and 
capacity planning, such as in healthcare systems (Ordu et al., 2021; Teles 2024; Wikman-Jorgensen et al., 2024).  
Beyond broad capacity planning, DES is a robust methodology for evaluating specific operational 
improvements, scheduling, and maintenance scenarios (Golbasi & Turan 2020) . For instance, DES has been 
used to compare st ochastic programming for offshore flight scheduling (Bastos et al., 2020) , assess lean 
construction principles (Al-Zqebah et al., 2022;  Bajjou & Chafi 2021) . Crucially, DES is widely applied to 
inventory management; tools like Arena simulation can model complex supply chains to reduce shortages 
(Arani et al., 2020)  and determine optimal stock levels (Mitrovi et al., 2021) . Simulation -based methods have 
been shown to significantly lower average inventory costs and volumes, improving overall management 
efficiency (Chen et al., 2022) . 
While the Oil and Gas (O&G) indust ry is increasingly adopting Industry 4.0 technologies and lean 
management frameworks to navigate market volatility and improve predictive maintenance (Elijah et al., 2021;  
Shou et al., 2021), DES applications in this sector remain limited. Despite DES's widespread success in modeling 
complex systems in other industries, existing coiled tubing literature primarily addresses isolated technical issues 
such as fatigue and corrosion failure mechanisms and fails to integrate these insights with long -term economic 
sustainability in marginal fields. This fragmented approach creates a critical research gap by overlooking DES's 
potential as a comprehensive dig ital twin framework that can optimize  the full asset lifecycle, including 
operational risks, maintenance strategies, and economic trade-offs.  
In a marginal oilfield context, the company relies on Coiled Tubing Gas Lift (CTGL) to support its 
production tar gets. From 2019 to 2024, CTGL deployment reached 283 installations, while 127 installations

389 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
were retrieved due to well depletion or equipment failure. The current operational practice dictates discarding 
these retrieved Coiled Tubing (CT) materials, genera ting massive metal scrap and highly inefficient inventory 
costs. With installation costs between 70 and 100 thousand USD, CT materials account for 30 to 50% of the 
total. This "use-and-dispose" approach exacerbates the economic challenges of mature fields,  creating a critical 
need for asset reutilization.  
To address this operational inefficiency, this research introduces a novel approach by shifting Coiled Tubing 
Gas Lift management from a linear 'use -and-dispose' model to a circular asset management framework. Unlike 
previous literature that focuses more on technical failures, this study aims to develop a DES model to optimize 
the entire lifecycle of CT reutilization. By utilizing Arena simulation software to replicate real -world process 
flows under stochastic conditions, this research provides a quantifiab le, risk -free methodology to evaluate 
dynamic cutting and inventory replenishment strategies (Lestari et al., 2022), effectively bridging the gap between 
field operations and long-term economic sustainability. 
The secondary objective is to evaluate the economic impact of these optimization strategies through cost -
benefit analysis, specifically using Net Present Value (NPV). Reutilizing coiled tubing offers a significant 
opportunity to reduce installation costs by approximate ly $20,000 to $30,000 per well. Ultimately, this research 
provides a sustainable alternative that not only minimizes waste and inventory costs but also ensures long -term 
operational resilience, thereby improving individual project feasibility and extending  the economic life of 
marginal oilfields. 
 
2. Methodology 
The sequence of the research methodology is mapped out in Figure 1 , which details the flowchart of the 
research stages from literature study through problem definition, data collection, and model validation. 
 
 
 
Figure 1.  
Research flowchart for DES coiled tubing reutilization.

390 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
2.1 Data collection and descriptive characteristics 
This study uses a historical dataset from a mature marginal oilfield in the Kutai Basin, with a reservoir depth 
of 700–8000 ft, operating  in East Kalimantan, Indonesia. These historical data  cover CTGL installations from 
2019 to 2024 and serve  as empirical inputs for the simulation. Using these data ensures the model reflects real -
world process flows  and stochastic conditions, identifying valid optimization opportunities without relying on 
hypothetical data. 
Table 1 Summarized data required for simulation and optimization. Historical data show that installations are 
evenly distributed, demonstrating that CTGL represents an integral and sustained operational policy. In contrast, 
the number of retrievals is much lower than installations during the same period, reflecting that they are not 
integrated into a systematic reuse & cycle strategy, which this research proposes to address. 
Furthermore, CTGL installations require coiled  tubing lengths ranging  from 750 to 8200 ft. Operational 
reasons suggest leaving around 300 to 1000 ft in the drums to support operational practicability and safety.  Based 
on quartile-based analysis, the majority of CTGL installations require 4000 ft or less (81%), while installations 
requiring >7000 ft represent only 3% of the population. Therefore, with a requirement of 1000 ft left on the drum, 
coiled tubing length is segmented into 7 classes ranging from 1000 to 7000 ft, with a 1000 ft increment for each 
class. For example, class 1 is 1000 ft CT length, class 2 is 2000 ft CT length, and so on until class 7 is CT length 
> 7000 ft. This segmentation reflects actual field conditions and provides a simplified framework for simulation 
input, inventory management, and operational decision -making, e.g., for class downgrades when ex -used coiled 
tubing is included in inventory for the next installation. 
2.2 Data preparation and distribution fitting 
Distribution analysis of statistical data is essential to understand population behavior based on historical data 
as input for simulation. The simulation input dataset is stochastic, consisting of installation interval distri bution 
as incoming job orders , retrieval range distribution, and production lifetime distribution. To ensure the data is 
statistically valid for simulation, we conduct a three-step validation process.  
The first step is to check whether the dataset follows  a normal distribution  (Bayoud 2021). This is done in 
Minitab using the Anderson-Darling test, with the null hypothesis (H₀) that the data follow a normal distribution. 
If the resulting p-value is less than a chosen signific ance level (0.05), reject the H0 hypothesis and conclude the 
data is not normal (H1). Darling-Anderson Equation 1: 
                                          (1) 
while,  
                    (2) 
where n, Y i, and F(Yi), are the number of observations in the sample,  the i th observation, and the cumulative 
distribution function (CDF) of the normal distribution for the value Yi, respectively. 
If the data does not follow a normal distribution, the second step is to identify the best-fit statistical distribution 
it does follow. This is accomplished using tools like the Input Analyzer embedded in Arena simulation software. 
This tool automatically tests the historical data against various theoretical distributions (suc h as Weibull, 
Lognormal, or Exponential) and ranks them to suggest the most appropriate model to use as an input parameter 
for the simulation.  
The final step is to validate the chosen best-fit distribution normally. This is done using goodness-of-fit tests 
like the Chi -Square (X 2) or Kolmogorov -Smirnov (K -S) test (Tezel et al., 2021) . For these tests, the null 
hypothesis (H₀) is that the historical data follow the selected theoretical distribution. If the p -value > 0.05, we 
accept the model, as it indicates there is no statistically significant difference between the historical data and the 
(1) 
(2)

391 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
theoretical distribution. The Chi-Square test compares observed (Oi) and expected (Ei) data frequencies, while the 
K-S test finds the maximum difference (D) between the data's cumulative shape and the theoretical distribution's 
shape. The Chi-Square statistics are calculated as Equation 3: 
                                      
where: k, Oi, and Ei, are the number of categories, The Observed frequency of data in the i th category, and The 
Expected frequency of data in the ith category, according to the distribution, respectively. The K-S statistic (D) is 
the maximum vertical distance between the two functions: 
                       
where Fn(x) = The Empirical CDF, which is a step function at any value x; it represents the proportion of data points 
that are less than or equal to x. F(x) is the theoretical CDF of the distribution being tested (e.g., Weibull, Lognormal). 
2.3 Production forecasting methods 
Project evaluation tool is NPV of CTGL installation cost against revenue. Revenue is defined as oil production 
from CTGL installation. The production data in Figure 2 shows two main trends happening at the same time. First, 
there's an overall declining trend, where the peaks of production are gradually getting lower each year, indicating 
the overall trend tends to show a gradual decline over the years, reflecting the natur al depletion of reservoir 
pressure. Second, the field exhibits a strong annual seasonal pattern, with predictable drops in production near the 
start of every year. This pattern is driven by the operational cycle of workover campaigns, where, at the end of 
the year, there is cumulative installation of CTGL and natural decline phenomena. 
In the oil and gas industry, production forecasting is technically challenging because it depends on reservoir 
properties, tubing performance, surface production facilities p erformance, and other  production methods 
involving artificial lift. Different approaches had been widely used for production forecasting handling data with 
trends such as linear regression (Alharbi et al., 2022)  and Winter’ s Holt (Sibuea et al., 2022) , decline curve 
forecasting (Maurenza et al., 2023b; Nguyen & Chan 2005; Tadjer et al., 2021; Thakuria et al., 2019), exponential 
smoothing, moving average and Arima (Ning et al., 2022;  Singh & Pateriy a 2019). In this research, three 
approaches for oil production forecasting are fitted to annual historical data: Moving Average, Holt's (double 
exponential), and Decline Curve Forecasting (DCF), an industry-standard artificial-lift oil production method.  
Forecasting accuracy is defined by the smallest Mean Absolute Percentage Error (MAPE) as the decision 
metric. Before forecasting, the original data is normalized yearly to avoid bias from monthly noise accumulation. 
The forecasting methods will follow the formulation of each method. 
 
Table 1.  
Historical data CTGL installation. 
Data Type 2019 2020 2021 2022 2023 2024 
 
Installation (Job) 44 46 51 50 42 50  
CT Length Installed - ft 102,009 104,741 111,478 142,150 115,670 148,600  
Retrieval (Job) 34 28 14 28 16 7  
CT Length Retrieved - Ft 78,609 55,170 31,245 56,477 42,320 11,450  
Production average from CTGL (bbl/day) 2,275 2,034 1,681 1,829 506 1,072  
Production/ctgl (bbl/day) 51.7 44.2 33.0 36.7 12.1 21.4  
(3) 
(4)

392 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
Figure 2.  
Depletion trends: CTGL’s production contribution based on historical data 2019 to 2024. 
 
 
 
• Holt methods (double exponential) 
Level (Lt): Estimate value at the current time point: 
              
Trend (Tt): Estimate the rate of change (slope):  
                 
Forecast (Ft+m): Forecast for the following year: 
                              
α, β are the smoothing parameters (between 0 and 1) that the model optimizes;  At is Actual production 
at time t; m is the number of periods of forecasting. 
• Simple moving average (SMA2) 
                                  
where Ft+1, At, and At-1 are the forecast for the following year , Actual Production , and Production last  
year, respectively . 
• Decline curve forecasting (DCF) 
Exponential as lower case (b=0): 
                                        
Hyperbolic as artificial lift forecast (b = 0.5): 
                           
(5) 
(6) 
(7) 
(8) 
(9) 
(10)

393 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Harmonic (b=1) as upper case: 
                                         
where b, Qi, Di, and t, are Arps exponent, Initial production t, Decline rate yearly (%), and corresponding   
year, respectively. 
2.4 Discrete event simulation (DES) model development 
Arena simulation is utilized to develop a Discrete Event Simulation (DES) model for CTGL installation and 
replenishment. The primary goal is to evaluate alternative scenarios against current practices to optimize coiled 
tubing reutilization, maximize cost -benefits, and minimi ze material waste . The proposed models optimize CT 
reutilization by inspecting retrieved materials to determine usability, as illustrated in the framework in Figure 3, 
as follows:  
• Scenario 0 (Baseline): Represents the current "a s-is" practice where all retrieved CT is scrapped, and job 
demand is met entirely by dynamically cutting new 20,000 ft rolls. Inventory replenishment is only from new 
CT material purchased to meet job demand. This system operates with a "take and cut" proc edure, where 
resources (new rolls) are considered unlimited, and remaining material is considered unrecoverable. 
• Scenario 1 (Dynamic Recycle): The primary optimization strategy where successfully inspected CT is 
downgraded by one class to serve as prioritized inventory for incoming jobs.  
• Scenario 2 (Fixed Cut 4k): Tests a rigid inventory policy by pre -cutting each new roll into five fixed 4,000 
ft lengths 
• Scenario 3 (Fixed Cut 4k and 8k): Modifies the fixed-cut strategy by pre-cutting new rolls into three 4,000 ft 
pieces and one 8,000 ft piece.  
• Scenario 4 (Hybrid Cut): Refines the dynamic approach by using standardized 4,000 ft cuts for smaller jobs 
while cutting larger jobs dynamically. 
2.5 Cost-benefit and sensitivity analysis 
Profitability of this project will be evaluated using NPV as the financial metric for cost-benefit analysis. NPV 
is used to assess potential return by comparing current model (scenario 0) against proposed model (Scenario 1-4). 
NPV is described in Equation 12.  In this simulation, cash flow is oil production revenue, while investment cost 
is derived from material and operational costs under  different scenarios. The NPV evaluation input is obtained 
from production forecasting and simulation results during the years of the project. 
                  
Some conditions for this simulation are assumptions due to limitations and simplifications. This simulation is 
based on assumptions such as a coiled tubing inspection pass threshold of 90% based on field best practice, a 
Hurdle NPV of 46.04 MUSD over six years, an oil price  of 60 USD/bbl, a discount rate of 10.22%,  and t years. 
This assumption is made based on company policy to project investment evaluation. Material cost for recycled 
coiled tubing is zero because holding inventory cost assumes no additional resources are re quired, no space 
limitations, and No Scrap handling is considered in this research, as  shown in Table 2. The financial figures in 
this analysis are based on a standard industry cost structure and normalized historical data to reflect the economic 
trade-offs of the scenarios.   
The cost differential between the two columns follows the procurement basis of each line item rather than a 
uniform discount. Coiled Tubing Material is booked at zero for reused CT because the string is alrea dy owned; 
its handling is absorbed within the Service Charge, which is why that line is unchanged. Surface Equipment falls 
from $11,182 to $1,326 because a reused installation requires only re-dressing and recertification of components 
(11) 
(12)

394 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
already held in inventory, whereas a new installation is charged the full procurement value of those components. 
Bottom Hole Assembly falls by a smaller margin, from $5,940 to $3,100, because only part of the assembly is 
recovered intact; consumable and sealing elements are r eplaced at every installation regardless of the string's 
origin, which sets a floor on the achievable reduction. Personnel Cost is identical because the same crew and 
duration apply in both cases. 
Because cost-benefit analysis comes with inherent uncertain ties, sensitivity analysis is used to evaluate and 
determine the impact of results and understand variation due to uncertainty. Purpose of sensitivity is to evaluate 
the responds of models against parameters change, identify the weakness and benefit of the  model, and provide 
more realistic decision making in optimization model (Menberg et al., 2016;  Usher et al., 2023) . Three main 
parameters measure the sensitivity of simulation results to real -world uncertainty relevant to this project: oil 
price, production forecast, and material cost increments to anticipate market volatility. A Monte Carlo 
simulation of 10,000 itera tions was constructed to evaluate the financial robustness of the models. Each of the 
three parameters was varied around its base case using an independent triangular distribution, whose bounds 
were derived from a distinct source. The production forecast b and was set based on the accuracy of the selected 
forecasting method. The oil price band was derived from the historical volatility of the realized selling price 
over the 2019 to 2024 dataset period, around the base case of $60/bbl. The CT material cost ba nd reflects 
anticipated supply -chain inflation, tested up to a 20% increment applied from the fifth project year. The bounds 
applied were therefore -50% to +200% on the production forecast, $45 to $100 per barrel on the oil price, and 
0 to +20% on the CT m aterial cost.   
 
Table 2. 
Cost structure with new and reused CT. 
Cost component Installation with new CT Installation with reused CT  
Surface Equipment $ 11,182 $ 1,326  
Bottom Hole Assembly (BHA) $ 5,940 $ 3,100  
CT Material (3000 ft) $ 26,370 -  
Personnel Cost $ 4,025 $ 4,025  
Service Charge $ 21,450 $ 21,450  
Total Cost $ 68,967 $ 29,901  
 
 
Table 3.  
Normality testing and distribution fitting results. 
Process Step Installation Time to failure (production life) Retrieval 
Data Characteristics N :282, μ: 7.75, 
Median: 6.00, σ: 7.08 
N :318, μ:591.1, 
Median:335.0, σ: 653 
N :126, μ:16.57, 
Median:8.50, σ: 2.88 
Normality Test 
(Poisson Fit) 
Chi-Square p: 0.000 
Anderson-Darling p< 0.05 
Skew:1.54 
Chi-Square p:0.000 
Anderson-Darling p < 0.05 
Skew:1.64 
Chi-Square p 0.000 
Anderson-Darling p < 
0.05 
Skew:2.88 
Best-Fit Distribution 
with input analyzer 
-0.5 + GAMM (5.98, 1.38) 
Sq.Error: 0.0046 
-0.001 + LOGN (821, 
2.11e+03) 
Sq.Error: 0.00245 
-0.001 + WEIB (14.9, 
0.817) 
Sq.Error: 0.00145 
Conclusion (Chi-Square 
p > 0.05) 
Chi-Square p-value: 0.0625. Chi-Square p-value: 0.1500 Chi-Square p-value: 
0.1690

395 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
Figure 3.  
DES framework for Current Practice (Scenario 0) compared to Proposed Optimization Scenario (Scenario 1–4). 
 
 
 
3. Result and analysis 
3.1 Data distribution and production forecast 
To construct a reliable simulation, the historical operational datasets required statistical distribution fitting. 
The normality tes ts showed that all three historical datasets were not normally distributed, as evidenced by an 
Anderson-Darling test 𝑝 < 0.05. Therefore, Arena's Input Analyzer was utilized to find the best fit based on 
minimum square error criteria. The installation data best fit a Gamma distribution, the time -to-failure data best 
fit a Lognormal distribution, and the retrieval data best fit a Weibull distribution. These goodness -of-fit results, 
summarized in Table 3, provide valid stochastic inputs for the simulation models.  
Evaluating the cost -benefit analysis requires an accurate projection of the production contribution from 
Coiled Tubing Gas Lift (CTGL). The normalized historical dataset displayed a downward trend, which aligns 
with marginal field behavior where the reservoir is naturally depleted, and artificial lift is utilized for 
recovery. Figure 4  illustrates the forecasting results comparing Moving Average, Holt's double exponential, 
and Decline C urve Forecasting (DCF). DCF outperformed the other methods with the lowest Mean Absolute 
Percentage Error (MAPE) of 6.1; therefore, its results are used as the revenue reference for the Net Present 
Value calculations .

396 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
 
 
 
                            
Figure 4.  
Comparison of Production Forecasting Methods using:  
(a) Moving average; (b) Holt’s double exponential; (c) Decline curve forecasting (DCF). 
a). 
b). 
c).

397 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
3.2 Baseline simulation model and validation 
The baseline DES model (Scenario 0) is developed as a digital twin of the current process, where coiled tubing 
installation and retrieval are  conducted without considering coiled tubing reutilization of CT retrieved from the 
well. Figure 5 shows the developed model using Arena 16.2 without recycling loops for CT material, to measure 
the extent of cost and waste before any process improvements are made. Simulation inputs are taken from data 
distributions fitted as stochastic conditions, coiled tubing class segments, and simulation  parameters to mirror 
real-world flow processes. The simulation flow chart and logic are described as follows: 
• Part A (Job Order & Classification): Acts as the system generator. Job arrivals are generated stochastically 
based on the fitted Gamma distribution, and each job is assigned a required CT length class (Class 1 to 7). 
• Part B (Installation Decision Flow): In the baseline model, job installation uses only new coiled tubing.  
• Part C (Retrieval of Installation): Simulates the CT lifecycle.  In the baseline model, the system follows a 
linear "take and cut" procedure: retrieved CT is immediately scrapped, and new jobs are fulfilled only by 
cutting from new CT rolls.  
• Part D (Retrieval of Existing Backlog): Models the depletion of the initial 207 historical installations, feeding 
them into the inspection module (Part C) to simulate real-world starting conditions. Several essential stochastic 
parameters derived from historical data control the system's behavior, including the job arrival rate (λjob), the 
time a Coiled Tubing unit remains in a well before failure (Tin_well), and the frequency of retrieval operations 
(Tretrieval). The simulation evaluates discrete strategic alternatives (Scenarios 0 to 4) by measuring the impact 
on key performance indicators (KPIs) such as New Coiled Tubing Rolls and Scrap generated. Table 4. 
Illustrates the simulation parameters used in this research. 
 
 
 
 
 
Figure 5.  
Baseline DES model in arena software representing the current linear 'Use-and-Dispose' practice (Scenario 0).

398 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Table 4.  
Simulation parameters. 
Element Name Description 
Entity JobOrder Represents a new installation request. 
 ExistingCT Represents a retrieved unit from the initial 207 CTGL 
backlog. 
Attribute RequiredClass The length class (1-7) needed for a job. 
 RequiredLength The specific length in feet for a job. 
 OriginType A tag (1=New Installation, 2=Existing CT) to 
distinguish the source of a retrieved CTGL 
 isRecycled A flag (1 or 0) to track if a recycled CT was used for an 
installation (Applied to Scenarios 1-4). 
Variables JobsCount Counter for total installations completed. 
 RetrievalsCount Counter for total retrieval operations performed. 
 ExistingRetrievedCount Counter for retrievals from the initial backlog only 
(Max 207 CTGL Installations) 
 NewRollsUsed Counter for new 20,000 ft rolls consumed. 
 UsedLengthTotal Sum of all installed CT lengths. 
 ScrapFromNewRoll Sum of scrap generated from new material. 
 ScrapFromRecycle Sum of scrap generated from retrieved/recycled 
material. 
 InspectionPassCount Counter for CTs that pass inspection (Applied to 
Scenario 1-4). 
 
 
Table 5.  
Validation of Baseline Model (Scenario-0). 
Key performance index (KPI) Simulation (Average) Actual data T-Test 
Installation  284.3 283 p:0.992 
Retrieval  132.9 127 p:0.935 
 
Before proceeding to the next step of the simulation, validate the model to evaluate whether it  represents the 
real-world system. Validating a simulation model is essential to ensure outputs are reliable and to avoid ineffective 
decisions. Model validation is achieved by comparing simulation results with historical data to confirm the model's 
accuracy. The significant difference between the two is evaluated using a t-test. This significance test is essential 
to proceed to the next step: an alternative simulation model for optimization. 
Table 5 shows the simulation result aga inst six years of historical data. The simulation, acting as a virtual 
timeline, projected an average of 284.3 installations and 132.9 retrievals, closely mirroring the actual historical 
counts. A two -sample T -test confirmed the accuracy, with p -values of 0.992 for installations and 0.935 for 
retrievals, both well above the p-value 0.05 threshold. This statistical alignment confirms the simulation model is 
valid and its outputs are reliable for strategic decision-making. 
3.3 DES optimization scenarios  
The simulation evaluates Scenario 0 against four alternative models (Scenarios 1 –4) designed to introduce a 
CT reutilization process, which differ primarily in their cutting strategies as optimization models. The fundamental 
logic behind these optimization scenarios is to transform retrieved CT from recycle into a high-priority inventory 
source. Figure 6  illustrates the process flow modeled in Arena software  Figure 6  illustrates the process flow

399 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
modeled in Arena software, using Scenario 1 as the representative simulation. Job arrivals (Part A) and existing 
retrievals (Part D) function identically to the baseline model. The critical optimization occurs in Part C, where 
retrieved CT undergo an inspection process. Passing CT are downgraded by one class and routed into the system 
as recycled inventory. For example, CT class 3 with length 3000 ft becomes class 2 when introduced to inventory. 
Part B (Installation Decision Flow): The core optimization that dictates the inventory routing logic. For Scenarios 
1-4, it applies a strict priority rule:  the system first searches for available downgraded CT in the recycle inventory. 
If unavailable, it pulls from pre -cut inventory and only cuts a new 20,000 ft roll as a last  resort, which diverge 
according to the specific scenario: executing fully flexible dynamic cutting from new rolls (Scenario 1), utilizing 
pre-cut fixed lengths (Scenarios 2 and 3), or applying a hybrid approach (Scenario 4).  
3.4 Discrete event simulation results  
Figure 7  shows the simulation results . The simulation compared the highly inefficient current practice 
(Scenario 0), which consumes 47 new rolls and generates over one million feet of scrap, against four alternative 
recycling strategies (Scenarios 1 –4). While all proposed scenarios significantly reduced new roll consumption 
(down to 19–26 rolls) and minimized overall waste, the rigid fixed -cutting policies of Scenarios 2 and 3 proved 
operationally unviable, failing to comple te 46 and 26 jobs, respectively, due to inflexible inventory policies. 
Because fulfilling full customer demand is a critical operational metric, this failure disqualifies them from serious 
consideration. Consequently, Scenario 1 (Dynamic Recycle) and Scenario 4 (Hybrid Cut) emerged as the optimal 
and most robust strategies; both successfully maintained the highest production output by completing the full 
demand of approximately 284 installation jobs with zero rejections, all while maximizing the utilization  of 
recycled materials. 
 
 
Figure 6.  
Example of DES Arena Simulation for optimization Scenario 1,  
demonstrating Dynamic Cutting and Recycled Coiled Tubing.

400 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
The primary requirement of any operational strategy is meeting customer demand. Figure 8 demonstrates that 
while Scenarios 0, 1,  and 4 serviced the full job demand of 283 to 284 installations, the fixed -cutting strategies 
(Scenarios 2 and 3) were operationally unviable. Scenario 2 failed to complete 46 jobs , and Scenario 3 rejected 
26 jobs because their inflexible inventory policies could not service the full range of required CT lengths. 
The operational success of the dynamic recycling strategies is rooted in establishing a circular supply chain. 
Figure 9 (a) shows that in Scenarios 1 and 4, nearly 60% of all work (168 jobs) was fulfilled using recovered ex-
used CT. This heavy reliance on recycled inventory led to a dramatic 53% reduction in new material consumption, 
requiring only 22 new 20,000 ft rolls compared to the 47 rolls consumed in Scenario 0, as detailed in Figure 9 (b).  
A detailed analysis of waste generation further highlights the inefficiency of current practices. As illustrated 
in Figure 10 (a) , Scenario 0 generates a significant 1,002 ,270 ft of scrap entirely from disposing of retrieved 
installations. By successfully re -using fit materials (Figure 10 (b)), Scenario 1 minimizes total scrap by 60% to 
404,860 ft. Table 6 summarizes the performance of all strategies and shows  that Scenario 1 (Dynamic Recycle) 
offers the optimal balance of operational flexibility and material efficiency.  
The simulation results support implementing Scenario 1 (Dynamic Recycle). While the fixed-cutting strategies 
(Scenarios 2 and 3) are operationally inefficient due to unmet customer demand, and the hybrid approach 
(Scenario 4) offers no significant benefit over the simpler dynamic model while creating slightly more scrap, 
Scenario 1 delivers optimal performance. It provides a massive reduction in new material costs, generates the least 
scrap, and maintains operational flexibility to service 100% of installation jobs. 
 
 
Figure 7.  
Simulation outputs comparing Key Operational Metrics across all scenarios (Using Arena Software 16.2).

401 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
Figure 8.  
Successful versus Rejected Installation Jobs, highlighting the limitations of fixed-cut strategies (Scenarios 2 and 3). 
 
 
 
 
Figure 9.  
Coiled tubing consumption breakdown: (a) Installation Job Using New versus Recycled CT;  
(b) Total new Coiled Tubing consumption. 
a). 
b). 
Scenario            Scenario         Scenario                     Scenario                       Scenario 
      0                        1                     2                                 3                                   4 
Installation Recycled CT (Job) 
Installation New CT (Job) 
Scenario            Scenario           Scenario            Scenario            Scenario 
      0                        1                       2                       3                         4 
284 283 
239 
258 
283

402 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
 
 
 
 
 
Figure 10.  
Waste reduction and circular inventory efficiency illustrate (a) the significant decrease in total scrap length generated and  
(b) the volume of successfully repurposed coiled tubing per job. 
 
 
 
 
3.5 Cost-benefit and sensitivity analysis 
The operational metrics were translated into financial evaluations using Net Present Value (NPV), assessed 
against a project hurdle rate of $46.04 million to justify the surface facility and running costs. As illustrated in the 
NPV evolution and cumulative totals in Figure 11, Scenarios 1 and 4 are the most financially successful, each 
delivering a peak NPV of $58.53 million, which represents a 7.62% improvement over the current baseline 
(Scenario 0). In contrast, the fixed-cutting strategies (Scenarios 2 and 3) proved financially detrimental, yielding 
lower NPVs of $49.36 million and $52.32 million, respectively. These underperformances were directly caused 
by inventory shortages that led to significant lost revenue opportunities: $14.25 million for Scenario 2 and $8.06 
million for Scenario 3. This underscores that cutting efficiency must be balanced against inventory availability: a 
policy that lowers material consumption but cannot service the full range of required lengths destroys more value 
through rejected jobs than it saves on material.  
 
 
a). 
b).

403 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Table 6.  
Summary of simulation result. 
Key Performance Scenario-0 Scenario-1 Scenario-2 Scenario-3 Scenario-4 
Installation (Job/year) 47.3 47.2 39.8 43.0 47.2 
New CT Roll (Roll/year) 7.8 3.7 3.2 4.3 3.7 
Recycled CT (Job/year) 0.0 28.0 24.5 26.2 28.0 
Job Rejected (job/year) 0.0 0.0 7.7 4.3 0.0 
Scrap Length (ft) 1,002,270 404,860 490,990 585,710 420,520 
 
 
 
 
 
Figure 11.  
Financial evaluation using Net Present Value (NPV), illustrating (a) the annual NPV trajectory and (b) cumulative NPV 
against the $46.04 million project hurdle rate, identifying Scenarios 1 and 4 as the most profitable strategies. 
a). 
b).

404 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
 
 
 
Figure 12.   
Tornado charts representing sensitivity analysis, the financial impact of (a) production forecast accuracy,  
(b) oil price volatility, and (c) coiled tubing material cost inflation on the project's robustness. 
 
 
This research conducted three sensitivity evaluations to assess each scenario's simulation results under varying 
conditions. Because marginal field projects operate under inherent uncertainties, a Monte Carlo sensitivity 
analysis (10,000 iterations) was co nducted to assess each scenario's financial robustness against three major 
external factors: production forecasting accuracy, oil price volatility, and CT material cost inflation. The resulting 
Tornado Charts (Figure 12) reveal that production forecasts and external oil prices are the most critical risks, each 
capable of swinging the project's NPV by more than $20 million.  
Crucially, the sensitivity to CT price increments highlights the extreme vulnerability of the current "use -and-
dispose" practice; Scenario 0 relies entirely on purchasing new materials, causing its NPV to plunge below the $46.04 
million hurdle rate if CT prices increase by 20% in the fifth year. By drastically reducing reliance on new materials, 
Scenario 1 acts as a strong financial hedge against supply chain inflation, keeping NPV well above the hurdle.  
a). 
c). 
b).

405 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Based on this financial benefit and its sensitivity, two recommendations emerge for this project related to best-
scenario and retrieval-strategy optimization. Consequently, implementing the dynamic recycling strategy 
alongside a "lean retrieval" policy where CT is retrieved only when necessary to replenish inventory is strongly 
recommended to protect long-term project viability and profitability. The company should avoid treating retrieval 
as a standalone service and instead schedule it only when necessary to replenish recycled CT inventory, as this 
minimizes costs and protects the project's high NPV. 
 
4. Discussion 
Previous studies on coiled tubing have predominantly focused on isolated technical parameters such as plastic-
elastic deformation and corrosion failure mechanisms. Meanwhile, DES has been widely and successfully 
implemented in other sectors such as healthcare and logistics to manage uncertainty and optimize complex supply 
chains (Ala & Chen 2020; Coelho et al., 2021). The contrast with the deterministic approach ordinarily applied to 
this decision is substantive. A static payback or average-cost comparison evaluates a single expected demand path 
and would rank the fixed-cut policies favorably because they consume the fewest new rolls per installation; it has 
no mechanism to represent the stochastic arrival of job lengths and therefore cannot expose the rejected jobs those 
policies generate. The DES formulation surfaces exactly that failure mode, and the $14.25 million and $8.06 
million of lost revenue opportunity attached to Scenarios 2 and 3 are visible only because de mand is modeled as 
a stochastic process rather than an average. By integrating DES, the best -performing Dynamic Cutting model 
(Scenario 1) proves that flexible inventory routing can fully satisfy stochastic well demands without job rejections. 
Consistent with broader inventory optimization studies where simulation methods significantly lowered average 
holding costs and material volumes (Chen et al., 2022;  Mitrovi et al., 2021) , Scenario 1 leverages dynamic 
flexibility to deliver a reduction in metal scrap and NPV improvement through avoided new material purchases. 
The simulation results for and strongly support a fundamental shift from the current linear "take-make-dispose" 
framework to a circular asset management model. The superior Net Present Value (NPV) achieved by the dynamic 
cutting strategies (Scenarios 1 and 4) represents more than a marginal operational improvement; it significantly 
enhances the asset's overall value. This value creation is d riven by two primary mechanisms: massive cost 
avoidance through a dramatic reduction in the procurement of expensive new Coiled Tubing (CT) rolls, and 
revenue assurance by ensuring all job demands are met. By fulfilling 100% of operational demands, the dynamic 
reutilization project goes beyond simple cost-saving to become a value-creation engine that improves both the top 
and bottom lines of marginal field operations.  
Beyond base-case profitability, the sensitivity analysis provides critical insights into the strategic value of 
operational resilience. While the baseline practice (Scenario 0) is profitable under ideal conditions, it is extremely 
vulnerable to external market shocks. In contrast, the dynamic recycling models proved highly resilient because 
their reduced dependence on new materials acts as a powerful hedge against supply chain volatility and material 
cost inflation. In an oil and gas industry defined by uncertainty, particularly regarding production forecasts and 
oil prices, this resilience is arguably as important as the initial NPV, making dynamic reutilization the most 
strategic choice for long-term planning.  
The simulation reveals two unexpected yet pivotal findings. First, the detrimental performance of the fixed -
cutting strategies (Scenar ios 2 and 3) proved that a poorly implemented reutilization strategy lacking adequate 
inventory management introduces a new mode of failure (rejected jobs) , which entirely negates the benefits of 
recycling. Second, the analysis revealed that the program su ccessfully reframes a liability into a financial asset. 
The baseline practice incurred $8.81 million in scrap costs over six years from over one million feet of discarded 
tubing, recovering zero value. In contrast, the optimal recycling strategies not only  reduced scrap costs to $3.6 
million but simultaneously generated $4.04 million in value from the reutilized CT. This new concept shift proves 
the initiative is a profitable, self-sustaining component of the business.

406 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
From a management perspective, this study validates Discrete Event Simulation (DES) as a critical tool for 
de-risking decisions. It allows decision -makers to quantify trade -offs and test complex operational changes in 
a risk-free virtual environment before committing substa ntial capital. However, to maintain practical integrity, 
the model's limitations must be acknowledged. The assumption of zero material cost for recycled CT is a 
deliberate simplification for modeling purposes. In actual field applications, nominal costs as sociated with 
storage space, logistical handling, and non -destructive inspection of retrieved tubing would apply. Furthermore, 
while this model successfully demonstrates the economic viability of CT reutilization, it currently assumes an 
unconstrained insp ection capacity. Future iterations should incorporate physical resource limitations to identify 
potential operational bottlenecks.  
 
5. Conclusion 
This study was initiated to address the critical business challenge of declining production contributions from 
CTGL installations in marginal fields, necessitating significant cost-efficiency improvements to maintain project 
viability. The comprehensive DES evaluation conclusively proves that shifting from a "use and scrap" to a "use 
and recycle" approach through a d ynamic cutting strategy is the optimal path forward. Scenario 1 raises NPV 
from $54.39 million to $58.53 million, an improvement of 7.62% or $4.14 million, while cutting new coiled tubing 
consumption by 53% and metal scrap by 60% and servicing 100% of job demand. By synthesizing the simulation 
outcomes, this study establishes DES as a robust decision -support tool that effectively bridges technical asset 
evaluation with long -term economic planning. The findings highlight a critical implication for oil and ga s 
operators: rigid inventory policies are fundamentally detrimental in stochastic circumstances. Meanwhile, 
adopting reutilization strategies transforms retrieved coiled tubing from a waste liability into a high-value financial 
hedge.  Ultimately, implemen ting a robust recycling inventory with dynamic cutting minimizes vulnerability to 
market shocks and maximizes long-term financial returns.  
Moving forward, future research should refine the model's precision by transitioning from deterministic inputs 
to fully stochastic variables for process times and future job planning. To address operational realities, subsequent 
models must incorporate resource constraints to accurately identify potential physical bottlenecks in the retrieval 
and inspection phases. Finally, expanding the scope of the key performance indicators to quantify environmental 
benefits such as CO2 emission reductions and avoided waste handling costs will provide a more holistic validation 
of the circular economy's value within the oil and gas industry. 
 
6. Acknowledgement 
The authors would like to express their sincere gratitude to Bina Nusantara University (Binus University) for 
the invaluable support, resources, and research environment provided throughout this study. 
 
7. Declarations 
7.1 Author contributions 
Warno contributed to the conception and design of the study, data collection, data analysis, and the initial 
drafting of the manuscript. Suharjito provided data validation, critical review, and overall supervision of the 
research process. Both authors discussed the results, contributed to the refinement of the manuscript, and approved 
the final version for submission. 
7.2 Funding statement 
The author(s) received no financial support for the research, authorship, and/or publication of this article.

407 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
7.3 Competing interest 
The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or 
publication of this article.  
7.4 Data availability 
The data supporting this study were obtained from the corresponding auth or upon reasonable request and 
subject to permission from the data owner, due to commercial confidentiality. 
7.5 The use of AI or AI-assisted technologies 
During the preparation of this manuscript, the authors used AI -based writing and editing tools to support  
language refinement, formatting, and reference organization . All scientific content, data interpretation, and 
conclusions are sole responsibility of the authors, who reviewed and edited all AI -assisted output and take full 
responsibility for content of this publication. 
 
8. Glossary of terms and symbols 
Terms & Symbols Definition Unit 
CTGL Coiled Tubing Gas Lift - 
DES Discrete Event Simulation - 
DCF Decline Curve Forecasting - 
NPV Net Present Value - 
 
 
9. References 
Ala, A., & Chen, F. (2020). Alternative mathematical formulation and hybrid meta -heuristics for patient 
scheduling problem in health care clinics. Neural Computing and Applications , 32(13), 8993 –9008. 
https://doi.org/10.1007/s00521-019-04405-4  
Alagoz, E., & Tali, B. (2023). Applications and Limitations of Coiled Tubing Technology: A Glance. Science 
Journal of Energy Engineering, (July). https://doi.org/10.11648/j.sjee.20231101.12  
Alharbi, R., Alageel, N., Alsayil, M., Alharbi, R., & Alhakamy, A. (2022). Prediction of Oil Production through 
Linear Regression Model and Big Data Tools. (December). https://doi.org/10.14569/IJACSA.2022.0131246  
Al-Zqebah, R., Hoffmann, F., Bennett, N., Deuse, J., & Clemon, L. (2022). Woolshed Throughput Improvement 
Using Discrete Event Simulation. Journal of Industrial Engineering and Management , 15(2), 296 –308. 
https://doi.org/10.3926/jiem.3721  
Arani, M., Liu, X., & Abdolmaleki, S. (2020). Scenario-Based Simulation Approach for An Integrated Inventory 
Blood Supply Chain System. Proceedings - Winter Simulation Conference , 2020-Decem(c), 1348 –1359. 
https://doi.org/10.1109/WSC48552.2020.9384018  
Bajjou, M. S., & Chafi, A. (2021). Lean construction and simulation for performance improvement: a case study 
of reinforcement process. International Journal of Productivity and Performance Management , 70(2), 459–
487. https://doi.org/10.1108/IJPPM-06-2019-0309  
Bastos, Y. B., Fleck, J. L., & Ma rtinelli, R. (2020). A stochastic programming approach for offshore flight 
scheduling. IFAC-PapersOnLine, 53(4), 478–484. https://doi.org/10.1016/j.ifacol.2021.04.068

408 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Bayoud, H. A. (2021). Tests  of normality: new test and comparative study. Communications in Statistics: 
Simulation and Computation, 50(12), 4442–4463. https://doi.org/10.1080/03610918.2019.1643883  
Chen, C. N., Lai, C. H., Lu, G. W., Huang, C. C., Wu, L. J., Lin, H. C., & Chen, P. S. (2022). Applying Simulation 
Optimization to Minimize Drug Inventory Costs: A Study of a Case Outpatient Pharmacy. Healthcare 
(Switzerland), 10(3). https://doi.org/10.3390/healthcare10030556  
Coelho, F., Relvas, S., & Barbosa -Póvoa, A. P. (2021). Simulation -based decision support tool for in -house 
logistics: the basis for a digital twin. Computers and Industrial Engineering , 153(March 20 20). 
https://doi.org/10.1016/j.cie.2020.107094  
de la Torre, R., Corlu, C. G., Faulin, J., Onggo, B. S., & Juan, A. A. (2021). Simulation, optimization, and machine 
learning in sustainable transport ation systems: Models and applications. Sustainability (Switzerland), 13(3), 
1–21. https://doi.org/10.3390/su13031551  
Efa D., A., H.T., R., N.D., W., Chandra, S., & A.A., P. (2019). Progressing Cavity Pump as a Solution to Increase 
Productivity of Highly Viscous Oil Wells with Sand Production: A Case Study of Field X. Scientific 
Contributions Oil and Gas, 42(3), 59–63. https://doi.org/10.29017/SCOG.42.3.376  
Elijah, O., Ling, P. A., Rahim, S. K. A., Geok, T. K., Arsad, A., Kadir, E. A., Abdurrahman, M., Junin, R., Agi, 
A., & Abdulfatah, M. Y. (2021). A Survey on Indust ry 4.0 for the Oil and Gas Industry: Upstream Sector. 
IEEE Access, 9, 144438–144468. https://doi.org/10.1109/ACCESS.2021.3121302  
Golbasi, O., & Turan, M. O. (2020). A discrete-event simulation algorithm for the optimization of multi-scenario 
maintenance policies. Computers and Industrial Engineering , 145(May), 106514. 
https://doi.org/10.1016/j.cie.2020.106514  
Hagianu, A., Nae, I., Ionescu, G. C., & Ripeanu, R. G. (2020). Research on mechanical and geometrical 
characteristics of materials used for flexible tubing production. IOP Conference Series: Materials Science and 
Engineering, 724(1). https://doi.org/10.1088/1757-899X/724/1/012004  
Khalid, A., Molero, N., Hassan, G., Lovie, E., Khan, R. S. A., Shafin, R., & Khan, A. (2020). Coiled tubing gas 
lift: An innovative solution for reviving dead wells in southern Pakistan. International Petroleum Technology 
Conference 2020, IPTC 2020, 1–18. https://doi.org/10.2523/19930-abstract 
Kolawole, O., Gamadi, T. D., & Bullard, D. (2020). Artificial Lift System Applications in Tight Formations: The 
State of Knowledge. SPE Production and Operations, 35(2), 422–434. https://doi.org/10.2118/196592-PA  
Lestari, F., Kurniawan, R., Ismail, K., Mawardi, M., Nurainun, T., & Hariadi, I. (2022). Business Unit Utilization 
in Supply Chain of Distribution Channel. Journal of Industrial Engineering and Management , 15(2), 143–
154. https://doi.org/10.3926/jiem.3546  
Long, Y., Huang, S., Peng, L., Wa ng, S., & Zhao, W. (2020). A new dual magnetic sensor probe for lift -off 
compensation in magnetic flux leakage detection. I2MTC 2020 - International Instrumentation and 
Measurement Technology Conference, Proceedings , 21(9), 10854 –10863. 
https://doi.org/10.1109/I2MTC43012.2020.9129204  
Marshall, D. A., Grazziotin, L. R., Regier, D. A., Wordsworth, S., Buchanan, J., Phillips, K., & Ijzerman, M. 
(2020). Addressing Challenges of Economic Evaluation  in Precision Medicine Using Dynamic Simulation 
Modeling. Value in Health, 23(5), 566–573. https://doi.org/10.1016/j.jval.2020.01.016  
Maurenza, F., Yasutra, A., & Tungkup, I. L. (2023). Production Forecasting Using Arps Decline Curve Model 
with The Effect of Artificial Lift Installation. Scientific Contributions Oil and Gas , 46(1), 17 –26. 
https://doi.org/10.29017/SCOG.46.1.1310  
Menberg, K., Heo, Y., & Choudhary, R. (2016). Sensitivity analysis methods for building energy models: 
Comparing computational costs and extractable information. Energy and Buildings , 133, 433 –445. 
https://doi.org/10.1016/j.enbuild.2016.10.005

409 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Mitrovi, M., Vidovi, M., & Radivojevi, G. (2021). Order Level Optimization in Inventory Management Using 
Arena Simulation Model. International Journal for Tr affic and Transport Engineering , 11(2), 257 –266. 
https://doi.org/10.7708/ijtte.2021.11(2).06  
Nguyen, H. H., & Chan, C. W. (2005). Applications of data analysis techniques for oil production prediction. 18, 
549–558. https://doi.org/10.1016/j.engappai.2004.11.010  
Ning, Y., Kazemi, H., & Tahmasebi, P. (2022). A comparative machine learning study for time series oil 
production forecasting : ARIMA, LSTM, and Prophet. Computers and Geosciences , 164(March), 105126. 
https://doi.org/10.1016/j.cageo.2022.105126  
Okeke, O. B. (2020). The impacts of shared autonomous vehicles on car parking space. Case Studies on Transport 
Policy, 8(4), 1307–1318. https://doi.org/10.1016/j.cstp.2020.09.002  
Ordu, M., Demir, E., Tofallis, C., & Gunal, M. M. (2021). A novel healthcare resource allocation decision support 
tool: A forecasting -simulation-optimization approach. Journal of the Operational Research Society , 72(3), 
485–500. https://doi.org/10.1080/01605682.2019.1700186  
Shaohu, L., Feng, G., Xianjin, W., Hui, X., Zhen, W., & Ting, Y. (2019). Theoretical and experimental research 
of bearing capacity and fatigue life for coiled tubing under internal pressure. Engineering Failure Analysis , 
104(June), 1133–1142. https://doi.org/10.1016/j.engfailanal.2019.06.062  
Shaohu, L., Yuanliang, L., & Hong, Z. (2020). Corrosion Failure and Electrochemical Corrosion Behavior of 
Coiled Tubing. Journal of Failure Analysis and Prevention , 20(6), 1964 –1974. 
https://doi.org/10.1007/s11668-020-01007-4  
Sherik, A., Abdalla, M. Ben, Abdoalqader, A., Abusninah, G., Abdaldaem, A. A., Ayad, A. N. Ben, Nagim, A., 
Ayad, B., & Oil&gas, M. (2019). Coiled -tubing gas lift system doubled oil production from Al-Wafa field. 
Society of Petroleum Engineers - SPE Kuwait Oil and Gas Show and Conference 2019, KOGS 2019 . 
https://doi.org/10.2118/198096-MS  
Shou, W., Wang, J., Wu, P., & Wang, X. (2021). Lean management framework for improving maintenance 
operation: development and application in the oil and gas industry. Production Planning and Control, 32(7), 
585–602. https://doi.org/10.1080/09537287.2020.1744762  
Sibuea, N., Ramadhan, A. R., Tri Aulia, R., Khairunni sa, S., Yendra, R., & Adnan, A. (2022). Comparison of 
Linear Regression Method and Holt-Winters Method in Oil and Gas Export Volume Forecasting in Indonesia. 
International Journal of Mathematics Trends and Technology , 68(12), 7 –12. 
https://doi.org/10.14445/22315373/ijmtt-v68i12p502  
Singh, A., & Pateriya, R. K. (2019). Artificial oil lift production forecasting and analysis using autoregressive 
and deep learning models. SSRN. https://doi.org/10.2139/ssrn.3396282  
Suharjito, S., & Warno, W. (2025). Coiled Tubing Circular Efficiency: A Systematic Literature Review on Failure 
Mechanisms, Inspection Methods, and Reuse Potential. Scientific Contributions Oil and Gas , 48(4), 1–15. 
https://doi.org/10.29017/scog.v48i3.1906  
Tadjer, A., Hong, A., & Bratvold, R. B. (2021). Machine learning-based decline curve analysis for short-term oil 
production forecast. Energy Exploration and Exploitation , 39(5), 1747 –1769. 
https://doi.org/10.1177/01445987211011784  
Teles, A. (2024). Discrete Event Simulation to Evaluate Capacity Planning under Uncerta inty in the Aircraft 
Industry. 
Tezel, O., Tiryaki, B. K., Ozkul, E., & Kesemen, O. (2021). A new goodness -of-fit test: Free chi -square (fcs). 
Gazi University Journal of Science, 34(3), 879–897. https://doi.org/10.35378/gujs.743444  
Thakuria, C., Al-Ghnemi, M., Bora, A., & Al -Bahar, M. (2019). Decline curve analysis for production forecast 
assurance: A novel approach. Society of Petroleum Engineers - SPE Kuwait Oil and Gas Show and Conference 
2019, KOGS 2019. https://doi.org/10.2118/197991-ms

410 
 
Warno & Suharjito. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2149 
 
Tong, S., & Gao, D. (2019). Elastic -plastic collapse limit analysis of coiled tubing under complex stress s tate. 
Journal of Petroleum Science and Engineering , 174(November 2018), 106 –114. 
https://doi.org/10.1016/j.petrol.2018.11.018  
Usher, W., Barnes, T., Moksnes, N., & Niet, T. (2023). Global sensit ivity analysis to enhance the transparency 
and rigor of energy system optimization modeling . Open Research Europe , 3. 
https://doi.org/10.12688/openreseurope.15461.1  
Wikman-Jorgensen, P. E., Ruiz, A., Giner-Galvañ, V., Llenas-García, J., Seguí-Ripoll, J. M., Salinas-Serrano, J. 
M., Borrajo, E., Ibarra -Sánchez, J. M., García -Sabater, J. P., & Marin -Garcia, J. A. (2024). Hospitalization 
Forecast to Inform COVID-19 Pandemic Planning and Resource Allocation Using Discrete Event Simulation. 
Journal of Industrial Engineering and Management, 17(1), 168–181. https://doi.org/10.3926/jiem.6404  
Wiranata, K., Ridene, A., Yusoff, M. M. N. A. M., Hamdi, A., Sa, R., Chaari, Y., Arifin, M., Afendy, N., Yusoff, 
M. M. N. A. M., Hamdi, A., Sa, R., Chaari, Y., & Arifin, M. (2020). Novel application of magnetic flux 
leakage-based technology validating pipe  elongation in coiled tubing drilling operation. International 
Petroleum Technology Conference 2020, IPTC 2020. https://doi.org/10.2523/iptc-20084-ms  
Yan, F., Li, Z., Zhang, C., & Wang, H. (2021). Stud y on grooving corrosion behavior of QT800 coiled tubing. 
AIP Advances, 11(4). https://doi.org/10.1063/5.0044098  
Zhou, Z., Zhang, J., Wang, C., Wan, F., He, S., & Yu, R. (2020). Non -Magnetization Detection of Arbitrary 
Direction Defects in Coiled Tubing Based on Fluxgate Sensor. IEEE Sensors Journal , 20(14), 7661–7668. 
https://doi.org/10.1109/JSEN.2020.2979497
