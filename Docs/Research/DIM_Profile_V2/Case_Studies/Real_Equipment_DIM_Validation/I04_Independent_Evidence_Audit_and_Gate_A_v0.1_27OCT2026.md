# Iteration I04 — Independent Evidence Audit and Gate A Decision

**Date:** 27 October 2026  
**Status:** **COMPLETE — Gate A CONDITIONAL PASS for product/design facts; actual individual-unit and observation verification NOT PASSED.**  
**Workstream:** [Case study README](README.md) · [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md) · [I02 pinned source register](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) · [I03 60-fact extraction](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md).  
**Standing:** Independent **source-fidelity audit**, not a new Domain Information Model (DIM), an Open Geospatial Consortium (OGC) API – Connected Systems (CSAPI) mapping, a hardware conformance test, or observed real-world measurement.

## 1. What was checked and how

The task was **not to repeat I03 and certify all 60 statements by reading them again**. I independently re-opened original, **full-commit-pinned upstream files** and inspected the actual evidence ranges for a **targeted sample of 34/60** I03 statements across **15 original source files**. I also inspected three engineering files to check consequential claims: the SCK 2.3 Urban Board Eagle schematic (I02 H03) and two newly inspected files **within the already frozen H repository commit**, namely its Data Board manufacturing pick-and-place list and `lib/Sensors/Sensors.h`. The older [I02 list of 25 indexed source files](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) is a *selected-file* register, not the complete content of its four frozen repository trees; **these I04 source additions do not change the repository commit**.

For the alleged sensor-name discrepancy, I also re-opened the **current public** [Kit page](https://docs.smartcitizen.me/hardware/kit/) and [Urban Board page](https://docs.smartcitizen.me/hardware/boards/urban-board/) on **27 October 2026**, checking their visible SCK 2.3 tables against both the pinned text and engineering schematic. Current public HTML can change later; this is **a dated recheck**, not an archival HTML snapshot.

**Audit labels:** **CONFIRMED AS SOURCE STATEMENT** (the exact original states it, within its stated scope); **CONFIRMED WITH QUALIFICATION** (native statement exists, but earlier wording or cited range needs precision); **CORRECTED** (incorrect earlier research claim or inadequate citation); **UNRESOLVED** (the current evidence cannot justify a single equipment fact); **NOT TESTED** (no actual unit, measurement or runtime evidence). “Confirmed as source statement” is **not** a laboratory validation of product performance or a source-standard mapping.

### Audited 34 fact IDs

| Source concern | I03 records checked | Result |
| --- | --- | --- |
| Version, assembly, physical dimensions and connectors | **F003, F004, F007, F008, F013, F015, F017, F020** | Manufacturer statement supported; model/product scope only; F017 humidity limit is marked *storage* condition by its source |
| Sensors, options and firmware gating | **F021, F022, F023, F024, F025, F026, F028** | Part labels corroborated in engineering design; F023 citation needed extension; F025 wording tightened; no actual installed sensor evidence |
| Operation, processing, state, storage, firmware version | **F029, F032, F035, F037, F038, F042, F043, F045** | Most statements supported as intended behavior; F035 clarified; 8 MB vs 4 MB conflict adjudicated at SCK2.3 *design* level (not an installed-unit measurement) |
| Registration, data source and candidate device IDs | **F047, F049, F050, F051, F052, F054, F056, F057, F058, F059, F060** | Native source distinctions confirmed; I03 F047 wording clarified; R01 is **unexecuted example code**, not a returned device record |

**Coverage limit:** **26/60 I03 records were not individually re-audited**; their Git line links exist and they remain **provisional source statements**, not blanket PASS. If a later iteration depends materially on one, retrieve its exact original source before asserting or mapping it.

## 2. Six flagged issues — actual findings

### FLAG-01 — supposed public-site versus frozen-source part-number disagreement

**Verdict: CORRECTED / previous discrepancy claim RETRACTED.**

The I02 and I03 notes claimed the publicly rendered SCK2.3 sensor table showed `AS7311`, `BH1721FVC`, `ICS-434342` and `MPL3115A26S` instead of the pinned source's `AS7331`, `BH1730FVC`, `ICS-43432` and `MPL3115A2`. **The dated independent recheck did NOT reproduce that claimed conflict.** Both present public Kit/Urban Board tables agree with the pinned Git documentation ([I02 D01, SCK2.3 measurement table, lines 86–96](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/index.md#L86-L96); [I02 D02, lines 47–59](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/urban-board.md#L47-L59); Smart Citizen 2026). Do not preserve the earlier claim as a real manufacturer inconsistency.

**Independent hardware check:** The **pinned SCK2.3 Urban Board Eagle schematic** identifies `S1/MPL3115A2`, `S2/AS7331`, `S3/ICS-43432`, `S4/SHT31`, and `S5/BH1730FVC` in its own parts section (Fab Lab Barcelona 2026a, [H03 lines 7496–7543](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.sch#L7496-L7543)). This is stronger **design-level corroboration**, **not** proof a particular produced unit has all those devices fitted. The kit's PM sensor is an **external connected sensor**, not a populated part within this Urban Board schematic.

**Disposition:** F021–F024 can retain the **pinned source's exact part labels** for manufacturer-defined SCK2.3 design. The alleged four-name conflict is **false/unreproduced** and must be excluded from later DIM work. This is an explicit correction of an earlier AI conclusion.

### FLAG-02 — 4 MB and 8 MB flash-memory statements

**Verdict: SOURCE CONFLICT; SCK2.3 DESIGN EVIDENCE FAVORS AN 8 MB DEDICATED READING-BUFFER CHIP.**

The pinned [Data Board narrative D03, line 28](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/data-board.md#L27-L28) says **4 MB of extra flash for offline data** and separately mentions **4 MB within the ESP8266 Wi-Fi module**. The pinned [firmware documentation D07, lines 50–61](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/firmware/index.md#L50-L61) instead names an **S25FL064L dedicated 8 MB SPI flash chip** for storing reading groups.

**New directly verified manufacturing evidence** is decisive at the *specified 2.3 design* level: the [SCK2.3 Data Board pick-and-place list](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_DATA_BOARD_2.3/SCK_DATA_BOARD_2.3_for_Manufacture/04-SCK_DATA_BOARD_2.3_pick%26place.mnt#L38-L40), `IC6`, specifically lists **S25FL064L**, distinct from the `IC4` ESP-12-E module. Thus D07 and the manufacturer’s 2.3 manufacturing file agree on the dedicated flash component, while D03's **4 MB extra-flash sentence is inconsistent with that specified design** (Fab Lab Barcelona 2026a; Smart Citizen 2026).

**Disposition:** For a **source-specified SCK2.3 data-buffer design**, use the *documented 8 MB S25FL064L* as the **better-supported source fact**, with this conflict note. Retain F043 as a *true record of what D03 says*, but **do not promote 4 MB as the resolved 2.3 buffer capacity**. The on-module Wi-Fi flash is **another storage function**, not automatically the same buffer. We have **not** established a manufactured unit's physical chip inventory or firmware use of that chip.

### FLAG-03 — SEN5X model options versus installed equipment

**Verdict: CONFIRMED PRODUCT OPTIONS; INDIVIDUAL INSTALLATION NOT ESTABLISHED.**

The [Kit documentation D01, lines 120–123](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/index.md#L120-L123) explicitly distinguishes **SEN50, SEN54 and SEN55**; the manufacturer says it chose SEN50 as a PM option and identifies additional VOC/NOx functions on compatible variants. The pinned [firmware configuration `SCK23_AIR` section](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/lib/Sensors/Sensors.h#L35-L41) enables `SCK_WITH_SEN5X`, `SCK_WITH_MPL` and `SCK_WITH_AS7331` compilation paths. The [I02 H05 firmware source](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/SckUrban.cpp#L73-L103) implements corresponding sensor cases (Fab Lab Barcelona 2026a).

**Disposition:** Vendor model alternatives and supported software paths are **product/implementation evidence**. They do **not** identify which option any one of the notebook’s four prospective platform records actually used, or prove the firmware configuration compiled/flashed on those devices.

### FLAG-04 — registration code, platform device ID and advanced Station/Hardware ID

**Verdict: DISTINCT NATIVE ID ROLES; NO PROVEN PHYSICAL-TO-PLATFORM JOIN.**

The [DIY assembly guide D08, lines 25–30](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md#L25-L30) describes a short code on a box/sticker for registration, awkwardly calling it **“four-digit” while saying it contains letters and numbers**. Its exact character semantics should not be exaggerated into a globally unique permanent hardware ID. Separately, the [advanced-device section D08, lines 256–273](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md#L256-L273) and [calibration guide D09, lines 18–25](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/data/handling-calibration-data.md#L18-L25) distinguish a **physical station/hardware ID** (used to attach calibration records) from a **platform device/kit ID** (which can change with re-registration). These are described especially for **advanced calibrated stations**, not proved mandatory for the basic SCK2.3.

**Disposition:** Keep the three evidentiary roles separate: **DIY registration code**, **platform device record ID**, **advanced station/calibration hardware ID**. No asserted equivalence or physical-unit match. The guide's example hardware IDs and sensor-serial entries are **examples**, not our case-study unit(s).

### FLAG-05 — platform-record candidates versus actual data

**Verdict: ONLY SOURCE-CODE REFERENCES; NO OBSERVATION VERIFIED.**

The pinned [data-analysis notebook R01](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/examples/notebooks/learning/01_basic_data_exploration.ipynb#L159-L170) names `devices_ids = [18486, 18487, 18488, 18489]`, uses `sc_air`, and requests data for **12 February–7 March 2025**. The complete notebook parses to **27 cells, 17 code cells, zero saved execution counts and zero saved outputs**. Its introductory text describes an enclosure study of four kits, but that is a **project description**, not returned individual device metadata or observations (Fab Lab Barcelona 2026b). The separate `sc_air` blueprint includes advanced electrochemical processing, not a confirmed installed SCK2.3 sensor inventory.

**Disposition:** IDs 18486–18489 are **not verified physical hardware IDs, actual data records, or individually validated units**. The execution environment did not retrieve their live API responses (I02); this limitation **does not imply the live service is down or the referenced IDs invalid**. No actual temperature/UV/PM values, timestamps, locations, calibration events, or device configurations have been observed.

### FLAG-06 — source revision versus deployed runtime

**Verdict: SOURCE CONSTANTS CONFIRMED; DEPLOYED VERSIONS UNAVAILABLE.**

The pinned [firmware `sam/src/version.h`](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/version.h#L1) declares `SAMverNum = "0.9.11"`; the pinned [API repository `VERSION` file](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/VERSION#L1) says `1.1.5`. These are **source-tree values** (Fab Lab Barcelona 2026a, 2026c), not a readback from an individual SCK or proof of the production API deployment.

**Disposition:** Retain them as source revision context, not as the individual device's firmware state or the server software actually serving February–March 2025 data.

## 3. Additional precision fixes from sampled claims

The source check uncovered three narrower but important corrections to I03:

- **F023 — citation range.** The original `D01 lines 92–94` supports the SCK2.3 `MPL3115A2` part but **does not contain the comparison to the SCK2.2 `LPS33K`**. The citation must also cover **[D01 lines 100–105](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/index.md#L100-L105)**. This is a **citation correction**, not a dispute about those two source values.
- **F025 — physical quantity terminology.** The source names PM1/PM2.5/PM4/PM10 with **µg/m³**, not a standalone generic “mass fraction” quantity. Record the four **particulate-matter size-designated readings** and their source unit without introducing a different quantity term.
- **F035 — WARNING behavior.** Say the firmware's **WARNING** state may permit reading collection while an SD-saving **or** online-publication path is impaired; the source describes internal flash buffering. Do **not** imply that every WARNING simultaneously disables both external pathways.
- **F047 — “four-digit” source wording.** Source says the code includes letters and numbers. Keep the source's ambiguous “four-digit” phrasing and **do not certify its exact syntax or lifelong uniqueness**.

The I03 record is retained as the historical extraction but will carry a **visible I04 audit correction notice** and precise F023/F025/F035/F047 fixes. The earlier I02 false-public-conflict statement is likewise retained in its dated discovery log only with a prominent **superseding correction**, not erased silently.

## 4. Gate A judgment — what may pass into the actual DIM experiment?

**Formal verdict: CONDITIONAL PASS.** This is a **PASS for using the supported Smart Citizen Kit 2.3 *product/design* evidence under the qualifications below; it is NOT a pass for verifying one specific physical unit or for observed data.**

| Evidence dimension | Gate A disposition | Consequence for later iterations |
| --- | --- | --- |
| **Source provenance and reproducibility** | **PASS** | Four full-commit-pinned manufacturer/project repositories plus 25 originally indexed files, with 3 targeted engineering files added during I04 source check. |
| **Relevant 2.3 product construction / intended sensors** | **PASS — scoped to documented design** | Reuse F001–F060 only according to actual source provenance; 34 independently sampled; 26 still require source recheck if consequential. Use schematic-backed 2.3 part labels and the actual SEN5X optionality. |
| **Operating/firmware/platform interface descriptions** | **PASS — published/implemented capability only** | No inference of runtime configuration, commands executed, or deployed software version. |
| **Exact extra-flash capacity in conflicting narratives** | **QUALIFIED** | S25FL064L/8 MB is corroborated for SCK2.3 *specified data-buffer design*; D03's 4 MB narrative remains an inconsistent statement, not a supported exact 2.3 design conclusion. |
| **Individual physical equipment identity, component inventory and deployment** | **NOT PASSED / NOT VERIFIED** | **No authenticated unit** and no valid join between hardware and platform IDs. Keep GAP-01 through GAP-04 open. |
| **Real device observations, field state, calibration record and actual execution** | **NOT PASSED / NOT TESTED** | No timestamped sample obtained. GAP-05 and GAP-06 open; no empirical interoperability or performance claim. |

**Permitted next step (conditional):** The project's planned **I05 — Individual System Identity and Product / Model / Kind** can proceed using these audited product-level distinctions **as a bounded mapping exercise**, with explicit rows for **“individual unit not established”** and **“hardware-to-platform correspondence unknown.”** It must **not claim to validate real-unit identity**. If later results require authenticated individual-device observations or equipment-replacement history, that test is **blocked until a source-verifiable unit record and an actual sample are acquired**. Do not bypass this qualification merely to complete the 13-iteration schedule.

**What this is not:** It is neither a FAIL of the whole DIM research nor a successful end-to-end validation of equipment identity. A *conditional* gate precisely distinguishes the strong design evidence from the unearned empirical claims.

## 5. PITON A and the next action

The separately committed [**PITON A — Evidence Gate A Continuity**](PITON_A_Real_Equipment_DIM_Validation_v0.1_27OCT2026.md) is the current case-study recovery point. It tells a future conversation exactly which branch and files to read, what has been corrected, what is authorized, what is quarantined, and how to invoke I05 with one `proceed`.

**Next only when directed:** **Iteration I05 — apply the existing Individual System Identity and Product/Model/Kind research to verified evidence with fact IDs.** This is *semantic mapping*, not a new source extraction, not proof of one physical serial number, and not an application-profile requirement. **I05–I13 have not started.**

## References — Chicago Manual of Style, 18th edition, author–date

Fab Lab Barcelona. 2026a. *Smart Citizen Kit 2.X Hardware and Firmware*. Commit `3dbbc1061509920aca2dda2aca32abe82563500b`. Official `fablabbcn/smartcitizen-kit-2x` repository. https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b.

Fab Lab Barcelona. 2026b. *Smart Citizen Data Tooling and Example Notebook*. Commit `4f024f4d42cb40c2cd515062ee7e4815bd2798eb`. Official `fablabbcn/smartcitizen-data` repository. https://github.com/fablabbcn/smartcitizen-data/tree/4f024f4d42cb40c2cd515062ee7e4815bd2798eb.

Fab Lab Barcelona. 2026c. *SmartCitizen API Backend*. Commit `25a524cbfb036f8950c247b847d8884a4e776297`. Official `fablabbcn/smartcitizen-api` repository. https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297.

Smart Citizen. 2026. *Smart Citizen Documentation*. Frozen authored documentation, commit `0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f`. Official `fablabbcn/smartcitizen-docs` repository. https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f. Current rendered Kit and Urban Board pages accessed October 27, 2026, with no reproduced name conflict.
