# SOSA-G2-7O — original Class3 connector, J1 power and J2 signal audit

**Original The Open Group SOSA C239 Edition1.1 (2023) §§13.5.3–13.5.3.3.11, PDF317–329, STOP before §13.5.3.4 J3 video.** [Original stable 202-record source ledger](SOSA_G2_7O_Original_Source_Item_Coverage_11NOV2026.json) includes **47 individually numbered SHALL Rules, nine Observations, five Permissions, 20 original headings, three source tables/88 contact rows, two figure captions, one distinct unnumbered NEZ SHALL** and 22 precise holds. Printed Conformance Methodology breakdown: **39 Inspection (I), 4 Analysis (A), 3 Test (T) and 1 Analysis/Test (A,T)**; every Rule has stable original identifier/page in the ledger. Figure geometry and dense modality checkmarks were unavailable, and no original external companions were independently read.

## Actual native distinctions and source discrepancies

**Equipment scope and connector catalog:** Table13.5.3.1-1 accounts for 13 Class3 connector kinds, while printed Rule13.5.3.1-2 includes J10 and the table omits it; a separate Permission allows mission-dependent omissions. The global connector table says J2 **N-keying**, but the detailed J2 table says **A-keying**. Multiple keyed connector instances have source-specific inventory/documentation duties, not independent system identities or a universal Domain Information Model chassis.

**Class3 J1 physical 28VDC:** One J1 connector per external sensing element, with five platform-supplied pairs nominally 28VDC/10A, **14A per pair up to two seconds inrush**, later **10A nominal maximum**, return-to-chassis **≥1MΩ isolation** and safety-ground **≤0.1Ω resistance**. These are original physical design Rules, not live Status or tested power on any of four empirical source cases.

**Class3 J2 original signal table:** Table13.5.3.3-1 contains **64 individually named contact positions** (number range 1–66, unlisted 18 and 26), grouped into Power Enable, Gigabit Ethernet pairs/shields, four serial ports, MASTER_ARM, No Emit Zone (NEZ) cutout, emission mode, annunciation, safety status, gimbal, 1PPS, hand-controller and USB circuits. J2 Power Enable ON requires a **strictly less-than-5Ω** circuit (not the earlier Class1&2 ≤5Ω text), and OFF requires **≥100kΩ**. The table is not evidence of 64 separate sensors or digital output fields.

**Critical source conflicts (retained, not silently resolved):**
- **MASTER_ARM** Rule13.5.3.3.4.1-1 names pins **2/95**, but the J2 table lists **2/5**.
- **NEZ** Rule13.5.3.3.4.2-1 and unnumbered SHALL name **4/5/11/12**, but the table lists **11/12/13/52**.
- **Emissions Mode** Rule13.5.3.3.4.3-1 names **89/90/97/98**, versus **53/54/59/65** in the table.
- Class3 **Ethernet** Rule13.5.3.3.2-2 and **serial** Rule13.5.3.3.3-1 explicitly say **Class1&2 J2** inside Class3 subsections.
- Two distinct printed **Observation13.5.3.3-1** paragraphs appear on original PDF321 and PDF326, with distinct meanings/source IDs.
- Class3 1PPS Rule refers to Figure13.5.3.3-1 captioned J2 connector arrangement, not a visually confirmed waveform.

Physical master-arm, NO-EMIT cutout, gimbal disable and emissions annunciation are source-specific hardware safety/management interfaces, **not authenticated OGC API–Connected Systems software Commands**, observed device actions or approved generic Profile requirements.

## Source-qualified donor-to-DIM comparisons (24 existing rows)

| Existing master information row | Fit | Original source meaning | Negative equivalence boundary |
|---|---|---|---|
| Physical constituent | RELATED | Class3 original connector families and individual keyed instances are hardware interface configurations. | Not separate installed Systems or a universal DIM chassis. |
| Network-visible participant | NO_ESTABLISHED | J2 physical Ethernet link design is specified. | No independently IP-addressable or remotely discoverable participant. |
| Network instance and connection context | RELATED | Ethernet and serial channel physical interface options are source-defined. | No actual IP session, address allocation or network service. |
| Composition member exposure and source attribution | NO_ESTABLISHED | J1 per external sensing element and repeated keyed connector descriptions constrain physical designs. | No independently discoverable composition member. |
| Declared component capability catalogue | RELATED | Class3 conformance requires documentation of physical connectors, their variants and non-SOSA exceptions. | Not a measured runtime capability or preapproved DIM schema. |
| Declared command interface | RELATED | Arming and gimbal inhibition are hardwired safety inputs. | Not authenticated CSAPI software commands. |
| Supported operating mode | RELATED | NEZ and emissions-mode selection pins address predefined hardware alternatives. | No universal mode enumeration; source connector pin conflicts unresolved. |
| Source-reported operating mode | NO_ESTABLISHED | Emission mode source controls pin-level input. | No reported current operating-mode output. |
| Issued control request | RELATED | External power-enable/gimbal circuits have conditional electrical effects. | No issued digital command or recorded execution request. |
| Command acknowledgement / reported outcome | NO_ESTABLISHED | Physical emission annunciation interface provides a source signal. | No digitally acknowledged software command. |
| Component capability and readiness report | RELATED | Connector inventory and Ethernet design reflect declared hardware capability. | No verified source device readiness or network service. |
| Component property-value report | RELATED | Isolated electrical Safety Status signals are specified. | No actual sampled Status resource value. |
| Required and recommended capability support | RELATED | Class3 connector conformance includes mission permissions and documented exceptions. | Not universal Profile SHALL, unresolved required-list conflicts retained. |
| Component time basis and synchronization | RELATED | J2 conditionally accepts a platform rollover pulse. | No actual synchronized UTC clock, resultTime or uncertainty. |
| Reported arming state | NO_ESTABLISHED | Physical MASTER_ARM source contacts are described. | No actually reported arming state or safe software control. |
| Reported physical parent/child attachment relationships | RELATED | J1 per element and differently keyed connector descriptions are physical design relationships. | No identified installed physical parent/child assets. |
| Power-source classification | RELATED | Class3 J1 receives power under selected source standards. | Not source energy generator or observed battery/mains type. |
| Source-side DC voltage | RELATED | Five designed 28VDC inputs support 10A nominal per pin pair. | Not measured source-side voltage telemetry. |
| Reported condition of power to the component | NO_ESTABLISHED | External Power Enable threshold conditions are normative input design. | No measured source-case current power state. |
| Reported output field | NO_ESTABLISHED | Source J2 table enumerates physical contacts and signal families. | Not 64 digital output properties or 64 sensor devices. |
| REVIEW HOLD — reporting path | NO_ESTABLISHED | Physical Ethernet/serial connections could carry traffic. | No observed data flow or CSAPI DataStream. |
| REVIEW HOLD — power / state | RELATED | J1 power inrush/nominal/grounding limits are hardware design criteria. | No installed or independently verified electrical conformance. |
| REVIEW HOLD — time / QA | NO_ESTABLISHED | Conditional physical 1PPS pulse may be accepted. | No validated observation clock/source QA. |
| REVIEW HOLD — control execution | NO_ESTABLISHED | Physical NEZ selection and gimbal disable provisions do not map to CSAPI commands. | No authorized execution, independent safety verification, or resolved pin assignments. |

Every correspondence names stable original source IDs in the JSON source ledger. No source label becomes an adopted DIM class, field, cardinality, universal chassis or Profile SHALL.

## 22 precise source holds

- **SOSA-G2-7O-Q01:** Class3 family connector table J2 N-key conflicts with detailed J2 table A-key.
- **SOSA-G2-7O-Q02:** Rule13.5.3.1-2 names J10 in conformance list but original Class3 connector family table omits J10.
- **SOSA-G2-7O-Q03:** Rule13.5.3.1-2 lists required connectors while Permission13.5.3.1-3 allows mission-dependent omissions.
- **SOSA-G2-7O-Q04:** J1 original MIL-STD704F/1275E and MIL-STD1310 originals not audited; 10A nominal/14A inrush/1MΩ/0.1Ω not physically tested.
- **SOSA-G2-7O-Q05:** J2 original 19-35 connector figure, exact dense modality checkmarks and contact pixel geometry not verified.
- **SOSA-G2-7O-Q06:** J2 64 text-registered pin numbers leave 18 and 26 unmentioned; no assumption of reserved wiring.
- **SOSA-G2-7O-Q07:** Class3 J2 Ethernet Rule13.5.3.3.2-2 explicitly says Class1&2 J2; applicability conflict.
- **SOSA-G2-7O-Q08:** Class3 J2 serial Rule13.5.3.3.3-1 explicitly says Class1&2 J2; applicability conflict.
- **SOSA-G2-7O-Q09:** MASTER_ARM Class3 Rule pins 2/95 conflict with table 2/5; no silent pin reassignment.
- **SOSA-G2-7O-Q10:** NEZ Class3 Rule/un-numbered SHALL pins 4/5/11/12 conflict with table 11/12/13/52.
- **SOSA-G2-7O-Q11:** Emissions-mode Rule pins 89/90/97/98 conflict with detailed J2 table 53/54/59/65.
- **SOSA-G2-7O-Q12:** Two different Observations use source ID13.5.3.3-1 at PDF321 and PDF326; retain both separately.
- **SOSA-G2-7O-Q13:** Class3 physical Power Enable ON threshold strictly less than 5 Ohms; Class1&2 threshold differs.
- **SOSA-G2-7O-Q14:** Power Enable and isolated discrete logic thresholds not measured on actual sensor/case.
- **SOSA-G2-7O-Q15:** 1PPS Rule cites Figure13.5.3.3-1 captioned J2 pin arrangement, not a verified timing waveform.
- **SOSA-G2-7O-Q16:** Original IEEE802.3-2008, AS6070/6, TIA/EIA422, ICD-GPS060B, MIL/ANSI/VITA originals unreviewed.
- **SOSA-G2-7O-Q17:** Class3 safety/NEZ/gimbal arming are physical controls, not executable CSAPI software Commands.
- **SOSA-G2-7O-Q18:** USB Host permission and 5V conditional power do not establish operating USB service.
- **SOSA-G2-7O-Q19:** Hand-controller Rule unconditional power wording versus conditional maximum Rule needs contextual interpretation.
- **SOSA-G2-7O-Q20:** Connector documentation not proof of installed serialized equipment or sensor subsystems.
- **SOSA-G2-7O-Q21:** Eight original C239 DSDM/IDL/OpenAPI companion originals, later S251 and restricted Appendix C still held.
- **SOSA-G2-7O-Q22:** No adopted DIM chassis/class/cardinality, CSAPI Profile SHALL or runtime/hardware conformance.

**Earned original coverage:** C239 **174 headings at least sampled/inline-reviewed, 17 substantially unread, one restricted, of 192**. Previously unread registered heading §13.5.3 is now source-reviewed; original figures/external referenced sources remain separately held and the broader §13.5 parent is still PARTIAL. **Stop:** exact next distinct owner Proceed only **G2-7P Class3 §§13.5.3.4–13.5.3.17.2**, ending before Class5 §13.5.4, after same-master Excel and mirror verification.

