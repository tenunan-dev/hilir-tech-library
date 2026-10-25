---
source_id: "arxiv"
title: "GSO-Net: Visual State Machines for Hazardous Freight Transfer Compliance at Petrochemical Logistics Nodes"
summary: "Benchmark and model (GSO-Net) for judging whether hazardous freight transfers at petrochemical logistics sites follow standard procedures, from camera images with sparse polling."
url: "http://arxiv.org/abs/2609.12408v1"
published: "2026-09-11T04:00:41Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "7f1c387a4764dde8864248676e8ffaf9e00f8b2d1fd8162c5b2b6d53c5369872"
content: "metadata-and-abstract"
---

# GSO-Net: Visual State Machines for Hazardous Freight Transfer Compliance at Petrochemical Logistics Nodes

**Authors:** Yu Xie, Bangshu Xiong, Zhibo Rao, Rui Gan, Chongxuan Liu, Zechu Ouyang

**Abstract:** Hazardous-freight operations at petrochemical logistics nodes are safety-critical for intelligent transportation systems, yet existing vision benchmarks rarely address procedural compliance under realistic deployment constraints. In large infrastructure networks, cameras often operate under sparse round-robin polling, so transfer status must be inferred from incomplete observations and localized evidence. We present GSO-Net, a large-scale benchmark for visual understanding of standard operating procedures (SOPs) in petrochemical unloading scenarios. To our knowledge, GSO-Net is the first public benchmark dataset dedicated to visual SOP understanding in petrochemical hazardous-freight transfer scenarios. It contains over 50,000 independently sampled frames from 64 real expressway petrochemical logistics nodes and adopts an SOP-derived hierarchy linking 9 macroscopic procedural steps with 15 microscopic operational states. Two tasks are defined: joint detection of microscopic states and macroscopic steps as the core benchmark, and frame-level step classification as a diagnostic reference. Experiments with lightweight, transformer-based, open-vocabulary, and holistic models reveal a clear gap between object perception and transfer-stage understanding. Current models remain weak on contact-level state grounding, transient step recognition, and stage consistency, especially under sparse polling, tiny critical targets, and long-tailed operational evidence. GSO-Net provides a practical benchmark for fine-grained state perception and vision-based safety monitoring in hazardous freight transportation. The dataset is publicly available at https://github.com/yuxieHarrison/GSO-Net
