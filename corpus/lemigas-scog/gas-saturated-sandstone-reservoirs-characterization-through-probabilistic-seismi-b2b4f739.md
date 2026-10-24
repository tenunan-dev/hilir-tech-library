---
source_id: "lemigas-scog"
title: "Gas Saturated Sandstone Reservoirs Characterization through Probabilistic Seismic Inversion Using Bayesian Neu"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2138"
retrieved_at: "2026-10-24T14:30:24+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "b2b4f73980e2d603e52e0c9b5c8bb32605c90e3546b0470793b0fe6d06e6d9b2"
collected: "manual"
---

# Gas Saturated Sandstone Reservoirs Characterization through Probabilistic Seismic Inversion Using Bayesian Neu

567 
 
https://doi.org/10.29017/scog.v49i3.2138 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 567 – 592 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Gas Saturated Sandstone Reservoirs Characterization through 
Probabilistic Seismic Inversion Using Bayesian Neural Networks 
 
 
Edi Sanjaya, Praditiyo Riyadi*, and Fadhlur Rahman 
 
Department of Physics, Universitas Islam Negeri Syarif Hidayatullah Jakarta, 
Ir. H. Djuanda Street No. 95, Ciputat, South Tangerang, Indonesia. 
*Corresponding author: Praditiyo Riyadi (praditiyo.riyadi@uinjkt.ac.id) 
Praditiyo Riyadi: Orchid id: https://orcid.org/0000-0002-0759-7183 
Google Scholar: https://scholar.google.com/citations?hl=id&authuser=6&user=PdeERWYAAAAJ 
Received:  06 April 2026; Revised: in revised form 17 July 2026; Accepted: 18 August 2026 
Available: online 30 September 2026. 
  
 
ABSTRACT - Shallow gas-saturated sandstone reservoirs are prevalent throughout Indonesia, presenting highly 
lucrative economic prospects that are often hindered by complex geological heterogeneities. Characterization of 
these reservoirs typically relies on deterministic seismic inversion methods. However, the inherent non -
uniqueness of such approaches yields singular solutions devoid of uncertainty quantification. This study proposes 
a robust probabilistic seismic inversion methodology utilizing a Convolutional Bayesian Neural Network (BNN). 
By incorporating Monte Carlo (MC) dropout, which forces the stochastic deactivation of hidden nodes during 
training, the algorithm successfully generates a comprehensive ensemble of predictive realizations. The proposed 
framework is evaluated using 2D pre -stack synthetic angle gathers (0  to 45°) across two scenarios: a baseline 
layer-cake model and a structurally complex faulted model incorporating random noise to simulate field-acquired 
data. Using seismic amplitudes and low -frequency models to simultaneously predict porosity, clay volume, and 
water saturation, the BNN demonstrates exceptional predictive accuracy on the baseline model, yielding an 
average Root Mean Square Error (RMSE) of 0.03 and a coefficient of determination (R2) of 0.9. When applied to 
the complex faulted model, the predictive fidelity naturally degraded (average R2 of 0.7 to 0.8; RMSE of 0.09 to 
0.15), consistent with the inherent challenges of noise -contaminated data. Furthermore, a comparative analysis 
against a conventional model -based deterministic inversion reveals that while the deterministic approach better 
delineates fault architectures vi a horizon constraints, the BNN framework yields supe rior quantitative fidelity. 
Notably, the BNN successfully overcomes the systematic underestimation of porosity inherent in the deterministic 
acoustic impedance-to-porosity conversion process. The stochastic inversion explicitly produces 2D petrophysical 
cross-sections detailing the P10, P90, and mean distributions extracted from 50 realizations. Given their high 
fidelity, the mean distributions are directly applicable for reservoir characteriza tion. Crucially, the probabilistic 
P10 and P90 boundary percentiles facilitate a comprehensive assessment of in-place hydrocarbon volumes. This 
study are currently limited to synthetic validation , and subsequent validation with real -field data is necessary 
before the approach can be practically applied. 
Keywords: probabilistic inversion, Bayesian Neural Network, petrophysical properties, gas sandstone. 
  
 
How to cite this article: 
Edi Sanjaya, Praditiyo Riyadi, and Fadhlur Rahman, 2026, Gas Saturated Sandstone Reservoirs 
Characterization through Probabilistic Seismic Inversion Using Bayesian Neural Networks, Scientific 
Contributions Oil and Gas, 49 (3) pp. 567-592.

568 
 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
1. Introduction 
Gas saturated sandstone reservoirs are commonly found across various regions in Indonesia and present 
highly promising, economically viable targets due to their typically shallow depths (Jin et al., 2024 ; Shan et 
al., 2026 ; Widarsono et al., 2025) . Prominent examples include the fluvio -deltaic sequences of the Tunu field 
in East Kalimantan (Andrieu et al., 2018 ; Laidlaw et al., 2012)  and the Bentu gas field in Central Sumatra 
(Yuwono et al., 2012) . For these fields, accurate reservoir characterization specifically the quantification of 
fundamental petrophysical properties like porosity, shale volume, and water saturation is critical for 
assessing economic feasibility and calculating initial hydroca rbons in place (Coimbra & Sampaio 2025 ; 
Mahmud et al., 2020 ; Yusof et al., 2018) . 
Determining the spatial dimensions and petrophysical parameters of these reservoirs relies heavily on seismic 
reflection methods, where gas accumulations often present as "bright spot" anomalies due to low gas density 
(Horozal et al., 2021 ; Lowrie & Fichtner 2020) . Consequently, seismic inversion is widely used for 
characterization (Putra et al., 2026) . However, conventional deterministic seismic inversion methods depend 
heavily on seismic data quality and typically yield non-unique solutions (Li et al., 2024). This limitation has driven 
a shift towards probabilistic inversion methods capable of providing multiple possible outcomes to better assess 
uncertainty (Li et al., 2024). 
Increasingly, machine learning algorithms are employed to drive these probabilistic workflows (Grana et al., 
2022). For instance, Bayesian Neural Networks (BNN) have been successfully applied for the probabilistic 
inversion of surface wave data (Zhang & Curtis 2021)  and, more recently, for deriving petrophysical properties 
from seismic reflection data (Grana et al., 2022). Furthermore, (Romero et al., 2025) demonstrated the advantages 
of BNN-driven probabilistic inversion over conventional deterministic approaches. Despite these advancements, 
existing studies fall short of addressing the specific non -linear complexities associated with gas -saturated 
sandstone reservoirs, leaving a critical gap in evaluating BNN performance for this specific geological context. 
To address this gap, this study aims to rigorously evaluate the performance of BNN -driven probabilistic 
inversion specifically tailored for characterizing gas -saturated sandstone reservoirs. Physically, the seismic 
responses of these reservoirs are highly non-linear and non-unique, making them difficult to predict using standard 
deterministic neural networks. Such standard networks struggle with this ill-posed inverse problem, as they output 
single-point estimates without accounting for data or model confid ence, often leading to overconfident 
predictions. In contrast, by replacing deterministic network weights with probability distributions, the proposed 
BNN approach inherently provides robust uncertainty estimation critical for reliable gas reservoir analysis. 
To validate this methodology, a synthetic forward model of a gas -bearing sandstone reservoir is constructed. 
Utilizing synthetic data is a strategically necessary preliminary step to evaluate the operational behavior and 
computational requirements of the B NN before field application. Because training and simulating stochastic 
realizations within a BNN demand significant computational resources, the synthetic model serves as a practical, 
cost-effective platform to test algorithmic feasibility, optimize netwo rk parameters, and ensure stability without 
the prohibitive overhead of large -scale field datasets. By benchmarking these inversion outputs against the true 
synthetic model, this study intends to establish a robust reference workflow for future BNN impleme ntations in 
real-field case studies across Indonesian sedimentary basins.  
 
2. Methodology 
2.1 Synthetic seismic data 
The present study employs synthetic seismic data derived from a forward modeling approach . The synthetic 
seismic workflow  (Figure 1)  is driven by a deterministic rock physics model  (Jin et al., 2024) . Initially, 
petrophysical parameters are defined to calculate the P -wave velocity (𝑉𝑝) utilizing (Han et al., 1986) empirical 
model (Equation 1). The bulk density (𝜌) is subsequently estimated through a linear mixing model (Voigt bound) 
(Yu 2024) , which accounts for the respective volume fractions of the mineral matrix and pore -filling fluids

569 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
(Equations 2, 3, and 4). 
𝑉𝑝(𝑘𝑚 𝑠⁄ ) = 5.59 − 6.93𝜙 − 2.18𝑉𝑐𝑙   (1) 
where 𝑉𝑝 and 𝜙 are the compressional velocity (km/s),  the total porosity fraction, and 𝑉𝑐𝑙 is the clay 
volume fraction, respectively. 
𝜌𝑚𝑎 = (1 − 𝑉𝑐𝑙)𝜌𝑞𝑢𝑎𝑟𝑡𝑧 + 𝑉𝑐𝑙𝜌𝑐𝑙𝑎𝑦      (2) 
where 𝜌𝑚𝑎, 𝜌𝑞𝑢𝑎𝑟𝑡𝑧, and 𝜌𝑐𝑙𝑎𝑦 are denotes the rock matrix density, represent the densities of the quartz 
and clay minerals, respectively. 
𝜌𝑓𝑙 = 𝑆𝑤𝜌𝑤𝑎𝑡𝑒𝑟 + (1 − 𝑆𝑤)𝜌ℎ𝑐                         (3) 
where 𝜌𝑓𝑙, 𝑆𝑤 and 𝜌𝑤𝑎𝑡𝑒𝑟 are the fluid density in the rock, the water saturation, the water density, and 
𝜌ℎ𝑐 is the hydrocarbon density, , respectively. 
𝜌𝑏𝑢𝑙𝑘 = 𝜙𝜌𝑓𝑙 + (1 − 𝜙)𝜌𝑚𝑎       (4) 
where 𝜌𝑏𝑢𝑙𝑘 denotes the bulk density, which is fundamentally a function of the respective densities of 
the pore fluid and the solid rock matrix. 
The targeted petrophysical properties comprise clay volume, porosity, and water saturation. Furthermore, the 
shear-wave velocity (𝑉𝑠) is estimated based on the proportional relationship between 𝑉𝑝 and 𝑉𝑠, applying a specific 
𝑉𝑝/𝑉𝑠 ratio for each respective layer  (Liu et al., 2023) . All petrophysical parameters and input values utilized in 
the synthetic forward modeling are detailed in Table 1. 
Following the derivation of 𝑉𝑝 and 𝑉𝑠, the acoustic impedance (AI) is calculated via the following expression  
(Lowrie & Fichtner 2020): 
𝐴𝐼 =  𝑉𝑝 × 𝜌𝑏𝑢𝑙𝑘                                                  (5) 
where 𝐴𝐼 is the acoustic impedance, the contrast of which defines the interface between distinct lithologies 
(Taqiy et al., 2026) .  
Following the derivation of the 𝐴𝐼 profile, the reflection coefficient (𝑅𝐶) series can be computed (Fariz et al., 
2022). The 𝑅𝐶 quantifies the reflection magnitude at the geological boundary, yielding either positive or negative 
values dictated by the impedance contrast across the bounding rock layers (Sukma et al., 2025). 
The 𝑅𝐶 is mathematically determined by the following expression (Lowrie & Fichtner 2020): 
𝑅𝐶 =
𝐴𝐼2−𝐴𝐼1
𝐴𝐼2+𝐴𝐼1
                                                         (6) 
where 𝑅𝐶 is the reflection coefficient at the geological boundary, and 𝐴𝐼1 and 𝐴𝐼2 represent the acoustic 
impedances of the upper and lower layers, respectively. 
Following the derivation of the reflectivity series (RC), a convolution process is applied using a 30 Hz zero -
phase Ricker wavelet to generate the seismic response. The resulting synthetic data are structured as pre -stack 
angle gathers (Figure 2). To achieve this, the amplitude variation with angle is modeled utilizing Shuey's 2 -term 
approximation of the exact Zoeppritz interface equations (Kuai et al., 2025).

570 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
 
Table 1. 
Petrophysical properties and 𝑉𝑝/𝑉𝑠 ratios applied as inputs for the synthetic forward modeling workflow 
Layer Litologi/fluida Depth (m) VClay Porositas SW (%) Vp/Vs ratio 
Lapisan 1 Shale 1000 - 1050 0.80 0.05 1.00 2.50 
Lapisan 2 Brine Sand 1050 - 1100 0.10 0.25 1.00 2.00 
Lapisan 3 Shale 1100 - 1150 0.85 0.05 1.00 2.50 
Lapisan 4 Gas Sand 1150 - 1200 0.05 0.30 0.20 1.60 
Lapisan 5 Shale 1200 - 1250 0.80 0.05 1.00 2.50 
 
 
Figure 1. 
Workflow for generating angle-dependent synthetic seismic data 
 
𝑅(𝜃) = 𝑅0 + 𝐺𝑠𝑖𝑛2𝜃                                         (7) 
where 𝑅(𝜃), 𝑅0, and and 𝐺 are defines the angle-dependent reflection coefficient, denote the Amplitude Variation 
with Angle intercept and gradient, respectively.  The synthetic forward model was parameterized to carefully 
reflect typical geological conditions of shallow gas -bearing siliciclastic sequences. A 30 Hz zero -phase Ricker

571 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
wavelet was selected, as it represents the dominant seismic frequency conventionally observed for shallow to 
intermediate reservoir targets. Layer thicknesses were deliberately set to 50 m to comfortably exceed the seismic 
tuning thickness, thereby isolating the BNN’s evaluation to pure petrophysical variations without the confounding 
interference of thin-bed effects. Furthermore, the applied Vp/Vs ratios (e.g., approximately 1.6 for gas sands and 
>2.0 for background shales) were assigned based on established empirical rock physics trends for clastic rocks. 
To generate the pre -stack response, synthetic angle gathers were modeled over an incident angle range 
of 0° to 45° with a step size of 5°. The 45° far -angle limit is strictly necessary to capture the diagnostic far -
offset AVO anomalies typically associated  with gas -saturated sandstones, while the 5° increment provides 
sufficient angular resolution for generating partial stacks without incurring excessive computational 
redundancy. Finally, the synthetic trace was replicated 100 times to construct a pseudo -2D seismic section 
comprising 100 Common Depth Points (CDPs). This lateral replication creates a controlled spatial window, 
predictions prior to real -field application.  
To ensure the synthetic data closely resembles field measurements, noise and geological features were 
incorporated into the model. The applied noise is Gaussian noise, which is a type of normally distributed random 
noise, using a noise level parameter of 0 .005 to represent its standard deviation. Furthermore, to better reflect 
realistic subsurface conditions, a normal fault was introduced into the model. In this configuration, the footwall 
acts as a structural trap saturated with gas hydrocarbons, whereas t he hanging wall represents a brine -saturated 
zone devoid of hydrocarbons. 
2.2 Bayesian neural network inversion 
Within the realm of statistical and computational inverse problems, the Bayesian framework remains the 
most widely adopted probabilistic approach (Fernandes et al., 2024). The primary objective of this methodology 
is to estimate the posterior probability distribution of the model parameters, denoted as 𝑃(𝑚|𝑑) (Grana et al., 
2022). This posterior distribution is mathematically derived via Bayes' theorem (Li, Liu, et al., 2024), expressed 
as follows :  
𝑃(𝑚|𝑑) = 𝑃(𝑑|𝑚)𝑃(𝑚) 𝑃(𝑑)⁄                           (8) 
where 𝑃(𝑚) and 𝑃(𝑑|𝑚) are the posterior is evaluated as the product of the prior model probability distribution, 
the data likelihood function,  respectively. (Li et al., 2024) . This product is subsequently normalized by the 
marginal likelihood of the data (the evidence), 𝑃(𝑑), ensuring the probability density integrates to unity: 
∫ 𝑃 (𝑚|𝑑)𝑑𝑚 = 1 (Grana et al., 2022). 
Evaluating the exact Bayesian formulation (Equation 8) is notoriously intractable, as computing the 
normalizing constant (the marginal likelihood) analytically is virtually impossible for non-linear physical forward 
operators (Gou et al., 2022). To circumvent this analytical bottleneck, Monte Carlo methods are employed. Instead 
of a deterministic calculation, this approach stochastically generates thousands of model realizations from the 
prior distribution 𝑃(𝑚) and evaluates their data fit via the likelihood function 𝑃(𝑑|𝑚), iteratively constructing a 
robust empirical approximation of the desired posterior distribution (Li et al., 2024). The most robust Monte Carlo 
strategy for circumventing the intractable Bayesian evidence is the Markov chain Monte Carlo (MCMC) 
framework, notably the Metropolis-Hastings algorithm (Li et al., 2024). This method evaluates a proposed model 
realization (𝑚′) relative to the current state ( 𝑚𝑖) by calculating their posterior probability rasio (Zhang & Curtis 
2021). Because the marginal likelihood 𝑃(𝑑) is invariant for an observed dataset, it elegantly cancels out in the 
evaluation, significantly alleviating the computational burden  (Fernandes et al., 2024) . Mathematically, the 
acceptance probability of the proposed state is defined as follows: 
𝑃𝑎 = min (
𝑃(𝑑|𝑚′)𝑃(𝑚′)
𝑃(𝑑|𝑚𝑖)𝑃(𝑚𝑖) ×
𝑔(𝑚𝑖|𝑚′)
𝑔(𝑚′|𝑚𝑖)
, 1)            (9) 
where 𝑃𝑎, 𝑚′, and 𝑔 are the final value that determines the probability of the new guess being accepted, 𝑚𝑖 
represents the current model (current state), the newly proposed model (proposed state), and the proposal 
distribution, respectively.

572 
 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
Riyadi et al. Scientific Contributions Oil and Gas 
 
 
 
Figure 2. 
Synthetic seismic forward modeling as a function of angle

573 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Deep learning approaches have established themselves as formidable computational tools for seismic inversion 
(Simutė et al., 2023) , where the fundamental objective is to map seismic responses back to reservoir 
petrophysical properties, such as porosity, clay volume, and water saturation (Li et al., 2024). In this architecture, 
artificial neural networks are utilized to derive the inverse mapping approximation, 𝑔 =̃ 𝑓˜−1, where 𝑓 represents 
the deterministic rock physics forward modeling operator (Zhang & Curtis 2021). Diverging from conventional 
stochastic optimization schemes, these deep layered networks efficiently characterize the intricate, non -linear 
mappings between observed seismic data and subsurface model parameters (Siahgoli et al., 2025). 
Given that seismic data are fundamentally recorded as time-series signals, the use of Recurrent Neural Network 
(RNN) architectures (Siahgoli et al., 2025), particularly the Long Short-Term Memory (LSTM) variant, is highly 
crucial due to their ability to capture temporal dependencies (Sun et al., 2024). The subsurface model properties, 
𝑚, are extracted from the network's hidden states, 𝑧. Mathematically, the transformation within this network with 
𝐿 hidden layers (Li et al., 2024) is formulated as: 
𝑚 = ℎ(𝑤𝐿𝑧𝐿 + 𝑏𝐿)     (10) 
where the hidden states are sequentially updated across successive time steps using the following Equation 11 
𝑧𝑙 = 𝑔(𝑤𝑙−1𝑧𝑙−1 + 𝑏𝑙−1)    (11) 
for 𝑙 = 1, … , 𝐿, where {𝑤}1,…,𝐿 and {𝑏}1,…,𝐿 represent the trainable weight matrices and bias vectors at the 𝑙-th 
layer, respectively, and 𝑔 and ℎ denote the non-linear activation functions governing the information flow. 
Despite their capacity to yield robust sequential predictions, purely deterministic RNN architectures are often 
inadequate due to their inability to quantify the intrinsic uncertainties ubiquitous in geophysical inverse problems 
(Xiang et al., 2026) . To address this limitation, the neural network is embedded within a probabilistic Bayesian 
framework (Chala & Ray 2025) . Under the assumption of independent Gaussian measurement noise, the 
likelihood function mapping the observed data 𝑑 to the complete set of network parameters 𝜃 (Li et al., 2024) is 
defined as follows: 
𝑃(𝑑|𝜃) = ∏ 𝒩(𝑓(𝑚(𝜃))𝑖; 𝑑𝑖; 𝜎𝑖2)𝑛𝑖=1              (12) 
where 𝑃(𝑑|𝜃), 𝒩(… ), 𝑓(𝑚(𝜃))𝑖, 𝑑𝑖, and 𝜎𝑖2 are defines the data likelihood function, denotes the Gaussian 
probability density function, represent the 𝑖-th modeled response and observed data,  and the variance 
characterizing the uncertainty or noise of the 𝑖-th measurement, respectively. 
The final stage of this probabilistic petrophysical inversion workflow entails estimating the comprehensive 
probability distribution of the network parameters by applying Bayes' theorem  (Li et al., 2024). Conditioned on 
the observed data 𝑑, the posterior distribution of the network parameters 𝜃 is evaluated via the following 
expression: 
𝑃(𝜃|𝑑) = 𝑃(𝑑|𝜃)𝑃(𝜃) 𝑃(𝑑)⁄                          (13) 
where 𝑃(𝜃|𝑑), 𝑃(𝜃), and 𝑃(𝑑) are defines the posterior probability distribution, represents the prior probability, 
and denotes the marginal likelihood, often referred to as the Bayesian evidence, respectively. 
2.1 Model hyperparameter estimation 
The proposed computational framework bypasses the conventional seismic inversion by introducing a direct 
petrophysical inversion approach (Grana et al., 2022). Instead of first extracting elastic properties ( 𝑉𝑝, 𝑉𝑠, and 𝜌) 
from seismic amplitudes and subsequently deriving petrophysical parameters through empirical relations, the 
artificial neural network comprising Convolutional Neural Networks (CNN) and Gated Recurrent Units (GRU)  
directly interprets pre-stack seismic data (near, mid, and far partial stacks)  (Zhang & Curtis 2021). Through this 
direct mapping, the neural network functions as an inverse model that outputs simultaneous predictions for 
porosity ( 𝜙), clay volume ( 𝑉𝑐𝑙𝑎𝑦), and water saturation ( 𝑆𝑤) in a single computational step, avoiding the 
propagation of errors inherent in intermediate deterministic calculations (Grana et al., 2022).

574 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
Within this Bayesian Neural Network (BNN) framework, the fundamental physical laws are exclusively 
utilized as an evaluation mechanism rather than for direct prediction (Romero et al., 2025) . The output 
variables from the neural network are fed into a forward physical model to validate their geological 
plausibility (Gou et al., 2022) . Specifically, the predicted petrophysical parameters ( 𝜙, 𝑉𝑐𝑙𝑎𝑦, and 𝑆𝑤) serve 
as inputs for the Dvorkin -Gassmann soft sand model  (Li et al., 2024) , which translates these compositional 
and fluid properties into elastic wave velocities ( 𝑉𝑝, 𝑉𝑠) and bulk density ( 𝜌). Subsequently, the Aki-Richards 
approximation calculates the angle -dependent reflection coefficients to generate synthetic partial -stack 
seismic traces (Li et al., 2024) . The algorithm then compares these synthetic traces with the observed field 
data, utilizing the misfit to backpropagate and adjust the neural network weights if the physical constraints 
are violated (Zhang & Curtis 2021) . 
To establish a robust baseline and isolate the network's internal predictive capability, a purely data -driven 
mode can be implemented by bypassing the forward seismic modeling operators (Simutė et al., 2023) . In this 
configuration, the objective function minimized by the optimization algorithm depends solely on the 
petrophysical prediction error, devoid of physical regularizers (Grana et al., 2022) . The total loss function is 
mathematically defined as:  
ℒ𝑡𝑜𝑡𝑎𝑙 = 𝛼ℒ𝑝𝑟𝑜𝑝𝑒𝑟𝑡𝑦                                              (14) 
where ℒ𝑡𝑜𝑡𝑎𝑙, and ℒ𝑝𝑟𝑜𝑝𝑒𝑟𝑡𝑦 are denotes the overall loss value optimized by the network during training, and 
represents the data -driven property loss function. The symbol 𝛼 is a user  defined hyperparameter weight that 
controls the strictness of the model in fitting the well log data constraints, respectively. 
This data-driven evaluation relies on the Mean Squared Error (MSE) to quantify the discrepancy between the 
neural network predictions and the actual well log targets  (Zhang & Curtis 2021) . The property loss function 
accounts for the three predicted parameters across all temporal samples and seismic traces within a given training 
batch (Romero et al., 2025). The formulation is expressed as: 
ℒ𝑝𝑟𝑜𝑝𝑒𝑟𝑡𝑦 = MSE(mˆ , m) = 1𝑁×𝑁𝑡 ∑ ∑ ∑ (𝑚ˆ 𝑖,𝑡,𝑗 − 𝑚𝑖,𝑡,𝑗)23𝑗=1𝑁𝑡𝑡=1𝑁𝑖=1                 (15) 
where mˆ , m, denote the overall predicted, true petrophysical property matrices, respectively. Specifically, 𝑚ˆ 𝑖,𝑡,𝑗 
represents the predicted value of property index 𝑗 (where 𝑗 = 1 corresponds to 𝜙, 𝑗 = 2 to 𝑉𝑐𝑙𝑎𝑦, and 𝑗 = 3 to 𝑆𝑤) 
at time or depth sample 𝑡 within the seismic trace 𝑖. The parameter 𝑚𝑖,𝑡,𝑗 denotes the corresponding true target 
value derived from the training well logs. The variables 𝑁 and 𝑁𝑡 represent the total number of spatial seismic 
traces in a single training batch and the total number of temporal samples per trace, respectively. 
Although the employed loss function resembles that of a standard deterministic neural network, the Bayesian 
nature of the framework is rigorously derived from its stochastic architecture (Chala & Ray 2025). During training, 
the network optimizes the standard MSE; however, Bayesian inference is achieved through the continuous 
application of Monte Carlo (MC) Dropout before each evaluation layer (Grana et al., 2022) . From a theoretical 
perspective, minimizing the MSE combined with L2 regularization applied via the weight decay parameter in the 
Adam optimization algorithm is mathematically equivalent to maximizing the Evidence Lower Bound (ELBO) in 
Variational Inference (Li et al., 2024). This structural approach allows the network to capture complex predictive 
distributions without the profound computational burden of explicitly calculating variational divergence integrals 
(Zhang & Curtis 2021). 
During the inference phase, the stochastic nature of the network is leveraged to quantify model 
uncertainty and extract robust petrophysical mappings (Grana et al., 2022) . The predictive mean and its 
associated epistemic uncertainty are obtained by performing multiple stochastic forward passes (MC Loop) 
on the same input data, intentionally deactivating random neurons in each iteration (Li et al., 2024) . The 
expected value of the target property prediction is approximated by the empirical mean of these stochastic 
realizations (Li et al., 2024) :

575 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
𝔼[mˆ ] ≈ 1𝑁𝑀𝐶 ∑ mˆ 𝑘𝑁𝑀𝐶𝑘=1                                        (16) 
where 𝔼[mˆ ] denotes the expected value (predictive mean) of the petrophysical properties. The term 𝑁𝑀𝐶 
represents the total number of Monte Carlo simulation iterations (realizations) performed during the inference 
phase, and the symbol mˆ 𝑘 represents the stochastic property vector output generated at the 𝑘-th iteration. This 
methodology ensures that the final inversion results are grounded in probabilistic estimation, providing critical 
uncertainty quantification for advanced reservoir characterization. 
Figure 3  illustrates the proposed data -driven Bayesian Neural Network (BNN) workflow utilized for the 
stochastic inversion of petrophysical properties. The architecture takes seismic partial stacks (near, mid, and far 
incident angles) as inputs. Unlike deterministic networks, the hidden layers of the BNN represent their weights as 
probability distributions, employing Monte Carlo dropout to generate an ensemble of predictive realizations. 
Ultimately, the network outputs the estimated petrophysical properties  which are iteratively optimized by 
minimizing a data -driven objective function, defined by the Mean Squared Error (MSE) between the predicted 
spatial properties and the actual well log measurements. 
 
Figure 3. 
Workflow of the Bayesian Neural Network (BNN) process 
 
 
3. Result and discussion 
Synthetic Seismic Data Analysis 
The generated synthetic seismic gathers (Figure 2), augmented to simulate 100 Common Depth Points (CDPs), 
are subsequently utilized to generate partial stacks. To realistically represent lateral variation (heterogeneity) 
typical of actual reservoirs, this initial setup employs a continuous "layer -cake" ge ological model. This step 
ensures that while the base geological framework remains horizontally stratified and continuous, the seismic 
amplitudes and waveforms vary laterally from trace to trace. 
Utilizing these 100 heterogeneous CDPs to generate the partial stacks is crucial; it provides a controlled 2D 
spatial window to test the BNN’s lateral stability , and its capability to capture continuous uncertainty bounds 
across laterally varying seismic responses before analyzing the final prediction results. This partial stacking 
procedure involves integrating the synthetic angle gathers over specific angular b ounds. Stacking is performed 
across incidence angles of 0° –15° to derive the near -angle stack, 15°–30° for the mid -angle stack, and 30° –45° 
for the far-angle stack (Figure 4).

576 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 The synthesized seismic amplitudes span a range of 1 to -1, exhibiting distinct variations across the strata. At 
the lithological boundaries, the seismic response manifests as a trough for sandstone intervals and a peak for shale 
formations. This polarity behaviour is dictated by the use of a zero-phase wavelet featuring a dominant frequency 
of 30 Hz (Figure 4). Notably, the amplitude signature within the gas-saturated reservoirs displays a substantially 
stronger negative magnitude relative to the water-bearing reservoirs (Figure 4). 
In addition to the partial stack seismic data, the BNN inversion framework also requires input from 
petrophysical properties. For the purpose of this study, the predefined petrophysical properties (Table 1)  are 
augmented to match the spatial dimensions of the partial stack data, yielding an ensemble of 100 seismic traces 
(Figure 4). In field-scale applications, this population procedure is typically achieved via geostatistical simulation. 
Integrating data from a dense well network, characteristic of development fields, significantly enhances the 
accuracy of the resulting spatial model. 
To comprehensively evaluate the robustness of the BNN inversion framework, this baseline layer-cake model 
will be systematically compared against a more complex structural model. This subsequent structural model 
incorporates a normal fault to simulate real istic geological traps, wherein the footwall acts as a gas -saturated 
reservoir and the hanging wall represents a brine -bearing zone devoid of hydrocarbons. Comparing these two 
scenarios allows for a critical assessment of the BNN’s performance in resolving  both laterally continuous 
formations and abrupt structural discontinuitie. 
 
Figure 4. 
Seismic partial angle stacks for the layer-cake model: 
(a) Near-angle stack, (b) Mid-angle stack, and (c) Far-angle stack; alongside the corresponding petrophysical sections: 
(d) Porosity, (e) Clay volume, and (f) Water saturation 
 
To quantify the predictive uncertainty, the Monte Carlo (MC) sampling technique was employed with 50 
realizations. This specific number of iterations was selected to optimize computational efficiency while still 
generating a robust probability distribution for the targeted rock properties. By injecting stochasticity into the 
network during each realization, the model produces a range of outputs, allowing for the estimation of the posterior 
distribution and the extraction of the mean prediction, albeit with a slightly lower probability curve resolution 
compared to higher iteration counts. The training phase was configured with a maximum of 150 epochs, limiting 
the number of complete learning passes through the entire dataset. The learning objective in this BNN approach

577 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
was governed exclusively by the property loss, which was scaled by a weighting parameter 𝛼 set to 1. This 
parameter serves as a definitive multiplier for the Mean Squared Error (MSE) computed between the predicted 
network outputs and the actual well log data.  
Table 2. 
Performance Evaluation of BNN Hyperparameters for Layer Cakes Model 
 Porosity Clay volume Water stauration 
RMSE 0.0203 0.0350 0.0366 
R2 Score 0.9598 0.9891 0.9867 
Pearson (r) 0.9845 0.9963 0.9959 
 
Furthermore, the optimization process utilized a batch size of 30, indicating that the network's weights were 
updated iteratively after evaluating subsets of 30 samples. This mini -batch gradient descent approach was 
implemented to ensure stable optimization steps and manage computational memory usage effectively during the 
training process. 
The foundation of the model's predictive capability relies heavily on the training dataset, which is initially 
anchored by data extracted from 15 selected wells. In data -driven architectures such as BNNs, maximizing the 
volume and diversity of training dat a directly enhances the network's predictive accuracy and generalization. 
However, relying solely on isolated well logs is insufficient to capture continuous spatial heterogeneity. To 
adequately represent this geological heterogeneity  and to simulate pract ical field conditions where well data is 
typically sparse, these 15 wells serve as primary geostatistical control points. The training dataset is subsequently 
expanded by extracting additional samples along the seismic traces, where the corresponding petrophysical target 
values are populated based on spatial geostatistical distributions derived from the initial well data. This approach 
ensures that the BNN is trained on a comprehensive, heterogeneous dataset that bridges the spatial gaps between 
well locations. 
Given the relatively abbreviated training duration of 150 epochs, the network's capacity to fully generalize the 
subsurface heterogeneity from these 15 training wells is a critical point of evaluation. Subsequent monitoring of 
the loss convergence curve is imperative to ensure that the model does not exhibit underfitting and has adequately 
captured the essential data features. 
The application of the BNN framework with the specified parameters results in an average Root Mean Square 
Error (RMSE) of 0.03 (a 3% error rate) across the predictions of the three petrophysical properties. Additionally, 
the average coefficient of determin ation (𝑅2) is 0.9, indicating that 90% of the data variance is successfully 
explained by the model. These evaluation metrics demonstrate a robust predictive performance for porosity, clay 
volume, and water saturation. A comprehensive summary of these quantitative results is presented in Table 2. 
The loss convergence curve (Figure 5)  illustrates that the BNN model has undergone optimal and stable 
learning without exhibiting any signs of overfitting or underfitting. From the initiation of training until 
approximately epoch 30, both the training and validation losses undergo a steep, co ncurrent decline, 
demonstrating the network's swift capacity to delineate the non-linear patterns within the petrophysical data. 
Subsequent to epoch 40 and extending to the final training limit at epoch 150, both curves flatten 
asymptotically towards zero and remain closely superimposed. This seamless convergence validates that the 
prescribed hyperparameter configuration is sufficient to establish an equilibrium state, thereby substantiating the 
model's robust generalization ability when applied to unseen well log data. 
Petrophysical property estimations obtained via the Bayesian Neural Network (BNN) framework demonstrate 
an exceptional degree of fidelity to the ground -truth data (Figure 6).  This synthetic dataset is ideal for BNN 
training because it combines complex, non -linear rock physics relationships with error -free labels. Furthermore, 
integrating geostatistical variance simulates the inherent ambiguity of real seismic data, providing th e perfect 
environment for the BNN to simultaneously learn deterministic mappings and explicitly quantify underlying 
uncertainties via probabilistic bounds (e.g., P10 and P90) . Analysis of the 1D vertical profiles for porosity, clay

578 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
volume, and water saturation reveals that the mean prediction curve accurately delineates both the macroscopic 
trends and localized anomalies of the reference well across the seismic time interval.  
A notable merit of this architecture is its proficiency in resolving sharp lithological boundaries and abrupt 
property transitions, such as the distinct step -like changes observed at approximately 1.78 s, 1.84 s, and 1.91 s 
(Figure 6). The network effectively reconstructs these high -frequency features without suffering from excessive 
smoothing, thereby preserving the vertical integrity of the target strata. Unlike conventional model -based 
inversions that rely heavily on low -frequency sta rting models and strict deterministic regularizations that 
inherently dampen sharp boundaries, the BNN directly maps band -limited seismic responses to broadband well 
log properties. Furthermore, by drawing stochastic realizations from the posterior weight distributions, the BNN 
preserves the sharp, non -linear petrophysical contrasts (such as abrupt gas -sand interfaces) across individual 
predictions, avoiding the over-smoothed outputs typical of single-point deterministic averaging. 
 
 
Figure 5. 
Training and validation loss convergence curves 
 
Beyond yielding precise mean predictions, the deployment of this stochastic framework proves highly robust 
in uncertainty quantification. The uncertainty bands, defined by the P10 and P90 percentiles (Figure 6) , 
comprehensively encapsulate the probabilistic output range of the model, effectively providing a range of possible 
realizations. Crucially, the ground -truth logs consistently fall within this confidence interval across the entire 
profile, corroborating the validity of the model's statistical inferences. 
The well -calibrated, relatively uniform width of the uncertainty bounds signifies a consistent degree of 
predictive confidence throughout the reservoir interval. This behaviour validates the stability of the BNN 
architecture (Figure 6), demonstrating its capacity for robust generalization while simultaneously mitigating the 
risks of overconfidence or overfitting. Such stability is particularly vital when characterizing complex geological 
environments, ensuring that the model provides reliable estimates for both lithology and fluid content. 
Quantitative assessment via residual point plots on the blind well substantiates the outstanding precision of 
the developed inversion framework (Figure 7) . The scatter distribution of the residual points across all three 
petrophysical properties is densely and symmetrically clustered around the zero-error reference line. Notably, for 
porosity and water saturation estimates, the vast majority of deviations are confined to a highly constrained margin 
(ranging from -0.05 to 0.05 v/v).

579 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
This uniform dispersion, lacking any severe directional skew, demonstrates that the model is fundamentally 
devoid of detrimental systematic bias (Figure 7). The network displays no persistent propensity for aggregate 
overestimation or underestimation; rather, the remaining minor random errors merely characterize the acceptable 
bounds inherent to the stochastic nature of Bayesian modeling. 
Furthermore, the 1D spatial analysis of the residual plots facilitates the precise localization of geological 
intervals characterized by peak reconstruction complexity. It is apparent that the marginally more pronounced 
residual spikes (approaching ± 0.1 v /v), particularly within the clay volume profile, are acutely localized and 
strictly confined to time intervals of approximately 1.78 s, 1.84 s, and 1.91 s. These localized deviation maxima 
directly correlate with stratigraphic lithology interfaces where the ground-truth data display abrupt, discrete shifts 
in petrophysical properties (blocky transitions). 
The observation that the maximum errors are strictly isolated at these layer boundaries with their magnitudes 
firmly maintained within a highly acceptable analytical tolerance further corroborates the robust validity of the 
model in reconstructing subsurface formation heterogeneity without introducing spurious computational artifacts. 
Following the initial validation, the BNN inversion framework was deployed across the full spatial extent of 
the partial stack seismic data. This yielded 2D petrophysical property sections for the P10, P90, and mean values, 
aggregated from 50 stochastic realizations (Figure 8). The performance of the BNN inversion was then rigorously 
evaluated by comparing the predicted outputs against the ground-truth well data across the entire seismic volume. 
The 2D spatial distribution of the inverted petrophysical properties demonstrates the exceptional capability of 
the Bayesian Neural Network (BNN) framework in reconstructing subsurface stratigraphy (Figure 8). A direct 
comparison between the BNN’s mean predictions and the actual ground -truth models reveals a high degree of 
spatial fidelity and lateral consistency across all seismic traces. 
 The network successfully captures the layer -cake geometries and the thicknesses of the target formations 
without introducing artificial horizontal smoothing artifacts. Sharp lithological boundaries that separate the 
sealing shale layers from the target clean sandstones clearly visible in both the clay volume and porosity profiles 
are precisely mirrored in the network's deterministic output. This confirms the proficiency of the data -driven 
architecture in handling high-frequency spatial transitions across contrasting geological facies. 
  Crucially, the effectiveness of the BNN framework is highlighted by its precision in fluid discrimination, 
which is paramount for characterizing gas -saturated sandstone reservoirs. The 2D water saturation profile 
generated by the model flawlessly identif ies and spatially localizes a distinct, massive low -saturation anomaly. 
This anomaly is sharply bounded and maintains the integrity of the fluid contacts continuously across the lateral 
extent of the target zone. 
By successfully correlating this low water saturation interval with the corresponding high porosity and low 
clay volume zones, the model unambiguously delineates the gas-bearing sandstone reservoir. The seamless match 
between the predicted spatial fluid di stribution and the true subsurface model validates the BNN's robustness in 
complex fluid and lithology identification. 
Beyond accurate deterministic mapping, the stochastic nature of the BNN provides critical spatial uncertainty 
quantification, visualized through the P10 and P90 percentile panels (Figure 8). These uncertainty bounds offer a 
continuous probabilistic assessment of the inverted properties, effectively capturing the model's predictive 
confidence. An analysis of these uncertainty profiles reveals that while the absolute property magnitudes exhibi t 
expected statistical variance, the macroscopic structural framework and the spatial integrity of the gas -saturated 
sandstone remain highly consistent.

580 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
  
Figure 6. 
1D BNN-derived petrophysical properties for layer cakes model: porosity (left), clay volume (center), and water saturation (right)

581 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
  
 
Figure 7. 
Prediction residuals for (left) porosity, (center) clay volume, and (right) water saturation, derived from actual petrophysical data.

582 
 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
Riyadi et al. Scientific Contributions Oil and Gas 
 
 
Figure 8. 
2D petrophysical sections of a layer-cake model generated via BNN inversion, illustrating the P10 stochastic realizations for (a) porosity, (b) clay volume, and (c) water saturation; the mean 
distributions for (d) porosity, (e) clay volume, and (f) water saturation; and the P90 realizations for (g) porosity, (h) clay volume, and (i) water saturation.

583 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
The critical low-saturation anomaly is robustly preserved even at the outer confidence limits (P10 and P90), 
significantly reducing interpretive ambiguity. This uniform and narrow confidence interval across the traces 
proves that the network generalizes well spatially without suffering from instability or overfitting. Consequently, 
this distinguishing characteristic sets the BNN framework apart, as it uniquely yields comprehensive uncertainty 
quantification alongside the derived petrophysical properties. 
These preliminary findings necessitate further investigation, particularly through the integration of field -
acquired seismic data, which is inherently subjected to recording noise. The current synthetic modelling 
framework does not fully account for such noise characteristics, and therefore may not perfectly mirror real-world 
subsurface conditions. Nonetheless, this study provides robust validation that the probabilistic BNN inversion 
framework is a highly viable approach for characterizing gas-saturated hydrocarbon reservoirs. 
In addition to using the layer-cake model, a comparison will be made with another model. This second model 
adds random noise and a fault that separates the gas -filled sandstone layer in the footwall from the brine zone in 
the hanging wall (Figure 9) . This model was created to represent subsurface conditions that resemble actual 
measured seismic data. 
This complex model is constructed utilizing control data from two synthetic wells: Well -20 located in the 
footwall block and Well-70 situated in the hanging wall block. The petrophysical properties of Well-20 replicate 
those of the baseline model shown in Figure 2 , featuring a gas -saturated sandstone reservoir in layer 4 with 
correspondingly low water saturation. Conversely, Well -70 simulates a non -hydrocarbon-bearing scenario , 
wherein the sandstone interval is entirely devoid of gas and reaches a water saturation of 100% (Figure 9). 
 
 
Figure 9. 
Seismic partial angle stacks for faulted and noisy model: 
(a) Near-angle stack, (b) Mid-angle stack, and (c) Far-angle stack; alongside the corresponding petrophysical sections: (d) 
Porosity, (e) Clay volume, and (f) Water saturation

584 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
The seismic data configuration for this second model is identical to the initial layer -cake model, generated 
using 100 CDPs across an angle range of 0 to 45 degrees. The 100 CDPs are incorporated to evaluate the BNN's 
lateral performance, mimicking field -acquired seismic data. Furthermore, the 0 to 45 -degree angle range was 
selected to optimize the BNN process and accurately represent real seismic data, which typically reaches a 
maximum angle of 45 degrees. 
The synthetic seismic data from the second model is subsequently processed into partial angle stacks, 
which serve as the primary input for the BNN inversion framework (Figure 9) . The resulting partial stacks 
for this complex model exhibit amplitude signatures that are distinctly different from those of the baseline 
layer-cake model . 
Table 3. 
Performance evaluation of bnn hyperparameters for faulted and noisy model 
 
Porosity Clay volume Water stauration 
Well-20 Well-70 Well-20 Well-70 Well-20 Well-70 
RMSE 0.078 0.142 0.104 0.156 0.088 0.152 
R2 Score 0.815 0.725 0.775 0.685 0.810 0.690 
Pearson (r) 0.903 0.851 0.880 0.828 0.900 0.831 
 
The difference is clearly visible from the amplitudes, which are not as neat and sharp as in the first model. The 
near-angle partial stack results do not show a significant change between the footwall and hanging wall positions. 
However, the mid- and far-angle partial stack results show a substantial amplitude difference in the footwall area 
compared to the hanging wall area, especially at the transition from layer three to layer four (Figure 9). 
Following the application of the BNN process using parameters identical to those of the first (layer -cake) 
model, the performance evaluation metrics for the two control wells (Well -20 and Well-70) were derived (Table 
3). The analysis of Well-20 reveals a different degree of accuracy compared to the layer-cake model; the predictive 
errors for the three properties are higher, yielding an average RMSE of 0.09 (a 9% error margin), alongside a 
reduced correlation characterized by an average R2 of 0.8 (an 80% match). Furthermore, the results for Well -70 
exhibit a substantially larger error margin, with an average RMSE of 0.15 (15%), and a comparatively lower 
correlation value with an average R2 of 0.7 (70%) when juxtaposed with the Well-20 results (Table 3). 
The 1D petrophysical property predictions for the blind-test wells (Well-20 and Well-70) demonstrate the high 
fidelity and reliability of the proposed Bayesian Neural Network (BNN) framework. As illustrated in Figure 10, 
the predicted mean curves closely track the actual well logs across the porosity, clay volume, and water saturation 
profiles. The model successfully reconstructs sharp, blocky lithological transitions such as the abrupt fluid and 
lithology contrasts observed between 1.75 s and 1.95 s without exhibiting severe smoothing effects. Furthermore, 
the stochastic nature of the BNN provides robust uncertainty quantification. The true log values consistently fall 
within the estimated 80% confidence intervals (bound ed by the P10 and P90 percentiles), confirming that the 
model's predictive variance is statistically reliable and successfully avoids overconfidence. 
Quantitative evaluation through the prediction residual plots (Figure 10) further validates the stability of the 
inversion model. The error distributions for all three petrophysical parameters are tightly clustered and 
symmetrically distributed around the zero -error reference line, indicating an absence of systematic bias in th e 
network's predictions. While minor local spikes in the residuals are observable (e.g., approaching ±0.1 v/v for 
clay volume), these deviations are highly localized and exclusively associated with abrupt stratigraphic boundaries 
where extreme petrophysical contrasts occur. Overall, the minimal and randomly distributed residuals confirm the 
BNN model's capability to generalize complex subsurface heterogeneities with high precision.

585 
 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
Figure 10. 
1D Bayesian Neural Network (BNN) inversion results and the corresponding prediction residuals for faulted and noisy model (a) Petrophysical property predictions (porosity, clay volume, and 
water saturation) (b) Point plot of the prediction residuals for Well-20 (c) Petrophysical property predictions for Well-70 (d) Point plot of the prediction residuals for Well-70

586 
 
 
 
https://doi.org/10.29017/scog.v49i3.2138 
Riyadi et al. Scientific Contributions Oil and Gas 
 
 
 
 
 Figure 11. 
2D petrophysical sections of a faulted and noisy model generated via BNN inversion, illustrating the P10 stochastic realizations for (a) porosity, (b) clay volume, and (c) water saturation; the 
mean distributions for (d) porosity, (e) clay volume, and (f) water saturation; and the P90 realizations for (g) porosity, (h) clay volume, and (i) water saturation.

587 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
The inclusion of noise and fault structures is hypothesized to be the primary cause for the decreased predictive 
performance in this second model compared to the layer-cake model. This observation aligns with the findings in 
(Romero et al., 2025), where the BNN inversion applied to the structurally complex Marmousi model successfully 
predicted acoustic impedance with high precision. Nevertheless, when applied to real seismic data containing 
inherent noise in the same study, the prediction results were noticeably inferior to those achieved with the 
Marmousi or other synthetic models. 
The hypothesized degradation of the BNN's predictive performance in the second model  incorporating noise 
and faults is further corroborated by (Li et al., 2024). In that study, petrophysical predictions were conducted using 
data characterized by noise and structural complexity. The resulting correlation coefficients averaged between 0.7 
and 0.8, which is strikingly similar to the findings of our second model. Notably, none of the property predictions 
in (Li et al., 2024)  study achieved a correlation of 0.9. This suggests that, generally speaking, attaining a 
correlation of 0.9, as observed in the ideal layer-cake model, is highly challenging for the BNN method. 
As with the layer-cake model, this second model also produces 2D petrophysical cross -sections (Figure 11). 
The derived P10, P90, and mean values exhibit geological structural patterns that mirror those of the input partial 
stack seismic data. Among the three estimated properties, it is evident that the porosity values predicted by the 
BNN exhibit considerable variation. Consequently, the provided information is more diverse and distinct, as the 
probabilistic approach yields an ensemble of values rather than a single deterministic output. 
While the variability observed in the clay volume and water saturation fields is less pronounced than that of 
porosity, it nevertheless facilitates a comprehensive probabilistic assessment of in -place hydrocarbon volumes  
(Figure 11). These varied in-place estimates critically influence the economic viability analysis of a hydrocarbon 
field. Consequently, production and drilling expenditures can be robustly forecasted, effectively mitigating the 
economic risks associated with subsequent production phases and overall field development strategies. 
In addition to evaluating the BNN framework across two distinct geological models, a comparative analysis 
was performed against a conventional deterministic model-based inversion. The visual comparison, presented in 
Figure 12, highlights diverging spatial patterns between the two approaches, most notably in proximity to the fault 
zone. The BNN predictions exhibit localized discrepancies within the near -fault regions. This artifact arises 
because the porosity cross -section utilized as training data (Figure 12) does not yet structurally align with the 
inherent fault trends delineated in the seismic data. 
To mitigate these discrepancies, the property model should be constrained using interpreted seismic horizons. 
Conversely, the deterministic inversion results display clearly defined fault patterns that align with geological 
concepts, as this model is inher ently constrained by seismic horizons. Nevertheless, regarding the absolute 
porosity values, the BNN -derived porosity cross -section demonstrates a higher degree of accuracy than the 
deterministic method. This improvement is particularly evident in the seco nd layer, a water -bearing sandstone 
interval. In this layer, the deterministic method underestimates the porosity compared to the actual data, whereas 
the BNN outputs accurately reflect the predefined values in Table 1. 
The underestimated porosity values observed in the deterministic inversion results can be largely attributed to 
the conversion process. In the deterministic approach, the porosity cross-section is derived by converting acoustic 
impedance values into porosity. This conversion relies on establishing a linear relationship between the porosity 
and the acoustic impedance generated by the deterministic inversion. Consequently, the accuracy of the 
conversion heavily depends on this linear correlation; a strong cor relation yields high accuracy, whereas a weak 
correlation results in an inaccurate or mismatched porosity cross-section. 
Deterministic inversion yields only a single output without providing any quantification of uncertainty. 
Conversely, the probabilistic approach generates an ensemble of values, rendering its results more advantageous 
than deterministic methods. This probab ilistic approach, coupled with uncertainty estimation, is highly essential 
for field development. Economic evaluations derived from probabilistic outputs offer a wider range of scenarios, 
delivering critical information regarding the minimum and maximum economic potential of a field. Consequently, 
the BNN method serves as an excellent solution for implementing seismic inversion in field development projects.

588 
 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
 
Figure 12. 
Comparison of porosity cross-sections derived from: (a) BNN probabilistic inversion, and (b) model-based deterministic inversion.

589 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
4. Conclusion 
The probabilistic inversion process utilizing BNN has been successfully executed on the synthetic seismic 
data. The outputs derived from this inversion include key petrophysical properties: porosity, clay volume, and 
water saturation. By leveraging these p roperties, the characteristics of gas -saturated sandstone reservoirs can be 
effectively differentiated from those of water -bearing reservoirs. Additionally, this BNN inversion generates an 
ensemble of values, enabling the probabilistic calculation of the 1 0th percentile (P10), the 90th percentile (P90), 
and the mean value across all model outputs. Among the derived probabilistic distributions, the mean realization 
exhibits the highest fidelity to the ground -truth data, rendering it directly applicable for deterministic reservoir 
characterization. However, within the context of field development, bou ndary percentiles such as P10 and P90 
are frequently employed to quantify the uncertainty associated with hydrocarbon resource estimation. Crucially, 
this probabilistic envelope provides a direct solution to the non-uniqueness problem inherent in seismic inversion. 
In complex geological settings where multiple varying petrophysical combinations yield identical seismic 
responses, deterministic models fail by forcing a single, potentially biased estimate.  
In contrast, the BNN explicitly captures and maps this ambiguity. A wide interval between the P10 and P90 
boundaries serves as a quantitative diagnostic tool, explicitly flagging zones of high geological heterogeneity and 
strong non-uniqueness. Conversely, a narrow envelope indicates regions of high predictive confidence. Therefore, 
the BNN framework solves the non -uniqueness problem not by eliminating it, but by accurately quantifying the 
full range of plausible geological scenarios. 
The probabilistic BNN inversion framework has demonstrated considerable success in characterizing gas -
saturated sandstone reservoirs. Nonetheless, further investigation into the practical deployment of this method is 
essential, fundamentally requiring the integration of field-acquired seismic and well log data. While adapting this 
methodology for alternative reservoir typologies is highly promising, it necessitates rigorous subsequent studies 
to adequately address their contrasting petrophysical and geological characteristics. 
 
5. Acknowledgement 
  The authors wish to express their gratitude to the Center for Research and Publication (PUSLITPEN) of UIN 
Syarif Hidayatullah Jakarta for supporting this research.  
 
6. Declarations 
6.1 Author contributions 
Edi Sanjaya served as the principal investigator, conceptualized the research, and oversaw the overall project 
administration. Praditiyo Riyadi was responsible for data processing, preparing the original draft, as well as 
reviewing and editing the manuscript. Fadhlur Rahman was involved in data processing and the structural editing 
of the manuscript. 
 
6.2 Funding statement 
This research was fully funded by the BOPTN research grant from UIN Syarif Hidayatullah Jakarta, Fiscal 
Year 202 3, under Decree Number U N.01/KPA/31/2023 and Contract Number B -302/LP2M-
PUSLITPEN/TL.02/2023. 
 
6.3 Competing interest 
The authors declare that they have no known competing financial interests or personal relationships that could 
have appeared to influence the work reported in this paper.

590 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
6.4 The use of AI or AI-assisted technologies 
During the preparation of this work, the authors used artificial intelligence (AI) tools to assist with the script 
development and debugging of the Python programming codes. Furthermore, AI was employed for language 
editing, grammar checking, and manuscrip t formatting. After using these tools, the authors reviewed and edited 
the content as needed and take full responsibility for the scientific content, interpretation, and conclusions of 
the publication.  
 
7. Glossary of terms & symbols 
 Terms & 
symbols Definition Unit 
 Vp Compressional (P-wave) velocity km/s or m/s 
 Vs Shear-wave velocity km/s or m/s 
 ϕ Total porosity fraction fraction, % or v/v 
 Vcl Clay volume fraction fraction or v/v 
 ρ Bulk density g/cc 
 ρma Rock matrix density g/cc 
 ρquartz Density of quartz minerals g/cc 
 ρclay Density of clay minerals g/cc 
 ρfl Fluid density in the rock g/cc 
 Sw Water saturation fraction, % or v/v 
 ρwater Water density g/cc 
 ρhc Hydrocarbon density g/cc 
 ρbulk Bulk density (function of pore fluid and solid rock matrix densities) g/cc 
 Rθ Angle-dependent reflection coefficient - 
 R0 Amplitude Variation with Angle (A V A) intercept - 
 G Amplitude Variation with Angle (A V A) gradient - 
 θ Angle of incidence ° 
 P(m|d) Posterior probability distribution of the model parameters - 
 P(m) Prior model probability distribution - 
 P(d|m) Data likelihood function - 
 P(d) Marginal likelihood of the data (evidence) - 
 Pa Acceptance probability in Metropolis-Hastings algorithm - 
 mi Current model (current state) - 
 m' Newly proposed model (proposed state) - 
 g Proposal distribution (MCMC) / Non-linear activation function - 
 f Deterministic rock physics forward modeling operator - 
 z Hidden states in neural network - 
 w Trainable weight matrices - 
 b Bias vectors - 
 σi² Variance characterizing the uncertainty or noise of the measurement - 
 α User-defined hyperparameter weight controlling well log constraint strictness - 
 Ltotal Overall loss value optimized by the network - 
 Lproperty Data-driven property loss function - 
 Em Expected value (predictive mean) of petrophysical properties - 
 NMC Total number of Monte Carlo simulation iterations - 
 mk Stochastic property vector output generated at the k-th iteration - 
 N Total number of spatial seismic traces in a single training batch - 
 Nt Total number of temporal samples per trace - 
 
 
8. References 
Andrieu, J., Kutzky, B., Schackmann, B. T., Ag, G., Mahardhini, ; A, Abidiy, I., & Poitrenaud, H. M. (2018). 
Tunu: From Lab to Field Application with a New Hybrid Inorganic -Organic Sand Consolidation Fluid as 
Primary Treatment on Shallow Reservoirs. 2, 189548. http://onepetro.org/SPEFD/proceedings-pdf/18FD/2-
18FD/D021S012R002/1213502/spe-189548-ms.pdf.

591 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
Chala, A. T., & Ray, R. (2025). Uncertainty Quantification in Shear Wave Velocity Predictions: Integrating 
Explainable Machine Learning and Bayesian Inference. Applied Sciences (Switzerland), 15(3). 
https://doi.org/10.3390/app15031409. 
Coimbra, A., & Sampaio, M. A. (2025). Reservoir characterization based on data incorporation throughout 
production development. Geoenergy Science and Engineering, 252, 213911. 
https://doi.org/https://doi.org/10.1016/j.geoen.2025.213911. 
Fariz, M., Zera, T., & Purba, H. (2022). Analisis Penyebaran Reservoir Batupasir Dan Karbonat Menggunakan 
Metode Inversi Seismik Studi Kasus : Lapangan RB, Blok Rangkas. Lembaran Publikasi Minyak Dan Gas 
Bumi, 56(2), 61–75. https://doi.org/10.29017/LPMGB.56.2.959. 
Fernandes, F. J. D., Teixeira, L., Freire, A. F. M., & Lupinacci, W. M. (2024). Stochastic seismic inversion and 
Bayesian facies classification applied to porosity modeling and igneous rock identification. Petroleum Science, 
21(2), 918–935. https://doi.org/10.1016/j.petsci.2023.11.020. 
Gou, R., Zhang, Y., Zhu, X., & Gao, J. (2022). Bayesian Physics -Informed Neural Networks for the Subsurface 
Tomography based on the Eikonal Equation. https://doi.org/10.1109/TGRS.2023.3286438 
Grana, D., Azevedo, L., De Figueiredo, L., Connolly, P., & Mukerji, T. (2022). Probabilistic inversion of seismic 
data for reservoir petrophysical characterization: Review and examples. Geophysics, 87(5). 
https://doi.org/10.1190/geo2021-0776.1. 
Han, D., Nur, A., & Morgan, D. (1986). Effects of porosity and clay content on wave velocities in sandstones. 
Geophysics, 51(11), 2093–2107. https://doi.org/10.1190/1.1442062 
Horozal, S., Chae, S., Kim, D. H., Seo, J. M., Lee, S. M., Han, H. S., Cukur, D., & Kong, G. S. (2021). Seismic 
evidence of shallow gas in sediments on the southeastern continental shelf of Korea, East Sea (Japan Sea). 
Marine and Petroleum Geology, 133. https://doi.org/10.1016/j.marpetgeo.2021.105291 
Jin, H., Liu, C., & Guo, Z. Q. (2024). Gas prediction in tight sandstones based on the rock-physics-derived seismic 
amplitude variation versus offset method. Petroleum Science, 21(6), 3951 –3964. 
https://doi.org/10.1016/j.petsci.2024.06.006. 
Kuai, Z. Y., Cao, D. P., & Jin, C. (2025). Joint inversion with prestack waveform and spectral information for 
layered media. Petroleum Science, 22(10), 4065–4082. https://doi.org/10.1016/j.petsci.2025.06.004 
Laidlaw, D., Madyanova, M., Agee, D., & Hustache, H. (2012). Combination of Dual String Single Trip Multi -
Zone Completion Systems and High Rate Formation Pack as a Proven Completion Methodology for an 
Unconsolidated Reservoir: Case Study Tunu Field. https://doi.org/10.2118/155202-MS 
Li, P., Grana, D., & Liu, M. (2024). Bayesian neural network and Bayesian physics-informed neural network via 
variational inference for seismic petrophysical inversion. Geophysics, 89(6), M185 –M196. 
https://doi.org/10.1190/geo2023-0737.1 
Li, P., Liu, M., Alfarraj, M., Tahmasebi, P., & Grana, D. (2024). Probabilistic physics -informed neural network 
for seismic petrophysical inversion. Geophysics, 89(2), M17–M32. https://doi.org/10.1190/geo2023-0214.1 
Liu, J., Gui, Z., Gao, G., Li, Y., Wei, Q., & Liu, Y. (2023). Predicting Shear Wave Velocity Using a Convolutional 
Neural Network and Dual -Constraint Calculation for Anisotropic Parameters Incorporating Compressional 
and Shear Wave Velocities. Processes, 11(8). https://doi.org/10.3390/pr11082356 
Lowrie, W., & Fichtner, A. (2020). Fundamentals of Geophysics (3rd ed.). Cambridge University Press. 
https://doi.org/DOI: 10.1017/9781108685917 
Mahmud, H. Ben, Bin Muhammad Hisham, M. H., Mahmud, W. M., Leong, V. H., & Shafiq, M. U. (2020). 
Petrophysical interpretations of subsurface stratigraphic correlations, Baram Delta, Sarawak, Malaysia. 
Energy Geoscience, 1(3–4), 100–114. https://doi.org/10.1016/j.engeos.2020.04.005

592 
 
 
 
Riyadi et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2138 
 
 
 
Putra, H. A., Sanjaya, E., Suwondo, Nafian, M., Riyadi, P., & Atmoko, W. (2026). Seismic -Based Reservoir 
Characterization of The Lower Arang Formation in West Natuna Basin Using Acoustic Impedance Inversion 
and Seismic Attributes. Scientific Contributions Oil and Gas, 49(2), 353 –375. 
https://doi.org/10.29017/scog.v49i2.2065 
Romero, J., Heidrich, W., & Ravasi, M. (2025). Bayesian seismic inversion with implicit neural representations. 
Geophysical Journal International, 242(3). https://doi.org/10.1093/gji/ggaf249 
Shan, H., Sun, Y., Li, B., Wang, H., & Zhang, G. (2026). Enhancing marine shallow gas production through 
hybrid vertical and horizontal wells. Applied Ocean Research, 170. 
https://doi.org/10.1016/j.apor.2026.105027 
Siahgoli, H. M., Riahi, M. A., Nabi-Bidhendi, M., & Seyedali, S. (2025). Integrating Bayesian classification and 
ANN for lithofacies classification using well and seismic data: Bahregansar case study. Discover Applied 
Sciences, 7(4). https://doi.org/10.1007/s42452-025-06701-2 
Simutė, S., Boehm, C., Krischer, L., Gokhberg, A., Vallée, M., & Fichtner, A. (2023). Bayesian Seismic Source 
Inversion With a 3 -D Earth Model of the Japanese Islands. Journal of Geophysical Research: Solid Earth, 
128(1). https://doi.org/10.1029/2022JB024231 
Sukma, R. F. N., Rosid, M. S., & Wijanarko, E. (2025). Telisa Formation Characterization Using Seismic Acoustic 
Impedance Inversion In The Akasia Area of The Central Sumatra Basin. Scientific Contributions Oil and Gas, 
48(2), 29–40. https://doi.org/10.29017/scog.v48i2.1774 
Sun, Y. ( 孙有壮), Pang, S. ( 庞善臣), Zhang, J. ( 张军华), & Zhang, Y. ( 张永安). (2024). Porosity prediction 
through well logging data: A combined approach of convolutional neural network and transformer model 
(CNN-transformer). Physics of Fluids, 36(2), 026604. https://doi.org/10.1063/5.0190078 
Taqiy, Z. F., Utomo, W., Shidqii, M., & Susilo, A. (2026). Karakterisasi Reservoir Berdasarkan Analisis Inversi 
Seismik Impedansi Akustik dan Multiatribut Seismik, Studi Kasus: Lapangan Bunyu Tapa, Cekungan 
Tarakan, Kalimantan Utara. Lembaran Publikasi Minyak Dan Gas Bumi, 59(3), 23 –40. 
https://doi.org/10.29017/lpmgb.59.3.1891 
Widarsono, B., Musu, J. T., & Yohanes, Y. D. W. (2025). Rock Compressibility Characteristics of Oil and Gas 
Sandstone Reservoirs in the Western Part of Indonesia. Scientific Contributions Oil and Gas, 48(4), 77 –93. 
https://doi.org/10.29017/scog.v48i4.1936 
Xiang, Y., Song, Z., Wang, Z., & Song, G. (2026). Residual Physics -Informed Neural Networks for Seismic 
Tomography with Multi-Source Prior Constraints. Mathematics, 14(8). https://doi.org/10.3390/math14081392 
Yu, W. (2024). Common Misconceptions on Rules of Mixtures for Predicting Elastic Properties of Composites. 
AIAA Journal, 62(5), 1982–1987. https://doi.org/10.2514/1.J063863 
Yusof, M. A., Agi, A., Gbadamosi, A., Junin, R., & Abbas, A. (2018). Uncertainty analysis of hydrocarbon in 
place calculation using 3D seismic and well data during appraisal stage – Case study of Goldie Field, offshore 
Sarawak. Journal of Natural Gas Science and Engineering, 57, 238 –265. 
https://doi.org/https://doi.org/10.1016/j.jngse.2018.06.038 
Yuwono, R. W., Fitriana, B. S., Kirana, P. S., Djaelani, S., & Sjafwan, B. A. (2012). Biogenic Gas Exploration 
and Development in Bentu PSC, Central Sumatra Basin, Indonesia*. 
Zhang, X., & Curtis, A. (2021). Bayesian Geophysical Inversion Using Invertible Neural Networks. Journal of 
Geophysical Research: Solid Earth, 126(7). https://doi.org/10.1029/2021JB022320
