# Rank 9 provenance donor intake

Authorized by the owner's Proceed on 23 November 2026 following the discussion of the draft SOSA–PROV alignment. Compare with the 620-row master at f65205635b90605b2f3f5fab01495427ec563831. Roster W3C-PROV-DM, source register 159 and companion 160, plan step 32.

## Pinned originals

| Source | Status and use |
|---|---|
| [PROV-DM, 30 April 2013](https://www.w3.org/TR/2013/REC-prov-dm-20130430/) | Recommendation. Use §5 and its six components to inventory the donor's concepts. |
| [PROV-O, 30 April 2013](https://www.w3.org/TR/2013/REC-prov-o-20130430/) | Recommendation. Use starting-point, expanded and qualified terms to check the semantics of proposed mappings. |
| [SOSA/SSN Working Draft, 19 November 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261119/) | Draft §§4.3.1 and 7.1.4. Use as companion evidence for the sensor-domain bridge. |
| [SOSA/SSN Recommendation, 19 October 2017](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/) | Existing crosswalk edition. Its §6.5 alignment is explicitly non-normative. Compare these published mappings separately from the draft. |

## Initial edition comparison

Both align observation, actuation and sampling with Activity, procedures with Plan, and results with Entity. The draft also aligns Execution and Deployment with Activity and maps input value usage and execution start/end timestamps. The 2017 alignment lists Sensor, Actuator and Sampler under both Agent and Entity. The draft gives a union of Agent or Entity for Asset and System and uses a generic madeBySystem mapping. Check the inference from that property against PROV-O before assigning responsibility to equipment. The draft's qualified execution association and procedure chain is a specific mapping pattern. Carry each edition and status with its evidence.

## Bounded comparison

1. Inventory entities/activities and times, derivation, agents and responsibility, bundles, alternate/specialized entities, and collections. Record applicable terms, scope exclusions and unresolved differences.
2. Compare each of the 620 information rows and check for additional client needs. Start with N42.42 derived data and analysis execution plus MIMOSA recorded events and supporting evidence. Test whether a client can distinguish input from output, plan from execution, responsible agent from equipment used, observation time from generation time, and a derivation assertion from an evidence or confidence assertion. Treat provenance assertions independently of issuer authentication or authorization.
3. Document each direct, partial, related, unsupported or held comparison with an original locator and explanation. Check possible new candidates against each existing donor before proposing rows. Keep the 2017 mapping and draft evidence edition-qualified. Confirm distinct contributions and workbook parity in the subsequent comparison and integration step.

Intake reviewed the cited alignment sections and identified the Recommendation editions. Full term reconciliation, ontology-file and inference checks, row dispositions and Excel integration are pending.
