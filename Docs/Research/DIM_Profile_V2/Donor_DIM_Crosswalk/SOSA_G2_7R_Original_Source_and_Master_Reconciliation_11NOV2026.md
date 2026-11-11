**G2-7R SAME-Excel final exit VERIFIED (11 November 2026):** 33 source-qualified SOSA column-I master cells; current canonical JSON, two CSV, two Markdown, original editable 26-sheet Excel with all 346×15 actually saved cells matching and 22 historical sheets preserved. SHA256 `0d92b99df979c524b61a89b11a7ea9cb1a3c2402ab4b59b1aa8f9a82ac24ef8a`, zero workbook lag; [publisher](https://github.com/OS4CSAPI/glaux-client/actions/runs/43104649463), [independent verifier](https://github.com/OS4CSAPI/glaux-client/actions/runs/43104863962). Original source inventory: 127 typed records and 26 precise holds, C239 registered headings 186 at least sampled/inline, five unread, one restricted. No DIM/Profile adoption, runtime certification or Chapter15 audit. **Next only G2-7S Chapter15 §§15–15.7 on separate owner Proceed.**

---

# SOSA G2-7R — Original C239 Chapter14 Run-Time Environment source review

**Original The Open Group SOSA C239 Edition1.1 (2023), §§14–14.5.3, PDF361–371; STOP before Chapter15.** [Stable typed source inventory](SOSA_G2_7R_Original_Source_Item_Coverage_11NOV2026.json): 38 numbered SHALL Rules, 18 Observations, two Permissions, one Recommendation, 15 headings, two original tables/five rows, six figure captions, 14 original configuration field/subfield descriptions and 26 exact source holds. Printed verification methods: 11 Inspection(I), 18 Demonstration(D), 9 Rules without printed method. No original figure pixel geometry, external FACE/OCI/DMTF or eight C239 native model files examined.

## Native original meaning

Three **alternative** software runtime profiles: FACE Operating System Segment (OSS), OCI container and DMTF Open Virtualization Format (OVF) virtual machine. A Procurable Unit with runtime must support at least one, while a module may contain multiple executables/containers/VMs. Nested runtimes are described but have explicitly **no encapsulation Rules**. FACE profile conformance references Edition3.1; OCI Runtime1.0.2 and OVF2.1.1 are format/engine versions, not OGC/CSAPI representation negotiation.

Common config **minimum content** is ProfileType (one), ImageLoad (per software item), Resources (core count/volatile-memory/network ports), conditional FileSystem (device/mount point/type) and conditional StartOrder for multiple executables. One file per RTE when multiple run on same PIC. Custom attributes/references to other files are Permissions; human-readable XML/JSON/YAML is merely a Recommendation; **no mandatory file format is specified**. These file fields are native software/platform configuration, not adopted DIM properties or reported device status.

Each runtime profile separately requires config validation, matching ProfileType, ImageLoad loading, resource adequacy, filesystem mounting and execution order (Demonstration D). Container/VM requires appropriate network access for intermodule SOSA interactions. Neither defines an authenticated CSAPI Command, reported process state or live service endpoint. Container orchestration, host-resource permissions and intra-module multi-container/VM communication remain explicitly unspecified; NIST security pointers are not audited. Shared config sections misrefer to §14.3.1 where common field definitions appear in §14.2; exact source locator held.

## 33 existing master donor comparisons

| Original master row | Fit | Source meaning and no-equivalence boundary |
|---|---|---|
| Described sensing System / arrangement | RELATED | Procurable Unit may host several RTE software profiles. **Boundary:** Not a mandatory whole-system DIM class or fixed topology |
| Network-visible participant | RELATED | Container and VM engines provide network access needed for module interactions. **Boundary:** Not discoverable CSAPI System or live IP participant |
| Network participation role and responsibilities | RELATED | Module software uses network interfaces for SOSA interactions. **Boundary:** Not online provider authority or tasking role |
| Network instance and connection context | RELATED | Runtime config describes network port number/type and access. **Boundary:** Not actual network session or IP address |
| Composition member exposure and source attribution | NO_ESTABLISHED | One module can comprise several software processes/containers. **Boundary:** No exposed component resources or observation attribution |
| Connection-specific network participation lifecycle | NO_ESTABLISHED | OCI engine manages container lifetime. **Boundary:** Not connection enrollment or client lifecycle |
| Declared component capability catalogue | RELATED | RTE ProfileType and Resources describe runtime capabilities. **Boundary:** Not an observed runtime-advertised CSAPI catalog |
| Declared property definition | RELATED | RTE config has software image and resource fields. **Boundary:** Not ObservedProperty or standardized digital property |
| Declared property mutability | RELATED | Clearly distinguished custom RTE config fields permitted. **Boundary:** Not remotely writable common property |
| Declared command interface | NO_ESTABLISHED | RTE internally loads and orders software execution. **Boundary:** Not authenticated CSAPI Command interface |
| Declared command parameter | NO_ESTABLISHED | ImageLoad identifies software to load. **Boundary:** Not issued command parameter schema |
| Command acknowledgement / reported outcome | NO_ESTABLISHED | Runtime verifies adequacy of processing resources. **Boundary:** No published command result/acknowledgement |
| Component capability and readiness report | RELATED | Configured resources and internal adequacy checks. **Boundary:** Not measured or publicly reported readiness |
| Component property-value report | NO_ESTABLISHED | Core/memory/ports are descriptive config values. **Boundary:** Not measured property-value Status |
| Required and recommended capability support | RELATED | Alternative RTE profiles required if RTE present; human-readable format recommended. **Boundary:** Not universal software Profile SHALL for all sensors |
| Negotiated message encoding and model version | RELATED | OCI runtime and DMTF OVF software packaging versions specified; RTE config format not standardized. **Boundary:** Not OGC representation/encoding negotiation |
| Component time basis and synchronization | NO_ESTABLISHED | ARINC653 time-window scheduling observations. **Boundary:** Not UTC clock lock or source timestamp |
| REVIEW HOLD — processing | RELATED | Processing cores RAM network ports and runtime adequacy are configured. **Boundary:** Not actual CPU utilization or observed processing status |
| REVIEW HOLD — reporting path | RELATED | Module software uses intermodule network interactions. **Boundary:** Not observed CSAPI DataStream or service path |
| REVIEW HOLD — control execution | NO_ESTABLISHED | RTE internally follows start-order to launch software. **Boundary:** Not authorized remotely issued CSAPI Command |
| REVIEW HOLD — service history | NO_ESTABLISHED | Source leaves container orchestration to integrator. **Boundary:** No historical runtime operation log |
| REVIEW HOLD — time / QA | NO_ESTABLISHED | Partition time-window sharing unaddressed. **Boundary:** No timing QA or UTC traceability |
| Component configuration version | NO_ESTABLISHED | Config minimum fields prescribed but no revision/version field. **Boundary:** Not current deployed configuration revision |
| Version of software running on the component | NO_ESTABLISHED | ImageLoad lists loadable software items. **Boundary:** Not package version of currently running software |
| Requested current component configuration message | NO_ESTABLISHED | RTE config file exists with profile and conditional file-system fields. **Boundary:** Not ISA/CSAPI read-configuration request |
| Network-interface IP addresses | NO_ESTABLISHED | Config counts/types of networking ports. **Boundary:** Not IP address assignments |
| Network-interface up/down state | NO_ESTABLISHED | Necessary network access for container required. **Boundary:** Not an observed network link state |
| Reported component operating condition | NO_ESTABLISHED | RTE resource sufficiency is verified internally. **Boundary:** Not current reported device condition |
| Service role and required command support | NO_ESTABLISHED | VM module software intercommunicates over SOSA interactions. **Boundary:** Not CSAPI service role or required commands |
| Certificate identity and trust context | NO_ESTABLISHED | Container host security and permissions explicitly unspecified. **Boundary:** Not verifiable trust identity or certificate fields |
| Request access-control metadata | NO_ESTABLISHED | Container/VM source references other security practice but no permission schema. **Boundary:** Not authenticated CSAPI API access-control metadata |
| Requested component active state | NO_ESTABLISHED | Internal runtime loads and starts executables. **Boundary:** Not externally requested component active-state action |
| Current command execution record | NO_ESTABLISHED | Virtual machine startup order is a source requirement. **Boundary:** No command state/activity record |

All comparisons cite stable Rule/Observation/Permission/Recommendation source IDs and do not authorize DIM adoption.

## Source holds

- SOSA-G2-7R-Q01: RTE alternatives are software execution profiles, not mandatory installed sensor chassis
- SOSA-G2-7R-Q02: Procurable Unit with RTE differs from SOSA module with many software artifacts
- SOSA-G2-7R-Q03: Nested runtime profile examples do not create encapsulation Rules
- SOSA-G2-7R-Q04: Shared minimum RTE configuration fields do not prescribe file serialization format
- SOSA-G2-7R-Q05: XML/JSON/YAML is only a recommended format, not SOSA JSON schema
- SOSA-G2-7R-Q06: Custom config attributes and nested config references are Permissions, not SHALLs
- SOSA-G2-7R-Q07: ProfileType/ImageLoad/Resources/FileSystem/StartOrder are source-specific conditional fields, not adopted DIM fields
- SOSA-G2-7R-Q08: FACE OSS Edition3.1 POSIX and ARINC653 originals not inspected
- SOSA-G2-7R-Q09: FACE Rule14.3.1-1 has no printed Conformance Method; no FACE certification claimed
- SOSA-G2-7R-Q10: Profile config paragraphs §14.3.3,14.4.3,14.5.3 reference §14.3.1 although shared fields appear §14.2
- SOSA-G2-7R-Q11: OCI Runtime1.0.2 original normative specification not independently read
- SOSA-G2-7R-Q12: OCI Image spec described but source only mandates run-time bundles; do not invent image build
- SOSA-G2-7R-Q13: DMTF OVF2.1.1 original spec unread and no installed virtual appliances witnessed
- SOSA-G2-7R-Q14: Container and VM network access not real CSAPI System discovery or published services
- SOSA-G2-7R-Q15: Intra-module multiple container/VM communication not specified
- SOSA-G2-7R-Q16: Container orchestrator and multi-container lifecycle management unspecified
- SOSA-G2-7R-Q17: Container host-resource security/permissions expressly not specified
- SOSA-G2-7R-Q18: NIST SP800-190, NIST SP800-125 and SRG/STIG pointers do not prove full original source coverage
- SOSA-G2-7R-Q19: ARINC653 partition scheduling time-window sharing unspecified and Observational
- SOSA-G2-7R-Q20: Future filesystem/blockIO/RDMA access not present mandatory runtime guarantee
- SOSA-G2-7R-Q21: Three runtime-specific six Demonstration(D) steps are internal operations not client Command semantics
- SOSA-G2-7R-Q22: No actual CPU/memory/network port counts, utilization or software image/version from four source cases
- SOSA-G2-7R-Q23: Six original RTE figures' pixel geometry not independently examined
- SOSA-G2-7R-Q24: Eight original C239 DSDM/IDL/OpenAPI companions, later S251, restricted AppendixC remain held
- SOSA-G2-7R-Q25: Chapter15 intermodule interaction definitions remain unread in this packet
- SOSA-G2-7R-Q26: No adopted DIM/Profile class, field, cardinality, SHALL or independent runtime conformance

**Original source coverage:** 186 of 192 registered headings at least sampled/inline-reviewed, five unread and one restricted; ten previously UNREAD Chapter14 registered headings now source-reviewed. External original specs and exact figures remain unexamined; no donor closeout. **Publication gate:** update canonical JSON, two CSV mirrors, two GitHub-readable comparisons and SAME original editable 26-sheet Excel; independently inspect saved cells and source/case preservation before completion. **NEXT owner Proceed**: G2-7S original Chapter15 §§15–15.7, stop before Appendix A.
