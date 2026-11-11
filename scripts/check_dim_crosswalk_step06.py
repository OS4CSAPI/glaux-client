#!/usr/bin/env python3
"""Read-only verification of the Step06 committed binary XLSX and its JSON/CSV mirrors.
This is file-integrity and presentation testing, NOT source semantic verification.
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE = Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NAME = "Master_Donor_Concept_to_DIM_Crosswalk"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def fail(message: str) -> None:
    raise AssertionError(message)


def required(cond: bool, message: str) -> None:
    if not cond:
        fail(message)


def colnum(label: str) -> int:
    result = 0
    for char in label:
        result = 26 * result + ord(char) - ord("A") + 1
    return result - 1


def data_rows(xml_bytes: bytes, width: int) -> tuple[ET.Element, list[list[str]]]:
    root = ET.fromstring(xml_bytes)
    out = []
    sheet_data = root.find(S + "sheetData")
    required(sheet_data is not None, "worksheet lacks sheetData")
    for row in sheet_data.findall(S + "row"):
        values = [""] * width
        for c in row.findall(S + "c"):
            ref = c.attrib.get("r", "")
            m = re.match(r"^([A-Z]+)([0-9]+)$", ref)
            required(m is not None, f"bad cell reference {ref}")
            col = colnum(m.group(1))
            required(col < width, f"cell outside expected width: {ref}")
            x = c.find(S + "is")
            if x is None:
                v = c.find(S + "v")
                value = v.text if v is not None and v.text is not None else ""
            else:
                value = "".join(t.text or "" for t in x.iter(S + "t"))
            values[col] = value
        out.append(values)
    return root, out



def verify_sosa_d_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Current 15-column source-backed crosswalk verifier; retains historical checks."""
    import hashlib
    l = json.loads((BASE / "Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    v = json.loads((BASE / "Step17_SOSA_D_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
    isa = json.loads((BASE / "ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json").read_text(encoding="utf-8"))
    twin = (BASE / "ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    grid = doc["review_grid"]
    required(doc["schemaVersion"] == "0.11" and len(doc["rows"]) == 329, "SOSA-D current schema and 329 stable rows")
    required(len(doc["columns"]) == 15 and doc["columns"][8]["key"] == "OpenGroupSOSA" and doc["columns"][9]["key"] == "SOSA", "separate Open Group vs W3C donor columns")
    required(doc["columns"][-1]["key"] == "DIM" and [x["key"] for x in doc["columns"][:4]] == ["Dragino","AirGradient","Campbell","Bennett"], "DIM-right / four-source-case-left layout")
    required(len(grid) == 346 and all(len(r) == 15 for r in grid) and mirror == grid, "CSV and structured 346x15 grid")
    required(md.split("<table>",1)[1] == twin.split("<table>",1)[1] and md.count('colspan="15"') == 15, "current readable table and section dividers")
    required(len(doc["originalDonorEvidence"]) == 58 and len(doc["caseEvidence"]) == 73, "historical 58 donor / 73 case records preserved")
    required(len(l["all_57_qualified_source_decisions"]) == 57 and len(l["integration_row_ledger"]) == 38 and l["source_native_records"] == 76, "original C239 SOSA 57/38/76 evidence")
    required(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"], "no unverified native companion or DIM adoption claim")
    required(len(isa["six_precise_source_questions"]) == 6 and all(x["question_closed"] is False for x in isa["six_precise_source_questions"]), "six original ISA source holds unchanged")
    required(doc["ISAEvidence"]["currentPrimaryReviews"] == 480 and doc["ISAEvidence"]["specificQuestions"] == 6, "preserve 480-source ISA census")

    source_cells = {r["row_id"]: r["display_cell"] for r in l["integration_row_ledger"]}
    for row in doc["rows"]:
        required(row["display"][8] == source_cells.get(row["row_id"], "Not assessed here"), "source-grade The Open Group SOSA cell " + row["row_id"])
    current = (BASE / (NAME + ".xlsx")).read_bytes()
    digest = hashlib.sha256(current).hexdigest()
    required(digest == doc["currentWorkbookSha256"] == doc["workbookSnapshot"]["sha256"] == v["workbook_sha256"], "current saved workbook binary SHA-256 and master metadata")
    with zipfile.ZipFile(io.BytesIO(current)) as book:
        required(book.testzip() is None, "current XLSX ZIP CRC")
        for path in book.namelist():
            if path.endswith((".xml", ".rels")):
                ET.fromstring(book.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                bad = [cell.get("r") for cell in ET.fromstring(book.read(path)).iter(S + "c") if cell.get("t") == "e"]
                required(not bad, "error-valued worksheet cell in " + path)
        wb = ET.fromstring(book.read("xl/workbook.xml"))
        sheet_nodes = wb.find(S + "sheets")
        names = [node.get("name") for node in sheet_nodes]
        required(names == v["workbook_sheets"] and len(names) == 26, "original 26 sheet names and order")
        rels = {x.get("Id"): x.get("Target") for x in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        mapped = {}
        for x in sheet_nodes:
            target = rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            mapped[x.get("name")] = target.lstrip("/") if target.startswith("/") else "xl/" + target
        for name, old_hash in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(book.read(mapped[name])).hexdigest() == old_hash, "original historical worksheet SHA: " + name)
        sheet, actual = data_rows(book.read(mapped["Master Crosswalk"]), 15)
        required(actual == grid, "all 5190 saved XLSX cells equal source grid")
        merges = [x.get("ref") for x in sheet.find(S + "mergeCells").findall(S + "mergeCell")]
        expected = ["A1:D1","E1:I1","J1:N1"] + [f"A{i+1}:O{i+1}" for i in doc["review_sections"]]
        required(merges == expected, "frozen source/other/foundational DIM groups and 15 section dividers")
        pane = sheet.find(S + "sheetViews").find(S + "sheetView").find(S + "pane")
        required(pane.get("xSplit") == "4" and pane.get("ySplit") == "2", "source cases and header frozen")
    required(v["tests"]["all_XLSX_grid_cells_exact"] and not v["tests"]["DIM_new_content_adopted"], "scoped actual workbook parity only; zero model adoption")
    print("PASS: current SOSA-D 329 rows / 15 columns / 26 original sheets, full XLSX-cell-to-source parity and exact SHA.")
    print("PASS: 76 original C239 concepts, 57 staged correspondence decisions across 38 rows; no source-authenticated DSDM/API class claims.")
    print("LIMIT: no native DSDM/IDL/OpenAPI file review, full C239 conformance, independent deployment, or new DIM adoption.")


def verify_current_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Read-only successor for the current source-backed, 26-sheet ISA22 master.

    The archived six-sheet Step06 checker below remains intact for historic
    content. This branch no longer contains the 2026-11-06 8-column schema.
    """
    import hashlib
    state = json.loads((BASE / "ISA_Correction_Status_07NOV2026.json").read_text(encoding="utf-8"))
    evidence = json.loads((BASE / "ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json").read_text(encoding="utf-8"))
    record = json.loads((BASE / "ISA22_Validated_Workbook_Record_09NOV2026.json").read_text(encoding="utf-8"))
    mirror_md = (BASE / "ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    grid = doc["review_grid"]
    required(len(grid) == 346 and len(doc["rows"]) == 329 and len(doc["columns"]) == 14, "current grid / row / column counts")
    required(all(len(row) == 14 for row in grid) and mirror == grid, "current JSON/CSV 346x14 exact parity")
    required(md.split("\n", 1)[1] == mirror_md.split("\n", 1)[1], "current Markdown and review mirror bodies")
    required(len(doc["originalDonorEvidence"]) == 58 and len(doc["caseEvidence"]) == 73, "original donor/case evidence preserved")
    required(doc["columns"][-1]["key"] == "DIM" and [x["key"] for x in doc["columns"][:4]] == ["Dragino", "AirGradient", "Campbell", "Bennett"], "case-left / DIM-right layout")
    required(len(evidence["original_row_and_case_targets"]) == 31 and len(evidence["original_earlier_findings"]) == 25 and len(evidence["six_precise_source_questions"]) == 6, "31/25/six source audit")
    required(all(x["question_closed"] is False for x in evidence["six_precise_source_questions"]), "six exact source questions remain open")
    required(doc["ISAEvidence"]["currentPrimaryReviews"] == 480 and doc["ISAEvidence"]["sourceSupportedPrimary"] == 474 and doc["ISAEvidence"]["specificQuestions"] == 6, "480/474/six catalogue")
    required(state["technicalIterationsCompleted"] == 41 and state["nextOnOwnerProceed"] == "BROADER-DONOR-CROSSWALK-STEP16-OWNER-REVIEW", "ISA22 completion and owner Step16 route")
    binary = (BASE / (NAME + ".xlsx")).read_bytes()
    digest = hashlib.sha256(binary).hexdigest()
    required(digest == doc["currentWorkbookSha256"] == state["workbookSnapshot"]["sha256"] == record["workbook_sha256"], "GitHub current saved workbook SHA-256")
    with zipfile.ZipFile(io.BytesIO(binary)) as book:
        required(book.testzip() is None, "current workbook ZIP CRC")
        for path in book.namelist():
            if path.endswith((".xml", ".rels")):
                ET.fromstring(book.read(path))
        root = ET.fromstring(book.read("xl/workbook.xml"))
        sheets = [x.get("name") for x in root.find(S+"sheets")]
        required(sheets == record["sheets"] and len(sheets) == 26, "26 original workbook sheets in order")
        required(len(record["updated_tabs"]) == 10 and len(record["untouched_original_tabs"]) == 16, "ten current and sixteen preserved worksheet views")
        rels={x.attrib["Id"]:x.attrib["Target"] for x in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        master_path=None
        for node in root.find(S+"sheets"):
            if node.get("name") == "Master Crosswalk":
                target=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
                master_path=target.lstrip("/") if target.startswith("/") else "xl/"+target
                break
        required(master_path is not None, "current primary sheet target found")
        master, actual = data_rows(book.read(master_path), 14)
        required(actual == grid, "every current saved master XLSX cell matches source JSON")
        merges = [x.attrib["ref"] for x in master.find(S+"mergeCells").findall(S+"mergeCell")]
        want = ["A1:D1", "E1:H1", "I1:M1"] + [f"A{i+1}:N{i+1}" for i in doc["review_sections"]]
        required(merges == want, "case and donor group/section full-width merges")
        view = master.find(S+"sheetViews").find(S+"sheetView")
        pane = view.find(S+"pane")
        required(pane is not None and pane.get("xSplit") == "4" and pane.get("ySplit") == "2", "frozen case and column header panes")
        for node in book.namelist():
            if node.startswith("xl/worksheets/") and node.endswith(".xml"):
                bad = [c.get("r") for c in ET.fromstring(book.read(node)).iter(S+"c") if c.get("t") == "e"]
                required(not bad, f"Excel error-value cells in {node}: {bad[:5]}")
    required(record["counts"]["source_blocks"] == 279 and record["counts"]["DMS_outcomes"] == 480 and record["counts"]["DIM_adopted"] == 0, "source inventory and no DIM adoption")
    print("PASS: current ISA22 26-sheet workbook exact cell/merge/freeze/ZIP/XML/error scan and SHA-256 parity with source master.")
    print("PASS: 329 rows, 346 display rows, 14 columns, 480 DMS entries, 279 original source blocks, 31/25/six audit, 58 donor and 73 case records, no DIM adoption.")
    print("LIMIT: original-source interpretation, vendor authenticity, full ISA/OGC ATS and actual equipment conformance are separate from this scoped workbook verification.")


def verify_sosa_g2_1_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """G2-1 live text vs exactly verified preserved SOSA-D workbook checkpoint."""
    import hashlib
    import html
    old_l = json.loads((BASE / "Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    old_v = json.loads((BASE / "Step17_SOSA_D_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
    ledger = json.loads((BASE / "SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    grid = doc["review_grid"]
    required(doc["schemaVersion"] == "0.12" and len(doc["rows"]) == 329, "G2-1 schema, 329 unchanged source rows")
    required(len(doc["columns"]) == 15 and doc["columns"][8]["key"] == "OpenGroupSOSA" and doc["columns"][9]["key"] == "SOSA" and doc["columns"][-1]["key"] == "DIM", "independent Open Group/W3C and rightmost DIM")
    required([x["key"] for x in doc["columns"][:4]] == ["Dragino", "AirGradient", "Campbell", "Bennett"], "four case columns left")
    required(len(grid) == 346 and all(len(row) == 15 for row in grid) and mirror == grid, "full current JSON/CSV grid")
    required(len(doc["originalDonorEvidence"]) == 58 and len(doc["caseEvidence"]) == 73, "all original donor and case records present")
    required(doc["ISAEvidence"]["currentPrimaryReviews"] == 480 and doc["ISAEvidence"]["specificQuestions"] == 6, "ISA evidence still present")
    required(len(old_l["all_57_qualified_source_decisions"]) == 57 and len(old_l["integration_row_ledger"]) == 38, "previous SOSA-D source evidence")
    required(len(ledger["items"]) == 201 and len({x["id"] for x in ledger["items"]}) == 201, "201 original native G2-1 item IDs")
    required(sum(x["kind"] == "RULE" for x in ledger["items"]) == 6, "6 separate explicit C239 Rules")
    required(sum(x["support"] == "V1.0" for x in ledger["items"] if x["kind"] != "RULE") == 129, "129 V1.0 printed function/interaction entries")
    required(sum(x["support"] == "Future" for x in ledger["items"] if x["kind"] != "RULE") == 66, "66 Future printed function/interaction entries")

    # Verify EVERY GitHub-readable body cell against the current 346x15 grid.
    required("<tbody>" in md and "</tbody>" in md, "complete readable donor comparison")
    table = md.split("<tbody>", 1)[1].split("</tbody>", 1)[0]
    readable = []
    for fragment in re.findall(r"<tr>.*?</tr>", table, re.S):
        if 'colspan="15"' in fragment:
            section = re.search(r'<th colspan="15">(.*?)</th>', fragment, re.S)
            required(section is not None, "15-column topic divider")
            readable.append([html.unescape(section.group(1))] + [""] * 14)
        else:
            cells = [html.unescape(x) for x in re.findall(r"<td>(.*?)</td>", fragment, re.S)]
            required(len(cells) == 15, "complete 15-column readable source row")
            readable.append(cells)
    required(readable == grid[2:] and md.count('colspan="15"') == 15, "all current Markdown cells match JSON/CSV exactly")
    # BOTH independently named CSV and GitHub-readable mirror files must stay current.
    with (BASE / "ISA_Correction_Review_07NOV2026.csv").open(newline="", encoding="utf-8") as twin_csv:
        required(list(csv.reader(twin_csv)) == mirror, "second CSV mirror matches canonical 346x15 grid")
    twin_md = (BASE / "ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in twin_md and twin_md.split("<table>", 1)[1] == md.split("<table>", 1)[1], "both GitHub-readable comparisons match exactly")


    # Reconstruct the exact old saved XLSX grid by reverting ONLY qualified G2-1 SOSA cells.
    prior_source_cells = {x["row_id"]: x["display_cell"] for x in old_l["integration_row_ledger"]}
    item_ids = {x["id"] for x in ledger["items"]}
    prior_grid = [list(row) for row in grid]
    changed = []
    for row in doc["rows"]:
        old_cell = prior_source_cells.get(row["row_id"], "Not assessed here")
        new_cell = row["display"][8]
        ev = row.get("G2_1_source_correspondence")
        if ev:
            required(ev["relation"] in ("RELATED", "PARTIAL") and ev["DIM_adopted"] is False, "only qualified donor correspondence")
            required(bool(ev["source_item_ids"]) and all(x in item_ids for x in ev["source_item_ids"]), "native source IDs for "+row["row_id"])
            required(new_cell != old_cell and (new_cell.startswith(old_cell + " · ") if old_cell != "Not assessed here" else new_cell.startswith("Related only · ")), "preserve old SOSA-D value and add bounded evidence")
            matches = [i for i, r in enumerate(grid) if r[14] == row["label"] and r[8] == new_cell]
            required(len(matches) == 1, "unique G2-1 grid row: "+row["row_id"])
            prior_grid[matches[0]][8] = old_cell
            changed.append(row["row_id"])
        else:
            required(new_cell == old_cell, "unchanged SOSA-D cell: "+row["row_id"])
    required(len(changed) == 12 and set(changed) == set(doc["workbookSnapshot"]["G2_1_affected_row_ids"]), "exactly 12 new SOSA cells, unchanged other rows")
    synced=bool(doc["workbookSnapshot"]["currently_matches_readable_view"])
    if synced:
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-1-CANONICAL-VERIFIED","G2-1 current snapshot")
        validated=json.loads((BASE/"SOSA_G2_1_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
        required(validated["G2_1_source_qualified_updated_cells"]==12 and validated["tests"]["all_XLSX_grid_cells_exact"],"saved G2-1 workbook source/cell evidence")
    else:
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-D-PRE-G2-1","declared unsynced old workbook")
        validated=old_v

    # Check actual old binary, all historical sheets and ALL source cells at saved snapshot.
    workbook = (BASE / (NAME + ".xlsx")).read_bytes()
    digest = hashlib.sha256(workbook).hexdigest()
    required(digest == doc["currentWorkbookSha256"] == doc["workbookSnapshot"]["sha256"] == validated["workbook_sha256"], "saved old XLSX hash and explicitly retained metadata")
    with zipfile.ZipFile(io.BytesIO(workbook)) as archive:
        required(archive.testzip() is None, "saved XLSX CRC")
        for p in archive.namelist():
            if p.endswith((".xml", ".rels")):
                ET.fromstring(archive.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                errors = [c.get("r") for c in ET.fromstring(archive.read(p)).iter(S + "c") if c.get("t") == "e"]
                required(not errors, "Excel error-valued cells in "+p)
        root = ET.fromstring(archive.read("xl/workbook.xml"))
        sheets = root.find(S + "sheets")
        names = [s.get("name") for s in sheets]
        required(names == validated["workbook_sheets"] and len(names) == 26, "26 original sheets in order")
        rels = {r.get("Id"):r.get("Target") for r in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
        sheet_paths = {}
        for entry in sheets:
            target = rels[entry.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            sheet_paths[entry.get("name")] = target.lstrip("/") if target.startswith("/") else "xl/" + target
        for n, h in validated["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(archive.read(sheet_paths[n])).hexdigest() == h, "original source evidence sheet unchanged: "+n)
        sheet, actual = data_rows(archive.read(sheet_paths["Master Crosswalk"]), 15)
        required(actual == (grid if synced else prior_grid), "saved 346x15 XLSX matches its correctly declared checkpoint; current G2-1 if synced, prior SOSA-D if lagged")
        merges = [x.get("ref") for x in sheet.find(S + "mergeCells").findall(S + "mergeCell")]
        expected = ["A1:D1", "E1:I1", "J1:N1"] + [f"A{i+1}:O{i+1}" for i in doc["review_sections"]]
        required(merges == expected, "15 topic merged dividers preserved")
        pane = sheet.find(S + "sheetViews").find(S + "sheetView").find(S + "pane")
        required(pane.get("xSplit") == "4" and pane.get("ySplit") == "2", "four source case columns and header frozen")
    print("PASS: CURRENT G2-1 canonical JSON/CSV/Markdown exact 346x15 parity; 12 source-qualified SOSA-only updates, 201 native source items and 6 Rules.")
    if synced:
        print("PASS: saved 26-sheet G2-1 XLSX all 346x15 cells match live source/CSV/Markdown, exactly twelve SOSA source edits relative to older snapshot.")
    else:
        print("PASS: old SOSA-D saved XLSX exact; exactly twelve current source-text cells deliberately lag.")
    print("LIMIT: no original native DSDM/IDL/OpenAPI review, comprehensive donor completeness, runtime conformance or DIM adoption.")



def verify_sosa_g2_2_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """C239 G2-2: prove current four-text parity and exact saved same-workbook checkpoint or named 22-cell lag."""
    import hashlib
    import html
    base = json.loads((BASE/"Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    prev_v = json.loads((BASE/"SOSA_G2_1_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
    g1 = json.loads((BASE/"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g2 = json.loads((BASE/"SOSA_G2_2_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    rows=doc["rows"]; grid=doc["review_grid"]
    required(doc["schemaVersion"]=="0.13" and len(rows)==329, "G2-2 source schema and 329 stable information rows")
    required(len(doc["columns"])==15 and doc["columns"][8]["key"]=="OpenGroupSOSA" and doc["columns"][9]["key"]=="SOSA"
        and doc["columns"][-1]["key"]=="DIM", "source donor separation and DIM-last")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four source cases left")
    required(len(grid)==346 and all(len(row)==15 for row in grid) and grid[1]==[c["name"] for c in doc["columns"]],"346x15 live horizontal grid")
    required(mirror==grid,"current canonical JSON/CSV exact parity")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid, "BOTH current CSV mirrors exact")
    second=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==second.split("<table>",1)[1],"BOTH current readable comparisons exact")
    content=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for part in re.findall(r"<tr>.*?</tr>",content,re.S):
        if 'colspan="15"' in part:
            h=re.search(r'<th colspan="15">(.*?)</th>',part,re.S)
            required(h is not None,"source topic divider")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",part,re.S)]
            required(len(vals)==15,"full readable source/donor/DIM row")
            readable.append(vals)
    required(readable==grid[2:] and md.count('colspan="15"')==15,"all 344 current readable body rows and 15 dividers match source grid")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
        and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
        "original donor, case and ISA evidence retained")
    required(len(base["all_57_qualified_source_decisions"])==57 and len(base["integration_row_ledger"])==38,"original SOSA-D evidence retained")
    required(len(g1["items"])==201, "earlier G2-1 native item evidence preserved")
    items=g2["source_items"]; labeled=g2["original_rule_appearances"]; ids={x["id"] for x in items+labeled}
    required(len(items)==340 and len(labeled)==12 and len(ids)==352,"352 unique native C239 source items/Rule appearances")
    required(sum(x["support"]=="V1.0" for x in items)==208 and sum(x["support"]=="Future" for x in items)==132,
        "208 V1.0 /132 Future actual source table entries")
    required(sum(x["normative_standing"]=="RULE_SHALL" for x in labeled)==10
        and sum(x["normative_standing"]=="RULE_LABELED_DESCRIPTIVE" for x in labeled)==2,
        "10 source shall / two source descriptive Rule labels")
    require_old=doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-1-PRE-G2-2"
    synced=doc["workbookSnapshot"]["currently_matches_readable_view"] is True
    if synced:
        v=json.loads((BASE/"SOSA_G2_2_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-2-CANONICAL-VERIFIED","new saved G2-2 checkpoint")
        required(v["G2_2_qualified_source_cell_count"]==22 and len(v["changed_saved_cells"])==22
            and all(re.fullmatch(r"I\d+",x) for x in v["changed_saved_cells"]), "only 22 original SOSA column I saved-cell changes")
        required(all(v["checks"][k] for k in ("actual_XLSX_all_346x15_equal_current_JSON_and_CSV",
            "both_CSV_and_GitHub_readable_mirrors_exact","same_26_worksheet_names_order",
            "22_unmodified_historical_sheets_XML_byte_identical","only_22_original_SOSA_I_column_cells_changed")),
            "G2-2 actual saved-cell validation report")
    else:
        required(require_old,"explicit G2-2 22-cell prepublication checkpoint")
        v=prev_v
    previous_grid=[list(x) for x in grid]
    selected=[]
    for row in rows:
        selected_ev=row.get("G2_2_source_correspondence")
        if selected_ev:
            required(selected_ev["source_item_ids"] and all(x in ids for x in selected_ev["source_item_ids"]),
                "original G2-2 source IDs for "+row["row_id"])
            required(selected_ev["dim_adopted"] is False and selected_ev["api_schema_bytes_read"] is False,
                "no new source-unsupported DIM adoption/native API claim")
            now=row["display"][8]
            required("G2-2:" in now,"G2-2 readable source qualification "+row["row_id"])
            if now.startswith("Related only · G2-2:"):
                old="Not assessed here"
            else:
                required(" · G2-2:" in now,"append only qualified older SOSA source")
                old=now.rsplit(" · G2-2:",1)[0]
            hits=[i for i,r in enumerate(grid) if r[8]==now and r[14]==row["label"]]
            required(len(hits)==1,"unique source row "+row["row_id"])
            previous_grid[hits[0]][8]=old
            selected.append(row["row_id"])
    required(len(selected)==22 and set(selected)==set(doc["workbookSnapshot"]["G2_2_affected_row_ids"]),
        "exactly 22 source-qualified row IDs accounted and no other source deltas")
    required(sum(bool(r.get("G2_1_source_correspondence")) for r in rows)==12,"G2-1 source evidence preserved")
    data=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
        "actual saved workbook hash matches its stated checkpoint")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        required(z.testzip() is None,"valid actual saved workbook ZIP")
        for f in z.namelist():
            if f.endswith((".xml",".rels")):
                ET.fromstring(z.read(f))
            if f.startswith("xl/worksheets/") and f.endswith(".xml"):
                errors=[c.get("r") for c in ET.fromstring(z.read(f)).iter(S+"c") if c.get("t")=="e"]
                required(not errors,"no Excel formula/error type cells in "+f)
        root=ET.fromstring(z.read("xl/workbook.xml"))
        sheets=root.find(S+"sheets")
        names=[x.get("name") for x in sheets]
        required(names==v["workbook_sheets"] and len(names)==26,"26 original sheet names/order preserved")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        mapped={}
        for entry in sheets:
            target=rels[entry.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            mapped[entry.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for title,stored in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(mapped[title])).hexdigest()==stored,
                "original supporting sheet preserved by bytes "+title)
        sheet,actual=data_rows(z.read(mapped["Master Crosswalk"]),15)
        required(actual==(grid if synced else previous_grid),
            "all 346x15 saved cells match declared current G2-2 source grid or precisely reverted 22-cell prior snapshot")
        merge=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        expected=["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]]
        required(merge==expected, "exact original 15-column section groups/merges")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","frozen source cases/header")
    print("PASS: 340 original C239 source table items + 12 source Rule appearances with 208/132 support grades; 22 bounded SOSA master qualifications.")
    print("PASS: BOTH CSV and BOTH readable comparisons exactly equal 346x15 canonical JSON source; all 58 donor, 73 case, 480 ISA evidence preserved.")
    print("PASS: saved 26-sheet workbook verified at "+("CURRENT G2-2 source 346x15 parity" if synced else "OLDER G2-1 exact 22-cell lag")+".")
    print("LIMIT: no original native API/DSDM/IDL source contents, full SOSA donor audit, independent physical control or DIM/Profile adoption.")

def verify_sosa_g2_3_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """G2-3 original source inventory and both-text + SAME saved 26-sheet workbook parity."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.14" and len(rows)==329 and len(doc["columns"])==15 and len(grid)==346,"G2-3 329x15 stable canonical master")
    required(all(len(r)==15 for r in grid) and mirror==grid,"canonical JSON and first CSV 346x15")
    required(doc["columns"][8]["key"]=="OpenGroupSOSA" and doc["columns"][9]["key"]=="SOSA" and doc["columns"][-1]["key"]=="DIM","Open Group SOSA separate from W3C and DIM rightmost")
    required([c["key"] for c in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four source columns left")
    required(grid[1]==[c["name"] for c in doc["columns"]],"source names and order")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as second_csv:
        required(list(csv.reader(second_csv))==grid,"BOTH CSV mirrors exact source grid")
    second_md=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==second_md.split("<table>",1)[1],"both readable comparisons identical")
    readable=[]
    content=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    for snippet in re.findall(r"<tr>.*?</tr>",content,re.S):
        if 'colspan="15"' in snippet:
            d=re.search(r'<th colspan="15">(.*?)</th>',snippet,re.S)
            required(d is not None,"full-width topic divider")
            readable.append([html.unescape(d.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",snippet,re.S)]
            required(len(vals)==15,"complete 15-column comparison row")
            readable.append(vals)
    required(readable==grid[2:] and md.count('colspan="15"')==15,"all GitHub-readable table cells match source")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
        and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,"historical donor, case and ISA evidence")
    prior_d=json.loads((BASE/"Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    g1=json.loads((BASE/"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g2=json.loads((BASE/"SOSA_G2_2_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g3=json.loads((BASE/"SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json").read_text(encoding="utf-8"))
    required(len(prior_d["all_57_qualified_source_decisions"])==57 and len(prior_d["integration_row_ledger"])==38,"SOSA-D source retained")
    required(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352,"G2-1 and G2-2 original research retained")
    clauses=g3["source_clauses"];states=g3["source_states"];context=g3["architectural_context"];ids={x["id"] for x in clauses+states+context}
    required(len(clauses)==76 and len(states)==32 and len(context)==11 and len(ids)==119 and g3["counts"]["source_items"]==119,"119 unique original G2-3 source objects")
    required(g3["counts"]["normative_rule_labels"]==49 and g3["counts"]["rule_shall"]==48 and g3["counts"]["rule_incomplete"]==1
        and g3["counts"]["recommendations"]==8 and g3["counts"]["observations"]==11 and g3["counts"]["permissions"]==8,"original source grades")
    required(sum(bool(r.get("G2_1_source_correspondence")) for r in rows)==12
        and sum(bool(r.get("G2_2_source_correspondence")) for r in rows)==22,"previous progressive SOSA comparison preserved")
    updated=[r for r in rows if r.get("G2_3_source_correspondence")]
    required(len(updated)==28 and set(r["row_id"] for r in updated)==set(doc["workbookSnapshot"]["G2_3_affected_row_ids"]),"28 source-qualified master changes")
    older_grid=[list(r) for r in grid]
    for row in updated:
        ev=row["G2_3_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]), "native G2-3 original source evidence IDs "+row["row_id"])
        required(ev["DIM_adopted"] is False and ev["native_external_references_read"] is False,"grade of donor contribution "+row["row_id"])
        now=row["display"][8]
        if now.startswith("Related only · G2-3:"):
            old_cell="Not assessed here"
        else:
            required(" · G2-3:" in now,"G2-3 donor cell must preserve earlier content")
            old_cell=now.rsplit(" · G2-3:",1)[0]
        hits=[i for i,g in enumerate(grid) if g[14]==row["label"] and g[8]==now]
        required(len(hits)==1,"unique approved existing source row "+row["row_id"])
        older_grid[hits[0]][8]=old_cell
    synced=doc["workbookSnapshot"]["currently_matches_readable_view"] is True
    if synced:
        v=json.loads((BASE/"SOSA_G2_3_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-3-CANONICAL-VERIFIED","source and Excel must identify G2-3 checkpoint")
        required(v["G2_3_qualified_source_cell_count"]==28 and len(v["changed_saved_cells"])==28,"28 actual workbook changes")
        required(all(re.fullmatch(r"I\d+",a) for a in v["changed_saved_cells"]),"28 saved changes confined to SOSA column I")
        required(all(v["checks"][key] for key in ("actual_XLSX_all_346x15_equal_current_JSON_CSV","two_CSV_and_two_Markdown_comparisons_equal",
            "same_26_worksheet_names_order","22_historical_worksheet_XML_bytes_preserved",
            "only_28_original_SOSA_I_column_cells_changed","ZIP_CRC_and_XML_valid","zero_XLSX_error_type_cells","zero_DIM_Profile_adoption")),
            "validated saved workbook and preservation claims")
    else:
        v=json.loads((BASE/"SOSA_G2_2_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-2-PRE-G2-3","prepublication exact named G2-2 saved snapshot")
    x=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(x).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],"actual saved XLSX hash exact to stated source checkpoint")
    with zipfile.ZipFile(io.BytesIO(x)) as z:
        required(z.testzip() is None,"valid zipped saved XLSX")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):
                ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                bad=[c.get("r") for c in ET.fromstring(z.read(p)).iter(S+"c") if c.get("t")=="e"]
                required(not bad,"no Excel error-type cell in "+p)
        root=ET.fromstring(z.read("xl/workbook.xml"));sheetNodes=root.find(S+"sheets")
        names=[node.get("name") for node in sheetNodes]
        required(names==v["workbook_sheets"] and len(names)==26,"26 original worksheet names/order")
        rels={n.get("Id"):n.get("Target") for n in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in sheetNodes:
            dest=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=dest.lstrip("/") if dest.startswith("/") else "xl/"+dest
        for n,hash_saved in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[n])).hexdigest()==hash_saved,"historical worksheet intact: "+n)
        sheet,actual=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(actual==(grid if synced else older_grid),
            "every single saved 346x15 master cell equals current G2-3 source or exact declared prior 28-cell snapshot")
        merges=[a.get("ref") for a in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        expected=["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]]
        required(merges==expected,"exact unchanged topic separator/group merge positions")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","case/header freeze")
    print("PASS: G2-3 119 original source items, 28 qualified SOSA cells, JSON/both CSV/both Markdown 346x15 parity, 58 donor and 73 case facts retained.")
    print("PASS: SAME 26-sheet saved workbook at "+("CURRENT G2-3 all-cell parity" if synced else "exact 28-cell prior G2-2 source snapshot")+".")
    print("LIMIT: external ANSI/VITA/HOST/IPMI and C239 DSDM/IDL/OpenAPI unread; full donor source completion, DIM adoption and runtime conformance not claimed.")


def verify_sosa_g2_4a_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """G2-4A: original Chapter1–5 coverage, four source formats and same verified 26-sheet Excel."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(doc["columns"])==15 and len(grid)==346,"G2-4A live 329-row/15-column master")
    required(all(len(x)==15 for x in grid) and mirror==grid,"canonical structured source matches first CSV 346x15")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four original equipment cases left")
    required([x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"] and doc["columns"][-1]["key"]=="DIM","Open Group SOSA distinct from W3C; DIM last")
    required(grid[1]==[c["name"] for c in doc["columns"]],"preserve all source headings/order")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"both CSV mirrors equal current live master")
    other_md=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==other_md.split("<table>",1)[1],"both GitHub-readable comparison bodies equal")
    table=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    body=[]
    for fragment in re.findall(r"<tr>.*?</tr>",table,re.S):
        if 'colspan="15"' in fragment:
            h=re.search(r'<th colspan="15">(.*?)</th>',fragment,re.S)
            required(h is not None,"15-column topic group divider")
            body.append([html.unescape(h.group(1))]+[""]*14)
        else:
            cells=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",fragment,re.S)]
            required(len(cells)==15,"complete donor/case/DIM source comparison row")
            body.append(cells)
    required(body==grid[2:] and md.count('colspan="15"')==15,"all GitHub-readable comparison grid cells equal source")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
        and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
        "historical donor/real cases/ISA source records preserved")
    earlier=json.loads((BASE/"Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    g1=json.loads((BASE/"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g2=json.loads((BASE/"SOSA_G2_2_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g3=json.loads((BASE/"SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json").read_text(encoding="utf-8"))
    g4=json.loads((BASE/"SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    required(len(earlier["all_57_qualified_source_decisions"])==57 and len(earlier["integration_row_ledger"])==38,"SOSA-D earlier selected meanings intact")
    required(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352 and g3["counts"]["source_items"]==119,"G2-1/2/3 prior source records retained")
    items=g4["original_source_items"];ids={x["id"] for x in items}
    required(len(items)==95 and len(ids)==95 and len(g4["chapter1_5_toc_coverage"])==42 and len(g4["chapter7_11_pending"])==27,"original Chapter1–5 inventory and pending 7–11 exact")
    required(g4["item_counts"]["QUALITY_ATTRIBUTE"]==10 and g4["item_counts"]["ARCHITECTURE_PRINCIPLE"]==15 and g4["item_counts"]["MODULE_CATALOG"]==27,"10/15/27 native original concepts")
    required(g4["item_counts"]["previously_G1_UNREAD_1_5"]==27 and g4["item_counts"]["previously_G1_sampled_1_5"]==15,"bounded heading coverage from old G1")
    required(g4["source"]["native_DSDM_IDL_OpenAPI_externally_referenced_files_read"] is False and g4["dim_profile_adopted"] is False,"native companion/DIModel still unadopted")
    for count,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),(28,"G2_3_source_correspondence")):
        required(sum(bool(row.get(key)) for row in rows)==count,"prior progressive SOSA evidence: "+key)
    changed=[x for x in rows if x.get("G2_4A_source_correspondence")]
    required(len(changed)==20 and {x["row_id"] for x in changed}==set(doc["workbookSnapshot"]["G2_4A_affected_row_ids"]),"20 new qualified original master rows only")
    older=[list(r) for r in grid]
    for r in changed:
        ev=r["G2_4A_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]), "source-qualified original Chapter 1–5 ids "+r["row_id"])
        required(ev["DIM_adopted"] is False and ev["unverified_native_companions"],"native original limitations/zero adoption "+r["row_id"])
        current=r["display"][8];previous=ev["previous_sosa_cell_value"]
        required(current!=previous and "G2-4A:" in current,"old SOSA cell preserved separately "+r["row_id"])
        matches=[i for i,g in enumerate(grid) if g[8]==current and g[14]==r["label"]]
        required(len(matches)==1,"unique existing master source row "+r["row_id"])
        older[matches[0]][8]=previous
    synced=doc["workbookSnapshot"]["currently_matches_readable_view"] is True
    if synced:
        v=json.loads((BASE/"SOSA_G2_4A_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-4A-CANONICAL-VERIFIED","current Excel saved checkpoint")
        required(v["G2_4A_qualified_existing_source_cells"]==20 and len(v["changed_saved_cells"])==20
            and all(re.fullmatch(r"I\d+",a) for a in v["changed_saved_cells"]),"20 actual saved The Open Group SOSA only I-column changes")
        required(all(v["checks"][k] for k in ("all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD",
            "two_CSV_mirrors_equal","two_GitHub_readable_comparisons_equal","same_26_worksheet_names_order",
            "22_historical_worksheet_XML_bytes_preserved","only_20_original_SOSA_I_column_cells_changed",
            "valid_ZIP_CRC_and_XML","zero_XLSX_error_type_cells","zero_DIM_Profile_adoption")),"saved binary verification evidence")
    else:
        v=json.loads((BASE/"SOSA_G2_3_Workbook_Validation_09NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-3-PRE-G2-4A","named old verified G2-3 snapshot before new XLSX publication")
    x=(BASE/(NAME+".xlsx")).read_bytes();digest=hashlib.sha256(x).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],"actual saved workbook binary SHA matches master and validation")
    with zipfile.ZipFile(io.BytesIO(x)) as z:
        required(z.testzip() is None,"saved workbook valid ZIP CRC")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):
                ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                bad=[c.get("r") for c in ET.fromstring(z.read(p)).iter(S+"c") if c.get("t")=="e"]
                required(not bad,"no error-valued Excel worksheet cell in "+p)
        root=ET.fromstring(z.read("xl/workbook.xml"));sn=root.find(S+"sheets")
        names=[v.get("name") for v in sn]
        required(names==v["workbook_sheets"] and len(names)==26,"26 original sheet names/order preserved")
        rels={a.get("Id"):a.get("Target") for a in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in sn:
            target=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for name,oldHash in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==oldHash,"untouched historical evidence sheet "+name)
        sheet,actual=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(actual==(grid if synced else older),
            "every actual saved 346x15 source grid cell equals CURRENT G2-4A or exact reconstructed 20-cell older G2-3 snapshot")
        merges=[a.get("ref") for a in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        want=["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]]
        required(merges==want,"15 source-topic dividers and header group merges retained")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","four source cases frozen and headers")
    print("PASS: original C239 42 headings/95 source items, 20 qualified SOSA cells and both CSV/Markdown mirrors full source parity.")
    print("PASS: SAME saved canonical 26-sheet Excel "+("CURRENT G2-4A exact 346x15 source-cell parity." if synced else "prior G2-3 exact snapshot, 20 newer source-text cells held.") )
    print("LIMIT: Chapters7–11, referenced SOSA native DSDM/API, original RIG and figure geometry not fully audited; no DIM/Profile adoption.")


def verify_sosa_g2_4b_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Read-only independent current G2-4B source-native and saved 26-sheet Excel checks."""
    import hashlib
    import html
    rows=doc["rows"];grid=doc["review_grid"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346 and len(doc["columns"])==15,"G2-4B preserves 329 source rows, 346 review rows and 15 columns")
    required(all(len(x)==15 for x in grid) and mirror==grid,"canonical JSON and CSV exact 346x15 source parity")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
        and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
        and doc["columns"][-1]["key"]=="DIM","source cases, distinct Open Group/W3C SOSA and rightmost DIM preserved")
    required(grid[1]==[c["name"] for c in doc["columns"]],"canonical column sequence preserved")
    sections=set(doc["review_sections"])
    required(len(sections)==15 and [r for i,r in enumerate(grid) if i>1 and i not in sections]==[r["display"] for r in rows],"all source information row positions preserved")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"BOTH CSV mirrors exact source parity")
    other_md=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==other_md.split("<table>",1)[1],"BOTH GitHub-readable comparison tables exactly identical")
    tbody=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    body=[]
    for fragment in re.findall(r"<tr>.*?</tr>",tbody,re.S):
        if 'colspan="15"' in fragment:
            heading=re.search(r'<th colspan="15">(.*?)</th>',fragment,re.S)
            required(heading is not None,"15-column source group divider")
            body.append([html.unescape(heading.group(1))]+[""]*14)
        else:
            cells=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",fragment,re.S)]
            required(len(cells)==15,"all master row table cells present")
            body.append(cells)
    required(body==grid[2:] and md.count('colspan="15"')==15,"actual readable Markdown grid matches all JSON source cells")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
        and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
        "all earlier donor and empirical-case/ISA evidence retained")
    earlier=json.loads((BASE/"Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    g1=json.loads((BASE/"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g2=json.loads((BASE/"SOSA_G2_2_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g3=json.loads((BASE/"SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json").read_text(encoding="utf-8"))
    g4=json.loads((BASE/"SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    g5=json.loads((BASE/"SOSA_G2_4B_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    required(len(earlier["all_57_qualified_source_decisions"])==57 and len(earlier["integration_row_ledger"])==38,"original SOSA-D contributions retained")
    required(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352 and g3["counts"]["source_items"]==119
        and len(g4["original_source_items"])==95,"source-native G2-1 through G2-4A evidence preserved")
    required(len(g5["chapter7_11_toc_coverage"])==27 and all(h["G2_4B_status"]=="ORIGINAL_INLINE_TEXT_TABLE_READ" for h in g5["chapter7_11_toc_coverage"]),
        "27 original C239 Chapters7–11 heading audit records")
    items=g5["original_source_items"];ids={x["id"] for x in items}
    required(len(items)==234 and len(ids)==234,"unique original source-native 234 item records")
    c=g5["source_item_counts"]
    required(c["TASK_INTERACTION"]==36 and c["RF_INTERACTION"]==82 and c["CRE_SUPPORT_FUNCTION"]==20
        and c["STORAGE_RULE"]==5 and c["RF_RULE"]==3 and c["explicit_original_C239_shall_rules"]==8
        and c["REFERENCE_MODULE"]==9,"native preliminary/RF/future/reference/shall standing")
    c=g5["cumulative_C239_original_TOC_after_packet"]
    required(c["registered_total"]==192 and c["at_least_source_sampled_or_inline_read"]==121
        and c["still_substantively_unread"]==70 and c["one_restricted"]==1,
        "count source coverage separately from full-donor completeness")
    required(g5["source"]["original_native_model_companion_files_uninspected"]==8
        and g5["source"]["external_MORA_VICTORY_VITA_source_files_inspected"] is False,
        "native original source holds retained")
    for num,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
        (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence")):
        required(sum(bool(r.get(key)) for r in rows)==num,"preserved prior SOSA source evidence "+key)
    changed=[r for r in rows if r.get("G2_4B_source_correspondence")]
    required(len(changed)==29 and {r["row_id"] for r in changed}==set(doc["workbookSnapshot"]["G2_4B_affected_row_ids"]),
        "29 exact G2-4B qualified original source cells")
    for row in changed:
        ev=row["G2_4B_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),"native original source IDs on "+row["row_id"])
        required(ev["DIM_adopted"] is False and ev["unverified_native_companions"] is True,"source limitations and nonadoption on "+row["row_id"])
        required("G2-4B:" in row["display"][8] and row["display"][8]!=ev["previous_sosa_cell_value"]
            and ev["relation"] in {"DIRECT","PARTIAL","RELATED","BROADER","NARROWER","NO_ESTABLISHED","CONFLICT"},
            "qualified actual source comparison "+row["row_id"])
    v=json.loads((BASE/"SOSA_G2_4B_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-4B-CANONICAL-VERIFIED"
        and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
        and doc["workbookSnapshot"]["refreshed_cell_count"]==29,"actual G2-4B saved workbook checkpoint exact")
    required(v["G2_4B_original_inline_source_headings"]==27 and v["G2_4B_original_source_items"]==234
        and v["G2_4B_qualified_existing_source_cells"]==29 and len(v["changed_saved_cells"])==29
        and all(re.fullmatch(r"I\d+",x) for x in v["changed_saved_cells"]),
        "saved G2-4B original source-item/specific donor cell counts")
    required(all(v["checks"][k] for k in ("all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD",
        "two_CSV_mirrors_equal","two_GitHub_readable_comparisons_equal","same_26_worksheet_names_order",
        "22_historical_worksheet_XML_bytes_preserved","only_29_original_SOSA_I_column_cells_changed",
        "valid_ZIP_CRC_and_XML","zero_XLSX_error_type_cells","zero_DIM_Profile_adoption")),
        "reported all-saved-cell and untouched-sheet verified exit")
    book=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(book).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
        "real saved canonical workbook hash and JSON/check record agree")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved workbook ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not [c.get("r") for c in ET.fromstring(z.read(path)).iter(S+"c") if c.get("t")=="e"],
                    "no error-valued Excel cell in "+path)
        wb=ET.fromstring(z.read("xl/workbook.xml"));tabnames=[x.get("name") for x in wb.find(S+"sheets")]
        required(tabnames==v["workbook_sheets"] and len(tabnames)==26,"all 26 original worksheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        sheetpaths={}
        for x in wb.find(S+"sheets"):
            target=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            sheetpaths[x.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for name,oldhash in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(sheetpaths[name])).hexdigest()==oldhash,
                "22 original historical sheet contents preserved: "+name)
        root,actual=data_rows(z.read(sheetpaths["Master Crosswalk"]),15)
        required(actual==grid,"EVERY current saved 346x15 Excel cell matches canonical source and CSV/MD")
        merges=[a.get("ref") for a in root.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
            "main master section/divider merges")
        pane=root.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","case columns/frozen headers unchanged")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
        and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True
        and not doc["SOSAEvidence"]["G2_4B"]["model_adoption"],"no donor-closeout, next-donor, or DIM adoption")
    print("PASS: G2-4B 27 headings, 234 source-native items (8 scoped native SHALL), 29 qualified SOSA column-I updates.")
    print("PASS: current 329x15 JSON / TWO CSV / TWO Markdown / SAME 26-sheet actual saved 346x15 Excel; 22 untouched sheets; old sources and cases preserved.")
    print("LIMIT: 70 C239 headings unread, one restricted; original MORA and 8 native DSDM/IDL/OpenAPI files unread, no DIM/Profile adoption or device tests.")


def verify_sosa_g2_5_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """G2-5: original C239 Chapter12 coverage plus the SAME saved 26-sheet workbook, pre- or post-publication."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346 and len(doc["columns"])==15,
             "G2-5 canonical 329 original rows/346 display rows/15 original columns")
    required(all(len(r)==15 for r in grid) and mirror==grid,"JSON/current CSV all 346×15 source cells agree")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM","case columns, Open Group vs W3C SOSA and DIM rightmost")
    required(grid[1]==[x["name"] for x in doc["columns"]],"original donor column layout preserved")
    sections=set(doc["review_sections"])
    required(len(sections)==15 and [r for i,r in enumerate(grid) if i>1 and i not in sections]
            ==[r["display"] for r in rows],"every original stable source row value/section maintained")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror all 346×15 current source cells equal")
    other_md=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==other_md.split("<table>",1)[1],
             "two GitHub-readable horizontal source comparison table bodies equal")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    table=[]
    for frag in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in frag:
            h=re.search(r'<th colspan="15">(.*?)</th>',frag,re.S)
            required(h is not None,"topic divider text exists")
            table.append([html.unescape(h.group(1))]+[""]*14)
        else:
            v=[html.unescape(c) for c in re.findall(r"<td>(.*?)</td>",frag,re.S)]
            required(len(v)==15,"all 15 current donor comparison cells in Markdown row")
            table.append(v)
    required(table==grid[2:] and md.count('colspan="15"')==15,
             "Markdown source table all 344 body rows equal to canonical JSON source grid")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
             "historical donor, four source cases, 480 ISA outcomes/6 questions retained")
    earlier=json.loads((BASE/"Step17_SOSA_D_Source_First_Integration_09NOV2026.json").read_text(encoding="utf-8"))
    g1=json.loads((BASE/"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g2=json.loads((BASE/"SOSA_G2_2_Original_Item_Inventory_09NOV2026.json").read_text(encoding="utf-8"))
    g3=json.loads((BASE/"SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json").read_text(encoding="utf-8"))
    g4=json.loads((BASE/"SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    g5=json.loads((BASE/"SOSA_G2_4B_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    g6=json.loads((BASE/"SOSA_G2_5_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    required(len(earlier["all_57_qualified_source_decisions"])==57 and len(earlier["integration_row_ledger"])==38,
             "original SOSA-D selected original source evidence unchanged")
    required(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352
             and g3["counts"]["source_items"]==119 and len(g4["original_source_items"])==95
             and len(g5["original_source_items"])==234,"prior SOSA-G2-1/2/3/4A/4B original native ledgers preserved")
    required(len(g6["toc_heading_coverage"])==23 and len(g6["unregistered_nested_headings_read"])==6
             and len(g6["original_source_items"])==164,"23 original Chapter12 headings, six nested and 164 native item IDs")
    ids={i["id"] for i in g6["original_source_items"]}
    required(len(ids)==164,"unique stable original Chapter12 native source items")
    c=g6["native_source_item_counts"]
    required(c["RULE"]==38 and c["PERMISSION"]==9 and c["OBSERVATION"]==10
             and c["HOST_INTERACTION"]==43 and c["REFERENCE_ONLY_MODULE"]==7,
             "Chapter12 source normativity and 43 host interactions vs undefined module standing")
    g=g6["full_donor_source_coverage_after_packet"]
    required(g["registered_C239_heading_total"]==192 and g["at_least_original_source_sampled_or_inline_read"]==136
             and g["still_substantively_unread"]==55 and g["restricted_heading"]==1 and not g["source_fully_complete"],
             "C239 original source remains incomplete despite chapter audit")
    required(g6["source"]["native_DSDM_IDL_OpenAPI_originals_unread"]==8
             and not g6["source"]["external_companion_norms_audited"],
             "uninspected native companion/crypto sources not upgraded to evidence")
    for count,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
                      (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
                      (29,"G2_4B_source_correspondence")):
        required(sum(bool(r.get(key)) for r in rows)==count,"preserved earlier original SOSA source "+key)
    touched=[r for r in rows if r.get("G2_5_source_correspondence")]
    required(len(touched)==43 and {r["row_id"] for r in touched}==set(doc["workbookSnapshot"]["G2_5_affected_row_ids"]),
             "exactly 43 distinct source-qualified SOSA column-I cells")
    prior=[list(r) for r in grid]
    for row in touched:
        ev=row["G2_5_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
                 "actual original Rule/interaction source IDs for "+row["row_id"])
        required(ev["DIM_Profile_adopted"] is False and ev["native_companions_unreviewed"] is True,
                 "no source-invalid native content / no model adoption "+row["row_id"])
        current=row["display"][8]
        required("G2-5:" in current and current!=ev["previous_sosa_cell_value"],
                 "source-qualified new The Open Group SOSA cell "+row["row_id"])
        hit=[i for i,r in enumerate(grid) if r[8]==current and r[14]==row["label"]]
        required(len(hit)==1,"source row unique for "+row["row_id"])
        prior[hit[0]][8]=ev["previous_sosa_cell_value"]
    synced=doc["workbookSnapshot"]["currently_matches_readable_view"] is True
    if synced:
        required(doc["SOSAReviewCompletion"]["G2_5_XLSX_lag"]==0 and doc["SOSAEvidence"]["G2_5"]["excel_lagged_cells"]==0,
                 "G2-5 source text and saved workbook record zero outstanding lag")
        v=json.loads((BASE/"SOSA_G2_5_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-5-CANONICAL-VERIFIED",
                 "G2-5 same canonical saved Excel named checkpoint")
        required(v["G2_5_qualified_existing_sosa_cells"]==43 and len(v["changed_saved_cells"])==43
                 and all(re.fullmatch(r"I\d+",x) for x in v["changed_saved_cells"]),
                 "actual 43 SOSA I-column saved changes and no other column")
        required(all(v["checks"][k] for k in ("all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD",
                 "two_CSV_mirrors_equal","two_GitHub_readable_comparisons_equal",
                 "same_26_worksheet_names_order","22_historical_worksheet_XML_bytes_preserved",
                 "only_43_original_SOSA_I_column_cells_changed","valid_ZIP_CRC_and_XML",
                 "zero_XLSX_error_type_cells","zero_DIM_Profile_adoption")),"full saved-file evidence verdicts")
    else:
        v=json.loads((BASE/"SOSA_G2_4B_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-4B-SAVED_XLSX__G2_5_SOURCE_PENDING",
                 "precise G2-5 prepublication 43-cell older workbook snapshot")
        required(doc["SOSAReviewCompletion"]["G2_5_XLSX_lag"]==43,"mandatory workbook publication not claimed early")
    book=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(book).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved canonical Excel bytes exact to published source checkpoint SHA")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved Excel ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no saved Excel error-valued cells "+path)
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        nodes=list(wb.find(S+"sheets"))
        names=[x.get("name") for x in nodes]
        required(names==v["workbook_sheets"] and len(names)==26,"same 26 sheets/order preserved")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        sheetpaths={}
        for x in nodes:
            target=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            sheetpaths[x.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for name,h in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(sheetpaths[name])).hexdigest()==h,
                     "prior 22 historical worksheet exact source bytes "+name)
        master,actual=data_rows(z.read(sheetpaths["Master Crosswalk"]),15)
        required(actual==(grid if synced else prior),
                 "EVERY actual saved 346x15 source cell exact to current G2-5 or documented 43-cell older G2-4B snapshot")
        merges=[x.get("ref") for x in master.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "all 15 source section dividers and three header groups preserved")
        pane=master.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "frozen original four case columns and main headers")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True
             and doc["SOSAEvidence"]["G2_5"]["DIM_Profile_adopted"] is False,
             "donor source incomplete, no Step18/SAPIENT or DIM/Profile model decision")
    print("PASS: G2-5 original C239 Chapter12 23 headings/164 native items/38 Rules, 9 Permissions, 10 Observations, 43 host interactions, 43 qualified SOSA cells.")
    print("PASS: current source JSON, both CSV and both Markdown comparisons; saved workbook "+
          ("all current 346x15 source cells" if synced else "precisely named 43-cell older snapshot")+
          ", 26 sheets/22 unchanged historical evidence sheets.")
    print("LIMIT: 55 C239 headings unread, one restricted, eight original native model files and security/protocol companions unread; no DIM/Profile adoption or actual hardware test.")


def verify_sosa_g2_6a_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent C239 hardware source and same original saved Excel parity, pre/post L23 publisher."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346 and len(doc["columns"])==15,
        "original 329 source rows, 346 display rows, 15 columns")
    required(all(len(r)==15 for r in grid) and mirror==grid,"current JSON and first CSV 346x15 parity")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
        and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
        and doc["columns"][-1]["key"]=="DIM","case/source/OGC foundation/DIM column order unchanged")
    required(grid[1]==[x["name"] for x in doc["columns"]],"original source column headings exact")
    sections=set(doc["review_sections"])
    required(len(sections)==15 and [r for i,r in enumerate(grid) if i>1 and i not in sections]==[r["display"] for r in rows],
        "source grid exactly preserves 329 stable row values and all dividers")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror all current source cells")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==other.split("<table>",1)[1],"two identical readable horizontal tables")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    table=[]
    for frag in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in frag:
            h=re.search(r'<th colspan="15">(.*?)</th>',frag,re.S)
            required(h is not None,"group heading present")
            table.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",frag,re.S)]
            required(len(vals)==15,"15 cells for each source row")
            table.append(vals)
    required(table==grid[2:] and md.count('colspan="15"')==15,"all Markdown cells and topic groups match JSON")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
        and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
        "earlier donor, case and ISA facts/questions preserved")
    ledger=json.loads((BASE/"SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    ids={i["id"] for i in ledger["original_source_items"]}
    counts=ledger["source_counts"]
    required(len(ledger["original_toc_heading_coverage"])==13
        and len(ledger["additional_native_subclauses_read"])==19
        and len(ids)==168 and len(ledger["original_source_items"])==168,
        "13 registered C239 source headings, 19 additional subclauses, 168 unique native/analytical items")
    required(counts["RULE"]==98 and counts["PERMISSION"]==8 and counts["RECOMMENDATION"]==3
        and counts["OBSERVATION"]==21 and counts["TABLE"]==10 and counts["FIGURE"]==5
        and counts["COV_FIELD"]==11 and counts["ANALYTICAL_CONTEXT"]==12,
        "source Rule/Permission/Recommendation/Observation/Table/Figure/CoV standing")
    cover=ledger["C239_cumulative_coverage"]
    required(cover["registered_headings"]==192 and cover["at_least_source_sampled_or_inline_read"]==149
        and cover["substantively_unread"]==42 and cover["restricted"]==1,
        "partial corpus not invented as complete")
    required(ledger["source"]["native_ANSI_VITA_companions_read"] is False
        and ledger["source"]["C239_DSDM_IDL_OpenAPI_8_files_read"] is False
        and ledger["source"]["figure_pixels_audited"] is False,"source files and original image limits held")
    for n,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
       (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
       (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence")):
        required(sum(bool(x.get(key)) for x in rows)==n,"previous source donor evidence retained "+key)
    selected=[r for r in rows if r.get("G2_6A_source_correspondence")]
    required(len(selected)==39 and {r["row_id"] for r in selected}==set(doc["workbookSnapshot"]["G2_6A_affected_row_ids"]),
        "39 source-qualified actual existing SOSA comparison cells")
    older=[list(r) for r in grid]
    for r in selected:
        ev=r["G2_6A_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
            "original item provenance on "+r["row_id"])
        required(ev["DIM_Profile_adopted"] is False and ev["native_VITA_and_DSDM_companions_unreviewed"],
            "external original limits and DIM/Profile nonadoption "+r["row_id"])
        val=r["display"][8]
        required("G2-6A:" in val and val!=ev["previous_sosa_cell_value"],
            "source new comparison distinct from old SOSA cell")
        match=[i for i,g in enumerate(grid) if g[8]==val and g[14]==r["label"]]
        required(len(match)==1,"one stable master source row "+r["row_id"])
        older[match[0]][8]=ev["previous_sosa_cell_value"]
    synced=doc["workbookSnapshot"]["currently_matches_readable_view"] is True
    if synced:
        v=json.loads((BASE/"SOSA_G2_6A_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-6A-CANONICAL-VERIFIED"
            and doc["SOSAReviewCompletion"]["G2_6A_XLSX_lag"]==0
            and doc["SOSAEvidence"]["G2_6A"]["excel_lag_cells"]==0,"saved G2-6A zero workbook lag")
        required(v["G2_6A_qualified_existing_sosa_cells"]==39 and len(v["changed_saved_cells"])==39
            and all(re.fullmatch(r"I\d+",x) for x in v["changed_saved_cells"]),"39 only column I saved edits")
        required(all(v["checks"][k] for k in ("all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD",
            "two_CSV_mirrors_equal","two_GitHub_readable_comparisons_equal","same_26_worksheet_names_order",
            "22_historical_worksheet_XML_bytes_preserved","only_39_original_SOSA_I_column_cells_changed",
            "valid_ZIP_CRC_and_XML","zero_XLSX_error_type_cells","zero_DIM_Profile_adoption")),
            "actual saved 26-sheet workbook evidence records PASS")
    else:
        v=json.loads((BASE/"SOSA_G2_5_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
        required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-5-CANONICAL-VERIFIED__G2_6A_SOURCE_PENDING_XLSX"
            and doc["SOSAReviewCompletion"]["G2_6A_XLSX_lag"]==39,
            "precise 39-cell prior G2-5 saved workbook source lag")
    book=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(book).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
        "exact saved XLSX SHA matches its declared checkpoint")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved XLSX ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(path)).iter(S+"c")),
                    "no error-type Excel cells")
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        nodes=list(wb.find(S+"sheets"))
        names=[x.get("name") for x in nodes]
        required(names==v["workbook_sheets"] and len(names)==26,"same exact 26 source workbook sheet names and order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for x in nodes:
            target=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[x.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for name,h in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==h,"historical exact unchanged sheet "+name)
        master,actual=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(actual==(grid if synced else older),"every 346x15 actually saved Excel cell agrees with current source or precise 39-cell prior snapshot")
        merges=[x.get("ref") for x in master.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
            "all 15 divider rows and 3 header merges retained")
        pane=master.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
            "source case columns and first two header rows frozen")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
        and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True
        and doc["SOSAEvidence"]["G2_6A"]["DIM_Profile_adopted"] is False,
        "source incomplete, no next donor or model adoption")
    print("PASS: G2-6A 13 C239 TOC headings/19 nested, 98 original Rules, 8 Permissions, 3 Recommendations, 21 Observations, 39 source-qualified SOSA comparisons.")
    print("PASS: current source JSON, both CSVs and both Markdown grids; SAME 26-sheet saved workbook "+
        ("all current 346x15 cells exact." if synced else "39-column-I cells older at identified G2-5 source checkpoint."))
    print("LIMIT: 42 C239 headings unread, one restricted; original ANSI/VITA and 8 DSDM/IDL/OpenAPI files, figure pixels unverified; no DIM/Profile adoption or physical device test.")

def verify_sosa_g2_6b_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent current C239 G2-6B original source, both mirrors and SAME saved Excel readback."""
    import hashlib
    import html
    grid=doc["review_grid"]; rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(x)==15 for x in grid),
             "G2-6B original 329 rows and 346x15 source grid")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM", "original distinct donor/case/DIM order")
    required(mirror==grid, "first CSV equals all source grid cells")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror equals all source grid cells")
    second=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==second.split("<table>",1)[1],"both readable tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    parsed=[]
    for part in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in part:
            h=re.search(r'<th colspan="15">(.*?)</th>',part,re.S)
            required(h is not None,"15-column topic")
            parsed.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",part,re.S)]
            required(len(vals)==15,"all 15 original columns readable")
            parsed.append(vals)
    sections=set(doc["review_sections"])
    required(len(sections)==15 and parsed==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in sections]==[r["display"] for r in rows],
             "all 15 topic dividers and original stable row/cell geometry")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480 and doc["ISAEvidence"]["specificQuestions"]==6,
             "earlier donor/case/ISA facts and six precise questions")
    b=json.loads((BASE/"SOSA_G2_6B_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    ids={x["id"] for x in b["original_source_items"]}; counts=b["source_counts"]
    required(len(ids)==81 and len(b["original_toc_heading_coverage"])==1 and len(b["additional_native_subclauses_read"])==7
             and counts["original_native_records_excluding_analyst"]==73 and counts["ANALYTICAL_CONTEXT"]==8,
             "81 item-level source/analyst records and original section hierarchy")
    for k,n in (("RULE",7),("PERMISSION",2),("RECOMMENDATION",4),("OBSERVATION",9),
                ("TABLE",6),("FIGURE",9),("SLOT_PROFILE_DASH_ROW",27),("ANSI_VITA_RULE_TABLE_POINTER",9)):
        required(counts[k]==n, "source-native item kind count "+k)
    required(any(x["identifier_repeated_in_original"] for x in b["original_source_items"] if x["native_kind"]=="RULE")
             and counts["distinct_printed_rule_identifiers"]==6,
             "duplicate Rule13.2.11.5-3 must retain two separate native occurrences")
    cover=b["C239_cumulative_coverage"]
    required((cover["registered_headings"],cover["at_least_source_sampled_or_inline_read"],
              cover["substantively_unread"],cover["restricted"])==(192,150,41,1),
             "accurate partial original corpus accounting")
    required(b["DIM_Profile_adopted"] is False and b["real_device_or_conformance_test"] is False,
             "no premature source-completeness/model/runtime claim")
    for n,k in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
      (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
      (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
      (39,"G2_6A_source_correspondence")):
        required(sum(bool(r.get(k)) for r in rows)==n,"preserve original source packet "+k)
    updated=[r for r in rows if r.get("G2_6B_source_correspondence")]
    required(len(updated)==26 and {r["row_id"] for r in updated}==set(doc["workbookSnapshot"]["G2_6B_affected_row_ids"]),
             "exact G2-6B 26 qualified existing source rows")
    current_ids=set();prior=[list(x) for x in grid]
    for row in updated:
        e=row["G2_6B_source_correspondence"];val=row["display"][8]
        required(all(x in ids for x in e["source_item_ids"]) and bool(e["source_item_ids"]),
                 "original printed source IDs "+row["row_id"])
        required(e["DIM_Profile_adopted"] is False
                 and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
                 "source/edition holdings and no adoption")
        required("G2-6B:" in val and val!=e["previous_sosa_cell_value"],
                 "one source-justified new contribution")
        idx=[i for i,g in enumerate(grid) if g[8]==val and g[14]==row["label"]]
        required(len(idx)==1,"unique stable row correspondence "+row["row_id"])
        cell="I"+str(idx[0]+1);required(cell not in current_ids,"one changed cell only")
        current_ids.add(cell);prior[idx[0]][8]=e["previous_sosa_cell_value"]
        required(all(row["display"][n]==prior[idx[0]][n] for n in range(15) if n!=8),
                 "other donor and source case cells untouched")
    v=json.loads((BASE/"SOSA_G2_6B_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(set(v["changed_saved_cells"])==current_ids and len(current_ids)==26,
             "published saved difference agrees with exactly 26 qualified SOSA source IDs")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-6B-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_6B_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_6B"]["Excel_lag_cells"]==0,
             "mandatory same-workbook L23 exit complete")
    required(all(v["checks"].values()),"publisher saved-cell, historical sheet and nonadoption checks")
    book=(BASE/(NAME+".xlsx")).read_bytes()
    h=hashlib.sha256(book).hexdigest()
    required(h==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "saved actual Excel bytes and metadata SHA equal")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"XLSX CRC")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                required(not any(c.get("t")=="e" for c in ET.fromstring(z.read(p)).iter(S+"c")),
                         "no Excel error type cells")
        root=ET.fromstring(z.read("xl/workbook.xml"))
        nodes=list(root.find(S+"sheets"));names=[x.get("name") for x in nodes]
        required(names==v["workbook_sheets"] and len(names)==26,"all 26 worksheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        locations={}
        for x in nodes:
            t=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            locations[x.get("name")]=t.lstrip("/") if t.startswith("/") else "xl/"+t
        for name,digest in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(locations[name])).hexdigest()==digest,"unchanged historical "+name)
        sheet,actual=data_rows(z.read(locations["Master Crosswalk"]),15)
        required(actual==grid,"every one of the 5190 saved grid cells matches original source current")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "all original full-width groups")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","frozen case and two header rows")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "entire donor OPEN, no transition")
    print("PASS: G2-6B source 1 heading/7 child sections, 73 native records/8 contexts, 26 qualified SOSA cells.")
    print("PASS: SAME original 26-sheet XLSX exact 346x15 current JSON/both CSV/both Markdown saved-cell parity; 22 historical sheets.")
    print("LIMIT: 41 C239 headings unread/1 restricted; ANSI/VITA and 8 native DSDM/API files held; zero model adoption/command/conformance.")


def verify_sosa_g2_6c_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent SOSA-G2-6C 6U original-source, canonical mirrors, saved 26-sheet Excel validation."""
    import hashlib
    import html
    grid=doc["review_grid"]; rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(v)==15 for v in grid),
             "exact source dimensions and original 329 stable rows")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM","original case/donor/OGC foundation/DIM order")
    required(mirror==grid,"first CSV matches canonical JSON")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second CSV all 346x15 saved source cells")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==twin.split("<table>",1)[1],"both Markdown comparison tables identical")
    textbody=md.split("<tbody>",1)[1].split("</tbody>",1)[0];parsed=[]
    for element in re.findall(r"<tr>.*?</tr>",textbody,re.S):
        if 'colspan="15"' in element:
            header=re.search(r'<th colspan="15">(.*?)</th>',element,re.S)
            required(header is not None,"original topic divider")
            parsed.append([html.unescape(header.group(1))]+[""]*14)
        else:
            val=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",element,re.S)]
            required(len(val)==15,"full case/donor/DIM row")
            parsed.append(val)
    section=set(doc["review_sections"])
    required(len(section)==15 and parsed==grid[2:]
             and [x for i,x in enumerate(grid) if i>1 and i not in section]==[r["display"] for r in rows],
             "complete 15-divider Markdown JSON and stable 329 row ordering")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "preserved 58 donor,73 source-case,480 ISA and six unresolved interpretations")
    ledger=json.loads((BASE/"SOSA_G2_6C_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    ids={x["id"] for x in ledger["original_source_items"]}; count=ledger["source_counts"]
    required(len(ids)==51 and len(ledger["original_toc_heading_coverage"])==1
             and len(ledger["additional_native_subclauses_read"])==4
             and count["actual_native_records_excluding_analytical_context"]==43
             and count["ANALYTICAL_CONTEXT"]==8,"one TOC, four nested, 43 native/8 analytical source records")
    for kind,n in [("RULE",4),("RECOMMENDATION",2),("OBSERVATION",5),("TABLE",4),
                   ("FIGURE",5),("SLOT_PROFILE_DASH_ROW",18),("RULE_LIST_PROFILE_OPTION",5)]:
        required(count[kind]==n,"source-native exact item inventory "+kind)
    cover=ledger["C239_cumulative_coverage"]
    required((cover["registered_headings"],cover["at_least_source_sampled_or_inline_read"],
              cover["substantively_unread"],cover["restricted"])==(192,151,40,1),
             "honest 151 sampled/inline, 40 unread, one restricted source assessment")
    required(ledger["source"]["original_ANSI_VITA_companions_read"] is False
             and ledger["source"]["original_C239_DSDM_IDL_OpenAPI_8_files_read"] is False
             and ledger["source"]["full_figure_pixel_geometry_verified"] is False
             and not ledger["DIM_Profile_adopted"]
             and not ledger["independent_conformance_or_physical_device_operation_performed"],
             "external source, figure, runtime and DIM/Profile adoption holds")
    for number,key in [(12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
             (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
             (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
             (39,"G2_6A_source_correspondence"),(26,"G2_6B_source_correspondence")]:
        required(sum(bool(x.get(key)) for x in rows)==number,"previous source decisions retained "+key)
    updated=[x for x in rows if x.get("G2_6C_source_correspondence")]
    required(len(updated)==24 and {r["row_id"] for r in updated}==set(doc["workbookSnapshot"]["G2_6C_affected_row_ids"]),
             "exact 24 source-qualified G2-6C existing rows")
    actual_cells=set()
    for x in updated:
        e=x["G2_6C_source_correspondence"]
        required(e["source_item_ids"] and all(v in ids for v in e["source_item_ids"]),
                 "source-original locator support "+x["row_id"])
        required(e["DIM_Profile_adopted"] is False and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
                 "exact original source holds and zero model adoption "+x["row_id"])
        required("G2-6C:" in x["display"][8] and e["previous_sosa_cell_value"]!=x["display"][8],
                 "source-qualified new SOSA cell, previous value preserved "+x["row_id"])
        idx=[i for i,g in enumerate(grid) if g[8]==x["display"][8] and g[14]==x["label"]]
        required(len(idx)==1,"stable original source row ID "+x["row_id"])
        actual_cells.add("I"+str(idx[0]+1))
    v=json.loads((BASE/"SOSA_G2_6C_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_6C_qualified_existing_sosa_cells"]==24
             and len(v["changed_saved_cells"])==24 and set(v["changed_saved_cells"])==actual_cells,
             "saved publication delta matches 24 source-qualified column-I cells")
    required(all(v["checks"].values()),"publisher workbook and evidence invariant PASS")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-6C-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_6C_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_6C"]["Excel_lag_cells"]==0,
             "binding L23 source-to-same-saved-workbook completion")
    binary=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(binary).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved workbook bytes match both metadata SHA fields and independent record")
    with zipfile.ZipFile(io.BytesIO(binary)) as z:
        required(z.testzip() is None,"ZIP CRC")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(p)).iter(S+"c")),
                         "no Excel formula/value error type cells")
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        sheets=list(wb.find(S+"sheets"));names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==v["workbook_sheets"],"all 26 original worksheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        pathmap={}
        for sh in sheets:
            p=rels[sh.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            pathmap[sh.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        for n,h in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(pathmap[n])).hexdigest()==h,"unchanged historical worksheet XML "+n)
        xml,cellrows=data_rows(z.read(pathmap["Master Crosswalk"]),15)
        required(cellrows==grid,"ALL 346x15 actual saved XLSX cells match current source grid")
        merges=[x.get("ref") for x in xml.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "original merged headings and 15 topic dividers")
        pane=xml.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","original frozen source case and header layout")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA still open and next donor not authorized")
    print("PASS: G2-6C one original TOC, four child sections, 43 native source records/8 analysis, 24 source-qualified cells.")
    print("PASS: SAME canonical 26-sheet workbook, all saved 346x15 JSON/both CSV/both readable Markdown cells, 22 untouched historical tabs.")
    print("LIMIT: 40 C239 headings unread/1 restricted; external ANSI/VITA and 8 native source files held; no DIM/Profile adoption or device conformance.")


def verify_sosa_g2_6d_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent G2-6D source-item census, semantically qualified cells and saved 26-sheet readback."""
    import hashlib
    import html
    rows=doc["rows"];grid=doc["review_grid"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(r)==15 for r in grid),
             "original 329 source rows, 346x15 display grid")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM","original source/donor/foundation/DIM geometry")
    required(mirror==grid,"first CSV all source grid cells")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second CSV all source cells")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==other.split("<table>",1)[1],"both GitHub-readable comparisons identical")
    contents=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for f in re.findall(r"<tr>.*?</tr>",contents,re.S):
        if 'colspan="15"' in f:
            head=re.search(r'<th colspan="15">(.*?)</th>',f,re.S)
            required(head is not None,"grouped full-width source rows retained")
            readable.append([html.unescape(head.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",f,re.S)]
            required(len(vals)==15,"readable case/donor/DIM row exactly 15 cells")
            readable.append(vals)
    dividers=set(doc["review_sections"])
    required(len(dividers)==15 and readable==grid[2:]
             and [x for i,x in enumerate(grid) if i>1 and i not in dividers]==[r["display"] for r in rows],
             "all human-readable and source cells agree, original stable row order preserved")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "historical donor, source-case, ISA decisions and unresolved questions preserved")
    ledger=json.loads((BASE/"SOSA_G2_6D_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    source=ledger["source"];counts=ledger["source_counts"];data=ledger["original_source_items"]
    ids={x["id"] for x in data}
    required(len(data)==26 and len(ids)==26 and len(ledger["original_toc_heading_coverage"])==1
             and len(ledger["additional_native_subclauses_read"])==3 and len(ledger["exact_holds"])==14,
             "1 original heading, 3 children, 26 distinct item/context records and 14 exact holds")
    for key,n in (("RULE",4),("RECOMMENDATION",2),("PROCESS_STATEMENT",4),("FIGURE",2),
                  ("RULE_LIST_MODULE_OPTION",7),("DASH_OPTION",1),("ANALYTICAL_CONTEXT",6),
                  ("conditional_narrative_shall_provisions",2),
                  ("original_source_native_items_excluding_analytical_context",20)):
        required(counts[key]==n,"original source-item kind/standing "+key)
    rule_ids={v["id"] for v in data if v["native_kind"]=="RULE"}
    required(rule_ids=={"SOSA-C239-G2-6D-RULE-13.2.13.1-1","SOSA-C239-G2-6D-RULE-13.2.13.1-2",
                        "SOSA-C239-G2-6D-RULE-13.2.13.2-2","SOSA-C239-G2-6D-RULE-13.2.13.2-3"},
             "no invented 6U Rule13.2.13.2-1; four printed native Rules")
    dash=next(v for v in data if v["native_kind"]=="DASH_OPTION")
    required(dash["marked_legacy_dash"]=="-1" and dash["other_dash_options_legacy"] is False,
             "3U radial-clock SMPM-10 -1 only Legacy; no blanket status")
    narrative=[v for v in data if v["native_kind"]=="PROCESS_STATEMENT"
               and v["normative_standing"]=="SOURCE_NARRATIVE_CONDITIONAL_SHALL_NOT_NUMBERED_RULE"]
    required(len(narrative)==2 and any("18-month" in v["native_name"] for v in narrative),
             "conditional after-removal 18-month certification provisions not phantom numbered Rules")
    coverage=ledger["C239_cumulative_coverage"]
    required((coverage["registered_headings"],coverage["at_least_source_sampled_or_inline_read"],
              coverage["substantively_unread"],coverage["restricted"])==(192,152,39,1),
             "C239 original coverage 152 sampled/inline,39 unread,1 restricted")
    required(source["ANSI_VITA_65_0_65_1_origins_read"] is False
             and source["C239_DSDM_IDL_OpenAPI_eight_native_files_read"] is False
             and source["original_figure_pixels_verified"] is False,
             "native source and original figure geometry holds explicitly retained")
    required(ledger["DIM_Profile_adopted"] is False
             and ledger["actual_runtime_conformance_or_physical_device_operation_performed"] is False,
             "source analysis not DIM/Profile or device conformance adoption")
    for n,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
                  (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
                  (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
                  (39,"G2_6A_source_correspondence"),(26,"G2_6B_source_correspondence"),
                  (24,"G2_6C_source_correspondence")):
        required(sum(bool(v.get(key)) for v in rows)==n,"earlier source mapping preserved "+key)
    changed=[r for r in rows if r.get("G2_6D_source_correspondence")]
    required(len(changed)==14
             and {r["row_id"] for r in changed}==set(doc["workbookSnapshot"]["G2_6D_affected_row_ids"]),
             "exactly 14 original-source qualified existing-row contributions")
    updated_addr=set()
    for row in changed:
        e=row["G2_6D_source_correspondence"]
        required(e["source_item_ids"] and all(i in ids for i in e["source_item_ids"]),
                 "original item-level source IDs for "+row["row_id"])
        required(e["DIM_Profile_adopted"] is False
                 and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
                 "no made-up new Profile/companion rule for "+row["row_id"])
        v=row["display"][8]
        required("G2-6D:" in v and v!=e["previous_sosa_cell_value"],
                 "distinct source-qualified incremental SOSA cell")
        positions=[i for i,r in enumerate(grid) if r[8]==v and r[14]==row["label"]]
        required(len(positions)==1,"stable original source row "+row["row_id"])
        updated_addr.add("I"+str(positions[0]+1))
    v=json.loads((BASE/"SOSA_G2_6D_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_6D_qualified_existing_sosa_cells"]==14
             and set(v["changed_saved_cells"])==updated_addr and len(updated_addr)==14,
             "publisher 14 changed saved column-I cells correspond to 14 original source ID records")
    required(all(v["checks"].values()),"saved publisher workbook source/evidence invariants PASS")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-6D-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_6D_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_6D"]["Excel_lag_cells"]==0,
             "same-workbook L23 exit complete; zero lag")
    b=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(b).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved binary workbook hash equals metadata and check record")
    with zipfile.ZipFile(io.BytesIO(b)) as archive:
        required(archive.testzip() is None,"Excel ZIP CRC")
        for p in archive.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(archive.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                required(not any(c.get("t")=="e" for c in ET.fromstring(archive.read(p)).iter(S+"c")),
                         "Excel error-valued cell absent")
        book=ET.fromstring(archive.read("xl/workbook.xml"))
        sheets=list(book.find(S+"sheets"))
        names=[x.get("name") for x in sheets]
        required(names==v["workbook_sheets"] and len(names)==26,"same original 26 sheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))}
        sheetpaths={}
        for node in sheets:
            dest=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            sheetpaths[node.get("name")]=dest.lstrip("/") if dest.startswith("/") else "xl/"+dest
        for name,hashv in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(archive.read(sheetpaths[name])).hexdigest()==hashv,
                     "historical original sheet XML unchanged "+name)
        sh,actual=data_rows(archive.read(sheetpaths["Master Crosswalk"]),15)
        required(actual==grid,"all 346x15 actual saved Excel cells match canonical source")
        merge=[n.get("ref") for n in sh.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merge==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "original layout and 15 dividers")
        pane=sh.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","frozen four source cases and header rows")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "no premature SOSA donor closure or next donor")
    print("PASS: G2-6D original source 20 native records, 4 numbered Rules, 2 Recommendations, 2 conditional narrative SHALLs, 14 qualified comparisons.")
    print("PASS: SAME original 26-sheet XLSX saved 346x15 grid equals JSON, two CSV and two readable Markdown tables; 22 historical sheets preserved.")
    print("LIMIT: 39 C239 headings unread, 1 restricted; native original ANSI/VITA/8 DSDM/IDL/API files held; no DIM/Profile adoption/device operation.")


def verify_sosa_g2_7a_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent current G2-7A AMPS original C239 ledger, mirror, saved canonical Excel verification."""
    import hashlib
    import html
    rows=doc["rows"];grid=doc["review_grid"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(v)==15 for v in grid),
             "original 329 rows and 346x15 grid retained")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM", "four cases left, Open Group separate from W3C and DIM right")
    required(mirror==grid,"canonical CSV all source cells")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror all current cells")
    second=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required(md.split("<table>",1)[1]==second.split("<table>",1)[1],"both GitHub-readable comparison bodies match")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    parsed=[]
    for fragment in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in fragment:
            h=re.search(r'<th colspan="15">(.*?)</th>',fragment,re.S)
            required(h is not None,"full-width section heading")
            parsed.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",fragment,re.S)]
            required(len(vals)==15,"full 15-column GitHub-readable source row")
            parsed.append(vals)
    sec=set(doc["review_sections"])
    required(len(sec)==15 and parsed==grid[2:]
             and [x for i,x in enumerate(grid) if i>1 and i not in sec]==[r["display"] for r in rows],
             "329 original rows/15 section dividers and full readable/source parity")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "58 donor,73 original source cases,480 ISA primary and six questions preserved")
    ledger=json.loads((BASE/"SOSA_G2_7A_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    count=ledger["source_counts"];items=ledger["original_source_items"]
    ids={x["id"] for x in items}
    required(len(items)==77 and len(ids)==77 and len(ledger["original_toc_heading_coverage"])==3
             and len(ledger["exact_holds"])==16 and count["source_native_items_excluding_analytical_context"]==70
             and count["ANALYTICAL_CONTEXT"]==7,"original AMPS 3 headings, 70 native source items, 7 analyst contexts, 16 holds")
    for k,n in (("DEFINITION",5),("SOURCE_CONTEXT",11),("TABLE",2),
                ("EXAMPLE_ROW",2),("PROTOCOL_CODE",50),("numbered_C239_rule_shalls",0),
                ("numbered_C239_recommendations",0)):
        required(count[k]==n,"G2-7A source standing and item inventory "+k)
    groups=ledger["protocol_groups"]
    required(len(groups)==7 and sum(x["source_row_count"] for x in groups)==50,
             "seven original Table13.3.2-2 protocol groups and exactly 50 native rows")
    n_codes=[x for x in items if x["native_kind"]=="PROTOCOL_CODE" and x["source_protocol_code"]=="N"]
    required(len(n_codes)==4 and len({x["protocol_group"] for x in n_codes})==4,
             "repeated N codes kept group-qualified")
    coverage=ledger["C239_cumulative_coverage"]
    required((coverage["registered_headings"],coverage["at_least_source_sampled_or_inline_read"],
              coverage["substantively_unread"],coverage["restricted"])==(192,155,36,1),
             "C239 original coverage is partial: 155 sampled/inline, 36 unread, 1 restricted")
    required(ledger["source"]["normative_ANSI_VITA_65_0_and_65_1_originals_read"] is False
             and ledger["source"]["original_C239_DSDM_IDL_six_OpenAPI_files_read"] is False
             and ledger["source"]["full_pdf_figure_and_high_resolution_table_geometry_verified"] is False
             and ledger["DIM_Profile_adopted"] is False
             and ledger["runtime_or_independent_conformance_performed"] is False,
             "explicit unreviewed normative originals, no physical runtime or model adoption")
    for n,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
                  (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
                  (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
                  (39,"G2_6A_source_correspondence"),(26,"G2_6B_source_correspondence"),
                  (24,"G2_6C_source_correspondence"),(14,"G2_6D_source_correspondence")):
        required(sum(bool(r.get(key)) for r in rows)==n,"original prior source interpretations preserved "+key)
    qualified=[r for r in rows if r.get("G2_7A_source_correspondence")]
    required(len(qualified)==20 and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7A_affected_row_ids"]),
             "exactly 20 earned new SOSA source comparisons")
    touched=set()
    for row in qualified:
        e=row["G2_7A_source_correspondence"]
        required(e["source_item_ids"] and all(x in ids for x in e["source_item_ids"]),
                 "original source-item lineage "+row["row_id"])
        required(e["DIM_Profile_adopted"] is False and e["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and e["full_AMPS_13_3_3_per_port_and_protocol_rules_unread"],
                 "local source limits and no model adoption "+row["row_id"])
        current=row["display"][8]
        required("G2-7A:" in current and current!=e["previous_sosa_cell_value"],
                 "new source finding retains exact previous SOSA cell")
        idx=[i for i,x in enumerate(grid) if x[8]==current and x[14]==row["label"]]
        required(len(idx)==1,"one original stable source row "+row["row_id"])
        touched.add("I"+str(idx[0]+1))
    v=json.loads((BASE/"SOSA_G2_7A_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_7A_qualified_existing_sosa_cells"]==20
             and len(touched)==20 and set(v["changed_saved_cells"])==touched,
             "original-source-qualified 20 cell IDs agree with actual saved workbook changes")
    required(all(v["checks"].values()),"publisher every saved workbook/ledger check PASS")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7A-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7A_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7A"]["Excel_lag_cells"]==0,
             "L23 same canonical Excel saved and verified with zero lag")
    binary=(BASE/(NAME+".xlsx")).read_bytes()
    sha=hashlib.sha256(binary).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved Excel binary SHA equals master and validation metadata")
    with zipfile.ZipFile(io.BytesIO(binary)) as z:
        required(z.testzip() is None,"saved XLSX CRC valid")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no Excel error-typed cells")
        work=ET.fromstring(z.read("xl/workbook.xml"))
        sheets=list(work.find(S+"sheets"));names=[x.get("name") for x in sheets]
        required(len(sheets)==26 and names==v["workbook_sheets"],"original 26 worksheet names/order exactly preserved")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in sheets:
            target=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        for name,digest in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==digest,
                     "historical worksheet byte-equivalent: "+name)
        xml,actual=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(actual==grid,"all 346x15 actual saved worksheet cells equal current source grid")
        merges=[x.get("ref") for x in xml.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "full-width topic dividers and original source/donor headers")
        pane=xml.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original four source cases and two title rows frozen")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "AMPS donor remains source-incomplete, next donor blocked")
    print("PASS: SOSA-G2-7A original AMPS §§13.3.1–.2, 5 definitions, 50 native protocol codes, 20 qualified cells.")
    print("PASS: SAME original 26-sheet XLSX with 346x15 saved cells equal JSON, BOTH CSV and BOTH Markdown; 22 historical worksheets preserved.")
    print("LIMIT: 36 C239 original headings unread, one restricted, native VITA+8 models/API original files held; no DIM/Profile or runtime conformance.")


def verify_sosa_g2_7b_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent C239 G2-7B §13.3.3 source, both mirrors, SAME saved 26-sheet Excel."""
    import hashlib
    import html
    grid=doc["review_grid"]; rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(r)==15 for r in grid),
             "329 stable rows, original 346x15 presentation")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM","four case columns left, OGC distinct, proposed DIM far-right")
    required(grid[1]==[x["name"] for x in doc["columns"]] and mirror==grid,
             "approved source header and canonical CSV all current cells")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror full canonical source equality")
    second=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==second.split("<table>",1)[1],
             "two GitHub-readable comparison tables identical")
    content=md.split("<tbody>",1)[1].split("</tbody>",1)[0];readable=[]
    for frag in re.findall(r"<tr>.*?</tr>",content,re.S):
        if 'colspan="15"' in frag:
            head=re.search(r'<th colspan="15">(.*?)</th>',frag,re.S)
            required(head is not None,"source topic divider")
            readable.append([html.unescape(head.group(1))]+[""]*14)
        else:
            values=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",frag,re.S)]
            required(len(values)==15,"all readable source-case/donor/DIM cells exist")
            readable.append(values)
    sec=set(doc["review_sections"])
    required(len(sec)==15 and readable==grid[2:]
             and [x for i,x in enumerate(grid) if i>1 and i not in sec]==[r["display"] for r in rows],
             "all 15 topic dividers and 329 original row-source values identical")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "all previous 58 donor, 73 source-case, 480 ISA outcomes and 6 questions preserved")
    ledger=json.loads((BASE/"SOSA_G2_7B_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    items=ledger["original_source_items"]; ids={x["id"] for x in items}; cc=ledger["source_counts"]
    required(len(items)==len(ids)==67 and len(ledger["original_toc_heading_coverage"])==1
             and len(ledger["exact_holds"])==17
             and cc["source_native_records_excluding_analytical_context"]==59
             and cc["ANALYTICAL_CONTEXT"]==8,"one C239 §13.3.3, 59 original native items, 8 analyst contexts, 17 holds")
    for key,n in (("SOURCE_CONTEXT",3),("FIGURE",1),("TABLE",6),("PARAMETER",12),
                  ("EXAMPLE",18),("DCP_OPTION",15),("DCP_SUPPORTED",4),
                  ("source_numbered_rule_shalls",0),("source_numbered_recommendations",0)):
        required(cc[key]==n,"native original source-item kind "+key)
    examples=[x for x in items if x["native_kind"]=="EXAMPLE" and x.get("printed_protocol_field")=="4P3U"]
    required(len(examples)==2 and {x["port_context"] for x in examples}==
             {"ANS_FOUR_FAT_PIPES","ANS_EIGHT_LANES"},"4P3U preserved as two different ANS contexts")
    supported={x["supported_code"] for x in items if x["native_kind"]=="DCP_SUPPORTED"}
    required(supported=={"F2C","F4C","F8H","S2E"},"only 4 original supported depth/cooling/pitch combinations")
    required(any("A4F" in x["meaning"] for x in ledger["source_discrepancies"]),
             "original A4F code discrepancy recorded and not invented as verified")
    cov=ledger["C239_cumulative_coverage"]
    required((cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,156,35,1),
             "156 original C239 headings at least source reviewed, 35 unread, 1 restricted")
    source=ledger["source"]
    required(source["native_original_ANSI_VITA_65_0_read"] is False
             and source["other_native_ANSI_VITA_48_cooling_read"] is False
             and source["C239_eight_DSDM_IDL_OpenAPI_native_files_read"] is False
             and source["source_figure_pixels_verified"] is False
             and ledger["DIM_Profile_adopted"] is False
             and ledger["actual_runtime_or_independent_conformance_performed"] is False,
             "original normative, visual, model and runtime limitations not lost")
    for n,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
                  (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
                  (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
                  (39,"G2_6A_source_correspondence"),(26,"G2_6B_source_correspondence"),
                  (24,"G2_6C_source_correspondence"),(14,"G2_6D_source_correspondence"),
                  (20,"G2_7A_source_correspondence")):
        required(sum(bool(r.get(key)) for r in rows)==n,"all previous original SOSA contributions "+key)
    changed=[r for r in rows if r.get("G2_7B_source_correspondence")]
    required(len(changed)==24 and {r["row_id"] for r in changed}==set(doc["workbookSnapshot"]["G2_7B_affected_row_ids"]),
             "24 new source-qualified existing-row correspondences")
    touched=set()
    for r in changed:
        ev=r["G2_7B_source_correspondence"]
        required(ev["source_item_ids"] and all(i in ids for i in ev["source_item_ids"]),
                 "actual native source IDs "+r["row_id"])
        required(ev["DIM_Profile_adopted"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["full_AMPS_diagram_pixel_geometry_unverified"],
                 "qualified nonadoption and visual/original source limits "+r["row_id"])
        val=r["display"][8]
        required("G2-7B:" in val and val!=ev["previous_sosa_cell_value"],
                 "source-qualified changed SOSA cell preserves prior provenance")
        ix=[i for i,v in enumerate(grid) if v[8]==val and v[14]==r["label"]]
        required(len(ix)==1,"original stable row ID uniquely locates saved Excel comparison "+r["row_id"])
        touched.add("I"+str(ix[0]+1))
    v=json.loads((BASE/"SOSA_G2_7B_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_7B_qualified_existing_sosa_cells"]==24
             and len(v["changed_saved_cells"])==24 and set(v["changed_saved_cells"])==touched,
             "publisher saved 24 column-I cell delta equals source-qualified row provenance")
    required(all(v["checks"].values()),"publisher exact saved-cell/source checks PASS")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7B-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7B_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7B"]["Excel_lag_cells"]==0,
             "binding L23 same editable workbook verified; zero lag")
    actual_binary=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(actual_binary).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved Excel bytes equal original-source meta and validation SHA")
    with zipfile.ZipFile(io.BytesIO(actual_binary)) as z:
        required(z.testzip() is None,"saved workbook ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no saved Excel error-typed cells")
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        nodes=list(wb.find(S+"sheets"));names=[x.get("name") for x in nodes]
        required(len(names)==26 and names==v["workbook_sheets"],"original 26 saved worksheet names/order unchanged")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in nodes:
            dest=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=dest.lstrip("/") if dest.startswith("/") else "xl/"+dest
        for name,digest in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==digest,
                     "untouched historical worksheet original XML preserved "+name)
        sheet,values=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(values==grid,"every one of 346x15 actual saved Excel source cells matches canonical master")
        merge=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merge==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "all originally approved header and section merges")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original source cases and header row frozen")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "original source completeness and next donor kept blocked")
    print("PASS: G2-7B original §13.3.3: six source tables, 59 native items/8 contexts, 24 qualified existing SOSA cells.")
    print("PASS: SAME saved 26-sheet Excel, all 346x15 actual cells match canonical JSON and both CSV/Markdown mirrors; 22 historical sheets unchanged.")
    print("LIMIT: 35 C239 headings unread, 1 restricted, external ANSI/VITA and 8 C239 DSDM/API files unexamined; zero model or runtime adoption.")


def verify_sosa_g2_7c_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent C239 §13.3.4 text/partial dense-matrix source ledger and SAME saved 26-tab Excel readback."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(x)==15 for x in grid),
             "original 329 information rows and full 346x15 approved grid")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM","approved four source cases, distinct SOSA columns and far-right DIM")
    required(mirror==grid,"first CSV exact canonical JSON grid")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second original historical ISA CSV mirror exact current grid")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==twin.split("<table>",1)[1],
             "BOTH human-readable donor comparisons equal")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0];readable=[]
    for part in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in part:
            h=re.search(r'<th colspan="15">(.*?)</th>',part,re.S)
            required(h is not None,"original full-width topic divider")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",part,re.S)]
            required(len(vals)==15,"readable row has all 15 original columns")
            readable.append(vals)
    secs=set(doc["review_sections"])
    required(len(secs)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in secs]==[r["display"] for r in rows],
             "every case/donor/DIM source cell and all 15 original dividers agree")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "original 58 donor,73 case facts and ISA480/six questions intact")
    ledger=json.loads((BASE/"SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    cc=ledger["source_counts"];items=ledger["original_source_items"];ids={x["id"] for x in items}
    required(len(items)==len(ids)==77 and len(ledger["original_toc_heading_coverage"])==1
             and len(ledger["exact_holds"])==19
             and cc["native_source_records_excluding_analysis"]==68
             and cc["ANALYTICAL_CONTEXT"]==9,
             "G2-7C one registered heading, 68 native+9 analytical source records, 19 exact holds")
    for k,n in (("SOURCE_CONTEXT",6),("TABLE",3),("PROFILE_FAMILY",10),
                ("DASH_OPTION",39),("FULL_STRING_EXAMPLE",10),
                ("table_13_3_4_1_named_dash_options",23),
                ("table_13_3_4_2_named_dash_options",16),
                ("original_numbered_RULE_SHALLs",0)):
        required(cc[k]==n,"original C239 inventory count "+k)
    f=[x for x in items if x["native_kind"]=="PROFILE_FAMILY"]
    required(sum(x["form_factor"]=="3U" for x in f)==6
             and sum(x["form_factor"]=="6U" for x in f)==4,
             "preserve exactly 6 native 3U and 4 native 6U physical family roles")
    d=[x for x in items if x["native_kind"]=="DASH_OPTION"]
    required(sum(x["printed_legacy_asterisk"] for x in d)==5,
             "five original specifically asterisked hardware dash options, not entire family")
    ex=[x for x in items if x["native_kind"]=="FULL_STRING_EXAMPLE"]
    sample=next(x for x in ex if x["stable_source_item_id"]=="6U-EXTERNAL_IO")
    required(sample["source_grammar_string"].startswith("MODA3p-12.2.8"),
             "6U External I/O original MODA3p anomaly preserved, not silently repaired")
    cov=ledger["C239_cumulative_coverage"]
    required((cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,157,34,1),
             "C239 original heading progress 157 sampled/inline,34 unread,1 restricted")
    sr=ledger["source"]
    required(sr["source_table_high_resolution_geometry_verified"] is False
             and cov["full_high_resolution_table_matrix_audit_complete"] is False
             and sr["original_ANSI_VITA65_0_65_1_examined"] is False
             and sr["original_VITA66_67_examined"] is False
             and sr["C239_eight_DSDM_IDL_OpenAPI_original_companions_examined"] is False,
             "dense legal matrix exact cell coordinates and original native companions explicitly HELD")
    required(ledger["DIM_Profile_adopted"] is False
             and ledger["runtime_or_independent_conformance_performed"] is False,
             "no unapproved DIM/Profile model, physical or runtime claim")
    for n,key in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
                  (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
                  (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence"),
                  (39,"G2_6A_source_correspondence"),(26,"G2_6B_source_correspondence"),
                  (24,"G2_6C_source_correspondence"),(14,"G2_6D_source_correspondence"),
                  (20,"G2_7A_source_correspondence"),(24,"G2_7B_source_correspondence")):
        required(sum(bool(x.get(key)) for x in rows)==n,"preserve earlier native source mappings "+key)
    qualified=[r for r in rows if r.get("G2_7C_source_correspondence")]
    required(len(qualified)==22
             and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7C_affected_row_ids"]),
             "exact original 22 justified SOSA source row IDs")
    changed=set()
    for r in qualified:
        ev=r["G2_7C_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
                 "source-item provenance intact on "+r["row_id"])
        required(ev["DIM_Profile_adopted"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["dense_matrix_exact_cell_alignment_unverified"],
                 "no fabricated complete dense-matrix/ANSI or DIM adoption "+r["row_id"])
        current=r["display"][8]
        required("G2-7C:" in current and current!=ev["previous_sosa_cell_value"],
                 "prior SOSA cell retained with source-qualified increment")
        hits=[i for i,v in enumerate(grid) if v[8]==current and v[14]==r["label"]]
        required(len(hits)==1,"unique original row ID and saved cell "+r["row_id"])
        changed.add("I"+str(hits[0]+1))
    v=json.loads((BASE/"SOSA_G2_7C_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_7C_qualified_existing_sosa_cells"]==22
             and len(changed)==22 and set(v["changed_saved_cells"])==changed,
             "verified saved 22 new source-qualified SOSA cell addresses")
    required(all(v["checks"].values()) and v["G2_7C_dense_matrix_visual_complete"] is False,
             "publisher saved parity PASS and visual qualification PARTIAL")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7C-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7C_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7C"]["Excel_lag_cells"]==0
             and doc["SOSAEvidence"]["G2_7C"]["exact_dense_multi_column_matrix_audit_complete"] is False,
             "binding L23 same saved workbook with zero lag and exact visual hold")
    book=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(book).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved original canonical workbook checksum and source/check metadata")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved Excel ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(c.get("t")=="e" for c in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no error-valued Excel cells in any historical worksheet")
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        nodes=list(wb.find(S+"sheets"));names=[x.get("name") for x in nodes]
        required(len(names)==26 and names==v["workbook_sheets"],
                 "same original 26 worksheet names and order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in nodes:
            path=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=path.lstrip("/") if path.startswith("/") else "xl/"+path
        for name,h in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==h,
                     "historical worksheet original XML bytes preserved: "+name)
        sheet,saved=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(saved==grid,"all 346x15 actual saved Excel cells match canonical source and both mirrors")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "case/donor/foundation original merged groups and 15 topic headings")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original four source-case columns and header freeze")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA source coverage incomplete and SAPIENT transition blocked")
    print("PASS: G2-7C original §13.3.4: 10 source families, 39 named dash variants, 10 full strings, 22 source-qualified SOSA comparisons.")
    print("PASS: SAME saved 26-sheet Excel, every 346x15 saved cell equals JSON/both CSV/both Markdown, 22 historical sheets unchanged.")
    print("LIMIT: exact dense matrix pixel cell alignments remain unverified, 34 C239 headings unread, one restricted, VITA/8 native model/API files held; zero DIM or runtime adoption.")



def verify_sosa_g2_7d_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent original C239 §13.3.5 source, mirror, and SAME saved canonical workbook checks."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(x)==15 for x in grid),
             "G2-7D original 329 rows and 346x15 canonical master")
    required([x["key"] for x in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM",
             "four original cases left, separate SOSA donors and proposed DIM far right")
    required(mirror==grid,"canonical JSON and first CSV parity")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second historical CSV exact parity")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==twin.split("<table>",1)[1],
             "BOTH GitHub-readable comparison tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0];readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            h=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(h is not None,"section divider rendered")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"readable case/donor/DIM row complete")
            readable.append(vals)
    secs=set(doc["review_sections"])
    required(len(secs)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in secs]==[r["display"] for r in rows],
             "all readable cells and fifteen topic groups agree with source grid")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "prior donor, four-case and ISA480/six-question records preserved")
    prior=json.loads((BASE/"SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    required(len(prior["exact_holds"])==19 and prior["source"]["source_table_high_resolution_geometry_verified"] is False,
             "all nineteen earlier G2-7C original source visual holds remain")
    required(sum(bool(r.get("G2_7C_source_correspondence")) for r in rows)==22
             and doc["SOSAReviewCompletion"]["G2_7C_XLSX_lag"]==0,
             "earlier twenty-two source-graded Payload AMPS cells retained")
    ledger=json.loads((BASE/"SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json").read_text(encoding="utf-8"))
    c=ledger["source_counts"];items=ledger["original_source_items"];ids={x["id"] for x in items}
    required(len(items)==len(ids)==44 and c["source_native_item_records"]==38
             and c["analytical_contexts"]==6 and len(ledger["exact_holds"])==17
             and c["PROFILE_FAMILY"]==4 and c["MATRIX_DEPTH_ROW"]==16
             and c["PROFILE_DASH_OPTION"]==5 and c["FULL_STRING_EXAMPLE"]==4
             and c["numbered_rule_shalls"]==0,
             "original Switch AMPS source census: 38 native+6 analytic, four families, sixteen rows, five dashes, four examples, seventeen holds")
    examples=[x["exact_printed_amps_string"] for x in items if x["native_kind"]=="FULL_STRING_EXAMPLE"]
    required(len(examples)==4 and sum(s.startswith("MODA3-") for s in examples)==3
             and sum(s.startswith("MODA6-") for s in examples)==1
             and sum("-j-" in s for s in examples)==2,
             "preserve four original printed MODA3/MODA6 source example strings and j placeholders")
    required((ledger["C239_cumulative_coverage"]["registered_headings"],
              ledger["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
              ledger["C239_cumulative_coverage"]["substantively_unread"],
              ledger["C239_cumulative_coverage"]["restricted"])==(192,158,33,1),
             "one additional original C239 section source-read; thirty-three unread, one restricted")
    required(ledger["source"]["full_matrix_visual_alignment_checked"] is False
             and ledger["source"]["publisher_ANSI_VITA65_0_65_1_read"] is False
             and ledger["source"]["original_C239_DSDM_IDL_OpenAPI_eight_read"] is False
             and ledger["DIM_Profile_adopted"] is False
             and ledger["independent_device_or_runtime_conformance"] is False,
             "source-visual and original normative companion gaps preserved; zero DIM or conformance adoption")
    qualified=[r for r in rows if r.get("G2_7D_source_correspondence")]
    required(len(qualified)==17
             and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7D_affected_row_ids"]),
             "exact seventeen justified original row IDs")
    changed=set()
    for row in qualified:
        ev=row["G2_7D_source_correspondence"]
        required(ev["source_item_ids"] and all(a in ids for a in ev["source_item_ids"]),
                 "G2-7D source item IDs in original inventory "+row["row_id"])
        required(ev["DIM_Profile_adopted"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["dense_switch_matrix_exact_pixel_alignment_unverified"],
                 "no invented hardware, Profile rule or exact matrix mapping "+row["row_id"])
        value=row["display"][8]
        required("G2-7D:" in value and value.startswith(ev["previous_sosa_cell_value"]),
                 "current source-qualified cell retains exact previous donor text "+row["row_id"])
        matches=[i for i,v in enumerate(grid) if v[8]==value and v[14]==row["label"]]
        required(len(matches)==1,"one source row-to-grid position "+row["row_id"])
        changed.add("I"+str(matches[0]+1))
    v=json.loads((BASE/"SOSA_G2_7D_Workbook_Validation_10NOV2026.json").read_text(encoding="utf-8"))
    required(v["G2_7D_qualified_existing_sosa_cells"]==17
             and len(changed)==17 and set(v["changed_saved_cells"])==changed
             and all(v["checks"].values()) and v["G2_7D_visual_matrix_complete"] is False,
             "exact seventeen saved SOSA source cells and partial original matrix audit")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7D-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7D_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7D"]["Excel_lag_cells"]==0,
             "mandatory L23 exact SAME original Excel exit and zero lag")
    book=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(book).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual original saved XLSX byte checksum and project source metadata")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"original saved Excel ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(cell.get("t")=="e" for cell in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no error-valued saved cell in "+path)
        wb=ET.fromstring(z.read("xl/workbook.xml"));sheets=list(wb.find(S+"sheets"))
        names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==v["workbook_sheets"],"original twenty-six sheets remain ordered")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in sheets:
            a=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=a.lstrip("/") if a.startswith("/") else "xl/"+a
        required(len(v["exact_original_untouched_xml_sha256"])==22,"twenty-two original historical sheets tracked")
        for name,h in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==h,
                     "unchanged historical original worksheet XML: "+name)
        ws,saved=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(saved==grid,"all 346x15 saved worksheet cells equal source JSON and readable mirrors")
        merges=[x.get("ref") for x in ws.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "original column groups and fifteen dividers intact")
        pane=ws.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "source-case columns and headings frozen")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA original-source audit remains open, SAPIENT blocked")
    print("PASS: G2-7D original §13.3.5 38 native and 6 analytic entries, 17 qualified existing SOSA comparisons, 17 precise holds.")
    print("PASS: SAME original 26-sheet 346x15 saved workbook, JSON, BOTH CSV and BOTH readable Markdown exact; 22 historical sheets unchanged.")
    print("LIMIT: original ANSI/VITA and 8 C239 native companions unread, dense physical matrix pixel alignment unverified, 33 C239 headings unread and 1 restricted, no DIM/Profile or installed-device adoption.")



def verify_sosa_g2_7e_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent source-graded C239 §13.3.6 + same saved XLSX/CVS/Markdown verification."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(row)==15 for row in grid),
             "G2-7E original canonical 329 information rows and full 346x15 grid")
    required([c["key"] for c in doc["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [c["key"] for c in doc["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
             and doc["columns"][-1]["key"]=="DIM",
             "four empirical case columns left, independent SOSA donors, DIM far right")
    required(mirror==grid,"master JSON and first CSV exact source-cell equality")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second existing historical CSV exact JSON grid")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==twin.split("<table>",1)[1],
             "BOTH GitHub-readable Markdown master tables exact")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            h=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(h is not None,"readable section divider present")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"readable case/donor/DIM row includes all columns")
            readable.append(vals)
    sections=set(doc["review_sections"])
    required(len(sections)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in sections]==[r["display"] for r in rows],
             "source-readable cells and all fifteen topic divider rows match source grid")
    required(len(doc["originalDonorEvidence"])==58
             and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "original fifty-eight donor, seventy-three case, ISA480/six-question evidence retained")
    prevC=loadjson=lambda n:json.loads((BASE/n).read_text(encoding="utf-8"))
    g7c=prevC("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")
    g7d=prevC("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")
    required(len(g7c["exact_holds"])==19 and len(g7d["exact_holds"])==17,
             "19 prior original Payload and 17 prior original Switch local holds survive")
    required(sum(bool(r.get("G2_7C_source_correspondence")) for r in rows)==22
             and sum(bool(r.get("G2_7D_source_correspondence")) for r in rows)==17
             and doc["SOSAReviewCompletion"]["G2_7C_XLSX_lag"]==0
             and doc["SOSAReviewCompletion"]["G2_7D_XLSX_lag"]==0,
             "prior 22 Payload and 17 Switch source mappings and Excel checkpoints intact")
    ledger=prevC("SOSA_G2_7E_Original_Source_Item_Coverage_10NOV2026.json")
    c=ledger["source_counts"];items=ledger["original_source_items"];ids={x["id"] for x in items}
    required(len(items)==len(ids)==27 and c["native_records"]==21
             and c["analytical_contexts"]==6 and len(ledger["exact_holds"])==16,
             "original VITA66 item inventory 21 native / 6 analytical / 16 exact holds")
    required(c["SOURCE_CONTEXT"]==14 and c["TABLE"]==1
             and c["MT_PROFILE_EXAMPLE"]==3 and c["PROTOCOL_FIELD_EXAMPLE"]==3
             and c["original_numbered_RULE_SHALLs"]==0
             and c["unnumbered_scoped_narrative_must_statements"]==1,
             "one original source table, fourteen source contexts, three MT and three protocol examples, no numbered Rule")
    exampleStrings={x["literal"] for x in items if x["native_kind"]=="PROTOCOL_FIELD_EXAMPLE"}
    required(exampleStrings=={"[E18]","[4E18]","[N-3E18-3A6F]"},
             "exact printed original C239 bracketed optical protocol examples")
    mt={x["mt"] for x in items if x["native_kind"]=="MT_PROFILE_EXAMPLE"}
    required(mt=={"MTA1","MTB1","MTC1"},"three original example Optical Profiles retained")
    cov=ledger["C239_cumulative_coverage"]
    required((cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,159,32,1),
             "original heading accounting after one source-reviewed §13.3.6")
    required(ledger["source"]["page_image_pixels_verified"] is False
             and ledger["source"]["source_ANSI_VITA65_0_65_1_originals_reviewed"] is False
             and ledger["source"]["C239_native_DSDM_IDL_OpenAPI_original_eight_reviewed"] is False
             and ledger["DIM_Profile_adopted"] is False
             and ledger["installed_device_or_independent_conformance_performed"] is False,
             "exact original page-image and ANSI/VITA/native-source gaps/no model adoption retained")
    qualified=[r for r in rows if r.get("G2_7E_source_correspondence")]
    required(len(qualified)==15
             and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7E_affected_row_ids"]),
             "exact fifteen qualified existing source-to-DIM master rows")
    sourceCells=set()
    for row in qualified:
        ev=row["G2_7E_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
                 "stable original G2-7E source IDs belong to ledger "+row["row_id"])
        required(ev["DIM_Profile_adopted"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["original_table_page_pixels_unverified"],
                 "no native companion or pixel table audit falsely claimed "+row["row_id"])
        sourceValue=row["display"][8]
        required("G2-7E:" in sourceValue and sourceValue.startswith(ev["previous_sosa_cell_value"]),
                 "previous source interpretation retained verbatim before new evidence "+row["row_id"])
        hit=[i for i,x in enumerate(grid) if x[8]==sourceValue and x[14]==row["label"]]
        required(len(hit)==1,"unique original row-to-grid saved source-cell "+row["row_id"])
        sourceCells.add("I"+str(hit[0]+1))
    validation=prevC("SOSA_G2_7E_Workbook_Validation_10NOV2026.json")
    required(validation["G2_7E_qualified_existing_sosa_cells"]==15
             and len(sourceCells)==15 and sourceCells==set(validation["changed_saved_cells"])
             and all(validation["checks"].values())
             and validation["source_page_images_verified"] is False,
             "actual fifteen changed source cells and original source-pixel hold verified")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7E-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7E_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7E"]["Excel_lag_cells"]==0,
             "current G2-7E SAME original saved Excel with zero outstanding source-cell lag")
    book=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(book).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==validation["workbook_sha256"],
             "actual saved 26-sheet workbook bytes and canonical source/validation SHA agree")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved original Excel ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(c.get("t")=="e" for c in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no error-valued worksheet cells "+path)
        workbook=ET.fromstring(z.read("xl/workbook.xml"))
        sheets=list(workbook.find(S+"sheets"));names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==validation["workbook_sheets"],
                 "all 26 original saved worksheet names/order intact")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        sheetPaths={}
        for node in sheets:
            p=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            sheetPaths[node.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        required(len(validation["exact_original_untouched_xml_sha256"])==22,
                 "22 original historical evidence worksheet XMLs tracked")
        for name,h in validation["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(sheetPaths[name])).hexdigest()==h,
                     "original untouched source sheet preserved "+name)
        worksheet,saved=data_rows(z.read(sheetPaths["Master Crosswalk"]),15)
        required(saved==grid,"all original 346x15 actually saved Excel values equal canonical grid")
        merges=[x.get("ref") for x in worksheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "four source cases, donors/foundation and 15 merged topic dividers")
        pane=worksheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original four left source cases and header freeze intact")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA donor original source incomplete, SAPIENT next donor blocked")
    print("PASS: SOSA-G2-7E original §13.3.6 21 native source records, three MTs, three bracketed examples and 15 source mappings.")
    print("PASS: SAME original 26-sheet saved Excel, every 346x15 saved cell equals canonical JSON/two CSVs/two readable Markdown; 22 historic sheets unchanged.")
    print("LIMIT: ANSI/VITA, native 8 C239 companions, source page-image visuals and prior matrix holds remain; no final DIM/Profile or installed-conformance adoption.")


def verify_sosa_g2_7f_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent C239 §13.3.7 four native Rules and original 26-sheet Excel check."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(doc["columns"])==15 and all(len(r)==15 for r in grid),
             "original approved 329 information rows / 15 columns / 346 display rows")
    keys=[c["key"] for c in doc["columns"]]
    required(keys[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and keys[8:10]==["OpenGroupSOSA","SOSA"] and keys[-1]=="DIM",
             "four empirical source cases left, separate SOSA donors, DIM far right")
    required(mirror==grid,"source JSON and first CSV exact grid parity")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"second historical CSV identical to current canonical grid")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==twin.split("<table>",1)[1],
             "both GitHub-readable comparison tables exactly equal")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            h=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(h is not None,"source topic divider")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"all source-case/donor/DIM cells in readable row")
            readable.append(vals)
    sec=set(doc["review_sections"])
    required(len(sec)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in sec]==[r["display"] for r in rows],
             "readable 329 source rows and 15 dividers agree with entire canonical grid")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "58 older donor records, 73 four-case source facts, ISA480/six questions intact")
    def sourcefile(name):
        return json.loads((BASE/name).read_text(encoding="utf-8"))
    required(len(sourcefile("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==19
             and len(sourcefile("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==17
             and len(sourcefile("SOSA_G2_7E_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==16,
             "19,17,16 previous original-source and dense matrix holds persist")
    required(sum(bool(r.get("G2_7C_source_correspondence")) for r in rows)==22
             and sum(bool(r.get("G2_7D_source_correspondence")) for r in rows)==17
             and sum(bool(r.get("G2_7E_source_correspondence")) for r in rows)==15
             and all(doc["SOSAReviewCompletion"][f"G2_7{x}_XLSX_lag"]==0 for x in ("C","D","E")),
             "previous 22/17/15 original source-qualified donor cells and saved Excel exits preserved")
    z=sourcefile("SOSA_G2_7F_Original_Source_Item_Coverage_10NOV2026.json")
    c=z["source_counts"];its=z["original_source_items"];source_ids={x["id"] for x in its}
    required(len(its)==len(source_ids)==15 and c["native_items_excluding_analyst"]==10
             and c["analytical_contexts"]==5 and len(z["exact_holds"])==17,
             "original G2-7F 10 native plus 5 analytical entries and 17 precise holds")
    required((c["RULE"],c["OBSERVATION"],c["PERMISSION"],c["TABLE_REFERENCE"])==(4,1,1,3)
             and (c["source_RULE_shall"],c["source_RULE_must"],c["source_RECOMMENDATION"])==(3,1,0)
             and c["normative_rule_method_A_only"]==2 and c["normative_rule_method_A_and_D"]==2,
             "correct Rule/Observation/Permission totals, original modal wording and conformance methods")
    rules=[x for x in its if x["kind"]=="RULE"]
    required([x["printed_rule_id"] for x in rules]==["13.3.7-1","13.3.7-2","13.3.7-3","13.3.7-4"]
             and [x["printed_modal_verb"] for x in rules]==["shall","must","shall","shall"]
             and [x["conformance_methodology_printed_codes"] for x in rules]==[["A"],["A"],["A","D"],["A","D"]],
             "all four original printed Rule identifiers, modal verbs and A/D conformance codes exact")
    obs=next(x for x in its if x["kind"]=="OBSERVATION")
    perm=next(x for x in its if x["kind"]=="PERMISSION")
    required(obs["illustrated_UTP_count"]==4 and "subset" in obs["exception"]
             and perm["not_mandatory"] is True,
             "Observation's lane-subset exception retained; PCI Express EP1/EP2 Permission not promoted to SHALL")
    cov=z["C239_cumulative_coverage"]
    required((cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,160,31,1),
             "source 160/31/1 of 192 original registered C239 headings, not full corpus certification")
    required(z["source"]["original_image_pixel_rendering_verified"] is False
             and z["source"]["original_ANSI_VITA_and_C239_native_companions_read"] is False
             and z["DIM_and_CSAPI_Profile_adopted"] is False
             and z["installed_device_or_independent_conformance_performed"] is False,
             "honest original page-image and external native-source holds, no model or hardware conformance adoption")
    qualified=[r for r in rows if r.get("G2_7F_source_correspondence")]
    required(len(qualified)==18 and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7F_affected_row_ids"]),
             "exactly 18 existing SOSA source-qualified row IDs, no source-derived row proliferation")
    addresses=set()
    for r in qualified:
        ev=r["G2_7F_source_correspondence"]
        required(ev["source_item_ids"] and all(x in source_ids for x in ev["source_item_ids"]),
                 "every correspondence points to inspected original stable C239 source IDs "+r["row_id"])
        required(ev["DIM_Profile_adopted"] is False and ev["independent_conformance_performed"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["original_dense_matrix_pixels_unverified"],
                 "source audit/installed conformance/DIM adoption statuses not conflated "+r["row_id"])
        v=r["display"][8]
        required("G2-7F:" in v and v.startswith(ev["previous_sosa_cell_value"]),
                 "preserved previous donor evidence and new source comparison "+r["row_id"])
        hits=[i for i,x in enumerate(grid) if x[8]==v and x[14]==r["label"]]
        required(len(hits)==1,"unique saved row to source ID "+r["row_id"])
        addresses.add("I"+str(hits[0]+1))
    v=sourcefile("SOSA_G2_7F_Workbook_Validation_10NOV2026.json")
    required(v["G2_7F_qualified_existing_sosa_cells"]==18
             and len(addresses)==18 and addresses==set(v["changed_saved_cells"])
             and all(v["checks"].values()) and v["source_page_images_verified"] is False,
             "18 source-qualified actually changed Excel cells, source image held, all publisher checks true")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7F-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7F_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7F"]["Excel_lag_cells"]==0,
             "binding L23 SAME original Excel saved-cell checkpoint passed with zero lag")
    book=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(book).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "actual saved original 26-sheet workbook SHA equal current source and validation metadata")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        required(z.testzip() is None,"saved ZIP CRC")
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(z.read(path)).iter(S+"c")),
                         "no XLSX error-valued cell "+path)
        wb=ET.fromstring(z.read("xl/workbook.xml"));sheets=list(wb.find(S+"sheets"))
        required(len(sheets)==26 and [x.get("name") for x in sheets]==v["workbook_sheets"],
                 "same original 26 worksheet names and order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for x in sheets:
            p=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[x.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        required(len(v["exact_original_untouched_xml_sha256"])==22,"22 historical unaffected original sheets")
        for name,oldsha in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(z.read(paths[name])).hexdigest()==oldsha,
                     "byte-identical historical original worksheet "+name)
        sheet,values=data_rows(z.read(paths["Master Crosswalk"]),15)
        required(values==grid,"all 346x15 actual saved Excel values equal canonical JSON/BOTH CSV/Markdown")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "original four case columns, donor/OGC grouped header and 15 topic dividers")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original frozen source-case columns and row heading")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA donor original source remains incomplete, SAPIENT still blocked")
    print("PASS: G2-7F original C239 §13.3.7 4 Rules/1 Observation/1 Permission, 18 source qualified SOSA cells.")
    print("PASS: SAME original 26-sheet Excel, every 346x15 cell equals canonical JSON/BOTH CSV/BOTH readable Markdown, 22 unaffected sheets.")
    print("LIMIT: 31 C239 source headings unread and one restricted, original VITA/eight native companions and physical matrix pixels held; zero model/installed conformance.")


def verify_sosa_g2_7g_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent original C239 §13.3.8 analog pinout and SAME saved original Excel audit."""
    import hashlib
    import html
    grid=doc["review_grid"];rows=doc["rows"];keys=[c["key"] for c in doc["columns"]]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(keys)==15 and all(len(r)==15 for r in grid),
             "original approved 329 source rows, 15 donor/case/DIM columns, 346 display rows")
    required(keys[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and keys[8:10]==["OpenGroupSOSA","SOSA"] and keys[-1]=="DIM",
             "approved source cases left, distinct The Open Group SOSA vs W3C, proposed DIM right")
    required(mirror==grid,"current source JSON and first CSV full-grid parity")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(newline="",encoding="utf-8") as f:
        required(list(csv.reader(f))==grid,"historical second CSV mirror matches canonical 346x15")
    twin=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==twin.split("<table>",1)[1],
             "BOTH readable source comparison HTML tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0];readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            h=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(h is not None,"source topic full-width divider retained")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(a) for a in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"readable original case/donor/DIM row 15 columns")
            readable.append(vals)
    sections=set(doc["review_sections"])
    required(len(sections)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in sections]==[r["display"] for r in rows],
             "every JSON/CSV/Markdown comparison cell and 15 source topic dividers agree")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "preserve 58 earlier donor facts,73 cases and ISA480/six source questions")
    def sourcefile(name):
        return json.loads((BASE/name).read_text(encoding="utf-8"))
    previous=[("C",19,22),("D",17,17),("E",16,15),("F",17,18)]
    for step,hold_count,cell_count in previous:
        z=sourcefile("SOSA_G2_7"+step+"_Original_Source_Item_Coverage_10NOV2026.json")
        required(len(z["exact_holds"])==hold_count
                 and sum(bool(r.get("G2_7"+step+"_source_correspondence")) for r in rows)==cell_count
                 and doc["SOSAReviewCompletion"]["G2_7"+step+"_XLSX_lag"]==0,
                 "preserve previous source/SOSA workbook checkpoint G2-7"+step)
    z=sourcefile("SOSA_G2_7G_Original_Source_Item_Coverage_10NOV2026.json")
    count=z["source_counts"];src=z["original_source_items"];source_ids={a["id"] for a in src}
    required(len(src)==len(source_ids)==36 and count["native_source_items"]==30
             and count["analytical_contexts"]==6 and len(z["exact_holds"])==19,
             "G2-7G direct source item inventory, stable IDs, exact unresolved holds")
    required(count["RULE"]==2 and count["RECOMMENDATION"]==1
             and count["OBSERVATION"]==1 and count["FIGURE"]==3
             and count["PIN_ROW"]==10 and count["SOURCE_CONTEXT"]==13,
             "native two Rules, one Recommendation, one Observation, three Figures, ten SMPM10 pin text rows")
    rules=[x for x in src if x["kind"]=="RULE"]
    required({r["source_rule"] for r in rules}=={"13.3.8.1-1","13.3.8.2-2"}
             and all(r["printed_modal_verb"]=="shall" for r in rules),
             "actual original two numbered SHALL Rules without inventing Rule13.3.8.2-1")
    a=next(r for r in rules if r["source_rule"]=="13.3.8.1-1")
    b=next(r for r in rules if r["source_rule"]=="13.3.8.2-2")
    required(a["conformance_method_printed"] is None
             and b["conformance_method_printed"]==["T"],
             "SMPM10 no printed conformance method; SMPM14 Rule T retained")
    recommend=next(x for x in src if x["kind"]=="RECOMMENDATION")
    observation=next(x for x in src if x["kind"]=="OBSERVATION")
    required(recommend["printed_modal_verb"]=="should"
             and recommend["conformance_method_printed"]==["T"]
             and recommend["not_mandatory_rule"] is True
             and observation["single_channel"]=="B1"
             and observation["two_channels"]=={"channel_1":"B1","channel_2":"B4"}
             and observation["geometry_and_other_six_contact_assignments_verified"] is False,
             "separate source SHOULD Recommendation and scoped B1/B4 Observation, not complete eight-channel map")
    pins=[x for x in src if x["kind"]=="PIN_ROW"]
    required({p["pin"] for p in pins}=={"A1","A2","A3","B1","B2","B3","B4","C1","C2","C3"}
             and len(pins)==10 and all(p["graphic_contact_geometry_verified"] is False for p in pins),
             "ten readable printed SMPM10 signal rows and visual contact geometry source held")
    conflict=next(x for x in src if x["id"].endswith("SOURCE_CONTEXT-TABLE_POINTER_INCONSISTENCY"))
    required(conflict["caption_pointer"]=="6.5.4.6.4-1"
             and conflict["numbered_rule_pointer"]=="6.4.5.6.4-1",
             "exact original conflicting SMPM14 Figure/Table reference locators preserved")
    cov=z["C239_cumulative_coverage"]
    required(len(z["original_registered_heading_coverage"])==1
             and len(z["additional_nested_subsections_reviewed"])==2
             and (cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
                  cov["substantively_unread"],cov["restricted"])==(192,161,30,1),
             "one newly source-reviewed C239 registered heading, two nested, original coverage still PARTIAL")
    required(z["source"]["original_page_images_verified"] is False
             and z["source"]["original_ANSI_VITA65_1_67_3_66_5_companions_read"] is False
             and z["source"]["original_C239_DSDM_IDL_OpenAPI_eight_companions_read"] is False
             and z["DIM_CSAPI_Profile_adopted"] is False
             and z["runtime_or_independent_hardware_conformance_performed"] is False,
             "source image, ANSI/VITA and native companions access held, no adopted model or device conformance")
    qualified=[r for r in rows if r.get("G2_7G_source_correspondence")]
    required(len(qualified)==18
             and {r["row_id"] for r in qualified}==set(doc["workbookSnapshot"]["G2_7G_affected_row_ids"]),
             "18 source-qualified existing master target row IDs, no row additions")
    addresses=set()
    for r in qualified:
        ev=r["G2_7G_source_correspondence"]
        required(ev["source_item_ids"] and all(x in source_ids for x in ev["source_item_ids"]),
                 "stable original source-item reference for "+r["row_id"])
        required(ev["DIM_Profile_adopted"] is False
                 and ev["runtime_or_independent_conformance_performed"] is False
                 and ev["source_pinout_figures_pixel_verified"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"],
                 "no unjustified legal pinout geometry/native standard, adopted DIM/Profile or hardware conformance")
        v=r["display"][8]
        required("G2-7G:" in v and v.startswith(ev["previous_sosa_cell_value"]),
                 "previous native SOSA donor text retained verbatim, new source-qualified relation appended")
        hits=[i for i,x in enumerate(grid) if x[8]==v and x[14]==r["label"]]
        required(len(hits)==1,"unique source row/grid cell "+r["row_id"])
        addresses.add("I"+str(hits[0]+1))
    validation=sourcefile("SOSA_G2_7G_Workbook_Validation_10NOV2026.json")
    required(validation["G2_7G_qualified_existing_sosa_cells"]==18
             and len(addresses)==18 and addresses==set(validation["changed_saved_cells"])
             and all(validation["checks"].values())
             and validation["source_figure_pixels_verified"] is False,
             "eighteen actual SOSA saved-cell deltas and all published sheet integrity checks")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7G-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7G_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7G"]["Excel_lag_cells"]==0,
             "binding G2-7G SAME saved Excel L23 gate and zero outstanding lag")
    original=(BASE/(NAME+".xlsx")).read_bytes();sha=hashlib.sha256(original).hexdigest()
    required(sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]
             ==validation["workbook_sha256"],"actual saved original 26-sheet workbook checksum equals canonical metadata")
    with zipfile.ZipFile(io.BytesIO(original)) as zbook:
        required(zbook.testzip() is None,"actual saved workbook ZIP CRC")
        for path in zbook.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(zbook.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(zbook.read(path)).iter(S+"c")),
                         "no error-valued cell in current/historical worksheet "+path)
        workbook=ET.fromstring(zbook.read("xl/workbook.xml"))
        sheets=list(workbook.find(S+"sheets"));sheetnames=[x.get("name") for x in sheets]
        required(len(sheetnames)==26 and sheetnames==validation["workbook_sheets"],
                 "same 26 original workbook worksheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(zbook.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for node in sheets:
            target=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[node.get("name")]=target.lstrip("/") if target.startswith("/") else "xl/"+target
        required(len(validation["exact_original_untouched_xml_sha256"])==22,"22 original unaffected historical sheets tracked")
        for name,oldsha in validation["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(zbook.read(paths[name])).hexdigest()==oldsha,
                     "historical worksheet bytes preserved "+name)
        sheet,actual=data_rows(zbook.read(paths["Master Crosswalk"]),15)
        required(actual==grid,"every actual 346x15 saved Excel cell equals JSON and BOTH CSV/Markdown")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "source-case/other-donor/foundation original header groups and 15 topic dividers")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original source cases and header frozen panes")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "full original SOSA donor remains OPEN, SAPIENT next donor blocked")
    print("PASS: G2-7G original C239 §13.3.8 30 native items/two Rules/one Recommendation/Observation/three Figures/ten text pins and 18 qualified SOSA cells.")
    print("PASS: SAME original 26-sheet workbook, exact saved 346x15 cell equality to canonical JSON/BOTH CSV/BOTH readable markdown, all 22 untouched historical sheets.")
    print("LIMIT: original figure pixels, 30 other C239 headings, one restricted, ANSI/VITA and C239 native companions unreviewed; no DIM/Profile or hardware conformance.")



def verify_sosa_g2_7h_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent original §13.4 source census and actual G2-7H 26-sheet XLSX readback."""
    import hashlib
    import html
    grid=doc["review_grid"]; rows=doc["rows"]; columns=doc["columns"]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and all(len(g)==15 for g in grid) and len(columns)==15,
             "original 329 source rows, 346 grid rows and 15 approved columns")
    required([x["key"] for x in columns[:4]]==["Dragino","AirGradient","Campbell","Bennett"]
             and [x["key"] for x in columns][8:10]==["OpenGroupSOSA","SOSA"]
             and columns[-1]["key"]=="DIM",
             "original four source cases, distinct Open Group and W3C, proposed DIM at right")
    required(grid==mirror,"master JSON and first CSV exactly match")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"both CSV mirrors equal original master source grid")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==other.split("<table>",1)[1],
             "both readable comparison tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    compared=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            header=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(header is not None,"source divider present")
            compared.append([html.unescape(header.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"15-column human-readable comparison row")
            compared.append(vals)
    required(len(doc["review_sections"])==15 and compared==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in set(doc["review_sections"])]
             ==[r["display"] for r in rows],"all four source formats, row order, topic dividers match")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "previous 58 donor, 73 case and ISA 480/six exact unresolved source evidence intact")
    def load(name):
        return json.loads((BASE/name).read_text(encoding="utf-8"))
    z=load("SOSA_G2_7H_Original_Source_Item_Coverage_11NOV2026.json")
    original=z["original_source_items"]; kinds=z["source_counts"]; ids={a["id"] for a in original}
    required(len(original)==len(ids)==57 and kinds["native_source_items"]==57
             and [kinds[k] for k in ("HEADING","CONTEXT","FIGURE","TABLE","CONFIG","THERMAL","OBSERVATION","TBD")]
                 ==[9,10,2,4,9,3,2,18],
             "all 57 original VNX typed source entries: heading/context/figure/table/config/thermal/Observation/TBD")
    required(kinds["source_numbered_RULE_SHALL"]==0
             and kinds["source_numbered_RECOMMENDATION_SHOULD"]==0
             and kinds["source_numbered_OBSERVATIONS"]==2
             and len(z["registered_headings"])==9 and len(z["nested_subsections"])==17
             and len(z["exact_holds"])==17,
             "two original descriptive Observations, no numbered SHALL or SHOULD and 17 source holds")
    cfg=z["connector_table_rows"]
    required(len(cfg)==9 and {(v["size"],v["mode"],v["pins"]) for v in cfg}
       =={(a,b,c) for a in ("19mm","32.5mm","39mm")
                   for b,c in (("Connector Only",400),("Small Aperture",320),("Large Aperture",240))},
       "all nine original VNX configuration table values and pin-count possibilities")
    required(len([v for v in cfg if v["config_class"]=="1" and v["aperture_fill"]=="None"])==1
             and len([v for v in cfg if v["config_class"]=="TBD"])==8
             and cfg[0]["image_cell"]=="BLANK",
             "source first 19mm connector-only Class1 vs eight TBD classes, blank source image")
    required((z["C239_cumulative_coverage"]["registered"],
              z["C239_cumulative_coverage"]["at_least_sampled_or_inline_read"],
              z["C239_cumulative_coverage"]["substantively_unread"],
              z["C239_cumulative_coverage"]["restricted"])==(192,170,21,1),
             "nine newly inline-reviewed original TOC headings but NOT full 192-section audit")
    required(z["source"]["inline_source_text_examined"] is True
             and z["source"]["figure_images_verified"] is False
             and z["source"]["VITA_74_native_read"] is False
             and z["source"]["eight_C239_DSDM_IDL_OpenAPI_native_read"] is False
             and z["source"]["later_S251_original_read"] is False
             and z["DIM_Profile_adopted"] is False
             and z["independent_hardware_runtime_conformance"] is False,
             "source figure/native ANSI-VITA/2025 edition holds and no DIM/Profile/hardware claims")
    required(len(load("SOSA_G2_7G_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==19
             and doc["SOSAReviewCompletion"]["G2_7G_XLSX_lag"]==0,
             "previous G2-7G original aperture and saved-workbook result preserved")
    qualified=[row for row in rows if row.get("G2_7H_source_correspondence")]
    required(len(qualified)==16
             and {row["row_id"] for row in qualified}==
                 set(doc["workbookSnapshot"]["G2_7H_affected_row_ids"]),
             "sixteen existing row IDs only, no new domain-model row")
    addresses=set()
    for row in qualified:
        ev=row["G2_7H_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"])
                 and row["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7H:" in row["display"][8]
                 and ev["figure_images_verified"] is False
                 and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
                 and ev["DIM_Profile_adopted"] is False
                 and ev["independent_equipment_runtime_conformance_performed"] is False,
                 "native source refs, preserved prior donor cell, no uninspected native claims "+row["row_id"])
        hits=[i for i,r in enumerate(grid) if r[8]==row["display"][8] and r[14]==row["label"]]
        required(len(hits)==1,"unique saved source grid record "+row["row_id"])
        addresses.add("I"+str(hits[0]+1))
    report=load("SOSA_G2_7H_Workbook_Validation_11NOV2026.json")
    required(report["G2_7H_qualified_existing_sosa_cells"]==16
             and set(report["changed_saved_cells"])==addresses
             and len(addresses)==16 and all(report["checks"].values()),
             "independent source-to-16-saved-cell delta and full workbook integrity record")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7H-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7H_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7H"]["Excel_lag_cells"]==0,
             "new same-Excel original G2-7H verification and ZERO lag")
    saved=(BASE/(NAME+".xlsx")).read_bytes()
    saved_sha=hashlib.sha256(saved).hexdigest()
    required(saved_sha==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]==
             report["workbook_sha256"],"actual committed binary workbook checksum and master metadata")
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        required(book.testzip() is None,"current 26-sheet ZIP CRC")
        for file in book.namelist():
            if file.endswith((".xml",".rels")):ET.fromstring(book.read(file))
            if file.startswith("xl/worksheets/") and file.endswith(".xml"):
                required(not any(t.get("t")=="e" for t in ET.fromstring(book.read(file)).iter(S+"c")),
                         "no error cells in actual workbook")
        wb=ET.fromstring(book.read("xl/workbook.xml"))
        sheets=list(wb.find(S+"sheets")); names=[t.get("name") for t in sheets]
        required(len(names)==26 and names==report["workbook_sheets"],
                 "same original 26 worksheet names/order")
        links={t.get("Id"):t.get("Target") for t in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for sheet in sheets:
            url=links[sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[sheet.get("name")]=url.lstrip("/") if url.startswith("/") else "xl/"+url
        required(len(report["exact_original_untouched_xml_sha256"])==22,
                 "original 22 historical worksheets counted")
        for sheet,digest in report["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(book.read(paths[sheet])).hexdigest()==digest,
                     "original historical sheet content "+sheet)
        main,actual=data_rows(book.read(paths["Master Crosswalk"]),15)
        required(actual==grid,"all actual saved 346x15 cells agree with JSON/BOTH CSV/BOTH Markdown")
        merges=[t.get("ref") for t in main.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+
                 [f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "owner-approved four cases/OGC grouped columns and 15 full-width topic dividers")
        pane=main.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original frozen case columns and source heading panes")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA donor stays open and next SAPIENT donor stays blocked")
    print("PASS: G2-7H 57 original VNX native entries, nine registered source headings, 17 nested, 18 TBD, two Observations, zero Rules.")
    print("PASS: all 346x15 saved cells, both CSV/MD mirrors, 16 SOSA I-column changes, 26 sheets and 22 unaffected original XML sheets.")
    print("LIMIT: remaining C239 21 unread/one restricted and unexamined figure/VITA/DSDM/IDL/OpenAPI/later-edition sources; zero DIM/Profile adoption.")



def verify_sosa_g2_7i_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independently audit source-grade C239 §13.5 Class1&2 J1 and SAME saved original XLSX."""
    import hashlib
    import html
    grid=doc["review_grid"]
    rows=doc["rows"]
    columns=[x["key"] for x in doc["columns"]]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and all(len(x)==15 for x in grid) and len(columns)==15,
             "original canonical master 329 information rows and all 346x15 cells")
    required(columns[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and columns[8:10]==["OpenGroupSOSA","SOSA"] and columns[-1]=="DIM",
             "owner-approved source cases, distinct Open Group and W3C SOSA, proposed DIM on right")
    required(grid==mirror,"canonical JSON and first CSV mirror exact source grid")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second CSV mirror exact original grid")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==other.split("<table>",1)[1],
             "both readable Markdown comparison tables identical")
    data=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",data,re.S):
        if 'colspan="15"' in tr:
            h=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(h is not None,"topic divider HTML cell")
            readable.append([html.unescape(h.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"full-width original donor/case information row")
            readable.append(vals)
    required(len(doc["review_sections"])==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in set(doc["review_sections"])]
              ==[r["display"] for r in rows],
             "all source grid, two readable tables, original information rows and topic dividers")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "original 58 donor/73 case/ISA480 outcomes and six source questions preserved")
    def load(name):
        return json.loads((BASE/name).read_text(encoding="utf-8"))
    z=load("SOSA_G2_7I_Original_Source_Item_Coverage_11NOV2026.json")
    c=z["source_counts"]; original=z["source_items"]; source_ids={x["id"] for x in original}
    required(len(original)==len(source_ids)==82 and c["total"]==82
             and c["HEADING"]==3 and c["NESTED_SECTION"]==4
             and c["TABLE"]==3 and c["CLASS_ROW"]==2 and c["FIGURE"]==1
             and c["RULE"]==23 and c["PERMISSION"]==4 and c["OBSERVATION"]==3
             and c["CONNECTOR"]==16 and c["J1_PIN"]==11
             and c["rules_method_I"]==18 and c["rules_method_A"]==5
             and len(z["exact_holds"])==20,
             "82 original native entries classified, 23 Rules, four Permissions, three Observations, 16 J and 11 J1 rows")
    rules=[a for a in original if a["kind"]=="RULE"]
    required(len(rules)==23
             and sum(a["printed_conformance_method"]=="I" for a in rules)==18
             and sum(a["printed_conformance_method"]=="A" for a in rules)==5
             and all(a["printed_modal"]=="shall" for a in rules),
             "23 exact original numbered SHALL Rules and printed methodology counts")
    perms=[a for a in original if a["kind"]=="PERMISSION"]
    required(len(perms)==4
             and any(a["id"].endswith("PERMISSION-13_5_2_4") for a in perms),
             "original Permission13.5.2-4 printed atypical native ID retained")
    obs=next(a for a in original if a["id"].endswith("OBSERVATION-13_5_2_2_1_2"))
    required(obs["not_rule"] is True and obs["printed_method"]=="I",
             "Observation13.5.2.2.1-2 remains Observation despite original printed Inspection I")
    connectors=[a for a in original if a["kind"]=="CONNECTOR"]
    required({a["id"].split("-")[-1] for a in connectors}=={"J"+str(i) for i in range(1,17)}
             and all(a.get("original_modality_support") and a.get("original_connector_type") for a in connectors),
             "16 original J connector types and modality information retained")
    required(next(a for a in connectors if a["id"].endswith("-J7"))["insert"]=="UNPRINTED"
             and next(a for a in connectors if a["id"].endswith("-J14"))["original_connector_type"]=="UNPRINTED_IN_ORIGINAL_PARSED_TABLE",
             "unprinted J7 insert and J14 type not silently fabricated")
    power=[a for a in original if a["kind"]=="J1_PIN"]
    required({a["id"].split("-")[-1] for a in power}==set("DEFLCGK A JBH".replace(" ",""))
             and len(power)==11,"J1 five positive/return pairs plus ground K source pin rows")
    cov=z["c239_coverage"]
    required((cov["total"],cov["at_least_sampled_or_inline"],cov["unread"],cov["restricted"])==(192,173,18,1)
             and cov["full_13_5_review"] is False and cov["newly_touched"]==3,
             "C239 coverage source grade correctly stays PARTIAL on §13.5 and §13.5.2 parents")
    required(z["source"]["figure_pixels_verified"] is False
             and z["source"]["original_SAE_MIL_VITA_unread"] is True
             and z["source"]["C239_eight_native_files_unread"] is True
             and z["DIM_and_CSAPI_Profile_adopted"] is False
             and z["independent_hardware_conformance_performed"] is False,
             "original figures/external standards/native files still held and no DIM/Profile/hardware conformance")
    prev=load("SOSA_G2_7H_Original_Source_Item_Coverage_11NOV2026.json")
    required(len(prev["exact_holds"])==17 and doc["SOSAReviewCompletion"]["G2_7H_XLSX_lag"]==0,
             "previous G2-7H original evidence and canonical Excel preserved")
    changed=[r for r in rows if r.get("G2_7I_source_correspondence")]
    required(len(changed)==25 and {r["row_id"] for r in changed}
             ==set(doc["workbookSnapshot"]["G2_7I_affected_row_ids"]),
             "25 existing source-qualified target IDs without extra DIM elements or rows")
    addresses=set()
    for r in changed:
        ev=r["G2_7I_source_correspondence"]
        required(ev["source_item_ids"] and all(k in source_ids for k in ev["source_item_ids"])
                 and r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7I:" in r["display"][8]
                 and ev["figure_and_native_companion_unverified"] is True
                 and ev["DIM_Profile_adopted"] is False and ev["independent_device_conformance"] is False,
                 "each existing donor cell maps to stable original source ID, no adopted DIM or live conformance "+r["row_id"])
        hits=[i for i,g in enumerate(grid) if i>1 and g[8]==r["display"][8] and g[14]==r["label"]]
        required(len(hits)==1,"unique source grid location "+r["row_id"])
        addresses.add("I"+str(hits[0]+1))
    validation=load("SOSA_G2_7I_Workbook_Validation_11NOV2026.json")
    required(validation["G2_7I_qualified_existing_sosa_cells"]==25
             and set(validation["changed_saved_cells"])==addresses
             and len(addresses)==25 and all(validation["checks"].values()),
             "25 source-grounded SOSA-I Excel deltas and actual saved-workbook checks")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7I-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7I_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7I"]["Excel_lag_cells"]==0,
             "required L23 SAME original Excel exit, ZERO lag")
    saved=(BASE/(NAME+".xlsx")).read_bytes()
    digest=hashlib.sha256(saved).hexdigest()
    required(digest==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]
             ==validation["workbook_sha256"],"actual current saved workbook SHA equals committed source and validation")
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        required(book.testzip() is None,"SAME workbook ZIP CRC valid")
        for entry in book.namelist():
            if entry.endswith((".xml",".rels")):ET.fromstring(book.read(entry))
            if entry.startswith("xl/worksheets/") and entry.endswith(".xml"):
                required(not any(t.get("t")=="e" for t in ET.fromstring(book.read(entry)).iter(S+"c")),
                         "no spreadsheet error cell in any worksheet")
        wb=ET.fromstring(book.read("xl/workbook.xml"))
        sheets=list(wb.find(S+"sheets")); names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==validation["workbook_sheets"],
                 "same 26 original worksheet names/order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for x in sheets:
            p=rels[x.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[x.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        required(len(validation["exact_original_untouched_xml_sha256"])==22,"22 unaffected historical sheets")
        for name,sha in validation["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(book.read(paths[name])).hexdigest()==sha,
                     "preserve exact earlier source worksheet bytes "+name)
        sheet,values=data_rows(book.read(paths["Master Crosswalk"]),15)
        required(values==grid,"every saved 346x15 grid cell equals canonical JSON/both CSV/both Markdown")
        merges=[v.get("ref") for v in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+
                 [f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "four cases left, standards grouped, DIM right and 15 topic dividers retained")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "approved frozen original source-case columns/header preserved")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA donor still OPEN and next SAPIENT donor blocked")
    print("PASS: original G2-7I C239 82 native entries/23 Rules/4 Permissions/3 Observations/16 connectors/11 J1 pins, 20 held sources.")
    print("PASS: 25 exact SOSA column-I cells and 346x15 saved source grid match JSON/BOTH CSV/BOTH Markdown; same 26 sheets and 22 original historical XML preserved.")
    print("LIMIT: 18 original C239 headings still unread, one restricted, §13.5 other clauses and original SAE/MIL/VITA/DSDM/IDL/OpenAPI/S251 source held.")



def verify_sosa_g2_7j_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent J2 original source, canonical mirrors and SAME saved XLSX verifier."""
    import hashlib, html
    grid=doc["review_grid"];rows=doc["rows"];keys=[x["key"] for x in doc["columns"]]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and len(keys)==15 and all(len(r)==15 for r in grid),
             "approved canonical 329 source rows and full 346x15 source grid")
    required(keys[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and keys[8:10]==["OpenGroupSOSA","SOSA"] and keys[-1]=="DIM",
             "four source cases, distinct Open Group/W3C SOSA and proposed DIM right")
    required(mirror==grid,"canonical JSON equals first CSV source grid")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"second source CSV exact match")
    second_md=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==second_md.split("<table>",1)[1],
             "both GitHub-readable horizontal comparison tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0];readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            heading=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(heading is not None,"source topic divider")
            readable.append([html.unescape(heading.group(1))]+[""]*14)
        else:
            vals=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(vals)==15,"15-column readable source row")
            readable.append(vals)
    sections=set(doc["review_sections"])
    required(len(sections)==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in sections]
                  ==[r["display"] for r in rows],
             "all canonical JSON, both CSV, both Markdown, 15 original topic groups and row order agree")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "prior 58 donor/73 cases/480 ISA source outcomes and six unresolved questions preserved")
    def source(n):return json.loads((BASE/n).read_text(encoding="utf-8"))
    z=source("SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json")
    count=z["source_counts"];original=z["original_source_items"];ids={x["id"] for x in original}
    required(len(original)==len(ids)==134 and count["total_source_native_items"]==134
             and [count[k] for k in ("SECTION","RULE","OBSERVATION","FIGURE","TABLE","SOURCE_CONTEXT","SIGNAL_GROUP","PIN_LABEL")]
                 ==[2,8,4,1,1,7,26,85],
             "134 stable original J2 source-native entries, exact type categories")
    required(count["numbered_rules"]==8 and count["rules_inspection_I"]==6
             and count["rules_test_T"]==2 and count["numbered_observations"]==4
             and count["numbered_permissions"]==0 and count["source_signal_groups"]==26
             and count["individually_printed_pin_label_records"]==85
             and count["aggregated_unresolved_pin_rosters"]==2
             and count["source_printed_pin_designator_tokens"]==103
             and len(z["source_holds"])==22,
             "eight native Rules, four Observations, 26 groups/103 pin tokens, 22 exact holds")
    rules=[v for v in original if v["kind"]=="RULE"]
    required({v["printed_rule_id"] for v in rules}=={
             "13.5.2.3-1","13.5.2.3-2","13.5.2.3-3","13.5.2.3-4",
             "13.5.2.3.1-1","13.5.2.3.1-2","13.5.2.3.1-3","13.5.2.3.1-4"}
             and sum(v["conformance_method_printed"]==["I"] for v in rules)==6
             and sum(v["conformance_method_printed"]==["T"] for v in rules)==2
             and all(v["printed_verb"]=="shall" for v in rules),
             "all eight original SHALL Rule IDs and printed I/T methods")
    byrule={v["printed_rule_id"]:v for v in rules}
    required("≥18.0" in byrule["13.5.2.3-3"]["meaning"]
             and "≤1.5" in byrule["13.5.2.3-4"]["meaning"]
             and "≥100" in byrule["13.5.2.3.1-1"]["meaning"]
             and "≤5" in byrule["13.5.2.3.1-2"]["meaning"]
             and "100 mA" in byrule["13.5.2.3.1-3"]["meaning"]
             and "30 VDC" in byrule["13.5.2.3.1-4"]["meaning"],
             "numeric high/low voltage and Power Enable ON/OFF conditions preserved")
    observations=[v for v in original if v["kind"]=="OBSERVATION"]
    required({v["printed_observation_id"] for v in observations}==
             {"13.5.2.3-1","13.5.2.3-2","13.5.2.3-3","13.5.2.3-4"}
             and all(v["normative_rule"] is False for v in observations),
             "four separate numbered Observations not transformed into Rules")
    groups=z["source_signal_groups"];records=z["printed_pin_label_evidence"]
    required(len(groups)==26 and sum(g["pin_count"] for g in groups)==103
             and len(records)==87 and len([x for x in records if x.get("aggregate")])==2
             and {x["group"] for x in records if x.get("aggregate")}=={"SENMAN","ARMING_ISOLATION"}
             and all(x["source_id"] in ids for x in records),
             "six-page table pin-label evidence and two held manufacturer/isolated-arming rosters")
    pins={v["pin"] for v in records if not v.get("aggregate")}
    required(len(pins)==85 and {"25-1","25-2","25-S","75-1","75-2","75-S"}<=pins,
             "literal original twinax 1553B subcontact designators cannot be collapsed")
    coverage=z["c239_cumulative_registered_headings"]
    required((coverage["total"],coverage["at_least_sampled_or_inline_reviewed"],
              coverage["substantively_unread"],coverage["restricted"])==(192,173,18,1)
             and coverage["newly_registered_headings_reviewed"]==0
             and coverage["full_13_5_source_coverage"] is False,
             "G2-7J nested source items do not falsely increment registered heading completion")
    origin=z["source"]
    required(origin["original_inline_text_examined"] is True
             and origin["source_table_text_examined_all_six_pages"] is True
             and origin["original_figure_pixels_verified"] is False
             and origin["original_table_graphic_alignment_verified"] is False
             and origin["eight_C239_model_API_companions_reviewed"] is False
             and origin["original_S251_2025_reviewed"] is False
             and z["model_or_CSAPI_Profile_adopted"] is False
             and z["independent_hardware_conformance"] is False,
             "source text grades/figure hold/natives and no DIM/Profile/physical conformance retained")
    prior=source("SOSA_G2_7I_Original_Source_Item_Coverage_11NOV2026.json")
    required(len(prior["exact_holds"])==20 and doc["SOSAReviewCompletion"]["G2_7I_XLSX_lag"]==0,
             "previous original G2-7I Rule/Excel evidence not lost")
    updated=[r for r in rows if r.get("G2_7J_source_correspondence")]
    required(len(updated)==25 and {r["row_id"] for r in updated}
             ==set(doc["workbookSnapshot"]["G2_7J_affected_row_ids"]),
             "twenty-five exact qualified existing source comparison rows")
    addresses=set()
    for r in updated:
        ev=r["G2_7J_source_correspondence"]
        required(ev["source_item_ids"] and all(v in ids for v in ev["source_item_ids"])
                 and r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7J:" in r["display"][8]
                 and ev["pinout_figure_and_dense_modality_matrix_unverified"] is True
                 and ev["external_native_companions_unread"] is True
                 and ev["DIM_Profile_adopted"] is False
                 and ev["independent_hardware_conformance"] is False,
                 "source item original IDs, prior donor cell preserved, no unwarranted equivalence "+r["row_id"])
        matches=[i for i,g in enumerate(grid) if i>1 and g[8]==r["display"][8] and g[14]==r["label"]]
        required(len(matches)==1,"unique source record actual grid row "+r["row_id"])
        addresses.add("I"+str(matches[0]+1))
    report=source("SOSA_G2_7J_Workbook_Validation_11NOV2026.json")
    required(report["G2_7J_qualified_existing_sosa_cells"]==25
             and len(addresses)==25 and set(report["changed_saved_cells"])==addresses
             and all(report["checks"].values()),"25 original SOSA-I cell deltas verified in actual saved workbook")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7J-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7J_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7J"]["Excel_lag_cells"]==0,
             "L23 required same-original-workbook 25-cell saved parity with ZERO lag")
    saved=(BASE/(NAME+".xlsx")).read_bytes()
    actual_hash=hashlib.sha256(saved).hexdigest()
    required(actual_hash==doc["currentWorkbookSha256"]==doc["workbookSnapshot"]["sha256"]
             ==report["workbook_sha256"],"saved binary workbook SHA256 agrees with source/validation")
    with zipfile.ZipFile(io.BytesIO(saved)) as zbook:
        required(zbook.testzip() is None,"actual saved 26-sheet Excel ZIP CRC")
        for part in zbook.namelist():
            if part.endswith((".xml",".rels")):ET.fromstring(zbook.read(part))
            if part.startswith("xl/worksheets/") and part.endswith(".xml"):
                required(not any(x.get("t")=="e" for x in ET.fromstring(zbook.read(part)).iter(S+"c")),
                         "no error-valued cells in any saved worksheet")
        wb=ET.fromstring(zbook.read("xl/workbook.xml"))
        sheets=list(wb.find(S+"sheets"));names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==report["workbook_sheets"],
                 "same original 26 sheet names and order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(zbook.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for sheet in sheets:
            p=rels[sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[sheet.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        required(len(report["exact_original_untouched_xml_sha256"])==22,
                 "22 previous worksheets unchanged and counted")
        for name,sha in report["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(zbook.read(paths[name])).hexdigest()==sha,
                     "exact historical worksheet bytes "+name)
        sheet,actual=data_rows(zbook.read(paths["Master Crosswalk"]),15)
        required(actual==grid,"all actual 346x15 saved cells match JSON/BOTH CSV/BOTH Markdown")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+
                 [f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "cases left, donor/OGC grouped, proposed DIM far-right and 15 topic dividers")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original four frozen empirical columns and source headers")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "SOSA remains OPEN and SAPIENT next donor BLOCKED")
    print("PASS: J2 original C239 134 source items, 103 printed pin-designators, 8 Rules (6 I/2 T), 4 Observations, 22 source holds.")
    print("PASS: all 346x15 actual saved Excel cells, both CSV/MD mirrors, 25 SOSA-I changes, SAME 26 sheets and 22 historical XMLs retained.")
    print("LIMIT: 18 original registered headings unread and one restricted; §13.5 partial, J2 graphics, companion/native standards and runtime conformance HELD.")



def verify_sosa_g2_7k_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent original C239 §13.5.2.3.2 two-Rule source, all saved Excel and mirror verification."""
    import hashlib, html
    grid=doc["review_grid"]; rows=doc["rows"]; keys=[c["key"] for c in doc["columns"]]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and all(len(r)==15 for r in grid) and len(keys)==15,
             "original master 329 information rows, 346x15 actual source review geometry")
    required(keys[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and keys[8:10]==["OpenGroupSOSA","SOSA"] and keys[-1]=="DIM",
             "original source cases, distinct OpenGroup and W3C SOSA, DIM-right approved layout")
    required(mirror==grid,"canonical JSON/CSV source grid parity")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"BOTH CSV mirrors match approved grid exactly")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==other.split("<table>",1)[1],
             "BOTH GitHub-readable source-comparison tables identical")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]; readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            title=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(title is not None,"source heading divider present")
            readable.append([html.unescape(title.group(1))]+[""]*14)
        else:
            cells=[html.unescape(v) for v in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(cells)==15,"every readable source information row has 15 columns")
            readable.append(cells)
    required(len(doc["review_sections"])==15 and readable==grid[2:]
             and [r for i,r in enumerate(grid) if i>1 and i not in set(doc["review_sections"])]
              ==[r["display"] for r in rows],
             "source-original 15 topic dividers, row order and both MD tables")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "earlier 58 donor records/73 empirical cases/480 ISA outcomes/six exact questions")
    def load(n):return json.loads((BASE/n).read_text(encoding="utf-8"))
    z=load("SOSA_G2_7K_Original_Source_Item_Coverage_11NOV2026.json")
    c=z["native_source_counts"];native=z["original_source_items"];source_ids={n["id"] for n in native}
    required(len(native)==len(source_ids)==7 and c["total_records"]==7
             and c["native_numbered_SHALL_Rules"]==2 and c["inspection_I_rules"]==2
             and c["source_contexts"]==1 and c["normative_companion_pointers"]==2
             and c["prior_source_cross_references"]==1 and c["nested_heading"]==1
             and c["numbered_recommendations"]==c["numbered_permissions"]==c["numbered_observations"]==0
             and len(z["exact_holds"])==11,
             "original 7 typed source items, 2 Inspection SHALLs, 11 source holds")
    rules=[v for v in native if v["kind"]=="RULE"]
    required({v["printed_rule_id"] for v in rules}=={"13.5.2.3.2-1","13.5.2.3.2-2"}
             and all(v["modal_verb"]=="shall" and v["conformance_methodology_printed"]==["I"] for v in rules),
             "both exact source Rule IDs/shall/method Inspection(I)")
    physical=next(v for v in native if v["kind"]=="SOURCE_CONTEXT")
    required(physical["wire_count"]==8 and physical["twisted_pair_count"]==4
             and physical["characteristic_impedance_ohms"]==100
             and physical["standing"]=="DESCRIPTIVE_SOURCE_CONTEXT_NOT_NUMBERED_RULE",
             "four twisted pairs, eight wires and 100-ohm unnumbered context, not third Rule")
    second=next(v for v in rules if v["printed_rule_id"]=="13.5.2.3.2-2")
    required(second["reference_IEEE"]=="IEEE 802.3-2008"
             and second["physical_medium"]=="1000BaseT"
             and second["cable_specification"]=="CAT 6A AS6070/6 or equivalent",
             "exact original IEEE edition/1000BaseT/cable alternative, not replacement specification")
    prior=load("SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json")
    required(z["prior_source_reference"]["source_item_id"] in {v["id"] for v in prior["original_source_items"]}
             and len(prior["source_holds"])==22
             and doc["SOSAReviewCompletion"]["G2_7J_XLSX_lag"]==0,
             "source-grade prior original J2 table and previous workbook checkpoint retained")
    cov=z["c239_registered_heading_standing"]
    required((cov["total_registered_headings"],cov["at_least_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,173,18,1)
             and cov["new_registered_headings_earned"]==0,
             "nested Ethernet does not advance original 192-heading coverage count")
    src=z["source"]
    required(src["source_access"]=="ORIGINAL_INLINE_TEXT_FULL_SUBSECTION_READ"
             and src["original_IEEE_802_3_2008_read"] is False
             and src["original_AS6070_6_read"] is False
             and src["original_C239_DSDM_IDL_OpenAPI_eight_read"] is False
             and z["DIM_CSAPI_Profile_adopted"] is False
             and z["independent_runtime_or_hardware_conformance"] is False,
             "unexamined external originals and zero DIM/Profile adoption or hardware conformance")
    matched=[r for r in rows if r.get("G2_7K_source_correspondence")]
    required(len(matched)==10
             and {r["row_id"] for r in matched}==set(doc["workbookSnapshot"]["G2_7K_affected_row_ids"]),
             "only ten qualified existing The Open Group SOSA master rows")
    addresses=set()
    for r in matched:
        v=r["G2_7K_source_correspondence"]
        required(v["source_item_ids"] and all(s in source_ids for s in v["source_item_ids"])
                 and r["display"][8].startswith(v["previous_sosa_cell_value"])
                 and "G2-7K:" in r["display"][8]
                 and v["original_IEEE_and_AS6070_6_companion_unread"] is True
                 and v["actual_1000BaseT_hardware_or_traffic_unverified"] is True
                 and v["DIM_Profile_adopted"] is False and v["independent_conformance"] is False,
                 "each incremental donor source meaning preserves earlier data, native holds and no model adoption "+r["row_id"])
        matches=[i for i,g in enumerate(grid) if i>1 and g[8]==r["display"][8] and g[14]==r["label"]]
        required(len(matches)==1,"unique native source-qualified grid row "+r["row_id"])
        addresses.add("I"+str(matches[0]+1))
    validation=load("SOSA_G2_7K_Workbook_Validation_11NOV2026.json")
    required(validation["G2_7K_qualified_existing_sosa_cells"]==10
             and set(validation["changed_saved_cells"])==addresses and len(addresses)==10
             and all(validation["checks"].values()),
             "ten exact source-qualified SOSA-I saved-cell deltas and all publisher integrity controls")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7K-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7K_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7K"]["Excel_lag_cells"]==0,
             "L23 saved-original-workbook checkpoint source parity and zero Excel lag")
    b=(BASE/(NAME+".xlsx")).read_bytes()
    required(hashlib.sha256(b).hexdigest()==doc["currentWorkbookSha256"]==
             doc["workbookSnapshot"]["sha256"]==validation["workbook_sha256"],
             "actual saved binary workbook hash matches master and independent record")
    with zipfile.ZipFile(io.BytesIO(b)) as wb:
        required(wb.testzip() is None,"Excel ZIP CRC")
        for p in wb.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(wb.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                required(not any(q.get("t")=="e" for q in ET.fromstring(wb.read(p)).iter(S+"c")),
                         "no formula/error-valued cells in any original worksheet")
        w=ET.fromstring(wb.read("xl/workbook.xml"))
        sheets=list(w.find(S+"sheets"));names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==validation["workbook_sheets"],
                 "SAME original 26-sheet workbook names and sheet order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(wb.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for sh in sheets:
            p=rels[sh.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[sh.get("name")]=p.lstrip("/") if p.startswith("/") else "xl/"+p
        required(len(validation["exact_original_untouched_xml_sha256"])==22,"original 22 preserved historical worksheets")
        for name,sha in validation["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(wb.read(paths[name])).hexdigest()==sha,
                     "unchanged original historical worksheet "+name)
        sheet,saved=data_rows(wb.read(paths["Master Crosswalk"]),15)
        required(saved==grid,"all 346x15 actual saved Excel cells agree with source JSON/BOTH CSV/BOTH MD")
        merges=[x.get("ref") for x in sheet.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merges==["A1:D1","E1:I1","J1:N1"]+
                 [f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "approved cases/other-donors/OGC and 15 topic dividers")
        pane=sheet.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "approved source-case and header frozen panes")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "C239 donor stays open and original Step18 SAPIENT blocked")
    print("PASS: source-native original C239 §13.5.2.3.2 two numbered Inspection SHALL Rules, four physical pairs and original IEEE/cable holds")
    print("PASS: 10 actual saved SOSA I-column cells; all 346x15 saved grid cells, both CSV/MD mirrors, original 26 sheets and 22 historical sheets")
    print("LIMIT: C239 source corpus remains PARTIAL (173 touched,18 unread,one restricted), external IEEE/AS6070/6 originals and real device conformance held.")


def verify_sosa_g2_7l_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Independent G2-7L original 2023 C239 source and all saved 26-sheet Excel cell verification."""
    import hashlib, html
    grid=doc["review_grid"]; rows=doc["rows"]; keys=[c["key"] for c in doc["columns"]]
    required(doc["schemaVersion"]=="0.15" and len(rows)==329 and len(grid)==346
             and all(len(r)==15 for r in grid) and len(keys)==15,
             "G2-7L original approved 329 information rows, 346×15 source grid")
    required(keys[:4]==["Dragino","AirGradient","Campbell","Bennett"]
             and keys[8:10]==["OpenGroupSOSA","SOSA"] and keys[-1]=="DIM",
             "source cases left, distinct Open Group/W3C SOSA, OGC foundation and DIM far right")
    required(mirror==grid,"canonical JSON and CSV exact")
    with (BASE/"ISA_Correction_Review_07NOV2026.csv").open(encoding="utf-8",newline="") as f:
        required(list(csv.reader(f))==grid,"BOTH CSV mirrors match current canonical source")
    other=(BASE/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    required("<table>" in md and md.split("<table>",1)[1]==other.split("<table>",1)[1],
             "BOTH readable Markdown comparisons exact")
    body=md.split("<tbody>",1)[1].split("</tbody>",1)[0]
    readable=[]
    for tr in re.findall(r"<tr>.*?</tr>",body,re.S):
        if 'colspan="15"' in tr:
            title=re.search(r'<th colspan="15">(.*?)</th>',tr,re.S)
            required(title is not None,"source topic divider has title")
            readable.append([html.unescape(title.group(1))]+[""]*14)
        else:
            cells=[html.unescape(x) for x in re.findall(r"<td>(.*?)</td>",tr,re.S)]
            required(len(cells)==15,"fifteen distinct source data cells in each readable row")
            readable.append(cells)
    required(len(doc["review_sections"])==15 and readable==grid[2:]
             and [x for i,x in enumerate(grid) if i>1 and i not in set(doc["review_sections"])]
                 ==[x["display"] for x in rows],
             "15 source topic divider rows, exact 329 original data rows, MD/JSON/CSV parity")
    required(len(doc["originalDonorEvidence"])==58 and len(doc["caseEvidence"])==73
             and doc["ISAEvidence"]["currentPrimaryReviews"]==480
             and doc["ISAEvidence"]["specificQuestions"]==6,
             "58 other-donor, 73 empirical case source records, ISA 480 outcomes and six questions retained")
    def load(n):
        return json.loads((BASE/n).read_text(encoding="utf-8"))
    z=load("SOSA_G2_7L_Original_Source_Item_Coverage_11NOV2026.json")
    c=z["counts"]; native=z["original_source_items"]; ids={v["id"] for v in native}
    required(len(native)==len(ids)==148==c["total_unique_native_evidence_records"]
             and c["source_numbered_rule_shalls"]==48
             and c["numbered_observations"]==6
             and c["numbered_recommendations_should"]==2
             and c["numbered_permissions_may"]==1
             and c["source_headings"]==23
             and c["table_texts"]==4
             and c["table_pin_rows"]==34
             and c["figure_captions"]==4
             and c["exact_source_holds"]==19,
             "complete 148 individual typed original C239 J2–J6 source items and exact holds")
    for kind,count in (("RULE",48),("OBSERVATION",6),("RECOMMENDATION",2),
                       ("PERMISSION",1),("NESTED_SECTION",23),("TABLE",4),
                       ("TABLE_PIN_ROW",34),("FIGURE_CAPTION",4)):
        required(len([v for v in native if v["kind"]==kind])==count,
                 "exact distinct original source kind "+kind)
    rules=[v for v in native if v["kind"]=="RULE"]
    required(len({v["source_rule_id"] for v in rules})==48
             and all(v["modal_verb"]=="shall" and v["conformance_methodology_printed"] for v in rules),
             "all 48 Rule identifiers, original SHALL and each printed conformance method distinct")
    required({v["source_rule_id"] for v in rules if v["source_rule_id"].startswith("13.5.2.7.1-")}
             ==set("13.5.2.7.1-"+str(i) for i in range(1,7)),
             "six source J6 power Rules retained including separately repeated -4/-5")
    rcs={v["source_item_id"]:v for v in native if v["kind"]=="RECOMMENDATION"}
    required(set(rcs)=={"13.5.2.7.1-1","13.5.2.7.1-2"}
             and rcs["13.5.2.7.1-1"]["conformance_methodology_printed"]==["I"]
             and not rcs["13.5.2.7.1-2"]["conformance_methodology_printed"],
             "source Recommendations both distinct SHOULD, first prints I and second no method")
    oc={v["source_item_id"]:v for v in native if v["kind"]=="OBSERVATION"}
    required(oc["13.5.2.7.1-2"]["conformance_methodology_printed"]==["I"],
             "original J6 Observation with printed Inspection method not converted to Rule")
    cov=z["c239_registered_heading_standing"]
    required((cov["registered"],cov["at_least_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,173,18,1)
             and cov["new_registered_headings_earned"]==0,
             "nested J2–J6 original source coverage earns zero new registered headings")
    source=z["source"]
    required(source["source_figure_pixels_verified"] is False
             and source["external_companion_originals_read"] is False
             and source["eight_native_companion_files_read"] is False
             and z["DIM_Profile_adopted"] is False and z["independent_equipment_conformance"] is False,
             "unexamined actual external originals/figures and no adoption or live conformance")
    mappings=z["qualified_existing_row_mappings"]
    required(len(mappings)==24 and len(z["exact_holds"])==19
             and len({v["label"] for v in mappings})==24
             and all(v["source_item_ids"] and all(x in ids for x in v["source_item_ids"])
                     and v["DIM_Profile_adopted"] is False for v in mappings),
             "24 independently source-cited existing semantic mappings,19 held,zero DIM adoption")
    matched=[r for r in rows if r.get("G2_7L_source_correspondence")]
    required(len(matched)==24 and {r["row_id"] for r in matched}
             ==set(doc["workbookSnapshot"]["G2_7L_affected_row_ids"])
             and {r["label"] for r in matched}=={v["label"] for v in mappings},
             "24 exact prior existing original master row IDs; no extra row/class")
    addresses=set()
    for row in matched:
        ev=row["G2_7L_source_correspondence"]
        required(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"])
                 and row["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7L:" in row["display"][8]
                 and ev["DIM_Profile_adopted"] is False
                 and ev["external_companions_and_figure_pixels_unverified"] is True,
                 "preserve earlier donor cell, source provenance, original holds and non-adoption "+row["row_id"])
        matches=[i for i,x in enumerate(grid) if i>1 and x[8]==row["display"][8] and x[14]==row["label"]]
        required(len(matches)==1,"single stable row/column match "+row["row_id"])
        addresses.add("I"+str(matches[0]+1))
    v=load("SOSA_G2_7L_Workbook_Validation_11NOV2026.json")
    required(v["G2_7L_qualified_existing_sosa_cells"]==24
             and set(v["changed_saved_cells"])==addresses
             and len(addresses)==24 and all(v["checks"].values()),
             "actual saved 24 SOSA donor I addresses, all publisher source/format checks")
    required(doc["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7L-CANONICAL-VERIFIED"
             and doc["workbookSnapshot"]["currently_matches_readable_view"] is True
             and doc["SOSAReviewCompletion"]["G2_7L_XLSX_lag"]==0
             and doc["SOSAEvidence"]["G2_7L"]["Excel_lag_cells"]==0,
             "L23 saved workbook snapshot current, no Excel lag")
    b=(BASE/(NAME+".xlsx")).read_bytes()
    required(hashlib.sha256(b).hexdigest()==doc["currentWorkbookSha256"]
             ==doc["workbookSnapshot"]["sha256"]==v["workbook_sha256"],
             "independently computed actual saved XLSX sha equals JSON and report")
    with zipfile.ZipFile(io.BytesIO(b)) as wb:
        required(wb.testzip() is None,"existing Excel ZIP CRC")
        for p in wb.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(wb.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                required(not any(cell.get("t")=="e" for cell in ET.fromstring(wb.read(p)).iter(S+"c")),
                         "no spreadsheet error cells in any of 26 worksheets")
        root=ET.fromstring(wb.read("xl/workbook.xml"))
        sheets=list(root.find(S+"sheets"))
        names=[x.get("name") for x in sheets]
        required(len(names)==26 and names==v["workbook_sheets"],
                 "SAME original 26 sheet names and exact order")
        rels={x.get("Id"):x.get("Target") for x in ET.fromstring(wb.read("xl/_rels/workbook.xml.rels"))}
        paths={}
        for sh in sheets:
            val=rels[sh.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
            paths[sh.get("name")]=val.lstrip("/") if val.startswith("/") else "xl/"+val
        required(len(v["exact_original_untouched_xml_sha256"])==22,
                 "full historical 22 untouched saved XML worksheet records")
        for name,sha in v["exact_original_untouched_xml_sha256"].items():
            required(hashlib.sha256(wb.read(paths[name])).hexdigest()==sha,
                     "original historical worksheet unchanged "+name)
        sh,actual=data_rows(wb.read(paths["Master Crosswalk"]),15)
        required(actual==grid,"ALL 346×15 actual saved Excel cells equal JSON/two CSV/two MD")
        merged=[x.get("ref") for x in sh.find(S+"mergeCells").findall(S+"mergeCell")]
        required(merged==["A1:D1","E1:I1","J1:N1"]+
                 [f"A{i+1}:O{i+1}" for i in doc["review_sections"]],
                 "original grouped columns and all 15 topic dividers")
        pane=sh.find(S+"sheetViews").find(S+"sheetView").find(S+"pane")
        required(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
                 "original frozen case columns and header")
    required(doc["SOSAReviewCompletion"]["source_coverage_complete"] is False
             and doc["SOSAReviewCompletion"]["step18_SAPIENT_blocked"] is True,
             "The Open Group SOSA remains OPEN, SAPIENT transition BLOCKED")
    print("PASS: independently verified original C239 J2–J6 148 typed source entries, 48 SHALL, six Observation, two SHOULD, one MAY; holds intact")
    print("PASS: 24 existing I-column mappings and every 346×15 actual saved cell, both CSVs, both MDs, 26 sheets, 22 untouched historic sheets")
    print("LIMIT: 173 sampled/inline (not fully complete), 18 unread,1 restricted; native companion and figure originals held, no DIM/Profile/device adoption")



def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

    if "review_grid" in doc and "columns" in doc:
        if len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7L"):
            verify_sosa_g2_7l_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7K"):
            verify_sosa_g2_7k_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7J"):
            verify_sosa_g2_7j_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7I"):
            verify_sosa_g2_7i_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7H"):
            verify_sosa_g2_7h_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7G"):
            verify_sosa_g2_7g_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7F"):
            verify_sosa_g2_7f_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7E"):
            verify_sosa_g2_7e_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7D"):
            verify_sosa_g2_7d_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7C"):
            verify_sosa_g2_7c_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7B"):
            verify_sosa_g2_7b_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7A"):
            verify_sosa_g2_7a_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_6D"):
            verify_sosa_g2_6d_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_6C"):
            verify_sosa_g2_6c_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_6B"):
            verify_sosa_g2_6b_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_6A"):
            verify_sosa_g2_6a_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_5"):
            verify_sosa_g2_5_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_4B"):
            verify_sosa_g2_4b_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15":
            verify_sosa_g2_4a_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.14":
            verify_sosa_g2_3_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.13":
            verify_sosa_g2_2_master(doc, mirror, md)
        elif len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.12":
            verify_sosa_g2_1_master(doc, mirror, md)
        elif len(doc["columns"]) == 15:
            verify_sosa_d_master(doc, mirror, md)
        else:
            verify_current_master(doc, mirror, md)
        return

    expected = [([x["name"] for x in doc["donorColumns"]] + ["PROPOSED DIM ELEMENT"])]
    divider_rows = []
    for row in doc["rows"]:
        if row["type"] == "section":
            divider_rows.append(len(expected) + 1)
            expected.append([row["title"]] + [""] * 7)
        else:
            expected.append(row["display"])
    required(len(expected) == 28, "master not 1 header + 5 dividers + 22 rows")
    required(expected == mirror, "CSV differs from structured JSON source")
    required(len(doc["evidence"]) == 51, "expected exactly 51 evidence claims")
    required(all(x["sourceVerification"] == "PRIOR_SOURCE_EXTRACT_ONLY" for x in doc["evidence"]), "a claim was falsely promoted to original checked")
    required(all(x["disposition"] == "PROPOSED_NOT_ADOPTED" for x in doc["evidence"]), "unapproved mapping decision")
    required(md.count('colspan="8"') == 5, "Markdown lacks 5 full-width section rows")
    required(doc["display"]["finalDonorUsageRanking"] == "UNDETERMINED", "unapproved final donor ordering")

    with zipfile.ZipFile(BASE / (NAME + ".xlsx"), "r") as book:
        required(book.testzip() is None, "ZIP CRC mismatch in XLSX")
        all_names = book.namelist()
        required("[Content_Types].xml" in all_names, "missing OOXML content types")
        for n in all_names:
            if n.endswith(".xml") or n.endswith(".rels"):
                ET.fromstring(book.read(n))

        wb = ET.fromstring(book.read("xl/workbook.xml"))
        sheets = wb.find(S + "sheets")
        names = [node.attrib["name"] for node in sheets.findall(S + "sheet")]
        required(names == ["Master Crosswalk", "Evidence", "DIM Definitions", "Donor Sources", "Holds & Decisions", "Read Me"], f"worksheet mismatch: {names}")

        master, actual = data_rows(book.read("xl/worksheets/sheet1.xml"), 8)
        required(actual == expected, "XLSX Master Crosswalk differs from original JSON/CSV cells")
        merge_root = master.find(S + "mergeCells")
        merges = [x.attrib["ref"] for x in merge_root.findall(S + "mergeCell")] if merge_root is not None else []
        wanted = [f"A{i}:H{i}" for i in divider_rows]
        required(merges == wanted, f"incorrect section merges: {merges} != {wanted}")
        required(master.find(S + "autoFilter") is None, "invalid AutoFilter across merged section rows")
        view = master.find(S + "sheetViews").find(S + "sheetView")
        pane = view.find(S + "pane")
        required(pane is not None and pane.attrib.get("ySplit") == "1", "master header is not frozen")

        evidence, evalues = data_rows(book.read("xl/worksheets/sheet2.xml"), 15)
        required(len(evalues) == 52, "Evidence sheet not 51 records plus header")
        required(all(row[7] == "PRIOR_SOURCE_EXTRACT_ONLY" for row in evalues[1:]), "Evidence sheet source statuses incorrect")
        required(len(evidence.find(S + "hyperlinks").findall(S + "hyperlink")) == 51, "Evidence source URL hyperlinks not complete")
        for n in [2, 3, 4, 5]:
            root, table = data_rows(book.read(f"xl/worksheets/sheet{n}.xml"), [15,7,9,9][n-2])
            required(root.find(S + "autoFilter") is not None, f"sheet {n} lacks supporting filter")

        definitions, dvalues = data_rows(book.read("xl/worksheets/sheet3.xml"), 7)
        required(len(dvalues) == 23, "DIM Definitions has wrong row count")
        required(all("PROPOSED" in row[5] for row in dvalues[1:]), "definition accidentally treated as adopted")
        sources, svalues = data_rows(book.read("xl/worksheets/sheet4.xml"), 9)
        required(len(svalues) == 8, "Donor Sources is not seven original columns")
        required(all(row[7] == "UNDETERMINED" for row in svalues[1:]), "donor ranking prematurely finalized")

    print("PASS: GitHub-stored Step06 XLSX ZIP and XML parse; 6 editable sheets; 7 donors, DIM last; 5 full-width merges; 22 original proposed rows; 51 identical source claims; all 51 PRIOR_SOURCE_EXTRACT_ONLY; matching Markdown/CSV/JSON; 51 Evidence links; 4 companion filters; no new donor ranking.")
    print("LIMIT: source-semantic verification, original publisher clauses, complete DIM adoption and external CSAPI interoperability were NOT tested.")


if __name__ == "__main__":
    main()
