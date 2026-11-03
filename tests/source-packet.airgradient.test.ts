import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';

/**
 * Step 35 AirGradient ORIGINAL-SOURCE test oracle, NOT a vendor branch in Glaux.
 * Original A01 hardware README: pinned 89aacf5013fc0ffe4b988a2e3c5a227bce3c4983,
 * product O-M-1PPSTON-CE, 2x PMS5003 at sockets PM1/PM2 (A-I01/A-I06).
 * Original A02 firmware README: pinned 84e479a415d81151e7a81aea9a2f7449a15e98cc,
 * Wi-Fi pm01/pm25/pm10 fields and printed pm25=27.7 (A-F04/05/06).
 * The original sources are designs/examples, not an authenticated installed unit,
 * current data, verified firmware pair or a certified calibrated reading.
 * This fixture's source Git blob is f3684d6e1e8285f9f766420a379cef8c0dc60201.
 */
const fixtureURL = new URL('./fixtures/source-packets/airgradient.reference.packet.json', import.meta.url);
const fixture = (): any => JSON.parse(readFileSync(fixtureURL, 'utf8'));
const read = (packet: any) => interpretSourcePacket(packet);
const assertion = (packet: any, id: string): any => packet.assertions.find((x: any) => x.id === id);

/** Case-specific comparison with original-source audit; NEVER used to select reader mappings. */
function originalSourceOracle(packet: any): string[] {
  const issues: string[] = [];
  const byId = (id: string): any => packet.subjects.find((x: any) => x.id === id);
  if (packet.focus !== 'a-max' ||
      byId('a-max')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      byId('a-max')?.sourceIdentity?.scheme !== 'model designation' ||
      byId('a-max')?.sourceIdentity?.raw !== 'O-M-1PPSTON-CE')
    issues.push('A-I01/A-I16: model/reference cannot become an installed physical individual');
  const components = packet.subjects.filter((s: any) => s.standing === 'REFERENCE_COMPONENT');
  const sockets = packet.assertions.filter((a: any) => a.concept === 'equipment.reference_component');
  if (packet.subjects.length !== 3 || components.length !== 2 ||
      !byId('a-pm1')?.label?.includes('PMS5003') ||
      !byId('a-pm2')?.label?.includes('PMS5003') ||
      byId('a-pm1')?.sourceIdentity?.raw !== 'PM1' ||
      byId('a-pm2')?.sourceIdentity?.raw !== 'PM2' ||
      sockets.length !== 2 ||
      assertion(packet, 'a-socket1')?.target !== 'a-pm1' ||
      assertion(packet, 'a-socket2')?.target !== 'a-pm2')
    issues.push('A-I06: exactly two PMS5003 reference modules at PM1 and PM2 hardware sockets');
  const output = packet.assertions.filter((a: any) => a.concept === 'output.native_field');
  const expected = ['pm01', 'pm25', 'pm10'];
  if (output.length !== 3 || !expected.every(field =>
      output.some((a: any) => a.about === 'a-max' &&
        a.value?.raw === field && a.value?.nativeField === field &&
        a.value?.unit === 'µg/m³' && a.standing === 'SOURCE_FACT')))
    issues.push('A-F04/05/06: PM1.0, PM2.5 and PM10 are output properties, not hardware sockets');
  if (assertion(packet, 'a-example')?.standing !== 'SOURCE_EXAMPLE' ||
      assertion(packet, 'a-example')?.value?.raw !== '27.7' ||
      assertion(packet, 'a-example')?.value?.nativeField !== 'pm25')
    issues.push('A-F05: printed Wi-Fi example pm25=27.7 is not an original observed result');
  if (assertion(packet, 'a-installed')?.standing !== 'UNKNOWN')
    issues.push('A-I16/A-G01: installed identity is not established by hardware/firmware design');
  if (packet.originalEvents.length !== 0 || packet.representations.length !== 0)
    issues.push('A-G03: no authenticated performed observational events or CSAPI copies');
  return issues;
}

test('unchanged shared reader accepts the original reference packet, not an authenticated installed system', () => {
  const p = fixture(), original = JSON.stringify(p);
  const model = read(p);
  expect(model.accepted).toBe(true);
  expect(model.issues).toEqual([]);
  expect(model.focus?.standing).toBe('REFERENCE_ARRANGEMENT');
  expect(model.subjects.map(s => s.standing))
    .toEqual(['REFERENCE_ARRANGEMENT', 'REFERENCE_COMPONENT', 'REFERENCE_COMPONENT']);
  expect(model.claims).toHaveLength(7);
  expect(model.events).toHaveLength(0);
  expect(originalSourceOracle(p)).toEqual([]);
  expect(model.raw).toBe(p);
  expect(JSON.stringify(p)).toBe(original);
});

test('hardware sockets PM1 and PM2 are distinct PMS5003 reference components', () => {
  const m = read(fixture());
  const links = m.claims.filter(a => a.concept === 'equipment.reference_component');
  expect(links.map(a => [a.target, a.evidence[0]?.nativeToken]))
    .toEqual([['a-pm1', 'PM1'], ['a-pm2', 'PM2']]);
  expect(links.every(a => a.standing === 'SOURCE_FACT' && a.kind === 'relationship')).toBe(true);
  expect(m.subjects.filter(s => s.standing === 'REFERENCE_COMPONENT')).toHaveLength(2);
});

test('pm01, pm25 and pm10 are three distinct particulate properties, not additional physical sensors', () => {
  const m = read(fixture());
  const fields = m.claims.filter(a => a.concept === 'output.native_field');
  expect(fields.map(a => [a.about, a.value?.raw, a.value?.unit]))
    .toEqual([['a-max', 'pm01', 'µg/m³'], ['a-max', 'pm25', 'µg/m³'], ['a-max', 'pm10', 'µg/m³']]);
  expect(m.subjects).toHaveLength(3);
  expect(m.events).toHaveLength(0);
});

test('the 27.7 µg/m³ PM2.5 value remains a published Wi-Fi example, not current telemetry', () => {
  const p = fixture(), m = read(p), sample = m.claims.find(x => x.id === 'a-example')!;
  expect([sample.kind, sample.standing, sample.value?.raw, sample.value?.nativeField])
    .toEqual(['literal', 'SOURCE_EXAMPLE', '27.7', 'pm25']);
  expect(sample.evidence[0]?.sourceId).toBe('a02');
  expect(m.events).toHaveLength(0);
  expect(p.representations).toEqual([]);
});

test('installed identity remains UNKNOWN and source raw text is unmodified', () => {
  const p = fixture(), original = JSON.stringify(p), m = read(p);
  const unknown = m.claims.find(x => x.id === 'a-installed')!;
  expect([unknown.kind, unknown.standing, unknown.value]).toEqual(['unknown', 'UNKNOWN', undefined]);
  expect(unknown.reason).toBeTruthy();
  expect(m.raw).toBe(p);
  expect(JSON.stringify(p)).toBe(original);
});

test('opaque subject IDs and labels can change without changing the reader semantic decisions', () => {
  const p = fixture(), renamed = structuredClone(p);
  renamed.focus = 'focus-renamed';
  renamed.subjects[0].id = 'focus-renamed';
  renamed.subjects[0].label = 'Unrelated title';
  renamed.subjects[1].id = 'socket-left';
  renamed.subjects[2].id = 'socket-right';
  for (const a of renamed.assertions) {
    if (a.about === 'a-max') a.about = 'focus-renamed';
    if (a.target === 'a-pm1') a.target = 'socket-left';
    if (a.target === 'a-pm2') a.target = 'socket-right';
  }
  const result = read(renamed), before = read(p);
  expect(result.accepted).toBe(true);
  expect(result.claims.map(x => [x.concept, x.standing, x.kind, x.value?.raw]))
    .toEqual(before.claims.map(x => [x.concept, x.standing, x.kind, x.value?.raw]));
});

test('broken socket target is structurally rejected', () => {
  const p = fixture(); assertion(p, 'a-socket1').target = 'missing-socket';
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('Relationship target'))).toBe(true);
});

test('untraceable firmware example source is rejected', () => {
  const p = fixture(); assertion(p, 'a-pm25').evidence[0].sourceId = 'fake-source';
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('Evidence must resolve'))).toBe(true);
});

test('invented actual unit UID inside UNKNOWN is rejected', () => {
  const p = fixture(); assertion(p, 'a-installed').value = { raw: 'imaginary-device-001' };
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('UNKNOWN'))).toBe(true);
});

test('a fictional observation event from a reference-only subject is rejected', () => {
  const p = fixture(); p.originalEvents.push({
    id: 'fake-event', subject: 'a-max', sourceId: 'a02',
    recordLocator: 'published Wi-Fi example', nativeField: 'pm25',
  });
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('reference-only'))).toBe(true);
});

test('duplicate source assertion ID is structurally rejected', () => {
  const p = fixture(); p.assertions.push(structuredClone(p.assertions[1]));
  const result = read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x => x.message.includes('Duplicate assertion ID'))).toBe(true);
});

test('source-FALSE reference model promoted to actual device passes shape but fails original-source oracle', () => {
  const p = fixture(); p.subjects[0].standing = 'SOURCE_IDENTIFIED_EQUIPMENT';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('A-I01/A-I16: model/reference cannot become an installed physical individual');
});

test('source-FALSE PM2.5 property reassigned as hardware socket passes pointers but fails original evidence', () => {
  const p = fixture(), field = assertion(p, 'a-pm25');
  delete field.value;
  field.concept = 'equipment.reference_component';
  field.target = 'a-pm2';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('A-F04/05/06: PM1.0, PM2.5 and PM10 are output properties, not hardware sockets');
});

test('source-FALSE manufacturer PM2.5 example promoted to actual SOURCE_FACT remains structurally accepted', () => {
  const p = fixture(); assertion(p, 'a-example').standing = 'SOURCE_FACT';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('A-F05: printed Wi-Fi example pm25=27.7 is not an original observed result');
});

test('source-FALSE third PMS5003 physical reference component is exposed by independent hardware audit', () => {
  const p = fixture();
  p.subjects.push({ id: 'invented-pm3', label: 'PMS5003 at PM3',
    standing: 'REFERENCE_COMPONENT', sourceIdentity: { issuer: 'AirGradient', scheme: 'hardware socket in reference design', raw: 'PM3' } });
  p.assertions.push({ id: 'fabricated-third', about: 'a-max', concept: 'equipment.reference_component',
    standing: 'SOURCE_FACT', target: 'invented-pm3',
    evidence: [{ sourceId: 'a01', locator: 'plug-in modules', nativeToken: 'PM3' }] });
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('A-I06: exactly two PMS5003 reference modules at PM1 and PM2 hardware sockets');
});

test('coverage limitations: packet omits source-known other modules, power options and active firmware evidence', () => {
  const p = fixture(), m = read(p);
  expect(m.accepted).toBe(true);
  expect(originalSourceOracle(p)).toEqual([]);
  expect(p.subjects).toHaveLength(3);
  expect(p.assertions.some((a: any) => a.concept.startsWith('power.'))).toBe(false);
  expect(p.assertions.some((a: any) => a.concept === 'configuration.effective_setting')).toBe(false);
  expect(p.originalEvents).toHaveLength(0);
  // This packet's omission is source→packet coverage, not reader loss.
});
