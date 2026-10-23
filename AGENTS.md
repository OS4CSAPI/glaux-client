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
- The current increment implements the existing Overview, Equipment, and Condition
  wireframes using the MPSS v0.3.5 source materials. Read the actual sources and
  the bounded view mapping; do not infer requirements from this brief.
- Bounded profile interpretation and explicitly synthetic, source-grounded local
  fixtures are authorized for this increment. Keep standard access competent and
  expose unsupported or ambiguous mappings without inventing profile rules.
- Vendor adapters, device controls, generalized ontology engines, OSCAR workflows,
  and an Operational Episode model remain outside this increment.
- Do not commit research archives, manuals, internal documents, captured operational
  data, credentials, private endpoints, or unrelated workspace material.
- Do not deploy, alter existing infrastructure, write to servers, or change the
  profile. No DGIWG or other organizational adoption/endorsement is established.
- Install and validate using the [README](README.md); dependency changes must follow
  the deliberate update procedure in [DEPENDENCIES](Docs/DEPENDENCIES.md).

## Documentation convention

- Use [Docs/README.md](Docs/README.md) as the documentation index and `Docs/` as
  the single project documentation root; do not create a parallel lowercase tree.
- Organize material under Governance, Plans, Research, Design, or Testing as
  described in the index. Keep the root README and this file in place.
- Keep current authoritative material easy to identify. Label proposals and
  superseded history explicitly, with links to their current replacements.
  A folder or recorded proposal does not approve a design change.
- Add only material suitable and authorized for public release. Do not bulk-import
  research archives, manufacturer manuals, or private workspace material.
- Keep executable tests and fixtures in code directories; link to them from
  documentation rather than maintaining competing copies.
- Keep `Docs/Plans/CURRENT_WORK.md` current with the last verified implementation
  checkpoint, completed checks, limitations, and the next concrete action. Save
  source changes on the working branch at meaningful increments; an in-chat
  progress report is not a source-code checkpoint.
