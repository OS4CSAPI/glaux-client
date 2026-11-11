# SOSA-G2-7L — consolidated original C239 §13.5.2.3.3–§13.5.2.7.2 source-first review

**11 November 2026 — Original The Open Group SOSA C239 Edition1.1 (2023), PDF pages 285–295 (printed 259–269).** All 23 nested source sections were reviewed at the original inline text, Rule, Observation, Recommendation, Permission, connector-table and figure-caption depth. Original high-resolution figure geometry and modality checkmarks were NOT verified; original external normative companions, eight native C239 DSDM/IDL/OpenAPI files and S251 remain unexamined. STOP before C239 §13.5.2.8 J7; the heading at the bottom of PDF295 does not authorize J7 source review.

## Source-native inventory, exact standing and key findings

| Item kind (disjoint) | Count |
| --- | ---: |
| source numbered rule shalls | 48 |
| numbered observations | 6 |
| numbered recommendations should | 2 |
| numbered permissions may | 1 |
| source headings | 23 |
| table texts | 4 |
| table pin rows | 34 |
| figure captions | 4 |
| source contexts | 11 |
| unexamined external pointers | 15 |
| total unique native evidence records | 148 |
| existing sosa cells qualified | 24 |
| exact source holds | 19 |
| rule conformance I only | 34 |
| rule conformance A only | 8 |
| rule conformance T only | 2 |
| rule conformance I T | 1 |
| rule conformance A T | 2 |
| rule conformance I A | 1 |

**J2 signal and safety (§13.5.2.3.3–.3.17):** Source Rule13.5.2.3.3-1 specifies TIA/EIA-422-B serial ports and a separate supplier-dependent return-line Observation. Arming/Cutout/Emission Mode each has electrical current ≤100mA and voltage ≤30VDC Rules, plus specific physical pin allocation for MASTER_ARM, No Emit Zone (NEZ) map selection and emissions mode. NEZ maps are described as pre-defined azimuth/elevation suppression zones stored in sensor memory, with platform-originated hardwired selection—not a CSAPI geospatial service, read-out, software Command or evidence of actual safe operation. Isolated 28V emissions annunciation/safety status, gimbal-motion control description, conditionally platform-provided 1PPS rollover, optional hand-controller and USB power, physically triggered 30ms memory purge, optional MIL-STD1553B twinax, LVDS and manufacturer maintenance pins remain distinct source provisions. Permission13.5.2.3.14-1 says USB Host MAY be provided; Rule13.5.2.3.15-1 is conditional when USB Host is required.

**J3 copper video (§13.5.2.4):** Table13.5.2.4-1 carries eleven pin rows: A–F six digital video channels, G/H two composite video channels, J/K separate analog Y/C lines and L unused. Two Inspection Rules govern 21-11 connector and table, two Test Rules SMPTE ST292/424/2081/2082 and 75-ohm size12 coax, and two Analysis Rules RS-170a analog and 75-ohm contacts. None constitutes an actual video frame, published DataStream or installed equipment link.

**J4 optical fiber (§13.5.2.5):** Table13.5.2.5-1 contains eleven rows, A–H four send/receive physical pair roles plus J/K/L three SMPTE video fibers; the original has apparent misspellings including Rreceive and 25GBAASE, preserved as source caveats. Nine distinct numbered Rules cover 19-11 connector, table assignment, 850nm high-speed 10/25/40/100GBASE-SR, low-power SMPTE video at 1310nm, 50±3μm core and 125±2μm cladding, MIL-PRF termini, 1.8mm ARINC aramid cable and OM3 per ISO/IEC11801; external original standard texts not audited.

**J5 GPS antenna (§13.5.2.6):** Three Inspection Rules and a one-row 50-ohm coax table set a conditional external antenna for an internal receiver requiring one, citing SAE AS6129 and MIL-STD188-148B. No actual position, source clock or observation time is established.

**J6 auxiliary DC power (§13.5.2.7–.7.2):** Eleven Table13.5.2.7-1 rows account for five platform 28VDC power/return pairs plus one safety ground. Ten Rules cover connector/pin arrangement, conditional platform feed, same power standard as J1, max 25A per pair for up to 2s inrush, max 15A per pair after the inrush period, ≥1MΩ chassis isolation to returns and ≤0.1Ω safety ground. **Original Rules13.5.2.7.1-4 and -5 are two separately numbered repeated 15A SHALLs**; **Recommendations13.5.2.7.1-1 and -2 are separately printed repeated SHOULDs** governing J1-first and ascending pairs. Rec -1 prints Inspection (I), Rec -2 does not; Observation13.5.2.7.1-2 prints Inspection (I) but is NOT a SHALL. Do not de-duplicate source IDs, infer actual wiring or promote a physical requirement to an adopted general Profile rule.

The 173/18/1 original C239 heading count remains unchanged because the entire packet sits within the previously sampled and still PARTIAL §13.5.2 heading; 173 means at least sampled/inline-reviewed, **not** 173 source-complete sections. The [original item inventory and exact holds](SOSA_G2_7L_Original_Source_Item_Coverage_11NOV2026.json) preserve external-original, figure, repeated source Rule and real-device limitations.

## 24 existing-row source-qualified comparisons

| Existing row label | Match type | Original source native meaning | Negative equivalence boundary |
| --- | --- | --- | --- |
| Network-visible participant | RELATED | J2 serial and J4 fiber physical communication paths. | Not a network-addressable System, IP instance or reachable CSAPI service. |
| Physical constituent | RELATED | J3 video, J4 fiber and J6 power are distinct connector designs. | No observed installed physical component or mandatory DIM chassis. |
| Network instance and connection context | RELATED | Original TIA/EIA serial and multi-mode optical designs. | No observed network session or software endpoint. |
| Composition member exposure and source attribution | NO_ESTABLISHED | Physical optical communications may interconnect elements. | No individual digital component resource or source attribution established. |
| Declared component capability catalogue | RELATED | Optional USB Host and conditional video/fiber capabilities. | Not a runtime-advertised live capability. |
| Declared command interface | RELATED | Hardwired emission arming, No Emit Zone and purge switches. | Not software Command schema or authorized API. |
| Supported operating mode | RELATED | Hardwired mode and predefined NEZ map selectors. | Not an adopted universal mode list. |
| Source-reported operating mode | NO_ESTABLISHED | Emission mode selector pins are defined. | No real reported operating mode value. |
| Issued control request | RELATED | External electrical closures can initiate local hardware actions. | No digitally issued CSAPI control or observed act. |
| Command acknowledgement / reported outcome | NO_ESTABLISHED | Isolated annunciation and safety-status lines described. | No software command acknowledgement. |
| Component capability and readiness report | RELATED | Physical video and optical signaling standards. | No ready/online state or observed equipment result. |
| Component property-value report | RELATED | Safety and annunciation physical signals. | Not a sampled digital property or CSAPI Status record. |
| Required and recommended capability support | RELATED | J6 per-pair current SHALLs distinct from J1-before-J6 SHOULD guidance. | Not mandatory Profile capability for all sensing systems. |
| Negotiated message encoding and model version | NO_ESTABLISHED | Video channels cite SMPTE signal standards. | Not CSAPI model/schema negotiation. |
| Component time basis and synchronization | RELATED | Conditional J2 1 PPS platform rollover input. | No measured clock accuracy, UTC or resultTime. |
| Reported arming state | NO_ESTABLISHED | Physical MASTER_ARM closure provision. | No real digital arming status. |
| Reported physical parent/child attachment relationships | RELATED | Physical mating and pin assignment requirements. | No verified installed parent/child relationship. |
| Power-source classification | RELATED | J6 accepts extra 28VDC platform supply. | Not installed solar/battery/mains source or telemetry. |
| Source-side DC voltage | RELATED | J6 nominal 28V and 15A post-inrush per pair. | Not measured voltage. |
| Reported condition of power to the component | NO_ESTABLISHED | J6 insulation and safety-ground resistance constraints. | Not observed electrical condition. |
| REVIEW HOLD — reporting path | NO_ESTABLISHED | J3/J4 video signal links. | No observed video frames or CSAPI DataStream. |
| REVIEW HOLD — power / state | RELATED | J6 inrush, post-inrush and safety-ground rules. | No actual current, isolation or source-case state. |
| REVIEW HOLD — time / QA | NO_ESTABLISHED | 1 PPS design for platform signal input. | No validated actual time or observation quality. |
| REVIEW HOLD — control execution | NO_ESTABLISHED | NEZ hardwired select and 30ms purge trigger. | No authenticated Command or witnessed effect. |

Every mapping references one or more stable original Rule/Recommendation/Permission records in the linked JSON, and is a **source-to-master donor correspondence only**. It cannot adopt DIM classes, equipment model hierarchy, OGC Profile SHALL, observed status or hardware actions. Only SOSA donor column I is authorized for new comparison cells. The previous master, all four source cases, ISA 480 source outcomes/six open questions, 58 donor facts and 22 historical workbook sheets must remain preserved.

## 19 precise unresolved original-source and meaning holds

- **SOSA-G2-7L-Q01:** TIA/EIA-422-B original and EMC/EMI practices unexamined.
- **SOSA-G2-7L-Q02:** Physical arming, emission mode, gimbal safety switch is not software CSAPI Command/ack.
- **SOSA-G2-7L-Q03:** NEZ maps, installed turret, location and suppression state not observed.
- **SOSA-G2-7L-Q04:** Purge 30ms physical switch provision; no actual erase command/event.
- **SOSA-G2-7L-Q05:** J3 SMPTE/RS170a originals and figure/modality matrix unverified.
- **SOSA-G2-7L-Q06:** J4 external IEEE/SMPTE/MIL-PRF/ARINC/ISO specs and full figure geometry unread.
- **SOSA-G2-7L-Q07:** J4 source prints Rreceive and 25GBAASE inconsistencies; preserve literal source standing.
- **SOSA-G2-7L-Q08:** J5 antenna conditional; no actual GNSS fix/time inferred.
- **SOSA-G2-7L-Q09:** J6 original MIL-STD704F and MIL-STD1310 text unreviewed.
- **SOSA-G2-7L-Q10:** J6 separate repeated Rule13.5.2.7.1-4 and -5 post-inrush constraints retained.
- **SOSA-G2-7L-Q11:** J6 Recommendation13.5.2.7.1-1 prints Inspection(I) and -2 prints none; both SHOULD.
- **SOSA-G2-7L-Q12:** J6 Observation13.5.2.7.1-2 prints Inspection(I); remains Observation.
- **SOSA-G2-7L-Q13:** No physical measurements confirm 25A/2s, 15A, 1MΩ or 0.1Ω design conditions.
- **SOSA-G2-7L-Q14:** J3/J4 video physical signal channels do not establish video frame or CSAPI DataStream.
- **SOSA-G2-7L-Q15:** J2 1 PPS ICD-GPS-060B companion and actual time-quality unverified.
- **SOSA-G2-7L-Q16:** Four original figure images and dense table modality checkmark pixels not verified.
- **SOSA-G2-7L-Q17:** Eight C239 DSDM/IDL/OpenAPI, later S251, and restricted Appendix C remain held.
- **SOSA-G2-7L-Q18:** No four source cases independently prove J2–J6 SOSA implementation.
- **SOSA-G2-7L-Q19:** No DIM/Profile class, SHALL, actual device control or runtime conformance adopted.

**Source-ledger/readable report complete; mandatory L23 same-Excel publication and independent grid verification must succeed before declaring the delivery complete.** One separate owner Proceed after full verification may start consolidated **G2-7M original §§13.5.2.8–13.5.2.12 only**. No G3, SAPIENT, DIM/Profile adoption, real equipment or deployment.
