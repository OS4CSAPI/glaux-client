# ISA Controller Requirements 6.0r4 — Delivery 18 source review (first area)

**8 November 2026 · ISA accelerated delivery 18 · SOURCE TEXT REVIEW COMPLETE, integration/publication reconciliation pending.** This record is source-grounded in the original project-provided *ISA Controller Requirements*, release 6.0 revision 4, 31 October 2023, Distribution Statement A, Project Files ID `file_00000000e00082109d88d0119f744880`. Reviewed the indexed original PDF text on PDF pages **8–42 of 74** (printed pages 1–35), including the two terminology/document-structure tables. The page-image rendering route was unavailable: do **not** claim the pages were visually inspected. This is a requirements/documentary review, not a running Controller conformance test.

## Exact scope and census

The **20 registered blocks** assigned to delivery18 are `CNTR-1.0`, `CNTR-1.1`, `CNTR-1.2`, `CNTR-1.3`, `CNTR-2.0`, `CNTR-3.0`, `CNTR-4.0`, `CNTR-5.0`, and `CNTR-5.1` through `CNTR-5.12`. All 20 have been read. Their source headings, explanatory prose, normative definitions, parent/child references and notes were examined. There are **108 distinct native requirement definitions: 13 high-level, 33 mid-level, 62 low-level**. The actual normative sentences contain **107 shall, 0 should, and 1 may** (CMSV-L-0019, begin application exchange after Handshake Complete). Do not count referenced child-list headings as additional definitions.

| Source section | Original printed pages (PDF pages) | Native requirement inventory |
| --- | --- | --- |
| 1.0–1.3, 2.0, 3.0 | 1–7 (8–14) | Explanatory scope, terminology, document structure and requirement-level/modality rules; no native shall definitions |
| 4.0 Deployment | 8–9 (15–16) | DPLY-H-0001; DPLY-M-0001; DPLY-L-0001–0004 = **6** |
| 5.1 Controller Discovery | 10–11 (17–18) | CMSV-H-0001; M-0001–0003; L-0001–0004 = **8** |
| 5.2 Connection Creation | 12–14 (19–21) | CMSV-H-0002; M-0004–0006; L-0005–0013 = **13** |
| 5.3 Format Establishment | 15–16 (22–23) | CMSV-H-0003; M-0007; L-0014–0020 = **9** |
| 5.4 Registration | 17–19 (24–26) | CMSV-H-0004; M-0008–0012; L-0021–0027 = **13** |
| 5.5 Configuration | 20–22 (27–29) | CMSV-H-0005; M-0013–0016; L-0028, L-0029, L-0032, L-0033 = **9** |
| 5.6 Status Reporting | 22–23 (29–30) | CMSV-H-0006; M-0017–0018; L-0034–0035 = **5** |
| 5.7 Service Recommendation | 23–25 (30–32) | CMSV-H-0007; M-0019–0020; L-0037–0040 = **7** |
| 5.8 Command Brokering | 25–27 (32–34) | CMSV-H-0008; M-0021–0023; L-0041–0043 = **7** |
| 5.9 Observation Handling | 27 (34) | CMSV-H-0009; M-0024; L-0044 = **3** |
| 5.10 Availability Monitoring | 27–30 (34–37) | CMSV-H-0010; M-0025–0027; L-0045–0050 = **10** |
| 5.11 Deregistration | 30–33 (37–40) | CMSV-H-0011; M-0028–0030; L-0030, L-0031, L-0036, L-0051–0056 = **13** |
| 5.12 Connection Termination | 34–35 (41–42) | CMSV-H-0012; M-0031–0032; L-0057–0058 = **5** |

The source's total is 6 DPLY + 102 CMSV = 108 distinct definitions. No requirements from §6 onward were credited to this iteration. **Eight registered Controller blocks remain:** CNTR-6.0, 7.0, 7.1, 7.2, 7.3, 8.0, AppendixA, AppendixB, all for delivery19.

## Source findings and bounded crosswalk implications

**Controller hosting versus whole-System hardware.** §1.2 defines one Controller as the collection of one instance of each core service. §4.0 requires Communication, Live Data and Authorization services provided by the Controller on a single computing-platform instance. This does not prove there is only one Controller in an ISA network, that a Controller equals a physical chassis, or that the source describes installed equipment inventory.

**Discovery, connections and presentation.** §5.1 uses Zeroconf, a configurable advertisement frequency, and literally names `_isa._tcp`, `_isa-mockets._udp` and `_isa-sctp._udp`. §5.2 separately requires secure TCP, SCTP and Mockets listeners and connection handlers using certificates. Preserve these Controller 6.0r4 statements separately from narrower or differently scoped prior ICD 6.0r5 text; do not silently unify transport obligations or invent an implementation. §5.3 selects a supported preferred IPL presentation format from a sorted offered list; the 0x03 error names supported formats and 0x04 concerns premature application data. CMSV-L-0019 explicitly **may** begin data exchange after sending Handshake Complete. The Sensor CE IPL3 note is a source example/context, not an observed implementation.

**Registration identity, authorization and clocks.** §5.4 requires an explicit match of the originating Registration REQUEST ADD UCI against certificate UCI, ERROR for missing/mismatched UCI and for denied authorization, and ADDED for successfully authorized registration. The Controller response is due within 30 seconds after the request. Authentication/identity matching, permission to register, registration outcome and TLS establishment must remain distinct. §5.5 has a high-/mid-level trigger based on receiving the first Config from a registered component, whereas low-level CMSV-L-0028/L-0029 tie initial Config to sending ADDED and a separate 30-second bound. §5.6 likewise ties mid-level initial Status to receiving a first Status while low-level L-0034/L-0035 tie it to the Controller's initial Config. Record both native wordings; neither is a license to invent one universal lifecycle timestamp. Later Config and Status updates carry only changes in their respective domains.

**Recommendation versus command execution.** §5.7 makes provider choice conditional on Config declaring the Set ISA Live Data Service or Set ISA Authorization Service capability, uses a best-available-provider concept without a specified algorithm, and sends Request with the chosen UCI. The source spells the command names with 'ISA'; preserve the DMS catalogue's distinct literal names without silently renaming. §5.8 explicitly distinguishes authorization checking, PERMISSION DENIED Response, and forwarding an authorized Request to its cited performer. None proves a command executed, succeeded or affected hardware.

**Events, availability and removal.** §5.9 forwards a registered component's Event to the Controller-associated Live Data Service, which is neither a new original Observation nor proof of subscriber receipt. §5.10 uses a configurable multiplier of the component's Maximum Status Interval since last Status to decide non-responsiveness; Controller sends NON RESPONSIVE or REVIVED Registration messages within 500 ms after determination and generates corresponding DEVICE notifications. These are network-presence assertions, not hardware diagnoses. §5.11 includes forced deregistration on missing Config or initial Status (30-second conditions), missing prompted Status (configurable bound), and 500 ms to send REMOVED once the Controller determines removal is required. Announced components still marked available receive corresponding DEVICE REMOVED notifications on announcer deregistration or link loss; this does not prove their physical removal. §5.12 requires Controller-side forced connection termination/initiation following REMOVED; earlier Component Requirements' should/may socket rule applies to a differently stated actor and condition.

**Local source inconsistencies (no new primary ISA question or added step).** §1.2 expands CCD as *Component Capability Description* versus earlier ISA *Declaration* wording. CMSV-L-0018 lacks its own printed parent-requirements list, although M-0007 names it as a child. CMSV-H-0011 says *Parent Requirements* before listing its M-0028–0030 children. Preserve these literal discrepancies. The 5.5/5.6 trigger wording and 5.7 command-name variants are likewise local edition/source qualifications, not repaired or silently equated.

## Integration and next action

Source-first review alone does not adopt model classes. Map these findings to **existing** candidate rows for Controller/network context, connection presentation, certificate trust, Registration, Config, Status, participation lifecycle, service choice, brokered Request/Response, Administrative availability notices and visible-member exposure. Do not add a row for each SHALL. The baseline working master remains 329 information/review rows, all480 DMS entries reviewed (474 supported and six source questions), with the old 253-row/226-primary workbook snapshot. Original 31 correspondence targets and 25 earlier findings are reserved for the preplanned final source audit.

**Publication closeout (8 November 2026):** Following the source-first checkpoint, this review was integrated into the canonical [structured master](Master_Donor_Concept_to_DIM_Crosswalk.json), [readable comparison](Master_Donor_Concept_to_DIM_Crosswalk.md), [cumulative evidence](ISA_Service_and_Context_Evidence_08NOV2026.json), [coverage register](ISA_Coverage_Register_07NOV2026.json), [exact status](ISA_Correction_Status_07NOV2026.json), [PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) and [execution plan](PLAN_ISA_Coverage_Correction_07NOV2026.md). Source review/integration are not DIM adoption, actual runtime conformance or a refreshed XLSX. The next separate owner “Proceed” executes **Delivery 19 only**.
