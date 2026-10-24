# Open sensor candidates for MERLIN DIM and MPSS experiments

Research date: **24 October 2026**. Status: **research findings and recommendations**.
This report preserves the candidate assessment requested by the project owner.
The accompanying [Smart Citizen plan](../../Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md)
is proposed follow-on work. The [access evidence record](../Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json)
contains reviewed response excerpts and the available acquisition metadata.

## Recommendation

**Begin with Smart Citizen Kit 2.3, using an already accessible public specimen
before purchasing hardware. Use AirGradient as the first independent comparison.**
Smart Citizen combines public current and historical readings, documented
equipment, open project resources, and an attainable physical kit. Its actual
data already expose useful modeling questions: registration versus physical
identity, individual channel timestamps, battery percentage, communication
measurements, storage indicators, and aggregated history.

Use a small portfolio over time. Meshtastic/RAK adds communications and controlled
field configurations; AudioMoth adds recorded acoustic products; OpenEEW adds
seismic waveforms and historical deployment metadata; Safecast adds moving
radiation measurements. Each extends a different part of the model. Buying all
of them is unnecessary for the first experiment.

The purpose is to test whether integration preserves enough meaning for a useful
MERLIN Resource Details view. These candidates supplement the original TRSS and
McQ OmniSense II reference cases. Environmental readings are an accessible first
specimen, not a replacement definition of the domain.

## Baseline and assessment method

The retained technical baseline is
[MPSS v0.3.5](../../Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx).
The presentation baseline is the recovered
[560 × 440 Resource Details frame](../../Design/RESOURCE_DETAILS_TEMPLATE.md).
The model covers eight connected information subjects:

| Information subject | What a useful experimental source can expose |
| --- | --- |
| Identity and technical description | Which physical system, model, revision and description are actually identified? |
| Equipment and physical arrangement | Which components, supports and relationships are known? |
| Sensing functions, capabilities and products | What can be produced, and which observations or products actually exist? |
| Deployment and employment | Where, for what purpose, over which interval, and under whose responsibility? |
| Configuration and actions | What is configured, what was requested, and what effect was observed? |
| Communications and access | Who produced the information, which gateway represented it, and what links are evidenced? |
| Power arrangement | Which resource powers or measures which subject, and when? |
| Condition, service and lifecycle | Which condition is measured or derived, and which events are administrative history? |

Candidate selection considers accessible sample data, physical availability,
documentation, hardware/software/data openness, inspectable UI examples, and
the particular modeling questions each can test. It does not assign a
whole-profile conformance score.

Three evidence levels are kept separate:

1. **Direct access check:** an endpoint or file returned a response that was
   inspected on the research date. This establishes that specific access result.
2. **Documented capability:** an official manual, schema, repository or supplier
   describes something. It has not necessarily been exercised on hardware here.
3. **Proposed use:** our judgment about how that evidence could test the DIM,
   profile or client. This is not a supplier claim or an implemented binding.

No physical device was operated in this study. No candidate is asserted to be a
native implementation of MERLIN's profile or an already integrated OGC resource.
Public civilian documentation supplies useful examples; it does not supply a
formal classification marking for imported records. A source API must still be
mapped deliberately into the selected CSAPI, SensorML and SWE Common mechanisms.

## Shortlist and acquisition observations

Prices and availability below were observed on **24 October 2026** and require
rechecking before ordering. They are listed product prices, not delivered quotes.
Tax, shipping, regional variants, batteries, host computers and enclosures may
add cost. Sources and configuration limits appear in each candidate section.

| Candidate | Useful first role | Access established | Listed acquisition option |
| --- | --- | --- | --- |
| **Smart Citizen Kit 2.3** | First complete evidence-to-view specimen | Public current JSON and one-day grouped history | Seeed SKU 114993536: **US$149**, listed in stock; current shipment omits UV sensing |
| **AirGradient ONE / OpenAir** | Independent producer and documented local interface | Public current measurements; local API documented | ONE: **$138 kit / $230 assembled**; OpenAir: **$125 kit / $225 assembled** |
| **Meshtastic with RAK WisBlock** | Gateway, network and power/configuration experiments | Schemas and interfaces inspected; no curated measured sample archive established | Two selected RAK19007/RAK4631 kits plus one RAK1906: **$75.18** before extras |
| **AudioMoth 1.2.0** | Acoustic files, recording configuration and offline collection | Public sample WAV header inspected; tools and firmware documented | GroupGets: **$99.99** for one device; product data indicated availability |
| **OpenEEW / Grillo** | Seismic time series and time-scoped deployment metadata | Actual historical waveform and device-metadata JSONL | Public archive requires no device purchase; current Grillo One is contact-sales |
| **Safecast / bGeigieZen** | Mobile measurements, radiation units and provenance | Actual legacy and current-map API responses | Zen kit: **$475**; build/notification availability, not immediate-stock evidence |
| **senseBox** | Alternative independent environmental source | Actual openSenseMap device response | senseBox:home base **€124.95**, listed in stock; selected sensors add cost |

## 1. Smart Citizen Kit: recommended starting point

### What is available

The [official kit documentation](https://docs.smartcitizen.me/hardware/kit/)
describes modular boards, environmental sensing, Wi-Fi publication and local
microSD recording. The [project's openness page](https://docs.smartcitizen.me/about/open-source/)
distinguishes CERN OHL 1.2 hardware, GPLv3 firmware/tools and AGPLv3 platform
software. The [platform](https://smartcitizen.me/) identifies ODbL for shared
data. These are different layers of openness, not a single license for everything.
The [firmware and board repository](https://github.com/fablabbcn/smartcitizen-kit-2x)
provides an inspectable implementation.

The [Seeed product listing](https://www.seeedstudio.com/Smart-Citizen2-3-p-6327.html)
showed SKU 114993536 at **$149**, in stock. It explicitly says that shipments from
July 2026 omit the UV sensor. A public record from an earlier configuration can
therefore contain channels absent from a newly purchased kit bearing the same
2.3 designation. The kit guide also says SCK 2.3 requires a connected battery,
including when continuously powered over USB. Confirm exact package contents;
the [general assembly guide](https://docs.smartcitizen.me/guides/getting-started/kit-assembly/)
does not establish the contents of this retailer SKU.

### What was actually retrieved

An unauthenticated request to
[device registration 19639](https://api.smartcitizen.me/v0/devices/19639)
returned HTTP 200 at **2026-10-24 21:57:35 UTC**. Its `hardware` object identifies
SmartCitizen Kit 2.3. The evidence file preserves selected original fields;
the table below is a readable interpretation of that dated response.

| Reported item | Source value and unit | Individual `last_reading_at` on 24 October |
| --- | --- | --- |
| Battery SCK, sensor 10 | 99.0 `%` | 21:55:12Z |
| SHT31 temperature, sensor 55 | 19.82 `ºC`; QUDT `DEG_C` definition supplied | 21:55:12Z |
| Relative humidity | 64.85 `%` | 21:55:12Z |
| A-weighted noise | 36.51 `dBA` | 21:55:12Z |
| Wi-Fi RSSI, sensor 220 | −45 `dBm` | 21:55:12Z |
| SD-card indicator, sensor 221 | 1 | 21:55:12Z |
| PM2.5, sensor 194 | 10.6 `ug/m3` | 21:46:09Z |
| PN2.5, sensor 199 | 7600 `#/0.1l` | 21:46:09Z |

The older particulate timestamps are a particularly useful test. Displaying the
top-level latest time beside every channel would misrepresent the evidence.
An older reading does not, by itself, establish a fault: expected cadence and
an adopted staleness rule would be additional information. PM mass concentration
and particle-number concentration are also distinct quantities.

The [temperature-history request](https://api.smartcitizen.me/v0/devices/19639/readings?sensor_id=55&rollup=1h&from=2026-10-23&to=2026-10-24)
returned 24 groups with `rollup: "1h"`, `function: "avg"`, and
`sample_size: 1439`. The [API reference](https://developer.smartcitizen.me/)
defines that last field as the number of readings examined to construct the
response. It is response-wide, not a count for every group. Returned timestamps
are not all exact hour boundaries; preserve them without inventing precise bin
boundaries. The original exact retrieval time for this historical request was
not retained; only the research date is established.

### What the data do and do not mean

The API's device ID and UUID identify a registration. Its documentation allows
one physical device to have multiple registrations. A shared `sensor_id`
identifies a catalogue definition, while the historical `component_id` denotes
a device-to-sensor association. None automatically proves a physical serial.
The public response's hardware status message is filtered, so this capture does
not establish firmware revision. These identity limits belong in the mapping,
not in invented equipment records.

Battery percentage does not establish battery identity, capacity, chemistry,
charging state, runtime, an active supply relationship or readiness. The SD
indicator's description combines absent and corrupted states in value 0; value
1 alone does not prove available storage or successful recording. A noise-level
observation is not an audio waveform or detected-target classification.

**Proposed value:** begin with temperature and battery percentage, then introduce
the older particulate reading and aggregate history. This gives the view real
values and semantic limits to explain. The first useful question is: *what is
this resource, what has it reported, when did each report apply, and what remains
unknown?* A later owned kit can provide independently recorded installation,
component and power-arrangement facts unavailable in someone else's public record.

## 2. AirGradient: first independent comparison

[AirGradient ONE](https://www.airgradient.com/indoor/) and
[OpenAir](https://www.airgradient.com/outdoor/) provide environmental readings,
documented builds, and a particularly useful local interface. The listed kit and
assembled prices are in the shortlist. Those are different purchase forms; a
kit should not inherit claims about assembly testing or package contents from
another variant. The [build documentation](https://www.airgradient.com/documentation/kb/kb-diy-airgradient-models/)
and [firmware repository](https://github.com/Open-Air-Foundation/firmware-one-openair)
are inspectable; the latter identifies CC BY-SA 4.0.

The [documented local API](https://github.com/Open-Air-Foundation/firmware-one-openair/blob/master/docs/local-server.md)
includes `/measures/current`, configuration reads and configuration updates.
It exposes model/serial/firmware information and measurements in a form useful
for a local integration. Its examples are documentation, not readings we obtained
from a physical device. Raw and corrected values must remain distinguishable;
VOC/NOx indices are not concentrations. Configuration requests, accepted settings
and observed physical effects need separate treatment.

The [public indoor current-data endpoint](https://map-data.airgradient.com/map/api/v1/indoor/measurements/current)
returned HTTP 200 without authentication at **21:58:20 UTC**. One selected record,
location 102112442, reported `pm25: 4.1`, `atmp: 22.9`, `rhum: 31`, `rco2: 553`,
`pm10: null`, and `measuredAt: 2026-10-24T21:57:33Z`. These literal fields are
retained in the evidence excerpt. This cloud response supplies less equipment
metadata than the local interface; a location ID is not an established physical
serial. Local `pm02` and cloud `pm25` require a documented semantic correspondence,
not matching field names by intuition.

The [dataset description](https://www.airgradient.com/documentation/kb/global-indoor-air-quality-dataset/)
explains location/history access and reduced location precision. The
[data-sharing policy](https://www.airgradient.com/documentation/kb/kb-diy-data-ownership-and-sharing)
specifies CC BY-SA 4.0 for public API/map data; contributor/source attribution
must be carried with any published fixture. Nulls and model-dependent fields
must not become zero readings.

**Proposed value:** use overlapping quantities after the Smart Citizen mapping
is reviewable. Determine whether the same DIM concepts, bindings and presentation
rules work when field names, metadata completeness and hardware differ. Only
the adapter should be supplier-specific where the underlying meaning is shared.
The official product pages also link a dashboard demo suitable for later UI
inspection; this study did not perform a signed-in usability evaluation.

## 3. Meshtastic and RAK: communications and controlled configurations

The [Meshtastic firmware](https://github.com/meshtastic/firmware) is GPLv3.
RAK provides documented commercial hardware; this study did not establish that
every selected hardware design is openly licensed. The
[telemetry module](https://meshtastic.org/docs/configuration/module/telemetry/)
distinguishes device metrics from environmental measurements and documents
optional measurement modules. The [Python interface](https://meshtastic.org/docs/software/python/cli/)
offers a practical route from a supported connected node to an integration host.

The [RAK starter listing](https://store.rakwireless.com/products/wisblock-meshtastic-starter-kit)
and its product JSON showed the selected **RAK19007 + RAK4631** no-extra-module
variants at **$29.99** each, available. The 900 MHz variant ID is
43884034654406; the 800 MHz variant is 43884034621638. Choose the appropriate
regional radio configuration. The product's $24.99 minimum belongs to a
different variant. One [RAK1906 environmental module](https://store.rakwireless.com/products/rak1906-bme680-environment-sensor)
was $15.20 and available: two selected kits plus one module total **$75.18**,
before batteries, enclosures and delivery costs.

A plausible owned arrangement is an environmental node, a mesh path, and a
USB-connected gateway/host using the documented interface. The RAK4631 is not
a direct Wi-Fi/MQTT JSON gateway. The
[MQTT documentation](https://meshtastic.org/docs/software/integrations/mqtt/)
also distinguishes originating node from gateway sender; receive timestamps
must not silently replace measurement times. A serial integration should use
its own actual packet contract rather than assuming an identical MQTT envelope.

The [telemetry schema](https://github.com/meshtastic/protobufs/blob/master/meshtastic/telemetry.proto)
defines a battery field whose values above 100 indicate powered operation.
Treating that sentinel as “101% battery” would be an integration error. The
[MQTT schema](https://github.com/meshtastic/protobufs/blob/master/meshtastic/mqtt.proto)
separates gateway identity from packet content. These are inspected schema
facts; no measured public packet archive was verified in this study.

[Remote administration](https://meshtastic.org/docs/configuration/remote-admin/)
requires appropriate provisioning and is not a universally available control
path. The [detection-sensor module](https://meshtastic.org/docs/configuration/module/detection-sensor/)
can provide GPIO-triggered notifications, but a switch or motion trigger does
not itself classify a person or vehicle.

**Proposed value:** a later low-cost owned test of source versus gateway,
directed communications, changing configurations and power measurements.
Voltage or percentage still does not independently supply identified battery
resources or a complete power topology.

## 4. AudioMoth: acoustic products and disconnected operation

[AudioMoth](https://www.openacousticdevices.info/audiomoth) records audio to
microSD, uses three AA batteries, and supports configurable sample rates up to
384 kHz. [GroupGets](https://groupgets.com/products/audiomoth) listed AudioMoth
1.2.0 at **$99.99**. Its selected product data reported availability despite
generic sold-out markup elsewhere on the page. The package is one device;
cards, batteries and protective housing need separate checking.

The [open-source policy](https://www.openacousticdevices.info/open-source)
identifies MIT software/firmware and attribution-licensed hardware designs,
but releases the previous hardware design when a new version is developed.
The available 1.1.0 design therefore does not establish availability of every
design file for the currently sold 1.2.0 unit. The
[basic firmware](https://github.com/OpenAcousticDevices/AudioMoth-Firmware-Basic)
is publicly inspectable.

The [configuration application guide](https://www.openacousticdevices.info/config-app-guide)
documents schedules, gain, sample rate, filtering and triggers. Estimated energy
or storage requirements are predictions, not measured remaining runtime. A
battery-chemistry setting is configuration, not proof of an installed battery.
Offline files and upload times require separate modeling. Triggered recordings
can contain gaps; reconstructed playback should not invent continuous observation.

The official [AudioMoth Play](https://www.openacousticdevices.info/play) project
provides [public sample assets](https://github.com/OpenAcousticDevices/AudioMoth-Play).
The first 512 bytes of `assets/BAT.WAV` were successfully read and identified
mono, 16-bit PCM audio at 192 kHz. This verifies a reachable sample and header,
not complete field provenance or an independently verified bat-detection event.
No complete recording was archived here. Repository software licensing alone
does not settle each recording's redistribution terms.

The alternate [USB microphone firmware](https://www.openacousticdevices.info/usb-microphone)
and [AudioMoth Live](https://www.openacousticdevices.info/live) offer a documented
host-connected live path. That is a different configuration from an unattended
microSD recorder; it does not add Wi-Fi to the device.

**Proposed value:** test declared recording capability versus available media,
time spans, sample encoding, physical recorder versus upload host, and the
distinction between an acoustic product and an interpretation of its contents.

## 5. OpenEEW and Grillo: real seismic history without a purchase

The [AWS Open Data registry](https://registry.opendata.aws/grillo-openeew/)
and [OpenEEW project](https://github.com/openeew/openeew) expose historical
accelerometer data. The [sensor project](https://github.com/openeew/openeew-sensor)
is also public. Project/sensor software and designs identify Apache 2.0;
the archive data identify CC BY-SA 4.0. The current
[Grillo One product](https://grillo.io/products/grillo-one/) is contact-sales;
no purchase price was verified. Historical open designs and archived devices
must not be equated with every detail of the current commercial revision.

An unauthenticated request to a
[2017 Mexican waveform file](https://grillo-openeew.s3.amazonaws.com/records/country_code=mx/device_id=000/year=2017/month=11/day=30/hour=23/55.jsonl)
returned HTTP 200. The inspected first record identified country `mx`, device
`000`, three 32-value axis arrays, sample rate `31.25`,
`device_t: 1512086340.318`, and `cloud_t: 1512086340.369`.
The [device metadata file](https://grillo-openeew.s3.amazonaws.com/devices/country_code=mx/devices.jsonl)
also returned HTTP 200. Its selected historical row provides an effective
interval and says the vertical axis is `x`, with `y` and `z` horizontal.

The [data documentation](https://raw.githubusercontent.com/openeew/openeew/master/data/README.md)
defines acceleration in gals (cm/s²), `device_t` as the last sample's timestamp,
and `cloud_t` as cloud receipt. Array length is not sample rate; rows need not
arrive in order. Device IDs are scoped within country, and metadata intervals
use the source's inclusive endpoint convention. Do not impose the existing
power demonstration's half-open interval convention on this unrelated source.
Any clock-drift compensation or receipt-time substitution is an explicit method.

**Proposed value:** inspect waveform timing, encoding, orientation, deployment
history and derived products using actual data before choosing hardware. Only
historical access was checked; archive freshness or continuous current ingestion
was not established. Full response bodies and exact capture times were not
retained for these checks, a limitation recorded in the evidence file.

The [current Grillo sensor-details UI documentation](https://docs.grillo.io/dashboard/sensors/sensor-details)
is a useful later comparison for communications, gaps and reported health.
A gap or restart alone does not diagnose whether power, network or firmware
caused it. That documentation is not proof that the historical archive includes
all current product telemetry or that an OpenEEW dashboard was exercised here.

## 6. Safecast and bGeigieZen: mobility and radiation semantics

Safecast [publishes its data under CC0](https://safecast.org/data/).
The [bGeigieZen project](https://github.com/Safecast/bGeigieZen),
[product introduction](https://safecast.org/safecast-introduces-our-latest-open-source-geiger-counter-the-bgeigiezen/)
and [license policy](https://safecast.org/about/licenses-we-use/) provide
implementation and hardware context. The project repository identifies MIT;
hardware components and third-party material retain their own applicable terms.
GPS, SD recording, Wi-Fi publication and replaceable battery operation create
a useful deployment/mobility specimen.

The [Zen kit listing](https://bgeigiezen.safecast.jp/store-2/?model_number=V421)
showed **$475**, with units being built and notification when ready. That is not
proof of immediate stock. The listing excludes the battery for shipments outside
Japan. This is a later purchase candidate, not necessary for the first exercise.

Two unauthenticated responses were inspected:

- The [legacy measurements API](https://api.safecast.org/measurements.json?per_page=1)
  returned record 249507276, device 65001, value 40 `cpm`, captured
  `2024-08-28T09:23:51Z`, with several equipment-description fields null.
- A bounded [current-map API query](https://simplemap.safecast.org/api/latest?lat=35.6812&lon=139.7671&radius_m=1500&limit=1)
  returned record 139061733, dated `2026-09-01T12:59:12Z`, reporting
  `bGeigie-2001(1.4.4nano)`, `countRateCPS: 3` and
  `doseRateMicroSvH: 0.0748502994011976`.

The second response is an older Nano-family record, **not proof of a bGeigieZen
feed or live readings on the query date**. The evidence excerpt omits exact
record coordinates. The [map](https://simplemap.safecast.org/) and
[API interface](https://simplemap.safecast.org/map-api/index.html) expose useful
spatial access, but a platform's “latest” query can return historical data.

**Proposed value:** distinguish counts, count rates and dose-rate estimates;
preserve method and calibration provenance when available; associate moving
observations with their own times and positions rather than assigning all data
to a current device location. Full calibration and equipment history were not
established by these sample records.

## Other candidates and reasons for sequencing

### senseBox: strong alternate environmental source

The [senseBox project](https://sensebox.de/en/) and
[home documentation](https://sensebox.de/en/products-home.html) provide modular
hardware and multiple transport/storage choices. The
[store](https://sensebox.kaufen/products/sensebox-home) listed the home base at
**€124.95**, in stock; the base price does not include every optional sensor.
The project identifies PDDL 1.0 for public data.

An [openSenseMap record](https://api.opensensemap.org/boxes/5a0c347b9fd3c2001111b701)
returned HTTP 200 at **21:59:45.988389 UTC**. It identified
`homeEthernetFeinstaub`, seven channels, sensor types, units and individual
measurement timestamps. Temperature was `10.17` °C and PM2.5 was `0.60` µg/m³;
source values are strings, and zero values in other channels are not missing
data. This is a credible second-producer option. AirGradient is sequenced first
because its documented local equipment/configuration interface adds another
useful access pattern; that is a project judgment, not a performance ranking.

### AnyShake: promising owned seismic system, with unresolved fit

[AnyShake Explorer on Crowd Supply](https://www.crowdsupply.com/senseplex/anyshake-explorer)
listed a **$795** full kit and advertised stock/shipping availability. Its
[Explorer hardware/firmware](https://github.com/anyshake/explorer) and
[Observer application](https://github.com/anyshake/observer) are public and
identify AGPLv3-or-later with a commercial alternative. Geophones, acceleration,
host interfaces and waveform tools make it relevant.

The project's [license/use notice](https://anyshake.org/docs/docs-license/)
also says it is not designed or authorized for military or critical uses.
Clarify supplier fit before selecting it for a MERLIN acquisition. This is not
a claim that AGPL prohibits commercial use. Requests to the advertised
[live demos](https://anyshake.org/docs/live-demo/) returned 403 in the research
environment, so no real demo waveform was verified. Begin seismic evaluation
with the accessible OpenEEW archive; revisit AnyShake when owned seismic
hardware is the next question.

### Raspberry Shake: useful comparison, different openness and data terms

The [Raspberry Shake license page](https://raspberryshake.org/license/)
distinguishes its closed hardware/software from the open `rsudp` component and
sets specific network-data access and redistribution conditions. A publicly
viewable network waveform is not automatically a freely redistributable
repository fixture. Its UI and owned-device path may still be useful comparison
material. It is not the first recommendation for this open, shareable test corpus.

### Lower-evidence reserves

[Sensor.Community airRohr](https://sensor.community/en/sensors/airrohr/) offers
a documented DIY route and [public firmware](https://github.com/opendata-stuttgart/sensors-software).
[FieldKit](https://www.fieldkit.org/platform/) offers modular field sensing and
an application workflow. Neither received the same actual sample/price/stock
verification as the recommended first choices in this study. FieldKit's
advertised future LoRa work should not be counted as an already verified path.

## UI/UX references and what to learn from them

These references are examples of operator tasks and information requirements,
not evidence that any RFC prescribes their screen layout. This study inspected
documentation and accessible data, not a complete hands-on usability test.

| Reference | Useful design question |
| --- | --- |
| [Smart Citizen data platform](https://docs.smartcitizen.me/data/data-platform/) | Can a reader tell which kit/channel, source time, unit and history a graph represents? |
| [AirGradient product/demo entry](https://www.airgradient.com/indoor/) and local API | How are equipment, settings, live readings and corrected values distinguished? |
| Meshtastic telemetry and administration documentation linked above | How do node, gateway, radio metrics and configuration requests remain separate? |
| AudioMoth configuration, Play and Live tools linked above | How are recording configuration, file coverage, playback and derived interpretations presented? |
| Grillo sensor-details documentation linked above | Which health facts are directly reported, and which causes remain unresolved? |
| Safecast map and API linked above | How do time, motion, units and measurement method remain visible on a map? |

A manufacturer's tab arrangement need not become MERLIN's taxonomy. Extract the
question, required evidence and interaction, then test whether the shared domain
model can support it across different producers. Keep competent generic access
available; profile-aware organization should demonstrate added value against
that credible baseline.

## Implications for the four maintained artifacts

| Artifact | What this research can contribute next |
| --- | --- |
| PBI | A bounded operator task and observable acceptance examples, based on actual source limits. |
| Wireframe | Real labels, values, distinct times, absent fields and overflow cases inside the recovered frame. |
| Profile | A traceable applicability/mapping record identifying which existing binding is sufficient and which question remains open. |
| DIM | Evidence that common concepts survive a second producer, alongside precise counterexamples to supplier-specific assumptions. |

Classify an encountered difficulty before changing the model: **source omission**,
**integration decision**, **profile gap**, or **presentation issue**. For example,
an absent battery serial is a source limitation; copying a device-wide timestamp
onto all readings is an integration error. A hard-to-find source-time label can
be a presentation issue. These findings have different remedies.

The proposed order is Smart Citizen public specimen, one reviewable mapped
example in the existing frame, an exact owned kit and read-only live access,
then AirGradient. Extend to networking, acoustic products, seismic data and
radiation when their distinct questions become the next useful test. The
[experiment plan](../../Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md) turns that order
into concrete outputs and acceptance examples.

## Evidence preservation and standing

The accompanying JSON preserves selected fields, source URLs, available capture
times, access outcomes and original-body fingerprints where those bytes were
retained during research. **It is an excerpt record, not an archive of every
complete response.** A fingerprint of an original body does not make that body
recoverable from GitHub. For checks without retained bytes, missing hashes and
exact capture times remain explicit. Sample audio is linked rather than copied.

The original 14 imported project artifacts retain their bytes and versions.
This subsequent Git-native study does not renumber the v0.10 master bibliography,
assign new global source IDs, adopt a donor binding, revise MPSS v0.3.5 or create
a conformance result. Any later accepted source-selection or binding change must
be reconciled into the appropriate maintained technical and research artifacts.

Return to [Research](../README.md), the [Artifact Register](../../ARTIFACT_REGISTER.md),
or the [documentation index](../../README.md).
