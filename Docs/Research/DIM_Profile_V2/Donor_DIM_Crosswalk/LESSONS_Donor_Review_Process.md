# CURRENT REUSABLE DONOR PRACTICE — L23 mandatory source-to-Excel synchronization gate (9 November 2026)

**Owner decision, 9 November:** The earlier phrases "substantive checkpoint" and "at donor closeout" were too discretionary: after SOSA-G2-1, **12 source-qualified donor cells** were current in JSON/CSV/Markdown but absent from the canonical 26-sheet XLSX. This was an execution/method-control failure even though the older snapshot was correctly labeled. A previously described workbook-lag exception is not authorization to silently make it the default.

**L23 (controlling):** For *every bounded, substantive original-source review packet that changes one or more canonical comparison cells*, update the one JSON plus both CSV and both readable comparisons, and complete a verified refresh of the **SAME** canonical Excel workbook **before starting the next source packet**. A metadata-only census or genuinely zero-cell pass does not trigger a rebuild. A deferral needs explicit owner consent for the precise affected cells, named snapshot/version, planned next Excel checkpoint and pause/resumption boundary. No automatic bundling across several independently completed donor packets, and no artificial micro-packets to force wasteful releases.

**Verification required:** Compare every actual saved workbook grid cell to the current source grid (not merely the changed-cell count), preserve all 26 sheet names/order, unchanged historical evidence sheets, non-target donor/case/DIM cells and previous decisions; confirm workbook bytes/hash, XML/ZIP integrity, real source/coverage and a GitHub commit/readback plus appropriate CI. Report separately **source coverage**, **master text parity**, **Excel parity**, **DIM/Profile adoption**, and **runtime conformance**. If a workbook refresh or CI fails, investigate and repair within the same bounded publication checkpoint; **do not advance donor work** and do not claim parity.

**Why this does not reverse ISA lesson L11:** The source packets are chosen for meaningful original-source complexity, not fixed tiny entry counts. Only after a coherent packet actually changes the master is the Excel checkpoint mandatory; existing publishers, workbook and verification checks must be reused. This adds a clear stop condition to the accepted catalogue-level cadence, not a new script/report/Excel release after each trivial subclause or source spotcheck.

[Actual G2-1 source and 12-cell difference](SOSA_G2_1_Original_Source_and_Master_Correspondence_09NOV2026.md) · [controlling SOSA execution plan](PLAN_SOSA_Source_Coverage_Correction_v0.1_09NOV2026.md).

## Earlier lessons and historical comments — preserved below

# CURRENT — Lessons through SOSA-G2-1, 9 November 2026

<!-- LESSONS_THROUGH_SOSA_D_09NOV2026 -->

Source-first method now incorporates bounded The Open Group SOSA C239 review, explicit 8-file native source gaps and verified 15-column workbook. [Final source/workbook evidence](Step17_SOSA_D_Crosswalk_Integration_Closeout_09NOV2026.md). Do not automatically impose ISA's 22-delivery correction process on other donors; only next owner “Proceed” advances Step18 SAPIENT.

## Historical lessons and earlier activity

# Donor review — lessons and reusable practices

**7 November 2026 · Updated after ISA-03D and the owner's rejection of repeated miniature releases.** This is an evidence-based lessons record, not a second execution plan. The [current progress](ISA_Correction_Status_07NOV2026.json), [plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) and [PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) alone route the next action. Historical NEXT instructions were removed from this document to avoid competing recovery instructions.

Completed ISA-01/02/03A-D source and publication work remains complete. The source reviews produced useful findings; that does not establish that their repeated delivery process was efficient. The original twelve-prompt estimate and the later mandatory per-mini-batch Excel-release cadence are superseded. No new donor work or scientific conclusion is created by recording this lesson.

## Practices and the evidence behind them

| ID | Evidence observed in this effort | Practice and its limits |
| --- | --- | --- |
| **L01 — Source-native inventory** | The original eleven-concept ISA selection omitted Manufacturer, Model and Serial Number. The census registered480 named entries independently of the selected rows. [Census](ISA01_Source_Census_07NOV2026.md). | Enumerate from original source contents/body/index or schema/ontology structure, then examine both existing-row coverage and useful unmatched source concepts. An inventory is a coverage instrument, not a semantic verdict or a required row count. |
| **L02 — Explicit empty-cell states** | A blank manufacturer position was reasonably read as possible donor absence. The census gave unreviewed cells explicit status. | Distinguish not reviewed, an exact question and no correspondence found in a named inspected scope. Keep coverage, mapping relation and model acceptance separate. |
| **L03 — Complete entry boundaries** | Zones/Zoom and several observables continued beyond the plan's approximate page ranges. [Boundary amendment](ISA01_Plan_Amendment_07NOV2026.md). | Assign complete named entries; page ranges navigate rather than define scope. Follow continued tables and required cross-references. |
| **L04 — Coverage is not parity** | The early workbook and its ledger agreed while both omitted native identity properties. | Check inventory-to-source coverage separately from workbook/data parity. A source-first semantic audit must compare original definitions, not only generated artifacts. No checksum proves interpretation. |
| **L05 — Trace every assigned item** | Census assignments account for480 catalogue entries,279 blocks,31 original row/topic targets and25 earlier findings. | Preserve assignment and justified disposition for each relevant item. Supporting definitions and grouped mappings are legitimate outcomes; a field count is neither physical-component count nor compulsory DIM-row count. These record populations are not additive. |
| **L06 — Local uncertainty and earned completion** | A completed census originally had a separate publication problem; several definitions later produced precise questions. | Attach uncertainty to its exact source/record/action. Completed work is reopened for new evidence, not an old blanket disclaimer. Do not disguise unread material as a completed question. |
| **L07 — Durable GitHub delivery** | The owner had to repeat the repository-publication requirement after a sandbox-only checkpoint. Recovery verified original artifact hashes. [Recovery record](ISA01_Publication_Recovery_07NOV2026.json). | Commit research to the named branch and read back actual content. Local attachments supplement GitHub. Source/readable-table publication and a dated Excel snapshot can have explicitly different cadences; do not claim an old workbook contains newer data. |
| **L08 — Actual meaning beats similar labels** | Maintenance is contact information, Identity tactical classification, Data Outputs transfers, Visible laser-spectrum information and Relationship physical attachment. [ISA-02 evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json), [ISA-03D evidence](ISA03D_Relationship_Visible_Evidence_07NOV2026.json). | Inspect the native definition, kind, type and scope before matching names. Preserve individual traceability whether the disposition is an existing row, new row, group, support type or exclusion. |
| **L09 — Extension standing and sparse definitions** | Source body markings identify Accepted extensions; Level and Link Loss lack particular defining prose. POC and reporting types carry qualifications that a title alone misses. | Preserve core/Custom/Nominated/Accepted standing. Read referenced definitions and actual field/cardinality constraints. Keep an exact question instead of invented semantics or a project-wide hold. |
| **L10 — Whole-task sizing, not headings** | ISA-02 combined49 properties,46 supporting definitions,45 added rows, identifier reconciliation, workbook work, checks and publication. The subsequent two-to-six-property rule still produced long repeated deliveries. | Estimate source interpretation plus dependencies and the actual delivery being performed. A large source section is not a prompt; a small entry count does not guarantee an efficient prompt. The old numeric ceilings were a failed universal prescription, not a permanent method. Platform failure causation is not diagnosed by this observation. |
| **L11 — Batch expensive delivery; keep research current** | ISA-03A-D repeatedly used input exports, locally authored workbooks, transfer segments, bespoke batch validators/workflows and many document updates. The scripts already share an assembler; source batches of only two properties still carried substantial release overhead. [Example publisher](../../../../scripts/publish_isa03d_checkpoint.py). | Commit source/evidence/coverage and the cumulative readable table during coherent review passes; produce the workbook at catalogue or substantial-section checkpoints. Reuse the existing assembler and verification code. Do not create a new exporter/workflow/report/index rewrite merely because another prompt ended. This change removes a mandated repeated activity; actual throughput improvement must be observed, not claimed in advance. |

## Specific findings retained

**Original identity omissions:** Manufacturer, Model and Serial Number were found in original DMS6.0r12 and corrected. Their scopes and the UCI identifier rules still matter; correcting an omission does not make every same-name mapping exact.

**Source standing:** ISA-02 retained46 core and three Accepted-extension properties. ISA-03B retained five Accepted extensions and core Specification Version, with distinct contact and version meanings. See [ISA-03B evidence](ISA03B_Ownership_Versions_Support_Evidence_07NOV2026.json). Prior source-standing decisions are not altered by scheduling changes.

**Spatial interpretation:** ISA-03C retained world Orientation as a source concept while isolating its exact frame wording as ISA-Q003. Optional hardware-perceived Position does not become mandatory whenever override is supported, and default uncertainty values are not observed perfect accuracy. [ISA-03C evidence](ISA03C_Position_Orientation_Evidence_07NOV2026.json).

**Physical versus network versus spectral meanings:** Relationship's ATTACHED/DETACHED concern physical links; its child list cardinality0+ does not invent a mandatory installed child. Visible concerns laser wavelength range, not architectural exposure or a firing action. [ISA-03D report](ISA03D_Relationship_Visible_07NOV2026.md).

**Transfer and source images:** The Actions artifact-download route recovered exact source workbook inputs when public raw download was unavailable. Original indexed PDF text could be accessible even when page-image export failed. Describe precisely which bytes/text/images were inspected; do not generalize a failed route to source unavailability.

## What is current practice versus what remains to demonstrate

The catalogue-level publication cadence is now the active execution rule. Every source pass still goes to GitHub, and the readable comparison must reflect its evidence. The workbook is explicitly labeled by its own covered checkpoint until refreshed; planned snapshot lag is not an error or unfinished source review. Do not multiply reports, lessons entries or index copies to restate the same progress.

The remaining26 property IDs have been partitioned exactly once into three source/readable-table passes, followed by one workbook checkpoint. This is a bounded working schedule for that catalogue remainder, not a new guarantee of the entire ISA completion cost. Actual semantic workload and useful grouping determine later source passes. Do not conceal an unexpected missing dependency or relabel unreviewed work to protect the schedule.

The final audit must still demonstrate full inventory coverage and source-fidelity checking. It also needs to reconcile model granularity: multiple source entries may contribute to one information element, and some entries are supporting definitions rather than new DIM concepts. Keep all evidence traceable without assuming that maximal row proliferation is completeness.

## Maintenance and historical provenance

Add a lesson only for a new substantive observation, normally in the existing record. At final ISA closeout, consolidate demonstrated practices into the reusable donor-review method, adapting it to the next donor's actual source structure. Do not duplicate the whole lessons document in each PITON or treat a particular number of prompts as universal.

The prior detailed chronology and now-obsolete routing labels remain in [the lessons file at completed ISA-03D](https://github.com/OS4CSAPI/glaux-client/blob/c34f7b1560a920a85c9061deec63c6dd6ab49e4b/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/LESSONS_Donor_Review_Process.md). Current task selection belongs to progress and the current PITON, not to an old lesson's next-step sentence.


## 8 November 2026 — separate evidence inclusion from model adoption

A working comparison must accumulate verified donor findings as they are reviewed. Holding them in a separate donor workbook until final model adoption can leave the master misleadingly empty. The owner authorized integrating completed ISA evidence into the canonical master now, with candidate/model standing retained separately.

Use existing cross-donor checkpoints for substantive adoption: ready coherent portions at broader Step24, then consolidated version approval after Steps35–39 synthesis and case review, at Step40. Readiness means clear meaning,scope need,relevant alternatives and a concrete example—not four new per-field tasks, majority-donor voting or a compulsory one-source-row/one-model-class mapping. Once accepted, content is recorded as accepted for the version and revised only for an evidenced specific reason.

One canonical master and one active routing record prevent a future recovery from following obsolete CURRENT/NEXT banners. Historical snapshots remain usable evidence, not new work assignments.

## Final reusable donor-review lessons — ISA Delivery22, 9 November 2026

These lessons are anchored in the actual Delivery21 source-first audit, Delivery22 published saved-XLSX comparison and original ISA source-register inventory. They describe methods to apply to later donors; ISA-specific batch sizes, native terms and unresolved interpretation questions are not universal requirements.

| ID | Observed ISA evidence | Reusable practice |
| --- | --- | --- |
| L12 — Inventory coverage and true source meaning are distinct | All 480 DMS entries and 279 source records are accountable, yet six original interpretation questions remain precisely held. | Count original entries/sections first, then adjudicate exact native meaning; never convert a catalogue or title into an automatically accepted DIM field. |
| L13 — Qualified correspondence is not DIM adoption | The source-first audit examined 31 original targets and 25 prior findings: 18 proposed information elements gained some qualified native correspondence, four have no established equivalence, nine case topics and fourteen design issues remain held. | Record match type, source edition/clause and negative-equivalence boundary per contribution. Separate source discovery, workbook inclusion and owner-approved model adoption. |
| L14 — Periodic Excel snapshots require explicit verification | Before finalization, the current readable source master had 329 rows while the older 26-sheet workbook still had 253; the final actual saved workbook now agrees with all 346×14 grid cells. | Keep JSON/CSV/Markdown current, clearly label stale workbook snapshots and rebuild at substantive/final checkpoints instead of manufacturing repeated per-group publishers. |
| L15 — Historical case/donor evidence must survive publication | The final workbook retained all 26 sheet names; ten current audit/review views changed, sixteen original sheet XML contents remained unchanged, and all 58 donor and 73 source-case records were preserved. | Preserve original case truth and non-target audit sheets with actual file/cell checks, not just row counts or written assertions. |
| L16 — Visual review is not external conformance | The saved workbook was rendered to a PNG preview and inspected; original-source and ZIP/XML/cell-parity tests passed, but no native Excel application screenshot, ISA runtime or OGC ATS was executed. | Name the renderer and original evidence precisely, maintain explicit limitations and avoid treating successful project-specific validation as certified standards or independently interoperable producer/client behavior. |

The next use of this method is the existing broader donor crosswalk Step16 substantive owner review, only when separately authorized. No automatic extra ISA step, 182-donor audit, or compulsory ISA chassis is implied.


## Lessons L17–L20 — The Open Group SOSA source-first review and integration (9 November 2026)

| ID | Original evidence | Practice for later donors |
| --- | --- | --- |
| **L17 — A named component is not necessarily physical equipment** | C239 distinguishes SOSA Sensor, physical Hardware Element, logical Module, Host Platform, runtime infrastructure and procurable implementation. | Keep native identity, implementation kind, physical membership, functional role and relation type separate, even when one source uses the same general word. |
| **L18 — Normative file pointer is not native source audit** | Appendix B names separate DSDM/IDL and six OpenAPI files; §5.7's B.2 pointer differs from actual Appendix B.1. Actual files were not retrieved. | Record exact source/edition and access status, never fabricate native fields, cardinality or endpoints, and retain original conflicting source references visibly. |
| **L19 — Source-grade matters more than a candidate count** | C239 includes defined management Rules but also explicitly preliminary task functions and reference-only power/reporting modules. | Do not elevate descriptions, future placeholders, or example modules into mandatory whole-system classes or applied equipment controls. |
| **L20 — One canonical donor column plus detailed held evidence** | 76 native C239 records were reconciled into 57 related/partial/held decisions across only 38 existing master rows; all other donor/case facts survived 26-sheet workbook checks. | Integrate at substantial donor closeout, retain Not assessed here distinctly from no equivalence, verify actual workbook cell parity and leave DIM adoption to owner checkpoints. |

The next application is Step18 SAPIENT v2 with a donor-specific source-census and edition check before attempting exhaustive claim. The original Step24 and Steps35–40 reconciliation/adoption reviews remain in force.


## L21 — Complete source census before claiming a donor review is complete (SOSA-G1, 9 November 2026)

The earlier four SOSA-A/B/C/D iterations established 76 selected original C239 source records, 57 qualified review decisions, and a verified 15-column workbook, but did not establish exhaustive original-source coverage. G1 then identified **12 registered lineage artifacts, one additional C239-native DSDM dependency, a separate restricted Appendix C overlay and 192 original C239 table-of-contents headings**: 65 with selected source passages inspected, 126 not substantively reviewed and one restricted. Each of the 76 prior source records was traceable to a known original contents heading, but **no section was certified fully audited**.

**Reusable requirement:** Original-source artifact/section/Rule/element inventory and relevance screening must precede claims of donor completeness. Maintain separate *source sample read*, *full source coverage verified*, *native companion actually accessed*, *crosswalk-integrated*, *DIM adopted*, and *runtime conformance* states. Populate the current master progressively as qualified findings arise; retain explicit dated Excel refresh checkpoints. No AI-generated number of planned iterations can substitute for a documented source-evidence completion gate. [Actual G1 source audit baseline](SOSA_G1_Source_Coverage_Census_09NOV2026.md).

## L22 — Original C239 item-level audit, source support, and progressive master controls (SOSA-G2-1)

C239 §§6.2.3–6.2.5 contain 124 function entries, 71 interaction entries and six binding Rules across two separately scoped interfaces. A source table label **V1.0** or **Future** is not a runtime-observed capability or a profile-approved SHALL; explicit native Rules have their own implementation conditions, and original Appendix B companion schemas still require access. System Manager Rules 6.2.4.3-2/-4 point to B.3 even though the original Appendix B.2 names the System Manager OpenAPI file; keep that conflict local, not silently repaired.

**Reusable practice:** enumerate actual source table entries/Rules and their original page locators, classify normative standing and interface/edition scope, distinguish source-printed input/output types from unread actual API schemas, then incrementally add only source-qualified comparisons to existing master rows. G2-1 updated 12 existing SOSA cells and preserved the other donor/case data while explicitly labeling the 26-sheet XLSX as 12 cells older. Do not equate cross-format integration, source audit, workbook synchronization or DIM/CSAPI Profile acceptance. [Evidence](SOSA_G2_1_Original_Source_and_Master_Correspondence_09NOV2026.md).

