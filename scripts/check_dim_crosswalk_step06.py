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

def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

    if "review_grid" in doc and "columns" in doc:
        if len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15":
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
