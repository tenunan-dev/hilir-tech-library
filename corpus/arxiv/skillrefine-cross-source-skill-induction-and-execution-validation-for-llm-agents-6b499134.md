---
source_id: "arxiv"
title: "SkillRefine: Cross-Source Skill Induction and Execution Validation for LLM Agents in Refinery Planning Software"
summary: "Research paper on an LLM agent method that combines documentation, expert records and run-time feedback to operate refinery planning software such as AspenTech PIMS."
url: "http://arxiv.org/abs/2609.30674v1"
published: "2026-09-25T01:29:20Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "6b49913424b7fb2f77c5f36a8008742546c8c9f86753ad151d805f93c11817c8"
content: "metadata-and-abstract"
---

# SkillRefine: Cross-Source Skill Induction and Execution Validation for LLM Agents in Refinery Planning Software

**Authors:** Dongxiao Liu, Boren Zhu, Yuwen Ding, Linghui Li, Lei Li, Xiaoyong Li

**Abstract:** Operating industrial planning software such as AspenTech PIMS (Process Industry Modeling System) requires an LLM agent to combine structural knowledge, procedural knowledge from expert records, and constraints revealed only during execution. These evidence sources are heterogeneous and individually incomplete: documentation describes tables and interfaces but omits task-level coordination, expert CASE records expose multi-table modification patterns without explicit schema grounding, and execution feedback reveals latent constraints only when a plan is executed. We present \textsc{SkillRefine}, a framework that exploits the Documentation--Practice Gap between documented structure and expert practice to extract candidate coordination patterns, ground them against table definitions and COM specifications, and compile them into progressively disclosed skill packages with provenance. The library is then refined through label-free compliance screening, oracle-based match decomposition over table, row, column, and value dimensions, and signal-conditioned trajectory attribution for localized repair. We evaluate \textsc{SkillRefine} on PIMS-Bench, a benchmark built from two AspenTech PIMS demonstration models, using disjoint construction and held-out test tasks. On the held-out test set, \textsc{SkillRefine} achieves absolute component match F1 gains of 14\%--30\% across four LLM backbones, with the largest gains on complex multi-table coordination tasks.
