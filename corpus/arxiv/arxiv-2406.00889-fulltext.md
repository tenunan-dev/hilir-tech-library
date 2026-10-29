---
source_id: "arxiv"
title: "RESERVOIR HISTORY MATCHING OF THE Norne FIELD WITH"
url: "https://arxiv.org/abs/2406.00889"
retrieved_at: "2026-10-28T00:00:00+00:00"
licence: "arXiv-non-exclusive"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["H2"]
disciplines: ["PRC"]
collected: "manual"
summary: "Full-text conversion of arXiv 2406.00889. Abstract: RESERVOIR HISTORY MATCHING OF THE Norne FIELD WITH
GENERATIVE EXOTIC PRIORS AND A COUPLED MIXTURE OF
EXPERTS - PHYSICS INFORMED NEURAL OPERATOR FORWARD
MODEL
Clement Etienam
Nvidia
cetienam@nvidia.com
Yang Juntao
Nvidia
yjuntao@nvidia.com
Oleg Ovcharenko
Nvidia
oovcharenko@nvidia.com
Issam Said
Nvidia
Isaid@nvidia.com
ABSTRACT
We have developed a novel reservoir characterization workflow that solv"
---

# RESERVOIR HISTORY MATCHING OF THE Norne FIELD WITH

RESERVOIR HISTORY MATCHING OF THE Norne FIELD WITH
GENERATIVE EXOTIC PRIORS AND A COUPLED MIXTURE OF
EXPERTS - PHYSICS INFORMED NEURAL OPERATOR FORWARD
MODEL
Clement Etienam
Nvidia
cetienam@nvidia.com
Yang Juntao
Nvidia
yjuntao@nvidia.com
Oleg Ovcharenko
Nvidia
oovcharenko@nvidia.com
Issam Said
Nvidia
Isaid@nvidia.com
ABSTRACT
We have developed a novel reservoir characterization workflow that solves the reservoir history
matching problem coupling a physics Informed neural operator (PINO) forward model with a mixture
of experts’ approach termed cluster classify regress (CCR). The inverse modelling is computed via an
adaptive Regularized Ensemble Kalman inversion (aREKI) method, and the method is optimal for
rapid inverse uncertainty quantification tasks during reservoir history matching. We parametrize the
unknown permeability and porosity fields for the case of sampling non-gaussian posterior measures
by using, for instance, a variational convolution autoencoder and another instance using a denoising
diffusion implicit model (DDIM). The CCR serves as exotic priors in the inverse modelling and as
a coupled supervised model with the prior PINO surrogate for replicating the nonlinear Peaceman
well equations in the forward model. The CCR is flexible, and any separate and independent machine
learning algorithm can be used for each of the 3 stages. The loss function required for the PINO
reservoir surrogate updating is obtained from the combined supervised data loss and losses arising
from the initial conditions and residual of the governing black oil pde. The output from the coupled
PINO-CCR surrogate is the pressure, water and gas saturations as well as the well outputs of oil, water,
and gas production rates. The developed methodology is first compared to a standard numerical black
oil reservoir simulator for a waterflooding case on the Norne field, and the similarity of the outputs
with those from the PINO-CCR surrogate is very close. Next, we use this developed PINO-CCR
surrogate in the developed aREKI history matching workflow. The overall workflow is successful in
recovering the unknown permeability and porosity field and simulation is very fast with a speedup of
up to 6000X to conventional numerical reservoir simulation approaches. Learning the PINO-CCR
surrogate on an NVIDIA H100 with 80G memory takes approximately 5 hours for 100 training
samples of the Norne field. The workflow is also suitable to be used in an ensemble-based workflow,
where sampling the posterior density, given an expensive likelihood evaluation, to quantify uncertainty,
as with most scientific computation, is desirable.
Keywords adaptive Regularized Ensemble Kalman Inversion, PINO, Cluster Classify Regress, Reservoir simulation,
Bayesian inverse problems
1 Introduction.
1.1 Overview
Reservoir engineers are mostly burdened with the task of developing reliable simulation models that can accurately
capture the complex dynamics of subsurface reservoir systems. The use of a set of observed measurements, ddd , to infer
a set of model parameters, mmm , is known as an inverse problem [1, 4, 5, 15, 24, 41]. Given specific observations which
are the observed data of the state variable (data that is a direct function of state variables); the aim is to infer information
about the model parameters which includes some uncertainty. The focus is on discrete inverse problems (systems
characterized by a few or a finite number of parameters). Reservoir history matching is an example of a discrete inverse
problem. In such situations, the number of data is always finite, and the data always contain some measurement errors
arXiv:2406.00889v1  [cs.LG]  2 Jun 2024

[1, 12, 15, 53, 63]. It is hence impossible to estimate the parameters of a reservoir model correctly from inconsistent,
inaccurate and insufficient data using a forward model that most likely will contain some modeling errors. In most
cases, we always have some prior information about the realism and plausibility of the reservoir model, these include a
geological model that is constructed from cores, logs and seismic data and also some information on the depositional
environment.
Reservoir history matching is the process of constraining the reservoir model to mimic actual historical dynamic
production data of the reservoir to predict its future production behavior and reduce uncertainty about the description of
the reservoirs [1, 12, 15, 53, 63]. Reservoir history matching is an ill-posed problem because the amount of independent
data available is much less than the number of variables. Hence, there exist an infinite number of combinations of
the unknown reservoir properties that result in reservoir models which can match the observations. Besides that, the
information accessible about the reservoir is always inaccurate and may be inconsistent [1, 12, 15, 53, 63]. As a result,
reservoir models are constructed with uncertain parameters; consequently, their predictions are also uncertain.
Over the last decade, increased importance has been attributed to the quantification of uncertainty in reservoir
model performance predictions and reservoir model descriptions to manage risk. Because of this obsession with the
characterization of uncertainty, it is now common to generate multiple history-matched models. However, generating
multiple history-matched models may not necessarily lead to a correct assessment of uncertainty. Uncertainty has no
scientific meaning beyond the realm of statistics and probability. Bayesian statistics provides a straightforward theory
for dealing with uncertainty.
In the application of interest, Bayes’ theorem allows one to write down the posterior probability density function (pdf)
for reservoir model parameters conditional to field measurements such as production, electromagnetic and seismic data.
Then, the optimization problem of characterizing the model uncertainty in reservoir model parameters is tantamount to
the problem of sampling this posterior pdf [4, 5, 36]. If a set of realizations of the vector of reservoir model parameters
represents a set of samples from the posterior pdf, then a correct assessment of the uncertainty in specific outcomes of
reservoir performance predictions can be generated by predicting with each model and then constructing statistics for
the set of outcomes. For example, one can estimate the pdf for a well’s predicted oil rate at each time from a histogram
of the predictions set. Markov chain Monte Carlo (MCMC) provides a theoretically attractive technique for sampling
the posterior pdf for model parameters.
It is established that a properly designed MCMC method samples this pdf correctly in the limit as the number of states
in the chain goes to infinity. For high-dimensional problems, MCMC typically requires many iterations to provide
a reasonable sampling of the desired pdf. When utilizing MCMC to compute the posterior pdf of reservoir model
parameters conditional to historical observed production data, computation of the probability of accepting the transition
from the current state to the proposed state requires a run of the reservoir model simulator to evaluate the likelihood
part associated with the posterior pdf. This requirement makes the direct application of MCMC to realistic reservoir
problems computationally prohibitive [4, 5, 36].
The modeling of flow and transport processes in subsurface formations is essential for various reservoir engineering
applications, such as oil reservoir development and carbon sequestration. Quantifying flow mechanisms in these
scenarios often requires using partial differential equations (PDEs) founded on laws of conservation. Traditionally,
PDEs have been solved numerically using methods such as finite elements, finite differences, spectral, and mesh-
less techniques. These methods have undergone significant development over the years, rendering them robust
and flexible for solving complex subsurface flow and transport problems. However numerical simulations can be
computationally demanding for large-scale simulation problems in petroleum engineering, posing challenges during
execution [48, 52, 54].
Moreover, tasks like history-matching, sensitive analysis, and project design optimization require multiple simulation
runs, leading to prohibitively inefficient computations for obtaining meaningful results [58].In recent years, data-driven
methods have garnered significant attention and achieved remarkable progress in various domains such as natural
language processing [ 19] and image classification[ 62]. Among these methods, artificial neural networks (ANNs)
have emerged as one of the most important data-driven simulation techniques due to their universal approximation
property and ability to accurately approximate any measurable function. The versatility of ANNs extends to various
science and engineering fields, demonstrating their potential in nonlinear universal approximation and data assimilation
[12].Notably, within the realm of petroleum engineering, ANNs have made substantial advancements in both forward
modeling and other applications. Dong et al.[51] proposed an enhanced artificial neural network model for predicting
CO2 minimum miscibility pressure based on the full composition of the crude oil and temperature.
Erofeev et al.[3] studied the applicability of various machine learning algorithms for predicting rock properties usually
defined by geoscientists through specialized laboratory analysis. Moosavi et al. [ 56] utilized multilayer perceptron
neural networks to accurately identify reservoir models from pressure derivative curves derived from horizontal wells.
2

Chung et al. [60] proposed a pore-scale finite volume solver to predict permeability on digital cores by solving flow
on micro-CT images. Kim et al. [33] proposed an innovative data-integration method that uses an iterative-learning
approach with a deep neural network coupled with a stacked autoencoder to address challenges encountered in many-
objective history matching. Santos et al. [32] tackled the limitation of modeling important geometries like fractures and
vuggy domains accurately using a general multiscale deep learning model that can learn from porous media simulation
data. Furthermore, Wang et al. [48] outlined an integrated method that combines predictions of fluid flow with direct
flow simulation, significantly reducing computation time without compromising accuracy. Alakeely and Horne [ 2]
examined the effectiveness of generative deep learning methods in predicting multiphase flow profiles of new wells in
unseen locations using historical production data and a variational autoencoder algorithm.
Dong et al. [51] introduced a deep reinforcement learning based approach for automatic curve matching for well test
interpretation, utilizing the double deep Q-network. Despite its remarkable advancements, the conventional data-driven
approach inevitably faces several challenges. Firstly, the data-driven model is perceived as a "black box," since it
lacks the incorporation of physical meaning of the dataset, leading to predictions that may be physically inconsistent
or implausible[42]. Secondly, the robustness of the data-driven model maybe poor, and its long-term prediction
capabilities are weak. This can be attributed to the fact that generalizing and extrapolating beyond the parameter space
of the included dataset is remain extremely challenging, as the models developed within artificial neural networks are
bounded by the parameter space of the training dataset [42, 22]. A recent and innovative neural network architecture
that embodies this concepts known as ’physics-informed neural networks’ (PINNs)[42, 22]. By incorporating PDEs,
boundary conditions, initial conditions, and other measurable prior knowledge into the loss function, PINNs seamlessly
integrate data and physics laws to construct a physics-constrained loss function based on automatic differentiation.
These algorithms not only improve the interpretability of machine learning models in terms of physical principles but
also demonstrate robustness in handling flawed data, such as missing or noisy values, outliers, and other irregularities
[42, 22].
The performance of PINNs has been demonstrated in petroleum reservoir problems associated with subsurface flow and
transport in porous media. Li et al. [31] introduced a TGNN model that integrates high-fidelity numerical simulation
data, fundamental physical laws, boundary conditions, initial conditions, expert knowledge, and engineering control
terms in the loss function, enabling the solution of two-phase subsurface f low problems at the reservoir scale beyond
the Buckleye Leverett equation. Daolun et al. [38] proposed an improved physics constrained PDE solution method by
integrating potential features of the PDE into the loss functions to alleviate the strong nonlinear problem of the flow
equation caused by the source-sink term in the single-phase homogeneous reservoir problem. Gasm and Tchelepi (2021)
[14] utilized PINNs to tackle the two-phase immiscible flow problem governed by the BuckleyeLeverett equation,
achieving physical solutions by incorporating either a diffusion term into the partial differential equations or observed
data. Almajid and Abu-Al-Saud [40] implemented a physics informed neural network technique that combines fluid
flow physics and observed data to model the Buckleye Leverett problem.
Cornelio et al. [30] developed a neural network (NN) model to learn the physical model residual errors in simulation-
based production prediction as a function of input parameters of an unconventional well. Hanna et al. [29] developed
a novel residual based adaptive PINN and compared it with the residual-based adaptive refinement (RAR) method
and a PINN with fixed collocation points. Wang et al. [ 48] proposed a theory-guided convolutional neural network
(TgCNN) framework that incorporates discretized governing equation residuals into the training of convolutional
neural networks, to extend to two-phase porous media f low problems. However, when applying PINNs to reservoir
simulation with large-scale systems and production wells, existing research typically relies on training neural networks
using high-fidelity numerical simulation data. The challenge arises from the scarcity of real reservoir data available
for training purposes, which is often limited to information such as production rates and bottomhole flow pressures.
Consequently, the accuracy of the physical information method may not always be guaranteed, when solving complex
partial differential equations (PDEs) with large-scale systems and production wells, especially in the near-well zone
where the pressure gradient is the largest. In this study, we extend the methodology proposed by Etienam et al. [12],
focusing entirely on the Norne field [64] by incorporating denoising diffusion implicit model[ 25] and variational
convolutional autoencoder [18] as generative exotic priors, we construct a forward solver surrogate that couples a
modified mixture of experts approach [ 10, 17] with the PINO to give an augmented surrogate we call PINO-CCR.
We then use the PINO-CCR surrogate in a Bayesian ensemble history matching workflow to recover the unknown
permeability,porosity and fault multipliers parameters. Our contribution includes,
1. Develop a Fourier neural operator surrogate (PINO-surrogate) trained from both the data and physics loss to
replace the black oil model reservoir equations with Nvidia Modulus framework.
2. Develop an inverse modeling workflow using the prior developed PINO surrogate together with exotic priors
to calibrate the permeability and porosity field for the reservoir under consideration.
3. Use the developed inverse modeling workflow for forward uncertainty quantification and field optimization.
3

2 Forward problem
Our simplified Black oil model for three-phase flow in porous media for reservoir simulation is given as [50, 54].
ϕ ∂Sw
∂t − ∇ · [Tw (∇Pw + ρwgk)] =Qw (1a)
ϕ ∂So
∂t − ∇ · [To (∇Po + ρogk)] =Qo (1b)
∇ ·
 ρg
Bg
Tg (∇Pg + ρggk) +RsoρgBo To (∇Po + ρogk) − Qg = − ∂∂t ϕ  ρgBg Sg + RsoρgBo So (1c)
subscript w = water,o = oil,g = gas. The system is closed by adding three additional equations Pcwo = Po − Pw;Pcog =
Pg −Po;Sw +So +Sg = 1. Gravity effects are considered by the terms ρwgk and ρogk. Ω ⊂ Rn (n = 2,3) is the modeling
domain with boundary ∂ Ω, and [0,t f ] is the time interval for which production data is available. ϕ(x) = porosity,
To,Tw,Tg and T the transmissibilities,
Tw = K(x)Krw(Sw)µw ;To = K(x)Kro(Sw)µo ;Tg = K(x)Krg(So)µg ; (2)
Assuming fault transmissibility multiplier (FTM),
T = FT M · (Tw + To + Tg) (3a)
−∇ · [T ∇P] =Q (3b)
ϕ ∂Sw
∂t − ∇ · [Tw (∇P)] =Qw (3c)
∇ ·
 ρg
Bg
Tg (∇P) +RsoρgBo To (∇P) − Qg = − ∂∂t ϕ  ρgBg Sg + RsoρgBo So (3d)
Boundary and initial conditions are given as Sw(x,0) =S0w(x);P(x,0) =P0w(x); ∇p · ν = 0. ν = outward unit normal to
∂ Ω. The overall elliptical-hyperbolic coupled PDE equations to solve are equations 3b, 3c, and 3d.
2.1 Surrogate forward modeling with a Fourier Neural operator ( FNO) - Contribution
If the notation above is clear, we now discuss thePINO model used for solving the forward problem posed in Eqn.3(b-d).
The Fourier neural operator (FNO) is effective in learning the mapping relationships between the infinite-dimensional
Figure 1: A standard Fourier neural operator (FNO) as adopted from [66]
function spaces that convert a traditional convolution operation into a multiplication operation using the Fourier
transform [66]. This causes the higher modes of the neural layer to be removed from the Fourier space, leaving only the
lower modes in the Fourier layer. Hence, FNO can greatly improve the computational efficiency of the training process.
The goal of FNO is to use a neural network G†(a) = u to approximate the mapping of function G : A → U, G ≈ G†.
en+1(x) = σ (Wen(x) + (℘(a; ϑ )en(x))(x)) (4a)
Figure 1 shows the full FNO architecture; input observation v(x) is first lifted to a higher dimensional potential
representation e0(x) = M(v(x)) by a fully connected shallow neural network M. Then, e0(x) is used as input for an
iterative Fourier layer e0 → e1 → e2 → · · · → eN. The concrete iterative process from state en → en+1 can be
written as:
en+1(x) = σ (Wen(x) + (℘(a; ϑ )en(x))(x)) (4b)
4

Figure 1. Architecture of the FNO. 𭟋 denotes the Fourier transform, and𭟋−1 denotes the inverse Fourier transform.Rϑ is
a Fourier transform of the periodic function℘; W is a local linear transform; σ is a non-linear activation function;e0 and
e1 are the input and output of Fourier layer 1. Here, σ is a non-linear activation function, W is a linear transformation,
and ℘ is an integral kernel transformation parameterized by a neural network. (℘(a; ϑ )en(x))(x) is the bias, which can
be written as an integral:
(℘(a; ϑ )en (x)) (x) =
Z
℘ϑ (x,y)en (y)dy (4c)
To accelerate the integration process
R
℘ϑ (x,y)en (y)dy, Li et al. (2020) imposed a condition that℘ϑ (x,y) =℘ϑ (x −y)
and the new integral becomes,
(℘(a; ϑ )en (x)) (x) =
Z
℘ϑ (x,y)en (y)dy = 𭟋−1(Rϑ . (𭟋en))(x) (4d)
where 𭟋 denotes the Fourier transform, and 𭟋−1denotes the inverse Fourier transform. Rϑ is a Fourier transform
of periodic function ℘, Rϑ = 𭟋(℘ ϑ), and ℘ ϑis the kernel of the neural network. Following the N Fourier layer
iteration, the last state output eN(x) is projected back to the original space using a fully connected neural network
S, y(x) = S(eN(x) ). In every block of the Fourier layer,FNO approximates highly non-linear functions mainly via
combining the linear transform W and global integral operator Rϑ (Fourier transform). Rϑ can be parameterized as a
complex-valued tensor in the Fourier space from truncating high Fourier frequency modes k, and it can greatly reduce
the number of trainable parameters and improve efficiency during the process of training. We are interested in predicting
the pressure, water & gas saturation given any input of the absolute permeability field (K) and effective porosity (ϕ).
For completeness, the input and output tensors are indicated below. Pini,Sini are the initial pressure and water saturation,
dt is the change in time steps. Three different FNO models are trained simultaneously for the pressure, gas saturation
and water saturation, with the same interacting loss function, this is to accommodate for the difference in magnitude
between these quantities.
X = {K, ϕ,FT M,Pini,Sini} ∈ RB0×1,D×W ×H (4e)
P = f1 (X; θp) , Sw = f2 (X; θs) ,Sg = f3(X; θg) (4f)
K is the absolute permeability, Q is the total flow, Qw is the water flow (injection rate), Qg is the gas flow (injection
rate), dt is the time stepping, Pini is the initial pressure of the reservoir, and Sini is the initial water saturation of the
reservoir.P is the pressure, and Sw is the water saturation and Sg is the gas saturation f1(X; θp) is the FNO model for the
pressure output, f2(X; θs) is the FNO model for the water saturation output, and f3(X; θs) is the FNO model for the gas
saturation output The physics loss ansatz is then,
V (Q, p;T )pressure equation = 1ns  ∥ (− ∇ . [T ∇P] − Q) .act∥22 (5a)
V (p,Sw;t,Tw)water equation = 1ns




ϕ ∂Sw∂t − ∇ . [Tw.FT M. (∇P)] − Qw .act 



22 (5b)
V (p,Sg;t,Tg)gas equation =
1
ns




∇ ·  ρgBg Tg · FTM(∇P) +RsoρgBo To · FTM(∇P) − Qg + ∂∂t ϕ  ρgBg Sg + RsoρgBo So · act



22 (5c)
φc f d = V (Q, p;T )pressure equation + V (p,Sw;t,Tw)water equation + V (p,Sg;t,Tg)gas equation (5d)
Together with the initial conditions and boundary conditions.
Sw (x,0) =S0w (x) ; P (x,0) =P (x) ;Sg (x,0) =S0g (x); Fy= 0 (6a)
φic= 1ns 

Sw (x,0) − S0w (x)

22+ 1ns ∥P (x,0) − P (x)∥22+ 1ns 

Sg (x,0) − S0g (x)

22 (6b)
φbc= 1ns 

Fy

22 (6c)
φφφ = φφφ ccc fff ddd+φφφ iiiccc+φφφ bbbccc +++ φφφ dddaaatttaaa (6d)
θ = [θp, θs, θg]T (6e)
θ j+1=θ j − ε∇φ jθ (6f)
5

Algorithm 1 PINO Reservoir Simulator Surrogate for Dynamic Properties
Require: • X1 = {K, ϕ,FT M,Pini,Sini} ∈RB1×1×D×W ×H ▷ dictionary of varied tenosr inputs
• XN1 = {Qw,Qg,Q,dt,act} ∈RB1×T ×D×W ×H ▷ dictionary of fixed tensor inputs
• Y1pt – labelled pressure, Y1st – labelled water saturation, Y1gt – labelled gas saturation, f1(:, θp), f2(:, θs), f3(:, θg)
• T ▷ Time reporting steps
• epoch, tol, w1, w2, w3, w4, w5, w6 ∈ R
Ensure:
1: j = 0
2: while ( j ≤ epoch) or (φ ≤ tol) do
3: Y1p = f1(X1; θp) · act
4: Y1s = f2(X1; θs) · act
5: Y1g = f3(X1; θg) · act
6: Compute: Tw = K(x)·Krw(Y1s)µw
7: To = K(x)·Kro(1−(Y1s+Y1g))µo
8: Tg = K(x)·Krg·Y1gµg
9: T = XN1[act] · XN1[FT M] · (Tw + To + Tg)
10: Compute: V (Y1p,Y1s;t,Tw)1s = 1ns · 


(ϕ · ∂Y1s∂t − ∇ · [Tw · ∇Y1p] − X1[Qw])


22
11: Compute:
V (Y1p,Y1s,Y1g;t,To,Tg)1g = 1ns · 



∇ ·  ρgBg · Tg · XN1[act] · XN1[FT M] · ∇Y1p
+ Rso · ρg
Bo
· To · XN1[act] · XN1[FT M] · ∇Y0p

− XN0[Qg]
+ ∂∂t ϕ ·  ρgBg ·Y1g + Rso · ρgBo · (1 − (Y1s +Y1g))



22
12: Compute: V (X1[Q],Y1p;T )1p = 1ns · 

(−∇ · [T · act · ∇Y1p] − X1[Q])

22
13: φp =


Y1pt − f1(X1; θp)

22 ▷ data supervised loss for pressure
14: φs = ∥Y1st − f2(X1; θs)∥22 ▷ data supervised loss for water saturation
15: φg =


Y1gt − f3(X1; θg)

22 ▷ data supervised loss for gas saturation
16: φ = w1 · φp + w2 · φs + w3 · φg + w4 ·V (Y1p,Y1s;t,Tw)1s + w5 ·V (X1[Q],Y1p;T )1p + w6 ·V (Y1p,Y1s,Y1g;t,To,Tg)1g ▷ overall
loss
17: Update models:
18: θ = [θp, θs, θg]T
19: θ j+1 = θ j − ε∇φ jθ ▷ Back-propagation
20: j ← j + 1
21: end while
22: Output:: f1(:, θp), f2(:, θs), f3(:, θg) ▷ pressure,water saturation and gas saturation PINO surrogates
w1. . . ,w6 are the weights associated to the loss functions associated to the 6 terms. X1= {K, FTM,ϕ,Pini,Sini} are the
dictionary inputs from running the reservoir simulator. epoch,tol are the number or epochs and the tolerance level for
the loss function. f1 (:,θp) , f2 (:,θs) , f3 (:,θg) are the FNO models for the pressure, water, and gas saturation equation
respectively, act is the inactive /active cells grid, FTM is the fault transmissibility multiplier.
3 Inverse Problem
A probability space is defined as a triplet (Ω, F , P). The sample space Ω is a set containing all possible outcomes.
The σ-algebra F on Ω is a set of all possible events from an experiment, and follows the following axioms: if
A ∈ F , then Ac ∈ F , where Ac is the complement of A. If A1, A2, ... ∈ F is a countable sequence of elements,
then U ∞i=1 = Ai ∈ F [4] The measure P : F → [0,1] defines a probability to every event in F and satisfies:
P (A) ≥ 0, ∀ A ∈ F , P (Ω) =1, If A1, A2, ... ∈ F are pairwise disjoint (meaning Ai ∩ A j = 0, ∀ i , j), then
P (U ∞i=1 = (Ai)) = ∑∞i=1 P(Ai). This property is called countable additivity[4].
If measurable sets Ai for i ∈ N are pairwise disjoint, then P (S∞i=1 Ai) =∑∞i=1 P(Ai). A measure is called σ-finite if Ω is
a countable union of measurable sets with finite measure. In this paper, we restrict the Euclidean space Ω = Rn, with
Borel σ-algebra F = B(Rn), and with Lebesgue measure on Rn. A random variable X is defined as a measurable map
6

X : (Ω, F ) → (Rn, B(Rn)), which means that if A ∈ B(Rn), then X −1(A) ∈ F . The probability distribution of X is
then defined as a measure on (Rn, B(Rn)): µ(A) := P(X −1(A)).
Theorem 1 (Radon- Nikodym Theorem). Let µ and ν be two measures on the same measure space (Ω, F ). If ν is σ-
finite and µ ≪ ν then there exists a function f ∈ L 1 (Ω, F , ν) such that
µ (A) =
Z
A
f (x)dν (x) , .∀ A ∈ F (7a)
And f (x) = dµdν (x) is called the Radon-Nikodym derivative of µ with respect to ν
Suppose µ is a probability measure on (Rn, B(Rn)), Ln is a Lebesgue measure on Rn, and µ ≪ Ln, then there exists
π ∈ L 1(Rn) such that µ(A) =RA π(x)dx for any A ∈ B(Rn), and π(x) is called the probability density function (pdf)
of X. The joint distribution of two random variables X and Y over corresponding measurable sets A and B is given by
µX×Y (A ×B) =P(X −1(A) ∩Y −1(B)), and the marginal distribution ofX is defined as µX (A) =µX×Y (A × Rn), similarly
for Y . Two random variables X and Y are independent if µX×Y (A × B) =µX (A)µY (B).
A random variable Y ∈ L 1(Ω,GGG, P; Rn) is called the conditional expectation of X ∈ L 1(Ω, F , P; Rn) with respect to
the partial σ-algebra GGG if RG X(ω)dP(ω) =RGY (ω)dP(ω) for all G ∈ GGG, then define the expectation E(X|GGG) := Y .
The conditional probability of an event A ∈ F given the sub-σ-algebra GGG is a conditional expectation of the form
E( f (x),GGG) where P(A|GGG) =E(111A(X)|GGG) and 111A(X) :=

1 if x ∈ A
0 if x < A is the indicator function of a subset A of a set X.
The cost functional for the history matching inverse problem is posed as [4, 1, 11, 63, 12, 41].
Φ (u;y) ≡ 12 


Γ −12 (y − G (u))


2 (7b)
Where ∥.∥ represents the M dimensional Euclidean Norm. G : Rd → Rk represents the forward simulator, that solves
the forward problem and defines the relationship between unknown parameters u ∈ Rd , y ∈ Rk is the corrupted noisy
(or noiseless in rare cases) true data given by.
y = F

K+, φ + + η (7c)
where K+, φ + is the underlining unknown true model (we want to recover) and η∼N (0, Γ) . Γ ∈ Rk×k is the data
noise covariance matrix with Lebesgue density ρ(η). The unknown u follows a prior distribution µ0 with Lebesgue
density ρ0(u). This prior density ρ0(u) contains any information that we already know about u; a good prior is key to
the solution of the inverse problem. It then follows that (u,y) ∈ Rd ×Rk is a random variable with Lebesgue density
ρ (y − G (u) )ρ0(u). The posterior distribution u|y is then the solution to the inverse problem and is given by Bayes’
theorem,
P (u | y) = 1P (y) P (y | u) P(u) (7d)
Assume that Z :=
R
Rn ρ(y − G(u))ρ0(u)du > 0, then u|y is a random variable with Lebesgue density π(u) =1Z ρ(y −G(u))ρ0(u), where Z is the probability of y and acts as a normalizing constant; for random variables A and B,
let P(A|B) be the conditional pdf of A given B and P(A) be the pdf of A, then P(u,y) =P(u|y)P(y) =P(y|u)P(u),
and P(y) =
R
Rd P(u,y)du and P(u) =
R
Rk P(u,y)dy, assuming that P(y) > 0 then Bayes’ theorem gives us P(u|y) =
1
P(y) P(y|u)P(u) =1Z ρ(y −G(u))ρ0(u) > 0; if we define the negative log likelihood asΦ(u;y) =−log ρ(y −G(u)), then
dµy
dµ0 (u) =1Z exp(−Φ(u;y)), where Z = RRk exp(−Φ(u;y))µ0(du), and µy and µ0 are measures on Rk with densitiesπ and ρ0 respectively, which shows the posterior is absolutely continuous with respect to the prior density and the
Radon-Nikodym derivative dµydµ0 (u) is proportional to the likelihood. Using the Sherman -Morrison-Woodbury Lemma
[26], we arrive at the VanillaEnsemble Kalman Inversion (EKI),
u( j)n+1 = u( j)n +CuGn CGGn + αnΓ−1(y + √αξn − G(u( j)n )) (8a)
n is the iteration index, j is the ensemble member (columns in the matrix) in the ensemble size J. αn is a (crucial)
regularisation dampener, CuGn and CGGn are cross-covariance matrixes to be explained shortly, ξ ∼N(0,1).
CGGn = 1j − 1 J∑j=1 G u( j)n  − G u( j)n  ⊗ G u( j)n  − G u( j)n  (8b)
7

CuGn = 1j − 1 J∑j=1 u( j)n  − u( j)n  ⊗ G u( j)n  − G u( j)n  (8c)
In the developed aREKI method, the dampening parameter α is developed via the discrepancy principle [5, 4] in
Algorithm 2. Covariance localization means localising the effect of an observation to the state variables that are ‘closer’
Algorithm 2 aREKI
Require: •
n
u( j)0 oJj=1 ▷ prior density
• y ▷ measurements
• Γ ▷ measurement errors covariance
• iter ▷ iteration
1: Initialize: sn = 0, n = 0
2: while (sn < 1) or (n ≤ iter) do
3: Compute: G

u( j)n  , j ∈ {1, . . . ,J}
4: Compute: Φn ≡

1
2



Γ −12 (y − G (u))


2
2
J
j=1
5: Compute: Φn, σ 2Φn ▷ mean & variance
6: Compute: αn = 1
min
(
max
(
L(y)
2Φn ,
s
L(y)
2σ2Φn
)
,1−sn
)
7: Compute: sn = sn + 1αn
8: Compute: CGGn = 1j−1 ∑Jj=1

G

u( j)n  − G u( j)n  ⊗ G u( j)n  − G u( j)n 
9: Compute: CuGn = 1j−1 ∑Jj=1

u( j)n  − u( j)n  ⊗ G u( j)n  − G u( j)n 
10: Update ensemble: u( j)n+1 = u( j)n +CuGn CGGn + αnΓ−1 y + √αnξn − G u( j)n 
11: Increment: n ← n + 1
12: end while
13: Output:: u( j) ▷ posterior density
to the observations. It is a technique used in history matching to eliminate filter divergence and spurious correlations
which are found in both standard ensemble-based methods [21, 63, 1, 15, 16]. It selectively assimilates data during
the update step by adjusting the correlation between the data measured at a location A and the model parameters or
data measured at a further location B to be zero, therefore eliminating long-distance non-zero spurious correlations
and increasing the degrees of freedom available for data assimilation. It is usually applied with a Schur product. The
various localization methods proposed in the literature have the common goal of removing the spurious terms in the
cross-covariance matrix; this matrix is in turn used to update the state vectors during the ensemble update process. This
is done by conditioning the Kalman Gain through a localizing function [21, 63, 1, 15, 16]. Each localization scheme
distinguishes itself from each other by how this localizing function, also known as the Schur product or the multiplier
function, is computed. The motivation of covariance localization is to achieve a similar level aREKI performance
if a larger ensemble size would have been used. However, it requires enormous computational resources to perform
history matching if the ensemble size is large. ρ is the localization function or multiplier function, this is a specified
parameter for covariance localization. It is introduced to modify the Kalman Gain during update step for aREKI. The
symbol ‘◦’ is an element-by-element multiplication operator known as the Schur product. To implement the Schur
product in covariance localization, a correlation function with local support, ρ is defined. The term local support refers
to the function taking on non-zero values in a small region and being zero elsewhere. The function ρ is usually defined
to be the compactly supported fifth order piecewise rational function defined by Gaspari and Cohn as shown below
[21, 63, 1, 15, 16].
ρ=



− 14

|z|
c
5
+ 12

|z|
c
4
+ 58

|z|
c
3
− 53

|z|
c
2
+1, 0≤ |z| ≤c,
1
12

|z|
c
5
− 12

|z|
c
4
+ 58

|z|
c
3
+ 53

|z|
c
2
−5

|z|
c

+4− 23

|z|
c

, c≤ |z| ≤2c,
0, 2c≤ |z| .
(9a)
u( j)n+1 = u( j)n + ρ · o ·CuGn CGGn + αnΓ−1 y + √αnξn − G u( j)n  , j ∈ {1, . . . ,J} (9b)
8

4 Mixture of experts.
In general, the problem of designing machine learning-based models in a supervised context is the following. Assume a
set of labeled dataDDD = {(xi,yi)}Ni=1, where xi ∈ Rd are the inputs and the outputsyi ∈ R for regression oryi ∈ {0,1, . . . ,J}
for classification. Postulating amongst a family of ansatz f (·; θ ), parametrized by θ ∈ RP, we can find a θ ∗ such
that for all i = 1, . . . ,N, yi = f (xi; θ ∗). Then for all x′ in the set {xi}Ni=1, y′ ≈ f (x′; θ ∗), where y′ is the true label of x′.[10, 45, 12] . Assume (xi,yi) ∈ χ × γ are the input and output pairs of a model shown in Eqn. 10a.
yi ≈ f (xi) (10a)
f : χ → γ is irregular and has sharp features, very non-linear and has noticeable discontinuities, The output space is
taken as γ=R and χ = Rd
4.0.1 Cluster
In this stage, we seek to cluster the training input and output pairs. λ : χ × γ → L B {1, . . . ,L} where the label
function minimizes,
Φclust (λ ) =
L
∑
l=1
∑
iεSl
ℓ (xi,yi) (10b)
Sl = {(xi,yi); λ (xi,yi) =l} (10c)
ℓl loss function associated to cluster l
zi = (xi,yi) , ℓl = |zi − µl|2 (10d)
µl = 1|Sl | ∑iεSl zi where |.| denotes the Euclidean norm
4.0.2 Classify
li = λ (xi,yi) is an expanded training set
{(xi,yi,li)}Ni=1 (11a)
fc : χ → L (11b)
x ∈ χ provides an estimate fc : x 7− →f (x) ∈ L such that fc (xi) =li for most of the data. Crucial for the ultimate
fidelity of the prediction. {yi} is ignored at this phase. The classification function minimizes,
Φclust ( fc) =
N
∑
i=1
φc (li, fc (xi)) (11c)
φc : L × L → R+ is small if fc (xi) =li for example we can choose fc (x) =argmaxl∈L gl (x) where gl (x) >
0, ∑Ll=1 gl (x) is a soft classifier and φc (li, fc (xi)) =−log (gl (x)) is a cross-entropic loss.
4.0.3 Regress
fr : χ × L → γ (11d)
For each (x,l) ∈ χ × L must provide an estimate fr : (x,l) 7− →fr (x,l) ∈ γ such that fr (x, fc (x)) ≈ y for both
the training and test data. If successful a good reconstruction for
f : χ → γ (11e)
Where f (.) =fr (., fc (.)) the regression function can be found by minimizing
Φr ( fr) =
N
∑
i=1
φr (yi, f r (xi, fc (xi))) (11f)
Where φr : γ × γ → R+ minimized when fr (xi, fc (xi)) =yi in this case can be chosen as φr (y, f r (x, fc (x))) =
|y − f r (x, fc (x))|2. Data can be partitioned into Cl = {i; fc (xi) =l} for l = 1, . . .L and then perform L separate
regressions done in parallel.
Φlr( fr (.,l) =∑
i∈Cl
φr (yi, f r (xi, l)) (11g)
9

4.0.4 Bayesian Formulation
A critique of this method is that it re-uses the data in each phase. A Bayesian postulation handles this limitation
elegantly. Recall,
DDD = {(xi,yi)}Ni=1 (12a)
Assume parametric models for the classifier gl (.; θc) =gl

.; θ lc and the regressor. fr .,l; θ lr  for l = 1, . . .L where
θc =

θ 1c , . . . ,θ Lc  and θr = θ 1r , . . . ,θ Lr  and let θ = (θc, θr), the posterior density has the form,
π (θ ,l | D) ∝
N
∏
i=1
π (yi | xi, θr,l)π (l | xi, θc) π (θr) π (θc) (12b)
π (yi | xi, θr,l) ∝ exp

−12 yi − fr xi,l; θ lr 2 (12c)
And
π (l | xi, θc) =gl (xi; θc) (12d)
gl (xi; θc) = exp

hl

x; θ lc
∑Ll=1 exp(hl (x; θ lc)) (12e)
hl

x; θ lc are some standard parametric regressors.
4.1 Sparse Gaussian process experts
Mixtures of GP experts have proven to be very successful [20, 47, 57, 10, 13]. In particular, they overcome limitations of
stationary Gaussian process models by reducing the computational complexity through local approximations and allow
different local properties of the unknown function to handle challenges, such as discontinuities, non-stationarity and
non-normality. In this case, one assumes a GP prior on the local regression function with hyperparametersθ lr = (µl, ψl):
fr(·; θ lr ) ∼ GP(µl,Kψl ),
where µl is the local mean function of the expert (for simplicity, it assumed to be constant) and ψl are the parameters
of the covariance function Kψl , whose chosen form and hyperparameters encapsulate properties of the local function
such as the spatial correlation, smoothness, and periodicity. While GP experts are appealing due to their flexibility,
intrepretability and probabilistic nature, they increase the computational cost of the model significantly. Indeed, given
the allocation variables z, the GP hyperparameters, which crucially determine the behavior of the unknown function,
can be estimated by optimizing the log marginal likelihood:
log(p(y|x, z)) =
L
∑
l=1
log

N(yl | µµµl, KlNl + σ 2lr INl ) , (12f)
where yl and xl contain the outputs and inputs of the lth cluster, i.e. yl = {yi}zi=l and xl = {xi}zi=l; µµµl is a vector with
entries µl; KlNl represents the Nl × Nl matrix obtained by evaluating the covariance function Kψl at each pair of inputs
in the lth cluster; and Nl is number data points in the lth cluster. This however requires inversion ofNl × Nl matrices,
which scales O(∑Ll=1 N3l ). While this reduces the computational complexity compared with standard GP models which
scale O(N3), it can still be costly[10].
To improve scalability, one can resort to approximate methods for GPs, including sparse GPs based on a set of inducing
points or pseudo inputs [20, 47, 57, 10], basis function approximations [57], or sparse formulations of the precision
matrix [47, 57], among others for a recent review of approaches in spatial statistics and [ 47, 57] for a review of
approaches in machine learning).
In the present work, we employ an inducing point strategy, assuming the local likelihood of the data points within each
cluster factorizes given a set of Ml < Nl pseudo-inputs ˜xl = (˜xl1, . . . ,˜xlMl ) and pseudo-targets ˜fl = (˜f l1, . . . ,˜f lMl );
p(yl|xl, ˜xl,˜fl) =∏
i:zi=l
N(yi|bµli , bσ 2li ), (12g)
where
bµli = µl + (klMl ,i)T (KlMl )−1(˜fl − µµµl),
bσ 2li = σ 2lr + Kψl (xi,xi) − (klMl ,i)T (KlMl )−1klMl ,i,
10

where KlMl is the Ml ×Ml matrix with elements Kψl ( ˜xlj, ˜xlh) and klMl ,i is the vector of length Ml with elements Kψl ( ˜xlj,xi).This corresponds to the fully independent training conditional (FITC) approximation [35]. After marginalization of the
pseudo-targets under the GP prior ˜fl ∼ N(µµµl, KlMl ), the pseudo-inputs ˜xl and hyperparameters (µl, ψl) can be estimatedby optimizing the marginal likelihood:
log(p(y|x, z, ˜x)) =
L
∑
l=1
log

N (yl | µµµl, (KlMlNl )T (KlMl )−1KlMlNl + ΛΛΛl + σ 2lr INl ) , (12h)
where KlMlNl is the Ml × Nl matrix with columns klMl ,i and ΛΛΛl is the diagonal matrix with diagonal entries Kψl (xi,xi) −
(klMl ,i)T (KlMl )−1klMl ,i. This strategy allows us to reduce the complexity to O(∑Ll=1 NlM2l ).
5 Generative priors and Tree based learning
5.1 Variational Convolutional Autoencoder (VCAE)
A Variational Convolutional Autoencoder (VCAE) is an extension of the Variational Autoencoder (V AE) with convolu-
tional layers to handle image data more effectively[18].
5.1.1 Encoder
The encoder is a convolutional neural network that maps the input data x ∈ Rd to the parameters of a variational
distribution over the latent variables z ∈ Rk. The encoder outputs the mean and log variance of a Gaussian distribution:
qφ (z|x) =N (z; µφ (x), σ 2φ (x)I) (13a)
µφ (x) =ConvNetµ (x) (13b)
log σ 2φ (x) =ConvNetlog σ 2(x) (13c)
where φ denotes the parameters of the encoder network.
5.1.2 Decoder
The decoder is a deconvolutional neural network that maps the latent variables z back to the data space, producing the
parameters of a generative distribution over x:
pθ (x|z) =N (x; µθ (z), σ 2θ (z)I) (13d)
where θ denotes the parameters of the decoder network, and µθ (z) and log σ 2θ (z) are outputs of the deconvolutionalnetwork.
5.1.3 Evidence Lower Bound (ELBO)
The VCAE maximizes the evidence lower bound (ELBO) to approximate the true posterior distribution p(z|x):
L (θ , φ;x) =Eqφ (z|x)[log pθ (x|z)] − DKL(qφ (z|x)∥p(z)) (14a)
= Eqφ (z|x)[log N (x; µθ (z), σ 2θ (z)I)] − DKL(N (z; µφ (x), σ 2φ (x)I)∥N (0, I)) (14b)
The first term is the reconstruction loss, and the second term is the Kullback-Leibler (KL) divergence between the
approximate posterior qφ (z|x) and the prior p(z).
11

Algorithm 3 CCR
1: Input: Set of labeled data DDD = {(xi,yi)}Ni=1 where xi ∈ Rd and yi ∈ R2: Output: Refined model estimation f (x; θccr) =fr(x, fc(x))
3:
4: function CLUSTER (DDD)
5: Initialize λ : Rd × R → {1, . . . ,L}
6: for each (xi,yi) ∈ DDD do
7: Assign (xi,yi) to a cluster l = λ (xi,yi)
8: Calculate Sl = {(xi,yi) : λ (xi,yi) =l}
9: Calculate cluster center µl = 1|Sl | ∑i∈Sl (xi,yi)
10: end for
11: Minimize Φclust (λ ) =∑Ll=1 ∑i∈Sl |zi − µl|2
12: end function
13:
14: function CLASSIFY (DDD, λ)
15: for each (xi,yi) ∈ DDD do
16: Classify li = λ (xi,yi)
17: Define fc(xi) ← argmaxl∈L gl(xi)
18: end for
19: Minimize Φclust ( fc) =∑Ni=1 −log(gli (xi))20: end function
21:
22: function REGRESS (DDD, fc)
23: for each (xi,yi,li) do
24: Estimate fr(xi,li) ≈ yi using the regression model
25: Minimize Φr( fr) =∑Ni=1(yi − fr(xi, fc(xi)))2
26: end for
27: end function
Algorithm 4 Variational Convolutional Autoencoder (VCAE)
1: Initialize encoder parameters φ and decoder parameters ψ
2: Input image x
3: Encode x to get latent variables: z, µ, σ = Encoderφ (x)
4: Sample latent space: z ∼ N (µ, σ 2)
5: Decode z to reconstruct the image: ˆx = Decoderψ (z)
6: Compute loss: L = Reconstruction Loss( ˆx,x) +KL Divergence(µ, σ )
7: Update parameters φ and ψ to minimize L
8: Output: Return the reconstructed image ˆx
5.2 Denoising Diffusion Implicit Models (DDIM)
Denoising Diffusion Implicit Models (DDIMs) are a type of generative model that produce samples by reversing a
forward diffusion process.[25]
5.2.1 Forward Diffusion Process
The forward diffusion process incrementally adds Gaussian noise to the data x0 through a sequence of latent variables
xt:
q(xt |xt−1) =N (xt; √αtxt−1, (1 − αt )I) (15a)
where αt are the variance preserving coefficients that determine the noise level at each diffusion step.
5.2.2 Reverse Diffusion Process
In DDIMs, the reverse diffusion process aims to reconstruct the original data by gradually denoising the sequence of
noisy samples:
p(xt−1|xt ) =N (xt−1; µθ (xt ,t), σ 2θ (xt ,t)I) (15b)
where µθ (xt ,t) and σ 2θ (xt ,t) are parametrized by a neural network, typically conditioned on t to capture the step-dependent dynamics.
12
