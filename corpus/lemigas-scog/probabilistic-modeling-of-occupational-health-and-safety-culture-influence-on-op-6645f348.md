---
source_id: "lemigas-scog"
title: "Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety in Petrochemi"
summary: "Bayesian network study of how occupational health and safety culture affects operational safety in petrochemical plants, using data from 78 industrial placement students."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2097"
retrieved_at: "2026-10-24T14:30:45+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "6645f348e2dfffeb5f72f5af45e9522e05e32aab6c8210b895b93c0e51fa8643"
collected: "manual"
---

# Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety in Petrochemi

DOI org/10.29017/scog.v49i2.2097 I 509 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Probabilistic Modeling of Occupational Health and Safety  Culture 
Influence on Operational Safetyin Petrochemical and Oil and Gas 
Facilities Using Bayesian Networks 
ABSTRACT - The oil and gas industry and petrochemicals are known for high -risk operations, 
characterized by complex processes, hazardous materials, and varied work conditions; therefore, there is a 
need for a strong OHS culture to promote operational safety. This paper examines the effect of OHS culture 
on operational safety by employing probabilistic analysis based on Bayesian Network modeling. In this 
study, a quantitative explanatory research design is used, in which data are obtained from 78 industrial 
placement students at Politeknik Industri Petrokimia Banten who worked in production and maintenance 
facilities at high -risk petrochemical and oil and gas companies in the industrial area of Cilegon -Banten, 
Indonesia. OHS culture is measured across four aspects: management commitment, safety communication, 
risk awareness, and safety participation. In contrast, operational safety is assessed using measures of safety 
behavior and near -miss reporting. OHS culture plays a major role in determining operational safety, with 
safety communication that has the greatest influence on safety performance. Probabilistic inference 
indicates that higher OHS culture levels lead to safer operating conditions, while a lack of communication is 
a significant factor in poor safety performance. Sensitivity analysis further supports communication as a key 
determinant of safety behavior and risk management. 
Keywords: OHS culture, operational safety, bayesian network, oil and gas industry, safety communication 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 509 - 527 
Politeknik Industri Petrokimia Banten, 
Raya Anyer street KM 2, Ciwandan, Cilegon, Banten 42443, Indonesia. 
Corresponding author: Supardi (supardi@poltek-petrokimia.ac.id) 
Manuscript received:  February 27th, 2026; Revised: April 08th, 2026 
Approved:  May 14th, 2026; Available online: June 22th, 2026; Published: June 22th, 2026. 
Supardi, Jerry, and Denny Hendrik Nainggolan 
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Supardi, Jerry, and Denny Hendrik Nainggolan, 2026, Probabilistic Modeling of Occupational 
Health and Safety Culture Influence on Operational Safety in Petrochemical and Oil and Gas 
Facilities Using Bayesian Networks , Scientific Contributions Oil and Gas, 49 (2) pp. 509-
527. DOI org/10.29017/scog.v49i2.2097.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
510 I DOI org/10.29017/scog.v49i2.2097 
 
INTRODUCTION 
The occupational safety and health (OSH) 
problem remains relevant throughout the period 
2021–2024. According to the ILO, nearly 2.3 
million workers die yearly due to accidents and 
work-related illnesses, and more than 374 million 
non-fatal injuries are observed across the world. 
The overall fatality rate remains rather stable at 3.6
-4 deaths per 100,000 workers per year. 
In Indonesia, the oil, gas, and petrochemical 
industries remain among the largest sources of 
occupational accidents. For instance, the Social 
Security Administering Body for Employment 
(BPJS Ketenagakerjaan) reports over 297,000 work 
accidents occurring in the country in 2023. These 
figures have been steadily growing for several 
years. What is more important, the above -
mentioned industrial sectors have always been a 
focus of occupational accidents in Indonesia 
because of their high hazard levels. Additionally, 
as follows from government regulations, in 
particular Government Regulation No. 50 of 2012 
(PP No. 50 Tahun 2012) on the Implementation of 
Occupational Safety and Health Management 
Systems (SMK3), all high -risk industries are 
required to use certain OHS management systems. 
Figure 1. Safety performance trends in the oil and gas industry (2021–2024). 
Based on IOGP safety performance indicators & ILO global occupational safety data. 
In the oil, gas, and petrochemical industries, this 
means companies are obliged to implement OHS 
management system models. Compliance with this 
regulation, however, varies greatly among different 
firms, particularly between state -owned enterprises 
(BUMN) and private enterprises. 
According to industry performance data, the oil 
and gas industries face higher risks than the global 
average. According to reports from the 
International Association of Oil and Gas Producers 
(IOGP), 20 deaths occurred in 2021, and the 
number rose slightly in subsequent years to 32 in 
2024. The fatal accident rate was reduced to 0.77 
deaths per million working hours due to the rising 
total number of working hours. Nevertheless, the 
accident rates in the industry remain significantly 
higher than those of other industries. 
In addition to fatal accidents, the number of non
-fatal accidents is crucial for analyzing the safety 
performance of oil and gas operations. Data show 
that non-fatal incidents still occur frequently in the 
field, with a considerable share attributed to 
equipment accidents and general operational risks. 
As for the causes of incidents in the industry, more 
than 60% are related to human factors, and less 
than 40% to technical and organizational factors.

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 511 
More precisely, human factors play the key role 
in accidents in oil and gas operations according to 
accident analyses. As shown in the HFACS -OGI 
model analysis, over 60% of accidents in the oil 
and gas industry stem from human factors, 
including individual errors, loss of situational 
awareness, and poor communication (Nwankwo et 
al., 2022) . Technical factors account for only 10 -
20%, while organizational and environmental 
factors account for 10-15%. 
To start with, the concept of OHS culture needs 
to be explained. OHS culture refers to people's 
perceptions of safety issues. In high -risk industries, 
OHS culture is an informal structure that influences 
workers' actions in high -risk situations. Studies 
have shown that organizations with a strong OHS 
culture have a good safety record, as they 
demonstrate higher compliance with safety 
standards and fewer accidents. In terms of 
numbers, a strong OHS culture can improve safety 
performance by 30 -35% compared with 
organizations with a weak OHS culture  (Ehiaguina 
et al., 2024; Jasmadi et al., 2025). 
Moreover, modern concepts in industrial 
safety management include the vision of zero 
accidents, meaning that all industrial accidents 
can be prevented with a strong OHS culture in 
the company. Data show that implementing 
culture -based strategies can decrease accidents 
by 40 -60% over time when combined with a 
leader's role in promoting effective 
communication and cooperation among 
employees  (Blanco -Juárez & Buele 2025) .  
Examples of risky activities in the oil and gas 
industry reveal how a safety culture can be 
important in preventing accidents in high -risk 
situations. For example, working in confined 
spaces poses risks such as accidental inhalation 
of toxic gases or suffocation from lack of 
oxygen. According to research findings, about 
70% of risks stem from improper execution of 
work procedures and employees' risky behavior, 
including inadequate atmospheric testing and the 
use of personal protective equipment  (Silva & 
Amaral 2025) . Thus, the effective functioning of 
safety systems relies heavily on employees' 
safety behavior . 
Similarly, risk identification and evaluation 
methods (such as HIRARC) suggest that the 
success of risk control measures greatly depends on 
human factors. Although risks can be effectively 
identified and managed, their implementation is 
highly contingent on employees' awareness and 
willingness to comply. In particular, increased risk 
awareness has been shown to increase the 
effectiveness of risk controls by up to 25%; 
therefore, an OSH culture should be promoted to 
facilitate the work of the safety management 
system (Ihsan et al., 2025). 
However, beyond purely technical 
considerations, psychosocial factors also contribute 
to workplace safety issues in the oil and gas 
industry. Offshore employees experience heavy 
workload, tough weather conditions, and isolation 
from their social environment; such stressful 
factors may significantly contribute to mental 
disorders and, therefore, increase accident risk. 
Research results indicate that under such 
conditions, psychosocial factors increase the 
possibility of accidents by 20–30%  (D’Antoine 
et al., 2023) . Workplace safety in the oil and gas 
industry thus requires a comprehensive approach 
that accounts for both psychological and 
technical considerations . 
Safety performance management methods have 
expanded from lagging to leading indicators. 
Leading indicators such as safety culture, 
procedural compliance, and safety training were 
found to be much more indicative of safety 
performance than traditional lagging indicators, 
such as accident count. In other words, using 
leading indicators can improve the effectiveness 
of safety management practices by up to 50%; as 
such, leading indicators, especially safety 
culture, need to be included in safety systems  
(Niu et al., 2023) . 
Based on a thorough literature review, it was 
found that although many studies have explored 
various applications of Bayesian Networks (BN) 
for technical safety, very few have applied BN to 
behavioral and psychosocial safety problems. 
Within the oil and gas industry in particular, most 
research papers analyzing OSH culture issues 
relied on traditional statistical methods, such as

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
512 I DOI org/10.29017/scog.v49i2.2097 
regression analysis or SEM. Given the limitations 
of conventional analysis methods, the current study 
employs BN as an appropriate tool to analyze the 
impact of OSH culture on workplace safety. 
Although numerous research studies explore 
OSH culture and its influence on workplace safety, 
the vast majority rely on classical statistical 
techniques that cannot effectively handle complex 
interactions among variables and the uncertainty 
inherent in real -world data. In practice, the 
relationship among safety culture, human factors, 
and workplace safety is uncertain and nonlinear. 
Therefore, this study aims to develop a BN -based 
probabilistic model for analyzing the impact of 
OSH culture on operational safety in the 
petrochemical and oil and gas industries. Expected 
contribution includes scientific development in the 
area of probabilistic safety analysis, as well as 
some recommendations to increase OSH 
effectiveness in the industry. 
 
METHODOLOGY 
Research design 
An explanatory quantitative design will be used 
in the present study to investigate the influence of 
occupational safety and health (OSH) culture on 
operational safety in high -risk industries. An 
explanatory approach was chosen to detect 
relationships among the variables analyzed and to 
measure the magnitude of their influence on one 
another. To capture the complexity and uncertainty 
of interactions among variables, the Bayesian 
Network (BN) methodology was adopted; this 
method allows for estimating probabilistic 
dependencies among variables and predicting the 
probability of accidents under certain conditions. 
Population and sample 
The population consists of all third -year, sixth-
semester students at the Banten Petrochemical 
Industry Polytechnic undergoing industrial 
placement; the total number of subjects is 112. The 
survey was conducted at sites where students 
undergo industrial placement at several 
petrochemical and oil and gas companies operating 
in the Cilegon -Banten industrial complex, one of 
the largest petrochemical hubs in Indonesia. 
Participating companies include state -owned 
enterprises, such as PT Chandra Asri 
Petrochemical and PT Krakatau Steel, as well as 
related companies that adhere to SMK3 safety 
standards established by Government Regulation 
No. 50 of 2012 (PP No. 50/2012). None of the 
multinational companies was surveyed. 
Sampling will be conducted on purposive 
grounds; specifically, only students who spent at 
least 3 months in industrial practice and worked in 
hazardous departments (production, process, and 
maintenance divisions) will be included in the 
survey; as a result, 78 samples will be selected. 
All participating companies operate in 
accordance with SMK3 safety standards 
established by Government Regulation No. 50 of 
2012 (PP No. 50/2012); some also adhere to 
internationally recognized OHS standards, such 
as ISO 45001:2018 and IOGP safety guidelines. 
These safety systems formed the basis for 
assessing students' perceptions of safety culture 
and safety behavior . 
Research variables 
Variables are considered either independent or 
dependent in this research within a Bayesian 
Network framework. The independent variable in 
the analysis is Occupational Health and Safety 
(OHS) Culture, while the dependent variable is 
Operational Safety. The indicators of each variable 
are outlined in Table 1. The two research variables 
are modeled as nodes in the Bayesian Network that 
show their relationship. 
Data collection techniques 
Data collection was conducted using a 
structured questionnaire with a five -point Likert -
scale response format. These include response 
choices of 1 (Strongly disagree), 2 (Disagree), 3 
(Neither agree nor disagree), 4 (Agree), and 5 
(Strongly Agree). The research tools were 
developed by drawing on reliable indicators of 
OSH culture and operational safety identified in 
previous research. Field observation was also 
conducted alongside the questionnaires to 
validate the responses .

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 513 
Table 1. Research variables and indicators 
 Variable Dimension Indicator 
 OHS culture Management Commitment Leadership support for OSH 
  Safety Communication Risk Information Communication 
  Risk Awareness Ability to identify hazards 
  OSH participation Involvement in OSH programs 
 Operational safety Procedural compliance Adherence to SOPs 
  Use of PPE Consistent use of PPE 
  Near-miss reporting Willingness to report incidents 
  Safe behavior Safe work practices 
 
Data processing and analysis 
A Bayesian Network model was used to analyze 
the data through three main processes: structure 
learning, parameter estimation, and probabilistic 
inference. From a mathematical perspective, 
Bayesian Networks depend on Bayes' theorem as 
follows Equation 1, 
where P(A|B) is the posterior probability, P(B|A) is 
the likelihood, P(A) is the prior probability, and P
(B) is the evidence probability.  For models with 
multiple variables, the joint probability is 
expressed as Equation 2, 
𝑃 𝐴  𝐵  = 𝑃 𝐵  𝐴   𝑃 𝐴 𝑃 𝐵  
 
(1)  
𝑃 𝑋1, 𝑋2, … , 𝑋𝑛 =  𝑃 𝑋𝑖   Pa 𝑋𝑖  
𝑛
𝑖=1
 
 
(2)  
where Pa(Xi) is the parent node of variable Xi. 
Survey data, in the form of Likert -scale 
responses, are then converted into probabilities to 
construct a Conditional Probability Table (CPT) for 
each node. An example of a CPT structure is 
shown in Table 2. 
Table 2. Example of a conditional probability table (CPT) 
OHS culture Operational safety (safe) Operational safety (unsafe) 
High 0.85 0.15 
Medium 0.65 0.35 
Low 0.40 0.60 
 
The second phase entails inferential analysis to 
determine the probability of operational safety at 
different values of the OSH culture variable. 
Sensitivity analysis was conducted to identify 
the variables with the greatest impact on 
operational safety . 
Validity and reliability 
Pearson correlation with a criterion coefficient 
of over 0.3 was used to test the validity. On the 
other hand, Cronbach's Alpha of 0.7 was the cutoff 
for assessing reliability. Results show that all 
research instruments met the validity and reliability 
requirements for Bayesian Network analysis. 
 
RESULT AND DISCUSSION 
Respondent characteristics and data description 
A total of 78 respondents were analyzed. All the 
respondents were industry trainees with a three -
month placement period in high -risk environments. 
As for placement area, 50 respondents (64.1%) 
were placed in the Production/Operation unit, 
while 28 respondents (35.9%) were in the 
Maintenance Unit. About placement duration, 31 
respondents (39.7%) completed 3–4 months of 
placement; 29 respondents (37.2%) completed 5–6

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
514 I DOI org/10.29017/scog.v49i2.2097 
months of placement; and 18 respondents 
(23.1%) exceeded 6 months of placement When 
asked about safety orientation, 56 respondents 
(71.8%) received safety induction before going 
into work area; and 35 respondents (44.9%) 
received intensive training of hazards in the unit. 
This means that although all respondents have 
worked in operational environments, they have 
not been equally reinforced in OSH at the hazard
-specific level . 
From the above characteristics of the 
respondents, it is apparent that most respondents 
have worked in hazardous environments. However, 
some discrepancies have arisen regarding the 
transfer of safety competence from general safety 
induction to hazard -specific training. This 
implies a lack of safety knowledge transfer, 
especially on operational hazards such as 
chemical handling, hot work, confined space, 
and high -energy mechanical operations . 
Descriptive analysis of OSH culture and 
operational safety 
Based on the descriptive statistics, OSH Culture 
is in the 'Good' category, with a mean score of 
68.5%. As for dimensions, risk awareness achieved 
the highest score of 74.3%, followed by 
management commitment (71.0%) and safety 
participation (67.0%), while safety 
communication had the lowest score of 61.2%. 
This means that trainees have adequate 
knowledge of risks but face challenges in 
communicating those safety -related risks .Before 
providing descriptive statistics, it is worth noting 
the criterion used to classify scores on the five -
point Likert scale. Scores between 81%–100% fall 
under Very Good; scores between 61%–80% fall 
under Good; scores between 41%–60% fall 
under Fair; scores between 21%–40% fall under 
Poor, while scores between 0%–20% fall under 
Very Poor. These criteria, which are adopted 
from Riduwan (2013), have been used 
throughout the analysis . 
The highest score of the risk awareness 
dimension depicts a good perception of hazards in 
the work environment. On the other hand, the 
lowest score for the safety communication variable 
indicates a poor willingness to communicate 
hazards and to report near misses. It is worth noting 
that safety communication is a key element in 
enhancing safety operations. Therefore, to achieve 
operational safety, the first step is to identify risks 
through safety communication. 
Table 3. Respondent characteristics 
 Characteristics Category n % 
 Assignment area Production/operations  50 64.1 
  Maintenance 28 35.9 
 Duration of placement 3–4 months 31 39.7 
  5–6 months 29 37.2 
  > 6 months 18 23.1 
 Safety orientation Yes 56 71.8 
  No 22 28.2 
 Specific hazard training Yes 35 44.9 
  No 43 55.1 
 
Table 4. Descriptive scores of OSH culture dimensions 
 Operational safety indicators Average score Percentage (%) Category 
 Compliance with SOP 3.48 69.6 Good 
 Use of PPE 3.32 66.4 Good 
 Near-miss reporting 2.89 57.8 Fair 
 Safe work behavior 3.41 68.2 Good 
 Total average 3.28 65.5 Good

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 515 
One of the major differences here is in safety 
communication, where the gap between risk 
awareness and safety communication has widened. 
This suggests that trainees have been unable to 
translate knowledge of risks into effective safety 
communication. That is why they have shown 
good awareness of risks but poor safety 
communication skills . 
To strengthen the description of operational 
safety, measurements were also taken for four 
outcome indicators: SOP compliance, PPE use, 
near-miss reporting, and safe work behavior. 
Safety operations are classified as good, while 
the near -miss reporting indicator remains rated as 
average. This combination of ratings indicates that 
the level of safety communication identified in the 
survey data is low. It is important to 
acknowledge that there is a direct connection 
between the lack of safety communication and 
the low incidence of near -miss reports, which is 
one of the most important indicators for 
preventing more serious accidents . 
Development of a Bayesian network structure 
Bayesian network structure development aims 
to model the causal structure between the 
components of OSH culture dimensions and 
operational safety in the complex context of the 
petrochemical industry and oil -and-gas sector. 
Therefore, the structure of the Bayesian Network 
(BN) includes three basic layers: 1). The 
organizational layer; 2). The behavioral layer; and 
3). The operational outcome layer. 
Organizational Layer – OSH cultural 
components at the organizational level are root 
causes. Such variables characterize this layer as 
management commitment, safety communication, 
risk awareness, and safety participation. These 
variables can be viewed as major determinants of 
individual worker behavior. 
Behavioral Layer – worker behavior resulting 
from the effects of various OSH cultural 
components. Variables such as safe behavior, 
tendency toward unsafe behavior, and near -miss 
reporting behavior are included in this layer. 
Herein, safe behavior refers to compliance with 
safe procedures. Unsafe behavior is characterized 
by violations and actions that pose potential risks. 
Near-miss reporting is a proactive indicator of 
OSH performance. 
Operational Outcome Layer – operational safety 
conditions as major outcomes of OSH 
performance. The operational safety state variable 
is used here. This is the main output of the BN 
model. Worker behavior (the previous layer) 
directly affects the operational safety state variable. 
It should be emphasized that the relationship 
structure is built on a cause -and-effect basis, a 
widely recognized approach in the industrial safety 
literature. Organizational causes affect behavior, 
which, in turn, leads to safety consequences. First, 
safety communication and management 
commitment affect such components as near -miss 
reporting and safe behavior. Secondly, increased 
risk awareness leads to better hazard identification 
and safe behavior. Thirdly, both safe behavior and 
near-miss reporting behavior are directly linked to 
the probability of safe operational conditions. 
 
Table 5. Operational safety indicators 
 Operational safety indicators Average score Percentage (%) Category 
 Compliance with SOP 3.48 69.6 Good 
 Use of PPE 3.32 66.4 Good 
 Near-miss reporting 2.89 57.8 Fair 
 Safe work behavior 3.41 68.2 Good 
 Total average 3.28 65.5 Good

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
516 I DOI org/10.29017/scog.v49i2.2097 
 Node Low Medium High  
 Management commitment 0.18 0.44 0.38  
 Safety communication 0.24 0.48 0.28  
 Risk awareness 0.14 0.40 0.46  
 Safety participation 0.20 0.47 0.33  
 
 
Layer Node Description State 
 Organizational Management commitment Level of management commitment to OSH implementation Low, Medium, High 
 Organizational Safety communication Effectiveness of risk and safety communication Low, Medium, High 
 Organizational Risk awareness Individual ability to recognize and understand hazards Low, Medium, High 
 Organizational Safety participation Level of involvement in occupational safety and health programs Low, Medium, High 
 Behavioral Safe behavior Level of compliance with safety procedures Low, Moderate, High 
 Behavioral Tendency toward unsafe behavior Tendency to engage in unsafe behavior Low, Moderate, High 
 Behavioral Near-miss reporting Level of near-miss reporting Low, Moderate, High 
 Intermediate Hazard exposure level Hazard exposure level Low, Medium, High 
 Intermediate Control effectiveness Effectiveness of risk control in the field Low, Moderate, High 
 Outcome Operational safety status Operational safety status Safe, Unsafe 
 
To increase the model's complexity and make it 
more realistic, the inter -variable relationship 
structure includes intermediary variables (nodes). 
The major relationships are described below:   
• Management commitment, safety 
communication and safety participation. 
Improved management commitment leads to 
better safety communication and worker 
participation in OSH activities.  
• Safety communication, near -miss reporting and 
safe behavior. Efficient safety communication 
increases risk information transparency and 
promotes near-miss reporting and safe behavior.  
• Risk awareness, safe behavior and tendency 
toward unsafe behavior. Higher risk awareness 
encourages safe behavior and reduces tendency 
toward unsafe behavior.  
• Safety participation, control effectiveness. 
Increased participation in OSH programs 
enhances control effectiveness in the field.  
• Tendency toward unsafe behavior, level of 
hazard exposure. Increased tendency to unsafe 
behavior means higher hazard exposure.  
• Safe behavior + control effectiveness, 
operational safety state. Both safe behavior and 
control effectiveness affect the probability of 
operating conditions being safe. Both safe 
behavior and control effectiveness affect the 
probability of operating conditions being safe. 
According to the Bayesian network structure 
developed in this study, operational safety depends 
on the interactions between organizational causes, 
Note: The 'Intermediate' layer nodes (Hazard Exposure Level and Control Effectiveness) serve as bridging variables between th e 
behavioral layer and the operational outcome layer. These nodes are not directly observed through the questionnaire but are i nferred 
through probabilistic relationships derived from the parent nodes in the organizational and behavioral layers. This distincti on prevents 
conceptual overlap between the node categories and ensures structural clarity in the Bayesian Network topology.  
human behavior, and operational conditions. The 
network model demonstrates that changes in OSH 
culture will lead to improved operational safety 
conditions, not only through direct effects but also 
through behavioral change. 
The use of intermediary variables, such as 
hazard exposure level and control effectiveness, 
creates another aspect of real -life operations. 
Overall, the BN model enables the explanation of 
the link between OSH culture and operational 
safety, as well as the development of decision -
making scenarios.  
Probability estimation and conditional 
probability table (CPT) 
After constructing the BN network structure, the 
next step concerns probability estimates and the 
Conditional Probability Table (CPT). According 
to the results, the initial probabilities of OSH 
culture components performing are moderate to 
high. Risk awareness shows the highest 
probability distribution. Thus, the probability of 
belonging to the high -risk awareness group is 
0.46, while the probability of high safety 
communication is only 0.28 . 
Table 6. Node and state structure in a Bayesian network 
Table 7. Initial probabilities of several main nodes

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 517 
Moreover, the first probability distribution is 
consistent with the earlier descriptive analysis, 
where risk awareness is more prevalent than any 
other element. The dimension of safety 
communication has the smallest portion of high 
categories among all others. It implies that 
communication barriers not only emerge within the 
medium category but also persist in the probability 
distribution. As an example of the CPT, Table 8 
illustrates how the probability of the system 
being safe depends on safe behavior and near -
miss reporting . 
According to the table, the highest probability 
of the system operating safely occurs when both 
the level of safe behavior and the rate of near -miss 
reporting are high. However, when safe behavior 
and near -miss reporting are low, the system is 
likely unsafe to operate. Hence, the CPT confirms 
that safe behavior and near -miss reporting are the 
two main mediators between OSH culture and 
operational safety. 
In terms of organizational behavior, these CPT 
values mean that if organizations do not motivate 
employees to engage in proactive reporting and 
adhere to certain procedures, they expose 
themselves to a high risk of failure. It implies that 
 
 
 
 
 
Safe behavior Near-miss reporting P(Safe) P(Unsafe) 
 
 Safe High 0.92 0.08  
 Safe Moderate 0.84 0.16  
 Safe Low 0.73 0.27  
 Medium High 0.78 0.22  
 Medium Moderate 0.65 0.35  
 Moderate Low 0.51 0.49  
 Unsafe High 0.42 0.58  
 Unsafe Moderate 0.31 0.69  
 Unsafe Low 0.18 0.82  
 
Table 8. Example of a conditional probability table (CPT) for operational safety 
organizations should ensure a specific behavioral 
outcome by implementing policies. Specifically, 
regular safety briefings, leadership presence in 
operational areas, and non -punitive incident -
reporting systems can improve overall safety. 
Probabilistic inference analysis 
To estimate the influence of OSH culture on 
operational safety, an inferential analysis was 
conducted. In the baseline scenario, the probability 
of safety is 0.68. On the contrary, the probability 
that the system is in an unsafe state is 0.32. If all 
OSH culture dimensions are high, then the 
probability of safety increases to 0.86. On the other 
hand, low probability occurs when all dimensions 
are in low categories; it amounts to 0.41. 
The comparison of probability values obtained 
for different scenarios demonstrates that OSH 
culture influences operational safety. For instance, 
increasing all dimensions results in a high safety 
probability (0.86). On the contrary, the probability 
of safety in the low -communication scenario is 
0.57. This result indicates that safety 
communication is an important control point in the 
operational safety system. 
 
 Scenario P(safe) P(unsafe)  
 Baseline 0.68 0.32  
 High OHS culture 0.86 0.14  
 Moderate OHS culture 0.68 0.32  
 Low OHS culture 0.41 0.59  
 High communication, others moderate 0.76 0.24  
 Low communication, others moderate 0.57 0.43  
Table 9. Results of probabilistic inference for several scenarios

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
518 I DOI org/10.29017/scog.v49i2.2097 
 
Figure 2. Bayesian inference results for several scenarios 
Figure 2 shows the results of Bayesian inference 
across different safety culture scenarios. From the 
figure, it can be seen that when all OHS culture 
dimensions are high simultaneously, the probability 
of safety is 0.86, whereas under low conditions, it 
drops to 0.41. In turn, reducing the dimension of 
safety communication lowers the probability of 
operational safety. More specifically, it decreases 
from 0.68 to 0.57. As a result, the dimension of 
safety communication serves as a pivotal control 
point for operational safety. This conclusion is 
consistent with the study by Naji et al. (2022). 
The researchers have proven that safety 
communication mediates the relationship 
between safety culture and performance . 
Sensitivity analysis 
The purpose of the sensitivity analysis was to 
identify OHS culture nodes that most strongly 
influence the probability of operational safety. 
Based on the results obtained, the highest 
sensitivity is observed in the safety communication 
node, with a weight of 0.34. Management 
commitment node follows with a sensitivity weight 
of 0.27, whereas risk awareness equals 0.23. 
Lastly, safety participation has a sensitivity weight 
of 0.16. Therefore, it can be concluded that safety 
communication is the most important variable 
affecting changes in the probability of safety. 
Based on these results, it is clear that improving 
the quality of safety communication, including 
hazard reporting, toolbox talks, and feedback, may 
significantly reduce the likelihood of risks 
occurring. Management commitment is also 
important because it serves as a policy guide, sets 
an example for other employees, and allocates 
safety resources. 
As illustrated in Figure 3, the sensitivity weight 
at the safety communication node is 0.34. 
According to this parameter, any change at this 
node has the greatest influence on operational 
safety outcomes. The findings are similar to those 
reported by Mathisen et al. (2022), who found that 
safety voice has important predictive value for 
safety outcomes on offshore oil rigs. Such a voice 
represents a form of safety communication, guided 
by leadership presence and job control. 
Based on the sensitivity chart, it is possible to 
outline the priority of intervention. Specifically, 
safety communication is the first intervention node. 
This is confirmed by the results of the descriptive 
analysis, in which safety communication received 
the lowest score.

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 519 
 
Figure 3. Sensitivity analysis of operational safety 
Discussion 
Based on the findings of this study, it becomes 
evident that an OSH culture significantly impacts 
operational safety via systemic factors rather than 
linear ones. In particular, according to the 
constructed Bayesian Network, the dimensions of 
OSH culture – namely, management commitment, 
safety communication, risk awareness, and safety 
participation – affect safe behavior, near -miss 
reporting, and operational safety. Such a pattern is 
particularly important for oil and gas and 
petrochemical organizations, where hazardous 
environments predominate due to large 
hydrocarbon inventories, high pressure and 
temperature levels, explosive gases, and 
simultaneous operation under risky conditions 
(Skiba 2025). In other words, operational safety in 
such organizations stems from a combination of 
human, organizational, technological, and 
environmental interactions. It is in line with the 
modern approach to OSH issues, which views 
accidents as resulting from multiple layers of 
failure rather than a single factor (Jamil et al., 
2025; McKinnon 2025). 
Interpreting the descriptive findings, in which 
the highest dimension value corresponds to risk 
awareness and the lowest to safety communication, 
it is worth noting that this information is 
particularly important in oil and gas organizations 
(Tribuana et al., 2018). Indeed, the latter often have 
workers who recognize risks such as fire danger, 
explosions, H2S, flammable atmospheres, or 
hazards associated with confined spaces. However, 
they do not communicate their views on these 
matters either due to hierarchical barriers, pressure 
from production targets, or a lack of a 
communicative safety culture (Okon et al., 2025. 
These findings are consistent with those of 
Quaigrain et al., who argue that workers' 
knowledge and attitudes towards OSH issues affect 
compliance in Ghana's oil and gas industry, and 
with those reported by Mathisen et al. on the 
impact of the "safety voice" on offshore oil rigs. 
More precisely, the authors state that such a 
measure increases in cases when leadership support 
and job control are available, while high work 
demands reduce it. As such, there is no automatic 
transition from risk awareness to safe behaviors in 
the absence of a psychologically safe 
communication environment (Mathisen et al., 
2022; Quaigrain et al., 2022). 
As for the concepts that explain this study's 
findings, the most relevant are safety climate and 
safety culture. While the first refers to workers' 
perceptions of the importance of safety -related 
actions and measures at a given point in time, the 
second term describes the underlying values, 
beliefs, norms, and practices related to OSH in 
organizations (Houette & Mueller -Hirth 2022. For 
instance, oil and gas organizations may have OSH 
management programs described on paper. 
However, their implementation and effectiveness in 
practice may vary depending on employees' 
perceptions of the importance of OSH measures, 
management's actual commitment, and other 
factors. Djunaidi et al. reported the effects of a 
change in ownership from multinational 
corporations to state -run companies on workers' 
perceptions of safety climate in oil and gas 
organizations in Indonesia. Their findings are 
consistent with this research and demonstrate that 
the safety culture dimension is highly sensitive to 
organizational, leadership, and regulatory changes  
(Djunaidi et al., 2024).

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
520 I DOI org/10.29017/scog.v49i2.2097 
Turning to the Indonesian regulatory system, the 
state-owned enterprises (BUMN) in the oil, gas, 
and petrochemical sectors are obliged to implement 
the OHS Management System (SMK3) pursuant to 
Government Regulation No. 50 of 2012 (PP No. 
50/2012). Conducting a brief gap analysis of its 
application reveals the following strengths and 
weaknesses of the policy. Its main strength is that 
PP No. 50/2012 provides a set of elements for the 
OHS management system, comprising 12 parts, 
including policy development, planning, hazard 
identification, and performance evaluation. One of 
the main drawbacks is that the regulation is 
implemented in a rather mechanistic way: 
organizations meet documentation requirements yet 
fail to achieve cultural internalization, as evidenced 
by a relatively low rate of safety communication 
(61.2%). In addition, PP No. 50/2012 does not 
include the use of probabilistic risk assessment 
or the quantitative measurement of OSH culture. 
All these gaps indicate that PP No. 50/2012 can 
serve as a foundation for developing a safety 
culture to improve safety performance in the 
study organization.   
From a technical point of view, the Bayesian 
model's finding that a high level of safety culture 
significantly increases the likelihood of safe 
conditions seems quite understandable. First, 
management commitment affects specific decisions 
such as the allocation of the HSE budget, the 
quality of permits to work, process discipline, 
proper worker training, toolbox meetings, field 
audits, and readiness to stop operations when 
conditions are unsafe (Salleh et al., 2024. Second, 
implementing the Occupational Health and Safety 
Management System requires specific 
organizational and behavioral factors: leadership, 
worker participation, risk assessment, 
operational control, and improvement measures. 
The absence of at least one element increases 
barriers and corresponding safety performance  
(McKinnon 2025) . 
First, it should be noted that the result that 
safety communication is the most influential factor 
in the model is very robust from both practical and 
theoretical viewpoints. According to research by 
Naji et al., safety communication acts as a mediator 
between safety culture and safety performance in 
the petrochemical industry, meaning that a good 
safety culture does not necessarily translate into 
safety performance unless there is effective 
communication. This is true in the present study as 
well, because when situations related to safety 
communication are limited, the likelihood of 
maintaining safe operations becomes much lower 
even with the same other variables (Miloševiæ et 
al., 2025. It is natural from an industrial viewpoint 
because almost any high -risk process performed in 
the oil and gas or petrochemical industries involves 
communication: shift handovers, coordination of 
energy isolation, checking equipment status, 
reporting process deviations, SIMOPS activities, 
reporting near misses, and making stop -work 
decisions. A lack of communication at any step 
can trigger a chain of events that culminates in 
loss of control over the process or employee 
injury  (Naji et al., 2022) . 
As far as human factors are concerned, the 
study's findings align with the conclusions of 
Nwankwo et al., who found that accidents in the oil 
and gas industry were usually caused by human 
factors such as unsafe decisions, lack of 
supervision, and organizational issues. According 
to the HFACS -OGI framework, workers' mistakes 
are symptoms of organizational issues, not the 
causes themselves. Using Bayesian network 
analysis, the study concluded that unsafe behavior 
was not spontaneous but stemmed from limited 
communication and participation, and ineffective 
safety controls. Thus, improving the situation by 
focusing solely on workers' discipline is not an 
effective strategy (Manikumar et al., 2024; 
Nwankwo et al., 2022). 
When discussing the relevance of the results to 
the petrochemical industry, it is necessary to 
consider the industry's sensitivity to process 
deviations. Indeed, compared to most traditional 
manufacturing industries, petrochemical companies 
rely on stable processes and quick reaction to 
deviations in them. Since petrochemical operations 
involve flammable materials, complex chemical 
reactions, high pressures, and interconnected 
utilities, small defects can easily become 
significant threats to employees or processes 
(Alahjil et al., 2025. Thus, reporting of near misses 
within this study is to be regarded as a leading

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 521 
indicator rather than a lagging one. If near -miss 
reporting is limited, it will be much harder for 
companies to discover weaknesses in safety 
barriers (Chukwuma 2023). This conclusion aligns 
with the literature that distinguishes between the 
two types of safety indicators  (Pati 2023). 
About the safety culture maturity theory, the 
study results indicate that the investigated system's 
current safety culture is at an intermediate maturity 
level. Workers have relatively high levels of risk 
awareness, but safety communication and active 
participation have not yet developed to a sufficient 
level. The characteristics of mature safety cultures 
include openness to reporting, collective learning, 
consistent leadership and decision -making, and the 
integration of safety into decision -making 
processes. As stated by Foussard et al., 
improvements in safety performance in 
multinational oil and gas companies are attributable 
to a higher level of maturity in their safety culture. 
Other studies also showed that maturity levels 
presented opportunities for further improvement in 
safety performance in the oil and gas industry. 
Thus, the sensitivity analysis highlighting the 
importance of safety communication can be 
interpreted as necessitating an organization's shift 
from a reactive or compliance -oriented approach to 
a proactive or generative one  (Foussard et al., 
2025; Rahim et al., 2025; Yudiawan et al., 2025). 
Finally, safety behavior theory should also be 
discussed. In the oil and gas industry, employee 
safety behavior is usually determined by a variety 
of factors, including employees' knowledge and 
attitudes, the organizational environment, and 
system factors. According to the findings obtained 
by Quaigrain et al., compliance is determined by 
the first two factors mentioned. Guzman et al. also 
focused on the influence of occupational safety 
vulnerabilities and organizational environment on 
workers' safety. In addition, the study's findings 
revealed that this connection is unstable and 
depends on factors such as management 
commitment, safety communication, and 
participation. In other words, when all three 
factors improve simultaneously, the likelihood 
of safe behavior increases significantly (Haleem 
et al., 2025. In fact, it is why Bayesian Networks 
can be used to analyze the oil and gas industry 
and petrochemicals (Guzman et al., 2022; 
Quaigrain et al., 2022) . 
In addition, the interaction between safety 
culture and organizational performance warrants 
consideration. Bautista -Bernal et al. found that 
safety culture is related not only to safety 
performance but also to organizational 
performance. For the oil and gas industry, these 
findings mean that not only does poor safety 
culture increase injury risks, but it also poses 
threats of production losses, unplanned plant 
shutdowns, equipment damage, the cost of 
accident investigations, potential fines, and 
reputational damage. For petrochemical 
companies, even a small deviation can disrupt 
utilities, reactors, storage facilities, or loading/
unloading systems. Thus, the present study 
demonstrated that investing in safety culture is 
equivalent to investing in organizational success 
(Bautista -Bernal et al., 2024) . 
The topic of workplace fatigue deserves 
attention, especially in offshore operations, in long 
work schedules, and jobs requiring constant 
alertness. In their study, Wang et al. show a strong 
correlation between safety culture and the 
management of employee fatigue in the offshore oil 
and gas industry. In this research context, 
management commitment and safety 
communication could be seen as preconditions that 
enable fatigue, workload, and human resource 
capabilities to be perceived as elements of the 
safety culture rather than as individual issues for 
workers. Organizations lacking opportunities to 
discuss fatigue -related problems will be at risk of 
unsafe practices, even if employees' hazard 
awareness is quite high. This explains why the 
awareness of risks is not enough to ensure effective 
safety management  (Wang et al., 2024). 
On the governance and reporting side, the 
discussion is relevant to Pati's paper, which 
addresses sustainability reports and whether they 
reflect the level of organizational safety culture in 
the oil and gas and process sectors. In other words, 
formal safety indicators used in enterprise reporting 
cannot reveal the true quality of the safety culture 
implemented within the company. In the case under 
consideration, descriptive results and probabilities 
indicate a problem: deficiencies in safety

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
522 I DOI org/10.29017/scog.v49i2.2097 
communication go unnoticed in companies that 
focus solely on formal compliance and lagging 
statistics (Agustini et al., 2024. Hence, these results 
suggest that deeper indicators, such as near -miss 
reporting, safety voice, and control effectiveness, 
must be used to provide an accurate picture of 
organizational safety  (Pati 2023). 
From this perspective, it becomes clear that 
Indonesia's oil and gas industry needs a model for 
analyzing OSH culture that includes both the 
descriptive features of culture and the probability 
of relationships among its elements, while 
prioritizing interventions. Methodologically, the 
Bayesian Network used in the current research can 
serve as a tool for simulating scenarios to analyze 
what will happen if, for instance, organizations 
improve safety communication and increase the 
likelihood of successful operations (Asyik et al., 
2026; Nurdiansyah & Lestari 2026). 
Thus, the above discussion shows that OSH 
culture in the oil and gas and petrochemical 
industries constitutes a socio -technical system that 
affects operational reliability. Management 
commitment defines priorities; safety 
communication makes hazards audible; risk 
awareness helps workers identify deviations from 
established safety standards; and, finally, safety 
participation fosters learning processes. As a result, 
these four elements determine safe work behaviors, 
near-miss reports, effectiveness of controls, and 
operational safety conditions. Therefore, any 
strategy for improving OSH should focus on 
developing a culture of communication, a safety 
voice, cultural maturity, and the use of worker 
behavior data in operational systems. 
 
CONCLUSION 
Occupational safety and health (OSH) culture 
profoundly influences operational safety in the oil 
and gas and petrochemical sectors through 
systemic and probabilistic mechanisms. According 
to the analysis, the safety communication element 
is the most important variable influencing changes 
in the probability of creating and maintaining safe 
operating conditions in the industry, followed by 
management commitment, risk awareness, and 
safety participation. The identified factors shape 
safe work behavior and near-misses, which serve as 
mediators in the safety system under study. Thus, 
improvements in operational safety depend on 
much more than procedural measures; they require 
building a safety culture embedded in the safety 
management system and enabled by 
communication. For these reasons, it is 
recommended to focus on improving safety 
communication through transparent reporting 
systems, fostering a safety voice, and enhancing 
workers' participation in safety programs. 
Moreover, it is important to develop probabilistic 
methods for safety analysis (such as Bayesian 
Networks) as decision -support tools. Implications 
suggest that effective OSH management requires 
recognizing that it is part of a socio -technical 
system that influences business sustainability. 
 
ACKNOWLEDGMENT 
The authors would like to express their sincere 
gratitude to all individuals and institutions who 
contributed to the completion of this research. The 
authors also appreciate the support, guidance, and 
cooperation provided throughout the research and 
manuscript preparation process. 
 
DECLARATIONS 
The authors declare that this manuscript is 
original, has not been published previously, and is 
not under consideration for publication elsewhere. 
All authors have read and approved the final 
version of the manuscript and agree to its 
submission for publication. 
Author contributions 
Supardi contributed to the conceptualization, 
data collection, formal analysis, and preparation of 
the original manuscript draft. Samsudi, Arief 
Yulianto, and Suwito Eko Pramono contributed as 
supervisors through methodological guidance, 
validation, critical review, and manuscript editing 
throughout the research process. 
Funding Statement 
This research received no external funding.

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 523 
Competing interest 
The authors declare that they have no known 
competing financial interests or personal 
relationships that could have appeared to influence 
the work reported in this paper. 
Declaration of the use of AI and AI -assisted 
technologies 
During the preparation of this manuscript, the 
authors used AI -assisted technology to support 
language editing, translation, and improvement of 
grammar and readability. The authors carefully 
reviewed and revised the content and take full 
responsibility for the accuracy, integrity, and 
originality of the final manuscript. 
 
GLOSSARY OF TERMS AND SYMBOLS 
Terms & 
Symbols Definition  Unit 
OHS Occupational Health 
and Safety — the 
interdisciplinary field 
concerned with the 
safety, health, and 
welfare of workers in 
occupational settings 
 
OSH Occupational Safety 
and Health — used 
interchangeably with 
OHS in this study; 
refers to K3 
(Keselamatan dan 
Kesehatan Kerja) in 
the Indonesian 
regulatory context 
 
K3 Keselamatan dan 
Kesehatan Kerja — 
the Indonesian term 
for Occupational 
Safety and Health, as 
mandated under PP 
No. 50/2012 (SMK3) 
 
BN Bayesian Network — 
a probabilistic 
graphical model 
representing a set of 
variables and their 
conditional  
 
 
 dependencies via a 
directed acyclic graph 
(DAG) 
 
CPT Conditional 
Probability Table — a 
table that specifies the 
probability of each 
state of a node given 
all possible 
combinations of states 
of its parent nodes in 
the Bayesian Network 
 
DAG Directed Acyclic 
Graph — a graph in 
which edges have a 
direction and no 
directed cycles exist; 
forms the structural 
backbone of a 
Bayesian Network 
 
SMK3 Sistem Manajemen 
Keselamatan dan 
Kesehatan Kerja — 
Indonesian OHS 
Management System 
as mandated by 
Government 
Regulation No. 50 of 
2012 (PP No. 
50/2012) 
 
PPE Personal Protective 
Equipment — 
protective gear worn 
by workers to 
minimize exposure to 
occupational hazards 
(e.g., helmets, gloves, 
respirators, safety 
goggles) 
 
SOP Standard Operating 
Procedure — 
documented step-by-
step instructions 
designed to ensure 
consistent and safe 
execution of specific 
operational tasks 
 
HIRARC Hazard Identification, 
Risk Assessment, and 
Risk Control — a 
systematic method for 
identifying workplace 
hazards, evaluating 
associated risks, and 
implementing 
appropriate control 
measures

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
524 I DOI org/10.29017/scog.v49i2.2097 
HFACS-OGI Human Factors 
Analysis and 
Classification System 
— Oil and Gas 
Industry adaptation; a 
framework for 
classifying human 
factors that contribute 
to accidents in the oil 
and gas sector 
 
IOGP International 
Association of Oil and 
Gas Producers — 
global industry body 
that publishes safety 
performance 
indicators used as 
benchmarks in this 
study 
 
ILO International Labour 
Organization — a 
United Nations 
agency that sets 
international labour 
standards and collects 
global occupational 
safety data referenced 
in this study 
 
BPJS 
Ketenagakerjaan 
Badan Penyelenggara 
Jaminan Sosial 
Ketenagakerjaan — 
Indonesian Social 
Security 
Administering Body 
for Employment; the 
primary source of 
national occupational 
accident statistics in 
this study 
 
P(A|B) Posterior probability 
— the conditional 
probability of event A 
occurring given that 
event B has occurred; 
the primary output of 
Bayesian inference in 
this model 
 
P(B|A) Likelihood — the 
probability of 
observing evidence B 
given that hypothesis 
A is true; used in 
Bayes’ theorem to 
update prior beliefs 
 
P(A) Prior probability — 
the initial probability 
of hypothesis A 
before observing any 
 
 evidence; derived 
from survey data and 
literature in this study 
 
P(B) Evidence probability 
(marginal likelihood) 
— the total 
probability of 
observing evidence B 
across all possible 
hypotheses; acts as a 
normalizing constant 
in Bayes’ theorem 
 
Pa(Xᵢ) Parent node set of 
variable Xᵢ — denotes 
the set of direct 
predecessor nodes of 
Xᵢ in the Bayesian 
Network DAG; used 
in the joint probability 
factorization formula 
 
P(Safe) Probability of safe 
operational condition 
— the inferred 
probability that the 
operational safety 
node is in the “Safe” 
state given observed 
evidence in the 
Bayesian Network 
 
P(Unsafe) Probability of unsafe 
operational condition 
— the complement of 
P(Safe); represents the 
likelihood that 
operational safety 
conditions are 
hazardous given 
current evidence 
states 
 
Near-miss An unplanned event 
that did not result in 
injury, illness, or 
damage but had the 
potential to do so; 
used as a leading 
safety indicator and 
proactive reporting 
metric in this study 
 
SIMOPS Simultaneous 
Operations — 
concurrent execution 
of multiple activities 
in close proximity, 
presenting 
compounded safety 
risks that require 
heightened

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 525 
 heightened 
communication and 
coordination 
 
Likert scale A five-point 
psychometric rating 
scale (1 = Strongly 
Disagree to 5 = 
Strongly Agree) used 
in this study to 
quantify respondents’ 
perceptions of OHS 
culture and 
operational safety 
 
Cronbach’s 
Alpha (α) 
A coefficient of 
internal consistency 
reliability; values ≥ 
0.7 indicate 
acceptable reliability 
of the research 
instrument, as applied 
in this study’s validity 
and reliability testing 
 
SEM Structural Equation 
Modeling — a 
conventional 
multivariate statistical 
method; contrasted 
with the Bayesian 
Network approach in 
this study due to its 
assumption of linear 
relationships 
 
BUMN Badan Usaha Milik 
Negara — Indonesian 
state-owned 
enterprise; refers to 
government-owned 
companies such as PT 
Chandra Asri 
Petrochemical and PT 
Krakatau Steel 
included in this 
study’s sample 
context 
 
 
 
REFERENCES 
Agustini, Kusnoputranto, H., & Hartono, D. M. 
(2024). Korelasi Penyebaran Emisi SO 2 
Industri Pengilangan Migas dengan Kualitas 
Lingkungan Udara di Sekitarnya Correlation 
between Dispersion of SO 2 Emissions from 
The Oil and Gas Re nery with The Surrounding 
Air Quality. Lembaran Publikasi Minyak Dan 
Gas Bumi, 48(1), 23–32. 
Alahjil, R. A. A., Jaafar, M. H., Zuknik, M. H., 
Firdaus, R. B. R., & Ibrahim, A. M. (2025). the 
Impact of Physical, Chemical and Biological 
Hazards on Occupational Accidents and 
Illnesses in the Oil and Gas Industry – a 
Review. Journal of Sustainability Science and 
Management, 20(6), 1344–1363. https://
doi.org/10.46754/jssm.2025.06.013 
Asyik, N., Latief, R. U., & Burhanuddin, S. (2026). 
Risk-Informed Strategic Governance in Precast 
Concrete Production as A High Risk Industry : 
Cross - Sector Evidence from The Construction 
and Oil & Gas Industries. Scientific 
Contributions Oil and Gas , 49(1), 459 –474. 
https://doi.org/10.29017/scog.v49i1.195. 
Bautista-Bernal, I., Quintana -García, C., & 
Marchante-Lara, M. (2024). Safety culture, 
safety performance and financial performance. 
A longitudinal study. Safety Science, 172, 
106409. https://doi.org/https://doi.org/10.1016/
j.ssci.2023.106409 
Blanco-Juárez, J., & Buele, J. (2025). Industrial 
Safety Strategies Supporting the Zero Accident 
Vision in High -Risk Organizations: A Scoping 
Review. In Safety (Vol. 11, Issue 4, p. 101). 
https://doi.org/10.3390/safety11040101 
Chukwuma, O. I. (2023). The Impact of Safety 
Culture on Workers ’ Safety Performance in the 
Nigerian Oil and Gas Industry. European 
University of Cyprus (Cyprus). 
D’Antoine, E., Jansz, J., Barifcani, A., Shaw -Mills, 
S., Harris, M., & Lagat, C. (2023). Psychosocial 
Safety and Health Hazards and Their Impacts on 
Offshore Oil and Gas Workers. In Safety (Vol. 
9, Issue 3, p. 56). https://doi.org/10.3390/
safety9030056 
Djunaidi, Z., Wirawan, M., Susilowati, I. H., 
Khaliwa, A. M., & Kanigara, S. A. (2024). 
Safety Climate Transformation in Oil and Gas 
Company Ownership Transition (Study Case 
from Multinational to National Company). 
Safety and Health at Work, 15(3), 292–299. 
https://doi.org/https://doi.org/10.1016/

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 509-527 
 
526 I DOI org/10.29017/scog.v49i2.2097 
j.shaw.2024.04.009 
Ehiaguina, E., Nnadi, B. C., Rangarajan, R., & 
Moda, H. M. (2024). Safety culture assessment 
in petroleum industry: cross sectional survey of 
workers safety performance in the Niger Delta 
Region, Nigeria. Safety in Extreme 
Environments, 6(3), 235–247. https://
doi.org/10.1007/s42797-024-00104-z 
Foussard, C., Ellias, B., van Wassenhove, W., & 
Denis-Rémis, C. (2025). Enhancing Safety 
Performance through Cultural Maturity: A 
Comprehensive Framework for Multinational 
Oil and Gas Operations. European Safety and 
Reliability (ESREL) and Society for Risk 
Analysis Europe (SRA-E) 2025. 
Guzman, J., Recoco, G. A., Pandi, A. W., 
Padrones, J. M., & Ignacio, J. J. (2022). 
Evaluating workplace safety in the oil and gas 
industry during the COVID -19 pandemic using 
occupational health and safety Vulnerability 
Measure and partial least square Structural 
Equation Modelling. Cleaner Engineering and 
Technology, 6, 100378. https://doi.org/https://
doi.org/10.1016/j.clet.2021.100378 
Haleem, A., Javaid, M., & Singh, R. P. (2025). 
Encouraging Safety 4.0 to enhance industrial 
culture: An extensive study of its technologies, 
roles, and challenges. Green Technologies and 
Sustainability, 3(3), 100158. https://doi.org/
https://doi.org/10.1016/j.grets.2024.100158 
Houette, B., & Mueller -Hirth, N. (2022). Practices, 
preferences, and understandings of rewarding to 
improve safety in high -risk industries. Journal 
of Safety Research, 80, 302–310. https://doi.org/
https://doi.org/10.1016/j.jsr.2021.12.013 
Ihsan, T., Sajidah, H., Edwin, T., & Derosya, V. 
(2025). Identification and Control of OHS Risks 
in the CPO Production Process using the 
HIRARC Method . Jurnal Kesehatan Komunitas 
(Journal of Community Health), 11(1 SE -
Articles), 120–130. https://doi.org/10.25311/
keskom.Vol11.Iss1.2107 
Jamil, Z., Nordin, S., Miraj, M., Alqahtani, M., 
Shaik, R. A., Akhter, S., & Nizam Isha, A. S. 
(2025). Sustainable safety practices and hazard 
management in the oil and gas industry: an HSE 
perspective. Frontiers in Public Health, 13, 
1611106. 
Jasmadi, J., Sugiarto, S., & Ramli, S. (2025). 
Analysis Implementation Safety Management 
System Oil and Gas and Safety Culture That 
Influence on Safety Performance and Worker 
Motivation To Work Safely. Dinasti 
International Journal of Education Management 
and Social Science, 7(1 SE -Articles), 1189–
1199. https://doi.org/10.38035/
dijemss.v7i1.5598 
Manikumar, D., Raju, T. B., & Sharma, U. (2024). 
Analysis of Accidents in the Oil and Gas 
Industry in Kuwait. International Journal of 
Safety and Security Engineering, 14(3), 893–
905. https://doi.org/10.18280/ijsse.140321 
Mathisen, G. E., Tjora, T., & Bergh, L. I. V. 
(2022). Speaking up about safety concerns in 
high-risk industries: Correlates of safety voice 
in the offshore oil rig sector. Safety Science, 
145, 105487. https://doi.org/https://
doi.org/10.1016/j.ssci.2021.105487 
McKinnon, R. C. (2025). Implementation of an 
Occupational Health and Safety Management 
System. The Design, Implementation, and Audit 
of Health and Safety Management Systems, 
Second Edition, October, 19–28. https://
doi.org/10.1201/9781003584568-5 
Miloševiæ, I., Stojanoviæ, A., Nikoliæ, Ð., 
Mihajloviæ, I., Brkiæ, A., Perišiæ, M., & 
Spasojeviæ-Brkiæ, V. (2025). Occupational 
health and safety performance in a changing 
mining environment: Identification of critical 
factors. Safety Science, 184, 106745. https://
doi.org/https://doi.org/10.1016/
j.ssci.2024.106745 
Naji, G. M. A., Isha, A. S. N., Alazzani, A., 
Saleem, M. S., & Alzoraiki, M. (2022). 
Assessing the Mediating Role of Safety 
Communication Between Safety Culture and 
Employees Safety Performance. Frontiers in 
Public Health, Volume 10. https://
www.frontiersin.org/journals/public-health/
articles/10.3389/fpubh.2022.840281 
Niu, Y., Fan, Y., & Li, Y. (2023). Safety 
performance measurement in collectivized oil

Probabilistic Modeling of Occupational Health and Safety Culture Influence on Operational Safety 
in Petrochemical and Oil and Gas Facilities Using Bayesian Networks(Supardi et al.) 
 
DOI org/10.29017/scog.v49i2.2097  I 527 
companies in China: Contribution of leading 
indicators to lagging indicators. Journal of Loss 
Prevention in the Process Industries, 83, 
105090. https://doi.org/https://doi.org/10.1016/
j.jlp.2023.105090 
Nurdiansyah, W., & Lestari, F. (2026). Improving 
Safety Awareness in the Workforce Through 
Education and Programs : A Scoping Review. 
Scientific Contributions Oil and Gas , 49(1), 513
–524. https://doi.org/10.29017/scog.v49i1.204. 
Nwankwo, C. D., Arewa, A. O., Theophilus, S. C., 
& Esenowo, V. N. (2022). Analysis of accidents 
caused by human factors in the oil and gas 
industry using the HFACS -OGI framework. 
International Journal of Occupational Safety and 
Ergonomics, 28(3), 1642–1654. https://
doi.org/10.1080/10803548.2021.1916238 
Okon, O. S., Gift, C.-O., & Osazuwa, C. M. (2025). 
Prevalence And Patterns Of Workplace 
Accidents In Selected Oil Servicing Companies 
In Port Harcourt, Nigeria. Emerging Frontiers 
Library for The American Journal of Social 
Science and Education Innovations, 7(10), 23–
47. 
Pati, S. (2023). Sustainability reporting pathway – 
Is it a true reflection of organisational safety 
culture: Insights from oil and gas and process 
sector of India. Safety Science, 159, 106006. 
https://doi.org/https://doi.org/10.1016/
j.ssci.2022.106006 
Quaigrain, R. A., Owusu -Manu, D. -G., Edwards, 
D. J., Hammond, M., Hammond, M., & Martek, 
I. (2022). Occupational health and safety 
orientation in the oil and gas industry of Ghana: 
analysis of knowledge and attitudinal influences 
on compliance. Journal of Engineering, Design 
and Technology, 22(3), 795–812. https://
doi.org/10.1108/JEDT-11-2021-0664 
Rahim, H., Dom, N. C., & Dapari, R. (2025). 
Safety Culture Maturity Assessment: Insights 
and Improvement Opportunities for the Oil and 
Gas Sector. Malaysian Journal of Medicine & 
Health Sciences, 21(5). 
Salleh, F., Darwsih, S., Chadran, S., Johari, S. A. 
M., Mohamed, N. A., Arumugam, S., & Afandi, 
M. S. H. (2024). Improving Occupational Safety 
and Health (OSH) Culture in the Oil and Gas 
Industry Management Through Sustainable 
Development Goals (SDGs). In Business 
Development via AI and Digitalization: Volume 
2 (pp. 899–909). Springer. 
Silva, C. M. I. da, & Amaral, F. G. (2025). Study 
on safely working in confined spaces in the 
petroleum industry: Risk factors, current control 
procedures, and alternatives. Journal of 
Industrial Safety, 2(2), 90–98. https://doi.org/
https://doi.org/10.1016/j.jinse.2025.04.005 
Skiba, R. (2025). Frameworks and models for 
working safely and health and safety training in 
vocational education and training for High -Risk 
occupations. 
Tribuana, I. Y., Mulyadi, U., Ramdhan, A. M., & 
Rustam, A. H. (2018). Pore Pressure Estimation 
in Hard Unloading -Overpressure Zone Using 
Single Compaction Equation, Case Study: 
Lower Kutai Basin. Scientific Contributions Oil 
and Gas, 39(2), 77–90. https://doi.org/10.29017/
scog.39.2.105 
Wang, X., Sasangohar, F., Payne, S., & Mehta, R. 
K. (2024). Safety culture and worker fatigue 
management in the offshore oil and gas 
industry: An interview study. International 
Journal of Industrial Ergonomics, 102, 103614. 
https://doi.org/https://doi.org/10.1016/
j.ergon.2024.103614 
Yudiawan, R., EDDYONO, F., & POERNOMO, 
M. I. (2025). The Influence of Culture 
Implementation and Maturity Level on OHS 
Performance in The Upholstery Oil and Gas 
Company Citic Seram Energy Limited. 
International Journal of Environmental, 
Sustainability, and Social Science, 6(6), 1349–
1357.
