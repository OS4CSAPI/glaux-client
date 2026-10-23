import { afterEach, expect, test, vi } from 'vitest';
import {
  CSAPIQueryBuilder,
  createCSAPIBuilder,
  parseSWEComponent,
} from '@camptocamp/ogc-client/csapi';
import { csapiLibraryStatus } from '../src/data/library';

afterEach(() => {
  vi.unstubAllGlobals();
});

test('the real pinned CSAPI factory builds a systems URL without network access', () => {
  const fetch = vi.fn(() => {
    throw new Error('Network access is forbidden in the offline smoke test.');
  });
  vi.stubGlobal('fetch', fetch);
  const systemsUrl = 'https://example.invalid/systems';
  const builder = createCSAPIBuilder(
    {
      id: 'synthetic-offline-example',
      links: [{
        rel: 'ogc-cs:systems',
        href: systemsUrl,
        type: 'application/json',
        title: 'Synthetic systems',
      }],
    },
    new Map([['systems', systemsUrl]]),
  );

  expect(builder).toBeInstanceOf(CSAPIQueryBuilder);
  expect(builder.availableResources.has('systems')).toBe(true);
  const url = new URL(builder.getSystems({ limit: 2 }));
  expect(url.origin + url.pathname).toBe(systemsUrl);
  expect(url.searchParams.get('limit')).toBe('2');
  expect(csapiLibraryStatus()).toContain('No server is connected');
  expect(fetch).not.toHaveBeenCalled();
});

test('the real CSAPI SWE Common parser preserves a synthetic quantity and its units', () => {
  const quantity = parseSWEComponent({
    type: 'Quantity',
    uom: { code: 'Cel' },
    value: 23.5,
  });

  expect(quantity.type).toBe('Quantity');
  if (quantity.type !== 'Quantity') {
    throw new Error('Expected the CSAPI parser to return a SWE Quantity.');
  }
  expect(quantity.value).toBe(23.5);
  expect(quantity.uom).toEqual({ code: 'Cel' });
});
