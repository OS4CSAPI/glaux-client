import { expect, test } from 'vitest';
import { interpretSourcePacket, STEP32_FORMAT } from '../src/profile/source-packet';

// Artificial, neutral packet; NOT an original vendor record, live unit or OGC payload.
function referencePacket(): any {
  return {
    format: STEP32_FORMAT, id: 's33-neutral-reference', focus: 'design',
    sources: [{ id: 'document', issuer: 'Fictional study publisher', title: 'Synthetic equipment description',
      url: 'https://example.invalid/design', authority: 'MANUFACTURER_ORIGINAL', edition: 'synthetic test edition',
      researchTrace: 'Step 33 test-only fixture' }],
    subjects: [
      { id: 'design', label: 'Reference arrangement', standing: 'REFERENCE_ARRANGEMENT',
        sourceIdentity: { issuer: 'Fictional study publisher', scheme: 'model', raw: 'MODEL-X' } },
      { id: 'module', label: 'Externally connected reference part', standing: 'REFERENCE_COMPONENT' },
    ],
    assertions: [
      { id: 'connects', about: 'design', concept: 'equipment.external_probe', standing: 'SOURCE_FACT',
        target: 'module', evidence: [{ sourceId: 'document', locator: 'synthetic p.1' }] },
      { id: 'example', about: 'module', concept: 'output.example_value', standing: 'SOURCE_EXAMPLE',
        value: { raw: ' 0 ', unit: 'Cel', nativeField: 'sample' },
        evidence: [{ sourceId: 'document', locator: 'synthetic p.2', nativeToken: ' 0 ' }] },
      { id: 'unknown', about: 'design', concept: 'configuration.effective_setting', standing: 'UNKNOWN',
        reason: 'A reference design supplies no installed setting.', evidence: [{ sourceId: 'document', locator: 'synthetic p.1' }] },
      { id: 'future', about: 'design', concept: 'future.external-vocabulary-field', standing: 'SOURCE_FACT',
        value: { raw: '' }, extraSourceDetails: { missing: false, numericZero: 0 },
        evidence: [{ sourceId: 'document', locator: 'synthetic p.3' }] },
    ],
    originalEvents: [], representations: [], holds: [], futureTopLevel: { preserved: false, empty: '' },
  };
}

test('same typed path preserves reference standing, exact tokens, SOURCE_EXAMPLE and UNKNOWN without an Observation', () => {
  const raw = referencePacket();
  const original = JSON.stringify(raw);
  const model = interpretSourcePacket(raw);
  expect(model.accepted).toBe(true);
  expect(model.focus?.standing).toBe('REFERENCE_ARRANGEMENT');
  expect(model.claims.find(c => c.id === 'example')).toMatchObject({
    standing: 'SOURCE_EXAMPLE', kind: 'literal', value: { raw: ' 0 ', unit: 'Cel', nativeField: 'sample' },
  });
  expect(model.claims.find(c => c.id === 'unknown')).toMatchObject({
    standing: 'UNKNOWN', kind: 'unknown', reason: 'A reference design supplies no installed setting.',
  });
  expect(model.claims.find(c => c.id === 'unknown')?.value).toBeUndefined();
  expect(model.events).toEqual([]);
  expect(model.raw).toBe(raw);
  expect(JSON.stringify(raw)).toBe(original);
});

test('unrecognized concept and extensions remain inspectable, never given invented normalized meaning', () => {
  const raw = referencePacket();
  const interpreted = interpretSourcePacket(raw);
  const foreign = interpreted.claims.find(c => c.id === 'future')!;
  expect(interpreted.accepted).toBe(true);
  expect(foreign.recognized).toBe(false);
  expect(foreign.raw).toEqual(raw.assertions[3]);
  expect((interpreted.raw as any).futureTopLevel).toEqual({ preserved: false, empty: '' });
});

test('interpretation is independent of names and packet-local identifier spelling', () => {
  const input = referencePacket();
  const changed = structuredClone(input);
  changed.subjects[0].id = 'opaque-001'; changed.subjects[0].label = 'Unrelated name';
  changed.subjects[1].id = 'opaque-002'; changed.focus = 'opaque-001';
  changed.assertions.forEach((claim: any) => {
    claim.about = claim.about === 'design' ? 'opaque-001' : 'opaque-002';
    if (claim.target === 'module') claim.target = 'opaque-002';
  });
  const view = (raw: unknown) => interpretSourcePacket(raw).claims.map(c => [c.concept, c.standing, c.kind, c.value?.raw]);
  expect(interpretSourcePacket(changed).accepted).toBe(true);
  expect(view(changed)).toEqual(view(input));
});

test('invalid UNKNOWN with an invented actual value is rejected rather than interpreted as zero or false', () => {
  const input = referencePacket();
  input.assertions[2].value = { raw: '0' };
  const result = interpretSourcePacket(input);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(i => i.message.includes('UNKNOWN'))).toBe(true);
  expect(result.raw).toBe(input);
});

test('reference model cannot become an actual individual without original source-scoped identity', () => {
  const input = referencePacket();
  input.subjects[1].standing = 'SOURCE_IDENTIFIED_EQUIPMENT';
  const result = interpretSourcePacket(input);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(i => i.message.includes('original issuer/scheme/identity'))).toBe(true);
});

test('invalid original source link cannot be treated as supported evidence', () => {
  const input = referencePacket();
  input.assertions[0].evidence[0].sourceId = 'unknown-source';
  const result = interpretSourcePacket(input);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(i => i.message.includes('Evidence must resolve'))).toBe(true);
});

test('documented design/example input cannot be converted into a performed original event', () => {
  const input = referencePacket();
  input.originalEvents.push({ id: 'imaginary', subject: 'design', sourceId: 'document', recordLocator: 'synthetic example', nativeField: 'sample' });
  const result = interpretSourcePacket(input);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(i => i.message.includes('reference-only'))).toBe(true);
});

test('synthetic original-event copies are grouped by explicit source-event ID, not counted as new source events', () => {
  const input = referencePacket();
  input.subjects.push({ id: 'station', label: 'Synthetic historical station', standing: 'SOURCE_IDENTIFIED_STATION',
    sourceIdentity: { issuer: 'Fictional study publisher', scheme: 'station code', raw: 'TEST-001' } });
  input.originalEvents.push({ id: 'source-event', subject: 'station', sourceId: 'document', recordLocator: 'synthetic row 1', nativeField: 'sample' });
  input.representations.push(
    { id: 'copy-a', originalEventId: 'source-event', resourceRef: 'synthetic-resource-a', carrier: 'CSAPI_JSON_SCALAR_EXPERIMENT',
      standing: 'HISTORICAL_PROJECT_EXPERIMENT', experimentTrace: 'fictional test fixture, not a real server' },
    { id: 'copy-b', originalEventId: 'source-event', resourceRef: 'synthetic-resource-b', carrier: 'CSAPI_JSON_ARCHIVAL_REPORT_EXPERIMENT',
      standing: 'HISTORICAL_PROJECT_EXPERIMENT', experimentTrace: 'fictional test fixture, not a real server' },
  );
  const result = interpretSourcePacket(input);
  expect(result.accepted).toBe(true);
  expect(result.events).toHaveLength(1);
  expect(result.events[0].copies).toHaveLength(2);
});

test('copy without its original source event is rejected', () => {
  const input = referencePacket();
  input.representations.push({ id: 'orphan', originalEventId: 'does-not-exist', resourceRef: 'orphan-copy',
    carrier: 'CSAPI_JSON_SCALAR_EXPERIMENT', standing: 'HISTORICAL_PROJECT_EXPERIMENT',
    experimentTrace: 'fictional test fixture' });
  expect(interpretSourcePacket(input).accepted).toBe(false);
});
