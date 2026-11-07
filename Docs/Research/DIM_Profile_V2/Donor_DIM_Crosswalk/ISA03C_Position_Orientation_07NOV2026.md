# ISA-03C — Position and orientation

**7 November 2026 · Four of four assigned source reviews COMPLETE and integrated. Next: ISA-03D only.**

[Current workbook](ISA_Correction_Review_ISA03C_07NOV2026.xlsx) · [Full comparison](ISA_Correction_Review_ISA03C_07NOV2026.md) · [Source evidence](ISA03C_Position_Orientation_Evidence_07NOV2026.json) · [Publication record](ISA03C_Publication_Record_07NOV2026.json) · [PITON](PITON_ISA_Coverage_Correction_07NOV2026.md).

## Four original-source outcomes

Original authority: *ISA Data Model Specification*, release 6.0 revision12, 31 October2023, §3.1 printed pp.14–15/PDF29–30. Full Perceived Position continuation was read. Core/extension standing follows the original body markings.

| Native term | Standing | Recorded outcome |
|---|---|---|
| Orientation | Core | World-orientation role and Rotation structure recorded; exact reference-frame interpretation retained as ISA-Q003. |
| Perceived Position | Accepted extension | Hardware-reported position when ordinary Position is overridden. Optional even when an override capability is provided. |
| Position | Core | Reported current geographic position of the identified component. |
| Position Override | Accepted extension | Position value used to override a hardware-perceived position, not a boolean activation flag. |

Four spatial candidate/review rows were added: ISA-C-083, -086, -088 and -089. Three have supported direct fits to deliberately specific information labels. The Orientation row is present with its known role and a precise frame question—not omitted and not a claim that ISA lacks orientation.

## Reference-frame question ISA-Q003

The Orientation property calls its reference Earth-Centered Earth-Fixed and also describes x toward true north, y to the component's right and z down along gravity. It distinguishes this world-space use from Attached Orientation and Local Orientation. The Rotation type separately defines required yaw, pitch and roll and their sequential axes (z, new y-prime, new x-double-prime). Those statements are retained without choosing an implicit frame identifier or manufacturing a coordinate transformation.

ISA-Q003 asks which precise frame/axis interpretation should govern a numeric transformation. It is assigned to the later full Rotation/spatial-guidance reconciliation, with the original definition and alternatives retained. The source review of these four entries is complete; this question affects the numerical Orientation mapping, not the existence of its information role or the three position-property mappings.

## Supporting structures and missing values

Same-edition Rotation, Geographic Position, Measured Degrees, Degrees and Meters evidence was reused from ISA-02. The original Geographic Position table on PDF110 was inspected as an image and text; Rotation was read across PDF126–127. The property-page image request failed, but its indexed original text was available. No unavailable image inspection is claimed.

Geographic Position requires latitude and longitude. It separately describes optional altitude and error-ellipsoid fields, the source's geoid/EGM96 convention and default behavior. An absent altitude or default zero error term is not an observed height or proof of perfect accuracy. Preserve the source geographic fields; do not transform them into a manufactured Cartesian representation. No new supporting-definition identities were introduced: unique support count remains47, and later full catalogue passes remain assigned.

The source roles do not establish active override state, the setter's identity, authorization, physical movement, verified survey accuracy, or actual device locations. In particular, the Bennett station location must not silently become the exact EE181 probe coordinate. Existing case facts, attached/local transforms and earlier source decisions are unchanged.

## Coverage, checking and handoff

Cumulative primary outcomes: **63 reviewed /60 supported /three exact questions** (Level, Link Loss, Orientation frame). **90 information/review rows** comprise the original31 plus56 supported candidates and three question rows. Parent ISA-03:14 of42 properties reviewed,28 remain. The 480-entry source inventory,279 blocks,31 original row/topic targets,25 earlier findings,58 earlier primary donor records and73 case statements are preserved.

The existing workbook was edited with artifact_tool, with changed spatial rows and the summary visually checked. Formula caches, source/CSV/workbook parity, previous grid values and original evidence preservation are checked before publication and again by a separate read-only job on the published commit. The [publication record](ISA03C_Publication_Record_07NOV2026.json) pins output hashes and the workflow result.

**Next “proceed”: ISA-03D only—Relationship and Visible.** Their actual definitions control the comparison; do not assume a familiar word means an ISA architectural role.
