import type { CapturedResource } from '../domain';
import { MPSS, mpssGroup, mpssTerm } from './definitions';

/** Transport/fixture metadata is separate from the unchanged resource body. */
export interface PowerResourceInput {
  canonicalUrl: string;
  capture?: CapturedResource;
  role?: string;
  datastreamRef?: string;
  error?: string;
}

export interface PowerEvidence {
  sourceUrl: string;
  canonicalUrl: string;
  path: string;
  raw: unknown;
  retrievedAt?: string;
}

export interface PowerIssue {
  code: string;
  message: string;
  evidence: PowerEvidence;
}

export type PowerRecordStatus = 'valid' | 'unresolved' | 'invalid' | 'conflicting' | 'unsupported';
export type PowerApplicability = 'applicable' | 'outside' | 'unknown' | 'unselected';
export type EnergyRelationshipKind = 'powers' | 'meters' | 'aggregates';

export interface PowerEntity {
  key: string;
  ref: string;
  aliases: string[];
  id?: string;
  uniqueId?: string;
  label?: string;
  type: string;
  ownerRef?: string;
  evidence: PowerEvidence;
}

export interface PowerReference {
  value: unknown;
  resolvedRef?: string;
  status: 'resolved' | 'unresolved' | 'invalid' | 'ambiguous';
  target?: PowerEntity;
  evidence: PowerEvidence;
}

export interface PowerInterval {
  from?: string;
  until?: string;
  fromEvidence?: PowerEvidence;
  untilEvidence?: PowerEvidence;
  status: 'valid' | 'invalid' | 'unspecified';
}

export interface PowerRelationship {
  key: string;
  id?: string;
  ref?: string;
  label?: string;
  kind?: EnergyRelationshipKind;
  declaredKind?: unknown;
  subject?: PowerReference;
  object?: PowerReference;
  deployment?: PowerReference;
  interval: PowerInterval;
  applicability: PowerApplicability;
  status: PowerRecordStatus;
  issues: PowerIssue[];
  evidence: PowerEvidence;
}

export interface PowerReplacementEvent {
  key: string;
  id?: string;
  ref?: string;
  label?: string;
  time?: string;
  affectedSubjects: PowerReference[];
  deployment?: PowerReference;
  replaced?: PowerReference;
  replacement?: PowerReference;
  status: PowerRecordStatus;
  issues: PowerIssue[];
  evidence: PowerEvidence;
}

export interface PowerObservation {
  key: string;
  id?: string;
  datastream?: PowerReference;
  reportingSystem?: PowerReference;
  observedSubject?: PowerReference;
  deployment?: PowerReference;
  definition?: string;
  unit?: string;
  value?: number;
  rawResult: unknown;
  phenomenonTime?: string;
  resultTime?: string;
  matchingRelationshipRefs: string[];
  status: PowerRecordStatus;
  issues: PowerIssue[];
  evidence: PowerEvidence;
  schemaEvidence?: PowerEvidence;
  outputEvidence?: PowerEvidence;
}

export interface PowerModel {
  at?: string;
  deploymentRef?: string;
  resources: readonly PowerResourceInput[];
  entities: PowerEntity[];
  relationships: PowerRelationship[];
  replacementEvents: PowerReplacementEvent[];
  observations: PowerObservation[];
  issues: PowerIssue[];
}

type JsonObject = Record<string, unknown>;
interface Resource {
  input: PowerResourceInput;
  body: JsonObject;
  path: string;
  entity: PowerEntity;
}
interface Located {
  value: JsonObject;
  evidence: PowerEvidence;
}
interface Checked {
  status: PowerRecordStatus;
  issues: PowerIssue[];
}

const PROCESS_TYPES = new Set(['PhysicalSystem', 'PhysicalComponent', 'SimpleProcess', 'AggregateProcess']);
const GREGORIAN = 'http://www.opengis.net/def/uom/ISO-8601/0/Gregorian';
const VOLTAGE = mpssTerm('supply-terminal-voltage');
const REPLACEMENT = `${MPSS}event/power-source-replacement`;
const ENERGY_CODES = `${MPSS}codes/energy-relationship`;
const statusRank: Record<PowerRecordStatus, number> = { valid: 0, unresolved: 1, unsupported: 2, conflicting: 3, invalid: 4 };

function object(value: unknown): value is JsonObject {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function text(value: unknown): string | undefined {
  return typeof value === 'string' && value.trim() !== '' ? value : undefined;
}

function id(value: unknown): string | undefined {
  return text(value) ?? (typeof value === 'number' && Number.isFinite(value) ? String(value) : undefined);
}

function pointer(parent: string, key: string | number): string {
  return `${parent}/${String(key).replace(/~/g, '~0').replace(/\//g, '~1')}`;
}

/** Parse explicit zoned instants to millisecond precision. Never round finer
 * source times into a possibly different side of the replacement boundary. */
function instant(value: unknown): number | undefined {
  if (typeof value !== 'string') return undefined;
  const match = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d{1,3})?(Z|[+-]\d{2}:\d{2})$/.exec(value);
  if (!match) return undefined;
  const [, yearText, monthText, dayText, hourText, minuteText, secondText, zone] = match;
  const [year, month, day, hour, minute, second] = [yearText, monthText, dayText, hourText, minuteText, secondText].map(Number);
  const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  const monthDays = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (month < 1 || month > 12 || day < 1 || day > monthDays[month - 1] || hour > 23 || minute > 59 || second > 59) return undefined;
  if (zone !== 'Z' && (Number(zone.slice(1, 3)) > 23 || Number(zone.slice(4)) > 59)) return undefined;
  const parsed = Date.parse(value);
  return Number.isFinite(parsed) ? parsed : undefined;
}

function uri(value: unknown, base?: string): string | undefined {
  if (!text(value)) return undefined;
  try {
    const url = new URL(value as string, base);
    if (!['https:', 'http:', 'urn:'].includes(url.protocol) || url.username || url.password) return undefined;
    return url.href;
  } catch { return undefined; }
}

function unit(value: JsonObject): string | undefined {
  if (!object(value.uom)) return undefined;
  const code = text(value.uom.code);
  const href = text(value.uom.href);
  return code && href ? undefined : code ?? href;
}

function nil(value: unknown, schema: JsonObject): boolean {
  return Array.isArray(schema.nilValues) && schema.nilValues.some(entry => object(entry)
    && Object.hasOwn(entry, 'value') && String(entry.value) === String(value));
}

function same(left: PowerReference | undefined, right: PowerReference | undefined): boolean {
  if (!left?.target || !right?.target || left.status !== 'resolved' || right.status !== 'resolved') return false;
  return left.target.key === right.target.key
    || (left.target.uniqueId !== undefined && left.target.uniqueId === right.target.uniqueId);
}

function evidence(input: PowerResourceInput, path: string, raw: unknown): PowerEvidence {
  return { sourceUrl: input.capture?.url ?? input.canonicalUrl, canonicalUrl: input.canonicalUrl, path, raw,
    retrievedAt: input.capture?.retrievedAt };
}

/** Pure bounded MPSS R16–R18 interpretation. Does not fetch, mutate or infer now. */
export function derivePowerModel(
  resources: readonly PowerResourceInput[],
  options: { at?: string; deploymentRef?: string } = {},
): PowerModel {
  const result: PowerModel = { ...options, resources, entities: [], relationships: [], replacementEvents: [], observations: [], issues: [] };
  const contexts: Resource[] = [];
  const aliases = new Map<string, PowerEntity[]>();
  const entityInputs = new Map<string, PowerResourceInput>();
  const eligibleProcesses = new Set<string>();
  const addIssue = (checked: Checked | undefined, code: string, message: string, source: PowerEvidence, status: PowerRecordStatus): void => {
    const issue = { code, message, evidence: source };
    result.issues.push(issue);
    if (checked) {
      checked.issues.push(issue);
      if (statusRank[status] > statusRank[checked.status]) checked.status = status;
    }
  };

  const addEntity = (input: PowerResourceInput, value: JsonObject, path: string, ref: string, ownerRef?: string): PowerEntity => {
    const type = text(value.type) ?? (Object.hasOwn(value, 'resultSchema') ? 'ResultSchema'
      : Object.hasOwn(value, 'datastream@id') || Object.hasOwn(value, 'datastream@link') ? 'Observation'
      : Object.hasOwn(value, 'observedProperties') && Object.hasOwn(value, 'system@link') ? 'DataStream' : 'JSON record');
    const entity: PowerEntity = { key: `${result.entities.length}:${input.canonicalUrl}#${path}`, ref, aliases: [ref],
      id: id(value.id), uniqueId: text(value.uniqueId) ?? text(value.uid), label: text(value.label) ?? text(value.name),
      type, ownerRef, evidence: evidence(input, path, value) };
    if (entity.uniqueId) {
      const unique = uri(entity.uniqueId);
      if (unique) entity.aliases.push(unique);
    }
    if (!ownerRef && Array.isArray(value.links)) {
      for (const link of value.links) {
        if (object(link) && link.rel === 'self') {
          const self = uri(link.href, input.canonicalUrl);
          if (self) entity.aliases.push(self);
        }
      }
    }
    entity.aliases = [...new Set(entity.aliases)];
    result.entities.push(entity);
    entityInputs.set(entity.key, input);
    for (const alias of entity.aliases) aliases.set(alias, [...(aliases.get(alias) ?? []), entity]);
    return entity;
  };

  for (const input of resources) {
    const capture = input.capture;
    const source = evidence(input, '', capture?.json ?? input.error);
    if (!capture || input.error || capture.status < 200 || capture.status >= 300) {
      addIssue(undefined, 'resource-unavailable', input.error ?? `Resource unavailable${capture ? ` (HTTP ${capture.status})` : ''}; no facts are derived from it.`, source, 'unresolved');
      continue;
    }
    if (!object(capture.json) || !uri(input.canonicalUrl)) {
      addIssue(undefined, 'invalid-resource', 'A resource needs an explicit safe canonical identifier and a JSON object; original content remains evidence.', source, 'invalid');
      continue;
    }
    const body = capture.json.type === 'Feature' && object(capture.json.properties) ? capture.json.properties : capture.json;
    const path = body === capture.json ? '' : '/properties';
    const entity = addEntity(input, body, path, uri(input.canonicalUrl)!);
    contexts.push({ input, body, path, entity });
    // Resolve existing native owner#id addresses. This does not classify an
    // embedded record as a battery, connector or Power Interface.
    const indexChildren = (value: unknown, childPath: string, depth: number): void => {
      if (depth > 48) return;
      if (Array.isArray(value)) { value.forEach((entry, index) => indexChildren(entry, pointer(childPath, index), depth + 1)); return; }
      if (!object(value)) return;
      const localId = text(value.id);
      if (localId) {
        const child = addEntity(input, value, childPath, `${entity.ref.split('#')[0]}#${encodeURIComponent(localId)}`, entity.ref);
        // Self aliases of a resource may also address its explicitly owned ids.
        for (const ownerAlias of entity.aliases) {
          const alias = `${ownerAlias.split('#')[0]}#${encodeURIComponent(localId)}`;
          if (!child.aliases.includes(alias)) {
            child.aliases.push(alias);
            aliases.set(alias, [...(aliases.get(alias) ?? []), child]);
          }
        }
      }
      for (const [key, child] of Object.entries(value)) indexChildren(child, pointer(childPath, key), depth + 1);
    };
    if (PROCESS_TYPES.has(entity.type) || entity.type === 'Deployment') {
      for (const [key, child] of Object.entries(body)) indexChildren(child, pointer(path, key), 0);
    }
    if (PROCESS_TYPES.has(entity.type)) {
      eligibleProcesses.add(entity.key);
      // Addressability is not eligibility. Only native embedded process
      // components are accepted here, not arbitrary metadata carrying an id.
      const nativeComponents = (parent: JsonObject, parentPath: string, depth = 0): void => {
        if (depth > 48 || !Array.isArray(parent.components)) return;
        parent.components.forEach((component, index) => {
          if (!object(component) || !PROCESS_TYPES.has(String(component.type))) return;
          const componentPath = pointer(pointer(parentPath, 'components'), index);
          const candidates = result.entities.filter(candidate => entityInputs.get(candidate.key) === input && candidate.evidence.path === componentPath);
          if (candidates.length === 1) eligibleProcesses.add(candidates[0].key);
          nativeComponents(component, componentPath, depth + 1);
        });
      };
      nativeComponents(body, path);
    }
  }

  const reference = (value: unknown, source: PowerEvidence): PowerReference => {
    const rawHref = object(value) ? value.href : value;
    const suppliedUid = object(value) ? text(value.uid) : undefined;
    const resolvedRef = uri(rawHref, source.canonicalUrl) ?? (rawHref === undefined && suppliedUid ? uri(suppliedUid) : undefined);
    const ref: PowerReference = { value, resolvedRef, status: 'invalid', evidence: source };
    if (!resolvedRef) return ref;
    const found = aliases.get(resolvedRef) ?? [];
    if (found.length === 0) ref.status = 'unresolved';
    else if (found.length !== 1) ref.status = 'ambiguous';
    else if (suppliedUid !== undefined && found[0].uniqueId !== suppliedUid) ref.status = 'ambiguous';
    else { ref.status = 'resolved'; ref.target = found[0]; }
    return ref;
  };
  const checkReference = (ref: PowerReference | undefined, checked: Checked, name: string): void => {
    if (!ref || ref.status === 'resolved') return;
    addIssue(checked, `${ref.status}-reference`, `${name} reference is ${ref.status}; no target is chosen.`, ref.evidence,
      ref.status === 'invalid' ? 'invalid' : ref.status === 'ambiguous' ? 'conflicting' : 'unresolved');
  };
  const locatedMembers = (value: unknown, source: PowerEvidence, key: string): Located[] => {
    return Array.isArray(value) ? value.flatMap((member, index) => object(member)
      ? [{ value: member, evidence: { ...source, path: pointer(pointer(source.path, key), index), raw: member } }] : []) : [];
  };
  const termMembers = (members: Located[], term: string): Located[] => members.filter(member => member.value.definition === mpssTerm(term));
  const singleton = (members: Located[], term: string, checked: Checked, source: PowerEvidence, required = true): Located | undefined => {
    const matches = termMembers(members, term);
    if (matches.length > 1) {
      addIssue(checked, 'duplicate-term', `The singleton ${term} is supplied more than once; all candidates remain evidence.`, source, 'conflicting');
      return undefined;
    }
    if (!matches.length && required) addIssue(checked, 'missing-term', `Required ${term} is not supplied.`, source, 'invalid');
    return matches[0];
  };
  const textReference = (member: Located | undefined, checked: Checked, name: string): PowerReference | undefined => {
    if (!member) return undefined;
    if (member.value.type !== 'Text' || !text(member.value.value) || nil(member.value.value, member.value)) {
      addIssue(checked, 'invalid-reference-term', `${name} requires a non-nil Text reference.`, member.evidence, 'invalid');
      return undefined;
    }
    const ref = reference(member.value.value, { ...member.evidence, path: pointer(member.evidence.path, 'value'), raw: member.value.value });
    checkReference(ref, checked, name);
    return ref;
  };
  const deploymentScope = (resource: Resource, explicit: PowerReference | undefined, checked: Checked, source: PowerEvidence): PowerReference | undefined => {
    const owner = resource.entity.type === 'Deployment' ? reference(resource.entity.ref, resource.entity.evidence) : undefined;
    if (explicit?.target && explicit.target.type !== 'Deployment') {
      addIssue(checked, 'invalid-deployment', 'The declared deployment reference resolves to a different resource type.', explicit.evidence, 'invalid');
    }
    if (owner && explicit && !same(owner, explicit)) {
      addIssue(checked, 'conflicting-deployment', 'The explicit deployment does not unambiguously match the enclosing Deployment.', source, 'conflicting');
    }
    return explicit ?? owner;
  };
  const localIdentity = (value: JsonObject, source: PowerEvidence, checked: Checked): { id?: string; ref?: string } => {
    const localId = text(value.id);
    if (!localId) { addIssue(checked, 'missing-id', 'This profile record requires an explicit native id.', source, 'invalid'); return {}; }
    const ref = `${source.canonicalUrl.split('#')[0]}#${encodeURIComponent(localId)}`;
    if ((aliases.get(ref)?.length ?? 0) !== 1) addIssue(checked, 'ambiguous-id', 'The native owner#id identifies multiple records; none is selected as authoritative.', source, 'conflicting');
    return { id: localId, ref };
  };

  const readInterval = (group: JsonObject, source: PowerEvidence, checked: Checked): PowerInterval => {
    const interval: PowerInterval = { status: 'unspecified' };
    if (group.conditions === undefined) return interval;
    if (!Array.isArray(group.conditions)) {
      addIssue(checked, 'invalid-conditions', 'Relationship conditions are not an array.', source, 'invalid');
      return { status: 'invalid' };
    }
    const conditions = locatedMembers(group.conditions, source, 'conditions');
    if (conditions.length !== group.conditions.length || conditions.some(item => ![mpssTerm('effective-from'), mpssTerm('effective-until')].includes(String(item.value.definition)))) {
      addIssue(checked, 'unsupported-condition', 'Additional or unsupported conditions prevent a claim of temporal applicability.', source, 'unsupported');
      interval.status = 'invalid';
    }
    for (const [term, key] of [['effective-from', 'from'], ['effective-until', 'until']] as const) {
      const matches = termMembers(conditions, term);
      const member = singleton(conditions, term, checked, source, false);
      if (matches.length > 1) interval.status = 'invalid';
      if (!member) continue;
      interval[key] = typeof member.value.value === 'string' ? member.value.value : undefined;
      interval[key === 'from' ? 'fromEvidence' : 'untilEvidence'] = member.evidence;
      if (member.value.type !== 'Time' || unit(member.value) !== GREGORIAN || instant(member.value.value) === undefined || nil(member.value.value, member.value)) {
        addIssue(checked, 'invalid-time-bound', `${term} requires a valid zoned Time with the supplied Gregorian unit.`, member.evidence, 'invalid');
        interval.status = 'invalid';
      }
    }
    if (interval.status !== 'invalid' && (interval.from !== undefined || interval.until !== undefined)) interval.status = 'valid';
    if (interval.from && interval.until && instant(interval.from)! >= instant(interval.until)!) {
      addIssue(checked, 'invalid-interval', 'The exclusive end must be later than the inclusive start.', source, 'invalid');
      interval.status = 'invalid';
    }
    return interval;
  };

  const selectedDeployment = options.deploymentRef === undefined ? undefined
    : reference(options.deploymentRef, { sourceUrl: '', canonicalUrl: options.deploymentRef, path: '', raw: options.deploymentRef });
  if (options.at !== undefined && instant(options.at) === undefined) {
    addIssue(undefined, 'invalid-selection-time', 'The selected time is not a valid zoned instant; applicability remains unknown.',
      { sourceUrl: '', canonicalUrl: '', path: '', raw: options.at }, 'invalid');
  }
  if (selectedDeployment && (selectedDeployment.status !== 'resolved' || selectedDeployment.target?.type !== 'Deployment')) {
    addIssue(undefined, 'unresolved-selected-deployment', 'The selected deployment is not unambiguously resolved as a Deployment.', selectedDeployment.evidence, 'unresolved');
  }

  const applicability = (relationship: PowerRelationship, at: string | undefined, scope?: PowerReference): PowerApplicability => {
    if (at === undefined) return 'unselected';
    const selected = instant(at);
    if (selected === undefined || relationship.status !== 'valid' || relationship.interval.status !== 'valid') return 'unknown';
    if (scope) {
      if (scope.status !== 'resolved' || scope.target?.type !== 'Deployment' || !relationship.deployment) return 'unknown';
      if (!same(scope, relationship.deployment)) return 'outside';
    }
    // An omitted end is explicitly open-ended. An omitted start supplies no
    // supported earliest applicability, so we do not invent one.
    if (relationship.interval.from === undefined) return 'unknown';
    if (selected < instant(relationship.interval.from)!) return 'outside';
    if (relationship.interval.until !== undefined && selected >= instant(relationship.interval.until)!) return 'outside';
    return 'applicable';
  };

  for (const resource of contexts) {
    if (!PROCESS_TYPES.has(resource.entity.type) && resource.entity.type !== 'Deployment') continue;
    if (Array.isArray(resource.body.characteristics)) {
      for (const [index, group] of resource.body.characteristics.entries()) {
        if (!object(group) || group.definition !== mpssGroup('energy-relationship')) continue;
        const source = evidence(resource.input, pointer(pointer(resource.path, 'characteristics'), index), group);
        const relationship: PowerRelationship = { key: `${resource.entity.key}:${source.path}`, label: text(group.label),
          interval: { status: 'unspecified' }, applicability: 'unknown', status: 'valid', issues: [], evidence: source };
        Object.assign(relationship, localIdentity(group, source, relationship));
        const members = locatedMembers(group.characteristics, source, 'characteristics');
        relationship.subject = textReference(singleton(members, 'relationship-subject-ref', relationship, source), relationship, 'Relationship subject');
        relationship.object = textReference(singleton(members, 'relationship-object-ref', relationship, source), relationship, 'Relationship object');
        for (const endpoint of [relationship.subject, relationship.object]) {
          if (endpoint?.target && !eligibleProcesses.has(endpoint.target.key)) {
            addIssue(relationship, 'invalid-energy-subject', 'This bounded energy endpoint binding requires a native System/process or embedded process component; an arbitrary owner#id record is not equipment or a Power Interface.', endpoint.evidence, 'invalid');
          }
        }
        const kind = singleton(members, 'energy-relationship-kind', relationship, source);
        if (kind) {
          relationship.declaredKind = kind.value.value;
          const codeSpace = object(kind.value.codeSpace) ? kind.value.codeSpace.href : kind.value.codeSpace;
          if (kind.value.type !== 'Category' || codeSpace !== ENERGY_CODES || nil(kind.value.value, kind.value)) {
            addIssue(relationship, 'invalid-kind', 'The relationship kind requires the exact profile Category and code space, without a declared nil value.', kind.evidence, 'invalid');
          } else if (!['powers', 'meters', 'aggregates'].includes(String(kind.value.value)) || typeof kind.value.value !== 'string') {
            addIssue(relationship, 'unsupported-kind', 'The supplied relationship kind has no supported definition; its original value remains evidence.', kind.evidence, 'unsupported');
          } else relationship.kind = kind.value.value as EnergyRelationshipKind;
        }
        const explicitDeployment = textReference(singleton(members, 'deployment-ref', relationship, source, false), relationship, 'Deployment');
        relationship.deployment = deploymentScope(resource, explicitDeployment, relationship, source);
        relationship.interval = readInterval(group, source, relationship);
        relationship.applicability = applicability(relationship, options.at, selectedDeployment);
        result.relationships.push(relationship);
      }
    }
    if (Array.isArray(resource.body.history)) {
      for (const [index, event] of resource.body.history.entries()) {
        if (!object(event) || event.definition !== REPLACEMENT) continue;
        const source = evidence(resource.input, pointer(pointer(resource.path, 'history'), index), event);
        const replacement: PowerReplacementEvent = { key: `${resource.entity.key}:${source.path}`, label: text(event.label),
          time: typeof event.time === 'string' ? event.time : undefined, affectedSubjects: [], status: 'valid', issues: [], evidence: source };
        Object.assign(replacement, localIdentity(event, source, replacement));
        if (instant(event.time) === undefined) addIssue(replacement, 'invalid-event-time', 'Replacement time is not a valid supplied zoned instant.', source, 'invalid');
        const members = locatedMembers(event.properties, source, 'properties');
        const affected = termMembers(members, 'affected-subject-ref');
        if (!affected.length) addIssue(replacement, 'missing-affected-subject', 'No affected equipment reference is supplied.', source, 'invalid');
        replacement.affectedSubjects = affected.flatMap(member => {
          const ref = textReference(member, replacement, 'Affected subject'); return ref ? [ref] : [];
        });
        replacement.replaced = textReference(singleton(members, 'replaced-subject-ref', replacement, source), replacement, 'Replaced source');
        replacement.replacement = textReference(singleton(members, 'replacement-subject-ref', replacement, source), replacement, 'Replacement source');
        replacement.deployment = deploymentScope(resource,
          textReference(singleton(members, 'deployment-ref', replacement, source), replacement, 'Deployment'), replacement, source);
        if (same(replacement.replaced, replacement.replacement)) addIssue(replacement, 'same-replacement-subject', 'Removed and installed references identify the same subject; no distinct-source replacement is derived.', source, 'conflicting');
        result.replacementEvents.push(replacement);
      }
    }
  }

  const dataStreams = contexts.filter(resource => resource.entity.type === 'DataStream');
  const resourceFor = (ref: PowerReference | undefined): Resource | undefined => {
    if (!ref?.target) return undefined;
    const root = contexts.find(resource => resource.entity.key === ref.target!.key);
    if (root) return root;
    const input = entityInputs.get(ref.target.key);
    return input && eligibleProcesses.has(ref.target.key) && object(ref.target.evidence.raw)
      ? { input, body: ref.target.evidence.raw, path: ref.target.evidence.path, entity: ref.target } : undefined;
  };
  const nativeReference = (resource: Resource, name: string, checked: Checked, required: boolean): PowerReference | undefined => {
    const nativeId = resource.body[`${name}@id`];
    const resolveId = (): PowerReference => {
      const source = evidence(resource.input, pointer(resource.path, `${name}@id`), nativeId);
      const suppliedId = id(nativeId);
      if (suppliedId === undefined) return { value: nativeId, status: 'invalid', evidence: source };
      const matches = contexts.filter(candidate => candidate.entity.id === suppliedId
        && (name !== 'datastream' || candidate.entity.type === 'DataStream'));
      return matches.length === 1
        ? { value: nativeId, resolvedRef: matches[0].entity.ref, target: matches[0].entity, status: 'resolved', evidence: source }
        : { value: nativeId, status: matches.length ? 'ambiguous' : 'unresolved', evidence: source };
    };
    const link = resource.body[`${name}@link`];
    if (link !== undefined) {
      const source = evidence(resource.input, pointer(resource.path, `${name}@link`), link);
      const ref: PowerReference = object(link) ? reference(link, source) : { value: link, status: 'invalid', evidence: source };
      checkReference(ref, checked, name);
      if (nativeId !== undefined && !same(ref, resolveId())) {
        addIssue(checked, 'conflicting-native-reference', `The native ${name}@id and ${name}@link do not resolve to the same subject.`, source, 'conflicting');
      }
      return ref;
    }
    if (nativeId !== undefined) {
      const ref = resolveId();
      checkReference(ref, checked, name);
      return ref;
    }
    if (required) addIssue(checked, 'missing-native-reference', `No native ${name} reference is supplied.`, resource.entity.evidence, 'unresolved');
    return undefined;
  };
  for (const resource of contexts) {
    if (resource.entity.type !== 'Observation') continue;
    const observation: PowerObservation = { key: resource.entity.key, id: resource.entity.id,
      rawResult: resource.body.result, phenomenonTime: typeof resource.body.phenomenonTime === 'string' ? resource.body.phenomenonTime : undefined,
      resultTime: typeof resource.body.resultTime === 'string' ? resource.body.resultTime : undefined,
      matchingRelationshipRefs: [], status: 'valid', issues: [], evidence: resource.entity.evidence };
    observation.datastream = nativeReference(resource, 'datastream', observation, true);
    const stream = resourceFor(observation.datastream);
    if (stream && !dataStreams.includes(stream)) addIssue(observation, 'invalid-datastream', 'The native datastream reference resolves to a different resource type.', observation.datastream!.evidence, 'invalid');
    if (!stream || !dataStreams.includes(stream)) { result.observations.push(observation); continue; }
    observation.reportingSystem = nativeReference(stream, 'system', observation, true);
    const subjectContextKeys = ['featureOfInterest@link', 'featureOfInterest@id', 'foi@link', 'foi@id', 'samplingFeature@link', 'samplingFeature@id'];
    const ownSubjectContext = subjectContextKeys.filter(key => Object.hasOwn(resource.body, key));
    const samplingContext = ['samplingFeature@link', 'samplingFeature@id'].filter(key => Object.hasOwn(stream.body, key));
    if (ownSubjectContext.length || samplingContext.length) {
      addIssue(observation, 'unsupported-subject-context', 'This bounded fixed-subject example does not resolve supplied per-observation or sampling subject context. It is retained without retargeting a reading or silently applying the stream default.', resource.entity.evidence, 'unsupported');
    } else observation.observedSubject = nativeReference(stream, 'featureOfInterest', observation, true);
    for (const [name, ref] of [['Reporting system', observation.reportingSystem], ['External-source subject', observation.observedSubject]] as const) {
      if (ref?.target && !eligibleProcesses.has(ref.target.key)) {
        addIssue(observation, 'invalid-observation-subject', `${name} is not a native process or embedded process component supported by this example.`, ref.evidence, 'invalid');
      }
    }
    // The fixed stream subject and schema-declared owned subject are preserved;
    // the selected display time never rewrites either historical assertion.
    if (instant(resource.body.phenomenonTime) === undefined) addIssue(observation, 'invalid-phenomenon-time', 'A valid supplied phenomenonTime is needed for this bounded instantaneous reading.', resource.entity.evidence, 'invalid');
    if (resource.body.resultTime !== undefined && instant(resource.body.resultTime) === undefined) addIssue(observation, 'invalid-result-time', 'Supplied resultTime is not a supported zoned instant.', resource.entity.evidence, 'invalid');
    const schemas = contexts.filter(candidate => candidate.input.datastreamRef !== undefined
      && same(reference(candidate.input.datastreamRef, candidate.entity.evidence), observation.datastream));
    if (schemas.length !== 1) {
      addIssue(observation, 'unresolved-schema', schemas.length ? 'More than one explicitly associated schema is supplied; none is chosen.'
        : 'No schema is explicitly associated with this datastream; no endpoint path or unit is invented.', resource.entity.evidence, schemas.length ? 'conflicting' : 'unresolved');
      result.observations.push(observation); continue;
    }
    const schemaResource = schemas[0];
    if (schemaResource.body.obsFormat !== 'application/json') {
      addIssue(observation, 'unsupported-observation-format', 'This bounded derivation requires an explicitly associated application/json observation schema.', schemaResource.entity.evidence, 'unsupported');
    }
    const schema = schemaResource.body.resultSchema;
    observation.schemaEvidence = evidence(schemaResource.input, pointer(schemaResource.path, 'resultSchema'), schema);
    if (!object(schema)) {
      addIssue(observation, 'invalid-result-schema', 'The associated result schema is not a component object.', observation.schemaEvidence, 'invalid');
      result.observations.push(observation); continue;
    }
    observation.definition = text(schema.definition);
    observation.unit = unit(schema);
    if (schema.type !== 'Quantity' || observation.definition !== VOLTAGE || observation.unit !== 'V') {
      addIssue(observation, 'unsupported-quantity', 'This bounded example requires its exact supply-terminal-voltage Quantity in V; other meanings and units remain evidence without conversion.', observation.schemaEvidence, 'unsupported');
    }
    const properties = stream.body.observedProperties;
    if (!Array.isArray(properties) || properties.length !== 1 || !object(properties[0]) || properties[0].definition !== schema.definition) {
      addIssue(observation, 'conflicting-property', 'Datastream observedProperties and the scalar result definition do not match unambiguously.', stream.entity.evidence, 'conflicting');
    }
    const producer = resourceFor(observation.reportingSystem);
    if (!producer || !eligibleProcesses.has(producer.entity.key)) {
      addIssue(observation, 'unresolved-producer-output', 'No supported reporting-process description is available to verify the named output; missing context is not a successful match.', observation.reportingSystem?.evidence ?? stream.entity.evidence, 'unresolved');
    } else {
      const outputs = Array.isArray(producer.body.outputs) ? producer.body.outputs : [];
      const matches = outputs.flatMap((output, index) => object(output) && output.name === stream.body.outputName && text(stream.body.outputName)
        ? [{ output, index }] : []);
      if (matches.length !== 1) addIssue(observation, 'unresolved-output', 'The supplied outputName does not resolve to one producer output.', producer.entity.evidence, matches.length ? 'conflicting' : 'unresolved');
      else {
        const { output, index } = matches[0];
        observation.outputEvidence = evidence(producer.input, pointer(pointer(producer.path, 'outputs'), index), output);
        if (output.type !== 'Quantity' || output.definition !== schema.definition || unit(output) !== observation.unit) {
          addIssue(observation, 'conflicting-output', 'Producer output, datastream property and result schema must retain the same definition and unit.', observation.outputEvidence, 'conflicting');
        }
      }
    }
    const parametersSchema = schemaResource.body.parametersSchema;
    const parameterFields = object(parametersSchema) && parametersSchema.type === 'DataRecord'
      ? locatedMembers(parametersSchema.fields, evidence(schemaResource.input, pointer(schemaResource.path, 'parametersSchema'), parametersSchema), 'fields') : [];
    const parameterReference = (term: string): PowerReference | undefined => {
      const field = singleton(parameterFields, term, observation, schemaResource.entity.evidence, false);
      if (!field) return undefined;
      if (field.value.type !== 'Text' || !text(field.value.name)) {
        addIssue(observation, 'invalid-parameter-schema', `${term} needs a named Text field in parametersSchema.`, field.evidence, 'invalid');
        return undefined;
      }
      const parameters = resource.body.parameters;
      const value = object(parameters) ? parameters[field.value.name as string] : undefined;
      if (value === undefined) return undefined;
      const source = evidence(resource.input, pointer(pointer(resource.path, 'parameters'), field.value.name as string), value);
      if (!text(value) || nil(value, field.value)) {
        addIssue(observation, 'invalid-parameter-reference', `${term} is not a supplied non-nil Text reference.`, source, 'invalid');
        return undefined;
      }
      const ref = reference(value, source); checkReference(ref, observation, term); return ref;
    };
    observation.deployment = parameterReference('deployment-ref');
    if (observation.deployment?.target && observation.deployment.target.type !== 'Deployment') addIssue(observation, 'invalid-deployment', 'Observation deployment-ref resolves to a different type of resource.', observation.deployment.evidence, 'invalid');
    const refinedSubject = parameterReference('subject-ref');
    if (refinedSubject) {
      if (refinedSubject.target?.ownerRef && eligibleProcesses.has(refinedSubject.target.key) && observation.observedSubject?.target
        && same(reference(refinedSubject.target.ownerRef, refinedSubject.evidence), observation.observedSubject)) observation.observedSubject = refinedSubject;
      else addIssue(observation, 'unresolved-subject-refinement', 'The refinement is not unambiguously an owned subject within the native feature of interest.', refinedSubject.evidence, 'conflicting');
    }
    if (typeof resource.body.result !== 'number' || !Number.isFinite(resource.body.result)) {
      addIssue(observation, 'invalid-result', 'The supplied result is not a finite numeric Quantity; no numeric reading is derived.', resource.entity.evidence, 'invalid');
    } else if (nil(resource.body.result, schema)) {
      addIssue(observation, 'nil-result', 'The result matches a declared SWE nil value; it is not a voltage reading.', observation.schemaEvidence, 'unsupported');
    }
    if (observation.status === 'valid') {
      observation.value = resource.body.result as number;
      observation.matchingRelationshipRefs = result.relationships.filter(relationship => relationship.kind === 'powers'
        && same(relationship.subject, observation.observedSubject) && same(relationship.object, observation.reportingSystem)
        && applicability(relationship, observation.phenomenonTime, observation.deployment) === 'applicable')
        .flatMap(relationship => relationship.ref ? [relationship.ref] : []);
    }
    result.observations.push(observation);
  }
  return result;
}
