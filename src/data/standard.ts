import {
  extractCSAPIFeature,
  getCSAPIResourceType,
  parseSensorML30,
  parseSWEComponent,
} from '@camptocamp/ogc-client/csapi';
import type { CapturedResource, StandardFact, StandardGroup, StandardLink, StandardModel } from '../domain';

type JsonRecord = Record<string, unknown>;
const processTypes = new Set(['PhysicalSystem', 'PhysicalComponent', 'SimpleProcess', 'AggregateProcess']);
const scalarTypes = new Set(['Quantity', 'Count', 'Boolean', 'Text', 'Time', 'Category', 'QuantityRange', 'CountRange', 'TimeRange', 'CategoryRange']);
const complexTypes = new Set(['DataRecord', 'DataArray', 'Vector', 'Matrix', 'DataChoice', 'Geometry']);
const componentMetadata = new Set([
  'type', 'name', 'id', 'label', 'definition', 'description', 'value', 'values', 'uom', 'codeSpace',
  'subject', 'sourceTime', 'sourceTimeMeaning', 'phenomenonTime', 'resultTime',
]);

function record(value: unknown): value is JsonRecord {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function string(value: unknown): string | undefined {
  return typeof value === 'string' ? value : undefined;
}

function identifier(value: unknown): string | undefined {
  return typeof value === 'string' || typeof value === 'number' ? String(value) : undefined;
}

function pointer(parent: string, key: string | number): string {
  return `${parent}/${String(key).replace(/~/g, '~0').replace(/\//g, '~1')}`;
}

function suppliedLabel(value: JsonRecord, fallback: string): string {
  return string(value.label) ?? string(value.name) ?? fallback;
}

function suppliedReference(value: unknown): string | undefined {
  return string(value) ?? (record(value) ? string(value.href) : undefined);
}

interface SourceContext {
  subject?: string;
  sourceTime?: string;
  sourceTimeMeaning?: string;
}

function suppliedContext(value: JsonRecord, inherited: SourceContext = {}): SourceContext {
  const context = { ...inherited };
  const subject = suppliedReference(value.subject);
  // A SensorML description's characteristics describe its declared process.
  // Use its supplied unique ID, never an ID manufactured from a label or slot.
  const processSubject = typeof value.type === 'string' && processTypes.has(value.type)
    ? string(value.uniqueId)
    : undefined;
  const featureSubject = value.type === 'Feature' && record(value.properties)
    ? (getCSAPIResourceType(value) ? string(value.properties.uid) : undefined) ?? identifier(value.id)
    : undefined;
  const declaredSubject = subject ?? processSubject ?? featureSubject;
  if (declaredSubject !== undefined) context.subject = declaredSubject;
  // Literal time values are never parsed, corrected, or replaced by retrieval time.
  if (typeof value.sourceTime === 'string') {
    context.sourceTime = value.sourceTime;
    context.sourceTimeMeaning = string(value.sourceTimeMeaning);
  } else if (typeof value.phenomenonTime === 'string') {
    context.sourceTime = value.phenomenonTime;
    context.sourceTimeMeaning = 'phenomenonTime';
  } else if (typeof value.resultTime === 'string') {
    context.sourceTime = value.resultTime;
    context.sourceTimeMeaning = 'resultTime';
  }
  return context;
}

/**
 * Generic extraction uses supplied standard types and fields only. All paths are
 * JSON Pointers into a capture's original JSON; SWE fact paths identify components.
 * The library's selected/normalized properties never replace captured JSON or bytes.
 */
export function extractStandardModel(captures: CapturedResource[]): StandardModel {
  if (captures.length === 0) throw new Error('At least one captured response is required.');
  const model: StandardModel = {
    id: '',
    name: '',
    resourceType: 'JSON',
    groups: [],
    links: [],
    captures: [...captures],
    warnings: [],
    libraryParsed: false,
  };

  for (const [captureIndex, capture] of captures.entries()) {
    const keyFor = (path: string): string => `${captureIndex}:${capture.url}#${path}`;
    const warn = (path: string, message: string): void => {
      model.warnings.push(`${capture.url}${path ? ` at ${path}` : ''}: ${message}`);
    };
    const addGroup = (path: string, label: string, kind: string, definition?: string): StandardGroup => {
      const group: StandardGroup = { key: keyFor(path), path, label, kind, definition, facts: [] };
      model.groups.push(group);
      return group;
    };
    const addFact = (
      value: unknown,
      path: string,
      label: string,
      kind: string,
      group: StandardGroup,
      metadata: JsonRecord = {},
      context: SourceContext = {},
    ): void => {
      const unit = record(metadata.uom)
        ? string(metadata.uom.code) ?? string(metadata.uom.href)
        : undefined;
      const codeSpace = suppliedReference(metadata.codeSpace);
      const fact: StandardFact = {
        key: keyFor(path), path, label, kind, value,
        definition: string(metadata.definition),
        unit, codeSpace,
        groupPath: group.path,
        groupLabel: group.label,
        groupDefinition: group.definition,
        ...context,
        sourceUrl: capture.url,
        retrievedAt: capture.retrievedAt,
      };
      group.facts.push(fact);
    };

    const collectLinks = (value: unknown, path: string, depth = 0): void => {
      if (depth > 64) return;
      if (Array.isArray(value)) {
        value.forEach((item, index) => collectLinks(item, pointer(path, index), depth + 1));
        return;
      }
      if (!record(value)) return;
      if (typeof value.href === 'string') {
        try {
          const resolved = new URL(value.href, capture.url);
          if (!['http:', 'https:'].includes(resolved.protocol) || resolved.username || resolved.password) {
            warn(path, 'A non-HTTP(S) or credential-bearing link is retained in the original JSON but is not exposed as a navigation link.');
          } else {
            const link: StandardLink = {
              rel: string(value.rel) ?? '',
              href: resolved.href,
              title: string(value.title),
              mediaType: string(value.type) ?? string(value.mediaType) ?? string(value.rt),
              path,
              sourceUrl: capture.url,
            };
            model.links.push(link);
          }
        } catch {
          warn(path, 'An invalid link is retained in the original JSON.');
        }
      }
      for (const [key, child] of Object.entries(value)) collectLinks(child, pointer(path, key), depth + 1);
    };

    const walk = (
      value: unknown,
      path: string,
      label: string,
      group: StandardGroup,
      context: SourceContext,
      depth = 0,
    ): void => {
      if (depth > 64) {
        warn(path, 'Nested content exceeds the extraction depth; it remains available as JSON.');
        addFact(value, path, label, 'JSON', group, {}, context);
        return;
      }
      if (Array.isArray(value)) {
        if (value.every((item) => !record(item) && !Array.isArray(item))) {
          addFact(value, path, label, 'JSON array', group, {}, context);
        } else {
          value.forEach((item, index) => walk(item, pointer(path, index), `${label}[${index}]`, group, context, depth + 1));
        }
        return;
      }
      if (!record(value)) {
        addFact(value, path, label, value === null ? 'null' : typeof value, group, {}, context);
        return;
      }

      const ownContext = suppliedContext(value, context);
      const type = string(value.type);
      const ownLabel = suppliedLabel(value, label);
      let kind = type;
      if (type && (scalarTypes.has(type) || complexTypes.has(type))) {
        try {
          const parsed = parseSWEComponent(value);
          kind = parsed.type;
          model.libraryParsed = true;
          if (Object.hasOwn(value, 'value') && !Object.hasOwn(parsed, 'value')) {
            warn(path, 'The pinned SWE parser did not retain the supplied value; the original value is displayed.');
          }
        } catch (error) {
          warn(path, `The pinned SWE parser rejected this component: ${error instanceof Error ? error.message : String(error)}. Its supplied content is retained.`);
        }
        if (type === 'DataRecord') {
          const nested = addGroup(path, ownLabel, kind ?? type, string(value.definition));
          if (Array.isArray(value.fields)) {
            value.fields.forEach((field, index) => walk(field, pointer(pointer(path, 'fields'), index), `fields[${index}]`, nested, ownContext, depth + 1));
          } else {
            addFact(value, path, ownLabel, type, nested, value, ownContext);
          }
          for (const [key, child] of Object.entries(value)) {
            if (!componentMetadata.has(key) && key !== 'fields') walk(child, pointer(path, key), key, nested, ownContext, depth + 1);
          }
          return;
        }
        if (type === 'DataArray') {
          // Do not reinterpret encoded rows, expand implicit observations, or invent sample times.
          addFact(value.values, path, ownLabel, kind ?? type, group, value, ownContext);
          for (const [key, child] of Object.entries(value)) {
            if (!componentMetadata.has(key)) walk(child, pointer(path, key), key, group, ownContext, depth + 1);
          }
          return;
        }
        if (scalarTypes.has(type)) {
          addFact(value.value, path, ownLabel, kind ?? type, group, value, ownContext);
          for (const [key, child] of Object.entries(value)) {
            if (!componentMetadata.has(key)) walk(child, pointer(path, key), key, group, ownContext, depth + 1);
          }
          return;
        }
      }

      // Other typed/unknown JSON is still rendered literally, never classified by a label.
      if (Object.keys(value).length === 0) addFact(value, path, ownLabel, 'JSON object', group, {}, ownContext);
      for (const [key, child] of Object.entries(value)) {
        const childPath = pointer(path, key);
        if ((key === 'characteristics' || key === 'capabilities') && Array.isArray(child)) {
          child.forEach((entry, index) => {
            const entryPath = pointer(childPath, index);
            if (!record(entry)) {
              walk(entry, entryPath, `${key}[${index}]`, group, ownContext, depth + 1);
              return;
            }
            // SensorML's group wrappers need no invented CharacteristicList type.
            if (Array.isArray(entry[key])) {
              const suppliedGroup = addGroup(entryPath, suppliedLabel(entry, `${key}[${index}]`), key, string(entry.definition));
              const groupContext = suppliedContext(entry, ownContext);
              (entry[key] as unknown[]).forEach((component, componentIndex) => {
                walk(component, pointer(pointer(entryPath, key), componentIndex), `${key}[${componentIndex}]`, suppliedGroup, groupContext, depth + 1);
              });
              for (const [extraKey, extra] of Object.entries(entry)) {
                if (![key, 'id', 'label', 'name', 'definition', 'type'].includes(extraKey)) {
                  walk(extra, pointer(entryPath, extraKey), extraKey, suppliedGroup, groupContext, depth + 1);
                }
              }
            } else {
              walk(entry, entryPath, `${key}[${index}]`, group, ownContext, depth + 1);
            }
          });
        } else if (key === 'links' && Array.isArray(child)) {
          // Navigation links are exposed separately, and unchanged in original JSON.
          if (child.length === 0) addFact(child, childPath, key, 'JSON array', group, {}, ownContext);
        } else if (record(child) && !scalarTypes.has(String(child.type)) && !complexTypes.has(String(child.type))) {
          const nested = addGroup(childPath, suppliedLabel(child, key), string(child.type) ?? 'JSON object', string(child.definition));
          walk(child, childPath, key, nested, ownContext, depth + 1);
        } else {
          walk(child, childPath, key, group, ownContext, depth + 1);
        }
      }
    };

    const root = capture.json;
    collectLinks(root, '');
    if (!record(root)) {
      warn('', 'The response is not a JSON object describing one resource. It is retained for inspection.');
      const group = addGroup('', 'Original JSON', 'JSON');
      addFact(root, '', 'Response', 'JSON', group);
      continue;
    }

    const properties = root.type === 'Feature' && record(root.properties) ? root.properties : root;
    const propertyPath = properties === root ? '' : '/properties';
    const sensorML = typeof properties.type === 'string' && processTypes.has(properties.type);
    const csapiType = getCSAPIResourceType(root);
    if (sensorML) {
      try {
        const parsed = parseSensorML30(properties);
        model.resourceType = parsed.type;
        model.libraryParsed = true;
      } catch (error) {
        model.resourceType = String(properties.type);
        warn(propertyPath, `The pinned SensorML parser rejected this description: ${error instanceof Error ? error.message : String(error)}. Its supplied content is retained.`);
      }
    } else if (csapiType) {
      try {
        extractCSAPIFeature(root);
        model.libraryParsed = true;
      } catch (error) {
        warn('', `The pinned CSAPI extractor rejected this feature: ${error instanceof Error ? error.message : String(error)}. Its supplied content is retained.`);
      }
      if (!processTypes.has(model.resourceType)) model.resourceType = csapiType;
    } else if (model.resourceType === 'JSON') {
      model.resourceType = string(root.type) ?? 'JSON';
    }

    const suppliedId = identifier(root.id) ?? identifier(properties.id);
    const suppliedUniqueId = string(properties.uniqueId) ?? string(properties.uid);
    const suppliedName = string(properties.label) ?? string(properties.name) ?? string(root.label) ?? string(root.name);
    if (model.uniqueId !== undefined && suppliedUniqueId !== undefined && suppliedUniqueId !== model.uniqueId) {
      warn(propertyPath, 'This response supplies a different unique identifier from the first description. Values retain their original source attribution.');
    }
    if (model.id === '' && suppliedId !== undefined) model.id = suppliedId;
    if (model.uniqueId === undefined && suppliedUniqueId !== undefined) model.uniqueId = suppliedUniqueId;
    if (model.name === '' && suppliedName !== undefined) model.name = suppliedName;
    if (model.description === undefined) model.description = string(properties.description) ?? string(root.description);

    const rootGroup = addGroup('', 'Resource properties', string(root.type) ?? 'JSON object');
    walk(root, '', 'Resource', rootGroup, {});
  }

  // This label communicates absence; it is not a fabricated resource identity.
  if (model.name === '') model.name = 'Unnamed resource';
  if (model.id === '' && model.uniqueId === undefined) model.warnings.push('No resource identifier was supplied.');
  model.groups = model.groups.filter((group) => group.facts.length > 0);
  return model;
}
