# Smart Citizen execution roadmap

Prepared 24 October 2026. This is the current execution sequence for the Smart Citizen real-source experiment. It complements the maintained research paper and preserves detailed work outside the paper so the paper can remain a readable research narrative.

## Objective

Demonstrate, with traceable evidence, whether useful sensing-system meaning can survive the path from a real producer through an authored adapter and OGC API — Connected Systems service into a standards-aware client, and whether the MERLIN DIM/MPSS profile helps reconstruct a useful Resource Details experience without relying on vendor-specific UI knowledge.

The experiment must preserve the distinction among native source facts, documentary model facts, donor concepts, MERLIN-authored mappings, OGC representation mechanisms, server behavior, client interpretation, and presentation choices. A successful visual result is insufficient unless the displayed meaning can be traced backward through that chain.

## Current baseline

| Area | Current standing |
| --- | --- |
| Source system | Smart Citizen Kit is the first real-source case; public registration 19639 is frozen as formal specimen `20261025T024348Z` |
| Vendor UI baseline | First-party Smart Citizen core-platform and dashboard examples are preserved; they remain historical presentation evidence rather than the formal specimen |
| DIM/Profile | MPSS v0.3.5 remains the technical baseline |
| CSAPI server | Existing Oracle-hosted 52°North connected-systems-pygeoapi deployment is the intended target |
| Client | Glaux Client exists and is deployed; full Smart Citizen connected-resource traversal is not yet implemented |
| Resource Details frame | Recovered 560 × 440 CSS-pixel working canvas is deployed |
| Research paper | Paper v0.10 is the corrective model-currency edition: accepted MPSS v0.3.5 is separated from the wider v0.10 research corpus, Phases 1–4 are audited, and the paper architecture is rebuilt before Phase 5 |
| Completed before Phase 4 | Frozen specimen, complete representative source characterization, corrected vocabulary evidence, reviewed current/aggregate mapping ledger |
| Completed through Phase 4 | Frozen source/characterization retained; mapping ledger and resource graph re-audited against MPSS v0.3.5 plus later research; corrected R15 provenance/process-execution design; no server writes |
| Not yet complete | Phase 5 adapter; server load; connected Glaux retrieval; matched UI comparison |

## Governing sequence

Do not begin adapter implementation by guessing target structures from source labels. Complete and review the source specimen, source inventory, mapping ledger, and proposed CSAPI resource graph first. The adapter should implement reviewed mappings rather than become the place where mappings are invented implicitly.

**25 October current checkpoint:** a proof-level model-currency audit revalidated/corrected Phases 1–4 against MPSS v0.3.5 and the wider research corpus, and paper v0.10 has been rebuilt and fully verified from that audited baseline. Phase 5 deterministic adapter work has not started; it is the next experiment phase when the owner resumes implementation.

### Phase 1 — Freeze the experiment specimen

Reassess public registration 19639 for suitability and current reporting. Capture the complete native device response and bounded history needed for the experiment, recording source URL, query, acquisition time, HTTP result, body hash, and available source-version information.

**Gate:** one reproducible source specimen exists and every publishable excerpt is traceable to retained original evidence.

### Phase 2 — Characterize the native source

Inventory source metadata, identifiers, channel definitions, units, definition URIs, values, timestamps, aggregation metadata, status fields, location/exposure information, and missing or filtered fields. Distinguish platform registrations, catalogue identifiers, association identifiers, and verified physical identifiers.

**Gate:** every source field selected for mapping has a documented native meaning, evidence location, subject hypothesis, time meaning, and known limitation.

### Phase 3 — Build the mapping ledger

For each consequential assertion, document: native source assertion → underlying DIM concept → individual donor concept(s) → MPSS rule/binding → CSAPI/SensorML/SWE carrier → transformation → presentation implication → unresolved issue.

**Gate:** every proposed target assertion has a reviewed semantic rationale and unresolved mappings remain explicit.

### Phase 4 — Design the connected CSAPI representation

Define the resources, relationships, stream/schema structure, observations, provenance, and creation order needed to represent the approved mapping set. Produce a reviewable resource graph before any write to the CSAPI server.

**Gate:** every proposed resource and relationship is evidence-backed and dependencies have a deterministic creation order.

**25 October status:** design gate satisfied for owner review in `Workbook/03_CSAPI_RESOURCE_GRAPH.md`; no server write or adapter implementation performed.

### Phase 5 — Implement the adapter

Implement deterministic replay of the frozen specimen first, then live polling. Preserve original source evidence separately from normalized and target-standard representations, and emit mapping identifiers so transformations remain auditable.

**Gate:** tests show approved source assertions produce reviewed target structures and unsupported content is retained or explicitly excluded according to the mapping decision.

### Phase 6 — Load and verify the CSAPI server

Create resources in dependency order, record assigned server IDs, retrieve every created representation, compare semantic preservation, and verify cleanup/replay procedures. Add live observations only after deterministic resource creation is stable.

**Gate:** the selected dataset survives create/retrieve comparison with its intended meaning and relationships intact within the tested scope.

### Phase 7 — Extend Glaux for connected retrieval

Implement the missing traversal needed to discover and retrieve the System and connected resources required by the experiment. Keep original responses, generic extraction, profile interpretation, and presentation distinguishable.

**Gate:** Glaux can reconstruct selected information from the CSAPI server without reading Smart Citizen native JSON for the operator presentation.

### Phase 8 — Build the Resource Details experiment

Populate the 560 × 440 Resource Details view from the interpreted standardized dataset. Use operator questions and source-supported distinctions to decide presentation; do not copy Smart Citizen pixels or force every DIM subject into a separate tab.

**Gate:** every displayed fact is traceable, unknowns remain qualified, and generic/profile-aware conditions use the same standardized evidence.

### Phase 9 — Perform the comparison

Compare first-party vendor presentation evidence, competent generic OGC presentation, and profile-aware Glaux behavior. Capture matched evidence where possible and label unmatched historical/vendor examples accurately.

**Gate:** the paper can report semantic preservation, domain coverage, and presentation utility separately.

### Phase 10 — Disposition findings

Classify each issue as source limitation, documentation conflict, mapping defect, DIM gap, donor-lineage question, profile gap, server behavior, client behavior, or presentation/PBI issue. Do not silently revise the profile or DIM inside implementation code.

**Gate:** every material finding has an evidence-backed disposition or explicitly open question.

### Phase 11 — Test transferability

Repeat a bounded subset with an independent producer such as AirGradient, then later with hardware the project owns when physical deployment, power, configuration, and lifecycle evidence become the next priority.

**Gate:** reusable DIM/Profile behavior can be distinguished from Smart Citizen-specific adapter work.

## Immediate next steps

1. Retain paper v0.10 as the current research/explanatory baseline and the audited mapping ledger plus Phase 4 resource graph as the semantic implementation baseline.
2. When the owner resumes implementation, begin **Phase 5 only**: implement deterministic replay of the frozen specimen against the audited graph. Do not perform CSAPI server writes or live polling during the deterministic adapter phase.
3. Keep the Phase 4 creation/retrieval/cleanup order authoritative for implementation; code may not silently add resources, subjects, relationships or fallback time semantics.
4. After Phase 5 tests and homework records are complete, pause again for discussion before Phase 6 server loading.

## Milestones

**Milestone A — Reviewed semantic design:** frozen specimen, selected-source inventory, reviewed mapping ledger, and proposed CSAPI resource graph exist before code implementation.

**Milestone B — Standards-preserving integration:** one Smart Citizen representation exists in the 52°North server and selected facts are traceable from native evidence through DIM/donors and MPSS/SensorML/SWE/CSAPI into retrieved server resources.

**Milestone C — Standards-based reconstruction:** Glaux consumes the server representation and produces a useful Resource Details experience without Smart Citizen-specific UI knowledge.

**Milestone D — Transfer evidence:** a second producer reuses enough of the same DIM/Profile and presentation behavior to test generality.

## Supporting records

Detailed phase work is maintained in the experiment workbook under Docs/Research/Studies/Smart_Citizen/Workbook. The research paper should cite or summarize workbook evidence only when it becomes relevant to the research narrative.
