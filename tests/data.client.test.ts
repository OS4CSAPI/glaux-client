import { expect, test, vi } from 'vitest';
import { captureResource, loadStandardResource, ResourceReadError } from '../src/data/client';

const origin = 'https://example.test/api/systems/0';
const physicalSystem = {
  type: 'PhysicalSystem',
  uniqueId: 'urn:synthetic:system:0',
  label: 'Literal synthetic system',
};

function response(body: string, options: ResponseInit = {}): Response {
  return new Response(body, { headers: { 'content-type': 'application/json' }, ...options });
}

test('captures Fetch-exposed original bytes independently from parsed JSON, including whitespace and unknown fields', async () => {
  const body = '{\r\n  "unknown": {"false":false,"zero":0}, "label":"λ", "escaped":"\\u0061"\r\n}\n';
  const inputBytes = new TextEncoder().encode(body);
  const fetchImpl = vi.fn<typeof fetch>().mockResolvedValue(new Response(inputBytes, {
    headers: { 'content-type': 'application/json; charset=utf-8', 'x-source-test': 'preserved' },
  }));
  const signal = new AbortController().signal;
  const captured = await captureResource(origin, { fetchImpl, signal });
  expect(captured.bytes).toEqual(inputBytes);
  expect(captured.text).toBe(body);
  expect(captured.json).toEqual({ unknown: { false: false, zero: 0 }, label: 'λ', escaped: 'a' });
  expect(captured.headers['x-source-test']).toBe('preserved');
  expect(captured.requestedUrl).toBe(origin);
  expect(captured.url).toBe(origin);
  expect(Number.isNaN(Date.parse(captured.retrievedAt))).toBe(false);
  (captured.json as Record<string, unknown>).changed = true;
  expect(captured.bytes).toEqual(inputBytes);
  expect(captured.text).toBe(body);
  expect(fetchImpl).toHaveBeenCalledExactlyOnceWith(origin, expect.objectContaining({
    method: 'GET', credentials: 'omit', signal,
  }));
  expect(fetchImpl.mock.calls[0][1]?.body).toBeUndefined();
});

test('preserves invalid JSON and a non-JSON HTTP error body in ResourceReadError', async () => {
  const invalid = '{"unknown": unfinished';
  const fetchImpl = vi.fn<typeof fetch>().mockResolvedValue(response(invalid));
  const failure = await captureResource(origin, { fetchImpl }).catch((error: unknown) => error);
  expect(failure).toBeInstanceOf(ResourceReadError);
  expect((failure as ResourceReadError).message).toMatch(/not valid JSON/);
  expect((failure as ResourceReadError).capture?.text).toBe(invalid);
  expect((failure as ResourceReadError).capture?.bytes).toEqual(new TextEncoder().encode(invalid));
  expect((failure as ResourceReadError).capture?.json).toBeUndefined();

  fetchImpl.mockResolvedValue(response('Not here', { status: 404 }));
  const notFound = await captureResource(origin, { fetchImpl }).catch((error: unknown) => error);
  expect((notFound as ResourceReadError).message).toBe('The server returned HTTP 404.');
  expect((notFound as ResourceReadError).capture?.text).toBe('Not here');
});

test('network errors are clear and do not substitute synthetic data', async () => {
  const cause = new TypeError('Network unavailable');
  const fetchImpl = vi.fn<typeof fetch>().mockRejectedValue(cause);
  const error = await captureResource(origin, { fetchImpl }).catch((failure: unknown) => failure);
  expect(error).toBeInstanceOf(ResourceReadError);
  expect((error as ResourceReadError).message).toMatch(/CORS/);
  expect((error as ResourceReadError).cause).toBe(cause);
  expect((error as ResourceReadError).capture).toBeUndefined();
});

test.each([
  'file:///tmp/secret.json',
  'data:application/json,{}',
  'javascript:alert(1)',
  'ftp://example.test/resource',
  'https://user:secret@example.test/resource',
  'https://%75ser@example.test/resource',
  'not an absolute URL',
])('rejects an unsafe or invalid URL without fetching: %s', async (url) => {
  const fetchImpl = vi.fn<typeof fetch>();
  await expect(captureResource(url, { fetchImpl })).rejects.toBeInstanceOf(ResourceReadError);
  expect(fetchImpl).not.toHaveBeenCalled();
});

test('cancellation stops before a read and remains cancellation during a read', async () => {
  const controller = new AbortController();
  controller.abort();
  const fetchImpl = vi.fn<typeof fetch>();
  await expect(captureResource(origin, { fetchImpl, signal: controller.signal })).rejects.toMatchObject({ name: 'AbortError' });
  expect(fetchImpl).not.toHaveBeenCalled();

  const active = new AbortController();
  fetchImpl.mockImplementation(async () => {
    active.abort();
    throw new DOMException('Aborted', 'AbortError');
  });
  await expect(captureResource(origin, { fetchImpl, signal: active.signal })).rejects.toMatchObject({ name: 'AbortError' });
});

test('follows one explicitly advertised relative SensorML alternate and preserves both responses', async () => {
  const firstBody = JSON.stringify({
    type: 'Feature', id: 0,
    properties: { featureType: 'http://www.w3.org/ns/sosa/System', name: 'System 0', unknown: false },
    links: [{ rel: 'alternate', type: 'application/sml+json', href: './0/description' }],
  });
  const secondBody = JSON.stringify({
    ...physicalSystem,
    extension: { vendorField: 0 },
    links: [{ rel: 'describedby', type: 'application/sml+json', href: '/third-resource' }],
  });
  const fetchImpl = vi.fn<typeof fetch>()
    .mockResolvedValueOnce(response(firstBody))
    .mockResolvedValueOnce(response(secondBody));
  const model = await loadStandardResource(origin, { fetchImpl });
  expect(fetchImpl.mock.calls.map(([url]) => url)).toEqual([origin, `${origin}/description`]);
  expect(model.captures.map((capture) => capture.text)).toEqual([firstBody, secondBody]);
  expect(model.id).toBe('0');
  expect(model.uniqueId).toBe(physicalSystem.uniqueId);
  expect(model.resourceType).toBe('PhysicalSystem');
  expect(model.libraryParsed).toBe(true);
  expect(model.links.some((link) => link.href === 'https://example.test/third-resource')).toBe(true);
});

test('does not guess endpoints, follow untyped links, or follow links buried in unknown properties', async () => {
  const fetchImpl = vi.fn<typeof fetch>().mockImplementation(async () => response(JSON.stringify({
    type: 'Feature',
    properties: { vendor: { rel: 'alternate', type: 'application/sml+json', href: '/not-advertised' } },
    links: [{ rel: 'describedby', href: '/details' }, { rel: 'related', type: 'application/sml+json', href: '/another' }],
  })));
  const model = await loadStandardResource(origin, { fetchImpl });
  expect(fetchImpl).toHaveBeenCalledTimes(1);
  expect(model.captures).toHaveLength(1);
  expect(model.links).toHaveLength(3);
});

test('a direct SensorML description needs no additional request', async () => {
  const fetchImpl = vi.fn<typeof fetch>().mockResolvedValue(response(JSON.stringify({
    ...physicalSystem,
    links: [{ rel: 'alternate', type: 'application/sml+json', href: '/other' }],
  })));
  const model = await loadStandardResource(origin, { fetchImpl });
  expect(model.resourceType).toBe('PhysicalSystem');
  expect(fetchImpl).toHaveBeenCalledTimes(1);
});

test('a failed alternate retains the first resource and any received alternate bytes', async () => {
  const fetchImpl = vi.fn<typeof fetch>()
    .mockResolvedValueOnce(response(JSON.stringify({
      type: 'Feature', id: 'original', properties: { name: 'Still available' },
      links: [{ rel: 'alternate', type: 'application/sml+json', href: '/bad' }],
    })))
    .mockResolvedValueOnce(response('Bad JSON'));
  const model = await loadStandardResource(origin, { fetchImpl });
  expect(model.name).toBe('Still available');
  expect(model.id).toBe('original');
  expect(model.captures[1].text).toBe('Bad JSON');
  expect(model.warnings.some((warning) => warning.includes('not valid JSON'))).toBe(true);
});
