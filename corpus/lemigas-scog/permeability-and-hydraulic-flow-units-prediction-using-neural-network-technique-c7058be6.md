---
source_id: "lemigas-scog"
title: "Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique of The Clastic Mamuniyat Reser"
summary: "Study using neural networks to predict permeability and hydraulic flow units in the clastic Mamuniyat reservoir of the Murzuq Basin, Libya."
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2035"
retrieved_at: "2026-10-24T14:30:41+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "c7058be68aeaa79231a0fdd2ce0ad3db95f551de5e66fc1e2f5f3e9de5c29969"
collected: "manual"
---

# Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique of The Clastic Mamuniyat Reser

DOI org/10.29017/scog.v49i2.2035 I 45 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Permeability and Hydraulic Flow Units Prediction Using Neural Network 
Technique of the Clastic Mamuniyat Reservoir (Upper Ordovician), 
Murzuq Basin-Libya 
Bahia M. Ben Ghawar1, Fathi M. Salloum2, Mahmud A. Al Tarhouni1, and Mousa G. El Shamli1  
ABSTRACT - Delineation of the hydraulic flow unit (HFU) and a petrofacies parameter (R 35) are essential 
reservoir characteristics, which are functions of the routine core analysis (CCA) and well log data. Thus, 
this work has been carried out with the Neural Network (NN) application to predict the HFU, pore size 
radius (R 35), and permeability (KHFU) in uncored well 3 within an average thickness of 133 feet of the 
clastic Mamuniyat reservoir Murzuq basin (Libya). This prediction is based on data of two wells (1 and 2) 
producing from the same reservoir. Hence, log analysis demonstrates about 12% effective porosity (Øe) and 
not exceeding 14% of the shale content (V sh). Also, 11% and 96 mD are averages of core porosity (Øcore) 
and permeability (Kcore), respectively. Whereas micropores, mesopores, and macropores are three pore 
throat radius (R 35) classifications recognized in the reservoir and six HFUs in well 1 and five in well 2. 
Furthermore, gamma ray (GR) logs correlate among three wells and reveal a similarity between wells 1 and 
3 that sustain the HFUs of well 3 by using the NN model. Whereas, the comparison between the predicted 
KHFU and two approved empirical permeability Equations manifests furnishing high agreement results 
with some exceptions. However, the NN provides predictions supported by data of Mamuniyat reservoir 
quality (HFU, R35, and K) within the uncored reservoir section from the nearby wells that reveal consistent 
and reliable results.    
Keywords: neural network; permeability; sandstone; mamuniyat; hydraulic flow unit.  
 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 45 - 60 
1University of Tripoli, College of Engineering, Geological Engineering Department, 
University Road (Thariq al-Jami'a), Al-Furnaj, 13932, Tripoli, Libya. 
2University of Benghazi, Faculty of Science, Earth Sciences Department, 
Aruba Street, 3333+W63, Benghazi, Libya.  
Corresponding author: Bahia M. Ben Ghawar (B.Ben-Ghawar@uot.edu.ly ) 
Manuscript received:  February 26th, 2026; Revised: March 13th, 2026 
Approved:  March 16 th, 2026; Available online: June 04th, 2026; Published: June 04th, 2026. 
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Bahia M. Ben Ghawar, Fathi M. Salloum, Mahmud A. Al Tarhouni,  and Mousa G. El Shamli, 
2026, Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique of 
the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin -Libya, Scientific 
Contributions Oil and Gas, 49 ( 2) pp. 45-60. DOI org/10.29017/scog.v49i2.2035.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
46 I DOI org/10.29017/scog.v49i2.2035 
INTRODUCTION 
The Reservoir characterization plays an 
important role in the distribution of formation and 
fluids properties within the heterogeneous 
reservoirs. Defining of rock types and pores 
geometry are essential part of reservoir 
characteristic. Also, both the deposition 
environment and diagenetic history have mainly 
impact on the pore geometry, which in turn 
controls on effective porosity and permeability of 
reservoir rocks. However, core samples and well 
logs are considerable source data for storage and 
flow capacity assessment of reservoir rocks in oil 
fields. Thus, hydraulic flow unit (HFU) is a 
technique concept introduced by (Ebanks Jr 1987)  
who has defined a hydraulic unit as a mappable 
portion of reservoir within the geological and 
petrophysical properties of other reservoir volumes. 
Whereas, Hearn et al. (1984)  has defined a flow 
unit as, a reservoir zone that is laterally and 
vertically continuous and has similar permeability, 
porosity and bedding characteristics. Gunter et al. 
(1997) has defined a flow unit as stratigraphically 
continuous interval of similar reservoir process that 
honors the geological framework and maintains the 
characteristics of rock types. Moreover, flow zone 
indicator (FZI) is another unique parameter that 
includes the geological attribution of the texture 
and mineralogy of distinct pore, with geometrical 
filling materials. Furthermore, Winland correlation 
is another technique to classify reservoir rock 
based on pore size radius (R 35) (Winland 1972) . 
Also, this petrofacies parameter (R 35) perfectly 
correlate with the HFU. Hence, these techniques 
essentially depend on the porosity (Ø core) and 
permeability (K core) that are measured by core 
samples, which may not be available in all the 
exploration and development wells. On the other 
hand, artificial intelligence tools (neural networks, 
NN) are a good alternative technique that has made 
a significant contribution to oil fields' performance 
in the petroleum industry in recent decades. The 
NN is based on supervised training algorithms 
(Mohaghegh 2000) that provides a high uncertainty 
and without consumption of time and costing to 
predict a property. Therefore, application of the 
NN technique has been applied by many 
researchers such as ( Hamzah et al., 2021 ; Usmanet 
al., 2010 ; and Wahyudi et al., 2025) . In the same 
manner, many published studies have been carried 
out, and described the rock type that defines HFU 
by Global Hydraulic Elements (GHE). Ha et al. 
(2021) present the same GHE work of a deltaic 
facies (Miocene formation) at Eastern Poland. 
Whereas, Khalid et al. (2020) utilized the hydraulic 
flow unit (HFU) to predict the permeability of un 
cored wells of JG field (Abu El -Gharadig basin), 
and enhanced the reservoir characteristics by 
integration between core and well logs data. 
Accordingly, Mamuniyat Formation (Upper 
Ordovician) is a clastic potential reservoir rock in 
the intracratonic Murzuq basin (southwest Libya), 
which subjects to describe the rock type as the 
HFU by Global Hydraulic Elements (GHE) by 
(Salaheddin 2010 ; and Castro et al., 2012) . Also, 
These HFU's of the Mamuniyat reservoir were 
defined within wells have core and logs data. It 
worth mentioning that the Castro et al., 2012  have 
documented that the Mamuniyat reservoir 
illustrates changing of the porosity and 
permeability, with their impact on the global 
hydraulic elements (GHE) that have low porosity 
and permeability.  
Consequently, our present work will utilize 
Interactive Petrophysics software (version 2018) to 
build NN model that provide the hydraulic flow 
units (HFU), and predict the permeability (K HFU) 
of the Mamuniyat reservoir in un cored well 3. This 
NN model is based on two wells (1 and 2), that 
have core and log data. In addition, defined the 
studied reservoir quality assessment by hydraulic 
pore radius (R35). 
Geological setting 
The present geologic borders of the Murzuq 
basin are delimited by tectonic uplifts. The present-
day structural framework is a consequence of the 
cumulative tectonic movements ranging from 
Palaeozoic through to Tertiary times. The main 
tectonic events are related to the Caledonian (late 
Silurian-early Devonian), Hercynian (end 
Carboniferous-Permian) and Alpine (early 
Tertiary) orogenies. Although the present -day

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 47 
structuring is related mostly to Hercynian 
compressional movements and the later tectonic 
activity, the regional lineaments (NW -SE) are 
probably related to late Precambrian Pan -African 
fault systems, which largely controlled the early 
Palaeozoic structural and depositional evolution of 
this basin (Hallett & Clark-Lowes 2016).  
Mamuniyat Formation complex interplay 
between eustatic and isostatic controls (El -ghali 
2005). Periglacial and postglacial fluvial and 
marine environments gave rise to heterogeneity in 
reservoir character (Figure 1b). Distribution and 
thickness of the Mamuniyat reservoir facies in the 
Murzuq basin are poorly defined (Cubitt et al., 
2011). Previous drilling together with rock 
outcrops studies suggests that the clastic formation 
may be sub -divided into two upward -coarsening 
cycles. The lower part of each cycle is represented 
by widespread, fine -grained (shaly) marine facies 
representing a transgressive phase (Shalbak 2015). 
These coarsening upwards into progradational 
highstand deposits in which facies become 
increasingly isolated (channelised). However, three 
oil wells (1, 2 and 3) are utilized within this 
work, they are belonging to an oil field NC186, 
located in the south -west side of Murzuq Basin, 
Libya (Figure 1a) . 
 
METHODOLOGY 
Many scientists and engineers have dedicated 
extensive efforts to developing models for 
predicting the permeability of reservoir rocks, often 
integrating well logs (continuous data) with core 
data. This integration provides continuous 
predicted permeability for uncored depth intervals 
of potential hydrocarbon-bearing reservoir sections 
(Zhang et al. 202; and Mahmoud et al., 2019). 
Also, Mohamed & Kashlaf (2016) had adopted and 
made a quick petrophysical interpretation of the 
Hawaz formation (Middle Ordovician) by using 
logs and core analysis data, leading to the 
prediction of more than one HFU. However, well 
logs and routine core analysis (CCA) are essential 
data utilized to estimate the permeability of 
reservoir rocks (Yogi 2018). Hence, well logs 
package and CCA data of two wells have been 
analyzed to define the hydraulic flow unit (HFU) of 
the Mamuniyat reservoir, and utilized to predict 
permeability in the unscored well No 3. These 
Figure 1. a). Location map of Murzuq basin, and b). Sequence stratigraphy of the Mamuniyat Formation (after Shalbak 
2015; Hallett & Clark-Lowes 2016). 
 
b) 
a)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
48 I DOI org/10.29017/scog.v49i2.2035 
𝑉𝑠ℎ = 0.33 ×  22×𝐼𝐺𝑅 − 1  
(2)  
𝐼𝐺𝑅 =   𝐺𝑅𝑙𝑜𝑔− 𝐺𝑅𝑚𝑖𝑛  𝐺𝑅𝑚𝑎𝑥−  𝐺𝑅𝑚𝑖𝑛   
(1)  
wells are producing from the Mamuniyat reservoir 
(Upper Ordovician) that has a thickness of 40.6 
meters (133.33 feet). Also, the measured well logs 
package are including; Gamma Ray (GR), 
spectmetry (NGS), neutron porosity (Øn), bulk 
density ( ρb), and interval travel time ( ΔT). 
Therefore, the basic petrophysical evaluation is 
dependent on both the processed logs and core data 
to assess any reservoir rocks (Novita et al. 2022. 
Thus, in order to predict the required permeability 
(k) there would be a basic petrophysical evaluation, 
including shale volume (Vsh), effective porosity 
(Øe), water saturation (Sw), and permeability (k). 
Whereas, the CCA data are also processed to 
provide the HFU and pore throat radius (R 35) of the 
studied reservoir. Thus, Figure (2) summarizes the 
workflow of this study. 
Petrophysical evaluation 
The shale volume (V sh) is an essential 
estimation parameter used for porosity correction 
and delineating the net pay thickness of reservoir 
rocks. The GR logs are the most providing shale 
content parameter, and define the clay minerals that 
may exist in the rock composite as may explored 
by the spectrometry (NGS) logs. Therefore, 
Equations 1 and 2 (Asquith and Gibson 1982a were 
used to process the measured GR logs and calculate 
the volume of shale (Vsh) as follows: 
where: GRlog = gamma₋ray log value for shaly sand 
API; GR min = gamma ₋ray minimum value for 
clean sand API; GR max = gamma ₋ray maximum 
value for shale zone API; and V sh = volume of 
shale for older formations (fraction). 
Porosity gives an important physical rock 
property, and it gives an idea about a storage 
capacity of reservoir rocks that required to reserve 
estimation of oil fields in static and dynamic status. 
Hence, total and effective porosity are two 
distinctive porosity types, which has controlled 
flow capacity of the reservoir rocks. The porosity 
could be measured from core samples or different 
wire lines techniques. The neutron (Øn), bulk 
density (ρb) and interval travel time ( ΔT) are three 
wirelines porosity indicators. In addition, the 
neutron (Øn) log is a direct measured porosity 
values of rocks, which is sensitive to the presence 
of shale content by an increasing log reading. 
While the bulk density (ρb) and interval travel time 
(ΔT) are indirect porosity logs that use Equations 
to calculate the density and sonic porosity, also to 
demonstrate the clayey content influence and rocks 
overburden. Therefore, Equations 3 and 4 (Asquith 
and Gibson 1982b are used to calculate the density 
porosity (Ød) and total porosity (Øt). Further, the 
permeability (K) is another significant physical 
property of rocks that describes the ability of fluid 
flow through the effective porosity (Øe). 
Accordingly, elimination of the shale content from 
the calculated total porosity (Øt) or density 
porosity (Ød) will provide the effective porosity 
(Øe) by Equation 5 (Asquith and Gibson 1982a. 
However, there are many published empirical 
Equations can be used to assess the permeability 
Figure 2. Workflow chart of the study procedures.

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 49 
Log  RQI = Log FZI + Log(Øz) 
(11)  
Øt = (Øn + Ød)/2 
(4)  
Øe = Øt × 1− Vsh  
(5)  
𝑘1/2 = 250 Ø3
𝑆𝑤𝑖𝑟𝑟 ,  Swirr = 
𝑎 ∅𝑚 
2000  
(6)  
K =  4 × 107 ×∅7.2044  
(7)  
Ød = (ρbma −ρblog )/(ρbma −𝜌𝑓) 
(3)  
(K). Babadagli & Al -Salmi 2004 have summarized 
methods applied to estimate the permeability in 
carbonate reservoir rocks. Also, Ahmed et al., 
1991; and Alkinani et al., 2019 present a literature 
review of different permeability estimation 
techniques and discussed most most influencing 
factors. Whereas, Mohammed 2020 illustrates Tiny 
Permll device techniques for permeability 
determination, and diagenesis process that affecting 
the physical property of sandstone reservoirs, as 
well as a Permian Rotliegend Sandstone Formation 
as a case study. In general, Wyllie & Rose 1950 
have applied permeability empirical Equation 6 
that depend on well logs data, that are functioning 
on rock properties such as porosity, Archie 
parameters; tortuosity factor (a) and cementation 
factor (m), and irreducible water saturation (Swirr). 
On the other hand, Ghawar et al., 2026 is another 
attempt applying an empirical Equation 7 of the 
Mamuniyat reservoir (Upper Ordovician). 
where: ρma = apparent matrix density for sandstone 
(equal to 2.65 g/cc), ρblog = bulk density log 
reading (g/cc), ρf = fluid density (equal to 1 g/cc 
for fresh drilling mud), Øn = neutron porosity log 
reading (fraction), Ød = density porosity (fraction), 
Øt = total porosity (fraction), Øe = effective 
porosity (fraction), Swirr = irreducible water 
saturation, fraction, a = tortuosity, and m = 
cementation factor. 
Statistical analysis is necessary for the uncertainty 
evaluation when applying any empirical Equation, 
which provide a confidently and widely 
utilization of this Equation. Thus, average 
values of the calculated petrophysical properties 
(Vsh, Øt, Øe, and, Øcore) of each well could be 
calculated by Equation 8.      
where: Xaverage = average of the petrophysical 
property, X = calculated petrophysical property, h= 
thickness of each property, and Ʃ is the summation 
of property value.   
Hydraulic flow unit (HFU) and R35 
determination 
The routine core analysis (CCA) is a principle 
measured data of the HFU and Winland parameter 
(R35) determination of the Mamuniyat reservoir 
rock. including the porosity (Øcore), horizontal and 
vertical permeability (Kh and Kv), respectively. 
Hence, Equations 9 and 10 were applied to 
calculate Rock quality index (RQI) and flow zone 
index (FZI) of the studied reservoir within the wells 
1 and 2. Where the FZI is a function of normalized 
porosity (Øz), which is a pore volume to grain 
volume ratio. Then, reordering Equation 10 by 
picking the logarithm of both sides, as a linear 
Equation form (Equation 11). Thus, cross plot 
between the RQI and FZI produce multi -straight 
lines that have the same pore throat. These lines 
provide an empirical Equation to predict the 
permeability for each FZI value of each HFU zone. 
Furthermore, Winland parameter (pore throat 
radius, R 35) is another technique used to 
discriminate and classify lithofacies within the 
reservoir rocks based on the pore size.  Also, 
Equation (12) could be used to calculate the pore 
throat radius (R 35) of the Mamuniyat reservoir.   
𝑋𝑎𝑣𝑒𝑟𝑎𝑔𝑒 =    𝑋 ×ℎ  ℎ  
(8)  
RQI = 0.0314 K/Ø 
(9)  
FZI = RQI/Øz ; Øz =
Ø
(1−Ø) 
(10)  
Log R35 = 0.732 + 0.588 Log K− 0.864 Log ∅ 
(12)  
where: Ø = porosity (fraction), K = permeability 
(mD), FZI is flow zone indicator ( μm), Øz = 
normalized porosity, and R 35 = Winland 
parameter ( μm).

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
50 I DOI org/10.29017/scog.v49i2.2035 
Neural network technique application 
The neural network (NN) technique, invented 
by McCulloch & Pitts (1943) on the basis of a 
simplified biological process, is a flexible 
mathematical structure capable of describing 
complex non -linear relations between input and 
output of the data sets. Supervised and 
unsupervised are two categories of NN based on 
training methods. All applications of NN in the oil 
and gas industry are based on supervised training 
algorithms, which are divided into three main 
steps: training, calibration and verification 
(Mohaghegh 2000). However, in the Mamuniyat 
reservoir the NN model is constructed by the IP 
Software with one input layer, one hidden layer 
and one output layer. The trial zones were selected 
in front of input data curves; GR, Øe, Øcore, 
Kcore, FZI, HFU, Øn, and ρb at different depths of 
the studied reservoir within two trail wells 1 and 2. 
Training passes, epoch per pass and cross -
validation percentage are three training settings of 
the NN technique. The training passes specify how 
many times the NN will be trained each time, and 
in this case, it was 3. The epoch per pass shows 
how frequent training data will be interpreted in 
this case, it was found to be 100. The cross -
validation percentage of the input data defines how 
much the training data cross -check to process, and 
this was 5%. Epochs trained, the epoch of best cost 
and raw sensitivity are four outputs of the training 
settings.  Therefore, after training the tool many 
times, resulted building the NN model. Then, this 
created NN model will run automatcialy to yield 
the HFU in the wells.   
 
RESULT AND DISCUSSION 
Processing of well logs and CCA data provide a 
set of results required to predict the permeability 
from the HFU. Therefore, Table 1 summarized the 
average values of the essential calculated 
petrophysical properties (V sh, Øt, and Øe) of the 
Mamuniyat reservoir. Generally, the percentage of 
the volume of shale does not exceed 20%, and Well 
3 has a higher average value of the V sh than wells 1 
and 2. This variety of the shale content has the 
material caused the average total porosity (Øt) does 
not reach 20%, and the effective porosity is about 
15%. Also, the comparison procedure between 
measured core and calculated log porosity is an 
important step for reservoir evaluation. Hence, 
Figure 3 displays an accepted match of the 
measured core porosity (Øcore) and the calculated 
total and effective porosity results of well 1 and 2. 
As earlier stated, no core data for well 3. Thus, 
generation of relationship between the core 
permeability and porosity of well 3 is helpful to 
predict permeability of un cored reservoir depth 
intervals. Therefore, Figure 4 displays a cross plot 
between the measured core permeability (Kcore) 
and the porosity (Øcore) of wells 1 and 2 which do 
not exceed 70% of regression coefficient (R2). 
   Application of the Kolodzie (1980) to 
estimate the Winland parameter (R 35), provide a 
contribution indicator of the HFU of the 
Mamuniyat reservoir. Hence, the reservoir includes 
three pore throat sizes classification; micropores, 
mesopores, and macropores based on the results of 
the pore size radius (R 35). The micropores and 
macropores classification are presented in well 2, 
as well as the minor presence of the mesopores 
pore throat sizes, while well 1 concerned with the 
three pore throat radius classifications. Thus, two 
reasons could be referred to the minor presence of 
the mesopores pore throat sizes in well 2, that may 
be attributed to depositional heterogeneity of the 
Mamuniyat reservoir as reported by Castro et al. 
(2012); Fello (2001); Fello & Turner (2004); 
Salaheddin et al. (2010); and (Shalbak 2015). Also, 
a rich quartz mineral in the Mamuniyat sandstone 
(El-ghali et al. 2006  may cause the elimination of 
the mesopores pore throat sizes. However, the pore 
size radius (R35) versus core permeability is widely 
Table 1. Summary of avalues of the petrophysical 
properties of the Mamuniyat reservoir. 
 
Wells 
Average 
1 2 3 
h (ft) 181 99 120 133.33 
Vsh, % 13.7 12.00 14.61 13.46 
Øt, % 11.3 11.04 13.56 11.96 
Øe, % 11.5 11.39 12.08 11.68 
Øcore, % 13.1 10.85 UC 10.87 
Kcore, mD 116.7 75.83 UC 96.29 
 
UC = Un cored

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 51 
applied in limestone and sandstone reservoir rock 
several local oil field, this provides a linear 
empirical Equation (Lala and El -Sayed 2017. 
Accordingly, Figure 5 discloses a good linear 
relationship between the core permeability and 
pore throat radius of wells 1 and 2, with a high 
regression coefficient (R 2) equal to 0.9806 of the 
Mamuniyat reservoir. Also, on Figure 4 manifests a 
combined correlations of wells 1 and 2 between the 
Kcore, Øcore, and R 35 of the Mamuniyat reservoir. 
These correlations disclose and conformably 
emphasis between the permeability ranges and the 
pore throat sizes classification in wells 1 and 2. On 
the same procedure, cross plot between the core 
porosity and R 35 of well 1 and 2 reveals more 
scatter plotting points of well 2 than well 1 (Figure 
6). This high linearity of plotting points in well 1 
yield an ability to derive an empirical Equation for 
predicting the R35 in well 3.  
 
Figure 3. Overlay between the core (Øcore) and calculated porosity (Øt and Øe) of wells 1 and 2. 
 
Log-Log plots of the reservoir quality index 
(RQI) and normalized porosity (Øz) of the 
Mamuniyat reservoir within the two wells 1 and 2 
are shown on Figures 7a and 8a. These plots are 
constructed by the Interactive Petrophysical (IP) 
Software that reveal  well 1 has six hydraulic flow 
unit (1, 2, 3, 4, 5, and 6), while well 2 contains five 
(1, 2, 3, 5, and 6) of HFUs. Therefore, 
reconstruction of the core permeability (Kcore) and 
porosity (Øcore) cross plots (Figs. 7b and 8b) were 
based on the HFU of each well. Thus, the lines of 
each HFU that has an empirical Equation as 
summarized in Table (2) for permeability 
prediction against the hydraulic flow unit in wells 1 
and 2. However, the Castro et al. (2012 have 
documented heterogeneity of the Mamuniyat 
formation due to variation in vertical and lateral 
depositional flow regime resulting variations in 
porosity, permeability and regional hydraulic 
element (GHE) distribution.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
52 I DOI org/10.29017/scog.v49i2.2035 
Figure. 4. Core permeability versus core porosity and permeability versus pore throat radius (R35) of the Mamuniyat 
reservoir, a). Well 1, and b). Well 2. 
 
 
 
 
  
Figure 5. Core permeability versus pore size radius (R35) of wells 1 and 2 of Mamuniyat reservoir 
 
y = 1.8762x1.9426
R² = 0.9806
0.01
0.1
1
10
100
1000
10000
0.1 1 10 100
Core permeability 
(kcore, mD)
Pore throat radius (R35), μm
Well 1
Well 2

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 53 
Validation process 
Identification of the hydraulic flow units of the 
wells 1 and 2 within the Mamuniyat reservoir 
rocks, provides and drive to delineate hydraulic 
flow units in uncored well 3. Hence, the 
availability of core data of well 3 is essential to 
HFU of the Mamuniyat reservoir section, which is 
suitable to estimate HFU in terms of permeability 
empirical Equations, adjacent well 1 or well 2. In 
order, predicate permeability in well 3 may be 
subjected to verification procedure, also requires 
another permeability source to enhance uncertainty 
in Mamuniyat reservoir permeability evaluation. 
Accordingly, Wyllie and Rose (1950 have 
approved an empirical Equation applied to estimate 
the permeability of the Mamuniyat reservoir 
(Upper Ordovician) in well 3. However, utilizing 
of Neural Network (NN) technique by Interactive 
Petrophysics (IP 2018) to generate the HFU in well 
3 based on the HFU in well 1 that is in turn to 
predict the permeability (K HFU). Therefore, the 
gamma ray (GR) logs of the studied wells (Figure 
9) illustrate high matching between wells that is 
used to create the HFU in well 3, in the Neural 
Network training process. Then, Figure 10 
Reservoir Quality Index (RQI) and normalized 
porosity (Øz) and permeability - Porosity cross 
plotting of well 3, by predicated the HFU ’s. Figure 
10 manifests three hydraulic flow units (4, 5, 6) 
within the Mamuniyat reservoir. In addition, Figure 
11 demonstrates two different approved empirical 
Equations, predicated permeability by HFU 
Equations and R 35 classification with the GR and 
porosity logs. Although the predicated permeability 
Figure 6. Core porosity versus pore size radius (R35) of wells 1 and 2 of Mamuniyat reservoir.  
 
by HFU (K HFU) of well 3 furnish higher values 
than the Wyllie & Rose (1950) and (Ben Ghawar et 
al., 2026), it has a good fluctuation pattern between 
the predicated permeability results. Meanwhile, 
both Wyllie & Rose (1950); and (Ben Ghawar et 
al., 2026) furnished high agreement results with 
some exceptions. These exceptions are 
disconformable results of the predicated 
permeability of well 3, retracted between the 
depths 4700 and 4810 foot, which could attribute to 
limited number of the predicted HFU4, HFU5, and 
HFU6 though this depth interval may attribute to 
be changed from fine - to medium -grained sands 
into coarse -grained to pebbly sands of a braided 
system as reported by (Salaheddin et al., 2010).    
 
CONCLUSION 
The petrophysical evaluation of the Mamuniyat 
reservoir, is characterized by an approximate 
thickness of 133 feet and a low shale content (V sh) 
of 13%, effectively addresses the inherent 
challenges of reservoir heterogeneity and pore 
geometry distribution within the Murzuq Basin. By 
establishing a high convergence between total and 
effective porosity, and a strong correlation between 
core-measured and calculated porosity, this study 
provides a fine assessment of storage capacity. The 
integration of the Flow Zone Indicator (FZI) and 
the Winland parameter (R 35) successfully 
delineated five distinct hydraulic flow units (HFUs) 
categorized into micropores, mesopores, and 
macropores, thereby honoring the geological 
framework and depositional history essential for

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
54 I DOI org/10.29017/scog.v49i2.2035 
Figure 7. a). Reservoir quality index (RQI) and normalized porosity (Øz), b). Permeability- Porosity cross plotting and 
the different HFU’S of two wells 1, Mamuniyat reservoir. 
 
 
 
a
b

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 55 
Figure 8. a). Reservoir quality index (RQI) and normalized porosity (Øz), b). Permeability- Porosity cross plotting and 
the different HFU’S of two wells 2, Mamuniyat reservoir. 
 
 
 
a
b

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
56 I DOI org/10.29017/scog.v49i2.2035 
Figure 9. Gamma ray logs correlation between wells, of the Mamuniyat reservoir. 
 
Figure 10. a). Reservoir Quality Index (RQI) and normalized porosity (Øz), b). Predicted permeability- Porosity cross 
plotting and the different HFU’S of well 3, Mamuniyat reservoir. 
 
b

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 57 
Terms& 
Symbols Definition Unit 
K Permeability mD 
Øt Total porosity fraction 
Øe Effective porosity fraction 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
 
Figure 11. Gamma ray (GR) log, calculated porosity and permeability predication comparison of well 3, Mamuniyat 
reservoir.  
 
flow capacity assessment. The primary novelty of 
this research lies in the application of the Neural 
Network (NN) technique to overcome the 
limitations of missing core data in exploration 
wells. By utilizing training algorithms based on 
Wells 1 and 2 (R 2 ≈ 70%), the NN model 
successfully predicted HFUs and permeability for 
the uncored Well 3. This approach yielded superior 
performance and reliability compared to traditional 
empirical models like Wyllie and Rose (1950 or 
Ben Ghawar et al. (2026. Ultimately, this study 
demonstrates that artificial intelligence tools offer a 
robust, cost -effective alternative for enhancing 
reservoir characterization and predicting hydraulic 
properties in complex clastic reservoir.  
 
ACKNOWLEDGEMENT 
The authors thank the Akakus Oil 
Operations company for providing the basic data used 
in this work. We also thank the reviewers for their 
constructive comments which leas to improve this 
research. Authors admit that no any funding received 
from institutions nor any others. 
DECLARATIONS 
Author contribution 
The authors contributions is perfectly lead by 
the first Author, in terms of working hard, getting 
the data, editing, revision, administration and 
supervision of this work.  
Funding statement 
None 
Competing interest 
None 
The use AI or AI-assisted technologies 
None 
 
GLOSSARY OF TERMS AND SYMBOLS

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
58 I DOI org/10.29017/scog.v49i2.2035 
Øcore Core porosity fraction 
Kcore Core permeability mD 
Vsh Volume of shale fraction 
HFU Hydraulic flow unit - 
FZI Flow zone indicator - 
CCA Routine core analysis - 
R35 Pore throat radius μm 
NN Neural network - 
GR Gamma ray API 
IGR Gamma Ray index - 
NGS Spectmetry gamma ray - 
Øn Neutron porosity fraction 
ρb Bulk density  gm/cm3 
ΔT Interval travel time μs/ft 
Sw Water saturation fraction 
Ød Density porosity fraction 
a Tortuosity factor - 
m Cementation factor - 
Swirr Irreducible water 
saturation 
fraction 
RQI Quality index - 
Øz Normalized porosity fraction 
 
REFERENCES 
Ahmed, Usman, S. F. Crary, & G. R. Coates., 
(1991), Permeability Estimation: The Various 
Sources and Their Interrelationships. Journal of 
Petroleum Technology 43(05):578–87. 
Alkinani, Husam H., Abo Taleb Al-Hameedi, Shari 
Dunn-Norman, Ralph E. Flori, Mortadha T. 
Alsaba, & Ahmed S. Amer., (2019), 
Applications of Artificial Neural Networks in 
the Petroleum Industry: A Review. P. 
D032S063R002 in SPE Middle East Oil and 
Gas Show and Conference. SPE. 
Asquith, George B., & Charles R. Gibson, (1982a), 
Basic Relationships of Well Log Interpretation: 
Chapter I. P. 244 in AAPG. Tulsa, Oklahoma: 
AAPG Special Volumes. 
Asquith, George B., & Charles R. Gibson, (1982b), 
Porosity Logs: Chapter IV. Pp. 66–90 in Basic 
well log analysis for geologists. AAPG Special 
Volumes. 
Babadagli, T., & S. Al-Salmi, (2004), A Review of 
Permeability-Prediction Methods for Carbonate 
Reservoirs Using Well -Log Data. SPE 
Reservoir Evaluation & Engineering  7(02):75–
88. doi: 10.2118/87824-PA. 
Ben Ghawar, M. Bahia, M. F. Salloum, & A. M. Al 
Tarhouni, (2026), Neural Network and 
Empirical Models of Mamuniyat Reservoir 
Permeability Prediction, Murzuq Basin -Libya.” 
Iraqi National Journal of Earth Science (INJES)  
26(2):143–55. doi: 10.33899/injes.v26i2.60857. 
Castro, Abel, Sandrya Laksana, Gaaim 
Abdussalam, Osama Allotai, Muhaned Shaiebi, 
Tarek Alkhemri, Candido Gomez Nacarino, 
Aljilani Almhedwi, Faisal Burghig, & Faiza 
Omar, (2012), Integrated Reservoir Modeling 
on Heterogeneous Ordovician Sandstone of IR -
Fields, Murzuq Basin Libya, Helps Optimizing 
Field Development Plan and Reduce 
Uncertainty. P. SPE -161197-MS in Abu Dhabi 
International Petroleum Conference and 
Exhibition. SPE. 
Ebanks Jr, W. J., (1987), Flow Unit Concept --
Integrated Approach to Reservoir Description 
for Engineering Projects: ABSTRACT. AAPG 
Bulletin 71(CONF -870606-):551–52. doi: 
10.1306/94887168-1704-11D7-
8645000102C1865D. 
El-ghali, M. A. K., (2005), Depositional 
Environments and Sequence Stratigraphy of 
Paralic Glacial, Paraglacial and Postglacial 
Upper Ordovician Siliciclastic Deposits in the 
Murzuq Basin, SW Libya. Sedimentary 
Geology 177(3–4):145–73. doi: 10.1016/
j.sedgeo.2005.02.006. 
El-ghali, Mohamed Ali Kalefa, Howri Mansurbeg, 
Sadoon Morad, Ihsan Al -Aasm, & Karl 
Ramseyer, (2006), Distribution of Diagenetic 
Alterations in Glaciogenic Sandstones within a 
Depositional Facies and Sequence Stratigraphic 
Framework: Evidence from the Upper 
Ordovician of the Murzuq Basin, SW Libya. ” 
Sedimentary Geology  190(1):323–51. doi: 
https://doi.org/10.1016/j.sedgeo.2006.05.020. 
Fello, Nuri M., & B. R. Turner, 2004, Depositional 
Environments of the Upper Ordovician 
Mamuniyat Formation, NW Murzuq Basin, 
Libya. Pp. 166–82 in Proceedings of 3rd 
International Symposium on Geophysics, Tanta. 
Fello, Nuri Mohamed, (2001), Depostional 
Environments, Diagenesis and Reservoir

Permeability and Hydraulic Flow Units Prediction Using Neural Network Technique 
of the Clastic Mamuniyat Reservoir (Upper Ordovician), Murzuq Basin-Libya (Ghawar et al.) 
 
DOI org/10.29017/scog.v49i2.2035  I 59 
Modelling of Concession NC115, Murzuq 
Basin, SW Libya.” Durham University. 
Ben Ghawar, M. Bahia, M. F. Salloum, & A. M. Al 
Tarhouni, (2026), Neural Network and 
Empirical Models of Mamuniyat Reservoir 
Permeability Prediction, Murzuq Basin -Libya. 
Iraqi National Journal of Earth Science (INJES)  
26(2):143–55. doi: 10.33899/injes.v26i2.60857. 
Gunter, G. W., J. M. Finneran, D. J. Hartmann, & 
J. D. Miller, (1997), Early Determination of 
Reservoir Flow Units Using an Integrated 
Petrophysical Method. ” P. SPE -38679 in SPE 
Annual Technical Conference and Exhibition. 
SPE. 
Ha, Man Quang, Anh Ngoc Le, & Jadwiga Jarzyna, 
(2021), Hydraulic Flow Unit Classification from 
Core Data: Case Study of the Z Gas Reservoir, 
Poland. Journal of Mining and Earth Sciences  
62(3):29–36. doi: 10.46326/JMES.2021.62
(3).04. 
Hallett, D., & Daniel Clark -Lowes, (2016), 
Petroleum Geology of Libya: Second Edition. 
Sesonc Edi. Amsterdam: Elsevier. 
Hamzah Kamal, Amega Yasutra, & Dedy Irawan, 
(2021), Prediction of Hydraulic Fractured Well 
Performance Using Empirical Correlation and 
Machine Learning. Scientific Contributions Oil 
and Gas , 44(2):141 –52. https://
doi.org/10.29017/SCOG.44.2.589.  
Hearn, C. L., W. J. Ebanks  Jr., R. S. Tye, & V. 
Ranganathan, (1984), Geological Factors 
Influencing Reservoir Performance of the 
Hartzog Draw Field, Wyoming. Journal of 
Petroleum Technology  36(08):1335–44. doi: 
10.2118/12016-PA. 
J. Cubitt, C., W. Gruber, B. C. Stummer, & O. 
Allottai, (2011), Depositional Environments of 
the Mamuniyat Formation in the Central 
Murzuq Basin, Libya.” P. cp-238 in 73rd EAGE 
Conference and Exhibition incorporating SPE 
EUROPEC 2011. Vienna, Austria: European 
Association of Geoscientists & Engineers. 
Khalid, Mostafa, Saad El -Din Desouky, 
Mohammed Rashed, Tarek Shazly, & Kadry 
Sediek, (2020), Application of Hydraulic Flow 
Units’ Approach for Improving Reservoir 
Characterization and Predicting Permeability. 
Journal of Petroleum Exploration and 
Production Technology  10(2):467–79. doi: 
10.1007/s13202-019-00758-7. 
Lala, Amir Maher Sayed, & Nahla A. A. El -Sayed, 
(2017), Controls of Pore Throat Radius 
Distribution on Permeability. Journal of 
Petroleum Science and Engineering  157:941–
50. 
Mahmoud, S. E., W. M. Mabrouk, & M. A. 
Waziry, (2019), Integration of core data and 
well logs for reservoir characterization, flow 
units evaluation and permeability estimation in 
shaly sand reservoirs, onshore east nile delta 
egypt. Journal of Egyptian Geophysical Society 
17(1):71–84. doi: 10.21608/jegs.2019.402337. 
McCulloch, Warren S., & Walter Pitts. 1943. “A 
Logical Calculus of the Ideas Immanent in 
Nervous Activity. The Bulletin of Mathematical 
Biophysics 5(4):115–33. 
Mohaghegh, Shahab, (2000), Virtual -Intelligence 
Applications in Petroleum Engineering: Part 
1—Artificial Neural Networks. ” Journal of 
Petroleum Technology  52(09):64–73. doi: 
10.2118/58046-JPT. 
Mohamed, Adel K., & Adel Kashlaf, (2016), 
Comparative Study between Well Logging and 
Core Analysis of Hawaz Reservoir in Murzuq 
Basin, Libya. Egyptian Journal of Basic and 
Applied Sciences  3(3):301–13. doi: 10.1016/
j.ejbas.2016.07.003. 
Mohammed, Abbas Kareem Abdulsahib, (2020), A 
Review: Controls on Sandstone Permeability 
during Burial and Its Measurements 
Comparison—Example, Permian Rotliegend 
Sandstone. Modeling Earth Systems and 
Environment 6(2):591–603. 
Novita, Dian, Dzul Fadli Badaruddin, Sorja 
Koesuma, & Handono Ramelan, (2022), 
Interpretasi Sumur Log Untuk Menentukan 
Zona Prospek Hidrokarbon Pada Cekungan 
Akimeugah, Papua. Lembaran Publikasi 
Minyak Dan Gas Bumi  56(1):1–10. https://
doi.org/10.29017/LPMGB.56.1.91.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 45 - 60 
 
60 I DOI org/10.29017/scog.v49i2.2035 
Salaheddin, K., S. Laksana, & M. Schöbel, (2010) 
Rock Typing Approach for Reservoir 
Characterization of Ordovician Sandstones, 
Fields Case Study, Concessions NC115/NC186, 
Murzuq Basin, Libya. North Africa Technical 
Conference and Exhibition SPE-128825-MS. 
Shalbak, Farid Ali Ka., (2015), Palaeozoic 
Petroleum Systems of the Murzuq Basin, 
Libya.” Universitat de Barcelona. 
Usman, Usman, Darsono Marino, & Marzuki 
Soelistijono, (2010), Study On Productivity 
Improvement Of Low Permeability Gas 
Reservoir By Hydraulic Fracturing. Scientific 
Contributions Oil and Gas , 33(2):120 –28. 
https://doi.org/10.29017/SCOG.33.2.815.  
Wahyudi, Agus, Tutuka Ariadji, Taufan 
Marhaendrajana, Kuntjoro Adji Sidarto, & 
Zuher Syihab, (2025), A Fully Implicit 
Reservoir Simulation Using Physics Informed 
Neural Network. ” Scientific Contributions Oil 
and Gas  48(3):131–47. https://doi.org/10.29017/
scog.v48i3.185. 
Winland, H. D., (1972), Oil Accumulation in 
Response to Pore Size Changes, Weyburn Field, 
Saskatchewan: Amoco Production Company. 
Report F72-G-25, 20 p.(unpublished). 
Wyllie, M. R. J., & Walter D. Rose, (1950), Some 
Theoretical Considerations Related to the 
Quantitative Evaluation of the Physical 
Characteristics of Reservoir Rock from 
Electrical Log Data. Journal of Petroleum 
Technology 2(04):105–18. 
Yogi, Ade, (2018), Estimasi Permeabilitas Dengan 
Beberapa Metode Karakterisasi Reservoir 
Untuk Formasi Talangakar. Lembaran Publikasi 
Minyak Dan Gas Bumi 52(1):25–48. https://
doi.org/10.29017/LPMGB.52.1.91. 
Zhang, Zhao, Heng Zhang, Jie Li, & Zhongxian 
Cai., (2021), Permeability and Porosity 
Prediction Using Logging Data in a 
Heterogeneous Dolomite Reservoir: An 
Integrated Approach. ” Journal of Natural Gas 
Science and Engineering 86:103743. doi: 
10.1016/j.jngse.2020.103743.
