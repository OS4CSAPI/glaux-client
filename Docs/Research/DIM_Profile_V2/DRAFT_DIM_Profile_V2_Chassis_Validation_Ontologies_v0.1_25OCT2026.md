# DIM/Profile V2 Chassis Validation — Ontologies and Formal Semantic Models

**Working draft v0.1 — 25 October 2026**  
**Status:** First cross-group validation of the CIDM Phase D candidate; no clean-DIM promotion in this artifact.  
**Candidate under test:** a `System` whose principal operational role is sensing/observing and whose realization is physical `Equipment`, modeled as the complete operational subject.

## 1. Validation question

Does the ontology/formal-semantic evidence support, refine, or contradict the CIDM result that V2 should keep **sensing role** distinct from **physical realization** rather than replace the current `Sensor + Equipment` baseline with a new umbrella class?

The source-type audit identifies nine ontology/formal-semantic artifacts. Several are different versions or representations of the same lineage, so they are reviewed individually but are not counted as independent semantic “votes.”

## 2. Current SOSA/SSN — 2023 Edition, 21 October 2026 Working Draft

**Result: strongly supports and sharpens the candidate.**

The current draft makes the distinction explicit:

- `sosa:Asset` is an abstract deployment resource that generalizes `sosa:System` and `sosa:Platform`.
- `sosa:System` is an Asset that implements a Procedure in an Execution and may be a **device, piece of infrastructure, human/other agent, or software simulation**.
- `sosa:Sensor` is a System that implements an ObservingProcedure and likewise may be physical, human, infrastructure, or software.
- `sosa:Platform` is separately an Asset that hosts Assets, especially Systems/Sensors and other Platforms.
- `sosa:hasSubSystem` relates a System to component Systems.
- The ontology provides a concrete complex-device example in which the whole Inkbird IBS-TH2-PLUS package is a subclass of `sosa:System` while its humidity and temperature sensing subsystems are subclasses of `sosa:Sensor`.

### V2 consequence

This is direct semantic evidence that **Sensor role alone does not establish physical equipment realization**. It therefore supports retaining a separate physical-realization constraint/facet. It also cautions against forcing every sensor package itself to be typed directly as `sosa:Sensor`: the current SSN example permits an overall `System` composed of sensing subsystems. This does not invalidate CSAPI `systemType=Sensor`, whose classification is based on primary activity, but it creates a validation question for the eventual formal ontology mapping: whether V2’s top-level subject should be asserted as `sosa:Sensor`, a sensing-oriented `sosa:System`, or both under profile constraints.

Platform separation is also strongly validated: hosting and deployment do not imply that the Platform is intrinsic composition of the Sensor/System.

## 3. SOSA/SSN — 2023 Edition, 12 October 2026 Working Draft

**Result: same semantic lineage; no independent change to the chassis result.**

This artifact is the immediately preceding working-draft snapshot of the same developing 2023 Edition. It remains in the frozen corpus and is retained as evidence of evolution, but it must not be treated as a separate conceptual vote from the 21 October draft.

Where the 21 October draft is the later source, it controls current semantic interpretation unless the project needs to document a specific editorial change between snapshots.

## 4. SOSA/SSN — 2017 Recommendation

**Result: supports the role/realization separation and shows the lineage predates the 2026 draft.**

The 2017 Recommendation defined `sosa:Sensor` as a device, agent (including humans), or software simulation involved in or implementing a Procedure, with `sosa:Sensor` a subclass of `ssn:System`. `ssn:System` was a unit of abstraction for pieces of infrastructure implementing Procedures and could have subsystems. `sosa:Platform` was an entity hosting Sensors, Actuators, Samplers, or other Platforms.

### V2 consequence

The key point is stable across the lineage: **Sensor is a functional/operational semantic category broad enough to include non-equipment realizations**, while Platform/hosting remains distinct. The 2023 Edition makes the structure cleaner by introducing `Asset` and moving System/Sensor/Actuator/Sampler into a more consistent common pattern.

## 5. SAREF Core 4.1.1

**Result: strongly supports the physical-sensor intersection, but uses a different ontology design pattern from SOSA/SSN.**

SAREF defines:

- `saref:Device` as a **tangible object** designed to accomplish a task by performing functions; Device is also a `s4syst:System`.
- `saref:Sensor` as a **Device** designed to observe and measure properties/states; Sensor is therefore a subclass of Device.
- Actuator, Appliance, Meter, and Sensor are Device subclasses.
- SAREF provides composition through `saref:consistsOf` and system semantics through SAREF4SYST.

### V2 consequence

SAREF demonstrates a legitimate alternative ontology pattern: it **builds physical realization into the Sensor class itself** because every SAREF Sensor is a tangible Device. Conceptually, this is very close to the V2 target family.

However, because the intended CSAPI/SSN environment uses the broader SOSA Sensor semantics, V2 should not silently adopt the narrower SAREF class semantics as though they were identical. Instead, SAREF provides strong external confirmation that the intended V2 family is approximately the intersection of:

- a sensing/observing system role, and
- a tangible/physical device-equipment realization.

That supports the two-axis boundary rather than requiring a new term.

## 6. SWEET ontology suite

**Result: strongly corroborates the same intersection through explicit multiple inheritance.**

SWEET is a large modular Earth-system-science ontology suite. Its dedicated instrument module v3.6.0 provides a particularly useful semantic pattern:

- `Instrument` is a subclass of SWEET `Equipment`.
- SWEET `Device` is equivalent to `Instrument`.
- SWEET `Sensor` is a subclass of **both** SWEET `Instrument` and `sosa:Sensor`.

Thus SWEET literally models its Sensor concept as the conjunction of an **equipment/instrument realization** and the external **SOSA sensing role**.

### V2 consequence

Among the ontology sources, this is the clearest independent corroboration of the CIDM synthesis. It does not require an invented umbrella class: SWEET obtains the intended meaning through existing sourced classifications.

SWEET is nevertheless an Earth-science vocabulary and its Sensor class should not automatically become the V2 normative class. Its value here is structural evidence for the modeling pattern.

## 7. I-ADOPT Framework Ontology 1.1.0 — specification

**Result: cross-cutting; does not challenge the chassis.**

I-ADOPT is organized around semantic descriptions of **Variables**, minimally an ObjectOfInterest plus a Property, with Entity, ContextObject, Matrix, Constraint, and StatisticalModifier concepts. Its `System` class means a combination of two or more Entities for variable-description purposes.

### V2 consequence

I-ADOPT should not be used to define the sensor-equipment chassis. Its principal value is later in describing observable-variable semantics and preserving donor meaning. Its generic “System” must not be confused with SOSA/SSN System.

## 8. I-ADOPT Framework Ontology 1.1.0 — Turtle artifact

**Result: same ontology lineage and semantics as the specification; not an independent vote.**

The machine-readable Turtle is important for implementable semantic mappings and future validation but does not add a separate chassis theory beyond the normative/authoritative ontology specification.

## 9. PROV-O

**Result: cross-cutting; does not challenge the chassis.**

PROV-O is the OWL encoding of the W3C PROV data model and provides generic Entity/Activity/Agent provenance semantics. It can describe provenance for system descriptions, observations, configuration changes, mappings, and other V2 information, but it intentionally does not define Sensor, Device, or Equipment.

### V2 consequence

Retain as a future provenance semantic source, not a chassis source.

## 10. Cross-ontology comparison

| Ontology source | Sensing role | Physical realization | System/host distinction | Effect on candidate |
|---|---|---|---|---|
| SOSA/SSN 2026-10-21 | Sensor = observing System | Sensor may be device, infrastructure, human, software | Platform separately hosts Assets/Systems | **Supports split strongly** |
| SOSA/SSN 2026-10-12 | Same developing lineage | Same lineage | Same lineage | No independent vote |
| SOSA/SSN 2017 | Sensor subclass of System; broad realization | Device/human/software possible | Platform distinct | **Supports split** |
| SAREF 4.1.1 | Sensor observes/measures | Sensor is tangible Device | Device is also System | **Supports intersection; narrows Sensor physically** |
| SWEET 3.6.0 | SWEET Sensor is also SOSA Sensor | Sensor also Instrument; Instrument ⊂ Equipment | Not chassis-defining | **Very strong intersection corroboration** |
| I-ADOPT spec/Turtle | Observable-variable semantics | Not chassis-defining | “System” has local variable-model meaning | Non-applicable to chassis |
| PROV-O | Provenance only | Not chassis-defining | Not chassis-defining | Non-applicable to chassis |

## 11. Ontology-level synthesis

The ontology group does **not** reveal a better single established umbrella term.

Instead, it exposes three legitimate patterns:

1. **Broad role ontology — SOSA/SSN:** Sensor is an observing System and can have many realizations.
2. **Physical-role specialization — SAREF:** Sensor is a tangible Device that performs observation.
3. **Explicit intersection — SWEET:** Sensor is both an Instrument/Equipment concept and a SOSA Sensor.

These are not contradictions that V2 needs to “fix.” They demonstrate why a two-axis boundary is semantically robust across communities.

### Refined candidate statement

The CIDM candidate survives ontology validation with one useful refinement:

> **The V2 domain concerns physically realized equipment Systems whose defining domain role is sensing/observing. The formal domain boundary is the conjunction of sensing-system semantics and equipment/device realization; neither `Sensor`, `Device`, nor `Asset` alone is sufficient across the donor landscape.**

This remains a boundary statement, not a new V2-owned class name.

## 12. New caution exposed by the ontology group

The ontology review reveals one issue that must be carried into architecture validation:

The current SOSA/SSN complex-device example represents a multi-sensor package as an overall `sosa:System` containing `sosa:Sensor` subsystems rather than necessarily asserting the package itself as `sosa:Sensor`. CSAPI, by contrast, permits a System with primary activity sensing to carry `systemType=Sensor`.

Therefore the project must preserve a distinction between:

- **CSAPI classification:** what primarily characterizes the represented System;
- **OWL class assertion:** what ontology class the System is formally asserted to instantiate.

The eventual profile/binding should not equate a CSAPI classification token with an OWL class assertion unless the adopted semantic mapping explicitly establishes that equivalence.

## 13. Validation standing

| Question | Ontology result |
|---|---|
| Is a new chassis term required? | **No** |
| Does Sensor alone enforce physical equipment? | **No in SOSA/SSN; yes in SAREF; therefore not cross-community invariant** |
| Is Device/Equipment alone sufficient? | **No; it does not establish sensing role** |
| Is the sensing-role + equipment-realization conjunction externally supported? | **Yes, strongly; SWEET models nearly this exact conjunction** |
| Is Platform/host distinct from the sensing System? | **Yes, strongly supported by SOSA/SSN** |
| Does candidate survive ontology validation? | **Yes, with formal-mapping caution** |
| Clean V2 DIM promotion | **Still blocked pending architecture and requirements validation** |

## 14. Next step

Proceed to the Reference Architecture / Architectural Framework group and attempt to falsify the candidate against architectural boundaries, physical/functional decomposition, hosting, distributed systems, and system/subsystem organization.
