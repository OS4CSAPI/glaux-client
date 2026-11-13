**FINAL CANONICAL/SAVED-EXCEL PUBLICATION READBACK PASS:** 40 original source-qualified SAPIENT column-G comparisons saved in canonical JSON, both CSV mirrors, both Markdown views and SAME original 26-sheet Excel; all 5190 saved values matched with zero lag. [Saved validation](SAP04_Workbook_Validation_12NOV2026.json). The source-audit proposal and publication-pending statements below are retained historical prepublication text.

# SAP-04 — original SAPIENT v2 Status and Detection messages, Tables 60–77

**12 November 2026 · Owner-authorized SAP-04 original-source packet, bounded to BSI §§6.3–6.4 and native Status/Detection companions.** Read original [British Standards Institution (BSI) Flex 335 v2.0:2024-03](https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf) **PDF pages 63–76, §§6.3.1–6.3.3 and 6.4.1–6.4.2.19, and all 18 numbered Tables 60–77** at actual clause, table, source standing and field/enum depth. Selected original table images (Table60, both pages of Table69, Table77) were inspected in addition to extracted original content. Compared against original pinned Defence Science and Technology Laboratory (Dstl) source [status_report.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/status_report.proto) and [detection_report.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/detection_report.proto), with bounded reuse of associated media/derived-report companions. This step **did not** inspect §6.5 Task and later sections, execute protobuf compilation, test physical equipment or declare SAPIENT donor completeness.

## Plain-English meaning for the whole-sensing-system DIM/CSAPI research

SAPIENT **StatusReport** separates an operational heartbeat from individual current-state claims. A Node reports a source-status code, information-newness flag, selected mode, optional active task, power source and battery percentage, current location, field of view, broader coverage, obscured areas and scoped status conditions. These do not all share the same reporting obligation or interpretation: a missed heartbeat is not a measured physical failure, coverage is not the portion currently in view, a reported GOODBYE differs from network-link truth, and battery level is not voltage, measured capacity or time-to-empty. The registered interval remains a communications obligation, not a DIM health-state rule.

SAPIENT **DetectionReport** separately identifies the reporting network Node, report ULID, detected object ULID, optional task reference, reported target location/velocity, optional prediction, class/behaviour confidence, media, detected signals and linked source/fused reports. An object identifier may change for every detection if the Node cannot associate tracks; reporting a track or predicted position does not establish the actual original observing instrument or an independently performed Open Geospatial Consortium (OGC) Observation. DerivedDetection/AssociatedDetection links are traceable *report references*, not a complete cryptographically authenticated scientific provenance chain.

SAPIENT's object taxonomy, SAPIENT Node operating status, physical equipment and an optional Glaux Details-view concept are **four different subjects**; keep their different identities and source grades rather than invent a mandatory class hierarchy. No Domain Information Model (DIM) class, field/cardinality or OGC API – Connected Systems (CSAPI) Profile SHALL is adopted by this donor comparison.

## All 18 native BSI main tables actually inspected

| Stable source ID | Original BSI section | PDF page | Original content and normative distinction |
|---|---|---|---|
| SAP-BSI-T060 | §6.3.2.1 | 64 | StatusReport wrapper: report_id, system, info, task_id, mode, power, location, field_of_view, coverage, obscuration, status |
| SAP-BSI-T061 | §6.3.2.2 | 65 | StatusReport System: UNSPECIFIED/OK/WARNING/ERROR/GOODBYE |
| SAP-BSI-T062 | §6.3.2.3 | 65 | StatusReport Info: UNSPECIFIED/NEW/UNCHANGED |
| SAP-BSI-T063 | §6.3.2.5 | 66 | Power level battery percentage, current source and supply status |
| SAP-BSI-T064 | §6.3.2.5 | 66 | PowerSource MAINS/INTERNAL_BATTERY/EXTERNAL_BATTERY/GENERATOR/SOLAR_PV/WIND_TURBINE/FUEL_CELL |
| SAP-BSI-T065 | §6.3.2.5 | 67 | PowerStatus UNSPECIFIED/OK/FAULT |
| SAP-BSI-T066 | §6.3.2.10 | 68 | Status condition level/type/value and task-related transition/stop meanings |
| SAP-BSI-T067 | §6.3.2.11 | 68 | StatusLevel INFORMATION/WARNING/ERROR severity; former enum1 deprecated |
| SAP-BSI-T068 | §6.3.2.12 | 69 | StatusType: internal/external faults, illumination, weather, clutter, exposure, PTZ, platform, other |
| SAP-BSI-T069 | §6.4.1 | 70–71 | DetectionReport: separate report/object/task IDs, location/confidence, track, prediction, classification, media, signal, provenance and velocity |
| SAP-BSI-T070 | §6.4.2.8 | 72 | PredictedLocation oneof and optional predicted_timestamp |
| SAP-BSI-T071 | §6.4.2.9 | 73 | TrackObjectInfo name/value/error |
| SAP-BSI-T072 | §6.4.2.12 | 73 | DetectionReportClassification type with namespace, confidence and subclasses |
| SAP-BSI-T073 | §6.4.2.13 | 74 | Nested SubClass type with namespace, confidence, level and sub_class |
| SAP-BSI-T074 | §6.4.2.14 | 74 | Behaviour type and confidence |
| SAP-BSI-T075 | §6.4.2.15 | 75 | AssociatedFile type and URL |
| SAP-BSI-T076 | §6.4.2.16 | 75 | Signal amplitude, frequency endpoints/centre, pulse duration |
| SAP-BSI-T077 | §6.4.2.19 | 76 | DerivedDetection time, fusion node and object identifier from linked original/fused report |

This is **18 substantive table-depth inspections, cumulative 77 of 97 numbered BSI main tables** since SAP-02. A full original corpus audit or comprehensive proto compilation **is not claimed**. BSI Tables78–97, informative annexes and other source limitations remain graded as such in the one [cumulative coverage ledger](SAP01_Original_Corpus_Coverage_12NOV2026.json).

## Source-qualified native meaning and Rule/Note standing

| Stable finding ID | Original source locator | Standing | Source meaning and limits |
|---|---|---|---|
| SAP04-N01 | §6.3.1/§6.3.2.1 original PDF63–64; T60,T62 | SCOPED_SHALL_AND_NOTE | Initial status follows RegistrationAck; regular heartbeat with Node UUID and timestamp; three missing registered intervals require fusion-side connection close. 1–60s suggestion is NOTE, not a mandatory universal rate. |
| SAP04-N02 | §§6.3.2.1–.3 PDF64–65; T60,T61,T62 | SCOPED_SHALL | StatusReport.report_id is a ULID and distinct from outer sender node_id UUID; System condition and Info NEW/UNCHANGED have separate meanings; an UNCHANGED report contains no new information. |
| SAP04-N03 | §§6.3.2.2, .10–.12 PDF65–69; T60,T61,T68 | SCOPED_SHALL | System OK/WARNING/ERROR/GOODBYE denotes source-reported Node state; detailed StatusType/Level denote scoped conditions. These are not verified physical condition or an ISA Operating State equivalence. |
| SAP04-N04 | §6.3.2.4 PDF65; T60,T62 | SCOPED_SHALL_AND_NOTE | Reported mode should match Registration; switching can take settle_time. Table60 labels mode M but §6.3.2.4 says it SHALL be included where multiple modes/states are provided. |
| SAP04-N05 | §6.3.2.5 PDF66–67; status_report.proto; T63,T64,T65 | SCOPED_SHALL | Power.level is optional remaining battery percentage 0–100; PowerSource enum identifies node's current supply type, and PowerStatus reports OK/FAULT. No sampled voltage/capacity/runtime or all installed sources. |
| SAP04-N06 | §§6.3.2.6–.9 PDF67; T60 | SCOPED_SHALL_AND_NOTE | node_location, field_of_view, coverage, obscuration have different geographic meanings. NEW without field_of_view means lost view; coverage may exceed instantaneous FOV and obscuration describes blind areas. |
| SAP04-N07 | §§6.3.2.10–.12 PDF68–69; status_report.proto; T66,T67,T68 | SCOPED_SHALL_AND_NOTE | Status level/value/type and enumerated environmental/platform conditions are scoped reports; paused/stopped task ≠ physical immobility; deprecated StatusLevel enum1 is not current. |
| SAP04-N08 | §6.3.3 PDF69; T68 | SCOPED_SHALL_AND_HISTORICAL_NOTE | One-off status messages SHALL NOT be used; earlier one-off status for alerts is replaced by Alert message, not a stream of StatusReport events. |
| SAP04-N09 | §§6.4.1–6.4.2.3 PDF69–71; detection_report.proto; T69 | SCOPED_SHALL | DetectionReport.report_id ULID identifies the report, object_id ULID identifies detected object (may be unique per detection if no tracking), task_id is task reference; outer node UUID identifies sender, not necessarily physical observer. |
| SAP04-N10 | §§6.4.1–6.4.2.6 PDF69–72; detection_report.proto; T69 | SCOPED_SHALL | Detection location oneof provides Location/RangeBearing; optional detection_confidence 0–1 describes node's reported existence confidence, not accuracy proof or OGC Observation conversion. |
| SAP04-N11 | §6.4.2.8 PDF72; detection_report.proto PredictedLocation; T69,T70 | SCOPED_SHALL | PredictedLocation is a future object position in Location/RangeBearing with optional predicted_timestamp; it is not a performed Observation or reliable future event. |
| SAP04-N12 | §6.4.2.9 PDF73; detection_report.proto TrackObjectInfo; T69,T71 | SCOPED_SHALL | TrackObjectInfo type/value/optional error records named metadata about reported track or object, not proof of continuous video track or general ISA Event detector properties. |
| SAP04-N13 | §§6.4.2.12–.14 PDF73–74; detection_report.proto; T69,T72,T73,T74 | SCOPED_SHALL_AND_NOTE | Object classification and nested subclass type use namespace:value with sapient_core default; optional confidence and behaviour report source assertions, not authenticated tactical identity or a physical equipment taxonomy. |
| SAP04-N14 | §6.4.2.15 PDF75; associated_file.proto; T69,T75 | SCOPED_SHALL | AssociatedFile type/URL references media; URL is not proof that retrieval succeeded or the media came from identified physical observing equipment. |
| SAP04-N15 | §6.4.2.16 PDF75; detection_report.proto Signal; T69,T76 | SCOPED_SHALL_AND_NOTE | Signal amplitude, start/centre/stop frequency and pulse duration concern detected signal attributes with typically used units, not actual network receive level, transmit power or a universal signal strength ratio. |
| SAP04-N16 | §6.4.2.19 PDF76; detection_report.proto DerivedDetection; T69,T77 | SCOPED_SHALL_AND_NOTE | DerivedDetection references fused results from original reports using timestamp, source node and object identity; linked AssociatedDetection gives reverse connections, not proof original measurement or full transformation lineage. |
| SAP04-N17 | §6.3.2.4 + Tables60/70/77 and pinned status_report.proto/detection_report.proto; T60,T70,T77 | SOURCE_CONFLICT_OR_VALIDATION_CEILING | Current mode M versus conditional mode text; PredictedLocation nested required oneof versus no is_mandatory annotation; DerivedDetection.timestamp M content time versus optional/send-time code comment are distinct source issues. |
| SAP04-N18 | §6.4.2.19/Table77, detection_report.proto; T77 | SOURCE_CONFLICT | BSI DerivedDetection.node_id is identity of fusion Node that sourced detection; pinned code comment calls it Node where associated detection originated. Neither is verified physical-sensor identity. |
| SAP04-N19 | §6.4.1/Table69/Table77, associated_detection.proto; T69,T77 | SOURCE_OBSERVATION_AND_LIMIT | Detected-object report linking permits fused data lineage with contributor IDs but does not automatically identify the original observing physical instrument, exact phenomenon time or an OMS provenance chain. |

## Exact unresolved holds — do not silently harmonize

- **SAP04-H01** (INTRA_BSI_CONDITIONALITY, SAP-BSI-T060): BSI Table60 labels StatusReport.mode M; §6.3.2.4 says mode SHALL be included where multiple modes or states are provided. Source text does not establish an unambiguous single-mode applicability rule; pinned status_report.proto sets is_mandatory=true.
- **SAP04-H02** (NATIVE_VALIDATION_ANNOTATION_SCOPE, SAP-BSI-T070): BSI Table70 marks the nested PredictedLocation.predicted_location_oneof M, yet pinned detection_report.proto PredictedLocation.oneof has no oneof_options is_mandatory annotation; an optional enclosing prediction_location is different from whether oneof contents must be present when included.
- **SAP04-H03** (PUBLISHED_REQUIREDNESS_AND_TIME_CONFLICT, SAP-BSI-T077): BSI Table77 marks DerivedDetection.timestamp mandatory and describes timestamp of associated detection; pinned detection_report.proto declares optional timestamp without is_mandatory and comments 'UTC timestamp the message was sent'. No silent equivalence to content/send/observed time.
- **SAP04-H04** (DERIVATION_SOURCE_IDENTITY_DIFFERENCE, SAP-BSI-T077): BSI Table77 describes DerivedDetection.node_id as fusion Node source of detection, while pinned DerivedDetection.node_id comment says Node where associated detection originated. The actual original physical observing instrument cannot be inferred from either alone.

Original earlier source conflicts **remain open**, including Registration config_data field9 vs pinned proto field10, Duration.value field2 vs proto3, angular units, identity/annotation and other precise earlier SAP-ISSUE/SAP02/SAP03A/SAP03B holds. An original normative SHALL, informative NOTE, code annotation and observed sensor installation are not interchangeable.

## Original-to-master contribution and justified boundary

The source ledger proposes **40 existing master-row comparisons in SAPIENT column G**, each with stable `row_id`, qualified relation and source IDs. These relate reported system health, power and view/coverage; observed-target report position/prediction/classification and signal details; and distinctions between native report, object, Node and fused source identities. In no case does a declared Native field become an approved universal DIM property, automatic OGC Observation, live command or mandatory Glaux client UI.

The evidence must be integrated into the existing canonical JSON, **both CSV mirrors, both GitHub-readable Markdown comparisons, and SAME original 26-sheet Excel** with actual **346×15 saved-value verification** before the cross-format exit is declared complete. The entire previous repository state is preserved in [pre-SAP04 archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sap04-20261112/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk) at `1b138f07ce3b6ce915127cb25c45912ad829e0a8`; previous ISA/SOSA/SAPIENT findings and case/DIM cells must remain intact. Source research coverage and workbook parity are different claims.

## Forecast and ONE next owner boundary

SAPIENT's prior forecast after SAP03B was low3 / most likely4 / high6 additional substantive Proceeds. This table/status/detection packet reduces the provisional remaining estimate to **LOW 2 / MOST LIKELY 3 / HIGH 5**, inclusive of SAP05 task/alert/error, SAP06 taxonomy and informative annexes, and SAP07 original-source/owner donor disposition. Exact source holds can justify changed scope only with owner notification and authorization; the count must not rush a false comprehensive audit or silently add more work.

**ONE NEXT separate owner `Proceed` = SAP05 ONLY**, BSI §§6.5–6.7 and Tables78–95 with original Task/TaskAck/Alert/Error companions, then STOP before SAP06 or any DIM/Profile/adoption/client/deployment work. No donor transition or model-owner decision occurs in SAP04.
