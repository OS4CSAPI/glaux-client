# IEEE/ANSI N42.42-2020 donor comparison

## Question and starting point

What must a Connected Systems Details view preserve so a reader can trace a radiation measurement to its instrument, the detector that contributed it, its acquisition and calibration context, and any subsequent analysis? Compare against all 582 information rows at [the RFC 8348 checkpoint](https://github.com/OS4CSAPI/glaux-client/commit/3fa153b74df0092c87cfc4db86bc73a056dc0460). Rank 6, source 163, roster IEEE-N4242-2020. The eight RFC additions are part of this baseline.

## Source boundary

Use the [2020 edition](https://webstore.ansi.org/standards/ieee/ieeeansin42422020), the [NIST edition package](https://www.nist.gov/pml/radiation-physics/ansiieee-n4242-2020-version) and the [fingerprinted inventory](N42_42_Source_Coverage.json). The inventory covers the primary XML Schema Definition (XSD), the Schematron rules, the extension schema and eleven examples. Obtain the standard through the IEEE GET route, record actual clause contact, and identify any text-dependent conclusions that remain open. Instrument control and transport fall outside the published scope. Treat IEC 62755 and N42.61 as separately registered donors.

## One bounded comparison and delivery

1. Work outward from the standard. Account for the 315 named global declarations in the principal XSD in groups, following local types, attributes, references, multiplicity, units, constraints and extension points. Reconcile the Schematron rules with their applicability and the text. Record the edition, locator, subject, meaning, exceptions and normative or illustrative standing. Cover instrument, detector and item identity, state and characteristics, acquisition and timing, calibrations, raw and derived results, analysis, grouping, provenance and extensions. Use the eleven examples to test interpretation across instrument classes. Distinguish example records from observed devices. Document genuine access or interpretation holds.
2. Compare both ways. Give every baseline row a source-qualified decision. For each potentially new distinction, identify the closest row and explain what merging them would lose. Test detector-to-spectrum linkage and real versus live duration explicitly. Check all 17 earlier donor columns on each warranted addition, including prior original sources where they could resolve a question. Record held, related and scoped-negative results explicitly. Use the established classification and fill rules.
3. Deliver once. Update the canonical master, both CSVs, both readable comparisons, the same editable workbook, donor findings, evidence and recovery checkpoint. Preserve stable IDs, prior evidence and the accessible pre-change version. Verify saved values, fills, row-only freeze, package structure, mirrors, published files and the downloaded workbook. Report the information gained and source limits. Stop for the owner's assessment decision.

One **Proceed** covers these activities through verified delivery. Source and integration checkpoints are internal recovery points.
