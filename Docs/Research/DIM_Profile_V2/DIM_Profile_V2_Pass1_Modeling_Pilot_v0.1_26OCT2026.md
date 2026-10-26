# Domain Information Model (DIM) / Profile Version 2 (V2) — Pass 1 Modeling Pilot

**Date:** 26 October 2026  
**Version:** 0.1  
**Standing:** Controlled **illustrative test** of the [Pass 1 Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md) candidate; **not** an adopted class model, root class, application-profile requirement, or conformance result.  
**Conventions:** [V2 Modeling Convention](DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) and [Modeling and Visualization Guide](DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md).

## 1. Question and source basis

Can the sourced distinction **an individual System is not its kind/model, method, identifier, digital representation, or output** be expressed using established modeling notation **without inventing V2 classes, associations, or identifier rules**?

The Pass 1 study describes the present subject as an individual System, characterized for the target sensing-equipment cases by Connected Systems `systemType = Sensor` and `assetType = Equipment`. The World Wide Web Consortium (W3C) and Open Geospatial Consortium (OGC) Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) Working Draft explicitly distinguishes **individual System instances** from **system types**. The distinction between one System and information about that System is also reflected in Connected Systems' System resource and its links to other resources (Open Geospatial Consortium 2025, §§ 8.5 and 9.1–9.2; W3C and Open Geospatial Consortium 2026, § 8.16).

For Unified Modeling Language (UML), the Object Management Group (OMG) specifies that an instance is shown using an **underlined** `instanceName : ClassifierName` label (OMG 2017, § 9.8.4). That notation directly addresses the specific issue raised by our identity research: **individuality is about instances, not automatically a new class**.

## 2. Working instance view

![Two distinct illustrative instances with underlined UML labels](Figures/Pass1_Individual_System_Instances.svg)

**Figure 1 — Example UML instance view (not a DIM class model).** `exampleA : System` and `exampleB : System` illustrate two **different individual** Systems of the same named source concept. These are fictional labels, not actual CSAPI identifiers or adopted naming conventions. The visible space between objects does **not** imply an association, containment, shared product model, or identity equivalence; none of those has been asserted. The notation follows the UML instance-specification convention (OMG 2017, § 9.8.4).

**Editable source:** [Pass1_Individual_System_Instances.dot](Visualization/source/Pass1_Individual_System_Instances.dot). The linked vector figure is the SVG mechanically generated from that source. Graphviz was used as an available local rendering fallback; it is **not** an OMG UML authoring/interchange model or an assertion of machine-readable UML/XMI conformance. The figure remains a **working pilot**; any later Word/PDF publication derivative must pass the existing same-source rendering review.

## 3. What was actually tested

| Check | Result and implication |
| --- | --- |
| **Concept versus instance** | **Pass.** Two underlined instance labels communicate distinct individual Systems using the existing word `System`. No `IndividualSystem` class is required or proposed. |
| **New associations or attributes** | **Pass.** The example adds **none**. It does not invent relations to Product, Procedure, representation, Observation, or identifying metadata whose detailed modeling belongs to later passes. |
| **DIM versus binding** | **Pass.** No CSAPI `uniqueIdentifier`, resource URL, `systemType`, `assetType`, JSON member, or server endpoint appears as an intrinsic UML instance slot. Those are already documented as source/binding constructs in the Pass 1 note, not accepted DIM attributes by drawing them. |
| **Meaning traceability** | **Pass.** `System` and the individual-versus-type distinction derive from the cited source traditions; the diagram's fictitious instance labels, status, and scope are clearly marked as examples. |
| **Ability to show the entire Pass 1 meaning** | **Deliberately partial.** This one object view cannot demonstrate whether two services describe the *same* equipment, how to reconcile identifiers, or what persists through replacement. Showing those prematurely would suggest unearned relationships and rules. |
| **Need for a formal conceptual class diagram now** | **Not established.** A `System` box alone would add little beyond the sourced definition. A graph linking `System` to Product/Kind, Procedures, representations and observations would predetermine Passes 2–5. |

The old illustrative infographic remains an **explanatory overview**, not a formal UML class model. Its surrounding boxes should not be promoted to UML classes or associations merely because their subjects were discussed.

## 4. Pilot verdict and next use

**The new method works for its narrow test:** a standards-recognizable *instance view* demonstrates one substantive distinction from Pass 1 without inventing the DIM's structure. The more important result is knowing **what not to draw yet**.

The [modeling convention](DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) does **not** need revision on this evidence. Keep the Pass 1 concept statement and donor-native narrative pedigree as the authoritative **candidate research explanation**; this figure is subordinate, informative, and reproducible. Do not create a new `IndividualSystem` class, define object multiplicities or identifier reconciliation, or establish a formal UML class model on the strength of this example.

**Next research step remains Pass 2 — Product / Model / Kind.** At the scheduled five-pass checkpoint, determine which relationships are sufficiently settled to warrant a small conceptual class diagram, rather than expanding this instance illustration into an assumed architecture.

## References — Chicago Manual of Style, 18th ed., author-date

Object Management Group. 2017. *Unified Modeling Language (UML)*, version 2.5.1, § 9.8.4. https://www.omg.org/spec/UML/2.5.1.

Open Geospatial Consortium. 2022. *OGC Testbed-17: UML Modeling Best Practice Engineering Report*. OGC 21-031, February 8, §§ 1.2–1.3 and 8.1–8.12. https://docs.ogc.org/per/21-031.html.

Open Geospatial Consortium. 2025. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

W3C and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21, § 8.16. https://www.w3.org/TR/vocab-ssn-2023/.
