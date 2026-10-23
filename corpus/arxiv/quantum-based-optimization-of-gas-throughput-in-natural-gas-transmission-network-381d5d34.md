---
source_id: "arxiv"
title: "Quantum-Based Optimization of Gas Throughput in Natural Gas Transmission Networks Under Hydraulic Constraints Using QAOA"
url: "http://arxiv.org/abs/2609.00825v1"
published: "2026-09-01T07:26:34Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "381d5d34a287bd6f05b912d8e72645d9556a9e2c06313e531d0f51408b562a41"
content: "metadata-and-abstract"
---

# Quantum-Based Optimization of Gas Throughput in Natural Gas Transmission Networks Under Hydraulic Constraints Using QAOA

**Authors:** Alex Ben Ishay, Yuval Eyal, Yuval Cohen, Nati Erez

**Abstract:** Maximizing gas throughput in transmission networks under hydraulic and operational constraints is a combinatorial problem whose complexity grows exponentially with network size, making it computationally intensive to solve exactly. This paper addresses the graph-based optimization problem by optimizing nodal-pressure assignments under the Panhandle-B hydraulic equation. By framing the problem as a search over discretized nodal-pressure assignments coupled with a cost Hamiltonian that encodes both the delivery objective and physical-constraint penalties, we establish a unified formulation suitable for the Quantum Approximate Optimization Algorithm (QAOA). The mathematical model is adapted to a Quadratic Unconstrained Binary Optimization (QUBO) formulation and implemented using the Classiq quantum software platform. In simulator-based experiments, QAOA recovered the maximum-throughput valid operating point, consistent with classical exhaustive evaluation and classical hydraulic simulation reference solutions. A distinctive contribution of this work is the end-to-end execution of a reduced problem instance on the IonQ Forte-1 trapped-ion quantum processor. Remarkably, the hardware implementation used only $p=2$ QAOA layers, substantially fewer than the $p=30$ layers used in the simulator-based study. Despite this significant reduction in circuit depth, the QPU produced physically valid and interpretable candidate solutions that bracketed the continuous classical optimum, with each located within one pressure-discretization step of it. These results demonstrate that meaningful gas-network optimization behavior can be obtained using considerably shallower QAOA circuits than initially expected and provide an end-to-end proof of concept for near-term quantum-assisted gas-network optimization.
