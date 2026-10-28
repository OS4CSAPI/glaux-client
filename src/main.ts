import { csapiLibraryStatus } from './data/library';
import { loadStandardResource, ResourceReadError } from './data/client';
import { extractStandardModel } from './data/standard';
import { loadPowerExample, type PowerExampleBundle } from './data/power-example';
import type { DetailsActions, DetailsState } from './domain';
import { examplePages, experimentPages } from './experiments';
import { interpretDetails } from './profile/interpret';
import { derivePowerModel, type PowerModel } from './profile/power';
import { renderDetails } from './presentation/details';
import { renderExperimentIndex } from './presentation/index';
import { renderResourceDetailsActivity } from './presentation/resource-details-activity';
import { renderResourceDetailsTemplate } from './presentation/resource-details-template';
import { renderResourceDetailsSmartCitizen } from './presentation/resource-details-smart-citizen';
import { renderResourceDetailsProfileTest } from './presentation/resource-details-profile-test';
import './presentation/style.css';

const app = document.querySelector<HTMLElement>('#app');
if (!app) {
  throw new Error('The application mount point #app is missing.');
}

const examples = examplePages;

const state: DetailsState = {
  loading: false, error: null, model: null, examples, selectedExampleId: examples[0].id,
  sourceKind: 'synthetic', resourceUrl: '', mode: 'operator', tab: 'overview',
  libraryStatus: csapiLibraryStatus(),
  power: null,
};
let currentRead: AbortController | undefined;
let readVersion = 0;
const mount = app;
const render = (): void => renderDetails(mount, state, actions);

function powerAt(bundle: PowerExampleBundle, at: string): PowerModel {
  return derivePowerModel(bundle.records, {
    at,
    deploymentRef: bundle.records.find(record => record.role === 'deployment')?.canonicalUrl,
  });
}

function supplyAt(bundle: PowerExampleBundle, model: PowerModel): string {
  const station = bundle.records.find(record => record.role === 'station')?.canonicalUrl ?? '';
  const supply = model.relationships.find(relationship => relationship.kind === 'powers'
    && relationship.status === 'valid' && relationship.applicability === 'applicable'
    && relationship.object?.resolvedRef === station);
  return supply?.subject?.resolvedRef ?? station;
}

async function read(url: string, clear: boolean): Promise<void> {
  currentRead?.abort();
  currentRead = new AbortController();
  const signal = currentRead.signal;
  const version = ++readVersion;
  state.loading = true;
  state.error = null;
  const previousPower = state.power;
  const isPower = state.sourceKind === 'synthetic' && state.selectedExampleId === 'power';
  if (clear) { state.model = null; state.power = null; }
  render();
  try {
    if (isPower) {
      const bundle = await loadPowerExample(url, { signal });
      if (version !== readVersion) return;
      const at = !clear && previousPower ? previousPower.at
        : (bundle.times.find(time => time.id === 'after') ?? bundle.times[0]).time;
      const model = powerAt(bundle, at);
      const station = bundle.records.find(record => record.role === 'station');
      state.model = interpretDetails(station?.standard ?? extractStandardModel([bundle.manifest]));
      state.power = {
        bundle, model, at,
        selectedRef: !clear && previousPower && model.entities.some(entity => entity.ref === previousPower.selectedRef)
          ? previousPower.selectedRef : supplyAt(bundle, model),
        standardRecordRole: !clear && previousPower ? previousPower.standardRecordRole : 'station',
      };
      if (!station?.standard || station.error) state.error = 'The station record is unavailable. Related captures and their notices remain inspectable.';
    } else {
      const standard = await loadStandardResource(url, { signal });
      if (version !== readVersion) return;
      state.model = interpretDetails(standard);
      state.power = null;
    }
  } catch (error) {
    if (signal.aborted || version !== readVersion) return;
    state.error = error instanceof Error ? error.message : 'The selected source could not be read.';
    if (error instanceof ResourceReadError && error.capture) {
      state.power = null;
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
    const pageUrl = new URL(location.href);
    pageUrl.searchParams.delete('page');
    pageUrl.searchParams.set('example', id);
    history.replaceState(null, '', pageUrl);
    document.title = `${example.title} | Glaux Client`;
    state.selectedExampleId = id;
    state.sourceKind = 'synthetic';
    if (id === 'power') { state.tab = 'overview'; state.mode = 'operator'; }
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
  selectPowerTime(at) {
    const power = state.power;
    if (!power || state.loading || !power.bundle.times.some(time => time.time === at)) return;
    power.at = at;
    power.model = powerAt(power.bundle, at);
    power.selectedRef = supplyAt(power.bundle, power.model);
    render();
  },
  selectPowerEntity(ref) {
    if (!state.power || !state.power.model.entities.some(entity => entity.ref === ref)) return;
    state.power.selectedRef = ref;
    render();
  },
  selectPowerRecord(role) {
    if (!state.power || role !== 'manifest' && !state.power.bundle.records.some(record => record.role === role)) return;
    state.power.standardRecordRole = role;
    state.mode = 'standard';
    render();
  },
};

const parameters = new URLSearchParams(location.search);
const requestedPage = parameters.get('page');
const requestedExample = parameters.get('example');
const selectedTemplate = experimentPages.find(page => page.kind === 'template' && page.id === requestedPage);
const selectedExample = examples.find(example => example.id === requestedExample);
if (selectedTemplate) {
  document.title = `${selectedTemplate.title} | Glaux Client`;
  if (selectedTemplate.id === 'resource-details-profile-test') renderResourceDetailsProfileTest(mount);
  else if (selectedTemplate.id === 'resource-details-smart-citizen') renderResourceDetailsSmartCitizen(mount);
  else if (selectedTemplate.id === 'resource-details-activity') renderResourceDetailsActivity(mount);
  else renderResourceDetailsTemplate(mount);
} else if (requestedPage === null && selectedExample) actions.selectExample(selectedExample.id);
else {
  document.title = 'Experiment index | Glaux Client';
  renderExperimentIndex(mount, requestedPage !== null || requestedExample !== null);
}
