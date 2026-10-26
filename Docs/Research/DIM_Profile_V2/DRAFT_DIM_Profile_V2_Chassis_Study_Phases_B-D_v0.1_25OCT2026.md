# DIM/Profile V2 Chassis Study — Phases B–D: Comparison, Source Standing, and Synthesis Gate

**Working draft v0.1 — 25 October 2026**  
**Status:** Research synthesis after completion of Phase A. Candidate chassis only; not yet promoted into the clean V2 DIM/Profile artifact.  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v0.4_25OCT2026` §§13–17.  
**Phase A evidence record:** `DRAFT_DIM_Profile_V2_Chassis_Study_Phase_A_v0.1_25OCT2026.md`

## 1. Purpose and guardrails

This document executes the next permitted stages of the chassis study after all fourteen Conceptual / Information / Domain Model artifacts received independent extraction.

- **Phase B** compares the sources across common dimensions.
- **Phase C** assigns relative source standing within this source-type group.
- **Phase D** proposes a candidate V2 chassis/boundary for validation.

The result is still a research candidate. It does **not** edit the clean V2 DIM, invent a new umbrella class, or claim implementation/conformance to any donor standard. The candidate must next be tested against the Ontology / Formal Semantic Model, Reference Architecture / Architectural Framework, and Requirements / Capability / Operational Specification groups before promotion.

---

# Phase B — Cross-source comparison

## 2. Neutral comparison matrix

| Source | Organizing subject | Does sensing define membership? | Does physical equipment define membership? | Whole-subject coverage | Relationship to current `Sensor + Equipment` baseline |
|---|---|---:|---:|---|---|
| AAS Part 1 | Asset as represented by an AAS | No | No — Asset can be physical, digital, or intangible | Broad whole-asset digital representation | Broader on Asset; orthogonal on Sensor |
| IEEE 1451.1-1999 | NCAP object model | Yes, with actuation | Physical context, but not generic equipment root | Specialized processor/transducer slice | Narrower / partial |
| ISO/IEC 29182-4 SNRA | Sensor network physical + functional entities | Yes | Yes for physical-entity view | Whole sensor-network aggregate | Broader aggregate; direct physical/sensing relevance |
| ISO/IEC/IEEE 21451-1 | NCAP object model | Yes, with actuation | Physical context, but not generic equipment root | Specialized processor/transducer slice | Narrower / partial; same conceptual lineage as 1451.1 |
| NIEM 6.0 | Multi-domain exchange model | No | No | Cross-domain information building blocks | Orthogonal / much broader |
| MIMOSA CCOM | Asset and asset lifecycle | No | Strong physical-asset orientation | Broad whole-asset lifecycle | Broader role; strong Equipment/whole-subject match |
| JC3IEDM 3.1.4 | C2 operational object/action information | No | Equipment is one branch under Materiel | Very broad operational world model | Broader / orthogonal |
| OGC OMS 3.0 | Observation and sampling acts | Yes | No | Process/observation slice | Partial; explains sensing semantics, not equipment chassis |
| OPC PA-DIM | Process Automation Device | Measurement + actuation | Yes | Strong whole-device information model | Narrower domain; broader functional role |
| OPC UA Part 100 Devices | Device | No | Yes | Strong whole-device frame | Strong Equipment match; Sensor role absent |
| OSUS-R | Asset = physical device producing data/responding to command | Strong but not exclusive | Yes, explicitly | Strong whole-device operational interface | Direct / partial; one Asset may contain multiple sensors |
| RFC 7326 | Energy Object / Device / Component | No | Yes | Specialized energy-management slice | Partial; strong Equipment semantics |
| SOSA DSDM | SOSA Sensor with Components and Platform | Yes | Sensor realization may include physical/software Components; Platform physical | Strong whole-Sensor operational model | Direct on Sensor; Equipment facet implicit rather than explicit |
| PROV-DM | Provenance | No | No | Cross-cutting provenance | Orthogonal |

## 3. Recurring conceptual patterns

### 3.1 The sources separate **role/function** from **physical realization**

The strongest recurring pattern is not a shared umbrella noun. It is the repeated separation of:

1. **what the subject principally does**, and
2. **what kind of thing realizes that role**.

Examples from the Phase A evidence:

- SOSA DSDM makes **Sensor** the operational subject but distinguishes it from its physical/software **Components** and from a physical **Platform**.
- ISO/IEC 29182-4 deliberately separates **functional entities** from **physical entities**.
- OPC UA Part 100 separates generic **Component** from concrete **Device** and **Software** specializations; PA-DIM then specializes Device for a particular operational domain.
- OSUS-R makes the whole **Asset** a physical device while allowing one Asset to have multiple internal sensors.
- AAS separates a very broad **Asset** from the digital representation and its aspect models.
- The current CSAPI baseline independently expresses the same separation as `systemType = Sensor` and `assetType = Equipment`.

**Comparison result:** the two-axis CSAPI characterization is not an isolated API convenience. The donor landscape repeatedly distinguishes operational/functional role from realization.

### 3.2 “Asset” is useful but semantically unstable across communities

“Asset” recurs, but it does not carry one stable boundary:

- AAS Asset may be physical, digital, or intangible.
- MIMOSA CCOM uses Asset in a physical-asset lifecycle-management setting.
- OSUS-R defines Asset much more narrowly as a **physical device** that typically produces data or responds to a command.
- SOSA/SSN, outside this 14-source group but in the current baseline, uses Asset as a broad superconcept for System and Platform.

**Comparison result:** Asset is an important superconcept/context concept, but using **Asset** alone as the V2 chassis would import incompatible donor expectations and would not preserve the required sensing/equipment boundary.

### 3.3 “Device” is the most stable recurring physical-equipment concept

Across OPC UA Devices, PA-DIM, RFC 7326, ISO/IEC 29182-4, and the plain-language definition embedded in OSUS-R Asset, **device** consistently points toward a bounded physical equipment subject.

- OPC DeviceType is the generic physical-device frame used by companion specifications.
- PA-DIM specializes that frame into a Process Automation Device.
- RFC 7326 explicitly defines Device as a physical piece of equipment that may contain Components.
- SNRA uses devices/nodes/gateways/sensors as physical entities.
- OSUS-R’s Asset is literally defined as a physical device.

**Comparison result:** Device strongly corroborates the **Equipment** side of the current CSAPI baseline. It does not, however, answer the sensing-role question and may be narrower than “equipment” for large or distributed installations.

### 3.4 “Sensor” can legitimately denote the whole operational subject, not merely a detector

The most consequential counterexample to the “sensor means one transducer” intuition is the SOSA DSDM:

- Sensor is the named top-level operational entity.
- Sensor carries health, operational state, and configuration state.
- SensorComponent explicitly relates Components as parts of the Sensor.
- Components may themselves be physical or software.
- HostPlatform relates the Sensor to a distinct physical Platform.

OSUS-R independently supports the same whole-versus-internal distinction from the opposite direction: one whole physical Asset may have **multiple sensors**.

The current SensorML baseline likewise treats a physical sensor system as a whole whose internal subprocesses can include sensing, actuation, and computation.

**Comparison result:** a V2 top-level subject may remain a **Sensor/System characterized by sensing** even when it contains multiple detectors, processors, radios, actuators, software components, or other subsystems. Internal heterogeneity does not force the chassis upward into a generic Asset class.

### 3.5 The whole equipment boundary and the observation boundary are different

OMS is very strong for the semantics of observation and sampling, while the device/asset models are strong for the whole physical subject. Neither should be forced to do the other’s job.

- OMS defines Observation, procedure, observed property, result, feature/sample, and participants.
- OPC Devices, CCOM, OSUS-R, PA-DIM, and AAS describe the enduring thing and its properties/parts/lifecycle.
- IEEE 1451/21451 models the processor/transducer interaction architecture.
- PROV models provenance of information about any of these.

**Comparison result:** observation semantics belong **inside or alongside** the whole-system model but do not define the chassis of the equipment itself.

### 3.6 Internal composition and external hosting/context are repeatedly distinct

Several donors draw a useful boundary between what is part of the subject and what merely hosts, locates, or contextualizes it:

- SOSA DSDM: SensorComponent vs HostPlatform.
- OPC: HasComponent vs ConnectionPoints/network context.
- CCOM: AssetComponent vs Site/Segment/Organization context.
- RFC 7326: Device/Component vs deployment/site/organizational context.
- AAS: co-managed parts vs self-managed entities with their own AAS.
- CSAPI baseline: enduring Composition vs deployment-scoped Aggregation.

**Comparison result:** the chassis should not absorb every thing physically attached to or operationally associated with the sensor equipment. Integral composition and deployment/hosting context remain distinct semantic relationships.

---

## 4. Equivalent, overloaded, and conflicting terminology

| Term | Cross-source finding | V2 consequence |
|---|---|---|
| **Sensor** | Can mean a top-level operational sensor (SOSA DSDM), an internal sensing element (OSUS-R), or an observation-role System (SOSA/SSN baseline). | Use sourced semantics explicitly; do not assume “Sensor” always means a single detector. |
| **Asset** | Ranges from any valuable physical/digital/intangible entity (AAS) to physical lifecycle-managed asset (CCOM) to physical device (OSUS-R). | Do not use Asset alone as the family-defining chassis term. |
| **Device** | Comparatively stable as a bounded piece of physical equipment across OPC/RFC/SNRA usage. | Strong corroboration for CSAPI `Equipment`; useful mapping concept, but functionally neutral. |
| **Equipment** | Explicit physical-realization term in CSAPI; JC3IEDM treats Equipment as a Materiel type; RFC equates Device with physical equipment. | Retain as the realization facet unless later groups expose a gap. |
| **Component** | Commonly means a constituent of a larger device/system, though AAS and SOSA permit physical/software forms. | Useful internal boundary primitive; do not assume all Components are hardware. |
| **Platform** | In SOSA DSDM, a physical entity on which Sensor is mounted; in SOSA/SSN baseline, an Asset that hosts other Assets. | Keep host/platform concept separate from the Sensor unless the target itself is principally a Platform. |
| **System** | Broad functional/behavioral abstraction in SOSA/SSN and SensorML; not a dominant root in most equipment CIDMs. | Remains useful formal superconcept; needs role + realization facets to bound V2. |

---

## 5. Explicit lineage and non-independence

The comparison must not count documents as independent conceptual votes when one directly adopts another.

- **IEEE 1451.1-1999 → ISO/IEC/IEEE 21451-1:2010:** IEEE identifies the 2010 standard as an adoption of IEEE 1451.1-1999. These are two corpus artifacts but one primary conceptual lineage for chassis purposes.
- **OPC UA Part 100 Devices → PA-DIM:** PA-DIM is explicitly a specialization of the OPC Devices model. PA-DIM provides domain-specific evidence, not an independent generic device root.
- **AAS Part 1:** sits inside a larger aligned AAS specification family; this review isolates the Part 1 metamodel.
- **OMS:** has joint OGC/ISO lineage and explicit harmonization with SSN/SOSA.
- **SOSA DSDM:** is native to the SOSA Reference Architecture; its “SOSA Sensor” must not be conflated with W3C/OGC SOSA merely because both use the acronym SOSA.

---

## 6. Complete conceptual frames versus specialized slices

### More complete frames for the bounded thing

These sources describe a persistent whole subject with identity/structure/state/context rather than only one interaction:

- SOSA DSDM — whole Sensor with components, state, configuration, health, hosting.
- OPC UA Part 100 Devices — generic Device with identity, health, components, interfaces, functional groups.
- MIMOSA CCOM — Asset with type/model, composition, lifecycle, events, measurements, health, work/history.
- OSUS-R — physical Asset with activation, capabilities, observations, commands, status, BIT, communications.
- PA-DIM — Process Automation Device with identification, diagnostics, process values, configuration, condition, lifecycle.
- AAS — broad whole Asset digital representation, though too unconstrained to establish sensing/equipment membership.

### Specialized slices

- IEEE 1451.1 / ISO 21451-1 — NCAP/transducer interaction architecture.
- OMS — observation/sampling semantics.
- RFC 7326 — energy-management view of devices/components.
- PROV-DM — provenance.
- NIEM — reusable exchange semantics.
- JC3IEDM — broad C2 operational context.
- SNRA Part 4 — sensor-network aggregate/entity view rather than one equipment subject.

---

## 7. Gaps not resolved by the fourteen sources alone

The Phase B evidence exposes several questions that require the next source-type groups rather than local invention:

1. **Primary-role threshold:** when a multifunction device senses and actuates/effects, what makes sensing sufficiently primary for V2 membership?
2. **Distributed equipment boundary:** when a sensing capability spans multiple physically separated devices, when is it one Sensor/System versus an aggregate/network?
3. **Platform inclusion:** when is a vehicle/structure merely the host Platform, and when is it part of the sensing System itself?
4. **Integral vs field-reconfigurable attachment:** the current CSAPI Composition/Aggregation distinction is strong, but the 14-source group does not independently settle every case.
5. **Equipment breadth:** whether CSAPI Equipment is broad enough for fixed infrastructure/large installations without needing Device as a competing formal class.
6. **Human/simulation realizations:** current V2 is intentionally equipment-oriented; the chassis should not be generalized merely for hypothetical future profiles.
7. **Management/lifecycle minimum:** CCOM/OSUS/OPC show that whole-device information can be rich, but the chassis itself should not prematurely define which lifecycle/management subjects become mandatory modules.

These are validation questions for the ontology, architecture, and requirements groups, not reasons to coin a new class now.

---

# Phase C — Source standing within the group

## 8. Relative standing by contribution

The following standing is assigned **after** all fourteen sources were independently extracted and compared.

### 8.1 Foundational chassis candidates

**SOSA Domain-Specific Data Model (2022)**  
Strongest source-native model in this group for the **functional/operational Sensor as the whole subject**. It directly answers the concern that a Sensor can have Components, health/state/configuration, and a separate host Platform.

**OPC UA Part 100: Devices (2025)**  
Strongest generic source in this group for the **bounded physical Device/equipment subject**. It gives Device a clear place relative to Component and Software and supplies identity, health, interfaces, and composition without constraining the device to one industry.

**MIMOSA CCOM**  
Strongest source in this group for the **whole physical-asset lifecycle frame**: asset/type/model, composition, site/segment context, measurements/events, condition/health, and lifecycle/work information. It is broader than sensing but strongly supports V2’s “complete operational subject” objective.

**OSUS-R Asset model**  
Strongest domain-near corroboration for the motivating class of systems: a whole **physical device** that can produce data, respond to commands, expose capabilities/status/BIT, communicate, and contain multiple sensors. Its implementation-specific/runtime character keeps it from standing alone as the universal chassis.

These four are complementary rather than interchangeable: SOSA DSDM is strongest on **Sensor role**, OPC Devices on **generic device realization**, CCOM on **whole lifecycle**, and OSUS-R on **operational unattended-sensor/device reality**.

### 8.2 Supplemental conceptual coverage

**AAS Part 1** — valuable broad Asset/digital-representation and managed-part distinctions, but Asset is too broad to bound V2 alone.

**ISO/IEC 29182-4 SNRA** — valuable sensing-domain physical/functional entity distinction and sensor-network context; boundary is usually larger than one equipment subject.

**PA-DIM** — excellent example of how the generic Device chassis is specialized into a well-bounded operational device family; too process-automation-specific to become V2’s universal family.

### 8.3 Specialized / gap-filling distinctions

**IEEE 1451.1-1999 / ISO/IEC/IEEE 21451-1:2010** — NCAP/transducer boundary and smart-transducer architecture; useful but narrow, and one conceptual lineage.

**RFC 7326** — unusually clear Device/Component/Power Interface physical distinctions and deployment context; specialized to energy management.

### 8.4 Cross-cutting semantics that belong elsewhere

**OGC OMS 3.0** — central for observation/sampling semantics, but those semantics describe what sensing does rather than the whole equipment chassis.

**PROV-DM** — central for provenance, deliberately domain-neutral.

**NIEM 6.0** — broad reusable exchange semantics and mapping/extension discipline rather than a sensing-equipment boundary.

### 8.5 Broad operational context, not chassis

**JC3IEDM 3.1.4** — rich operational object/type, status, capability, location, and action context, but far broader than the intended V2 family.

---

# Phase D — Chassis synthesis gate

## 9. Candidate result

### 9.1 No single donor noun adequately defines the V2 family

The comparison does **not** support replacing the current baseline with one newly preferred noun:

- **Asset** is too semantically variable.
- **Device** is strong for physical realization but says nothing about sensing role.
- **Sensor** is strong for operational role but, without qualification, can be misread as a single transducer and is not intrinsically physical in the SOSA/SSN baseline.
- **Sensor network** is generally too large an aggregate.
- **Process Automation Device**, **NCAP**, and **Energy Object** are purpose/domain-specific.
- **OBJECT-ITEM** and **Entity** are far too broad.

The source evidence therefore does not justify inventing a new umbrella class merely to collapse these dimensions.

### 9.2 The strongest candidate chassis is a **two-axis bounded frame using existing sourced concepts**

The Phase D candidate is:

> **The V2 DIM is about a System whose principal operational role is sensing/observing and whose realization is physical equipment, modeled as the complete operational subject rather than merely as an observation producer or individual transducer.**

This is a **boundary statement**, not a new class name.

In the current CSAPI vocabulary, the most direct representation remains:

- `systemType = Sensor`
- `assetType = Equipment`

The Conceptual / Information / Domain Model study now provides independent support for both halves:

- **Sensor-role support:** SOSA DSDM, SNRA, IEEE/ISO 1451 lineage, OMS.
- **physical-device/equipment support:** OPC Devices, PA-DIM, OSUS-R, CCOM, RFC 7326, SNRA.
- **whole-subject support:** SOSA DSDM, OPC Devices, CCOM, OSUS-R, PA-DIM, AAS.

### 9.3 Candidate anchor and realization

The candidate model should distinguish:

1. **Anchor / operational identity:** a **System characterized as Sensor** because sensing/observing is the primary role that makes the subject belong to this V2 domain.
2. **Realization constraint:** **Equipment** because this V2 effort is about physically realized sensing systems, not human or simulation Sensors.
3. **Internal constituents:** Components/subsystems may be physical or software and may sense, actuate, compute, communicate, store data, provide power, or manage the system.
4. **External host/context:** Platform, deployment, site, organization, network, environment, and operator are related context unless source evidence makes them enduring constituents of the System.
5. **Outputs/interactions:** observations, commands, events, products, provenance, and management records are information about or interactions with the System; they do not replace the System as the chassis.

### 9.4 Why “Device” is not adopted as a competing root

The Phase B comparison shows that **Device** is the best recurring cross-community corroboration for the physical-equipment side. It should be retained as a mapping/comparison concept.

It should not displace the current CSAPI `Equipment` facet at this stage because:

- Device is functionally neutral and therefore cannot establish domain membership.
- “Equipment” is already native to the intended binding environment.
- Equipment can naturally encompass one or more hardware devices/pieces of equipment, which may better fit large or composite sensing systems.
- adopting Device as a new V2 root would unnecessarily turn a donor comparison concept into profile-owned architecture before the next validation groups are checked.

### 9.5 Why “Asset” is not adopted as the chassis

Asset is useful as a superconcept and for lifecycle/digital-twin mappings, but the donor evidence shows incompatible breadth:

- AAS Asset includes physical, digital, and intangible assets.
- CCOM Asset is grounded in physical asset lifecycle management.
- OSUS-R Asset is a physical device.
- SOSA/SSN Asset is broader than System and Platform.

Therefore an unqualified V2 **Asset** root would weaken, not strengthen, the boundary.

### 9.6 Why the current baseline survives the clean-slate challenge so far

The clean-slate study was not supposed to defend `Sensor + Equipment`; it was allowed to replace it.

After independent extraction and comparison, no Conceptual / Information / Domain Model source provides a single established concept that captures both:

- the **primary sensing role**, and
- the **physical whole-equipment realization**

more faithfully than the current two-facet combination.

Instead, the donor group strengthens the conceptual rationale for keeping those dimensions separate. The current baseline therefore **survives this source-type group**, but it is not yet promoted to a final V2 domain decision because the required ontology, architecture, and requirements validation has not occurred.

---

## 10. Candidate boundary consequences

If the candidate survives cross-group validation, the following consequences would be justified without creating a new V2-owned class:

- A weather station, UGS node, camera system, radar sensor, radiation detector, or similar equipment can be one top-level Sensor System even when it has multiple internal sensing elements.
- Internal processors, radios, storage, software, actuators, power subsystems, and diagnostic functions do not stop the whole from being a Sensor when the whole system’s primary role remains sensing/observing.
- A vehicle, building, mast, pod, or other host is not automatically part of the Sensor; host Platform and deployment relationships must remain explicit.
- An interchangeable payload is not automatically permanent composition merely because it is physically attached.
- An Observation is not the Sensor, and an observation model is not a substitute for the whole-system model.
- Asset/digital-twin/lifecycle/provenance concepts can enrich the Sensor System description without redefining the chassis.

These are synthesis implications to validate, not yet clean-DIM normative statements.

---

# 11. Required next validation

Before the candidate chassis is promoted into `Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md`, the PITON requires testing against the next groups.

## 11.1 Ontologies / Formal Semantic Models

Test whether the candidate boundary remains semantically coherent across:
- current SOSA/SSN Asset → System/Sensor/Platform distinctions;
- SAREF device/system concepts;
- SWEET instrument concepts;
- other ontology sources in the frozen corpus.

Key question: **Does the ontology evidence support a Sensor-role + physical-equipment-realization boundary without requiring a new class?**

## 11.2 Reference Architectures / Architectural Frameworks

Test:
- physical vs functional decomposition;
- Sensor vs Platform/host boundary;
- controller/compute/comms roles;
- system/subsystem composition;
- distributed and networked sensing cases;
- deployment context.

Key question: **Can the candidate chassis remain stable when the equipment is embedded in a larger architecture or distributed across components?**

## 11.3 Requirements / Capability / Operational Specifications

Stress-test with requirements sources for:
- multifunction sensor/effector equipment;
- operational management and health;
- component/controller boundaries;
- concrete deployed system expectations.

Key question: **Does “primary role = sensing + realization = equipment” include the real systems V2 must support without silently excluding required cases?**

---

## 12. Current decision status

| Question | Standing after CIDM chassis study |
|---|---|
| Does one donor supply a complete universal chassis term? | **No.** |
| Is a new umbrella class justified? | **No.** |
| Strongest functional/operational chassis evidence | **SOSA DSDM Sensor** |
| Strongest generic physical-device chassis evidence | **OPC UA Device** |
| Strongest whole-lifecycle asset frame | **MIMOSA CCOM Asset** |
| Strongest motivating-domain physical-device corroboration | **OSUS-R Asset** |
| Best recurring physical realization concept across donors | **Device / physical equipment** |
| Current V2 anchor candidate | **System characterized as Sensor** |
| Current V2 realization candidate | **Equipment** |
| Current formal CSAPI comparison | `systemType = Sensor` + `assetType = Equipment` |
| Candidate chassis status | **Survives CIDM group; pending ontology/architecture/requirements validation** |
| Clean V2 DIM edit | **Blocked until cross-group validation** |

## 13. Immediate next step

Proceed to the **Ontology / Formal Semantic Model** source group as the next validation layer. The task is not to restart chassis discovery from scratch, but to attempt to falsify or refine the candidate boundary produced here.
