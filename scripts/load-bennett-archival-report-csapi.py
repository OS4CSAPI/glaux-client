#!/usr/bin/env python3
"""Publish and verify a reversible *parallel* archival-report stream per probe.

This is a preservation bridge for the deployed 52°North/pygeoapi build, NOT a claim
that the native JSON Observation.phenomenonTime can represent a time interval.
Existing scalar DataStreams/Observations are neither edited nor deleted.
"""
import json
import runpy
from datetime import datetime, timedelta, timezone
from pathlib import Path

legacy = runpy.run_path(str(Path(__file__).with_name("load-bennett-v2-csapi.py")))
request = legacy["request"]
rows = legacy["rows"]
find_system = legacy["find_system"]
find_stream = legacy["find_stream"]
same_time = legacy["same_time"]
BASE = legacy["BASE"]

DATA = [
    {
        "uid": "urn:merlin:v2:bennetts:ee181:probe4",
        "serial": "222016000109CE",
        "end": "2024-04-15T17:00:00Z",
        "air": 29.1,
        "flag": "<0> ",
        "source_row": 10130
    },
    {
        "uid": "urn:merlin:v2:bennetts:ee181:probe3",
        "serial": "21281600077814",
        "end": "2024-04-18T17:00:00Z",
        "air": 27.3,
        "flag": "<0> ",
        "source_row": 10418
    }
]

SENSOR_SOURCE = "https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf"
CSV_SOURCE = "https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv"

def report(p):
    closing = datetime.fromisoformat(p["end"].replace("Z", "+00:00"))
    opening = closing - timedelta(minutes=15)
    start = opening.isoformat(timespec="seconds").replace("+00:00","Z")
    return {
        "stamp": p["end"],
        "window": [start, p["end"]],
        "air": p["air"],
        "qc": p["flag"],
        "probe": p["uid"]
    }

def observation_schema():
    return {
        "obsFormat": "application/json",
        "resultSchema": {
            "type": "DataRecord",
            "label": "Archival temperature report: value, source QA token and nominal 15-minute period",
            "fields": [
                {
                    "name": "stamp",
                    "type": "Time",
                    "definition": "http://www.opengis.net/def/property/OGC/0/SamplingTime",
                    "label": "Source record timestamp (closing the average)",
                    "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
                    "uom": {"href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"}
                },
                {
                    "name": "window",
                    "type": "TimeRange",
                    "definition": "urn:merlin:dim-v2:bennetts:nominal-averaging-window",
                    "label": "Nominal 15-minute averaging interval (not native phenomenonTime)",
                    "referenceFrame": "http://www.opengis.net/def/trs/BIPM/0/UTC",
                    "uom": {"href": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"}
                },
                {
                    "name": "air",
                    "type": "Quantity",
                    "definition": "https://vocab.nerc.ac.uk/standard_name/air_temperature/",
                    "label": "15-minute mean air temperature",
                    "uom": {"code": "Cel"}
                },
                {
                    "name": "qc",
                    "type": "Text",
                    "definition": "urn:merlin:dim-v2:bennetts:source-F_ATemp",
                    "label": "Original temperature-specific NOAA/CDMO QA flag",
                    "description": "Verbatim F_ATemp source token, including whitespace and any supplementary codes; this is not a separate measurement or equipment condition."
                },
                {
                    "name": "probe",
                    "type": "Text",
                    "definition": "urn:merlin:dim-v2:bennetts:attributed-sensing-unit-uid",
                    "label": "Attributed physical sensing System UID",
                    "description": "Project attribution from the station equipment history; the CSV does not contain this UID."
                }
            ]
        }
    }

def ensure_stream(p, system_id):
    stream_key = p["uid"] + ":archival-report:v1"
    existing = find_stream(system_id, stream_key)
    if existing:
        ds_id = existing["id"]
        print("archival stream exists", ds_id)
    else:
        payload = {
            "name": "Bennett's Point EE181 — archival air-temperature report (" + p["serial"] + ")",
            "description": stream_key + " | Controlled archival-report preservation carrier. Exact NOAA F_ATemp and computed nominal TimeRange are in the DataRecord result because this 52°North build only stores a scalar Observation.phenomenonTime and drops Observation.parameters. NOT native phenomenon interval, true resultTime, or full CSAPI/OMS conformance. Source CSV: " + CSV_SOURCE,
            "system@link": {"href": BASE + "/systems/" + system_id, "uid": p["uid"]},
            "observedProperties": [{
                "definition": "https://vocab.nerc.ac.uk/standard_name/air_temperature/",
                "label": "15-minute mean air temperature"
            }],
            "resultType": "measure",
            "live": False,
            "formats": ["application/json"],
            "schema": observation_schema()
        }
        status, response = request("POST", "/systems/" + system_id + "/datastreams", payload)
        if status not in (200,201):
            raise RuntimeError(f"create archival DataStream HTTP {status}: {response}")
        existing = find_stream(system_id, stream_key)
        if not existing:
            raise RuntimeError("archival DataStream not findable after POST")
        ds_id=existing["id"]
        print("archival stream created", ds_id)
    status, retrieved = request("GET", "/datastreams/" + ds_id + "?f=application/json")
    if status != 200 or retrieved.get("schema", {}).get("resultSchema", {}).get("type") != "DataRecord":
        raise RuntimeError(f"DataRecord schema did not round-trip HTTP {status}: {retrieved}")
    for component in observation_schema()["resultSchema"]["fields"]:
        saved = next((x for x in retrieved["schema"]["resultSchema"]["fields"] if x.get("name") == component["name"]), None)
        if not saved or saved.get("type") != component["type"] or saved.get("definition") != component["definition"]:
            raise RuntimeError(f"schema component did not survive: {component['name']}")
    return ds_id

def ensure_report(p, ds_id):
    wanted = report(p)
    path = "/datastreams/" + ds_id + "/observations?f=application/json&limit=100"
    status, doc = request("GET", path)
    if status != 200:
        raise RuntimeError(f"archival observations preflight HTTP {status}: {doc}")
    for obs in rows(doc):
        if obs.get("result") == wanted:
            print("archival report exists", obs["id"], "F_ATemp", repr(wanted["qc"]))
            return obs["id"]
    payload = {
        "datastream@id": ds_id,
        # Server-required instant fields: this is the *source stamp* as a
        # compatibility surrogate. It is NOT independently evidenced result time
        # or a native representation of the period of observation.
        "phenomenonTime": p["end"],
        "resultTime": p["end"],
        "result": wanted
    }
    status, response = request("POST", "/datastreams/"+ds_id+"/observations", payload)
    if status not in (200,201):
        raise RuntimeError(f"create archival observation HTTP {status}: {response}")
    status, doc = request("GET", path)
    if status != 200:
        raise RuntimeError(f"read-back observation HTTP {status}: {doc}")
    matching=[obs for obs in rows(doc) if obs.get("result") == wanted and same_time(obs.get("phenomenonTime"),p["end"])]
    if len(matching) != 1:
        raise RuntimeError(f"Observation result/flag/interval not preserved exactly; matching={len(matching)}")
    print("archival report created",matching[0]["id"],"F_ATemp",repr(wanted["qc"]))
    return matching[0]["id"]

def main():
    result={"source_csv":CSV_SOURCE,"metadata":SENSOR_SOURCE,"server":BASE,"kind":"experimental archival-report preservation carrier","entries":[]}
    for p in DATA:
        system=find_system(p["uid"])
        if system is None:
            raise RuntimeError("Existing probe System missing: "+p["uid"])
        serials=[x.get("value") for x in system.get("identifiers",[]) if x.get("label")=="Serial Number"]
        if p["serial"] not in serials:
            raise RuntimeError(f"Source attribution and live System disagree: {p['uid']} -> {serials}")
        stream_id=ensure_stream(p,system["id"])
        obs_id=ensure_report(p,stream_id)
        result["entries"].append({"system_id":system["id"],"system_uid":p["uid"],"serial":p["serial"],"datastream_id":stream_id,"observation_id":obs_id,"result":report(p),"source_csv_line":p["source_row"]})
    print("ARCHIVAL_BRIDGE_MANIFEST="+json.dumps(result,ensure_ascii=False,separators=(",",":")))

if __name__ == "__main__":
    main()
