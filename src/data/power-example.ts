import type { CapturedResource, StandardModel } from '../domain';
import { captureResource, ResourceReadError, type ResourceReadOptions } from './client';
import { extractStandardModel } from './standard';

/** Roles in this local demonstration's catalogue, not new CSAPI resource types. */
export type PowerExampleRole = 'station' | 'source-a' | 'source-b' | 'deployment' | 'datastream' | 'schema' | 'observation';

export interface PowerExampleRecord {
  role: PowerExampleRole;
  canonicalUrl: string;
  file: string;
  sha256: string;
  mediaType: string;
  /** Explicit catalogue association; never derive a schema route from a stream URL. */
  datastreamRef?: string;
  capture?: CapturedResource;
  standard?: StandardModel;
  error?: string;
}

export interface PowerExampleTime {
  id: 'before' | 'swap' | 'after';
  label: string;
  time: string;
  sourceLocator: string;
}

export interface PowerExampleBundle {
  manifest: CapturedResource;
  records: PowerExampleRecord[];
  times: PowerExampleTime[];
  warnings: string[];
}

const fixtureFiles: Record<PowerExampleRole, string> = {
  station: '02_station.sml.json',
  'source-a': '05_power_a.sml.json',
  'source-b': '06_power_b.sml.json',
  deployment: '08_site_deployment.sml.json',
  datastream: '16_power_stream.json',
  schema: '17_power_schema.json',
  observation: '18_power_observation.json',
};

function object(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function canonicalReference(value: unknown): value is string {
  if (typeof value !== 'string') return false;
  try {
    const url = new URL(value);
    return url.origin === 'https://demo.example' && url.pathname.startsWith('/csapi/')
      && !url.username && !url.password && !url.hash;
  } catch {
    return false;
  }
}

function parseManifest(capture: CapturedResource): Pick<PowerExampleBundle, 'records' | 'times'> {
  const fail = (message: string): never => {
    throw new ResourceReadError(`The bundled power example catalogue is invalid: ${message}`, capture);
  };
  const json = capture.json;
  if (!object(json) || json.kind !== 'glaux-power-arrangement-example/v1') return fail('unknown catalogue format.');
  if (!Array.isArray(json.records) || json.records.length !== Object.keys(fixtureFiles).length) {
    return fail('the seven explicit resource entries are required.');
  }
  const roles = new Set<string>();
  const urls = new Set<string>();
  const records: PowerExampleRecord[] = json.records.map((entry: unknown) => {
    if (!object(entry) || typeof entry.role !== 'string' || !Object.hasOwn(fixtureFiles, entry.role)) {
      return fail('unknown resource role.');
    }
    const role = entry.role as PowerExampleRole;
    if (entry.file !== fixtureFiles[role] || roles.has(role)) return fail('unexpected or duplicate local filename/role.');
    if (!canonicalReference(entry.canonicalUrl) || urls.has(entry.canonicalUrl)) return fail('invalid or duplicate canonical reference.');
    if (typeof entry.sha256 !== 'string' || !/^[a-f0-9]{64}$/.test(entry.sha256)) return fail('missing source fingerprint.');
    if (entry.mediaType !== 'application/sml+json' && entry.mediaType !== 'application/json') return fail('unknown source media type.');
    if (entry.datastreamRef !== undefined && !canonicalReference(entry.datastreamRef)) return fail('invalid explicit stream association.');
    roles.add(role);
    urls.add(entry.canonicalUrl);
    return {
      role, canonicalUrl: entry.canonicalUrl, file: entry.file as string,
      sha256: entry.sha256, mediaType: entry.mediaType,
      ...(typeof entry.datastreamRef === 'string' ? { datastreamRef: entry.datastreamRef } : {}),
    };
  });
  const stream = records.find((entry) => entry.role === 'datastream');
  if (records.find((entry) => entry.role === 'schema')?.datastreamRef !== stream?.canonicalUrl) {
    return fail('the schema must explicitly identify its catalogued stream.');
  }
  if (!Array.isArray(json.times) || json.times.length !== 3) return fail('three source-grounded view times are required.');
  const timeIds = new Set<string>();
  const times: PowerExampleTime[] = json.times.map((entry: unknown) => {
    if (!object(entry) || !['before', 'swap', 'after'].includes(String(entry.id))
      || typeof entry.id !== 'string' || timeIds.has(entry.id)
      || typeof entry.label !== 'string' || !entry.label.trim()
      || typeof entry.time !== 'string' || !Number.isFinite(Date.parse(entry.time))
      || typeof entry.sourceLocator !== 'string' || !entry.sourceLocator.trim()) {
      return fail('a view time is missing its identity, instant or source locator.');
    }
    timeIds.add(entry.id);
    return { id: entry.id as PowerExampleTime['id'], label: entry.label, time: entry.time, sourceLocator: entry.sourceLocator };
  });
  return { records, times };
}

/**
 * Read a fixed local fixture catalogue and its seven sibling files. Canonical
 * demo.example references are identities in that catalogue, never fetch targets.
 * Captures keep the actual local response URL, headers, bytes and retrieval time.
 * Independent standard models avoid assigning every resource the station identity.
 */
export async function loadPowerExample(
  manifestUrl: string,
  options: ResourceReadOptions = {},
): Promise<PowerExampleBundle> {
  const manifest = await captureResource(manifestUrl, options);
  const parsed = parseManifest(manifest);
  const records = await Promise.all(parsed.records.map(async (entry): Promise<PowerExampleRecord> => {
    let capture: CapturedResource | undefined;
    try {
      // The validated filename is a fixed sibling, with no route discovery or link traversal.
      capture = await captureResource(new URL(entry.file, manifest.url).href, options);
      return { ...entry, capture, standard: extractStandardModel([capture]) };
    } catch (cause) {
      options.signal?.throwIfAborted();
      capture = cause instanceof ResourceReadError ? cause.capture : capture;
      let standard: StandardModel | undefined;
      // HTTP/JSON failures can still have an inspectable body. If projection
      // itself failed, keep that original capture without repeating the failure.
      if (capture && cause instanceof ResourceReadError) {
        try {
          standard = extractStandardModel([capture]);
        } catch {
          // The capture remains the independent source of truth.
        }
      }
      return {
        ...entry, capture, standard,
        error: cause instanceof Error ? cause.message : 'The bundled resource could not be read.',
      };
    }
  }));
  options.signal?.throwIfAborted();
  return {
    manifest, records, times: parsed.times,
    warnings: records.flatMap((entry) => entry.error ? [`${entry.role}: ${entry.error}`] : []),
  };
}
