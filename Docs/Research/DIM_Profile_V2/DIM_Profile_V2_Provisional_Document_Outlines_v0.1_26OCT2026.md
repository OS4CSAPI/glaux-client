# Domain Information Model (DIM) / Application Profile Version 2 (V2) — Provisional Document Outlines

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Document-structure plan only. **Neither outline is a completed specification, an adopted model architecture, or a conformance claim.**  
**Workspace:** `Docs/Research/DIM_Profile_V2/` on `research/dim-profile-v2`

## 1. Purpose and standing

V2 needs **two distinguishable eventual artifacts**, not one document in which conceptual meaning and implementation obligations become indistinguishable:

- **The DIM** defines the bounded domain's concepts, meanings, relationships, and justified semantic constraints, independently of an implementation technology.
- **The application profile** selects and constrains relevant DIM meanings and establishes the requirements of their intended **Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI)** realization, distinguishing inherited OGC requirements from any carefully justified profile-authored requirements.

This separation reflects the established information-model/data-model distinction (Pras and Schönwälder 2003, §§ 2–4). **The profile supplies interoperability needs to the DIM; the DIM supplies meanings to the profile.** The document outlines are destinations for future evidence-backed work, **not containers to fill with guesses**.

**Existing material:** The [combined V2 working draft](Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md) already has preliminary sections, but it promotes chassis/anatomy conclusions derived from the subsequently **quarantined Phase B/C/D work**. Treat it as **historical candidate material, not an authoritative DIM, model architecture, or V2 profile outline**. The earlier [MERLIN Managed Physical Sensing Systems and Deployments (MPSS) profile v0.3.5](../../Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx) likewise remains predecessor evidence, **not the V2 normative baseline**. Do not transplant either artifact's requirements or headings without re-evaluation.

## 2. What established practice actually governs

| Source | Role in these outlines | Authority / limit |
| --- | --- | --- |
| Internet Engineering Task Force **Request for Comments (RFC) 3444** | Distinguishes implementation-independent information models from specific data models | Informative methodological precedent, **not** a prescribed DIM table of contents (Pras and Schönwälder 2003) |
| OGC Testbed-17 *Unified Modeling Language (UML) Modeling Best Practice Engineering Report* (21-031) | Conceptual/class modeling, consistency between model and text, machine-readable model artifacts | **Engineering Report, not an OGC Standard** (Open Geospatial Consortium 2022) |
| **ISO 19103:2024** and **ISO 19109:2025** | Geographic conceptual-schema and feature/application-schema practices where applicable | Actual International Standards, but **not a general obligation for all sensing-equipment concepts**; this outline uses publicly available scope/abstract descriptions, not a normative conformance audit (International Organization for Standardization 2024, 2025) |
| **OGC ModSpec Model, Part 1: Core, version 1.1**, 08-131r7 | Requirements classes, dependencies, standardization target types, conformance classes, and associated tests | **Approved OGC Standard** for structuring modular standards, and relevant to an intended OGC-standardization path; using the outline alone does not establish ModSpec conformance (Open Geospatial Consortium 2026a, §§ 1–2, 8–9) |
| **OGC ModSpec Model, Part 2: UML, version 1.1**, 24-065r1 | Optional extra requirements if normative UML is used as part of a ModSpec-based standard | **Optional** ModSpec UML requirements class; not triggered by including illustrative DIM diagrams (Open Geospatial Consortium 2026b, §§ 1–2, 7) |
| **ISO 19106:2004**, *Geographic information—Profiles* | Background guidance on profiles of ISO/TC 211 geographic-information standards | **Scope-limited**; does not itself make a profile of CSAPI an ISO 19106-conformant profile (International Organization for Standardization 2004) |
| **CSAPI Parts 1–2**, OGC 23-001 and 23-002, v1.0 | Concrete precedent for OGC requirements-class chapters, conformance declaration and Abstract Test Suite annexes | **Approved base implementation standards**; actual profile obligations and inherited classes must be determined later from exact editions and dependencies (Open Geospatial Consortium 2025a, 2025b) |

**Governance principle:** When future V2 text says `SHALL`, identifies a requirements class, or asserts conformity with a source standard, it must mean an actual specified and assessable obligation. Merely borrowing a diagram style, concept, heading, or author-date reference is **not implementation or conformance** to the originating standard.

## 3. Provisional outline A — the Domain Information Model

The eventual DIM document should be **self-describing and concept-centered**. These are *documentation sections*, not proposed ontology classes, DIM modules, or mandated model packages.

| Proposed section | What belongs there | When to populate |
| --- | --- | --- |
| **Front matter and standing** | Title, edition, purpose, model status, editors/change history, citation information | Skeleton now; maintain as needed |
| **1. Introduction, purpose, scope** | Problem domain, target real-world subjects, intended integration value, exclusions and assumptions; separate **domain scope** from **root-class selection** | Draft when boundary evidence is stable enough; avoid declaring the final name prematurely |
| **2. Standards foundation and modeling conventions** | Normative *only when actually applicable* versus informative sources; ontology/model dependencies; terminology; adopted [modeling convention](DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) | Reference existing method now; refine as substantive choices are made |
| **3. Conceptual model overview** | Human-readable summary and small UML class views showing established concepts and relationships, with explicit candidate/adopted standing | **After** concept consolidation, not as a substitute for it |
| **4. Concept definitions** | Reused source-native terms, definitions, identifying characteristics, applicability, relationships, exclusions, and justified new terms, if any | Accumulate incrementally from accepted concept findings |
| **5. Relationships and semantic constraints** | Association roles, inheritance where justified, composition/hosting/context distinctions, intrinsic multiplicities/constraints only when supported | After corresponding concepts are defined; no inferred cardinalities |
| **6. Common meaning and justified specialization** | Cross-family invariants, specialized concepts, dependencies, and any genuinely coherent modules/packages | Only once source evidence justifies them; **not** the old V1 bins |
| **7. Donor pedigree and mapping** | Traceable alignment to CSAPI, SOSA/SSN, SensorML, and other contributing donors; native meaning vs V2 synthesis; partial or non-equivalent mappings; evidence limits | Existing pedigree research supplies inputs; preserve cited narrative, not just a matrix |
| **8. Model governance and unresolved questions** | Model version, amendment rules, limitations, unclosed questions, change rationale, references | Start light; maintain incrementally |

**No mandated class diagram yet.** A DIM can use UML as its primary structural notation while its current research artifacts remain human-readable, sourced candidate concepts. The [existing visualization guide](DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md) governs maintained figures; diagrams do not create domain semantics merely by drawing boxes or arrows (Open Geospatial Consortium 2022, §§ 8.1–8.12).

## 4. Provisional outline B — the CSAPI application profile

The profile is a **future normative interoperability artifact**. This suggested sequence mirrors the structural logic of ModSpec and the published CSAPI standards, **without preassigning any requirements or conformance classes** (Open Geospatial Consortium 2026a, §§ 8.3–9.6; 2025a; 2025b).

| Proposed section | What belongs there | When to populate |
| --- | --- | --- |
| **Front matter** | Title, edition/status, editors, abstract, intellectual-property and security notices as relevant | Skeleton now; eventual OGC formatting process may refine |
| **1. Scope and interoperability objectives** | Intended use, in-scope systems and information, exclusions, relationship to the DIM, and the profile's purpose | When DIM boundary and use cases are sufficiently stable |
| **2. Conformance** | Precisely identified **standardization target type(s)**, selected base conformance classes, and overall conformance approach | **Later**; do not guess server/resource/representation targets |
| **3. Normative references** | Exact base standards, versions, required dependent specifications and explicitly normative vocabulary | When actual normative dependencies are selected |
| **4. Terms, definitions and conventions** | Only genuinely necessary profile terms, normative wording, identifier conventions and abbreviated terms | As obligations are specified |
| **5. Profile overview and DIM relationship** | Plain explanation of semantic selection; what is inherited, reused, constrained, specialized, or authored; informative mapping to DIM concepts | After candidate concepts and profile scope align |
| **6. Selected base-standard requirements** | Exact CSAPI Part 1/Part 2 requirements and conformance classes selected, inherited dependencies, options and applicability | After examining each relevant existing requirement |
| **7. Additional profile requirements, if needed** | Clearly identified, justified, assessable **requirements classes** grouped by actual common purpose and target type; no duplicate/redefined base obligations | Only if demonstrated interoperability gaps remain |
| **8. Representation and encoding bindings** | Selected representations, allowed additional information, linkages, vocabularies, encoding-dependent constraints; no invention where CSAPI/SensorML already suffices | After DIM concept decisions; bound to real standards |
| **Annex A. Abstract Test Suite** | One or more mapped conformance test classes and abstract tests corresponding to actual selected/authored requirements; dependencies and target types made explicit | In tandem with writing normative obligations; no untestable mandates |
| **Informative annexes** | Worked examples, correspondence tables, donor mappings, implementation notes and rationale; test data only when honestly representative | Later and clearly labeled informative |

**Not every row is a mandatory ModSpec chapter title.** The structure above is **our working table of contents**, with normative content organized in the ModSpec idiom when authored. OGC ModSpec 1.1 requires testable requirements and organized classes for standards claiming conformance; the specific sections, dependencies, normative/optional choices, and Abstract Test Suite must be completed against its actual requirements at the appropriate stage (Open Geospatial Consortium 2026a, §§ 2, 8.3, 9.1–9.5; annex A).

**Important profile classification question:** Whether the eventual V2 artifact is a selection/restriction of existing conformance classes, or also introduces additional requirements classes/extensions, remains **open**. The profile label does not by itself license unrelated new requirements, alter base-standard semantics, or imply donor-standard conformance.

## 5. Relationship and population sequence

Keep the flow explicit rather than drafting a profile backward from interface/API implementation:

1. **Now — maintain the outlines.** These tables are provisional destinations and scope controls; they are not requirements, accepted modules, or frozen chapter headings.
2. **Next — complete the five sequential concept passes.** The current checkpoint is [Pass 1: Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md). Pass 2 is Product/Model/Kind; Passes 3–5 follow the [incremental plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md).
3. **At the concept checkpoint — establish only earned model content.** Adopt or leave open conceptual definitions, relationships, and necessary constraints; decide if a compact UML view adds clarity.
4. **Then — select profile semantics and base-standard classes.** For each selected meaning, state exactly what an implementation must support, what CSAPI/SensorML already provides, and whether a genuine profile requirement remains.
5. **Finally — complete bindings and conformance.** Specify assessable requirements classes, their standardization targets and dependencies, corresponding tests, representative examples, and versioned release criteria.

A simple traceable path should remain possible:

**donor-native concept → DIM meaning/relationship → profile selection/requirement (if any) → OGC binding → conformance test (if normative).**

These are **different kinds of artifacts and claims**. A source map does not mean a source standard is implemented. A conceptual mapping does not establish profile conformance. A sample encoding does not establish a complete model.

## 6. Scope and authority controls

- **Do not** use the earlier combined V2 working draft's promoted anatomy or chassis conclusions as accepted content; preserve it as predecessor/historical material.
- **Do not** copy the older MPSS profile's requirements into V2 merely to fill an outline.
- **Do not** turn section headings into DIM classes, formal modules, conformance classes, or obligations.
- **Do not** claim compliance with ISO 19103, ISO 19109, or ISO 19106 unless relevant clauses actually apply and are assessed.
- **Do not** claim ModSpec conformity yet. It is an **applicable target for a future standards-track specification**, not an achieved property of this planning note.
- **Do** continue using donor-native terminology unless a documented semantic gap warrants V2-authored language.
- **Do** distinguish normative references, informative research sources, inherited base obligations, and new profile obligations.
- **Do** keep each normative obligation attributable to an exact edition, target, requirement class and means of assessment.

## References — Chicago Manual of Style, 18th ed., author-date

International Organization for Standardization. 2004. *Geographic Information—Profiles*. ISO 19106:2004. https://www.iso.org/standard/26011.html.

International Organization for Standardization. 2024. *Geographic Information—Conceptual Schema Language*. ISO 19103:2024. https://www.iso.org/standard/83454.html.

International Organization for Standardization. 2025. *Geographic Information—General Feature Model and Rules for Application Schema*. ISO 19109:2025. https://www.iso.org/standard/84700.html.

Open Geospatial Consortium. 2022. *OGC Testbed-17: UML Modeling Best Practice Engineering Report*. OGC 21-031, February 8. https://docs.ogc.org/per/21-031.html.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC API—Connected Systems—Part 2: Dynamic Data*. OGC 23-002, version 1.0, July 16. https://docs.ogc.org/is/23-002/23-002.html.

Open Geospatial Consortium. 2026a. *The ModSpec Model—Part 1: Core—A Standard for Designing and Writing Modular Standards*. OGC 08-131r7, version 1.1, May 21. https://docs.ogc.org/pol/08-131r7/08-131r7.html.

Open Geospatial Consortium. 2026b. *The ModSpec Model—Part 2: UML*. OGC 24-065r1, version 1.1, May 21. https://docs.ogc.org/pol/24-065r1/24-065r1.html.

Pras, Aiko, and Jürgen Schönwälder. 2003. “On the Difference between Information Models and Data Models.” RFC 3444, January. https://www.rfc-editor.org/rfc/rfc3444.html.

*Source-access note:* The ISO 19103/19109/19106 conclusions above rely on the publicly available ISO descriptions, not an inspection of full licensed normative text. OGC ModSpec and CSAPI provisions were checked against publicly available official standards text. This plan makes **no conformance claim** for any of these sources.
