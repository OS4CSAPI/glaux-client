import { csapiLibraryStatus } from './data/library';
import { loadStandardResource, ResourceReadError } from './data/client';
import { extractStandardModel } from './data/standard';
import type { DetailsActions, DetailsState, ExampleOption } from './domain';
import { interpretDetails } from './profile/interpret';
import { renderDetails } from './presentation/details';
import './presentation/style.css';

const app = document.querySelector<HTMLElement>('#app');
if (!app) {
  throw new Error('The application mount point #app is missing.');
}

const examples: readonly ExampleOption[] = [
  { id: 'trss', label: 'TRSS ETU-II · configuration and estimate', url: './fixtures/trss-etu-ii.json',
    description: 'Synthetic source replay: selected detector configuration, supported options, and battery estimator values.' },
  { id: 'core2', label: 'OmniSense Core2 · reported equipment', url: './fixtures/omnisense-core2.json',
    description: 'Synthetic source replay: five reported transducer labels. No individual physical identities or detection time.' },
  { id: 'core5', label: 'OmniSense Core5ADS · reported condition', url: './fixtures/omnisense-core5ads.json',
    description: 'A separate synthetic source case: 15.43 V DC, individual diagnostics, and an unverified source clock.' },
  { id: 'mpss', label: 'MPSS technical description · contract example', url: './fixtures/mpss-technical-description.json',
    description: 'Fully synthetic manufacturer/model/revision values exercise the bounded MPSS technical-description binding.' },
];

const state: DetailsState = {
  loading: false, error: null, model: null, examples, selectedExampleId: examples[0].id,
  sourceKind: 'synthetic', resourceUrl: '', mode: 'operator', tab: 'overview',
  libraryStatus: csapiLibraryStatus(),
};
let currentRead: AbortController | undefined;
let readVersion = 0;
const mount = app;
const render = (): void => renderDetails(mount, state, actions);

async function read(url: string, clear: boolean): Promise<void> {
  currentRead?.abort();
  currentRead = new AbortController();
  const signal = currentRead.signal;
  const version = ++readVersion;
  state.loading = true;
  state.error = null;
  if (clear) state.model = null;
  render();
  try {
    const standard = await loadStandardResource(url, { signal });
    if (version !== readVersion) return;
    state.model = interpretDetails(standard);
  } catch (error) {
    if (signal.aborted || version !== readVersion) return;
    state.error = error instanceof Error ? error.message : 'The selected source could not be read.';
    if (error instanceof ResourceReadError && error.capture) {
      const standard = extractStandardModel([error.capture]);
      standard.warnings.push(state.error);
      state.model = interpretDetails(standard);
      state.mode = 'standard';
    } else if (!clear && state.model) {
      state.error += ' Showing the previously captured response; it has not been refreshed.';
    }
  } finally {
    if (version === readVersion) {
      state.loading = false;
      render();
    }
  }
}

const actions: DetailsActions = {
  selectExample(id) {
    const example = examples.find(item => item.id === id);
    if (!example) return;
    state.selectedExampleId = id;
    state.sourceKind = 'synthetic';
    void read(new URL(example.url, document.baseURI).href, true);
  },
  loadResource(url) {
    state.resourceUrl = url.trim();
    state.sourceKind = 'remote';
    state.selectedExampleId = '';
    void read(state.resourceUrl, true);
  },
  refresh() {
    if (state.loading) return;
    const url = state.sourceKind === 'synthetic'
      ? new URL(examples.find(item => item.id === state.selectedExampleId)!.url, document.baseURI).href
      : state.resourceUrl;
    void read(url, false);
  },
  selectMode(mode) { state.mode = mode; render(); },
  selectTab(tab) { state.tab = tab; render(); },
};

actions.selectExample(examples[0].id);
