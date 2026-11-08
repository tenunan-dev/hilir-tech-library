---
source_id: "wikipedia"
title: "Process_simulation"
url: "https://en.wikipedia.org/wiki/Process_simulation"
retrieved_at: "2026-11-08T15:35:01+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "0c70f904aa6e3c2c08af670db487ffe7b6ab39677ce6c92a211644984dcf1452"
collected: "manual"
summary: "Wikipedia overview of process simulation: steady-state flowsheeting with property methods and unit models, and its role in process design and optimisation."
---

# Process_simulation

# Process simulation

**Process simulation** is used for the design, development, analysis, and optimization of technical process of simulation of processes such as: chemical plants, chemical processes, environmental systems, power stations, complex manufacturing operations, biological processes, and similar technical functions.

## Main principle

\[edit\]
Process simulation is a **model**-based representation of  chemical,  physical,  biological, and other technical processes and unit operations in software. Basic prerequisites for the model are chemical and physical properties<sup>\[1\]</sup> of pure components and mixtures, of reactions, and of mathematical models which, in combination, allow the calculation of process properties by the software.

Process simulation software describes processes in flow diagrams where unit operations are positioned and connected by product or educts streams. The software solves the mass and energy balance to find a stable operating point on specified parameters. The goal of a process simulation is to find optimal conditions for a process. This is essentially an optimization problem which has to be solved in an iterative process.

In the example above the feed stream to the column is defined in terms of its chemical and physical properties. This includes the composition of individual molecular species in the stream; the overall mass flowrate; the streams pressure and temperature. For hydrocarbon systems the Vapor-Liquid Equilibrium Ratios (K-Values) or models that are used to define them are specified by the user. The properties of the column are defined such as the inlet pressure and the number of theoretical plates. The duty of the reboiler and overhead condenser are calculated by the model to achieve a specified composition or other parameter of the bottom and/or top product. The simulation calculates the chemical and physical properties of the product streams, each is assigned a unique number which is used in the mass and energy diagram.

Process simulation uses models which introduce approximations and assumptions but allow the description of a property over a wide range of temperatures and pressures which might not be covered by available real data. Models also allow interpolation and extrapolation - within certain limits - and enable the search for conditions outside the range of known properties.

## Modelling

\[edit\]
The development of models<sup>\[2\]</sup> for a better representation of real processes is the core of the further development of the simulation software. Model development is done through the principles of chemical engineering but also control engineering and for the improvement of mathematical simulation techniques. Process simulation is therefore a field where practitioners from chemistry, physics, computer science, mathematics, and engineering work together.

Efforts are made to develop new and improved models for the calculation of properties. This includes for example the description of

- thermophysical properties like vapor pressures, viscosities, caloric data, etc. of pure components and mixtures
- properties of different apparatus like reactors, distillation columns, pumps, etc.
- chemical reactions and kinetics
- environmental and safety-related data

There are two main types of models:

1. Simple equations and correlations where parameters are fitted to experimental data.
2. Predictive methods where properties are estimated.

The equations and correlations are normally preferred because they describe the property (almost) exactly. To obtain reliable parameters it is necessary to have experimental data which are usually obtained from factual data banks<sup>\[3\]</sup><sup>\[4\]</sup> or, if no data are publicly available, from measurements.

Using predictive methods is more cost effective than experimental work and also than data from data banks. Despite this advantage predicted properties are normally only used in early stages of the process development to find first approximate solutions and to exclude false pathways because these estimation methods normally introduce higher errors than correlations obtained from real data.

Process simulation has encouraged the development of mathematical models in the fields of numerics and the solving of complex problems.<sup>\[5\]</sup><sup>\[6\]</sup>

## History

\[edit\]
The history of process simulation is related to the development of the computer science and of computer hardware and programming languages. Early implementations of partial aspects of chemical processes were introduced in the 1970s when suitable hardware and software (here mainly the programming languages FORTRAN and C) became available. The modelling of chemical properties began much earlier, notably the cubic equation of states and the Antoine equation were precursory developments of the 19th century.

## Steady state and dynamic process simulation

\[edit\]
Initially process simulation was used to simulate steady state processes. Steady-state models perform a mass and energy balance of a steady state process (a process in an equilibrium state) independent of time.

Dynamic simulation is an extension of steady-state process simulation whereby time-dependence is built into the models via derivative terms i.e. accumulation of mass and energy. The advent of dynamic simulation means that the time-dependent description, prediction and control of real processes in real time has become possible. This includes the description of starting up and shutting down a plant, changes of conditions during a reaction, holdups, thermal changes and more.

Process simulation software can also be developed for specific industrial fields. An example is DPSIM, which is oriented toward mineral processing flowsheets and includes steady-state and dynamic process simulation capabilities.<sup>\[7\]</sup>

Dynamic simulation require increased calculation time and are mathematically more complex than a steady state simulation. It can be seen as a multiple repeated steady state simulation (based on a fixed time step) with constantly changing parameters.

Dynamic simulation can be used in both an online and offline fashion. The online case being model predictive control, where the real-time simulation results are used to predict the changes that would occur for a control input change, and the control parameters are optimised based on the results. Offline process simulation can be used in the design, troubleshooting and optimisation of process plant as well as the conduction of case studies to assess the impacts of process modifications. Dynamic simulation is also used for operator training.

## See also

\[edit\]
## References

\[edit\]
1. ↑ Rhodes C.L., “The Process Simulation Revolution: Thermophysical Property Needs and Concerns”, J.Chem.Eng.Data, 41, 947-950, 1996
2. ↑ Gani R., Pistikopoulos E.N., “Property Modelling and Simulation for Product and Process Design″, Fluid Phase Equilib., 194-197, 43-59, 2002
3. ↑ Marsh K., Satyro M.A., “Integration of Databases and their Impact on Process Simulation and Design”, Conference, Lake Tahoe, USA, 1994, 1-14, 1994
4. ↑ Wadsley M.W., “Thermochemical and Thermophysical Property Databases for Computational Chemical Process Simulation”, Conference, Korea, Seoul, August 30 - September 2, 1998, 253-256, 1998
5. ↑ Saeger R.B., Bishnoi P.R., “A Modified 'Inside-Out' Algorithm for Simulation of Multistage Multicomponent Separation Processes Using the UNIFAC Group-Contribution Method”, Can.J.Chem.Eng., 64, 759-767, 1986
6. ↑ Mallya J.U., Zitney S.E., Choudhary S., Stadtherr M.A., “Parallel Frontal Solver for Large-Scale Process Simulation and Optimization″, AIChE J., 43(4), 1032-1040, 1997
7. ↑ "Mineral Process Simulation". *DPSIM*. Retrieved 6 September 2026.
8. ↑ "ASL: Physical Vapor Deposition Simulation".
