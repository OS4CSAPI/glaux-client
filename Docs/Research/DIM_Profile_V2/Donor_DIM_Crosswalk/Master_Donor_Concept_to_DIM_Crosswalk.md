# Master donor-concept → proposed DIM crosswalk (working sample)

**Step06 · 6 November 2026 · editable workbook edition.** This is the approved horizontal sample presentation only: seven donors in the original provisional sample order, proposed DIM at far right; 22 proposed rows and five full-width dividers. Original semantics remain **PRIOR_SOURCE_EXTRACT_ONLY**, not independently checked publisher equivalences. See [actual editable Excel workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx), [flat CSV](Master_Donor_Concept_to_DIM_Crosswalk.csv), [structured source/evidence](Master_Donor_Concept_to_DIM_Crosswalk.json), and [Step06 limitations](Step06_Master_Workbook_Build_and_Verification_06NOV2026.md).

**Legend:** `≈` qualified partial/related/conditional, not equivalence. Empty = no established comparison among the seven sampled donors, not donor absence. Sections are navigation only; proposed DIM rows are not adopted classes.

<table>
<thead><tr><th>IEEE 1451 (public 2024 evidence)</th><th>OGC OMS 3.0</th><th>OPC UA Devices</th><th>W3C SOSA/SSN</th><th>SensorML 3.0</th><th>SAPIENT v2</th><th>CSAPI Parts 1–2</th><th style="background:#F1F6FA">PROPOSED DIM ELEMENT</th></tr></thead>
<tbody>
<tr><th colspan="8">▣ 01 — IDENTITY &amp; DESCRIPTION — Identify a manufacturer, reusable model, particular unit and API identity without collapsing them.</th></tr>
<tr><td></td><td></td><td>Manufacturer</td><td></td><td></td><td>ConfigurationData.manufacturer</td><td></td><td><strong>Manufacturer name</strong></td></tr>
<tr><td></td><td></td><td>Model</td><td></td><td>≈ typeOf → model process</td><td>ConfigurationData.model</td><td>≈ systemKind → Procedure</td><td><strong>Product model designation</strong></td></tr>
<tr><td></td><td></td><td>SerialNumber</td><td></td><td></td><td>≈ ConfigurationData.serial_number</td><td></td><td><strong>Individual hardware serial number</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td>≈ uniqueIdentifier</td><td></td><td>uniqueIdentifier / uid</td><td><strong>Persistent System identifier</strong></td></tr>
<tr><th colspan="8">▣ 02 — SYSTEM, EQUIPMENT &amp; RELATIONSHIPS — Describe the whole, physical constituents, separate connections, reporting participant and hosting context.</th></tr>
<tr><td></td><td></td><td>≈ Device</td><td>≈ ssn:System</td><td>≈ PhysicalSystem</td><td></td><td>≈ System resource</td><td><strong>Described sensing System / arrangement</strong></td></tr>
<tr><td>≈ Network Capable Application Processor (NCAP)</td><td></td><td></td><td></td><td></td><td>≈ Node (registered network role)</td><td></td><td><strong>Network-visible participant</strong></td></tr>
<tr><td>≈ Transducer Interface Module (TIM)</td><td></td><td>≈ ComponentType (can include software)</td><td></td><td>≈ PhysicalComponent / components</td><td></td><td>≈ subsystems → System</td><td><strong>Physical constituent</strong></td></tr>
<tr><td></td><td></td><td>≈ ConnectsTo</td><td></td><td>≈ connections</td><td></td><td></td><td><strong>Connected external equipment</strong></td></tr>
<tr><td></td><td>≈ Host</td><td></td><td>≈ sosa:Platform</td><td></td><td></td><td>≈ System typed sosa:Platform</td><td><strong>Hosting platform / station context</strong></td></tr>
<tr><td></td><td>ObservingProcedure</td><td></td><td>≈ sosa:Procedure</td><td>≈ ProcessMethod</td><td></td><td>≈ Procedure (observing type)</td><td><strong>Observing procedure / method</strong></td></tr>
<tr><th colspan="8">▣ 03 — CHANNELS, OUTPUTS &amp; OBSERVATIONS — Separate physical/transducer channels, output fields, observable properties, performer and performed event.</th></tr>
<tr><td>TransducerChannel</td><td></td><td></td><td></td><td></td><td></td><td></td><td><strong>Addressed transducer channel</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td>≈ outputs / named fields</td><td></td><td>≈ DataStream resultSchema</td><td><strong>Reported output field</strong></td></tr>
<tr><td></td><td>ObservableProperty</td><td></td><td>sosa:ObservableProperty</td><td></td><td></td><td>≈ DataStream observedProperties</td><td><strong>Observed / observable property</strong></td></tr>
<tr><td></td><td>Observer</td><td></td><td>≈ sosa:Sensor</td><td></td><td></td><td>≈ System typed sosa:Sensor</td><td><strong>Observer / observing System</strong></td></tr>
<tr><td></td><td>Observation</td><td></td><td>sosa:Observation</td><td></td><td></td><td>≈ Observation resource</td><td><strong>Performed Observation</strong></td></tr>
<tr><th colspan="8">▣ 04 — CONFIGURATION &amp; CONTROL — Differentiate supported/default capabilities, applied/reported configuration and actual command execution.</th></tr>
<tr><td>≈ SampMode (sampling capability)</td><td></td><td></td><td></td><td>≈ modes (declared)</td><td>ModeDefinition.mode_name</td><td></td><td><strong>Supported operating mode</strong></td></tr>
<tr><td>≈ SDefault (sampling mode default)</td><td></td><td></td><td></td><td></td><td>ModeDefinition.mode_type=DEFAULT</td><td></td><td><strong>Declared default mode</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td>StatusReport.mode</td><td></td><td><strong>Source-reported operating mode</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td>≈ Task</td><td>≈ Command</td><td><strong>Issued control request</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td>≈ TaskAck.task_status</td><td>≈ CommandStatus.statusCode</td><td><strong>Command acknowledgement / reported outcome</strong></td></tr>
<tr><th colspan="8">▣ 05 — SOURCE, EVIDENCE &amp; REPRESENTATION — Deliberate unmatched proposal rows: unsupported equivalence is not concealed by a blank cell.</th></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td><strong>Source-qualified assertion (proposed DIM)</strong></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td><strong>Original event and derived digital representation (proposed DIM)</strong></td></tr>
</tbody>
</table>

**No new mappings or original-standard verification occurred in Step06.** The mandatory owner review is still Step08.
