---
source_id: "arxiv"
title: "Towards Natural Gas Contract Selection via Quantum-Guided Independent Set Reduction"
url: "http://arxiv.org/abs/2609.00881v1"
published: "2026-09-01T08:14:34Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "6d45768792d59093d78e1874451912ff6bfb9c19cc1d14ad7d32df46e176eafc"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
content: "metadata-and-abstract"
---

# Towards Natural Gas Contract Selection via Quantum-Guided Independent Set Reduction

**Authors:** Vivek Dixit, Vaibhaw Kumar, Kentaro Ohno, Alberto Maldonado Romo, Larry Bowden

**Abstract:** Selecting mutually compatible natural gas transportation contracts is a practically important optimization task in which operators must choose from many candidate agreements subject to temporal, infrastructural, and flow-related constraints. As the number of candidates grows, the resulting search space becomes difficult to explore exhaustively. We study a pairwise abstraction of this task, formulated as a Maximum Clique problem on a contract-compatibility graph, or equivalently as a Maximum Independent Set (MIS) problem on the complement graph. Building on recent work, this paper studies a quantum-classical framework for solving large-scale MIS instances within the limitations of noisy quantum hardware. The approach combines iterative classical graph reduction with quantum-guided optimization to progressively simplify the search space while maintaining high solution quality. This enables large candidate spaces to be reduced to smaller subproblems that are more suitable for execution on current quantum computers. We evaluate the approach on fifteen benchmark instances from the Quantum Optimization Benchmarking Library (QOBLIB), obtaining an average approximation ratio of 0.996 and recovering optimal solutions for fourteen instances, including graphs with up to 186 vertices. We further evaluate the algorithm on six synthetic pairwise contract-compatibility graphs containing up to 900 contracts, where the proposed method achieves an average approximation ratio of 0.989 and obtains optimal solutions in four cases. These experiments demonstrate the ability of the hybrid MIS solver to reduce industrially motivated graphs. The pairwise abstraction serves as the first step of a two-stage screening procedure that narrows the candidate contracts to a smaller set of mutually compatible ones, which can then be verified against pipeline-capacity constraints.
