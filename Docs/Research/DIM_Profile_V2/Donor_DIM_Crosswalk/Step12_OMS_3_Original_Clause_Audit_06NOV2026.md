# Step12 — Original-source review of OGC OMS 3.0

**6 November 2026 · Bounded technical Step12 only · Five original OMS concepts verified and qualified; twelve additional native-source leads held.**

**Published source:** [OGC 20-082r4, *Observations, measurements and samples*, version 3.0.0](https://docs.ogc.org/as/20-082r4/20-082r4.html), published **26 May 2023**. The standard is an **OGC Abstract Specification** on the observation conceptual and logical model, aligned with ISO 19156:2023. It is **not** itself the JSON encoding/schema defined by SensorML or SWE Common, and this audit performed no source-to-client execution test.

## 1. What actually matters

OMS draws a particularly useful line between four roles. An **ObservableProperty** is the characteristic of the feature being studied. An **ObservingProcedure** is the reusable method used to find its value. An **Observer** is the specific actor capable of performing that method—possibly an instrument, algorithm or person—while an **Observation** is the actual act that produces a result. A **Host** is a grouping of Observers, often a platform or monitoring facility, but not necessarily a distinct manufactured physical assembly.

This helps the DIM because our rows for *Observer / observing System* and *Hosting platform / station context* currently cover broader meanings than OMS's formal concepts. We therefore keep those correspondences **PARTIAL**, rather than implying that a CSAPI System, a physical sensing probe, the producing logger, a reporting server and an OMS Observer or Host always name the same thing.

## 2. Five existing OMS correspondences checked at their original clauses

No new OMS mappings were inserted into the 22 proposed DIM rows. Each existing OMS cell was source-reviewed, the precise native role was clarified, and the original clause and non-equivalence warning were recorded in the structured source ledger and workbook **OMS Clause Audit** worksheet.

| Proposed DIM element | Native OMS concept | Relation | Original clause | Boundary we must preserve |
| --- | --- | --- | --- | --- |
| S06-R009 — Hosting platform / station context | `Host (grouping of Observers)` | **PARTIAL** | [OGC §8.7.2 /req/obs-cpt/Host/Host-sem; §8.8.2 Deployment-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | A Host is not necessarily a physical station, surveyed sensor location, parent hardware, or proof of an installed Observer. |
| S06-R010 — Observing procedure / method | `ObservingProcedure (reusable observing method)` | **DIRECT** | [OGC §8.5.2 /req/obs-cpt/ObservingProcedure/ObservingProcedure-sem; §8.2.9](https://docs.ogc.org/as/20-082r4/20-082r4.html) | A reusable method is not an installed hardware identity or proof the method was executed for a historical event. |
| S06-R013 — Observed / observable property | `ObservableProperty (quality of feature-of-interest)` | **DIRECT** | [OGC §8.3.2 /req/obs-cpt/ObservableProperty/ObservableProperty-sem; §8.2.7](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Outdoor air temperature and logger-panel temperature are not the same observed property merely because both use °C; property != measured value. |
| S06-R014 — Observer / observing System | `Observer (identifiable individual performing observing)` | **PARTIAL** | [OGC §8.6.2 /req/obs-cpt/Observer/Observer-sem; §8.2.10](https://docs.ogc.org/as/20-082r4/20-082r4.html) | The broad DIM label 'Observer / observing System' exceeds OMS: an Observer is not necessarily physical equipment or the CSAPI DataStream publisher. |
| S06-R015 — Performed Observation | `Observation (act determining property value)` | **DIRECT** | [OGC §8.2.2 /req/obs-cpt/Observation/Observation-sem; §§8.2.3–8.2.4; §9.3](https://docs.ogc.org/as/20-082r4/20-082r4.html) | A published manufacturer example is not a performed act; a copied API representation is not a new original act. Original Bennett resultTime is UNKNOWN, so fully conformant source-native OMS serialization is not demonstrated. |

## 3. Twelve OMS concepts worth keeping on hold

These are genuine OGC-defined concepts or constraints. The table records them as **source-confirmed research leads**, not twelve newly approved DIM rows or automatically valid source-case values.

| Lead | Current proposed/held context | Native OMS concept | Exact source location | Reason for HOLD |
| --- | --- | --- | --- | --- |
| OMS-H01 | CASE-H08 | `Observation.phenomenonTime` | [OGC §8.2.3 /req/obs-cpt/Observation/phenomenonTime-sem and -card](https://docs.ogc.org/as/20-082r4/20-082r4.html) | The period to which the result applies; the standard explicitly uses a time interval for averages of multiple samples. Preserve source coverage and timezone; no unsupported precise interval inferred. |
| OMS-H02 | CASE-H08 | `Observation.resultTime` | [OGC §8.2.4 /req/obs-cpt/Observation/resultTime-sem and -card; §9.3.3](https://docs.ogc.org/as/20-082r4/20-082r4.html) | An instant when the result became available; exactly one in a fully modeled Observation. Original Bennett NOAA resultTime remains UNKNOWN and must not be filled with the API publication date or phenomenonTime. |
| OMS-H03 | CASE-H08 | `Observation.resultQuality` | [OGC §9.2.5 /req/obs-core/AbstractObservationCharacteristics/resultQuality-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Observation result quality is distinct from equipment health and from the procedure's generic trustworthiness; Bennett's literal F_ATemp='<0> ' and separate blank F_Record must not be normalized away. |
| OMS-H04 | S06-R012 | `Observation.result and quantitative UoM` | [OGC §8.2.8 /req/obs-cpt/Observation/result-sem; §8.2.16 /req/obs-cpt/Observation/uom](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Observation result is an instance value, not a reusable native output field/schema position; a measurable result needs appropriate units without inventing native 14-field result bodies. |
| OMS-H05 | CASE-H02 | `Observation.featureOfInterest (what was measured)` | [OGC §8.2.6 /req/obs-cpt/Observation/featureOfInterest-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | For an air temperature measurement the observed feature may be a volume of air; station site location, mounted probe and feature-of-interest are distinct subjects. |
| OMS-H06 | CASE-H07 | `proximateFeatureOfInterest / ultimateFeatureOfInterest` | [OGC §9.2.6–§9.2.7 /req/obs-core/AbstractObservationCharacteristics/pFoI-sem / uFoI-sem; §9.3.5](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Allows proxy samples versus ultimate target, not evidence that a particular proxy/sample chain exists in one of our cases. |
| OMS-H07 | CASE-H01 | `Observer ↔ Deployment ↔ Host association` | [OGC §8.6.5; §8.8.2–8.8.4](https://docs.ogc.org/as/20-082r4/20-082r4.html) | A deployment assigns an Observer to a Host. The model alone does not create dated EE181 serial role periods, exact change instant, or 2026 installed state. |
| OMS-H08 | CASE-H06 | `AbstractObservationCharacteristics.parameter: NamedValue` | [OGC §9.2.4 /req/obs-core/AbstractObservationCharacteristics/parameter-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Event-specific settings/inputs may be recorded as parameters, but a device's factory default is not necessarily the actual setting during an observation. |
| OMS-H09 | S06-R022 | `relatedObservation association` | [OGC §8.1.3 /req/obs-cpt/gen/relatedObservation-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Relates Observation ACTS; it is not automatically an original-record to derivative API-copy provenance relation and does not turn Bennett two NOAA events into four. |
| OMS-H10 | S06-R021 | `Abstract Observation Core.metadata association` | [OGC §9.1.2 /req/obs-core/gen/metadata-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Generic descriptive metadata link does not enforce project-specific original issuer, edition, locator, attestation, source truth grade or signed provenance. |
| OMS-H11 | CASE-H08 | `Observation.validTime` | [OGC §8.2.5 /req/obs-cpt/Observation/validTime-sem](https://docs.ogc.org/as/20-082r4/20-082r4.html) | Period during which result is useful is separate from phenomenonTime and resultTime; NOAA station summary does not establish a validity period. |
| OMS-H12 | CASE-H07 | `ObservingProcedure versus processing-chain/Observer implementation` | [OGC §8.5.2; §8.6.2; §7.1.6](https://docs.ogc.org/as/20-082r4/20-082r4.html) | An algorithm or simulation may generate an Observation; source does not reveal the full producing algorithm, aggregation chain or original issuer behind Bennett's summary. |

## 4. Bennett's Point is the critical test

**There are two original historical NOAA temperature-mean events, not four original acts.** The four earlier experimental API representations refer back to those two source events. An OMS `relatedObservation` association links observation acts; it is not a general provenance assertion that a digital copy equals a newly executed measurement. Creating another API representation does not establish a new observed original event.

**`phenomenonTime` differs from `resultTime`.** OMS §8.2.3 specifies the time over which an average applies and allows a period; §8.2.4 specifies the instant when the result became available. Both have an exactly-one requirement for a conforming conceptual Observation. For the Bennett source, the **original `resultTime` is not known**. We must not assign the record's nominal period end, later repository retrieval time or our own API publication time and claim it was original evidence.

**Original quality and identity are separate.** Bennett's `F_ATemp="<0> "` token retains its trailing space and its separate blank `F_Record` field; OMS `resultQuality` is a conceptual quality carrier, not license to invent quality classifications. The source has two EE181 serial identities across three dated service statements, not three physical probes. `Deployment` can relate Observer to Host, but the actual probe-to-station join, exact replacement minute and original result-generation algorithm remain source-qualified holds.

**Observed feature-of-interest is not automatically the station.** For ambient air-temperature data, the observed subject may be the air surrounding the intake. A station site coordinate, physically mounted probe and the air whose temperature is estimated are distinct referents. OMS also distinguishes proximate and ultimate features-of-interest where sampling/proxy relations exist; none should be invented from the evidence we have.

## 5. The other three cases

**Dragino S31-LB:** A documented SHT31 and two separate output properties describe a manufacturer reference product, not an observed real-world event or uniquely identified deployed OMS Observer.

**AirGradient Open Air Max:** Two distinct physical PMS5003 modules and three particulate properties are different information roles; OMS ObservableProperty is not a physical module or an emitted DataStream field.

**Campbell CR1000X + ClimaVue 50:** The sensing attachment, logger and separate published logger Status example must not be treated as one confirmed operating Observer or a chain of actual OMS Observations without real installation and event evidence.

## 6. Source boundaries and preservation checks

The native concepts/clauses above have been reviewed directly in **OGC 20-082r4**. The mappings to our **proposed DIM rows remain analytical**, and `DIRECT` is restricted to narrowly equivalent terms, never an assertion of interoperability or certification. The five OMS donor cells carry original source clause locators, their source status and caveats. **No new arbitrary R24/DIM superclass or physical provenance model was added.**

**Preserved:** 13 owner-approved columns, six section bands, 22 proposed DIM rows, nine case-only holds, 73 case source records, 4 SWE Common, 10 SensorML and 12 CSAPI source-checked donor cells, and 26 prior-only other donor cells. The source workbook from Step11 remains an untouched historical baseline. No CSAPI Profile, DIM UML, Glaux runtime, server, Cloudflare deployment or real Observation execution was changed.

**NEXT separate owner's ‘proceed’ executes Step13 only**, per controlling plan. Step13 is not performed or preauthorized by Step12.

## Step12 independent final workbook test

The actual v0.6 workbook has Git object SHA `15dbdde7bde030cb110e37ff34665d8ecc570dbc`. [GitHub Actions run 42334124885](https://github.com/OS4CSAPI/glaux-client/actions/runs/42334124885) finished **SUCCESS** on the exact Step12 workbook commit and checked the 11 worksheets, 13 grouped columns, six full-width divider rows, source/evidence/CSV/JSON parity, all 57 unchanged donor row identities, 73 case statements and the five revised OMS clauses. This verifies spreadsheet and source-record consistency, **not** original-source implementation/encoding conformance or adoption of any DIM/Profile concepts. The historical source does not provide original Bennett `resultTime`.
