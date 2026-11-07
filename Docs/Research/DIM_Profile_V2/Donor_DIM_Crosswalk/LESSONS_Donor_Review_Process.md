# Donor review — lessons and reusable practices

**7 November 2026 · Living record, updated after ISA-02 and workload resizing.** ISA-01 and ISA-02 remain complete. **Next technical task: ISA-03C, four position/orientation properties only.** The former twelve-prompt estimate is withdrawn; the twelve existing work-package labels now execute through bounded child batches. This is an ISA-only correction, not another donor review.

[Current PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) · [Revised execution plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress and exact child batches](ISA_Correction_Status_07NOV2026.json) · [ISA-01 census](ISA01_Source_Census_07NOV2026.md) · [Current ISA review](ISA_Correction_Review_ISA03B_07NOV2026.md).

## How to use and maintain this record

Add or change a lesson only when ordinary research supplies evidence. Record what happened, the evidence, the resulting practice and where it applies. Do not produce another lessons report after every prompt. The PITON links here instead of duplicating the history.

**Observed** means the event occurred in this project. **Demonstrated benefit** means the practice produced a particular observed improvement. **Under test** means the proposed safeguard has not yet been exercised through the relevant review. These are evidence descriptions, not permanent grades or universal rules.

At ISA-12, consolidate demonstrated practices into a reusable donor-review procedure and starter template. Adapt the process to the next donor's source form. ISA's work-package structure and batch count are not mandatory for another standard. A later finding can refine a practice without erasing completed work.

## Initial lessons

| ID | What happened and evidence | Reusable practice | Applicability and present standing |
| --- | --- | --- | --- |
| **L01 — Start with the source inventory** | The earlier eleven-concept selection omitted Manufacturer, Model and Serial Number. Their DMS 6.0r12 definitions occur at printed pp.13, 14 and 16. ISA-01 then registered 480 named entries from contents, body headings and index. See [census](ISA01_Source_Census_07NOV2026.md) and [inventory](ISA_DMS_Entry_Inventory_07NOV2026.csv). | Build the checklist from the source, compare against DIM rows, and ask what relevant content needs new rows. Do not select only familiar or architecturally interesting concepts. | **Omission observed; inventory benefit demonstrated.** Adapt enumeration to catalogues, schemas, ontologies or actual source structure. An inventory is not semantic verification. |
| **L02 — Make empty cells intelligible** | A blank manufacturer cell was reasonably read as possible absence. ISA-01 replaced twenty empty cells with review state and assigned pass while retaining eleven earlier terms. | Separate review coverage, mapping relationship and owner acceptance. Distinguish Not reviewed, a precise Question, and No correspondence found in a named scope. | **Ambiguity observed; display improvement delivered.** A blank or failed keyword search is not donor absence. |
| **L03 — Follow entries across page boundaries** | Zones and Zoom continue on printed p.18; Solar Radiation, Velocity and Verified By on p.22. Approximate planning ranges would have missed them. See [boundary amendment](ISA01_Plan_Amendment_07NOV2026.md). | Assign named entries, reading definitions to completion. Page ranges navigate; they do not define the complete scope. | **Demonstrated benefit.** Applies to shared pages, continued tables and split schema definitions. |
| **L04 — Check coverage separately from consistency** | Step15 workbook/evidence parity passed despite omitted identity properties. ISA-01 reconciled source contents/body/index independently of populated cells. | Validate source coverage as well as file parity. Start the final semantic audit from original definitions and inventory, not two generated artifacts. | **Prior limitation observed; census reconciliation demonstrated.** Full semantic closeout remains under test until its audit. Automated checks cannot certify meaning. |
| **L05 — Bound work by assigned source content** | The selected eleven mappings had no complete remaining-work inventory. ISA-01 assigned 480 entries, 279 source blocks, 31 row/topic targets and 25 earlier findings. | Define exact source assignments; split oversized work without dropping entries. Do not substitute a mapping quota for coverage. | **Inventory benefit demonstrated; original batch sizing failed at ISA-02. See L10.** These record categories are not additive concept totals. Parent source-block ownership alone is not prompt sizing. |
| **L06 — Keep unknowns and completed work local** | The census completed before publication; the owner warned against later chats treating broad caution as a reason to reopen everything. | Attach uncertainty to its exact record, evidence and next action. Distinguish review, acceptance and publication. Reopen for new evidence, not an old blanket caveat. | **Workflow problem observed; continuity rule established.** No permission to conceal unread sources or unsupported claims. |
| **L07 — Publish to the actual repository** | ISA-01 was delivered sandbox-only; the user repeated the GitHub requirement. An interrupted upload was not a published checkpoint. | Commit to the designated branch, update recovery pointers and read back actual content. Sandbox copies supplement GitHub. Discover available supported writes before declaring publication unavailable. | **Delivery failure observed; recovery verified separately.** No unsupported attribution to a model switch. Publication repair must not cause completed research to be repeated. |

## Verified publication recovery — historical ISA-01 checkpoint

The interrupted ISA-01 transfer resumed from ten exact matching segments; original file hashes were checked before publication-label and recovery-routing updates. See [publication record](ISA01_Publication_Recovery_07NOV2026.json) and [verification run](https://github.com/OS4CSAPI/glaux-client/actions/runs/42388276114). This closed the particular GitHub-delivery action in L07. Its then-next ISA-02 has since completed; current progress controls the handoff.

## Evidence added at ISA-02

| ID | Observation and evidence | Reusable practice | Standing |
| --- | --- | --- | --- |
| **L08 — Read the native definition, not just the label** | DMS §3.1 makes Maintenance a contact list, Identity a tactical classification and Data Outputs an ongoing-transfer description, not maintenance history, persistent identity or a field schema. See [ISA-02 evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json). | Follow the actual type and meaning before matching an existing row. Preserve particular source contributions instead of forcing similar labels together. | **Demonstrated in ISA-02.** Applied to its 49 properties and separate UCI reconciliation. |
| **L09 — Preserve source standing and isolate sparse definitions** | Body text identifies three accepted extensions. Level and Link Loss have declared types but lack defining prose; cross-page Camera Mode and measured-type definitions add qualifications. | Verify source standing in the body, follow cross-page/type dependencies, and isolate a precise question instead of inventing a meaning or reopening unrelated completed work. | **Demonstrated in ISA-02.** 46 core properties, three accepted extensions, two local questions; that assigned review is complete. |
| **L10 — Size the entire prompt, not just the source heading block** | ISA-02 combined 49 primary properties, 46 supporting definitions, 45 added information/question rows, UCI reconciliation, workbook preparation, checks and publication. The owner challenged the oversized effort despite the explicit request for manageable one-prompt steps. The earlier plan allowed splits, but none was applied before starting. See [ISA-02 publication record](ISA02_Publication_Record_07NOV2026.json) and the [revised plan](PLAN_ISA_Coverage_Correction_07NOV2026.md). | Preflight exact inputs, dependencies, affected rows, checks and publication. Begin with 4–6 simple definitions or 1–3 dense items, with at most four newly inspected supporting definitions and six new/materially changed information rows. Split before exceeding the budget, retaining every remaining entry. Reuse verified evidence and stable publication machinery; no new exporter project inside a semantic pass. | **Oversized workload observed. Smaller ceilings newly established, to be calibrated by actual batch delivery.** Counts are guardrails, not guarantees or completion quotas. The earlier platform error's cause has not been diagnosed. Twelve work packages are no longer represented as twelve prompts. |

## What the sizing correction changes

All 42 remaining ISA-03 properties are assigned once across ISA-03A–J, with 2–6 primary entries per batch and a mandatory dependency/output check before execution. The next batch contains only Maximum Status Interval, Minimum Status Interval, Name and Operating State. No source entry was removed and no completed ISA-02 interpretation was changed to justify the smaller schedule.

A normal batch reserves effort for source checking, the actual table update and verified GitHub publication. If publication fails, allow one bounded repair attempt; otherwise stop adding source work, preserve exact evidence through a supported write route and make the particular repair a separately named action. Do not drift into an unbounded debugging loop or claim an unverified delivery. This is a process safeguard, not a diagnosis of the platform failure.

The remaining work packages use the same bounded-child approach, including architecture reconciliation and the final audit. Keep scope completeness and prompt sizing separate: all entries stay tracked, while one prompt handles only its named subset. Completion remains earned for that subset; it does not automatically complete the parent package.

## Practices still being tested

Calibrate small-batch sizes from actual source and publication workload. Test presentation of one-to-many/many-to-one relations and useful additional/split rows without forcing a universal table granularity. The equipment cases challenge interpretations but do not restrict discovery to their features. Keep core/extension standing distinct. Do not promote the new numerical ceilings into permanent scientific truths.

## Update schedule

**During source batches:** record a brief lesson only for new evidence, as part of ordinary closeout. **At ISA-12:** consolidate demonstrated practices into a reusable procedure/template. **At the next donor:** adapt that procedure to its source structure rather than copying ISA's package or prompt count.

**Current checkpoint:** ISA-01 and ISA-02 remain complete. This sizing amendment changes planning/recovery documentation only. **Next technical task: ISA-03A only.**


## ISA-03A integration closeout

The four saved decisions were integrated without repeating their source review. The existing GitHub Actions artifact-download route supplied the exact current workbook after public raw-download attempts failed. Input/output hashes, original-row preservation and the actual published commit are checked in [the publication record](ISA03A_Publication_Record_07NOV2026.json). This is an application of L06/L07, not a new donor-review method. ISA-03A is complete; next ISA-03B only.


## ISA-03B application of existing practices

The six-entry batch reused existing POC/String support and preserved distinct owner, program-of-record and non-maintenance-support roles, plus three different version meanings. Five source entries retained Accepted-extension status. This applies lessons L08/L09; no new universal rule or additional research campaign is introduced. [Evidence](ISA03B_Ownership_Versions_Support_Evidence_07NOV2026.json).

## ISA-03C — preserve a source's role without inventing its numerical convention

The original Orientation entry names one reference frame and also describes specific axes; its world-orientation role is clear, but an exact numeric frame mapping needs clarification. The correction keeps the native property visible with ISA-Q003 rather than deleting the concept or silently choosing a transform. See [source decisions](ISA03C_Position_Orientation_Evidence_07NOV2026.json). Likewise, an optional hardware-perceived position does not become mandatory whenever override is supported, and source defaults are not measured accuracy.

**Demonstrated practice:** record the supported information role and the specific unresolved representation constraint separately; reuse reviewed dependencies and do not turn a local question into a project-wide failure state. Active progress fields were also checked for stale “pending integration” instructions and corrected; historical reports stay unchanged. **Next technical task: ISA-03D only.**
