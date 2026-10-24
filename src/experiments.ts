import type { ExampleOption } from './domain';

export interface ExperimentPage extends ExampleOption {
  title: string;
  latestUpdate: {
    at: string;
    summary: string;
    commit?: string;
  };
}

/** Keep page metadata here so the index and example selector stay in agreement.
 * Update the summary and explicit timestamp when a page changes; link a source
 * commit when one is already recorded rather than inventing a future commit ID.
 * a rebuild or deployment alone must not change an example's recorded date.
 */
export const experimentPages: readonly ExperimentPage[] = [
  {
    id: 'trss', title: 'TRSS ETU-II',
    label: 'TRSS ETU-II · configuration and estimate',
    url: './fixtures/trss-etu-ii.json',
    description: 'Synthetic source replay: selected detector configuration, supported options, and battery estimator values.',
    latestUpdate: {
      at: '2026-10-24T05:50:09-04:00',
      summary: 'Added a direct page link and a description of the configuration-and-estimate example.',
      commit: '64e2287b8b6366eed7fdf0bd83ca502997caeb9d',
    },
  },
  {
    id: 'core2', title: 'OmniSense Core2',
    label: 'OmniSense Core2 · reported equipment',
    url: './fixtures/omnisense-core2.json',
    description: 'Synthetic source replay: five reported transducer labels. No individual physical identities or detection time.',
    latestUpdate: {
      at: '2026-10-24T05:50:09-04:00',
      summary: 'Added a direct page link and a description of the reported-equipment example.',
      commit: '64e2287b8b6366eed7fdf0bd83ca502997caeb9d',
    },
  },
  {
    id: 'core5', title: 'OmniSense Core5ADS',
    label: 'OmniSense Core5ADS · reported condition',
    url: './fixtures/omnisense-core5ads.json',
    description: 'A separate synthetic source case: 15.43 V DC, individual diagnostics, and an unverified source clock.',
    latestUpdate: {
      at: '2026-10-24T05:50:09-04:00',
      summary: 'Added a direct page link and a description of the reported-condition example.',
      commit: '64e2287b8b6366eed7fdf0bd83ca502997caeb9d',
    },
  },
  {
    id: 'mpss', title: 'MPSS technical description',
    label: 'MPSS technical description · contract example',
    url: './fixtures/mpss-technical-description.json',
    description: 'Fully synthetic manufacturer/model/revision values exercise the bounded MPSS technical-description binding.',
    latestUpdate: {
      at: '2026-10-24T05:50:09-04:00',
      summary: 'Added a direct page link and a description of the technical-description contract example.',
      commit: '64e2287b8b6366eed7fdf0bd83ca502997caeb9d',
    },
  },
  {
    id: 'power', title: 'Power arrangement',
    label: 'Power arrangement · source replacement',
    url: './fixtures/power-arrangement/manifest.json',
    description: 'Original synthetic profile records: inspect which source supplies the station, a recorded replacement, and the subject of a voltage observation.',
    latestUpdate: {
      at: '2026-10-24T06:00:19-04:00',
      summary: 'Kept rejected relationship endpoints out of equipment selection and clarified supply direction on mobile.',
      commit: 'd74b33dabc5fdfcf22574b8efa7f436b4cf32857',
    },
  },
];

export const experimentHref = (id: string): string => `/?example=${encodeURIComponent(id)}`;
