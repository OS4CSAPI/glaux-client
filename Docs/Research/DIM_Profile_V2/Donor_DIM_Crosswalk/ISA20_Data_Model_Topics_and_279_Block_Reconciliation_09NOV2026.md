# ISA Data Model Topics 6.0r2 — original-source review and 279-block reconciliation (accelerated Delivery 20)

**9 November 2026 · Original ISA Step 11, accelerated Delivery 20 · original 2023 source material only.** This records the 23 registered sections of the original *ISA Data Model Topics*, release 6.0 revision 2, 31 October 2023 (Distribution Statement A; original Project PDF `file_000000006b5881f4988dfb57ac11965c`, 22 PDF pages, printed pp.1–15 after seven front-matter pages), plus bounded 2015 historical access and all-279 registered block accounting. The [structured 23-block source evidence](ISA20_Data_Model_Topics_Original_Source_Evidence_09NOV2026.json) contains every source ID, section, page, plain meaning and must-not-imply condition. **Indexed text for all22 pages reviewed; selected figure/table page images visually checked (PDF pp.9,13,14,19,21).** No tests, actual media retrieval, original PDF hash, independent issuer attestation, hardware control or every-page visual audit is claimed.

## 1. Edition and directly inspected source features

Revision History Table1 on PDF p.2 says revision2 updates **Resource Descriptor parameter usage** and the **Event Update example**. Source sections must be read under this edition; examples are not forward/backward normative contracts. The source contains Table2's illustrated change-method matrix, Table3's original/update/augmented sample, Figures1–3 distinguishing tracking versus Event correction, Figures4–7 Resource Descriptor samples, and Figure8 Help Desk QR/contact context. Parent headings and children overlap in document span, but are **23 distinct registered coverage records, not23 extra independent DMS classes or requirement definitions**.

### Property mutability (§§1.0–1.2, PDF pp.8–10)

**PERMANENT** means not expected to change within a component operational cycle; the source *should* guidance to deregister/rejoin before a necessary change is not transformed into a universal mandatory step. **READ WRITE** indicates a value the component needs but cannot determine independently, supplied by **Set Property**. **READ ONLY** may change as real state changes and can be modified via a separate supported Change/Adjust command, **not Set Property**. Source Table2 visually shows: PERMANENT permits neither method; READ WRITE permits Set Property only; READ ONLY permits Change/Adjust only. Deprecated **WRITE ONLY** is described as being removed in a future version, not a standard mandatory fourth active mode.

In the source imager example, externally setting Position can allow the imager subsequently to slew and change Orientation, while the supplied Position itself remains unchanged. **Direct assignment of a READ WRITE value must not be equated with physical movement**, nor should the possibility of indirect movement be denied. This matters to the existing mutability, declared property, Set Property and Status candidate rows.

### Event Updates and observed-entity tracks (§§2.0–2.6.2, PDF pp.11–14)

An originally distributed Event is described as an immutable record, and later updates **augment its consumer-interpreted information**, not rewrite an original message at every recipient. The original Event identity normally combines **Time, ID and Source**; Table3's ID and Ref are explicitly shorthand. A later Event supplying **Event Reference** replaces **only supplied observables**, retaining unmentioned original values. The amended observation retains original Event time; new Event Update time is the *update* time. For multiple updates, the guide directs ordering updates by time first. Figure2 on PDF p.14 visually retains original time and combines later information.

**Recall** (erroneous observation; string explanation; advise disregard) and **Resolve** (previously accurate event no longer requiring attention) are different. Neither creates proof of deletion or uniform consumer handling. **BSO** identifies the observed battlefield entity for track correlation among multiple Events, while **Event Reference** corrects a specific prior Event; they may coexist when adding or correcting an earlier BSO. Figure1 on PDF p.13 contrasts track versus correction, and Figure3 on p.14 depicts Recall without deleting a published original. Do not transform BSO into the ISA component's UCI or a source-authenticity credential.

### Resource Descriptors (§§3.0–3.4.4, PDF pp.15–21)

The guide describes a **URL-addressed external resource**, with Resource Type **primary/secondary** analogous to an IANA media type and optional title, created/modified fields and named metadata. Its examples include an image, a video stream, a text XML file and custom-protocol service. The type analogy and custom examples must not be inflated into a claim of IANA registration, safe/available URL, authenticated issuer or universal protocol support.

General component resources are **typically** reported through Status **Resources**; an observation's related resources through Event **Media**; custom capability fields may carry descriptors as well. Linked raw sensor files, KML and vCard or a custom native command interface are use cases, not automatically executed sensing acts, verified original observations or new CSAPI Profile requirements. A URL is a pointer to possible retrieval, not evidence that its content is currently running or has been fetched.

The §3.3.1 **recommended** video Resource Type parameters list Bitrate (Mbpsec), Bitrate Control, Codecs (String list), Container, Compression Level, Frame Rate (Hertz), Width/Height (Integer pixels), Scan Type and Audio (Boolean), including a specific omitted-versus-`Uncompressed` Compression Level note. They are **not mandatory across all video streams**. Figure5 and its Java API example show sample **15,30,h.264/aac,1920×1080,PROGRESSIVE,audio=true**, not live telemetry, a real stream or installed configuration. Figures4,6,7 use localhost/mock custom examples; those endpoints are not validated or deployed.

### Further Resources (§4.0, PDF p.22)

Help Desk text and QR code are support/contact material, **not additional 2023 Domain Information Model source fields, software implementation requirements or evidence of network performance**.

## 2. Exactly what the 23 registered sections add

| Registered blocks | Count | Source result | Master consequence |
| --- | ---: | --- | --- |
| `TOPICS-1.0` to `1.2` | 3 | Operational mutability and Table2 direct-value/physical-action distinction | Existing mutability/property/Set Property candidate qualifications |
| `TOPICS-2.0` to `2.6.2` | 9 | Original Event, partial Update, timing, Recall, Resolve and BSO correlation | Existing Event/observables/reference/track candidates qualified |
| `TOPICS-3.0` to `3.4.4` | 10 | Resource Descriptor roles, recommended video parameters, four illustrative examples | Existing Resources/Media/Status candidate qualifications |
| `TOPICS-4.0` | 1 | Further Resources/Help Desk only | Context, no model claim |
| **Total** | **23** | **All 23 inspected at original indexed-text scope** | **No added master row, DMS catalogue definition, displayed comparison-cell edit or model adoption** |

The [structured source evidence](ISA20_Data_Model_Topics_Original_Source_Evidence_09NOV2026.json) lists the **15 source-qualified existing candidates** and the ten local boundary notes. Source evidence is additive: all prior DMS/requirements, DQL, ICD, Component/Controller, original case and donor statements remain previously credited at their earlier checkpoints. New source review does not silently resolve earlier source-specific questions.

## 3. Historical 2015 SPIE source — bounded access result

The separately registered Moulton et al. paper, *Open architecture design and approach for the Integrated Sensor Architecture (ISA)* (SPIE Vol.9479, 94790C, 2015, DOI [10.1117/12.2177842](https://doi.org/10.1117/12.2177842)) has a verifiable public [SciXplorer abstract and bibliographic record](https://scixplorer.org/abs/2015SPIE.9479E..0CM/abstract). The [ResearchGate record](https://www.researchgate.net/publication/300883836_Open_architecture_design_and_approach_for_the_Integrated_Sensor_Architecture_ISA) did not provide full text in the bounded check. The abstract supports only historical design motivation and broad SOA/open-architecture emphasis; the **full six-page source was not read**. Keep `SRC-ACCESS-01` **HISTORICAL_ABSTRACT_ONLY_FULL_TEXT_NOT_ACCESSED**, not COMPLETE. It is historical context, **not controlling authority for 2023 DMS/Controller definitions**, and it does not block the current 2023 source inventory.

## 4. All 279 registered source blocks — bounded reconciliation

The actual coverage register partitions **279 distinct records** as follows: **226** previously fully reviewed companion/requirement source blocks (SDD27, ICD39, CMPT34, CNTR28, DQL31, INTRO18, WHITE30, CERT11, IPL3 8); **23** new TOPICS original-source sections reviewed in Delivery20; **29** DMS chapter/heading registers reconciled **to the already completed 480 individual DMS native entries and prior source reviews** (not falsely credited as 29 fresh independent parent-section readings); and **one** PAPER2015 bibliographic/source-access item held for missing full text. Thus **249 fully reviewed companion/requirements/TOPICS blocks +29 accounted DMS heading/section records +one bounded historical access hold =279**, zero unassigned or duplicate IDs.

This reconciles the **register population and original assigned obligations**, not the **31 original source-to-crosswalk targets or 25 prior mapping findings**. Those remain precisely **4/31 and1/25** reconciled, with **six** local primary source-definition questions open for Delivery21 source-first audit. No 2015 missing-text excuse is imported into the 2023 complete catalogue. Existing DMS catalogue outcomes remain **480/480 reviewed =474 supported and six questions**. All 329 master information/review rows, 58 donor evidence records and 73 case source statements are preserved.

## 5. Preservation, source fidelity and exact next scope

No permission is inferred to expand other donors, choose an ISA chassis, adopt DIM classes, modify the CSAPI Profile, deploy software, issue a physical command, fabricate a completed observation, or publish a refreshed Excel workbook. The canonical **26-sheet XLSX is still the earlier253-row/226-primary integration snapshot** and is scheduled for Delivery22, after source-first correspondence audit.

**Next authorized owner “Proceed” is accelerated Delivery21 only:** re-evaluate the original **31** row/case correspondence targets, **25** earlier findings and **six** local ISA questions against original source/evidence, recording actual holds/revisions. **Delivery22** remains consolidated validation, full XLSX refresh, lessons and verified GitHub closeout. No new research mini-series or unscheduled independent paper-access chase is authorized.
