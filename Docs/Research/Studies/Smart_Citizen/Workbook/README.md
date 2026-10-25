# Smart Citizen experiment workbook

This folder is the living engineering/research workbook behind the Smart Citizen experiment. It holds detailed homework that would make the research paper unreadable if copied into the main narrative: exhaustive source inventories, mapping decisions, resource-graph design, execution records, discrepancy classification, and transferability notes.

The workbook does not replace the paper, MPSS profile, DIM research, or implementation code. It records the evidence and reasoning that support those artifacts.

## Workbook records

| Phase | Record | Purpose |
| --- | --- | --- |
| 1–2 | 01_SOURCE_SPECIMEN_AND_INVENTORY.md | Freeze the native dataset and characterize what the producer actually supplies |
| 3 | 02_MAPPING_LEDGER.md | Explain each source→DIM→donor→MPSS→OGC mapping and its limits |
| 4 | 03_CSAPI_RESOURCE_GRAPH.md | Design connected target resources and creation dependencies before coding |
| 5–7 | 04_EXECUTION_LOG.md | Record adapter, server, and Glaux executions with exact revisions and evidence |
| 8–10 | 05_EVALUATION_AND_FINDINGS.md | Record UI/PBI evaluation, discrepancies, and dispositions |
| 11 | 06_TRANSFERABILITY.md | Compare a second producer against the same concepts and behavior |
| Corrective audit | 06_MODEL_CURRENCY_AUDIT.md | Prove Phase 1–4 currency against MPSS v0.3.5 and the later research corpus; record retained decisions and required corrections before Phase 5 |
| All phases | DECISIONS.md | Preserve material scope, mapping, implementation, and interpretation decisions |

## Evidence rules

- Keep native evidence separate from reviewed excerpts and derived representations.
- Record exact source locations, timestamps, revisions, and hashes where available.
- Distinguish source-reported facts, model-level documentation, integration-created facts, and unresolved interpretations.
- Do not use a successful server write as proof of semantic correctness.
- Do not use a polished UI as proof that the DIM/Profile contributed useful meaning.
- Preserve conflicts and record their disposition instead of silently choosing the convenient value.

## Relationship to the paper

The paper should summarize method, representative mappings, important evidence, results, and implications. The workbook may contain many more rows, intermediate failures, alternative mappings, diagnostic requests, and rejected ideas than belong in the paper.

A workbook item becomes paper evidence only when its standing is clear enough to cite or summarize. The paper should link to the relevant workbook record or stable evidence artifact when detail materially supports a claim.

## Status

Phases 1–4 have now undergone a **corrective model-currency audit** against the actual MPSS v0.3.5 baseline and the wider donor/research corpus. The frozen source evidence and most semantic decisions are retained; the Phase 4 graph is corrected to use R15 representation-source provenance and to distinguish the persistent aggregate Process System, reusable Procedure and query/execution provenance. No CSAPI write, adapter implementation, Glaux change, application deployment or profile revision has occurred. Phase 5 remains blocked until the v0.10 corrective paper, current-work/roadmap records, and publication verification are complete.
