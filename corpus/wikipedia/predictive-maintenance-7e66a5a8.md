---
source_id: "wikipedia"
title: "Predictive_maintenance"
url: "https://en.wikipedia.org/wiki/Predictive_maintenance"
retrieved_at: "2026-11-08T02:02:47+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "7e66a5a8e49a1e56b44ac229e9c3bf982f0b188ca8d8379cd6647fb17f196f62"
collected: "manual"
summary: "Wikipedia overview of predictive maintenance: condition monitoring techniques, data-driven and model-based failure prediction, and its contrast with preventive and reactive maintenance."
---

# Predictive_maintenance

# Predictive maintenance

**Predictive maintenance** (**PdM**)<sup>\[1\]</sup> techniques are designed to help determine the condition of in-service equipment in order to estimate when maintenance should be performed. This approach claims more cost savings over routine or time-based preventative maintenance, because tasks are performed only when warranted. Thus, it is regarded as condition-based maintenance carried out as suggested by estimations of the degradation state of an item.<sup>\[2\]</sup><sup>\[3\]</sup>

The main appeal of predictive maintenance is to allow convenient scheduling of corrective maintenance, and to prevent unexpected equipment failures. By taking into account measurements of the state of the equipment, maintenance work can be better planned (spare parts, people, etc.) and what would have been "unplanned stops" are transformed to shorter and fewer "planned stops", thus increasing plant availability. Other potential advantages include increased equipment lifetime, increased plant safety, fewer accidents with negative impact on environment, and optimized spare parts handling.

Predictive maintenance differs from preventive maintenance because it does take into account the current condition of equipment (with measurements), instead of average or expected life statistics, to predict when maintenance will be required. Machine Learning approaches are adopted for the forecasting of its future states.<sup>\[4\]</sup>

Some of the main components that are necessary for implementing predictive maintenance are data collection and preprocessing, early fault detection, fault detection, time to failure prediction, and maintenance scheduling and resource optimization.<sup>\[5\]</sup> Predictive maintenance has been considered one of the driving forces for improving productivity and a way to achieve just-in-time manufacturing.<sup>\[6\]</sup><sup>\[7\]</sup>

## Overview

\[edit\]
Predictive maintenance evaluates the condition of equipment by performing periodic (offline) or continuous (online) equipment condition monitoring. The ultimate goal of the approach is to perform maintenance at a scheduled point in time when the maintenance activity is most cost-effective and before the equipment loses performance within a threshold. This results in a reduction in unplanned downtime costs because of failure, where costs can be in the hundreds of thousands per day depending on industry.<sup>\[8\]</sup> In energy production, in addition to loss of revenue and component costs, fines can be levied for non-delivery, increasing costs even further. This is in contrast to time- and/or operation count-based maintenance, where a piece of equipment gets maintained whether it needs it or not. Time-based maintenance is labor intensive, ineffective in identifying problems that develop between scheduled inspections, and therefore is not cost-effective.

The "predictive" component of predictive maintenance stems from the goal of predicting the future trend of the equipment's condition. This approach uses principles of statistical process control to determine at what point in the future maintenance activities will be appropriate.

Most predictive inspections are performed while equipment is in service, thereby minimizing disruption of normal system operations. Adoption of predictive maintenance can result in substantial cost savings and higher system reliability. In today's dynamic landscape of service maintenance, prolonged repair processes present a significant challenge for organizations striving to maintain operational excellence. Extended downtime, increased Mean Time to Repair (MTTR), and production losses not only affect profitability but also disrupt service continuity and diminish customer satisfaction. As equipment ages and maintenance requirements intensify, the quest for innovative solutions becomes increasingly urgent.

One goal is to transfer the predictive maintenance data to a computerized maintenance management system so that the equipment condition data is sent to the right equipment object to trigger maintenance planning, work order execution, and reporting.<sup>\[9\]</sup> Unless this is achieved, the predictive maintenance solution is of limited value, at least if the solution is implemented on a medium to large size plant with tens of thousands pieces of equipment. In 2010, the mining company Boliden, implemented a combined Distributed Control System and predictive maintenance solution integrated with the plant computerized maintenance management system on an object to object level, transferring equipment data using protocols like Highway Addressable Remote Transducer Protocol, IEC61850 and OLE for process control.

## Technologies

\[edit\]
To evaluate equipment condition, predictive maintenance utilizes nondestructive testing technologies such as infrared, acoustic (partial discharge and airborne ultrasonic), corona detection, vibration analysis, sound level measurements, oil analysis, and other specific online tests. A new approach in this area is to utilize measurements on the actual equipment in combination with measurement of process performance, measured by other devices, to trigger equipment maintenance. This is primarily available in collaborative process automation systems (CPAS). Site measurements are often supported by wireless sensor networks to reduce the wiring cost.

Vibration analysis is most productive on high-speed rotating equipment and can be the most expensive component of a PdM program to get up and running. Vibration analysis, when properly done, allows the user to evaluate the condition of equipment and avoid failures. The latest generation of vibration analyzers comprises more capabilities and automated functions than its predecessors. Many units display the full vibration spectrum of three axes simultaneously, providing a snapshot of what is going on with a particular machine. But despite such capabilities, not even the most sophisticated equipment successfully predicts developing problems unless the operator understands and applies the basics of vibration analysis.<sup>\[10\]</sup>

In certain situations, strong background noise interferences from several competing sources may mask the signal of interest and hinder the industrial applicability of vibration sensors. Consequently, motor current signature analysis (MCSA) is a non-intrusive alternative to vibration measurement which has the potential to monitor faults from both electrical and mechanical systems.

Remote visual inspection is the first non-destructive testing. It provides a cost-efficient primary assessment. Essential information and defaults can be deduced from the external appearance of the piece, such as folds, breaks, cracks, and corrosion. The remote visual inspection has to be carried out in good conditions with a sufficient lighting (350 LUX at least). When the part of the piece to be controlled is not directly accessible, an instrument made of mirrors and lenses called endoscope is used. Hidden defects with external irregularities may indicate a more serious defect inside.<sup>\[11\]</sup>

Acoustical analysis can be done on a sonic or ultrasonic level. New ultrasonic techniques for condition monitoring make it possible to "hear" friction and stress in rotating machinery, which can predict deterioration earlier than conventional techniques.<sup>\[12\]</sup> Ultrasonic technology is sensitive to high-frequency sounds that are inaudible to the human ear and distinguishes them from lower-frequency sounds and mechanical vibration. Machine friction and stress waves produce distinctive sounds in the upper ultrasonic range.
Changes in these friction and stress waves can suggest deteriorating conditions much earlier than technologies such as vibration or oil analysis. With proper ultrasonic measurement and analysis, it's possible to differentiate normal wear from abnormal wear, physical damage, imbalance conditions, and lubrication problems based on a direct relationship between asset and operating conditions.

Sonic monitoring equipment is less expensive, but it also has fewer uses than ultrasonic technologies. Sonic technology is useful only on mechanical equipment, while ultrasonic equipment can detect electrical problems and is more flexible and reliable in detecting mechanical problems.

Infrared monitoring and analysis has the widest range of application (from high- to low-speed equipment), and it can be effective for spotting both mechanical and electrical failures; some consider it to currently be the most cost-effective technology. 
Oil analysis is a long-term program that, where relevant, can eventually be more predictive than any of the other technologies. It can take years for a plant's oil program to reach this level of sophistication and effectiveness. 
Analytical techniques performed on oil samples can be classified in two categories: used oil analysis and wear particle analysis. Used oil analysis determines the condition of the lubricant itself, determines the quality of the lubricant, and checks its suitability for continued use. Wear particle analysis determines the mechanical condition of machine components that are lubricated. Through wear particle analysis, you can identify the composition of the solid material present and evaluate particle type, size, concentration, distribution, and morphology.<sup>\[13\]</sup>

Model-based condition monitoring is another approach used in predictive maintenance programs. It involves analyzing electrical signals, such as motor current and voltage, and comparing measured parameters to a reference model in order to identify deviations associated with faults. This method has been applied in aerospace and industrial systems.<sup>\[14\]</sup> Model-based systems can support automated data analysis and continuous monitoring. Additional predictive maintenance methods include various data-driven and smart testing strategies.<sup>\[15\]</sup>

## Applications

\[edit\]
### Vehicle predictive maintenance

\[edit\]
An application of predictive maintenance is in the automotive and transportation sectors, particularly in fleet management. The process relies on telematics to collect real-time data from vehicles. A telematic control unit installed in a vehicle continuously gathers telemetry from the engine's CAN bus, including diagnostic trouble codes (DTCs), fuel consumption, and component status.<sup>\[*citation needed*\]</sup>

This data is then transmitted to a fleet telematics system, where machine learning algorithms analyze it to detect patterns that precede failures. This allows the system to predict potential issues with critical components, such as the battery, starter motor, or brakes, before they result in a breakdown.<sup>\[16\]</sup> This approach is a component of modern fleet digitalization, enabling businesses to schedule maintenance at a cost-effective time, reduce unplanned downtime, and improve vehicle reliability.

### Environmental monitoring

\[edit\]
- Detect changes of the calibration distribution (i.e., statistical distribution of pollutants and environmental conditions) for low-cost gas sensor systems.<sup>\[17\]</sup>

### Railway

\[edit\]
- Detect warning signs before they cause downtime for linear, fixed and mobile assets.<sup>\[18\]</sup>
- Improving safety and track void detection through a new vehicle cab-based monitoring system
- Can also identify the type of track asset that the void is located under and provide an indication of the severity of the void
- Health Monitoring of point Machines (devices used to operate railway turnouts) can aid in detecting early symptoms of degradation prior to failure.

### Manufacturing

\[edit\]
- Early fault detection and diagnosis in the manufacturing industry.<sup>\[6\]</sup>
- Manufacturers increasingly collect big data from Internet of Things (IoT) sensors in their factories and products and using different algorithms for the collected data to detect warning signs of expensive failures before they occur.<sup>\[19\]</sup>

### Oil and gas

\[edit\]
- Oil and gas companies often lack visibility into the condition of their equipment, especially in remote offshore and deep-water locations.<sup>\[20\]</sup>
- Big data can provide insight to oil and gas companies, this way equipment failures and the optimal lifetime of the system and components can be analyzed and predicted.<sup>\[20\]</sup>

## See also

\[edit\]
## References

\[edit\]
1. ↑ Nunes, P.; Santos, J.; Rocha, E. (2023). "Challenges in predictive maintenance – A review". *CIRP Journal of Manufacturing Science and Technology*. **40**: 53–67. doi:10.1016/j.cirpj.2022.11.004.
2. ↑ Goriveau, Rafael; Medjaher, Kamal; Zerhouni, Noureddine (2016-11-14). *From prognostics and health systems management to predictive maintenance 1 : monitoring and prognostics*. ISTE Ltd and John Wiley & Sons, Inc. ISBN 978-1-84821-937-3.
3. ↑ Mobley, R. Keith (2002). *An introduction to predictive maintenance* (2nd ed.). Butterworth-Heinemann. pp. 4–6. ISBN 978-0-7506-7531-4.
4. ↑ Susto, Gian Antonio (2015). "Machine Learning for Predictive Maintenance: A Multiple Classifier Approach". *IEEE Transactions on Industrial Informatics*. **11** (3): 812–820. Bibcode:2015ITII...11..812S. doi:10.1109/TII.2014.2349359. S2CID 18888927.
5. ↑ Amruthnath, Nagdev; Gupta, Tarun (February 2018). "Fault Class Prediction in Unsupervised Learning using Model-Based Clustering Approach". *ResearchGate*. doi:10.13140/rg.2.2.22085.14563.
6. 1 2 Amruthnath, Nagdev; Gupta, Tarun (April 2018). "A Research Study on Unsupervised Machine Learning Algorithms for Fault Detection in Predictive Maintenance". *ResearchGate*. doi:10.13140/rg.2.2.28822.24648.
7. ↑ Chiorean, Ligia-D.; Vaida, Mircea-F.; Hedesiu, Horia (November 2020). "Modelling an OPC UA client application for predictive maintenance support". *2020 International Symposium on Electronics and Telecommunications (ISETC)*. pp. 1–4. doi:10.1109/ISETC50328.2020.9301058. ISBN 978-1-7281-8921-5.
8. ↑ "How Much Does Predictive Maintenance Save You Money?". *LearnOilAnalysis.com*. Archived from the original on 2017-10-03. Retrieved 2017-12-03.
9. ↑ Peng, K. (2012). *Equipment Management in the Post-Maintenance Era: A New Alternative to Total Productive Maintenance (TPM)*. CRC Press. pp. 132–136. ISBN 9781466501942. Retrieved 18 May 2018.
10. ↑ Yung, Chuck (June 9, 2006). "Vibration analysis: what does it mean?". *Plant Services*. Putman Media. Archived from the original on June 29, 2006. Retrieved June 12, 2025.
11. ↑ "AI-Based Predictive Maintenance for Marine Auxiliary Engines". *Mega Marine*. 2024-05-20. Retrieved 2025-09-29.
12. ↑ Kennedy, Sheila (2006). "New tools for PdM". *Plant Services*. Putman Media. Archived from the original on May 21, 2006. Retrieved June 12, 2025.
13. ↑ Robin, Lana (August 15, 2006). "Slick tricks in oil analysis". *Plant Services*. Putman Media. Archived from the original on October 17, 2006. Retrieved June 12, 2025.
14. ↑ Duyar, Ahmet; Merrill, Walter (March 1992). "Fault diagnosis for the Space Shuttle main engine". *Journal of Guidance, Control, and Dynamics*. **15** (2): 384–9. Bibcode:1992JGCD...15..384D. doi:10.2514/3.20847.
15. ↑ Douek-Pinkovich, Y.; Ben-Gal, I.; Raviv, T. (2022). "The Stochastic Test Collection Problem: Models, Exact and Heuristic Solution Approaches" (PDF). *European Journal of Operational Research*. **299** (3): 945–959. doi:10.1016/j.ejor.2021.12.043.
16. ↑ "Staying Ahead Of The Curve: 3 Key Fleet Management Trends For 2023". *Forbes*. April 18, 2023. Retrieved September 29, 2025.
17. ↑ Tancev, Georgi (May 2021). "Relevance of Drift Components and Unit-to-Unit Variability in the Predictive Maintenance of Low-Cost Electrochemical Sensor Systems in Air Quality Monitoring". *Sensors*. **21** (9): 3298. Bibcode:2021Senso..21.3298T. doi:10.3390/s21093298. PMC 8126229. PMID 34068777.
18. ↑ 
*Predictive maintenance benefits for the railway industry*, 13 April 2015, archived from the original on 2016-11-29, retrieved 19 November 2016
19. ↑ 
Trotman, William, *5 Use Cases for Predictive Maintenance and Big Data, Oracle Corporation, CA 94065 USA.*, retrieved 8 November 2018
20. 1 2 *22 Big Data Use Cases You Want to Know, Oracle Corporation, CA 94065 USA*, retrieved 31 October 2018
