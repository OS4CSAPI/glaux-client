# SAP-01 — original SAPIENT v2 source census, coverage and finish-line forecast

**12 November 2026 — SAP-01 completed at corpus-inventory depth.** The owner explicitly gave two "Proceed"s and said to start, authorizing the revised plan and this **one bounded SAP-01 step**. SAPIENT remains **ACTIVE, source audit incomplete**; this is not a second source-semantic packet or a donor-closeout decision. The full stable source ledger (58 original numbered contents entries, 97 table IDs, 16 pinned protocol files and shared options) is [SAP01_Original_Corpus_Coverage_12NOV2026.json](SAP01_Original_Corpus_Coverage_12NOV2026.json). [Browse the complete pre-SAP01 version](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-crosswalk-pre-sapient-sap01-20261112/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/).

## What was actually verified

The British Standards Institution's original **BSI Flex 335 v2.0:2024-03** interface specification contains **116 PDF pages**, original numbered main clauses **0–7**, **four explicitly informative Annexes A–D**, and **97 numbered main tables** plus a separate Annex C.1 table. Original publisher front matter, edition, table of contents, table index, introduction, scope, explicit absence of normative references (§2) and selected original definitions were accessed at targeted indexed-text depth from the user-provided Library original. A later attempt to reopen the PDF failed, so no raw-byte SHA or full-body review is asserted. **Inventorying an original title or table does not mean reading and validating its requirements.**

All **16** source `.proto` files from the [official pinned Dstl v2 directory](https://github.com/dstl/SAPIENT-Proto-Files/tree/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0) were fetched as original GitHub text and structurally scanned, totaling **62 message declarations and 31 enum declarations** across those files (some nested/duplicated names). The repository also has the shared imported `proto_options.proto`, inspected at structural depth; it is not a seventeenth independently normative standard. **Eight** proto files had earlier selected source/semantic checks, and **eight** had not; this step establishes original-file structural contact, **not a complete field/enum/Rule audit in any of the sixteen**. No protobuf compilation, source system behavior or interoperability test occurred.

The [earlier SAPIENT native-source challenge](../Donor_Challenge/02_SAPIENT_Challenge.md) contains narrow original § and field checks, including selected visual Tables 15, 24, 32, 63 and 86–87. Its six original `SAP-ISSUE-##` holds (Registration field-number inconsistency; content versus sent time; BSI requiredness versus proto syntax; middleware cache/routing; harness limits; unestablished source-authored CSAPI/OMS equivalence) are still open. A reported SAPIENT Node does not automatically establish installed physical equipment; Task acknowledgement does not independently demonstrate a physical result.

## Which original sources account for the remaining work?

| Original BSI Table IDs | Family | Source tables | Printed family page span | Proposed packet |
| --- | --- | ---: | --- | --- |
| 1–1 | Envelope | 1 | 7 | SAP-02 |
| 2–14 | Inner messages | 13 | 15–23 | SAP-02 |
| 15–32 | Registration core | 18 | 25–36 | SAP-03A |
| 33–59 | Registration nested definitions | 27 | 37–51 | SAP-03B |
| 60–68 | Status | 9 | 52–57 | SAP-04 |
| 69–77 | Detection | 9 | 58–64 | SAP-04 |
| 78–87 | Task and TaskAck | 10 | 65–72 | SAP-05 |
| 88–95 | Alert, AlertAck, Error | 8 | 73–77 | SAP-05 |
| 96–97 | Taxonomy | 2 | 80–83 | SAP-06 |
| **1–97** | **Total** | **97** | **7–83** | **TOC/table index count, not 97 audits** |

**Registration is the heaviest identifiable original unit: Tables 15–59 contain 45 of the 97 BSI tables.** Its nested schema definitions and constraints justify planning two source-sized increments. The rest separates the interface/envelope and inner messages, status/detection, task/ack/alert/error, and taxonomy with informative annexes. The ledger identifies each original section by `SAP-BSI-<section>`, each table `SAP-BSI-T001` through `T097`, and each original v2 proto by `SAP-PROTO-01` through `16`, with its actual GitHub blob ID. Later steps must identify the finer native clauses/field options and source standing; any not yet examined is **UNREVIEWED**, not absent.

## Source-based forecast — after SAP-01

**LOW 6 / MOST LIKELY 7 / HIGH 9 additional substantive Proceeds** remain, including final cross-format evidence, unchanged-or-refreshed SAME Excel validation and the owner donor-disposition gate. With this completed SAP-01, that means **7–10 total** at this stage. The earlier 6–10 was an unvalidated conversational allowance; the forecast now has a concrete original-corpus basis. These are **not artificial fixed packet quotas** or a promise of complete BSI source coverage irrespective of access.

| Source-sized proposed packet | Original evidence to examine | Complexity |
| --- | --- | --- |
| **SAP-02** | BSI introduction/terms and §§4–5, Tables 1–14; envelope/location/range/bearing/velocity/associated-file protos + shared options | medium |
| **SAP-03A** | BSI §6.2 Registration Tables 15–32: Node, capabilities, mode, configuration; registration proto | high |
| **SAP-03B** | BSI §6.2 Registration Tables 33–59: detection/task/dependent definitions; registration proto | high |
| **SAP-04** | BSI §§6.3–6.4 Status/Detection Tables 60–77; status/detection source protos | medium-high |
| **SAP-05** | BSI §§6.5–6.7 Task/Alert/Error Tables 78–95; task/ack/alert/error/follow protos | medium-high |
| **SAP-06** | BSI §7 Taxonomy and Annexes A–D, Tables 96–97 and informative Table C.1; version/source issues | medium |
| **SAP-07** | Source/meaning coverage gate, existing master/26-sheet Excel parity, plain-English synthesis and owner disposition | conditional medium |

The **low** case allows consolidation of source-neighbor packets when justified by inspected complexity, and the **high** case allows roughly two added original-source packets or issue-resolution checks. Every later authorized step must report its *actual* original source units audited by grade, master/Excel changed cells or exact lag, unresolved holds, and a revised low/likely/high remaining count. Material growth (two Proceeds or around 25%) or any meaningful method/scope change requires an owner choice; do not create endless automatic follow-up packets or rush a false complete conclusion.

## Canonical crosswalk, provenance and STOP

**SAP-01 warranted no new donor-to-DIM row mapping.** The canonical one JSON, both CSV mirrors, both GitHub-readable Markdown comparisons and SAME original editable **26-sheet Excel** are unchanged from C4, with previously independently verified **346×15 actual saved comparison cells, exact lag zero**. This is inherited C4 parity, not a new SAP01 Excel audit. The prior six ISA source-definition questions and nine The Open Group SOSA grouped source holds remain binding; no universal chassis, DIM class/field/cardinality, CSAPI Profile SHALL, physical tasking or client/deployment activity was adopted.

**ONE NEXT OWNER "Proceed" = SAP-02 ONLY.** Source-first review of the original BSI introduction/definitions and interface/inner-message clauses **0–5**, source Table IDs **1–14** and relevant original pinned protobufs/shared options, at actual clause/field/Rule depth. Integrate any warranted source-qualified comparisons into the **same** canonical crosswalk and SAME Excel at substantive checkpoints, update the source coverage/remaining forecast, then STOP before the first registration packet SAP-03A.
