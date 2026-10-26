# DIM/Profile V2 — Phase A Validation/Audit

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Calibration audit; C08 only  
**Controlling recovery state:** PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md

## 1. Purpose

This artifact begins the corrective validation gate between Phase A extraction and any future cross-source synthesis.

The objective is deliberately narrow:

> **Determine whether the existing Phase A extraction represents each donor accurately enough to be used later, without re-running the donor research or redesigning the DIM.**

The audit is human-facing. It does not sentence-tag the entire Phase A record. It checks only material structural claims and records corrections that could change later interpretation.

Audit labels:

- **SOURCE-DIRECT** — materially supported by the donor source.
- **INTERPRETATION** — defensible project reading, but not stated by the source in those terms.
- **ABSTRACTION** — project-created language used to organize or compare donor evidence.
- **NEEDS CHECK** — insufficiently established.
- **WRONG / OVERREACH** — source does not support the claim as written.

## 2. Calibration lineage — C08 OGC API – Connected Systems Parts 1–2

### Human verdict

**C08 is substantially recoverable and mostly source-faithful.**

The extraction correctly captured most of the important CSAPI structural distinctions:

- System instance versus reusable descriptions;
- independent `systemType` and `assetType` facets;
- `Sensor + Equipment` as a native CSAPI combination rather than a newly invented class;
- persistent UID versus API resource URL/local identity;
- Composition versus Aggregation;
- enduring subsystem topology versus Deployment-scoped association;
- Part 1 feature/static-description resources versus Part 2 dynamic resources;
- DataStream versus Observation;
- ControlStream versus Command;
- Command versus CommandStatus versus CommandResult;
- Feasibility versus actual command execution;
- SystemEvent history versus current System description.

The audit found **three material corrections/qualifications** and one general epistemic-labeling issue.

---

## 3. Material finding 1 — Procedure and systemKind were blurred

**Phase A treatment:** repeatedly groups “Procedure/systemKind” as a single reusable-kind/procedure concept.

**Audit result:** **CORRECTION REQUIRED.**

CSAPI uses the same `Procedure` resource type in more than one semantic role, but the relationships are distinct:

1. `systemKind` links a System to **one Procedure describing the kind of System**, such as a model/datasheet.
2. `procedures` links a System to **Procedures that the System can implement**, such as observing, sampling, actuating, or other methods.

The standard explicitly says Procedure resources can describe either system types/datasheets or procedures/methodologies. That does **not** make product/model/kind identity and implemented Procedure/Method the same relationship.

**Correction for later use:** preserve:

> **System instance ≠ System kind/model/datasheet ≠ Procedure/Method implemented by the System**

even though CSAPI represents both latter descriptions using the Procedure resource type.

**Why this matters:** later DIM work must not infer semantic equivalence merely because CSAPI reuses one API resource class as the carrier for both roles.

Primary evidence:
- OGC 23-001 §9.1–9.2, especially System associations `systemKind` and `procedures`.
- OGC 23-001 §13.1–13.2, Procedure purpose, examples, and Procedure types.

---

## 4. Material finding 2 — Feature of Interest was presented too much like a CSAPI resource type

**Phase A treatment:** lists “Sampling Feature / Feature of Interest” alongside the primary Part 1 resources.

**Audit result:** **QUALIFICATION REQUIRED.**

Part 1 defines **Sampling Feature** as a CSAPI resource type. It does **not** define Feature of Interest as another equivalent CSAPI resource type in the same sense. The ultimate feature of interest may be a Feature available through the CSAPI environment or an external feature resource.

The source-native distinction itself is real and important:

> Sampling Feature / sampling context ≠ ultimate Feature of Interest.

But the Phase A wording makes the two look more symmetrical in the CSAPI resource model than they are.

**Correction for later use:** refer to:

> **Sampling Feature resource and linked ultimate Feature(s) of Interest**

rather than treating both as peer CSAPI-defined resource types.

Primary evidence:
- OGC 23-001 §7.3 resource-type overview.
- OGC 23-001 §14 Sampling Features, especially `sampledFeature`.

---

## 5. Material finding 3 — Deployment-specific configuration needs carrier qualification

**Phase A treatment:** treats deployment-specific configuration as part of the general Deployment/context picture.

**Audit result:** **QUALIFICATION REQUIRED.**

The base CSAPI Deployment resource model explicitly carries deployment identity, type, valid time, location, Platform, deployed Systems, subdeployments, features of interest, sampling features, DataStreams, and ControlStreams.

A **SensorML representation** of a CSAPI Deployment can additionally express configuration for a deployed System. That is useful evidence, but it must not be flattened into the claim that “configuration” is simply a base CSAPI Deployment property/association.

**Correction for later use:** distinguish:

- source-native CSAPI Deployment semantics; from
- additional detail available through the SensorML encoding/model used to represent a Deployment.

**Why this matters:** this is a concrete example of the project's standing rule that useful domain distinctions may be exposed through an implementation/binding standard, but the carrier must not be mistaken for the concept itself.

Primary evidence:
- OGC 23-001 §11.2 Deployment properties and associations.
- OGC 23-001 SensorML Deployment representation example in §19.2.

---

## 6. General issue — several Phase A headings are our analysis, not CSAPI's own partitions

The following C08 structures are useful **INTERPRETATION / ABSTRACTION**, not source-native CSAPI taxonomies:

- “intrinsic vs contextual standing”;
- “cross-cutting concepts”;
- “capability / function / behavior organization” as one analytical topic;
- “management / condition organization”;
- “semantic invariants” as a compiled list;
- “potential V2 structural contribution.”

Nothing is inherently wrong with these sections. They are precisely the kind of interpretation needed for later DIM research.

The correction is epistemic:

> **Do not cite those analytical headings as though CSAPI itself defines an intrinsic/contextual/cross-cutting/capability architecture.**

Individual facts inside them may be source-direct; the grouping and labels are ours.

---

## 7. What survived the audit

The following C08 conclusions are safe enough to retain as source-grounded inputs, subject to normal later synthesis discipline:

1. CSAPI System resources describe instances and carry a persistent `uniqueIdentifier` distinct from the resource URL.
2. `systemType` and `assetType` are separate facets.
3. CSAPI explicitly uses combinations including Sensor + Equipment, Sensor + Simulation, Sensor + Human, and Platform + Equipment.
4. Subsystems are regular System resources.
5. Composition and Aggregation have explicitly different meanings and API realization.
6. Deployment is a time/purpose/context structure involving Systems and optionally a Platform.
7. DataStream/Observation and ControlStream/Command are distinct channel-versus-instance structures.
8. Command, CommandStatus, CommandResult, and Feasibility are explicitly distinguished.
9. SystemEvent provides explicit event/history structure, including maintenance/configuration/deployment-related events.
10. Part 1 resource semantics are separated from concrete encoding choices, and Part 2 deliberately separates dynamic resources from Part 1 feature resources.

---

## 8. Calibration conclusion

**C08 does not indicate that Phase A is wholesale hallucination.**

Instead, it shows a more specific failure mode:

> **source facts were often extracted correctly, but analytical interpretation and source-native semantics were not consistently labeled as different epistemic layers.**

For C08, the extraction can be repaired without redoing the research.

The most consequential substantive correction is the distinction between:

- `systemKind` as kind/model/datasheet description; and
- separately implemented Procedures/Methods.

The other corrections primarily prevent binding/resource-carrier structure or project-created analytical categories from being promoted into donor-native domain truth.

### Decision for the validation method

The lightweight audit method is viable.

For subsequent calibration donors, continue to ask only:

1. What did Phase A think the donor told us?
2. What materially survives source checking?
3. What was interpretation, abstraction, or overreach?
4. Does the correction change what we thought we learned?

Do not sentence-tag the entire extraction and do not reopen full donor research unless a material uncertainty requires it.

## References

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0. https://docs.ogc.org/is/23-001/23-001.html

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 2: Dynamic Data*. OGC 23-002, version 1.0. https://docs.ogc.org/is/23-002/23-002.html
