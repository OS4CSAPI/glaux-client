import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { expect, test, vi } from 'vitest';
import { ResourceReadError } from '../src/data/client';
import { loadPowerExample } from '../src/data/power-example';

const fixtureDirectory = new URL('../public/fixtures/power-arrangement/', import.meta.url);
const manifestUrl = 'https://example.test/client/fixtures/power-arrangement/manifest.json';
const originalFiles = [
  '02_station.sml.json', '05_power_a.sml.json', '06_power_b.sml.json',
  '08_site_deployment.sml.json', '16_power_stream.json', '17_power_schema.json',
  '18_power_observation.json',
];
const expectedUrls = [manifestUrl, ...originalFiles.map((file) => new URL(file, manifestUrl).href)];
const originalBodies = new Map(expectedUrls.map((url) => [
  url,
  new Uint8Array(readFileSync(new URL(new URL(url).pathname.split('/').at(-1)!, fixtureDirectory))),
]));

interface Catalogue {
  kind: string;
  records: Array<{
    role: string;
    file: string;
    canonicalUrl: string;
    sha256: string;
    mediaType: string;
    datastreamRef?: string;
  }>;
}

function catalogue(): Catalogue {
  return JSON.parse(readFileSync(new URL('manifest.json', fixtureDirectory), 'utf8')) as Catalogue;
}

function fixtureResponse(url: string, status = 200): Response {
  const body = originalBodies.get(url);
  if (!body) throw new Error(`Unexpected request outside the fixed fixture set: ${url}`);
  return new Response(body.slice(), { status, headers: { 'content-type': 'application/json' } });
}

test('reads only the manifest and seven fixed sibling files; preserves independent identities and original bytes', async () => {
  const fetchImpl = vi.fn<typeof fetch>().mockImplementation(async (input) => fixtureResponse(String(input)));
  const bundle = await loadPowerExample(manifestUrl, { fetchImpl });

  expect(fetchImpl).toHaveBeenCalledTimes(8);
  const requested = fetchImpl.mock.calls.map(([url]) => String(url));
  expect(requested[0]).toBe(manifestUrl);
  expect(new Set(requested)).toEqual(new Set(expectedUrls));
  expect(requested.every((url) => new URL(url).origin === 'https://example.test')).toBe(true);
  for (const [, options] of fetchImpl.mock.calls) {
    expect(options).toMatchObject({ method: 'GET', credentials: 'omit' });
    expect(options?.body).toBeUndefined();
  }

  expect(bundle.manifest.bytes).toEqual(originalBodies.get(manifestUrl));
  expect(bundle.records).toHaveLength(7);
  expect(bundle.warnings).toEqual([]);
  const declared = catalogue();
  for (const entry of bundle.records) {
    const source = declared.records.find((item) => item.role === entry.role)!;
    const localUrl = new URL(source.file, manifestUrl).href;
    expect(entry.error).toBeUndefined();
    expect(entry.canonicalUrl).toBe(source.canonicalUrl);
    expect(entry.capture?.requestedUrl).toBe(localUrl);
    expect(entry.capture?.url).toBe(localUrl);
    expect(entry.capture?.bytes).toEqual(originalBodies.get(localUrl));
    expect(entry.capture?.text).toBe(new TextDecoder().decode(originalBodies.get(localUrl)));
    expect(createHash('sha256').update(entry.capture!.bytes).digest('hex')).toBe(source.sha256);
    expect(entry.standard?.captures).toHaveLength(1);
    expect(entry.standard?.captures[0]).toBe(entry.capture);
  }

  const station = bundle.records.find((entry) => entry.role === 'station')!;
  const sourceA = bundle.records.find((entry) => entry.role === 'source-a')!;
  const sourceB = bundle.records.find((entry) => entry.role === 'source-b')!;
  expect(station.standard).toMatchObject({ id: 'station-01', resourceType: 'PhysicalSystem' });
  expect(sourceA.standard).toMatchObject({ id: 'power-a', resourceType: 'PhysicalComponent' });
  expect(sourceB.standard).toMatchObject({ id: 'power-b', resourceType: 'PhysicalComponent' });
  expect(new Set([station.standard?.uniqueId, sourceA.standard?.uniqueId, sourceB.standard?.uniqueId]).size).toBe(3);
  expect(new Set(bundle.records.map((entry) => entry.standard)).size).toBe(7);
  expect(bundle.records.find((entry) => entry.role === 'deployment')?.standard?.id).toBe('site-01');
  expect(bundle.records.find((entry) => entry.role === 'schema')?.datastreamRef)
    .toBe('https://demo.example/csapi/datastreams/power');

  // These real, unbundled station links remain inspectable but never become requests.
  expect(station.standard?.links.some((link) => link.href === 'https://demo.example/csapi/systems/station-01/datastreams')).toBe(true);
  expect(requested.some((url) => url.startsWith('https://demo.example/'))).toBe(false);
  expect(requested.some((url) => url.includes('/systems/') || url.includes('/schema?'))).toBe(false);
});

test('a failed source response retains its body and error while the other six resources remain available', async () => {
  const failedUrl = new URL('05_power_a.sml.json', manifestUrl).href;
  const fetchImpl = vi.fn<typeof fetch>().mockImplementation(async (input) => {
    const url = String(input);
    // A plausible source body on an HTTP error must still be explicitly marked failed.
    return fixtureResponse(url, url === failedUrl ? 503 : 200);
  });
  const bundle = await loadPowerExample(manifestUrl, { fetchImpl });
  const failed = bundle.records.find((entry) => entry.role === 'source-a')!;
  expect(failed.error).toBe('The server returned HTTP 503.');
  expect(failed.capture?.status).toBe(503);
  expect(failed.capture?.bytes).toEqual(originalBodies.get(failedUrl));
  expect(failed.standard?.id).toBe('power-a');
  expect(failed.standard?.captures[0]).toBe(failed.capture);
  const retained = bundle.records.filter((entry) => entry.role !== 'source-a');
  expect(retained).toHaveLength(6);
  expect(retained.every((entry) => entry.capture?.status === 200 && entry.standard && !entry.error)).toBe(true);
  expect(bundle.warnings).toEqual(['source-a: The server returned HTTP 503.']);
  expect(fetchImpl).toHaveBeenCalledTimes(8);
});

const invalidCatalogues: Array<{ name: string; change: (value: Catalogue) => void }> = [
  { name: 'unknown catalogue format', change: (value) => { value.kind = 'unrecognized-catalogue'; } },
  { name: 'parent-directory traversal', change: (value) => { value.records[0].file = '../02_station.sml.json'; } },
  { name: 'absolute canonical URL as a filename', change: (value) => { value.records[0].file = 'https://demo.example/csapi/systems/station-01'; } },
  { name: 'network-path filename', change: (value) => { value.records[0].file = '//outside.example/source.json'; } },
  { name: 'duplicate canonical identities', change: (value) => { value.records[2].canonicalUrl = value.records[1].canonicalUrl; } },
  { name: 'missing explicit schema association', change: (value) => { delete value.records.find((entry) => entry.role === 'schema')!.datastreamRef; } },
];

test.each(invalidCatalogues)('rejects $name before requesting child records and retains the invalid catalogue', async ({ change }) => {
  const invalid = catalogue();
  change(invalid);
  const body = JSON.stringify(invalid);
  const fetchImpl = vi.fn<typeof fetch>().mockResolvedValue(new Response(body, {
    headers: { 'content-type': 'application/json' },
  }));
  const failure = await loadPowerExample(manifestUrl, { fetchImpl }).catch((error: unknown) => error);
  expect(failure).toBeInstanceOf(ResourceReadError);
  expect((failure as ResourceReadError).message).toMatch(/catalogue is invalid/);
  expect((failure as ResourceReadError).capture?.text).toBe(body);
  expect(fetchImpl).toHaveBeenCalledExactlyOnceWith(manifestUrl, expect.objectContaining({ method: 'GET' }));
});

test('a pre-aborted bundle read makes no requests', async () => {
  const controller = new AbortController();
  controller.abort();
  const fetchImpl = vi.fn<typeof fetch>();
  await expect(loadPowerExample(manifestUrl, { fetchImpl, signal: controller.signal }))
    .rejects.toMatchObject({ name: 'AbortError' });
  expect(fetchImpl).not.toHaveBeenCalled();
});

test('aborting while a child is pending rejects the bundle instead of returning partial success', async () => {
  const controller = new AbortController();
  const pendingUrl = new URL('06_power_b.sml.json', manifestUrl).href;
  let release!: (response: Response) => void;
  let childStarted!: () => void;
  const waiting = new Promise<void>((resolve) => { childStarted = resolve; });
  const fetchImpl = vi.fn<typeof fetch>().mockImplementation(async (input) => {
    const url = String(input);
    if (url === pendingUrl) {
      return new Promise<Response>((resolve) => {
        release = resolve;
        childStarted();
      });
    }
    return fixtureResponse(url);
  });
  const loading = loadPowerExample(manifestUrl, { fetchImpl, signal: controller.signal });
  const rejection = expect(loading).rejects.toMatchObject({ name: 'AbortError' });
  await waiting;
  expect(fetchImpl).toHaveBeenCalledTimes(8);
  controller.abort();
  // Even a transport that completes after abort cannot publish a successful bundle.
  release(fixtureResponse(pendingUrl));
  await rejection;
  expect(fetchImpl.mock.calls.every(([, options]) => options?.signal === controller.signal)).toBe(true);
});
