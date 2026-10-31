import * as L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { node } from './resource-details-template';
import './resource-details-map.css';

/** A map of the reported GeoJSON Point, not a claim of current physical position. */
export function renderResourceMap(content: HTMLElement, position: unknown): () => void {
  const section = node('section', 'rd-map-widget');
  section.append(node('h3', 'rd-map-heading', 'Reported location'));
  const description = node('p', 'rd-map-description', 'Position from the selected System · not a live tracking feed');
  section.append(description);
  content.append(section);
  if (!position || typeof position !== 'object') {
    section.append(node('p', 'rd-map-empty', 'No position was supplied for this System.'));
    return () => {};
  }
  const geometry = position as { type?: unknown; coordinates?: unknown; [key: string]: unknown };
  const raw = node('p', 'rd-map-raw', `Reported position: ${JSON.stringify(position)}`);
  const coords = geometry.coordinates;
  const hasReference = Object.keys(geometry).some(key => /^(crs|srs|srsname|referenceframe|reference_frame|frame|srid)$/i.test(key));
  if (geometry.type !== 'Point' || !Array.isArray(coords) || coords.length < 2 || coords.length > 3 ||
      hasReference || !coords.every(value => typeof value === 'number' && Number.isFinite(value)) || Math.abs(coords[0]) > 180 || Math.abs(coords[1]) > 90) {
    section.append(node('p', 'rd-map-empty', 'This position is not a supported WGS 84 longitude/latitude Point. It cannot be plotted safely.'), raw);
    return () => {};
  }

  const canvas = node('div', 'rd-map-canvas'); canvas.setAttribute('aria-label', 'Map of reported resource position');
  const controls = node('div', 'rd-map-controls');
  const basemapLabel = node('label', undefined, 'Basemap');
  const basemap = node('select', 'rd-map-basemap'); basemap.setAttribute('aria-label', 'Basemap');
  for (const [value, label] of [['imagery', 'Satellite · 2016'], ['streets', 'Street map']]) {
    const option = node('option', undefined, label); option.value = value; basemap.append(option);
  }
  basemapLabel.append(basemap);
  const recenter = node('button', 'rd-map-recenter', 'Recenter'); recenter.type = 'button';
  controls.append(basemapLabel, recenter);
  const mapBox = node('div', 'rd-map-box'); mapBox.append(canvas, controls);
  const status = node('p', 'rd-map-status'); status.setAttribute('aria-live', 'polite');
  const axisLabel = node('label', 'rd-map-axis-label', 'Coordinate interpretation');
  const axis = node('select', 'rd-map-axis');
  const standard = node('option', undefined, 'GeoJSON: longitude, latitude'); standard.value = 'standard'; axis.append(standard);
  if (Math.abs(coords[0]) <= 90 && Math.abs(coords[1]) <= 180) {
    const alternative = node('option', undefined, 'Alternative: latitude, longitude'); alternative.value = 'alternate'; axis.append(alternative);
  }
  axisLabel.append(axis);
  const note = node('p', 'rd-map-note', 'The source does not identify axis order separately. GeoJSON uses longitude, latitude; verify the producer’s intent before relying on this position. The position time and accuracy are not supplied here. Basemap requests disclose the viewed area and your IP address to the map provider.');
  section.append(mapBox, status, axisLabel, raw, note);

  const initial = (): L.LatLngExpression => axis.value === 'alternate' ? [coords[0], coords[1]] : [coords[1], coords[0]];
  const limit = 85.05112878;
  const mappable = (): boolean => Math.abs(axis.value === 'alternate' ? coords[0] : coords[1]) <= limit;
  const map = L.map(canvas, { zoomControl: true, scrollWheelZoom: false, attributionControl: true, zoomAnimation: false, fadeAnimation: false, markerZoomAnimation: false }).setView(mappable() ? initial() : [0, 0], mappable() ? 9 : 1);
  const imagery = L.tileLayer('https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless_3857/default/g/{z}/{y}/{x}.jpg', {
    maxZoom: 19,
    attribution: '<a href="https://cloudless.eox.at/" target="_blank" rel="noopener noreferrer">EOxCloudless</a> by EOX IT Services GmbH (Contains modified Copernicus Sentinel data 2016)',
  });
  const streets = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap contributors</a>',
  });
  let failed = false;
  const updateStatus = (): void => {
    const [lat, lon] = axis.value === 'alternate' ? [coords[0], coords[1]] : [coords[1], coords[0]];
    status.textContent = `${lat}° latitude, ${lon}° longitude · ${axis.value === 'standard' ? 'GeoJSON order' : 'alternative order selected'}${!mappable() ? ' · Outside the basemap’s supported latitude; position cannot be shown on this map.' : failed ? ' · Some map tiles failed; switch basemaps or try again.' : ''}`;
  };
  for (const layer of [imagery, streets]) {
    layer.on('tileerror', () => { failed = true; updateStatus(); });
    layer.on('loading', () => { failed = false; updateStatus(); });
  }
  if (mappable()) imagery.addTo(map);
  const marker = L.marker(mappable() ? initial() : [0, 0], {
    title: 'Reported resource position', alt: 'Reported resource position',
    icon: L.divIcon({ className: 'rd-map-marker', html: '<span aria-hidden="true"></span>', iconSize: [28, 28], iconAnchor: [14, 14] }),
  });
  if (mappable()) marker.addTo(map);
  mapBox.hidden = !mappable();
  const relocate = (): void => {
    mapBox.hidden = !mappable();
    if (mappable()) {
      const point = initial(); marker.setLatLng(point).addTo(map);
      if (!map.hasLayer(imagery) && !map.hasLayer(streets)) (basemap.value === 'streets' ? streets : imagery).addTo(map);
      map.invalidateSize({ pan: false }); map.setView(point, map.getZoom());
    } else { marker.remove(); map.removeLayer(imagery); map.removeLayer(streets); }
    updateStatus();
  };
  axis.addEventListener('change', relocate);
  recenter.addEventListener('click', () => map.setView(initial(), map.getZoom()));
  basemap.addEventListener('change', () => {
    failed = false; map.removeLayer(basemap.value === 'streets' ? imagery : streets);
    (basemap.value === 'streets' ? streets : imagery).addTo(map); updateStatus();
  });
  updateStatus();
  let disposed = false;
  const resize = new ResizeObserver(() => { if (!disposed) map.invalidateSize({ pan: false }); }); resize.observe(canvas);
  const frame = requestAnimationFrame(() => { if (!disposed && canvas.isConnected) map.invalidateSize({ pan: false }); });
  return () => { disposed = true; cancelAnimationFrame(frame); resize.disconnect(); map.stop(); map.remove(); };
}
