# Details View source and implementation mapping

This companion defines the first Overview, Equipment, and Condition increment.
The subsequently authorized connected power example is specified separately in
[POWER_ARRANGEMENT.md](POWER_ARRANGEMENT.md); the limits below describe the initial
historical-device cases and technical-description contract.
It applies the existing working views to the MPSS v0.3.5 source materials and
records the additional experimental meanings needed for the selected examples.
It is not a new normative profile, a manufacturer adapter, or a claim of overall
OGC/MPSS conformity or demonstrated profile benefit.

The implementation recognizes the MPSS technical-description subset described
below. TRSS detector selections and battery estimates, the Core 2 reported list,
and Core 5 ADS condition facts use explicitly experimental bindings. A separate,
fully synthetic technical-description fixture exercises the recognized MPSS
contract; it supplies no new facts about any historical device.

Source keys and exact artifact fingerprints are in the
[source index](../Research/SOURCE_INDEX.md). Verification criteria are in
[Details View acceptance](../Testing/DETAILS_VIEW_ACCEPTANCE.md). Actual execution
results belong in the [current-work checkpoint](../Plans/CURRENT_WORK.md).

## Selected presentation

Use **Operational > Overview** as the entry point, with Equipment and Condition
as sibling subtabs. This selects the later working-view direction for this
experiment over the older Details > Summary proposal in the requirements.
Keep the compact resource frame, fixed Type/ID/Source, top and bottom marking
positions, adjacent tab levels, and in-place disclosure. Source examples without
markings must not acquire an invented Unclassified marking.

Pages 50-51 of `SRC-VIEWS` refine the older Assignment row: retain **Mission** and
**Sensor string** as distinct concepts. Show supplied values in a stable order;
retain source gaps in further operational detail. A string label is useful before
an identified Deployment exists. It does not create a Deployment, membership
period, actor, installation event or physical attachment.

The TRSS source supplies **Sensor string: MM101** and does not supply a Mission.
Do not copy MM101 into Mission. Core 2 supplies neither a mission nor a sensor
string in this excerpt; that gap does not establish that it is unassigned.

Keep three historical subjects separate: TRSS ETU-II, OmniSense Core 2, and
OmniSense Core 5 ADS. A synthetic fixture identifier identifies the test record,
not a recovered manufacturer or operational identity. Transmitter 0 and the
Core 2 number remain source identifiers with their actual roles. Core 2 is a
system label, not evidence of its product-model designation.

## Namespaces and recognition

| Prefix used below | Exact namespace | Status |
| --- | --- | --- |
| `P` | `https://schemas.example/merlin/mpss/0.3/` | Original unpublished MPSS example namespace retained through v0.3.5. Do not replace it with `/0.3.5/`. |
| `EP` | `https://example.invalid/glaux-client/experiment/v1/` | This prototype's authored experiment contract. Every `group/` and `term/` identifier here remains outside MPSS. |

An identifier written as `P` + `group/technical-description` means their exact
concatenation. Recognition uses definitions, supported carriers and value types,
required group content, and subject scope. Labels, manufacturer names, array
positions and suggestive identifier spelling do not select a semantic mapping.
Unknown content remains inspectable.

`SRC-PROFILE` section 5.2 describes the profile link scopes
`P` + `profile/system-description` and `P` + `profile/dynamic-description`, normally
through the RFC 6906 HTTP Link relation. Preserve a supplied declaration in its
permitted carrier. These links are not OGC conformance classes or implementation
certificates. The common `/0.3/` namespace alone does not establish which working
revision a producer implemented.

## Recognized MPSS technical description

The supported group is a native SensorML CharacteristicList under
`characteristics[]`, identified by the exact definition
`P` + `group/technical-description`. The JSON shape has a meaningful `label`,
`definition`, optional native `id`, and a nested `characteristics[]` array. The
connected example does not add a `type: "CharacteristicList"` member.

| Exact member definition | SWE type | Meaning retained |
| --- | --- | --- |
| `P` + `term/manufacturer` | `Text` | Organization responsible for manufacture of the described equipment or model. |
| `P` + `term/model-designation` | `Text` | Manufacturer/provider designation of the product model. |
| `P` + `term/hardware-revision` | `Text` | Hardware revision of the described equipment. |
| `P` + `term/firmware-revision` | `Text` | Firmware revision of the described equipment. |

The group contract requires at least one selected property. Each selected
single-valued definition occurs at most once **within that group**. The source
does not impose a single technical-description group per process. Keep distinct
groups separate, retaining their source labels, owners and paths; do not merge
their values or impose a global single-term rule across groups.

A meaningful producer-supplied group label is part of the selected contract.
A missing or blank label cannot be repaired by an extractor's generated fallback
and then counted as a complete recognized group. Label text does not choose the
semantic mapping: different meaningful labels with the same supported definition
and content remain eligible. Preserve unsupported members and
conflicting duplicates; do not silently choose the first value. A matching label
with another definition, or a value of the wrong type, is not the supported MPSS
term. No field is inferred simply to complete the group.

Reusable model information and instance revisions retain their owners. The
native `typeOf` link identifies the model/Procedure; model text does not replace
it. An inherited group keeps its actual model owner and reference context.
Unresolved inheritance is not a license to flatten or apply last-writer-wins
precedence. This increment does not claim a complete inheritance resolver.

Sources: `SRC-PROFILE` sections 5.3, 5.5 and R01 in section 5.6;
`SRC-CATALOGUE`; `SRC-EXAMPLES` files 01-02.

## Experimental group and term contracts

All groups and terms in this table use `EP`, including the common source/context
groups. They are application experiment definitions authored for this increment,
not additions to the MPSS catalogue. Group members retain explicit names, types,
labels and definitions. A native CharacteristicList contains allowed typed
properties; a bare DataRecord is not placed directly in its member array.

`EP` + `group/detector-options` uses a native **CapabilityList**, under the
process's `capabilities[]`, with members in the group's `capabilities[]`.
Every other selected experimental group uses a native **CharacteristicList**,
under `characteristics[]`, with members in the group's `characteristics[]`.
These are the prototype's explicit carrier choices; they do not establish
original manufacturer serialization or new MPSS placements.

| Exact `EP` group suffix | Exact `EP` term suffixes | Interpretation and scope |
| --- | --- | --- |
| `group/source-context` | `term/source-document`, `term/source-locator`, `term/assertion-basis`, `term/source-time-status`, `term/fixture-note` | Documentary provenance and the source limits of the owning experiment record. These fields do not claim MPSS representation-source provenance or an implemented native adapter. |
| `group/operational-context` | `term/mission-label`, `term/sensor-string-label`, `term/source-mode`, `term/source-report-interval`, `term/source-on-time` | Preserve separate literal operational concepts. Mode is source-qualified; report interval and on-time retain source form where units or interpretation remain unresolved. |
| `group/configured-detectors` | `term/detector-position`, `term/selected-detector-type`, `term/detector-orientation` | One group per supplied position. Position scopes the selected type and optional orientation. This is configuration, not identified composition or observed connection. |
| `group/detector-options` | `term/detector-position`, `term/supported-detector-type`, `term/orientation-constraint` | One group per position; repeated supported-type members are allowed by this experiment contract. Options are distinct from selected values and do not establish a complete joint validator. |
| `group/reported-transducers` | `term/reported-transducer-label` | Repeated source list entries are allowed and preserved in full. Each member is a reported label, not an inferred physical-device identity, connector position or subsystem link. |
| `group/battery-estimate` | `term/estimated-capacity-remaining`, `term/estimate-status`, `term/estimator-internal-battery-count`, `term/estimator-battery-nominal-voltage`, `term/estimator-external-battery-count`, `term/estimator-temperature-input`, `term/reported-message-count`, `term/reported-time-on` | Source-estimated remaining capacity and its accompanying estimator state/inputs. Counts, nominal voltage and temperature input are not newly measured battery/environment facts. |
| `group/reported-condition` | `term/reported-battery-voltage`, `term/voltage-kind`, `term/unverified-source-clock`, `term/source-mode`, `term/source-report-interval`, `term/source-on-time` | Report-qualified voltage and accompanying literal report context for the owning Core 5 ADS example. Preserve numeric volts and the source's DC qualification separately. The raw clock remains unverified text. The three literal report-context terms are also permitted in operational-context; their placement does not change their meaning. |
| `group/reported-diagnostics` | `term/diagnostic-finding` | Repeated individual source findings are allowed. Retain each distinct member name, source label and Category value. The labels identify report entries, not new physical components. No aggregate readiness inference is defined. |

The semantic selectors above are authored for the test representations. They do
not assert that a manufacturer payload used these paths. `SRC-VIEWS` page 54
explicitly leaves the original detector URIs and transducer-report schema
unavailable. Each representation must be identified as a source-grounded
experimental transcription or a wholly synthetic contract test, as appropriate.

### Types, code spaces and nil values

The selected experimental Category terms use these exact authored code spaces:

| Exact `EP` term suffix | Required exact `EP` code-space suffix |
| --- | --- |
| `term/selected-detector-type` | `codes/selected-detector-type` |
| `term/supported-detector-type` | `codes/supported-detector-type` |
| `term/diagnostic-finding` | `codes/diagnostic-finding` |

The term and its code-space URI are separate checks. A missing or different code
space leaves the value available for generic inspection; it does not earn this
experiment's Category interpretation. The detector tokens and diagnostic Pass
values are the selected source examples, not a newly claimed complete vendor
vocabulary.

Quantities retain the explicitly supplied expected unit: orientation `deg`,
remaining capacity `%`, nominal/reported voltage `V`, and estimator temperature
`Cel`. The count fields use Count values; context, reported time text and the
transducer labels remain Text. The prototype does not convert another unit or
coerce a numeric-looking Text value merely to match a rule.

A value matching a nil token declared by its own component is withheld from the
interpreted physical-value presentation. Preserve the original token, declaration
and reason for inspection. An undeclared sentinel-looking number is not
automatically nil, and zero remains a real supplied value unless that exact
component explicitly declares it nil. This is separate from ordinary missing,
unloaded or unsupported content.

The selected interpretation is limited to supported top-level SensorML process
groups and their immediate members. Matching definitions in unrelated nested
metadata, disputed subject scope or an unsupported carrier remain generic.

### Equipment facts and qualifications

| Subject | Preserved facts | Required qualification |
| --- | --- | --- |
| TRSS ETU-II | Detector 1: SEISMIC/ACOUSTIC. Detector 2: IRID-II. IRID-II orientation: 0 degrees. | Configured detector types; physical identities, connection confirmation and configuration time are not established. Orientation reference direction is not supplied. |
| TRSS supported choices | Detector 1: MAGID, IRID-II, SEISMIC/ACOUSTIC. Detector 2: MAGID, IRID-II, NONE. | Seismic/acoustic uses Detector 1. Orientation 0-360 degrees is unavailable for seismic/acoustic. These are limited source rules, not a complete compatibility model. |
| OmniSense Core 2 | Magnetic; Seismic (ext); Detection Switch 1; Detection Switch 2; Control Switch. | Five reported list entries. Individual identities and connector positions are not supplied. Detection algorithms are separate. Editor Last Updated does not date each detection. |

`P` + `group/equipment-role` is deliberately not used to fill these gaps. Its
actual contract requires one component-ref and one or more function-ref values;
the native `components[]` relationship must already be supported. A detector
selection or anonymous list label is insufficient evidence for those references.
Likewise, a declared sensing function or mode does not establish installed
equipment or present readiness. Sources: `SRC-PROFILE` R02/R04;
`SRC-VIEWS` pages 52-55 and its embedded equipment facts.

### Condition facts and qualifications

| Subject | Preserved facts | Required qualification |
| --- | --- | --- |
| TRSS ETU-II | 100.0% capacity estimate; collecting data for battery lifespan calculation; four internal 9 V batteries; zero external batteries; 25 degrees C estimator input; zero messages; zero days/zero hours. | Keep the estimate and collecting-data state together. The source does not establish full charge or readiness. ETU-II does not return measured battery voltage. Received-message counts can affect the estimate; no new estimator is implemented. |
| OmniSense Core 5 ADS | 15.43 V DC; source clock `12/30/99 05:00:00`; Normal mode; report interval `00:30`; on-time `0 01:00:28`. | Clock unverified; timezone not established. Preserve source duration/interval text. Do not convert voltage into remaining percentage/runtime or synthesize a trend. |
| OmniSense Core 5 ADS tests | Analog board, CPB, Local comms, Analog voltage, Digital voltage and Magnetic voltage each report Pass. | Six separate findings. No overall mission-readiness result. These values do not belong to Core 2. |

Sources: `SRC-VIEWS` pages 22-23; `SRC-REQUIREMENTS` RD-V08;
`SRC-GUIDE` section 10.1.3.

The reusable estimate rule must show the status actually supplied by the record.
The historical TRSS example's collecting-data state is not a default status for
every record containing the estimated-capacity term.

## Applying R11 and R17 without inventing a binding

R11 keeps the producing System distinct from the observed subject. Use an actual
SamplingFeature/sampledFeature relationship where the source supports it; an
embedded `subject-ref` must refine the correct owner and declared subject.
Do not create a battery identity, sampling-feature URL or Deployment merely to
complete a display. Changing the current equipment relationship must not retarget
historical observations.

R17 preserves source-supported subject, measurement point, property, unit, time
and reading-versus-rating-versus-estimate meaning. Operating readings and
method-derived estimates use appropriate dynamic representations when the
source contract is available. These historical transcriptions do not establish
a recovered native DataStream/Observation schema or a verified sample time.
Retain their limitations rather than fabricate missing observation fields.

Two existing MPSS example definitions are inapplicable substitutions here:

- `P` + `term/supply-terminal-voltage` describes output terminals of an identified
  external source in the fictional station example.
- `P` + `term/rfc7577-battery-actual-voltage` qualifies the selected RFC 7577
  batteryActualVoltage meaning. Its millivolt conversion and reserved-code rule
  belong to that separate illustration, not to an OmniSense packet.

For a source contract that actually uses a declared nil code, decode it before
unit conversion and preserve its reason. Zero is not nil merely because it is
zero. The example's `-9999`
output token is not a universal missing-value rule. R20 permits qualifying
measured/method-derived findings; it does not authorize a client-generated health
or readiness conclusion from the six source test results.

## Time, provenance and generic inspection

Keep source report time, configuration validity, description validity, deployment
applicability, observation/result times and retrieval time distinct. Retain the
Core 5 source clock as raw unverified text; do not append a timezone. Retrieving
the fixture or refreshing a server response does not make its historical reading
current or request a new device report.

Each interpreted fact should retain the original representation/selector, owning
subject, definition, typed value, supplied unit or code space, assertion basis,
relevant time meaning and known limitations. Interpretation labels distinguish
the recognized MPSS subset from the experiment mappings. They describe what the
client understands, not producer conformance.

The generic view remains competent at supported SWE types, labels, units, nested
content, arrays and native relationships. Preserve unfamiliar fields and the
original source representation even when the library's parsed model selects fewer
fields. Missing, explicit NONE, zero, declared nil, unsupported, unloaded and
denied states remain distinguishable where known. No view infers physical absence,
health or lack of assignment from missing information.

## Explicit gaps and completion limits

The device-specific selectors, full vocabularies, native report schemas,
authoritative clocks, identity correspondence and attachment relationships remain
source-integration gaps. The experimental contracts make this first implementation
reviewable without silently amending MPSS. They are not evidence that an
off-the-shelf cross-vendor UGS binding exists or that the profile improves every
selected field.

Document later findings against the specific gap. Continue working portions of
the view while unsupported content remains inspectable. This increment performs
no device control, server writes, infrastructure changes or profile revision.

Return to the [documentation index](../README.md).
