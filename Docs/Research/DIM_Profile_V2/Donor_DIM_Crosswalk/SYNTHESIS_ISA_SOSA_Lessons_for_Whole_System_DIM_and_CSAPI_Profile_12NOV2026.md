# What ISA and SOSA Have Taught Us About a Whole-Sensing-System DIM and CSAPI Profile

**Narrative research synthesis · 12 November 2026 · Interpretive findings, not an adopted model**

## Purpose, basis, and status

This paper explains in plain English what our corrected Integrated Sensor Architecture (ISA) and The Open Group Sensor Open Systems Architecture (SOSA) donor assessments contribute to the proposed Domain Information Model (DIM) and OGC API – Connected Systems (CSAPI) Profile. Its purpose is to turn the source audit and Excel crosswalk into understandable research conclusions, open questions, and recommendations for a useful common client Details view. It is a synthesis of existing research, not new original-source coverage, a new domain name, a class hierarchy, a Profile requirement, or a declaration that either standard governs all sensing systems.

The ISA source-first correction is complete within its **documented, bounded review scope**, with six source-definition questions still open. The Open Group SOSA C239 Edition 1.1 (2023) has **191 of 192 registered headings with at least source text or original source-reference pointers examined**, but that is not a claim of 191 complete clause audits; its eight original C239 native companions, external references, figures and restricted Appendix C retain material holds. **SOSA is still ACTIVE/OPEN pending the owner's explicit G5-D choice between bounded PARTIAL disposition and continued original-source work.** Nothing here accepts that choice or authorizes the next donor.

The principal basis is the [ISA source-first semantic assessment](ISA21_Source_First_Correspondence_Review_09NOV2026.md), [ISA closeout and remaining questions](ISA22_Final_Validation_Closeout_09NOV2026.md), [SOSA original-source and master reconciliation](SOSA_G4_F_Original_Corpus_and_Master_Reconciliation_11NOV2026.md), [SOSA 2022 native model/IDL findings with edition caveat](SOSA_G3_N2_Original_2022_DSDM_IDL_and_Master_Reconciliation_11NOV2026.md), and [one canonical donor-to-DIM master](Master_Donor_Concept_to_DIM_Crosswalk.md). More granular auditability resides in the linked source-item ledgers, rather than in the conclusions of this narrative.

## 1. The two standards reveal different but complementary parts of the problem

ISA is particularly informative about how sensing components participate in a connected system. It describes component identities, communications and service roles, declarations of capabilities and data, events, command requests, responses, and how a composition can expose or mediate its members. It is useful for asking what a participant says it supports, what it communicates, and how its interfaces behave.

The Open Group SOSA examines the sensor architecture from another direction. It separates physical hardware elements, plug-in cards, host arrangements, chassis and backplane interfaces, logical modules, software run-time environments, management interfaces, and the roles of processing and other sensor functions. Its physical architecture is intentionally much more specific than the equipment types represented by our full set of real-world cases.

These perspectives overlap, but their native entities are not automatically interchangeable. An ISA component that communicates through a distinct network identity does not thereby become a separately installed physical probe; a SOSA plug-in card or logical module does not automatically become its own independently discoverable CSAPI System. A useful common DIM needs to preserve the underlying meanings rather than map similar labels into one invented universal class.

**Interpretive conclusion:** ISA helps us understand how connected components declare, exchange, and manage information; SOSA helps us understand how specialized equipment and logical functions may be arranged into a functioning sensor. Neither standard independently supplies the entire cross-vendor, whole-sensing-system description we seek. [ISA evidence](ISA21_Source_First_Correspondence_Review_09NOV2026.md) · [SOSA evidence](SOSA_G4_F_Original_Corpus_and_Master_Reconciliation_11NOV2026.md)

## 2. System identity, physical equipment identity, and network identity are different

A system may be regarded as a subsystem when considered within a larger context, and the SOSA C239 glossary allows a sensor to refer to a device or a system. ISA's Universal Component Identifier (UCI) establishes an ISA component identity for its source-specific purposes, with additional qualifications for virtual identifiers. Neither finding proves that an ISA UCI, an equipment serial number, a station identifier, or a CSAPI System URI is necessarily the same identifier.

Consider a station with a data logger, one or more measuring instruments, communication equipment, and power supply. The station can be individually described, while constituent instruments can retain product and serial identities and the logger can act as the reporting network participant. A logical or virtual participant might also be exposed through an interface without corresponding one-to-one with physical hardware.

The accepted research direction of **individual system identity** is useful here, but the two donor reviews do not justify a new universal identity syntax or every constituent being an individually exposed CSAPI resource. The eventual model should distinguish a particular system being described, actual identified equipment, manufacturer/model/serial information where established, and identifiers used for network or software participation. Whether this becomes one structure or several related structures remains an owner-controlled modeling question.

**Possible client implication:** A Details view could identify the whole described system and separately identify its contributing equipment, while labeling a publishing gateway or software participant appropriately. We should never imply that one communication identity automatically proves the existence, position, or provenance of a distinct physical sensor.

## 3. Physical composition, logical composition, and connection are not the same relationship

ISA's Composition Interface Component (CIC) can broker interactions with members that are visible, opaque, taskable, or not independently taskable. That is a logical and interaction-oriented composition: membership and external visibility do not prove that the elements occupy one box or have a physical *part-of* relationship. The ISA audit also distinguished physical attachment relationships from ISA-defined participation and member exposure.

SOSA provides examples of specific physical architecture and engineering constraints: plug-in cards, chassis, slots, backplanes, electrical and RF interfaces, host platforms, and associated software environments. Those examples demonstrate how meaningful physical integration differs from a message-level or management relationship. They do **not** establish that every kind of sensing system uses a SOSA chassis, a plug-in-card arrangement, or any single fixed equipment hierarchy.

Our equipment examples make this concrete. The reference Dragino arrangement has an external SHT31 probe and a reporting node joined by a cable; the Campbell example has a ClimaVue 50 connected to a CR1000X data logger; and a modular SOSA implementation could have cards in a chassis with software running in an identified environment. These are legitimate but different forms of physical and logical arrangement, with individual installation evidence and design alternatives requiring different evidentiary standing.

**Interpretive conclusion:** Physical containment, installed attachment, electrical connection, network communication, software hosting, and logical membership should not be casually merged into a generic parent-child relationship. This does not automatically mandate separate DIM classes for all six ideas; it establishes questions the remaining donors and real installations must help resolve. [ISA comparison on composition](ISA21_Source_First_Correspondence_Review_09NOV2026.md) · [current equipment and donor rows](Master_Donor_Concept_to_DIM_Crosswalk.md)

## 4. The whole sensing system is more than the observations it produces

An observation or value is essential to sensing interoperability, but it does not by itself explain which equipment produced it, which component reported it, how it was configured, whether it was healthy, or what power and communications constraints affected it. ISA contributes source definitions for component capabilities, configuration, properties, events and control interactions. SOSA separately contributes system architecture, management, health, diagnostics, operating condition and specialized equipment constraints.

The common information problem therefore extends beyond presenting measurement results. We need to investigate information that helps a user understand equipment identity, physical and logical arrangements, supported sensing functions, operational condition, service and management interfaces, and the evidence for each fact. Some of that information may be unavailable or genuinely inapplicable for a particular kind of system.

**Interpretive recommendation:** Treat these as candidate *information concerns* for a whole-system DIM and Profile, not as an approved set of mandatory sections or properties. The relevant question is which information can be standardized accurately across unlike equipment, which should remain optional, and which is better kept in native extensions.

## 5. Health, status, state, mode, configuration, communications and power must not collapse into one field

Both donor assessments show why a generic word such as *status* is insufficient. A sensor may be powered on yet unhealthy, operational but in a particular behavior mode, or sensing correctly while its external communication link is unavailable. A configured capability, the selected mode, the device's operational lifecycle, and the condition of a power source each answer a different question.

The C239 glossary and management chapters distinguish **Health**, **Status**, **State**, **Mode**, **Configuration** and **Capability**. ISA's source model distinguishes declared capabilities in configuration, present reported values in status, source-specific operating modes, and other device and network condition properties. Importantly, source-specific enumerations or lifecycle states do not establish one universal status-code list for every sensor.

For a client, those distinctions could support meaningful descriptions such as: the overall system is operational; a sensing component reports degraded health; the network link is down; and power remains available. That is much more informative than a single unexplained warning. It also prevents us from inferring that a lack of communication proves that the equipment has failed or lost power.

**Interpretive recommendation:** Preserve these concepts as distinct candidate information needs, while deferring exact DIM fields, cardinalities, state vocabularies and Profile requirements until cross-donor reconciliation. [ISA DMS and source-meaning audit](ISA21_Source_First_Correspondence_Review_09NOV2026.md) · [SOSA model and glossary comparison](SOSA_G3_N2_Original_2022_DSDM_IDL_and_Master_Reconciliation_11NOV2026.md)

## 6. Declaring a capability, requesting an action, receiving a response and proving a physical effect are different

ISA defines command declarations and request/response messages, along with authorization and reportable dispositions. A successful response from an authorization function can mean it successfully determined **authorization was denied**, while a successful command disposition does not independently measure whether the desired physical effect occurred. Queued or in-progress states differ from final outcomes.

SOSA has distinct mission tasks, internal assignments, management interfaces and component operations, with some entries explicitly marked **Future** rather than currently defined. This matters because an architecture's listed operation, a source example, and a verified working CSAPI Command endpoint are different levels of evidence. The 2023 C239 normative management OpenAPI original files also remain unexamined; the later 2025 API metadata cannot fill that gap by assumption.

**Interpretive recommendation:** Any later model of control should distinguish supported or declared capability, invocation, permission, progress, reported result and independently evidenced physical outcome when relevant. A common client should not display a control simply because a source describes a possible interface, and it must not present a reported outcome as independently verified device behavior. This is an architectural consideration, not approval of new CSAPI Command requirements. [ISA command and authorization findings](ISA21_Source_First_Correspondence_Review_09NOV2026.md) · [SOSA native-source holds](SOSA_G4_F_Original_Corpus_and_Master_Reconciliation_11NOV2026.md)

## 7. The reporting component is not automatically the observing instrument

The ISA audit distinguished the ISA Event message and its reported source component from a performed physical observation. A controller, logger, composition interface or relay might author, aggregate, broker or transmit information that was originally sensed elsewhere. The source identity of a message does not, by itself, identify the physical instrument that measured a property.

In the Campbell reference case, a ClimaVue 50 may sense properties while the CR1000X collects and reports results. In the Bennett's Point historical case, **two original NOAA temperature means** were distinguished from **four project-created digital representations**; the copies were not four independent original observations. The original result-time question was preserved instead of inventing the missing time.

These examples reveal a fundamental provenance requirement for our research: keep separate the original measuring act, original source record, reporter or processor, and subsequent representations when the evidence permits that separation. This does not prove every device supports a full traceable provenance chain; it tells us not to erase distinctions when the available records show one.

**Interpretive recommendation:** Our eventual Details view should strive to answer *what physically sensed this, what reported it, what transformed it, and how do we know?* Exact provenance fields and required evidence grades still need cross-donor and owner review. [ISA source-event distinction and case holds](ISA21_Source_First_Correspondence_Review_09NOV2026.md) · [Bennett's Point source/case comparisons](Master_Donor_Concept_to_DIM_Crosswalk.md)

## 8. The equipment cases are a reality check against attractive but incorrect abstractions

The Dragino reference arrangement distinguishes a cabled external sensing probe from the node that reports data. AirGradient's two PMS5003 sensing modules show that multiple sensing elements do not necessarily mean multiple network-visible Systems. Campbell distinguishes a logger from a connected instrument and a measured atmospheric property from a separate logger-internal property. Bennett's Point reveals station identity, real historical serials and measurements, original-versus-derived values, and uncertain original provenance and times.

The evidence grades are not identical: manufacturer configurations, illustrative combinations, a real historical station record, and synthetic API examples have distinct standings. A product manual may establish what could be connected, but not what was actually installed at a specific date and location. An interoperability message can establish a reported value, but not always the original measurement source or method.

**Interpretive recommendation:** Continue testing emerging common information concerns against different equipment cases. A DIM should not force undocumented installations, fictitious sensor serial numbers, or artificial identity links into a record simply because a uniform Details view has a place for them. [Empirical examples and distinctions in the master](Master_Donor_Concept_to_DIM_Crosswalk.md) · [ISA preservation and case limitations](ISA22_Final_Validation_Closeout_09NOV2026.md)

## 9. What the master Excel really is — and what it is not

The canonical crosswalk is an evidence and comparison instrument, **not a completed DIM specification**. It currently has **329 information-review rows**, real-equipment/source cases on the left, donor comparisons, grouped OGC-related foundations, and a **proposed** DIM column on the right. The ISA correction accounted for all **480 named ISA Data Model Specification entries**, with **474 source-supported** and **six unresolved** definition questions; this is not a recommendation to create 480 common DIM attributes.

The SOSA work contributed **776 packet-level source correspondences across 117 distinct existing rows**, linked to 1,583 source-item references, with no DIM adoption. The number 776 is the sum of packet-to-row contributions, not a count of unique concepts, approved properties or comprehensive source audits. Similarly, the spreadsheet's existing 329 candidate rows do not equal 329 adopted DIM elements.

The useful comparison is semantic. ISA's component identity and SOSA's architecture-specific identity may both inform a candidate persistent identity concern without becoming equivalent to a physical serial number or a CSAPI System identifier. A physical constituent, a logical member and a network-visible participant may each contribute useful information while retaining their native meanings.

**Interpretive recommendation:** Later reconciliation should evaluate what deserves common representation based on source meaning, actual equipment cases and OGC compatibility, not on which donor has the most matches or the most terminology. No donor vote should turn a source-specific class into an automatic generic DIM class. The workbook retains its same original **26 editable worksheets** and the verified comparison values; its source-coverage metadata remains at the older G3-N2 snapshot, while newer SOSA 191-heading contact accounting is recorded in G4 evidence. [Current master](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) · [SOSA G4 accounting](SOSA_G4_F_Original_Corpus_and_Master_Reconciliation_11NOV2026.md)

## 10. A possible common client Details view — explicitly not yet adopted

A coherent client Details view might first establish the **individual described sensing system**: its identifier, description, manufacturer/model where known, and source or installation context. It could then show associated equipment and established relationships, without pretending that a logical composition, a communications role and a physical assembly are all the same. For one system that could mean a cabled probe and logger; for another it might mean a SOSA chassis with plug-in cards and hosted software functions.

Additional information areas could describe what the system declares it can sense or do, the observations and data products associated with it, and the current operational information actually available. Health, operating state, selected mode, configuration, power and network condition could be presented separately where a source provides those distinctions. Any available controls should be clearly distinguished from declared capabilities, and command responses from proven physical effects.

The common experience would be **consistent meaning and intelligible presentation, not identical content from every vendor**. A meteorological station may have maintenance and instrument records; a modular SOSA implementation may have card/profile, run-time environment and management information. Either could fit a coherent viewing experience without asserting that all fields or internal structures are universal.

This is a **design hypothesis to test in the existing later owner checkpoints**, not a client specification, an adopted schema, or authorization to change Glaux. The exact layout, data model, supported Profile requirements and minimum/optional content remain undecided.

## 11. Research methodology lessons: completeness is not a spreadsheet checksum

The corrective ISA and SOSA work revealed that recording a standard in a list, extracting its terminology, comparing a few clauses, and auditing its complete original source corpus are different accomplishments. ISA's source-first effort reconciled original definitions and preserved six exact uncertainties instead of guessing answers. SOSA's earlier apparent closeout was reopened because its original 2023 native files and substantial sections were not adequately inspected, and the most recent reconciliation still supports only **bounded PARTIAL** source standing.

The improvements are meaningful: edition/publisher distinctions, stable original source IDs, Rule versus Recommendation versus Permission versus Observation, exact native access standing, limitations, real equipment evidence and progressive master integration. But methodology must not become busywork: source work should be sized according to the complexity of actual original material, not artificial prompt counts, and unchanged Excel content should not be published or rechecked repeatedly. We must distinguish a complete workbook from a complete donor assessment.

The six ISA source questions illustrate why narrow unresolved facts should remain open without invalidating hundreds of independent reviewed entries. They concern *Level*, *Link Loss*, *Orientation*, *Signal Strength Ratio*, the *Adjust Power* rate mechanism, and *Slew Velocity/Rotation Rate* axes. Their original source meanings were rechecked; no authoritative repair was invented.

**Interpretive recommendation:** For future donors, identify the actual original corpus first, inspect relevant original source clauses and native files to justified depth, integrate useful comparisons incrementally, and close a donor only at an evidence-based owner checkpoint. Each donor should also produce a **plain-English synthesis of what it adds, what it challenges, and what it does not justify**, so the work remains understandable to a human decision-maker. [Reusable lessons](LESSONS_Donor_Review_Process.md) · [ISA closeout limitations](ISA22_Final_Validation_Closeout_09NOV2026.md) · [SOSA G4 closure recommendation](SOSA_G4_F_Original_Corpus_and_Master_Reconciliation_11NOV2026.md)

## 12. Recommendations for the next phase of the broader DIM/Profile effort

The current findings support continuing with a **common individual sensing-system description** while keeping physical equipment, network-facing participants and logical functions appropriately distinct. They support considering **identity and equipment relationships, declared capabilities, observations and provenance, current operating condition and configuration, and management/control semantics** as candidate whole-system information concerns. They do not yet select a final overarching name, a chassis class, a finished hierarchy, accepted fields, allowed cardinalities, or CSAPI Profile SHALL statements.

The remaining donors should **challenge these hypotheses**, not merely supply more terms agreeing with ISA and SOSA. For example, the later SAPIENT donor may illuminate different system boundaries, message patterns and integration functions, but its native meanings must be examined on their own sources before it is reconciled with ISA, The Open Group SOSA and the OGC foundations. A term present in only one donor could be crucial for the equipment cases; a label shared across many standards might hide a material semantic difference.

The existing owner-controlled process should be maintained: coherent and ready information may be considered at Step 24, broader cross-donor reconciliation and case testing belong in Steps 35–39, and a named-version decision belongs at Step 40. This synthesis does **not** carry out those decisions early. The common client view should be tested against source-qualified case data and actual CSAPI/SensorML/SWE representation, rather than merely rendered from invented uniform examples.

Regarding the current The Open Group SOSA decision, **bounded PARTIAL disposition is recommended as an owner option**, because the existing comparison has useful defensible material but lacks the original 2023 native companions, restricted content and other original-source audits needed for a comprehensive claim. That recommendation is **not** acceptance, automatic donor closeout, or permission to start SAPIENT. The alternative remains keeping SOSA open for primary-source completion; see the [G5-D owner decision packet](SOSA_G5_D_Owner_Disposition_Decision_Packet_11NOV2026.md).

## Central takeaway

**The DIM should eventually help answer not merely “What is this sensor?” but “What is this sensing system, which physical equipment and logical functions contribute to it, how are they related, what does it produce, what is its operating condition, and what evidence supports those statements?”**

ISA contributes source-backed meaning about connected participation, capability declarations, events, requests and responses. The Open Group SOSA contributes source-backed meaning about specialized system architecture, physical elements, logical modules, management roles and operational distinctions. The real equipment cases show why neither perspective can substitute for actual installation and observation evidence.

This is the value of the corrected donor work: better-informed **questions and comparison boundaries** from which a trustworthy common DIM, profile-aware CSAPI client and defensible Profile may eventually be developed. **The final model, class hierarchy, information requirements, Profile language and source-completeness claims remain subject to their separate evidence and owner decisions.**

---

**Document standing:** Research synthesis based on saved ISA and SOSA corrections and master as of 12 November 2026. The GitHub research branch is authoritative; this narrative is a human-readable interpretation and makes **no modifications to the canonical comparison, Excel, approved design, SOSA closure decision or downstream donor state**.
