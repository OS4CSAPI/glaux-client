# ISA-03D — Relationship and Visible
**7 November 2026 · COMPLETE: both assigned properties reviewed, integrated and prepared for verified GitHub publication.** Next ISA-03E only.

[Workbook](ISA_Correction_Review_ISA03D_07NOV2026.xlsx) · [Full comparison](ISA_Correction_Review_ISA03D_07NOV2026.md) · [Exact evidence](ISA03D_Relationship_Visible_Evidence_07NOV2026.json) · [Publication](ISA03D_Publication_Record_07NOV2026.json) · [PITON](PITON_ISA_Coverage_Correction_07NOV2026.md).

## Source results
| Native ISA property | Specific candidate information | Source | Result |
|---|---|---|---|
| Relationship | Reported physical parent/child attachment relationships | DMS6.0r12 §3.1, printed p.16/PDF31 | Supported, core |
| Visible | Laser visible-spectrum indication | DMS6.0r12 §3.1, printed p.17/PDF32 | Supported, core |

Relationship has an optional parent and a required child list with **0+** entries, using Relation Link values. A Relation Link contains a required component UCI and required Link value. The sealed Link values **ATTACHED / DETACHED** concern physical attachment, not network connectivity, CIC visibility or authorization. This does not establish an installed assembly, complete parts list or precise spatial transform.

Visible is a Boolean indication that the laser is in the visible spectrum. It is **not the architectural visible/opaque distinction** and does not prove that a laser is firing or supply a measured wavelength or visibility condition. Neither property supplies any values for our equipment cases.

Supporting original definitions: Relationship and Relation Link, printed p.110/PDF125 (text and page image inspected); Link printed p.80/PDF95; Boolean printed p.50/PDF65; prior verified UCI, printed p.55/PDF70, reused. All five dependency entries were already in the47-definition support register; no new unique definitions or future type-catalogue completions are claimed.

## Integrated review
Two source-supported candidate rows are added, one in Position and orientation and one in Imaging and sensing settings. Earlier source meanings and all non-ISA/equipment values remain unchanged. Cumulative coverage: **65 primary entries reviewed, 62 supported outcomes, three unchanged local questions**. The table has **92 information/review rows**: original31 plus58 supported candidates and three questions. ISA-03 package progress:16/42 properties reviewed;26 remain.

The exact earlier questions Level, Link Loss and Orientation remain local to their records. No new question arose. Historical source and workbook checkpoints remain intact; no other donor review or application/CSAPI Profile change occurred.

## Next
ISA-03E only: **Power, Power State, Reserve Capacity and Time to Empty**. No ISA-03E source review was executed in this batch.
