# Development boundaries

- Use existing CSAPI, SensorML, and SWE Common mechanisms before custom conventions.
- Keep library behavior (`src/data`), profile interpretation (`src/profile`), and
  operator presentation (`src/presentation`) distinguishable. Do not modify the
  upstream library as part of application work.
- Retain original server bytes and relevant metadata independently of parsed or
  derived models. Preserve unknown content, source meaning, subject, time, units,
  provenance, and uncertainty.
- Do not manufacture device identities, readings, relationships, or operational
  readiness. Test examples must be explicitly synthetic, never operational claims.
- Do not infer meaning from manufacturer names, display labels, or identifier spelling.
- Generic mode must retain competent standard-property and relationship handling;
  never deliberately weaken it to make profile-aware interpretation look better.
- Record specific profile gaps rather than silently revising the MERLIN/MPSS profile.
- The future starting UI scope is the existing Overview, Equipment, and Condition
  wireframes. Do not infer wireframes or profile requirements from the bootstrap
  brief when their actual source materials are unavailable.
- Do not implement vendor adapters, profile resolution, controls, OSCAR workflows,
  or an Operational Episode model during this bootstrap.
- Do not commit research archives, manuals, internal documents, captured operational
  data, credentials, private endpoints, or unrelated workspace material.
- Do not deploy, alter existing infrastructure, write to servers, or change the
  profile. No DGIWG or other organizational adoption/endorsement is established.
- Install and validate using the [README](README.md); dependency changes must follow
  the deliberate update procedure in [DEPENDENCIES](docs/DEPENDENCIES.md).
