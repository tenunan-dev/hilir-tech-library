---
source_id: "arxiv"
title: "Physics-Constrained Soft Actor-Critic for Simulator-in-the-Loop Petroleum Reservoir History Matching"
summary: "Machine-learning paper that wraps a commercial reservoir simulator and uses soft actor-critic reinforcement learning to match production history without gradients."
url: "http://arxiv.org/abs/2608.01986v1"
published: "2026-08-03T09:46:38Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "28c56e5861e9dde80ed586f156bdb1578039d7244caab06460b664980063f246"
content: "metadata-and-abstract"
---

# Physics-Constrained Soft Actor-Critic for Simulator-in-the-Loop Petroleum Reservoir History Matching

**Authors:** Nam-Phong Huu Nguyen, Duy-Dong Nguyen, Tho Quan

**Abstract:** Many scientific calibration problems expose only an expensive executable simulator, making gradients unavailable and large-scale training-data generation impractical. We study petroleum reservoir history matching as an instance of this broader AI problem and formulate it as physics-constrained, simulator-in-the-loop policy search. Our method wraps the CMG IMEX full-physics simulator as a Gymnasium environment and uses Soft Actor-Critic (SAC) to learn a stochastic proposal distribution over continuous porosity, directional-permeability, and well-skin parameters. Each interaction generates and executes a reservoir case, aligns simulated and observed production responses, and returns a reward that combines multi-response mismatch with penalties for physically invalid properties. Off-policy replay reuses costly simulator feedback, while maximum-entropy learning preserves exploration. Unlike forward-surrogate approaches, the policy learns where to evaluate rather than learning to replace the simulator; every retained candidate is validated by IMEX. Under a 200-call budget on PUNQ-S3, the best valid candidate achieves category-macro NMSE $0.0285$, $R^2=0.9324$, and a bounded match score of $97.23\%$. Well-level analysis further exposes localized water-rate failures hidden by pooled metrics. These results establish a full-physics proof of concept for reinforcement-learning-based calibration of expensive scientific simulators.
