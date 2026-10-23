---
source_id: "arxiv"
title: "Repairing PBE-Spurious Metallicity for HSE06-Level Screening of 2D Photocatalysts for Green Hydrogen Production"
url: "http://arxiv.org/abs/2609.02883v1"
published: "2026-09-02T17:57:21Z"
retrieved_at: "2026-10-23T14:24:39+00:00"
licence: "CC0-1.0"
reuse_level: "full-text-restricted"
permitted_use: "unstated"
sectors: ["PWR", "H2", "CCS", "UPS"]
disciplines: ["DIG", "PRC"]
sha256: "72d52aceead34ebc051ba659cbaaded0b54728235e16a7400a5a15fcc65e2abc"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
content: "metadata-and-abstract"
---

# Repairing PBE-Spurious Metallicity for HSE06-Level Screening of 2D Photocatalysts for Green Hydrogen Production

**Authors:** Ritam Chakraborty, Arpan Das

**Abstract:** Semilocal PBE calculations can remove viable photocatalysts before screening by labeling narrow-gap semiconductors as metals. We address this failure mode in the Computational 2D Materials Database (C2DB) by combining leakage-aware repair of PBE-spurious metallicity with HSE06--PBE $Δ$-learning. Stage~I classifies HSE06-unknown PBE metals using structural, chemical, magnetic, and stability descriptors, while excluding HSE06/GW quantities and PBE electronic shortcuts. Stage~II learns $E_g^{HSE} - E_g^{PBE}$ for the corrected insulating population. The curated XGBoost regressor reconstructs HSE06 gaps with a mean absolute error of 0.108~eV ($R^2=0.989$), compared with 1.036~eV for raw PBE. The Stage~I classifier is used only for triage because the labeled true-metal class contains 29 materials; its best holdout performance gives 87.5\% accuracy, 0.286 true-metal recall, and 0.643 balanced accuracy. The corrected pH~0 electronic screen yields 10 strict and 29 initial relaxed green-hydrogen photocatalyst candidates. Four strict and 18 relaxed candidates would fail the same 1.6--2.8~eV gap window at the PBE level. Targeted VASP HSE06 calculations for six ML-predicted compounds give material-level MAEs of 0.417, 0.182, and 0.110~eV for the C2DB-native, Magpie+structural, and curated models, respectively; \feat{1AgBr-1} shifts above the upper gap cutoff, leaving 28 retained relaxed candidates. The workflow shows that high-fidelity correction must be evaluated by candidate membership, not only by global regression error.
