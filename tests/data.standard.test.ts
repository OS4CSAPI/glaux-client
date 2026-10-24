import { expect, test } from 'vitest';
import type { CapturedResource, StandardModel } from '../src/domain';
import { extractStandardModel } from '../src/data/standard';

function captured(json: unknown): CapturedResource {
  const text = JSON.stringify(json);
  return {
    requestedUrl: 'https://example.test/systems/zero',
    url: 'https://example.test/systems/zero',
    retrievedAt: '2026-10-23T12:00:00.000Z',
    contentType: 'application/sml+json',
    status: 200,
    headers: { 'content-type': 'application/sml+json' },
    text,
    bytes: new TextEncoder().encode(text),
    json,
  };
}

function facts(model: StandardModel) {
  return model.groups.flatMap((group) => group.facts);
}

test('preserves literal SensorML group definitions, names, values, zero, false, and unknown extensions', () => {
  const json = {
    type: 'PhysicalSystem', uniqueId: 'urn:synthetic:zero', label: 'Literal label',
    characteristics: [{
      id: 'group', definition: 'https://example.test/group/custom', label: 'Literal group label',
      characteristics: [
        { type: 'Quantity', name: 'voltage', label: 'Reported voltage', definition: 'https://example.test/property/voltage', uom: { code: 'V' }, value: 0, extension: { preserved: false } },
        { type: 'Boolean', name: 'flag', label: 'Literal flag', value: false },
        { type: 'Category', name: 'category', value: 'unknown', codeSpace: { href: 'https://example.test/codes' } },
        { type: 'Text', name: 'blank', value: '' },
      ],
    }],
    vendorExtension: { opaque: ['left', 0, false] },
  };
  const original = JSON.stringify(json);
  const resource = captured(json);
  const model = extractStandardModel([resource]);
  const found = facts(model);
  const voltage = found.find((fact) => fact.definition === 'https://example.test/property/voltage');
  expect(voltage).toMatchObject({
    path: '/characteristics/0/characteristics/0', label: 'Reported voltage', kind: 'Quantity', value: 0, unit: 'V',
    groupPath: '/characteristics/0', groupLabel: 'Literal group label', groupDefinition: 'https://example.test/group/custom',
    sourceUrl: resource.url, retrievedAt: resource.retrievedAt, subject: 'urn:synthetic:zero',
  });
  expect(found.find((fact) => fact.label === 'Literal flag')?.value).toBe(false);
  expect(found.find((fact) => fact.label === 'category')?.codeSpace).toBe('https://example.test/codes');
  expect(found.find((fact) => fact.label === 'blank')?.value).toBe('');
  expect(found.find((fact) => fact.path.endsWith('/extension/preserved'))?.value).toBe(false);
  expect(found.find((fact) => fact.path === '/vendorExtension/opaque')?.value).toEqual(['left', 0, false]);
  expect(model.name).toBe('Literal label');
  expect(model.uniqueId).toBe('urn:synthetic:zero');
  expect(model.libraryParsed).toBe(true);
  expect(model.captures[0].json).toBe(json);
  expect(JSON.stringify(json)).toBe(original);
  expect(model.captures[0].bytes).toEqual(new TextEncoder().encode(original));
});

test('extracts capabilities and DataRecord/DataArray schemas and values at exact source paths', () => {
  const model = extractStandardModel([captured({
    type: 'PhysicalSystem', uniqueId: 'urn:synthetic:record', label: 'Records',
    capabilities: [{ definition: 'https://example.test/group/options', label: 'Supplied capability', capabilities: [{
      type: 'DataRecord', name: 'record', label: 'Record label', definition: 'https://example.test/record',
      fields: [
        { name: 'count', type: 'Count', value: 0 },
        { name: 'active', type: 'Boolean', value: false },
        { name: 'samples', type: 'DataArray', label: 'Reported samples',
          elementCount: { type: 'Count', value: 2 },
          elementType: { name: 'voltage', type: 'Quantity', uom: { code: 'V' } },
          encoding: { type: 'JSONEncoding' }, values: [0, 1.5],
        },
      ],
    }] }],
  })]);
  const found = facts(model);
  const path = '/capabilities/0/capabilities/0/fields';
  expect(found.find((fact) => fact.path === `${path}/0`)).toMatchObject({ value: 0, kind: 'Count', groupDefinition: 'https://example.test/record' });
  expect(found.find((fact) => fact.path === `${path}/1`)?.value).toBe(false);
  expect(found.find((fact) => fact.path === `${path}/2`)).toMatchObject({ kind: 'DataArray', value: [0, 1.5] });
  expect(found.find((fact) => fact.path === `${path}/2`)?.unit).toBeUndefined();
  expect(found.find((fact) => fact.path === `${path}/2/elementType`)).toMatchObject({ kind: 'Quantity', value: undefined, unit: 'V' });
  expect(found.find((fact) => fact.path === `${path}/2/elementCount`)?.value).toBe(2);
  expect(found.every((fact) => fact.sourceTime === undefined && fact.subject === 'urn:synthetic:record')).toBe(true);
});

test('extracts properties-wrapped SensorML and ordinary GeoJSON properties without inventing a System identity', () => {
  const wrapped = extractStandardModel([captured({
    type: 'Feature', id: 0,
    properties: { type: 'PhysicalSystem', uniqueId: 'urn:synthetic:wrapped', label: 'Wrapped', characteristics: [{
      label: 'Group', definition: 'https://example.test/group', characteristics: [{ type: 'Text', name: 'text', value: 'Literal' }],
    }] },
  })]);
  expect(wrapped.id).toBe('0');
  expect(wrapped.resourceType).toBe('PhysicalSystem');
  expect(facts(wrapped).find((fact) => fact.path === '/properties/characteristics/0/characteristics/0')?.value).toBe('Literal');

  const ordinary = extractStandardModel([captured({
    type: 'Feature', id: 0, properties: { name: 'Ordinary feature', enabled: false, battery_voltage: 0, 'a/b~c': 'escaped pointer' }, geometry: null,
  })]);
  expect(ordinary.id).toBe('0');
  expect(ordinary.resourceType).toBe('Feature');
  expect(ordinary.libraryParsed).toBe(false);
  expect(facts(ordinary).find((fact) => fact.path === '/properties/battery_voltage')).toMatchObject({ value: 0, unit: undefined, definition: undefined });
  expect(facts(ordinary).find((fact) => fact.path === '/properties/enabled')).toMatchObject({ value: false, subject: '0' });
  expect(facts(ordinary).find((fact) => fact.path === '/properties/a~1b~0c')?.value).toBe('escaped pointer');
});

test('uses the actual CSAPI extractor for recognized featureType and retains properties it does not select', () => {
  const json = {
    type: 'Feature', id: 'sys-0',
    properties: { featureType: 'http://www.w3.org/ns/sosa/System', uid: 'urn:synthetic:sys', name: 'Supplied name', unknownProperty: 0 },
  };
  const model = extractStandardModel([captured(json)]);
  expect(model.resourceType).toBe('System');
  expect(model.libraryParsed).toBe(true);
  expect(model.uniqueId).toBe('urn:synthetic:sys');
  expect(facts(model).find((fact) => fact.path === '/properties/unknownProperty')?.value).toBe(0);
  expect(model.captures[0].json).toEqual(json);
});

test('does not infer units, relationships, identities, or trustworthy time from labels or vendor spellings', () => {
  const model = extractStandardModel([captured({
    manufacturer: 'TRSS OmniSense', model: 'Core 5', batteryVoltage: 12, detector: 'GPS',
    deviceClock: '12/30/99 05:00:00',
    data: { type: 'Count', name: 'remainingBatteryHours', value: 200 },
  })]);
  expect(model.id).toBe('');
  expect(model.uniqueId).toBeUndefined();
  expect(model.name).toBe('Unnamed resource');
  expect(model.resourceType).toBe('JSON');
  expect(model.links).toEqual([]);
  expect(facts(model).every((fact) => fact.unit === undefined && fact.subject === undefined && fact.sourceTime === undefined)).toBe(true);
  expect(facts(model).find((fact) => fact.label === 'deviceClock')?.value).toBe('12/30/99 05:00:00');
  expect(model.warnings).toContain('No resource identifier was supplied.');
});

test('retains explicitly supplied subject and raw source time with its supplied meaning', () => {
  const model = extractStandardModel([captured({
    type: 'DataRecord', label: 'Direct record', subject: { href: 'urn:synthetic:subject' },
    sourceTime: '12/30/99 05:00:00', sourceTimeMeaning: 'Unverified device display clock',
    fields: [{ name: 'voltage', type: 'Quantity', uom: { code: 'V' }, value: 12.2 }],
  })]);
  expect(facts(model).find((fact) => fact.path === '/fields/0')).toMatchObject({
    subject: 'urn:synthetic:subject', sourceTime: '12/30/99 05:00:00', sourceTimeMeaning: 'Unverified device display clock',
  });
  expect(facts(model)[0].sourceTime).not.toBe(model.captures[0].retrievedAt);
});

test('declared process identity supplies the description subject, with explicit and nested process overrides only', () => {
  const model = extractStandardModel([captured({
    type: 'PhysicalSystem', label: 'Parent', uniqueId: 'urn:synthetic:parent',
    characteristics: [{ label: 'Source group', characteristics: [
      { name: 'slotA', type: 'Text', label: 'Detector A', value: 'CPB' },
      { name: 'explicit', type: 'Text', subject: 'urn:synthetic:explicit-subject', value: 'Reported' },
    ] }, {
      label: 'Scoped group', subject: { href: 'urn:synthetic:group-subject' },
      characteristics: [{ name: 'scoped', type: 'Boolean', value: false }],
    }],
    components: [{
      name: 'child', type: 'PhysicalComponent', label: 'Declared child', uniqueId: 'urn:synthetic:child',
      characteristics: [{ label: 'Child group', characteristics: [{ name: 'child-value', type: 'Count', value: 0 }] }],
    }],
  })]);
  const found = facts(model);
  expect(found.find((fact) => fact.label === 'Detector A')?.subject).toBe('urn:synthetic:parent');
  expect(found.find((fact) => fact.label === 'explicit')?.subject).toBe('urn:synthetic:explicit-subject');
  expect(found.find((fact) => fact.label === 'scoped')?.subject).toBe('urn:synthetic:group-subject');
  expect(found.find((fact) => fact.label === 'child-value')?.subject).toBe('urn:synthetic:child');
  expect(found.some((fact) => fact.subject?.includes('slotA'))).toBe(false);
});

test('parser rejections are reported while malformed values and unknown metadata stay inspectable', () => {
  const json = {
    type: 'PhysicalSystem', label: 'Missing unique ID',
    characteristics: [{ label: 'Original', characteristics: [
      { type: 'Quantity', name: 'bad', value: 'not-a-number', extension: 0 },
      { type: 'DataArray', name: 'bad-array', values: [0] },
    ] }],
  };
  const model = extractStandardModel([captured(json)]);
  expect(model.warnings.some((warning) => warning.includes('SensorML parser rejected'))).toBe(true);
  expect(model.warnings.some((warning) => warning.includes('SWE parser rejected'))).toBe(true);
  expect(model.warnings.some((warning) => warning.includes('did not retain the supplied value'))).toBe(true);
  expect(facts(model).find((fact) => fact.label === 'bad')?.value).toBe('not-a-number');
  expect(model.captures[0].json).toEqual(json);
});

test('resolves supplied standard links relative to the response and retains unsafe links only in original JSON', () => {
  const json = { links: [
    { href: '../other', rel: 'related', title: 'Literal title', type: 'application/json' },
    { href: 'javascript:alert(1)', rel: 'alternate' },
    { href: 'https://name:password@example.test/private', rel: 'related' },
  ] };
  const model = extractStandardModel([captured(json)]);
  expect(model.links).toEqual([expect.objectContaining({ href: 'https://example.test/other', rel: 'related', title: 'Literal title', path: '/links/0' })]);
  expect(model.warnings.filter((warning) => warning.includes('not exposed as a navigation link'))).toHaveLength(2);
  expect(model.captures[0].json).toEqual(json);
});

test('an ambiguous scalar response stays inspectable and an empty capture set is an error', () => {
  const model = extractStandardModel([captured(false)]);
  expect(facts(model)[0].value).toBe(false);
  expect(model.id).toBe('');
  expect(model.warnings.some((warning) => warning.includes('not a JSON object'))).toBe(true);
  expect(() => extractStandardModel([])).toThrow('At least one captured response is required.');
});
