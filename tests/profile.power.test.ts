import { readFileSync } from 'node:fs';
import { expect, test, vi } from 'vitest';
import type { CapturedResource } from '../src/domain';
import { derivePowerModel, type PowerResourceInput } from '../src/profile/power';
import { MPSS, mpssTerm } from '../src/profile/definitions';

const directory = new URL('../public/fixtures/power-arrangement/', import.meta.url);
const manifest = JSON.parse(readFileSync(new URL('manifest.json', directory), 'utf8'));
const deployment = 'https://demo.example/csapi/deployments/site-01';
const station = 'https://demo.example/csapi/systems/station-01';
const sourceA = 'https://demo.example/csapi/systems/power-a';
const sourceB = 'https://demo.example/csapi/systems/power-b';
const before = '2026-09-01T08:00:00Z';
const swap = '2026-09-02T10:00:00Z';
const after = '2026-09-02T10:10:00Z';
const end = '2026-09-03T18:00:00Z';

function fixtures(): PowerResourceInput[] {
  return manifest.records.map((entry: { canonicalUrl: string; role: string; file: string; datastreamRef?: string }) => {
    const bytes = new Uint8Array(readFileSync(new URL(entry.file, directory)));
    const text = new TextDecoder().decode(bytes);
    const url = `https://local.example/fixtures/power-arrangement/${entry.file}`;
    const capture: CapturedResource = { url, requestedUrl: url, status: 200, contentType: 'application/json', headers: {},
      retrievedAt: '2030-01-01T00:00:00Z', bytes, text, json: JSON.parse(text) };
    return { canonicalUrl: entry.canonicalUrl, role: entry.role, datastreamRef: entry.datastreamRef, capture };
  });
}

function input(records: PowerResourceInput[], role: string): PowerResourceInput {
  return records.find(record => record.role === role)!;
}

function body(records: PowerResourceInput[], role: string): any {
  return input(records, role).capture!.json;
}

function power(records = fixtures(), at?: string) {
  return derivePowerModel(records, { at, deploymentRef: deployment });
}

function supplies(records: PowerResourceInput[], at: string) {
  return power(records, at).relationships.filter(edge => edge.kind === 'powers' && edge.applicability === 'applicable')
    .map(edge => edge.subject?.target?.ref);
}

test('unchanged connected example derives the A/B boundary without altering captured identities, bytes or readings', () => {
  const records = fixtures();
  const preserved = records.map(record => ({ bytes: [...record.capture!.bytes], text: record.capture!.text,
    json: JSON.stringify(record.capture!.json) }));
  const fetch = vi.fn(() => { throw new Error('Pure derivation must not fetch.'); });
  vi.stubGlobal('fetch', fetch);
  try {
    expect(supplies(records, before)).toEqual([sourceA]);
    expect(supplies(records, '2026-09-02T09:59:59.999Z')).toEqual([sourceA]);
    expect(supplies(records, swap)).toEqual([sourceB]);
    expect(supplies(records, after)).toEqual([sourceB]);
    expect(supplies(records, end)).toEqual([]);
    const model = power(records, after);
    expect(model.issues).toEqual([]);
    expect(model.relationships.map(edge => [edge.interval.from, edge.interval.until]))
      .toEqual([[before, swap], [swap, end]]);
    expect(model.replacementEvents).toHaveLength(1);
    const event = model.replacementEvents[0];
    expect([event.status, event.time, event.ref, event.replaced?.target?.ref, event.replacement?.target?.ref])
      .toEqual(['valid', swap, `${deployment}#event-swap`, sourceA, sourceB]);
    expect(event.affectedSubjects.map(ref => ref.target?.ref)).toEqual([station]);
    expect(event.evidence.path).toBe('/history/1');
    const reading = model.observations[0];
    expect([reading.status, reading.value, reading.unit, reading.definition]).toEqual(['valid', 12.6, 'V', mpssTerm('supply-terminal-voltage')]);
    expect(reading.reportingSystem?.target?.ref).toBe(station);
    expect(reading.observedSubject?.target?.ref).toBe(sourceB);
    expect(reading.reportingSystem?.target?.uniqueId).not.toBe(reading.observedSubject?.target?.uniqueId);
    expect(reading.phenomenonTime).toBe(after);
    expect(reading.resultTime).toBe(after);
    expect(reading.schemaEvidence?.path).toBe('/resultSchema');
    expect(reading.outputEvidence?.path).toBe('/outputs/2');
    expect(reading.matchingRelationshipRefs).toEqual([`${deployment}#power-after`]);
    expect(model.observations).toHaveLength(1);
    expect(fetch).not.toHaveBeenCalled();
    records.forEach((record, index) => {
      expect([...record.capture!.bytes]).toEqual(preserved[index].bytes);
      expect(record.capture!.text).toBe(preserved[index].text);
      expect(JSON.stringify(record.capture!.json)).toBe(preserved[index].json);
    });
  } finally { vi.unstubAllGlobals(); }
});

test('selected or retrieval times never move a later reading to source A, and omission of at never means now', () => {
  const records = fixtures();
  const model = power(records, before);
  expect(model.observations[0].observedSubject?.target?.ref).toBe(sourceB);
  expect(model.observations[0].phenomenonTime).toBe(after);
  expect(model.observations[0].matchingRelationshipRefs).toEqual([`${deployment}#power-after`]);
  expect(power(records).relationships.every(edge => edge.applicability === 'unselected')).toBe(true);
});

test('literal labels and harness roles do not choose energy semantics; the three directed kinds stay distinct', () => {
  const records = fixtures();
  for (const record of records) {
    record.role = 'unrelated-harness-label';
    (record.capture!.json as any).label = 'Battery ready 100%';
  }
  const resource = records.find(record => record.canonicalUrl === deployment)!.capture!.json as any;
  resource.characteristics[3].label = 'Voltage meter';
  resource.characteristics[3].characteristics[1].value = 'meters';
  resource.characteristics[4].label = 'Add these values';
  resource.characteristics[4].characteristics[1].value = 'aggregates';
  const model = power(records, after);
  expect(model.relationships.map(edge => edge.kind)).toEqual(['meters', 'aggregates']);
  expect(model.relationships.every(edge => edge.status === 'valid')).toBe(true);
  expect(model.observations[0].value).toBe(12.6);
  expect(model.observations[0].matchingRelationshipRefs).toEqual([]);
  expect(model.relationships).toHaveLength(2);
  expect(model.observations).toHaveLength(1);
});

test('unknown group definitions remain raw while unknown kind codes remain rejected relationship evidence', () => {
  const records = fixtures();
  const groups = body(records, 'deployment').characteristics;
  groups[3].definition = 'https://unrecognized.example/group/energy-relationship';
  groups[4].characteristics[1].value = 'charges';
  const model = power(records, after);
  expect(model.relationships).toHaveLength(1);
  expect(model.relationships[0].declaredKind).toBe('charges');
  expect(model.relationships[0].kind).toBeUndefined();
  expect(model.relationships[0].status).toBe('unsupported');
  expect(model.relationships[0].applicability).toBe('unknown');
  expect(model.resources).toBe(records);
  expect((model.relationships[0].evidence.raw as any).characteristics[1].value).toBe('charges');
});

test('duplicate singleton terms, wrong code space and declared nil references cannot become applicable assertions', () => {
  const duplicate = fixtures();
  body(duplicate, 'deployment').characteristics[3].characteristics.push({ type: 'Text',
    definition: mpssTerm('relationship-subject-ref'), value: sourceB });
  expect(power(duplicate, before).relationships[0].status).toBe('conflicting');
  expect(power(duplicate, before).relationships[0].subject).toBeUndefined();
  const wrongSpace = fixtures();
  body(wrongSpace, 'deployment').characteristics[3].characteristics[1].codeSpace = `${MPSS}codes/not-energy`;
  expect(power(wrongSpace, before).relationships[0].status).toBe('invalid');
  const declaredNil = fixtures();
  body(declaredNil, 'deployment').characteristics[3].characteristics[0].nilValues = [{ value: sourceA, reason: 'unknown' }];
  expect(power(declaredNil, before).relationships[0].subject).toBeUndefined();
  expect(supplies(declaredNil, before)).toEqual([]);
});

test('owner#id and relative references resolve supplied owned identities, and duplicate ids remain ambiguous', () => {
  const records = fixtures();
  body(records, 'source-a').components = [{ type: 'PhysicalComponent', id: 'terminal/1', uniqueId: 'urn:test:owned-terminal', label: 'Reported terminal' }];
  body(records, 'deployment').characteristics[3].characteristics[0].value = '../systems/power-a#terminal%2F1';
  const edge = power(records, before).relationships[0];
  expect(edge.status).toBe('valid');
  expect(edge.subject?.target?.ownerRef).toBe(sourceA);
  expect(edge.subject?.target?.uniqueId).toBe('urn:test:owned-terminal');
  expect(edge.subject?.target?.evidence.path).toBe('/components/0');
  body(records, 'source-a').components.push({ type: 'PhysicalComponent', id: 'terminal/1', label: 'Another supplied record' });
  const ambiguous = power(records, before).relationships[0];
  expect(ambiguous.subject?.status).toBe('ambiguous');
  expect(ambiguous.subject?.target).toBeUndefined();
  expect(ambiguous.status).toBe('conflicting');
  expect(ambiguous.applicability).toBe('unknown');
});

test('unresolved and unsafe references are retained without fetches or endpoint guesses', () => {
  const records = fixtures();
  body(records, 'deployment').characteristics[3].characteristics[0].value = '../systems/not-supplied';
  body(records, 'deployment').characteristics[4].characteristics[0].value = 'javascript:alert(1)';
  const edges = power(records, after).relationships;
  expect(edges[0].subject?.status).toBe('unresolved');
  expect(edges[0].subject?.value).toBe('../systems/not-supplied');
  expect(edges[0].subject?.resolvedRef).toBe('https://demo.example/csapi/systems/not-supplied');
  expect(edges[1].subject?.status).toBe('invalid');
  expect(edges.every(edge => edge.applicability === 'unknown')).toBe(true);
});

test('invalid or unsupported temporal conditions do not create applicability; explicit open ends retain their meaning', () => {
  for (const bad of ['2026-02-30T08:00:00Z', '2026-09-01T08:00:00', '2026-09-01T08:00:00.0001Z', 'yesterday']) {
    const records = fixtures();
    body(records, 'deployment').characteristics[3].conditions[0].value = bad;
    const edge = power(records, before).relationships[0];
    expect(edge.interval.from).toBe(bad);
    expect(edge.status).toBe('invalid');
    expect(edge.applicability).toBe('unknown');
  }
  const unsupported = fixtures();
  body(unsupported, 'deployment').characteristics[3].conditions.push({ type: 'Boolean', definition: 'https://example.invalid/condition', value: false });
  expect(power(unsupported, before).relationships[0].applicability).toBe('unknown');
  const openEnded = fixtures();
  body(openEnded, 'deployment').characteristics[3].conditions.splice(1, 1);
  expect(power(openEnded, after).relationships[0].applicability).toBe('applicable');
  expect(power(openEnded, after).relationships[0].interval.until).toBeUndefined();
  expect(power(fixtures(), '2026-09-02T10:00:00').relationships.every(edge => edge.applicability === 'unknown')).toBe(true);
});

test('deployment scope mismatch and duplicate owner ids remain conflicts instead of first-value-wins', () => {
  const records = fixtures();
  body(records, 'deployment').characteristics[3].characteristics.push({ type: 'Text', definition: mpssTerm('deployment-ref'), value: station });
  const first = power(records, before).relationships[0];
  expect(first.status).toBe('invalid');
  expect(first.applicability).toBe('unknown');
  const duplicate = fixtures();
  body(duplicate, 'deployment').characteristics[4].id = 'power-before';
  expect(power(duplicate, before).relationships.every(edge => edge.status === 'conflicting')).toBe(true);
  const selected = derivePowerModel(fixtures(), { at: after, deploymentRef: 'https://demo.example/csapi/deployments/missing' });
  expect(selected.relationships.every(edge => edge.applicability === 'unknown')).toBe(true);
});

test('a replacement must preserve distinct identities and valid event evidence', () => {
  const records = fixtures();
  body(records, 'deployment').history[1].properties[3].value = sourceA;
  const event = power(records, after).replacementEvents[0];
  expect(event.status).toBe('conflicting');
  expect(event.issues.some(issue => issue.code === 'same-replacement-subject')).toBe(true);
  expect((event.evidence.raw as any).properties[3].value).toBe(sourceA);
  body(records, 'deployment').history[1].time = false;
  expect(power(records, after).replacementEvents[0].status).toBe('invalid');
});

test('zero is a reading, while false, null, numeric strings and declared nil values are not', () => {
  const zero = fixtures();
  body(zero, 'observation').result = 0;
  expect(power(zero, after).observations[0].value).toBe(0);
  for (const bad of [false, null, '12.6', Number.NaN, Infinity]) {
    const records = fixtures();
    body(records, 'observation').result = bad;
    const reading = power(records, after).observations[0];
    expect(reading.status).toBe('invalid');
    expect(reading.value).toBeUndefined();
    expect(reading.rawResult).toBe(bad);
  }
  const unknown = fixtures();
  body(unknown, 'schema').resultSchema.nilValues = [{ value: -9999, reason: 'unknown' }];
  body(unknown, 'observation').result = -9999;
  const reading = power(unknown, after).observations[0];
  expect(reading.value).toBeUndefined();
  expect(reading.rawResult).toBe(-9999);
  expect(reading.status).toBe('unsupported');
});

test('definition and unit mismatches across producer, stream and schema cannot become reported terminal voltage', () => {
  const changedDefinition = fixtures();
  body(changedDefinition, 'schema').resultSchema.definition = 'https://example.invalid/battery-percent';
  expect(power(changedDefinition, after).observations[0].value).toBeUndefined();
  const changedUnit = fixtures();
  body(changedUnit, 'schema').resultSchema.uom.code = 'mV';
  const reading = power(changedUnit, after).observations[0];
  expect(reading.unit).toBe('mV');
  expect(reading.rawResult).toBe(12.6);
  expect(reading.value).toBeUndefined();
  const outputMismatch = fixtures();
  body(outputMismatch, 'station').outputs[2].definition = 'https://example.invalid/other-voltage';
  expect(power(outputMismatch, after).observations[0].status).toBe('conflicting');
  const streamMismatch = fixtures();
  body(streamMismatch, 'datastream').observedProperties.push({ definition: 'https://example.invalid/unexplained' });
  expect(power(streamMismatch, after).observations[0].value).toBeUndefined();
  const formatMismatch = fixtures();
  body(formatMismatch, 'schema').obsFormat = 'text/csv';
  expect(power(formatMismatch, after).observations[0].status).toBe('unsupported');
  expect(power(formatMismatch, after).observations[0].value).toBeUndefined();
});

test('missing or competing schema associations and stream ids cannot be silently guessed', () => {
  const missing = fixtures();
  delete input(missing, 'schema').datastreamRef;
  expect(power(missing, after).observations[0].status).toBe('unresolved');
  expect(power(missing, after).observations[0].value).toBeUndefined();
  const duplicatedSchema = fixtures();
  duplicatedSchema.push({ ...input(duplicatedSchema, 'schema'), canonicalUrl: 'https://demo.example/another-schema' });
  expect(power(duplicatedSchema, after).observations[0].status).toBe('conflicting');
  const duplicatedStream = fixtures();
  duplicatedStream.push({ ...input(duplicatedStream, 'datastream'), canonicalUrl: 'https://demo.example/another-stream' });
  expect(power(duplicatedStream, after).observations[0].datastream?.status).toBe('ambiguous');
  const conflictedLink = fixtures();
  body(conflictedLink, 'observation')['datastream@link'] = { href: station };
  expect(power(conflictedLink, after).observations[0].value).toBeUndefined();
});

test('fixed historical stream subjects never become the reporting system by fallback', () => {
  const historical = fixtures();
  body(historical, 'datastream')['featureOfInterest@link'] = { href: sourceA };
  body(historical, 'observation').phenomenonTime = before;
  body(historical, 'observation').resultTime = before;
  const reading = power(historical, after).observations[0];
  expect(reading.reportingSystem?.target?.ref).toBe(station);
  expect(reading.observedSubject?.target?.ref).toBe(sourceA);
  expect(reading.matchingRelationshipRefs).toEqual([`${deployment}#power-before`]);
  const missing = fixtures();
  delete body(missing, 'datastream')['featureOfInterest@link'];
  expect(power(missing, after).observations[0].observedSubject).toBeUndefined();
  expect(power(missing, after).observations[0].value).toBeUndefined();
  const conflictingUid = fixtures();
  body(conflictingUid, 'datastream')['system@link'].uid = 'urn:example:different-physical-system';
  expect(power(conflictingUid, after).observations[0].reportingSystem?.status).toBe('ambiguous');
  expect(power(conflictingUid, after).observations[0].value).toBeUndefined();
  const wrongSubject = fixtures();
  body(wrongSubject, 'datastream')['featureOfInterest@link'].href = deployment;
  expect(power(wrongSubject, after).observations[0].status).toBe('invalid');
  expect(power(wrongSubject, after).observations[0].value).toBeUndefined();
});

test('owner#id addressability does not turn Events, characteristic groups or vendor metadata into energy subjects', () => {
  for (const ref of [`${deployment}#event-swap`, `${station}#technical`, `${sourceB}#faux-source`]) {
    const records = fixtures();
    // Even a process type buried in a non-native carrier is insufficient.
    body(records, 'source-b').vendorMetadata = { id: 'faux-source', type: 'PhysicalComponent', label: 'Power source' };
    body(records, 'deployment').characteristics[4].characteristics[0].value = ref;
    const edge = power(records, after).relationships[1];
    expect(edge.subject?.status).toBe('resolved');
    expect(edge.status).toBe('invalid');
    expect(edge.applicability).toBe('unknown');
    expect(edge.issues.some(issue => issue.code === 'invalid-energy-subject')).toBe(true);
  }
});

test('reporting process and output correspondence are required even when a fragment resolves', () => {
  const wrongProducer = fixtures();
  body(wrongProducer, 'datastream')['system@link'] = { href: `${station}#technical` };
  const rejected = power(wrongProducer, after).observations[0];
  expect(rejected.reportingSystem?.status).toBe('resolved');
  expect(rejected.status).toBe('invalid');
  expect(rejected.value).toBeUndefined();
  expect(rejected.issues.some(issue => issue.code === 'unresolved-producer-output')).toBe(true);
  const embeddedProducer = fixtures();
  body(embeddedProducer, 'station').components.push({ type: 'PhysicalComponent', id: 'reporter',
    uniqueId: 'urn:example:reported-component', outputs: [structuredClone(body(embeddedProducer, 'station').outputs[2])] });
  body(embeddedProducer, 'datastream')['system@link'] = { href: `${station}#reporter`, uid: 'urn:example:reported-component' };
  const accepted = power(embeddedProducer, after).observations[0];
  expect(accepted.status).toBe('valid');
  expect(accepted.value).toBe(12.6);
  expect(accepted.outputEvidence?.path).toBe('/components/1/outputs/0');
});

test('unimplemented observation-specific or sampling subject context stays evidence and cannot retarget a valid reading', () => {
  for (const field of ['featureOfInterest@link', 'featureOfInterest@id', 'foi@link', 'foi@id', 'samplingFeature@id']) {
    const records = fixtures();
    body(records, 'observation')[field] = field.endsWith('@link') ? { href: sourceA } : 'power-a';
    const reading = power(records, after).observations[0];
    expect(reading.status).toBe('unsupported');
    expect(reading.value).toBeUndefined();
    expect(reading.observedSubject).toBeUndefined();
    expect((reading.evidence.raw as any)[field]).toEqual(body(records, 'observation')[field]);
  }
  const sharedSampling = fixtures();
  body(sharedSampling, 'datastream')['samplingFeature@link'] = { href: 'https://demo.example/csapi/samplingFeatures/part' };
  expect(power(sharedSampling, after).observations[0].value).toBeUndefined();
});

test('schema-declared subjectRef can refine only a supplied native component inside its owning feature', () => {
  const records = fixtures();
  body(records, 'source-b').components = [{ type: 'PhysicalComponent', id: 'terminal', uniqueId: 'urn:example:terminal' }];
  body(records, 'schema').parametersSchema.fields.push({ type: 'Text', name: 'subjectRef', definition: mpssTerm('subject-ref') });
  body(records, 'observation').parameters.subjectRef = `${sourceB}#terminal`;
  const reading = power(records, after).observations[0];
  expect(reading.status).toBe('valid');
  expect(reading.observedSubject?.target?.ref).toBe(`${sourceB}#terminal`);
  expect(reading.value).toBe(12.6);
  body(records, 'source-a').components = [{ type: 'PhysicalComponent', id: 'terminal', uniqueId: 'urn:example:other-terminal' }];
  body(records, 'observation').parameters.subjectRef = `${sourceA}#terminal`;
  const unrelated = power(records, after).observations[0];
  expect(unrelated.status).toBe('conflicting');
  expect(unrelated.value).toBeUndefined();
});

test('failed resource capture cannot contribute evidence-selected facts but remains inspectable', () => {
  const records = fixtures();
  input(records, 'source-b').capture!.status = 503;
  const model = power(records, after);
  expect(model.relationships[1].subject?.status).toBe('unresolved');
  expect(model.relationships[1].applicability).toBe('unknown');
  expect(model.observations[0].value).toBeUndefined();
  expect(model.resources).toBe(records);
  expect(model.issues.some(issue => issue.code === 'resource-unavailable')).toBe(true);
});
