#!/usr/bin/env python3
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://129-80-248-53.sslip.io/csapi-pygeoapi"
MODEL = "https://glaux-client.pages.dev/fixtures/bennetts-point-ee181-model.sml.json"
MODEL_UID = "urn:merlin:v2:datasheet:campbell:ee181"

PROBES = [
    {
        "uid": "urn:merlin:v2:bennetts:ee181:probe4",
        "label": "Bennett's Point EE181 Probe 4",
        "serial": "222016000109CE",
        "stream_key": "urn:merlin:v2:bennetts:ee181:probe4:airtemp",
        "time": "2024-04-15T17:00:00Z",
        "value": 29.1,
        "period": "documented in use at Bennett's Point from 2023-06-08 until the 2024-04-16 probe change",
    },
    {
        "uid": "urn:merlin:v2:bennetts:ee181:probe3",
        "label": "Bennett's Point EE181 Probe 3",
        "serial": "212816000109CE",
        "stream_key": "urn:merlin:v2:bennetts:ee181:probe3:airtemp",
        "time": "2024-04-18T17:00:00Z",
        "value": 27.3,
        "period": "documented as returned to service at Bennett's Point on 2024-04-16 and still in use at the 2024 report cutoff",
    },
]

# Correct the Probe 3 serial from the controlled evidence record.
PROBES[1]["serial"] = "21281600077814"

def request(method, path, payload=None, content_type="application/json"):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": "application/json, application/sml+json"}
    if data is not None:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            body = response.read().decode("utf-8")
            try:
                parsed = json.loads(body) if body else None
            except ValueError:
                parsed = body
            return response.status, parsed
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except ValueError:
            parsed = body
        return exc.code, parsed

def rows(doc):
    return (doc or {}).get("features", (doc or {}).get("items", [])) if isinstance(doc, dict) else []

def list_all(path, page_size=100, max_pages=20):
    out = []
    for page in range(max_pages):
        sep = "&" if "?" in path else "?"
        status, doc = request("GET", f"{path}{sep}f=application/json&limit={page_size}&offset={page*page_size}")
        if status != 200:
            raise RuntimeError(f"list {path} HTTP {status}: {doc}")
        batch = rows(doc)
        out.extend(batch)
        if len(batch) < page_size:
            break
    return out

def find_system(uid):
    for item in list_all("/systems"):
        if item.get("uniqueId") == uid:
            return item
    return None

def ensure_system(p):
    current = find_system(p["uid"])
    if current:
        print("system exists", current["id"], p["uid"])
        return current["id"]
    payload = {
        "type": "PhysicalSystem",
        "definition": "http://www.w3.org/ns/sosa/Sensor",
        "uniqueId": p["uid"],
        "label": p["label"],
        "description": "Controlled MERLIN V2 Bennett's Point case: Campbell Scientific EE181 physical probe, " + p["period"] + ".",
        "typeOf": {
            "href": MODEL,
            "uid": MODEL_UID,
            "title": "Campbell Scientific EE181 — MERLIN V2 model description",
            "type": "application/sml+json"
        },
        "identifiers": [{
            "definition": "http://sensorml.com/ont/swe/property/SerialNumber",
            "label": "Serial Number",
            "value": p["serial"]
        }]
    }
    status, body = request("POST", "/systems", payload, "application/sml+json")
    if status not in (200, 201):
        raise RuntimeError(f"system POST {p['uid']} HTTP {status}: {body}")
    current = find_system(p["uid"])
    if not current:
        raise RuntimeError(f"system round trip failed for {p['uid']}; create response was {body}")
    print("system created", current["id"], p["uid"])
    return current["id"]

def find_stream(system_id, stream_key):
    status, doc = request("GET", f"/systems/{system_id}/datastreams?f=application/json&limit=100")
    if status != 200:
        raise RuntimeError(f"datastream list {system_id} HTTP {status}: {doc}")
    for ds in rows(doc):
        if ds.get("description", "").startswith(stream_key + " |"):
            return ds
    return None

def ensure_datastream(p, system_id):
    current = find_stream(system_id, p["stream_key"])
    if current:
        print("datastream exists", current["id"], p["stream_key"])
        return current["id"]
    payload = {
        "name": p["label"] + " — air temperature",
        "description": p["stream_key"] + " | 15-minute mean air temperature from the Bennett's Point historical station record. This stream is tied to the identified physical probe; it is not live telemetry.",
        "system@link": {
            "href": BASE + "/systems/" + system_id,
            "title": p["uid"]
        },
        "observedProperties": [{
            "definition": "http://vocab.nerc.ac.uk/standard_name/air_temperature/",
            "label": "Air temperature"
        }],
        "resultType": "measure",
        "live": False,
        "formats": ["application/json"],
        "schema": {
            "obsFormat": "application/om+json",
            "resultTimeSchema": {
                "name": "time",
                "type": "Time",
                "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
                "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
                "label": "Station timestamp",
                "uom": {"href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"}
            },
            "resultSchema": {
                "name": "airTemperature",
                "type": "Quantity",
                "definition": "http://vocab.nerc.ac.uk/standard_name/air_temperature/",
                "label": "Air temperature",
                "uom": {"code": "Cel"}
            }
        }
    }
    status, body = request("POST", f"/systems/{system_id}/datastreams", payload)
    if status not in (200, 201):
        raise RuntimeError(f"datastream POST {p['stream_key']} HTTP {status}: {body}")
    current = find_stream(system_id, p["stream_key"])
    if not current:
        raise RuntimeError(f"datastream round trip failed {p['stream_key']}; create response was {body}")
    print("datastream created", current["id"], p["stream_key"])
    return current["id"]

def same_time(value, expected):
    return value == expected or (isinstance(value, list) and expected in value)

def ensure_observation(p, datastream_id):
    status, doc = request("GET", f"/datastreams/{datastream_id}/observations?f=application/json&limit=100")
    if status != 200:
        raise RuntimeError(f"observation preflight HTTP {status}: {doc}")
    for obs in rows(doc):
        if obs.get("result") == p["value"] and (same_time(obs.get("resultTime"), p["time"]) or same_time(obs.get("phenomenonTime"), p["time"])):
            print("observation exists", obs.get("id"), p["time"], p["value"])
            return obs.get("id")
    payload = {
        "datastream@id": datastream_id,
        "phenomenonTime": p["time"],
        "resultTime": p["time"],
        "result": p["value"]
    }
    status, body = request("POST", f"/datastreams/{datastream_id}/observations", payload)
    if status not in (200, 201):
        raise RuntimeError(f"observation POST {p['time']} HTTP {status}: {body}")
    status, doc = request("GET", f"/datastreams/{datastream_id}/observations?f=application/json&limit=100")
    if status != 200:
        raise RuntimeError(f"observation round trip list HTTP {status}: {doc}")
    for obs in rows(doc):
        if obs.get("result") == p["value"] and (same_time(obs.get("resultTime"), p["time"]) or same_time(obs.get("phenomenonTime"), p["time"])):
            print("observation created", obs.get("id"), p["time"], p["value"])
            return obs.get("id")
    raise RuntimeError(f"observation round trip failed {p['time']} {p['value']}")

def main():
    manifest = {"server": BASE, "systems": []}
    for probe in PROBES:
        system_id = ensure_system(probe)
        datastream_id = ensure_datastream(probe, system_id)
        observation_id = ensure_observation(probe, datastream_id)
        manifest["systems"].append({
            "id": system_id,
            "uid": probe["uid"],
            "serial": probe["serial"],
            "datastream": datastream_id,
            "observation": observation_id,
            "time": probe["time"],
            "value": probe["value"],
        })
    print("BENNETT_MANIFEST=" + json.dumps(manifest, separators=(",", ":")))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("ERROR:", exc, file=sys.stderr)
        raise
