# Step 02 — Starting Evidence and Coverage Audit

**5 November 2026 · New Donor Concept → DIM Crosswalk plan, original Step 02 ONLY · AUDIT COMPLETE / NO NEW DONOR MAPPINGS · STEP 03 NEXT**

This is the **starting-data and evidence-standing audit** required by the [owner-directed crosswalk plan](PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md), not a new concept-research iteration. It freezes exactly what we have before building a larger spreadsheet. **No approved sample table, model, donor terminology, original source register, UML, CSAPI Profile, application, server, or deployment was changed.**

**Plain-language result:** The accepted horizontal comparison is **structurally consistent** across its saved JSON, flat CSV and cell evidence ledger. But its current “SOURCE-VERIFIED SAMPLE” label is stronger than the proof recorded for each individual correspondence. Its 51 cells have prior source citations and proposed alignment classifications; they are **not 51 independently reverified, final normative equivalences**. We should preserve the useful layout while making original-source verification states explicit before expanding.

**Machine-readable frozen inventory:** [Step02_Starting_Data_Inventory_v0.1_05NOV2026.json](Step02_Starting_Data_Inventory_v0.1_05NOV2026.json). This records counts, nine review-status discrepancies, exact source file paths, original Git blob SHAs and the research branch head at the start of Step 02 (`92f85060703b2953c63ae3df163678ab5028489a`). These are **baseline provenance**, not an instruction to revert subsequent commits.

## 1. Exactly what the owner accepted — and what was actually counted

The owner explicitly approved the **format/template**, **not** every proposed row, donor correspondence, category or final donor ordering. The controlling artifact is the [GitHub-readable approved 5 November sample](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.md), with [structured JSON](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.json), [flat CSV](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.csv) and [evidence ledger](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026_Evidence.csv).

| Actual attribute inspected | Verified baseline | Qualification |
| --- | --- | --- |
| Donor columns | **7** | Donors fixed in a left→right sample order; **DIM rightmost is a separate 8th column**. |
| Candidate DIM information-element rows | **22** | Candidate wordings only, not 22 finalized DIM classes/attributes. |
| Full-width group-divider rows | **5** | Identity (4 rows); system/equipment (6); channels/observations (5); configuration/control (5); source/provenance (2). |
| Populated donor→DIM cells | **51** | 51 **recorded mapping proposals** across 22 rows, not original clause-verification events. |
| Mapping classifications | **16 DIRECT; 27 PARTIAL; 7 RELATED; 1 CONDITIONAL** | Original project research ratings. A “DIRECT” note is not a published normative equivalence axiom. |
| Sample donor rows with no established counterpart | **2** | `Source-qualified assertion (proposed DIM)` and `Original event and derived digital representation (proposed DIM)`. Do not treat blanks as proof no other donor supports these meanings. |
| Rows with one populated donor cell | **2** | Unique or specialized concepts are retained rather than force-filled horizontally. |
| Sample CSV to source JSON | **PASS — 22 element rows + 5 group headings; zero cell differences** | Tested the actual saved strings, including the sample's `≈` notation. |
| Evidence rows to source JSON | **PASS — 51 matches, zero orphans/mismatched locator/classification, zero missing evidence records** | Structural/reference consistency only. No fresh publisher-source reading in this step. |
| Evidence source locator entries | **51 nonempty; 44 distinct locator strings** | Some are generic section references, not atomically verified each original field; several entries reuse one clause. |
| Evidence source links | **51 nonempty HTTPS pointers** | Link presence is **not** semantic accuracy, publisher authentication, or current link availability. |
| Stable user-facing row IDs, edition-per-cell and verification status | **Not yet available in the approved sample** | Step03 should define source/row IDs and states **outside the visible main table**. |

**Provisional sample column order, with number of populated rows (including weak/related matches):**

| From left to right | Donor displayed | Rows populated | Prior evidence qualification |
| --- | --- | ---: | --- |
| 1 | IEEE 1451 public 2024-linked evidence | 5 | Full licensed normative IEEE 1451.0-2024 clause set **not audited**; four sampled links are third-party Playground technical explanations. |
| 2 | OGC Observations, Measurements and Samples 3.0 | 5 | Existing original OMS review is more developed, but original source/edition fit must still be confirmed for **each cell**. |
| 3 | OPC UA Devices | 6 | Device and nameplate review exists; does **not** automatically include PA-DIM content. |
| 4 | W3C SOSA/SSN | 6 | 2017 Recommendation used for sample; distinct from 2026 draft **and** The Open Group SOSA. |
| 5 | SensorML 3.0 | 8 | Process, description and component ideas may be related without having identical semantics to a particular physical unit. |
| 6 | SAPIENT v2 | 9 | Mode, registration and Task/TaskAck have useful selected original definitions and important target/scope caveats. |
| 7 | CSAPI Parts 1–2 | 12 | **One sample column combines two distinct OGC Parts**, a later roster decision; Part1/Part2 native resources/requirements must remain distinct. |
| 8 | **Proposed DIM** | **22 proposed labels** | **Always final rightmost**, not ranked; names/definitions remain open to revision. |

**Important:** This is **NOT** a quality, independence or standards-authority ranking. The sample counts `DIRECT`, `PARTIAL`, `RELATED` and `CONDITIONAL` cells together as merely “populated.” A rank suitable for the owner's intended least-used→most-used final layout must emerge only **after source-aware alignment**, not from this sample.

## 2. What the 182-source inventory really establishes

The [original 182-artifact accountability register](../Donor_Alignment/03_Source_Accountability_Register.csv) was read and counted at its real source fields. Its derived [lineage/accountability CSV](../Donor_Alignment/05_Donor_to_R24_Artifact_Traceability_04NOV2026.csv) was independently joined to it by artifact ID, assignment and individual assessment status. **182/182 IDs matched; zero lineage/status discrepancies** at those columns.

| Source-inventory characteristic | Verified count | What it means |
| --- | ---: | --- |
| Individually catalogued artifacts | **182** | Titles/citations and metadata, **not** 182 independent standards or 182 independently validated model mappings. |
| Individual concept-review status `NOT_ASSESSED` | **182** | Status of **this specific artifact register's individual review process**. It does **not** prove no original-source reading ever occurred elsewhere in the project. |
| Nonblank lineage-category labels | **30 distinct labels** | Historical classification buckets, **not** necessarily 30 final donor columns. |
| Artifact rows without an assigned lineage label | **27** | May include real relevant cross-cutting material such as **SWE Common 3.0** (artifact 14), units/quantities, Web Linking RFCs and governance; not “irrelevant” by default. |
| Historical source roles: core structural donor | **88** | Source-role label, not source verification. |
| Historical source roles: cross-cutting structural donor | **52** | Source-role label, not source verification. |
| Historical source roles: specialization donor | **15** | Source-role label, not source verification. |
| Historical source roles: non-structural | **27** | Source-role label, **not identical by definition** to the 27 unassigned-lineage rows. |

The [older donor-contributions comparison](../Concept_Donor_Comparison/Donor_Contributions.md) has **13 named lineages with a developed family-level comparison** and **17 preliminary/deferred lineage leads**, which is compatible with **182/182 individual records marked `NOT_ASSESSED`**: they represent **different granularity and review purposes**. One family-level report may analyze some actual original source terms and still not establish an individual complete concept review of every historical artifact in that family. Both facts must remain visible to prevent false “100% coverage.”

**The 13 developed lineage labels** in the old comparison are Asset Administration Shell, IEEE 1451 / ISO 2145x, Integrated Sensor Architecture, OMS 3.0, OGC API – Connected Systems Parts 1–2, OPC UA Devices/PA-DIM (with PA-DIM separately incomplete), OSUS-R, SAPIENT v2, SAREF, SensorML 3.0, The Open Group SOSA, W3C/OGC SOSA/SSN and W3C Web of Things. They have **varying source depth and edition/semantics caveats**, not a common verification grade.

**The 17 preliminary/deferred leads** are Bosch BME280, I-ADOPT, IETF energy management, IETF hardware, IETF interface/topology, ISO/IEC 29182 sensor networks, OMA Lightweight M2M, Matter, MIMOSA, MIP/JC3IEDM, NIEM, NISTIR 8259A, radiation instrumentation, Redfish/CIM, SWEET, historical UGS operational cases and W3C PROV. They are **leads to assess**, not proof a source has no matching or useful concept. The 30 historical lineage labels and these 13+17 review rows are **not automatically identical as column candidates**: some standards are bundled, some companion sources live outside a headline category and source-type methods may not be donor columns.

## 3. Evidence-standing discrepancies and repairs to make later — DO NOT modify the sample during Step02

The audit found **no data-integrity defects** among the three sample representations, but it identified **nine evidence interpretation/coverage issues**. These are not automatically “errors in the original standards,” and Step02 has made **no source corrections**. They must inform the next steps rather than be silently painted green.

| ID | What the files say / what we found | Proper standing and next bounded treatment |
| --- | --- | --- |
| **D02-01** | Sample JSON calls itself `SOURCE-VERIFIED SAMPLE / NOT ADOPTED`. | Too strong without individual verification flags. **Re-label the *review standing*, not rewrite approved example facts**: all 51 cells are `prior source-claim recorded; independently source-checked status unestablished in Step02`. |
| **D02-02** | The evidence CSV has 51 locators and URLs, **no separate per-cell original-source verification grade**. | Step03 must define `ORIGINAL_CHECKED / PRIOR_SOURCE_EXTRACT_ONLY / SOURCE_UNAVAILABLE / NEEDS_REVIEW` fields with clause/edition and reviewed-on marker; don't infer positive status from a URL. |
| **D02-03** | A `DIRECT` cell is a **project rating**, not an explicit assertion of equivalence by the donor publisher. Sample donor ordering counts all relation types equally. | Step03 needs a precise relation rubric; later final order must distinguish supported direct from partial/related, with ties and edition scopes. |
| **D02-04** | 13 developed family reviews exist, yet 182 artifact-level flags are `NOT_ASSESSED`. | Distinct bookkeeping scales, not proof prior work is absent. Step02 freezes both; Step04 must separate actual edition/standard columns without assuming full corpus coverage. |
| **D02-05** | 30 historical lineage categories are assigned and 27 artifacts have none. | “Unassigned” is **not** excluded. Later roster/coverage must inspect cross-cutting standards and methods on their merits. |
| **D02-06** | The sample has no **stable DIM row ID**, donor element kind, source edition **per mapping cell**, or a recorded review decision independent of row position. | Step03 defines a **hidden/evidence-ledger schema**, keeping the user's rightmost-DIM visual table intact. No R24 codes need appear in the main layout. |
| **D02-07** | Two DIM proposal rows have all seven donor cells empty. | Do not declare them unsupported by the whole 182 corpus. W3C PROV and other **unsampled** sources might contribute meaning. Open candidate standing. |
| **D02-08** | Four IEEE evidence URLs in the sample point to `iml.ubi.pt` public Playground technical material; one to official IEEE scope page. | Public technical research matters, but external examples **are not the IEEE publisher's full original normative clauses**. Step03 status must distinguish this, then Step14 review accessible original/source-backed evidence without inventing licensed text. |
| **D02-09** | The CSAPI donor sample combines OGC Parts 1–2; OPC UA Devices and PA-DIM are combined in historical family accounting but not sample; W3C SOSA differs from Open Group SOSA. | Step04 should propose distinct columns where technical semantics warrant it; do not assume “family” = one actual standard. Final donor order remains **provisional**. |

**URL observation, not a live-link test:** 51 source-ledger pointers use HTTPS and have nonempty locator text. The host labels visible in the saved strings are `docs.ogc.org` (25 cells), `www.bsigroup.com` (9), `reference.opcfoundation.org` (6), `www.w3.org` (6), `iml.ubi.pt` (4) and `standards.ieee.org` (1). This is **a source-label inventory** only. A host name, a valid-looking URL or a generic section locator is not evidence that every line was read or that the URL is currently reachable. **No live original-PDF/standards review was performed by Step02.**

## 4. Frozen artifact identities, reproducibility and scope of this audit

[Machine-readable snapshot](Step02_Starting_Data_Inventory_v0.1_05NOV2026.json) pins the original **Git blob SHAs** of the approved Markdown sample, JSON, CSV, 51-cell ledger, original and derived 182-register files, donor-contributions review and donor-term review. The full **start-of-Step02** research branch HEAD was `92f85060703b2953c63ae3df163678ab5028489a`. Those references enable another chat to fetch the exact starting bytes, even after this plan/status/PITON advances.

**Audit operations actually performed:** Read the eight original GitHub files on `research/dim-profile-v2`; independently parsed **quoted CSV fields**, including citations with commas; counted 182 original and derived artifact rows; joined them on actual artifact IDs and compared source lineage/status; extracted all 22 JSON proposed elements/5 dividers and 51 populated donor cells; cross-matched the flat CSV literal per-cell values; cross-matched every evidence-ledger cell, mapping classification and recorded locator to the structured JSON; checked that all 51 saved original-source links were nonempty HTTPS strings and grouped their named hosts. The structural audit found **zero missing/mismatched sample cells and zero 182-register join discrepancies** at the checked fields.

**Not performed:** Fresh reading of the original OGC/IEEE/ISA/SAPIENT/AAS/SOSA/OPC normative documents; validating the correctness of individual source mappings; web live-URL availability; rewriting source assertions; deciding final donor eligibility or least→most contribution order; inventing additional DIM concepts, classes or cardinalities; creating a new master XLSX; rendering/editing UML; modifying application/server or deploying anything. The source documents themselves, not any prior AI summary, will control original clause review during the later donor steps.

**Quality of result:** We now have a usable, **explicitly qualified frozen baseline** and discrepancy register. No measured positive original-source equivalence tests were newly added. We have **earned the ability to build the next record/rubric design without guessing which material is actually reviewed**; we have not earned declaring the original donor-to-DIM crosswalk complete.

## 5. Next single iteration

**NEXT owner “proceed”: [Plan Step 03](PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md#phase-a--establish-controls-before-touching-the-mapping-0104) ONLY — define a concrete, versioned **row/cell evidence record schema and interpretation decision rubric**, including a worked positive and rejected equivalence using existing source facts.** This must preserve the donor-columns/DIM-rightmost appearance, define source-edition/locator and `PRIOR_SOURCE_EXTRACT_ONLY` vs `ORIGINAL_CHECKED` explicitly, and not begin a donor mapping campaign or relabel existing primary standards as checked. Owner can review it without learning R24 project codes.

**No new rows or donor correspondences are authorized in this Step02 audit.**
