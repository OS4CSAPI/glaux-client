# DIM/Profile V2 Chassis — Cross-Group Validation and Working Decision

**Decision record v0.1 — 25 October 2026**  
**Status:** Chassis study complete; working decision promoted and subsequently corpus-wide reconciled across all 182 frozen donor artifacts.  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v0.4_25OCT2026`.

## 1. Decision purpose

This record closes the narrow chassis question defined by the active PITON:

> Across the candidate sources, what bounded conceptual frame best identifies the class of real-world thing the V2 DIM is about, and is there an existing recognized concept that should replace the current System / Sensor / Equipment baseline?

The study did **not** attempt to derive the complete DIM structure, determine future modules, select all donor concepts, define the CSAPI binding, or establish donor-standard conformance. Those remain later work.

The research sequence followed the required gates:

1. independent extraction of all fourteen Conceptual / Information / Domain Model artifacts;
2. neutral cross-source comparison;
3. source standing within that group;
4. candidate chassis synthesis;
5. ontology/formal-semantic validation;
6. reference-architecture validation; and
7. requirements/capability/operational validation.

No clean-DIM edit was made before all gates completed.

---

# 2. Working decision

## 2.1 Chassis boundary

The V2 DIM is bounded around:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

This is a **domain-boundary statement**, not a newly authored class.

The boundary is intentionally expressed through established sourced concepts rather than by inventing a compound umbrella class.

## 2.2 Current CSAPI characterization

For the intended CSAPI application-profile environment, the most direct present classification remains:

- `systemType = Sensor`
- `assetType = Equipment`

This combination is no longer merely the pre-study comparison baseline. It is now the **working V2 boundary characterization**, having survived independent challenge by the Conceptual / Information / Domain Model, Ontology / Formal Semantic Model, Reference Architecture / Architectural Framework, and Requirements / Capability / Operational Specification groups.

The characterization remains subject to later binding details and conformance rules.

## 2.3 No new umbrella class is justified

The study does not justify a V2-owned class such as “Managed Physical Sensing System,” “Sensor Equipment System,” or another compound term merely to collapse the two dimensions.

No reviewed source provides a single term that more faithfully and consistently captures both:

1. the system’s defining **sensing/observing role**, and
2. its **physical equipment realization**.

The correct result is therefore a bounded conjunction of sourced concepts, not a newly named root.

---

# 3. Why the decision is two-dimensional

The strongest cross-source finding is that mature donor communities repeatedly distinguish **what the thing does** from **what kind of thing realizes that role**.

## 3.1 Role/function evidence

- The Open Group SOSA DSDM and Technical Standard treat the whole **Sensor** as an operational subject that may contain heterogeneous components.
- SOSA/SSN defines **Sensor** through observing behavior while allowing physical, human, infrastructure, and software realizations.
- OMS defines observation/sampling semantics without equating the observation process with the physical equipment.
- SNRA separates functional and physical views of sensor-network entities.

## 3.2 Physical-realization evidence

- OPC UA Part 100 supplies a generic **Device** frame distinct from software.
- PA-DIM specializes Device into a physical process-automation equipment family.
- MIMOSA CCOM supplies a physical-asset lifecycle frame.
- OSUS-R defines its whole Asset as a physical device that can contain multiple sensors.
- RFC 7326 distinguishes physical Device, Component, and Power Interface.
- NIST IoT guidance treats the device as hardware/software containing a sensor or actuator transducer rather than as the transducer itself.
- Radiation-detection operational sources describe complete fixed, mobile, portable, and multi-element equipment systems.

## 3.3 Explicit intersection evidence

SWEET provides the clearest ontology-level corroboration of the pattern: its Sensor is both a SOSA Sensor and an Instrument, with Instrument under Equipment. SAREF independently uses the alternative but compatible pattern of making Sensor a tangible Device.

The donor landscape therefore supports the V2 boundary as a **sensing-role + equipment-realization intersection** even though individual ontologies encode the intersection differently.

---

# 4. Why the principal alternatives were not adopted

## 4.1 Asset

**Not adopted as the chassis.**

“Asset” is semantically unstable across the donors:

- AAS Asset may be physical, digital, or intangible.
- MIMOSA CCOM uses Asset in a physical lifecycle-management context.
- OSUS-R uses Asset for a physical device.
- SOSA/SSN Asset is a broad superconcept above System and Platform.

Asset remains useful as a sourced superconcept or donor-mapping concept, but it is too broad and inconsistent to define V2 membership by itself.

## 4.2 Device

**Not adopted as the universal root.**

Device is the most stable recurring physical-equipment concept, but it is functionally neutral and can be too narrow for composite installed systems.

The architecture and operational evidence shows that one V2 sensing System may consist of multiple hardware elements, including elements physically distributed across a host platform. Fixed radiation portal monitors may likewise comprise multiple pillars, detectors, occupancy sensing, recording, analysis, and other supporting elements.

Device remains an important mapping concept; **Equipment** is the better V2 realization facet because it does not force a one-box or one-device form factor.

## 4.3 Thing

**Not adopted.**

W3C WoT intentionally defines Thing as an abstraction of a physical or virtual entity and leaves domain-specific semantics to external vocabularies. It is useful as an interaction/description architecture but too broad to define the V2 sensing-equipment family.

## 4.4 Sensor Network

**Not adopted as the ordinary V2 subject.**

SNRA establishes Sensor Network as a legitimate larger architectural subject. That strengthens rather than weakens the distinction between an individual sensing System and an aggregate/network.

A network of cooperating systems is not automatically one V2 System.

## 4.5 Observation / Observer

**Not adopted as the chassis.**

OMS and related sources are foundational for what sensing/observing means, but observation semantics describe an act/process and its participants/results rather than the complete enduring equipment subject.

---

# 5. Earned boundary rules

The cross-group evidence supports the following chassis-level rules.

## 5.1 Complete operational subject

The top-level subject is the enduring sensing System/equipment itself, not merely:

- an Observation;
- a detector/transducer;
- an API endpoint;
- a network interface;
- a deployment record;
- a software service; or
- a digital representation.

Information needed to understand the System may include identity, composition, capabilities, state, configuration, commands, communications, power, health, management, history, provenance, observations, and products without changing the subject into a system-of-systems.

## 5.2 Composite physical realization

One sensing System does **not** have to be one hardware box or one Device.

The Open Group SOSA Edition 1.1 explicitly allows one Sensor to contain multiple hardware elements and allows those elements to be grouped or distributed at different locations on/in one host platform.

The realization constraint is therefore **Equipment**, potentially composite equipment.

## 5.3 Heterogeneous internal components

Internal constituents may include:

- sensing elements;
- actuators/effectors;
- processors;
- software and firmware;
- storage;
- communications;
- power;
- apertures;
- chassis;
- run-time environments;
- management functions; and
- diagnostic/BIT functions.

The whole can remain a sensing System when sensing/observing is its defining operational role.

## 5.4 Sensing need not be exclusive

A System may also execute commands, actuate/effect, process, communicate, identify/classify, manage itself, report status, or support other functions.

Membership does not require every component or capability to be observational.

The test is the **defining operational role of the whole System**, not functional purity.

## 5.5 Host Platform is separate unless composition evidence says otherwise

A vehicle, structure, building, pod, mast, or other host is not automatically part of the Sensor merely because it carries, powers, connects to, or deploys it.

SOSA architecture supplies direct precedent for a Sensor boundary with a separate Host Platform and explicit Host Platform Interface.

## 5.6 Network/aggregation is separate from one System

A sensor network, operational grouping, deployment aggregation, or set of cooperating Systems does not automatically become one sensing System.

The project should require evidence of one enduring System identity/composition boundary before collapsing multiple independent Systems into one.

## 5.7 Mobility/form factor does not define membership

Operational evidence includes handheld, portable, mobile, mounted, fixed, and installed sensing equipment.

The chassis is therefore not tied to mobility, size, enclosure, or one physical-device form factor.

## 5.8 Virtual/interface identity does not prove physical realization

ISA supports virtual components with configuration, status, observations, and commands.

A network-visible component, service, digital twin, or virtual entity therefore cannot satisfy the V2 Equipment boundary merely by exposing sensor-like capabilities. Physical realization must remain explicit.

---

# 6. Formal semantic caution

The working domain boundary must not be confused with an OWL class assertion.

In current SOSA/SSN:

- `sosa:System` is broad;
- `sosa:Sensor` is a System that implements an ObservingProcedure; and
- a complex physical package can be modeled as an overall System containing Sensor subsystems.

In CSAPI, by contrast, `systemType = Sensor` classifies the represented System by its principal activity.

Therefore:

> **CSAPI `systemType = Sensor` must not automatically be treated as semantically identical to asserting RDF type `sosa:Sensor`.**

The eventual ontology alignment/binding must state the mapping explicitly. This caution does not reopen the chassis boundary; it protects the distinction between domain classification and a particular ontology encoding.

---

# 7. Source standing that produced the decision

## 7.1 Strongest chassis evidence

- **The Open Group SOSA DSDM / Technical Standard** — strongest evidence for Sensor as the complete operational subject with components, state, configuration, management, and distinct Host Platform.
- **OPC UA Part 100: Devices** — strongest generic physical Device/equipment frame.
- **MIMOSA CCOM** — strongest whole physical-asset lifecycle frame.
- **OSUS-R Asset model** — strongest motivating-domain whole physical-device corroboration.

## 7.2 Strongest cross-group validators

- **SOSA/SSN** — establishes Sensor as a role-bearing System whose realization is not necessarily physical.
- **SAREF** — provides physical Sensor-as-Device pattern.
- **SWEET** — explicitly combines SOSA Sensor semantics with Instrument/Equipment semantics.
- **SOSA Reference Architecture Edition 1.1** — validates composite/distributed hardware, whole-Sensor boundary, and Host Platform separation.
- **ISA requirements** — validates that observable/command capability and interface component identity are distinct from physical realization.
- **IAEA 44-T / ISO 22188** — validate fixed, portable, mobile, and multi-element sensing equipment in real operations.

## 7.3 Cross-cutting/non-chassis sources

OMS, PROV, NIEM, NCDF, OSA-CBM, JC3IEDM, and related specialized sources remain useful to later DIM subjects but did not supply or overturn the chassis.

---

# 8. What this decision does not settle

This decision deliberately leaves later modeling questions open.

It does **not** yet determine:

- the final DIM module/subdomain structure;
- which donor owns each detailed concept;
- the complete composition ontology;
- the exact threshold for “primary/defining sensing role” in every edge case;
- the formal SOSA/SSN OWL mapping of a CSAPI Sensor-classified System;
- the detailed treatment of large distributed sensing installations spanning multiple host platforms;
- which lifecycle/management information becomes mandatory versus optional;
- the application-profile requirements;
- the OGC binding rules;
- JSON/Schema/SHACL or other machine-readable constraints;
- conformance classes or tests; or
- an editorial/publication title beyond the descriptive “Sensor Systems” wording.

Those questions proceed under the earned chassis boundary rather than reopening it by default.

---

# 9. Promotion decision

The chassis candidate has survived all validation gates required by the active PITON.

**Disposition: PROMOTE AS WORKING V2 DECISION.**

The maintained clean V2 artifact has been updated to:

1. replace the “Sensor + Equipment” candidate standing with the earned boundary decision;
2. record that no additional umbrella class is required;
3. state the composite-equipment and host-platform boundary rules;
4. preserve the CSAPI-classification versus OWL-assertion caution;
5. update the decision table and development sequence; and
6. leave detailed DIM architecture/modules and binding obligations open for subsequent donor synthesis.

The clean artifact deliberately does not absorb the full research narrative above. That evidence remains in the dedicated chassis-study and validation records.

---

# 10. Chassis-study artifact chain

1. `DRAFT_DIM_Profile_V2_Chassis_Study_Phase_A_v0.1_25OCT2026.md` — independent extraction of all fourteen CIDM artifacts.
2. `DRAFT_DIM_Profile_V2_Chassis_Study_Phases_B-D_v0.1_25OCT2026.md` — cross-source comparison, source standing, initial candidate.
3. `DRAFT_DIM_Profile_V2_Chassis_Validation_Ontologies_v0.1_25OCT2026.md` — ontology/formal-semantic validation.
4. `DRAFT_DIM_Profile_V2_Chassis_Validation_Architectures_v0.1_25OCT2026.md` — architecture validation.
5. `DRAFT_DIM_Profile_V2_Chassis_Validation_Requirements_v0.1_25OCT2026.md` — requirements/operational validation.
6. **This record** — cross-group working decision and promotion gate.

# 11. Corpus-wide reconciliation addendum

A later methodological review identified that the original discovery population had treated primary source type too strongly as an eligibility gate. SAPIENT demonstrated that an artifact primarily standardized as an interface specification can nevertheless contain a substantive domain abstraction capable of challenging the chassis.

A bounded audit was therefore performed across the complete frozen 182-source corpus. Every source received exactly one chassis-capability disposition. The accounting is:

- 38 already explicitly chassis-tested;
- 13 previously under-contested artifacts explicitly challenged in the reconciliation;
- 101 lineage/companion/specialized artifacts retained without independent evidentiary weight;
- 24 artifacts with no credible chassis potential; and
- 6 reference-system/operational falsifiers.

The thirteen under-contested artifacts represent approximately ten semantic lineages: SensorML 3.0, SAPIENT, ISA DMS/SDD, Redfish, MIMOSA OSA-EAI, Matter, current IEEE 1451.0, LwM2M, RFC 8348, and the radiation-instrument exchange family.

None supplied a superior universal boundary. The working chassis is therefore **reaffirmed after corpus-wide reconciliation**, not merely after the original source-type-group validation.

The audit adds four material cautions:

1. source type must never again be used as an eligibility gate for a domain-boundary challenge;
2. `Equipment` must remain broader than any single donor abstraction such as Device, Node, Chassis, or SensorML PhysicalSystem;
3. network-visible/registered/component identities may be virtual, mediated, aggregated, or role-based and cannot automatically be treated as the physical System; and
4. SensorML `PhysicalComponent` versus `PhysicalSystem` is a later concrete binding/model-selection question rather than the V2 chassis itself.

The full reconciliation record is:

- `DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv`
- `DIM_Profile_V2_Chassis_Corpus_Wide_Reconciliation_v0.1_25OCT2026.md`

This addendum supersedes any implication elsewhere in this record that the original fourteen-source discovery population plus three validation groups alone constituted exhaustive corpus-wide chassis coverage.

