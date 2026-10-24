import type { CapturedResource, StandardModel } from '../domain';
import { extractStandardModel } from './standard';

export interface ResourceReadOptions {
  signal?: AbortSignal;
  fetchImpl?: typeof fetch;
}

/** A failed response remains available to callers, including its original bytes. */
export class ResourceReadError extends Error {
  readonly capture?: CapturedResource;

  constructor(message: string, capture?: CapturedResource, cause?: unknown) {
    super(message, { cause });
    this.name = 'ResourceReadError';
    this.capture = capture;
  }
}

function resourceUrl(input: string): URL {
  let url: URL;
  try {
    const base = typeof location === 'undefined' ? undefined : location.href;
    url = new URL(input, base);
  } catch {
    throw new ResourceReadError('Enter a valid HTTP or HTTPS resource URL.');
  }
  if (url.protocol !== 'http:' && url.protocol !== 'https:') {
    throw new ResourceReadError('Only HTTP and HTTPS resource URLs are supported.');
  }
  if (url.username || url.password) {
    throw new ResourceReadError('Resource URLs must not include a username or password.');
  }
  url.hash = '';
  return url;
}

/**
 * Capture the body exposed by Fetch before parsing. These are response-body bytes,
 * after any browser transport decompression, not a reconstructed JSON download.
 * No cookies or authorization credentials are sent by this boundary.
 */
export async function captureResource(
  input: string,
  options: ResourceReadOptions = {},
): Promise<CapturedResource> {
  const requestedUrl = resourceUrl(input).href;
  options.signal?.throwIfAborted();
  let response: Response;
  try {
    response = await (options.fetchImpl ?? fetch)(requestedUrl, {
      method: 'GET',
      credentials: 'omit',
      headers: { Accept: 'application/sml+json, application/geo+json, application/json' },
      signal: options.signal,
    });
  } catch (cause) {
    options.signal?.throwIfAborted();
    throw new ResourceReadError(
      'The resource could not be read. Check the URL, network connection, and server CORS access.',
      undefined,
      cause,
    );
  }

  // Real Fetch supplies the final URL; test Responses may leave it empty.
  const url = resourceUrl(response.url || requestedUrl).href;
  let bytes: Uint8Array;
  try {
    bytes = new Uint8Array(await response.arrayBuffer());
  } catch (cause) {
    options.signal?.throwIfAborted();
    throw new ResourceReadError('The response body could not be read completely.', undefined, cause);
  }
  options.signal?.throwIfAborted();
  const text = new TextDecoder().decode(bytes);
  const capture: CapturedResource = {
    requestedUrl,
    url,
    retrievedAt: new Date().toISOString(),
    status: response.status,
    contentType: response.headers.get('content-type') ?? '',
    headers: Object.fromEntries(response.headers.entries()),
    bytes,
    text,
    json: undefined,
  };
  let parseError: unknown;
  try {
    capture.json = JSON.parse(text) as unknown;
  } catch (cause) {
    parseError = cause;
  }
  if (!response.ok) {
    throw new ResourceReadError(`The server returned HTTP ${response.status}.`, capture, parseError);
  }
  if (parseError) {
    throw new ResourceReadError('The response body is not valid JSON. The original response was preserved.', capture, parseError);
  }
  return capture;
}

/** Read one supplied resource and, at most, one explicitly advertised SensorML alternate. */
export async function loadStandardResource(
  url: string,
  options: ResourceReadOptions = {},
): Promise<StandardModel> {
  const first = await captureResource(url, options);
  const model = extractStandardModel([first]);
  if (['PhysicalSystem', 'PhysicalComponent', 'SimpleProcess', 'AggregateProcess'].includes(model.resourceType)) {
    return model;
  }

  // No guessed /details, /schema, or format query. Only a supplied, typed link is eligible.
  const candidates = model.links.filter((link) => {
    const relations = link.rel.split(/\s+/);
    const mediaType = link.mediaType?.split(';', 1)[0].trim().toLowerCase();
    return link.sourceUrl === first.url
      && /^\/(?:properties\/)?links\/\d+$/.test(link.path)
      && (relations.includes('alternate') || relations.includes('describedby'))
      && mediaType === 'application/sml+json'
      && resourceUrl(link.href).href !== first.url;
  });
  const alternate = candidates[0];
  if (!alternate) return model;

  try {
    const second = await captureResource(alternate.href, options);
    const combined = extractStandardModel([first, second]);
    if (candidates.length > 1) {
      combined.warnings.push('More than one SensorML alternate was advertised; only the first was read. All advertised links remain available.');
    }
    if (!['PhysicalSystem', 'PhysicalComponent', 'SimpleProcess', 'AggregateProcess'].includes(combined.resourceType)) {
      combined.warnings.push('The advertised SensorML response did not identify a supported SensorML process type. Its original response is retained.');
    }
    return combined;
  } catch (cause) {
    options.signal?.throwIfAborted();
    const captures = cause instanceof ResourceReadError && cause.capture
      ? [first, cause.capture]
      : [first];
    const retained = extractStandardModel(captures);
    retained.warnings.push(`The advertised SensorML description could not be read: ${cause instanceof Error ? cause.message : 'Unknown read error.'}`);
    return retained;
  }
}
