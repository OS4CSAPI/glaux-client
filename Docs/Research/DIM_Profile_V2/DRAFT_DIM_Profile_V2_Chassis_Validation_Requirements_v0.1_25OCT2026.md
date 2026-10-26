# DIM/Profile V2 Chassis Validation — Requirements, Capability, and Operational Specifications

**Working draft v0.1 — 25 October 2026**  
**Status:** Final cross-group validation required by the active PITON before chassis promotion.  
**Candidate under test:** a physically realized equipment `System` whose defining operational role is sensing/observing, modeled as the complete operational subject; the realization may consist of one or multiple hardware elements and may contain heterogeneous supporting components.

## 1. Validation question

Do concrete requirements and operational specifications expose real systems that the candidate cannot describe faithfully, or do they support the distinction between:

- the **whole operational sensing System**,
- its **physical equipment realization**,
- its internal sensing/non-sensing components,
- its capabilities/interactions, and
- its external deployment/network context?

The source-type audit identifies six artifacts in this group:

1. ISA Controller Requirements 6.0r4.
2. ISA Component Requirements 6.0r4.
3. NISTIR 8259A IoT Device Cybersecurity Capability Core Baseline.
4. IEEE N42.38-2022 spectroscopy-based radiation portal monitor performance standard.
5. IAEA Nuclear Security Series No. 44-T.
6. ISO 22188:2023.

---

## 2. Integrated Sensor Architecture — Controller Requirements 6.0r4

**Evidence depth:** full source-native project-provided PDF.

ISA describes itself as an interoperability layer for communication between **networked devices, algorithms, and user interfaces** in a tactical domain. An ISA Controller is an ISA component that supplies core ISA services. The requirements address discovery, registration, configuration, status reporting, command brokering, observation handling, availability monitoring, authorization, live data, subscription, and related network behaviors.

### V2 consequence

The Controller Requirements do not define a physical sensor/equipment family. They define an interoperability-role component that can mediate many different kinds of participants.

This is important negative evidence: **network role is not physical chassis identity**. A controller/service component should not be promoted into the V2 System root merely because it brokers sensor interactions.

**Result:** cross-cutting requirements layer; does not challenge the candidate chassis.

---

## 3. Integrated Sensor Architecture — Component Requirements 6.0r4

**Evidence depth:** full source-native project-provided PDF.

The Component Requirements are especially useful as a stress test because they deliberately avoid assuming that every interoperating component is one physical sensor device.

### Capabilities are heterogeneous

An ISA component declares:

- **commands** it can execute;
- **properties**, which are state information about the component; and
- **observables**, which are data elements about observations made by the component.

ISA groups properties, observables, and commands together as component capabilities and carries readiness/reporting state for them.

### Virtual components are first-class operational participants

ISA requirements explicitly support **virtual ISA components**. A physical or logical ISA component can announce a virtual component, provide its configuration and property status, publish its observations, and support commands for it.

### Compositions can hide multiple subcomponents behind one interface participant

ISA's architecture terminology defines an ISA composition as a collection of components interoperating with an ISA network through a single Composition Interface Component. This supports a distinction between an externally visible interface identity and the internal component structure behind it.

### V2 consequence

ISA strongly reinforces several boundary rules:

1. **Observation capability does not make an interface participant physically a Sensor device.**
2. **Command capability does not disqualify a sensing subject.** Real interoperating components can both produce observations and execute commands.
3. **Component is not a physical-realization invariant.** ISA components may be virtual.
4. **One exposed operational identity may represent multiple internal components.**

The V2 chassis therefore needs an explicit physical-equipment realization constraint in addition to a sensing role. At the same time, a whole sensing System may legitimately expose properties, observations, commands, status, configuration, and other management behavior without losing its sensing identity.

**Result:** strongly supports role/realization separation and heterogeneous whole-system capability.

---

## 4. NISTIR 8259A — IoT Device Cybersecurity Capability Core Baseline

**Evidence depth:** official NIST publication/scope and related NIST program definition.

NISTIR 8259A defines device cybersecurity capabilities implemented through device hardware/software. The broader NIST IoT program defines an in-scope IoT device as having at least one **transducer (sensor or actuator)** for interacting with the physical world and at least one network interface for the digital world. Such a device can function on its own but may depend on other devices or systems for some functionality.

The 8259A baseline includes capabilities such as device identification, configuration, data protection, logical interface access, software update, and cybersecurity-state awareness.

### V2 consequence

NIST provides independent operational evidence for a whole physical device that:

- contains sensing **or** actuation capability rather than being identical to a transducer;
- includes network/software/security behavior beyond physical sensing;
- has persistent identity and configuration/state; and
- may depend on external systems without becoming identical to those systems.

However, the NIST IoT Device category is **too broad** for V2 because actuation alone can satisfy the transducer criterion. It is therefore excellent corroboration for the equipment/device realization axis but cannot establish the sensing-family membership criterion.

**Result:** supplemental physical-device and lifecycle/management validation; too broad functionally to define the chassis alone.

---

## 5. IEEE N42.38-2022 — Spectroscopy-Based Radiation Portal Monitors

**Evidence depth:** official IEEE scope/metadata; complete normative text not available in this pass.

IEEE identifies N42.38-2022 as the active standard describing performance requirements for **spectroscopy-based radiation portal monitors** used in homeland-security applications.

### V2 consequence

This is a domain-specialized operational-equipment standard rather than a general information model, but that specialization is precisely what makes it useful as a chassis stress case.

A radiation portal monitor is recognized as one operational equipment/system type by its monitoring/detection purpose and performance, not as an abstract observation record or an individual radiation detector element.

The public scope does not justify importing detailed N42.38 performance semantics into V2. It does support the existence of mature equipment families whose whole identity is established by a sensing/detection mission.

**Result:** supports the whole sensing-equipment boundary; detailed conclusions are limited by normative-access ceiling.

---

## 6. IAEA Nuclear Security Series No. 44-T

**Evidence depth:** official IAEA online publication text.

IAEA 44-T addresses detection of nuclear and other radioactive material at state borders and describes multiple classes of radiation detection equipment.

The publication distinguishes equipment such as:

- personal radiation detectors;
- handheld gamma/neutron survey meters;
- handheld radionuclide identification devices;
- fixed radiation portal monitors;
- mobile systems; and
- airborne systems.

Of particular chassis importance, a fixed radiation portal monitor is described as a pass-through monitor that may consist of **one or two pillars containing gamma detectors**, optionally neutron detectors, and may also include an occupancy sensor and video recording. Spectroscopic portal monitors can both detect radiation and identify radionuclides.

IAEA also distinguishes **portable**, **mobile**, and **fixed** equipment operationally.

### V2 consequence

This is strong reality-check evidence that a recognized sensing/detection System:

- may contain multiple sensing elements;
- may contain different detector modalities;
- may contain non-detection supporting sensors (for example occupancy);
- may include software/analysis and ancillary recording functions;
- may be fixed infrastructure rather than a handheld/device-shaped object; and
- can remain one operational equipment subject because of its integrated monitoring purpose.

This directly supports retaining **Equipment** as broader than a single Device and validates the “complete operational subject” framing.

**Result:** strong operational validation of composite physical sensing equipment.

---

## 7. ISO 22188:2023

**Evidence depth:** official ISO scope/abstract.

ISO 22188 specifies methods and means for monitoring inadvertent movement and illicit trafficking of radioactive material, with guidance for both **stationary and portable/handheld instruments**. Its emphasis is operational and includes requirements derived from monitoring traffic/commodities at border facilities. The stated users include regulators, law-enforcement agencies, equipment manufacturers, and end users.

The standard's scope covers operational use of multiple monitoring-instrument forms rather than one hardware form factor.

### V2 consequence

ISO 22188 independently reinforces the IAEA evidence:

- sensing-equipment membership is operationally defined by the monitoring/detection purpose;
- the relevant family spans fixed/stationary and portable realizations;
- physical form factor is therefore not the chassis;
- operational deployment and user context are important but external to the basic equipment identity.

**Result:** supports the operational-role + physical-equipment boundary.

---

# 8. Cross-requirements comparison

| Source | Real-world/operational subject | Sensing exclusive? | Physical realization guaranteed? | Composite/virtual possibility | Effect on candidate |
|---|---|---:|---:|---|---|
| ISA Controller Req. | Controller/interoperability services | No | No | Logical/service role | Cross-cutting; not chassis |
| ISA Component Req. | ISA interface participant | No — properties, observations, commands | **No — virtual components supported** | Yes | **Strongly requires role/realization distinction** |
| NISTIR 8259A | IoT computing device | No — sensor **or actuator** transducer | Yes for device | May depend on other devices/systems | Strong Equipment/device corroboration; functionally too broad |
| IEEE N42.38 | Spectroscopic radiation portal monitor | Detection/identification central | Yes | Whole monitor/system likely multi-element; detailed text gated | Supports whole sensing-equipment family |
| IAEA 44-T | Radiation detection equipment | Detection central | Yes | **Explicit multi-detector/multi-element systems** | **Strong real-system validation** |
| ISO 22188 | Radiation-monitoring instruments | Monitoring central | Yes | Multiple form factors / deployment types | Strong real-system validation |

---

# 9. Requirements-level answers to remaining open questions

## 9.1 Must every V2 System be “purely” observational?

**No.**

ISA explicitly combines observables, properties, commands, configuration, and management behavior in the same component-capability framework. Radiation detection equipment may also perform identification, alarm generation, analysis, recording, and other functions.

### Refinement

The whole System belongs because sensing/observing is its **defining operational role**, not because every capability is observational.

---

## 9.2 Does the presence of command/actuation behavior exclude a sensing System?

**No.**

ISA components can publish observations and execute commands. NIST's IoT device concept similarly recognizes devices containing sensor or actuator transducers and broader hardware/software functions.

### Refinement

Actuation or commanded behavior is compatible with membership when sensing remains the defining role of the whole equipment System.

This does **not** mean every actuator-containing device belongs; sensing must still establish the domain role.

---

## 9.3 Can virtual/interface components define the V2 chassis?

**No.**

ISA permits virtual components with configuration, state, observations, and commands. Therefore interface visibility and capability exposure are insufficient evidence of physical equipment realization.

### Refinement

The V2 profile must keep **physical-realization status** distinct from interface/component identity.

---

## 9.4 Is “Device” broad enough for the real equipment family?

**Not reliably.**

The radiation domain includes fixed portal monitors consisting of multiple pillars/detectors and other installed systems. SOSA architecture independently permits multiple/distributed hardware elements in one Sensor.

### Refinement

`Equipment` remains the better V2 realization facet. Device can be mapped where donors use it, but the chassis should not require a one-device form factor.

---

## 9.5 Can fixed infrastructure be one sensing System?

**Yes.**

IAEA and ISO operational guidance recognize fixed/stationary radiation detection systems as equipment alongside portable and mobile forms.

### Refinement

Mobility and portability are not membership criteria. A V2 System may be handheld, portable, mobile, vehicle-mounted, fixed, or installed infrastructure.

---

## 9.6 Do requirements sources force network/system-of-systems scope?

**No.**

ISA's network is an interoperability environment containing components and compositions; it does not make the whole network one physical component. NIST likewise allows an IoT device to depend on external systems without merging its identity into them.

### Refinement

External networks/controllers/clouds/platforms remain context unless an explicit enduring composition/System boundary says otherwise.

---

# 10. Requirements-level synthesis

The candidate survives the final required validation group.

The requirements and operational sources do not reveal an excluded real-system class that demands a new chassis term. Instead, they strengthen the boundary by showing why the two axes must remain explicit:

> **The V2 domain concerns physically realized equipment Systems whose defining operational role is sensing/observing. The System is the complete operational subject: it may contain multiple sensing elements and heterogeneous hardware/software/firmware/supporting components, may expose observations, properties, commands, configuration and management behavior, and may be portable, mobile, mounted, fixed, or distributed across multiple hardware elements. Interface participation, virtual representation, host Platform, network membership, or deployment association do not by themselves change the System's physical composition boundary.**

This remains a boundary definition using established source concepts, not a newly invented umbrella class.

---

# 11. Final cross-group validation standing

| Question | Result after Requirements group |
|---|---|
| New chassis term required? | **No** |
| Is sensing exclusivity required? | **No** |
| Can sensing and command/actuation coexist? | **Yes** |
| Can one whole System have multiple detectors/sensors? | **Yes** |
| Can it contain non-sensing components? | **Yes** |
| Can fixed infrastructure qualify? | **Yes** |
| Can virtual/interface component identity substitute for physical realization? | **No** |
| Is Device sufficient as universal realization term? | **No; Equipment remains broader and better supported** |
| Does the candidate survive all PITON-required cross-group validation? | **Yes** |
| Is the chassis now eligible for clean-DIM promotion? | **Yes, subject to a final synthesis record that preserves the mapping cautions and does not invent a new class** |

# 12. Immediate next step

Create the final cross-group chassis decision record integrating:

1. CIDM Phase A–D;
2. ontology validation;
3. architecture validation; and
4. requirements validation.

If that synthesis confirms no unresolved contradiction, promote only the **earned chassis/boundary decision** into the maintained clean V2 DIM/Profile working artifact.
