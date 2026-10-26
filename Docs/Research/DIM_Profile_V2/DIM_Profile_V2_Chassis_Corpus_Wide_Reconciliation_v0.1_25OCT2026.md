# DIM/Profile V2 Chassis — Corpus-Wide Capability Reconciliation

**Working decision record v0.1 — 25 October 2026**  
**Scope:** Frozen 182-source V2 donor corpus  
**Purpose:** Correct the source-type eligibility gap exposed by SAPIENT before DIM-anatomy work begins.

## 1. Method correction

The original chassis study used the fourteen artifacts classified as Conceptual / Information / Domain Models as its discovery population, then challenged the candidate with ontology, architecture, and requirements sources. That was orderly, but SAPIENT exposed a weakness: **primary source type had become too strong an eligibility gate**.

The corrected rule is:

> **Source type determines how an artifact should first be understood; it does not determine whether that artifact is allowed to challenge the chassis.**

All 182 artifacts in the frozen source-type audit were therefore screened for one question: does the artifact define or operationalize a top-level real-world/domain participant, system boundary, assembly, node, device, asset, platform, instrument, component aggregate, or equivalent construct that could plausibly alter the V2 chassis?

## 2. Complete corpus accounting

| Disposition | Count |
| --- | ---: |
| A — already explicitly chassis-tested | 38 |
| B — previously under-contested; explicitly reconciled here | 13 |
| C — lineage/companion/specialized evidence; no independent chassis vote | 101 |
| D — no credible chassis potential | 24 |
| E — operational/reference falsifier | 6 |
| **Total** | **182** |

The row-by-row record is `DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv`.

The thirteen B artifacts represent about ten independent challenger lineages because ISA contributes two artifacts and the radiation-instrument family contributes three exchange standards.

## 3. Explicitly reconciled challengers

### 3.1 SensorML 3.0 — source 13

SensorML should have been allowed to compete directly rather than only serving as foundation/binding evidence. It defines `PhysicalComponent` for an indivisible physical processing device and `PhysicalSystem` for a hardware device modeled as an aggregate of components. A sensor system can contain sensing, acting, and computational subprocesses.

**Result: chassis survives, with a binding refinement.** `PhysicalSystem` is not sensing-specific and does not cover every atomic device; `PhysicalComponent` may be the appropriate concrete SensorML class for some equipment. SensorML therefore confirms composite whole-system semantics but does not supply one universal V2 root. Concrete SensorML class choice remains a later binding decision.

### 3.2 SAPIENT / BSI Flex 335 — source 21

SAPIENT defines a substantive `Node` model with node types, capabilities, modes, status, dependencies, platform nodes, fusion nodes, hierarchy, and recursive configuration.

**Result: chassis survives; SAPIENT becomes a high-value structural donor.** Node is intentionally broader than the V2 family: it can represent sensing and non-sensing roles, platform/fusion roles, human participation, and software-oriented realizations. SAPIENT is explicitly system-of-systems oriented. Sensor Edge Node is closer to V2 but remains a SAPIENT architectural/interface role, not a cross-community physical-equipment root.

### 3.3 Integrated Sensor Architecture — sources 37 and 42

ISA DMS/SDD define ISA Component, Composition, Composition Interface Component, composition members, virtual components, network and deployment boundaries, plus properties, observables, commands, state, capability, and relationships.

**Result: chassis survives; ISA Composition becomes a major structural donor.** ISA Component is an interface/behavioral participant and can be virtual. ISA Composition is useful for complex-system exposure but is neither intrinsically physical nor intrinsically sensing. ISA reinforces the need to distinguish physical System identity from network-visible representation.

### 3.4 Redfish resource model — source 89

Redfish distinguishes Chassis, ComputerSystem, Manager, Sensor, and AutomationNode, with strong physical-container and management relationships.

**Result: chassis survives.** Chassis is a physical-container concept, ComputerSystem is computing-oriented, and AutomationNode is industrial-automation oriented. Redfish is valuable for physical containment, management separation, instrumentation, health, power, and hierarchy, but no Redfish root captures the sensing-role plus physical-realization intersection.

### 3.5 MIMOSA OSA-EAI — source 101

OSA-EAI exchanges and stores asset registry, condition, maintenance, and reliability information for physical assets.

**Result: chassis survives.** This converges with the already-tested CCOM Asset finding: Asset is an important whole-lifecycle physical subject but is functionally broader than sensing equipment.

### 3.6 Matter 1.3 — source 107

Matter organizes Nodes, Endpoints, Device Types, and composed devices. Sensor and non-sensor device types share the same architecture.

**Result: chassis survives.** Matter Node is principally a protocol/data-model boundary, while Device Type is broad across automation roles. Matter contributes an important composed-device pattern but not a universal sensing-equipment root.

### 3.7 IEEE 1451.0-2024 current family — source 114

Current public evidence retains the NCAP, TIM, TransducerChannel, transducer/network services, and TEDS architecture. The prior public-source reconstruction explicitly treated exact normative details as access-gated.

**Result: chassis survives; exact normative details remain gated.** IEEE 1451 is a rich smart-transducer interface/information architecture, but it is narrower than the complete employed equipment System. A TransducerChannel is not automatically the whole System or even a physical component. IEEE remains a high-value transducer/channel semantic donor, not a replacement chassis.

### 3.8 OMA Lightweight M2M 1.2.2 — source 129

LwM2M defines a Client running on a Device and an Object/Object Instance/Resource data model for device management and service enablement.

**Result: chassis survives.** LwM2M Client is a protocol component; Device is a generic managed IoT subject. Neither establishes sensing as the defining role. The source reinforces the distinction between management/interface identity and physical/domain equipment identity.

### 3.9 RFC 8348 Hardware Management — source 133

RFC 8348 defines a physical hardware/component hierarchy with class, parent, containment, and identity/state information. Sensor is one hardware class among chassis, modules, ports, power supplies, processors, and others.

**Result: chassis survives.** The model is excellent for physical composition but contains no sensing-domain membership criterion for the whole equipment.

### 3.10 Radiation-instrument exchange family — sources 163, 164, 166

The exchange standards organize information around complete radiation measurement/detection instruments, detectors/sensors, results, status, and related instrument information.

**Result: chassis survives.** These are strong domain examples of a whole Instrument/Equipment subject containing detector/sensor information, but the domain class is intentionally modality-specific and cannot serve as the universal heterogeneous sensing-system root.

## 4. Lineage control

The audit did not count every schema, API, test harness, guidance document, or submodel as an independent chassis vote. Examples of companion evidence include:

- AAS technical-data, bill-of-material, hierarchy, and capability submodels beneath the already-tested AAS Asset metamodel;
- NIEM Core/domain schemas beneath the already-tested NIEM model;
- SOSA IDL/OpenAPI artifacts beneath the tested SOSA DSDM/architecture;
- SAPIENT protobuf/test artifacts beneath BSI Flex 335;
- SNRA vocabulary/interface/application artifacts around the tested entity/architecture parts;
- Redfish battery/power child schemas beneath the Redfish structural challenge;
- historical IEEE 1451 parts and NIST explanatory material around the current-family challenge;
- IETF EMAN concrete MIBs beneath the already-tested RFC 7326 framework.

This prevents a prolific standards family from receiving artificial evidentiary weight merely because it publishes many companion artifacts.

## 5. Operational falsification

The six reference-system/operational sources cannot establish normative terminology, but they were retained as reality checks.

The available TRSS/OmniSense evidence does **not** falsify the current boundary. It supports a recognizable individual sensing-system/equipment viewpoint with explicit components and external operational relationships. The evidence therefore does not require Node, Network, Platform, or system-of-systems to replace the individual equipment/System chassis.

## 6. Reconciled chassis decision

The source-type gap was real, but after screening **all 182 artifacts** and explicitly challenging the ten under-contested semantic lineages, no source provides a superior universal boundary.

The corpus-wide reconciled V2 chassis remains:

> **Version 2 concerns physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

For the intended CSAPI application profile, the working classification remains:

- `systemType = Sensor`
- `assetType = Equipment`

No new umbrella/root class is justified.

## 7. What the reconciliation adds

The decision now carries these additional guardrails:

1. **Source type is never an eligibility gate for a DIM-boundary challenge.**
2. **Equipment remains broader than Device, Node, Chassis, or SensorML PhysicalSystem.**
3. **SensorML concrete class selection is a later binding decision, not the chassis itself.**
4. **Network-visible identity may be virtual, aggregated, mediated, or role-based and must not be assumed to equal the physical System.**
5. **Physical composition and sensing-domain membership are separate questions.**
6. **Composition visibility is meaningful:** ISA and SAPIENT show that members can be exposed, hidden, aggregated, or represented through another participant.
7. **Domain-specific Instrument models are specializations, not universal roots.**
8. **Lineage must be controlled** so companion artifacts do not masquerade as independent conceptual agreement.

## 8. Consequence for DIM anatomy

The same correction applies to the next research phase.

The fourteen CIDM artifacts remain an important core anatomy population, but they can no longer be the exclusive population merely because of primary source type. Structural evidence must also be admitted from cross-type sources when they define genuine domain organization.

The corpus-wide audit identifies especially important cross-type structural donors for the anatomy phase:

- SensorML 3.0;
- SAPIENT;
- ISA DMS/SDD;
- Matter;
- Redfish;
- RFC 8348;
- MIMOSA OSA-EAI; and
- applicable IEEE 1451 and domain-instrument models.

The next anatomy evidence population should therefore be selected by **structural semantic capability**, not document classification alone.
