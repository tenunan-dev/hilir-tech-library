---
source_id: "lemigas-scog"
title: "Amplitude Versus Frequency AVF as an Alternative Method for Detecting Gas Presence in Carbonate Reservoirs A C"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2122"
retrieved_at: "2026-10-24T14:29:49+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "7f8a572b31626e0479babe7580dc1f97db4d99c35e14887a2b0124dcf48225ef"
collected: "manual"
---

# Amplitude Versus Frequency AVF as an Alternative Method for Detecting Gas Presence in Carbonate Reservoirs A C

647 
 
https://doi.org/10.29017/scog.v49i3.2122 
© 2026 The Author(s). Published by LEMIGAS under the Creative Commons Attribution-ShareAlike 4.0 
International License (CC BY-SA 4.0) 
 
 
TESTING CENTER FOR OIL AND GAS LEMIGAS 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS (SCOG) 
Vol. 49. No. 3, September: 647 – 666 - https://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
 
 
 
Amplitude Versus Frequency (A VF) as an Alternative Method for 
Detecting Gas Presence in Carbonate Reservoirs: A Case Study of the 
Baturaja Formation, South Sumatra Basin 
 
Tati Zera, Bahrul Ulum*, Praditiyo Riyadi, and Jarea Yurika Lubis 
 
Department of Physics, Faculty of Science and Technology, Universitas Islam Negeri Syarif Hidayatullah Jakarta,  
Ir. H. Juanda Street No. 95, Ciputat, South Tangerang, Banten 15412, Indonesia. 
*Corresponding author: Bahrul Ulum (bahrul.ulum22@mhs.uinjkt.ac.id) 
Bahrul Ulum: https://orcid.org/0009-0004-3048-4672 
Received: 23 February 2026; Revised: in revised form 30 April 2026; Accepted: 03 July 2026 
Available: online 30 September 2026. 
 
 
 
ABSTRACT - Accurate characterization of heterogeneous carbonate reservoirs remains challenging because 
conventional amplitude -based seismic methods may be affected by complex lithology, pore systems, and 
fractures. This study evaluates the application of Amplitude Versus Frequency (AVF) integrated with 
Continuous Wavelet Transform (CWT) to identify hydrocarbon -bearing zones in the Baturaja Formation, South 
Sumatra Basin. The analysis uses 3D Post Stack Time Migration  (PSTM) seismic data integrated with well -
log, checkshot, and marker data from three wells (B1, N1, and N2). Well -to-seismic tie analysis yielded 
correlation coefficients of 0.702, 0.638, and 0.805, respectively, confirming reliable seismic –well integratio n. 
CWT spectral decomposition was performed over a frequency range of 10 –70 Hz, followed by AVF analysis 
to evaluate frequency -dependent amplitude attenuation. The results show dominant low -frequency anomalies 
and predominantly negative AVF gradients withi n the target interval, indicating attenuation of high -frequency 
seismic energy. These responses are consistent with low water saturation and low gamma -ray values observed 
in the wells, supporting their interpretation as gas -bearing carbonate reservoir zone s. AVF horizon slicing 
further reveals laterally continuous anomalies concentrated in the eastern to northeastern part of the study area. 
The results demonstrate that CWT -based AVF provides complementary frequency -dependent information for 
hydrocarbon iden tification and reservoir delineation, offering a useful approach for reducing interpretation 
uncertainty in heterogeneous carbonate reservoirs. To the best of the authors’ knowledge, its application to the 
Baturaja Formation remains limited, highlighting t he contribution of this study to frequency -based carbonate 
reservoir characterization.  
Keywords: Amplitude Versus Frequency (AVF), Continuous Wavelet Transform (CWT), reservoir 
characterization, hydrocarbon identification, Baturaja Formation, South Sumatra Basin. 
 
 
How to cite this article: 
Tati Zera, Bahrul Ulum, Praditiyo Riyadi, and Jarea Yurika Lubis, 2026, Amplitude Versus Frequency 
(AVF) as an Alternative Method for Detecting Gas Presence in Carbonate Reservoirs: A Case Study of 
the Baturaja Formation, South Sumatra Basin, Scientific Contributions Oil and Gas, 49 (3) pp. 647-666.

648 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
1. Introduction 
Oil and gas exploration relies on accurate reservoir characterization to identify hydrocarbon accumulations 
and evaluate reservoir potential. Reservoir characterization involves understanding petrophysical properties, 
lithological distribution, and structu ral conditions, all of which are critical for reducing uncertainties in reserve 
estimation and exploration decision-making (Mineral 2022). 
Seismic reflection methods are widely used for subsurface imaging and reservoir inte rpretation. However, 
conventional seismic analysis often faces challenges in distinguishing hydrocarbon-bearing reservoirs from non-
productive zones, particularly in thin -layered or highly heterogeneous formations. Although Amplitude Versus 
Offset (AVO) analysis has been extensively applied to identify hydrocarbon indicators, its interpretation may be 
affected by lithological variations, data quality, and its dependence on high-quality pre-stack seismic data (Wu et 
al., 2014) Recent studies have demonstrated that AVO remains effective for hydrocarbon prediction in carbonate 
reservoirs when integrated with additional seismic analyses. (Hong Li et al., 2024)  demonstrated that 
incorporating seismic disper sion into AVO inversion significantly improved hydrocarbon prediction in deep 
carbonate reservoirs. Likewise, (Hong Li et al., 2024) reported that rock-physics calibration is essential for reliable 
AVO interpretation because ca rbonate elastic responses are strongly influenced by pore types and diagenetic 
processes. Furthermore, (Setyawan 2021) showed that AVO inversion successfully delineated hydrocarbon -
bearing carbonate intervals using Lambda -Rho and Mu -Rho attributes when supported by well -log calibration. 
These studies indicate that AVO can provide valuable fluid and lithology information in carbonate reservoirs; 
however, its reliability depends strongly on appropriate rock -physics calibratio n and the availability of high -
quality pre -stack data . Despite these advances, AVO interpretation in carbonate reservoirs remains uncertain 
because carbonate rocks exhibit highly heterogeneous lithology, complex pore systems, fractures, and vugs, 
causing seismic responses that may deviate from conventional AV O classifications  (Rutherford & Williams 
1989). Consequently, hydrocarbon-bearing and water-bearing carbonate intervals may exhibit overlapping AVO 
responses, highlighting the need for complementary seismic attrib utes that provide information beyond angle -
dependent amplitude variations. 
To overcome the limitations of conventional amplitude -based interpretation, frequency -dependent seismic 
analysis has increasingly been used to investigate attenuation effects and su btle reservoir responses. Spectral 
decomposition provides a means of separating seismic data into individual frequency components, enabling 
frequency-dependent variations that may be obscured in broadband seismic data to be identified (Partyka et al., 
1999) Among the available approaches, Continuous Wavelet Transform (CWT) is particularly useful because its 
variable time –frequency resolution allows localized spectral anomalies to be analyzed while preserving their 
temporal p osition (Sinha et al., 2005) . Previous applications have demonstrated that CWT -based spectral 
decomposition can improve the delineation of stratigraphic features and hydrocarbon -related anomalies. For 
example, Mandong et al. (2021)  applied CWT -derived frequency gathers and Amplitude Variation with 
Frequency (AVF) to delineate hydrocarbon-bearing zones, with the resulting AVF anomalies showing consistency 
with AVO responses and water -saturation logs. More recent applications have also demonstrated the ability of 
spectral decomposition to resolve subtle reservoir features, including hydrocarbon -bearing intervals and 
stratigraphic baffles that are difficult to identify using conventional seismic attr ibutes alone (Durogbitan et al., 
2023). However, these studies primarily demonstrate the value of spectral decomposition for identifying 
frequency-dependent seismic responses and improving qualitative reservoir delineati on. The quantitative 
relationship between seismic amplitude and frequency, particularly its use for evaluating frequency -dependent 
attenuation, remains less extensively investigated in heterogeneous carbonate reservoirs. 
This distinction is important becau se frequency variations in carbonate reservoirs may arise from multiple 
geological and seismic factors, including complex pore systems, fractures, vugs, lithological variations, diagenetic 
alteration, tuning effects, and intrinsic attenuation. Therefore, f requency anomalies observed in carbonate 
reservoirs should not be interpreted solely from spectral amplitude patterns, but should be evaluated through their 
amplitude–frequency relationship and supported by independent geological and petrophysical evidence. Although 
AVF has been demonstrated as a complementary hydrocarbon indicator (Mandong et al., 2021), the application 
of AVF to heterogeneous carbonate reservoirs remains relatively limited compared with its broader use for

649 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
frequency-based seismic interpretation. In addition, CWT-based spectral decomposition in carbonate settings has 
commonly been applied to delineate reservoir geometry and frequency anomalies, whereas the quantitative 
integration of CWT -derived frequency comp onents with AVF parameters and well -derived petrophysical 
information remains insufficiently documented. This represents the principal research gap addressed in this study 
whether the integration of CWT -based spectral decomposition and AVF can provide a co nsistent frequency -
dependent indicator for hydrocarbon identification in a heterogeneous carbonate reservoir and how the resulting 
seismic response can be constrained using petrophysical properties. 
The South Sumatra Basin is one of Indonesia’s major hydro carbon-producing basins and contains a complex 
petroleum system. One of its primary reservoir units is the Baturaja Formation, an Oligocene–Miocene carbonate 
reservoir characterized by significant heterogeneity resulting from depositional and diagenetic processes (Satyana 
2008) . Previous studies have reported that the Baturaja Formation exhibits variable reservoir characteristics, 
reflecting the complex nature of carbonate reservoirs in the region (Widarsono, 2022). Such heterogeneity makes 
the Baturaja Formation an appropriate geological setting for evaluating complementary frequency -domain 
approaches, particularly where conventional seismic responses may be ambiguous. The complex reservoir 
characteristics of the Baturaja Formation create challenges in reservoir delineation and hydrocarbon identification 
using conventional seismic interpretation methods (Waples 2000) . 
Therefore, this study applies the Amplitude Versus Frequency (AVF) method  using Continuous Wavelet 
Transform (CWT) to characterize reservoirs and identify prospective hydrocarbon zones within the Baturaja 
Formation of the South Sumatra Basin. The scientific novelty of this study lies in the application and integration 
of CWT-based spectral decomposition and quantitative AVF analysis to evaluate frequency-dependent amplitude 
attenuation within the Baturaja carbonate reservoir of the South Sumatra Basin. Unlike previous studies that 
primarily employ spectral decomposition for qual itative frequency mapping or apply AVF in other geological 
settings, this study combines CWT -derived frequency volumes, AVF intercept and gradient analysis, and well -
derived petrophysical information to constrain the interpretation of potential hydrocarbon-related attenuation. To 
the best of the authors’ knowledge, this represents a previously undocumented application of a CWT-based AVF 
workflow for hydrocarbon-oriented characterization of the Baturaja Formation in the South Sumatra Basin. The 
results are expected to improve reservoir characterization, delineate potential hydrocarbon-bearing intervals, and 
provide further insight into the applicability of frequency-dependent seismic attributes for reducing interpretation 
uncertainty in heterogeneous carbonate reservoirs. 
 
2. Methodology 
This study applies the Amplitude Versus Frequency (AVF) method for reservoir characterization in the 
Baturaja Formation, South Sumatra Basin. The dataset consists of 3D Post Stack Time Migration (PSTM) seismic 
data covering inline numbers 2326 –2610 and crossline numbers 10201 –10420. In addition to seismic data, well 
data including wireline logs, checkshot surveys, and horizon markers from three wells (B1, N1, and N2) were 
utilized. The study area is located within the South Sumatra Basin, one of Indonesia’s most productive hydrocarbon 
basins with a complex petroleum system. The regional geological map and the base map showing the locations of 
seismic lines and wells are presented in Figures 1 and Figures 2, respectively. 
The data processing workflow began with a well tie procedure, which integrated well logs, horizon markers, 
and checkshot data with the seismic dataset. This process converted geological information from the depth domain 
into the time domain through synthetic seismogram generation, allowing accurate correlation  between well 
markers and seismic reflectors (Yilmaz 2001). Well tie analysis is an essential step in seismic interpretation 
because it minimizes uncertainty in horizon picking and improves the reliability of reservoir mapping by ensuring 
consistency between borehole measurements and seismic responses (Sheriff & Geldart 1995). 
2.1 Continuous wavelet transform (CWT) 
Following the well tie process, spectral decomposition was performed using the Continuous Wavelet 
Transform (CWT) with a complex Ricker wavelet to obtain a high -resolution time–frequency representation of

650 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
the seismic signal. Unlike the Short -Time Fourier Transform (STFT), which applies a fixed window length and 
therefore provides constant time -frequency resolution, CWT employs scalable wavelets that allow adaptive 
resolution across differe nt frequencies (Sinha et al., 2005) . Consequently, CWT  is particularly  suitable for 
detecting thin beds, stratigraphic discontinuities, and hydrocarbon-related attenuation because it preserves both 
temporal and spectral informa tion (Partyka et al., 1999)  The Continuous Wavelet Transform of a seismic trace 
𝑥(𝑡)is mathematically expressed as in Equation 1 
𝑊(𝑎, 𝑏) = ∫∞ 
∞
𝑠(𝑡) ψ∗(𝑎𝑡 − 𝑏) 𝑑𝑡                  (1) 
where 𝑊 (𝑎, 𝑏), 𝑎, 𝑏, 𝜓(𝑡), and 𝜓∗, are wavelet coefficient, scale parameter related to frequency, translation 
parameter in time,  mother wavelet  and complex conjugate of the mother wavelet , respectively . The scale 
parameter is inversely proportional to frequency, allowing lo w-frequency components to be represented with 
higher frequency resolution while preserving high temporal resolution for high -frequency events                       
(Stéphane Mallat 2009) . 
In this study, frequency extraction was carried out over a range of 10 to 70 Hz at 5 -Hz intervals, resulting 
in 13 iso -frequency volumes. The 10 –70 Hz frequency range was selected to encompass the effective and 
reliable bandwidth of the seismic data, while avoiding frequencies outside the do minant energy range that may 
contain limited signal energy or be more strongly affected by noise and attenuation. This frequency range 
therefore provides a suitable basis for capturing the frequency -dependent variation of seismic amplitude within 
the target reservoir interval. The extracted frequency volumes were subsequently combined through a gathering 
process, in which the frequency values were sequentially assigned to an analogous incident -angle parameter. 
This procedure enabled the implementation of AV F analysis by treating frequency as an equivalent variable to 
reflection angle, allowing the variation of seismic amplitude with frequency to be quantified through the AVF 
intercept and gradient.  
 
 
Figure 1.  
Regional geological map.

651 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 2. 
Base map of the research area in the South Sumatra Basin showing the 3D seismic survey boundary, seismic inline–crossline 
grid, and the locations of wells B1, N1 and N2 used in the AVF reservoir characterization study. 
 
2.2 Amplitude versus frequency (A VF) 
The AVF method employed in this study consists of two main stages. The first stage involves the generation of 
frequency-dependent seismic amplitude information through spectral decomposition using the Continuous 
Wavelet Transform (CWT). The CWT decomposes the seismic signal into its constituent frequency components 
while preserving their temporal information, thereby enabling the amplitude response to be examined at different 
frequencies and time samples. The resulting frequency gather is presented in Figure 3, where each subfigure 
represents the time-frequency distribution of an individual seismic trace, with frequency displayed along the x -
axis and time along the y -axis. This decomposition provides detailed information on the variati on of seismic 
amplitude across the frequency spectrum and forms the basis for the subsequent AVF analysis. 
 
 
Figure 3. 
 Frequency gathering form the continues wavelet transform.

652 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
In the second stage, the amplitude response obtained from the CWT-derived frequency components is 
evaluated as a function of frequency at each seismic time sample. In this study, the relationship between seismic 
amplitude and frequency is approximated using a linear formulation rather than  the squared sine function of 
frequency adopted in previous AVF studies, such as (Mandong et al.2021) and (Wihardy & Khairy 2021) The linear 
relationship is expressed as in Equation 2 
𝑦 = 𝐼 + 𝐺sin 2(𝑥)                      (2) 
The selection of the frequency range is an important parameter in determining the reliability of the AVF 
response. As illustrated in Figure 4, (f_1) and (f_2) represent the lower and upper frequency limits used in the 
linear fitting process. In this study, the dominant frequency identified from the spectral decomposition  is used as 
a reference for defining the lower frequency limit, while the upper frequency limit is  selected based on the 
characteristics and usable range of the amplitude spectrum. This approach ensures that the fitting process is 
performed within a frequency interval that provides a representative amplitude response  while minimizing the 
influence of poorly resolved or insignificant frequency components (Han & others 2023). 
 
 
 
Figure 4. 
Schematic illustration of AVF intercept and gradient estimation by linear fitting of spectral amplitude within  
the frequency range ([f_1, f_2]) (adapted from Wihardy and Khairy, 2021). The red and blue curves represent  
the spectral amplitude responses associated with hydrocarbon-bearing and non-hydrocarbon areas, respectively.  
The hydrocarbon-associated response exhibits a relatively larger intercept and steeper gradient, indicating stronger 
frequency-dependent attenuation (Han & others 2023). 
 
 
The fitted intercept and gradient provide complementary information about the frequency-dependent behavior 
of the seismic signal. The intercept (I) represents the extrapolated amplitude at the zero-frequency reference, 
whereas the gradient (G) describes the rate and direction of amplitude change with increasing frequency. A negative 
gradient indicates that seismic amplitude decreases as frequency increases, representing a frequency -dependent 
attenuation response. Such attenuation may be associated with hydrocarbon  saturation; however, the gradient 
response is not uniquely diagnostic of hydrocarbons because frequency-dependent amplitude variations may also 
result from lithological changes, tuning effects, pore-fluid and pore-structure variations, intrinsic attenuation, and 
seismic processing effects (Castagna et al., 2003;  Mandong et al., 2021) . Therefore, the gradient response must 
be interpreted in conjunction with independent geological and petrophysical information. 
To enhance the spatial expression of anomalous frequency-dependent responses, the AVF attribute is calculated 
from the combination of the intercept and gradient parameters: 
𝐴𝑉𝐹 = 𝐼 × 𝐺                             (3)

653 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
where (I) and (G) are the intercept and gradient obtained from the amplitude-frequency fitting. The product of these 
two parameters provides an integrated measure of the amplitude level and its frequ ency-dependent variation, 
allowing anomalous zones to be more clearly delineated within the seismic volume. In particular, areas 
characterized by relatively strong amplitudes accompanied by negative gradients may produce  distinctive AVF 
responses that can be evaluated as potential hydrocarbon-related anomalies when supported by geological and 
petrophysical evidence (Mandong et al., 2021). 
 
 
Figure 5. 
Workflow of AVF-based reservoir characterization, including well-to-seismic tie, spectral decomposition, frequency 
gathering, AVF attribute calculation, and AVF mapping using 3D PSTM seismic and well data. 
 
 
The AVF attributes were calculated for each seismic sample by fitting the amplitude values extracted from the 
available CWT-derived frequency volumes to the frequency variable. The resulting intercept and gradient volumes 
were then analyzed together with the individual frequency components to assess the spatial and temporal 
distribution of frequency-dependent seismic responses. This integrated approach allows the  AVF response to be 
evaluated not only from the final AVF attribute but also from its individual components, thereby providing a more 
robust basis for geological interpretation. 
Finally, interpretation was performed through horizon slicing of the  AVF attribute volume within the target 
interval of the Baturaja Formation. The dominant frequency distribution and reservoir characteristics were 
interpreted by integrating AVF results with geological and petrophysical information obtained from wells B1, N1, 
and N2. The integration of seismic attributes and well data provided a comprehensive understanding of reservoir 
geometry and facilitated the identification of potential hydrocarbon-bearing zones.

654 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
Overall, the met hodological workflow begins with well -to-seismic integration to establish the relationship 
between the well information and the 3D PSTM seismic data. The seismic data are subsequently decomposed 
into frequency -dependent components using the CWT, from which  amplitude information is extracted at 
individual seismic samples. These amplitudes are then fitted as a function of frequency to obtain the intercept 
and gradient parameters, which are combined to generate the AVF attribute. Finally, the AVF results are 
interpreted through horizon slicing and integrated with seismic geological, and petrophysical information to 
characterize the reservoir and identify potential hydrocarbon -bearing zones. The complete workflow adopted 
in this study is presented in Figure 3. 
 
3. Result and discussion 
3.1 Analysis well seismic – tie 
Well-to-seismic tie analysis is a crucial step in integrating well data in the depth domain with seismic data in 
the time domain. The process begins with the calibration of well data using checkshot information to establish a 
more accurate time–depth relationship. Subsequently, a seismic wavelet is extracted from the seismic dataset. In 
this study, a statistical wavelet was generated with a wavelet length of 74 ms and a dominant frequency of 16 Hz. 
The next step involves convolving the reflection coefficient series derived from the well logs with the extracted 
wavelet to generate a synthetic seismogram. This synthetic seismogram is then matched with the seismic trace at 
the well location to establish the well -to-seismic tie. The resulting correlation ensures accurate identification of 
geological horizons on the seismic data and improves the reliability of subsurface interpretation. 
The well-to-seismic tie results, demonstrate a satisfactory correlation between the synthetic seismograms and 
the observed seismic data. Correlation coefficients of 0.702, 0.638, and 0.805 were obtained for wells B1, N1, and 
N2, respectively. These values indicate a good to very good match between the synthetic traces generated from 
well-log data and the corresponding seismic responses, suggesting that the  synthetic seismograms adequately 
represent the subsurface seismic characteristics at each well location. 
Among the three wells, Well N2 exhibits the highest correlation coefficient, indicating the strongest 
agreement between the synthetic and seismic traces. Meanwhile, Wells B1 and N1 also show acceptable 
correlation values, confirming the reliability of the tie despite potential i nfluences from factors such as seismic 
noise, wavelet estimation uncertainties, and variations in log quality. Overall, the correlation results indicate 
that the generated synthetic seismograms provide a robust representation of the seismic signal and can be 
confidently used for seismic interpretation.  
The successful well -to-seismic tie validates the time –depth relationship established through checkshot 
calibration and ensures accurate positioning of geological markers within the seismic volume. This step is essential 
for minimizing uncertainties in horizon picking and stratigraphic correlation. Consequently, the well tie serves as 
a reliable foundation for subsequent analyses, including horizon interpretation,  spectral decomposition, and 
Amplitude Versus Frequency (AVF) attribute extraction within the Baturaja Formation. 
3.2 Analysis continuous wavelet transform (CWT) 
The 3D Post Stack  Time Migration (PSTM) seismic data were decomposed using the Continuous Wavelet 
Transform (CWT) method to investigate the freque ncy-dependent characteristics of the seismic response and to 
identify potential hydrocarbon reservoirs. Spectral decomposition enables the analysis of seismic signals in the 
time–frequency domain, allowing localized variations in frequency content to be observed with greater detail than 
conventional seismic interpretation.  This capability  is particularly useful for detecting attenuation -related 
anomalies associated with hydrocarbon-bearing reservoirs.

655 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 6. 
Well seismik – tie, well N1. 
 
   
Figure 7. 
Well seismik – tie, well B1. 
 
 
 
Figure 8. 
Well seismik – tie, well B2

656 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
The presence of hydrocarbons within porous reservoir rocks can induce seismic attenuation, where high -
frequency components experience greater energy loss than low-frequency components during wave propagation. As 
a result, the frequency spectrum shifts toward lower frequencies, producing a phenomenon commonly referred to as 
a low-frequency shadow. This anomaly is widely recognized as a potential indicator of hydrocarbon accumulation 
because the absorption of high-frequency energy by hydrocarbon-saturated rocks leads to the relative enhancement 
of low-frequency responses. Consequently, zones characterized by dominant low-frequency amplitudes are often 
interpreted as prospective hydrocarbon reservoirs. 
The Continuous Wavelet Transform (CWT) method was selected because it provides adaptive time–frequency 
resolution by adjusting the wavelet window according to the analyzed frequency. Low frequencies are represented 
by wider windows, allowing deeper signal penetration and improved detection of large-scale geological features, 
whereas high frequencies utilize narrower windows, providing enhanced vertical resolution and greater stratigraphic 
detail. This characteristic mak es CWT particularly suitable for analyzing non -stationary seismic signals and 
identifying subtle frequency variations associated with reservoir properties. 
The spectral decomposition results obtained using the Continuous Wavelet Transform were evaluated at  
frequencies of 10 Hz, 20 Hz, and 40 Hz to investigate the variation of seismic responses within the target 
interval. At 10 Hz (Figure 8), a laterally continuous low -frequency amplitude anomaly is observed within the 
target zone. The anomaly appears relatively strong and persistent, suggesting the presence of attenuation effects 
commonly associated with hydrocarbon -bearing reservoirs. The dominance of low -frequency energy at this 
interval is consistent with the low -frequency shado w phenomenon reported by Partyka et al. (1999) , who 
demonstrated that hydrocarbon -saturated reservoirs often exhibit enhanced low -frequency responses compared 
to surrounding formations.  
At 20 Hz (Figure 9), the seismic image exhibits improved vertical resolution, allowing geological boundaries 
and subsurface geometries to be delineated more clearly. Although the low-frequency anomaly remains 
identifiable, the enhanced resolution facilitates a better assessment of its lateral continuity and spatial distribution. 
The 20 Hz frequency slice therefore serves as an important intermediate frequency for validating the extent of the 
anomaly detected at lower frequencies. 
The 40 Hz frequency volume (Figure 10) displays sharper reflectors and more detailed stratigraphic features due 
to the higher vertical resolution associated with high -frequency components. However, a noticeable reduction in 
amplitude is observed within the target zone compared to the lower-frequency volumes. The reduction in high-
frequency amplitude may indicate frequency-dependent attenuation associated with energy absorption during 
seismic-wave propagation through porous, fluid-saturated rocks. Since high -frequency components generally 
experience stronger attenuation than lower -frequency components, this response can be consistent with a 
hydrocarbon-related attenuation effect. However, frequency attenuation is not uniquely d iagnostic of 
hydrocarbons and may also result from intrinsic absorption, fluid properties, lithological heterogeneity, pore 
structure, fractures, vugs, scattering, tuning effects, and seismic processing. 
This uncertainty is particularly relevant to the Baturaja Formation, where heterogeneous carbonate pore 
systems and diagenetic variations can influence seismic amplitude and frequency response independently of 
hydrocarbon saturation. In addition, wavelet characteristics, bandwidth limitations, and spectr al decomposition 
parameters may affect the extracted frequency amplitudes. Therefore, the high -frequency amplitude reduction 
observed in Figure 10 is interpreted as evidence of frequency -dependent behavior rather than definitive proof of 
hydrocarbon presence. 
The systematic low-frequency anomalies and progressive attenuation of high-frequency amplitudes across the 
spectral decomposition volumes provide stronger support than an isolated amplitude anomaly. Nevertheless, the 
interpretation is further constrained by the subsequent AVF analysis and independent petrophysical information. 
Thus, the observed frequency response is considered a potential hydrocarbon-related attenuation indicator, while 
acknowledging uncertainty from geologi cal heterogeneity, seismic resolution, attenuation mechanisms, and 
processing effects. These frequency volumes subsequently form the basis for the AVF analysis to quantify the 
amplitude–frequency relationship and improve reservoir characterization.

657 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 9. 
Original 3D PSTM seismic section of the study area. 
 
 
 
 
Figure 10 
 CWT-based seismic section at 10 Hz showing the frequency-dependent amplitude  
response within the target reservoir interval. 
 
 
 
3.3 Analysis A VF Attribut 
The results of the  Amplitude Versus Frequency (AVF) attribute as shown in Figure 11 , indicate a 
predominance of negative gradient values within the target interval. These negative gradient values suggest the 
occurrence of frequency attenuation, wh ere the energy of seismic waves, particularly at higher frequencies, 
decreases as the waves propagate through the subsurface medium. This attenuation phenomenon  is commonly 
associated with the presence of fluids within the pore spaces of reservoir rocks, which influence the elastic 
properties of the formation.

658 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 11. 
CWT-based seismic section at 20 Hz showing the frequency-dependent amplitude  
response within the target reservoir interval. 
 
 
 
 
Figure 12. 
CWT-based seismic section at 40 Hz showing the frequency-dependent amplitude  
response within the target reservoir interval. 
 
 
The reduction in high -frequency amplitudes observed within the target interval indicates that the reservoir 
has a greater capacity to absorb seismic energy compared  to the surrounding formations. This observation is 
consistent with the theory of seismic attenuation, which states that porous and fluid -saturated rocks tend to 
attenuate high -frequency seismic energy more significantly than low -frequency energy. As a res ult, low -
frequency components become relatively dominant, producing spectral anomalies that are commonly 
associated with hydrocarbon -bearing reservoirs. According to Mandong et al. (2021) , hydrocarbon-saturated 
reservoirs frequently exhibit a loss of high -frequency energy, causing the dominant frequency to shift toward 
lower frequencies. This phenomenon forms the basis for the application of AVF attributes as a Direct 
Hydrocarbon Indicator ( DHI) in reservoir characterization.

659 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
The AVF interpretation was further evaluated using the well-log responses from wells B1, N1, and N2,  as 
summarized in Table 1. At well B1, the gamma-ray (GR) value is 88.756 API, with a water saturation (Sw) of 
60.43% and a bulk density (RHOB) of 2.571 g/cm³. The moderate Sw value indicates that approximately 39.57% 
of the pore space is occupied by non -water fluids, which may provide support for the presence of hydrocarbons 
when consistent with the AVF response and other petrophysical indicators. At  well N1, the GR value is 89.347 
API, with an Sw of 70.5% and an RHOB of 2.498 g/cm³. The higher Sw relative to B1 indicates a greater 
proportion of water saturation, although the remaining 29.5 % non-water saturation may  still be consistent with  
hydrocarbon-bearing pore space. At well N2, the GR value is 87.573 API and the RHOB is 2.585 g/cm³, while 
Sw is unavailable for the analyzed interval. Overall, the GR values range from 87.573 to 89.347 API, while RHOB 
ranges from 2.498 to 2.585 g/cm³ and the available  Sw values range from 60.43% to 70.5%. The lower Sw at B1 
compared with N1 provides stronger petrophysical support for a potential hydrocarbon contribution, particularly if 
it coincides spatially with the negative AVF gradient anomaly. However, the relatively high GR values observed 
across the three wells indicate  that lithological and shale-related effects should also be considered. Therefore, the 
AVF anomalies are interpreted more reliably when integrated with Sw, GR, RHOB, seismic amplitude, and other 
available reservoir properties rather than being used as a standalone hydrocarbon indicator. 
Furthermore, the AVF responses observed at wells B1, N1, and N2 are chara cterized by negative gradient 
values, indicating frequency-dependent amplitude attenuation within the target interval. This response is supported 
by the available well-log data, particularly the water saturation (Sw) values of 60.43% at B1 and 70.5% at N1. The 
lower Sw at B1 provides relatively stronger support for a potential hydrocarbon contribution compared with N1, 
while the absence of Sw data at N2 prevents direct evaluation of its fluid saturation. The gamma -ray values of 
88.756, 89.347, and 87.573 API at B1, N1, and N2, respectively, indicate relatively similar lithological responses 
across the three wells, although the relatively high GR values suggest that shale -related and lithological effects 
should also be considered. The occurrence of negativ e AVF gradients across the three wells, together with the 
available petrophysical evidence, suggests that frequency-dependent attenuation may provide a useful indicator 
for identifying anomalous reservoir intervals within the heterogeneous carbonate succes sion of the Baturaja 
Formation. However, the AVF response should be interpreted as an integrated indicator rather than definitive 
evidence of gas accumulation, particularly because the observed Sw values and lithological responses indicate 
that fluid and lithological effects may both contribute to the frequency-dependent seismic response. 
 
 
Figure 13. 
 AVF attribute seismic section showing negative gradient anomalies within the target reservoir interval, integrated with 
Gamma Ray (GR) log responses from wells B1, N1, and N2 to support the interpretation of frequency-dependent attenuation 
and potential hydrocarbon-bearing zones.

660 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
Table 1.  
AVF attributes and petrophysical parameters of wells B1, N1, and N2. 
Well A VF Attribut GR Sw RHOB 
B1 −1.70095×106 88.756 API 60.43% 2.571 g/cm³ 
N1 −1.17377×106 89.347 API 70.5% 2.498 g/cm³ 
N2 −1.32474×106 87.573 API - 2.585 g/cm³ 
 
 
The integration of AVF attributes with well-log information demonstrates a consistent relationship between 
low-frequency anomalies, negative gradient values, and the petrophysical properties of the reservoir. The observed 
attenuation pattern suggests the presence of hydrocarbon-bearing zones within the Baturaja Formation. These 
findings are consistent with the study of Mandong et al. (2021), which demonstrated that AVF attributes derived 
from spectral decomposition can effectively delineate hydrocarbon reservoirs through the analysis of frequency -
dependent amplitude variations. 
The present results also support the findings of (Hong Li et al., 2024), who reported that hydrocarbon prediction 
in carbonate reservoirs can be significantly improved by incorporating frequency-dependent information because 
conventional AVO responses are often affected by fracture systems, vuggy porosity, and strong lithological 
heterogeneity. Unlike conventional AVO analysis, which relies on amplitude variations with offset and commonly 
requires high-quality prestack seismic data and rock -physics calibration for reliable interpretation in carbonate 
reservoirs (Yongyi Li et al., 2003), the CWT-based AVF method evaluates amplitude variations with frequency, 
enabling the identification of seismic attenuation associated with hydrocarbon saturation. The consistent negative 
AVF gradients observed at wells B1, N1, and N2 indicate that the proposed method successfully characterizes 
gas-bearing carbonate reservoirs and provides complementary information that reduces the ambiguity commonly 
encountered in conventional AVO interpretation. 
Therefore, the results indicate that AVF analysis based on Complex Ricker Wavelet (CRW) spectral 
decomposition provides an effective and reliable approach for reservoir characterization and hydrocarbon 
identification within the study area. 
3.4 Analysis intercept vs gradient 
Analysis of wells B1, N1, and N2 shows a consistent negative AVF gradient, indicating decreasing seismic 
amplitude with increasing frequency. Well  B1 exhibits the strongest attenuation, with the highest intercept  A = 
99,683.82 and the most negative gradient B = −117,663.81, although its correlation coefficient is relatively lower R 
= 0.7825. N2 shows an intermediate response A = 72,310.45, B = −73,391.92; R = 0.8920, while N1 exhibits the 
weakest attenuation A = 51,644.29, B = −40,940.74 with the highest correlation R = 0.8992. 
The larger intercept and more negative gradient at B1 indicate stronger low-frequency dominance and greater 
high-frequency attenuation compared with N1 and N2. However, the absence of distinct clusters in the gradient –
intercept crossplots indicates that these parameters alone cannot definitively discriminate hydrocarbon presence. 
The observed differences are the refore interpreted as variations in frequency -dependent seismic response, 
potentially influenced by reservoir heterogeneity, pore structure, fluid effects, and attenuation mechanisms, and 
should be integrated with independent petrophysical evidence.

661 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 14. 
Intercept–gradient kurva & crossplot of the UBRF zone showing the distribution of AVF responses and the separation of 
anomalous points associated with potential hydrocarbon-bearing reservoir intervals. 
 
 
 
Figure 15. 
 Intercept–gradient kurva & crossplot of the BSMT zone showing the distribution of AVF responses and the separation of 
anomalous points associated with potential hydrocarbon-bearing reservoir intervals. 
 
 
 
Analysis of wells B1, N1, and N2 in the BSMT interval shows a consistent negative AVF gradient, indicating 
decreasing seismic amplitude with increasing frequency. Well N2 exhibits the strongest attenuation, with  the 
highest intercept A = 84,164.30 and the most negative gradient B = −97,618.84, with a correlation coefficient of 
0.7908. N1 shows an intermediate response A = 77,028.53; B = −85,352.24, R = 0.7606, while B1 exhibits the 
weakest attenuation A = 60,558.38, B = −68,475.92, R = 0.7984. 
The gradient magnitude follows the order N2 > N1 > B1, indicating that N2 has the strongest frequency -
dependent attenuation within the BSMT interval. However, the relatively similar correlation ccoefficients and 
absence of clear cluster separation indicate that the AVF parameters alone are insufficient to definitively discriminate 
hydrocarbon presence. The observed variations are therefore interpreted as differences in frequency -dependent 
seismic response that may reflect variations in reservoir properties, fluid effects, and geological heterogeneity. 
These results indicate that AVF analysis is capable of capturing frequency-dependent attenuation phenomena 
associated with reservoir properties. Therefore, when integrated with well-log data and geological interpretation, 
AVF attributes can provide additional insights into reservoir characterization and assist in identifying zones with 
potential hydrocarbon accumulation.

662 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
3.5 Analysis slicing A VF 
The results of Amplitude Versus Frequency (AVF) attribute slicing on the UBRF_time_map horizon  at 
intervals of 0 ms, +5 ms, +1 0 ms, and +15 ms reveal variations in amplitude distribution across several zones 
within the study area. The AVF attribute provides detailed information on amplitude and frequency responses, 
allowing changes in reservoir characteristics, subsurface geometr y, and potential hydrocarbon accumulations 
to be identified more effectively.In general red to pink colors represent relatively high amplitude values, 
whereas green to blue colors indicate lower amplitudes. High -amplitude zones are interpreted as areas wit h 
significant acoustic impedance contrasts and are therefore considered potential hydrocarbon -bearing reservoirs 
accumulations to be identified more effectively. In general, red to pink colors represent relatively high 
amplitude values, whereas green to blue colors indicate lower amplitudes. High -amplitude zones are interpreted 
as areas with significant acoustic impedance contrasts and are therefore considered potential hydrocarbon -
bearing reservoirs.  
At the 0 ms slice, a prominent high-amplitude anomaly is observed in the eastern to northeastern part of the 
study area. This zone is characterized by dominant red to pink colors with amplitude values ranging from 
approximately −1.35 × 10⁶ to −2.47 × 10⁶, contrasting sharply with the su rrounding areas, which are dominated 
by green, yellow, and blue colors with amplitudes ranging from approximately −4.0 × 10⁵ to −1.0 × 10⁶. The 
presence of this anomaly suggests a reservoir zone exhibiting a strong AVF response associated with frequency-
dependent attenuation effects (Figure 16). 
At the +5 ms interval, the high-amplitude anomaly remains well developed and displays good lateral continuity 
in the eastern and northeastern portions of the study area. The a nomaly exhibits a distribution pattern similar to  
that observed  at the  0 ms  slice, indicating  that the reservoir extends  laterally and  likely belongs to the same 
reservoir system. The persistence of high amplitudes at this interval suggests a consistent fr equency response 
related to the presence of fluids within the reservoir (Figure 17). 
 
 
Figure 16. 
 AVF attribute map at a 0-ms interval slice showing the spatial distribution of negative AVF anomalies associated with 
frequency-dependent amplitude attenuation within the target reservoir interval of the Baturaja Formation.

663 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
 
Figure 17. 
AVF attribute map at a 5-ms interval slice showing the spatial distribution of negative AVF anomalies associated with 
frequency-dependent amplitude attenuation within the target reservoir interval of the Baturaja Formation. 
 
 
 
Figure 18. 
AVF attribute map at a 10-ms interval slice showing the spatial distribution of negative AVF anomalies associated with 
frequency-dependent amplitude attenuation within the target reservoir interval of the Baturaja Formation.

664 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
At the +10 ms interval, the high -amplitude anomaly is still present in approximately the same location,  
although its areal extent begins to decrease compared to the shallower intervals. Nevertheless, the anomaly  
maintains good lateral continuity  and remains clearly identifiable.  This observation suggests that the  reservoir 
continues into this interval, although the effective reservoir thickness or quality may begin to diminish (Figure 18). 
At the +15 ms interval, high amplitudes are still observed in the eastern to northeastern area, but with a  more 
limited spatial extent and amplitude values ranging from  approximately −1.39 × 10⁶ to −2.18 × 10⁶. The 
surrounding areas are dominated by lower amplitudes, ranging from approximately −7.0 × 10⁵ to −1.2 × 10⁶, which 
may indicate a reduction in reservoir quality or proximity to the lower boundary of the reservoir interval. Despite 
this reduction, the consistent occurrence of high-amplitude anomalies across all slicing intervals indicates that the 
reservoir exhibits relatively good lateral and vertical continuity (Figure 19). 
Overall, the AVF attribute slicing results suggest that the prospective reservoir zone is predominantly 
distributed in the eastern to northeastern part of the study area. The relatively continuous distribution of high -
amplitude anomalies across multiple time slices indicates the presence of a laterally extensive reservoir body with 
favorable hydrocarbon potential. The consistency of these anomalies throughout the analyzed intervals further 
suggests good reservoir continuity both laterally and vertically. The highest concentration of AVF anomalies is 
observed in the northeastern part of the study area, corresponding to the locations of wells B1 and N1, where 
negative AVF gradients are consistently associated with low water saturation and low gamma -ray values, 
indicating gas-bearing carbonate reservoirs. In contrast, well N2 also exhibits negative AVF gradients indicative 
of gas saturation, although the anomalies are less extensive than those observed around wells B1 and N1. This 
spatial agreement between the AVF anomaly distribution and well -log interpretation demonstrates that the 
identified hydrocarbon-bearing zones are geologically consistent and laterally continuous within the carbonate 
reservoir. These results demonstrate that AVF attributes are effective for delineating reservoir distribution, 
evaluating reservoir continuity, and identifying prospective hydrocarbon-bearing zones within the Baturaja 
Formation. The successful correlation between  AVF anomalies and petrophysical evidence from all three wells 
confirms that the CWT -based AVF method is capable of effectively characterizing heterogeneous carbonate 
reservoirs. By capturing frequency -dependent attenuation associated with gas saturation,  AVF provides reliable 
complementary information for hydrocarbon  detection and reduces the uncertainty commonly encountered in 
conventional amplitude-based interpretation of carbonate reservoirs. 
 
 
Figure 19. 
AVF attribute map at a 15-ms interval slice showing the spatial distribution of negative AVF anomalies associated with 
frequency-dependent amplitude attenuation within the target reservoir interval of the Baturaja Formation.

665 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
4. Conclusion 
The integration of Continuous Wavelet Transform (CWT) and Amplitude Versus Frequency (AVF) 
successfully identifie d frequency -dependent anomalies in the Baturaja Formation. The results show low -
frequency anomalies and predominantly negative AVF gradients, indicating attenuation that may be associated 
with gas-bearing reservoir zones. The anomalies are mainly distributed in the east–northeast area and show good 
lateral continuity. Integration with well-log data, particularly water saturation and gamma-ray, provides additional 
support for the interpretation. Therefore, CWT-based AVF can be used as a complementary method for identifying 
prospective hydrocarbon zones, although it should be integrated with geological and petrophysical data for more 
reliable interpretation. 
5. Acknowledgement 
The authors would like to express their sincere gratitude to UIN Syarif Hidayatullah Jakarta, particularly the 
Physics Study Program, for the support, facilities, and academic guidance provided throughout the research and 
manuscript preparation process. The assistance and resources made available by the institution greatly contributed 
to the successful completion of this study and the preparation of this journal article. The authors also appreciate 
the valuable academic environment that fostered the development and completion of this research.  
 
6. Declarations 
6.1 Author contributions 
Tati Zera: Supervision, Methodology, Validation, Writing Review and Editing. Bahrul Ulum: 
Conceptualization, Methodology, Investigation, Data Curation, Formal Analysis, Software, Visualization, Writing 
Original Draft, Writing Review & Editing. Pradityo Riyadi: Supervision, Methodology, Validation, Visualization, 
Writing Review. Jarea Yurika Lubis: Data Curation, Formal Analysis, Software, and Visualization. 
6.2 Funding statement 
None.  
6.3 Competing interest 
None.  
6.4 The use of AI and AI-assisted technologies 
During the preparation of this work, the authors used Consensus GPT and Cloud AI to support literature 
exploration, language refinement, and manuscript drafting. The AI-assisted outputs were critically evaluated, verified 
against the original references, and substantially revised by the authors. The authors take full responsibility for the 
accuracy, integrity, and originality of the content presented in this publication. 
7. Glossary of terms and symbols 
Terms & Symbols Definition Unit 
A VF Amplitude variation 
with frequency 
Unitles 
A VO Amplitude Variation with Offset Unitles 
CWT Continous wavelet transform Unitles 
STFT Short-Time 
Fourier Transform 
Unitles 
SW Saturation Water SW 
GR Gamma Ray GR

666 
 
 
 
Ulum et al. Scientific Contributions Oil and Gas 
https://doi.org/10.29017/scog.v49i3.2122 
 
8. References 
Castagna, J. P., Sun, S., & Siegfried, R. W. (2003). Instantaneous spectral analysis: Detection of low -frequency 
shadows associated with hydrocarbons. The Leading Edge, 22(2), 120–127. https://doi.org/10.1190/1.1559038  
Durogbitan, A., Simon, E., Auduson, A., Ekene, O., & Collins, I. (2023). Use of spectral decomposition in identifying 
stratigraphic baffles below seismic resolution; A case study of UTB field, offshore Niger Delta. Journal of 
Applied Geophysics, 217, 105193. https://doi.org/10.1016/j.jappgeo.2023.105193  
Han, X., & others. (2023). Amplitude Versus Frequency (AVF). GeoConvention 2023 . 
https://geoconvention.com/wp-content/uploads/abstracts/2023/91410-amplitude-versus-frequency.pdf  
Li, H., Yin, H., Tang, J., & Xiao, P. (2024). Application of AVO Characteristics Analysis and Seismic Dispersion 
AVO Inversion to the Carbonate Hydrocarbon Reservoirs in Region Y of the Tarim Basin, China. Geofluids, 
2024(1). https://doi.org/10.1155/2024/3034459  
Li, Y., Downton, J., & Goodway, B. (2003). Recent applications of AVO to carbonate reservoirs in the Western 
Canadian Sedimentary Basin. The Leading Edge, 22(7), 670–674. https://doi.org/10.1190/1.1599694  
Mandong, A. F., Bekti, R. P. A., & Saputra, R. I. A. (2021). Amplitude Variation with Frequency as Direct 
Hydrocarbon Indicator for Quick Look and Different Insight of Hydrocarbon Delineation. Jurnal Geofisika, 
19(2), 62. https://doi.org/10.36435/jgf.v20i2.517  
Mineral, K. E. dan S. D. (2022). Peran Sektor Eksplorasi dan Produksi Migas dalam Mendukung Kebutuhan Energi 
Nasional dan Pemetaan Struktur Menggunakan Data Seismik di Cekungan Sund a. Laporan Statistik Energi 
Indonesia 2022. https://www.esdm.go.id/assets/media/content/content-laporan-statistik-energi-2022.pdf  
Partyka, G., Gridley, J ., & Lopez, J. (1999). Interpretational applications of spectral decomposition in reservoir 
characterization. The Leading Edge, 18(3), 353–360. https://doi.org/10.1190/1.1438295 
Rutherford, S. R., & Williams, R. H. (1989). Amplitude-versus-offset variations in gas sands. Geophysics, 
54(6), 680–688. https://doi.org/10.1190/1.1442696 
Satyana, A. H. (2008). Carbonate reservoir characteristics of Baturaja Formation, South Sumatra Basin. Indonesian 
Petroleum Association Proceedings. 
Setyawan, D. (2021). Hydrocarbon Mapping on Reservoir Carbonate Using AVO Inversion Method. 
JPSE (Journal o f Physical Science and Engineering) , 6(1), 19 –25. 
https://doi.org/10.17977/um024v6i12021p019  
Sheriff, T., & Geldart, L. (1995). Exploration Seismology (2nd ed.). Cambridge University Press. 
Sinha, S., Routh, P. S., Anno, P. D., & Castagna, J. P. (2005). Spectral decomposition of seismic data with 
continuous-wavelet transform. Geophysics, 70(6), P19–P25. https://doi.org/10.1190/1.2127113  
Stéphane Mallat. (2009). A Wavelet Tour of Signal Processing (3rd Edition). Elsevier. https://doi.org/10.1016/B978-
0-12-374370-1.X0001-8 
Waples, D. (2000). Geochemistry in Petroleum Exploration. Springer. 
Widarsono, B. (2022). Rock Wettability Characteristics Of Some Indonesian Limestones Case Study: Baturaja 
Formation. Scientific Contributions Oil and Gas, 34(2), 105–116. https://doi.org/10.29017/SCOG.34.2.796  
Wihardy, G. G., & Khairy, H. (2021). Slope of Spectral Amplitude: Simple Yet Effective Hydrocarbon Indicator. 
Jurnal Geofisika, 19(2), 57. https://doi.org/10.36435/jgf.v20i2.523  
Wu, X., Chapman, M., Li, X. -Y., & Boston, P. (2014). Quantitative gas saturation estimation by frequency -
dependent amplitude-versus-offset analysis. Geophysical Prospecting, 62. 
Yilmaz, Ö. (2001). Seismic Data Analysis . Society of Expl oration Geophysicists. 
https://library.seg.org/doi/book/10.1190/1.9781560801589
