# SOSA-G2-7M — consolidated original C239 J7/J8/J9 and auxiliary RF source assessment

**11 November 2026.** This one source-sized packet examines original The Open Group SOSA C239 Edition1.1 (2023), **§§13.5.2.8–13.5.2.12**, PDF pp.295–306 (printed269–280), **STOP before §13.5.2.13 J10**. The [complete stable source inventory](SOSA_G2_7M_Original_Source_Item_Coverage_11NOV2026.json) accounts for **27 individually numbered SHALL Rules (26 Inspection I, one Analysis A), two Observations, zero numbered Recommendations, zero numbered Permissions, six original table texts, 102 individual table rows, five figure captions, and one separate unnumbered source SHALL in a table preamble**. Table/figure/context/pointer records are separate from numbered requirements.

## Native original findings and scope distinctions

**J7 high-speed electrical (C239 §13.5.2.8 and six children).** The original J7 pin table specifies 66 distinct contact rows across Ethernet, USB, DisplayPort, SATA, serial, Write Enable, digital ground and spare positions. Original normative numbered Rules separately require physical connector pin arrangement, 10GBase-T under **IEEE802.3an-2006**, USB3.1 Generation2 and backwards compatibility with USB2.0, DisplayPort1.3, SATA3.0, TIA232 serial, and a hardwired **WR_EN/WR_EN_RTN** maintenance switch for nonvolatile memory. Original 13.5.2.8.6-2 spells **WR-EN_RTN** with a hyphen; this name inconsistency is retained as a question, not treated as an invented second signal. Original Table13.5.2.8-1 also contains a **separate unnumbered SHALL for the receptacle/plug shell plating**; table note referring to Meritec or equivalent is not independent compliance evidence. J7 is not proof of an addressable network node, a working software Command or observed traffic.

**J8 high-density RF connector (§13.5.2.9 and performance §13.5.2.10).** Original **19 physical antenna channel contacts A–V (omitting I/O/Q)** are individually registered with signal labels Ch1–Ch19 and 50Ω RF channels described up to 50GHz. Seven J8 connector Rules plus a separate performance Rule distinguish a conditional connector, 25-19 insert, pin assignment, SMPM size12 interface and original SAE/MIL references. Only **Rule13.5.2.9-3 is printed Analysis (A)**; the other J8 Rules are Inspection (I). Original Table13.5.2.10-1 specifies four maximum mated-contact voltage standing wave ratios: **DC–18GHz 1.25:1, 18–26.5GHz 1.30:1, 26.5–40GHz 1.40:1, 40–50GHz 1.60:1**. These are conditional physical design/performance bounds, not measured observed signal power.

**J9 low-loss RF connector (§13.5.2.11 and §13.5.2.11.1).** Original source includes eight 50Ω antenna contacts Ch1–Ch8, each described up to 22GHz; seven connector Rules and one performance Rule specify separate **25-8 insert**, BMB size8 contact design and MIL/SAE companion pointers. Original maximum voltage standing wave ratio for mated contact pairs is **1.40:1 over DC–22GHz**. J8's SMPM design and J9's BMB design may not be collapsed into an invented universal RF connector object.

**Auxiliary RF connectors (§13.5.2.12).** One conditional Inspection Rule points to the original source table with four application-specific choices: **TNC to 3GHz, SMA to 27GHz, 2.4mm to 50GHz, 1.0mm to 110GHz**. These are source-specific connector/cable possibilities and do not establish actual installed connectors, tested maximum sensor frequency or an operational transmission service.

## Complete native source-item accountability

| Type | Distinct records |
|---|---:|
| numbered rules | 27 |
| observations | 2 |
| recommendations | 0 |
| permissions | 0 |
| nested sections | 12 |
| source tables | 6 |
| table rows | 102 |
| figures caption only | 5 |
| unnumbered narrative shall | 1 |
| analytical context | 7 |
| unexamined original companion pointers | 11 |
| source records | 173 |

The original C239 registered-heading account remains **173 at least sampled/inline-read, 18 substantively unread and one restricted of 192**: all J7–J9/auxiliary subsections belong to previously sampled parent §13.5.2. Full original figure pixels, dense modality checkmark alignment, exact referenced external ANSI/VITA/IEEE/MIL/USB/other standards and eight native C239 data model/interface files were not inspected; **unreviewed does not mean absent**.

## Source-qualified correspondence to existing master (no new classes)

| Existing information row | Relation | Native meaning and non-equivalence |
|---|---|---|
| Network-visible participant | NO_ESTABLISHED | J7 provides physical Ethernet and serial interfaces. **Boundary:** No separately identified or reachable network participant or actual IP endpoint. |
| Network instance and connection context | RELATED | J7 has source-native physical pair, shield and protocol pins. **Boundary:** No live connected network session, negotiated address or service. |
| Physical constituent | RELATED | J8/J9 are two distinct conditional RF connector arrangements. **Boundary:** Neither establishes installed components, mandatory containment or a general DIM chassis. |
| Composition member exposure and source attribution | NO_ESTABLISHED | J8 may join physical sensor elements through RF contacts. **Boundary:** No individually represented CSAPI member or attributed digital report. |
| Reported output field | NO_ESTABLISHED | J8/J9 Ch1–Ch19 or Ch1–Ch8 are physical pin/channel designations. **Boundary:** Not 27 digital observation fields or physical sensor instances. |
| Declared component capability catalogue | RELATED | J7 declares specific hardware transport/protocol design support. **Boundary:** No verified runtime-advertised service or connected source-case hardware. |
| Declared command interface | RELATED | Physical maintenance switch enables nonvolatile writing. **Boundary:** Not a software Command endpoint, authorization scheme or request schema. |
| Issued control request | NO_ESTABLISHED | Hardwired contact closure is a physical maintenance provision. **Boundary:** No executed CSAPI command transaction or request identity. |
| Command acknowledgement / reported outcome | NO_ESTABLISHED | Electrical write-enable closure prescribes hardware behavior. **Boundary:** No reported success, acknowledgement or observed memory write. |
| Component capability and readiness report | RELATED | Interface designs constrain potentially supported physical signals. **Boundary:** Not current operational readiness or present-device capability report. |
| Component property-value report | NO_ESTABLISHED | VSWR maximum-by-band is a design/test criterion. **Boundary:** Not a transmitted or observed instantaneous RF property value. |
| Required and recommended capability support | RELATED | J8/J9/auxiliary RF connector rules have scoped conditions, not universal application. **Boundary:** No compulsory interfaces for all sensing Systems or adopted CSAPI Profile SHALL. |
| Negotiated message encoding and model version | NO_ESTABLISHED | Physical USB/DisplayPort protocol specifications carry edition references. **Boundary:** No negotiated model schema, OGC content-type or software version contract. |
| Reported physical parent/child attachment relationships | RELATED | RF connections can physically interconnect sensor elements. **Boundary:** No established installed attachment of named individual assets. |
| Reported component receive data rate | NO_ESTABLISHED | A 10GBase-T Ethernet channel is specified at design level. **Boundary:** Not measured current received data rate or online link. |
| Reported component transmit data rate | NO_ESTABLISHED | A 10GBase-T Ethernet channel is specified at design level. **Boundary:** Not measured current transmit throughput. |
| Reported received signal power | NO_ESTABLISHED | VSWR maxima constrain impedance mismatch by frequency. **Boundary:** Not received radio-frequency signal power in dBm. |
| REVIEW HOLD — reporting path | NO_ESTABLISHED | Pinout and RF connector families provide physical signaling options. **Boundary:** No observed data path to a CSAPI service or sensor reporting endpoint. |
| REVIEW HOLD — control execution | NO_ESTABLISHED | Write Enable depends on physical contact closure. **Boundary:** No authorizable software action, execution evidence or effect. |
| Link Loss value — reference question | NO_ESTABLISHED | VSWR is an RF impedance mismatch criterion. **Boundary:** Not definition or resolution of ISA-Q002 Link Loss concept. |
| Signal Strength Ratio — reference quantity question | NO_ESTABLISHED | Voltage standing wave ratio is specifically defined for mated RF contacts. **Boundary:** Not established as ISA signal-strength ratio concept ISA-Q004. |

Each comparison has exact original stable source IDs in the JSON inventory; physical pin designations are **not** digital observation fields, VSWR is **not** reported signal power, and hardwired Write Enable is **not** an authenticated CSAPI software Command. Source-graded comparisons are not owner approval of DIM classes, cardinality, Profile SHALLs or actual hardware conformance.

## Exact unresolved source/original evidence holds

- **SOSA-G2-7M-Q01:** Original J7 pinout figure 13.5.2.8-1 has not been verified at full image/contact geometry; Table source rows are text-read.
- **SOSA-G2-7M-Q02:** Original J8 pinout and SMPM size12 mating diagrams 13.5.2.9-1/-2 were not independently verified visually.
- **SOSA-G2-7M-Q03:** Original J9 pinout and BMB size8 mating diagrams 13.5.2.11-1/-2 were not independently verified visually.
- **SOSA-G2-7M-Q04:** Original dense modality checkbox placement in J7/J8/J9/auxiliary RF tables remains unverified; text pins and frequency bounds were inspected.
- **SOSA-G2-7M-Q05:** Original ANSI/VITA76.0 full source, Meritec-equivalent connector compliance and shell-plating measurements were not examined.
- **SOSA-G2-7M-Q06:** J7 Table 13.5.2.8-1 contains an unnumbered same-shell-plating SHALL distinct from the 27 numbered Rules; preserve exact native standing.
- **SOSA-G2-7M-Q07:** J7 table refers to USB3.0/2.0 while numbered Rule13.5.2.8.2-1 requires USB3.1 G2; do not silently harmonize scope or versions.
- **SOSA-G2-7M-Q08:** Original IEEE802.3an-2006, USB3.1/2.0, DisplayPort1.3, SATA3.0 and TIA232 native specifications were not read.
- **SOSA-G2-7M-Q09:** J7 WR_EN_RTN versus WR-EN_RTN spelling differs in original Rule13.5.2.8.6-2; preserve source text without inventing a second pin.
- **SOSA-G2-7M-Q10:** J7 maintenance Write Enable is a physical hardware closure, not a network-issued CSAPI software Command or verified equipment action.
- **SOSA-G2-7M-Q11:** J8 original SAE AS39029/56, MIL-DTL38999 and MIL-STD348B Change3 connector originals remain unexamined.
- **SOSA-G2-7M-Q12:** J9 original SAE AS39029/59, MIL-DTL38999 and MIL-STD348B Change3 connector originals remain unexamined.
- **SOSA-G2-7M-Q13:** J8 frequency-banded VSWR limits 1.25:1/1.30:1/1.40:1/1.60:1 are design criteria; no actual mated pairs were tested.
- **SOSA-G2-7M-Q14:** J9 1.40:1 DC–22GHz VSWR limit is original design criterion, not a measured link-quality or RF power reading.
- **SOSA-G2-7M-Q15:** J8 up-to-50GHz and J9 up-to-22GHz described antenna-channel families do not establish operational frequencies or device signal quality.
- **SOSA-G2-7M-Q16:** Auxiliary TNC/SMA/2.4mm/1.0mm RF interfaces have application-specific quantities; there is no universal required quantity or actual installed connector.
- **SOSA-G2-7M-Q17:** The original C239 DSDM, IDL and six OpenAPI companion bytes, later 2025 S251 and restricted Appendix C remain unexamined.
- **SOSA-G2-7M-Q18:** None of the four empirical source cases establishes installation or conformance of these J7/J8/J9 RF source-specific connectors.
- **SOSA-G2-7M-Q19:** No mandatory DIM chassis/class/cardinality, CSAPI Profile SHALL, real device command or independent runtime conformance was adopted.

**Mandatory work-product boundary:** Earned source correspondences must appear in the same canonical JSON, **both CSV mirrors, both GitHub-readable comparisons and the same original 26-sheet Excel**, with all saved cells verified and earlier other-donor/case/ISA evidence preserved; one new owner Proceed then may start **G2-7N §§13.5.2.13–13.5.2.19.2**, no automatic G3/donor/model transition.
