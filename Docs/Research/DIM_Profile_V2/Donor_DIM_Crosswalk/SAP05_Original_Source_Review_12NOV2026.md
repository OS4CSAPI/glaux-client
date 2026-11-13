**FINAL SAP05 CANONICAL/SAVED-EXCEL PUBLICATION PASS:** 42 source-qualified SAPIENT G-column comparisons in canonical JSON, BOTH CSV, BOTH Markdown and SAME original 26-sheet Excel. All 5190 saved grid values agree, with zero Excel lag and 42 other ZIP entries preserved. [Saved workbook validation](SAP05_Workbook_Validation_12NOV2026.json). Prepublication wording in the original report below is historical.

# SAP-05 — Original BSI Flex 335 v2 Task, TaskAck, Alert, AlertAck, and Error

**12 November 2026 · One owner-authorized SAP-05 original-source packet.** Read the original British Standards Institution (BSI) *[Flex 335 v2.0:2024-03](https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf)*, PDF pages **76–89**, §§6.5–6.7 and **all 18 numbered Tables 78–95**, at relevant normative clause, field, enumeration and source-note depth. Original printed table pixels were specifically checked on PDF pages **77, 81, 84, 88 and 89**. Matched all applicable declarations in the pinned Defence Science and Technology Laboratory (Dstl) [SAPIENT v2 Protocol Buffers source](https://github.com/dstl/SAPIENT-Proto-Files/tree/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0), with exact source blob identifiers in the cumulative [coverage ledger](SAP01_Original_Corpus_Coverage_12NOV2026.json). This packet **does not** include later BSI §7, Annexes A–D, protobuf compilation, live hardware/CSAPI interoperability testing, or donor disposition.

## What this tells us in plain English

**SAPIENT separates what a system can accept from what it actually does.** Registration previously described supported commands; Task now defines the transmitted request, using its own ID, lifecycle control, optional geographic region and a selected command. TaskAck separately records acceptance, rejection, reported completion or reported failure, possibly more than once during a Task. None is, by itself, independently verified physical movement, image acquisition, sensor measurement or effector activation. A useful cross-vendor Details view must not present source-declared command support as an authorized executable user-interface action.

**It also separates different kinds of non-observation information.** Alerts have two communication purposes, Node-to-fusion and Node-to-GUI, but the actual trigger conditions are *system-specific*, not a universal event category. An alert's identity, severity, status, priority, confidence, associated detection and media URL are reporting constructs, not proof that the physical event happened as described. AlertAck is different from Alert status, and protocol Error messages identify malformed or invalid messages rather than equipment malfunction. This is particularly important when a fusion participant or middleware mediates messages on behalf of unlike hardware.

**No donor-wide chassis or command class hierarchy follows.** A mobile Node can receive MOVE_TO/PATROL/FOLLOW tasks, but native rules place autonomous route decisions at that Node and distinguish temporary LOOK_AT and mode changes. No universal mapping to Integrated Sensor Architecture (ISA) commands, Open Geospatial Consortium (OGC) Observations or OGC API – Connected Systems (CSAPI) Commands is declared. The original BSI safety-case discussion for effectors is a NOTE and is neither a certified safety case nor authority to operate physical equipment.

## All original table IDs audited this step

| Original item | Section | BSI PDF page | Native meaning |
| --- | --- | --- | --- |
| SAP-BSI-T078 | §6.5.2 | 77 | Task ID, description, scheduling, control, region, command |
| SAP-BSI-T079 | §6.5.4 | 77 | Task Control START/STOP/PAUSE values |
| SAP-BSI-T080 | §6.5.5.1 | 78 | Region type/ID/name/geometry and class/behaviour filters |
| SAP-BSI-T081 | §6.5.5.2 | 79 | ClassFilter parameter/type/subclass/priority |
| SAP-BSI-T082 | §6.5.5.3 | 79 | SubClassFilter parameter/type/subclasses/priority |
| SAP-BSI-T083 | §6.5.5.4 | 79 | DiscreteThreshold LOW/MEDIUM/HIGH values |
| SAP-BSI-T084 | §6.5.5.5 | 80 | BehaviourFilter parameter/type/priority |
| SAP-BSI-T085 | §6.5.6.1 | 80–81 | Command oneof types, thresholds, mode, geographic pointing/movement, optional parameter |
| SAP-BSI-T086 | §6.5.9.1 | 84 | TaskAck Task ID/status/repeated reasons/associated media |
| SAP-BSI-T087 | §6.5.9.2 | 84 | TaskStatus UNSPECIFIED/ACCEPTED/REJECTED/COMPLETED/FAILED |
| SAP-BSI-T088 | §6.6.1 | 85–86 | Alert ULID, type/status/description, location, priority, confidence and linked evidence |
| SAP-BSI-T089 | §6.6.3 | 86 | AlertType INFORMATION/WARNING/CRITICAL/ERROR/FATAL/MODE_CHANGE |
| SAP-BSI-T090 | §6.6.4 | 87 | AlertStatus ACTIVE/ACKNOWLEDGE/REJECT/IGNORE/CLEAR |
| SAP-BSI-T091 | §6.6.8 | 87 | DiscretePriority LOW/MEDIUM/HIGH |
| SAP-BSI-T092 | §6.6.11 | 88 | AssociatedFile type and media URL within Alert |
| SAP-BSI-T093 | §6.6.13 | 88 | AlertAck original alert ID, repeated reason, AlertAckStatus |
| SAP-BSI-T094 | §6.6.13 | 89 | AlertAckStatus ACCEPTED/REJECTED/CANCELLED and retry rationale |
| SAP-BSI-T095 | §6.7 | 89 | Error original invalid packet bytes and repeated textual error messages |

This is **18 source-table content inspections**, not merely 18 Table-of-Contents contacts. Together with earlier packets, **95 of 97 numbered BSI main tables** have now been examined at recorded content/field depth. Remaining original Tables96–97, Annex C.1, Taxonomy/Annex original material, source access obligations, and specific holds are reserved for SAP-06 and the eventual owner disposition. Main-table contact must not be misrepresented as comprehensive entire-original or native-schema conformance.

## Stable native source findings

| Source ID | Original BSI / proto locator | Native standing | Source meaning, scope and limits |
| --- | --- | --- | --- |
| SAP05-N01 | BSI §§6.5.1–6.5.3 PDF76–77; Task proto; T78 | SCOPED_SHALL_AND_NOTE | Fusion Node tasks a lower Node through message handling; one region or command must be specified subject to default-task conditions; Task ID, start/end and Control are distinct from execution. |
| SAP05-N02 | BSI §§6.5.3–6.5.4 PDF77–78; task.proto Task.Control; T78, T79 | SCOPED_SHALL_AND_NOTE | START/STOP/PAUSE manage a Task lifecycle and prior-task restoration; Task.ID is stated required while a NOTE describes blank ID as default. DEFAULT control is listed in Table78 but absent in current Table79/proto. |
| SAP05-N03 | BSI §6.5.5.1 PDF78; task.proto Task.Region; T80 | SCOPED_SHALL_AND_COMMENTARY | Task.Region names a tasking region with ID/type/area and optional class/behaviour filters; not necessarily a presently installed or executed equipment Zone. |
| SAP05-N04 | BSI §§6.5.5.2–.5 PDF79–80; task.proto filters; T81, T82, T83, T84 | SCOPED_SHALL_AND_NOTE | Class/SubClass/Behaviour filters and DiscreteThreshold priority are task criteria that may be supported by an edge Node; not source observations or general ISA range schemas. |
| SAP05-N05 | BSI §6.5.6.1 PDF80–81; task.proto Task.Command; T85 | SCOPED_SHALL | Only one command oneof choice appears per Task.Command; potential REQUEST, sensitivity/report-rate thresholds, mode change, LOOK_AT, MOVE_TO, PATROL, FOLLOW have distinct native meanings. |
| SAP05-N06 | BSI §6.5.6.2 PDF81; task.proto Task.Command; T85 | SCOPED_SHALL | REQUEST registration/status/reset/stop/start affects SAPIENT Node task/reporting; STOP detection messages still allows regular status and is not evidence equipment was powered off. Reset scope conflicts with earlier BSI Table58 reboot wording. |
| SAP05-N07 | BSI §§6.5.6.3–.5 PDF81–82; task.proto DiscreteThreshold; T83, T85 | SCOPED_SHALL_AND_COMMENTARY | Detection threshold, detection report rate and classification threshold request different sensor adjustments; two passages mislabel their field as classification_threshold, held against distinct pinned oneof names. |
| SAP05-N08 | BSI §§6.5.6.6–.7 PDF82; task.proto Task.Command; T85 | SCOPED_SHALL_AND_NOTE | MODE_CHANGE chooses a registered mode (ignored for one-mode Node); LOOK_AT temporarily suspends tasking then resumes, with a DetectionReport only if an object is detected. TaskAck completion alone does not authenticate physical pointing. |
| SAP05-N09 | BSI §§6.5.6.8–.10 PDF82–83; task.proto/follow.proto; T85 | SCOPED_SHALL | MOVE_TO waypoints and autonomous routing, PATROL loops/routes and FOLLOW targets are distinct mobile-platform instructions, which can supersede each other; no proof a real platform moved. |
| SAP05-N10 | BSI §6.5.6.10 PDF83 and Table59 PDF63; follow.proto; T85 | CROSS_ARTIFACT_CONFLICT | BSI current §6.5.6.10 says FOLLOW accepts a list of object ULIDs, while earlier Table59 and pinned FollowObject carry a single follow_object_id. Do not infer multi-target wire support. |
| SAP05-N11 | BSI §§6.5.7–6.5.9 PDF83–84; task_ack.proto; T86, T87 | SCOPED_SHALL | A Node may send one or more TaskAck messages over a task lifetime; ACCEPTED, REJECTED, COMPLETED, FAILED are reported statuses, not independent evidence of completed physical effect. |
| SAP05-N12 | BSI §6.5.9 PDF84; task_ack.proto; T86, T87 | SCOPED_SHALL | TaskAck.task_id correlates with Task ID, repeated reason describes rejection/failure, associated file may link output; malformed Task gets Error instead of TaskAck. |
| SAP05-N13 | BSI §§6.6.1–6.6.2 PDF85–86; alert.proto; T88 | SCOPED_SHALL_AND_NOTE | Node Alert may be intended for GUI or fusion Node; trigger conditions are explicitly system-specific; Alert ULID, optional type/status/location/priority/rank/confidence/media are reported claims. |
| SAP05-N14 | BSI §§6.6.3–.10 PDF86–87; alert.proto; T89, T90, T91 | SCOPED_SHALL | AlertType severity/intended mode change, AlertStatus lifecycle and discrete Priority are separate enums; MODE_CHANGE may request autonomy permission and is not the Node's selected mode or actual physical action. |
| SAP05-N15 | BSI §6.6.11 PDF88; associated_file.proto; T92 | SCOPED_SHALL_AND_NOTE | Alert-associated media has MIME-like type and URL; link is not verified retrieval, original observing instrument or authenticated event provenance. |
| SAP05-N16 | BSI §6.6.13 PDF88–89; alert_ack.proto; T93, T94 | SCOPED_SHALL_AND_NOTE | AlertAck uses same alert_id, reasons and ACCEPTED/REJECTED/CANCELLED; rejection can advise a retry interval; acknowledging Alert is not authority for arbitrary device command or proof of action. |
| SAP05-N17 | BSI §6.7 PDF89; error.proto; T95 | SCOPED_SHALL | Message handling responds to invalid incoming protocol messages with Error.packet bytes plus repeated error strings; this is messaging validation, not an equipment fault diagnostic. |
| SAP05-N18 | BSI Task Table78/Table79 and task.proto; T78, T79 | CROSS_SOURCE_DISCREPANCY | Task Table78 lists DEFAULT control among accepted controls, but Table79 does not and pinned Task.Control reserves enum tag 4; a mandatory DEFAULT wire value cannot be inferred. |
| SAP05-N19 | BSI §6.5.6.2 and earlier Table58; task.proto; T85 | INTRA_BSI_CONFLICT | BSI §6.5.6.2 REQUEST reset returns the Node to default state, whereas earlier Table58 says REQUEST Reset reboots the Node; the two meanings are not silently identical. |
| SAP05-N20 | BSI AlertAck Table93/Table94 and alert_ack.proto; T93, T94 | CROSS_SOURCE_DISCREPANCY | AlertAck reason is described in BSI Table93 as for rejected task and Table94 ACCEPTED as an alert active awaiting response; native AlertAck relates to alert receipt/status. Retain exact wording conflict. |
| SAP05-N21 | BSI §§6.5.6.3–.4 and task.proto; T83, T85 | INTRA_BSI_FIELD_WORDING_CONFLICT | Detection_threshold and detection_report_rate passages name classification_threshold as field type; pinned proto and BSI Table85 distinguish actual fields. |
| SAP05-N22 | BSI TaskAck/AlertAck field tables and pinned source tags; T86, T87, T93, T94 | SCOPED_ENCODING_RECONCILIATION | TaskAck.reason repeats at tag5 after reserved3; AlertAck.reason repeats at tag4 and alert_ack_status tag5 after reserved2–3. These are field-serial facts, not BSI-to-CSAPI equivalence. |

## Exact conflicts and unavailable proof retained

- **SAP05-H01 (INTRA_BSI_VS_NATIVE_ENUM_CONFLICT)** — BSI Task Table78 prints Control 'Default' while Table79 lists only UNSPECIFIED/START/STOP/PAUSE and pinned Task.Control reserves enum tag4. Do not fabricate CONTROL_DEFAULT.
- **SAP05-H02 (NORMATIVE_VS_NOTE_ID_APPLICABILITY)** — BSI §6.5.3 says Task shall include task_id, with a NOTE saying blank task_id signifies default task; pinned Task.task_id has is_mandatory and is_ulid annotations. Applicability/default-message interpretation not automatically reconciled.
- **SAP05-H03 (INTRA_BSI_RESET_MEANING)** — BSI current §6.5.6.2 REQUEST reset says stop task and return to default state, while Registration Table58 calls REQUEST Reset a Node reboot. Do not equate these for an ISA Reset or CSAPI Command binding.
- **SAP05-H04 (COPYEDIT_FIELD_REFERENCE_CONFLICT)** — BSI §6.5.6.3 and §6.5.6.4 describe detection_threshold and detection_report_rate but each calls its parameter classification_threshold; pinned Task.Command keeps three different oneof fields. Do not alias them.
- **SAP05-H05 (FOLLOW_CARDINALITY_CONFLICT)** — BSI §6.5.6.10 describes list of object ULIDs, while original Table59 and pinned FollowObject contain single follow_object_id string (without explicit repeated); do not assert multi-target wire compatibility.
- **SAP05-H06 (ALERT_ACK_REASON_SCOPE)** — BSI Table93 AlertAck.reason describes rejection of a 'task', while surrounding §6.6.13 and pinned alert_ack.proto describe rejection of an alert; retain explicit cross-wording hold.
- **SAP05-H07 (ALERT_ACK_ACCEPTED_SEMANTICS)** — BSI Table94 ACCEPTED says alert 'active and has yet to be responded to'; pinned AlertAckStatus.ACCEPTED means alert accepted and this is an acknowledgement; do not infer an additional mandatory alert workflow.
- **SAP05-H08 (ALERT_PERMISSION_STATUS_FIELD)** — BSI §6.6.13 rejection response refers generically to 'status field to reject', while Table93 and pinned schema use alert_ack_status; distinguish from separate Alert.status and preserve source-specific retry reasons.

All previous SAPIENT source holds (six original `SAP-ISSUE` families, SAP02 five, SAP03A three, SAP03B five and SAP04 four) remain open or bounded at their original scopes. **Unreviewed original text does not mean no source equivalent**, and descriptive/Note language or protobuf `optional` does not override normative BSI mandatory/discretionary/conditional rules. We do not repair BSI/protobuf disagreements by guessing wire tags, deleting source clauses, or constructing a final DIM schema.

## One canonical crosswalk, source-qualified integration

The source ledger stages **42 existing-row SAPIENT column-G mappings** with stable `row_id`, original source IDs, relation grades and negative-equivalence caveats. These cover real Task/TaskAck/Alert/AlertAck/Error message roles and carefully limited parallels to some ISA request/control/diagnostic topics. The aim is to preserve vendor/equipment distinctions and explicit no-established mappings, not to manufacture new generic command semantics for every named source operation.

The **same original 26-sheet editable Excel** must be refreshed and verified against the canonical one JSON, BOTH CSV mirrors and BOTH GitHub-readable Markdown comparisons before this SAP-05 result is declared cross-format complete. The full pre-step research branch version is preserved in [pre-SAP05 historical archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sap05-20261112/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/) at `33876c1a5802c742b452b1831dd8c6a76d9345a8`. No case values, other donor data, grouped OGC foundations, proposed DIM adoption flags or original Excel historical tabs are authorized for mutation.

## Remaining work and single stop boundary

The previous post-SAP04 remaining forecast was **LOW 2 / MOST LIKELY 3 / HIGH 5** additional substantive Proceeds. Following original SAP05 source research the estimate becomes **LOW 1 / MOST LIKELY 2 / HIGH 4** for remaining Taxonomy/Annex source audit and final source coverage/owner-disposition gate, with access-dependent source holds. This is a qualified forecast, **not a promise of entire-original comprehensive coverage within two steps**; a materially larger scope or method change requires an explicit owner decision.

**ONE NEXT distinct owner `Proceed` = SAP-06 ONLY**, BSI original §7 Taxonomy, Tables96–97, informative Annexes A–D and Table C.1, plus outstanding original source issue reconciliation at evidence-bounded depth; then **STOP** before SAP07 donor disposition, DIM/Profile requirements, Glaux/client or deployment.
