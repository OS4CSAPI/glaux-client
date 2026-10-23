import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import type { CapturedResource, DetailsModel } from '../src/domain';
import { extractStandardModel } from '../src/data/standard';
import { interpretDetails } from '../src/profile/interpret';
import { EXPERIMENT, mpssTerm } from '../src/profile/definitions';

function fixture(name: string): any {
  return JSON.parse(readFileSync(new URL(`../public/fixtures/${name}.json`, import.meta.url), 'utf8'));
}
function capture(json: unknown, suffix = 'record'): CapturedResource {
  const text = JSON.stringify(json);
  return { requestedUrl: `https://example.invalid/${suffix}`, url: `https://example.invalid/${suffix}`,
    retrievedAt: '2026-10-23T12:00:00.000Z', status: 200, contentType: 'application/sml+json',
    headers: { 'content-type': 'application/sml+json' }, text, bytes: new TextEncoder().encode(text), json };
}
function interpret(json: unknown): DetailsModel { return interpretDetails(extractStandardModel([capture(json)])); }
function facts(model: DetailsModel) { return Object.values(model.views).flatMap(sections => sections.flatMap(section => section.facts)); }
function semantics(model: DetailsModel) { return facts(model).map(fact => [fact.mapping.id, fact.value]); }

test('the historical examples use only visible experimental mappings and never masquerade as MPSS bindings', () => {
  for (const name of ['trss-etu-ii', 'omnisense-core2', 'omnisense-core5ads']) {
    const result = interpret(fixture(name));
    expect(facts(result).length).toBeGreaterThan(0);
    expect(facts(result).every(fact => fact.mapping.kind === 'experiment')).toBe(true);
    expect(result.interpretationNotes.join(' ')).toContain('does not supply the device-specific bindings');
  }
});

test('system names, IDs and member labels do not select semantic mappings', () => {
  const original = fixture('trss-etu-ii');
  const renamed = structuredClone(original);
  renamed.id = 'completely-different-id';
  renamed.uniqueId = 'urn:example:renamed';
  renamed.label = 'Different vendor display label';
  for (const group of [...renamed.characteristics, ...renamed.capabilities]) {
    group.label = 'Unrelated group display text';
    for (const member of group.characteristics ?? group.capabilities) member.label = 'Unrelated field display text';
  }
  expect(semantics(interpret(renamed))).toEqual(semantics(interpret(original)));
});

test('familiar labels with unknown identifiers stay available generically without inferred bindings', () => {
  const input = fixture('trss-etu-ii');
  const unknown = JSON.parse(JSON.stringify(input).replaceAll(EXPERIMENT, 'https://example.invalid/unrecognized/'));
  const result = interpret(unknown);
  expect(facts(result)).toHaveLength(0);
  expect(result.standard.groups.flatMap(group => group.facts).some(fact => fact.value === 'SEISMIC/ACOUSTIC')).toBe(true);
  expect(result.standard.captures[0].json).toEqual(unknown);
});

test('configured selections, supported options, and estimator inputs retain their distinct meanings', () => {
  const result = interpret(fixture('trss-etu-ii'));
  expect(result.views.equipment.filter(section => section.title === 'Configured detector selection')).toHaveLength(2);
  expect(result.views.equipment.filter(section => section.title.startsWith('Supported detector options · ')).map(section => section.title))
    .toEqual(['Supported detector options · Detector 1', 'Supported detector options · Detector 2']);
  const all = facts(result);
  expect(all.find(fact => fact.label === 'Orientation')?.value).toBe('0 deg');
  expect(all.find(fact => fact.label === 'Estimated capacity remaining')?.value).toBe('100.0 %');
  expect(all.find(fact => fact.label === 'External batteries used by estimator')?.value).toBe('0');
  expect(all.find(fact => fact.label === 'Reported messages')?.value).toBe('0');
  expect(all.find(fact => fact.label === 'Temperature used by estimator')?.notice).toContain('not an ambient temperature observation');
  expect(all.some(fact => fact.label === 'Reported battery voltage')).toBe(false);
  expect(all.some(fact => fact.label === 'Mission')).toBe(false);
});

test('Core2 equipment and Core5 condition are separate cases with no missing evidence filled in', () => {
  const core2 = interpret(fixture('omnisense-core2'));
  const core5 = interpret(fixture('omnisense-core5ads'));
  expect(core2.views.equipment.flatMap(section => section.facts).map(fact => fact.value))
    .toEqual(['Magnetic', 'Seismic (ext)', 'Detection Switch 1', 'Detection Switch 2', 'Control Switch']);
  expect(core2.views.condition.flatMap(section => section.facts)).toHaveLength(0);
  expect(core5.views.equipment.flatMap(section => section.facts)).toHaveLength(0);
  expect(facts(core5).find(fact => fact.label === 'Reported battery voltage')?.value).toBe('15.43 V');
  expect(facts(core5).find(fact => fact.label === 'Voltage qualifier')?.value).toBe('DC');
  const diagnostics = core5.views.condition.find(section => section.title === 'Reported diagnostic findings')!.facts;
  expect(diagnostics).toHaveLength(6);
  expect(diagnostics.map(fact => fact.label)).toContain('CPB');
  expect(diagnostics.map(fact => fact.label)).not.toContain('GPS');
});

test('the unverified source clock remains literal and never becomes retrieval or observation time', () => {
  const result = interpret(fixture('omnisense-core5ads'));
  const clock = facts(result).find(fact => fact.label === 'Unverified source clock')!;
  expect(clock.value).toBe('12/30/99 05:00:00');
  expect(clock.notice).toContain('Unparsed');
  expect(clock.source.sourceTime).toBeUndefined();
  expect(clock.source.retrievedAt).toBe('2026-10-23T12:00:00.000Z');
  expect(facts(result).some(fact => /remaining runtime|charge percentage/i.test(fact.label))).toBe(false);
});

test('the separate MPSS contract example recognizes four explicit Text terms and no device-label inference', () => {
  const result = interpret(fixture('mpss-technical-description'));
  expect(facts(result)).toHaveLength(4);
  expect(facts(result).every(fact => fact.mapping.kind === 'mpss')).toBe(true);
  expect(result.standard.links.some(link => link.rel === 'profile')).toBe(true);
  expect(facts(interpret(fixture('omnisense-core2'))).some(fact => fact.mapping.id === mpssTerm('model-designation'))).toBe(false);
});

test('conflicting singleton MPSS terms are not resolved by first-value-wins', () => {
  const input = fixture('mpss-technical-description');
  const members = input.characteristics[0].characteristics;
  members.push({ ...members[1], name: 'conflicting_model', value: 'Conflicting model B' });
  const result = interpret(input);
  expect(facts(result).some(fact => fact.mapping.id === mpssTerm('model-designation'))).toBe(false);
  expect(result.interpretationNotes.join(' ')).toContain('duplicate model-designation');
  expect(result.standard.groups.flatMap(group => group.facts).filter(fact => fact.definition === mpssTerm('model-designation')).map(fact => fact.value))
    .toEqual(['Synthetic Bench Model A', 'Conflicting model B']);
});

test('wrong MPSS type, wrong group, and non-SensorML carrier do not earn profile interpretation', () => {
  const wrongType = fixture('mpss-technical-description');
  wrongType.characteristics[0].characteristics.forEach((member: any) => { member.type = 'Category'; });
  expect(facts(interpret(wrongType))).toHaveLength(0);
  const wrongGroup = fixture('mpss-technical-description');
  wrongGroup.characteristics[0].definition = 'https://example.invalid/other-group';
  expect(facts(interpret(wrongGroup))).toHaveLength(0);
  const wrongCarrier = fixture('mpss-technical-description');
  wrongCarrier.type = 'UnrelatedJSON';
  expect(facts(interpret(wrongCarrier))).toHaveLength(0);
});

test('incorrect quantity units and missing required selection context are retained without reinterpretation', () => {
  const input = fixture('trss-etu-ii');
  const estimate = input.characteristics.find((group: any) => group.id === 'battery-estimate');
  estimate.characteristics[0].uom.code = 'V';
  const selection = input.characteristics.find((group: any) => group.id === 'configured-detector-1');
  selection.characteristics = selection.characteristics.filter((member: any) => !member.definition.endsWith('/detector-position'));
  const result = interpret(input);
  expect(facts(result).some(fact => fact.label === 'Estimated capacity remaining')).toBe(false);
  expect(result.views.equipment.filter(section => section.title === 'Configured detector selection')).toHaveLength(1);
  expect(result.interpretationNotes.join(' ')).toContain('missing or ambiguous');
  expect(result.standard.captures[0].json).toEqual(input);
});

test('an alternate describing a different declared subject cannot populate the first system operator card', () => {
  const first = fixture('omnisense-core2');
  const second = fixture('omnisense-core5ads');
  const standard = extractStandardModel([capture(first, 'first'), capture(second, 'second')]);
  const result = interpretDetails(standard);
  expect(result.views.condition.flatMap(section => section.facts)).toHaveLength(0);
  expect(standard.captures).toHaveLength(2);
  expect(standard.groups.flatMap(group => group.facts).some(fact => fact.value === 15.43)).toBe(true);
  expect(result.interpretationNotes.join(' ')).toContain('subject');
});

test('interpretation leaves source JSON, bytes and standard facts unchanged, including unknown extensions', () => {
  const input = fixture('trss-etu-ii');
  input.unknownExtension = { preserved: false, count: 0, empty: '', nested: ['x', 7] };
  const standard = extractStandardModel([capture(input)]);
  const before = JSON.stringify(standard);
  const result = interpretDetails(standard);
  expect(result.standard).toBe(standard);
  expect(JSON.stringify(standard)).toBe(before);
  expect(standard.captures[0].json).toEqual(input);
  expect(new TextDecoder().decode(standard.captures[0].bytes)).toBe(standard.captures[0].text);
});

test('declared nil tokens and foreign code spaces remain source data rather than physical readings or selected types', () => {
  const input = fixture('omnisense-core5ads');
  const voltage = input.characteristics[1].characteristics[0];
  voltage.value = -9999;
  voltage.nilValues = [{ value: '-9999', reason: 'urn:example:no-reading' }];
  const result = interpret(input);
  expect(facts(result).some(fact => fact.label === 'Reported battery voltage')).toBe(false);
  expect(result.standard.captures[0].json).toEqual(input);
  const trss = fixture('trss-etu-ii');
  trss.characteristics[2].characteristics[1].codeSpace = 'https://example.invalid/foreign-vocabulary';
  expect(interpret(trss).views.equipment.filter(section => section.title === 'Configured detector selection')).toHaveLength(1);
});

test('estimate status comes from the selected source and no fixed collection state is invented', () => {
  const input = fixture('trss-etu-ii');
  const group = input.characteristics.find((item: any) => item.id === 'battery-estimate');
  group.characteristics.find((member: any) => member.definition.endsWith('/estimate-status')).value = 'A different supplied estimator state';
  const result = interpret(input);
  const estimate = facts(result).find(fact => fact.label === 'Estimated capacity remaining')!;
  expect(estimate.notice).not.toMatch(/collecting|in progress/);
  expect(facts(result).find(fact => fact.label === 'Estimate status')?.value).toBe('A different supplied estimator state');
});

test('separate valid MPSS groups preserve their supplied context without inventing a global singleton rule', () => {
  const input = fixture('mpss-technical-description');
  const second = structuredClone(input.characteristics[0]);
  second.id = 'alternate-technical-context'; second.label = 'Other supplied technical context';
  second.characteristics = [second.characteristics[1]];
  second.characteristics[0].value = 'Synthetic model in another context';
  input.characteristics.push(second);
  const result = interpret(input);
  expect(facts(result)).toHaveLength(5);
  expect(result.views.overview[1].description).toContain('Other supplied technical context');
});

test('a missing or blank MPSS group label remains incomplete instead of borrowing a renderer fallback', () => {
  const input = fixture('mpss-technical-description');
  delete input.characteristics[0].label;
  expect(facts(interpret(input))).toHaveLength(0);
  input.characteristics[0].label = '   ';
  expect(facts(interpret(input))).toHaveLength(0);
});

test('a failed HTTP response stays inspectable but cannot supply an operator reading', () => {
  const response = capture(fixture('omnisense-core5ads'));
  response.status = 500;
  const result = interpretDetails(extractStandardModel([response]));
  expect(facts(result)).toHaveLength(0);
  expect(result.standard.captures[0].status).toBe(500);
  expect(result.standard.groups.flatMap(group => group.facts).some(fact => fact.value === 15.43)).toBe(true);
});

test('an unknown viewed-process identity does not authorize an explicitly different subject', () => {
  const input = fixture('omnisense-core5ads');
  delete input.uniqueId;
  input.characteristics[1].characteristics[0].subject = 'urn:example:some-other-system';
  const result = interpret(input);
  expect(facts(result).some(fact => fact.label === 'Reported battery voltage')).toBe(false);
  expect(result.interpretationNotes.join(' ')).toContain('subject');
  expect(result.standard.groups.flatMap(group => group.facts).some(fact => fact.value === 15.43 && fact.subject === 'urn:example:some-other-system')).toBe(true);
});
