# Step 04 — Candidate B Evidence Audit: Raspberry Shake & Boom

**Version:** 0.1 · **30 October 2026, America/New_York**  
**Standing:** **STEP 04 COMPLETE; CANDIDATE B CONDITIONAL — NOT A QUALIFIED PRIMARY CASE.** The documentary evidence is useful, but a candidate-applicable native record or original example was not successfully retrieved and inspected. A located download is not an acquired dataset.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`.  
**Authority:** [Controlled-corpus plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 04; [unchanged Step 01 criteria](01_Eligibility_and_Evidence_Gates.md); [Step 02 audit assignment](02_Discovery_and_Four_Audit_Slots.md). The owner's separate “proceed” authorized this candidate only.  
**Purpose:** Evidence for the future Domain Information Model (DIM), separate OGC API – Connected Systems (CSAPI) Profile and common System Resource Details experience—not model adoption or implementation.  
**Pre-step research revision:** `65973f72628291d62e365227d183b8a192fe3a9f`.

## A. What we learned, and exactly which case we examined

Raspberry Shake & Boom offers a promising connection between a documented combined instrument and a specifically identified historical station. However, this audit obtained equipment and interface descriptions, not the station's waveform or response-file contents. The distinction matters: evidence that a provider publishes data does not establish that this research has inspected usable records. Candidate B therefore remains **CONDITIONAL**, rather than being counted as a passing case on the strength of links.

The reference subject is the **RS&BOOM V3 combined seismic/infrasound instrument**, using the manufacturer's documented standard arrangement: combined sensing electronics, vertical geophone, pressure transducer, Raspberry Pi computer, microSD storage, enclosure, external low-voltage supply and network connection. The specification describes a Raspberry Pi 3 Model B arrangement; compatible alternatives are not an installed inventory. The documentary basis is the RS&BOOM section dated **15 August 2023**, supplemented by the model-specific manual and hardware history. It is not a new instrument assembled by the analyst. [B01–B03]

The separate historical-record lead is **AM.R9D92.00**, explicitly identified by the manufacturer as **RS&BOOM V3**, with **EHZ and HDF** channels. This is a manufacturer attribution, not our physical inspection. No assertion is made that its actual Pi revision, filter, enclosure, software or power arrangement matches every detail of the reference description. The linked earthquake example concerns **22 July 2018**, not present operating state. [B08]

This is relevant to the original unattended sensing use case because it combines two sensing modalities in one equipment arrangement. It is not evidence of equivalent military surveillance functionality, detection classification, ruggedness or command interfaces. The documentary case, historical station lead and shared software examples remain separate evidence scopes.

## B. Source manifest, editions and access

All web sources below were inspected on **30 October 2026, America/New_York**. Unless an edition is stated, the date is an access date for mutable documentation—not a release identifier. Links and short attributed findings are retained; no manufacturer PDF, waveform archive, credentials or private installation information is redistributed. Each source label applies only to the claim inspected.

| ID | Primary source and exact locator | Evidence obtained and applicability limit |
| --- | --- | --- |
| **B01** | Raspberry Shake, [Raspberry Boom (RBOOM/RS&BOOM) Infrasound Monitors](https://manual.raspberryshake.org/boom.html), Manual; Mechanical Filters; Installation. | **PRIMARY_DESIGN_OR_SPEC.** Read. Distinguishes the pressure-only RBOOM from combined RS&BOOM; shared software does not make their hardware equivalent. Describes default/optional mechanical filtering. No actual filter inventory obtained. |
| **B02** | Raspberry Shake, [Global Technical Specifications](https://manual.raspberryshake.org/_downloads/52fa676cd01d82be3c9d2babec71408d/RSGlobalTechnicalSpecificationsDocument.pdf), RS&BOOM/RBOOM section dated **15/08/2023**, PDF pp.32–46. | **PRIMARY_DESIGN_OR_SPEC.** Parsed text plus screenshots of pp.32, 33, 35, 40, 45 and 46 inspected. Supports bounded assembly and input-power facts; shared RBOOM passages are not automatically RS&BOOM-only facts. No original-byte checksum or comprehensive schematic audit. |
| **B03** | Raspberry Shake, [Change log](https://manual.raspberryshake.org/changelog.html), Hardware → RS&BOOM/RBOOM; Software → Most recent. | **PRIMARY_DESIGN_OR_SPEC.** Read. V3 mass-production release June 2018; later V5 and V6 separately listed. Software page lists **21.2, 23 March 2026**, at capture. Neither the current software listing nor automatic-update policy proves R9D92's historical or current installed release. |
| **B04** | Raspberry Shake, [Quick Start Guide](https://manual.raspberryshake.org/quickstart.html), setup and configuration; [Assembly Guide](https://manual.raspberryshake.org/assembly.html), product assembly navigation. | **PRIMARY_DESIGN_OR_SPEC.** Read relevant setup material. Supports network/power/setup context, not a retrieved RS&BOOM configuration export or a tested assembly. |
| **B05** | Raspberry Shake, [Station Naming Convention](https://manual.raspberryshake.org/stationNamingConvention.html), station and component-code descriptions. | **PRIMARY_DESIGN_OR_SPEC.** Read. Supplies naming scope and distinctions among EHZ, HDF and other models' channels. A station identifier is not automatically a persistent identity for every constituent. |
| **B06** | Raspberry Shake, [Metadata—Instrument Response Files](https://manual.raspberryshake.org/metadata.html), Overview; Automatic metadata generation; RS&BOOM V3+ templates; template instructions. | **PRIMARY_DESIGN_OR_SPEC.** Page read. Nominal responses, epochs and model/filter-specific links are documented. Linked XML contents were not exposed by the browsing tool or downloaded to the runtime. No values inside those files are treated as inspected. |
| **B07** | Raspberry Shake, [FDSN Web Services](https://manual.raspberryshake.org/fdsn.html), service introduction, waveform/metadata sections and limits. | **PRIMARY_DESIGN_OR_SPEC.** Read. Describes Federation of Digital Seismograph Networks (FDSN) access, miniSEED waveforms and XML metadata. Service documentation is not an actual station response. |
| **B08** | Raspberry Shake, [How does the Raspberry Shake compare to a broadband seismometer?](https://manual.raspberryshake.org/bru2.html), instrument list; Instrument Response files; Continuous waveform data; Example 1. | **PRIMARY_DESIGN_OR_SPEC** for provider attribution and retrieval instructions. Read. The provider links an original historical R9D92 record; its bytes remain **UNAVAILABLE_OR_UNVERIFIED in this audit**. Performance-comparison claims and figures were not independently tested. |
| **B09** | Raspberry Shake, [Local Shake Monitoring](https://manual.raspberryshake.org/shakemon.html), checks and Combined example. | **PRIMARY_DESIGN_OR_SPEC + PRIMARY_PUBLISHED_EXAMPLE.** Read. Local reachability, service, storage and archive checks. Example includes EHZ and EN* paths, not an attributed RS&BOOM health record; its displayed status is not assigned to R9D92. |
| **B10** | Raspberry Shake, [FAQ](https://manual.raspberryshake.org/FAQ.html), low-power warning; downloading logs; shared software. | **PRIMARY_DESIGN_OR_SPEC.** Read targeted sections. Documents local warning/log access, not measured voltage or an actual unit's diagnostics. No local device was contacted. |
| **B11** | Raspberry Shake, [Data Producer UDP Port Output](https://manual.raspberryshake.org/udp.html), Output Format and DATACAST configuration. | **PRIMARY_DESIGN_OR_SPEC + PRIMARY_PUBLISHED_EXAMPLE.** Read. User Datagram Protocol (UDP) format is documented; the explicit numeric example is labeled **RS1D**, so it cannot be relabeled RS&BOOM. |
| **B12** | Raspberry Shake developers, `raspishake/rsudp`, verified commit **467e8c01fbc878232487e1fcca62da03426f4eaf**: [testing documentation](https://github.com/raspishake/rsudp/blob/467e8c01fbc878232487e1fcca62da03426f4eaf/docsrc/testing.rst) and [testdata](https://github.com/raspishake/rsudp/blob/467e8c01fbc878232487e1fcca62da03426f4eaf/rsudp/test/testdata), first six lines. | **PRIMARY_DESIGN_OR_SPEC + PRIMARY_PUBLISHED_EXAMPLE** for developer testing, not acquired RS&BOOM telemetry. Text read through GitHub. Observed blobs: documentation `8d7dc0397beeef6e843bbb4f55894b8346441229`; data `3bad4b2fc40e0069fd998a7cae3379ddeec2eb03`. Inspected excerpt contains EHZ, ENE and ENN, without a demonstrated candidate join. Full test suite and binary fixture were not run/read. |
| **B13** | Raspberry Shake, [License](https://raspberryshake.org/license/), Legacy & FDSN Web Services; Redistribution of Legacy Data; application integration. | **PRIMARY_DESIGN_OR_SPEC** for the provider's published access/reuse terms. Read. Access and redistribution are different permissions. This audit makes no determination that this project's eventual use qualifies for a particular free-use category and acquires no new permission. |

**Evidence vocabulary:** No candidate record was established as **REAL_RECORDED**. No outside synthesis substitutes for primary material. Analyst arithmetic below is **SYNTHETIC_OR_DERIVED** reasoning, not a new sensor value. Uninspected files and unknown applicability stay **UNAVAILABLE_OR_UNVERIFIED**.

## C. Eligibility gates

| Gate | Result | Reason and exact boundary |
| --- | --- | --- |
| **G1 — Bounded sensing configuration** | **MET, reference scope** | B01–B04 establish a combined sensing arrangement rather than an unspecified controller. V3 is identified separately from later hardware. The documentary reference is not an authenticated installed bill of materials. |
| **G2 — First-party whole-System account** | **MET** | B01–B04 and B09–B11 cover assembly, power input, communication, operation, settings and diagnostic mechanisms. The consumption inconsistency below and missing actual state remain explicit; neither is filled by inference. |
| **G3 — Inspected usable candidate record/example** | **UNVERIFIED** | A specifically attributed record was located (B08), but neither waveform nor response contents were acquired. B09/B11/B12 examples do not establish the required RS&BOOM applicability. A nominal response-template link alone does not meet this gate. |
| **G4 — Traceability and honest evidence limits** | **MET for documentary review only** | Sources, editions, failed retrievals and known reuse restrictions are recorded. No data use/redistribution authorization or verified documentation-to-record join is asserted. This is not a frozen reusable dataset. |

**Verdict: CONDITIONAL.** The unresolved gate is specific and potentially resolvable, not a demonstrated absence of product data. Under Step 01, this result does **not** count as a qualified primary case. The audit step is complete because its bounded finding is documented; qualification is not forced.

## D. Shared questions and coverage

| Question | Supported answer and what remains unknown |
| --- | --- |
| **Q1 — What exactly is the case?** | A source-described combined V3 instrument, with a separate named historical-record lead. Hardware revision, software version, station ID and channel ID are different facts. Do not attach current documentation values to an uninspected 2018 record. [B03, B05, B08] |
| **Q2 — What is included?** | Two sensing functions share supporting electronics, computing, storage and power. The nominal reference is not a verified station inventory; optional filtering and other installed choices remain unknown for R9D92. [B01, B02, B08] |
| **Q3 — What can be configured?** | Shared setup/DATACAST instructions describe selectable forwarding and destinations. These are supported choices, not obtained selected state, command acknowledgements or successful execution. [B04, B11] |
| **Q4 — What condition information exists?** | Low-power warning, logs and local checks are documented. No candidate power trace, health history, remaining-capacity percentage or readiness verdict was acquired. [B09, B10] |
| **Q5 — What can we inspect now?** | Equipment/interface prose and other-model developer examples. Candidate waveform/response bytes, configuration export and attributable diagnostic records remain uninspected. [B06–B12; §E] |
| **Q6 — Do records and documentation join?** | The provider explicitly joins a station to a model, but our verification cannot proceed into file headers, record times, response epochs, units or installed configuration without the files. No cross-file join has passed. [B08; §E] |
| **Q7 — Is the evidence repeatable?** | Specific source paths and failed attempts are recorded. Mutable pages, unacquired bytes and reuse restrictions prevent calling this a frozen publicly redistributable packet. [B12, B13; §E] |
| **Q8 — What should a common Details view preserve?** | Proposed research implications: keep whole equipment separate from channels; nominal description separate from installed state; raw counts separate from interpreted quantities; and a reachable service separate from healthy equipment. These are questions to test, not adopted model rules. |

**Category coverage:** Whole-System, kind/version/capability, communication and possible configuration have documentary support. Condition has descriptions of mechanisms but no candidate status record. Measurement has a strong attributed retrieval lead but no inspected sample. Actual configuration, actual status and actual observation availability therefore remain separately unverified—not collapsed into one “data available” label.

## E. Small-record investigation and access outcomes

The targeted historical example is `eq20180722a-r9d92.ms`, linked by B08. The provider's retrieval command requests **AM.R9D92.00.EHZ**, **2018-07-22T11:23:00 through 11:25:00**. This does not establish that the file contains the HDF channel too. The named instrument has two channels, but a request for one channel is not evidence for both.

| Attempted source | Actual outcome | Consequence |
| --- | --- | --- |
| [Original linked miniSEED example](https://manual.raspberryshake.org/_downloads/ff6abc66520a48428d6f665bd47dcbb4/eq20180722a-r9d92.ms) | Browser tool did not expose bytes and reported a fetch/format error; direct runtime request and download failed. Runtime log records DNS resolution failure at **04:14:34 UTC, 30 October 2026**. | No waveform parsed, no byte checksum, no sample count or measured value verified. This is not evidence that the origin file is absent. |
| [Provider-linked R9D92 response](https://data.raspberryshake.org/fdsnws/station/1/query?format=sc3ml&level=resp&network=AM&station=R9D92) | Browser rejected `application/xml`; runtime request failed DNS resolution at **04:14:34 UTC**. | Metadata existence is a lead; contents, epochs and instrument parameters remain unverified. An unsupported content type is not an authentication failure. |
| [V3+ 1-second nominal XML template](https://manual.raspberryshake.org/_downloads/e3a34ac4fe6b742fcf00ac7e3665d815/RSnBV3-1s.dataless.xml-reformatted.xml) | Browser rejected `text/xml`; runtime request failed DNS resolution at **04:14:39 UTC**. | No template fields were checked. This would in any case be nominal model evidence, not proof of the station's actual filter or state. |
| Channel-level text query for R9D92 | Browser could not retrieve the requested response. | No inspected alternative station record. |
| Official rsudp test excerpt, B12 | Text successfully inspected; first three packets use EHZ, ENE and ENN. | The excerpt does not establish RS&BOOM provenance. It is not used to repair G3. |

These were limited read-only attempts, not station access, authenticated requests, continuous subscriptions or bulk archive downloads. The local acquisition log records failed requests, not successful retrievals. No instrument-response removal, miniSEED decoder, waveform calibration, live receiver or producer/client transformation was run.

### Field-level distinctions supported by the documentation—not a decoded candidate record

| Native item | Source meaning / locator | What remains unproven |
| --- | --- | --- |
| `AM.R9D92.00.EHZ` / `HDF` | Network/station/location/channel context; EHZ vertical seismic and HDF infrasound naming. [B05, B08] | No file-header match or independent hardware identity verification. |
| Nominal response; epochs | Response descriptions supply interpretation context and time-dependent applicability. Templates require station/date substitutions. [B06] | No inspected candidate gains, units, epoch coverage or calibration certificate. |
| DATACAST channel, timestamp, integer samples | UDP format includes one channel, first-sample epoch time and integer values; other context must be obtained separately. [B11] | Its printed RS1D packet is not a candidate sample or an RS&BOOM configuration. |
| `Reachable`, service availability, disk use | Local checks answer different host/service/storage questions. [B09] | No aggregate health assertion and no candidate-specific status history. |

## F. Material limitations to retain

**Power-source inconsistency:** B02 p.46 prints startup **5 V × 0.550 A = 3.1 W** and runtime **5 V × 0.290 A = 1.9 W**. Arithmetic gives **2.75 W** and **1.45 W**, respectively. This establishes an internal inconsistency, not which printed quantities correctly describe hardware. Do not silently choose one value, construct a battery budget from it or convert it into measured consumption. The separately documented input-supply requirement remains usable.

**Version and interpretation limits:** The current software listing cannot be retroactively assigned to historical recordings. Distinct filter variants require the appropriate response. Published metadata locations may be obfuscated; they are not automatically exact installation coordinates. A nominal response is not evidence of an individual calibration event. [B03, B06]

**Access is not reuse permission:** B13 describes permitted research access categories, commercial-use conditions and restrictions on redistributing server-obtained waveform data through another server or application. This matters to a future CSAPI/Glaux experiment even after retrieval succeeds. Record the intended use and obtain appropriate permission where required; this audit does not declare an exemption, legal compliance or unrestricted republication. No waveform data is checked into the repository.

**No wrong-model substitution:** RBOOM, RS1D, RS4D and RS&BOOM evidence remains distinct. Shared software helps interpret interface possibilities but does not turn a differently sourced example into this equipment's state. Later corpus selection must preserve this conditional result rather than counting its documentation as a complete data packet.

## G. Six evidence-depth scores—no aggregate

| Dimension | Score | Evidence and ceiling |
| --- | ---: | --- |
| Whole-System component/architecture depth | **2** | Useful bounded design/assembly account. No independently verified installed inventory or comprehensive hardware source audit. [B01–B04] |
| Capability/configuration depth | **2** | Supported settings and fixed operating details described. No actual candidate configuration record obtained. [B01–B04, B11] |
| Operational condition/power/diagnostic depth | **2** | Specific local diagnostic mechanisms and input-power context, with the conflicting consumption figures explicitly excluded from confident use. No status history. [B02, B09, B10] |
| Machine-readable source/communication depth | **1** | Formats and exact candidate download leads located, but no inspected usable candidate record/example. Other-model examples do not raise this score. [B06–B12] |
| Actual attributed observations/history | **0** | No qualifying waveform/telemetry extract obtained. Provider attribution is not counted as successful data acquisition. [B08; §E] |
| Reproducibility/version/rights | **2** | Exact locators, document dates, GitHub provenance, access failures and restrictions recorded. No candidate byte-level snapshot or authorized rehosting established. [§B, §E, B13] |

The scores describe the evidence obtained, not equipment quality. A good design score cannot compensate for unresolved G3.

## H. Verdict, supported uses and handoff

**CONDITIONAL / NOT QUALIFIED AS A PRIMARY CASE.** Documentary research can use this case now to examine equipment/channel identity, response applicability, configuration possibilities and the distinction between public observations and local management. It cannot yet underpin a reproducible candidate-data experiment, actual operating-state fidelity assessment or source-to-CSAPI-to-client proof.

The immediate evidentiary condition is a successfully inspected, attributable RS&BOOM observation/status/configuration record or original applicable example with sufficient definitions and provenance. For calibrated waveform use, the matching response and time applicability would also need verification; for republication, the intended rights would need resolution. No new live-hardware requirement is introduced, and an appropriate original example could still satisfy the existing gate.

**Step 04 is complete despite the conditional candidate verdict.** Candidate A remains unchanged; C and D are unstarted. No eligibility criteria, frozen donor inventory, candidate DIM v0.2, Profile, application code or deployment was changed. This report is not a final corpus decision and does not authorize indefinite retries or another equipment audit.

**Next separate “proceed”: Step 05 only—Dragino S31-LB external-probe, battery-powered node.** Pin its applicable variant/region/firmware, inspect original configuration/status/measurement material and apply the same gates. Do not borrow S31B construction or LS solar features, reopen A/B automatically, audit D, select the final corpus or change Glaux.
