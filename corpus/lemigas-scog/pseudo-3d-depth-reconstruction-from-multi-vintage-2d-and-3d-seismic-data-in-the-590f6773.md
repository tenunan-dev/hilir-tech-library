---
source_id: "lemigas-scog"
title: "Pseudo 3D Depth Reconstruction from Multi Vintage 2D and 3D Seismic Data in The Offshore Southeast Sumatra"
url: "https://journal.lemigas.esdm.go.id/index.php/SCOG/article/view/2110"
retrieved_at: "2026-10-24T14:30:45+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "REF", "GAS"]
disciplines: ["PRC"]
sha256: "590f67733834ac6b87dc5ce7702c85beeac4cb716fba5ee7c694eaeec1cad801"
collected: "manual"
---

# Pseudo 3D Depth Reconstruction from Multi Vintage 2D and 3D Seismic Data in The Offshore Southeast Sumatra

DOI org/10.29017/scog.v49i2.2110 I 593 
 
SCIENTIFIC CONTRIBUTIONS OIL AND GAS 
Testing Center for Oil and Gas  
LEMIGAS  
Journal Homepage:http://journal.lemigas.esdm.go.id   
ISSN: 2089-3361, e-ISSN: 2541-0520 
Pseudo-3D Depth Reconstruction from Multi-Vintage 
2D and 3D Seismic Data in The Offshore Southeast Sumatra 
ABSTRACT - The availability of legacy 2D seismic data in many mature basins offers an opportunity to 
generate 3D -like subsurface images without the need for expensive 3D seismic acquisition. This study 
proposes and demonstrates a workflow to construct a pseudo-3D seismic volume from multi-vintage 2D and 
3D seismic data in Offshore Southeast Sumatra. The objective is to improve subsurface imaging and depth -
structure mapping while minimizing exploration cost and time. Major challenges include variations in 
amplitude, frequency, phase, and time alignment across datasets acquired with different parameters, as well 
as determining the optimum line spacing required for reliable 3D reconstruction. The workflow begins with 
2D–3D matching and amplitude balancing, followed by spatial interpolation using the 3D Sparse Radon 
Interpolation technique, which reconstructs coherent reflectors between 2D lines. The generated pseudo -3D 
volume is then merged with available 3D seismic data to create a unified volume for interpretation. 
Subsequent time-to-depth conversion is performed using interval velocity data, and the velocity model is 
iteratively updated using time -preserving tomography based on depth mis -ties between seismic horizons 
and well markers until convergence is achieved. The resulting depth -structure map provides improved 
consistency with well control and reveals subtle structural features that are not observed in the individual 
2D datasets. The proposed approach demonstrates that pseudo -3D reconstruction from multi -vintage 2D 
seismic data can serve as a practical and cost-efficient alternative for early-stage exploration and pre-survey 
evaluation, especially in offshore areas where 3D seismic acquisition is economically constrained.  
Keywords: pseudo-3D seismic, multi-vintage 2 D data, 3D s parse radon interpolation, depth conversion, 
time-preserving tomography, Offshore Southeast Sumatra (OSES) Basin. 
Scientific Contributions Oil & Gas, Vol. 49. No. 2, June: 593 - 608 
1Universitas Indonesia, 
Master of Physics Program, Pondok Cina, Beji, Depok, Indonesia.  
2Pertamina EP 
RDTX Square, Semanggi, Setiabudi, Jakarta, Indonesia. 
Corresponding author: Dadang Ramdan (da.ramdan@gmail.com) 
Manuscript received:  February 27th, 2026; Revised: April 13th, 2026 
Approved:  May 19th, 2026; Available online: June 23th, 2026; Published: June 23th, 2026. 
Dadang Ramdan1, Abdul Haris1, Dewi Manik Darmayanti2, Permana Citra Adi2, Iwan Rudiyanto2, and 
Muhamad Yanuar Mahardi2

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
594 I DOI org/10.29017/scog.v49i2.2110  
Copyright © 2026 by Authors, Published by LEMIGAS 
How to cite this article: 
Dadang Ramdan, Abdul Haris, Dewi Manik Darmayanti, Permana Citra Adi, Iwan Rudiyanto, 
and Muhamad Yanuar Mahardi , 2026, Pseudo-3D Depth Reconstruction from Multi-Vintage 
2D a nd 3 D Seismic Data in The Offshore Southeast Sumatra , Scientific Contributions Oil 
and Gas, 49 (2) pp. 593 -608. DOI org/10.29017/scog.v49i2.2110.  
INTRODUCTION 
In mature basins, such as the Sunda basins, 
hydrocarbon exploration has become increasingly 
challenging due to geological complexity and 
reduced prospectivity. The availability of 3D 
seismic data is crucial for analyzing geological 
conditions and mapping the presence of 
hydrocarbons (Wicaksana, K. S.,  et al, 2025) . 
Consequently, 3D seismic surveys play a vital role 
in reducing exploration risk and improving 
subsurface imaging. However, acquiring new 3D 
seismic data is both costly and time -consuming. 
Fortunately, most mature basins possess extensive 
legacy datasets, including hundreds of 2D 
seismic lines and well data. These datasets 
provide an opportunity to reconstruct a 3D -like 
subsurface model without conducting new 3D 
seismic acquisition.   
Advances in seismic interpolation and data 
reconstruction techniques have greatly enhanced 
the use of legacy seismic datasets. Early 
interpolation approaches were predominantly based 
on Fourier transform methods, which performed 
well under regular sampling conditions but were 
often inadequate for sparsely and irregularly 
sampled seismic surveys. To overcome these 
limitations, various approaches have been 
continuously developed to address data sparsity 
and improve the reconstruction of incompletely 
sampled seismic datasets. These developments 
include transform -domain methods, prediction -
filter techniques, sparse reconstruction algorithms, 
and low -rank approaches, all of which aim to 
recover missing seismic information while 
preserving the continuity of geological structures 
and seismic events. 
In addition to seismic reconstruction, accurate 
structural depth maps are critical for hydrocarbon 
exploration, as reliable depth positioning directly 
impacts prospect evaluation, well planning, and 
reservoir characterization. Accurate structural 
depth maps are typically generated through pre -
stack depth migration (PSDM) or recursive seismic 
inversion (RSI) (Triyoso, W. et al, 2025) , which 
utilizes shot -gather data and a detailed velocity 
model. However, when shot -gather data are 
unavailable, depth conversion of time -migrated 
seismic data is commonly used as an alternative 
approach to generate depth maps. However, 
discrepancies between seismic horizons and well 
markers are commonly observed due to 
uncertainties in the velocity model used for time -to
-depth conversion. Consequently, velocity model 
calibration using well -control data is necessary to 
improve depth -imaging accuracy and structural 
mapping reliability. 
To address these challenges, we propose and 
demonstrate a workflow for pseudo -3D depth 
reconstruction that integrates sparse 2D seismic 
data and well information to generate a coherent 
pseudo-3D depth volume. 
 
METHODOLOGY 
The development of modern seismic 
interpolation methods, according to Bezzera, Y. S. 
F., et al., 2021, began with Fourier transform-based 
approaches, such as minimum weighted norm 
interpolation (MWNI) (Liu and Sacchi, 2004), Anti 
Leakage Fourier Transform (ALFT) (Xu, et al., 
2005), and Matching Pursuit Fourier Interpolation 
(MPFI) (Schonewille et al., 2013) , which exploit 
data sparsity in the frequency domain to 
reconstruct missing traces. Subsequently, other 
transform-based methods, including Radon and 
Curvelet transforms, were developed to improve 
reconstruction performance in more complex 
geological settings.

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 595 
0 = 𝛿𝑡 =  𝑖(𝐴𝑣∆𝑉 +𝐴𝜀∆𝜀 +𝐴𝛿∆𝛿 +𝐴𝑧∆𝑍) 
 
(4)  
𝑓(𝑥 ≔ 𝑓𝑥2).  
𝑥 
𝑑 𝑡,𝑥  
More recent advancements have focused on 
compressed sensing and sparse reconstruction 
techniques, including 3D sparse radon interpolation 
(Wang, S., 2017) , which achieve higher -quality 
reconstruction by promoting sparsity through 
optimization. 
3D sparse radon interpolation with ALPRT 
3D Sparse Radon Interpolation with Anti -
Leakage Parabolic Radon Transform (ALPRT) is 
an advanced seismic data processing technique that 
was adapted from Anti-Leakage Fourier Transform 
(ALFT) (Xu, S. et al, 2005;  Schonewille, M. et al, 
2009) used to reconstruct missing traces in 3D 
seismic datasets while minimizing energy leakage 
in the Radon domain. According to Hollander et 
al., 2019, the method starts by representing the 
seismic gather    as a combination of 
multidimensional Radon basis functions. This 
approximation can be written in the most general 
form as in Equation 1, 
d 𝑡,𝑥 ≈  𝑚𝑗
𝑗
𝑒𝑖2𝜋𝑓𝑗𝑥 2.p𝑗𝑒𝑖2𝜋𝑓𝑗𝑡 , 
(1)  
with t and f denoting the vertical regularly sampled 
dimension in the time and frequency domains, 
respectively. Following a preliminary vertical FFT 
to separate the gather into temporal frequency 
slices, each slice is approximated as Equation 2, 
where    is the vector of Radon coefficients for a 
particular frequency f. The matrix A contains in its 
columns the corresponding Fourier basis functions 
sampled at the irregular 4D spatial grid    , scaled 
for Radon by itself and by the temporal frequency.     
                      By applying a sparsity constraint, the 
algorithm selects only the most significant Radon 
coefficients to represent seismic events, which 
helps suppress noise and interpolation artifacts. 
The Anti-Leakage Parabolic Radon Transform is a 
matching pursuit approach to find a sparse  
representation of the form (2). The ALPRT is 
incorporated to reduce energy spreading 
between neighboring model parameters, a 
common problem in conventional Radon 
d 𝑓,𝑥 ≈  𝑚𝑗
𝑗
𝑒𝑖2𝜋𝑓𝑥 2.p𝑗 = Am, 
(2)  
𝑚 
transforms due to limited aperture and irregular 
sampling. This constraint improves the focusing 
of seismic events in the Radon domain and 
enhances the stability of the inversio n. Sparse 
Radon Inversion also improves the resolution of the 
Radon model by employing the L1 norm (Geng, 
W. et al, 2022) to promote sparsity in the 
transformed model. As a result, seismic energy 
is concentrated into a limited number of 
significant Radon coefficients, reducing 
smearing artifacts caused by limited data 
sampling. The objective function of sparse 
inversion can be expressed as Equation 3,   
where L denotes the Radon operator,  d represents 
the observed data,  m is the Radon model, and  λ is 
the regularization parameter . After estimating the 
optimal sparse Radon model, the data are 
transformed back to the space domain to 
reconstruct missing traces and generate a more 
regular 3D seismic grid. As a result, this method 
significantly improves reflector continuity, 
preserves structural information, and produces 
higher-quality seismic volumes for subsurface 
interpretation and pseudo-3D reconstruction. 
Time preserving tomography 
Time Preserving Tomography (TPT) is a 
technique that preserves the travel times of seismic 
events while updating the depth domain horizons 
and interval velocities by ray tracing  (Hong, Y., et 
al, 2024) . TPT aims to incorporate constraints on 
medium parameters and structure, taken from 
geological knowledge or well marker information, 
into the tomographic solution. TPT is implemented 
in structural model-based tomography, keeping the 
refined models tied to the structure as shown in 
Figure 2. The fundamental equation of TPT can be 
written as Equation 4, 
𝐽 𝑚 =  𝐿𝑚−𝑑 22 +𝜆 𝑚 1, 
(3)  
where        denotes the velocity change,         and   
represent the changes in the anisotropic parameters 
epsilon and delta, respectively, and     denotes the 
change in horizon depth. 
∆𝑉 
∆𝜀 
∆𝛿 
∆𝑍

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
596 I DOI org/10.29017/scog.v49i2.2110  
 
Data description 
 The study area, shown in Figure 3, is located 
north of Jakarta, in Offshore Southeast Sumatra. 
The input dataset consists of: 
• 148 multi-vintage 2D PSTM stack seismic lines  
• 138 2D RMS velocity lines  
Figure 1. The schematic workflow of 3D sparse parabolic Radon interpolation with ALPRT inversion methods 
was adapted from Hollander & Yilmaz 2019). 
Figure 2. Conceptual illustration of Time Preserving Tomography (TPT). 
The depth mismatch between the seismic horizon and well markers (a) is converted into a depth-mismatch map (b) and 
incorporated into the TPT formulation, allowing the model to be updated while preserving structural consistency with the 
well data(c). (modified from Rob, M., 2015) 
 
(a) (b) (c) 
• One 3D PSTM stack seismic volume  
• One 3D RMS velocity volume  
• Five wells containing sonic, density, and 
formation markers. 
The multi-vintage 2D seismic dataset consists of 
ten surveys acquired using different acquisition  
parameters, as summarized in Table 1. 
Continuous advancements in seismic acquisition

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 597 
 
technology have enabled the efficient collection 
of increasingly large volumes of seismic data, 
thereby improving the quality and spatial 
coverage of subsurface imaging . 
The workflow 
The workflow used in this study was developed 
based on methodologies previously described by 
Whiteside et al. (2013), O'Keefe et al. (2017), 
Humberto et al. (2018), and Abdullah (2022), with 
several modifications introduced to accommodate 
the characteristics of the available dataset and the 
objectives of the present study. The workflow, a s 
shown in Figure 4, is divided into two stages. Stage 
I focuses on pseudo -3D reconstruction. It begins 
with seismic matching analysis and rebinning into 
a new pseudo-3D survey geometry, followed by 3D 
post-stack interpolation. After the pseudo -3D 
volume is generated, it is merged with the existing 
3D seismic data and is ready for interpretation. 
The interpretation process begins with the 
generation of a synthetic seismogram from sonic 
and density logs, which is then convolved with a 
wavelet. Stretching and squeezing are subsequently 
applied to calibrate the synthetic seismogram to the 
seismic section. This process is iteratively 
performed until the maximum correlation 
coefficient between the synthetic seismogram and 
seismic data is achieved. 
Stage II focuses on velocity model building. 
The process begins with time -to-depth 
conversion using an initial interval velocity 
model. This interval velocity model is updated 
using the time -preserving tomography method 
based on the mis -depth information between the 
interpreted seismic horizons and well markers. 
The process is performed iteratively until 
 
Figure 3. Study area highlighted by the yellow box, comprising a dozen 2D multi-vintage seismic lines (black) 
and a 3D seismic survey (orange) (modified from Ralanarko et al., 2011).

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
598 I DOI org/10.29017/scog.v49i2.2110  
Table 1. Summary of acquisition parameters for ten multi-vintage 2D seismic surveys used in this study 
 
Vintage 80 81 82 83 87 89 90 91 93 94 
 
 Number of Channels 48 48 48 48 60 192 240 192 240 240  
 Source Interval (m) 25 25 25 25 26.6 26.6 25 25 25 25  
 Group Interval (m) 25 25 25 25 26.6 13.3 12.5 12.5 12.5 12.5  
 Delay time (ms) 61.2 51.2 51.2 0 16.43 0 0 51.2 51.2 115  
 Near offset (m) 150 87 135 100 134 118.2 150.3 143 130 108  
 Source depth (m) 7.8 7 7 5.6 6 6 5 5 5 5  
 Receiver depth (m) 8 7 7 6 6 6 6 5 5 6  
 
convergence is achieved.  
RESULT AND DISCUSSION 
Seismic matching analysis  
The seismic matching analysis functionality is 
used to identify seismic mis -ties between seismic 
sections (Abdullah, A., et al, 2022) . After the 
calculations are completed, as shown in Figure 5a,  
the resulting mis -tie values of amplitude, phase, 
and time shift are displayed in tabular form and 
then applied to the seismic sections. To control and 
evaluate the process, the results can be visualized 
in correlation windows. The maximum cross -
correlation value is obtained when the time shift is 
zero. For frequency matching, band-pass filtering is 
Figure 4. Workflow of pseudo 3D depth reconstruction 
 
applied to adjust the frequency content between the 
datasets. Matching analysis is a crucial step in 
the workflow to ensure consistency between 2D 
lines. It is done line by line to ensure the 
interpolation process produces a reliable and 
coherent seismic volume . 
After seismic matching analysis, the maximum 
correlation has a time shift value around zero, and 
the sections have the same frequency trend, as 
shown in Figure 5b.   
Pseudo 3D reconstruction 
Figure 6a shows  an example of the pseudo -3D 
reconstruction. Real 3D seismic data are shown on

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 599 
the left and right sides, and the pseudo -3D area is 
shown in the middle. The pseudo -3D area 
comprises seismic lines with 50–1000 m spacing. 
The pseudo-3D area exhibits strong spatial aliasing 
and trace gaps, resulting in discontinuous and noisy 
reflectors. Figure 6b shows a significantly 
improved seismic image of the missing traces 
obtained by interpolation and reflector continuity. 
Demonstrating that 3D sparse Radon interpolation 
recovers structural information and greatly 
facilitates seismic interpretation compared with pre
-interpolated data. T he impact of regularizing the 
section for interpretability  allows the horizon  
interpretation to be interpreted more smoothly and 
confidently from point A to B. The  interpretation 
becomes more geologically consistent. 
Interval velocity model building using TPT 
Figure 7a presents an initial pseudo -3D depth 
seismic section overlaid with an initial interval 
velocity model and well data markers, illustrating 
the relationship between seismic reflectors and 
actual well -based depth references. The initial 
pseudo-depth section is produced from time -to-
depth conversion using the interval velocity. The 
colored horizons represent the interpreted seismic 
events, and the vertical markers indicate the well 
positions and their corresponding depth picks. A 
clear depth mismatch can be observed between the 
pseudo-depth seismic reflectors and the well 
markers in the highlighted (red box) and zoomed -
in area on the right, where the seismic horizons do 
not perfectly align with the known formation tops 
from the wells. This discrepancy may indicate 
inaccuracies in the velocity model or limitations in 
the pseudo -depth conversion process, resulting in 
the mispositioning of subsurface structures. 
Overall, the image emphasizes the need for further 
calibration, such as velocity updating or depth 
refinement, to better tie the seismic data with well 
control and improve geological reliability. Figure 
7b shows a pseudo -3D depth seismic section that 
has been tied to well data markers, demonstrating 
improved alignment between seismic reflectors and 
well-known formation depths from wells. 
Compared with an untied section, the highlighted 
and zoomed -in area reveals that the seismic 
horizons now more closely match the well markers, 
reducing the previous depth mismatch as shown in 
Figure 8. This improved correlation that the depth 
model has been calibrated, likely through velocity 
updating or well -based correction, resulting in 
more accurate positioning of geological structures. 
Overall, the image emphasizes the importance of 
well ties in validating and refining pseudo -depth 
seismic interpretations to achieve higher 
confidence in subsurface mapping. 
Optimum line spacing for pseudo 3D 
reconstruction 
What is the optimum reliable line spacing for 
pseudo 3D reconstruction? To answer this question, 
we conducted an experiment using a 3D seismic 
dataset by systematically subsampling a full 3D 
seismic dataset at varying distances, as shown in 
Figure 9. The original (legacy) 3D data were 
treated as the reference, and pseudo -3D sections 
were generated using different input spacings (125 
× 125 m, 250 × 250 m, and 500 × 500 m).  
The structural fidelity of each reconstructed 
section is then quantitatively evaluated using the 
Structural Similarity Index (SSIM) by 
metadata2go.com, which measures how closely 
each pseudo -3D result resembles the original 3D 
image. SSIM is  an image quality metric proposed 
by Wang et al. (2004) to evaluate the similarity 
between two images based on structural 
information rather than pixelwise errors. SSIM 
assesses image similarity by considering 
luminance, contrast, and structural components, 
resulting in a measure that is more consistent with 
human visual perception. 
As shown in Figure 9, denser spacing (125×125 
m) preserves structural features more accurately, 
yielding higher similarity, whereas increasing the 
spacing leads to progressive degradation in the 
continuity and resolution of reflectors, reflected by 
lower SSIM values. This comparison demonstrates 
that the optimum spacing should balance 
acquisition efficiency and structural reliability, 
with closer spacing providing more accurate

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
600 I DOI org/10.29017/scog.v49i2.2110  
Figure 5. Seismic matching analysis showing (a) before and (b) after mis-tie correction. 
The correction ensures consistency among the seismic datasets in terms of amplitude, phase, time, and frequency. 
An optimal correlation window is achieved when the time shift approaches zero and the frequency spectra of the 
datasets exhibit similar trends. 
 
(a) 
(b)

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 601 
 
 
 
 
  
(a) 
Figure 6. (a) Traverse line across existing 3D seismic and pseudo-3D reconstruction areas. 
The pseudo-3D region contains missing traces with spacing varying from 50 to 1000 m. (b) The missing traces were 
reconstructed after 3D post-stack interpolation using 3D Sparse Radon Interpolation, producing a continuous seismic 
image and revealing a carbonate structure or body that was not previously visible. 
(b)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
602 I DOI org/10.29017/scog.v49i2.2110  
 
(b) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
Figure 7. (a) The traverse line across the well location shows a depth between the initial pseudo 3d depth section and 
the well marker data, and (b) the pseudo depth section is tied to the well marker data. 
(a)

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 603 
 
 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
  
(c) 
(a) 
Figure 8. Comparison of depth mismatch before (blue) and after (orange) velocity model updating for the H1 (a), H2 (b), 
and H3 (c) formations.   The reduced mismatch after updating indicates improved depth-model accuracy. 
(b)

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 591-606 
 
604 I DODOI org/10.29017/scog.v49i2.2110 
 
Figure 9.   Structural similarity index (SSIM) comparison between pseudo-3D volumes generated from varying line spacings and the legacy 3D seismic volume. Higher 
SSIM values indicate greater similarity between the compared seismic images. Higher similarity scores indicate the two images were the same and vice versa

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 605 
 
 
pseudo-3D reconstruction. 
Limitation 
The 3D sparse Radon interpolation method has 
several limitations. The reconstruction result is 
strongly dependent on the input line spacing, where 
wider spacing may reduce the interpolated pseudo -
3D volume’s reliability. This is in line with another 
previous study by Humberto, P. et al. (2018). 
Furthermore, the sparsity regularization applied in 
the inversion process may cause a loss of 
absolute amplitude and introduce amplitude 
distortion, making the method unsuitable for 
quantitative seismic analyses such as amplitude -
based interpretation .  
The Time Preserving Tomography (TPT) 
method also has several limitations. The accuracy 
of the updated velocity model is highly dependent 
on the availability and distribution of well data 
used as calibration references. Furthermore, the 
method cannot directly resolve anomalous velocity 
effects, such as pull -up effects, because the 
velocity update process mainly relies on mis -
depth information between seismic interpretation 
and well markers . 
In addition to the two abovementioned points, 
the frequency matching step in the workflow may 
cause a loss of high-frequency content, as shown in 
Figure 10,  due to the balancing of frequency 
content between the datasets. An additional 
processing step is recommended to overcome this 
issue and obtain more robust results, as shown in 
Figure 11. First, the 2D multivintage seismic data 
should be reprocessed from the raw gathers 
using consistent processing parameters across all 
datasets. The pseudo -3D depth reconstruction 
workflow can be applied after the PSTM 
Figure 10. Frequency matching between seismic datasets of different vintages. The dataset represented by the blue 
spectrum contains higher-frequency content than the red spectrum and is therefore subjected to a high-cut filter to 
achieve spectral consistency, resulting in the loss of high-frequency energy.   
Figure 11. An additional workflow is proposed to achieve more robust and reliable results. In this approach, the multi-
vintage 2D seismic datasets should be reprocessed from the raw gathers using a consistent processing sequence and 
parameters across all surveys before proceeding with the pseudo-3D depth reconstruction workflow. This would 
improve data consistency, minimize vintage-related discrepancies, and enhance the quality of the reconstructed pseudo
-3D depth volume.

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
606 I DOI org/10.29017/scog.v49i2.2110  
Terms & 
Symbols Definition Unit 
ALPRT Anti-leakage parabolic 
radon transform 
 
MWNI Minimum weighted norm  
 
 
Interpolation 
 
OSES Offshore southeast 
sumatra   
 
PSTM Pre-stack Time Migration 
 
PSDM Pre-stack Depth 
Migration 
 
RMS Root mean square 
 
SSIM Structural similarity index 
 
SSA Singular spectrum 
analysis 
 
TPT Time preserving 
tomography 
 
 
sections are generated . 
CONCLUSION 
In conclusion, the proposed pseudo -3D depth 
reconstruction workflow has demonstrated its 
effectiveness in enhancing the value of sparse multi
-vintage 2D seismic datasets. The results show that 
seismic matching analysis is a crucial step in the 
workflow to produce coherent 2D seismic lines. 
3D sparse Radon interpolation methods 
successfully reconstruct coherent 2D seismic lines 
into consistent pseudo-3D seismic volumes.  
An optimum line spacing of 100-250 m provides 
reliable pseudo -3D reconstruction, achieving a 
structural similarity index (SSIM) score exceeding 
68% relative to the legacy 3D reference data.  
Time-preserving tomography successfully 
generated a reliable velocity model, as 
demonstrated by the pseudo -depth section, which 
exhibits strong correlation and accurate tying with 
well marker data. 
 
ACKNOWLEDGMENT 
The author would like to express sincere 
appreciation to Prof. Dr. rer. nat. Abdul Haris for 
his invaluable guidance and supervision throughout 
this study. The author also gratefully acknowledges 
PT. Pertamina EP for providing the data, 
computational facilities, and permission to publish 
this work. 
 
DECLARATIONS 
Author contribution 
D. Ramdan: conceptualization, 
methodology, data processing, data curation, 
data analysis, visualization, writing original 
draft, writing review & editing. A. Haris: 
Supervision (co), methodology, validation, 
writing review & editing. D.M. Darmayanti: 
Supervision (co), data collecting, seismic 
interpretation, writing review. P.C. Adi: 
Supervision (co), writing review. I. 
Rudiyanto: Supervision (co), data access 
authorization. M. Y. Mahardi: Supervision 
(co), data access authorization.   
Funding statement  
 The authors declare that they have no 
known competing financial interests or 
personal relationships that could have 
influenced the work reported in this paper. 
Competing interest  
The authors declare that they have no 
known competing financial interests or 
personal relationships that could have 
influenced the work reported in this paper. 
The use of AI or AI-assisted technologies 
The author(s) used ChatGPT to assist. After 
using this tool, the authors review and edit the 
content as needed and take full responsibility 
for the publication's content 
 
GLOSSARY OF TERMS AND SYMBOLS 
REFERENCES 
Abdullah, A. & Basyuni, S., (2022), Pseudo 3D 
Seismic Generation From Multi-Vintage 2D and 
3D Seismic data  for Hydrocarbon Exploration 
at Eastern Indonesian Basin, Indonesian 
Petroleum Association  46 th CONVEX, Jakarta: 
21-23 September 2022,  ISBN: 978 -602-8601-

Pseudo-3D Depth Reconstruction from Multi-Vintage 2D and 3D Seismic Data 
in The Offshore Southeast Sumatra (Ramdan et al.) 
 
DOI org/10.29017/scog.v49i2.2110  I 607 
28-3. 
Bevc, D., Neodorub, O., Hollander, Y., & Yilmaz, 
O., (2019), An acceleration method for the anti -
leakage parabolic Radon transform for seismic 
data interpolation, SEG Technical Program 
Expanded Abstract 2019,  https://
doi.org/10.1190/segam2019-3199275.. 
Bezerra, Y. S. F., Garabito, G., and Sacchi, M. D., 
(2021), A comparative study of 
multidimensional Fourier reconstruction of 2D 
prestack seismic data ’, Journal of Applied 
Geophysics,https://doi.org/10.1016/
j.jappgeo.2021.104445. 
Geng, W., Li, J., Chen, X., Ma, J., Xu, J., Zhu, G. 
and Tang, W, (2022), 3D high -order sparse 
radon transform with L1 –2 minimization for 
multiple attenuation, Geophysical Prospecting, 
70: 655 -676. https://doi.org/10.1111/1365 -
2478.13185. 
Hong, Y., Cambois, G., Al Neyadi, A. A., Cowell, 
J., Aljaberi, F., Al Kaabi, A. S., & Puri, A. K., 
(2024), Time -Preserving Tomography in 
Structure Mapping: A Case Study of a Deep 
Gas Reservoir, Offshore Abu Dhabi. Abu Dhabi 
International Petroleum Exhibition & 
Conference 2024, Abu Dhabi: 4 -7 November 
2024,  https://doi.org/10.2118/222921-M. 
Humberto, P., Neves, F., Caerio, M. H., & Gomes, 
J., (2018), First Abu Dhabi 2D/3D Seismic 
Merge. Fast Track Approach For Seismic Data 
Integration at Regional Scale in Exploration 
Studies, Abu Dhabi International Petroleum 
Exhibition & Conference 2018, Abu Dhabi: 12 -
15 November 2018,  https://
doi.org/10.2118/193066-M. 
Metadata2Go, (2026), Metadata2Go: Online 
metadata and image analysis tool, QaamGo 
Web GmbH. Metadata2G.com, Accessed March 
19, 2026. 
O’Keefe, S., Ratnett, N., Woodburn, N., Pedersen, 
C., Bradbury, W., Guo, M., and Whiteside, 
W., (2018), The development and 
applicability of structurally conformable 2D 
to 3D interpolation, SEG International 
Exposition and 87 th Annual Meeting, 
Houston: 24 -29 September 2017,  https://
doi.org/10.1190/segam2017 -17723357.  
Ralanarko, D., Wahyuadi, D., Nugroho, P., 
Rulandoko, W., Syafri, I., Almabrury, A., and 
Nur, A, A., (2020), Seismic Expression of 
Paleogene Talangakar Formation – Asri & 
Sunda Basin, Java Sea, Indonesia, Berita 
Sedimentology : Indonesian Journal of 
Sedimentary Geology, Vol 46, No 1. 
Robb, M., (2015), Time Preserving Tomography 
(TPT) - Velocity Refinement through 
Tomographic Depthing, Paradigm Gephysical 
Schonewille, M., Klaedtke, A., Vigner, A., Brittan, 
J., & Martin, T., (2009), Seismic data 
regularization with the anti -alias anti -leakage 
Fourier transform, First Break 27(9): 85 -92. 
https://doi.org/10.3997/1365-
2397.27.1304.32570. 
Triyoso, W., & Hutapea, F. L., (2025), The Use of 
the Common Offset of the Common Reflection 
Surface (CO -CRS) for Velocity Analysis and 
Data Preconditioning.  Scientific Contributions 
Oil and Gas , 48(4), 165 -177. https://
doi.org/10.29017/scog.v48i4.193. 
Wang, Y., Gong, X., & Hu, B., (2024), Seismic 
Data Reconstruction Using a Phase -Shift-Plus-
Interpolation-Based Apex -Shifted Hyperbolic 
Radon Transform, Remote Sens. 2024, 16, 
1114. https://doi.org/10.3390/ rs16071114. 
Wang, S., Li, J., Xue, Y., Zhou, Y., & Ma, X., 
(2017), AVO -Preserving Data Reconstruction 
by 3D High -Order Sparse Parabolic Radon 
Transform, SEG International Exposition and 
87th Annual Meeting, Houston. 
Wang, Z., Bovik, A. C., Sheikh, H. R.,  & 
Simoncelli, E. P., (2004), Image quality 
assessment: from error visibility to structural 
similarity, IEEE Transactions on Image 
Processing, Vol. 13, 600 -612, https://
doi.org/10.1109/ TIP.2003.819861. 
Whiteside, W., Wang, B., Bondeson, H., & Li, Z., 
(2013), Enhanced 3D Imaging from 2D Seismic 
Data and its Application to Surveys in the North 
Sea, EAGE Conference & Exhibition 
incorporating SPE EUROPEC, London: 10 -13

Scientific Contributions Oil & Gas, Vol. 49. No. 2, June 2026: 593-608 
 
608 I DOI org/10.29017/scog.v49i2.2110  
June 2013.  
Wicaksana, K. S., Pasaribu, D., & Purba, H. , 
(2025), Structural Configuration And 
Paleogeography of The Krishna Field in The 
Sunda Basin.  Scientific Contributions Oil and 
Gas, 48(4), 463 -487. https://doi.org/10.29017/
scog.v48i4.1964. 
Xu, S., Zhang, Y., Pham, D., & Lambare, G., 
(2005), Antileakage Fourier transform for 
seismic data regularization’, Geophisic, Vol. 70, 
No. 4 (July -August 2005); P. V87 -V95, 17 
FIGS.  https://doi.org/10.1190/1.199371.
