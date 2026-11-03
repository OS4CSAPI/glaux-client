import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';

/**
 * Step 34 SOURCE ORACLE, not a manufacturer branch in the shared interpreter.
 * Original source: research/dim-profile-v2 controlled C sheet
 *   C-I01/02/04, C-F05/06, C-O03, C-C01 and original pinned C02/C03 locators.
 * The JSON fixture is an exact Git-blob match to the Step 32 research packet
 *   5d7931846ff88b0752dab81402a4df1703fa8077.
 * No physical installed S31-LB, operational observations or current settings exist
 * in this source corpus.
 */
const fixtureURL = new URL('./fixtures/source-packets/dragino.reference.packet.json', import.meta.url);
const fixture = (): any => JSON.parse(readFileSync(fixtureURL, 'utf8'));
const read = (x: any) => interpretSourcePacket(x);
const row = (input: any, id: string) => input.assertions.find((x: any) => x.id === id);

function sourceOracle(input: any): string[] {
  // These source checks are deliberately LOCAL TO THE TEST, not Glaux interpretation code.
  const issues: string[] = [];
  const probe = input.subjects.filter((x: any) => x.standing === 'REFERENCE_COMPONENT');
  if (input.focus !== 'c-s31' ||
      input.subjects[0]?.standing !== 'REFERENCE_ARRANGEMENT' ||
      input.subjects[0]?.sourceIdentity?.scheme !== 'model' ||
      input.subjects[0]?.sourceIdentity?.raw !== 'S31-LB')
    issues.push('C-I01: manufacturer product model is not a source-identified installed unit');
  const externalLinks = input.assertions.filter((a: any) => a.concept === 'equipment.external_probe');
  if (input.subjects.length !== 2 || probe.length !== 1 || probe[0]?.id !== 'c-sht31' ||
      externalLinks.length !== 1 || row(input, 'c-external')?.target !== 'c-sht31')
    issues.push('C-I02: one externally cabled SHT31; no second probe');
  const fields = input.assertions.filter((a: any) => a.concept === 'output.native_field');
  if (fields.length !== 2 || fields.some((x: any) => x.about !== 'c-sht31') ||
      !fields.some((x: any) => x.value?.raw === 'TempC_SHT31' && x.value?.unit === '°C') ||
      !fields.some((x: any) => x.value?.raw === 'Hum_SHT31' && x.value?.unit === '% RH'))
    issues.push('C-F05/06: two source fields from one physical reference probe');
  if (row(input, 'c-example')?.standing !== 'SOURCE_EXAMPLE' ||
      row(input, 'c-example')?.value?.raw !== '26.1')
    issues.push('C-F05: printed scalar 0x0105 is an example, not a measured current result');
  if (row(input, 'c-battery')?.standing !== 'SOURCE_FACT' ||
      row(input, 'c-battery')?.value?.raw !== '8500' ||
      row(input, 'c-battery')?.value?.unit !== 'mAh')
    issues.push('C-I04: manufacturer-rated design capacity is not remaining charge');
  if (['c-installed', 'c-effective'].some(id => row(input, id)?.standing !== 'UNKNOWN'))
    issues.push('C-I15/C-O03: no authenticated individual or effective installed interval');
  if (input.originalEvents.length || input.representations.length)
    issues.push('The model-only packet contains no acquired performed observations or copies');
  return issues;
}

test('the unchanged interpreter accepts the exact manufacturer-reference packet only at declared reference level', () => {
  const packet = fixture(), original = JSON.stringify(packet);
  const model = read(packet);
  expect(model.accepted).toBe(true);
  expect(model.issues).toEqual([]);
  expect(model.focus?.standing).toBe('REFERENCE_ARRANGEMENT');
  expect(model.subjects.map(s => s.standing)).toEqual(['REFERENCE_ARRANGEMENT', 'REFERENCE_COMPONENT']);
  expect(model.claims).toHaveLength(7);
  expect(model.events).toHaveLength(0);
  expect(model.raw).toBe(packet);
  expect(JSON.stringify(packet)).toBe(original);
  expect(sourceOracle(packet)).toEqual([]);
});

test('one external physical reference probe provides two output fields, not two independent sensor units', () => {
  const model = read(fixture());
  const external = model.claims.find(x => x.id === 'c-external')!;
  expect([external.kind, external.target, external.evidence[0]?.nativeToken])
    .toEqual(['relationship', 'c-sht31', 'SHT31']);
  expect(model.subjects).toHaveLength(2);
  const outputs = model.claims.filter(x => x.concept === 'output.native_field');
  expect(outputs).toHaveLength(2);
  expect(outputs.map(x => [x.about, x.value?.raw, x.value?.unit]))
    .toEqual([['c-sht31', 'TempC_SHT31', '°C'], ['c-sht31', 'Hum_SHT31', '% RH']]);
});

test('published decoded 26.1 °C scalar example is never counted as a performed original Observation', () => {
  const model = read(fixture());
  expect(model.accepted).toBe(true);
  const example = model.claims.find(x => x.id === 'c-example')!;
  expect([example.standing, example.value?.raw, example.value?.nativeField])
    .toEqual(['SOURCE_EXAMPLE', '26.1', 'TempC_SHT31']);
  expect(model.events).toHaveLength(0);
  expect(model.raw).toMatchObject({ originalEvents: [], representations: [] });
});

test('8500 mAh is a design rating; installed serial, effective interval and condition are not invented', () => {
  const model = read(fixture());
  const battery = model.claims.find(x => x.id === 'c-battery')!;
  expect([battery.standing, battery.value?.raw, battery.value?.unit]).toEqual(['SOURCE_FACT', '8500', 'mAh']);
  for (const id of ['c-installed', 'c-effective']) {
    const unknown = model.claims.find(x => x.id === id)!;
    expect([unknown.kind, unknown.standing, unknown.value]).toEqual(['unknown', 'UNKNOWN', undefined]);
    expect(unknown.reason).toBeTruthy();
  }
  expect(model.claims.some(x => x.concept === 'power.remaining_charge')).toBe(false);
});

test('renaming opaque local subject IDs and labels does not change interpretation rules', () => {
  const p = fixture(), clone = structuredClone(p);
  clone.focus = 'new-node'; clone.subjects[0].id = 'new-node'; clone.subjects[0].label = 'Another label';
  clone.subjects[1].id = 'new-probe'; clone.subjects[1].label = 'Other reference component';
  clone.assertions.forEach((a: any) => {
    a.about = a.about === 'c-s31' ? 'new-node' : a.about === 'c-sht31' ? 'new-probe' : a.about;
    if (a.target === 'c-sht31') a.target = 'new-probe';
  });
  const original = read(p), renamed = read(clone);
  expect(renamed.accepted).toBe(true);
  expect(renamed.claims.map(x => [x.concept, x.standing, x.kind, x.value?.raw]))
    .toEqual(original.claims.map(x => [x.concept, x.standing, x.kind, x.value?.raw]));
});

test('rejects an externally connected probe pointing to an undeclared subject', () => {
  const p = fixture(); row(p, 'c-external').target = 'invented-subject';
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('Relationship target'))).toBe(true);
});

test('rejects a broken original publisher/decoder source reference', () => {
  const p = fixture(); row(p, 'c-humidity-field').evidence[0].sourceId = 'missing-source';
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('Evidence must resolve'))).toBe(true);
});

test('rejects an invented installed serial value on an explicitly UNKNOWN claim', () => {
  const p = fixture(); row(p, 'c-installed').value = { raw: 'fictional-device-serial' };
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('UNKNOWN'))).toBe(true);
});

test('rejects manufacturing an actual performed event from a reference example', () => {
  const p = fixture();
  p.originalEvents.push({ id: 'fake-observation', subject: 'c-s31', sourceId: 'c02',
    recordLocator: 'printed scalar example', nativeField: 'TempC_SHT31' });
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('reference-only'))).toBe(true);
});

test('critical counterexample: a model renamed as an actual individual passes reader shape but FAILS original-source standing', () => {
  const p = fixture();
  p.subjects[0].standing = 'SOURCE_IDENTIFIED_EQUIPMENT';
  const result = read(p);
  expect(result.accepted).toBe(true); // the generic reader does NOT authenticate issuer/scheme
  expect(sourceOracle(p)).toContain('C-I01: manufacturer product model is not a source-identified installed unit');
});

test('critical counterexample: printed sample promoted to SOURCE_FACT passes structural read but FAILS source oracle', () => {
  const p = fixture(); row(p, 'c-example').standing = 'SOURCE_FACT';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p)).toContain('C-F05: printed scalar 0x0105 is an example, not a measured current result');
});

test('critical counterexample: an invented second SHT31 passes local pointers but FAILS original equipment count', () => {
  const p = fixture();
  p.subjects.push({ id: 'invented-probe', label: 'Second SHT31', standing: 'REFERENCE_COMPONENT' });
  p.assertions.push({ id: 'false-connection', about: 'c-s31', concept: 'equipment.external_probe',
    standing: 'SOURCE_FACT', target: 'invented-probe',
    evidence: [{ sourceId: 'c02', locator: 'C-I02' }] });
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p)).toContain('C-I02: one externally cabled SHT31; no second probe');
});

test('coverage gap: documented 20-minute default in C-O03 is absent from the Step 32 packet, not lost by reader', () => {
  const p = fixture();
  expect(sourceOracle(p)).toEqual([]);
  expect(read(p).accepted).toBe(true);
  expect(p.assertions.some((x: any) => x.concept === 'configuration.documented_default')).toBe(false);
  // This is a known source-to-packet omission. Do not invent an effective setting to compensate.
  expect(row(p, 'c-effective').standing).toBe('UNKNOWN');
});
