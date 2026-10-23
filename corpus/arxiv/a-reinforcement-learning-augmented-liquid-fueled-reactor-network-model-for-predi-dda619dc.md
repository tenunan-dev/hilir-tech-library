---
source_id: "arxiv"
title: "A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors"
url: "http://arxiv.org/abs/2607.19281v1"
published: "2026-07-21T16:53:08Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "dda619dc3875efc0492ecdd38608f0aecd67d7534ad73f40f8ad02460c5e57e8"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
content: "metadata-and-abstract"
---

# A Reinforcement-Learning-Augmented Liquid-Fueled Reactor Network Model for Predicting Lean Blowout in Gas Turbine Combustors

**Authors:** Philip John, Eloghosa Ikponmwoba, Pinaki Pal, Opeoluwa Owoyele

**Abstract:** This study introduces a reinforcement learning (RL) framework for generating optimal liquid-fueled reactors to improve lean blowout (LBO) predictions in gas turbine combustors. Existing approaches for determining cluster boundaries rely on manual heuristics or distance-based metrics in the input space. In contrast, the proposed method is goal-oriented, explicitly accounting for the target metric (e.g., LBO prediction accuracy) during cluster formation. The framework employs a multi-stage clustering--classification strategy: an initial clustering step (e.g., $k$-means clustering) generates a large set of homogeneous micro-clusters, followed by an actor-critic RL agent that merges them into optimal reactor zones. The validation study, performed using a Jet-A mechanism (119 species, 841 reactions), shows the RL framework offers improved predictive fidelity compared to $k$-means and captures the correct LBO trends, while achieving substantial speedups relative to the high-fidelity computational model. Overall, the RL-driven approach demonstrates strong potential as a computationally efficient reduced-order modeling technique that can complement high-fidelity simulations for rapid design-space exploration.
