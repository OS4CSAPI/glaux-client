# Step 08 — Frozen Corpus Manifest and Handoff

**Version:** 0.1 · 30 October 2026 (America/New_York)  
**Standing:** **STEP 08 COMPLETE; EIGHT-STEP CONTROLLED-CORPUS PLAN CLOSED (8/8).** Preservation is complete at the declared research-record and small-example level, **not as a complete archive of upstream source bytes**. No actual operating-history dataset, validated deployed stack or end-to-end interoperability result exists in this set.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, `Docs/Research/DIM_Profile_V2/Controlled_Corpus/`.  
**Frozen input revision:** `8558e27ab744d2ae34938570e0ee16ee2eecf736`. The new handoff and preservation record are identified by their creation commit; this input revision does not purport to contain them.  
**Authority:** [Eight-step plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 08; unchanged [criteria](01_Eligibility_and_Evidence_Gates.md) and [Step 07 selection](07_Corpus_Qualification_Decision.md). The owner's separate “Proceed” authorized preservation and closure, not another audit or modeling effort.

## 1. What is handed over

The primary cases remain **A: AirGradient Open Air Max O-M-1PPSTON-CE gas-equipped reference assembly; C: Dragino S31-LB external-probe/primary-battery reference; D: Campbell CR1000X with first-generation ClimaVue 50 reference arrangement**. Their selection and bounded PASS verdicts are unchanged. **B: Raspberry Shake & Boom remains CONDITIONAL, G3 unverified, outside the primary set.** All four audits retain **zero acquired actual observations/history**. [Step 07, §§3–6]

This handoff preserves the exact research inputs, source locations and edition limits, small examples already embedded in the original checkers, executable-check dependencies, and reproducibility results. A future researcher can identify the same material and tell which checks require an external input. We have **not** frozen every manufacturer website, manual, firmware package, live endpoint or operating configuration. A linked source is not an archived source, and a successful example replay is not a new equipment finding.

The original goal remains a Domain Information Model (DIM), a separate OGC API – Connected Systems (CSAPI) application Profile, and a useful common System Resource Details experience. This evidence can challenge meaning in later work; it neither defines the full domain nor adopts model classes, Profile requirements or a user-interface design. The [Research Story](../DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md) and [Original Problem/Outcome Baseline](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) remain the purpose authorities.

## 2. Exact preserved project artifacts

All eight files below already existed at the frozen input revision. Their mounted copies were read, their complete byte lengths and SHA-256 digests computed, and their computed Git blob identities matched the repository records. They remain unchanged; they are **project reports/checkers**, not copies of entire manufacturer sources. B is retained as a negative/conditional research finding, not as an admitted primary case.

| Preserved file | Bytes | SHA-256 of complete file bytes |
| --- | ---: | --- |
| [03_AirGradient_Example_Check.py](03_AirGradient_Example_Check.py) | 3584 | `f552ae478c4b6194de07423ed7123e42d2a63ebcff11f7afdb917774602a4b63` |
| [03_Candidate_A_Evidence_Audit.md](03_Candidate_A_Evidence_Audit.md) | 25805 | `95c0f56d8becf6bd6d15451409d654642f921f56c57f873feaeb868da3236caf` |
| [04_Candidate_B_Evidence_Audit.md](04_Candidate_B_Evidence_Audit.md) | 22382 | `ab409e5b32c212cd0aa2e7916937daf93683698bb5aeaef1e4cc6992cf248b50` |
| [05_Candidate_C_Evidence_Audit.md](05_Candidate_C_Evidence_Audit.md) | 20708 | `29a9cac1be4cd2417c8b08f08220ee3030cc0784640b19ae01aa17ae19c83ad6` |
| [05_Dragino_Example_Check.cjs](05_Dragino_Example_Check.cjs) | 5457 | `6030bf1c57f2e864aeaaa241c4e22d5fb6edc8f5c3a9f3fb749050c708335120` |
| [06_Candidate_D_Evidence_Audit.md](06_Candidate_D_Evidence_Audit.md) | 17943 | `de5eb02c5f1011cabaf603441a5feacec4abac63f46b17826c337f664d97d926` |
| [06_Campbell_Example_Check.py](06_Campbell_Example_Check.py) | 4303 | `1683e9d2e5eadf2dfc0255687dc2022a77e288c79e4e1d57f966b8ed7f936572` |
| [07_Corpus_Qualification_Decision.md](07_Corpus_Qualification_Decision.md) | 20901 | `2f06febc631f2267065830af87fe6feeb48fa0c2455a9fe5a1cc78c9c6cc6fab` |

The [machine-readable preservation record](08_Preservation_Record.json) also records Git blob identities, the input revision, example/dependency hashes and replay results. The method and discovery files are pinned by repository reference at the same revision: criteria blob `7592bc828a11977e6e308b929d9081da68bac416`, discovery blob `1b0e1619d48de229e70c83ca51c0ce2dabec1d51`. No locally computed SHA-256 is claimed for those two files in this step.

**Preservation-record SHA-256:** `469c487a316784b88f2e83df6ee8e770194ede5595996476e4d2ff3b24eb08d7`. It covers that JSON file, not the truth of its claims or an upstream archive. Neither file hashes itself; the Git creation commit identifies this handoff and its companion.

## 3. Examples, dependencies and replay results

The existing checkers were inspected and rerun without modification using **Python 3.13.5** and **Node.js v22.16.0**, with standard libraries only. No device, gateway, broker, credential, firmware upgrade or CSAPI endpoint was used. Reacquiring the already-audited decoder and status example for reproducibility did not reopen the equipment audits or upgrade their verdicts.

| Case | Actually preserved with project | External dependency and preservation limit | Step 08 result |
| --- | --- | --- | --- |
| **A** | Original checker contains attributed cellular and annotated Wi-Fi example transcriptions. Its header retains AirGradient attribution and CC BY-SA 4.0 terms. The comment-stripped JSON is explicitly a derivative. | No full firmware README, hardware repository, forum response or manual archive is bundled. Source commits remain independently pinned, not a verified installed pair. | Checker completed: 52 cellular integers, three groups of 17 values after the interval; annotated Wi-Fi text rejected as strict JSON as expected; comment-stripped derivative has 17 keys. Original values were not repaired. |
| **C** | Original harness contains the 88-byte, eight-entry numerical documentary example and separately labeled synthetic probes. | Manufacturer decoder must be obtained separately from C03. Its UTF-8 reconstruction from connector text matched Git blob `59af776a4b7ce287dc4c3030763e215b31f645f8`, 3,786 bytes. No express redistribution license was verified, so it is **not bundled**. | Unchanged harness passed in UTC and America/New_York. The same first epoch gives `2023-05-24 03:30:41` versus `2023-05-23 23:30:41`. Synthetic no-data and branch checks retained their prior meaning. |
| **D** | Original checker and the audit's results; no complete publisher JSON input is bundled. | Same D07 example re-read and newly transcribed locally. Canonical JSON hash matches Step 06 exactly; whitespace-format bytes differ. Redistribution permission was not established, so the input remains **external-dependent**. | Checker passed: 31 unique names paired with 31 values, 18 numbers, three strings, ten Booleans. This is logger-component example verification, not ClimaVue weather history or execution of its program. |

**Input hashes identify different things.** A's cellular UTF-8 excerpt hashes to `1f3f9cf32d94a58b0909cf649dedd5c439a19fc5d7deb2b96422ed9687222d5c`; its annotated Wi-Fi excerpt hashes to `fac20cd24153d598b32dda8ef86a1046e88ad4c67188f648978eced4ce9319d8`. C's reconstructed 88 payload bytes hash to `a8d229062fd2aa1e4a34b04a07be8cdd85e7a7f7dd65f97fd54dfbd9fa2ac298`; the separately obtained decoder reconstruction hashes to `5138bd882f573918a63a95fdd6839641c2d83cfeefba4edd5d7a4ec1d2a9db67`. These are not checksums of a complete manual or captured over-the-air transmission.

D's new local transcription hashes to `a001c5539ca6839f4f0396e24b6a734a3c5f506b9babe2c497077b2d4305cea1`. Its canonical hash remains `ef93d1fc12a09fe04a4d06da743b07a8694cd6bc74af3ce612110a8d4e15c8a8`, matching the Step 06 semantic content under that checker's explicit canonicalization, not asserting original publisher-byte identity. The prior transcription hash remains recorded separately in the audit and JSON record. No source values were changed to obtain this match.

**Evidence labels are preserved.** Original examples remain `PRIMARY_PUBLISHED_EXAMPLE`; hardware/code/interface accounts are `PRIMARY_DESIGN_OR_SPEC`. Local transcriptions identify their documentary origin, while comment removal, independent decoding and test outputs are `SYNTHETIC_OR_DERIVED`; they are not fresh device evidence. Unknown versions, inaccessible records and disputed editions remain `UNAVAILABLE_OR_UNVERIFIED`. `REAL_RECORDED` coverage remains zero; no new `SECONDARY_TECHNICAL` source was introduced.

## 4. Frozen source-reference inventory — not an upstream byte archive

This inventory retains **27 source IDs with 32 distinct original URLs** from the selected audits: A01–A12, C01–C06 and D01–D09. IDs preserve the meaning of each audit's §B; several IDs contain more than one source file/page. Exact original inspection ranges, claim scope, access attempts and rights cautions remain in those immutable audit registers at the input revision. Titles/sections below are extracted from those registers; edition summaries preserve rather than reconcile their limits.

Unless identified in §3, sources were **not re-audited or re-downloaded in Step 08**. A was inspected on 29 October 2026; C and D on 30 October 2026, America/New_York. Mutable-page dates are access evidence, not firmware versions. All rows below are **references, not a claim that complete source bytes are checked into this project**. Direct runtime retrieval of one raw GitHub file failed DNS resolution in Step 08; connector text and browser text still supported the bounded checks.

### A sources

| ID and inspected source/section | Edition and evidence kind | Original source location(s) |
| --- | --- | --- |
| **A01** — AirGradient hardware team / Open Air Foundation. Open Air Max hardware README, Overview, Design structure, Key components, Plug-in modules, Related repositories. | Hardware commit 89aacf5013fc0ffe4b988a2e3c5a227bce3c4983; README blob 6a915a09e7d34bd11b6b0dbe6698898d36976466 — **design/spec** | [source 1](https://github.com/Open-Air-Foundation/pcb-openair-max-main/blob/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/README.md) |
| **A02** — AirGradient / Open Air Foundation. Firmware README, Sensor Support, System Settings Portal, Transmission and both Example Payload Breakdown sections. | Firmware commit 84e479a415d81151e7a81aea9a2f7449a15e98cc; README blob 1322b58c7ed70ec0f4900bd557ec09fa65e03732 — **design/spec/published example** | [source 1](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md) |
| **A03** — Same firmware commit: Configuration.cpp, Sensor.cpp, MaxConfig.h. | Same firmware commit as A02; Configuration.cpp lines 95–135, Sensor.cpp lines 1–215, MaxConfig.h — **design/spec** | [source 1](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/Configuration.cpp#L95-L135); [source 2](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/Sensor.cpp#L1-L215); [source 3](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/MaxConfig.h) |
| **A04** — AirGradient. Open Air Max product page, Technical Data. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://www.airgradient.com/professional/products/open-air-max/) |
| **A05** — AirGradient. Device Overview and First Test, Device Overview and Connect the monitor; Adding to the Dashboard, Add the Monitor and Viewing Battery and Solar Data. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-device-overview); [source 2](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-adding-to-the-dashboard) |
| **A06** — AirGradient. Power, Battery Backup, and Solar, USB-C Power, Battery Backup and Solar Power. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-power-battery-backup-and-solar) |
| **A07** — AirGradient. Status LED and Reporting Intervals, Status LED behavior, Reporting Interval and Power Modes. | Mutable guide; power-mode section says firmware 0.7.0 onward; not a deployed version — **design/spec** | [source 1](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-status-led-and-reporting-intervals) |
| **A08** — AirGradient. What Data Is Included in an AirGradient Dashboard CSV Export?, General Parameters and Open Air Max with/without NO2/O3. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://www.airgradient.com/documentation/kb/kb-diy-air-quality-parameters) |
| **A09** — Tai_AirGradient. Max API — Working example with O3 and NO2 data, manufacturer replies **#3, #5 and #6**, 15–17 September 2026. | Manufacturer replies #3, #5, #6; 15–17 September 2026 — **design/spec/published example** | [source 1](https://forum.airgradient.com/t/max-api-working-example-with-o-and-no-data/7345) |
| **A10** — Public lab endpoint, explicitly offered in A09 #6. | Unretrieved endpoint; no response version — **unavailable/unverified** | [source 1](https://api.airgradient.com/public/api/v1/world/locations/194928/measures/current) |
| **A11** — AirGradient. Open Air Max manual PDF. | Conflicting parsed/rendered manual editions; excluded from positive evidence — **unavailable/unverified** | [source 1](https://www.airgradient.com/documents/manuals/Open_Air_Max_Manual.pdf) |
| **A12** — AirGradient. Open-Source Files & Builds Overview, Firmware Repositories and Open Air Max; pinned firmware LICENSE. | Pinned firmware LICENSE at A02 commit plus mutable manufacturer overview — **design/spec** | [source 1](https://www.airgradient.com/documentation/kb/kb-diy-the-airgradient-builds-overview); [source 2](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/LICENSE) |

### C sources

| ID and inspected source/section | Edition and evidence kind | Original source location(s) |
| --- | --- | --- |
| **C01** — Dragino. “S31-LB/LS — LoRaWAN Temperature & Humidity Sensor.” Features, specifications and order information; page displays last modified **25 June 2026**. | Page displayed last modified 25 June 2026; not a firmware release — **design/spec** | [source 1](https://dragino.com/products/temperature-humidity-sensor/item/264-s31-lb-ls.html) |
| **C02** — Dragino. “S31/S31B-LB/LS.” §§1.4–1.8, 2.3–2.5, 2.7–2.8, 3.3 and 4–5. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec/published example** | [source 1](https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/) |
| **C03** — Dragino. “S31-LB_v1.3_TTN_decoder.txt.” `decodeUplink`, `Decoder`, `datalog`, `getMyDate`; commit 6354176. | Commit 635417693adb215b32ac367c8e8909d9d609a120; blob 59af776a4b7ce287dc4c3030763e215b31f645f8; decoder v1.3 filename not device firmware — **design/spec** | [source 1](https://github.com/dragino/dragino-end-node-decoder/blob/635417693adb215b32ac367c8e8909d9d609a120/S31-LB%26S31B-LB/S31-LB_v1.3_TTN_decoder.txt); [source 2](https://github.com/dragino/dragino-end-node-decoder/commit/635417693adb215b32ac367c8e8909d9d609a120) |
| **C04** — Dragino. “How to calculate battery life of Dragino sensors.” §§1.1, 1.3 and 4.0. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://wiki.dragino.com/docs/FAQs/battery-life-calculation/) |
| **C05** — Dragino. “UART/TTL Upgrade Mode.” model/motherboard table. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://wiki.dragino.com/docs/LoRaWAN-Firmware-Update/uart-ttl-upgrade-mode/) |
| **C06** — Dragino-linked firmware/changelog folder, from C02 §§2.8/5. | Uninspected linked firmware/changelog folder — **unavailable/unverified** | [source 1](https://www.dropbox.com/sh/fis3g6nmhv0eokg/AAC6BcCZaX4BdqZkduUvZ3jIa?dl=0) |

### D sources

| ID and inspected source/section | Edition and evidence kind | Original source location(s) |
| --- | --- | --- |
| **D01** — Campbell Scientific. “ClimaVue 50: Compact Digital Weather Sensor”, Overview, Detailed Description, Specifications, Downloads and FAQs. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://us.campbellsci.com/climavue-50) |
| **D02** — Campbell Scientific. *ClimaVue 50 Compact Digital Weather Sensor: Product Manual*, revision **08/2024**; §§5–8; Table 7-1, printed p.13; Table 8-1, pp.21–23. | US product manual 08/2024; sections 5–8; Table 7-1 p.13, Table 8-1 pp.21–23 — **design/spec** | [source 1](https://s.campbellsci.com/documents/us/manuals/climavue50.pdf) |
| **D03** — Campbell Scientific. *ClimaVUE 50 Compact Digital Weather Sensor*, revision **9/19 as identified in extracted text**, Appendix B, **B-1–B-3**, “CR1000X Program Measuring the ClimaVUE 50.” | EU manual 9/19 per extracted text; Appendix B pp.B-1–B-3; screenshots/bytes not obtained — **design/spec/published example** | [source 1](https://s.campbellsci.com/documents/eu/manuals/climavue50.pdf) |
| **D04** — Campbell Scientific. “ClimaVue 50 Example Program”, download description. | Example program v1, July 8, 2021, 3 KB; login-gated package uninspected — **design/spec** | [source 1](https://www.campbellsci.com/resources/software/climavue50-example-program) |
| **D05** — Campbell Scientific. “CR1000X: Measurement and Control Datalogger”, Communications, Enclosures, Power and Specifications. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://us.campbellsci.com/cr1000x) |
| **D06** — Campbell Scientific. “CR1000X Status Table”, Battery, LithiumBattery, PanelTemp, SW12Volts, CommsMemFree, WatchdogErrors and program/version entries. | Mutable documentation; exact edition unspecified; retain the dated audit access. — **design/spec** | [source 1](https://help.campbellsci.com/crbasic/cr1000x/Content/Instructions/StatusTable.htm) |
| **D07** — Campbell Scientific. “Status — MQTT API”, **CR1000X Example**. | Displayed footer 2026-09-21 (ced60094); not a verified commit/firmware — **design/spec/published example** | [source 1](https://help.campbellsci.com/datalogger-api/mqtt/status.html) |
| **D08** — Campbell Scientific. “JSON Data Formats — MQTT API”, GEOJSON Output Format. | Same displayed footer as D07 — **design/spec** | [source 1](https://help.campbellsci.com/datalogger-api/mqtt/json_data_formats.html) |
| **D09** — Campbell Scientific. “Data Logger MQTT API”, introduction and warning. | Same displayed footer as D07 — **design/spec** | [source 1](https://help.campbellsci.com/datalogger-api/mqtt/index.html) |

**Reuse scope remains source-specific.** A's embedded licensed README excerpts do not confer permission over AirGradient's website, forum or live records. C's publicly readable decoder is not redistributed without an established permission basis. D's copyrighted manuals, program package and complete status-example input are not bundled. This preserves the audits' access/reuse limits, not a legal opinion or a claim that every later experiment is authorized. The unresolved B waveform-data reuse restriction also survives its exclusion; nothing from B's inaccessible dataset is republished.

## 5. Matched questions and intentional differences

Use the same Step 01 questions; do not turn this table into adopted DIM classes or mandatory interface tabs. Detailed findings and native terminology remain in the unchanged audits and Step 07 §4.

| Shared question | A — integrated assembly | C — external-probe node | D — logger/sensor arrangement |
| --- | --- | --- | --- |
| **Q1: What exactly is the case?** | Named gas-equipped `...-CE` design; no universal `-CE-S` equivalence. | External-probe, primary-battery S31-LB; region/firmware unknown. | CR1000X plus first-generation ClimaVue 50; not Xe/G2 or a deployed stack. |
| **Q2: What is included?** | Modules and quantities remain distinct; expansion options are not installed parts. | Probe, node, radio and battery; gateway remains external context. | Logger, sensing assembly and cable; support roles do not invent an installed battery/enclosure/modem. |
| **Q3: What can be configured?** | Portal/source keys show possibilities, not current state or successful action. | Commands documented; synthetic settings/status bytes are not device configuration. | Historical pairing-specific program and later package description are different artifacts; no verified running program. |
| **Q4: What condition information exists?** | Voltage examples and local mode/diagnostic descriptions; no actual health history. | Voltage/flag meanings, not capacity or comprehensive health. | Rich logger-component status; sensor and whole-station condition remain separate. |
| **Q5: What can be inspected?** | Published cellular/Wi-Fi examples embedded; cloud examples remain external references. | Eight-entry message example embedded; decoder externally obtained. | Typed 31-field logger example is externally supplied; no weather series. |
| **Q6: Do sources describe the same scope?** | Product-level attribution only; independent source commits and timing differences are not unified. | Example does not authenticate an installed unit, firmware or region. | Independent 2019/2021/2024/2026 sources do not establish one release combination. |
| **Q7: What is reproducible?** | Embedded example check is self-contained; broader manufacturer evidence remains source-dependent. | Exact replay needs pinned decoder plus explicit timezone; raw epoch preserved. | Exact semantic replay needs original example/transcription matching canonical hash; no original-byte archive. |
| **Q8: Which differences must survive?** | Module versus output; raw versus calculated; alternative reporting paths. | No-data versus zero; timestamp versus local display; decoder labels versus physical facts. | Logger versus sensor; Boolean output state versus voltage; processing/carried-forward values versus fresh measurement. |

**B stays outside this matrix's primary membership.** Its combined V3 design and separately attributed AM.R9D92.00 historical lead remain documentary context. A public link does not supply inspected waveform/response contents. No record was substituted and no retry was performed here. The desired qualified seismic/acoustic or surveillance case remains missing; the selected cases do not narrow the eventual DIM to environmental monitoring.

## 6. Reproduction instructions and limits

From this repository's `Controlled_Corpus/` directory, first verify the eight input files against `08_Preservation_Record.json`. The relative names below refer to unchanged files at the frozen input revision. These are instructions for a future authorized replay, not evidence that remote source services or hardware were tested.

```python
from pathlib import Path
import hashlib, json
record = json.loads(Path("08_Preservation_Record.json").read_text())
for item in record["preserved_project_files"]:
    path = Path(item["repository_path"]).name
    data = Path(path).read_bytes()
    if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
        raise ValueError(f"Frozen input changed: {path}")
print("Eight preserved input artifacts match.")
```

Replay the self-contained AirGradient example:

```bash
python3 03_AirGradient_Example_Check.py
```

For Dragino, obtain **C03 at its exact commit/path**, preserve the original UTF-8 content and check its Git blob before use; the existing harness enforces the expected blob. The manufacturer decoder is not in the project bundle. Do not replace it with a newer `main` version and claim an identical replay.

```bash
TZ=UTC node 05_Dragino_Example_Check.cjs /path/to/S31-LB_v1.3_TTN_decoder.txt
TZ=America/New_York node 05_Dragino_Example_Check.cjs /path/to/S31-LB_v1.3_TTN_decoder.txt
```

For Campbell, obtain the **D07 CR1000X Example**, preserve array order, types and values, and identify any transcription. Run the existing helper and compare its reported canonical hash with §3; successful field-count checking alone is not an exact-content match. A failed retrieval or changed page must be recorded, not filled in from expected values.

```bash
python3 06_Campbell_Example_Check.py /path/to/status_example.json
```

**Offline availability is unequal.** A can replay from the retained project file alone. C needs the separate decoder; D needs the separate example. Both external inputs were obtained for this step's replay, but they are not distributed as enduring project artifacts. No complete licensed manual archive, firmware binary, actual station inventory, calibration record or joined configuration/condition/measurement history has been preserved. The earlier AirGradient PDF conflict, C release-folder access gap and D program/extraction limits remain in their audits.

## 7. Recovery instructions and final boundary

For a new chat, start with the [project README](../README.md), [Research Story](../DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md) and [Original Problem/Outcome Baseline](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md). Then read this handoff, the preservation record, Step 07 and the applicable audits. The [candidate DIM v0.2](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md) remains candidate text; its donor findings, including the useful IEEE 1451 public/Playground correction, were not reopened or displaced by these equipment cases. PITON v1.7 and “next proceed” sentences in earlier step reports are historical context, not current execution instructions.

The research branch is `research/dim-profile-v2`; separate client work belongs on `work/details-view-20261023`. No merge, deployment, donor-inventory edit, final chassis/name selection, Condition/Status study, Profile rule or source-to-CSAPI mapping is authorized by this closure. No field names from these products automatically become model concepts, and examples cannot repair missing operating evidence.

**Completion:** eight bounded iterations are complete. The controlled set is A/C/D for documentary/reference-example research, with B conditional and excluded, zero actual-history coverage, source-specific limits and explicit preservation gaps. Step 08 added this manifest and preservation record, reran existing checks against the same documentary inputs, and updated the plan/README. Original criteria, audits, checkers, selection, donor work, DIM and application remain unchanged.

**STOP. There is no Step 09 in this plan and no automatically authorized next modeling or implementation task.** A future task requires the owner's separate direction; this handoff records the starting evidence without prescribing a new campaign.
