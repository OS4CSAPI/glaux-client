#!/usr/bin/env python3
"""41R-05 isolated READ-ONLY CSAPI Part 1 GeoJSON producer experiment.

The native GeoJSON bodies use OGC 23-001 Part 1 structures; the linked evidence
sidecar is explicitly PROJECT-AUTHORED and is *not* a native OGC resource.

No physical Commands, POST/PUT/PATCH/DELETE, Oracle access, Cloudflare deploy,
or fabricated Bennett Observations / exact-time Deployments.
"""
import argparse
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[2]  # Docs/Research/DIM_Profile_V2
HERE = Path(__file__).resolve().parent
PROFILE_SLUG = "dim-csapi-source-evidence/v0.1"
PROFILE_FORMAT = "dim-csapi-evidence-sidecar.v0.1"
GEOJSON = "application/geo+json"
DOCS = {
    ("procedures", "dragino-s31-lb"): {
        "id": "dragino-s31-lb",
        "uid": "urn:os4csapi:dim-v2:reference-procedure:dragino-s31-lb",
        "name": "Dragino S31-LB (manufacturer reference design)",
        "description": "S31-LB model/datasheet reference, external SHT31. Not an installed device.",
        "featureType": "http://www.w3.org/ns/sosa/Procedure",
        "packet": "Candidate_Specification/examples/step41r03-source-packets/dragino.coverage.packet.json",
        "kind": "Procedure",
        "standing": "REFERENCE_ARRANGEMENT",
    },
    ("systems", "bennetts-point-acebpmet"): {
        "id": "bennetts-point-acebpmet",
        "uid": "urn:os4csapi:dim-v2:historical-system:acebpmet",
        "name": "Bennett's Point ACE Basin meteorological station",
        "description": "Source-identified continuing historical station, qualified 2024 source evidence; no current-operation claim.",
        "featureType": "http://www.w3.org/ns/sosa/System",
        "packet": "Candidate_Specification/examples/step41r04-source-packets/bennetts-point.coverage.packet.json",
        "kind": "System",
        "standing": "SOURCE_IDENTIFIED_STATION",
    },
}
CONFORMANCE = [
    # A self-declared test producer implementation; individual ATS obligations
    # and full independent OGC certification are NOT established merely here.
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/landing-page",
    "http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/json",
    "http://www.opengis.net/spec/ogcapi-connected-systems-1/1.0/conf/api-common",
    "http://www.opengis.net/spec/ogcapi-connected-systems-1/1.0/conf/system-features",
    "http://www.opengis.net/spec/ogcapi-connected-systems-1/1.0/conf/procedure",
    "http://www.opengis.net/spec/ogcapi-connected-systems-1/1.0/conf/geojson",
]
# During this research experiment we deliberately do not make a normative
# /conformance claim before all prerequisite class/ATS checks pass.
ADVERTISE_CONFORMANCE = False

def source_packet(info):
    packet = json.loads((ROOT / info["packet"]).read_text(encoding="utf-8"))
    if packet["focus"] not in {x["id"] for x in packet["subjects"]}:
        raise ValueError("Source-evidence packet focus is not declared")
    if not packet["sources"] or not packet["assertions"]:
        raise ValueError("Empty source evidence")
    return packet

def base_for(handler):
    host = handler.headers.get("Host", "")
    if not host or "/" in host or "\\" in host or "@" in host:
        host = f"127.0.0.1:{handler.server.server_address[1]}"
    # Only loopback/isolated addresses. Do not treat untrusted proxy headers as
    # authoritative public origin for a production source-evidence identity.
    if not (host.startswith("127.0.0.1:") or host.startswith("localhost:")):
        host = f"127.0.0.1:{handler.server.server_address[1]}"
    return "http://" + host + "/api"

def native_feature(base, collection, info):
    href = f'{base}/{collection}/{info["id"]}'
    profile = base + "/profiles/" + PROFILE_SLUG
    evidence = base + "/evidence/" + info["id"]
    geometry = None
    if info["kind"] == "System":
        # Source-reported site location, NOT per-probe surveyed coordinates.
        geometry = {"type": "Point", "coordinates": [-80.45456, 32.55934]}
    return {
        "type": "Feature", "id": info["id"], "geometry": geometry,
        "properties": {
            "uid": info["uid"], "name": info["name"],
            "description": info["description"], "featureType": info["featureType"],
        },
        "links": [
            {"rel": "self", "href": href, "type": GEOJSON},
            {"rel": "profile", "href": profile, "type": "application/json"},
            {"rel": "describedby", "href": evidence, "type": "application/json"},
        ],
    }

def evidence_sidecar(base, collection, info):
    p = source_packet(info)
    return {
        "format": PROFILE_FORMAT,
        "profile": base + "/profiles/" + PROFILE_SLUG,
        "describes": {
            "href": f'{base}/{collection}/{info["id"]}',
            "uid": info["uid"], "kind": info["kind"],
            "sourceStanding": info["standing"],
        },
        "integratingProducer": {
            "name": "OS4CSAPI DIM/Profile V2 isolated 41R-05 producer",
            "role": "INTEGRATING_PRODUCER_NOT_ORIGINAL_ISSUER",
            "verification": "PRODUCER_ASSERTED_UNVERIFIED",
            "reason": "Earlier controlled-source oracles are not manufacturer/NOAA digital signatures.",
        },
        "sourceEvidence": {
            "projectPacketFormat": p["format"], "packetId": p["id"],
            "focus": p["focus"],
            "sources": p["sources"],
            "subjects": p["subjects"],
            "assertions": p["assertions"],
            "originalEvents": p["originalEvents"],
            "representations": p["representations"],
            "holds": p["holds"],
        },
    }

def collection_feature_list(base, collection):
    subset = [(key, info) for (key, _), info in DOCS.items() if key == collection]
    return {
        "type": "FeatureCollection",
        "features": [native_feature(base, collection, item) for _, item in subset],
        "numberMatched": len(subset), "numberReturned": len(subset),
        "links": [{"rel": "self", "href": base + "/" + collection, "type": GEOJSON}],
    }

class Handler(BaseHTTPRequestHandler):
    server_version = "41R05-ReadOnly-CSAPI-Experiment/0.1"
    def do_POST(self): self._readonly()
    def do_PUT(self): self._readonly()
    def do_PATCH(self): self._readonly()
    def do_DELETE(self): self._readonly()
    def _readonly(self):
        self._json(405, {"code": "MethodNotAllowed", "description": "Read-only isolated research producer"},
                   allow="GET, HEAD, OPTIONS")
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Allow", "GET, HEAD, OPTIONS")
        self._cors()
        self.end_headers()
    def do_HEAD(self):
        self._dispatch(head=True)
    def do_GET(self):
        self._dispatch(head=False)
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Accept, Content-Type")
        self.send_header("Access-Control-Expose-Headers", "Link, Content-Type, Allow")
    def _json(self, code, obj, media="application/json", links=None, allow=None, head=False):
        raw = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", media)
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        if allow: self.send_header("Allow", allow)
        self._cors()
        if links:
            self.send_header("Link", ", ".join(
                f'<{link["href"]}>; rel="{link["rel"]}"'
                + (f'; type="{link["type"]}"' if link.get("type") else "")
                for link in links
            ))
        self.end_headers()
        if not head: self.wfile.write(raw)
    def _dispatch(self, head=False):
        base = base_for(self)
        path = unquote(urlsplit(self.path).path).rstrip("/")
        if not path.startswith("/api"):
            return self._json(404, {"code":"NotFound"}, head=head)
        target = path[4:]
        if target in ("", "/"):
            return self._json(200,{
                "title": "41R-05 isolated, read-only CSAPI native GeoJSON producer",
                "description": "Research test producer, not independent OGC conformance certification.",
                "links": [
                    {"href": base, "rel":"self","type":"application/json"},
                    {"href":base+"/api","rel":"service-desc","type":"application/vnd.oai.openapi+json;version=3.0"},
                    {"href":base+"/conformance","rel":"conformance","type":"application/json"},
                    {"href":base+"/collections","rel":"data","type":"application/json"},
                    {"href":base+"/procedures","rel":"ogc-rel:procedures","type":GEOJSON},
                    {"href":base+"/systems","rel":"ogc-rel:systems","type":GEOJSON},
                ],
            },head=head)
        if target == "/conformance":
            return self._json(200,{
                "conformsTo": CONFORMANCE if ADVERTISE_CONFORMANCE else [],
                "scope": "isolated-research-subset",
                "candidateClassURIs": CONFORMANCE,
                "disclaimer": "No full class/ATS conformance claim until all prerequisite tests pass."
            },head=head)
        if target == "/api":
            return self._json(200,{
                "openapi":"3.0.3",
                "info":{"title":"41R-05 Isolated CSAPI Producer","version":"0.1.0"},
                "servers":[{"url":base}],
                "paths":{f"/{r}":{"get":{"responses":{"200":{"description":"Read-only GeoJSON resources"}}}}
                         for r in ["systems","procedures","collections","conformance"]},
            },head=head)
        if target == "/collections":
            return self._json(200,{
                "collections": [self._collection_meta(base, coll) for coll in ("procedures","systems")],
                "links":[{"rel":"self","href":base+"/collections","type":"application/json"}]
            },head=head)
        for collection in ("procedures","systems"):
            if target == "/"+collection or target == f"/collections/{collection}/items":
                if "application/json" in self.headers.get("Accept","") and GEOJSON not in self.headers.get("Accept",""):
                    return self._json(406,{"code":"NotAcceptable","description":"Use application/geo+json"},head=head)
                return self._json(200,collection_feature_list(base,collection),
                                  media=GEOJSON,head=head)
            if target == f"/collections/{collection}":
                return self._json(200,self._collection_meta(base,collection),head=head)
            prefixes = ["/"+collection+"/",f"/collections/{collection}/items/"]
            for prefix in prefixes:
                if target.startswith(prefix):
                    name = target[len(prefix):]
                    info = DOCS.get((collection,name))
                    if not info:
                        return self._json(404,{"code":"NotFound","description":"No such resource"},head=head)
                    if "application/json" in self.headers.get("Accept","") and GEOJSON not in self.headers.get("Accept",""):
                        return self._json(406,{"code":"NotAcceptable","description":"Use application/geo+json"},head=head)
                    native=native_feature(base,collection,info)
                    return self._json(200,native,media=GEOJSON,
                        links=[x for x in native["links"] if x["rel"] in ("profile","describedby")],
                        head=head)
        if target.startswith("/evidence/"):
            name=target.split("/")[-1]
            for (coll,ident),info in DOCS.items():
                if ident==name:
                    return self._json(200,evidence_sidecar(base,coll,info),head=head)
            return self._json(404,{"code":"NotFound"},head=head)
        if target == "/profiles/"+PROFILE_SLUG:
            return self._json(200,{
                "id":base+"/profiles/"+PROFILE_SLUG,
                "projectContract":"dim-csapi-evidence-sidecar.v0.1",
                "schema":base+"/evidence-schema",
                "appliesTo":["Procedure","System"],
                "standing":"PROPOSED_PROJECT_PROFILE_EXTENSION_NOT_OGC_STANDARD",
                "normativeReferences":[
                    "https://docs.ogc.org/is/23-001/23-001.html",
                    "https://www.rfc-editor.org/rfc/rfc6906",
                    "https://www.rfc-editor.org/rfc/rfc8288",
                ],
            },head=head)
        if target == "/evidence-schema":
            return self._json(200,json.loads((HERE/"source-evidence.schema.json").read_text()),
                              media="application/schema+json",head=head)
        return self._json(404,{"code":"NotFound"},head=head)
    @staticmethod
    def _collection_meta(base,coll):
        return {
            "id":coll,"title": "41R-05 " + coll + " source-selected test collection",
            "itemType":"feature","featureType":"sosa:Procedure" if coll=="procedures" else "sosa:System",
            "links":[{"rel":"items","href":base+"/collections/"+coll+"/items","type":GEOJSON},
                     {"rel":"self","href":base+"/collections/"+coll,"type":"application/json"}],
        }
    def log_message(self,*args): pass

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--host",default="127.0.0.1")
    ap.add_argument("--port",type=int,default=0)
    opt=ap.parse_args()
    if opt.host not in ("127.0.0.1","localhost"):
        ap.error("Research producer only binds to a loopback interface")
    with ThreadingHTTPServer((opt.host,opt.port),Handler) as server:
        print(f"41R05_READY http://127.0.0.1:{server.server_port}/api",flush=True)
        server.serve_forever()

if __name__=="__main__":main()
