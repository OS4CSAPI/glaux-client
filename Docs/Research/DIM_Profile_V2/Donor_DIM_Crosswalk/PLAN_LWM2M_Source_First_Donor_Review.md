# Rank 10 Lightweight Machine to Machine source intake

Review rank 10, roster OMA-LWM2M-122, register 129, against the 621 information rows at 9f24133348739e2b27f712bfa31d1ceda19796da.

- [OMA LwM2M Core 1.2.2, 13 June 2024](https://www.openmobilealliance.org/RELEASE/LightweightM2M/V1_2_2-20240613-A/HTML-Version/OMA-TS-LightweightM2M_Core-V1_2_2-20240613-A.html) is the approved baseline for the model, registration and operations.
- [OMA LwM2M Transport 1.2.2, 13 June 2024](https://www.openmobilealliance.org/RELEASE/LightweightM2M/V1_2_2-20240613-A/HTML-Version/OMA-TS-LightweightM2M_Transport-V1_2_2-20240613-A.html) is the approved binding companion. Use it where a comparison depends on addressing, encoding or delivery behavior.
- [OMA object registry snapshot](https://github.com/OpenMobileAlliance/lwm2m-registry/tree/a763bb5414099844fadf0797b2c8223d169d0c7e) provides object definitions. Start with Device, Server, Access Control, Connectivity Monitoring and Firmware Update. Record each XML object version and applicable LwM2M version before using it. The registry evolves independently of the Core release.

Compare what a management client can discover about an endpoint, Object, Object Instance, Resource and Resource Instance. Test multiplicity, identity scope, object versions, the distinction between a declared resource and a readable value, and the effect of access control. Cover registration and update, reads and writes, execution, observation and notification, and the distinction between a reported management result and evidence of actual execution.

Compare in both directions. Check each existing row and examine whether native distinctions need additional candidate rows. Start with device identity, property availability, management commands, subscriptions and software updates. Record source and version for each match. Treat transport bindings and registry-specific object semantics according to their own sources. Record explicit statuses for nonmatches and holds. Confirm parity between the ledger and the saved workbook before reporting integration.

This intake identifies the approved documents and freezes the registry revision. Object-version validation, row adjudication and workbook integration follow in the comparison.
