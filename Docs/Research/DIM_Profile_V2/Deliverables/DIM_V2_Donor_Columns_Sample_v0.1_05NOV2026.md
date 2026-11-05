# DIM V2 — donor columns → proposed DIM: small layout sample

**Trial only, not an adopted model or comprehensive donor mapping.** Seven donor families are used only to test your preferred side-by-side layout. The donor columns run **left to right in increasing numbers of populated candidate correspondences within this small sample**, not in order of quality or final importance. The last/rightmost column is the proposed DIM element.

**Legend:** `≈` = partial or related, **not exact equivalence**; plain text = a direct or conditional field-level alignment. Empty cells mean *no correspondence established in this sample*, not a claim that the donor lacks the concept. The first workbook sheet should look like this, with each section a full-width divider row.

<table>
<thead><tr>
<th>IEEE 1451 (public 2024 evidence)<br><small>5 sample rows</small></th>
<th>OGC OMS 3.0<br><small>5 sample rows</small></th>
<th>OPC UA Devices<br><small>6 sample rows</small></th>
<th>W3C SOSA/SSN<br><small>6 sample rows</small></th>
<th>SensorML 3.0<br><small>8 sample rows</small></th>
<th>SAPIENT v2<br><small>9 sample rows</small></th>
<th>CSAPI Parts 1–2<br><small>12 sample rows</small></th>
<th><strong>PROPOSED DIM ELEMENT</strong></th>
</tr></thead>
<tbody>
<tr><th colspan="8">▣ 01 — IDENTITY &amp; DESCRIPTION — Identify a manufacturer, reusable model, particular unit and API identity without collapsing them.</th></tr>
<tr>
<td></td>
<td></td>
<td>Manufacturer</td>
<td></td>
<td></td>
<td>ConfigurationData.manufacturer</td>
<td></td>
<td><strong>Manufacturer name</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Model</td>
<td></td>
<td>≈ typeOf → model process</td>
<td>ConfigurationData.model</td>
<td>≈ systemKind → Procedure</td>
<td><strong>Product model designation</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td>SerialNumber</td>
<td></td>
<td></td>
<td>≈ ConfigurationData.serial_number</td>
<td></td>
<td><strong>Individual hardware serial number</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>≈ uniqueIdentifier</td>
<td></td>
<td>uniqueIdentifier / uid</td>
<td><strong>Persistent System identifier</strong></td>
</tr>
<tr><th colspan="8">▣ 02 — SYSTEM, EQUIPMENT &amp; RELATIONSHIPS — Describe the whole, physical constituents, separate connections, reporting participant and hosting context.</th></tr>
<tr>
<td></td>
<td></td>
<td>≈ Device</td>
<td>≈ ssn:System</td>
<td>≈ PhysicalSystem</td>
<td></td>
<td>≈ System resource</td>
<td><strong>Described sensing System / arrangement</strong></td>
</tr>
<tr>
<td>≈ Network Capable Application Processor (NCAP)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>≈ Node (registered network role)</td>
<td></td>
<td><strong>Network-visible participant</strong></td>
</tr>
<tr>
<td>≈ Transducer Interface Module (TIM)</td>
<td></td>
<td>≈ ComponentType (can include software)</td>
<td></td>
<td>≈ PhysicalComponent / components</td>
<td></td>
<td>≈ subsystems → System</td>
<td><strong>Physical constituent</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td>≈ ConnectsTo</td>
<td></td>
<td>≈ connections</td>
<td></td>
<td></td>
<td><strong>Connected external equipment</strong></td>
</tr>
<tr>
<td></td>
<td>≈ Host</td>
<td></td>
<td>≈ sosa:Platform</td>
<td></td>
<td></td>
<td>≈ System typed sosa:Platform</td>
<td><strong>Hosting platform / station context</strong></td>
</tr>
<tr>
<td></td>
<td>ObservingProcedure</td>
<td></td>
<td>≈ sosa:Procedure</td>
<td>≈ ProcessMethod</td>
<td></td>
<td>≈ Procedure (observing type)</td>
<td><strong>Observing procedure / method</strong></td>
</tr>
<tr><th colspan="8">▣ 03 — CHANNELS, OUTPUTS &amp; OBSERVATIONS — Separate physical/transducer channels, output fields, observable properties, performer and performed event.</th></tr>
<tr>
<td>TransducerChannel</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>Addressed transducer channel</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td>≈ outputs / named fields</td>
<td></td>
<td>≈ DataStream resultSchema</td>
<td><strong>Reported output field</strong></td>
</tr>
<tr>
<td></td>
<td>ObservableProperty</td>
<td></td>
<td>sosa:ObservableProperty</td>
<td></td>
<td></td>
<td>≈ DataStream observedProperties</td>
<td><strong>Observed / observable property</strong></td>
</tr>
<tr>
<td></td>
<td>Observer</td>
<td></td>
<td>≈ sosa:Sensor</td>
<td></td>
<td></td>
<td>≈ System typed sosa:Sensor</td>
<td><strong>Observer / observing System</strong></td>
</tr>
<tr>
<td></td>
<td>Observation</td>
<td></td>
<td>sosa:Observation</td>
<td></td>
<td></td>
<td>≈ Observation resource</td>
<td><strong>Performed Observation</strong></td>
</tr>
<tr><th colspan="8">▣ 04 — CONFIGURATION &amp; CONTROL — Differentiate supported/default capabilities, applied/reported configuration and actual command execution.</th></tr>
<tr>
<td>≈ SampMode (sampling capability)</td>
<td></td>
<td></td>
<td></td>
<td>≈ modes (declared)</td>
<td>ModeDefinition.mode_name</td>
<td></td>
<td><strong>Supported operating mode</strong></td>
</tr>
<tr>
<td>≈ SDefault (sampling mode default)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>ModeDefinition.mode_type=DEFAULT</td>
<td></td>
<td><strong>Declared default mode</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>StatusReport.mode</td>
<td></td>
<td><strong>Source-reported operating mode</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>≈ Task</td>
<td>≈ Command</td>
<td><strong>Issued control request</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>≈ TaskAck.task_status</td>
<td>≈ CommandStatus.statusCode</td>
<td><strong>Command acknowledgement / reported outcome</strong></td>
</tr>
<tr><th colspan="8">▣ 05 — SOURCE, EVIDENCE &amp; REPRESENTATION — Deliberate unmatched proposal rows: unsupported equivalence is not concealed by a blank cell.</th></tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>Source-qualified assertion (proposed DIM)</strong></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><strong>Original event and derived digital representation (proposed DIM)</strong></td>
</tr>
</tbody>
</table>
**Why there are unmatched rows:** The final two rows are intentionally not assigned to donors. Those are proposed evidence/provenance needs, not claimed original source equivalences. Your review should decide whether the DIM needs them and how they fit the model.

**Why the column order is provisional:** These counts are based on 22 sampled DIM rows and correspondences, including partial relationships. They are not a 182-source or all-donor popularity measurement. We should recalculate from source-verified mappings when the full crosswalk is built.

**Supporting files:** [Editable sample data and per-cell locators](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.json), [flat CSV for Excel](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.csv), [source-by-source evidence table](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026_Evidence.csv), [original 2017/2023/2025/2024 donor research](../Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md), [candidate DIM](../Candidate_Specification/DIM_Profile_V2_Proposed_Research_Candidate_DIM_v0.1_03NOV2026.md).

**Review questions:** (1) Are the group dividers and order intuitive? (2) Can you find what you expect? (3) Are the remaining distinctions that need their own rows obvious? (4) Is the fixed donor order useful? (5) Is the far-right DIM concept wording sensible?
