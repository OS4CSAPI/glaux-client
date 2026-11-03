import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';

/**
 * Step 36: original-source CASE ORACLE only; NEVER a Campbell-specific branch
 * in the shared interpreter. Source: source sheet D (30 Oct 2026), Campbell
 * first-generation ClimaVue 50 manual D02 (08/2024) Table 7-1 / Table 8-1,
 * and the separately published CR1000X MQTT Status example D07.
 * No real joined station, active program or ClimaVue numeric weather reading
 * has been obtained. Fixture matches research Git blob 3671babc4d415d480022d9372851eeb5f1c82ae3.
 */
const fixtureURL = new URL('./fixtures/source-packets/campbell.reference.packet.json', import.meta.url);
const fixture = (): any => JSON.parse(readFileSync(fixtureURL, 'utf8'));
const read = (input: any) => interpretSourcePacket(input);
const assertion = (p: any, id: string): any => p.assertions.find((a: any) => a.id === id);

/** Independent test-side source-ledger checks (not available to a generic client). */
function originalSourceOracle(p: any): string[] {
  const problems: string[] = [];
  const byId = (id: string): any => p.subjects.find((s: any) => s.id === id);
  if (p.focus !== 'd-pair' || p.subjects.length !== 3 ||
      byId('d-pair')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      byId('d-logger')?.standing !== 'REFERENCE_COMPONENT' ||
      byId('d-climavue')?.standing !== 'REFERENCE_COMPONENT' ||
      byId('d-logger')?.sourceIdentity?.scheme !== 'model' ||
      byId('d-logger')?.sourceIdentity?.raw !== 'CR1000X' ||
      byId('d-climavue')?.sourceIdentity?.raw !== 'ClimaVue 50')
    problems.push('D-I01/02/17: two separate kinds are not serial-numbered installed station components');
  const composition = p.assertions.filter((a: any) => a.concept === 'equipment.reference_component');
  if (composition.length !== 2 || assertion(p,'d-sensor')?.target !== 'd-climavue' ||
      assertion(p,'d-logger-part')?.target !== 'd-logger' ||
      assertion(p,'d-connection')?.about !== 'd-logger' ||
      assertion(p,'d-connection')?.target !== 'd-climavue' ||
      assertion(p,'d-connection')?.concept !== 'equipment.design_connection' ||
      assertion(p,'d-connection')?.evidence[0]?.nativeToken !== 'SDI-12')
    problems.push('D-I02/06: potential logger-to-sensor SDI-12 design is not a verified installed relation');
  // A response containing fourteen numerical positions is NOT fourteen independent instruments.
  if (p.subjects.length > 3 || composition.length > 2)
    problems.push('D-R01–14: fourteen aR7! positions cannot establish fourteen additional physical sensors');
  const fields = p.assertions.filter((a: any) => a.concept === 'output.native_field');
  if (assertion(p,'d-field-count')?.about !== 'd-climavue' ||
      assertion(p,'d-field-count')?.value?.raw !== '14' ||
      assertion(p,'d-field-count')?.value?.nativeField !== 'aR7!' ||
      fields.filter((a: any) => a.about === 'd-climavue').length !== 1 ||
      assertion(p,'d-ambient-field')?.about !== 'd-climavue' ||
      assertion(p,'d-ambient-field')?.value?.raw !== '8' ||
      assertion(p,'d-ambient-field')?.value?.nativeField !== 'aR7! position 8')
    problems.push('D-R01–14/D-R08: fourteen response positions belong to ONE ClimaVue, not fourteen sensors');
  if (assertion(p,'d-panel-field')?.about !== 'd-logger' ||
      assertion(p,'d-panel-field')?.value?.nativeField !== 'PanelTemp' ||
      assertion(p,'d-panel-field')?.value?.unit !== '°C' ||
      fields.filter((a: any) => a.about === 'd-logger').length !== 1)
    problems.push('D-S02: PanelTemp is the CR1000X wiring panel, not ClimaVue ambient air');
  if (assertion(p,'d-panel-example')?.about !== 'd-logger' ||
      assertion(p,'d-panel-example')?.standing !== 'SOURCE_EXAMPLE' ||
      assertion(p,'d-panel-example')?.value?.raw !== '25.91098' ||
      assertion(p,'d-panel-example')?.evidence[0]?.sourceId !== 'd07')
    problems.push('D-S02/D07: 25.91098 is a separate published logger Status example');
  if (assertion(p,'d-installed')?.about !== 'd-pair' ||
      assertion(p,'d-installed')?.standing !== 'UNKNOWN' ||
      p.originalEvents.length !== 0 || p.representations.length !== 0)
    problems.push('D-G01/G02/G05: no authenticated installed station, active program or weather Observations');
  return problems;
}

test('the unchanged reader recognizes a three-subject reference packet, not an actual station', () => {
  const p = fixture(), before = JSON.stringify(p), m = read(p);
  expect(m.accepted).toBe(true);
  expect(m.issues).toEqual([]);
  expect(m.focus?.standing).toBe('REFERENCE_ARRANGEMENT');
  expect(m.subjects.map(s => s.standing)).toEqual([
    'REFERENCE_ARRANGEMENT', 'REFERENCE_COMPONENT', 'REFERENCE_COMPONENT',
  ]);
  expect(m.claims).toHaveLength(8);
  expect(m.events).toHaveLength(0);
  expect(originalSourceOracle(p)).toEqual([]);
  expect(m.raw).toBe(p);
  expect(JSON.stringify(p)).toBe(before);
});

test('two separately documented physical reference kinds are linked only by a potential SDI-12 design connection', () => {
  const m = read(fixture());
  const membership = m.claims.filter(c => c.concept === 'equipment.reference_component');
  expect(membership.map(c => c.target)).toEqual(['d-climavue', 'd-logger']);
  expect(membership).toHaveLength(2);
  const connection = m.claims.find(c => c.id === 'd-connection')!;
  expect([connection.about, connection.target, connection.kind, connection.evidence[0].nativeToken])
    .toEqual(['d-logger', 'd-climavue', 'relationship', 'SDI-12']);
  expect(connection.concept).toBe('equipment.design_connection');
});

test('one ClimaVue aR7! response describes fourteen ordered positions, not fourteen physical sensor Systems', () => {
  const m = read(fixture());
  const count = m.claims.find(c => c.id === 'd-field-count')!;
  expect([count.about, count.standing, count.value?.raw, count.value?.nativeField])
    .toEqual(['d-climavue','SOURCE_FACT','14','aR7!']);
  expect(m.subjects).toHaveLength(3);
  expect(m.claims.filter(c => c.concept === 'output.field_count')).toHaveLength(1);
  expect(m.events).toHaveLength(0);
});

test('ClimaVue ambient air-temperature response position 8 and logger PanelTemp remain different subjects and meanings', () => {
  const m = read(fixture());
  const ambient = m.claims.find(c => c.id === 'd-ambient-field')!;
  const panel = m.claims.find(c => c.id === 'd-panel-field')!;
  expect([ambient.about, ambient.value?.nativeField, ambient.value?.raw, ambient.evidence[0]?.sourceId])
    .toEqual(['d-climavue','aR7! position 8','8','d02']);
  expect([panel.about,panel.value?.nativeField,panel.evidence[0]?.sourceId])
    .toEqual(['d-logger','PanelTemp','d07']);
  expect(panel.value?.unit).toBe('°C');
  expect(ambient.value?.raw).not.toBe('25.91098');
});

test('published logger PanelTemp=25.91098 °C is an example, not a ClimaVue reading', () => {
  const m = read(fixture());
  const sample = m.claims.find(c => c.id === 'd-panel-example')!;
  expect([sample.about,sample.standing,sample.value?.raw,sample.value?.nativeField])
    .toEqual(['d-logger','SOURCE_EXAMPLE','25.91098','PanelTemp']);
  expect(sample.evidence[0]?.sourceId).toBe('d07');
  expect(m.events).toHaveLength(0);
});

test('reference identity and actual installed program/address/status remain UNKNOWN', () => {
  const m = read(fixture());
  const unknown = m.claims.find(c => c.id === 'd-installed')!;
  expect([unknown.about,unknown.standing,unknown.kind]).toEqual(['d-pair','UNKNOWN','unknown']);
  expect(unknown.value).toBeUndefined();
  expect(unknown.reason).toContain('No authenticated assembled operating station');
  expect(m.events).toEqual([]);
  expect(m.claims.filter(c => c.kind === 'literal' && c.standing === 'SOURCE_EXAMPLE')).toHaveLength(1);
});

test('renaming packet-local IDs and display labels cannot change semantic interpretation', () => {
  const p = fixture(), x = structuredClone(p);
  const ids: Record<string,string> = { 'd-pair':'x-arrangement', 'd-logger':'x-controller', 'd-climavue':'x-meteo' };
  x.focus = ids[x.focus];
  x.subjects.forEach((s: any) => { s.id = ids[s.id]; s.label = 'Unrelated label'; });
  x.assertions.forEach((a: any) => {
    a.about = ids[a.about] ?? a.about;
    if (a.target) a.target = ids[a.target] ?? a.target;
  });
  const before = read(p), after = read(x);
  expect(after.accepted).toBe(true);
  expect(after.claims.map(c => [c.concept,c.kind,c.standing,c.value?.raw]))
    .toEqual(before.claims.map(c => [c.concept,c.kind,c.standing,c.value?.raw]));
  expect(after.events).toEqual([]);
});

test('invalid SDI-12 target is rejected by generic source-pointer rules', () => {
  const p = fixture(); assertion(p,'d-connection').target = 'not-in-packet';
  const m = read(p);
  expect(m.accepted).toBe(false);
  expect(m.issues.some(i => i.message.includes('Relationship target'))).toBe(true);
});

test('missing publisher evidence for logger status is rejected', () => {
  const p = fixture(); assertion(p,'d-panel-example').evidence[0].sourceId = 'unlisted-D07';
  const m = read(p);
  expect(m.accepted).toBe(false);
  expect(m.issues.some(i => i.message.includes('Evidence must resolve'))).toBe(true);
});

test('invented actual station serial on explicit UNKNOWN is rejected', () => {
  const p = fixture(); assertion(p,'d-installed').value = {raw:'fake-station-serial'};
  const m = read(p);
  expect(m.accepted).toBe(false);
  expect(m.issues.some(i => i.message.includes('UNKNOWN'))).toBe(true);
});

test('fake performed weather event on reference pair is rejected', () => {
  const p = fixture(); p.originalEvents.push({id:'fake-weather',subject:'d-pair',sourceId:'d02',
    recordLocator:'manual aR7! definition only',nativeField:'aR7! position 8'});
  const m = read(p);
  expect(m.accepted).toBe(false);
  expect(m.issues.some(i => i.message.includes('reference-only'))).toBe(true);
});

test('duplicate assertion ID is rejected without first-value-wins', () => {
  const p = fixture(); p.assertions.push(structuredClone(p.assertions[3]));
  const m = read(p);
  expect(m.accepted).toBe(false);
  expect(m.issues.some(i => i.message.includes('Duplicate assertion ID'))).toBe(true);
});

test('source-FALSE logger reference model promoted to actual identified physical unit passes shape but fails source oracle', () => {
  const p = fixture(); p.subjects.find((s: any) => s.id === 'd-logger').standing = 'SOURCE_IDENTIFIED_EQUIPMENT';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('D-I01/02/17: two separate kinds are not serial-numbered installed station components');
});

test('source-FALSE logger PanelTemp recast as ClimaVue sensor data passes shape, fails original subject', () => {
  const p = fixture(); assertion(p,'d-panel-field').about = 'd-climavue';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('D-S02: PanelTemp is the CR1000X wiring panel, not ClimaVue ambient air');
});

test('source-FALSE published logger Status sample promoted to SOURCE_FACT passes shape but fails evidence standing', () => {
  const p = fixture(); assertion(p,'d-panel-example').standing = 'SOURCE_FACT';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('D-S02/D07: 25.91098 is a separate published logger Status example');
});

test('source-FALSE fourteen response positions turned into fourteen physical components passes pointers, fails evidence', () => {
  const p = fixture();
  for (let i = 1; i <= 14; i++) {
    const id = 'false-sensor-' + i;
    p.subjects.push({id,label:'Invented sensor '+i,standing:'REFERENCE_COMPONENT'});
    p.assertions.push({id:'false-link-'+i,about:'d-pair',concept:'equipment.reference_component',
      standing:'SOURCE_FACT',target:id,evidence:[{sourceId:'d02',locator:'Table 8-1, output position '+i}]});
  }
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('D-R01–14: fourteen aR7! positions cannot establish fourteen additional physical sensors');
});

test('source-FALSE SDI-12 reference design asserted as historical role service passes shape, fails source', () => {
  const p = fixture(); assertion(p,'d-connection').concept = 'equipment.role_service';
  expect(read(p).accepted).toBe(true);
  expect(originalSourceOracle(p))
    .toContain('D-I02/06: potential logger-to-sensor SDI-12 design is not a verified installed relation');
});

test('the selected packet omits thirteen aR7! response fields and thirty Status fields; no actual values are invented', () => {
  const p = fixture(), m = read(p);
  expect(m.accepted).toBe(true);
  expect(originalSourceOracle(p)).toEqual([]);
  expect(p.assertions.filter((x: any) => x.concept === 'output.native_field')).toHaveLength(2);
  expect(p.assertions.filter((x: any) => x.concept === 'output.field_count')).toHaveLength(1);
  expect(p.assertions.filter((x: any) => x.standing === 'SOURCE_EXAMPLE')).toHaveLength(1);
  expect(p.originalEvents).toEqual([]);
  expect(p.representations).toEqual([]);
  // D source sheet has 14 sensor response positions, 31 logger Status fields; packet only selects
  // one response field (position 8) and one example Status field (PanelTemp).
});
