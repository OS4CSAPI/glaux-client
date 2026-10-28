# Iteration I02 — Versioned Source Corpus Register

**Date:** 27 October 2026  
**Status:** **I02 COMPLETE — core, version-pinned product/engineering/data-source corpus recorded; actual unit identity and readings UNVERIFIED.**

**I04 CORRECTION (27 October 2026):** The claim below in §6.1 that the public sensor table disagreed with pinned Git text **has been retracted**. A direct audit of the published pages and the SCK2.3 Urban Board schematic found the same intended part names: `AS7331`, `BH1730FVC`, `ICS-43432`, and `MPL3115A2`. The earlier variant spellings were **an unsupported claim by our research**, not a verified Smart Citizen contradiction. See [I04 independent audit, FLAG-01](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md#flag-01--supposed-public-site-versus-frozen-source-part-number-disagreement). All four Git commit pins and original 25 selected files remain unchanged; I04 also inspected two extra manufacturing/firmware sources *within the frozen H commit*.  
**Project:** [Real Equipment DIM Validation](README.md) | [13-Iteration Plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md) | [I01 equipment selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md)  
**Target:** Fab Lab Barcelona **Smart Citizen Kit 2.3** (SCK2.3), not an assumed individual unit or a Smart Citizen advanced Station.  
**Corpus rule:** Git **full commit SHA + exact path + blob SHA** fixes file content. Links to published websites and public live application programming interfaces (APIs) are **context/verification paths**, **not frozen snapshots or evidence of successful retrieval**. The Git commit timestamp is the repository snapshot's commit date, **not necessarily a document publication date**.

## 1. Freeze decision and evidence classes

For the selected **product-level** case, the main source corpus is now pinned to four official Fab Lab Barcelona repositories:

| Key | Official repository and immutable tree | Frozen commit SHA | Commit timestamp (UTC) | Relevance |
| --- | --- | --- | --- | --- |
| **D** | [`fablabbcn/smartcitizen-docs`](https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f) | `0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f` | 2026-10-27 10:52:31 UTC | Official authored documentation |
| **H** | [`fablabbcn/smartcitizen-kit-2x`](https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b) | `3dbbc1061509920aca2dda2aca32abe82563500b` | 2026-09-16 09:32:38 UTC | Hardware designs and firmware |
| **R** | [`fablabbcn/smartcitizen-data`](https://github.com/fablabbcn/smartcitizen-data/tree/4f024f4d42cb40c2cd515062ee7e4815bd2798eb) | `4f024f4d42cb40c2cd515062ee7e4815bd2798eb` | 2026-10-20 14:05:36 UTC | Data tools and candidate experiment |
| **A** | [`fablabbcn/smartcitizen-api`](https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297) | `25a524cbfb036f8950c247b847d8884a4e776297` | 2026-07-01 09:41:31 UTC | Backend application source (not deployed-version proof) |

**Freeze standing:** These four full commits define the **bounded, reproducible source set** for the case study's first evidence pass. Their files were accessed from these exact Git refs, or their presence and blob SHA were verified in immutable directory listings. Selected engineering designs are **indexed but not yet substantively interpreted**; detailed equipment claims belong in I03, then targeted audit I04. Future upstream edits will not silently update this baseline.

**Evidence types:** `PRODUCT-SPEC` (designed model capabilities/configurations); `ENGINEERING` (schematic/firmware implementation); `PLATFORM-DOC` (published data/registration semantics); `CODE-REFERENCE` (example of intended API usage); `UNIT-RECORD` (returned real device metadata, **not obtained**); `OBSERVATION` (actual readings, **not obtained**). Source availability is not source assertion truth or individual-unit evidence.

## 2. Frozen manufacturer documentation (D series)

Source repository **D** in §1. All are manufacturer/project-authored documentation, primarily **product/design-level**.

| ID | Frozen official source | Git blob SHA | Evidence purpose | Limit / qualification |
| --- | --- | --- | --- | --- |
| **D01** | [docs/hardware/kit/index.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/index.md) | `28d4163525a29baae6b67043d0c87cb85507155a` | Kit 2.3 hardware generation, measurement table, optional PM variants | Product-level; published HTML may differ from pinned Markdown |
| **D02** | [docs/hardware/boards/urban-board.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/urban-board.md) | `c93d9de03774f0ebcb59edcb9e22c016cd17ccf5` | Urban Board sensor list, layout/context and PM attachment | Product-level; confirm exact part numbers against schematic |
| **D03** | [docs/hardware/boards/data-board.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/data-board.md) | `9a5da8ac9cac6168c17dd34185b9fe068ce85784` | Data Board, interfaces, processor, logging and power | Product-level; no evidence of actual unit configuration |
| **D04** | [docs/hardware/kit/features.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/features.md) | `04ac11e2207aea80e5608a64a54a601307ecbc7f` | Designed operation modes, power, storage and state indications | Firmware-version caveats; not a runtime trace |
| **D05** | [docs/hardware/kit/specs.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/specs.md) | `358d008adf2325bce6cbed0a540e236da05a0e60` | Physical specifications; imports a separate technical-spec snippet | Must read with D06, not alone |
| **D06** | [docs/includes/specs.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/includes/specs.md) | `cf5e335162d7299498de4017de36673f2a841106` | Actual included absolute/electrical/connectivity specifications | General design ratings, not unit measurements |
| **D07** | [docs/hardware/firmware/index.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/firmware/index.md) | `614ceb208409099aff1100863ea69dc748b8dee6` | Sensor discovery, firmware responsibilities, settings and data path | Documentation about firmware; not installed firmware on any unit |
| **D08** | [docs/guides/getting-started/kit-assembly.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md) | `0ff930c4e5af96e683709dd0fbdd0845767e7786` | Assembly, device registration, deployment and advanced station ID | Hardware/station ID distinction documented for advanced stations |
| **D09** | [docs/guides/data/handling-calibration-data.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/data/handling-calibration-data.md) | `b77b47ed6b4f6dff5f6a960385a372b13d33eda2` | Hardware versus kit ID and calibration/processing provenance | Advanced calibration workflows, not proof IDs exist for basic Kit |
| **D10** | [docs/data/data-platform.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/data/data-platform.md) | `ce3104d3b8d36658ccd2d46c6d86059dbf56df58` | Platform, storage, MQTT/HTTP ingestion, device metadata and API | Describes architecture, not any specific live platform response |
| **D11** | [docs/guides/getting-started/downloading-data.md](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/downloading-data.md) | `f25ac4d264f28e4c44c5eb74304c83031bbd630f` | Documented CSV and REST retrieval methods | Method exists; no observed actual device file |
| **D12** | [mkdocs.yml](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/mkdocs.yml) | `88f3b560cbbbe8682f63e67a722c555eda5cb3b1` | Docs build/navigation and macro/template configuration | Auxiliary source for reproducing rendered documentation |

**Linked content caveat:** D05's `{{ get_snippet_rel("docs/includes/specs.md") }}` imports D06. Without pinning **both** files, “technical specifications” would not be fully reproducible. The published documentation is generated using templates; exact source and rendered HTML are not the same artifact.

## 3. Frozen hardware and firmware (H series)

Source repository **H** in §1. These are authentic hardware/firmware **source artifacts**; a file in the design tree does **not establish** what was installed, manufactured or flashed in a particular unit.

| ID | Frozen official source | Git blob SHA | Evidence purpose | Limit / qualification |
| --- | --- | --- | --- | --- |
| **H01** | [hardware/README.md](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/README.md) | `db7f428954938aff46615bcc2f38bc5e425e0c99` | Repository-defined 2.3 current board/design scope | Descriptive index |
| **H02** | [hardware/SCK2.3/SCK_DATA_BOARD_2.3/SCK_DATA_BOARD_2.3.sch](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_DATA_BOARD_2.3/SCK_DATA_BOARD_2.3.sch) | `c77e75615d16387ca58e5906be3c590d0ddccf0f` | Original Data Board circuit schematic | Available, binary/large engineering source; not yet detail-audited |
| **H03** | [hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.sch](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.sch) | `0d949c30970609189cbd1574271d10d8e18b3813` | Original Urban Board circuit schematic | Available, engineering source; check actual part labels in I03–I04 |
| **H04** | [hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.brd](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.brd) | `285aa3149d7012d20108c742998c7ab3a2bf0479` | Urban Board layout/placement file | Available, layout source; not asserted to be an installed revision |
| **H05** | [sam/src/SckUrban.cpp](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/SckUrban.cpp) | `4f2d549d18a563734ff611c1ddd4bc7a7ff555e8` | SAMD21 firmware implementation of Urban Board sensors | Firmware capability evidence, not actual running firmware |
| **H06** | [sam/src/version.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/version.h) | `984655d4a89b6c34a9be5a7f848865864c0d07bd` | Source constant `SAMverNum = 0.9.11` | Source-tree version string; NOT physical-unit firmware reading |
| **H07** | [sam/platformio.ini](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/platformio.ini) | `a3b16986520e92a727b1d5fe867a1f7f6bafba6a` | Build environments and dependencies | Source build configuration, not field-unit deployment |
| **H08** | [esp/platformio.ini](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/esp/platformio.ini) | `0d745c0c1c238a9e787228a1b3cf5afde99fa36d` | ESP firmware build information | Not proof of any installed firmware |

**Revision scope:** Board-specific `SCK_DATA_BOARD_2.3` and `SCK_URBAN_BOARD_2.3` design files are separated. The Product baseline includes a particulate sensor connection, but **whether an individual kit used SEN50, SEN54, SEN55 or a different supported PM configuration is not proved by a wiring-capability or catalogue description** (Fab Lab Barcelona 2026a, H01; Smart Citizen 2026a, D01).

## 4. Frozen data tooling and prospective device evidence (R series)

Source repository **R** in §1.

| ID | Frozen official source | Git blob SHA | Evidence purpose | Limit / qualification |
| --- | --- | --- | --- | --- |
| **R01** | [examples/notebooks/learning/01_basic_data_exploration.ipynb](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/examples/notebooks/learning/01_basic_data_exploration.ipynb) | `6df07be36a671b37eaa279000159154ed87f97d0` | Official enclosure-test notebook references platform IDs 18486–18489 | 27 cells; 17 code cells; zero executed cells/output: NO empirical readings |
| **R02** | [blueprints/sc_air.json](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/blueprints/sc_air.json) | `786c7568c6f91e4212da0e9bef999c760d853d92` | Air-quality data processing blueprint cited by notebook | Contains processing channels incl. electrochemical sensor logic; NOT proof of base-kit assembly |
| **R03** | [scdata/io/device_api.py](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/scdata/io/device_api.py) | `f263b7a3b0d43128188702071e2ac16413f8ede9` | Library-level Smart Citizen device API/query semantics | Client source code only; not a successful response or unit ID |

**Notebook audit:** R01 contains **27 notebook cells, 17 code cells, none with a saved execution count or output**. A source cell declares `devices_ids = [18486, 18487, 18488, 18489]`, processes them with the **`sc_air` blueprint** and names a test `SCK2.3_ENCLOSURE_TEST`, requesting a **2025-02-12 to 2025-03-07** analysis interval (Fab Lab Barcelona 2026b, R01). These are **potential platform registrations** in code, not verified returned records, not observed measurement data and not four physical-unit hardware IDs. The notebook's use of an air-quality processing blueprint R02 may involve a broader sensor configuration; **do not presume the four records are standard retail SCK2.3 assemblies** until device-level evidence confirms it.

**Advanced station calibration files:** The same R repository has a separately organized `hardware/SCAS*.json` collection that demonstrates **station-specific hardware-calibration IDs**. These files are *not* silently included as evidence for the basic SCK2.3 case, and none has yet been linked to one of 18486–18489.

## 5. Frozen API backend source (A series); live API remains external

Source repository **A** in §1.

| ID | Frozen official source | Git blob SHA | Evidence purpose | Limit / qualification |
| --- | --- | --- | --- | --- |
| **A01** | [README.md](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/README.md) | `fdcd132cf9237f389664094926a58bbb160454d8` | Backend API project architecture and published API address | Repository source does not prove what revision production is running |
| **A02** | [VERSION](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/VERSION) | `e25d8d9f357cfa028ffbf2f7bdc597e28968696b` | Source-tree version string `1.1.5` | Not a verified production release/version |

**Separate, unfrozen published interface reference:** [Smart Citizen API documentation](https://developer.smartcitizen.me/) (accessed 27 October 2026) describes device registrations, sensors, measurements and the `GET /v0/devices/:id` and historical-readings endpoints. The project's [Data Platform documentation](https://docs.smartcitizen.me/data/data-platform/) explains ingestion through MQTT/HTTP and storage of device metadata/readings (Smart Citizen 2026b, D10). The API reference's JSON illustrations are **examples**, sometimes with historic timestamps, **not evidence of a retrieved 2026 or 2025 unit record**. The backend source snapshot **does not identify what commit the production API deployed**.

**Actual-data retrieval attempts (not evidence records):** During I02, the public `https://api.smartcitizen.me/v0/devices/{18486,18487,18488,18489}` requests failed to yield a readable response in the available browser retrieval environment, and independent HTTP attempts from the execution container failed at **DNS resolution**, before any HTTP status was obtained. Attempts to inspect `https://smartcitizen.me/kits/18486` and `.../18487` also did not return readable records. **These are access/tool failures, not proof the service is down, that the IDs are invalid, or that no data exist.** No JSON, CSV, timestamped measurement or hardware-ID association was observed. No access token was requested or used.

**A productive follow-up path:** Device metadata and reading records should be checked in a normal working external connection or via a **public, source-verifiable archival data file**. If an individual hardware identifier is unavailable, retain a platform-record-level test and mark physical identity unverified. Do not assume that a device/kit ID is the physical hardware ID.

## 6. Version/source discrepancies that must not become silent facts

1. **RETRACTED AFTER I04 AUDIT — claimed rendered-page part mismatch:** During I02 an unsupported research claim said the public Urban Board/Kit tables used different names such as `AS7311`, `BH1721FVC`, `ICS-434342`, and `MPL3115A26S`. **That discrepancy was not reproduced** in the 27 October 2026 independent check: the [published Urban Board table](https://docs.smartcitizen.me/hardware/boards/urban-board/) and [Kit table](https://docs.smartcitizen.me/hardware/kit/) agree with frozen **D01/D02**. The SCK2.3 schematic **H03** independently names `AS7331`, `BH1730FVC`, `ICS-43432`, and `MPL3115A2`. The earlier claim is preserved here solely to make the correction visible; **do not use it as manufacturer-conflict evidence**. See [I04 FLAG-01](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md#flag-01--supposed-public-site-versus-frozen-source-part-number-disagreement).
2. **Design/firmware versus deployed unit:** H06 contains a source-tree string `SAMverNum = "0.9.11"`. That says nothing about the firmware revision **actually running** in an individual kit. D04/D07 describe supported features and firmware-dependent operation; they likewise do not establish runtime state.
3. **SCK Kit versus SCK Station:** D08/D09 explicitly distinguish station **hardware ID** from platform **device/kit ID**, and warn that one physical station can be registered multiple times. Those examples concern advanced station/calibration workflows; **do not automatically assign such station IDs to a basic SCK2.3** (Smart Citizen 2026c, D08–D09).
4. **Engineering source vs donor standard:** Neither a software API node nor a firmware channel label establishes a new domain class, physical composition relation, actual sensor deployment or conformance with a donor standard. The five prior V2 passes remain **candidate research**, not accepted model structure.

These are **explicit risks for the next fact register and audit**, not an attempt to complete their substantive resolution in I02.

## 7. Relevant standards environment — named editions, not re-audited here

The product-corpus freeze does **not** redefine the project's normative/semantic sources. The subsequent donor mapping must name exact editions and distinguish source-native from project interpretation. The principal already selected baselines are: [OGC API – Connected Systems Part 1, OGC 23-001 v1.0](https://docs.ogc.org/is/23-001/23-001.html); [Part 2, OGC 23-002 v1.0](https://docs.ogc.org/is/23-002/23-002.html); [OGC SensorML 3.0, OGC 23-000](https://docs.ogc.org/is/23-000/23-000.html); [OGC Observations, Measurements and Samples 3.0 / ISO 19156:2023, OGC 20-082r4](https://docs.ogc.org/as/20-082r4/20-082r4.html); and the **21 October 2026 Working Draft** of [SOSA/SSN (2023 Edition)](https://www.w3.org/TR/vocab-ssn-2023/), which is not interchangeable with earlier editions cited by CSAPI 1.0. Additional selected donor standards retain their precise editions and ceilings as recorded by the [five-pass checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md), [C08 audit](../../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md) and [30-lineage trust triage](../../DIM_Profile_V2_Anatomy_PhaseA_Bulk_Trust_Triage_v0.1_26OCT2026.md). **No new standards conformance assessment was performed during I02.**

## 8. I02 disposition and instructions for I03

**I02 PASS for a reproducible *product-design/source corpus*; CONDITIONAL for an actual individual-unit case.** We have version-pinned authoritative source material sufficient to begin source-native *product-level* fact extraction. We have **NOT** obtained an independently verifiable unit record, hardware identifier, installed sensor inventory or actual measurements. The planned Gate A audit (I04) must decide whether remaining limitations are acceptable or whether a different physical-unit evidence source is necessary. The 13-iteration workflow must not launder missing unit data into a fabricated instance.

**I03 — Source-native fact extraction:** Use the **D/H/R/A source IDs and exact pinned URLs above**. Give each substantive fact its own evidence ID, native term, exact source file/section, explicit PRODUCT/DESIGN/IMPLEMENTATION/PLATFORM/UNIT/OBSERVATION evidence level, and any contradiction/limit. Consult H03/H04 when part numbers matter, but do not infer actual unit assembly from them. Include an explicit **“No verified individual-unit facts available”** entry rather than invent values. **Do not apply DIM class mappings until I05**, and do not audit every donor as a replacement for the focused I04 evidence check.

**Next: Iteration I03 — extract source-native equipment facts. Say “proceed” to begin.**

## References (Chicago Manual of Style, 18th ed., author–date)

Fab Lab Barcelona. 2026a. *Smart Citizen Kit 2.X Hardware and Firmware*. Repository source at frozen commit `3dbbc1061509920aca2dda2aca32abe82563500b` (16 September 2026). https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b.

Fab Lab Barcelona. 2026b. *Smart Citizen Data Tooling and Examples*. Repository source at frozen commit `4f024f4d42cb40c2cd515062ee7e4815bd2798eb` (20 October 2026). https://github.com/fablabbcn/smartcitizen-data/tree/4f024f4d42cb40c2cd515062ee7e4815bd2798eb.

Fab Lab Barcelona. 2026c. *SmartCitizen API Backend*. Repository source at frozen commit `25a524cbfb036f8950c247b847d8884a4e776297` (1 July 2026). https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297.

Smart Citizen. 2026a. *Smart Citizen Documentation*. Frozen Git source at commit `0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f` (27 October 2026), especially D01–D12. https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f.

Smart Citizen. 2026b. “Data Platform,” frozen source D10. https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/data/data-platform.md.

Smart Citizen. 2026c. “Assembling a Smart Citizen Kit,” D08, and “Handling Calibration Data,” D09. https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md; https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/data/handling-calibration-data.md.

Smart Citizen API. n.d. “SmartCitizen API Reference.” Accessed 27 October 2026. https://developer.smartcitizen.me/.
