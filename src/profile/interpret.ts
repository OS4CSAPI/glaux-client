import type { DetailsModel, DetailsTab, PresentedFact, StandardFact, StandardGroup, StandardModel, ViewSection } from '../domain';
import { EXPERIMENT, MPSS, experimentGroup, experimentTerm, mpssGroup, mpssTerm } from './definitions';

interface TermRule {
  term: string;
  kind: 'Text' | 'Category' | 'Quantity' | 'Count';
  label: string;
  unit?: string;
  repeated?: boolean;
  notice?: string;
  useSourceLabel?: boolean;
}

interface GroupRule {
  group: string;
  tab: DetailsTab;
  title: string;
  description: string;
  terms: TermRule[];
  carrier?: 'characteristics' | 'capabilities';
  required?: string[];
  hero?: string;
  collapsible?: boolean;
  referenceTerms?: string[];
}

const text = (term: string, label: string, notice?: string): TermRule => ({ term, label, kind: 'Text', notice });
const count = (term: string, label: string, notice?: string): TermRule => ({ term, label, kind: 'Count', notice });
const quantity = (term: string, label: string, unit: string, notice?: string): TermRule => ({ term, label, kind: 'Quantity', unit, notice });

// These rules intentionally cover only the first three Details View tabs. The
// experimental rules are not profile additions or inferred vendor semantics.
const experimentRules: GroupRule[] = [
  {
    group: 'source-context', tab: 'overview', title: 'Source context', collapsible: true,
    description: 'Source assertions and limitations supplied with this record.',
    terms: [text('source-document', 'Source document'), text('source-locator', 'Source location'),
      text('assertion-basis', 'Assertion basis'), text('source-time-status', 'Source time'), text('fixture-note', 'Example status')],
  },
  {
    group: 'operational-context', tab: 'overview', title: 'Operational context',
    description: 'Literal source values. These labels do not establish Deployment or other resource relationships.',
    terms: [text('mission-label', 'Mission'), text('sensor-string-label', 'Sensor string'),
      text('source-mode', 'Source mode'), text('source-report-interval', 'Source report interval', 'Literal source notation; no duration conversion is asserted.'),
      text('source-on-time', 'Source on time', 'Literal source notation; no duration conversion is asserted.')],
  },
  {
    group: 'configured-detectors', tab: 'equipment', title: 'Configured detector selection',
    description: 'Selected configuration at a named position. Physical detector identity, connection state, and configuration time are not established.',
    required: ['detector-position', 'selected-detector-type'],
    terms: [text('detector-position', 'Position'), { term: 'selected-detector-type', kind: 'Category', label: 'Selected detector type' },
      quantity('detector-orientation', 'Orientation', 'deg', 'Source angle only. The reference direction is not supplied.')],
  },
  {
    group: 'detector-options', tab: 'equipment', title: 'Supported detector options', carrier: 'capabilities', collapsible: true,
    description: 'Possible choices for this position. Options do not identify installed or active equipment, and do not establish a complete compatibility model.',
    required: ['detector-position', 'supported-detector-type'],
    terms: [text('detector-position', 'Position'), { term: 'supported-detector-type', kind: 'Category', label: 'Supported type', repeated: true },
      text('orientation-constraint', 'Orientation constraint')],
  },
  {
    group: 'reported-transducers', tab: 'equipment', title: 'Reported transducers',
    description: 'Source-reported labels. No individual physical identifiers, connectors, or detection times are supplied.',
    terms: [{ ...text('reported-transducer-label', 'Reported transducer'), repeated: true }],
  },
  {
    group: 'battery-estimate', tab: 'condition', title: 'Battery capacity estimate',
    description: 'A source application estimate. It is not measured state of charge, measured battery voltage, remaining runtime, or operational readiness.',
    hero: 'estimated-capacity-remaining',
    referenceTerms: ['estimator-internal-battery-count', 'estimator-battery-nominal-voltage', 'estimator-external-battery-count', 'estimator-temperature-input', 'reported-message-count', 'reported-time-on'],
    terms: [quantity('estimated-capacity-remaining', 'Estimated capacity remaining', '%', 'Source estimate; inspect the supplied status and inputs.'),
      text('estimate-status', 'Estimate status'), count('estimator-internal-battery-count', 'Internal batteries used by estimator'),
      quantity('estimator-battery-nominal-voltage', 'Nominal voltage used by estimator', 'V', 'A configuration input, not a voltage reading.'),
      count('estimator-external-battery-count', 'External batteries used by estimator'),
      quantity('estimator-temperature-input', 'Temperature used by estimator', 'Cel', 'Estimator input; not an ambient temperature observation.'),
      count('reported-message-count', 'Reported messages'), text('reported-time-on', 'Reported time on')],
  },
  {
    group: 'reported-condition', tab: 'condition', title: 'Reported condition',
    description: 'Historical source values. The raw source clock is unverified and does not establish a current observation.',
    hero: 'reported-battery-voltage',
    terms: [quantity('reported-battery-voltage', 'Reported battery voltage', 'V', 'Voltage only. No charge percentage, remaining runtime, or readiness is derived.'),
      text('voltage-kind', 'Voltage qualifier'), text('unverified-source-clock', 'Unverified source clock', 'Unparsed source text; time zone and clock validity are unknown. Retrieval time is separate.'),
      text('source-mode', 'Source mode'), text('source-report-interval', 'Source report interval', 'Literal source notation; no duration conversion is asserted.'),
      text('source-on-time', 'Source on time', 'Literal source notation; no duration conversion is asserted.')],
  },
  {
    group: 'reported-diagnostics', tab: 'condition', title: 'Reported diagnostic findings',
    description: 'Individual source findings only. No aggregate health or mission readiness is inferred.',
    terms: [{ term: 'diagnostic-finding', kind: 'Category', label: 'Diagnostic finding', useSourceLabel: true, repeated: true }],
  },
];

const technicalRule: GroupRule = {
  group: 'technical-description', tab: 'overview', title: 'Technical description',
  description: 'The bounded MPSS v0.3.5 technical-description binding. Display names are not substituted for these supplied technical terms.',
  terms: [text('manufacturer', 'Manufacturer'), text('model-designation', 'Model designation'),
    text('hardware-revision', 'Hardware revision'), text('firmware-revision', 'Firmware revision')],
};

function validValue(fact: StandardFact, rule: TermRule): boolean {
  if (fact.kind !== rule.kind || (rule.unit !== undefined && fact.unit !== rule.unit)) return false;
  if (rule.kind === 'Category' && fact.codeSpace !== `${EXPERIMENT}codes/${rule.term}`) return false;
  if (rule.kind === 'Quantity') return typeof fact.value === 'number' && Number.isFinite(fact.value);
  if (rule.kind === 'Count') return typeof fact.value === 'number' && Number.isSafeInteger(fact.value) && fact.value >= 0;
  return typeof fact.value === 'string';
}

function displayValue(fact: StandardFact, term: string): string {
  const value = term === 'estimated-capacity-remaining' && typeof fact.value === 'number'
    ? fact.value.toFixed(1) : String(fact.value);
  return fact.unit ? `${value} ${fact.unit}` : value;
}

function record(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function supportedProcessCarrier(group: StandardGroup, standard: StandardModel): boolean {
  const capture = standard.captures.find(item => item.url === group.facts[0]?.sourceUrl);
  if (!capture || capture.status < 200 || capture.status >= 300 || !record(capture.json)) return false;
  const wrapped = group.path.startsWith('/properties/');
  const process = wrapped ? capture.json.properties : capture.json;
  return record(process)
    && ['PhysicalSystem', 'PhysicalComponent', 'SimpleProcess', 'AggregateProcess'].includes(String(process.type))
    && /^\/(?:properties\/)?(?:characteristics|capabilities)\/\d+$/.test(group.path);
}

function sourceNode(sourceUrl: string, path: string, standard: StandardModel): unknown {
  let component: unknown = standard.captures.find(item => item.url === sourceUrl)?.json;
  for (const segment of path.split('/').slice(1)) {
    const key = segment.replace(/~1/g, '/').replace(/~0/g, '~');
    if (Array.isArray(component)) component = component[Number(key)];
    else if (record(component)) component = component[key];
    else return undefined;
  }
  return component;
}

function suppliedNilValue(fact: StandardFact, standard: StandardModel): boolean {
  const component = sourceNode(fact.sourceUrl, fact.path, standard);
  if (!record(component) || !Array.isArray(component.nilValues)) return false;
  return component.nilValues.some(nil => record(nil) && 'value' in nil && String(nil.value) === String(fact.value));
}

/** Interpret explicit bindings without changing the standard model or any capture. */
export function interpretDetails(standard: StandardModel): DetailsModel {
  const views: DetailsModel['views'] = { overview: [], equipment: [], condition: [] };
  const notes: string[] = [];
  const mapped = new Set<string>();
  let mpssCount = 0;
  let experimentCount = 0;

  const interpretGroup = (group: StandardGroup, rule: GroupRule, kind: 'mpss' | 'experiment'): void => {
    const termUri = kind === 'mpss' ? mpssTerm : experimentTerm;
    const expectedCarrier = rule.carrier ?? 'characteristics';
    if (group.kind !== expectedCarrier || !supportedProcessCarrier(group, standard)) {
      notes.push(`${group.label}: the declared binding requires a SensorML ${expectedCarrier} group. Supplied content remains in standard view.`);
      return;
    }
    const suppliedGroup = sourceNode(group.facts[0].sourceUrl, group.path, standard);
    if (kind === 'mpss' && (!record(suppliedGroup) || typeof suppliedGroup.label !== 'string' || suppliedGroup.label.trim() === '')) {
      notes.push(`${group.label}: the MPSS technical-description binding requires a meaningful supplied group label; the incomplete group remains in standard view.`);
      return;
    }
    const accepted = new Map<string, StandardFact[]>();
    for (const term of rule.terms) {
      const candidates = group.facts.filter(fact => fact.definition === termUri(term.term));
      if (!term.repeated && candidates.length > 1) {
        notes.push(`${group.label}: duplicate ${term.term} values are ambiguous; all are retained in standard view.`);
        continue;
      }
      const valid = candidates.filter(fact => {
        // A definition buried in unrelated metadata is not a group member.
        const immediateMember = fact.path.startsWith(`${group.path}/${expectedCarrier}/`)
          && /^\d+$/.test(fact.path.slice(`${group.path}/${expectedCarrier}/`.length));
        const sameSubject = fact.subject === undefined || (standard.uniqueId !== undefined && fact.subject === standard.uniqueId);
        return immediateMember && sameSubject && validValue(fact, term) && !suppliedNilValue(fact, standard);
      });
      if (valid.length !== candidates.length) {
        notes.push(`${group.label}: ${term.term} has an unsupported carrier, subject, type, value, unit, or code space, or a declared nil value; supplied content remains in standard view.`);
      }
      accepted.set(term.term, valid);
    }
    if (rule.required?.some(term => !accepted.get(term)?.length)) {
      notes.push(`${group.label}: required explicit position/selection members are missing or ambiguous; this group remains in standard view.`);
      return;
    }
    const facts: PresentedFact[] = [];
    for (const term of rule.terms) {
      for (const fact of accepted.get(term.term) ?? []) {
        facts.push({
          key: fact.key, label: term.useSourceLabel ? fact.label : term.label,
          value: displayValue(fact, term.term), notice: term.notice, source: fact,
          mapping: {
            kind, id: termUri(term.term),
            explanation: kind === 'mpss'
              ? 'Exact technical-description group, Text term, immediate SensorML member, and per-group cardinality from the unpublished MPSS v0.3.5 catalogue. This is a bounded interpretation, not whole-profile conformance.'
              : 'Explicit application experiment: matched group, term, carrier, value type, and required unit. This definition is not an MPSS binding; the source-to-view mapping records the open profile gap.',
          },
        });
        mapped.add(fact.key);
        if (kind === 'mpss') mpssCount += 1;
        else experimentCount += 1;
      }
    }
    if (facts.length) {
      const referenceUris = new Set((rule.referenceTerms ?? []).map(termUri));
      const primaryFacts = facts.filter(fact => !referenceUris.has(fact.mapping.id));
      const referenceFacts = facts.filter(fact => referenceUris.has(fact.mapping.id));
      const section: ViewSection = {
        id: `${kind}:${group.key}`,
        title: rule.group === 'detector-options'
          ? `${rule.title} · ${facts.find(fact => fact.source.definition === experimentTerm('detector-position'))?.value ?? group.label}`
          : rule.title,
        description: `${rule.description} Source group: ${group.label}.`, facts: primaryFacts,
        collapsible: rule.collapsible,
        heroFactKey: rule.hero ? facts.find(f => f.source.definition === termUri(rule.hero!))?.key : undefined,
      };
      if (primaryFacts.length) views[rule.tab].push(section);
      if (referenceFacts.length) views[rule.tab].push({
        id: `${kind}:${group.key}:reference`, title: 'Estimate inputs and source values',
        description: rule.description, facts: referenceFacts, collapsible: true,
      });
    }
  };

  for (const group of standard.groups) {
    if (group.definition === mpssGroup(technicalRule.group)) interpretGroup(group, technicalRule, 'mpss');
    const rule = experimentRules.find(candidate => group.definition === experimentGroup(candidate.group));
    if (rule) interpretGroup(group, rule, 'experiment');
  }

  const allFacts = standard.groups.flatMap(group => group.facts);
  const unmappedFactCount = allFacts.filter(fact => !mapped.has(fact.key)).length;
  if (experimentCount) notes.unshift('MPSS v0.3.5 does not supply the device-specific bindings used here. The separate experiment namespace makes those prototype choices visible; it does not revise the profile.');
  if (mpssCount) notes.push('The MPSS identifiers are from an unpublished example catalogue. Recognizing the technical-description subset does not establish OGC or whole-profile conformance.');
  const unsupportedBound = allFacts.filter(f => !mapped.has(f.key) && (f.definition?.startsWith(MPSS) || f.definition?.startsWith(EXPERIMENT))).length;
  if (unsupportedBound) notes.push(`${unsupportedBound} fact(s) with MPSS or experiment identifiers have no supported unambiguous view binding. Their original values and definitions remain in standard view.`);
  notes.push('Retrieval timestamps describe HTTP capture only. Missing source time, subject detail, classification marking, physical identity, or condition evidence remains unknown.');

  const empty: Record<DetailsTab, ViewSection> = {
    overview: { id: 'overview-empty', title: 'Overview', facts: [], emptyText: 'No supported explicit overview binding is supplied. Resource identity, standard properties, relationships, and original responses remain available in standard view.' },
    equipment: { id: 'equipment-empty', title: 'Equipment', facts: [], emptyText: 'No supported equipment binding is supplied for this resource. This does not mean no equipment exists.' },
    condition: { id: 'condition-empty', title: 'Condition', facts: [], emptyText: 'No supported condition binding is supplied for this resource. No health, readiness, or battery state is inferred.' },
  };
  for (const tab of ['overview', 'equipment', 'condition'] as const) if (!views[tab].length) views[tab].push(empty[tab]);

  return {
    standard, views, unmappedFactCount,
    interpretationSummary: `${mpssCount} MPSS technical-description fact(s), ${experimentCount} explicit experiment fact(s), and ${unmappedFactCount} other standard fact(s). Both views use the same captured responses.`,
    interpretationNotes: notes,
  };
}
