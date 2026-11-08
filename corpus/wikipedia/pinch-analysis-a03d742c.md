---
source_id: "wikipedia"
title: "Pinch_analysis"
url: "https://en.wikipedia.org/wiki/Pinch_analysis"
retrieved_at: "2026-11-08T15:35:00+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "a03d742cd013d56f78ed13b4d709c35fd99a5875d25918a3b579de12697b79c5"
collected: "manual"
summary: "Wikipedia overview of pinch analysis: heat-recovery targeting from composite curves, the pinch temperature concept and energy-saving network design."
---

# Pinch_analysis

# Pinch analysis

**Pinch analysis** is a methodology for minimising energy consumption of chemical processes by calculating thermodynamically feasible *energy targets* (or minimum energy consumption) and achieving them by optimising heat recovery systems, energy supply methods and process operating conditions. It is also known as *process integration*, *heat integration*, *energy integration* or *pinch technology*.

The process data is represented as a set of energy flows, or streams, as a function of heat load (product of specific enthalpy and mass flow rate; SI unit W) against temperature (SI unit K).  These data are combined for all the streams in the plant to give *composite curves*, one for all *hot streams* (releasing heat) and one for all *cold streams* (requiring heat). The point of closest approach between the hot and cold composite curves is the *pinch point* (or just *pinch*) with a hot stream pinch temperature and a cold stream pinch temperature.  This is where the design is most constrained.  Hence, by finding this point and starting the design there, the energy targets can be achieved using heat exchangers to recover heat between hot and cold streams in two separate systems, one for temperatures above pinch temperatures and one for temperatures below pinch temperatures. In practice, during the pinch analysis of an existing design, often cross-pinch exchanges of heat are found between a hot stream with its temperature above the pinch and a cold stream below the pinch. Removal of those exchangers by alternative matching makes the process reach its *energy target*.

## History

\[edit\]
In 1971, Ed Hohmann stated in his PhD thesis that

one can compute the least amount of hot and cold utilities required for a process without knowing the heat exchanger network that could accomplish it. One also can estimate the heat exchange area required


In late 1977, Ph.D. student Bodo Linnhoff under the supervision of Dr John Flower at the University of Leeds<sup>\[1\]</sup>  showed the existence in many processes of a heat integration bottleneck, ‘the pinch’, which laid the basis for the technique, known today as pinch-analysis. At that time he had joined Imperial Chemical Industries (ICI) where he led practical applications and further method development.

Bodo Linnhoff developed the 'Problem Table', an algorithm for calculating the energy targets and worked out the basis for a calculation of the surface area required, known as ‘the spaghetti network’. These algorithms enabled practical application of the technique.

In 1982 he joined University of Manchester Institute of Technology (UMIST, present day University of Manchester) to continue the work. In 1983 he set up a consultation firm known as Linnhoff March International later acquired by KBC Energy Services.

Many refinements have been developed since and used in a wide range of industries, including extension to heat and power systems and
non-process situations. The most detailed explanation of the techniques is by Linnhoff et al. (1982),<sup>\[2\]</sup> Shenoy (1995),<sup>\[3\]</sup> Kemp (2006)<sup>\[4\]</sup> and Kemp and Lim (2020),<sup>\[5\]</sup> while Smith (2005)<sup>\[6\]</sup> includes several chapters on them. Both detailed and simplified (spreadsheet) programs are now available to calculate the energy targets. See Pinch Analysis Software below.

Pinch analysis has been extended beyond energy applications. It now includes:

- Mass Exchange Networks<sup>\[7\]</sup>
- Water pinch<sup>\[8\]</sup><sup>\[9\]</sup><sup>\[10\]</sup>
- Hydrogen pinch<sup>\[11\]</sup><sup>\[12\]</sup>
- Carbon pinch<sup>\[5\]</sup>

## Weaknesses

\[edit\]
Classical pinch-analysis primarily calculates the energy costs for the heating and cooling utility. At the pinch point, where the hot and cold streams are the most constrained, large heat exchangers are required to transfer heat between the hot and cold streams. Large heat exchangers entail high investment costs. In order to reduce capital cost, in practice a minimum temperature difference (Δ T) at the pinch point is demanded, e.g., 10 °F.  It is possible to estimate the heat exchanger area and capital cost, and hence the optimal Δ T minimum value. However, the cost curve is quite flat and the optimum may be affected by "topology traps". The pinch method is not always appropriate for simple networks or where severe operating constraints exist.  Kemp (2006)<sup>\[4\]</sup> and Kemp and Lim (2019) discuss these aspects in detail.

## Recent developments

\[edit\]
The problem of integrating heat between hot and cold streams, and finding the optimal network, in particular in terms of costs, may today be solved with numerical algorithms. The network can be formulated as a so-called mixed integer non-linear programming (MINLP) problem and solved with an appropriate numerical solver. Nevertheless, large-scale MINLP problems can still be hard to solve for today's numerical algorithms. Alternatively, some attempts were made to formulate the MINLP problems to mixed integer linear problems, where then possible networks are screened and optimized.  For simple networks of a few streams and heat exchangers, hand design methods with simple targeting software are often adequate, and aid the engineer in understanding the process.<sup>\[13\]</sup>

## See also

\[edit\]
- CHP Directive – EU Directive on cogeneration of heat and power
- Energy policy of the European Union – Legislation in the area of energetics in the European Union
- Relative cost of electricity generated by different sources – Comparison of costs of different electricity generation sources
- Cogeneration – Simultaneous generation of electricity and useful heat
- Process flowsheeting

## References

\[edit\]
1. ↑ Ebrahim, M.; Kawari, Al- (2000). "Pinch technology: an efficient tool for chemical-plant energy and capital-cost saving". *Applied Energy*. **65** (1–4): 45–49. doi:10.1016/S0306-2619(99)00057-4.
2. ↑ Linnhoff, B., D.W. Townsend, D. Boland,  G.F. Hewitt, B.E.A. Thomas, A.R. Guy and R.H. Marsland, (1982) *A User Guide on Process Integration for the Efficient Use of Energy.* IChemE, UK.
3. ↑ Shenoy, U.V. (1995). *Heat Exchanger Network Synthesis: Process Optimization by Energy and Resource Analysis*. Includes two computer disks. Gulf Publishing Company, Houston, TX, USA. ISBN 0-88415-391-6.
4. 1 2 Kemp, I.C. (2006). *Pinch Analysis and Process Integration: A User Guide on Process Integration for the Efficient Use of Energy, 2nd edition*. Includes spreadsheet software. Butterworth-Heinemann. ISBN 0-7506-8260-4. (1st edition: Linnhoff et al., 1982)
5. 1 2 Kemp, I.C. and Lim, J.S. (2020). *Pinch Analysis for Energy and Carbon Footprint Reduction: A User Guide on Process Integration for the Efficient Use of Energy, 3rd edition*. Includes spreadsheet software. Butterworth-Heinemann. ISBN 978-0-08-102536-9.
6. ↑ Smith, R. (2005). *Chemical Process Design and Integration*. John Wiley and Sons. ISBN 0-471-48680-9
7. ↑ El-Halwagi, M. M. and V. Manousiouthakis, 1989, "Synthesis of Mass Exchange Networks", AIChE J., 35(8), 1233–1244
8. ↑ Wang, Y. P. and Smith, R. (1994). Wastewater Minimisation. Chemical Engineering Science. 49: 981-1006
9. ↑ Prakash, R. and Shenoy, U.V. (2005) Targeting and Design of Water Networks for Fixed Flowrate and Fixed Contaminant Load Operations. Chemical Engineering Science. 60(1), 255-268
10. ↑ Hallale, Nick. (2002). A New Graphical Targeting Method for Water Minimisation. Advances in Environmental Research. 6(3): 377-390
11. ↑ Nick Hallale, Ian Moore, Dennis Vauk, "Hydrogen optimization at minimal investment", Petroleum Technology Quarterly (PTQ), Spring (2003)
12. ↑ Agrawal, V. and U. V. Shenoy, 2006, "Unified Conceptual Approach to Targeting and Design of Water and Hydrogen Networks", AIChE J., 52(3), 1071–1082.
13. ↑ Furman, Kevin C.; Sahinidis, Nikolaos V. (2002-03-09). "A Critical Review and Annotated Bibliography for Heat Exchanger Network Synthesis in the 20th Century". *Industrial & Engineering Chemistry Research*. **41** (10): 2335–2370. doi:10.1021/ie010389e.

- de Klerk, LW, de Klerk, MP and van der Westhuizen, D "Improvements in hydrometallurgical uranium circuit capital and operating costs by water management and integration of utility and process energy targets" AusImm Conference, U 2015 Archived 2016-04-25 at the Wayback Machine

## External links

\[edit\]
- PinCH - Software for continuous and batch processes including indirect heat recovery loops and energy storages. Free manuals, tutorials, case studies and success stories available
- HeatIT - Free (light) version of Pinch Analysis software that runs in Excel - developed by Pinchco, a consultancy company offering expert advice on energy related matters
- Simulis Pinch - A powerful tool from Fives ProSim SAS that can be used directly in Excel and that is dedicated to the diagnosis and the energy integration of the processes.
- Integration - A practical and low-cost process integration computation tool developed by CanmetENERGY, Canada's leading research and technology organization in the field of clean energy.
- Pinch Analysis Tool - TLK-Energy's online pinch analysis software enables you to swiftly identify efficiency potential in unused waste heat flows and optimally integrate heat pumps for your industrial operation.
