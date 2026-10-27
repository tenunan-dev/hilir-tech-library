---
source_id: "azeez-torque-drag-thesis"
title: "Torque and Drag Analysis (MSc thesis, Technical University of Crete, 2019)"
url: "https://id.scribd.com/document/625547964/Azeez-Mustafa-MSc-2019-1"
retrieved_at: "2026-10-27T00:24:50+00:00"
licence: "proprietary"
reuse_level: "full-text-restricted"
permitted_use: "personal-non-commercial"
sectors: ["UPS"]
disciplines: ["PRC", "ROT"]
sha256: "df12b64900d55ec5bfb8e0e6f3595b8203f59a4acbccf7d2e1eb8d5d435db2e2"
summary: "MSc thesis by Mustafa Shamss Alah Azeez covering torque and drag theory for directional and horizontal wells, soft-string versus stiff-string model assumptions, and spreadsheet-based field case calculations of drag, surface torque and margin of overpull."
collected: "manual"
use_note: "Private reference copy. Do not redistribute or use commercially; cite the url."
---

# Torque and Drag Analysis (MSc thesis, Technical University of Crete, 2019)

TECHNICAL UNIVERSITY OF CRETE

SCHOOL OF MINERAL RESOURCES ENGINEERING

MSc in Petroleum Engineering

TORQUE AND DRAG ANALYSIS

A Thesis

By

Mustafa Shamss Alah Azeez

To be presented to:

The Department of Mineral Resources Engineering

In partial fulfillment of the requirements for the Degree of

MASTER OF SCIENCE IN PETROLEUM ENGINEERING

Faculty supervisor: Prof. Pasadakis Nikolaos

External supervisor: Alexis Koulidis

February 2019

i


TECHNICAL UNIVERSITY OF CRETE

DEPARTMENT OF MINERAL RESOURCES ENGINEERING

The undersigned hereby certify that they have read and recommended to the Faculty of

Mineral Resources Engineering for acceptance a thesis entitled “TORQUE AND DRAG

ANALYSIS" by

Mustafa Shamss Alah Azeez in partial fulfillment of the requirements for the degree of

Master of Science.

Date: 05-02-2019

Committee Members,

Prof. Pasadakis Nikolaos (Supervisor)

Prof. Gaganis Vasileios

Dr. Marinakis Dimitrios

ii


ABSTRACT

Drilling through the subsurface is a complex operation and problems are almost

guaranteed to occur. Therefore, understanding and anticipating drilling problems,

understanding their causes and planning solutions are necessary for successfully reaching

the target. The most prevalent drilling problems include pipe sticking, lost circulation,

hole deviation, pipe failures, borehole instability, mud contamination, formation damage,

hole cleaning.

Torque and drag modeling is very important to analyze the mechanical behavior of the

drill string and the wellbore condition, hence, to predict and prevent downhole problems.

There have been a number of different approaches to the way that torque and drag has

been modeled in the well drilling industry. These include the soft string and stiff string

approaches.

This thesis will study the torque and drag in the wellbore and will give a general

overview of the sources, effects and challenges of torque, drag and buckling in the

wellbore. Furthermore, it will study and simulate the soft string model to calculate torque

and drag along a drill string in a 12 1/4” vertical section wellbore as well as provide

calculations of hook-loads and frictional torque for specific bit depths. Additionally, it

will provide a simulation of the section with the PayZone drilling simulator to calculate

the torque on bit while drilling. Both the model and the PayZone values are summed up

together to get the cumulative torque which is the torque observed at the surface while

drilling.

iii


TABLE OF CONTENTS

ABSTRACT ...................................................................................................................... iii

Table of Contents ............................................................................................................. iv

List of figures ................................................................................................................... vii

List of tables.................................................................................................................... viii

1 INTRODUCTION ...................................................................................................... 1

1.1 Introduction to Drilling ........................................................................................ 1

1.2 Historical Perspective ........................................................................................... 3

1.3 Deviation and Directional Wells .......................................................................... 3

1.4 Drilling Problems ................................................................................................. 4

2 LITERATURE STUDIES ......................................................................................... 5

2.1 Torque and Drag Definition ................................................................................. 5

2.1.1 Drag .................................................................................................................. 5

2.1.2 Torque ............................................................................................................... 6

2.2 Sources ................................................................................................................. 6

2.3 Types of Torque ................................................................................................... 9

2.3.1 Frictional Torque .............................................................................................. 9

2.3.2 Mechanical Torque ......................................................................................... 10

2.3.3 Bit Torque ....................................................................................................... 10

2.4 Challenges .......................................................................................................... 10

2.5 Reduction of Torque and Drag ........................................................................... 11

2.5.1 Wellpath.......................................................................................................... 11

2.5.2 Rotary Steerable Systems ............................................................................... 11

2.5.3 Bit Selection ................................................................................................... 12

2.5.4 Mechanical Friction Reduction Subs .............................................................. 12

2.5.5 Mud System .................................................................................................... 12

iv


3 TORQUE AND DRAG MODELING .................................................................... 13

3.1 Background ........................................................................................................ 13

3.2 Uses of Torque and Drag Modeling ................................................................... 14

3.3 Soft-String Versus Stiff-String Model ............................................................... 15

3.4 The Soft-String Model ....................................................................................... 16

3.4.1 For Inclined Straight Hole Section ................................................................. 17

3.4.2 For Curved Hole Section ................................................................................ 18

3.5 Side Forces ......................................................................................................... 20

3.6 Buoyancy Factor ................................................................................................ 21

3.7 Friction ............................................................................................................... 22

3.8 Buckling ............................................................................................................. 24

3.8.1 Buckling in a Deviation Wellbore .................................................................. 25

3.8.2 Buckling in a Vertical Well ............................................................................ 26

4 TORQUE AND DRAG MODELING .................................................................... 27

4.1 Input Data ........................................................................................................... 27

4.1.1 Drill String Data ............................................................................................. 28

4.1.2 Hole Sections Information .............................................................................. 29

4.1.3 Caliper log data ............................................................................................... 29

4.1.4 Survey Data .................................................................................................... 30

4.2 Model Construction ............................................................................................ 31

4.2.1 Calculation of Buoyed Weight ....................................................................... 31

4.2.2 Calculation of Axial Loads ............................................................................. 32

4.2.3 Calculation of Torsional Loads ...................................................................... 35

4.2.4 Calculation of buckling loads ......................................................................... 36

5 CALCULATION OF TORQUE ON BIT USING PAYZONE SIMULATOR .. 37

5.1 PayZone Drilling Predictive Simulator .............................................................. 37

5.2 ROP Modeling and Prediction ........................................................................... 38

5.3 Constructing the Lithology................................................................................. 40

5.4 Drilling the 12 ¼” section .................................................................................. 43

5.5 Tuning ................................................................................................................ 45

5.6 Torque values from PayZone ............................................................................. 45

v


6 RESULTS AND DISCUSSIONS ............................................................................ 47

6.1 The Tension Along the Drill String.................................................................... 47

6.2 The Frictional Torque Along the Drill String .................................................... 50

6.3 The Hook-load While Tripping .......................................................................... 52

6.4 The Frictional Torque While Tripping ............................................................... 54

6.5 Hook-load Comparison ...................................................................................... 56

6.6 Cumulative Torque Comparison ........................................................................ 58

7 CONCLUSIONS AND RECOMMENDATIONS ................................................. 62

REFERENCES ................................................................................................................ 64

vi


LIST OF FIGURES

Figure 1.1 Different types of wells \[1\]................................................................................ 3

Figure 2.1 Hook load as observed on the surface ............................................................... 5

Figure 2.2 Torque to rotate the pipe.................................................................................... 6

Figure 2.3 Key seating ........................................................................................................ 7

Figure 2.4 Differential sticking mechanism........................................................................ 8

Figure 2.5 Settled cuttings due to poor cleaning................................................................. 8

Figure 3.1 Forces acting on an object resting on a horizontal plane ................................. 16

Figure 3.2 Forces acting on an object resting on an inclined straight plane ..................... 17

Figure 3.3 Forces acting on a drill string element, illustrating the normal force, friction

and changes in inclination and azimuth \[4\] ...................................................................... 18

Figure 3.4 Side forces on a drill pipe ................................................................................ 21

Figure 3.5 Forces on an object sliding on an inclined plane ............................................. 23

Figure 3.6 Static and dynamic friction .............................................................................. 24

Figure 3.7 Sinusoidal buckling of the pipe in a horizontal wellbore \[11\] ........................ 25

Figure 3.8 Helical buckling of the pipe in a horizontal wellbore \[11\] .............................. 25

Figure 4.1 Hole diameter from the caliper log .................................................................. 29

Figure 4.2 Inclination and DLS versus measured depth ................................................... 30

Figure 4.3 Azimuth versus measured depth ...................................................................... 31

Figure 5.1 Payzone simulator ........................................................................................... 38

Figure 5.2 LAS file parameters - PayZone Parameters mapping ..................................... 41

Figure 5.3 LAS file parameters ......................................................................................... 42

Figure 5.4 Lithology data – After importing LAS file into PayZone ............................... 42

Figure 5.5 Actual section lithology ................................................................................... 43

Figure 5.6 Drilling control panel 1 ................................................................................... 44

Figure 5.7 Drilling control panel 2 ................................................................................... 44

Figure 5.8 Torque values from PayZone .......................................................................... 46

Figure 6.1 Tension loads along the drill string ................................................................. 49

Figure 6.2 Frictional torque along the drill string ............................................................. 51

Figure 6.3 Hook-loads while tripping ............................................................................... 53

Figure 6.4 Frictional torque while tripping ....................................................................... 55

Figure 6.5 Errors between the calculated and the actual Hook-load ................................ 56

Figure 6.6 Hook-load comparison .................................................................................... 57

Figure 6.7 Actual torque and calculated torque ................................................................ 59

Figure 6.8 Torque and UCS .............................................................................................. 60

Figure 6.9 The effect of wellbore diameter on the results ................................................ 61

vii


LIST OF TABLES

Table 4.1 12 ¼” Bottom hole assembly (BHA) ................................................................ 28

Table 4.2 Pipes characteristics .......................................................................................... 28

Table 4.3 Hole sections details ......................................................................................... 29

viii


1 INTRODUCTION

1.1 Introduction to Drilling

When locating and extracting hydrocarbons from reservoirs, a hole must be drilled

into the earth. This hole is known as an oil or gas well, depending on the type of

hydrocarbons produced in the reservoir. Well drilling is achieved by complex

processes and techniques; it is typically done by using special platforms known as

Drilling Rigs. In drilling rigs, there is a rotating drilling string with a bit attached to it,

and the bit is rotated and simultaneously forced against the rock formations in order

to overcome the resistance of the rocks and break or crush the rocks into small

particles. It is then brought back to the surface by a drilling fluid - usually by a liquid,

a gas, or foam – that is pumped from the surface through the drill string, down to the

bit and then back to the surface through the annulus between the hole and the drilling

string. Besides removing cuttings particles from the hole, drilling mud is used to

maintain the stability of the walls of the well and prevent formation fluid influx into

the well while drilling and during suspensions. The drilling rigs are complexes of

mobile equipment which can be relocated to different drilling sites.

Traditionally, the rotation of the drilling string is introduced at the surface by a rotary

table. In modern rigs, the rotation is generated by a top drive motor and then

transmitted to the bit by the drill string, which in this case are circular pipes

connected to each other, as well as some special tools and pipes to add weight, allow

for reaming and center the string in the hole. In addition, they orient the well into a

specific direction, downhole measurements, and add rotation such as the mud motor

located above the bit; all together these components are called Bottom Hole

Assembly (BHA).

Drill bits are the most refined tools in the rotary system; bits are available for every

condition of drilling, and certain types of bits are used for specific formation

hardness. Two types of bits are widely used in the rotary system – the first type is

Polycrystalline Diamond Compact (PDC) bits, which are made of heat-treated alloy

1


steel or a tungsten carbide matrix body with fixed cutters attached to the bit face,

which would be in contact with formation rocks. These cutters are made by bonding a

layer of synthetic polycrystalline diamond to a cemented tungsten carbide substrate in

a high temperature and pressure process. The hard and wear-resistant diamond is

produced at the end of this process, which penetrates rocks in a shearing mechanism.

The other type is roller cone bit; it is made of a body with three rotating cones with

casted or inserted teeth to break the rocks.

After the hole is drilled to a predetermined depth, sections of steel tubing slightly

smaller than the borehole, known as casing strings, are set in the hole to provide an

annulus for cementing. The casing provides structural integrity to the newly drilled

wellbore and isolates any potentially dangerous high pressure zones from each other

and from the surface.

With these zones safely isolated and the formation protected by the casing, the well

can then be drilled deeper, often into potentially more unstable formations. Here, a

smaller bit and smaller size casing is used. Modern wells often have two to five sets

of subsequently smaller hole sizes drilled, each inside one another and each cemented

with a differently sized casing.

During drilling operations, sub-surface pressures must be continuously controlled as

the various layers of the downhole formation are pierced by the wellbore. “Down hole

blowouts” can often occur when a zone of high pressure is penetrated and

uncontrolled pressure starts flowing to another zone of lower pressure. To control this

situation, mud pressure is increased above the pressure in the formation. This form of

wel l control is called “primary well control”, and pressure is maintained and closely

monitored throughout the entire well drilling process. In the secondary well control

approach, a blowout preventer is activated which seals off the well annulus to prevent

the downhole pressure from reaching the surface.

2


1.2 Historical Perspective

During the 1860s, the oil industry started to develop and wells were drilled using

cable tool rigs that originated in China. This was the best method available until 1900,

as cable tool rigs were very slow and were operated by lifting and dropping a special

string into the hole.

The rotary system was developed in 1901 to drill deeper and faster and eventually

became the common method to drive the rigs until the present day. (Please, do not use

a comma before the “and” word)

1.3 Deviation and Directional Wells

Most of the wells drilled today are directional wells to increase exposure to producing

zones and intersect a larger number of fractures. Directional wells deviate from the

vertical position of the wellbore path. Deviations can occur naturally from the result

of inserting the drill string to the downhole structure, such as fractures and formation

dipping. However, wells are often deliberately deviated by the use of a steering

mechanism attached to the drill string.

Multiple directional wells can be drilled from the same pad, which is common in

offshore drilling. The most common method is when a driller moves the rig a few

yards and starts another vertical shaft. Multiple wells can also be drilled from the

same vertical borehole to reach different zones.

Figure 1.1 Different types of wells \[1\]

3


1.4 Drilling Problems

Drilling through the subsurface is a complex and risky operation and problems are

almost guaranteed to occur. Therefore, it is always important to predict potential

problems rather than caution and containment, which is a key issue while designing

the well.

The most prevalent drilling problems include pipe sticking, lost circulation, hole

deviation, pipe failures, borehole instability, mud contamination, formation damage,

hole cleaning, H2S -bearing formation, shallow gas, and equipment and personnel-

related problems \[2\].

This thesis will study the torque and drag in the wellbore. Torque and drag modeling

is a very important tool used to avoid drilling problems and allows for further drilling,

especially in complex and extended reach wells, where the loads are usually near the

limits of the available tools and materials.

4


2 LITERATURE STUDIES

2.1 Torque and Drag Definition

2.1.1 Drag

Drag is defined as the increase in the drill string weight when pulling out of the hole,

or the reduction of the weight while running in the hole. In other words, drag is the

force difference between the static weight and the force required to move the string

up or down in the hole. Thus, the observed weight of the drill string on the surface is

either heavier or lighter than the actual weight, depending on the direction of the drill

string motion. The observed weight of the string is lower than the actual weight while

running in the hole and the direction of the drag force is upwards. While pulling the

string out of the hole, the observed weight of the string is higher than the actual

weight and the direction of the drag force is downwards.

Hence, drag on the drill string is the difference between the apparent weight and the

actual weight. Drag is negative when the string moves downwards; therefore, there

will be reduction in the string weight. Drag is positive when the string moves

upwards, which means the apparent weight is higher than the actual weight.

Drag force = Apparent weight – Actual weight

Rotating weight

(No axial movement)

Hook load up

(POOH)

Hook load down

(RIH)

Martin Decker

Weight indicator

Figure 2.1 Hook load as observed on the surface

5


2.1.2 Torque

Torque, also called moment of a force in physics, is the tendency of a force to rotate

the body to which it is applied. The torque, specified with regards to the axis of

rotation, is equal to the magnitude of the component of the force vector lying in the

plane perpendicular to the axis, multiplied by the shortest distance between the axis

and the direction of the force component. Regardless of its orientation in space, the

force vector can always be located in a plane parallel to the axis \[3\].

When it comes to torque in a drilling context, it is the moment required to rotate the

drill string that will overcome the rotational friction between the drill string and the

well bore, as well as the torque on the bit. The torque observed on the surface is

usually higher than the torque caused by the drill bit; this is mainly because of the

rotational friction torque in the well. The torque loss is greater in deviated wells,

especially in complex or extended reach and horizontal wells, where torque is a major

problem due to the rig and drill string torque limitation. However, the torque loss

would be zero in a perfectly vertical well, except for the small viscous torque

generated by the mud.

T

+

r

F

Figure 2.2 Torque to rotate the pipe

2.2 Sources

There are many parameters that cause torque and drag along the drill string. The

main parameters are calculated, whereas some of the parameters cannot be calculated.

6


They are summed together and included in the friction factor. The main causes for

excessive torque and drag are hole instability, key seating, differential sticking, poor

hole cleaning, and wellbore friction \[4\].

Hole Instability: Hole instability such as swelling shale, tight hole, and sloughing

shale increases the torque and drag because they change the original shape and size of

the hole which increases friction between the wellbore and the drill string. Interaction

between the drilling mud and the formation affects the friction and results in erosion

in the well. Loss of circulation has an impact on the friction as it gives rise to friction

in the wellbore due to lack of lubrication.

Key Seating: Key seating is the condition where a tube of small diameter is worn

into the side of a borehole with a larger diameter (Figure 2.3). It is generally a result

of severe hole direction changes, such as a high dogleg or a hard formation ledge left

in soft formations which erode and enlarge with time. In both cases, the diameter of

the drilled hole is expected to be close to the diameter of the drill pipe. The larger

diameter tools such as stabilizers, drill collars, and tool joints are not able to pass

through the key seat and become stuck, which will result in problems associated with

high torque and drag. The preventive method is to enlarge the point of the key seat so

that the tools with larger diameters can pass through it \[5\].

Figure 2.3 Key seating

7


Differential Sticking: Differential sticking occurs when high wellbore pressure

causes a high contact force of the drill string against the wall of low formation

pressure in typically high permeable zones. Differential pressure appears when the

hydrostatic pressure of a drilling fluid acting on the outside wall of the drill pipe is

greater than the formation fluid pressure and results in a sticking force. The drill

string will be difficult to rotate or move axially, which increases torque and drag.

Figure 2.4 Differential sticking mechanism

Poor Hole Cleaning: Hole cleaning is one of the main issues while drilling. Improper

cleaning can cause improper cuttings transport; there is subsequently an accumulation

of cuttings in the wellbore and high angle section of cutting beds are formed. These

conditions increase the friction inside the wellbore and cause high torque and drag.

An increase in Equivalent Circulating Density (ECD) can indicate improper hole

cleaning.

Figure 2.5 Settled cuttings due to poor cleaning

8


Wellbore Friction: Friction occurs because of the interaction between the drill string

and the wellbore as frictional forces are generated against the direction of motion.

The friction factor is defined as the measure of the degree of resistance to motion of

two adjacent elements sliding against each other. It is the ratio of the frictional force

to the normal contact force and is affected by the drilling fluid and formation type.

Friction factors can be estimated for open hole and cased hole settings according to

previous drilling experiences in corresponding formations and mud types for

modeling. Minimizing the normal force will be effective on proper weight transfer to

the bit. Methods for reducing normal force carefully design a well path and use string

components of lower weight \[6\].

2.3 Types of Torque

There are three types of torque observed downhole: frictional torque, mechanical

torque, and bit torque \[7\].

2.3.1 Frictional Torque

Contact loads between the drill string and casing or open hole section of a well

generate frictional torque. It is the only torque type generated while rotating off-

bottom in a perfectly cleaned wellbore. The following parameters determine the

magnitude of frictional torque :

Tension/Compression in the Drill String: Increasing tension in the drill string

increases contact forces; hence, it increases frictional torque. Both tension and

frictional torque are affected by the weight on bit.

String Weight: As the string weight is increased, more weight is pushed at the side

of the hole, resulting in higher contact forces that yield more frictional torque.

Dogleg Severity: A dogleg is the dramatic change of wellbore direction in three-

dimensional space, which increases the contact forces. This is generally a concern at

shallower depths where the tension in the string is high. As the tension in the drill

string gets lower as depth in the hole increases, the effects of dogleg severity become

negligible.

9


Inclination: Higher inclination values yield larger components of drill string weight

perpendicular to the borehole, increasing thus normal forces. Conversely, torque can

decrease at very high inclinations, as more of the string weight is taken by the

borehole wall; hence, decreasing the contact forces.

Hole and Pipe Size: The space between the drill string and hole is called the annulus.

A smaller annulus increases the effective stiffness of the pipe and increases contact

forces.

Lubricity & Friction Factor: Lubricity is controlled by the drilling fluid and

formation type, but it also controls friction. During drilling in abrasive formations,

significant torque changes can be seen.

2.3.2 Mechanical Torque

Mechanical torque is caused by cutting accumulations in the wellbore due to poor

cleaning because of poor hydraulics; therefore, there is an increase in friction inside

the wellbore. In addition, unstable formations such as sloughing and swelling

formations, which are affected by the drilling fluid, generates mechanical torque.

Differential sticking of the drill pipe generates mechanical torque when it is difficult

to rotate the pipe.

2.3.3 Bit Torque

Bit torque is generated from the interaction between the drill bit and the formation.

The factors affecting bit torque are WOB, RPM, formation characteristics, PDC bit

design variations, bit wear, and hydraulics \[8\].

2.4 Challenges

Weight Transfer to Bit: Weight transfer to the bit is achieved by slacking off at the

surface or pushing down. Drag force is the difference between the actual weight

available at the bit and the amount slacked off at the surface that is opposite to the

pipe movement. Controlling the weight on the bit becomes difficult as depth or

horizontal displacement increases because of the elasticity of the pipes. The elasticity

will cause part of the pipes to move while other parts are stationary, or it will cause

10


movement at different velocities. Weight is occasionally suddenly released because of

the difference between kinematic and static friction that occurs between the drill

string and casing or open hole. Hang-ups such as key seats, ledges, and uneven

cutting beds also contribute to the sudden release of the bit.

The bit rotation will suddenly stop if a weight transfer is released from the drill string

that exceeds the maximum weight that the motor can withstand. Such a condition is

called a motor stall and it is destructive for the rubber component of the motor.

The longitudinal drag of the drill string increases with increasing horizontal departure

of a well. Hence, weight transfer to the bit without the stalling motor becomes more

difficult, and drilling becomes more challenging.

2.5 Reduction of Torque and Drag

There is a variety of methods available to reduce torque and drag, if a well is drilled

and the torque is much higher than predicted and exceeds the top-drive capacity of the

rig. The application of such methods can be essential for ensuring that the TD can be

reached before reaching the torque limit of the rig or drill string.

2.5.1 Wellpath

Tortuosity reduction significantly reduces the torque and drag while drilling. The use

of RSS is recommended to make the smoothest wellbore. Finding compromises with

geologists may be very beneficial, as even small adjustments to the target may reduce

the torque. Reducing the DLS in build-up, drop off and bends can significantly reduce

torque and drag, especially at the top of the well where tension forces are greatest.

2.5.2 Rotary Steerable Systems

A hole drilled using a mud motor with a bent sub generally has greater tortuosity than

with a RSS, due to the steering principle of such tools. Directional drillers obtain the

desired DLS by switching from rotary drilling to sliding drilling as many times as

needed. Rotary drilling with a motor creates a smaller hole than with sliding drilling.

Drilling with a motor creates a larger hole than a RSS would, whereas with sliding

drilling, a high DLS is utilized to correct for the direction achieved by rotary drilling,

11


due to a combination of gravity and centralizer placement. This continued alteration

is the reason why motors create much more tortuosity than a RSS. Adding a mud

motor to an RSS will increase ROP, while RPM at the surface can be reduced to a

minimum and thus reduce the torque. Using RSS with an integrated mud motor will

reduce surface torque as compared to a conventional RSS.

2.5.3 Bit Selection

Bit selection is normally based on ROP, steer ability, and durability, but another

factor is important as well. The gauge length can significantly affect the propagation

of a cyclic hole. A short gauge bit is more aggressive and creates more caliper

variations and what is called micro tortuosity, whereas a long gauge bit tends to

create fewer caliper variations and a smoother hole. The micro tortuosity is not seen

by MWD directional sensors, and will add extra torque and drag. This can be seen as

measured torque and drag trends deviate from simulated trends.

2.5.4 Mechanical Friction Reduction Subs

Mechanical friction reducing subs have been tried and proven successful in reducing

friction. Use of mechanical friction reduction tools and other techniques for reducing

friction have shown to be effective. Various types exist, but either they consist of

mechanical rollers, or a sleeve on bearings, which then becomes the effective contact

surface. The low friction in a smooth bearing relative to rough steel against rough

steel reduces the torque and drag significantly. The subs are typically placed one per

stand in the sections of the well that sees the highest side force.

2.5.5 Mud System

The easiest way to reduce torque and drag is to use oil-based mud (OBM) or synthetic

based mud (SBM) instead of water based mud (WBM). It is also possible to add

lubricants, even to WBM.

12


3 TORQUE AND DRAG MODELING

3.1 Background

Software for torque and drag models has been developed and used in the industry and

is crucial in avoiding drilling problems and allowing for further drilling, especially in

complex and extended reach wells, where the loads are usually near the limits of the

available tools and materials.

During the well planning, torque and drag models are used to validate the planned

well path that can be drilled within the equipment’s limits and rig capacity. T hese

models are then used for load analysis to optimize the well path design, to minimize

torque and drag and to ensure that the torque is within safe working limits for the drill

string and rig equipment.

The planned well path is designed for ideal smooth curves to counter the real well

path which has tortuosity, so that planned paths cause the model to predict torques

and drags lower than the actual torques and drags.

Torque and drag models are also used in real time to detect potential drilling

problems at an early stage before these problems cause serious damage. This is done

by comparing hook-load measurements in real time to the calculated values.

Deviations from the values in the models indicate a problem down-hole. The problem

might be due to key seating, differential sticking and cuttings bed accumulation.

Other factors such as ECD, standpipe pressure, and pit volume must be checked to

evaluate the nature of the problem. In order to obtain the best results, real time

surveys should update the model in order to include deviations from planned well

trajectory and directional drilling errors. Torque and drag models are the best tool

available for monitoring hole conditions.

13


In real time it is also possible to back-calculate the friction factor from the measured

hook-load by iterating until a match between the measured value and the model

(Lesage 1988) is found.

A plot of calculated friction factors versus depth is then used to identify downhole

problems. This can also be calculated during drilling if the downhole weight on the

bit and the downhole torque on bit is present. Torque and drag models are steady state

models, which means that the calculations are only made for string movement in a

steady manner and sudden transient effects are not incorporated into the calculations.

In post drilling, a detailed analysis can be helpful in revealing the true cause of

problems that were previously unexplainable. The post drilling analysis allows for

changes to operational procedures to be made, so that problems can be avoided when

drilling the next well.

The measured data can be used to yield a better understanding and allow for a better

planning of the next well. Post analysis may also lead to a more accurate friction

factor, by including local information such as formation lithology, permeability, and

mud properties. The gained information can be used to evaluate improved well

trajectories and kick-off point depths, as well as correcting casing setting depths, in

order to avoid encountering hole problems in the evaluated wells.

3.2 Uses of Torque and Drag Modeling

• Trajectory design to minimize torque and drag forces

• Determining hole condition to determine if problems are arising

• Drill string design to reduce torque and drag

• Monitoring hole cleaning in real time

• Monitoring friction when running casing

• Determine the onset of drill pipe buckling

• Determine the possibility of reciprocating casing during cementing

14


• Providing lateral load inputs for casing wear models

• An aid in determining if a changes to the mud is necessary

• Calculating WOB in highly inclined wells with high frictional drag

• Determining if drill string torque limits may be exceeded

• Aid in making strategic decisions on mud systems

3.3 Soft-String Versus Stiff-String Model

The soft string and the stiff string models are two different mathematical models

which are used for torque and drag analysis. They were developed to describe the

mechanical behavior of the drill string inside the borehole and they have their own

theoretical background and assumptions. The soft string model is widely used in the

industry and it assumes that the drill string has a continuous surface contact area with

the wellbore as it deforms to the shape of the wellbore.

The model ignores the bending stiffness in the drill string and borehole clearance. For

a smooth well geometry, the model has a good approximation of forces and contact

loads.

In some cases, due to the friction force generated by the rotation, the string climbs on

the wellbore wall and will cause the contact force to be less than if the pipe lies on the

low side of the wellbore, which is the main soft string model assumption. Therefore,

the soft string model cannot predict such diverse positing which in some cases will

lead to errors in torque and drag prediction due to the drill string position on the side,

high, right, or left side of the wellbore depending on the section and operation.

The stiff sting model takes into account the drill string stiffness in the wellbore and

the annulus clearance. The model calculates all the contact points between the drill

string and the wellbore and the drill string reacts naturally to the forces and moments.

Therefore, the model predicts more realistically the side forces along the drill string,

which helps to determine torque and drag losses and better match with the actual

15


measurements. But the stiff string model is not recommended for real time torque and

drag monitoring because of the long time required for its application \[9\] \[10\].

Both soft and stiff string models show similar results over the smooth wellbore

geometry but they give different predictions in a tortuous wellbore.

3.4 The Soft-String Model

Considering an object of weight W is resting on a horizontal plane:

Figure 3.1 Forces acting on an object resting on a horizontal plane

In order to slide the object a force Ft must be exerted to overcome the force of friction

Ff between the object and the plane surface.

The magnitude of the frictional force is:

Ff   

Where:

Ff = frictional force (lb)

µ = dimensionless coefficient of friction, a constant that depends on the roughness of

the object and plane surface, determined experimentally

W = normal force acting perpendicular to the surface (lb)

16


Therefore, the force Ft (Drag Force) required to slide the object should be slightly

greater than Ff (friction Force).

3.4.1 For Inclined Straight Hole Section

Considering a straight section of drill pipe in a wellbore inclined at an angle:

Figure 3.2 Forces acting on an object resting on an inclined straight plane

The buoyed weight of the drill pipe W is acting vertically downward and can be

resolved into two forces:

Fn – normal force acting perpendicular to the hole:

Fn   sin 

Fx – the weight component acting parallel to the hole axis:

Fx   cos 

17


The frictional or drag force Ff is the normal force multiplied by the coefficient of

friction:

Ff  Fn     sin 

The force Ft required to move the drill pipe is determined by making a force balance

Ft  Fx  Ff

Ft   cos     sin 

The frictional force or drag always acts in the opposite direction of the pulling force

Ft. Therefore, the sign is negative (-) if the drill pipe is lowered into the hole, and

positive (+) when the drill pipe is pulled out of the hole.

3.4.2 For Curved Hole Section

In a curved section of the wellbore where inclination and azimuth change across the

section, the calculation of the drag force is more difficult.

Figure 3.3 Forces acting on a drill string element, illustrating the normal force,

friction and changes in inclination and azimuth \[4\]

18


In 1984, C.A. Johancsik presented the pioneer friction analysis model. In his model

both torque and drag were assumed to be caused entirely by sliding friction between

drillstring and borehole wall. Other sources of torque and drag like friction due to

fluid and cuttings, static friction, and piston forces were not considered \[4\].

The sliding friction coefficient is the ratio of the friction force to the normal contact

force.

The normal force is given by:

Fn    Ftasin)  (Ft  sin)

Where:

Fn = The normal force at the lower end of the string element (Ib)

Ft = The tensile force at the lower end of the string element (Ib)

a  The change in azimuth angle over the string element (radians)

  The inclination at the lower end of the string element (radians)

  The change in inclination angle over the string element ( radians)

W = The buoyed weight of the string element (lb)

The normal force is then used to derive the equation for tension increments:

Ft  cos  Fn

19


here  is the friction coefficient, the positive sign () is used when hoisting, and the

negative sign (-) is used when lowering the drill string. In addition, the torsion

increment is calculated as:

M   Fn r

Where:

M = The increment in torque across the string element (ft.Ib)

r = The radius of the string element (ft)

The model assumes that the drill string is consisted of short elements joined by

connections that transmit torsion, tension, and compression, but not the bending

moment.

The basic equations of friction are applied to each segment with calculations starting

from the bottom of the drill string and continuing upward to the surface. Each short

interval of drill string contributes increments of torque, drag, and weight. Forces and

torque values are added to produce the cumulative loads on the string. Initial

conditions are specified at the bit and the inputs are the weight on the bit and bit

torque values for drilling operations.

3.5 Side Forces

The weight of the drill string acting on the wellbore is a major contributor to side

forces and to the magnitude of the normal force against the wellbore. As such, heavier

drill strings induce greater side forces against wellbores. Therefore, it is important to

minimize the weight of the drill string within safe limits.

20


Figure 3.4 Side forces on a drill pipe

Side forces created by tension typically only occur with doglegs. In build sections, the

direction of pipe movement affects the direction of side forces. When moving down,

the drill string will be lying on the low side – therefore, the effect of tensile load is

reduced and the resultant side force is in the direction of the weight component.

When moving up or tripping out, the drill string will be in contact with the high side.

Therefore the effect of tensile load is increased and the resultant side force will be in

the direction of the tensile component. In drop sections, regardless of whether the

drill string is tripping out or running in the hole, the drill string will be lying on the

low side of the wellbore. Therefore, the resultant force will always act on the low

side.

3.6 Buoyancy Factor

Buoyancy is an upward force exerted by the drilling fluid against the weight of the

drill string. In the well filled with drilling fluid, the weight of the drill string is the

weight in the air minus the mud weight that the steel in the string displaces. This

phenomenon is known as Archimedes’ principle. The buoyancy factor can be more

conveniently defined as:

    

  1

21


If there are different densities of fluids inside and outside the pipe – for example,

during tripping in, during displacement of mud to new mud, and while cementing, the

buoyancy factor can be defined as:

           

  1

Where:

  Buoyancy factor

ρ (mud)  Dens ity of drilling mud

ρ (string)  Density of drill string (usually the density of steel)

ρo  Density of fluid outside the pipe

ρi  Density of fluid inside the pipe

Ao = Outer cross sectional area

Ai = Inner cross sectional area

A heavy mud will decrease the effective weight of the drill string and thus decrease

the side force and the load from friction and torque. However, a heavy mud has

heavier particles, which could lead to less lubricity and therefore higher friction.

3.7 Friction

Contact friction, such as when two relatively smooth solid bodies slide against each

other, will be independent of the speed at which the two bodies slide and independent

of the contact area. This applies only for soft string models under consideration but

the friction force will be proportional to the contact force of the sliding surfaces. A

friction coefficient  is the ratio of the friction force to the normal force. In order to

find the normal force in an inclined plane, consider the schematics shown in Figure

3.5.

22


 

 

Ft to

Ff

θ

Ft bottom

Fn = Wsin θ W

Figure 3.5 Forces on an object sliding on an inclined plane

Where:

 friction coefficient

Ff = Friction force

Fn = Normal force

Ft = Tensile force

W = weight of the segment

  Inclination angle

23


Figure 3.6 Static and dynamic friction

The friction factor is a key parameter in torque and drag modeling because it

characterizes the surface-to-surface interaction, which is the heart of the model. The

friction factor applicable to any situation is a function of many things, including fluid

type, composition, lubricity, formation type, casing and tool joint material, and

roughness. When significant portions of both cased and open hole exist, it may be

necessary to use more than one friction factor, usually two - one for open-hole, and

one for cased hole. Generally the friction factors selected are 0.2 and 0.3 for cased

and open-hole respectively. But in real time operations these friction factors are

calibrated regularly during the operations.

3.8 Buckling

Buckling is a very important issue in torque and drag calculations and it occurs when

the drill string is in compression. Buckling increases the contact surface area between

the drill string and the wellbore, which increases side forces. Sinusoidal buckling

occurs first; it begins when axial compression increases in the drill string and there is

a string snake phenomenon along the wellbore. As the axial compression continues to

increase, the buckling will change into a helix drill string, a phenomenon called

helical buckling.

24


Sinusoidal buckling can generally be tolerated while helical buckling should be

avoided, because helically buckled strings create additional drag, which could lead to

a “lock up” situation. This means that after the drill string is released from the

derrick, the entire drill string will be supported by wellbore friction instead of by the

bit force.

Figure 3.7 Sinusoidal buckling of the pipe in a horizontal wellbore \[11\]

Figure 3.8 Helical buckling of the pipe in a horizontal wellbore \[11\]

3.8.1 Buckling in a Deviation Wellbore

A long pipe in a wellbore will be buckled into a sinusoid along the lower side of the

hole at an axial compressive force of Wu and Juvkam- old’s model (1991):

  

Fs  2

25


The helical buckling is given by: √ 

Fh  (2 Fs

Where:

Fs = Sinusoidal buckling

Fh = Helical buckling

E  Young’s modulus of elasticity

W = Buoyed weight of the string element

I = Moment of inertial component

  ellbore inclination

r = Radial clearance between the wellbore and drill string (tool joint)

F = Compressive axial force

3.8.2 Buckling in a Vertical Well

In a vertical section, the tube is easily buckled, which adds some considerable axial

friction force. The critical load for sinusoidal buckling, presented by Wu and Juvkam-

Wold, (1993) \[12\] is:

Fs  2      ⅓

The helical buckling load is about 2.2 times as large as the sinusoidal buckling load in

the vertical wellbore as presented by Wu and Juvkam-Wold, (1993):

Fh  2  

26


4 TORQUE AND DRAG MODELING

4.1 Input Data

The torque and drag model is constructed for the 12 ¼” section, which starts from a

depth (1100m) which is the casing seat of the previous casing of 13 3/8” until depth

(2700m), which is the TD of the 12 ¼” section. The section is vertical, with minor

deviations according to the survey data.

Thus, the model will simulate the forces acting on the drill string from the surface

(depth equal to zero, as the top drive system is ignored in the calculations) through

the 13 3/8” cased hole until (1100m), then continuing through the 12 ¼” open hole

section until (2700m).

Mud weight of 10.5 ppg was used in the model, as in the actual drilling data. The

friction factor is assumed to be 0.25 for the cased hole section and 0.35 for the open

hole section based on calibrations from nearby wells. Taking into account that the

weakest point in the drill string that will have the highest load is the last string of the

drill pipe in the surface, the maximum allowable tension is 436 KIbs and the

maximum make-up torque that should not be reached is 30.7 ft.Ibs.

The drill string is divided into segments of “1 meter”, and calculations of tension

forces have been done for each segment starting from the bottom and summed up to

the top.

27


4.1.1 Drill String Data

Table 4.1 12 ¼” Bottom hole assembly (BHA)

The drill string is modeled for the Drill Pipe (DP), Heavy Weight Drill Pipe (HWDP)

and Drill Collars (DC), therefore, the BHA is assumed to be consists of DP, HWDP

and DC only.

Table 4.2 Pipes characteristics

Length Weight OD ID Tool Tensile Make up

(m) (Ibs/ft) (inch) (inch) Joint OD Strength Torque

(inch) (Klbs) (ft-KIbs)

Drill pipe 2368 19.5 5 4.276 6.625 436 30.7

HWDP 156 49.8 5 3 6.625 691 33.9

Drill collar 177 158.7 8.25 2.813 8.25 1856 52.1

28


4.1.2 Hole Sections Information

Table 4.3 Hole sections details

Length (m) OD ID Friction Mud density

(inch) (inch) factor (ppg)

Casing 1100 13 3/8" 12.62 0.25 10.5

Open hole 1600 N/A 12.25 0.35 10.5

4.1.3 Caliper log data

A caliper log is a well logging tool that provides a continuous measurement of the

size and shape of a borehole along its depth; it is used for the open hole inside

diameter in the calculations in order to give more accurate results. For the cased hole

section, the inside diameter is fixed \[13\].

Figure 4.1 Hole diameter from the caliper log

29


4.1.4 Survey Data

Survey data represents the well path and surveys are taken from MWD

measurements. An inclination of 0° would be true vertical, and an inclination of 90°

would be horizontal. Azimuth is the angle, measured in degrees, of the horizontal

component of the borehole or survey-instrument axis from a known north reference.

This reference is true north, magnetic north, or grid north, and is measured clockwise

by convention. It is important to highlight that all the angles should be converted to

radians in order to be used in the model \[14\].

Figure 4.2 Inclination and DLS versus measured depth

30


Figure 4.3 Azimuth versus measured depth

4.2 Model Construction

4.2.1 Calculation of Buoyed Weight

The buoyancy factor is calculated using a density of 65.5 ppg for steel and 10.5 ppg

for the drilling mud:

    

  1

31


Where:

  Buoyancy factor

ρ (mud)  Density of drilling mud

ρ (string)  Density of drill string (density of steel)

Then the buoyed weight of each element is calculated:

Buoyed weight  Actual weight x 

The nominal weight of the drill pipe used is 19.5 Ib/ft; for HWDP it is 49.3 Ib/ft; and

for the drill collar it is 147.22 Ib/ft. It is important to convert the one meter element to

feet in order to multiply it by the buoyed weight from the above equation to obtain the

buoyed weight for each element.

4.2.2 Calculation of Axial Loads

First, the tension at the bottom of each element is calculated:

Ft   cos

Where:

Ft = The tensile force at the lower end of the string element (Ib)

W = Buoyed weight of the string element (Ib)

  Inclination at the lower end of string element (radians)

32


The tension force of each element, summed up to the elements above it, starting from

the bottom, is used in normal force calculations. In other words, the tension force at

the lower end of an element will be the sum of tension forces of all elements below it.

This tensional incensement is called the free rotation weight or off bottom weight of

the drill string.

Next, the normal force for each element is calculated:

Fn    Ftasin)  (Ft  sin)

Where:

Fn = The normal force at the lower end of the string element (Ib)

Ft = The tensile force at the lower end of the string element (Ib)

a = The change in azimuth angle over the string element (radians)

  The inclination at the lower end of the string element (radians)

  The change in inclination angle over the string element (radians)

W = The buoyed weight of the string element (lb)

The frictional force is then calculated for each element:

Ff   Fn

Where:

Ff = frictional force (lb)

µ = coefficient of friction, assumed to be 0.25 for cased hole section and 0.35 for

open hole section

33


For upward movement of the drill string, the frictional force is acting downwards;

therefore, the frictional force must be added to the tensional force. This confirms that

the measured weight of the drill string on the surface while pulling out of the hole is

greater than the actual weight of the string.

The tensional force is calculated as:

Ft = Ft + Ff

The above tensional force for each element is separate. In order to calculate the

cumulative tensional loads along the drill string, tensions for every element must be

added to the element above. For example, the tensional load at the lower end of an

element is the total load of all elements below this element.

The same scenario is applied for the case of running in the hole, but with a negative

sign (-). As the drill string moves downward, the friction acts upward; therefore, the

frictional force is subtracted from the tensional load and the measured weight of the

drill string at the surface while running in the hole appears to be less than the actual

weight of the string.

Ft = Ft – Ff

34


4.2.3 Calculation of Torsional Loads

The frictional torque at each element is calculated by multiplying the frictional force

by the radius of the drill string; the tool joint radius is usually considered.

M = Ff r

Then the torsion increment is calculated by adding the torque of each element to the

element above starting from the bottom – this is called the off bottom torque.

To calculate the torque (on bottom), the torque on the bit must be added. Therefore,

the torsion increment is calculated starting from the torque on the bit.

Torque at the surface = Torque on the bit + M1 (last element in the bottom) + M2 + . .

. , + Mn (First element from the surface).

Furthermore, for (on bottom) torque calculation, the weight on the bit is subtracted

from the tension increment. To calculate the torque while running in the hole, the

tensional force of RIH is used, and the tensional force of POOH is used for pulling

out of hole torque.

35


4.2.4 Calculation of buckling loads

The sinusoidal and helical buckling is calculated as \[11\]:

  

Fs  2

Fh  (2 √  Fs

Where:

Fs = Sinusoidal buckling (Ib)

Fh = Helical buckling, (Ib)

E  Young’s modulus of elasticity (psi)

W = Buoyed weight of the string element (lb)

I = Moment of inertial component

  Inclination at the lower end of string element

r = Radial clearance between the wellbore and drill string (tool joint) (ft)

36


5 CALCULATION OF TORQUE ON BIT USING

PAYZONE SIMULATOR

5.1 PayZone Drilling Predictive Simulator

The PayZone Drilling Simulator is a PC based simulator that can be used for training

as well as planning and optimizing field operations. It is built around a drilling

mechanics model that predicts the rate of penetration and rate of wear of a drill bit as

a function of the bit, the rock being drilled and a set of operating parameters. The

software is able to carry out the following operations: Drilling, hydraulics

optimization, directional drilling, dealing with kicks and losses, handling hole

stability problems, logging, casing and cementing \[15\].

The heart of the program is a drilling mechanics algorithm that calculates the state of

wear of a drill bit and its resulting rate of penetration as a function of the type of drill

bit, the operating parameters and the nature of the rocks being penetrated.

37


Figure 5.1 Payzone simulator

PayZone functions are divided between nine different editors. Before drilling begins,

some information is assembled in order for the simulator to operate. The simulator is

built up of contributions from six primary editors (lithology, drill bits, BHAs, muds,

casings and settings).The output is then combined by the State Editor into a State file.

The State file is the data source from which the simulator runs its calculation \[15\].

5.2 ROP Modeling and Prediction

Researches has demonstrated that rate of penetration (ROP) depends on two group of

parameters: drilling rig and formation parameters. The drilling rig parameters

includes the following: weight on bit (WOB), bit rotational speed (RPM), hydraulic

parameters (mud flow rate, mud rheology and mud density), bit and bit condition. All

these parameters should be identified \[16\].

From the formation group the most essential parameters affecting penetration rate are:

local stresses, rock compaction, fluid pore pressure and mineralogical content which

is related strongly to lithology of subsurface formations \[16\].

38


PayZone simulator enables the prediction of ROP using a mathematical model; the

model is developed based on Teale’s concept of mechanical specific energy \[17\]. The

main features of the model predicting rate of penetration are given as \[16\]:

ROP = (flow\_factor)(c)(aggressivity)(RPM)(tooth\_length)(G)

\[(   )  (     )\]

G  1  exp

toothlength

Where:

ROP = Penetration rate

RPM = Rotary speed

tooth\_length = The average length of the bit teeth

UCS = Unconfined compressive strength of the rock

D = Bit diameter

WOB = Applied weight on bit

C = Constant

aggressivity = Formation and bit characteristic constant ranging between 20% and

100% and normally is given the value of 35%

curv = Formation-bit interaction constant and it is usually given the value of 1.5

flow\_factor = Constant, ranging between 50% and 100% and defines the capability of

the system to adequately clean the bit front by the cuttings

A similar rock-bit interaction model, with adjustable parameters, is the one that has

been presented by Teale \[17\]. In this model the concept of specific energy is

introduced. This concept predicts the energy required by the rig to drill a unit volume

39


of rock. This model has been used by many researchers and practitioners in the past

as shown below:

   

ROP      

Where:

Abit = Bit face area

µ = The coefficient of friction between drill string and formation, converting applied

WOB to torque

eff = The efficiency of transmitting the rock destruction power of the drilling rig to

the rock

It has been shown that predictions from both models are essentially the same and lead

to the same results \[18\]. Thus, the values of UCS can be used to estimate rock

drillability \[19\].

5.3 Constructing the Lithology

The Lithology Editor section in the software enables the user to build a sequence of

rock layers that can be drilled by the simulator. This sequence is known as a lithology

or litho. Each layer can be given its own properties (thickness, mineralogy, strength,

abrasivity, log properties… etc.) which will be used by th e simulator to generate the

drilling response.

User can build the lithology by importing the LAS file. LAS files contain columns of

data in standard text format. every LAS file begins with \~C (\~Curve Information),

that associates the title of each column of data with the corresponding measurement.

The LAS Converter identifies the title of the column and assigns the data in that

column to the appropriate position in the PayZone Litho. Titles currently identified

are converted as shown in the table.

40


Figure 5.2 LAS file parameters - PayZone Parameters mapping

As a pre-processing step, LAS data are analyzed before assigning them to the litho

section. And some titles have been changed to match with the software titles. One of

these changes is a missing rock unconfined compressive strength (UCS). This

parameter is calculated and then added to the LAS file before importing into

PayZone. UCS is estimated using the formula:

UCS = 72.5 x ((304.8/ DT\_C) 3 + RHO x (304.8/ DT\_C) 2)

Where:

UCS: Unconfined compressive strength (psi)

DT\_C: Sonic data in the form of slowness (microseconds/ft)

RHO: bulk density (g/cc)

41


Figure 5.3 LAS file parameters

Figure 5.4 Lithology data – After importing LAS file into PayZone

42


Figure 5.5 Actual section lithology

5.4 Drilling the 12 ¼” section

Drilling is simulated using the input parameters from actual drilling data:

WOB: Weight on bit, kIbs

RPM: Rotary speed, revolution per minute

GPM: Flow rate, gallon per minute

TFA: Nozzles total flow area, inche²

MUD WEIGHT: Pounds per gallon (ppg)

43


Figure 5.6 Drilling control panel 1

Before the drilling starts, BHA and drill bit are selected. By clicking on run in hole

and then start drilling, the simulator will make drilling through the lithology using the

provided input parameters to calculate:

Torque: Down-hole Torque (ft-lb)

SPP: Standpipe pressure (psi)

ROP: Rate of penetration (ft/hr)

ECD: Equivalent circulating density (ppg)

Bit HSI: Bit Hydraulic Horsepower

Pit Gain: mud pit gain (bbl)

HP: Mud Pump Horsepower

Figure 5.7 Drilling control panel 2

44


5.5 Tuning

In The first simulation run, the predicted ROP does not match the real ROP. This is

caused by uncertainty in bit characteristics and rock properties. Therefore, ROP factor

is selected as an uncertain variable and varied within an acceptable range. Until the

best match of predicted and real ROP is reached. After matching the ROP with up to

10% error, the predicted torque is used as a best estimated torque.

5.6 Torque values from PayZone

After simulating the drilling process and tuning for the best ROP matching. The

torque values are exported to be added to the frictional torque calculated from the

frictional model, then compared with the actual cumulative torque.

45


Figure 5.8 Torque values from PayZone

46


6 RESULTS AND DISCUSSIONS

The first part of this chapter deals with results of the constructed Torque and Drag

model analysis that applied on the drill string for the 12 ¼” section TD. The main

results are:

• The tension along the drill string.

• The frictional toque long the drill string.

• Hook-load while tripping.

• The frictional torque while tripping.

The second part deals with the hook-load comparison between actual data and the

hook-load calculated from the Torque and Drag model.

The third part deals with torque results from PayZone simulator, the frictional torque

from the Torque and Drag model. Then both results are compared to the actual

cumulative torque for the same section.

6.1 The Tension Along the Drill String

Using the Torque and Drag model, loads have been calculated for every meter of the

drill string. The drill string length is 2700 m, this is for the case of drill bit is at depth

of 2700m. The top part of the drill string (surface – 1100m) is located inside the 13

3/8” casing and the lower part (1100m – 2700m) is located in the 12 ¼” open hole

section.

The calculations have been done for four scenarios:

• The drill string tension/load/weight while the bit is off bottom i.e. free rotating

weight with no axial movement.

47


• The drill string weight while the bit is on bottom with applying weight of bit of 50

KIbs. It is obvious that the loads on the drill string are less in this case because

most of the stress is exerted upon the bit.

• The drill string weight while running in the hole. These weights are less than the

free rotating weight due to the frictional forces which acting against the string

motion, which means acting upwards, this approves the scenario when the hook-

load is less than the actual weight of the drill string when monitored from the

weight indicator at the surface while tripping in the hole which is discussed in the

literature.

• The drill string weight while pulling out of the hole, this is opposite to the

previous case, the weights are more than the actual due to the frictional forced

which acts against the drill string motion, which means acting downwards,

therefore, it adds loads to the string. The hook-load shows more than the actual on

the weight indicator at the surface.

Both, critical Sinusoidal and helical bucking limits are calculated for every meter

along the drill string. Buckling is described in negative sign. However, there is no

buckling of the drill string in the presented case.

It’s important to note that values of weights lie in the positive area of the graph shows

tension loads, while in the negative area shows a compression, which is

recommended not to be in the drill pipes to avoid buckling.

As we can see, the drill string falls into the safe window. The safe window being the

maximum allowable tension the can be exerted upon the drill string.

48


Figure 6.1 Tension loads along the drill string

49


6.2 The Frictional Torque Along the Drill String

Likewise, the tensional loads and frictional torque are calculated for every meter

along the drill string. The calculations for four scenarios are presented:

• The torque along the drill string while the bit is off bottom in other words, free

rotating weight with no axial movement.

• The torque along the drill string while the bit is on bottom. In this case 8 ft-KIbs

torque on bit is added to the bottom of the string. The bit torque affects overall

torque along the drill string, and therefore, higher torque is observed.

• The torque along the drill string while running in the hole, assuming no reaming,

in case of back reaming, more torque will be generated and exceeds the free

rotating torque.

• The torque along the drill string while pulling out of the hole, theoretically, the

frictional torque is higher in both cases of with or without back-reaming.

Because the frictional torque depends on the normal force, in this case, normal

force during upward movement of the drill string.

50


Figure 6.2 Frictional torque along the drill string

51


6.3 The Hook-load While Tripping

The hook-load values are calculated from the torque and drag model. These values

are the summation of all tensional loads along the drill string for every meter of bit

depth. Therefore, it simulates the hook-load reading at the surface for various depths

unlike the previous analysis where the calculations have been done for only one bit

depth of 2700m. The traveling block is ignored in the hook-load calculations. The

traveling block weight is added when comparing the simulated results with actual

hook-load data.

Three scenarios are implemented free rotating weight, hook-load values while

running in the hole and while pulling out of the hole.

52


Figure 6.3 Hook-loads while tripping

53


6.4 The Frictional Torque While Tripping

Likewise, the hook-load while tripping and the surface torque values are calculated.

These values are the summation of all frictional loads along the drill string for every

meter of bit depth unlike the previous analysis where the calculations have been done

for one case of bit depth of 2700m. Three scenarios were implemented, free rotating

torque, torque values while running in the hole and while pulling out of the hole.

54


Figure 6.4 Frictional torque while tripping

55


6.5 Hook-load Comparison

The hook-load values in static condition are calculated from the torque and drag

model. Those values are added to the traveling block weight and the weight on bit is

subtracted to give the final value of the hook-load, which is compared to the actual

hook-load values.

The calculated data shows good results, and the majority of errors are below 15%.

Hook-load = Static hook-load + Traveling block weight - Weight on bit

Figure 6.5 Errors between the calculated and the actual Hook-load

56


Figure 6.6 Hook-load comparison

57


6.6 Cumulative Torque Comparison

The torque on bit values from PayZone is added to the frictional torque from the

Torque and Drag model. The result of the two torque values is the cumulative torque

that is observed at the surface. The resultant torque is then compared to the actual

cumulative torque for the same section.

The comparison shows that the torque which is calculated from the model and

PayZone gives underestimated results. However, the torque values follow the trend of

the estimated unconfined rock strength as it is shown in figure 6.8

The model did not take into consideration the exact contact area and ignored the

effect of borehole diameter variations.

Looking at figure 6.9, the hole diameter is much bigger than the bit size in the upper

part of the section, this indicates a borehole instability i.e. shale swelling. Cavings

from failing formation of the upper part of the section makes hole cleaning more

difficult, thus, increase in torque and drag. Furthermore, a narrowing hole is also

observed which also increase torque and drag.

58


Figure 6.7 Actual torque and calculated torque

59


Cumulative Surface Torque UCS

Torque (ft-KIbs) UCS

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 0 5000 10000 15000

1100

1300

1500

1700

)

( m

D 1900

M

2100

2300

2500

2700

Actual Torque (ft-KIbs) (Payzone+model) Torque (ft-KIbs) UCS (Psi)

Figure 6.8 Torque and UCS

60


Cumulative Surface Torque Hook-load Comparison Wellbore ID

Torque (ft-KIbs) Hook-load (KIbs) Wellbore ID (Inch)

01234567891011121314151617 050100150200250300350 -15-10-5051015

1100 1100

1300 1300

1500 1500

1700 1700

) )

( m ( m

D 1900 D 1900

M M

2100 2100

2300 2300

2500 2500

2700 2700

Actual Torque (ft-KIbs)(Payzone+model) Torque(ft-KIbs) Actual Hook-load KIbsHook-load (model) KIbs

Figure 6.9 The effect of wellbore diameter on the results

61


7 CONCLUSIONS AND RECOMMENDATIONS

 The frictional torque values seem to be underestimated using the frictional model

due to some uncertainties and assumptions:

• The model assumed perfectly cleaned wellbore. Therefore, no cuttings

accumulation is considered.

• The model ignored the radial clearance between the string and the

borehole.

• The model is a steady state model, which means that the calculations have

been only made for string movement in a steady manner, and sudden

transient effects such as string vibrations were not incorporated into the

calculations.

• The model did not take into consideration the mud cake effect.

• The model did not take into consideration the exact contact area and

ignored the effect of borehole diameter variations and borehole instability

such as shale swelling and borehole closure.

• As mentioned above, from figure 6.9, a shallow swelling is observed in

the upper part of the section. The cavings from failing formation of the

upper part of the section makes hole cleaning more difficult, thus, increase

in torque and drag. Furthermore, a narrowing hole is also observed which

also increase torque and drag.

62


 The weight of the drill string acting on the wellbore is a major contributor to side

forces and to the magnitude of the normal force against the wellbore. As such,

heavier drill strings induce greater side forces against wellbores. Therefore, it is

important to minimize the weight of the drill string within safe limits.

 The soft-string model used in the thesis has shown good results for the simulated

vertical section. However, to simulate a more complex well profile; equations of

the new 3D frictional model must be used for more accurate results.

The two models have many similarities. In a straight section there is no

difference, the equations used are identical, in any curved section the models only

differ in the way side force is calculated. A whole well can then be analyzed by

two sets of equations, one for straight sections and one for curved sections. The

model also has capability of combined axial and tangential motion, such as for

reaming and drilling.

63


REFERENCES

\[1\] Uncoverenergy, www.uncoverenergy.com/the-will-to-drill, last visited on October

2018.

\[2\] Petrowiki, www.petrowiki.org/PEH:Drilling\_Problems\_and\_Solutions, last

visited on October 2018.

\[3\] Britannica, www.britannica.com/science/torque, last visited on October 2018.

\[4\] Johancsik, C.A., Friesch, D.B., and Dawson, R. 1984. Torque and Drag in

Directional Wells-Prediction and Measurement. Journal of Petroleum Technology 36:

987-992.

\[5\] WiperTrip Drilling and Well Engineering Resources, www.wipertrip.com/stuck-

pipe/causes/363-mechanical-sticking-cause-of-stuck-pipe.html, last visited on

October 2018

\[6\] McCormick J.E., Evans C.D., Le J., Chiu T., "The Practice and Evolution of

Torque and Drag Reduction: Theory and Field Results," 2012 International Petroleum

Technology Conference held in Bangkok, Thailand, 7-9 February 2012, IPTC 14863.

\[7\] Drilling Design and Implementation for Extended Reach and Complex Wells,

K&M Technology Group, LLC, Houston, Texas, 2003.

\[8\] Payne M.L., Abbassian F., "Advanced Torque and Drag Considerations in

Extended-Reach Wells," SPE 35102, 1997.

\[9\] Robert F. Mitchell and Robello Samuel, Halliburton DE&DS,” How good is the

Torque- Drag” Model?” SPE/IADC 105068,Copyright 2007, SPE/IADC Drilling

Conference.

\[10\] S. Menand, SPE, H. Sellami, SPE, M. Tijani, and O. Stab, École des Mines de

Paris; D. Dupuis, SPE, Pride- Intl.; and C. Simon, DrillScan,” Advancements in 3D

64


Drillstring Mechanics: From the Bit to the Topdrive”,IADC/SPE 98965, Copyright

2006, IADC/SPE Drilling Conference.

\[11\] Wu, J., and Juvkam-Wold, H.C., 1991. Drag and Torque Calculation for

Horizontal Wells Simplified for Field Use. Oil & Gas J. 89: unpaged.

\[12\] Wu, J., and Juvkam-Wold, H.C. 1993. Study of Helical Buckling of Pipes in

Horizontal Wells. Paper SPE 25503 presented at the Production Operations

Symposium, Oklahoma City, Oklahoma, 21-23 March.

\[13\] Schlumberger Oilfield Glossart,

www.glossary.oilfield.slb.com/Terms/c/caliper\_log.aspx, last visited on October

2018.

\[14\] Petrowiki, www.petrowiki.org/Directional\_survey, last visited on October 2018.

\[15\] PayZone User Manual, 2015

\[16\] Vassilios C. Kelessidis, Shehab Ahmed, Alexandros Koulidis, 2015. An

Improved Drilling Simulator for Operations, Research and Training, paper SPE-

172793-MS presented at the SPE Middle East Oil & Gas Show and Conference held

in Manama, Bahrain, 8 – 11 March.

\[17\] R. Teale, 1965. The concept of specific energy in rock drilling, Int. J. Rock

Mechanics and Mining, 2, 57 – 73.

\[18\] V.C. Kelessidis, P. Dalamarinis, 2009. Monitoring drilling bit parameters allows

optimization of drilling rates, 9th International Multidisciplinary Scientific Geo-

Conference & EXPO SGEM 2009, Albena, Bulgaria, 14-19 June.

\[19\] V.C. Kelessidis, 2009. Need for better knowledge of in-situ unconfined

compressive strength of rock (UCS) to improve rock drillability prediction, 3rd

International AMIREG Conference, Athens, 7-9 Sept.

\[20\] Mohammad Fazaelizadeh, March 2013. Real Time Torque and Drag Analysis

during Directional Drilling. UNIVERSITY OF CALGARY.

\[21\] Hussain Rabia, 2002. Well Engineering & Construction.

65
