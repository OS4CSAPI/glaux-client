# Existing power arrangement demonstration

This implementation companion describes the original synthetic source A/B
replacement example from MPSS v0.3.5. Its purpose is to make the existing power
relationship model inspectable from the selected sensing System: which external
source supplies it at a stated time, why that source changed, and which subject
the supplied voltage reading describes.

This is a bounded implementation of existing example content. It does not create
a new power profile, complete the proposed battery specialization, establish
manufacturer integration, or demonstrate whole-profile/RFC conformance. The
TRSS and OmniSense examples remain separate. Their experimental fields are not
used to populate this arrangement.

## Sources and kinds of authorship

| Layer | Source and meaning | What this demonstration uses |
| --- | --- | --- |
| Donor concepts | [RFC 7326 sections 6.2 and 6.6](https://www.rfc-editor.org/rfc/rfc7326.html#section-6.6): energy-relevant equipment and distinct power-source, metering and aggregation relationships. | The directed `powers` meaning, at the equipment granularity supported by the original records. A relationship alone does not establish active electrical flow. |
| Native OGC carriers | [CSAPI Part 1](https://docs.ogc.org/is/23-001/23-001.html), [Part 2](https://docs.ogc.org/is/23-002/23-002.html), [SensorML 3.0 JSON](https://schemas.opengis.net/sensorML/3.0/json/) and [SWE Common 3.0 JSON](https://schemas.opengis.net/sweCommon/3.0/json/). | System/Deployment descriptions, native links and identities, CharacteristicList/Event content, typed values, DataStream/schema/Observation roles. |
| MERLIN profile binding | MPSS v0.3.5 sections 5.8 R11, 5.10 R16/R17, 5.11 R18/R19, 5.14.3 and 6.6; its original catalogue and connected example. | The exact energy-relationship group, reference terms, code space, applicability convention, replacement-event meanings and illustrative source-terminal quantity. These bindings are authored by MERLIN. |
| Application presentation | This client and its explicit local catalogue. | Source/consumer explanation, three selected view times, record inspection and source disclosures. Neither the RFC nor MPSS mandates this screen layout or these controls. |

The original Power Source recommendation selected RFC 7326 as the organizing
model and RFC 7577 as its preferred battery donor. The accepted main-profile R16
increment already supplied the relationship contract below. Detailed Energy
Object/interface/battery groups, charging, estimates and enriched solar/controller
examples remained separate decisions. Their unfinished status does not remove
the accepted R16 content.

RFC 7577's separate `batteryActualVoltage` illustration in files 31–33 is not
part of this bundle. The selected sources A/B are external-source Systems;
their records do not establish that either is a battery. No battery-specific
meaning, millivolt conversion, polarity, DC/AC qualification or nil token is
imported from that separate illustration.

## Original artifacts and fingerprints

The original profile, complete connected-example ZIP, and Power Source
recommendation are now published through the [Artifact Register](../ARTIFACT_REGISTER.md).
The application's runnable fixture still selects seven explicitly synthetic JSON
response bodies. They are unchanged, including unrelated content and links outside
that selected bundle. Its `manifest.json` is an authored demonstration catalogue;
publishing the full source package does not change the runtime's bounded inputs.

| Original artifact | SHA-256 |
| --- | --- |
| [MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx](MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx) | `8096648ea481822ae7f98fd5bdd1443851b4bcf47556392de5a713a3b6ffa4f8` |
| [MERLIN_Profile_v0.3.5_Connected_Example_and_Definitions_17OCT2026.zip](MPSS/MERLIN_Profile_v0.3.5_Connected_Example_and_Definitions_17OCT2026.zip) | `b45c7ce801adafb939e5f48231fd85a9dbae13ef6d3ce528a3fc1c7b0ce94b1f` |
| Original `MPSS_v0.3.5_example/domain_catalogue.json` | `1f974ed2428e696efc0cb7cfe7193062c6493278ea7fcdf4df0fdad121823837` |
| Original `MPSS_v0.3.5_example/00_manifest.json` | `ce3442f4b22acac3266499128a33104240d0e77ec58077be95d9af1a784c0dc0` |
| [MERLIN_Power_Source_Domain_Model_and_Main_Profile_Binding_Recommendation_v0.1_14OCT2026 (1).docx](../Research/Reports/MERLIN_Power_Source_Domain_Model_and_Main_Profile_Binding_Recommendation_v0.1_14OCT2026.docx) | `cf2004793fe67c6b923b6d807ec3950a161891dccdd5d96746288f6c450ae2c4` |

The recommendation's sections 2.2, 5–9, 11 and 14 explain the intended connected
operating view and proposal boundary. The v0.3.5 profile and actual example
bodies determine this increment's supported contract. The recommendation's richer
fictional batteries, interfaces, controller and solar source are not silently
treated as present in those bodies.

### Public response-body inventory

All files below are in [public/fixtures/power-arrangement](../../public/fixtures/power-arrangement).
Canonical references are copied from the original package manifest. Their
`https://demo.example/csapi/` prefix is abbreviated below only for readability.

| Original filename | Canonical resource suffix | SHA-256 |
| --- | --- | --- |
| `02_station.sml.json` | `systems/station-01` | `51f8378cfa8fa52db0d09d3ed15be12f048589ffe8c874ab5763b4ce6d42b32c` |
| `05_power_a.sml.json` | `systems/power-a` | `01769d8b4d15aa8f34f9e25014cde106ebc36f566ef61ee64c497a59fc6e566e` |
| `06_power_b.sml.json` | `systems/power-b` | `fffdab778a5cdfc17011a7304d2830b8828de985456a0c0d29ebd6a226c3766b` |
| `08_site_deployment.sml.json` | `deployments/site-01` | `3f6afc0628e407454449a63861877c2fe08855887ae1dc41ae68fa3df064f46b` |
| `16_power_stream.json` | `datastreams/power` | `e72925267bc72d7d21f30787d25fc4fbecd44147236fb63c37e5afb88b86e22d` |
| `17_power_schema.json` | `datastreams/power/schema?obsFormat=application/json` | `b9f2c02529d0902f88a42358a93dd2b0a53d03558eed2479fca994fab6d6fa8f` |
| `18_power_observation.json` | `observations/power-01` | `bc468c6719c66a89a1299540ee9cfc1e38df04e6ab156026a7038a8c314fb904` |

## Exact supported relationship contract

`P` means the unchanged unpublished example namespace
`https://schemas.example/merlin/mpss/0.3/`. The working document version does not
change this base to `/0.3.5/`.

R16 uses an id-bearing native CharacteristicList under `characteristics[]` with
definition `P/group/energy-relationship` and a meaningful supplied label. Its
immediate `characteristics[]` contains exactly one of each selected term:

| Definition | SWE type and value |
| --- | --- |
| `P/term/relationship-subject-ref` | Text URI identifying the relationship's subject |
| `P/term/energy-relationship-kind` | Category with code space `P/codes/energy-relationship` |
| `P/term/relationship-object-ref` | Text URI identifying the relationship's object |

The catalogue distinguishes `powers`, `meters` and `aggregates`. Only `powers`
is instantiated here: the subject supplies the object. No meter or aggregator is
created by this example. A different relationship kind cannot be rendered as a
supply link merely because its endpoints look familiar.

Deployment-specific groups carry their owner and named Time conditions:
`P/term/effective-from` is inclusive and `P/term/effective-until` is exclusive.
The original conditions use
`uom.href = http://www.opengis.net/def/uom/ISO-8601/0/Gregorian`.
Those conditions are profile-authored applicability semantics, not a redefinition
of native `validTime` or an observation timestamp. Keep separate groups and their
periods; ambiguous or conflicting claims must not be silently collapsed.

## Source paths and interpretation

Paths in this table are JSON Pointers into the unchanged named body. Array
indices are evidence locators, not semantic selectors; interpretation uses the
actual definitions, typed values, identifiers and references.

| Body and paths | Supported interpretation |
| --- | --- |
| `02_station`: `/id`, `/uniqueId`, `/links/0/href`; `/outputs/2` | Identified focal System; declared `supplyVoltage` Quantity, `P/term/supply-terminal-voltage`, unit `V`. |
| `05_power_a`, `06_power_b`: `/id`, `/uniqueId`, `/label`, `/links/0/href` | Two different identified external-source Systems. Their labels do not imply battery class, ratings or condition. |
| `08_site_deployment`: `/deployedSystems/0/system` | The Deployment's explicitly referenced station and its supplied UUID. |
| `08_site_deployment`: `/characteristics/3` | `power-before`: source A powers the station from `2026-09-01T08:00:00Z` until `2026-09-02T10:00:00Z`. |
| `08_site_deployment`: `/characteristics/4` | `power-after`: source B powers the station from `2026-09-02T10:00:00Z` until `2026-09-03T18:00:00Z`. |
| `08_site_deployment`: `/history/1` | `event-swap`, definition `P/event/power-source-replacement`, at `2026-09-02T10:00:00Z`. Its `properties` entries 0, 1, 2 and 3 retain affected station, deployment, removed source and installed source; its `contacts` entry 0 supplies the maintainer. |
| `16_power_stream`: `/system@link`, `/featureOfInterest@link`, `/outputName`, `/observedProperties/0`, `/id`, `/live` | Station produces `supplyVoltage`; source B is the observed subject; stream id is `power`; `live` is false. Producer and observed subject are distinct. |
| `17_power_schema`: `/resultSchema`, `/parametersSchema/fields/0` | Result is a Quantity in `V` with the same source-terminal definition; `deploymentRef` is a declared Text context field. |
| `18_power_observation`: `/datastream@id`, `/phenomenonTime`, `/resultTime`, `/result`, `/parameters/deploymentRef` | Stream `power`, phenomenon and result time `2026-09-02T10:10:00Z`, scalar result `12.6`, deployment `site-01`. |

The catalogue's `supply-terminal-voltage` means voltage across the output
terminals of the identified external source and remains explicitly illustrative.
It is not nominal voltage, inferred state of charge, available runtime, or a
universal health assessment. The stream's producer/output, observed subject,
property and schema must agree before the result is presented as that reading.

R11 preserves the fixed source-B subject through history. The source replacement
changes the applicable R16 relationship; it does not relabel an earlier reading
as belonging to the newly installed item. R17 preserves the quantity, point,
unit and times. No extra terminal resource or pre-replacement reading is created.

## Time views and missing evidence

| View | Selected source instant | Arrangement and available reading |
| --- | --- | --- |
| Before replacement | `2026-09-01T08:00:00Z`, from `08` `/characteristics/3/conditions/0/value` | Source A supplies the station. No voltage observation at or before this instant is included. |
| At replacement | `2026-09-02T10:00:00Z`, from `08` `/history/1/time` | A's interval has ended and B's interval begins; the replacement event applies. The supplied voltage observation is still in the future. |
| After replacement, default | `2026-09-02T10:10:00Z`, from `18` `/phenomenonTime` | B supplies the station. Its one supplied observation reports 12.6 V at this time. |

These controls select interpretation times in a historical synthetic example;
they are not a live clock, device commands or newly requested measurements.
The original package's `timeView` of 10:20 is not another sample. The service
review at 10:15 and later recovery remain in the source body; neither is a
completed past event at the default 10:10 view. The administrative service review
is explicitly not a condition/readiness determination.

“No supplied observation” means missing evidence in this bundle, not a zero
reading, failed source, absent equipment or unmeasured operational impossibility.
The completed replacement event does not prove instantaneous physical work,
hot-swapping, uninterrupted power or engineering compatibility.

## Read-only capture and local catalogue boundary

[`src/data/power-example.ts`](../../src/data/power-example.ts) fetches the new local
manifest and its seven fixed sibling files through existing `captureResource`.
It retains actual request/final URLs, response bytes, decoded text, JSON,
Fetch-exposed headers, status and retrieval time. Each body gets its own
`extractStandardModel` projection, using the actual pinned library. The bundle
does not merge unrelated equipment identities into the station's standard model.

The manifest maps each canonical example identity to a local filename. Its
`role`, `sha256`, `mediaType`, view-time locators and schema `datastreamRef` are
packaging metadata. In particular, `datastreamRef` explicitly associates the
schema with the catalogued stream; it is not inserted into either native body.
The captured HTTP media type remains separate from the manifest's original
representation media type. Source hashes record the copied bytes; they are not
a producer signature or a claim of runtime authenticity verification.

No request is made to `demo.example`, and no `/schema`, `/details`, observations
or deployment route is guessed. Links to the original model, gateway, mast,
campaign, communications and command examples remain source content; unbundled
targets are unresolved in this demonstration. Failed HTTP/JSON responses retain
any captured body and their error, so Standard inspection can explain a partial
bundle without using failed responses as operator facts.

## Scope and verification

This demonstrates the accepted coarse supply relationships, replacement and
correctly scoped reading. It does not implement the complete proposed Power
Source module, server collection discovery, generalized graph traversal, a
history service, native RFC MIBs, native vendor adapters or device controls.
Original artifacts were not claimed to pass a complete base-schema suite; using
the pinned parser is not that claim. Unknown/unrecognized content stays available.

Verification must cover byte preservation, each independent resource identity,
exact group/type/code-space/time recognition, the replacement boundary, future
observation suppression, absent/failed/conflicting references, schema/stream and
subject mismatches, and per-record Standard inspection. The fixture copy was
compared byte-for-byte with the selected originals. Execution results for the
integrated client belong in [CURRENT_WORK](../Plans/CURRENT_WORK.md); this mapping
document does not assert a test result or deployment outcome.
