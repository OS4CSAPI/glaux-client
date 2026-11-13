# SAP-07 — SAPIENT v2 source-coverage and owner-disposition packet

**13 November 2026.** **SAP-07 evidence/owner packet COMPLETE; owner decision AWAITED; SAPIENT remains ACTIVE.** This is the approved source-first closure audit and recommendation, not source-completeness certification, adoption of a Domain Information Model (DIM) class or a Connected Systems (CSAPI) Profile rule, or authorization for another donor. [Preserved pre-SAP-07 complete version](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sap07-20261113/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/) is fixed at `887d0f825899466b3c1d4e4b316641e5e65e4733`.

## Result in plain English

The SAPIENT v2 research is sufficiently developed for a useful **source-qualified comparison** of a connected sensing system's network participants, declarations, reports, tasks and responses. SAPIENT Nodes may be physical-edge, fusion, software or middleware roles; they are not necessarily separately installed sensors with equipment serial numbers. Registration declares potential capability, status/detection reports describe source messages, task acknowledgements report processing outcomes, and a detected object's “Equipment” class is **not** the physical sensing-equipment inventory.

**Recommendation: OWNER OPTION A — bounded PARTIAL donor disposition.** Preserve all documented source conflicts and access/test limitations, but do not manufacture endless extra packets merely to eliminate every editorial inconsistency or audit every implementation. A bounded PARTIAL is an honest completion of this research scope, **not** complete original-source or runtime conformance. Only the owner can select it.

## Original corpus and coverage: contact is not completeness

| Original source | SAP-07 verified source coverage | Exact limitation |
| --- | --- | --- |
| British Standards Institution (BSI) *Flex 335 v2.0:2024-03*, 116-page original publisher PDF, clauses 0–7 | **97 of 97 main numbered tables** have explicitly annotated **bounded original-source content review** across SAP-02 14, SAP-03A 18, SAP-03B 27, SAP-04 18, SAP-05 18, SAP-06 2. Stable IDs `SAP-BSI-T001` to `T097` are distinct and represented. | Not every standalone narrative SHALL, visual, external work or figure has been exhaustively clause-audited; table-depth counts are not complete 116-page conformance. |
| BSI's 58 numbered contents entries | **57/58** source-ledger heading records have a later packet review annotation. The unannotated `SAP-BSI-6` is a parent heading; its children (§6.1–6.7 and Tables15–95) were inspected in the detailed packets. | Missing parent annotation is a ledger bookkeeping limit, not proof that the substantive child clauses are unread. No claim of full independent §6 parent clause audit. |
| Four **informative** Annexes A–D, Figure7, Annex C Table C.1 | SAP-06 inspected the annex text and selected source figures; target taxonomy and behavior have exact original records. | Annex B's JSON-like illustrations are **not executable protobuf conformity fixtures**; Annex D links to restricted/external works not audited. Streaming video is excluded by the original specification. |
| 16 Defence Science and Technology Laboratory (Dstl) pinned SAPIENT v2 `.proto` original files and shared `proto_options.proto` | Confirmed **16/16 original files** at pinned commit `244a741c13bcee628f84944aef91e4a66854bd7d`; the source census counted 62 message and 31 enum declarations. Packet semantic reviews examined relevant fields/enums/options/comments at graded depth. | **No full native source file-by-file field/enum/constraint audit, protobuf compiler or test harness execution**; structural file retrieval is not normative or runtime completeness. |
| Other companion evidence | Selected official middleware, harness, guidance and earlier bounded SAPIENT challenge records were qualified as context, not source rules. | No independently proven physical actuation, vendor deployment, middleware behavior, OGC binding or comprehensive original external standards audit. |

**Access correction:** The original 116-page BSI source is accessible via Library text/page reading, as rechecked in Profile Rewrite 29. Its raw original binary SHA-256 has not been authenticated. Do not convert the historical SAP-01 raw-byte-access limitation into a claim the original contents cannot be read.

## Source-to-master crosswalk and workbook audit

The six audit packets record **181 source-to-row mapping assessment events across 110 distinct existing stable row IDs**: SAP-02 17, SAP-03A 28, SAP-03B 28, SAP-04 40, SAP-05 42 and SAP-06 26. The relation codes are **93 RELATED, 27 PARTIAL, 58 NO_ESTABLISHED and 3 NARROWER**. All **271 referenced source-ID uses** resolve to **82 unique native finding IDs** without an orphan; none of those packet mappings records an adopted DIM/Profile element. The older SAP-02 `source_ids/value` structure and later `source_item_ids/display` are different retained historical evidence shapes, not lost originals.

Mapping events are not 181 simultaneously populated current SAPIENT cells or model-vote counts: later packets revised some of the **same** existing column-G cells. Their earlier source-qualified mappings, exact source IDs and caveats remain in the cumulative ledger and original packet reports. The current GitHub master CSV retains **all 26 latest SAP-06 G-display values exactly**, and the SAP-06 saved validation records a **346 × 15 = 5,190-cell** match across one JSON, both CSV mirrors, both readable Markdown views, and the **same original 26-sheet editable Excel**, preserving the other worksheets and 42 unaffected ZIP members.

**SAP-07 changes zero canonical master comparison cells.** The latest [editable master Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) is unchanged since verified SAP-06; no fresh binary parser rerun is claimed because there was no workbook change. [SAP-06 actual saved-file validation](SAP06_Workbook_Validation_13NOV2026.json) remains the last verified checkpoint, with **zero comparison-cell lag**. Master/Excel parity is separate from original-source completeness, substantive mapping support, DIM/Profile adoption and runtime conformance.

## Outstanding precise source holds

The cumulative source ledger retains **39 named hold/limitation entries**: six prior `SAP-ISSUE-01..06`; two early `SAP01-ACCESS/DETAIL` notes; 31 new packet-specific `SAP02-H01..05`, `SAP03A-H01..03`, `SAP03B-H01..05`, `SAP04-H01..04`, `SAP05-H01..08` and `SAP06-H01..06`. The records overlap: **39 does not mean 39 independent defects, research packets or mandatory remediation actions.** All original IDs and locators remain in the [cumulative original-source ledger](SAP01_Original_Corpus_Coverage_12NOV2026.json).

| Family | Representative exact original/source questions |
| --- | --- |
| **Native serials and schemas** | `SAP-ISSUE-01` BSI Registration `config_data` tag9 versus pinned proto tag10/`reporting_region` tag9; `SAP03A-H01` Duration.value BSI2 versus proto reserved2/value3; `SAP03B-H03/H04` type terminology and enum-versus-oneof serial distinctions. **No invented wire-tag repair.** |
| **Identity, time, units and requirements** | `SAP-ISSUE-02/03/06`, `SAP02-H01..H04`, `SAP03A-H02/H03`, `SAP04-H01..H04`: content vs send time, coordinates/datum/angles, BSI M/D/C vs protobuf optionality, mode applicability and DerivedDetection timestamps/attribution remain qualified. A Node UUID does **not** prove physical equipment identity or exact CSAPI System mapping. |
| **Tasks and alert semantics** | `SAP05-H01..H08`: DEFAULT control, blank task IDs, reboot vs reset-to-default, mislabeled command parameters, FollowObject single/multiple IDs and AlertAck status/wording. TaskAck is **not** independent evidence of physical effect or a CSAPI Command equivalence. |
| **Taxonomy and informative samples** | `SAP06-H01..H05`: editorial Flex355 predecessor heading, missing TaskAck mandatory status in example, UUID-shaped example instead of ULID alert ID, removed `Command.name`, and informative middleware registration exception. Detected-object classes and behaviors are not sensor chassis, active equipment status or universal ontology imports. |
| **Original access, external works and runtime** | `SAP-ISSUE-04/05`, `SAP01-ACCESS/DETAIL`, `SAP06-H06`: full original external/restricted references, detailed all-clause/diagram audit, unverified raw PDF hash, native compilation/test harness, middleware/source-device runtime and cross-standard interoperability. The text of the source BSI PDF **is available**, notwithstanding its unverified binary checksum. |

The earlier **six** Integrated Sensor Architecture (ISA) source-definition questions and **nine** The Open Group Sensor Open Systems Architecture (SOSA) C239 owner-accepted **PARTIAL** source-hold families remain separate. No SAPIENT research finding waives them or establishes 2022/2023/2025 SOSA native-equivalence assumptions.

## Meaning for future whole-system DIM / common client

SAPIENT adds a **network interaction and reporting viewpoint** to the prior ISA and The Open Group SOSA perspectives: participating Nodes, declared modes and capabilities, health/status messages, detection data, classified targets, alerts, requested work, acknowledgments and optional intermediaries. It does not define an independent universal physically installed equipment list or standardize all vendor sensors' power, cables, video resources, data histories and management capabilities. Future cross-donor reconciliation should preserve distinct **individual equipment, physical/logical relationship, Node role, declared capability, current report, observed target, task request, status and actual verified effect** meanings without automatically inventing one class for each.

**No adoption:** the next owner gates remain established broader Step24 (ready coherent DIM portions), Steps35–39 (reconciliation, diagram, source-case testing) and Step40 (named-version decision). No new mandatory chassis, field/cardinality, CSAPI Profile SHALL, UI tabs, live controls or Glaux changes are approved by SAPIENT source assessments.

## Owner choices and STOP

**OPTION A — ACCEPT BOUNDED PARTIAL (RECOMMENDED).** Accept the SAP-01–SAP-07 original-source work as sufficient at its specifically documented **bounded PARTIAL** grade, preserve all 39 hold/limitation entries and prior ISA/SOSA evidence, and record SAPIENT as **PARTIAL—OWNER ACCEPTED** in a separately authorized status publication. This finishes this donor's planned research without pretending external originals or deployed devices have been comprehensively assessed. It does **not** automatically authorize another donor or model implementation.

**OPTION B — KEEP SAPIENT ACTIVE.** Specify **which exact original native conflict, companion file, external authoritative source or conformance obligation** must be addressed to justify a stronger disposition. Rebaseline the source-sized work and remaining low/likely/high estimate for owner approval before any new packet; do not silently start work or revive an endless prompt series. Source-inaccessible material remains a named limitation, not a fictional resolved equivalent.

**SAP-07 is finished; the owner has not selected A or B.** **ONE NEXT ACTION:** owner explicitly chooses **OPTION A or OPTION B**; STOP before donor closure publication, another donor, DIM/Profile adoption, application/UI or deployment.

**Owner delivery rule:** Whenever a future step actually updates the master Excel document, its final response **must link directly to the latest committed canonical editable `.xlsx`**. SAP-07 edits no workbook cells; the current direct link is supplied above anyway.
