# Donor Alignment — Step 01: Frozen Corpus Baseline and Exceptions

**Date:** 28 October 2026  
**Execution:** Step 01 of [Controlled Donor Alignment and Foundational DIM Plan v0.1](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md)  
**Status:** **COMPLETE at the artifact-ID, citation and existing-classification metadata level only**; original standards/editions were **not** independently reread or revalidated.  
**Repository/branch:** `OS4CSAPI/glaux-client` / **`research/dim-profile-v2`**, pre-Step-01 branch HEAD `d28db958e2c63837f0d2d2f72089e8c75fc1f6e5`.  
**Standing:** Read-only reconciliation report; **no changed donor records, accepted DIM classes/modules, donor-equivalence claims or Profile requirements**. Continue one bounded step per owner `proceed`.

## 1. Exactly what was checked

Three complete **182-row CSV inventories** were read from the same research branch and parsed as quoted CSV (including embedded commas). Their frozen Git blob identities, row IDs and fields are:

| Role in this review | Existing source (not edited) | Git blob SHA |
| --- | --- | --- |
| **Frozen artifact ID, citation, primary/secondary type** | [Source-Type Assessment v0.1, 25 October](../DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv) | `c94ceded9eaea2efa97fe9a153779b2e9651ffb3` |
| **Historical anatomy-lineage associations and structural triage** | [Phase 0 182-Source Ledger v0.1, 26 October](../DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv) | `e9561a24dc5dc2388998eb8f9794e9204eb431a5` |
| **Historical corpus-wide chassis challenge/disposition** | [Chassis 182-Source Audit v0.1, 25 October](../DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv) | `5b93918a5bb82c33cd4a1bf920206b37cfa1be57` |

The [source-type-grouped bibliography v0.5](../DIM_Profile_V2_Candidate_Donor_Bibliography_Source_Type_Grouped_v0.5_25OCT2026.md) and [original provenance-grouped bibliography v0.4](../DIM_Profile_V2_Candidate_Donor_Bibliography_Grouped_v0.4_25OCT2026.md) were also crosschecked against the citation strings from the ID-bearing source-type CSV. We compared editorial grouping with the recorded primary source type, **not** just the count of bibliography entries.

**Checks performed:**

| Mechanical check | Observed result |
| --- | --- |
| Parse all three 182-row CSV files and validate column counts | **3/3 parse correctly**, no field-count failures |
| Exact distinct IDs per file | **182 each**, exact set **1–182**, no missing or duplicate IDs |
| Per-ID `citation`, `primary_type`, `secondary_type` between all three ledgers | **182/182 exact agreement** for all three compared fields |
| Citation presence and primary type in each CSV | **No blank citations or blank primary types** |
| Optional `secondary_type` | **134 blank in each ledger**, consistently; blank is a permitted optional field, not 134 missing identities |
| Exact citation text in bibliography v0.5 | **182/182 present exactly once**, no unmatched/duplicated citation entries |
| Exact citation text in older bibliography v0.4 | **182/182 present**; different organizational grouping, not a different artifact population |
| Bibliography v0.5 grouped placement vs CSV `primary_type` | **7 exceptions among 171 non-foundational entries** — see §3; no source record changed |

**Conclusion at this scope:** **No ID, citation-text or primary/secondary-type mismatch exists among the three CSV ledgers**. This is a strong starting point for a stable crosswalk, **not** verification that each original source exists, that its metadata is an authoritative statement by a standards body, or that the classification of every artifact is semantically correct.

## 2. Frozen corpus structure and what the counts do—and do not—mean

The source-type inventory's 13 primary classes account for all 182 artifacts:

| Primary artifact type, as frozen | Rows |
| --- | ---: |
| Data model / schema / encoding / exchange format | 38 |
| Guidance / explanatory / research / training | 30 |
| API / interface / protocol / service specification | 29 |
| Modeling / packaging / versioning / conformance methodology | 15 |
| Conceptual / information / domain model | 14 |
| Vocabulary / terminology / units / code list / registry | 13 |
| Ontology / formal semantic model | 9 |
| Reference architecture / architectural framework | 8 |
| Implementation / test / executable companion artifact | 6 |
| Requirements / capability / operational specification | 6 |
| Policy / standards registry / strategy / governance | 5 |
| Reference system / product / operational evidence | 5 |
| Profile / specialization / application model | 4 |
| **Total** | **182** |

**Important distinct classifications:**

- **Phase 0 anatomy screen:** `ADMIT — core structural donor` **29**, `ADMIT — cross-cutting structural donor` **29**, `ADMIT — specialization donor` **14**, `COMPANION` **83**, `EXCLUDE — non-structural for DIM anatomy` **27**. Thus **72 primary anatomy evidence artifacts**, **83 companions**, **27 anatomy-scope exclusions**. The latter still **belong to the 182-artifact corpus**. There are **30 distinct nonblank anatomy-lineage labels**, covering **155 rows**; the **27 excluded rows have blank anatomy-lineage entries**. A lineage label is **not** proof of a distinct independent donor vote.
- **Chassis capability audit:** **A=38** already directly chassis-tested; **B=13** under-contested/reconciled; **C=101** companion/specialization, no independent chassis vote; **D=24** no credible *chassis* potential; **E=6** operational/reference falsifiers. Totals **182**. These dispositions are **not** synonymously named phases, and **D does not mean globally irrelevant to every later DIM concept**.
- **Grouped bibliography:** **11** entries are deliberately retained in the **CSAPI and Immediate Foundational Standards** group, regardless of primary artifact type. The other **171** are editorially grouped by purported primary source type. Bibliographic grouping and classification are **not donor-value rankings**.

The original [chassis corpus-wide reconciliation](../DIM_Profile_V2_Chassis_Corpus_Wide_Reconciliation_v0.1_25OCT2026.md) explicitly warns that **source type cannot be an eligibility gate for a semantic/domain boundary challenge**. The [Phase A trust triage](../DIM_Profile_V2_Anatomy_PhaseA_Bulk_Trust_Triage_v0.1_26OCT2026.md) assessed **30 semantic lineages** as **22 GREEN, 8 YELLOW, 0 RED**, but states clearly this is **not 30 independent audits**; GREEN is not full clause-level verification. The 30 nonblank Phase 0 labels and 30 trust-triage lineages are not assumed to be one-to-one until concept-level lineage identification is verified.

## 3. Seven grouping-versus-primary-type discrepancies: flagged, not repaired

These are **exact, reproducible placement differences** between the grouped bibliography's section and the source-type CSV's `primary_type`. The bibliography's introductory statement says that each non-foundational entry is placed according to what it primarily standardizes. That **does not establish that the CSV is substantively right and the bibliography wrong**—editorial judgment or prior classification choices may explain a difference. **Do not change either source or count the mismatched placement as a donor-standard contradiction.** Step 02's register should preserve the frozen `primary_type` and separately record the bibliography section.

| Artifact ID | Source (short identification) | Frozen `primary_type` | Bibliography v0.5 section | Initial disposition |
| --- | --- | --- | --- | --- |
| **4** | OGC 09-033, *OWS-6 SensorML Profile for Discovery Engineering Report* | Guidance / explanatory / research / training | Profiles, Specializations, and Application Models | **UNRESOLVED EDITORIAL/CLASSIFICATION DIFFERENCE** |
| **42** | ISA, *Software Design Document* (2023h) | Guidance / explanatory / research / training | Reference Architectures and Architectural Frameworks | **UNRESOLVED** |
| **50** | Open Group SOSA *SOSA_TechStd_v1_DSDM_IDL* (2023b) | API / interface / protocol / service specification | Data Models, Schemas, Encodings, and Exchange Formats | **UNRESOLVED** |
| **73** | NIEMOpen, *Common Model Format Specification* (n.d.) | Modeling / packaging / versioning / conformance methodology | Data Models, Schemas, Encodings, and Exchange Formats | **UNRESOLVED** |
| **89** | DMTF, *Redfish Resource and Schema Guide* DSP2046 v2025.2 | Data model / schema / encoding / exchange format | Guidance, Research, and Explanatory Sources | **UNRESOLVED** |
| **157** | UCUM, *Copyright and License* (n.d.) | Vocabulary / terminology / units / code list / registry | Standards Policy, Registries, Strategy, and Governance | **UNRESOLVED** |
| **158** | RFC 6906, *The “profile” Link Relation Type* (2013) | Modeling / packaging / versioning / conformance methodology | APIs, Interfaces, Protocols, and Service Specifications | **UNRESOLVED** |

**No identity correction is implied**: all seven have the **same ID and identical frozen citation text across the three CSVs**, and the bibliography includes each exactly once. The problem is interpretive **classification/placement**, not record loss. A later focused review can classify a relevant item's source role more precisely **without altering its ID or concealing the historical classification**.

## 4. Source-ID, lineage, edition and evidence conventions for future Steps 02–12

The following are **operational source-of-truth precedence rules for the new alignment work**, not new DIM semantics:

1. **ID is the cross-file primary join key.** Use the exact numeric `id` 1–182 from the frozen [source-type CSV](../DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv), preserving it unchanged in any future derived register. **Do not generate a second serial-number scheme, reassign an ID, or use title/citation text as an identifier.** A source artifact ID is **not** an individual hardware/System ID, source-standard identifier, or CSAPI identifier.
2. **The frozen source-type CSV controls baseline citation text and primary/secondary type values** for Step 03 mechanical seeding. The anatomy and chassis CSVs provide their **own separately named historical analysis fields**. The grouped bibliography is a **human-readable presentation**, not an alternative source-ID allocator. **Do not erase or silently reconcile §3's seven grouping differences.** If later original-source investigation indicates a different type, record a qualified correction **in a separate derived decision**, leaving frozen metadata unchanged.
3. **Preserve full edition/standard/revision detail from the citation**. Different editions, working drafts, companion files, schemas, implementations and dated revisions can be separate *artifact rows* while contributing to **one or more source lineages**. For example, source **IDs 18, 19 and 20** represent two **October 2026 Working Drafts** of the SSN “2023 Edition” and an earlier **2017 W3C Recommendation**, respectively; they are **not equivalent authority or three independent confirmations of one clause**. **W3C/OGC SOSA/SSN is not The Open Group SOSA** (e.g., IDs 47–58). Also distinguish **CSAPI Part 1 (ID 10)** from **Part 2 (ID 11)**.
4. **Source lineage is not a stand-in for proof.** Preserve `anatomy_lineage`, `lineage_role` and `source_role` verbatim from Phase 0 when deriving later records; treat them as **prior structural research/triage**, not universally accepted model hierarchy. Verify a relevant source-defined class/relationship at the **exact source edition and clause** before claiming equivalence, adoption or standards conformance. The frozen trust triage's GREEN/YELLOW ceilings remain applicable.
5. **Chassis disposition has only chassis relevance.** Keep `audit_disposition` and `challenger_lineage` separately rather than overwriting anatomy data. A seemingly different label may simply represent a different question. As a concrete scope warning, **ID 33**, the NATO Core Data Framework study, was classified **EXCLUDE for DIM anatomy** but **A — already chassis-tested**. This is not an ID/citation discrepancy; it warns us against uncritically treating one historical disposition as a universal exclusion.
6. **Source-declared dependency vs project-inferred alignment** must remain distinguishable. An explicitly cited dependency between standards is not the same as our judgment that their concepts align. The eventual Step 02 register must differentiate source-native text, our candidate synthesis, absent evidence and test-verified transformations.
7. **An artifact's contribution may cross its primary source-type classification**. Schema, implementation and operational/reference artifacts can corroborate or challenge the model. **Do not pre-exclude a donor from a concept on source-type or prior anatomy disposition alone**. Multiple companions do not multiply independent evidence.
8. **Edition/citation identity check has a narrow ceiling here:** all three ledgers agree **textually**, and every citation appears in both bibliography versions. This does **not** authenticate normative edition status, URLs, original content, amendment currency, supersession, precise donor-to-donor dependency, or semantic compatibility. **79/182 frozen citation strings do not contain an explicit HTTP(S) URL**; many nevertheless include a standard identifier, source-local reference or other locator. This is a future **retrieval/traceability requirement when material**, not 79 proven errors. Do not infer unpublished/unavailable status from an absent link alone.
9. **Never auto-promote donor compatibility**. `SOURCE-DIRECT`, `DONOR-NATIVE`, `V2-INFERENCE`, candidate, partial mapping, incompatible, unverified and conformance-tested are **different standings**. The new register can cite the five completed research passes, but a citation plus similar wording does **not** prove lossless round-trip conversion or implementation of a donor standard.

**Exception handling:** retain immutable source IDs and text; log the precise row, field, two observed values, scope and uncertainty in the new register/decision record. Correct only after targeted source confirmation and explicit adjudication; do not silently patch the frozen 182-row baseline. Preserve source-family distinctness when the same organization publishes several standards.

## 5. Step 01 decision, limits and Step 02 readiness

**Result:** **Step 01 COMPLETE**. The stable 182-ID baseline is **consistent across the three CSVs and both bibliographies**, and the metadata-only count, join and classification checks are reproducible. The **seven unresolved placement differences** can safely accompany the derived register as separate *metadata exceptions* without blocking further work. No frozen source was edited.

**What this proves for the original objective:** We can now build the future donor-alignment register on **stable source identities**, retaining the difference between source artifact, independent conceptual lineage, actual donor concept and our intended DIM meaning. This reduces the risk of double-counting repeated editions or allowing earlier structural-triage classifications to masquerade as adopted V2 architecture.

**What it does not prove:** the original text of all 182 documents was rechecked; the 30 lineage labels or 22 GREEN findings are independent standards endorsements; the present chassis is finally adopted; the first five candidate meanings are globally compatible; any published Profile rule or rich vendor-fidelity client is implemented.

**Next authorized step only upon owner's next `proceed`: Step 02 — define the smallest maintainable donor alignment register format and evidence-status vocabulary**, with an illustrative example from **one** already researched concept. Don't seed all 182 entries until Step 03, and don't start concept deep-dives until Steps 04–08.
