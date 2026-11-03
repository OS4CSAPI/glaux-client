import { interpretSourcePacket, type ClaimView, type SourcePacketView } from './source-packet';
import type { ViewKey } from './resource-details-proof';

/**
 * Step 38 bounded UI projection of the SAME Step 33 reader.
 * Local project source packets are NOT native CSAPI responses, a validated
 * Profile carrier, or authenticated publisher claims. All foreign/raw content
 * remains available in the original object and Management > Record.
 */
export interface PacketSourceDocument {
  id: string;
  issuer: string;
  title: string;
  url: string;
  edition: string;
  authority: string;
}
export interface PacketHold { gap: string; topic: string; reason: string; }
export interface PacketPresentation {
  model: SourcePacketView;
  packetId: string;
  sourceDocuments: PacketSourceDocument[];
  holds: PacketHold[];
  originalEventCount: number;
  experimentalRepresentationCount: number;
  /** Neither an issued physical identity nor source authority is independently verified. */
  sourceAuthenticated: false;
  nativeCsapiCarrier: false;
  /** The selected four packets have no validated subject-specific GeoJSON Point. */
  mappablePosition: null;
  warnings: string[];
}
const object = (x: unknown): x is Record<string, unknown> =>
  x !== null && typeof x === 'object' && !Array.isArray(x);
const text = (x: unknown): string => typeof x === 'string' ? x : '';

export function buildPacketPresentation(raw: unknown): PacketPresentation {
  const model = interpretSourcePacket(raw); // one unmodified, source-independent reader
  const docs: PacketSourceDocument[] = [];
  const holds: PacketHold[] = [];
  if (object(raw)) {
    if (Array.isArray(raw.sources)) for (const source of raw.sources) {
      if (!object(source)) continue;
      docs.push({ id: text(source.id), issuer: text(source.issuer), title: text(source.title),
        url: text(source.url), edition: text(source.edition), authority: text(source.authority) });
    }
    if (Array.isArray(raw.holds)) for (const h of raw.holds) {
      if (!object(h)) continue;
      holds.push({ gap: text(h.gap), topic: text(h.topic), reason: text(h.reason) });
    }
  }
  return {
    model, packetId: object(raw) ? text(raw.id) : '', sourceDocuments: docs, holds,
    originalEventCount: model.events.length,
    experimentalRepresentationCount: model.events.reduce((sum, event) => sum + event.copies.length, 0),
    sourceAuthenticated: false, nativeCsapiCarrier: false, mappablePosition: null,
    warnings: [
      'Project-authored research evidence packet — not a native CSAPI response or adopted Profile.',
      'Accepted structure does not authenticate source issuer, claim standing, derived attribution or copy identity.',
      'Source-relative omissions and explicit UNKNOWN values are not zero, current state or proof of nonexistence.',
    ],
  };
}

/** View selection is based on declared assertion CONCEPT, never a vendor/model/name/ID. */
export function packetClaimsForView(presentation: PacketPresentation, view: ViewKey): ClaimView[] {
  const items = presentation.model.claims;
  switch (view) {
    case 'operational/Equipment':
      return items.filter(x => x.concept.startsWith('equipment.') || x.concept === 'identity.installed_unit' ||
        x.concept === 'location.probe_position');
    case 'operational/Communications':
      return items.filter(x => x.concept.startsWith('output.') || x.concept.startsWith('communications.') ||
        x.concept === 'equipment.design_connection');
    case 'operational/Condition':
      return items.filter(x => x.concept.startsWith('power.') ||
        x.concept === 'configuration.effective_setting');
    case 'activity/Table':
      // A source example is inspectable but must never be promoted to an original event.
      return items.filter(x => x.standing === 'SOURCE_EXAMPLE' || presentation.model.events.some(e => e.id === x.about));
    case 'management/Configuration':
      return items.filter(x => x.concept.startsWith('configuration.') || x.concept.startsWith('software.') ||
        x.concept === 'identity.installed_unit');
    case 'management/Sources':
      return items;
    default:
      return [];
  }
}
