import type { PowerExampleBundle, PowerExampleRole } from './data/power-example';
import type { PowerModel } from './profile/power';

/** Shared read-only contracts. Original responses stay independent of all interpretations. */
export interface CapturedResource {
  requestedUrl: string;
  url: string;
  retrievedAt: string;
  status: number;
  contentType: string;
  headers: Record<string, string>;
  bytes: Uint8Array;
  text: string;
  json: unknown;
}

export interface StandardFact {
  key: string;
  path: string;
  label: string;
  definition?: string;
  kind: string;
  value: unknown;
  unit?: string;
  codeSpace?: string;
  groupPath: string;
  groupLabel: string;
  groupDefinition?: string;
  subject?: string;
  sourceTime?: string;
  sourceTimeMeaning?: string;
  sourceUrl: string;
  retrievedAt: string;
}

export interface StandardGroup {
  key: string;
  path: string;
  label: string;
  definition?: string;
  kind: string;
  facts: StandardFact[];
}

export interface StandardLink {
  rel: string;
  href: string;
  title?: string;
  mediaType?: string;
  path: string;
  sourceUrl: string;
}

export interface StandardModel {
  id: string;
  name: string;
  resourceType: string;
  uniqueId?: string;
  description?: string;
  groups: StandardGroup[];
  links: StandardLink[];
  captures: CapturedResource[];
  warnings: string[];
  libraryParsed: boolean;
}

export interface PresentedFact {
  key: string;
  label: string;
  value: string;
  notice?: string;
  source: StandardFact;
  mapping: {
    kind: 'mpss' | 'experiment' | 'standard';
    id: string;
    explanation: string;
  };
}

export interface ViewSection {
  id: string;
  title: string;
  description?: string;
  facts: PresentedFact[];
  emptyText?: string;
  heroFactKey?: string;
  collapsible?: boolean;
}

export type DetailsTab = 'overview' | 'equipment' | 'condition';
export type DisplayMode = 'operator' | 'standard';

export interface DetailsModel {
  standard: StandardModel;
  views: Record<DetailsTab, ViewSection[]>;
  interpretationSummary: string;
  interpretationNotes: string[];
  unmappedFactCount: number;
}

export interface ExampleOption {
  id: string;
  label: string;
  url: string;
  description: string;
}

export interface DetailsState {
  loading: boolean;
  error: string | null;
  model: DetailsModel | null;
  examples: readonly ExampleOption[];
  selectedExampleId: string;
  sourceKind: 'synthetic' | 'remote';
  resourceUrl: string;
  mode: DisplayMode;
  tab: DetailsTab;
  libraryStatus: string;
  power: PowerViewState | null;
}

export interface PowerViewState {
  bundle: PowerExampleBundle;
  model: PowerModel;
  at: string;
  selectedRef: string;
  standardRecordRole: PowerExampleRole | 'manifest';
}

export interface DetailsActions {
  selectExample(id: string): void;
  loadResource(url: string): void;
  refresh(): void;
  selectMode(mode: DisplayMode): void;
  selectTab(tab: DetailsTab): void;
  selectPowerTime(time: string): void;
  selectPowerEntity(ref: string): void;
  selectPowerRecord(role: PowerExampleRole | 'manifest'): void;
}
