# SOSA-G2-7P — consolidated original Class3 source review

**11 November 2026. The Open Group SOSA C239 Edition1.1 (2023), original §§13.5.3.4–13.5.3.17.2, PDF329–351 (printed303–325). STOP before Class5 §13.5.4.** Original direct inline source text review: **74 numbered Rule appearances, 73 explicit SHALL and 1 Rule-labeled descriptive J13 item; 4 Recommendations, 5 Observations, 14 tables/135 source contact/frequency rows and 14 figure captions**. Stable clause IDs, original pages, typed evidence, 30 local holds and all 28 justified existing-row mappings are in [the source ledger](SOSA_G2_7P_Original_Source_Item_Coverage_11NOV2026.json). Figure geometry and cited original companion standards are not verified.

## Main original-source technical distinctions

**Class3 J3/J4:** J3 has four digital and two composite video physical contacts. J4 has two optical transmit/receive pairs and an OM2-or-better fiber baseline, compared with the earlier OM3 Class1&2 baseline. **Rule13.5.3.5-1 prints J4 insert13-3 while Table13.5.3.5-1 prints13-4**, and a separate 1310nm SMPTE Rule lacks distinctly allocated J4 video contacts in the four-contact table.

**Class3 J6/J7/J8/J9:** J6 28V input inrush **14A for up to two seconds and 10A nominal per pair** differs from Class1&2 25A/15A. Duplicate 10A Rules13.5.3.7.1-3/-5 and repeated SHOULD Recommendations -1/-2 are kept separate. J7 has 66 electrical contacts over multiple physical interface families and hardwired WR_EN, plus one unnumbered shell-plating SHALL. J8 provides 11 antenna contacts versus earlier 19, J9 four versus earlier eight, and **J9 Rule13.5.3.10-2 prints25-8 insert while native Table13.5.3.10-1 prints21-75**. RF voltage-standing-wave ratio is a conformance bound, not measured signal power.

**Class3 J11/J12/J13/J14/J15/J16:** J11 source is 270VDC@5A with 7.5A/2s inrush vs earlier 10A/15A; **Rule13.5.3.12.1-1 erroneously cites later Class5 Table13.5.4.3-1**. J12/J13 key-fill headings print Class1&2 even within Class3, with physically distinct non-GPS TIA485 and GPS TIA232 roles. J13 Rule13.5.3.14-5 has no explicit SHALL. Class3 J14 uses two MT/48 optical fibers, J15 one MT/24; J14 cross-reference methods conflict with the direct J4 source rules and point to unresolved 13.5.2.16.1-* clauses. J16 platform-fed V_BATT/ALT_V_BATT supports clocks/memory/key-fill, not battery charge or time-to-empty.

These are **source-specific physical/electrical meanings**, not a universal DIM chassis, digital CSAPI Commands, installed equipment or verified source-case observations.

## Original-source inventory

| Kind | Count |
|---|---:|
| source numbered rules | 74 |
| source explicit shall | 73 |
| source Rule labeled descriptive | 1 |
| source recommendations | 4 |
| source observations | 5 |
| source permissions | 0 |
| nested sections | 29 |
| source tables | 14 |
| table pin and frequency rows | 135 |
| figure captions | 14 |
| source contexts | 12 |
| unread companion pointers | 10 |
| unnumbered table shall | 1 |
| typed source records | 298 |
| qualified existing rows | 28 |
| precise holds | 30 |

## 28 source-qualified comparisons to approved existing rows

| Existing master row | Fit | Original meaning | Non-equivalence boundary |
|---|---|---|---|
| Physical constituent | RELATED | Class3 J3/J4/J8 source physical connectors differ in form and contact roles. | Not individual installed Systems or DIM universal chassis. |
| Network-visible participant | NO_ESTABLISHED | J7 10GBaseT is a physical Ethernet design. | No online IP endpoint or CSAPI System identity established. |
| Network instance and connection context | RELATED | Source J7 Ethernet/serial physical channels. | No observed network session or service discovery. |
| Composition member exposure and source attribution | NO_ESTABLISHED | J4 and MT fiber can connect source-specific equipment. | No observed attributed digital member resource. |
| Reported output field | NO_ESTABLISHED | J3 video and J8 RF contacts are physical channels. | Not reported observation fields or individual sensors. |
| Declared component capability catalogue | RELATED | Class3 video, OM2 fiber and USB are specified hardware interface capabilities. | Not an actively offered source-case service. |
| Declared command interface | RELATED | Physical J7 Write Enable circuit is a maintenance hardware interface. | Not an authenticated software Command API. |
| Issued control request | NO_ESTABLISHED | Hardwired write-enable closure controls nonvolatile writing. | Not an issued or witnessed digital request. |
| Command acknowledgement / reported outcome | NO_ESTABLISHED | Original source specifies physical write-enable behavior. | No command acknowledgement or success report. |
| Component capability and readiness report | RELATED | Optical/Ethernet design standards may describe hardware support. | No observed operational readiness. |
| Component property-value report | NO_ESTABLISHED | Original VSWR limits apply to RF connector performance. | Not measured or published Status. |
| Required and recommended capability support | RELATED | J6 mandatory per-pair current differs from recommended J1-before-J6 priority. | No universal Profile SHALL on every sensing system. |
| Negotiated message encoding and model version | NO_ESTABLISHED | J7 physical USB/DisplayPort protocols have standards editions. | No negotiated software schema or message version. |
| Component time basis and synchronization | RELATED | J16 platform backup may hold real-time clock state. | No source clock sync or time accuracy. |
| Reported physical parent/child attachment relationships | RELATED | J14 and J15 have different physical MT arrangements. | No installed parent/child identity inferred. |
| Power-source classification | RELATED | Platform feeds 28VDC/270VDC/hold-up inputs of different roles. | Not observed battery or source generator. |
| Source-side DC voltage | RELATED | Class3 electrical input design voltages and current constraints. | Not measured voltage data. |
| Reported condition of power to the component | NO_ESTABLISHED | J6 isolation and J11 inrush are physical design criteria. | No observed device power state. |
| Reported energy reserve relative to maximum capacity | NO_ESTABLISHED | J16 is battery-designated low-current hold-up input. | No state-of-charge or energy reserve. |
| Estimated time to empty under expected usage | NO_ESTABLISHED | J16 may preserve memory/clocks over power cycling. | No discharge prediction. |
| Reported component receive data rate | NO_ESTABLISHED | 10GBaseT is a nominal physical interface class. | No measured live receive throughput. |
| Reported component transmit data rate | NO_ESTABLISHED | 10GBaseT specifies hardware signaling. | No observed transmit data rate. |
| Reported received signal power | NO_ESTABLISHED | VSWR is RF impedance mismatch metric. | Not received RF power. |
| Request access-control metadata | NO_ESTABLISHED | J12/J13 key-fill are role-dependent hardware security interfaces. | No software API credentials or grants. |
| REVIEW HOLD — reporting path | NO_ESTABLISHED | Copper video and optical interfaces could carry signals. | No observed OGC DataStream. |
| REVIEW HOLD — power / state | RELATED | Class3 physical inrush/hold-up ratings differ from other Classes. | No live measurements or adopted general power rules. |
| REVIEW HOLD — control execution | NO_ESTABLISHED | WR_EN is a hardwired maintenance circuit. | No safe network-executable Command. |
| Signal Strength Ratio — reference quantity question | NO_ESTABLISHED | RF VSWR is a physical ratio with source-specific frequency bands. | Not the separate unresolved ISA Signal Strength Ratio concept. |

Each comparison uses exact source-native Rule or Recommendation IDs. No DIM/Profile class/field/cardinality or runtime adoption is approved.

## 30 original-source holds

- **SOSA-G2-7P-Q01:** J4 Rule13.5.3.5-1 says insert13-3, source table says13-4.
- **SOSA-G2-7P-Q02:** J4 original SMPTE 1310nm Rule has no separately identified video optical contacts in four-contact Ethernet table.
- **SOSA-G2-7P-Q03:** J4 OM2-or-better Class3 fiber baseline differs from Class1&2 OM3.
- **SOSA-G2-7P-Q04:** J3 Class3 four digital/two composite differs from earlier Class1&2 eleven-contact video; no live footage.
- **SOSA-G2-7P-Q05:** J5 conditional GPS antenna not actual position/time.
- **SOSA-G2-7P-Q06:** Class3 J6 14A/2s inrush and10A nominal differ from earlier25A/15A; no device measurements.
- **SOSA-G2-7P-Q07:** Separate J6 Rules13.5.3.7.1-3 and -5 repeat 10A post-inrush shall.
- **SOSA-G2-7P-Q08:** J6 repeated Recommendations -1 and -2 carry different verification notes but remain SHOULD.
- **SOSA-G2-7P-Q09:** J6 Observation13.5.3.7.1-2 prints Inspection(I) but remains Observation.
- **SOSA-G2-7P-Q10:** J6 isolation/grounding physical conformance never independently tested.
- **SOSA-G2-7P-Q11:** J7 original table preamble unnumbered matching-shell-plating SHALL retained.
- **SOSA-G2-7P-Q12:** J7 physical Write Enable is not a software CSAPI Command or observed memory write.
- **SOSA-G2-7P-Q13:** J8 Class3 eleven RF contacts rather than Class1&2 nineteen; modality pixels not verified.
- **SOSA-G2-7P-Q14:** J9 Rule13.5.3.10-2 says25-8 insert, table and Class3 catalog say21-75.
- **SOSA-G2-7P-Q15:** J9 Class3 four RF contacts rather than earlier eight; actual RF links untested.
- **SOSA-G2-7P-Q16:** J8/J9 VSWR upper limits are physical criteria, not measured power or ISA signal strength.
- **SOSA-G2-7P-Q17:** J11 Rule13.5.3.12.1-1 wrongly points at later Class5 Table13.5.4.3-1 rather than Class3 native J11 table.
- **SOSA-G2-7P-Q18:** Class3 J11 270VDC5A/7.5A inrush differ from Class1&2 270V10A/15A.
- **SOSA-G2-7P-Q19:** Class3 J12/J13 original headings say Class1&2 and applicability is not silently changed.
- **SOSA-G2-7P-Q20:** J12 differential non-GPS vs J13 TIA232 GPS key-fill roles, no online key provisioning service.
- **SOSA-G2-7P-Q21:** J13 Rule13.5.3.14-5 label lacks explicit shall.
- **SOSA-G2-7P-Q22:** J14 Class3 two MT/48 fibers and J15 one MT/24 fibers not separate installed sensors.
- **SOSA-G2-7P-Q23:** J14 common reference to 13.5.2.16.1-2/-3/-4 unverified.
- **SOSA-G2-7P-Q24:** J14 common source method notes differ from directly printed J4 Rule13.5.3.5-3/-9 methods.
- **SOSA-G2-7P-Q25:** J16 nominal3.3V vs max3.5V V_BATT; ALT3.9V, 115mA each, no charge/energy evidence.
- **SOSA-G2-7P-Q26:** All fourteen figure pixels and modality checkbox alignment unverified.
- **SOSA-G2-7P-Q27:** Original external IEEE/MIL/SMPTE/VITA etc and eight C239 original native DSDM/IDL/OpenAPI files unread.
- **SOSA-G2-7P-Q28:** 2025 S251 edition separate and C239 AppendixC restricted.
- **SOSA-G2-7P-Q29:** Four empirical devices have no direct test of SOSA Class3 connectors.
- **SOSA-G2-7P-Q30:** No adopted DIM classes/chassis/cardinality, CSAPI Profile SHALL or independent device/runtime conformance.

**Source coverage:** C239 174/192 registered headings at least sampled or inline-read, 17 unread, one restricted. These new nested Class3 subsections do not add registered-heading credit; broader figure/companion audit remains PARTIAL. **Mandatory L23 publisher:** one canonical JSON, BOTH CSV, BOTH Markdown and SAME original 26-sheet Excel, verifying actual saved cells and historical sheets. Only distinct new owner Proceed may start G2-7Q Class5 §§13.5.4–13.5.5.6.1, stop before Chapter14.

