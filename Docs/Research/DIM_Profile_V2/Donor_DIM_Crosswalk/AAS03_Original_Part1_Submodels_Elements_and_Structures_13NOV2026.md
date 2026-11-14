# AAS03 — Original Part 1 Submodels, elements and information structures

13 November 2026 · Research branch `research/dim-profile-v2` · Preflight `76aa3d40e99a117cbb3e29f00c63d6784017ca5a`

**Completed at the bounded source scope below. Asset Administration Shell (AAS) remains active and incomplete.** This step follows the owner’s “Prpceed” after Profile Rewrite 34 recovery and stops before AAS04. The governing [donor plan](PLAN_AAS_v3_2_Source_First_Donor_Review_13NOV2026.md) and [cumulative source ledger](AAS01_Original_Source_Corpus_Coverage_13NOV2026.json) retain the original source grades, owner decisions and earlier limitations. No Domain Information Model (DIM) class, hierarchy, cardinality or OGC API–Connected Systems (CSAPI) Profile requirement was adopted.

## What we learned

AAS separates an asset from the information used to describe it. A Submodel describes an aspect of that asset; a collection gathers named values, while a list gathers typed elements and indicates whether their order matters. These structures can organize technical data and support a future Details view, but their nesting does not establish the physical equipment hierarchy. Entity and semantically defined relationships address composition more directly, while still requiring evidence of the actual installed arrangement. The source findings and exact locators are recorded as AAS03-N001–N003 and N011–N017 in the ledger.

The basic value carriers also retain different meanings. Property holds a single typed value, MultiLanguageProperty holds language-specific text, File points to content, and Blob contains the content itself. Range is explicitly Experimental and supplies typed endpoints without establishing whether those endpoints are permitted limits, measurement uncertainty or another domain-specific interval. A generic Property is not automatically an observation or a declared sensor output, and a generic file is not automatically media associated with an observation. These distinctions support qualified comparisons in existing rows rather than one new DIM class for each AAS term (AAS03-N004–N010).

The normal JSON serialization exposes a concrete compatibility issue. It requires empty aggregation arrays to be omitted and treats an empty aggregation as equivalent to an absent attribute; the ISA comparison already preserves the distinction between a supplied empty list and an omitted update. A direct substitution therefore cannot preserve that distinction without an additional mapping decision. This is recorded as a bounded **CONFLICT** for the normal JSON representation, while AAS Part 2 update semantics remain unreviewed. The same source explains why ordinary Property values appear as strings interpreted through valueType and why modelType is a serialization discriminator rather than an equipment field (AAS03-N025–N027).

Semantic references and qualifiers add context but do not remove the need to inspect meaning. A ConceptDescription can supply a semantic definition and identify compatible or derived definitions; the informative matching guidance distinguishes exact matching from several knowledge-dependent strategies. A Submodel template, a data specification template and an administrative templateId serve different purposes. Qualifier examples distinguish value quality, semantic context such as as-planned/as-maintained, and template requirements, but external qualifier dictionaries were not audited here. The earlier optional-semanticId versus overview-wording question remains open (AAS03-N019–N024, N028).

## Exact original-source coverage

The source is Industrial Digital Twin Association (IDTA), *Specification of the Asset Administration Shell, Part 1: Metamodel*, version 3.2.0, Release 26-01, pinned to [`ecd191273a28dd9c4e7bb75e923f0f0fe5da444e`](https://github.com/admin-shell-io/aas-specs-metamodel/tree/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e). These counts describe inspected material at the stated depth, not a percentage of the whole donor or a count of adopted DIM fields. All original source URLs, Git blob identities, line ranges, findings, attributes and limitations are in the existing cumulative ledger. No current working-branch text was substituted for the pinned release.

| Material | Actual coverage in AAS03 | Boundary |
| --- | --- | --- |
| SubmodelElement original page | All 1,001 lines; all 24 section spans read; 46 class-attribute entries individually recorded | Operations, Capability and experimental events were inventoried for structure; behavior/comparison remains AAS04 |
| Core Submodel/SubmodelElement | Lines 252–321 reread | Earlier core identity evidence remains AAS02; no full-corpus restart |
| ConceptDescription, data-specification explanation, normal JSON mapping | Full text of these three files | Linked companion specifications, generators and external standards were not thereby audited |
| Common attributes, references and semantic-matching annex | Exact selected ranges in the ledger | No full common/reference/annex audit claim |
| Constraints | 17 individually anchored rules; original global/included constraint text reread | Source rules are not proved by schema acceptance or adopted as Profile SHALLs |
| Original JSON schema | 30 named definitions inspected for structure, cardinality and representation | Not all 70 definitions; no exhaustive regex, XML/RDF or runtime validation |
| Diagram sources | 15 pinned local class partials and three wrapper files read | Publisher figure pixels and equality with remote working-branch includes remain unverified |
| Findings and master | 33 native finding records; 19 existing-row comparisons changed | Findings, attribute entries and rule records overlap; do not add them as a unique-clause denominator |

The source’s original optional cardinalities are retained, including Entity.entityType, RelationshipElement.first/second, and File/Blob contentType. List children must follow the declared element/value type and semantic constraints; template/operation-variable lists have the native singleton rule AASd-138. These rules are recorded independently from JSON required arrays and array minItems. The DataElement section invokes **AASd-090**, but its pinned constraint include does not define that macro; this missing source rule is recorded as unresolved, not reconstructed.

## Progressive master integration

The same 337 information rows, topic dividers, four source cases and approved 16-column layout remain. **19 AAS cells changed: 15 newly populated and four extended; 23 AAS cells are populated in total.** Existing AAS02 text and source IDs remain in the four extended cells. Every other donor, case and proposed-DIM value is unchanged, and all AAS comparisons remain without individual classification colors.

| Existing row | Relation | Source-qualified addition |
| --- | --- | --- |
| `S06-R005` — Described sensing System / arrangement | RELATED | Submodels organize aspects of one represented asset; collections group named values and lists group typed elements. These information structures do not establish a physical sensing-system hierarchy. |
| `S06-R007` — Physical constituent | PARTIAL | Entity can describe composite-asset parts and their shell-management status; its statements are information. Native entityType is optional in v3.2. This still does not establish an observed installed constituent. |
| `S06-R008` — Connected external equipment | RELATED | ReferenceElement and semantically defined relationships can link objects; annotated relationships add supporting data. v3.2 first/second endpoints are optional. Neither structure proves a cable, attachment or reachable equipment. |
| `ISA-C-099` — Reported physical parent/child attachment relationships | PARTIAL | Entity and semantically qualified relationships can represent composition. Relationship annotations can qualify a link, but physical attachment, observed installation and applicable time require separate evidence. |
| `S06-R012` — Reported output field | RELATED | A Property can describe a typed field and its semantics. It does not by itself say that the field is an emitted sensor output or logger diagnostic. |
| `S06-R013` — Observed / observable property | RELATED | semanticId/ConceptDescription can identify the meaning of a property. They do not supply an observation act, feature of interest or evidence that two dictionary concepts are equivalent. |
| `ISA-C-146` — Media resources associated with observation | RELATED | File provides a locator; Blob embeds content (base64 in normal JSON). These can carry media, but no association with a particular observation or acquisition is established by those classes alone. |
| `ISA-K-PROPERTY-DECL` — Declared property definition | PARTIAL | A template Property can express type, semantic meaning and qualifiers without a value. Mutability, publication policy and a full ISA property contract are not established by this structure. |
| `ISA-K-CUSTOM-TYPE` — Declared custom data structure | RELATED | Submodel templates and nested collections/lists can describe structured information. A Submodel template and a data specification template serve different purposes; neither is automatically an ISA named custom-type declaration. |
| `ISA-K-FIELD-DECL` — Declared field within a custom structure | PARTIAL | Named collection members can carry value types, semantic identifiers and qualifiers. ISA field omission rules and optionality require separate alignment; list children use positional referencing. |
| `ISA-K-TYPE-CHOICE` — Declared built-in or custom value type | PARTIAL | valueType identifies a primitive value type, while typeValueListElement identifies an element type. JSON modelType is a serialization discriminator. None alone establishes ISA custom-type-name semantics. |
| `ISA-K-STRUCTURE` — Declared value shape and collection bounds | PARTIAL | Collection and List express named versus typed/repeated structures; list ordering and homogeneous child types are explicit. ISA minimum/maximum length and tree-depth bounds are not supplied by these generic AAS attributes. |
| `ISA-K-VALUE-RANGE` — Declared permitted or excluded values | RELATED | Experimental Range supplies typed min/max values. These do not establish permitted/excluded values, endpoint inclusion or an ISA Range Declaration. |
| `ISA-R-NAMED-VALUE` — Named value payload | PARTIAL | A named Property carries a typed value or coded value; multilingual values use a separate element type. Normal JSON Property.value is a string interpreted by valueType. A value need not be present. |
| `ISA-R-ASSOCIATIVE` — Named-value associative collection | PARTIAL | Collection groups named values with unique idShort names. Normal JSON omits an empty aggregation rather than sending an empty array; ISA empty-capable associative payloads require an explicit translation decision. |
| `ISA-R-LIST` — Declared-type value list | PARTIAL | List declares child element type and whether order matters; semantic/type consistency rules apply. Normal JSON omits an empty aggregation. This is not an automatic ISA list-payload equivalence. |
| `ISA-R-CUSTOM` — Custom-structure field values | PARTIAL | A collection instance can carry named field values guided by a template. Its structure and normal-JSON omission rules do not automatically reproduce an ISA custom-type wire contract. |
| `ISA-R-TREE` — Recursive same-type value hierarchy | RELATED | Nested collections/lists support recursive information structures. They do not require ISA same-datatype nodes, a named value at each node or ISA child-list semantics. |
| `ISA-R-LIST-PRESENCE` — Supplied list value versus no update | CONFLICT | Normal JSON explicitly equates empty aggregations with omitted attributes and forbids empty arrays. This conflicts with preserving ISA supplied-empty versus omitted-update distinction by direct normal-JSON substitution; Part 2 update behavior is unreviewed. |

The existing four case records were used as boundary checks, without inventing native AAS instances. Dragino, AirGradient and Campbell retain their manufacturer/design or prospective-pairing standing; Bennett retains its actual source-qualified equipment identities and historical limits. AAS’s structural mechanisms do not turn those records into authenticated installed AAS assets, establish observed connections, or resolve prior case holds. The original case cells and evidence records remain unchanged.

## Saved workbook and preservation checks

The same editable [master workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) was refreshed together with the canonical JSON, both CSV mirrors and both readable Markdown comparisons. Reopening the saved workbook verified all **354 × 16 = 5,664** comparison values, all 26 sheets in their original order, all original master-cell styles, and 21 unrelated sheet XMLs byte-for-byte. Original classification colors and mixed holds are retained; only the changed AAS comparison rows received additional height to display their longer source-qualified text. Summary/validation, legend and the existing AAS evidence column in DIM Register were refreshed, including stale M01 and SAPIENT disposition notices. The full machine-readable result and hashes are under `AAS03.saved_verification` in the cumulative ledger.

The final saved workbook was also rendered and visually checked at representative changed cells. The repository-wide artifact/link check still reports seven pre-existing register/path issues; comparison with the actual preflight commit found exactly the same seven errors and no new AAS03 link errors. Their exact messages are retained in the cumulative ledger, so the broader check is not represented as passing.

The permanent M00 and M01 workbooks are unchanged; no M02 was created. The two stale layout holds AAS01-H07 and AAS02-H01 now explicitly record their resolution by the already-approved AAS02-G publication, with their original text retained. Other earlier source limitations remain open, including identity/physical-relationship cautions, diagram provenance, selected-schema coverage and semantic wording. Source completeness, cross-format parity, model adoption and runtime conformance remain separate claims.

## Holds and next boundary

- **AAS03-H01 — native semantic wording:** AAS02-H07 remains: overview semantic-definition wording, optional semanticId and recommendation must not become an invented mandatory field.
- **AAS03-H02 — source rendering:** Pinned local class text and three wrapper sources read; remote working-branch includes and publisher rendered figure equality remain unverified (AAS02-H05).
- **AAS03-H03 — collection update meaning:** Normal JSON omission rule conflicts with direct preservation of ISA supplied-empty/omitted-update distinction; Part2 operation/update semantics not yet reviewed.
- **AAS03-H04 — native validation:** List uniformity, template singleton and conditional Entity/Qualifier rules are not established by generic JSON schema validity alone. No implementation or exhaustive conformance tests.
- **AAS03-H05 — concept specifications:** ConceptDescription prose expects data specification content while generic inherited cardinality is 0..*. Part3a/3b and external dictionary/template validation remain unreviewed.
- **AAS03-H06 — scope boundary:** Operation, Capability and experimental event structures read; state/effect/time/API behavior comparisons deferred to AAS04/Part2. Full XML/RDF, generated fixtures and external references remain unaudited.
- **AAS03-H07 — unresolved native source references:** SubmodelElement DataElement text line 375 invokes {aasd090}; the pinned includes/constraints.adoc defines no aasd090. The core validator note also names Collection/submodelElements whereas the collection attribute is value. No missing rule or corrected requirement is invented.

The accepted post-AAS01 research estimate was low 10 / most likely 14 / high 21 further research increments. With AAS02 and AAS03 now completed, the arithmetic working remainder is **8 / 12 / 19**, excluding separate owner approvals and layout publication. This is not a fixed packet schedule, a fresh exhaustive re-estimate, or a reason to add work; later estimates must follow actual remaining source complexity. No scope increase or methodology change is proposed by this step.

**One next fresh “Proceed” = AAS04 only:** review native condition, capability, operation/event and version/time semantics under the existing donor plan, reusing the structural evidence already read here. Stop before AAS05, donor transition, DIM/Profile adoption, client changes or deployment.

## References

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell. Part 1: Metamodel*. Version 3.2.0, Release 26-01. July. [Publisher edition](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html). Original source chapters and exact pinned locators are identified individually in the cumulative ledger; publisher source is licensed CC BY 4.0.
