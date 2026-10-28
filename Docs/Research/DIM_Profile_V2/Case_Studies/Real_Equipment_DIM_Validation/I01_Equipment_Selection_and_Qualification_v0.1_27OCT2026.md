# Iteration I01 — Equipment Selection and Qualification

**Date:** 27 October 2026  
**Workstream:** [Real Equipment DIM Validation](README.md) · [13-Iteration Plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md)  
**Status:** **I01 COMPLETE. Smart Citizen Kit (SCK) 2.3 selected as the real-product baseline, subject to verification of a specific physical-unit evidence chain during I02–I04.**  
**Not done:** Source corpus not frozen; no individual unit/measurement verified; no Domain Information Model (DIM) concept adopted; no Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) mapping undertaken.

## 1. Selection decision

**Select the Fab Lab Barcelona Smart Citizen Kit 2.3 (SCK2.3)**, initially the manufacturer's normal **Data Board + Urban Sensor Board + supported particulate-matter sensing** configuration, as the real equipment family for this case study. The project's official documentation calls SCK2.3 its latest Kit generation and specifies version-specific measurements and modular electrical/physical structure (Smart Citizen 2026a, “What is the Smart Citizen Kit?,” “Versions,” “Measurements”). The open hardware/firmware repository contains separate **SCK2.3 Data Board and Urban Board** design directories, with board and schematic files (Fab Lab Barcelona 2026a).

**Why this is suitable:** We have authoritative, accessible, version-aware source material describing a real equipment product—its physical construction, measurable variables, sensors, firmware, optional attachments, communication and power. The official platform documentation explains exposure of device records and readings, enabling a test of the distinction between a manufactured device and its online registration (Smart Citizen 2026b; Smart Citizen 2026c). The source range is wide enough to challenge the project's existing five *candidate* semantic distinctions, yet bounded enough to investigate without another donor survey.

**What this selection does NOT establish:** We have **not identified a specific verified physical SCK2.3 unit** with a source-confirmed hardware/station identifier, firmware revision, populated components, configuration, location and observations. Nor have we established that all sensor options in the manufacturer's version table were fitted to any one historical unit.

## 2. Qualification checks and evidence

| I01 criterion | Evidence checked | Finding and standing |
| --- | --- | --- |
| **Identifiable actual product/version** | Official Kit documentation distinguishes SCK2.1, SCK2.2 and **SCK2.3**; publishes version-specific sensor differences (Smart Citizen 2026a). | **PASS — product level.** Base target is **2.3**. Do not mix the 2.2 barometric sensor or optional particulate variants into a supposedly exact 2.3 individual configuration. |
| **Meaningful equipment/component detail** | Data Board + Urban Board + particulate-matter module and optional auxiliary connections; official GitHub `hardware/SCK2.3/` contains board schematics and layouts (Smart Citizen 2026a, 2026d; Fab Lab Barcelona 2026a). | **PASS — product/design level.** Actual installed configuration remains unit-specific. |
| **Technical operation and measurable outputs** | Manufacturer docs cover environmental channels including temperature, humidity, noise, light, pressure, ultraviolet and particulate matter, plus firmware, battery/power, Wi-Fi and stored/uploaded readings (Smart Citizen 2026a, 2026e, 2026f). | **PASS — documentation available.** This is evidence of designed/advertised support, **not** observations or status of a fielded unit. |
| **Digital representation and source data path** | Manufacturer describes its public Smart Citizen platform, documented device and reading endpoints, MQTT ingestion and API-backed website (Smart Citizen 2026b; Smart Citizen API n.d.). | **PASS — published architecture and access method.** **Actual live API responses were not retrieved in this iteration**; availability and data records are unverified. |
| **Potential reference to individual records** | Official project `smartcitizen-data` notebook at pinned commit `4f024f4d42cb40c2cd515062ee7e4815bd2798eb` uses platform device IDs **18486, 18487, 18488, 18489**, with a test named `SCK2.3_ENCLOSURE_TEST` and a historical data request window **12 February–7 March 2025** (Fab Lab Barcelona 2026b, `examples/notebooks/learning/01_basic_data_exploration.ipynb`, source cells). | **CONDITIONAL — candidates only.** These are *referenced platform device-registration IDs in unexecuted notebook cells*, not verified physical hardware IDs, returned measurements or four proven physical SCK2.3 units. |

**Crucial native identity warning:** Smart Citizen explicitly warns that the physical **hardware/station ID** used for advanced sensor/calibration records is **not** the platform's `device ID`/kit-page number: the hardware ID is intended to remain fixed, while the device-page ID can change when the same hardware is registered again (Smart Citizen 2026c, “Advanced devices”; Smart Citizen 2026g). This guidance concerns advanced-station workflows and does **not** by itself prove the basic SCK2.3 units in the notebook expose such a hardware ID. **Do not use platform ID 18486 as a manufacturer's physical serial number or assert that one platform record equals one irreversibly identified physical device.**

## 3. Specific source evidence located (discovery links, NOT the I02 frozen corpus)

**Official current documentation:** [Smart Citizen Kit product, generations and measurements](https://docs.smartcitizen.me/hardware/kit/); [technical specifications](https://docs.smartcitizen.me/hardware/kit/specs/); [features, modes and power](https://docs.smartcitizen.me/hardware/kit/features/); [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board/); [firmware](https://docs.smartcitizen.me/hardware/firmware/); [Data Platform](https://docs.smartcitizen.me/data/data-platform/); [assembly, registration and hardware-ID warning](https://docs.smartcitizen.me/guides/getting-started/kit-assembly/); [calibration hardware ID versus platform ID](https://docs.smartcitizen.me/guides/data/handling-calibration-data/).

**Engineering evidence:** [Fab Lab Barcelona SCK2.3 hardware and firmware repository at commit `3dbbc1061509920aca2dda2aca32abe82563500b`](https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3), with `SCK_DATA_BOARD_2.3` and `SCK_URBAN_BOARD_2.3` subdirectories and `.sch`/`.brd` source; upstream docs repository currently observed at [commit `0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f`](https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs). **I02 must explicitly freeze and audit versions; these are discovered anchors, not a completed source register.**

**Candidate individual-platform evidence:** [Official `smartcitizen-data` example notebook at commit `4f024f4d42cb40c2cd515062ee7e4815bd2798eb`](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/examples/notebooks/learning/01_basic_data_exploration.ipynb). The notebook lists **18486–18489** and labels a test as SCK2.3 enclosure study. It has **no executed outputs in the inspected source cells**; therefore it is *a useful path to look for data*, not confirmation that measurements are presently available.

**Platform/API documentation:** [Smart Citizen API reference](https://developer.smartcitizen.me/) describes `GET /v0/devices/:id`, `/readings` and the differentiation of device registrations from real-world equipment. Treat the older examples inside this documentation as **examples, not 2026 measurements**.

## 4. Explicit evidence limitations and risk decision

**Direct-live-access limit:** Requests to `https://api.smartcitizen.me/v0/devices/` in this execution environment could **not be read successfully**, including a historic device example and a dataset-discovery request. This **does not prove the platform is down or its endpoints are inaccessible to normal users**; it means we have **not independently observed live metadata, current sensor values, the actual platform hardware/version field, or a verified mapping from any specific platform ID to an individual physical SCK2.3**.

**Selection decision:** **PROCEED WITH SCK2.3 as a real documented hardware product**, but record the specific-instance validation as **OPEN**, not PASS. We have stronger direct engineering documentation than necessary for the product baseline; switching hardware families today would add unnecessary search and reset work. On the other hand, we should **not** claim that the future case study demonstrates physical-instance identity or live observations until supported by actual data or verified archived records.

**Fallback if needed:** At I02, check the pinned official notebook's linked candidate IDs and any official, downloadable, source-traceable archived records or device–hardware-ID mapping. If direct API access remains impossible, seek **officially published historical data** with clear source identity or select a more accessible independently documented unit. If the evidence cannot be obtained, carry product-level validation forward as limited, and explicitly mark unit/observation-level claims **NOT TESTED** at Gate A (I04). Do **not** create an example serial number or call a platform ID a physical ID just to satisfy a schedule.

## 5. I01 disposition and next action

**I01 COMPLETE**: selection and source qualification performed at **product level**, with a genuine identified **evidence gap at individual-unit level**. No datum or source identity has been silently invented, and no DIM concepts or CSAPI profile requirements have been adopted.

**Next: I02 — Freeze source corpus.** Pin official hardware/documentation repositories and relevant manufacturer pages by edition/commit; establish the stable source register and attempt to validate an actual historic SCK2.3 device record, its measurements and its relationship (if demonstrable) to a physical unit. Record inaccessible sources or incomplete provenance rather than assume successful retrieval. **Say “proceed” to begin.**

## References — Chicago Manual of Style, 18th edition, author–date

Fab Lab Barcelona. 2026a. *smartcitizen-kit-2x: Smart Citizen Kit 2.X hardware and firmware*, commit `3dbbc1061509920aca2dda2aca32abe82563500b`, 16 September. https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3.

Fab Lab Barcelona. 2026b. *smartcitizen-data: Examples/notebooks/learning/01_basic_data_exploration.ipynb*, commit `4f024f4d42cb40c2cd515062ee7e4815bd2798eb`, 20 October. https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/examples/notebooks/learning/01_basic_data_exploration.ipynb.

Smart Citizen. 2026a. “Smart Citizen Kit.” Official hardware documentation. Accessed October 27. https://docs.smartcitizen.me/hardware/kit/.

Smart Citizen. 2026b. “Data Platform.” Official project documentation. Accessed October 27. https://docs.smartcitizen.me/data/data-platform/.

Smart Citizen. 2026c. “Assembling a Smart Citizen Kit.” Official project documentation, “Advanced Devices.” Accessed October 27. https://docs.smartcitizen.me/guides/getting-started/kit-assembly/.

Smart Citizen. 2026d. “Data Board.” Official project documentation. Accessed October 27. https://docs.smartcitizen.me/hardware/boards/data-board/.

Smart Citizen. 2026e. “Technical Specifications.” Official project documentation. Accessed October 27. https://docs.smartcitizen.me/hardware/kit/specs/.

Smart Citizen. 2026f. “Features.” Official project documentation. Accessed October 27. https://docs.smartcitizen.me/hardware/kit/features/.

Smart Citizen. 2026g. “Handling Calibration Data.” Official project documentation. Accessed October 27. https://docs.smartcitizen.me/guides/data/handling-calibration-data/.

Smart Citizen API. n.d. “SmartCitizen API Reference.” Accessed October 27, 2026. https://developer.smartcitizen.me/.
