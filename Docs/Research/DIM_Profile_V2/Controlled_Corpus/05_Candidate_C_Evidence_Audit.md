# Step 05 — Candidate C Evidence Audit: Dragino S31-LB

**Version:** 0.1 · 30 October 2026 (America/New_York)  
**Standing:** **PASS FOR A DOCUMENTED EXTERNAL-PROBE / PRIMARY-BATTERY REFERENCE CASE AND ORIGINAL PUBLISHED EXAMPLES ONLY.** Not an authenticated installation, regional-firmware qualification, real telemetry dataset, final corpus selection or interoperability proof.  
**Authority:** [Controlled-corpus plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 05 only; unchanged [Step 01 gates and template](01_Eligibility_and_Evidence_Gates.md); [Step 02 audit assignments](02_Discovery_and_Four_Audit_Slots.md).  
**Purpose:** [Original problem/outcome baseline](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md): evidence for a later implementation-independent Domain Information Model (DIM), separate OGC API – Connected Systems (CSAPI) application Profile and common Resource Details experience.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; pre-step baseline `6c62b3184c2f50fcc0fcb870dbbee214c1782cd8`.

## A. What we obtained and what it means

We obtained an original, fully specified historical-message example and the manufacturer's linked decoder, then executed a small offline comparison. The example contains eight entries. It is useful evidence of a published representation, but neither its timestamps nor successful decoding authenticate an installed device. Unlike Candidate B's unresolved record-inspection problem, Candidate C's original example was actually inspected and processed. [C02, C03; §E]

The checks found useful limits as well as agreement: the decoder's calendar strings depend on the runtime timezone; its treatment of an all-zero no-data message produces apparent zero-valued records; and labels such as `Door_status` and `Node_type` should not be mistaken for independently verified equipment facts. These findings concern the inspected decoder and supplied inputs, not demonstrated defects in a physical sensor or an adopted Profile. No upstream code was modified. [C03; §E–F]

### Case boundary and version standing

The bounded subject is the **Dragino S31-LB**, with its **external three-metre SHT31 probe, enclosure, onboard electronics/radio and primary battery**, considered as a manufacturer-described reference product. The product page distinguishes its 8,500 mAh lithium-thionyl-chloride battery from the LS solar configuration and identifies Long Range Wide Area Network (LoRaWAN) Class A communication. Do not import the S31B's integrated-probe construction, LS charging behavior, or older LSN50v2 firmware. The gateway and server are communication dependencies, not automatically physical constituents of the node. [C01, C02]

| Scope to identify | What was established | What remains unverified |
| --- | --- | --- |
| Product/construction | S31-LB external-probe, primary-battery reference; manufacturer variant descriptions. [C01–C02] | Individual serial number, installed assembly, precise board revision and installation. |
| Board family | Manufacturer UART upgrade table associates S31-LB with the SN50v3 motherboard. [C05] | No schematic/BOM audit or particular board revision was established. |
| Region | Manufacturer lists regional order suffixes; the decoder has explicit frequency-band branches. [C01, C03] | The original historical example does not identify its region. No regional firmware, channel plan or radio-performance claim is qualified. The synthetic EU868 test below is not a real configuration. |
| Device firmware | Manual offers a firmware/changelog link and a version-field explanation. [C02, C06] | Linked folder contents were not exposed; no firmware binary/release was inspected. Decoder filename `v1.3` is not evidence of firmware 1.3 on any unit. |
| Decoder | `S31-LB_v1.3_TTN_decoder.txt`, pinned commit `635417693adb215b32ac367c8e8909d9d609a120`; exact blob verified locally. [C03] | No claim that every historic/deployed firmware uses this exact decoder contract. |

This is deliberately **not** a fabricated model/region/firmware installation. The qualification covers the documented construction and explicitly inspected example meanings, not a release-matched hardware/software bundle. Unknown region and firmware remain blockers for region- or release-dependent experiments; the Step 01 criteria permit bounded design/example research without inventing those facts.

## B. Primary sources, provenance and access

All access below occurred on **30 October 2026, America/New_York**. Source-owner statements are distinguished from our test results and research judgments. Mutable web pages are dated accesses, not immutable firmware editions. No credentials, registration keys or private device endpoints were used.

| ID | Owner, title and original locator | Standing, applicability and access limit |
| --- | --- | --- |
| **C01** | Dragino. [“S31-LB/LS — LoRaWAN Temperature & Humidity Sensor.”](https://dragino.com/products/temperature-humidity-sensor/item/264-s31-lb-ls.html) Features, specifications and order information; page displays last modified **25 June 2026**. | **PRIMARY_DESIGN_OR_SPEC**. Read. Product descriptions, not measured performance or an installed inventory. Product page states rights reserved; linked, not republished. |
| **C02** | Dragino. [“S31/S31B-LB/LS.”](https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/) §§1.4–1.8, 2.3–2.5, 2.7–2.8, 3.3 and 4–5. | **PRIMARY_DESIGN_OR_SPEC / PRIMARY_PUBLISHED_EXAMPLE**, assigned per claim. HTML text and full numeric §2.5.4 example inspected. Shared coverage explicitly includes S31-LB; does not identify which physical variant emitted an example. Screenshot-only payloads were not successfully retrieved and are not treated as inspected native records. No complete manual reproduced. |
| **C03** | Dragino. [“S31-LB_v1.3_TTN_decoder.txt.”](https://github.com/dragino/dragino-end-node-decoder/blob/635417693adb215b32ac367c8e8909d9d609a120/S31-LB%26S31B-LB/S31-LB_v1.3_TTN_decoder.txt) `decodeUplink`, `Decoder`, `datalog`, `getMyDate`; commit [6354176](https://github.com/dragino/dragino-end-node-decoder/commit/635417693adb215b32ac367c8e8909d9d609a120). | **PRIMARY_DESIGN_OR_SPEC**, specifically executable implementation evidence, not an independent standard. GitHub content read in full; local UTF-8 copy matched Git blob **59af776a4b7ce287dc4c3030763e215b31f645f8**, 3,786 bytes. No express redistribution license verified in this audit; vendor file is not bundled or committed. |
| **C04** | Dragino. [“How to calculate battery life of Dragino sensors.”](https://wiki.dragino.com/docs/FAQs/battery-life-calculation/) §§1.1, 1.3 and 4.0. | **PRIMARY_DESIGN_OR_SPEC**. Read selected sections. Explains non-linear battery voltage/capacity relationship and limits of battery-life estimates. No battery-life calculation or physical battery test performed. Other product-family examples on that page are not S31-LB measurements. |
| **C05** | Dragino. [“UART/TTL Upgrade Mode.”](https://wiki.dragino.com/docs/LoRaWAN-Firmware-Update/uart-ttl-upgrade-mode/) model/motherboard table. | **PRIMARY_DESIGN_OR_SPEC**. Relevant manufacturer table retrieved through web search. Supports board-family attribution only, not firmware interchangeability or installed revision. |
| **C06** | Dragino-linked [firmware/changelog folder](https://www.dropbox.com/sh/fis3g6nmhv0eokg/AAC6BcCZaX4BdqZkduUvZ3jIa?dl=0), from C02 §§2.8/5. | **UNAVAILABLE_OR_UNVERIFIED** contents. Link opened and redirected to a Dropbox folder; no usable file listing or release content was returned. No claim that firmware is absent or authentication is necessarily required. |

**Access outcomes:** Three C02 payload-image requests returned cache misses; a direct image request also encountered runtime name-resolution failure. Therefore no values were transcribed from those images. The original §2.5.4 numeric payload was readable in HTML and does not depend on the missing images. The decoder was obtained through GitHub; its locally reconstructed bytes match the independently returned blob identifier, rather than being an unchecked reimplementation.

**Reuse boundary:** This report and original harness retain a small factual numerical example and our findings, not a copied manual, device credentials, firmware distribution or vendor decoder. Future redistribution of additional source material needs its own verified permission basis. Public availability alone is not treated as a license. This is an access/provenance record, not a legal compliance opinion.

## C. Four eligibility gates

| Gate | Verdict | Evidence and limit |
| --- | --- | --- |
| **G1 — Bounded configuration** | **MET** | Product identifies a complete external-probe, battery-powered sensing node. The subject is a reference product, not an authenticated individual; regional/firmware limits are explicit. [C01, §A] |
| **G2 — First-party whole-System account** | **MET** | Product/operation sources address probe, electronics family, power, communication and control context. No claim of exhaustive schematics, security or maintenance coverage. [C01–C05] |
| **G3 — Usable native record/original example** | **MET** | C02 §2.5.4 contains a complete original numeric message example with definitions. Offline inspection and C03 execution agree on its eight temperature/humidity/time entries. This is not an actual device dataset. [§E] |
| **G4 — Reproducible, bounded provenance** | **MET for the stated scope** | Exact source locators, captured-access dates, decoder commit/blob, reproducible checker and gap ledger retained. Version-dependent claims, unavailable images and uncertain redistribution rights are not silently promoted. No whole deployment or release-pair compatibility is established. [§B, §E–F] |

**Verdict interpretation:** PASS makes this limited reference/example case eligible for Step 07 comparison. It does not qualify all regional/firmware variants or admit an operating installation. Requiring a real deployment now would change the criteria; pretending the missing version evidence exists would also change them. Neither was done.

## D. Shared questions and evidence coverage

| Step 01 question | Source-based answer and research boundary |
| --- | --- |
| **Q1 — What is it?** | S31-LB reference configuration in §A. C03 emits `S31-LB` labels from code; these do not prove a hardware serial identity. |
| **Q2 — What is included?** | One cabled SHT31 probe supports two environmental quantities. Product-specific physical construction is taken from C01, not inferred from output-key count. No door switch is established. |
| **Q3 — What can be configured?** | Original command examples and decoder branches for threshold replies are inspectable. Supported actions, hypothetical test settings and an actual accepted/applied configuration are different evidence levels. No command was sent. [C02–C03] |
| **Q4 — How is condition reported?** | C03 distinguishes voltage, alarm/input flags and identity/version status. C04 warns against a simple voltage-to-capacity percentage. No readiness assessment, battery percentage or diagnostic history is established. |
| **Q5 — What can be inspected?** | Historical-message bytes: original published example. Measurement/status/settings branch execution: explicitly synthetic test inputs. Actual observations/configuration/health: none acquired. [§E] |
| **Q6 — Do records and descriptions match?** | The manufacturer's shared manual expressly covers the selected product. This supports a shared example contract, not proof that its examples came from a particular S31-LB unit, region or firmware. |
| **Q7 — Is it reproducible?** | The checker requires the exact pinned decoder blob, runs offline and records runtime timezone. Manual page remains mutable; this is not the Step 08 evidence freeze. |
| **Q8 — What differences matter?** | Candidate C offers a small remotely configurable node as a counterpoint to integrated multi-sensor equipment. It is not claimed equivalent to a surveillance system or an already demonstrated CSAPI producer. |

The distinction between **configuration evidence**, **status evidence** and **measurement evidence** is retained. The retrieved command documentation demonstrates possible configuration, not actual state. A parsed software output is derived evidence; it cannot promote a documentary example into REAL_RECORDED standing.

## E. Executed small-record and decoder checks

The reproducible [offline checker](05_Dragino_Example_Check.cjs) was executed with **Node.js v22.16.0**, first with `TZ=UTC` and then `TZ=America/New_York`. It loads the separately obtained C03 file in a fresh restricted JavaScript context with execution timeouts; no networking, file writing by vendor code, sensor command, firmware update or CSAPI operation occurs. All assertions passed in both runs. Passing assertions mean the stated format/arithmetic checks succeeded, not product or semantic conformance.

**Source-byte verification:** local decoder Git blob `59af776a4b7ce287dc4c3030763e215b31f645f8`; SHA-256 `5138bd882f573918a63a95fdd6839641c2d83cfeefba4edd5d7a4ec1d2a9db67`. The vendor code is not included in our repository. The harness rejects a different file rather than silently testing a future revision.

**Original published example:** C02 §2.5.4 supplies **88 payload bytes**, independently segmented into **eight 11-byte entries**. The transcribed payload-byte SHA-256 is `a8d229062fd2aa1e4a34b04a07be8cdd85e7a7f7dd65f97fd54dfbd9fa2ac298`; this identifies the transcribed example bytes, not the entire web page. First-entry arithmetic produces **56.6% relative humidity, 27.2°C, and epoch 1684899041**, independently rendered as **2023-05-24T03:30:41Z**. The last entry is **2023-05-24T03:32:58Z**, 137 seconds later. These are documentary-example values, not verified environmental observations.

| Native location/key | Inspected interpretation | What must not be inferred |
| --- | --- | --- |
| Historical entry bytes 0–1 | Not used by C03's `datalog` function. | They are not evidence of zero battery voltage. |
| Bytes 2–3 / 4–5 | C03 scales humidity and signed temperature by 10. Tested on the original eight entries. | Not proof of calibration accuracy or two physical sensors. |
| Historical flag byte | C03 extracts input/alarm bits; its `PNACKMD` output reads the first entry's high bit. | The resulting label is not a retrieved configuration setting or proof of every entry's delivery history. |
| Historical bytes 7–10 | Unsigned epoch assembly, followed by `getMyDate`. | Decoder calendar text without timezone is not a self-contained UTC timestamp. |
| `DATALOG` | Decoder returns a concatenated string, with a trailing comma, inside a JSON object. | It is not an array of typed observation objects merely because it contains brackets. |
| FPort 2 `Door_status`, `EXTI_Trigger`, `Node_type` | Code-generated labels, exercised separately with synthetic inputs. | No installed door contact, unique physical identity, or source of an alarm is established by the label alone. |
| FPort 5 firmware/band/battery fields | Code parses compact version/band fields and voltage. | A hypothetical test output cannot pin the original example's deployed firmware or region. |

**Synthetic checks, clearly separate from G3 evidence:** The harness constructs a measurement input exercising negative temperature, humidity, voltage and flags; an alarm-settings reply; and a status message. The status test returns `1.0.0`, `EU868`, and `2.885` volts because those bytes were deliberately supplied by the analyst. None is a retrieved unit's state. An unsupported-port check confirms the decoder's error return; it is not a comprehensive robustness assessment.

## F. Discrepancies and interpretation hazards

| Finding | Observed evidence | Consequence for future use |
| --- | --- | --- |
| **Timezone-dependent calendar strings** | Unchanged example epoch yields `2023-05-24 03:30:41` in UTC and `2023-05-23 23:30:41` in America/New_York. C03 uses local date getters without an offset in the output. | Preserve the original epoch and explicitly interpret timezone. Do not label the returned string UTC unconditionally. |
| **No-data marker becomes apparent measurements** | C02 describes an all-zero 11-byte reply for no matching history. Feeding that constructed boundary case to C03 returns zero values and a 1970 calendar date in UTC. | A later adapter must distinguish absence from measurement. This audit records the behavior; it does not fix the vendor code or demonstrate actual device transmission. |
| **Misleading convenience labels** | `Door_status` is derived from a flag; `Node_type` is hard-coded in C03. The source context permits general input use. | Do not create a door component or authenticate product/individual identity from those labels. |
| **Manual arithmetic/transcription errors** | C02 prints `0x0197=412`, although calculation gives **407**; it also prints `0x7C >> 2 = 0x31`, whereas calculation gives **31 decimal / 0x1F**. C03 tests decimal mode 31. | Record source text and independent result separately. Do not silently rewrite the manual or treat every illustrative explanation as correct. |
| **Unjoined firmware and region** | The complete historical example contains neither field; C06 contents were unavailable. C03 filename and synthetic test values are separate evidence. | No inferred installed firmware, regional status or release-complete compatibility. Newer manual features are not assumed available in older devices. |
| **No real operational evidence** | No authenticated node, actual status/configuration response, calibration record or attributable telemetry history was acquired. | **REAL_RECORDED coverage remains zero.** Do not claim successful commands, live health or actual delivery recovery. |

C04 additionally cautions against interpreting battery voltage as a simple remaining-capacity percentage. That source-specific distinction is useful to the original cross-vendor problem, but no new power/condition model is authored here.

## G. Six evidence-depth scores — no aggregate

| Dimension | Score | Evidence and ceiling |
| --- | ---: | --- |
| Whole-System component/architecture depth | **2** | Identifiable complete product, probe/power/radio and board-family context. No complete schematic or installed inventory. [C01, C02, C05] |
| Capability/configuration depth | **2** | Source commands and decoder interpretation are useful; no complete original current-configuration response acquired. [C02, C03] |
| Operational condition/power/diagnostic depth | **2** | Voltage and flag/status meanings, battery limitations documented. No comprehensive diagnostics or actual history. [C03, C04] |
| Machine-readable source/communication depth | **2** | Original example decoded and fields cross-checked; additional synthetic branch checks. Not a coherent tested end-to-end interface across every version. [§E–F] |
| Actual attributed observations/history | **0** | Published examples and analyst-created probes do not establish real recorded measurements. |
| Reproducibility/version/rights | **2** | Pinned decoder bytes and executable harness; source locators, access failures and reuse limits explicit. Mutable manual and unverified firmware/region remain limits. |

## H. Verdict and next step

**PASS for the bounded reference/example case; not selected into the final corpus.** The available material can support later comparisons of physical probe versus output quantities, source-qualified voltage, configuration versus observed state, historical reporting, absence markers and decoder-mediated meaning. It cannot establish live operational fidelity, exact installed equipment, calibration, firmware interoperability or standards conformance. A narrower credible evidence case is useful without pretending that its missing real-device evidence has been supplied.

**Step 05 is complete.** The criteria and earlier A/B audits remain unchanged; Candidate D is not audited here. No donor ledger, candidate DIM v0.2, Profile requirement, client code or deployment changed. These source checks are supporting research, not the final corpus freeze or a new model campaign.

**Next separate “proceed”: Step 06 only — Campbell Scientific CR1000X with first-generation ClimaVue 50.** Establish its documented reference boundary, applicable program and source/record relationships using the same gates. Do not substitute CR1000Xe/G2, reopen A–C automatically, select the corpus or change Glaux.
