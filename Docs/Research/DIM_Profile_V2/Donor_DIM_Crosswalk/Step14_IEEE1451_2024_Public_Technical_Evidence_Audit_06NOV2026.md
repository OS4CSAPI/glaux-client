# Step14 — IEEE 1451.0-2024 public publisher and NIST/Playground technical evidence review

**6 November 2026 · Source-focused Step14 only · Five earlier IEEE correspondences reviewed; one carefully related TIM UUID entry added; fourteen additional source-native technical concepts held. Full IEEE 1451.0-2024 normative text NOT inspected.**

## 1. What has actually been verified

IEEE Standards Association's [publisher page for IEEE 1451.0-2024](https://standards.ieee.org/ieee/1451.0/11001/) confirms the active edition (published 26 June 2024) and its scope: Network Capable Application Processor (NCAP), Transducer Interface Module (TIM), application↔NCAP network services, NCAP↔TIM transducer services, and Transducer Electronic Data Sheet (TEDS) descriptions. [NIST's December 2024 account of the IEEE 1451 Playground](https://www.nist.gov/news-events/news/2024/12/nist-and-university-researchers-present-online-tool-support-ieee-standards) separately confirms that the online tool was demonstrated to illustrate and validate TEDS, network messages and transducer service messages. The [University of Beira Interior/IML IEEE 1451 Playground](https://iml.ubi.pt/playground/docs/ieee1451/intro/) exposes concrete TEDS field names and service-message examples attributed to the 2024 edition.

**Evidence classification:** The IEEE SA publisher scope is an *original publisher source* for the standard's existence and advertised scope. The Playground is *public technical educational material derived from the standard*, not the licensed IEEE normative text itself. We did **not** inspect the underlying 2024 normative requirement sentences, independent IEEE validation reports, or every 2024 official schema file, even though the IEEE publisher links an open-source schema project. Therefore the six correspondences are **PUBLIC_TECHNICAL_CHECKED, NORMATIVE_TEXT_UNINSPECTED**, not ORIGINAL_2024_NORMATIVE_CLAUSE_CHECKED and not an IEEE conformance assertion.

This is materially more detailed IEEE 1451 evidence than merely reading a standard title: the public field tables supply real `MetaTEDS.UUID`, `SampMode`, `SDefault`, channel-type, unit, timing, calibration-key and protocol-role terms. But checking those public descriptions cannot establish an installed TIM, the observed values of a particular probe, or manufacturer-signed electronic self-description.

## 2. Six donor-to-DIM mapping decisions

| Proposed DIM element | Exact IEEE/public technical term | Relation | Original/public technical locator | Critical qualification |
|---|---|---|---|---|
| S06-R006 — Network-visible participant | `Network Capable Application Processor (NCAP)` | **RELATED** | IEEE SA 1451.0-2024 published scope (NCAP/1451 server); IML Playground Network Services §10, Table 54 APP↔NCAP | Network-facing service function is not every network-visible physical device, a sensor probe, a gateway by label alone, or a guaranteed CSAPI System resource. |
| S06-R007 — Physical constituent | `Transducer Interface Module (TIM)` | **PARTIAL** | IEEE SA 1451.0-2024 published scope (TIM); IML Playground Transducer Services §11, Tables 64–70 | An architectural TIM role does not prove separately identifiable physical part, enclosure, installed component identity or containment relation. |
| S06-R011 — Addressed transducer channel | `TransducerChannel` | **DIRECT** | IML Playground transducer-channel TEDS §6.5 / Table 19; Transducer Services §11.1.3 (TIM and channel identifiers) | Not necessarily one physical sensor or probe, LoRaWAN FPort, SDI-12 address, reported output field, SWE DataRecord item or CSAPI DataStream. |
| S06-R016 — Supported operating mode | `SampMode (sampling capability)` | **PARTIAL** | IML Playground 1451.0-2024 TransducerChannel TEDS §6.5 / Table 19, Sampling.SampMode | Capabilities are not evidence of the mode actually selected or executed, and are not universal operating-mode descriptions for the whole sensing System. |
| S06-R017 — Declared default mode | `SDefault (sampling mode default)` | **PARTIAL** | IML Playground 1451.0-2024 TransducerChannel TEDS §6.5 / Table 19, Sampling.SDefault | A manufacturer/default TEDS value does not prove a fielded unit's actual current or historical mode, or a whole-System default. |
| S06-R004 — Persistent System identifier | `MetaTEDS.UUID (TIM identifier)` | **RELATED** | IML Playground 1451.0-2024 Meta TEDS §6.4 / Table 13 (UUID); Network Services §10 (timId) | TIM UUID is not automatically a CSAPI System URI, persistent station ID, manufacturer serial number, or authenticated identity of a deployed individual; fielded existence and issuer authority unproven. |

The **five old source claims have better, edition-specific locators**, qualified meaning and explicit provenance grade; none was automatically promoted to normative 2024 clause verification. A sixth `MetaTEDS.UUID (TIM identifier)` entry was added to the **already proposed** persistent-System-identifier row as **RELATED**, because a network-addressed TIM can have an identifier but that identifier is **not** necessarily the CSAPI System URI, station identifier or serial number of an authenticated field device. This is one additional donor cell, **not one new DIM requirement or class**.

## 3. Fourteen public technical concepts kept for synthesis

| Lead | IEEE/public documentation concept | Source standing | Why held |
|---|---|---|---|
| IEEE-H01 | `Meta TEDS: MaxChan, CGroup, VGroup, Proxies` | PUBLIC_2024_TECHNICAL | Channel counts, control/vector groupings and proxy channels are declarations, not individual physical probes, physical wiring or installed count verification. |
| IEEE-H02 | `TransducerChannel TEDS: PhyUnits, UnitType, UnitsExt` | PUBLIC_2024_TECHNICAL | Units and channel data model metadata do not alone identify the observed feature, original measurement result, CSAPI schema or object identity. |
| IEEE-H03 | `TransducerChannel TEDS: CalKey; optional Calibration TEDS` | PUBLIC_2024_TECHNICAL | Calibration method/coefficients or schedule are not automatically actual calibration event, certification, observed quality or field-history evidence. |
| IEEE-H04 | `LowLimit, HiLimit, OError, SelfTest, MRange` | PUBLIC_2024_TECHNICAL | Design limits, worst-case uncertainty and self-test capability differ from current diagnostics, measured uncertainty and performed self-test result. |
| IEEE-H05 | `SPeriod, UpdateT, WarmUpT, RSetupT, TimeSrc, TSError` | PUBLIC_2024_TECHNICAL | Declared sampling/timing parameters and timing-source metadata are not original phenomenonTime or resultTime of NOAA means or fielded applied settings. |
| IEEE-H06 | `User’s Transducer Name TEDS: TCName` | PUBLIC_2024_TECHNICAL | Readable/user-defined names do not equal individual factory serial numbers, uniquely verified equipment identity or deployed station identifiers. |
| IEEE-H07 | `TransducerChannel TEDS: ChanType; Sampling/Sample/DataSet` | PUBLIC_2024_TECHNICAL | Transducer channel type or data-model descriptors are not a guarantee of one physical sensor, one output field, or one actual sampled event. |
| IEEE-H08 | `Network Services: discovery, transducer access, TEDS access, event notification` | PUBLIC_2024_TECHNICAL | IEEE APP↔NCAP service message types are distinct from native CSAPI REST resources, interfaces or proof of a real registered network participant. |
| IEEE-H09 | `TIM/Transducer Service Commands: Query/Read/Write/Update TEDS, Run self-test` | PUBLIC_2024_TECHNICAL | Documented command/service types are affordances; they do not prove an issued request, authenticated permission or actual hardware action. |
| IEEE-H10 | `Transducer service reply: Success/Fail, ErrorCode and status condition` | PUBLIC_2024_TECHNICAL | Protocol reply or self-test status is not independent evidence that the requested physical effect occurred or was observed. |
| IEEE-H11 | `Optional Geographic Location TEDS` | PUBLIC_2024_TECHNICAL | Optional or manually entered installation location cannot establish surveyed per-probe coordinates, original location precision or time-dated deployment without source evidence. |
| IEEE-H12 | `Optional Security TEDS / Time Synchronization TEDS` | PUBLIC_2024_TECHNICAL | Declaration of a supported security or time synchronization protocol does not establish the current authorization configuration, signed original issuer claims or absolute resultTime. |
| IEEE-H13 | `PHY TEDS: Radio / Battery / Encrypt / Authent` | SEPARATE_IEEE_1451_5_2007 | THIS IS A DIFFERENT IEEE FAMILY STANDARD AND 2007 EDITION, NOT PROOF IEEE 1451.0-2024 REQUIRES THESE FIELDS; Battery indicates design/power type, not present charge level. |
| IEEE-H14 | `Historical NIST TEDS overview: manufacturer, serial, calibration descriptions` | HISTORICAL_NIST_NOT_2024_CLAUSE | NIST historical description cannot verify a particular 1451.0-2024 normative field path, a modern TIM self-ID value, or a serial-numbered installed transducer. |

The held list is selected and bounded, not an exhaustive normative inventory. It deliberately preserves channels, metadata, unit and calibration descriptions, discovery and message types, physical-layer configuration, power, diagnostics and control while avoiding forced equivalence with the initial twenty-two DIM labels.

## 4. Crucial mixed-edition issue: PHY TEDS is not proof of IEEE 1451.0-2024 obligations

The public Playground [PHY TEDS form](https://iml.ubi.pt/playground/docs/ieee1451/teds/phy-teds/) explicitly attributes its `Radio`, `Battery`, `Encrypt` and `Authent` details to **IEEE 1451.5-2007 §5.3 / Table 2**. The [same Playground's TransducerChannel TEDS form](https://iml.ubi.pt/playground/docs/ieee1451/teds/transducer-channel-teds/) attributes `Sampling.SampMode`, `SDefault`, `PhyUnits`, `SPeriod` and other fields to **IEEE 1451.0-2024 §6.5 / Table 19**. These are distinct family standard editions. **Do not label PHY TEDS battery/power fields as verified mandatory 1451.0-2024 attributes, and do not turn a design `Battery` indicator into an actual state of charge.**

The [NIST historic TEDS overview](https://www.nist.gov/el/intelligent-systems-division-73500/transducer-electronic-data-sheet) describes older STIM-based TEDS holding manufacturer and serial information, but it cannot substantiate an exact 2024 TIM field or vendor serial mapping. In the same way, the University-created 2022 IEEE 1451 ontology is useful research history, not an official replacement for 2024 normative text. We have kept the edition/source boundaries in the audit instead of relying on their apparent terminology similarity.

## 5. Four equipment examples prevent mistaken mappings

**Dragino S31-LB.** A documented LoRaWAN FPort does not become an IEEE `TransducerChannel` merely because it transports temperature and humidity from one external SHT31. The 20-minute manufacturer default and unrelated printed 60-second command example cannot be treated as deployed `SampMode` or `SDefault` values without an actual IEEE TIM/TEDS source.

**AirGradient Open Air Max.** Two PMS5003 physical components in the reference design are distinct from three particulate properties. No original IEEE 1451 TIM UUID, channel TEDS, physical configuration or 1451 NCAP service has been identified in the reference case, so the standard describes a possible mapping vocabulary rather than an authenticated vendor implementation.

**Campbell CR1000X + ClimaVue 50.** A first-generation ClimaVue response with fourteen fields is not fourteen IEEE transducer channels, and its SDI-12 address is not automatically a 1451 channel address. The separate 31-field logger Status publisher example includes panel temperature unrelated to ambient air temperature; there is no verified common fielded IEEE interface or installed configuration.

**Bennett's Point.** The historical station `acebpmet`, two serial-numbered EE181 probes, dated maintenance, two original NOAA mean observations and four project API representations are **not** evidence that 1451 Meta TEDS `UUID`, actual `TIM` or `TransducerChannel` values were present. Original quality token `F_ATemp="<0> "` (trailing space retained), separate blank `F_Record` and unknown original resultTime stay unchanged. No 1451 TIM ID can be inferred from station site coordinates or logger/probe serials.

## 6. Evidence and preservation counts

**Previous v0.7:** 57 evidence records = 37 original-standard-source-reviewed + 20 prior-only, including 5 historical IEEE entries. **After Step14:** **58 donor evidence records** = 37 earlier original-standard-checked (OGC/W3C) + **6 IEEE publisher-and-public-technical checked (not normative 2024)** + **15 prior-only** (OPC Devices 6 and SAPIENT 9). The five existing IEEE comparisons retained their conceptual fit (1 DIRECT, 3 PARTIAL, 1 RELATED); the one new TIM UUID comparison is RELATED. **No** previous OGC/W3C clause record was rewritten.

There are still **13 owner-approved display columns**, six topic navigation dividers, 22 proposed DIM rows, nine case-review holds and 73 source-qualified equipment statements. No new DIM superclass, existing candidate model/Profile rule, UML, Glaux client/server, IEEE/CSAPI conformance test, actual hardware Command or Cloudflare deployment occurred.

## 7. Cited sources — Chicago 18 author-date

Institute of Electrical and Electronics Engineers (IEEE). 2024. *IEEE Standard 1451.0-2024: Common Functions, Communication Protocols, and TEDS Formats.* IEEE Standards Association, June 26. https://standards.ieee.org/ieee/1451.0/11001/

National Institute of Standards and Technology (NIST). 2024. “NIST and University Researchers Present Online Tool to Support IEEE Standards at 2024 IECON.” December 1. https://www.nist.gov/news-events/news/2024/12/nist-and-university-researchers-present-online-tool-support-ieee-standards

University of Beira Interior, Instrumentation and Metrology Laboratory (IML). 2024–26. *IEEE 1451 Playground: Meta TEDS, Transducer Channel TEDS, Transducer Services, and Network Services.* https://iml.ubi.pt/playground/docs/ieee1451/intro/

National Institute of Standards and Technology (NIST). 2009. “Transducer Electronic Data Sheet.” Historical educational overview. https://www.nist.gov/el/intelligent-systems-division-73500/transducer-electronic-data-sheet

## 8. Publication and independent GitHub readback

The [editable 13-sheet current v0.8 Excel master](Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026.xlsx), [full horizontal GitHub-readable master](Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026.md), [JSON source/evidence](Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026.json), and [CSV mirror](Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026.csv) have been committed to `research/dim-profile-v2`. GitHub workbook blob `9eba78d247e2e7364cbfb98f73ca09b85e36afa1` is **453,463 bytes**. [Publication/build validation](https://github.com/OS4CSAPI/glaux-client/actions/runs/42340875575) and a separate [independent check on the actual published workbook](https://github.com/OS4CSAPI/glaux-client/actions/runs/42340946419) both finished **SUCCESS**. These checks cover 13-sheet ZIP/XML validity, donor/evidence/CSV/JSON parity, the one new IEEE cell and original 37 OGC/W3C reviewed records, 15 still prior-only records, 14 held IEEE technical concepts, and complete source-case preservation.

The independently checked record is **37 original-standard-source-reviewed + 6 IEEE PUBLIC TECHNICAL + 15 prior-only = 58**. It must not be summarized as **43 clauses of 2024 and prior original standards verified**; no licensed IEEE 1451.0-2024 normative clause text was independently inspected. Neither workbook structure nor the Playground proves an operating device, native IEEE 1451 implementation, full OGC/IEEE interoperability or physical control effect.

## 9. Next authorized iteration

**Step14 public technical review is complete as an evidence-bounded mapping proposal.** The next distinct owner “proceed” is **Step15 ISA 6.0 only**, not Step16 owner checkpoint, further IEEE clause research, final ranking, or a new app implementation. The full 2024 normative text remains held until actually accessible and reviewed.