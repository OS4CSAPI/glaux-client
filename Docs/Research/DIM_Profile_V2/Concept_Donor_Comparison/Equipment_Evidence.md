# Equipment Evidence — Connections to the Candidate DIM

**Version 0.1 · 30 October 2026 · America/New_York**  
**Iteration 3 complete: documentary comparisons, not implemented transformations.** Final verification and the next-task recommendation remain Iteration 4.  
**Input snapshot:** `8e4a126fbf2877c38737b685a0cdb90fee32595f`, branch `research/dim-profile-v2`.

[Concepts and donor comparisons](README.md) · [Donor contributions](Donor_Contributions.md) · [Four-iteration plan](../PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) · [Drift correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md)

## 1. What this comparison establishes

**The three equipment sheets can exercise specific meaning distinctions, but they do not supply three complete operating Systems.** Here, each source fact is connected to the current candidate Domain Information Model (DIM) discussion, or explicitly left unresolved. Identity, construction, capabilities, configuration, messages, processing, time, and diagnostics are included; power is one information area, not the organizing priority.

The direction is **equipment information → candidate meaning or unresolved question**. These correspondences are this iteration's analyst application of the existing research. They are not manufacturer-declared mappings, proof that the equipment implements a donor standard, new DIM definitions, or an OGC API – Connected Systems (CSAPI) Profile binding. The [selection decision](../Controlled_Corpus/07_Corpus_Qualification_Decision.md) and [preservation handoff](../Controlled_Corpus/08_Frozen_Corpus_Manifest_and_Handoff.md) retain their documentary/reference-example scope.

| Reading label | What it establishes here | What it does not establish |
| --- | --- | --- |
| **Supported distinction** | The sheet explicitly identifies a source meaning that fits a distinction already explained by the candidate foundation. The connection and its reason are visible. | A complete mapping, adopted class/property, source-declared equivalence, or passing conversion test. |
| **Proposed treatment** | The source information is available, but its detailed common representation or relationship is still a hypothesis. The relevant open question is identified. | A finished concept hidden behind a familiar heading. |
| **Hold interpretation** | The source value, label, or definition is retained, but a material meaning, applicability, or data link is unresolved. | Permission to infer the missing fact from a field name, a different example, or general knowledge. |

These are reading labels, not new confidence scores or replacements for the existing source evidence labels. **Design** means `PRIMARY_DESIGN_OR_SPEC`; **Example** means `PRIMARY_PUBLISHED_EXAMPLE`; **Derived** means `SYNTHETIC_OR_DERIVED`; **Unknown** means `UNAVAILABLE_OR_UNVERIFIED`. All three sheets report no acquired actual operating history. A timestamp in an example does not change that standing.

**Three kinds of gap remain separate:** a **model gap** is missing common meaning/structure; a **donor-review gap** is insufficient comparison of potentially relevant donor material; an **equipment/source gap** is an absent record, unknown applicability, or unresolved native meaning. More donor research cannot supply a missing serial number or repair an unexplained vendor unit. Conversely, obtaining a record does not by itself settle the common model.

<a id="donor-bridge"></a>
## 2. Which existing donor findings are relevant?

This table links to the existing comparison and its exact source trail. It does not declare the listed donors exhaustive or assign their native classes to these products. F-01–F-05, REL-01–REL-10, and DC05-G01–G05 remain the existing research labels; G01–G05 below are their short forms, not new concepts.

| Candidate distinction or open question | Existing donor basis to follow | Equipment-side use here |
| --- | --- | --- |
| [Individual versus kind/description — F-01/F-02](README.md#individual-system) and [kind discussion](README.md#kind-model) | CSAPI subject/kind; Asset Administration Shell type/instance; Smart Applications REFerence (SAREF) DeviceKind; OPC Unified Architecture (OPC UA) Model versus DeviceType; SAPIENT model versus role. | Keep a model designation or example identifier separate from an identified installed unit. No actual REL-01 instance link is asserted. |
| [Capability/method versus activity — F-03, REL-02/03](README.md#method-and-activity) | CSAPI, Observations, Measurements and Samples (OMS), SensorML, and edition-qualified SOSA/SSN; SAPIENT and Integrated Sensor Architecture (ISA) add declaration/request/outcome distinctions. | Separate documented settings and commands from applied configuration or execution. G01/G02 retain the unfinished behavior/action treatment. |
| [Part, function, channel and association — F-04, REL-04–07](README.md#composition) | SensorML process descriptions, CSAPI associations, IEEE 1451 channel/self-description, The Open Group SOSA part/function/product/host, ISA exposure/taskability. | Keep hardware, output fields, bus addresses and external services distinct. G03/G04 remain open; no compulsory subsystem tree or channel-per-chip rule. |
| [Representation, producer and time — F-05, REL-08–10](README.md#representation) | CSAPI producer/resource roles; Web of Things mediation; OPC UA online/offline distinctions; SAPIENT report/middleware context; ISA mediated sources. | Preserve what a message concerns and its documentary context. No verified identity join, live service, or actual recursive CSAPI discovery is implied. |
| [Additional open questions](README.md#open-questions) and [unrepresented contributions](Donor_Contributions.md#open-contributions) | G01/G02 behavior/actions; G03 channel metadata; G04 multiple structures; G05 mediation. | Locate incomplete interpretations without turning every unmatched field into “operational condition.” Preliminary donor leads remain distinct from reviewed correspondences. |

<a id="airgradient"></a>
## 3. AirGradient Open Air Max

**Reference subject:** the gas-equipped `O-M-1PPSTON-CE` design, not a verified installed unit. Hardware, firmware, local-device examples, and the two cloud examples remain separately attributed. The world-endpoint (W) and location-endpoint (L) cloud examples are not a synchronized record. [Identity/context][a-identity]; [source key][a-sources].

| Exact sheet inputs and source | Available information and evidence | Candidate connection and why | Disposition and unresolved gap |
| --- | --- | --- | --- |
| [A-I01–I04, I16][a-identity]; [A-API25/26/36][a-cloud-identity]. A01/A02/A04/A09. | Model string `O-M-1PPSTON-CE`; separate `-CE-S` spelling; independent source revisions. Cloud `firmwareVersion` is null and `serialno` is `"00000example"`. Design/Example/Unknown. | F-01/F-02/F-05 distinguish product description, source version and individual identity. | **Supported distinction.** No installed unit, verified revision pair, suffix equivalence, or actual REL-01/09 identity association. Equipment/source gaps A-G01/G06. |
| [A-I05–I10, I14][a-components]. A01. | Named main board/modules, two PMS5003 sensors, and spare connectors; Design. Output quantities are not separately identified hardware. | F-04 and G03/G04: physical component information differs from reported quantity/channel and available connector. | **Supported distinction; proposed relationship treatment.** No per-output System identities, attached spare-port equipment, or newly asserted IEEE 1451 implementation. Detailed component/channel relations remain a model gap. |
| [A-I07][a-co2-design]; [A-F01][a-co2-example]. A01/A02. | CO2 module range 0–5,000 ppm is Design; `rco2 = 452` is a numeric Example, ppm. Neither supplies an authenticated measurement event. | F-02/F-03: a capability/range and a sample value make different claims; REL-02 does not establish REL-03. | **Supported distinction.** Detailed performance/quantity treatment is open; the missing event and producer join are equipment gaps, not proof the sensor lacks that capability. |
| [A-C02, C06–C08][a-settings]. A02/A03. | Cellular is a documented default; Boolean `co2CalibrationRequested` and `ledBarTestRequested` and integer `abcDays` are supported configuration fields. No queried values or outcomes. Design. | F-03 with G01/G02: supported choice/request is not selected mode, completed calibration or performed test. | **Supported distinction; proposed state/action treatment.** No current configuration, acknowledgement, test result or universal action lifecycle. A-G02. |
| [A-C09][a-timing-readme]; [A-M01–M04][a-modes]. A02/A07. | README configuration checks every hour; separate guide from firmware 0.7.0 onward gives 90-minute/daily checks. Guide intervals and voltage conditions are Design, not active state. | F-05 source/applicability qualification; G01 for allowed behavior versus current report. | **Hold a unified schedule.** Keep the source contexts separate; no inferred deployed version, tie-breaking rule or missing boundary value. A-G01/G06. |
| [A-F07/F08/F13–F17][a-device-signals]; [A-API17/18/27/28/30–35/39–43][a-cloud-signals]. A02/A08/A09. | Raw signals, electrode mV, concentration/corrected-named fields and unresolved `measure4`/`afeTemp` coexist. Examples; documented scaling is Derived. Gas-validity cautions persist. | G03 concerns scope/units/processing; F-03/F-05 prevent a description or correction label proving a valid measurement or known method. | **Proposed treatment; hold unresolved units, algorithms and calibrated-gas claims.** No raw-to-concentration equivalence or Celsius assumption. A-G04/G05; model and equipment/source gaps. |
| [A-C10–C12][a-paths]; [A-F18 and device context][a-device-context]; [A-API16/24][a-cloud-time]. A02/A09. | Cellular interval `180` s, three example groups without absolute time/subject ID; Wi-Fi and cellular caching differ. Cloud timestamp strings have `Z`; separate timezone label is `Asia/Bangkok`. Design/Example. | F-05/REL-10: reporting path and source context affect interpretation; F-03/REL-03 requires event evidence, not just a readable time string. | **Supported distinction; proposed temporal/mediation treatment.** No synchronization, delivery proof, live record, or timezone overwrite. A-G03/G06. |
| [A-F11/F12][a-voltage-device]; [A-API37/38][a-voltage-cloud]. A02/A09. | Numeric Wi-Fi `volt = 11.24 V`; cellular `1124 / 100`; cloud `batteryVoltage = "12.25"` and `panelVoltage = "17.18"` are strings. Wi-Fi/cellular panel examples differ. | F-05 preserves separate paths/types; G03 exposes quantity/subject qualification still needed beyond the existing foundation. | **Proposed quantity treatment.** No joined reading, silent string-to-number substitution, capacity percentage or health verdict. The power heading is not a defined DIM destination. |
| [A-L01–L13][a-leds]; [A-API01–API06][a-location-service]. A02/A07/A09. | Local LED patterns are Design; cloud `offline = false` is an Example Boolean. Location IDs and zero coordinates are placeholders, not deployment evidence. | F-03/F-05 distinguish indicator meaning, example service assertion and actual state; G01/G05 remain incomplete. | **Supported distinction; proposed diagnostic/service treatment.** No observed LED history, whole-system readiness, authenticated location or software-to-equipment identity join. A-G01/G03. |

**What this case can exercise:** whether a proposed representation keeps design, source revision, supported configuration, raw/derived signal, reporting path and example record apart. It cannot establish that a particular unit was configured or measured as described. The native ambiguities remain recorded, not repaired.

<a id="dragino"></a>
## 4. Dragino S31-LB

**Reference subject:** the primary-battery node with an external three-metre SHT31 probe, excluding the integrated-probe S31B and solar LS construction. The original history bytes are preserved; their numerical/UTC expansion is Derived. Complete original FPort-2 measurement/alarm and FPort-5 status replies were not acquired. [Context][c-identity]; [source key][c-sources].

| Exact sheet inputs and source | Available information and evidence | Candidate connection and why | Disposition and unresolved gap |
| --- | --- | --- | --- |
| [C-I01/I15–I17][c-identity]; [C-F07][c-sampling]; [C-S01–S04][c-status]. C01–C03. | Model is Design; `Node_type = S31-LB` is hard-coded decoder text. Regional/version field definitions and scalar examples are not captured settings; no device EUI acquired. | F-01/F-02/F-05: product name, decoder revision, message label and physical-unit identity have different roles. | **Supported distinction.** No installed region/version, authenticated EUI, or model-to-unit join. C-G01/G05; synthetic branch values remain separate. |
| [C-I02/I03][c-probe]; [C-F05/F06][c-sampling]; [C-H02/H03][c-history-fields]. C02/C03. | One external SHT31 probe; temperature °C and relative humidity % RH fields. Design plus scalar examples; history values separately supplied. | F-04/G03: physical probe and two reported quantities are not two physical identities or automatically two separately managed Systems. | **Supported distinction; proposed channel/part relationships.** No chip-to-IEEE-channel or output-to-CSAPI-stream equivalence; no gateway automatically made a node constituent. |
| [C-I07–I11][c-performance]. C02 §1.3. | Operating/range/resolution/accuracy statements are Design. Printed temperature accuracy interval exceeds the printed measurement range; humidity specification resolution and payload scaling differ. | F-02 separates specification from individual performance; G03 retains quantity/measurement scope. | **Hold reconciliation of conflicting specifications; proposed performance treatment.** No observed accuracy, corrected manufacturer range, or calibration certificate. C-G07. |
| [C-E01–E08][c-history-example]; [C-H01–H08][c-history-fields]. C02 §2.5.4/C03. | First example entry expands to 56.6% RH, 27.2°C and epoch `1684899041` → `2023-05-24T03:30:41Z`. Original bytes are Example; values/UTC formatting Derived. Leading `00 00` is ignored. | F-03/REL-03 and F-05: an illustrative record and its decoding do not authenticate an occurrence. The date, values and source bytes must retain their distinct roles. | **Supported distinction; proposed typed/time representation.** No actual history, unique subject, firmware or location; ignored bytes are not a zero battery reading. The decoder's `DATALOG` string is not already a typed JSON array. |
| [C-C01/C-C03–C06][c-command-settings]; [C-T01–T04][c-thresholds]. C02. | `AT+TDC` example 60000 uses milliseconds; downlink `0100003C` uses seconds. Thresholds/settings replies are defined; zero disables a bound under stated rules. Design/Example. | F-03/G01/G02: allowed configuration, request form and reply structure do not establish applied settings or action success. | **Supported distinction; proposed configuration/command treatment.** No full original settings reply or execution record. Do not interpret a disabled threshold as an environmental zero. C-G02/G03. |
| [C-F04][c-sampling]; [C-C07/C-C08][c-input-output]. C02/C03. | `Door_status` is a CLOSE/OPEN decoder label for a general input. `AT+5VT` controls duration in milliseconds; it is not measured output voltage. Design/implementation. | F-04/F-05 distinguish the physical subject from convenience labels; G01/G03 keep state, setting and quantity separate. | **Supported distinction; detailed roles proposed.** No installed door contact or actual output state is established. A field name cannot supply missing equipment. |
| [C-I04–I06][c-battery-design]; [C-F01][c-sampling]; [C-S05][c-status]; [C-P05][c-power]. C02/C04. | 8,500 mAh is nameplate capacity; 2.5–3.6 V is supply range; 0x0B45 is a scalar voltage example. Voltage-to-capacity guidance is non-linear. Design/Example. | F-02/F-03 distinguish design/range/example from actual result; detailed electrical semantics extend beyond them. | **Supported distinction; quantity treatment open.** No actual battery/status record, percentage conversion, inferred runtime or adopted power architecture. |
| [C-O08–O11][c-runtime-rules]; [C-H04/H05/H07][c-history-fields]; [synthetic checks][c-synthetic]. C02/C03. | Datalog/time/acknowledgement rules are Design; decoder PNACKMD reads a bit, not queried configuration. No matching history has an 11-zero-byte marker. Earlier synthetic checking produced apparent zeros/1970 text. | F-03/F-05, G01/G05: protocol context, missing-data marker, decoder output and current setting are different claims. | **Supported distinction; proposed absence/time treatment.** No real 1970 observation, newly executed test, source-clock accuracy or guaranteed delivery. C-G03/G07. |
| [C-C12–C18][c-calibration]; [C-O12][c-servicing]. C02. | Calibration commands include integer tenths °C/% RH; time sync/polling requests and firmware-servicing methods are documented. No commands sent. Design/Example. | F-03 and G02/G03 distinguish available procedure, calibration metadata and actual execution/result. | **Supported distinction; detailed calibration/action representation proposed.** No applied coefficients, maintenance event, successful update or completed calibration. C-G03/G05/G07. |

**What this case can exercise:** whether hardware/output distinctions, native encodings, source time, configuration definitions and absence markers survive interpretation. The retained eight-entry example is inspectable, but it is not an authenticated eight-event operating history.

<a id="campbell"></a>
## 5. Campbell CR1000X and first-generation ClimaVue 50

**Three evidence groups must remain separate:** the documented logger/sensor arrangement; the sensor interface definitions; and the original logger-status example. The latter does not establish an attached ClimaVue or output from the historical program. [Context][d-identity]; [status envelope][d-envelope]; [source key][d-sources].

| Exact sheet inputs and source | Available information and evidence | Candidate connection and why | Disposition and unresolved gap |
| --- | --- | --- | --- |
| [D-I01–I03/I17][d-identity]; [D-V01][d-verification]; [D-E04][d-envelope]; [D-X24][d-extra-identity]. D02/D05–D07. | Model pairing is Design; sensor identification string is a pattern; `loggerID = ABCD-EFGH-1234` is an Example; SerialNumber has a numeric definition but no value. | F-01/F-02/F-05 distinguish kind, pattern, record identity and individual. | **Supported distinction.** No authenticated station, sensor/logger serial join, installed support inventory or release combination. D-G01/G05. |
| [D-I02/I05–I10][d-identity]; [D-R01–R14][d-response]. D02–D04. | One sensing assembly plus cable; SDI-12 signal and address/terminal choices. Fourteen numeric response positions have definitions, not actual values. | F-04/G03/G04 distinguish assembly, interface address, output structure and independent System standing. | **Supported distinction; relationship treatment proposed.** No fourteen physical Systems, inferred permanence from the cable, or demonstrated instance-level subsystem/stream mapping. |
| [D-R08/R12][d-response]; [D-S01/D-S02][d-status]; [D-V04/V05][d-verification]. D02/D06/D07. | Air and humidity-sensor temperature definitions have no values. `PanelTemp = 25.91098` °C and `WatchdogErrors = 0` are logger Examples. Sensor watchdog/uptime are definitions only. | F-04/F-05 require the subject of each assertion; G03 prevents a common quantity/name from erasing component scope. | **Supported distinction; subject-qualified representation proposed.** No logger-to-sensor value transfer; zero logger watchdog errors is not lifetime fault-free or station readiness. |
| [D-R10/D-R11 and response footnotes][d-response]; [D-C01/D-C02][d-processing]. D02/D04. | Absolute pressure uses kPa; relative humidity uses fraction 0–1, not percent. Program description adjusts pressure with assumed elevation and may carry forward wind values. Design; actual values absent. | F-03/REL-06 and F-05 distinguish method, processing and source result; G03 retains quantity/time scope. | **Proposed processing/freshness treatment.** No numerical conversion, adjustment execution, new wind observation or conflation of absolute and sea-level pressure. D-G02/G04/G05. |
| [D-I09–I14][d-program]; [D-C03–C05][d-processing]; [D-S06][d-status]. D03/D04/D07. | Historical example uses C1/address 0/60-second scan; separate 2021 package was not obtained. `CompileResults` belongs to the independent status example. Design/Example/Unknown transcription correctness. | F-03/F-05 distinguish documented method/example program, package/version and actual execution evidence. | **Supported distinction; hold executable/version join.** No assertion the program ran, compiled successfully, or produced the status example. D-G04; no repair of `Cont SeaLevelAdj...` transcription. |
| [D-E01–E06][d-envelope]; [D-C06/D-C07][d-processing]. D07–D09. | `type = Feature` is representation text; coordinate array is `[0.0,0.0,0.0]`; example time is `2025-06-04T18:29:23.271Z`; 31 names pair positionally with values. Topic is a pattern. | F-05/REL-09/10 separate record form/address and equipment identity; F-03 does not turn an example time into an event. | **Supported distinction; schema/time binding proposed.** No real location, topic-to-sensor identity join, actual publication interval or new transformation test. Preserve positional association, not independent sorting. |
| [D-S03/D-S04/D-S30/D-S31][d-status]. D06/D07. | `Battery = 13.2368` Vdc at logger supply; `LithiumBattery = 3.70477` V internally; both `SW12Volts` values are Boolean true. Example. | F-04/F-05 and G03 distinguish subject, type and quantity. | **Supported distinction; detailed quantity/state treatment proposed.** Do not relabel a Boolean as voltage, attribute supply voltage to the attached sensor, or create a capacity/health assessment. |
| [D-S05/S08–S12/S14/S16–S21][d-status]. D06/D07. | Thirteen fields have literal values/types but held definitions/units/reset semantics. `CardStatus = "Card OK."` remains source text. Example with unresolved meaning. | F-05 permits retaining source text; it supplies no missing detailed definition. No invented donor equivalence. | **Hold interpretation.** D-G03 is an equipment/source meaning gap; do not silently infer counts, microseconds, readiness or enum meaning from familiar names. |
| [D-X01–X29][d-additional]; [D-V06–V08][d-verification]. D02/D06. | Additional logger definitions have no example values. `FullMemReset` documents control input 98765; `MeasureTime` is compile-time calculation; `StartUpCode` has codes but no event; sensor commands are supported only. Design. | F-03/G01/G02 separate definition, input, calculated characteristic and actual report/action. G03 retains calibration/metadata scope. | **Supported distinctions; full catalog mapping deferred.** No reset sent, active configuration, calibration record, start-up event or command result. Missing values do not imply unsupported features. |

**What this case can exercise:** component-scoped attribution, definition versus value, method-dependent meaning, positional message structure and unknown fields. It cannot exercise a joined station history until applicable logger, sensor, configuration/program and record evidence are available.

<a id="coverage"></a>
## 6. Coverage — what was compared and what remains locatable

This is **section-level accounting, not a claim of every-field transformation**. Selected rows above demonstrate the links and gaps; unselected rows remain in the unchanged sheets. Source IDs such as A02, C02 and D07 resolve through their sheet source keys. Row links target the sheet's source lines; the exact input revision and blob identities are retained in §8.

| Sheet sections and named inventory | Treatment in this iteration | Material not fully mapped or resolved |
| --- | --- | --- |
| AirGradient §1: A-I01–I16 | Identity, model, module/capability and service context compared in §3. | Housing/mounting details and every engineering characteristic do not acquire a complete common schema. |
| AirGradient §2: A-P01–P07, A-C01–C13, A-M01–M04, A-L01–L13 | Representative design, choice/request, timing/path, indicator and quantity distinctions. | Full electrical arrangement, configuration catalog and indicator/state model; P07 electronics-name discrepancy remains unresolved. |
| AirGradient §3: A-F01–F18 | Examples, raw/scaled values, missing absolute time and signal ambiguities remain separate. | No exhaustive property vocabulary, physical-channel attribution or result-schema mapping. |
| AirGradient §4: A-API01–API43 | Identity/nulls, time, numeric/string types, processing labels and service scope compared. | Place/contributor metadata, other cloud quantities and all cross-path correspondences are not fully bound; W and L are not merged. |
| AirGradient §§5–8 | Prior power shortlist is historical navigation; A-G01–G08, preservation and source keys remain controlling. | No new priority from §5; no source archive, firmware re-audit or repair of held material. |
| Dragino §1: C-I01–I17; §2: C-P01–P05, C-O01–O12 | Product/probe, specifications, operating rules, source revision and absent installation evidence compared. | Complete radio/network, hardware/service and performance treatments remain undeveloped. |
| Dragino §3: C-F01–F07, C-T01–T04, C-H01–H08, C-S01–S05 | Measurement/settings/history/status roles and selected types/flags examined. | No original complete FPort-2/5 packets, full band dictionary mapping or universal alarm/state model. |
| Dragino §4: C-E01–E08; §5: C-C01–C18 | Example/derived history and representative commands/units mapped to distinctions. | Eight entries are not acquired actual history; no command lifecycle or complete settings schema was implemented. |
| Dragino §§6–9 | Synthetic checks, historical power navigation, C-G01–G08 and sources remain distinct. | No new tests, firmware acquisition, source-clock proof or decoder redistribution decision. |
| Campbell §1: D-I01–I17; §2: D-R01–R14 | Reference pairing, support/connection, identity and output-definition scope examined. | Weather values, independently identified internal components and a complete support inventory remain absent. Extra `aC!` definitions in §2 prose are not additional observations. |
| Campbell §3: D-V01–V08; §4: D-C01–C07 | Sensor identity/diagnostic/control definitions and processing/publication context compared. | No sensor replies, executable verified program, selected address, command result or installed version. |
| Campbell §5: D-E01–E06, D-S01–S31 | Envelope and representative logger values; all thirteen interpretation holds are carried forward. | Remaining diagnostics/memory/timing/port fields are retained but not exhaustively bound. No joined sensor/status/weather dataset. |
| Campbell §6: D-X01–X29; §§7–9 | Additional no-value definitions, historical power navigation, D-G01–G08 and sources remain visible. | No fabricated values, general control/maintenance/calibration model or original-byte source archive. |

The [three sheet indexes and source keys][sheet-index] remain the detailed inventories. The selected cases do not define the full scope of the eventual DIM. Raspberry Shake & Boom remains outside this comparison's three primary cases, with its conditional audit unchanged.

<a id="gaps"></a>
## 7. What kind of missing work does each gap represent?

| Gap category | Concrete evidence in these sheets | Consequence for this comparison |
| --- | --- | --- |
| **Equipment/source: individual identity and applicable configuration** | A-I16/A-G01, C-G01, D-G01/D-G05; illustrative serials/IDs and absent sensor replies. | Kind/reference descriptions can be compared, but no real cross-source individual or installation link is asserted. Donor selection cannot manufacture those missing facts. |
| **Equipment/source: meaning or applicability unresolved** | A-G04–G06, C-I09/C-I10 and C-G05, D-G03/D-G04. | Hold the particular interpretation or source reconciliation. General domain knowledge must not silently supply native units, code meanings or version equivalence. |
| **Equipment/source: actual history and executed outcomes** | A-G02/G03, C-G02/G03, D-G02/G05/G07. | Published examples and supported commands remain useful documentary inputs, not a joined operating-state or action-history test. |
| **Model: declarations, settings, requests and results** | A-C06/C08; C-C01–C18 and absent C-T replies; D-V06–V08/D-X08. | F-03 explains why claims differ; G01/G02 do not yet provide their complete definitions/relationships. Do not fill the gap with a generic Condition or Command class. |
| **Model: physical realization, channel and technical-description scope** | A-I06–I10/A-F01–F18; C-I02/C-F05–F06; D-I02/D-R01–R14. | F-04 prevents simple conflation; G03/G04 still need a developed treatment for scoped technical information and relationships. No exact device-to-donor channel mapping is established. |
| **Model: processing, time, mediation and assertions** | A-C10–C12/A-API16/24; C-H05/C-H07 and synthetic absence check; D-C01/C02/D-E06. | F-05 supports preserving context; exact provenance, freshness, source authority and derived-result relationships remain incomplete. |
| **Donor review: potentially useful material not yet comparably integrated** | The [donor coverage page](Donor_Contributions.md) records partial PA-DIM, broader SAREF/OSUS-R, preliminary I-ADOPT, W3C PROV, Redfish/CIM, MIMOSA and other leads. | These are coverage leads, not newly verified matches to a device field or a ranked queue. Their relevance and depth need explicit justification before adoption; existing five headings cannot exclude them. |

**A connected example of the reasoning:** Campbell supplies one attached sensing assembly, fourteen response positions, an absolute-pressure definition and a separate description of pressure adjustment. The current foundation helps distinguish physical equipment, output and processing. It does not provide an actual sensor response, applicable site elevation or executed program, and it does not yet finish the common quantity/processing model. Both the source-data gap and the model gap survive; neither cancels the other. [D-I02][d-identity], [D-R01–R14][d-response], [D-C01–C05][d-processing].

These comparisons make several future questions concrete. They do **not** select a winning next subject, conclude that power comes first, or reopen dataset acquisition. Comparison of next-step alternatives belongs to Iteration 4.

<a id="verification"></a>
## 8. Inputs, checks and stopping point

| Input sheet at the snapshot | Git blob identity |
| --- | --- |
| AirGradient Open Air Max v0.1 | `f5c87b5886d15e995e8c55bc28b8666e97a1b537` |
| Dragino S31-LB v0.1 | `8f34b2eef07964aa500273eba4a5950f52647c60` |
| Campbell CR1000X/ClimaVue 50 v0.1 | `60ae8242ae50fa967eeb6979c491fd613285d08a` |

The complete local sheets were read and their Git blob hashes checked against the repository input snapshot. All numbered sheet sections are accounted for above. Row identifiers, cited line ranges, local comparison anchors and Markdown table structure were checked. This is an extraction/link/interpretation check of the existing evidence, not a fresh primary-standard or manufacturer-source audit; no vendor API was called, no device command was issued, and the existing example checkers were not rerun.

No source sheet, audit, frozen evidence record, candidate DIM manuscript, Profile or application was modified. No numerical example was promoted into actual telemetry, no donor-conformance result was produced, and no source-to-CSAPI conversion was implemented. REL-05/07/08 can inform cautions, but no real deployment lifetime, hosting history or recursive API discovery record was acquired or mapped here.

**Next separate “proceed”: Iteration 4 only — verify the three connected comparison pages against their existing evidence, assess readability and omissions, and recommend the next substantive task from the exposed gaps.** Final verification is still pending. The [plan](../PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) records 3/4 complete after this iteration; no next domain study or dataset campaign is automatically authorized.

[a-identity]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L3-L34
[a-cloud-identity]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L151-L162
[a-components]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L22-L31
[a-co2-design]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L24-L24
[a-co2-example]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L99-L99
[a-settings]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L49-L55
[a-timing-readme]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L56-L56
[a-modes]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L63-L72
[a-device-signals]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L105-L115
[a-cloud-signals]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L143-L169
[a-paths]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L57-L59
[a-device-context]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L93-L119
[a-cloud-time]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L142-L150
[a-voltage-device]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L109-L110
[a-voltage-cloud]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L163-L164
[a-leds]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L74-L91
[a-location-service]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L127-L132
[a-sources]: ../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md#L195-L211
[c-identity]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L3-L35
[c-sampling]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L61-L75
[c-status]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L103-L110
[c-probe]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L19-L20
[c-history-fields]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L86-L100
[c-performance]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L24-L28
[c-history-example]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L112-L127
[c-command-settings]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L135-L140
[c-thresholds]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L76-L85
[c-input-output]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L141-L142
[c-battery-design]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L21-L23
[c-power]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L40-L44
[c-runtime-rules]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L52-L55
[c-synthetic]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L154-L156
[c-calibration]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L146-L152
[c-servicing]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L56-L56
[c-sources]: ../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#L175-L185
[d-identity]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L3-L36
[d-verification]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L59-L74
[d-envelope]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L89-L102
[d-extra-identity]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L172-L172
[d-response]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L37-L57
[d-status]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L103-L140
[d-processing]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L76-L87
[d-program]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L26-L31
[d-additional]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L143-L178
[d-sources]: ../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md#L197-L210
[sheet-index]: ../Controlled_Corpus/System_Data_Sheets/README.md
