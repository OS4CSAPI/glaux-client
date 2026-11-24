# Lightweight Machine to Machine comparison checkpoint

The [review plan](PLAN_LWM2M_Source_First_Donor_Review.md) pins the 621-row baseline and original sources. The following registry XML definitions were inspected at the pinned revision. LwM2M applicability as declared in the XML is distinct from the object version.

| Object ID | Definition | LwM2M version | Object version | Instances |
|---|---|---|---|---|
| 1 | Server | 1.2 | 1.2 | Multiple |
| 2 | Access Control | 1.0 | 1.1 | Multiple |
| 3 | Device | 1.1 | 1.3 | Single |
| 4 | Connectivity Monitoring | 1.1 | 1.3 | Single |
| 5 | Firmware Update | 1.1 | 1.2 | Single |

| Existing worksheet row | Finding |
|---|---|
| 4 | Direct. Device resource 0 represents Manufacturer. |
| 5 | Direct. Device resource 1 represents Model Number. |
| 6 | Direct. Device resource 2 represents Serial Number. |
| 260 | Partial. Device resource 3 describes firmware version. Broader software inventory needs additional evidence. |
| 306 | Direct for the address field. Connectivity Monitoring resource 4 exposes IP Addresses. The field alone does not establish a separate interface identity for each address. |
| 505 | Partial. Access Control resources 0–3 tie permissions and ownership to a target object and instance and distinguish servers. This is not a general current-user permission model. |
| 475 | Partial. Firmware Update resources 2, 3 and 5 distinguish the update operation, state and result. Proof that the new image is active depends on observed reporting and device-specific evidence. |
| 495 | Related. Firmware Update resource 12 represents the update state-change time, a narrower subject than a general device parameter change. |

## Candidate to test

The Core Discover operation returns resource links and applicable attributes scoped to the requesting server. It does not return the resource value as a Read does. Test whether the master already captures the distinction between a declared resource in the object definition, an instantiated path returned in discovery, and a value readable by the requesting server. Compare against rows 505 and 529 and the existing device and Thing affordance findings before adding any row.

Eight initial dispositions are recorded. The other 613 rows, candidate overlaps and workbook integration are pending.
