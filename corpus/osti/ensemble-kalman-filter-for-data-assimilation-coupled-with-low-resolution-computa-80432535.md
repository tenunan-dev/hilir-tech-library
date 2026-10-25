---
source_id: "osti"
title: "Ensemble Kalman filter for data assimilation coupled with low-resolution computations techniques applied in fluid dynamics"
summary: "OSTI paper on an ensemble Kalman filter for data assimilation with low-resolution fluid dynamics computations."
url: "https://www.osti.gov/biblio/3633837"
published: "2026-12-15T00:00:00Z"
retrieved_at: "2026-10-23T14:18:07+00:00"
licence: "mixed-per-document"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["UPS", "REF", "H2", "CCS", "PWR"]
disciplines: ["PRC", "MAT", "DIG"]
sha256: "80432535873c3e48ef1b98b95ba197291540c2d4689a0a594522e5978736c3a0"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
content: "metadata-and-abstract"
rights_note: "Check the record's rights before storing full text."
---

# Ensemble Kalman filter for data assimilation coupled with low-resolution computations techniques applied in fluid dynamics

**Authors:** Jeanney, Paul [Polytechnic University of Madrid (Spain)] (ORCID:000900090334219X); Hetherington, Ashton [Polytechnic University of Madrid (Spain)] (ORCID:0009000498503067); Ahmed, Shady E. [Pacific Northwest National Laboratory (PNNL), Richland, WA (United States)] (ORCID:0000000155480265); Lanceta, David [Arup, Madrid (Spain)]; Saiz, Susana [Arup, Madrid (Spain)] (ORCID:0000000256976737); Perez, José Miguel [Polytechnic University of Madrid (Spain)] (ORCID:0000000213352676); Le Clainche, Soledad [Polytechnic University of Madrid (Spain)] (ORCID:0000000336057351)

**Abstract:** This paper presents an innovative Reduced-Order Model (ROM) for merging experimental and simulation data using Data Assimilation (DA) to estimate the ”True” state of a fluid dynamics system, leading to more accurate predictions. Our methodology introduces a novel approach by implementing the Ensemble Kalman Filter (EnKF) within a reduced-dimensional framework, grounded in a robust theoretical foundation and applied to fluid dynamics. To address the substantial computational demands of DA, the proposed ROM employs low-resolution (LR) techniques to drastically reduce computational costs. This innovative approach involves downsampling datasets for DA computations, followed by an advanced reconstruction technique based on low-cost Singular Value Decomposition (lcSVD). The lcSVD method, a key innovation in this paper, has never been applied to DA before and offers a highly efficient way to enhance resolution with minimal computational resources. Our results demonstrate significant reductions in both computation time and RAM usage through these LR techniques without compromising the accuracy of the estimations. For instance, in a turbulent test case, for a data compression rate (𝐶<sub>𝑅,𝑢<sub>𝑏</sub></sub>) of 15.9, the LR approach can achieve a speed-up of 13.7 and a RAM compression of 90.9% while maintaining a low Relative Root Mean Square Error (<em>RRMSE</em>) of 2.6%, compared to 0.8% in the high-resolution (HR) reference. Furthermore, we highlight the effectiveness of the EnKF in estimating and predicting the state of fluid flow systems based on limited observations and given low-fidelity numerical data. This paper highlights the potential of the proposed DA method in fluid dynamics applications, particularly for improving computational efficiency in CFD and related fields. Its ability to balance accuracy with low computational and memory costs makes it especially suitable for large-scale and real-time applications, such as environmental monitoring or engineering design. This method will be incorporated into ModelFLOWs-app.
