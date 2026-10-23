---
source_id: "osti"
title: "Nodal capacity expansion planning with flexible large-scale load siting"
url: "https://www.osti.gov/biblio/3375389"
published: "2027-02-01T00:00:00Z"
retrieved_at: "2026-10-23T14:18:07+00:00"
licence: "mixed-per-document"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["UPS", "REF", "H2", "CCS", "PWR"]
disciplines: ["PRC", "MAT", "DIG"]
sha256: "e7ed88b10868ae55fb63891b7cfeb546ade69988e3e3dc99c3d5b7107ff0cb31"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
content: "metadata-and-abstract"
rights_note: "Check the record's rights before storing full text."
---

# Nodal capacity expansion planning with flexible large-scale load siting

**Authors:** Valencia Zuluaga, Tomas [Lawrence Livermore National Laboratory (LLNL), Livermore, CA (United States)] (ORCID:0000000174749768); Pang, Simon [Lawrence Livermore National Laboratory (LLNL), Livermore, CA (United States)] (ORCID:0000000329131648); Watson, Jean-Paul [Lawrence Livermore National Laboratory (LLNL), Livermore, CA (United States)] (ORCID:0000000160268875)

**Abstract:** We propose explicitly incorporating large-scale load siting into a stochastic nodal power system capacity expansion planning model that concurrently co-optimizes generation, transmission, and storage expansion. The potential operational flexibility of some of these large loads is also taken into account by considering them as consisting of a set of tranches with different reliability requirements, which are modeled as a constraint on expected served energy across operational scenarios. We implement our model as a two-stage stochastic mixed-integer optimization problem with cross-scenario expectation constraints. To overcome the challenge of scalability, we build upon existing work to implement this model on a high performance computing platform and exploit scenario parallelization using an augmented Progressive Hedging Algorithm. The algorithm is implemented using the bounding features of mpisppy, which have shown to provide satisfactory provable optimality gaps despite the absence of theoretical guarantees of convergence. We test our approach and assess the value of this proactive planning framework on total system cost and reliability metrics using realistic testcases geographically assigned to San Diego and South Carolina, with datacenter and direct air capture facilities as large loads.
