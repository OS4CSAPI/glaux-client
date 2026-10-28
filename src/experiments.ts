import type { ExampleOption } from './domain';

interface ExperimentPageMetadata {
  id: string;
  title: string;
  description: string;
  latestUpdate: {
    at: string;
    summary: string;
    commit?: string;
  };
}

export interface ExampleExperimentPage extends ExperimentPageMetadata, ExampleOption {
  kind: 'example';
}

export interface TemplateExperimentPage extends ExperimentPageMetadata {
  kind: 'template';
  id: 'resource-details-template' | 'resource-details-activity' | 'resource-details-smart-citizen';
}

export type ExperimentPage = ExampleExperimentPage | TemplateExperimentPage;

/** Keep page metadata here so the index and example selector stay in agreement.
 * Update the summary and explicit timestamp when a page changes; link a source
 * commit when one is already recorded rather than inventing a future commit ID.
 * A rebuild or deployment alone must not change a page's recorded date.
 */
export const experimentPages: readonly ExperimentPage[] = [
  {
    kind: 'example', id: 'trss', title: 'TRSS ETU-II',
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
    kind: 'example', id: 'core2', title: 'OmniSense Core2',
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
    kind: 'example', id: 'core5', title: 'OmniSense Core5ADS',
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
    kind: 'example', id: 'mpss', title: 'MPSS technical description',
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
    kind: 'example', id: 'power', title: 'Power arrangement',
    label: 'Power arrangement · source replacement',
    url: './fixtures/power-arrangement/manifest.json',
    description: 'Original synthetic profile records: inspect which source supplies the station, a recorded replacement, and the subject of a voltage observation.',
    latestUpdate: {
      at: '2026-10-24T06:00:19-04:00',
      summary: 'Kept rejected relationship endpoints out of equipment selection and clarified supply direction on mobile.',
      commit: 'd74b33dabc5fdfcf22574b8efa7f436b4cf32857',
    },
  },
  {
    kind: 'template', id: 'resource-details-template', title: 'Resource Details View template',
    description: 'The recovered 560 × 440 Resource Details View frame: fixed identity and marking bands, two-level navigation, and a blank canvas with compact overflow scrolling.',
    latestUpdate: {
      at: '2026-10-24T16:24:47-04:00',
      summary: 'Created the initial Resource Details View template from the recovered PBI working frame, with fixed bands and compact overflow scrolling.',
    },
  },
  {
    kind: 'template', id: 'resource-details-smart-citizen', title: 'Smart Citizen Kit 2.3 · DIM research test drive',
    description: 'Explore our 13-step findings in a Resource Details wireframe: documented equipment and procedures versus unverified identities and observations.',
    latestUpdate: {
      at: '2026-10-28T13:13:22-04:00',
      summary: 'Added a source-grounded Smart Citizen case-study walkthrough using the Resource Details template.',
      commit: '6c8010b403c24183d0cfe2e1af5479d0f000284a',
    },
  },
  {
    kind: 'template', id: 'resource-details-activity', title: 'Resource Details View · Activity table',
    description: 'The unchanged Resource Details wireframe with a System-scoped Activity table for Observations, Commands, and System Events, including resource-type filters.',
    latestUpdate: {
      at: '2026-10-26T12:43:36-04:00',
      summary: 'Added the researched Activity table wireframe as a separate page while preserving the blank template.',
    },
  },
];

/** Only data examples appear in the fixture selector and source-read flow. */
export const examplePages: readonly ExampleExperimentPage[] = experimentPages.filter(
  (page): page is ExampleExperimentPage => page.kind === 'example',
);

export const experimentHref = (page: ExperimentPage): string =>
  `/?${page.kind === 'example' ? 'example' : 'page'}=${encodeURIComponent(page.id)}`;
