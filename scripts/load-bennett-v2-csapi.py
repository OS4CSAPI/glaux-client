#!/usr/bin/env python3
import json
import sys
import urllib.error
import urllib.request

BASE = "https://129-80-248-53.sslip.io/csapi-pygeoapi"
MODEL = "https://glaux-client.pages.dev/fixtures/bennetts-point-ee181-model.sml.json"
MODEL_UID = "urn:merlin:v2:datasheet:campbell:ee181"

PROBES = [
    {
        "id": "b171318e-8efe-550d-be99-bec5364984c0",
        "uid": "urn:merlin:v2:bennetts:ee181:probe4",
        "label": "Bennett's Point EE181 Probe 4",
        "serial": "222016000109CE",
        "datastream": "bd10e9d3-0c03-5fbb-ba62-86559911d824",
        "observation": "542a6d5b-a4e1-5860-82be-6a1f7c6da883",
        "time": "2024-04-15T17:00:00Z",
        "value": 29.1,
        "period": "documented in use at Bennett's Point from 2023-06-08 until the 2024-04-16 probe change",
    },
    {
        "id": "ce4dd3bb-0b16-5772-8288-ba3e8e52c272",
        "uid": "urn:merlin:v2:bennetts:ee181:probe3",
        "label": "Bennett's Point EE181 Probe 3",
        "serial": "21281600077814",
        "datastream": "1eb64c0c-19c5-5f66-a34e-8d0f4244a561",
        "observation": "6e8cf4c0-1b66-5540-937c-f3743aee2c1e",
        "time": "2024-04-18T17:00:00Z",
        "value": 27.3,
        "period": "documented as returned to service at Bennett's Point on 2024-04-16 and still in use at the 2024 report cutoff",
    },
]

def request(method, path, payload=None, content_type="application/json"):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Accept": "application/json, application/sml+json"}
    if data is not None:
        headers["Content-Type"] = content_type
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            body = response.read().decode("utf-8")
            return response.status, json.loads(body) if body else None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except ValueError:
            parsed = body
        return exc.code, parsed

def ensure_system(p):
    status, body = request("GET", f"/systems/{p['id']}?f=application/json")
    if status == 200:
        print("system exists", p["id"])
        return
    if status != 404:
        raise RuntimeError(f"system preflight {p['id']} HTTP {status}: {body}")
    payload = {
        "type": "PhysicalSystem",
        "id": p["id"],
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
        raise RuntimeError(f"system POST {p['id']} HTTP {status}: {body}")
    status, returned = request("GET", f"/systems/{p['id']}?f=application/json")
    if status != 200 or returned.get("uniqueId") != p["uid"]:
        raise RuntimeError(f"system round trip failed {p['id']}: HTTP {status} {returned}")
    print("system created", p["id"])

def ensure_datastream(p):
    status, body = request("GET", f"/datastreams/{p['datastream']}?f=application/json")
    if status == 200:
        print("datastream exists", p["datastream"])
        return
    if status != 404:
        raise RuntimeError(f"datastream preflight {p['datastream']} HTTP {status}: {body}")
    payload = {
        "id": p["datastream"],
        "name": p["label"] + " — air temperature",
        "description": "15-minute mean air temperature from the Bennett's Point historical station record. This stream is tied to the identified physical probe; it is not live telemetry.",
        "system@link": {
            "href": BASE + "/systems/" + p["id"],
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
    status, body = request("POST", f"/systems/{p['id']}/datastreams", payload)
    if status not in (200, 201):
        raise RuntimeError(f"datastream POST {p['datastream']} HTTP {status}: {body}")
    status, returned = request("GET", f"/datastreams/{p['datastream']}?f=application/json")
    if status != 200:
        raise RuntimeError(f"datastream round trip failed {p['datastream']}: HTTP {status} {returned}")
    print("datastream created", p["datastream"])

def ensure_observation(p):
    status, collection = request("GET", f"/datastreams/{p['datastream']}/observations?f=application/json")
    if status != 200:
        raise RuntimeError(f"observation preflight HTTP {status}: {collection}")
    existing = (collection or {}).get("features", (collection or {}).get("items", []))
    if any(str(x.get("id")) == p["observation"] for x in existing):
        print("observation exists", p["observation"])
        return
    payload = {
        "id": p["observation"],
        "datastream@id": p["datastream"],
        "phenomenonTime": p["time"],
        "resultTime": p["time"],
        "result": p["value"]
    }
    status, body = request("POST", f"/datastreams/{p['datastream']}/observations", payload)
    if status not in (200, 201):
        raise RuntimeError(f"observation POST {p['observation']} HTTP {status}: {body}")
    status, collection = request("GET", f"/datastreams/{p['datastream']}/observations?f=application/json")
    rows = (collection or {}).get("features", (collection or {}).get("items", [])) if status == 200 else []
    if not any(str(x.get("id")) == p["observation"] and x.get("result") == p["value"] for x in rows):
        raise RuntimeError(f"observation round trip failed {p['observation']}: HTTP {status} {collection}")
    print("observation created", p["observation"])

def main():
    for probe in PROBES:
        ensure_system(probe)
        ensure_datastream(probe)
        ensure_observation(probe)
    print(json.dumps({
        "server": BASE,
        "systems": [{"id": p["id"], "uid": p["uid"], "serial": p["serial"], "datastream": p["datastream"], "observation": p["observation"]} for p in PROBES]
    }, indent=2))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("ERROR:", exc, file=sys.stderr)
        raise
