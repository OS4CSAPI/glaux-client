# ISA-03B — Ownership, versions and support

**7 November 2026 · Six of six assigned source reviews COMPLETE and integrated.** Next: ISA-03C only.

[Current workbook](ISA_Correction_Review_ISA03B_07NOV2026.xlsx) · [Full comparison](ISA_Correction_Review_ISA03B_07NOV2026.md) · [Exact evidence](ISA03B_Ownership_Versions_Support_Evidence_07NOV2026.json) · [Publication record](ISA03B_Publication_Record_07NOV2026.json) · [PITON](PITON_ISA_Coverage_Correction_07NOV2026.md).

## Source decisions

All six native properties were read in the original ISA Data Model Specification, Release 6.0 revision 12, dated 31 October 2023, §3.1, printed pp.14–17 / PDF pp.29–32. The body markings establish five Accepted extensions and one core entry.

| ISA source term | Source type / structure | Standing | Specific candidate information element |
|---|---|---|---|
| Owner | POC / List | ACCEPTED_EXTENSION | Component owner contact information |
| Parameter Version | String / Single Value | ACCEPTED_EXTENSION | Version of component configuration parameters not exposed through ISA |
| Program of Record | POC / List | ACCEPTED_EXTENSION | Component program-of-record contact information |
| Software Version | String / Single Value | ACCEPTED_EXTENSION | Version of software running on the component |
| Specification Version | String / Single Value | CORE | Reported ISA specification version of the component |
| Support | POC / List | ACCEPTED_EXTENSION | Non-maintenance support contact information |

The source supports each deliberately narrow candidate directly. Candidate-row fit is a source comparison, not owner adoption. **No new source-definition questions arose** and no installed case values were invented.

## Meanings that must remain separate

Owner identifies the owner of the specific component, represented through contact information; it is not an authorization or permission role. Program of Record also uses a POC list and is therefore not automatically a programme identifier or procurement-status field. Support explicitly covers **non-maintenance** help and remains separate from Maintenance and Manufacturer POC.

Parameter Version identifies hardware/software configuration parameters **not accessible via ISA**. The version field itself is available; the underlying values are not thereby exposed, and “traditionally do not change during runtime” is not an absolute immutability requirement. Software Version concerns software running on the component. Specification Version states the ISA version with which the component complies; the declaration does not independently prove tested conformance.

## Supporting definitions and provenance

POC (Accepted extension), DMS §8.3 p.106 / PDF p.121, was inspected in both its original text and page image. It has required organization and optional name, phone, email and Resource Descriptor details; the source says this nonstandard composite must be constructed using Custom Types. Optional details follow the source vCard 3.0/text-vcard description. None of these fields creates a claim about a real contact in the four equipment examples.

Same-edition String, Resource Descriptor and Resource Type evidence was reused from the completed ISA-02 dependency ledger. **Zero new unique supporting definitions were added**; the unique total remains 47, and their later full catalogue reviews remain separately assigned. Core versus Accepted extension remains explicit; an Accepted extension is not silently relabeled core.

## Coverage, preservation and delivery

The source ledger advances only ISA-DMS-084, 085, 092, 108, 109 and 110. Reviewed primary entries: **59/480**, comprising **57 supported** and **two existing questions**. Parent ISA-03 has ten properties completed across A and B, with 32 remaining. No ISA-03C source review occurred.

Six rows were inserted in the existing Identity and contacts group. All previous 80 information rows retain their values; total now 86. The four example columns remain left, foundational standards stay together and proposed DIM stays right. The 58 original primary donor records and 73 case-evidence statements are unchanged; no Profile, UML, app/server, production service or physical-device action occurred.

Workbook checks cover formulas, exact grid/evidence parity, source coverage, preservation and the summary/new-row render. GitHub publication and read-only verification use the existing exact-file/delta workflow; the linked publication record identifies the actual run and hashes.

## Next named batch

**ISA-03C only:** Orientation (083), Perceived Position (086), Position (088), Position Override (089). Apply the same small-batch preflight and reuse the exact-edition spatial supporting evidence already reviewed where applicable. Stop before ISA-03D.
