# ISA-02 — identity and first property block

**7 November 2026 · COMPLETE · correction progress 2/12 · next ISA-03 only.**

## Result

All **49 assigned properties** have a recorded source outcome: **47 supported correspondences** and **two precise source-definition questions**. The three known identity gaps are corrected. The earlier UCI comparison is reconciled against the Data Model Specification, Interface Control Document and Component Requirements. Camera Mode provides specific support that the earlier generic Status.properties comparison did not show.

The corrected [horizontal comparison](ISA_Correction_Review_ISA02_07NOV2026.md) and [editable workbook](ISA_Correction_Review_ISA02_07NOV2026.xlsx) now show **43 additional source-supported candidate information rows**, plus two rows preserving the exact Level/Link Loss questions. They are grouped by identity/contacts, placement, operating state, electricity, communications, imaging, diagnostics, security and source-definition questions. These are visible source contributions for owner review, not a new hierarchy or automatically accepted requirements.

## Existing-row corrections

| Existing DIM row | Source-native ISA result | Fit and reason |
|---|---|---|
| Manufacturer name | Manufacturer | Partial: ISA allows manufacturer, producer **or vendor**. |
| Product model designation | Model | Direct for the same component/product-model subject. |
| Individual hardware serial number | Serial Number | Partial: apply to a physical component; uniqueness is described using the manufacturer/model/serial combination. |
| Persistent System identifier | UCI | Existing partial mapping retained, meaning corrected: component uniqueness is not merely network-scoped. |
| Source-reported operating mode | Camera Mode | Narrower, camera-specific support; whole-row reconciliation continues in ISA-03. |


All 49 properties were read in DMS 6.0r12 §3.1: printed pp.9–13 / PDF pp.24–28, plus Model at printed p.14 / PDF p.29 and Serial Number at printed p.16 / PDF p.31. Cross-page continuations were included, especially Camera Mode. **46 properties are core entries; Hardware Version, Maintenance and Manufacturer POC are accepted extensions** in this edition. The body markings and original extension legend control that distinction, not the bullets in the contents.

## Important findings from actual definitions

**Maintenance is a contact list**, not a maintenance history or performed service event. **Identity is tactical classification** through Standard Identity, not a unique component identifier. **Active reports operation; Enabled reports permission to become active.** **Data Outputs concerns data being transmitted**, not simply an output-field definition or a catalogue of available resources.

Parent-relative Attached Position/Orientation and own-frame Local Position/Orientation are separate concepts with an explicit transform order. Field of Regard covers the scan-wide view, whereas Field of View is instantaneous; both use a typed angular structure. Current AC/DC current and voltage preserve source/load roles instead of becoming a generic battery-state property. These distinctions remain visible in the new rows and their source evidence.

Forty-six supporting type definitions were inspected for these comparisons. Their native fields, relevant cardinalities and constraints are recorded in the [evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json) and workbook Dependencies tab. Supporting reads are **not double-counted as completion of their later full catalogue-review passes**. For example, the UTC source declares a required Secs value and optional Secs error; no nanoseconds field is invented.

## Two record-local questions

**ISA-Q001 — Level.** The property entry declares a Percent single value but supplies no descriptive prose. Related Adjust Level and Change Level commands describe a relative setting; Auto Level refers to pixel adjustment. The exact referent of the separate Level property remains a named interpretation question, not a license to map it to battery charge, brightness or an absolute physical quantity.

**ISA-Q002 — Link Loss.** The property entry declares Db, but does not identify its reference quantity or sign convention. The Db type establishes a logarithmic ratio, not packet-loss percentage or a particular propagation-loss definition. Its native term and type remain visible, with the missing reference precisely identified for the assigned follow-up.

These two entries have been reviewed and their specific questions recorded. They do not reopen completed work on the other 47 properties.

## Complete assigned-entry disposition list

| Inventory ID | Exact ISA property | Source standing | Existing/candidate row | Relation/outcome |
|---|---|---|---|---|
| ISA-DMS-031 | AC Current Load | Core | ISA-C-031 — Consumed AC current | DIRECT |
| ISA-DMS-032 | AC Current Source | Core | ISA-C-032 — Produced AC current | DIRECT |
| ISA-DMS-033 | AC Voltage Load | Core | ISA-C-033 — Load-side AC voltage | DIRECT |
| ISA-DMS-034 | AC Voltage Source | Core | ISA-C-034 — Source-side AC voltage | DIRECT |
| ISA-DMS-035 | Active | Core | ISA-C-035 — Reported activity flag | DIRECT |
| ISA-DMS-036 | Armed | Core | ISA-C-036 — Reported arming state | DIRECT |
| ISA-DMS-037 | Attached Orientation | Core | ISA-C-037 — Orientation relative to attached parent | DIRECT |
| ISA-DMS-038 | Attached Position | Core | ISA-C-038 — Position relative to attached parent | DIRECT |
| ISA-DMS-039 | Auto Brightness | Core | ISA-C-039 — Automatic brightness enabled | DIRECT |
| ISA-DMS-040 | Auto Contrast | Core | ISA-C-040 — Automatic contrast enabled | DIRECT |
| ISA-DMS-041 | Auto Focus | Core | ISA-C-041 — Automatic focus enabled | DIRECT |
| ISA-DMS-042 | Auto Gain | Core | ISA-C-042 — Automatic gain enabled | DIRECT |
| ISA-DMS-043 | Auto Level | Core | ISA-C-043 — Automatic pixel-level adjustment enabled | DIRECT |
| ISA-DMS-044 | Auto Scan | Core | ISA-C-044 — Automatic scanning enabled | DIRECT |
| ISA-DMS-045 | Brightness | Core | ISA-C-045 — Current brightness level | DIRECT |
| ISA-DMS-046 | Built In Test Result | Core | ISA-C-046 — Latest built-in-test reported result | DIRECT |
| ISA-DMS-047 | Camera Mode | Core | S06-R018 — Source-reported operating mode | NARROWER |
| ISA-DMS-048 | Capability Version | Core | ISA-C-048 — Component configuration version | DIRECT |
| ISA-DMS-049 | Charged | Core | ISA-C-049 — Reported charged flag | DIRECT |
| ISA-DMS-050 | Contrast | Core | ISA-C-050 — Current contrast percentage | DIRECT |
| ISA-DMS-051 | Crypto Filled | Core | ISA-C-051 — Cryptographic-key-filled flag | DIRECT |
| ISA-DMS-052 | DC Current Load | Core | ISA-C-052 — Consumed DC current | DIRECT |
| ISA-DMS-053 | DC Current Source | Core | ISA-C-053 — Produced DC current | DIRECT |
| ISA-DMS-054 | DC Voltage Load | Core | ISA-C-054 — Load-side DC voltage | DIRECT |
| ISA-DMS-055 | DC Voltage Source | Core | ISA-C-055 — Source-side DC voltage | DIRECT |
| ISA-DMS-056 | Data Inputs | Core | ISA-C-056 — Current incoming data transfers | DIRECT |
| ISA-DMS-057 | Data Outputs | Core | ISA-C-057 — Current outgoing data transfers | DIRECT |
| ISA-DMS-058 | Enabled | Core | ISA-C-058 — Permission-to-become-active flag | DIRECT |
| ISA-DMS-059 | Eye Safe Distance | Core | ISA-C-059 — Minimum eye-safe distance | DIRECT |
| ISA-DMS-060 | Field of Regard | Core | ISA-C-060 — Current scan-wide angular coverage | DIRECT |
| ISA-DMS-061 | Field of View | Core | ISA-C-061 — Current instantaneous angular coverage | DIRECT |
| ISA-DMS-062 | Focus | Core | ISA-C-062 — Current focus level | DIRECT |
| ISA-DMS-063 | Frame Rate | Core | ISA-C-063 — Video frame rate | DIRECT |
| ISA-DMS-064 | Frequencies | Core | ISA-C-064 — Emission frequencies in use | DIRECT |
| ISA-DMS-065 | Ground Intercept | Core | ISA-C-065 — Pointing-vector ground intersection | DIRECT |
| ISA-DMS-066 | Hardware Version | Accepted Extension | ISA-C-066 — Component hardware version | DIRECT |
| ISA-DMS-067 | IP Addresses | Core | ISA-C-067 — Network-interface IP addresses | DIRECT |
| ISA-DMS-068 | Identity | Core | ISA-C-068 — Tactical identity classification | DIRECT |
| ISA-DMS-069 | Iris Size | Core | ISA-C-069 — Current iris opening percentage | DIRECT |
| ISA-DMS-070 | Level | Core | ISA-C-070 — Level value — meaning question | UNRESOLVED_MEANING |
| ISA-DMS-071 | Link Loss | Core | ISA-C-071 — Link Loss value — reference question | UNRESOLVED_MEANING |
| ISA-DMS-072 | Link State | Core | ISA-C-072 — Network-interface up/down state | DIRECT |
| ISA-DMS-073 | Local Orientation | Core | ISA-C-073 — Orientation offset in own frame | DIRECT |
| ISA-DMS-074 | Local Position | Core | ISA-C-074 — Position offset in own frame | DIRECT |
| ISA-DMS-075 | Maintenance | Accepted Extension | ISA-C-075 — Maintenance point of contact | DIRECT |
| ISA-DMS-076 | Manufacturer | Core | S06-R001 — Manufacturer name | PARTIAL |
| ISA-DMS-077 | Manufacturer POC | Accepted Extension | ISA-C-077 — Manufacturer point of contact | DIRECT |
| ISA-DMS-080 | Model | Core | S06-R002 — Product model designation | DIRECT |
| ISA-DMS-105 | Serial Number | Core | S06-R003 — Individual hardware serial number | PARTIAL |

## Preservation and checks

The 31 original DIM/case topics and every original non-ISA/equipment display cell remain intact. The original 58 non-ISA donor correspondences and 73 equipment evidence statements were not rewritten. The historical v0.9 master and ISA-01 files remain unchanged. The corrected ISA view contains **76 information/review rows**: the original 31, 43 new source-supported candidates, and two source-question rows.

All 49 assigned IDs are accounted for once; no ISA-03 entry was closed as primary work. Four identity row targets and one earlier UCI record are reconciled; the camera-specific contribution is recorded without declaring the whole later mode review complete. Workbook formulas, source/CSV/JSON agreement, ZIP/XML integrity and original-cell preservation pass; the summary and comparison were visually inspected. Requested original PDF page images were unavailable through Files; original indexed text and explicit body/extension markers were inspected, and no source-image inspection is claimed.

The [validation record](ISA02_Validation_07NOV2026.json), [coverage register](ISA_Coverage_Register_07NOV2026.json) and publication record distinguish source work, workbook checking and committed-file verification. The four case examples were used to challenge meanings, not to invent source equipment values.

## Original sources

Program Executive Office Intelligence, Electronic Warfare and Sensors. 2023. *ISA Data Model Specification*. Release 6.0, revision 12. October 31. §3.1; referenced §4 and §8 types; extension legend.

Program Executive Office Intelligence, Electronic Warfare and Sensors. 2023. *ISA Interface Control Document*. Document 6.0, revision 5. October 31. §6.1, printed p.19 / PDF p.27.

Program Executive Office Intelligence, Electronic Warfare and Sensors. 2023. *ISA Component Requirements*. Document 6.0, revision 4. October 31. §4.1.1, printed pp.7–9 / PDF pp.14–16.

## Next task

**ISA-03 only:** review the **42 remaining properties**, including Zones and Zoom on printed p.18. Model and Serial Number already belong to ISA-02 and must not be counted twice. The source ledger and readable comparison are the starting point; no ISA-04 or Step16 work begins automatically.


## Repository verification

[Publication record](ISA02_Publication_Record_07NOV2026.json) · [Read-only verification of the published commit](https://github.com/OS4CSAPI/glaux-client/actions/runs/42392228728). The correction remains 2/12; next ISA-03 only.
