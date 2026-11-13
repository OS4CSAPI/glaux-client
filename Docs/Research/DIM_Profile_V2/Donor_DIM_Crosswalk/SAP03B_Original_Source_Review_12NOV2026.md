# SAP-03B — original SAPIENT Registration Tables 33–59 and pinned native definitions

**Owner-authorized original-source packet: SAP-03B ONLY, 12 November 2026.** This review directly inspected the original British Standards Institution (BSI) [Flex 335 v2.0:2024-03](https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf), **§§6.2.5.16–6.2.5.41, PDF pages 49–63, numbered Tables 33–59 (27)** at original clause, table, source-standing and native field/enum depth. Matched to the pinned Defence Science and Technology Laboratory (Dstl) [registration.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/registration.proto), [follow.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/follow.proto), scoped [task.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/task.proto) RegionType/Task.Command and the earlier [velocity.proto](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/velocity.proto) SpeedUnits definitions. **Native version frozen at commit `244a741c13bcee628f84944aef91e4a66854bd7d`.** Full Task/DetectionReport messages, BSI §6.3 and later and protobuf compilation are **not** claimed audited here.

## What the original source actually teaches us

Registration describes what a Node **can support**, not what it has just done. DetectionDefinition can declare geometry, errors, object/track/signal fields, taxonomic classes, behaviours, velocity format and confidence reporting without establishing an actual DetectionReport. Likewise TaskDefinition declares accepted region types, class/behaviour filters, task concurrency and commands without proving a Task message was sent, accepted or physically executed.

Three different ideas must remain separate: **the category of a detected object**, **the sensing equipment**, and **the operational role of the network Node**. The recursive ClassDefinition/SubClass and namespaced taxonomy extension structures apply to detected object classes, not to manufacturer hardware or a mandatory generic DIM class hierarchy. The presence of a source-defined GO/NO_GO task RegionType is not evidence of the station's current configured zones.

Tables 57–59 distinguish sensor versus effector REQUEST semantics and the supported MOVE_TO, LOOK_AT, PATROL and FOLLOW task variants. The follow target is an **object identifier from detection content**, not the Node's equipment identifier, and Table59 covers a single target while explicitly reserving multi-object guidance for a future version. Registering a supported control interface cannot authorize physical command execution in OGC API – Connected Systems (CSAPI).

## Audited original numbered-table register — not a heading-contact claim

| BSI source ID | Original section | PDF page | Standing | Source meaning (native) |
| --- | --- | --- | --- | --- |
| SAP-BSI-T033 | §6.2.5.16 | 49 | SCOPED_SHALL | DetectionDefinition structure and declared location/performance/classes/behaviour/velocity/error |
| SAP-BSI-T034 | §6.2.5.17 | 50 | SCOPED_SHALL | GeometricError descriptors, SI units and variation |
| SAP-BSI-T035 | §6.2.5.18 | 50 | SCOPED_SHALL | Registration-side DetectionReport declared category/type/units/on_change |
| SAP-BSI-T036 | §6.2.5.19 | 51 | SCOPED_SHALL | DetectionReportCategory enum: DETECTION/TRACK/OBJECT/SIGNAL |
| SAP-BSI-T037 | §6.2.5.20 | 51 | SCOPED_SHALL | TrackObjectInfo and object information named fields/units correspondence |
| SAP-BSI-T038 | §6.2.5.21 | 52 | SCOPED_SHALL | DetectionClassDefinition confidence/performance/taxonomy docks |
| SAP-BSI-T039 | §6.2.5.22 | 52 | SCOPED_SHALL | ConfidenceDefinition enum SINGLE_CLASS/MULTI_CLASS |
| SAP-BSI-T040 | §6.2.5.23 | 53 | CONDITIONAL_SHALL_IF_AVAILABLE | PerformanceValue type/units/typical unit_value/variation |
| SAP-BSI-T041 | §6.2.5.24 | 53 | SCOPED_SHALL | ClassDefinition and mutually exclusive class taxonomy standing |
| SAP-BSI-T042 | §6.2.5.25 | 54 | SCOPED_SHALL | Recursive SubClass type/units/level |
| SAP-BSI-T043 | §6.2.5.26 | 54 | SCOPED_SHALL_AND_COMMENTARY | TaxonomyDockDefinition class namespaces and dock into existing class |
| SAP-BSI-T044 | §6.2.5.27 | 55 | SCOPED_SHALL_AND_COMMENTARY | ExtensionSubclass namespace/name/units with unique combination |
| SAP-BSI-T045 | §6.2.5.28 | 55 | SCOPED_SHALL | BehaviourDefinition type and confidence units |
| SAP-BSI-T046 | §6.2.5.29 | 56 | SCOPED_SHALL_AND_COMMENTARY | VelocityType ENU coordinate and datum selectors |
| SAP-BSI-T047 | §6.2.5.30 | 56 | SCOPED_SHALL | ENUVelocityUnits East/North and Up SpeedUnits |
| SAP-BSI-T048 | §6.2.5.31 | 56 | SCOPED_SHALL | SpeedUnits enum unspecified, m/s, km/h |
| SAP-BSI-T049 | §6.2.5.32 | 57 | SCOPED_SHALL | TaskDefinition concurrency/region/command declarations |
| SAP-BSI-T050 | §6.2.5.33 | 57 | SCOPED_SHALL | RegionDefinition region types/coordinates/settle/filter support |
| SAP-BSI-T051 | §6.2.5.33 | 58 | SCOPED_SHALL | RegionType enumerations incl mobile go/no-go |
| SAP-BSI-T052 | §6.2.5.34 | 58 | SCOPED_SHALL | ClassFilterDefinition parameters/subclasses/class type |
| SAP-BSI-T053 | §6.2.5.35 | 59 | SCOPED_SHALL | FilterParameter name/operators |
| SAP-BSI-T054 | §6.2.5.36 | 59 | SCOPED_SHALL | Operator enumeration ALL/GREATER/LESS/EQUAL |
| SAP-BSI-T055 | §6.2.5.37 | 59 | SCOPED_SHALL | SubClassFilterDefinition recursive level/type/filters |
| SAP-BSI-T056 | §6.2.5.38 | 60 | SCOPED_SHALL | BehaviourFilterDefinition type and filter parameters |
| SAP-BSI-T057 | §6.2.5.39 | 60 | SCOPED_SHALL_AND_NOTE | Command declaration units/completion_time/type; removed name |
| SAP-BSI-T058 | §6.2.5.40 | 61–62 | SCOPED_SHALL_AND_NOTES_AND_FUTURE | CommandType sensor/effector REQUEST, thresholds, mode, LOOK_AT/MOVE_TO/PATROL/FOLLOW |
| SAP-BSI-T059 | §6.2.5.41 | 63 | SCOPED_SHALL_AND_FUTURE_NOTE | FollowObject target detection object_id; one-object limit |

These are **27 original table-level readings**, not 27 source documents or a complete audit of all SAPIENT Rules, schemas, source graphics, illustrative annexes or external integrations. With SAP-02's fourteen and SAP-03A's eighteen, **59 of 97** numbered BSI main tables now have specific, relevant-content original inspection. The other 38 main tables, Annex C.1, parts of the source clauses/figures and companion/runtime obligations retain their own source grades.

## Source-qualified meaning findings (stable IDs)

| ID | Inspected native tables | Standing | Meaning and negative-equivalence boundary |
| --- | --- | --- | --- |
| SAP03B-N01 | T33, T34, T35 | SCOPED_SHALL | Detection registration declares schema, location error and outputs, not performed observations |
| SAP03B-N02 | T36, T37 | SCOPED_SHALL | Declared report categories DETECTION/TRACK/OBJECT/SIGNAL and named object/track fields are not actual observations |
| SAP03B-N03 | T38, T39 | SCOPED_SHALL | Class confidence definition states whether most-likely or multiple class confidences can be supplied; not validated classification accuracy |
| SAP03B-N04 | T40 | CONDITIONAL_SHALL_IF_AVAILABLE | PerformanceValue has type, units, typical value and variation; not a direct measured sample or guaranteed detection range |
| SAP03B-N05 | T41, T42 | SCOPED_SHALL | Class/subclass hierarchy and level describe detectable target classifications, not physical sensors or equipment parts |
| SAP03B-N06 | T43, T44 | SCOPED_SHALL_AND_COMMENTARY | Taxonomy dock classes with scoped namespaces and extensible subclasses; source of object-class extension, not mandatory DIM class hierarchy |
| SAP03B-N07 | T45 | SCOPED_SHALL | Behaviour type/units define detectable target behaviour taxonomy, not an operated device state |
| SAP03B-N08 | T46, T47, T48 | SCOPED_SHALL | Velocity type declares East/North/Up format, datum and SpeedUnits, not actual physical platform velocity or a performed reading |
| SAP03B-N09 | T49 | SCOPED_SHALL | TaskDefinition declares concurrent task count, region definition and command repertoire, not a transmitted Task or completed effect |
| SAP03B-N10 | T50, T51 | SCOPED_SHALL | RegionType advertises area of interest, ignore, boundary, mobile go/no-go with accepted coordinate systems; not a currently applied exclusion-zone state |
| SAP03B-N11 | T52, T53, T54, T55, T56 | SCOPED_SHALL | Class/subclass/behaviour filters and ALL/GT/LT/EQ operators declare acceptable filtering patterns, not processed sensor results |
| SAP03B-N12 | T57 | SCOPED_SHALL_AND_NOTE | Command declarations have units, completion time and type; legacy name field is removed/reserved in source |
| SAP03B-N13 | T58 | SCOPED_SHALL_AND_NOTES | Supported commands are scoped differently for sensor and effector Nodes; REQUEST, thresholds, MODE_CHANGE, LOOK_AT, MOVE_TO, PATROL and FOLLOW not executed by registration |
| SAP03B-N14 | T58, T59 | SCOPED_SHALL_AND_FUTURE_NOTE | LOOK_AT location vs MOVE_TO/PATROL route and FOLLOW detected-object ULID are different tasking semantics; single-target follow limit is source-local |
| SAP03B-N15 | T51, T58 | NATIVE_SCHEMA_AND_SCOPED_RULE | The six RegionType enum values match in pinned registration.proto and task.proto; CommandType enum codes must not be confused with Task.Command oneof wire tags |
| SAP03B-N16 | T43 | CROSS_ARTIFACT_REQUIREDNESS_CONFLICT | BSI Table43 discretionary Dock_class_namespace with omitted default 'sapient_core' versus pinned registration.proto field is_mandatory=true; mismatch held |
| SAP03B-N17 | T49, T55 | CROSS_ARTIFACT_REQUIREDNESS_DISCREPANCY | BSI mandatory concurrent_tasks and subclass filter level versus pinned registration.proto optional fields without is_mandatory annotations; semantics held |
| SAP03B-N18 | T33 | CROSS_ARTIFACT_TYPE_NAME_DIFFERENCE | BSI Table33 labels DetectionPerformance type but pinned registration.proto uses repeated PerformanceValue; exact type naming mismatch held |
| SAP03B-N19 | T58, T59 | NATIVE_ENCODING_SCOPE_AND_VALIDATION_HOLD | Table58 'Protobuf Field Serial' 7–9 aligns CommandType enum, not the Task.Command oneof MOVE_TO/PATROL/FOLLOW tags9/10/11; Table59 follow_object_id ULID requirement lacks proto is_ulid annotation |

**Additional original-source holds, not fabricated fixes:**

- **SAP03B-H01** (CROSS_ARTIFACT_REQUIREDNESS; SAP-BSI-T043): BSI Table43 treats Dock_class_namespace as discretionary with source-defined sapient_core default, but pinned registration.proto annotates field with is_mandatory:true; no silent reconciliation.
- **SAP03B-H02** (CROSS_ARTIFACT_REQUIREDNESS; SAP-BSI-T049;SAP-BSI-T055): BSI Table49 marks concurrent_tasks M and Table55 marks level M; pinned registration.proto represents both as optional without is_mandatory:true. BSI M/D/C must not be conflated with protobuf syntax or code annotations.
- **SAP03B-H03** (CROSS_ARTIFACT_TYPE_NAMING; SAP-BSI-T033): BSI Table33 labels detection_performance as DetectionPerformance, pinned registration.proto uses repeated PerformanceValue; Table40 describes its source type, but do not assert same wire-level type name.
- **SAP03B-H04** (ENCODING_LAYER_AMBIGUITY; SAP-BSI-T058): BSI Table58 prints CommandType values 7,8,9 under 'Protobuf Field Serial' for MOVE_TO/PATROL/FOLLOW; pinned Task.Command oneof uses field tags 9,10,11. They are separate layers; do not build a converter by treating enum code as field number.
- **SAP03B-H05** (VALIDATION_ANNOTATION_SCOPE; SAP-BSI-T059): BSI Table59 calls FollowObject.follow_object_id an object ULID; pinned follow.proto uses string is_mandatory:true but no is_ulid annotation. Absence of annotation is not proof source ULID rule is false.

The matched original `RegionType` enumerations in pinned `registration.proto` and `task.proto` have the **same six values (0–5)**; that is a genuine scoped corroboration, not an execution or registration-to-task equivalence proof. Table58's label **“Protobuf Field Serial”** must not be used to assign the actual transmitted Task.Command `move_to`, `patrol` or `follow` tags. Retain the previously held BSI Registration `config_data` tag 9 vs protobuf tag10, Duration tag2 vs tag3, and all prior SAPIENT source issues without converting them into DIM Profile requirements.

## Master comparison and exact next owner boundary

**Proposed source-qualified increment:** 28 existing-row SAPIENT column G comparisons; each includes its stable source IDs, relation grade and negative equivalence. No new row, donor column, hierarchy, class or proposed DIM adoption is justified. Case facts, Integrated Sensor Architecture (ISA), The Open Group Sensor Open Systems Architecture (SOSA), other donors, the grouped Open Geospatial Consortium (OGC) foundations and DIM-rightmost text remain unchanged. The [same cumulative original-source and mapping ledger](SAP01_Original_Corpus_Coverage_12NOV2026.json) is authoritative for these findings and their format-publication state.

**The same original editable Excel workbook must be refreshed and its saved 346×15 grid verified** against canonical JSON, both CSV mirrors and both readable Markdown comparisons before declaring this step's cross-format exit complete. The exact pre-step version is preserved [here](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sap03b-20261112/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk) at `6309f83ccb1ede9ba284704ebf274c9b4a1db253`. The old 26 worksheets, provenance, original six ISA questions and nine owner-accepted bounded PARTIAL The Open Group SOSA holds, existing SAPIENT six+five+three issues and these five local holds must survive; a successful workbook test is **not** comprehensive source coverage.

**Forecast:** After SAP-01 low6 / likely7 / high9; SAP-02 5/6/8; SAP-03A 4/5/7; after SAP-03B **LOW 3 / MOST LIKELY 4 / HIGH 6 additional substantive Proceeds** for BSI Status/Detection, Task/Alert/Error, Taxonomy/Annexes and an owner-controlled evidence/disposition gate. Rebaseline only for actual original-source complexity or access and owner decision; do not auto-append packets. **NEXT single owner-controlled step: SAP-04 only**, BSI original §§6.3–6.4 Tables60–77 and pinned Status/Detection native sources, then STOP before SAP-05. No DIM/Profile classes/fields/cardinalities, GLaux client, commands, runtime or deployment adopted.
