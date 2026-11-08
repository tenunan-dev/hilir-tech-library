---
source_id: "wikipedia"
title: "Ultrasonic_flow_meter"
url: "https://en.wikipedia.org/wiki/Ultrasonic_flow_meter"
retrieved_at: "2026-11-08T15:35:02+00:00"
licence: "CC-BY-SA-4.0"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"]
disciplines: ["PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
sha256: "3bd6dd4796bf9ab60d44ad0254aa2fabb284919c1802b547277cacbce713c34d"
collected: "manual"
summary: "Wikipedia overview of ultrasonic flow meters: transit-time and Doppler measurement principles, clamp-on and inline configurations and their custody-transfer use in gas metering."
---

# Ultrasonic_flow_meter

# Ultrasonic flow meter

An **ultrasonic flow meter** is a type of flow meter that measures the velocity of a  fluid with ultrasound to calculate volume flow. Using ultrasonic transducers, the flow meter can measure the average velocity along the path of an emitted beam of ultrasound, by averaging the difference in measured transit time between the pulses of ultrasound propagating into and against the direction of the flow or by measuring the frequency shift from the Doppler effect. Ultrasonic flow meters are affected by the acoustic properties of the fluid and can be impacted by temperature, density, viscosity and suspended particulates depending on the exact flow meter. They vary greatly in purchase price but are often inexpensive to use and maintain because they do not use moving parts, unlike mechanical flow meters.

## Means of operation

\[edit\]
There are three different types of ultrasonic flow meters. Transmission (or contrapropagating transit-time) flow meters can be distinguished into in-line (intrusive, wetted) and clamp-on (non-intrusive) varieties. Ultrasonic flow meters that use the Doppler shift are called reflection or Doppler flow meters. The third type is the open-channel flow meter.<sup>\[1\]</sup>

## Principle

\[edit\]
### Time transit flow meter

\[edit\]
Ultrasonic flow meters measure the difference between the transit time of ultrasonic pulses propagating with and against the flow direction. This time difference (TTFM = Transit Time Flow Measurement) is a measure for the average velocity of the fluid along the path of the ultrasonic beam. By using the absolute transit times  and , both the averaged fluid velocity  and the speed of sound  can be calculated. Using these two transit times, the distance between receiving and transmitting transducers  and the inclination angle , if we assume that sound has to go against the flow when going upstream and along the flow when going downstream,<sup>\[2\]</sup> then one can write the following two equations from the definition of velocity:

and

By adding and subtracting the above equations can solve for and ,

and

where is the average velocity of the fluid along the sound path and is the speed of sound.

### Doppler shift flow meters

\[edit\]
Another method in ultrasonic flow metering is the use of the Doppler shift that results from the reflection of an ultrasonic beam off sonically reflective materials, such as solid particles or entrained air bubbles in a flowing fluid, or the turbulence of the fluid itself, if the liquid is clean.

Doppler flowmeters are used for slurries, liquids with bubbles, gases with sound-reflecting particles.

This type of flow meter can also be used to measure the rate of blood flow, by passing an ultrasonic beam through the tissues, bouncing it off a reflective plate, then reversing the direction of the beam and repeating the measurement, the volume of blood flow can be estimated. The frequency of the transmitted beam is affected by the movement of blood in the vessel and by comparing the frequency of the upstream beam versus downstream the flow of blood through the vessel can be measured. The difference between the two frequencies is a measure of true volume flow. A wide-beam sensor can also be used to measure flow independent of the cross-sectional area of the blood vessel.

### Open channel flow meters

\[edit\]
In this case, the ultrasonic element is actually measuring the height of the water in the open channel; based on the geometry of the channel, the flow can be determined from the height. The ultrasonic sensor usually also has a temperature sensor with it because the speed of sound in air is affected by the temperature.

## See also

\[edit\]
## References

\[edit\]
1. ↑ "How Does an Ultrasonic Flow Meter Work".
2. ↑ Analog Devices. "Configuring the MAX35101 Time-to-Digital Converter as an Ultrasonic Water Meter". *Analog Devices*. Retrieved 2024-09-27.

- Lipták, Béla G.: Process Measurement and Analysis, Volume 1. CRC Press (2003), ISBN 0-8493-1083-0 (v. 1)
- Ultrasonic Acoustic Sensing Brown University
- Lynnworth, L.C.: Ultrasonic Measurements for Process Control. Academic Press, Inc. San Diego. ISBN 0-12-460585-0
