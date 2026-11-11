# SOSA-G2-7J — original C239 §13.5.2.3 J2-Signal Connector and §13.5.2.3.1 Power Enable

**SOURCE, SAME SAVED EXCEL AND INDEPENDENT VERIFICATION PASS (11 November 2026).** [Source-native ledger](SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json) · [saved workbook validation](SOSA_G2_7J_Workbook_Validation_11NOV2026.json) · [publisher PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/43039375756) · [independent original-source/master/saved-Excel PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/43039671439). Exactly 25 G2-7J qualified donor-column-I cells are current in canonical JSON, BOTH CSV mirrors, BOTH GitHub-readable comparison tables and the SAME 26-sheet original editable Excel; all 346×15 actual saved cells match, 22 prior historical worksheet XMLs preserved, Excel lag ZERO, SHA256 `8a962811eb1d6243156c3efb8b40ce874a42ae58dcc96f08203b0b9287e3de52`. Original figure, dense source table/checkmark geometry, external standard/native file and runtime hardware evidence remain held; no DIM/Profile adopted. The Open Group SOSA Consortium, *Technical Standard for SOSA Reference Architecture*, Edition1.1 (2023), C239 original project Library `c239_5.pdf` **PDF278–285 / printed252–259**. Authorized source scope is original §13.5.2.3 including all six pages of Table13.5.2.3-1 and §13.5.2.3.1 Power Enable, **STOP BEFORE §13.5.2.3.2 Ethernet (Copper)**. The original text was read directly including figure caption, table labels, numbered Rules and Observations. [Stable original source-item ledger](SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json) contains **134 source-record entries**: 2 nested source-section records, 8 numbered Rules (**six printed Inspection (I), two Test (T)**), four Observations, 1 figure caption, 1 six-page table, seven source narrative/table contexts, 26 signal-group records and 85 individually transcribed pin-label records. It also records **two grouped unresolved pin rosters**, **103 printed pin/contact designator tokens**, **22 local exact holds** and **25 existing-row qualified donor comparisons**. These are not 134 numbered SHALL requirements.

## 1. Native connector and bounded source Rule/Observation inventory

**Rule13.5.2.3-1 (SHALL, I)** requires the J2 **25-7 insert** portrayed by **Figure13.5.2.3-1**. **Rule13.5.2.3-2 (SHALL, I)** requires assignment to **Table13.5.2.3-1 when J2 is used**. The source table describes an N-keyed physical interface, with a sensor-side MIL-DTL-38999/***J7SN receptacle/socket and host-platform umbilical MIL-DTL-38999/26*J7PN plug/pin. This is a conditional physical connector role, not an application programming interface or universally mandatory CSAPI resource property. The figure image pixels/contact layout are **not** verified, despite original figure-caption and all table text labels being available.

**Rules13.5.2.3-3 and -4 (SHALL, T)** concern reception of an **isolated +28 VDC discrete signal**, defining logic **1 at ≥18.0 VDC** and logic **0 at ≤1.5 VDC** respectively. **The range between these thresholds is not assigned a universal value by these two Rules**. Observation13.5.2.3-3 notes that some acquisition programs may accept a higher logic-zero voltage following system safety analysis, but that source observation is not an unrestricted change to both binding Rules. Observation13.5.2.3-1 says commercial-protocol pinouts/names can deviate slightly to preserve ground/signal integrity; this does not allow invented connector maps. Observation13.5.2.3-2 discusses optional signal returns for electromagnetic compatibility/electromagnetic interference and platform integration; Observation13.5.2.3-4 describes **2419** wire as **American Wire Gauge (AWG) 24, silver-plated, 19 strands**. Each remains an Observation, not a numbered Rule.

## 2. Source-text audit of the multi-page J2 signal allocation table

Original Table13.5.2.3-1 spans **PDF279–284**, and records source direction, signal name, wire type, pin designator, signal type and usage-by-sensor-modality flags. It includes **26 named source signal groups** and **103 printed individual pin/contact designator tokens** (the latter count includes twinax subcontact names and *does not* assert a verified standard physical connector contact count). The 85 individually transcribed pin rows and two grouped rosters are carefully distinguished. Group-level source direction and signal naming are recorded, but full graphical matrix cell alignment and contact orientation **remain held**.

| Original signal-group family | Printed designator count | Source-side direction/role as readable |
| --- | ---: | --- |
| POWER_ENABLE | 2 | Platform |
| ETHERNET | 12 | Platform/Sensor |
| SERIAL1 | 5 | TX Sensor, RX Platform, return unassigned in source text |
| SERIAL2 | 5 | TX Sensor, RX Platform, return unassigned in source text |
| SERIAL3 | 5 | TX Sensor, RX Platform, return unassigned in source text |
| SERIAL4 | 5 | TX Sensor, RX Platform, return unassigned in source text |
| ARMING | 2 | Platform |
| NEZ | 4 | Platform |
| MODE | 4 | Platform |
| ANNUNCIATION | 2 | Sensor |
| SAFETY | 6 | Sensor |
| GIMBAL | 2 | Platform |
| PPS | 2 | Platform |
| RESERVED | 2 | NOT ASSIGNED |
| HC_POWER | 2 | Sensor |
| PURGE | 3 | Platform |
| MIL1553 | 6 | Platform/Sensor/Backshell |
| USB_DATA | 3 | Platform/Sensor |
| USB_PWR | 3 | Sensor |
| LVDS1 | 2 | DIRECTION NOT PRINTED |
| LVDS2 | 2 | DIRECTION NOT PRINTED |
| LVDS3 | 2 | DIRECTION NOT PRINTED |
| LVDS4 | 2 | DIRECTION NOT PRINTED |
| LVDS5 | 2 | DIRECTION NOT PRINTED |
| SENMAN | 10 | Sensor |
| ARMING_ISOLATION | 8 | NOT SPECIFIED |

The source prints **ten sensor-manufacturer pin positions** (24,31,32,39,40,57,58,66,67,74) next to `SENMAN_1 to SENMAN_10`; the original extracted text does **not** independently prove each pin-to-`SENMAN_n` positional association, so this remains one held group record. It also prints **eight pins reserved for arming isolation** (1,3,9,10,87,88,94,96) without individual signal assignments. MIL-STD-1553B twinax insert designators **25-1/25-2/25-S and 75-1/75-2/75-S** are preserved literally and not collapsed into plain numeric 25/75. Modality checkmark placement across the original EO-IR, Radar/SAR, EW, SIGINT and Communications columns is not pixel-verified, even where the printed inline signal label is clearly readable.

## 3. Original Power Enable electrical switch: not a CSAPI Command

Original §13.5.2.3.1 explains why the platform may need a **controlled sensor shutdown sequence** instead of abruptly removing input power. A platform-controlled switch, relay or solid-state relay (or platform-side human) joins physical `PWR_EN` and `PWR_EN_RTN`; **the sensor provides voltage** for that enable circuit. An externally **open** circuit signifies disabled Power Enable, while an externally **closed** circuit enables it. **Rule13.5.2.3.1-1 (SHALL, I)** specifies entry into **power OFF** for circuit resistance **≥100 kΩ**; **Rule13.5.2.3.1-2 (SHALL, I)** specifies entry into **power ON** for **≤5 Ω**. There is no complete source rule for every resistance between these thresholds, nor independently observed power transition on source-case equipment.

**Rules13.5.2.3.1-3 and -4 (SHALL, I)** limit the Power Enable signal's sourced current to **100 mA maximum** and driven voltage to **30 VDC maximum**. This is conditional physical signaling, **not** a CSAPI `Command`, web control endpoint, authorization, successful command acknowledgement, observation result, actual device power-on evidence, battery presence, or telemetered status. The **Power Enable circuit** is separate from **J1 platform input-power distribution** reviewed in G2-7I.

## 4. Source-to-DIM correspondence and evidence-based coverage

The original ledgers provide **25** native source-ID-qualified existing-row correspondences for specialized physical constituents and platform connections, transport wires vs active networks, declared timing vs observed time, electrical numeric thresholds vs measured values, arming/safety signals vs actual authorization/control/status, and the negative-equivalence boundaries of the four original equipment cases. Only **The Open Group SOSA donor column I** changes. No new canonical information row, final domain name, chassis/class hierarchy, control action, actual installation, vendor property or **Connected Systems API (CSAPI) Profile SHALL** is authorized by the source review.

**Original 192 registered-heading coverage remains 173 at least sampled/inline-reviewed, 18 substantively unread and one restricted**, because §13.5.2.3 and §13.5.2.3.1 are **nested beneath already counted §13.5.2**. Do NOT award new registered-heading credit for nested names. The §13.5 and §13.5.2 parent sources remain PARTIAL; unreviewed §13.5.2.3.2 and later clauses, figure pixels, original MIL-DTL/IEEE/USB/TIA companions, eight native C239 data-model/API files, 2025 S251 source and restricted security overlay remain unresolved. The original primary-source text/figure grades, 22 local exact holds, existing ISA/C239 prior questions and zero independent device conformance must be retained.

**Mandatory L23 source-to-SAME Excel gate SATISFIED:** Source-qualified canonical JSON, BOTH CSV mirrors, BOTH readable comparison tables and SAME 26-sheet original Excel all passed 346×15 actual saved-cell parity, preserved previous worksheet XML and independent source/Excel GitHub checks. **STOP before §13.5.2.3.2**; only a distinct new owner Proceed authorizes **G2-7K** starting that Ethernet subsection. SOSA remains ACTIVE/OPEN and SAPIENT Step18 blocked.
