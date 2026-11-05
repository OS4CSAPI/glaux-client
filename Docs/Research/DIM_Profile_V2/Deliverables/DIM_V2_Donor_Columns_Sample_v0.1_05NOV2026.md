# DIM V2 — donor columns → proposed DIM: small layout sample

**Trial only, not an adopted model or comprehensive donor mapping.** Seven donor families are used only to test your preferred side-by-side layout. The donor columns run **left to right in increasing numbers of populated candidate correspondences within this small sample**, not in order of quality or final importance. The last/rightmost column is the proposed DIM element.

**Legend:** `≈` = partial or related, **not exact equivalence**; plain text = a direct or conditional field-level alignment. Empty cells mean *no correspondence established in this sample*, not a claim that the donor lacks the concept. The first workbook sheet should look like this, with each section a full-width divider row.

| IEEE 1451 (public 2024 evidence) (5) | OGC OMS 3.0 (5) | OPC UA Devices (6) | W3C SOSA/SSN (6) | SensorML 3.0 (8) | SAPIENT v2 (9) | CSAPI Parts 1–2 (12) | **PROPOSED DIM** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **01 — IDENTITY & DESCRIPTION** |  |  |  |  |  |  |  |
|  |  | Manufacturer |  |  | ConfigurationData.manufacturer |  | **Manufacturer name** |
|  |  | Model |  | ≈ typeOf → model process | ConfigurationData.model | ≈ systemKind → Procedure | **Product model designation** |
|  |  | SerialNumber |  |  | ≈ ConfigurationData.serial_number |  | **Individual hardware serial number** |
|  |  |  |  | ≈ uniqueIdentifier |  | uniqueIdentifier / uid | **Persistent System identifier** |
| **02 — SYSTEM, EQUIPMENT & RELATIONSHIPS** |  |  |  |  |  |  |  |
|  |  | ≈ Device | ≈ ssn:System | ≈ PhysicalSystem |  | ≈ System resource | **Described sensing System / arrangement** |
| ≈ Network Capable Application Processor (NCAP) |  |  |  |  | ≈ Node (registered network role) |  | **Network-visible participant** |
| ≈ Transducer Interface Module (TIM) |  | ≈ ComponentType (can include software) |  | ≈ PhysicalComponent / components |  | ≈ subsystems → System | **Physical constituent** |
|  |  | ≈ ConnectsTo |  | ≈ connections |  |  | **Connected external equipment** |
|  | ≈ Host |  | ≈ sosa:Platform |  |  | ≈ System typed sosa:Platform | **Hosting platform / station context** |
|  | ObservingProcedure |  | ≈ sosa:Procedure | ≈ ProcessMethod |  | ≈ Procedure (observing type) | **Observing procedure / method** |
| **03 — CHANNELS, OUTPUTS & OBSERVATIONS** |  |  |  |  |  |  |  |
| TransducerChannel |  |  |  |  |  |  | **Addressed transducer channel** |
|  |  |  |  | ≈ outputs / named fields |  | ≈ DataStream resultSchema | **Reported output field** |
|  | ObservableProperty |  | sosa:ObservableProperty |  |  | ≈ DataStream observedProperties | **Observed / observable property** |
|  | Observer |  | ≈ sosa:Sensor |  |  | ≈ System typed sosa:Sensor | **Observer / observing System** |
|  | Observation |  | sosa:Observation |  |  | ≈ Observation resource | **Performed Observation** |
| **04 — CONFIGURATION & CONTROL** |  |  |  |  |  |  |  |
| ≈ SampMode (sampling capability) |  |  |  | ≈ modes (declared) | ModeDefinition.mode_name |  | **Supported operating mode** |
| ≈ SDefault (sampling mode default) |  |  |  |  | ModeDefinition.mode_type=DEFAULT |  | **Declared default mode** |
|  |  |  |  |  | StatusReport.mode |  | **Source-reported operating mode** |
|  |  |  |  |  | ≈ Task | ≈ Command | **Issued control request** |
|  |  |  |  |  | ≈ TaskAck.task_status | ≈ CommandStatus.statusCode | **Command acknowledgement / reported outcome** |
| **05 — SOURCE, EVIDENCE & REPRESENTATION** |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | **Source-qualified assertion (proposed DIM)** |
|  |  |  |  |  |  |  | **Original event and derived digital representation (proposed DIM)** |

**Why there are unmatched rows:** The final two rows are intentionally not assigned to donors. Those are proposed evidence/provenance needs, not claimed original source equivalences. Your review should decide whether the DIM needs them and how they fit the model.

**Why the column order is provisional:** These counts are based on 22 sampled DIM rows and correspondences, including partial relationships. They are not a 182-source or all-donor popularity measurement. We should recalculate from source-verified mappings when the full crosswalk is built.

**Supporting files:** [Editable sample data and per-cell locators](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.json), [flat CSV for Excel](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.csv), [source-by-source evidence table](DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026_Evidence.csv), [original 2017/2023/2025/2024 donor research](../Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md), [candidate DIM](../Candidate_Specification/DIM_Profile_V2_Proposed_Research_Candidate_DIM_v0.1_03NOV2026.md).

**Review questions:** (1) Are the group dividers and order intuitive? (2) Can you find what you expect? (3) Are the remaining distinctions that need their own rows obvious? (4) Is the fixed donor order useful? (5) Is the far-right DIM concept wording sensible?
