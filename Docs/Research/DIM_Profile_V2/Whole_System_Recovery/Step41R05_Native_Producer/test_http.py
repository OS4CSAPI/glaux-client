#!/usr/bin/env python3
"""41R-05 actual HTTP + original OGC v1.0 GeoJSON schema integration challenge.

Run from any directory after installing jsonschema:
  python3 Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step41R05_Native_Producer/test_http.py

Only loopback subprocess GET/HEAD/OPTIONS are used against the isolated server.
No Oracle, Cloudflare, physical Command or actual Observation is created.
"""
import json
import subprocess
import sys
import unittest
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, RefResolver

HERE = Path(__file__).resolve().parent
VENDOR = HERE / "schema-vendor"
OGC = VENDOR / "ogc/api/part1/openapi/schemas/geojson"
GEOJSON = "application/geo+json"

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate_original_schema(body, name):
    """Validate against pinned *unmodified published* OGC 23-001 v1.0.0 schemas."""
    source = OGC / name
    doc = load(source)
    store = {
        "https://geojson.org/schema/Feature.json": load(VENDOR / "geojson/Feature.json"),
        "https://geojson.org/schema/FeatureCollection.json": load(
            VENDOR / "geojson/FeatureCollection.json"),
    }
    resolver = RefResolver(base_uri=source.as_uri(), referrer=doc, store=store)
    Draft202012Validator(doc, resolver=resolver, format_checker=FormatChecker()).validate(body)

def source_binding(feature, evidence, kind):
    """Our project-specific binding check, NOT an OGC normative validation rule."""
    assert evidence["describes"]["href"] == next(
        link["href"] for link in feature["links"] if link["rel"] == "self")
    assert evidence["describes"]["uid"] == feature["properties"]["uid"]
    assert evidence["describes"]["kind"] == kind
    assert evidence["sourceEvidence"]["focus"] in {
        x["id"] for x in evidence["sourceEvidence"]["subjects"]}
    assert evidence["integratingProducer"]["verification"] == "PRODUCER_ASSERTED_UNVERIFIED"
    assert evidence["integratingProducer"]["role"] == "INTEGRATING_PRODUCER_NOT_ORIGINAL_ISSUER"
    ids = {x["id"] for x in evidence["sourceEvidence"]["sources"]}
    for claim in evidence["sourceEvidence"]["assertions"]:
        assert claim["evidence"]
        for e in claim["evidence"]:
            assert e["sourceId"] in ids
    if kind == "Procedure":
        assert evidence["describes"]["sourceStanding"] == "REFERENCE_ARRANGEMENT"
        assert evidence["sourceEvidence"]["originalEvents"] == []
    if kind == "System":
        assert evidence["describes"]["sourceStanding"] == "SOURCE_IDENTIFIED_STATION"
        assert len(evidence["sourceEvidence"]["originalEvents"]) == 2
        assert len(evidence["sourceEvidence"]["representations"]) == 4

class ActualReadOnlyHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proc = subprocess.Popen(
            [sys.executable, str(HERE / "server.py"), "--host", "127.0.0.1", "--port", "0"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
        line = cls.proc.stdout.readline().strip()
        if not line.startswith("41R05_READY http://127.0.0.1:"):
            raise RuntimeError("Server did not start: " + line)
        cls.base = line.split(" ", 1)[1]
        cls.api = cls.base.removesuffix("/api")

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait(timeout=10)
        cls.proc.stdout.close()
        cls.proc.stderr.close()

    def get(self, suffix, accept=None, method="GET", extra=None):
        url = suffix if suffix.startswith("http:") else self.base + suffix
        headers = dict(extra or {})
        if accept: headers["Accept"] = accept
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=10) as resp:
                data = resp.read()
                body = json.loads(data.decode("utf-8")) if data else None
                return resp.status, resp.headers, body
        except urllib.error.HTTPError as err:
            body = json.loads(err.read().decode("utf-8"))
            return err.code, err.headers, body

    def test_01_landing_and_versioned_profile(self):
        status, _, landing = self.get("")
        self.assertEqual(status, 200)
        self.assertEqual(landing["title"].split()[0], "41R-05")
        self.assertTrue(any(link["href"].endswith("/procedures") for link in landing["links"]))
        status, _, profile = self.get("/profiles/dim-csapi-source-evidence/v0.1")
        self.assertEqual(status, 200)
        self.assertEqual(profile["projectContract"], "dim-csapi-evidence-sidecar.v0.1")
        self.assertEqual(profile["standing"], "PROPOSED_PROJECT_PROFILE_EXTENSION_NOT_OGC_STANDARD")

    def test_02_conformance_honest_not_yet_ATS_claim(self):
        status, _, d = self.get("/conformance")
        self.assertEqual(status, 200)
        self.assertEqual(d["conformsTo"], [])
        self.assertTrue(d["candidateClassURIs"])
        self.assertIn("No full class/ATS", d["disclaimer"])

    def test_03_feature_collections_and_native_schema(self):
        for coll, typ in [("procedures", "procedure"), ("systems", "system")]:
            for path in ["/" + coll, "/collections/" + coll + "/items"]:
                status, headers, document = self.get(path, accept=GEOJSON)
                self.assertEqual(status, 200)
                self.assertEqual(headers.get_content_type(), GEOJSON)
                self.assertEqual(document["type"], "FeatureCollection")
                self.assertEqual(len(document["features"]), 1)
                validate_original_schema(document, typ + "Collection.json")
        status, _, c = self.get("/collections")
        self.assertEqual(status, 200)
        self.assertEqual({x["id"] for x in c["collections"]}, {"procedures", "systems"})
        for x in c["collections"]:
            self.assertEqual(x["itemType"], "feature")
            self.assertIn(x["featureType"], ("sosa:Procedure", "sosa:System"))

    def test_04_procedure_native_original_schema_and_no_fake_system(self):
        s, h, feature = self.get("/procedures/dragino-s31-lb", accept=GEOJSON)
        self.assertEqual(s, 200)
        self.assertEqual(h.get_content_type(), GEOJSON)
        validate_original_schema(feature, "procedure.json")
        self.assertEqual(feature["geometry"], None)
        self.assertEqual(feature["properties"]["featureType"], "http://www.w3.org/ns/sosa/Procedure")
        self.assertEqual(feature["id"], "dragino-s31-lb")
        self.assertNotIn("installedSerial", feature["properties"])

    def test_05_bennett_native_system_not_native_observation(self):
        s, h, feature = self.get("/systems/bennetts-point-acebpmet", accept=GEOJSON)
        self.assertEqual(s, 200)
        validate_original_schema(feature, "system.json")
        self.assertEqual(feature["properties"]["featureType"], "http://www.w3.org/ns/sosa/System")
        self.assertEqual(feature["geometry"], {
            "type":"Point", "coordinates":[-80.45456, 32.55934]})
        self.assertNotIn("resultTime", feature["properties"])
        self.assertNotIn("time", feature["properties"])

    def test_06_real_http_link_header_profile_evidence_and_CORS_visibility(self):
        for collection, name in [
            ("procedures", "dragino-s31-lb"), ("systems", "bennetts-point-acebpmet")]:
            _, headers, feature = self.get("/" + collection + "/" + name, accept=GEOJSON)
            link = headers.get("Link")
            self.assertIn('rel="profile"', link)
            self.assertIn('rel="describedby"', link)
            self.assertIn("Link", headers.get("Access-Control-Expose-Headers"))
            body_by_rel = {x["rel"]:x["href"] for x in feature["links"]}
            self.assertIn("<" + body_by_rel["profile"] + ">", link)
            self.assertIn("<" + body_by_rel["describedby"] + ">", link)
            status, evidence_headers, evidence = self.get(body_by_rel["describedby"])
            self.assertEqual(status, 200)
            self.assertEqual(evidence_headers.get_content_type(), "application/json")
            schema = load(HERE / "source-evidence.schema.json")
            Draft202012Validator(schema, format_checker=FormatChecker()).validate(evidence)
            source_binding(feature, evidence, "Procedure" if collection=="procedures" else "System")

    def test_07_dragino_reference_source_details(self):
        _, _, d = self.get("/evidence/dragino-s31-lb")
        packet = d["sourceEvidence"]
        self.assertEqual(len(packet["assertions"]), 21)
        claims = {x["id"]:x for x in packet["assertions"]}
        self.assertEqual(claims["c41-default"]["value"]["raw"], "20")
        self.assertEqual(claims["c41-command-example"]["standing"], "SOURCE_EXAMPLE")
        self.assertEqual(claims["c-effective"]["standing"], "UNKNOWN")
        self.assertEqual(len(packet["originalEvents"]), 0)
        self.assertEqual(d["integratingProducer"]["verification"], "PRODUCER_ASSERTED_UNVERIFIED")

    def test_08_bennett_two_original_reports_four_copies_raw_QA(self):
        _, _, d = self.get("/evidence/bennetts-point-acebpmet")
        packet = d["sourceEvidence"]
        self.assertEqual(len(packet["subjects"]), 8)
        self.assertEqual(len(packet["assertions"]), 37)
        self.assertEqual(len(packet["originalEvents"]), 2)
        self.assertEqual(len(packet["representations"]), 4)
        ids = {x["id"]:x for x in packet["assertions"]}
        self.assertEqual(ids["b-qc15"]["value"]["raw"], "<0> ")
        self.assertEqual(ids["b-qc18"]["value"]["raw"], "<0> ")
        self.assertEqual(ids["b-record-flag15"]["value"]["raw"], "")
        self.assertEqual(ids["b-record-flag18"]["value"]["raw"], "")
        self.assertEqual(ids["b-result-time15"]["standing"], "UNKNOWN")
        self.assertEqual(ids["b-producing-system18"]["standing"], "UNKNOWN")
        self.assertEqual(ids["b41r04-site-point"]["about"], "b-station")
        self.assertEqual(ids["b-probe-position"]["standing"], "UNKNOWN")
        self.assertEqual(ids["b41r04-maint16"]["about"], "b-station")

    def test_09_changed_sidecar_binding_fails_project_verification(self):
        _, _, feature = self.get("/systems/bennetts-point-acebpmet", accept=GEOJSON)
        _, _, evidence = self.get("/evidence/bennetts-point-acebpmet")
        source_binding(feature, evidence, "System")
        evidence["describes"]["uid"] = "urn:fake:unrelated-sensor"
        with self.assertRaises(AssertionError):
            source_binding(feature, evidence, "System")

    def test_10_all_command_and_write_methods_are_rejected(self):
        for method in ["POST", "PUT", "PATCH", "DELETE"]:
            status, headers, d = self.get("/systems/bennetts-point-acebpmet", method=method)
            self.assertEqual(status, 405)
            self.assertIn("GET", headers.get("Allow"))
        for path in ["/observations", "/commands", "/controlstreams", "/deployments"]:
            status, _, _ = self.get(path)
            self.assertEqual(status, 404)
        status, _, _ = self.get("/profiles/dim-csapi-source-evidence/v0.2")
        self.assertEqual(status, 404)

    def test_11_reject_incompatible_Accept_and_unknown_resources(self):
        status, _, _ = self.get("/procedures/dragino-s31-lb", accept="application/json")
        self.assertEqual(status, 406)
        status, _, _ = self.get("/procedures/nonexistent", accept=GEOJSON)
        self.assertEqual(status, 404)

    def test_12_HTTP_HEAD_OPTIONS_and_no_host_header_trust(self):
        status, headers, body = self.get("/systems/bennetts-point-acebpmet", method="HEAD")
        self.assertEqual(status, 200)
        self.assertIsNone(body)
        self.assertEqual(headers.get_content_type(), GEOJSON)
        status, headers, _ = self.get("/systems/bennetts-point-acebpmet", method="OPTIONS")
        self.assertEqual(status, 204)
        self.assertEqual(headers.get("Access-Control-Allow-Origin"), "*")
        status, _, evidence = self.get("/evidence/dragino-s31-lb", extra={"Host":"untrusted.example"})
        self.assertEqual(status, 200)
        self.assertIn("127.0.0.1", evidence["describes"]["href"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
