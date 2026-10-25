# Smart Citizen experiment plan

Prepared 24 October 2026. **Proposed next work; implementation has not started.**

## Purpose and baseline

Use one real, open environmental sensing system to test whether the DIM and
MPSS let MERLIN reconstruct useful operator meaning after integration. The first
question is practical: **what is this resource, what has it actually reported,
when did each report apply, and what can we responsibly say about its equipment,
power, communications, and condition?**

The technical baseline remains
[MPSS v0.3.5](../Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx),
including its existing R01–R20 meanings. The display baseline is the recovered
[560 × 440 Resource Details template](../Design/RESOURCE_DETAILS_TEMPLATE.md).
This experiment does not revise either baseline by implication. It exercises a
useful subset of the whole-system scope; TRSS and OmniSense remain reference
cases, and eight information subjects do not require eight populated panels.

The [candidate research report](../Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md)
records why Smart Citizen is the recommended first specimen and AirGradient an
independent follow-up. The
[access evidence](../Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json)
records the bounded public-source checks. This plan proposes work beyond filing
that research: no purchase, account creation, adapter, deployment, device command,
or live backend change is performed by publishing it.

The [maintained experiment paper](../Research/Studies/Smart_Citizen/README.md)
and its [study protocol](../Research/Studies/Smart_Citizen/MANUSCRIPT.md)
record the research questions, mapping method, coverage assessment, comparative
evaluation, and evidence requirements. This plan applies that method to the work
sequence. **Public live integration comes first, accompanied by deterministic
captures; owned hardware is a later extension.** Neither document records an
executed Smart Citizen adapter, CSAPI dataset, or interface comparison.

## Recommended immediate experiment: public live data and reproducible captures

Use the already inspected public API record **19639** as the first candidate,
checking its current suitability before the live run. Its response identifies
Smart Citizen Kit 2.3. A successful read on
**24 October 2026 at 21:57:35 UTC** established accessible data at that time;
it does not establish current availability whenever this document is read.

| Evidence in the captured response | Interpretation to preserve |
| --- | --- |
| Device registration `19639` and its UUID | Source record identifiers; durable physical-device identity remains unestablished. |
| Temperature, catalogue sensor `55`: **19.82 ºC**, `21:55:12Z` | Source value, unit, definition, channel and individual report time. |
| Battery, catalogue sensor `10`: **99%**, `21:55:12Z` | Source-reported remaining battery level; no supplied runtime, charging state, battery serial, or capacity. |
| PM2.5, catalogue sensor `194`: **10.6 ug/m3**, `21:46:09Z` | An older individual reading than the record's latest report; no established fault or staleness threshold. |
| Wi-Fi RSSI, catalogue sensor `220`: **−45 dBm**, `21:55:12Z` | Reported radio signal measurement; not proof of end-to-end availability. |
| SD-card indicator, catalogue sensor `221`: **1**, `21:55:12Z` | Preserve the supplier's indicator definition. Its `0` means absence or corruption; do not reduce it to a universal health score. |
| Temperature history, 23 October `00:00Z` to 24 October `00:00Z` | **24 groups with one-hour average aggregation**; response-wide `sample_size=1439` counts readings examined, not samples per group. Preserve `rollup=1h`, `function=avg`, returned times and query limits. |

These readings are a dated specimen, not measurements from a kit we own. Keep
the original source capture and retrieval metadata distinct from a reviewed
publishable excerpt, the normalized representation, and the rendered display.
Raw responses can contain owner/account-related fields; a fixture should contain
only reviewed fields needed for the experiment, with omissions and derivation
recorded. Record source URL, capture time, response hash, selected fields and
transform revision so later work is reproducible.

The proposed dataset includes registration and model metadata, reported channel
inventory, definitions, units, subject/time context, integration provenance,
current readings, and bounded history. Select varied supported meanings:
temperature and humidity, particulate mass and particle-number concentration,
light or pressure, noise level, battery percentage, radio signal strength, and
the SD-card indicator. Preserve the distinction between source-reported facts,
documentary model information, integration-created facts, and unresolved content.

Temperature and battery percentage can form the **first trace through the
integration chain**, but they do not define the whole proposed dataset. The older
PM2.5 reading and averaged history are discriminating temporal cases. Additional
channels and metadata test different meanings rather than merely increasing the
record count. Public data can support a substantial observation-rich specimen;
they do not establish complete physical deployment, power, control, or lifecycle
coverage. A purchase is not required for this first experiment.

## 1. Establish the source-to-standard mapping

Use the [published Smart Citizen API reference](https://developer.smartcitizen.me/),
its human-readable schema and endpoint descriptions, sensor/measurement metadata,
and actual captured responses together. A complete machine-readable OpenAPI or
JSON Schema contract for the exact deployed native API **has not yet been
verified**; this does not establish that none exists. Compare the documented
meaning with observed payloads. If implementation code resolves an ambiguity,
record its revision without assuming it is the version deployed publicly.

Use the selected target-standard schemas and MPSS rules to construct the
representation. A target-schema check establishes only its tested structural
constraints; preserving identity, subject, quantity, units, and time requires
separate semantic review.

For each selected field, record the exact JSON location, original value and
definition, subject, unit, time meaning, OGC carrier, applicable MPSS binding,
presentation decision, and unresolved question. Distinguish supplier facts,
standard mechanisms, existing MERLIN rules, and new experiment choices.

For every mapping, also explain its underlying DIM concept and each individual
donor-source concept invoked, using the paper's mapping-explanation requirements.
Give the donor term or identifier, edition, exact section or object, inline
citation, and the meaning reused or adapted. Distinguish that contribution from
the CSAPI resource and SensorML/SWE carrier, and identify project-authored choices
or any equivalence that remains unestablished. A general list of standards or a
JSON destination does not complete the semantic explanation.

| Source concern | Proposed mapping work and boundary |
| --- | --- |
| Identity and model | Apply R01/R02 distinctions. The API documents that a physical device may be registered more than once. Neither the registration ID nor its UUID is automatically a manufacturer serial. Local integration resource URIs may identify our representations if their limited meaning is explicit. |
| Channels and equipment | `sensor_id=55` identifies a shared sensor catalogue entry. The API documents a component as a device-to-sensor database association; history supplies `component_id=4039417141`. Neither is a physical serial. Channel availability alone does not prove a separately identified physical component. |
| Products and observations | Use R10/R11 to distinguish declared capabilities, available streams, observations, producer and observed subject. Preserve supplied property definitions and units; select an appropriate native sampling subject without inventing one from a display label. |
| Time and aggregation | Establish what `last_reading_at` and historical aggregate timestamps mean before choosing `phenomenonTime` or `resultTime`. Keep retrieval time separate. Returned hourly timestamps are not all exact hour boundaries; do not invent precise averaging intervals or per-bin sample counts. |
| Power | Apply R17 to the supplier's battery-percentage meaning. Do not relabel it as an RFC 7577 field solely because both concern batteries. R16 supply relationships require evidence of the arrangement and endpoints; percentage alone supplies neither. |
| Communication and condition | Preserve RSSI and SD-card meanings under appropriate typed values and subjects. R20 does not authorize a fabricated readiness assessment. API record state and Wi-Fi measurements do not automatically supply a physical link graph or sensor operating mode. |
| Provenance and missing data | Apply the existing provenance distinctions, including R15 where appropriate. Preserve unsupported native metadata for competent generic inspection; record unknown, absent and unavailable values without converting them to zero, false, or “healthy.” |

Use existing SensorML, CSAPI and SWE Common mechanisms first, following the
profile's selected bindings. Smart Citizen's native REST API is not thereby an
OGC endpoint. Any transcription or adapter is our authored integration work;
record its exact mapping and limits. A declared profile link is not a conformance
certificate. Record integration decisions explicitly. Classify discrepancies as
**source omission**, **mapping defect**, **profile gap**, or **presentation issue**
before proposing a change; retain uncertain classifications for review.

**Completion:** a reviewer can trace every proposed displayed fact to a source
field and every semantic enhancement to a documented rule. Unresolved mappings
remain explicit; they need not block supported fields.

## 2. Integrate public live readings through CSAPI

The immediate end-to-end experiment is **public Smart Citizen source → our
documented adapter → an OGC CSAPI service carrying the selected SensorML/SWE and
MPSS representations → Glaux's standards-aware reader → Resource Details**.
Use the documented [Smart Citizen API](https://developer.smartcitizen.me/)
as the upstream acquisition interface. Reuse an appropriate existing test service
when its current capabilities and access have been verified; identify the exact
service/version, supported publication interfaces, adapter revision, and execution
environment before the run. A direct native-JSON viewer is useful evidence
inspection but does not by itself test this OGC integration path.

Retain deterministic source captures and corresponding standardized resources
throughout the live work. These support reproducibility and focused checks;
completing a standalone fixture UI or buying hardware is not a prerequisite for
starting acquisition and integration. Preserve original acquisition metadata
separately from later replay and client-fetch metadata.

Trace identifiable source samples and their model/context metadata through
capture, mapping, publication, service retrieval, and client inspection. Verify
that references, schemas, observations, and provenance survive that chain, and
record which profile bindings were actually exercised. Validate applicable
target structures and inspect semantic correspondence separately: server acceptance
alone does not establish correct meaning or full-profile conformance.

Choose polling, caching, duplicate handling, rate-limit handling, and browser
access after checking documented and actual endpoint behavior. Introduce
additional infrastructure only for an identified need; keep account credentials
and device tokens out of public files and client code. Record actual responses,
failures, and handling decisions rather than describing an untested path as
available.

Distinguish observed/source time, API retrieval time, and our receipt time.
Refreshing an old observation must not make it appear new. Review temporary
unavailability and empty responses without inventing measurements or declaring
device failure. This bounded experiment covers read access and authored standard
representation; device controls and profile revisions remain outside its scope.

**Completion:** a reviewer can follow the selected real evidence through actual
CSAPI publication and retrieval into Glaux, with execution records, preserved
captures, and explicit limitations. No such execution is claimed by this plan.

## 3. Build deterministic and comparative Resource Details views

Use the integrated evidence and corresponding reviewed fixed captures in a
separate experiment page within the existing 560 × 440 frame. Preserve the blank
canvas for comparison. Begin with a compact Overview and a source-detail
inspection route; add Activity history for series actually captured. Do not
populate Commands with cloud record-edit operations or create empty content
merely to use every navigation label.

The page should disclose the capture date, each channel's source time, and the
meaning of any derived display value. A reader should be able to inspect native
metadata beside the mapped result. Generic handling should retain useful names,
units, definitions, timestamps and relationships. Profile-aware presentation
must earn its value through correct associations and understandable context,
rather than through deliberately weakened generic rendering.

This needs a distinct recorded-source representation: current source handling
distinguishes synthetic and remote data, and a fresh browser fetch sets a new
retrieval time. A captured-source manifest must retain original acquisition time
and URL separately from replay loading time. Do not label this real specimen
synthetic, or route battery percentage through the existing demonstration's
supply-voltage-only interpretation. These are bounded integration changes to
design, not capabilities already present in the client.

Follow the [paper's comparison protocol](../Research/Studies/Smart_Citizen/MANUSCRIPT.md#7-interface-comparison-and-figure-protocol)
for the actual Smart Citizen interface, competent generic OGC presentation, and
profile-aware Glaux. The two Glaux conditions use the same standardized evidence.
Record source registration, channel, observation or interval, aggregation, units,
capture time, application revision where available, browser, zoom, viewport, and
relevant controls for each screenshot. If the provider cannot show the same
sample or interval, identify the capture as descriptive rather than a matched
comparison. Images alone cannot demonstrate semantic correctness or profile
benefit; link findings to source records, mappings, and predefined operator tasks.

Proposed PBI acceptance examples:

- Selecting PM2.5 keeps `21:46:09Z`; the device's `21:55:12Z` does not overwrite it.
  An unknown expected cadence does not silently become an alarm.
- Battery `99%` stays source-attributed. No remaining hours, charging state,
  separate battery identity, supply edge or readiness rating appears without
  additional evidence.
- The history view says hourly average, distinguishes 24 returned aggregates
  from the 1,439 readings examined for the response, and preserves timestamp uncertainty.
- Unknown properties remain inspectable. Source-registration identifiers are
  not presented as verified physical serials, and missing classification does
  not create an “Unclassified” marking.
- At 560 × 440, identity and navigation remain usable while only body content
  scrolls. Thin native scrollbars appear for overflow without a permanent empty
  gutter; keyboard access and focus remain usable.
- The page distinguishes live retrieval from recorded replay and appears in the
  shared index with its actual change description and timezone-qualified update
  timestamp. A live request does not imply a fresh underlying observation.

Verify these risks with focused mapping tests, an overflow/keyboard review,
the existing build checks, and a small source-to-display review. Record actual
results separately from this proposal. This is a bounded client experiment,
not certification of the entire profile or proof of operational interoperability.

## 4. Acquire an owned kit later to fill physical-evidence gaps

After the public integration and specimen review, choose an exact purchasable
configuration when physical installation evidence becomes the next useful test. The
[manufacturer documentation](https://docs.smartcitizen.me/hardware/kit/) says
SCK 2.3 requires a battery even when continuously powered by USB. The
[supplier listing](https://www.seeedstudio.com/Smart-Citizen2-3-p-6327.html)
states kits shipped from July 2026 omit the UV sensor. The public specimen's
channel inventory is therefore not a promised inventory for a new purchase.
On 24 October the listing showed SKU 114993536 at **US$149, in stock**. This is
the kit's listed price, not a confirmed total including the battery, accessories,
tax and shipping. Recheck the selected SKU and package before making a budget
or order; no purchase is needed for the first public live integration and view
experiment.

Recheck the delivered sensor variant, firmware support, battery specification
and inclusion, cable/power supply, Wi-Fi needs, microSD option and enclosure
before purchase. Begin indoors at a stable location; an outdoor deployment
adds placement and enclosure decisions. Record the received model/board labels,
firmware, actual components, documented identifiers, and the separate platform
registration. If no physical serial is supplied, say so; a team-assigned asset
identifier can be recorded explicitly as ours.

Check the exact package contents: a general starter-pack assembly guide does
not establish what the selected retailer SKU includes. Firmware in the public
specimen is unestablished because its status message is filtered; record our
own kit's observed firmware instead of copying an assumed version.

Commission by collecting real observations, documenting placement and power
arrangement, and retaining a small reference sample. Team-authored installation
facts are useful evidence when their author and time are explicit. This supplies
relationships missing from someone else's public record without pretending
that the supplier API reported them.

The supported microSD/CSV route can supply an offline comparison at this stage.
Changes to placement, power, local settings, or supported physical operations
belong in that later experiment. Source views and API edits to names,
descriptions, or locations may manage records; they do not demonstrate physical
device control. Any eventual command experiment requires its own scope and must
preserve R12's distinction between request/service outcome and observed physical
effect. It is not included in the immediate public-data work.

## 5. Test transfer to AirGradient

Use a second independently produced source after the first mapping is reviewable.
[AirGradient's documented local interface](https://github.com/Open-Air-Foundation/firmware-one-openair/blob/master/docs/local-server.md)
and [public dataset](https://www.airgradient.com/documentation/kb/global-indoor-air-quality-dataset/)
offer useful comparisons. Begin with overlapping temperature/PM quantities and
their identity, subject, units and times; preserve native distinctions such as
raw versus corrected measurements and VOC/NOx indices versus concentrations.

Ask whether the same existing MPSS meanings and presentation rules work without
Smart Citizen-specific assumptions. A second supplier exposes overfitting; it
does not need to populate every domain or reproduce the same hardware. Record
where only the source adapter changes and where a real model question remains.

## What this should contribute to the maintained work

| Artifact | Concrete output |
| --- | --- |
| PBI | An operator task, bounded source assumptions, observable acceptance examples and unresolved product decisions. |
| Wireframe | A 560 × 440 example reviewed against real field lengths, missing values, differing times and overflow. |
| Profile | An R01–R20 applicability/mapping record, showing supported bindings and specific gaps without silently changing v0.3.5. |
| DIM | Evidence that source-independent concepts retain meaning across two producers, plus precisely identified ambiguities needing further thought. |

Success is a reviewable chain from **source evidence → meaning → binding →
display → operator question**, with missing links visible. The next concrete
work is the source/target mapping and public live integration, with deterministic
captures and the paper's evaluation record maintained alongside it. Report
semantic preservation, partial domain coverage, and presentation utility
separately. Hardware acquisition, physical controls, and changes to the retained
profile are not prerequisites or implicit additions to that work.
