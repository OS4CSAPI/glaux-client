# Details View acceptance criteria

These criteria define the bounded checks for the first Overview, Equipment, and
Condition increment. They are an experimental implementation companion. Test
execution, revision, result and remaining limitations belong in the
[current-work checkpoint](../Plans/CURRENT_WORK.md); this document does not claim
that a check has passed.

Use the [view mapping](../Design/DETAILS_VIEW_MAPPING.md) and
[source index](../Research/SOURCE_INDEX.md) to distinguish supported MPSS rules,
experimental mappings and unresolved source semantics. Keep executable checks in
the repository's test directories rather than reproducing them in this document.

## Operator tasks and required outcomes

| Check | Task or input | Required outcome |
| --- | --- | --- |
| DV-01 | Open each selected example and switch among Overview, Equipment and Condition. | The compact card retains the same focal resource, Type, API/fixture ID and Source. TRSS ETU-II, OmniSense Core 2 and Core 5 ADS remain separate records. Fixture identities are explicitly synthetic; a native transmitter or device number is not presented as a verified API ID. |
| DV-02 | Inspect Overview and expand a fact. | Use Operational > Overview. Disclosure expands within the card. TRSS supplies Sensor string MM101 and no Mission; do not copy the string into Mission. Core 2 has no supplied mission/string. Missing values can be inspected without asserting that the system is unassigned. |
| DV-03 | Inspect TRSS Equipment. | Detector 1 is SEISMIC/ACOUSTIC; Detector 2 is IRID-II; orientation 0 degrees remains scoped and reference direction unknown. The heading identifies configured selections. No linked devices or connection confirmation are fabricated. |
| DV-04 | Open supported detector choices. | Detector 1 and Detector 2 choices remain position-specific and separate from selected values. Explicit NONE is distinct from missing data. The limited manual rules are not presented as a complete compatibility validator. |
| DV-05 | Inspect Core 2 Equipment. | All five supplied labels remain visible or reachable: Magnetic, Seismic (ext), Detection Switch 1, Detection Switch 2 and Control Switch. They are reported entries, without inferred physical-device count, connector positions or individual identities. |
| DV-06 | Inspect TRSS Condition. | 100.0% remains qualified as a source capacity estimate alongside the collecting-data state. Estimator inputs remain inputs. No measured ETU-II voltage, full-charge conclusion or readiness state is invented. |
| DV-07 | Inspect Core 5 ADS Condition. | Preserve 15.43 V DC, raw unverified source time, Normal mode and the source-form interval/duration. Keep the six test results individual. No percent-full conversion, runtime calculation, trend or overall readiness result is produced. |
| DV-08 | Return to Core 2 after viewing Core 5 ADS. | Core 5 voltage, mode, time and test outcomes do not populate Core 2. Missing Core 2 condition remains explicitly missing for that source example. |
| DV-09 | Inspect generic and interpreted presentations of the same input. | Generic presentation retains typed values, labels, units, group structure, arrays, source definitions, relationships and unfamiliar fields. The interpreted presentation distinguishes recognized MPSS content from experiment-specific mappings. It does not make a benefit claim by deliberately weakening generic access. |
| DV-10 | Inspect a source fact and its origin. | The fact can be traced to its actual retained representation and selector, owning subject, mapping basis, unit/code space and time meaning. Source inspection renders data safely. A parsed model does not replace the original response. |

## Semantic regression cases

| Check | Input variation | Required outcome |
| --- | --- | --- |
| DV-11 | Valid MPSS technical-description with a meaningful supplied group label and one or more supported Text terms; also supply two separately labeled groups. | Recognize the exact group URI and applicable exact term URIs. Accept only the supported term meanings/types; no manufacturer-name switch is needed. Single-valued term cardinality applies within each group. Preserve separate groups and their source context without inventing a one-group-per-process constraint. |
| DV-12 | Similar label with an unknown definition, unsupported namespace version, wrong carrier/type, missing or blank group label, missing required content, conflicting duplicate term, or absent/foreign experimental Category code space. | Preserve the source content and explain the unsupported or conflicting interpretation. A generated fallback label does not satisfy the meaningful-label requirement. Category interpretation requires the exact `EP` code space for the selected term. Label similarity, array order and first-value-wins do not authorize a mapping. |
| DV-13 | Unknown group/property and extra vendor content. | It remains accessible in typed/source inspection and does not silently disappear during interpretation. |
| DV-14 | A reported list entry resembles a configured detector label. | Preserve both assertion kinds; do not merge by display text, equate Seismic (ext) with SEISMIC/ACOUSTIC, or present configuration as observed attachment. |
| DV-15 | Actual zero, explicit NONE, a value matching its component's declared nil token, an undeclared sentinel-looking number, missing field, unloaded optional data, denied request and unsupported structure. | Preserve the distinct known states. Zero remains zero unless that exact component declares it nil. A matching declared nil token is withheld from interpreted physical-value presentation, with original token and reason preserved for inspection; no global sentinel convention is invented. Missing data never means healthy, empty inventory or unassigned. |
| DV-16 | Raw Core 5 source clock and a later retrieval time. | Preserve the source clock string and its unverified status. Do not append an assumed timezone or replace source time with retrieval time. Refreshing a representation does not establish a new device report. |
| DV-17 | Source update time is available for a containing editor record. | Do not reuse it as the time each transducer was detected. Configuration validity, description validity, event time and observation/result times retain their own meanings. |
| DV-18 | Related data belongs to a different System or has unresolved subject scope. | Do not attach its readings to the selected System. Keep the unresolved relationship visible. The R11/R17 producer/subject distinction remains intact. |
| DV-19 | Only voltage is supplied; an estimate is collecting data; or the same estimate term appears with another or absent status. | No automatic percentage, remaining-life, healthy, online or readiness conclusion is derived. Display the actual supplied estimate status, without defaulting every estimate to the TRSS collecting-data state. No RFC 7577 or external-terminal definition is substituted for the OmniSense-specific meaning. |

## Retrieval and interface checks

| Check | Situation | Required outcome |
| --- | --- | --- |
| DV-20 | Successful local fixture load or authorized read-only retrieval. | Preserve original response text/bytes and relevant metadata independently of parsing. Identify local fixture versus server data and record actual retrieval time separately. |
| DV-21 | Failed refresh after useful data was loaded. | Retain the useful previous content with an explicit failed-refresh indication and its last successful retrieval time. Do not claim the old data was newly confirmed. |
| DV-22 | Partial collection or unavailable relationship/schema. | Bound retrieval, show the known limitation and retain usable facts. A first empty page does not establish physical absence. |
| DV-23 | Keyboard navigation, disclosures and narrow layout. | Reach controls with a visible focus indicator; expose selected/expanded states; preserve units, essential qualifications and source identity without clipping. Review both normal and narrow card widths. |
| DV-24 | Marking information is absent. | Retain banner positions and indicate that markings were not supplied for the example. Do not invent an Unclassified marking. |
| DV-25 | Open a card, change tabs, expand details or refresh. | No device control, server write, infrastructure change or unrequested deployment occurs. Source inspection and metadata display do not confer command permission. |
| DV-26 | Open the separate synthetic MPSS technical-description contract example. | Identify it as wholly synthetic, preserve the supported technical term meanings, and keep it separate from the historical device transcriptions. Its success does not establish a manufacturer mapping or an overall profile advantage. |

## Evidence and completion record

For the implementation revision being delivered, record the commands actually
run, their outcomes, the relevant automated cases, and the visual review scope.
Identify blocked checks individually. A production build proves that the bundle
builds; offline fixtures prove only the behaviors exercised. Neither establishes
manufacturer integration, complete OGC/MPSS conformance, or a demonstrated profile
advantage.

The separate server-to-client evaluation requires an authorized, source-grounded
read path and known records. Do not turn its absence into a reason to rewrite the
profile, invent observations, load fixtures into a server, or change existing
infrastructure during this increment.

Return to the [documentation index](../README.md).
