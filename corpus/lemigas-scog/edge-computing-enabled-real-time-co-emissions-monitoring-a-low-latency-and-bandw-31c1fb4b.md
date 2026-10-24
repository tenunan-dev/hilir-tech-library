---
source_id: "lemigas-scog"
title: "Edge Computing Enabled Real Time CO Emissions Monitoring A Low Latency and Bandwidth Efficient Architecture fo"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2020"
retrieved_at: "2026-10-24T14:30:17+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "31c1fb4bf0209ed6fd46693441b57e969262c1df69d96c94a74d4a5c7030a49d"
collected: "manual"
---

# Edge Computing Enabled Real Time CO Emissions Monitoring A Low Latency and Bandwidth Efficient Architecture fo

DOI org/10.29017/scog.v49i2.2020 I 155 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Edge Computing–Enabled Real-Time CO2 Emissions Monitoring:  
A Low-Latency and Bandwidth-Efficient Architecture 
for Oil and Gas Sector 
Suka Handaja and Bambang Yudho Suranta 
ABSTRACT - The oil and gas industry is facing increasing pressure to reduce carbon dioxide (CO ₂) 
emissions while maintaining operational efficiency and regulatory compliance. However, conventional 
cloud-based emissions monitoring systems often suffer from latency, bandwidth limitations, and reduced 
reliability in remote operational environments. This study aims to explore the role and implementation of 
edge computing as an enabling technology for real -time CO₂ emissions monitoring in oil and gas facilities. 
The architecture of the proposed system integrates the Internet of Things (IoT) gas sensors, local data 
processing units, and cloud platforms for long -term analytics and reporting. The system is designed to 
process the emissions data closer to the source with the aim of significantly reducing latency, improving 
measurement reliability, and enhancing responsiveness to abnormal emissions events. The performance was 
subsequently evaluated through a distributed monitoring test scenario that simulated multiple emissions 
monitoring points under intermittent network connectivity conditions often experienced in remote oil and 
gas operations. The focus was on key performance indicators including data latency, bandwidth utilization, 
and system availability. The results showed that the edge -enabled architecture reduced average data latency 
from approximately 3.8 s to 0.9 s and data transmission volume by an estimated 79% through local 
preprocessing while maintaining monitoring availability above 96% during network disruptions. The trend 
reflected the ability of edge computing to provide a scalable and robust solution for continuous CO ₂ 
emissions monitoring, particularly in geographically distributed and harsh operational environments often 
associated with oil and gas operations.  
Keywords: edge computing, CO₂ emissions monitoring, oil and gas industry, internet of things (IoT), Real-
time monitoring, environmental sustainability, ESG compliance, digital transformation. 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 155 - 171 
Politeknik Energi dan Mineral Akamigas 
Gajah Mada Street No. 38 Cepu, Blora, Indonesia. 
Corresponding author: Suka Handaja (suka.budi@esdm.go.id) 
Manuscript received:  February 26th, 2026; Revised: March 13th, 2026 
Approved:  March 16 th, 2026; Available online: June 04th, 2026; Published: June 04th, 2026.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
156 I DOI org/10.29017/scog.v49i2.2020 
How to cite this article: 
Suka Handaja and Bambang Yudho Suranta, 2026, Edge Computing–Enabled Real-Time CO₂ 
Emissions Monitoring for Enhanced Environmental Performance in the Oil and Gas Industry , 
Scientific Contributions Oil and Gas, 49 (2) pp. 155-171. DOI org/10.29017/scog.v49i2.2020. 
Copyright © 2026 by Authors, Published by LEMIGAS 
INTRODUCTION 
The oil and gas industry is currently a 
significant source of anthropogenic carbon dioxide 
(CO₂) emissions which contributes substantially to 
climate change. The phenomenon presents 
challenges for the commitments of the industry to 
sustainable development and environmental 
performance. Environmental monitoring of CO ₂ 
emissions is very important in sustainability 
assessments and industry decarbonization 
strategies. The mitigation and monitoring of CO ₂ 
in the oil and gas industry have also been 
considered in Carbon Capture, Utilization, and 
Storage (CCUS) strategies where emissions 
monitoring and storage are integrated into 
operational workflows (Sugihardjo 2022). 
Moreover, digitalization has been associated with 
improved environmental performance because it 
enables better measurement, transparency, and 
optimization of energy systems (Diófási -Kovács & 
Judit 2023). Digital integration in firms was also 
correlated with reductions in emissions and 
enhanced innovation (Quttainah & Ayadi 2024). 
A key enabler of industry decarbonization is 
advanced emissions monitoring that can provide 
accurate real -time data for operational decision -
making, regulatory reporting, as well as 
environmental, social, and governance (ESG) 
compliance. However, conventional monitoring 
systems that depend on centralized cloud 
processing face specific challenges such as high 
latency, bandwidth pressures, and vulnerability in 
remote or harsh industrial environments.  
These challenges are capable of hindering 
consistent data collection and system reliability 
(Roostaei et al., 2023). The situation leads to the 
introduction of edge computing which processes 
data near the source rather than in a remote cloud 
to address the limitations by reducing latency, 
improving reliability, and enabling local analytics 
and anomaly detection (Roostaei et al., 2023). The 
applications of the system in environmental 
monitoring (Yadav et al., 2025) and industrial CO ₂ 
tracking (Christensen 2024) show the potential to 
transform the management and utilization of data 
in real-world scenarios.  
Figure 1 shows an integrated Edge –IoT–Cloud 
architecture for real -time CO ₂ emissions 
monitoring in oil and gas operations. The 
distributed IoT sensors continuously capture and 
process high -resolution emissions data at critical 
sources such as the flaring systems, combustion 
units, and vent stacks.  
Moreover, edge computing nodes introduce 
localized intelligence by performing real -time data 
preprocessing, anomaly detection, and preliminary 
emissions analytics to significantly reduce latency, 
bandwidth dependence, and vulnerability to 
network disruptions common in remote and 
offshore facilities. The aggregated and validated 
data at the cloud level also support long -term 
analytics, regulatory reporting, ESG disclosure, 
and strategic decision -making to enable a 
balance between operational emissions control, 
regulatory transparency, and broader energy 
transition objectives. The limitations of 
conventional cloud -centric emissions monitoring 
motivate this study to introduce a novel system 
that positions edge computing as a strategic 
enabler of sustainable energy governance rather 
than a purely technical optimization layer.  
The conceptual presentation in Figure 2 
shows that the proposed framework explicitly 
connects real -time edge -level CO ₂ emissions 
intelligence with broader energy transition 
objectives and the United Nations sustainable

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 157 
 
Figure 1. Edge-IoT-Cloud architecture for Co2 emissions monitoring in the oil and gas industry. 
development goals (SDGs) as a reflection of the 
relevance to global sustainability efforts . Figure 
2 illustrates how an edge CO ₂ monitoring system 
provides real -time emissions data to improve 
operational performance in the oil and gas industry. 
The collected data supports the development of 
sustainable energy systems, cleaner industrial 
processes, and enhanced climate resilience and 
adaptation. As a result, the proposed system 
contributes directly to the achievement of SDG 7 
(Affordable and Clean Energy), SDG 9 (Industry, 
Innovation and Infrastructure), and SDG 13 
(Climate Action). 
The novelty of this study is in the development 
and evaluation of an integrated edge –IoT–cloud 
architecture specifically designed for real-time CO₂ 
emissions monitoring in oil and gas operations. 
Previous studies primarily emphasize either 
sensing technologies or cloud -based analytics but 
the current focus is on the system -level integration 
of distributed sensing, localized edge analytics, and 
cloud-based reporting infrastructures. The 
integration of real -time emissions data into digital 
analytics platforms was related to improved 
governance and sustainability outcomes (Samuel et 
al., 2025). The proposed system is also evaluated 
using quantitative performance metrics relevant to 
industrial monitoring systems such as data latency, 
bandwidth utilization, and monitoring reliability 
under simulated network disruption scenarios. 
The trend shows that the objectives of this study 
are threefold including to (1) design a scalable 
Edge–IoT–Cloud architecture for real -time CO ₂ 
emissions monitoring in oil and gas facilities, (2) 
evaluate the performance using key system 
performance indicators such as latency, bandwidth 
efficiency, and system availability, and (3) assess 
the operational benefits of localized edge analytics 
for improving the responsiveness and reliability of 
emissions monitoring systems in distributed 
industrial environments. 
 The objectives serve as the basis for the 
formulation of the study, which examines how an 
edge-enabled monitoring architecture improves the 
performance of real -time CO ₂ emissions 
monitoring compared with conventional cloud -
centric systems. The study further evaluates the 
extent to which edge computing reduces data 
latency and network bandwidth utilization in 
distributed emissions monitoring networks. 
Additionally, it analyzes how localized edge -level 
processing influences the reliability and 
responsiveness of emissions monitoring systems in 
remote oil and gas operational environments.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
158 I DOI org/10.29017/scog.v49i2.2020 
 
Figure 2. Edge computing-enabled CO2 monitoring: advancing SDGs & energy. 
Recent studies emphasized the role of digital 
innovation in bridging emissions monitoring with 
broader environmental performance and 
sustainability goals. The transition of industries 
toward more sustainable operations leads to the 
increasing recognition of real -time monitoring 
technologies as core components of environmental 
performance management systems. Therefore, the 
convergence of IoT, edge computing, and AI 
enhances emissions detection and reporting as well 
as facilitates the integration of performance data 
into sustainability metrics, environmental strategy 
formulation, and corporate ESG disclosure 
processes. The integration underscores the 
importance of digital -based emissions monitoring 
as an enabler of transparent performance 
evaluations and evidence -based environmental 
governance (Garcia et al., 2025). 
Previous studies primarily emphasized 
technological performance improvements but the 
current focus was on the ability of edge computing 
to function as a translational layer between 
industrial operations and climate policy 
implementation particularly in hard -to-abate 
sectors such as oil and gas. This is due to the fact 
that greenhouse gas emissions particularly CO ₂ are 
a principal concern in industry. Therefore, there is 
a need for mitigation strategies that include carbon 
capture and broader emissions reduction 
frameworks (Ismukurnianto 2008) and the mapping 
of CO ₂ source–sink dynamics relevant to carbon 
storage planning (Al Hakim et al., 2025).  
The efforts to mitigate CO ₂ emissions in oil and 
gas operations extend beyond monitoring to 
include source -sink matching and sequestration 
strategies such as screening CO ₂ EOR projects in 
depleted reservoirs to balance emissions abatement 
and enhanced oil recovery (Pasarai et al., 2010). 
The integrated method in the proposed system 
connects operational decarbonization efforts with 
SDG-oriented sustainability targets to reinforce the 
role of digital infrastructure as a cornerstone of the 
energy transition. 
 
METHODOLOGY 
System architecture 
The proposed system architecture adopted a 
layered design comprising three interconnected 
levels including the sensing, edge processing, and 
cloud integration layers as presented in Figure 3. 
The sensing layer consisted of distributed CO ₂ 
sensors strategically deployed across critical oil 
and gas process units including flaring systems, 
combustion equipment, compressors, and vent 
stacks. These sensors continuously measured CO ₂ 
concentration along with supporting process 
variables such as flow rate, temperature, and 
pressure. Moreover, the high -frequency data

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 159 
 
acquisition at the emissions source ensured a 
granular and accurate representation of real 
operational conditions. This was necessary to 
enable reliable quantification of emissions across 
both steady-state and transient process scenarios. 
The sensing layer consisted of four distributed 
CO₂ monitoring nodes deployed across 
representative emissions sources in oil and gas 
process units including flare stacks, combustion 
heaters, compressor exhaust systems, and vent 
stacks. Each monitoring node was equipped with 
an industrial CO ₂ sensor capable of measuring gas 
concentration in the range of 350 –10,000 ppm 
with a measurement accuracy of ±2%. The 
supporting process variables such as gas flow rate, 
temperature, and pressure were recorded in 
addition to CO₂ concentration to provide contextual 
information for emissions analysis. Sensor data 
were also sampled at a frequency of 1 Hz to enable 
high-resolution monitoring of both steady-state and 
transient emissions conditions. 
The edge processing layer served as the primary 
computational component of the system. Each 
sensor was connected to an edge device equipped 
with a 1.0 GHz quad -core processor, 512 MB 
RAM, and local storage capacity of 64 GB. These 
edge devices were installed in proximity to the 
sensing infrastructure to enable low -latency data 
processing. The incoming sensor data streams at 
the layer experienced preprocessing operations 
such as noise filtering, data validation, and sensor 
drift compensation. Moreover, lightweight anomaly 
detection algorithms developed in line with rule -
based thresholds and simplified statistical models 
were implemented to identify abnormal emissions 
patterns or equipment malfunctions. 
The cloud integration layer provided the 
centralized services for long -term data storage, 
advanced analytics, and policy -oriented reporting. 
The edge nodes transferred concise data 
summaries, event flags, and validated datasets to 
cloud servers to be aggregated and integrated into 
Figure 3. Proposed system architecture.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
160 I DOI org/10.29017/scog.v49i2.2020 
 
enterprise-level systems rather than transmitting 
raw sensor data. This cloud -based layer supported 
emissions inventory management, ESG and 
regulatory reporting, as well as historical trend 
analysis in line with environmental policy 
frameworks. Furthermore, the separation of real-time 
operational intelligence at the edge and strategic 
analytics in the cloud established a scalable, resilient, 
and energy-efficient monitoring architecture which 
enabled continuous emissions oversight while 
supporting sustainability governance and long -term 
decarbonization strategies in the oil and gas industry. 
The effectiveness of the proposed architecture was 
evaluated through an experimental monitoring system 
deployed in a simulated oil and gas operational 
environment to represent distributed emissions 
sources. The test configuration consisted of four CO₂ 
sensor nodes, four corresponding edge computing 
devices, and one centralized cloud server.  
The monitoring system operated continuously 
over a seven -day observation period during which 
both normal operational and simulated abnormal 
emissions events were generated. The network 
conditions were varied to replicate realistic 
industrial scenarios. These included stable 
connectivity conditions for onshore facilities with 
reliable network access and intermittent 
connectivity for remote or offshore installations 
with periodic network disruptions. Sensor data 
were sampled at 1-second intervals to produce high
-resolution time -series data for analysis. The 
monitoring system generated both routine and 
controlled anomaly events such as temporary CO ₂ 
concentration spikes exceeding predefined 
thresholds during the test. 
Data processing and analysis 
Edge computing was observed to have 
substantial potential for enhancing environmental 
monitoring systems by enabling localized data 
processing and real -time analytics. However, 
existing literature has only focused on the 
limitations of current edge analytics architectures 
in addressing efficient resource allocation under 
constrained and heterogeneous environments 
(Nayak et al., 2022). The need for deeper 
investigation into trade -offs between quality 
attributes such as latency, resource utilization, and 
data veracity was also reported (Ashouri et al.,  
2021). Furthermore, the complexity of resource 
allocation strategies across the edge -cloud 
continuum continues to pose challenges in terms of 
balancing latency, cost, and throughput in IoT 
deployments (Dankolo et al., 2025). 
The benefits of edge computing integration 
were quantified through a comparative 
performance analysis conducted between two 
monitoring architectures, as illustrated in figure 4.   
First, Cloud -Centric Architecture was used as the 
baseline system with raw sensor data streams 
transmitted directly from the sensing layer to the 
cloud server for processing. All preprocessing, 
anomaly detection, and analytics tasks were 
performed centrally in the cloud. Second, Edge -
Enabled Architecture was the proposed system 
Figure 4. Policy-oriented data processing.

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 161 
where the preprocessing, data reduction, and 
anomaly detection were performed locally at the 
edge nodes. Only validated data summaries and 
event notifications were transmitted to the cloud 
platform. Both architectures were evaluated using the 
same sensor data streams, network conditions, and 
operational scenarios to ensure fair comparison. The 
performance differences were measured using several 
key performance indicators (KPIs) including data 
latency, bandwidth utilization, system reliability, and 
event detection responsiveness.  
Latency was calculated by comparing timestamps 
between sensor data acquisition and alert generation. 
Bandwidth utilization was evaluated by measuring 
the total volume of transmitted data between field 
devices and the cloud platform. System reliability 
was also assessed based on monitoring uptime 
during simulated network disruptions while event 
detection responsiveness was evaluated by 
measuring the time required to identify emissions 
threshold exceedances.  
The evaluation framework enabled quantitative 
assessment of how edge -enabled processing 
improved monitoring performance compared with 
conventional cloud-based architectures. The results 
provided empirical evidence of the operational 
advantages of edge computing in supporting real -
time emissions monitoring, improving system 
resilience, and enabling scalable deployment of 
monitoring infrastructures in geographically 
distributed oil and gas facilities. 
Performance evaluation 
The performance of the proposed edge -enabled 
CO₂ emissions monitoring system was evaluated 
using a set of KPIs that reflected both technical 
efficiency and regulatory relevance. The KPIs 
included data latency, system reliability, bandwidth 
utilization, and responsiveness to emissions events. 
Data latency was defined as the elapsed time 
between emissions occurrence at the sensing point 
and alert generation or data availability for 
reporting and was considered a critical factor for 
timely mitigation and regulatory compliance. 
Moreover, system reliability was assessed through 
the continuity of monitoring functions under 
varying network conditions including intermittent 
connectivity scenarios common in remote and 
offshore oil and gas operations.  
Bandwidth utilization was evaluated by 
quantifying the reduction in transmitted data 
volume achieved through edge -level preprocessing 
and aggregation. Meanwhile, responsiveness to 
emissions events was measured through the ability 
of the system to promptly detect and flag 
regulatory exceedances and operational anomalies 
in line with MRV requirements. The benefits of 
edge computing integration were quantified 
through a comparative performance analysis with a 
 KPI Definition Evaluation Metric Measurement Method Policy/Operational Relevance  
 
Data Latency 
Time delay between 
emissions occurrence and 
data availability for 
alerting or reporting 
Latency 
(seconds) 
Timestamp 
comparison 
between sensor 
data acquisition 
and alert 
generation/cloud 
receipt 
Enables timely 
mitigation actions and 
rapid response to 
regulatory 
exceedances 
 
 
System 
Reliability 
Ability of the monitoring 
system to operate 
continuously under 
varying network 
conditions 
System uptime 
(%) 
Ratio of successful 
monitoring 
duration to total 
observation period 
Ensures continuous 
MRV compliance and 
data availability for 
audits 
 
 
Bandwidth 
Utilization 
Volume of data 
transmitted from field 
devices to cloud 
infrastructure 
Data 
transmission 
volume 
(MB/day) 
Comparison of 
transmitted data 
size with and 
without edge 
preprocessing 
Reduces 
communication costs 
and supports scalable 
deployment in remote 
facilities 
 
 
Table 1. Key performance indicators (KPIs) and evaluation metrics for edge-enabled CO₂                                                      
emissions monitoring system.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
162 I DOI org/10.29017/scog.v49i2.2020 
conventional cloud -only monitoring architecture 
where raw sensor data were continuously 
transmitted to centralized servers for processing. 
Both architectures were evaluated under identical 
operational and network conditions to ensure a fair 
comparison. The performance improvements were 
expressed in terms of percentage reductions in data 
latency and bandwidth consumption as well as 
enhanced event detection responsiveness. This 
comparative evaluation framework provided 
empirical evidence of the advantages of edge -
enabled monitoring in supporting real -time 
emissions oversight, strengthening compliance 
with environmental regulations, and enhancing the 
operational feasibility of large -scale emissions 
monitoring systems in the oil and gas industry. 
 
RESULT AND DISCUSSION 
Performance evaluation 
• Latency Performance Comparison 
Latency is a critical metric for real -time 
emissions monitoring because delayed data 
processing can prevent timely detection of 
abnormal events. Figure 5(a) presents the 
comparison between the conventional cloud-centric 
monitoring architecture and the proposed edge -
enabled system. 
The results showed that the average end -to-end 
latency in the cloud -only architecture reached 
approximately 3.8 seconds primarily due to 
continuous transmission of raw sensor data to the 
cloud server and centralized processing delays. 
Meanwhile, the edge-enabled architecture achieved 
an average of 0.9 seconds which represented a 
reduction of approximately 76%. 
The improvement was primarily attributed to 
local preprocessing and anomaly detection 
performed directly at the edge nodes. The 
processing of the data near the sensing point 
allowed the system to eliminate the need to 
transmit large volumes of raw data before analysis. 
Subsequently, the reduced latency significantly 
enhanced the ability of the system to detect 
abnormal emissions events in near real -time which 
was particularly important for operational safety 
and emissions control in oil and gas facilities. 
• Bandwidth Utilization and Data Reduction 
Bandwidth consumption is another major 
challenge in large -scale emissions monitoring 
systems particularly in geographically distributed 
facilities where network capacity is probably 
limited. Figure 5(b) shows the total daily data 
transmission volume for both monitoring 
architectures. 
The experimental results reflected that the cloud
-centric system transmitted approximately 520 MB/
day of raw sensor data. Meanwhile, the edge -
enabled architecture reduced data transmission to 
approximately 110 MB/day which represented a 
79% reduction. This was achieved through several 
edge-level data processing mechanisms including 
temporal aggregation, noise filtering, and event -
based reporting. The edge nodes transmitted only 
validated summaries and anomaly alerts to the 
cloud rather than continuously transferring raw 
time-series data. Therefore, the network load 
was significantly reduced without compromising 
the availability of critical emissions information. 
The reduced bandwidth requirement enabled 
more scalable deployment of emissions 
monitoring systems across multiple facilities 
particularly in offshore installations or remote 
production sites where communication 
infrastructure could be constrained . 
• System Reliability Under Network Disruptions 
Monitoring system reliability is particularly 
important in oil and gas operations where network 
connectivity can be unstable due to environmental 
conditions or infrastructure limitations. The system 
robustness was evaluated by conducting 
experiments under both stable network conditions 
and intermittent connectivity scenarios. 
Figure 5(c) compares system uptime between 
the cloud -centric and edge -enabled architectures. 
Both systems achieved similar performance levels 
under stable network conditions with uptime 
exceeding 99%. However, pronounced differences 
were observed under intermittent network 
conditions. The cloud-centric system experienced a 
significant reliability drop to approximately 82% 
uptime due to the disruption of the monitoring 
functionality whenever network connectivity to the

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 163 
 
Figure 5. (a). Average data latency comparison for edge vs Cloud; (b). Average data reduction comparison for edge vs 
cloud; (c). average system reliability under network disruption comparison for edge vs cloud. 
 
a) 
 
b) 
c)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
164 I DOI org/10.29017/scog.v49i2.2020 
 
KPI Category Metric Definition Edge-Enabled System (Reported Range) Cloud-Only Baseline Evidence from Literature 
 
 
Data Latency 
End-to-end delay 
from sensor 
acquisition to 
actionable output 
~490 µs – 2.6 s ~560 µs – 14.8 s 
Edge computing 
reduced latency by 
~13% in laboratory 
pilots and by up to 
~80% in real urban 
field deployments 
(Malhotra, 2025) 
 
 
Latency 
Reduction 
Relative 
improvement 
compared to cloud-
centric architecture 
~13% (lab) to >80% 
(field) Reference 
Showed consistently 
across IoTEC pilots 
and multi-node air 
quality monitoring 
systems (Roostaei, et 
al., 2023) 
 
 
Bandwidth 
Utilization 
Reduction in uplink 
data transmission 
volume 
~50–62% reduction 100% raw data transmission 
Local preprocessing 
and aggregation at the 
edge significantly 
reduced network load 
(Roostaei, et al., 2023) 
 
 
Data Accuracy 
Agreement with 
reference 
measurements 
≈95% accuracy Comparable but with higher noise 
Field deployments 
confirmed high data 
fidelity when edge-
based validation and 
filtering were applied 
(Siddiqui, Rabbani, 
Akhtar, Suneel, & 
Naik, 2025) 
 
 
Detection 
Performance 
Error reduction in 
pollutant/emissions 
estimation 
MAE reduced by ~63% 
(PM₂.₅ proxy) 
Higher estimation 
error 
Edge analytics 
improved detection 
accuracy and reduced 
estimation error in 
real-time monitoring 
scenarios (Malhotra, 
2025) 
 
 
System 
Responsiveness 
Time to trigger alerts 
relative to regulatory 
thresholds 
<500 ms Seconds to minutes 
Edge–blockchain IoT 
systems achieved sub-
second 
responsiveness, 
suitable for regulatory 
alarm thresholds 
(Alabdulkreem, et al., 
2025) 
 
 
Operational 
Resilience 
Ability to operate 
during network 
disruption 
Maintained local 
monitoring 
Degraded or 
unavailable 
Edge nodes ensured 
continued MRV 
functionality under 
intermittent 
connectivity 
conditions (Yadav, et 
al., 2025) 
 
 
Table 2. KPIs for edge-enabled CO₂ emissions monitoring systems.

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 165 
SDG SDG Target 
Relevant 
KPI/Technical 
Outcome 
Contribution of Edge-
Enabled Monitoring 
Policy and Energy 
Transition Relevance 
SDG 9 Industry, 
Innovation and 
Infrastructure 
9.4: Upgrade 
infrastructure and 
retrofit industries for 
sustainability 
Latency reduction (13–
80%), bandwidth 
reduction (50–62%) 
Enables digital upgrading 
of existing oil and gas 
infrastructure with 
minimal communication 
and energy overhead 
Supports modernization of 
legacy energy assets during 
the transition period without 
requiring full asset 
replacement 
SDG 12 
Responsible 
Consumption and 
Production 
12.4: Environmentally 
sound management of 
chemicals and 
emissions 
Detection accuracy 
(~95%), improved 
anomaly detection 
Provides continuous and 
accurate emissions 
monitoring, reducing 
unreported or delayed 
emissions events 
Strengthens compliance 
mechanisms and supports 
responsible industrial 
operations 
SDG 13 Climate 
Action 
13.2: Integrate climate 
measures into policies 
and planning 
Sub-second system 
responsiveness (<500 
ms), real-time alerts 
Enables rapid operational 
response when emissions 
exceed regulatory 
thresholds 
Facilitates proactive climate 
mitigation actions rather 
than reactive reporting 
SDG 7 Affordable 
and Clean Energy 
7.3: Improve energy 
efficiency 
Reduced data 
transmission and 
computational load 
Lowers digital energy 
consumption associated 
with emissions monitoring 
systems 
Balance digitalization with 
energy efficiency goals in 
the energy sector 
SDG 16 Peace, 
Justice and Strong 
Institutions 
16.6: Effective, 
accountable, and 
transparent institutions 
High data integrity and 
validation at the edge 
Improves credibility and 
transparency of emissions 
data for regulators and 
stakeholders 
Enhance trust in MRV 
systems and emissions 
disclosure frameworks 
SDG 17 
Partnerships for the 
Goals 
17.16: Multi-
stakeholder 
partnerships 
Cloud–edge integration 
for reporting and 
analytics 
Facilitates data sharing 
between operators, 
regulators, and third-party 
auditors 
Supports collaborative 
governance of emissions 
data across institutional 
boundaries 
 
cloud server was lost. Meanwhile, the edge-enabled 
system maintained approximately 95–96% uptime 
because the local edge nodes continued performing 
data processing and anomaly detection even during 
temporary communication failures.  
The capability shows the advantage of 
decentralized monitoring architectures in industrial 
environments where reliable network connectivity 
is not often guaranteed. Moreover, the performance 
evaluation reflects the ability of the proposed edge-
enabled monitoring architecture to consistently 
outperform the conventional cloud -only method 
across all KPIs relevant to emissions MRV. The 
results were in line with the reports of the previous 
studies summarized in Table 2. 
System responsiveness and operational 
resilience further reinforced the suitability of the 
proposed architecture for regulatory and policy -
driven applications. This was because the edge -
based systems consistently achieved sub -second 
alerting capabilities (<500 ms) which enabled rapid 
intervention when emissions exceeded the 
predefined regulatory limits.  
The edge nodes maintained core monitoring and 
alerting functions even during intermittent cloud 
connectivity to ensure the continuity of MRV 
processes in harsh operational environments. The 
results collectively confirmed that edge computing 
provided a robust technological foundation for real-
time CO ₂ emissions monitoring, regulatory 
compliance, and operational decarbonization 
strategies in the oil and gas industry. 
Implications for SDGs and energy transition 
The performance results presented in Section 4. 
A showed that edge -enabled emissions monitoring 
architectures provided measurable and policy -
relevant improvements in latency, data reliability, 
Table 3. Explicit mapping of edge-enabled CO₂ emissions monitoring to SDGs and energy transition objectives.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
166 I DOI org/10.29017/scog.v49i2.2020 
and operational resilience. These technical gains 
have direct implications for the achievement of 
multiple SDGs, particularly 9 on Industry, 
Innovation, and Infrastructure, 12 on Responsible 
Consumption and Production, and 13 on Climate 
Action. The near -real-time detection of CO ₂ 
anomalies allowed the proposed architecture to 
strengthen the operational capacity of oil and gas 
facilities in managing emissions proactively rather 
than reactively. The significant reduction in data 
latency and bandwidth utilization supported the 
digitalization of legacy hydrocarbon assets from an 
energy transition perspective without imposing 
excessive communication or energy overheads. Edge 
computing enabled high -frequency emissions 
monitoring in geographically dispersed and 
infrastructure-constrained environments such as 
offshore platforms and remote gas processing plants.  
This capability is critical during the transitional 
phase toward low -carbon energy systems where 
existing oil and gas infrastructure is required to 
operate with improved environmental performance 
while supporting the gradual integration of cleaner 
energy technologies. Moreover, the economic 
optimization of CCUS implementations including 
CO₂ injection strategies emphasizes the critical 
intersections between monitoring technologies and 
sustainability goals to reinforce the need for robust 
emissions monitoring systems (Iskandar & Musu 
2025). Long-term emissions management strategies 
require understanding CO ₂ storage potential and 
containment reliability in addition to real -time 
monitoring. These were assessed through criteria 
such as caprock quality indices for CO ₂ 
sequestration sites (Destiana et al., 2025). 
The observed improvements in data accuracy 
and detection performance further reinforced the 
role of edge computing in enhancing MRV 
systems. The accurate and timely measurement of 
emissions data reduced uncertainty in corporate 
greenhouse gas inventories and improved 
compliance with international reporting 
frameworks such as nationally determined 
contributions (NDCs) and voluntary ESG 
disclosure standards. In this context, edge -enabled 
monitoring served as a technical upgrade and also 
functioned as an enabling mechanism for 
transparent and credible climate governance within 
the energy sector. 
Another important observation was that the 
resilience of edge -based architectures under 
intermittent connectivity conditions addressed a 
critical barrier to emissions monitoring in 
developing and resource -rich regions. The 
maintenance of local monitoring and alerting 
capabilities even during network disruptions 
allowed edge computing to ensure continuity of 
environmental oversight. This attribute supports 
equitable progress toward SDGs by enabling 
consistent emissions accountability across both 
advanced and remote industrial operations. 
Policy implications 
The results have several important implications 
for policymakers, regulators, and industry 
stakeholders associated with emissions governance 
and energy transition planning. First, the latency 
reduction and sub -second responsiveness of edge -
enabled systems suggested that regulatory 
frameworks could increasingly recognize real -time 
or near-real-time emissions monitoring as a viable 
compliance mechanism.  
This allows regulators to move beyond periodic 
reporting toward continuous compliance models 
particularly for high-risk emissions sources such as 
flaring systems and combustion units. Second, the 
substantial reduction in data transmission 
requirements achieved through edge preprocessing 
has implications for the design of MRV policies in 
remote and offshore environments. This shows the 
need for regulators and standard -setting bodies to 
consider incorporating edge computing architectures 
into technical guidance for emissions monitoring 
particularly where communication bandwidth and 
infrastructure limitations have historically constrained 
compliance. The  recognition can lower 
implementation barriers and promote broader 
adoption of advanced monitoring technologies. 
Third, the improved data accuracy and detection 
performance enabled by edge analytics strengthen 
the credibility of emissions data used for ESG 
reporting and carbon accounting. Policymakers can 
leverage the capability by promoting or mandating 
the use of edge -based validation and anomaly 
detection as part of certified emissions monitoring

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 167 
systems. This is capable of enhancing trust in 
reported emissions data and supporting more robust 
market-based mechanisms such as carbon pricing 
or emissions trading schemes.  
Edge-enabled emissions monitoring is in line 
with policy objectives that emphasize digital 
innovation as a pathway to sustainable industrial 
transformation at a strategic level. The combination 
of engineering performance improvements with 
climate and energy policy goals allows edge 
computing to provide a pragmatic bridge between 
existing fossil -based operations and long -term 
decarbonization strategies. Therefore, the system 
represents a scalable and immediately deployable 
solution that can accelerate emissions 
transparency and accountability during the 
energy transition period . 
 
CONCLUSION 
In conclusion, this study confirmed that edge 
computing–based CO ₂ emissions monitoring 
provided a technically robust and policy -relevant 
solution for enhancing environmental performance 
in the oil and gas industry. The results showed that 
the deployment of analytics and validation at the 
edge significantly improved data latency, 
transmission efficiency, and emissions detection 
accuracy compared to centralized cloud -only 
architectures. These performance gains directly 
strengthened the Measurement, Reporting, and 
Verification (MRV) processes which enabled more 
reliable compliance with emissions regulations 
while supporting operational decision -making in 
complex industrial environments. The results 
emphasized the strategic role of edge -enabled 
monitoring systems in accelerating energy 
transition and sustainable development objectives in 
addition to the technical contribution. This was 
because the proposed framework supported 
responsible production practices and proactive 
climate action without compromising system 
scalability or reliability by bridging digital 
infrastructure modernization with climate governance 
needs. Therefore, future studies should focus on large
-scale multi-site deployments, integration of advanced 
machine learning models for predictive emissions 
forecasting, and compliance with changing 
international MRV standards to further enhance 
regulatory interoperability and long -term 
sustainability impact. 
 
ACKNOWLEDGMENT 
The authors gratefully acknowledge the 
Politeknik Energi dan Mineral Akamigas, Ministry 
of Energy and Mineral Resources of Indonesia, 
through the Research and Community Service Unit 
(UPPM), for providing study facilities and access 
to relevant data. 
 
DECLARATIONS 
Author contribution 
Suka Handaja, Bambang Yudho Suranta 
contributed equally as the main contributors of 
this paper. All authors read and approved the 
final paper.  
Funding statement 
 None 
Competing interest  
None  
The use of AI or AI-assisted technologies 
None 
 
GLOSSARY OF TERMS AND SYMBOLS 
 
Terms & 
Symbols Definition Unit 
Anomaly 
Detection 
 
 
 
 
 
 
Bandwidth 
Utilization 
 
 
 
 
 
 
The process of 
identifying abnormal 
patterns or deviations in 
emissions data that may 
show equipment 
malfunction, process 
upset, or regulatory 
exceedance  
The volume of data 
transmitted from sensing 
and edge devices to 
cloud infrastructure, 
commonly measured to

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
168 I DOI org/10.29017/scog.v49i2.2020 
 
 
 
 
Carbon 
Capture, 
Utilization, 
and Storage 
(CCUS) 
 
 
Carbon 
Dioxide 
(CO₂ ) 
 
 
 
 
 
Cloud 
Computing 
 
 
 
 
Cybersecurity 
Resilience 
 
 
 
 
Data Latency 
 
 
 
 
Data 
Reduction 
Ratio 
 
 
 
Edge 
Computing 
 
 
 
 
 
Edge Node 
 
 
 
 
 
 
Environmental 
Performance 
 
 
 
 
 
 
 
evaluate network 
efficiency in monitoring 
systems  
A set of technologies that 
capture CO₂ from 
industrial sources, use it 
in products or processes, 
or store it permanently to 
reduce greenhouse gas 
emissions 
A primary greenhouse 
gas emitted from 
combustion, flaring, and 
venting activities in oil 
and gas operations, 
serving as a key indicator 
of environmental 
performance  
A centralized computing 
paradigm that provides 
large-scale data storage, 
advanced analytics, and 
reporting services over 
the internet. 
The ability of a 
monitoring system to 
maintain secure and 
reliable operation in the 
presence of cyber threats 
or network disruptions 
The time delay between 
emissions occurrence at 
the source and data 
availability for alerting, 
analysis, or reporting 
A metric showing the 
proportion of raw sensor 
data volume reduced 
through edge-level 
preprocessing, filtering, 
and aggregation 
A distributed computing 
paradigm in which data 
processing and analytics 
are performed close to 
the data source, reducing 
dependence on 
centralized cloud servers 
A localized 
computational device 
installed near sensors 
that performs real-time 
data preprocessing, 
validation, analytics, and 
anomaly detection  
The measurable outcome 
of an organization’s 
activities related to 
emissions control,  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Environmental
, Social, and 
Governance  
(ESG)  
 
 
 
Industrial 
Internet of 
Things (IIoT) 
 
 
 
 
 
Internet of 
Things (IoT) 
 
 
 
 
 
Intermittent 
Connectivity 
 
 
 
 
Key 
Performance 
Indicators 
(KPIs) 
 
 
Measurement, 
Reporting, and 
Verification 
(MRV) 
 
 
 
Real-Time 
Monitoring 
 
 
 
 
Resource 
Allocation 
 
 
 
 
 
Scalability 
 
 
 
resource efficiency, and 
environmental impact 
mitigation. 
A framework used to 
evaluate corporate 
sustainability 
performance, including 
emissions transparency, 
regulatory compliance, 
and ethical governance 
An extension of IoT 
applied in industrial 
environments, integrating 
sensors, communication 
networks, and analytics 
for operational 
monitoring and 
optimization  
A network of 
interconnected physical 
devices embedded with 
sensors and 
communication 
technologies for data 
collection and exchange 
A condition in which 
network communication 
between field devices 
and cloud platforms is 
unstable or temporarily 
unavailable  
Quantitative metrics used 
to evaluate the technical 
efficiency, reliability, 
and regulatory relevance 
of the emissions 
monitoring system 
A systematic framework 
for quantifying 
emissions, documenting 
results, and verifying 
data accuracy to support 
regulatory compliance 
and climate policy. 
The capability to collect, 
process, and analyze 
emissions data with 
minimal delay, enabling 
immediate operational 
response. 
The management of 
computational, storage, 
and communication 
resources across edge 
and cloud layers to 
optimize system 
performance. 
The ability of the 
monitoring architecture

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 169 
REFERENCES 
Al Hakim, M. F., Tony, B., Chandra, S., Nugraha, 
F. Y., & Nandiwardhana, D. (2025). Mapping 
The Potential CO 2 Source-Sinks for Carbon 
Capture Storage From Industry in Indonesia. 
Scientific Contributions Oil and Gas , 48(1), 
DOI: https://doi.org/10.29017/scog.v48i1.1626. 
Alabdulkreem, E., Allafi, R., Arasi, M. A., Geetha, 
P., Nafie, F. M., Begum, A., . . . Vivek, S. 
(2025). Innovative IoT and blockchain 
integration for real -time urban air quality 
monitoring and an autonomous response 
system. Sustainable Computing: Informatics 
and Systems, 48, https://doi.org/10.1016/
j.suscom.2025.101250. 
Alkilany, A., & Dallaf, A. (2025). Edge Computing 
in IoT Networks: Enhancing Efficiency, 
Reducing Latency, and Improving Scalability. 
International Journal of Advanced Network, 
Monitoring and Controls. 
Ashouri, M., Davidsson, P., & Spalazzese, R. 
(2021). Quality attributes in edge computing for 
the Internet of Things: A systematic mapping 
study. Internet of Things, 11(3), https://
doi.org/10.1016/j.iot.2020.100346. 
Bagkis, E., Hassani, A., Schneider, P., DeSouza, 
P., Shetty, S., Kassandros, T., . . . Khan, J. 
(2025). Evolving trends in application of low -
cost air quality sensor networks: challenges and 
future directions. npj Climate and Atmospheric 
Science, 8, https://doi.org/10.1038/s41612 -025-
01216-4. 
Christensen, M. S. -F. (2024). Leveraging the 
Industrial Internet of Things (IIoT) for Real -
Time CO2 Monitoring, Measurement and 
Visualization: Technologies, Applications and 
Future Directions. Global Internet of Things and 
Edge Computing Summit (hal. 35 - 59, https://
doi.org/10.1007/978-3-031-78572-6). Brussels, 
Belgium: Springer. 
Dankolo, N. M., Radzi, N. H., Mustaffa, N. H., 
Arshad, N. I., Gabi, D., & Yusuf, M. N. (2025). 
Optimizing resource allocation for IoT 
applications in the edge cloud continuum using 
hybrid metaheuristic algorithms. Scientific 
Reports, 15, https://doi.org/10.1038/s41598-025
-97648-2. 
Destiana, S., Irawan, D., Aziz, P. A., & 
Merdekawati, I. (2025). CO 2 Storage Screening 
Criteria Based on Seal Capacity in Indonesia. 
Scientific Contributions Oil and Gas, 48(4), 
DOI: https://doi.org/10.29017/scog.v48i4.1829. 
Diófási-Kovács, O., & Judit, N. (2023). Beyond CO2 
emissions – The role of digitalization in multi -
dimensional environmental performance 
measurement. Environmental and Sustainability 
Indicators, 18, https://doi.org/10.1016/
 
 
 
 
 
Sensor Drift 
 
 
 
 
 
Sensing Layer 
 
 
 
 
 
Sustainable 
Development 
Goals (SDGs) 
 
 
 
System 
Reliability 
 
 
 
 
Temporal 
Granularity 
 
 
 
Threshold-
Based 
Detection 
 
 
Wireless 
Sensor 
Network 
(WSN) 
 
to maintain performance 
as the number of sensors, 
monitored locations, or 
data volume increases 
Gradual deviation in 
sensor measurement 
accuracy over time due 
to aging, environmental 
exposure, or calibration 
loss 
The system layer 
consisting of distributed 
CO₂ sensors and 
supporting instruments 
that acquire raw 
emissions data 
United Nations global 
goals addressing 
sustainability challenges, 
including climate action, 
responsible production, 
and industrial innovation 
The ability of the 
monitoring system to 
operate continuously and 
correctly under varying 
environmental and 
network conditions 
The frequency at which 
emissions data are 
collected and processed, 
influencing the resolution 
of time-based analysis 
A rule-based analytics 
method that triggers 
alerts when emissions 
values exceed predefined 
limits 
A network of spatially 
distributed sensors that 
communicate wirelessly 
to monitor environmental 
or process variables

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 155 - 171 
 
170 I DOI org/10.29017/scog.v49i2.2020 
j.indic.2023.100252. 
Fayos-Jordan, R., Segura -Garcia, J., Soriano -
Asensi, A., Felici -Castell, S., Felisi, J. M., & 
Alcaraz-Calero, J. M. (2021). VentQsys: Low -
cost open IoT system for CO2 monitoring in 
classrooms. Wireless Networks, 27, https://
doi.org/10.1007/s11276-021-02799-5. 
Ficili, I. G., Tricomi, G., & Puliafito, A. (2025). 
From Sensors to Data Intelligence: Leveraging 
IoT, Cloud, and Edge Computing with AI. 
Sensors, 25(6), https://doi.org/10.3390/
s25061763. 
Gamazo-Real, J. -C., Fernández, R. T., & Armas, 
A. M. (2025). Comparison of edge computing 
methods in Internet of Things architectures for 
efficient estimation of indoor environmental 
parameters with Machine Learning. Engineering 
Applications of Artificial Intelligence, 126, 
https://doi.org/10.1016/j.engappai.2023.107149. 
Garcia, A., Saez, Y., Harris, I., Huang, X., & 
Collado, E. (2025). Advancements in air quality 
monitoring: a systematic review of IoT -based 
air quality monitoring and AI technologies. 
Artificial Intelligence Review, 58, https://
doi.org/10.1007/s10462-025-11277-9. 
Hasan, R., Khatoon, R., Akter, J., Mohammad, N., 
Kamruzzaman, M., Shahana, A., & Saha, S. 
(2025). AI -Driven greenhouse gas monitoring: 
enhancing accuracy, efficiency, and real -time 
emissions tracking. AIMS Environmental Science, 
12(3), doi: 10.3934/environsci.2025023. 
Iskandar, U. P., & Musu, J. T. (2025). Optimisasi 
Ekonomi Carbon Capture, Utilization, and 
Storage (CCUS): Pendekatan Iteratif Latin 
Hypercube Sampling dalam Menentukan Laju 
Injeksi CO ₂. Lembaga Publikasi Minyak dan 
Gas Bumi ( LPMGB), 59(1), DOI: https://
doi.org/10.29017/LPMGB.59.1.1796. 
Ismukurnianto, D. (2008). Mitigation of Carbon 
Dioxide and Green House Gas Emissions From 
Oil and Gas Industry in Indonesia. Scientific 
Contribution Oil and Gas, 31(1), 1 - 11. https://
doi.org/10.29017/SCOG.31.1.856. 
Malhotra, A. (2025). Real -Time Air Quality 
Monitoring Using Edge IoT Gateways. 
International Journal of Advanced Research in 
Computer Science and Engineering, 1(4), 
https://doi.org/10.63345/v1.i4.202. 
Marquez-Zepeda, M. J., Santos -Ruiz, I., Pérez, E. -
J., Navarro -Díaz, A., & Delgado -Aguiñaga, J. -
A. (2025). Internet -of-Things-Based CO2 
Monitoring and Forecasting System for Indoor 
Air Quality Management. Mathematical and 
Computational Applications, 30(2), https://
doi.org/10.3390/mca30020036. 
Metia, S., Nguyen, H. A., & Phuc Ha, Q. (2021). 
IoT-Enabled Wireless Sensor Networks for Air 
Pollution Monitoring with Extended Fractional -
Order Kalman Filtering. Sensors, 21(16), 
https://doi.org/10.3390/s21165313. 
Nayak, S., Patgiri, R., Waikhom, L., & Ahmed, A. 
(2022). A review on edge analytics: Issues, 
challenges, opportunities, promises, future 
directions, and applications. Digital 
Communications, 10(3), https://doi.org/10.1016/
j.dcan.2022.10.016. 
Pasarai, U., Iskandar, P. U., & Sismartono, D. 
(2010). Worksheet Screening Of Co2 Eor 
Sequestration Potential In Indonesia. Scientific 
Contributions Oil and Gas , 33(1), DOI: https://
doi.org/10.29017/SCOG.33.1.806. 
Quttainah, M. A., & Ayadi, I. (2024). The impact 
of digital integration on corporate sustainability: 
Emissions reduction, environmental innovation, 
and resource efficiency in the European. Journal 
of Innovation & Knowledge, 9(3), https://
doi.org/10.1016/j.jik.2024.100525. 
Rahmadani, A. A., Syaifudin, Y. W., Setiawan, B., 
Panduman, Y. Y., & Funabiki, N. (2024). 
Enhancing Campus Environment: Real -Time 
Air Quality Monitoring Through IoT and Web 
Technologies. Journal of Sensors And Actuator 
Networks, 14(1), https://doi.org/10.3390/
jsan14010002. 
Roostaei, J., Wager, Y. Z., Shi, W., Dittrich, T., 
Miller, C., & Gopalakrishnan, K. (2023). IoT -
based edge computing (IoTEC) for improved 
environmental monitoring. Sustainable 
Computing: Informatics and Systems, 38,

Edge Computing–Enabled Real-Time CO₂ Emissions Monitoring: A Low-Latency and Bandwidth-Efficient 
Architecture for Oil and Gas Sector (Suka Handaja and Bambang Yudho Suranta). 
 
DOI org/10.29017/scog.v49i2.2020 I 171 
https://doi.org/10.1016/j.suscom.2023.100870. 
Samuel, D. -K., Daniel, A. -M., & Jennifer, M. -F. 
(2025). Conducting a systematic literature 
review of environmental emissions performance 
and eco -innovation research. International 
Journal of Innovation Studies, https://
doi.org/10.1016/j.ijis.2025.10.005. 
Siddiqui, F., Rabbani, H., Akhtar, N., Suneel, S., & 
Naik, A. S. (2025). Scalable Environmental 
Monitoring System Using Iot And Edge 
Computing. International Journal of 
Environmental Science, 11(11s), DOI: https://
doi.org/10.64252/ybsrxh42. 
Sugihardjo. (2022). CCUS -Aksi Mitigasi Gas 
Rumah Kaca dan Peningkatan Pengurasan 
Minyak CO2. LPMGB, 56(1), DOI: 10.29017/
LPMGB.44.3.709. 
Yadav, L., Murugan, V., Vijayakanthan, A, K. B., 
Mathurkar, P., & Urkude, G. (2025). Integrating 
Edge Computing And Iot For Real -Time Air 
And Water Quality Monitoring Systems. 
International Journal of Environmental 
Sciences, 11(17), DOI:10.64252/z52kvj10. 
Yavari, A., Mirza, I. B., Bagha, H., Korala, H., 
Dia, H., Scifleet, P., . . . Shafiei, M. (2023). 
ArtEMon: Artificial Intelligence and Internet of 
Things Powered Greenhouse Gas Sensing for 
Real-Time Emissions Monitoring. Sensors, 23
(18), https://doi.org/10.3390/s23187971.
