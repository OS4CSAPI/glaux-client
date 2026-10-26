# Domain Information Model (DIM) / Profile Version 2 (V2) — Modeling Convention

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Adopted **working method for documenting and representing the emerging DIM**, not a declaration that a DIM, class schema, or standards-conformant model has been completed.  
**Companion:** [Modeling and Visualization Guide](DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md) (notation mechanics and reproducible figures).  
**Basis:** [DIM Concept and Method Basis](DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md) and [incremental consolidation plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md).

## 1. What form we are adopting—and why

There is **no universal required document template called a “DIM.”** Our working choice is to follow the established **implementation-independent information-modeling tradition** and, when concepts are mature enough to model, express their structural relationships principally through **Object Management Group (OMG) Unified Modeling Language (UML) 2.5.1 class diagrams**, supported by precise textual definitions (Pras and Schönwälder 2003, §§ 2–4; OMG 2017; Open Geospatial Consortium 2022, §§ 1.2–1.3, 8.1–8.4).

Three additional sources inform this choice, with **different authority and scope**:

- **International Organization for Standardization (ISO) 19103:2024** specifies a UML profile and core datatypes **for geographic conceptual schemas**. Its applicability to geographic portions of V2 does **not** make every sensing-equipment concept an ISO 19103 feature or confer automatic conformance (International Organization for Standardization 2024).
- **ISO 19109:2025** defines a general feature model and rules for **geographic feature application schemas**. We can use its practices when V2 models geographic features or derives applicable application schemas; it is **not** a mandatory metamodel for the entire DIM (International Organization for Standardization 2025).
- **Open Geospatial Consortium (OGC) Testbed-17 UML Modeling Best Practice Engineering Report (21-031)** recommends platform-independent class diagrams, consistency with source standards, agreement between figures and text, value-added modeling, and preservation of model artifacts. It is an **informative OGC Engineering Report, not an OGC Standard** (Open Geospatial Consortium 2022, notice and §§ 8.1–8.12).

**Practical precedent:** OGC *Observations, Measurements, and Samples* (OMS) 3.0 expresses its conceptual observation and sample schemas using UML class diagrams paired with source-defined concepts, associations, and requirements. We can follow that *presentation and documentation approach* without copying its ontology/classes or declaring V2 to be an OMS implementation (Open Geospatial Consortium 2023, §§ 8, 11).

## 2. What the DIM will contain

The DIM is to explain **the domain and its meaning**, not serve as an API description. Its minimum documented parts, **when justified by evidence**, are:

| Part | Purpose and appropriate content |
| --- | --- |
| **Scope and standing** | The domain/problem boundary, purpose, intended uses, excluded cases, open decisions, and version. |
| **Concept definitions** | Established source terminology where suitable; concise meanings of individual concepts; identity/type/instance distinctions; source and any V2-specific interpretation. |
| **Relationships and constraints** | Meaningful associations and roles, genuine specialization, composition/context distinctions, and semantic constraints. Include multiplicity or datatypes only when evidence warrants their precision. |
| **Conceptual views** | Small, legible UML class diagrams conveying established concepts and their relationships; multiple focused diagrams if one would be unreadable. |
| **Logical detail, as needed** | Properties, permissible values, datatypes, multiplicities, and constraints sufficient to express the *technology-independent* model where required, rather than prematurely imitating a JSON schema. |
| **Source pedigree and change record** | Chicago Manual of Style, 18th-edition, author-date citations; donor-native meanings and limits; mappings; candidate/adopted status; rationale for material changes. |

This is **our lean documentation convention**, not a six-item obligation copied from an ISO standard. Feature-type cataloguing practices in ISO 19110:2016 support clearly defined feature types where applicable; they do not mean that every DIM concept must be registered as a geographic feature type (International Organization for Standardization 2016).

## 3. Modeling and notation rules

Use **UML class diagrams as the default *structural* view when a diagram adds value**. A concept note or comparison may be better expressed solely in prose or a table. Each diagram must answer a named question, use correct UML notation, identify its research/model standing, and agree with its source definitions (OMG 2017; Open Geospatial Consortium 2022, §§ 8.1–8.11).

- **Classes and names:** Use an already established donor concept or a separately justified V2 concept. A labeled box does not itself authorize a new class or root concept.
- **Relationships:** Define the association's meaning and, when useful, its roles. Generalization means true **is-a** specialization, not mere relatedness. Use UML composition/aggregation diamonds only if **UML semantics** have been justified—the OGC Application Programming Interface (API) – Connected Systems (CSAPI) standard's Composition/Aggregation wording is not sufficient by itself.
- **Attributes, multiplicities, and constraints:** Add them only when their domain meaning is supported. Keep unsettled cardinality **open**; never let sample data, drawing convenience, or an eventual profile requirement masquerade as a DIM invariant.
- **Modules and packages:** Depict a package/module only after evidence establishes a cohesive reusable grouping. Neither the Version 1 information subjects nor the donor groups predefine V2 modules.
- **Source and status:** Keep source-native definitions, our mappings, and V2-authored interpretations distinguishable in prose and trace records. Mark candidate or unresolved structures visibly. Color and diagram layout do not supply semantics.

Use the [existing visualization guide](DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md) for diagram types, arrow meanings, rendering, accessibility, and source-file preservation. **A PlantUML file or a rendered figure is not automatically an interoperable UML metamodel artifact.** When a formal machine-readable model becomes necessary, evaluate suitable UML tooling and interchange (for example, Extensible Markup Language (XML) Metadata Interchange (XMI)) rather than claiming diagram-source files alone satisfy that need (Open Geospatial Consortium 2022, §§ 5.1.2, 8.10–8.12; OMG 2017).

## 4. Boundaries between the DIM and other artifacts

The **conceptual/logical DIM** defines domain meaning independently of the technology used to carry it. The future **application profile** selects and constrains the needed information and conformance obligations. The **OGC API – Connected Systems (CSAPI) binding** describes the concrete representation and service behavior. Implementations supply server/client behavior, schemas, persistence, and validation. This division follows the distinction between implementation-independent information models and specific data models (Pras and Schönwälder 2003, §§ 2–4).

Accordingly, **do not put JavaScript Object Notation (JSON) members, OpenAPI paths, SensorML encoding placement, UML-generated code, database tables, or interface/user-interface layouts into the DIM merely because the eventual CSAPI profile will need them**. Equally, the intended profile may motivate which domain concepts need a meaningful description: *model for the profile, not to the profile*.

## 5. How we apply this now

We remain in **incremental canonical concept consolidation**. Pass 1 established a *cited candidate meaning* for **Individual System Identity**; it did **not** create an adopted formal UML class, module, or schema. Continue Passes 2–5 sequentially under the existing plan. Each pass supplies its candidate meaning and immediate donor-by-donor narrative pedigree before any formal class model is inferred.

**At the five-pass checkpoint**, review which concepts and relationships are genuinely stable. Then produce, if warranted, a **small, readable conceptual class view with corresponding definitions and traceability**. Do not undertake a comprehensive UML package, toolchain migration, ontology translation, or conformance exercise merely to satisfy the appearance of formality.

**Controlling principle:** The model's *semantic definitions and evidence* come first. The diagram faithfully depicts them; it never creates them.

## References (Chicago Manual of Style, 18th ed., author-date)

International Organization for Standardization. 2016. *Geographic Information—Methodology for Feature Cataloguing*. ISO 19110:2016. https://www.iso.org/standard/57303.html.

International Organization for Standardization. 2024. *Geographic Information—Conceptual Schema Language*. ISO 19103:2024. https://www.iso.org/standard/83454.html.

International Organization for Standardization. 2025. *Geographic Information—General Feature Model and Rules for Application Schema*. ISO 19109:2025. https://www.iso.org/standard/84700.html.

Object Management Group. 2017. *Unified Modeling Language (UML)*, version 2.5.1. https://www.omg.org/spec/UML/2.5.1.

Open Geospatial Consortium. 2022. *OGC Testbed-17: UML Modeling Best Practice Engineering Report*. OGC 21-031, February 8. https://docs.ogc.org/per/21-031.html.

Open Geospatial Consortium. 2023. *OGC Abstract Specification Topic 20: Observations, Measurements, and Samples*. OGC 20-082r4, version 3.0; aligned with ISO 19156:2023. https://docs.ogc.org/as/20-082r4/20-082r4.html.

Pras, Aiko, and Jürgen Schönwälder. 2003. “On the Difference between Information Models and Data Models.” RFC 3444, January. https://www.rfc-editor.org/rfc/rfc3444.html.

*Access/authority note: ISO 19103:2024, ISO 19109:2025, and ISO 19110:2016 are cited here at the level of their published ISO descriptions; detailed normative provisions were not independently inspected. This convention does not claim compliance with any of them.*
