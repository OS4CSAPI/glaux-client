# SOSA-G2-7N — original J10–J16 source-first donor assessment

**11 November 2026 · original C239 Edition1.1 (2023) §§13.5.2.13–13.5.2.19.2, PDF306–316, stopping before Class3.** [Stable original-source evidence](SOSA_G2_7N_Original_Source_Item_Coverage_11NOV2026.json) registers **31 original Rule-labeled appearances: 30 with explicit SHALL and one J13 Rule-labeled descriptive paragraph**, four SHOULD Recommendations, two Observations, six original tables/53 source pin and fiber rows, eight figure captions and 21 exact unresolved holds. No original high-resolution figure pixels, referenced original external standards or eight C239 model/interface companions were audited.

**J10 versus J11 power:** Original J10 table prints 120/208VAC and its normative Rule uses 115/200V RMS grounded-neutral Y, 400Hz up to 10A per phase; recommend all three phases interrupt together for any phase over-current. J11 separately describes platform-provided 270VDC@10A with limited 15A for 2s inrush, chassis isolation, grounding and wire safety Recommendations. **J11 Rule identifiers are misprinted as 13.5.2.13.1-1/-2**, including the same -1 identifier printed in J10. Both exact Rule appearances have separate stable source IDs in the ledger; no imaginary source correction.

**J12 versus J13 key fill:** Both relate to physical DS101 key fill but the non-GPS J12 interface specifies differential TIA485-A B/E with optional Wake-Up, whereas GPS J13 specifies TIA232 RTS/RX/TX/CTS signals. Printed J13 Rule13.5.2.16-5 contains role descriptions rather than an explicit SHALL; it remains Rule-labeled but not counted as one of 30 explicit SHALL statements. Neither interface establishes authenticated CSAPI software Commands, authorization or performed key transfer.

**J14 versus J15 optical:** A shared 24-position MT source table provides 12 receive and 12 transmit physical fiber positions; conditional Three Fat Pipes reuse these positions. J14 usage for >24 fibers is a **SHOULD**, while J15 option for ≤24 is an **Observation**. Source J14 Rules refer to 13.5.3.5-3, 13.5.2.5-7 and 13.5.2.16.1-2/-3/-4; J14 and J15 also cite 13.2.5.17.1-1. Those pointers need original resolution and were not silently corrected.

**J16 backup supply:** V_BATT table 3.3V and ALT_V_BATT 3.9V, contrasted with source maximum Rules of 3.5V/115mA and 3.9V/115mA; supplied from platform for volatile memory/clocks and key-fill hold-up, not measured stored battery energy or a time-to-empty forecast.

## Source item census

| Record kind | Count |
| --- | ---: |
| original rule appearances | 31 |
| rule with explicit shall | 30 |
| rule labeled descriptive | 1 |
| recommendations should | 4 |
| observations | 2 |
| nested sections | 15 |
| original source tables | 6 |
| pin and fiber table rows | 53 |
| figure captions | 8 |
| pointers | 14 |
| descriptive source contexts | 9 |
| all typed source records | 142 |
| source qualified master mappings | 24 |
| exact holds | 21 |

## 24 source-qualified existing-row donor correspondences

| Existing master element | Relationship | Original source meaning and boundary |
| --- | --- | --- |
| Physical constituent | RELATED | J14 four-MT and J15 one-MT are distinct physical connector designs. No installed sensing components or universal DIM chassis. |
| Network-visible participant | NO_ESTABLISHED | MT fiber channels can carry physical optical traffic. No IP participant, network service identity or reachable CSAPI node. |
| Network instance and connection context | RELATED | Three Fat Pipes group selected physical optical pin positions. No actual network connection or negotiated remote endpoint. |
| Reported output field | NO_ESTABLISHED | 24 physical fiber positions are organized as RX/TX contacts. Not 24 digital outputs, observations or individually identified physical sensors. |
| Declared component capability catalogue | RELATED | J10 AC, J11 HVDC and J16 hold-up power are source-specific design capabilities. Not an active capability observed on empirical cases. |
| Declared command interface | NO_ESTABLISHED | Physical DS101 key-fill signal interfaces differ by GPS role. No authenticated CSAPI software Command or safe network execution API. |
| Component capability and readiness report | NO_ESTABLISHED | J16 battery-designated low-current hold-up is a hardware provision. No source-reported readiness or actual device condition. |
| Required and recommended capability support | RELATED | J10 protective, J11 wire and J14 fiber-count guidance are SHOULD Recommendations. Not universal mandatory Profile SHALL or required connector. |
| Negotiated message encoding and model version | NO_ESTABLISHED | J12 differential TIA485-A and J13 single-ended TIA232 are native physical interfaces. No machine-readable data model or digital schema negotiation. |
| Component time basis and synchronization | RELATED | J16 hold-up can sustain a real-time clock over power cycles. Not clock synchronization, measured accuracy or actual timestamp. |
| Reported physical parent/child attachment relationships | RELATED | J14 and J15 specify possible physical mating arrangements. No named installed parent/child devices or actual mechanical attachment. |
| Power-source classification | RELATED | The source distinguishes platform AC, 270VDC and two backup DC feeds. Not actual source generator or field battery identity. |
| Source-side AC voltage | RELATED | J10 requires 115/200V RMS, while its table prints 120/208VAC. No measured voltage and source discrepancy unresolved. |
| Load-side AC voltage | NO_ESTABLISHED | J10 governs AC input connection. No observed internal load-side AC voltage. |
| Source-side DC voltage | RELATED | J11 270VDC plus J16 3.3/3.9V backup inputs carry physical input specifications. Not measured source-side voltage or actual charge. |
| Load-side DC voltage | NO_ESTABLISHED | J11 specifies platform DC power inputs. Not real load-side sampled output. |
| Reported condition of power to the component | NO_ESTABLISHED | J11 inrush and J16 hold-up provisions constrain design. Not current device power condition or measured electrical fault. |
| Reported energy reserve relative to maximum capacity | NO_ESTABLISHED | J16 battery-named backup is a platform-supplied input. No measured state-of-charge or energy reserve. |
| Estimated time to empty under expected usage | NO_ESTABLISHED | Source describes retention power over a cycle. No known capacity, discharge model or runtime forecast. |
| Request access-control metadata | NO_ESTABLISHED | Key-fill connector supports physical key provisioning. No authenticated online API access-control metadata. |
| REVIEW HOLD — reporting path | NO_ESTABLISHED | MT optical interfaces carry physical signaling possibilities. No observed stream, registered route or live CSAPI DataStream. |
| REVIEW HOLD — power / state | RELATED | Source distinguishes HVDC inrush and 2 independent small hold-up power feeds. No physical measurements, installed equipment state or adopted universal requirement. |
| REVIEW HOLD — time / QA | NO_ESTABLISHED | J16 input is intended to preserve real-time clocks. No actual UTC, clock uncertainty or observation QA evidence. |
| REVIEW HOLD — control execution | NO_ESTABLISHED | J12 wake-up Rule and J13 RTS/CTS labeled description are hardware-interface semantics. No authenticated software request, acknowledgement or verified device effect. |

Every correspondence cites exact registered source IDs in the ledger. Donor comparisons are not accepted DIM classes, universal power-chassis rules, CSAPI Profile SHALLs, real installed hardware or authorized security commands.

## 21 exact source holds

- **SOSA-G2-7N-Q01:** J10 120/208VAC table differs from 115/200V RMS numbered Rule; no silent normalization.
- **SOSA-G2-7N-Q02:** J11 source prints 13.5.2.13.1-1/-2 Rule identifiers despite §13.5.2.14, with duplicated -1 printed for J10 and J11.
- **SOSA-G2-7N-Q03:** J11 270VDC@10A source table differs from 15A/2s inrush Rule; no measured electrical data.
- **SOSA-G2-7N-Q04:** J10/J11 connector figure pixels and exact modality checkmarks are not source-verified.
- **SOSA-G2-7N-Q05:** Original military 270VDC/power/grounding/SAE wire references are pointers, not independently audited normative documents.
- **SOSA-G2-7N-Q06:** J11 arc-track/corona Recommendations are design safety guidance, not proven installed conformance.
- **SOSA-G2-7N-Q07:** J12/J13 external EKMS308/DS101/TIA232/TIA485/MIL-STD464C originals not examined.
- **SOSA-G2-7N-Q08:** J12 differential non-GPS signals and J13 TIA232 GPS keyfill remain physically distinct.
- **SOSA-G2-7N-Q09:** J13 Rule13.5.2.16-5 is printed as Rule but lacks explicit SHALL; classified separately.
- **SOSA-G2-7N-Q10:** Physical key-fill interfaces do not imply an online security service, retrieved keys or authorized software Commands.
- **SOSA-G2-7N-Q11:** J14 Rule13.5.2.17.1-1 references 13.5.3.5-3 and 13.5.2.16.1-2/-3/-4; original referent validation held.
- **SOSA-G2-7N-Q12:** J14/J15 source points to Rule13.2.5.17.1-1; possible source numbering inconsistency remains held.
- **SOSA-G2-7N-Q13:** J14 more-than-24 fiber choice is SHOULD; J15 24-or-fewer choice is Observation, not mandatory design.
- **SOSA-G2-7N-Q14:** J14/J15 Observations print Inspection(I) but are not transformed into Rules.
- **SOSA-G2-7N-Q15:** 24 original MT table pin/fiber positions and three Fat Pipes read as text; figure geometry/modalities held.
- **SOSA-G2-7N-Q16:** Original IEC61754-5 MT ferrule standard and eight figure pixels were not inspected.
- **SOSA-G2-7N-Q17:** J16 table 3.3V versus Rule 3.5V maximum for V_BATT, ALT_V_BATT 3.9V; not a measured voltage.
- **SOSA-G2-7N-Q18:** J16 platform power to clocks/keys does not establish a serialized battery, charge or time-to-empty.
- **SOSA-G2-7N-Q19:** Eight C239-native DSDM/IDL/OpenAPI, S251 and restricted Appendix C remain unreviewed/restricted.
- **SOSA-G2-7N-Q20:** No four source cases demonstrate installed J10–J16 hardware, actual keyfill, or safety conformance.
- **SOSA-G2-7N-Q21:** Zero adopted DIM classes/cardinality, Profile SHALL, commands or independent runtime interoperability.

**Source coverage and boundary:** C239 192 registered headings: 173 at least sampled/inline-reviewed, 18 unread, one restricted; nested subsections do not earn new heading credit. Original companion text and figure pixels remain held; SOSA ACTIVE/OPEN, SAPIENT Step18 blocked. The **mandatory L23 same workbook/cross-format checkpoint** must be completed before beginning **G2-7O** (original Class3 §§13.5.3–13.5.3.3.11) on a separate owner Proceed.

