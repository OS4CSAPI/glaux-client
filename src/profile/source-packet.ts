/**
 * First, bounded Glaux interpreter of the project-authored Step 32 evidence packet.
 * This is a read-only, source-independent research input; it is NOT an OGC/CSAPI
 * wire-format validator, discovery mechanism, source-authentication check, or
 * a production Resource Details adapter. See Step32_Source_Packet_Contract.md.
 */
export const STEP32_FORMAT = 'dim-csapi-source-packet.s32.v0.1';

export type ClaimStanding = 'SOURCE_FACT' | 'SOURCE_EXAMPLE' | 'DERIVED' | 'UNKNOWN';
export type SubjectStanding = 'REFERENCE_ARRANGEMENT' | 'REFERENCE_COMPONENT'
  | 'SOURCE_IDENTIFIED_STATION' | 'SOURCE_IDENTIFIED_EQUIPMENT';
export type InterpretationIssue = { path: string; message: string };
export type SourceIdentity = { issuer: string; scheme: string; raw: string };
export type SubjectView = { id: string; label: string; standing: SubjectStanding; sourceIdentity?: SourceIdentity };
export type EvidenceRef = { sourceId: string; locator: string; nativeToken?: string };
export type ClaimView = {
  id: string; about: string; concept: string; standing: ClaimStanding;
  kind: 'literal' | 'relationship' | 'unknown';
  recognized: boolean; value?: { raw: string; unit?: string; nativeField?: string };
  target?: string; reason?: string; evidence: EvidenceRef[];
  /** Original source time and derivation are retained, never normalized or promoted. */
  time?: unknown; derivation?: { method: string; inputs: string[] };
  /** The unmodified complete input assertion, including future/foreign fields. */
  raw: unknown;
};
export type EventView = {
  id: string; subject: string; sourceId: string; recordLocator: string; nativeField: string;
  copies: { id: string; resourceRef: string; carrier: string; standing: string }[];
};
export type SourcePacketView = {
  accepted: boolean; focus: SubjectView | null; subjects: SubjectView[];
  claims: ClaimView[]; events: EventView[]; issues: InterpretationIssue[];
  /** Source is retained byte-/value-faithfully by reference; this function never mutates it. */
  raw: unknown;
};

type RecordValue = Record<string, unknown>;
const record = (x: unknown): x is RecordValue => x !== null && typeof x === 'object' && !Array.isArray(x);
const nonempty = (x: unknown): x is string => typeof x === 'string' && x.trim().length > 0;
const claims = new Set<ClaimStanding>(['SOURCE_FACT', 'SOURCE_EXAMPLE', 'DERIVED', 'UNKNOWN']);
const subjects = new Set<SubjectStanding>([
  'REFERENCE_ARRANGEMENT', 'REFERENCE_COMPONENT', 'SOURCE_IDENTIFIED_STATION', 'SOURCE_IDENTIFIED_EQUIPMENT',
]);
// Candidate packet concept vocabulary, NOT an OGC property catalogue or adopted ontology.
const concepts = new Set([
  'equipment.external_probe', 'equipment.reference_component', 'equipment.design_connection', 'equipment.role_service',
  'output.native_field', 'output.field_count', 'output.example_value', 'power.rated_capacity',
  'observation.aggregation_method', 'observation.source_value', 'observation.source_stamp',
  'observation.raw_quality_token', 'observation.nominal_period', 'observation.contributing_equipment',
  'observation.result_time', 'observation.producing_system', 'configuration.effective_setting',
  'identity.installed_unit', 'location.probe_position', 'source.native',
  // 41R-03 generic, reference-only whole-System coverage vocabulary (project, not OGC wire).
  'configuration.documented_default', 'configuration.documented_example', 'configuration.supported_action',
  'output.message_type', 'output.status_field', 'communications.supported_interface',
  'communications.documented_reporting', 'power.design_specification',
  'software.reference_revision', 'software.installed_version',
]);
// Two distinct PROJECT packet versions; 41R-03 adds source coverage without altering frozen Step 32 syntax.
const supportedResearchFormats = new Set([STEP32_FORMAT, 'dim-csapi-source-packet.s41r03.v0.1']);

/** Only declared standing and cross-reference consistency are checked: NOT actual source authority. */
export function interpretSourcePacket(input: unknown): SourcePacketView {
  const issues: InterpretationIssue[] = [];
  const issue = (path: string, message: string): void => { issues.push({ path, message }); };
  const result: SourcePacketView = { accepted: false, focus: null, subjects: [], claims: [], events: [], issues, raw: input };
  if (!record(input) || !supportedResearchFormats.has(input.format as string)) {
    issue('/format', 'Missing or unsupported project input format; not a CSAPI resource.');
    return result;
  }
  const requiredArrays = ['sources', 'subjects', 'assertions', 'originalEvents', 'representations', 'holds'] as const;
  for (const key of requiredArrays) if (!Array.isArray(input[key])) issue('/' + key, 'Required array missing.');
  if (issues.length > 0) return result;
  if (!nonempty(input.id) || !nonempty(input.focus)) issue('/', 'Packet and focal subject IDs are required.');

  const sourcesById = new Map<string, RecordValue>();
  for (const [i, v] of (input.sources as unknown[]).entries()) {
    const path = '/sources/' + i;
    if (!record(v) || !nonempty(v.id) || !nonempty(v.issuer) || !nonempty(v.edition)
        || !nonempty(v.title) || !nonempty(v.url) || !nonempty(v.researchTrace)) {
      issue(path, 'Source must identify an issuer, edition, document and research trace.'); continue;
    }
    if (sourcesById.has(v.id)) issue(path, 'Duplicate source ID.');
    else sourcesById.set(v.id, v);
  }
  const subjectsById = new Map<string, SubjectView>();
  for (const [i, v] of (input.subjects as unknown[]).entries()) {
    const path = '/subjects/' + i;
    if (!record(v) || !nonempty(v.id) || !nonempty(v.label) || !subjects.has(v.standing as SubjectStanding)) {
      issue(path, 'Invalid declared subject identity or standing.'); continue;
    }
    if (subjectsById.has(v.id)) { issue(path, 'Duplicate subject ID.'); continue; }
    const subject: SubjectView = { id: v.id, label: v.label, standing: v.standing as SubjectStanding };
    if (v.sourceIdentity !== undefined) {
      if (!record(v.sourceIdentity) || !nonempty(v.sourceIdentity.issuer) ||
          !nonempty(v.sourceIdentity.scheme) || !nonempty(v.sourceIdentity.raw)) {
        issue(path + '/sourceIdentity', 'Identity declaration is incomplete.');
      } else subject.sourceIdentity = { issuer: v.sourceIdentity.issuer, scheme: v.sourceIdentity.scheme,
        raw: v.sourceIdentity.raw };
    }
    if (subject.standing.startsWith('SOURCE_IDENTIFIED_') && !subject.sourceIdentity) {
      issue(path, 'An actual source-identified subject needs its original issuer/scheme/identity.');
    }
    subjectsById.set(v.id, subject);
    result.subjects.push(subject);
  }
  result.focus = subjectsById.get(input.focus as string) ?? null;
  if (!result.focus) issue('/focus', 'Focal referent does not resolve to a declared subject.');

  const eventsById = new Map<string, EventView>();
  const originalKeys = new Set<string>();
  for (const [i, v] of (input.originalEvents as unknown[]).entries()) {
    const path = '/originalEvents/' + i;
    if (!record(v) || !nonempty(v.id) || !nonempty(v.subject) || !nonempty(v.sourceId) ||
        !nonempty(v.recordLocator) || !nonempty(v.nativeField)) {
      issue(path, 'Original event identity requires source, subject, record and field.'); continue;
    }
    if (eventsById.has(v.id)) { issue(path, 'Duplicate original-event ID.'); continue; }
    if (!sourcesById.has(v.sourceId) || !subjectsById.has(v.subject)) issue(path, 'Unknown source or event subject.');
    if (subjectsById.get(v.subject)?.standing.startsWith('REFERENCE_')) {
      issue(path, 'A reference-only subject cannot substantiate an actual performed source event.');
    }
    const key = JSON.stringify([v.sourceId, v.subject, v.recordLocator, v.nativeField]);
    if (originalKeys.has(key)) issue(path, 'The same original source record/field is counted as a new event.');
    originalKeys.add(key);
    const event: EventView = { id: v.id, subject: v.subject, sourceId: v.sourceId,
      recordLocator: v.recordLocator, nativeField: v.nativeField, copies: [] };
    eventsById.set(v.id, event);
    result.events.push(event);
  }
  const representationIds = new Set<string>();
  for (const [i, v] of (input.representations as unknown[]).entries()) {
    const path = '/representations/' + i;
    if (!record(v) || !nonempty(v.id) || !nonempty(v.originalEventId) || !nonempty(v.resourceRef) ||
        !nonempty(v.carrier) || v.standing !== 'HISTORICAL_PROJECT_EXPERIMENT' || !nonempty(v.experimentTrace)) {
      issue(path, 'Representation requires a traceable historical experiment, not a new source event.'); continue;
    }
    if (representationIds.has(v.id)) issue(path, 'Duplicate representation ID.');
    representationIds.add(v.id);
    const original = eventsById.get(v.originalEventId);
    if (!original) { issue(path, 'Copy does not resolve to an original source event.'); continue; }
    original.copies.push({ id: v.id, resourceRef: v.resourceRef, carrier: v.carrier, standing: v.standing });
  }

  const claimIds = new Set<string>();
  const pendingDerivations: { path: string; inputs: string[] }[] = [];
  for (const [i, v] of (input.assertions as unknown[]).entries()) {
    const path = '/assertions/' + i;
    if (!record(v) || !nonempty(v.id) || !nonempty(v.about) || !nonempty(v.concept) ||
        !claims.has(v.standing as ClaimStanding) || !Array.isArray(v.evidence)) {
      issue(path, 'Invalid assertion identity, standing or evidence list.'); continue;
    }
    if (claimIds.has(v.id)) issue(path, 'Duplicate assertion ID.');
    claimIds.add(v.id);
    if (!subjectsById.has(v.about) && !eventsById.has(v.about)) issue(path, 'Unknown assertion subject/event.');
    const ev: EvidenceRef[] = [];
    if (v.evidence.length === 0) issue(path + '/evidence', 'At least one original source locator is required.');
    for (const [j, x] of v.evidence.entries()) {
      if (!record(x) || !nonempty(x.sourceId) || !nonempty(x.locator) || !sourcesById.has(x.sourceId) ||
          (x.nativeToken !== undefined && typeof x.nativeToken !== 'string')) {
        issue(path + '/evidence/' + j, 'Evidence must resolve to a source and preserve literal tokens.'); continue;
      }
      const item: EvidenceRef = { sourceId: x.sourceId, locator: x.locator };
      if (typeof x.nativeToken === 'string') item.nativeToken = x.nativeToken;
      ev.push(item);
    }
    const standing = v.standing as ClaimStanding;
    const hasLiteral = v.value !== undefined, hasTarget = v.target !== undefined;
    const kind: ClaimView['kind'] = standing === 'UNKNOWN' ? 'unknown' : hasLiteral ? 'literal' : 'relationship';
    if (standing === 'UNKNOWN') {
      if (hasLiteral || hasTarget || v.derivation !== undefined || !nonempty(v.reason))
        issue(path, 'UNKNOWN must have a reason and no invented value, target or derivation.');
    } else if (hasLiteral === hasTarget) issue(path, 'Known claim needs exactly one literal value or relationship target.');
    const claim: ClaimView = { id: v.id, about: v.about, concept: v.concept,
      standing, kind, recognized: concepts.has(v.concept), evidence: ev, raw: v };
    if (hasLiteral) {
      if (!record(v.value) || typeof v.value.raw !== 'string' ||
          (v.value.unit !== undefined && typeof v.value.unit !== 'string') ||
          (v.value.nativeField !== undefined && typeof v.value.nativeField !== 'string')) {
        issue(path + '/value', 'Literal source value must retain its raw string.');
      } else claim.value = { raw: v.value.raw, ...(typeof v.value.unit === 'string' ? { unit: v.value.unit } : {}),
        ...(typeof v.value.nativeField === 'string' ? { nativeField: v.value.nativeField } : {}) };
    }
    if (hasTarget) {
      if (!nonempty(v.target) || !subjectsById.has(v.target)) issue(path + '/target', 'Relationship target is not a declared subject.');
      else claim.target = v.target;
    }
    if (standing === 'UNKNOWN') claim.reason = typeof v.reason === 'string' ? v.reason : undefined;
    if (v.time !== undefined) claim.time = v.time; // never interpret date-only or derived time as an instant
    if (standing === 'DERIVED') {
      if (!record(v.derivation) || !nonempty(v.derivation.method) || !Array.isArray(v.derivation.inputs) ||
          v.derivation.inputs.length === 0 || !v.derivation.inputs.every(nonempty)) {
        issue(path + '/derivation', 'Derived claim requires original assertion input IDs and a method.');
      } else {
        const inputs = v.derivation.inputs as string[];
        claim.derivation = { method: v.derivation.method, inputs: [...inputs] };
        pendingDerivations.push({ path, inputs });
      }
    } else if (v.derivation !== undefined) issue(path, 'Only DERIVED claims may have a derivation.');
    // Unknown or future concept names remain inspectable, never silently mapped to common semantics.
    result.claims.push(claim);
  }
  for (const { path, inputs } of pendingDerivations) {
    for (const inputId of inputs) if (!claimIds.has(inputId)) issue(path + '/derivation', 'Input assertion ID does not resolve: ' + inputId);
  }
  result.accepted = issues.length === 0;
  return result;
}
