# Step13 — W3C SOSA/SSN 2017 Recommendation original-vocabulary audit

**6 November 2026 · Bounded research Step13 only. Six existing W3C correspondences original-source-checked, twelve native-source leads held. No adopted DIM/Profile change.**

**Original authority:** World Wide Web Consortium (W3C), *Semantic Sensor Network Ontology*, W3C Recommendation, **19 October 2017**, [permanent edition](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/). This Recommendation documents both the lightweight Sensor, Observation, Sample, and Actuator (SOSA) vocabulary and the richer Semantic Sensor Network (SSN) ontology. It is a W3C Recommendation from a joint W3C/OGC working group, **not** The Open Group's distinct SOSA architecture standard.

## 1. What the original vocabulary means for the DIM

The central distinction is between an **abstract System**, a **hosting Platform**, a **reusable Procedure**, a **Sensor** capable of performing sensing, and an **Observation** representing an actual act. These roles are not interchangeable even when one physical instrument may be involved in several. Original source terms are OWL classes or relationships, not automatically literal JSON fields or CSAPI HTTP resources.

We retained the six candidate correspondences at their prior row positions, reviewed their original 2017 definitions and added precise section locators and boundaries. The two narrowly matching row meanings remain DIRECT and the other four remain PARTIAL. A direct analytical alignment in this workbook is **not** an RDF owl:equivalentClass assertion, a complete ontology transformation or adopted DIM requirement.

## 2. Six existing correspondences rechecked

| Proposed DIM information element | W3C 2017 native term | Mapping decision | Original source | Boundary |
|---|---|---|---|---|
| S06-R005 — Described sensing System / arrangement | `ssn:System` | **PARTIAL** | §4.9.2.4 ssn:System; §4.9.2.5 ssn:hasSubSystem | Does not itself define a single physical enclosure, installed station, deployed serial asset, CSAPI System resource or complete hardware bill of materials. |
| S06-R009 — Hosting platform / station context | `sosa:Platform` | **PARTIAL** | §4.9.2.1 sosa:Platform; §§4.9.2.2–4.9.2.3 hosts/isHostedBy | Hosting or mounting is not physical-part containment; a station coordinate cannot establish an individual probe point or original installation history. |
| S06-R010 — Observing procedure / method | `sosa:Procedure` | **PARTIAL** | §4.8.2.1 sosa:Procedure; §4.8.2.2 usedProcedure; §4.8.2.3 ssn:implements | It covers more than observing, and its declaration does not prove a historic procedure execution or effective on-device configuration. |
| S06-R013 — Observed / observable property | `sosa:ObservableProperty` | **DIRECT** | §4.3.2.1 sosa:ObservableProperty; §4.3.2.3 sosa:observedProperty | A property is neither its numeric result nor a physical PM sensor module; temperature of an enclosure panel is not necessarily ambient air temperature. |
| S06-R014 — Observer / observing System | `sosa:Sensor` | **PARTIAL** | §4.3.2.5 sosa:Sensor; §4.3.2.9 madeBySensor; §4.3.2.6 observes | Not necessarily one physical probe, logger, reported stream, or identifiably authenticated performer of Bennett's historical 15-minute mean. |
| S06-R015 — Performed Observation | `sosa:Observation` | **DIRECT** | §4.3.2.2 sosa:Observation; §§4.3.2.3–4.3.2.4; §4.3.2.9 | A manufacturer example is not an executed Observation; copying two NOAA source events into four API records does not create four original acts; original resultTime remains UNKNOWN. |

All six cells now carry original Recommendation source locators and the explicit verification grade `W3C_2017_RECOMMENDATION_ORIGINAL_VOCABULARY_CHECKED_DIM_RELATION_PROPOSED`. Every primary-source locator is in [W3C Recommendation sections 4.3, 4.8 and 4.9](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/); the matching evidence sheet retains native class, edition, semantic relation, limitation and review date.

## 3. Twelve original 2017 concepts / associations held for later reconciliation

| Lead | Source-native concept | Original clause | Why not inserted as a new DIM row |
|---|---|---|---|
| W3C-H01 | `ssn:hasSubSystem` | §4.9.2.5 | Relates System to component System, but physical-part completeness and assembly hierarchy do not automatically follow. |
| W3C-H02 | `sosa:hosts / sosa:isHostedBy` | §§4.9.2.2–4.9.2.3 | Hosting and mounted-on roles must not be silently converted to material containment, point coordinates or time-dated service. |
| W3C-H03 | `ssn:Deployment / deployedSystem / deployedOnPlatform` | §§4.9.2.6–4.9.2.10 | A deployment description does not establish the exact Bennett EE181 exchange minute, verified sensor site point or current state. |
| W3C-H04 | `sosa:usedProcedure / ssn:implements` | §§4.8.2.2–4.8.2.4 | A reusable method, implementation capability, and actual historical procedure execution are different claims. |
| W3C-H05 | `ssn:hasInput / ssn:hasOutput / ssn:Input / ssn:Output` | §§4.8.2.5–4.8.2.8 | Procedure input/output information is not necessarily a logger telemetry field, network endpoint or addressed transducer channel. |
| W3C-H06 | `sosa:FeatureOfInterest / sosa:hasFeatureOfInterest` | §§4.6.2.1–4.6.2.2 | Observed ambient air, sensor hardware, physical station and station coordinate are not the same feature. |
| W3C-H07 | `sosa:Result / hasResult / hasSimpleResult` | §§4.7.2.1–4.7.2.4 | Observation result instance/value differs from an output-field definition, observation act, and copied project representation. |
| W3C-H08 | `sosa:phenomenonTime` | §4.3.2.4 | Time of applicability may be an interval for a mean, and differs from resultTime; do not invent exact Bennett interval boundaries. |
| W3C-H09 | `sosa:resultTime` | §4.7.2.5 | Result-completion instant for original NOAA record is UNKNOWN; must not substitute retrieval time or project API publication time. |
| W3C-H10 | `sosa:madeBySensor` | §4.3.2.9 | Original mean-producing Sensor attribution cannot be asserted from station listing or associated probe inventory alone. |
| W3C-H11 | `ssn-system:SystemCapability / inCondition / OperatingRange` | §§5.1.2.2–5.1.2.21 | Capability and operating-range declarations are not measured present battery state, diagnostics, or verified operating conditions. |
| W3C-H12 | `sosa:Actuation / sosa:Actuator / sosa:madeActuation` | §§4.4.2.2, 4.4.2.5–4.4.2.7 | Actuation as world-changing activity must not be equated to a Command request, acknowledgement, success code, or measured effect. |

These twelve entries are **selected source-confirmed leads**, not an exhaustive list of everything in SOSA/SSN, and not twelve new DIM obligations. Several could justify new rows, splits or relations when the source-and-case synthesis is authorized later. For this bounded step, they remain on an audit sheet to prevent loss or invented equivalence.

## 4. Four equipment-case sanity checks

**Dragino S31-LB.** The manufacturer describes a cabled SHT31 probe able to report temperature and humidity. That design does not itself prove an individual installed `sosa:Sensor`, an actual `sosa:Observation`, or a performed 2017 `ssn:Deployment`.

**AirGradient Open Air Max.** Two installed-in-reference-design PMS5003 modules and three particulate-property outputs are different kinds of information. `sosa:ObservableProperty` concerns a characteristic of a feature, while `ssn:hasSubSystem` concerns the relationship between Systems; the ontology does not turn each output into a physical sensor.

**Campbell CR1000X and ClimaVue 50.** A 14-position ClimaVue response and an independently published 31-field logger Status example cannot be treated as 45 individual Sensor systems or 45 actual Observations. The publisher examples do not prove a joined operating installation or historical procedure execution.

**Bennett's Point.** The real historical `acebpmet` station has two documented EE181 serial-numbered probes over three dated service role statements, and two original NOAA ATemp means represented by four project API copies. The 2017 `sosa:Observation`, `sosa:madeBySensor`, `ssn:Deployment`, `sosa:phenomenonTime` and `sosa:resultTime` concepts can help distinguish them; they do **not** supply the unknown original result-completion time, producing Sensor identity, exact probe change minute, or surveyed probe coordinate.

## 5. 2026 draft is separate — do not silently merge editions

The [4 November 2026 *Semantic Sensor Network Ontology – 2023 Edition*](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261104/) is still a **W3C Working Draft**, not the 2017 Recommendation. Its own change-history annex explicitly identifies proposals such as new `Execution` and `Asset` superclasses, collection concepts, observing-procedure specialization, OMS/CSAPI alignments, and a reworked System Capabilities module. Those are recorded as **later-draft leads only** and contribute **zero** original-2017 donor mappings in this Step13 pass.

This edition separation matters because the proposed 2026 ontology is changing structure and alignments while this workbook is still discovering our DIM from independent donor evidence. The draft's publication date does not retroactively change the definition, modeling standing or authority of the permanent 2017 Recommendation.

## 6. Changes, preserved evidence and technical limits

The six W3C/SSN cells were source-qualified in the new structured master; **zero** new donor rows, **zero** adopted DIM rows, **zero** Profile rules and **zero** external implementation claims were made. **Fifty-seven donor records** remain: **37 original-source-checked** (CSAPI 12, SensorML 10, SWE Common 4, OMS 5, W3C 6) and **20 other prior-only** (IEEE 5, OPC 6, SAPIENT 9). The 13 accepted column positions, six dividers, 22 proposed DIM rows, nine case-only holds and 73 case statements survive without reclassification.

The previous v0.6 source JSON carried a stale `counts.otherDonorCellsUnverified=31` despite the actual record count being 26 before Step13. The v0.7 value is corrected to 20 after qualifying the six W3C cells, and is computed/checkable from the individual 57 evidence records. This is a bookkeeping correction, not an extra donor review.

**No** original Observation encoding/conformance, manufacturer/NOAA issuer authentication, external W3C ontology reasoner pass, physical device Command, Cloudflare redeployment, app code, server resource or adopted CSAPI Profile resulted.

## 7. Sources

World Wide Web Consortium (W3C). 2017. *Semantic Sensor Network Ontology.* W3C Recommendation, October 19. https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/

World Wide Web Consortium (W3C). 2026. *Semantic Sensor Network Ontology – 2023 Edition.* W3C Working Draft, November 4. https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261104/

## 8. Next controlled iteration

**Step13 source decisions complete; next distinct owner “proceed” is Step14 IEEE 1451/TEDS only.** Consult public technical/NIST Playground evidence at the actual inspected edition and keep uninspected proprietary 2024 normative clauses on explicit hold. Do not begin ISA Step15 or alter the final donor ranking by default.
