---
source_id: "wikipedia"
title: "Digital_twin"
url: "https://en.wikipedia.org/wiki/Digital_twin"
retrieved_at: "2026-11-08T02:02:46+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "268ab8be1bc96e1c76972f80fff81e0037107f35f82a540f454d66b929bcdabb"
collected: "manual"
summary: "Wikipedia overview of digital twins: virtual replicas coupled to physical assets, enabling characteristics, and applications from manufacturing to process plants."
---

# Digital_twin

# Digital twin

A **digital twin** is a computational model of an intended or actual real-world physical product, system, or process (a *physical twin*) that serves as a digital counterpart of it for purposes such as simulation, integration, testing, monitoring, and maintenance.<sup>\[1\]</sup><sup>\[2\]</sup><sup>\[3\]</sup>
By its strict definition, a digital twin is distinguished from an ordinary simulation in that it continuously uses real data from its physical counterpart to dynamically synchronize with the real system.<sup>\[4\]</sup><sup>\[5\]</sup> A model that operates without data from its physical counterpart may also be described as a digital twin, but this is considered an overly broad and largely marketing-oriented interpretation of the concept.<sup>\[6\]</sup>

A digital twin is "a set of adaptive models that emulate the behaviour of a physical system in a virtual system getting real-time data to update itself along its life cycle. The digital twin replicates the physical system to predict failures and opportunities for changing, to prescribe real time actions for optimizing and/or mitigating unexpected events observing and evaluating the operating profile of the system."<sup>\[7\]</sup> Though the concept originated earlier (as a natural aspect of computer simulation generally), the first practical definition of a digital twin originated from NASA in an attempt to improve the physical-model simulation of spacecraft in 2010.<sup>\[8\]</sup> Digital twins emerged through continual improvements in modeling and engineering.

In the 2010s and 2020s, manufacturing industries began moving beyond digital product definition to extending the digital twin concept to the entire manufacturing process. Doing so allows the benefits of virtualization to be extended to domains such as inventory management including lean manufacturing, machinery crash avoidance, tooling design, troubleshooting, and preventive maintenance. Digital twinning therefore allows extended reality and spatial computing to be applied not just to the product itself but also to all of the business processes that contribute to its production.<sup>\[*citation needed*\]</sup>

## History

\[edit\]
Early ideas of the model date back to the 1960s, when NASA began working with a "living model" to simulate missions from the Apollo program.<sup>\[9\]</sup> Their employment came after the oxygen tank explosion during the Apollo 13 mission. According to the American Society of Mechanical Engineers (ASME) Digital Twin Summit Keynote, the simulations were developed to closely mimic the conditions of real aircraft with the purpose of studying the tank failure in order to navigate different solutions and their effects. The keynote also showed that there were as many as fifteen simulations used with astronauts and mission controllers for training purposes.<sup>\[9\]</sup>

The broader idea that became the digital twin concept was anticipated by David Gelernter's 1991 book *Mirror Worlds*.<sup>\[10\]</sup><sup>\[11\]</sup> Dr. Michael Grieves first introduced the formal three-part concept of the digital twin back in 2002 during an industry presentation centered around Product life-cycle management (marketing), when he presented a slide depicting this process titled "Conceptual Ideal for PLM".<sup>\[12\]</sup> At the time, the model was often referred to as the "Mirrored Spaces Model", but its name was later changed by Grieves to "Information Mirroring Model" to emphasize the functionality of the link between real and digital spaces. It wasn't until 2010 that the name "Digital Twin" was officially coined by John Vickers of NASA in a draft of their technological roadmap for that year.<sup>\[13\]</sup>

During the late 1990s, the emergence of digital cities provided early practical demonstrations of this concept at an urban scale. Projects such as "Helsinki Arena 2000" (initiated in 1996) built interactive 3D virtual models of the physical city.<sup>\[14\]</sup> Shortly after, Digital City Kyoto (launched in 1998) advanced the paradigm by explicitly connecting physical urban environments with virtual spaces; it integrated real-time physical sensor data—such as live camera feeds from transit stations—into its 3D environment, foreshadowing the data-driven synchronization of modern digital twins.<sup>\[15\]</sup>

The digital twin concept consists of three distinct parts: the physical object or process and its physical environment, the digital representation of the object or process, and the communication channel between the physical and virtual representations. The connections between the physical version and the digital version include information flows and data that includes physical sensor flows between the physical and virtual objects and environments. The communication connection is referred to as the digital thread.<sup>\[*citation needed*\]</sup>

The International Council of Systems Engineers (INCOSE) maintains in its Systems Engineering Body of Knowledge (SEBoK) that: "A digital twin is a related yet distinct concept to digital engineering. The digital twin is a high-fidelity model of the system which can be used to emulate the actual system."<sup>\[16\]</sup> The evolving US DoD *Digital Engineering Strategy* initiative, first formulated in 2018, defines a digital twin as "an integrated multiphysics, multiscale, probabilistic simulation of an as-built system, enabled by a Digital Thread, that uses the best available models, sensor information, and input data to mirror and predict activities/performance over the life of its corresponding physical twin."<sup>\[17\]</sup>

## Types

\[edit\]
Digital twins are commonly divided into the three subtypes: *digital twin prototype* (DTP),  *digital twin instance* (DTI), and *digital twin aggregate* (DTA).<sup>\[18\]</sup> The DTP consists of the designs, analyses, and processes that realize a physical product. The DTI is the digital twin of each individual instance of the product once it is manufactured. The DTI is linked with its physical counterpart for the remainder of the physical counterpart's life. The DTA is the aggregation of DTIs whose data and information can be used for interrogation about the physical product, prognostics, and learning. The specific information contained in the digital twins is driven by use cases. The digital twin is a logical construct, meaning that the actual data and information may be contained in other applications.<sup>\[*citation needed*\]</sup>

For some types of digital twin, there is contention about whether the label truly applies. For example, LNS Research defines "digital twin" as any executable virtual model of a physical system. Researchers at the National Physical Laboratory have contested this definition, arguing that this includes "plain" models that do not produce results equivalent to measured quantities or are not dynamically updated in accordance with those measurements. They argue that this overly broad definition risks causing potential users to view "digital twin" as a buzzword and become cynical toward the idea.<sup>\[6\]</sup> The term has also been applied to large language models trained to mimic specific people. Describing these as "digital twins" implies a level of comprehensive fidelity that they fail to live up to in practice, and can cause psychological harm to users who believe that the model preserves or replicates human identity.<sup>\[19\]</sup>

## Examples

\[edit\]
### Manufacturing industry

\[edit\]
#### Civil aviation and transportation

\[edit\]
In 2019 Sheremetyevo International Airport started developing and implementation of a digital twin model aimed to forecast and plan all the airport operations. Even being launched on pilot level it already resulted in more than 1 billion rubles savings (more than US$120 million)<sup>\[20\]</sup>

#### Design and prototyping

\[edit\]
In the design phase, a Digital Twin Prototype (DTP) is often created before a physical product exists.<sup>\[21\]</sup><sup>\[22\]</sup> This virtual model is used for extensive simulation to test design choices and manufacturing processes. For example, in virtual commissioning, a digital twin of a proposed production line can simulate its operation to identify bottlenecks, optimize the layout of machinery, and validate automation logic before any physical equipment is installed.<sup>\[21\]</sup> For complex processes like welding, a digital twin can be used for process planning by simulating the heat distribution and material properties of a proposed weld joint, allowing engineers to define and qualify a Welding Procedure Specification (WPS) virtually, thereby reducing the need for costly physical tests.<sup>\[23\]</sup>

#### Production and operations

\[edit\]
During production, digital twins use data from sensors connected to manufacturing equipment via the Internet of Things (IoT) to monitor and optimize operations. A distinction is sometimes made between a Digital Shadow, where data flows one way from the physical asset to the digital model, and a true Digital Twin, where the data flow is bidirectional, allowing the twin to also send control commands back to the asset.<sup>\[24\]</sup><sup>\[25\]</sup> Applications in this phase include process monitoring and control, where sensors measuring force, temperature, vibration, or power consumption feed data to a digital twin to monitor a process in real time. In friction stir welding, for instance, force sensor data can indicate whether sufficient contact is being made between the tool and workpieces to ensure a quality weld.<sup>\[23\]</sup> In machining, acoustic emission signals can be analyzed to differentiate a worn tool from a new one, allowing for automated quality control.<sup>\[26\]</sup> Another application is real-time quality inspection, where vision systems integrated with a digital twin can automatically inspect products for defects on the production line. These systems can process images to detect surface defects, such as cracks or porosity in a weld, or measure geometric dimensions to ensure they meet specifications.<sup>\[23\]</sup>

#### Maintenance and service

\[edit\]
After a product is manufactured and in service, its digital twin continues to collect performance data, often referred to as a Digital Twin Instance (DTI).<sup>\[21\]</sup> This is particularly valuable for high-value industrial assets like jet engines, wind turbines, or industrial machinery. One key application is predictive maintenance, where the digital twin analyzes operational data (e.g., temperature, vibration) to predict when a component is likely to fail. For example, a gearbox twin can analyze vibration signals to detect the future breakage of a tooth.<sup>\[23\]</sup> This allows maintenance to be scheduled proactively, reducing unplanned downtime and preventing catastrophic failures. Another application is performance optimization. By aggregating data from a whole fleet of assets—a Digital Twin Aggregate (DTA)—manufacturers can understand how their products perform under different real-world conditions. This information can be used to provide operational guidance to users or to inform the design of future product generations, creating a closed feedback loop from the service phase back to the design phase.<sup>\[21\]</sup>

### Urban planning and the construction industry

\[edit\]
Digital twins are used in construction by creating dynamic digital replicas of physical assets. They support health monitoring, ergonomic risk assessment, and predictive maintenance of structures like bridges and historical buildings. Applications also optimize building energy and carbon performance. Case studies, such as Weihai Port, highlight their practical success. Digital twins rely on robust system architectures and tailored, requirements-driven designs. Advanced models like LSTM enable predictive capabilities, though challenges in integration and scaling remain.<sup>\[27\]</sup>

Recent studies have emphasized their role in enabling real-time operational control of HVAC, lighting, shading, and renewable systems, contributing significantly to decarbonization strategies. Layered system architectures typically comprising sensing, data processing, simulation, and visualization layers that support scalable and interoperable solutions for these applications.<sup>\[28\]</sup>

Geographic digital twins have been popularised in urban planning practice, given the increasing appetite for digital technology in the Smart Cities movement.<sup>\[29\]</sup> These digital twins are often proposed in the form of interactive platforms to capture and display real-time 3D and 4D spatial data in order to model urban environments (cities) and the data feeds within them.<sup>\[30\]</sup>

Beyond civilian urban planning, geographic digital twins are utilized within defense and tactical operations to map physical terrain. These frameworks integrate three-dimensional geographic information systems (GIS) data with live terrain feeds to construct dynamic digital sand models. For example, systems like VizExperts' 3D geospatial twin engine have been introduced into defense frameworks to allow military personnel to simulate mission scenarios, conduct interactive training, and analyze physical environments for strategic operations.<sup>\[31\]</sup>

Visualization technologies such as augmented reality (AR) systems are being used as both collaborative tools for design and planning in the built environment integrating data feeds from embedded sensors in cities<sup>\[27\]</sup> and API services to form digital twins. For example, AR can be used to create augmented reality maps, buildings, and data feeds projected onto tabletops for collaborative viewing by built environment professionals.<sup>\[32\]</sup>

In the built environment, partly through the adoption of building information modeling (BIM) processes, planning, design, construction, and operation and maintenance activities are increasingly being digitised, and digital twins of built assets are seen as a logical extension - at an individual asset level and at a national level. In the United Kingdom in November 2018, for example, the Centre for Digital Built Britain published *The Gemini Principles*,<sup>\[33\]</sup> outlining principles to guide development of a "national digital twin".<sup>\[34\]</sup>

One of the earliest examples of a working 'digital twin' was achieved in 1996 during construction of the Heathrow Express facilities at Heathrow Airport's Terminal 1. Consultant Mott MacDonald and BIM pioneer Jonathan Ingram connected movement sensors in the cofferdam and boreholes to the digital object-model to display movements in the model. A digital grouting object was made to monitor the effects of pumping grout into the earth to stabilise ground movements.<sup>\[35\]</sup>

Digital twins have also been proposed as a method to reduce the need for manual visual inspections of buildings and infrastructure after earthquakes or other extreme events, using unmanned aerial vehicles (UAVs), LiDAR scanning, and photogrammetry to automatically update the virtual model and support rapid damage assessment and response planning.<sup>\[36\]</sup><sup>\[37\]</sup>

### Healthcare industry

\[edit\]
Healthcare has been recognized as an industry being disrupted by the digital twin technology.<sup>\[38\]</sup><sup>\[39\]</sup> The concept was originally proposed and first used in health care product or equipment prognostics.<sup>\[39\]</sup>

With a digital twin, it has been predicted that lives could be improved in terms of medical health, sports and education by taking a more data-driven approach to healthcare. Personalized models for patients, continuously adjustable based on tracked health and lifestyle parameters could ultimately lead to a virtual patient, with detailed description of the healthy state of an individual and not only on previous records. Furthermore, the digital twin could enable individual's records to be compared to the population in order to easier find patterns with great detail.<sup>\[38\]</sup> The biggest benefit of the digital twin on the healthcare industry would be the fact that healthcare could be tailored to anticipate the responses of individual patients. Digital twins have been expected not only to lead to better resolutions when defining the health of an individual but also change the expected image of a healthy person. Previously, 'healthy' was seen as the absence of disease indications. Now, 'healthy' patients can be compared to the rest of the population in order to really define healthy.<sup>\[38\]</sup> However, the emergence of the digital twin in healthcare also may lead to inequality, as the technology might not be accessible for everyone by widening the gap between the rich and poor. Furthermore, the digital twin will identify patterns in a population which may lead to discrimination.<sup>\[38\]</sup>

As of 2025, digital twin applications in healthcare have expanded to include real‑time AI‑driven patient monitoring systems, personalized surgical simulations, and predictive diagnostics using multimodal data (e.g. imaging + wearables).<sup>\[40\]</sup><sup>\[41\]</sup>

### Automotive industry

\[edit\]
Digital twins in the automobile industry are implemented by using existing data in order to facilitate processes and reduce marginal costs. Currently, automobile designers expand the existing physical materiality by incorporating software-based digital abilities.<sup>\[42\]</sup> A specific example of digital twin technology in the automotive industry is where automotive engineers use digital twin technology in combination with the firm's analytical tool in order to analyze how a specific car is driven. In doing so, they can suggest incorporating new features in the car that can reduce car accidents on the road, which was previously not possible in such a short time frame.<sup>\[43\]</sup> Digital twins can be built for not just individual vehicles but also the whole mobility system, where humans (e.g., drivers, passengers, pedestrians), vehicles (e.g., connected vehicles, connected and automated vehicles), and traffics (e.g., traffic networks, traffic infrastructures) can seek guidance from their digital twins deployed on edge/cloud servers to actuate real-time decisions.<sup>\[44\]</sup>

### Renewable energy industry

\[edit\]
Digital twins are increasingly employed in the renewable energy industry to monitor and optimize systems such as wind farms, solar installations, microgrids, and battery storage. These virtual models help operators simulate real-world conditions, forecast issues, and enhance operational efficiency in a low-risk environment.<sup>\[45\]</sup>

Recent reviews emphasize that digital twins support advanced management strategies for microgrids, such as day-ahead scheduling and real-time coordination across renewable assets, enhancing grid resilience.<sup>\[46\]</sup> Systematic analysis further shows that combining digital twins with predictive analytics in smart energy systems can reduce energy consumption by up to 30%, thanks to optimized load balancing and proactive maintenance.<sup>\[47\]</sup>

Real-world applications are growing. A UK-based demonstrator project used a digital twin for voltage control simulations in a microgrid, showing a reduction of renewable curtailment by approximately 56% in typical operation.<sup>\[48\]</sup> Utilities and technology providers worldwide are now piloting twin platforms to anticipate turbine maintenance, improve battery storage usage, and simulate grid behavior under extreme or variable conditions, indicating a trend toward more automated and resilient energy systems.<sup>\[*citation needed*\]</sup>

### Heritage

\[edit\]
Digital twin technology is used in heritage and archaeological contexts to anticipate heritage loss and ensuring that an accurate record exists for heritage assets at risk, and engaging with planners to anticipate the needs of the cultural heritage sector.<sup>\[49\]</sup> Twins can also be drivers for tourism and urban heritage trails, where they can act as introductions to significant or iconic monuments, thereby using heritage to draw people into urban centres.

## Related technologies

\[edit\]
## References

\[edit\]
1. ↑ Moi, Torbjørn; Cibicik, Andrej; Rølvåg, Terje (May 2020). "Digital twin based condition monitoring of a knuckle boom crane: An experimental study". *Engineering Failure Analysis*. **112** 104517. doi:10.1016/j.engfailanal.2020.104517. hdl:11250/2650461.
2. ↑ Haag, Sebastian; Anderl, Reiner (January 2018). "Digital twin – Proof of concept". *Manufacturing Letters*. **15**: 64–66. doi:10.1016/j.mfglet.2018.02.006.
3. ↑ Boschert, Stefan; Rosen, Roland (2016). "Digital Twin—The Simulation Aspect". *Mechatronic Futures*. pp. 59–74. doi:10.1007/978-3-319-32156-1\_5. ISBN 978-3-319-32154-7.
4. ↑ "Understanding Digital Twins". PTC. 2021.
5. ↑ Grieves, Michael; Vickers, John (2017). "Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems". *Transdisciplinary Perspectives on Complex Systems*. Springer. pp. 85–113. doi:10.1007/978-3-319-38756-7\_4. ISBN 978-3-319-38754-3.
6. 1 2 Wright, Louise; Davidson, Stuart (2020-03-11). "How to tell the difference between a model and a digital twin". *Advanced Modeling and Simulation in Engineering Sciences*. **7** (1) 13. doi:10.1186/s40323-020-00147-4. ISSN 2213-7467.
7. ↑ Semeraro, Concetta; Lezoche, Mario; Panetto, Hervé; Dassisti, Michele (September 2021). "Digital twin paradigm: A systematic literature review". *Computers in Industry*. **130** 103469. doi:10.1016/j.compind.2021.103469.
8. ↑ Negri, Elisa; Fumagalli, Luca; Macchi, Marco (2017). "A Review of the Roles of Digital Twin in CPS-based Production Systems". *Procedia Manufacturing*. **11**: 939–948. doi:10.1016/j.promfg.2017.07.198. hdl:11311/1049863.
9. 1 2 Allen, B. Danette (3 November 2021). "Digital Twins and Living Models at NASA". Retrieved October 19, 2026.
10. ↑ Gelernter, David (1991). *Mirror Worlds*. doi:10.1093/oso/9780195068122.001.0001. ISBN 978-0-19-506812-2.<sup>\[*page needed*\]</sup>
11. ↑ "Siemens and General Electric gear up for the internet of things". *The Economist*. 3 December 2016. That technology allows manufacturers to create what David Gelernter, a pioneering computer scientist at Yale University, over two decades ago imagined as 'mirror worlds'.
12. ↑ Grieves, Michael; Vickers, John (2017). *Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems*. Springer International Publishing. pp. 85–113. doi:10.1007/978-3-319-38756-7\_4. ISBN 978-3-319-38754-3. Retrieved 19 October 2026 – via Transdisciplinary Perspectives on Complex Systems: New Findings and Approaches.
13. ↑ Grieves, Michael (31 December 2024). "Intelligent digital twins and the development and management of complex systems: \[version 1; peer review: 4 approved\]". Taylor & Francis. p. 8. doi:10.12688/digitaltwin.17574.1. `{{cite web}}`: Missing or empty `|url=` (help)
14. ↑ Linturi, Risto; Koivunen, Marja-Riitta; Sulkanen, Jari (2000). "Helsinki Arena 2000 - Augmenting a real city to a virtual one". *Digital Cities: Technologies, Experiences, and Future Perspectives*. Lecture Notes in Computer Science. Vol. 1765. Springer. pp. 83–96. doi:10.1007/3-540-46422-0\_8. ISBN 978-3-540-67265-4.
15. ↑ Ishida, Toru (2002). "Digital City Kyoto". *Communications of the ACM*. **45** (7): 76–81. doi:10.1145/514236.514238.
16. ↑ "Digital Engineering - SEBoK". *www.sebokwiki.org*. Retrieved 2022-12-12.
17. ↑ "US DoD Digital Engineering Working Group". June 2018. Retrieved 11 Dec 2022.
18. ↑ Grieves, Michael; Vickers, John (2017). "Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems". *Transdisciplinary Perspectives on Complex Systems*. pp. 85–113. doi:10.1007/978-3-319-38756-7\_4. ISBN 978-3-319-38754-3.
19. ↑ Annoni, Marco; Battisti, Davide; Marchegiani, Beatrice (2026-01-29). "Personalised LLMs and the risks of the digital twin metaphor". *AI & Society*. **41** (5): 5177–5189. doi:10.1007/s00146-026-02875-4. ISSN 0951-5666.
20. ↑ "Sheremetyevo Airport has created its own digital twin and now saves 1 billion rubles a year". *TAdviser.ru*. TAdviser Company Media. 5 July 2024. Retrieved 9 November 2025.
21. 1 2 3 4 Crespi, Drobot & Minerva 2023, p. <sup>\[*page needed*\]</sup>.
22. ↑ Vohra, Manisha, ed. (2022). *Digital Twin Technology*. doi:10.1002/9781119842316. ISBN 978-1-119-84220-0.<sup>\[*page needed*\]</sup>
23. 1 2 3 4 Pal et al. 2022, p. <sup>\[*page needed*\]</sup>.
24. ↑ Sabri, Soheil; Alexandridis, Kostas; Lee, Newton, eds. (2024). *Digital Twin*. doi:10.1007/978-3-031-67778-6. ISBN 978-3-031-67777-9.<sup>\[*page needed*\]</sup>
25. ↑ Kritzinger, Werner; Karner, Matthias; Traar, Georg; Henjes, Jan; Sihn, Wilfried (2018). "Digital Twin in manufacturing: A categorical literature review and classification". *IFAC-PapersOnLine*. **51** (11): 1016–1022. doi:10.1016/j.ifacol.2018.08.474.
26. ↑ Ostaševičius, Vytautas (2022). *Digital Twins in Manufacturing*. Springer Series in Advanced Manufacturing. doi:10.1007/978-3-030-98275-1. ISBN 978-3-030-98274-4.<sup>\[*page needed*\]</sup>
27. 1 2 Jebelli et al. 2024, p. <sup>\[*page needed*\]</sup>.
28. ↑ Mousavi, Yalda; Gharineiat, Zahra; Karimi, Armin Agha; McDougall, Kevin; Rossi, Adriana; Gonizzi Barsanti, Sara (2024-09-10). "Digital Twin Technology in Built Environment: A Review of Applications, Capabilities and Challenges". *Smart Cities*. **7** (5): 2594–2615. doi:10.3390/smartcities7050101. ISSN 2624-6511.
29. ↑ Huzzat, Annysha; Anpalagan, Alagan; Khwaja, Ahmed S.; Woungang, Isaac; Alnoman, Ali A.; Pillai, Anju S. (2025). "A comprehensive review of Digital Twin technologies in smart cities". *Digital Engineering*. **4** 100040. doi:10.1016/j.dte.2025.100040.
30. ↑ NSW, Digital (25 February 2020). "NSW Digital Twin". Retrieved 25 February 2020.
31. ↑ "India's 9 Defence Tech Startups Giving Boost To Indian Armed Forces". *IndianWeb2*. April 2017. Retrieved July 12, 2026.
32. ↑ Lock, Oliver; Bednarz, Tomasz; Pettit, Christopher (2019). "HoloCity – exploring the use of augmented reality cityscapes for collaborative understanding of high-volume urban sensor data". *Proceedings of the 17th International Conference on Virtual-Reality Continuum and its Applications in Industry*. pp. 1–2. doi:10.1145/3359997.3365734. ISBN 978-1-4503-7002-8.
33. ↑ "The Gemini Principles" (PDF). *www.cdbb.cam.ac.uk*. Centre for Digital Built Britain. 2018. Retrieved 2020-01-01.
34. ↑ Walker, Andy (7 December 2018). "Principles to guide development of national digital twin released". *Infrastructure Intelligence*. Retrieved 1 June 2020.
35. ↑ Ingram, Jonathan (2020). *Understanding BIM*. pp. 128–132. doi:10.1201/9780429282300. ISBN 978-0-429-28230-0.<sup>\[*page needed*\]</sup>
36. ↑ Hosamo, Haidar Hosamo; Nielsen, Henrik Kofoed; Alnmr, Ammar Njeeb; Svennevig, Paul Ragnar; Svidt, Kjeld (2022-11-09). "A review of the Digital Twin technology for fault detection in buildings". *Frontiers in Built Environment*. **8** 1013196. doi:10.3389/fbuil.2022.1013196. ISSN 2297-3362.
37. ↑ Zhang, Tianxiong; Grzelak, Dominik; Zhao, Wanqi; Islam, Md Ashraful; Fricke, Hartmut; Aßmann, Uwe (2025-05-24). "A Review on the Construction, Modeling, and Consistency of Digital Twins for Advanced Air Mobility Applications". *Drones*. **9** (6): 394. Bibcode:2025Drone...9..394Z. doi:10.3390/drones9060394. ISSN 2504-446X.
38. 1 2 3 4 Bruynseels, Koen; Santoni de Sio, Filippo; van den Hoven, Jeroen (13 February 2018). "Digital Twins in Health Care: Ethical Implications of an Emerging Engineering Paradigm". *Frontiers in Genetics*. **9** 31. doi:10.3389/fgene.2018.00031. PMC 5816748. PMID 29487613.
39. 1 2 Tao, Fei; Cheng, Jiangfeng; Qi, Qinglin; Zhang, Meng; Zhang, He; Sui, Fangyuan (February 2018). "Digital twin-driven product design, manufacturing and service with big data". *The International Journal of Advanced Manufacturing Technology*. **94** (9–12): 3563–3576. doi:10.1007/s00170-017-0233-1.
40. ↑ "Digital health". *OECD*. Retrieved 2025-09-20.
41. ↑ Katsoulakis, Evangelia; Wang, Qi; Wu, Huanmei; Shahriyari, Leili; Fletcher, Richard; Liu, Jinwei; Achenie, Luke; Liu, Hongfang; Jackson, Pamela; Xiao, Ying; Syeda-Mahmood, Tanveer; Tuli, Richard; Deng, Jun (22 March 2024). "Digital twins for health: a scoping review". *npj Digital Medicine*. **7** (1) 77. doi:10.1038/s41746-024-01073-0. PMC 10960047. PMID 38519626.
42. ↑ Yoo, Youngjin; Boland, Richard; Lyytinen, Kalle; Majchrzak, Ann (September–October 2012). "Organizing for innovation in the digitized world". *Organization Science*. **23** (5): 1398–1408. doi:10.1287/orsc.1120.0771. JSTOR 23252314.
43. ↑ Cearley, David W.; Burker, Brian; Searle, Samantha; Walker, Mike J. (3 October 2017). "The top 10 strategic technology trends for 2013" (PDF). *Gartner Trends 2018*: 1–24.
44. ↑ Wang, Ziran; Gupta, Rohit; Han, Kyungtae; Wang, Haoxin; Ganlath, Akila; Ammar, Nejib; Tiwari, Prashant (September 2022). "Mobility Digital Twin: Concept, Architecture, Case Study, and Future Challenges". *IEEE Internet of Things Journal*. **9** (18): 17452–17467. Bibcode:2022IITJ....917452W. doi:10.1109/JIOT.2022.3156028.
45. ↑ Kumari, Namita; Sharma, Ankush; Tran, Binh; Chilamkurti, Naveen; Alahakoon, Damminda (21 July 2023). "A Comprehensive Review of Digital Twin Technology for Grid-Connected Microgrid Systems: State of the Art, Potential and Challenges Faced". *Energies*. **16** (14): 5525. doi:10.3390/en16145525.
46. ↑ Kandemir, Ege (2024). "Predictive digital twin for wind energy systems: a literature review". *Energy Informatics*. **7** 68. doi:10.1186/s42162-024-00373-9.
47. ↑ Ardebili, Ali Aghazadeh (2024). "Digital Twins of Smart Energy Systems: Enablers, Design, Management and Challenges". *Energy Informatics*. doi:10.1186/s42162-024-00385-5.
48. ↑ Deakin, Matthew (2024). "Smart Energy Network Digital Twins: Findings from a UK-Based Demonstrator Project". *International Journal of Electrical Power and Energy Systems*. **162** 110302. arXiv:2311.11997. Bibcode:2024IJEPE.16210302D. doi:10.1016/j.ijepes.2024.110302.
49. ↑ Gaffney, C; Croucher, K; Bates, CR; Booker, O; Dunn, R; Evans, A; Ichumbaki, EB; Moore, J; Ogden, J; Ritchings, J; Simpson, S; Sparrow, T; Walker, A; Wilson, AS (2025). "Digital Twins at the City and Town Scale: Europe and Beyond". *Internet Archaeology* (70). doi:10.11141/ia.70.5.

## Sources

\[edit\]
- Crespi, Noel; Drobot, Adam T.; Minerva, Roberto, eds. (2023). *The Digital Twin*. doi:10.1007/978-3-031-21343-4. ISBN 978-3-031-21342-7.
- Jebelli, Houtan; Asadi, Somayeh; Mutis, Ivan; Liu, Rui; Cheng, Jack, eds. (2024). *Digital Twins in Construction and the Built Environment*. doi:10.1061/9780784485606. ISBN 978-0-7844-8560-6.
- Pal, Surjya Kanta; Mishra, Debasish; Pal, Arpan; Dutta, Samik; Chakravarty, Debashish; Pal, Srikanta (2022). *Digital Twin – Fundamental Concepts to Applications in Advanced Manufacturing*. Springer Series in Advanced Manufacturing. doi:10.1007/978-3-030-81815-9. ISBN 978-3-030-81814-2.

## Further reading

\[edit\]
- Herlyn, Wilmjakob; Zadek, Hartmut; Kersten, Wolfgang; Blecker, Thorsten; Ringle, Christian M. (23 September 2020). Kersten, Wolfgang; Blecker, Thorsten; Ringle, Christian M. (eds.). Mastering the supply chain by a concept of a ditigal control-twin (Report). TUHH Universitätsbibliothek. doi:10.15480/882.3120. hdl:11420/8010.
- Kumari, Namita; Sharma, Ankush; Tran, Binh; Chilamkurti, Naveen; Alahakoon, Damminda (2023). "A Comprehensive Review of Digital Twin Technology for Grid-Connected Microgrid Systems: State of the Art, Potential and Challenges Faced". *Energies*. **16** (14): 5525. doi:10.3390/en16145525.
- Sjarov, Martin; Lechler, Tobias; Fuchs, Jonathan; Brossog, Matthias; Selmaier, Andreas; Faltus, Florian; Donhauser, Toni; Franke, Jorg (2020). "The Digital Twin Concept in Industry – A Review and Systematization". *2020 25th IEEE International Conference on Emerging Technologies and Factory Automation (ETFA)*. pp. 1789–1796. doi:10.1109/ETFA46521.2020.9212089. ISBN 978-1-7281-8956-7.
- VanDerHorn, Eric; Mahadevan, Sankaran (June 2021). "Digital Twin: Generalization, characterization and implementation". *Decision Support Systems*. **145** 113524. doi:10.1016/j.dss.2021.113524.
- Wright, Louise; Davidson, Stuart (December 2020). "How to tell the difference between a model and a digital twin". *Advanced Modeling and Simulation in Engineering Sciences*. **7** (1) 13. doi:10.1186/s40323-020-00147-4.
- ISO/DIS 23247-1 Automation systems and integration — Digital Twin framework for manufacturing — Part 1: Overview and general principles
