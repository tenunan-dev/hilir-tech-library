---
source_id: "wikipedia"
title: "Tunable_diode_laser_absorption_spectroscopy"
url: "https://en.wikipedia.org/wiki/Tunable_diode_laser_absorption_spectroscopy"
retrieved_at: "2026-11-08T02:07:16+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "633e4da1f4e86f62fbd4e1347edafb783a0be7a46a243cb412aec077a8227362"
collected: "manual"
summary: "Wikipedia overview of tunable diode laser absorption spectroscopy: line-selective optical gas measurement, its absorption principle and industrial process and emissions applications."
---

# Tunable_diode_laser_absorption_spectroscopy

# Tunable diode laser absorption spectroscopy

**Tunable diode laser absorption spectroscopy** (**TDLAS**, sometimes referred to as TDLS, TLS or TLAS<sup>\[1\]</sup>) is a technique for measuring the concentration of certain species such as methane, water vapor and many more, in a gaseous mixture using tunable diode lasers and laser absorption spectrometry. The advantage of TDLAS over other techniques for concentration measurement is its ability to achieve very low detection limits (of the order of ppb). Apart from concentration, it is also possible to determine the temperature, pressure, velocity and mass flux of the gas under observation.<sup>\[2\]</sup><sup>\[3\]</sup> TDLAS is by far the most common laser based absorption technique for quantitative assessments of species in gas phase.

## Working

\[edit\]
A basic TDLAS setup consists of a tunable diode laser light source, transmitting (i.e. beam shaping) optics, optically accessible absorbing medium, receiving optics and detector/s. The emission wavelength of the tunable diode laser, viz. VCSEL, DFB, etc., is tuned over the characteristic absorption lines of a species in the gas in the path of the laser beam. This causes a reduction of the measured signal intensity due to absorption, which can be detected by a photodiode, and then used to determine the gas concentration and other properties as described later.<sup>\[4\]</sup>

Different diode lasers are used based on the application and the range over which tuning is to be performed. Typical examples are InGaAsP/InP (tunable over 900 nm to 1.6 μm), InGaAsP/InAsP (tunable over 1.6 μm to 2.2 μm), etc. These lasers can be tuned by either adjusting their temperature or by changing injection current density into the gain medium. While temperature changes allow tuning over 100 cm<sup>−1</sup>, it is limited by slow tuning rates (a few hertz), due to the thermal inertia of the system. On the other hand, adjusting the injection current can provide tuning at rates as high as \~10 GHz, but it is restricted to a smaller range (about 1 to 2 cm<sup>−1</sup>) over which the tuning can be performed. The typical laser linewidth is of the order of 10<sup>−3</sup>  cm<sup>−1</sup> or smaller.  Additional tuning, and linewidth narrowing, methods include the use of extracavity dispersive optics.<sup>\[5\]</sup>

## Basic principles

\[edit\]
### Concentration measurement

\[edit\]
The basic principle behind the TDLAS technique is simple. The focus here is on a single absorption line in the absorption spectrum of a particular species of interest. To start, the wavelength of a diode laser is tuned over a particular absorption line of interest and the intensity of the transmitted radiation is measured. The transmitted intensity can be related to the concentration of the species present by the Beer-Lambert law, which states that when a radiation of wavenumber  passes through an absorbing medium, the intensity variation along the path of the beam is given by,<sup>\[6\]</sup>

where,

- is the transmitted intensity of the radiation after it has traversed a distance through the medium,
- is the initial intensity of the radiation,
- is the absorbance of the medium,
- is the absorption cross-section of the absorbing species,
- is the number density of the absorbing species,
- is the line strength (i.e. the total absorption per molecule) of the absorbing species at temperature ,
- is the lineshape function for the particular absorption line. Sometimes also represented by ,
- is the center frequency of the spectrum.

### Temperature measurement

\[edit\]
The above relation requires that the temperature of the absorbing species is known. However, it is possible to overcome this difficulty and measure the temperature simultaneously. There are number of ways to measure the temperature. A widely applied method, which can measure the temperature simultaneously, uses the fact that the line strength is a function of temperature alone. Here two different absorption lines for the same species are probed while sweeping the laser across the absorption spectrum, the ratio of the integrated absorbance, is then a function of temperature alone.

where,

- is some reference temperature at which the line strengths are known,
- is the difference in the lower energy levels involved in the transitions for the lines being probed.

Another way to measure the temperature is by relating the FWHM of the probed absorption line to the Doppler line width of the species at that temperature. This is given by,

where,

- is the weight of one molecule of the species, and
- is the molecular weight of the species.

Note: In the last expression, is in kelvins and is in g/mol. However, this method can be used, only when the gas pressure is low (of the order of few mbar). At higher pressures (tens of millibars or more), pressure or collisional broadening becomes important and the lineshape is no longer a function of temperature alone.

### Velocity measurement

\[edit\]
The effect of a mean flow of the gas in the path of the laser beam can be seen as a shift in the absorption spectrum, also known as Doppler shift. The shift in the frequency spectrum is related to the mean flow velocity by,

where,

- is the angle between the flow direction and the laser beam direction.

Note :  is not the same as the one mentioned before where it refers to the width of the spectrum. The shift is usually very small (3×10<sup>−5</sup> cm<sup>−1</sup> ms<sup>−1</sup> for near-IR diode laser) and the shift-to-width ratio is of the order of 10<sup>−4</sup>.

## Limitations and means of improvement

\[edit\]
The main disadvantage of absorption spectrometry (AS) as well as laser absorption spectrometry (LAS) in general is that it relies on a measurement of a small change of a signal on top of a large background. Any noise introduced by the light source or the optical system will deteriorate the detectability of the technique. The sensitivity of direct absorption techniques is therefore often limited to an absorbance of \~10<sup>−3</sup>, far away from the shot noise level, which for single pass direct AS (DAS) is in the 10<sup>−7</sup> – 10<sup>−8</sup> range. Since this is insufficient for many types of applications, AS is seldom used in its simplest mode of operation.

There are basically two ways to improve on the situation; one is to reduce the noise in the signal, the other is to increase the absorption. The former can be achieved by the use of a modulation technique, whereas the latter can be obtained by placing the gas inside a cavity in which the light passes through the sample several times, thus increasing the interaction length. If the technique is applied to trace species detection, it is also possible to enhance the signal by performing detection at wavelengths where the transitions have larger line strengths, e.g. using fundamental vibrational bands or electronic transitions.

### Modulation techniques

\[edit\]
Modulation techniques make use of the fact that technical noise usually decreases with increasing frequency (which is why it is often referred to as 1/f noise) and improve the signal to noise ratio by encoding and detecting the absorption signal at a high frequency, where the noise level is low. The most common modulation techniques are wavelength modulation spectroscopy (WMS) and frequency modulation spectroscopy (FMS).

In WMS the wavelength of the light is continuously scanned across the absorption profile, and the signal is detected at a harmonic of the modulation frequency.

In FMS, the light is modulated at a much higher frequency but with a lower modulation index. As a result, a pair of sidebands separated from the carrier by the modulation frequency appears, giving rise to a so-called FM-triplet. The signal at the modulation frequency is a sum of the beat signals of the carrier with each of the two sidebands. Since these two sidebands are fully out of phase with each other, the two beat signals cancel in the absence of absorbers. However, an alteration of any of the sidebands, either by absorption or dispersion, or a phase shift of the carrier, will give rise to an unbalance between the two beat signals, and therefore a net-signal.

Although in theory baseline-free, both modulation techniques are usually limited by residual amplitude modulation (RAM), either from the laser or from multiple reflections in the optical system (etalon effects). If these noise contributions are held low, the sensitivity can be brought into the 10<sup>−5</sup> – 10<sup>−6</sup> range or even better.

In general the absorption imprints are generated by a straight line light propagation through a volume with the specific gas. To further enhance the signal, the pathway of the light travel can be increased with multi-pass cells. There is however a variety of the WMS-technique that utilizes the narrow line absorption from gases for sensing even when the gases are situated in closed compartments (e.g. pores) inside solid materia. The technique is referred to as gas in scattering media absorption spectroscopy (GASMAS).

### Cavity-enhanced absorption spectrometry (CEAS)

\[edit\]
The second way of improving the detectability of TDLAS technique is to extend the interaction length. This can be obtained by placing the species inside a cavity in which the light bounces back and forth many times, whereby the interaction length can be increased considerably. This has led to a group of techniques denoted as cavity enhanced AS (CEAS). The cavity can either be placed inside the laser, giving rise to intracavity AS, or outside, when it is referred to as an external cavity. Although the former technique can provide a high sensitivity, its practical applicability is limited because of all the non-linear processes involved.

External cavities can either be of multi-pass type, i.e. Herriott or White cells, of non- resonant type (off-axis alignment), or of resonant type, most often working as a Fabry–Pérot (FP) etalon. Multi-pass cells, which typically can provide an enhanced interaction length of up to \~2 orders of magnitude, are nowaday common together with TDLAS.

Resonant cavities can provide a much larger path length enhancement, in the order of the finesse of the cavity, *F*, which for a balanced cavity with high reflecting mirrors with reflectivities of \~99.99–99.999% can be \~ 10<sup>4</sup> to 10<sup>5</sup>. It should be clear that if all this increase in interaction length can be utilized efficiently, this vouches for a significant increase in detectability. A problem with resonant cavities is that a high finesse cavity has very narrow cavity modes, often in the low kHz range (the width of the cavity modes is given by FSR/F, where FSR is the free-spectral range of the cavity, which is given by  *c*/2*L*, where *c* is the speed of light and *L* is the cavity length). Since cw lasers often have free-running linewidths in the MHz range, and pulsed even larger, it is non-trivial to couple laser light effectively into a high finesse cavity.

The most important resonant CEAS techniques are cavity ring-down spectrometry (CRDS), integrated cavity output spectroscopy (ICOS) or cavity enhanced absorption spectroscopy (CEAS), phase-shift cavity ring-down spectroscopy (PS-CRDS) and Continuous wave Cavity Enhanced Absorption Spectrometry (cw-CEAS), either with optical locking, referred to as (OF-CEAS),<sup>\[7\]</sup> as has been demonstrated Romanini et al.<sup>\[8\]</sup> or by electronic locking.,<sup>\[8\]</sup> as for example is done in the Noise-Immune Cavity-Enhanced Optical-Heterodyne Molecular Spectroscopy (NICE-OHMS) technique.<sup>\[9\]</sup><sup>\[10\]</sup><sup>\[11\]</sup> or combination of frequency modulation and optical feedback locking CEAS, referred to as (FM-OF-CEAS).<sup>\[12\]</sup>

The most important non-resonant CEAS techniques are off-axis ICOS (OA-ICOS)<sup>\[13\]</sup> or off-axis CEAS (OA-CEAS), wavelength modulation off-axis CEAS (WM-OA-CEAS),<sup>\[14\]</sup> off-axis phase-shift cavity enhanced absorption spectroscopy (off-axis PS-CEAS).<sup>\[15\]</sup>

These resonant and non-resonant cavity enhanced absorption techniques have so far not been used that frequently with TDLAS. However, since the field is developing fast, they will presumably be more used with TDLAS in the future.

## Applications

\[edit\]
Freeze-drying (lyophilization) cycle development and optimization for pharmaceuticals.

Flow diagnostics in hypersonic/re-entry speed research facilities and scramjet combustors.

Oxygen tunable diode laser spectrometers play an important role in safety applications in a wide range of industrial processes, for this reason, TDLS are often an integral part of modern chemical plants. The fast response time compared to other technologies for measuring gas composition, and the immunity to many background gasses and environmental conditions makes TDL technology a commonly selected technology for monitoring of combustible gasses in process environments. This technology is employed on flares, in vessel headspace and in other locations where explosive atmospheres must be prevented from forming.<sup>\[16\]</sup> According to a 2018 research study, TDL technology is the 4th most commonly selected technology for gas analysis in Chemical Processing.<sup>\[17\]</sup>

## See also

\[edit\]
## References

\[edit\]
1. ↑ "nanoplus| Tunable Diode Laser Absorption Spectroscopy (TDLAS)". *nanoplus.com*. Retrieved 2020-05-17.
2. ↑ Cassidy, D. T.; Reid, J. (1982-04-01). "Atmospheric pressure monitoring of trace gases using tunable diode lasers". *Applied Optics*. **21** (7). The Optical Society: 1185–1190. Bibcode:1982ApOpt..21.1185C. doi:10.1364/ao.21.001185. ISSN 0003-6935. PMID 20389829.
3. ↑ Werle, Peter; Slemr, Franz; Maurer, Karl; Kormann, Robert; Mücke, Robert; Jänker, Bernd (2002). "Near- and mid-infrared laser-optical sensors for gas analysis". *Optics and Lasers in Engineering*. **37** (2–3). Elsevier BV: 101–114. Bibcode:2002OptLE..37..101W. doi:10.1016/s0143-8166(01)00092-6. ISSN 0143-8166.
4. ↑ Nadir, Zeeshan; Brown, Michael S.; Comer, Mary L.; Bouman, Charles A. (2017). "A Model-Based Iterative Reconstruction Approach to Tunable Diode Laser Absorption Tomography". *IEEE Transactions on Computational Imaging*. **3** (4). Institute of Electrical and Electronics Engineers (IEEE): 876–890. Bibcode:2017ITCI....3..876N. doi:10.1109/tci.2017.2690143. ISSN 2333-9403. S2CID 28611386.
5. ↑ P. Zorabedian, Tunable external cavity semiconductor lasers, in *Tunable Lasers Handbook*, F. J. Duarte (Ed.) (Academic, New York, 1995), Chapter 8.
6. ↑ See Bernath, Peter F. (2005), C7§6 p.272–274.
7. ↑ D. Romanini, A. A. Kachanav, J. Morville, and M. Chenevier, Proc. SPIE EUROPTO (Ser. Environmental Sensing) 3821(8), 94 (1999)
8. 1 2 Morville, J.; Kassi, S.; Chenevier, M.; Romanini, D. (2005-05-31). "Fast, low-noise, mode-by-mode, cavity-enhanced absorption spectroscopy by diode-laser self-locking" (PDF). *Applied Physics B*. **80** (8). Springer Science and Business Media LLC: 1027–1038. Bibcode:2005ApPhB..80.1027M. doi:10.1007/s00340-005-1828-z. ISSN 0946-2171. S2CID 120346016.
9. ↑ Ma, Long-Sheng; Ye, Jun; Dubé, Pierre; Hall, John L. (1999-12-01). "Ultrasensitive frequency-modulation spectroscopy enhanced by a high-finesse optical cavity: theory and application to overtone transitions of C<sub>2</sub>H<sub>2</sub> and C<sub>2</sub>HD". *Journal of the Optical Society of America B*. **16** (12). The Optical Society: 2255–2268. Bibcode:1999JOSAB..16.2255M. doi:10.1364/josab.16.002255. ISSN 0740-3224.
10. ↑ Taubman, Matthew S.; Myers, Tanya L.; Cannon, Bret D.; Williams, Richard M. (2004). "Stabilization, injection and control of quantum cascade lasers, and their application to chemical sensing in the infrared". *Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy*. **60** (14). Elsevier BV: 3457–3468. Bibcode:2004AcSpA..60.3457T. doi:10.1016/j.saa.2003.12.057. ISSN 1386-1425. PMID 15561632.
11. ↑ Schmidt, Florian M.; Foltynowicz, Aleksandra; Ma, Weiguang; Lock, Tomas; Axner, Ove (2007). "Doppler-broadened fiber-laser-based NICE-OHMS – Improved detectability". *Optics Express*. **15** (17). The Optical Society: 10822–10831. Bibcode:2007OExpr..1510822S. doi:10.1364/oe.15.010822. ISSN 1094-4087. PMID 19547439.
12. ↑ Kasyutich, Vasili L.; Sigrist, Markus W. (2013-02-02). "Characterisation of the potential of frequency modulation and optical feedback locking for cavity-enhanced absorption spectroscopy". *Applied Physics B*. **111** (3). Springer Science and Business Media LLC: 341–349. arXiv:1212.3825. Bibcode:2013ApPhB.111..341K. doi:10.1007/s00340-013-5338-0. ISSN 0946-2171. S2CID 253855037.
13. ↑ Paul, Joshua B.; Lapson, Larry; Anderson, James G. (2001-09-20). "Ultrasensitive absorption spectroscopy with a high-finesse optical cavity and off-axis alignment". *Applied Optics*. **40** (27). The Optical Society: 4904–4910. Bibcode:2001ApOpt..40.4904P. doi:10.1364/ao.40.004904. ISSN 0003-6935. PMID 18360533.
14. ↑ Kasyutich, V.L.; Canosa-Mas, C.E.; Pfrang, C.; Vaughan, S.; Wayne, R.P. (2002-11-01). "Off-axis continuous-wave cavity-enhanced absorption spectroscopy of narrow-band and broadband absorbers using red diode lasers". *Applied Physics B: Lasers and Optics*. **75** (6–7). Springer Science and Business Media LLC: 755–761. Bibcode:2002ApPhB..75..755K. doi:10.1007/s00340-002-1032-3. ISSN 0946-2171. S2CID 120045701.
15. ↑ Kasyutich, Vasili L.; Martin, Philip A.; Holdsworth, Robert J. (2006). "Effect of broadband amplified spontaneous emission on absorption measurements in phase-shift off-axis cavity enhanced absorption spectroscopy". *Chemical Physics Letters*. **430** (4–6). Elsevier BV: 429–434. Bibcode:2006CPL...430..429K. doi:10.1016/j.cplett.2006.09.007. ISSN 0009-2614.
16. ↑ "Tunable Diode Laser Spectroscopy: Theory & Background". Mettler-Toledo LLC. Retrieved 29 July 2021.
17. ↑ Purdum, Traci. "Gas Analytics: Study find ROI, Accuracy, Proof Key Factors". Chemical Processing. Retrieved 29 July 2021.
