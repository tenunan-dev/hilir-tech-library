---
source_id: "doe-affo"
title: "Sustainable Aviation Fuel: Review of Technical Pathways (DOE/NREL/PNNL, 2020)"
url: "https://www.energy.gov/sites/prod/files/2020/09/f78/beto-sust-aviation-fuel-sep-2020.pdf"
retrieved_at: "2026-10-25T15:35:26+00:00"
licence: "public-domain"
reuse_level: "full-text-open"
permitted_use: "any"
sectors: ["REF"]
disciplines: ["PRC"]
sha256: "e3a5d1eca8ba4c2bbda168a7744734221f578feffb7c2a1402928ec1e4050357"
collected: "manual"
summary: "DOE/NREL/PNNL review of SAF production pathways (HEFA, alcohol-to-jet, Fischer-Tropsch, power-to-liquids) covering readiness, feedstock potential and cost context; the multi-lab companion to the SAF Grand Challenge Roadmap."
---

# Sustainable Aviation Fuel: Review of Technical Pathways (2020)

Sustainable Aviation Fuel 
Review of Technical Pathways

(This page intentionally left blank)

iii 
Acknowledgments 
This report was prepared by Johnathan Holladay (Pacific Northwest National Laboratory), Zia Abdullah 
(National Renewable Energy Laboratory), and Joshua Heyne (University of Dayton) and is a compilation of 
information synthesized from three workshops with additional new information inspired from the workshops.  
The authors are indebted to Michelle Kocal (LanzaTech), Steve Csonka (Commercial Aviation Alternative 
Fuels Initiative), Bill Goldner (U.S. Department of Agriculture), Mark Rumizen (Federal Aviation 
Administration), Carol Sim (retired Alaska Airlines, Washington State University), and Jim Hileman (Federal 
Aviation Administration) for their poignant, challenging, and critical review of concepts in the report. 
The authors also thank Zia Haq, Liz Moore (U.S. Department of Energy, Bioenergy Technologies Office), and 
Mohan Gupta (Federal Aviation Administration) for support.

iv 
Abstract 
The 106-billion-gallon global (21-billion-gallon domestic) commercial jet fuel market is projected to grow to 
over 230 billion gallons by 2050 (U.S. EIA 2020a). Cost-competitive, environmentally sustainable aviation 
fuels (SAFs) are recognized as a critical part of decoupling carbon growth from market growth. Renewable and 
wasted carbon can provide a path to low-cost, clean-burning, and low-soot-producing jet fuel. Research shows 
an opportunity to produce fuel in which aromatics are initially diluted with the addition of renewable iso-
alkanes, aromatics are later fully replaced with cycloalkanes, and finally high-performance molecules that 
provide mission-based value to jet fuel consumers are introduced. Key to this fuel pathway is sourcing the 
three SAF blendstocks—iso-alkanes, cycloalkanes, and high-performing molecules—from inexpensive 
resources. When resourced from waste carbon, there are often additional benefits, such as cleaner water when 
sourcing carbon from wet sludges or less waste going to landfills when sourcing the carbon from municipal 
solid waste or plastic waste. Jet fuel properties differ from gasoline and diesel, so research will be most 
successful if it begins with the end result in mind.

Sustainable Aviation Fuel: Review of Technical Pathways 
v 
List of Acronyms 
ASTM ASTM International 
ATJ alcohol-to-jet 
BETO Bioenergy Technologies Office 
Btu British thermal unit(s) 
CAAFI Commercial Aviation Alternative Fuels Initiative 
Co-Optima Co-Optimization of Fuels & Engines 
CORSIA Carbon Offsetting and Reduction Scheme for International Aviation 
DCN derived cetane number 
DOE U.S. Department of Energy 
EERE Office of Energy Efficiency and Renewable Energy 
FAA Federal Aviation Administration  
FT Fischer-Tropsch  
GHG greenhouse gas  
HEFA hydroprocessed esters and fatty acids 
HTL hydrothermal liquefaction 
ICAO International Civil Aviation Organization 
LCA life-cycle analysis 
MFSP minimum fuel selling price 
MSW municipal solid waste  
NASA National Aeronautics and Space Administration  
NJFCP National Jet Fuels Combustion Program  
NREL National Renewable Energy Laboratory  
OEM original equipment manufacturer 
PNNL Pacific Northwest National Laboratory 
R&D research and development 
SAF sustainable aviation fuel  
SPK synthetic paraffinic kerosene 
syngas synthesis gas 
TEA techno-economic analysis 
USDA U.S. Department of Agriculture

Sustainable Aviation Fuel: Review of Technical Pathways 
vi 
Executive Summary 
Airlines have committed to carbon-neutral growth in international commercial aviation beginning in 2021 and 
U.S. airlines have set a goal to reduce carbon dioxide (CO2) emissions by 50% in 2050 compared to 2005 
levels (Airlines for America 2020; IATA 2020). U.S. airlines have improved efficiency by 130% compared to 
1978 levels (Airlines for America 2020). Additional efficiency improvements in planes and engines are not 
likely to be enough. Meeting the 2050 goal will required fuels that have a lower carbon footprint, referred to as 
sustainable aviation fuel (SAF)—defined by the International Civil Aviation Organization (ICAO) as 
alternative aviation fuels that “(i) achieve net GHG [greenhouse gas] emissions reduction on a life cycle basis; 
(ii) respect the areas of high importance for biodiversity, conservation and benefits for people from 
ecosystems, in accordance with international and national regulations; and (iii) contribute to local social and 
economic development, and competition with food and water should be avoided” (ICAO 2018).  
One challenge for providing SAF is that the size of the jet fuel market is large and growing. Global demand is 
expected to increase from 106 billion gallons in 2019 to 230 billion gallons in 2050 (U.S. EIA 2020a). The 
domestic market in 2019 was 26 billion gallons, exceeding 3 quadrillion British thermal units (3 quads) (U.S. 
EIA 2019). This market could consume several hundred million tons of biomass per year, which is consistent 
with the current availability of biomass in the United States (340 million tons) (Langholtz, Stokes, and Eaton 
2016).  
A second challenge is that the price of SAF today is higher than petroleum-based Jet A fuel. Fuel price is a 
hurdle because fuel is 20%–30% of the operating cost of an airline (IATA 2018). Research and development 
(R&D) can help bring the cost down. 
Unlike light-duty vehicles, the low energy density of even the best batteries severely limits opportunities for 
electrification.0F
1 While many are working on electrification, efforts are for smaller aircraft and airlines will 
have no alternative for some time but to use SAF to operate in a GHG-emission-constrained future.  
Part I of this report provides an overview of commercial jet aviation fuel: how it compares to fuels for cars and 
trucks, its composition, its specification, and its certification process.  
Jet fuels consist of n-alkanes, iso-alkanes, cycloalkanes, and aromatics. Aromatics do not burn as cleanly as 
alkanes, resulting in higher particulate emissions, and have lower specific energy. The n-alkanes are acceptable 
but do not meet fluidity and handling properties, limiting their blend potential. The iso-alkanes have high 
specific energy, good thermal stability, and low freezing points. Cycloalkanes bring complementary value to 
iso-alkanes, providing the same functional benefits as aromatics by enabling fuels to meet the density 
requirement and potentially providing the seal-swelling capacity provided today from aromatics. Combined, 
iso-alkanes and cycloalkanes offer the potential to add value to a fuel by enabling high specific energy and 
energy density and minimizing emission characteristics. The U.S. Department of Energy (DOE) is evaluating 
the hypothesis that improved fuel energetic properties (i.e., specific energy and energy density) may provide 
increased range, higher payload capacity, or fuel savings. 
Original equipment manufacturer (OEM)-led ASTM D4054 fit-for-purpose testing generally costs several 
million dollars and can require years to be approved (ASTM 2018). A fast-track approval process has been 
accepted for fuels in which the SAF blending component is limited to 10% and consists of the same types of 
molecules that are in petroleum-based jet fuel. A clearinghouse annex has also been proposed to reduce cost 
and time for approval. The Bioenergy Technologies Office (BETO), Federal Aviation Administration, and 
U.S. Department of Defense are investing in prescreening and testing protocols that need only small quantities 
(milliliters to liters) to provide feedback about a candidate fuel blend fit-for-purpose. To date, there are six 
 
1 Jet fuel has an energy density equal to 43 MJ/kg, while lithium-ion batteries in today’s electric vehicles have an energy density equal to 0.72 MJ/kg (200 
Wh/kg). The amount of weight severely limits battery use in large passenger aircraft.

Sustainable Aviation Fuel: Review of Technical Pathways 
vii 
ASTM International (ASTM) D7566-approved SAFs for use in up to 10% to 50% blends. The SAF initially 
composed of n- and iso-alkanes now include all four hydrocarbon families listed previously and are produced 
from synthesis gas (syngas); fats, oils, and greases; sugars; and alcohols. 
Part I finishes by summarizing the learnings from three BETO-supported workshops. These include the 
Alternative Aviation Fuel Workshop held in Macon, Georgia, in 2016, which focused on SAF production; the 
JET workshop held in Cleveland, Ohio, in 2017, which focused on high-performance fuels; and the Trilateral 
Biojet Workshop held in Richland, Washington, in 2018, which focused on jet fuel R&D collaborations 
between Canada, the United States, and Mexico. Some of the key learnings from these workshops include: 
• The aviation industry seeks to reduce its GHG emissions significantly, decoupling airline growth from 
carbon growth.  
• The current cost of SAF is high. Airlines are willing to support SAF development by purchasing some 
fuel at a higher price, but for SAF to scale, prices need to be reduced. 
• OEM-led ASTM D4054 approval and evaluation process is expensive and time-consuming. Developing 
new engines is even more onerous regarding timescale and cost, and hence a program coupling fuel 
development and engine development R&D would not help overcome industry barriers. 
• Existing engines can use fuels that have a much higher heat of combustion than Jet A, and specific 
energy (i.e., heat of combustion) increases can deliver greater range, higher payload capacity, or 
decreased fuel consumption.  
• More sources of low-cost feedstock are required as fats, oils, and greases are not currently available in 
enough volume to meet SAF demand. 
• The use of cover crops to increase availability of oil seeds while improving soil quality as well as use of 
other lipid-rich streams, such as manures and sludges, may increase availability. Processes for their 
conversion will need to be approved through ASTM. 
• Techno-economic analysis (TEA) and life cycle analysis (LCA) are inconsistent across the SAF industry, 
but the consistent message from most models is that the main cost drivers are feedstock costs, yields, and 
plant capital recovery. 
• Current policies are skewing renewable fuels towards diesel and away from the jet market. 
Part II provides insights resulting from a study of the aviation fuel industry, challenges of and successes with 
the approved pathways, and BETO capabilities and R&D portfolio. The insights focus on reducing cost and 
optimizing the value proposition for SAF. SAF in the future may include strained or otherwise novel 
molecules that are not found in conventional fuels, if the molecules can be produced at low cost. Research 
shows an opportunity to produce fuel in which aromatics are initially diluted with the addition of renewable 
iso-alkanes, aromatics are later fully replaced with cycloalkanes, and finally high-performance molecules that 
provide mission-based value to jet fuel consumers are introduced. To accomplish this transition and reduce 
costs to improve the value proposition, efforts in the following areas will be helpful: 
• Understanding properties of cycloalkanes and production routes from biomass 
• Developing process-intensification strategies as a means of reducing capital cost 
• “Solving another problem” as a means of improving the value proposition 
• Reducing cost and improving value of low-value process streams of currently approved pathways  
• Understanding scaling requirements that make sense to the industry as a means of reducing cost. 
Examples of work could include the following:

Sustainable Aviation Fuel: Review of Technical Pathways 
viii 
• In the near term (0–5 years), research can help further reduce the cost of existing approved pathways to 
iso-alkanes and synthetic paraffinic kerosene molecules. Research could include low-cost routes to 
cycloalkanes, including alkylated cyclohexanes, and understanding the properties of molecules with 
various ring structures available from catalytic, biological, thermal, and hybrid approaches.  
• Public–private partnerships and collaborations across agencies may accelerate cost reductions by 
ensuring a diverse set of stakeholders are involved early in the solution to ensure it can address barriers 
for industrywide use.  
• In the longer term, as SAF volumes increase, aviation fuels may provide better performance and reduced 
emissions (i.e., soot).  
• Use of nontraditional raw materials including carbon oxides, methane, deconstructed plastic, and other 
waste materials may keep cost in parity with conventional fuels. 
BETO’s R&D capabilities and feedstock/technology portfolio provide tools for meeting the technical needs 
to overcome hurdles preventing SAF deployment, including cost reduction.

Sustainable Aviation Fuel: Review of Technical Pathways 
ix 
Table of Contents 
Executive Summary ........................................................................................................................................... vi 
Introduction .......................................................................................................................................................... 1 
Part I – Background ............................................................................................................................................. 2 
1 Jet Fuel Markets ............................................................................................................................................ 3 
1.1 Jet Fuel Versus Ground Transportation Fuel Markets .................................................................... 3 
1.2 How Is Jet Fuel Similar to and Different from Other Transportation Fuels? ................................. 5 
1.3 Why Invest in SAF? ....................................................................................................................... 7 
2 Jet Fuel Specifications .................................................................................................................................. 7 
2.1 Properties: Performance, Operability, and Drop-In Requirements ................................................. 8 
2.1.1 Performance ......................................................................................................................... 8 
2.1.2 Operability ........................................................................................................................... 8 
2.1.3 Drop-In ................................................................................................................................. 9 
2.1.4 Other Properties ................................................................................................................. 10 
2.1.5 Fuel Properties Derived from Bulk Versus Trace Composition ........................................ 10 
2.2 Molecular Families in Jet Fuel ..................................................................................................... 10 
2.2.1 n-Alkanes and iso-Alkanes ................................................................................................ 12 
2.2.2 Aromatics ........................................................................................................................... 12 
2.2.3 Cycloalkanes ...................................................................................................................... 13 
2.2.4 Blended Fuels ..................................................................................................................... 14 
2.3 Beyond Current Fuels – High Performance .................................................................................. 14 
2.4 Review of Chapter 2 ..................................................................................................................... 15 
3 Jet Fuel Certification ................................................................................................................................. 16 
3.1 Getting a Fuel Approved .............................................................................................................. 16 
3.2 A Fast Track to ASTM Approval ................................................................................................. 18 
3.3 Currently Appro
ved and Emerging Fuels ..................................................................................... 19 
3.4 Summary of Current SAFs ........................................................................................................... 20 
4 Workshop Learnings ................................................................................................................................. 21 
4.1 Alternative Aviation Fuel Workshop............................................................................................ 22 
4.2 JET Workshop .............................................................................................................................. 23 
4.3 Trilateral Canada–Mexico–U.S. Biojet Workshop ....................................................................... 23 
Part II – Analysis and Insights ..................................................................................................................... 25 
5 R&D – Fuel Molecules ............................................................................................................................. 26 
5.1 Vision: Reduce Aromatic Content and Increase iso-Alkanes and Cycloalkanes ......................... 26 
5.2 High-Quality iso-Alkanes ............................................................................................................. 28 
5.2.1 Crack Large Molecules ...................................................................................................... 29 
5.2.2 Build Up Small Molecules ................................................................................................. 31 
5.2.3 Direct Fermentation ........................................................................................................... 32 
5.2.4 Summary ............................................................................................................................ 32

Sustainable Aviation Fuel: Review of Technical Pathways 
x 
5.3 Alkylcycloalkanes, Six-Carbon Rings .......................................................................................... 33 
5.3.1 Zeolite-Catalyzed Aromatization Followed by Hydrotreating ........................................... 34 
5.3.2 Phenol Hydrogenation ........................................................................................................ 35 
5.4 Cycloalkanes, Other Ring Sizes, and Fused Rings ....................................................................... 36 
5.4.1 Ring Contraction ................................................................................................................ 36 
5.4.2 Ring-Forming Reactions .................................................................................................... 36 
5.4.3 Ring Motifs in Wood Extractives and Fermentation .......................................................... 36 
5.4.4 Esoteric Cycloalkanes ........................................................................................................ 37 
5.5 Low-Aromatic, High-Energy-Content Fuel Properties ................................................................ 38 
5.5.1 Gaps in Understanding Cycloalkane Properties ................................................................. 38 
5.5.2 Quantifying the Value of SAF ........................................................................................... 39 
5.6 Quantifying the Value Added with SAFs ..................................................................................... 40 
5.7 Summary of Fuel Molecules ......................................................................................................... 40 
6 R&D -- Cost Reduction ............................................................................................................................. 41 
6.1 Feedstock-Related Research ......................................................................................................... 41 
6.1.1 “Solve Another Problem” .................................................................................................. 41 
6.1.2 Collected Carbon from Existing or Developing Processes ................................................ 42 
6.1.3 Waste Gases ....................................................................................................................... 42 
6.1.4 CO2 as a Carbon Source ..................................................................................................... 42 
6.2 Reducing Capital Cost .................................................................................................................. 44 
6.2.1 Use Current and Distressed Infrastructure ......................................................................... 44 
6.2.2 Petroleum Refinery Integration .......................................................................................... 45 
6.2.3 Separations ......................................................................................................................... 45 
6.2.4 R&D Needs for Small-Scale Distributed Refineries .......................................................... 45 
6.3 Rethinking Biorefineries ............................................................................................................... 46 
6.3.1 Sugars to Products, Lignin to Fuels ................................................................................... 46 
6.3.2 Focus R&D on Conversion Platforms That Provide Product Flexibility ........................... 46 
6.3.3 Feedstock Flexibility to Use Full Capacity ........................................................................ 47 
6.4 Sourcing Hydrogen ....................................................................................................................... 48 
6.5 Analysis of Cost Reduction .......................................................................................................... 48 
6.6 Summary of Cost Reduction ......................................................................................................... 49 
7 Summary and Insights ............................................................................................................................... 49 
7.1 An R&D Strategy for SAF ........................................................................................................... 49 
7.2 Insights on R&D ........................................................................................................................... 50 
7.2.1 Focus R&D on Low-Cost iso- and Cycloalkane Production ............................................. 50 
7.2.2 Focus on Low-Cost Feedstocks ......................................................................................... 51 
7.2.3 Focus R&D on Conversion Platforms that Provide Product Flexibility ............................ 51 
7.2.4 Provide Replacement for Hydrogen Gas in Distributed Processing .................................. 51 
7.2.5 Refine and Expand Analysis .............................................................................................. 51 
7.2.6 Sequencing R&D to Achieve Impact in the Short, Medium, and Long Term ................... 52 
7.3 Cooperative Opportunities for R&D ............................................................................................ 52 
7.3.1 Collaboration Between the National Laboratories ............................................................. 52 
7.3.2 Intersection with FAA Center of Excellence and USDA ................................................... 52

Sustainable Aviation Fuel: Review of Technical Pathways 
xi 
7.3.3 Intersection with North American Partners ........................................................................ 53 
7.3.4 SAF Working Group .......................................................................................................... 53 
References ......................................................................................................................................................... 54 
Appendix 1. Bioenergy Technologies Office Mission ................................................................................... 58 
Appendix 2. ASTM Fuel Approval Prescreening Tests ................................................................................ 59 
Appendix 3. Workshop Learnings ................................................................................................................... 60 
A3.1 Macon Workshop ........................................................................................................................ 60 
A3.2 Cleveland Workshop ................................................................................................................... 61 
A3.2.1 Two Schools of Thought .......................................................................................................... 61 
A3.2.2 High-Performance Fuel Options .............................................................................................. 61 
A3.2.3 Engine and Combustor Options ............................................................................................... 62 
A3.2.4 Aircraft On-Board Considerations ........................................................................................... 64 
A3.2.5 High-Performance Fuel Development to Deployment ............................................................. 65 
A3.2.6 Key Takeaways ........................................................................................................................ 66 
A3.3 Richland Workshop ..................................................................................................................... 66 
A3.3.1 Synopsis of the Workshop Report............................................................................................ 67 
A3.3.2 Key Takeaway Messages ......................................................................................................... 67

Sustainable Aviation Fuel: Review of Technical Pathways 
xii 
List of Figures 
Figure 1. U.S. transportation fuel consumption (billions of gallons per year) (U.S. EIA 2017) ................... 3 
Figure 2. Major U.S. refined products pipelines carrying jet fuels (Airlines for America 2018) and the 10 
largest airports by traffic volume ................................................................................................................. 5 
Figure 3. Carbon numbers and boiling points for gasoline, jet, and diesel fuels ............................................ 6 
Figure 4. U.S. renewable fuel production in 2018 (U.S. EPA 2019) ............................................................... 7 
Figure 5. Composition of an average Jet A (POSF 10325) (Edwards 2017). n-Alkanes, iso-alkanes, 
cycloalkanes, and aromatics are approximately normally distributed across the carbon number range. 
A molecule with 11 to 12 carbons is approximately average. ................................................................ 11 
Figure 6. Various examples of fused and strained molecules ....................................................................... 13 
Figure 7. Performance metrics of a fuel can be clumped into nine categories that are dependent on the 
mission of the flight ................................................................................................................................... 14 
Figure 8. Four-tiered process for testing new aviation fuels and fuel additives, per the ASTM D4054, 
Standard Practice for Evaluation of New Aviation Turbine Fuels and Fuel Additives ........................ 17 
Figure 9. ASTM-D4054 Fast Track Annex for qualification and approval of new aviation fuels that meet 
the compositional and performance standards with a limit of 10% blend (highlighted portion differs 
compared to Figure 8) ............................................................................................................................... 19 
Figure 10. SAF pathways approved under ASTM D7566 and emerging fuel pathways in the ASTM 
D4054 approval process ............................................................................................................................ 20 
Figure 11. Summary of four classes of hydrocarbons.................................................................................... 21 
Figure 12. Energy density and specific energy of various hydrocarbons ..................................................... 26 
Figure 13. Strategic focus on iso-alkanes and cycloalkanes .......................................................................... 28 
Figure 14. iso-Alkane production by cracking and isomerizing large molecules, building up small 
molecules, or fermentation ........................................................................................................................ 29 
Figure 15. Lipid sources for HEFA, including waste sources and crops ...................................................... 30 
Figure 16. Routes to cyclohexanes that can be synthesized in the jet-fuel range ........................................ 34 
Figure 17. Smaller and larger rings from 3 to 8 carbons ............................................................................... 36 
Figure 18. New ring structures, fused rings, and different ring sizes from nature ....................................... 37 
Figure 19. Esoteric molecules under examination for fuel properties .......................................................... 38 
Figure 20. CO2 from ethanol production conversion to jet fuel via synthesis gas ....................................... 44

Sustainable Aviation Fuel: Review of Technical Pathways 
xiii 
List of Tables 
Table 1. Performance Properties ........................................................................................................................ 9 
Table 2. Operability and Drop-In Requirements ............................................................................................... 9 
Table 3. Fuel Properties Derived from Either Bulk or Trace Components .................................................. 10 
Table 4. Comparison of Three Jet A Fuel Compositions and Properties (Edwards 2017) .......................... 11 
Table 5. Fuel Properties – Molecular Structure Relationship ....................................................................... 12 
Table 6. Approximate Fuel Volumes, Time, and Cost for D4054 Testing (CAAFI 2019) ......................... 18 
Table 7. The Sooting Propensity of Various Hydrocarbons (Yang, Boehman, and Santoro 2017; Olson, 
Pickens, and Gill 1985) ............................................................................................................................. 33 
Table A.1. Fuel Properties from the OEMs at the JET Workshop ................................................................ 63

Sustainable Aviation Fuel: Review of Technical Pathways 
1 
Introduction 
Commercial aviation is responsible for about 13% of transportation greenhouse gas (GHG) emissions (U.S. 
EIA 2020b, 202). Airlines have committed to carbon-neutral growth for international commercial aviation 
beginning in 2021 and reducing carbon dioxide (CO2) emissions by 50% in 2050 compared to 2005 levels 
(Airlines for America 2020; IATA 2020). While airlines are squeezing efficiency through improved aircraft 
and flight logistics, decoupling carbon growth will require non-fossil-sourced fuels, which in this report will be 
referred to as sustainable aviation fuel (SAF).1F
2 
In 2018, about two million gallons of SAF were produced. An additional 300 million gallons of renewable 
diesel was also produced using the same technology.2F
3 This is not enough for airlines to meet their CO2 
reduction goals, which is 50% GHG reduction by 2050.  
Purchasing fuel is a primary operating cost for airlines, a cost only exceeded by labor (IATA 2018). SAF will 
need to be cost-competitive, but although costs must be reduced, SAF does not need to mimic petroleum. A 
better fuel via bio-derivatives can be made and still meet international specifications (i.e., ASTM International, 
or ASTM). 
This report presents ways to lower costs and improve the benefits of aviation fuel through targeted SAF 
production. Part I provides background information needed for decision makers, program and technology 
managers, and biofuel researchers: 
• Chapter 1. Jet Fuel Markets 
• Chapter 2. Jet Fuel Specifications 
• Chapter 3. Jet Fuel Certification 
• Chapter 4. Workshop Learnings 
Given the preceding background, in Part II insights in consideration of one possible value chain is provided: 
• Chapter 5. R&D – Fuel Molecules 
• Chapter 6. R&D – Cost Reduction 
• Chapter 7. Summary and Insights 
The appendices provide more information.
 
2 Aircraft are more efficient than ever, and flight plans are being optimized for fuel efficiency. Electrification is not an option for commercial flight for 
decades, if not longer. Fuel that has a low carbon footprint is the sole option. 
3 Another 600 million gallons of renewable diesel used in the United States is under consideration for ASTM approval for jet fuel (U.S. EPA 2019).

Sustainable Aviation Fuel: Review of Technical Pathways 
2 
Part I – Background

Sustainable Aviation Fuel: Review of Technical Pathways 
3 
1 Jet Fuel Markets 
1.1 Jet Fuel Versus Ground Transportation Fuel Markets 
The ground transportation fuel market (motor gasoline and diesel) is 183 billion gallons per year (Figure 1). 
The market is highly segregated with a diversity of producers, sellers, and customers, each with various needs. 
Gasoline is blended with ethanol by up to 10% by volume, depending on the geographic location, climate, time 
of year, and other reformulated blendstock for oxygenate blending requirements, and this can have a 
significant impact on price. Gasoline is sold in different grades to a multitude of customers (more than 280 
million vehicles were on the road in 2019 [Hedges & Company 2020]) whose seasonal driving practices alter 
demand. Marketplace transactions for gasoline sales are generally at smaller volumes and for the short term, 
allowing for greater price variability. 
 
Figure 1. U.S. transportation fuel consumption (billions of gallons per year) (U.S. EIA 2017) 
Note: LNG = liquid natural gas 
The supply chain for gasoline uses blending terminals at central locations where the hydrocarbon fuel from 
refineries is blended with ethanol and other additives. These central locations confer a brand name to the final 
product that is shipped to service stations and is where the fuel is tested for quality. Gasoline is generally 
shipped via pipeline or rail to blending terminals and then transported to individual service stations in smaller 
quantities by truck.  
The demand for motor gasoline is expected to decrease in the coming decades because of higher-efficiency 
drivetrains, increasing electrification of the light-duty fleet, and societal changes such as increased use of ride 
sharing. 
The jet fuel market is different from the gasoline market in size, consumers, property variance, and demand 
locations. The domestic market size is 26 billion gallons per year. The global market size exceeds 81 billion 
gallons (Airlines for America 2018). Passenger demand is projected to double over the next 20 years (IATA 
2016).3F
4 In contrast to the gasoline market, the jet fuel market has a smaller number of customers4F5 (individual 
airlines and a modest number of fuel suppliers), who purchase the bulk of their fuel using negotiated long-term 
purchase agreements, and some small-volume customers (such as corporate fleets and private airplane owners) 
who purchase fuel at retail prices. Airlines are very price-sensitive because jet fuel accounts for approximately 
 
4 This is also consistent with projections from the U.S. Energy Information Administration. 
5 Two hundred and ninety International Air Transport Association airlines represent 82% of traffic, while several thousand smaller airlines comprise the 
rest.

Sustainable Aviation Fuel: Review of Technical Pathways 
4 
20%–30% of their operating costs. Some studies have suggested that a price increase of $1.00 per barrel of 
crude oil results in roughly $425 million of additional expense for the airline industry (Davidson et al. 2014). 
Large airlines, having significant bargaining power, negotiate offtake agreements with fuel providers for long 
periods—often years—because these agreements can be made at lower fuel prices and significantly reduce 
exposure to market volatility. In general, the price of jet fuel correlates to that of ultra-low-sulfur diesel, which 
is often used as a reference point for supply contracts (Airlines for America 2018). Jet fuel prices at the Gulf 
Coast are usually lower because production exceeds demand in that part of the country. 
Despite the sensitivity of bottom-line revenue to fuel prices, the renewable jet fuel demand curves for large 
airlines can potentially be more elastic with respect to price because airline customers have voluntarily shown 
a willingness to incur extra costs to assist new fuel introductions into the market. In addition to airlines, fixed-
base operators at airports can also be significant fuel purchasers. Fixed-base operators purchase fuel in bulk 
and resell it at airports to small corporate and private customers at retail prices, which can be three times the 
spot price for jet fuel. As a result, there can be substantial differences in price for the same Jet A fuel between 
what a large airline pays through a large and/or long-term offtake agreement and the price a corporate 
customer and private airplane owner pay. 
Unlike gasoline, jet fuel specifications do not vary by climate, time of year, or location, and thus blending, 
quality assurance, and quality control to meet applicable fuel specifications are done first at the refinery, with 
subsequent downstream validations. The jet fuel supply chain is different from that of gasoline because of the 
large volume requirements for jet fuel delivered to airports. Generally, shipment is by pipeline or barge from 
refineries to terminals, and from there to storage near airports (Figure 2). Airlines buy fuel from multiple 
suppliers because not every fuel supplier operates at every airport. Many airlines also purchase fuel directly 
from refineries, take the title of the fuel at the refinery gate, and ship it to where it is needed in order to avoid 
disruption of the fuel supply (ASTM 2018). Maintaining resilient jet fuel production and transport (pipelines) 
will be critical, particularly as fuel consumption doubles over the next 20 years. SAF offers resiliency in terms 
of feedstock and may help with fuel transport resiliency if biojet fuel facilities are located near the airports they 
serve. Port authorities that operate airports, such as SeaTac in Washington State, have announced their support 
of being a fuel aggregator and having fuel produced on land the ports own (Stephanie Meyn, personal 
communications; Biojet Workshop 2018).

Sustainable Aviation Fuel: Review of Technical Pathways 
5 
 
Figure 2. Major U.S. refined products pipelines carrying jet fuels (Airlines for America 2018) and the 10 largest airports by 
traffic volume 
1.2 How Is Jet Fuel Similar to and Different from Other Transportation Fuels? 
Gasoline, jet, and diesel fuels are mostly blended mixtures of several hundred different hydrocarbon 
molecules. Molecules in gasoline fuel range from those containing 4 carbon atoms to those containing 12 
carbon atoms. Gasoline has an initial boiling point at atmospheric pressure of about 35°C and a final boiling 
point of about 200°C. Molecules in jet fuel range from those containing 8 carbon atoms to those containing 16 
carbon atoms. Jet fuel has an initial boiling point at atmospheric pressure of about 125°C and a final boiling 
point of about 290°C. Molecules in diesel fuel range from those containing 8 carbon atoms to those containing 
23 carbon atoms. Diesel has an initial boiling point at atmospheric pressure of about 150°C and a final boiling 
point of about 380°C.  
As shown in Figure 3, jet fuel is the middle distillate product between gasoline and diesel. There is significant 
overlap in the boiling point range of gasoline and jet fuel, and almost complete overlap in the boiling point 
range between jet fuel and diesel. These overlaps have several implications from the perspective of fuel 
producers.  
First, if a process produces molecules that have a broad range of boiling points spanning those of gasoline, jet, 
and diesel, then collection of the jet fuel fraction through distillation will need to be done in a manner in which 
neither the gasoline nor diesel stream is compromised, which can affect the amount of jet fuel recovered. 
Otherwise, the gasoline fraction is left with only light volatile components (4–8 carbons in length) and the 
diesel fraction is composed of a distribution with the heaviest fractions.

Sustainable Aviation Fuel: Review of Technical Pathways 
6 
 
Figure 3. Carbon numbers and boiling points for gasoline, jet, and diesel fuels 
Second, the almost complete overlap of the boiling point ranges of jet fuel and diesel allows a refinery to select 
which product to make depending on market conditions and other incentives. For example, if the market value 
of diesel is higher than that of jet fuel, then a refinery would be incentivized to produce diesel rather than jet 
fuel. This would be particularly true if a refinery can have good control of the boiling point range and does not 
have to distill out the lower-value heavy components. Today, biorefiners are producing renewable diesel at the 
expense of renewable jet fuel. 
Third, if all jet fuel were replaced with SAF (in a long-term scenario), refiners would still have a home for all 
the fractions they produce. Today, many refineries do not produce jet fuel. Figure 4 shows 2018 domestic 
biofuel production. U.S. production of renewable diesel exceeded 300 million gallons. SAF, made with the 
same technology, was two million gallons. While there is some difference in production cost, the difference in 
renewable diesel production and SAF production is driven by policy.

Sustainable Aviation Fuel: Review of Technical Pathways 
7 
 
Figure 4. U.S. renewable fuel production in 2018 (U.S. EPA 2019) 
Note: RIN = renewable identification number 
1.3 Why Invest in SAF? 
Jet fuel is purchased by a small group of buyers who negotiate long-term contracts, or at least yearly contracts, 
and are exceptionally price-conscious. Those same purchasers, such as United Airlines and FedEx, have 
voluntary goals to decouple passenger growth and carbon emission growth (United Airlines 2018; FedEx 
2012). They view SAF as being critical to their future. Hence, there is a strong market pull for SAF. 
The fuels are delivered to airports via pipelines, stored in common tankage, and delivered to planes through 
hydrant systems at major airports. SAFs, as discussed in Chapter 2, are delivered as fully fungible fuels, and 
once they enter the airport storage are in the same storage and delivery systems as all other jet fuels. Hence, 
SAF fits into current infrastructure. 
The jet fuel market, although smaller than gasoline and diesel fuel markets, still exceeds 26 billion gallons (3.4 
exajoules of energy, or greater than 3 quadrillion British thermal units, or Btu). Market growth is expected to 
double over the next 20 years, while gasoline markets are not expected to grow. U.S. Department of Energy 
(DOE) investment today addresses current and future market needs. 
The jet fuel market matches biomass availability. The amount of biomass available today—about 340 million 
tons according to the 2016 Billon-Ton Report—could provide roughly 21 billion gallons, about the size of the 
jet fuel market (Langholtz, Stokes, and Eaton 2016). As biomass availability is expected to increase, so too 
does the size of the jet fuel market.  
Unlike cars, the commercial jet fleet currently cannot be fully electrified with battery technologies. SAF will 
continue to be important into the 21st century. 
2 Jet Fuel Specifications 
The material in this chapter covers the general requirements for SAF in terms of performance, operability, and 
infrastructure compatibility (drop-in). The information is useful background to researchers considering fuel 
properties desired in SAF.  
Jet fuel specifications are defined in ASTM D1655, Standard Specification for Aviation Turbine Fuels (ASTM 
2019a). ASTM has defined the steps for qualification and approval of new aviation turbine fuels in ASTM

Sustainable Aviation Fuel: Review of Technical Pathways 
8 
D4054, Standard Practice for Evaluation and Approval of New Aviation Turbine Fuels and Fuel Additives 
(ASTM 2019b). Finally, there is a specification for SAF, ASTM D7566, Standard Specification for Aviation 
Turbine Fuels Containing Synthesized Hydrocarbons (ASTM 2019c). A fuel meeting these specifications is 
fully fungible. Maintaining jet fuel properties is critical. Meeting the specifications outlined in ASTM D7566 
Table 1, Parts 1 and 2, and the associated D7566 annex ensures the necessary performance and operability 
requirements are met (ASTM 2019c). 
2.1 Properties: Performance, Operability, and Drop-In Requirements 
The categorical description of jet fuels and associated properties vary based on perspective. The following 
describes a jet fuel and its properties from the perspective of value, safety, and compatibility. The categorical 
requirements for jet fuel are then (1) performance (value added), (2) operability (safety), and (3) drop-in 
(infrastructure compatibility). A drop-in fuel is deemed to be equivalent to conventional jet fuel, can be used in 
current engines and infrastructure, and is fully fungible. These requirements are essential for safety, general 
usage, and execution of commercial and military missions. 
2.1.1 Performance 
Performance attributes in this report refer to properties that add to the value proposition of a fuel in the context 
of a mission. In a broader sense, performance can also be used to describe life cycle carbonaceous emissions, 
costs, or other associated valued effects throughout the supply chain. The functional performance of gas-
turbine aviation fuels is defined by the ability of a fuel to service the Brayton cycle of an engine. Performance 
properties are those that can provide the most direct financial incentives to fuel end-use consumers. These 
properties include:  
• S
pecific energy (energy per unit mass), expressed as MJ/kg 
• E
nergy density (energy per unit volume), expressed as MJ/L  
• E
missions, including particulate matter  
• T
hermal stability (inhibition of fuel to degrade or coke under thermal stress).  
T
hese performance properties enable mission payload-range requirements and maintenance of an acceptable 
limit of fuel degradation and, as discussed later, limit the range, payload, and cycle efficiency of fuel in a 
mission. The ratio of the number of hydrogen atoms to the number of carbon atoms in a molecule largely 
determines the specific energy of the fuel. Fuels with higher ratios have higher specific energies in the absence 
of bond strain. The fuel’s liquid density mostly determines the energy density of fuel because liquid densities 
change more than specific energies.  
Other properties of the fuel are also key to performance, such as a low freeze point, which allows long-range 
flights to use more optimum flight profiles, and clean-burning fuels, which may reduce maintenance cost. 
2.1.2 Operability 
Operability limits apply to the safe use of fuel under specific engine conditions. The determination of an SAF’s 
operability limits is the focus of high volumetric and capital cost expenditures as part of the ASTM D4054 
evaluation and approval process. Properties associated with operability limits are in the ASTM D1655 
specification, documented in the previous D4054 approval process, and under investigation through the 
National Jet Fuels Combustion Program (NJFCP), which is trying to streamline the process of securing ASTM 
approval of SAFs for commercial uses. Historically, the operability limits of an SAF are part of the 
certification process at original equipment manufacturer (OEM) facilities. The conditions of such tests ensure 
the safe usability of fuel under the most severe conditions, such as cold-soaked altitude relight with its 
associated low temperature and pressure.

Sustainable Aviation Fuel: Review of Technical Pathways 
9 
2.1.3 Drop-In 
Drop-in limits refer to a fuel’s ability to be used in conjunction with existing aircraft and handling hardware 
with no changes to fuel and aircraft infrastructure. For example, novel SAFs that meet drop-in requirements 
must have the ability to be used seamlessly with existing operations and handling because an aircraft can be in 
service for decades (i.e., they must be fully fungible). Nonetheless, non-drop-in characteristics of fuel are 
conceptually possible. However, non-drop-in fuels would have to meet additional requirements as well as all 
those associated with SAFs. These would be on top of those for the additional fueling infrastructure.  
Most of the performance characteristics and operability limit effects described here are associated with fuel 
bulk properties. However, both bulk and trace fuel property limits are needed to meet drop-in requirements. 
Performance, operability, and drop-in limits are listed in Table 1 and Table 2. Additional properties and 
specification requirements are listed in ASTM D4054 and D7566, and the D1655 documentation. The impacts 
of some of these properties on engine operability remains an open research issue that the NJFCP is currently 
investigating. 
Table 1. Performance Properties 
Property 
Units, {qualitative}, 
[quantitative] Description/Relevance 
Specific energy {Energy/mass}, [MJ/kg] Enables fuel efficiency by lowering takeoff weight, critical for 
mass-limited missions 
Energy density a {Energy/volume}, [MJ/L] Most important metric for volume-limited missions or military 
operations involving refueling 
Thermal stability Variable Limits ability of fuel to sustain elevated temperatures in the 
engine and fuel injector 
Emissions/sooting a Variable  Particulate emissions  
a Not included as part of the ASTM D1655 specification 
Table 2. Operability and Drop-In Requirements 
Property Units, {qualitative}, [quantitative] Description/Relevance 
Viscosity {length2/time}, [mm2/s] Important for flow performance, particularly at cold 
temperatures 
Density {mass/volume}, [kg/m3] Used in calculating fuel tank volumes 
Freeze point {temperature}, [°C] Inhibits freezing of the fuel in flight at an altitude 
Flash point {temperature}, [°C] Safe handling 
Distillate temperature {temperature}, [°C] Enables sufficient volatility of a fuel 
Derived cetane number 
(DCN) a 
unitless Important for lean blowout limit stability 
Minimum aromatic 
concentration a 
{percent}, [%] Ensures proper swelling of certain O-rings and seals that 
have been previously exposed to fuels with high aromatic 
content 
Surface tension a {force/length}, mN/m High values can inhibit spray break-up and atomization 
a Not currently included as part of the ASTM D1655 specification 
Bulk properties most important for approval and performance are in the ASTM D1655 specification sheet for 
Jet A and Jet A-1 for conventional fuels. Bulk properties are determined by the mean mass or volumetric 
composition of fuel and typically are not influenced heavily by contaminants or molecules in low 
concentrations, the latter of which must not be ignored.

Sustainable Aviation Fuel: Review of Technical Pathways 
10 
2.1.4 Other Properties 
Trace composition properties typically relate to auxiliary yet critical functions of the fuel as a working fluid 
while being pumped and stored in an aircraft or storage facility. Deleterious trace properties will result in 
seizing up of mechanical parts, leaking fuel, corrosive behavior, or other antagonistic issues.  
All told, these specifications tend to be tighter and less malleable than those used in marine or ground 
transportation applications because of the significantly higher safety issues, capital intensity of aircraft and 
engines, and the broad range of performance requirements that aviation transportation imposes on the fuel 
compared to other applications. The nuanced testing of SAFs for bulk and trace properties is an example of 
these more stringent specifications. Chapter 3 illustrates some of these nuanced and extensive testing 
requirements. 
2.1.5 Fuel Properties Derived from Bulk Versus Trace Composition 
Jet fuel properties are derived from both the bulk composition and trace components of the fuel. A list of bulk 
and trace properties is provided in Table 3. 
Bulk fuel properties primarily address performance and operability requirements of a fuel. Thermodynamic 
and mission efficiencies are determined by the thermal stability and energy content (MJ/kg and MJ/L), 
respectively. Safety and operability limits are primarily determined by a fuel’s viscosity, density, reactivity 
(DCN), surface tension, flash point, and freeze point. 
Table 3. Fuel Properties Derived from Either Bulk or Trace Components 
Bulk Composition Trace Composition 
Energy content Lubricity 
Combustion character Stability 
Distillation range Corrosivity 
Density Cleanliness 
Fluidity Electrical conductivity 
Trace properties must not impair the performance, combustion operability, or drop-in nature of the fuel. Trace 
properties are associated with material and component wear such as pumps (lubricity), corrosion, thermal 
stability, and conductivity, which typically affect aircraft operability. Both the bulk and trace property 
requirements of jet fuel need to be understood and considered even at the bench scale, when costs associated 
with separation and cleanup can still be mitigated. 
2.2 Molecular Families in Jet Fuel 
Four hydrocarbon families compose an acceptable alternative to conventional jet fuel: aromatics, cycloalkanes, 
iso-alkanes, and n-alkanes (Figure 5). Other molecular families—oxygenated molecules, heteroatom-
containing molecules, unsaturated hydrocarbons (olefins), and metals—are unacceptable for various reasons, 
including poor thermal stability, freeze point, and specific energy properties. Conventional fuels are composed 
of molecules with approximately 7 to 18 carbons, and most of the composition stems from molecules with 9 to 
15 carbons and an average of 12 carbons.

Sustainable Aviation Fuel: Review of Technical Pathways 
11 
 
Figure 5. Composition of an average Jet A (POSF 10325) (Edwards 2017). n-Alkanes, iso-alkanes, cycloalkanes, and 
aromatics are approximately normally distributed across the carbon number range. A molecule with 11 to 12 carbons is 
approximately average. 
Conventional fuel variance can be bounded by the difference between JP-8 and JP-5 fuels, which are 
conventional aviation fuels that meet ASTM D1655 but have different underlying specifications. JP-8-type 
fuels are generally “lighter” in molecular composition because lower-carbon-number molecules compose a 
larger fraction of the total fuel. Conversely, JP-5-type fuels are “heavier” due to the U.S. Navy’s requirement 
for a higher flash point and because a fuel’s average molecular weight scales proportionally. 
Table 4 reports select properties of a best-, average-, and worst-case conventional fuel. While the differences in 
conventional fuel properties seem small, combustion operability testing on them has yielded significantly 
different results, particularly regarding cold-ignition experiments. Qualitative jet fuel rankings are based on 
fuel performance and observed operability limits under NJFCP (Edwards 2017). 
Table 4. Comparison of Three Jet A Fuel Compositions and Properties (Edwards 2017) 
 
Best-case operability 
(JP-8 POSF 10264) 
Average 
(Jet A POSF 
10325) 
Worst-case 
operability 
(JP-5 POSF 
10289) 
Composition, wt%: 
   
n-alkanes 26 20 13 
iso-alkanes 37 30 19 
monocyclic alkanes 19 25 30 
bicyclic alkanes 3 7 17 
aromatics 14 19 20 
Properties: 
   
hydrogen to carbon ratio (H/C) 2.01 1.94 1.90 
specific energy (MJ/kg) 43.2 43 42.9 
density (kg/m3) 780 803 827

Sustainable Aviation Fuel: Review of Technical Pathways 
12 
 
Best-case operability 
(JP-8 POSF 10264) 
Average 
(Jet A POSF 
10325) 
Worst-case 
operability 
(JP-5 POSF 
10289) 
energy density (MJ/L) 33.7 34.5 35.5 
avg. molecular weight (g/mol) 152 159 166 
viscosity (cSt) 3.5 4.6 6.5 
flash point (°C) 42 48 60 
2.2.1 n-Alkanes and iso-Alkanes 
The n- and iso-alkane families of molecules typically compose approximately 55%–60% of conventional jet 
fuel. Table 5 summarizes the performance and operability effects of these molecules. They tend to have higher 
specific energy, lower energy density, and higher thermal stability than the remaining molecular families. The 
blending of these molecules is limited by the density specification despite their otherwise high-performance 
characteristics. n-Alkanes are known to have the highest DCN of hydrocarbons that have similar carbon 
numbers, and all n-alkanes violate either the freezing point or flash point specifications of ASTM D1655. 
Increasing isomeric branching of n-alkanes generally lowers the freeze point, which is a positive attribute (+), 
and lowers the DCN, which is a negative attribute (−), while raising the vapor pressure, which is a positive for 
ignition (+) but negative for flash point (−). 
Table 5. Fuel Properties – Molecular Structure Relationship 
 
 n-Alkanes Iso-Alkanes Weakly Branched Iso-Alkanes Strongly Branched Cycloalkanes Monocyclic Cycloalkanes Fused Bicyclic Aromatics 
Performance 
Specific energy ++ ++ ++ + 0 − 
Energy density − − − + ++ ++ 
Thermal stability + + + + +  
Sooting ++ ++ ++ + + − − 
Operability 
DCN ++ + −   − 
Density − − − + ++ + 
Freeze point − +/− + + + + 
Sooting ++ ++ ++ + + − − 
 
2.2.2 Aromatics 
Aromatics in conventional jet fuel are mostly composed of alkyl aromatics with smaller amounts of tetralins 
and naphthalenes (multi-ring aromatics). The attributes can be positive (+) or negative (−). Collectively, this 
group of molecules has low specific energy (−), high energy density (+), and contributes most significantly to 
sooting (− −). Early SAF testing indicated that aromatics contribute significantly to the ability of other nitrile 
O-rings to swell. The key is that the contribution of aromatics results in the current misperception of their need 
in all SAF blends. Aromatics are necessary only to ensure the swelling of nitrile O-rings and seals that have 
been previously exposed to fuel that had a high aromatic content. Seals that have not previously been exposed 
to fuel do not require aromatics for acceptable performance, as demonstrated using 100% hydroprocessed 
esters and fatty acids (HEFA) fuel in Boeing 777 aircraft. Additionally, aromatics are well established as the 
most significant contributor to incipient soot production and particulate matter emissions. Ground and altitude 
emissions of particulate matter are a growing concern in the aviation community because they contribute

Sustainable Aviation Fuel: Review of Technical Pathways 
13 
heavily to ground air quality, contrails, and environmental forcing. This concern could be addressed in part by 
understanding the minimal aromatic content required and blending aromatics to the minimum. Alternatively, 
there is evidence that certain cycloalkanes can provide seal swelling (FAA 2013). Research to validate the seal 
swelling requirements is needed as the International Civil Aviation Organization (ICAO) will begin regulating 
the emission of particulate matter in forthcoming requirements (ICAO 2019). 
2.2.3 Cycloalkanes 
Cycloalkanes comprise a diverse spectrum of molecules and properties, discussed here in the context of 
monocyclic, fused bicyclic, and strained molecules. Each of these cycloalkane classes is associated with higher 
energy densities than typical Jet A fuel; however, the properties across this group can vary significantly and it 
remains an area of needed research. Nominally, average Jet A fuel is approximately 25/7/0 wt% 
monocyclic/fused bicyclic/strained. The monocyclic portions of conventional fuels are mostly composed of 
six-member rings with alkyl chains and branches stemming from the central ring. Monocyclic alkanes can 
have a density (+), freeze point (+), flash point (+), and specific energy (+) exceeding conventional fuel 
requirements. Alkylated monocyclic alkanes could be the only molecular subfamily capable of being a drop-in 
fuel, ignoring the aromatic requirement and pending an acceptable DCN. Monocyclic alkanes with larger ring 
structures (>7 carbons) and smaller ring structures (3–5 carbons) remain an area of continued exploration in 
the properties they possess and biofeedstocks that could feed into their production.  
Fused bicyclic alkanes in Jet A fuel are composed of decalin moieties (Figure 6), often with additional carbons 
of varying alkyl lengths and branching. These fused bicyclic molecules are characterized by high energy 
densities (++), specific energies near Jet A averages (~), and superior thermal stabilities (++). Additionally, 
decalin and monocyclic alkanes have shown similar swelling capabilities near those of Jet A fuel with 
aromatics, making them a potential replacement for the aromatic concentration minimums previously 
mentioned (Graham et al. 2011). 
H
H
H
H
trimethyl-
adamantine
trans-decalin tetrahydro-
dicyclopenta-
dienes
carane camphane pinane
hydrogenated turpentines
cis-decalin
exo-
endo- adamantine
 
Figure 6. Various examples of fused and strained molecules 
Strained cycloalkanes remain an active area of research. This class of cycloalkanes is not found in 
conventional fuels and may have thermal stability issues. It may be difficult to predict the properties of 
strained cycloalkanes. Each of these would pose unique challenges to obtaining the approval of a novel SAF 
and advancement of technologies to enable their research exploration. 
Variation in conformation and level of branching can impact the fuel properties of fused and strained 
cycloalkanes. Examples of these property challenges can be found in the property variance between apparently 
similar molecules shown in Figure 6: 
• F
reeze points of endo- versus exo-tetrahydrodicyclopentadiene (+84°C and –90°C, respectively)

Sustainable Aviation Fuel: Review of Technical Pathways 
14 
• DCNs of trans- versus cis-decalin5F
6 (32.0 and 41.6, respectively)  
• Specific energies of alkyl adamantines versus adamantine (approximately –2% and +3% difference from 
an average Jet A fuel, respectively). 
The opportunity for a novel SAF with high performance lies in the reduction and removal of aromatics, and 
with the addition of molecules with high energy densities and specific energies. (However, it should be noted 
that in some optimization scenarios the low specific energy, high energy density JP-10 is preferred in 
concentrations around 2%.)  
2.2.4 Blended Fuels 
Fuels typically consist of blends of molecules rather than single compounds or even single classes of 
compounds.6F
7 The properties of blended fuels are based on the bulk properties of the blended molecules and 
minor/trace molecules (including inorganics, metals, etc.). Molecules from four chemical families—n-alkanes, 
iso-alkanes, cycloalkanes, and aromatics components—meet the requirements codified by ASTM when 
blended, which is the subject of Chapter 3. Because a single molecule or family of molecules will be blended 
with other molecules, only the finished fuel needs to meet the fuel specifications.  
2.3 Beyond Current Fuels – High Performance  
Fuel performance can be measured by the usefulness of a fuel in the utilitarian function of a flight (see Chapter 
2.1), as well as its performance regarding another metric (Figure 7). The utilitarian performance of a fuel—
what an airline is likely willing to pay more for—can be predicted by at least the specific energy and energy 
density of a fuel. High-performance fuel refers to any fuel composition, pathway, or effect that has 
advantageous characteristics relative to a conventional fuel and is not limited to strained or novel molecules.  
 
Figure 7. Performance metrics of a fuel can be clumped into nine categories that are dependent on the mission of the flight 
Other nonutilitarian performance benefits could be achieved by increasing the value proposition to some other 
stakeholder. For example, Figure 7 illustrates several other possible performance metrics that a hypothetical 
 
6 The cis and trans forms of decalin can adopt relatively low-strain chair configurations but have different strains relative to C–H interactions. Other ring 
structures could also have very different DCNs.  
7 In the Co-Optimization of Fuels & Engines (Co-Optima) initiative, fuel components are referred to as blendstocks.

Sustainable Aviation Fuel: Review of Technical Pathways 
15 
high-performance fuel could achieve. Costs associated with logistics or handling can conceptually be reduced. 
Alternatively, environmental benefits can be realized with fuels that have low aromatic content. Recent work, 
however, focuses on the direct utilitarian performance metrics with additional discussions of costs. 
Specific energy and energy density improvements have the potential to be used by an aircraft or airline 
immediately. All flights benefit from increases in specific energy, as the flight can achieve the mission at a 
lower total weight and hence reduce fuel burn. On payload-limited flights or flights that are limited in range by 
a maximum weight, high specific energy might enable carrying an additional payload and thus become more 
profitable. Flights that are range-limited by fuel capacity, less common for commercial aircraft but more 
common for business jets, can benefit directly from a fuel that has higher energy densities. The Bioenergy 
Technologies Office (BETO) is sponsoring studies to bound the potential benefits of increasing the range or 
payload.7F
8  
Higher thermal stability benefits may be achieved by using redesigned or adjusted hardware to achieve higher 
efficiency. Thermal stability benefits may result in decreased engine maintenance. These benefits, however, 
will remain unknown and unquantified until a substantial level of experience is accrued with the use of SAFs 
that have high thermal stability and until OEM concurrence of the benefits is obtained.  
To reiterate, while what an airline may be willing to pay can be modeled by others, keep in mind that there is 
low accuracy in such a number. Further, airlines will not pay more for a fuel based on model output and will 
require in-depth flight testing for anything other than modest adjustments to price based on energy content (J. 
Holladay, personal discussions with Alaska Airlines and Airlines for America, October 2018).  
Finally, fuel storage and delivery infrastructure must also be accounted for when considering the full cost of 
the fuel. SAFs today are approved in blends of 10% up to 50% and when blended are fully fungible drop-in 
fuels. Fuels are stored at airports and delivered through a hydrant system. For example, at Los Angeles 
International Airport, SAF blended 30:70 with petroleum is purchased by United Airlines. The fuel is mixed 
with all other jet fuel at the airport and delivered through the hydrant system to all planes. Through an 
accounting system, United Airlines is charged a premium for the fuel and receives “credit” for its use. 
Similarly, any fuel will: (1) need to be a fully fungible and drop-in compatible and (2) be delivered most cost-
effectively through the hydrant system, hence it must be diluted. While the fuel could be stored separately and 
delivered by a fueling truck, this would add cost and time and must be taken into account when considering 
what an airline would be willing to pay for the fuel. Having a fueling truck and a hydrant cart at the same gate 
in a major airport may not be practical because of limitations on fueling time and space. 
2.4 Review of Chapter 2 
Fuel properties needed in SAF must meet three general requirements: (1) performance, (2) operability, and (3) 
drop-in compatibility. These requirements are essential for safety, general usage, and execution of commercial 
and military missions.  
The bulk properties of jet fuel are derived from the hydrocarbon classes that make up the fuel, which include 
n-alkanes, iso-alkanes, cycloalkanes, and aromatics. Aromatics have lower heats of combustion, do not burn 
cleanly—particularly in older hardware—and are responsible for up to 90% of particulate emissions, which in 
turn contribute to wear on combustor liners.  
 
8 Preliminary model output based on a theoretical fuel and for a sample flight route suggests a potential benefit of up to 54 cents per gallon for what could 
be a theoretical maximum of unblended high-energy fuel (44.9 MJ/kg, 37.7 MJ/L) by improving the range of the aircraft. A fuel composed of only 
conventional fuel molecules could be reconfigured to garner an 18-cent-per-gallon benefit (43.6 MJ/kg, 36.1 MJ/L) or, in the case of a fuel partially 
composed of known strained molecules, a 30-cent-per-gallon benefit (44.0 MJ/kg, 36.8 MJ/L).

Sustainable Aviation Fuel: Review of Technical Pathways 
16 
Trace properties derived from impurities and minor components are also critical for fuel performance, 
operability, and drop-in compatibility, and affect the relative cost of jet fuel versus fuels that do not have the 
same criteria. An understanding of trace properties is vital for researchers to consider at the bench scale. 
Rather than mimic petroleum-derived jet fuel, there is an opportunity to produce jet fuel of higher quality 
through focusing chemistry and biology on producing the hydrocarbon classes most desirable for bulk 
properties. An SAF that has a lower aromatic content and higher energy and specific density is one example. 
Current fuel specs allow migration in this direction while maintaining drop-in compatibility.  
Jet fuels are primarily delivered to aircraft through hydrant systems. Hence, SAF fractions today are highly 
diluted with the conventional petroleum fuel and aromatic concentrations in the composite fuel, providing 
adequate swelling character. This means there is little reason for renewable fuels to contain aromatics to ensure 
seal swelling.  
Finally, cost cannot be understated in importance. SAFs with low (or no) aromatics offer greater performance 
attributes in many ways. However, current projected performance increases do not eclipse the increase in costs. 
High-quality SAFs must be near price parity to sell and scale in volume. 
3 Jet Fuel Certification 
Jet engines and airplanes are certified by the Federal Aviation Administration (FAA) to operate on a fuel that 
is specified by ASTM. Any new fuel, therefore, must meet conventional fuel ASTM specifications and be 
approved through the ASTM D4054 process, or it cannot be used in commercial flight. This chapter provides 
details on the ASTM fuel approval process, currently approved pathways, and pathways in the ASTM approval 
pipeline.  
3.1 Getting a Fuel Approved 
ASTM D4054, Standard Practice for Evaluation of New Aviation Turbine Fuels and Fuel Additives, was 
developed to ensure safe and reliable operation of aircraft on alternative aviation fuels (Radich 2015). This 
standard practice comprises a four-tiered process for testing new aviation fuels and fuel additives (Figure 8) 
(Rumizen 2017), with two reports submitted for OEM review and approval:  
• S
pecify the new fuel (Tier 1) 
• E
stablish the “fitness for purpose” (Tier 2) 
• T
est the components and rig operability limits (Tier 3) 
• T
est the aircraft, engine, and associated durability (Tier 4).

Sustainable Aviation Fuel: Review of Technical Pathways 
17 
 
Figure 8. Four-tiered process for testing new aviation fuels and fuel additives, per the ASTM D4054, Standard Practice for 
Evaluation of New Aviation Turbine Fuels and Fuel Additives 
Upon completion of the D4054 tests, the approval process for D7566, Standard Specification for Aviation 
Turbine Fuel Containing Synthesized Hydrocarbons, begins. For this approval process, data developed under 
the D4054 testing protocols enable the ASTM subcommittee to compare SAF properties and characteristics 
relative to conventional fossil-derived fuels. If the SAF is deemed equivalent to conventional jet fuel, then it is 
referred to as a drop-in fuel and the pathway used to develop the fuel can be included under ASTM D7566. A 
provision under D7566 allows any fuel meeting the specifications to be reidentified as a conventional fuel. 
With this inclusion, any SAF can be seamlessly integrated into the fuel delivery infrastructure without the need 
for separate tracking or regulatory approval; in other words, the fuel is fully fungible. The overall process for 
D7566 approval includes the following steps: 
1. Fuel producers draft a Phase 1 research report based on Tier 1 and Tier 2 outcomes 
2. Aircraft engine manufacturers review the draft research report with requirements needed for Tier 3 and 4 
tests 
3. Fuel producers draft a revised Phase 2 research report following Tier 3 and Tier 4 tests 
4. Aircraft engine manufacturers review the draft research report 
5. Fuel producers prepare the final research report incorporating manufacturers’ feedback 
6. The ASTM subcommittee votes on the final Phase 2 research report 
7. The ASTM full committee votes on specification(s) to be added to ASTM D7566. 
The D4054 process is an iterative and rigorous evaluation process that requires candidate fuel producers to 
generate a range of fuel volumes so that their properties, compositions, and performance can be tested. 
Volumes of fuel for the D4054 tests (listed in Table 6) are significant and are required early in the technology 
development stages.

Sustainable Aviation Fuel: Review of Technical Pathways 
18 
Table 6. Approximate Fuel Volumes, Time, and Cost for D4054 Testing (CAAFI 2019) 
Tier 
Approximate Fuel Volume in 
Gallons (Liters) 
Approximate Time in 
Months 
Approximate Cost in U.S. 
Dollars 
Tier 1 – Fuel specification 
properties 10 (40) 6 months $50,000 (testing cost) Tier 2 – Fit-for-purpose 
properties 10–100 (40–400) 
OEM Review  6–12 months $350,000 (OEM cost) 
Tier 3 – Component and rig 
testing 250–10,000 (950–40,000) 24–36 months ~$4 million (testing cost) Tier 4 – Aircraft and engine 
testing Up to 225,000 (850,000) 
OEM Review and Approval  6–12 months ~$1 million (OEM cost) 
While both testing fuel specification properties and fit-for-purpose properties may be provided at no cost to the 
fuel producers, scaling up new technologies for producing the required volumes for Tier 3 and Tier 4 testing is 
a challenge. Moreover, scaling capacity is seen as a requirement for formally entering the process by many 
involved in the approval process.  
Component and rig tests can represent significant costs to the fuel producers dependent on the level of testing, 
but fortunately some of the cost has been borne by the FAA and OEMs. Engine tests that can require even 
larger volumes may be required for the most innovative cases, but the very large fuel volumes have not been 
approached in practice for SAFs. The extent of required testing varies. As OEMs become more comfortable 
with SAF, they have the option to relax the Tier 3 and Tier 4 testing requirements. 
Typically, the certification process takes from 3 to 5 years and costs in excess of $5 million and has been as 
high as $10 to $15 million (Colket et al. 2017). There is a clear need to drive down the certification and 
production costs and reduce the time required for certification. As a multiagency-led program, the NJFCP aims 
to streamline these costs and the fuel and resource requirements to secure ASTM approval of SAFs for 
commercial uses (Colket et al. 2017). 
While there is room to adjust the ASTM specification process, the opportunity to change the fuel specification 
is limited and more about tightening the specification rather than expanding it. Finally, note that no fuels that 
are oxygenated or have heteroatoms, olefins, or metals will be approved, as they have deleterious properties 
associated with jet fuel.  
3.2 A Fast Track to ASTM Approval 
In January 2020, ASTM approved a Fast Track Annex to D4054 (Figure 9) that meets the strict compositional 
and performance requirements of conventional jet fuel and which limits the blend level to a maximum of 10% 
with Jet A or Jet A-1.  
Composition requirements include limits on the types of hydrocarbons in the blend. The cycloparaffin 
concentration must be less than 30 wt%, and the aromatic composition less than 20 wt%. Furthermore, tetralins 
and indans must have a composition less than 6 wt% (or less than 30 wt% of the aromatics). Metals and 
organic heteroatoms (S, N, and O) must be limited to trace amounts. The blend must have a well-distributed 
carbon range with a distillation point distribution having the slope of typical jet fuel. The blend must meet 
strict thermal stability standards.

Sustainable Aviation Fuel: Review of Technical Pathways 
19 
 
Figure 9. ASTM-D4054 Fast Track Annex for qualification and approval of new aviation fuels that meet the compositional 
and performance standards with a limit of 10% blend (highlighted portion differs compared to Figure 8) 
 
3.3 Currently Approved and Emerging Fuels 
Synthetic paraffinic kerosene (SPK) consisting of n- and iso-alkanes constituted the first alternative fuels 
approved and they came from four sources: synthesis gas (syngas), lipids (fats, oils, greases), sugars, and 
alcohols. While there are differences in the carbon chain length and level of branching, OEMs have become 
comfortable with SPK in jet fuel. More recently, SAF fuels are expanding beyond n- and iso-alkanes. Annexes 
with the addition of aromatics and cycloalkanes have been approved. Nevertheless, to date, no alternative fuel 
is approved at larger than 50% blending with conventional fuel.  
As of January 2019, six fuels are approved as annexes to ASTM D7566 (Figure 10): 
• Annex A1 (Fischer-Tropsch [FT]-SPK) was approved in June 2009 for up to a 50% blend with 
petroleum-derived jet fuel. FT-SPK is a mixture of iso- and n-alkanes derived from synthesis gas using 
the FT process. Syngas can be produced from reforming natural gas or from gasifying coal or biomass.  
• Annex A2 (HEFA-SPK) was approved in July 2011 for up to a 50% blend with petroleum-derived jet 
fuel. The molecular composition of HEFA-SPK is similar to FT-SPK, consisting of iso- and n-alkanes. 
The alkanes are the product of hydrotreating esters and fatty acids from fats, oils, and greases and from 
oilseed crops or algae.  
• Annex A3 (SIP, hydroprocessed fermented sugar-synthetic iso-parafﬁns) was approved in June 2014 for 
up to a 10% blend with petroleum-derived jet fuel. Unlike SPK from HEFA or FT, this is a single 
molecule, a 15-carbon hydrotreated sesquiterpene called farnesane, produced from fermentation of 
sugars. Today, the fermentation is done commercially from sugar cane juice and is used in higher-value 
applications, most commonly in personal care.  
• Annex A5 (alcohol-to-jet [ATJ]-SPK) was approved in April 2016 for SPK from iso-butanol (30% blend 
with petroleum) and expanded in April 2018 for SPK from ethanol and for fuel blends up to 50% with 
petroleum. ATJ-SPK consists of iso-alkanes of 8, 12, or 16 carbons when starting from iso-butanol. The 
iso-alkanes are highly branched and have lower DCNs than FT or HEFA, based on data from Gevo, Inc.

Sustainable Aviation Fuel: Review of Technical Pathways 
20 
The carbon number is broadened and the branching level can be significantly reduced, leading to a DCN 
similar to FT and HEFA when starting from ethanol.8F
9  
• Annex A6 (Applied Research Associates Catalytic Hydrothermolysis Jet, or ARA CHJ) was approved in 
January 2020 as a 50% blend. The fuel is produced from lipids using a supercritical hydrothermal 
process, creating a blendstock that contains all four hydrocarbon families: n-, iso-, and cyclo-alkanes and 
aromatics. 
• Annex A7 (HC-HEFA) synthesized paraffinic kerosene from hydroprocessed hydrocarbons, esters, and 
fatty acids was approved in 2020 as a 10% blend. This is specifically for lipids from an B. braunii algae 
that have been hydrocracking/hydroisomerization to remove all oxygen and saturate double bonds. The 
product is rich in iso-alkanes. This is the first approval through the fast track process. 
• ASTM D1655-20b allows coprocessing of up to 5% mono-, di-, and triglycerides, free fatty acids, and 
fatty acid esters or up to 5% of FT hydrocarbons. Hydrocracking/hydrotreating and fractionation are 
required. No other coprocessing in refineries is allowed for jet fuel.  
Several fuels are somewhere in the D4054 approval pipeline (Figure 10). These fuels include SPK (n- and iso-
alkanes), cycloalkanes, aromatics, and mixtures of the four hydrocarbon families. Figure 10 shows the state as 
of July 2020, with some companies in exploratory discussions (Global BioEnergies, POET, SBI BioEnergies, 
Vertimas and GSR/GTI); some companies in Phase 1 (Shell, Byogy, Swedish Biofuels), Phase 1 review 
(Neste, for green diesel), or Phase 2 (Virent, for aromatics). 
Figure 10. SAF pathways approved under ASTM D7566 and emerging fuel pathways in the ASTM D4054 approval process 
 
3.4 Summary of Current SAFs  
Figure 11 provides a graphical illustration of the four families of hydrocarbons in jet fuel and a summary of the 
properties imparted by each hydrocarbon class.  
 
9 Pacific Northwest National Laboratory internal data; see also alcohol-to-jet ASTM report, https://www.astm.org/Standards/D7566.htm.

Sustainable Aviation Fuel: Review of Technical Pathways 
21 
Since the first alternative jet fuel was approved in 2009, five additional fuels have been approved. The initial 
fuels were SPK blends. Later approvals included SPK in which aromatics and cycloalkanes were added or 
present. The starting feedstocks are synthesis gas; fats, oils, and greases; sugar; and alcohols. The carbon chain 
length and level of branching can vary dramatically, and hence the amount of the SAF fuel allowed in the 
blend with petroleum-derived jet fuel varies from 10% (farnesane) to 50%. Fuels that will be approved under 
Fast-Track will be limited to a maximum of 10% blends.  
An SAF consisting primarily of cycloalkanes (Shell’s IH2) without substantial amounts of acyclic alkanes or 
aromatics is now in the system at Tier 1.  
 
Figure 11. Summary of four classes of hydrocarbons 
 
There is not a physics-based limitation to the 50% blend requirement of broad boiling range fuels and the 
restrictions on blend level could be increased in the future, even for SPK fuels. With the low amount of SAF 
produced today there is not a driving force to increase fuel blend levels at this time.  
When blended with petroleum, the SAF-approved fuels are considered fully fungible (up to the 50% limit) as a 
D1655-approved fuel. Hence, approved fuels with SAF are not treated differently than current fuels from 
petroleum and can use airport fuel storage and hydrant systems, saving money on infrastructure costs. 
 
4 Workshop Learnings 
To move the nascent jet fuel industry from 25 million gallons to 2.5 billion gallons, and ultimately to 25 billion 
gallons, BETO has sponsored or cosponsored three workshops. This chapter distills the key learnings from 
each workshop, and more detailed summaries of the workshops are provided in Appendix 3.  
Participants along the entire value chain were invited to the workshops. These included: 
• Airframe manufacturers

Sustainable Aviation Fuel: Review of Technical Pathways 
22 
• E ngine manufacturers 
• F
eedstock producers 
• B
iorefiners 
• P
etroleum refiners 
• A
viation fuel distributors 
• A
irports 
• F
uel certifiers quality assurance/quality control  
• A
irlines 
• R
egulatory agencies (FAA, Environmental Protection Agency) 
• N
ongovernmental organizations. 
T
his broad spectrum of participants was invited because innovators require broad stakeholder buy-in, viable 
technology solutions, and consistent government support in order to move forward. A fuel change in a 
complex market such as commercial aviation fuels must have each sector represented and ideally have each 
sector see new opportunities, receive financial benefit, or at least mitigate loss. Further analysis identifying the 
value proposition and needs of each stakeholder is warranted and outside the scope of this report.  
4.1 Alternative Aviation Fuel Workshop 
BETO’s Advanced Development and Optimization Program held the Alternative Aviation Fuel Workshop on 
September 14–15, 2016. The purpose of the workshop was to engage stakeholders to gain additional 
knowledge related to aviation biofuels production. Input was sought specifically for the effort needed to: (1) 
develop technology for scalable production, (2) achieve economic competitiveness, (3) achieve environmental 
benefits, and (4) develop feedstock and supply chains for biojet fuel deployment. Key takeaways are listed 
below: 
Timeline 
• F
or 0–5 years, the near-term research and development (R&D) investment needs to reduce the cost in 
pathways already approved or near certification. 
Ma
rkets  
• J
et fuel properties fall within the light end of the diesel envelope and hence biofuels companies could 
sell to either market.  
• D
iesel fuel (ground transportation) is a significant competitor for lipids, including fats, oils, and greases. 
Light ends could offer a blending opportunity to meet bulk properties.  
• L
ipid routes are not likely to meet the SAF volume demand.  
• P
olicy and offtake agreements are necessary but are not sufficient criteria; biofuel costs must come 
down. Today, several offtake agreements are in place but are not being met.  
R
esearch Opportunities

Sustainable Aviation Fuel: Review of Technical Pathways 
23 
• T he low sulfur and low aromatic content in approved SPK SAFs should be considered when calculating 
additional benefits for SAFs. 
• Ne
w low-cost sources of feedstocks are needed to increase scale, including lignocellulosics. 
• T
echno-economic analysis (TEA) and GHG results need improved consistency and need to cover 
pioneer plants. Additionally, TEA should focus on identifying where cost reduction is most significant. 
4.2 JET Workshop 
The JET Workshop, held at the National Aeronautics and Space Administration (NASA) Glenn Research 
Center in Cleveland, Ohio, on September 21 and 22, 2017, was a perspective-gathering brainstorming event 
organized around four themes:  
Theme 1: H
igh-Performance Fuel Options 
Theme 2: E
ngine and Combustor Options 
Theme 3: A
ircraft On-Board High-Performance Fuel Considerations 
Theme 4: H
igh-Performance Fuel Development to Deployment Considerations.  
D
OE’s Office of Energy Efficiency and Renewable Energy (EERE), the U.S. Department of Defense, and 
NASA organized the event. In-person attendance was 75, with another 25 participating by webinar.  
High-performance SAF offers tremendous opportunity, but it will take time and money and can only be 
accomplished by understanding the critical fuel properties required and their impact. Notionally, fuels can 
make air transportation safer and more efficient, produce fewer emissions—of importance to both human 
health and global climate change—and increase aircraft performance. 
The matriculation of quantifying these benefits via research will take investment and time, with many federal 
agency strengths leveraged to fully capture these potential benefits. The optimum realization of these benefits 
will take time, money, and, perhaps most importantly, coordination.  
It was noted from an OEM that it takes 14–19 years for technology development for planes, engines, and fuels 
to progress through product introduction phases; hence, it is necessary to identify how these can work together. 
General Electric spent over $500 million to get GEnx-09 from development into production (an expensive and 
resource-intensive process); fuel production facilities have a similar price tag. The risk of developing a new 
engine on a fuel that is not commercial is too high. 
While there is little expectation for engine design to change radically, there is an expectation for reduced 
emissions. Therefore, the biofuel community can focus on improving fuel properties on engines used today 
and on providing fuels that have lower emissions. Opportunities exist to improve specific fuel consumption 
(increase payload, increase range, or reduce takeoff weight) using high-energy-content fuels with existing 
engines.  
4.3 Trilateral Canada–Mexico–U.S. Biojet Workshop 
The Trilateral Biojet Workshop, held in Richland, Washington, in May 2018 brought together researchers from 
Canada, Mexico, and the United States. The workshop was organized by EnerCan, SENER, and DOE, and was 
funded by DOE and Pacific Northwest National Laboratory (PNNL). The workshop covered the value chain, 
feedstock from each country in North America, research directions in each country, and how they can work 
together to accelerate SAF growth. 
Key takeaway messages included:

Sustainable Aviation Fuel: Review of Technical Pathways 
24 
• T he time and cost of bringing a new fuel to market must account for the fuel certification time ( 4 years) 
and cost through piloting to pioneer plants. 
• T
he airlines cannot meet their self-imposed targets for reducing GHG emissions based on engine and 
flight improvements alone; they need SAFs. Fuel cost is a significant fraction of operating cost.  
• S
ome airports are looking at opportunities to help make up the difference between the cost to make the 
fuel and the price of the fuel. One option for airports is to become fuel integrators by combining more 
substantial long-term purchase agreements (from the airport level) and by providing land for producing 
biofuels. Europe has similar models that could be followed (e.g., the Oslo model, which creates a central 
fund to bridge the delta on the cost of production and market value). 
• F
uels are delivered in hydrant systems in which life cycle analysis (LCA) accounting is attributed to 
those who pay for them. Refineries ask if similar accounting could be done for coprocessing even if jet 
fuel is not a product. (How does one draw the box around the LCA?) 
• F
eedstock cost must be reduced. 
• P
roducers need to maximize value of each process stream, which includes producing higher-value 
coproducts that match the scale of the process stream.  
• Ma
rkets span international boundaries and coordination needs to span countries. 
No
te that fuel prices paid by the airlines versus corporate and other “small” customers may be substantially 
different. Jet A may sell from between $3.37 and $5.05 per gallon (AirNav 2018). Prices at some major 
airports are even higher. The corporate jet fuel market is substantial in size and is a focus of early adoption for 
some SAF producers.

Sustainable Aviation Fuel: Review of Technical Pathways 
25 
Part II – Analysis and Insights

Sustainable Aviation Fuel: Review of Technical Pathways 
26 
5 R&D – Fuel Molecules 
This chapter provides a high-level analysis of research opportunities. The purpose of the analysis is to identify 
research efforts that would accelerate SAF development and to note ties between programs supported by DOE, 
FAA, the U.S. Department of Defense, and the U.S. Department of Agriculture (USDA).  
5.1 Vision: Reduce Aromatic Content and Increase iso-Alkanes and Cycloalkanes 
Jet fuel consists of four hydrocarbon families: n-alkanes, iso-alkanes, cycloalkanes, and aromatics. The 
presence of other molecular families, including olefins and heteroatoms, are limited to trace quantities.  
High energy content is valued in jet fuel, just as octane is for gasoline and cetane is for diesel. Blending 
cycloalkanes and iso-alkanes can give fuel higher energy content than Jet A fuel while meeting the density 
specification required by ASTM (Kosir et al. 2019).  
Figure 12 shows the relationship of each hydrocarbon class to energy content, including energy density (MJ/L) 
and specific energy (MJ/kg). The average composition of Jet A contains aromatics, shown in yellow; 
cycloalkanes, shown in brown (monocyclic) and pink (bicyclic); n-alkanes, shown in orange; and iso-alkanes, 
shown in green. As a mixture, the resultant energy density and specific energy is shown in red (the red 
hexagon is the average energy density and specific energy for Jet A). As a note, there are small amounts of 
multicyclic aromatics in a jet fuel composition, which are not illustrated here. 
 
Figure 12. Energy density and specific energy of various hydrocarbons 
Aromatics are more difficult to burn cleanly and the soot produced has implications for the environment, 
human health, and combustor life. Because fuels are delivered in hydrant systems, there is little reason to have 
a strategic focus on producing aromatics at a time when SAF is made in low amounts. Further, our long-term 
goal is to reduce and perhaps rid jet fuel of aromatics. Boeing has tested aromatic-free HEFA fuels in modern

Sustainable Aviation Fuel: Review of Technical Pathways 
27 
planes without issue. Moreover, the lower specific energy of aromatics makes them disadvantageous for 
mission performance. Hence, there are many reasons to avoid aromatic production.9F
10  
n-Alkanes have poor jet fuel characteristics. No n-alkane meets all D1655 specifications—larger n-alkanes 
have high freeze points and smaller n-alkanes do not meet the flash point. While they are an acceptable 
blending source as they are readily available in fatty acids and esters, as a class they do not offer a unique 
performance proposition and are not required in SAF. SAF and renewable diesel produced today are rich in n-
alkanes, as they are sourced from lipids.  
From a bulk-property perspective, jet fuel only requires iso-alkanes and cycloalkanes to meet ASTM D1655 
specifications. A jet fuel containing cycloalkanes (mono- and dicyclic) and iso-alkanes could increase energy 
density and specific energy; meet freeze point, flash point, and O-ring swelling demands; and burn much 
cleaner (Kosir 2019). Improvements to the specific energy result in a weight reduction for a flight, which for 
long ranges enables more passengers and cargo. Ninety-eight percent of flights do not operate with a payload 
range restriction; hence the weight savings would correlate to a modest fuel weight reduction. BETO has 
current work that seeks to understand the possible impact of fuel weight savings.  
Keeping a strategic focus on these iso-alkanes and cycloalkanes will help define research. While aromatics or 
n-alkanes as parts of a complex mix are acceptable, the authors would like researchers to understand the issues 
with aromatic production.10F
11  
Finally, jet fuel specifications restrict trace components—including ash, metals, and other inorganic and 
organic impurities—to very low levels. Understanding the cleanliness specification for jet fuel is essential in 
considering separation requirements coupled to conversion processes.  
The possible reduction in aromatic content and increased iso-alkanes and cycloalkanes is shown graphically in 
Figure 13. iso-Alkanes are desirable, though they are still too expensive, and R&D focus needs to be on 
continuing to reduce their cost of production. Note that light branching provides a DCN that is in line with jet 
fuel today and volatility properties desirable for engine relight. Further, the higher DCN allows the iso-alkanes 
to be sold into diesel markets, which allows flexibility to biorefineries. Heavily branched mixtures have a low 
DCN, although DCN is not part of the ASTM specification. The low-temperature fluidity of n-alkanes is 
illustrated. Note the difference that a single methyl substitution makes on improving freezing point: for C10, 
the single methyl branching reduces freezing point by 42°C, and for C14, the freezing point reduction is 21°C. 
Jet fuel today contains alkyl cyclohexane molecules, which have excellent properties. There are many 
additional cycloalkane molecules that could be used in jet fuel; however, more research is required as some 
cycloalkanes may have flaws related to freeze point or cost of production. Research goals include both 
deriving more information on combustion and molecular properties and reducing cost. Aromatics have the 
least desirable combustion character and hence are capped at 25% in jet fuel. Multi-ring aromatics are capped 
at 3%. Research is needed to determine the minimum aromatic content required for backward compatibility 
with older fuel systems regarding seal swelling. Early data suggest that if jet fuel contains aromatics, small, 
lightly substituted C8–C9 aromatics will have the least impact on soot formation while providing the seal 
swelling for backward compatibility. Fused-ring cycloalkanes may offer similar seal swelling, offer even 
higher energy density, and burn cleaner than aromatics. The question of aromatics versus cycloalkanes 
becomes one of cost, compatibility, and combustion character. 
 
10 The authors are not suggesting ceasing research on renewable aromatics altogether, as not all aromatics have the same soot-forming propensity, nor is 
there a clear understanding of the minimum aromatic content required for seal swelling in older aircraft. Nevertheless, aromatics are easy to produce due to 
their thermodynamic stability and are a common product in thermochemical streams, including those from lignin. A question remains on the cost–benefit 
analysis of converting aromatics to cycloalkanes. We are stating that separate R&D on producing aromatics for SAF does not require funding by DOE, as 
technology is sufficiently available and practiced, whereas producing cycloalkanes with low hydrogen demand remains a challenge. 
11 Further things for researchers to understand on aromatic production include: (1) aromatics are readily produced, requiring only temperature and an acid 
catalyst from any number of feedstocks, (2) there is sufficient aromatic content in petroleum jet fuel, and (3) seal-swelling properties may be derived from 
cycloparaffins, which offer better combustion behavior.

Sustainable Aviation Fuel: Review of Technical Pathways 
28 
 
Figure 13. Strategic focus on iso-alkanes and cycloalkanes 
Based on the previous analysis, the following conclusions are offered: 
• R
educing aromatic content (by adding high-quality iso-alkanes) – near-term benefit 
• R
eplacing aromatics with cycloalkanes – medium-term benefit 
• I
ncreasing specific energy by blending new fuel molecules – long-term benefit. 
I
n the near term, SAF will be a small component of Jet A. The addition of high-quality iso-alkanes improves 
the quality of the fuel. Little value is provided by increasing the aromatic content over what is in jet fuel today. 
Over time, as SAF volume grows in the market, the aromatic content can be reduced by increasing the 
cycloalkane content. In the long term, as SAF dominates the market, fuels with higher energy content than is 
available today can be produced and, to meet Carbon Offsetting and Reduction Scheme for International 
Aviation (CORSIA) targets, there may be blending of SAF blending components. The D7566 is written to 
allow blending of different SAFs to meet fuel specifications, which could entail mixing SPK with aromatics. 
The caveats to this strategy are stated previously, requiring further understanding of cost, compatibility, and 
combustion behavior of cyclic hydrocarbons versus aromatics in SAF fuels.  
5.2 High-Quality iso-Alkanes 
Today there are four ASTM-approved SAFs based on iso-alkanes (Figure 14). The fuels are prepared by (1) 
cracking and isomerizing larger alkanes derived from lipids or FT liquids, (2) building up small molecules 
(alkenes) to the jet range, or (3) fermenting sugar into molecules that are in (or near) the jet range. Each 
method is presented in more detail in Figure 14.

Sustainable Aviation Fuel: Review of Technical Pathways 
29 
 
Figure 14. iso-Alkane production by cracking and isomerizing large molecules, building up small molecules, or fermentation 
5.2.1 Crack Large Molecules  
Cleaving larger molecules into smaller molecules is required with lipids and FT liquids, and for converting 
diesel or heavies into jet-range molecules. Most processes that “crack” have low specificity; hence diesel-range 
molecules and heavy oils are converted into both jet fuel and light naphtha. The naphtha is a lower value than 
the diesel or jet fraction. Hydrocracking is commonly used to crack and is part of HEFA and FT processes. 
HEFA employs hydrogen to remove oxygen and to crack and isomerize the n-alkanes into jet-range iso-
alkanes.  
Today, lipids are the primary source for biodiesel, renewable diesel, and renewable jet fuel, accounting for 2.2 
billion gallons of U.S. renewable fuel production and 2.6 billion gallons of U.S. renewable fuel use (U.S. EPA 
2019). Lipid sources are shown in Figure 15. Lipids are coproduced in protein crops, and as the demand for 
plant protein increases, the lipids will need to be utilized. No one source of feedstock will be sufficient to 
satisfy SAF demand.

Sustainable Aviation Fuel: Review of Technical Pathways 
30 
 
Figure 15. Lipid sources for HEFA, including waste sources and crops 
FOG = fats, oils, greases 
Increasing the availability of low-cost oilseed crops will be required for lipid-sourced SAF. USDA is 
supporting new crops, including carinata, which is rich in C22:1 fatty acids. Companies are working on 
commercial production of carinata. Further out, BETO is supporting research to decrease the cost of algae, 
which today is too expensive for fuels. In Japan, the IHI Corporation recently entered its algae oil into the 
ASTM approval process. IHI produces an algal oil rich in C30 that has six unsaturation units.  
Conversion technologies for lipids include: 
• HEFA, hydrotreating to remove oxygen in carboxylic acid moieties, saturating double bonds, and 
hydrocracking/isomerization of the resultant n-alkanes. HEFA is commercially practiced, providing both 
renewable diesel and renewable jet fuel today. HEFA produces n- and iso-alkanes. 
• Hydrothermolysis, a form of hydrothermal liquefaction (HTL) using supercritical water followed by 
hydrotreating to produce n- and iso-alkanes as well as aromatics and cycloalkanes. Plans for the first 
facility have been announced. 
Potential new conversion technologies include: 
• HTL followed by hydrotreating of various lipid-containing feedstocks, including wastewater sludge and 
manures, which produce n-alkanes and cyclics.11F
12  
 
12 Hydrothermal liquefaction in which the jet and diesel fractions have been characterized and the diesel fraction tested in engines is performed at PNNL 
and supported by BETO funding.

Sustainable Aviation Fuel: Review of Technical Pathways 
31 
• M etathesis, a process that exchanges two double bonds through scission and recombination, is a means 
of reacting unsaturated esters with ethylene and hence of controlling the scission. Applying the ethylene 
metathesis to carinata oil, which is rich in C22:1 fatty acids, would produce two C11 compounds: an 11-
carbon fatty acid triglyceride and an 11-carbon alkene. The alkene could be distilled and saturated for jet 
fuel blending and the fatty acid could be esterified (or transesterified) for diesel markets. This would 
reduce the hydrogen demand of HEFA. 
• C
atalytic, thermocatalytic, and thermal deoxygenation processes of Shell/SBI, Aduro, and Forge, 
respectively. 
I
n summary, today large molecules are cracked to smaller molecules via hydrocracking to make fuels. The 
hydrogen gas demand is significant and is based on the number of ester/acid, olefin, and alcohol functional 
groups, as well as the amount of cracking required. The chemistry is used in HEFA and FT processes. 
Supercritical water hydrothermolysis provides another means of breaking down larger molecules to produce a 
broad range of hydrocarbons after hydrotreating. The hydrogen demand is still substantial. Other chemistries 
also could be applied. A challenge associated with cracking larger molecules is the loss of carbon to low-value 
naphtha.  
5.2.2 Build Up Small Molecules 
Nature excels at producing small alcohols. Through fermentation and hydrodeoxygenation, other small 
molecules—including olefins, carboxylic acids, and mixtures of oxygenates—are possible. Catalysis can be 
used to build up small molecules to the jet range with good selectivity. In the ATJ process, alkenes are 
oligomerized from C8 to C16 molecules. The key is controlling the growth regarding carbon length and carbon 
backbone (i.e., carbon length, branching level, and degree of cyclization/aromatization).  
Cost Drivers 
The cost of the alcohol feedstock is a critical driver. Sourcing the alcohol from high-cost sugars (e.g., biomass) 
is not feasible. Reports suggest that a $0.01 increase in sugar cost results in a $0.20 increase in fuel cost 
(Gruber 2018). Sourcing the alcohols from waste streams can drive down cost. Inexpensive sugars are likewise 
needed for other small molecules. 
Sourcing carbon from low-cost waste gases can change the paradigm. There are enough waste gases (carbon 
monoxide [CO]-rich streams) to produce 32 billion gallons of SAF globally from steel mills and refineries, and 
another 18 billion gallons from unsorted municipal solid waste (MSW) gasification. When added to the 360 
billion gallons of SAF available from agriculture residues via gasification, the amount exceeds global jet fuel 
demand (Holmgren 2019). 
Chemistry 
Several chemistries for building up small molecules to jet-range mixtures are supported by BETO, the Office 
of Basic Energy Sciences, and USDA: 
• A
lkene oligomerization (the underlying chemistry for ATJ) 
• P
rins condensation (reaction of alkene and aldehyde)  
• A
ldol condensation (reaction of two aldehydes) 
• K
etonization (reaction of two carboxylic acids) 
• G
uebert chemistry (reaction of two alcohols).

Sustainable Aviation Fuel: Review of Technical Pathways 
32 
From these five reaction families, all the various functional groups obtained from renewable sources can be 
oligomerized to larger compounds. Precursors include carboxylic acids from mixed anaerobes, furfural and 
other aldehydes, and olefins from dehydration of alcohols or isoprene. There are important research 
opportunities to reduce cost. At the same time, support for moving the current ASTM-approved processes 
through pilot and demonstration is critical. The value proposition for converting low-cost small molecules is 
high and can meet fuel demands in jet markets with feedstocks available today.  
5.2.3 Direct Fermentation 
Farnesane is approved for 10% blend in SAF. Many other compounds—isoprenoids, fatty acids, and 
polyketides—can also be sourced from sugars via fermentation.  
In 2015, Amyris stated the production cost of farnesene is $1.75 per liter (from cane sugar), not a price that 
supports fuel production, and this is before hydrotreating (Amyris 2015). While there are opportunities to 
increase value propositions of biorefineries with coproducts, research that focuses on reducing cost remains 
critical. 
Additional challenges include: 
• H
igh hydrogen demand of farnesene, which requires four moles of hydrogen to saturate the molecule, 
nearly the hydrogen demand for HEFA. Other isoprenoids, fatty acids, and polyketides likewise require 
hydrogen.  
• S
ingle molecules will have limits on how much they can be blended, mainly when they are on the 
extreme of carbon number distribution, as sesquiterpenes are (C15). 
• H
ydrolysates (sugars) will need to be clarified because lignin can act like active carbon, resulting in the 
product agglomerating onto the lignin.  
T
he upshot is that available fermentation routes produce large molecules. Theoretical fermentation yields of 
large molecules are about half the efficiency of the theoretical yield of ethanol. Weight loss of oxygen from 
ethanol is offset by fermentation efficiency. The challenges then are addressing the competition for the product 
in high-value applications versus additional processing to make fuels and achieving titer, yields, and rates 
needed that can match the rates of ethanol.  
There may be new ways to approach large molecules by combining biotechnology with thermochemistry that 
can reduce separations and increase the diversity of fuel products and total yield. A recent publication explores 
the concept of producing lipids via fermentation (Collett et al. 2019). In one example supported by BETO, a 
fermentation broth containing a fatty acid is partially concentrated to approximately 20% solids and 
hydrothermally converted to biocrude oil. In such an approach, separations are reduced, the need to reach a 
high titer is relaxed, and biomass growth is acceptable because it is converted to biocrude oil, as are all the 
other residues. The biocrude oil is washed and converted to jet and diesel fuel (Collett et al. 2019). 
5.2.4 Summary 
There are opportunities to reduce costs in iso-alkane production. Low-cost lipid availability will need to be 
addressed and USDA has current programs doing so. Diesel is the primary competitor in lipid routes; policy 
drivers that do not favor one fuel over another are essential. It is critical to control the jet/diesel mix while 
minimizing the production of lower-value naphtha. Controlling the level of branching is also important. 
Cracking large molecules is one general route. HEFA (e.g., hydrotreating) is done commercially; however, 
there may be some other chemistries, such as metathesis, that may be useful for large olefinic molecules, 
mainly C22:11-rich lipids such as are prevalent in carinata oil.

Sustainable Aviation Fuel: Review of Technical Pathways 
33 
Five chemistries have been identified to oligomerize small molecules with common functional groups from 
biomass to larger molecules. Low-cost, sustainable sugar sources are needed. There are also opportunities to 
source the carbon from non-sugar sources, and efficient technologies that can use waste streams with minimal 
cleanup provide a means to reduce feedstock cost. 
There are business reasons to convert alcohols to jet fuel (Brooks et al. 2016). Fermentation routes can directly 
produce larger molecules and the theoretical efficiency is offset by the weight loss of oxygen in dehydration. 
Hence, the choice is dictated by the lowest-cost fermentation.  
Hydrogen demand is required for all routes (hydrocracking large molecules, building up small molecules, or 
saturating direct fermentation molecules). The lowest hydrogen demand is for ATJ (one mole), which is four 
times less than the demand to saturate farnesene and significantly lower than the demand to hydrotreat and 
hydrocrack lipids.  
5.3 Alkylcycloalkanes, Six-Carbon Rings 
Alkyl-substituted cyclohexanes can be produced through multiple pathways and from various biomass-derived 
materials. Such cyclohexane derivatives are within the specification range of conventional fuels, already 
present in Jet A fuel in large concentrations by as much as 30% by weight, and many of the molecules in the 
cyclohexane family can be blended at high concentrations with conventional Jet A fuel without sacrificing 
energy density (Kosir et al. 2019).  
The combustion properties of cyclohexane and decalin (two fused cyclohexane rings) are not as good as iso-
alkanes in terms of soot formation, but are much better than aromatics (Table 7). Jet A fuel contains 
approximately 20% alkyl cyclohexane derivatives. 
Table 7. The Sooting Propensity of Various Hydrocarbons (Yang, Boehman, and Santoro 2017; Olson, Pickens, and Gill 
1985) 
Compound Formula Molecular Weight (g/mol) Boiling Point (°C) ρ (g/cm3) Threshold Sooting Index 
n-Dodecane C12H26 170 216.3 0.7487 5.1 
Cyclohexane C6H12 84 81 0.779 3.5 
Decalin C10H18 138 155.5 0.8965 15 
n-Butylbenzene C10H14 134 183.3 0.8601 62 
Naphthalene C10H8 128 217.9 1.0253 100 
Alkylcyclohexanes are a natural class of cycloalkanes to consider from biomass. They can be accessed through 
hydrotreating aromatic and phenolic compounds (Figure 16). Lignin provides a rich source of phenolics, as do 
bio-oils and biocrudes. Aromatics can be produced from catalytic processing of pyrolysis vapors, mixtures of 
oxygenated compounds, or simple alcohols.

Sustainable Aviation Fuel: Review of Technical Pathways 
34 
 
Figure 16. Routes to cyclohexanes that can be synthesized in the jet-fuel range 
5.3.1 Zeolite-Catalyzed Aromatization Followed by Hydrotreating 
Oxygenated compounds can be deoxygenated and aromatized using zeolite-type catalysts. The oxygenates can 
be simple, such as methanol or ethanol, or complex, such as mixtures of alcohols, carbonyls, and carboxylic 
acids. Two example sources of complex oxygenate streams are the hydrodeoxygenation of sugars (as 
developed by Virent) and pyrolysis vapors. Industrially, zeolite aromatization of oxygenates is established, as 
the chemistries are all variations of methanol-to-gasoline chemistry. There is a third example in the ASTM 
approval queue being piloted by Shell (IH2): hydropyrolysis, which is a catalytic pyrolysis process 
incorporating hydrogen gas. The product mixture from the hydropyrolysis reactor is fractionated (distillation) 
and the aromatics are hydrotreated.  
For purposes of simplicity, three challenges in zeolite-based chemistries are highlighted: 
• L
oss of carbon to coke: Coking occurs in all zeolite reactions; the challenge appears to be greater as the 
oxygenate mixture becomes more complicated from simple alcohols to mixtures that have diols, 
carbonyls, and carboxylic acids.  
• C
atalyst stability: Steam formed during the reaction can damage the structure of the zeolite, an 
aluminosilicate. Research is ongoing in industry and the Office of Basic Energy Sciences in stabilizing 
zeolites to hydrothermal conditions.  
• G
asoline versus jet range: Aromatization chemistry often favors gasoline range. Alkylation chemistry 
(reactions of aromatics and alcohols) can increase the content in the jet-fuel range.

Sustainable Aviation Fuel: Review of Technical Pathways 
35 
In general, converting aromatics to cyclohexanes will require three moles of hydrogen gas. While the product 
mixture will vary, an example from a patented ethanol-to-cyclic process at PNNL has a composition of n-
alkanes (0.3%), iso-alkanes (6%), monocycloalkanes (75%–85%), dicycloalkanes (6%–16%), and alkyl 
aromatics (2%–3%).12F
13  
5.3.2 Phenol Hydrogenation 
Phenols are the building blocks of lignin and hence are produced by deconstructing lignin. Native lignin, after 
separation from carbohydrates, can be cleaved through hydrocracking and similar means to make complex 
phenol mixtures. Various pyrolysis techniques also produce phenol-rich streams. Examples include fast 
pyrolysis; catalytic pyrolysis, which depending on the catalyst and conditions may produce mixtures of 
aromatics and phenols; and liquefaction, which produces mixtures of phenol and aromatics. Phenols can also 
be produced by fermentation. 
Hydrotreating is well-established chemistry; however, not all phenol mixtures are thermally stable. Fast 
pyrolysis oil, for example, has low stability, whereas bio-oils from a catalytic process using inexpensive 
(throwaway) catalysts such as “red mud” and other bifunctional catalysts engineered for robustness13F
14 and 
product streams from HTL are more stable.  
Challenges to phenol hydrogenation include: 
• E
xcess hydrogen use: In the complex streams that contain small oxygenated species, hydrogen is 
consumed, thereby removing oxygen from molecules that form water and light gases of little value. This 
significantly increases cost. Removing light oxygenates before hydrotreating improves hydrogen 
utilization. This is done naturally in some liquefaction processes; the hydrogen demand for HTL 
biocrude is half that of bio-oil from fast pyrolysis, and hydrogen demand for upgrading some catalytic 
pyrolysis oils is also much lower, and the small organics can be treated in subsequent operations.  
• P
yrolytic techniques favor products in the gasoline range: Dearomatizing gasoline is a worthy goal, but 
the gasoline-range cyclohexanes do not meet the necessary octane requirement. Hence, fractionation of 
gasoline- and jet-range material is needed. Shell fractionates IH2 liquids before hydrotreating, thereby 
only hydrotreating fractions that require low aromaticity. Low-cost fractionations are a potential area of 
research. A second area of research is an alkylation step that reacts low-molecular-weight oxygenates 
with phenols to increase both carbon yield and extend more of the mixture into the jet- and diesel-fuel 
ranges.  
• L
ignin will need to be non-recalcitrant if it is to be a feedstock for jet fuel: Pretreatment technologies 
will need to leave lignin in the most native form but also provide sugars in a highly usable form.  
P
henols require four moles of hydrogen to produce cycloalkanes, one mole to remove oxygen, and three moles 
to saturate the ring. Lignin species that have more than one oxygen on either the ring or the chain will require 
additional hydrogen. 
One example of possible fuel composition comes from work between PNNL and CanMET energy—part of the 
Canadian government’s Green Aviation Research and Development Network project—showing jet-range 
hydrocarbon of alkanes (6%), iso-alkanes (5%), monocycloalkanes (40%), dicycloalkanes (20%), 
polycycloalkanes (4%), alkylbenzenes (7%), tetralins/indanes (12%), and phenols (6%). Additional 
hydrotreating would be required to reduce the phenols to zero and would also reduce the aromatics to meager 
 
13 Data from PNNL, from an analysis by Jim Edwards on one-step ethanol to jet fuel. 
14 National Renewable Energy Laboratory’s (NREL’s) platinum-on-titania catalyst is an example of a thermally stable, fast-pyrolysis catalyst demonstrated 
at bench scale. There are other examples from industry.

Sustainable Aviation Fuel: Review of Technical Pathways 
36 
amounts, thereby increasing the mono- and bicycloalkanes and perhaps also the iso-alkanes (from ring 
opening). Such a mixture would be an intriguing jet fuel.14F
15 
5.4 Cycloalkanes, Other Ring Sizes, and Fused Rings 
While much is known about the fuel properties of alkylated cyclohexanes, less is known about other ring 
structures that are available from biomass sources through catalysis and fermentation.  
5.4.1 Ring Contraction 
Five-member rings can be produced from cyclohexanes using a catalytic route that causes a ring contraction, 
and such research has been sponsored by BETO (PNNL unpublished research). This chemistry is used in 
petroleum refining and has been applied to pyrolysis oils to improve gasoline fuel properties at PNNL 
(McVicker et al. 2005; McVicker et al. 2002).  
5.4.2 Ring-Forming Reactions 
Larger and smaller rings sizes are possible to produce from renewables (Figure 17). BETO announced a recent 
award to fund work that converts isoprene to cyclobutane and cyclooctane. Three-member rings are produced 
for specialty chemicals and can be made from olefins using carbene chemistry.  
 
Figure 17. Smaller and larger rings from 3 to 8 carbons 
Less is known about properties of larger and smaller ring sizes because they are not common in fuels. Because 
various ring structures are available from biomass, this as a knowledge gap that needs to be addressed. 
However, the cost of the compounds will have to be competitive and the value of the molecules high if this 
approach is to be used. 
5.4.3 Ring Motifs in Wood Extractives and Fermentation 
Biotechnology presents new possibilities for providing interesting possible ring structures (Figure 18). Natural 
product extractives such as turpentine are one source of new cyclic compounds. However, to achieve the 
 
15 Olarte, M. V., A. Padmaperuma, E. Christensen, J. Ferrell, G. G. Neuenschwander, L. J. Rotness, A. H. Zacher, R. Gieleciak, A. Alvarez-Majmutov, and 
J. Chen, PNNL project document, unpublished.

Sustainable Aviation Fuel: Review of Technical Pathways 
37 
amount required for fuel markets, fermentation of sugars may be required. The cost will need to be reduced if 
these products are to be industry-relevant.  
carane camphane pinane
hydrogenated turpentines
limonane
1-ethyl-3,3-dimethyl
cyclopentane
sabinane
selected other examples
 
Figure 18. New ring structures, fused rings, and different ring sizes from nature 
5.4.4 Esoteric Cycloalkanes 
There are many esoteric cycloalkanes—from adamantane to cubane—and various molecules from 
sesquiterpenes to ladderanes are under study within BETO. Interest in the highly strained compounds arises 
from the desire to increase energy density and specific energy. Simply having a strain in a molecule is not 
enough to improve energy content, as many strained molecules have poor specific energy. Furthermore, alkyl 
substitution on esoteric rings often results in moderating the fuel property of interest. For example, alkyl-
adamantane has properties more akin to common ring motifs (Harvey et al. 2016). Esoteric compounds that 
offer high energy density and specific energy may have flaws in other fuel properties that will strictly limit 
their blending levels. Such flaws include high melting points (e.g., cubane, one molecule of interest, melts 
above 100°C).  
BETO is currently examining several molecular structure motifs for fuel properties. Those shown in Figure 19 
were presented at the Advanced Bioenergy Leadership Conference and contained four- to nine-member fused-
ring systems (George et al. 2018). Many of the parent compounds are sesquiterpenes containing 15 carbons 
with unsaturation and are of interest for their pharmacological properties; examples of terpenes containing 10 
carbons may be a better fit for SAFs if they can be prepared at a sufficiently low cost.

Sustainable Aviation Fuel: Review of Technical Pathways 
38 
longifolane
alpha-cedrane
clovane
epi-isoziaene
trimethyl-
adamantine
H
H
beta-carphyllane
alpha-neoClovane
tricyclooctanes
bicyclohexane
 
Figure 19. Esoteric molecules under examination for fuel properties 
5.5 Low-Aromatic, High-Energy-Content Fuel Properties 
Research co-supported by the Vehicle Technologies Office and BETO in the Co-Optima initiative, designed to 
look at light-duty vehicles, is not addressing underlying gaps in understanding fuel properties, and hence 
structure–function relationships, required for aviation. Further, the types of hydrocarbons desired for aviation 
vary dramatically relative to the needs of ground transportation. Combustion R&D and analysis beyond what is 
done in Co-Optima is an opportunity for new work within this program. Energy content is only one of many 
properties a jet fuel must meet. There is a rich variety of ring structures, from substituted cyclohexanes to 
esoteric molecules that offer a variety of ring sizes and fused rings. Further, the potential cost–value 
relationship should be understood regarding blend limitations.  
5.5.1 Gaps in Understanding Cycloalkane Properties 
The energy density of many cycloalkanes is higher than that of iso-alkanes, while the sooting behavior is less 
than that of aromatics. Therefore, these molecules can potentially have compelling advantages as integral 
blending components in a jet fuel that has low aromatic content. Today, there are no general rules to predict the 
behavior of fuels composed of various cycloalkanes of various ring sizes, conformers, fused rings, and level of 
branching. Research opportunities related to cycloalkanes include: 
• C
ycloalkane molecules from biomass will likely be blended with Jet A fuel for the foreseeable future. 
Understanding the bulk properties of blends and blending behavior is needed. 
• U
nderstanding the fundamental properties of mono-cycloalkanes and how these properties vary with the 
number of carbon atoms in the ring during spray atomization and combustion.

Sustainable Aviation Fuel: Review of Technical Pathways 
39 
• C yclo alkanes, including those derived from lignin, will almost always have alkyl chains. An 
understanding of the impact of the length of the alkyl chain and isomerization on molecular properties is 
also necessary. 
• M
any biomass-based cycloalkanes can have multiple rings in many configurations. An example may be 
bicycloalkane, where two independent rings are tethered through an alkyl chain. Another example may 
be two rings that are “fused” together by sharing two carbon atoms, such as decalin. The carbon numbers 
of molecules in both examples can be the same, but their properties may be very different. Esoteric 
examples include additional fused ring structures. 
• S
ome results show favorable swelling characteristics when using fused bicyclic alkanes. These 
characteristics are a mechanism for the complete removal of aromatics from jet fuel, such as decalin. The 
removal of required aromatics will lead to reduced aircraft particulate matter and higher specific 
energies. Additional work on the swelling characteristics of fused bicyclic alkanes and other material 
compatibility is needed. 
• S
afety is critical in civil aviation and more work is needed to understand the viability of strained 
compounds for meeting civil aviation needs. 
5.
5.2 Quantifying the Value of SAF 
SAFs that have higher energy content, high thermal stability, and low aromatic content used at large scale can 
benefit the practical needs of a mission and perhaps other functions such as maintenance. Such benefits need to 
be quantified and understood within the larger feedstock–production–mission system. Technology 
opportunities and optimizations exist in this space that may further refine goals and collaborations across the 
fields of science, agriculture, and engineering.  
Nominally, performance benefits can be attributed directly to the specific energy and energy density 
improvements via payload–range curve studies.15F
16 A conceptual analysis of the thermal stability benefits of an 
energy-rich fuel suggests that a >3% decrease in specific fuel consumption may be possible in newer engine 
designs, combined with an approximately 5% drop in airline expenses associated with maintenance. 
Anecdotally, one engine company at the JET Workshop suggested that increases in thermal stability could 
revolutionize the engine market, driving down multiple costs. The required market penetration of SAFs to have 
this effect remains highly uncertain.  
Near-term impacts: Increases in specific energy and energy density can be more rigorously quantified and 
bounded. Current projections of the benefits of higher-energy fuels are limited in their applicability across 
airlines operations and aircraft that could see the most significant benefit. Discussions and collaborations with 
airlines and engine OEMs are still in their infancy. 
Work needs to be done on quantifying the opportunities for benefits of high-energy SAF under the three 
scenarios outlined throughout this report—minimization of aromatics, replacement of aromatics, and addition 
of novel molecules. Having a sense of the magnitude of these benefits is essential. Savings would need to be 
demonstrated in real-world scenarios before airlines would pay more.  
Mid-term impacts: Reduced maintenance requirements from increased thermal stability, while not currently 
quantified, would not require hardware augmentation. As one participant noted at the Cleveland meeting, a 
fuel with high thermal stability has the potential to disrupt industries within the aero-engine space, although 
challenges would need to be overcome to gain benefits from higher-thermal-stability fuels. Investments here 
could be low-hanging fruit in the quantification of benefits.  
 
16 Modeling supported by BETO at Georgia Tech is suggesting as much as a $0.54-per-gallon value added for a hypothetical high-energy-content SAF. 
Modeling SAFs that are attainable is needed. Lowering the cost of SAF remains a paramount need.

Sustainable Aviation Fuel: Review of Technical Pathways 
40 
Long-term impacts: The conceptual benefits of SAF with higher energy and thermal stability need to be more 
thoroughly and broadly explored. Increases in thermal stability are already aligned with the OEM research 
trajectories of increasing compression ratios and commensurate thermodynamic efficiency. Studies referenced 
above on thermal stability suggest a 14% potential improvement in specific fuel consumption. This result 
needs to be further vetted and stress-tested. The propagation of this to real benefits will require new OEM 
hardware that can use the fuel improvements. However, investigations in this realm require buy-in from 
multiple agencies at a minimum, with OEMs and fuel producers further enabling the rate and depth of progress 
in a co-optimization methodology. Undoubtedly, this path offers the most general benefit to all fuel, engine, 
and airline stakeholders. 
5.6 Quantifying the Value Added with SAFs 
Several performance, value-added fuel properties have been listed here. These properties are listed because 
industrial stakeholders have identified them as properties for which they would be willing to pay. However, the 
quantification of the additional value remains uncertain, although modeling can provide potential opportunity. 
Questions regarding these cost–benefit thresholds need to be answered to give pointed and clear requirements 
for successful deployment. Nominally, the benefits from properties listed in Chapter 2.1.1 need better 
quantification. Initial work has notionally quantified benefits from increases in specific energy and energy 
density. However, the monetization of thermal stability and sooting/particulate emissions is not as clear. For 
this work, it is important to understand and establish theoretical limits. Further study could then refine 
potential value with industry engagement.  
5.7 Summary of Fuel Molecules 
There is an R&D opportunity to further reduce cost of iso-alkanes and cycloalkanes. These two families of 
molecules provide all the properties needed in jet fuel. Aromatics and n-alkanes will often be coproduced; 
however, it is important for researchers to understand that their primary production is not an optimal research 
area. 
Larger molecules can be cracked to produce jet-range molecules. One challenge is the low specificity of the 
chemistry, where low-value naphtha is coproduced. Chemistries are available that could have higher 
specificity, but require strategically placed double bonds, as is the case for carinata oil. Thermal chemistry, 
such as supercritical liquefaction, is being pursued as an alternate way to process lipids, and the fuel is at the 
balloting stage for ASTM approval. 
Small molecules can be built up into jet-range molecules. Five chemistries—olefin oligomerization, aldol 
condensation, Prins condensations, ketonization, and Guebert chemistry—cover the functional groups common 
in bio-derived species, including olefins, carbonyls, and carboxylic acids. Building small molecules up 
provides the potential for better control of carbon chain length. BETO is currently supporting oligomerization 
chemistry. 
Cycloalkanes offer densities and swelling capacities that complement the high specific energy of iso-alkanes. 
Cyclohexanes are easily assessable from aromatics using thermal catalytic processing of total biomass and 
from depolymerization of lignin. A significant question is defining the cost–value proposition of the added 
hydrogen to reduce aromatics to cyclohexanes. One industrial process is being tested by industry, the Shell IH2 
process, which fully hydrogenates the jet fraction to produce aromatic-free, cyclohexane-rich jet fuel.  
Smaller and larger rings are also possible, including those with three, four, seven, and eight carbons. Fused 
rings with a variety of ring structures from four to nine carbons are available from fermentation pathways. 
Many compounds in this class are 15-carbon sesquiterpenes. Ten-carbon terpenes will likely be more 
applicable for SAF. Understanding the cost drivers and reducing cost will be necessary for these to be used in 
fuel applications. A hydrogenated sesquiterpene, farnesane, is approved for use today. It is produced 
commercially but not used in fuel application; industry analysis points to the cost of production as a

Sustainable Aviation Fuel: Review of Technical Pathways 
41 
hinderance. Before pursuing other terpenoids for fuel applications, an understanding of how to reduce the cost 
of production is needed. 
Modeling potential value can be done at a relatively low cost and provide information to the community. The 
value proposition of these fuels could be done with combustion modeling, small-quantity testing, structure–
activity determinations on performance properties, and a study on the benefit of thermal stability on coking and 
engine design with strong engine company support. It is important to understand fuel properties before 
proceeding with development of producing the various possible compounds. 
6 R&D -- Cost Reduction 
Generally, TEA results for most pathways show that the two most significant contributors to cost are the 
feedstock costs and capital cost. These are considered in this chapter.  
6.1 Feedstock-Related Research 
In our analysis, feedstocks ranging from lipids (fats, oils, and greases), sugars, lignin, and whole biomass 
(cellulosics) were considered. Feedstocks are the primary cost contributor to biofuels. Rethinking feedstock 
sourcing and the means of reducing costs while doing less harm to watersheds and land is a critical activity.  
6.1.1 “Solve Another Problem” 
Raw materials are grown or derived to provide value to the producer. Farmers are seeking the highest value for 
their lands. At the same time, environmental services are needed to improve soil and water quality. Solving 
another problem, such as providing an environmental service, provides new raw material options for biofuels, 
particularly materials already collected.  
• F
armers grow biomass on land between crops for other purposes, such as soil preservation, nutrient 
recovery, and erosion control. All are examples of biomass used for an environmental service. Because 
this biomass is grown not as feedstock, but for another purpose, there may be opportunities to obtain it at 
a lower cost compared to purpose-grown crops. Often, the new crop can be mustards and other crops rich 
in oilseeds ideal for distillate and mid-distillate fuels. In the arid western United States, fields can lay 
fallow for multiple years and still require care to break down vessels to preserve water retention. 
Growing a crop designed to improve soil and water retention for the fallow years provides a different 
value proposition. While crop research is mainly conducted by USDA and the Office of Science, 
understanding the crops grown and how they can best be converted belongs to EERE. Further, by 
working together, crops can be chosen that can more easily be converted to jet fuel. 
• Was
te feedstock such as manures are an environmental challenge. Their use in anaerobic digestion to 
produce biogas has low commercial value but is considered because the environmental service provides 
value. The return on investment can be improved by making a product of higher value than a medium-
Btu gas. One method of improving the return may be to arrest anaerobic digestion midway, produce 
volatile fatty acids, and then catalytically upgrade them to hydrocarbon fuels. Approximately 2,200 
anaerobic digestion systems are in operation in the United States at present, and many of them are close 
to major airports where there is a demand for SAF. Anaerobic digestion biogas capacity in the United 
States is estimated to be approximately 431 trillion Btu (NREL 2013), equivalent to over 3 billion 
gallons of jet fuel per year. Waste gases that are rich in CO could have an enormous global impact, 
exceeding 32 billion gallons without including syngas.  
• Sim
ilarly, environmental and other services can be addressed and wet, dry, or gaseous carbon feedstocks 
can be available at low cost. Other examples besides manures are landfill gas, landfill solids (sorted and 
unsorted MSW), and sludges from wastewater treatment plants. These require simple technologies to 
produce intermediates that can be cleaned and further processed to fuels. Such technologies can include 
liquefaction and gasification, as well as anaerobic digestion.

Sustainable Aviation Fuel: Review of Technical Pathways 
42 
• W oody biomass residuals from forest p roduction, wildfire mitigation, and forest health operations are 
available in many regions of the United States. Where TEA shows these residuals to be available in 
quantity and at reasonable cost, there are opportunities for SAF to be part of value propositions that may 
include products like biochar (pyrolysis) and lignosulfonates (from sulfite pretreatment pulping). 
Emerging processing technologies could create lower-capital options for the production of sugars and 
clean lignin and could be paired with ATJ SAF processing. 
6.
1.2 Collected Carbon from Existing or Developing Processes 
Firms that produce tires are developing technology to extract rubber resin from guayule biomass using solvent 
extraction processes, and therefore have already factored in biomass costs and the capital infrastructure to 
grow, harvest, and grind the biomass to extract the rubber resin. The residual biomass after resin extraction has 
a low value and must be disposed. While collected residues present an opportunity for low-cost raw materials, 
there may be higher-value uses of the residue than fuels. Nevertheless, SAF can be developed for residue 
biomass for which capital, harvesting, and preprocessing costs have already been paid.16F
17  
Anaerobic digestion firms have already made investments in collecting and processing low-value waste to 
produce low-value biogas. These investments can potentially be repurposed to make volatile fatty acids, which 
then can be upgraded to SAF via ATJ or aldol condensation pathways, resulting in additional value from these 
investments. As discussed previously, there is more than enough capacity to supply a significant part of the jet 
fuel market. Anaerobic digestion systems are well-suited for this opportunity because they are located close to 
large cities where the waste feedstock is created and where large airports have a demand for SAF. These 
systems would be relatively small and thus capital requirements would be low. Benefits would be derived from 
process intensification to improve capital effectiveness. 
6.1.3 Waste Gases  
An increased emphasis on collected underused renewable carbon and other carbon in waste streams that 
otherwise has a liability can change the cost paradigm. Industrial waste gases, rich in CO, can produce 32 
billion gallons of aviation fuel globally.  
Likewise, MSW is an increasing problem. Gasification of unsorted MSW is done today in Japan. Using the 
synthesis gas to make fuels rather than power is a tremendous opportunity. There is an opportunity for waste-
gas research to entail more than FT; waste-gas fermentation is commercially practiced today.17F
18 
Anaerobic digesters are becoming more prevalent. While anaerobic digestion does not use waste gases, it does 
produce methane-rich gases diluted in CO2. Other methane-rich gas sources are not being utilized and provide 
R&D opportunities between EERE and the Office of Fossil Energy. 
Arrested methanogenesis, a form of anaerobic digestion, offers options for producing volatile fatty acids that 
could be upgraded via various chemistries, such as hydrogenation (greatly increasing hydrogen demand) or 
ketonization (reducing carbon yield by loss of CO2), followed by further upgrading to obtain the required 
carbon numbers. The feedstock–reactor interface could be expanded with new thinking about how to reduce 
cost in distributed processing applications that arise from anaerobic digestion and waste-gas sources. 
6.1.4 CO2 as a Carbon Source 
The interest in reducing atmospheric CO2 is prevalent among U.S. companies that compete in the global 
markets, as well as some state governments.  
 
17 Guayule is a perennial desert shrub and USDA is investing in its cultivation for use in natural rubber with the residual to be converted to jet fuel. The 
project is led by the Center for Sustainable Bioeconomy for Arid Regions, PI Kim Ogden.  
18 The first steel mill waste-gas-to-ethanol facility is now operating in China (LanzaTech 2018). Municipal solid waste has also been demonstrated in Japan 
(LanzaTech 2017a).

Sustainable Aviation Fuel: Review of Technical Pathways 
43 
Unlike the waste gases discussed previously (CO and CH4), CO2 does not contain usable energy. Hence, CO2 
is merely a source of carbon in which all the energy of the fuel would need to come from an external source: 
hydrogen or electrons. 
As an example, a Canadian company has initiated contact with the Commercial Aviation Alternative Fuels 
Initiative (CAAFI) about a CO2-based FT fuel. Hydrogen gas combined with water–gas shift chemistry 
provides the syngas for FT (Csonka 2018).  
A second example where hydrogen is used to provide energy involves fermentation of a refinery waste gas 
stream containing CO, CO2, and H2. In this case, the organism facilitates the biological equivalent of water–gas 
shift chemistry. The stoichiometry of the reaction is five equivalents of H2, one equivalent of CO, and one 
equivalent of CO2.18F
19 
Research based on the use of electrons to reduce and convert CO2 is popular today and the focus of many 
research groups. A clean source of CO2 is from fuel ethanol production, in which a small 40-million-gallon-
per-year facility produces 114,000 metric tons of CO2 during the fermentation process. The total domestic 
production of CO2 from ethanol is 42 million metric tons. The energy required to convert the CO2 to carbon 
monoxide is 12.6 MJ/kg and converting water to hydrogen is 176 MJ/kg based on Gibbs free energy. With a 
synthesis gas at a ratio of 1:2 CO to H2, either FT or ATJ could be used to produce jet fuel. The electrical 
power requirement to convert the CO2 and water to synthesis gas is 90 MW for a single ethanol facility and in 
excess of 30 GW for current U.S. ethanol facilities (Figure 20). To put this in perspective, the largest dam in 
the United States, Grand Coulee, produces 6.8 GW of power. The second-largest wind farm in the United 
States is 845 MW and exceeds 300 turbines at the cost of $2 billion to build. The electrical power demand to 
add energy back to CO2 to be used as a fuel or fuel precursor is high.  
While the use of CO2 “solves another problem,” and when sourced from ethanol plants is clean and accessible, 
its use for fuel applications is less straightforward as the cost and environmental stress will need to be 
assessed. There are cases where CO2 conversion may make sense, such as when H2 is also part of the waste 
gas. 
 
19 A demonstration facility is being built at IndianOil’s Panipat Refinery in Hayrana, India, employing LanzaTech technology. The estimated cost of the 
demonstration facility is $55 million (LanzaTech 2017b). The stoichiometry is from LanzaTech.

Sustainable Aviation Fuel: Review of Technical Pathways 
44 
 
Figure 20. CO2 from ethanol production conversion to jet fuel via synthesis gas 
CF = capacity factor  
While all carbon sources should be considered, electrons to convert CO2 at a meaningful scale are not going to 
be free. Even at a low cost, $0.02–$0.04 per kWh, it is challenging to achieve the economics required to 
produce fuels from CO2 and water (Weber 2019; Jouny, Luc, and Jiao 2018). 
6.2 Reducing Capital Cost 
The simplest level of process intensification either reduces the number of unit operations that are required to be 
built or reconfigures unit operations to reduce cost. This can be done by reducing or combining unit 
operations, minimizing the number of separations required in a process, or using infrastructure that is already 
in place. Process intensification can also refer to using new chemistry designed for the scale of biomass rather 
than petroleum. 
6.2.1 Use Current and Distressed Infrastructure 
Use of existing depreciated equipment and infrastructure or coprocessing with other streams can potentially be 
a powerful approach to reducing capital costs. Conversely, not using infrastructure in place incurs costs.19F
20 
Following are examples of using existing infrastructure: 
 
20 Researchers have suggested using a second delivery system for SAF to airplanes but have not accounted for the costs incurred of not using the 
infrastructure in place. SAF will need to be delivered in the current hydrant systems.

Sustainable Aviation Fuel: Review of Technical Pathways 
45 
• Refinery infrastructure: Hydrogenation using imported pressurized hydrogen gas is best done at a larger 
scale at a central refinery—the “hub” of a hub-and-spoke model. When using the infrastructure of a 
petroleum refinery, even a separate reactor built within the boundary of the refinery reduces cost.  
• Send other streams to a refinery: Nearly all processes that produce SAF blendstocks in amounts that can 
be blended above 10%–15% also produce lights and heavies. Achieving the highest value from each 
stream is critical. Petroleum refineries provide one means of using the other streams or blending the 
streams in a way that is cost-effective and leverages depreciated capital.  
• World Energy-Paramount located its 45-million-gallon-per-year SAF/renewable diesel facility on a 
former asphalt refinery that had existing fuel storage, a truck rack, rail storage, and a pipeline connecting 
to southern California distribution hubs. Hydrogen is trucked in, and the light fraction (naphtha) is sold 
into the gasoline market.  
• Other infrastructure: Facilities, including paper mills and anaerobic digestion systems, are underutilized. 
Analysis to understand location and opportunities provide a means to reduce cost. Additional examples 
include Gevo, which uses dry-mill infrastructure to produce iso-butanol, and Poet, which has built a 
cellulosic ethanol plant next to a dry mill to share auxiliary units. A final example is corn ethanol plants, 
which are adding new unit operations to convert carbohydrates in distillers’ dried grains with solubles to 
ethanol, providing a cellulosic renewable identification number and building on existing infrastructure.  
6.2.2 Petroleum Refinery Integration 
Biomass being coprocessed in petroleum refineries is now occurring. The first materials to be coprocessed are 
lipids (fats, oils, and greases). These feedstocks go into hydrotreating units that primarily feed distillate 
streams. BETO is funding R&D studying coprocessing of other biocrude oils. An evaluation of the fractions—
jet in addition to gasoline and diesel—could be added to such a study. 
Pyrolysis oil co-refining is perhaps near commercial and can be licensed from UOP/Envergent to produce fuels 
with 2%–5% biofuel content. BETO is presently conducting bio-oil coprocessing trials at the Andeavor 
Martinez Refinery and already has capabilities to conduct coprocessing at its National Labs. One challenge to 
investigate is if the technology can be extended to SAF, and if the co-processed fuels could meet the tight 
specification. The technology would require hydrogen transfer catalysts, or more likely fractionation of the jet-
range hydrocarbons. This research could include an evaluation of additional hydrotreating to produce 
cycloalkanes. Note that today, the only renewables that can be coprocessed in a refinery are fats, oils, and 
greases. Any other coprocessing will require ASTM approval.  
6.2.3 Separations 
Separations and purifications are a significant cost driver. While not reviewed in this report, it is important for 
researchers to understand the value of separation needs and increasing the focus on reactive separations. 
Separations involve two opportunities: 
• Reduction of the number of separations: A process may be less expensive if a separation step can be 
eliminated, even if the conversion is less elegant. For example, while there are catalytic forms of HTL, 
the cleanup requirement to protect the catalyst may make the overall process less optimal than using 
thermal HTL, eliminating a cleanup step up front.  
• Reactive separations: A combination of reactive steps with separations step. Examples include reactive 
distillations in which a catalyst is combined as part of the distillation and continuous membrane 
separation or liquid–liquid extraction with fermentation. 
6.2.4 R&D Needs for Small-Scale Distributed Refineries 
The total capital cost and scale of a project, such as for FT processing, is often a deployment hurdle. This 
capital cost can be exacerbated for biomass because the local supply curve for feedstock is generally inelastic,

Sustainable Aviation Fuel: Review of Technical Pathways 
46 
resulting in significant increases in price with increases in volume. Because feedstock cost was identified as a 
critical component of SAF production cost at all three workshops, biomass-based processes need to be 
developed at a small scale to reduce biomass demand (and therefore feedstock cost) at a location. 
Small-scale plants must be designed to change the process throughput rate-limiting step paradigm so that the 
process economics are described by a different production curve that allows higher capital efficiency at lower 
throughput. Examples of the change of rate-limiting step paradigms can include a change from batch to 
continuous operations and the use of membrane and microchannel reactors, which scale based on area rather 
than volume. Labor costs generally become prohibitive for small-scale production facilities, so a high degree 
of automation is also required. 
Small-scale plants can be mass-produced at a significantly lower cost, and manufacturing can enable 
economies of scale. While the engineering and production of reactors is closely aligned to the mission of the 
Advanced Manufacturing Office, the chemistry and chemical engineering required to change rate-limiting 
phenomena in a process require essential science elements that are within BETO’s mission. 
6.3 Rethinking Biorefineries 
6.3.1 Sugars to Products, Lignin to Fuels 
Presently, the biological conversion pathway for lignocellulosic biomass has been to convert the sugars to fuels 
and the lignin to either power or products. The aromatic nature of lignin may make it particularly suitable as a 
feedstock for lower-cost production of cyclohexane derivatives with desirable properties as a higher-
performance SAF. Sugar from cellulose may also be a more natural feedstock for biological conversion to 
chemicals and products rather than lignin.  
An alternate paradigm would use lignin and residues as feedstock for fuels and sugars as a feedstock for 
bioproducts and biochemicals, both sourced from lignocellulosic biomass. The caveat in this approach is that 
the lignin to be used for SAF must be processable, which often requires it be as close as possible to its native 
form. BETO already has programs that remove significant lignin through solvent extraction or dual-mixed 
refrigerant types of mild processes. Lignin from these processes may be suitable to produce SAF. The sugars 
must not be harmed in such a process. Finally, in some manifestations, only easily removed sugars need to go 
into biochemicals, with residues added to lignin for production of fuels. 
There are various ways that new paradigms could be executed. BETO is funding work in which the six-carbon 
sugars from hydrolysate are converted to a higher-value product but without the constraints on high sugar 
utilization or low biomass growth. Preferably all the residuals (e.g., lignin and cell bodies, unconverted sugar) 
are converted to biocrude oil using liquefaction. Internal data have shown a high fraction of upgraded biocrude 
oil is in the jet-fuel range. Understanding the fuel properties, particularly with enough hydrotreating to produce 
high cycloalkane content, is in order.  
6.3.2 Focus R&D on Conversion Platforms That Provide Product Flexibility  
Supporting R&D that provides biorefineries with fuel and product options is critical for viability; however, 
chemical coproducts do not decrease the cost of fuel production and fuels cannot be sustainably sold as a loss 
leader. Hence, R&D will need to continue its focus on decreasing cost of the fuel pathway, and TEAs 
supporting R&D are best used to identify where cost can be removed from the system. The trend to have TEAs 
show lower selling price by invoking value in other streams can be misused, although it is wise to seek the 
highest value from each process stream. 
Consider how petroleum refineries maximize value. Petroleum refineries do not produce high-value products. 
Instead, refineries extract as much value as possible from each process stream using minimal added 
infrastructure and wasting little carbon. Petroleum refineries ship super-commodity chemicals, such as 
ethylene or benzene-toluene-xylene, to standalone chemical plants, specialty chemical plants, and 
pharmaceutical plants. These plants produce the many products such as petrochemicals (plastics, solvents,

Sustainable Aviation Fuel: Review of Technical Pathways 
47 
monomers), personal care products, and others that demand higher value. R&D needs for producing a fuel 
differ from those for producing a monomer or a personal-care product. Hence, producing a high-value 
chemical product first is not going to support the R&D to bring down the cost of the fuel. Furthermore, a 
biorefinery, which is much smaller in scale, cannot support the capital to produce a myriad of fuels and 
chemicals and instead focuses on extracting the highest value from each stream.  
There is an R&D opportunity that focuses on platforms in which a common intermediate, using standard or 
similar processing steps, can produce fuels or commodities based on market conditions, as this would reduce 
risk and add value. While there are examples of this in BETO’s portfolio,20F
21 a greater focus on the 
opportunities for platforms that support SAF and products using similar infrastructure could be a higher target.  
6.3.3 Feedstock Flexibility to Use Full Capacity 
Today, SAF is produced from lipids that can use low-cost feedstock such as fats, oils, and greases. However, 
lipid routes cannot meet the SAF volume demand alone with the current feedstock supply. New low-cost 
feedstocks are needed. Carinata research, funded by USDA, is a potential new source of lipids.  
A low-cost source of lipids that are not currently utilized are fats, oils, and greases in wastewater sludge. Algae 
is another source of lipids on a longer-term horizon. However, algae production rates vary dramatically from 
summer to winter, even in places like Florida. The variance is easily 50%. While modeling average yields is 
appropriate, the capital to build a plant that is only intended for full operation part of the year is a problem. If 
such lipids were coprocessed with more abundant lignocellulosic biomass, the biorefineries could run at full 
capacity year-round, yield higher output, and optimize capital.  
Feedstock–conversion interface research is needed for wet feedstocks that cannot be stored and for which 
coprocessing other biomass sources may be necessary. The interface includes reducing the cost of lipid 
extraction/purification and considering coprocessing lipid streams with other streams. 
Research can build on what has already been learned from other programs, such as optimization of lipid yield 
during combined extraction and conversion processes, with liquefaction utilizing both storage lipids (free fatty 
acids and glycerides) and cell wall lipids (often phospholipids). Study of coprocessing lipid-rich streams with 
more prevalent biomass streams is in its infancy. Further, there is an opportunity to apply the concept of mixed 
biomass–lipid streams to both algae and wastewater sludge.21F
22 
While HEFA is commercial, the lipid feedstock is purified extensively before processing, which adds cost. 
Biocrude oils will also need to be purified for long catalyst life. More R&D on purifications is warranted.  
Fats, oils, and greases prevalent in wastewater sludge present an opportunity. Coprocessing using liquefaction 
technologies could improve the product profile of thermal processing of lignocellulose, providing higher 
impact (fuel produced). Liquefaction research can be done under wet conditions, either subcritical or 
supercritical, in water or with other solvents. Also, dry feedstocks could be considered using more standard 
pyrolysis techniques.  
Regardless, R&D along the feedstock–conversion interface of a broader range of liquefaction conditions and 
mixed lipid–biomass feedstocks will bring value to the research and biofuel communities and produce a higher 
volume of fuel possible from lipids alone, and of higher quality than is possible from biomass alone regarding 
distillate fuel requirements. 
 
21 As one example of multiple products in a biorefinery-scale facility, BETO and the Advanced Manufacturing Office are supporting research at PNNL for 
several fuel and higher-value products using alcohol as a platform. The chemistries and infrastructure required are similar for the various products and may 
be assessable without added capital. 
22 Initial study of wastewater sludge indicates a fuel production potential in the United States of six billion liters per year.

Sustainable Aviation Fuel: Review of Technical Pathways 
48 
6.4 Sourcing Hydrogen 
Hydrogen demand is high for all biofuels and unusually high for SAF, where olefins and heteroatoms such as 
oxygen are not allowed for operational and safety reasons. In North America, the cheapest source of hydrogen 
gas is from steam methane reforming. This is not true globally; exceptions include areas where natural gas is 
expensive or not prevalent, including remote locations such as Hawaii and much of Europe, Africa, and Asia. 
Furthermore, at small distributed scales, use of pressurized hydrogen gas is cost-prohibitive.  
A steam methane reforming facility produces 10 tons of CO2 for each ton of hydrogen gas (Collodi 2010). 
Finding new low-cost sources of hydrogen gas can lead to reduced GHG emissions for petroleum refineries 
and biorefineries.  
Renewable electrons can provide the reducing equivalents needed to remove oxygen or saturation of biomass-
sourced molecules. Advances in electrocatalysis open distributed processing opportunities that allow use of 
dispersed carbon sources that are underutilized.  
The use of electrons as a replacement of hydrogen gas in this application differs from the use of electrons to 
convert CO2 to fuels in two aspects. First, the feedstock under consideration has available energy content. 
Second, there are examples where the reducing equivalents can be produced from oxidation of carbon that 
would be lost otherwise to the aqueous phase. This could theoretically be accomplished without bringing in 
outside renewable electrons. An example would be upgrading HTL biocrude oil. Oxidation of the wastewater 
has enough energy content to provide the reducing equivalents required to upgrade the biocrude oil. 
Regardless of the source of electrons, whether from nuclear energy, renewable energy, or oxidation of carbon 
in wastewater, both high-resolution consideration of cost–benefit and high-fidelity supply-chain analysis are 
needed to determine the best use of electrons. Both catalyst research and analysis are areas that fit the BETO 
mission. 
6.5 Analysis of Cost Reduction 
DOE, FAA, and USDA have developed a suite of analysis tools that could be helpful for defining research 
questions that can bring down the cost of SAF. These have not been sufficiently coupled to supply-chain 
analysis tools or to analysis tools examining the potential value of jet fuel supporting different missions. 
Further, TEA and GHG results are inconsistent across the industry and do not address the economics 
associated with pioneer plants.  
TEA provides essential information about where research could be prioritized to bring down costs. Used in this 
manner, TEA of various systems will be invaluable. TEA can also be used to rule out some processes, such as 
where the costs of inputs are higher than the value of the products. High-fidelity TEA is not needed for such 
“back-of-the-envelope” analysis. Using TEA to choose between two paths that are plausible can be 
problematic, as the uncertainty in the model output commonly exceeds the difference of cost between two 
routes. The use of TEA without understanding uncertainty is exacerbated by assumptions (positive or negative) 
on chemistry and for technologies at early technology readiness levels. Simply adding consistency to models is 
valuable but does not address the underlying issue of uncertainty, which requires uncertainty analysis. 
The LCA of pathways that are not fully developed also have a high level of uncertainty that is not expressed in 
the model output. However, if LCA was done to inform research, it would be a valuable addition. 
Supply-chain analysis tools developed by USDA’s Northwest Advanced Renewables Alliance and used in 
FAA activities can offer a new look at high resolution and a regional analysis that incorporates feedstocks, 
products, infrastructure, and other required aspects. Supply-chain analysis is valuable in research to define 
conversion requirements (size of plants and the location of facilities, utilities, and water) that offer valuable 
insights into the required technology, which informs science questions. While a supply-chain analysis has been

Sustainable Aviation Fuel: Review of Technical Pathways 
49 
done on MSW (Englund et al. 2016), it has not been done on other feedstocks or for a broad number of 
potential routes.  
6.6 Summary of Cost Reduction 
Research provides an opportunity to reduce production cost. The opportunities extend to lowering the 
feedstock cost and increasing availability of feedstocks. Waste feedstocks that are already collected are “low-
hanging fruit.” Feedstocks need not only include lipids and sugars; waste-gas streams, rich in CO, could have a 
significant impact on the global markets. Synthesis gas increases the impact even more. Finally, R&D needs 
for mixed feedstocks that include lipids and biomass present new opportunities. 
Separations are a large cost driver and there are research opportunities on process intensification—reducing 
and eliminating, where possible, process and clean-up steps. Reactive separations reduce unit operations and 
cost. There is an opportunity for separations to be considered early in process-flow planning and not wait until 
the later part of process development.  
Analysis can continue to be used to identify cost drivers and targets. The uncertainty in model output is high 
and discarding routes may be done more effectively using other criteria. Supply-chain analysis, in high 
resolution, can help identify new opportunities and research areas to drive down cost. 
It is important to “start with the end in mind,” because the fuel property requirements for gasoline, jet, and 
diesel fuels dramatically diverge.  
7 Summary and Insights  
While Chapter 6 provides a summary of important areas where R&D could reduce cost and/or increase value 
proposition for producing SAF, this chapter outlines research opportunities to achieve the goals set forth by the 
commercial aviation industry. Reducing capital, production, and feedstock costs for SAF are the key 
requirements for its widescale deployment. In the longer term, providing a fuel that has improved properties, 
within the bounds of ASTM specifications, further improves the possibility for market pull. In the near term, 
however, expanding production capacity of existing approved fuels is critical.  
7.1 An R&D Strategy for SAF  
The commercial aviation industry must significantly reduce its GHG impacts to continue to grow and support 
global mobility and commerce. Through the ICAO, the industry has established CORSIA, which sets 
voluntary carbon-reduction standards during Phase 1 (through 2026) and mandatory standards during Phase 2 
(2027 and beyond). SAF use will need to rise to greater than 30% of total jet fuel consumption by 2040 to meet 
ICAO commitments; on a global basis, this is greater than the total jet fuel currently consumed in the United 
States.  
Because civil aviation cannot meet CORSIA targets by efficiency gains and improving engines and flight 
operations alone, SAF is required. Today, there are five approved SAFs, but their use is limited. SAF fuel 
price, including subsidies, must be competitive with petroleum-based fuels (Jet A) because the cost of fuel is 
up to 30% of the operating cost of an airline.  
Airports also realize that the GHG impacts of their operations will eventually have a negative impact on their 
ability to serve their communities. Therefore, they are supportive in helping airlines with innovative models to 
serve as a fuel aggregator, reduce cost, and accelerate deployment.  
Jet A pricing to corporate and other private users is considerably higher than prices that airlines pay. For 
example, Jet A fuel is sold to corporate and noncommercial airlines at prices ranging from $3.37 to $5.05 per 
gallon for airports in a 50-mile radius of Seattle-Tacoma International Airport. Reaching this market may be a 
strategy for early market penetration.

Sustainable Aviation Fuel: Review of Technical Pathways 
50 
The ASTM D4054 approval and evaluation process for new fuels for jet engines is expensive and time-
intensive, requiring up to 100 gallons for Tier 2 testing and up to 225,000 gallons if Tier 4 engine testing is 
required (Table 6). The evolution of jet engine design takes 14 to 19 years and is significantly more expensive, 
costing several hundreds of millions of dollars, when compared to fuel certification. Therefore, the same 
engines that are in service at present are likely to be in use for a long time in the future. Existing engines can, 
however, use fuel that is up to 15% more energy dense than the average energy density of Jet A fuel, and 
higher energy density correlates with improved performance such as longer useful range or increased payload 
for select missions.  
Fuels are delivered in hydrant systems in which cost and LCA accounting is attributed to those who “pay for 
it.” A separate delivery system is expensive and takes up valuable space. Hence, SAF will be diluted with 
petroleum-based fuels to a significant degree beyond the 50% blend required by ASTM, as the fuel is stored 
and delivered in a single system to all planes serviced at an airport. This points to the primary need to reduce 
cost with a longer-term goal of improving performance.  
Even within the constraints on SAF based on fuel certification and fuel/engine infrastructure, there is an 
opportunity to make renewable fuels that offer better combustion properties than fuels derived from petroleum.  
In closing, the United States currently has a strategic advantage over other countries in terms of SAF, hosting 
the single most extensive collection of companies, approval experts, and researchers. Continuing the 
momentum in SAF R&D offers the opportunity for domestic companies to expand internationally, where 
experience currently lags behind the United States.  
7.2 Insights on R&D 
Bringing down cost and improving value must be properly balanced. The following sections summarize five 
prioritized opportunities for research to achieve these objectives. 
7.2.1 Focus R&D on Low-Cost iso- and Cycloalkane Production 
Conventional Jet A fuel contains n-alkanes, iso-alkanes, cycloalkanes, and aromatics. Of these four 
hydrocarbon classes, it is important for researchers to understand the importance of only two: iso-alkanes for 
specific energy, and cycloalkanes for energy density. iso-Alkanes and cycloalkanes offer desired jet fuel 
characteristics and require R&D, whereas n-alkanes and aromatics, while compliant with ASTM 
specifications, are limited due to poor low-temperature properties (n-alkanes) and poor combustion properties 
(aromatics).22F
23 Chapter 6 provides suggestions in detail as to R&D on the two classes that are complementary 
to current pathways and potentially new pathways. Examples of coprocessing with petroleum refineries are 
provided and allied R&D suggested. 
The focus on iso-alkane is to provide new routes to build up small molecules, with a focus on five chemical 
reactions that span alcohols, carbonyls, carboxylic acids, and olefins. Additional work on parallel pathways for 
breaking down large molecules is also presented. 
Cycloalkanes provide an area in which R&D could expand the understanding of structure–activity 
relationships with a balanced approach of cyclohexane derivatives that could be produced at relatively low cost 
with other ring structures. This study facilitates front-end combustion approval needs with back-end feedstock 
processing approaches. 
 
23 In addition to offering poor combustion (and thus being a primary source of sooting), aromatic production is relatively simple owing to its 
thermodynamic stability, and nearly any oxygenated source when passed over a zeolite-type catalyst produces aromatics. Targeted iso-alkanes and 
cycloalkanes are not as simple, and R&D is warranted.

Sustainable Aviation Fuel: Review of Technical Pathways 
51 
7.2.2 Focus on Low-Cost Feedstocks 
Chapter 6 provides more detail on concepts that can assist in reducing the cost of SAF. R&D is required on the 
fundamentals of conversion processes and engineering for pioneer (first-generation) biorefineries. Two priority 
areas include: 
• F
eedstocks that are already collected and extend an environmental service (e.g., those that “solve another 
problem” and thus change the cost structure). These can include manures, waste gases, and other 
municipal waste such as plastics that, under biological and/or thermal processing, can produce high-
quality intermediates that can be hydrotreated using existing capabilities.  
• M
ixed feedstocks that include lipids and lignocellulosic biomass. This is complementary to commercial 
processes that use low-cost lipids and extend the raw material to include storage lipids (fats, oils, and 
greases) and cell-wall lipids (phospholipids) that are available in quantities that vary seasonally or need 
to be augmented. Mixtures of lipids with high-volume lignocellulosics provide new opportunities to 
increase production, including stable, year-round processing of wet feeds otherwise difficult to store. 
7.
2.3 Focus R&D on Conversion Platforms that Provide Product Flexibility  
For biorefineries to be viable, they must be simple (e.g., low capital cost) and extract maximum value from 
each product stream. Focusing R&D on platforms in which multiple products can be produced from a common 
intermediate using common equipment is a means to reduce risk for biorefinery operators. This differs from 
concepts in which small biorefineries are expected to produce several different products requiring high capital 
(e.g., such as seen with a wet mill versus a dry mill) or in which a biorefinery is really a biochemical facility. 
Ethanol is an example platform and is affordable when sourced from a low-cost gas. Another example is a 
carboxylic acid platform, perhaps from arrested methanogenesis, using anaerobic digestion infrastructure. A 
platform based on a single molecule is likely easier than one based on a complex mixture. The key is that the 
molecule must be inexpensive. 
7.2.4 Provide Replacement for Hydrogen Gas in Distributed Processing 
Hydrogenation is ubiquitous in bioprocessing and particularly important for aviation fuels that cannot contain 
heteroatoms or olefins. There may be opportunities to replace natural-gas-derived hydrogen with renewable 
electrons that provide reducing equivalents needed to remove oxygen or saturation (e.g., hydrogenation of 
double bonds). Advances in electrocatalysis open distributed processing opportunities would allow use of 
dispersed carbon sources that are underutilized. Consideration of CO2 as a new carbon source is highly 
popular. CO2 contains no energy and all the energy in the fuel would have to come from an external source 
such as hydrogen or electrons. Electrons may be better used for carbon still containing energy. While all 
carbon sources should be evaluated, higher-resolution consideration of cost–benefit and high-fidelity supply-
chain analyses are needed to determine the best use of renewable electrons in upgrading raw materials at the 
distributed level.  
7.2.5 Refine and Expand Analysis 
TEA and GHG results are inconsistent across the industry and do not address the economics associated with 
pioneer plants. Generally, TEA results for most pathways show that the two most significant contributors to 
cost are the plant capital and feedstock costs. One of the approved routes for producing SAF is the lipid 
pathway, which can use low-cost feedstock such as fats, oils, and greases. However, lipid routes cannot meet 
the SAF volume demand with the current feedstock supply. New low-cost feedstocks are needed.  
Additional high-fidelity modeling beyond TEA and LCA that examines the resource supply chain at high 
resolution will be valuable to new fuel industry and help set research directions. Note that the model output can 
be quite different as the granularity of the model moves from the national scale to regional and farm scales. It 
is important that the models use the highest resolution (smallest scale) and aggregate up.

Sustainable Aviation Fuel: Review of Technical Pathways 
52 
Finally, connecting the previously described models with key R&D funded in BETO and elsewhere will help 
define cost–value propositions. 
7.2.6 Sequencing R&D to Achieve Impact in the Short, Medium, and Long Term 
Desired short-, medium-, and long-term outcomes of R&D are described in this section.  
Short-term outcomes include reducing the cost of and improving value propositions for fuels already approved 
or far along the ASTM process, or poised to enter the ASTM Fast Track process. These are the only short-term 
options given the length of time to complete the D4054 approval process. 
Medium-term outcomes include expanding opportunities in additional pathways, such as pathways that result 
in cycloalkanes. These will require that candidate molecules be screened and that more information on the 
performance of various classes of cyclic hydrocarbons of various ring size and substitution be collected. In this 
timeframe, there will be more opportunities for feedstocks and better use of all product streams in the jet-fuel-
oriented biorefinery.  
Long-term outcomes include targeted fuel molecules that offer even better fuel properties and higher energy. 
Such molecules may be produced by biological conversion of biomass-based sugars through engineered 
microorganisms, catalytic pathways from sugars and lignin, or a combination of biotechnology and catalysis.  
7.3 Cooperative Opportunities for R&D 
7.3.1 Collaboration Between the National Laboratories 
In the near term, it may be most effective for BETO to start a biojet effort under the existing programs at the 
National Laboratories, including consortia. This will enable a cost-effective leveraging of existing investments 
in terrestrial biofuels and accelerate research progress for SAFs. For example:  
• C
atalysis work to reduce net naphtha loss, improve building up small molecules, and for chemical 
production of cycloalkanes from sugars, lignin, alcohols, and diols can be incorporated into the Chemical 
Catalysis for Bioenergy Consortium. 
• B
iological routes for producing cycloalkane molecules, including terpenoids, sesquiterpenes, or 
ketonides can be incorporated into the Agile BioFoundry. In such an approach, R&D will be necessary to 
reduce cost of production organisms relevant for industrial use and also reduce fermentation and 
separation costs. 
• T
he separations consortium can contribute to process intensification to reduce net capital costs, including 
reactive separations and lowering the cost of removing heteroatoms that will impact catalyst life. 
• T
he Feedstock–Conversion Interface Consortium can support new pretreatments for providing lignin for 
cyclohexanes; a complementary focus on processing mixed wastes that are often wet is also important. 
• D
eveloping structure–activity relationships and retro-synthetic analysis can be helpful.  
7.
3.2 Intersection with FAA Center of Excellence and USDA 
USDA has several exciting feedstock programs that intersect with fuel production, including jet fuel. Forming 
formal relationships with USDA or large projects can reduce redundancy. Likewise, activities in FAA’s Center 
of Excellence, ASCENT (Aviation Sustainability Center), and other programs are important. 
An example of work that could build bridges is related to the ASTM D4054 procedure, which is onerous in 
terms of time and money. There would be great value to the research community if new fuels could be 
prescreened before they are submitted to ASTM for approval at volumes well below the ASTM 100-gallon 
requirement. Further development of Tier 𝛼𝛼 and Tier β tests to achieve more effective prescreening will be 
helpful. Some enhancements to Tier 𝛼𝛼 and Tier β tests could be the use of statistical predictive models to

Sustainable Aviation Fuel: Review of Technical Pathways 
53 
account for uncertainty in the predictions. These prescreening activities could be evaluated at some level with 
the CAAFI R&D committee, both in the development of comprehensive and robust prescreening activities and 
the evaluation of candidate fuels. 
7.3.3 Intersection with North American Partners 
Several synergies and opportunities exist to collaborate in partnerships across North American. Canada, which 
has a high percentage of the worlds certified sustainable forests, and Mexico, which has a warm climate year-
round, both offer unique opportunities for collaboration. 
7.3.4 SAF Working Group 
Finally, there is value creating an SAF joint working group that could include researchers and experts on 
aviation fuels that represent BETO, USDA, CAAFI, FAA, the National Labs, a fuel provider, a biorefinery, 
representatives from an engine OEM, universities, and representatives from Canada and Mexico. The working 
group would have an express charter that could include identifying the R&D needs appropriate for each partner 
and cross-fertilization programs across the agencies. Alternatively, additional focused SAF discussions with 
various stakeholder interests represented that further explore strategies for advancing R&D may add value.

54 
Sustainable Aviation Fuel: Review of Technical Pathways 
References 
Airlines for America. 2018. “Jet Fuel: From Well to Wing.” January 2018. http://airlines.org/wp-
content/uploads/2018/01/jet-fuel-1.pdf. 
Airlines for America. 2020. “Airlines Fly Green.” Accessed April 2020. https://www.airlines.org/airlines-fly-
green/. 
AirNav. 2018. “Local Fuel Prices.” Accessed December 26, 2018. https://www.airnav.com/fuel/local.html.  
Amyris. 2015. “Amyris Achieves Record Low Cost Farnesene Production.” Press release, October 12, 2015. 
https://investors.amyris.com/2015-10-12-Amyris-Achieves-Record-Low-Cost-Farnesene-Production.  
ASTM. 2018. “ASTM D4054 Clearinghouse Guide.” 
https://s3.wp.wsu.edu/uploads/sites/192/2018/03/clearinhouse.pdf. 
ASTM. 2019a. ASTM D1655-19, Standard Specification for Aviation Turbine Fuels. West Conshohocken, PA:
ASTM International. 
ASTM. 2019b. ASTM D4054-19, Standard Practice for Evaluation of New Aviation Turbine Fuels and Fuel 
Additives. West Conshohocken, PA: ASTM International. 
ASTM. 2019c. ASTM D7566, Standard Specification for Aviation Turbine Fuel Containing Synthesized 
Hydrocarbons. West Conshohocken, PA: ASTM International. 
Brooks, K.P., L.J. Snowden-Swan, S.B. Jones, M.G. Butcher, G.S.J. Lee, D.M. Anderson, J.G. Frye et al. 
2016. “Chapter 6: Low-Carbon Aviation Fuel Through the Alcohol to Jet Pathway” In Biofuels for Aviation: 
Feedstocks, Technology and Implementation, edited by Christopher J. Chuck, 109–150. Cambridge, MA: 
Academic Press. 
Bureau of Transportation Statistics (BTS). 2019. “First Quarter 2019 U.S. Airline Financial Data.” 
 
https://www.bts.gov/newsroom/first-quarter-2019-us-airline-financial-data. 
Colket, Meredith, Joshua Heyne, Mark Rumizen, Mohan Gupta, Tim Edwards, William M. Roquemore, 
Gurhan Andac et al. 2017. “Overview of the National Jet Fuels Combustion Program.” AIAA Journal 55 (4). 
Collett, J.R., J.M. Billing, P.A. Meyer, A.J. Schmidt, A.B. Remington, E.R. Hawley, B.A. Hofstad et al. 2019. 
“Renewable Diesel via Hydrothermal Liquefaction of Oleaginous Yeast and Residual Lignin from 
Bioconversion of Corn Stover.” Applied Energy 233–234: 840–853. 
https://doi.org/10.1016/j.apenergy.2018.09.115.  
Collodi, G. 2010. “Hydrogen Production via Steam Reforming with CO2 Capture.” Chemical Engineering 
Transactions 19: 37–42. Accessed September 30, 2018. 
https://pdfs.semanticscholar.org/4bce/0493c6937d4a8e5a844e75e51d5471182a04.pdf.  
Commercial Aviation Alternative Fuels Initiative (CAAFI). 2019. “Fuel Readiness Level (FRL).” 
http://www.caafi.org/tools/Fuel_Readiness_Level.html.  
Csonka, Steve. 2018. “Sustainable Alternative Jet Fuel (SAJF), Progress, Challenges, and Path Forward.” 
Sustainable Aviation Biofuel Work Group Meeting, Seattle, WA, Sept. 17, 2018. 
Davidson, C., E. Newes, A. Schwab, and L. Vimmerstedt. 2014. “An Overview of Aviation Fuel Markets, for 
Biofuels Stakeholders.” Golden, CO: National Renewable Energy Laboratory. NREL/TP-6A20-60254.

55 
Sustainable Aviation Fuel: Review of Te chnical Pathways 
Edwards, J.T. 2017. “Reference Jet Fuels for Combustion Testing.” In 55th AIAA Aerospace Sciences Meeting, 
Grapevine, Texas, January 9–13, 20 17. 
Englund, K., M. Azadfar, G. Schneider, L. Chet a n, and R.P. Samaniego. 2016. “Feedstock Supply Chain 
Analysis – MSW.” Northwest Advanced Renewables Al liance. 
FedEx. 2012. “FedEx Long-Term Commitment to Sustainability Gets a Boost: Emissions Reduction Goal 
Increased Fifty Percent.” Published August 20, 2012. https://about.van.fedex.com/newsroom/fedex-long-term-
commitment-to-sustainability -gets-a-boost-emissions-reduction-goal-increased-fifty -percent/. 
George, A., R. Denny, J. Heyne, and M. Gupta. 2018. “Engine Optimized Sustainable Drop-in JET Hi gh 
Performance Fuels (HPF).” Advanced Bioenergy Le adership Conference , San Francisco, CA, November 6–9, 
2018. 
G
raham, J.L., T.F. Rahmes, M.C. Kay, J.P. Belières, J.D. Kinder, S.A. Millett, J. Ray, and W.L. Vannice. 
2011. “Impact of Alternative Jet Fuel and Fuel Blends on Non-Metallic Materials Used in Com mercia l Aircraft 
Fuel Systems.” Continuous Lower Energy, Emissions and Noise (CLEEN) Project Final Report, July 29, 
2011. https://www.faa.gov/about/office_org/headquarters_offices/apl/research/aircraft_technology/cleen/
reports/med ia/Impact_of_Alternative_Jet_Fuel_and_Fuel_Blends.pdf. 
Gruber, Patrick. 2018. “Realities of Alternative Jet Fuel and What Gevo is Doing.” Advanced Bioenergy 
L
eadership Conference, Washington, D.C., February 28–M arch 2, 2018. 
Harvey, B.G., K.W. Harrison, M.C. Davis, A.P. Chafin, J. Baca, and W.W. Me rriman. 2016. “Molecular 
Design and Characterization of High-Cetane Alkyl Diamondoid Fuels.” Energy Fuels 30 (12): 10171–10178. 
https://doi.org/10.1021/acs.energyfuels.6b01865.  
Hedges & Company. 2020. “U.S. Vehicle Registration Statistics for 2019.” Accessed May 2020. 
https://hedgescompany.com/automotive-market-research-statistics/auto -mailing-lists-and-marketing/ . 
Holmgren, Jennifer. 2019. “Creating a Carbon Smart Future.” 2019 SAF Summit, Seattle, WA, March 7, 2019. 
https://www.portseattle.org/sites/default/files/2019-03/Holmgren_Jennifer.pdf. 
International Air Transportation Association (IATA). 2016 . “IATA Forecasts Passenger Demand to Double 
Over 
20 Years.” IATA Press Release No: 59, October 2016. https://www.iata.org/pressroom/pr/
Pages/2016-10-18-02.aspx.
International Air Transportation Association (IATA). 2018. “Fuel Fact Sheet.” 
https://www.iata.org/contentassets/25e5377cf53c4e48bbaa49d252f3ab03/fact-sheet-fuel.pdf. 
International Air Transport Association (IATA). 2020. “Carbon Offsetting Scheme for International Aviation 
(CORSIA).” Accessed April 2020. https://www.iata.org/en/policy/environment/corsia/. 
International Civil Aviation Organization (ICAO). 2018. “Sustainable Aviation Fuels Guide.” 
https://www.icao.int/environmental-
protection/Documents/Sustainable%20Aviation%20Fuels%20Guide_100519.pdf. 
International Civil Aviation Organization (ICAO). 2019. “Committee on Aviation Environmental Protection 
(CAEP).” https://www.icao.int/ENVIRONMENTAL-PROTECTION/Pages/CAEP.aspx.  
Jouny, M., W. Luc, and F. Jiao. 2018. “General Techno-Economic Analysis of CO2 Electrolysis Systems.” 
Ind. Eng. Chem. Res. 57 (6): 2165–2177. https://doi.org/10.1021/acs.iecr.7b03514.

56 
Sustainable Aviation Fuel: Review of Technical Pathways 
Kosir, S.T., L. Behnke, J.S. Heyne, R.D. Stachler, G. Flora, S. Zabarnik, A. George, A. Landera, R. Bambha, 
R. Denney, and M. Gupta. 2019. “Improvement in Jet Aircraft Operation with the Use of High-Performance 
Drop-in Fuels.” AIAA SciTech 2019 Forum, San Diego, CA, January 7–11, 2019.
Langholtz, M.H., B.J. Stokes, and L.M. Eaton. 2016. “2016 Billion-Ton Report: Advancing Domestic 
Resources for a Thriving Bioeconomy, Volume 1: Economic Availability of Feedstocks.” Oak Ridge National 
Laboratory, ORNL/TM-2016/160. http://doi.org/10.2172/1271651. 
LanzaTech. 2017a. “From Trash to Tank: Upcycling of Landfill to Fuel Demonstrated in Japan.” Dec. 7, 2017. 
https://www.lanzatech.com/2017/12/07/trash-tank-upcycling-landfill-fuel-demonstrated-japan/.  
LanzaTech. 2017b. “IndianOil and LanzaTech sign a Statement of Intent to Construct World’s First Refinery 
Off Gas-to-Bioethanol Production Facility in India.” July 10, 2017. 
https://www.lanzatech.com/2017/07/10/indianoil-lanzatech-sign-statement-intent-construct-worlds-first-
refinery-gas-bioethanol-production-facility-india/. 
LanzaTech. 2018. “World’s First Commercial Waste Gas to Ethanol Plant Starts Up.” June 8, 2018. 
https://www.lanzatech.com/2018/06/08/worlds-first-commercial-waste-gas-ethanol-plant-starts/.  
McVicker, G.B., M. Daage, M.S. Touvelle, C.W. Hudson, D.P. Klein, W.C. Baird Jr., B.R. Book et al. 2002. 
“Selective Ring Opening of Naphthenic Molecules.” Journal of Catalysis 210 (1): 137–148. 
McVicker, G.B., O.C. Feeley, J.J. Ziemiak, D.E.W. Vaughan, K.C. Strohmaier, W.R. Kliewer, and D.P. Leta. 
2005. “Methylcyclohexane Ring-Contraction:  A Sensitive Solid Acidity and Shape Selectivity Probe 
Reaction.” J. Phys. Chem. B 109 (6): 2222–2226. 
National Renewable Energy Laboratory (NREL). 2013. “Biogas Potential in the United States (Fact Sheet).” 
NREL/FS-6A20-60178. https://www.nrel.gov/docs/fy14osti/60178.pdf. 
Olson, D.B., J.C. Pickens, and R.J. Gill. 1985. “The Effects of Molecular Structure on Soot Formation II. 
Diffusion Flames.” Combustion and Flame 62 (1): 43–60. 
Radich, T. 2015. “The Flight Paths for Biojet Fuel.” U.S. EIA, Independent Statistics & Analysis. 
https://www.eia.gov/workingpapers/pdf/flightpaths_biojetffuel.pdf.  
Rumizen, M. 2017. “Alternative Jet Fuel (AJF) Certification.” ICAO Seminar on Alternative Fuels, Montreal, 
Canada, February 8–9, 2017. https://www.icao.int/Meetings/altfuels17/Documents/Mark%20Rumizen%20-%
20FAA.pdf. 
Statista. 2019. “Fuel Costs of Airlines Worldwide from 2011 to 2019, as Percentage of Expenditure.” 
Accessed February 2020. https://www.statista.com/statistics/591285/aviation-industry-fuel-cost/. 
United Airlines. 2018. “Sustainable Fuel Sources.” https://www.united.com/ual/en/us/fly/company/global-
citizenship/environment/sustainable-fuel-sources.html. 
U.S. Energy Information Administration (EIA). 2017. “Total Energy: Monthly Energy Review.” 
https://www.eia.gov/totalenergy/data/monthly/index.php#petroleum. 
U.S. Energy Information Administration (EIA). 2019. “Total Energy: Monthly Energy Review, September 25, 
2019.” https://www.eia.gov/totalenergy/data/monthly/archive/00351909.pdf. 
U.S. Energy Information Administration (EIA). 2020a. “Annual Energy Outlook 2020.” Table 47, Air Travel 
Energy Use. https://www.eia.gov/outlooks/aeo/data/browser/#/?id=57-
AEO2020&cases=ref2020&sourcekey=0.

57 
Sustainable Aviation Fuel: Review of Technical Pathways 
U.S. Energy Information Administration (EIA). 2020b. “July 2020 Monthly Energy Review.” 
https://www.eia.gov/totalenergy/data/monthly/pdf/mer.pdf. 
U.S. Environmental Protection Agency (EPA). 2019. “RINs Generated Transactions.” 
https://www.epa.gov/fuels-registration -reporting-and-compliance -help/rins-generated-transactions. 
U.S. Federal Aviation Administration (FAA). 2013. "Impact of Alte rnative  Jet Fuel and Fuel Blends on 
NonMetallic Materials Used in Commercial Aircraft Fuel Systems." 
https://www.faa.gov/about/office_org/headquarters_offices/apl/research/aircraft_technology/cleen/reports/med 
ia/Boeing_Alt_Fuels_Final.pdf
. 
Weber, Robert S. 2019. “Effective Use of Renewable Electricity for Making Renewable Fuels and Chemicals.” 
ACS Catal. 9 (2): 946–950. https://doi.org/10.1021/acscatal.8b04143.  
Yang, Y, A.L. Boehman, and R.J. Santoro. 2017. “A Study of Jet Fuel Sooting Tendency Using the Threshold 
Sooting Index (TSI) Model.” Combustion and Flame 149 (1–2): 191–205.

Sustainable Aviation Fuel: Review of Technical Pathways 
58 
Appendix 1. Bioenergy Technologies Office Mission 
The BETO mission is to develop industrially relevant, transformative, and revolutionary bioenergy 
technologies to enable sustainable, domestically produced biofuels, bioproducts, and biopower for a 
prosperous nation. 
BETO’s strategic goal is to enable use of America’s abundant biomass and waste resources for advanced 
biofuels, biopower, and bioproducts by: 
• Identifying and developing biofuel pathways and innovative end uses 
• Lowering the cost of production through increased efficiency, productivity, and yields 
• Completing applied R&D on complex, real-world systems and integrating engineering process for 
promising new advanced bioenergy technologies 
• All while maintaining or enhancing economic, environmental, and social sustainability. 
BETO’s performance goals are as follows: 
• By 2022, verify integrated systems research at the engineering scale for hydrocarbon biofuel 
technologies that achieve a minimum 50% reduction in emissions relative to petroleum-derived fuels at a 
mature modeled minimum fuel selling price (MFSP) of $3.00/gasoline gallon equivalent. 
• By 2030, verify integrated systems research at the engineering scale for hydrocarbon biofuel 
technologies that achieve a minimum 50% reduction in emissions relative to petroleum-derived fuels at 
mature modeled MFSP of $2.50/gasoline gallon equivalent.

Sustainable Aviation Fuel: Review of Technical Pathways 
59 
Appendix 2. ASTM Fuel Approval Prescreening Tests 
To evaluate the fuel candidates early to facilitate and reduce risk moving through the ASTM process, one 
could adopt the following:  
• T
ier 𝛼𝛼 testing: Complete a quick preliminary assessment of the opportunity on general properties of 
molecule and class (bulk property composition, modeling, small-scale tests, and contaminants). This 
level of testing will rule out blendstocks prior to ASTM testing and answer questions as simple as “Can 
the proposed blendstock be used at any level?” ahead of platform scaling required for entering the formal 
approval and evaluation process.  
• T
ier β testing: Validate Tier 𝛼𝛼, measuring density, viscosity, and other properties detailed in a CAAFI 
R&D document of fuels at minimal volumes.

Sustainable Aviation Fuel: Review of Technical Pathways 
60 
Appendix 3. Workshop Learnings 
A brief synopsis of the workshop learnings is provided in this chapter. A higher level of detail is provided for 
the Cleveland workshop, as neither a workshop report nor detailed workshop minutes are available to the 
public. 
A3.1 Macon Workshop 
BETO’s Advanced Development and Optimization Program held the Alternative Aviation Fuel Workshop on 
September 14–15, 2016, in Macon, Georgia. The purpose of the workshop was to engage stakeholders to gain 
additional knowledge related to aviation biofuels production. Input was sought specifically for effort needed 
to: (1) develop technology for scalable production, (2) achieve economic competitiveness, (3) achieve 
environmental benefits, and (4) develop feedstock and supply chains for biojet fuel deployment.  
Key findings from the plenary presentations noted common characteristics of successful biojet pathways. 
These include the need to make fuel in sufficient quantity to study blending impacts and to develop strategies 
for scaling up. Forward-looking TEA methodology to understand profitability competitiveness drivers and 
stable government policies were also identified as essential capabilities required for the success of any 
pathway.  
The breakout session on economic and technical competitiveness identified the need to develop consistent 
TEA methodology (in partnership with CAAFI, FAA, and other stakeholders) that considered both nth-plant 
and near-term, early-adopter economics. The TEA can inform the highest scale-up risks and barriers and point 
to further R&D needs. 
The session on fuel conversion and scale-up identified technical barriers ranging from a lack of availability of 
data on pathways; lack of access to equipment, low-cost feedstocks, capital, and expertise; and lack of time 
and investment required for ASTM certification. More than 20 pathways were identified as having a need for 
DOE support for preliminary evaluation. Nontechnical needs were also identified, such as public education on 
the benefits of SAFs, consistent policies, and regulations. 
The session on environmental sustainability and life cycle benefits provided insights for a consistent approach 
to sustainability analysis and LCA, as well as metrics for these analyses. Participants wanted researchers to 
understand that transparency be achieved by publication of these tools and assessments for use by 
stakeholders. 
The session on feedstock and product supply chains identified a lack of sufficient feedstock availability and 
limited scaling as barriers, as well as the need for a better understanding of best practices, particularly for new 
and emerging feedstocks. Attendees provided insights into the importance of DOE collaboration with USDA 
and other stakeholders to further enhance feedstock development and explore opportunities such as double 
cropping to increase efficient use of land and nutrients. Other insights included BETO playing a strong role in 
feedstock interface opportunities to help reduce the risks related to feed and handling at the biorefinery and 
improve the performance of the conversion process through integration of feedstock and fuels production. 
Key takeaways from the Macon workshop related to the timeline, markets, and research needs were as follows: 
Timeline 
• F
or 0–5 years, near-term R&D investment needs to reduce the cost in pathways already approved or near 
certification. 
Ma
rkets

Sustainable Aviation Fuel: Review of Technical Pathways 
61 
• J et fuel properties fall within the light end of the diesel envelop e; therefore, biofuels companies could 
sell into either market.  
• D
iesel fuel (ground transportation) is major competition for fats, oils, and greases. Light ends could offer 
blending opportunity to meet bulk properties.  
• L
ipid routes (fats, oils, and greases) are not likely to meet the SAF volume demand.  
• P
olicies that allow a level playing field will be helpful. 
• O
fftake agreements are necessary but not sufficient; the cost must come down, as offtake agreements 
kick in only when production is established.  
R
esearch Opportunities 
• Ad
ditional benefits for SAFs may be related to the low sulfur and low aromatics in SPK. 
• Ne
w low-cost sources of feedstocks, including lignocellulosics, are needed to increase scale. 
• T
EA and GHG results are inconsistent; there is a need to improve consistency and cover pioneer plants. 
Additionally, TEA can identify the greatest cost-reduction opportunities. 
A3.2 Cleveland Workshop 
The JET workshop was held in Cleveland, Ohio, from September 21–22, 2017. The workshop was a 
perspective-gathering and brainstorming event organized around four themes: (1) high-performance fuel 
options, (2) engine and combustor options, (3) aircraft on-board considerations, and (4) fuel development to 
deployment considerations. The event was organized by EERE, the U.S. Department of Defense, and NASA. 
In attendance were 75 people and another 25 people participated by webinar.  
A3.2.1 Two Schools of Thought 
Two divergent schools of thought were discussed during the workshop. One was to work within current 
standards (drop-in fuels) but bring the cost down. This approach avoids the expense of changing the 
infrastructure for distribution, fueling, and use, and the exorbitant cost of FAA engine (re)certification. The 
challenge for large-scale adoption is the high cost of SAF versus petroleum-derived jet fuel and not inferred 
impediments, low blending limits, limited pathways, or low-volume production capability.  
The second, alternative school of thought was to imagine what a fuel–engine combination could look like if all 
constraints were removed (non-drop-in fuel/engine combination). Those proposing the non-drop-in fuels 
discussed value propositions rather than cost.  
In the middle of these two schools of thought are considerations of how engines are evolving and what fuel 
properties are important. In this scenario, a fuel could still meet current (or perhaps lightly modified) ASTM 
specifications.  
Drop-in fuels are needed for near- and mid-term opportunities. There may be opportunities for commercial 
aviation for non-drop-in fuels in the long term, but even they will likely be bounded by high-energy-content 
hydrocarbons rather than single-molecule-based fuels, two-fuel concepts, metals, or gaseous-based fuels.  
Drop-in fuels allow uncoordinated growth of SAFs and are forwards–backwards compatible. Non-drop-in 
fuels would require a system-level coordination and it is unclear how deployment could or would proceed.  
A3.2.2 High-Performance Fuel Options 
High-performance fuel evaluation can revolve around emissions and operability (lean blowout, cold ignition, 
altitude relight). This can be done by removing some components from the fuel and biasing critical fuel

Sustainable Aviation Fuel: Review of Technical Pathways 
62 
properties. ASTM D1655 already enables improvements in jet fuel, such as higher energy content (optimizing 
specific energy and energy density without driving either to nonviability), higher heat capacity/thermal 
stability, lower sulfur and lower aromatics, lower freeze point, and others. The cost–benefit tradeoff must be 
significant if the fuel is more expensive. The question becomes whether or not there is a path for relaxing (or 
refining) the current fuel specification without engine recertification. 
Suggestions from the workshop include that fuels must be single-phase hydrocarbons; multiphase fuels are not 
allowed in civil aviation, oxygen is unwanted, and metal-based fuels are not acceptable. While a specific single 
molecule may exist that meets ASTM specifications, it is unlikely such a fuel would have the required 
performance to ensure safe operation over the wide range of conditions during flight. Moving to a narrower 
suite of molecules will need to be understood in terms of combustion characteristics and may require engine–
fuel co-optimization. 
In the near term, the low-hanging fruit is producing fuels with higher thermal stability, improved lubricity, 
high density, and improved specific energy (higher H:C ratio) while retaining acceptable energy density and 
higher thermal capacity (enabling thermodynamic efficiency, higher vapor pressure, lower viscosity, and lower 
surface tension, and bounding the cetane number [30–55]). Lowering aromatics and eliminating heavy-end, 
multi-ring aromatics is critical for reducing emissions, lowering infrared thermal load (hot spots), and 
improving specific energy. Use of certain cycloalkanes, such as decalins, could be a route to removal of 
aromatics while maintaining O-ring swelling. Alternatively, small olefins, such as ethyl benzene, have good 
swelling properties and lower sooting than heavier aromatics. 
In the medium term, options can be considered to blend noncompliant blendstocks from multiple feedstocks 
and pathways to achieve a renewable blend that is both compliant and meets performance targets. 
Developing new fuels, perhaps with the help of additives, could drive down soot, make fuel easier to ignite, 
reduce surface tension, and inhibit Zeldovich NOx (by facilitating better premixing, and in turn lower 
combustion temperatures). Other desired properties include lower viscosity and surface tension, higher thermal 
stability, and no aromatics, nitrogen, sulfur, olefins, or oxygen compounds.  
Discussion of flexible-fuel and dual-fuel engines was prevalent. Flexible fuels will require material 
compatibility; dual fuels will require additional tanks, lines, and fuel pumps on aircraft. In addition, on-
boarding fuel reforming was heavily discussed. Fuels that are not fully backward compatible will require a 
separate fueling (hydrant) infrastructure. Additives could assist in allowing backward–forward compatibility.  
In closing, optimizing jet fuel is a multivariate, multi-stakeholder activity. Altering one property can affect 
others, at times negatively. Next steps would be to determine optimization metrics and a holistic set of 
operability and safety constraints. 
A3.2.3 Engine and Combustor Options 
Engines are certified to run on a fuel, showing a critical tie between engines and fuels. The clarion call of fuel 
producers and engine/airframe manufacturers to work together is exemplified in the following quotations from 
the JET workshop:  
It is clear that there still remains a lack of understanding of the link between fuel physical and 
chemical properties and combustion performance. While some correlations do exist, a more complete, 
physics-based description is lacking. Furthermore, without having appropriate models to accurately 
predict combustion processes as a function of variation in combustor geometry or fuel properties, the 
probability of co-optimizing fuel formulations and combustor designs synchronously is low. 
[There is a] tremendous potential and opportunity if a will exists to pursue it.

Sustainable Aviation Fuel: Review of Technical Pathways 
63 
To achieve higher efficiency and lower emissions in the Brayton cycle, engines are moving to higher 
compression ratios and more premixing. Lower fuel burn is achieved by improving thermodynamic cycle 
efficiency.  
Engines will continue to evolve, including higher pressure ratios, higher temperature and pressure at the inlet, 
lower parasitic (cooling) air flow, advanced materials/coatings, higher heat rejection to the fuel system, and 
advanced seals and avionics. These changes require improved thermal stability and low contaminants in the 
fuels. Reducing emissions requires reduced variation in temperature and could change fuel/air mixing, 
coupling heat release to pressure, the position of the flame front, and links of chemicals to emitted species.  
It takes 15 years to develop an engine from scratch, and 15 years to develop a new airplane. It also takes about 
15 years to move a new fuel market from discovery to pilot to production. All of these activities must be done 
in parallel. Hence, three questions arise: What enabling technologies are needed to begin developing now? 
How early in the engine/aircraft development cycle is fuel mandated? What aircraft in development could 
benefit from new fuel specification?  
Table A.1 illustrates the relationships of select fuel properties and engine performance parameters. Linkages of 
fuel properties with engine operability and performance metrics are clarified where known. Because many of 
the fuel relationships are unknown, the table points out areas of potential future engine-fuel research. The 
dominant properties for which research is necessary are vapor pressure, viscosity, thermal stability, and 
aromatic content. 
Reduction of fuel viscosity at low temperatures as well as increased thermal stability of the fuel may require 
improved nozzle designs in terms of uniform and finer spray performance, broader operating space, and 
cheaper/simpler designs.  
Autoignition under high compression ratios with well-mixed fuels needs to be addressed. Nozzle design is one 
tool to address the challenge. Nozzle geometry changes under varying conditions experienced during takeoff 
and flight. The active geometries of flexible-fuel airplanes could account for the variation. Injector design 
needs to be investigated, as well as on-board, real-time fuel sensors for measuring critical property deviations.  
Table A.1. Fuel Properties from the OEMs at the JET Workshop 
 
Vapor 
Pressure 
(Evap. 
Rate) 
Viscosity Density (mass) Density (volume) Ignition Time Heat of Combustion Thermal Stability (Coking) Aromatics Extinction or High Temp. Chem. (kinematic rates) H:C Ratio 
Durability: 
Low soot 
(combustor 
and turbine) 
(soot) + (soot) − Wash Wash (Auto-ignition) − Wash + (soot/ radiation) − Wash Wash 
Dynamics Non-monatomic behavior 
Coking 
(injector) - low 
O2 
Wash Wash Wash 
(drives 
velocity of 
fuel up) − 
Wash Wash + − Wash Wash 
Coking 
(combustor) * + * (not universal) Wash Wash Wash Wash Wash Wash Wash Wash 
Forced ignition + − Wash Wash Wash Wash Wash ? Wash Wash 
Lean blow out 
(LBO) Depends Depends Wash Wash ? Wash Wash Wash (fast) + Wash

Sustainable Aviation Fuel: Review of Technical Pathways 
64 
 
Vapor 
Pressure 
(Evap. 
Rate) 
Viscosity Density (mass) Density (volume) Ignition Time Heat of Combustion Thermal Stability (Coking) Aromatics Extinction or High Temp. Chem. (kinematic rates) H:C Ratio 
NOx + − Wash Wash Wash Wash Wash Wash Wash Wash 
CO/unburned 
hydrocarbon 
(UHC) 
+ − Wash Wash ? Wash Wash Wash (fast) + + 
Soot/smoke/ 
particulate 
matter (PM) 
+ − Wash Wash Wash Wash Wash − ? + 
Temp. profile/ 
pattern  Flat + Flat − Wash Flat + Wash Wash Wash Wash Wash Wash 
Key 
− Down for improvement Depends Depends on design 
+ Plus for improvement P Peak 
* Additional debate   Big effects 
? Do not know    Smaller effects  
Variable geometric features with two or more mixer inlets allow active control of near-dome flow 
characteristics to meet the required performance, emissions, operability, and durability objectives. Fuel that 
does not coke allows for smaller injector nozzle orifices and thus finer spray. Less coking also allows staging 
of other functions. Lower coking fuels require very low olefins and heteroatoms. Aromatics have second-order 
coking effects.  
R&D topics may include real-time fuel sensors, analysis (understanding of sprays, computational fluid 
dynamics, acoustical instabilities, etc.), development of single-cup rigs requiring very small fuel quantities 
(initial screening), and identification of highly targeted additives that improve fuel properties. Alternative fuel 
producers can collaborate with OEMs to understand the unique engine types/cycles that could be optimized 
with a new fuel. 
A3.2.4 Aircraft On-Board Considerations 
Airplanes integrate all subsystems, including engines, auxiliary power units, tanks, and fuel delivery systems. 
At the airframe level, critical fuel properties include material compatibility for pumps (lubricity, viscosity), 
tanks (flash point, vapor pressure), fuel quantity indicating system (dielectric, speed of sound, density), and 
energy capacity/energy density. All the auxiliary aircraft systems that touch the fuel will need to be evaluated 
in the presence of the new fuel. Fuel system considerations include water solubility; a small level is needed to 
prevent ice-crystal formation during flight and low-aromatic fuels may require additives. For airports, airlines, 
and the military, fire suppression for unintended ignition and water in the fuel lines is a major issue.  
SAFs that are not drop-in would require that legacy engines and aircraft be recertified. For a new engine and a 
new plane, this may be less of a problem if the new fuel properties are understood prior to ASTM certification 
of the engine and plane, and if a duplicate fueling system is available at every intended destination.  
As stated in Chapter 3.2 of this report, drop-in fuels encourage supply growth. Non-drop-in fuels might feature 
potentially better performance and operability but will require system-level coordination along the entire value

Sustainable Aviation Fuel: Review of Technical Pathways 
65 
chain to ensure their compatibility with all parts that the fuel touches, and with how engines and planes are 
certified by the FAA.  
In the near term, SAF fuels that include additives, such as ethyl benzene for ring swelling, offer advantages. 
Material compatibility is going to be crucial for both the near and longer term. Many remaining unknowns 
about new fuels will need to be addressed. Chapter 2 offers an extensive list of important fuel properties. 
In the medium and longer term, swelling remains a concern for blend limits of SAF fuels that have minimal 
aromatic content, and lubricity is a concern with ultra-low-sulfur fuels. Identifying additives or blendstocks 
that assist with these properties is a research need. For example, certain cycloparaffins, such as decalin, may 
offer swelling properties. Trace levels of organic acids may increase the lubricity. An understanding of trace 
components in fuel today that lead to lubricity would be valuable. An understanding of the effect on engine 
components is also needed. 
Considerations for different phases of flight and specific energy/fuel requirements led to many discussions of 
the dual-fuel option under consideration. In such scenarios, landing and takeoff (drop-in) have different 
requirements than cruising (non-drop-in). While a dual-fuel option could improve aircraft performance 
(weight, cost, etc.), its performance benefits are offset by the complexity of the additional fuel system 
requirements (multiple tanks, lines, pumps, control, etc.). Further, use of a dual-fuel option requires the system 
and logic to switch between fuels versus mission segments. Concern about producing fuel flow spikes in 
switching will need to be addressed. Plumbing and pumping compatibility issues for each fuel will need to be 
understood, as will the risk profiles, which depend on the diversity of fuel types, logistics of fuel densities such 
as fuel gage issues and weight distribution, misfuelling, and complexity and redundancy of units. Therefore, 
when considering dual-fuel options, a thorough risk−benefit analysis must be done before investing public 
research dollars.  
In the extended long term, NASA is looking at partial to full electrification for mission-specific aircraft. This 
extends to considerations in commercial and cargo settings in which electricity is generated in flight and used 
in a hybrid concept. Which fuels could help enable hybrid engines is uncertain at this point. 
A3.2.5 High-Performance Fuel Development to Deployment 
Value chain buy-in: Scale-up and deployment of a new fuel, even a drop-in fuel, requires the participation of 
many entities along the value chain—from the feedstock providers (farmers, waste owners, foresters), fuel 
blenders, fuel distributors and suppliers, airports and airlines, financers, communities (where fuels is produced 
and used), and, finally, consumers. Each stakeholder group needs to see a financial benefit or at least a 
perceived societal or other long-term benefit. This was discussed in more detail during the Richland workshop; 
scaling up deployment often cannot withstand antagonists, who can kill the venture. 
Financing: Scaling up a new fuel facility requires extensive capital. The ability to acquire funding becomes 
increasingly challenging because the scale increases until risk has been mitigated, which may be after the 
pioneer plant or even subsequent plants have been established. Development of a new fuel without a clear line 
of sight for its use expressed through long-term purchase agreements is exceedingly challenging. For non-
drop-in fuels, a full set of partners will need to buy in. The value added (for both drop-in and non-drop-in) will 
have to be unambiguous and sufficient to overcome the risk. This message was made even stronger at the 
Richland workshop. 
Regulatory framework: Regardless of SAF sourcing, there is a need to work within a technology-neutral 
regulatory framework that can encompass new fuels and additives without legislative change. Few new clean-
energy ventures can move to market without a favorable regulatory framework. Three elements must come 
together: stable policy environment, de-risked technology, and acceptable economics. 
For near- and mid-term opportunities, infrastructure compatibility is important (i.e., the same pipelines, fuel 
delivery, tanks, and engines). Fuels streams can be differentiated to provide benefits, and the net benefit must

Sustainable Aviation Fuel: Review of Technical Pathways 
66 
offset costs throughout the value chain. A system-level approach is essential to understanding tradeoffs and 
upstream and downstream impacts. The regulatory framework must also be technology-neutral while 
incorporating market-based solutions that address society’s needs (e.g., California Low Carbon Fuel Standard 
versus the Renewable Fuel Standard of the Energy Independence and Security Act). Regulatory frameworks 
that incorporate market-based solutions that also address society’s needs will be helpful.  
There are two issues to consider in meeting the fuel specifications of ASTM D1655 (current specification). 
First, engine manufacturers do not have significant incentives to assume additional risks associated with 
certification outside of ASTM D1655. Barriers and limitations for deployment are determined by the need for 
the fuel to be drop-in. The fuel must comply with ASTM D1655. Second, the fuel must be within spec when it 
arrives at the airport (via pipeline, rail, truck, or barge). Blending offers opportunities to improve properties or 
to bring an out-of-spec fuel into spec. While blending is not the inhibitory challenge for large-scale production 
today, at large-scale production, who is responsible for quality assurance and how and where that is done will 
need to be addressed. Consumer infrastructure and maintenance need to be developed (developing proper 
metering blending infrastructure and seals). 
Timing: At the workshop, it was suggested that the timing of scaling up jet fuel pathways may be as follows: 
• S
hort term: HEFA, fat, and greases are commercially available today but limited in feedstock quantity 
(e.g., commercial today, but need cost reduction) 
• M
edium term: Waste gases, MSW, and agricultural waste can be used as feedstock (e.g., pathways that 
are in piloting or demonstration today) 
• L
ong term: Algae, hybrid technology, thermo-catalytic, and direct CO2 utilization (e.g., technologies at 
bench scale today). 
F
uture fuels could be built if existing knowledge and experience are used. 
A3.2.6 Key Takeaways 
There may be tremendous opportunity for high-performance SAF, but it will take time and money and can 
only be done with the integration of engine and fuel research. 
• T
ime: It takes 14–19 years from technology development through product introduction phases (for 
planes, engines, and fuels); hence, collaboration and how to work together is key. 
• M
oney: General Electric spent over $500 million to get GEnx-09 into production from development (an 
expensive and resource-intensive process); fuels have a similar price tag, so there is need to focus on 
lowering costs of existing fuels in the near term. 
• E
xpect engine design not to change significantly; plan for staged combustion to meet varying loads and 
reduce emissions. 
• O
pportunities exist to improve specific fuel consumption (increase payload or range or reduce takeoff 
weight) using high-energy-content fuels with existing engines (existing engines can use up to 15% 
higher energy-dense fuels). 
A3.3 Richland Workshop 
The Trilateral Biojet Workshop brought together researchers from Canada, Mexico, and the United States. 
Held in Richland, Washington, in May 2018, the workshop was organized by EnerCan, SENER, and DOE, and 
was funded by DOE and PNNL. The workshop covered the value chain, feedstock from each country in North 
America, research directions in each country, and how collaboration can be used to accelerate ATJ growth.

Sustainable Aviation Fuel: Review of Technical Pathways 
67 
The workshop report covers six areas: (1) what makes a great jet fuel, (2) ecosystem and the current state, (3) 
capabilities and programs in each country, (4) needs and research opportunities in the near term (0–5 years), 
(5) needs and research opportunities in the longer term (beyond 5 years), and (6) Canada, Mexico, and the 
United States working together.  
A3.3.1 Synopsis of the Workshop Report 
The workshop covered what is in current jet fuel, jet fuel markets in each country, and the ASTM process, as 
well as the FAA engine–airplane certification process. Many of the learnings have been covered previously in 
Chapter 1 of this report and are not repeated here. FAA does not certify fuels, but rather engines and airplanes 
that operate using a specified fuel. In the United States and throughout North America, the specified fuel is 
defined by ASTM. Testing has shown that blending reduces emissions and contrail size because of the 
reduction of aromatic content, hence there is no reason for SAF to mimic Jet A. Starting with renewable 
carbon, one can target the hydrocarbon families of highest value.  
The relatively low amount of SAF produced today in comparison to biodiesel and renewable diesel is sobering 
and indicative of challenges that producers face in the competition of the two markets. While airlines are 
seeking sustainable alternatives to petroleum-derived fuels, the cost of the fuel remains a critical driver. The 
cost of fuel between 2011 and 2019 range from 19% to 32% of the expenditures for airlines (Statista 2019). 
The Bureau of Transportation Statistics reported fuel costs being nearly 20% of the operating cost of U.S. 
airlines in 2019. (BTS 2019). At the workshop, one representative of a major airline noted that a single dollar-
per-barrel increase in jet fuel price equates to a $50-million increase in operating cost. Airlines are sensitive to 
the price of fuel. 
A3.3.2 Key Takeaway Messages 
• T
he time and cost of bringing a new fuel to market must account for the time and cost of fuel 
certification (4 years) and the time and cost through piloting to pioneer plants. 
• S
AF must be cost-competitive. The airlines cannot meet their self-imposed targets for reducing GHG 
emissions based on engine and flight improvements alone; they need biojet fuel, yet fuels are up to 30% 
of the operating cost.  
• S
ome airports are looking to help meet the difference on cost by being fuel integrators, combining larger, 
long-term purchase agreements (from the airport level, not the airline level) and providing land to 
produce biofuels. Europe has similar models that could be followed (the Oslo model is creating a central 
fund to bridge the difference between the cost of production and market value). 
• F
uels are delivered in hydrant systems in which LCA accounting is attributed to those who pay for it. 
Refineries ask if a similar accounting could be done for coprocessing even if jet fuel is not a product. 
(How does one draw the box around the LCA?) 
• F
eedstock cost must be reduced. 
• P
roducers need to make coproducts; however, fuel cannot be a loss leader in the long term.  
• M
arkets span international boundaries and coordination needs to cross countries.

For more information, visit: energy.gov/eere/bioenergy
DOE/EE–2041  •  September 2020
Cover photo from iStock 485632268
BIOENERGY TECHNOLOGIES OFFICE
