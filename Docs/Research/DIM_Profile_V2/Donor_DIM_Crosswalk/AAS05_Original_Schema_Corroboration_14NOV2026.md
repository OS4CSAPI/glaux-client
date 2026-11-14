# AAS05 — Original schema corroboration and source-to-master clarification

14 November 2026 · research/dim-profile-v2 · Preflight `02232bb6eed411ccb159692112a65394b8553db3`

**Bounded source-first original audit, not whole-Asset Administration Shell (AAS) source completeness.** Published Industrial Digital Twin Association (IDTA) Release 26-01 Part1 Metamodel v3.2.0 and Part2 Application Programming Interface (API) v3.2.0 are pinned at the distinct original Git commits recorded in the cumulative ledger. The work inspects 23 selected and overlapping schema blocks in six original files, rather than 23 independent normative SHALLs or a complete schema family review.

## What changes our understanding

The AAS digital shell and represented asset remain different referents. Part1 JSON and XML require `assetInformation`, but a modeled reference, asset ID or `Entity` does not authenticate the installed parts of a sensing system. A present `OperationVariable.value` describes a variable structure, not an issued or completed command; optional operation arrays do not define required invocation arguments.

**The event timestamp spelling contradiction is confirmed across original sources.** The source text calls the Experimental `EventPayload.timestamp`, while original JSON, XML Schema Definition (XSD), Web Ontology Language (OWL), Shapes Constraint Language (SHACL) and the shared API metamodel OpenAPI use `timeStamp`. These are incompatible names in the original publication, not a permission to silently change the native text. An event trigger time is not automatically a physical observation time.

Administrative `version`/`revision` are short digit strings in JSON/XML/OpenAPI although the prose calls them integers; selected UTC patterns allow zero-offset suffixes while a published `DateTimeUtc` example uses a nonzero offset. The original differences remain unresolved. Likewise, metamodel `Range` allows optional string lexical bounds with a value type, whereas the Part2 API `RangeValue` requires two numeric bounds: their representation-specific meaning is not interchangeable by assumption.

List value arrays in normal JSON/XML are optional but nonempty when present. In RDF, the original OWL property describes ordinary value-object relations and SHACL permits zero list-value triples; the mere RDF graph does not establish an order-preserving conversion despite the list's documented order relevance. No false empty-versus-omitted-update equality is introduced. Proprietary extensions remain native-specialized rather than mandatory DIM fields.

## Precisely inspected original source blocks

Each stable ID below has the original publisher, edition, source kind, standing, exact original line range and immutable URL in the **same cumulative AAS original-source ledger**. Entire files remain sampled, not exhaustively read.

| Source ID | Pinned source locator | Native standing | What was checked |
| --- | --- | --- | --- |
| `AAS05-S001` | [schemas/json/aas.json lines 131–210](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L131-L210) | SCHEMA_DEFINITION | Digital shell requires assetInformation, AssetInformation requires assetKind; optional global/specific asset ID is not installed equipment identity. |
| `AAS05-S002` | [schemas/json/aas.json lines 1295–1325](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L1295-L1325) | SCHEMA_CONSTRAINT | Reference requires type and keys, not proof of physical linkage or resolvable OGC URI. |
| `AAS05-S003` | [schemas/json/aas.json lines 1506–1566](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L1506-L1566) | SCHEMA_CONSTRAINT | Collection/List value optional, minItems 1 when present; list typeValueListElement required and orderRelevant optional. |
| `AAS05-S004` | [schemas/json/aas.json lines 1082–1127](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L1082-L1127) | SCHEMA_CONSTRAINT | Operation variable arrays optional, minItems 1 when present; OperationVariable.value required; not execution/mandatory argument semantics. |
| `AAS05-S005` | [schemas/json/aas.json lines 672–710](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L672-L710) | SCHEMA_CONSTRAINT_EXPERIMENTAL | EventPayload JSON requires timeStamp and source/observableReference; text uses timestamp. |
| `AAS05-S006` | [schemas/json/aas.json lines 52–124](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L52-L124) | SCHEMA_CONSTRAINT | Administrative version/revision digit strings 1–4 chars; UTC dates zero-offset patterns. |
| `AAS05-S007` | [schemas/json/aas.json lines 1215–1249](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L1215-L1249) | SCHEMA_CONSTRAINT | Full-model Range valueType and optional lexical string min/max. |
| `AAS05-S008` | [schemas/json/aas.json lines 711–754](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/json/aas.json#L711-L754) | SCHEMA_CONSTRAINT | Extension requires local name; semantics/typed values not automatic global interoperability. |
| `AAS05-S009` | [schemas/xml/AAS.xsd lines 90–133](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/xml/AAS.xsd#L90-L133) | SCHEMA_CONSTRAINT | XML shell requires assetInformation; optional digital/reference links not physical attachment evidence. |
| `AAS05-S010` | [schemas/xml/AAS.xsd lines 705–741](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/xml/AAS.xsd#L705-L741) | SCHEMA_CONSTRAINT | XML Operation optional variable wrappers require one-or-more child OperationVariable, with value required. |
| `AAS05-S011` | [schemas/xml/AAS.xsd lines 436–460](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/xml/AAS.xsd#L436-L460) | SCHEMA_CONSTRAINT_EXPERIMENTAL | XML EventPayload requires timeStamp, not text timestamp. |
| `AAS05-S012` | [schemas/xml/AAS.xsd lines 962–994](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/xml/AAS.xsd#L962-L994) | SCHEMA_CONSTRAINT | XML optional list/collection wrappers nonempty when present; no empty update equivalence. |
| `AAS05-S013` | [schemas/xml/AAS.xsd lines 32–62](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/xml/AAS.xsd#L32-L62) | SCHEMA_CONSTRAINT | Administrative versions constrained as digit strings in XML, versus integer prose. |
| `AAS05-S014` | [schemas/rdf/rdf-ontology.ttl lines 1165–1171](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/rdf/rdf-ontology.ttl#L1165-L1171) | ONTOLOGY_DECLARATION_EXPERIMENTAL | OWL EventPayload/timeStamp data property string, contrary to native text spelling. |
| `AAS05-S015` | [schemas/rdf/rdf-ontology.ttl lines 2092–2128](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/rdf/rdf-ontology.ttl#L2092-L2128) | ONTOLOGY_DECLARATION | OWL says list ordered, but value ordinary object property; triple order/round trip not proven. |
| `AAS05-S016` | [schemas/rdf/shacl-schema.ttl lines 594–656](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/rdf/shacl-schema.ttl#L594-L656) | SHACL_SHAPE_EXPERIMENTAL | SHACL EventPayload/timeStamp minCount1/maxCount1 with UTC pattern; not verified physical event. |
| `AAS05-S017` | [schemas/rdf/shacl-schema.ttl lines 1377–1414](https://github.com/admin-shell-io/aas-specs-metamodel/blob/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e/schemas/rdf/shacl-schema.ttl#L1377-L1414) | SHACL_SHAPE | SHACL list value minCount0 with class SubmodelElement; no order container in selected shape. |
| `AAS05-S018` | [Part1-MetaModel-Schemas/openapi.yaml lines 448–474](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part1-MetaModel-Schemas/openapi.yaml#L448-L474) | OPENAPI_SCHEMA | Part2-shared Part1 schema requires EventPayload.timeStamp, as do native serializations. |
| `AAS05-S019` | [Part1-MetaModel-Schemas/openapi.yaml lines 698–725](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part1-MetaModel-Schemas/openapi.yaml#L698-L725) | OPENAPI_SCHEMA | Part2-shared metamodel Operation/OperationVariable structure declares arguments, not effects. |
| `AAS05-S020` | [Part1-MetaModel-Schemas/openapi.yaml lines 780–795](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part1-MetaModel-Schemas/openapi.yaml#L780-L795) | OPENAPI_SCHEMA | Shared full-model Range has valueType and optional string min/max. |
| `AAS05-S021` | [Part2-API-Schemas/openapi.yaml lines 1190–1200](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part2-API-Schemas/openapi.yaml#L1190-L1200) | OPENAPI_VALUE_ONLY_SCHEMA | API RangeValue requires numeric min and max, unlike full-model lexical optional pair. |
| `AAS05-S022` | [Part2-API-Schemas/openapi.yaml lines 934–970](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part2-API-Schemas/openapi.yaml#L934-L970) | OPENAPI_SCHEMA | Operation request/result value-only structures are schema envelopes, not executed action contracts. |
| `AAS05-S023` | [Part2-API-Schemas/openapi.yaml lines 1410–1452](https://github.com/admin-shell-io/aas-specs-api/blob/f136ba1465e4c6b5b25444e0609d4de8f7429044/Part2-API-Schemas/openapi.yaml#L1410-L1452) | OPENAPI_SCHEMA | ListValue array versus CollectionValue ValueOnly; no equivalence with RDF or absent-vs-empty update. |

The original source is 4 Part1 files (JSON, XML, RDF ontology and SHACL) and 2 distinct Part2 *shared schema* files. This step does **not** read all 34 versioned Part2 service OpenAPI profile operation bodies, validate all JSON definitions and XML types or convert every native RDF shape at runtime. References to aligned IDTA companion editions are not proof that their original content was examined.

## Thirteen source-qualified clarifications to existing AAS donor cells

The following are research clarifications only: **no new rows, source-case changes, adopted model class, proposed Profile SHALL or newly imposed universal physical hierarchy**. Each prior AAS cell remains intact and gains a provenance-qualified AAS05 line.

| Existing row | Relation | Meaning/caveat | Original source IDs |
| --- | --- | --- | --- |
| `S06-R005` | RELATED | JSON/XML require shell assetInformation; that digital record may represent a physical or software asset, not proof of an installed sensing System or CSAPI URI. | `AAS05-S001`, `AAS05-S009` |
| `S06-R007` | PARTIAL/RELATED | Reference keys and optional submodel/asset links do not corroborate actual physically attached constituents. | `AAS05-S001`, `AAS05-S002`, `AAS05-S009` |
| `ISA-K-COMMAND-DECL` | PARTIAL | Normal schema Operation variable containers are declarative optional arrays (nonempty when present), not evidence of an issued request or physical effect. | `AAS05-S004`, `AAS05-S010`, `AAS05-S019` |
| `ISA-K-PARAMETER-DECL` | PARTIAL | OperationVariable.value is required, while value-only API argument envelopes are distinct; neither makes a specific argument mandatory. | `AAS05-S004`, `AAS05-S010`, `AAS05-S019`, `AAS05-S022` |
| `ISA-K-RESULT-DECL` | PARTIAL | Declared output/inoutput variables and API OperationResultValueOnly are structures, not completion, acknowledgment or physical result. | `AAS05-S004`, `AAS05-S010`, `AAS05-S022` |
| `ISA-K-STRUCTURE` | PARTIAL | Full-model list/collection arrays require at least one child if present, SHACL list values can be absent, and RDF triples do not guarantee element order. | `AAS05-S003`, `AAS05-S012`, `AAS05-S015`, `AAS05-S017` |
| `ISA-K-VALUE-RANGE` | RELATED | Full-model Range allows optional string-lexical min/max with valueType; API RangeValue requires both numeric endpoints. This is distinct representation scope, not a universal allowed-values rule. | `AAS05-S007`, `AAS05-S020`, `AAS05-S021` |
| `ISA-R-LIST` | PARTIAL | List.orderRelevant exists in the metamodel; generic RDF value object properties/SHACL triple shapes do not prove lossless ordered-list conversion. | `AAS05-S003`, `AAS05-S015`, `AAS05-S017`, `AAS05-S023` |
| `ISA-R-LIST-PRESENCE` | CONFLICT | Normal JSON/XML omit empty array/wrappers but require nonempty supplied containers, while SHACL can represent zero values and API ValueOnly differs. Preserve supplied-empty versus omitted-update hold. | `AAS05-S003`, `AAS05-S012`, `AAS05-S017`, `AAS05-S023` |
| `ISA-T-EVENT-TIME` | RELATED | Experimental EventPayload text spells timestamp; JSON/XML/OWL/SHACL/shared OpenAPI spell timeStamp. Original source inconsistency unresolved; neither proves observation time. | `AAS05-S005`, `AAS05-S011`, `AAS05-S014`, `AAS05-S016`, `AAS05-S018` |
| `ISA-A-TIME-BASIS` | RELATED | Selected UTC patterns use zero offset while the DateTimeUtc original example allows a nonzero offset; neither establishes device clock synchronization. | `AAS05-S005`, `AAS05-S006`, `AAS05-S013`, `AAS05-S016` |
| `ISA-C-048` | RELATED | Published prose calls administrative version/revision integers; selected JSON/XML/shared metamodel schemas use 1–4 digit strings. This is not installed firmware version. | `AAS05-S006`, `AAS05-S013` |
| `ISA-A-EXTENSION-STANDING` | RELATED | Typed named extensions in the original schema retain vendor specificity; syntactic admissibility does not establish globally shared meaning or adopted Profile requirement. | `AAS05-S008` |

A `CONFLICT` at the single `ISA-R-LIST-PRESENCE` comparison remains explicitly scoped to incompatible assumptions about data representation/update, not a statement that every AAS implementation lacks an update contract. `UNREVIEWED` elsewhere is not reclassified as `NO_ESTABLISHED`.

## The four empirical source cases remain unchanged

Dragino and AirGradient are reference designs, not authenticated installed AAS instances; Campbell and ClimaVue are a possible documented pairing, not proven physical attachment. Bennett's Point retains its two original NOAA mean records and historically identified equipment, distinct from four earlier digital copies. AAS event time, administration time and schema encoding cannot silently replace original QA, original event times, original provenance or the undecided producing System.

## Open holds

- **AAS05-H01 — Experimental event name and source truth:** Native EventPayload.timestamp disagrees with timeStamp in pinned JSON, XML, RDF and shared OpenAPI; experimental standing and no verified occurrence persist.
- **AAS05-H02 — Administrative representation:** Version/revision prose integer versus schema digit string; DateTimeUtc original nonzero-offset example versus selected zero-offset patterns.
- **AAS05-H03 — List semantics:** Normal full-model empty/omitted handling, SHACL zero-value shape and RDF triple order have no verified lossless conversion or update equality.
- **AAS05-H04 — Range variant meaning:** Full-model optional lexical string min/max versus required numeric ValueOnly RangeValue; no inferred universal allowed-values rule.
- **AAS05-H05 — Original corpus incompleteness:** Only selected blocks of six original schema files reviewed; no entire schema set, aligned companions, 34 API SSP operation contracts or external specifications.
- **AAS05-H06 — Runtime and adoption:** No schema runtime validation, actual API service call, externally verified producer, real command or adopted DIM/Profile class/SHALL.
- **AAS05-H07 — Historical source holds:** ISA six questions, The Open Group SOSA nine source-hold families and SAPIENT 39 overlapping partial-source limitations remain preserved.

Earlier AAS01–AAS04 open holds remain present. ISA's six unresolved questions, The Open Group SOSA's nine bounded-PARTIAL source-hold families and SAPIENT's 39 overlapping accepted-PARTIAL source limitations also remain. This AAS schema review is not an OGC standards conformance assessment.

## Exact existing master and manual workbook gate

The publisher must update **one canonical JSON**, both CSV mirrors, both readable Markdown comparisons, and the **same original 26-worksheet editable Excel**. Required preservation: 337 information rows, 354×16 comparison layout and all 5,664 independently reopened saved values; same case/donor/OGC/DIM order, original 325 source-classification colored cells, 67 deliberately uncolored mixed cells, 21 historical sheets, and manually frozen M00/M01 original workbook versions. No manual M02 is approved. Publish verification in the cumulative `AAS05.saved_verification`, separate from source completeness.

The donor stays ACTIVE and incomplete, with a low/most-likely/high arithmetic research remainder of **6 / 10 / 17** (planning guidance only). **STOP after AAS05; one later owner Proceed = AAS06 only**, original pinned Part2 API identity, registry, repository and discovery service operation meanings. No AAS07, DIM/Profile adoption, Glaux UI/server change, hardware command or deployment is authorized.
