import { readFileSync } from 'node:fs';
import { expect, test, vi } from 'vitest';
import { buildPacketPresentation } from '../src/profile/source-packet-presentation';

// No added DOM dependency. The test intercepts existing template node creation
// and the shared Map renderer, while exercising the REAL shared packet renderer.
const spy = vi.hoisted(() => ({ mapPositions: [] as unknown[] }));
vi.mock('../src/presentation/resource-details-map', () => ({
  renderResourceMap: (_content: unknown, position: unknown) => {
    spy.mapPositions.push(position);
    return () => {};
  },
}));
vi.mock('../src/presentation/resource-details-template', () => ({
  node: (tag: string, className?: string, text?: string) => ({
    tag, className: className ?? '', textContent: text ?? '', href: '', dataset: {},
    children: [] as unknown[],
    append(...children: unknown[]) { this.children.push(...children); },
  }),
}));
import { renderSourcePacketDetails } from '../src/presentation/source-packet-details';

interface MockElement {
  tag?: string; textContent?: string; children: MockElement[];
  className?: string; dataset?: Record<string,string>;
}
function root(): MockElement {
  return { tag:'root', textContent:'', children:[], append(...children: MockElement[]) { this.children.push(...children); } } as MockElement;
}
function flattened(element: MockElement): string {
  return [element.textContent ?? '', ...(element.children ?? []).map(flattened)].join('\n');
}
const base = new URL('../public/fixtures/source-packets/', import.meta.url);
function packet(name: string): any { return JSON.parse(readFileSync(new URL(name+'.json',base),'utf8')); }
function render(name: string, key: Parameters<typeof renderSourcePacketDetails>[2], mode:'profile'|'generic'='profile') {
  const input=packet(name), projection=buildPacketPresentation(input), content=root();
  renderSourcePacketDetails(content as unknown as HTMLElement,projection,key,mode);
  return { text: flattened(content), input, projection, content };
}

test('existing Resource Details Overview shows declared referent and 2 originals, not 4 observed acts',()=>{
  const {text}=render('bennetts-point.historical.packet','operational/Overview');
  expect(text).toContain("Bennett's Point");
  expect(text).toContain('SOURCE_IDENTIFIED_STATION');
  expect(text).toContain('Original source-report anchors\n2');
  expect(text).toContain('Prior experimental API representations\n4');
  expect(text).toContain('not independently authenticated');
});

test('existing Activity/Table keeps original values, exact QA whitespace and experiment copies separate',()=>{
  const {text}=render('bennetts-point.historical.packet','activity/Table');
  expect(text).toContain('Source-original reports — count each original ONCE');
  expect(text).toContain('CSV line 10130');
  expect(text).toContain('CSV line 10418');
  expect(text).toContain('29.1 °C');
  expect(text).toContain('27.3 °C');
  expect(text).toContain('"<0> "');
  expect(text).toContain('DERIVED — project transformation');
  expect(text).toContain('UNKNOWN — no asserted source value');
  expect(text).toContain('Multiple project resources do not create additional NOAA measurements');
});

test('manufacturer example displayed as SOURCE_EXAMPLE and never counted as performed event',()=>{
  const {text}=render('airgradient.reference.packet','activity/Table');
  expect(text).toContain('No original performed source events are asserted');
  expect(text).toContain('SOURCE_EXAMPLE — published illustration; not actual telemetry');
  expect(text).toContain('27.7 µg/m³');
});

test('same shared Map renderer receives only null for all four source packets',()=>{
  spy.mapPositions.length=0;
  for(const name of ['dragino.reference.packet','airgradient.reference.packet',
    'campbell.reference.packet','bennetts-point.historical.packet']){
    const {text}=render(name,'operational/Map');
    expect(text).toContain('No validated subject-specific geographic position');
  }
  expect(spy.mapPositions).toEqual([null,null,null,null]);
});

test('Management > Record retains complete raw local project packet and whitespace-sensitive tokens',()=>{
  const {text,input}=render('bennetts-point.historical.packet','management/Record');
  expect(text).toContain('Original project packet — complete raw JSON');
  expect(text).toContain('"F_ATemp"');
  expect(text).toContain('"<0> "');
  expect(text).toContain('"DERIVED"');
  expect(text).toContain('"originalEventId"');
  expect(JSON.parse(input && JSON.stringify(input)).assertions.length).toBe(23);
});

test('the generic/raw mode does not claim to render standardized CSAPI resource semantics',()=>{
  const {text}=render('campbell.reference.packet','operational/Equipment','generic');
  expect(text).toContain('Uninterpreted project evidence — not native CSAPI');
  expect(text).toContain('Management → Record and Sources');
  expect(text).not.toContain('Installed');
});

test('structurally accepted but source-false assertion still receives an UNVERIFIED UI banner',()=>{
  const p=packet('airgradient.reference.packet');
  p.subjects[0].standing='SOURCE_IDENTIFIED_EQUIPMENT';
  const projection=buildPacketPresentation(p), content=root();
  renderSourcePacketDetails(content as unknown as HTMLElement,projection,'operational/Overview','profile');
  expect(projection.model.accepted).toBe(true);  // parsing alone is insufficient
  expect(projection.sourceAuthenticated).toBe(false);
  expect(flattened(content)).toContain('not source-authenticated Profile');
});

test('a rejected input keeps its raw record visible rather than manufacturing equipment detail',()=>{
  const p=packet('dragino.reference.packet');
  p.assertions[0].target='nonexistent-reference';
  const projection=buildPacketPresentation(p), content=root();
  renderSourcePacketDetails(content as unknown as HTMLElement,projection,'operational/Equipment','profile');
  expect(projection.model.accepted).toBe(false);
  expect(flattened(content)).toContain('Packet structure or references rejected');
  expect(flattened(content)).toContain('"nonexistent-reference"');
  expect(flattened(content)).not.toContain('Equipment reference and source-identified referents');
});

test('Commands tab never asserts live permissions, actions or physical effects',()=>{
  const {text}=render('dragino.reference.packet','commands/Available');
  expect(text).toContain('No authenticated ControlStream');
  expect(text).toContain('research packet');
});
