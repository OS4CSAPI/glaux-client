# SAP-02 — Original BSI SAPIENT v2 interface and inner-message source audit

**12 November 2026 · SAP-02 COMPLETE at its authorized bounded original-source scope.** The British Standards Institution (BSI) original *Flex 335 v2.0:2024-03* §§0–5 and Tables 1–14, together with the pinned Defence Science and Technology Laboratory (Dstl) companion source files, have been examined and mapped to the one existing crosswalk. **No SAPIENT donor closeout, DIM/Profile adoption, client changes or SAP-03A work occurred.** The original research state is preserved at [the complete pre-SAP02 branch](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sap02-20261112/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk) (HEAD `894ffe1396844c03543252b20ff0d6a7db6fdd60`). The [same cumulative SAPIENT source coverage/evidence JSON](SAP01_Original_Corpus_Coverage_12NOV2026.json) retains the SAP-01 census and this step's grades, findings and holds.

## What we learned, in ordinary language

**SAPIENT defines operational information relationships, not a single physical sensor architecture.** Its Node can represent sensing, effector, platform or fusion participation; a message `node_id` identifies the sender, not automatically the physical instrument that measured an object. Platform `dependent_nodes` represent consequences for pointing, movement and tasking; hierarchical fusion Nodes describe communication/aggregation, not necessarily mechanically contained instruments. Original BSI §4.10, §4.11 and Figures 3–5 were directly examined, including the original figure pixels for those three diagrams.

**The original transport, identity and command rules have specific scopes.** BSI §4.1/Table 1 defines the sender/destination and oneof wrapper. §4.2 specifies a four-byte little-endian length prefix on the continuous byte stream, not a separate SAPIENT equipment property. §§4.4–4.9 distinguish registration, status, Task, Alert, node shutdown and reconnection; accepting or acknowledging a request does not prove an independent physical effect. The entire later Task/TaskAck schema remains scheduled for SAP-05, rather than being prematurely treated as audited here.

**Location, direction, velocity and linked reports have distinct meanings.** Original BSI Tables 2–11 and pinned `location.proto`, `range_bearing.proto` and `velocity.proto` describe coordinate systems, datums, native units, optional error values and missing-value interpretation. Missing `z` is ambiguous altitude, not zero; absent RangeBearing elevation denotes ambiguity while RangeBearingCone absence has a different source-defined meaning. Table 12/`associated_file.proto` describes linked media by type/URL; Tables 13–14/`associated_detection.proto` describe linked detection reports and fused source identities, not a newly authenticated physical observer or performed OGC Observation.

## Source material actually reviewed

The original BSI publisher PDF pages **9–35** were read at inline-clause/text and original table depth for §§0–5; all **14** original numbered Tables 1–14 were inspected. Original Figure pixels for **Figures 3, 4 and 5** were viewed directly, while **Figures 1, 2 and 6** were read at source text/caption level but **not** declared fully pixel-audited. Six pinned `bsi_flex_335_v2_0` original source files — `sapient_message.proto`, `location.proto`, `range_bearing.proto`, `velocity.proto`, `associated_file.proto` and `associated_detection.proto` — were read at applicable field/enum/comment depth, along with the shared `proto_options.proto`. No actual Protobuf compilation, network test, source-independent producer test or cross-edition equivalence check was performed.

**Stable original-source findings** (standing refers to the original BSI/proto scope, not proposed universal DIM rules):

| Source ID | Original locator | Native standing | Source-qualified original meaning |
| --- | --- | --- | --- |
| **SAP02-N01** | BSI §§0.2–0.4,1 original PDF9–13 | DESCRIPTION | SAPIENT network comprises autonomous sensing/effector edge Nodes, fusion Nodes, optional message handling; no general equipment schema. |
| **SAP02-N02** | BSI §3.1.1–17 PDF15–16 | DEFINITIONS | Node is an architecture module; sensor/fusion/effector, Task and status terms differ; BSI M/D/C requiredness differs from proto field syntax. |
| **SAP02-N03** | BSI §§4.1–4.3 Table1 PDF18–20; sapient_message.proto | SCOPED_SHALL_AND_NOTE | Sender node_id UUID and optional destination_id; oneof message and 4-byte little-endian frame. BSI content timestamp conflicts with pinned proto send timestamp comment. |
| **SAP02-N04** | BSI §§4.4–4.5,4.8–4.9 PDF20–22 | SCOPED_SHALL_AND_ILLUSTRATIVE | Initialization registration/ack/status; task override; GOODBYE reported shutdown, reconnection obligations. Not physical equipment lifetime. |
| **SAP02-N05** | BSI §§4.6–4.7 PDF21 | SCOPED_SHALL | Task and alert requests distinct from acknowledgment/accept-reject; receipt does not independently prove actuation. |
| **SAP02-N06** | BSI §4.10 and Figures3–4 PDF22–23 | DESCRIPTION_AND_PLATFORM_SHALL__FIGURE_PIXELS_READ | Mobile/pointable platform Node declares operationally dependent Nodes; source example does not prove physical part-of. |
| **SAP02-N07** | BSI §4.11 and Figure5 PDF24–25 | SCOPED_HIERARCHICAL_SHALL__FIGURE_PIXELS_READ | Child fusion Node can register to parent as edge participant with aggregated capabilities; network/fusion hierarchy not equipment assembly. |
| **SAP02-N08** | BSI §§5.1–5.2.2.4 Tables2–6 PDF26–29; location.proto | SCOPED_SHALL | Location/LocationList coordinates and datum, optional errors; absent altitude is ambiguous, not zero. |
| **SAP02-N09** | BSI §§5.2.2.5–5.2.5 Tables7–10 PDF30–32; range_bearing.proto | SCOPED_SHALL_AND_FUTURE_NOTE | RangeBearing and RangeBearingCone depend on north datum and coordinate units. Omitted elevation differs by message; platform datum undefined in v2. |
| **SAP02-N10** | BSI §5.3 Table11 PDF33–34; velocity.proto | SCOPED_SHALL__FIGURE6_CAPTION_ONLY | ENU east/north/up velocity and optional error fields; numeric data type not performed event proof. |
| **SAP02-N11** | BSI §5.4 Table12 PDF34; associated_file.proto | SCOPED_SHALL_AND_NOTE | AssociatedFile MIME-style type and URL are links to associated resources, not verified retrieval or original provenance. |
| **SAP02-N12** | BSI §5.5 Tables13–14 PDF35; associated_detection.proto | SCOPED_SHALL_AND_COMMENTARY | AssociatedDetection links timestamps, sender/object IDs and relations, including fused detection contributors; not physical part-of. |
| **SAP02-N13** | BSI §4.3 PDF20; proto_options.proto | VERSION_PROVISION_AND_NATIVE_SOURCE | Standard version file option and custom validation annotations distinct from runtime conformance or formal version negotiation. |

## What cannot be silently 'fixed'

All **six existing SAPIENT `SAP-ISSUE-01` through `06`** remain open, especially original Registration field serial 9/10, BSI content time versus pinned code's send-time comment, the distinct Protobuf optionality/BSI mandatory–discretionary–conditional statuses, middleware/harness limitations and absence of a native OGC mapping. This packet records **five additional narrow source issues** without creating an alternative standard:

| Open issue | Exact original-source problem |
| --- | --- |
| **SAP02-H01** | BSI §5.2.3/Table8 cone extents in radians versus pinned range_bearing.proto comments in degrees; no source-qualified conversion. |
| **SAP02-H02** | BSI §5.5 Table13 associated source node identity vs pinned associated_detection.proto comment saying ULID while is_uuid=true; do not infer equipment identity. |
| **SAP02-H03** | BSI §5.2.5 Table10 PLATFORM bearing datum is explicitly not defined until future edition. |
| **SAP02-H04** | BSI §5.2.2 Table3 x/y eastings/northings vs location.proto longitude/latitude comments; declared coordinate system must control interpretation. |
| **SAP02-H05** | BSI §4.9 original reconnect text says ASM; exact participant referent not resolved in this passage. |

**Two materially important differences:** BSI Table 8 describes certain range-bearing cone angular extents in **radians**, but the pinned source-code comments describe them in **degrees**. The associated-detection `node_id` has an inconsistent source-description/UUID-versus-ULID annotation across original text and code; the published/compiled identifier identity and real-world referent must not be guessed. The BSI source also states that the platform-relative north datum remains undefined for this edition. These caveats cannot become silent unit conversions, persistent hardware identities or mandatory CSAPI Profile fields.

## Actual master and saved Excel work

**17 existing SAPIENT G-column source comparisons** are source-qualified and integrated into canonical `Master_Donor_Concept_to_DIM_Crosswalk.json`, **both** CSV mirrors, **both** GitHub-readable Markdown comparisons, and the **SAME original 26-sheet editable Excel**. No row/topic/column was reordered, no prior donor/case/foundational/DIM cell was replaced, and no DIM classes, fields, cardinalities, mandatory Profile constraints or runtime conformance were adopted.

| Original canonical row ID | Relation | Relevant SAPIENT source IDs |
| --- | --- | --- |
| S06-R004 | RELATED | SAP02-N03 |
| S06-R005 | RELATED | SAP02-N01 |
| S06-R006 | PARTIAL | SAP02-N02, SAP02-N03 |
| S06-R007 | NO_ESTABLISHED | SAP02-N06, SAP02-N07 |
| S06-R008 | RELATED | SAP02-N06 |
| S06-R009 | RELATED | SAP02-N06, SAP02-N07 |
| S06-R014 | RELATED | SAP02-N03 |
| S06-R015 | RELATED | SAP02-N02, SAP02-N12 |
| ISA-T-EVENT-TIME | RELATED | SAP02-N03 |
| ISA-T-EVENT-ID | RELATED | SAP02-N03, SAP02-N12 |
| ISA-C-133 | NARROWER | SAP02-N09 |
| ISA-C-141 | PARTIAL | SAP02-N09 |
| ISA-C-159 | NARROWER | SAP02-N10 |
| ISA-C-146 | PARTIAL | SAP02-N11 |
| ISA-R-MEASUREMENT | NARROWER | SAP02-N08, SAP02-N09, SAP02-N10 |
| S06-R019 | RELATED | SAP02-N05 |
| S06-R020 | RELATED | SAP02-N05 |

**Saved file verification:** [SAP02_Workbook_Validation_12NOV2026.json](SAP02_Workbook_Validation_12NOV2026.json) records an independently read-back XLSX from its staged GitHub commit. The same original 26 sheets remain; **only the Master Crosswalk worksheet XML changed** and the other 42 ZIP entries' compressed payloads/CRC were preserved. Exactly **17 saved G cells** changed. All **346×15 = 5,190 actual saved comparison cell values** matched the updated canonical master and its intended text mirrors; ZIP workbook SHA-256 is `fb18d864dcdd2383e648af081117b57f8924bdf29175dbbfdda921f16d7ded72`, independently calculated with a method first validated against the prior original C4 workbook checksum. **Excel lag is ZERO**. This is a binary/cell-consistency check, not comprehensive original-source completeness.

## Remaining source research and one next boundary

The original BSI Registration family (Tables 15–59: 45 tables) still needs its own source-sized work. The owner-approved source-based forecast moves from **6 low / 7 likely / 9 high remaining Proceeds after SAP-01** to **5 low / 6 most likely / 8 high remaining Proceeds after SAP-02**. We have not invented an extra packet because of the new holds; if any requires substantive added work that changes scope/forecast, the owner must decide before expansion.

**ONE NEXT OWNER `Proceed` authorizes SAP-03A ONLY**, beginning the original BSI §6.2 Registration Tables 15–32 with pinned `registration.proto` and relevant related definitions at source item/field depth, including the previously identified field-number discrepancy. Stop before SAP-03B. The SAPIENT donor remains **ACTIVE/SOURCE-INCOMPLETE** with the original ISA six questions and The Open Group SOSA nine source-hold groups preserved.
